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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d6e2082-671f-37cf-a212-a132a4916717 | -17.54663 | -45.94522 | 2025-11-19 04:33:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01984fb9-9684-394b-a676-6c7a8325d539 | 3.6464 | -51.2963 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdc97dbc-90a6-3ee0-9433-936141a04ab3 | 3.66636 | -51.29319 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e40e5e-df5d-33b0-bcae-49a1751e3f50 | 3.64586 | -51.29281 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95954b81-4ec1-3177-85e6-831628b8eea7 | 3.64973 | -51.29578 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b28a6f-7c6d-3110-bd7c-beb33f922fd8 | 3.6669 | -51.29668 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a72343-0a88-3d7b-8e1b-4ba7120b5206 | 3.66303 | -51.29371 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c07024-a33e-39e0-9419-7789734d578b | 3.65583 | -51.29126 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8587851b-e9d5-3700-a090-d5540453a69e | 3.64531 | -51.28931 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddad012d-8bdb-37a8-afe9-a062d6321b3b | 3.64253 | -51.29332 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd441414-1153-3d1c-9090-04896990075a | 3.64864 | -51.2888 | 2025-11-19 04:48:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9d1a54a-dc30-3b55-beaf-16100f835a5c | -3.01769 | -49.42892 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a864366-00b8-3c9c-82b3-7c0dd0d89a33 | -2.85499 | -49.5029 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 294923fd-1ec9-3480-99bb-67370663c869 | -3.22153 | -46.12886 | 2025-11-19 04:50:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde4ba8a-cd14-3d15-aa51-f411d1471c96 | -3.37029 | -49.25649 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f03cb97a-89cf-33a7-ac2a-09ef25867ac0 | -0.90759 | -52.90319 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b54ce19-8bd8-326f-8106-5d59cb9cd3e0 | -2.91548 | -49.57081 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0faccbed-5819-32c8-80ab-dbde8acd198f | -3.02057 | -49.43332 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 538254bd-8ad0-3218-9e09-26803d209c50 | -2.52042 | -54.14038 | 2025-11-19 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57798527-6dbf-34ea-9c86-fe0efb567421 | -2.29054 | -46.52549 | 2025-11-19 04:50:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ab67f67-23f3-3552-b9f0-6086ee132a1e | -3.28977 | -44.88252 | 2025-11-19 04:50:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba42cc74-04cc-3301-b2b1-dc38e26f601a | -3.55466 | -43.47051 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdba20a2-1a1b-3a8f-b805-cd52ead4b6b7 | -3.35446 | -43.49704 | 2025-11-19 04:50:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8ac619a-1d0f-368b-bfd6-ded27d258780 | -3.02041 | -44.46304 | 2025-11-19 04:50:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a0f8e75-9a5c-3be7-929a-1d9e2167523a | -2.85992 | -49.60889 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e957b353-062e-3d97-a83e-32ed7e818bce | 0.90814 | -51.10602 | 2025-11-19 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c3a014-9e18-3d13-a33e-e491c8308898 | -4.14786 | -46.78527 | 2025-11-19 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9003701-1e9e-39e3-915b-f9f3319d3f57 | -2.85288 | -46.65762 | 2025-11-19 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d9a29d0-bf2f-3ced-8b17-0b8af35790f2 | -3.24918 | -43.29223 | 2025-11-19 04:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d78d9e59-3f4a-3318-a119-572ea78262cd | -3.25061 | -43.29311 | 2025-11-19 04:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a912338-8119-37c2-876e-443e9ef23d4a | -5.11868 | -46.08552 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15036b33-97f7-3180-bbf0-d42528c3c88e | -4.75412 | -45.90575 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e27356b0-115d-3ad3-871a-c67eaad5ffbb | -1.37813 | -45.79556 | 2025-11-19 04:50:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 759efb07-90c8-3701-8cb2-e61b170777bb | -2.82196 | -49.12807 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f1e16b12-b447-3c3b-9df7-2fa59c3600db | -3.02117 | -49.42946 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f368454-e70b-30ee-8f92-4dcb35aae772 | -3.22214 | -46.12489 | 2025-11-19 04:50:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248b5efd-b400-3af4-8db2-2aacd91e5248 | -2.9113 | -49.08891 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6d6cf8c-f5f9-352d-8126-0920be4e02bc | -4.1432 | -46.78826 | 2025-11-19 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d0fa0ba-d865-35a3-92eb-2676bfd02bde | -1.14968 | -54.10757 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a2284d-5d77-3272-bb8d-ce9c52f6eaf4 | -0.99144 | -52.44101 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d979d69-f034-3666-b733-b34551363d1e | -3.01709 | -49.43278 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 995c5264-bb5f-356f-88b0-504e1f3e36a1 | -4.48433 | -44.32981 | 2025-11-19 04:50:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94a8d27d-08ef-3cd9-97c5-83a420fc9693 | -3.07115 | -49.1079 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b296eed4-c34e-3a92-8741-1b981a045bb9 | -4.87686 | -45.89622 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91280675-87cc-3364-929e-8d2af5ba69f8 | -1.13254 | -54.21419 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbc843ab-a3ed-3e96-998d-d4534a398e22 | -3.55197 | -43.47159 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47e60c73-8770-3762-a237-225cba9ead99 | -3.68436 | -51.85367 | 2025-11-19 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f46ab7e-3c92-3490-af89-5404b595b85c | -2.42485 | -55.69867 | 2025-11-19 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 547d7650-ea1c-33fc-ad41-278cbffe69bd | -4.14732 | -46.78891 | 2025-11-19 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 139aa26c-d0d6-3599-8ce3-d54b63a9e0f7 | -3.75032 | -51.82175 | 2025-11-19 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1411dbe5-054a-3938-a7f0-73e0ec63bf59 | -3.68412 | -50.16774 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f512c839-a4d3-3ae9-9752-e06b03edf9e7 | -2.87735 | -52.61581 | 2025-11-19 04:50:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8613563f-e6b8-3d15-a9a6-e2b0e1a019eb | -2.81843 | -49.12751 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7af0b4e9-a642-3e5d-9c71-acfa06345be8 | -3.55753 | -43.46938 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3aa45eb-8d85-3751-b827-f318af5c7db9 | -4.69417 | -45.88401 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1287b2a9-7f9e-36f5-9519-e1b198acd102 | 0.19113 | -51.0016 | 2025-11-19 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8b74abf-cbe1-3d90-b600-7b9394fc6012 | -2.32048 | -57.00159 | 2025-11-19 04:50:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31af6a8b-e9a8-3751-9487-00a383e5c535 | -3.68382 | -51.85711 | 2025-11-19 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8efc0b5a-dbab-35b4-97c8-c81a6d9ff69a | -1.48584 | -54.20285 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2732d246-be41-3aad-b760-31b0ddf9de86 | -0.72368 | -52.37426 | 2025-11-19 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 916eb1a2-6dd1-3e19-bd90-52d2adfebfa1 | -3.0136 | -49.43224 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44e6f2eb-5e40-3239-8f16-a765601ae038 | 0.19443 | -51.00109 | 2025-11-19 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c6be72d-2ea1-3880-9c29-35a3c9c4b759 | -2.91077 | -49.09225 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10511ada-8646-3b5f-9f30-58cb895bd893 | -2.45441 | -53.80479 | 2025-11-19 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05f6b6ee-5260-3121-8975-18e088c3469b | -4.4902 | -45.86577 | 2025-11-19 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc6a9552-0b99-3d59-9d30-c22bacc460e9 | -3.45861 | -52.80731 | 2025-11-19 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ba18853-48f3-39f3-bca3-0cce0d133bc5 | -3.68014 | -50.17091 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9fe8186f-933e-32fb-be9e-61510970182e | -2.28647 | -46.52486 | 2025-11-19 04:50:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43deaa1e-07a1-3b2a-91dc-9c99ddbc1e94 | -3.36935 | -57.24409 | 2025-11-19 04:50:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cb5400b-e99e-3063-a015-d0eeb49d67fb | -3.00735 | -44.38786 | 2025-11-19 04:50:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d210c761-7fa9-3d7b-82ce-1950b2fb7826 | -4.6941 | -45.88631 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3dab85-88ac-3974-aa22-3ae2f6e11fa4 | -5.11806 | -46.08981 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eefdedc6-5465-3ff1-a7ac-ed638074fb55 | -3.55415 | -52.07614 | 2025-11-19 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24be3461-a3b7-374e-9290-b5c5e01ec3cb | -2.81782 | -49.13149 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13cab7cd-108c-3640-9483-e4684e28cc16 | -2.86666 | -49.47333 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6832e9ff-b5ba-386d-af27-e8ce70f743a5 | -1.09202 | -54.12755 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241d96f9-3dea-3543-851b-891598eae0c0 | -0.98866 | -52.43699 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc631f68-11ef-33ec-8d28-7ca0cb6013a3 | -3.23716 | -48.51981 | 2025-11-19 04:50:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a26a2eac-1515-33f8-a169-52fa8f6a50f0 | -2.85296 | -46.65745 | 2025-11-19 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0164c5d5-a7c5-3e20-9efc-4040284f3c84 | -3.01649 | -49.43664 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae9d86a-8fc6-3bc4-a680-2d2a5d953e77 | 0.18945 | -51.01241 | 2025-11-19 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 921003c9-23a4-3f05-9391-ad6f0bc32e97 | -1.15031 | -54.10368 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ee638c0-156b-3923-9784-331dc41e05f5 | -3.01829 | -49.42504 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44964e45-caa9-3ba2-87c8-0cebaeafbb82 | 0.19773 | -51.00058 | 2025-11-19 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb203df5-ac06-3f5a-9b72-f99a31780fb3 | -4.29353 | -48.26426 | 2025-11-19 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5618caf-bd48-390d-b45a-ea39b1b50a67 | -3.56298 | -49.43743 | 2025-11-19 04:50:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 711a2753-2e3b-39c2-8a22-a0d33c247012 | -2.39604 | -52.00576 | 2025-11-19 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ef7ca1c-fb68-3314-9e08-4379c54d908b | -3.35402 | -43.50005 | 2025-11-19 04:50:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47a04d15-b381-35e1-a6b5-8973759dcaa0 | -0.92092 | -48.06332 | 2025-11-19 04:50:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b5d99708-2708-3bf0-8c54-143f79db360a | -3.0142 | -49.42837 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8a22d01-2670-310a-92b9-3f5222dc4587 | -1.15094 | -54.09978 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43dc5cd-55c5-3710-8cba-bed635dc9140 | -2.17213 | -46.45538 | 2025-11-19 04:50:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fa3d424-eed0-3349-8464-5503c7b54b94 | 0.91144 | -51.10551 | 2025-11-19 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3238c04f-6b2f-358c-bdce-682159c3a3eb | -4.69345 | -45.89056 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861b2db8-232a-38b7-be04-a1ba0961db67 | -0.98533 | -52.43647 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ae19ac-8ae3-3e7a-b734-85ac4c1c7def | -4.72289 | -45.66711 | 2025-11-19 04:50:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 727d91b5-08bd-38ee-a49f-866bc2663af1 | -3.55512 | -43.46751 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0f41489-a35e-3e4e-8018-ac2522ace3c4 | -1.48999 | -54.1995 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87af33f9-d807-3826-afab-b93af2d880ac | -1.32361 | -47.56266 | 2025-11-19 04:50:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734582a5-13ef-3351-bc38-0db7ac55a59d | -2.91067 | -49.0929 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README18.md)
