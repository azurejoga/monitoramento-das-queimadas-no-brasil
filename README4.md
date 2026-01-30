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
| 63288a7e-1755-342b-af17-6af082967118 | 2.42873 | -60.23762 | 2026-01-30 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4e0fd39-ac43-3a46-8e64-d27cf41d23cb | 3.54407 | -60.70975 | 2026-01-30 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49a929b6-2452-34b5-848a-f3a1e1ed0e24 | 1.83248 | -60.8372 | 2026-01-30 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be101691-f756-3c2c-b390-228a5a767540 | 1.83181 | -60.83283 | 2026-01-30 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c58707ca-788d-3bb6-80ef-709fbb32899c | 2.74597 | -60.21849 | 2026-01-30 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 630eedfe-de51-3b12-a5eb-51ec91b1165b | 3.86436 | -60.5381 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a60b861-66d4-32d2-9f2a-d3dfc2a980e3 | 2.56295 | -60.38241 | 2026-01-30 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 067bdf0c-b8ac-3fdf-8c30-88aab9cfd9f6 | 3.48007 | -60.07209 | 2026-01-30 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 664fe091-f3f2-38f5-b12b-c637d5a8ef3c | 3.55163 | -60.53376 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68f57368-9024-30b7-84be-34b0108969d8 | 2.74896 | -60.21376 | 2026-01-30 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01342d68-7c40-39b5-9032-5e58169b304a | 3.86367 | -60.53362 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0263e3fa-97f2-3835-a726-107ff88131b2 | 3.53344 | -60.716 | 2026-01-30 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1753e570-0c27-32d6-abca-94b1db296fa6 | 3.54338 | -60.7052 | 2026-01-30 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18ee5f36-1371-3edb-8dab-9c3aa21c8f1e | 4.01767 | -60.88363 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6817d00-c737-321c-9038-e609933e7591 | -2.90411 | -49.37877 | 2026-01-30 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2934b24-d320-3d9e-b5b4-449087d8a251 | -3.74224 | -52.43346 | 2026-01-30 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac3b53aa-b58a-30f9-81ad-a5d9acc78418 | -1.62321 | -53.40305 | 2026-01-30 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3318aedd-8b49-3fb7-8ec5-e5b2a8cb3725 | -2.49721 | -56.07958 | 2026-01-30 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82fc68b4-953f-3c23-a3f7-e7a7bce317c1 | -3.55587 | -54.72357 | 2026-01-30 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 791cf679-da73-38f3-ba67-beb92ef51f39 | -2.81592 | -52.95829 | 2026-01-30 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e1fc2af-723f-35c7-8305-2681660a08b9 | -2.90238 | -49.37804 | 2026-01-30 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f61c141-fd1e-3dd9-94ae-6f75ef710049 | -2.15575 | -53.64922 | 2026-01-30 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8485fd6c-4708-3234-a038-59d231870102 | -2.92512 | -52.69305 | 2026-01-30 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad61970c-7a23-345d-99fa-72071ab207b8 | -3.16386 | -52.85258 | 2026-01-30 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40c5a99f-a32e-3f7d-94c1-139dbbe3f803 | -1.84055 | -54.09977 | 2026-01-30 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95c75f2b-0a73-3480-9f21-0c2e31816959 | -2.50067 | -56.08014 | 2026-01-30 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03c168c-4cbb-37f0-aa17-bbeb91f7adfa | -1.84433 | -54.10044 | 2026-01-30 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c0d9e1f-606c-395a-b71a-23ded825283e | -2.89881 | -49.37799 | 2026-01-30 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ad6366e-48d9-3045-9409-eb122e879f7d | -3.7379 | -52.43277 | 2026-01-30 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43a9a9c6-41d4-3d88-a9e6-8fad8e2851b9 | -4.19776 | -55.68254 | 2026-01-30 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43b548f8-9dcd-3c22-abcc-a0b8024743c4 | -4.08166 | -54.81164 | 2026-01-30 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83f193b4-232e-3fff-9bb9-2db3c091f5a8 | -12.54867 | -54.59763 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e4259b3-57eb-3a1e-9bb3-8cbe2b02c604 | -12.54613 | -54.59454 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905b10de-6818-374c-a626-66cd18ba3a72 | -12.54387 | -54.60102 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b42c789f-49d8-3712-980f-49f408070e28 | -12.54557 | -54.59855 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4006c74b-5aba-3a35-ab12-9e60885bccb6 | -12.54921 | -54.59359 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a90a1c92-4c37-3b38-90e4-31811a46f5b4 | -12.54975 | -54.58954 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecdc9404-c8bc-38ac-aec9-991731af1ecc | -12.80227 | -62.15807 | 2026-01-30 05:25:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6329497-6fd1-3c70-83d6-415c1ed21833 | -12.54814 | -54.60164 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 829dfa0f-d21e-378d-b31f-afa7c10b2572 | -12.34617 | -54.76673 | 2026-01-30 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5a0fffd-741f-3595-9fd3-3a8aaa0aea0f | -13.78652 | -52.73246 | 2026-01-30 05:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec7e6eb-be1f-3694-8f40-e0af8780639b | -12.55457 | -54.58604 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0062616-5380-3069-b550-65710ed9d76b | -12.29965 | -57.40379 | 2026-01-30 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afe22c25-b983-36e1-bf16-b4eac713db7e | -12.5444 | -54.59703 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398b5e78-4aa4-3717-91b5-13dc1be9bd34 | -12.54501 | -54.60254 | 2026-01-30 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2deba399-0b24-391a-9158-240e98a9f0c1 | -12.3467 | -54.76285 | 2026-01-30 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b6984f-81c6-3337-a272-5062096f4833 | -20.28646 | -57.34892 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 924806cb-c89f-3fba-8e16-2ad8c66edad6 | -19.14636 | -57.79478 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57f28019-2498-36a0-a41a-4e3516badeba | -20.31251 | -57.3494 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9ba3a066-9c50-3ffe-a2c1-76a62bb3351a | -20.26208 | -58.13942 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 308c108f-2475-3a27-8dcb-e9ce9fb21f57 | -20.29444 | -57.35009 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d3237e-5062-3167-a791-8f714e29b732 | -20.26589 | -58.13999 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ea775382-dbe2-3ee5-9d4a-803c6c11b76a | -16.59126 | -57.80651 | 2026-01-30 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 053fe8ad-f982-39e1-a62e-4e27ffe47124 | -16.01233 | -59.87167 | 2026-01-30 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ad4061a1-463e-3819-b804-c6ebdb39262d | -16.59062 | -57.811 | 2026-01-30 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9e535c68-35f6-3492-b241-5f4e24d6c799 | -16.58755 | -57.806 | 2026-01-30 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f2909df9-aa73-35c2-928b-79ca8a00c680 | -16.58321 | -57.80988 | 2026-01-30 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 369197b5-4a94-3133-a2b5-8f8c200b2b8b | -20.3151 | -57.34759 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6195e22e-359e-33de-9696-1ad06be41d59 | -20.26523 | -58.14489 | 2026-01-30 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3a66e95e-29c6-3911-9363-8bedda2f6cb6 | -16.58691 | -57.81046 | 2026-01-30 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d0481914-faaf-34b6-87f7-f1a588b5d164 | 3.48179 | -60.0741 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f07bb33-8486-3d9b-a4ca-4b63407b43fc | 3.55195 | -60.53019 | 2026-01-30 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d94e4dca-f5c5-3159-a7da-b31c739b19f6 | 3.54971 | -60.53862 | 2026-01-30 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec5ebc74-37ac-311f-b57d-534b98ab645d | 2.74704 | -60.21114 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3624c9eb-d07b-3376-b072-c1397dc7116b | 2.56444 | -60.38133 | 2026-01-30 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 419e4343-9a56-3fe8-97bf-f46b6180867e | 2.75558 | -60.21828 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011ff9e0-8344-34bb-ba57-8c483516788b | 2.75624 | -60.22242 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8052001-6373-3728-9083-edfc541ad209 | 3.53416 | -60.71559 | 2026-01-30 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 281d438e-13bc-39eb-b762-8123305de91c | 2.7477 | -60.21529 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa9f5fe4-73c6-3bc1-b944-af6ae5337c2d | 2.75064 | -60.21058 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da559331-18f8-3f63-ab56-534255bc22e1 | 3.55259 | -60.53413 | 2026-01-30 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d151e498-7ce6-356a-9b2a-d11ff271aaad | 2.74837 | -60.21944 | 2026-01-30 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c721672a-f075-33a3-a946-eefb979acbcc | -1.80714 | -54.49252 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| faa7b3e9-d5b7-3dec-a729-558bd2cc50b1 | -1.80771 | -54.48878 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b222b4e4-6d56-3182-aad1-13f87bd388e6 | 1.83295 | -60.83558 | 2026-01-30 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34fdf312-e725-3870-9978-ed0895fe6b92 | -1.81333 | -54.48967 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6c9309ca-2284-30a3-9eea-8064aad325f3 | -1.84328 | -54.09973 | 2026-01-30 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b15edb-0fb3-3b60-906c-0c6be4a50103 | -1.81219 | -54.49714 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c7c26d44-261b-39e6-a4f3-efa46d4c319e | -1.80657 | -54.49625 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 286d94c7-af32-35a6-aa0d-11ba8e8dcc03 | 1.83359 | -60.83955 | 2026-01-30 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d79fa37e-5964-3ed9-91eb-169c949fa327 | -1.84269 | -54.10365 | 2026-01-30 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f93325-3420-37c1-937d-a4c62af7f26d | -1.81276 | -54.49339 | 2026-01-30 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 14f39857-e7f0-3c51-9312-c89ee7c539a7 | -12.55062 | -54.60064 | 2026-01-30 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dbd90d4-62c3-3523-919f-a050ef755094 | -12.54415 | -54.5999 | 2026-01-30 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 746e4429-fb91-3fed-8a95-18c555112029 | -12.55122 | -54.59531 | 2026-01-30 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4030a0a-18c3-3692-ac33-dc3c3f448ce1 | -12.55184 | -54.58988 | 2026-01-30 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bff465a9-04cd-3e78-9e0b-7a9b52404ef2 | -12.80433 | -62.15958 | 2026-01-30 05:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f5e69ae-f93e-3883-b8ea-01817b3be305 | -20.26318 | -58.13789 | 2026-01-30 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c176989-3641-33dc-9d15-662caf3f5110 | -20.26481 | -58.14486 | 2026-01-30 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a824976f-1409-3917-b7f7-e6a6dc8015eb | -20.2652 | -58.14078 | 2026-01-30 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd767753-90e8-3f85-b762-2f3abe76e91a | -20.26276 | -58.14196 | 2026-01-30 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 725423a7-fe5f-39b9-96b0-eff37aa2a17c | -20.25952 | -58.14016 | 2026-01-30 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 14f734bf-5afc-3140-9e2b-d004ecffb467 | -1.81635 | -54.48944 | 2026-01-30 12:31:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 088ec4df-83ae-3c3f-9677-f5be631e8cc5 | -1.80851 | -54.49211 | 2026-01-30 12:31:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2a509fda-b4ca-3fbe-a1ef-9b7b01d725dc | -11.0019 | -53.99451 | 2026-01-30 12:33:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a12cc6b5-6826-36b4-a64d-de5febb18adf | -11.33004 | -54.92234 | 2026-01-30 12:33:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c3b5e49a-86bb-3564-9dcb-ec6b13ce6d7c | -11.32875 | -54.93131 | 2026-01-30 12:33:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c42f6d72-4e19-3765-bf5b-446288231506 | -8.39449 | -44.05199 | 2026-01-30 12:33:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 4dc56ffb-12c0-380f-9263-dbe8cf392165 | -11.00963 | -52.81872 | 2026-01-30 12:33:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 527202aa-d212-32b4-a63e-00b7090bd24d | -11.3115 | -52.55872 | 2026-01-30 12:33:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README5.md)
