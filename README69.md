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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 473a2752-274f-36b8-bbdd-06f69c45e866 | -14.596 | -54.7575 | 2025-08-22 14:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 493a705a-1a79-3376-8070-e6504fd9e1bf | -12.3129 | -50.0097 | 2025-08-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.2 |
| cba5f3bb-8aaa-33e7-9dec-707153c5a14b | -7.6559 | -46.2358 | 2025-08-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 221b05d0-7124-3e64-85be-2ef1b4310400 | -6.0058 | -44.4501 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| caa13757-6471-3ddb-b92e-b87bc3cf1780 | -10.2897 | -46.7642 | 2025-08-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 848269e3-a1e6-3655-a6f7-34686652b72e | -14.7694 | -56.0335 | 2025-08-22 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9c3a78bd-ad16-3510-8afe-0882e53737b2 | -8.3011 | -47.2873 | 2025-08-22 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 67ffe958-3c57-3a66-b81e-6214645e383b | -7.5922 | -63.4414 | 2025-08-22 14:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e3d45740-7993-33a2-9993-f7f403c403ed | -6.9649 | -44.1864 | 2025-08-22 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 58f6332b-9c79-3e5a-a9d9-499a3a9b82f7 | -7.1662 | -44.6736 | 2025-08-22 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4b1102a6-68a3-3f48-9a4c-48e9356c68fe | -12.9921 | -45.2252 | 2025-08-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| b2c2e74f-a3d8-3bc5-9a41-109f8e4ed0a4 | -7.0354 | -44.6167 | 2025-08-22 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6d913082-1f17-33fa-afa4-04dfde9a5af1 | -5.7782 | -44.787 | 2025-08-22 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 40e77aea-4552-3b9d-827d-7d50db6580c8 | -14.7501 | -56.0356 | 2025-08-22 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| d5b6954c-ae9e-3fa4-b09c-6fa23a0aa10a | -5.7784 | -44.7642 | 2025-08-22 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ffb28f44-3c2a-3df1-b231-287c1d5e260b | -12.9963 | -56.9 | 2025-08-22 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 696af0de-b9b9-3a33-a8df-b8c47da610f7 | -7.6296 | -45.2464 | 2025-08-22 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 9a892852-4707-3c6f-9a0d-f04b9492f23e | -12.9925 | -45.202 | 2025-08-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| fd542924-a2d3-34d2-8637-0efc7437bd63 | -7.0352 | -44.6396 | 2025-08-22 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 46ad63f3-0fd2-3564-8b65-313d2ec19aa8 | -13.3966 | -46.2406 | 2025-08-22 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 95ca9e3d-d5ec-3664-ba69-1b3e74d76354 | -6.5393 | -45.4546 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 837fa66d-17d1-3585-849f-68d61df35046 | -14.8348 | -47.9311 | 2025-08-22 14:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 280504c7-1e7b-350c-9bd0-c4cc8216e011 | -12.2938 | -50.0121 | 2025-08-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 7380c21e-5566-3474-860d-b63ca0b23335 | -7.6484 | -45.2446 | 2025-08-22 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 551be9ff-00a9-39aa-896d-b1ba76f6f873 | -6.539 | -45.4772 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3d482465-5f8e-37e2-a008-80678320fbcb | -14.7308 | -56.0377 | 2025-08-22 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| d04e021f-bf37-368d-b9f2-5d322b3aa4d0 | -6.5196 | -45.5464 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| ec5ac3ea-57af-36db-9105-ca63fabf5dff | -14.7717 | -45.4055 | 2025-08-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 9544d74f-537e-3155-80de-4291bb7222d8 | -7.6369 | -46.2599 | 2025-08-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2d07f9cc-8d7e-330c-b474-732bd106a99b | -7.6181 | -46.2616 | 2025-08-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 286.9 |
| 2765e33d-365e-31cd-985a-f32c9b384f82 | -6.7319 | -43.1379 | 2025-08-22 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2129a817-093b-3eaa-8b89-e91336e579b0 | -6.5199 | -45.5238 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 94161c0c-d451-37dd-a758-a600dd63e50f | -6.5386 | -45.5224 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 68a15211-bab0-3e0a-b68f-14d9671d2fb5 | -7.6366 | -46.2823 | 2025-08-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| f5b8caa5-b623-3e7b-b66d-344517e7c105 | -8.7951 | -45.4238 | 2025-08-22 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6e259626-9161-324c-8a1b-ff3cf166287f | -12.3133 | -49.9881 | 2025-08-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 74e59bec-661f-3ebc-a660-20dc8ec70259 | -14.5956 | -54.7782 | 2025-08-22 14:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 97d7f3ff-28ff-3735-a742-390e31bde2a7 | -14.7712 | -45.4289 | 2025-08-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| d5cbe16a-202e-3264-b69e-1ae9fc7398e2 | -12.9773 | -56.9017 | 2025-08-22 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 42467b8b-967a-3b6c-adc8-70fa061bd8ef | -5.7782 | -44.787 | 2025-08-22 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 5d42d0e5-35f3-3ae0-ba28-14d30d424043 | -12.3133 | -49.9881 | 2025-08-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 7a902628-ee5b-3f99-8e8e-1f1f8de7f7a2 | -7.6484 | -45.2446 | 2025-08-22 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 33b96478-eb55-3c6c-81af-482d8bee5e94 | -12.9921 | -45.2252 | 2025-08-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 17a9e229-a722-3c92-b174-3f47493880e0 | -6.0058 | -44.4501 | 2025-08-22 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 183fcebd-e099-3096-bff2-72bc0c59e6f7 | -11.3275 | -44.9468 | 2025-08-22 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2c4dc880-bfa2-33d0-8729-d58969d77349 | -12.9925 | -45.202 | 2025-08-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 6979b654-fb7c-3d7e-84bb-a8aaa106ef24 | -14.7504 | -56.0151 | 2025-08-22 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0325f2b3-00ad-3149-8d32-66e2fd73dd64 | -8.3011 | -47.2873 | 2025-08-22 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| f555c00a-8be4-3f74-b05a-c3fc1d920535 | -14.6146 | -54.7967 | 2025-08-22 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 46f39e02-74ad-38ff-914e-5727d4fad52a | -12.2938 | -50.0121 | 2025-08-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| a710534a-dc1c-3fec-a497-8a77ad3520b0 | -12.3129 | -50.0097 | 2025-08-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| f54e73ad-365f-39b2-9b08-bb7692753206 | -6.6623 | -44.397 | 2025-08-22 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f8f20bd4-c7f8-3eb0-b30e-db38a8803eff | -8.4776 | -48.2578 | 2025-08-22 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 76389788-9614-3078-8f38-5932081b909b | -5.7784 | -44.7642 | 2025-08-22 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 263f0c27-99a7-396c-b701-648be5567a68 | -13.0477 | -46.3412 | 2025-08-22 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9da752a0-d08f-31fa-b75d-efe54a840dbd | -6.4449 | -45.5298 | 2025-08-22 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 57719504-4220-37f5-be0b-db6f2eb018e4 | -13.3966 | -46.2406 | 2025-08-22 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ea3badb1-7b8d-3f22-8df8-a49956201bd2 | -6.7319 | -43.1379 | 2025-08-22 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c2e932bc-0e0a-3a9f-8008-6a3a21e9121b | -12.9963 | -56.9 | 2025-08-22 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a11e2b05-89e5-38a1-affd-a619e058a229 | -8.4588 | -48.2595 | 2025-08-22 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 82a0afcc-1de9-38f7-8d19-974eb6631fa2 | -8.613 | -62.6118 | 2025-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b45e0d9f-588f-3534-9b65-8b5be6601f65 | -7.0354 | -44.6167 | 2025-08-22 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a074f51c-7a18-3a41-9353-7392604ad73c | -14.8348 | -47.9311 | 2025-08-22 14:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cfb80e70-1482-36ab-9716-e670a7a428fa | -12.5042 | -53.8091 | 2025-08-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 05db1bb4-1e8a-328b-8e10-e1c856394320 | -14.7501 | -56.0356 | 2025-08-22 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 187.5 |
| ad2bd7a1-148a-3fd3-ac03-8e79b41a80e8 | -9.7446 | -62.7725 | 2025-08-22 14:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 668de586-aec6-38c5-8b6a-fd7267da8b58 | -7.6107 | -45.2481 | 2025-08-22 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7b59019c-d210-3d11-a646-555b5b1cf452 | -8.7567 | -45.4733 | 2025-08-22 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2523df16-301f-3aa5-b797-a60897b45695 | -14.6336 | -54.8151 | 2025-08-22 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1bd0de10-4f1a-3bf7-b4d3-d94c980de0ff | -14.7562 | -45.2219 | 2025-08-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a67b913e-6340-3c79-8c41-036760caae02 | -7.5922 | -63.4414 | 2025-08-22 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 187306f8-b58c-3ba0-a4b7-7b3f3796cbf9 | -14.7308 | -56.0377 | 2025-08-22 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| adf71405-316f-3bc4-859e-95b5a0ef5c8c | -7.6181 | -46.2616 | 2025-08-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a1212247-b01e-38c0-812d-3d93d3face65 | -8.6129 | -62.6308 | 2025-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ba2d519d-ce40-376e-88f8-e70b02e99e7e | -20.2492 | -46.7017 | 2025-08-22 14:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 90656614-3eff-33dc-9a33-90d4f23a328d | -6.6621 | -44.4199 | 2025-08-22 14:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7a198b74-27b4-3028-86da-0b118b2ae562 | -6.9649 | -44.1864 | 2025-08-22 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 208.3 |
| d68e7b3f-4892-3b23-b5f8-173d404793e4 | -6.9652 | -44.1633 | 2025-08-22 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| bd7e6c61-6071-35b6-87a4-503822581398 | -7.6559 | -46.2358 | 2025-08-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4157d028-3dea-3ab3-8922-62004b6f6563 | -6.5393 | -45.4546 | 2025-08-22 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 950fb350-8d50-3c7d-a4fa-b257602439c9 | -14.6713 | -54.8728 | 2025-08-22 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3c6d8b77-6e09-36fe-89bc-2b350c2b445e | -14.596 | -54.7575 | 2025-08-22 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| bc3ba469-61af-36bd-9ca8-09b87da85f8a | -7.6486 | -45.2218 | 2025-08-22 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3a69e08f-c78a-3ac8-8968-1c612271c714 | -11.3084 | -44.9495 | 2025-08-22 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 97a955b8-eec2-37ff-8b9e-50f32860bc48 | -14.5956 | -54.7782 | 2025-08-22 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| cc3947cb-ca85-3850-aca6-19ad2c463e15 | -7.6366 | -46.2823 | 2025-08-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7c3ff1c8-fb17-3366-bfcf-691e5d9bd488 | -12.656 | -47.7947 | 2025-08-22 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a3da7fde-af83-3dbc-9a45-70e58d01e823 | -7.6296 | -45.2464 | 2025-08-22 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 21c611c9-1e70-3cb9-9470-9beda5ef2edc | -10.8757 | -50.8376 | 2025-08-22 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| fd8a45ca-2360-325c-ba77-825bda61fb01 | -6.0252 | -44.3798 | 2025-08-22 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b60d9416-a9ce-35fe-b67e-4a48368aaf18 | -8.8736 | -62.4115 | 2025-08-22 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fec20eca-45db-3f20-811c-15730065a995 | -14.7694 | -56.0335 | 2025-08-22 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 11ccc64e-6b09-3f24-9404-e7bbd638f315 | -7.0352 | -44.6396 | 2025-08-22 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 423d7094-8ebc-3942-8a37-2688aa662a87 | -20.2492 | -46.7017 | 2025-08-22 14:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 040493a5-21af-3bc9-8726-5a7f5783963c | -7.6486 | -45.2218 | 2025-08-22 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 94737805-ca39-3b5a-8827-c44a3e52854f | -13.3966 | -46.2406 | 2025-08-22 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 9d103257-642c-3050-b015-c564260cf2e2 | -6.5393 | -45.4546 | 2025-08-22 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2a8f8c67-a6d7-37c1-a65c-502d62da929d | -12.9921 | -45.2252 | 2025-08-22 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| ae0ea81c-3b3f-3c5e-bc67-b163140df42e | -8.7951 | -45.4238 | 2025-08-22 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| f0bff31c-b366-3aa6-97fe-f6ce9780419c | -12.3133 | -49.9881 | 2025-08-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |


[Clique aqui para ver as próximas entradas](README70.md)
