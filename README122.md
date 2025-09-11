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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9fd8466-b93e-3cb3-9bbf-61342ba45a0f | -22.87564 | -48.53289 | 2025-09-11 04:49:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21955cb4-9d48-39ea-aba4-755464318fca | -20.40082 | -46.27881 | 2025-09-11 04:49:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac57ce1f-b5c2-3f48-b760-5373cffda565 | -20.24674 | -43.58063 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a64df4e7-138f-388e-a955-5523cf12879d | -16.5105 | -55.1449 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2515ec85-d98c-3c6c-b07a-fe360f9115ff | -22.56505 | -46.04656 | 2025-09-11 04:49:00 | NOAA-20 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b93eb1fe-1933-385c-85d7-3df60c3f660a | -18.50322 | -47.42105 | 2025-09-11 04:49:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e77371e-47ed-34d9-a918-43a00ce4b4b2 | -19.98843 | -47.62554 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f0245f0-1e73-328f-9e4f-01bcd7be5b98 | -16.54047 | -55.17632 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d4fae127-ea9e-37d0-ada3-0697902da7b0 | -19.72514 | -43.91447 | 2025-09-11 04:49:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e7a70ce-878d-316d-9c3e-c705b37ba8eb | -16.34377 | -52.94437 | 2025-09-11 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5be7145-659f-3bf3-ab0b-7c97a34b8015 | -20.24091 | -43.58107 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 011dde6b-dde8-332f-9da4-2d43540a4688 | -16.54829 | -55.1505 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 828633eb-5465-3751-85dd-191665560928 | -18.55653 | -46.57161 | 2025-09-11 04:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3407c080-a2b9-3ff9-b296-5373cb071743 | -19.10753 | -43.21892 | 2025-09-11 04:49:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 369a50f3-94aa-3efa-9433-919196b00148 | -19.90959 | -44.23912 | 2025-09-11 04:49:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13aadd2a-c761-3910-9f23-52ac7ce4b05d | -17.56459 | -44.55383 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e193bb5-39f7-3afe-9ba7-247bd2e76c16 | -17.5501 | -44.54194 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed84e097-e156-3de5-ac35-0e7cd87cd19f | -19.97941 | -47.62655 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e3b66f05-98c5-399c-a791-35a3ebba25d3 | -16.53707 | -55.17567 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a8cf12e5-fdf0-3b64-a6b8-9569a33387d8 | -20.06133 | -47.5383 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3ef8c51-c9fa-34d8-af00-53ef6506d968 | -19.99225 | -47.63108 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc52bd4e-0ea4-3b0e-bd1c-11e81a97f940 | -18.93756 | -48.70807 | 2025-09-11 04:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d2c25ac-4d51-396c-b8b7-891f441e6ff6 | -16.52098 | -55.16631 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1b122331-15fb-386a-8d51-cbf2a4f72a4c | -17.82324 | -46.74386 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82260e68-1334-3950-9317-0aba9aa8cad8 | -16.60825 | -49.77827 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a38215b5-711d-3dbf-b3a1-e49efc0d7351 | -19.66459 | -45.85008 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c2659e62-7eb8-3e8a-808c-c4cfcc5ebbb9 | -19.25297 | -48.01218 | 2025-09-11 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc2f2fd7-8492-3a08-bbd0-47674b5e7f97 | -17.78568 | -51.73356 | 2025-09-11 04:49:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa8ce994-f651-3f01-9f7d-e635b3463113 | -17.56521 | -44.55418 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca2eea46-4624-35bb-a5dc-98009c551642 | -17.56495 | -44.55075 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 751b96ee-91d2-348c-be1a-e0a3ba50387d | -19.37222 | -43.27161 | 2025-09-11 04:49:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 09db1752-54f2-31f9-a5c5-8903b1213eb9 | -20.53794 | -47.61979 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0090b879-0174-3725-8deb-95a059e979a7 | -18.07584 | -51.03147 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4cc1967-8c9d-3d8f-aa48-767576f2e0a4 | -18.00678 | -44.4502 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc19eb89-1cb8-3c33-9ed4-6f28934bbf6c | -18.34572 | -44.36079 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98e1ff25-06de-3dd1-aeb9-bb3ddeec8bd9 | -20.00102 | -47.63234 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdf4b5b6-2f79-3f9c-b8f1-df608b4ebfaa | -16.3482 | -52.93773 | 2025-09-11 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18edee78-3a65-3118-8f91-f685ff8c794b | -17.37645 | -52.93722 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 38175de6-23fa-33c6-9b16-57d545b1f947 | -17.93962 | -50.54327 | 2025-09-11 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f8c0222-91f7-3d18-a651-6ee23df0eacd | -16.18822 | -53.86556 | 2025-09-11 04:49:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b17d081d-f630-3ff6-aa1e-2b29275c6126 | -18.00465 | -47.99274 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9c90532-842b-310d-9ed5-4c1f942b495f | -18.55712 | -46.56662 | 2025-09-11 04:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97defb4e-762b-302c-aa3d-d5e4eb9e68ea | -17.20057 | -50.15489 | 2025-09-11 04:49:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e680796e-cbdb-360b-ab13-b0b0800baff5 | -19.95741 | -44.15238 | 2025-09-11 04:49:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 11fd9e7c-940c-3ed6-95b4-8b4ae3a78173 | -20.2471 | -43.57682 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7a78d249-3f6d-306d-b53c-a1b6a7ec03a9 | -20.23541 | -43.57801 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be3b84c2-81e9-3a1f-a436-7ff48320a3b5 | -20.24126 | -43.57731 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c5df5ac3-b253-373b-bbd7-8a998944d1f0 | -17.26191 | -46.08137 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b781bcc-e587-3207-befc-a86cd42be89b | -19.98761 | -47.63234 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d818dc45-a17c-3ad9-8cd1-7238e5692457 | -15.87168 | -54.93317 | 2025-09-11 04:49:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae7fcfd8-c1f6-326c-837d-5c9aa722412b | -20.69834 | -46.07328 | 2025-09-11 04:49:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 89e2c681-8d61-34ac-a570-320420cdbbec | -18.60298 | -43.97051 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3e1444-4252-3755-a4e1-6f60a778c0b7 | -22.56538 | -46.04332 | 2025-09-11 04:49:00 | NOAA-20 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b7aacc88-a75a-33cf-8a3d-b101d4e76d39 | -20.12899 | -47.68348 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84effe96-302e-3689-9dd6-5c907fba2f6c | -19.99615 | -47.63583 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b10646cb-9b5c-378d-820d-23eee85aa6f2 | -20.16668 | -44.61983 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a7fc90c-e9cc-3b7f-addc-cd1427a08478 | -20.44259 | -50.00198 | 2025-09-11 04:49:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31b9e020-799e-3dd2-bab4-c03ee5ad59b0 | -18.55771 | -46.56157 | 2025-09-11 04:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39e4d89a-7e84-36fd-95aa-909bb77c0b97 | -19.98323 | -47.63176 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b17d016c-000b-35d4-956e-a1f9a13552d5 | -16.51758 | -55.16567 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7f0be66b-d056-355f-b502-6434c0d8689f | -17.33124 | -46.68616 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 815b824d-e8b0-3587-9132-e20a4f570782 | -18.35395 | -49.32494 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 086292d4-a6c9-3213-bfb8-ee8f44677b4c | -17.90147 | -44.59166 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 737e7924-3fd3-3f48-988a-9fd8751dcd31 | -20.91693 | -49.46408 | 2025-09-11 04:49:00 | NOAA-20 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cb2890ad-e60e-3f16-a22d-c328b48803b8 | -20.91064 | -45.28965 | 2025-09-11 04:49:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 49d3eed9-f46e-3eff-8d7e-7c3562cd9357 | -17.33327 | -46.68387 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d62c493b-0d6a-3311-acf8-a114166464e8 | -21.12305 | -47.7305 | 2025-09-11 04:49:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29471ecd-3c17-3c7b-b0c1-f4d0c7dcfe70 | -19.99866 | -47.61515 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2bb6c86-b958-37f9-8bec-d561a16b3d08 | -23.02979 | -50.11111 | 2025-09-11 04:51:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f0135b7-23f8-397e-ae73-cd6c572e3db4 | -22.9301 | -48.38062 | 2025-09-11 04:51:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 58513c9d-e535-3f20-bcd9-bc20df0cbb1d | -22.92956 | -48.38535 | 2025-09-11 04:51:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c5fd546c-2f4b-354a-9f88-2ec192120085 | -23.33578 | -47.32314 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 37108c91-9dba-3bc2-ae04-b354063c5ccb | -23.34334 | -47.21135 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| afeb8fd0-6fdd-3709-8442-42fb8a97fa6f | -23.33381 | -47.31973 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3eea6fa1-e367-31a8-9a79-3cfd50f42086 | -22.59777 | -51.88232 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d1e67789-55e4-3f01-8e83-93e38d295350 | -22.67287 | -53.12451 | 2025-09-11 04:51:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4950814-21ae-398a-bcc6-8725565f8ebf | -23.34105 | -47.31845 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| acba645e-d3bc-3fc1-8088-fb1d8b3b7c39 | -23.34529 | -47.20822 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0406f7f7-3d7e-32c5-890f-84a2e3939914 | -23.68544 | -52.27472 | 2025-09-11 04:51:00 | NOAA-20 | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b174088b-d9af-3d90-ab80-c5e22ea24015 | -22.58829 | -51.8984 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3b782e89-3ea9-35f3-89b2-cb3064856ebb | -23.25109 | -45.97584 | 2025-09-11 04:51:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 203a5a35-d7e2-3b7e-a1ee-355fdd8e3740 | -24.19605 | -51.76047 | 2025-09-11 04:51:00 | NOAA-20 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6cab0cf0-0bb2-3ca5-804d-2c48be7e0002 | -22.97118 | -49.74524 | 2025-09-11 04:51:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 42b02043-67c1-33ff-8389-5134c57f05b9 | -22.59421 | -51.88179 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2bc68836-28d2-3364-bf7d-bdbf0d8e5ae0 | -22.58532 | -51.89359 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6237e50b-c722-3195-8382-57e478a48ccf | -23.33109 | -47.32267 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b3be766-d553-3db5-a780-0b2aaad3bbed | -23.76968 | -49.052 | 2025-09-11 04:51:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dee5400-8abd-36ca-b2ff-01296b5d50f2 | -23.33327 | -47.32494 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cc0bc157-1bbe-3f42-8eac-2d637d104327 | -23.34841 | -47.31618 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 907afac9-9456-321c-b6c8-9c52d88a5efa | -23.33637 | -47.31783 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 94583a53-834f-3814-a205-cf62c59bf94b | -23.09534 | -52.47153 | 2025-09-11 04:51:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7e7b3412-c9e5-3a83-af69-65dceb70a0ce | -23.22807 | -49.42928 | 2025-09-11 04:51:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe2c71cc-41ce-3e28-9d7c-20a5fdb240e1 | -23.35218 | -47.21786 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ce6b5327-7ec2-3681-9548-8749b51ef151 | -24.20007 | -51.7588 | 2025-09-11 04:51:00 | NOAA-20 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62699821-9dce-3bca-b17c-a5d4c491668e | -22.66946 | -53.12393 | 2025-09-11 04:51:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7be9ee6b-8a6d-34fa-be1f-da17455321ab | -23.0674 | -54.20058 | 2025-09-11 04:51:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 0fb521d3-75fc-351a-823b-8c0bc374789c | -22.59006 | -51.88555 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a7b92601-44f1-3424-8458-8983a17febdb | -23.34276 | -47.21664 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1fa21877-1aa7-386c-80db-fa81aececd93 | -22.59303 | -51.89036 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 20da3046-36ee-38dc-bddf-31ca9c557485 | -23.33493 | -47.30887 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README123.md)
