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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d966b204-e02f-3b5a-8544-39bfaef5d61c | -8.0513 | -43.1001 | 2025-08-01 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 209.5 |
| 085941a3-f292-3cfa-8675-45b4c76b5593 | -11.1884 | -51.5035 | 2025-08-01 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e8d3b856-389e-3cd9-a5a6-bc4d03ceec3e | -11.5106 | -44.3167 | 2025-08-01 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f1e67e00-c784-3f9b-8ac5-0820c4e0a3f4 | -11.549 | -44.311 | 2025-08-01 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1bea9ea9-8841-32d7-85b8-17b5de637d0d | -8.0321 | -43.1257 | 2025-08-01 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 396.6 |
| 9ee2b213-daa1-3814-b3f6-ccd26e6b1aa1 | -15.0908 | -55.1958 | 2025-08-01 13:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8a5ce69f-4e84-3b52-826f-977b23f8d34c | -11.1887 | -51.4824 | 2025-08-01 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 684c2c50-ce80-3ff4-87c4-463e83b7e917 | -8.0324 | -43.1022 | 2025-08-01 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 246.4 |
| 82d09168-58ae-3528-bb6a-33aa926b339d | -11.5298 | -44.3138 | 2025-08-01 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c3459419-49c2-379e-8643-2205dfbe32c3 | -11.7858 | -44.9958 | 2025-08-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1845a61e-e5ba-368d-8a03-1e95cef22cb2 | -11.1884 | -51.5035 | 2025-08-01 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 54668dd2-9414-3463-af43-ba5ca312affa | -11.1613 | -45.7498 | 2025-08-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 194113b3-04f8-3e34-9714-c0bfa13604ba | -13.0471 | -47.4031 | 2025-08-01 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4d34a411-c596-3bbe-91df-ffbe85e9e845 | -12.651 | -48.0842 | 2025-08-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1d8fa97d-8f4e-3dfd-ab33-653b73109884 | -8.0324 | -43.1022 | 2025-08-01 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 268.1 |
| 0ef1eafd-ec81-3f60-8468-acda073a5e9d | -11.7666 | -44.9986 | 2025-08-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 12585596-ffe0-3fe3-a50f-e8496e22b8bf | -11.767 | -44.9754 | 2025-08-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 05dc911a-c3bb-3e3a-9e46-67c094a4aa8f | -11.1887 | -51.4824 | 2025-08-01 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0e9538e9-b0d5-3799-8d56-f11c014daea0 | -11.1884 | -51.5035 | 2025-08-01 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 337f4089-afcc-3137-8254-bf4463049d42 | -11.767 | -44.9754 | 2025-08-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c353737d-009d-35ca-ae7c-945c30d2fbbe | -15.0908 | -55.1958 | 2025-08-01 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c44f1e07-7cbf-3b82-8ea0-739573707d3c | -11.7666 | -44.9986 | 2025-08-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 72b93fc7-4bbb-39bd-958b-86e6d3ecfb06 | -11.1613 | -45.7498 | 2025-08-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 213fba7b-eadd-394a-8231-082aef33a736 | -13.0471 | -47.4031 | 2025-08-01 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 80b9856d-2e5f-3dc3-a75e-1e2cb8c23077 | -11.7858 | -44.9958 | 2025-08-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3a36c115-3018-302a-b2aa-460c6c33af2b | -12.651 | -48.0842 | 2025-08-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d3135f5b-b796-3f8e-aeac-24a5d1eac9d0 | -11.767 | -44.9754 | 2025-08-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6368d46f-e584-3a0c-bcee-81644f66eeb5 | -11.7666 | -44.9986 | 2025-08-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 7cb77d90-38c8-36e3-8c9b-454269aa21de | -11.1884 | -51.5035 | 2025-08-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 8a5affe5-6e51-364c-b793-c3b0fe761cc9 | -12.6506 | -48.1064 | 2025-08-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f00501b2-0de5-330f-9cdd-8d56b75cbc30 | -11.1804 | -45.7472 | 2025-08-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 9d721595-0e64-38b0-8e1e-c4bf103ec8da | -13.0467 | -47.4256 | 2025-08-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e606d41e-a743-349a-ad75-6ce4e7c7bd0d | -11.767 | -44.9754 | 2025-08-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9d87a182-cabb-3549-a5af-11fd73d0e505 | -13.2996 | -51.6862 | 2025-08-01 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 61ac8f2c-66a0-33b3-8c35-66ad762cc71f | -11.1613 | -45.7498 | 2025-08-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ee4f3b35-142b-3b6e-944c-491e84f0e17a | -11.7666 | -44.9986 | 2025-08-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 1f9a6984-9b3b-3014-b062-fb77bfe9f839 | -11.1884 | -51.5035 | 2025-08-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b41f4c91-8a18-3f29-9de7-947710e19368 | -12.651 | -48.0842 | 2025-08-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 876fd856-e4e7-3098-a4a1-017def9f5d0e | -11.2954 | -50.6222 | 2025-08-01 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 95b5bdb1-569a-3495-bb2a-d0ece6b49f1a | -11.767 | -44.9754 | 2025-08-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 772f01ea-9b4f-3196-b08e-24ca40227ab9 | -11.3144 | -50.6201 | 2025-08-01 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 26f9b12f-7a41-3fca-8e52-cfe11e307dae | -13.0467 | -47.4256 | 2025-08-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 118d4bf9-6798-3039-97df-260a111a7130 | -13.2996 | -51.6862 | 2025-08-01 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 54290cd5-ad61-3820-9856-d9fe4d3b1f1f | -13.0471 | -47.4031 | 2025-08-01 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d8dd60f2-3479-34bd-9ffe-00ca3ef57cc5 | -11.2957 | -50.6008 | 2025-08-01 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 942d1a8e-c93a-385f-8ebb-3c74cda4548e | -11.2954 | -50.6222 | 2025-08-01 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 7aee476b-ae32-30cb-953c-ccf71d39ae4d | -11.7666 | -44.9986 | 2025-08-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 1dab1478-0d46-39f9-9e47-55e6d7263943 | -11.7858 | -44.9958 | 2025-08-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c7d19588-9d93-3aa1-aea1-8b95b20ae87f | -12.651 | -48.0842 | 2025-08-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |


