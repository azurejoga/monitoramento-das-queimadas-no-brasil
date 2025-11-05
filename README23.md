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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f602b1-2235-303a-a20e-5f732ec970a4 | -3.77003 | -45.89275 | 2025-11-05 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5fd2062-9fd9-30c2-9dbf-2b2c7ea09294 | -2.82429 | -49.41368 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5260e0bb-3208-3730-9111-789e92e9c400 | -5.01526 | -44.79503 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04e2530d-8fa3-3cca-9451-292347e9687f | -3.13392 | -44.47691 | 2025-11-05 04:12:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf3e8ff-07ce-3edf-a73a-2550a300443f | -2.48261 | -55.73445 | 2025-11-05 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc118ebb-f3b8-3842-a6fa-f9992b2ed6d4 | -4.29954 | -43.78816 | 2025-11-05 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8cced886-c865-394b-af92-bcd052b6c077 | -5.28272 | -44.24689 | 2025-11-05 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c31d8a41-0991-385b-bd7e-01f137b3f2c9 | -5.07334 | -41.20961 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62f13fd8-9bc8-3f70-83b5-a73166c46d50 | -4.40492 | -48.22243 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8e72458-c9a6-32a6-a4d4-2dbf5b2b0024 | -5.55022 | -40.75826 | 2025-11-05 04:12:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cdde0c48-c3c1-3f94-9b50-6b3b34f1eacd | -2.61449 | -49.23154 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 474254a8-4cb4-39fe-9e66-9e500510d895 | -4.29449 | -43.79827 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8951217f-67c5-34e9-add8-1ba86d40c99a | -1.26145 | -49.14735 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2207809e-d2b3-3d45-870e-cbe0f1e6c6c3 | -3.57006 | -50.64457 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30831648-14f7-39db-a14f-1e8cf95e96c1 | -5.61826 | -41.0884 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b30fed2-f869-3665-a807-640a8956fccc | -4.21036 | -45.49213 | 2025-11-05 04:12:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a87f021-5cd4-3eb3-a068-e4e48293ef5f | -3.84766 | -49.90601 | 2025-11-05 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a85074-8eeb-393a-a7f1-a4267962c492 | -2.89142 | -48.06546 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528d5772-3c38-347e-8bc2-1d05d1079ba3 | -4.84903 | -42.37902 | 2025-11-05 04:12:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec76d356-9520-3c5c-8534-afc58a1defbc | -3.48267 | -43.62725 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0b35073-8684-3717-bf6e-7346e95a466b | -4.28251 | -46.93696 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c69181a-84ce-3258-876b-2d699232861a | -2.78672 | -50.32005 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| afffbe14-6cef-3b75-ab06-e68ec15cb24b | -2.48502 | -45.97974 | 2025-11-05 04:12:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5356f41-ca3e-3d86-be31-42dd5403519d | -5.88875 | -42.91755 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad361c1d-2f6b-3df4-965a-1a6ec585d69e | -5.03925 | -43.6238 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78a5a47e-5edb-3c06-9294-94fa47ab6413 | -5.10628 | -46.22369 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17c93b6-fcf6-3be0-8cba-28136e79a23b | -6.11542 | -41.6407 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f79b5619-ec02-3377-afc9-3f0966c8d037 | -2.81405 | -54.3637 | 2025-11-05 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f406ef-9d0b-3319-a0f6-3cce5fa6470d | -5.92985 | -41.29151 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e469a5db-1faa-388f-ad38-dc573bf0cf5e | -5.53991 | -40.75666 | 2025-11-05 04:12:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1454f840-bd0d-374b-8fe3-54bc4ae028f0 | -3.4877 | -43.61717 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b42a5c27-2ae5-38a6-83a9-eadfb158c603 | -3.81031 | -51.28809 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c55109fd-28cb-361d-a97b-3ce55a1a6c57 | -5.06102 | -45.47684 | 2025-11-05 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e91b5548-4272-3a52-a263-9bf342383e65 | -4.79477 | -45.92963 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b19215a-4759-3f97-9c4c-6426d9a0c262 | -3.65936 | -44.8027 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef1da6a1-8c03-3f53-bac5-ee724aeda184 | -5.46839 | -43.57738 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4b17645-d7db-3270-8cdb-9b3e044603dd | -4.41396 | -48.94229 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 565661de-93d0-349b-a30e-55ec796ca813 | -3.06681 | -47.7799 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f42512aa-9e88-3575-9e4e-312008008b67 | -5.00819 | -44.20371 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a798e1ad-abaf-37ae-83ff-64b76d353b20 | -2.61583 | -49.22977 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9fc888f7-621f-3aa3-a112-4e74de891fb3 | -5.24273 | -48.50354 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c5f31eb-3ab7-3d9e-83a4-f9d8b24fe4f2 | -8.04975 | -49.63344 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 158aa0c6-efe1-3982-ac01-4565f2c017ce | -5.00618 | -49.70068 | 2025-11-05 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec04e878-6593-32ba-aebf-e841ffe050dd | -10.52865 | -44.17485 | 2025-11-05 04:14:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5a6ee51-fe46-3cb4-bebd-1c98328e3339 | -7.51811 | -45.34975 | 2025-11-05 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77c42a17-53ba-3ce4-a00f-26babf62cfc5 | -11.84951 | -43.72303 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e51ae72a-2705-3fc2-98c7-6d8d6449e091 | -5.24207 | -48.50743 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0a73585-31cc-31ce-871f-26c689f9e871 | -8.21091 | -43.81244 | 2025-11-05 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 819d3237-ae74-36a3-87cd-769a4e9ad48a | -7.16474 | -39.1581 | 2025-11-05 04:14:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6c432af-79d0-3d8e-a4de-fa8f4a8ae760 | -10.37748 | -47.75539 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f017147-24b2-3a42-9a0d-e67e08c66d4d | -9.05094 | -50.29428 | 2025-11-05 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0adf7b93-cbc3-3d68-9e01-70825696fbe0 | -7.78696 | -42.22646 | 2025-11-05 04:14:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df251555-7b33-32b4-a190-5f891497f3ce | -7.02887 | -43.80811 | 2025-11-05 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36747127-803b-3bc4-8603-2a53f0d947ae | -6.73982 | -44.14962 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 42476482-418c-381a-b286-f41c72c0de75 | -11.2778 | -44.63439 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1efd4f1-dc21-3ed1-8b56-ca75ffbfbded | -6.73756 | -44.16374 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c758dc-6691-3977-bbe4-736413e561a3 | -7.14664 | -41.82768 | 2025-11-05 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 759bf210-d936-3135-b718-8cfa836ec099 | -5.52018 | -46.23676 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0a279f9-c296-39d1-bbd2-66b7cbfd59b7 | -7.03823 | -46.98662 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac7ea35b-9eb3-3cad-bfbb-6cff23bf5931 | -7.45591 | -46.84015 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27eb7345-9818-3631-acc2-7d71df8a24c5 | -8.83289 | -50.02047 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f6e47a9-4988-344e-9ec8-7bc7f86e998b | -5.23497 | -48.49823 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 736417ca-e41a-3cbc-b762-5a5a54ea1b8b | -9.72829 | -46.35574 | 2025-11-05 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87367c82-a3c4-3902-a867-caa3b1530d50 | -6.03859 | -51.39048 | 2025-11-05 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc456fb-3ee3-3b3f-8e84-829c663da337 | -11.46688 | -45.15124 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f077de78-1410-3cf2-b750-96f1949d52be | -5.23852 | -48.50282 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f73a47f1-cb20-304d-95f0-ed8b44fdb3c9 | -7.32762 | -47.25274 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e885ee5-9c81-362c-bdd3-e71677e5b3b8 | -12.66051 | -43.92207 | 2025-11-05 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e717d918-7d8e-337e-9438-0c12124aace5 | -9.05303 | -47.00085 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 357a7897-4d08-392f-b6fa-0827f1213470 | -5.76626 | -45.90605 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51de4e31-ed37-36b5-a4d8-48f8338ce02f | -8.96575 | -44.10822 | 2025-11-05 04:14:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c62814aa-2a28-393e-8a78-4df2337dfbec | -6.3703 | -42.40524 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 088cbeaf-7241-3fb3-865b-4474cfc1e35f | -6.52566 | -39.69057 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb853cdf-38f2-34cc-8f0d-493c5668532b | -7.45662 | -46.94857 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d9e398f-0848-3480-986f-e238ddd6edbe | -11.01576 | -42.72915 | 2025-11-05 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a1339fa-b550-3670-a4f8-93bb522535ce | -7.02022 | -46.59752 | 2025-11-05 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b0468a1-ec57-3c94-b277-dd8575be0674 | -7.14069 | -40.46076 | 2025-11-05 04:14:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8356a8c0-e817-3a37-80be-864f02a80297 | -6.55154 | -44.47368 | 2025-11-05 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9434933-3462-3abe-9364-374fffc30171 | -10.42006 | -44.38694 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b09e0bc-9d5d-346d-9634-17b340a2ec2d | -6.05157 | -43.02787 | 2025-11-05 04:14:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a5014db-08a2-30f2-99a2-f6020b0d39b4 | -7.12882 | -41.33342 | 2025-11-05 04:14:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f76ce9c3-035e-3a10-8459-302c6b6319aa | -6.4822 | -47.93316 | 2025-11-05 04:14:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24e901af-540b-3d83-98d4-775a06a54093 | -7.41965 | -46.65338 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b0c7c39-c057-3b14-8714-f8ab4d3ebbda | -6.20449 | -43.26464 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c63f7759-b76b-327f-8878-54404e6aec01 | -9.62529 | -45.23035 | 2025-11-05 04:14:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70208584-4688-34bc-a0d1-74791bc52128 | -9.88372 | -47.45947 | 2025-11-05 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 360e1cb4-cfb9-3dab-b6dd-b89c1d038589 | -11.62964 | -41.47019 | 2025-11-05 04:14:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2098d076-f9cc-3269-8d20-2cb9cbf276ef | -7.5244 | -47.14611 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c185be-443e-3bb1-9840-ec21da55e161 | -6.07392 | -43.25062 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c0f48bbf-69a8-3236-96dd-4d1caae04594 | -6.36089 | -42.40025 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 005d39e7-03cf-3d5d-bd87-778272e71c49 | -8.67448 | -36.6887 | 2025-11-05 04:14:00 | NOAA-20 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbc32858-3ebe-3942-8a68-2d6854dd258e | -12.24216 | -50.29382 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e950c52-0293-3107-9a5d-8826ed5531b4 | -8.22482 | -49.98496 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8559df14-ba80-357a-af84-68c11b3aa374 | -7.14131 | -40.45675 | 2025-11-05 04:14:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e329e08e-73be-3646-9697-01e1094460cc | -7.17474 | -42.73434 | 2025-11-05 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 429d3a55-0cc3-34af-b368-4389a07a5387 | -10.40133 | -44.37669 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ccb8680-e094-3ebd-a322-147f9f66fc2c | -6.65602 | -42.66339 | 2025-11-05 04:14:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| afc8c011-cd31-3e42-93da-d115dad6527b | -11.01239 | -42.72862 | 2025-11-05 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40030a8f-8871-3791-9fe5-1bffe16f5575 | -12.23372 | -50.29223 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c84302c7-1aac-3358-9bd7-c02b1ec50e48 | -8.50729 | -44.17049 | 2025-11-05 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
