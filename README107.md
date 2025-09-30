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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e5cf71f-2282-3995-8a90-62ef04aba745 | -14.70891 | -48.1532 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 57f44e1b-be3b-3c46-8c9e-28a8593156fe | -14.51738 | -48.46758 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c88e67f8-0d5f-3c3b-8142-11aaf65a1f22 | -13.21364 | -47.30832 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 65ca2b04-bc9b-3356-8d6f-aedeec4d0d4d | 4.15513 | -60.01684 | 2025-09-30 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 003b6ad6-408f-32be-ae6e-437bb96844cd | 4.15424 | -60.01158 | 2025-09-30 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c13f5a-8254-3580-a92e-148e88cbd7c3 | -17.70022 | -46.65949 | 2025-09-30 06:18:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 409efcce-4913-3651-b971-83bcc5598e48 | -18.21117 | -53.30258 | 2025-09-30 06:18:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d151457a-d3d5-3abd-974f-235d56579b7a | -17.89845 | -57.5823 | 2025-09-30 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| eb6ffb3e-0d33-36ec-96bf-7081dbc86d49 | -17.38453 | -47.13333 | 2025-09-30 06:18:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 89647afa-ff74-3c1c-8363-5ff68bd929ef | -15.88093 | -52.26799 | 2025-09-30 06:18:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 745c97ee-f6fa-3448-966b-37eedf5d227c | -17.88132 | -57.62032 | 2025-09-30 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d64e2119-a491-3db5-97ef-b5ae597ba477 | -18.18806 | -53.33665 | 2025-09-30 06:18:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4d009e8-3ccb-3702-aaa4-48f2e812c3be | -17.90878 | -57.58375 | 2025-09-30 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| a7f86f54-b037-37c5-8cbd-1474ba767d17 | -18.16523 | -53.29812 | 2025-09-30 06:18:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ac565252-fb34-3938-9def-33d80ad28a65 | -18.1625 | -53.31657 | 2025-09-30 06:18:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3a8b2eec-b36c-394d-a7a9-9cbb7e86bb39 | -18.20235 | -53.3011 | 2025-09-30 06:18:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 87d963bb-eb30-313d-8613-f4939ac71614 | -22.08147 | -55.97112 | 2025-09-30 06:20:00 | AQUA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35dc1787-9711-34bd-b606-f6251956538e | -22.08303 | -55.9612 | 2025-09-30 06:20:00 | AQUA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 425d0599-b19f-3009-8b7f-ed3e2ed60cee | -7.0096 | -71.6211 | 2025-09-30 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c94d4369-2bb2-3da0-8615-78f03ea99657 | -8.47884 | -72.79565 | 2025-09-30 06:20:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9cb770f-4520-3c46-a470-9ce16ab78812 | -6.93733 | -71.50151 | 2025-09-30 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fdf631a-c164-3872-8310-fb47d9274e28 | -6.941 | -71.50206 | 2025-09-30 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b7cd8f-9a6e-3c8f-be0a-f57f5bc97732 | -15.2598 | -56.7965 | 2025-09-30 07:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8733d095-c645-386f-b918-aebad1d79544 | -14.5141 | -48.4299 | 2025-09-30 07:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 16542a15-73ee-3eb2-82e5-be8e37ca8d71 | -14.5137 | -48.4522 | 2025-09-30 07:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3af9e3ac-6f6a-3601-b144-0f86f3fc37b4 | -11.1546 | -54.126 | 2025-09-30 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3c58e0b1-bf80-3054-9b94-266c0c1e2bff | -14.5327 | -48.4715 | 2025-09-30 07:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 766af1c9-9ca5-346b-97e2-087e31589d0e | -14.5522 | -48.4684 | 2025-09-30 07:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 28c77bd7-9a89-3d81-bb27-9dc465bb3b7c | -14.5327 | -48.4715 | 2025-09-30 07:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b6f30f04-3d8a-330f-ad4a-998808a0d5cd | -14.5137 | -48.4522 | 2025-09-30 07:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7c2efcfb-1803-3471-94a4-8b6122427f44 | -14.5517 | -48.4907 | 2025-09-30 07:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 66c42613-ccb9-3edf-8da2-96161c0a2f14 | -11.1546 | -54.126 | 2025-09-30 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4b88c656-a6fd-319b-b9d3-0406dafc3213 | -14.5517 | -48.4907 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5977114c-1c4c-3e3f-804c-3c0bbca32074 | -14.5522 | -48.4684 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2a8a4cb3-889c-3bd6-ab79-0390a33895e3 | -14.5323 | -48.4938 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b1c9624a-c899-3cf1-90ea-70e0f9e159c2 | -11.1546 | -54.126 | 2025-09-30 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 80351278-f17a-3048-a2f1-d49cae490e78 | -14.5137 | -48.4522 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 240266a7-4434-3550-9eb3-7b77233a8fd5 | -14.5141 | -48.4299 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7423161d-e0dd-3484-af99-463c9f4cd141 | -14.5327 | -48.4715 | 2025-09-30 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ac0ba99d-e7a9-35a1-950b-2af6017be75a | -14.2849 | -57.7045 | 2025-09-30 08:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2ccc704b-f34a-3644-9a5a-b2ebb34b8a82 | -14.5327 | -48.4715 | 2025-09-30 08:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e4bf1c46-57af-3d7b-90c5-a7989c668f51 | -11.1546 | -54.126 | 2025-09-30 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8c580995-af37-35c7-82c4-cd2d4977997e | -14.5137 | -48.4522 | 2025-09-30 08:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| eb93e939-58ab-3730-8ee7-d06c1974d0a0 | -14.2849 | -57.7045 | 2025-09-30 08:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8947294c-700e-3b69-8ebc-625d553b5e2b | -14.5137 | -48.4522 | 2025-09-30 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e3278cca-c30f-311b-a500-ddc33e7ed02c | -14.5133 | -48.4745 | 2025-09-30 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 81973529-d5d9-35cd-b429-ebc38eb13563 | -14.5327 | -48.4715 | 2025-09-30 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c7940038-2696-34c8-b72f-c2103a530d02 | -11.1546 | -54.126 | 2025-09-30 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| eda60ab1-840a-35ed-a7f8-8003ccdf47b3 | -14.5323 | -48.4938 | 2025-09-30 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ed494d2a-5994-3e7e-9d43-4f48a7ff9f91 | -14.5327 | -48.4715 | 2025-09-30 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 146.9 |
| e9ec5aa9-0034-39bd-a51f-bef0790d494b | -14.5137 | -48.4522 | 2025-09-30 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| d7af0549-a4a6-3813-a3f6-0a3b54b13737 | -14.5323 | -48.4938 | 2025-09-30 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9d516aee-9a11-3488-958e-f7ed6dbe4df5 | -14.2849 | -57.7045 | 2025-09-30 08:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1e4fd4fa-d347-3cd0-bd5c-2d5524fc6c54 | -14.5133 | -48.4745 | 2025-09-30 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c62e0247-65e4-3e59-8305-c93f0321f54a | -11.1546 | -54.126 | 2025-09-30 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fa831899-21e6-3b0e-8d16-8bd93a63148b | -14.2849 | -57.7045 | 2025-09-30 08:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e1dffcbb-6423-3154-a857-35e4a5ee8597 | -11.1546 | -54.126 | 2025-09-30 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1def96cb-4812-359a-896b-5776f53d8a18 | -11.1546 | -54.126 | 2025-09-30 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d34dcaee-9eea-374d-9bc2-a6fdba20308d | -14.5137 | -48.4522 | 2025-09-30 09:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a44d7140-a734-3470-a31a-85ff6bc40a1f | -14.5327 | -48.4715 | 2025-09-30 09:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 43a1d48a-b5e0-3f2d-b214-26b7f75193c6 | -14.5137 | -48.4522 | 2025-09-30 09:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 67ce7a93-62dd-3fe8-a924-b1603c3ba8a9 | -14.5133 | -48.4745 | 2025-09-30 09:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 72890e1c-7332-32fb-a1f7-443da76241b5 | -10.9582 | -46.5242 | 2025-09-30 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 23639b84-958b-3f38-a5fb-3739b18a5935 | -12.2344 | -47.8086 | 2025-09-30 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8129cf3f-c5f9-3f26-8cda-faa4badce349 | -10.9582 | -46.5242 | 2025-09-30 10:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| e49e79c5-4cf6-325f-9fb7-e891dd1d291c | -12.2344 | -47.8086 | 2025-09-30 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 86fbc912-81dc-3c32-82e8-ac6cd6cf765e | -14.5323 | -48.4938 | 2025-09-30 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ffc7943b-d1ae-3620-99e5-e3f460270a26 | -11.7537 | -46.8461 | 2025-09-30 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cf83b76b-29b5-3471-ae01-17e28ba52e13 | -12.2344 | -47.8086 | 2025-09-30 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| ed599b22-ab24-3d74-a022-4191d8921057 | -11.1753 | -47.2358 | 2025-09-30 10:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6d3fe5fa-3c50-3a3b-b1d9-c98270080b71 | -14.5327 | -48.4715 | 2025-09-30 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| cb2f166d-fb38-3e02-bbcb-9bc2a551dd36 | -14.5133 | -48.4745 | 2025-09-30 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a37016d0-9710-3500-9422-8bc509931223 | -8.8732 | -46.6762 | 2025-09-30 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 53b1dfe3-75f2-34b1-8754-18555c5ee4c5 | -14.5327 | -48.4715 | 2025-09-30 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9735bea6-b8a7-3ce6-b88c-492186beb704 | -14.6603 | -46.9663 | 2025-09-30 11:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f2221fd6-8764-3b4b-9a80-fc9bb481483c | -10.9586 | -46.5016 | 2025-09-30 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 406f47e3-6289-36d0-b4ab-ab0f2f480229 | -8.8732 | -46.6762 | 2025-09-30 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 87737ae8-1384-34c4-a192-ec9472d9cd4f | -14.5327 | -48.4715 | 2025-09-30 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6fa0cb10-1942-388f-9e5b-c4dad84a61a4 | -14.6603 | -46.9663 | 2025-09-30 11:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2b3c2388-a306-3182-b985-9e7596f33c4c | -8.672 | -47.7144 | 2025-09-30 11:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| db80954a-5f75-3060-bfbb-59ef62d44d4c | -10.823 | -46.6538 | 2025-09-30 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d91b92d5-1d31-3849-9c92-de4cf6d4b452 | -14.5323 | -48.4938 | 2025-09-30 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0a376925-bc91-3a9e-ac37-f91fa78c54be | -8.5407 | -44.6745 | 2025-09-30 11:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ebda7d43-3d1d-3e34-bc2f-50973276eb9d | -8.8732 | -46.6762 | 2025-09-30 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8f219b6b-bb6f-37a5-9059-b4d3cadefe38 | -14.6603 | -46.9663 | 2025-09-30 11:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 138.1 |
| c9c0600e-c2c2-3178-b463-8490caa3ed6f | -8.8734 | -46.6539 | 2025-09-30 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0b689a77-9f35-30e4-8419-b8e89e00e9ba | -10.8227 | -46.6763 | 2025-09-30 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 33f14444-9a22-3074-99fb-684b5ce1668f | -8.541 | -44.6515 | 2025-09-30 11:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 591f5573-7932-3e78-8c0e-c47e05b14d8f | -8.8549 | -46.6335 | 2025-09-30 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f782afde-7ced-33d9-a7ae-cf45c0dc2deb | -8.8546 | -46.6558 | 2025-09-30 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4238de70-05e6-302a-b1f8-f17b62342bd9 | -14.5141 | -48.4299 | 2025-09-30 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 76cd085f-1f56-3c73-8ab0-0dbfa1090945 | -10.823 | -46.6538 | 2025-09-30 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 7a42ac6a-3173-381c-bb61-040051e4bc77 | -10.8417 | -46.6739 | 2025-09-30 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 51864672-a80c-3fb0-aa23-8633f36aa8b9 | -10.823 | -46.6538 | 2025-09-30 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 24a97448-8470-3a39-8379-7913eaf283f7 | -10.1045 | -47.7851 | 2025-09-30 11:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 773e5955-db20-35f5-aaa5-6bcb51676372 | -11.1546 | -54.126 | 2025-09-30 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 64eea465-f6d4-3a7d-a133-1e4d36ce06de | -11.2138 | -47.2086 | 2025-09-30 11:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c7a6c30f-7785-3822-a9e5-aa98a913e14f | -14.5141 | -48.4299 | 2025-09-30 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| df20a5a0-d942-3b9f-b0c9-5539cfa57f82 | -15.9273 | -46.2101 | 2025-09-30 11:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fe120663-9b37-3907-a7f6-7ad0decfb8e9 | -12.6829 | -45.2746 | 2025-09-30 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |


[Clique aqui para ver as próximas entradas](README108.md)
