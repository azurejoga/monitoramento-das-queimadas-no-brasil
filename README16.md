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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a38c3ec-e373-31b1-8207-c947e3e68d9a | -2.03622 | -47.04227 | 2025-11-13 04:12:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6296b30b-b4d6-37b0-95b6-b5eb2324961f | -3.3636 | -48.40834 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7d8220d-3f47-31ab-bd36-c4fa91bbda5b | -5.60721 | -41.06841 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75750cad-e2df-3870-b2c4-3e75e64bbbc5 | -5.64854 | -41.0786 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f3eebb15-d661-30e7-b6db-af999e46ea83 | -2.72098 | -47.40907 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 056158d2-559a-3874-bb14-58163d116397 | -4.63815 | -48.747 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86842892-b5d3-3f76-951c-2a1d85fbd811 | -2.89017 | -48.08146 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a13bb55-63c7-3974-8ef6-d8c16948d78b | -3.09092 | -49.26452 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b08a905-0a20-3865-9cd1-4e316b9a8414 | -4.75436 | -48.83434 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96ad736e-87a4-3aa6-9528-e2d6b521ca48 | -3.08861 | -49.27883 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6662a51f-c464-3119-89c3-09d96cb8674b | -3.5694 | -41.72843 | 2025-11-13 04:12:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 530912c3-0d30-3fa8-b9e6-864015b132be | -4.1091 | -48.01068 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d4051b9-3e67-3a4c-8f32-c6ed5e770834 | -3.35021 | -48.381 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4ccd03b-9d37-35c4-8ea7-60201293e345 | -4.44764 | -38.39458 | 2025-11-13 04:12:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a6f51a6-f03b-3c8a-8e98-7dc9c805a9f1 | -3.20919 | -50.19545 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a31fce3-cf2d-30b2-9a69-b04cb0369fd4 | -0.99527 | -48.09105 | 2025-11-13 04:12:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22f59b12-aa83-33ef-a1d1-7eb3c7ec7796 | -4.24274 | -49.67913 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f84d1c-8415-396e-930b-94704f893835 | -4.72252 | -46.44864 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f522a7b4-ca3d-362d-9eb5-8bb5ef4f4593 | -3.09861 | -49.27554 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04689013-a801-316b-92bd-bd6231f4623a | -3.21502 | -50.19068 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92084511-6004-3c94-a6cc-08100c89b8d5 | -4.25262 | -43.78802 | 2025-11-13 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e827b5d9-dce2-3a00-aeba-7a8076a195a7 | -4.0093 | -48.80387 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ae71b48-01f9-3060-aeb2-c31dd1efd0e7 | -2.45619 | -49.26561 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec9ad0ef-4c1b-3bf2-ae58-f0e568d7baa6 | -4.37813 | -46.39465 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 854a7c3d-3354-3e21-949b-c6f020aaed30 | -3.75131 | -40.81944 | 2025-11-13 04:12:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 099db0d1-a069-3cf9-bd43-e7465e5b869d | -5.09306 | -47.46461 | 2025-11-13 04:12:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 157183b6-bf13-3d68-85d8-6e8b0eabd92c | -2.17425 | -48.36909 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bcfb155-12ce-3869-b04c-baabd0f2f976 | -5.09702 | -47.46524 | 2025-11-13 04:12:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c886e74-332a-3741-96f0-7f356caa304c | -5.59478 | -41.08145 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42bc4880-1974-30dc-bbb8-207dfc976489 | -2.87122 | -51.47377 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf2696f8-2ac1-379f-a212-ec88b72df589 | -4.76051 | -44.46066 | 2025-11-13 04:12:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9494fbe-fa7c-3413-946a-be81fabb2a0a | -3.15566 | -45.81172 | 2025-11-13 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc169459-7571-3476-85cd-e05ad62c816a | -1.14345 | -45.71362 | 2025-11-13 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14b14bc5-4c4f-30ae-b0ed-7ce0c9b1a507 | -4.70828 | -46.44176 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d6ae492-6260-39dc-8a2a-2ac9ac0142e9 | -4.21912 | -42.44748 | 2025-11-13 04:12:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df6cd9ef-1c93-3225-b2d8-c30ae7e2351e | -2.97243 | -47.89632 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 055fb029-a4da-3acb-9c9f-eca59cb15df3 | -6.10018 | -41.58954 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5d8d9dfa-f1d2-3754-add8-fc9f785c4182 | -5.61456 | -41.06581 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7c2f36af-a5dc-3b9a-b1b4-faf6dcadbc18 | -5.59986 | -41.07105 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b2f7639-ca44-3019-a494-7ae0f2f26846 | -3.39768 | -41.14832 | 2025-11-13 04:12:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd977fd6-43f3-377b-a6e3-bf92d5e1490b | -4.73106 | -46.73093 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57538bcc-3aee-3992-b1c3-67a405eb21cd | -2.55455 | -51.24791 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 520c6f4a-5913-319d-a4f4-d54f905f13ca | -4.53375 | -43.38836 | 2025-11-13 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e0152f-6e83-349d-a27d-b277e0488f6f | -6.38201 | -39.49116 | 2025-11-13 04:12:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4803a142-92ed-321f-bec1-2ea03c95b0bc | -4.53912 | -46.57529 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5a4015a-9f12-3fcc-8492-1dbaab225741 | -1.93506 | -52.09561 | 2025-11-13 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32338074-64ba-3053-93d5-fed1be7c09b3 | -4.20575 | -47.80807 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46a7ee32-342d-31de-8b30-5e684e6faddc | -2.63136 | -52.08492 | 2025-11-13 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abb2c9d5-8ef9-3975-be5b-1896788bb434 | -5.84023 | -38.34833 | 2025-11-13 04:12:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 6f2be163-762c-3cc8-8a81-286475612154 | -5.61124 | -37.94264 | 2025-11-13 04:12:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e18ea88a-ba05-36f0-a5c7-3c624e9e05c0 | -2.87064 | -51.47717 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 099d5110-2904-3f27-8432-2f798dba8250 | -5.60778 | -41.06479 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c434110-dd76-3c87-b084-687be4b7e70b | -3.15854 | -49.16634 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd432fba-ab88-33c8-8fb3-946941f7ccdb | -6.10025 | -41.61143 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b1309ee9-a868-394f-a3d8-f440357b530f | -2.29038 | -47.87507 | 2025-11-13 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fd739a5-778a-3b80-9c2e-d5e1ef098256 | -4.62471 | -42.78951 | 2025-11-13 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 59a56890-a995-3d6f-9048-70d5aec652cd | -5.61574 | -41.06604 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e680a27-f7e9-3665-b71a-6ad884de5e66 | -2.8116 | -48.72512 | 2025-11-13 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744c390f-a5c3-3250-a262-e565850e9ecf | -2.85619 | -51.27896 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ba5a950-0c15-3d51-b32a-4bbbee2471c5 | -5.16049 | -44.65976 | 2025-11-13 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f20600fc-2f44-3342-b5ee-318a61fe8c53 | -5.8027 | -40.80294 | 2025-11-13 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a588306a-5af7-364e-89a0-a09de7a71f04 | -5.32671 | -45.19831 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 69c3c7ff-a7fc-3f7e-aea2-48828e517066 | -4.33349 | -41.97524 | 2025-11-13 04:12:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49850902-8b7b-38f6-833c-b4b8f4a792f3 | -4.77582 | -42.71494 | 2025-11-13 04:12:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a8f9dac-68d2-3b5c-a0e9-fa88e9666431 | -4.26792 | -42.11341 | 2025-11-13 04:12:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d9b77f65-c336-3529-9123-6714a82e1471 | -6.10518 | -41.57932 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df03f60f-1e9a-3cf6-9ec5-9fa41b7dc81c | -4.10848 | -48.01446 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 162b6013-3a5b-3d80-8a62-1c4984dc89b3 | -3.14972 | -50.26927 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 789e3f6a-d458-3711-9618-20b546f33ade | -3.34458 | -48.3884 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 85e74a49-74d8-3ff7-9430-587bd928e5df | -3.45583 | -44.15957 | 2025-11-13 04:12:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b831299b-3c37-3782-a7df-ae2874100bcf | -3.4437 | -45.58268 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9e79f818-783e-3f82-8c6f-8749113905d2 | -5.03983 | -41.10822 | 2025-11-13 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b81f45ec-0fc1-375e-a511-e75a187aabca | -3.58372 | -41.72352 | 2025-11-13 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ffa8d5cc-ffd6-3858-bca9-bde7ad560f3d | -2.90198 | -48.06283 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfbc48fd-06c2-3063-8bf4-3fd3376b4396 | -2.63061 | -49.19992 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e9ab58d-08b3-3b3f-a973-0a5ddf80cc56 | -2.45001 | -49.26217 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09fbecad-fbcf-3bf0-a558-1516fee12454 | -5.33022 | -44.78521 | 2025-11-13 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbf6b146-f995-342c-a323-e860563194d2 | -3.09903 | -49.2684 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c4db0cf-8f57-38ff-9324-e36ad04cb2f1 | -3.4394 | -45.58632 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9257d7ae-60b6-3e09-bb86-bed2ca303497 | -4.25598 | -43.78855 | 2025-11-13 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d09f2c9-2097-3a62-8783-ccf56b895ffa | -5.89775 | -42.26289 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 82b95356-caee-3a1e-87c7-d9121f58287a | -4.55755 | -45.77665 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4c5aff0-8186-3c94-825d-7743e9893785 | -5.02462 | -46.83463 | 2025-11-13 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e6ea744-c7de-3923-825e-ceed7f9cc754 | -4.71577 | -46.44291 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| f10f425e-f66d-3b2f-94fc-0c48762e1118 | -5.32963 | -44.78897 | 2025-11-13 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd298f64-31a6-33ed-a10e-8508b833956e | -2.45696 | -49.26072 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d23f7a1a-7cbc-3a87-b45e-d9118767f27f | -5.02523 | -46.8362 | 2025-11-13 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90e7658f-982c-3dca-8e9d-654c03c3b65b | -4.66255 | -48.15415 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 152791f2-e566-312f-a910-8a1dde563c2c | -4.24352 | -49.67431 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59e94ed2-8e3c-3deb-9f0b-d88d7d263710 | -4.57615 | -46.93735 | 2025-11-13 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62029ebd-56d5-3eeb-a477-a9bd67044a34 | -2.55491 | -49.11571 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37bf569e-ace2-3e5a-994c-63d897edb817 | -3.48737 | -44.04818 | 2025-11-13 04:12:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48f34bd7-867a-3db3-9d79-d2759f7d26f0 | -4.24254 | -48.38401 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6dbf09-0792-3811-b81d-373984af75bf | -3.47567 | -39.05234 | 2025-11-13 04:12:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c79b7940-34ce-3241-8a26-381f31126b7d | -6.09083 | -41.62816 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 557d1542-bc99-3d2e-b493-73cf498cd34c | -6.10073 | -41.58596 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 192c6a9a-cd13-3f6d-814e-c8bbf5eea57d | -3.46953 | -43.18831 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3ad14f8-59b4-3293-a969-814ca2b344f0 | -2.4554 | -49.27054 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d579eed2-6aea-365f-9f83-5e65fa03bcf8 | -4.89446 | -48.97013 | 2025-11-13 04:12:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb0d6fd6-1e12-37a8-ac35-b2b184996e31 | -4.84232 | -42.37656 | 2025-11-13 04:12:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
