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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4601a2fd-1f3a-3854-831e-de4a519d2c42 | -19.47583 | -47.77492 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e7abfae-4d6b-33d5-af1f-6336a8e86f74 | -19.4732 | -47.76522 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab465a7d-d41a-3ae2-b78f-d0c1632640ad | -18.23615 | -42.66449 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b05d9db-e83d-3c5f-8eac-960562c17c45 | -16.92691 | -45.7698 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de9db82-77f4-3b73-8e37-e0217b224809 | -16.33892 | -52.94958 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 228a4f73-a326-3c5f-8843-8cdcf5ec9f9d | -15.94535 | -41.88578 | 2025-09-07 04:00:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54ab349f-e524-35c1-9e46-587903ac59c5 | -14.29206 | -43.56189 | 2025-09-07 04:00:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d22598e4-f41e-381e-b3ed-4be38d0c9225 | -13.83332 | -46.25891 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9557f1af-6ad7-3b94-8335-9db14c1c8f3a | -17.70037 | -44.48471 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30d475af-1a8a-315f-af07-87c4e5eb0e02 | -19.46814 | -44.19009 | 2025-09-07 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e6d0aa3-6d55-3303-bc77-ec9957720376 | -15.8403 | -52.27963 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f10625e7-aab9-3248-b615-0da68ca9b764 | -16.29539 | -45.68746 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a5175c-ef56-3d56-8f89-705adaf6d255 | -17.22544 | -46.70271 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b5ae47f-91eb-312a-be0f-d7cf0b76e2e4 | -14.56915 | -43.72877 | 2025-09-07 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29721477-de06-3fd8-87fb-0ce51dc82e77 | -18.63249 | -43.26057 | 2025-09-07 04:00:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d45f8d49-1bc8-3281-b30e-6bdeb70df73d | -19.47835 | -47.76172 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 208910d8-d586-3fd6-8dbc-cb5eadee4bd7 | -17.48715 | -44.77455 | 2025-09-07 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04666c34-a883-3883-ae8d-aac02bbab236 | -13.93266 | -54.02485 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abadb09f-b277-34f1-82c6-8c51c023bbfa | -13.86237 | -46.24729 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77541c1a-0c29-3e08-a866-d3edbb45aa88 | -14.49127 | -48.77239 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88d8c4d3-7219-3f13-8dfa-997733a907fc | -18.35592 | -43.92459 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5067a9f-3882-3f7f-9d86-ffc96ffc5d46 | -14.45385 | -48.4601 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c2e3a44c-e5e1-36b4-9197-c80dbd7f00d5 | -16.30754 | -45.69349 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c876452-7087-35f7-b595-28f29c8e1c7e | -16.9318 | -45.79531 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e52f4f91-7741-34e4-98c1-768927f43fd7 | -17.87718 | -44.32635 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d180773c-99d6-3595-a612-bc3721503d44 | -17.67373 | -43.54127 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 665212da-9175-3553-b786-4fec8dfc7530 | -15.5363 | -48.37907 | 2025-09-07 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780cb1bb-628f-39f3-bec7-d0faf120845c | -14.85308 | -46.69633 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0aa8e26-d73e-37b1-afb2-305b8f116e66 | -16.92201 | -45.79703 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 253d3f53-9514-3878-a372-4bc5a65b258a | -20.04031 | -41.22488 | 2025-09-07 04:00:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| be199fa7-3ed6-3762-b70f-d498aa7d4e45 | -14.59846 | -48.08597 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 730cc50a-477c-329f-96c6-7167996012b6 | -13.83869 | -46.27838 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2275d18a-39f8-3a98-8ddd-28ef60f40377 | -13.46076 | -46.83933 | 2025-09-07 04:00:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0aa2c8ce-571c-34b5-8717-7772bfce7ce5 | -19.89538 | -41.43827 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f8669d6e-fb68-3428-a133-6a6815a9e4f7 | -16.78515 | -51.35913 | 2025-09-07 04:00:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b97a0e6-b135-3748-8092-b607b40f7926 | -19.34419 | -42.17568 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21961c5f-1910-3342-a74a-222d1e66b421 | -16.32967 | -52.95187 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ba90782-a07a-38fc-b29a-1005f3c70250 | -17.22316 | -46.71478 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0370c28e-4478-33f1-8c07-abe23670ed65 | -13.82064 | -46.27879 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088b4283-c836-31e4-b894-094a0e110adb | -19.89755 | -41.44621 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cb6fa98c-97ab-364d-9035-d50fa9780814 | -16.93872 | -45.74995 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b195e0d-e905-367c-9819-d3215dc512b0 | -16.91901 | -45.79073 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b346dfd5-85b4-3cb3-b480-03f225570b45 | -17.67934 | -43.55084 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90a0be38-b1b1-3ac0-babb-4dab3be9e05c | -16.92791 | -45.77183 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47574f2a-eabf-344e-b974-5be47b0ae835 | -17.68217 | -43.53442 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee5807ef-c4ce-3f50-9089-9389125a696f | -17.88002 | -44.33152 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14dd0dad-b2cc-3482-b034-1dbd4adc9a00 | -16.33308 | -41.95281 | 2025-09-07 04:00:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 313d5aeb-1c85-3576-86d3-2c9a2ceb79e2 | -15.88871 | -52.2047 | 2025-09-07 04:00:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6d32b04-6239-3c48-b821-a067fd46f821 | -16.34508 | -52.95165 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 110237fb-06f0-38ce-8a6a-48e661d0e5ec | -16.33785 | -52.95434 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b61f7143-9e8a-33bf-a613-5f4cdb356ea6 | -13.91517 | -48.0289 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa32bcf6-3a47-3065-b3e4-913e299c9be5 | -16.34225 | -52.95486 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47ee6af8-8311-39cd-8030-675e5849b77e | -13.84851 | -46.24954 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c32f8f4-ba30-3ff0-ad97-ffa67c8783e9 | -14.44312 | -48.46238 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac62b078-9eae-38aa-ab41-cd40f9b62806 | -13.9203 | -48.03791 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d74794c5-9596-3afb-8bc0-73a2a9cf9315 | -15.67781 | -48.20854 | 2025-09-07 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8fef2e9-4232-3166-aa16-b402837af509 | -13.83494 | -46.25021 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aed3cd6-e374-3ca7-ab3f-d5f117dded9f | -14.49068 | -53.24138 | 2025-09-07 04:00:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eafc5278-5407-361d-9e51-5d7ae1c044cd | -15.53958 | -42.65905 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9aed2058-1a36-3230-9aeb-4b824a4c01fb | -14.48786 | -48.76295 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ae97482-2a7e-36a2-8ac2-c03ecf850f39 | -15.531 | -42.62545 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9e2a747f-a281-381d-90e1-ddf461b971bb | -17.67161 | -43.53256 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6de0bb23-4b03-386a-8c3d-609feb563bad | -15.67695 | -43.23105 | 2025-09-07 04:00:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 019db290-0c66-3ac7-af06-0d3bab67d1a9 | -17.10416 | -49.89039 | 2025-09-07 04:00:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51468b23-4c0c-306d-b3f8-9664587cc8f0 | -16.90204 | -45.7703 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea835d70-884f-3e66-a65e-2a63578a3e8b | -17.69093 | -44.5173 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e33f8d0-a15c-3724-b4c3-64b69fd8a6ba | -16.9359 | -45.75113 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 446860b9-a682-3630-80f0-01368097af0e | -16.94077 | -45.7615 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4474a9cf-72b6-36fc-8c18-e89aba1bbebc | -16.69013 | -46.80263 | 2025-09-07 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7f40453b-4edc-3709-b5af-2b91835965aa | -13.82505 | -46.27924 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 174c9048-5ff4-361b-bab0-802a105f0f31 | -18.68981 | -44.44942 | 2025-09-07 04:00:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662b549d-fa6f-3fcb-9d96-69706835b7f2 | -17.62797 | -44.78948 | 2025-09-07 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c04e508c-9c68-3df8-a281-bbb492c036b2 | -17.70632 | -44.48435 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 670ba36b-8b0f-385c-8d6e-0459b25e9908 | -15.84756 | -52.27579 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 36b2c49c-cd8f-317a-a0b9-2b8eeab288cd | -18.49491 | -49.51618 | 2025-09-07 04:00:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 416a5a25-e08d-3e6b-aae2-cea43607eb50 | -16.55157 | -46.84578 | 2025-09-07 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15b6ef9b-9ab1-3186-8493-0e2ef2dcf822 | -13.83366 | -46.28123 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c9da74d-34db-3bba-a382-512e2c8138df | -17.10424 | -42.29862 | 2025-09-07 04:00:00 | NPP-375D | JENIPAPO DE MINAS | MINAS GERAIS | Brasil | 3135456 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a365bdc-c516-3975-bc85-991d9f3641d3 | -16.53783 | -45.09432 | 2025-09-07 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ef4a26d-01b6-363b-9601-83e9cc356aa2 | -19.47405 | -47.76077 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 145bce22-7505-3830-b7ba-fa65161f95e0 | -17.67866 | -43.53376 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6297b5-11f6-3bce-9ece-5f263cd42796 | -19.48085 | -47.77509 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e8c08c61-250a-3c1e-95a4-e1698bb50eeb | -13.83673 | -46.26474 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f9bc8bd-b064-3783-8845-19be3ce8e77e | -18.03302 | -47.09243 | 2025-09-07 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1920b2d6-9c6d-34a0-b777-dfbeb3331df1 | -19.89422 | -41.44563 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b38537e0-4edc-3c15-9626-3b2b41b7c5ed | -14.68325 | -47.14767 | 2025-09-07 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78b8086f-df33-3432-89c4-6bc5d342d292 | -15.11138 | -48.07982 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af4bb332-f0db-349a-9180-4aa6f16945f8 | -19.89321 | -41.43032 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e74708a-be90-3c7a-b4e2-621c7611525f | -17.10452 | -42.2987 | 2025-09-07 04:00:00 | NPP-375D | JENIPAPO DE MINAS | MINAS GERAIS | Brasil | 3135456 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 326901ad-c1f6-39fd-bdf4-4854563239aa | -13.84345 | -46.25268 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcff786b-716c-3c24-a122-40f0094982e2 | -16.93988 | -45.75194 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aac7dbea-60fa-3be1-a31d-49c7f3d29b3b | -17.68521 | -44.50654 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 440bf90c-1ec7-3832-9426-8d12d52bae2d | -14.45482 | -48.4551 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56451c4b-22eb-3198-99b8-f64e2f6a4051 | -18.24692 | -45.20541 | 2025-09-07 04:00:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9acbd574-944b-3221-9547-ea01dfbefb4b | -17.68704 | -43.54828 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9370b4d9-b786-355d-bdb7-6b4de90a2a5b | -19.74057 | -42.12682 | 2025-09-07 04:00:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 909ff8bd-959f-3a8e-bce6-06a7733708d8 | -17.7051 | -49.10897 | 2025-09-07 04:00:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7aa233-87e1-37e1-b872-647a60ba519b | -15.83413 | -52.28299 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 007b6e52-879f-3042-9c20-d45b9602b258 | -18.98687 | -44.22991 | 2025-09-07 04:00:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d6dccf13-9a5b-351a-ad50-625e9a821411 | -16.33149 | -52.95319 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
