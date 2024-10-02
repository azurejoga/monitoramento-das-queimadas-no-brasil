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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6964bf3-3800-3fdd-aa57-c45891f20387 | -9.9367 | -64.9179 | 2024-10-02 01:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 145.5 |
| f5f83d31-eb7e-3ae4-be02-427cabd4fe0f | -9.9368 | -64.8991 | 2024-10-02 01:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| d4c5a268-4523-33d8-ac11-cca08c48d4db | -9.9553 | -64.9172 | 2024-10-02 01:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.5 |
| c30f63ed-6ed6-387d-98bc-c4b67a83c690 | -9.9554 | -64.8984 | 2024-10-02 01:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 30462b0b-51f8-3a70-8752-b56b04e774c1 | -10.626 | -55.8752 | 2024-10-02 01:36:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 05025fe7-0ee4-3667-9669-7e8f9b240b75 | -11.884 | -43.8142 | 2024-10-02 01:36:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 3fae66fa-7e5c-3c8f-97b2-4fd278dfd921 | -11.6554 | -65.018 | 2024-10-02 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e0199b70-f809-372d-a494-14d5205e8aac | -11.6555 | -64.9991 | 2024-10-02 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a67d1dd9-4745-3ab5-9eaa-4fb4050b8623 | -11.6556 | -64.9802 | 2024-10-02 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4f950a39-f23d-35ea-ac77-e9c6ac096c1b | -11.6742 | -65.0172 | 2024-10-02 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| dc5a99fb-a32e-3af7-9377-dab3e92be61d | -11.6743 | -64.9983 | 2024-10-02 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 40ea5da3-bedd-3cd4-987f-c1b5613a1a01 | -12.4433 | -43.7242 | 2024-10-02 01:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1a3ab7c7-a5ba-3dc1-9f10-34fdaf53014b | -12.2946 | -47.6446 | 2024-10-02 01:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a5c1a1a0-8bcf-3754-85d9-09283bff72d5 | -12.6484 | -63.1214 | 2024-10-02 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.1 |
| ff276dd6-26c0-30b1-9756-8c9e60ec4e88 | -12.6486 | -63.1022 | 2024-10-02 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4fa1d438-e951-36fe-aceb-786e6ab50b47 | -12.7054 | -63.0798 | 2024-10-02 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| aa3dc3a2-7e42-356d-9270-1a6fa2da35a1 | -12.8593 | -62.7826 | 2024-10-02 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7f50a0db-9790-33c4-9249-90fd348f9a4c | -13.198 | -48.6267 | 2024-10-02 01:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 135628fd-8019-368c-853c-2f85e2474dc4 | -13.2173 | -48.624 | 2024-10-02 01:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 53fdd80d-695a-30eb-94a9-33d09944366d | -13.2177 | -48.6019 | 2024-10-02 01:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5fe909ab-89d8-3d24-9256-3d1b5ac19649 | -13.0738 | -51.4376 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 33e9011d-4948-3cbe-87e2-8bcefee75a1e | -13.0742 | -51.4163 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8b36e7b8-d975-3008-a956-e7e3fece5892 | -13.0927 | -51.4566 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 5c208caa-a9c5-3c05-b242-36131b6ebd3f | -13.093 | -51.4352 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 412.8 |
| a89b49a9-4a6e-3db9-b11a-294c371bf824 | -13.0933 | -51.4139 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| dcd99bc7-707d-3a8d-939d-58148c7a44fb | -13.1122 | -51.4329 | 2024-10-02 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1c344591-5e49-3a04-8a6f-b649b893f2b0 | -13.5965 | -51.1367 | 2024-10-02 01:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c961f4fa-cc15-380c-8a3e-402295623294 | -14.5699 | -44.8351 | 2024-10-02 01:36:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 83065084-3817-3ccf-8548-4f5e08af9662 | -15.8933 | -57.1754 | 2024-10-02 01:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b07631f7-e8d1-395e-a6c7-184fe29feda3 | -16.1086 | -53.5427 | 2024-10-02 01:36:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 277f1261-1773-34fc-b4eb-ddc7aa882344 | -16.4536 | -57.4188 | 2024-10-02 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 5649fe01-434a-35f5-a605-af9a28b17b73 | -16.6884 | -57.3718 | 2024-10-02 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 3b7af975-3765-315c-a27a-576b01a445c1 | -16.6887 | -57.3513 | 2024-10-02 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.8 |
| 0b495be1-8506-3bb2-870c-ba6a16905746 | -16.689 | -57.3309 | 2024-10-02 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.8 |
| bec688a1-5140-325e-a94c-23b2da30cb2e | -16.7082 | -57.3491 | 2024-10-02 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| c44ee9ae-68cd-3a3e-922e-eca90f0dd8c8 | -16.7086 | -57.3286 | 2024-10-02 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| b2757968-5b00-3b32-95d8-f243e21b1560 | -16.7265 | -57.4287 | 2024-10-02 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| ae7f8cd0-866d-3310-a15e-04165ea43da5 | -16.7269 | -57.4083 | 2024-10-02 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 33e2baeb-f811-38d4-b7af-f622c4839644 | -16.7452 | -57.4878 | 2024-10-02 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| ac7f1fe3-801f-3321-aa08-baa1c82b36ad | -16.7461 | -57.4265 | 2024-10-02 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 0070b8ef-84ab-38a7-8c3f-d044cefe6059 | -16.7647 | -57.4856 | 2024-10-02 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| b921a63d-67bf-361f-860c-68e530b3e4f2 | -16.8096 | -55.9177 | 2024-10-02 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 690d7785-98da-360a-b02a-6ee933640644 | -16.8292 | -55.9152 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 69626422-f818-3ba9-ad9a-8b8e38bf3ea9 | -16.8295 | -55.8945 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| c0453cef-7166-3ad0-adfa-008a53b437ff | -16.8299 | -55.8737 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 9325766e-8501-3365-8659-c11ab0bf3a34 | -16.8234 | -57.4789 | 2024-10-02 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| cf31a136-56d1-3378-b5c7-35cbd2c7e940 | -16.8488 | -55.9128 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 79968e5c-6b56-36f7-8383-077827cacb34 | -16.8491 | -55.892 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 5c307609-5a94-3c16-8665-6aa40b5ee2bd | -16.8695 | -55.848 | 2024-10-02 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| e5df17e2-fc9d-345d-9a44-5ec2851bb40e | -17.0502 | -56.7551 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 684ebe35-566a-3335-a676-03bff6426bcc | -17.0705 | -56.7114 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 4077a91c-3cc2-325e-8924-20ebb3aeeef0 | -17.0709 | -56.6908 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 2751a177-e8e2-361a-afdc-8562ac8c30f8 | -17.0892 | -56.7709 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| f95656a3-3b68-3079-8d75-2cc8ea717851 | -17.0895 | -56.7503 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 2819b224-448f-353a-ad77-e523b9895b7f | -17.1091 | -56.7479 | 2024-10-02 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| c5d281c7-d2fb-308c-8d7a-749a5345783a | -17.1577 | -56.1844 | 2024-10-02 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 0381f5bb-4232-3ad5-b7f6-be1805f1be78 | -17.1581 | -56.1637 | 2024-10-02 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 852ed513-d4a9-3c9d-8882-b735a7cf771e | -17.196 | -56.2417 | 2024-10-02 01:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 56d501a8-ba5f-3198-a4fd-058081b0df37 | -17.1964 | -56.2209 | 2024-10-02 01:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 39bb2e61-a78c-3ca3-a162-b69d1a85e4ee | -19.2317 | -46.8687 | 2024-10-02 01:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 53f505e3-a821-3056-af28-c67ba83b9bf7 | -19.2323 | -46.8452 | 2024-10-02 01:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b1857d95-ca30-3b4e-93d2-fb9035cf30f9 | -19.2519 | -46.8641 | 2024-10-02 01:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 707d82c4-7ce5-3ed5-ad34-5bb3edb8db56 | -20.0238 | -42.7271 | 2024-10-02 01:36:56 | GOES-16 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| 629279f8-0303-3c62-9c7d-756152732588 | -20.0424 | -55.9738 | 2024-10-02 01:36:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 6537e4c9-3846-3c76-95b4-d59b99b2168b | -20.5266 | -46.2783 | 2024-10-02 01:36:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 0ac49440-745d-3e6f-bd38-85b5b46cb36b | -20.6699 | -51.4641 | 2024-10-02 01:37:00 | GOES-16 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| a671419c-1f04-3124-a394-ace6e9f379db | -21.3456 | -55.6841 | 2024-10-02 01:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ec2f9228-535f-3c03-8dae-a96f808bdc77 | -22.3713 | -49.3011 | 2024-10-02 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 240.2 |
| 5ecc13e9-5ba2-3b4c-b3fd-f17abc973375 | -22.372 | -49.2777 | 2024-10-02 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 260.6 |
| ac12daec-d9d1-332b-bded-05ad0d3b02ca | -22.3916 | -49.3194 | 2024-10-02 01:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| 44802976-b4b8-3cfe-b031-92dbfe823094 | -22.3922 | -49.2961 | 2024-10-02 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 335.1 |
| 9d9b44e0-0b18-38b7-a836-34b8f47bf03b | -22.3929 | -49.2727 | 2024-10-02 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.1 |
| 36fcae2b-8b5c-3928-8a14-000cff506cd6 | -22.9277 | -43.7243 | 2024-10-02 01:37:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| 3620f5cb-55dd-3dde-9433-f5c2ebaf89c5 | -22.9006 | -45.1029 | 2024-10-02 01:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| 8d5a7e1a-9e73-3cf3-afee-c4708333538d | -22.9014 | -45.0779 | 2024-10-02 01:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |
| 320dd0af-158e-3f4a-ab52-752b0eb59a1f | -2.6679 | -54.6168 | 2024-10-02 01:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 22630e77-711c-36b8-946d-4598cdc4b563 | -2.9014 | -50.7142 | 2024-10-02 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| bac8ff81-d6af-3446-8f94-4b7e6d42676e | -3.2136 | -46.7843 | 2024-10-02 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 115ea579-2761-3fb9-9e83-2956121c5ee6 | -4.4657 | -42.8877 | 2024-10-02 01:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b1b79413-8432-336f-a56b-fb6df38ffd72 | -7.1796 | -46.9444 | 2024-10-02 01:45:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 66bc1cc7-b6d4-3d64-8daa-302c5e4971ca | -8.4643 | -62.7124 | 2024-10-02 01:45:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 506db88e-7d16-3928-a04e-b17277d9b4c0 | -9.5584 | -62.7997 | 2024-10-02 01:46:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e92049a9-a1b6-3a04-9926-81c5713f1a3a | -9.9367 | -64.9179 | 2024-10-02 01:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 2b6f895b-cc67-3e50-b18c-651a0a3acb47 | -9.9368 | -64.8991 | 2024-10-02 01:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 0d19f5ce-0a25-3243-add8-3a71717dce59 | -9.9553 | -64.9172 | 2024-10-02 01:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 131.5 |
| e8dd2672-d2f6-322c-b9a2-c6e316316442 | -9.9554 | -64.8984 | 2024-10-02 01:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 625a1526-b3ff-34c9-b15b-834a3e506988 | -11.6554 | -65.018 | 2024-10-02 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 389743a3-bf7f-3fdc-8008-818e1462bc7d | -11.6555 | -64.9991 | 2024-10-02 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 496279ce-b11e-32ef-b21a-2b1a1cbac9f2 | -11.6556 | -64.9802 | 2024-10-02 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e8606a4c-0f83-31a2-a8b6-907d61929c1d | -11.6742 | -65.0172 | 2024-10-02 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 810593c8-ae9b-3abc-a8b8-eb5bc4fb697f | -11.6743 | -64.9983 | 2024-10-02 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 89feee52-7843-3caf-90ce-3cd76b6bd45c | -12.4433 | -43.7242 | 2024-10-02 01:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| be51251f-8a05-31e4-ac13-79c95b92cc29 | -12.2946 | -47.6446 | 2024-10-02 01:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 7ffbf849-c6d2-37e3-af69-0ceb5cf58c25 | -12.6484 | -63.1214 | 2024-10-02 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 1d2fca73-98a9-3fa4-90c4-cd1b1bdd2f4a | -12.6486 | -63.1022 | 2024-10-02 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 26a4405c-a573-3ff4-91c6-ffce18c00764 | -12.7054 | -63.0798 | 2024-10-02 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b5bfedf2-d7c1-388b-a44c-dae2b726c53a | -12.8593 | -62.7826 | 2024-10-02 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7b5c87be-54af-3bff-9bd5-0bf3c04c2019 | -13.2173 | -48.624 | 2024-10-02 01:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d75ef1ed-fe4e-35ce-ab08-bfc253d4b775 | -13.2177 | -48.6019 | 2024-10-02 01:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| aad4845b-7f43-3e9b-bf62-ce481580824c | -12.9357 | -62.701 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 150.6 |


[Clique aqui para ver as próximas entradas](README40.md)
