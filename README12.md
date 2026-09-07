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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1771552e-9af7-3273-b31a-669d7ae8d370 | -3.49233 | -50.6102 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b71bf21-3df2-3b76-904d-9d0c32c2ec98 | -5.37141 | -49.05758 | 2026-09-07 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34767a7-0a7f-37f0-8cac-9803f1c3193d | -2.63837 | -46.77708 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b868636c-c1ca-3e29-a8e4-de6cbf4850a9 | -2.87324 | -50.45995 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7586254-0ea2-3660-bc97-c78f678ac80f | -3.21102 | -42.97532 | 2026-09-07 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4898ba-e1ff-31b2-b222-1df4a8d6dd7d | -2.87135 | -50.44652 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a563ad9b-67f6-364b-8d68-ac80564e2def | -5.50861 | -43.2028 | 2026-09-07 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e6b60a2-760b-3d03-9445-6665abbcbef7 | -4.4732 | -55.09457 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98aa78a2-8d64-30c7-8440-0e9afc234f4a | -2.76806 | -48.60228 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebbcd0b3-09c4-3c9e-8d8c-467c8bb3fc4a | -3.95214 | -49.03747 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6451850-b92e-3242-a3f9-63b3e15932b5 | -2.63893 | -46.77354 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9b4686b6-1957-3a96-be93-1c47029e2e2e | -5.1398 | -55.96025 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e53aabfe-3807-372e-a6c3-e1b3141d1667 | 0.21498 | -51.28088 | 2026-09-07 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3edffce5-9801-302c-b641-7292d0ea3fab | -2.56038 | -54.74373 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc877e2-8211-3e0d-96cd-3cdc2d7dbde5 | -1.84607 | -47.94761 | 2026-09-07 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d32a0bc8-cbec-392c-8922-e7eb23808057 | -2.8634 | -50.44529 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd1318a-343e-3990-8a17-eb98482484be | -5.80559 | -46.22918 | 2026-09-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccb772cd-4be3-3362-9eab-3be3df668394 | -4.50772 | -55.71173 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9759c39c-53fe-321d-aff4-7b13d0e6aa14 | -5.76121 | -47.63835 | 2026-09-07 04:25:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95865e35-2ac3-39d5-b2d4-226c517de2a8 | -5.4061 | -45.62896 | 2026-09-07 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4a51b5e-546a-3a1f-a3ec-acc1051e823e | -4.81393 | -49.38884 | 2026-09-07 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b3d1554-0401-385e-8394-94b870733b1d | -5.76064 | -47.64193 | 2026-09-07 04:25:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8810e3ca-3f40-3d0e-ac39-6a39e88a697f | -7.20368 | -39.3951 | 2026-09-07 04:25:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a0d2917-1ad8-30e9-b58f-f4f89978528f | -5.15157 | -55.95836 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc9b5c59-4c07-3130-b797-29d56defca82 | -3.67485 | -48.91633 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e34d7311-48b4-37e0-8988-470200825db7 | -5.14108 | -55.95286 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a398f885-b09c-3937-a1e1-5bd0c087fff2 | -5.16703 | -55.96828 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d726cf2-64e3-3a0b-b849-b4eb06ef9246 | -2.88244 | -50.4535 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71e58b8a-49ce-37fe-b81a-7470bf690e45 | -3.27329 | -50.59596 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ad1de6e-6fba-389b-81d1-a229fe0ec0d4 | -3.79486 | -55.87845 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76aa57fe-f46b-3f7a-8e4e-ca74f11bb372 | -3.49561 | -51.20835 | 2026-09-07 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ae5b70-23be-38f7-83dc-66182e12b3b7 | -6.38704 | -42.34394 | 2026-09-07 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c9c6a25-2090-3f1f-85fe-dc038bd3c3c6 | -2.87449 | -50.45226 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 77d33403-4b35-3fe7-a75d-68a94f705001 | -1.19975 | -55.73812 | 2026-09-07 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28ed1aec-cc4a-30fe-9cfe-4d6e35f37679 | -4.97424 | -50.63126 | 2026-09-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76f498dc-eae0-3e97-9840-40221c7c83e6 | -4.65014 | -46.31205 | 2026-09-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0df70f-9c18-3d19-8911-59536c2c8964 | -1.86917 | -47.98307 | 2026-09-07 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef47f653-4118-3e69-80f0-c889c7445485 | -2.63224 | -46.7725 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5b002db3-2d97-3c7c-942c-d8e7e8d9938d | -2.87532 | -50.44715 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5ed2278-a192-355d-909b-3c324278a8d4 | -4.6743 | -55.6322 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9309584-0615-35ee-a284-fb94d2b78c00 | -2.62889 | -46.77198 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 16e038e2-e268-3b78-ac23-03f3eabdfa6e | -2.08821 | -49.53323 | 2026-09-07 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 801f278a-ded7-3ace-858a-cc348b879216 | -2.82284 | -49.2272 | 2026-09-07 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d857e9f-da14-32da-b41f-aada9012d423 | -2.29983 | -48.57944 | 2026-09-07 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6b126c-1505-34a6-8d46-69f419325605 | 1.64392 | -56.05508 | 2026-09-07 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85d763f-b0f5-365b-9136-83e9c7e8c0a2 | -4.21723 | -48.5648 | 2026-09-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0379d20d-3068-3302-9387-b725d6c85555 | -2.63614 | -46.76948 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 69503eb5-0579-31dc-a10e-8ae2fe5d6449 | -2.88327 | -50.44841 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85c5cc79-672e-3bdd-84a8-828ad2f1e076 | -4.03785 | -50.87281 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d85a7d6f-875a-3764-a5ab-301e359ff164 | -4.06743 | -50.64065 | 2026-09-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a6fc267-f210-3d91-8058-800d98809fa3 | -5.16211 | -55.96361 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c4d7a37-0e45-380d-b4b4-c0c6aa90820b | -2.91387 | -54.12216 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c1a04ad-924b-317b-8bff-da4a96bb5e51 | -3.49289 | -50.60678 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73664b4b-0cf8-3458-9de6-cbcb42571056 | -4.01227 | -44.83714 | 2026-09-07 04:25:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 508f694f-ef57-318b-9ee4-1e00786479dc | -4.03591 | -52.07666 | 2026-09-07 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60205787-001b-3562-9df3-d874b0c3751b | -4.07655 | -48.95134 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 26c5de6f-acc3-3f9a-9320-54c7ad54df4f | -4.50708 | -55.71543 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddec2d4d-3f4e-3f65-ba9a-f343d00ca827 | -1.18576 | -55.71376 | 2026-09-07 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8885edb-072b-3e47-98e4-38afb774ac33 | -4.66757 | -55.63859 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32ea6328-23c5-3a6c-9d37-0b16a2d7c9f6 | -4.97553 | -56.28704 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cf0998f-ed56-349d-8555-dfdd308c3379 | -4.63198 | -45.37999 | 2026-09-07 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e63b66a8-a75d-37cd-aed0-c851f8021bdd | -4.46905 | -55.09482 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b59e3e-a4ff-328c-8dca-2f749189b0c8 | -5.14966 | -55.96945 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b0a0134-52d5-31fd-9b9b-81f7e40d9abe | -4.43025 | -55.09832 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fc59a00-2d29-32c8-8286-3919b494723f | -2.63503 | -46.77657 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8d6be871-e713-32f4-857c-c40308f1608d | -3.49688 | -50.60735 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cffa9a9-b1b6-3633-8a6f-c6c135d98141 | -4.03661 | -52.07248 | 2026-09-07 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de62ffac-7996-3cfc-8d50-1024d91c9792 | -5.14601 | -55.95741 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3101f850-b4a0-3747-8d32-f36c370e0f0e | -2.95807 | -48.70578 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c7720e8-1614-3f20-ad44-983a89a37a2f | -5.80505 | -46.23263 | 2026-09-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44563f60-6017-3892-a334-86f9caf2c8ae | -3.54623 | -48.18378 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eb1347c-9e6a-3389-8172-23f918d356ba | -4.07888 | -48.95061 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bbc874e8-5eb2-3f9a-9d14-9e2cc26f1c47 | -4.46792 | -55.09352 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aff92b8b-bfa7-3a76-ab1a-f05a253692c7 | -2.36867 | -44.58358 | 2026-09-07 04:25:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4673de18-0132-3f37-a613-3eead33d0d2e | -4.11261 | -49.06144 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5c59f20-4592-3ae8-92c0-d0d114a94b7c | -3.54436 | -48.18414 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fcbfe90-8354-3c4a-bb89-40c2eb033538 | -2.86997 | -50.43885 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 661bc866-6548-39f8-9ace-0c583766e28d | -1.49294 | -54.83039 | 2026-09-07 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9db75ca-508a-3453-a12b-333ffa9d2447 | -4.29723 | -38.52951 | 2026-09-07 04:25:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1eea11f0-7d49-3ed9-9111-55d336aa8f06 | -4.10539 | -49.06031 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1208a539-c467-332d-9c7f-08c8154cba92 | -4.37982 | -44.39003 | 2026-09-07 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bdd59ac-b103-3dd2-a06e-e15e1dd0cd3e | -4.43501 | -55.1025 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af3f2e0-a13a-31f7-a80e-f3e7ce56c960 | -2.9646 | -48.71099 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e6d72ac-7b9a-3157-9bc5-ce72e2c9359f | -5.44022 | -42.22731 | 2026-09-07 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1162f1d4-799d-3c4e-a4a4-96e37b878d3d | -2.86917 | -50.44398 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4162fe8c-a0a1-3146-87d1-83abdc33db0d | -4.46959 | -55.09154 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a0d513a-0e1a-3044-9ef3-bf122508523a | -4.11582 | -49.08755 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffb78de7-dac4-3da6-bcae-7e8ab53af472 | -2.36922 | -44.58008 | 2026-09-07 04:25:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfcaba10-08da-383f-8a7e-f89778e9c92c | -3.67551 | -48.91222 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4317ee2b-8eaa-32eb-a0d3-1eba8d329df2 | -4.12189 | -56.351 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e4da4f8-681c-3e2f-9b97-1140ebefbbd1 | -2.87302 | -50.43629 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b585ecea-3263-392a-9a5e-40d1f8334d5c | -2.96101 | -48.71044 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7af09940-ce7a-36de-80cd-a040d4e9ec4d | -2.62944 | -46.76844 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| eaab1c3d-c064-3ffd-a874-3d5bcdfe803e | -3.0615 | -51.24804 | 2026-09-07 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff001d06-8d37-3313-9d37-8adcf7f2ace8 | -2.86584 | -50.4553 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 797fb9be-355b-31e4-be48-0927faf8baf3 | -4.47488 | -55.09254 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a7feb78-fc99-3fe6-9dd2-29422a3b63af | -2.8841 | -50.44329 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| defd620b-0dfc-3d33-b3c7-e7f3ce122cc3 | -4.59587 | -50.98213 | 2026-09-07 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 085b3d62-14a5-30fa-929b-6451c5e57472 | -6.78281 | -42.73666 | 2026-09-07 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4269b68e-9716-34a4-ab1f-609f629904fe | -2.63168 | -46.77605 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README13.md)
