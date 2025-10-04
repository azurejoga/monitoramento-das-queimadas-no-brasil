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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f363d93a-277e-3218-9c52-38379b99c319 | -7.6458 | -45.4716 | 2025-10-04 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 8e1a80d1-c46a-3aca-aebb-636239f050aa | -12.8761 | -47.2937 | 2025-10-04 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 83b16528-6219-33ae-b50d-12490e45d9f5 | -13.4925 | -47.2685 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c4cae8f6-f9dc-3e28-9152-ef625abfb7a9 | -11.5256 | -46.7871 | 2025-10-04 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5b2ead5a-6ede-35f5-a293-4d6839de12c1 | -13.3426 | -48.0742 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0da45bdd-0600-30d6-ba56-00fc2b5993f2 | -5.9742 | -45.8799 | 2025-10-04 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 373d8e28-8592-3c89-877e-5993b2509efb | -13.9189 | -48.1882 | 2025-10-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1ecb421b-36b8-3758-892b-25545ad21f98 | -8.5458 | -47.264 | 2025-10-04 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 931ac6e3-e6d7-325b-9216-5a407b7233fe | -9.1901 | -49.9604 | 2025-10-04 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 8c1b1583-928e-3a4b-9031-38e65ecffc1a | -12.3162 | -45.3545 | 2025-10-04 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d539448e-3ae0-3303-8dde-37cbbd4ac677 | -13.7473 | -51.3097 | 2025-10-04 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b4f68f53-2aca-38f0-ac3f-04fcf1089933 | -6.3673 | -43.8916 | 2025-10-04 14:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8a1f9593-ee82-36cd-97e4-7a20a75ee261 | -7.0604 | -45.7946 | 2025-10-04 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| fcb89e28-f421-3ca2-a21e-9e81138ab1d8 | -11.8442 | -44.9408 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| fb24d74a-c720-35a7-874d-dfff0ae142e4 | -9.1114 | -44.4029 | 2025-10-04 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 55385240-572f-3537-9c12-976099593390 | -6.0616 | -42.537 | 2025-10-04 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 9664feae-624e-36f4-894f-bce5accaa83c | -5.9555 | -45.8812 | 2025-10-04 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bbe3af94-eb14-3eef-b004-74f395c0e7ec | -8.1888 | -44.1588 | 2025-10-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| af528604-5722-3134-9fb8-47093ae89cf2 | -14.8268 | -54.7926 | 2025-10-04 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 6711f083-179c-374a-8a63-dd5c28c8687f | -12.3222 | -50.6322 | 2025-10-04 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 855307e4-c844-3179-84d2-cc600985cb8f | -8.2476 | -47.0492 | 2025-10-04 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8b25cd00-d2d1-3e93-aedd-72194bfc4495 | -11.5069 | -46.7671 | 2025-10-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 5f4882c7-fca4-35b4-9818-ee5279b67eac | -13.2934 | -47.6129 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e3e23dd2-f5de-3cc9-abd3-160163a1dceb | -13.3127 | -47.61 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d04d9919-6ad9-353c-8fb3-0b5f9bba5304 | -13.251 | -47.8203 | 2025-10-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a5a82776-bf7b-30d0-963d-805655baa949 | -11.5054 | -43.5426 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 3af92371-596c-3410-bd66-fea5426aea16 | -11.6841 | -45.3333 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f1f24570-ac75-3705-a0c6-70ee01454a2e | -5.9584 | -43.5072 | 2025-10-04 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 22d1d85e-5822-37ef-8779-8a99dda1b95a | -10.2206 | -50.373 | 2025-10-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5b0440af-f405-3bb3-8897-3e2bbb25baa4 | -11.863 | -44.9612 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9d1b519b-13c7-3af8-8c28-289fe1868dd8 | -10.5835 | -48.7178 | 2025-10-04 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 23ddb18f-9c66-3cc3-972a-82f4ffa008fb | -9.648 | -54.3143 | 2025-10-04 14:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e58e6a31-c625-3bdf-9087-4dbf3f9eb56f | -14.9548 | -46.8473 | 2025-10-04 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 04f864a9-c93f-3821-b51b-449d21ea977f | -11.7924 | -46.8184 | 2025-10-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| daf59108-3f2e-38b6-a65b-31298cd3e643 | -7.7684 | -46.2479 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| be517792-b8cb-3557-803e-b54127fcb4b1 | -8.2664 | -47.0474 | 2025-10-04 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 24489bd3-c2ad-318f-b092-9b4e0e80f19f | -8.8534 | -46.7451 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| fffed4b3-79ec-3d38-97f1-d52e5237a983 | -5.8739 | -42.5289 | 2025-10-04 14:10:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 0ebc0f14-cfdf-3470-be26-47ece91ff4e3 | -8.7964 | -49.9106 | 2025-10-04 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 1d46211a-0afa-3b6c-8c57-fbb843fae421 | -9.3274 | -54.5418 | 2025-10-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 92812bf7-67a2-3c82-98ad-0177f2167d54 | -6.1728 | -44.6203 | 2025-10-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 19dc128b-79c3-3e48-80bf-73c025252eea | -7.7123 | -37.3184 | 2025-10-04 14:10:00 | GOES-19 | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 10b3a121-20a2-3bf2-9c34-9b7cda9a5f51 | -13.1164 | -47.8178 | 2025-10-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fe89564c-c92f-3962-956c-27f06cad8194 | -9.1114 | -44.4029 | 2025-10-04 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4d59523d-2f17-3776-9b6d-4d0b7b2ea899 | -11.4877 | -46.7696 | 2025-10-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 7fb82724-1b91-3528-b42c-00140198e966 | -11.4862 | -43.5456 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| ab9ca8f0-1be8-39af-8e27-623522100fd0 | -9.3089 | -54.5229 | 2025-10-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 39ce5c6e-82c8-3274-bf7a-5c23f2d25625 | -7.0046 | -42.3091 | 2025-10-04 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 4182f9f6-c1f1-3778-b3a9-e44a39b36387 | -6.0616 | -42.537 | 2025-10-04 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 776c9b01-6a54-3ff7-88c1-01ce05860703 | -7.7933 | -44.1304 | 2025-10-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 4ee9f032-3c0d-3080-83a0-3dded56a5c5d | -15.3792 | -47.9746 | 2025-10-04 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 164.8 |
| dfaf9cfa-117e-314e-826e-8c8642b6154c | -11.3265 | -53.9665 | 2025-10-04 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 3b6ec93a-ae91-35e9-a463-5f45bb961de8 | -13.7472 | -48.0806 | 2025-10-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 11d6c20e-6f58-3597-b50f-2be0c982fc86 | -11.792 | -46.8409 | 2025-10-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e80c80a2-ded0-36ef-a9cf-7dc09183c2a2 | -6.2408 | -45.3424 | 2025-10-04 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8270ba5d-2f1a-3948-91a2-83751b15bfb3 | -8.8526 | -46.812 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8347c989-6826-36a0-946a-d5357f7f0e8d | -12.4364 | -44.079 | 2025-10-04 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 289.3 |
| ca764c7c-321b-3ed3-bb84-00f532726236 | -7.7933 | -47.3776 | 2025-10-04 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2f790506-109a-3004-a956-dd5fde96cc2b | -15.5211 | -46.838 | 2025-10-04 14:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 368b73ae-027e-3dca-bf4d-f698da2e7837 | -15.1357 | -45.7104 | 2025-10-04 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 255.6 |
| f4044682-f7d0-31e9-bc75-861c59002f8c | -7.0604 | -45.7946 | 2025-10-04 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 45276544-6149-3416-9fe6-4f5d0de39387 | -14.5755 | -52.4576 | 2025-10-04 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 7f7dae8f-c0a1-36da-9d50-69f89f30b88c | -13.3032 | -48.1244 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 826d586a-8a50-385f-8323-120bb1719800 | -7.7938 | -42.5607 | 2025-10-04 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 2cf928ea-80dc-3720-a0f9-b9cc31618ff2 | -14.5751 | -52.4789 | 2025-10-04 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 63e99fdb-23b4-3252-8503-82f48d70671c | -9.1716 | -49.9408 | 2025-10-04 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c58d5c02-8ae4-32e4-8b4e-f98f874667eb | -7.7743 | -42.6103 | 2025-10-04 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 0d20b470-64ee-313f-a022-c131bec2ad93 | -7.0369 | -42.78 | 2025-10-04 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 243.0 |
| 4d73ea9e-cbd4-333c-b812-f077facd2a04 | -6.1234 | -45.9139 | 2025-10-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 03f0a39f-26d0-3de9-bf64-ca46ff3a875e | -14.8461 | -54.7903 | 2025-10-04 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fa42f8e8-d095-3245-bf52-fec606eb0d10 | -8.9002 | -46.0459 | 2025-10-04 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 234.6 |
| e0e5da3a-e825-37de-ada3-1f19133bc87e | -14.6521 | -48.3188 | 2025-10-04 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 30f2a685-61b3-3cdf-a1b0-c8f0b457be4d | -6.6069 | -44.3098 | 2025-10-04 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0339e884-ff0a-3671-b4b7-f331aa2056fc | -13.5119 | -47.2655 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 98042ff9-88ca-36a9-a622-e6e4f52a09c5 | -14.9881 | -49.9892 | 2025-10-04 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| f2bde37c-5c33-35d8-b325-a5f641abe994 | -8.2666 | -47.0252 | 2025-10-04 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8350a090-6dd0-3061-bec4-b2c09704249f | -11.6314 | -45.0646 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f50b7d3b-ce9a-36aa-b068-4b22173fdefc | -13.116 | -47.8401 | 2025-10-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| c9a483b9-2a72-3150-83a5-84a29c8804c4 | -5.7884 | -45.7585 | 2025-10-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 317b9352-f76e-36fe-8417-67072a083480 | -12.9468 | -51.0053 | 2025-10-04 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| a4cbb525-fc1a-3ae2-b547-7b54c4cebf25 | -5.9742 | -45.8799 | 2025-10-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9f3c84d3-2b18-3533-8c44-5ed49804f1bb | -11.1268 | -47.9077 | 2025-10-04 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 6d506f67-31fd-33e4-9503-b7c3876a9104 | -15.3179 | -46.3011 | 2025-10-04 14:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 28f371f2-f0cf-321d-8337-bba858866e3e | -15.3797 | -47.952 | 2025-10-04 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 3585cdf7-f98c-3bea-8a39-72112d02217d | -5.9555 | -45.8812 | 2025-10-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2dc7feea-0697-3770-a3e5-672acb49a1ec | -6.1542 | -44.5989 | 2025-10-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b7f58ec6-ed31-3add-bc38-f09325ff70a4 | -13.9387 | -48.1629 | 2025-10-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| efd22e20-6e08-34fe-86cc-6fff01148170 | -11.4486 | -43.504 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 86c738fd-ade7-3c54-a824-6eadb426a058 | -11.5256 | -46.7871 | 2025-10-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 23ea3134-85e3-37ef-90b7-96821a2d6ff3 | -10.2973 | -50.2799 | 2025-10-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| fa46bc59-e3cf-35db-864b-400f6fc3ec57 | -5.2588 | -37.9238 | 2025-10-04 14:10:00 | GOES-19 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 130.3 |
| f8c0421e-1ce5-3664-b395-2c5f35c9c448 | -8.2128 | -46.8084 | 2025-10-04 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ed51f06e-44c6-3def-947b-450365201b3b | -15.3601 | -47.9554 | 2025-10-04 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 6c2211b8-d575-384d-be77-edc4de4d826e | -15.3597 | -47.9779 | 2025-10-04 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5050ceb4-9089-3dfd-a205-fa704deb8007 | -9.3276 | -54.5215 | 2025-10-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 322.6 |
| d59e2ec9-9b8d-3325-a87b-3cbb7aba3173 | -11.8438 | -44.964 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c5d33255-02f6-335c-a26a-2f66f9c4224c | -5.7882 | -45.7809 | 2025-10-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9088d761-e4fa-303e-a3cb-77845a8aafd4 | -5.8764 | -44.2764 | 2025-10-04 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 66c29e5a-50f5-3d6c-8256-32b5160c24be | -7.7682 | -46.2703 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 55973001-c809-3b52-880d-0a758b3c3c8d | -8.7777 | -49.9123 | 2025-10-04 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |


[Clique aqui para ver as próximas entradas](README154.md)
