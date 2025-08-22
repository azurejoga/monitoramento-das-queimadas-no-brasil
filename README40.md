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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66ed795a-98b5-3d59-888a-e22747adeb86 | -13.50031 | -47.07125 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f5896df-2cc0-34ac-830b-b29281217b43 | -15.13728 | -48.11235 | 2025-08-22 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb57a2cc-ab99-3484-9a3b-2808b834f017 | -14.97756 | -47.13857 | 2025-08-22 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78007d8b-021a-3f50-97bf-6766c75db276 | -20.18816 | -48.71338 | 2025-08-22 04:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59f45116-db67-3649-9508-837fec625141 | -13.0313 | -45.1669 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96817701-7fef-3802-9be9-9f9e698561d9 | -13.32765 | -54.40269 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad88734-b7dc-39cf-a990-4b01446db801 | -20.18611 | -45.23787 | 2025-08-22 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 408c4f54-2c3c-3616-bba8-40f2f012acfa | -11.31236 | -55.22671 | 2025-08-22 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 217687fe-afd8-37d8-9e4f-667d29ba02c3 | -12.93094 | -46.1859 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0344a29-850d-30a1-b231-c860eadccd82 | -12.95687 | -46.28078 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0b6dd40f-551b-3fb5-86cc-af620f65be25 | -12.49541 | -53.81561 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23b6cc22-88a4-33c5-8985-69d42779fb2e | -15.90679 | -48.41093 | 2025-08-22 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e98907de-1118-3ac7-9c46-14c186d009e1 | -13.3641 | -46.26011 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee6de1c5-19d2-39b1-8a9b-673965a1105b | -20.13564 | -47.45868 | 2025-08-22 04:21:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2777376-a479-31e8-b3de-93a2196b94a9 | -14.66329 | -54.85174 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f7c6e86-e8f9-3f5a-963a-db38adb1dfdd | -15.02894 | -54.86858 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 351a3cda-54c6-3cc6-916b-2c25587bcded | -13.37495 | -47.4928 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4542872c-b69e-3da6-af89-0bd79945ffd9 | -20.23132 | -46.60712 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5bf2b4af-8e0b-30f5-aa17-8ada0db29466 | -18.87984 | -45.01769 | 2025-08-22 04:21:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 30f80255-b8db-37d6-bb26-efe41b04c105 | -14.75321 | -56.03141 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07b2d2a7-babd-3d1c-977b-0739984763e8 | -13.0555 | -46.83656 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a451e9b6-3f5b-398c-b0a3-4ca395626d3f | -15.0862 | -47.15977 | 2025-08-22 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfe1e799-8ae3-3940-972d-621f5305c121 | -14.7644 | -56.03024 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 478d3da2-0abd-317e-853e-f2f764e8f061 | -13.39976 | -49.13219 | 2025-08-22 04:21:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c14b21f9-2614-3e0f-a59f-8bcca1fbcda8 | -19.88838 | -44.81443 | 2025-08-22 04:21:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3687d93f-fe2e-35b8-a4a7-c56da3d4f6fc | -18.26362 | -45.5428 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af1c106d-2cb5-3bc2-bd29-ddbc6df2f8ff | -12.953 | -46.28377 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c089f7c0-2157-35f8-96f4-a4cfe6370da1 | -13.14647 | -54.92123 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc847821-bdfc-36dd-ab94-40b7989dca43 | -12.98877 | -56.88465 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfb27672-9a24-38eb-8875-cc330e0095f6 | -13.0041 | -45.23277 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18ad880b-5465-34bb-b637-6628571d6965 | -15.13788 | -48.10868 | 2025-08-22 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db71a847-6f92-376e-b5c3-c0db107f584a | -12.92819 | -46.18184 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4297050-e591-3907-98ce-75b5384e0fb3 | -13.0274 | -45.16998 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4c564ef-4de2-375e-83c8-3df55a292dab | -23.29641 | -47.46907 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 75312d0e-fc3e-3bbb-9123-dfd854ec3a4f | -21.43388 | -45.96575 | 2025-08-22 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| adcb7c91-5c10-328c-bcd9-fbf3fb150fcf | -22.5522 | -49.76857 | 2025-08-22 04:23:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 43087bc8-7aca-3a14-9d3f-0fe9d0f73a51 | -20.74228 | -47.89882 | 2025-08-22 04:23:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc10c345-2f77-3024-a2cf-e75ed8fd856f | -23.90649 | -49.44771 | 2025-08-22 04:23:00 | NOAA-20 | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6f31ff-2e66-3165-9dae-71fcaeb27191 | -23.2919 | -47.47618 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2d57765e-5185-3c84-975a-e4c0e490640b | -21.43042 | -45.96521 | 2025-08-22 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0b3e5543-19f1-3d9f-a5f3-530d11fe2ff8 | -22.07213 | -47.3238 | 2025-08-22 04:23:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08511cfb-b1dc-3396-becd-6414d5302379 | -23.52295 | -45.87811 | 2025-08-22 04:23:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c247cf1-623a-3f83-b285-ee7ec9880217 | -24.01131 | -49.04752 | 2025-08-22 04:23:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc24a457-ce79-319a-8b28-f704b68caec6 | -22.55555 | -49.76921 | 2025-08-22 04:23:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0d4e3396-f56c-3472-a55c-0d1708d94a36 | -23.41653 | -46.0504 | 2025-08-22 04:23:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e32cddbe-a9b5-3f80-891d-1c068a0c91e4 | -20.87002 | -48.53026 | 2025-08-22 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d766f7cf-088e-36f1-8510-3f4052f14fce | -21.42983 | -45.96924 | 2025-08-22 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 001684e3-525a-3157-a903-37b3365b3ebc | -20.35606 | -48.34483 | 2025-08-22 04:23:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 955dc633-6b14-3708-9a3a-50fa37f8e4f1 | -22.48108 | -43.18683 | 2025-08-22 04:23:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eaf4df63-9ea3-35d5-bc1d-333d2763c577 | -21.18438 | -47.13795 | 2025-08-22 04:23:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdc0e535-7cb5-3b26-b56e-3c438efe5079 | -20.9489 | -49.16018 | 2025-08-22 04:23:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f37f22fb-a00d-3849-bf83-21ac794dbbd0 | -21.12755 | -46.43489 | 2025-08-22 04:23:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d77d3ec-f8db-314b-a0fd-fe77dddd0d00 | -23.99467 | -48.60976 | 2025-08-22 04:23:00 | NOAA-20 | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 87adca07-0912-3596-be02-1d7acac96133 | -24.54275 | -49.05889 | 2025-08-22 04:23:00 | NOAA-20 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c48b3eac-d1a4-3e4b-a939-c7daa6529b94 | -20.35274 | -48.34424 | 2025-08-22 04:23:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0646d36e-72ab-3c59-ad56-fc5286df0898 | -21.24134 | -44.58345 | 2025-08-22 04:23:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6ac6ab47-c128-3fd0-acdc-0e211ec46053 | -20.69644 | -47.11914 | 2025-08-22 04:23:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5be02c47-d38d-31d8-a0f9-d831341c80de | -21.96285 | -44.97144 | 2025-08-22 04:23:00 | NOAA-20 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ef9b3bd2-344e-391f-93bf-deafaf7f9610 | -21.1883 | -47.13476 | 2025-08-22 04:23:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18877d88-1f96-3db2-a1ce-dc68ee9f6c4d | -21.25906 | -50.29838 | 2025-08-22 04:23:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8cbcba6e-216a-33e6-84a6-e983895c92eb | -22.29591 | -48.21077 | 2025-08-22 04:23:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1f02d59f-f141-320a-8226-bbb505e09f6c | -23.4789 | -46.22382 | 2025-08-22 04:23:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9dd38b4f-df24-3d0c-b566-b4403d85dc8b | -23.21195 | -44.90236 | 2025-08-22 04:23:00 | NOAA-20 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4788792d-5ef8-34fc-9505-2a71a0b81770 | -23.90317 | -49.44707 | 2025-08-22 04:23:00 | NOAA-20 | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b84575-c17d-30dc-806a-d2340c0390c1 | -22.23967 | -48.3959 | 2025-08-22 04:23:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823c3d8e-0beb-3768-9954-60408ca248aa | -21.42637 | -45.96868 | 2025-08-22 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 10c0466b-6c39-34cf-a5aa-1b612e29a82e | -22.55618 | -49.76537 | 2025-08-22 04:23:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2146284d-2538-3a29-9d38-5bc32bfa022e | -20.87804 | -54.99601 | 2025-08-22 04:23:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bade2d2-a438-37e4-b3d3-cb165347048a | -23.21003 | -44.90418 | 2025-08-22 04:23:00 | NOAA-20 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 5f036098-3989-3e43-8d2a-fd2c9050fe52 | -23.58597 | -45.68315 | 2025-08-22 04:23:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9636a09a-6b91-3c38-bad7-20c616d3f7f1 | -21.4333 | -45.96979 | 2025-08-22 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2acd93f4-c5f3-39ff-b3da-7d50f26b68ce | -23.97425 | -46.47165 | 2025-08-22 04:23:00 | NOAA-20 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c685ec0b-6d9f-378d-a521-d0916c2b0ce1 | -24.6858 | -48.37257 | 2025-08-22 04:23:00 | NOAA-20 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c37741b2-66a4-373b-8a71-f48ff815c6ce | -22.05853 | -46.32607 | 2025-08-22 04:23:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de45ebcf-087c-3945-9dea-f8eec8be2c85 | -21.63068 | -48.97934 | 2025-08-22 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bce348bd-e7af-38c9-8330-36804f1a77bd | -21.064 | -48.59143 | 2025-08-22 04:23:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d36a92c-733f-3585-8646-7db21c253fd3 | -22.78442 | -44.78858 | 2025-08-22 04:23:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d3b0277-2ea7-3c33-beeb-35c7ca9ccdcd | -22.69537 | -43.743 | 2025-08-22 04:23:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 62645c37-f52a-31ea-93a1-dbbba26c0afe | -22.90158 | -43.49456 | 2025-08-22 04:23:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8512393-b7be-38e3-a4ab-d4254459c680 | -21.41306 | -47.9726 | 2025-08-22 04:23:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6067c0d-4c1c-3d94-98f9-8836d9c46e38 | -22.07548 | -47.32438 | 2025-08-22 04:23:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3333e67-6854-3efd-80d7-5146fc8ad531 | -21.62736 | -48.97873 | 2025-08-22 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b775615-82b7-3abf-b516-9e129516a8b8 | -21.18773 | -47.13853 | 2025-08-22 04:23:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb1b8305-54a5-3c4f-b75e-bda4966cf16c | -22.78382 | -44.79303 | 2025-08-22 04:23:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ffa3cdc1-20dd-331a-8a02-0d37dff38cf0 | -23.25054 | -45.97458 | 2025-08-22 04:23:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67ede637-39a8-3a91-a7bf-2417a970fde9 | -23.19743 | -46.85569 | 2025-08-22 04:23:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cef38bc2-2d37-34a3-8901-4792a2f0f9cc | -23.28911 | -47.47173 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4cc0f439-8f5d-3abe-b388-d7275d625518 | -22.25506 | -50.03772 | 2025-08-22 04:23:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4c02630e-1e1f-33f0-be8c-a6f48c0bf49d | -22.66306 | -43.65073 | 2025-08-22 04:23:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5494a82d-aac9-3aa1-9fec-67ea08571dd4 | -23.59374 | -45.6798 | 2025-08-22 04:23:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f0e05c9-e8fe-3470-92f7-b765ed75c616 | -20.40856 | -51.36994 | 2025-08-22 04:23:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3f8dc14-fde0-3846-aa1a-9be23feb0901 | -20.87334 | -48.53086 | 2025-08-22 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 880b4b93-0e2a-3acc-8cc9-da28d004c1ab | -22.18916 | -42.86729 | 2025-08-22 04:23:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66523593-7524-319a-b892-96193a6db850 | -21.59837 | -48.98873 | 2025-08-22 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e1c7cfe-84d8-391b-9acc-72dcc474329f | -21.59172 | -48.98749 | 2025-08-22 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54d9361e-c21f-38be-80c2-dd7240ae43c7 | -23.29583 | -47.47293 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9ae6ce16-4e21-32db-8cda-a2793c51ea60 | -23.37651 | -46.77896 | 2025-08-22 04:23:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d3e0fcf-747c-3c95-afd4-3be4ec46a671 | -23.20761 | -44.90649 | 2025-08-22 04:23:00 | NOAA-20 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9055152e-5849-328c-9c53-284f92b67db1 | -21.89841 | -48.16714 | 2025-08-22 04:23:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d975bef4-0b83-368c-b05c-1137e1607a2f | -23.59017 | -45.67918 | 2025-08-22 04:23:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
