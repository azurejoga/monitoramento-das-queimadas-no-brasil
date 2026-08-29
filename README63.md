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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb07461b-162e-3487-a64c-ee724ec2d9e4 | -8.66229 | -62.84464 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713e5b74-278b-3d15-a086-d9c7222a34a9 | -8.15216 | -64.00291 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be5c264b-569d-3aff-ad75-d5a4ba60867f | -14.91135 | -52.62778 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82d6ed52-74d0-3192-8d19-a15c70a6fe91 | -8.9494 | -63.28284 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c5fd78ae-3793-36dc-b592-09728afcb275 | -8.60437 | -54.77819 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3dbd90b-cf4a-38a1-b970-4345ca5f912d | -9.91905 | -60.43095 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f00ac4f4-5a48-3f20-b6f3-a4b698c599eb | -9.61017 | -55.1291 | 2026-08-29 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6a2cb386-8273-3240-ba5d-985d1e249ef4 | -8.95179 | -62.40826 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb6c8043-56d7-3129-b304-21ec8b6ab2cb | -11.04136 | -57.24584 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b88026d-65a5-3c3d-94e6-98ab9f04e4f3 | -8.53332 | -55.26417 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfbdc1ee-a5c8-3d80-b5d0-f65774c7062a | -11.26047 | -54.01733 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1b3169f-bae4-3017-a1ed-127ad9a8e258 | -8.95329 | -63.2798 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82550030-40a6-3881-a57a-c248e3c9912a | -9.38388 | -66.52213 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c1eebb-66d7-3fe4-810f-2a217cfc188f | -8.59943 | -70.20721 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9481bca4-beba-376c-a716-83da866247fe | -9.40135 | -55.97707 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6faef815-3af8-3a97-a518-7c0967d9acc6 | -14.90379 | -56.338 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03dd1a03-84e5-30f6-8017-d57c7a0206fb | -9.22373 | -59.77066 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4457a02-a06f-3a87-9b5a-5a4ba24ab72d | -8.14858 | -64.00231 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 791f0c82-1324-3100-887a-5ab63d309349 | -8.79321 | -62.48442 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aed4cc19-3644-3995-94e1-16c5c4d42dab | -8.81995 | -62.33121 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48139663-8028-3866-9bc5-ea8c4cb59e0f | -14.91446 | -52.6208 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ed03d84-5795-3e3f-9424-bdd6ae2bc740 | -8.5308 | -55.36007 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 422509c4-f55f-38e7-94cf-8cd9f49a838b | -11.71041 | -54.54139 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5391d89-4bb4-32e9-a5a8-a50734d20f5a | -11.02698 | -57.24383 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06b8cfd5-47a7-3a98-b390-9dda247138ad | -9.87594 | -65.02698 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6dffd31-9f12-3044-bded-ab2cd63b3fc8 | -10.28815 | -62.81838 | 2026-08-29 05:38:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb4dcae8-e6db-3a2d-bc61-0d7a104e68f8 | -8.90226 | -71.39767 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bef1bea8-4072-318d-9f48-6bbf90f554d4 | -14.91842 | -56.33117 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5efb391-eaba-3346-93d8-dd268c6af04a | -15.12148 | -53.58062 | 2026-08-29 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 01c756bb-1478-34a4-92ac-c47f50aa9653 | -9.25052 | -65.49589 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d638299-3c40-3e48-85fb-4e396604d7d8 | -7.55691 | -61.41735 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01b25296-b086-3b13-bcb6-83f050bf6bdc | -8.94659 | -63.27877 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8ce3d873-8dc7-3991-a14b-88b3e1e4a12a | -11.72223 | -54.53775 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af72e86e-4271-3e8b-a2f9-09fea745d159 | -8.68257 | -62.84777 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0aa3041-a765-3c2e-accb-5eba9b06880a | -9.92985 | -60.43732 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5577f063-f745-3965-9479-a8957cd15811 | -11.71693 | -54.53288 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d15acbe-7b90-37ba-808d-f961a9a28e37 | -8.95438 | -63.27266 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3cd0bcdf-e5ed-3f19-8351-4bfb3d1dab5e | -8.00012 | -61.40662 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38103435-0523-323c-b4f0-799502de1836 | -14.90045 | -52.62396 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee0f158f-7cf7-3cbd-8bbd-0d5b6503e830 | -7.57234 | -61.3871 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3c9bef17-5b99-3700-9369-ca8d98b59f40 | -14.92303 | -56.33882 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc53410c-4a7c-3698-8aad-78ab34d57e65 | -9.53463 | -67.43491 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b025d4-e7ac-3083-857c-106a565049eb | -7.82252 | -69.99731 | 2026-08-29 05:38:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8c80ae8-14b2-34af-8497-3b481052aaa5 | -8.60578 | -54.77315 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57c41831-e876-3ecc-9734-de65b16c40bb | -8.24773 | -70.10447 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b63b5b-421e-38dd-91c5-6ab63e533f85 | -8.59807 | -70.21513 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cd0adfe-6f94-3333-ae3d-e990f181293a | -14.89788 | -52.62548 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da101056-423f-3c5a-b4d2-55eed85a096d | -9.04666 | -65.43017 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 704b220c-eeac-3f9e-b5c4-5a1e58128602 | -9.50998 | -65.57799 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51dd8fcc-b617-391c-86eb-029c57679220 | -11.26293 | -54.02346 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141833e5-ca8c-367e-9d00-28e9c1bb926c | -8.60532 | -54.7768 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6349906c-84d2-3ea9-9918-7a012d5b9c14 | -9.87263 | -65.02645 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be77cf67-9330-34e8-bf33-ffd98bb62c26 | -8.50239 | -55.33398 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e807fc52-6b9f-3c32-8be8-468401d33002 | -8.95634 | -62.40126 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cca2041-e044-32cc-8330-cb6b6cf2cbb0 | -9.87587 | -60.30468 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43a367e6-214f-39cb-b5f8-dcca8fd5758f | -9.0461 | -65.43371 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a412800f-2a9a-390f-bd03-a74455f06a17 | -8.95235 | -62.40451 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3cfc6b-44c5-3451-aee2-3f12fa03034d | -9.88981 | -66.99522 | 2026-08-29 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70a8676-c4f4-3333-b83b-aa4065049023 | -9.02435 | -70.91528 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5e6be38-6243-3678-9aff-fd992f9178df | -11.04073 | -57.21355 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14810840-ad7a-33a3-8901-2c53308125af | -9.92602 | -60.43679 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 357369c0-46a1-3f2a-9e91-1232d69c116f | -9.20802 | -51.54626 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4807b3a2-095b-32ec-8fe5-395c2c1f46ec | -8.95664 | -63.28032 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 939dbde5-af9e-39a1-a02d-2b5102196457 | -11.72297 | -54.5346 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5478cab1-0062-3949-a0d6-401643eef1af | -9.18826 | -65.52605 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 770782a6-fe2d-33df-8d98-f864cf1e98f2 | -10.08106 | -62.30422 | 2026-08-29 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3753bb7c-d464-3cc3-972c-a47d47304546 | -9.30429 | -56.80172 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbeb0167-8911-3115-aaa0-d29ca2c9cb80 | -9.86159 | -65.03186 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e89de1f6-382d-3932-9954-1c83540736cc | -8.99336 | -65.44708 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16b3439c-a189-3b17-9523-aaac5180b1b2 | -11.04413 | -57.22488 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ec5e60f-3ab4-3c36-a9b6-b59615abd90e | -8.93134 | -62.40533 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d3156e9-5f09-3900-a698-ee433600d7c7 | -8.53204 | -55.26646 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23222bdb-7d4d-3ece-8895-e299e9fb2572 | -9.13697 | -61.01412 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3be7aee7-1c5b-3142-9977-70176aa9f22d | -14.91281 | -56.30745 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 152c588d-1449-358d-a16a-0630cf00f223 | -9.94032 | -67.80673 | 2026-08-29 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e406fb5-c4db-38c4-b2d1-515f35eaebfc | -11.27924 | -54.03932 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 208139b2-0a73-3fe9-96d8-61d600a22aeb | -10.50916 | -59.63002 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8582d667-d784-3824-ac18-9b0943a47c30 | -11.24162 | -53.99807 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac04bb6a-658a-364f-a39b-f3c08a452ba0 | -8.82518 | -70.63144 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8a2f24c-3e98-3237-b2b9-02c8d56f9ba6 | -9.86887 | -60.29875 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50487110-33f8-303d-a4fd-ff98c1056199 | -11.26836 | -54.02888 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53ef3b17-a29e-3032-929a-3660d0bc79bd | -8.95858 | -62.3862 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbf5dca-0e17-33fd-b406-f13c9683948e | -14.90419 | -56.33453 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da6545d0-d75b-3f42-acb5-86a1973f6779 | -8.65554 | -62.84359 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c41a20cb-3d84-3260-a4c3-75cce6bfe84d | -8.94714 | -63.27519 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c1a53698-5759-36ec-b0a8-94c0a9b71634 | -11.19182 | -55.10627 | 2026-08-29 05:38:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d20125c-4e4d-3c87-bbb2-8ba4e3f7651a | -10.48609 | -64.49477 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 055299bd-7e41-3676-9772-732de600eee5 | -9.86502 | -60.29815 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8c0410f-2338-3463-a87b-44190e62f018 | -8.95683 | -62.37437 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9e76921-2384-32c9-ad92-4053b0e50d03 | -9.38792 | -66.51893 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9c342d5-6959-3d88-9927-5a2ff443c89d | -8.99891 | -65.45525 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d63ec112-bb3a-3ed7-8122-c647894d9396 | -10.4655 | -64.49503 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2242bc6f-f977-306d-88bf-527013a49a5b | -9.92917 | -60.44208 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdf73596-6f49-3619-842f-bc5d58d27bf9 | -11.04624 | -57.20882 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df5f935d-d2e1-3389-bf24-04562b6b11b8 | -9.10205 | -68.62328 | 2026-08-29 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3507cb0-f8f8-3856-a85f-72b7770cf635 | -9.93052 | -60.4326 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c3a2892-481d-3b6c-ab5f-788914df161e | -14.47014 | -58.52438 | 2026-08-29 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcc8a033-3540-33d0-9d2e-4412d55ddeac | -10.28776 | -62.82151 | 2026-08-29 05:38:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a812d12-229c-3764-85fa-19959a840d51 | -11.26344 | -54.01903 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5179a32f-3160-3c66-ba04-76e5509aa6e3 | -6.924 | -69.99542 | 2026-08-29 05:38:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README64.md)
