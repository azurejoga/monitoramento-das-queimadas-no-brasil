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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee21cc1-7739-3bb3-a8ef-7fd6e470f097 | -9.73867 | -65.01561 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d360820b-4db2-30a1-9947-e5c397f1c639 | -11.08942 | -51.43005 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 53952f37-5e7d-3476-aa98-e28f3bc53ddc | -9.96918 | -50.29662 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a58c3a14-f358-3656-a18c-565cce3d7eae | -9.27101 | -59.42142 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82090b87-9d07-33f7-9441-c7fc67e746d4 | -8.43736 | -55.63251 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33e736a4-05f6-3d74-902c-07af01bb370f | -11.41358 | -50.73808 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c73f120-8bc8-3c46-8552-6be701b1170b | -11.78962 | -50.54593 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bae919b-43cf-3569-805c-60cce876c906 | -10.33517 | -54.32544 | 2025-09-13 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f1554d21-e2b6-37ae-b226-8f307ede19c0 | -11.85528 | -50.57202 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d502026-2e7c-342b-9f4c-113b4ef89220 | -11.07598 | -51.42992 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b91fa6a2-d23c-3102-af7f-ae48cddad930 | -10.5311 | -51.54692 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd17c04-229a-30f4-b0e7-b01670503ec5 | -11.13739 | -50.70016 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 00fce633-110c-36cf-9f91-8d6fce7c601a | -8.9299 | -62.11324 | 2025-09-13 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6589ae12-fc2b-31ad-bed9-a13f2ee73375 | -9.88887 | -58.3315 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd94943-0451-350a-b2a8-a64368b5cb26 | -11.10416 | -51.45201 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c465bfd-5cb1-3d7c-9127-e1e9f16df40b | -3.44423 | -59.57182 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 053332e1-25a4-3927-84d5-9092004819ad | -11.18955 | -51.41909 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d8b86350-07f7-3f09-8054-a9d9b92d307e | -11.14937 | -50.70171 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e8a202be-45b2-3902-889f-3f8a0439d8f4 | -11.86137 | -50.57279 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a4f08ee-28be-3391-8bba-61afb7f60f74 | -11.10848 | -51.41651 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc57fbc-e8b6-3d54-ab00-33a623e91a00 | -11.0973 | -51.44466 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| abc7e659-8b12-3ca9-b893-d597a0f0122f | -9.97075 | -50.29572 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1eeed5e-0340-3c86-a144-59a4115b62e5 | -10.09585 | -59.1575 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a522fb0b-d677-3a40-97a7-fb7f40b33df4 | -10.78308 | -50.54237 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6884ce3-d487-3307-a3b4-4809f37b77a5 | -9.52503 | -54.63631 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 08e3d236-955b-3ce8-9244-688beddadba8 | -11.15101 | -50.68844 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d5c9a756-458b-3d70-b71c-0d3a7b8e1855 | -11.15967 | -51.37892 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acb5ccbb-9811-3179-9510-b7bc8183c791 | -7.97231 | -55.3073 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b0feea-005a-30db-a62d-b75be038cf9d | -10.52551 | -51.54589 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c910a8a9-1502-32c0-a93b-12478cb0061a | -9.26929 | -59.40973 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 7e01087b-5ab5-39df-9d3b-e731fd445a4b | -11.17861 | -51.41364 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7c16da50-dbbc-3576-8607-e84bcf52b6cd | -9.27555 | -59.39164 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2984d96-f8a4-32fa-b411-1fa901506ffc | -10.34313 | -48.82547 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9b80c21-773d-3788-9981-8cbf1dcc7c90 | -9.36664 | -59.48137 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7233f76-c1b4-30c4-b59b-34c2d2c2c050 | -10.42127 | -60.46856 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6644352b-d5c3-329c-9cd6-c576da8cde15 | -11.09893 | -51.44732 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e909f814-281b-3354-b314-6d82ec96e573 | -9.16856 | -60.3098 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ffcecaf-c802-32d4-8b1a-859a125be513 | -9.25616 | -59.4039 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24971f83-ac84-3701-a516-d21d03140d9d | -11.41851 | -50.74773 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9479e239-423f-3ac1-b411-607ed35d1e57 | -9.26414 | -59.3975 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14e9d667-38ca-3955-bd49-9902f63d442f | -11.41252 | -50.74697 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ffc57a0-e59a-3d67-a2e1-184e0b492bb0 | -7.7583 | -61.12722 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 423101e2-f3ab-389c-9ff0-f66dbc3b76f0 | -9.25518 | -57.06727 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| babe3581-1e33-3989-80f5-3cc7adf26896 | -9.10898 | -60.36208 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc65618c-6070-36ca-9cf7-f01c90cff86d | -9.23651 | -51.22524 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dae6c0e-0d1b-3056-9745-89cc8e6bb9c2 | -9.24337 | -51.26096 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7d55f1b0-85f0-39e3-85d0-d75f3f7c9e6d | -11.0956 | -51.42688 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1da38771-e31e-3aad-aa08-7412cf3e5d55 | -9.16631 | -60.30218 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a51892f-f420-336a-ae22-52279f729f40 | -11.82694 | -50.54958 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 994fd4c7-7770-3df0-93d7-743b24a57bfc | -8.43331 | -55.63132 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc334b22-35f4-3992-900d-2ee8c819caf7 | -11.56332 | -50.57038 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0b09bdc-592d-382d-b815-2fcf850d7838 | -11.16025 | -50.71207 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22dec4ed-19a5-3518-9139-92724bcabfb1 | -9.26816 | -59.41717 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe70cdd4-4d55-379b-982e-fa65cffd08ff | -9.16687 | -60.29864 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e628c59-be9f-3411-b7f2-cfd2375a54f0 | -10.52597 | -51.54233 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d062a18c-c2c6-3f11-aeea-ed935acf13bd | -9.52627 | -54.62729 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dd836316-d484-3f59-940d-e3627015df26 | -11.57602 | -50.56733 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9a976e57-9c03-3db2-9952-2e6a5ca08869 | -11.8203 | -50.55344 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6b0367b2-afc9-31b5-acf1-b372ab99c454 | -9.27441 | -59.39911 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a0c3e97-36c1-313d-8560-b3bc9b8da4e9 | -11.11156 | -51.33373 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 44116a7d-b185-3fea-b45d-ab57c4673977 | -9.83683 | -54.53043 | 2025-09-13 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51fcd36f-48b7-3749-add9-362301bc1f26 | -9.74356 | -65.01508 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be8c1e80-1c3c-3b51-a5cf-9d01ee900bb2 | -10.70196 | -48.65863 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f6175da-d9f1-30a0-bdab-13e6738a667a | -9.51661 | -54.63089 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f3184827-b20a-3988-b6af-0b27d43bebf0 | -9.26985 | -59.40602 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d9491dc5-13ac-3631-88c5-a66ea10bacd5 | -9.2767 | -59.40708 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e84d508d-ff11-3be5-8bbc-d060b7105211 | -9.50293 | -55.96094 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a0c245f-59fe-3c49-baf7-1db9378104af | 0.6915 | -50.65439 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 97f60590-2cef-3663-b862-b722074999e5 | -11.12541 | -50.69863 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce393c14-25fb-3c8d-bd7a-15e5a3fd8aac | -10.35224 | -50.50925 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e90878a-76fc-32fb-96b5-60cec1ac392a | -8.10058 | -50.17923 | 2025-09-13 05:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88c715b5-9779-3809-84a6-eacb9cd4dacc | -9.23261 | -51.2555 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b456c782-eeee-3b02-9c89-cc05aa413259 | -11.19613 | -51.41968 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b02cdf28-7688-3b3c-b5b9-1682a32b1ac3 | -10.09816 | -59.16573 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d41bbfc-ac33-3ff3-a7db-c75712092b10 | -8.43271 | -55.63549 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f706562d-6f80-3813-bce8-5596229cb6a7 | -10.09933 | -59.15803 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 389c1f48-4fc1-3cbe-918e-6a8130dbb038 | -9.82261 | -65.16154 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f9b4e4c-b0ee-389c-a7b3-5e4e0448282f | -9.30222 | -65.59397 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e67bbe50-75ab-3e27-b4bd-2342f86e851d | -7.53918 | -52.5155 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc620178-28d7-38f7-a8c0-35d2ae3e698a | -11.85636 | -50.56275 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6335e77a-e290-3cd8-a7db-536f31fc244c | -4.93432 | -55.78928 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78647fc8-56bf-31a0-8cd0-41e92532c673 | -11.38842 | -50.47509 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87bdbfe7-0674-39c2-8d5f-4a44b30e16f1 | -4.92405 | -55.7748 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34befaa-01db-36ab-8eca-e991852ef2d5 | -9.8099 | -48.89394 | 2025-09-13 05:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd77daba-24c0-33dc-a6a7-8cb5529f9d01 | -10.50468 | -51.5298 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a86f70b1-524b-3aa5-b946-a9954f231fd5 | -10.54637 | -57.08669 | 2025-09-13 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84f64f8-3769-341e-ac70-a1a37cfd870b | -9.13713 | -60.5329 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5137d50c-f2c7-34b6-a3c8-b7569391a88a | -9.27215 | -59.41398 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 092bd8ef-f2b7-3a85-be98-2be67f59b52a | -11.19578 | -51.41587 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c816becd-51c0-3d63-a653-3e07cdc5b3ff | -11.07752 | -51.43249 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 10b5d09f-a0fa-3cf0-9296-efaba3932be3 | -11.86856 | -50.56431 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15e30a0d-ce7d-3160-b6f2-ffdcd9213d77 | -10.76291 | -50.52331 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f397ed91-83b2-3cd1-8d39-64c12b290ec5 | -10.33582 | -54.32062 | 2025-09-13 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ba7a1a3-25a4-3427-a760-757ec86ee446 | -10.09874 | -59.1619 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 162d00a7-12b1-3ec3-a640-75800fa6877f | -9.27962 | -56.89556 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a50c89-cdea-3db4-9cd9-081061e46bb6 | -11.57437 | -50.58108 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3444464c-6925-3826-9770-2105827f26ba | -11.839 | -50.54738 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37fe50bf-2e99-3bdf-9538-a6263d61925b | -9.82315 | -62.33101 | 2025-09-13 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a1b79a6-6581-366f-be50-7c8ef0075448 | -7.81577 | -63.57857 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 924a2ecd-9c20-3603-9aae-eaed1edb9396 | -7.86911 | -61.15562 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README106.md)
