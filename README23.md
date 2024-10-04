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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51b507d5-0797-31c0-8d3f-7a39d6de255d | -18.85711 | -43.59848 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 788ec79e-b723-30e1-aa9b-bd5c086d5032 | -18.85528 | -43.60956 | 2024-10-04 01:07:00 | TERRA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 7b92c56d-e630-3e3a-b406-076e75f77a55 | -18.85404 | -43.58002 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| b1b1bd0a-4fa4-36af-b80a-cd3c16a510b8 | -18.85248 | -43.59349 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| 09f15bd8-8ebc-301c-923e-5058e28870bd | -18.84901 | -43.5737 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| d213fcb5-bcd4-38c0-a4a2-4f8ae7135dfd | -20.52556 | -44.90155 | 2024-10-04 01:07:00 | TERRA_M-M | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c65b9d4b-1257-32fe-823c-0fb1300edb28 | -20.51532 | -44.90357 | 2024-10-04 01:07:00 | TERRA_M-M | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 056b649f-b308-364c-af5e-6e7c5726e513 | -20.4915 | -44.04461 | 2024-10-04 01:07:00 | TERRA_M-M | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0684e8b3-fe58-3e82-b6ab-3f04ce56b473 | -20.48893 | -44.02969 | 2024-10-04 01:07:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| a6a12382-0e2b-3483-af32-6384145b0f0f | -20.48757 | -44.03642 | 2024-10-04 01:07:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 7c033081-ff37-31d0-83d7-d23ee6acfe34 | -20.42302 | -43.78587 | 2024-10-04 01:07:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| 6a5d4650-7989-3b0e-8c10-7103e98c6ee5 | -20.42037 | -43.77016 | 2024-10-04 01:07:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 799211f4-5c5e-3dac-ae3c-d92a5331b995 | -20.34074 | -43.57555 | 2024-10-04 01:07:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 06f30815-8094-3afb-afc2-29c8383bc370 | -20.33791 | -43.55928 | 2024-10-04 01:07:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 60cfb245-7185-3c20-8415-a8c3cd98cff1 | -20.14639 | -43.85676 | 2024-10-04 01:07:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 30d37a92-53da-37e4-a60c-c97e29dbe518 | -20.13785 | -43.87408 | 2024-10-04 01:07:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| f0e1def3-9d4a-3d0b-8527-b9e9ee89ea0d | -20.1352 | -43.85848 | 2024-10-04 01:07:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.3 |
| 051db40f-03b3-33f7-a6a3-074ab63ddee7 | -20.13376 | -43.51649 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c87d63e5-1ca8-315f-8f76-c5121687a530 | -20.13257 | -43.843 | 2024-10-04 01:07:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| a9359f2c-2431-3169-975c-dffa083d2a19 | -20.12747 | -43.53808 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| f2d2c5e5-4c34-306d-8641-d9b8826314f5 | -20.12491 | -43.5332 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 3b8dde19-dd9b-32ee-9983-72b16fc9aa7c | -20.12485 | -43.52253 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 75fd0077-c72a-377c-a309-c3c620a3cf65 | -20.12217 | -43.5176 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 42b645aa-7e48-3e22-bb57-929852b81ed4 | -20.11351 | -43.52508 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.4 |
| 86c345a8-678f-3491-90f7-48a11c4ffe67 | -20.01379 | -44.49728 | 2024-10-04 01:07:00 | TERRA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5e1b1403-237e-36bd-999c-589eb40db8a4 | -19.96696 | -44.09014 | 2024-10-04 01:07:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 2638e2db-7be8-3098-89da-a97f5f47ea87 | -19.95601 | -44.09235 | 2024-10-04 01:07:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 36270caf-6b68-36d1-a321-81ddd20cdb0d | -19.90048 | -44.531 | 2024-10-04 01:07:00 | TERRA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ee2d69ad-7fa6-3c8b-a8ae-9c9dfe3c7a89 | -19.87776 | -44.59232 | 2024-10-04 01:07:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| bfeeb3ac-e458-37d2-9865-7719ca306420 | -19.75389 | -44.27139 | 2024-10-04 01:07:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0d1e5cab-b3a0-325f-98c8-2336651b5c2b | -21.31584 | -44.84306 | 2024-10-04 01:07:00 | TERRA_M-M | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 4982a087-c285-327c-8cca-ae9dcd5d75e8 | -20.76363 | -46.29511 | 2024-10-04 01:07:00 | TERRA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 159091a7-5a19-30bf-90a3-96edc7326096 | -20.50787 | -46.39849 | 2024-10-04 01:07:00 | TERRA_M-M | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5c4a686-3b19-3009-b93b-fdcc494228a9 | -19.60586 | -46.28458 | 2024-10-04 01:07:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d0b2902-d45a-3b25-abc9-98e3a13389ba | -19.60411 | -46.27335 | 2024-10-04 01:07:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 98030622-fa1e-3a01-93f9-a5808ed7d884 | -20.24014 | -45.95399 | 2024-10-04 01:07:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 93ecb958-8fc4-36ed-b911-e35cfecde24c | -21.44089 | -46.56754 | 2024-10-04 01:07:00 | TERRA_M-M | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 26e7f1dd-6738-367f-9ba6-d63207641872 | -21.75994 | -45.55469 | 2024-10-04 01:07:00 | TERRA_M-M | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| aff380a4-025b-3d69-b590-5e38ab4c127a | -17.60976 | -46.98233 | 2024-10-04 01:07:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9426bcd2-a5b3-31c5-9930-463337051fc3 | -17.60815 | -46.97169 | 2024-10-04 01:07:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7b79539b-80f2-3ad2-b9ff-1c7589c2ca30 | -17.53506 | -46.75005 | 2024-10-04 01:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 33913795-6e0f-3362-af97-7eeed4a13e51 | -17.53336 | -46.73908 | 2024-10-04 01:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3ac7de47-1941-3021-ab2e-3b2e6d7bb7ec | -17.49399 | -47.01847 | 2024-10-04 01:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ab14fd60-6104-394d-abfd-4efb11de6659 | -18.802 | -46.64806 | 2024-10-04 01:07:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37caab74-db00-34e9-907a-96d819b5ffb2 | -18.80033 | -46.63732 | 2024-10-04 01:07:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c652fa30-c8a2-31f9-91ec-398cbc7df086 | -18.79252 | -46.64971 | 2024-10-04 01:07:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b5d892a-5fa2-319b-95d2-dbc88227a981 | -18.79086 | -46.63904 | 2024-10-04 01:07:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5b2c434a-32cc-3bf9-9bfc-cc5ea733fc76 | -20.7245 | -46.89986 | 2024-10-04 01:07:00 | TERRA_M-M | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8bf440a5-79b5-30dc-b935-fc69c70e5ac4 | -20.31113 | -47.21928 | 2024-10-04 01:07:00 | TERRA_M-M | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dc53dc2-5285-3a6f-8921-4974584573e5 | -20.27033 | -46.8835 | 2024-10-04 01:07:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 643927b5-e9b9-3328-acf8-b52980d8c22b | -20.19089 | -47.46503 | 2024-10-04 01:07:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0801ca99-6d24-3226-9911-529b3df93d84 | -22.42808 | -47.57497 | 2024-10-04 01:07:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 069f2734-7225-383b-8784-c90f44808a90 | -22.36921 | -47.93604 | 2024-10-04 01:07:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 911cbf65-620e-39e5-be69-d45083f2e5b4 | -22.19224 | -47.59782 | 2024-10-04 01:07:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2227e7d2-cff0-3db3-a6db-ab5ba1b8072e | -22.18473 | -47.60904 | 2024-10-04 01:07:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 97ea8690-43b4-3ba5-9a25-d3fac702e5eb | -22.18334 | -47.59942 | 2024-10-04 01:07:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9c36553d-c800-34a1-937a-47fd815ac8a7 | -22.07963 | -48.4963 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5cf9f977-9f67-35ae-a3ae-f2185cf7b5f2 | -22.07831 | -48.48678 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b9975aa3-ad3b-3594-abba-5233bd120eff | -22.07077 | -48.49776 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8189414-f175-390c-9941-6e20ff5737a9 | -22.06944 | -48.48824 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68c2e12f-042b-38d1-bafa-81aab717d3ee | -21.92138 | -48.41133 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 19aefb5f-9224-31ff-ad4f-c6daf969a81e | -21.8929 | -48.41266 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 905a3fdc-633a-3e1f-ba4c-34deb8e4ffb6 | -21.88537 | -48.42361 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 846e367c-a2a2-3427-b97d-8bac99762b04 | -21.88404 | -48.41411 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6daa35d5-820c-397b-878a-53f171a01065 | -21.85966 | -48.36951 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97449cc9-8766-32b9-b779-982bae9cced1 | -21.8508 | -48.37097 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ee647e82-15ef-3cdf-af97-d1c5bad0226b | -21.84991 | -48.42943 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| ff55dc48-e5bf-39ca-9e1e-16f1eac65287 | -21.84859 | -48.41993 | 2024-10-04 01:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 777d2da8-ca1d-3c7c-8bfd-a904ec702983 | -21.8446 | -48.39143 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f76c9630-6a3a-3eaa-8f25-b39bf40a47d4 | -21.84371 | -48.44989 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 8ad15a72-df48-354d-a738-ddf5250dbc60 | -21.84238 | -48.44039 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 82e0eb66-ee70-37d5-a363-06200b213e31 | -21.84105 | -48.43089 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e9d4ed2c-bae6-3c27-b367-938483e9c50d | -21.83617 | -48.46084 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7d38366b-a9f5-3ed2-a119-b85d6119f03f | -21.83484 | -48.45134 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9dedd4d0-9ead-3825-89cc-1572836befc7 | -21.8344 | -48.38339 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e31b24d1-fa8f-30b7-bc9e-8d40ecb4af9d | -21.83307 | -48.3739 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 25.2 |
| dc0d4ddb-6b88-3ad2-8677-14735c75fe3c | -21.82466 | -48.4433 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bca6cf61-a7d2-3c33-a3f6-04c64c1d54a7 | -21.82333 | -48.4338 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 19994baf-0a7b-3651-b27e-e71cfc5c76ab | -21.81401 | -48.36732 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 37.2 |
| bf74ade3-f78b-389b-93b6-42f6a3161fd3 | -21.81395 | -48.44122 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d54eaeba-1d81-30a5-8115-f19bf83ac1e2 | -21.80864 | -48.40323 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6dd7924d-bff5-38fa-adb4-045bc049dc3f | -21.8073 | -48.39374 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 64465f2c-bfa1-36b8-984b-3e5755661e4a | -21.80641 | -48.45218 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 370b4221-2dd1-3b8b-854c-755613c1dca7 | -21.80597 | -48.38425 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5551fbbe-689d-3e74-8861-28c1d1ff4c1a | -21.80509 | -48.44268 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3cd14b1f-9e67-32fb-a719-6bee61f4db44 | -21.80464 | -48.37475 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 78203705-6dcc-3173-91f6-4453b6b8145e | -21.80331 | -48.36525 | 2024-10-04 01:07:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 20c4b04a-dfa2-3ffb-bb88-6157290a5c9e | -21.79844 | -48.3952 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 736b2e26-f49a-333b-924f-b6457532b4a5 | -21.79755 | -48.45363 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4f120572-456e-3ee0-8684-d694ad50fb47 | -21.79711 | -48.3857 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e3729786-c80c-33ce-b0e8-743afaa5f4b0 | -21.79622 | -48.44413 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1aae88f1-843a-34bb-9b91-d78e803c904b | -21.79578 | -48.37621 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ad7ceab3-b1ad-3621-9bb8-30f5fcb305af | -21.78825 | -48.38716 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f364d202-7d1e-34ca-802a-7d86f753cc5d | -21.78692 | -48.37767 | 2024-10-04 01:07:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52780a5a-e860-331b-be6b-38a81caeb460 | -21.75986 | -48.50835 | 2024-10-04 01:07:00 | TERRA_M-M | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f34f0cfd-a890-3c48-a945-4e8102a70ded | -21.7139 | -47.04182 | 2024-10-04 01:07:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed065c3d-15fa-3dc2-97b4-1e3b3331d91c | -21.30157 | -47.62223 | 2024-10-04 01:07:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1caa17cc-17bc-3524-af35-2f550bb45722 | -21.30018 | -47.61265 | 2024-10-04 01:07:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e851f4f-c5c7-31dc-a890-5d58ad226dc3 | -22.39217 | -47.89662 | 2024-10-04 01:07:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c58af3c7-8a07-3980-a6b5-0c40b38a659b | -17.68787 | -48.57616 | 2024-10-04 01:07:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README24.md)
