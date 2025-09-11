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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15945690-ed17-3da0-8152-3be716e8dd26 | -5.42982 | -43.41536 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9677c0d4-d78f-314b-ad62-7bf32852313d | -7.39662 | -47.37704 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bccb9f55-3d8a-3bec-8dbf-bf4aaafd8cfb | -8.7319 | -47.09206 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9f49c501-d38c-3fbf-809d-c8ed3d9dee27 | -6.39788 | -43.50207 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6e48fd2-79b9-3a88-b874-b286517b6226 | -6.16156 | -41.06122 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ec3067a-2610-3dc8-b68e-5a36f2c11fb2 | -5.62027 | -43.11229 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b43b7f1e-bf85-3030-9562-0fe8bb97173e | -5.73561 | -45.29177 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57ae5f68-5fd6-333f-8b8f-7a132ccd43ff | -5.34346 | -44.80379 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d64acbc-bdca-36fe-839c-bd03107150c6 | -6.83486 | -45.61464 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d73927a-c824-3d26-bbae-812fbd244c99 | -8.52654 | -45.69714 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cabcd625-ba86-3074-9d07-de882ccff8c8 | -5.46373 | -44.8516 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fb4eb33-9193-358b-8d25-3fda8ee23acf | -5.35824 | -43.41144 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe1dd158-046c-338c-925c-4ee8abc031c0 | -3.67679 | -47.49463 | 2025-09-11 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea7e8bc0-d934-3a25-b5ea-d8cfd2a3bc33 | -4.5631 | -43.74357 | 2025-09-11 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 301934ff-a167-3ba9-b7fc-16000e937554 | -5.57665 | -42.92425 | 2025-09-11 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ac22e679-3923-3666-878c-503e53787775 | -5.8136 | -45.67719 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0312ded2-b1a9-3f61-b01a-efb29a3d266d | -7.5559 | -48.20781 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85d051e-44f6-3f3c-891b-a2d8359de894 | -5.22063 | -45.42689 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e0c29f4-69ff-36ab-b629-155b1679c124 | -7.08083 | -44.84796 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a361c10a-32bc-3f7b-addb-b7c08170f754 | -5.65148 | -43.89941 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38a11f0b-33d3-34bf-bcee-aea9436d9f81 | -6.35284 | -43.4145 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 259cf030-91ed-3891-bc69-8f9af1238696 | -5.6689 | -43.33638 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b5633d1-9bb1-30b3-933a-293484126638 | -6.40334 | -44.49811 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 209d142b-b04b-333c-a4cd-720265e646fa | -7.35945 | -47.42759 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3242dd9b-d6fa-3f90-98f4-a2b476e492b0 | -6.48733 | -41.74974 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0f12768-ea97-3d49-b53a-f0accaf18e92 | -4.38325 | -48.06853 | 2025-09-11 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d02a405f-2cb8-3f2e-b58b-b28a8f9b1026 | -7.70334 | -45.14704 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 546709fe-c25d-3a31-bf02-f5486192a757 | -3.14269 | -49.89556 | 2025-09-11 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c6c703e-2609-3885-8578-bca6e5b63a9c | -7.54584 | -42.52763 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 195ee81c-9878-3c07-9dee-2a665e6aecc9 | -7.69614 | -45.14946 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ab2a3ae-2a8b-3723-8d04-9fbc538a6eaf | -6.22132 | -43.49698 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a73966cd-db9d-3cf3-9e3f-4c8f6e2232e1 | -9.05075 | -45.78552 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f17965b6-e4dd-3d83-8c00-2153beb42b8b | -8.51043 | -45.69095 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8c1e02c-c5d7-315a-a546-96093dd3e280 | -5.93607 | -45.71788 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 919201b2-83db-32c4-936b-84b9e86723bc | -6.87153 | -51.97692 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58dd9664-f659-343f-8264-55e461502775 | -9.16683 | -45.58456 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abd497fe-1e4e-3bb9-aa9d-191260b8497a | -5.47254 | -43.43985 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b486461-7aa3-3898-b89d-f69a21c947a6 | -5.57761 | -43.56861 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 934c152c-4961-32bc-9bc3-212aa5c14a94 | -7.26147 | -44.60613 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 574bbeb9-88bd-3ff4-a1bb-cfc797386c5a | -6.25707 | -43.42196 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09d6be04-d731-3937-abc6-992399a1fe11 | -6.27661 | -42.40823 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 235321f6-a1af-3bb5-b345-07c4a99e89a3 | -5.74173 | -45.29635 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ed51d7-c791-3415-8a9a-d2c963f7dd5b | -6.32278 | -43.44315 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcc99dca-25cf-32c5-8ef3-c6ca0048707c | -6.34064 | -39.86008 | 2025-09-11 04:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2f31db14-1d9d-3fe5-a1a5-e911b5199947 | -5.38582 | -46.14008 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7870826b-9b7a-3e29-b39f-2991f842d766 | -5.68797 | -43.34666 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d24727ae-612b-3ef9-a6ea-373cf83a2cae | -8.02846 | -48.66567 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a1c05e3-d968-34ee-9ebc-20f08b22df3b | -7.53575 | -44.67083 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 564dfdce-8ea5-30c9-878d-a081caf4429d | -6.10126 | -45.9309 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bcb7e88-5516-303b-9936-6018b02664ab | -5.73046 | -45.40992 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65d95c7-67f0-3cf7-9309-1c2dab7f78e7 | -8.56715 | -45.59222 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81290a6b-a059-33b7-b5f8-52545914d489 | -8.93742 | -46.12926 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98cf548d-906f-3556-b576-76d2b8d26889 | -6.25199 | -43.41022 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9878b902-6345-3d71-9b52-7edc1a7524eb | -5.5728 | -43.44498 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2448d5b2-dc0b-3d4f-991d-c8ef31556456 | -7.49841 | -48.25957 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe840f40-0581-30b8-bcdb-d19845b517b4 | -6.40013 | -43.50973 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 805b99c4-2334-32d4-9149-9055bb13f94a | -5.93944 | -45.71842 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06efc643-c36e-3718-93eb-d2add68a98b2 | -8.42459 | -47.26905 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1549ef08-c439-358a-b5b2-a9b442b68e0c | -7.80828 | -46.08279 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39be6fa6-a4bf-3718-8859-24870265e6b2 | -7.18776 | -44.96523 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5575fc08-d2f3-3531-ba48-8a550fcc6b79 | -4.96148 | -42.99697 | 2025-09-11 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55f3f4e9-12a4-3093-9a82-44ecf361b823 | -7.92804 | -44.88635 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aca802f6-0142-3810-b885-1d73c491381f | -3.18183 | -49.44889 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6554536a-4e54-3830-82b6-fbb294890c01 | -5.23571 | -45.46194 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef16cac4-4a20-3707-b42e-d8d147ec7562 | -6.31266 | -43.41962 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0320da4a-7aed-3e87-be03-cf0ec6244da9 | -7.18666 | -44.97219 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4491a200-f842-32c2-af11-c326041f8829 | -6.7514 | -45.94334 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9cc39a8-4f9d-3410-a648-ccde0f4cb6e3 | -5.74722 | -51.69474 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2769ae51-a1f4-37f8-9f4a-1a2f4313c3d0 | -8.08638 | -45.56977 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3469384b-a4b6-35f4-9e65-3c0a50b11792 | -5.57609 | -42.92788 | 2025-09-11 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7a656d4d-56ee-3a6c-929a-d2db327aa7c3 | -8.08561 | -48.2322 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df287b54-9b7e-3f5e-a85f-d9558deedb57 | -8.02947 | -44.02134 | 2025-09-11 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5edb6005-617e-3033-808d-487e1c86e99d | -7.86373 | -44.88329 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29f06e79-3692-33da-96d6-5c5b826b65da | -7.31366 | -44.36068 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31c1120e-8f04-3086-87d7-9d86c42ac3ee | -8.48431 | -45.6832 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c12e40ad-474c-3c25-a2fd-57b4015a9a9b | -7.20437 | -44.94647 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f040cfda-60a8-3aca-b535-c4cb1545d21a | -5.51834 | -42.69098 | 2025-09-11 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fd9fc82d-4de7-31c9-86b2-a2a0d0a598c5 | -5.48707 | -45.61847 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d478fc46-6ace-3b47-b822-d200793162fc | -7.99356 | -45.79605 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35ba00a6-2c95-3c19-acfb-8bf639e3c9aa | -7.50279 | -48.25592 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 764f506d-fe00-36ea-8dee-870fa6f2b13e | -7.4683 | -45.28445 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e86d7f-7478-3a77-908b-7aed0a6288fb | -4.08579 | -48.04348 | 2025-09-11 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ba6cc95-49a9-3d2f-a976-c3875dd2c7d2 | -6.35709 | -45.15678 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed76cf48-610c-3ec4-a576-fc0aa80707b9 | -9.14356 | -45.55928 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76b1e00-44be-3f99-8412-e98a67452c6a | -6.56348 | -44.20956 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea68e1dd-573e-3458-8f17-7d75bc638e24 | -7.65951 | -49.84393 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7074010-1499-3060-a691-a8515904c530 | -7.83546 | -47.25425 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7b62b0-05ea-300d-b6f2-e25044690e7d | -8.10241 | -49.24913 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24050f5b-de4b-39e3-bc96-0a058c3829af | -7.91105 | -46.85431 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abd3c712-9078-3d5d-ac6d-508361eda360 | -5.60139 | -48.11432 | 2025-09-11 04:21:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6192065-ccc8-3712-bd94-90c220a58016 | -7.99673 | -46.32296 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed51096d-2425-307f-bb84-040af2a0e2c8 | -6.86199 | -41.48375 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66d23e83-15b3-36f2-9d20-bce5c6c1e858 | -5.40067 | -45.94014 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8b9db5a-29df-303e-929a-2f8e42a67462 | -7.90618 | -46.25669 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60460e60-16c1-3f91-9a28-cf48e08875e8 | -6.99606 | -44.78817 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65688dd9-cf27-35b8-ac79-6fc4fb6bc32e | -7.19164 | -44.96228 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0278cb2-721b-3df4-8a1c-fd4ab9b32e90 | -7.88456 | -46.04746 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d16ff96-266f-349b-9255-272d57d74832 | -6.31549 | -43.44566 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5632fb46-c8c8-3f44-a2d1-494c969d1f66 | -8.51376 | -45.6915 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b22f19ba-e185-3db5-8307-fb0e8dd2dc4e | -6.57191 | -42.94233 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
