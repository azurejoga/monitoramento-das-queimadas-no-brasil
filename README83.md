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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f808fa0a-b9fc-3c20-906a-f8bb6bf03f7f | -16.64895 | -52.52728 | 2025-10-18 04:51:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0791cffa-2a1d-332b-a9c4-b85b2e5c920b | -12.70203 | -48.62471 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cbf39d8-579e-323c-b29e-95682ea5af16 | -14.43253 | -52.90358 | 2025-10-18 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7e026da-6019-3622-8b8c-bf2687361229 | -14.85875 | -52.43755 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df7b430d-dcfb-3f9a-8c03-f82ce25d6951 | -9.77754 | -57.41101 | 2025-10-18 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61fce6f8-c6fb-3ee5-acfe-8ef42c2b27ad | -13.77115 | -48.23462 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527c2592-c5bd-3e35-9903-b4ffa206e30a | -13.40454 | -48.58327 | 2025-10-18 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fd44ff7-d159-345a-a297-b35aece20e2d | -11.47739 | -44.01848 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 568a2619-a243-3a51-afbd-807bf08c6fbf | -10.92126 | -47.9859 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b545fbfe-ecfe-3bb1-8f62-3cb04e15021b | -12.70151 | -48.62853 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d8ccd61-230d-3059-959b-8e48117749d6 | -12.20629 | -43.56035 | 2025-10-18 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78a24079-0d94-3f77-b4f4-1c8e839db8c0 | -11.60022 | -44.06739 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fc91078-fbc1-3dbd-99e8-1990c1207a85 | -15.5847 | -44.5124 | 2025-10-18 04:51:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d2a3037-50c0-3a99-b910-8bd816cb093b | -11.61434 | -44.08717 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69bff0c3-ef8a-316c-b34b-d63b0d4d30bd | -11.60523 | -44.07159 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 964eb5fd-b94b-366c-aa52-675f404f7eb5 | -10.80447 | -44.02084 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e915d0b0-a23a-3585-8236-daad22227a79 | -11.00229 | -47.90591 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd1c14e3-5481-34d3-af13-73d63385cb58 | -14.9158 | -52.4307 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e209896-7bab-37aa-91b1-82876e0247b2 | -10.95503 | -45.452 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed4028f3-c14e-3f1b-ade3-a12ed2c07522 | -14.09154 | -43.63617 | 2025-10-18 04:51:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b577e796-b7bd-3371-8116-d569dacb0cdc | -9.21812 | -61.82981 | 2025-10-18 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d19f8f6-f498-3b53-b914-8404cb0d8c60 | -12.1683 | -45.0967 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06109ef2-b954-38b7-8fe4-e327044cc6b5 | -10.48966 | -43.44198 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 70710914-ef75-3ea7-872d-affed5de4ac2 | -9.35979 | -60.8637 | 2025-10-18 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e330b0ef-5a3b-3ea4-9268-7793a9bacbb5 | -12.90342 | -47.00917 | 2025-10-18 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed5618ab-20ad-3505-869f-81bafa807aa6 | -13.40949 | -47.9731 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 164d12e5-0707-3d87-a7a2-92d09314da46 | -10.53812 | -55.25946 | 2025-10-18 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53225c89-08fc-3ef4-bf4a-e2998277eecb | -13.51294 | -48.00338 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6551353e-a1fc-3764-ad81-14a2fd5b2fa3 | -11.60799 | -44.09363 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cad6564f-02de-3a9b-abf8-3252bd9d5d99 | -10.98067 | -44.31987 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 142afc2d-8627-3ece-a947-346380f70c13 | -10.27809 | -44.05463 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d043872b-7443-3c37-a5bd-7eab41cf1c06 | -11.75823 | -61.068 | 2025-10-18 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9691e67-811d-3c35-89d1-3320b166c8cf | -10.23188 | -44.04874 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b23f8b5-85c7-34de-880e-42d03ccc366f | -12.15581 | -45.07241 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 496552dc-59de-3153-b8f8-345b9cf5d3d6 | -15.58427 | -44.51626 | 2025-10-18 04:51:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b701067d-bdea-31f3-9e2e-3d101cf0b87b | -9.8923 | -55.39141 | 2025-10-18 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3693f364-7606-3787-8b7a-cd619c5cb8ba | -10.63042 | -42.30636 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a438b3fc-1f7f-3f1a-937d-f4dac538c0eb | -10.6953 | -44.55087 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7caa57f9-2943-31a4-bad9-55f4232ca127 | -12.16519 | -45.0574 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a64ec1f7-47c3-30e5-8188-9c46bd443bfe | -13.45434 | -47.93151 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05f1f9ec-8484-3b7a-873a-78c2baf1440c | -9.96587 | -50.9114 | 2025-10-18 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3218f473-361b-32c6-aa3f-e85351aeb374 | -14.76013 | -48.19699 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd86422-9973-3c4a-ba19-aa3f4784f36f | -13.26809 | -46.44179 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbd8d915-a81f-3300-aba2-e5e957531aeb | -10.13097 | -44.53518 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc3e360-af96-339f-8a0e-19cd56540295 | -13.91984 | -45.59978 | 2025-10-18 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48d8c35c-a3ef-36d3-b5ff-3e052d94f709 | -11.34641 | -45.25974 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f57849c-a2ba-3392-9ac4-39a072428d5d | -12.30279 | -47.26205 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f1998d-8bf0-3e42-8f23-96dc4ec4681f | -10.63097 | -42.30182 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3944c515-c75a-35ed-880d-0a4a104bc113 | -10.07379 | -47.63865 | 2025-10-18 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6503e94c-fa02-3f9d-aa87-813bafb82db3 | -10.82097 | -43.93213 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e191bf30-2471-3769-9bd1-b6f31efd40a5 | -10.41632 | -47.74421 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80b800fa-6ce5-3c91-bc18-7e073266cf22 | -10.14055 | -44.58263 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a1dab4-1a51-3e0e-bc7c-2a2a671b77a5 | -13.69224 | -47.72506 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1487fa03-228e-3d85-a169-07ffa20853a2 | -10.16259 | -44.53506 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4edf4506-bf7f-31ad-a78c-edb772a21188 | -14.74707 | -48.18003 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea0d485-40cd-35cb-a2aa-b90d18f2735e | -12.99094 | -48.45629 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e0b7d6e-c191-35e0-91b8-eabce6995da5 | -10.68926 | -44.55655 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dfb7610-afdd-3d05-957e-3e34ec512243 | -10.14534 | -44.58615 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42dde026-fb5b-3ca1-95da-cd9e62b4fe17 | -12.46006 | -45.47527 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b0c0103-e469-3e08-bc4b-b26dc703c10a | -11.20654 | -47.83445 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f745aa1e-56aa-3fd8-8d0e-6806a8cc59b9 | -14.12799 | -44.71052 | 2025-10-18 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f662d84-508b-3136-9df5-226f78a95d97 | -11.5902 | -44.0589 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fe72fb7-3d42-3ba1-80b1-b15f7e4df513 | -13.04073 | -48.19225 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31f592b8-8889-3a2d-95ea-77703061bbca | -10.10667 | -44.56042 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31ebed0f-da96-3afd-a508-f97be443f4be | -11.43956 | -54.09584 | 2025-10-18 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66bd9b53-7b3d-3afc-a723-694d198346af | -10.49336 | -43.45768 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a47633-9b08-3ada-b366-df7196b3ef4c | -11.60478 | -44.07513 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1056b988-b778-3206-9efe-482c04f96504 | -13.61155 | -43.96644 | 2025-10-18 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af1dc577-413d-3d6c-b44b-3ca8256740c9 | -11.50611 | -44.05478 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c84f2c18-a3a6-31e3-a7d1-cfeeaa320657 | -12.66025 | -54.76995 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 109adf44-5a0c-333e-856f-40deacb0f9f5 | -10.70093 | -44.54831 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a98d09c-b900-3ecd-a309-714cb2968a57 | -14.4471 | -52.8984 | 2025-10-18 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ec9ce81-9b9c-382a-b3fd-43fd6fd316a3 | -14.47843 | -48.60957 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ef09f55-3ccd-3963-8ffa-9ad4f9613316 | -11.40456 | -44.27357 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60dad016-089e-36f4-8892-af20bf9914ad | -11.84939 | -56.86179 | 2025-10-18 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1a8116-2c90-3cee-bfd5-e19f528cf48a | -10.69447 | -44.55721 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ac76470-351c-368e-9b7b-4d168979ead8 | -13.52095 | -48.00888 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c09561c-60ae-3042-9e9f-732da998af6d | -10.62069 | -48.02076 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4dd3e7-2386-3f60-a739-17776ea962d3 | -10.70574 | -44.55209 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821cda1a-b454-3885-91e5-4e7054655a6f | -10.68364 | -44.55902 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20e13835-3ff0-38e2-949f-08475ed6b970 | -10.95016 | -45.4509 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e3e32cf-432f-35f5-871e-62689fd687cb | -10.2337 | -44.07641 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d499fafe-2f9e-356f-a590-bd809b33b127 | -10.39977 | -57.28848 | 2025-10-18 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a534240-e340-35a8-b04d-6d0caee068f0 | -10.49289 | -43.46141 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f198234-2793-3965-a907-d2d9b49dffea | -13.77543 | -48.23489 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3158401b-79a5-3de3-949b-cd62eddf9eef | -10.15777 | -44.53172 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 885df3f2-952f-3d9e-bbde-eb39276f1bb8 | -11.35994 | -44.28169 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b7a6341-429a-3ddb-8a35-20f7b0f65ab3 | -13.76589 | -48.24163 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dda6d74-cde5-3deb-9c0e-f1171048ac8b | -11.61479 | -44.08362 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0f7e18d4-d860-327e-a2f9-cc2346856bc2 | -10.23233 | -44.04529 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfd56e13-89e5-3f1d-9967-59dd0d4a8fd4 | -17.84735 | -42.62052 | 2025-10-18 04:51:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b427587-84b6-300d-bfa0-8583b43d7cfc | -10.2434 | -44.044 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae35f3fc-a347-3bf3-a96c-7e5668e4bbd2 | -9.3219 | -56.26743 | 2025-10-18 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301bf79c-5580-3630-8b69-55284037af39 | -11.72166 | -59.1233 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8e1f3c5-bf8a-3819-8d18-ecc538132b65 | -11.36187 | -45.25849 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c09d63c9-228a-351d-9f65-406655c7df92 | -15.03709 | -46.61549 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c950dae8-b673-35aa-a4de-2e272241617a | -11.47282 | -44.01058 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4968843-83be-3fda-b100-248d30f1370b | -11.94452 | -44.23994 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a00f2e4-3d35-30a1-9ca9-62612751f5dc | -11.40412 | -44.27699 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 874e41be-571a-3f85-b5b2-5b5ec9bb1dde | -12.45466 | -45.47767 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README84.md)
