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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f91e81a-61f4-3337-87b7-5ee394ba2fc2 | -16.34448 | -48.92593 | 2026-08-28 17:43:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b86a2aa-e253-3e62-8a8e-488c36d811fb | -15.37222 | -52.68278 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 112072ba-db1a-3a69-93ab-7ac6beb613df | -18.12237 | -51.60994 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 64a457f0-12d0-3304-9449-08e3a776e157 | -17.98427 | -50.18622 | 2026-08-28 17:43:00 | NOAA-20 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e15c741-961c-3d06-a37c-32c3f97dd8e7 | -15.72891 | -51.18366 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 93577db0-7bea-3f5c-b5d8-f7b9423bb36c | -22.64134 | -52.4346 | 2026-08-28 17:43:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 50a97b70-184f-320e-ab8f-e9067f60aa3c | -20.68518 | -50.47978 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| b2d8bdca-e34a-3c5c-bf89-d9099e13f101 | -15.73975 | -51.18175 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b9b9ffbd-0c1d-3d4a-bcfe-8f2cfedc24df | -19.06611 | -57.40068 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 6dad3db9-a8e1-3c05-8fd3-35d960cd0bed | -19.06967 | -57.40001 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 59471aa1-791f-37e0-ba97-3053b00da501 | -16.15936 | -58.57796 | 2026-08-28 17:43:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 873b8516-1248-31f0-a5e1-9b031a116953 | -18.10696 | -51.61278 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 3d0007bd-a4d1-38c5-bfb7-d979f4cb4211 | -15.35769 | -53.79401 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 871012a8-7fab-320e-8aa7-9dc95422ac55 | -19.23687 | -57.65516 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ff9a9600-00ac-35f8-9786-ac74e6fbdea5 | -20.6808 | -50.4864 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f6ac44e5-12cf-3af9-8b0d-758d11c1aaaa | -21.04949 | -57.84279 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6f767ad1-afdc-306c-8eac-a9f78641a4fb | -21.64304 | -49.74475 | 2026-08-28 17:43:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8d9e883d-ab66-3e10-a716-ef7e212c06ec | -14.60253 | -47.96809 | 2026-08-28 17:43:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ccd0a075-60ca-346b-8175-7c2c3738f675 | -15.3808 | -53.8774 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9da667f9-bb2f-3057-b638-7c70ec51fd11 | -19.06361 | -57.40001 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 635f15c4-ece7-389f-be72-a0adfa67aee5 | -17.3072 | -46.57767 | 2026-08-28 17:43:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b0743157-d0f3-3530-99c6-0b21ada693dd | -20.32483 | -46.59167 | 2026-08-28 17:43:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 17e81a5a-8692-3270-887e-1a9e4ae83c02 | -17.59595 | -51.64373 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 8fd044d0-2047-385c-a67c-4a8f224fa25f | -20.90254 | -57.59211 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 61a46a4e-d05d-3c37-b6d9-c113e8d5fbc6 | -19.06718 | -57.39933 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| e92e586f-01b0-3722-8a74-3e58346bf3ca | -14.49592 | -49.11374 | 2026-08-28 17:43:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 63709633-b05f-3cdc-815c-2a40844865d4 | -15.13159 | -52.83063 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8fc27888-beee-342c-8a40-946850dad697 | -15.72725 | -51.1767 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 16ec0d3d-502c-3e34-9be5-e4ee1736f78e | -19.22914 | -57.6524 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 7bd0eb2a-11a7-3dc1-952e-405dc06dcfc1 | -15.38545 | -53.87654 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 680a5e84-d81e-3166-aa62-4f6b06d9b0dc | -20.6918 | -50.48526 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 1150d569-88af-307b-9ec2-aa934b20980a | -20.69038 | -50.48021 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 6de232ea-b7c8-3750-be2d-e3e78531c67b | -16.56318 | -49.38208 | 2026-08-28 17:43:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e5eeef32-a4b3-3d70-81cc-9d0e8a707bb8 | -15.9028 | -56.23613 | 2026-08-28 17:43:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 488c8c07-65c9-3d3c-af4d-aad7db42b685 | -15.37602 | -52.68056 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e3565bce-baf3-352c-b2af-234fb2c835a9 | -15.73826 | -51.17453 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 616ba3cc-a02f-327d-94b1-58bbc6b5701a | -17.60561 | -51.63843 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 10f76161-81c4-3740-ac2b-aeb61c28b4e5 | -19.232 | -57.66912 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e4039b3a-fbf9-32a5-adc0-e2bcf1714073 | -16.5853 | -49.78564 | 2026-08-28 17:43:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c9345ca-d347-33c0-95e1-d001c5084d3e | -14.33912 | -47.24335 | 2026-08-28 17:43:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 57391b28-60ba-37a2-9509-c076f757b420 | -22.21471 | -56.06666 | 2026-08-28 17:43:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a116bd43-1fb3-3898-bafe-6853a9f06a59 | -20.90078 | -51.54686 | 2026-08-28 17:43:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 5d50e8d7-50c4-3fd3-adb9-d75cefbcc162 | -17.59007 | -51.64122 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 494da91a-26eb-3529-b1c2-05a99256cd94 | -14.94672 | -49.03896 | 2026-08-28 17:43:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d10050d0-dd3f-3fc5-8c30-b3fa881ba6d5 | -17.56122 | -51.11091 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5607427e-dc59-3de9-bb07-9983458a0d27 | -22.10453 | -51.25622 | 2026-08-28 17:43:00 | NOAA-20 | INDIANA | SÃO PAULO | Brasil | 3520608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 79500564-8e84-3998-ac65-7b4d956f4779 | -15.72827 | -50.72973 | 2026-08-28 17:43:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70f199c6-08bb-3d50-9bdf-c96811cb850c | -20.69108 | -50.48185 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 4e056636-dde6-38ff-bf89-0d587cf8dc07 | -14.33472 | -47.23912 | 2026-08-28 17:43:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 75a9e0f8-70e3-3d5a-9f98-3b80c7a24f72 | -15.73351 | -51.17924 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e4509d18-2b80-39a0-95e8-e04758edcd17 | -16.86723 | -50.49865 | 2026-08-28 17:43:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| aedf99b4-03bd-3c0c-85ed-b503b467032c | -21.07907 | -56.62317 | 2026-08-28 17:43:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 78f4e6b5-e5aa-34a0-8b47-35b2e7c6c564 | -20.23481 | -49.19302 | 2026-08-28 17:43:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5add28c8-b4c7-31e7-a163-8b0ca2837196 | -15.73369 | -51.17892 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 411551d6-b490-39dc-ad51-1d2391d99fb0 | -20.82045 | -57.3191 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c4f78763-ba1e-359c-a2bf-1c6d2d3d0ff0 | -20.69631 | -50.48229 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 710efa2d-0156-3877-b588-d13a6b97858b | -21.30333 | -50.5653 | 2026-08-28 17:43:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 51e8b71e-8ac6-3d41-b86f-80616e70812e | -19.22986 | -57.65659 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| eeb80dc9-1d74-365e-bd83-c4ecb64d7f6b | -15.35969 | -52.83321 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 306c16bc-cb84-3395-84b2-f27156579ea4 | -18.12305 | -51.6132 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a22c13f4-a7ca-3a93-9429-d96d2c57889a | -22.21107 | -56.06739 | 2026-08-28 17:43:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f6cd6a8-95ee-3ecb-9232-ab67283aa792 | -15.38506 | -52.93762 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a4a72882-878a-34cf-983e-f503842cf652 | -16.86645 | -50.49489 | 2026-08-28 17:43:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bbd7ece2-c4f8-3955-a59c-aea7b27cc258 | -15.73296 | -51.1753 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3f4c89b7-7430-36a6-9065-248e6e584fbe | -16.57944 | -49.78707 | 2026-08-28 17:43:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1adf1fe4-a3f0-3883-822e-dc4accd31b87 | -22.08633 | -55.97699 | 2026-08-28 17:43:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8b2f5c99-2f97-3497-a41a-cf739e15488b | -19.22293 | -57.6584 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 521c7a40-28e5-3d0e-965d-72cd689635dc | -19.2278 | -57.66578 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 00df82c5-7bd9-3dd6-9403-cb78d027b034 | -15.48061 | -53.95809 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ed1872dc-7db2-3a4a-b5b2-02a8efded431 | -20.46946 | -48.78112 | 2026-08-28 17:43:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 968382cf-60fd-3e04-bc15-fa91670ed46b | -20.68966 | -50.47684 | 2026-08-28 17:43:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 8f08d078-fa60-3e99-b1d1-b418b621f731 | -20.9295 | -57.60375 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 42dbcbe3-1390-37f2-af0c-f46d44201cd2 | -21.0413 | -57.83611 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| fc8dd5e0-6937-3361-977c-f4a9d1c067d9 | -15.43663 | -52.90789 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c866a2c4-3686-38c4-9627-1e151cc14ed7 | -20.22912 | -49.19429 | 2026-08-28 17:43:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1117a861-87e5-3b26-bb48-f2c1263afe62 | -17.30532 | -46.57764 | 2026-08-28 17:43:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 692b3832-1d46-3093-bf72-eab6827ee1e1 | -19.23129 | -57.66495 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a3b0bb5f-f8f6-3922-949b-b40e142dab36 | -21.54078 | -55.833 | 2026-08-28 17:43:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4196fab7-5c84-30fd-86a6-93274823d8ec | -18.35726 | -54.98683 | 2026-08-28 17:43:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| f4d3f2ee-3f6f-397c-aa32-def7d9c30549 | -20.69037 | -50.47846 | 2026-08-28 17:43:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| ef43d6ed-fe34-31eb-ab09-541ef7ed8b7d | -19.22434 | -57.66671 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a28d83d7-2ebd-3246-ae6f-aa1c567f23ea | -15.73425 | -51.18286 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 72a83bfe-4c53-3f29-a97d-600e4bba5d42 | -18.11721 | -51.61078 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 86c98884-cceb-3978-86e5-f0a583ca0524 | -18.11273 | -51.61491 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 839ed90d-39f9-3fee-9e9b-7e808cf2056f | -16.12697 | -55.87054 | 2026-08-28 17:43:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 2affa0ef-697e-3443-9bc7-626b150b80b5 | -17.55355 | -51.11467 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3100bdfa-60d4-35be-9551-4a86f34ecb39 | -16.16702 | -58.58076 | 2026-08-28 17:43:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ae2ed98c-6fa0-3542-b5c9-7e4b24dfe749 | -16.7972 | -50.01887 | 2026-08-28 17:43:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17e2853b-ce9a-3bbb-85b4-7d18faee36de | -15.35358 | -52.8284 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1dd58760-2d11-31ea-a542-d4ad134aa37f | -17.98903 | -50.18104 | 2026-08-28 17:43:00 | NOAA-20 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b22eece-07da-37cc-974c-1f635aedcd8c | -19.22364 | -57.6627 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7d21a7dc-570d-3a80-8eb6-ee40f3e2fb48 | -19.22215 | -57.6539 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7153a8c0-9395-377d-852c-fdfdf0a9f82b | -19.22362 | -57.66246 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| eb300ab8-9666-3c33-88f3-20261cf0b2dc | -20.69113 | -50.48362 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 8707a734-62f5-35fd-90b3-6f731a489c6d | -20.68521 | -50.48156 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f2bad914-4484-3481-bd6a-df20bc744a3a | -15.37987 | -52.67364 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 869556a7-4bfc-3421-a3ba-a50e27761210 | -20.68597 | -50.48503 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 861ecd68-58b9-3ee3-8d14-6fde252c6c01 | -20.90213 | -50.24717 | 2026-08-28 17:43:00 | NOAA-20 | LOURDES | SÃO PAULO | Brasil | 3527256 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7b8bde77-64b0-328c-b705-0ac851a9e1cc | -18.12101 | -51.60334 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ca2d2ef1-c3e4-36f9-b4d8-add11e9a6d9e | -15.38555 | -52.67591 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README137.md)
