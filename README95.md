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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b351f422-2e10-3c6f-b420-fcc9108bcf28 | -9.4339 | -45.6931 | 2026-09-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6c75af1c-0f0b-3ac6-b84c-e1837da25ca3 | -8.7819 | -46.4399 | 2026-09-01 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 6f3626a3-4e43-3adc-91e9-c7ac7deb427c | -7.571 | -60.4643 | 2026-09-01 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 38d49e25-ac7b-3882-af12-4f734cfaba96 | -11.2634 | -45.3471 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 45010a09-6f54-3651-bb62-9b86a774ef1b | -11.2295 | -51.2667 | 2026-09-01 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 121c364f-e4c1-383a-91c0-ad74339c54f0 | -17.1146 | -46.8556 | 2026-09-01 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 095c5a2e-df35-3970-9a2f-57ef9ca8aeed | -10.8404 | -50.6499 | 2026-09-01 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f011791b-fa06-3e6d-9597-f8e1a6b22612 | -3.879 | -44.0576 | 2026-09-01 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 176.3 |
| edf27e36-0ae5-35af-9547-a3f46db9bf30 | -11.0928 | -51.5767 | 2026-09-01 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b904b8a3-56fa-35b5-81e6-993fdb0cb0fd | -10.1542 | -45.6755 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ae15273e-e972-32b2-a54b-a2c491d11a8e | -14.7305 | -53.5756 | 2026-09-01 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b2aab50a-5a6a-3278-b1c3-f60c40d34658 | -14.4587 | -52.5151 | 2026-09-01 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2d2dcbd9-713f-373e-878c-265a7a069c93 | -10.7856 | -50.5066 | 2026-09-01 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 97a5c824-acb8-3422-84d0-017259691655 | -11.2292 | -51.2879 | 2026-09-01 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 91dad887-0662-3154-ad4c-c83a53939c23 | -14.6732 | -53.5408 | 2026-09-01 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 49762b11-2916-3739-9c9f-247af030e443 | -6.6036 | -58.5972 | 2026-09-01 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 518f6bb1-b614-39af-b1fe-94a209124ac4 | -11.5479 | -45.4676 | 2026-09-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 9a71d416-04c7-3031-9c01-cb10df0544a3 | -8.279 | -54.9174 | 2026-09-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| f4ceb743-29b3-3e54-9a47-fd47462cf332 | -7.3488 | -60.5691 | 2026-09-01 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 38f27203-eb8b-30d6-85bf-9c436259999d | -10.8407 | -50.6286 | 2026-09-01 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9de09501-583d-350e-a7fd-8dbd0d900a2d | -11.2317 | -46.1041 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 875ecab2-b7bd-397a-b7bf-1159974374fb | -8.2788 | -54.9376 | 2026-09-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 4d21a63d-7f90-3a4e-8df4-f168c2fd847d | -11.2485 | -51.2647 | 2026-09-01 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 13ed21a7-9374-379a-8a5d-00f450c44935 | -11.2673 | -45.1167 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ad4638c3-2535-38e7-b792-8e1c319f5a88 | -10.8624 | -45.3789 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 472f55f8-d9df-3050-87b1-6932bb13a0e9 | -10.036 | -44.7056 | 2026-09-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cb0c1071-37ae-321b-bfda-1ba854fd7849 | -10.8627 | -45.356 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| de011469-4512-3d72-b8cf-724e73aca008 | -8.7817 | -46.4623 | 2026-09-01 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 79a60a3b-bf00-3268-89cf-af73e86a8e19 | -14.4014 | -52.4802 | 2026-09-01 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4e5c40d8-adfc-3245-a927-fc4704f6045f | -14.4397 | -52.4964 | 2026-09-01 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 0ed1d814-17c6-3f31-9628-d35f82a6ca63 | -14.4208 | -52.4777 | 2026-09-01 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 49f388ff-1562-3daf-b49a-706d1c63ec57 | -7.8716 | -47.0838 | 2026-09-01 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5bca4653-a010-3f76-a1e3-e394db57abc9 | -6.1659 | -57.7403 | 2026-09-01 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d841b13b-c5aa-30e2-a68a-e6048f6340ce | -14.6538 | -53.5433 | 2026-09-01 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d7408344-6a00-325d-9c3b-b90eace51f70 | -3.1083 | -61.238 | 2026-09-01 13:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fc2473d3-4234-38ab-917d-c913b1c2d1b0 | -12.9032 | -45.8382 | 2026-09-01 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 348d1cc0-3653-32c8-b144-1971d3c0e977 | -3.8605 | -44.0355 | 2026-09-01 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cdcf35be-dfe4-3a2e-9024-267bb1922b13 | -6.9552 | -55.635 | 2026-09-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 70265e76-9b65-3499-ad2b-295ecafbb429 | -11.8056 | -46.0476 | 2026-09-01 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 327.8 |
| cac1d962-8774-3e9d-8d99-6967617692bb | -7.5709 | -60.4835 | 2026-09-01 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 71d6ee6a-a467-3dc8-ab0d-faa565ab5ee5 | -8.2602 | -54.9388 | 2026-09-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2d08898b-6671-30fe-bfde-da2c372dd677 | -10.8818 | -45.3534 | 2026-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 9831047b-dc3f-3fa0-bcbb-6293ae7d1302 | -15.4429 | -52.681 | 2026-09-01 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 02d3d053-2717-32c3-b68c-556dfb711249 | -3.8603 | -44.0815 | 2026-09-01 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| db5eb42b-0a9c-36da-82af-17d59ae1e91c | -3.8789 | -44.0805 | 2026-09-01 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e34cdb36-8ae7-3593-a561-72573a1f9956 | -6.9553 | -55.6151 | 2026-09-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1931e4cb-3425-37a4-812d-d114a6325a54 | -7.3119 | -60.5706 | 2026-09-01 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 3ac640a2-8602-34bc-bdcf-f0c8bbec486c | -11.2298 | -51.2456 | 2026-09-01 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f6b15b9a-5244-3765-9083-66b26c478e50 | -14.4647 | -53.3151 | 2026-09-01 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ebc5f13d-dc6c-3354-855f-04d932b03eaf | -7.3488 | -60.5691 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7bb7aebd-7770-3d32-a83d-a6cd63f9e48f | -3.8605 | -44.0355 | 2026-09-01 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8caa6714-62cd-320f-84cf-89864abc5281 | -11.2106 | -51.2688 | 2026-09-01 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 9946f4a5-54a8-3cb8-9ad1-e4f04f515f2a | -7.8628 | -61.1405 | 2026-09-01 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 578a367a-f0e5-39c3-88d8-7faa83abe746 | -10.6964 | -46.242 | 2026-09-01 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 09f22dc6-fcaa-372b-971f-8c40d92ad856 | -11.6914 | -47.1461 | 2026-09-01 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4dd5dd97-b3d6-37f4-942d-75d5b6fd2199 | -6.8193 | -59.5734 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 6a380ee3-887b-3dd8-a771-e0a8cbadd6a0 | -6.6036 | -58.5972 | 2026-09-01 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3a984e28-9ae9-3b3f-a1c8-1cff33b064d5 | -10.036 | -44.7056 | 2026-09-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e6a32fb5-3c7b-3942-986b-b6cd2d254600 | -7.5709 | -60.4835 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 13551dba-317b-35f8-bea0-da9e865bfd28 | -14.6535 | -53.5642 | 2026-09-01 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 728768ad-a692-30de-8023-2077c5dec0e6 | -6.8009 | -59.5742 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8ca32659-588c-322f-86e4-f80511eb01e6 | -8.279 | -54.9174 | 2026-09-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 80d479e0-31f9-3b76-979b-3242f5633de9 | -9.9931 | -46.3057 | 2026-09-01 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 80145c37-e408-3f84-a38d-4652ae11130d | -3.879 | -44.0576 | 2026-09-01 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 1156ce18-f6b1-342d-bd4c-4c1aadca43c3 | -3.8604 | -44.0585 | 2026-09-01 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 3caaece2-6cee-3790-b71b-835ec8f2b66f | -11.2485 | -51.2647 | 2026-09-01 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| abf78cef-8ce3-3735-8220-da83fc87b5f5 | -10.8818 | -45.3534 | 2026-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f2d3a743-0867-36f9-9c2d-1b5752b55481 | -15.4429 | -52.681 | 2026-09-01 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 9c0b75fa-9d50-3f86-9de2-e46fb148872d | -11.2634 | -45.3471 | 2026-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| ef09c785-f48c-3522-8465-81bb85108823 | -9.9912 | -46.4409 | 2026-09-01 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| c51fcd72-c4d5-39da-815c-c7db563438fb | -7.3487 | -60.5883 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| afc6f072-2c80-325f-bde7-6d661709a07f | -13.9477 | -54.3971 | 2026-09-01 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0fb32ff9-7939-35df-a775-fe94284efbdf | -8.4235 | -44.9849 | 2026-09-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c93f64fa-ba97-3b4c-9a41-809e290ef1cc | -14.5021 | -52.2339 | 2026-09-01 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b27f953a-356e-37cd-b103-ddde35e07ed2 | -14.7112 | -53.578 | 2026-09-01 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f3635c13-b929-3512-aafc-0448a7757ec5 | -7.3119 | -60.5706 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2f679d86-14de-318c-b3c5-0b4745b9e9f9 | -14.5452 | -51.9729 | 2026-09-01 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 52a2445c-341d-37af-8819-d2f5088fabce | -6.9553 | -55.6151 | 2026-09-01 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 339d680a-33c8-3e93-87ec-3206444d527b | -12.9032 | -45.8382 | 2026-09-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| b95c118f-f0d6-3273-b1c4-8f56bc7a31e1 | -11.5479 | -45.4676 | 2026-09-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| dec50b1a-0573-3385-88a4-7f58f1226876 | -6.8036 | -59.0921 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3dff31be-777c-34b1-a430-eb07b9f6948d | -14.5448 | -51.9943 | 2026-09-01 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 53c4008c-e138-3780-97ca-296799e0871a | -3.1265 | -61.2377 | 2026-09-01 13:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3555fdba-540b-32ac-8a23-a08c522560b4 | -11.2292 | -51.2879 | 2026-09-01 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 75a2c466-8bed-3094-a9b9-59292b32b94a | -14.6538 | -53.5433 | 2026-09-01 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c1d667a6-0ef8-37ae-be78-e24d6d8f02b7 | -7.1167 | -45.7898 | 2026-09-01 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8fa4d0d5-a88d-3966-af5f-09521831cc2b | -8.7817 | -46.4623 | 2026-09-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c69079f9-eb9c-34ed-a998-2c993ebe2719 | -7.9048 | -44.2577 | 2026-09-01 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2c169425-a073-3670-8f30-174b9580b2fe | -11.8056 | -46.0476 | 2026-09-01 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| d213a2f5-c4cf-3fbf-bb3c-d505e60093c6 | -6.1659 | -57.7403 | 2026-09-01 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e458e6da-39c8-30c2-a57d-c6c8badf9ac3 | -11.2295 | -51.2667 | 2026-09-01 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 224.5 |
| cbbfbbe9-3952-34a3-b3d7-c4e1aa5df55d | -9.4606 | -67.4531 | 2026-09-01 13:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ca01b034-5cf4-3226-b41a-b97a3e9c1b2b | -3.5161 | -59.0597 | 2026-09-01 13:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4310e562-f4bc-3c4f-9d15-4fc893c4b953 | -17.1146 | -46.8556 | 2026-09-01 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 08942fac-78d9-3f50-a0c4-e0e40b8281df | -7.8716 | -47.0838 | 2026-09-01 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b3dd2d73-f6b8-33f6-a18e-98a0ee4b4b8b | -10.8046 | -50.5046 | 2026-09-01 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| db0a71a9-ef2c-3792-b6c0-b93f5f7847cf | -8.4232 | -45.0077 | 2026-09-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e4baf551-51b3-3ffc-b84b-77a47bd99003 | -14.7305 | -53.5756 | 2026-09-01 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 1397291f-8519-3e0a-92b5-222f17d909ce | -8.4046 | -44.9869 | 2026-09-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2ca6e320-1f00-325f-b3d9-32c15d74bf34 | -10.0101 | -46.4386 | 2026-09-01 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |


[Clique aqui para ver as próximas entradas](README96.md)
