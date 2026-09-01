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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb7b435-427c-307b-b9a1-13400000ae71 | -15.17209 | -46.24275 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66bc0924-7158-3d99-a355-cda4813a515b | -14.39306 | -52.53006 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c3126318-3509-311d-854c-77b5c37a61e4 | -13.38416 | -51.75055 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f1de0e2-95aa-3359-ab8d-d755d1967eb3 | -14.45981 | -52.51488 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30beb8ad-12ea-392a-9da5-771d4e2ef014 | -15.25134 | -53.88636 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52b22776-7d85-3d20-b0a8-7746b55125da | -14.66404 | -53.54777 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1671c12e-a12f-3a9f-8201-30a74642192a | -14.46707 | -52.51244 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377547d2-cd51-323b-a180-62890a1e9d14 | -16.48073 | -47.95184 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0091e0d7-b39b-34fc-88ab-b4ba58ad3a95 | -17.39037 | -42.35173 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e73b3f3-2918-3e98-ae0e-85aaa30037b0 | -14.67217 | -53.54119 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 799a7a31-8030-3106-89af-dfdc4098c244 | -15.63718 | -56.38543 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c81b047a-e802-3dd7-bd73-bf65acd9c74d | -13.33024 | -51.72652 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e28a825a-d54d-3a32-aad3-4346891dc907 | -15.40088 | -52.71454 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b93035e-6660-3604-b63a-f72f922a1997 | -14.57639 | -52.10556 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5dba604-ea6f-31ec-917d-edbf9fc53bc5 | -14.67671 | -53.59666 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa23624e-2d47-38ab-b4a0-4596948cbccb | -17.19082 | -54.31234 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ff00fe3-76e5-3e25-b74f-fbaae53a1bea | -15.24744 | -53.84551 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c44728f9-d22c-3681-aa74-b54c41211929 | -17.18804 | -54.30778 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da86b036-1f5d-39f4-8386-c41f0326d74a | -14.59203 | -54.1208 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae853a35-6b72-3d0a-81a2-aad51a5f9660 | -17.22891 | -53.26477 | 2026-09-01 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a711561a-7945-3970-862c-4f88f7e5c664 | -14.39248 | -52.5337 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9116657d-7464-3ece-aa99-bd4946a40c08 | -14.03055 | -47.80775 | 2026-09-01 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa481d5-766f-37c5-b258-209a44b3cab3 | -15.03113 | -52.7682 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe3e9bd9-0f6b-3013-9cc1-a331d0ce2ec4 | -15.8686 | -56.49113 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4b7e952-86e7-363e-a669-7ff9019346b7 | -14.58547 | -54.11251 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c0596f0-577b-3ae3-b899-5aac670a66d8 | -15.24399 | -53.84489 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96023de3-60cd-3695-bcaa-207e6621587a | -17.18409 | -48.71725 | 2026-09-01 04:42:00 | NOAA-21 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2d3033fe-f6dd-3fa1-b1f0-a13968ea4341 | -14.66467 | -53.54391 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c49fe938-f26e-3ae0-ae25-c6b67362f11a | -13.3308 | -51.72298 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90a5c537-0248-34a2-8266-900cfd8b49c7 | -15.18488 | -46.24035 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c059035-d6e7-36af-97f4-a918f9f9d66f | -13.19336 | -44.07591 | 2026-09-01 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd238962-87ae-32d3-808f-d562b3f71458 | -12.8943 | -45.84002 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 186bc1e1-4be6-389a-afc8-affacc3d7e84 | -14.50822 | -52.23405 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4ce1c3f-157f-3a53-893e-c9b9c7c2de18 | -17.38569 | -42.35613 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f7b2d846-e18c-3b53-b470-0351da9f101a | -16.13002 | -47.49026 | 2026-09-01 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19bb8c67-686a-303d-a617-69dd28e86b33 | -14.02688 | -47.80726 | 2026-09-01 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9b8156b-1759-35c1-831f-1d17a9cc8d90 | -14.73488 | -53.58672 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 422b9abb-2054-3c39-b19d-58cabd671caf | -17.3846 | -42.354 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21304edc-ac01-353b-8ab8-fe2c4d9827dc | -14.41166 | -52.49961 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb30f00c-e3de-3847-a546-35f019f108c2 | -14.69173 | -53.59132 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560a6a9c-016f-3fe9-9061-1112605d9f67 | -16.93329 | -47.91918 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1141f886-1f06-3da6-9c74-88f0da6f0785 | -12.38223 | -48.15824 | 2026-09-01 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40ecc6f7-d9d0-3fc1-b741-5d5519782854 | -14.4508 | -48.99832 | 2026-09-01 04:42:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2d66c68-daad-31ec-bd76-10fd42ea575f | -13.27944 | -48.55387 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b72b0054-8e81-3aae-9e47-482adeb09aff | -14.27563 | -52.89414 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a39f2f89-8e23-39d0-a145-ed4715338646 | -16.44703 | -51.40422 | 2026-09-01 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 832416be-eb1b-32b4-a860-3823b58f5471 | -16.54369 | -49.57138 | 2026-09-01 04:42:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 202bea63-3acd-3aae-a5a7-ee7015c51597 | -15.24335 | -53.84879 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fd3e08b-871d-3b63-bd06-f40052eacf6c | -15.66419 | -48.69754 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a399791-4f0b-37ff-8151-4fb4206fe7b5 | -16.36045 | -51.01594 | 2026-09-01 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8361c69c-fe1c-3a90-b794-79bb0bf1b609 | -15.40206 | -52.70724 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d817a549-42fb-37b6-a3da-ff7a646894a6 | -13.38192 | -51.76473 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19849f35-a25e-3ca5-8dee-0223d21d686d | -15.75536 | -56.09956 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f44b046c-c106-3797-b013-b4009159e2c7 | -14.72928 | -53.57788 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 420d4d2b-4f5e-3be9-a992-f1bd385c229b | -14.42973 | -52.50983 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3e390a1-0643-3714-a4ba-47eb60280473 | -12.90769 | -45.83447 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f438404f-640e-3fc4-b1f3-873d334f62ac | -16.15215 | -46.676 | 2026-09-01 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5677d1b0-87bb-3bef-95a4-243ceb14bd98 | -14.51097 | -52.23819 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dce64adf-1e68-3153-8714-2e1e9926cbcb | -13.34734 | -43.67197 | 2026-09-01 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3e0ae26-4f3a-3be0-920f-4c8ee8f02a6f | -15.49099 | -56.00431 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1706e39a-a3b9-37d2-beae-5f2d7c897c96 | -14.37968 | -52.52785 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e5f60ea-e209-387c-ac4b-30a2c869e449 | -10.95099 | -61.66366 | 2026-09-01 04:42:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 57a8069a-df5e-3594-8b50-7be9b4c6b982 | -15.39596 | -52.70253 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff8d688-0baa-36c4-97c8-a956f2a3fd69 | -14.00965 | -54.08229 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec2f7ec4-ac5f-3747-a906-c1620400c6e1 | -13.27594 | -48.55331 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0345ea33-1d79-3f25-9ce5-27a27b2ab332 | -15.168 | -46.24226 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d65cfe7-061b-38f7-b203-4a6d5dc07f83 | -13.99155 | -54.40119 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f817e04-56c1-316f-96b5-4e397eaa26ad | -15.20838 | -46.22024 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cc53ca0-b302-3400-9bb4-d43fffa2f4e8 | -14.58732 | -54.07943 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5adec14-ca3e-3dd7-8b94-0c3d16928a07 | -16.47762 | -47.94673 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c55214a7-0d9e-3138-b48f-d35993871457 | -13.44906 | -51.87779 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e678db7-1be4-3a25-9f4a-2aa3d4813240 | -14.58637 | -54.11157 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09ff1a54-ecc2-35fc-b2a4-300747e34483 | -15.64557 | -50.10818 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7133c0-66fc-38a3-960b-8528f64de8bc | -18.15539 | -49.59455 | 2026-09-01 04:42:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 520f1fab-6e67-381f-abe2-ec09106f7dd1 | -18.50334 | -48.44185 | 2026-09-01 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 631f42a3-838a-32e6-99f0-fba57171417b | -15.87137 | -56.47559 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a66c678c-3a13-33f5-a58d-790134b2b2fc | -15.21608 | -46.22494 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf9fa433-8a5d-3a29-b3ab-30120ea9da2a | -17.38349 | -42.36415 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6d845b4-b44b-31ef-8c9f-bde32a951e67 | -15.45676 | -53.96175 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27faa036-d5e7-3ff2-a799-a95aab4de187 | -15.62458 | -56.38839 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c35abf2-f4c3-3212-9e3e-edf563877a6c | -15.61039 | -56.39842 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d19120db-1268-3626-b0d6-ab2ca52b16f7 | -13.38748 | -51.75108 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 053de145-7244-3eb7-a32d-9bb70e883997 | -14.41421 | -52.4997 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0515435d-107e-3832-9d2f-e0f2862e5d52 | -14.12956 | -52.7933 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12e6b99e-8b09-3b7e-a20b-f524da3f5e29 | -18.50708 | -48.44241 | 2026-09-01 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 25c18be8-1339-3419-b551-bf588fafb16b | -14.46373 | -52.51186 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1acbf676-a63d-3b60-b519-1aa9a08e02ea | -15.20427 | -46.21981 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d31ebcff-bbbe-398e-8eb6-3dc96051f3f2 | -14.44703 | -52.50898 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60f1b5e3-35e0-3d3e-9466-9cce8fb7c902 | -12.78374 | -46.46054 | 2026-09-01 04:42:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1255c020-60e6-3d68-9185-12eca2adfd64 | -13.45627 | -51.87532 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 862cc58d-a988-37e4-a3d3-ab0dd878e744 | -15.03448 | -52.76877 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd51ca15-5f02-3410-866f-f13c4317a879 | -17.37688 | -42.37424 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67ea7545-0a86-3cac-8ee5-7264c7dbee1b | -17.88289 | -52.16346 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89160aab-51fe-3c9c-aba3-011ea93e0a0b | -10.94619 | -61.6568 | 2026-09-01 04:42:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5fa33f60-e6f3-3797-8c5b-387fc4f37315 | -14.45022 | -49.0023 | 2026-09-01 04:42:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33798d23-84b4-3e16-a7c1-84ed816b806e | -14.3919 | -52.53733 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08a4acef-9b0b-3e7e-804b-bac3580aefc5 | -16.86965 | -43.23678 | 2026-09-01 04:42:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daee2195-f070-3922-bae1-b3dce6325a3a | -14.66747 | -53.54836 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22932b49-10dc-3ea0-9b71-88ede9539f08 | -17.8798 | -50.49113 | 2026-09-01 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5789e015-c209-31c5-a4bf-bb6eb03646f6 | -17.72338 | -49.22861 | 2026-09-01 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
