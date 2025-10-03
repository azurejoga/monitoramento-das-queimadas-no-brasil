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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b1717d-a1be-3a01-8f08-b2c8c091b113 | -16.17746 | -57.58495 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2aac4f32-7e95-3184-8313-d24a613035f9 | -14.63795 | -48.25871 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5225609d-53a6-388e-bed2-377939bca1e7 | -13.76233 | -47.54456 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3376d596-87ee-302c-96a8-9169a1f97726 | -13.33564 | -50.93164 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27cdd1c3-fac4-35a1-b3db-8a0e6dc453f6 | -17.84477 | -44.31342 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c3aaca1-6dc2-30d4-ba8a-599694986f98 | -15.24749 | -50.12552 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73f0acf0-20f9-312e-8031-f0e385b4233a | -13.268 | -47.27097 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4fc6fe5-7549-3015-825f-d8bcb005ad69 | -13.27706 | -47.25738 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 072170dc-3744-3edf-99c2-af51411fdadc | -12.61693 | -46.99897 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5c2009d-7c12-3022-8b97-a63ca7c48c2c | -13.32919 | -47.58744 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c076e31a-42d1-35e8-8530-34b833443efe | -15.31941 | -46.38338 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21a1d14f-b2e5-3fca-ac6f-ce1f981540ea | -12.85311 | -46.93089 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7bc31c6-917b-32a8-8912-d5ca2b949c28 | -18.6468 | -50.68621 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b55112b1-291e-3e41-91a2-fe9f58b4b726 | -12.60017 | -49.91936 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e537feb-2fd8-3ad9-9504-28f0a2fc595b | -12.19275 | -47.81453 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63f4e240-3c65-3176-8cca-86aa24dd6e55 | -15.31292 | -46.27293 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfe335a7-3dd7-3860-a163-aa60618b4874 | -15.70964 | -46.26039 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 063f80da-6d47-36c4-bf23-1ba4ba35122f | -13.53556 | -47.28458 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4693772-5013-3a10-b2f8-56c76079d25b | -14.92812 | -46.90757 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 529e1ba4-7d5f-34e6-93b7-dff84a5e2af5 | -12.47387 | -54.42831 | 2025-10-03 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e021afe-bfc2-3c74-b5a7-eed1ac7a28aa | -15.23755 | -50.12384 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d80ab015-74d2-3967-b922-a5e80f44b000 | -13.56731 | -47.58516 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acc7e242-88c7-3e65-b8ad-cbe66f6d536e | -14.40817 | -47.87841 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d22dc249-56b9-31ea-a8f3-913e68659f59 | -14.30534 | -45.88037 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87df2be8-1e09-33c5-8151-28aee3589968 | -13.68519 | -48.03482 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05575006-f083-379c-bce5-63f32c606fb1 | -13.18552 | -47.37933 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b28677-91cd-3c17-ae2e-f750e513b835 | -18.45038 | -43.70858 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dc52596-cf3d-3d06-a68f-9b6d38715ba8 | -14.91322 | -48.32896 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bffb010b-1c38-31bd-af96-707f100ec122 | -16.17649 | -57.5899 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fc72856d-6451-3498-ab75-86204cf6d8fa | -14.58862 | -46.71326 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04284928-7487-34de-8f58-cb392e3f39c8 | -14.68159 | -48.08424 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f085b0-ce93-36ae-8d79-b5307507b2e7 | -13.27455 | -46.95232 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2e032335-9d9b-3ad7-bbef-a16cef3c7079 | -13.97969 | -48.17064 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64b75d03-9e7e-3e4c-983d-4b4ec61e84bf | -13.13151 | -47.89349 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 274c48e0-a5ee-370c-8183-134979167cce | -14.61887 | -48.24804 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dd41335-255b-37ab-a030-f8a094d41b80 | -16.04627 | -50.92611 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0447d73-3580-3082-984b-69e97140ce40 | -12.24801 | -51.43348 | 2025-10-03 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6679ed3-04d5-3b22-9865-2d3eb0c64f46 | -13.34898 | -47.33786 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a040b99-eb49-39cc-aaef-b4ecba6d6854 | -12.86811 | -46.92533 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ace2201-cb66-3a50-a94f-1fe94273abff | -14.31831 | -45.86863 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6859eba-0f43-3b0e-81a9-f1ee325f65bc | -15.9285 | -43.0767 | 2025-10-03 04:34:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef5a79f2-57a3-38ca-916a-7831a694e9bb | -19.50905 | -41.96575 | 2025-10-03 04:34:00 | NOAA-20 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f90031f9-3ce7-325a-9089-4d0461332b18 | -14.94041 | -46.89764 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e85aa0e3-ebae-3d37-a27a-93916f52c436 | -13.96108 | -48.10116 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26cb2cc0-c425-3846-9fa7-ce5f06a8d7d7 | -11.08099 | -54.78836 | 2025-10-03 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a077ca5-b753-3c01-a463-c3e594ff481e | -12.61576 | -46.98333 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7cd79660-1171-3e6a-a418-3520e620df09 | -13.26387 | -47.25154 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a8057b3-d0be-34bf-9728-8a0e583edabd | -15.94638 | -46.22147 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a97eedef-960a-3ac3-9d13-5fc81faf513c | -13.15999 | -47.89769 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97009a8-fa43-3f35-9c01-94cd57443091 | -13.76797 | -47.53026 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99160655-dccd-3f75-a08a-505ba3d693f6 | -13.76697 | -48.05116 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480ec114-a7fd-301c-bb45-e15919ffe149 | -14.35803 | -43.8509 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eabd1d2f-627c-3dd0-b2a5-69b4de347153 | -12.62348 | -46.99465 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88819adc-5400-375b-ae68-4f68b1f3d5bd | -14.89787 | -46.96652 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 73635efc-9188-367d-bf14-2a5c591cf32a | -15.24307 | -49.29068 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3e0a467-8051-3a5e-9ee8-dda4c9bca166 | -13.74747 | -47.9884 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c5a1fc6-1745-3382-a0f0-822f22467213 | -14.6726 | -48.07497 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 35bed7cd-8d62-3c79-875b-292851616095 | -12.60658 | -46.97395 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a5a63046-5144-33a2-ae14-065ff09999db | -12.68784 | -48.54537 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 500c11ae-5d31-397a-bd4a-0460ecc8e220 | -15.6003 | -47.0504 | 2025-10-03 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 235d66e3-a04e-3e93-b834-f035122b50f1 | -13.54188 | -47.28936 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03fbac38-c06c-32b8-8e38-41e2263e144c | -13.6383 | -48.67577 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e564d9de-f173-3826-a34e-a716ba72eb58 | -14.44157 | -46.10741 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0604df73-2ffa-3b94-9b6f-c321abdbe9cb | -13.58439 | -48.18711 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e5e98ca-3dac-3193-8fd4-2c1bb7d4ef33 | -18.40001 | -50.78584 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64954823-a4bd-3c93-8c8c-9ca2647ef400 | -13.29654 | -47.26825 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e98f01c-3414-3a76-80a5-f7010403917f | -15.588 | -46.9089 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4071af9-9d60-3793-b841-dbb94f4cf5f4 | -14.22367 | -46.09236 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f872cad-cc32-3c58-aa16-34cc6a50eff7 | -14.36917 | -45.93578 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f6247d-c45b-3538-8d1f-30ef31cf7a07 | -18.2223 | -53.35027 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb719b85-7986-3e66-adfe-80da270aee07 | -14.88963 | -46.97349 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8434cb-4489-340c-9248-d31f588b257e | -14.40995 | -47.86669 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc90c75-6e4c-3927-afd5-ed8d025f5bc7 | -15.66095 | -44.49754 | 2025-10-03 04:34:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8678e17-44bf-3fb6-8b62-62d73724084a | -13.33204 | -47.5916 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44c64ea9-b255-35d1-b888-eb4b1ed0a538 | -14.85036 | -48.28879 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c2cdbe7-d6c0-3e94-bee2-8b7add41eccf | -14.60167 | -48.23796 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0abe0fe9-e628-34a9-a495-eeb61570fd6e | -16.76858 | -43.96179 | 2025-10-03 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6db75dc-1f0d-3803-ab60-e150b336f653 | -13.26843 | -47.24453 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01cd197c-ce79-3ea5-8dec-7b1cd564ab41 | -13.80451 | -48.05384 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa588f97-8954-3f48-a29d-7d7b180e1141 | -15.3109 | -46.391 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5be41336-1fd3-3289-9da9-03b04b14b5ee | -13.5379 | -47.29248 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18eb200a-5efa-30f9-be5c-ccfca4de6526 | -12.61003 | -46.99791 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36e5c79d-1d0c-3ed2-8b2d-e832a3ef9111 | -13.94485 | -48.1397 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 670b4eb5-eaa9-3892-a8b0-d265d90e2799 | -14.87451 | -48.33416 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b14a0bb2-247c-32da-a639-c327c58743aa | -13.65886 | -47.3033 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0c71307-2e24-3971-9ddc-c99ba9710533 | -13.36613 | -48.08242 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c012aa72-e3d2-38df-850f-ed7090133cfc | -12.92861 | -48.43761 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 396163eb-5d92-3cc2-a45f-516c650fd2bf | -12.76268 | -44.91212 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 067ed134-de16-37c2-bf7b-8a4f7daf03b2 | -12.62393 | -46.96768 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e7d157-90ba-3d79-8c0b-98be91847d69 | -14.22671 | -46.09723 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1012ee31-682d-3c07-9d2f-f886d886614b | -13.85116 | -47.92855 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b80669e-631f-3b87-8031-fe38e87e839a | -15.24862 | -50.11839 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf2cdc8f-3f95-3ab7-959d-1bb1e2dc4620 | -13.96908 | -44.86317 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5258bf1-ee6a-34b1-9918-c19923b02e38 | -13.96904 | -48.17272 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8641a50-28b3-3953-bf04-dd76f59be0d5 | -13.05398 | -47.06231 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bbbc4a0-8d6e-363e-8aee-708a6cf5117f | -14.73359 | -48.11499 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42f1896b-bdd8-395c-b9c8-9d9e951bc5c2 | -11.17423 | -54.11452 | 2025-10-03 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15926cb-bcf0-3efc-9447-297509f6d457 | -12.38719 | -46.51276 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f3789d5-7e93-36f9-bfb5-fa9e20e9c21a | -13.65546 | -47.30254 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3b4990d-0da7-33cb-a12e-0208a1aba859 | -15.19682 | -46.40437 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README116.md)
