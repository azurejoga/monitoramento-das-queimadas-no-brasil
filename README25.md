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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b6c2f1e-38fe-3a79-8f64-1e9f094a0cb4 | -4.68166 | -44.59161 | 2024-10-21 04:12:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b9b8afe-9329-3fc1-b717-3abaf14ceef2 | -4.66909 | -50.63068 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a03370b-0cdb-3e30-a186-c6281c4a522c | -4.66815 | -50.63622 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 674dd4e5-dacb-3deb-bc95-0eb26d2bfefe | -4.66764 | -45.70655 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23545ff2-6bc6-3a63-99c6-972da8c761ec | -4.66402 | -45.70601 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6af18a8e-58be-3a97-8211-ffcc6512cfac | -4.66186 | -50.94678 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74d60fdb-c840-3b69-ba51-8832a9ea7589 | -4.66137 | -50.94972 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28152646-b67f-33c7-a985-00608b8d5312 | -4.66087 | -50.95267 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 009d08c0-79e2-304d-a3a9-0edce3b095cd | -4.6568 | -50.94587 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffca11b7-d18a-3abe-9274-cf6d84a7e541 | -4.6563 | -50.94886 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8beb84af-03bc-3cba-8ac6-5faed4adde9b | -4.63756 | -50.93634 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0ee174e-d6cd-315f-a70b-8fd77bde02f6 | -4.63707 | -50.93923 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07f05393-d963-343d-83af-e321247b1837 | -4.63247 | -50.93564 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaf0102e-67d2-3ad3-a6f1-0f6ade473900 | -4.63197 | -50.93851 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 744da64d-eb28-301c-be10-0a4c4803a3f8 | -4.62443 | -46.06939 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdb2b19c-1f44-3c6d-ae88-0c87af254377 | -4.62375 | -46.0736 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c3827d0-9b98-3ca4-8ff0-ebc7924f602e | -4.62074 | -46.06883 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e788ecf5-a079-3e35-8c97-ba9e5f833d89 | -4.62006 | -46.07305 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93f966c2-b8b6-38c0-816a-32f0715ff8ea | -4.61254 | -50.66626 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9f811c-2bbb-37d3-98d1-e02264ceadfb | -4.61163 | -50.67173 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9c028f3-a31e-3df5-9364-528c4e7c8f08 | -4.61076 | -45.64635 | 2024-10-21 04:12:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d3c7a19-6944-3b14-b0b9-295ca3011840 | -4.57762 | -49.50118 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1b7612e-7600-3cde-be78-a7ffd0ece6ab | -4.56917 | -50.95701 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30ccd4cf-1a59-31d7-a7d0-c09e7c2ad8f2 | -4.56869 | -50.95991 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4488194c-2a2f-33f4-b846-7308f3e8f22b | -4.56819 | -50.96288 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e20b6d1-14be-3eb5-af0a-c4a2642283c6 | -4.56357 | -50.9593 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e20e5d5-c8c1-31d7-a703-1c8e8c654498 | -4.49772 | -46.06879 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2bbe024-618b-347d-a181-c3badc7a58c8 | -4.4488 | -46.44418 | 2024-10-21 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 445fd692-ee8e-34f3-a40d-ab1a3ff452db | -4.44501 | -46.44364 | 2024-10-21 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecf86111-9563-3217-a7d8-daa991fe187f | -4.44427 | -46.44823 | 2024-10-21 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77a319b-53fe-3d43-a982-5cc907f33474 | -4.4255 | -49.79897 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0c453c5-1630-3410-ae89-89016d92d7b8 | -4.42421 | -50.93344 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc72db3a-da39-3190-a371-2b74bfa1bc60 | -4.4237 | -50.93644 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8349581-ea2c-3087-992f-837f7d08e614 | -4.4208 | -49.79815 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| caf489c3-637a-3011-9e58-93bcde21de9d | -4.41119 | -50.52959 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e6a3a14-1178-3242-91c3-aad3c6c9551d | -4.38688 | -45.80692 | 2024-10-21 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db49bd55-64b8-3902-af7b-bbbc8534b9f6 | -4.38323 | -45.80638 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54b45d8b-a972-304b-8040-ee37a74dcaec | -4.38157 | -46.11873 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a4cd493-9050-3896-b401-771d7b34cef9 | -4.37786 | -46.11814 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68dac634-c998-39fa-b9c7-849d5e5dbd0f | -4.36389 | -48.48046 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b085ffbe-8e0b-377e-8e96-ef936176b1aa | -4.36214 | -48.47839 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6471b9e-af2f-3333-bbe0-7f2b1f833e6d | -4.36148 | -48.4825 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d66d4a4-b608-37df-9abf-07a2ea97a42d | -4.35957 | -48.47982 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30703de1-657b-3986-937c-b90ddc71f2c2 | -4.34171 | -48.71843 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 507d79b2-c07a-310e-b606-aa2d8a377fad | -4.33802 | -48.71359 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3c8221f-ad69-3173-a92a-53246876e30a | -4.32165 | -46.00845 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7628fdb4-158d-36a6-8eeb-1a323dfaf24b | -4.31796 | -46.00789 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb8fc533-7d66-3376-8a57-09a3dbe7a057 | -4.31214 | -45.80949 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc141ea5-e124-3449-a52b-79cef6f49c90 | -4.30848 | -45.80896 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b85ad1f9-64db-371b-9611-dcfec38cfac3 | -4.29204 | -51.05229 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2e62932-5afa-37f8-8945-491e40ec8bac | -4.28742 | -51.04834 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f3b08b-ddd1-3129-95d9-6e2f44b7aa23 | -4.2869 | -51.05142 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ca9c0d3-8e98-3e93-bf9d-8db1d7d750b2 | -4.28654 | -44.51104 | 2024-10-21 04:12:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bfbcb455-9c8e-3c1d-b5a5-476bab6626ee | -4.28594 | -44.51477 | 2024-10-21 04:12:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e836d083-e2b4-3791-934b-f6d05e8f229d | -4.28221 | -49.98589 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c524994-479f-3c6b-88fc-e5d6f194224f | -4.25865 | -50.98983 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c24f072-09f7-3af3-a42d-ad7b457a4e0c | -4.25815 | -50.99286 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426175ad-7efb-3c3f-b5ce-db9e320ac3d3 | -4.25584 | -50.98656 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2117fb9-9979-334e-81cb-51c4fb373b09 | -4.25531 | -50.98956 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6953ecf0-9fb9-356b-a641-bd06fd353356 | -4.25478 | -50.99263 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d5aa82d-b2d7-3fa6-a037-2606ca69e6c7 | -4.25453 | -50.98293 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55037a07-434b-3c51-9a86-9ad1d0e8e245 | -4.25425 | -50.99571 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f565fe64-0131-321f-b352-0abe1fa44a0c | -4.25405 | -50.98582 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9363269a-c155-3fb2-a86a-b780b166c57d | -4.25356 | -50.98881 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2667b297-4bd1-3a51-988f-6e6d736c185b | -4.25305 | -50.99189 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22cdb5dd-5fbb-3c33-b70c-78412068301a | -4.25254 | -50.99498 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 499c9c61-9e92-3462-9cb9-b4b1f272216a | -4.24897 | -50.98474 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61488e64-cb42-3ad1-8487-68540b8bb3a2 | -4.24848 | -50.98767 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549c1cff-4f4f-3664-b8a8-ed4762327a0a | -4.24797 | -50.99076 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed5aa1c7-58e4-37b2-ba8e-f5378ea29983 | -4.24745 | -50.99387 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51d0c256-4b4c-3820-8eea-594aec5f7e22 | -4.24694 | -50.99697 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c71bc165-a9be-3a75-b03a-5c19005fcf0c | -4.22561 | -50.08817 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff7f7c1-db44-37de-935b-72cd869af0ff | -4.2208 | -50.08729 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8abb660-063f-3602-845f-0d7fc147e8f6 | -4.21521 | -48.55484 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 13ac24f8-c473-31c2-a133-16d0e9b27fba | -4.19244 | -48.58512 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43bfaeef-af84-3703-b8ad-616d85bf196e | -4.1881 | -48.58439 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bbcd41c-c33b-38d0-9a1f-00bfb84586bd | -4.17872 | -48.58714 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 901d51f8-5cbd-32b4-bf52-4109de609b78 | -4.17436 | -48.58652 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8498e9ef-9401-3063-8d8b-8f1be23a9c2b | -4.1443 | -46.4915 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48376962-8092-3bda-8826-db05e95a5b02 | -4.14356 | -46.4962 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad6062e6-6c5b-355d-93e9-a7653e5bc7fe | -4.14306 | -46.49383 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc947f89-d2aa-3173-be9d-8a6e3ebfc445 | -4.14229 | -46.49849 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4adaf8d-77f9-3480-af88-2f6bb502134f | -4.14051 | -46.49086 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 626a83e9-c14e-398d-a755-6ffb07ec760a | -4.13976 | -46.49561 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bdd4ffb-8d8e-336f-b1a8-606590abe067 | -4.13926 | -46.49322 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42599a68-8e66-361f-9978-861b60faa4cc | -4.12548 | -46.86434 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0630eafb-9112-3036-ae51-a423bf0e03e6 | -4.1065 | -48.23967 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecc085b7-d111-318e-b281-4e3fe0449e0c | -4.10402 | -44.23234 | 2024-10-21 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cff2a0a-54a2-3fa7-8f35-36107c7cff71 | -4.10224 | -48.23905 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c96745-3603-3c22-bd1b-ec0a1bea78f3 | -4.10159 | -48.24294 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10047e0f-9577-3417-85e4-d62b2a989bb4 | -4.10119 | -44.22813 | 2024-10-21 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13fb6940-8958-36a4-91ae-4a9e1a4ac383 | -4.1006 | -44.2318 | 2024-10-21 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8653c3b-0dbb-33c6-8547-825da945a0ec | -4.09993 | -46.14524 | 2024-10-21 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f030fad-b952-3abb-9a13-fefcbf97f5f6 | -4.09797 | -48.23848 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c9a149-1109-3834-830e-e47d04cf5036 | -4.09619 | -46.14473 | 2024-10-21 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a596dd92-a247-30de-9880-f95a7f1d400a | -4.06703 | -46.65565 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b99e53e2-c222-39bf-b87d-9f82c710e52a | -4.05225 | -50.9538 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107991b9-6e1a-368c-b32c-544813e5a346 | -4.05156 | -51.01926 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b6e506a-5d74-344f-8a73-56caee9751ca | -4.05103 | -51.02236 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 243c1f60-6f19-3662-b9a4-802ccaabe2cc | -4.04764 | -50.94994 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
