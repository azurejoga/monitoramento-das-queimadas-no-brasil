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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a900781-d94a-37a2-9d48-c21c39c7d892 | -4.44587 | -46.34599 | 2024-11-23 03:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c86bbf6-ce70-37aa-8e14-8b0e953b207f | -3.46725 | -48.24865 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c448a50c-549a-3791-a779-44f101fd1995 | -4.66521 | -45.67953 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9972f20d-d22a-3b49-85b5-f21db90d1249 | -4.10253 | -47.81139 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95378211-bc54-31bd-aea3-859a815cbfa8 | -5.93284 | -43.77935 | 2024-11-23 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5966a55c-f4aa-3284-926b-041b65a9e5c4 | -5.56407 | -43.31893 | 2024-11-23 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31af300-72c8-3ab0-8f38-760db4ea8289 | -4.5276 | -43.90783 | 2024-11-23 03:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44120760-9abe-3417-9d08-d4154fda4922 | -5.22794 | -45.11011 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af54f2bd-e9ae-3555-91c8-4778492bab49 | -6.56444 | -39.76434 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44ffede9-a4b3-3a4e-a545-e5d6434547fb | -6.23307 | -39.62991 | 2024-11-23 03:55:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9b7a3483-f2ae-35e5-baf6-ea4d7377ed6f | -4.9516 | -47.80533 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4595029d-1f7d-30e4-9953-5dd640943b4f | -3.82909 | -48.9832 | 2024-11-23 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b9ee2c8-aeed-36ef-b5d1-47a4a102aaa3 | -3.79921 | -51.76134 | 2024-11-23 03:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27dfbedc-dc3b-3643-9562-8ca901a521dc | -4.65633 | -45.67256 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 502e3e76-3e4f-3a03-b9c8-78b35e438e99 | -4.75432 | -45.78448 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b34bd99-5748-399d-82a2-00ad0510878f | -5.96672 | -46.30354 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4030623-f0f8-3c2f-852f-b69c54d04873 | -4.26254 | -46.29184 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09fc3ed-c24d-3d5b-9aed-cbb4c821a18e | -4.66714 | -45.66832 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c60d42f6-1698-3949-847a-fb395e9ef08d | -3.82991 | -48.97845 | 2024-11-23 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08442b60-e24e-372e-87aa-10e0ffaa2cde | -4.69696 | -45.85003 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 32ab3c10-a36f-37a4-9ef8-a9c103600370 | -4.58755 | -46.07502 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 241e6317-5364-3cdc-b780-3d04f459e97a | -5.56885 | -46.29013 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de6101e3-8c87-3e74-98ca-9c191a884cb0 | -4.41582 | -44.11642 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eaedec70-2b66-3f5c-a24a-0db5f14f9fe4 | -4.90437 | -47.41597 | 2024-11-23 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 285c80a8-e90a-3ae4-8a66-00e518e83ccd | -5.95036 | -38.32924 | 2024-11-23 03:55:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e1411b1-a59d-3b82-9ac4-31d72dbec571 | -6.35282 | -39.79817 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5af6f7a7-a4ea-359d-ba9f-ec6160e5f4cf | -4.53689 | -42.92036 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 045c87b8-188a-3e14-8aa0-dab8016ee2fa | -5.56834 | -46.2931 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5814488-e33f-3100-a4c1-dc865f550d30 | -4.27282 | -46.29361 | 2024-11-23 03:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d320ec10-24d5-30e3-b4ef-0380b1b38b77 | -4.6137 | -46.50038 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf759151-d162-3492-8be0-87f3445d00a3 | -3.94949 | -47.97119 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3985fa47-e40e-3d2b-9495-ea59bf55da22 | -3.94473 | -47.9665 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 408cbcab-e5e6-3997-9ad9-d80a958f2296 | -4.12314 | -43.23256 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6ef699f-f0ea-3bbe-85f3-d04a678cdc58 | -4.44145 | -46.34872 | 2024-11-23 03:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 275e9604-15e7-3c18-9b2f-800c04b3783b | -5.03503 | -45.81572 | 2024-11-23 03:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c73ce96-a604-35c5-b1b1-b3bd5152f2d8 | -4.08964 | -47.03337 | 2024-11-23 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d17f2cf-6f79-39e8-b002-f092cdbff7b5 | -4.59129 | -46.07665 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 128ddb94-372b-31c2-bc65-e4b12c5b0b34 | -5.58722 | -45.20863 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b659a753-6c64-350e-80f7-e0613597d662 | -5.92456 | -44.60482 | 2024-11-23 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69fcd571-c4e1-3a8c-b203-0a722969ab4c | -3.94407 | -47.97041 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9b248a4-1f56-3c05-9917-021184bea1d6 | -5.94704 | -38.32871 | 2024-11-23 03:55:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 19f2669a-d9cc-3b77-910c-9a4a8eda04d9 | -4.66937 | -45.67289 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8fa36b7-7e3c-3c1c-a42c-1ed4b23defb5 | -7.01967 | -39.22511 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| db16f0cf-1b4a-3b7a-900d-76e1c7cb51f1 | -3.67752 | -50.11971 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e429676a-246b-37e4-b2d9-9081acdca6a9 | -7.00849 | -39.63135 | 2024-11-23 03:55:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e745ec9-3652-3bb8-ae0f-7a2685725315 | -3.9726 | -46.64637 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 527c20cb-0bae-3a00-873e-12b644eee9d8 | -4.69599 | -45.85573 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1b2a8a0-4f97-3b79-aa98-afc8ff1b7f46 | -4.10185 | -47.81529 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2df188cd-d2d0-3fb3-a866-f57de5412361 | -5.11892 | -45.83735 | 2024-11-23 03:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 304e5cc1-357f-3c30-a39c-3ce7b1887b9c | -4.67299 | -45.66365 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a8a7a34-164f-3a34-90f8-12cc0b8cd2d9 | -3.90275 | -47.93363 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2092fcd3-e368-3372-8f3b-243e5e8b1152 | -3.68037 | -47.12299 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6b967d2-1ec4-3d91-8665-4f74db1c77f2 | -4.4217 | -44.10838 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45087572-2219-381b-9707-5f04ac2d5005 | -6.05629 | -44.04546 | 2024-11-23 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4152ba92-2179-30a1-8481-283b7f5b925c | -4.12733 | -43.2332 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b92f502-010c-3053-90da-7a12412a1fc7 | -4.72172 | -45.49628 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7fca9e3f-75fb-3385-9716-ad943f58fc99 | -4.94596 | -47.80441 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba85e30a-3077-368e-9665-51a1c3d95c43 | -4.60325 | -46.49905 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e7efa646-9f4b-3412-abc1-13b268015cdf | -3.96975 | -46.65208 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4e66a1f-00b2-3da8-9476-e80a28f987c8 | -7.01577 | -39.22815 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8df044e-cd8c-3b4f-8c36-f93f77c14178 | -5.06566 | -44.23717 | 2024-11-23 03:55:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f14123a-fd33-31cb-991d-78eb05b2fa99 | -5.94862 | -44.46566 | 2024-11-23 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6fcd8db-1c19-31da-8321-dd54e339a8c9 | -4.55876 | -48.02443 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4d343459-db93-3573-bc2e-47137c800f21 | -4.53022 | -42.75908 | 2024-11-23 03:55:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea787b6-47cb-39c3-9940-7196ce4f5d18 | -5.22222 | -43.73832 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c93c10d9-a219-3e33-90c9-fed13233681f | -4.48291 | -45.66294 | 2024-11-23 03:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e21920e2-77e0-39d5-a211-f95a7908797d | -4.1015 | -47.80782 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70b7a55-3896-30df-8c00-caa752608bd4 | -4.41213 | -44.1113 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5366e39b-47a0-3722-a857-10e48e0942e4 | -5.13302 | -41.55853 | 2024-11-23 03:55:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e28097b7-f35b-3a6b-bfd3-f237c98b6f3f | -4.34581 | -46.01722 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f3f0a9c-5fd0-3951-b77b-c697987a73e2 | -4.41802 | -49.68966 | 2024-11-23 03:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c451a7b9-551e-3925-a2c0-8e960118784a | -4.67207 | -45.66899 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb6854a8-c263-37d0-8869-f642e881f241 | -5.9322 | -43.7832 | 2024-11-23 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddf089cc-fdaf-3330-8c17-161d2242286f | -5.66469 | -47.33679 | 2024-11-23 03:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f05e5396-0e5a-367b-9337-f0b208a3480b | -3.70186 | -47.61731 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048575b1-fdd5-32a5-ab64-a91a2e68fd25 | -6.04482 | -44.82604 | 2024-11-23 03:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e94c773-c1b5-3eb7-ba4b-22c199602b74 | -4.94942 | -47.80222 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b76a6b5-943d-31f7-88e2-c97ad1275635 | -4.95226 | -47.80142 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b63ece2c-316d-33c5-8be4-2c0a541cb868 | -5.61889 | -43.48438 | 2024-11-23 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfb2a884-e0d5-33be-a048-0c75501064d9 | -5.75801 | -46.25985 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d090ab-fab1-3533-92be-314cbe3c9717 | -3.67852 | -50.1141 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a66ecf8-191f-3dd8-b62b-b76e8f5b2d82 | -3.46391 | -48.25253 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2c8c899-eaf6-38b0-9d83-e411a767acfe | -3.67979 | -47.12654 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2138be3f-7687-3d08-950f-3bb10c815c9f | -5.75302 | -46.25894 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61a3a592-8292-3a09-8d63-6f3980ad0615 | -13.28909 | -39.80671 | 2024-11-23 03:55:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 35b7565e-9740-3a95-8c67-3cf2a8c48ec6 | -5.48833 | -46.25423 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65177151-3bef-3d94-99cd-7d25a6369570 | -5.11401 | -45.83647 | 2024-11-23 03:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 946a29a2-3a22-3c21-8805-cc8bfaec233e | -3.99858 | -46.93593 | 2024-11-23 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a962edec-84d7-306e-a5dd-d92f3676fd25 | -4.54684 | -45.88837 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 92cc54f8-716f-3ece-8e0d-c88856b9d2ac | -4.44535 | -46.34916 | 2024-11-23 03:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3bfcb6a5-5efd-3624-857d-09330f224eae | -3.95085 | -47.9634 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a63fb8e9-b738-30ef-b0df-a82d537807ba | -3.95017 | -47.9673 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4eee4222-3c05-392b-b01a-a3eb8adf759c | -4.58799 | -46.07236 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d36b846-3873-3596-857e-58e29d10c007 | -4.70098 | -45.85643 | 2024-11-23 03:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8bdc753c-6d22-36a2-b529-f195544e53eb | -4.12377 | -43.22879 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e26880a-0411-3a7a-a5a9-8ae5d66168ed | -4.69564 | -44.40618 | 2024-11-23 03:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbb5174e-8aac-393a-b5c6-2ce0e55f9c1d | -4.69189 | -44.40107 | 2024-11-23 03:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d223598-064f-3842-857d-35c6f217caad | -3.46886 | -47.68732 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fadd57b-9f50-3322-a3ac-48c53c339e8c | -4.54185 | -45.88757 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94e2fca9-24f5-3a54-b62b-af8fa64fcf68 | -5.43278 | -45.34388 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README26.md)
