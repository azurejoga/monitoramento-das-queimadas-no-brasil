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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a38b2f7d-0211-3f11-8e17-3e2d3e7b15f6 | -9.7359 | -64.2295 | 2024-10-13 03:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b40ef7fd-2d92-3411-85eb-2759b933e993 | -10.5097 | -42.5023 | 2024-10-13 03:06:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 1d6742b8-efb1-3af2-8203-2b29d70f5b67 | -10.5283 | -49.9564 | 2024-10-13 03:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 56084cf7-18a1-3da2-8a92-d9bf7b2a7adf | -10.5094 | -49.9584 | 2024-10-13 03:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| bb6b5212-b235-3cc5-9e3d-cd6bf6d5edd1 | -10.9506 | -44.653 | 2024-10-13 03:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ef8765ee-8b19-3bb5-9a5b-766974ecf44e | -10.9311 | -44.6789 | 2024-10-13 03:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c32e190b-b4f4-33b0-a420-ecf21513880a | -11.2766 | -60.4455 | 2024-10-13 03:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c6abe8c1-ac52-3a3b-9ac9-f4996532af3f | -11.2765 | -60.465 | 2024-10-13 03:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0bc2b5fa-892e-3162-ba5b-c106d2487ad0 | -12.4792 | -63.0159 | 2024-10-13 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4434011d-61ca-3a86-85b8-f63852e1faf5 | -15.6419 | -59.9767 | 2024-10-13 03:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a5df1ead-f2b6-3ef7-bfcb-0ac4d4521c65 | -17.6478 | -56.2668 | 2024-10-13 03:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 238.5 |
| 20325dc8-64a9-3909-8e92-33096501eadc | -17.6474 | -56.2876 | 2024-10-13 03:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 303.2 |
| 898ab81d-97ef-32c0-ae3d-73d9523001ee | -17.6471 | -56.3084 | 2024-10-13 03:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 32b63f26-4e2f-31bd-a755-32b1672a6aa9 | -17.6675 | -56.2643 | 2024-10-13 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 2fa9cd70-54f7-3833-b931-36fa34a09b73 | -17.6672 | -56.2851 | 2024-10-13 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 99b65d37-d298-3927-bd80-0f1d8fe63dda | -17.9841 | -57.3612 | 2024-10-13 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.7 |
| 6367dddd-29b1-3727-9423-b06a87c72adf | -17.9837 | -57.3819 | 2024-10-13 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| b40060b0-29d2-3178-92bd-1c6ed6186de2 | -17.9643 | -57.3637 | 2024-10-13 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 002b89e8-1917-304e-ba2c-c271ebc81090 | -17.964 | -57.3843 | 2024-10-13 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.4 |
| bb5bd86a-940b-399c-beaf-467296eccdff | -18.2364 | -56.4806 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.0 |
| 312eb254-d528-3b43-a980-7982f5b40258 | -18.236 | -56.5014 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.9 |
| a350ebd5-c6bd-3c19-a44f-4c53bf93fa4c | -18.2169 | -56.4624 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 934ec349-4231-3d6e-abdc-f4ad20f93edb | -18.2166 | -56.4832 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.2 |
| ff229667-bacc-3b67-82c6-eedeee9e1faa | -18.2162 | -56.504 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 8bc16e6e-e3a3-3719-9087-0574ee24776a | -18.2155 | -56.5457 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| baa56cd1-c811-397d-aee6-0a2554a1c1d3 | -18.2151 | -56.5665 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 1ec39c66-ceef-36b0-a01a-c1f00fda0115 | -18.2368 | -56.4597 | 2024-10-13 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| abd7cab3-44f4-38fe-ba39-7d95b7af75be | -3.1792 | -50.4551 | 2024-10-13 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| a8d65c44-801d-3048-9909-6ae652d80e0d | -3.1791 | -50.476 | 2024-10-13 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1e542f4c-6dea-3d00-b680-4114270a50c4 | -3.1141 | -53.0351 | 2024-10-13 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| edf75cf9-bfea-3876-991c-d407ec07e498 | -3.114 | -53.0554 | 2024-10-13 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 84c8bd20-d94f-3f55-8eda-5a04b988b72e | -3.0957 | -53.0355 | 2024-10-13 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| d87c4f46-75fc-34a5-b606-cc484636cfbf | -3.0956 | -53.0559 | 2024-10-13 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ef2a6cce-4adc-3718-ab39-2566d015868b | -3.0773 | -53.036 | 2024-10-13 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 86af1b72-7841-37f7-be5f-e0c573a1099f | -4.1149 | -48.2299 | 2024-10-13 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 012251a9-dc84-3ee8-8af1-146876ff1c15 | -4.1148 | -48.2515 | 2024-10-13 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 183c71d1-18c7-3038-aa02-7c48f68ac145 | -4.3985 | -44.4881 | 2024-10-13 03:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| cc5cc1ef-93fb-3e28-b415-2d78ca45e4d8 | -5.1238 | -60.3397 | 2024-10-13 03:15:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 29a1ff9e-bf2a-3751-b5d2-5d04294d396f | -7.6815 | -47.3213 | 2024-10-13 03:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| fd82922b-82c6-3cc4-a544-071c058a2570 | -7.6627 | -47.3229 | 2024-10-13 03:15:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8548f1d8-50d2-3064-b7c6-4d23ff5d18a8 | -9.7359 | -64.2295 | 2024-10-13 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d44569b7-a17a-3afd-a70c-a3a634087234 | -10.5097 | -42.5023 | 2024-10-13 03:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 7007de3a-baee-36c6-aa89-6147bbb78b12 | -10.9506 | -44.653 | 2024-10-13 03:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7038ecfd-c5c5-3322-968e-7e6170d10bbf | -10.9502 | -44.6762 | 2024-10-13 03:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| fd4f791d-85cb-3001-a9c4-bbfb1213df74 | -10.9315 | -44.6557 | 2024-10-13 03:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f84879b7-adf0-3acf-b8ba-77988e018e8f | -10.9311 | -44.6789 | 2024-10-13 03:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 65fad5c6-0b69-3244-b20a-f8b5af27be2c | -11.2766 | -60.4455 | 2024-10-13 03:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 05dcf6f0-8021-36d3-8edd-20eb6b4c8bf0 | -11.2765 | -60.465 | 2024-10-13 03:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4f81e3ca-1c8b-3e6a-98f9-403deffe7a79 | -11.6334 | -48.3736 | 2024-10-13 03:16:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 16662693-b8c6-3cb7-b72d-f5dcfd12ab17 | -12.4792 | -63.0159 | 2024-10-13 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8b872420-79e5-3384-b858-48ef2ff00e37 | -13.7348 | -60.5883 | 2024-10-13 03:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cb10589f-b1c5-3a69-88b2-e2292ff819af | -13.7346 | -60.6079 | 2024-10-13 03:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| aca06d46-1938-38d5-a941-43a5dcfc738a | -13.7541 | -60.5672 | 2024-10-13 03:16:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 443bbe3d-d855-3ec5-855a-198d14abca40 | -15.3244 | -41.8911 | 2024-10-13 03:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| 8c622802-9431-3385-9a27-dc667f0ee2ea | -15.6419 | -59.9767 | 2024-10-13 03:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fe9a2497-94e9-30d2-8f04-845f2a4f0cc3 | -17.0626 | -56.01 | 2024-10-13 03:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 1a70190c-e417-39a5-8b35-00be0ab798dd | -16.9995 | -57.4791 | 2024-10-13 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 9de1513e-f449-3b2d-a575-d1b3f9eb0a31 | -17.2639 | -42.6527 | 2024-10-13 03:16:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| eb0e5665-1a5f-350a-b94b-b4140458a3a3 | -17.1957 | -57.4562 | 2024-10-13 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 05b9a3fd-eadb-37e8-867a-198f953497d0 | -17.1954 | -57.4767 | 2024-10-13 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| d0e36898-9841-34bf-98dd-6c91f842a2a8 | -17.1758 | -57.479 | 2024-10-13 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 796164ee-d0f3-359a-8498-8f8c00a5274d | -17.6481 | -56.246 | 2024-10-13 03:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| bf93039b-102e-39bf-8f40-a631a8244d46 | -17.6478 | -56.2668 | 2024-10-13 03:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.0 |
| 3e935c59-a67c-35f3-90e5-3cad52b485c4 | -17.6474 | -56.2876 | 2024-10-13 03:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 215.5 |
| 5ebfc44c-ca82-3cec-9f8c-8526c9f510f0 | -17.6675 | -56.2643 | 2024-10-13 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 45dc40a2-c0ed-321c-8874-18771535f983 | -17.6672 | -56.2851 | 2024-10-13 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| faf26a09-1bd6-3002-85e5-eced70d09060 | -17.9841 | -57.3612 | 2024-10-13 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| c97cac82-d935-364a-b28c-f298daf681b8 | -17.9837 | -57.3819 | 2024-10-13 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| da7ff19b-a42e-338b-ab58-01116502045c | -17.9643 | -57.3637 | 2024-10-13 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.1 |
| bf112f8e-23b5-3821-9b19-eb0e5eac6a85 | -17.964 | -57.3843 | 2024-10-13 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 01bbeb78-def0-33c3-b38f-83ceba9adea8 | -18.2364 | -56.4806 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 254.7 |
| 235a48dc-6256-3289-b1ef-f0f53a391317 | -18.236 | -56.5014 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 216.7 |
| 89be5a72-f281-3616-9ed5-a5f4bc9a685b | -18.2169 | -56.4624 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| c0d15d45-346e-3b8c-92ab-8bb17224cba2 | -18.2166 | -56.4832 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.4 |
| a29cf4c7-7ffc-394a-8a39-42c7c780baa4 | -18.2162 | -56.504 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 892703c8-cc45-3230-af8d-c4ad4363d304 | -18.2155 | -56.5457 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| af4bc036-a64e-3c0b-93d6-384350a42890 | -18.2151 | -56.5665 | 2024-10-13 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 3f63ff6d-3e77-3096-bee3-8cdcdd50df02 | -4.09295 | -43.9205 | 2024-10-13 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eebd287-ff1a-3871-b3d6-14a9d6dc830e | -4.0922 | -43.92089 | 2024-10-13 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ead6f7-9ff1-311c-a652-23dfe7b7d0f7 | -4.09166 | -43.92761 | 2024-10-13 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 336d15d9-cd17-362c-a70a-8b81c957e744 | -9.30413 | -35.60238 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 28194fe3-4a10-386f-9d0e-27c2182e92f7 | -9.30327 | -35.60732 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 11400426-8493-3bc9-8c28-43b9d276d3df | -9.30198 | -35.60045 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55f26cc0-a122-3353-8759-233d5248b806 | -9.30114 | -35.60543 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 1d01efbb-72ee-38b4-b98b-925323bd146b | -9.30019 | -35.6017 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bbfcc55e-974c-3cb7-92d2-56915627547b | -9.29932 | -35.60668 | 2024-10-13 03:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d0431a75-e78f-38fd-b610-aadd8a192ea4 | -8.50839 | -35.45298 | 2024-10-13 03:21:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e3ec16f-cd6d-31df-823e-788c06be0ff2 | -9.71666 | -36.43345 | 2024-10-13 03:21:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 99b399ae-753f-303a-9946-2a3a7c2788ad | -9.71616 | -36.46044 | 2024-10-13 03:21:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a71a0e4c-cf02-3775-ab02-bd21f4ac3169 | -9.716 | -36.43718 | 2024-10-13 03:21:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 70a59dad-ddfc-3a41-8629-6af1ed2f8295 | -9.71053 | -36.44407 | 2024-10-13 03:21:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c72f3b3d-e3b6-3115-b499-b4493640693f | -6.65718 | -37.47672 | 2024-10-13 03:21:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 20648d05-e757-3a77-a2f5-d39542d5988e | -7.88724 | -39.15177 | 2024-10-13 03:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 167254fc-0f67-3dfd-adae-530f1452ce76 | -7.51784 | -40.51743 | 2024-10-13 03:21:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e1346d6b-5e89-3e4d-ba0f-80622cae971c | -7.51721 | -40.5209 | 2024-10-13 03:21:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fba19b53-0253-3649-b88d-7e575e46e452 | -7.51157 | -40.51991 | 2024-10-13 03:21:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a909e4a6-870f-3a2a-86dd-eaeee0301fa0 | -7.48568 | -40.59777 | 2024-10-13 03:21:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85e7072d-a2c8-34b2-9530-a53ca81a379c | -7.38997 | -39.1402 | 2024-10-13 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08f47e47-4f4a-3287-8ab6-b816442ca9cc | -7.3894 | -39.14328 | 2024-10-13 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8293985d-410f-35f0-b68a-c2ce7da2bc4d | -7.38857 | -39.14159 | 2024-10-13 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
