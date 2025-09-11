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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf5ac35f-004d-3408-9472-4fc3c8a3a1da | -6.19068 | -43.3977 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e5a4d22-d37d-3207-ad97-2ecef08288a7 | -5.73241 | -45.5917 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc10aeda-654e-36f0-a0c5-baad792ad674 | -6.54572 | -42.4356 | 2025-09-11 04:21:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c92be855-4af7-3ae2-9d97-471754b7da8d | -6.83764 | -47.89932 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c22f02b6-73db-3d94-9b20-56a9416cdf18 | -6.20147 | -43.52702 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ea9c6e1-aa04-3c4f-ab1b-d0eb93d3eed7 | -6.79525 | -43.41638 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e9b5092d-aa0f-32d9-9d82-ebaea4802c8d | -8.52377 | -45.6931 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8717a68-0ef7-3c51-b59d-20c84b9df698 | -7.26613 | -39.38515 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93ed0bd3-3f89-3a43-83bf-ad3cfc7b2fc6 | -7.18886 | -44.95827 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1b13915-ada8-30e8-a326-5f6831089eca | -6.63487 | -44.08107 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5153cee6-33dd-36d6-82c5-5de65aa01f33 | -6.28498 | -42.20553 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32cfc81e-5871-3c34-8321-2f0381dbc603 | -6.2979 | -44.5875 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64663270-d822-33fe-8206-fab36a15c39d | -7.88849 | -46.04444 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d383286-50d2-3859-8767-8b21577297e7 | -7.08494 | -43.8783 | 2025-09-11 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f8e390a-a4c8-3a3e-8d23-3d146ffc187c | -4.04249 | -49.0778 | 2025-09-11 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de6f30f5-ae55-3adc-a688-b01644629cb4 | -8.09872 | -48.24316 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c6d8638-d9cc-3638-9bf2-19a44761edd9 | -8.16635 | -46.09282 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 96dee690-ae73-3bbd-b2b3-91171b64666c | -8.02945 | -44.49426 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6fcabf3-f389-3c98-969f-779fa338eba8 | -5.40406 | -45.94068 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec567120-bc22-3b8c-8697-262afd34033e | -7.47441 | -45.28901 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6283cd23-3af2-3929-9695-294829526aa7 | -5.85065 | -45.12312 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70e629e-4244-30df-92bf-b5d4f6a54220 | -3.40513 | -42.99781 | 2025-09-11 04:21:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56701281-b333-3d51-99eb-1dfad4f735cf | -5.48764 | -45.61491 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c40c922-715c-34fa-a175-b0dfbe1c01fc | -6.63875 | -44.07809 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96cd362-142b-3082-b5e1-f7276a43e55c | -7.23869 | -55.05541 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da71de40-6e61-3ab7-b104-77beff340ee1 | -8.07356 | -50.17602 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86dd6b75-08d2-3dc1-b7d8-820c9b70ec4f | -7.20659 | -44.95396 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 051e44ab-9a12-38b9-9f66-dc81058df27e | -5.69463 | -43.3364 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98d36d46-223d-3f36-ba12-62dda0f3de2c | -7.18276 | -44.95374 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f8d5c43-99e8-3a1a-930e-3398a91fc537 | -5.60065 | -48.1188 | 2025-09-11 04:21:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75a35165-3b00-3267-8b6e-a0c3de6557e5 | -4.65293 | -47.03546 | 2025-09-11 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c52da31b-8e9a-3925-ad57-7adbeca3a1d0 | -5.56999 | -43.44091 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eeaec1c-58a8-30f6-8f00-70d50577f323 | -6.55544 | -47.5107 | 2025-09-11 04:21:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cc7a5b3-a1dd-31d1-8884-cba084d1bf88 | -6.43915 | -44.40053 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81a34b96-f76c-3983-a3b5-a6f617104908 | -5.66592 | -43.89454 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f2bd610-6260-3f00-be5b-0460bbaf1c69 | -7.92801 | -44.86491 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab53f818-e722-3110-8550-71343467e5ab | -8.02636 | -48.65535 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b58c178-512e-3607-9999-d6e7184c3a7b | -6.31404 | -43.81888 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18adecf3-0b1a-3812-b6bb-edc6603615f9 | -6.39676 | -43.50921 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e80d5bc-be78-3e4a-9991-d99f5af4a2c2 | -7.48495 | -45.28712 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efd5f76d-17ba-3f35-ba51-560e499350ca | -6.39395 | -43.50513 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e29b4f-7bef-3e50-8ba9-a587a7b305ac | -5.50827 | -46.65705 | 2025-09-11 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d951756-6c58-3288-acc6-ffba981f48e2 | -8.19835 | -50.10257 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9ff52706-42ee-339f-941b-4c6d9976fa56 | -6.36654 | -45.16183 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b8b3234-96bf-34ab-b7ea-75a4bf81fac5 | -8.43983 | -49.11767 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09fd14ec-7597-3794-b89b-8ba18c5ef272 | -8.44056 | -47.2667 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 766851e6-e93e-3605-a7bf-941b41ebe224 | -7.48889 | -54.9561 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6133c5a1-4458-3d7d-af32-e7218c0faa9a | -9.14689 | -45.55981 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 200fa267-202e-3d4d-845a-014cf1a01aa9 | -7.87793 | -46.02445 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79262994-4b39-30af-8e50-00c8c0627d82 | -6.52684 | -42.91646 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b287d9-6725-3d7b-8bcc-87fd97d1d07a | -8.51432 | -45.68797 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f2a7ca1-3ad8-3d22-8494-d2cddcc3de0f | -5.97822 | -45.80872 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc61883b-b142-341d-9ba8-c76a8bf5ff41 | -8.07974 | -50.18882 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23693e98-2163-39fd-8976-7ab40f30810a | -7.9028 | -46.25614 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef2542bb-b695-3721-92b0-155b417d4f79 | -6.34684 | -43.78443 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e34c422-1d2d-3599-9170-67ad775ca2a5 | -5.85229 | -44.17311 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93d3342e-53d8-3f7f-8719-86b180463a12 | -5.36875 | -45.96526 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd1eaa3d-68d2-3efe-b815-44c647116aaa | -5.68737 | -45.23728 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b28b9057-0d66-31f7-99d5-076d68bd7a9a | -8.04256 | -48.67279 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e0c85f4-ddff-358c-8e83-f56e08fe3165 | -4.41696 | -47.95584 | 2025-09-11 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10f2fad3-792d-3b7d-96b4-d835cfe26f6b | -5.22398 | -45.42743 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2fbae2a-6f82-374d-9a08-7c84a4fbd7e6 | -5.72542 | -45.41996 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbebc649-b818-3ac4-ba47-8b6e6ea8702d | -7.88791 | -46.048 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7827580a-32b1-3d08-9d1a-209cc71dfffd | -5.89941 | -45.77434 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77dda35b-971a-3209-882c-a2c0330b7c17 | -8.43417 | -49.10885 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a61d8dcc-a520-333e-9a9a-2e4a6c315590 | -9.00067 | -46.07769 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e308232-5209-3c3b-88da-e7575ab59493 | -6.17504 | -41.07228 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac679b6f-fc0e-362b-874e-bfbf17423e23 | -6.54164 | -42.43893 | 2025-09-11 04:21:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 91b18902-059a-3e30-8db8-9234ae34e055 | -5.62075 | -43.11258 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f6817bc-318e-3058-9d2c-53309c6b0e93 | -4.43976 | -38.45601 | 2025-09-11 04:21:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6a648e73-1d73-379b-b9de-1ff88b6f5e1d | -5.48176 | -44.11547 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83d244d3-cc9c-3232-a9f7-e6d8a1a81817 | -7.22193 | -44.81378 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b617b0e8-c826-376d-a022-cd24920dc520 | -7.9197 | -44.87431 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfa83ef5-a54d-3c26-a679-3faeac6804f1 | -6.38345 | -42.57886 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb20a428-30a3-3b01-b33e-64f42277b9ed | -5.82086 | -45.27289 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19187cd0-7735-3f6c-97dd-c36911e04ab9 | -7.98966 | -45.79905 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 517d35be-1974-3771-8916-d4d5114244c5 | -4.29 | -50.59206 | 2025-09-11 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13328983-09e0-3a10-ba86-9de404482865 | -5.6935 | -45.3282 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5e95d76-c104-3e10-8a06-072ea88acee4 | -5.40301 | -45.92564 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35ff6e4e-7ab9-3906-b42e-8c3ef6a0e4d7 | -8.66114 | -45.72656 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca1dcc5-7b6e-3462-9c6d-ab06a927f981 | -8.51541 | -45.70262 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f53d7baf-6a04-3c0e-bdd9-37245b71029d | -6.75012 | -51.96143 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5fe9dbb-8041-354d-8b3c-a65dc20af445 | -5.95289 | -45.81564 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11310e65-8b1c-3b6a-a5eb-67586b288d45 | -7.92248 | -44.87832 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0b00ffa-42fe-3434-a72d-dcfaaabf3df5 | -6.83095 | -45.61761 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c7f0966-9e15-3f1c-8423-3c75c5192e69 | -6.9035 | -47.90602 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ab879cc-1fd0-336c-bb51-ef4aac220d09 | -7.48128 | -46.09677 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4d3a808-8999-33f1-8862-de9a06e197c3 | -5.82328 | -45.27297 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 125b59e4-f044-3db1-9c8e-74f158132b8c | -5.67034 | -43.88808 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 599363ae-0199-30ab-afa3-d1b64ac7bf47 | -5.68684 | -43.33192 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64c7eecc-0476-399e-9516-4b09d7134edb | -6.304 | -44.59202 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cde4fbb4-f3cb-32e4-a0b5-a12f1eb5e8e8 | -3.49958 | -49.56541 | 2025-09-11 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1a4c2c9-4ff1-3cb9-b3df-f7204d2b7a5e | -5.78851 | -45.45537 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eca600a1-f150-3929-ba49-a9e762bcb418 | -6.4114 | -44.3819 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 493c74e0-91ef-343c-965e-933159d625fa | -5.79736 | -45.43472 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed5baa2-3cb1-3632-bb9b-151e30f555e4 | -7.16053 | -48.88881 | 2025-09-11 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efaa200d-5839-3f29-8992-3361d8d8165b | -6.38069 | -44.4298 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a82933-a1b8-30be-bc00-f0e677cad531 | -6.99551 | -44.79165 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b999d6a3-0731-3ec8-a834-72aa601663bf | -5.40465 | -45.93704 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 857e9012-2d24-37ef-8bba-6780e814be88 | -3.79838 | -51.15746 | 2025-09-11 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README53.md)
