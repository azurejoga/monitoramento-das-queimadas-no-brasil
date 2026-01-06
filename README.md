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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2353b684-fff6-3ebe-9666-8db562421995 | -2.5238 | -47.8332 | 2026-01-06 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| b9eb5900-a027-3deb-a67c-1e404161a9c6 | -20.5279 | -58.0039 | 2026-01-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 00062bb1-191e-3283-af50-6dc252485d80 | -20.5077 | -58.0066 | 2026-01-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| f36ac07a-cad4-36fa-be04-d82eef3523c1 | -2.6431 | -45.6499 | 2026-01-06 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| dd6e6ce8-c9f9-32c4-8f6f-750ba84d3a0b | -10.1999 | -36.2927 | 2026-01-06 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 651ef3b1-626c-3882-922b-b07598311915 | -2.5238 | -47.8115 | 2026-01-06 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f095af76-63a0-3da6-a979-c06ffde9ed67 | -21.0345 | -48.5034 | 2026-01-06 00:00:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| c03c6b06-ae25-3efe-84d3-9930683c7857 | -5.3805 | -43.1779 | 2026-01-06 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 918260a1-d702-3a40-ad84-b9b03f11d343 | -2.2846 | -53.7822 | 2026-01-06 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1d76bf58-4994-36ce-aad2-5c94e60d1da9 | -2.5423 | -47.8327 | 2026-01-06 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 26f9c214-6a1a-3a17-bb2c-bc1f576707fc | -5.3802 | -43.2013 | 2026-01-06 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1fd7f60c-8f0f-32cc-bb25-dfc810137e89 | -4.5758 | -43.793301 | 2026-01-06 00:02:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 650cd5dc-f691-3488-9412-460cd0510df4 | -3.186 | -51.072201 | 2026-01-06 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e6746d-b3ed-3e6b-85c5-d41ecbaa06f5 | -5.8975 | -39.229698 | 2026-01-06 00:02:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 91bd772e-146a-3eb1-b5de-0413de508e5b | -3.6951 | -43.416199 | 2026-01-06 00:02:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04356247-9e48-3c4c-aa93-aa92431cbb81 | -3.6971 | -43.424999 | 2026-01-06 00:02:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04c5cbdb-5164-3909-a782-03bf62340514 | -2.1599 | -47.883301 | 2026-01-06 00:02:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51aa753-41a7-37b1-b0d3-99f27881c2e9 | -0.0923 | -51.260201 | 2026-01-06 00:02:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 989fe65b-af98-3ac1-9c3c-2f12ba99c51b | -2.0739 | -46.9132 | 2026-01-06 00:02:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 365589b7-ad2c-394d-a05b-235a588135d9 | -6.581 | -38.447601 | 2026-01-06 00:02:00 | METOP-B | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 01606bee-0649-3381-8736-c079e12486f5 | -4.1059 | -47.284801 | 2026-01-06 00:02:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e27e85a2-c7d2-37a3-bf9b-2dcd269bfe49 | -6.3324 | -39.582699 | 2026-01-06 00:02:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bcd95be0-59fe-30d7-9b15-cbb9ce6784cc | -2.6491 | -45.637001 | 2026-01-06 00:02:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 203c7298-698f-376c-9d9f-958979c9762a | -5.0423 | -43.5821 | 2026-01-06 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a1ecde1-e90e-30cd-a1fd-04a5a156665b | -3.2177 | -50.386002 | 2026-01-06 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9544662-93a6-32df-bdc1-5fecbfa93267 | -6.3261 | -39.5989 | 2026-01-06 00:02:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6d460bdb-485a-39f9-ae53-a45b22f8a528 | -4.1198 | -43.8717 | 2026-01-06 00:02:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59e92910-754e-324f-bb2d-8e64b8e0b799 | -2.5147 | -47.8116 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c81b31fe-b87c-359e-8d67-9d034f9ab0ad | -3.7156 | -47.1996 | 2026-01-06 00:02:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8bf4e3-6e13-32c5-8871-58dfefe0705a | -2.4791 | -46.292999 | 2026-01-06 00:02:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e711994-35e5-35f0-9a56-6090666db00c | -1.1448 | -48.087502 | 2026-01-06 00:02:00 | METOP-B | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce4f38e-8a71-3845-8adb-6f22280b69af | -2.3582 | -47.666901 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00d0f5a-6d20-329e-b4e5-f644a2d8f51f | -4.325 | -48.211102 | 2026-01-06 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3109ce-87f6-383e-8913-b636be2ace12 | -2.9247 | -48.2127 | 2026-01-06 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d30a3a20-77bd-3713-88d1-38660a17bd2a | -2.641 | -45.6465 | 2026-01-06 00:02:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab4fa347-8103-38eb-a764-58c4d34ed37d | -22.496099 | -46.929401 | 2026-01-06 00:02:00 | METOP-B | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b4e9116a-04ea-3749-82bf-b659677b66d1 | -4.109 | -49.221298 | 2026-01-06 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc63f99b-8f7d-3072-ac62-47c15bc2beb2 | -2.5245 | -47.809399 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ff9575-53a8-3b00-9edc-b52bdfcf7721 | -2.879 | -52.5494 | 2026-01-06 00:02:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340c873e-0b34-30dd-a162-c7c211c10264 | -12.4067 | -41.370499 | 2026-01-06 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d12e4241-2cb8-3729-b804-1c6bb21c817f | -12.4165 | -41.368099 | 2026-01-06 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 05f0c799-8808-30c3-82c0-d93bbeaaf00c | -12.4046 | -41.3615 | 2026-01-06 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b66b9e70-8770-3bb8-a650-a44617aaff13 | -5.3728 | -43.1856 | 2026-01-06 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 682d5bc0-18f8-3262-bbcb-7cb6f087e7ab | -3.9857 | -47.984501 | 2026-01-06 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b48927-2025-3047-899b-efa58a415255 | -2.9887 | -45.454102 | 2026-01-06 00:02:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3308dd3-df2c-3f53-b376-3dd07f56ee29 | -3.2158 | -50.377701 | 2026-01-06 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650e1006-ba2f-38b7-be52-9b628f7c8e23 | -2.6393 | -45.639198 | 2026-01-06 00:02:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdb90ef-765d-3ad6-8e82-a6a9b44880fb | -21.0187 | -48.473 | 2026-01-06 00:02:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 26b230cb-b9c0-3f30-a9fc-1b7ee8de2957 | -2.4532 | -47.767799 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddcae159-6dbf-3318-99a8-edacec74ca32 | -6.3227 | -39.584999 | 2026-01-06 00:02:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30066bb5-0180-339a-a425-dc951fb7271e | -0.3661 | -48.425999 | 2026-01-06 00:02:00 | METOP-B | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff011fb1-ea23-3f56-9a15-16409ced048c | -1.4597 | -49.069199 | 2026-01-06 00:02:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9223dc0a-a161-3b8d-8f21-0b6d42899ee3 | -4.1482 | -43.637699 | 2026-01-06 00:02:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 773cb699-535e-3f0b-af76-649870b460b1 | -2.5374 | -47.8209 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d7f4a1-0d20-3051-8bb4-8fd26ce49151 | -4.0607 | -42.507 | 2026-01-06 00:02:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be0f28ea-b6cb-36dc-9886-2c92293603ca | -2.526 | -47.816299 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7829598-9e91-3ed0-b606-ea312d730e8a | -2.3665 | -47.657902 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef73c533-fd3a-3c0c-be7b-9648ee821a2d | -2.9361 | -48.217499 | 2026-01-06 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 005f7794-7f5f-3678-8214-98e0cd736533 | -1.1463 | -48.094299 | 2026-01-06 00:02:00 | METOP-B | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec90c9a-0d1a-34ca-932a-789e28e159a0 | -4.0742 | -42.874199 | 2026-01-06 00:02:00 | METOP-B | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 729cebda-7783-3017-a77c-0e38dc6eaae2 | -2.9857 | -48.574402 | 2026-01-06 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89270b22-cef3-3703-bb55-40932dbbcff5 | -2.7133 | -49.147598 | 2026-01-06 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae4b40a-62d5-37f6-9aaa-6489eb7a6b19 | -6.5769 | -38.431099 | 2026-01-06 00:02:00 | METOP-B | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 3366d84e-b742-3b69-877e-7f4c5765382d | -2.9873 | -48.581501 | 2026-01-06 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f87616c-a4c8-3ad0-aaca-971a1f3ce27b | -5.3806 | -43.174801 | 2026-01-06 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2490a5f9-3daf-3505-bc13-6555491146b4 | -2.5483 | -48.918098 | 2026-01-06 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef479a78-5d94-3f4e-838c-137afb0b5250 | -4.1044 | -47.278 | 2026-01-06 00:02:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46301c16-5eb0-3ade-b437-85c7f6f0f25e | -1.2127 | -47.069401 | 2026-01-06 00:02:00 | METOP-B | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65294a57-8ebf-3550-8067-2960acba58a6 | -6.9633 | -46.2061 | 2026-01-06 00:02:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55de107c-4b83-37b4-9d93-3ed06548ee6f | -2.3681 | -47.6647 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d526f54f-2180-33f3-bbd5-0fac66ee7214 | -4.3266 | -48.218102 | 2026-01-06 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f48787-3aff-3412-a08a-c28c791a4d65 | -22.494301 | -46.919601 | 2026-01-06 00:02:00 | METOP-B | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 91979ad9-4316-3ecf-b53d-9f6755b225a2 | -4.1501 | -43.646099 | 2026-01-06 00:02:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc01e39-b378-342b-bbb6-aa429d381045 | -2.1584 | -47.876499 | 2026-01-06 00:02:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 220a3783-4b6b-3e82-bbce-c6b54f380a5b | -4.0653 | -42.526501 | 2026-01-06 00:02:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e8a1156-7504-3879-bbbe-facada1ada8a | -2.6508 | -45.644199 | 2026-01-06 00:02:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79624c34-b876-3b93-8fb3-f59a9a548e52 | -10.1851 | -36.2882 | 2026-01-06 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54df37b2-842f-3381-863d-75094bf03245 | -5.8721 | -39.679001 | 2026-01-06 00:02:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8ca31d7a-ac47-3dbe-8173-e77d716e6bd0 | -10.1896 | -36.2654 | 2026-01-06 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7654005-0c75-3664-9ae4-4296ae62887e | -20.995001 | -48.4543 | 2026-01-06 00:02:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 35ba9086-4b8b-3b76-bdab-ba5b4e9a7a5e | -5.8687 | -39.665001 | 2026-01-06 00:02:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c32a2bfb-5f26-33cb-9cc1-9716891ed6fd | -10.1799 | -36.268002 | 2026-01-06 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 598cd13c-9afa-36a3-ba6e-deba9219ba52 | -2.1615 | -47.890099 | 2026-01-06 00:02:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3df5a96-5aee-30a5-bb03-dad5e596d390 | -2.9232 | -48.205799 | 2026-01-06 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 629c868f-2b07-3991-9c7b-cd16243ed66f | -2.5276 | -47.823101 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903f034a-1fd1-3830-bf62-6ae8725550fa | -4.7045 | -43.993801 | 2026-01-06 00:02:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c4b3245-0263-35d0-91a0-70b8f73dfc75 | -2.5229 | -47.802601 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 508eeeeb-3a4a-306c-bccc-b438d837ecd7 | -4.1217 | -43.879902 | 2026-01-06 00:02:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2f9f02f-7618-303f-9a73-ea438f750b4e | -2.6377 | -45.632 | 2026-01-06 00:02:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc4d4da-3c15-3f70-9d96-10b045f13236 | -4.063 | -42.516701 | 2026-01-06 00:02:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83628618-0397-3f67-b8ce-7b76fc4027dd | -3.7039 | -46.965599 | 2026-01-06 00:02:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9787af-bded-3f14-8189-42e2bb360c0d | -2.8766 | -52.538502 | 2026-01-06 00:02:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfda1a4-aa4a-3c74-9332-7ce6523c9998 | -2.1833 | -48.1231 | 2026-01-06 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f2ebb6-47de-3a57-9b92-2f1c5ccb1f53 | -2.3566 | -47.660099 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4ac70e-3636-3076-984e-dc77c6e5cf0e | -10.1948 | -36.285599 | 2026-01-06 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd634739-3d23-3809-8a15-c24878a9a707 | -3.7023 | -46.958801 | 2026-01-06 00:02:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa8de905-fee7-325a-8259-0609089a50cc | -20.997101 | -48.465698 | 2026-01-06 00:02:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 36bf29c2-77aa-3501-8d82-2cf5df61619e | -3.9485 | -45.955898 | 2026-01-06 00:02:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a977c01-f2f9-38c4-be6c-198a6837058f | -4.072 | -42.865002 | 2026-01-06 00:02:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe4ab59-9ea1-3ece-9a1a-5fa31b64c30c | -1.2111 | -47.0625 | 2026-01-06 00:02:00 | METOP-B | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
