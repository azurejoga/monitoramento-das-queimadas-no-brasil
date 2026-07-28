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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba93fc0e-04b2-3b9d-ac20-b5bc37421d6e | -9.4 | -40.3722 | 2026-07-28 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 383262a5-f771-3244-b1c4-c964fc144762 | -13.3037 | -45.0812 | 2026-07-28 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 79f47728-1a02-3939-a9e5-61d844e82ffa | -10.9397 | -43.0593 | 2026-07-28 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 6928abe3-df33-3cf2-a847-9a3334d07971 | -13.2838 | -45.1077 | 2026-07-28 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 425e1e27-b964-3d00-88cc-f8a50c2a44a0 | -20.723 | -49.4242 | 2026-07-28 03:10:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1bb9fd85-fe9e-390b-8397-d04244811d07 | -13.3032 | -45.1045 | 2026-07-28 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 06c7b709-0d57-3740-a985-4dbf538bef11 | -20.7435 | -49.4197 | 2026-07-28 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a1d9b6ff-7ddb-3b73-b6bb-76a325e5399b | -10.9401 | -43.0355 | 2026-07-28 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 905d2cc0-c29c-30a2-b5a9-05f80f22aa14 | -10.9593 | -43.0326 | 2026-07-28 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 45ddbfbd-e048-3568-8f7b-709016e6704c | -10.9588 | -43.0565 | 2026-07-28 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| bd3981ba-caa8-31de-80dd-c5c5e3ff1095 | -13.3037 | -45.0812 | 2026-07-28 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0432cadc-2514-3f33-8e33-d79dd86bd0c7 | -5.90482 | -35.73598 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b1215d4-01b2-38b1-bce9-3539f37650be | -9.3946 | -40.36938 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 6d4e602f-4952-3512-b8ec-8b96a93f5d4f | -9.39604 | -40.36243 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 9492c690-5f55-35c9-b260-57f6e36b7332 | -15.81245 | -41.89744 | 2026-07-28 03:10:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4201045-2660-3c46-aa43-308c7be712fa | -9.39161 | -40.36192 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ad6d4ac0-bd74-3599-a4fd-31880ccab1cd | -17.31078 | -42.67558 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 03ff7da8-d03a-3bab-9ea4-98f29cbd087a | -17.30713 | -42.68154 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5cc9f400-85e3-3e5d-a1e0-3326f5017189 | -17.30382 | -42.67396 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2afebd03-0a86-3297-8939-00be926083a0 | -5.90619 | -35.72839 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 220e7dc1-84bc-33bb-af6d-381468748cf9 | -5.90372 | -35.72396 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e67c15fd-37ec-3bd7-978a-3eebf68a776b | -17.30882 | -42.67445 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c22a89a6-535a-30d4-b599-6d78906a2774 | -5.90055 | -35.72747 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9530097-82fd-39c4-bb19-462090eaefe2 | -9.39724 | -40.37032 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 150aaec0-f6c0-3b81-9c14-74edd5637ca5 | -5.90688 | -35.7246 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 457fe25c-138d-3887-ab6f-cc4b8f48390d | -5.90307 | -35.72774 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a66b59b6-eb23-307c-ad23-b49a61ad7ca5 | -5.90241 | -35.73154 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e9ce6bf-a3e6-37c1-88d7-857532e9d013 | -9.39864 | -40.36335 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fc39ca98-dfe3-3dbb-a579-869ade4d9574 | -9.39022 | -40.36887 | 2026-07-28 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1069a5e0-eda8-3406-812d-2fb6a728a3aa | -17.30912 | -42.68276 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| afe9a5e5-21e8-3dc2-9e3a-7a4afd5b5b1a | -5.90551 | -35.73218 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58284faa-141a-3860-95fd-369c43a53d8a | -17.31046 | -42.66754 | 2026-07-28 03:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3dec8720-9c59-3127-a840-a1f11ffbb3f6 | -5.90124 | -35.72368 | 2026-07-28 03:10:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f770a900-2d26-34c0-80db-41007c8a4bcd | -20.72419 | -40.59835 | 2026-07-28 03:13:00 | NOAA-20 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 468b6723-028a-3c92-9222-2eedd63526b3 | -10.94 | -43.05 | 2026-07-28 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26aef9c9-45f5-3c0d-90fc-29c668e24e03 | -10.9397 | -43.0593 | 2026-07-28 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.3 |
| d8b1e09d-21c9-33a8-95ff-f6ef7252c774 | -13.3032 | -45.1045 | 2026-07-28 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 5bf2be55-03ee-3377-a31b-ee1f67de7cbd | -10.9401 | -43.0355 | 2026-07-28 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 173cab05-4153-3d13-aacc-8cbd7b8e906c | -13.2838 | -45.1077 | 2026-07-28 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 982a1a32-5631-3254-8a26-7ac058f8d216 | -13.3037 | -45.0812 | 2026-07-28 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| b5564000-4300-3137-9bd0-ad062050159b | -20.723 | -49.4242 | 2026-07-28 03:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5a770a7f-3b7c-3b56-9de6-f2d6a4bde5ee | -20.7223 | -49.4471 | 2026-07-28 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 87aabeea-ad2f-3b69-ba5f-9f1644699175 | -13.2843 | -45.0844 | 2026-07-28 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 50f4a13b-2d79-3cd2-a110-3560d5270b5d | -13.3037 | -45.0812 | 2026-07-28 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| db44e1a3-f1ea-3e34-a8c1-ccbb99a009d0 | -13.3032 | -45.1045 | 2026-07-28 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| a3d08714-a946-3c72-9044-f432151bc90d | -20.723 | -49.4242 | 2026-07-28 03:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 44f90d13-e09e-364f-9dea-9a28b858b22d | -10.9401 | -43.0355 | 2026-07-28 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| d6e1129d-14f3-377c-91fb-e8c2707c8032 | -13.2838 | -45.1077 | 2026-07-28 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| c9945fd9-2f6e-32fd-b23a-c57b5a9c00e9 | -10.9397 | -43.0593 | 2026-07-28 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 300.5 |
| 552a7188-27f5-388b-ab46-23f446a20a11 | -10.9588 | -43.0565 | 2026-07-28 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fee24b19-9c54-3877-a26a-2daea04d826c | -10.9397 | -43.0593 | 2026-07-28 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 84f3c15d-ee50-3440-9092-28b121ca506f | -10.9593 | -43.0326 | 2026-07-28 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 76486098-ef23-3a46-b83f-43bfdea8a642 | -10.9588 | -43.0565 | 2026-07-28 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c1c2d4e0-e3c7-3ca3-8948-f1f0b85a36e7 | -13.2843 | -45.0844 | 2026-07-28 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 51f5de7a-3a0b-3904-8dce-add31e329892 | -13.3032 | -45.1045 | 2026-07-28 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 1166e864-1e4c-3e0c-9289-8e34a1fbc2f0 | -13.2838 | -45.1077 | 2026-07-28 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 326333a3-2e29-37ef-b077-da761c54dedf | -13.3037 | -45.0812 | 2026-07-28 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 8bd88b49-d7af-32a4-8943-ab8fd96db2ed | -10.9401 | -43.0355 | 2026-07-28 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| e9fbbcaa-2b8e-3d6e-b414-b3f0db737d3c | -20.723 | -49.4242 | 2026-07-28 03:50:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 849b94e5-86cc-398d-9d1c-22ee46f85a8d | -10.9588 | -43.0565 | 2026-07-28 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e1ba295a-9ba8-3c38-9f45-5c7e1587544f | -13.2843 | -45.0844 | 2026-07-28 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2992268a-15a8-3e97-b376-1853311811fb | -13.3032 | -45.1045 | 2026-07-28 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| c5509f87-c917-3291-ab3f-777c6a28e8a6 | -10.9401 | -43.0355 | 2026-07-28 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 37920630-7955-36a4-8f5c-225c3b1b4691 | -13.2838 | -45.1077 | 2026-07-28 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| af18eaa2-4f0e-3b98-8ab0-9a59fc7881b7 | -10.9397 | -43.0593 | 2026-07-28 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 1cb886c2-9647-30cc-a4ee-a91cb34ec9cd | -13.3037 | -45.0812 | 2026-07-28 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 16a678f0-b9d2-31ee-9352-b86c6ee15e5c | -3.24581 | -47.92377 | 2026-07-28 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5be66e51-99b6-32f2-accd-38480bf74a56 | -5.90842 | -35.72514 | 2026-07-28 03:53:00 | NOAA-21 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 967984a5-693e-30cf-a989-10b85925c1d3 | -4.3322 | -40.18999 | 2026-07-28 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b8fda3f1-2380-30b9-b2d4-1a72e2eaace3 | -4.23066 | -39.21353 | 2026-07-28 03:53:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e4bed68-d2de-3a4a-81a3-a72edb74b082 | -3.67526 | -49.48303 | 2026-07-28 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e2362775-7f88-369b-81d5-46535fb8c365 | -3.67889 | -49.48277 | 2026-07-28 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dface1f9-b378-3023-8645-6bcc31dcb68b | -4.95513 | -37.93809 | 2026-07-28 03:53:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30f9269e-9f65-3724-a4d5-5100da39a6e9 | -4.37167 | -47.7668 | 2026-07-28 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c5688a50-5927-3b6b-ad3e-a55c324cda6f | -4.36607 | -47.76595 | 2026-07-28 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56c04b81-c30b-32a4-9588-d41bb53eb5f2 | -3.14352 | -51.10349 | 2026-07-28 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd6b2cd9-7f8e-344b-aee3-66d24a18fabc | -3.24647 | -47.91989 | 2026-07-28 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c8ffe4-c396-394d-a6db-a5ddbf38a071 | -4.37102 | -47.77061 | 2026-07-28 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cff14cde-a302-3e3b-b313-302f68c078da | -2.88579 | -42.95469 | 2026-07-28 03:53:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c02a95b-8eef-386b-8842-b1d3dabede39 | -5.90493 | -35.72459 | 2026-07-28 03:53:00 | NOAA-21 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 33806148-a086-3851-8fcd-d39d8ef7eb79 | -3.6726 | -49.48175 | 2026-07-28 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 644f4088-2a97-3a17-9ad1-b7cdf278ba70 | -3.14468 | -51.09674 | 2026-07-28 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0c55b62-ccc7-3415-b640-c0c77ae47318 | -2.93508 | -40.44735 | 2026-07-28 03:53:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a4bd2f9-f786-304d-853a-64964076e9bf | -12.49451 | -43.77503 | 2026-07-28 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3d29359-b1a7-3f01-9403-dbcbe42345bd | -10.93957 | -43.05243 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| dc468342-7dcc-359a-bc4d-16f906be9316 | -9.53061 | -40.31626 | 2026-07-28 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f007fda7-405a-3401-a4ca-36bc2a8a49c9 | -7.87916 | -46.9047 | 2026-07-28 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a264fa4a-617d-3d9f-a798-5f690505e3b2 | -9.66209 | -40.59689 | 2026-07-28 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d9874b42-b7cd-38f7-9ba8-04660ab788d3 | -11.82906 | -38.2669 | 2026-07-28 03:55:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0d53fc8-c1fc-358d-84b2-1b1480c32740 | -6.48123 | -42.23036 | 2026-07-28 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1f10c87e-51ad-3a0e-8631-bb0d8b342136 | -9.60851 | -47.7675 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b6e1e8-bf98-32be-9480-67b858c20eea | -11.94097 | -43.39269 | 2026-07-28 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43320089-faf3-356d-b3bd-ff86649e7106 | -5.84396 | -44.89595 | 2026-07-28 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cfef22b-bd1e-3c37-8c53-18565d97a9a5 | -7.89804 | -48.27888 | 2026-07-28 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc0e5e88-1dd0-36cb-b017-7336673a62b9 | -7.24993 | -43.13958 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4fc9b8cc-26b5-3dd7-917a-fa633d4414bc | -9.36826 | -44.72595 | 2026-07-28 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0366e8b-6131-38e2-81f1-88f75556c673 | -6.87886 | -43.69442 | 2026-07-28 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4083629-7f88-3d87-97a0-23228b4829d3 | -7.87866 | -46.9075 | 2026-07-28 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a458187-9939-3c4d-80a4-c4414d9b01e5 | -7.24526 | -43.14146 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c138e658-f5aa-3720-9a19-87f5c064d1d9 | -10.67659 | -49.66282 | 2026-07-28 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
