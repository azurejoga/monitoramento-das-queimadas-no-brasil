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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c27e0c5-a57e-3b0b-96ec-299eb6c8668c | -6.60973 | -37.88646 | 2026-10-05 04:38:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1cc685d2-af7e-3d92-8f29-de3fbcc1e344 | -2.80625 | -54.08707 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd9f241d-5f93-3c70-905d-6adc596353a8 | -3.8403 | -50.32087 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 160d6d26-e45c-3af1-a9d5-63cad4d97a16 | -2.97603 | -54.09879 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16ca3a8b-1829-3a1a-8403-9497e56ea398 | -3.11099 | -53.74938 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb23929f-2dec-3a1b-85a4-97c9f1a62a7d | -2.94282 | -54.19971 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6dc78abb-543e-3195-ab7b-556554bdedf9 | -3.8789 | -55.81065 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37d6abc7-02a7-3e68-b49f-440139394d4b | -1.18051 | -49.25668 | 2026-10-05 04:38:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6552de4-7a1c-3ff6-96f2-d1115b158c93 | -3.11776 | -53.75306 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f615898-792d-32ea-ab21-f070e44f02f8 | -2.67612 | -49.02886 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab0fcf34-0f8f-3c5a-aa7a-73a0a0caa999 | -3.12805 | -53.7217 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebbf045-55be-3926-b642-16adfd3de329 | -2.85098 | -51.30065 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fab5036d-bd7c-3a96-8caa-996d3a93e1b7 | -3.6637 | -54.28314 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 530f30a1-83b5-3847-bb40-a576a48c0cf3 | -2.90776 | -54.1202 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e6742b-43a4-38b0-bd8f-3963254c3e64 | -6.90899 | -43.66839 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6dc8ce-ef74-3f87-a2eb-476daa63801a | -3.13114 | -53.72271 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d186c3c1-eb1a-31a6-ae23-ff997dbb3af7 | -6.91129 | -43.67692 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8a85d99-bf5d-3da2-aa08-7a32bf814e0c | -3.0527 | -54.21475 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b65bdaa-e9ce-39ab-b1be-12b48e029d3d | -3.12659 | -53.71894 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 06f51e4d-7169-37ac-82b6-849a2ebe93b6 | -2.36441 | -50.60376 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d10eab1c-affc-3f63-8eaf-3cb8757f42be | -3.30061 | -53.8517 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032b9cd4-c4e0-345c-830b-8f615a5e047a | -2.47389 | -48.03762 | 2026-10-05 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8720a25-97e8-324f-a15e-08ace7f74a18 | -2.58045 | -51.8787 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a6699fe-f784-3c2d-9d4a-67519f63807b | -1.55761 | -54.79628 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c67a3e0-4ece-3916-9fbd-cd7ee6132cbf | -2.95152 | -54.1473 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 79e1d827-0378-366d-84c2-f65109b100d8 | -2.78644 | -54.10963 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce88b1da-9c72-3159-a8af-0ea293b1c279 | -3.31126 | -53.85046 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc0ceade-501b-39a8-8e63-21d4fe607e67 | -3.57566 | -55.42092 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbc17879-6c31-35f2-895a-44be1d12a6e0 | -3.51002 | -54.61485 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ea153a0-d908-3487-8ce9-16b94f628b30 | -6.20319 | -52.82859 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86a9b799-5eb1-3ee9-a8ef-d2e8224ae441 | -3.11549 | -53.7231 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1785fe1-4feb-3bdf-8ec3-85cb5f3fa8a5 | -2.81773 | -54.11483 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4853af80-d3ea-397e-ad7e-3d57880a21c8 | -3.50805 | -54.60777 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bad3293a-e507-32df-b8c8-74161a2a2be3 | -2.96925 | -54.10731 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d25526ad-192c-391d-a11e-2d67327136a9 | -3.11146 | -53.72794 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e1471fc-32cd-3473-ac0f-4276943d4338 | -3.92465 | -49.71122 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f484fa1b-81dd-3b8d-a1b4-82b217e4a23b | -3.12609 | -53.72185 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d38c68f-eee1-3d25-8ae8-bc30623614d6 | -7.8866 | -44.19481 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7997adce-43dd-3490-b754-c816b3721d42 | -2.90097 | -54.12878 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28af63fb-894b-387d-b6f7-a1579af376e1 | -3.04852 | -54.21092 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7a5c199-e3e7-3100-b71c-ad6df1ca9eeb | -2.80783 | -54.10991 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92534d37-ed3b-3619-9635-4d686a65f1f0 | -3.28732 | -53.83732 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2742dcfb-0a56-360f-a550-5d8a8f51897b | -6.92189 | -43.67316 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0d12d18-d5ab-378a-9dd3-33500facb92d | -4.0427 | -50.75882 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 716ed2b1-6f97-366e-8e83-016ff6ffbc66 | -4.05185 | -51.07837 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3205357-a6dd-3f72-8b30-fdaaaa8feba6 | -2.78227 | -54.10249 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e78cdcc-7398-369f-840d-9e13aa0a962b | -1.97313 | -48.91471 | 2026-10-05 04:38:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 935b0bb7-59d3-354d-9c15-e49f8f86ec9f | -3.05527 | -54.39148 | 2026-10-05 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 352887b3-6691-3fb6-8541-47f12a7f46a1 | -2.22336 | -53.71808 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41ac10db-a3bf-38d8-a4c0-a2a3bcadbd55 | -3.87822 | -55.81456 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5ea9220e-5243-35de-b05c-a07b9b3a7a88 | -3.30764 | -53.84074 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ec4b8b2-224a-37fb-914f-262410b52e45 | -6.90128 | -43.67132 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88f0c551-7d4e-3281-a350-4d8a073ec2c2 | -3.30966 | -53.84462 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55dc60de-e902-3c52-8894-a86ee7523277 | -2.78279 | -54.09933 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e8a1430-45e7-3194-842e-7b0e033fe2cc | -3.50751 | -54.61101 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4df9f15-22d5-35b2-b874-6031ba39ddca | -4.29064 | -50.7874 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10625f58-c7e9-368f-9e8b-aa6c92023773 | -1.33467 | -54.22932 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a64f4cbb-f8ae-3aa3-a84e-a55e57a14e09 | -2.77811 | -54.09532 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 872352d8-fd28-39dc-87a3-86a4c14417fa | -3.57004 | -55.41991 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14aa5ce1-7a2d-3968-aea7-91e8db242f8d | -3.90863 | -49.71329 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e495ab0f-24ae-3f92-ae1c-28064c740ebd | -2.94384 | -54.19453 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d65500c-f809-3108-b9bc-8b2b3ced54a7 | -3.06743 | -54.1913 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 521c7bb6-95e4-3248-8afc-c36e142b9b55 | -3.07134 | -49.54395 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 710e45e8-6360-372b-bf0a-eeb2524f3324 | -6.92836 | -43.67828 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a7ba536-05c7-3d9c-ba2e-e1fa9844b26a | -3.12615 | -53.73341 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f599a1e-4cf8-300b-bd98-e5eabc0c62bc | -3.57484 | -54.65336 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8bcca2-0d13-33c9-8891-f26ece3ed92f | -5.99318 | -53.64019 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 283a10d7-b195-342c-9d70-47b99988be4e | -2.95253 | -54.14106 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b332f9e4-77cc-3be4-a75c-f0e44221cf40 | -3.51897 | -54.62663 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c24068b6-3198-3053-805c-6a5391fd8d90 | -3.10135 | -53.72621 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| faaf7cdc-1d9c-3fa8-bbf9-be89b0e504d9 | -3.12518 | -53.75777 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a67bfdef-4e92-3350-9ada-d4df52a95ef8 | -2.90252 | -54.08731 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87cfed83-23b3-3528-9dc9-da8b3a24ff1a | -2.93223 | -54.13415 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ae08a10-41ba-3274-86e6-e3b294bfdb06 | -3.12353 | -53.70646 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2f49ecf-f14c-3cc6-9eba-7100c6c13066 | -2.97294 | -54.08551 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 746afdae-b8b2-3770-bdf8-4278f87ccaeb | -3.12538 | -53.70624 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99388b9e-c724-3eb4-84fc-11509c179890 | -3.11399 | -53.73186 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61e29a67-5f5a-354d-b544-82679ba72dd3 | -0.49226 | -49.10221 | 2026-10-05 04:38:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d5dec3e-8faf-3f42-b877-4d813c19374c | -4.08206 | -48.95831 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9505a8a4-c13f-386f-95a8-ce5d8c353ad3 | -3.16068 | -50.43699 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4806b71-1c3c-377e-8519-f0ad7d63b899 | -6.21147 | -52.83444 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e8ab56-55b6-32e3-816e-04f5bea56431 | -3.12161 | -53.74815 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43fda2dc-29bd-3845-90b0-f070f00daf25 | -1.0941 | -54.10856 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 618581ac-0243-3a12-91e0-67732086a2eb | -2.24113 | -51.91413 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c53ba61-01b2-34ff-a292-7bbb24107313 | -3.0555 | -54.16682 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b16be9eb-3211-30f0-b3ed-8ba9a5fa77f3 | -3.04586 | -54.22333 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cd94806-d5de-3182-a5df-52d95c4c89ec | -3.06048 | -54.23232 | 2026-10-05 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cd66eee-80fc-3a50-b378-64ba9c62e836 | -3.51785 | -54.63314 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb10d7bd-2bb8-3aec-8032-4286520a5842 | -3.05657 | -54.16054 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a2b5b3-d1f1-33e0-84fe-769a594fd981 | -3.11655 | -53.7473 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0b2a36-0a4c-3377-8987-ea5f069482d0 | -3.28429 | -54.17863 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9dd3297b-8721-3b68-a311-5b8a8dd8ec78 | -6.90607 | -43.66387 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52f5da4a-78a0-303f-8a8c-1ccf4d3a2cce | -3.50944 | -54.6182 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ba04678-d313-37ac-b559-3c5b9de24332 | -5.99885 | -53.63586 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 359b850a-96d3-3715-b501-015889b0bdb1 | -3.99025 | -55.82107 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3709df10-0efc-33cd-a51d-3cb1831a5761 | -6.01738 | -53.52792 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e206327f-6ded-3f5e-b392-e3fa29043481 | -2.95191 | -54.14632 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 995307f5-5d09-3868-ae9f-ad52f7f57b74 | -2.80262 | -54.10902 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d27cb464-22df-3da8-81e8-ded5190caa99 | -7.18117 | -42.00741 | 2026-10-05 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d003de67-7cfc-3e47-8cbf-8e1323673df9 | -3.12139 | -53.76271 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README27.md)
