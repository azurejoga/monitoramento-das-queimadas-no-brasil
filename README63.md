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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9089940-343b-38f5-8fa0-3ab00a0868ad | -22.22238 | -51.68788 | 2025-10-25 13:01:00 | TERRA_M-T | PRESIDENTE BERNARDES | SÃO PAULO | Brasil | 3541208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| e38c62be-2fe5-352c-bab8-fac1821b7135 | -22.21961 | -51.71975 | 2025-10-25 13:01:00 | TERRA_M-T | PRESIDENTE BERNARDES | SÃO PAULO | Brasil | 3541208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 159.9 |
| b310a82b-60c0-330d-99d3-2bc2d415dcfe | -14.8847 | -52.4592 | 2025-10-25 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 412d431d-573c-33ce-8258-46f5fc408dfb | -13.6488 | -48.1845 | 2025-10-25 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 8a378be0-9247-3928-b3c9-c5a2493c506d | -11.8576 | -49.8709 | 2025-10-25 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0f8ecd69-3110-30f6-b201-dd81f587d92a | -15.1927 | -44.0773 | 2025-10-25 13:10:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 67b54e12-8f08-3560-a3b0-80fb96ad5795 | -10.9953 | -50.3988 | 2025-10-25 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9db440bd-e57c-3de9-8d6e-2506a9ae6516 | -14.3375 | -46.611 | 2025-10-25 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d3fd65fb-d000-3085-be4c-ea0806af407b | -12.2203 | -43.3103 | 2025-10-25 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9702da21-8ef4-32fd-837f-fcef9de059d0 | -11.8579 | -49.8493 | 2025-10-25 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| abad4f9c-9d88-37db-81b3-0cf8229e0091 | -14.3744 | -51.8038 | 2025-10-25 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| aec6cebf-3b29-3ed8-b27e-d6612a3f0625 | -10.9589 | -50.2958 | 2025-10-25 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2615daf2-a46d-3a20-9d5d-31dc617835db | -10.9962 | -50.3345 | 2025-10-25 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6cb49312-20cb-3925-8e86-3c63626cbce1 | -12.466 | -44.5428 | 2025-10-25 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 83d5604b-a184-3ed4-b3ce-faea327a6d8a | -10.9956 | -50.3774 | 2025-10-25 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 82b2ed4f-27c0-3a2a-bc38-d78ee84f7fed | -13.9147 | -48.4112 | 2025-10-25 13:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9627729a-3f36-3ae2-a3fb-f69620d966db | -14.318 | -46.6143 | 2025-10-25 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 764b7f08-17b1-3398-8ab2-393e95fe5faa | -11.5502 | -48.8224 | 2025-10-25 13:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 3922a126-ed41-3af8-8913-fdaea5db6891 | -14.8847 | -52.4592 | 2025-10-25 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4e9c019a-1854-391b-a66f-59fef58f5a2f | -11.8579 | -49.8493 | 2025-10-25 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4219feec-8374-352e-9e8d-55c8ea719ac8 | -11.8576 | -49.8709 | 2025-10-25 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3a1a1347-a8b7-33e8-abd6-48b664493d68 | -10.9956 | -50.3774 | 2025-10-25 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 27df9089-341a-370d-9a64-de53a2432b55 | -10.9953 | -50.3988 | 2025-10-25 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 516858bb-f062-3d6d-81d6-5febcbe734cb | -13.2804 | -47.2784 | 2025-10-25 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7ef29bd2-eb31-34f1-9c1e-8fd1f0ae65c8 | -10.9399 | -50.2979 | 2025-10-25 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a3d6b93e-5b8b-3377-9dfe-6d384be72127 | -12.466 | -44.5428 | 2025-10-25 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c5eacff0-858e-3d80-a9e6-89fe830c335d | -4.8933 | -43.2349 | 2025-10-25 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| df602dc9-2b4a-33e4-8540-f36fa1846293 | -14.9041 | -52.4566 | 2025-10-25 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 01909e02-5edd-3ad2-a2e0-792ef8e906e7 | -10.9589 | -50.2958 | 2025-10-25 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 46c22240-b438-329f-abe4-6a4b3cec50bc | -15.1927 | -44.0773 | 2025-10-25 13:20:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 48d82d24-5b01-3f54-b4e6-4b9f503f6937 | -3.0779 | -44.0248 | 2025-10-25 13:20:00 | GOES-19 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 144a43fe-db04-39ac-8f8b-4e891bf4ae55 | -21.9179 | -46.4947 | 2025-10-25 13:30:00 | GOES-19 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.8 |
| b3071a4f-994a-3487-8e0b-da388d7038a7 | -5.9045 | -41.3072 | 2025-10-25 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| ef23bb72-527a-344d-afcc-76b1c9b8bfa8 | -10.9592 | -50.2744 | 2025-10-25 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c389996e-a15d-35f5-b038-65822b08893f | -5.886 | -41.2847 | 2025-10-25 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 151.5 |
| ed4f6d40-387b-31a0-94a8-e9796e0bff88 | -10.9589 | -50.2958 | 2025-10-25 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9761c046-bca0-37d2-9b22-6929ceb67b0f | -11.5502 | -48.8224 | 2025-10-25 13:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3291b7df-2cfe-37db-8d83-91cd41332dc4 | -11.9453 | -46.8198 | 2025-10-25 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 53ba2251-35e2-37aa-b3b9-0f71509f3451 | -12.2203 | -43.3103 | 2025-10-25 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| cfdfe3d0-452b-3122-a93c-28483ea31f5e | -4.8933 | -43.2349 | 2025-10-25 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 55618a8d-8fbb-3fb3-9593-91997f6568a1 | -12.0545 | -47.1415 | 2025-10-25 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9bb3f3b4-ef4b-3a38-9351-0963d0803d2a | -3.715 | -40.3682 | 2025-10-25 13:30:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 82.6 |
| da11432e-fcb7-310f-826e-76ada5043ad4 | -11.8576 | -49.8709 | 2025-10-25 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4ea3a94f-da2a-33e6-a96d-8c85811033ef | -5.854 | -42.6486 | 2025-10-25 13:30:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 3fe87a6f-b94a-3fb9-878e-c419e7928140 | -14.318 | -46.6143 | 2025-10-25 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 574bd59f-fd39-3f05-9916-9e959b08a89a | -10.9956 | -50.3774 | 2025-10-25 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 31748f9e-9e73-32f6-ad35-2139a0ceed5a | -14.9041 | -52.4566 | 2025-10-25 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f61831f0-5556-3268-80c4-27a062b9131b | -11.8579 | -49.8493 | 2025-10-25 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c104eff9-be1b-3f24-8da6-b8176c83c19f | -14.8847 | -52.4592 | 2025-10-25 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ac034ea7-13b9-3a65-8ae8-e0ac48a2fbbb | -5.9048 | -41.2831 | 2025-10-25 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| ed123535-6b28-3620-84a7-b040e6bda40e | -10.9399 | -50.2979 | 2025-10-25 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a0fc3764-b39c-305b-8217-d9edcad0267a | -10.9962 | -50.3345 | 2025-10-25 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 64ca50e4-3e21-3339-b23c-2b2c693dbf54 | -15.1927 | -44.0773 | 2025-10-25 13:30:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 896a78c0-2ef4-39b3-acbd-51db7a5b08bf | -13.6488 | -48.1845 | 2025-10-25 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 519057b1-205b-31d0-bbbe-002168f48095 | -4.8933 | -43.2349 | 2025-10-25 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 32954e37-b74d-3bae-bf0c-1f95468504d0 | -13.9147 | -48.4112 | 2025-10-25 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bf17f4b8-7558-307c-92e5-54ec4500875c | -12.0545 | -47.1415 | 2025-10-25 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 17bc6c8d-2b04-3bcb-a312-c22486581b40 | -15.1927 | -44.0773 | 2025-10-25 13:40:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 232.4 |
| d97a1056-8e3d-320c-adbb-051266a8a5ce | -11.9453 | -46.8198 | 2025-10-25 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b2268262-f53d-38de-8bd0-b0517082f203 | -12.852 | -48.653 | 2025-10-25 13:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 76f14cd1-836b-3c05-bb52-724e77278ae9 | 1.6386 | -55.7455 | 2025-10-25 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 339b1dab-bf48-39aa-a6ba-5d6680dea6cd | -5.9045 | -41.3072 | 2025-10-25 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| a701f85c-870f-3ee5-991a-bbad13a31379 | -11.0032 | -49.8404 | 2025-10-25 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 52ac7098-84ee-3d88-83e3-485e4cafeefc | -11.8536 | -50.13 | 2025-10-25 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6acd8ad5-76aa-3ed3-89b4-b68f8a94fca6 | -5.9048 | -41.2831 | 2025-10-25 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| aaf445b4-30b5-3fb2-a120-c414af499fa8 | -4.8935 | -43.2115 | 2025-10-25 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 61dab936-0ad5-3cfa-a282-f841b22b79af | -13.6488 | -48.1845 | 2025-10-25 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7a6b22e0-bb8a-3d78-a548-69d3e45f6849 | 1.6386 | -55.7258 | 2025-10-25 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8eb2e273-0bb5-301f-a0d6-19e6a6336bac | -14.8847 | -52.4592 | 2025-10-25 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| bc40c261-bbff-3d5e-95da-0f394d20d011 | -14.9041 | -52.4566 | 2025-10-25 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| d7be52b4-0078-38a6-ae53-c9a7b0774c88 | -12.466 | -44.5428 | 2025-10-25 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8bc61f0b-8069-30e9-aaee-6bafe25f379e | -5.886 | -41.2847 | 2025-10-25 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 16be8e13-84b2-3f0b-9863-9cc5d43b9c0d | -10.9041 | -50.1519 | 2025-10-25 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 35e57dd8-8443-3808-b151-ca90bfcd2ad6 | -13.2804 | -47.2784 | 2025-10-25 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| b3df172a-986d-3051-aaad-fc2045e184ca | -14.9045 | -52.4354 | 2025-10-25 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b96b08d5-a896-35d9-a221-0f16e26fff38 | -12.852 | -48.653 | 2025-10-25 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 653431a2-3096-3291-b5a9-704f8fd9a329 | -12.0032 | -46.7892 | 2025-10-25 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0c000e6a-7229-3712-baa9-e8c4afba06f4 | -6.5289 | -41.0324 | 2025-10-25 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| e0c51977-863b-314c-acd2-3766c55aefa3 | -6.5475 | -41.0549 | 2025-10-25 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| bb0d6a72-b54d-345a-bce8-dc354eeadbea | -14.8847 | -52.4592 | 2025-10-25 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ee81c126-a342-3b15-9e06-947c946bce77 | -12.2475 | -47.0473 | 2025-10-25 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f32a2310-99cb-35af-b390-37710029898a | -3.9928 | -43.7522 | 2025-10-25 13:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1011331b-2026-3d3b-90e2-3480761afff8 | -12.2863 | -47.0194 | 2025-10-25 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| eef6e270-9731-3e96-912d-cb7f75ef53f4 | -14.3792 | -51.5255 | 2025-10-25 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 294bf32a-ddb8-3687-97af-dd2a9dea4991 | -13.9147 | -48.4112 | 2025-10-25 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 703cf4fa-24ea-374c-b9ae-151882aeb7e8 | -6.5478 | -41.0306 | 2025-10-25 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 197.5 |
| 84c2d5b4-4d79-35ca-bfb2-776dcad4eb6f | -11.9453 | -46.8198 | 2025-10-25 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 5a6aaddd-12d4-31af-91d2-e372466ade15 | -6.2854 | -40.885 | 2025-10-25 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 9e3f5481-f4b8-3ff0-8bc7-8d4e9613ecec | -5.886 | -41.2847 | 2025-10-25 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 226.2 |
| 643606f9-384c-3ef1-9910-8f0ab659c004 | -12.0545 | -47.1415 | 2025-10-25 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 1baefaac-cddc-3a35-8ca4-42799ff1161a | -14.9041 | -52.4566 | 2025-10-25 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ceb8ab34-ab62-3a50-a54a-cb5acd17f7b8 | -7.8238 | -40.256 | 2025-10-25 13:50:00 | GOES-19 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 252.7 |
| 1fd79688-a7d7-3a41-bee1-50f8575be22f | -12.0674 | -46.3962 | 2025-10-25 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1ab61da7-c0db-3b52-87e2-3fc3f93c5630 | -12.3427 | -47.0788 | 2025-10-25 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 62e7af42-b17c-364d-9389-b2d2d8c19256 | -6.5286 | -41.0567 | 2025-10-25 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 5dc1ab72-8a96-38a9-8683-fff36879c598 | -11.0155 | -50.311 | 2025-10-25 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a508fc4f-d476-31f7-b549-b0e5a1af2bfb | -15.1927 | -44.0773 | 2025-10-25 13:50:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 343.3 |
| 5ae30b9c-93b7-3a5d-9fa0-cdcb158c272c | -10.9962 | -50.3345 | 2025-10-25 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 25bdc98c-1bd6-3aeb-99a2-29dffe928f73 | -5.6065 | -45.1852 | 2025-10-25 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e6913826-337b-3567-b763-14d20ad88976 | -16.1703 | -45.0881 | 2025-10-25 13:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README64.md)
