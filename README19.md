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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6ccfb77-a567-35d8-9df5-0687f7f12d5f | -11.9641 | -50.3747 | 2026-07-23 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 04801dce-97a9-3eb5-a466-f1218ada43d3 | -11.6789 | -50.3651 | 2026-07-23 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ad601a28-6e30-3d2b-bd35-e165a06e9910 | -11.9451 | -50.377 | 2026-07-23 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d1451807-305d-350b-886c-eb17c1f89059 | -11.6599 | -50.3673 | 2026-07-23 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| de41c649-a94f-39a0-a59f-ac446b2526f0 | -11.6789 | -50.3651 | 2026-07-23 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 9bbdbcfe-069a-3454-b814-a68e92960e17 | -11.6789 | -50.3651 | 2026-07-23 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 5c6719f7-5750-37d2-850c-772ecce3e06a | -11.6599 | -50.3673 | 2026-07-23 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d31f2ee0-8814-325b-9bf4-d55911cd849a | -11.9641 | -50.3747 | 2026-07-23 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 17f7ac9e-e94a-34e4-9f5a-d1dfeff0ea33 | -11.9641 | -50.3747 | 2026-07-23 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 14eb6822-af6f-30a3-a263-a014adc76659 | -11.6789 | -50.3651 | 2026-07-23 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 805a6b45-dd18-3b41-b19a-1809221c29be | -11.9641 | -50.3747 | 2026-07-23 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 588b7ec9-aa55-34ee-b42f-98120d2470f5 | -11.6789 | -50.3651 | 2026-07-23 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 70cc480b-9b19-36a7-94a9-5fb39bcf8d66 | -11.9641 | -50.3747 | 2026-07-23 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 1bd2adbc-247b-3946-9698-17264c46e35b | -11.6599 | -50.3673 | 2026-07-23 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d7387a5a-0f78-3bf9-b713-8eadcf1396e5 | -7.2531 | -39.26687 | 2026-07-23 11:21:00 | TERRA_M-M | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4c1a0d25-89ac-3948-bdb7-644a0e02c49e | -7.25438 | -39.25785 | 2026-07-23 11:21:00 | TERRA_M-M | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cb879a77-7e94-3191-a30d-4b41482e5afe | -11.78018 | -47.09699 | 2026-07-23 11:23:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 472ef4de-7d66-3a3e-ab52-8d97f9c342b6 | -12.38831 | -50.39588 | 2026-07-23 11:23:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 060d6ac5-4781-3fdd-b021-b7f5a37cb21f | -11.39086 | -47.47231 | 2026-07-23 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3081ae35-2f1c-34c2-af3c-980cd6bcf29b | -14.62111 | -43.75747 | 2026-07-23 11:23:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a014514f-ce24-3b4d-8898-d1b07a0f0d68 | -11.82072 | -47.33674 | 2026-07-23 11:23:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3f15b9f1-f39a-3b5b-8ce2-069c841221cd | -14.74587 | -43.54067 | 2026-07-23 11:23:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a143fa2b-6bff-3310-b593-1525435c40bd | -14.47113 | -42.47069 | 2026-07-23 11:23:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 33933a27-8ee8-3202-85b9-14ea8770daae | -11.39032 | -47.46677 | 2026-07-23 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8a6313a3-43b1-36b4-a97f-8b0a3b503402 | -11.65657 | -50.37665 | 2026-07-23 11:23:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b56ba132-5f9f-3041-90b1-c73f7f4cd192 | -10.42265 | -46.55987 | 2026-07-23 11:23:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 39bd04ea-a102-364d-8e3d-ea004a854a83 | -11.6623 | -50.3442 | 2026-07-23 11:23:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 2c7768b9-8e77-3c25-8e8a-b13e92e8a59e | -17.60175 | -44.61623 | 2026-07-23 11:25:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 12daa374-7971-309a-a946-fad0b22da0c3 | -17.58552 | -47.50307 | 2026-07-23 11:25:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 577c2580-faef-3e43-8ff7-75de4496c133 | -17.60334 | -44.60587 | 2026-07-23 11:25:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 691c6e9a-d1ac-3354-ad88-96275a546a23 | -20.16348 | -43.92238 | 2026-07-23 11:25:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 53c0d90a-7374-3818-a02b-d30920ed7274 | -17.41927 | -43.81234 | 2026-07-23 11:25:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 93256033-588e-37f7-902f-cee5a967118f | -21.02638 | -40.89465 | 2026-07-23 11:25:00 | TERRA_M-M | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| d8728da0-e858-3732-872b-2004d6976da3 | -21.67904 | -41.59162 | 2026-07-23 11:28:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e2d870b4-6683-3385-95f5-434083008cb3 | -21.68736 | -41.58821 | 2026-07-23 11:28:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 43011270-f0d5-3cfc-ac6b-ed2b3d76f253 | -21.61492 | -41.58183 | 2026-07-23 11:28:00 | TERRA_M-M | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| df8ed359-cac6-3f26-b071-f53e28b6ed66 | -11.6599 | -50.3673 | 2026-07-23 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 17ada82e-9eed-3440-bf04-0d3ca94613d7 | -11.6599 | -50.3673 | 2026-07-23 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3254a5e3-185d-38d0-a3ef-bbef57a20377 | -11.8576 | -60.6999 | 2026-07-23 12:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9b7aa33b-32cb-3859-9bdc-7e16195e3887 | -12.3833 | -50.3888 | 2026-07-23 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| faa125ad-f95e-3421-9e46-f388f9f01aaf | -12.3833 | -50.3888 | 2026-07-23 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 38efeb51-7cc1-34df-ada2-757255cf0575 | -11.8576 | -60.6999 | 2026-07-23 13:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ae049827-de7f-31dc-9335-d95594c4e73c | -8.82985 | -63.90129 | 2026-07-23 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26def7ed-7a51-39eb-bfa9-202638f0e219 | -11.86129 | -60.69434 | 2026-07-23 13:01:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b70bbab1-d97f-3737-8274-1dedad346be0 | -11.33605 | -62.22514 | 2026-07-23 13:01:00 | TERRA_M-T | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bcad5e57-3910-3c64-b862-b1e9d56d8fe0 | -11.85934 | -60.70979 | 2026-07-23 13:01:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 201a9f74-eb9a-3f4b-a31c-238c8b81503f | -11.84979 | -60.69286 | 2026-07-23 13:01:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7c8f2bea-c6fd-3e02-9878-6d12a1484189 | -8.79435 | -63.82401 | 2026-07-23 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03d20bc1-57f3-379b-bbb6-9bade5425eea | -11.84785 | -60.70836 | 2026-07-23 13:01:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 518c2900-dcf6-320a-874e-1e1116ea39c4 | -8.80409 | -63.82193 | 2026-07-23 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f521065-9dc9-39db-8be5-921dcd718b3e | -13.3555 | -54.2973 | 2026-07-23 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d9500c6e-3a54-3811-b7c5-71ffb1f5074f | -9.5277 | -47.1187 | 2026-07-23 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 48baf4a3-04b3-32d9-8482-e5800dc2e9ee | -13.3743 | -54.3159 | 2026-07-23 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c8a352da-2d42-342b-b857-afb2c5b26038 | -13.3552 | -54.3179 | 2026-07-23 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| edfdaa26-901a-3805-ad9b-b8ffa3ed9417 | -11.9451 | -50.377 | 2026-07-23 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 03ce2994-ef9e-3edd-83bd-bbb2a9ae7ebc | -17.0609 | -45.043 | 2026-07-23 13:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d3551a25-8d2c-3376-881a-f328292a66e8 | -11.9641 | -50.3747 | 2026-07-23 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6ccbf25d-2617-329d-9acd-ae26b0106b25 | -13.3552 | -54.3179 | 2026-07-23 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 83bce552-d230-3b02-9e8b-328526d061f1 | -13.3555 | -54.2973 | 2026-07-23 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 02aa62b7-7109-3000-b50e-47690e5b7347 | -11.8879 | -50.3837 | 2026-07-23 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ac618493-7b5c-3bbf-ab3e-3acf1b96e7f6 | -17.0609 | -45.043 | 2026-07-23 13:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 408c9b39-fb2d-3875-ba4f-cdc76df91d5f | -11.926 | -50.3792 | 2026-07-23 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 38b51787-ed04-3c17-8793-2db25216b2d7 | -9.5277 | -47.1187 | 2026-07-23 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| dadf7a97-aa91-38a3-b380-9449e113e4e1 | -11.9451 | -50.377 | 2026-07-23 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 432a5bdd-4cf5-3666-99e3-fa8798bdba52 | -11.9641 | -50.3747 | 2026-07-23 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 2b61e94b-2520-3ca8-9d4c-743017048380 | -14.3117 | -52.0889 | 2026-07-23 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a728c65a-d2ec-3d1e-9179-fbff8047e112 | -9.5088 | -47.1208 | 2026-07-23 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6a1a3fef-92cd-3040-b130-0e1677134108 | -11.9641 | -50.3747 | 2026-07-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 08ac5cf8-0d3b-389c-8eae-024249471cc4 | -9.5277 | -47.1187 | 2026-07-23 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 66b3fc3d-d5ea-3671-9bda-14cb79599d6e | -12.3833 | -50.3888 | 2026-07-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a3c1eb3a-385c-35ba-95a5-5db80ce94238 | -11.8879 | -50.3837 | 2026-07-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d84d5df5-d377-3b0b-b5d8-30de69f28838 | -11.926 | -50.3792 | 2026-07-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 97348499-3257-3160-81a4-ff421ea1e36f | -11.9451 | -50.377 | 2026-07-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| dc110c53-0b44-34ae-98db-1d76257fbad3 | -8.8026 | -49.3748 | 2026-07-23 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e8b534ea-6b81-3397-8d07-f646fb9768e3 | -17.0609 | -45.043 | 2026-07-23 13:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 2be27785-0713-3823-820d-c14d4e79bc5c | -15.7254 | -48.2299 | 2026-07-23 13:50:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4b66fe9e-191b-30f5-b46a-7c7a7108e399 | -11.9451 | -50.377 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| f23e5697-5e6a-3925-adc6-da4b5b153ab8 | -11.8879 | -50.3837 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 4a79e663-4a92-38f9-b20e-0aeb0c22f508 | -9.5277 | -47.1187 | 2026-07-23 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ba1a57de-1d0b-3a17-8f10-cd32840dc581 | -11.6599 | -50.3673 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6f68ba6d-a6e5-3bfc-8322-aa6af47bb36b | -12.3833 | -50.3888 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6d67bdb3-6ca3-3be6-bb9a-0bb1937dd8ee | -11.926 | -50.3792 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| ea0c1129-db01-3a76-b2f6-80412fdc06b2 | -11.9641 | -50.3747 | 2026-07-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 016a4345-b337-3a3e-b0d3-40878485f4d3 | -17.0609 | -45.043 | 2026-07-23 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 7cb93b1c-c612-39d9-ac6b-e1041cbee10a | -9.5277 | -47.1187 | 2026-07-23 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b23c1b02-f050-32c9-a720-93fd04d5ffad | -12.3833 | -50.3888 | 2026-07-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 56a334f6-e5f7-3935-acd0-0950a7e8ecb5 | -11.9832 | -50.3725 | 2026-07-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8ed7892e-e629-3f36-8169-b9e1e1e8efc2 | -11.926 | -50.3792 | 2026-07-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0d3fb648-8417-3b28-a01f-c42a7df6d289 | -15.7254 | -48.2299 | 2026-07-23 14:00:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9f0043a9-6044-3223-995f-e52abb76f7f9 | -11.2642 | -50.155 | 2026-07-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b101419c-467a-3e75-aae2-1916f6bb8cb9 | -11.2449 | -50.1786 | 2026-07-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 6b64ac3c-f744-3162-834a-9cf6d291afc5 | -11.9641 | -50.3747 | 2026-07-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| bf3b6d74-67fa-36a9-b52a-20cd09b7c35b | -17.0609 | -45.043 | 2026-07-23 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| faa76309-42fb-3351-99e4-a86f580e0c86 | -11.9451 | -50.377 | 2026-07-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| c74e877b-ce03-3b53-9259-eaed32b43792 | -17.0609 | -45.043 | 2026-07-23 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d1117e47-9b5e-3309-b52b-49c9ac1513c9 | -11.8879 | -50.3837 | 2026-07-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3f02d613-0880-3607-afdb-0c06141acd6c | -12.3833 | -50.3888 | 2026-07-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bae429c4-14fe-3ac0-9d9e-5d73c0e26e46 | -11.926 | -50.3792 | 2026-07-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3eb4f217-358c-3fa4-ab3b-0cc09cc69442 | -15.7254 | -48.2299 | 2026-07-23 14:10:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ef8b8155-4ac8-30d6-bc97-0b7a48193ebe | -9.1752 | -59.0744 | 2026-07-23 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |


[Clique aqui para ver as próximas entradas](README20.md)
