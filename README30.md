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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57650437-4b9a-3a7c-bad2-e713d7d23f59 | -7.60184 | -44.3919 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b05801f-15ac-3248-a514-2cd91b2b1123 | -4.01999 | -48.06032 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1a7ebce-0df1-3c2a-8a7c-e6b315387022 | -7.69952 | -44.01997 | 2025-08-20 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c11ced8-3d7c-3774-b33b-3f8210c0b8ee | -6.11913 | -42.73169 | 2025-08-20 04:34:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eaaa5a4c-2dde-3d09-be21-8a886d4b6969 | -6.55479 | -43.00173 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8e7ab2-0fbb-32dd-93d5-17d2c19e2615 | -5.78882 | -43.60999 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4696775b-1d45-3b8a-ae83-a4a85c2213f8 | -8.29827 | -47.62053 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd68b449-03c4-3858-a19e-23ae095fcfa2 | -3.40001 | -46.90717 | 2025-08-20 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ebcdd46-869d-3184-b7e1-6fa2727c8911 | -6.39435 | -44.25258 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a592cc0-0faa-3e94-9213-1933e21bb074 | -7.96811 | -55.29991 | 2025-08-20 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae98c627-9c8d-3ffa-80d8-0b4017aedadc | -5.8717 | -48.12033 | 2025-08-20 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae358f51-92dd-3664-989e-6b8938072499 | -6.85496 | -43.61204 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0304a5fe-ed7f-3fe0-8f39-61ba2991feed | -5.37394 | -50.89617 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb1dc00-c2a0-3c2b-a036-fc00184fb9ba | -6.46447 | -53.37001 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56da2410-8316-36c2-9f8b-ff48b0dbf4d3 | -6.95588 | -42.86975 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 62d80417-6e3f-3632-8b58-312bd14e4971 | -8.03297 | -47.67147 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb95bce2-8f3e-37d1-952e-b550ee5e9928 | -4.169 | -42.02972 | 2025-08-20 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 443af831-33bd-3c94-8ceb-ccdf1b36bd8d | -8.8042 | -45.44138 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b2b83e-18f6-30ce-964f-30f0ea73125c | -6.85566 | -43.60731 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8506ccc1-b41f-3691-a793-955ccc785c67 | -4.42696 | -47.75625 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3609d839-39de-3c74-8fea-6adea0689252 | -4.91063 | -43.22862 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73ed4790-f465-355f-996b-5056c9179a4d | -8.15288 | -45.56463 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0869800d-e4d6-37f8-8478-b16c3c55e65c | -6.14581 | -57.71241 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 699c18dc-83cb-398a-b8f5-1d74cda29554 | -8.16777 | -47.3552 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dce86d31-fdb9-3043-b115-539f0f31bc28 | -6.94681 | -42.87553 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| b8c8dab6-02da-3836-a85b-c468eb94b7ec | -4.29547 | -48.06781 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22a8ede5-5ad4-3a7e-a915-eff756e1fcbc | -2.77489 | -48.59548 | 2025-08-20 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0296b997-7449-3b35-bd77-b0b2798a9803 | -8.83313 | -52.04389 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3a35256-20d0-3c68-808d-ea9dddd2cef0 | -8.30619 | -46.35191 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad0f4097-1e48-3132-b315-dd1d47891376 | -9.44946 | -48.36562 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 183cf0b2-9660-396e-8914-ab4632d10364 | -7.12529 | -44.6434 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cca0703-9326-3c1c-ae0c-f3e96d1d76fc | -6.49142 | -45.19387 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5a51e35-b07b-3919-915f-acc173121d6a | -7.27436 | -50.182 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50f3da17-97df-3504-b250-414180b49e59 | -7.65761 | -45.26746 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad03a379-667e-3fcc-a6b2-92e53f8cbe7e | -4.30271 | -48.06537 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94db6464-95dd-3065-879f-5aecc22e0dc8 | -6.37567 | -44.74866 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e2cbe72-a5a2-3aed-b97c-431516bc47dc | -4.31439 | -48.09952 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20a62fc3-fec9-323c-95ed-a8597966cffd | -6.0372 | -44.35352 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 975cbfd0-6a70-3e7e-80f9-902e33330e69 | -2.38109 | -47.66286 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 475dc5e6-6e4b-3a90-99f3-0d3af076aba3 | -5.98023 | -44.14566 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 457ae492-1bd9-3326-b5ce-7bb84d2f7904 | -5.46003 | -44.87199 | 2025-08-20 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a1f54a2-31e7-3aaa-b2f1-827bec8c26b6 | -6.94692 | -43.84792 | 2025-08-20 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff943906-6ef2-3780-89f2-8ce880371183 | -4.87385 | -47.75565 | 2025-08-20 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcc42a94-54e2-3517-a7e4-80932594046f | -2.83353 | -49.14279 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fe2ecca-cc8b-3053-9b14-2d68ba2c1507 | -3.27301 | -49.14777 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5456440-5db5-3631-8ebd-bbbe86544707 | -2.54338 | -47.70292 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2686991c-3662-383e-aabb-28ba37543532 | -5.40798 | -45.19034 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c301151e-c34c-3b31-b2e5-277a04738a16 | -6.11964 | -42.72819 | 2025-08-20 04:34:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 221f8a75-2a51-3aea-9ca2-a61785e6c11e | -8.21774 | -47.31303 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86de7eba-393a-3564-ac59-358dd77dc33f | -8.80196 | -45.44239 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15ebf681-4789-3bd7-a4b2-2d27935e80d1 | -6.95134 | -42.87265 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 8724b4aa-ae26-3909-88b6-7953525c299f | -8.21884 | -47.306 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f59fbd1-24bf-3304-b8b5-8f0d16d4e63f | -8.30562 | -46.35561 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89363e52-c1ca-32a1-a85b-c34a8ad26ae1 | -7.28779 | -43.67984 | 2025-08-20 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d55ceb4-a75d-35e4-b4e7-1422343847d6 | -9.33638 | -48.39743 | 2025-08-20 04:34:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 004cd832-fc15-30f5-8257-819d862b5424 | -6.92304 | -52.85651 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1037c023-aee1-3cbf-9078-b15eac170537 | -2.97436 | -49.29791 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64363551-3a15-3123-9137-1d995dde87e2 | -6.14015 | -57.71135 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d06e32fc-2824-3caf-8d52-cc8707c7d3e8 | -7.27498 | -50.17817 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ac1b3ab-793f-3b66-9b63-05e6dcc3468f | -7.63495 | -45.2774 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 731614ee-59af-3fd5-a9fd-f55e9401a9e0 | -7.63911 | -45.27393 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035c1b5a-b9e3-3f8d-ba40-988ea93e2762 | -7.64265 | -45.27451 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abe1142-261c-309f-80ed-4b636453b0b1 | -5.87599 | -50.14864 | 2025-08-20 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9138a310-73db-3675-ab71-e73dfe7cfbaf | -5.98261 | -44.14412 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 451e458d-d7c1-3bf9-9b27-6d8822b5a803 | -7.02663 | -44.2894 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7a7ad14-2b05-3ca6-a05d-0fb70979ee63 | -6.15081 | -57.71713 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bd08037-3be1-3133-8e8c-7a14f53fb099 | -6.95992 | -42.87033 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d1a7ba25-c923-3b5b-94ee-47dbe4efcb5f | -6.51273 | -43.41798 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b02026a1-7e52-35ff-ba2c-7946da694e55 | -7.22441 | -44.7005 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa615563-586a-340e-8e80-44e7c17e398e | -8.82275 | -52.03478 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d03d8cd-4d2e-3bf3-b44e-78408988f2a5 | -6.16352 | -42.70958 | 2025-08-20 04:34:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 039637d6-a5aa-3de3-a47c-ba4150390522 | -3.98187 | -42.508 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5cccb5d5-706c-3a69-a811-6945b6fc508c | -9.65922 | -47.14903 | 2025-08-20 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 776f359e-eb58-3d44-8b8b-13eeb14284bb | -5.11335 | -43.21105 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5573c8c-592d-360c-9801-7259866c042e | -5.98471 | -42.82869 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d671898c-a0c7-3f55-bdcd-1fd849661747 | -2.90354 | -48.29254 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba9c09d0-db12-309c-bf91-066fb2608bef | -6.1345 | -57.71025 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f52378a4-ccee-338c-9d9a-4eb8fdb34748 | -8.7964 | -45.47881 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f642f6b7-26d9-3d38-830b-16374835488b | -4.76316 | -47.91619 | 2025-08-20 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4995dc7-07bc-3cea-bdfb-783ec9f428bc | -7.22142 | -44.69567 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aeed0c50-9f54-38fd-9f99-2f6aac530eb2 | -3.99221 | -42.51989 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63e5cf2e-d32f-3e2f-a77b-768871ea8efd | -2.77431 | -48.59914 | 2025-08-20 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eaf86ac-6a53-3540-880c-a380bc97eba1 | -8.02895 | -47.66038 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f922cdd3-ba54-3643-8949-1a532271249e | -9.26735 | -44.53514 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 274d4eda-392a-3d86-b0d0-6359af49aac8 | -2.84595 | -48.78742 | 2025-08-20 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bc9b565-ab0d-320b-9cc9-b2e0fc04463c | -4.60231 | -43.32502 | 2025-08-20 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c765ae6-a545-3e24-85fb-1f3671b1c343 | -7.65227 | -45.27894 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f10994-8c6f-34c8-9672-da1ae35e460c | -5.99206 | -44.28189 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e4a51dc-1974-342d-936b-2ab8a385ebf8 | -6.44509 | -45.49916 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c46c5b15-9b34-31be-a6d6-0eebbb613cd7 | -6.8602 | -43.6032 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1b818b2-e4d8-3fa9-ac06-69328614e78a | -4.64825 | -43.1222 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 658bf8c3-68cd-36b3-bee8-6f82e28e1fe0 | -5.63854 | -43.38362 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae113de2-d1b3-380c-bd1a-b423097bc368 | -7.22505 | -44.69625 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a16f8d1b-b4a7-3f55-9999-00e6d5a11acc | -6.46381 | -53.37388 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74e29c4a-b9a9-35e5-9a5b-87b99b9899a5 | -7.58072 | -45.41918 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83279669-b55c-31be-963e-6c20d94d22aa | -4.91446 | -43.22917 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ce1a923-567b-36db-8575-d011ede62b67 | -8.82722 | -52.05434 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c0543d2-dd02-3a90-b08f-1c459ee84a43 | -5.46063 | -44.86804 | 2025-08-20 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ddda2b6-4de1-38d6-bc0f-ac205df0175c | -2.90635 | -48.29666 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ccc3cec-350c-3ccc-a8ce-c034eb50a072 | -3.38496 | -47.6059 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README31.md)
