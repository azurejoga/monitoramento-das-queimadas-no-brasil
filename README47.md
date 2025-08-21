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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 055e3486-09ce-322b-8439-299e63f543b8 | -11.31665 | -55.2206 | 2025-08-21 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3f02003-7b53-3801-83bb-b77e935145a2 | -11.29758 | -44.93106 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9579483-580b-3fef-838a-ee101c531b8f | -11.59524 | -50.36241 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6910459-78e9-382b-8737-482179da1c59 | -17.40015 | -44.24278 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cfba80fe-3c25-3fa6-a5c2-40eb7ad96f7e | -13.01891 | -45.19513 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51f9ac95-858f-323a-ae32-68bde99a7a89 | -13.18021 | -46.9052 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dac8a27-147f-3529-93a4-05eaa067e12f | -13.04752 | -45.17374 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc510bc8-ad49-343c-8597-45df5662052d | -11.4354 | -47.31968 | 2025-08-21 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d65f80fb-ad54-332f-bab2-8fb31fd51bcf | -13.02329 | -45.16313 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| e5682a99-f803-32e1-b13b-8cfb35d456d8 | -13.02055 | -45.18315 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 149db4f5-a4b4-37d7-992a-5200cb875bf0 | -11.81538 | -44.25584 | 2025-08-21 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f47b0fb-795c-3fab-8df3-dbaf4c975768 | -13.53492 | -47.04194 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 827353f7-d08e-3bfc-a544-e248bef41280 | -11.32636 | -47.83223 | 2025-08-21 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc1f035-6760-3ad5-8d59-ec04785c121b | -13.73861 | -52.03375 | 2025-08-21 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b32d2a3-dabc-34e7-afdc-06766556804a | -10.72669 | -48.24289 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48d949c8-d784-356a-a6a3-5054d8d8917d | -12.0889 | -47.90221 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93298852-d0ee-3295-948c-79090fe7e17c | -12.64169 | -46.86704 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1fab5c0d-32cf-30c6-8532-324f38a8c3e9 | -8.87186 | -62.42207 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f1764cf-c024-39cd-8777-c0ebb8219b64 | -8.84678 | -52.04744 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cece3c72-79bf-3f3a-a324-381acd4d65d4 | -13.19748 | -46.89298 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c264f19b-49a7-364e-8310-31698bbbedd5 | -13.39078 | -47.49457 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 33fde0eb-5664-3661-b17d-eee654fe855b | -11.86109 | -51.6012 | 2025-08-21 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a127248e-5a57-34fd-a2eb-e279196df922 | -13.01945 | -45.19114 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 650ec4da-18b6-349d-ab9c-c3f4e8fc64da | -8.84455 | -52.03952 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa538e1d-514f-3ced-b65d-6e90d6574a08 | -13.03955 | -45.16869 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 26e5d0d8-dfc8-3836-80a6-1cf414e428e5 | -8.87292 | -62.41667 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8dc8a10-4ae7-31ef-98ac-702eda00fe12 | -11.43112 | -47.32346 | 2025-08-21 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13d2bd93-89d2-361f-a817-caac25297153 | -13.03528 | -45.20146 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23bd42d9-212d-351b-a2bd-edc4bc7379cd | -13.55519 | -47.0354 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a18fe929-1e4c-3cf3-aab8-b4efcc6d07d4 | -16.25312 | -49.94163 | 2025-08-21 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff2f4c4f-115c-3a81-a259-604768d596ba | -11.81509 | -50.64993 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371a5644-a35e-3399-8a5d-f0a97b1fac6b | -16.11291 | -46.8206 | 2025-08-21 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 648ad9e8-ce15-3a42-8df4-f2cd58761829 | -15.8837 | -46.1783 | 2025-08-21 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc8234d5-2a5c-333b-81d0-5706bf0deec7 | -13.04275 | -45.17722 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3247f95b-1b25-31e0-a278-d626cb9ed77d | -15.02138 | -54.84689 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05d7c1cb-e590-30cc-9957-6502989a51b9 | -11.86166 | -51.59764 | 2025-08-21 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c14f9c96-abc8-3bd8-9a3c-a3c34ae3ca0a | -13.53263 | -47.03463 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b3236de-5ff8-315a-8894-4ce2d68a0932 | -14.85351 | -47.93216 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31c2fcb9-dc2e-3f95-a713-46f6bfcce2cc | -8.87212 | -62.41925 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2cb36ce6-4bba-3104-aa45-f96d26404d19 | -12.59956 | -47.08293 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc4fae6-bf37-39eb-94e1-1558f0bf345f | -12.08059 | -47.90917 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e77c0c-69eb-323c-901f-4eb8c13da014 | -13.04379 | -45.1692 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fd301620-9b5f-3953-9e27-7b5437ac9038 | -15.91824 | -47.34365 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97061293-4ed4-3ea4-abe0-0eecc7237618 | -8.84212 | -52.05453 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb004b83-bd62-3f76-98d0-d8160859c703 | -16.10186 | -48.00521 | 2025-08-21 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8588078-77fd-3ed4-8730-73dba9e08923 | -10.99283 | -45.62868 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d2fdb8f-1a2c-308a-a64d-ce54d71ea5d5 | -13.03602 | -45.16483 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b513f217-ede2-31a7-a09b-25714dc64930 | -14.75396 | -56.02588 | 2025-08-21 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85fe842d-ed65-38f8-b1e6-4171c04cdbb3 | -15.19808 | -48.7035 | 2025-08-21 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57b25936-28bd-3045-abd8-444022b190bd | -17.57781 | -42.27678 | 2025-08-21 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7ffd1eab-a4ec-3edf-8fea-e5b20d74b051 | -14.7462 | -56.02446 | 2025-08-21 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b014004-e1dd-3df1-842c-20f3eb18d34d | -13.03327 | -45.18483 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c83e68fb-57af-34c6-80f9-4fbccfc0ba8d | -13.1796 | -46.90952 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96c5abe6-a575-3ed8-983e-1c1f5b853931 | -13.03693 | -45.18872 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38cf07bb-a597-3959-9820-3510b2316223 | -13.03974 | -46.81164 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a44e5b5-15ec-33f3-9422-e79ada519394 | -13.63121 | -46.88124 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 787c46d4-f812-3201-a183-736d8acc7ab2 | -8.8806 | -62.40976 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 676afad7-0a5a-320b-b1ea-e058509eb2e1 | -13.01208 | -45.18194 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b761b31f-1fd8-3a12-820d-8951db538057 | -8.84396 | -52.04313 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9c97807-2e86-371a-a0e7-9cce2b18a7a1 | -13.03861 | -45.17738 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 11df1d96-97d6-327e-8a83-b478fb0354d2 | -14.85046 | -47.92725 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6c806e5-5938-3bfb-938e-4d30cf4acd63 | -12.5817 | -60.36151 | 2025-08-21 04:40:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ac78584-b9dc-37ea-924b-c5bc6cae2314 | -15.42879 | -46.718 | 2025-08-21 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7f9f9ed-59fb-3c47-b572-5f5efba295b9 | -14.85841 | -47.95057 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 593366ed-172e-300d-91ea-11cfdda2ba4b | -10.40819 | -59.37755 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b293b8a-d3a5-3e30-bcdd-64f773ded212 | -13.14273 | -54.92864 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19a4e0d-c923-3766-aaab-febcbc793482 | -14.65256 | -54.87573 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d4d926b3-c42e-3a2f-ae96-8851e6b7d5d6 | -8.84738 | -52.04371 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc2397a4-7b70-3b9c-b87a-5ccfed3bfb5a | -13.02698 | -45.16773 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 3b5b6c5f-cf05-38a9-aa29-db9968bcd81a | -8.86982 | -62.3961 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 0b439b83-e51a-33ff-a65a-c3075210c84a | -8.87753 | -62.426 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd3bf0c4-df9b-305e-9825-c2d90339e8fb | -16.82168 | -49.32725 | 2025-08-21 04:40:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ad346a2-60e0-3fef-8d75-2bfab171ada0 | -10.40761 | -59.38073 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0cf2fc8-86fb-318f-bc69-88ea880d20d2 | -14.4976 | -45.9531 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d993e8-4fea-3310-8801-6eddcae7c0ef | -14.5012 | -45.95746 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c47fbf2-d095-31f0-8f25-a6fd044ea420 | -13.1497 | -46.90118 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ff6853e-1787-382e-8df9-ba0560b87c88 | -14.85717 | -47.95932 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| abddd41a-5811-3ccf-b9c3-d73bd73e6f14 | -8.86133 | -62.40561 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| fdbaac8d-dc5d-378b-8b96-73be36311068 | -14.37209 | -51.98106 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2157cb3a-da26-35dd-8f40-2b8f896299d5 | -14.4677 | -48.36334 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3669556-83a0-38ff-a9c1-6bb86398c919 | -16.26534 | -49.95488 | 2025-08-21 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c505755b-3ecf-3c8c-8933-39e489564b2a | -14.36327 | -51.97223 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 165db9ce-a628-341a-837b-6379745c2824 | -13.03959 | -45.20139 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2df653f-c1c9-307d-b44b-135ebda98595 | -14.8799 | -48.06164 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f64e2ae-1f33-326a-b6b4-d1ba7c5f8bc9 | -13.16297 | -46.88961 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75ec444b-7bc7-38fa-9499-6d4dc9f4a619 | -11.09016 | -44.81026 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b08a96c9-f6ab-3b9d-a158-301207ec1f1c | -13.15794 | -46.89782 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5303677-9db3-37fe-83ba-79e564d1fda6 | -13.03798 | -45.18069 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be53abad-9da6-3f79-8569-00b303f06920 | -12.95669 | -46.24603 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b74f65cd-06f9-31f2-ae19-c77f3207da23 | -9.56007 | -48.11417 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4d67d42-f989-3735-ab06-46e84b4383d6 | -13.1725 | -46.90478 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bdfc584-53ca-3fee-95cc-44c0e01c0e18 | -13.03233 | -45.16026 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 195e87c3-2084-395e-9544-d915a1301132 | -13.49132 | -47.05277 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3689019-547c-3cb7-b465-77cbfb8261e1 | -13.49445 | -47.05803 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b57062e-2810-3467-8e80-88bc8f7d253c | -8.85255 | -62.41807 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff288e79-dbf4-3517-a740-46575993ea44 | -13.1443 | -54.91945 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e8fb95b-2097-3b87-8032-299fbe67763c | -13.32946 | -54.42652 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71456fbc-44bd-38dc-b57e-e141d0b84c73 | -14.12149 | -45.38244 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef8f8ac8-95b6-3f72-83ae-cfb96c1f3280 | -14.49611 | -45.96424 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 068b7b82-cedd-3e16-96ac-08ede90054d6 | -14.63591 | -54.86342 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README48.md)
