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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b5cf70d-f64a-3777-8b0f-b16b9dfe6997 | -13.0648 | -52.0115 | 2024-12-13 00:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3c91c337-3efa-30da-9a20-609691265f72 | -13.6933 | -54.7555 | 2024-12-13 00:20:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 23e4b6b4-1dc6-33ef-a555-c28d7089ce84 | -1.62 | -46.6747 | 2024-12-13 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 483e8626-5418-3f95-ab2f-74ae8ce5217a | -11.2148 | -53.833 | 2024-12-13 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 254c86a4-602e-3061-b7b9-993fa4f19944 | -11.1959 | -53.8348 | 2024-12-13 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 37b2114d-c37b-30cd-b0b5-3661b855af9a | -3.2686 | -46.9142 | 2024-12-13 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 516d33b2-4045-3016-a9cd-cf9b703a9546 | -6.9161 | -43.4952 | 2024-12-13 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| f2a7c494-44d0-36bd-a9fe-0038fa9abf82 | -3.2685 | -46.9362 | 2024-12-13 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 773b25c4-8169-3480-a0a8-ffcab8b3f422 | -2.8196 | -53.0832 | 2024-12-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 75e47472-e341-3736-8b4c-47a7806462b9 | -6.9158 | -43.5185 | 2024-12-13 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 93e2353a-d9cd-36ff-93ac-1f2a0b4dc362 | -3.2936 | -45.5817 | 2024-12-13 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3a690dae-b399-3241-a1ca-67bc56c505e7 | -3.1449 | -45.5875 | 2024-12-13 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 375bbce8-9ed9-3c1c-927d-16fbd9d2efc4 | -2.1173 | -54.6472 | 2024-12-13 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9a46d976-e51d-31d5-94cb-fe3fad453e85 | -11.1962 | -53.8142 | 2024-12-13 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| ac35adcb-2af2-32ca-9a85-291fcad9dd60 | -12.5495 | -57.7395 | 2024-12-13 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 43eb312d-b1ba-395e-a643-8cf2fb8d834e | -13.0641 | -52.0538 | 2024-12-13 00:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f7e88dfe-f009-3123-b937-d6805118bda9 | -12.5497 | -57.7196 | 2024-12-13 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c9665bd5-3b30-3276-aa9f-7e0316befbec | -3.3301 | -45.7146 | 2024-12-13 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 93f313a1-802a-304a-a667-57fbd15b2b0c | -11.2151 | -53.8125 | 2024-12-13 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bd34e504-a073-3c47-bf32-2861d6f2c2e2 | -2.4923 | -51.8027 | 2024-12-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 263.2 |
| d14b5bff-7aac-3a5d-8284-e89586bdd77e | -6.9346 | -43.5168 | 2024-12-13 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 99382aee-d766-3534-a36f-2980301699a7 | -14.7655 | -52.6446 | 2024-12-13 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e4b11ce5-cc1e-304b-9c5e-b6e454c12fc4 | -2.8196 | -53.0629 | 2024-12-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8b580da5-639d-3388-aadd-cad4d6a9957c | -5.2298 | -43.282 | 2024-12-13 00:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9ab07eec-0f37-3998-8ab0-3eb3db8150c8 | -3.4784 | -45.7979 | 2024-12-13 00:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a8f9fd3b-e4d1-3f38-b5e7-9186546d7cc6 | -3.13617 | -48.60657 | 2024-12-13 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8e2c5fff-63d9-3280-b782-c5c4ee892ce3 | -8.26508 | -48.02435 | 2024-12-13 00:20:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ab66368a-862a-31a5-bf2a-2c6f53337eb6 | -9.32094 | -35.99953 | 2024-12-13 00:20:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e9731c7b-43e2-33cc-a0a2-cb3a95587d7e | -6.93467 | -43.51256 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 4c9b6b31-4c7c-315c-8538-639405b1184f | -2.83747 | -42.28174 | 2024-12-13 00:20:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c200793d-4274-326a-94df-41d12d214f33 | -4.77118 | -44.42794 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82269f24-96e7-33cc-8636-15471aa1fac3 | -4.88169 | -44.40695 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 8cc17ce6-d4da-38b4-b94c-eb3c11ffddf7 | -3.00448 | -40.23078 | 2024-12-13 00:20:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ea43b52c-d185-3075-b1ea-b76e9e98f4da | -4.24342 | -41.93048 | 2024-12-13 00:20:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a1adbf7e-c67c-3950-9573-846c269ea86f | -7.21349 | -35.08632 | 2024-12-13 00:20:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| b4b6bae3-2836-395b-9127-ae2873ed5d3b | -3.18648 | -45.62414 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d75ab413-a665-32ef-b098-a7043c2345bc | -2.17916 | -45.8038 | 2024-12-13 00:20:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 46b088ef-5b81-38c5-9c9f-4acc5489a50e | -3.81308 | -44.12494 | 2024-12-13 00:20:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4ce3efe8-b77c-3a5d-bcb0-e1c42f43e2c7 | -3.07146 | -40.05125 | 2024-12-13 00:20:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| e86055f0-d2d6-326e-8f7d-8ff74238007c | -4.24216 | -41.92117 | 2024-12-13 00:20:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bf6f8e4a-f32a-334b-b80f-ef1e5c4e4226 | -7.63273 | -35.35687 | 2024-12-13 00:20:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 0f6bdc33-6e63-3808-aec1-c1179761a075 | -5.20263 | -43.2982 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9a3be066-153a-3876-9d69-bd5ccbc721d8 | -4.45619 | -43.74332 | 2024-12-13 00:20:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f841b30b-8c2e-3af3-b142-d0b860ea5321 | -5.21099 | -43.28579 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 747c6ec9-7083-3399-a4d1-467cb6eb73d0 | -4.53783 | -43.28709 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 09552699-d788-394d-96ef-265fff80b063 | -9.81435 | -36.28447 | 2024-12-13 00:20:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 7886e203-7070-31fc-931e-51ec004be476 | -2.30881 | -45.58002 | 2024-12-13 00:20:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 00bb1887-d6bc-3084-a2bc-132d906098e2 | -2.34541 | -45.84551 | 2024-12-13 00:20:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c22730e7-e845-39aa-bd17-e5c406de26fe | -6.09805 | -44.76149 | 2024-12-13 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 04a9b74e-ecb9-38bb-8c48-47f79008276b | -3.83429 | -41.56334 | 2024-12-13 00:20:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 2bd3da6e-59f3-31c2-a8cb-373285335288 | -9.92495 | -36.27231 | 2024-12-13 00:20:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 5bc30e72-1c93-3576-82bc-5cb5f90b6f54 | -3.48475 | -45.7992 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7f96ca17-354d-3b17-b9e8-825e213e8ef8 | -3.7001 | -42.12548 | 2024-12-13 00:20:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 94cdb38c-8563-3bd3-b7a7-180f55ea3322 | -10.47526 | -40.26025 | 2024-12-13 00:20:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f97ed476-943c-31c6-88e7-4fb0d6efcf0d | -2.2971 | -45.74546 | 2024-12-13 00:20:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ebf41d03-90ba-36a9-a617-ea4345ada724 | -5.42972 | -37.85798 | 2024-12-13 00:20:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| bd53db56-aeeb-3068-aeda-03d26a75989d | -3.28517 | -45.58913 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f1a82e64-93c8-31e2-96f5-bd386ecb8eca | -6.7428 | -35.08939 | 2024-12-13 00:20:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 5cad5ccf-0b87-30d0-ab8b-48b35f765089 | -3.35786 | -42.31269 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 119f01d9-cb1a-3733-9222-1f706969202e | -3.26893 | -46.94154 | 2024-12-13 00:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e2435544-1328-3e85-8967-2ec075465590 | -3.30526 | -43.54216 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 74e10764-d2c4-3f96-b87e-1a5505057722 | -7.4351 | -44.73864 | 2024-12-13 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a70f9fb1-6ec8-3202-9291-f6421c33ed46 | -6.13859 | -43.9563 | 2024-12-13 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e7b5506b-0ab8-3d05-b2ea-4bfb4fd6004d | -11.5198 | -45.0128 | 2024-12-13 00:20:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 551abd42-0ab1-3ea1-8d11-6fe6204c50f0 | -7.63638 | -35.36491 | 2024-12-13 00:20:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 333cfe7d-e5a9-3a0b-8b0c-339271296a67 | -5.24111 | -45.1301 | 2024-12-13 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0b499b30-45a3-34dd-aa28-59550ee6bd0d | -4.55511 | -43.57238 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2a7591f8-66d7-3912-93a3-d6ac2dd1e91a | -3.14404 | -40.05008 | 2024-12-13 00:20:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d7d0f3f8-b434-3460-a69b-282376f7d6c9 | -6.0828 | -43.54218 | 2024-12-13 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 75b58d8a-db13-3b35-9792-46910595b18d | -1.5807 | -46.04557 | 2024-12-13 00:20:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d1036d4-4ad6-3c5e-86c6-b7c99069d97f | -3.14937 | -46.35709 | 2024-12-13 00:20:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| da4f9e8a-6bbf-371a-b5d9-0def47af94d3 | -5.76248 | -40.9986 | 2024-12-13 00:20:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 9b6a1141-b99f-3979-90b3-04528e9a69da | -3.13654 | -45.59082 | 2024-12-13 00:20:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7f6cb793-d9e3-381b-93f8-60ad80e12759 | -6.09584 | -44.75354 | 2024-12-13 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f32fcb3a-6041-305c-9cd6-93f65b8b7985 | -10.85146 | -37.12267 | 2024-12-13 00:20:00 | TERRA_M-M | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| cd85c124-d8a8-3765-8e27-7e57d0aa19b2 | -3.18449 | -45.60916 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bf1eb33c-d240-330c-b77a-da963c16e43f | -10.66689 | -44.71864 | 2024-12-13 00:20:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 76f9d0d9-3bb0-3fe1-9110-16d1d3ae8c02 | -3.28717 | -45.6041 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f998aa07-7ea6-3daf-829b-77e8291a5001 | -4.76486 | -44.42186 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 52899b28-4a26-3404-891a-f9d0d9dbc134 | -5.46193 | -44.80226 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0bda2848-f6a5-3a5e-bebe-9afd1d3d9fd7 | -3.35655 | -42.30325 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 793ed07f-aa62-3843-80ac-094bbbd1d0f6 | -6.3815 | -35.4409 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 039901c2-9079-35e3-b2d8-3e88f07eb828 | -5.21248 | -43.29676 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| e3faa92b-8776-3cea-9c63-3f54001c04b7 | -6.08121 | -43.53042 | 2024-12-13 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2db5d6df-6e6f-32af-85c3-38b59119d4cc | -9.82254 | -36.27159 | 2024-12-13 00:20:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 297a809e-918c-301f-af72-4bfe64223275 | -3.26643 | -46.92252 | 2024-12-13 00:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 7e16e178-c00c-33b8-8d85-75b96cc0be55 | -7.78965 | -37.61145 | 2024-12-13 00:20:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8b6054a8-5999-3887-bb95-01103f7d4301 | -5.4499 | -44.80967 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2574b50f-7615-34f9-bfac-1e398e1c460c | -6.27127 | -38.90071 | 2024-12-13 00:20:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bbfc7d70-7a51-357c-8de0-fd290126b8b9 | -7.21235 | -35.07706 | 2024-12-13 00:20:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 491.8 |
| b665617b-1684-3803-ad66-2b9308657162 | -5.82814 | -39.2197 | 2024-12-13 00:20:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2dabc680-61aa-3d27-baea-0f34953fc05e | -7.63479 | -35.37089 | 2024-12-13 00:20:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| df4d2fd7-1a23-3102-8281-91e5fab8bf17 | -4.31416 | -38.49091 | 2024-12-13 00:20:00 | TERRA_M-M | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a2a6a200-bf95-35ce-8cca-7b8d4f029abf | -10.71595 | -37.19635 | 2024-12-13 00:20:00 | TERRA_M-M | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1a10280d-c997-3fdb-a12b-347aa3107ebf | -6.21923 | -43.95224 | 2024-12-13 00:20:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 10793e72-a68e-3f48-8011-143070380bec | -2.31079 | -45.59439 | 2024-12-13 00:20:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9ff41ac6-b798-31d0-ae9a-768253a6a171 | -3.48588 | -45.78958 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 8eccaed9-4f6f-379c-9938-969bc10f6a94 | -3.04328 | -44.47121 | 2024-12-13 00:20:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15e96b63-560f-3c5f-b61d-7023de6c6d2a | -7.21118 | -35.07141 | 2024-12-13 00:20:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 559.1 |
| 89668014-6178-3140-9d25-745439dcc4d7 | -6.09781 | -44.76797 | 2024-12-13 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README3.md)
