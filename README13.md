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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 535a368d-f63e-3806-b880-0c08e64c77da | -20.7238 | -56.65621 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 26547249-c176-3898-838a-1c49eb356982 | -20.38538 | -47.18989 | 2025-07-03 04:12:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcceeccc-989d-34ae-8eb7-6c111a1e5a08 | -20.31273 | -45.58257 | 2025-07-03 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f5b7d7f-e346-3634-ab82-650029913545 | -18.21272 | -51.35369 | 2025-07-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0408d483-0258-3bf0-8e56-44adcc43a62e | -22.74462 | -47.13993 | 2025-07-03 04:12:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc8af34f-b232-3937-b0a4-c89e51a01a41 | -27.32323 | -48.58531 | 2025-07-03 04:14:00 | NOAA-21 | GOVERNADOR CELSO RAMOS | SANTA CATARINA | Brasil | 4206009 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 006c1d01-e8d8-341f-9778-889baf0bbe24 | -6.9602 | -42.9052 | 2025-07-03 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| d345d84f-4e47-382b-91cc-984a90fe5444 | -6.9793 | -42.8798 | 2025-07-03 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 6252d7f2-0cbe-3c0b-b2ee-e6bebc5228f2 | -5.9938 | -43.7366 | 2025-07-03 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 44fd3de3-9f8a-31f0-9ac0-4a8589b92fce | -11.6588 | -44.5974 | 2025-07-03 04:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2f3ce609-f6de-3b60-ac9d-899c77f1b7b6 | -6.2945 | -43.6659 | 2025-07-03 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a33bc689-1e11-32ef-b7cc-037b92caad01 | -7.2219 | -43.0682 | 2025-07-03 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 8aa46746-08f4-3912-9da2-7752d98a4ff6 | -6.9605 | -42.8816 | 2025-07-03 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 319.2 |
| 9b255aeb-775c-38fa-a85a-84ca2bc5210e | -6.9416 | -42.8834 | 2025-07-03 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| d44c3d5b-178b-3146-9ded-86fb766b42fa | -6.2943 | -43.6891 | 2025-07-03 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4cbf5425-b3c7-30fc-846a-75d621513995 | -6.2945 | -43.6659 | 2025-07-03 04:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 195a7068-e614-359b-99a2-17b187eb94be | -11.6588 | -44.5974 | 2025-07-03 04:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8f7405e2-1784-3c09-a91e-ff647c143a0c | -6.9602 | -42.9052 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 35fde940-d79b-337f-8ce4-a5b090a7c7f7 | -6.9793 | -42.8798 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 6375bc42-62c3-3c3a-99cf-52e86eeb4237 | -6.9607 | -42.858 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 7553f676-83e4-3294-87a8-d690fb242dfb | -6.9416 | -42.8834 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| e4a1eca5-f2a5-3a01-adcd-374e82fefbf8 | -7.2219 | -43.0682 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| f9ba2448-6bea-3bce-bbfe-68fdeea200c7 | -5.9938 | -43.7366 | 2025-07-03 04:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 139867fa-f2de-3b67-ab6a-311f5e61cb12 | -6.9605 | -42.8816 | 2025-07-03 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 293.5 |
| 6c89c2c8-b595-34c9-ad66-174ece268b7d | -6.19702 | -42.64554 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0acd1c31-afed-3963-8a56-1b5fbc561008 | -6.02306 | -49.22804 | 2025-07-03 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a427861-c011-3df8-aaa3-389b5923fe02 | -6.19621 | -42.64211 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 21fabdaa-cfbb-3138-be06-061f41cee307 | -6.96943 | -42.8788 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48bf0b7a-92b0-3698-a720-ad55873c834e | -3.08025 | -52.43085 | 2025-07-03 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6c05f5d-1bfc-3aa1-bfca-4b4e0249109a | -9.51591 | -45.43902 | 2025-07-03 04:34:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed20a90-c847-39dd-8e75-5c76a7ac77ee | -2.90878 | -54.48849 | 2025-07-03 04:34:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 057fcbb2-18bb-3310-bfeb-aac9d1e3eb43 | -4.49059 | -50.50285 | 2025-07-03 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa7dad7-b34b-3e71-843c-fc2fe0327a5c | -6.01967 | -49.2275 | 2025-07-03 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f19d44a-edbe-321d-8054-d81db0e6753d | -5.91901 | -43.44884 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3aee96e-e7f6-3db7-b1da-73d163e8fa37 | -8.86039 | -47.95119 | 2025-07-03 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b373708-7783-38dd-b137-5b3f892df71a | -6.30024 | -43.67734 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8c356b82-c619-3115-9d4a-e7227cf99418 | -6.2964 | -43.67674 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3da98dac-e2c2-3223-99cb-7e0d5541d190 | -5.99842 | -43.74301 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 31887bc5-ddc5-34c9-b588-86f08cbbe7b7 | -6.02364 | -49.22443 | 2025-07-03 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31da622-d567-34dc-8d31-df4b80f2b3a0 | -6.95314 | -42.87642 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 547da977-655f-3f44-acdd-d73d64b7c039 | -6.20731 | -43.36465 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27a47048-8b43-3877-9cd0-c5c2566aed3e | -6.95668 | -42.88065 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 2f924a6e-1d5c-3fdd-bf45-d6d542b3c156 | -2.91055 | -48.24047 | 2025-07-03 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 360f1456-1d5e-37ef-a172-3d78f9bab8bd | -7.19376 | -43.0969 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9f0adaf8-746d-3da5-877b-6b408bdb6383 | -7.61525 | -45.75029 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| db67b503-2823-39c8-b57c-3db8c58cb49d | -6.21193 | -43.36035 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a3242f-c583-37da-9a77-c6c3e701ec1a | -5.92172 | -43.48342 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3d74b161-a067-335d-bfaf-3a86b2f6317f | -7.2274 | -43.06554 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| da14b200-5e00-36c1-bf1b-325abdbb2db1 | -7.36571 | -43.86711 | 2025-07-03 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f073e47-6816-3183-a9a7-3b16341a0adc | -7.09428 | -44.39339 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aea36be9-e9b2-37d3-85f7-216b44df847d | -7.19428 | -43.09341 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 093057ec-c97d-3c31-b407-e551966e0abb | -7.90179 | -44.53581 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edc120e8-3671-3828-9c4c-9db4f2d73ea4 | -7.86021 | -47.88282 | 2025-07-03 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e43013-cbc6-3504-a110-b768f38cc103 | -7.23496 | -43.07032 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 92df3020-e1ca-3c2b-a1b4-7e82d4eccb38 | -7.40257 | -45.41784 | 2025-07-03 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac52d5a2-8f27-30bd-b149-fe56211ad0cc | -5.91785 | -43.48287 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b790269f-b494-3dae-81ca-2360f14ef2ba | -8.58369 | -49.8816 | 2025-07-03 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aac281e-5819-37b5-8a63-7356a16091a4 | -6.18092 | -42.61361 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8ab35588-0ea1-3a3e-8ad7-f5402a79742e | -7.19883 | -43.09052 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0228f0c4-f56c-3d2e-a70e-9ece417061d0 | -4.42001 | -47.66223 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 668e25a1-e51e-3756-aecc-52c4e3b2e651 | -6.33629 | -43.74987 | 2025-07-03 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70102948-0d63-3744-95d2-58aeabc1bbaf | -7.0912 | -44.38857 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f925616a-40d9-34c5-ae5f-9795eac45309 | -7.22388 | -43.06137 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 985e659c-3955-3ec0-b6fc-20af39052f39 | -7.57024 | -43.99448 | 2025-07-03 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09ff22e4-1a74-3ed0-9791-01500ec9c818 | -5.819 | -42.62055 | 2025-07-03 04:34:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d56f5684-e63e-32a7-ad1f-c86c2d620270 | -7.61467 | -45.75416 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16dfd14f-55d3-3c28-b284-1dfe6b650be3 | -8.62828 | -50.0388 | 2025-07-03 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 064d570b-364b-33bb-b2ae-05e611e5e3de | -6.5902 | -43.0362 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee206edd-c323-3981-b809-05a7db2f1087 | -7.84128 | -46.87053 | 2025-07-03 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3435e6f6-7172-3dc2-8159-61e7c585bec2 | -6.68887 | -43.15574 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 12.3 |
| bab11e49-3d83-39af-9d1f-46d58b5884c2 | -6.60173 | -43.04133 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e29c3bcd-a5c3-3cc7-9d1d-a47ac5b92029 | -6.21121 | -43.36528 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9714886f-1b72-35da-8014-beed6d778999 | -7.4411 | -44.44423 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da558e16-0e3f-380e-8331-7e1d8358f3ee | -7.19831 | -43.09402 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 514355b9-9c96-310d-a984-b2155762c519 | -6.72244 | -43.17645 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31751be7-e15e-360f-ae9c-ba5159b61995 | -6.17224 | -48.05287 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9402fe97-9b76-3c0d-ab3b-916f4ea7d857 | -6.72168 | -43.18159 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96e8b2ac-9deb-3a47-98c5-67bd51fa5297 | -6.7255 | -43.15591 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84a705a4-055a-37a6-a973-ce4df0015c98 | -8.58428 | -49.87796 | 2025-07-03 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea651158-7a87-3bef-9a6e-c6d5c4523b9f | -7.70281 | -46.04607 | 2025-07-03 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e538e9b8-93f5-33a8-a346-2b77e0be5065 | -2.89555 | -48.03206 | 2025-07-03 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f29c367-60b0-3759-acc1-ee64e4967e7b | -9.83666 | -44.67799 | 2025-07-03 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86be90b4-1123-3b28-949c-b66bfd21f51f | -5.62388 | -44.2664 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46de4545-5b77-3741-89b3-47f509a71469 | -6.17888 | -48.05392 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ef72427-68e7-32c0-acc7-6557d3e66d08 | -9.1742 | -48.77423 | 2025-07-03 04:34:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3951395c-ba27-3b15-8690-8fc9949be9dc | -8.43916 | -49.19966 | 2025-07-03 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cbba61d-d02f-3f5f-b69e-00938d4291ac | -7.85412 | -47.87828 | 2025-07-03 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec26fdb3-6981-38fb-b9fd-00d33432aa93 | -5.31437 | -47.48453 | 2025-07-03 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a90bdc12-2776-345f-95da-eb83d9b0ead8 | -7.20286 | -43.09113 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36b6a16c-7cb9-3c42-aa7b-e4ade6baa859 | -6.72929 | -46.31935 | 2025-07-03 04:34:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bae307c-eb19-3e76-91a2-97278e5fdf2a | -9.11017 | -47.63693 | 2025-07-03 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75e6bfd7-df6a-339b-94ba-37f31f559017 | -4.53815 | -48.02571 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b28f11b-335e-31f5-8dca-c086a6199842 | -6.69371 | -44.06156 | 2025-07-03 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e2804a8-b392-377e-84dc-d4f970181a8d | -4.53482 | -48.0252 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58214733-d64c-3819-b3f5-4a79198f1f83 | -7.67847 | -44.66301 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f038cec-9f45-3bed-8484-4798008e6f57 | -6.02248 | -49.23166 | 2025-07-03 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9783244e-c2bd-3005-84c6-62061c24a280 | -4.2853 | -48.18917 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 104a9605-41a2-3e10-af5e-34ced875c229 | -8.86696 | -47.27884 | 2025-07-03 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb24463-b736-3041-a715-7dbd68f53421 | -4.38743 | -41.91455 | 2025-07-03 04:34:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79381bf7-a9be-3518-88b5-92da02aeb484 | -8.86559 | -49.03706 | 2025-07-03 04:34:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
