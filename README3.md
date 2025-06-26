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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e28fa7fa-2285-38e3-a541-c524fad1bf4b | -11.07321 | -55.38497 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| bf327af8-4b69-3eaa-b848-4198fe3e8f87 | -11.80829 | -57.35633 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 317119cb-b37c-3277-b688-2c2d63227731 | -11.92053 | -54.8152 | 2025-06-26 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e434c8b0-f30f-3fc5-9bfc-b548df78008a | -12.61915 | -57.88105 | 2025-06-26 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4da6a35f-99e2-3f8d-b6df-01aecd37bcd6 | -11.35786 | -48.70667 | 2025-06-26 01:20:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| e7cfee10-8211-32b5-9c04-495e55bb8625 | -11.07225 | -55.36714 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7a79463c-f983-3809-9e96-0c3709c93fbf | -11.0683 | -55.07291 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d42cb0f5-90cd-3733-ad41-80ead7eabc00 | -11.83187 | -51.25762 | 2025-06-26 01:20:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b3380c0b-4dc3-39d6-92d6-a7c9b9897290 | -11.36745 | -48.71007 | 2025-06-26 01:20:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 336e66d7-546a-3e06-bafe-9958966a56e3 | -10.5067 | -53.59173 | 2025-06-26 01:22:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0dad3c52-9173-381f-bf97-f018b7880752 | -9.11235 | -49.45374 | 2025-06-26 01:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7aa59038-1c25-31b3-9fc3-d46c7a81f16e | -9.51916 | -56.10603 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 7a355893-2362-39c0-a652-29b967234e9b | -10.29365 | -57.14016 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5d5856b2-1933-3a67-b64b-a4a0f242a5ac | -9.25376 | -63.28698 | 2025-06-26 01:22:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 647749d4-8c52-38fa-a997-69aeb22c83ff | -9.79019 | -57.42423 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4a5f5cd-765a-3b8c-a16f-5022e5f5cc23 | -9.50954 | -56.10745 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 70cefd56-82a5-3df5-b3e5-74683c8198bc | -8.76328 | -63.75503 | 2025-06-26 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d07eb698-8b11-3461-a227-eb9b7fe73da6 | -8.72276 | -64.15897 | 2025-06-26 01:22:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 63467ac2-c1a6-3773-8c9f-0defbf6816fc | -10.87505 | -56.44878 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b2ca9431-951f-3bd9-a7f3-5a9ff1f98a7d | -10.30272 | -57.1388 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 451adc3d-4f8e-3fd7-8171-ea7b33319c5d | -10.2923 | -57.13065 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8baff6f7-2c55-3849-bacf-a929e5a5b569 | -9.12007 | -49.44711 | 2025-06-26 01:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 55f4013b-e3ea-3e36-ba32-3676a12e5626 | -10.71048 | -59.12707 | 2025-06-26 01:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef2ec3f6-2220-3655-af35-e1157a46e3da | -9.1284 | -49.45095 | 2025-06-26 01:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 015420ae-2197-37a5-8955-ab89d4b75455 | -9.5207 | -56.11666 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9852668b-a78e-3060-ba7f-f4a998b17226 | -9.508 | -56.09678 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ee2f2bbb-8792-376d-95d5-f62b5766d373 | -9.49838 | -56.09822 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 24478052-2d6f-39c9-97a5-3130cd9517c3 | -9.51109 | -56.1181 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a8e56fd4-8f9d-37de-89b0-3d9fa283ffa8 | -10.30137 | -57.12935 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 15a19a94-373b-3f83-afc0-7734ad2cd1c3 | -10.71171 | -59.13608 | 2025-06-26 01:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84ad8d6b-f30a-323a-8b9a-1a7839f7da57 | -9.49683 | -56.08755 | 2025-06-26 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 07530200-e2c6-3df5-9eb4-ec2e10792995 | -10.87652 | -56.45879 | 2025-06-26 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f8f1ee8a-5ca3-3891-b3de-49eecae98d86 | -6.1977 | -48.0699 | 2025-06-26 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5b3df5fb-c607-324a-b962-c7a36a9f5b6a | -9.1213 | -49.4313 | 2025-06-26 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6ad02f05-621f-35ae-9fcf-9575e48207f3 | -11.0705 | -46.6447 | 2025-06-26 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8109c9ab-bdf9-32c7-989a-54b29e058a32 | -6.3687 | -43.7525 | 2025-06-26 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e55a4c0b-0215-385d-84bd-0647cf1eb9cb | -13.0408 | -48.825 | 2025-06-26 01:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d74e8539-8b54-3121-b825-8884a82b9cc3 | -4.5242 | -48.0377 | 2025-06-26 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 15b499de-26e5-3f56-bc92-da36bbe186a5 | -6.1789 | -48.0929 | 2025-06-26 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 710f6401-a80d-37e8-8ab9-1e0480936e50 | -9.4993 | -56.0988 | 2025-06-26 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8ad12c9c-e4f8-30bb-8866-2d036b4db95a | -6.1604 | -48.0724 | 2025-06-26 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| df1b5975-2693-3d75-9992-3a3b6409f428 | -9.121 | -49.4528 | 2025-06-26 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| da30768b-86db-3161-855a-87d3692f5f7e | -9.518 | -56.0975 | 2025-06-26 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 61372339-e781-3bc1-bc8e-5be4237bffb3 | -11.0644 | -55.3757 | 2025-06-26 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 46f8a341-3008-3586-bde4-dbf4d391c29d | -6.1791 | -48.0712 | 2025-06-26 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 19dce4d5-a3b0-38b6-a99e-bc39ab13498e | -4.524 | -48.0593 | 2025-06-26 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| de4b02d1-6cee-3688-b1b8-1d5d8c053223 | -6.1975 | -48.0916 | 2025-06-26 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1b3b5caf-993c-35ae-8732-b4c47bd63421 | -11.0832 | -55.3741 | 2025-06-26 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| b96d1bd6-b4ab-3ec1-af60-43cf0d18f976 | -9.121 | -49.4528 | 2025-06-26 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f5bf6e6e-e5e6-3047-a743-042c503b488e | -6.3687 | -43.7525 | 2025-06-26 01:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 0c832e18-928c-39b7-8447-60a97ebd0d7b | -9.4993 | -56.0988 | 2025-06-26 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 04ed2c83-cd17-334e-ad84-5592977fce81 | -4.524 | -48.0593 | 2025-06-26 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 99f141de-5453-3141-995b-a08dd0b4a8c7 | -4.5242 | -48.0377 | 2025-06-26 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 949a2ed8-96da-37cb-821c-958129d86440 | -11.0832 | -55.3741 | 2025-06-26 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 4159a7d5-d1ca-345d-b247-6ec681601d02 | -9.518 | -56.0975 | 2025-06-26 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e47dc7ea-2379-3a7b-9df7-d30659c17140 | -6.1977 | -48.0699 | 2025-06-26 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| db69c9bd-b7fc-35f7-a097-2242bdbf8539 | -9.1213 | -49.4313 | 2025-06-26 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 591a969a-0d43-3d6a-ab84-8d817f3e5113 | -11.0644 | -55.3757 | 2025-06-26 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5dd1e6c7-2ed4-3c84-82b8-2142347d24d4 | -6.1791 | -48.0712 | 2025-06-26 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 539891b9-dfba-3624-b2d3-5faf9698b449 | -6.1789 | -48.0929 | 2025-06-26 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 3c35d29f-5d13-3ee4-9032-6a6603de58e4 | -6.1604 | -48.0724 | 2025-06-26 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 54afacfc-da3a-3d5e-a218-2d034533bd5e | -6.1977 | -48.0699 | 2025-06-26 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3e0d519f-d2c3-3492-901a-4d6db8529a46 | -6.1789 | -48.0929 | 2025-06-26 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 752aec54-2356-3ad3-a170-0b28ae5ccdd1 | -11.0832 | -55.3741 | 2025-06-26 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fc2366d0-1733-3ed8-ac0a-d31afd1e403f | -6.1791 | -48.0712 | 2025-06-26 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 209.2 |
| f3d44981-398f-33ad-9b3d-5bfdb00a6b92 | -9.1213 | -49.4313 | 2025-06-26 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b1698c40-09a2-3235-9a0b-b6d20f5c98c3 | -9.121 | -49.4528 | 2025-06-26 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 75d1361a-925b-3b32-85ec-f409adee53a6 | -9.518 | -56.0975 | 2025-06-26 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8f670e8d-39a4-3dab-8633-aa8401a122e9 | -9.4993 | -56.0988 | 2025-06-26 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a1a36cd8-8ad0-3242-8124-76f40ae525f2 | -11.0644 | -55.3757 | 2025-06-26 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a448069c-6de9-3eec-ab02-b6d92a9b7504 | -6.1791 | -48.0712 | 2025-06-26 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 58b01378-cca7-39ec-be78-0187d9e7363c | -6.1977 | -48.0699 | 2025-06-26 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ae72da1f-9c27-31a2-8bfc-5e5122b66d53 | -6.3687 | -43.7525 | 2025-06-26 02:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 94a1ac2d-3706-35e1-840b-098324e90d2a | -9.518 | -56.0975 | 2025-06-26 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e1549cc8-acf3-3aec-8fbf-de638e94f24c | -7.2028 | -43.0936 | 2025-06-26 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| b1a6c6a7-089d-3c89-aa6b-05d591e267b5 | -11.0644 | -55.3757 | 2025-06-26 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8a2be220-367c-3d0f-9adb-28f7a0f97ab6 | -6.1789 | -48.0929 | 2025-06-26 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 07bb170e-7cc3-304c-aa60-9537ff14353d | -9.4993 | -56.0988 | 2025-06-26 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 13993730-28fb-345a-93b9-0641e938ff6f | -9.1213 | -49.4313 | 2025-06-26 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 56c16456-7f27-3df3-baf2-94ad89a7863c | -9.121 | -49.4528 | 2025-06-26 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3442fe73-1c18-306d-a6f1-13007690c214 | -6.1791 | -48.0712 | 2025-06-26 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| a307006e-8b7a-3918-80e2-67b495280f2e | -11.0644 | -55.3757 | 2025-06-26 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 819c7f4a-cf67-368e-a44d-940483aa7537 | -6.1789 | -48.0929 | 2025-06-26 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5e39e2a0-b926-3cc7-a09e-1631c24d03bc | -9.121 | -49.4528 | 2025-06-26 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b18f8ddc-7fe4-3406-9c55-85eb61cf7fde | -9.1213 | -49.4313 | 2025-06-26 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b545b91d-f803-31ba-827c-8a07a8138f50 | -6.1977 | -48.0699 | 2025-06-26 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4e29f41e-4819-3d66-979a-1f35bd10f64c | -9.4993 | -56.0988 | 2025-06-26 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f4f18165-719e-3ee6-a48d-5e7f6090e82a | -9.1213 | -49.4313 | 2025-06-26 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| def71cfd-fd05-3f6b-9b67-67d058aa51f4 | -9.121 | -49.4528 | 2025-06-26 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 842279bf-587a-340b-a2b0-2abfbe0c832a | -9.4993 | -56.0988 | 2025-06-26 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f97eecff-9629-34be-a042-74cf85c3b99e | -6.1789 | -48.0929 | 2025-06-26 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 97e313a4-491b-3e89-a019-5fe41c02729c | -6.1791 | -48.0712 | 2025-06-26 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 4ceee73d-830b-311c-aa2f-4638fec9a9b6 | -11.0644 | -55.3757 | 2025-06-26 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 611ea1e3-45f4-3113-a5ca-29499b650ab0 | -11.0644 | -55.3757 | 2025-06-26 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fc1eb044-abae-32ab-9526-a59b7c387a9c | -9.4993 | -56.0988 | 2025-06-26 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3f1ca6a4-6521-39fb-8553-f0fe613b1f1e | -21.3268 | -49.0368 | 2025-06-26 02:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 2c41630d-3411-3987-8a0a-799aefcda0dc | -6.1977 | -48.0699 | 2025-06-26 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d16f4cab-d553-31d6-89b1-817fb801719f | -6.1789 | -48.0929 | 2025-06-26 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f8591a9e-4b6c-300a-8f73-467b49e3e850 | -9.1213 | -49.4313 | 2025-06-26 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| cf596833-b5a4-3136-af70-da3b900efedb | -6.1791 | -48.0712 | 2025-06-26 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |


[Clique aqui para ver as próximas entradas](README4.md)
