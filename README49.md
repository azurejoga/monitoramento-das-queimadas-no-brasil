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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a7bcf75-280c-3fae-bc11-87967cfec210 | -17.6463 | -57.5257 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 91063d7e-03eb-36b7-9572-c3517f128a58 | -17.6073 | -57.5099 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| e237fd12-b9df-37a3-aa23-6712f121164a | -17.2737 | -57.488 | 2024-11-11 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 9807da8e-0c46-3e0b-b39a-bab91f9eb2f3 | -17.5875 | -57.5122 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.3 |
| a79f637f-5add-39bf-bee7-c4db305f6e72 | -17.2737 | -57.488 | 2024-11-11 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 8510c6a2-60f4-317e-b4a2-56f952d0230d | -17.2936 | -57.4652 | 2024-11-11 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| fdbbbea2-af04-3d05-9e18-7c0befa6e8ec | -23.9312 | -54.034 | 2024-11-11 12:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.2 |
| 996766d0-7807-380f-b64d-94277b95e8c2 | -17.628 | -57.4458 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 628b0d25-0647-31a1-9241-606736d4e0d1 | -15.9791 | -59.3468 | 2024-11-11 12:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b766c84d-810d-3144-9ffc-6cb42c053bdb | -17.6083 | -57.4482 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 3b538b1c-6f00-34bb-951c-0618403849d1 | -17.6463 | -57.5257 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| f0469359-376a-3f86-b89c-b8f56c893d72 | -17.5875 | -57.5122 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 811442a6-0ec3-34cd-a7ac-1d20de894b54 | -17.5872 | -57.5328 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 3d9ff60f-4e36-3688-a83f-1a98465d9118 | -17.6086 | -57.4276 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 4042359a-a8f0-3851-8da8-b2f25d19c165 | -17.6069 | -57.5304 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.6 |
| f3133fc9-f420-3906-b523-449c67ccec6c | -17.6066 | -57.551 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| f2271b60-3dab-3d33-85d3-4951ce7e3ef9 | -17.2933 | -57.4857 | 2024-11-11 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| dd2c84ad-cf00-35df-8a2a-aa6431da4760 | -23.9306 | -54.0564 | 2024-11-11 12:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| cd34f2e8-80b8-359e-adb4-0c84cac90a77 | -17.6266 | -57.5281 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 7892c44e-94d5-34a7-9f90-31bd02753b80 | -17.6283 | -57.4252 | 2024-11-11 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 8cfa0821-b4f8-3b8a-a48f-808459708f95 | -17.2933 | -57.4857 | 2024-11-11 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 195d03c7-8b8b-3d6a-a4ba-f7a2753b8482 | -17.2936 | -57.4652 | 2024-11-11 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 89f263d2-0001-344b-a8a6-7f1feed95d4c | -17.6283 | -57.4252 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 1db7c435-2aa4-3947-93c8-4c90b770a473 | -17.6086 | -57.4276 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| b2311a7e-6e99-39fd-8503-8604b08b41de | -15.9791 | -59.3468 | 2024-11-11 12:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| ccdef7a2-28eb-3639-b00a-ddf73e6e93d5 | -17.628 | -57.4458 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 404c6471-de9d-3f63-b370-e21fc63b1fb2 | -23.9312 | -54.034 | 2024-11-11 12:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| ce10df06-a90c-30aa-9b37-651a10f6d0df | -17.6463 | -57.5257 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 8038f0fd-7615-3667-9b7f-976ea8c11603 | -17.2737 | -57.488 | 2024-11-11 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 181a4ab0-43c4-3b66-9c5b-8c7031952654 | -17.6266 | -57.5281 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 9020b0c1-68c6-35db-95b1-cc6b7f5c6388 | -17.5875 | -57.5122 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.2 |
| b3ee7c71-b55f-30df-9065-4e79196db985 | -17.6066 | -57.551 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| e407c080-ccd2-3a50-821f-d163abeb4ebc | -17.6083 | -57.4482 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 42526e05-067a-373b-93e0-8f043edd45e7 | -17.5872 | -57.5328 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| c2c66995-c10b-3862-9cd4-c7b1e9d7951a | -17.6069 | -57.5304 | 2024-11-11 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 157.6 |
| 949d28b6-43a3-3632-bb73-21779c4c950f | -2.69835 | -46.67062 | 2024-11-11 12:42:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 58bc1cd3-c5fc-3cca-a630-27529703c082 | 1.47699 | -56.03261 | 2024-11-11 12:42:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4e9da658-23a2-3912-b809-d220fe0ad71c | -2.2318 | -46.44274 | 2024-11-11 12:42:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1fdb9af0-c41a-3d76-b44e-cca9a60e7141 | -3.37998 | -41.47806 | 2024-11-11 12:42:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| cf6797d1-e9c1-32ef-ab95-b09554303a8f | -3.37771 | -41.49437 | 2024-11-11 12:42:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 45.1 |
| 60dbd4c0-73d0-32f1-80ef-5734c63b0b66 | -2.42349 | -46.51777 | 2024-11-11 12:42:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 56b80c3c-ca2a-3474-a514-e965ad398905 | -3.48454 | -40.90439 | 2024-11-11 12:42:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 48.6 |
| c3592f1e-62ec-32bf-b29f-3c819d6c940b | -2.90995 | -45.64363 | 2024-11-11 12:42:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 41a4b715-3399-38f6-993f-5e78e6f36756 | 1.47767 | -56.02463 | 2024-11-11 12:42:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0c57f577-caf0-3986-8d08-6d51bd79c83b | -3.12944 | -45.97637 | 2024-11-11 12:42:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fd4e4a94-e5c2-3ad8-8748-1157efa64f98 | -2.46414 | -46.23678 | 2024-11-11 12:42:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f0df954d-6f24-338c-8e49-11e38d66cd34 | 0.45514 | -50.96175 | 2024-11-11 12:42:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c8dd839e-b14e-344a-bd0a-3272237bb5bd | -3.48794 | -40.91078 | 2024-11-11 12:42:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 74fc021f-bf0d-33e7-a660-5a7b96c10681 | -2.34523 | -46.56055 | 2024-11-11 12:42:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d88000c0-62d6-3bc1-a195-98a59dae8020 | -2.41466 | -46.51653 | 2024-11-11 12:42:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 0dcd1a96-a628-38df-baf9-15b5abdf9a86 | -2.5447 | -46.31725 | 2024-11-11 12:42:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 34ac5a59-b9cd-3b23-a8cb-3ea5914b04e3 | -7.71643 | -39.21266 | 2024-11-11 12:44:00 | TERRA_M-T | CEDRO | PERNAMBUCO | Brasil | 2604304 | 26 | 33 | nan | nan | nan | Caatinga | 27.4 |
| b712276b-acbd-30af-b3f8-b502b854b01c | -17.59368 | -57.43134 | 2024-11-11 12:46:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| ba09daa0-0275-398d-a448-72fe357c87cd | -22.83136 | -46.33255 | 2024-11-11 12:46:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 46cd5a56-da4b-3918-bde5-ee7bf9e55ef7 | -17.76345 | -50.07543 | 2024-11-11 12:46:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ef51c586-aa24-38f2-811c-268f6ef6ea34 | -15.98792 | -59.33842 | 2024-11-11 12:46:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| d2d083be-4f9c-3543-8927-a6e14ba8986b | -17.62105 | -57.43678 | 2024-11-11 12:46:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 6b148972-2590-34b9-851d-dce876588068 | -22.8331 | -46.31757 | 2024-11-11 12:46:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| b2c55933-9ce8-397a-82f9-43cbd4572cc0 | -15.99747 | -59.37696 | 2024-11-11 12:46:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9893bec0-fa20-3414-b09f-01c6db441522 | -19.43698 | -50.80838 | 2024-11-11 12:46:00 | TERRA_M-T | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 04e221d6-ed1b-3d99-8f4e-618f6e714b4a | -23.61539 | -46.98899 | 2024-11-11 12:46:00 | TERRA_M-T | VARGEM GRANDE PAULISTA | SÃO PAULO | Brasil | 3556453 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| af4cbd3e-7acf-3c7c-b42a-19aa5b26506e | -22.80376 | -46.28385 | 2024-11-11 12:46:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 0aa66848-3922-3034-86b6-686bc9900d11 | -17.2883 | -57.47091 | 2024-11-11 12:46:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| c640e340-4995-3cd1-bf45-4c4ad43035c1 | -23.32261 | -46.22651 | 2024-11-11 12:46:00 | TERRA_M-T | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 2f689d1e-0810-3796-9e1c-2ede0c490883 | -23.93991 | -54.04708 | 2024-11-11 12:48:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 1d6b9964-800a-3164-a3ce-58b142e0431c | -29.6009 | -51.96949 | 2024-11-11 12:48:00 | TERRA_M-T | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| de8fc716-3561-362e-a7d6-bfc79b812ee0 | -29.0546 | -51.18579 | 2024-11-11 12:48:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4f718bdb-aa58-3e7e-9185-3b95a55b299d | -23.68207 | -51.7276 | 2024-11-11 12:48:00 | TERRA_M-T | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| f3856274-66bd-3c6c-999d-b269b98b2440 | -26.33242 | -53.18887 | 2024-11-11 12:48:00 | TERRA_M-T | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| cc23b917-cbef-3ef0-bef2-a29272965b17 | -26.18873 | -51.60819 | 2024-11-11 12:48:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| cc5e0c46-adf9-3ae0-a251-1b5d9f39f993 | -27.37351 | -51.56916 | 2024-11-11 12:48:00 | TERRA_M-T | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| bb0d3f99-4a91-3f12-a57e-c03339dd5a2b | -27.07554 | -51.9764 | 2024-11-11 12:48:00 | TERRA_M-T | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b794aacc-43ed-3b9b-acaf-fdb21be4b115 | -23.02474 | -53.59809 | 2024-11-11 12:48:00 | TERRA_M-T | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 39ee3fc1-8217-3c52-9f27-2269d18c6393 | -23.93033 | -54.04527 | 2024-11-11 12:48:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 236f78d6-8484-37d3-bbff-83c5523d7922 | -25.60893 | -49.17204 | 2024-11-11 12:48:00 | TERRA_M-T | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d89f620b-7a90-3703-a415-78069d526429 | -25.64896 | -49.27541 | 2024-11-11 12:48:00 | TERRA_M-T | FAZENDA RIO GRANDE | PARANÁ | Brasil | 4107652 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 847f8f40-f435-30fe-ac39-9cc239503a0a | -23.89392 | -51.47917 | 2024-11-11 12:48:00 | TERRA_M-T | BORRAZÓPOLIS | PARANÁ | Brasil | 4103305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 3cc0d7c7-e5aa-353f-80d9-e17482c9e2a4 | -23.9306 | -54.0564 | 2024-11-11 12:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 131.0 |
| d2ecbbbc-3bcd-3fbb-916d-f1c2a7247d13 | -17.6283 | -57.4252 | 2024-11-11 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| bd99cecc-775e-3669-b0cb-e26fc9879666 | -17.6083 | -57.4482 | 2024-11-11 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 14abc4ad-6fc3-3d6a-8223-0d23eb07e15a | -17.6086 | -57.4276 | 2024-11-11 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 8536e765-fc09-369b-adba-67ff3fdb7546 | -17.254 | -57.4903 | 2024-11-11 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 7afddd5f-a286-3cfe-bb3b-31b1bf04222a | -17.2737 | -57.488 | 2024-11-11 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 6d4c442f-44bd-3c04-9d91-3c951c4cab8d | -17.2936 | -57.4652 | 2024-11-11 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| ee14a6fa-a460-38f3-829e-cc8f67a09fa8 | -17.2933 | -57.4857 | 2024-11-11 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| 701bf6e5-8707-3f32-816c-609efbc2fbe4 | -23.9312 | -54.034 | 2024-11-11 12:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 183.2 |
| d6b834e0-3fc4-32f7-96e9-b4fff8bf5d4c | -17.628 | -57.4458 | 2024-11-11 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 02408774-a649-369a-834d-b0b6f09d050a | -30.54972 | -52.87399 | 2024-11-11 12:50:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| 80f38d76-fbf7-3308-bf82-d1512d908131 | -30.5512 | -52.86374 | 2024-11-11 12:50:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 27.7 |
| 1c87fc2c-a8dd-3622-b988-5e48144db51f | -30.06475 | -52.39966 | 2024-11-11 12:50:00 | TERRA_M-T | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 9.2 |
| a08a4af0-6e52-3729-835b-50ff16dffa81 | -17.254 | -57.4903 | 2024-11-11 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 9266b191-54f0-33e7-bd55-14b9732a6b8b | -17.6083 | -57.4482 | 2024-11-11 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| e64275e2-9ee9-369e-80d0-75b8d5e795fc | -17.2933 | -57.4857 | 2024-11-11 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.4 |
| d859613a-a999-390c-a463-f6b3f51729c4 | -23.9312 | -54.034 | 2024-11-11 13:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 189.4 |
| 27ad2299-6096-3671-98fa-4f3d45ed0b71 | -17.2936 | -57.4652 | 2024-11-11 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 8a950201-82c5-3ba5-a341-8fa097ed007a | -17.2737 | -57.488 | 2024-11-11 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 69d3146c-bdac-3f96-a9e4-d99e44063ca9 | -17.5889 | -57.43 | 2024-11-11 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 135cfb20-8dd9-39b7-8fdd-5ceb4017dfba | -15.9791 | -59.3468 | 2024-11-11 13:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 53ca9bc8-530e-302f-8499-b8cfe11ba2d3 | -17.2766 | -57.3032 | 2024-11-11 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a4a0f1c7-3076-3b83-a468-6434f6d1e976 | -17.6086 | -57.4276 | 2024-11-11 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |


[Clique aqui para ver as próximas entradas](README50.md)
