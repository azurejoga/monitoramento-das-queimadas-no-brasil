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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af112445-06f6-3adf-8eff-d8e752729fbd | -11.74592 | -57.81862 | 2026-07-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 844bca63-1d58-3537-9089-6795b3045555 | -20.62952 | -41.39953 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1f909e3-90cc-32ec-bb32-8730f493b184 | -13.31543 | -45.14724 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d5423254-f087-3d4d-86d5-26530b580e69 | -20.07037 | -43.70702 | 2026-07-18 04:40:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fdb0aa4f-7bb6-350c-8bf0-f8a80ebdcbda | -20.63684 | -41.39502 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6c7aafd9-3c88-3777-870c-6a0e4d6e9d3c | -13.30769 | -45.14619 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d3d2e3d8-f942-38ea-b208-43b80e70f83b | -20.52509 | -42.35583 | 2026-07-18 04:40:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86c4f5ca-b3f3-3536-9284-0cf44affa1ed | -12.68508 | -48.21026 | 2026-07-18 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b7ab987-25a7-356d-9329-aa1269fa21e2 | -13.73484 | -51.87874 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8aad206-e5f8-3fe9-aac4-fe6d7ac6aade | -13.12311 | -52.51563 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8514a19d-cb5d-359e-800f-08cb486d3541 | -14.8764 | -48.46013 | 2026-07-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cab1b9b6-8afe-3ee4-bf6f-e104550b37c1 | -13.55756 | -47.78703 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8fe2d9-2fc9-3fc4-ae12-9773fe62d5c5 | -13.31669 | -45.14989 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fd7265a0-4a1d-35ff-91ef-8b0dbcaa6301 | -13.32056 | -45.15044 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dfe41fe-7c21-330b-829b-9caacdb5825d | -20.63519 | -41.39801 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0077b440-5c29-3581-af5a-3047edbd7552 | -18.73358 | -54.19848 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 49316df3-cc3d-3573-93ca-7cfd411382c3 | -14.08505 | -51.71722 | 2026-07-18 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 833f2193-875a-3cc8-834d-ce1a36c36b52 | -22.79647 | -49.34157 | 2026-07-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d23781ca-54b2-3a39-877a-106592d1a9c1 | -20.78543 | -57.93048 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 72df3f45-6011-31da-8b78-92b987a20bfc | -19.86985 | -57.95711 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9a3266f5-dc57-3bd0-856e-4e0d71b85b45 | -20.77863 | -57.93489 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 094ecb94-9fd6-3c45-bda8-0a6d1eac600c | -20.78113 | -57.9295 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6ede9727-161e-3bdd-9e9b-47725372ab2d | -22.24915 | -52.8695 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4dd9d14-7a0b-3441-bb8e-1f893dac59ef | -23.77883 | -49.04346 | 2026-07-18 04:42:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 470bcf85-0ed3-3d7e-9cf5-91e0abe50cb5 | -23.81717 | -48.71279 | 2026-07-18 04:42:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9db85aaf-3d9a-314d-9efc-f31bb33c9bb6 | -20.77348 | -57.9383 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2fc61e11-8e18-3706-b2dc-3d5214b38ea1 | -22.79298 | -49.34102 | 2026-07-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc04a022-7ce7-36ad-8786-06dec0ea0469 | -22.25312 | -52.86636 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2ec95e9e-558c-390e-8e8f-61cd50b96a1b | -19.82227 | -57.98928 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| de487cd5-01f0-336a-bbf9-23061fa86ba6 | -22.44984 | -45.23951 | 2026-07-18 04:42:00 | NOAA-20 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48ca00ec-bbec-3016-919f-95c50754de29 | -23.59961 | -48.25211 | 2026-07-18 04:42:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 407dd41e-74b7-38f7-aec9-ec28bf7881a9 | -19.81787 | -57.98829 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 501ea5f6-a3bd-3c2d-9569-27dd8aa95a4c | -19.83015 | -57.99582 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1b89a07-c334-34d2-b4e5-98f52c8c7aa0 | -21.85785 | -48.76002 | 2026-07-18 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1611e6aa-e6c7-3fb9-a402-bace9d93dbc9 | -22.7924 | -49.34519 | 2026-07-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edaf8afd-579f-38f1-af61-12ac0a919cd4 | -22.81194 | -43.56099 | 2026-07-18 04:42:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1c5670aa-3133-31cd-9c9c-a26691cd4f64 | -22.24853 | -52.87329 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30634a5b-8fcc-31d7-a741-d035579ff0ed | -19.80999 | -57.98175 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 59e466d6-2a24-36e5-acb0-dd3f7d51d85c | -24.63412 | -51.00932 | 2026-07-18 04:42:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 058fda1b-f4f7-3869-ae80-44f87aae3b36 | -20.77937 | -57.93826 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6bb98961-f552-3ff3-9100-ebc83762b89f | -21.85491 | -48.75522 | 2026-07-18 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7562da7-c660-3d3c-bbee-596c2d825015 | -22.25187 | -52.87393 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d3c041a-2ac4-3d94-b1bc-17d22a8e72a2 | -21.85845 | -48.75578 | 2026-07-18 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10ce36d4-ba1c-31e1-8891-a70341582fb7 | -22.45073 | -45.24096 | 2026-07-18 04:42:00 | NOAA-20 | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40f05259-7c33-341e-b96f-537c31ddf8e9 | -21.27074 | -49.15657 | 2026-07-18 04:42:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 186b6131-455d-321a-8aa5-e35133c6619f | -22.46598 | -43.0906 | 2026-07-18 04:42:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8e83815f-d13f-30e0-abe3-b5842f1b0e49 | -20.77419 | -57.94166 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53167c90-4dfa-3feb-a6a7-eceb493ba323 | -22.27777 | -56.07456 | 2026-07-18 04:42:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97fa8879-84f8-3bc0-9c44-3f17f1d59b9b | -22.47143 | -43.08688 | 2026-07-18 04:42:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2e3f9ebe-535a-3f3c-bd32-6e849bb116ea | -20.77948 | -57.9305 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 95f9c933-ece4-382c-9ebe-60dfa6fa8bf6 | -21.26216 | -49.11781 | 2026-07-18 04:42:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f9e928e8-066d-3261-9e59-1b5a9b16e187 | -22.2479 | -52.87708 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8ff98acf-c982-30bc-ba4b-9ce4f864f3c1 | -22.79706 | -49.33738 | 2026-07-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caceb9c1-6a89-311a-bd54-43e49a6d3399 | -22.28152 | -56.07541 | 2026-07-18 04:42:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0de49ce-0999-390e-8afa-208d2210048b | -19.82086 | -57.9272 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5e729219-c294-3b8e-8367-fbad4a024547 | -19.81558 | -57.93075 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 36e08965-f275-3ca8-b279-f80b249b1754 | -23.16078 | -46.57729 | 2026-07-18 04:42:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d0b4c6e6-142b-3156-b539-194c8263ebf3 | -23.83027 | -47.509 | 2026-07-18 04:42:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5f639df-d731-380c-a3a7-7823bde3608d | -23.59899 | -48.25684 | 2026-07-18 04:42:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a73b0d-490c-3bc9-b3de-4a1b50094b6f | -19.81347 | -57.98731 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8aa79a00-e593-3dc1-ae79-959c518814b8 | -19.82576 | -57.99483 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ccba12dc-8ebd-345c-9749-74aab4d51b44 | -20.77507 | -57.93729 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| adb450eb-c024-35ae-adeb-c18845eb04b1 | -22.25249 | -52.87014 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b56a953c-a68a-387f-8ee5-57b5014a2144 | -19.81468 | -57.93528 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 86b922ed-1784-3475-a508-87941a3ed263 | -22.79589 | -49.34575 | 2026-07-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4387174-9718-3124-987b-eec4eb63f21d | -23.82078 | -48.71339 | 2026-07-18 04:42:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c97c79ae-865d-32e0-9a35-779b22a6acb3 | -21.66396 | -56.3305 | 2026-07-18 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 286003e8-41c2-3bbe-a7b0-c40127cd9df1 | -21.25869 | -49.11725 | 2026-07-18 04:42:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2101509d-3148-346e-a5f9-8a4a546bece3 | -22.92444 | -48.73294 | 2026-07-18 04:42:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f294403-595f-3c4c-8d13-69194ac7c402 | -21.85431 | -48.75946 | 2026-07-18 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 926cb0cd-6c4d-3260-87aa-61f4498c872b | -20.64071 | -47.20969 | 2026-07-18 04:42:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b1527b0-2f8a-35bb-8dcf-6a02eaf5a7cf | -22.47131 | -43.08732 | 2026-07-18 04:42:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5d3933df-eba1-3114-bdb9-955e846116e4 | -23.45286 | -52.01048 | 2026-07-18 04:42:00 | NOAA-20 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0ce56649-1f95-3a6e-aceb-0548489d4a64 | -19.8109 | -57.97719 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c2e2a90d-d6ee-33a3-98e7-058e203d0046 | -19.82136 | -57.99385 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 377c230b-59c1-391f-89f9-ff9544f7254e | -22.57188 | -47.30719 | 2026-07-18 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a78d1294-bb1e-33b5-af91-a76354e5c7b4 | -19.81996 | -57.93172 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 71467037-6066-3373-9708-e86ef6cfa48b | -22.46588 | -43.09098 | 2026-07-18 04:42:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3d58e066-ba0f-318d-a44d-71ff2dbbe062 | -23.45617 | -52.01109 | 2026-07-18 04:42:00 | NOAA-20 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fb63b1b7-6923-38f8-8044-0384bf996f2a | -22.25855 | -52.87522 | 2026-07-18 04:42:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7e8453f-7443-394f-853e-d9b95631ab2b | -21.2742 | -49.15714 | 2026-07-18 04:42:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 452819ec-d178-3207-ba5d-03f8d455a57f | -23.76102 | -47.33017 | 2026-07-18 04:42:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8edc7cf6-0db3-369d-81dc-7098695ca83e | -22.92086 | -48.73238 | 2026-07-18 04:42:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 27e27a4f-d6ab-3303-91ee-fe0f18d85855 | -20.43017 | -54.5611 | 2026-07-18 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0b154f-28e2-3ef9-8246-eb5a62d013c2 | -21.77081 | -56.3013 | 2026-07-18 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4df4d3df-2af0-3804-9a8b-aa978da8a86c | -19.81377 | -57.93981 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ab020d32-aa0e-380e-86f4-e506a4e2bcc4 | -22.37759 | -49.78431 | 2026-07-18 04:42:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 13c5618c-37fd-3347-be1d-f0e157737324 | -19.81439 | -57.98273 | 2026-07-18 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 702f24fb-2516-3be9-8d49-a89867cdc092 | -28.67698 | -56.02884 | 2026-07-18 04:44:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| de9d0508-b930-33af-9985-f484882dbe27 | -28.08872 | -50.59564 | 2026-07-18 04:44:00 | NOAA-20 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 53237dcd-9ce3-38b1-a632-144dbcbf02e8 | -29.07551 | -50.7294 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| df7bef31-59fd-3f52-b318-b1444a39941d | -28.67985 | -56.02689 | 2026-07-18 04:44:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 4e95771d-4a19-3700-8f02-b9cb1dbb012d | -28.758 | -50.00721 | 2026-07-18 04:44:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 33966c86-849b-3e09-b528-b4cfccb5f94a | -30.09804 | -56.65456 | 2026-07-18 04:44:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| cd34846a-7276-312c-95f2-eb712e8c0ede | -29.27458 | -50.34829 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2caf2616-d62c-332c-b183-14154e470d5e | -28.09222 | -50.5962 | 2026-07-18 04:44:00 | NOAA-20 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 96d21cba-9b54-3082-98d9-a0d5b33282f5 | -29.07603 | -50.72742 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6843b653-42b6-33fc-b8d3-27ae0ad81ed3 | -27.34513 | -50.72635 | 2026-07-18 04:44:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12f27bf3-8f56-34f7-8128-7d27ba132bea | -29.9294 | -53.91057 | 2026-07-18 04:44:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 080acab0-0228-3a3f-a173-c84d6c89b670 | -30.20926 | -53.9923 | 2026-07-18 04:44:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
