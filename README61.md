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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e676a15-5dc0-3f89-b441-ab6fd36e64ec | -5.66239 | -45.14892 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0ecdbe8-f757-329d-bd1f-684953e50b62 | -5.87795 | -57.76495 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe9419a-90c9-3c1c-97ff-c80f621f8058 | -7.0303 | -44.66002 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09d92ea9-db73-34db-b7f4-a86a24ad2c5a | -6.77499 | -44.31549 | 2025-08-24 04:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8209a91a-24b2-341e-9b0a-a112613c312f | -6.20229 | -42.98807 | 2025-08-24 04:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dfea185-c6c9-38dc-ad0d-1267ffad6076 | -4.71074 | -55.93349 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6096f85d-728d-33ca-bb24-95e4d1f4ebff | -5.65322 | -51.84033 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f584a09-d581-3245-bcdc-faca973dc04a | -7.08064 | -44.62137 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d765a5ef-d024-376b-a270-2c9bf96a4e6d | -5.45291 | -60.18518 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fae6cb54-d838-3761-9da6-3ac934d15970 | -6.89461 | -45.687 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 819c0b0b-3729-31c1-b1b2-d13a23ede250 | -4.56136 | -55.96528 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10c63a8b-bdaf-3e2a-b0de-784196c03ec0 | -7.62771 | -45.24372 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68949b5b-de9f-3fdf-b29d-006fa1b6749d | -6.91864 | -43.78323 | 2025-08-24 04:59:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1efd36a-9dfd-3c77-bbfd-70a7e68e3dfa | -5.87572 | -57.75528 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38ef13cd-a84f-368f-a12b-e4c62dcf4aef | -7.59455 | -46.24717 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65f6265b-e99e-3c2f-b899-7433179b39d2 | -5.65764 | -45.14494 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23f64731-a2d0-399f-a200-d52fc045c1b3 | -4.13528 | -56.37169 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47a8b48d-0b2d-32af-8e86-95beaccf2f21 | -5.64977 | -51.83981 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6789be3c-7a25-3842-9e37-6119e1927fcd | -6.8938 | -45.69287 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9499cc8d-8af9-329f-b9f2-f242bb4cf170 | -4.48997 | -55.57026 | 2025-08-24 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e29262f9-3acf-3d59-a6b1-be52877a5c10 | -6.88637 | -44.85099 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdb72a1-0eba-3b7c-b1c0-288292ff7099 | -6.18742 | -55.46084 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7468e56-48dd-39ec-a92b-f0ea849cea43 | -6.87973 | -45.68112 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d8aa49-de1b-3525-bdab-b2b7c0b52d54 | -6.43492 | -44.55015 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2d3dd92-9721-3f55-a009-3c196c7dd9a3 | -7.17514 | -44.66394 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd49d727-7f14-3b41-9da3-89ddc087c22e | -7.59953 | -46.24794 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ac4766-f469-3fb5-bf62-a2ee1e53b4e4 | -5.42419 | -60.16708 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 987a1bdc-34f5-3099-abd4-0cf4e90c758f | -6.18716 | -45.43712 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa828ede-3dad-325b-87aa-7d0f6a7a2201 | -7.02075 | -44.6476 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9af02648-54b6-3663-87e6-1b7d7bbaf94b | -6.67242 | -44.41436 | 2025-08-24 04:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 298f227a-18b5-394e-abf8-567d0ac8c721 | -7.62575 | -46.28222 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30725005-cad2-33cd-8f98-b0b1374eac40 | -6.05951 | -53.88568 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da16719f-64f1-39c0-b355-8e0f32c7e1ae | -5.7492 | -57.58285 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 305fbfc7-016c-3c8d-b529-a98773062c9a | -6.10071 | -44.6919 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aba1bca-4ce8-3e67-a483-a6926a7d020a | -5.43004 | -60.15922 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4bccaf2-b0b8-3cf3-b8b7-fd5398936622 | -6.18846 | -45.42786 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f439d9aa-7158-3567-8afa-d8ebb76f6bb5 | -6.76926 | -44.31551 | 2025-08-24 04:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d62e8ae0-3e99-36a2-bfff-e14965222d69 | -6.47299 | -43.46356 | 2025-08-24 04:59:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2344b057-41a3-314a-816e-c5bd651665f4 | -5.66285 | -45.14577 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5870a47c-d59f-3472-9246-936803d39daa | -6.19685 | -42.98257 | 2025-08-24 04:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 846f36fd-6237-38b1-9d84-57cbe151a23e | -5.45732 | -60.18594 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea99601-e1ed-3554-b0ab-65e23f31678e | -6.59077 | -44.55629 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9e95c26-1e86-37d1-9921-62e1b38bfe94 | -6.47356 | -43.45939 | 2025-08-24 04:59:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 335938ac-5f83-364b-842e-62c8c9fa5b37 | -5.42932 | -60.16351 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| daa7ff1d-cd54-3a79-a343-faf2d8108bf1 | -5.87871 | -57.76042 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84b2ce92-9f48-3a77-a863-3f99c0308ae3 | -6.8891 | -45.68902 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3d8f9ef-e758-3a94-b520-5834d84d3bce | -4.95919 | -55.82359 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a80eb5e4-9af5-36dc-ab41-7c9bcf9a820e | -5.10127 | -56.97885 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bbf9566-87b2-342f-96f1-ebe741cb1deb | -7.62815 | -45.24049 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55ed4a49-2342-358e-910f-aab6781f85ed | -5.65731 | -45.14983 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0646e8d-a37e-3d02-a766-35b60d69800b | -7.60205 | -46.26617 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c6c653-4ff1-3a26-9c9e-661c9db35a6f | -6.23246 | -55.94193 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d2aec44-d496-3ee6-8955-e35727c8a538 | -5.64689 | -51.83553 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a2ad66e-2ed0-3c1e-b831-8ea0c0ac6284 | -5.66192 | -45.15206 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87a47082-8064-3ce2-9b82-d7d119fdf095 | -5.87789 | -57.76254 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 071e1aa4-99db-30fb-9615-989d39515fd2 | -6.43309 | -53.38153 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1308dc66-e90f-3293-bab2-67d4cb210af6 | -6.67193 | -44.41788 | 2025-08-24 04:59:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5d31821-a168-31df-a5c6-4a0df57caccd | -7.63106 | -46.2766 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 074db789-65d2-3e74-800d-ff005465113f | -6.5903 | -44.55976 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9503967-4ce7-32e3-b032-aa1b4f632160 | -4.70727 | -55.93293 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71184cd-ba5f-3d6f-8579-d3474f4bc75d | -5.42347 | -60.17136 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 893b59a0-31ee-36ba-af3a-7be0b1cecdba | -5.66209 | -45.15382 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be850ae6-58b6-3767-b16b-fc21125154a5 | -4.96264 | -55.82414 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2b89d962-b5eb-3aa3-b864-98f4c0eab8fc | -5.75148 | -57.5923 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 326a4b4e-3c53-309e-9eab-89fad6bd1a48 | -6.88643 | -45.67051 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a8fde7-f3d3-3c66-bbc2-faa054a1fd43 | -6.06229 | -53.88968 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35e2df1a-44b8-344f-80d6-9b4c3c156cd2 | -7.01671 | -44.63586 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd433d2d-142b-3cf4-b99b-c03e1d8c1894 | -5.66341 | -45.14435 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5852f776-d83d-35b3-80b0-cf77f42716aa | -6.91936 | -43.78123 | 2025-08-24 04:59:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3632e878-1c59-3b8c-b4a5-fff2d4401214 | -5.65034 | -51.83605 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfe0576c-347f-3505-8fee-e17d9f2478e3 | -6.8942 | -45.68996 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83d735ea-7876-3572-a8c2-a338203afdaa | -5.10195 | -56.97465 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59b1babe-4672-3171-a91c-e574f4df8b0a | -6.42641 | -53.38049 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7040a6b7-4d80-3fc4-83a6-b75c4ca5d679 | -6.42975 | -53.38101 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4540a6-f4c8-3b76-a411-51c81ad9af4a | -4.93906 | -55.81651 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0ed378-2ca4-3e21-b325-212762922f49 | -5.43301 | -60.16857 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 949ceb42-3e20-3864-9a0a-1c22b023b915 | -6.46091 | -53.40023 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1386990f-1551-354f-9e5b-a2e26c700a6b | -5.74703 | -57.59611 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2626e92-d36c-3430-8aa6-a9f2388a38bb | -7.01623 | -44.63939 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6758e19-755f-350c-b000-a302df4adff8 | -6.88951 | -45.68605 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e7bd8c89-ba87-3c5e-92d4-8014d391a7b8 | -7.59439 | -45.24835 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d1a90b-eff2-3753-8c4b-c8d1d598d410 | -5.65775 | -45.14666 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4f75934-abee-3f6f-96f3-51076f01847e | -6.4637 | -53.40425 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a34b446-a05e-3c27-b7f5-75d68ce5e8fd | -6.09433 | -44.69791 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbe7567a-c691-378c-af39-9e3ff8483327 | -7.02725 | -44.64108 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cc1a6ef-8e54-35ef-907c-5e6960c1a1e2 | -6.91879 | -43.78531 | 2025-08-24 04:59:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bacbde63-4db7-3e65-b198-51733fbaaf50 | -7.25962 | -43.67204 | 2025-08-24 04:59:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5533f19f-8a1d-3122-ada4-72ea236aaeec | -6.1932 | -45.43165 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10818ac3-0cff-3955-bb1f-aee0b50632ba | -5.45661 | -60.19024 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 202e69ab-7309-3c0b-8f55-24b792b03cb2 | -6.8887 | -45.69194 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 72899ed8-a9ea-3f24-9f43-5b8671db47fa | -5.67976 | -52.21328 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c1eb837-bc13-3140-9bf6-f7f536ad5917 | -4.70317 | -55.9362 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb20fca0-3a51-3e9a-bdcb-d764dcaef4b4 | -7.02774 | -44.63747 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 470f0340-2c25-3284-ab66-9f5cf0b65804 | -7.18022 | -44.66788 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a8ceefd-bd43-33e6-a97e-bbbbddff572b | -5.43229 | -60.17286 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 84450fd0-f198-3cdc-8b6d-4c79d518b48e | -5.66332 | -45.14262 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4024baf-f1a7-3b98-bd25-564e5c331f3f | -5.75364 | -57.57906 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 349ba089-d7e3-3a81-98e8-4962eace19ca | -4.95979 | -55.8198 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53576a6a-60f9-3117-88b0-49a94e9be306 | -7.62281 | -45.23969 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b036f4b-f3aa-340a-8fb5-99261ba80bd7 | -5.41906 | -60.17063 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README62.md)
