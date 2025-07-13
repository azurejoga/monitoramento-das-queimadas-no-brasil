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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 994a80b9-0cb2-3920-b5da-a076d003f255 | -13.13824 | -47.32125 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3caa4e9d-382b-39ee-b8fc-5ee696b635e8 | -12.03003 | -63.78643 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5636d37c-010c-3906-af9d-b3c6660f8568 | -9.85338 | -65.21122 | 2025-07-13 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79d54b99-1159-3c8b-900d-00e4686b86c5 | -13.10917 | -47.29753 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98523a3d-887e-3367-a8f7-3bd3d5b5938d | -10.2785 | -60.53541 | 2025-07-13 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c0ddab6-6b96-37b9-b02d-35336828a973 | -14.17465 | -56.30471 | 2025-07-13 05:12:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d05cf08-6f6f-3010-9f2c-3b435f4a40ed | -14.29571 | -58.65112 | 2025-07-13 05:12:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65fe637e-84da-3077-b7a9-bd99f9a4e878 | -12.44722 | -50.46309 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bef416a-bc96-32cb-b383-7870eeb603ce | -13.83846 | -45.89844 | 2025-07-13 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc8f241e-8d24-31e2-8165-899990bbb54d | -13.14507 | -47.31679 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cba26df-3a8a-379f-91af-95514bcf6fc8 | -13.02577 | -47.82978 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2010e9b-e2cf-3a3c-926f-0e58784337dc | -13.02458 | -47.82789 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e762b996-3441-3f13-b90d-d362563bb43f | -12.1493 | -50.23919 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77d517f9-7b37-3d93-97cd-18b4f8012896 | -13.91505 | -47.41817 | 2025-07-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0612caa-94f8-3be3-9c42-7d460292c0a6 | -17.65575 | -50.48377 | 2025-07-13 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7305e179-4672-380e-bf70-3d438a3afd8a | -17.65035 | -50.4831 | 2025-07-13 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e4ebbd5-b1c0-3f22-b216-91ad6f4cb45e | -12.02145 | -63.78845 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f7b95ab-d392-344e-8ce3-abbf5b062c0b | -13.85048 | -46.89483 | 2025-07-13 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 154be42c-6333-30f8-a0a8-83f907c91e7d | -13.91126 | -47.41855 | 2025-07-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e29ac92-3a23-32da-a109-d2ccd70866e2 | -17.64996 | -50.48671 | 2025-07-13 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d9c101b-1ae8-3a12-9dfd-a03d2850f095 | -9.64499 | -65.74027 | 2025-07-13 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 212fd9eb-af60-34ca-b9a4-f19a17e8b14b | -13.02621 | -47.82579 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdac98a0-d775-326a-95f3-efc656b5e226 | -13.11159 | -47.29685 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e339d577-0f5f-3008-89b2-ccef92fd3b0f | -11.72365 | -57.43871 | 2025-07-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58bce62e-b9d6-3cf6-922b-345ac38369cf | -13.10971 | -47.29258 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c4a1626-c7d7-3280-8142-b27754f2b70e | -13.11058 | -47.30556 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d6c0a37-5c8e-355f-a66c-d4d7719bc6a7 | -12.58179 | -56.97604 | 2025-07-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85c0d552-0cd1-3e1c-bc40-c2912c519da3 | -12.02028 | -63.78478 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6719ae08-96e3-3514-8eaa-d285c33e2603 | -12.02605 | -63.78569 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eeaef02-ae62-3f22-bad0-c48d4dcdd9d9 | -12.01967 | -63.7883 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 896ccd3a-6516-3e03-9490-0b55b40e1ec9 | -12.41654 | -50.46206 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c294cb5-990f-3c90-af4d-357d552e7a8a | -14.31471 | -52.74196 | 2025-07-13 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 394d0502-b4ed-3d8e-ae13-a5c030957300 | -13.10546 | -47.29501 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4241aa6c-3bbc-3d75-8244-86c10704e70f | -10.13812 | -63.23257 | 2025-07-13 05:12:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3edddada-294a-3578-8dc5-02923ac85d9d | -12.0181 | -63.7842 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa43ce79-8d21-3a22-98dd-d1a2823c3414 | -12.11703 | -58.0106 | 2025-07-13 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d2d7e4b-a88e-3bab-a73b-b15b62685e1e | -12.10145 | -63.70674 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fa8127e-fe88-31fb-a4da-f40cd50f8972 | -12.0227 | -63.78143 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1eb6bd-3f32-3f50-8994-aa04b7b88f07 | -14.31916 | -52.74253 | 2025-07-13 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d117c00-3a36-37bc-ba59-f45bfce3266c | -13.83915 | -45.89177 | 2025-07-13 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b1ccc87-2dbb-3a54-80c0-80ab9dfe1f16 | -13.02505 | -47.82388 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d50d0eb0-a9c9-3e8a-8dc1-b9c6f6d56291 | -12.01873 | -63.78068 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53ae5c1d-d854-3746-aabb-3b45ed0464e2 | -13.10498 | -47.2992 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5adeef55-7e00-3f97-a8fc-98e57a193f59 | -12.34919 | -57.42739 | 2025-07-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee906160-e01e-3a88-b872-193c4f023841 | -12.02208 | -63.78494 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58125eef-353d-3c3f-a677-2cbefcad2401 | -12.02543 | -63.7892 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d68484f-33d0-313d-881f-b5b36f54b744 | -13.84983 | -46.90082 | 2025-07-13 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a470c5f6-b34d-3673-8755-c7ff1da18b52 | -13.11223 | -47.29137 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9653ea45-9d87-319f-ad9c-9f54f31fd3ea | -12.42196 | -50.45975 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ab5530-5401-3540-b145-ba3097cc395e | -12.1442 | -50.2385 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 120b30ef-6b90-3298-94e0-16350136e812 | -12.01901 | -49.52494 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce355eca-26b0-3894-8872-bc967c0ac564 | -12.44647 | -50.46905 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f13df4b5-0d6b-36af-82dd-32e95aa314f8 | -15.0529 | -55.8259 | 2025-07-13 05:12:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60272d7a-ce1d-3bae-923e-b9a56295d61a | -12.44759 | -50.46011 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8940adc7-0314-3d4c-a92a-1fff34c029ea | -13.13772 | -47.32591 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f334ba2-99ca-3f40-b028-03c01b069ffc | -12.42738 | -50.45744 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4b06342-a89f-3f4a-b281-6aec939928aa | -11.86242 | -58.70727 | 2025-07-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 965ee4bf-31d7-32ff-9aa3-adf9d8130e13 | -11.86628 | -58.7043 | 2025-07-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7275b0ea-1be0-3619-b51c-3bb928ad02f0 | -17.65536 | -50.4874 | 2025-07-13 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8296b4f5-04d2-32f5-a93e-8976305dcb08 | -12.57895 | -56.97173 | 2025-07-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa8100e6-4aa4-3091-b4f2-05699c7d7fed | -19.08592 | -56.05253 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f8deb637-1471-3618-b311-db95ea2d3daf | -19.0866 | -56.04755 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5e8b1530-afea-3e71-a9f3-2c167777c877 | -19.09347 | -56.0403 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d9286a96-d9af-3620-a949-158cc2ce734a | -19.09111 | -56.04313 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 48a5b671-7b61-32ed-ab72-ffc176a7d8de | -17.68858 | -54.00853 | 2025-07-13 05:14:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c67223d-ba22-3d62-94c9-85d1fcd6cd4d | -20.18772 | -48.82116 | 2025-07-13 05:14:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa77221b-0c6e-3911-9fbc-9d7885be2341 | -17.68807 | -54.01262 | 2025-07-13 05:14:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f86cbbe-584b-381f-a4b1-1f2bc9cc0b27 | -20.18197 | -48.81585 | 2025-07-13 05:14:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2037fc7c-6ceb-396d-8d89-ad7399c5d800 | -19.08343 | -56.042 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 27c7dd4b-b8d4-3346-84c9-da2899dc90a6 | -19.08727 | -56.04256 | 2025-07-13 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3695198c-119a-30f8-b557-aed7a1381e82 | -22.25658 | -54.74118 | 2025-07-13 05:14:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0e91608-2ccc-363b-8ee4-5515bed6555b | -27.50107 | -53.66224 | 2025-07-13 05:16:00 | NOAA-20 | REDENTORA | RIO GRANDE DO SUL | Brasil | 4315404 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| df9ba4b0-43d3-308a-b9eb-66e77a91ee4a | -27.50044 | -53.66349 | 2025-07-13 05:16:00 | NOAA-20 | REDENTORA | RIO GRANDE DO SUL | Brasil | 4315404 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d880f0b1-1db2-3090-ab13-1f8369582cab | -4.28704 | -48.05445 | 2025-07-13 05:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 93644b07-6a5d-3080-be10-fe9b4fe21ed9 | -8.00926 | -50.10302 | 2025-07-13 05:59:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50f47548-bf76-37f9-95c5-487d88e4b203 | -4.53278 | -48.01722 | 2025-07-13 05:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ea7764b0-5262-3aa8-8f52-a094f0f4e605 | -5.74041 | -44.98197 | 2025-07-13 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 43a60497-db29-3396-ba73-b5dbe1f651e0 | -3.61606 | -47.53689 | 2025-07-13 05:59:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb37d2fc-887c-3839-b3cb-09d13f115d93 | -6.12893 | -42.96272 | 2025-07-13 05:59:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 974bd5f6-763f-31e9-975a-bdbc26e96e1e | -8.34769 | -45.64584 | 2025-07-13 05:59:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43d53997-a00b-38a1-bbdc-c1136557e84a | -4.29811 | -48.10182 | 2025-07-13 05:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| f74ae907-7b62-318b-856f-b2c5e42d37a5 | -5.7296 | -44.98047 | 2025-07-13 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b12c8578-97f5-3f6e-8875-fc6d726dc27d | -3.75336 | -47.10481 | 2025-07-13 05:59:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 00b7484c-9066-3373-a62d-c4b4145df24e | -3.61469 | -47.54607 | 2025-07-13 05:59:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e85d5a51-ad8e-39ec-bcc3-f00cc928cbea | -6.94421 | -42.73055 | 2025-07-13 05:59:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 2e2a225f-f84c-34e6-8e6c-918b74b2c458 | -9.39613 | -68.93449 | 2025-07-13 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be55e3cb-6c95-3e94-adcf-8d31bc424e20 | -9.24637 | -64.40443 | 2025-07-13 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d1eb1f5-88b7-3ebb-ad7d-aed2f37e29a3 | -9.85453 | -65.21072 | 2025-07-13 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44deedfd-f660-3a10-b85f-365ccd15f48d | -13.85136 | -46.90287 | 2025-07-13 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f61ef4ef-bc69-36ce-aaca-563b3622e5f7 | -9.92205 | -59.90969 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59659d10-5c16-3669-a3ee-64ea2f433b5a | -9.28976 | -68.25816 | 2025-07-13 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2704ce-5e61-3699-8057-85b9d5016e4c | -7.3828 | -72.6883 | 2025-07-13 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adaf96ca-8b2d-359b-a3dc-d28384deb6c2 | -9.02604 | -61.22931 | 2025-07-13 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abbf8fc5-d4c7-3714-8f20-ec834124501c | -7.38378 | -72.68905 | 2025-07-13 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecc7f17b-54a0-377b-a360-2f7001ed2369 | -7.67357 | -72.32708 | 2025-07-13 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f9c36c-42b3-3b63-887b-ffcbea4e2707 | -9.02104 | -61.22488 | 2025-07-13 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 222e1f51-383d-356e-9193-efbe54a86046 | -9.39669 | -68.93074 | 2025-07-13 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf8ea62a-0685-3f7c-8d78-caa47a83c032 | -10.57391 | -49.12553 | 2025-07-13 06:01:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc276527-a3b2-3364-b7eb-5795f9a8a5db | -7.59628 | -63.47162 | 2025-07-13 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7666ce4f-5e73-3149-8d3a-a34fd6f33c5d | -13.8532 | -46.88911 | 2025-07-13 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |


[Clique aqui para ver as próximas entradas](README16.md)
