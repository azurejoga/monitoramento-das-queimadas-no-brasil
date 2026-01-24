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
| 32950100-252b-3e97-b96c-378ca51c4885 | -18.81107 | -51.61226 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2d8303a-5d12-3827-866d-d54c0b910d88 | -18.81389 | -51.59721 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f180a32-648a-3eea-8d2b-54cd03673610 | -18.25282 | -51.27734 | 2026-01-24 04:18:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e86ccef-215e-3ec6-92fe-c1a9b400a6fd | -18.76824 | -49.83066 | 2026-01-24 04:18:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ae7f231-e100-35c0-b017-4c1d25b66acf | -18.81514 | -51.61303 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dfaa0fa-90e6-390a-b216-d5c2b693e325 | -14.3072 | -57.59704 | 2026-01-24 04:18:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ed8facd-286b-31e3-baef-88c26b29fd0b | -18.24813 | -51.28021 | 2026-01-24 04:18:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d014c73-9ab6-3947-9e58-4d3e306fdf2d | -18.81249 | -51.60468 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24064f40-30ad-3534-ae40-0b48a2f72dd3 | -18.24879 | -51.27657 | 2026-01-24 04:18:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc1995c8-db04-309b-af0a-9b5b20cb09c6 | -16.44392 | -58.1692 | 2026-01-24 04:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 33f6f8bf-2e59-3a40-9864-5c9a3e3fb20b | -17.08097 | -39.46331 | 2026-01-24 04:18:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4a2ca16-63bc-3600-8a07-0d7c6bccf807 | -18.81726 | -51.60171 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c91fa282-d328-3620-bfd6-9f5c411c39d2 | -18.8185 | -51.61756 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bececdce-d3c3-35b9-af83-a10f6ac2de56 | -16.44582 | -58.16692 | 2026-01-24 04:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 740d98b0-db09-3233-bfbe-94ee6a9396d5 | -18.8132 | -51.60094 | 2026-01-24 04:18:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4caf233-b043-35d7-be23-cc1e03a98303 | -18.25349 | -51.27369 | 2026-01-24 04:18:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5340567d-5784-3b49-9979-d9b39dd9170d | -21.13934 | -48.6678 | 2026-01-24 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 982bff67-ace3-3730-9245-339eda284be6 | -19.67476 | -57.1945 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 58ecf466-5295-3dd1-b1a0-9fab50cd82ba | -21.13933 | -48.66648 | 2026-01-24 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f85f9c57-a8fb-313d-b981-fda54e84e503 | -20.59344 | -48.85738 | 2026-01-24 04:21:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1fd14b7f-3f32-3a4a-8c0e-5a0e87cd6e0f | -20.33868 | -57.85252 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e34a0d4c-509c-3367-a436-dd8f38f9c570 | -21.14 | -48.66385 | 2026-01-24 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f5000e5-4054-39f5-b07e-b124d1f03159 | -21.77961 | -56.28566 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3388f366-49f1-3e09-b688-55d3a863610f | -19.56009 | -54.44207 | 2026-01-24 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38b353b-219b-34f3-8934-0d0851211092 | -20.36178 | -57.85857 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f0caccb3-27e4-385b-94d1-d491403b57cc | -19.66733 | -57.20129 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| d1dc1808-ab98-3739-bb37-1ec0ded81c8f | -20.32714 | -57.84951 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 54532f11-499a-3c61-bf7d-79107a7068df | -20.34546 | -57.84964 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 52dfd893-cc83-3337-a05e-5f2764c5bfd9 | -20.37811 | -57.8675 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 414296a6-c1af-3121-807f-f13851e9edd2 | -20.31458 | -57.85088 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3fcf99a4-1c31-3640-9196-ffe3597f8129 | -23.53351 | -55.50716 | 2026-01-24 04:21:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03b86210-f933-3f2c-b4f4-088ce2f3b518 | -24.6608 | -51.55652 | 2026-01-24 04:21:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cf82c60d-003f-3849-865c-c7091a648ab0 | -20.38768 | -57.87933 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e1f31635-8548-3b20-bc7c-a7ba750a0947 | -20.32254 | -57.84857 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3bb727b6-151c-3581-8c0d-daba99905930 | -20.32036 | -57.85239 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87d0a5b7-27be-3f9e-8f4e-3822a8f6fc65 | -21.13593 | -48.66711 | 2026-01-24 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84b5aead-e514-3dbf-9d27-aaa559330ab9 | -23.60757 | -48.25758 | 2026-01-24 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5753d4-8849-3ec7-ae74-6370b13eefcf | -22.73197 | -49.34394 | 2026-01-24 04:21:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b937f5-6293-3a92-bbb4-3e1f7ad71906 | -22.02468 | -56.33687 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d560566-39ae-363a-98c4-a3519430467a | -20.73077 | -48.81707 | 2026-01-24 04:21:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b68e1c27-b778-3794-97e2-c762c83d2cd0 | -20.45485 | -48.68451 | 2026-01-24 04:21:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a043a6a7-cd49-3f48-a2ff-8c46b0d784d9 | -19.56372 | -54.44874 | 2026-01-24 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48ac9c71-59b4-3716-87d4-4bb111fa94b4 | -20.31579 | -57.85144 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8e785d16-f502-36ab-981b-690e163bb109 | -19.67386 | -57.19862 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 311c1ef2-0a48-3ab6-a3a5-160191b7da71 | -22.0181 | -56.34237 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2279625f-996f-3d22-b5bf-54493512b9af | -20.35601 | -57.85705 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 48b50f73-a658-3f12-a561-be98255bdad6 | -20.34446 | -57.85403 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3357e529-97e6-3ba0-93cc-92d7ef4ae544 | -20.45828 | -48.68518 | 2026-01-24 04:21:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54daf3cd-b033-3710-8b23-b0d52a3b6fe8 | -21.28599 | -48.54806 | 2026-01-24 04:21:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18adc799-f36f-38d0-be9c-e8d71ac30ee5 | -20.36656 | -57.86447 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cf4c084c-5cce-3414-b79f-6e4e6dd26903 | -27.09532 | -50.5293 | 2026-01-24 04:21:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5f114da3-2666-369d-9803-bc1131d0d012 | -22.83527 | -48.65154 | 2026-01-24 04:21:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe3ef03b-9667-31ca-b8a6-6abfa2ed3774 | -19.66823 | -57.19717 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 4a24958e-f18f-3ea6-9be6-d35df71fb973 | -22.01882 | -56.33904 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 438b5ee9-5d89-3976-9b41-1b060495670f | -23.5384 | -55.50906 | 2026-01-24 04:21:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ecd65bfa-dd03-3d97-9bc3-aaaabae6294a | -26.28948 | -48.80786 | 2026-01-24 04:21:00 | NOAA-20 | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1391bc68-73e8-3fce-97bf-734b44f0bad2 | -22.03608 | -49.50441 | 2026-01-24 04:21:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2c3c7fa-ba6e-31c1-8f37-7759bd6dd3bc | -20.72733 | -48.81642 | 2026-01-24 04:21:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9674e659-d8b7-3f03-bdc0-8172c07127b5 | -19.67668 | -57.19461 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 659a292f-a218-3557-8220-e10d9657c200 | -23.6036 | -48.26075 | 2026-01-24 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| adeeb616-4a31-3e9f-ade1-d516d6ba087e | -19.67296 | -57.20273 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d5582ebd-ae84-3d5f-8f28-b91944ce7135 | -27.455 | -48.45258 | 2026-01-24 04:21:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa5a090c-fc0d-393a-af8c-95d2259d27c2 | -23.00529 | -52.38873 | 2026-01-24 04:21:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3902143c-dbc2-379a-957d-74962da62ea6 | -21.13659 | -48.66316 | 2026-01-24 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd474754-9d60-3f40-be96-4aed2632a4e3 | -22.02396 | -56.34018 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52a16703-907d-3360-8e89-06fdf2fe2efd | -23.53822 | -55.50838 | 2026-01-24 04:21:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 464b5d34-9998-3f79-af9a-6be6366e645f | -19.34274 | -54.17247 | 2026-01-24 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2884c300-48e4-3d1b-886b-18e669f88a3d | -20.32136 | -57.848 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b3bb5255-1f25-3db1-810b-62f61d36cfc3 | -23.60631 | -48.26519 | 2026-01-24 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fa148474-df73-3ae6-8038-d3cbe31289a7 | -20.35123 | -57.85115 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| be1c58d1-c4ee-36c3-9806-92a7b64f7367 | -20.3829 | -57.87341 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f8faa7b7-b9a8-3d76-80c2-bd93a0cfd5f9 | -20.45552 | -48.68056 | 2026-01-24 04:21:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7db7cd9a-46f4-3c4f-8a60-7c5418b07457 | -22.02325 | -56.34349 | 2026-01-24 04:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f0ba491-c20a-370c-ac05-e2264e452a97 | -25.41115 | -52.99585 | 2026-01-24 04:21:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3800cd4a-c2d0-314c-b787-1dbaefa7d57f | -23.60694 | -48.26139 | 2026-01-24 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cd7d49e7-dd15-333d-ae6d-0b7bbe6f701d | -20.36755 | -57.86008 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fb3bd287-1a44-35cf-8312-c1e5ef2b2097 | -27.09605 | -50.52508 | 2026-01-24 04:21:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df11ce46-bd85-324e-93ab-3913dd898099 | -20.35023 | -57.85554 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 05bf3362-5395-3e64-9e28-a767bb6aaa95 | -19.68295 | -56.86278 | 2026-01-24 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 23b6b5e2-dc35-31cc-974d-19806573c467 | -20.84395 | -51.73843 | 2026-01-24 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec9a986c-e923-30f1-a453-21929ca5d8b7 | -20.33968 | -57.84814 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6bae3941-79e7-3ec9-b36a-e9d9c16933d0 | -23.60298 | -48.26456 | 2026-01-24 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 89056109-3705-3069-8375-14ff6f34f70b | -22.83864 | -48.6522 | 2026-01-24 04:21:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 545b3f22-72ed-3b3a-9e8c-a26732f62573 | -25.22268 | -52.14641 | 2026-01-24 04:21:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04bb4496-b04d-3e0e-85a7-ce5791d1b052 | -23.00637 | -52.38315 | 2026-01-24 04:21:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 971813eb-4e40-3940-9528-e9a694bcce23 | -20.32157 | -57.85297 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 90925f5c-dc2a-36e6-bf8c-6eb7c8b60d32 | -19.34146 | -54.17634 | 2026-01-24 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 728e7e62-f1c2-3f96-bce2-7dfeda476432 | -20.33291 | -57.85101 | 2026-01-24 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4dcddb75-7ce5-3e24-8533-5a9abc3ba320 | -24.65847 | -51.5583 | 2026-01-24 04:21:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1a7af95-3c11-3b45-9cda-5457aaa449b3 | -30.08994 | -50.79405 | 2026-01-24 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8fcd0990-e23f-30d5-90f9-a0eb2cb5bd93 | -30.05103 | -50.75502 | 2026-01-24 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| d93eb365-9fa5-346f-8ade-7e89b9f20e13 | -29.12024 | -51.1846 | 2026-01-24 04:23:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| abc816bc-cf76-36ad-a335-58537f706e13 | -30.05512 | -50.75161 | 2026-01-24 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| c185dee5-be3e-3773-bfd9-e19b33b0a5fd | -30.0585 | -50.75235 | 2026-01-24 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 73d6348a-54f9-3463-b681-9ed59f8578f2 | -30.05175 | -50.75085 | 2026-01-24 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| fa46376c-459a-3a36-a6c3-59a48e1425ca | -29.11678 | -51.18387 | 2026-01-24 04:23:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61f32488-cfd8-336b-8348-c86b1802a70c | 3.60386 | -60.35971 | 2026-01-24 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb69e48d-eb50-393b-8791-c83a34d4001e | 3.6559 | -60.16744 | 2026-01-24 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a93adf-84df-3c68-8307-3ff51102cecf | 4.00009 | -60.62044 | 2026-01-24 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d781e6ca-9883-361c-bd5b-03e937499881 | 3.23837 | -60.23628 | 2026-01-24 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README5.md)
