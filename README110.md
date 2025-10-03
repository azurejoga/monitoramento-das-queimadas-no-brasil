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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95395cf4-bf70-3a76-a8b2-e54af12a2f05 | -15.5832 | -46.91707 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fba3733b-ccec-3bc8-844c-a21ab0a5973a | -14.98392 | -49.96783 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 194b6ddb-1750-347f-b803-ca20b44674a8 | -13.25601 | -48.42778 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3adb5150-09b2-357d-9e48-65bf28758b07 | -12.93193 | -48.43819 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61586aeb-7d48-377e-b55b-a475578d7cef | -15.46388 | -51.56086 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68a8a06c-23ec-349c-b541-122d288fd7f4 | -13.21271 | -48.53107 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 914d890d-62bc-3a37-9c4e-affab41aa701 | -14.23026 | -46.12437 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1836e01-5f53-3fae-843a-aa7f50615cdd | -15.28025 | -47.91818 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f87a77d-a42b-3803-805a-bf6efb830777 | -12.90911 | -46.91199 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e9ed869-d03c-3b65-8211-f1c3710c393a | -13.30296 | -47.8302 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8edba3a-e753-3513-9d49-d77f8cfda6f9 | -13.96447 | -44.86763 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6f7403-d3c3-3d0b-996a-af33d744dfd0 | -14.89812 | -46.96569 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 68856655-3686-3cdb-9f57-7d01ca4a7184 | -18.1617 | -53.34216 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db542fe8-a887-3424-9fd6-d5f33c272c07 | -13.15716 | -47.89357 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7134d98e-07ff-30f4-8e74-b5a29727cb1d | -14.9882 | -46.86777 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e018f95-296b-34f7-9fbe-15df9401d9b9 | -14.89193 | -46.98228 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fe0aed7-e835-324e-a771-60fc84474eec | -12.51107 | -46.84046 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0821664-bd1c-3f50-a2e3-c2e67c04f96b | -15.24692 | -50.12908 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f344615e-043a-3f9a-b1f2-fe0171250903 | -18.31567 | -44.039 | 2025-10-03 04:34:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6990fd-dc8f-3a55-98f1-fb01156e8d42 | -18.20061 | -53.30669 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73059a1b-4c2a-3df3-ac61-8289407d28aa | -15.92271 | -43.33481 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4658bd63-cfd4-3ab1-8671-0788199911d6 | -14.87059 | -48.33726 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63385d1a-55a9-3f3d-ac15-8cbb62b583b8 | -13.13806 | -47.88308 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1560a51-e41a-3d72-9815-43f7bcb30ed6 | -15.98717 | -46.59024 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea307ce4-035e-34e1-9fc9-b2b5c8cc35eb | -16.33248 | -49.94376 | 2025-10-03 04:34:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9552dbc4-4b2c-35fd-99df-a23f2ff48ddc | -14.72502 | -48.09475 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b5808e-9a20-3931-964a-90a1fec8df41 | -14.74206 | -48.1277 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 102210ff-5f0d-3bd4-b944-8036c80fc8ec | -17.98806 | -45.02492 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98fae754-ecab-3414-ac15-2af6b9c0324a | -15.84727 | -46.23734 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59b315f9-36e0-307c-953f-cd87812060a6 | -13.77267 | -47.56893 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97b59584-51de-36f6-9945-8192bed9fafb | -14.7314 | -48.12953 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b2bc48e-478f-31c2-83bc-935d408608b3 | -14.74044 | -48.13849 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eddf5fbd-c6b1-339c-9f28-138ee64bbb10 | -13.74357 | -48.01398 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5fcd95-1428-330d-9649-33bc077d3a7e | -14.59808 | -46.72315 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c12dd1-9059-37e5-b429-994f35daf4b5 | -14.6732 | -48.09395 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3825a4ab-c06a-3f20-adc0-a6263c41d3b6 | -13.76586 | -48.05856 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 094ae3f8-7a86-3126-bda6-8b4273fef416 | -12.19386 | -47.8072 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11421913-3fc2-383f-99bb-8a3eda2768ec | -14.19317 | -46.07069 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1323d6de-e02f-323c-a4fd-da7a098235b6 | -14.19931 | -46.05372 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 53c7516f-5347-3e24-bd8b-b080a0a074b3 | -14.90871 | -46.96729 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84aa4e56-c4b3-3586-a372-10988b52ee49 | -14.93163 | -46.90836 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 75d58a61-eacd-3dd8-96c7-c95899cb1000 | -19.89783 | -44.51145 | 2025-10-03 04:34:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 250c4d61-ee04-327f-86f1-03d588a15167 | -12.61746 | -46.97205 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3065d2c7-ee8d-391c-b2ac-8d13b35f1c3f | -16.03507 | -50.93166 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b92e906-8e70-3d35-bc30-43f1ffcdc355 | -15.80277 | -46.25876 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b6dc2a3-a4c6-3b41-90ca-880fbf5ea212 | -14.80887 | -51.42572 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fdcb24d3-87e5-34f5-8870-329e1f8b65d3 | -14.74029 | -48.09331 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2d9bf16-07d0-3df0-8ffb-c71dc9850c91 | -16.27179 | -47.09879 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec5fb8a1-ac1e-3493-8f6c-638a486cefbb | -13.2965 | -46.98296 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf8d0af6-f415-3499-a05c-8a3deddde17a | -17.90488 | -46.84061 | 2025-10-03 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1976a55a-2c4e-3828-a4f4-621c97b11366 | -12.93416 | -48.44583 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09313f21-0a42-37ac-99a3-dd16024f7674 | -14.87865 | -47.44387 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b379046a-c0e5-31c5-b247-bbb4238f58a6 | -13.32644 | -47.60574 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4cc15e4-3cb9-362c-9a5d-6164787ef621 | -13.26512 | -47.26672 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3092df47-3a6c-3471-ad2a-94fc79cd6ae5 | -17.16449 | -47.02222 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32286aee-552b-33df-8864-0056bfb7bc99 | -13.14526 | -47.83525 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb561fa2-b2df-32b7-9f1a-d97b4c0865dc | -13.48159 | -47.24499 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ee3710d-91f7-341c-9e0c-1eb5e0274c80 | -13.52292 | -47.25143 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37f2c8c-5515-3d3e-899e-0032acdeb8de | -15.28785 | -49.30892 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 873d4aa9-58d7-3967-8927-bb5684590b88 | -13.53501 | -47.28824 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2b181be-8dca-3b10-85a4-852a6c65d73e | -16.03174 | -50.9311 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1458f89-de67-346e-9ea7-41501461cea9 | -13.32822 | -47.8004 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b6e98f5-4060-3a71-849a-8a7c45ada03b | -13.32485 | -47.79986 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c525df-8bbb-3dce-a634-88a82a080d1d | -15.29941 | -46.28888 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca9b663d-22fb-3d89-b456-da14600d28b9 | -15.25125 | -48.08762 | 2025-10-03 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59916a01-6e66-3af6-962d-633f1b3df47b | -18.195 | -53.29699 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d74ff2ef-9581-33f3-acae-d6c33baf2f05 | -13.63554 | -48.67164 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9debbd5-32d3-3451-9598-0b51a0bb115b | -13.14369 | -47.8915 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc4ddf28-d25d-3fe8-8352-f5ca89d680ff | -18.45072 | -43.81482 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1495987e-4195-33eb-bfb7-102b10c9fca4 | -13.27166 | -46.94787 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aeb57783-39a3-3787-8b9b-6c9039166f41 | -12.38016 | -46.51173 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88d7a2f4-27b7-3d6c-a7b0-b86ea51cb621 | -14.44045 | -46.37917 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b2fbe2-6e61-35f7-936d-5aa436a58008 | -13.21841 | -50.87777 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9693c6d7-f544-3e17-8c37-f89aff10d95b | -13.34322 | -48.09738 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b33e4db-491c-3a8d-afda-8ae213dc7f38 | -18.40894 | -50.7725 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d31c6d11-68ef-3868-9eab-136b54278676 | -14.59046 | -48.34506 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bc80e98-66b1-3faa-8730-ab6cb530af38 | -13.13095 | -47.89716 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 819a87f0-a16a-3922-a780-4533ceacf4f0 | -12.20056 | -47.78576 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d96c40f5-3951-3772-9782-b72005f4e69f | -19.59093 | -45.89793 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb469463-78d9-3ea0-94f4-a8957f1acba1 | -13.34887 | -48.12804 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95610f6b-fdc7-3ad8-ad7b-e3aabf43ffdd | -12.65611 | -46.89344 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e6577da-8c92-35fe-861d-7ea95a4bffbe | -14.36636 | -46.1112 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26f537b8-3868-31fd-abc6-0065e35d7bec | -19.72688 | -44.8962 | 2025-10-03 04:34:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a990cfb1-c1a9-3be8-917a-eb7926abef9f | -18.15598 | -46.11322 | 2025-10-03 04:34:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4a4d69c-701d-31e1-aed6-b596d8f2f5ae | -15.99665 | -50.89906 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d06dedc9-bfd5-36e4-a316-095f256379f6 | -15.99136 | -50.86823 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee130201-d449-31d9-b8cd-04b0d5a1fb87 | -13.38633 | -48.13026 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc68304-0771-33e6-be13-7d5f15628e7c | -13.81338 | -51.31195 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ef2567-835a-3e3d-bda6-9e5ad1f0eaed | -13.27596 | -47.26474 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81fcfc8d-a039-398c-b33c-6f3bf989df37 | -16.34993 | -47.10494 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5f83fd9-ac63-3b3d-a93f-bcadc7e56b25 | -12.65111 | -46.99881 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bffc1d5e-eef9-3b0c-afd5-bf436b11bc0e | -14.83061 | -51.7385 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33566c27-20f4-31e9-90ed-75c57a6cd923 | -17.06216 | -46.63224 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28eca85-1ca0-3e9b-9a70-0795def15d2b | -13.75533 | -47.98212 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f11e7afc-ace5-3dde-b99b-ca5ad71bd71c | -14.65699 | -48.29225 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e396909b-ee90-3d77-be54-3982bc361a3b | -18.24142 | -53.3235 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 984f4259-c44b-31c2-a564-e8105b7eccee | -18.44982 | -43.71311 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be72548f-af99-3cab-a4f1-1dad5b5efa6d | -13.93531 | -48.08931 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8c98e28-6709-39a2-b79d-256fa9cfad76 | -15.27512 | -49.32516 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6738deaa-3c0f-3e70-ae67-49a4ee0f5e5c | -16.92992 | -54.14851 | 2025-10-03 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README111.md)
