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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d68358-6325-3428-aaf9-d615e7bc9cca | -20.06538 | -45.29191 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e28d4483-821d-333a-ab06-a1efb6f99662 | -19.98788 | -47.63029 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f44ac84c-beee-3fc0-b844-b1dad67f934c | -17.78625 | -51.72971 | 2025-09-11 04:49:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5e71ae9-e02f-317c-beb5-603a69cb47e5 | -17.4651 | -45.10374 | 2025-09-11 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cee129f7-3ce4-35b2-b71e-fa6d8660f7ac | -16.5128 | -55.0675 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4e299c3b-517d-3324-8e92-e9080564a5ed | -17.32876 | -46.6833 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a73dbd1d-3291-3751-8e7d-f12bfda9adeb | -20.00595 | -47.62825 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9f8341d-f061-38a8-a116-2deeac81d089 | -20.90544 | -45.28918 | 2025-09-11 04:49:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7f126b8e-e87d-38f2-82aa-58634f96d6de | -17.82951 | -46.73031 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 803c83f2-35e9-3b6d-8ae1-572e1a9df876 | -15.60731 | -58.30618 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64a08132-3b4b-35b6-8fe5-081a32d99826 | -20.07623 | -47.52648 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c79166db-5723-3660-b42d-9729a265f56b | -19.35129 | -56.70266 | 2025-09-11 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ce308c6-df89-3396-b103-a75ad41bc64b | -18.05489 | -50.72603 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e3aa263-b238-338f-a1f5-4a442d0a3a07 | -20.0398 | -42.73025 | 2025-09-11 04:49:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| d63e4176-be1e-3526-a818-6bec2e6e69ce | -22.84085 | -47.46874 | 2025-09-11 04:49:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 05546b7e-bc9d-397a-a572-03f8af79f208 | -18.07936 | -51.03204 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90c36fd9-6855-39b5-a8d0-b85dfc76d5f9 | -17.55047 | -44.53863 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48836f3d-df7b-3306-91e4-e64bb1c890f2 | -19.20476 | -47.9864 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63757398-e99c-32de-8592-3fe0a675197e | -22.52201 | -49.08796 | 2025-09-11 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ce1fa9d9-af3b-3724-8460-d35d70cfaa99 | -19.46223 | -40.88491 | 2025-09-11 04:49:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5e36b849-0173-307f-b3b9-e55b11c9d84e | -18.60427 | -43.96569 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd8f9e01-07fa-33e1-95bb-982c3be98433 | -20.38552 | -46.63208 | 2025-09-11 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf57696-7592-3c72-a060-df2039753589 | -19.00661 | -46.25341 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab827f19-4eec-39f3-b99a-737a9ffa645d | -18.06139 | -50.73156 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4bfb1b33-5864-34b8-9ed6-075515b1e5a5 | -18.57116 | -47.41544 | 2025-09-11 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c3b31d6-2d05-3d51-9813-5239e9746f76 | -17.26609 | -46.08611 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f0d3f773-10cb-321c-ae97-372529642b55 | -18.83692 | -50.11182 | 2025-09-11 04:49:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fb521fb-292a-3e2a-8822-40952394a53f | -21.43743 | -48.91757 | 2025-09-11 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9806952a-2360-3cd4-8a78-ead0e367f7e5 | -19.99198 | -47.63307 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d269079e-ad81-38cc-b1ae-852954c9ec07 | -19.10711 | -43.22323 | 2025-09-11 04:49:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c9c1f31-777d-3ff4-a005-ca4cd0a007a2 | -18.60261 | -43.97391 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6f579ba-0433-3119-871c-3eae5e47f388 | -19.659 | -45.85545 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ea5984-67ed-3e70-9bfb-421a21972353 | -22.79395 | -47.80935 | 2025-09-11 04:49:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30e2d9a8-e920-337a-a660-f5e41c0cd7ee | -17.37869 | -52.92271 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82f53ded-765a-3707-abbd-58daf386e758 | -18.0138 | -47.99724 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8faab932-69b0-3fdf-abda-6e4a4b594b79 | -17.94434 | -44.49023 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 114692e4-a607-33d1-9af4-28f621cba8c2 | -20.69895 | -46.06745 | 2025-09-11 04:49:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 46b5f414-c1f9-3e06-9b97-86783c67f5ed | -19.98378 | -47.62726 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ef7e793a-4d32-3a4f-9ed8-47b27f2abd54 | -19.9925 | -47.62888 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8652b34-e5fe-3f7e-859d-5dbe2aef9e48 | -16.61486 | -49.41615 | 2025-09-11 04:49:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63e5df74-3e8f-30e7-93f4-6b5d3237824a | -19.66159 | -45.85158 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 46bd5e19-1fe2-31d7-8659-e488c867b2bd | -17.20118 | -50.15046 | 2025-09-11 04:49:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea333988-62e9-3704-9ee4-77eb5590a016 | -19.80769 | -47.16283 | 2025-09-11 04:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c51a90a7-7c49-31dc-b277-ff8427fc373e | -17.83796 | -46.73627 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34949278-d837-30b6-bef2-1228d575e3a8 | -18.15464 | -48.10321 | 2025-09-11 04:49:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| affd5c94-bc8f-3643-8cfe-77203a307b04 | -17.24685 | -46.08788 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffacf8c0-4fea-3cf2-893b-98414058797a | -16.61495 | -49.78426 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9117fc79-fd27-38ae-b3b7-9f232e3813df | -20.00126 | -47.6302 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a86e72-0533-34f8-b795-25430d7d9795 | -16.55441 | -49.73962 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8632f0ca-e6c8-3c36-a504-a5707977f7cb | -19.66651 | -45.85218 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d753a98c-5045-3928-993f-9a8bf2a8a7c9 | -19.95669 | -46.88682 | 2025-09-11 04:49:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85474cbb-7cda-317b-bf59-692a819dab7a | -18.345 | -44.36765 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf9dc8f-595e-3a64-abd3-2f45b91e99f8 | -20.91229 | -49.46877 | 2025-09-11 04:49:00 | NOAA-20 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1e141e31-04c8-3ecf-b00e-b01a4892a493 | -17.8419 | -46.74156 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4e45524-0059-36f2-812c-72428d4a7a73 | -19.70878 | -44.23658 | 2025-09-11 04:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a77ca3ad-62a6-320d-968d-d407ce046e67 | -20.44588 | -49.99892 | 2025-09-11 04:49:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca13dc5d-3c80-3bb1-802b-c8ab4a54b67a | -19.95261 | -46.88177 | 2025-09-11 04:49:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4aa84fd-a134-39d6-a81a-1dcb4f53f7a2 | -18.15513 | -48.09937 | 2025-09-11 04:49:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 234dca33-5ac2-342f-a4ca-6aebdb6253b3 | -16.57045 | -49.73266 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffec79f1-a79b-37ca-a195-8dd874c7e447 | -20.35855 | -46.6596 | 2025-09-11 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26d7e3dc-2a6c-3ea9-a359-61a96b671a55 | -17.95128 | -44.47549 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 730a7eb7-40d0-32e3-b26b-cb2fb63f663d | -21.72479 | -50.09903 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 750e5110-f455-3087-99d7-c6b71340c435 | -16.18432 | -53.8686 | 2025-09-11 04:49:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf4c8584-3573-3f93-a61e-02a23b8b1bee | -17.3203 | -46.67746 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb14723a-ba23-35a6-8d99-3af21415d4d5 | -17.70525 | -44.43947 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d18453-e8b4-3583-9d2b-a74abe518bad | -16.53367 | -55.17506 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3880804a-41ac-3b9a-a55b-a2cbc3e2d00a | -17.23991 | -46.75972 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6ec3883-cd5e-3ea0-a200-63ee007c1e39 | -20.00543 | -47.63272 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c304ad08-5062-306e-9067-2fd9c0b0bd19 | -20.15536 | -41.03479 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3d45e8b1-6809-3849-ac56-7c0aed86adc5 | -17.56554 | -44.55106 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54ee6be9-6821-3609-aa7e-a369bde0da97 | -20.48705 | -54.91368 | 2025-09-11 04:49:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9f7a662-25af-3821-8bdd-c4607bd32757 | -21.29757 | -45.95922 | 2025-09-11 04:49:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5bf7064-9ac1-34c9-b51c-1612353b4d73 | -20.39024 | -46.63256 | 2025-09-11 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a73532b5-68b7-37f2-9e31-f49b7156b34f | -18.34693 | -44.36393 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 477f4e79-001f-3f9f-ae7c-bb965dfc56ca | -19.66391 | -45.85605 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bc7a9828-d21a-3cba-b24c-02ddc5030ed7 | -17.79922 | -44.41009 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb8f09d9-1b96-39b3-9d0e-efebbb4f8948 | -15.87508 | -54.93377 | 2025-09-11 04:49:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32ca7dd2-30a9-315e-9a99-71c5a7c757d3 | -19.75223 | -45.18758 | 2025-09-11 04:49:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14760e61-7b70-3e20-b214-3c8a0694df84 | -18.34872 | -49.33456 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fefad008-51c2-3456-aefd-b1d77e842465 | -21.66103 | -53.70142 | 2025-09-11 04:49:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 063b2891-2a60-3b8e-923f-7270e4378cdd | -17.84582 | -46.74691 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d4d8d4-f51b-3ea5-b63b-a3c4295ab75c | -17.51038 | -43.74488 | 2025-09-11 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c0b3fa4-9a1e-398c-8dc6-8d8aea5b871e | -16.62914 | -49.76322 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a5b34f4-9087-3a8a-aa50-88a9ab95144a | -19.80318 | -47.16221 | 2025-09-11 04:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42201131-b471-306e-9e7b-e7d60c8002ed | -17.93488 | -44.47924 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9050dda-f232-305a-abe6-cc98daee85be | -19.72551 | -43.91081 | 2025-09-11 04:49:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6870106a-f5fe-33df-819b-2aacf860482e | -18.71187 | -47.17873 | 2025-09-11 04:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 076d980d-4f61-3c2e-adfd-ddcc0c854b14 | -16.53027 | -55.17444 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2a73c3df-a83c-31ec-b7db-c79161cab981 | -19.34778 | -56.70199 | 2025-09-11 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 360e2e6b-88bc-33af-bbda-a558ebc13e9c | -16.5698 | -49.73726 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59d03cb3-646c-38f2-b8e4-8380801ab5f5 | -17.31733 | -46.75967 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d22f90e-511d-33ac-a463-5b293b106ddd | -19.23704 | -48.00165 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cb265dff-9c4e-34fd-b312-b7cf1eda209d | -16.63214 | -49.76867 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dab41b3-e968-35f4-9e0d-19efcce7b356 | -17.0656 | -49.6754 | 2025-09-11 04:49:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c868078-f107-33e6-9319-072bbd2a894a | -17.31072 | -49.3153 | 2025-09-11 04:49:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5855474-5087-35a2-a0ef-100072d29e2c | -17.71053 | -44.43991 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baf2f786-c79f-3b0f-a608-20da2b1ec2c5 | -15.8723 | -54.92939 | 2025-09-11 04:49:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8703710c-d6b2-31de-82f7-50be0ad79818 | -19.23653 | -48.00579 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ded344ff-df6b-362c-b9d7-60f70dde84fa | -16.58778 | -50.08614 | 2025-09-11 04:49:00 | NOAA-20 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb26beff-fdc1-392c-a60b-6e267d667ad2 | -16.62289 | -49.78116 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README122.md)
