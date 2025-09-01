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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c256a5c-b7ad-30d8-84c0-c2321a22ceff | -9.45729 | -62.35817 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4c474c-7316-3a2e-bd05-ede02764d1cd | -7.70119 | -61.4794 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2525b93f-9ba0-3e93-b9da-0ae2d9279b84 | -7.07718 | -63.07034 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3a315e4-0423-3456-bc52-6aabd228725b | -9.8771 | -65.01132 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82e78716-231b-38cc-8d2f-bce2e46d07b3 | -9.83672 | -65.0494 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c27d7ff-8f91-3081-8869-a3a6db18831b | -8.6538 | -62.9193 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6d43969-3ff5-3053-b0b7-0d076ae88f41 | -4.09146 | -55.80955 | 2025-09-01 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a20a6893-5b26-33ca-be1a-dd94464790a1 | -6.96773 | -71.74583 | 2025-09-01 05:23:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e68c019-3c3a-3b80-b5ec-061f935504bd | -9.84056 | -65.05186 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed8befa5-52da-3952-91cd-540a3b22462e | -9.43941 | -60.53869 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28248cd1-8e91-3893-9b52-96b6bca97df1 | -9.44836 | -60.56899 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2475b14-5752-3a7b-9bad-6bec2e74f5ad | -9.93217 | -51.61033 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 307b99cd-0288-34ba-8817-8dba6fd1669d | -9.01111 | -65.69366 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0342f943-7906-3cf5-bf0f-68fd5e288f7b | -8.85322 | -70.62518 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ea695a-7757-301a-aef2-26a6740422be | -8.73265 | -62.40164 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 879fa64a-9379-366a-ab6a-f1fe6ecd1eea | -7.28579 | -60.6573 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68569417-cc56-3812-85dc-d2f682061bff | -8.97765 | -65.96227 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6624a07c-639d-339c-af0a-e06e18018187 | -8.73152 | -62.40876 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2f200b-bb2d-39f7-8cad-171a040d6de9 | -8.72256 | -62.42197 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97b6a99c-511b-3c20-bba8-64baf09c4505 | -8.09216 | -70.22309 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22fc203d-7b05-3c30-90e4-ab27390111a9 | -11.83736 | -51.47454 | 2025-09-01 05:23:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46b9cc08-8ddc-3ecb-bf9b-ca4a4d5fd46a | -9.13005 | -65.84664 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef7afba6-0b54-31a7-a5fa-61315710d9f7 | -9.84039 | -65.05001 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 966ae8df-1f75-326f-aa1e-29b433a8c3f7 | -7.535 | -63.85241 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbf3298b-61eb-38f1-8f73-3be42880a6f0 | -8.73821 | -62.4098 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18fba928-2b16-3f0d-9897-349953117d6e | -8.6134 | -62.58829 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b54513-2de3-3cd7-bac7-8f979e7d96f6 | -8.96503 | -65.96534 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5d30ac1-41c6-3349-b694-90d7ac138197 | -7.56046 | -60.87805 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cec0c9f-049f-3741-8aa9-76e7e3de3097 | -8.72874 | -62.40467 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf51645-7eea-36b5-a7a3-6b227ace6093 | -9.12107 | -65.73441 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9398c29-935a-3cfd-ae81-b657a4b285a9 | -8.78987 | -62.93007 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fdf99a3-7118-3905-9808-0f7b9a1400d5 | -8.62685 | -62.59047 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c988c353-e104-3c3a-af35-cc7a07ff62ba | -8.74212 | -62.40678 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c3491d8-9598-3333-8ffb-6efbe0596dc3 | -8.76698 | -61.42917 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c7a77b6-67f9-38d0-8209-05bdfaeecab9 | -8.85017 | -47.51014 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 954019eb-9ab5-3357-bafa-77914b2c6ee3 | -7.46442 | -70.13602 | 2025-09-01 05:23:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a7d972f-6de1-3a7f-a620-1367ba95e81b | -8.60142 | -62.56438 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 035f1f49-5f77-32c1-bbd8-1262b31f6b68 | -9.13947 | -65.83808 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 371d0fdf-5797-3c31-8eed-2e4655c7e192 | -9.83394 | -65.04625 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c563794-8314-31a5-86d1-153c3e614212 | -9.23007 | -60.26343 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b43645e-f87a-3a81-9764-b04ff913745a | -7.07779 | -63.06654 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f700cb6d-3476-3df9-8198-580a3a80cc63 | -7.07028 | -63.06923 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af6e02d-dbee-368b-8875-44ca9c1b7f18 | -8.24361 | -72.82219 | 2025-09-01 05:23:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e16e1ad9-4700-3d29-901c-7061dbfe2798 | -8.65941 | -62.92776 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d2ec971-53c7-3aa2-831e-fdf93e922fc0 | -1.42157 | -48.38874 | 2025-09-01 05:23:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09ff273c-762d-3163-9160-55a3372d9efc | -7.62265 | -62.71659 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 991b9b9c-fcd0-308d-9c8b-0864787b96ff | -7.69971 | -61.09846 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7ac9a3-cde9-300f-874d-d3c10a12e4a4 | -9.45678 | -62.33994 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e47b9a1-2111-3328-a45a-b0d75f431685 | -7.93294 | -63.0129 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928a61c7-a08b-3211-8094-1b6ce4aab630 | -8.51949 | -72.69683 | 2025-09-01 05:23:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86e70b11-af2a-3d2f-907d-f926ca72c23b | -9.88664 | -65.02184 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84a2664f-edef-38e0-be24-d61955dfda42 | -7.08672 | -63.03295 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 395b7214-b014-3da6-a750-a4dcc43fd8ba | -8.6611 | -62.92395 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e6d43d1-293d-3cfe-8cee-bda758492232 | -8.86264 | -63.02442 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ed3e91-a758-3b2b-a77f-04a6a06c4621 | -8.69693 | -62.41053 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdabc54c-1f5f-36aa-bb73-49c4290981d4 | -10.04586 | -48.09167 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fcbef9ea-d81d-3419-9298-a2fffafdc482 | -9.23061 | -60.25987 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf7d440-595b-3be3-96f2-f01a803e8d23 | -8.84514 | -64.1443 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 009a0fc9-f083-3cfa-bf88-33e852786776 | -9.45402 | -62.33586 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b8d676-b599-323e-b19d-343a4964f535 | -7.06683 | -63.06868 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5477627b-8a22-3740-b49a-0e22bba192a6 | -8.70305 | -62.41519 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16f6dc2b-2229-3b09-9ea3-f2474cd03bd6 | -9.44116 | -60.57148 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 993adcf8-2ac4-3a9b-ada0-da2181e9f96a | -10.23821 | -51.11149 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6a743bdd-8ef9-3283-8ca8-8037e79146cc | -10.23871 | -51.10733 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e7d2c5d-6117-3eb1-b2f0-dc37d86a5bab | -9.30499 | -64.54603 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c09d2df-dbe7-3f4b-b6cb-07f63e7ed728 | -9.11467 | -61.20726 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f91f75ba-b54c-3d5f-b0f3-e9ad8478d2f2 | -4.15426 | -46.78854 | 2025-09-01 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 538ae809-f028-3e08-888b-befca2898d47 | -9.13559 | -65.83742 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b699020f-f785-33ac-8886-b14cfe0cbb4f | -7.7045 | -61.47993 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b1d58c2-a496-39b7-95fb-c9d95fcbbf51 | -10.04356 | -48.11115 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a47377dd-90f3-3d43-ba10-ebd04ca706bf | -8.74804 | -62.40762 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f9356d-a3ca-3d7c-b08b-a67de17edbc9 | -9.34436 | -65.42339 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f731c43d-2aa2-39f9-adac-5ecea19ac523 | -8.69636 | -62.4141 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2b90a50-d1be-3258-8482-7c323aa77745 | -8.71978 | -62.41786 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a60976f2-4506-3726-9098-7cd119629013 | -10.3735 | -52.29113 | 2025-09-01 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7364454-dd27-3c57-ba6e-dd90c42b5cf9 | -8.34704 | -62.93031 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc8729ad-6fec-32d5-ab6e-5e7ecbd6d641 | -8.73934 | -62.4027 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aef3081b-7a68-3d5a-ab14-d5c1bdc10b23 | -9.07045 | -65.43454 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a0eb46a-a105-3bdf-8ef4-a2c5b6a3787c | -8.74918 | -62.40051 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fe2220f-87ef-32cc-81a7-736267ae1403 | -3.63659 | -49.20674 | 2025-09-01 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6afdffcc-6108-3ca3-b205-06347c9d4422 | -8.62071 | -62.58577 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6067c8f-0a42-3ebd-ae57-c8a44b74c5d8 | -8.65602 | -62.92719 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5a64937-1b3d-3aea-a9be-a83790ca2521 | -8.34644 | -62.934 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11c4acd0-0bff-3402-9f5c-2d79536f42b6 | -11.07648 | -52.06722 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b44f4d3a-4007-3cfd-80be-62b60ad20b28 | -8.2265 | -62.93763 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd27e14a-05c1-382e-8376-f1fdf1928707 | -7.68097 | -61.08842 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c37d8cc-0fc4-3b0e-8396-7421953f7741 | -11.07716 | -52.05864 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea7a5090-5f31-3b3b-ad52-586ea959d898 | -9.44395 | -60.57551 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5505b634-cd7a-3014-bc99-c08fad7cd04e | -8.50881 | -67.12749 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb22736d-9688-338e-9d33-fc818f5b4aa9 | -9.17084 | -67.71489 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d72247f-8542-3ad2-9a0b-33ec31d32742 | -7.73767 | -61.57073 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3553fdb4-c598-395f-a52b-544e6a026ae6 | -7.06237 | -63.05238 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 250836c5-2ad3-3a9a-99a3-1dcb7d57a81b | -8.6566 | -62.92352 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 626fbbdd-84e7-3c4c-afc0-fbfb4e0ab550 | -9.14092 | -60.92993 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e7ae67c-3659-32b3-bf34-7298ff9e98e3 | -7.0999 | -63.03894 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd150247-cf36-36dc-92f4-0391a25cc5c9 | -7.45558 | -63.16144 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75145425-40fc-30cb-b137-09dd9cc7da9e | -8.71922 | -62.42142 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc579c25-cc38-3854-9d93-8c7bbe33b3ca | -10.24925 | -51.11552 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bc3e4ee-23f4-3dc3-bc47-a9513573b889 | -8.14967 | -62.7823 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c57f2d2-c6a0-359a-80a5-2b130d398246 | -7.09508 | -63.13577 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README79.md)
