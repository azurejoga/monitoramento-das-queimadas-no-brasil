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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e5f707-2536-36a6-9902-1505127ba7f1 | -15.88625 | -43.46627 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a89df623-3166-32ea-9761-b16a0b4863be | -17.22866 | -54.44129 | 2024-11-27 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fdd6d105-1f47-3db8-bf5b-b3681a1bc49e | -20.85383 | -49.87443 | 2024-11-27 04:46:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae9b15b0-82eb-390f-99ba-e8b512b767a8 | -15.89208 | -43.4634 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| febebd0b-8dd9-3c44-9dbc-bf956b8ac77d | -20.1571 | -48.91872 | 2024-11-27 04:46:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d59d8a1-182c-38d2-b2e9-3012a9fb2b39 | -20.76531 | -46.77129 | 2024-11-27 04:46:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a13a26d2-5f54-395f-8ba5-0cccd24cf648 | -16.88683 | -57.51364 | 2024-11-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3668c999-5119-3a12-a799-1c32db21e076 | -16.68235 | -43.88623 | 2024-11-27 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 383e898f-7962-3c0c-94fd-64972ee9b09d | -18.30203 | -50.90088 | 2024-11-27 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ecf7f5c-3a99-3077-bb6d-696d461c02ab | -15.89247 | -43.45984 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7764f5c3-db09-3f62-8f66-fbf0aa339724 | -17.22533 | -54.44069 | 2024-11-27 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2ec3393-5ee4-3203-b8bd-8906a5b26bf8 | -20.38674 | -47.47865 | 2024-11-27 04:46:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d617f1cd-be73-3fe2-964f-9bedeca89887 | -16.67476 | -47.24401 | 2024-11-27 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c85e226-62fb-3d67-9b66-927ca756ff62 | -15.29277 | -56.52831 | 2024-11-27 04:46:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29bf8bde-c9a7-3533-b8ab-963f53b5645c | -15.88503 | -43.46662 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9384101b-3fcb-38dd-96cd-92e8eb475a06 | -16.34632 | -43.69756 | 2024-11-27 04:46:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9f881aa-dc1b-3be2-8ff8-213d4b4e105b | -17.56696 | -57.47638 | 2024-11-27 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b6ab4b8c-5eec-39a2-9c31-7e5f386a3a56 | -17.63486 | -52.90501 | 2024-11-27 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e282bb-4e1c-33d4-8877-81e4b31f3043 | -18.03755 | -52.19382 | 2024-11-27 04:46:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33199963-5044-39f7-8d1f-a4d7a21e3f1d | -20.38622 | -47.4831 | 2024-11-27 04:46:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5ee4211-4779-3ba7-bceb-ea0c257a21ae | -15.28987 | -56.52329 | 2024-11-27 04:46:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b44de3-8943-3a32-ac0c-5d0ef2f22afb | -18.01214 | -54.00811 | 2024-11-27 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e20326c-21ef-35aa-9596-423be89959f0 | -15.88664 | -43.4627 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a9315d76-57a5-3b01-b9ee-3e3687aed4c5 | -17.56324 | -57.47566 | 2024-11-27 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12a24472-8bf9-35c6-9ecd-0189f8f71c9d | -15.88545 | -43.46305 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0c3df89-d8e4-3b2e-9f34-d3332151296c | -18.29849 | -50.9003 | 2024-11-27 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c515cb2c-1e7a-317e-b966-49113ecc2fd4 | -19.27338 | -51.46982 | 2024-11-27 04:46:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f328c7b-df8c-37f2-8eeb-2817eb86fb55 | -18.67888 | -50.73381 | 2024-11-27 04:46:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| eb3cae34-17da-375e-b7f8-88e24a736937 | -16.67528 | -47.23994 | 2024-11-27 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd7b2acf-38e0-3756-b5a6-fd769667aca7 | -21.19667 | -44.93721 | 2024-11-27 04:46:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8a1d8b5-8691-345c-9bfe-0260f14a7a68 | -16.88734 | -57.51016 | 2024-11-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e54e4a09-9939-30f8-a9c0-7192bea6ff11 | -16.16147 | -59.61351 | 2024-11-27 04:46:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c316755-ff34-3f33-8d71-1e41a9ff8b6c | -14.72183 | -57.76686 | 2024-11-27 04:46:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da2bd4d-e066-3109-b6d9-10779e81f964 | -18.01603 | -54.00507 | 2024-11-27 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 260e03bf-2bee-35a0-ba82-5cec3f0bafa8 | -17.77874 | -42.81367 | 2024-11-27 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89c47c5a-b105-3f9e-899e-d395a9fdea97 | -17.70017 | -54.08819 | 2024-11-27 04:46:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08b33eef-85d4-3f58-b466-c4c289f73c42 | -20.38283 | -47.4736 | 2024-11-27 04:46:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a88274-c651-3d1a-ad13-04c16d3f42cd | -16.16227 | -59.60918 | 2024-11-27 04:46:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab64c24b-642b-3f78-89ac-d52529156f5b | -16.67956 | -47.24051 | 2024-11-27 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddb23919-4a5f-30a2-9210-fd7ad53577b3 | -20.97585 | -47.21258 | 2024-11-27 04:46:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd8aade1-6731-3e5f-8c67-06a02f4ec446 | -16.88648 | -57.5149 | 2024-11-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bbbccbff-4b82-3fff-9262-61ce54503134 | -17.70407 | -54.08514 | 2024-11-27 04:46:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 748bbaa2-e196-3b92-9522-a11bd0687bf2 | -15.8913 | -43.46017 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7855c2cb-45c9-38db-a092-3544388e7673 | -18.01545 | -54.00869 | 2024-11-27 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94abfeec-f78f-3504-b966-14efe350cd11 | -17.70075 | -54.08456 | 2024-11-27 04:46:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3468e2fb-c2bb-3a1c-9d2f-f453e59cb9e1 | -17.77902 | -42.81038 | 2024-11-27 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d05d33c-2f20-30ce-8641-dbc04c011304 | -18.01271 | -54.00449 | 2024-11-27 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 479e3524-7e4e-3414-8ef1-4439918036ad | -22.11569 | -49.61435 | 2024-11-27 04:48:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b6738776-1c87-35d7-a7db-8894522d3b50 | -22.53925 | -48.81311 | 2024-11-27 04:48:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0af1e51a-aa8e-3093-bbac-5a3c28269490 | -22.10778 | -49.61311 | 2024-11-27 04:48:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 91bd178d-1e9c-3982-a2ce-68b86f5ddd3b | -21.60601 | -57.49443 | 2024-11-27 04:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d62c693-d805-3240-8430-a5417e79efc2 | -22.98677 | -50.39897 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 77632d12-b466-375f-a5a4-505546967649 | -22.97913 | -50.39767 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 397a4189-4110-3f81-b4ed-13f3587be375 | -25.06233 | -51.1512 | 2024-11-27 04:48:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5cac6139-a14c-3091-89e4-5209a9632863 | -24.4493 | -49.80314 | 2024-11-27 04:48:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 88f18359-589b-3bee-a0d7-faa58908c9f0 | -22.98102 | -50.39973 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 43807036-c1fd-3c03-86ed-fcf98eefad8b | -22.98484 | -50.40039 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 7e08b3d0-2509-3d40-a7a6-8584802db1c8 | -25.06171 | -51.15607 | 2024-11-27 04:48:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab437ae8-4c37-384c-a645-145b08efd2e1 | -23.36314 | -47.04898 | 2024-11-27 04:48:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 07b62cea-7293-31f4-b2a5-3b9a707f0f0f | -22.53979 | -48.81487 | 2024-11-27 04:48:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 844452e1-a7fe-34ea-8b4c-7da301544867 | -25.13824 | -52.14457 | 2024-11-27 04:48:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4e7edea2-e1f1-3164-bfc9-e2a73b0e0623 | -21.60524 | -57.49881 | 2024-11-27 04:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad44579e-a6e0-343d-a8d6-ad4a0c687377 | -21.34091 | -53.37523 | 2024-11-27 04:48:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abda2531-4e57-3055-a9dc-b68da013860b | -21.6108 | -54.61773 | 2024-11-27 04:48:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb7a879d-1a2e-36e7-bd1b-6f9fb78a5a10 | -23.77284 | -54.48621 | 2024-11-27 04:48:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7fb5856-345c-3c3d-ad8b-bfc35e896e20 | -22.11487 | -49.61044 | 2024-11-27 04:48:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 542f6d6b-6c39-3118-aabf-ca4eeb81a8ef | -21.44535 | -48.70187 | 2024-11-27 04:48:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f94ba4-215a-3274-9c40-8a53b51243e5 | -21.31538 | -55.95292 | 2024-11-27 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cf2d25b-fae6-3458-9553-212bed453644 | -24.71476 | -53.0803 | 2024-11-27 04:48:00 | NOAA-20 | IGUATU | PARANÁ | Brasil | 4110052 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb4fad90-07e0-3b6e-bfaf-818a2deb0b7a | -21.34148 | -53.37145 | 2024-11-27 04:48:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b36415a8-d041-3ff8-813c-ef8cc309b1cf | -22.13946 | -50.86314 | 2024-11-27 04:48:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6badd56-77ac-30e0-8957-115e270dcee8 | -22.98295 | -50.39832 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 40caddce-e3dc-3ca4-b92e-22ea1ddcebee | -22.98228 | -50.40339 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 1ff51443-eb88-3ee1-86cd-f8802d4e532f | -21.31876 | -55.95354 | 2024-11-27 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23192267-a6ba-3d2d-83c3-1c17200e5d84 | -21.48959 | -46.02921 | 2024-11-27 04:48:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c41fce9c-338e-315b-b72c-3b9c50f99255 | -23.43533 | -51.43664 | 2024-11-27 04:48:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f392a7b-6f1b-3fc9-a1f3-accc9fa50eab | -23.36254 | -47.05453 | 2024-11-27 04:48:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 72c307f2-d83b-3e07-9376-a668dcbcae59 | -23.77617 | -54.4868 | 2024-11-27 04:48:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae2144ae-a8b9-300c-b76f-bd402dad5d43 | -22.10383 | -49.61245 | 2024-11-27 04:48:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d8a422a6-a0bf-3ec6-bf54-37a49b2393a3 | -22.11641 | -49.60877 | 2024-11-27 04:48:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a731741-ed64-3e36-bfc0-0656b1f0e15d | -22.98039 | -50.4048 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| ea0ebe38-27eb-3bcf-81af-a415ebe67c92 | -24.7182 | -53.0809 | 2024-11-27 04:48:00 | NOAA-20 | IGUATU | PARANÁ | Brasil | 4110052 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fad3b08e-7323-3f40-b338-fbe8a7b019f5 | -22.97846 | -50.40274 | 2024-11-27 04:48:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 250ce63a-e269-3b02-b791-c7dc30303409 | -2.8347 | -54.1125 | 2024-11-27 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 979a2c05-4f7b-3fdb-97b1-3f2c677f8b33 | -2.9428 | -54.7904 | 2024-11-27 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 14b56013-88b2-3f8a-8e47-4a509b34f13b | -3.0393 | -48.5082 | 2024-11-27 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0123efb5-400b-3f55-8230-a92cedecc090 | -4.2114 | -50.899 | 2024-11-27 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f6538cbd-faee-3a4c-a1c5-972e0fad0d88 | -4.23 | -50.8774 | 2024-11-27 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2706eb15-61f5-37ab-be85-5f44a0e41ce7 | -2.8346 | -54.1326 | 2024-11-27 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5d9a0100-8352-3d33-9614-fe004a55ab67 | -3.1876 | -48.4387 | 2024-11-27 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2fac61ce-c4ed-377b-a220-9dc36492a4b1 | -2.1928 | -53.7839 | 2024-11-27 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3f6a567d-6501-353c-9f18-166eb915f1bc | -3.9674 | -48.0851 | 2024-11-27 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b5b0b66b-fa1b-3516-a3b3-2b9f171b5239 | -4.2115 | -50.8782 | 2024-11-27 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3545aa3e-4b33-3bc3-88b9-4ce00ae04b0d | -3.1691 | -48.4394 | 2024-11-27 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| da748fd4-d81d-3d72-9a8e-affb93b91366 | -29.20371 | -51.89881 | 2024-11-27 04:50:00 | NOAA-20 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9a3f867-801f-34a7-8759-3cdbdc67061f | -22.9841 | -50.4019 | 2024-11-27 05:00:00 | GOES-16 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| 14c15f20-1d8c-3596-94d2-f9212edcf889 | -5.9788 | -45.3621 | 2024-11-27 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f432023a-bb13-3d99-b218-f51a059a58e3 | -2.1928 | -53.7839 | 2024-11-27 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c621920a-cc75-312d-9a7f-ece46e47ebfe | -3.1691 | -48.4394 | 2024-11-27 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| f13ba907-587d-3478-805e-364e66c5940a | -3.9674 | -48.0851 | 2024-11-27 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |


[Clique aqui para ver as próximas entradas](README75.md)
