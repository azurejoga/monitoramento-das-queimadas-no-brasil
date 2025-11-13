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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91cd291f-af19-3132-9e4c-6efadaaac1e8 | -2.63965 | -49.22063 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ddb2827-1701-324a-b54d-36d68be57ff1 | -3.58487 | -50.11122 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 570041d1-9cf5-359c-ba33-c9990f2fca91 | -3.12975 | -49.24463 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d8ceaea-21ba-3c46-9fed-f98b7672f120 | -5.38599 | -46.76154 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 146c5196-2147-3c53-9d0f-55b8378a0ab3 | -3.48962 | -49.96522 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfee1ebf-238b-3d1d-a3a5-b5d6fb403d55 | -4.63959 | -48.74943 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c9bdc1d-cb0d-392a-adf5-38f45df4ff57 | -2.63241 | -49.20171 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e5c02d4-a08c-3197-9d84-183ccd98b2ef | -4.5574 | -45.77646 | 2025-11-13 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3be0519-f7bb-3bfa-ba68-add28ed7e72b | -4.14442 | -47.65673 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d2cb1e2-a255-31cc-bd83-2ea5059744d8 | -2.86949 | -51.47321 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4de8dadc-cfcf-3927-933f-93086d8cb533 | -7.22741 | -39.95722 | 2025-11-13 04:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40aee67d-4df5-393b-a083-9c4079e0ee4d | -3.09816 | -49.27168 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38ccfcc-1bd4-33d4-be14-98b89359953a | -2.37569 | -49.41106 | 2025-11-13 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 146ea9c2-a795-319b-ae30-acfac932d57c | -7.47272 | -42.56543 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ddffd9a5-ee4c-392d-82da-83820bcdae6a | -4.20663 | -50.09198 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 970a580c-985f-3b7f-9859-f93c5af83386 | -3.48569 | -49.96823 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc1ded2a-1824-37d3-8ded-9f313df992a6 | -3.70184 | -49.02977 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47405a8-12db-3b1e-9e4a-97e997829dac | -4.71763 | -47.2238 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e396f42-b68e-32a2-9df6-bad4c6a820d5 | -2.86642 | -53.80716 | 2025-11-13 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f196f443-7980-3e2a-97ac-78524ce6856b | -3.57366 | -44.16149 | 2025-11-13 04:42:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4e16b6f-4eac-38ac-ace7-c0244d957224 | -2.52436 | -51.0412 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23546950-d2db-35df-a9c3-8e0362b52024 | -7.26056 | -45.36977 | 2025-11-13 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f7ca95-484f-3cc0-935a-f309cc13bd48 | -3.48726 | -44.04813 | 2025-11-13 04:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d0df0ec-bda8-3333-9b5d-23b840bd79c2 | -4.53188 | -46.43324 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ab3b69a5-d769-3acd-9379-d50a76565e4a | -3.29218 | -52.1108 | 2025-11-13 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb22bb1e-e223-3656-bfa9-def6cdc08822 | -3.0911 | -49.27765 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2e84252-8e7c-3518-86d1-01a5a8f6beac | -5.72231 | -43.53278 | 2025-11-13 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a719958d-fbf6-3ec3-973d-1f08ec6fe218 | -6.09925 | -41.58921 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cce5c471-c903-3521-b9b2-62e448c39488 | -4.84625 | -49.26324 | 2025-11-13 04:42:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9cea85e-3f9a-356e-8ffd-bda24011fe0f | -5.84748 | -47.68001 | 2025-11-13 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d0b592-d159-3143-ade9-001bf59877a3 | -3.46785 | -43.18363 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ce3946f-2cb8-3266-b968-4741f7da587a | -3.57259 | -44.15768 | 2025-11-13 04:42:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e4856e8-9e26-3319-881a-a11c565a5428 | -3.15446 | -50.2688 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a310ac1-a9b4-331e-95a4-d089e03c8c28 | -4.71176 | -46.39125 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dbd831a-2d0c-375f-b680-ef367f12ed64 | -3.86466 | -49.79947 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7c7ff3f-7e33-321b-abaf-b8544103c7f1 | -4.24546 | -49.67671 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bcb08ac-9d12-353e-8dfe-372aba9102ee | -2.73236 | -45.48222 | 2025-11-13 04:42:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3fb8eee-f17d-3b76-996f-5328239f8ed7 | -4.7153 | -46.39184 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 339b5732-ac34-3591-af93-9615690c6847 | -7.15307 | -41.70259 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 254c896a-c0fd-30ac-80d7-e470e4aa2ae5 | -4.51899 | -46.42302 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5af35831-a83b-3ad3-bc77-6f31f6091c97 | -2.00647 | -54.45491 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b69ae9b7-b410-35a7-92cf-0ce75122f00f | -4.44919 | -50.10157 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fff37c08-45f4-3f34-b14e-dd117f23539e | -2.4587 | -49.27026 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3757d618-7e9c-3043-a8d0-9f433e1c945d | -6.10909 | -41.53199 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b16185c-a824-3257-8faf-fd824a19327c | -5.44342 | -44.65371 | 2025-11-13 04:42:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9560c952-44eb-3f64-9194-cd128536ccf6 | -2.45536 | -49.26974 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fced62d-b49d-3c35-827c-dc7315dbbfaf | -2.45259 | -49.26574 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8dd79d8-0790-3c33-98f2-ad04d0f645b9 | -2.03734 | -47.0411 | 2025-11-13 04:42:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e05ee6d-8a63-3ba4-8c50-df6546735967 | -4.52835 | -46.43269 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9d05ce21-78b4-3ceb-81f4-2e0932677671 | -2.9454 | -45.55025 | 2025-11-13 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3929cb10-9b76-32b5-9064-1229228c4e82 | -1.83063 | -53.80919 | 2025-11-13 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c9a4a82-cd13-36ec-8c52-e8db2bb2e7d8 | -3.3079 | -49.46482 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25792520-0576-3b34-9994-22153cab3d76 | -1.53469 | -47.21876 | 2025-11-13 04:42:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b5da492-6222-34d3-acdc-159b80330b66 | -6.10075 | -41.5917 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ea884099-fad9-3205-9719-209eef53b6a1 | -2.17169 | -48.369 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1de0eb79-504d-3ba5-bff9-ef63ac37fcb7 | -4.24697 | -50.05481 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea408ac-e87e-37aa-ae35-d469351e3f96 | -2.00214 | -54.45426 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d7b3ea3-c14e-318d-ae5d-d1a0f1a28dde | -4.12754 | -46.8417 | 2025-11-13 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d74f55ba-882e-3b5b-8793-54c663af4b48 | -3.66929 | -45.69024 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9fe4f5-00ab-3964-821d-50b6d3f88502 | -3.58405 | -46.45825 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16093970-c7d9-3601-9a8a-936842bb9be4 | -5.72868 | -46.54783 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f7b9818-78c1-35d4-b854-b88df0a20472 | -5.09557 | -47.4656 | 2025-11-13 04:42:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 587e8339-1b24-3ba4-a85d-6420612a0059 | -4.81691 | -47.34854 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f81e59-8761-3f1c-ba04-100a27ae743f | -4.20271 | -50.09499 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58c17e39-bbfa-35cc-bd40-36eb04559a15 | -7.83149 | -41.7674 | 2025-11-13 04:42:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b97db9ae-aae7-3e99-abcd-59ad49147603 | -4.01166 | -48.80598 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c735bf08-3e3d-3514-bcb5-ffb60361b869 | -7.49547 | -47.33379 | 2025-11-13 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6e6540-30db-3240-89cc-dded14a41db9 | -3.34906 | -48.39079 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eec3589-7d4f-34ec-b06a-ff1a8a4591e3 | -7.12737 | -41.86043 | 2025-11-13 04:42:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ffc51cc-b666-3433-bdda-6e47701e17c2 | -7.1053 | -42.36939 | 2025-11-13 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6f1b5f12-6b9c-352e-827d-e9b3dde1aa67 | -3.0922 | -49.27071 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d6928b74-4e17-34d1-8f1c-fd114cbb66c9 | -3.87272 | -52.2135 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd45b59-d386-3865-8e8c-cb0accacb6a1 | -4.56462 | -48.4958 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb44a5d3-8342-31a9-9a71-670395114b93 | -2.45307 | -48.81524 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b1a8b4-c102-3639-b68d-89cbe4cf04df | -4.61442 | -49.29426 | 2025-11-13 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8219e9e-75a3-314d-a122-a07a23c2d6e1 | -2.64075 | -49.21369 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b76979da-7134-3587-ae98-4556982ff5b0 | -3.33823 | -48.37867 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e36bd750-9f2c-320a-92fb-ddd957386fcb | -5.67954 | -46.0117 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6485d719-33bf-3052-8cd2-6ab736f292c1 | -4.25684 | -44.59661 | 2025-11-13 04:42:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5989d5c-047b-34d7-9104-643253bb1e57 | -6.29865 | -41.7408 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15fa3293-3a64-3c8b-b8fb-53b9ac76b565 | -4.00779 | -48.80891 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b961867c-c33f-3560-9417-022e8576b7e4 | -4.70691 | -48.12475 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e82bcd6-56ee-3c69-bc61-23830b9b40d0 | -4.84758 | -47.57729 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fe2c465-d4c7-30f5-bd95-e81b878d7ae4 | -3.06577 | -40.08463 | 2025-11-13 04:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8d7e12ec-ad69-3519-9b12-d9f9a9ff75a5 | -4.68303 | -45.85417 | 2025-11-13 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 937cf65b-5ce6-3349-b034-c8b47b63f334 | -4.01111 | -48.80943 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12cca6c0-a357-3e46-bbfa-ca051a0c33f9 | -3.08832 | -49.27365 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34372374-5cfd-327e-9f35-45028f3154cf | -1.67599 | -54.22638 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0dc19f9-ec76-397b-ac57-b9f3a940a0df | -7.55267 | -47.2461 | 2025-11-13 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f084eeaa-af86-3a1a-8cf9-8c3bba6edf19 | -3.36736 | -48.40428 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9e0d2f0-0c3a-3e37-a137-a3519090fc42 | -5.7264 | -44.83897 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef469fa6-6dee-3409-8d9f-9ea61bb14f1f | -3.03866 | -51.03229 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e5e0331-71db-3c14-a734-cfdaef33dc47 | -4.53248 | -46.42928 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 33c91956-8dea-363b-9f78-84f1e4122e51 | -4.24009 | -48.38481 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e164b0b-8349-335e-b928-bf7bab3c6b25 | -3.09706 | -49.27861 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef3e59ab-437b-38f3-a359-f4fd60cd79c9 | -3.43966 | -45.58196 | 2025-11-13 04:42:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a434092-dea6-3691-8cbe-e326d1730bb3 | -4.71594 | -49.76531 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527e81cb-5866-3fa4-b011-74fd34e192ae | -5.83705 | -38.3539 | 2025-11-13 04:42:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 135626cc-3de1-39ab-893c-0e7c65bc5fcb | -3.29324 | -50.07664 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8f4316-8f3f-3c4a-9715-3c607c2dfa86 | -3.70462 | -49.03374 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README30.md)
