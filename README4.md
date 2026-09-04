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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36bd801b-baae-3a58-967f-c6afdae0cda4 | -18.1305 | -51.7971 | 2026-09-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b639a673-3685-3751-816c-0b2c68e9e88c | -8.5048 | -54.6606 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 240.0 |
| 931c56a8-d025-30a2-bbac-2ddf727f222f | -8.5046 | -54.6808 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 191d42fb-52b1-3a54-9a9b-16634df28199 | -6.3086 | -46.1015 | 2026-09-04 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 14c57148-3cd3-3d1a-8fa8-b3b67812b015 | -8.1863 | -62.7986 | 2026-09-04 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 6858d07c-9fe4-3c05-9e16-219a09bb8020 | -18.1505 | -51.7937 | 2026-09-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f8b03338-120d-3c6b-b22c-2fa7b7dd2cb8 | -8.4481 | -54.7452 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 32d05c1a-f3d8-3f3c-88d3-07e648f415a1 | -8.5048 | -54.6606 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 420.7 |
| f76c4a78-44ef-33d2-930d-c302daabfe06 | -20.0159 | -50.0499 | 2026-09-04 00:40:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| 0a3c1e39-43cf-3fcd-87ab-5d3ca7275f6c | -8.5234 | -54.6594 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 9c0e5ee7-0366-37f8-8d27-67a86743e440 | -18.7363 | -48.908 | 2026-09-04 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 31c7fec0-cef7-338b-bb63-9d2ae1aa48de | -7.5476 | -61.3437 | 2026-09-04 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 5baa648e-2c1b-3840-9127-7dbd96bf05b2 | -6.3088 | -46.0791 | 2026-09-04 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e7c2067e-c4be-34f0-88db-e837b33158bf | -5.8321 | -52.0887 | 2026-09-04 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ba988e62-7d57-368e-82e2-9c132439522f | -8.4861 | -54.6619 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 35e9ee90-e892-31f0-a238-6287494ab3a2 | -20.0153 | -50.0725 | 2026-09-04 00:40:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| 1abb8463-dba4-3388-bdba-efc948863e51 | -8.1863 | -62.7986 | 2026-09-04 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 41914a70-ff00-35df-9a40-0b79f66c832e | -18.1505 | -51.7937 | 2026-09-04 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 69d26126-1364-31ec-9116-8ddcad3f7968 | -8.4863 | -54.6417 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 1bba3ce5-1722-35fe-b907-66ade5c6e360 | -18.7358 | -48.9307 | 2026-09-04 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a11795da-a77a-3b82-8d24-70a25986053a | -8.1312 | -54.786 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f1ecc2f8-e262-34bb-a016-8d34cd768fdf | -8.1126 | -54.7871 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| f3c44316-a538-341e-a487-2a5a0e23108b | -6.3086 | -46.1015 | 2026-09-04 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 450b8008-acd0-3d06-b6e3-86736938cb76 | -7.566 | -61.343 | 2026-09-04 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 7c0c6fa6-027f-3665-9c62-dad1a86bae16 | -8.5046 | -54.6808 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 72379122-689d-3f10-a963-74976e1e2e49 | -7.5659 | -61.362 | 2026-09-04 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d92f8753-52c0-3df7-a43f-19208b6015cf | -8.505 | -54.6404 | 2026-09-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 097432b4-ec2a-34e2-b541-742284bb472d | -18.14018 | -51.80346 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fbe140b7-9898-3e5d-a494-69e23fcdf389 | -18.734 | -48.94758 | 2026-09-04 00:41:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d9ca83c1-a002-3ba3-a829-511b73a9470e | -18.74254 | -48.91007 | 2026-09-04 00:41:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| aea78575-06f5-37c3-9e68-f4980a7df0d2 | -17.09913 | -56.85223 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| fb0ae5cd-3872-3489-9fe5-30e97b2b911a | -19.14174 | -57.3471 | 2026-09-04 00:41:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 69a4048e-831c-3391-ad56-21f7fddc2f39 | -17.09776 | -56.84274 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| bc4ac244-85ed-3bec-b79d-9769dcdd63e8 | -17.08743 | -56.83466 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| fd5ca517-951e-31e0-a60c-b13601846818 | -15.91403 | -50.18351 | 2026-09-04 00:41:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2864fc20-183d-38a0-bb00-d6b51f365379 | -18.14756 | -51.81514 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 31689e14-117e-30c2-8bad-3f7b4c5f0be8 | -16.57796 | -49.42381 | 2026-09-04 00:41:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 96c77587-e934-3667-ad9d-46774d6092e6 | -20.01554 | -50.06004 | 2026-09-04 00:41:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.5 |
| 676cc143-285c-3c5c-96cd-91cb774a87b7 | -18.14443 | -51.79714 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 792aacd5-3f3b-3775-a7b6-cf992ccc93dd | -18.72774 | -48.91295 | 2026-09-04 00:41:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 214.2 |
| f303fce6-0ff7-354a-8d86-a7bc77117eaa | -17.1005 | -56.86173 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| c0ca8456-7b87-39be-b23e-7729e539c13c | -20.01966 | -50.08292 | 2026-09-04 00:41:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.3 |
| f05dfe4d-2ad3-3e19-afa8-169b97a0d261 | -17.10809 | -56.85081 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a96ee15f-90aa-3334-99e1-58ddabd116ba | -15.90244 | -50.17918 | 2026-09-04 00:41:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4a705e75-c79a-35dd-9ded-5977cc6818f8 | -15.90974 | -50.15894 | 2026-09-04 00:41:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| c9280e8b-0244-3cf2-8a2b-de809eeb5774 | -21.7252 | -47.15478 | 2026-09-04 00:41:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 4c8167ec-92c0-3d01-9f17-02f5db2be452 | -21.45791 | -48.68053 | 2026-09-04 00:41:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7fb1dd2e-dd43-3f46-8d48-9d730298a1d7 | -18.13238 | -51.79924 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 56e58a12-300b-3272-9c35-646b1e6e413d | -18.73333 | -48.94221 | 2026-09-04 00:41:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ccb52d56-4c2b-33e3-8d97-e85c8d657666 | -17.14629 | -55.91723 | 2026-09-04 00:41:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| eb0791b4-e208-3ac1-a0f8-a254997d323b | -17.09292 | -56.87265 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 6a23b464-5a6a-3df9-8731-ec3ccab0b301 | -17.09155 | -56.86316 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 46a5430c-042c-3930-9bdd-97f854181b92 | -18.12813 | -51.80559 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f98f45eb-9191-3954-b99d-9df0d68d5e8b | -17.10187 | -56.87122 | 2026-09-04 00:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 07e6b421-fcf7-3f80-ae74-c27c4e74de96 | -18.13554 | -51.81738 | 2026-09-04 00:41:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 863280be-4ea8-3f84-b66e-a3ab3a808fe3 | -16.57656 | -49.41869 | 2026-09-04 00:41:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 75ce9d45-64d4-37e9-9ef4-c35a074b6e68 | -18.72861 | -48.91825 | 2026-09-04 00:41:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 1b45f72f-43c6-3820-b6a9-4dfa7f6d1b61 | -10.91546 | -49.61905 | 2026-09-04 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 403e4b84-68a8-33b1-b004-3f90e41168dd | -13.46247 | -57.03015 | 2026-09-04 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39d16c62-cfac-3eeb-a309-38f245ca99c9 | -10.45413 | -61.20488 | 2026-09-04 00:43:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9f7a111a-83bd-3360-bdec-71a9324c6909 | -11.94613 | -55.92359 | 2026-09-04 00:43:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10428bfa-919c-3b48-8136-01807f6c76ae | -10.5002 | -51.34011 | 2026-09-04 00:43:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8181821d-a24e-3504-b327-331488e4b0c8 | -11.51874 | -49.20117 | 2026-09-04 00:43:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 92475e37-7357-3f32-8012-f6ce165347c7 | -11.94443 | -55.91206 | 2026-09-04 00:43:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7284c7fe-0b2d-39ce-b82a-6e283ca54336 | -10.45542 | -61.21457 | 2026-09-04 00:43:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2fb2e944-7c08-3736-8866-ac9741bee5d9 | -13.47162 | -57.02868 | 2026-09-04 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ef8a76b-dde2-3415-bd98-fb3408cd73fb | -13.40061 | -57.04566 | 2026-09-04 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5a0b2c30-3ce9-3600-b9d5-bd5812413e82 | -10.3141 | -50.33382 | 2026-09-04 00:43:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a192e723-0473-38a9-ac04-683d788d3398 | -10.65442 | -61.76257 | 2026-09-04 00:43:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c8c8413b-1d37-3d9f-9113-d82ad9d7c761 | -10.32019 | -50.33807 | 2026-09-04 00:43:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 2d80b361-b635-3aff-84a1-953b0626518b | -12.16293 | -60.76411 | 2026-09-04 00:43:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5e9ed0f-df05-388e-9f09-7e3ce28e20a8 | -10.51568 | -57.4422 | 2026-09-04 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 14ec610d-8759-37e5-9a11-c71ec20458b2 | -9.8337 | -59.47855 | 2026-09-04 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8cadb0af-b952-3683-9e5e-474777664491 | -13.30198 | -61.09975 | 2026-09-04 00:43:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4eec375-1113-30c0-8336-8694fd2e47cc | -10.6531 | -61.75229 | 2026-09-04 00:43:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d051a67a-3386-3b10-aa58-a9ed71f8b0ea | -7.37118 | -60.60375 | 2026-09-04 00:45:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 39a5415d-981a-35da-b699-2930717c6115 | -7.8034 | -63.42233 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d5f7663c-ec85-397b-adf6-77a9b44018e9 | -7.5616 | -61.33362 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 23707754-e121-3ec4-8af6-7e702959f5a8 | -10.29443 | -68.84607 | 2026-09-04 00:45:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8ce4dba7-5663-3f82-9ed1-a30efd4a4a7a | -7.55408 | -61.3499 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1a20e8bb-5a0a-3c0c-b2bc-ef14d6215ad6 | -8.19075 | -62.7993 | 2026-09-04 00:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c7564275-3650-3583-97cd-c95062c639f0 | -8.11521 | -54.79948 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 685690ac-605f-3e6c-b2dc-4473b55c702a | -8.6068 | -67.17976 | 2026-09-04 00:45:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| a520173a-cbbf-3828-b2bc-e446c4414d20 | -9.035 | -65.74058 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8a0356b2-1803-30c5-bd22-2dcfdca2e34d | -9.104 | -65.49505 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7f6f7d3b-ee0c-32b8-becc-10f426aa6aa1 | -6.98986 | -62.98467 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fcfb65a9-5e15-34f2-be46-f28b001a3d8f | -8.67114 | -66.95591 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 1d1fcd9d-3376-3639-8195-9e09b897e8e1 | -9.11065 | -65.50552 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 26fd6b16-b2ce-3fac-97b3-c111d5bff78a | -7.57586 | -61.30353 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1af4da34-599d-3562-8d9a-51984e0f5d22 | -7.01065 | -62.99286 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d532d119-004c-3cf5-9f35-2cf3c3322668 | -8.11032 | -54.7678 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7a806c2c-3035-3a30-b2e5-b06f3e65d34c | -9.04732 | -65.73891 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7e0a78bc-4c71-3264-8ca3-bedd84936fb5 | -7.78872 | -63.38848 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b84b6bcd-40a6-3975-b949-205648efb8bb | -8.52861 | -67.17221 | 2026-09-04 00:45:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 6693ddb4-8169-30cd-bc71-f159edcd64aa | -9.89909 | -64.82317 | 2026-09-04 00:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5eb92af8-4613-33b6-9e7c-56ba900df18f | -8.46522 | -54.74169 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 880b567b-f9bd-3a18-805e-af6d88b56c9f | -8.50781 | -54.64805 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 4368e3df-6021-32e2-9d3e-705f80878dd7 | -8.77601 | -62.57841 | 2026-09-04 00:45:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 20c103cb-2887-366d-a025-7d0586590683 | -6.1601 | -57.76357 | 2026-09-04 00:45:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ac6e31f-bb73-34d6-b520-538310d9ccb2 | -8.60036 | -67.18727 | 2026-09-04 00:45:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README5.md)
