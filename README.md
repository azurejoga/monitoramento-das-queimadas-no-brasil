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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec8e49d-9190-38c3-95ca-e11a3571904c | -11.2786 | -50.4746 | 2025-08-16 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0d1d9c6b-81d6-3ff7-a35d-c831fa10b0c5 | -9.518 | -60.5268 | 2025-08-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 723005d5-8cc0-31af-b5d3-ba2ec3872be0 | -4.9116 | -43.2803 | 2025-08-16 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e19fb34a-ad9f-3deb-80b5-bdb58b8ea124 | -11.3468 | -55.4124 | 2025-08-16 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| aa922cb7-088f-35e3-923b-121cc7990bc8 | -13.1265 | -57.1494 | 2025-08-16 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 1e126cc0-4b98-3812-9478-dd691e184392 | -14.9632 | -54.7143 | 2025-08-16 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4f612aa6-3f78-3d31-a654-b6f0c557d7d2 | -13.1074 | -57.1511 | 2025-08-16 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 8edd3609-4186-307c-805d-2d36b082c0eb | -3.821 | -47.7227 | 2025-08-16 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1e1fb50d-07c4-3095-aa28-e1fa4b4c90b0 | -14.9441 | -54.6959 | 2025-08-16 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 512730d3-61a6-3ccf-9df3-6be96a069cf8 | -23.1686 | -51.9992 | 2025-08-16 00:00:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| 3b0fc11d-cc2f-359a-8b93-7c15289e0497 | -7.8963 | -61.7485 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6225d3b1-c399-3695-8244-f737d9fac915 | -6.6327 | -60.0033 | 2025-08-16 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 81b21367-3f05-328f-b003-5a2f9cf8efef | -7.8247 | -61.3327 | 2025-08-16 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 9e87055b-f1cf-3737-b128-18eac466fc44 | -6.6142 | -60.0039 | 2025-08-16 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c1c147f1-2d34-35b4-b241-18549197d0a6 | -9.4992 | -60.547 | 2025-08-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| e72dbe06-e552-3156-960b-fd0b234717d9 | -13.1077 | -57.131 | 2025-08-16 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 207.7 |
| dffcf047-d202-321a-a1fa-a44ccedf1720 | -14.6023 | -47.9018 | 2025-08-16 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 19a2f206-f077-3b58-8b0e-080e8774cf20 | -5.762 | -46.6741 | 2025-08-16 00:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7f32c2bb-63bb-3c11-97cd-49c7a6f00489 | -23.1903 | -51.972 | 2025-08-16 00:00:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 247.1 |
| c2e3e30e-0894-3315-8970-503fb1c09c3b | -9.1708 | -59.6568 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| ad0ebb42-8d8b-310b-9aff-f478cefb9149 | -4.9305 | -43.2558 | 2025-08-16 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a692b58d-5b17-3bd8-9b7a-e9ad133e3c8e | -9.0531 | -67.4265 | 2025-08-16 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bd99945a-b85a-3be5-bd7b-62cb0b36a83b | -11.2593 | -50.4981 | 2025-08-16 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b22fdd93-e820-38ae-85fa-82f4223c2f8e | -6.9481 | -59.6452 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f288c375-ec59-3384-a7d5-a4a5195f89af | -7.5292 | -61.3254 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7551e2ba-26db-39fa-bed3-e1930acfd375 | -9.208 | -59.6548 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| abb24c08-b82b-35d1-a931-f751bc09ee10 | -14.9628 | -54.7351 | 2025-08-16 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 45bf2a44-d672-30f7-af20-641073f06c9e | -14.6213 | -47.9211 | 2025-08-16 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 12c2d58d-69e8-30b3-8893-32c3db83c5de | -4.9118 | -43.257 | 2025-08-16 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 32c8d0aa-3afd-3be9-9678-1dfbda18f5ce | -7.9149 | -61.7288 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 2615b86f-c325-3262-b66c-81e76f7aef7a | -9.4994 | -60.5278 | 2025-08-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 710c90ae-ac35-39c9-b5a1-a8d669e681ac | -6.7811 | -59.8249 | 2025-08-16 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0a821e8f-e7a3-3cb3-bc06-63383565a12e | -11.2596 | -50.4767 | 2025-08-16 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f4fdf2e0-e62e-36cc-9f4c-a9cea2c2879a | -9.1523 | -59.6384 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f64c0241-bab7-3e14-a7d8-433cfbc1804c | -13.4294 | -43.6733 | 2025-08-16 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 958fa21f-ecf2-3749-b801-a550078c781e | -11.3466 | -55.4326 | 2025-08-16 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f8622763-749f-35ad-8271-751b5f30cc4b | -6.9296 | -59.646 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| fd13da50-beea-3c71-bab5-27553ed12747 | -13.4099 | -43.6768 | 2025-08-16 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 130e28d1-1b76-3936-acf6-dc2c161e3c7d | -9.1709 | -59.6374 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 6cd8397e-62cc-3f13-b864-b864c65465e6 | -7.8248 | -61.3137 | 2025-08-16 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9addc5ae-51f1-35d6-a2d6-79c43abaddda | -9.5179 | -60.5461 | 2025-08-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 27a4cf1f-8762-3503-b2fc-95d804d3b01a | -14.9635 | -54.6936 | 2025-08-16 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| c0964708-04a4-302c-af91-3ba5a60e25d9 | -23.1896 | -51.9947 | 2025-08-16 00:00:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 193.6 |
| 1335ed2d-852e-3eff-b15e-cb5dc072d157 | -18.5325 | -50.7384 | 2025-08-16 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4b430034-9324-3eff-b897-3036eee5f4d6 | -9.2082 | -59.6354 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 0ba7ad21-3c7f-3bc3-90ec-187fe421c915 | -6.7995 | -59.8242 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 6e76c2f3-4bef-3bd8-ad8a-de91b5974a84 | -7.0797 | -59.2157 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 277d78cc-3f6d-3375-ad5f-f7759a93f292 | -15.5781 | -49.6778 | 2025-08-16 00:00:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b2c74ee2-3c8a-3180-b9f6-b2f90d9d2d34 | -23.1693 | -51.9765 | 2025-08-16 00:00:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.2 |
| 090a70ef-9a02-3864-b551-920015e6498a | -2.3763 | -47.6636 | 2025-08-16 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a655ba3c-f888-371f-8f4b-c95211d2d2a9 | -7.0612 | -59.2358 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 9e1b6007-421b-3892-aa7e-a82934eed3a5 | -7.9333 | -61.7471 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4b274273-e0be-3303-839d-3b8e75ddbe08 | -7.9334 | -61.7281 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6f1c12aa-fdfc-3723-b15c-29ea525b5942 | -6.6326 | -60.0224 | 2025-08-16 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 67f9e969-64ab-3c69-b09d-75a7d3b41073 | -14.6018 | -47.9243 | 2025-08-16 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4fc080f7-10d5-3fda-bb8d-d3062dc4da3f | -14.9438 | -54.7166 | 2025-08-16 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8ad9d3ca-8f04-3ce1-b813-df821d9a91d0 | -7.9148 | -61.7478 | 2025-08-16 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 833d8fb2-9357-3457-86af-30895d3e3fd8 | -9.1711 | -59.618 | 2025-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 9cca7543-4eed-32fc-985d-548ee8be9bfd | -3.8209 | -47.7444 | 2025-08-16 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| c5044753-606b-3044-87b5-2e58da435849 | -9.4991 | -60.5663 | 2025-08-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 68493272-a9ae-311f-95ff-fe85d8954c30 | -7.0796 | -59.2351 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 1549d46a-c67a-35a4-b025-c43a0ee7c00c | -7.0404 | -59.6222 | 2025-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 38107793-436d-3a61-aab0-7ff7912ba925 | -9.0346 | -67.427 | 2025-08-16 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| eb2ab838-1725-38e2-8625-8995bcde42fa | -13.1267 | -57.1293 | 2025-08-16 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 2205c54c-b9ab-3370-a880-4a92e7020e96 | -6.5615 | -43.019798 | 2025-08-16 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad83ea3-ca54-3020-af97-4d1766ce0f39 | -5.2717 | -36.1717 | 2025-08-16 00:02:00 | METOP-C | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f1666d22-d0de-3cd3-b5f3-ea032c546bf3 | -13.4149 | -43.670399 | 2025-08-16 00:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 545c874b-f6b2-31c4-ba74-ee0cae0ab510 | -6.862 | -42.801102 | 2025-08-16 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c12b090c-e875-3b8b-b9ca-2f88e313a0d7 | -6.5639 | -43.030399 | 2025-08-16 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ddad8f3-efeb-31eb-9a20-de6d9aaed5c1 | -11.9961 | -44.538601 | 2025-08-16 00:02:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9bf6ec3-959b-38e0-b1af-3dcfdc74f2da | -4.5965 | -43.311501 | 2025-08-16 00:02:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91017f8e-b705-3f18-989e-abb55c2fec44 | -14.5954 | -47.933601 | 2025-08-16 00:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f49caad3-7750-3bed-8a71-2711549764aa | -6.9254 | -42.9977 | 2025-08-16 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fc84a2cc-6717-3013-869d-adc7ace1224d | -5.7493 | -46.659 | 2025-08-16 00:02:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3b56ec8-411b-37c9-8730-d9948381c79b | -12.5818 | -46.9277 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa1af479-69b3-34ca-b093-f95f7789f452 | -6.6748 | -43.773102 | 2025-08-16 00:02:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 476e8aff-bc20-3e6b-977f-5e3b811e3ac6 | -6.5518 | -43.0219 | 2025-08-16 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad7137fc-4f29-3b8f-9897-7a255ce4fa56 | -5.2619 | -36.173901 | 2025-08-16 00:02:00 | METOP-C | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f79d7bad-26a2-3a15-929f-362d02625a1d | -2.3758 | -47.652199 | 2025-08-16 00:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52125f89-3010-3987-9a13-69418d287c04 | -4.9217 | -43.2519 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edab785a-cd72-3c6b-99b6-d45cc5bef048 | -3.8136 | -47.710098 | 2025-08-16 00:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8526ec3d-c2a6-3d5f-91f2-733cb7c6936d | -11.9928 | -44.522301 | 2025-08-16 00:02:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 157ecf12-b488-3548-ad75-72ab001e10dd | -5.2734 | -36.1791 | 2025-08-16 00:02:00 | METOP-C | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 7fdfac4d-17e5-3c7b-9a5e-22caf6ead658 | -4.924 | -43.262402 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd23002f-77e0-384e-88cb-1d8618cb5fe9 | -6.9586 | -42.868099 | 2025-08-16 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8339238f-ddec-368b-9a21-f10023bef36b | -6.9563 | -42.857601 | 2025-08-16 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf9b1417-1483-30c4-b4d5-d12c481d290e | -12.5334 | -46.937 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f87c293a-dc70-37aa-a800-1fc6a14b9e77 | -3.8225 | -47.7505 | 2025-08-16 00:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf894f21-9db9-3315-9a63-b65341b76873 | -14.6008 | -47.964199 | 2025-08-16 00:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25ae9004-e064-35d9-b64d-6bc00765f045 | -12.8292 | -46.010399 | 2025-08-16 00:02:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a394489b-1299-3bf1-a455-999e2fc4f7a1 | -12.5864 | -46.952099 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e25f5803-a574-39a2-a7a7-3c21a4ddb0bb | -12.6012 | -46.924099 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68950aba-3278-3118-84c7-3d0af99188da | -11.4181 | -44.688499 | 2025-08-16 00:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a53a586-d84a-381d-9433-421a26cf37a4 | -12.5527 | -46.9333 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e8a563b-7913-3887-8ab3-27865ee78983 | -4.1431 | -46.4356 | 2025-08-16 00:02:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1156aa18-cd71-3076-a3e4-271690eee439 | -13.5727 | -46.9725 | 2025-08-16 00:02:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f09ff0f-6b51-3616-8939-8d2eab710f2b | -12.5574 | -46.9576 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a66a7875-763b-3a32-acca-f30670b1a104 | -13.4276 | -43.683399 | 2025-08-16 00:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 469bd82a-1139-3ed0-8f30-55b297f1bd36 | -12.538 | -46.9613 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a6655bd-79af-3943-ab29-192574018296 | -4.1467 | -46.452301 | 2025-08-16 00:02:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
