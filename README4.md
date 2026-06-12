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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99be326e-2643-35f9-a73d-f69e3cf80eea | -13.84569 | -41.41079 | 2026-06-12 03:53:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8f47a29f-013d-380c-8881-b87e02b09c52 | -15.19198 | -42.2886 | 2026-06-12 03:53:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17bb0420-d261-37e5-a743-060d63fc94da | -11.53941 | -48.27192 | 2026-06-12 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 212fb96e-94c9-38cd-8456-6474229246d5 | -10.99716 | -46.74569 | 2026-06-12 03:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96661c09-d31a-320f-a430-1feba68d168c | -19.05269 | -40.41563 | 2026-06-12 03:55:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84ad81f1-c63f-3309-b162-1fd15419428a | -17.79683 | -44.57393 | 2026-06-12 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c288576a-db0f-3952-97d6-ec4857f4e0a9 | -20.2252 | -50.19044 | 2026-06-12 03:55:00 | NPP-375D | PEDRANÓPOLIS | SÃO PAULO | Brasil | 3536901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b9ba9f80-66c4-3c89-8da9-87a4ce119b9c | -18.72767 | -39.76839 | 2026-06-12 03:55:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84b87888-6f82-3647-92cf-a1e738b94a54 | -17.79162 | -44.57734 | 2026-06-12 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e0ad52-8a7d-30d9-9554-761b6f9b7902 | -20.22418 | -50.19487 | 2026-06-12 03:55:00 | NPP-375D | PEDRANÓPOLIS | SÃO PAULO | Brasil | 3536901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| feaf46cb-fafd-35d4-8496-7ef1f7352e93 | -19.76531 | -40.73254 | 2026-06-12 03:55:00 | NPP-375D | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7bfb725d-385f-3602-8a1d-de3163f1f0d1 | -19.88721 | -40.46399 | 2026-06-12 03:55:00 | NPP-375D | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f94e9e64-101f-3650-9288-df1fb2240cb8 | -17.79263 | -44.57525 | 2026-06-12 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c7c5a5-35e2-3c70-beae-96792abad6f6 | -12.8548 | -44.3625 | 2026-06-12 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 26b5dd81-b7d8-391f-90fd-b44a3ea5e6df | -12.4274 | -58.484 | 2026-06-12 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 08575e00-6137-3fe7-9201-bf25f16d195f | -5.20317 | -47.71358 | 2026-06-12 04:10:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c788ea6-0781-383f-8d68-130ad2346701 | -6.44127 | -44.56033 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3df0e893-86c9-33a8-9305-51e870701798 | -6.44195 | -44.55623 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a4da9f-9745-317a-b6a2-8dc67af9f2f4 | -6.19218 | -44.86106 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c7afe88-8f9d-371a-bed1-778932a72ad8 | -6.43958 | -44.55677 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e05fd252-ab79-3df0-a0e1-b571e0f46308 | -6.43837 | -44.55567 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b14d0286-b8ea-326e-a437-4d46e03da251 | -6.44417 | -44.56499 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 588f3004-7e0a-336c-8afd-d62c461116b8 | -6.56854 | -47.91663 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cd491591-16f5-39ed-adf5-3a7f40ed89ba | -3.98916 | -47.93607 | 2026-06-12 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9f04972-1176-360f-be06-e587478dcf2c | -8.45228 | -36.23106 | 2026-06-12 04:10:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e72e0e2-2c6c-380f-8afb-9fd209d603ab | -3.49695 | -48.0367 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e36b5657-17dd-3500-96fa-fc6cc24d1747 | -6.44024 | -44.55268 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dae8f94-2dad-3164-9f9d-b4309787ab1a | -6.43666 | -44.55213 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18891955-2a8f-3719-b610-de0ee81c92c8 | -6.44775 | -44.56555 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a94fb126-751f-3e58-adcf-3b454a521c50 | -5.79587 | -45.11052 | 2026-06-12 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5aa87fc-7627-3caf-8cc0-aab15d532b06 | -4.41473 | -42.13449 | 2026-06-12 04:10:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3303feab-20f9-3c12-9d95-a03bf8a37956 | -6.58245 | -47.91443 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcdf18e6-4324-351e-a107-043f88c6688e | -5.79659 | -45.1061 | 2026-06-12 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e57748-4853-3f95-99f7-b5822f674966 | -6.18782 | -44.86478 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aec07aea-7b32-3688-88b9-2d6bfddfd7fc | -6.436 | -44.55622 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 271c737e-86ef-34dc-bb3d-a7818c7afee5 | -6.44317 | -44.55733 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c16db9e5-f1d4-39ad-9f03-487feea1716d | -3.90845 | -40.97837 | 2026-06-12 04:10:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a24b2e4e-4d00-3ddc-8c2d-24666cb2579f | -6.3961 | -44.17488 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06bb7278-24bd-357e-a3b6-cbafba3fcb5b | -3.5071 | -48.03323 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec70a095-4ad3-338d-ae6d-221ef1249188 | -6.43905 | -44.55159 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6b2e253-5db3-3512-9bb3-4df30640ac99 | -7.00293 | -43.8617 | 2026-06-12 04:10:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e7b5d99-25c9-3fb2-84a7-34a320ad9c48 | -5.8024 | -45.10516 | 2026-06-12 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0adf6543-b22b-37d9-90f6-7bb6b21d6a58 | -6.3931 | -44.17342 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0bcc8f3-21ee-389a-9c4c-9812c3c92825 | -5.58068 | -43.50655 | 2026-06-12 04:10:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c447de0-0229-3301-b9ab-9a892281bb35 | -3.87354 | -40.70491 | 2026-06-12 04:10:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1cc4fbc-87e3-3401-936e-8b970e9fa105 | -6.43467 | -44.56448 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3833304-94a1-367a-98b5-6c74d4ae20be | -6.72582 | -44.37625 | 2026-06-12 04:10:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a104e406-ddf0-3da2-9437-a8fcd0bcf9a3 | -6.99948 | -43.86113 | 2026-06-12 04:10:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13502c82-d5a8-3335-b944-997e8932cd6d | -6.39258 | -44.1743 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86e642a4-dc57-335c-b1c1-3915f742dcd0 | -6.39673 | -44.17094 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5784e05-a535-3f3b-860a-935548ef5d94 | -6.72228 | -44.37568 | 2026-06-12 04:10:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 830e6105-a014-38fc-82c2-7f4ff63ae2fb | -6.56416 | -47.91582 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aaa3232-f69d-3edf-962f-d31c1a86cc1e | -6.39662 | -44.17399 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d12badb-f622-3606-a2c6-0d28ed2ed483 | -3.50243 | -48.03259 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b360ffe7-3334-3aea-8437-cf8549d6df86 | -6.57882 | -47.90927 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d44b0d0c-9f71-3d90-afdd-6983521007a7 | -6.18489 | -44.85992 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e598642a-ea36-31b7-8835-0152aed12fc1 | -3.50629 | -48.03803 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06d170ae-fa2a-33fe-8712-eeecc30dd49d | -7.00638 | -43.86227 | 2026-06-12 04:10:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fa821d2-5591-339a-878b-9a80c70d372f | -6.44184 | -44.56556 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 240b5741-8d4c-3195-9e7b-92c02a159598 | -6.5737 | -47.91287 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4ecd1e3-9fb6-3d12-9d6c-7ec294eff1c5 | -3.4961 | -48.04176 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37abcf34-d59c-34c3-98bd-5ffb88bfc727 | -5.80029 | -45.10677 | 2026-06-12 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 602de822-abf1-3783-9cb0-fd248a04337d | -6.39195 | -44.17826 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de52313a-60d3-3e8b-9d2f-19721aa8b2eb | -6.44058 | -44.56444 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7533234-260c-331f-bb1f-9f48571b8f5d | -6.39245 | -44.17736 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11632e6f-54f2-3e98-b727-dab14bae7149 | -5.58413 | -43.50713 | 2026-06-12 04:10:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c6825b4-7d26-32fc-88f8-ca07e747060b | -6.03729 | -43.99827 | 2026-06-12 04:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7700e368-aa5a-341d-9d8a-e8508580a253 | -5.51881 | -37.61958 | 2026-06-12 04:10:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 791ad8d8-b49d-36ae-a566-b01876d26242 | -6.86737 | -40.89169 | 2026-06-12 04:10:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5eac5cec-403b-3790-a2cf-0396b59337ae | -6.57808 | -47.91363 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff1c22d6-a4dc-35d2-ae8d-68cc30dab1a0 | -3.50163 | -48.03733 | 2026-06-12 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b77c04a7-fe89-35c5-844b-1585088bf948 | -6.18853 | -44.86049 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7b731ef-8c71-33ef-89bf-501bea3a3bbf | -6.39727 | -44.17006 | 2026-06-12 04:10:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3818ca7-74b6-3d0c-903a-0a8debd8f6b7 | -6.437 | -44.5639 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ee822a0-d593-3445-8d03-17562a912006 | -6.56932 | -47.91211 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65b7d21b-397b-31a8-ba0a-6e4b0caa70b2 | -6.56494 | -47.91133 | 2026-06-12 04:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 302ffeac-6bc3-3313-8906-d0b4e253c413 | -6.43826 | -44.56501 | 2026-06-12 04:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be28b178-ddc8-37fc-842e-4d744fbc3711 | -9.1946 | -48.64244 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e9f667d-4f40-3313-8214-7d451849769e | -11.25887 | -53.96692 | 2026-06-12 04:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8fd9d18-9a8a-3eab-b462-2f4374174f60 | -9.69322 | -47.6939 | 2026-06-12 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7347cb59-577b-37f8-b587-b38f7ce790ec | -10.71163 | -49.48191 | 2026-06-12 04:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877c4e35-02dd-3306-8fcc-6d0003f73983 | -10.83976 | -53.74599 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f63b4657-2a72-3038-89b6-8c09844498f4 | -7.3314 | -47.04822 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a81d39ab-fbc8-3cab-b219-46b7d812c6dc | -7.63772 | -45.29895 | 2026-06-12 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e34abd5-1b4f-3b81-9e63-ba32bf5e3849 | -7.37105 | -49.87111 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73dd90ba-6d74-324b-adb7-c4022670844f | -10.71532 | -49.4874 | 2026-06-12 04:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2feb140-3f56-3c0c-8a3b-01a441ad9df2 | -9.06259 | -44.75957 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a024dabd-6c21-3c96-8777-1f61dc39b771 | -9.20948 | -48.58304 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08ce31d6-31b5-342c-9911-c277544cfd92 | -9.30738 | -48.97242 | 2026-06-12 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d2ab791-af44-3185-b151-29fa52c7068e | -12.85744 | -44.36848 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 972b37f3-13de-38c2-92cf-00b79702ed03 | -7.33024 | -47.05089 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f8423e8-f2a2-326d-a304-aa3c530e2b65 | -10.9342 | -44.66835 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38198072-1474-3da5-98ae-4e8f152a539d | -9.21902 | -48.58022 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5c1e1c5-4162-3b01-8d74-34413a831fb3 | -10.94756 | -48.83583 | 2026-06-12 04:12:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8186747f-9c1a-356b-92b5-92f8f3ac9ca7 | -7.34875 | -47.01678 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bebf9cf6-4318-3183-b2f4-91cd12f07068 | -10.99581 | -46.7463 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10ddb90f-bab5-3aa4-9d57-f039fd2fbca3 | -12.36309 | -47.89271 | 2026-06-12 04:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 494ce6ae-8033-3be6-a553-eb74bb1816d3 | -10.89465 | -49.48549 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e51ac191-da6f-321c-b4f3-abbd3f5d3a9b | -10.93077 | -44.66776 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05e756fc-d09c-3437-a641-b2de26f26bfd | -8.56281 | -47.39387 | 2026-06-12 04:12:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
