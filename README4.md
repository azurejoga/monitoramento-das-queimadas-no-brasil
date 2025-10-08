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
| 01a8acc7-518e-35a1-a151-fa8ede071747 | -12.0036 | -46.7667 | 2025-10-08 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 52bab2c3-d971-3800-b361-7cf6f7565059 | -13.8112 | -45.8057 | 2025-10-08 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7cdc8e60-d83d-3785-bd1e-5b26eddf8113 | -3.4422 | -45.598 | 2025-10-08 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 869018ea-8e2b-3eeb-8eb3-3906a757620b | -6.9982 | -42.878 | 2025-10-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| e02188d0-c730-3310-8238-c6f10c200a20 | -3.7937 | -49.4211 | 2025-10-08 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a292bb5a-9cfa-3763-8d91-13d5f3175c10 | -11.6701 | -50.9641 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3be4f186-7460-3001-ba37-e5a7ff06df24 | -12.031 | -45.2132 | 2025-10-08 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 45352dae-d2a5-3568-9276-8a61d55d276e | -5.8469 | -43.3995 | 2025-10-08 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 4b97e3f1-98b6-3c6f-9954-a243bb0c3eb7 | -5.1227 | -44.9682 | 2025-10-08 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 02f672d0-232b-38aa-88b5-a3a66c3db1ee | -11.7079 | -50.9811 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c697f30d-05ce-31c9-a18b-cb65853b76a4 | -10.93 | -51.0229 | 2025-10-08 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 60b359c8-99a3-3ffd-b0f9-4364405a09aa | -21.101 | -44.21337 | 2025-10-08 00:50:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 5da2817d-ea69-320c-b5c5-4dbe9d9809c5 | -17.26402 | -46.91345 | 2025-10-08 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 906203bf-42c9-3438-830f-9063df5b0311 | -17.82779 | -57.62183 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 3638287e-4872-3719-8c92-2d53cc18736d | -19.51498 | -44.07038 | 2025-10-08 00:50:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5c0b326f-a758-3ad0-8362-7d6dcfa1c4da | -17.94489 | -57.52986 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 92e8705b-fef0-36f7-a472-d45a919e9a11 | -17.16142 | -56.59804 | 2025-10-08 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| afe53d40-e73d-39ec-be30-039ce811c06f | -15.40061 | -48.01722 | 2025-10-08 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 28caea96-297a-38d2-931f-af3a7829efe6 | -18.42463 | -45.19858 | 2025-10-08 00:50:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 340131ab-8b0f-3f1e-9344-77e27c243f42 | -19.46906 | -45.95297 | 2025-10-08 00:50:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 03b676c0-978f-37e7-bcf4-3111782035af | -15.38986 | -48.01888 | 2025-10-08 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e69431e8-2cc3-3b3b-91ff-630f972cbb17 | -17.28409 | -42.66615 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 739.7 |
| 8244d743-da2e-3a83-88e2-d91c99a2afc2 | -21.0998 | -44.20736 | 2025-10-08 00:50:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 98070ee3-ee58-3ec9-baed-422c98357054 | -17.97502 | -44.97373 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 3db96c09-726d-3fb8-ac23-3fc42a929c5a | -17.87319 | -57.64534 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 374cc9c7-42a9-37a9-a89d-1721ea245636 | -17.97882 | -44.99467 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6bce5b0d-abf9-3ea8-a040-2f599cf62223 | -17.93098 | -57.5136 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 10e2dab5-0b1a-37ba-afca-2669c2a713e4 | -18.42808 | -45.21808 | 2025-10-08 00:50:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e49a4f43-8855-367d-b213-6c86bc1970ad | -17.27313 | -58.11221 | 2025-10-08 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 1f738b83-4e95-3416-b7ab-2817988a54a7 | -18.03045 | -44.31314 | 2025-10-08 00:50:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9bf7bb6a-3371-362d-825b-711e71edad01 | -15.38013 | -47.31904 | 2025-10-08 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b100d548-4fc2-3c9b-96ba-b9566abe3eae | -20.19332 | -43.93891 | 2025-10-08 00:50:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 43210eab-b58d-3ef9-900c-be0f8c7168c7 | -19.30303 | -43.17606 | 2025-10-08 00:50:00 | TERRA_M-M | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 3e26f386-dde9-3429-8d69-ad62ae78431f | -20.88206 | -48.68656 | 2025-10-08 00:50:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 1215b219-4b88-3d20-8c1c-0da03806ec12 | -15.08232 | -46.63353 | 2025-10-08 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6e61b82e-9dd9-3c34-98e6-198488522fa9 | -17.98481 | -57.50216 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.1 |
| 24920a6f-6b0b-3a6f-b2ea-3006ef9c8013 | -21.02271 | -44.79892 | 2025-10-08 00:50:00 | TERRA_M-M | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a8341de1-67d0-3c0c-8cc3-339aed7a5434 | -17.96909 | -48.55572 | 2025-10-08 00:50:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 152a7064-68f4-34ae-812d-2f77eeb66d59 | -19.50726 | -44.07763 | 2025-10-08 00:50:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9e916079-f5bf-37a3-949b-5f96e0c48306 | -19.51929 | -44.09381 | 2025-10-08 00:50:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 67d9b9a5-ca81-3bbf-a838-efa985a71a7b | -19.85364 | -46.16563 | 2025-10-08 00:50:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 91d39e13-c8f0-3165-897d-90ac751f8805 | -17.97692 | -44.97895 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4a85efb4-225a-39d6-b380-b58453fbb51e | -21.59913 | -47.36805 | 2025-10-08 00:50:00 | TERRA_M-M | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 5aede894-8f67-3d8b-b6f4-f301cdb5e919 | -17.27863 | -42.66027 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 423.6 |
| e76be35d-21af-3d5a-be8f-7997419a59b5 | -17.93912 | -57.52411 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.6 |
| d955bb74-2b2b-339c-a2d2-de2ed74fe4ec | -19.85429 | -46.1765 | 2025-10-08 00:50:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0a8568a2-b1ad-348b-bbde-cf0d60403803 | -15.35753 | -47.32314 | 2025-10-08 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2e8717cb-6f36-3ca7-a0b3-470b8946c902 | -17.28563 | -57.99771 | 2025-10-08 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| e3021d28-cb1c-3863-b18e-be9be53aa7d1 | -15.07932 | -46.61559 | 2025-10-08 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fac97799-4403-3bc3-a661-fded14b70b8b | -17.43734 | -45.8214 | 2025-10-08 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7ad5a00a-2c77-3df1-933e-e8a0c5e6bc46 | -17.29959 | -42.66292 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 774afcbd-14a6-375d-b513-5ac86c71c95e | -17.26231 | -42.63582 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 22ae2b82-e8e4-3654-9017-1e1f28047fb9 | -18.07208 | -44.46912 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 8935cd4b-23e0-3255-a294-0af67dabf954 | -15.49134 | -47.93748 | 2025-10-08 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| dd7e3283-43d8-3b9b-940d-229fd4daf932 | -18.0227 | -44.94231 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0aa4a955-dd32-35ac-9126-7cf837b0e1ce | -17.8677 | -57.6529 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 7fd3f643-b9fd-321a-9864-e7a05a79c7b0 | -17.28764 | -42.62333 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 125.6 |
| a76b79cc-0b24-32cf-a987-ff720bdf8852 | -17.94094 | -57.54102 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 797085c7-1a9a-3d33-848d-47b6000630fd | -18.67759 | -47.41642 | 2025-10-08 00:50:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 9b014c8e-b5ac-3d07-894a-3b2bf61d851f | -21.02075 | -50.69971 | 2025-10-08 00:50:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 402513cf-3cd8-3d71-8832-7209e14cc798 | -18.02638 | -44.96306 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 249d0aa0-4f12-374d-aa7c-86ccdc22a588 | -19.85147 | -46.16034 | 2025-10-08 00:50:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e0596134-8e3d-368e-a1b6-eab3c9275727 | -21.07111 | -46.8941 | 2025-10-08 00:50:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 397f7526-bec4-39cb-9cbc-f42bfcda6103 | -19.32927 | -44.2152 | 2025-10-08 00:50:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a7bcb17a-cef4-39f0-9cfc-893fd6f4e429 | -17.93284 | -57.52995 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.1 |
| d64b76fd-7817-3535-99ec-dd017c5ff035 | -17.86124 | -57.64696 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| f1979727-b659-3dba-ab4d-ddfdf4a010c4 | -18.05586 | -57.53712 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 787582ad-f278-39c5-9caf-025c3bb44cf6 | -21.18713 | -47.61583 | 2025-10-08 00:50:00 | TERRA_M-M | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9796e9ae-4592-3183-bcee-1277ecaf3ced | -17.27793 | -42.63305 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 473.8 |
| c93d896f-74e3-3123-a917-8b84a2d7dac8 | -17.16314 | -56.61247 | 2025-10-08 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 4e2ad235-a35b-32c1-83cc-14af1f7b3bdc | -18.41157 | -45.20718 | 2025-10-08 00:50:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d62e6a85-541b-3b4e-be5d-859950e32514 | -17.82956 | -57.6376 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 34a8fca9-0250-366d-9a6f-62cd2ca54a86 | -19.83096 | -46.16967 | 2025-10-08 00:50:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4bc5a073-8932-31a1-975e-21dd0a563a2e | -16.29591 | -48.28742 | 2025-10-08 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b6ba70bb-2539-38c2-b7c3-5f931257e1b3 | -18.05884 | -44.47238 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f1fa65e8-5eae-30c4-bd64-c6d8218841c2 | -17.4851 | -43.3362 | 2025-10-08 00:50:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2fae0e2b-22fa-370c-bd94-fc7b94d2d484 | -17.2934 | -42.62945 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 910925f9-9c76-38ca-8078-44340e417021 | -17.26857 | -42.66926 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 42983c7d-4ba4-3930-b184-df736e0343a5 | -15.39208 | -48.03267 | 2025-10-08 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0d86cb91-bf42-3186-aca4-b969d65e9e39 | -19.85088 | -46.14903 | 2025-10-08 00:50:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c4a8de3d-a408-3b79-8ac6-da307b3f911c | -17.98295 | -57.48539 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 9c703a20-7e16-3430-a9fa-54577db890e4 | -17.27003 | -58.11813 | 2025-10-08 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 320a5ef0-e999-3844-bdef-fb6204b68290 | -18.41222 | -45.20173 | 2025-10-08 00:50:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| be44add5-0962-3bbe-b1ce-0f12132ef41f | -17.92713 | -57.52446 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.8 |
| 1332fd42-48a9-30a9-b8d2-ef58d0b52cdc | -18.67336 | -47.42381 | 2025-10-08 00:50:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5016d523-4539-3ec6-bf38-a2a7268466b9 | -17.94289 | -57.5126 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 8783daeb-1671-3af4-8f2e-ea1becbd632a | -18.6839 | -47.42175 | 2025-10-08 00:50:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b57223eb-ab4d-38f9-a7b9-147f33571b03 | -17.85545 | -57.59305 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| edd3b4f5-693f-3965-bcec-b574eb967b4a | -18.06711 | -44.46563 | 2025-10-08 00:50:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| ba24dbfe-e23e-3686-8c95-4c73a2cf13e0 | -15.70006 | -47.51317 | 2025-10-08 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7cedab22-6c60-3db6-beb1-371da82a7ce0 | -16.71744 | -47.59342 | 2025-10-08 00:50:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6fc2fd48-7e2a-34fb-acef-2207d481e129 | -18.49618 | -42.90697 | 2025-10-08 00:50:00 | TERRA_M-M | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| cb5c6365-a362-3a95-9a73-3a7fb9cbdd1c | -17.93736 | -57.50781 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 7a10797f-e8c1-3adf-9385-39f7d0aa88fc | -17.92547 | -57.50889 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 96d5ae4f-998b-3b57-83ee-0c82e67e63a1 | -17.30035 | -42.68941 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 87adb80e-a3e3-33dc-809e-a7c9d7eb0e38 | -17.27213 | -42.62673 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8fc2178c-5342-35d5-9ec2-58ff42b0a108 | -19.33391 | -44.21991 | 2025-10-08 00:50:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 007dba1a-0184-3f78-ab01-029e3842f835 | -15.24735 | -46.36664 | 2025-10-08 00:50:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| af9e291a-7192-3c69-b70f-64bf9570d5bf | -16.13321 | -47.91123 | 2025-10-08 00:50:00 | TERRA_M-M | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e8d831e-aaa6-3f5b-9532-04b31ebfe35f | -17.53929 | -46.76099 | 2025-10-08 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README5.md)
