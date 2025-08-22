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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f03fd3f-ce70-3e9e-981f-3dd7c2dcf632 | -13.38151 | -47.49824 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf3d9f93-7f39-37da-b873-681378b85687 | -7.58775 | -63.43881 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aed0fbb4-a326-3e82-90e1-497cf07251a4 | -8.714 | -69.4637 | 2025-08-22 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f45ed21d-749c-3f9e-b222-1ff53847a19b | -10.67929 | -51.5641 | 2025-08-22 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1a3f109-1eec-3022-86bf-ae10edb52857 | -7.56136 | -63.85394 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae517a0-c88c-3ade-ad91-15316a288aee | -13.0356 | -46.32657 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8adb6767-03da-3e28-88ea-37e3e88c1489 | -7.44216 | -60.62694 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8368407-4e9c-3e99-9265-310cd7ed4e47 | -9.93494 | -60.51957 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e80bd009-0cf3-3d9a-aac2-8f0146963ead | -8.85037 | -52.04248 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ef7a366-c22b-3315-b811-57ef4299b30e | -10.46014 | -59.13388 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a71f59b7-380a-3f85-9c78-1989ca26495b | -11.34107 | -55.42579 | 2025-08-22 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c826f4a6-cf9e-3576-9a68-4c8f8744ec86 | -13.64625 | -45.71214 | 2025-08-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0b558dd-94a8-30c0-8a2a-e504379e0208 | -9.51969 | -60.54752 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 316cff5b-68cf-316a-a9f8-6f4547d1aecb | -8.07008 | -49.71288 | 2025-08-22 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 690ad96c-2155-307e-9ba2-ed6eab55f7ff | -9.9025 | -60.28572 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dd735fd-1b52-3c91-ad12-f1da55ba3377 | -12.51469 | -57.65621 | 2025-08-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c75ee9e2-4066-32ef-9e54-d58f60621a19 | -7.84028 | -61.72563 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bac47849-5420-3a7d-90f6-a4c9a2e437a3 | -8.90187 | -47.33087 | 2025-08-22 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6617d58b-df47-385e-b723-35d92748b2a5 | -13.46394 | -47.04983 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 223df8fa-5265-35cf-aa5f-e06bd043205d | -13.02997 | -45.19415 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d57520f8-72b7-374d-8319-5af2a9bedcba | -9.50737 | -60.51389 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4959c7d0-caa3-35ad-8fae-c0a8d916f0d0 | -9.20993 | -59.46269 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3ad4b2f-778f-3759-9687-1388b5a047ee | -10.86577 | -50.8413 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f7e41a74-4861-3677-a526-47cc5ff6ad34 | -7.55707 | -63.8532 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec9cd35-5744-3356-8b94-154f965c9549 | -13.36561 | -46.25738 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a14ba10-8c8e-318e-9faa-44dacd708c80 | -9.59172 | -55.35096 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec40b338-f7be-3e67-8049-222902ab5b64 | -11.24752 | -52.08289 | 2025-08-22 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3efe45e-1c41-38bc-9339-9b68005ec2fc | -8.83439 | -52.03117 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3eeb3ca-dffc-367a-99f6-7d8600efce91 | -9.52786 | -60.54095 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1e21d821-cac3-3bf7-84e9-2b4f073972b1 | -12.93928 | -46.17991 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f185f26e-b169-3379-b92d-bb745b63adf7 | -9.51623 | -60.54696 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bcc9353-569e-32b1-9a8a-91f50a83ebaa | -13.03074 | -45.18704 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31f5fa00-1220-360e-a348-83c6a8566b61 | -9.21223 | -59.44835 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a561a2cc-89ce-32df-9a55-d7da7aca54c8 | -11.48378 | -50.50886 | 2025-08-22 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db2346be-4aad-3cf0-b243-9f0200c74cd2 | -12.99943 | -45.21173 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73bdabe0-c6c8-320f-a7e8-46d8824ab99a | -13.34423 | -54.39623 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3198e5d3-815e-31cd-858a-a1ba2911e8f7 | -9.93377 | -65.00655 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a1ac61-4114-309b-84e6-96447de0e3b7 | -8.87062 | -62.39907 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fa8040b-7685-36b5-8bcc-96161049751b | -9.05252 | -54.93963 | 2025-08-22 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcab196-79de-3352-9d93-a4f1b512436e | -10.28348 | -46.75303 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fef48347-65bb-3ff3-bbf2-8dd3727f45b1 | -9.47541 | -57.82256 | 2025-08-22 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fe63d3a-aaee-3317-b365-f98606435ac1 | -10.29095 | -46.7602 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa279467-f071-391a-9aab-543a9afa06d9 | -8.6254 | -62.61258 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0f8ba0d2-fb75-3e7e-9565-8766994f038d | -9.65293 | -59.65308 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b903335-4d0f-35f5-b333-550f0d99a270 | -13.1381 | -46.90012 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24f0124a-0127-3336-b5dd-3d458b615409 | -13.17059 | -46.9124 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24521c65-1142-32f3-97c8-b37d084d577d | -10.86988 | -50.85069 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 54491f97-2cb1-31d7-addc-fce4226627ce | -13.02846 | -45.18366 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dd3dbf9-4b8b-3082-9b36-396b4a728e95 | -13.02136 | -45.1829 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1d4706a-2ba5-3652-96fb-fe87ec0d1543 | -8.66227 | -70.03551 | 2025-08-22 05:12:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04554195-fa7e-3576-bf57-cf381382c42b | -7.05795 | -59.82328 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9507aa1-4509-3fd9-b4a8-5a5024d415f5 | -9.64841 | -59.65977 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a195fb6c-5517-37d7-a456-6270cb613ba8 | -11.90145 | -55.89826 | 2025-08-22 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1691430b-2807-30c5-a411-02af2b37b62b | -9.16101 | -59.5953 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1460a03a-bbda-32e0-897d-0c1e675bcd9a | -11.039 | -59.17403 | 2025-08-22 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aa82a58-aeb3-348f-9151-c0ff96431d59 | -9.52316 | -60.54809 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6376bca6-663d-3084-9f9e-6042e59789cd | -7.71908 | -66.9197 | 2025-08-22 05:12:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 950b78be-43b3-3423-94dd-137045e52e42 | -8.88965 | -62.4269 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 411f6564-ea57-3d4a-ac18-50e0c74af53b | -12.5876 | -47.09189 | 2025-08-22 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef2dad47-7359-3658-abfe-f3e5e36f95e1 | -7.71849 | -66.92298 | 2025-08-22 05:12:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae27d407-5d88-3ede-807a-197c553efd0f | -12.98819 | -45.22819 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0baf4110-82c7-3627-a3d7-67602a120023 | -9.09615 | -59.49253 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a09fd44-4e24-310d-9615-fdf3659435bd | -8.11956 | -47.15243 | 2025-08-22 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b6be0be-3faa-31c6-8671-83f712c8201e | -12.96319 | -46.27194 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b142405a-d990-3469-aaed-d0cf93353b1e | -13.03627 | -45.17736 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47646059-d58b-3e68-9caa-9af7f1fd85d1 | -9.22764 | -59.77055 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0f4756-1ee4-3c7a-84d1-725f51abbbf9 | -8.86296 | -62.39772 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a60704ae-f17f-3ea9-9b4e-2c8d1e4d448d | -12.95507 | -46.28475 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b341498a-4dec-3659-a2be-ddb70357292d | -8.55163 | -66.94994 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5d4c41-8c37-3f94-a901-b6536f347541 | -9.59468 | -55.35561 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a94967c-b448-3e37-9075-1d1d774cbeb3 | -10.28907 | -46.75963 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2354c21b-3e98-3ccb-86d6-e94a1518c973 | -9.91585 | -62.14283 | 2025-08-22 05:12:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee114ca0-a6c7-32fb-acdf-b775ea6fb198 | -12.98609 | -56.88851 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb36bccc-1246-3cf6-a7a8-abd3c030c96a | -9.21099 | -60.79788 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e95d002-3242-3b51-abe9-3ded9dfceb58 | -8.44153 | -63.86295 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6ce31bc-fba0-3687-b58b-df8e9043fe7d | -12.50155 | -53.81227 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3cbac7e-9c81-3fb5-96f8-69cfcc629ce7 | -10.55119 | -62.73758 | 2025-08-22 05:12:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d981f253-4880-3f7f-97a0-e437715ee7b6 | -14.75861 | -56.02886 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab4a46fc-9297-3b51-95cf-113e3f31da9c | -14.67566 | -54.87315 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5261f7c-a22e-36f6-b875-715f82734f9a | -19.66931 | -48.98872 | 2025-08-22 05:14:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7bd84e18-1cc8-3e0c-b65d-295bc45e0786 | -14.76296 | -55.9982 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8875cfd3-545c-3842-8641-2704e01ccfaf | -14.77127 | -45.40927 | 2025-08-22 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba895aea-2492-3097-8ad1-83e32b4412fa | -15.00466 | -54.86496 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7521fab-80c7-3802-8287-7f064dd3603e | -14.76652 | -56.02561 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d13280d-3a26-31b8-802f-1ff1e46df7fb | -14.6349 | -54.84496 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| befaea43-b391-3106-a815-e30ead4f064b | -14.34042 | -53.12558 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17693264-5a98-3c13-8d66-d63bd05840b4 | -14.64841 | -54.86933 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50353fd9-c53c-3090-998e-d4d9e4777441 | -14.75675 | -56.04199 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf9e531-77ff-3c20-a851-67716e3cd57d | -14.65544 | -56.59763 | 2025-08-22 05:14:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab5790f4-e1a2-3032-a6e7-1e0d5fa60c43 | -20.30098 | -46.63824 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e3b362d7-5535-3ec6-85d9-e6312b868c1b | -15.5557 | -50.32308 | 2025-08-22 05:14:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a992047-daa3-35d5-9f79-ba1eb8697a28 | -14.78668 | -59.65249 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28b2ce3a-4e1c-39b3-8b36-177deade6e46 | -14.6317 | -54.83942 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e4668f7-87cb-3f49-bf73-4cd84d51b845 | -14.73914 | -56.03484 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97aea10c-6314-3c18-b3a8-42d01bdd5fdd | -14.62969 | -54.83101 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90689be9-58a9-3f7d-b2c7-510c8ced9024 | -15.155 | -47.95 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae2f9b81-bc4b-3b29-b23e-63c63d0c6d97 | -13.43111 | -57.1708 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a2a80d-29e4-3ad3-bad8-cad604ec4f2e | -15.16149 | -47.95224 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23cb10d1-098a-3332-b943-3945c828b52e | -15.02871 | -54.86403 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f25bdfd7-7fe8-3ffa-b19f-02b064a05dca | -17.67457 | -54.05182 | 2025-08-22 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README51.md)
