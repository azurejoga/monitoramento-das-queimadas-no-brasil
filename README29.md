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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07c98db2-eafb-39c2-8811-aba5c411de96 | -8.14113 | -54.85458 | 2024-12-10 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c36b9c-3d02-334d-b0a1-335b18cea27f | -12.9135 | -55.05235 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ad77979-967f-371d-b798-a60cd6c28048 | -15.09176 | -59.62599 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f9681c8-4e8d-3f6b-acb1-eeb4a6a06c8e | -12.55724 | -58.35041 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9bbef149-b6f1-33e1-bd0a-82832b63a11d | -12.54433 | -58.35768 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1cd678ea-9654-3e3e-ada7-89ae90587cf9 | -8.13996 | -54.86189 | 2024-12-10 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8dfdc93-794f-38c0-8487-52b5bc39a0b0 | -8.8635 | -47.67376 | 2024-12-10 04:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c4d776e-947f-39a5-8649-e75db44562b4 | -12.54514 | -58.35299 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6026d8ca-3a2b-3811-b3a1-087180d5dc41 | -12.56539 | -58.37113 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e18e929b-d1e5-3a22-8caa-dc84616dea5f | -12.04289 | -62.78334 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6a883fb-31bc-3263-b0b2-5d34fda215b2 | -12.91406 | -55.04879 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bea6bc5-892a-3632-837d-25addb64b622 | -13.48398 | -60.3508 | 2024-12-10 04:55:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f010e5-e596-3fe6-b640-7be87825749e | -15.06647 | -59.65639 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92424cf3-00a9-3b1c-8d45-cd4565054fa4 | -13.20751 | -56.88279 | 2024-12-10 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f438964-ead4-32be-94c0-836a37fe3262 | -14.21459 | -56.4458 | 2024-12-10 04:55:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77a83bb9-a156-3b86-835e-fc4d022ff89f | -12.78012 | -54.90666 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec9a8d0-f35e-39dc-b91d-7ab916af0135 | -14.97508 | -44.41075 | 2024-12-10 04:55:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6d8e90b-3f30-3f1e-9729-292d9080c803 | -15.16226 | -56.47554 | 2024-12-10 04:55:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e00fa43-e903-358d-9e21-15203ef414d5 | -7.60222 | -46.63241 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d573412d-8ace-397c-a537-839d4e286c41 | -7.60099 | -46.64114 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d74d23a-18ec-3e10-a335-5095c8fc8455 | -17.44676 | -48.17547 | 2024-12-10 04:55:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f7ab79a-10c6-3e39-bfbd-3478e728fcdf | -15.25998 | -53.57015 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5482b5ef-a5b0-36e1-a593-f8c10dd94e5f | -15.37066 | -53.12954 | 2024-12-10 04:55:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7c668d9-2369-3e60-9e6c-b833347df589 | -13.31921 | -52.4169 | 2024-12-10 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18dea2f6-23b6-3e0f-95fc-0c05b4687273 | -8.14054 | -54.85823 | 2024-12-10 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d7266c5-aa27-3224-bf1b-69fe93dd5dbe | -16.37636 | -47.39944 | 2024-12-10 04:55:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8af5f41-2e44-30a0-9fab-d310ab335fa7 | -14.7966 | -47.41874 | 2024-12-10 04:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcd40e3d-9f04-3949-8579-ab54e11057c4 | -17.46595 | -47.02689 | 2024-12-10 04:55:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8866cd8-b568-350a-bfae-3514c120b07f | -12.04231 | -62.7864 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b557b0-1402-3295-8e28-dc253caf1c10 | -13.02816 | -57.21631 | 2024-12-10 04:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680ca9b2-648e-399d-81e8-9a9484707968 | -15.0704 | -59.6571 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 642ebac2-b145-3e82-800b-7e068af8e9b0 | -15.86882 | -53.26708 | 2024-12-10 04:55:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaca9575-bfe7-3984-a0a6-e807b82e99fa | -14.5284 | -45.48004 | 2024-12-10 04:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df728bb3-df9f-3bcb-8d3e-22204a2b19d8 | -12.90962 | -55.05537 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58ccc3e4-69f9-3367-b56f-0a20fec9e108 | -12.5505 | -58.34436 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03be4312-d389-33bd-8287-f2399bcdc8e9 | -7.79896 | -50.00765 | 2024-12-10 04:55:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e67c6f6-8162-3f32-a2f8-3abcb635d9c4 | -12.91792 | -55.72997 | 2024-12-10 04:55:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8c0ef21-b7df-3cbb-87e7-1d7560034bae | -15.9942 | -57.1652 | 2024-12-10 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab0e8ab-79fb-3beb-b471-c75e29f74baf | -12.53541 | -58.34167 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 848bd5e3-e866-3f78-b994-c1caf561afa1 | -12.5327 | -57.72038 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4fcdef9-8e14-3860-9676-aeda35d3bed9 | -13.31978 | -52.41309 | 2024-12-10 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8715b5d6-61bf-3347-9ea1-5927583c7c9e | -7.59212 | -46.63987 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72d5786e-4f1a-33db-a1d8-a62abf08b9c4 | -15.07131 | -59.65192 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc55d871-37f6-3bd5-ad41-af469cb6faa5 | -13.32321 | -52.41363 | 2024-12-10 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ad27838-5929-34e9-b182-77b130e800f1 | -12.54594 | -58.34831 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71497582-2ae5-39b1-be7b-9ce87e54bf08 | -14.96936 | -44.41008 | 2024-12-10 04:55:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a580df6b-4229-30af-900c-36646b23940d | -12.70525 | -54.97102 | 2024-12-10 04:55:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f85b6d-125c-3310-8a67-a40064fbfa44 | -12.53919 | -58.34232 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e4d39ed0-95ba-3106-b818-ced42d89993c | -7.66305 | -49.25772 | 2024-12-10 04:55:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4752e09b-92fb-3b68-a8b8-8090be01548f | -12.04737 | -62.78738 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc6070f-3d2e-35d0-b83e-23b804aaa79d | -12.56321 | -58.36108 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 92201f81-fb0a-3260-b78f-3671d5f76f40 | -12.71189 | -54.9721 | 2024-12-10 04:55:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bb58e2d-185d-310c-82bb-eebad8c8f516 | -15.88526 | -53.27353 | 2024-12-10 04:55:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d258b7bf-4440-3426-bf36-681e88ddd59f | -12.56102 | -58.35111 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f60112ed-2825-32bc-be67-144cdc3e4f86 | -15.25943 | -53.57384 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f8e81d8-7821-3bc4-b286-1c64f822bca5 | -12.56334 | -57.76159 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c4c89f0e-35ad-3356-b0b6-57c45dc08a49 | -15.99234 | -43.29032 | 2024-12-10 04:55:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e542455-abad-33d8-a114-796b4a4d339f | -12.86085 | -58.21655 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7b074d6-e8d8-3170-9eea-6315fc7aee2a | -15.09083 | -59.6311 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f4b7488-0852-3472-9db9-42d9ccfe2b55 | -14.53331 | -45.48403 | 2024-12-10 04:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8093a346-cf7f-38a3-8de8-11f8b809378b | -12.55028 | -58.36841 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 226e1bd1-7454-3f99-9251-6c8c8387bbdb | -12.85925 | -58.22577 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e84debc-1188-3b12-b454-82e563ee2cec | -12.53706 | -57.73901 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd64c232-d38e-3647-8a37-e2909f62a656 | -8.13832 | -54.8504 | 2024-12-10 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b299c8f1-d60d-3c73-bd4f-e6439495692d | -8.14335 | -54.86243 | 2024-12-10 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 046a1569-8853-3138-8a88-1ebae2b7acf7 | -14.14614 | -60.18698 | 2024-12-10 04:55:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee7acea-b0d4-3ab7-bd5b-ed533f5da69c | -15.09061 | -59.63417 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3422edf8-ca63-38eb-acf0-2cc207605738 | -13.21099 | -56.88337 | 2024-12-10 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3826517-b2a0-3f1c-afa8-62e9f3fed31a | -15.25607 | -53.57332 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aed2c7b-ccf0-3d90-aad4-db58ce588784 | -7.58768 | -46.63921 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66d2315d-23ad-3970-bfa1-fd47053ba570 | -15.0876 | -59.62824 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbdc9b49-9ac9-31e0-893a-68c7db7be242 | -12.5346 | -58.34639 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df99478f-d96f-3d9e-b8fb-06abb99dc148 | -12.05187 | -62.79136 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33f93be7-8a56-398b-abae-ceb1dbbb349a | -8.36554 | -49.48547 | 2024-12-10 04:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08eca6bb-4ed1-31fe-97dc-70b97f98250c | -15.08971 | -59.63935 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22078e4d-1e9b-35a1-8f0e-1ad05ea68808 | -12.564 | -58.35644 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 25b2059e-c8c4-3751-828f-cd8422aee69d | -12.56161 | -58.37046 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c9ec590b-0498-3f1c-bd15-6fbb5dd3618f | -12.71465 | -54.9762 | 2024-12-10 04:55:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 45433df4-b608-3153-b207-0d5b32755a6f | -15.08895 | -59.64143 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 220eb3ee-3dea-34b0-9a11-568e60d2bc67 | -7.59777 | -46.63183 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 401522f1-ebe0-3596-a787-13eb7d806bc7 | -12.86005 | -58.22114 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2f729e6-1d0d-333e-b405-fe51652cfa99 | -15.61595 | -59.74488 | 2024-12-10 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e56fece1-b042-366a-a407-1fac9d43756d | -12.56241 | -58.36575 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2d8ce56c-7127-3285-abbd-cc8efaf3271c | -12.53926 | -57.72601 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6e01be0-a589-3795-8d39-22a7fcc51487 | -15.17387 | -56.79118 | 2024-12-10 04:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f27b0e40-bf32-3d0d-934f-bd8b4c1f50d8 | -12.55109 | -58.36369 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c75f5334-be58-3a2c-8235-3a13fd9ecdae | -12.91018 | -55.05181 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ee49f6c-7bbb-3549-adba-3a5eab0b61c3 | -8.97682 | -47.0838 | 2024-12-10 04:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d215cbb2-a180-3b92-a664-91eeb8e8cb30 | -12.5407 | -57.73967 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9047f9c0-9379-34ca-b52e-29dd50136a97 | -12.70857 | -54.97156 | 2024-12-10 04:55:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae9133e8-4701-3814-9211-f53cc29e534f | -7.98431 | -50.68038 | 2024-12-10 04:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37dd3499-b8b8-38c0-a687-dc52b2c8537b | -14.8316 | -55.9115 | 2024-12-10 04:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bffd269c-0706-35bc-a44f-1609016c30db | -15.09151 | -59.62901 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7503d9cc-b5c1-3129-865c-1b8b1e012bc8 | -12.54136 | -58.35233 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ba944be6-ee99-3366-9fa2-aac79b5cc881 | -14.80127 | -47.41938 | 2024-12-10 04:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9cb8f5-5e4e-3f5a-9908-6604a1f799ff | -8.71417 | -44.00866 | 2024-12-10 04:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86d71434-b4a4-3d9d-a01a-826360b21d95 | -15.07976 | -59.62683 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d3dd63a-836f-3af7-b510-22feeb4c5f8e | -12.85712 | -58.21587 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 588950af-153f-3d3a-bd9f-137c6e54f22c | -12.90629 | -55.05482 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62eab220-f39a-3e39-829e-bafbc7a03012 | -15.44505 | -57.81429 | 2024-12-10 04:55:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README30.md)
