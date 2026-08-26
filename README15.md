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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b76bda-e35e-3056-958f-d577f7566274 | -5.98437 | -43.74356 | 2026-08-26 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea5f716-3bdf-37ce-8a03-c18fda14b912 | -3.50538 | -48.03883 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 311f311c-caed-384d-8d8a-bbd2ccf58330 | -3.51666 | -48.03432 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce18fea-93e5-3ca5-8a36-cbf7e86599c3 | -5.73834 | -43.27457 | 2026-08-26 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 57328aba-4728-3e3d-97e8-39026dd8cc3f | -4.40871 | -42.14906 | 2026-08-26 04:06:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e79324c5-e48a-3706-9752-7aed841bed55 | -6.24259 | -44.79888 | 2026-08-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0fadb6b-cac8-3d9c-b6b0-2b188d6f244b | -1.55275 | -47.7051 | 2026-08-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf29ad20-85ce-39c6-97db-cc49c9a5dcab | -5.31148 | -42.79123 | 2026-08-26 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c285cc0e-2977-3afd-9b12-58c0fea5e621 | -5.31118 | -37.33204 | 2026-08-26 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84bdf442-50b0-3b1b-817a-a091bca1fbd6 | -6.46307 | -41.55484 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8380a9d-8dd6-3ff7-bd26-3d440374fdce | -5.9173 | -43.64171 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9b0268a-ce02-35a2-b21c-77c2a84bebb5 | -4.55984 | -49.51911 | 2026-08-26 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d9adae-9d5a-37d4-b5fb-e78ea5804ff2 | -6.85612 | -38.34968 | 2026-08-26 04:06:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec80b81b-0dd2-3f8e-8448-2df7bf16c78e | -5.658 | -46.95555 | 2026-08-26 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 194cc191-3f3d-3557-a550-e14372d51bc5 | -6.24287 | -44.80172 | 2026-08-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e2c7693-88b6-365c-bcfc-1900caae9015 | -6.91069 | -41.12085 | 2026-08-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b421180d-dc88-3eca-aca7-7580f43fb63c | -3.30592 | -42.77178 | 2026-08-26 04:06:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20e168c0-1cc4-38c2-9522-55a960d9739a | -3.37052 | -43.00134 | 2026-08-26 04:06:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f338636e-ee31-36b5-938a-6ed732c84160 | -6.61311 | -42.54711 | 2026-08-26 04:06:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29fb8282-b715-3b41-8933-9f7af329122a | -5.98941 | -44.04846 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 386ce083-c415-3e3b-8ec4-9f881b3f15cb | -2.49821 | -48.14027 | 2026-08-26 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b8420b1-7d94-3178-ad24-6cfe19bacaca | -6.454 | -41.56815 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 587e3b55-8334-38d5-a080-184ca156efe1 | -4.79979 | -43.17009 | 2026-08-26 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8abbaf46-7016-3077-9fb2-7540797089c3 | -5.65885 | -46.95287 | 2026-08-26 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52c855e7-9cdc-382c-93ad-258b6b62cbd7 | -5.00847 | -37.52848 | 2026-08-26 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12cca01d-c5fd-38aa-9f85-cecf1f0243c0 | -4.80345 | -43.17067 | 2026-08-26 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e9ea5df-fd23-3507-9b91-612491b3c4af | -6.36574 | -43.28445 | 2026-08-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643a3a9a-685c-37f3-98ef-1b405a7a0289 | -5.7412 | -41.52599 | 2026-08-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3836b749-f0f0-32c0-b4d0-a18024dd7006 | -5.59647 | -45.6546 | 2026-08-26 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f9bb9e8-4a13-3a2f-81c0-07e1c5fab759 | -3.54102 | -48.18547 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2838ac79-2944-3f88-90d8-41ea0fe924de | -3.53011 | -48.18698 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cf896f1-dae1-3a18-9459-1f46fe794039 | -5.73724 | -41.52907 | 2026-08-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c7debd0b-aa09-3819-be66-714184df382a | -6.56284 | -35.16874 | 2026-08-26 04:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 50b6e9c3-38e2-3153-9633-8cbeab5b7254 | -4.44662 | -43.85115 | 2026-08-26 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f3fcf05-3ac4-3f8d-8441-43d54f52b389 | -1.55326 | -47.70198 | 2026-08-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b207f251-ade2-3df5-aad2-ed05431f56cc | -5.84518 | -39.5504 | 2026-08-26 04:06:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e226f08-1818-3deb-88cb-56b92ec6be01 | -5.65426 | -46.95212 | 2026-08-26 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2eaae03e-87c0-3848-9f9f-fb14fb8623a1 | -4.84666 | -44.297 | 2026-08-26 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df8f0053-59b6-3625-9ce9-ab4f50a87168 | -2.79015 | -49.58247 | 2026-08-26 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f0e9b19-4ce0-357e-abe0-a906190c1ec5 | -2.7959 | -49.58342 | 2026-08-26 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ace3f187-2534-3816-af57-c2150a4d2257 | -4.8026 | -43.15298 | 2026-08-26 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06c2aceb-6a3f-33b1-8769-ae871e380544 | -3.32824 | -42.86601 | 2026-08-26 04:06:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f226cea1-5785-300b-abf3-6ba75e1eeee5 | -3.96745 | -43.10551 | 2026-08-26 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1811efb6-4a06-3be3-9247-c1dc8d2a51dc | -5.91657 | -43.64612 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88eacbf4-571b-31f5-a610-1b7fd3212fa7 | -7.12294 | -35.1152 | 2026-08-26 04:06:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b81782b-0bd8-3a5e-b21b-c8e5edead45a | -5.43927 | -45.19907 | 2026-08-26 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3570b3-56c0-35c6-8708-f1c36687ce0e | -3.36683 | -43.00075 | 2026-08-26 04:06:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b0dcdea-8ba6-3f62-b9d8-93b03c5af1b7 | -4.84975 | -44.30254 | 2026-08-26 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 595cbf0e-62ea-3948-ba3f-cd0b39a9d7e4 | -4.65057 | -38.46681 | 2026-08-26 04:06:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bd878344-3d23-382c-ae48-115fff51e1ed | -6.33028 | -38.73223 | 2026-08-26 04:06:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 634a0a9f-b756-38d4-a81b-5db3498d204a | -6.12879 | -44.07321 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63f54475-60bb-3d24-b804-a72bb9ad83d9 | -6.42728 | -43.86616 | 2026-08-26 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fd3c007-b887-36e9-826b-bc1feb123485 | -5.9272 | -44.97844 | 2026-08-26 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52616991-bc26-3c6e-9ea9-3c096ee3082c | -6.4603 | -41.55067 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ff3690a-0160-3fb2-bb6c-3fdb0b82ec3f | -3.5317 | -48.17766 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7895b966-4a99-3858-9dd9-0f58c1588481 | -3.53636 | -48.18155 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e39228ad-941c-373d-9ef0-54edca163e53 | -3.588 | -50.67824 | 2026-08-26 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a2d4ce6c-f27b-3fc8-9c15-f689b988dd7b | -4.80469 | -45.77195 | 2026-08-26 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df575ecd-76a0-385a-85cd-01b9fc2d1d8b | -3.53688 | -48.17846 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d03f31aa-023c-339c-a65f-fc61113b66ed | -5.98212 | -43.7454 | 2026-08-26 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccfb30a8-d292-35b2-8bdb-44c74ed615c4 | -5.77093 | -46.11585 | 2026-08-26 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a506125a-a767-3e03-8f76-baa1005d7f56 | -6.91346 | -41.12489 | 2026-08-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa68a1d0-631b-309a-b101-7182d946cc2f | -5.5958 | -45.65859 | 2026-08-26 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf5ee88a-bc22-3c18-8820-282225067b7c | -5.99697 | -44.0497 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c489e4a3-a99d-3252-b797-2881a96ce2d0 | -5.80541 | -43.63866 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9033a04c-dd93-3e62-8acc-fb8450ddcf46 | -6.56581 | -35.16926 | 2026-08-26 04:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be8672e3-c357-3391-a14d-223613d249db | -6.12956 | -44.06844 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5c7b852-1092-3fa5-a4f4-d930fb67c707 | -2.04645 | -48.04 | 2026-08-26 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9750378c-3d3d-3ec7-8b51-b31dc84f45c6 | -3.62289 | -49.7012 | 2026-08-26 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 512d7c28-08b9-303e-8a3e-6bb1ba4eb2f2 | -6.45854 | -41.56149 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bf0c94d-6c21-352e-8117-50a80a4304b4 | -5.92779 | -44.97493 | 2026-08-26 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c662286-420c-31a5-909d-92d2b13d6556 | -6.43392 | -43.87222 | 2026-08-26 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab27ce47-0a0e-36ca-9f47-44bb0747e925 | -5.62874 | -44.93998 | 2026-08-26 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31cf39e2-9281-33af-a5b7-6ba0ad3b34ba | -3.53583 | -48.18465 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d68a803-f9fa-3de1-a505-94402cd0e578 | -6.23893 | -44.80104 | 2026-08-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c945dbe1-0353-3a64-8637-5cac58093537 | -6.01274 | -45.80971 | 2026-08-26 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ebfc5fe-9b04-368d-8e3f-021a355c940c | -2.74814 | -42.79612 | 2026-08-26 04:06:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d90f69c-40a8-3162-b00d-3e98878014c8 | -2.8922 | -48.80511 | 2026-08-26 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2809676-9d5a-3a91-a512-768eae1fa083 | -5.39446 | -43.61046 | 2026-08-26 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8623b80-9359-37c4-8cea-4ab7c2e0b0e1 | -5.63333 | -44.93716 | 2026-08-26 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06f46176-a4ff-3e05-b879-9a5b5d3c5025 | -6.45445 | -43.09041 | 2026-08-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1da387-a6d0-3da9-9613-8189893adfe4 | -6.41483 | -42.78033 | 2026-08-26 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 83bd2b90-b91e-3a3b-a77d-cff1982d0843 | -5.921 | -43.64231 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b2ad5c5-1b89-38cc-aa61-64501b87fbdf | -3.96377 | -43.10492 | 2026-08-26 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d075803b-3b2e-32a7-9505-b6b393bf399c | -4.55922 | -49.5228 | 2026-08-26 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d71b0d3-6d56-35c9-a4e9-58cb73ea136a | -2.49874 | -48.13701 | 2026-08-26 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b5c27c2-2683-32ba-be0c-a4b77987b7a5 | -6.01208 | -45.81361 | 2026-08-26 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 135f16aa-f588-33c3-ac6d-ba460889bf93 | -3.62222 | -49.70515 | 2026-08-26 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd861d9a-6103-3157-922d-0f81f0c6649d | -6.89106 | -39.42184 | 2026-08-26 04:06:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 046af629-1706-3285-8909-f0147f1c3388 | -5.51677 | -44.11375 | 2026-08-26 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7846942b-f79a-3792-ae31-e7258d3df8ba | -5.33754 | -45.15935 | 2026-08-26 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb23dd01-43d1-379d-bb18-33eff92867c6 | -7.28326 | -44.085 | 2026-08-26 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9e75332-8a1a-3f7d-9907-e85fc9f9c21e | -8.07986 | -45.90257 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 409b06c1-35bb-3cad-a85a-aac7befb7b3c | -9.02104 | -50.77826 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1367990-6e7d-3dd2-af04-fbe3b5ebc33f | -9.03298 | -50.80748 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dc13269-9e0a-32a3-a088-12fd42354eca | -7.15633 | -42.81143 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3518a3a4-bf5e-37ea-a496-d0ce1bca2325 | -12.72674 | -48.38567 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f6d3b67-a0fc-33dd-98a8-09725d642a27 | -11.9683 | -47.75388 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0d72d5d-a0e4-3284-9a76-c99754b20def | -7.75432 | -44.75301 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 870d9811-a745-3834-9b5b-f86403993b1a | -6.83701 | -52.50223 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
