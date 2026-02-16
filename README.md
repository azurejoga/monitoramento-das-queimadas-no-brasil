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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf63e105-06a7-3e66-8843-c9eb74727b7d | -23.4252 | -46.346 | 2026-02-16 00:00:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.9 |
| 4a8881b9-40eb-3682-8f53-f688fa1e13e8 | -23.404 | -46.3521 | 2026-02-16 00:00:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.2 |
| 1d73892b-517f-3e00-8a6a-78344a51eba1 | -23.404 | -46.3521 | 2026-02-16 00:10:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 156.7 |
| 0a89048f-9071-3ef7-a040-3acfc30f223c | -23.404 | -46.3521 | 2026-02-16 00:20:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.6 |
| e16ff9d3-da3f-36bf-83d3-bea6b5e63020 | -23.4252 | -46.346 | 2026-02-16 00:40:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.8 |
| 29961c06-6147-3fff-bdb6-d6ba90a48377 | -23.404 | -46.3521 | 2026-02-16 00:40:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| 4e43d05e-8d14-3aac-9229-88725ddd3a18 | -23.404 | -46.3521 | 2026-02-16 00:50:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| 69aa8f12-73f4-3f89-a1ce-9a04b064d1cd | -23.4252 | -46.346 | 2026-02-16 00:50:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.7 |
| d532e603-31a9-3681-86da-774005a60feb | -23.404 | -46.3521 | 2026-02-16 01:00:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| b2fa8111-0175-3eea-905e-4427dd1d7b49 | -23.4252 | -46.346 | 2026-02-16 01:00:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 5c39a606-c14e-33bf-bfca-686c3af8e30f | -23.404 | -46.3521 | 2026-02-16 01:10:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.4 |
| 34cf4c22-3be9-3286-b9c9-e6cf45eed415 | -23.4252 | -46.346 | 2026-02-16 01:20:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| a3ee113b-7689-3edf-84d8-666048a0e638 | -23.404 | -46.3521 | 2026-02-16 01:30:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| d06664e9-0cff-3d27-85c9-0505e21cecbf | -23.4252 | -46.346 | 2026-02-16 01:30:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| 2f793fa3-e6ff-3409-b242-0ee4631821df | -23.404 | -46.3521 | 2026-02-16 02:00:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| eb3ba15d-c9a2-3cae-b688-b9938edd569f | -23.4252 | -46.346 | 2026-02-16 02:00:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 6f5ada75-88c4-3cf5-884c-bcb7a6a62c5e | -23.4252 | -46.346 | 2026-02-16 02:10:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 9ea8814f-1e9a-3409-b6f8-0460670e20d3 | -23.4252 | -46.346 | 2026-02-16 02:30:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| cad88105-43fd-3909-884f-80d7a9800240 | -9.7877 | -37.21023 | 2026-02-16 02:53:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 76c3d5b1-d0ba-3fad-9b29-e60588296b57 | -9.45765 | -37.04592 | 2026-02-16 02:53:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f0b7fa4d-3cf4-360e-8e12-d682326b6f5d | -16.8329 | -39.30399 | 2026-02-16 02:55:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| afac0c11-7ebb-3c4d-a914-3529f71bbdfe | -23.404 | -46.3521 | 2026-02-16 03:10:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| a0edad30-e662-3aff-b801-589737789368 | -23.4252 | -46.346 | 2026-02-16 03:20:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| c2a02df7-c307-3664-ac20-3b0544d47ae6 | -9.78746 | -37.21365 | 2026-02-16 03:23:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8734633c-c67f-36f3-8c0e-b7b5599d76c8 | -9.46092 | -37.0403 | 2026-02-16 03:23:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b59277d9-4026-3696-837e-c29e764f2c95 | -9.78835 | -37.20861 | 2026-02-16 03:23:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ea3fd49-09c9-374b-a65c-eeec69c6c474 | -9.46473 | -37.04632 | 2026-02-16 03:23:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 51d8abac-e730-3233-8770-20ad419fbf08 | -9.46001 | -37.04541 | 2026-02-16 03:23:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 94d19cff-dcb7-3cab-8b6c-3a99b0eeaebb | -9.78818 | -37.2103 | 2026-02-16 03:23:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0ae9a961-ab7c-356a-871d-fe1d052de550 | -15.31816 | -42.05483 | 2026-02-16 03:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 25e8ce56-1126-319a-931d-86b7c4a04cff | -17.80901 | -40.32234 | 2026-02-16 03:25:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 53847075-0b27-3385-bd21-f6b29fb16f31 | -17.83904 | -40.14836 | 2026-02-16 03:25:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd5d9cb8-165b-3d90-88fc-91d19ad899b0 | -17.8428 | -40.15544 | 2026-02-16 03:25:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b968739f-628b-3f97-8974-70caf0fbd0e2 | -17.84896 | -40.15068 | 2026-02-16 03:25:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3ba5f69b-56f0-3fe4-9c97-c0b2ed0a42cf | -17.844 | -40.1495 | 2026-02-16 03:25:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cac82e67-67cc-33c8-a431-cfb2c887fa1b | -17.84519 | -40.14361 | 2026-02-16 03:25:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d91d9c35-9bcd-347d-a23a-ea177fd82b2f | -15.32057 | -42.05469 | 2026-02-16 03:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 50258895-9ff2-388b-bcfe-4b4554e52d75 | -15.31475 | -42.05312 | 2026-02-16 03:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb97aa86-bfe2-3488-ac85-72ee9298db9d | -22.24901 | -47.21759 | 2026-02-16 03:27:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9134ddd0-59c3-3c8c-92be-6269cae16dd6 | -23.40619 | -46.3561 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| f51b6647-055c-3141-98c6-07b93bea4fbd | -23.40786 | -46.35128 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 4408a8cb-d8bd-3698-8082-10e5e16c8adf | -23.40638 | -46.35723 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 3506903f-cd2c-392c-a56b-45118331afc0 | -23.41257 | -46.3579 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0fdf9b84-88f0-3c0d-9184-750755a5e423 | -22.24449 | -47.2137 | 2026-02-16 03:27:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78b3102b-af7b-3227-88ab-3d336fe367c1 | -23.40768 | -46.35023 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| cfe731fe-7681-3b8b-8606-f19c209469b8 | -22.25129 | -47.21577 | 2026-02-16 03:27:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f725d24-bce0-303b-8b77-c211607a813b | -20.76049 | -44.03223 | 2026-02-16 03:27:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3ec6837c-b00d-30f1-b9d4-38adedb88dc7 | -23.41406 | -46.35204 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6db56730-ddfd-3647-8f7b-e8252a82dd76 | -20.76155 | -44.02766 | 2026-02-16 03:27:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ee66ea8-b65e-39d7-a0b2-ec147c809a73 | -23.41423 | -46.35313 | 2026-02-16 03:27:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c12f1c90-01bd-3868-84e2-780cdcddd6f4 | -23.4252 | -46.346 | 2026-02-16 03:40:00 | GOES-19 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 3f8c40af-b8bc-3448-b803-86dcf213a402 | -4.86243 | -37.45466 | 2026-02-16 03:44:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3776c8ce-c5eb-315c-b362-0d269f74da28 | -10.55572 | -37.87814 | 2026-02-16 03:44:00 | NOAA-20 | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cc3598e-5b46-36cc-82e7-89eb000d66c3 | -10.55511 | -37.88183 | 2026-02-16 03:44:00 | NOAA-20 | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 656eb304-8770-3da1-ad0a-c06e28d6f1d7 | -9.25345 | -36.85713 | 2026-02-16 03:44:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8963833e-4609-36c4-acb7-77598a8812ae | -9.78745 | -37.21018 | 2026-02-16 03:44:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3e3dd6b1-2e35-3264-8fcd-c49eaabf1635 | -8.16376 | -43.16906 | 2026-02-16 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae3b852b-17f1-387d-b28e-9ad8faacae2b | -9.46152 | -37.04394 | 2026-02-16 03:44:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9c25bfc9-e821-33ad-8d40-1f174d980c8f | -9.33833 | -36.85637 | 2026-02-16 03:44:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b3fdf259-6e92-3d16-ae93-3221a5d6bf9e | -8.40465 | -36.61823 | 2026-02-16 03:44:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ab2cb5f2-0321-3656-830c-c17c62303016 | -9.335 | -36.85583 | 2026-02-16 03:44:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e05343ec-e74a-3c27-9bbf-b415a98cc679 | -15.42181 | -41.44001 | 2026-02-16 03:46:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1ee9ace3-c41a-3f44-8125-14f2d86c2fd2 | -15.42096 | -41.44479 | 2026-02-16 03:46:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 54594af1-315b-3f92-9a89-66ce021d80fe | -11.80817 | -43.77861 | 2026-02-16 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da0fbe1c-66db-303a-9544-db099509e4d0 | -15.31615 | -42.05353 | 2026-02-16 03:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7babe273-1e9f-3ea0-a782-65f0a0065748 | -16.83141 | -39.30642 | 2026-02-16 03:46:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| efbc7124-6400-372a-b026-fe4cea82caa9 | -13.78915 | -42.6204 | 2026-02-16 03:46:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7045c3f4-b9b3-3434-8eb0-a14346c0a7a8 | -16.82803 | -39.30582 | 2026-02-16 03:46:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 66bf4d1b-2c14-3346-9d24-d946f1ac04bf | -11.81232 | -43.77509 | 2026-02-16 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 307c3b75-8a4a-3670-adb0-cfa23f137084 | -14.29091 | -41.50531 | 2026-02-16 03:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a1c87ba2-871f-38f2-87e5-67d291a172a1 | -15.0088 | -45.14925 | 2026-02-16 03:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3a2e951-216a-359e-a617-cddfdc8c5369 | -12.82139 | -38.41943 | 2026-02-16 03:46:00 | NOAA-20 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 89eeebf1-d286-33ef-8335-bb89ea74adee | -14.28973 | -41.50271 | 2026-02-16 03:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 60824801-b276-3700-9ee6-20a124bc04a0 | -11.81141 | -43.77999 | 2026-02-16 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae22c6ae-3976-3f01-a5a8-309115db129b | -11.81278 | -43.77952 | 2026-02-16 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a9c2945-c57e-39c7-8bfe-fdefe8d7d21e | -15.00981 | -45.14392 | 2026-02-16 03:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3112d754-63ed-3bb7-a79c-90204dc9db02 | -16.82865 | -39.30208 | 2026-02-16 03:46:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bee3a168-48f1-30ed-8194-8dc18d189ceb | -20.75972 | -44.02923 | 2026-02-16 03:49:00 | NOAA-20 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 744f7fee-afe9-317d-8fd4-0faee94f838d | -18.97157 | -52.93079 | 2026-02-16 03:49:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc03d8fe-d3c6-33c5-a998-0329098134fa | -23.40899 | -46.35508 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 25834988-4504-3ff5-ba87-f80de43370a8 | -18.97372 | -52.9361 | 2026-02-16 03:49:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac9403e3-712a-3385-a767-83f8add3f933 | -22.24685 | -47.21949 | 2026-02-16 03:49:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a95cb0ec-e30e-3750-a4f3-b0e1dc31b597 | -23.40587 | -46.35141 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| c7b717d8-67b9-3426-9306-e1b49a4374e4 | -23.40558 | -46.34938 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| e5e86884-6f46-33d3-9db8-b182c0eb939e | -19.75929 | -48.29214 | 2026-02-16 03:49:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9710bba-0798-3b13-9743-de2fac089daa | -18.71015 | -43.01299 | 2026-02-16 03:49:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60d9373b-8db0-32c3-839a-2845a643b54f | -18.715 | -43.00866 | 2026-02-16 03:49:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee1f1f75-5dc5-316d-96f9-2deb141c901d | -18.97539 | -52.92918 | 2026-02-16 03:49:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e46cd69-5a60-3ae4-9e51-458c8441ab7b | -22.24798 | -47.21395 | 2026-02-16 03:49:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a4dbbc6-ce7d-33ad-af37-2e3221da88cb | -23.40931 | -46.35716 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 453d3ba2-af1a-3b15-86fc-159b377979a0 | -23.40493 | -46.35612 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 2a1b02f3-f8e8-3a5c-81eb-d5472470066e | -23.41026 | -46.35243 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 5cabc84a-5d39-38de-9d64-7b62f8b042f1 | -22.24776 | -47.21511 | 2026-02-16 03:49:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40c6b135-9bc6-3f99-b0f9-5a8bd882c473 | -23.40461 | -46.35405 | 2026-02-16 03:49:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 8f75e460-3c62-369e-9998-9634b65c2e0e | -23.404 | -46.3521 | 2026-02-16 03:50:00 | GOES-19 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 87a80bd1-dbae-3fc8-a24a-bad6326d57d1 | -23.40999 | -50.77097 | 2026-02-16 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 31840132-60ae-3dda-9780-c901ec5a050b | -23.4167 | -50.76827 | 2026-02-16 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34a20015-661b-3fe6-b41c-447d853e9d64 | -23.41567 | -50.7726 | 2026-02-16 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3877543-0768-3caf-980f-73d9730f0e51 | -23.41599 | -50.77044 | 2026-02-16 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ab520197-ff10-3497-8632-afdb47c4bef4 | -23.41031 | -50.76882 | 2026-02-16 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
