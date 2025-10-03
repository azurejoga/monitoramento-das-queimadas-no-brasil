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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69ee6a2b-a3fc-3129-9b3a-77f6bbc3af83 | -6.55822 | -43.89879 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c84b72-40ce-32bd-83d7-1d2b78de0d47 | -5.2378 | -45.17039 | 2025-10-03 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a9505c9-e7a1-3a51-820a-01da3b09b631 | -7.77778 | -42.50402 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ffc75f9-c34d-36af-a0c6-9be0bc101eea | -7.30382 | -45.26448 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66bbbfc4-345f-32ae-8a75-a8c1289a3518 | -6.72794 | -44.14516 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78d21ed4-ab9d-3415-bac2-f85f230b7bd5 | -6.2777 | -44.05048 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f85377fe-6952-39cc-a45a-84d1d6a49e18 | -3.55854 | -51.13026 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 470603c8-d7fb-323c-b2a6-4fe8b7853459 | -8.59612 | -44.76458 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da9aadcb-be4e-3ea3-8b50-f9fa33f1bf9b | -5.62976 | -43.90707 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6b04312-9680-3e8d-8264-f7bfcaec686d | -7.29767 | -44.19276 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0263732d-dbac-36c0-ad13-91e4e2ab4768 | -4.39169 | -38.41425 | 2025-10-03 04:10:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7a57686-d2e1-36b4-924f-ed120ae433aa | -8.27462 | -43.83988 | 2025-10-03 04:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bef028cc-264c-31fb-982e-7580a8f6c233 | -7.31947 | -42.87659 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2217f77a-eabd-3fc1-aa4c-3d3dc502e346 | -6.64392 | -43.5968 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce39032c-f0b2-3a73-877e-82bca3fed7b5 | -7.23461 | -42.98798 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3a72e80b-643a-315c-8951-24642fd5a6b9 | -8.23587 | -39.02392 | 2025-10-03 04:10:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c33df669-9f11-3ba0-9f35-94df42866c87 | -7.75233 | -46.24261 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d1b8046f-8bc4-30a5-a5f2-3e2c963a498d | -5.90302 | -44.26623 | 2025-10-03 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4eda71c4-06b4-30af-8b87-55e2bf891794 | -5.39916 | -41.33698 | 2025-10-03 04:10:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9b8669b3-0345-3698-b786-6e82665cde25 | -6.23279 | -45.34458 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11f94406-a181-330f-9342-2a8af8a9bd33 | -6.05469 | -44.61755 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fa566ed-be17-3927-98ae-ef3f37cb124f | -7.74846 | -46.24188 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b603fc3f-179e-377b-9d0c-4c0c5586f497 | -2.92246 | -48.30369 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b77f7077-0bc1-3a82-a975-b71d19b1b26c | -7.72674 | -46.22881 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46cf92e3-8caf-3564-9087-6e6a45c74525 | -6.23879 | -45.35493 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bd01974-5f4b-36ef-b4fa-0d9415d401a7 | -6.67453 | -42.8246 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8a00141e-00c5-302e-83c2-4c55c4a55f13 | -6.55084 | -43.87788 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26f7ab7d-af97-3d84-addd-8a41e3c1d5b2 | -1.07997 | -53.68535 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3262386c-657e-31e4-9d82-a11d67bf381d | -4.65018 | -45.80013 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8057ea29-6a15-388f-ba9a-61e48eb1233f | -6.73978 | -44.58151 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b27f829-f1f6-3659-84d4-e1895d24ce7c | -4.4848 | -47.67389 | 2025-10-03 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ede44a7c-c0bf-310a-b297-a0084515f991 | -8.15701 | -44.12622 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7ad5bb4-490d-3db0-9f66-fc97639e7646 | -7.77765 | -42.59047 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7e5558e6-f398-3e55-b5cc-7772860cfeb4 | -4.20617 | -46.44091 | 2025-10-03 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32021596-dabe-31a4-83ef-3c11affb4bad | -7.52798 | -47.29388 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f18a65e2-95ad-3611-974b-a80482b752c9 | -6.06628 | -43.21597 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2962dbd-1f85-3fe3-bb5c-375f40d36b88 | -5.54339 | -51.13033 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a40f3f3f-98b9-3d6e-adb0-b9cfd499937e | -7.78883 | -42.5634 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8186a41a-6404-30ff-967c-1341decbd335 | -6.55945 | -43.89109 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87416ab0-f39d-3007-9ebb-527988720f0a | -8.58988 | -44.78011 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a98843-03fb-38e9-9bc8-9ba669d6eada | -7.74686 | -46.25145 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0142f10-3270-3ddf-b914-b143d07fddf6 | -7.7591 | -46.27374 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 02c281a4-7085-3e49-966d-1f1829461e23 | -7.77441 | -42.52507 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 462d84b8-60b6-3d27-9589-ff6768d7b478 | -5.69871 | -42.83215 | 2025-10-03 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f79225c-6124-39a6-b955-b72e56bda415 | -7.77097 | -42.5894 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 721d2e65-4a37-399e-beee-96383467e6b3 | -3.08948 | -47.01342 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 753242a3-6e33-3630-898b-54df722b2474 | -5.49132 | -52.13519 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793e52da-4b94-3640-8017-765ea8680c92 | -6.69024 | -42.83445 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37e5b302-fbcd-3523-a50f-2500e5a90208 | -5.24674 | -43.10234 | 2025-10-03 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62482945-2e99-35bd-831f-e8fa97558689 | -6.6533 | -42.78473 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6bd50dd1-7193-3fba-97d1-0451d110b8d8 | -4.7013 | -37.37078 | 2025-10-03 04:10:00 | NPP-375D | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7bfb37ea-2cd4-3fd8-8148-cf5c5ca8a11e | -6.38908 | -43.60297 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01ebf5d8-0ded-31b2-8e58-6487ddf11868 | -6.68492 | -43.71592 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c0c5632-7000-338a-b2b5-95a32230fa26 | -8.10967 | -40.91988 | 2025-10-03 04:10:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0f00a16d-765e-3735-87f0-5f40cccd7ca5 | -7.30312 | -45.26881 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae39078b-cf67-3c79-9b33-0355f4d697c6 | -6.23263 | -44.2384 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df2a2a73-5223-3356-923e-c627365865fa | -7.7491 | -46.26189 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 04da75ba-d2c9-3e1a-b691-d54aa8e9f9b2 | -6.23329 | -44.23432 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c9d93b3-4ae3-300e-8f8c-c45d5cbb08dd | -4.26565 | -48.55002 | 2025-10-03 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd0820d2-4cd6-3618-b35e-8f89317dda9b | -6.6582 | -43.86004 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 416f61e9-91a0-3924-be85-94530c7ae8e4 | -4.64935 | -45.8051 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41765ee1-8683-37ab-8fa1-023fde2387c6 | -5.97444 | -44.0728 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f1b7e41-df57-3777-862b-ffef7b19d964 | -6.3487 | -44.30112 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd139b5d-6179-3807-8fd4-307bfa7c529f | -5.90236 | -44.27029 | 2025-10-03 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 798a043f-22b6-35ec-8976-40c9bf71d3a8 | -7.76763 | -42.58886 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b9e79805-85fd-359d-a705-968502a719a4 | -8.3375 | -46.22281 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695e2920-a82c-3b32-83d2-65523ba558e2 | -6.37658 | -43.88582 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d324ca6-d571-32ee-9a1f-73afe5a40795 | -6.22752 | -45.35296 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2ba9324-3f84-39e3-9a67-c5a4d78dc38e | -8.44963 | -41.89461 | 2025-10-03 04:10:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 99849ac5-11af-3ce2-938f-5dc091582cd6 | -7.76537 | -46.2601 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6ba9ace-0fd1-3293-a809-85ca1fe5297c | -7.8821 | -47.3451 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 581ab20f-54de-3dfb-90c2-b6438d911f0d | -7.7799 | -42.57639 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| cb64cb51-0c72-3616-858f-7af2e2b67887 | -2.9255 | -48.31492 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 856cd16e-48f1-31c8-85bc-ec4625798010 | -6.29666 | -45.91665 | 2025-10-03 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 500526c6-7c4b-3233-ba5e-1c5ea698319c | -7.7145 | -46.20695 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| afd70e26-c42b-3ce6-a534-4ea08bd18676 | -7.75933 | -42.55508 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b496a128-c722-31aa-9990-6c73a548a91c | -5.48537 | -52.13415 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa064bc1-5eef-3fe8-b7e0-cd913a62271a | -7.78112 | -42.50455 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f61af533-abf8-3689-b4d9-8d1769ce912c | -6.55145 | -43.87408 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2bcb993-a24e-3a31-b4bd-ad1bdfb7f0fe | -7.73518 | -46.2497 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc34668b-7ec3-39b9-a33c-ed7f574e7e12 | -7.28536 | -45.26147 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de6afb25-ea7d-3297-b9d5-8030b833046c | -6.68292 | -42.83699 | 2025-10-03 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3227ebf8-b895-39b2-aca4-ce5713b8dd76 | -6.67733 | -42.82872 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec8f8380-6ff9-30c3-a3d8-63c3e47af41f | -5.64032 | -43.9088 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9db3a8fd-284e-30d3-ae96-38b02e3bfa1b | -3.66623 | -38.8111 | 2025-10-03 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd77911a-87db-3da8-819c-8acf5a59e10c | -6.35773 | -44.5939 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 860b7e95-249b-3034-8c97-9ca5a9ba1b73 | -6.54673 | -43.88118 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 782753ee-b1db-3559-ae16-0abb0f9b714b | -7.77209 | -42.58235 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c7236788-3fa4-398c-84ae-8af83a8346ef | -7.75209 | -42.55751 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 1a36ce5e-68c7-3c98-b8e5-91030c4ef526 | -6.38463 | -44.76968 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b6b421-864b-34e3-895e-1dda5cf6b933 | -6.29688 | -43.90991 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d64aa66d-39fb-3ce3-9e4a-0214e749bdea | -8.58153 | -44.77211 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc406ef1-611b-3b17-b5f9-a26d0d23fb35 | -7.78437 | -42.5699 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f39ac687-4810-3550-8071-a8ae3724950c | -4.80905 | -46.81223 | 2025-10-03 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e2f8e0-00a3-35f2-8789-fea5a8620af5 | -8.30591 | -44.86537 | 2025-10-03 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26227149-e142-3033-9354-e16d7fa05e4b | -7.776 | -42.57937 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1f3bcc2c-dae7-3f14-93c5-1115cf0f0cc5 | -4.66603 | -45.80236 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 90331347-cefa-3e8e-bfa5-cef6d2462c1d | -7.90222 | -43.52935 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd6306d7-54eb-334a-b302-6fa784bb4a5a | -5.26928 | -42.65763 | 2025-10-03 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47fa7a39-ef22-3c78-92b9-dee7ce12f174 | -7.29195 | -44.18377 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
