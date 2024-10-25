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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1c0e7cf-ec8c-3b3e-a0dc-c810c436854c | -3.60134 | -47.25871 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4ed5e15-9fbe-38ea-9a54-634435b9933e | -3.60079 | -47.26233 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 189a1371-f3bf-3365-be41-c0dac8521f85 | -3.60079 | -47.25905 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5cbcb70-efeb-3e41-bec8-46c24d30c6eb | -3.60023 | -47.26593 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5257968c-c67c-3434-a566-a946727f9c0c | -3.60022 | -47.26267 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2382e524-21f6-327e-9c43-ace1b2479dfa | -3.54728 | -47.35741 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4434c68d-a015-388c-8423-db51fb8f65c9 | -3.54673 | -47.36095 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01db31a-2e61-3757-ac69-88df4953b23a | -4.19828 | -46.80842 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db99d07d-2e76-3a96-a9e7-1085a6f3bf7b | -4.18836 | -46.87192 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c408bd6b-adee-3777-a92e-e065a4fbbbd0 | -4.18793 | -46.80683 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 717aa260-b81a-3dd1-aaf9-b1a1b0b12913 | -4.1855 | -46.86766 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02ff4921-6b87-31fe-8fa2-c376cfccf45e | -4.18449 | -46.80626 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bde9b047-d9e0-311b-894c-c4ed6d7ef8ed | -4.18105 | -46.80567 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8c38aa7-bb64-346e-a00a-4dbddadf77e3 | -4.16756 | -47.60922 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275e1501-0c58-3f54-a40c-be54cbfe4cec | -4.14882 | -46.83144 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| db4e294c-8ae7-3e72-a212-73a013909d73 | -4.14858 | -47.10391 | 2024-10-25 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a03bdd0-39c2-393a-bae0-14c529a1d096 | -4.14825 | -46.83512 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 43aba597-e9af-37b0-be9b-4bdf97034d2f | -4.14538 | -46.83089 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 011fc369-f71a-3a32-85c9-af29702218c5 | -4.14481 | -46.83458 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3a2cda1f-d79c-36bb-9121-20dcc5119c25 | -4.12986 | -46.88577 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f1d666-c93b-3b4a-b346-f50c89937525 | -4.02989 | -47.21689 | 2024-10-25 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafe6d56-c292-34e1-9e04-6fc2a250f644 | -3.85983 | -46.92122 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db8df90b-d6ee-3bae-9fb6-204c307e844e | -3.82383 | -46.9271 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7bae017-5f3b-3559-b403-09a18442663c | -3.81984 | -46.93026 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d55400-dc1a-305e-95f9-91214d0d1a57 | -3.81927 | -46.9339 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a5c3953-4457-3386-8b06-c8a7799df0ca | -3.81641 | -46.92973 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58858211-c161-32fe-a54d-7fbea80e44fa | -3.81356 | -46.92549 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 894ff005-0cb0-3d38-b0b2-839c78573c37 | -3.81299 | -46.9292 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a568b919-8f3b-3cb4-9f1e-05226170a5e4 | -3.81072 | -46.92122 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fb10319-956e-3b1c-a389-feab458c7214 | -3.81014 | -46.92493 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7795b694-0765-31a3-9366-3bf38ec1adc1 | -3.80591 | -47.4915 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa3166c7-4965-3c6b-85a2-b3aa54717011 | -3.80535 | -47.49507 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1171d81-d23f-397e-a5db-85c4c027b6e0 | -4.14807 | -46.43893 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031e6b2f-eb33-3539-8c59-8de18d7b19a7 | -4.14747 | -46.4428 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fd3c349-4e70-3297-b7ed-9ac9bfe65abb | -3.97151 | -46.46377 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d331390-d9f5-3981-9560-aa85fb48825f | -3.96118 | -46.39101 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d91fee7-1887-3aa9-9b30-8d509a2c67ec | -3.96109 | -46.41508 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64c5804d-081a-394c-8ee2-4a8e2619ee8c | -3.95759 | -46.41457 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a50f155-1143-31c0-953a-6062eba9f44f | -3.95708 | -46.3944 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d1f0c3b-fbfa-3c26-ab4c-3c353ac04fd7 | -3.95526 | -46.42986 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 26b7ecb1-1338-30cc-ab65-42490f6188df | -3.95467 | -46.43377 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 149c0980-9ece-3b71-9e95-4d1c7fd66f26 | -3.95409 | -46.41407 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e50b1cf-2d61-3560-b140-8007ef7ffee1 | -3.95299 | -46.39778 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc3a50ce-0164-31d9-b7a4-44afadf5cec3 | -3.9524 | -46.40165 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8a87c8b-d79f-34cf-999c-8f215ee067be | -3.95238 | -46.39867 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e827a75-5e28-36fd-8239-a5b01eb26ca4 | -3.95176 | -46.42936 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a07a4ad5-2b08-3448-b06f-9348f9a606c6 | -3.95117 | -46.43327 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8ed0be1e-b214-312b-aaf4-29bd3ddff804 | -3.95058 | -46.43716 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3c3d0be-fe11-37dc-aec0-b27509fe4764 | -3.94826 | -46.42889 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb396b77-2bec-3285-b213-eff50b907a82 | -3.94811 | -46.4259 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf48dd89-33aa-3a1b-8d16-110d939f6a73 | -3.94767 | -46.43277 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f38af26b-88a6-3324-9e8b-5c086d4801b2 | -3.9475 | -46.42975 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5f47b1c8-8c08-32f1-a9ce-039792c74fed | -3.94708 | -46.43664 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e84df4-73bb-3f13-b805-70a9f20db1df | -3.9469 | -46.43362 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 493380c0-f291-378d-be91-c83c1ccfd943 | -3.94476 | -46.42839 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86e25b02-a459-3ed6-ae9e-b512550a57bd | -3.94461 | -46.4254 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ec360f1-7176-346d-9532-616a4d2fb824 | -3.94417 | -46.43226 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eee7529c-3503-32cd-b05b-bcaf0398e314 | -3.94401 | -46.42925 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6994d16f-70f5-391f-be94-fd3f384ec467 | -3.94388 | -46.45282 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bed93198-48a3-3a07-a89c-5034ec301663 | -3.94359 | -46.43612 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d2045e0-8d92-319d-924d-0b0753566cab | -3.9434 | -46.43311 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be2ea155-a0c0-3917-b537-f577dc1435d8 | -3.9428 | -46.43696 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6efdac25-86da-3c58-b235-f84efa889b0a | -3.94125 | -46.45149 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a945a3-c008-318b-90e6-d89373e36762 | -3.94067 | -46.45529 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9a78d7-7d4f-3594-9c44-b8f3dcb59085 | -3.94051 | -46.42873 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60f03103-ae3e-369f-b68d-2a5d2d66cf52 | -3.94039 | -46.45231 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1227b49b-bccc-30c5-bad7-66cdfec15800 | -3.93991 | -46.43258 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9e69fc4-ab08-387f-b6a0-55c561638e22 | -3.93702 | -46.42819 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19ecaee7-ac0a-3f8b-bf14-84a3e2df6322 | -3.93642 | -46.43204 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 621dce2c-3365-34d2-ab8f-ad14fabe08a7 | -3.93353 | -46.42762 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0209c2d9-24d2-31a0-88dc-adf4a645da1e | -3.92017 | -46.42161 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f14271d-31dd-3764-959a-1d46d5cbb933 | -3.877 | -46.44655 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa36c75f-6a9c-334c-90c1-ee3fcb9fdf0c | -3.87352 | -46.44596 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf9341c-0255-340d-8e03-fbac699e4404 | -3.86674 | -46.62804 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4528d6aa-cbfa-3274-899a-ba30bf9964fd | -3.86556 | -46.63566 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf31ca07-736c-33c9-a364-c640dc120f8f | -3.86327 | -46.62754 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ab3bbe6-dc16-3e61-b351-0aede1c812f9 | -3.86151 | -46.63892 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ad14095-bd0c-3349-8e4b-69c895c68bfd | -3.86093 | -46.64271 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adef618f-01b1-34d5-9615-8c751465f4bf | -3.85493 | -46.45077 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bbd522e-4e84-33b6-92f2-c243ea9e915b | -3.85434 | -46.45464 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99cd220-b622-38e4-abc4-0a02b61d2347 | -3.85254 | -46.48964 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5ca1255-0b8e-36bb-9cd9-fcac978c2f17 | -3.84906 | -46.48911 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e80fdd5b-cb1c-3a8f-ba58-82a51bc79d9b | -3.82933 | -46.47831 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a77d541-5efc-3913-b686-1e0935f1508e | -3.82781 | -46.47883 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4d4c9bf-79da-36a0-90e2-903667b91d7b | -3.77738 | -46.66499 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c762ada2-9448-3bc7-b3fc-ece46011c647 | -6.28475 | -47.82154 | 2024-10-25 04:38:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78f66db1-0851-3fb2-9419-bb8059b217e2 | -5.64966 | -47.90862 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a6a7706-287f-3b47-bc25-56eb7264b225 | -5.6491 | -47.9122 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fad2e3eb-0be3-3005-b3dc-0bdd70eeb001 | -5.44152 | -47.67861 | 2024-10-25 04:38:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2a47450-1daa-3ac1-ad91-049180ee9b71 | -6.29414 | -46.67957 | 2024-10-25 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d2bc34a-d391-3098-bd4d-4ac1aa1b8431 | -6.17907 | -46.79986 | 2024-10-25 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af452b47-ffba-3763-8afd-152adb738aa5 | -6.0572 | -46.93696 | 2024-10-25 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f9b8de9-81da-339a-8c15-649d8bb400d9 | -6.0543 | -46.93257 | 2024-10-25 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 871c8fd7-81ae-360b-a721-02b3fcd734b7 | -6.05371 | -46.93642 | 2024-10-25 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7f01bc3-931d-3929-a2e8-fa2a57610289 | -5.97711 | -47.28627 | 2024-10-25 04:38:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be0f5063-ca00-3a5f-b920-17ffe069420d | -5.97597 | -47.28532 | 2024-10-25 04:38:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c874b206-c0c0-3b6d-a03a-94c0b40c842a | -5.85176 | -47.19103 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| daae288e-6b3e-378c-97f6-388791ba100c | -5.84791 | -47.03198 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62a4c16e-165d-3bfc-a0c7-2fd35d65bd4c | -5.84733 | -47.03578 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6554be8-194b-31c1-adb8-7b3528ab1afe | -5.83509 | -46.62257 | 2024-10-25 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README54.md)
