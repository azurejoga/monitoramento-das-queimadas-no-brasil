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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c704f00-6573-3a57-aac8-c5410b2fc215 | -14.62034 | -52.03597 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51136bd1-4fec-32cd-b0ea-a6e61000eebd | -14.74927 | -45.25756 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd106d54-3d15-3c36-acb9-fa381ad6a779 | -15.9255 | -49.97844 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6fbdbd65-85bc-3533-9c3b-e6ed60e5f769 | -6.20564 | -44.51595 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1481888c-c23d-31e6-883a-fa298346cb88 | -5.73067 | -43.19104 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91dd6c95-b5c4-3a0f-871c-ec69cc5cb918 | -11.91301 | -46.52866 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 355b5b9b-ba55-3662-abf2-1aafa3a901b6 | -12.81668 | -47.15718 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43c63aa3-6772-3ef9-b09e-53e78acb731e | -12.1438 | -47.58775 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d734fa-78e2-3816-80ac-2bcb3c963e00 | -13.00802 | -46.74527 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ea47d57-92fc-39ad-9d01-505475a2029a | -12.72418 | -48.02971 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26186fbc-3a09-3647-813b-2c105e7ff6c6 | -6.10928 | -45.93555 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d44788d-eb5e-3153-8a16-c1cc7b9b6a92 | -16.3274 | -51.5277 | 2025-09-14 03:49:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85f6c2ba-e352-37e9-9ed3-5200b117f4c9 | -5.97961 | -43.7785 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd30993d-cc8e-3ef4-a523-a23929859a41 | -14.60021 | -46.33094 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90c9e5a8-b425-3731-8457-988f24c25271 | -14.14437 | -45.40916 | 2025-09-14 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e58aafb4-b226-310d-aedb-9d1e0c144138 | -17.3891 | -42.63097 | 2025-09-14 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a225e66-7d7f-3fb3-8564-37bec271765a | -14.43817 | -43.20907 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 671d4d1c-7a54-3fcc-9c6d-737e3fd7aebc | -14.45341 | -47.30953 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0ce4591-dfa8-3995-bb66-5c32b0f35e62 | -18.01778 | -46.96561 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b540f1a-70f5-38a7-bb3d-2573ac2aaf8d | -18.06929 | -45.41645 | 2025-09-14 03:49:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be2be8cf-6c8b-3f24-a9af-f3a4bd022088 | -12.77369 | -48.01046 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| af72c0f0-1c45-3589-a4b0-6a146de4083e | -12.96787 | -48.03807 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1ff8ddb-b478-3559-98b0-ba336514f3b4 | -15.63582 | -51.35019 | 2025-09-14 03:49:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbdd7d8f-eba5-325a-844a-bc3b6aa48204 | -15.60276 | -47.94727 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| be482225-9d54-39ec-9aa5-718a60c3c142 | -15.76076 | -52.24561 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e49ab999-b3d8-3133-baf0-737d890db2a4 | -15.7647 | -52.24563 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f47c7ccc-a145-3e37-94a4-44583c5c8e23 | -11.91246 | -46.53155 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8d9a03c-1d39-3b0f-a139-210f0ff55a57 | -12.77443 | -48.00676 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6b641f51-5d42-3c96-8ab2-d10413d1ac7d | -17.9945 | -46.96152 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d285d5b-b66c-3820-87b7-860ea9c9cce6 | -5.95552 | -42.79128 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a6e6841-075c-37b9-af6b-beb8805e928c | -17.94086 | -45.26334 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45bd661d-5594-3454-9388-165815701ce6 | -13.26072 | -43.79173 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ab62172-6716-36cd-a12e-7c7af55535ff | -14.42295 | -47.34167 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47f8c20a-0174-37dc-9753-b188432aef9a | -11.24307 | -44.77165 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 071f9ef8-7238-3981-9620-d40ad3cb1538 | -14.17334 | -46.15807 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bebc2e14-4bbb-308d-be44-0851a9989654 | -6.67799 | -45.52061 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d83fa34e-29fe-3087-ae42-754273dd53fc | -6.28167 | -39.68908 | 2025-09-14 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b51f57e7-2b11-3a13-b000-266d7267b455 | -5.79706 | -43.88847 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 098840c1-1bd6-33bf-9057-f3aaae85835d | -10.8797 | -48.18938 | 2025-09-14 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01b3c048-8fc6-3def-8de6-7fd13fba109f | -12.92629 | -47.95874 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1956b3a1-282a-382f-aed3-8422c31577da | -15.12294 | -52.48508 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fc12618-ba40-3e42-b79e-55bc82696600 | -12.9602 | -47.98705 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ffdea4-0cd2-353a-b92e-3b71f0658f5a | -12.24887 | -46.79314 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6607b343-e5e0-3329-90b9-9e397b9a9f52 | -15.92814 | -49.97057 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 03f1e0e1-83ac-3e56-b59e-76311e390a74 | -12.97055 | -48.05033 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36320380-1380-3eb6-a457-3c493de73f07 | -15.15541 | -52.47092 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59aedacd-4429-3585-90f9-8d78090e228b | -14.19214 | -46.16212 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91fa9bd9-a5f8-3f58-b1ea-5c27e4843433 | -6.79933 | -43.40045 | 2025-09-14 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99ae2b27-4e0c-3b56-b1f0-a1867fbebe51 | -17.9981 | -46.96766 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 434a209e-1f00-3799-a012-663009f23577 | -14.47639 | -47.32639 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 997a4f02-5aa5-35fa-b432-dfea966bec95 | -14.63872 | -52.1118 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a652c4a-6de2-3f14-957b-83df1e5aae33 | -15.43502 | -47.3434 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19211453-3a21-3f33-85ff-01a49751b710 | -12.69825 | -48.30056 | 2025-09-14 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cb3652c-b9c7-30fc-88a6-3c3e3329f1df | -11.34112 | -50.8293 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41be4aa6-9afc-3d38-a9a0-38cfd5ce5646 | -11.35198 | -43.49477 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd0ea2b1-bed5-394f-8930-763c400bd1c3 | -12.57439 | -45.6608 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b3512c9-3724-3cdb-bbb4-5126cd5cbf51 | -10.76289 | -46.47684 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab4f5f3-328d-3309-b578-087fb04799af | -11.39778 | -43.52686 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ef950cf-97e6-32c3-8372-28b3dbab79b0 | -11.14126 | -45.32602 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e983aa79-193d-3bc1-b252-a463a23be38d | -5.79236 | -43.88777 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 245cc91b-1590-379b-a349-f8906b026ffe | -12.12564 | -44.82352 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a781f0de-87ca-361a-9151-2117bcb0fe30 | -11.36423 | -47.34235 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 008e646c-1c90-38cd-8255-faf517f4a382 | -7.15116 | -37.32142 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOSÉ DO BONFIM | PARAÍBA | Brasil | 2514602 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20773beb-4abd-38c3-86e7-6a1d8cd47d93 | -18.20578 | -42.57524 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5751fcd8-0540-32cc-ba5e-a05cc4a8140b | -18.05946 | -45.42235 | 2025-09-14 03:49:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc58cd29-96fb-3a45-8ca8-df2f2bde81a8 | -14.61927 | -52.02996 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dbfb5f5-0ae6-30c2-bb96-df8701e815ce | -6.17558 | -41.14711 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a94248c0-172d-3a5a-82b7-f9189c563a84 | -17.29978 | -46.10868 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c751ec02-9e94-3068-8bb8-f3eab1c0dd23 | -14.15699 | -46.24455 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d27ee1bd-ee19-362e-80b2-e7b973b67a67 | -12.25007 | -46.78697 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c144d87c-04df-3617-8ae3-6c13b153425d | -14.63535 | -52.11864 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d26d40-5ae3-3f5e-8bfd-adc7ac779d57 | -12.08421 | -44.73317 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28449454-fa19-3a70-8be5-d41efee1f979 | -10.73864 | -46.43637 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e67efd9-3e19-3e75-9aa5-7eaff54ef63c | -11.4484 | -43.563 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5dc3a97-cab8-35be-9ddd-741b9ac77a3b | -18.29696 | -45.10668 | 2025-09-14 03:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02041367-f582-3fca-b846-43289310e5ee | -14.18732 | -46.31828 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43caa2b1-b341-3397-a983-38e4838cc44b | -11.38372 | -47.34065 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e66d1fe-5614-3044-91bc-6a90bc1aa8cf | -15.79263 | -52.21375 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5beca76-212b-3d9a-86bc-f4f26f23a0ff | -12.14173 | -47.59845 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16bafd62-2c3c-32c4-89d5-b0241ce8dc4e | -11.48252 | -43.61333 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba252659-cc57-3fe3-a5bf-3525a98551c6 | -15.17649 | -52.47252 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18b17a2d-1051-3c58-b1e7-122a0931ac85 | -12.76664 | -48.01561 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3ac63a0-7db1-3fe6-9b49-41c7878541e8 | -11.8919 | -50.54226 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 091df6a7-9eca-3fb2-aa7c-352afd203097 | -14.31124 | -46.07951 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d433d26e-1234-3e31-b462-e29e2784eb3a | -12.73649 | -48.02479 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 419b62ca-5ee9-3bba-90a0-59065af78544 | -14.62282 | -52.07854 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96af5aae-b282-33fe-8256-155567433e79 | -12.77759 | -48.01762 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efe22d16-0f61-3973-bbc1-45f077646d59 | -13.0135 | -46.74372 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 783ca37d-f80d-3802-8515-12f14e2815ed | -10.40242 | -48.61096 | 2025-09-14 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5c7fb96c-d37c-302d-8d34-a017efb2ef5d | -12.08998 | -47.56517 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a59ec8f2-14fc-3cf6-b321-6af805236801 | -12.78416 | -47.98318 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5de72e7-a34e-3739-b1b2-b1c15c54c13a | -5.96401 | -43.21666 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e73b00f-b92b-33c8-b1ac-cb63b11f441e | -12.78814 | -47.13838 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd34f781-f257-3671-a641-5617ccd11b04 | -7.11268 | -36.4883 | 2025-09-14 03:49:00 | NOAA-20 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27831b1a-6d6f-3445-b982-836a53de2a6e | -18.06269 | -42.58131 | 2025-09-14 03:49:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd371916-0add-3e22-aafa-d31394ab20a8 | -12.7783 | -48.01389 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dc6c3317-08d0-3574-a792-a4bd0b80c555 | -15.66688 | -44.69965 | 2025-09-14 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a427996b-cf6c-3a71-9073-8f52d11765e5 | -11.49993 | -43.63699 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1381bba-b16a-3bac-9eca-b2f052b5efd3 | -17.06859 | -47.1611 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beea42d0-5e56-39f8-8190-ae4bea8243df | -14.40463 | -43.23684 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
