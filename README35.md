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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0327fe0c-4741-387b-9a79-b34c57da0bae | -8.10154 | -45.33341 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9a26f697-9d90-33b8-8c10-27e5decdf7c9 | -13.27491 | -46.81254 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ec8d791-d2bd-3ebe-86e9-1e25c6c6f2e9 | -8.02808 | -44.77535 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 895fd312-63a8-3dcb-b817-518bb0543f6c | -2.91368 | -48.6722 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5812a30-1153-316c-bf04-bf7f06634c24 | -15.17992 | -47.99026 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c282b54-c617-3a0a-9cbf-414950589d34 | -12.6403 | -56.98389 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 234c4ccd-63e3-3cb0-8a60-82256b73d706 | -3.24123 | -50.80788 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 91beee98-e286-3c5b-95b1-f97028db74c9 | -7.72946 | -50.32796 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 564be3d2-4ef8-30a0-a670-f487416c69c2 | -10.06875 | -48.065 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee28f955-e11f-3688-a18c-a2b028ac43ae | -14.57504 | -48.03474 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eefb297-de27-3a0b-9998-ed249d10e655 | -6.20479 | -44.18634 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca019a37-f136-31ae-bc4a-a6c08935d6aa | -9.44357 | -49.44867 | 2025-09-06 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad07fe7d-cf82-3a02-a213-226b20c17dcb | -6.21353 | -43.53773 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51aef64d-b0b2-3a16-954b-b6ff5dce1ccf | -12.49716 | -53.86063 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8807d935-fb0f-323f-b205-fbc98e2445ca | -9.44778 | -49.44947 | 2025-09-06 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6021764e-ef93-3a7a-9429-29dd26b2e3b5 | -12.96059 | -54.80949 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be7e2ac-0a73-3bc6-807d-a89e352b1c34 | -7.26074 | -41.89229 | 2025-09-06 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 43eece2a-fa0a-3783-85bd-02c7052d7013 | -6.23309 | -42.64394 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 85c1271a-a877-3998-9b0a-d1b80daffa03 | -5.84764 | -46.10873 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66855876-c508-383c-a3bd-a2d3d72c68d9 | -8.34965 | -52.54591 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59c18d2b-a616-3b65-a978-1e5b45ae8b37 | -12.96219 | -54.80155 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c23a4ee9-8e1b-3519-8f59-a7e3ef0150d8 | -6.30061 | -44.39282 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d13d38e-fc4c-3d77-8c97-ebc879b4738c | -7.73214 | -50.31298 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0b1076d-075d-35ec-be63-9bc26127bd28 | -13.9277 | -53.99681 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7085f87b-1c41-382b-902b-1fedd57c4676 | -6.20688 | -43.57957 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 829ee1bf-6043-3075-a8a5-bd7bc88eea5f | -6.66677 | -48.39676 | 2025-09-06 04:17:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d99d12e-f61b-3cfd-ac69-b5c6a36d3a58 | -10.03606 | -48.1297 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07b40aac-aa22-3a8b-a755-8c437ed44608 | -14.8011 | -48.11084 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b752f10b-eadb-3cb5-979f-44f2182b08cf | -5.72411 | -43.91369 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a5beafd-b39b-3951-969a-0645b792938d | -5.85186 | -46.10784 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd533020-de42-3c10-a3fc-01d3a4eeec44 | -3.31589 | -48.70823 | 2025-09-06 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 571c3f4e-b25c-3a1b-84ab-3f2f772ffca9 | -12.95334 | -54.81635 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba3b1b69-9cf3-3edc-b36d-8b115987aa28 | -7.34452 | -43.95803 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e448024-33e6-3a24-b9c9-6a8d3ee8dc24 | -8.69392 | -45.27965 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 565756ae-8eef-3988-9937-953365c8a697 | -8.45408 | -45.0338 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 962ed3b8-738f-3cd6-922e-f0e3c516a2a9 | -12.97994 | -54.83015 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 414ba843-8c43-3c5a-a2c7-9278893eaec0 | -9.82762 | -46.54144 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e245ee7-07f2-34ec-8cf2-800925f5c103 | -12.97102 | -54.81604 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d40d7e-3e73-3005-8acb-7173fee7898e | -6.27898 | -53.4385 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a8d81b2-5b46-30d7-a4ca-426767c9957d | -8.34792 | -46.94935 | 2025-09-06 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d578edd8-fba2-3a20-b025-807012b205e6 | -10.30795 | -46.34552 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d000a767-14ec-3e1b-8117-4a12ae8418ac | -8.10276 | -45.32585 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 862eefc0-a018-390c-b9a4-aceffbe976fc | -6.50551 | -42.4183 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| afe58196-9f36-3fdf-89ee-49addad2c549 | -6.80767 | -45.65575 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6880d83f-d836-3815-bc9b-9c1a64e5a27b | -16.91975 | -45.75501 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c3ed48fe-dd7a-3001-9b77-883dc16ad03e | -3.2375 | -50.80778 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2a06dc9-4b87-34b5-be14-cd0fa2281814 | -5.97451 | -53.60431 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 779ab45e-a56c-3b25-8c86-f1c27001262f | -6.14992 | -43.19276 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48c14663-dce5-3b61-a41a-09b1bc8406fe | -8.51732 | -51.31517 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76f8b97c-3448-3dae-862b-88d860a4e4f6 | -9.30805 | -45.41258 | 2025-09-06 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 286d81b4-3bf2-36f5-94e4-b5c19b3cf55c | -9.0126 | -49.7999 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2659e53f-37a7-3844-a78b-a27c4bc1e6f7 | -6.22462 | -45.6264 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb7be21f-270c-36e4-a46c-26c7a4e84d80 | -6.87468 | -45.55436 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2a5b11a5-fc60-3346-9ace-e0942488a41e | -5.70328 | -45.14655 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9f8eaee-a682-30f9-976e-853c04342b27 | -6.30898 | -44.57969 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58d75779-c3f2-3ef9-b667-e63811b07354 | -8.08056 | -50.19979 | 2025-09-06 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe693236-6b9e-3ee3-a16e-0ebe08bc3100 | -6.51474 | -43.06842 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11719425-4fca-3304-bbf5-7067da0fcbff | -8.08685 | -45.3153 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 082b4a9b-bea5-3820-810e-9da67c8730aa | -13.66327 | -46.95634 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6061be32-efa5-3082-82aa-8065e20bf888 | -6.72914 | -45.91704 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea99aa2-c2a5-3011-aec7-39f9a23a16ae | -5.72648 | -49.28792 | 2025-09-06 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a3d4707-473e-3723-9178-831cf13b1617 | -8.87708 | -47.92065 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4b91324-e8bd-3172-a927-6c1d63fcce54 | -13.05945 | -47.1075 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9df3dcc-673f-3704-9bc4-c06cb27a9aa1 | -5.96955 | -44.7335 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dc3a793-c5ce-395d-858c-267a1f67b501 | -5.97974 | -53.58963 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f12031-7d81-3e06-a830-48a73ef4c323 | -5.33551 | -42.6945 | 2025-09-06 04:17:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba8bbedd-7a93-3b65-8915-20ba04d9f4ee | -12.99845 | -54.82565 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e185ee6-6cd9-3618-acf0-ca7d84664b32 | -5.89198 | -43.64792 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b72a5124-1607-3ffb-9139-0c5aa092c054 | -5.20086 | -43.69352 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82ebf1b9-5329-38cb-96ba-496dc84a7086 | -6.15602 | -43.19728 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34dd3e2c-148d-3810-8555-f1cf90f260fa | -9.30546 | -40.4874 | 2025-09-06 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f2113f3-5722-3806-bb9d-637271011169 | -6.36325 | -43.53638 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb9e8607-067c-3e21-8f38-3f3a8c430e05 | -13.01225 | -54.84489 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59793d32-e83c-341d-9dda-6b8c0e99fc98 | -7.33581 | -48.5019 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 836128f0-3947-32ea-b1a9-7800af0e279d | -8.08905 | -45.32342 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 562c8ea2-6a85-3d8a-8c50-d057d369c528 | -6.20365 | -44.19345 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e583624e-55b6-399d-9a34-3896e59e9fa4 | -6.19338 | -53.25274 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d7c0e39-9175-32d4-9509-e3af211e722b | -6.00825 | -46.69862 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 574d1866-7430-34ec-8832-40372b75b5cc | -5.44956 | -42.80801 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a29a2715-9b09-3db6-bc87-2404e6e71dc1 | -14.5729 | -48.02557 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a715c0cf-c384-3b28-b09b-a92bb64eb098 | -5.97608 | -53.59571 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45b47c57-8126-3ec7-a5ad-3f62c6c511aa | -7.21303 | -43.99482 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7c6b975-5e67-3ba7-af15-25ba15c434a1 | -13.592 | -43.3536 | 2025-09-06 04:17:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a500845d-6137-3f21-ae3a-27855650e84e | -16.73704 | -43.02076 | 2025-09-06 04:17:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48fb00a3-1e69-3d16-8ad1-44060e7a20bf | -9.69069 | -51.09866 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc0514c-ccdb-3a8d-b6cb-4442cdda378f | -5.72722 | -49.28354 | 2025-09-06 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 897b1069-de13-3364-932d-360151b081b3 | -6.01648 | -46.6953 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22210b44-58c6-33c7-83fc-86f294bb78c5 | -6.16319 | -43.17351 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d2357463-565d-3c29-aec3-506733412229 | -6.1869 | -53.25581 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81598381-4c63-31b2-8597-a2f053a2d55a | -7.60407 | -44.67411 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0ba1cc6-d1b9-3a26-ada4-ba94131cdc36 | -8.64474 | -45.74668 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4fa1bdc-06e4-3e64-a6f6-648a8dd30e9f | -5.94972 | -46.17139 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02e74f0f-11d3-32da-97ea-7a04e7b803ba | -13.63374 | -44.22347 | 2025-09-06 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 566e5cc5-95e5-381f-ac55-e089d648de7b | -13.00306 | -48.05295 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7747731-e235-3664-a053-652d47a70fcf | -13.35933 | -46.83007 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c7b720b-410f-3e0f-a2d4-001f917f95c5 | -14.11409 | -51.71599 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e82a85aa-36d9-337c-b519-474f0837ecfb | -13.27084 | -46.81556 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7adbc05f-7c60-3af0-9065-048e7a036e6d | -14.58148 | -48.08395 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da3c076c-ab75-3819-8f22-0d9bd0524e70 | -9.8066 | -48.30149 | 2025-09-06 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e616bc61-e955-3245-84ba-547d77d25e15 | -12.50922 | -53.85587 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
