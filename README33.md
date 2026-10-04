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
| 661f74ed-f954-3020-a725-a30252b14794 | -7.74994 | -49.20296 | 2026-10-04 04:21:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d8f2a2-14df-380e-9522-ca2d7750fee9 | -10.38584 | -45.14914 | 2026-10-04 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 660aaf8e-e6e4-3d67-92e8-c3b9f69648b9 | -10.25578 | -49.6639 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b05018f5-1e50-3ca6-ab81-31bfda1da4b3 | -12.35252 | -48.04001 | 2026-10-04 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d0f530b-5840-3a93-8fd9-5c9084e0c66d | -10.99221 | -59.15046 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31af1811-e320-39b1-83bf-47d243a49e60 | -10.70315 | -44.20036 | 2026-10-04 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a382c1b2-d2fb-345e-91ea-fa90d0a9614b | -8.32776 | -51.31408 | 2026-10-04 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681fcc04-3558-32a4-9558-3c1ed71cfcd9 | -9.70024 | -57.44929 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c692274e-4ae8-3826-acc1-f6b2f0c239c1 | -9.51726 | -54.6305 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d85b6f9-0376-3f9c-8736-d555a9ffedf6 | -10.24375 | -49.65845 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b634c0f5-5f5e-3a2f-aa4f-71b42f48a528 | -10.24084 | -49.66132 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 488702a9-8118-386f-aafc-fad4cd73166e | -10.99353 | -59.14411 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 43416e55-a9df-3921-b10f-7ca06e1e7458 | -10.24001 | -49.65783 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2cebf23-eccd-39df-bdae-0c9785e71930 | -10.24748 | -49.65909 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 495ca810-7198-326d-a1f8-c6c4492e31c9 | -10.24613 | -49.65287 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 635de630-2d18-3bf6-8ec2-d5ff5d5e7b7c | -9.51265 | -54.62621 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d06e8b0-f213-3f48-bd10-f85db8d5614b | -13.37773 | -41.3463 | 2026-10-04 04:21:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 260c9311-568e-317a-8aca-4efccc44e342 | -9.50619 | -54.63192 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d20a73ce-0fd9-3a4c-942e-a9a71cfaff79 | -12.20425 | -57.12027 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c68fbe-92f7-3f5e-abe6-cb9981786785 | -8.80026 | -48.6455 | 2026-10-04 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b85f3405-556e-327e-8dd8-0009399bd6d1 | -15.91315 | -56.34235 | 2026-10-04 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0fbfcff-217b-31d0-8246-891a077db129 | -14.57279 | -52.88126 | 2026-10-04 04:23:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04504e1c-e37b-3322-ac01-870b8cec11b1 | -19.84621 | -51.54348 | 2026-10-04 04:23:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8905bded-c40f-3a9c-9ea9-98ded77b8470 | -17.7817 | -46.48318 | 2026-10-04 04:23:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df21f90a-d5f7-36e6-b63a-183337c5ea0a | -19.85571 | -49.05642 | 2026-10-04 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81de6efa-8274-3e91-94df-0a831010a8f8 | -16.84205 | -39.15233 | 2026-10-04 04:23:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cebab152-be25-35e0-a9c5-5975e7280901 | -20.37374 | -48.52287 | 2026-10-04 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85586752-e7fd-3914-85dd-64c46f407a49 | -15.91768 | -56.34678 | 2026-10-04 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34dca6d8-4cfe-3146-a973-f3210161fc98 | -17.78504 | -46.48372 | 2026-10-04 04:23:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb09bd18-2cc5-3f87-9075-83227f4c3d55 | -16.41596 | -50.4896 | 2026-10-04 04:23:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9186e26-6908-3079-8a22-fbbbda6ece99 | -14.57353 | -52.87711 | 2026-10-04 04:23:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad342f25-132b-340a-960f-638aaa1efb5e | -17.78115 | -46.48685 | 2026-10-04 04:23:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1415b33-a505-372a-81da-62d0a9241e24 | -18.91849 | -47.91063 | 2026-10-04 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c312fd-a615-3375-bec9-68cce60804e6 | -15.91247 | -56.34568 | 2026-10-04 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01c643fc-1fe7-3289-a8b3-72125b928640 | -20.36985 | -48.52595 | 2026-10-04 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cff15c7-ce15-3639-a249-2b1d077b1b66 | -20.22932 | -57.99126 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8da1186a-3aac-3174-999f-859d6f90903f | -20.23915 | -57.99731 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fcd63d1a-c327-3957-9cc3-aa2a00791892 | -20.22778 | -57.99833 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 08b483b9-2021-373e-b437-5223e558ad99 | -21.91231 | -56.9235 | 2026-10-04 04:25:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 175d545c-f865-3367-b2c4-33460e7b9293 | -20.22984 | -57.99882 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9e14d2ff-aec9-3709-9ddf-6bc8ac62b683 | -20.22604 | -57.99044 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b43cde96-341e-3b8a-bbf4-214f3b6b0fb6 | -21.56407 | -56.73492 | 2026-10-04 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2b26d4-dc02-3134-9cdf-f5563da04b2d | -20.22403 | -57.98999 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b6cd6c45-a6a4-3ab7-a870-1643540e14e2 | -20.23308 | -57.99959 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7699209f-16e5-3d4c-bf09-3652ea0b14b8 | -20.23059 | -57.99527 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6dac1fd5-ff91-3b33-b9a4-454841073dd2 | -20.22855 | -57.99479 | 2026-10-04 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 99167ead-79d5-3776-8906-62d0328d2402 | -3.1117 | -53.7032 | 2026-10-04 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0b0e8227-76e3-34c6-90dd-ca643332d247 | -2.8163 | -54.133 | 2026-10-04 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2b9b00e8-6a79-39ec-8155-39a7018e4407 | -3.1116 | -53.7436 | 2026-10-04 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 135e9157-11aa-37c6-aa9e-8c679d9b9419 | -2.7979 | -54.1134 | 2026-10-04 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c86c716b-fd69-3440-b426-4daa2264a51e | -3.1116 | -53.7234 | 2026-10-04 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| 589d65d5-6071-3808-ac66-f79ea5f1f98d | -2.8163 | -54.1129 | 2026-10-04 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 76f82303-c99b-339d-8872-8333a0c9c478 | -3.8757 | -55.7986 | 2026-10-04 04:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fdf2943e-5c41-34b9-a498-400fb5e9b41b | -4.2886 | -50.2886 | 2026-10-04 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 834ff60a-c3f7-31b3-938f-d38ae3659606 | -3.13 | -53.7229 | 2026-10-04 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0ed34804-1351-3f04-9410-d6c01c22a8ae | -2.5842 | -51.8623 | 2026-10-04 04:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 62915d26-b985-393a-ba8d-9312b8516c88 | -4.3072 | -50.2668 | 2026-10-04 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 53e62316-cf96-3888-abe8-005ebeb69cd3 | -4.2887 | -50.2675 | 2026-10-04 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 568.2 |
| 543846bb-8ed4-3cbe-896b-bfa3cd0ee07c | -3.1299 | -53.7431 | 2026-10-04 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2a8d7c95-015e-3dd1-b423-782e7840da14 | -3.8756 | -55.8184 | 2026-10-04 04:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d150f1ed-e6ae-378a-93cb-b57e8f25dfba | 3.42124 | -51.30067 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e74e88b2-a2cc-38e5-8299-a723c7dccc6a | 3.35965 | -51.34563 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee6f484-4a87-3664-8b4a-8209d9abe525 | 3.71372 | -51.39538 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b2d24dd-1675-31a7-9474-5371956b92c6 | 3.42185 | -51.3046 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eeeff9f-6d87-37b4-82db-9497aa626244 | 3.35734 | -51.35405 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28ac2f11-84b2-33e8-829b-63a20c7aef6f | 3.42477 | -51.30012 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e76c7b-236b-39ef-a949-ce690e224554 | 3.42537 | -51.30405 | 2026-10-04 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00700bca-4517-3dcd-8662-43613ffa13d4 | -3.26874 | -50.08957 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d674419b-cd0c-3eac-b583-a87ce9987684 | -3.73875 | -53.42456 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d56ba9-7f72-3f6f-a3d8-4a403135698c | -1.75829 | -55.55402 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35bdfc5a-5d0a-3225-ab75-9e7fb2b89d04 | -2.80981 | -54.09474 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b976e70-0cfc-3ca5-98b9-01ce432bfbcb | -4.26078 | -50.78495 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4608676c-210e-3180-9924-a5b7d0bf91dd | -3.50755 | -54.60547 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a8789c0-c81f-3337-8bc6-7d662ab77e17 | -3.18022 | -54.0946 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1c3072-13f1-3aaf-8639-6fcb95b5852c | -2.83456 | -54.20811 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7fefd6-4811-3968-a912-bc5bb29616f5 | -3.05847 | -54.15826 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 339a9e88-f26d-3548-9165-105b94d84a1f | -3.04661 | -54.22575 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 37597f89-05c2-31b3-9a6d-37a8acf827d2 | -3.07116 | -49.53943 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b3388075-549a-3373-84ed-4ac108ea4a71 | -2.81601 | -54.12875 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8096540a-aeb6-39a0-99f3-7279c18894ab | -3.17802 | -50.53226 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4bb1370-ee96-30dd-9d38-19f45b324728 | -3.63534 | -54.50617 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa0c0c19-9a1e-3d3d-b883-f3d1e0e1bce3 | -2.81749 | -54.11954 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f127a70-b476-34f8-8897-33782e4b9bf0 | -3.05577 | -54.17054 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a1f5d11-28f0-370d-b000-8301b9fbfd4f | -4.26685 | -50.74685 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 742412f2-6dfc-30d4-8af4-5d80e6f52f9a | -2.85537 | -51.28718 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3850ec96-0358-3a63-bdaa-0cdb746ca9c8 | -2.25307 | -51.93167 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009bc9c2-2fbb-3513-b665-0b908c1eeb82 | -4.28116 | -50.27385 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 9ea67fdf-aa8f-3b97-82c3-e3e01c209fdc | -2.93727 | -54.19323 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd329d2a-55be-3ff5-ac5d-19baac32d11e | -2.80074 | -54.10269 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 636a39a0-9c07-326b-a7f5-ce3091940e00 | -3.27648 | -50.40245 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0387c632-a9d4-3b95-979c-4ebceb1e012a | -2.96901 | -53.26855 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db577920-4c49-391c-935f-91508e1283ea | -2.56248 | -48.24671 | 2026-10-04 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 217e5fae-ef49-30ae-a4f9-2d92a6bea7b5 | 2.34222 | -50.75167 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084fed22-c1fc-3702-8ad6-8e50b958bd70 | -2.88316 | -54.14185 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e94d907e-beee-343f-8ebe-317b81a7c588 | 1.83599 | -55.54435 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25ed28e3-14ba-3878-9465-50677573a2df | -3.10679 | -50.30095 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43a457a1-d635-3e44-aa67-7a5199cb4d8a | -1.18343 | -47.61408 | 2026-10-04 04:55:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4937c580-5f08-370a-bc0b-2b5760f64bcc | -4.33309 | -46.64749 | 2026-10-04 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8786178-7902-381e-8aa6-639810d7dc4c | -2.21264 | -48.2272 | 2026-10-04 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f0d7c69-fb27-3534-a604-c9469c218ff8 | -4.27948 | -50.26294 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |


[Clique aqui para ver as próximas entradas](README34.md)
