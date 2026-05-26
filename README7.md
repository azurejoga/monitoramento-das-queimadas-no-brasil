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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a461ded-72ca-3f50-9e85-ae20576b14e7 | -10.8824 | -51.21792 | 2026-05-26 04:12:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30a974d-9929-3403-8277-58b9b8b43d7a | -9.3643 | -45.46621 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26750274-c779-3f80-93b5-16d13b01c802 | -9.90733 | -44.35209 | 2026-05-26 04:12:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53ed0260-e6e5-3682-999b-c318f849eb0d | -12.67658 | -43.09383 | 2026-05-26 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 468e8b18-654c-397d-89eb-a0e67cc8dfd2 | -9.35867 | -45.47555 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 32c117fe-506e-3b55-b543-c1376d25893d | -14.15133 | -45.35807 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 201a1e77-16ac-30b4-aeb6-a4423e518286 | -9.36346 | -45.47122 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf6e4bf2-5aae-3e9f-84d7-cb08dcdd0b3d | -9.46675 | -46.11483 | 2026-05-26 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2bbec88-8d13-36d9-8d79-62844961cf58 | -12.04416 | -47.3378 | 2026-05-26 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3b6fcfc-a7f0-3b5f-9b37-7cd214787037 | -15.94206 | -41.83384 | 2026-05-26 04:12:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c012c7ae-ebfb-396f-90af-9a9960ff07cb | -11.78801 | -46.47348 | 2026-05-26 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6ee55283-f824-397f-a773-3b96716157c2 | -15.6601 | -43.28702 | 2026-05-26 04:12:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afd0adb5-a7e6-3d03-9456-8f46e7e99c6f | -10.87754 | -51.21294 | 2026-05-26 04:12:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10915130-0f9f-3195-b01c-ee4b03e50f7f | -11.35815 | -52.95571 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 2f87e869-22c5-3f42-a4aa-663ed1253cf2 | -20.28914 | -46.79546 | 2026-05-26 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90b7bbe6-39a7-3fa0-8c3e-bbb830f18d92 | -21.30409 | -48.58799 | 2026-05-26 04:14:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 854563af-e2d5-3ba3-ae1a-5bbea16607a8 | -20.91516 | -46.79004 | 2026-05-26 04:14:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99a8a055-929f-3988-9187-97aff8046594 | -21.32237 | -47.06965 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0f8eae81-61f5-341d-a40a-6062ce58b793 | -17.24306 | -48.29793 | 2026-05-26 04:14:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 399337de-0f8f-3602-87ff-575acef5f1f8 | -18.77238 | -48.04115 | 2026-05-26 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b779e570-9f7b-392f-b082-9f6c66320891 | -21.32158 | -47.07413 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a3d964b-e66a-3321-8496-927a7795779d | -17.24233 | -48.3018 | 2026-05-26 04:14:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 314ace18-2c47-3135-9d97-8337f3b55386 | -18.77051 | -48.03788 | 2026-05-26 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b1201cb4-d34f-37ee-aa06-05509c637b75 | -21.55328 | -47.05605 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19663433-e56c-390c-b2ff-008aef2ad05c | -20.91875 | -46.79083 | 2026-05-26 04:14:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30d069c5-7479-3633-b242-34b8d382756e | -17.24718 | -48.29881 | 2026-05-26 04:14:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5befa578-509e-3fae-b8b4-7b79293dc500 | -21.32599 | -47.0704 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 899838c4-4e34-3c8d-aa2a-db6857461da6 | -21.26752 | -49.47611 | 2026-05-26 04:14:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b5b3b16b-befa-39ac-acd8-d16f3ca14fb7 | -21.55722 | -47.05433 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1735c29e-ca7e-3b24-83c4-fd685cd9139e | -18.77447 | -48.03867 | 2026-05-26 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17cf4995-303b-3110-8f5d-1d67d4853f1e | -20.19425 | -49.5658 | 2026-05-26 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ca8d3632-d3c9-3e02-8099-9b37ff727185 | -17.59098 | -46.5657 | 2026-05-26 04:14:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad5b7f01-6220-37ea-8b2a-858524be3d82 | -21.55689 | -47.05681 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1beadd9e-0033-3c5d-a4a5-175ab0eda866 | -18.08193 | -46.87591 | 2026-05-26 04:14:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab8388a2-0a5c-386d-8500-1cc3ba0bf7cb | -16.23826 | -43.49468 | 2026-05-26 04:14:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3211757-b646-3829-b835-31dab4d284fe | -21.26339 | -49.47514 | 2026-05-26 04:14:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7bcf8153-5195-3f47-a14c-38faf133e71d | -21.55047 | -47.05087 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aed4b9df-7e94-304a-a493-dea6f1d70f5a | -21.30016 | -48.5872 | 2026-05-26 04:14:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4060807e-c1f2-3a9c-af7c-00368e0dd129 | -18.29219 | -40.14339 | 2026-05-26 04:14:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9e2d9f0-2d3a-35d0-a28b-915e95af7fe4 | -21.55408 | -47.05162 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8158885-2d9e-3df7-8d95-c3cb6e3842a8 | -19.60149 | -43.87175 | 2026-05-26 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17cf750-7af5-3dc8-8a90-04a8a874d12e | -20.19506 | -49.56161 | 2026-05-26 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f8386e5-b0f4-3264-905a-a57f0145c372 | -18.08568 | -46.87666 | 2026-05-26 04:14:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc3a903-c0d4-3d13-a2d8-8e9b90eabe12 | -21.54999 | -47.05282 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57277eb3-9ccd-3151-b29c-4907935e661b | -21.5536 | -47.05357 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 859488fc-70f1-3803-a31a-5ee376337994 | -21.55644 | -47.05876 | 2026-05-26 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a99ae15-cba1-3a7b-b815-677bb41e822b | -20.27935 | -50.72509 | 2026-05-26 04:14:00 | NPP-375D | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ff440bf8-2a04-3817-9831-e36090488b58 | -21.28593 | -56.10706 | 2026-05-26 04:17:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e823695d-40df-3aa3-8f8d-51c5685d2977 | -23.3371 | -52.30116 | 2026-05-26 04:17:00 | NPP-375D | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 446da975-9cad-3e78-b450-537daeb17c0e | -23.1525 | -51.64112 | 2026-05-26 04:17:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1bf692e7-a589-3cf5-b520-f7a78c1e2fc1 | -11.3584 | -52.9514 | 2026-05-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| f4ae7375-612a-3c30-9878-fcae0f59b7b5 | -5.35002 | -45.18689 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb9cc48-99f6-32bd-94c7-b9b5d512c0d5 | -3.95734 | -43.12565 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1500f81f-7a7d-34e3-81f9-23f23f5e575f | -6.08153 | -44.0044 | 2026-05-26 04:27:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bb03d45-69c8-3c68-9929-1d9780964145 | -2.96127 | -39.92199 | 2026-05-26 04:27:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 299c29aa-d461-3b2c-beb5-9d06b2f329b3 | -6.07748 | -44.00772 | 2026-05-26 04:27:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 118eec34-25c8-307c-b9de-b2126105d304 | -4.43067 | -47.73131 | 2026-05-26 04:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9ac746e-552c-3cff-ac41-2d5fb52d5816 | -5.81475 | -43.20259 | 2026-05-26 04:27:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6a93d3e-a941-3248-ab53-d49d6632f640 | -6.7288 | -44.36953 | 2026-05-26 04:27:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf10229e-9ef2-3876-a7de-2a0f56e7ccbc | -4.42784 | -47.72709 | 2026-05-26 04:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a32f868-f91a-35d3-93a7-f1668221c18e | -5.81413 | -43.20665 | 2026-05-26 04:27:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01bfec60-9de5-31be-a81f-baaf23d91fda | -5.78968 | -45.13332 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d86f3bd-3162-37fd-90fe-8a5347fffd92 | -6.10206 | -44.73414 | 2026-05-26 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e65f356f-f01a-3e24-b167-2f11aeec8c8c | -5.30866 | -43.06072 | 2026-05-26 04:27:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78175247-b1fa-3ffd-a85b-505164644f88 | -5.30029 | -43.0677 | 2026-05-26 04:27:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e6be214-94c4-3ffe-8cb4-d62ece2898d4 | -5.79133 | -45.1228 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c148b629-219e-3fa7-92d5-7ff7ef102e2b | -4.42793 | -47.72722 | 2026-05-26 04:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cf9eae2-c428-3029-b550-08a3e0ab4d7c | -5.9553 | -43.48883 | 2026-05-26 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb4c5719-81aa-387e-9876-43b041bf291b | -5.78745 | -45.12579 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3be05e92-aec5-3def-85df-caa596840873 | -3.95531 | -43.13415 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d21dc9-eda0-3f27-b274-02d9e6bd173e | -4.6565 | -42.43421 | 2026-05-26 04:27:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c69d9e48-7109-3890-9023-c5ab0566349b | -5.30091 | -43.06364 | 2026-05-26 04:27:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7d62ea0b-edee-36ac-acf7-74ac526612e1 | -3.95592 | -43.13028 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6dfba44-f2df-3fbd-9e58-9991de64deca | -6.10543 | -44.73467 | 2026-05-26 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d33c378-840b-3f2a-bf03-6bed27611d31 | -5.30509 | -43.06017 | 2026-05-26 04:27:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a8085a3-8928-3f47-9ff4-95736c6950f8 | -5.79357 | -45.13033 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 683105bd-25a6-3e55-8130-17088498767a | -5.788 | -45.12228 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9082e522-e5cb-34c7-b16b-f5d0f3e5769c | -4.42734 | -47.73092 | 2026-05-26 04:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 868cf0be-716c-3954-882f-34f6bc8d3ed3 | -5.79412 | -45.12682 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03f8c5af-6efa-32a8-add1-daddd9a4eead | -5.81057 | -43.20611 | 2026-05-26 04:27:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0cc3949-05da-3132-a936-4b80019211c5 | -5.68071 | -50.10328 | 2026-05-26 04:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14bda250-32ca-3c17-b534-44e87cead070 | -2.96544 | -39.92262 | 2026-05-26 04:27:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57b69da5-d913-32fd-9fdd-474433870db2 | -5.81166 | -43.22298 | 2026-05-26 04:27:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2753925f-aaf6-3f7c-9241-ef2b1fb706d7 | -3.95675 | -43.12954 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20560480-ac5a-3630-b95c-a62c7e30d64d | -5.79188 | -45.11929 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a1405ea-9a71-3979-b703-8d44d5d90402 | -5.79244 | -45.11578 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9696454-8847-3e4f-ab62-70409cd43b4d | -5.79522 | -45.1198 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ce0e112-91c0-30e3-bcdc-3a2faeb06f9e | -3.35684 | -43.16845 | 2026-05-26 04:27:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97c81ec9-e36a-3e31-b9f8-7bca3859e391 | -4.43127 | -47.72763 | 2026-05-26 04:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62dc5fe6-b323-3b51-8ffb-eee8fe319f68 | -5.79467 | -45.12331 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01f16dd8-20b1-3887-8b9b-a36d41a947e8 | -5.95178 | -43.48829 | 2026-05-26 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75cc8049-52a4-3af5-b8b7-7b3cc8a7b798 | -6.32924 | -44.52849 | 2026-05-26 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 460ebcea-9e59-3eca-85cc-8e8d8375d9ed | -5.79078 | -45.1263 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f3ebe4b-c6c2-35cd-bfa8-341a0864f78a | -3.95615 | -43.13342 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bac7c423-f310-31db-b9f1-b37c4a9e5215 | -5.64903 | -48.61267 | 2026-05-26 04:27:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4e8b36a-8a47-3e00-8c51-eb7a6da01859 | -5.78855 | -45.11877 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 61229252-f2f2-3c68-a199-b1a0335a58ec | -5.35057 | -45.1834 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faefab71-aa17-389c-823e-0d72575f7d8f | -5.81584 | -43.21944 | 2026-05-26 04:27:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a44a636e-9b2f-3408-9646-a2eeaf0026e6 | -3.95653 | -43.12639 | 2026-05-26 04:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c67894d2-4367-3eb0-8d29-58e009591261 | -4.63054 | -43.04966 | 2026-05-26 04:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
