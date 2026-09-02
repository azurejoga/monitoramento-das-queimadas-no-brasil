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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da0f15cd-7a11-3865-ad2b-ade475189811 | -6.04685 | -53.84501 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20b7a3ea-85c6-3ee0-8079-670bf3bf2a95 | -1.95385 | -46.48637 | 2026-09-02 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eca0a9af-0668-3e9c-bef6-07af4ffaab53 | -6.0325 | -44.43703 | 2026-09-02 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| badd8f6f-1781-3c0b-b992-0eae20a02ccb | -6.15159 | -55.67149 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 407c0693-afd3-3ea9-af3c-4e0840b04bb7 | -6.85226 | -41.65387 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78c800cf-106c-39ac-b3a1-44c8c744c180 | -1.96411 | -48.38221 | 2026-09-02 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62290081-857d-3cb6-aa21-90be3e0bb2bc | -3.61402 | -45.35319 | 2026-09-02 04:19:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0901243-5056-3162-914a-b77b44a07456 | -6.07765 | -53.6632 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d5684fd-238b-3ee0-9ebf-0927bd7ccc25 | -5.24623 | -55.90381 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90fd012d-3aa5-3da4-95b1-68996510105b | -6.20219 | -53.48279 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b6f4b1c-b1b9-3fe5-8a9c-c8abafe8fd14 | -7.65728 | -45.8776 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5a1da328-f1af-309c-a24e-3292b240645d | -4.35783 | -47.77534 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4022d6fd-81d8-38b7-a921-611314c27c0d | -5.85868 | -51.71114 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f906ed5-91c9-38fd-b4f7-0c33911c75f6 | -1.01912 | -53.728 | 2026-09-02 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4308fbb-d69e-3e20-a1b9-42bc0ce270a8 | -6.09592 | -44.13814 | 2026-09-02 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b18a872d-43d6-300f-89dd-cbaede1dbc93 | -6.25256 | -55.43306 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6815e1c-1fb6-3b5d-9faf-71f54f71d9fc | -5.02992 | -43.60108 | 2026-09-02 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a538d8d-af1e-31a6-b47b-b116db9c29d2 | -6.07653 | -53.66982 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 450435b7-8161-38e8-986f-5f7a549271dc | -4.49607 | -45.90759 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| bd954b42-6cce-354b-a08f-3a98a54cf154 | -5.24559 | -55.90826 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 740e3913-c895-3c69-8efa-c2542fe18641 | -6.1901 | -55.27918 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e579ef8-f54b-3c8b-85c6-3df1de92fc88 | -4.5 | -45.90453 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c96b9ad-9a21-3564-a145-fc154de2151d | -2.49561 | -47.1116 | 2026-09-02 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f035ac5-9a45-3912-9b79-3ce20efcf05c | -7.45651 | -46.15586 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 772ca450-ace7-3e7f-babd-44864ff90f4d | -6.2 | -53.48454 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61839241-a12e-3d25-a83c-6ec6c7ee6a8c | -5.9794 | -53.57932 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de776fe6-accb-3d0e-9da9-6de63470edc4 | -7.66503 | -45.87165 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4d9568d-f041-3bda-84bf-c470682604bf | -6.94791 | -45.19736 | 2026-09-02 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a0e13cb-2802-33c8-b013-0a572d2550df | -4.37107 | -47.78616 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf6a3b39-1a6a-340a-b4cb-780be76f4a27 | -5.97636 | -53.59278 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed96c6a5-9249-315d-a041-e50243690d77 | -3.24232 | -47.25028 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 689199f7-3fc8-3b00-a534-24bf6fa81c2f | -7.66116 | -45.87462 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db0159b0-a956-3a26-b0af-588fa6a4970d | -5.85597 | -57.56162 | 2026-09-02 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 347e63e8-4bbc-301f-aa0f-39985f2f2a74 | -4.12498 | -51.02906 | 2026-09-02 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9611f8cc-26fa-3ed4-b4b0-f16521acb164 | -3.84775 | -44.0558 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 880ed5bb-1054-31b1-9237-6bb2dac08823 | -6.07187 | -53.66557 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49b9406a-4928-3054-8ce5-a506f347f60e | -4.96535 | -55.84995 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a15d7e1e-e21f-35d6-93b1-db53d24e0989 | -7.0777 | -44.36269 | 2026-09-02 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b33a27c1-f254-3c26-8dfb-f288c5200e03 | -4.36445 | -47.78075 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5972ba4-3056-3051-be04-7e255120b043 | -7.60867 | -47.28625 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b42c6c69-0a7d-3506-af53-4ffa6aaa2cb8 | -7.16228 | -44.05689 | 2026-09-02 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3000de6-89f3-3419-9e63-993ec6a6b5ef | -3.21125 | -49.8096 | 2026-09-02 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9664eddd-9e30-311e-a060-85ad0cb0fdcc | -6.67705 | -43.40638 | 2026-09-02 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9a063b8e-3e76-348a-be18-b8711d975745 | -4.36218 | -47.77168 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6771975-8684-3a36-8618-672e3209bf96 | -5.39674 | -45.63006 | 2026-09-02 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 367740dd-79d0-3997-b80d-7f29e29e142b | -3.85766 | -44.05733 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1194e65-b604-3eb3-9f14-06f0c80c10cf | -4.34721 | -44.29947 | 2026-09-02 04:19:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad05c81d-6a89-3d29-9e25-ef1751a46916 | -5.40063 | -45.62708 | 2026-09-02 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7e093300-2a00-3741-b07d-80ffe049930e | -4.49827 | -42.55991 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e811feb1-74fe-38cd-9400-abb57ede00ee | -6.20273 | -53.47971 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a4350f12-b964-3cd0-bc52-ba47f2cc6056 | -4.36376 | -47.78499 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1ec8280-c3fa-3eed-9467-5658696cb7b9 | -3.85159 | -44.05287 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| afbe4fac-6798-38a4-8122-48eebcf89f9a | -6.76739 | -41.17107 | 2026-09-02 04:19:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c395a19e-36db-37b1-b6f6-74c3b0811a82 | -5.63917 | -43.55413 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5ca1544-cd43-343b-b5d0-14c594eb3baa | -6.14257 | -55.67197 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24404a78-3782-3c0d-a681-13a13ec6684b | -7.15285 | -46.84519 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3810f62c-98d9-3d3b-bdf6-02cbc0c5d178 | -4.55886 | -38.45204 | 2026-09-02 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64ed606b-3001-3d43-a74b-a1b129387969 | -7.11916 | -45.81656 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8e6b57-0ca2-3c69-9c31-0cfe3e2db464 | -6.20105 | -53.47839 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 075138be-982e-329c-9d9e-8b12794156b3 | -5.9728 | -53.58216 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520d8e75-6127-337c-bcf3-94c99af5570f | -3.37429 | -52.79895 | 2026-09-02 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14ad2b17-9b7c-3ce7-abd0-280dca09b928 | -6.84494 | -41.67828 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64a8ca52-cc08-3f54-8c65-5db18ee11688 | -6.4188 | -43.0735 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 959f4dd8-efcf-3196-a399-712d27d1a1a9 | -6.0463 | -53.84829 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 264de36d-fdce-35b6-a27c-965fc8f4ffb9 | -4.52179 | -40.55014 | 2026-09-02 04:19:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b412838-9031-317b-9868-788065568570 | -5.97748 | -53.58618 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c7ae4e9-ee5c-3e15-9522-378db835db55 | -3.85052 | -44.05975 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6039bb0-48a2-35cf-b55a-059b2c707380 | -5.64252 | -43.55465 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e5f90d7-3071-32b1-9566-c39435b17d1a | -4.36583 | -47.77224 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5f176f4b-1709-353c-a9f0-d2dee8297d31 | -6.0768 | -53.67065 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d14f52a1-579c-3c0e-86cf-1bc5514552cc | -7.03724 | -42.18674 | 2026-09-02 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7577d58e-008a-3407-9a96-aaea898bf8af | -6.80961 | -46.2021 | 2026-09-02 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb6479da-3e63-37b3-a9ed-8a21b7769bd9 | -6.14574 | -55.66988 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 308a4c8f-a313-3035-8bbd-6bc3337fe16e | -4.49944 | -45.90813 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 44934341-bd43-3e9d-aac6-48f7786e033e | -7.37175 | -45.0517 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff14a019-9984-30e1-88d8-743e1ce5231e | -2.82944 | -48.65455 | 2026-09-02 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c30656e-d42e-316d-b8a7-3fa4108338eb | -6.80626 | -46.20158 | 2026-09-02 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d8145eb-9c6b-332e-991a-32eeb231f1ec | -6.91451 | -45.7121 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d9a31f-6d25-3f91-b4c1-d3350376e598 | -4.37314 | -47.77337 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b974b0-6cd1-39ab-844b-213505d134fb | -5.93693 | -50.21204 | 2026-09-02 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d90999fb-ccec-3bcc-96b5-b63a038ae250 | -6.14418 | -55.67882 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b758206b-3c10-34e0-ba85-84f4269f7323 | -5.64197 | -43.55817 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7934b087-3e53-3f08-9de8-3d14e891b070 | -6.5446 | -49.82811 | 2026-09-02 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76417853-a739-3451-95c9-f9ca06a53ca6 | -6.98349 | -35.13433 | 2026-09-02 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 394da8b8-34ab-3c55-8f1d-53c97a0ad501 | -6.09646 | -44.13466 | 2026-09-02 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 996a9afc-e333-3108-a849-9af35303ad36 | -5.39729 | -45.62656 | 2026-09-02 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 20bdcb21-ecc0-3201-a41c-cf50be6bd807 | -5.97712 | -53.59221 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce7fda3d-aa4a-3cfc-a5fd-bb0fdcb2ce20 | -7.14021 | -45.81277 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde4eab6-987f-3b40-a14b-dad9c9edb9b4 | -6.91783 | -45.71264 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc36b4cf-2ca8-3a23-abe9-ef0165fd24ae | -6.07216 | -53.66642 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e39bcea-15a9-3497-bffb-a6d29629ae8a | -1.51112 | -54.95741 | 2026-09-02 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 97f523ef-ff63-39c1-b936-f66f85681599 | -7.52427 | -47.33188 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aff6a5a-8b7e-32e3-bc50-ae7be7371051 | -4.69698 | -56.05751 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8df5f75f-ccc7-3f80-a712-2d1523b07a51 | -6.09977 | -44.13518 | 2026-09-02 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7502ab3f-76c0-3f75-bd4a-3202fd965069 | -5.97194 | -53.59119 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7dbc500-b690-3bc0-ab54-66c3a96b1149 | -3.61067 | -45.35267 | 2026-09-02 04:19:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97efbe6d-97a1-361c-805a-f79e06101248 | -3.85307 | -52.04023 | 2026-09-02 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d0371cd-0d55-32b8-9824-0c02d900d69c | -7.14076 | -45.80928 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a50afe98-0fe2-3db9-9438-cf5d94d18494 | -4.97311 | -55.84178 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2b89f22-28c1-3bcc-a991-18890f9b6fb6 | -4.50168 | -42.56043 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
