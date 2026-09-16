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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6669ce74-6903-3ecd-b9eb-e95768f2aa41 | -10.75923 | -44.82 | 2026-09-16 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a15412-a42d-3584-8033-a64fe2171600 | -11.21758 | -49.9497 | 2026-09-16 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c107ba66-579e-3cb1-8961-f0b1c7437e1a | -9.13928 | -65.84402 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2af2b54c-5b1f-3bc8-bb35-358c4d465db1 | -8.41079 | -54.72058 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e94685c-6363-3dfd-b687-69dc0e6505f4 | -11.24364 | -43.47739 | 2026-09-16 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93f86ed7-c9e5-3f9e-b540-4f01b91b5278 | -10.88507 | -54.0176 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cde57c7-c561-366f-a8be-718c7fdd4cd7 | -9.39013 | -60.30972 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3750b084-f5d8-32df-a1d2-bf583583d78c | -9.79643 | -46.49163 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2269beb4-4df1-30de-a537-a768c4a7b5aa | -10.75381 | -44.81796 | 2026-09-16 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfa4af94-e585-30d1-bd3d-fac0510ece86 | -12.13767 | -57.18747 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f7e9855-13aa-3260-9318-76332c128516 | -9.38607 | -60.30901 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aab6c9fb-a438-369a-b2ae-f2c35b5d3eab | -18.2387 | -55.38984 | 2026-09-16 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cb57fedd-a987-3902-a71e-c909b5f103c6 | -15.45253 | -53.77671 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a673104a-0c3b-3bad-974a-f353ed0a4043 | -15.48239 | -53.79384 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50a64159-ab2f-3867-9f2c-ab87534c20e8 | -15.99028 | -50.35409 | 2026-09-16 05:01:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39f061d1-1895-376e-9908-429af95476c1 | -15.52445 | -53.85686 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c1e6118-4800-3fb5-9101-478bccc53fbe | -15.46892 | -53.78765 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1221b30b-c459-3924-aa18-d01d7abeb300 | -15.26737 | -56.28833 | 2026-09-16 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b1088cb-3934-370e-9c09-c33f9e003a47 | -18.116 | -51.6958 | 2026-09-16 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4024dc07-c5fc-338d-b724-b986a017b632 | -15.51838 | -48.9306 | 2026-09-16 05:01:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73097cbf-eeb8-323e-9f70-0a66ade2997d | -15.5637 | -54.24008 | 2026-09-16 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b07d6f7-a34f-3bcc-9da5-ae4227366153 | -15.44433 | -53.78375 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a53aef0e-220c-3b9e-a44e-07f017174ee2 | -15.46599 | -53.78301 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f66bb25-44af-3045-9fff-c2b6093f7510 | -18.11193 | -51.69522 | 2026-09-16 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32a3b40f-d0f6-33ab-8e05-1f5862766488 | -15.45604 | -53.77726 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c27d4586-daa3-3c42-9b54-920e7c212efe | -15.33954 | -52.96507 | 2026-09-16 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d9ee8f1-b8de-3b02-a426-67d8c99aad3c | -15.62919 | -53.83139 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0c39a20-f328-3a9e-9088-2f4aeff0da86 | -15.44375 | -53.78784 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b2faed4-7103-303e-a318-3b6581dffac1 | -15.47887 | -53.79332 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 576ad420-c2c9-3a31-a66b-a5afffeed575 | -15.48532 | -53.79844 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61889aff-324b-351c-955f-44f676fef16b | -18.37876 | -49.3963 | 2026-09-16 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80aa2263-0389-34db-b223-dfb8f541ab57 | -18.64906 | -47.28747 | 2026-09-16 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f259df9-0605-3175-b842-fe35f62001eb | -15.51265 | -53.81368 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf2d0a2-5740-378c-8f45-e39948ea778b | -18.11647 | -51.69212 | 2026-09-16 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcccf341-0406-36f4-af86-e315d396f16a | -15.49818 | -53.80875 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 649320a0-09f8-395d-b589-93837a7f615b | -18.64869 | -47.291 | 2026-09-16 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac587575-7a0d-385b-bee8-161b98da7dbe | -15.5052 | -53.80983 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9334e0a7-3897-3b37-a5d2-2ed754f64663 | -15.49815 | -53.83358 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67da150b-9893-39b2-a550-641f102f915d | -15.50872 | -53.81036 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 264938ea-676a-335b-9d43-d0983eeff64e | -15.50913 | -53.81315 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbf8bfc2-1767-33ae-9c57-dffb779c8d64 | -15.45955 | -53.77782 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c51aaed5-4ba4-3f10-a2a6-6d421ff0035f | -15.50169 | -53.80929 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 237ff62a-5b0b-3138-af8a-f178f2fe2e5c | -15.51795 | -53.82694 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 179db9a6-6f3d-3b8d-83fc-fab3d9406ef6 | -15.511 | -53.85064 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84500358-9886-3b62-8e16-43c551f8f50a | -15.65542 | -52.72703 | 2026-09-16 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4214ae1d-383d-3b58-ba6e-dcc6ae3e4b3c | -15.47536 | -53.7928 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16bbda92-5f77-3c38-9ff8-f495ee882e8b | -15.46248 | -53.78246 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 336f2fa6-a6c9-3f78-8483-f0f868af7032 | -17.7266 | -53.04889 | 2026-09-16 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8ba47d7-1ed9-305e-9c2f-69cc099a1008 | -15.47595 | -53.78872 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db7719bd-526a-3df7-8c10-913696a32da5 | -15.5099 | -53.80223 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01e4fdbe-306e-3fbf-85c8-31b149e71f22 | -15.50806 | -53.84605 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69a1b18c-b739-32d8-a084-1fa755bc3585 | -15.52795 | -53.85743 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737e8d23-546e-3be6-a3ee-b1570d1bd48c | -15.49467 | -53.80821 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b67099f-6d03-3994-9b36-5e45e6399dfb | -17.5479 | -49.42509 | 2026-09-16 05:01:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac400c2a-6e27-3750-a036-15536f5a819e | -15.49873 | -53.82957 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56ec0fc6-8650-3fcb-a695-1f598e91b1f6 | -15.53847 | -53.85907 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 188cba4a-ab87-3698-9692-64604422de8c | -15.51086 | -53.80095 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06f15b16-0448-3888-9b39-3140807c0147 | -16.76001 | -57.09437 | 2026-09-16 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 264567ff-3503-3336-884f-b25c15585e74 | -15.47243 | -53.78819 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fdfc314-60a3-34c9-b3f7-99d4eb35877d | -15.49759 | -53.81283 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514940d2-79d2-3bf2-8891-f91b9e54f61f | -15.45897 | -53.7819 | 2026-09-16 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0e05ad3-e4c7-3aab-85d9-055bc42f2c53 | -6.3257 | -62.6721 | 2026-09-16 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 50d096e4-d302-3d33-b5e6-7eb5c955ee1c | 4.75136 | -60.56658 | 2026-09-16 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b96282b8-a90a-3ed0-89da-db0b7a04fe42 | 2.6985 | -60.29869 | 2026-09-16 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b60a3253-614b-32c4-af8d-2372d13a5f8d | 1.18363 | -50.93761 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 003816a8-88fe-3a73-904b-2854751f2792 | 1.34859 | -50.63637 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6eef18f-7e18-3709-b7f9-ea47dcc47b30 | 1.18053 | -50.94943 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b7e04b0c-f2a4-392f-b6b4-1b6c669c3c1b | 2.58043 | -60.30145 | 2026-09-16 05:31:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc71e486-438f-3f14-84bc-69f33297be9e | 1.17179 | -50.96315 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 06efffec-1b0f-331f-b782-d4c5770015fc | 1.97493 | -50.95535 | 2026-09-16 05:31:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98911500-1ce2-3878-b7dd-e0ba701a94f4 | 1.1756 | -50.95021 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 554b222c-17a1-307b-a688-7d22ac7e44e2 | 2.581 | -60.30512 | 2026-09-16 05:31:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25f9fef0-398f-365a-a0b2-f2d133ffb09c | 1.17989 | -50.9505 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 484063d5-f438-30b5-a5ef-f669ee3266e2 | 1.25206 | -51.01655 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89215bd-4170-3a72-a98f-3023dd916430 | 1.17903 | -50.94503 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a2110ca-503f-32cb-a72e-0555fb67d627 | 1.18395 | -50.94421 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 29.5 |
| a677db55-300e-3fff-9399-a3ff375a61bf | 4.29281 | -60.60792 | 2026-09-16 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594d3bd5-40a1-3b3c-92a0-de1a98820a4a | 1.18454 | -50.94314 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 13b79943-29da-338f-9570-79c399faa9bd | 1.17962 | -50.94394 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| de1cc4e4-7dee-384e-985a-d79df58b9e3b | 1.17584 | -50.95682 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b440580-258e-3183-b77e-be3dda82cae9 | 2.60877 | -61.43323 | 2026-09-16 05:31:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873a88ea-5988-3746-9f8e-7e79e6d2b567 | 4.74786 | -60.56719 | 2026-09-16 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0071a778-301b-32ff-b6ff-e97b59ccac4e | 1.1725 | -50.962 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca79b58a-f255-33cf-89df-caaea364d109 | 1.97404 | -50.94996 | 2026-09-16 05:31:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dd7a5e4-2970-3be3-88ba-44ffb3f8f052 | 1.24148 | -50.88837 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55c6546e-d2a9-3cd6-8b5c-cb9581762d8e | 1.24553 | -50.88203 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28a965eb-7fdd-3e41-b4dd-c57282d249c8 | 2.20467 | -50.89281 | 2026-09-16 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75985145-ae5b-36d5-914d-4191c9cc7410 | 2.20954 | -50.89202 | 2026-09-16 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d9b5554-2a97-3a1e-8dd9-d529368afd1f | 1.17497 | -50.95131 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4de18896-92f8-3e7a-b455-14dea8d47117 | 1.18308 | -50.93868 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 955c189a-3238-38e3-ba96-c604b1817f3e | 1.17342 | -50.96747 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba95fd2d-d286-306e-8bf2-47468d168355 | 2.70192 | -60.29816 | 2026-09-16 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c1f469a-c414-3dff-9b3c-d49f9df33d5c | 1.18856 | -50.93682 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e68ee86a-9e5a-336e-a71e-cb88c58bc01d | 1.18801 | -50.93787 | 2026-09-16 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3b115d2c-02b1-3397-8d6a-0d97f154c84d | 2.58385 | -60.30091 | 2026-09-16 05:31:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7282ce31-81bf-3134-b5cf-b96ac100cc9d | -5.15099 | -55.92865 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cb5fa3eb-0666-3f1e-b74a-2de7fe7ab1d3 | -6.3682 | -54.96779 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7789d80d-768d-33b8-a157-434f32a1d289 | -3.72406 | -58.86663 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f564b336-4f44-334a-8e04-404943c0c95c | -5.10235 | -47.61222 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9ab99b05-4caa-3fc6-a6e2-269cf9841ea8 | -1.61233 | -55.5705 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README50.md)
