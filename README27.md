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
| ba1a7f98-a58b-3d87-8824-bf0c5331561f | -17.6471 | -56.3084 | 2024-10-14 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 9eeb8a0b-7970-3f38-9f28-e99b58628a3c | -18.2562 | -56.478 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 41a46a3a-067d-3aed-9fb5-175f62d73bd5 | -18.2559 | -56.4988 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.2 |
| 61668d4a-dc5e-37ab-a474-6ea592944e4c | -18.2555 | -56.5196 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 120dd376-9272-365d-b38e-4d6fa7b16fdd | -18.2346 | -56.5847 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 9a30d550-8641-39f3-818e-768230431296 | -18.2342 | -56.6055 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 8463b2b1-f373-3ab4-ac9e-704eeccf6ee1 | -18.2338 | -56.6263 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 72f7573e-0cac-3fbd-8b3b-b1ec74c5a690 | -18.2147 | -56.5873 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 19ebdf1e-c58d-3f13-9802-e781338ac75e | -18.2144 | -56.6081 | 2024-10-14 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 4cc2f5d3-8143-37a8-9e79-d11a42b622f1 | -2.4344 | -46.9195 | 2024-10-14 02:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| baa27b84-b59d-3143-b03d-f8cd5386500b | -2.4529 | -46.919 | 2024-10-14 02:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d00c5590-fe11-31c5-a2b1-e38452cf62e2 | -2.6118 | -49.0985 | 2024-10-14 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| b8dc9729-d069-3405-8ae3-69d419333b1a | -2.6119 | -49.0772 | 2024-10-14 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3b4dbc3c-4927-36c3-a1e5-f39101749d8f | -3.2889 | -42.8561 | 2024-10-14 02:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c021b7c8-7773-3c41-9f7d-930df564c2c1 | -3.289 | -42.8327 | 2024-10-14 02:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f55e50bc-4b91-3674-b134-c410d92ca500 | -3.3076 | -42.8553 | 2024-10-14 02:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f24fc492-2ddb-3f71-93d3-ad3db9ce9bee | -3.3077 | -42.8318 | 2024-10-14 02:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| fbbc2a26-e2b8-35df-b386-964312627a04 | -3.3264 | -42.831 | 2024-10-14 02:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b94859ab-455a-32b4-a076-5e8265b08e63 | -4.1149 | -48.2299 | 2024-10-14 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 877fd3c3-d894-32d1-969e-cf5e29ab505a | -4.6384 | -44.8615 | 2024-10-14 02:35:33 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 33f0ea35-cef2-381c-857c-bb8de30a5650 | -6.2141 | -48.329 | 2024-10-14 02:35:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8483c5f7-c280-3765-880f-a99d0216284e | -7.9418 | -63.6365 | 2024-10-14 02:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8d8991a4-3eb8-3fef-a806-bb2cc3a52ed6 | -7.9603 | -63.6359 | 2024-10-14 02:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 22e9ca93-3f71-38f8-9173-a88180a55334 | -9.1043 | -61.162 | 2024-10-14 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 760ba295-953d-3523-9493-a194cd05ed42 | -9.4699 | -45.8249 | 2024-10-14 02:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 6cf392e5-55c9-324b-a9f3-55a3163a80d3 | -9.4702 | -45.8023 | 2024-10-14 02:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4d3a7a05-9cc1-3653-a784-06d81e9f29b6 | -9.4888 | -45.8228 | 2024-10-14 02:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 76b19b95-db96-33a5-a202-ec18dccc1aa8 | -10.0619 | -44.2624 | 2024-10-14 02:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 240.8 |
| fb091641-def3-3639-9364-e681c7bc6d47 | -10.0622 | -44.2391 | 2024-10-14 02:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 3f3466ae-16c7-32ef-ad3b-77da8329939d | -10.0809 | -44.2599 | 2024-10-14 02:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| ec1af0e8-6488-3ab2-9b0f-2f38f4bd97e3 | -10.0813 | -44.2366 | 2024-10-14 02:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 243.3 |
| ec946ce9-c718-31a7-a109-c8a6a233880e | -10.0816 | -44.2133 | 2024-10-14 02:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0741528e-f0df-3b48-b63b-ca0889a150e3 | -10.0163 | -47.3308 | 2024-10-14 02:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| f27f4e9c-16e8-3c22-a743-dfe8c5c379a0 | -10.0166 | -47.3085 | 2024-10-14 02:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b6114dc6-176f-3201-a85c-ae5f8c521e46 | -10.0352 | -47.3286 | 2024-10-14 02:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1e92a12f-5d2a-31e6-b022-35fb84adb613 | -10.4313 | -44.9541 | 2024-10-14 02:36:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 68b6ff76-909c-3cee-8833-3d25a7fb424a | -10.4504 | -44.9516 | 2024-10-14 02:36:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 886f5058-09eb-3369-8068-cbed4f05597f | -10.5307 | -49.7843 | 2024-10-14 02:36:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d029a95c-104a-3388-84ca-fd1c1921a486 | -12.3804 | -53.1376 | 2024-10-14 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 2f546fd3-f4a8-33af-ad59-bda179cc3ec0 | -12.3807 | -53.1167 | 2024-10-14 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 215.0 |
| d37155e4-1889-3115-a6f0-772f5285ae14 | -12.381 | -53.0959 | 2024-10-14 02:36:17 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a87072f2-b0eb-3696-8e5f-d9844842077d | -12.3994 | -53.1355 | 2024-10-14 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 08839264-6c91-3837-972c-aee972d2260b | -12.3997 | -53.1147 | 2024-10-14 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 251.4 |
| 12f68524-84f5-3107-927d-8a63a205a31a | -12.4 | -53.0938 | 2024-10-14 02:36:17 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7cc49e4e-e45a-352a-82cd-a38981e23791 | -13.1475 | -62.3215 | 2024-10-14 02:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 76b721f6-d5dd-34de-a8d9-52199149d85e | -16.9995 | -57.4791 | 2024-10-14 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 90eac52a-9d23-3485-ad17-2f295d6eff1e | -17.0197 | -57.4358 | 2024-10-14 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 63eed1e5-e751-328c-a746-00bb21474761 | -17.02 | -57.4153 | 2024-10-14 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 85725c6d-a3bb-3854-8895-f387774f489a | -17.1957 | -57.4562 | 2024-10-14 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 124ec998-7874-38a0-ace0-4365804cccb9 | -17.196 | -57.4357 | 2024-10-14 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 2f982f0b-b8b9-3e18-ba5c-9cd56efb5512 | -17.6471 | -56.3084 | 2024-10-14 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| e3f7f42d-dff6-3ce0-b44a-f8bf97eee381 | -18.2555 | -56.5196 | 2024-10-14 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 712ff9fd-8421-3d86-9de5-f9a76d6cdfb7 | -18.2559 | -56.4988 | 2024-10-14 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 9d6595fa-dabe-31ec-afe3-999b24ac7922 | -18.2562 | -56.478 | 2024-10-14 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 6352f10f-b35f-325a-8415-c4e747e7c0fd | -2.4529 | -46.919 | 2024-10-14 02:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bfc9b591-6cab-3ef9-8111-bf4a1c476e61 | -2.4344 | -46.9195 | 2024-10-14 02:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 73495efb-6261-3cc7-b6ba-3cc79cbf7ac0 | -3.3077 | -42.8318 | 2024-10-14 02:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6cf2aa39-530c-3140-87cf-7190f8ec814b | -3.3076 | -42.8553 | 2024-10-14 02:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 3b0985f2-637c-3534-8194-abc4bdec4aa5 | -3.289 | -42.8327 | 2024-10-14 02:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 4f12aad2-2729-343b-a53b-91c55aa08bd4 | -3.2889 | -42.8561 | 2024-10-14 02:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 2aa9f4eb-bcab-3848-9933-721bbeba7868 | -3.9299 | -56.034 | 2024-10-14 02:45:29 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| a2f3b1b4-e98b-3ec0-ada5-a20557ebde61 | -4.1149 | -48.2299 | 2024-10-14 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5904ea31-5b90-3d38-9a83-4cf5a0890ee4 | -6.1955 | -48.3302 | 2024-10-14 02:45:41 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 57f1a676-55f5-3606-86ca-82101545f83b | -6.2141 | -48.329 | 2024-10-14 02:45:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 7d3f8727-38c8-3fe6-ad15-86d7d729d715 | -6.2328 | -48.3277 | 2024-10-14 02:45:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a115690f-7b76-3be3-9b2d-d0cfdecef2f3 | -6.2143 | -48.3073 | 2024-10-14 02:45:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8021547e-3ca0-348f-ac10-32f53e0a9c52 | -9.1043 | -61.162 | 2024-10-14 02:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f391f349-b28b-3f52-b40d-11f5882035b9 | -9.4888 | -45.8228 | 2024-10-14 02:46:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| ef33e0c3-82bf-3326-98a7-bc5b3e355770 | -9.4699 | -45.8249 | 2024-10-14 02:46:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 8eb46347-7939-3eba-9def-d406eb69b64d | -10.0816 | -44.2133 | 2024-10-14 02:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b351b9e4-e7f5-3177-b7f1-df07c39edec1 | -10.0813 | -44.2366 | 2024-10-14 02:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 10662b07-619b-3962-a1ca-8e04eceda738 | -10.0809 | -44.2599 | 2024-10-14 02:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| b92725bc-8acc-3589-8fbd-0f5a554797a3 | -10.0622 | -44.2391 | 2024-10-14 02:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| a846d2a8-33f4-3d56-bbcf-d2ebaacfb68e | -10.0619 | -44.2624 | 2024-10-14 02:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 4867143c-b00f-3bfc-a442-1a79c5548822 | -10.0163 | -47.3308 | 2024-10-14 02:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 78890413-1919-3e57-acd6-b92732bdb67f | -10.4918 | -42.433 | 2024-10-14 02:46:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 75.9 |
| fcc81fac-3132-3507-b4dc-949a43b1d09b | -12.3997 | -53.1147 | 2024-10-14 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 175.0 |
| d82c796e-b262-3282-ac23-cd27e8c4bc73 | -12.3994 | -53.1355 | 2024-10-14 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| bf3d8977-75c8-3b44-8dc1-28e779019cfd | -12.3804 | -53.1376 | 2024-10-14 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 5631ff8e-f633-3da1-b5ad-a4da68b863bb | -12.3807 | -53.1167 | 2024-10-14 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 25b70492-ade4-3314-a0d5-bffda92fd13f | -13.1475 | -62.3215 | 2024-10-14 02:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 939e753f-3dfc-3756-89be-29cf454c58d9 | -17.1758 | -57.479 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 6e785b4b-5501-39d1-b194-d75f81e3f369 | -17.1761 | -57.4585 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| d6f6f326-7d54-3cf7-a918-07ba4082e58e | -17.1764 | -57.438 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| c237b492-d03f-313f-a612-1a6052248da2 | -17.1954 | -57.4767 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| e09d8ab9-a6c4-3f0c-a7fa-5c3fc2ae4acc | -17.1957 | -57.4562 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| b31a759c-3cfc-3c11-98ab-db370d6dcf96 | -17.196 | -57.4357 | 2024-10-14 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 3f0815ab-0f48-3f11-8fd8-b6fb6be73c06 | -18.2757 | -56.4962 | 2024-10-14 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| d90d49f4-fd04-32a1-9e6e-4ace3254856d | -18.2562 | -56.478 | 2024-10-14 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 68822ed4-4aaa-3efc-ad5d-d94a9f91982a | -18.2559 | -56.4988 | 2024-10-14 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| c688ec02-4419-38ac-ad2d-9c2a398ce22a | -18.2555 | -56.5196 | 2024-10-14 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 4f3c1ead-332b-3adf-ab54-d4db6969897a | -2.4529 | -46.919 | 2024-10-14 02:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 424ba89e-2ddb-3744-9b6f-c477984a6eb9 | -2.6119 | -49.0772 | 2024-10-14 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 2753ef6f-8870-30ad-923a-7977a9ad8c15 | -2.6118 | -49.0985 | 2024-10-14 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 7f9985ec-5da7-33e8-95db-fc147a032f79 | -3.3264 | -42.831 | 2024-10-14 02:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 68b38873-6fe5-3801-ba3c-1c1e89c09e1f | -3.3077 | -42.8318 | 2024-10-14 02:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 9f41a566-ca59-31c8-baac-aaad6f71e7ce | -3.3076 | -42.8553 | 2024-10-14 02:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| cc20fc1d-620f-3949-9316-77bea0a4b57b | -3.289 | -42.8327 | 2024-10-14 02:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 899fe4f5-809c-39af-a9f9-76b2c4ee5f4e | -3.2889 | -42.8561 | 2024-10-14 02:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f72d6a17-32d3-3222-991b-4bfdd151933f | -3.9299 | -56.034 | 2024-10-14 02:55:29 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |


[Clique aqui para ver as próximas entradas](README28.md)
