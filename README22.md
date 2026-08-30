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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46353eef-f0cc-3bd9-84ae-85ee19b4c76d | -6.86854 | -41.67509 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 395a8e48-ffc1-32ef-882f-3c3b14cc07a1 | -6.28747 | -37.67791 | 2026-08-30 03:36:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f0c17f44-dc0a-377d-a3b8-e4199207936a | -4.97605 | -37.23851 | 2026-08-30 03:36:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ed2616f4-3df8-3f12-9563-3117e76038ab | -6.04446 | -35.2133 | 2026-08-30 03:36:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 800dd14b-0846-34e2-a9f9-4cf8dc280259 | -6.86729 | -41.67252 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6cbdca81-5269-3f50-b5ae-da72142df4b9 | -7.21783 | -42.75803 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd5ff5b1-83e3-3486-976b-24b187109ca0 | -7.10445 | -42.22048 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88bb1e20-aab0-3133-a6fe-98f5a0e8c059 | -6.92001 | -44.95259 | 2026-08-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96d4ce56-4367-308d-a1ad-92d82c2b4dd9 | -5.49924 | -40.77887 | 2026-08-30 03:36:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fdd891b0-ace5-3755-b9cb-3328be4d24df | -7.04673 | -42.19858 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89e4fb90-f353-3efc-8805-16b7d646bb10 | -6.3435 | -44.09951 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c4932821-ffb5-3345-8193-963506d08078 | -4.85777 | -42.94853 | 2026-08-30 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c44446b-996c-3493-a56a-26e19da07063 | -6.2837 | -37.67729 | 2026-08-30 03:36:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6deb81a7-9238-3af9-9bdd-ff1c2bdb7cfc | -1.99831 | -44.80368 | 2026-08-30 03:36:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4bb9eae-50b3-3e59-ad44-98dd7f47bcfc | -7.18085 | -43.71633 | 2026-08-30 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4a07dfd-e528-3ea6-b3e1-c6ec67c559d3 | -8.09795 | -40.07384 | 2026-08-30 03:36:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7f0fbc3b-4c9c-334f-91a5-89000c97802e | -6.87045 | -41.66383 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 02b2069e-e739-3c06-9e75-1697c000fa1a | -7.05124 | -42.20234 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4f90760-b7d1-3405-a4dc-870923f95834 | -6.92513 | -42.67542 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 045484ca-7bda-36bf-9043-4ad90893fe9a | -7.10968 | -42.19135 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b04988f6-de81-3a10-9d52-a7f2d71f5e26 | -6.83045 | -42.87227 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 87c4a6b6-9195-30d7-b5cd-93c41b8b0248 | -7.11 | -42.19135 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e0ad062d-b7be-3b77-8f16-c4439b4da9a6 | -6.04785 | -35.21383 | 2026-08-30 03:36:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 472a0b00-cc05-3f0e-98ad-c2daee8c3eb7 | -6.34833 | -44.10131 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4e7a5a39-1f6e-31b8-95ce-8871b9a9861a | -6.91384 | -41.63532 | 2026-08-30 03:36:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 80574961-f58a-3137-9dae-e9ace3c3795d | -4.86265 | -42.95295 | 2026-08-30 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f1e2cc7-44fd-3bb7-9805-28d449a8049d | -6.34425 | -44.09542 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afe7f792-e59b-345c-874d-0983d20d0bd2 | -7.04723 | -42.19573 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 579cd168-2fd6-33ae-87e3-69c0d27b3013 | -6.86557 | -41.66314 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c1ca5693-6f21-3fbf-b0bc-49321f26213a | -7.07936 | -42.21915 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2748cc2f-993d-3fbc-96ab-ced490665ee2 | -6.34993 | -44.09683 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 520b9b5b-79a5-36dc-9996-6313a62878c7 | -6.34903 | -44.09729 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a2c918d-d4f1-3768-b30c-4f29c25f6112 | -6.3492 | -44.10082 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 753d61c5-e8b9-30cb-bdd8-28786bb30936 | -6.87318 | -41.66756 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1cb4bbd8-1f06-3432-afee-1c8f0c687b11 | -6.34333 | -44.09592 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b59bc865-a567-3154-843c-a72b165df1f3 | -6.86631 | -41.67801 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4ebeb610-5050-3202-a356-ac531e556f05 | -7.2094 | -44.01977 | 2026-08-30 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48209b3a-3b80-3987-ba8f-dfd635963c2b | -6.86829 | -41.66688 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fa35e12b-c3bf-3eb5-b732-0aad4a621f2d | -6.88249 | -42.88229 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5bbed51-f110-3183-89f8-bb869e7d5430 | -6.86655 | -41.65739 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a70f423e-5bc4-38e2-867f-656b474327af | -6.9199 | -42.6747 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea2a6022-6dd0-314d-9fe7-8878e33c701e | -7.04623 | -42.20143 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2fbda322-ec36-37aa-b7e6-b253a1f46baf | -7.21293 | -44.01653 | 2026-08-30 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a32e3655-8c5f-3f44-990d-94837ff6661f | -7.21838 | -42.75489 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3995692-b2d3-3e22-a3b0-2375429a3f10 | -5.76647 | -35.7459 | 2026-08-30 03:36:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc8d38d4-7913-354f-a86c-bd1ea2eb0189 | -4.86325 | -42.94942 | 2026-08-30 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca602c89-0fb9-3561-aa99-b89e53e948f1 | -4.08465 | -45.94162 | 2026-08-30 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe8621ca-f412-34df-ba35-5b186d785929 | -2.00561 | -44.79955 | 2026-08-30 03:36:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e046526b-ec93-3f7f-9ef0-dd3dfb36702b | -7.1253 | -42.76081 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a6be1ac-0f2b-3cf1-8d18-02d64f308414 | -4.08055 | -45.94529 | 2026-08-30 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2edb5a7f-b415-37f2-a082-844bcb28d4c3 | -7.12602 | -42.76168 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91e8dc7b-62cc-332f-a50d-08569d2278f6 | -7.10653 | -42.21158 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af2227a7-e698-35cd-9d2e-a66f61e60ea8 | -2.93898 | -41.73548 | 2026-08-30 03:36:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c26f805-c1e6-3acb-8a85-1b7786fbcb9e | -5.77438 | -44.20115 | 2026-08-30 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 541a0cab-c6b4-38be-b01f-a1a37e2e6c4f | -7.25272 | -39.31213 | 2026-08-30 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6ac6fef-8d30-338b-992a-0bdd762dc1f1 | -7.18562 | -43.71851 | 2026-08-30 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baaf6397-2a56-3663-a2d7-436b9993002a | -6.87418 | -41.66194 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 995934e8-3aa6-3a5a-80c5-b8889ecefa98 | -7.20961 | -42.74376 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6c3a721b-4167-3dd1-923e-9a37419f9569 | -6.34261 | -44.10005 | 2026-08-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2fb01d0f-02ed-339c-b800-fe4b3b630ef8 | -7.21728 | -42.76118 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08c53c32-857b-389f-aecb-53122fe4e347 | -2.00474 | -44.80477 | 2026-08-30 03:36:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51500df7-c086-39fc-a338-76f33bb66d39 | -6.82985 | -42.87563 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 22a66d60-5dd1-36e5-9ef3-dc480636fc79 | -2.88705 | -40.4605 | 2026-08-30 03:36:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5b199bb1-5463-3761-b5d1-6f2fe6c865ca | -6.06725 | -44.87923 | 2026-08-30 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b72b8878-3a83-30c1-9bb9-83956c33611e | -6.86271 | -41.67991 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| bec779e7-b3f1-3a0a-a268-806992ead4b4 | -7.10605 | -42.21154 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b95c456-186f-3776-8ccd-6002d24cfc9a | -5.5058 | -44.62176 | 2026-08-30 03:36:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 820dfd82-2e59-3c9d-b921-63408459d9f2 | -6.87663 | -42.88464 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a1881010-d107-31d2-b183-19f1ed41ea1c | -6.92417 | -42.6746 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 63cb6523-8429-36ee-9324-46c478c95f8b | -7.21224 | -44.0204 | 2026-08-30 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79846290-4fa7-3aa9-b373-6ef80fc5519a | -6.82926 | -42.87899 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f10e2283-e9e5-3034-bfc5-6d70f57d5be0 | -5.31756 | -45.25847 | 2026-08-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 920e3aed-1690-3557-a6e4-c312e0df4b17 | -5.507 | -44.62458 | 2026-08-30 03:36:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a094d153-f4d5-312b-aeb1-1e07d29c7e64 | -6.872 | -42.88316 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a83074a0-de3b-37ea-900c-ffb19d3cdb0e | -7.21373 | -42.75082 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30506144-0f68-3dad-a0c5-2b9ef3f38c5f | -4.86857 | -37.4484 | 2026-08-30 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 851b7f2e-ba9f-32b3-a841-79efcaf5ac2a | -7.06037 | -42.1503 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5745720-e3e1-3f25-afaa-29fea6593a63 | -6.87667 | -42.88759 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f197fd4-c731-3de6-a410-dd0b5b91ec29 | -7.12476 | -42.76394 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0311360c-1599-3152-bd42-ea9d503ee82d | -7.10499 | -42.22053 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12cf10df-4d3a-3bbf-9b23-a906cfd7a0ac | -6.8646 | -41.66883 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| efe551f7-c6b0-32a7-962c-ea36c6d13523 | -5.50502 | -44.62624 | 2026-08-30 03:36:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87a4cb59-020a-383a-aa4e-06dd0caed5da | -7.1802 | -43.72001 | 2026-08-30 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c179a1f5-2f30-365b-b635-f6a9b0e23bc4 | -4.07695 | -45.9462 | 2026-08-30 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ad07b8b-2030-3bf9-a880-f97e46e9754f | -7.11049 | -42.18849 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d341343-8510-3fb9-b2fe-167ce9738a24 | -6.33477 | -38.97874 | 2026-08-30 03:36:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5205b63-263d-3c3f-8948-f71e27055bc5 | -6.86948 | -41.66953 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4cf15343-000c-30a0-8def-1b874e0dd185 | -6.86931 | -41.66119 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9bf0bfae-dbac-3240-ae4c-ecc8c079744a | -4.08361 | -45.94748 | 2026-08-30 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09ee0128-033a-30ee-b4ec-11b7593ae5a8 | -6.92365 | -42.67765 | 2026-08-30 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 21fce389-76c0-3d0e-ba6f-0689d68861c3 | -7.10548 | -42.18757 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b41bbc7-0aab-3aee-a1d1-013508f88ce7 | -7.08438 | -42.22004 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ec1438c-075e-35ad-9274-1a9c25723eba | -7.06539 | -42.1511 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb313513-c29c-3847-bb8b-286c67e43cdd | -7.11019 | -42.1885 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c1b485b-df06-30d5-8c43-74474c3c4735 | -6.86365 | -41.67439 | 2026-08-30 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a784f827-f50d-3c3c-a7ca-6407884e35e6 | -6.87603 | -42.88799 | 2026-08-30 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1b44de5-4ade-3d9e-bb84-577e90d72987 | -6.9129 | -41.64065 | 2026-08-30 03:36:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab2ad9f8-eed1-384f-b186-8a703e14355b | -7.10113 | -45.7677 | 2026-08-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24f3ed42-1736-3f5b-b019-52705ce23725 | -7.07885 | -42.22211 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a00582c2-3c64-3bcf-8141-639339289b26 | -11.51622 | -45.5415 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |


[Clique aqui para ver as próximas entradas](README23.md)
