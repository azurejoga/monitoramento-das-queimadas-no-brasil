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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3635094-1a24-3964-8cc7-f2bffc783adf | -9.85492 | -61.43234 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fc32ff5-c580-392e-9fd6-72295bb98672 | -8.90969 | -60.60521 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 88f9d2ef-4c27-3c2c-abb0-268be9b2fd44 | -8.91643 | -60.76241 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41066d29-7076-317d-bdfb-719ff935b9f7 | -10.2217 | -59.411 | 2025-08-06 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 99e9b294-d96f-349e-a342-fc99b764a2fb | -8.91821 | -60.54761 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f7886a9-61f4-32bf-b8df-755dcda30a3d | -9.83115 | -60.7566 | 2025-08-06 05:38:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51bf8de1-d089-3634-a31d-da566bdf1359 | -8.90053 | -60.59023 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09971ba7-0017-31e9-ab3e-1443659faaa1 | -8.91775 | -60.60191 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4d9981b-5b95-31ae-83cb-a29cb686e568 | -11.32426 | -55.22014 | 2025-08-06 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be2bd35c-5079-330a-ac53-c3143d304f93 | -8.91799 | -60.57473 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e79460e2-07d1-3292-8bd9-994b88e770e5 | -8.91493 | -60.56974 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7de1b47-3029-322b-94f4-4e1304a7411c | -8.91886 | -60.54319 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42ccc2c4-5213-3b50-9ab1-b7488c40d56a | -5.59517 | -51.13343 | 2025-08-06 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae04e0ac-b01b-303e-b64a-bdf952d13ecb | -8.91536 | -60.59249 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| ba4d0a88-eb6a-3a8a-b97b-cdf56f59b446 | -9.18073 | -60.83161 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27e12f7d-988a-3da5-89f5-10853bf872a9 | -8.91406 | -60.75321 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ea3d192-a76c-3b4a-adde-821a3acc7cb7 | -9.8256 | -63.23719 | 2025-08-06 05:38:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ee29f3-40e0-3d8c-8e8b-7be10464bcef | -8.91578 | -60.76675 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 25aeca08-c656-3631-b911-2dc76f47576c | -8.90445 | -60.56365 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 84a26737-9a8e-3d71-a492-aabba0f3e89e | -9.50941 | -63.5275 | 2025-08-06 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e95bec-140d-3ba0-be94-f80dfebb1a8b | -7.01287 | -59.83773 | 2025-08-06 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5012d43b-3c67-323e-a226-66a45cd5eb6c | -5.59371 | -51.1276 | 2025-08-06 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21c025f-4a9f-3a6c-af32-42ba19633a4c | -8.916 | -60.74022 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 00a5f514-0c55-3c0d-ad66-b36594c70a86 | -8.9193 | -60.5659 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7bc0150-9c1a-3a3e-a372-e2300779efb7 | -8.90118 | -60.58581 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0732a57e-8495-33c9-bfc6-24dec3eaa8e2 | -8.91034 | -60.6008 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d70a88be-a99f-375e-93bb-97b6e31a5e9a | -8.92146 | -60.60248 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e37407c0-c4bd-3373-8f4c-d6cea43b3d87 | -8.92039 | -60.58415 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85611978-1161-3c49-bc80-d08ac0cfa32e | -8.90947 | -60.55535 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| dfaa965c-8879-3853-bb8a-e00c0fa18d38 | -8.91471 | -60.74888 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cb1482e7-4e89-390c-82f8-7699a3433e1b | -10.62409 | -55.31138 | 2025-08-06 05:38:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcc9aa0e-4b2b-376b-bc35-ab266676a91c | -9.71067 | -61.29838 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6332d6b-b7d2-3d00-a8e1-e14d3014b644 | -8.9241 | -60.58472 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6d48b047-8a07-35ef-a1e2-2f14a903f0fc | -8.9038 | -60.56805 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0aeeeb21-9f46-398c-ade2-d8799519fa59 | -8.91665 | -60.73588 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4a6eac06-216b-3720-aa7c-a2411996c480 | -8.92127 | -60.5526 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ed8cfc8-0657-301f-bd8a-3ce66bf0b4e6 | -8.91339 | -60.60575 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| eb7cf8be-8630-3833-9215-899828685f44 | -9.18504 | -60.82781 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49d469f5-1838-36bb-91cd-5a4d80e3b02b | -10.62947 | -55.31222 | 2025-08-06 05:38:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b809996-adaa-3bd4-aaba-f695c4df1955 | -9.65504 | -62.94102 | 2025-08-06 05:38:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64d9d144-76ba-34f4-83c2-fc10c45b1ba1 | -8.90138 | -60.55865 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 56782835-60ba-316e-a381-5dfe37d66ea0 | -8.92034 | -60.7364 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e5a4fdd7-564d-36a4-bf40-3cfd877dca35 | -8.90663 | -60.60024 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 1508f148-e08e-3ba9-8369-b942111e4a91 | -9.51275 | -63.52803 | 2025-08-06 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 142aa7ea-f976-3483-be59-ce4517aa513b | -8.90073 | -60.56308 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 48ce00ba-d39b-3177-b6e7-75187d88533a | -8.91297 | -60.58305 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 136d0e87-4ab2-306f-9bda-c873332dc417 | -8.91187 | -60.56479 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| efc5d967-92fe-307d-b0b2-45a1161a84b4 | -9.46737 | -57.85011 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 145a6088-2bae-3b53-b9b7-572b98fe7dfc | -8.91428 | -60.57417 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c100c30-dc7a-3ae8-8090-b4adefcc33ca | -8.91341 | -60.75755 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ac244b-c04d-3978-91d4-20a69a1b18de | -8.91252 | -60.56036 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2a2a28ec-3d2d-3536-9429-4d0b7754c5f4 | -8.90315 | -60.57248 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6322f013-5c5b-3e0e-800c-9fc86578bcb3 | -8.92236 | -60.57088 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 402c58d2-ac07-37f7-828b-cbfe1f24a8cd | -8.9171 | -60.60632 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8f341d5-9c7c-3787-98f1-4da501f8a788 | -8.90991 | -60.57805 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 84c93c51-b107-39d9-b705-60a70c295317 | -8.9158 | -60.53819 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 872f451e-8c27-3669-ac7f-bc9fd795ac6d | -8.91012 | -60.55092 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b4d95db0-7fbf-3612-9b58-14a606dd93e0 | -8.90598 | -60.60466 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 413bee60-ed08-3561-8be6-af537656ff72 | -8.90424 | -60.59081 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 7c1d4c30-3a30-358b-92c3-1f3b8d2a4ab3 | -8.91535 | -60.74455 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e0cf355-7fb6-3c94-b323-93daced3fa38 | -8.91122 | -60.56918 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2b1870f8-16e6-3b89-817e-010aefa13d4d | -9.18872 | -60.82835 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3aa5331-48ee-3118-ba74-9cc18ce15909 | -9.70282 | -61.30147 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d273b2-2ca2-3f2c-b74e-35967d3b8abf | -6.41499 | -53.36775 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0df98a89-1daf-3e64-a846-b64885dfc45e | -8.90926 | -60.58249 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b2de69fa-218e-3f50-ab40-bca227c25f2a | -8.91318 | -60.5559 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 0abce439-af98-36bd-9ab6-72bb789fb0d2 | -8.9062 | -60.5775 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b7317d02-3b17-33c2-8c26-cd77fb008446 | -8.91839 | -60.7494 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 87acc4ac-165d-3ea2-89c7-f98b7ddce602 | -8.91231 | -60.58747 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 52152ad2-c3b1-33c6-b223-3f3877cd1bf2 | -8.9064 | -60.55035 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f33041-8d59-3ac3-acac-9d9034de62c1 | -8.91864 | -60.57032 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 093ea261-422c-3c8b-ab52-fe687e9ddf30 | -8.92564 | -60.54873 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f44787-2fea-326d-80df-f981a0ca9c99 | -8.90794 | -60.59137 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 17a847e2-5464-30ab-a8bf-19c657ba8327 | -8.91057 | -60.5736 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5beb4e10-a3fc-3c57-966c-26e4987dca36 | -8.91668 | -60.5836 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 27aa92cc-62b3-3cf0-b110-f924cc3ad439 | -8.9147 | -60.59694 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 31c57c3a-524e-3269-b45b-8fbf7809d408 | -9.1844 | -60.83215 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20316623-1375-3227-930f-a8bc8f458700 | -6.26569 | -53.63721 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b80e96b4-e8cf-356d-a204-ee0a9f3e3e90 | -6.41555 | -53.36377 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ef6b8c-e712-3d67-bbf9-8a25f3069e20 | -9.70345 | -61.2973 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea7725ec-4d36-36a3-ab4e-1b2d7fb46da5 | -8.91165 | -60.59193 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 6e6d2a71-1df3-3abe-bd2e-1ddfa3970ba2 | -9.8305 | -60.76105 | 2025-08-06 05:38:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4943d37b-ddd8-36ce-a450-42655cca376f | -6.41388 | -53.37572 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3449516-1136-3eec-b647-6fd704694b71 | -8.91907 | -60.59304 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fccd59c0-49d2-396e-a936-bc267fe6f59c | -8.92476 | -60.58027 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 693c690f-0676-3e70-9bfb-894272c96214 | -9.69077 | -57.42442 | 2025-08-06 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710aecda-2a88-30e0-b7c7-6a2178878f1e | -8.91559 | -60.56535 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5116859a-ff5c-3d7c-ac3b-361db86da072 | -5.59296 | -51.1332 | 2025-08-06 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de1357b-a640-362f-be5c-ab1716446c61 | -9.46033 | -57.83574 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 002730d2-ad84-3899-b191-61d0bef05f28 | -8.91973 | -60.5886 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eb888604-ac2f-3e9d-8c25-eb22435f2cf5 | -8.90575 | -60.5548 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c2d2e0c2-7a3e-3119-baf2-6489a09ea72a | -8.91602 | -60.58803 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 07b18e62-6d72-39b7-8ea4-eb4e3186ecae | -10.75952 | -60.74822 | 2025-08-06 05:38:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48f81da-562a-34d2-9a88-75a5e12dfe78 | -8.92498 | -60.55317 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a3f5fb7-0b2e-38f0-98f6-14a6f2da8a92 | -8.92142 | -60.75426 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3d8e9555-054d-3606-aee9-5200cdb20929 | -8.91099 | -60.59639 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 3bc14249-cb42-3dcc-9f23-d52990355856 | -8.92516 | -60.60303 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e39245f-4e1e-379d-a214-b5cc5ac26120 | -6.41444 | -53.37173 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b52de9dc-5178-36c6-9fa9-106990cd1c2a | -9.93295 | -60.48016 | 2025-08-06 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1123199-03b5-31ff-8964-515d567fba3d | -8.92278 | -60.59359 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README28.md)
