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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86135ae-4949-3ef8-a8b1-7edbe679c2a9 | -11.80238 | -47.09575 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5aeb765-19da-35a6-a38f-9a9401302c75 | -21.70523 | -48.4141 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36efc07a-72e7-36aa-b2a0-2383e1a16d2e | -21.03551 | -48.93807 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| e9d37f96-f83d-3cf2-abd4-cb56da1e0d95 | -9.56148 | -44.57571 | 2026-05-08 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b696717-04c5-3ab1-b0f6-14f4b2981adb | -14.14212 | -45.34019 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0fc4c57-a91e-39ff-99e4-faa9984c2c8d | -11.97952 | -46.7904 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a4c1805-74c0-3e8e-a9a6-fb4d25230cb0 | -21.0348 | -48.94217 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| bd2afa1f-134f-3aeb-ad2e-b4e751522ff6 | -14.13753 | -45.39062 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b53552-2db3-342d-b680-6c4e71d23bc1 | -13.64399 | -44.28529 | 2026-05-08 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8e66331-e90a-300c-9200-f78bfe07cc3f | -8.7041 | -49.07652 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8e1a45-0b3e-3748-8676-b8a36d0df0a3 | -9.45971 | -49.30714 | 2026-05-08 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b07bc3d-9baa-31b8-97e1-39c503c687b5 | -14.1381 | -45.38706 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c61c2842-3b6f-3082-a6d2-84f321a65e20 | -16.13311 | -44.29414 | 2026-05-08 04:17:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca0a9331-3bd5-3235-a1ae-2eb222d3f71c | -9.41042 | -50.68439 | 2026-05-08 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c724098c-64c4-3de4-8323-e01beea72165 | -21.03898 | -48.93874 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| fae26bf4-f332-3bc0-907b-207e31542bc4 | -9.47491 | -46.14469 | 2026-05-08 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72363162-64e9-3955-8fde-60d46a8cb560 | -10.67153 | -49.69585 | 2026-05-08 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc953d56-bb41-31f2-8497-13effc5e1c76 | -14.13316 | -45.37527 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff31a96a-0451-3850-8365-480971971cfe | -18.25158 | -51.2664 | 2026-05-08 04:17:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac17882a-4830-3fd7-a061-4c94bd6ffb0c | -11.82234 | -47.34432 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eed9253-a3fc-32ac-836b-0428ccd42f2e | -11.98301 | -46.791 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28632ab9-3173-3df3-9db1-3f249b5dd10f | -15.61829 | -46.51541 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 842baf77-51c1-3c9e-a8ac-0471bb5848cb | -11.80458 | -47.10453 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36283d5b-00f3-3f77-b249-d989045dd65c | -17.94476 | -52.96098 | 2026-05-08 04:17:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b11eef3c-dd8e-3c9f-9716-291c6c93e1a1 | -11.61305 | -54.17659 | 2026-05-08 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa95e25-ead6-32b9-bb9a-d1d1be1f63bf | -9.29905 | -48.58725 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe38b76e-d0cd-31db-8744-6c7e294ed632 | -14.14714 | -52.89015 | 2026-05-08 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55869fb9-440f-3eb4-a75e-b0ebad366716 | -11.79175 | -47.09392 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb55da06-45b4-3a42-9db2-167147b7616d | -9.46858 | -46.13961 | 2026-05-08 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e137f47d-0f07-35fd-8121-d544d7581427 | -18.51229 | -55.51313 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0f6dadd-4292-34ea-99ea-e02551be786b | -8.78798 | -44.8414 | 2026-05-08 04:17:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38fc2809-5ddb-3cd4-9c12-3e030831dc27 | -11.80171 | -47.09983 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21af8cc3-71de-38bd-8c0e-76245cec3e8c | -21.03757 | -48.94696 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9859dc3a-6d60-3988-9e85-3b15a8f9d315 | -11.61232 | -54.18038 | 2026-05-08 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d6769e5-b792-3ba5-8463-1cf2f7689a5e | -11.12556 | -45.11723 | 2026-05-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3df701e0-a2bf-301e-b499-d74b30c2f138 | -18.50699 | -55.51193 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b56531b3-2f50-30e6-aa9f-c66053720ccf | -12.86535 | -43.75742 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 604257c8-5a61-30a7-97a7-ed3cd97b7644 | -11.42562 | -47.08862 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| baef4b95-a04f-3a4b-8a3f-0a11a77dfbe7 | -11.63379 | -47.88165 | 2026-05-08 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c759247-57f8-33c4-975a-b21627b277e3 | -11.1355 | -45.14078 | 2026-05-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2369dc4-5a04-367f-9640-6eeea2c2730b | -12.50068 | -45.43469 | 2026-05-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fe84d04-528d-3930-aff9-c1cc342859e6 | -12.8648 | -43.76097 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a061ea44-36af-336b-9e75-dc2745ee279d | -27.9493 | -51.06865 | 2026-05-08 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cce7c6c1-1b05-3ddf-b499-f58f46dfed59 | -23.65444 | -47.07494 | 2026-05-08 04:19:00 | NOAA-21 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1dba688-4a27-3d34-b685-cf6d6e7c7eaf | -21.37746 | -52.29752 | 2026-05-08 04:19:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d14e6ab4-88f0-386f-89fc-6012c7d1f3f7 | -21.84528 | -50.34772 | 2026-05-08 04:19:00 | NOAA-21 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 524989d2-acd5-3e69-b0b8-e7bd0a9cb748 | -17.83656 | -46.51869 | 2026-05-08 04:19:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86989bb7-edc6-3d7d-9851-7672ab64b884 | -16.2853 | -50.34357 | 2026-05-08 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8095ab5e-d7c5-389c-a0a8-d6e5f36e8528 | -16.28131 | -50.34288 | 2026-05-08 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fd4ab00-e88e-37e4-819d-6fa354952794 | -27.94656 | -51.06358 | 2026-05-08 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2bbed597-72e5-3017-988f-45fa9874b1b7 | -22.34506 | -49.06392 | 2026-05-08 04:19:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad1598fc-8e1d-31a1-8525-a5d200f6255c | -22.37997 | -47.13422 | 2026-05-08 04:19:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 185be385-9121-3071-be48-cd022b7adc5e | -23.86448 | -47.4488 | 2026-05-08 04:19:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d121191-9c90-36a2-be28-c3db2c3a94c9 | -27.95007 | -51.06431 | 2026-05-08 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 542d9d1a-bd67-3e0e-99e7-f3cf3ce3b859 | -14.19629 | -57.42331 | 2026-05-08 04:19:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14cb1f5d-4513-3b02-b576-6e2bd5e5e200 | -21.84923 | -50.3506 | 2026-05-08 04:19:00 | NOAA-21 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b84a452e-a1f4-3f3c-86fe-881e7201b7e0 | -21.84557 | -50.34987 | 2026-05-08 04:19:00 | NOAA-21 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bf3e3a6c-c5d3-3026-81d8-00a4982f4ef4 | -18.01398 | -42.83247 | 2026-05-08 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ddbb9f0-9d5d-36ab-8215-73e85e022527 | -17.25235 | -47.07994 | 2026-05-08 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9198e9a-1964-3517-9806-0f683db2faa0 | -16.4264 | -52.79613 | 2026-05-08 04:19:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2cec4df2-8bc7-343a-b888-5457ef9bbf7b | -27.94998 | -51.06759 | 2026-05-08 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90e78739-b980-3a9e-9d7a-da35ebff1263 | -27.95075 | -51.06325 | 2026-05-08 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8867973b-84b8-38fd-8ae5-0f866d26f907 | -23.65503 | -47.07119 | 2026-05-08 04:19:00 | NOAA-21 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ef11f0ac-10ce-31e4-990e-0005c5d4f914 | -16.15432 | -58.48773 | 2026-05-08 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| fed6945c-3c80-3aee-97e8-e1e36c716f7f | -16.28462 | -50.34721 | 2026-05-08 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 563cd189-4a20-36ee-8095-9015f0c58029 | -16.28314 | -50.3432 | 2026-05-08 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 697c1f57-4b35-3a60-a807-6446041d5eb4 | -21.0427 | -48.9403 | 2026-05-08 04:40:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| b05cdfff-31e1-32f8-8565-f33d6b6f29ff | -9.29537 | -48.57998 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c771df4-d2e4-3680-9b29-82e06c197ad2 | -11.94468 | -43.38157 | 2026-05-08 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5ec8b20-9d59-3fd7-b27f-34db608fa5a5 | -8.70938 | -49.07975 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f94bfeea-26ff-3024-b7b8-480aa0a7d678 | -8.70883 | -49.08331 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3a0af82-80b7-38de-8f37-78ae9cc1867c | -8.79192 | -44.83182 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27986882-4011-395b-92d6-d010d1869dff | -10.94025 | -49.44865 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6dbd4c58-6f2e-34cd-8189-ab71510f5526 | -11.0657 | -49.47201 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3023258-4491-3e00-a28d-b0b9e84c071e | -9.30789 | -48.58946 | 2026-05-08 04:46:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3f15677-86d5-34aa-ae33-64677725643c | -8.69151 | -49.09541 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d96f0e5f-f2a9-3deb-86a8-58bcdc5a8e53 | -10.6713 | -49.70102 | 2026-05-08 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 948d089b-6013-3ada-9efd-1a9d644d024b | -9.41187 | -50.68231 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7fba95-880f-3df6-98d2-291d4141fee5 | -8.68815 | -49.09488 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4fab1ec-82e5-30c3-84af-eabc66609a27 | -8.70321 | -49.07514 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2eae851-98d2-3f04-87b8-550b62c48df5 | -8.71275 | -49.08027 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96c4bafe-c292-36a5-9942-ab84d6e397de | -9.30846 | -48.58576 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d29000c4-7bd0-3538-b91b-5dd240276141 | -10.40518 | -44.93516 | 2026-05-08 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0974ffec-bed3-330b-b50c-9ba80bcc6edd | -8.7847 | -44.83885 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c2861c2-7dfb-3bbf-bcba-53d85448098a | -9.87282 | -44.6893 | 2026-05-08 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2141b2bc-a4e5-3aa8-b7f7-da015a08688f | -9.30163 | -48.58472 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f790fed-96c6-309a-ac17-7d4423301317 | -8.79142 | -44.83544 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37aae776-1d73-3fc5-baa7-3f51a7c4d518 | -10.93744 | -49.4445 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52313c8-37aa-3408-a421-cc7d6c9a3fd6 | -9.73562 | -47.8938 | 2026-05-08 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a4a64a-3e4d-3750-8c14-dffbad81f8ab | -11.7682 | -43.65408 | 2026-05-08 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb7b9b71-9b43-3128-aa2d-fa42cd767e7a | -8.71219 | -49.08383 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30a2d558-d0d3-345f-b36a-63c702dfa9cb | -9.41409 | -50.68987 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6fc09c2-02e0-3506-80aa-ea2b48b15c98 | -11.42264 | -47.08984 | 2026-05-08 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae23766-e5e4-37ef-8f59-5e99710e326d | -9.41076 | -50.68933 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a2fe8a-8017-3b1e-baed-d356cf6bf67d | -9.25145 | -60.33638 | 2026-05-08 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c16a310e-495e-3287-bb96-9033b3bb9547 | -9.46933 | -46.13974 | 2026-05-08 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e426dd-0109-3f77-a5b7-2714ad141649 | -9.34853 | -47.08685 | 2026-05-08 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc8d1c97-24f0-35a3-bcbc-c3346f4c74fb | -10.04379 | -51.67028 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 799b3c9a-856e-3b8d-9fbb-3410d98d9a08 | -10.04042 | -51.66972 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35594d46-fd87-3179-8f8f-48715ba2fc71 | -8.68871 | -49.09132 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
