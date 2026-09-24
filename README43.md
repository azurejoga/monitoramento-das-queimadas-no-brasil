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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dd02896-4bc7-35d8-a17e-cae43e77f5d1 | -5.19874 | -44.6912 | 2026-09-24 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7c58564d-0279-322a-bae4-73b4a24d8e69 | -1.62482 | -54.918 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13d77548-4b6a-3b6d-b31b-51895e5c2f59 | -5.77494 | -56.5247 | 2026-09-24 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa24104-67f7-32a4-85a8-e53854063a9e | -6.33085 | -49.86453 | 2026-09-24 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 310b4e29-c544-3274-8d33-cbe32b1f64c6 | -5.25261 | -49.22747 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ee80cf2-78e0-30c0-8f31-916da7053df3 | -3.68113 | -60.56466 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08b6101d-9313-344b-861f-afc5d9b78a4a | -4.95524 | -45.14527 | 2026-09-24 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca54d01b-cc20-3eed-b1e3-a7cc0ac9ee7a | -7.41752 | -42.63608 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95b54998-e327-3151-9d39-e0d8323ae30e | -5.79151 | -49.9712 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50e7bd2c-8473-3cc3-8407-adbf644aa241 | -5.82669 | -52.02263 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c30988b-f61b-3b3a-ab79-2b779a3ad1fa | -5.949 | -51.79372 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3fd9932-6ba0-391c-8bea-c60719453e9f | -6.57651 | -44.14612 | 2026-09-24 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 390146d1-0d02-3df1-88ac-5cff04706c86 | -3.70527 | -54.20278 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e03d3518-a3be-3889-bb9f-64d0eecb205b | -3.72638 | -49.05593 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dcbe46f-4785-3766-a31a-d5f2a09dc791 | -6.66021 | -50.94936 | 2026-09-24 04:44:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009da6a6-0c86-38f6-a888-a26106eb8c1a | -2.39114 | -48.51846 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a5384d8-18d0-3fb4-82fa-a05573850ad2 | -1.27146 | -57.0379 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e7c9160-b602-3a70-8cd6-3eb115a42b3c | -6.7257 | -43.94155 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2148f312-8efd-34e1-8b6f-0a1e2e495042 | -7.20164 | -47.45459 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1c8c141-6367-3ed0-ad83-613fc77f1f73 | -1.72075 | -49.98299 | 2026-09-24 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2864590f-8be3-3f7e-bc13-ea4d3710e8e6 | -5.72401 | -49.83204 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4432651f-fbd5-3dfc-af96-503308907377 | -1.62385 | -54.92378 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a27d614-dfc9-3f8d-92f9-aa7a2a644622 | -7.32319 | -46.74406 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67326f96-978d-360b-81b9-c2f73b6df753 | -3.35798 | -43.24383 | 2026-09-24 04:44:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eea3e84-b7d6-3fd4-9939-59ec286f8163 | -5.45637 | -47.9057 | 2026-09-24 04:44:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbe37095-3dce-3008-8a16-a76383b9bd82 | -5.57431 | -42.30753 | 2026-09-24 04:44:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0c44bbc4-a434-3374-86f3-7e9de8301ec1 | -3.44157 | -50.08879 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a0c915-dfc9-3bdd-9e9b-01d673f067f6 | -6.72333 | -43.9391 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc07c4b4-35d9-318a-99c9-898e714a110e | -6.72641 | -43.94431 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ce15b32-c795-3fdf-b198-43d7aa8b8655 | -6.72374 | -50.94995 | 2026-09-24 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f63e086c-abb9-3cbf-b215-017bc1ad90b1 | -2.5737 | -54.74301 | 2026-09-24 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fb6a6f0-5ae8-373f-8304-65847e21f8f4 | -6.21687 | -45.30193 | 2026-09-24 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 156444d0-5e71-3b86-aaed-389b1a6655d3 | -5.38613 | -46.56945 | 2026-09-24 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc08b74-0175-3880-8493-c7d5fb12f824 | -6.27463 | -43.26929 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a052eae-9065-362a-a692-76a0ed541e66 | -7.2718 | -45.53801 | 2026-09-24 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 002c660a-cf78-36b3-af31-816b6cc99d4a | -4.02062 | -52.06755 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6a3d946-5328-3a8e-9f74-02ee4c9ca01d | -5.0075 | -44.63836 | 2026-09-24 04:44:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab5abe4f-1c31-3f1a-825f-53dc8c4957ca | -5.61966 | -51.63679 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b215e4d-656f-3eb5-8a9f-f429d25bf8a9 | -6.78333 | -48.68244 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 366724d3-eef6-358d-96c5-ea0995beda7a | -3.44491 | -60.5802 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e629758-580d-330f-8991-9b431b4642c2 | -2.31227 | -48.57691 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 951fe4d9-6221-3d31-978a-a13fe4e17f81 | -7.19442 | -47.45705 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 828f5c1f-250a-3648-998c-ddc14c071a91 | -2.88128 | -40.02481 | 2026-09-24 04:44:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42dd36d0-0c06-3764-ae89-3f36576a2eaf | -6.91193 | -47.42725 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6da791c-a65b-3831-8933-08c9d7947f27 | -7.67868 | -45.48777 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0b70634-ab89-33cf-8aaa-95e9cd16e6ce | -6.00937 | -42.72789 | 2026-09-24 04:44:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 943bb826-1f06-3e22-b023-507fe3b737f2 | -6.17708 | -53.28946 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca5ace63-0252-3d2e-ac5a-f5a3e1c7507a | -6.51668 | -52.82417 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4476921-68cd-31d9-adb2-a87cc2716d97 | -3.68345 | -60.59199 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c2aee96-a965-3c72-b632-475271c0bad9 | -7.50476 | -39.27651 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b4723dab-8c7e-3724-a9b8-5da3bf970ab4 | -7.46307 | -44.57122 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 349155ca-4075-3589-b75c-3d4d50e960c1 | -6.43633 | -48.44362 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f3c124-9fb9-32ac-80f1-054980a23c13 | -3.18438 | -48.0174 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 217b9c2c-87f0-37c7-b0da-d5e06452cf05 | -3.44672 | -60.58046 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af91bbfb-bf00-3e83-833d-2126d283eca0 | -3.91908 | -59.66833 | 2026-09-24 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5791bb8-d5b1-34de-9d03-e6e71bb275ca | -3.67753 | -60.59403 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b02dde4-0bb9-31e8-904a-481fe38f6abe | -4.99272 | -45.55458 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6b1b0f58-95f2-3134-be1c-0aa77186fabd | -5.98867 | -44.4289 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4e53212-8734-3071-bde2-2af002c982f0 | -4.9864 | -45.54975 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3dfdc69b-ea83-3bbd-88b5-7b5fe344d948 | -3.45363 | -50.08241 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c65d055-cef4-3e75-bd2a-3b3f18ffc26c | -4.28719 | -48.60865 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb6a60f-1ff3-39bf-ac73-b7c89bce9e53 | -1.62473 | -54.92278 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 41265037-a04e-3eaa-999b-e812fe353082 | -5.22502 | -49.22733 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ae33a44-6004-3823-b1f9-1f5091796b44 | -7.47417 | -44.57287 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2af099b5-be56-3123-b1f0-b629c86017c2 | -5.49763 | -49.03135 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e841139-e069-30a3-b606-ea8a5d784cc5 | -6.39394 | -43.74598 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74fd69b-ccf3-3055-be39-76d9b12fc9dd | -5.84111 | -53.8486 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa2532e5-c42a-3711-a525-3ad3480bf5cf | -4.02459 | -52.06828 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e06d9da3-59af-3ce9-a86e-dd9f2775a0ef | -6.57486 | -51.49215 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63effa14-344a-3170-9824-5889b0542cd7 | -5.75179 | -44.63842 | 2026-09-24 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 516697bb-8e21-304b-9aee-db740246ce8f | -6.60786 | -43.83448 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0af2a0a4-6a31-3357-837c-0371e0356b0b | -6.72165 | -44.15089 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5561eafd-bee7-3315-9a67-7d2b7b0ba8f0 | -4.99616 | -45.5551 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b6818edf-8c39-36be-a328-890f38141630 | -6.20722 | -53.57364 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a60104-c778-3986-8a46-6e3b7b3133b8 | -3.76429 | -47.5024 | 2026-09-24 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70cabc82-e5b4-3cd8-bb66-c8740efae226 | -6.40601 | -46.20277 | 2026-09-24 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beba476f-d0e8-3c4e-9f01-9c3d9c572cda | -6.00027 | -44.10717 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1eef2ae4-acb3-3fb4-a72f-2464263b77ca | -3.58477 | -50.03171 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c9dd2f-2398-3b27-8103-f719039be6e9 | -5.29208 | -49.28639 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 871076e7-1adb-311f-b12e-e086dca1ff59 | -6.26602 | -43.27307 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b4df2e5-1953-3e35-baff-40b9ddd03301 | -6.12276 | -44.59739 | 2026-09-24 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7bfbcc65-5101-371a-90c1-b57c291c6038 | -3.81624 | -58.88923 | 2026-09-24 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f91bc4-aefa-3851-9c4e-dfd597830618 | -3.16377 | -54.60068 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9eeff23-eee7-3a7e-a581-3b47e9c9e2cc | -3.01212 | -51.53692 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81248de1-93f7-325f-8f7c-45324aa71c9e | -3.71375 | -54.20885 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea5e5b83-82fb-3932-a8c4-26e9628c8aa7 | -3.73501 | -51.28302 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b87d8a7-defc-304e-819d-c36446ea66fe | -7.67342 | -45.47444 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99988557-ff8d-3e78-af5e-1c3b48052074 | -5.38557 | -46.57297 | 2026-09-24 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62597f04-55d7-3d7e-9f11-719f7a38ff37 | -3.67879 | -60.57778 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afaee28c-24c9-3d99-825e-a892932ba739 | -6.18275 | -52.80581 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e44f55-99bd-3665-ad4f-1d55a7afcf2c | -2.96704 | -52.15269 | 2026-09-24 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d19634-21c4-323a-ae8f-6bf36ce30e1d | -4.36646 | -46.17161 | 2026-09-24 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d98f05a-24e4-3d4c-9980-49d2847ad96b | 0.60777 | -51.57038 | 2026-09-24 04:44:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1651ef18-861c-3319-92fd-9fcc02d6d5f3 | -3.45135 | -50.07375 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c4f32508-8bf6-36f0-a602-43e7c1600cc8 | -5.81754 | -47.75693 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36e2867e-49a6-35ec-996b-370f951cb9a4 | -3.17768 | -48.01634 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6553faa6-0f8e-3c2e-b794-b330f46a5c82 | -4.11585 | -51.08096 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 282b6699-af28-3a07-9f6f-6c60c69895f7 | -1.63676 | -54.90813 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31cef345-f38e-3c79-b2dd-d89a09b8f50c | -7.03362 | -44.65475 | 2026-09-24 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| daf7d004-9822-3b74-aa32-8b3d99afb103 | -3.70608 | -54.19798 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README44.md)
