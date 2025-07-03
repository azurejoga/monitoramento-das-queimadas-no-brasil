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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c680c0-afe9-3227-b52e-db6772cbc8f4 | -10.6639 | -49.4544 | 2025-07-03 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c32823-9f20-3bb4-b4a4-1d005be9d15c | -13.39693 | -47.85052 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0de5d6c-68b1-379f-94bd-48bcc10cd11f | -16.29925 | -49.95279 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 314eb995-2ad6-368e-9c8f-b46d5be26038 | -12.43165 | -50.02906 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36de931d-864c-39c3-ae3c-db710e83def0 | -12.63041 | -54.21545 | 2025-07-03 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14f13680-47c7-3264-91fa-73c6878da5f1 | -11.50465 | -48.95626 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdac30f5-20cf-3366-b27b-ed45e98c23c8 | -16.29653 | -49.94388 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b9e6805f-55ff-350f-b590-6602d7a0b8b0 | -17.09598 | -43.80344 | 2025-07-03 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3698c92-ff60-3149-8155-005b5ae0363b | -17.75738 | -39.66068 | 2025-07-03 04:10:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8c3242fc-d4b3-33d4-82af-26782f895ce1 | -11.50393 | -48.96045 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0572d80a-b944-35e6-8b8f-b017e783032d | -17.75672 | -39.65919 | 2025-07-03 04:10:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| cc1f6e5f-927c-3846-a969-3c16d058cd26 | -11.54157 | -47.30744 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f65733a-eb69-3d11-92cf-45e3a3c6e689 | -14.63495 | -53.88805 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dec66b3-2ff5-3fb1-9e33-22590ce92297 | -11.65024 | -44.58044 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e054cd41-905e-3b53-8242-ed1283b8804c | -14.62855 | -53.89084 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d11874ea-2c01-34a5-8c5a-503d3df2094f | -11.65801 | -44.59696 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 639924cb-0425-330a-b338-72a5f175c139 | -11.65981 | -44.58583 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39c0a5d3-b87e-37b1-a534-0c5ca5194078 | -15.61946 | -46.45737 | 2025-07-03 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0947d29-3803-33a6-9b9b-15e69adb19bc | -11.83755 | -47.55719 | 2025-07-03 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3da137f9-494c-3b8f-92f5-86a841978799 | -12.42625 | -50.0329 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 232b8580-971f-37e2-b847-0b17228de08a | -15.56862 | -47.85494 | 2025-07-03 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fff7d19-ac11-349f-96aa-b69cf5b4ed1b | -10.88981 | -56.45339 | 2025-07-03 04:10:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d513f3c2-0596-39a5-9bbf-eae94ac10648 | -12.44338 | -43.56165 | 2025-07-03 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ef2d03c-1153-344d-8e02-d4274c4baba8 | -16.2958 | -49.94788 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c8bf0438-c930-314a-8829-7ef2ec59820f | -13.56768 | -40.90586 | 2025-07-03 04:10:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1cb461e-3773-3386-b3ec-d08dedf84302 | -14.88113 | -48.36451 | 2025-07-03 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f23b9207-222d-3616-a344-d39c9db4c91f | -13.39853 | -47.81838 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f97e7d85-1288-33ca-9aa2-ef985ab1f392 | -10.70865 | -49.67464 | 2025-07-03 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aaec8800-8475-3b70-b190-ac14b65fb4ce | -14.8573 | -48.33936 | 2025-07-03 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888eb1af-2064-31ea-8c99-b717e74124fe | -14.62776 | -53.89473 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d46ec5f7-b64c-3e55-abc1-dd318eeff670 | -10.96142 | -48.22464 | 2025-07-03 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33eb81be-4f11-3ee6-86c2-c111acd15343 | -14.2402 | -43.66589 | 2025-07-03 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15654b64-beed-302f-9bfc-fa5b667fa0e0 | -13.408 | -47.80983 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5189c3a-f664-3e32-ad02-77719a94a146 | -14.62935 | -53.88694 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59ea8149-04c6-3368-be7a-33e66184928a | -18.04044 | -39.92701 | 2025-07-03 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61d100f7-f11a-33fe-8822-e4a558e5b477 | -11.63948 | -48.07784 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f47696b7-76b1-326a-a8a9-951f12bcc93c | -14.85637 | -48.34465 | 2025-07-03 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7968411d-8e4d-34d4-bb9a-211c09048db3 | -10.7091 | -49.67354 | 2025-07-03 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f998b7f1-5fb5-3ab9-996c-011907ae2462 | -12.42712 | -50.02818 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f5f7fd7-93f4-3074-a314-0fa408053570 | -18.29166 | -44.6824 | 2025-07-03 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0c3aa25-480d-3c58-bc7d-a318df9a455e | -12.56984 | -48.88618 | 2025-07-03 04:10:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a3d3af5-69be-32d0-a7d5-2a5b86b494a0 | -10.68058 | -49.49073 | 2025-07-03 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e18e1f4-d034-387c-bdfb-c9ef2014c7a9 | -14.90002 | -41.98039 | 2025-07-03 04:10:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a47ba14-5841-35c3-ad93-46b222d0ba8d | -17.59616 | -43.19693 | 2025-07-03 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54906881-bca0-31cc-8d3b-4da33a769c0e | -12.42798 | -50.02351 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26d90fa3-9510-3edd-8fa3-fb5aa5b01363 | -11.84231 | -47.55285 | 2025-07-03 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf7ae28-9b69-30c5-93e5-b8ea373227d2 | -11.54459 | -47.31305 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af0d7d1d-18b6-3625-9139-84cbfa556a52 | -11.64011 | -48.0742 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0e227607-c5e5-3489-a5f3-4a39dc095f5a | -11.66321 | -44.5864 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbdcdabb-9041-383e-8126-272d6b4ab242 | -13.44547 | -47.83062 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b37903a4-c10c-3ae8-9008-ce83084cf195 | -11.64073 | -48.07056 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ae473be3-02c5-3467-8ce1-4f75b91c8d85 | -16.58006 | -43.64401 | 2025-07-03 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0652ee17-0736-3d95-80da-09e016bde04f | -11.55231 | -47.31447 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3635842f-8c36-307a-9b72-e6df20fa9ae5 | -15.4097 | -41.90118 | 2025-07-03 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f9a846c-0827-3fe0-af49-391a7fc6a6b0 | -17.66639 | -42.26881 | 2025-07-03 04:10:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5946a70-1592-3bc7-be3c-b05661d5e2ac | -18.61539 | -44.26552 | 2025-07-03 04:10:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 188bbd97-9897-3fb4-9ddb-1cbba5776dfc | -20.72478 | -56.65188 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73504c3a-1651-3bfd-b741-06e37216cde4 | -18.21803 | -51.35013 | 2025-07-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 98f653d8-ce9f-3eba-b11e-c6317fbf6e75 | -19.43654 | -44.34104 | 2025-07-03 04:12:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc915975-7c25-3abc-9090-a26301b2d633 | -20.72198 | -56.65363 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ad6115a-28e4-32cf-8fb9-8d05c985d44a | -18.66219 | -55.74421 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b222a368-e8dc-3ed3-86c3-5d7ef918757c | -20.58008 | -44.57347 | 2025-07-03 04:12:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f18906b-a7cb-3781-a32b-1f7a507b158a | -18.6564 | -55.74282 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 08ea4774-a88b-3192-a84c-d5e66890da27 | -20.54018 | -48.74942 | 2025-07-03 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c61fb42a-b3d4-387b-a2b3-8fcd94402c6a | -21.68829 | -49.50193 | 2025-07-03 04:12:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d0fbc2bf-51ad-37a5-8991-4d8a31c39fca | -21.61347 | -57.56031 | 2025-07-03 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e366f9-2369-30f5-9df5-132db4a99c0c | -20.72795 | -56.65465 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3941549e-d88c-3994-86dd-5814e81ef42e | -22.53093 | -47.38371 | 2025-07-03 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6545def9-2f94-364b-a660-6688383fa4b6 | -20.05426 | -44.28003 | 2025-07-03 04:12:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| efc6c6c4-cefc-3fa2-ad39-0f188c4b0284 | -20.76564 | -46.76965 | 2025-07-03 04:12:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5e9b699-e612-378a-ab66-2232b3ee361a | -20.07455 | -45.81494 | 2025-07-03 04:12:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a7c6d8-39f3-332f-9395-4f0717108b22 | -19.45485 | -45.30687 | 2025-07-03 04:12:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0a588f-b42c-34c5-b5c0-9437585e1ea5 | -20.72983 | -56.65697 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6461b1a-0a90-3b3f-b7ee-c21ac0bd4f9c | -21.8901 | -56.11338 | 2025-07-03 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 479b775b-e135-3ddf-8cf9-316bd64f1ad7 | -21.61884 | -57.56596 | 2025-07-03 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1108f5ca-d615-3047-a41a-0d62183a38e8 | -20.25844 | -44.49974 | 2025-07-03 04:12:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1dea71b2-24dc-3182-b272-bdf2dbd289b1 | -20.73071 | -56.65306 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29bda5c6-ca54-3586-b6ff-c5efb1c916b8 | -19.74658 | -42.00365 | 2025-07-03 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a31d0a91-8ad5-3dc5-beae-9318416e6f6a | -18.65737 | -55.73847 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f799fe41-e452-3062-814f-251e64b01478 | -21.61819 | -57.5675 | 2025-07-03 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b757ced8-8572-372c-b8ac-0c5d3a717d5d | -20.72704 | -56.6586 | 2025-07-03 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 03edefbb-5ae7-3ca1-b4ae-d251086ea19f | -18.65796 | -55.74009 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 9a36073e-b43a-3a18-a806-23f8f7352b2d | -18.2136 | -51.34912 | 2025-07-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| df28a139-6e94-3af6-ad69-d019219a73b9 | -19.36086 | -44.30237 | 2025-07-03 04:12:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c02a50b7-7ec0-3b7c-ae2b-a770f5847804 | -20.37749 | -45.60205 | 2025-07-03 04:12:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3138b1a-b3e1-3dc8-8baa-3683737db92d | -19.36029 | -44.30601 | 2025-07-03 04:12:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19723de5-2145-34a7-a7ad-438c6b5e0f2f | -19.43739 | -48.55269 | 2025-07-03 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1399a1c-f88c-32fb-a649-6f8d7d0f3cdd | -20.45989 | -45.55604 | 2025-07-03 04:12:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e972feb2-86ec-328c-9e01-bb374b73836e | -19.37605 | -47.68898 | 2025-07-03 04:12:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96e4f9ba-a46a-3f43-9316-1271bef52c73 | -19.96871 | -44.21689 | 2025-07-03 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 423dca72-6d0d-3609-b2e2-17639150f982 | -18.65543 | -55.74719 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 819ea6dd-1fb5-3884-80b1-ae73efbd5b37 | -19.53771 | -44.07996 | 2025-07-03 04:12:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cfb93a8-699e-3986-8f7b-c59d3d9bf0a5 | -20.54385 | -48.75016 | 2025-07-03 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 72610320-a827-3038-aa8d-a039e160a60d | -19.3725 | -47.68833 | 2025-07-03 04:12:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eec398e8-3d39-3a71-96ef-322dbafc25f2 | -21.95434 | -57.58565 | 2025-07-03 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc7f0a0-f1b7-3217-b4f6-a414597342dd | -18.65702 | -55.74445 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 4c44dba3-7e76-3818-a688-2cd764c64e45 | -21.61294 | -57.56366 | 2025-07-03 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bae0784-0f87-3cbe-a524-21ea1cdcb548 | -18.66605 | -55.75433 | 2025-07-03 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 35092b02-0514-345a-be02-974da06d7033 | -19.43822 | -48.54808 | 2025-07-03 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fcaad8b-caad-3310-a268-82696733fe88 | -21.88918 | -56.11747 | 2025-07-03 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
