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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eeab1e7-d072-3e15-97d5-f466afd8df62 | -9.75235 | -65.09008 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5362c32-777d-3e63-9ed4-892a8d88dd2e | -8.59193 | -63.94987 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8939ead-a282-3aa8-8b13-ca9adaab330d | -8.93989 | -71.32316 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fecbea8-0cea-328c-b137-cd49c287b017 | -9.45006 | -62.36342 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6046d5ef-3184-3206-839c-08cbca6c5ce1 | -9.47257 | -60.31807 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2a17e98-dd70-31ca-853e-226678d030c5 | -13.02155 | -56.90155 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f1e011d-a0ad-3ad5-8bd9-454f73a1b6ff | -8.8415 | -66.72702 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 980047d4-923c-3bfe-96e6-b293ee28d7f2 | -13.02897 | -56.90446 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f63ff806-2817-387d-af5f-807b4fd57e1c | -7.92605 | -63.01341 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d7180fa4-1e5c-3cdf-a00c-bca3586e6a01 | -8.96107 | -65.96812 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a050c7e-65c6-3670-bdf7-e4b4ca499603 | -9.07192 | -65.45042 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff824487-5773-3230-aa5e-2f450547ba5d | -13.02288 | -56.88982 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb5b230a-c6ae-315f-82bf-a34bc6bf7937 | -9.45202 | -62.3499 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b3e5cfd-2596-3b6c-9979-76847ccbc1b4 | -10.74987 | -59.82621 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 260e3bba-86f7-3d86-bfa5-7004f8a495e2 | -9.28348 | -67.64655 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2234b994-f7a6-36b0-b83b-17d72f47f066 | -9.45109 | -60.56876 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8bb8c8d-782c-32a7-8c8e-150c065c943a | -14.31453 | -60.35152 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c52350-5a54-3d47-afdf-8cd77bdd16d8 | -9.06853 | -65.42837 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aafa139-0add-3852-8dde-51d903667c4c | -12.93399 | -56.98581 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a113d4-f477-3b77-9efb-0de5f149d8c5 | -15.21977 | -56.06019 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9aa427f6-b266-3b0c-b472-7996a6f98c2e | -9.67192 | -63.17055 | 2025-08-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff3bb9ae-bc6f-3f99-8584-fdfc31975558 | -9.44213 | -62.33921 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de34c49f-d7f9-3118-be93-59999ac2331f | -8.34555 | -62.93941 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d029679-5fd5-3b7e-8796-e004fa9b9af8 | -9.71684 | -62.39664 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c1f4b6-1ef7-375c-b8d0-2ef97c45f3d5 | -8.688 | -62.87325 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2463f826-2d46-336a-874d-3d39ab471214 | -9.43944 | -60.549 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7841fb4-b2a3-326c-ab54-8e4c5210111c | -8.67047 | -62.42846 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1268455e-f3aa-3ec4-995a-8d9e6cf908ca | -9.70479 | -61.28389 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f878a9df-26f2-35ac-8f56-e88d7b13707c | -15.21396 | -56.06395 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6654125-1dae-3498-8b75-bfc0bfb21684 | -8.73719 | -62.38473 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e09c04c1-9dfd-351a-a75b-64b24367a6ae | -9.44848 | -60.55676 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe357e0-5a64-332f-a200-1e55a311914f | -9.44587 | -60.57579 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c73d4150-4a73-344b-818c-cdd23be781c5 | -8.84533 | -64.15184 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9012fe92-dc8d-33b4-b164-84dca725219c | -11.28129 | -63.24013 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95245b6d-c406-31aa-80f1-7ad153f39ffb | -11.68999 | -63.90708 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5339f389-6cd4-31f2-af31-6db34ae9615b | -8.5338 | -64.00991 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc90c00f-b435-3be0-8c23-3a39780993da | -10.31755 | -59.20714 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88929b5-7340-3817-9ff9-bc7f3ec5c003 | -9.47689 | -60.31682 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 249bb314-3db4-382d-84af-4e0b83e1efb5 | -9.46321 | -62.35159 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ee20da96-6e40-3c0a-950e-f65d7811becc | -12.92327 | -56.98045 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e570212-79cd-37ab-81c5-bd44bfb49185 | -8.39862 | -61.36837 | 2025-08-31 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bc21d1b-5cb2-348a-ad8a-c3a2f51fcd09 | -9.44278 | -62.33467 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04275748-298a-388e-8cc7-2779b0625622 | -8.92578 | -62.42293 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c40b771-906e-3b72-8550-534278774f13 | -9.27277 | -67.64857 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 619a49db-ecbf-3a28-91e7-e43b70be272f | -9.45057 | -60.57257 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 62c5a84d-4b11-3522-9be4-e48e773a8602 | -15.22015 | -56.06369 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68606068-d2a0-3e19-ab30-0245c7efc4d1 | -9.44796 | -60.5606 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b5e92d6-83c0-36df-9217-879a33ef13b0 | -8.91905 | -62.41741 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae72f20-ff47-325d-9745-52cec8ef9dff | -11.31849 | -63.27007 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8a07246-dc6f-38a5-9d99-9e662704e0bd | -11.38807 | -63.27626 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35c5be29-0e61-3030-8a89-e05aa0b307f4 | -14.79448 | -59.72402 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f7f45f6f-8b62-3360-91e8-13d40be23ae5 | -9.0076 | -63.62768 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da095cc-fca4-3ab6-933c-b14ce4e7c6b3 | -9.27732 | -67.64184 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9740981-31b7-3ebe-b4b4-9ee9f31db16f | -9.45318 | -60.55356 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80697498-c9c7-3c88-98b6-d424a19d4e8b | -12.43521 | -63.92764 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80eedd30-769c-369a-ae89-b6396cfa28f4 | -6.91759 | -71.75121 | 2025-08-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea3933e-bcef-359c-9c99-ba3d8b8bd4d9 | -9.44717 | -62.33072 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba04a826-778a-3a09-bdce-a6b427aa400b | -9.44083 | -62.34816 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cc11245-c658-3e64-89bf-e614fcde5d7f | -8.96823 | -65.96569 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b198e313-11bf-3ba5-b632-341f8a5f595a | -8.7384 | -62.3961 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee0e929e-38b5-34b8-a259-022a2512ee5a | -9.46211 | -62.33294 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efc1ceb0-1d64-3c24-be4c-1d7399c2ee5b | -11.31448 | -63.26696 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 859f6693-c3c6-341d-9b4b-b193da6d84ba | -12.63485 | -57.00417 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560fa500-c997-354b-bc0e-f77b4016fb5b | -9.0663 | -65.42085 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52fde0a9-ebe1-3d2a-b6f8-c876a8800ee2 | -8.56643 | -63.01236 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce576590-9920-3289-98c3-c0ec4630a1fb | -7.90126 | -63.00962 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef71f38-c091-3928-96c3-ea334109e06c | -9.27057 | -67.64075 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 794e141e-924e-307d-a30a-90eb4ec35880 | -9.4384 | -62.33861 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 727d5434-49b8-310d-a69e-8d7f10e3fc11 | -8.63569 | -67.25343 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96703d5a-a2f7-37af-83bd-35b02ae876f5 | -8.56106 | -63.02407 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecd1892c-a066-3c44-bfcc-2117b9b30207 | -7.91897 | -63.01233 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7653e43e-245e-38b5-955d-f85deb872a04 | -8.54977 | -63.02653 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9cbb594-51c6-38e4-a5d3-02a802e8df66 | -13.02334 | -56.90387 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 602b61a4-94ff-3eae-93b4-6efd60324823 | -12.9237 | -56.97672 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d7eb7a0-36fb-3c86-b569-744ced7a5995 | -9.07909 | -63.97198 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 127a025f-fada-3a4f-b3bd-9c8e17db0c77 | -15.23097 | -56.07075 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b375a803-bb4a-37f5-9b36-486973b855e1 | -9.10878 | -61.1981 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73c1b534-0209-3756-ae96-f597e2ea8256 | -7.46172 | -70.14091 | 2025-08-31 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88f3163f-695e-373f-8348-38d4eeab948e | -8.42967 | -62.29036 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f8a2fcf-659e-3980-b3ed-663b99fac10d | -8.56226 | -63.0159 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5520e994-f517-3fe9-b4b9-b485b98fba0b | -10.66248 | -65.09486 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36330d1e-bb4e-3df3-8f36-091967669118 | -7.56469 | -63.41861 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d88d79-e911-3211-a610-d200312829f6 | -8.7403 | -62.38288 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c957dfd-d372-332c-ba9a-22dd8ba06757 | -10.64231 | -69.04695 | 2025-08-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eb65d2d-0b0e-313f-b9ee-5dcf40366222 | -8.90753 | -62.10363 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcbd2f33-1964-3828-9bb6-997c5ba86eda | -8.3898 | -70.76057 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5326dc-9f60-34ec-bf55-c5debeb26fa5 | -12.91769 | -56.97962 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60aebf3b-0562-32c6-b062-c8909cb97870 | -11.41788 | -63.25013 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aca4156-0791-3baa-8f75-7b6c82622e8a | -9.76402 | -67.53857 | 2025-08-31 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f572b906-1744-39f3-9695-213437d3f8fd | -9.44698 | -62.35834 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bd8859b-dddd-3b7f-ac22-0ada4ab2a632 | -9.44172 | -60.5439 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45431d35-9c58-355e-abf9-a0ebdd74157b | -9.46889 | -60.31353 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94bc73ad-fae3-3019-9b00-c80544df36b4 | -7.91837 | -63.01636 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58499aed-31bc-33f0-ba99-39aee4082cb2 | -9.44633 | -62.36284 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58ee10f3-acc3-353c-9931-8e96062c050f | -9.05804 | -65.43031 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f948b124-fe5c-33bd-8502-97528eb95d08 | -7.50071 | -63.28761 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71a1462e-861c-3a03-9e58-84c0429f3479 | -8.74324 | -62.39466 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17011c40-950b-34eb-ac98-390f6ae5a8e1 | -8.90378 | -62.10305 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc8d27df-9677-3596-a814-2613297d25cb | -9.04712 | -71.59746 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 945235da-ee17-3ec4-9b25-88db8f986cfe | -8.6453 | -62.82597 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README78.md)
