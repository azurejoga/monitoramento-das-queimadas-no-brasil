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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1e2ce49-0228-3bc1-86d0-86a3ee40e9c1 | -9.95257 | -49.28447 | 2026-07-03 04:19:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31a41655-fe8d-3923-ad02-72b39a308f22 | -12.50842 | -48.28016 | 2026-07-03 04:19:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e83f67db-5113-3902-835b-96907c9d0e5f | -10.94049 | -43.0497 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 342010a1-d588-34c8-b549-e98ba9d4e671 | -5.79643 | -45.0475 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce427d27-62af-3b0b-a877-103bff907710 | -12.50032 | -43.80857 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8180767-5bb1-3892-b5a0-7014fe3ac37b | -12.75055 | -44.53001 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ebcb0a88-1250-3391-b0ec-2d2337c64120 | -5.79823 | -45.03631 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7fab42b-30be-3843-8519-dd125da670f9 | -5.93942 | -43.47103 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d591d6-7cdf-3a9f-bea8-8ce792d8cde2 | -10.94664 | -43.05435 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7064bdc7-ab16-3b78-a5fe-3f5957ca64b3 | -10.93769 | -43.04558 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b05690-61ff-3975-82cb-d4f81a6f185c | -11.29553 | -48.92729 | 2026-07-03 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4aa4b38-c3c8-3553-a86f-ddcf716e286e | -5.81132 | -45.04232 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d02f9fe1-68f8-3768-b9ee-27b4d43e94df | -5.7949 | -43.63267 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7ab607-eb4c-3ce0-8cd5-4fa5bd17e96a | -12.32022 | -46.73908 | 2026-07-03 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c46eab-7071-3bec-a69e-c4ccd76a42fe | -11.29465 | -48.93228 | 2026-07-03 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97fa5349-830b-3eaa-9fba-9bae6775040c | -5.8079 | -45.04176 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 08bfca78-3337-3360-8670-d30983b56942 | -12.35594 | -47.43293 | 2026-07-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 871e77ec-d316-3cd1-b27d-45d2d52caf44 | -10.94719 | -43.05075 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 680bb8c7-2aef-3789-98ad-b0dd96a25051 | -11.43522 | -46.53303 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3fae56f7-5222-3408-9e43-34eaea813b8d | -4.01436 | -48.06045 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 64794a4a-d302-3f7a-9294-c7f2c9b3cb31 | -11.34806 | -55.41546 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54885dcb-f280-3ee5-8bd4-018b781a54f4 | -12.75607 | -44.51647 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 8b867337-0d8b-3f3b-bec6-a61cadfb8219 | -6.03458 | -42.61197 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 55ac667e-66b1-303c-889c-d9bd55707bd7 | -10.89806 | -56.85627 | 2026-07-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dcd2689-8b52-353f-9945-83224f1da67a | -17.26 | -42.6576 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15887f5f-7e3b-3b4f-8f91-f59a9e1461ae | -13.30294 | -43.55583 | 2026-07-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d5b200b-66b3-3a98-971a-f5fe42f7be2b | -17.30816 | -42.64192 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 409a6ee1-6abd-36ed-b236-4059b5e4fa8c | -12.85121 | -44.40941 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f14eb83-ffae-3126-8b28-04f2d6cc18a3 | -9.75504 | -47.88115 | 2026-07-03 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd66406e-8735-3ba0-a243-5a3b8a876117 | -5.46904 | -45.41984 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7db91ff-9cc7-3dc2-80c3-4f7f95ed619e | -5.47253 | -45.42038 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4f32dff-cd50-3a66-9f2d-4de3f7dd2bfd | -12.74616 | -44.51485 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c8ee33a-0532-3c07-85d1-75435d148a98 | -11.49832 | -54.50565 | 2026-07-03 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c40d5f71-800f-3a58-b11a-b546288cf56e | -12.74944 | -44.53704 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5dc26604-1e77-39a1-a034-a51c69c3b565 | -5.80045 | -45.04435 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| becaeeee-98f1-331c-afe7-ecdf126559b1 | -5.80153 | -43.63372 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aac4c516-34b3-3129-883c-fe4170dadc32 | -5.79361 | -45.04321 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad116ae3-2266-3ca5-bb0f-9aff28e538cf | -4.00607 | -48.05935 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 798a827b-ebe3-3485-a72f-de85303ef5b5 | -12.74449 | -44.52541 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c9046a-9a08-310e-b845-9b9fa0659113 | -11.91741 | -43.3867 | 2026-07-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b7aa5b2-d40d-3896-8e56-3be4857084f0 | -17.30576 | -42.65887 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ce17296-ac35-3da5-884d-bc1849fba07f | -9.75878 | -47.8818 | 2026-07-03 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c317df6e-cfc6-3ac1-b191-96b83fa3a8b1 | -5.79103 | -43.63562 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c19917a0-3f41-3e7a-9e5f-9d70c57d9ae9 | -5.3044 | -47.24397 | 2026-07-03 04:19:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cf3e5f3-d908-321e-809f-bf9ff5bef977 | -5.78599 | -45.0687 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 768a2512-8e50-319f-af92-760f8c4d48a8 | -11.41293 | -56.06798 | 2026-07-03 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4895972b-f414-3496-9035-6f67c1b4b645 | -5.64012 | -42.59241 | 2026-07-03 04:19:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c16edeaa-69ee-3391-a3c7-f44db012bcbe | -11.34298 | -55.42631 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f3f6ae-43a2-3ae6-9806-1f914654dadf | -12.75552 | -44.51999 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 48872994-2075-3ac5-9057-e2e1290183b4 | -17.30755 | -42.64619 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c101b0-2bc9-328b-b60b-13757dd4f292 | -11.35156 | -55.41392 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 239c842d-f1cd-316d-8f14-f1976cd0cd9c | -15.68817 | -43.28869 | 2026-07-03 04:19:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e5aa369-45b0-3af8-8fc8-b22d993d2d45 | -5.53106 | -43.94497 | 2026-07-03 04:19:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1faa7bc3-0cee-36d9-91b0-8010aab31f4c | -9.69658 | -48.59994 | 2026-07-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fffe6904-9f2c-3493-b43c-15d04f42a468 | -13.3035 | -43.5522 | 2026-07-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8282afb-f81c-381d-b5eb-5b3127be978b | -12.5042 | -43.80555 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9dd7801-e8e4-3075-ad40-26e4b925aa4e | -16.77254 | -48.52444 | 2026-07-03 04:19:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a18bb40-f0b3-3a83-822b-8bb17cda2c44 | -15.6876 | -43.29255 | 2026-07-03 04:19:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2bc1db2-2db0-3bc9-9bff-752c94c732b0 | -12.75332 | -44.51241 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 3f2e566a-f461-36c5-bd0f-72000b7dbb93 | -12.74724 | -44.52946 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f3c3f8c8-4347-3fb8-b168-44878d08982b | -10.83791 | -49.38561 | 2026-07-03 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e2d1df2-ae2c-33a5-b949-66eeea62134a | -11.34896 | -55.41102 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 497fa56a-8e19-3318-a76f-34c1a6308c05 | -17.31174 | -42.64249 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f9cc302-6b61-3ac3-a178-14a8a7f0578d | -17.31412 | -42.65149 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f77cff69-b2ae-3f00-9bcd-138eafd146c4 | -10.93434 | -43.04505 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a5bab9f-85cf-3f79-928f-36f1c0d2ade7 | -5.79524 | -45.05493 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72425983-a56c-3ddb-b129-c9580aadd098 | -11.85364 | -48.24498 | 2026-07-03 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de9d2990-b130-32ec-8284-23f49cef5319 | -8.70285 | -54.58359 | 2026-07-03 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 626bc80c-e51e-36b2-b1b8-2830dc30b30c | -17.31472 | -42.64727 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2631a16c-2fc5-359d-9358-bd7b4f711918 | -13.98599 | -47.44754 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0f6eaa2-dd36-3664-88ff-8bea77feb048 | -5.79405 | -45.06234 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| edf54429-3f15-36db-9fb2-df1769b480b0 | -15.72772 | -41.35516 | 2026-07-03 04:19:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38fc6bc2-2bfc-3448-b97e-9434e98016b7 | -5.78959 | -45.04637 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4fe0c49-fc9e-3dea-a9b0-6055d6daec69 | -10.94329 | -43.05383 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| da56c377-1baa-3682-a01d-9c9fb93cb5a8 | -10.56343 | -49.13474 | 2026-07-03 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4496c08-f7f3-3e40-bb6b-253056d7a077 | -12.50549 | -48.27507 | 2026-07-03 04:19:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa398af4-f27a-3d60-a795-08dec9901f81 | -5.79122 | -45.05808 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e7789fb-ef77-3fb2-8ff8-c6b68ef9cfd6 | -5.79688 | -45.06662 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac0466f9-39b2-3538-999e-3402a1f301eb | -12.85232 | -44.40236 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cef71074-8bc3-3cd3-bc54-7dc292207507 | -11.34475 | -55.41727 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abce470f-6de4-38e0-aa6d-b5fea67d852e | -11.36077 | -55.41363 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a64ebd-22dd-3a8b-b809-c2520b900980 | -5.79464 | -45.05864 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c82982df-775b-3704-9ef6-2c890b6a89b5 | -4.01376 | -48.06419 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0d3a0b75-c76c-33f1-a289-3bc92846f59d | -5.07556 | -42.51077 | 2026-07-03 04:19:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8157b26a-fc9a-3e7b-9635-81c51198f9ca | -12.74613 | -44.5365 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 872a75d4-8aac-3d62-87d9-2e9b1b0310b5 | -4.00545 | -48.06318 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331dbcca-0a73-373a-923a-74eb27371f73 | -5.8054 | -43.80191 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 351b965f-2fdc-31ad-bce8-243e9555fcb9 | -13.98732 | -47.43962 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81f36429-a76a-32b9-bbe3-2c80b9b94758 | -12.49699 | -43.80804 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7f335d1-1837-344b-89f7-dab9fa925ea2 | -5.79181 | -45.05437 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbdfbf8f-33f7-38cd-a481-fe22d8690c11 | -6.20287 | -42.51428 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81583a62-8d37-3180-a13a-48e3c43ce5d7 | -10.98522 | -43.70465 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a806655-91a1-3f64-a485-c77042c28d55 | -12.7533 | -44.53406 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d19dea0a-4ddf-3853-a938-8559e2aec239 | -5.79763 | -45.04004 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d1db5ee-86e0-354d-9214-6f7b289041b9 | -10.93714 | -43.04917 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05dc9324-b0b2-3670-9588-6cad943debe8 | -12.75385 | -44.53055 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c0a823f5-e0ce-341a-9397-ad62982550e7 | -11.85072 | -48.23978 | 2026-07-03 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 78d0bdb5-3071-344a-8a46-d4f58637e561 | -17.30337 | -42.64989 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d03dc87-e588-3d31-a675-f005ec11e13b | -12.74835 | -44.52243 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 494bbf01-a4b1-3607-8b9c-1da2d5e74ef1 | -11.35661 | -55.41965 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
