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
| 3494632a-1ba4-3c6b-8d8e-f2855a85ae82 | -12.87375 | -62.09983 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 81a53b59-2f7d-34ef-a1b3-01afc8f5a46b | -15.78489 | -56.42019 | 2025-09-09 01:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 56b97d40-18e5-32b7-9c2c-a82bde12e07c | -14.90373 | -55.83789 | 2025-09-09 01:28:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f91b2eb2-535c-3d67-ae63-4552accb8809 | -14.70811 | -60.25935 | 2025-09-09 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 29b1c14c-fdb9-365c-a597-4bd7c351e717 | -12.90013 | -62.08084 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 624ec8ef-564f-3d1c-b89a-8e9a57f716ea | -15.77391 | -56.42228 | 2025-09-09 01:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4f98d47f-c269-3348-93f8-e4cc330ec2ca | -12.88258 | -62.09854 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a2c0f201-5a1d-3fa4-a2f4-f874c194ad01 | -11.15632 | -57.18757 | 2025-09-09 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 12cbf3bb-4739-3e88-b5bc-ef533e4078a3 | -12.87499 | -62.10885 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5f0fba88-7004-3b44-88a6-fb05798a90f1 | -12.1955 | -53.87724 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5fc23a9f-9c98-30ab-a774-6cd34724523c | -14.35568 | -60.30975 | 2025-09-09 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7dc948e3-9b22-3172-b37b-6c47474a195e | -11.16761 | -57.18567 | 2025-09-09 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 07d785d2-9b8f-3dfa-a657-733da2070568 | -12.61165 | -56.98567 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5d2fa9f1-ff41-3446-9b24-9779b3ead0c6 | -11.819 | -63.00154 | 2025-09-09 01:28:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 31c182fe-2350-3479-a63b-4db330f9e6f6 | -14.37366 | -60.30728 | 2025-09-09 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdee7712-16cf-3f17-a631-2372dc0524b5 | -12.8339 | -52.94506 | 2025-09-09 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 8be3386b-c833-3020-b3b5-f46cab7bb24d | -14.72468 | -60.24714 | 2025-09-09 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4203a1c8-0d3d-3753-a1c5-7266041d19ad | -12.62284 | -56.98389 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e97ebfe5-9114-346d-a383-4f929912ec63 | -15.77629 | -56.43695 | 2025-09-09 01:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a15b0b7c-e07e-3bd7-ac84-3518b66e588f | -15.82645 | -52.27892 | 2025-09-09 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| d01c0bab-1f6c-3276-a6ce-725ed9bc3e40 | -12.64516 | -56.97998 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| c99d215a-cc11-3655-9120-2a00d11f7648 | -13.12656 | -54.91811 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 86d8bda3-334d-3d58-bd5d-61a48a4b3a2b | -12.84572 | -52.93596 | 2025-09-09 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| feacdde9-f55d-3452-a707-5ea516a39cc8 | -12.60924 | -56.97062 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 75a43431-36c5-3610-a817-bd06cbadfa82 | -15.26604 | -53.79399 | 2025-09-09 01:28:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a303208f-07ef-35ff-8692-8b0a56b1d8f4 | -12.20194 | -53.89793 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 8a94a7d6-5a31-3c2e-a77c-a1ad2dc4e3fd | -15.18833 | -56.01063 | 2025-09-09 01:28:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 07daa70f-e8d0-3646-8a94-8bc9a244fc3b | -12.62044 | -56.96883 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 7a3d4306-e96d-3e2e-8b69-d5e7f4563f8e | -15.17426 | -55.99678 | 2025-09-09 01:28:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 52c94187-6965-35ce-88b3-81efeb72f737 | -16.32878 | -52.94137 | 2025-09-09 01:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 8d28ef07-7e7b-37bf-85de-8824c08d6aca | -12.87623 | -62.11787 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fbd9d7fa-de78-3dc3-b4e8-d0d0613747f4 | -12.19988 | -53.90374 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 60cad461-82a9-34cf-96b9-eca5e175bd46 | -12.93403 | -54.78812 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| b5e79884-48be-3ecd-90f7-4a8ed8b270a7 | -12.63161 | -56.96687 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| bd001642-da18-3752-8a35-82b40fd606ac | -15.87035 | -52.3545 | 2025-09-09 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| c43e6767-adac-302b-8808-f853e8af69a3 | -15.86756 | -54.93562 | 2025-09-09 01:28:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| da2af176-7da7-351f-9009-8a572949e04e | -16.32419 | -52.9155 | 2025-09-09 01:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7d47b7fb-ceea-30e8-a8e2-66f9a86e9574 | -12.90137 | -62.08986 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e306956f-760c-387e-a8b4-2602d85fe7dc | -12.95262 | -54.75544 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| b5dcccae-f7eb-3e0c-9fcc-b5fc450ea01a | -11.15775 | -57.19368 | 2025-09-09 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f9684b31-3b1b-393d-b075-5ca8c2d001b4 | -18.8375 | -49.6777 | 2025-09-09 01:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.6 |
| 490de883-d87e-347d-a556-eef79b0d7b9d | -18.4808 | -49.5447 | 2025-09-09 01:30:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 411a3cbc-4cf7-3332-beb1-fbd012c4538d | -12.1991 | -53.8817 | 2025-09-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d8815830-052a-3168-931d-1b573f913375 | -18.8174 | -49.6816 | 2025-09-09 01:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a39c90e3-a5f4-3026-b29d-3ce8b562b77c | -17.2757 | -46.7538 | 2025-09-09 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 49c66918-80be-33eb-9aad-2bf8b1e65bed | -15.8275 | -48.9505 | 2025-09-09 01:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 7091f6e5-47fa-3398-9d2f-6cad952c61dd | -11.4277 | -43.6017 | 2025-09-09 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b3eed21b-f704-35dd-9573-7a40a7bf7640 | -5.5703 | -45.0518 | 2025-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 665014af-b863-363b-9ef3-8dfe5b7a3387 | -12.9673 | -54.7499 | 2025-09-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 4e6ea908-2dc4-3734-bfb9-769e6728df5e | -20.339 | -48.5688 | 2025-09-09 01:30:00 | GOES-19 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8d66eb6a-90e2-3f1a-aa23-bdbe72d772dc | -5.5892 | -45.0278 | 2025-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5e9a12fc-ebbf-3a4c-8657-af1ddd24f770 | -9.0802 | -65.3789 | 2025-09-09 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9a28ce00-7b30-36fe-b171-ed8257bc53d6 | -5.589 | -45.0505 | 2025-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| ba6ae35a-c718-3469-80b6-f1ed25645582 | -10.011 | -64.9339 | 2025-09-09 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dc73d4fe-7bf9-34b4-b356-38c45b7f718c | -5.5705 | -45.0291 | 2025-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 4ae621f2-9b33-375b-95a6-6d034f231ce6 | -10.0111 | -64.9151 | 2025-09-09 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 174835e2-68b5-3048-9ce8-6ec27399e87a | -12.9482 | -54.7519 | 2025-09-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 47121c74-38c9-3c34-ba1a-7baf5608771c | -12.0295 | -51.0935 | 2025-09-09 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d85301f2-65ef-3bd0-9fa7-1193ed555f70 | -12.1988 | -53.9024 | 2025-09-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e8e23343-4fd5-351b-b013-539e3459d508 | -9.06261 | -60.44968 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd8ece2a-4ac4-398a-8c61-d7431ce12991 | -9.95078 | -60.15089 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5b2b8134-c97b-35c7-84ad-d0462a05eeac | -9.69488 | -64.18875 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2426a6c3-8b5c-3ee6-babe-18ae06e55f9c | -9.08473 | -65.39359 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5da808b0-9173-330a-a259-7717b39a6541 | -9.9345 | -65.23988 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| df125f0d-4f41-3ddf-8c9d-d073faeeb798 | -10.77597 | -59.85504 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 8edb2fbd-32f1-3c30-9ddb-029b89caa581 | -8.01761 | -63.49137 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bcf49245-8026-316c-bff2-487a9d52532d | -9.08329 | -65.38277 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a8118ee2-6ebc-37a0-9ae9-cc56c6b1c4b5 | -9.44216 | -60.52085 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2ee9b843-abca-303f-a945-3d874aeb6bd8 | -9.08764 | -65.41527 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 52374a64-874e-3e17-9570-7e5332c9dc70 | -9.69616 | -64.19839 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ae21997f-f9a0-3a8f-86fc-ba32e96b85d3 | -9.94777 | -60.13052 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8bd1f8c0-4c9b-33b4-9213-f9c72527608e | -9.11121 | -60.96809 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| be7f8e61-1017-3ba3-9187-c824596872e7 | -9.21867 | -60.82224 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| a255074e-dcd0-312f-8168-38ee805f1cac | -8.98015 | -65.44739 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f6034d23-a720-3b09-82d7-19b029b319b2 | -9.47636 | -60.49545 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9b024629-c64c-3f61-8cb9-e7049d68f824 | -9.67631 | -65.52994 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 613b191e-3c11-3a57-ad08-534de05d0b7f | -9.28965 | -60.8608 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab36e940-db18-3c10-97d5-8f402e4cdd52 | -9.20067 | -59.38385 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 140b13c5-d2f4-3b28-b958-c8c25b397bc2 | -8.08975 | -54.76165 | 2025-09-09 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ae4ba728-3e4d-3a17-8259-8671e570245b | -9.21044 | -67.57297 | 2025-09-09 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 82286f60-2647-3ab8-9b2e-189a04a16297 | -9.00245 | -69.39876 | 2025-09-09 01:30:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ff90d1f0-3997-3699-a661-139d46550109 | -9.16931 | -59.38276 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 966d1c62-c148-3fcb-bc82-ac0ee3f8b7ef | -9.29879 | -60.85945 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1ada1b5f-eb88-3b67-a653-fbb21fc9055f | -10.41443 | -60.79813 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb02c01e-0d68-311f-88f3-8b48a2ecb49d | -9.16038 | -60.79731 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03c60a66-a9cd-3e46-96df-c7ce6d1c41b6 | -7.82593 | -63.58258 | 2025-09-09 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a932d168-3470-3c76-8840-257a301e8670 | -10.17765 | -61.13939 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a48c9db-f093-311a-a84b-86912520f9ed | -9.98372 | -64.98727 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0090df63-2c79-3b83-a3bf-22d557084cab | -9.16957 | -60.79598 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a3feb85a-10c5-3fa8-8f9a-06694474da08 | -9.22782 | -60.82083 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9f0fb326-ff7f-3cec-a03e-e6a8f2e92f5c | -9.05727 | -60.45695 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 35a0b5a7-efe7-3f17-bab9-2e50aa202380 | -9.08185 | -65.37199 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 521c2331-7c63-34c4-b934-d9b08e54474a | -10.58241 | -61.26206 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2a32afa5-d737-3af9-8321-812beb6ffe0b | -9.43469 | -60.51825 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bd680539-5010-3e23-b456-85321d23c286 | -9.46852 | -60.50677 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0b029e36-a276-3029-9c0e-27bfb4ec226b | -10.41352 | -59.60576 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 03f30905-31a0-3ebd-9d0b-4647170ffa60 | -9.67775 | -65.54121 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c5fcf9f9-f6a4-3f27-96ba-06a1798cdacd | -8.54314 | -64.04272 | 2025-09-09 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f6c47016-c337-36ff-afaf-2e342708af95 | -8.72139 | -62.38544 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1e97759-28d8-3b71-bd4d-2b5eaf84dadc | -9.94928 | -60.14073 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README5.md)
