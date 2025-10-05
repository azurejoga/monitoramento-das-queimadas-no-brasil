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
| 34e6e593-fff3-3d3f-be4c-db0548bea770 | -8.60132 | -46.29358 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5529aec-ca79-3932-8def-6a9f6ee48c67 | -13.12249 | -43.84665 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d2e0876e-03c0-3765-ace7-b9a603241ab1 | -7.79489 | -44.53699 | 2025-10-05 03:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3a0afb76-51aa-35c8-a21b-d41d18ba4107 | -7.64657 | -45.42675 | 2025-10-05 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24894a80-913c-3570-b862-123e54688c86 | -10.86446 | -45.41292 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13e39236-91ef-3daa-a488-3112b440cbe7 | -6.9872 | -44.22103 | 2025-10-05 03:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 937bc55b-28aa-3d92-8e5b-63646028ebf0 | -8.89669 | -46.04589 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fca0947-5f48-367c-a0f0-03be5429dfd8 | -9.06718 | -47.01865 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1873c8a3-6a8b-3049-8765-1ad1d5220250 | -9.47236 | -45.53547 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1fa608b-1787-3def-9d43-96ac2217ca35 | -11.83096 | -45.07911 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f7e9681-955c-3835-a911-5280d56d95f9 | -7.72767 | -46.28248 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb2e51bc-6b58-3bc4-b0c7-9085cef985a1 | -9.06083 | -47.01624 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 360a2657-8114-3b0f-865f-82ea608c015f | -10.20778 | -40.55035 | 2025-10-05 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 574c567d-7a53-370a-9e17-fc252cb416ce | -7.78154 | -42.59908 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ff6aaa3-0c16-30d3-b03b-2cb46351e3c3 | -11.82161 | -45.09313 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8489e5f-9f10-3e03-bf3a-3442cd7a3fd9 | -11.48322 | -45.04441 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4a32bb6-78ee-339d-8721-fe81164625c8 | -11.53103 | -47.67369 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21b8d5cb-0a97-3076-99e6-9170e026ba17 | -8.5657 | -46.34681 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 291c93ee-06de-3b1d-8d41-9be8af80f487 | -11.91152 | -46.24184 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 548477c5-6a64-3311-be8a-796eba3acdaf | -8.56999 | -46.36198 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f09a7a5b-65b8-3253-8911-c6c496d8293a | -7.7116 | -42.5617 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9507dca8-f9eb-3f0b-b2e8-68062b44245b | -9.0448 | -47.02058 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 736a6ebe-7480-36c6-afb1-eaded18ad796 | -12.46399 | -45.52504 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b561fa1c-907e-35c4-b03a-9a22bac5a2c6 | -9.37115 | -43.02927 | 2025-10-05 03:34:00 | NPP-375D | VÁRZEA BRANCA | PIAUÍ | Brasil | 2211357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 553d5606-6082-3662-ab76-dc1300c2c55d | -9.29543 | -46.00492 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ff8f0716-64c9-3f25-be71-7e09b202abfa | -10.75673 | -46.61461 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 72ed6969-d271-3de9-a952-aae177346a1e | -10.94291 | -47.09705 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| edb93b91-f910-3e9e-b701-820e7cdb7a0f | -9.90822 | -45.9596 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cb3e0ca9-2ce6-3115-8c0a-0534554bf52c | -7.72474 | -46.28185 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd9a5e57-c435-3dcb-8fdc-ff0603a3e740 | -7.31501 | -45.56414 | 2025-10-05 03:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f43c2e9-5054-3a86-8eab-c7b69c04f366 | -8.56704 | -46.34014 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 567e1203-322d-3366-9e85-968df67e1f32 | -7.23679 | -44.88953 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82ece842-4823-39bf-b884-f4357bba1292 | -11.49841 | -44.98478 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4031f17d-739b-3191-a1e0-3994f580f761 | -13.29393 | -47.57639 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac4837f8-a2e8-3336-86f0-9d8b2f6d14e1 | -8.58407 | -46.365 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e14b70c7-001a-350c-86e4-941060481d6a | -13.85734 | -43.99196 | 2025-10-05 03:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 90e4066e-3677-3464-a7e7-fbc90926a91d | -11.8173 | -45.06276 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f14657db-f1fd-302d-bfa1-1f816aee0b7e | -7.78011 | -42.60703 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0258f45a-66a0-3e3e-ab2c-04d1e6964116 | -9.90957 | -45.96081 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5bc64de3-1dca-3666-80bf-d9ae486f995b | -12.92746 | -47.30585 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2222a65-f08c-3128-a09c-9434180281af | -13.23574 | -47.82549 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 072b5a87-a8b3-3e57-8625-d0540ff3b809 | -8.58194 | -46.31821 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 72c9b69f-fde0-3ddc-9260-057556d96349 | -7.72597 | -46.27544 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 917aa580-5cd7-3bf8-a6bd-352061fa2074 | -9.46723 | -45.54057 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce9ea90d-4392-3d41-beaa-a303658a87e4 | -11.83805 | -45.05594 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 096464e7-cd14-355e-b866-f65be7665367 | -7.72566 | -42.39091 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e4156e9-0cbd-3abd-8a34-2a4d695a6574 | -13.09384 | -47.84873 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec054fe4-a661-33ae-ac64-89b574554556 | -11.82964 | -45.09851 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2651907a-62a4-325b-addf-7325d280ff61 | -11.81636 | -45.05562 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66f03e82-ad17-3327-a054-43533d7b6dc2 | -10.94312 | -47.06036 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 29ed0cc8-2c17-3f8a-a13b-6c6288549079 | -11.86743 | -44.96355 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32488e03-ff28-3add-b3c0-8650fda1e6aa | -10.3936 | -45.3919 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e29c72cc-9892-3921-81ec-a6fb973eda18 | -11.83274 | -45.08281 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ea9399e4-d8ad-3294-8c12-f963d6127bcf | -10.19916 | -45.53313 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c9aa227-d469-39f1-a305-c9b55c32748b | -7.80928 | -42.54297 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d1675ba-78c0-302b-b430-9612bdd9b1f3 | -11.80294 | -46.83017 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 319c1289-d59d-3bc6-9478-71249170a0fa | -7.15487 | -46.08839 | 2025-10-05 03:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7d3f4ac-5b53-3416-8fd4-3d0e37404c36 | -12.08234 | -45.15381 | 2025-10-05 03:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6eed58b-fbd1-313b-a95d-e81b384fd228 | -12.89413 | -47.32593 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5784417-5cff-357b-96ee-5e57515542b8 | -11.43362 | -43.48425 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c8a62d-db15-3716-ade8-ceea7a9f3013 | -12.38533 | -44.45523 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51e59eda-f178-3912-b689-6bc702ad339f | -13.85811 | -43.98811 | 2025-10-05 03:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10036dd3-66c2-3798-a390-2292bdf30957 | -11.71011 | -47.5074 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8769a710-4f9c-385d-ba55-99ef3729416d | -13.32492 | -47.18111 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801b5ab6-248f-3b5a-b59f-cb5338d48012 | -11.70165 | -47.51207 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 510406f1-ba89-340c-93ff-30093ab9b38b | -12.38263 | -44.45272 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d07a44e0-f1db-36f6-aec1-1ff2a282b439 | -9.29438 | -46.01028 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6aa137b5-07f1-36da-8842-283931d4595e | -9.28061 | -46.00799 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad12199d-ad6e-3abe-ba77-ec727188f363 | -11.71242 | -45.35798 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1b0b487-9a91-30e1-8e00-7bbf28838ef3 | -13.85438 | -43.98967 | 2025-10-05 03:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f096893b-ea30-3919-b99d-47074fd29e1b | -8.17082 | -43.34847 | 2025-10-05 03:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0185b275-ed61-3934-bea3-066797a0487d | -13.48153 | -47.28174 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 96c31678-90c9-3766-9b4f-feb9df2f0fc8 | -12.90395 | -47.31403 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24286c45-7f4a-3759-8473-21da658d15a7 | -10.94448 | -47.05377 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef19513e-1a93-343b-939f-54e1ab934d57 | -12.39422 | -44.82901 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b455c4ea-677a-30ea-9b43-026f65adbf4d | -11.01888 | -46.69299 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 21d9a39e-6bc0-3194-9cc5-d27daf9ad47e | -13.30098 | -48.0915 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6cb7c9ef-0bcf-3afc-afb9-11f8e380438a | -10.203 | -40.54942 | 2025-10-05 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d5986faa-ee43-34ec-bbef-8ba0999c5831 | -11.83448 | -45.07397 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6666fe52-6619-398f-be5e-e59a281b340f | -13.44754 | -47.27297 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 936c7a12-0a82-3731-b95c-c7d8ca7ed00b | -13.51576 | -47.2894 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8d08d60-7555-3fe8-bfad-a8b7a6a51d37 | -13.35773 | -47.58577 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90aaf059-4c8b-3323-add0-8001244f13d8 | -11.52192 | -47.68094 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f951b1d-29d0-367e-93a6-94d7a71947ed | -9.26033 | -46.77816 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b60962f7-5783-3aa2-8a50-5654518eb50a | -8.56335 | -46.26348 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40949e74-d340-3396-b548-1ed3514d30da | -8.60415 | -46.27885 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cc3edff8-7f33-3480-8804-b26b936dae6d | -7.77209 | -42.61873 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4be954c2-1ba8-3f66-b9c8-6574ffabf97c | -10.87161 | -45.4108 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcb099e3-1a57-31a7-871a-040ca23c21e7 | -8.60268 | -46.2865 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ade6193d-815a-3509-b660-576ed8d48dcb | -11.02067 | -46.71352 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cdd3774-3f11-311a-8af1-828433abcdbc | -8.59645 | -46.30296 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| fa28bf38-4c19-3c38-a7b6-9f098e8e3228 | -11.82468 | -45.09082 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6841a9da-d271-3b4d-9dc7-4505a8db2f51 | -12.89016 | -47.31068 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56bff0bf-a4d7-35e1-b67b-8cc9b9b222c3 | -7.80042 | -42.56691 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f04f10b-f6df-335a-9f9f-50cb3f17f06f | -11.75994 | -44.74373 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 232e672a-1875-3fa4-a84c-e5e749518ebf | -9.91062 | -45.9557 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8b081cdd-c041-3429-96f8-64ae1904076e | -11.82075 | -45.06576 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3aa31dd-2ddd-319c-95d0-8f0af5d4e3d3 | -14.01426 | -44.92484 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6167fd87-a73f-3f08-b31a-623c5e1f09bf | -12.92604 | -47.31252 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98262c5d-f7d2-3ff9-81fb-36f3285d9661 | -11.87444 | -44.96067 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
