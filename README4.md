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
| aec7c7a6-1fcf-3b77-9b0d-c9b5c3f6ef59 | -2.9392 | -40.40052 | 2026-01-10 03:17:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b8e3d32b-ef5d-3eab-a7c9-e4a6481d194b | -7.74985 | -35.25093 | 2026-01-10 03:17:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5d8300e3-dc65-341e-80e0-16171edb97f8 | -5.17592 | -37.76059 | 2026-01-10 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41a16e01-51c9-31fb-83d4-d3bcdbd720b5 | -5.47832 | -39.66 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ec7622a3-86a2-3946-873c-482efd513a24 | -9.68498 | -37.10483 | 2026-01-10 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56e46a10-e4a4-36f3-bd91-bc249a6a6164 | -15.2574 | -59.8521 | 2026-01-10 03:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1f6a4623-4204-326a-beb0-9b0c2c284f93 | -12.3754 | -58.0521 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3192bebf-5ee4-30a5-9d27-84d34add03e1 | -12.3946 | -58.0307 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 5f78798a-a361-31ea-b202-255e47f73382 | -12.4135 | -58.0292 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 038a8d03-1d8c-3f65-bd43-b72ac25279aa | -12.3943 | -58.0506 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 0fef24ec-e821-3fdb-8282-cbe20194bd1b | -12.4133 | -58.049 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 55ce551f-59a5-3fe6-929b-0310d3be2fa8 | -12.3756 | -58.0322 | 2026-01-10 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 729b78ee-6335-3af6-a2ea-26976d6f99ab | -12.3946 | -58.0307 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 0a899d0a-d15c-3a87-a829-f4a0bfb62c6e | -12.3756 | -58.0322 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9aec3b70-71e4-39e9-b79a-4baee87ab00b | -12.3754 | -58.0521 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2b51f94f-f594-3667-9368-1919683c4d32 | -12.4135 | -58.0292 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 807943dc-f359-3fe4-83fb-d6ea4a54ccc6 | -12.4133 | -58.049 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ace3ca74-19e0-34fa-a339-d31166059c08 | -12.3943 | -58.0506 | 2026-01-10 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 92682d20-81d9-3077-bb52-43ec8f2b44ca | -1.70495 | -45.80994 | 2026-01-10 03:36:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dae69708-c819-37ba-ba08-6c924641140d | -6.55243 | -35.29723 | 2026-01-10 03:36:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b7e43acf-3a6a-3573-ba6d-a5e715272335 | -4.52126 | -38.61824 | 2026-01-10 03:36:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 370b74e3-f254-36df-adbb-b3327cf7a60b | -4.68298 | -38.16331 | 2026-01-10 03:36:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2aabe31f-75b4-3b2a-b730-85a21a0af4e2 | -2.78626 | -43.34873 | 2026-01-10 03:36:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a25c499-4fa9-3f30-a392-0eb7a59ae0e0 | -4.10583 | -38.20016 | 2026-01-10 03:36:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc269879-a189-3f2d-8671-6a5124f7c265 | -5.60595 | -39.82253 | 2026-01-10 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f78d083-4167-3808-8a5f-b99f5ec840a0 | -5.70209 | -39.86891 | 2026-01-10 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1529066d-5b48-393b-ad3d-8a0f25f04806 | -5.88921 | -39.29217 | 2026-01-10 03:36:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5e97aeb5-2a0f-3289-bf9f-3ce4c3be40b1 | -5.48131 | -39.65365 | 2026-01-10 03:36:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebbe1cf7-e371-3d0e-8f68-8425f111a231 | -5.1004 | -37.64717 | 2026-01-10 03:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8f54a1a-f3b9-33a8-b015-098ef7aced9d | -5.47631 | -39.65688 | 2026-01-10 03:36:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c489fde0-26d2-3c8f-ae87-0751fd4344a6 | -6.34347 | -37.65707 | 2026-01-10 03:36:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b73d5582-857a-3e83-90c1-30e87f06937e | -5.47563 | -39.66089 | 2026-01-10 03:36:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 792d741d-f29a-3162-9812-672bc8aa0a32 | -6.34271 | -37.6616 | 2026-01-10 03:36:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f02c65db-eaf4-3ee0-865d-4b217f2f3042 | -2.93616 | -40.39753 | 2026-01-10 03:36:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 77d6d794-7f3c-3c2e-91f7-8e8366da7151 | -1.70385 | -45.81636 | 2026-01-10 03:36:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd409256-da36-356d-842f-0729f203a8b1 | -1.697 | -45.81515 | 2026-01-10 03:36:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be1219b7-3ad9-3c1a-84fa-ec08df52345c | -7.10888 | -35.1317 | 2026-01-10 03:36:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad5f3495-1fa7-35b2-b8b9-7cd5fced619a | -1.70314 | -45.81958 | 2026-01-10 03:36:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 153d382f-ccaf-3358-9e0b-6362ab73938c | -5.91521 | -42.28269 | 2026-01-10 03:36:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a646f240-a2cf-3ee9-9190-4c76ade22544 | -6.24387 | -35.29646 | 2026-01-10 03:36:00 | NOAA-20 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d0e42b5b-b8c5-31b2-87f5-8ce32ec6afd0 | -2.78556 | -43.35283 | 2026-01-10 03:36:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6a8c152-1c22-362e-978f-b7dec96cb716 | -3.97157 | -42.49908 | 2026-01-10 03:36:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc1eb25c-cb3b-3e20-9d33-c67bfa50400c | -5.6293 | -35.30395 | 2026-01-10 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ae12439b-d28e-37fb-be53-9f3228176fe9 | -6.3397 | -37.65647 | 2026-01-10 03:36:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9c82a6df-c588-3106-bb5d-d1b7652a857c | -6.73598 | -35.48625 | 2026-01-10 03:36:00 | NOAA-20 | SERRA DA RAIZ | PARAÍBA | Brasil | 2515609 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9338e6bf-dfd9-358a-857c-f846b6376b89 | -5.17412 | -37.76443 | 2026-01-10 03:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f655eae0-d6ec-317a-8c6d-f2110f0caaa0 | -6.09342 | -35.23137 | 2026-01-10 03:36:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 975d2034-c244-3cb8-a1b1-eea95cd253d4 | -5.70147 | -39.87263 | 2026-01-10 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9c250b1-9159-332a-85ef-fcbd4bdac422 | -1.70421 | -45.81306 | 2026-01-10 03:36:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 387c511b-ea00-318a-b0a0-1f030e1231e0 | -2.78641 | -43.35041 | 2026-01-10 03:36:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96df500a-e375-362a-88ab-0b0e251d741b | -3.87302 | -40.34619 | 2026-01-10 03:36:00 | NOAA-20 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ceebb6c-3128-3f97-92f8-802c900b0df5 | -3.60506 | -41.59085 | 2026-01-10 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 052ab039-254e-396e-971d-e85e3aea7bb7 | -5.62989 | -35.30029 | 2026-01-10 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4600ff6a-c922-3b75-823e-3f0022dd2825 | -5.48062 | -39.65775 | 2026-01-10 03:36:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 82039c9c-92ff-3a4a-ae64-ba9b3a3f08e3 | -3.60457 | -41.59384 | 2026-01-10 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de2eff1d-e35d-30b8-8759-c41d4ac22f28 | -5.60663 | -39.81847 | 2026-01-10 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5030ea7b-ba39-396f-a1df-744080fa1a66 | -3.60259 | -41.59215 | 2026-01-10 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db44e2aa-f70d-317b-b5c5-16bffee1195f | -5.75476 | -39.79939 | 2026-01-10 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39205fb7-865d-33eb-a6cf-d52d4119ee2e | -5.75313 | -35.38397 | 2026-01-10 03:36:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bce3a3ff-6e9e-305f-a082-4551ea3fa410 | -5.92143 | -42.27739 | 2026-01-10 03:36:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6e512a3-cc0b-30b7-b686-c5e71e39e918 | -3.64183 | -42.02182 | 2026-01-10 03:36:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3986974e-9c29-379a-bf81-ead6bc9d0b00 | -3.78376 | -40.97337 | 2026-01-10 03:36:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69a26081-392d-3933-86a3-facef6121696 | -3.64709 | -42.02266 | 2026-01-10 03:36:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1901931d-d591-31f8-9903-5bfffb6f339e | -3.97215 | -42.49564 | 2026-01-10 03:36:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79075b7a-74e8-3177-bde1-a45b39f63842 | -5.91574 | -42.27966 | 2026-01-10 03:36:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eff5f91b-24d1-3af3-86db-a1323a4ac376 | -4.38478 | -40.75508 | 2026-01-10 03:36:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72488439-72e6-32a5-ac80-6b1a5e670535 | -5.57546 | -36.25526 | 2026-01-10 03:36:00 | NOAA-20 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1190b1e9-7238-3844-9561-3c27c8d6264b | -2.93728 | -40.39499 | 2026-01-10 03:36:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 13ee0bac-2ec2-39fe-8472-c0231143610d | -6.09003 | -35.23082 | 2026-01-10 03:36:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0c5a29f-946c-3e99-b56e-7e746eb765fe | -6.55185 | -35.30087 | 2026-01-10 03:36:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0f7f6bf3-5339-3741-a605-77f11f7af316 | -5.1749 | -37.75965 | 2026-01-10 03:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1d7034e-bf1c-3ea1-b7a3-4c6e0a981e36 | -3.60207 | -41.59516 | 2026-01-10 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cddb792-2054-3add-82cf-a16cbb4b4a4e | -5.5488 | -35.82008 | 2026-01-10 03:36:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59cec76a-275a-3088-aea1-3d51d1cfc644 | -5.5748 | -36.25925 | 2026-01-10 03:36:00 | NOAA-20 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c0fa34c4-b19f-3ffa-a132-0e6c28f7fcd7 | -7.70902 | -35.10003 | 2026-01-10 03:38:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f84b3f5d-ce94-3b89-8f05-5ae748866554 | -6.74215 | -38.35049 | 2026-01-10 03:38:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f0e3994b-e1b2-330e-846a-ea84e1adca24 | -7.49068 | -45.56749 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70cadb0d-fefc-30e6-a50c-da7dd4a1aaec | -9.17076 | -40.91696 | 2026-01-10 03:38:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3a61d9bb-55c9-338e-a94b-92fd19def1f4 | -7.4861 | -45.59225 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d33604a4-6edb-3f59-ad14-2041f880a4c5 | -7.70958 | -35.09648 | 2026-01-10 03:38:00 | NOAA-20 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9ab135cd-b2b4-32cd-bb8a-c3268c8bb4c7 | -8.55612 | -40.58272 | 2026-01-10 03:38:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ebd7fb3-5df3-32d2-84fb-1b7d01b8e0e2 | -11.17256 | -43.30693 | 2026-01-10 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e9bc712-6112-3bea-ba76-faf8c71e7279 | -11.82931 | -46.61501 | 2026-01-10 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 726bc3a7-684d-3caf-96c5-ecdd5bf161cf | -11.82945 | -46.61832 | 2026-01-10 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c102fd1-4248-3290-9edb-3617062bd148 | -7.39719 | -35.19553 | 2026-01-10 03:38:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e9b3032b-a52d-3f0b-8c5f-f7e9c2db64db | -8.18405 | -43.5745 | 2026-01-10 03:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04171c9c-5ea3-35a0-89a9-667ae48d5de8 | -11.95578 | -44.21223 | 2026-01-10 03:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ceb7a0b-5ade-33ad-8c82-fed324fa53d1 | -10.59575 | -38.41009 | 2026-01-10 03:38:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4098fdc4-4a6f-35bb-a718-e238a6a3f692 | -7.48886 | -45.57731 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52daecde-215d-3718-ac74-64e3eb76902f | -10.48686 | -44.93026 | 2026-01-10 03:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cae5256-adcf-322a-9126-a6e612e0e6c5 | -11.83045 | -46.6133 | 2026-01-10 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 801b7bc7-cdf9-3204-a428-6b788469463a | -7.48795 | -45.58223 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11a58e00-4350-39eb-8f9a-ccfa307e19a8 | -9.42607 | -40.35775 | 2026-01-10 03:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df4db295-c48a-358f-a6be-08071288986e | -8.1834 | -43.57808 | 2026-01-10 03:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e63ea3e-cd6d-3cc3-a98b-7fc538a93726 | -6.74133 | -38.35292 | 2026-01-10 03:38:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4ae28f5a-af10-31eb-902e-d19c8e28823c | -7.71293 | -35.09702 | 2026-01-10 03:38:00 | NOAA-20 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c76a7a7b-75f6-3bf7-b1b4-92af5a2aa021 | -7.49413 | -45.58347 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb5289eb-1a06-3d14-8a01-a61b487cccd6 | -7.49229 | -45.59347 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5579380b-43e1-31df-9d4f-6c73fb32ceb0 | -7.10683 | -35.68794 | 2026-01-10 03:38:00 | NOAA-20 | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b3447a1-a853-3f28-87de-329a5007559c | -12.29242 | -38.98138 | 2026-01-10 03:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
