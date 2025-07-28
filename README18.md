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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 786305a7-37e8-3329-b0ae-0de050cc3704 | -14.98932 | -46.97588 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0695fb2e-b8e4-3955-8df1-445661aad9af | -14.4997 | -48.6488 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dcca4f8-6df9-37a0-bbe8-62c696df8d72 | -14.98344 | -46.9641 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe732831-f0ae-3d86-9bca-4986589ba513 | -11.21021 | -55.92496 | 2025-07-28 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93c38aeb-5176-3f62-9245-2f7b82218c78 | -10.75109 | -52.76747 | 2025-07-28 05:08:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba065b44-29bc-3c17-b5e8-962a99a364ba | -14.49448 | -48.64801 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2031623-d888-39c2-ae71-ba9f6219101e | -12.66199 | -47.02514 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cef3ab5-9934-38cc-a9db-63905babbd6b | -10.54405 | -49.4926 | 2025-07-28 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 900640fb-4b96-33be-9fe8-2a5c061de16d | -13.12089 | -47.37403 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0a0f6f8-5eda-352d-8373-3c24c3cec029 | -10.0382 | -59.10557 | 2025-07-28 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 577600e3-d18e-3aef-bee2-55b678a488e2 | -14.51876 | -48.66716 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2eecfa8-3d1d-32f2-b623-1cdd0cbd8dd6 | -14.98448 | -46.96605 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ea6aaf8-6c78-3a26-a5e2-1a520d323dd1 | -11.52128 | -54.68354 | 2025-07-28 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 691cb323-8871-3efe-bf41-59f67a26be9a | -11.30246 | -55.1466 | 2025-07-28 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27e109bc-0b32-3166-85d2-c3dd4c231abe | -6.5074 | -56.213 | 2025-07-28 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2dfff44a-7515-346c-abb8-72f8262c104f | -18.40376 | -54.88964 | 2025-07-28 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad3d1feb-e977-3332-a80f-85ed82839e37 | -23.33037 | -46.89146 | 2025-07-28 05:10:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a26283ae-55bb-3b5f-9af4-8d2ee78c5316 | -20.47714 | -53.67426 | 2025-07-28 05:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4acaf9b2-61c3-3b68-9dc8-94935ccc9f7f | -22.76527 | -44.68317 | 2025-07-28 05:10:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6e353a66-8bbe-381d-8490-3fce1e550a37 | -18.40005 | -54.88917 | 2025-07-28 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 481616eb-b215-3a0f-b9f3-3333509f36c4 | -22.75803 | -44.68221 | 2025-07-28 05:10:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 117dff1e-fc60-3ee0-a0ea-0099c86931e6 | -23.32432 | -46.88535 | 2025-07-28 05:10:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b0644b3-8b5b-37d7-bd72-08bc2c8561b5 | -23.33082 | -46.88539 | 2025-07-28 05:10:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d4407c4a-d092-35ea-82f5-8349c8699510 | -20.48741 | -54.57005 | 2025-07-28 05:10:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d83b950-da73-30be-8f0f-4397ceb5dd33 | -7.80637 | -50.77611 | 2025-07-28 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8adc8b12-b1c0-31a0-b67d-3418d9debb74 | -6.5492 | -56.19622 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23c2ee05-5b45-3867-92ef-8d35db7f0919 | -6.49405 | -56.19755 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c67e86b-e8dc-351c-9d0f-f2e1c3b5fd7c | -3.21719 | -48.818 | 2025-07-28 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0ffd42de-73f9-3c62-9444-81c65a72b213 | -6.89633 | -52.86638 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec69503f-98d4-3026-9363-543287bc472f | -6.49345 | -56.20164 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1d7960c-6b0c-3d0e-b023-98dad7a103f6 | -6.39675 | -53.36085 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb619c4-50aa-3308-babd-e6810e5c2c76 | -6.50149 | -56.20703 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2dd8f92a-5abb-327e-9c00-59ea9b01fb34 | -6.39651 | -53.3612 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d67356a8-f29c-3540-a28f-33e2404b8b24 | -6.49717 | -56.2064 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4117834d-919c-3946-8961-7642473d3ced | -3.29872 | -49.196 | 2025-07-28 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13567c7a-5555-3ecf-9e70-11af6591d029 | -3.21944 | -48.82203 | 2025-07-28 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c06cbaa2-06be-3840-88f7-a567f1e86cc7 | -3.88223 | -54.21293 | 2025-07-28 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78e9a366-b96b-3775-a256-03f50c002046 | -6.90047 | -52.87095 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 648bd188-3528-36e1-9028-bffdacf0a0ec | -6.9018 | -52.86716 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb75a916-3d28-393a-bb05-ea034540f202 | -6.89551 | -52.8666 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 831896f4-0a2e-3bb8-8451-4c13a01dfde8 | -6.895 | -52.87018 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f953da-d282-3a64-86e0-49031478adf0 | -4.10771 | -47.92599 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a015b680-6c43-300d-b5fb-00ecc90b4c61 | -4.11171 | -47.92541 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73e21fc7-bf8a-38a6-81c7-5b7d27bb7dc5 | -7.80572 | -50.78131 | 2025-07-28 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29080c0a-0aec-3b3c-8479-3bb6864ec381 | -6.40175 | -53.36199 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920f956d-f9e1-35f6-9ccb-28cca6cc38b3 | -6.5021 | -56.2029 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e4f1df-b823-3c65-bf60-78ee7f069b0a | -6.40338 | -53.352 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6d1e9b8-c811-3fca-aa01-3ad8aecc87c7 | -4.10663 | -47.93367 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 482fb778-7ccc-338b-a60c-550efcab0e42 | -6.54546 | -56.19144 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd74cf57-51de-3e9f-aabf-fee183b5d16c | -6.49596 | -56.21468 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3600b73-6b84-33e6-bc45-69a659930bd5 | -3.29954 | -49.19038 | 2025-07-28 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35646b44-b3fc-33b9-842d-c9a0aa6fda00 | -6.39694 | -53.35797 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5ec9e7f-5ea8-3fa4-b64d-303a82142db5 | -4.30461 | -48.09838 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7555c2a1-6006-3d8a-9fe5-b3f1151a55c7 | -6.40219 | -53.35878 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a65f21a8-6900-3883-97fa-9c4e306a475c | -6.49898 | -56.19405 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32ab9f30-4d26-3197-9727-49d0718fe532 | -6.49285 | -56.20576 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83d746c7-f2f8-35b3-895d-b8e9def54ed1 | -4.11059 | -47.93306 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52e9184c-d496-3306-bf27-07e5a5de3a85 | -6.49656 | -56.21054 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 909a8eb0-007f-3060-b04e-0434ba42304f | -6.88957 | -52.86919 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8500d23-8256-39ed-8d01-222651599a6c | -6.54487 | -56.19563 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d58881d-4345-3a14-8cd4-58ea235bd5a7 | -6.90098 | -52.86737 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 911840d6-79c3-3e97-8073-3752505f67ce | -6.50088 | -56.21118 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 39283d2c-0ec1-3037-a37a-aab7d936ebb4 | -6.39721 | -53.35763 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a516dc1-9397-343e-a04d-4c5f5616deff | -4.30902 | -48.09693 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6c16caa-7997-3349-91e3-21219b678236 | -4.30191 | -48.09595 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fe2f9f5-c2d2-3abe-9444-9cf378515a23 | -6.54285 | -56.19618 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b4877c3-af5b-3ba2-a40d-e43cafcd1e16 | -6.39782 | -53.35156 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8916a43c-70a3-31e9-b5a9-fb59b7614f64 | -4.11479 | -47.92762 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fe3ea23-1765-3347-85bf-cef0ba38613e | -6.40292 | -53.35522 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee214392-c3fc-3834-bf0d-4823f32693c1 | -3.22029 | -48.81614 | 2025-07-28 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e97beff4-0f19-39f8-b9e5-e6aba8983e1e | -6.40307 | -53.35234 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deee3914-dfe5-3af4-89d8-c57c572d9e0d | -4.10955 | -47.9401 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 738b0753-42ab-37cb-b2f3-5129d23f8881 | -6.40263 | -53.35557 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12111215-4e50-315a-a178-c387c520b94f | -4.30094 | -48.10286 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6002b8b6-3dc4-3197-bca7-d9a2aecfe5a0 | -6.89041 | -52.86901 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7791d841-73ee-3652-acf4-5bddd69bd79a | -6.39738 | -53.35475 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f908928-b8fe-3eb1-952a-fe330c790d41 | -6.50028 | -56.21531 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12041aeb-81d4-3c81-add4-bd688a07e11e | -6.54347 | -56.19201 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcbf0f69-58a3-3fd8-b91d-823dad5d79b1 | -6.39813 | -53.35124 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4725dffb-f2f7-3485-a92d-fbab52cbefe5 | -6.49225 | -56.20989 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c8cea7f-338d-3d3c-8913-5617291e7b52 | -6.40199 | -53.36164 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d1d42b9-25fc-3d83-bdf4-3463707aaaab | -6.40246 | -53.35843 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dcc9345-c172-3f53-a082-b5238674edd9 | -6.39767 | -53.35443 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f49c0892-538a-3b88-a994-d83247781ec9 | -6.89585 | -52.87 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 912dda2f-398f-3fb5-b88e-c5d9e30dc74e | -4.30359 | -48.10527 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fa155166-800c-3216-a637-3c6251f9892e | -6.49777 | -56.20228 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f184e5b-0f6f-30a1-b01f-5a25e54b68ba | -4.11373 | -47.93512 | 2025-07-28 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 558c879c-df68-3e49-9c34-d92da22ec2eb | -6.49837 | -56.19818 | 2025-07-28 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 522dcf7b-687f-35da-b6c8-32611910f817 | -6.40153 | -53.36483 | 2025-07-28 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 628c6d7d-e206-3dab-af7d-b9bc2d7600d2 | -4.30805 | -48.10384 | 2025-07-28 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b173a23e-f879-39f8-8ac0-7e4326ddd86f | -6.90132 | -52.87077 | 2025-07-28 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3373ee66-b9dd-3494-bcfd-b29d8c2fa1f6 | -10.02365 | -67.74062 | 2025-07-28 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a915233-44c7-386e-a9a9-5245ebec9d2e | -10.0375 | -59.10445 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 904a5478-8efd-3e1a-bab0-eff2b01b3fb4 | -9.27418 | -60.77457 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b427d2e-b1bb-3ec2-8b50-fd0c4270eddb | -7.94052 | -63.61909 | 2025-07-28 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e3ed2c9-63f0-3225-a207-013d9dd39fbe | -10.04128 | -59.105 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86e4db55-49bc-3beb-b2c5-33d37258d93f | -11.87537 | -55.44986 | 2025-07-28 05:29:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ea7d43-ccbb-3bae-ac4f-e380cb83ef45 | -9.2736 | -60.77836 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbef034d-26d3-3307-a67e-f1def2b5a97b | -9.03009 | -64.01337 | 2025-07-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dc94322-aa29-3f07-8e6c-63c484271a55 | -9.02953 | -64.01691 | 2025-07-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
