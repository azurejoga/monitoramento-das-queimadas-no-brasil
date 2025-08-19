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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38d3fb6-27e0-38fd-ad7b-7b4f68af0b79 | -13.18401 | -54.94638 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff3ccc4-9aca-30fe-9171-a738bb1d8d76 | -14.97246 | -54.80225 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e35073e-2292-36e5-8e58-fd2051a2f0ce | -16.50262 | -45.1081 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adec8874-f024-3235-b05c-de0ef5818088 | -13.169 | -54.93275 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69101287-4b7f-36b3-90c8-76d74a7015af | -13.13951 | -57.15432 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff0c8b8-96d0-3e7f-a4fa-2e570baa9870 | -13.1388 | -57.15857 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93adbe5f-f698-36ba-aeb8-d99a378573b5 | -13.15793 | -54.9161 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c3e7fe4-291d-3d18-a4f8-77a877f68556 | -13.16012 | -54.92386 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c24e0f4-f3b4-311c-bede-0a4896921020 | -12.97842 | -56.85666 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d15fdaa8-8d89-3512-bd5d-ee4a673eec48 | -14.64714 | -54.91327 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9c70691-785e-3cdd-8bc1-e69bdbf2ab55 | -13.14351 | -57.15787 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aced48bc-697d-3f22-9f28-886eae1a7ad2 | -16.83716 | -48.91613 | 2025-08-19 04:55:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb18daf2-e2a7-3e59-b841-5f186c21c942 | -17.39948 | -46.70618 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ce3bc9f-d564-336a-a70b-39000b632e3a | -14.16785 | -45.31903 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8639e7e3-e29d-3a54-9c27-06fc36f55e46 | -17.98623 | -46.35527 | 2025-08-19 04:55:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c2e42ab-ef66-3ff9-b258-247a2be65aa3 | -14.84324 | -48.06208 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6f66fbb-cc38-3245-ad4b-25c83e3ffd46 | -15.0412 | -54.82108 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec05e696-69a8-3338-9b7d-65b44ec515a4 | -13.00544 | -56.84882 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c2db0a-6ca2-3807-8970-85931812de82 | -15.16205 | -48.78249 | 2025-08-19 04:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 954bda6c-2d5e-325c-82f0-0f3690adaf90 | -13.14742 | -57.15141 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd6da60-2b93-320e-8ac3-6bf93df9e7ac | -17.48506 | -45.8539 | 2025-08-19 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef31ad22-dfe6-35e7-a480-93b86ebcf4eb | -13.47411 | -47.0611 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b127643-6b55-3de0-b09d-3b6dcce2b1d4 | -14.50219 | -45.94405 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0affb9f3-d360-3226-b775-de469525af39 | -17.82348 | -44.49269 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 281d93e2-a9c4-3241-a1a4-92edc4865958 | -14.30896 | -53.37947 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c746b4fe-e027-32fe-9a58-135a44844426 | -13.17986 | -46.88463 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea25981-5f11-326d-a8b2-81979350a0a0 | -13.14311 | -57.15498 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5de2a7c-d9ad-34d2-a971-a6ddc487e4b1 | -14.17791 | -45.32368 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baadc385-cfbb-3e6a-a295-c6fae97a2949 | -15.01905 | -54.81004 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5830f38b-fdbd-3f60-bb71-eeb5737a3e6a | -14.62222 | -54.89799 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ab45fe-65ac-31ca-981c-c191290c38a4 | -13.14857 | -57.15009 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36834ea5-399c-31a2-954e-5a684e0fb04d | -13.17235 | -54.93332 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462da620-0341-3b8a-896f-a065f74c7034 | -14.64599 | -54.92044 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b977b65-8fb3-3054-a093-fb9549d0dc83 | -14.47581 | -53.04043 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40f998eb-3160-3195-8001-72173ffe1f24 | -12.99125 | -56.86748 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a31ae912-ea27-3521-bd99-6c9e129559f6 | -17.40874 | -46.71346 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bafe1c42-2536-3a80-b8c2-e56eb722c29e | -12.98184 | -56.84513 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb9037f-542e-3140-bcef-bd64f933ed66 | -13.17454 | -54.9411 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa4bddb8-fd8d-3ac6-b7e6-15690891f8d3 | -13.31801 | -50.78915 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a66ae08c-81b9-30d6-9b44-342d9c191004 | -13.13808 | -57.16283 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b056dab9-3cf2-3ccb-b4c8-498c95283355 | -13.15459 | -54.91554 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2759954-dd22-3983-9311-65c1be7437fa | -14.64886 | -54.90252 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e71f583-52ca-32ab-824c-abe1926fd373 | -13.17338 | -54.9483 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67268821-4748-3c2d-991b-aa8fdf8994ec | -13.19287 | -54.94365 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74ecdd8c-0e44-30a3-a9cd-89143875bf9e | -16.81587 | -49.36875 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92ddf7a1-d20a-3986-8c3c-e690adf24ecb | -14.9852 | -54.80808 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62fd2ac7-aee7-3658-a33c-1595a0654f68 | -13.14497 | -57.14942 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80ef1e3-45cc-3883-a7c7-b7c7e1623f4d | -14.84309 | -48.05992 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b98f89a-56af-32c4-8744-f6c133020abd | -13.15838 | -54.93468 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 89a47566-ee80-3f7b-b347-5420c199e24f | -15.03017 | -54.8045 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d411449a-3f1d-3451-bd87-983ae6494718 | -16.62364 | -51.36244 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 724f1acf-4a14-36ff-b923-aaa7c96e9137 | -13.44156 | -56.89961 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7002af3f-950f-3e98-a3b2-37fcf56824a4 | -13.18736 | -54.94695 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 760bbc6e-0d8d-3481-8bca-b6657937a33e | -13.44139 | -56.85761 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a95e804e-9165-34a7-aeb8-c068dec81c4d | -13.16682 | -54.92498 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da07d1c-efa0-347e-82f8-c66b7db00e94 | -17.82335 | -44.49063 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b123d754-15d4-3403-b95c-b840edcdeabf | -16.47811 | -45.07876 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6772dba-cd9d-383a-8e1f-3c7403632a0d | -16.0139 | -47.78986 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2bf0a16-0b92-3329-ae34-cb5a151c2267 | -13.25621 | -50.8037 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90ac48a1-9399-3e96-87b2-0a910a68af56 | -13.58854 | -47.00194 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cbe2fe1-3d4a-3b17-9933-89e7fa18f332 | -12.97622 | -56.85683 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 728ad507-e12c-362f-865a-6c2d59159619 | -14.96695 | -54.79397 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ea62ec4-aa07-3259-86aa-6e1c9551fdaa | -12.97759 | -56.84861 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29b774de-bf5c-3a15-aeac-fece444f4beb | -16.47686 | -45.08965 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb340541-4910-33b5-9501-9e4e84a6d43c | -14.64381 | -54.91271 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9de9ab7d-3552-36d4-9973-475fd4abef60 | -14.84653 | -48.07087 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a88715f-bf62-3337-a323-84705910b09a | -13.15066 | -54.91858 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bef6c379-1503-319d-9538-c7445c68a692 | -12.97828 | -56.84451 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f75db35-3b73-3719-b8b7-31ecad8e4fa4 | -14.64266 | -54.91988 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae88eda9-6aec-3924-b569-97caee35d2b0 | -14.61888 | -54.89743 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bbf375a-dcd6-3648-a4b4-9d589e658181 | -13.86452 | -45.53814 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7b82fde-47c2-3c27-a65c-aa139a57aaa8 | -14.17463 | -45.30687 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f936a9ff-0fc0-3208-918a-f6fdd16cc60f | -13.18776 | -54.95391 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0898b6f2-58c5-335d-87d5-664f6f4374e4 | -19.82003 | -44.32784 | 2025-08-19 04:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef22b15e-6f9d-3321-bc64-9b253c80284e | -12.98053 | -56.84435 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ccc60f4-fa8c-3eeb-a7c9-ccaf740598a6 | -16.4878 | -45.09099 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edc2d807-88e7-3273-b97d-785a5c231540 | -14.31286 | -53.3764 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c7ed859f-9d02-3a15-8c28-2175fc4e7e14 | -13.1607 | -54.92026 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fd9096b-1dfa-3418-bb5c-d6abd896bc85 | -13.00329 | -56.83996 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a6807fa-8105-3968-891f-0a6f3c5ba91f | -18.9745 | -54.90445 | 2025-08-19 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea2863d4-2ed6-3df2-be67-6b4c4feafa40 | -13.01535 | -56.8337 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 322b2072-3fa7-3897-b130-3517be7589e7 | -17.41939 | -46.70871 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5287c43c-3df4-318c-bc50-edcd1ae5e8d0 | -13.02679 | -56.85265 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e73229f1-164c-39b4-8c72-e44c8637dc4e | -13.18048 | -46.87975 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf91e21f-e968-3710-825e-78b35d07cee3 | -13.43838 | -56.81103 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 746403d8-a164-3504-bc44-9925804b1734 | -15.08206 | -55.42427 | 2025-08-19 04:55:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ba8402-48da-3c3d-b080-460baa85ed11 | -14.30617 | -53.37531 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b0bac40-2b0d-38c1-8714-072df2669e65 | -12.99903 | -56.84341 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecdf854b-7ca9-3412-92c7-cd4c073443dd | -19.93723 | -45.06615 | 2025-08-19 04:55:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6805e58d-c0ae-3282-bd0f-dc5d28f52372 | -13.00824 | -56.83242 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f40386c-edcf-36e3-a2c7-f954ea880712 | -14.4059 | -56.45119 | 2025-08-19 04:55:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9ee1a15-3fc7-3aca-b42c-72c1c038fe6c | -12.99617 | -56.83867 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c11ac20-fedd-3d43-8290-476bd35f9a0e | -14.16862 | -45.31258 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7743f3e4-6b7a-34c8-8ec9-1647fe2fc632 | -13.1795 | -54.95303 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85bec84-42be-3d55-9f8d-5798792076dd | -14.17424 | -45.3101 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18fbd021-28bb-3194-ac45-f0c55822b0df | -13.16726 | -54.94358 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fac7de8-c7fe-3a56-8ca4-3de614beb872 | -15.01629 | -54.80591 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61fc418c-4749-36ab-bdb1-903d9cb57c8a | -16.48113 | -45.10178 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e6563b7-e19f-3872-8558-3c4589e59aba | -12.97471 | -56.8439 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b19937d-551a-34e7-8457-560e523b99d9 | -13.61511 | -46.89391 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README45.md)
