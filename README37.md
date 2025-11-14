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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385568e7-0493-3ae2-b9dd-e20b2382c2ac | -6.23998 | -46.23908 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7423bb9a-ba38-3088-b66a-a84d4dd7d44a | -5.61545 | -41.06097 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 764658b7-cc87-36d6-a02c-05cf0bf1b6c3 | -6.11089 | -41.59602 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b516511e-8288-391e-8f2c-3ecf5b66d16c | -5.47057 | -41.40019 | 2025-11-14 04:25:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fa50027f-989c-3581-89ce-3f51ca8fd725 | -4.90454 | -48.62524 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0f93b74-118f-36b4-b245-562790d1fb5f | -4.5353 | -46.41378 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db0616a5-4556-3b45-9858-340e4aac9fff | -5.57633 | -47.0995 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b671207a-8b88-3982-852f-d615cbb06e3d | -12.01911 | -46.76804 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b0b4e7e-c45d-37a0-bfc3-d24fa5158741 | -6.48634 | -43.75748 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fbecc75-7c1c-347a-a070-5c990f205d8e | -13.48725 | -46.71479 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ea5d56-cb35-366e-8084-0b0bfb977492 | -5.8431 | -47.67981 | 2025-11-14 04:25:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1d960d-4457-3f34-951c-e57d80565e88 | -6.45233 | -45.65999 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aed3bf4-6bf3-3d28-9d7c-ab39cc569b50 | -7.00342 | -42.78744 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e54bc8f1-ebff-3f64-8506-1a707c99bb50 | -5.59191 | -45.17792 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e305821b-eb09-3a78-aeaf-2b7c25ad883a | -5.74237 | -42.73293 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d4ed45b-0050-366b-8f79-35847bda592a | -4.71148 | -46.44443 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9309338-7205-3ee3-8a9c-811bd68407dc | -14.9016 | -46.23876 | 2025-11-14 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8d4c3d6-2f21-3858-87d5-86609f61ee3c | -6.09645 | -41.5941 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9484b94a-99c4-33d5-96ba-f3fbbee7669c | -17.62588 | -39.9221 | 2025-11-14 04:25:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0c405e18-8c23-328e-8bca-2d54a0152ec9 | -12.58421 | -43.35874 | 2025-11-14 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a890f2ab-330e-37aa-807e-c23fac4a44ea | -11.85734 | -49.22896 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3b1260b8-c848-38cb-a010-c05eb4d62412 | -6.07275 | -41.57429 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 44d25f27-6b10-35b9-9e13-488cd9464606 | -13.66191 | -44.21521 | 2025-11-14 04:25:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce8fd5b-d89e-3f71-900c-444f0619afca | -6.06146 | -43.68402 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ab9b781-249e-33ba-be63-cb30d3253007 | -12.90702 | -46.34246 | 2025-11-14 04:25:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b14671c9-6f22-3c84-9e4a-6460dc7e0d14 | -5.01031 | -50.91575 | 2025-11-14 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bce0e8e3-1365-3bfc-8a33-87313b7cb4e1 | -5.5728 | -47.09897 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f668b6e0-d49d-357a-b2e6-4f5ab13700b7 | -14.94649 | -49.79258 | 2025-11-14 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb294690-2d13-31b6-a0b9-1138e57b27f7 | -11.7403 | -48.52698 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d10a7c1-6550-363c-9023-b5081b457306 | -6.09459 | -41.6065 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cad4fab8-0dd1-37be-b5c2-8dfc7ea702a1 | -6.97726 | -39.17031 | 2025-11-14 04:25:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ab77230e-24e9-3d20-8851-49cec252287f | -17.29835 | -46.82954 | 2025-11-14 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2113d22a-4e45-3444-9c76-ce093d9cbbbe | -5.52274 | -41.74783 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3cd7fa6a-7d25-3825-a15c-6ee24859cc3c | -7.14402 | -41.70855 | 2025-11-14 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e5f27a80-f67b-3ae5-befa-606c476caa0a | -11.8479 | -49.21846 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 468fb9ee-8d80-3f33-91d6-bace1eb18f66 | -16.03576 | -44.97256 | 2025-11-14 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55ca5c58-43fc-3937-a23b-9587a4d6663d | -4.68752 | -45.85698 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70059d71-9446-3ca1-8062-b871c6a61d09 | -10.34025 | -49.91554 | 2025-11-14 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 405cde5a-1aa4-3262-8bf5-725ab19bbc8f | -5.71797 | -42.9129 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d770d9ca-1212-326e-b263-2b738218accc | -6.8858 | -42.8509 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0431f45-8f35-3e5f-b525-309d825f5f13 | -6.10789 | -41.59147 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e28235af-e686-366e-b7c6-c980159624cd | -11.93477 | -43.94955 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcb47ffd-d97e-3db4-a223-eaec4126f6be | -12.66737 | -46.75772 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bda1798-d51a-3f0f-ba51-9b575444ae45 | -4.71494 | -46.44497 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b6434549-60cc-3457-ad17-702edfbec6c2 | -14.70481 | -46.613 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 248fb531-9a1c-3aef-948a-611de949f603 | -11.60663 | -45.11744 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a13e5416-3221-3655-9fe8-e8ff78bae908 | -16.47369 | -42.17213 | 2025-11-14 04:25:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be45b4f2-7390-3c6d-82d5-48adcce88d9b | -6.10665 | -41.59974 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42816bf3-7cee-34b6-8c0d-5fb9d76fc6b5 | -5.7481 | -42.74117 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 25000ea4-a8f9-309c-9b12-82efa3ce763a | -12.62198 | -47.01786 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a27237e5-63f4-3c30-b3d6-ec9810ca11f4 | -5.42376 | -44.80869 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6097cc-366b-36c4-bf87-b7a0b46093f8 | -5.72073 | -42.35831 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f651af1-5af0-3b5e-b96e-a571c550de27 | -12.70927 | -45.42454 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c47d16c-2c58-33f2-8cc4-9a3efb4a3390 | -12.68815 | -45.42845 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ec2ec76-df4f-39ab-a830-b5e764658f17 | -14.91687 | -47.36414 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2bb8657-0585-38b4-85af-96d7ba582747 | -6.10727 | -41.59563 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 490d854b-b73f-3c4c-ab2c-12a354a9102c | -6.54744 | -41.71143 | 2025-11-14 04:25:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28cb900b-cf87-350c-9ff0-cbc692c2729c | -17.03281 | -46.75552 | 2025-11-14 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d154cb0-b6b2-30b4-a93b-e5df82e23128 | -7.05611 | -45.06124 | 2025-11-14 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f923d7e-88ab-338a-8222-91415abf9594 | -6.44899 | -45.65945 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebe9ef6c-0da9-3544-9e8a-7770cb63ddd0 | -11.96629 | -43.99727 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6da4068e-27ea-3dfd-aa1d-1131b403f2f8 | -3.41689 | -52.7314 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed747a07-9384-312e-9693-b705cf7f003c | -13.33178 | -43.18794 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 339fa753-3d9b-3ed7-9093-217663595616 | -7.42497 | -39.10468 | 2025-11-14 04:25:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f056563f-b08f-3669-aa70-8b99b4d20186 | -7.42072 | -39.10397 | 2025-11-14 04:25:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 34a1ccdf-efa6-3ae2-a5ad-a631891a292d | -6.88523 | -42.85465 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6ead4001-ea73-36fa-b523-8e23030602c9 | -14.69816 | -46.61189 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1226f323-a8a6-3648-852e-ad7bd564cf76 | -4.73084 | -46.72923 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc460a7-0128-31e7-8e11-ede39239bd14 | -5.7065 | -42.76126 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50000664-a031-375c-8d0a-2617b7adfecb | -4.64874 | -47.94925 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d6d5f96-7985-392c-9684-fc6240472b14 | -14.66448 | -46.56602 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56cf043c-b745-3755-bcb0-93ce7536502a | -11.31801 | -48.5034 | 2025-11-14 04:25:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6acb873-91a8-32f3-ad6d-608a1f8565b2 | -7.14766 | -41.70898 | 2025-11-14 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6f08e2ec-84c2-3e55-9a47-21901e8246cb | -7.15175 | -41.26042 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb1124fe-cc7c-38af-98a4-4b04c510a8d1 | -10.45712 | -49.02374 | 2025-11-14 04:25:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05388f3a-ae1b-3130-8c08-fff297d45c8a | -4.79574 | -46.48459 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27205b0a-da18-3647-83ec-19a12bdaa47f | -12.68705 | -45.43557 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7269443c-8f66-3024-a40e-ea2591fd93ca | -12.9037 | -46.34192 | 2025-11-14 04:25:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27416c07-6a41-340a-a2a2-6f7a59ecf770 | -5.53842 | -49.36699 | 2025-11-14 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c649b7-2532-3171-b5f5-5ff136391c2d | -5.42165 | -42.57429 | 2025-11-14 04:25:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c5b08aa-cffb-30c1-8ed6-3df7c264ad28 | -6.06971 | -41.72321 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6288f21f-2c50-3f85-a66a-ae0a28b2f80d | -12.58776 | -43.35928 | 2025-11-14 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 860f77b7-378a-36bb-9220-84feebbe671a | -5.7242 | -42.35883 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c504e93d-7bd1-33b6-8730-4013d63d84b1 | -5.02469 | -44.50792 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33af32c1-fdf0-3f81-9510-39313a9aedbf | -5.54086 | -41.81964 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e2b3dde9-172b-34ea-b69c-c67b779c675c | -14.77656 | -46.67236 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f525c4c9-915e-319a-a11d-d349eb0fb29b | -12.78498 | -43.62967 | 2025-11-14 04:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a378689-48ad-3c96-adcc-6bfdf6a8f7fb | -14.35304 | -47.89336 | 2025-11-14 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 484662ea-46bb-375c-a7f1-e2484ae8d495 | -14.28035 | -45.35962 | 2025-11-14 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 476b0e37-15e1-368f-a935-1236b0b1381c | -14.67777 | -46.56823 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 887f17e3-5398-3795-a16e-f8e40f9487da | -11.82556 | -47.78141 | 2025-11-14 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bcd5ae2-33ba-39f4-ae2c-a383b4c64513 | -6.13716 | -48.05468 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a979dedd-91cf-3bc9-b966-71e8917d39b2 | -10.84179 | -48.0238 | 2025-11-14 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca988351-f66a-3e77-97d9-60c2327a3537 | -4.98703 | -43.88874 | 2025-11-14 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 967a46f0-e226-33b7-9ac3-992eb053e658 | -6.28372 | -41.73623 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d9b8136-d255-3071-bfef-0f40ff121093 | -6.09583 | -41.59824 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b03dcb1a-c6bf-3fe0-b1fe-19481c63008c | -4.84821 | -45.59461 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 215dbb15-ab66-35e2-8c7d-a966749495af | -15.54932 | -43.17171 | 2025-11-14 04:25:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7d7b2f2-acf5-3657-9ca3-2f89e9cb5da2 | -6.14367 | -48.05361 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01941928-de0a-3f78-8ad8-f68f6514b0f2 | -6.88122 | -42.85786 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README38.md)
