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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4561553-8695-39c4-923e-d139c448fa5e | -10.81549 | -43.97803 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4cc5d9e1-4322-32d9-b6a6-00149ab1b145 | -7.49515 | -45.12648 | 2025-10-13 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f214273a-9e48-359d-9aed-7ccaf52bfb9d | -10.80991 | -43.98271 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f67eb83a-72f1-3b7f-a96c-609840287d5d | -7.55669 | -43.84158 | 2025-10-13 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1123e64-c4cb-3f69-86fc-7fa6d30c17b5 | -7.28655 | -41.9616 | 2025-10-13 04:44:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3cd21fea-fb59-3ee1-ac2c-501bebf907c5 | -4.65714 | -46.29057 | 2025-10-13 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c3097b0-68c5-3c82-aa26-a6f3dae336f9 | -3.58831 | -47.2836 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 33d61ec8-0b3a-39b8-a9ca-198121cb08eb | -3.81789 | -45.7651 | 2025-10-13 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af6a2da0-8b69-3217-9e17-1dddc8f127de | -3.60986 | -48.91395 | 2025-10-13 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 402205d0-e34e-3ebd-a7f4-4a26aa61f165 | -7.64554 | -42.58127 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0252a8a-81fa-3940-9d5e-883a5ac7c7e7 | -7.80273 | -42.44543 | 2025-10-13 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4a107e3d-7729-3f2f-af50-32d4cd705b9f | -8.21276 | -43.32552 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7741d6ff-ac7b-32c4-aead-4044c659a1dd | -7.92076 | -47.21802 | 2025-10-13 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b319d9e1-0dc7-3251-9a86-99ef1214efae | -4.83198 | -41.48309 | 2025-10-13 04:44:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd8e2ea0-c05e-334e-9136-1f7536092de5 | -7.31834 | -44.75554 | 2025-10-13 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ed482e7-b4c8-3554-83f2-02995a401f4c | -4.11376 | -50.05335 | 2025-10-13 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c830db-1fa6-31c3-b752-ecebd594e900 | -7.78492 | -44.05502 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 358e2e1a-8961-3888-8c85-9eeb9f4b7b4b | -5.93425 | -40.89145 | 2025-10-13 04:44:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8aaa9b8a-e94e-3ce5-b91b-f4bdc536a385 | -6.73823 | -42.08686 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c304e616-6590-3437-bb5d-1865adb47cc4 | -2.96111 | -51.51624 | 2025-10-13 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504a2894-708f-37b4-91cc-67bf19e90c12 | -2.87827 | -50.73444 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82433104-4425-3169-a985-cbff3de95216 | -7.48872 | -42.15753 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6d1af91-c554-35fc-a1d0-f29d0ce56ae3 | -7.79799 | -42.44152 | 2025-10-13 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55a404d0-c44f-31e9-9b66-f3f28a281416 | -3.38587 | -50.16783 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de6405ce-f447-3adf-8f73-69cdaa247df1 | -7.54803 | -46.09311 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d120436-98bf-3b39-9c6f-abc87beba2b2 | -7.5102 | -42.15727 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f30f280-631a-31d4-bb6c-d251a8198019 | -7.34914 | -43.85765 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e39b1ecd-14c5-361d-88c0-6db5e57f3acc | -6.6316 | -44.65941 | 2025-10-13 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51603c0b-70a4-3993-a940-3cadef974a74 | -7.34586 | -44.08481 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dec5509d-2fd6-335e-8b8e-d583aec702a8 | -7.49705 | -44.6355 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eed126ee-3f8f-3c8a-a948-365cd3348dd0 | -7.49487 | -42.15169 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c850e09-181d-36ff-8c12-ca5f9e62b1cc | -6.73376 | -42.08083 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 852d3ab5-266d-32f3-8a10-4acccd6b1805 | -7.50056 | -42.14923 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a5baff8-2519-3043-b70b-9ca5cb297a2e | -7.68815 | -42.38318 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac1496ab-5772-3b82-85eb-64be7985be9d | -8.45382 | -46.12317 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4df57a26-0531-312a-ba39-73031ab3be68 | -4.30304 | -48.10742 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f6fe4d1-4f4d-3967-a082-d283720d4839 | -3.12511 | -52.00386 | 2025-10-13 04:44:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18018ec5-328a-3899-8b9d-3218f5067717 | -7.34519 | -44.08954 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bde71357-c757-3e4e-b342-c2ad0789fd9b | -2.88491 | -50.73549 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8d5abdd-b058-382e-81e1-1965776156f0 | -6.58214 | -44.38028 | 2025-10-13 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27720ce9-9987-343a-bd65-89c35d4e0c21 | -4.3065 | -48.10795 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e9eb41e-b08c-3cf8-a47a-e4143cbb9ba3 | -6.58659 | -44.38092 | 2025-10-13 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e57de62-2ec6-34d3-ba1d-919456d3c3c3 | -3.09678 | -50.383 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d24fffdd-4f77-3600-82ce-036992bacd21 | -7.49324 | -44.6305 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4a5172a3-6556-37fd-b082-f27b17b42fee | -4.84796 | -42.75038 | 2025-10-13 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3d93cd1f-f3b5-3f21-b9fa-9c0cb73dc38d | -10.80154 | -43.97097 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7557112e-feaa-37f4-ae11-4ec3b8035fa1 | -3.07145 | -49.38037 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0273c84-88ab-3b45-9aef-d15ffdfa0ad7 | -2.98894 | -50.29205 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ab6ef3d-2845-3861-a0e8-e736d0ea9085 | -6.57592 | -45.9757 | 2025-10-13 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f2af8ea-aca5-3b26-a663-c91559676a00 | -8.45432 | -46.11962 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e312329f-7e1f-343d-ba01-812b7a2ad3a4 | -3.1349 | -50.20573 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65a863fe-955f-38e4-9d5a-b4715f3b312a | -5.04666 | -49.88772 | 2025-10-13 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 288b8336-3277-3564-ae58-fba2441fecfc | -7.34114 | -43.85994 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef791493-875b-3aac-a0de-7ebcad76bc4f | -3.61322 | -48.91447 | 2025-10-13 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61740d88-26b7-3c0b-8651-c53b9d1dad81 | -7.79756 | -42.44466 | 2025-10-13 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa1fb429-6916-3d2b-bb70-d05283f8059f | -10.80362 | -43.95506 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2cc8bd0f-055f-3a5a-9cfd-df8344e843f6 | -12.38978 | -63.87881 | 2025-10-13 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31d84f0f-952d-31cb-8fb0-9d6e82f61b97 | -14.30817 | -51.54369 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a66c802-9c9c-3c54-aa9d-b9cc80250c1c | -14.31319 | -51.55565 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d2f8901-fe49-3963-b931-ec07e996a3da | -9.88459 | -60.36128 | 2025-10-13 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45258186-ab48-3550-9856-61f29a56bd29 | -14.21766 | -51.51484 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 035c8b42-759b-3c0b-87fb-0ecf0f9fdc4b | -17.34142 | -53.81291 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3866dc3a-1b4a-3697-9e97-49c9bba6055c | -16.21452 | -59.12901 | 2025-10-13 04:46:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 801d8f5c-f612-3483-b427-a9c729e196e0 | -13.49528 | -51.29322 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df5aa129-e1bb-38d9-80e6-51816ee54271 | -14.26909 | -51.50763 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42521483-b0d1-37d2-9d22-7d1a62e0ec97 | -12.78744 | -56.96597 | 2025-10-13 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a546633c-1564-37ee-be0a-4ae08eb1d257 | -14.273 | -51.50453 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7519a384-2d6f-30bb-98d6-1ace92295037 | -16.76476 | -42.31121 | 2025-10-13 04:46:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fd87d8ac-d7e6-36e9-8094-609799033035 | -14.21821 | -51.51122 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cedc31a2-4e75-383d-920b-e6bad40b0e6d | -17.67234 | -46.96589 | 2025-10-13 04:46:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b42203b-0516-3c3a-bf8f-0d6fe72d550e | -13.88277 | -45.48439 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd2c7a50-cc66-3510-9629-0b6c86749b68 | -17.3381 | -53.81234 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aee45638-25a8-3b79-9bad-78567a23708f | -14.30929 | -51.55875 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d8ea9db-b602-3010-b677-9b10a046efd3 | -12.75871 | -50.6652 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a069cde9-b375-3d71-8bb4-47ed3ff0c6b7 | -14.21319 | -51.52156 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43792fea-a90e-36a4-a46a-30f27f279f54 | -13.50142 | -51.29792 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50a218f4-f490-3830-8cab-c6a74b77c9b2 | -13.50681 | -51.2985 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d6f25ef-ed05-350f-bd7e-5b90396358b5 | -13.86481 | -45.4429 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffe141e0-a14f-3a8d-bd09-cead79dad846 | -14.26295 | -51.50292 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e38c0596-b56a-3770-9cb7-2a51611f5ea9 | -16.12643 | -53.97362 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2c2807ef-b0ec-3f0e-b330-c48ef5087954 | -14.31152 | -51.54422 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 429a5e1a-309b-357f-afe2-5c7460362471 | -13.84262 | -45.542 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4770aac1-1269-3016-81c8-cffc7305eb5b | -11.73621 | -64.96069 | 2025-10-13 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50a54dc0-0256-36d7-953c-018b319e160f | -9.82249 | -62.19421 | 2025-10-13 04:46:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a194b32-6d62-35f7-943a-39d598366a7a | -15.85057 | -56.75708 | 2025-10-13 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6cc9a0e-0f01-3610-81d2-024726c74a8d | -14.27806 | -51.56116 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 849fd943-4d3e-3eca-b6d1-b3812b5a5fcc | -16.12585 | -53.97725 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 70bbdb70-b0da-3128-a2f3-c786a2b05dde | -16.9049 | -43.95511 | 2025-10-13 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c61e72c1-d3a4-3198-9070-dd48a7d49ad4 | -11.14765 | -51.28442 | 2025-10-13 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93d2c864-3cec-3485-b711-9f10130d05b3 | -17.32759 | -53.81423 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68ebdae7-8180-354f-bdbd-5b38db6f563f | -12.73837 | -50.662 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 952a759f-071d-3b25-b3d3-050b2eb24afb | -17.32932 | -53.80336 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0caa8df-e1ad-34b7-89c1-3eb7d1fcde1f | -12.74571 | -50.65936 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d7cb08-d339-361b-a162-694ba0046d88 | -14.25965 | -51.54704 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ea30a2d-1b61-3fa9-8fbb-c712a7d30bb3 | -16.12135 | -53.98395 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8424c9a2-b25c-3701-a070-97a361712abb | -12.39076 | -63.87403 | 2025-10-13 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 371d03c4-070a-3fd9-904a-4afb68e785a9 | -17.33205 | -53.80756 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e24b1e4-8245-33f8-a0c3-b350395a0d9c | -17.32096 | -53.81308 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb7bf798-a57b-31ec-89db-7c2c63da1671 | -17.33047 | -53.79613 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 847b79f2-3749-32fa-8732-b9d9ebb63225 | -12.95361 | -46.99118 | 2025-10-13 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README31.md)
