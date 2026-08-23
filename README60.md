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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a10ef42-b01e-3524-9fdf-55bb52c817bf | -4.536 | -55.51119 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8da9afe-61d1-3685-aadc-ff2ec066248c | -4.5368 | -55.51664 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3e91909-77eb-3da2-b153-3bd2c9be2751 | -6.23116 | -55.62126 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 995fdfe2-9c85-312b-9f85-720102d71bef | -1.61426 | -54.40141 | 2026-08-23 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f9168f1-4598-39a7-a0ff-f25edae73a46 | -6.2006 | -53.52637 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a62508d-b842-32c3-be40-3584271b0306 | -5.7833 | -57.57644 | 2026-08-23 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53381632-7f1e-310f-8953-45fd9c95a8d5 | -4.53743 | -55.51199 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc572648-0eb1-3a2e-b904-af8622b184a1 | -6.24413 | -55.3895 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32f4e5f4-ef45-397f-a52d-4e568264fb34 | -6.37651 | -54.95832 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37f05bec-fb05-35e5-b968-b50e636c012e | -5.49085 | -60.17209 | 2026-08-23 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 517901bd-1f4f-38b9-a5e6-e647d64d76e2 | -6.19362 | -53.52539 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a183cd9c-35df-346e-8122-31f72326da6b | -6.17511 | -55.57154 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91018b92-730c-3971-98df-504f04da4344 | -6.38081 | -54.97508 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d17bdf5-9cb6-36c6-be7e-2769ae67bf96 | -6.24333 | -55.38144 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38881e3c-0d14-3421-b3b8-4ab22806fd28 | -4.966 | -56.27333 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14db1d99-6276-37d6-9ccf-72271452408b | -1.6119 | -54.40395 | 2026-08-23 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa2197f7-c0b6-34de-ae17-7ec1944fc68e | -6.18751 | -53.51791 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 412d0dea-cd65-3544-a577-77c43c2f4077 | -6.2427 | -55.3863 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78a81927-a314-31b2-aa5e-6c634a507b66 | -6.3758 | -54.96366 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42448b96-d3d7-3db2-8663-f4099145ba30 | -6.38152 | -54.96983 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f97982a-fe32-3288-b2ce-d4f7f68f3cb3 | -6.225 | -55.62044 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c99f3ee-7ccc-3c27-863c-8c5e986dc78f | -6.19971 | -53.5329 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b55a29b-94a1-3da5-b60e-2799e1d18900 | -6.19212 | -53.52645 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b85b9df7-4a7d-3c80-a920-540ac3f7a746 | -6.19273 | -53.53191 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7ce9a1d-ac33-36d9-a21e-434b7efff01a | -5.48843 | -60.1736 | 2026-08-23 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fb10eab-3836-3cc9-9174-64bb6d35c87e | -6.22563 | -55.61586 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c4f43bae-6e15-38e1-830f-49e9283f459c | -6.2015 | -53.51971 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0bd56fe-5d2b-39f2-aecf-13056f6ae7ba | -5.00293 | -56.1341 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f70d49-486d-3e73-993d-1ea01dc7d806 | -6.23131 | -55.61883 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bd1b73b-4152-3482-84b1-69cb18b6e88f | -5.96091 | -53.62908 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 371e638c-4f74-3f95-9227-d9ebd998f6b9 | -6.1945 | -53.51883 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b423e53-8156-33f7-90f5-f29fb6491641 | -6.22514 | -55.61805 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4f208ad0-dc3e-3c8e-8060-05d9133f63e2 | -6.23716 | -55.37988 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de805347-8f28-38a2-8449-fda799028b33 | -6.1991 | -53.52745 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc59ebe2-103e-3d42-a515-54452957f404 | -6.18663 | -53.52448 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7e2274e-da4d-32a9-b2d6-95cfc3e60c67 | -1.42041 | -55.72526 | 2026-08-23 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0b3607f-13b2-3b1f-87ee-ce33fa8170d0 | -4.93657 | -55.77737 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2fce0a1-4c55-3ad3-8a66-7585230bc736 | -4.96546 | -56.27726 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a663e3d5-f64f-31eb-8308-56000f32a6e5 | -6.23862 | -55.38315 | 2026-08-23 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d5694e0-eab3-3a02-ab94-6678368f20ca | -4.53615 | -55.5214 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee278f59-4423-34f0-a6c3-5bc59bf21c55 | -6.19996 | -53.52082 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c92045e-8f34-325d-8ee6-06fbcaf36427 | -4.53465 | -55.52057 | 2026-08-23 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 262ea380-5fbf-3ef3-bbe8-a5fbe91deba9 | -5.96175 | -53.62258 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe241f02-9d0f-3993-a3ac-47daf2202dda | -5.00232 | -56.13858 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbc2558e-901f-3d62-b90f-7a1883595d8f | -6.38294 | -54.95921 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29a990f2-f710-3f10-a2e3-0eaa3bd5c051 | -6.18683 | -53.51224 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 25cdbf32-ff88-369c-a0ab-6787881bc709 | -5.77835 | -57.57246 | 2026-08-23 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25d8e19a-720c-3d5c-9ab9-ba175702af6b | -5.78377 | -57.57305 | 2026-08-23 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d509322f-2fb4-377d-b18e-c83a3699054a | -6.18597 | -53.51896 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94997c52-2e52-3cfd-93db-ab18baa438b7 | -4.93293 | -55.77975 | 2026-08-23 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b344f4-ae48-3c2f-b305-d22c153456b9 | -6.18513 | -53.52547 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18e86452-6da9-36e0-a5cd-5864bfaad3ae | -1.61262 | -54.39909 | 2026-08-23 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e46e97a5-8b05-3592-9a6c-a2ede92c0f8b | -5.47828 | -60.25655 | 2026-08-23 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f159ef5-f4bf-321b-8da1-0abe5f1c23a7 | -1.42214 | -55.72527 | 2026-08-23 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32903275-04ab-31d6-8cdf-4e8f90adf44b | -6.18842 | -53.51121 | 2026-08-23 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5142fff-c8dd-3649-b1af-82216d6b721d | -6.9699 | -59.0658 | 2026-08-23 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4f8bbd41-ddd9-3a64-aafd-c50e2f9f4047 | -6.9514 | -59.0666 | 2026-08-23 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ed3469c3-68b0-3639-9f6e-16ddf782c4fd | -6.6765 | -58.7492 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 842eacf1-399f-36de-ad0a-a1037f33c9e4 | -16.0509 | -50.4363 | 2026-08-23 05:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b7c48797-75dd-3807-8dd5-78b434f4534d | -6.8061 | -58.6663 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 926b0d44-9c61-3fe1-8f39-3434857d89b8 | -6.9513 | -59.0859 | 2026-08-23 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3c8a5ecb-827f-32a9-b88f-dcc657c3e7d7 | -6.695 | -58.7291 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 383f50dc-865c-3ed5-9991-aaffb9380cac | -6.6949 | -58.7485 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| bf8091a8-2e4c-3219-8886-7ee19749b127 | -6.658 | -58.75 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| aaae22ca-bdbd-39f2-b8d0-d23471ec84fb | -6.8062 | -58.6469 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 08f94b30-077a-3d2d-b30c-fece8d1227c8 | -6.6766 | -58.7299 | 2026-08-23 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fb7a82cb-be6b-3517-87f3-493ac0d945dc | -6.8188 | -59.6696 | 2026-08-23 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 378bcb73-f7ce-3ede-ac2f-c387e886bb1c | -8.52528 | -54.81803 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a91b860c-0650-3d2e-b22d-5854ae8d7b1b | -8.93335 | -60.72124 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39aec208-52ea-36bf-957a-dcc06b24d8b8 | -6.76807 | -59.44659 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f201d8b2-70bd-3396-89be-01c25afe0bfc | -7.61688 | -60.98023 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730825ce-fbf6-3c27-b26e-5e9a5e3cf380 | -7.62817 | -61.6221 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 109542ed-5089-34af-9a6d-efa60dc56f20 | -7.78053 | -61.42944 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18c45323-cb76-397d-8c7e-f1d0f3e4bc26 | -6.90392 | -59.00292 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d529f2a-933c-38ae-b01c-869303196781 | -6.80203 | -58.66551 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c70bb075-9a94-3c54-95f1-c376cb0e3d4e | -6.88557 | -59.41518 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f854e7ab-d5a4-3115-a6ae-e54593a53cda | -9.11718 | -60.34234 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 174c566d-59cb-369b-ab93-2a78eb01417a | -6.80801 | -59.44178 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a88acc5-50c1-343a-9174-59a95b89e342 | -6.94938 | -59.08473 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a216a05-690f-3db6-a38d-ed452e517689 | -9.10895 | -61.59301 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9676bde2-ef41-3cd5-8cff-9890ea2a9068 | -9.06564 | -60.44036 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a2f694f-d5b0-3cc1-9995-6fd299225b5c | -6.86623 | -59.41254 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f06f1c7-8076-3feb-b3f3-57722848d535 | -9.08296 | -65.40834 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e47789e8-d14a-3389-bf3f-e058747f11e4 | -6.55644 | -55.10268 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0948b97a-a658-378c-a2b5-11e6873078ab | -6.78612 | -59.42222 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d69192b-4499-3305-a0cd-414c23785909 | -6.68445 | -58.74169 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 29f3e141-827e-3edc-83e6-c4c94634486c | -6.66971 | -58.73657 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 56e3a66a-10ab-3978-96b6-a0224d95bb4f | -9.11381 | -61.58961 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6e246b-6b0d-3d01-9151-acb284538e6a | -6.78771 | -59.41512 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d540373-e3c3-38f7-aadd-9592e465981e | -6.93979 | -59.07142 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 301a1b58-1be0-3eb6-a079-5b5b8d68a148 | -8.95613 | -60.59055 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 804e358e-e302-3fe8-8dc2-b82f6c6d4167 | -6.77057 | -58.67921 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6bcd468-b0ff-3c83-98b7-947f850662ce | -7.68288 | -63.3359 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| be15794a-1a82-37a4-b86e-9aac850b8c6c | -7.01508 | -59.57021 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9991ae1-9c3f-3e51-8629-731eab21b743 | -6.80825 | -59.68411 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b75777f-680c-3793-bc91-e2f6d587f719 | -6.66811 | -58.7484 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae900265-a273-3e8d-bdfa-f11b2bf9e370 | -9.14803 | -65.95433 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7cd990a-0ac4-3051-bbdf-63d43eebc75b | -8.92944 | -60.71599 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 880bf452-d404-3d68-8a3e-94c82b5a969c | -9.45862 | -56.90802 | 2026-08-23 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2d59370-7a85-3947-b4e7-771a3ff2abee | -9.86073 | -60.12383 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README61.md)
