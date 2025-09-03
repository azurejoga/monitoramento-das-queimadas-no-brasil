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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49a996d5-2a09-30ef-ae7a-fd2539450020 | -22.86617 | -47.39014 | 2025-09-03 04:51:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 201b86aa-7f91-3cdc-8b79-7878a32bb3d7 | -22.17667 | -48.83272 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| cadf0bd4-f6e1-3431-9f85-8879b585b362 | -19.14096 | -47.69955 | 2025-09-03 04:51:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c9f71bf-e289-3dac-b0b6-685a093f45fe | -23.92438 | -48.86154 | 2025-09-03 04:51:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d16658-6c3c-385b-b3c4-d5b0afe92223 | -24.41118 | -49.90887 | 2025-09-03 04:51:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6922fd73-44e6-37a8-b8f0-c9bb11fa31a2 | -22.7585 | -47.26796 | 2025-09-03 04:51:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 860eb87e-9279-3a54-b4e9-7484487f54a5 | -20.89023 | -55.14403 | 2025-09-03 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9daadf88-2853-3afa-9767-8d29beeaf58c | -24.41071 | -49.91275 | 2025-09-03 04:51:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e1441ab-7677-31bf-8ae8-9cb8626042d9 | -18.14118 | -51.74621 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aba28056-3db4-3269-bbf9-5a93c385d3c2 | -22.75267 | -47.27778 | 2025-09-03 04:51:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8bc78b1-42c7-3730-8aa5-788e992f1b09 | -18.66494 | -49.09065 | 2025-09-03 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df3e2cd1-1f26-39b1-bafa-e4ada3201785 | -20.70724 | -46.30093 | 2025-09-03 04:51:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2967be16-17ab-382c-ab3c-09de21f3ca2b | -21.24352 | -46.13406 | 2025-09-03 04:51:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d67151a3-7f65-3935-9e57-f931ca0ae376 | -22.17246 | -48.83207 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| ae372a96-2faa-38f0-a97a-8a0a74db167e | -22.66332 | -50.67035 | 2025-09-03 04:51:00 | NOAA-21 | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 43f68530-adef-3492-982b-34a8330dce4e | -20.89551 | -50.09677 | 2025-09-03 04:51:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d542d4db-978d-3114-8bf0-1b831c7746a5 | -22.18091 | -48.83114 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f2a5d5e1-d982-3de2-91c0-f1e78a0cb9e9 | -22.00519 | -45.06456 | 2025-09-03 04:51:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4491e14a-585b-352b-a445-1738980ac14d | -19.36789 | -49.11381 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9b48c43-1907-386a-877b-b2dff613bac2 | -22.65952 | -50.66977 | 2025-09-03 04:51:00 | NOAA-21 | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 90ea0d88-5495-3888-b78b-d8a5109a54a0 | -22.17771 | -48.82224 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 14acdd6e-4aeb-3a3d-8b04-c1a3ed24c110 | -18.66099 | -49.09003 | 2025-09-03 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f3f76ee-4249-30b2-bcc2-42b6192fb562 | -22.1762 | -48.83463 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aaaf087d-d7e6-3dd8-b5be-04f5f44d25d9 | -23.20877 | -49.41254 | 2025-09-03 04:51:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffb3598a-b5b2-38d1-b901-aab2304ada69 | -23.92917 | -48.85782 | 2025-09-03 04:51:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44233ce4-0bae-33d3-83a7-9807958d5582 | -23.66861 | -55.21658 | 2025-09-03 04:51:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33a7326c-a4c1-3ac6-a2ae-304627a4c447 | -23.67134 | -55.22094 | 2025-09-03 04:51:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a33d93e-81ac-3e48-8164-edb2d6f30feb | -22.1767 | -48.83054 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| bcf432ac-fc37-3fbf-9f39-cbe143db0c2c | -19.36391 | -49.11314 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aa05102-4acf-31b0-8290-74d4e021fffb | -23.36108 | -47.17712 | 2025-09-03 04:51:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7212227b-fc8b-3814-b517-dd13c67a592f | -22.18605 | -48.82569 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a660417b-7d6f-3498-b03e-8c3f8872559e | -21.08452 | -45.45506 | 2025-09-03 04:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c561fd2-2d20-3059-a602-98e3ec9ca500 | -19.13613 | -47.70296 | 2025-09-03 04:51:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91eb41b2-6707-30f1-b297-19a471f33f1d | -20.40588 | -45.69483 | 2025-09-03 04:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53e77ca1-b7e3-3002-afaa-cb85131aab5e | -18.14462 | -51.74678 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b555bee9-3daf-3bdc-b9b2-3ecaf1e320dc | -19.14385 | -47.60119 | 2025-09-03 04:51:00 | NOAA-21 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f741ddb-a035-35a3-a80d-8ba7f9b0e140 | -18.63816 | -51.8455 | 2025-09-03 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f65287d-eaf2-3f80-af38-86c3f1a08e71 | -24.08603 | -52.37955 | 2025-09-03 04:51:00 | NOAA-21 | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccc9c3c1-3c25-3993-8cc8-1cd5f07c8f38 | -18.66889 | -49.09127 | 2025-09-03 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56066e19-437f-3c0c-9293-1c6190c92c5a | -23.39519 | -45.96547 | 2025-09-03 04:51:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 239b3a64-c710-3eee-8d82-8dc825dceda5 | -23.35689 | -47.1709 | 2025-09-03 04:51:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4785f35a-863e-3a6e-bac0-5bbac1a0dedf | -20.89083 | -55.14033 | 2025-09-03 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e6c8cc-0e5b-3317-b2a0-6ee65e217505 | -23.48469 | -51.81438 | 2025-09-03 04:51:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3d8dae68-8c97-3cd9-a0bc-b23a52420ff7 | -23.34911 | -47.15247 | 2025-09-03 04:51:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a97de66c-57c3-3be3-8c91-ee7d4a94f4e1 | -19.12311 | -46.44044 | 2025-09-03 04:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643c2e61-72d2-3c85-8ca6-26d68f5a6f7a | -22.18231 | -48.82093 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b9fb9555-fe8c-38a7-a681-88edd9ad40fd | -23.67075 | -55.22469 | 2025-09-03 04:51:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a828885e-e8aa-3ca8-a6e0-89a2c033a2a6 | -22.1781 | -48.82026 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f80f5a00-0c31-3029-bbf6-88bd5a22d8bc | -22.70625 | -47.03575 | 2025-09-03 04:51:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da0fefb4-50d3-3095-bf3a-ee8c70b76a69 | -24.41101 | -49.91131 | 2025-09-03 04:51:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45f6566c-de28-335d-8d83-456404439d70 | -18.14175 | -51.74227 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0623e429-aa12-3b21-849c-21c4ccdd6521 | -22.18242 | -48.81872 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7f14e406-2177-3328-a56a-85a886e50f7f | -23.32805 | -47.84292 | 2025-09-03 04:51:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e8af928-41f1-39aa-b2a3-d925ebbfc0d1 | -19.14147 | -47.69535 | 2025-09-03 04:51:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40618da7-4c62-3e50-bd23-01444698ad28 | -23.66803 | -55.22033 | 2025-09-03 04:51:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 93d0a468-c03c-36b9-8c7b-2d963e30ab2c | -22.172 | -48.83398 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 27d6a7d3-42c2-304e-82c9-34755cc0bc49 | -19.14874 | -47.59751 | 2025-09-03 04:51:00 | NOAA-21 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fca77711-43ea-3872-9091-82248f5475d5 | -22.18192 | -48.82288 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 21525b98-9c24-3d73-9709-f0f5ba4eb69c | -23.04266 | -45.54059 | 2025-09-03 04:51:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d99259d-ba32-36a9-959e-e3b2e9914446 | -19.82943 | -45.67582 | 2025-09-03 04:51:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46470686-7066-364d-bbd2-cfc4c550b33d | -18.66032 | -49.09514 | 2025-09-03 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a63c909-9c75-32b1-aa01-5e2f8f902883 | -23.48409 | -51.81889 | 2025-09-03 04:51:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a69507f3-adf3-33c3-973a-15a98f02d920 | -22.17249 | -48.82991 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 15d68631-df35-33c3-86f7-146527761118 | -22.18141 | -48.82701 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b632fe8f-64db-38cb-a76c-fe29ba99f8ab | -22.76173 | -46.22486 | 2025-09-03 04:51:00 | NOAA-21 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ebf479e-8d3f-3103-98fa-ebb656d9190c | -20.75013 | -47.1319 | 2025-09-03 04:51:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2313b50-1bf8-3f1f-aff2-0629ce2dc99d | -20.89485 | -50.10186 | 2025-09-03 04:51:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bde7226c-1583-3355-9fcf-5eb555bf103e | -22.00605 | -45.05564 | 2025-09-03 04:51:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a49d2fe-e145-3520-99a3-9bcd4410bc23 | -20.47929 | -53.6773 | 2025-09-03 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab1da1c9-e904-32a6-bbff-40571238ea46 | -19.36721 | -49.11919 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 784028c2-ed43-3c99-8f32-a5d3aa392994 | -22.49105 | -49.01149 | 2025-09-03 04:51:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a569e75-976b-3e46-8920-030c48c0b206 | -18.14005 | -51.75411 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1198b00a-518b-35a2-8c16-7ad5c5f47988 | -20.41089 | -45.69592 | 2025-09-03 04:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22e621f5-a9ba-3e4c-b0f8-b46a194f7665 | -20.90195 | -55.13473 | 2025-09-03 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d4ec47f-797c-3ee5-9ec8-5a5f5abf5025 | -26.71413 | -52.44371 | 2025-09-03 04:53:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a6dd73e6-c7ab-3a87-b079-96904448340d | -7.7039 | -48.7371 | 2025-09-03 05:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 139.5 |
| dcec4386-762b-3e35-b66e-931e9a6915dc | -7.7036 | -48.7587 | 2025-09-03 05:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 934215a8-bb72-302a-be01-35ddc01c9d0b | -12.9382 | -56.9856 | 2025-09-03 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b29eeeab-8215-36d6-bfcc-90ba65930d9d | -11.5963 | -52.155 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4a2d96ba-ae5b-37b2-9124-0084b1eac8f0 | -11.5779 | -52.115 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| dddb91f6-125f-3c19-a27f-a493d2154af6 | -11.6156 | -52.132 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 47e21e79-1aff-351a-bb3d-e5d8763b1ec6 | -7.6851 | -48.7386 | 2025-09-03 05:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a82c47ea-6988-3c81-a5e1-c967788bd76a | -7.7036 | -48.7587 | 2025-09-03 05:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d31a4e15-5c3a-3eb0-a6de-7dd579ca06d8 | -11.5776 | -52.136 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 411fc744-6609-370a-8a15-4a43d0bb2cd4 | -7.7039 | -48.7371 | 2025-09-03 05:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 3699ae14-08c6-3f50-92b2-058a71c9ec99 | -11.5966 | -52.134 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 246.3 |
| 4d518a91-5cf3-3e78-936d-0ce88ed95a41 | -11.5969 | -52.113 | 2025-09-03 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 86e68ffb-1344-3fe8-844a-995bb7041176 | -2.90346 | -48.29676 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bfb64ba-b3a5-3a25-b816-b9cfc123e40b | -8.0689 | -45.38057 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb5bdbfe-6f49-3243-a4a5-e71151ed6257 | -6.87852 | -45.56229 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e33d7a-2151-3a30-8ecd-6a17b8ae6ef8 | -6.78679 | -52.81534 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 905b48ab-00c8-3fe0-a176-fe0cab415b90 | -6.465 | -49.52372 | 2025-09-03 05:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a75ff4c9-104f-3d11-9e79-0850b975179d | -6.03066 | -46.01377 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5c2911b-6b14-3c01-8861-48628a9c6a00 | -8.07113 | -45.37192 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31ac70b6-dd0e-33cb-822a-c19ad717d48f | -5.8189 | -43.22309 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 59267308-4b64-3e18-b2e4-9768b3db303e | -5.69186 | -45.94267 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ec6d80-aaec-3476-84e1-b7b79a8efda1 | -7.90299 | -46.43658 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 139bd566-ce0d-388e-880e-58a8fe88a038 | -7.89619 | -46.44091 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b84a6fd8-86cc-3d20-ae55-6acfec2ef240 | -5.70603 | -53.6923 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f90ff6cb-6be1-363a-b950-bd5c05e02c7c | -5.90254 | -57.74964 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README80.md)
