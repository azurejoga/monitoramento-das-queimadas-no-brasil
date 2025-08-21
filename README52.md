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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e4b92dc-366d-336b-80d3-afc0d204fa2a | -2.91228 | -48.3045 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4fddf1c-b21d-376e-8739-d9d07fb8c388 | -2.98116 | -60.07922 | 2025-08-21 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 754865c5-b2f7-3926-9ae3-05db4583d3e6 | -4.31363 | -48.09883 | 2025-08-21 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9d7f338-94cb-3777-840f-f21f1f0d5030 | -2.58448 | -51.92354 | 2025-08-21 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46091e20-2cc8-384c-84de-b515e09d1c9c | -3.04236 | -49.44238 | 2025-08-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0d963f1-8d41-3882-a016-ff16b6ff7de7 | -2.919 | -48.30747 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbd95b41-4461-3657-91cf-e5e6f548434d | -2.69988 | -48.21302 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7fba989-7d62-3030-9f66-14f61574d834 | -2.38065 | -47.66011 | 2025-08-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f59e3554-4ed6-36fb-a988-e67bda1ec82c | -2.93722 | -53.69782 | 2025-08-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 680fc174-fdba-373c-80fd-ab5c3ffd82e0 | -2.58995 | -51.92446 | 2025-08-21 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cb381c1-807b-34b6-b472-45e86644068a | -2.91917 | -48.30568 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9444888-4035-3a4d-b0cd-b8fcce0b0c14 | 3.54268 | -60.72624 | 2025-08-21 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e64ae9b-d0be-39c2-8f41-8b48b03c2397 | -2.7002 | -48.2081 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4336421d-dd13-3d21-b9f2-2d5869a892ce | -2.91995 | -48.30104 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0150301e-82b2-3e94-ba1f-acacab57a844 | -2.92009 | -48.29915 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 47bb0040-38f7-3beb-9ce7-4ce05f034649 | -2.91211 | -48.30636 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d69cfcd6-d93c-3e65-b8dc-27a05eafc4f6 | -5.98158 | -61.35896 | 2025-08-21 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d328e4f9-776d-38d8-a6bc-fe90900cf6c6 | -9.15909 | -59.60429 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5a3194-2afe-3880-963b-1748e75e35c1 | -5.33161 | -60.15123 | 2025-08-21 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6d14218-6dcd-3e0a-88fa-9c747739f5e7 | -6.45901 | -53.3832 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56a06c58-a6f0-3738-894d-f7b86c7c4492 | -5.14706 | -60.37434 | 2025-08-21 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a99250e7-1ba5-32e0-87cc-806f53ac4334 | -4.94814 | -55.79113 | 2025-08-21 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6071c5-2b8c-32b3-acda-1068810cf5b6 | -7.05487 | -59.82298 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49d964f3-7cea-3d57-b0fa-aeade1e45a1d | -7.77638 | -66.9519 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b86e7d4f-436c-3763-8fd6-80f745ff374c | -9.20946 | -59.4625 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f29b8a7b-f723-398d-9890-122cc31234ec | -8.86484 | -62.39049 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| be87ebee-03f3-3ccd-a840-128f8e97022e | -5.98212 | -61.35545 | 2025-08-21 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0630dbb5-f686-3b6b-9bc7-e0a597c9f891 | -4.951 | -55.79282 | 2025-08-21 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7c3eb64-8fa0-3b14-9b45-38037e8718c6 | -8.8814 | -62.39308 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cc1b2ce-a572-37e6-8549-db72140433f2 | -8.62132 | -62.14082 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7d4f4ba-d957-37cc-b7f1-ae0b18114f3b | -8.36617 | -54.99678 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abcfd759-7d7f-31db-acb7-ef664ed2fe44 | -7.02599 | -59.68024 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e300ac45-f731-3751-bea4-8b194aae25ba | -7.55642 | -63.85118 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8fd66e0-7ac7-3f27-9681-f995131fc2a9 | -7.54636 | -63.84959 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b3bfe4c-c330-3da5-83dc-d2d5f3ab4401 | -7.56371 | -63.84867 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad5ee865-f712-334e-8e93-83b875782c50 | -8.86322 | -62.40094 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eba7b140-8404-3b7a-aa72-7100fd69d85f | -7.50235 | -63.83156 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ca5fe1d-50ed-3ce0-921e-c8db4e2c6b4e | -5.82379 | -51.68893 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4751d2b-59ff-33c9-9111-0d96b6c9f223 | -8.70342 | -62.88097 | 2025-08-21 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1071af-45e8-3949-84b0-c12e17f49433 | -9.15971 | -59.60003 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97b1d412-3953-3c27-844a-f0a9b24593d1 | -8.69125 | -63.67001 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 886b9f16-ff48-3324-ac13-06df902dbaea | -7.5525 | -63.85423 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08706e0f-dd24-3bd2-886d-acdb9677d14e | -5.4483 | -60.16836 | 2025-08-21 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 757b989c-eafe-34ec-8b3e-0a726cd7d31c | -7.77944 | -66.95736 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b0f828a8-96f5-34e8-8ce3-3bd589f804c9 | -8.67914 | -62.0959 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 451da7e3-9076-3710-8d71-392dae0c5c61 | -6.45421 | -53.37915 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f9dc7a0-64cd-34fe-a381-3cb7cb4cd731 | -6.45946 | -53.37999 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b13a866f-236c-32ad-81d1-4bf53e7dd2e7 | -7.55029 | -63.84654 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e9da26e-34d2-3215-a664-1b59e563ee83 | -7.51298 | -63.82959 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad88a14-0000-3353-8cef-fb5b6d17c853 | -8.86815 | -62.39101 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14d86bf7-5df4-3841-9e1e-bb79eab9725d | -6.93768 | -62.88377 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc9b02a1-e788-3b3d-91b8-a5414e56c48c | -9.1887 | -59.63063 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1460de34-375d-3daa-9e9b-44e1610366ff | -5.88311 | -57.75302 | 2025-08-21 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2fd012a-0a9c-341b-b5bd-eb084d95920f | -8.62742 | -62.14536 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 684be9a4-ee08-326b-b877-6a0a184fd4d0 | -7.5057 | -63.83209 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e7866d7-9fa9-34c2-a371-66ff892b3348 | -8.84128 | -52.05597 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6114f8fa-29c7-3998-8d2a-c3253d024662 | -7.05565 | -59.82197 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7765c0-981b-3105-8999-4948e7c9ffab | -8.8643 | -62.39397 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b6bc5ac1-703d-3e82-b040-af5ac510e888 | -9.18507 | -59.63005 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2be4d570-f6c1-364c-b393-11f927b27e59 | -8.43905 | -63.86497 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0962a96e-f7b4-3535-8e5c-a33a3fdf7c0a | -7.55307 | -63.85065 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76c039b7-c156-3c07-991f-16d854646d88 | -5.44773 | -60.17207 | 2025-08-21 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| def7b9d8-ab63-3e5d-a040-83ca1eea3ddf | -9.22933 | -60.33538 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4540afc2-3f9e-38c7-a115-49ebb104c906 | -6.8852 | -56.47991 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 746d7763-6f03-3b9b-b543-2f4b185f7ce9 | -8.43571 | -63.86444 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 941330d6-2922-33a8-9d54-00a2889d40c8 | -7.55921 | -63.8553 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e57eaf62-43c6-369b-b1d7-9e9af74b6e5f | -8.86653 | -62.40146 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 79092164-5829-35cd-8be3-466db4cfe2d2 | -4.13758 | -54.89782 | 2025-08-21 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cba6dffb-e75d-3b2e-abe3-b5185afabe1a | -4.95249 | -55.79182 | 2025-08-21 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d028b3-2aa3-3ef5-a410-d99708f70e7a | -9.17913 | -59.59431 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3bcab7-80c0-3b77-8f41-2687edb18e86 | -9.21009 | -59.45815 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1273e198-3d14-3eb5-a464-ee5efe920e9a | -8.86761 | -62.39449 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e925e5d4-2267-3edd-ad98-68c21846cc14 | -7.55421 | -63.8435 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e49fa99b-ba6c-34cf-8595-bb5154d04d83 | -9.16273 | -59.60485 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1bd908c-0bff-3e16-9ccc-5eb91d41d706 | -6.45376 | -53.38237 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e152b48-40e7-3cfb-af5e-c98f5428f00c | -8.86268 | -62.40443 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b49d3f7-2487-3f7f-8168-6649d5f8fd2f | -8.62464 | -62.14134 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0bc2b80-af21-3a93-8263-9d93d3d0e872 | -7.05718 | -59.83134 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aae1a30-3843-3497-9757-a8cf3484747f | -8.85937 | -62.40392 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 132f5a18-469c-3833-b7fa-56dd680bc73b | -5.13537 | -56.97355 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4941483-342f-3a7c-95a7-d4625f453040 | -8.67968 | -62.0924 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 977baee2-2330-3071-93df-fcb1cb81ce93 | -9.23857 | -60.66668 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2de5f05e-b5a4-3ab7-b81b-db0b70f02eb5 | -8.84826 | -52.04862 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c78a2f7-defb-31f2-bfa6-23e76cb6650f | -6.44941 | -53.37514 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5e0dcfa-035a-31d3-9bce-beadf1a511b0 | -9.21376 | -59.45869 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 891c2fe3-3cd5-3cd4-8bc7-7c2ce8f311cc | -8.6241 | -62.14484 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 467abd3a-6380-32a0-9c9d-1df7b6f2b861 | -8.88472 | -62.3936 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9623a024-6e2e-387f-8a92-396e6027632e | -7.77845 | -61.36955 | 2025-08-21 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07a11b1c-8f93-3ac3-94d4-77b06ba647a8 | -6.93382 | -62.88672 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69236486-0128-3fed-968e-90369d3ff819 | -8.86099 | -62.39346 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 32553cce-d958-3193-b2e9-a7040c18df69 | -6.26268 | -52.82199 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c531004-47e5-3fda-816c-c3dce265da70 | -7.50962 | -63.82905 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 529712af-7067-3be4-9658-85412999792e | -8.43237 | -63.8639 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4ad388b-1b39-3089-bc52-032ab77f8677 | -7.55364 | -63.84707 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7211592-d7ce-311b-bee5-3090bead412e | -7.77559 | -66.95672 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d736c5c-4ba0-3dec-974a-cc451508c1d2 | -8.24098 | -67.3599 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d8aae3-ecbc-3a5d-9e5b-3d78e8717a38 | -8.66595 | -63.85073 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a80eb2-f64b-3ba5-a6da-c8d261a59eb6 | -6.94099 | -62.88429 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63e238cd-37c0-3fb5-a525-48f2172b9035 | -8.70396 | -62.8775 | 2025-08-21 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d610bb15-ae98-3333-b26f-0b5735c0aa2c | -7.02365 | -59.67171 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
