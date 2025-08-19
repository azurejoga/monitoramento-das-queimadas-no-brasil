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
| 1f9b5883-dc71-3689-a655-f842f46b84f7 | -14.5036 | -45.940899 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 488b3581-4e36-3fec-9a30-9fd8fba626a6 | -2.5453 | -47.727501 | 2025-08-19 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab6726b-6c48-3678-9a88-8b707cff6ecf | -2.5437 | -47.7206 | 2025-08-19 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 113550a3-2505-3a42-96d4-780df48735aa | -6.9787 | -43.5928 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f790b005-9a2d-3e64-a7f4-d6e2d9260e64 | -15.0215 | -54.800598 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca4c7577-cee1-38de-87a3-2f09666292f0 | -12.6363 | -46.896198 | 2025-08-19 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5d56f89-0313-34fe-86cf-9d0bb87ce802 | -11.8611 | -51.580002 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d4ceca8-6d63-33f7-b9c5-3fd0cce71cc9 | -6.9417 | -43.611 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa15d968-607f-3ad3-a41a-1b518ca7ff66 | -5.5557 | -49.0769 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1176c1e7-844b-3134-9a46-c4a5a8577d20 | -7.2905 | -43.688202 | 2025-08-19 00:34:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1a39a4-01a7-3b9a-b8e9-2f4df4cab055 | -14.9886 | -54.785999 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91ca58d5-8465-36b5-879b-f26305abcd4c | -12.6495 | -45.811699 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf999b60-45dd-329e-96ac-4d5c6beb6840 | -14.8749 | -48.057301 | 2025-08-19 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0099b903-5953-3fc8-9804-acf7fdab714b | -4.928 | -43.2561 | 2025-08-19 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95f7e149-ab32-3fe8-8b0c-43771589e1b5 | -3.9849 | -47.886398 | 2025-08-19 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e248572-db07-32ea-b0c2-b632662c4df1 | -3.2631 | -43.2761 | 2025-08-19 00:34:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aadd062-20cf-3146-8924-b8935c181163 | -12.4359 | -48.695801 | 2025-08-19 00:34:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 498c6083-be1b-3b3a-8708-a2ca43902715 | -14.9691 | -54.789799 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5866fdee-a44a-3aae-97c2-9a16df36d4d7 | -7.074 | -46.8727 | 2025-08-19 00:34:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f00d4ce3-8c48-3654-8c71-bec84b57c780 | -6.9515 | -43.6087 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5f382e2-4c14-3a9f-a213-1893355df587 | -14.9826 | -54.807899 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5b30f55-beb7-388a-9de9-2fe66c037f34 | -4.9232 | -43.236099 | 2025-08-19 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 111cd9ae-f8d6-3fa4-b767-69e178b6e413 | -12.0381 | -44.016701 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84e5debb-553a-3b4b-a20d-3c71b18de01d | -13.8673 | -45.542198 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa19bc17-700a-3edc-b87f-3f55222733e3 | -13.0023 | -45.188099 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40a9e1b7-64b8-30d7-bc95-29516dd65237 | -12.6593 | -45.809399 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad1f8d4-2faa-3a7c-afed-ec93d82dc9ed | -10.9615 | -49.565399 | 2025-08-19 00:34:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc63bbe3-ec13-3194-a69b-3ebcfc072551 | -3.4585 | -48.965599 | 2025-08-19 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905cdb39-80d1-3a2e-9065-3f1c79e9bccf | -12.9941 | -45.197601 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10e63903-8e21-3d5e-b28e-47315c4b2d18 | -10.4573 | -48.809799 | 2025-08-19 00:34:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54a857a3-01db-3aea-aa8f-97ed7e8e974c | -14.1764 | -45.313801 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e63a0105-18c6-35ce-9688-0f681c5f526f | -12.4261 | -48.698002 | 2025-08-19 00:34:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebfa0260-e6dd-38c5-a04f-dbcb9f39570c | -7.2532 | -50.172401 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fcbcbab-b283-33b6-8cbb-6f737fa2495d | -6.0566 | -43.752102 | 2025-08-19 00:34:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5d9a212-5428-38bb-b572-2f1aac9db48e | -12.0363 | -44.008999 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30b2d5cf-babe-37a7-bd68-2405906b35d4 | -7.3024 | -43.694698 | 2025-08-19 00:34:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0d02c97-4e32-32b2-9c16-ea05d65a5094 | -7.2745 | -50.175999 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7699d381-9729-3edf-9a9a-0d9eac417d04 | -14.8715 | -48.041599 | 2025-08-19 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdb1fefa-c5dc-357b-afdd-1bac453298fe | -12.6527 | -45.825699 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f303e327-5f57-37cb-8104-728bdfd07829 | -6.9766 | -43.583801 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06775e12-6ad0-3bed-ba24-c1b764d2daca | -4.5934 | -43.323502 | 2025-08-19 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec246b64-5cfd-32e0-994a-0562ab9ff73c | -3.9834 | -42.5327 | 2025-08-19 00:34:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f550a652-b6d1-33a4-a43f-93d80b9f5c86 | -6.9537 | -43.617599 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05428c3e-7fa8-3990-9058-e1f7f1bdd7cb | -6.9689 | -43.5951 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81017892-1c02-35ba-a94a-44e1c8e5d398 | -5.6545 | -43.405399 | 2025-08-19 00:34:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0247752-099b-3ba2-b665-762d56cb116b | -13.2534 | -50.811298 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 440e51c3-d267-3f53-9cd8-296960f6508b | -12.5006 | -45.566101 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe8b481f-96c8-31a7-a9a1-e956c68d6335 | -11.815 | -44.255001 | 2025-08-19 00:34:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4ad29a6-fd84-3863-a96e-4b7db7d5ab45 | -5.9835 | -44.1413 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2beed9d4-25b2-398d-9244-c3f7ab12ca2c | -5.8765 | -48.129799 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abd6daf7-ee00-313e-937b-08f3f5c4c6ca | -5.7862 | -43.612701 | 2025-08-19 00:34:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e56eb090-b675-3e47-bd62-85728d7045c5 | -6.2504 | -44.837101 | 2025-08-19 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff9f3e15-abb9-3dc7-ad51-6fbcec06ca7c | -9.5778 | -47.4063 | 2025-08-19 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48e82225-3e44-3f6b-82eb-63ccca516934 | -3.9806 | -42.521198 | 2025-08-19 00:34:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4377c776-e8e4-38b6-aec1-ea26d743e1e5 | -12.0479 | -44.014301 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fdba183-e6f8-36ba-941b-aac6dbdf0291 | -5.9794 | -44.1241 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ff922a5-aa05-3596-a719-2f69b474978b | -7.0756 | -46.879601 | 2025-08-19 00:34:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1d890c-4867-37cc-85ea-1f2795bb6b58 | -12.9753 | -56.858898 | 2025-08-19 00:34:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6acd458-fa52-32b6-bf3c-e33341160e61 | -4.6009 | -43.311298 | 2025-08-19 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1d5f67-bb28-3470-be26-954f7754f252 | -3.9904 | -42.519001 | 2025-08-19 00:34:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 73ac1133-a9c1-35e4-b770-4d093d691bd8 | -7.3019 | -46.294201 | 2025-08-19 00:34:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32542984-9263-3b57-84f4-c6972ceff216 | -2.9137 | -48.2981 | 2025-08-19 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d08870b2-6189-35d3-97e5-6125825059fe | -8.7028 | -47.866402 | 2025-08-19 00:34:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c32c166-9fbd-38b8-a19d-fe33be02e65c | -7.3117 | -46.292 | 2025-08-19 00:34:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de1660d2-19bc-3bbe-9f0f-d8ca727d04e9 | -14.8455 | -48.063801 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a84bb7be-1ef7-3cfb-9628-680a697bce55 | -8.7707 | -50.017601 | 2025-08-19 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0995173-c8fa-3804-93a7-fe8b40751a6a | -11.8565 | -51.558201 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5f53125-8baa-3024-9a7d-c032d395d12d | -13.5944 | -46.991402 | 2025-08-19 00:34:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e04f060-0ca7-3005-9641-c3bf828fda84 | -14.8732 | -48.0495 | 2025-08-19 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9efd7c6c-6df1-3329-91af-b9f4de3f4c06 | -13.2632 | -50.8092 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af3b0155-bae1-367a-b6a2-73ed81756f70 | -14.8472 | -48.071701 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5cc8d3-c5e0-3308-803f-e69642eab9e8 | -13.0056 | -45.202301 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04281665-4709-3bcc-8a07-e584093c00da | -5.8863 | -48.127602 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa4fdd33-1840-394b-b34a-23b3622b8d5b | -5.6522 | -43.395901 | 2025-08-19 00:34:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 617d0c32-7f9e-3e81-8911-c3e6effd86ec | -12.6625 | -45.823399 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc0fb73-b2c2-3d66-98c4-bc535d417901 | -4.9256 | -43.246101 | 2025-08-19 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 241e7e70-c30d-369b-83c9-91736ef9078e | -10.9633 | -49.573601 | 2025-08-19 00:34:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcc53d81-cd77-397f-abd7-db0354e5aef4 | -4.9159 | -43.248402 | 2025-08-19 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1b0809-b89a-3f3f-b9fe-73ef6a5912b5 | -5.7511 | -46.6842 | 2025-08-19 00:34:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba1dc252-d856-3bba-baef-3499dcf80574 | -12.499 | -45.559101 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73332a50-5f36-3a33-aa66-db4e9fa3b771 | -4.1511 | -46.458599 | 2025-08-19 00:34:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc06094b-5b4e-3c65-bf14-9ffcf1775719 | -5.9815 | -44.132702 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 879cd1ea-e071-3156-b6f2-1514eeeabc0e | -9.0432 | -50.1828 | 2025-08-19 00:34:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b95f84d-c67d-3e81-b17f-af07ce924771 | -11.8633 | -51.5909 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aefb05b9-a5bc-30b2-939e-4945b6010832 | -15.4089 | -49.574402 | 2025-08-19 00:34:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8999dab5-9fad-317c-b748-e9ad87c0f9c4 | -9.715 | -51.964401 | 2025-08-19 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69530aee-f143-31bb-a6ed-5b2420bb1dea | -3.8295 | -47.7491 | 2025-08-19 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a799ee45-033a-34e8-9e46-74a17ac161d3 | -6.9451 | -43.581699 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72e3bbe0-77a0-39b2-9d4d-ab60378d5297 | -3.9931 | -42.530399 | 2025-08-19 00:34:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1da6a62f-99af-3b9f-aacf-0434134941b6 | -9.7173 | -51.975101 | 2025-08-19 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd2bb1b-362f-346f-8063-a07dabe8a6f2 | -8.2394 | -47.868198 | 2025-08-19 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddddd025-06b5-3f47-bbcf-149cbbcb32df | -5.5427 | -49.064999 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97d5a3cf-6bd3-3d24-b355-62d520f25be4 | -11.5819 | -44.849899 | 2025-08-19 00:34:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7f9e86c-4439-3cd6-8c52-f1eb24c67a92 | -8.2379 | -47.861198 | 2025-08-19 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a12c4379-52fc-3803-80bb-1c676d5c4e7f | -3.4841 | -47.682701 | 2025-08-19 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b4af43-a212-30c7-922e-7369d09830c2 | -7.2594 | -50.154301 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfd2912-5288-3601-a6b5-92df60e37e8d | -12.9925 | -45.190498 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc7dc7a8-75e6-3956-add2-c7de4b1f9e06 | -6.7477 | -41.556 | 2025-08-19 00:34:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a34449a-f73c-3124-a777-35e1cfbeda10 | -5.8831 | -48.113899 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f62e411-ff82-34d3-bcc9-a9f50b0c3fff | -5.9235 | -46.002201 | 2025-08-19 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
