# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41c05c4b-b7b5-3d1d-9dd1-e994c16a79e9 | -5.15703 | -46.07813 | 2025-09-29 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40f65bdb-7570-3c9f-9821-bea54b5076d1 | -9.35686 | -51.48761 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8014a7-85c4-34bc-8168-5e402287b71d | -9.79447 | -46.93787 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1263bc4d-33fb-3cc0-af3a-badb70dd43b0 | -8.82348 | -46.20023 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 086fda3c-fc98-3990-972f-501d58d9516a | -8.30423 | -45.50716 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| cc995b55-29bd-38ef-aac1-953e94080599 | -4.26274 | -48.55643 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9cea67b-54b6-3976-91f4-15208da6217d | -9.77444 | -46.17746 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8c5a015-9ed8-3a9c-aa75-92c8198f7e6d | -9.0576 | -46.71435 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7feda368-830d-3d5b-aa9f-e1741bf0e3b7 | -8.91238 | -46.08496 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3eba260d-1443-31fc-a34b-9843a6e90b1b | -3.81116 | -51.34407 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a543da6c-70ce-384c-afde-6a2db1c428c7 | -9.40409 | -54.69392 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9c4174d-afc0-3608-95c0-0e414c2dc315 | -8.27644 | -45.51155 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 244285d3-d763-3f25-9760-ecfda7f20022 | -9.31092 | -49.82399 | 2025-09-29 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5433072-d473-3f1a-a5a9-3eafbf4057d4 | -4.71575 | -41.98295 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56488f1b-ebbb-397e-87aa-096b65fa1bfc | -10.40243 | -48.11433 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd1b09ad-f065-3299-9755-ea52f482f9ae | -7.22904 | -44.78973 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7d643a06-9cbd-3ef8-b9d8-afe7b96b023c | -9.56065 | -54.58718 | 2025-09-29 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20c8387e-40fd-37d0-9fe8-c6a2cbd18bfa | -11.42219 | -44.90972 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc57ae73-9d81-3ffb-ab56-c142bc3084a1 | -9.40192 | -54.70781 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f3c9910-fa00-3214-b5b3-24ec041f81eb | -8.44025 | -49.12746 | 2025-09-29 04:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678c1865-5008-3e7c-8382-3072d60ba273 | -10.40841 | -48.14003 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5181d875-8091-3d4f-8a1a-15e3d47ddd2c | -8.1485 | -46.40041 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93c41128-d9a9-3d1a-8a0e-b97bfda37292 | -9.0592 | -46.73178 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5496335-9950-320f-8086-8b57dfe0a01c | -10.39283 | -48.15156 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57e5ef36-0ef7-30a1-a6c2-534c1087e658 | -9.39863 | -54.70729 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a7b6ffd-bc69-3690-8cc1-ffccf1f391c1 | -9.42144 | -54.71791 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ea8e735-1ba3-35e5-91e1-8948cc5f2d2b | -6.62187 | -45.89888 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5849180-5bca-3c32-91b9-b73d5cf52b93 | -7.80873 | -46.89799 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96aa237e-41c1-3575-b685-145eaa291a9e | -8.16465 | -46.39439 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68f963b6-ad94-3fa7-b064-39a2e7b99f37 | -8.86866 | -46.59625 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63b42a0a-f494-39dd-b5f2-bc45fdaf6521 | -9.40025 | -54.69687 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03fa465c-3a09-32d0-bb4f-044793a62abb | -6.62184 | -44.95222 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05f9f2a4-f476-31f7-88c6-8de29dc38914 | -5.74017 | -42.67421 | 2025-09-29 04:57:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa6f6768-638f-35af-9c87-6381df04cca7 | -5.73962 | -42.86636 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2781fcc9-53c3-3a86-bf6f-f72b3fa9f981 | -8.25252 | -45.48629 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66e2b01a-d284-3f66-96a4-da1341d0815f | -10.68066 | -46.7536 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c973d195-179c-336b-bbc2-4210c6eb23ff | -9.40739 | -54.69444 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a75ae9b-b548-3115-83d1-0be6f5c34af9 | -8.25385 | -45.49093 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 664f69ea-3bc6-31dd-a11c-cefceca07205 | -8.2574 | -45.49066 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fae4435c-8ef9-3b7b-b4e7-f9ba2e1c3ba2 | -9.28522 | -45.73082 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b4dbed7-4d81-3326-87a3-fd1f04b1b945 | -9.41399 | -54.69548 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b5aeb32-bdd9-3089-b646-1af771837572 | -7.22451 | -44.7816 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 84516ab0-3baf-3217-9ed1-160195c7d3b1 | -4.39279 | -47.28299 | 2025-09-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 497d557a-cd01-36e4-86b5-5e6fe07807e9 | -10.82441 | -47.93845 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cac4b5dd-c0ad-38e2-b2af-3b45804aff09 | -10.0463 | -50.40551 | 2025-09-29 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f58bd32-797b-3a00-a983-56240399f3ef | -7.74623 | -46.99648 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b9fa39a-733e-3d62-bab7-1529e5b4754a | -5.96508 | -43.27242 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c10b85ad-f216-3b21-a0c4-a6a8d0da8b2b | -8.00094 | -50.86536 | 2025-09-29 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c3ea78-28c2-36f0-89cc-1b16e1370c25 | -3.89043 | -52.08092 | 2025-09-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad012fe-2591-3619-9620-4dedc0043592 | -6.62679 | -44.95647 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7420255-f994-325c-aba4-e27949c9562e | -3.83323 | -52.3621 | 2025-09-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df71b9c5-4a99-376f-b5d2-56890db77586 | -10.8172 | -47.93952 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4bbcd6e0-24c5-33c1-9d20-246bba673067 | -11.40543 | -44.90185 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba1a24e8-dc3a-32cc-a041-019724b10dcd | -4.70865 | -41.98718 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 41611a57-b0ad-372f-96ce-b6f47a6ba1c9 | -8.27817 | -45.49837 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 114a1148-6c7c-30b5-8355-02e699d5934e | -5.82409 | -42.79507 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 01b4a8f9-93dd-3d37-9cd4-846bec1ffb57 | -5.81854 | -42.78959 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 49739212-1cfa-368b-884d-6b24dcb7dbd4 | -8.67053 | -49.93585 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a225ec01-02f2-3d68-8c26-74fe48751657 | -4.29003 | -48.26662 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2cc4b14-d8b9-3e6d-a178-c9baf0b2bfff | -10.81501 | -47.93736 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 775b313e-346f-35bc-9240-476bd3bdb932 | -8.15349 | -46.40137 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1b7b9322-80f9-373c-b49e-ae2dc12951d8 | -10.1799 | -52.57275 | 2025-09-29 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738204de-5e7b-3430-a2f4-1cf0f67e6437 | -5.61466 | -43.35891 | 2025-09-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9e8d8b73-2784-335b-bbdc-61a91df197e6 | -6.42976 | -43.50497 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43244409-c42f-3670-9088-084f73e4d1f5 | -6.77298 | -45.61736 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b697182e-ce00-3320-a87e-f8924298385e | -5.88794 | -43.30156 | 2025-09-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b61e1aa-119f-311d-9685-7c83858bc8bf | -10.82767 | -45.39447 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6696f64-a74f-30cf-ae6b-bc6e05b92d66 | -10.04186 | -52.10469 | 2025-09-29 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1e620ec-871c-3dc6-a5c1-775f062ac590 | -10.80314 | -45.3643 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 509da258-e32a-3f41-9c27-362cd5475d48 | -6.46859 | -44.22002 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d548851-2e01-388c-aaf2-8752096a7e9f | -4.52223 | -50.52722 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4de3f5bd-93b1-3b1d-9699-ef3c3bce8878 | -5.82079 | -42.82204 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 146c9c82-3d37-3260-a950-4d69b7ebc8a2 | -11.48899 | -43.21586 | 2025-09-29 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 493c35c5-cd9d-3932-94f8-2b4665c320a0 | -6.57146 | -43.42689 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74054ef1-5fa7-31c5-8b55-8dafd049fd0a | -9.41344 | -54.69895 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c96d098-b9e3-33f0-ae7e-8cfb40ac6c2e | -6.89763 | -44.53068 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfb159e4-3e15-3e4b-a23d-c921bc534c2d | -5.67346 | -48.28138 | 2025-09-29 04:57:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d507ac3-0754-3135-8b81-5cf0e7f198da | -9.40852 | -54.70885 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c4e9273-7a31-33f4-b61e-dbb79b9ba8de | -8.29541 | -45.49155 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0858a4da-e3e4-3b40-9816-a15d7c4e0f74 | -7.55475 | -46.2921 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22f54bb6-323a-3878-aa4d-885ac1694810 | -6.91442 | -43.999 | 2025-09-29 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a61d441-ebd2-38a1-9370-28e171c07933 | -9.54981 | -47.76882 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d545b34-3eff-3897-93b1-1783b391b046 | -11.27409 | -47.18544 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0a18a8fb-53f0-321d-88e5-a606c3e7d194 | -3.08243 | -52.92596 | 2025-09-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc57fe3-9983-3ead-9eb0-a69406ed75ff | -6.45416 | -44.02765 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fdaeebe-47f9-37fc-86da-4c62e42b5bea | -3.84534 | -52.2836 | 2025-09-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da1ce6d-6dce-3756-b745-87f148ec1cd5 | -6.46263 | -44.00832 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 758a7b36-fd50-3275-9bc8-7f0a777b1703 | -9.06035 | -46.73204 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68a5aab4-a792-3a08-9c14-2c1f51d65f2a | -6.74436 | -44.74831 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92f60e7a-be10-3b43-9a4d-7f48f271ecad | -6.40219 | -42.82538 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fb257f8-6cf4-3904-ac87-d450b13de252 | -9.27948 | -45.73326 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8858326e-6efd-3b05-b3cc-0507b4d31d1a | -5.90815 | -45.84584 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38f79800-8abf-31fd-9413-2487fc978917 | -10.82191 | -47.94003 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d4c019b5-965f-3314-8775-16ba6a7c0c76 | -5.76847 | -42.83802 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 06dfabfb-9853-3620-b54d-73fdfcd3e4b2 | -11.36745 | -45.06434 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89686c85-3435-32e6-a7f8-00020c5be1bc | -10.4653 | -48.20336 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2078a46f-3239-3e8b-87dc-48c51a4b5b25 | -10.80822 | -46.67508 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f1aedc6-bd25-308c-9bb4-05e5760cce15 | -9.7764 | -46.20383 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e19b650-48fe-3447-b789-f6de66700fac | -7.91075 | -49.20007 | 2025-09-29 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61103b49-d0a6-3645-9495-f0ae08d48b9d | -5.74079 | -42.66953 | 2025-09-29 04:57:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
