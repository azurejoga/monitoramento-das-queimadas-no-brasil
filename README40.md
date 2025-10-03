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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b73eb2c-4f42-3a7a-91cf-d069fc5364d4 | -19.72463 | -45.91995 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 535af37e-5172-3cfc-a219-b27672e03a06 | -18.46286 | -39.7593 | 2025-10-03 03:47:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86fa915d-f3a8-333e-ae8a-50cf30232167 | -15.99299 | -50.90362 | 2025-10-03 03:47:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c9cf651-2048-3fe4-ac91-69021b1f0e68 | -17.62586 | -44.44364 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eec8b84f-1fe3-3f7a-93aa-ee9bd2dc8612 | -19.23387 | -43.71543 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c9b7524-2ff2-31dd-8653-3c68b937beb1 | -19.23316 | -43.71921 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3a238dc-9455-3fe7-a8ad-6f0dcb13c833 | -19.89735 | -44.50632 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e8549855-5169-3b3b-ad4a-020d1cd5c51f | -20.12949 | -44.0048 | 2025-10-03 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9ce2e160-ff9f-3097-9933-03bb59b109f5 | -19.28894 | -43.73536 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db740c48-3673-3187-8bde-31316a50c68b | -17.27349 | -49.01193 | 2025-10-03 03:47:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bdeec05-c108-36a4-a4a4-e1aced6ff708 | -19.86917 | -43.64785 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 05c4e8db-e1c9-3c6f-b973-154ad3b57c0e | -19.14588 | -41.49929 | 2025-10-03 03:47:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1a9fc67f-2f24-35c2-9462-e3609387e3df | -17.361 | -45.02039 | 2025-10-03 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2d6c7bc-11dd-3ffc-8a71-e0cae8f89ff1 | -20.38733 | -44.13201 | 2025-10-03 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 34894d99-2096-334b-91fb-fa70b172672c | -19.59687 | -43.84161 | 2025-10-03 03:47:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7485494c-7525-35e4-b603-51a085325f37 | -18.51687 | -44.04226 | 2025-10-03 03:47:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60eee32e-fa92-3c56-914e-9ff283bf4b03 | -17.62666 | -44.44207 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34945690-83c2-36eb-a5dc-f967c03ed04a | -16.05519 | -51.04457 | 2025-10-03 03:47:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af327d8f-926b-330e-9b1b-1f99a6290c18 | -19.9312 | -47.07135 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb5774b1-1f0b-3491-be0a-d6799bbfa36d | -18.3161 | -44.04097 | 2025-10-03 03:47:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab969bf7-a1cc-3a2c-86d2-965f213a8d45 | -19.23244 | -43.72302 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2be00c66-6a34-30b9-8681-df7176b1d814 | -20.62999 | -43.80394 | 2025-10-03 03:47:00 | NOAA-21 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69134f45-8e13-3335-9096-75307e1104f0 | -19.14152 | -41.50291 | 2025-10-03 03:47:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 76640d00-1c2c-3d23-b041-8c3139e9d4ae | -17.06508 | -46.62927 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73bac388-fce8-3489-abcd-4a462ab4b258 | -21.29781 | -42.02242 | 2025-10-03 03:47:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0445dc67-882a-322f-ae5f-42f418cb1d77 | -20.043 | -41.32751 | 2025-10-03 03:47:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 542c924f-feaf-3a77-9851-b53bb8ee5c8b | -15.75624 | -47.77227 | 2025-10-03 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c94eb50-1ab8-3519-a5a5-d6f3cdaf52ee | -20.61594 | -41.61286 | 2025-10-03 03:47:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c37ee680-4cc0-3f2e-882e-0a81845ad15c | -15.25207 | -50.13022 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3431a26c-1fee-3b42-aace-7783328ccb53 | -19.97164 | -41.65634 | 2025-10-03 03:47:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 496bc1d1-1aa1-3cee-a335-677a65238ee8 | -19.45994 | -43.65275 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17fbf7be-7205-3882-802a-67dd5040fca0 | -20.11907 | -44.37332 | 2025-10-03 03:47:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f07682dd-4477-3748-8071-90883f52ec12 | -20.13349 | -44.00592 | 2025-10-03 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 206c2db3-bb76-3e35-8fb7-3223570522db | -20.76142 | -44.56536 | 2025-10-03 03:47:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fac9078d-53b6-39aa-bd55-dbd1c97a749c | -17.70406 | -44.4393 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f798bc58-ea73-3a14-b0d2-8914c0c52905 | -19.9553 | -41.644 | 2025-10-03 03:47:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 34154211-9457-3e80-8ab0-d0ae2b55e83d | -20.08281 | -41.26617 | 2025-10-03 03:47:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d893c713-2085-356d-802d-4b0adaeae3b6 | -19.90124 | -44.50733 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8e3eadae-c0f5-36ad-821d-f5dfdf5cb39d | -19.73465 | -45.88858 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccb3055d-319b-3774-99d4-9ee244d23afd | -18.15848 | -46.1091 | 2025-10-03 03:47:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2804d73e-e911-35dc-b7aa-78713689292c | -19.72233 | -45.88305 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d9c183f-9764-3822-8bbb-02b75357ca7f | -15.25145 | -50.13113 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9ade40c2-bab1-39cd-8e17-ba135d086665 | -17.18844 | -47.01861 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24c9598d-1d97-3092-a601-91a24f13d9aa | -18.45588 | -45.07456 | 2025-10-03 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16539c4-92d1-34fd-89ac-1c71d36fb69e | -19.60165 | -43.83861 | 2025-10-03 03:47:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7862ebe5-67bf-3b23-95a4-a4bdb86afb8d | -15.24654 | -50.12265 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2e268d72-1e3e-3c27-b14f-eabb87b1111f | -18.97332 | -46.97175 | 2025-10-03 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12a3226c-edb5-3e02-84cb-80e16c865233 | -17.32055 | -49.37995 | 2025-10-03 03:47:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2186ddf4-3596-36de-bc88-c0590372b778 | -17.18329 | -47.01732 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8861c177-6970-30d9-96e6-b209ff0bff01 | -15.25321 | -50.12494 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 41dec134-1f2f-369a-8393-95bac59f97e4 | -20.00648 | -44.18748 | 2025-10-03 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 02ea3066-8ed2-35f9-aace-4ffb06129760 | -19.47274 | -43.65117 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b423a4-e083-3617-85e3-0790ad3e8673 | -16.26538 | -47.86304 | 2025-10-03 03:47:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebf25a75-8343-3004-b4fc-5bc7da6cf5f7 | -19.58988 | -45.90279 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41977579-45d6-37e2-bc78-aa14fa86bccd | -17.96322 | -44.39776 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebc031a6-76cc-389f-b7f6-359910f2ecaa | -19.7164 | -45.91301 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ce3f6dc-60fe-3f81-8c29-c4e75be41d89 | -16.36687 | -47.01419 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec8bd467-9ca3-3c13-a797-98c8f2c5aaa2 | -17.9122 | -43.93569 | 2025-10-03 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d755819-f9df-3ec1-849a-70b948761545 | -19.8376 | -42.29107 | 2025-10-03 03:47:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4889815c-1424-32f4-9d8c-17019518ffc6 | -19.14396 | -41.50061 | 2025-10-03 03:47:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3b70d7e4-ffa7-3cc3-91bd-7529f614fb0a | -20.44172 | -42.34468 | 2025-10-03 03:47:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cd6d659-131a-335f-925f-6de6965b4bf2 | -19.46064 | -43.64902 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1095f63a-9ae8-3704-a7d3-4ce28fdd8894 | -19.97861 | -43.71286 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f22d7d55-78e3-376f-9d55-209be37867e0 | -16.34695 | -47.11066 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 542a549a-7c2b-3b34-9342-87f48b62ab1d | -18.51273 | -44.04124 | 2025-10-03 03:47:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bee5342-c674-32ef-9454-22a7e01bf8df | -18.52387 | -45.0481 | 2025-10-03 03:47:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 988322e4-d6f4-3ff8-b07a-c97aafe46625 | -19.72789 | -45.87913 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 581bf368-84d4-37ba-a1b7-836ccb6f3beb | -19.72097 | -45.9142 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c7fad4c-6fbd-3cdf-91ad-db834d065895 | -20.13198 | -44.01382 | 2025-10-03 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c256a5a4-7411-3a70-ae9f-6a2e8743950a | -18.79525 | -43.74649 | 2025-10-03 03:47:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0804d7e-1fc5-3dc9-9226-c8b8a732f788 | -16.0717 | -51.0029 | 2025-10-03 03:47:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c6e0d019-1b06-3c03-9d5b-734a33ef6251 | -19.14053 | -43.6075 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 01963abd-dfc5-3489-ba83-63f62c21d8bd | -19.95281 | -46.08056 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f83931cd-6bea-347b-8aaf-db483ab9c5eb | -15.7618 | -47.77351 | 2025-10-03 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9d574ed-5e39-3473-af4c-b0603bb6dda2 | -17.96837 | -44.39433 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4457c444-469d-34e6-992e-844e52dcc7cb | -19.97087 | -41.66079 | 2025-10-03 03:47:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5acf67ec-f00b-33ca-9d56-21cf732a5200 | -19.21721 | -43.19437 | 2025-10-03 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a677153f-1669-33ff-a9c6-96e30d5db38f | -15.25382 | -50.12046 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3b6459fc-e3e6-381b-8c37-c4cdf7c692f8 | -19.4576 | -44.28928 | 2025-10-03 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3391820-1838-320b-9f3f-40658495e4fc | -19.93071 | -47.06956 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b8729ff-4555-33c7-a4d7-186628c07da1 | -19.90571 | -44.50824 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fb292b1c-1c7b-30d6-8548-fcae76aa4513 | -19.8921 | -44.191 | 2025-10-03 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc4b6bfb-579f-312f-8813-423748c0520c | -16.36159 | -47.01317 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93bd2eb3-8af1-3086-9fee-7b2e6120619d | -18.66306 | -46.58469 | 2025-10-03 03:47:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d59ba31a-3820-32bf-aff1-a2a9ce81cf98 | -17.18394 | -47.01413 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 580b7e30-9ca7-3218-bde1-78a9c8e97db8 | -17.78698 | -45.00223 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69d415dd-320b-372e-9b67-65371d8e011b | -18.68049 | -47.83431 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1bc8a58-0c2c-3d20-8b52-4d2c207c7642 | -18.68125 | -47.8308 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fa963f9-111c-37b7-a8f3-6fb63ee2c2a2 | -19.58424 | -45.90694 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4f0b94-2fcb-3868-994b-8f9316309057 | -19.14125 | -43.60365 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9971be26-e21a-3622-81f4-f910a9caa22d | -19.82385 | -46.83285 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd998e55-8336-3246-9fc5-aaace05e2e52 | -16.3476 | -47.10752 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c63f9d23-682c-3aa7-b009-469b5e05a192 | -16.06185 | -51.04632 | 2025-10-03 03:47:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93ed92b5-11cf-313e-a9b3-b87ec0e72092 | -17.59484 | -46.67826 | 2025-10-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6871751-060b-32d0-8e1b-efa4748e672a | -20.75974 | -44.56606 | 2025-10-03 03:47:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 562a0655-1e72-397e-a7c5-499e0e67217c | -20.18079 | -43.77881 | 2025-10-03 03:47:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 878c328c-2428-3892-a115-bd73ce192196 | -18.81843 | -47.4164 | 2025-10-03 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ae510e3-bb28-38ac-ac27-66180f3dd8b9 | -19.46873 | -43.6503 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c3547d6-4c19-3d58-8455-0b7602c2882f | -16.34895 | -47.10098 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce80877a-6b35-3274-9c80-5985f0d96165 | -17.18132 | -47.02699 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
