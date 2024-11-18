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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5095f340-1757-32ee-b078-8dfce83d2679 | -1.6962 | -45.8087 | 2024-11-18 01:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| aba2b2c9-3326-39c3-a1f2-50c495d35200 | -1.3148 | -51.7202 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a1138faa-2578-392d-94a1-b310b38b7e67 | -1.7147 | -45.8307 | 2024-11-18 01:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 157.3 |
| e9174172-3958-3426-aafb-141c1ab21080 | -1.6962 | -45.8311 | 2024-11-18 01:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 60d2e6d6-1c49-34f2-90da-5954e5cef9e1 | -2.5846 | -51.7387 | 2024-11-18 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b39d3a0b-d221-3908-8412-3a60cdfe09b3 | -2.7659 | -52.6163 | 2024-11-18 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c8433184-44fb-359d-8021-618e89e31cef | -6.5216 | -35.194 | 2024-11-18 01:30:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 210.6 |
| f616ca43-b260-39d9-8d56-5357121adda6 | -3.3267 | -50.4923 | 2024-11-18 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 53208db5-0eec-3b5f-9436-6d743c10ad03 | -16.08261 | -60.09716 | 2024-11-18 01:38:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c9fc731-a653-3afd-a024-ffb9adff1924 | -16.07347 | -60.09849 | 2024-11-18 01:38:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 90050892-3cc9-3a6e-ac67-ee27f968b9a4 | -18.72814 | -55.57461 | 2024-11-18 01:38:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b011532b-8aeb-3ebf-a9ef-990ae3dabea0 | -15.67498 | -59.73077 | 2024-11-18 01:38:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 594d4b9f-c14e-3793-8431-429c04a26330 | -15.6737 | -59.72132 | 2024-11-18 01:38:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b85e14d-8cbe-38dc-90db-50902dd6492e | -15.6542 | -59.84984 | 2024-11-18 01:38:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0c9f048b-241a-3a18-a284-0b5dec164e68 | -1.7585 | -50.7398 | 2024-11-18 01:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| daed637d-ec89-3820-83cd-d0af8abebb22 | -1.6962 | -45.8311 | 2024-11-18 01:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 160.2 |
| d8dd3f81-2cb7-3353-986b-072d2ca8aeeb | -1.3148 | -51.7614 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 5fe39070-83c4-3db9-abb3-2543b8c17127 | -3.3452 | -50.4917 | 2024-11-18 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6cf20f1d-af13-3efd-a4d6-45a761cd8da6 | -1.6962 | -45.8087 | 2024-11-18 01:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 43bc2dee-809c-3c0b-9cdb-adefbf56ec93 | -1.3148 | -51.7408 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 266.3 |
| 7b5ac8c9-b572-3e79-91a5-bf11448e9701 | -14.286 | -57.624 | 2024-11-18 01:40:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 5bf69b64-7e93-3e10-8055-fb0f1bbb7278 | -1.7147 | -45.853 | 2024-11-18 01:40:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 294a8071-f678-3650-bbf2-3412a39728ee | -3.1454 | -45.4753 | 2024-11-18 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 07411ab7-8518-399d-ab13-473534ec87fe | -2.7659 | -52.6163 | 2024-11-18 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8753561a-25a8-3a27-8dc7-4cf7f6add00c | -2.5847 | -51.7181 | 2024-11-18 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9bd4a488-a136-3991-9bd6-951dd97ce3e2 | -1.2964 | -51.7616 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| bb6bb6e2-0fa0-3b45-9289-e27ae3f3f8b3 | -3.0542 | -54.4081 | 2024-11-18 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9f615cb2-4f3b-3917-90c6-b5b51f487c89 | -2.8608 | -51.7731 | 2024-11-18 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 98fe28a2-80f5-31d9-b148-9c7845428ffe | -2.8791 | -51.7932 | 2024-11-18 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8fb80c4f-7fcf-3426-9e96-2159971a0102 | -3.1455 | -45.4528 | 2024-11-18 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 5c726fc4-d19c-34fd-884d-e3482d1359c4 | -1.3148 | -51.7202 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dcd7ad92-c09f-34aa-bb3f-0b04f092365c | -4.9059 | -44.022 | 2024-11-18 01:40:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 22e61d0a-39fc-39fb-982e-0d6c074f21b2 | -1.2964 | -51.7204 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| cbf7ee6e-2c76-3174-b1d7-c486b7a27da5 | -1.7147 | -45.8307 | 2024-11-18 01:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 14f05114-ea82-3262-8afd-b33b436cae41 | -1.2964 | -51.741 | 2024-11-18 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 4ecefe16-1404-3a05-b953-b65b531ff117 | -1.7148 | -45.8084 | 2024-11-18 01:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| fd870ebe-4700-33c0-8373-e8e96ff95563 | 0.966 | -51.1452 | 2024-11-18 01:40:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9db67d84-5959-38d1-9a65-abee6d025076 | -2.8607 | -51.7937 | 2024-11-18 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| bfa25069-39ef-32e6-b433-cf63bdc8d5c9 | -13.22307 | -54.16511 | 2024-11-18 01:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ef1c506e-d6be-3c40-abda-17068a1d9c95 | -13.01765 | -56.45246 | 2024-11-18 01:41:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f3f73f41-7f80-3ced-895a-47d4c361f54f | -12.5725 | -57.76851 | 2024-11-18 01:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1dcce2f4-8b13-3a56-848e-ccc3e7021ed2 | -13.02299 | -56.46763 | 2024-11-18 01:41:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d92bb37c-f759-37c1-947b-e0285ffc5cfc | -13.01926 | -56.46342 | 2024-11-18 01:41:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 3bda9ebd-8d90-3eb8-bf28-4c1926cf11f2 | -12.4213 | -57.8041 | 2024-11-18 01:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19fe5a53-5350-3c56-87c2-d2318fa3e982 | -14.54696 | -59.95869 | 2024-11-18 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34ea40ca-9ce4-32ca-b350-322456ee0d9d | -12.55263 | -57.81671 | 2024-11-18 01:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 22172d76-542d-33e7-8c6d-ec139edd2764 | -14.28535 | -57.62726 | 2024-11-18 01:41:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a7cf415a-3a9b-37f4-bfc2-398f33723d2b | -14.88315 | -60.06487 | 2024-11-18 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07f69d21-051f-3cf0-ab24-37c465ae638f | -12.55401 | -57.82627 | 2024-11-18 01:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 89505f23-db0e-39fa-bccc-8f11496004aa | -14.28809 | -57.64633 | 2024-11-18 01:41:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad2a6708-9350-323a-9c07-c811c435e4aa | -11.37099 | -55.12949 | 2024-11-18 01:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 360bb965-d6f4-332a-9779-74c7a605c5b1 | -14.28673 | -57.63682 | 2024-11-18 01:41:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a62d1ed4-4b5e-3885-b4fa-c71004e9ab04 | -13.02132 | -56.45672 | 2024-11-18 01:41:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a9d995bb-2b88-3b20-b083-4ed41baba01d | -12.57392 | -57.77813 | 2024-11-18 01:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9203a2cc-a47d-3cd9-a22d-2f6467906bd3 | -13.22126 | -54.15881 | 2024-11-18 01:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1730c4e5-cf02-3033-a4bb-92120f10d66f | -3.06146 | -54.41463 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 362e3ba3-6b83-374c-ad83-3f98941b3c5c | -1.44352 | -53.39599 | 2024-11-18 01:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ad46e274-b668-3268-a467-c0b22e77518d | -3.06979 | -53.2729 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 51cd6d99-4155-35b9-838b-94b7d0fac4d4 | -1.30246 | -51.75687 | 2024-11-18 01:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 362.8 |
| eb184824-94c0-32b8-8503-3c4f0e4d1320 | -2.20185 | -53.67313 | 2024-11-18 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| ae34a6a9-89d7-375d-9638-98b8533ddfc1 | -2.19987 | -53.679 | 2024-11-18 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 20c4aa9c-685c-35de-94c1-75e72cb21a6d | -2.58516 | -51.70634 | 2024-11-18 01:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3777cf3b-8e4f-316f-bd44-9a78fa8ab3af | -2.66188 | -51.72488 | 2024-11-18 01:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 1ef1a4ac-b28d-3512-976c-a2995562a5c7 | -2.86506 | -51.82253 | 2024-11-18 01:43:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| de85af26-21c0-3f78-8f8d-b384dcce018d | -3.08352 | -54.64999 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e95b52d3-40a3-3fd3-a18e-dfa16ca7fc5d | -3.06314 | -54.39738 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e4e9c69c-7ca3-3f0d-bda0-f657ae2c3b8d | -3.08668 | -54.67078 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 2226798d-3c41-3876-9c8d-bf2c342475ca | -3.04805 | -54.4165 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 4dd14aa3-157e-3b83-a6c2-5847ba46906b | -3.10836 | -53.11585 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e5421504-ee66-33a8-90b7-9894bfd20e8d | -3.18824 | -53.24306 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ecb8c8e5-4146-3807-8e00-e8ddce617826 | -3.07032 | -53.26756 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 9b123001-06f0-325b-96ce-5d9deecde400 | -3.0581 | -54.39238 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 48b5d510-feb0-3a0d-987b-6e13b051c888 | -1.30572 | -51.7495 | 2024-11-18 01:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 444.9 |
| 871be206-a710-3b5e-9607-0237ce131742 | -1.44463 | -53.40131 | 2024-11-18 01:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 1586e80e-bd7d-38bc-b1dc-784014d3de37 | -1.44069 | -53.37342 | 2024-11-18 01:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 6d7ac58e-2398-33a0-9652-5b9089955aad | -2.59538 | -51.73515 | 2024-11-18 01:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| e385959d-8475-3bc6-afc4-3e8a64eec96b | -3.31117 | -53.35417 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| aeb12d7d-0042-35f8-afdb-653879d00084 | -1.61711 | -52.61634 | 2024-11-18 01:43:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 95af10b7-8df2-3fd7-9a64-3896ed7e745f | -3.04975 | -54.39954 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| b1e95675-7f8d-3127-957d-74e6f4561087 | -3.08951 | -54.67612 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 70264553-1d44-32d5-9313-f78eecea33bf | -2.57875 | -51.73769 | 2024-11-18 01:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e31f9131-5a15-3aa6-836e-9ce117f89c7e | -2.76192 | -52.6288 | 2024-11-18 01:43:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1e2c25df-373b-3614-8347-5aac241840f4 | -1.28875 | -51.75202 | 2024-11-18 01:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a9b2141b-b581-3952-a625-14f82087e159 | -3.0447 | -54.39451 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| fe6b6bba-407e-34db-815d-7ffeadc42e5f | -1.29702 | -51.71864 | 2024-11-18 01:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| a04115e1-ada8-3a1a-9aaf-88ca47a16789 | -3.58035 | -53.73883 | 2024-11-18 01:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| bc807263-7d40-3ba9-a3f6-7a13265e59ae | -3.57685 | -53.71497 | 2024-11-18 01:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 7f1e7f9a-dfb5-3cdb-875f-85303445a560 | -3.07375 | -53.30016 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ea79a430-dfb0-383d-829a-e096849767ab | -1.30002 | -51.71127 | 2024-11-18 01:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b7901078-d3b1-3485-ba87-b5128a168647 | -2.7574 | -52.59821 | 2024-11-18 01:43:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 5ddbe4c2-89db-3582-a812-f7d1b42182dc | -3.70781 | -61.27328 | 2024-11-18 01:43:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cfe408ea-9b49-3f5e-a33a-101903ba54e4 | -2.8704 | -51.79079 | 2024-11-18 01:43:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 0dd4f283-799d-3404-ad1d-8f001631af81 | -3.08652 | -54.65531 | 2024-11-18 01:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ccab8f10-28ed-3339-bf62-a02a74cf6767 | -3.10408 | -53.08835 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0d4aa8d9-e716-3374-9acc-c5f62505c7d0 | -3.58519 | -53.73196 | 2024-11-18 01:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2ef47f3c-f731-3faa-9706-1077d391379e | -3.07447 | -53.29468 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| fa497cbb-b32d-3e5f-ba36-5942435d2ece | -2.59041 | -51.74268 | 2024-11-18 01:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 89879d98-22ed-36c4-9f4c-5b7fc30a7a62 | -2.85966 | -51.78729 | 2024-11-18 01:43:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 93a0b4d5-7bb5-340f-a348-7667cca0d6a0 | -3.10479 | -53.09499 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| cd8d9dcb-3dc8-3401-b17b-3d89f578438a | -1.43939 | -53.36828 | 2024-11-18 01:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |


[Clique aqui para ver as próximas entradas](README12.md)
