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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47415345-296b-3cd4-97da-6a63d010b68d | 0.89615 | -59.54715 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 563f4360-a1dc-3ecb-9870-a5ba7f509dec | 0.76446 | -60.09019 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f2fa99-15b5-341e-8647-3ad1aacba222 | 1.13073 | -59.43935 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35b8d9d5-5550-3c19-9d8d-3986884ca208 | 2.19484 | -61.81672 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36d63f61-2944-39e6-91d6-9201235a8242 | 0.66756 | -59.99222 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7e45973-80e4-363c-b4fd-2c52ee52a613 | 2.29293 | -60.21691 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a160ef-8d3e-3bb6-9a5f-d54ab3c37895 | 0.84461 | -59.5408 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a6a7d59-8b1c-3e61-8b42-e6bfa04cdf25 | 3.6027 | -60.09913 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69a86c41-ecfb-38c6-bfcf-e4dc3c95c760 | 1.10358 | -59.91358 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74f98943-fdb8-310f-adc3-da3c93f97622 | 1.13352 | -59.43531 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59a588ee-5d58-31da-a239-08cf5866d7fc | 0.92777 | -60.32859 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae6e572a-5b68-3261-a2cf-2dde5193dd2f | 1.90012 | -60.57035 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a8e4b9b-b06b-3c0e-b109-b9c6474855a2 | 1.04288 | -59.5712 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36a0d449-b137-3d6a-9116-41fd6d8553fd | 1.32894 | -60.71984 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 926139f2-aa67-3ba3-8608-32c46ff88907 | 1.12351 | -59.43689 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4916109-35f5-3689-ac85-a579ae354615 | 3.52594 | -59.89292 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d66d441-e8a4-3cb6-a251-cff1a9c00abb | 3.22126 | -60.37449 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 191792d2-f8f6-3ecf-9f2a-d39b14b51041 | 3.32967 | -61.02309 | 2025-01-17 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 724a78ba-e5f8-3e8d-b9ec-b865d20c7e89 | 1.17688 | -60.48682 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80809951-255c-3290-b269-833654c1ed20 | 2.16045 | -61.86272 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9e0711c-d47d-3d6e-8b0e-ca145752e71f | 0.72901 | -60.12402 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d32548e-e93d-3e66-9f0e-f278b313b75f | 3.92652 | -59.67504 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 047deede-892a-3a8b-9da6-affec0994138 | 0.55833 | -59.68607 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da84a38a-b573-30aa-8792-e0df8a5fa34d | 2.17343 | -61.85701 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b39cf8b0-7964-31b6-adf6-76027b6e0fee | 2.11588 | -61.8215 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 066afc54-9e09-381e-a8f4-57581cbc9214 | 4.17817 | -60.45427 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4485e36-025b-3564-bbe6-5aa570055dfd | 1.12015 | -59.45893 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25ad7e72-4fe6-398d-a84a-a31b479a0775 | 2.28963 | -60.21743 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80c43683-1da0-3c3b-913e-44f006e18edd | 1.90066 | -60.57378 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1382806e-a110-3471-9a2b-d3e25338f792 | 3.84991 | -60.15942 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23f3d085-7389-3f5f-afdf-dd080afa30ed | 2.16948 | -61.85391 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6313b54-b98c-318e-8f82-f3c84e85b238 | 2.11306 | -61.82564 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ae253b-eb5c-3cbf-9b90-8e1881e91f29 | -0.35664 | -62.75222 | 2025-01-17 05:27:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc2984b7-2a67-3b29-a852-316ba4624d80 | -0.35606 | -62.75593 | 2025-01-17 05:27:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d91662-0b1f-3783-b203-129bf7df070b | 3.79223 | -59.72813 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61e5c182-758d-32b4-ad2f-d5359081cd21 | 0.84795 | -59.54028 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf15f6aa-b56e-3555-b951-c310bac71859 | 0.71308 | -59.22882 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0fc8814-b245-3f53-8505-41ca9aeb17fa | 1.32693 | -60.03732 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5ad00be-9a96-31f7-94e5-3f73980fa79b | 0.16712 | -60.65564 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86c4f863-360b-3b64-a398-7eb88f613689 | 1.32639 | -60.03387 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fc9eb97-b8f0-34ad-9c0d-2da7d6bf1995 | 2.1875 | -61.81415 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e0342bd-0f24-351e-a389-47de2460dc2c | 2.19891 | -61.81235 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17214628-1229-3934-a5a6-e368b94114dc | 2.19089 | -61.81362 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d38829cd-5aad-36ac-8fb9-0e2164f5f76c | 0.72515 | -60.12109 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fc742ba-5dac-3ec0-a1c4-a48405f07313 | 0.63378 | -60.03637 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f4eac78-5146-3af3-a974-54c16467a47c | 1.17189 | -60.49814 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e978e1-8994-350a-af58-fdb8759b68a2 | 3.60324 | -60.10256 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6d76dd3-8a0f-3cfc-bb3a-578e62f8de9b | -0.1556 | -60.8713 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22ab5877-6b9e-3506-a037-3708d7de0a00 | -16.1156 | -58.18116 | 2025-01-17 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d6e6386e-0870-32f1-9ce4-2addc685d405 | -16.11613 | -58.17691 | 2025-01-17 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 53c0d26a-2ecc-3cee-be24-6bba38e6a02a | -16.22371 | -60.1115 | 2025-01-17 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 860099c3-8679-3c76-a96a-514367cf7a88 | -15.60783 | -57.34321 | 2025-01-17 05:29:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0acce1fb-c707-37f3-a26a-d8362327788e | -15.38962 | -59.57763 | 2025-01-17 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3a44c7-e7b7-3a32-80be-63748bd364fc | -15.38916 | -59.58088 | 2025-01-17 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edaf2206-0c17-3f70-8fbf-338143bf1264 | 1.3403 | -60.0271 | 2025-01-17 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fc1cc04f-b2bd-30c6-ade7-e015973e57ea | 1.3403 | -60.0271 | 2025-01-17 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 330d91d3-045a-3aa3-9b1b-20d2211364d4 | 1.3403 | -60.0271 | 2025-01-17 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b33a3e85-6c1a-32fb-831c-e5acfc9eec2d | 1.3403 | -60.0271 | 2025-01-17 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1d2c35cb-a534-377b-a332-066a1c0607da | 1.3403 | -60.0271 | 2025-01-17 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 52a919b4-fd9f-3031-b1f0-2122cb21dfc9 | 2.9861 | -60.25206 | 2025-01-17 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b28ae25e-c8c3-3813-a4b9-f8b9b170e1c8 | 0.72746 | -60.1268 | 2025-01-17 06:18:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bc21c60-7267-3a7c-b0aa-e92f884e3c4d | 4.0243 | -59.67664 | 2025-01-17 06:18:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2a2f6ae-fd9d-3718-8089-f381b56f144e | 2.28581 | -60.22133 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69cb0f17-4eb7-3f47-add4-dbbae4d0e517 | 1.8985 | -60.5686 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4eca80fd-9010-3f53-8806-2c53ed75a4a9 | 2.28858 | -60.22058 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc87e84b-4816-3477-9f5c-12d23d1bea51 | 1.34397 | -60.03579 | 2025-01-17 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| eb5182d3-7332-3b68-8c5c-102de0e11f76 | 2.1953 | -61.81108 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 961533ac-d14e-3b17-a088-8e48a13b7047 | 1.17306 | -60.48546 | 2025-01-17 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cbb2316-0b14-37e1-8a5d-4cce412638ba | 2.19603 | -61.81557 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d73545a-1aef-3b0b-927e-82c25d5633b8 | 1.34291 | -60.02931 | 2025-01-17 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4e536ae5-570d-3049-b3eb-609c6b8d24c5 | 2.98707 | -60.25775 | 2025-01-17 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf20c53-ea8d-3595-89e0-86d863c6794f | 2.29244 | -60.22009 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5018ed-b641-3d47-ba51-e232b206e569 | 2.17798 | -61.85661 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a470107-ffc9-3392-9019-693019b3248f | 2.18926 | -61.81213 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6eecd34-4ac2-396a-b444-6033e1dc1b7e | 2.17197 | -61.85772 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c2624ec-f78b-3763-84fa-677c0f92e41e | 1.89942 | -60.57424 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af5428dc-d028-3617-8f99-28deba88df0a | 1.34969 | -60.02795 | 2025-01-17 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 39236325-e8e6-3c0c-b141-fc10ec6bf363 | 2.19001 | -61.81668 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff5ac7a-4e8e-3f4a-bbe3-defe5f91f47f | 2.29519 | -60.21922 | 2025-01-17 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a85d121d-5e69-3b1c-8b57-c7ac12b175b9 | 2.98051 | -60.25889 | 2025-01-17 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32ba719a-0fd4-3c1f-8f1c-a8393473c61d | 0.72644 | -60.12047 | 2025-01-17 06:18:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7efd4604-ba1e-3446-9bdc-c4a7409a2676 | 2.16595 | -61.85875 | 2025-01-17 06:18:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4e75ea9-b794-322b-9c23-17bbee1fc7d6 | 1.17121 | -60.49039 | 2025-01-17 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5f393b0-673f-3dcb-9208-99ed14077344 | 4.02805 | -59.67783 | 2025-01-17 06:18:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fa706c1-6276-3c1e-8bf8-db4108688a84 | 4.12352 | -60.02792 | 2025-01-17 06:18:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3e1e9ff-05f2-31c9-aa51-fa1041568b9a | 4.11682 | -60.02818 | 2025-01-17 06:18:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450f76d5-cc48-303e-a2d9-1ee36b90536e | 1.3403 | -60.0271 | 2025-01-17 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0764fec4-c225-37f4-8483-09b3ff07d7b1 | -7.35625 | -72.92159 | 2025-01-17 06:20:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e872fef3-671d-38af-8804-53debd55473c | 1.3403 | -60.0271 | 2025-01-17 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2858f4bf-96a5-3187-838e-e5cc5ca6d11d | 1.3403 | -60.0271 | 2025-01-17 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0c66fb9c-a829-384b-a66e-f2dde9c75fb3 | 1.3403 | -60.0271 | 2025-01-17 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| dbb5e9b1-3c65-36a4-b073-ee6453952f9c | 1.3403 | -60.0271 | 2025-01-17 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 03338c9e-f74c-3a9b-8dc9-ca6d68608dba | 1.3403 | -60.0271 | 2025-01-17 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e87fd9e9-1312-3a61-a6c7-22f7ae1a3687 | 1.3403 | -60.0271 | 2025-01-17 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 024f1c8c-559e-3211-ae41-f3eb4b834b0a | 1.3403 | -60.0271 | 2025-01-17 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0281470b-347a-3fe2-aa42-ee11ce19c1ea | 1.3403 | -60.0271 | 2025-01-17 08:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c4346d8a-1fc9-3146-a207-ee515b29664e | 1.3403 | -60.0271 | 2025-01-17 09:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d0475456-86cd-3582-a1a6-6ccf82ab45d8 | 1.3403 | -60.0271 | 2025-01-17 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4b33b01c-d244-313d-af04-961e9eeddd10 | -15.83 | -43.46 | 2025-01-17 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 09731597-e15e-34dc-a7d6-b84ca282b18e | -19.6836 | -57.9712 | 2025-01-17 13:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |


[Clique aqui para ver as próximas entradas](README6.md)
