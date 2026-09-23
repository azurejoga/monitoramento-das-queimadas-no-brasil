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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1eede3c-2d70-3ea9-a6a7-302a50690771 | -6.6357 | -59.9342 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 376e8ce4-e8d2-3e77-b914-5030645a06b2 | -11.7161 | -50.769901 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb3ad0f0-a14c-35f0-a9d6-943689b49847 | -11.7195 | -50.784599 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11a488e3-cea1-3640-b241-4252851d1fad | -8.4634 | -51.478901 | 2026-09-23 00:58:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ff0885-cae0-377d-8551-25ece97562fa | -9.5627 | -47.941299 | 2026-09-23 00:58:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53da7983-64a5-3a4d-b1d2-572eec330cf0 | -6.6739 | -58.562401 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1246e1-096b-3bb7-8371-d3e22c644125 | -1.2962 | -55.8335 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70340b5c-ab15-307f-99db-001199d558c4 | -10.2672 | -49.968498 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86b99f11-9271-3a7d-a4ad-57cefbbbf2c9 | -5.2729 | -60.198399 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06fefa1a-90bc-36a5-aca5-aa6c7c646dd5 | -11.7292 | -50.782299 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae23727d-6498-3e46-a42a-13763a858e59 | -8.8374 | -50.475399 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195f566c-b7d2-3c84-8e2e-840fb68093c0 | -5.9813 | -55.362202 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0a8676-edcb-32b4-a7a5-2cd57fafeca0 | -6.69 | -59.949501 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1727dfb6-3ffc-35fc-8298-49d450c4cb23 | -11.7784 | -50.993599 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79b105f9-61fc-373b-adf6-a947d8eb2b85 | -3.5783 | -51.952 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dc82e96-e79c-3fad-acfa-675879214ab4 | -5.3969 | -49.0723 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35443553-75cb-3b42-9e23-fd742d943279 | -10.9138 | -53.945202 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18c02b5c-a888-3885-923e-80db5577ea3c | -7.8804 | -61.1786 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 041602e6-ef7f-3b14-8b3d-15e8cbd44316 | -7.2786 | -56.4669 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96f79435-ca29-3132-a4d8-ac4df740dd2a | -9.7033 | -58.138901 | 2026-09-23 00:58:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3de6b37-d7c7-30eb-ba42-825c887d6f4a | -9.173 | -51.467098 | 2026-09-23 00:58:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180a63de-40bc-37c6-8a46-ccca982b099b | -2.8833 | -54.076801 | 2026-09-23 00:58:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a2dd90-4769-342d-90ef-2f92c484c6c1 | -11.7212 | -50.791901 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abd56e27-b55e-3cf6-a4a5-220719d0b01b | -4.4407 | -55.0667 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bce7b9c-23ed-3000-9576-f79f44a97a5c | -2.239 | -48.741798 | 2026-09-23 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f166bc6f-7fa6-3674-9427-240b2dbe11b2 | -5.9968 | -45.229599 | 2026-09-23 00:58:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cf464a5-9a5d-3808-b72e-841af79f43ec | -6.7317 | -44.1432 | 2026-09-23 00:58:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b64027a4-8d20-3c42-a086-2121f25b20c6 | -3.4685 | -59.546299 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5a8644e-e104-33fb-90cc-395263e495a4 | -6.214 | -47.4981 | 2026-09-23 00:58:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4871646-74bf-3467-b269-bdde6d93cc07 | -10.615 | -53.9897 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bacbca38-00be-304b-bdeb-539f6925681f | -8.4536 | -48.692799 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8f667f47-b764-3034-9761-470db2d68281 | -5.9923 | -45.211601 | 2026-09-23 00:58:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bfa7986-e921-3552-854b-c0feb23604b6 | -10.7191 | -48.703098 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be1f8051-5285-38eb-a543-e18962d7fee1 | -8.4512 | -48.682999 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 38f16960-150a-3839-bd17-a33d51d6905c | -6.6694 | -58.5415 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d47d885-3a66-394d-9408-4bd61cb8931f | -9.0895 | -61.426498 | 2026-09-23 00:58:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6cac1e-8174-30f6-a5bf-7ffdaf565d48 | -8.3086 | -54.769199 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35b8c8de-fdd8-3940-bb43-0ea30a9d89de | -6.7273 | -44.1665 | 2026-09-23 00:58:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7da6c29-5eac-3a90-81c1-9a09012c5600 | -4.2689 | -55.443401 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00db650-7fb9-3ac1-a988-4354315bec8e | -5.8754 | -52.067699 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023d5349-c614-3839-9672-42df52978add | -8.315 | -54.8894 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb9a1c7-6a08-3244-a567-b65bfdef7b99 | -4.0455 | -58.916901 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f123d7c7-12a0-303f-9300-4342e3eee165 | -6.7879 | -48.678101 | 2026-09-23 00:58:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fc66de67-5678-3d23-a2b3-1a1ce646545d | -10.271 | -49.9846 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb4e9aae-be59-3139-a21f-2b97006c4db6 | -4.2865 | -48.608398 | 2026-09-23 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fad5956-5310-3ddd-8c45-1142ae1d7ef4 | -3.2118 | -50.911301 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520f5d29-be7c-3768-a48f-da355b079411 | -6.3 | -57.749901 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d61b29-8c09-3205-8fe3-99d07c21a542 | -11.6785 | -50.9636 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae25c5ee-941b-33bc-8d86-5c2f1398118c | -3.1057 | -61.078602 | 2026-09-23 00:58:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2da9f3d-a90d-3f16-96c2-1e1dcb17615f | -8.2498 | -54.782299 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f06083-bb2b-3f30-9ee9-b63541f70670 | -6.6398 | -59.906502 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34a9e980-ea07-331e-90fd-6229aca40761 | -8.2354 | -54.672298 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28da1018-c63d-3a84-b53e-59f7821eb009 | -4.1579 | -60.7519 | 2026-09-23 00:58:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 067e0366-3b98-39cd-ab2a-55c87f2b5fc5 | -6.3097 | -57.747799 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b356f35e-18cd-396d-ace4-668a4ada08d2 | -3.1393 | -57.678501 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6e9cf59-c62f-3955-ad99-5d9317b8ea5c | -8.7334 | -47.591202 | 2026-09-23 00:58:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 964ec5af-727b-3ac0-87c4-022b97baa573 | -2.8665 | -57.791401 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45cf0e99-1491-39cd-94a4-28c6ba6d7b84 | -8.2776 | -54.768501 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2617ce4f-4a75-3fde-8b29-71decb93b379 | -6.0973 | -57.669201 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca4edb92-374d-39b7-a712-028757587186 | -6.179 | -53.291199 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7751d8e3-8a47-32b8-8266-737f1db2653f | -6.1225 | -59.924 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9a22c63-4b9c-3687-b2ee-9adff307c52c | -11.6948 | -50.9445 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2167d8f-6e42-3cfa-9b85-fe671221f329 | -3.151 | -57.6847 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0de7b3-65de-3070-9ade-3abce99b25a8 | -8.1746 | -54.814098 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df0c9fdc-d5f2-345d-a61f-f82c238dabe3 | -4.3387 | -55.6591 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215adaad-4b92-33d9-8afa-4ea551413c7f | -10.326 | -50.5238 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b64c2290-b1ba-3dcd-ba64-22dfd101009c | -5.8662 | -51.9394 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb89dd4-5926-3b37-8c04-2de9586bcf68 | -7.5827 | -57.658501 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89f9b5ee-03f8-3917-9a96-6b9e1507ab6f | -10.2531 | -50.214802 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d89a8ee7-1feb-3a4c-9b61-4cf12eb22179 | -8.2027 | -54.709702 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8856e75-d57b-33e5-b535-5d73769189ed | -8.9406 | -50.914101 | 2026-09-23 00:58:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01da4c8-feef-3f7b-90f5-cd3efaf47459 | -5.9872 | -45.231998 | 2026-09-23 00:58:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee29acb7-1506-3b3b-9e57-071356f4b0dc | -9.9718 | -50.248501 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5414f430-ce5e-3b92-bbc4-2dc936f7cbf6 | -9.7019 | -51.967201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3c0dc64-bf3f-375e-b238-5e21b7a67efe | -5.4131 | -49.2701 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6c9ec9-8532-33c8-8bd1-839131712a66 | -6.211 | -47.4856 | 2026-09-23 00:58:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff7c6065-1ec5-3e12-8afe-c573c87165ba | -11.2998 | -51.333698 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea50bdf2-d9d3-38e2-988e-45e1cefb2923 | -5.2374 | -48.190498 | 2026-09-23 00:58:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc614cb-e18a-3cd4-a261-ebcb263fcff3 | -12.81 | -50.8559 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f066a5a-a4a6-3f58-a989-91245a7c4ab5 | -4.2701 | -56.2644 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c00c013c-37b1-3818-9d72-8c6f5fa96e56 | -11.3048 | -51.355099 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d301b772-a6e8-3266-bcde-6adf3ecf06f0 | -11.7796 | -50.0718 | 2026-09-23 00:58:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed1fb372-3a92-37f9-a5cc-e16540e66bb3 | -5.1218 | -48.784 | 2026-09-23 00:58:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93de5a25-08f5-3794-a148-b9802f2bcc14 | -3.7376 | -59.4198 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee92bfcf-0982-3e92-8218-2bf1afb0f63a | -10.3144 | -50.518501 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b67663f0-0065-3f3c-a1e7-7e99c56f72ec | -9.936 | -48.456699 | 2026-09-23 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad8dd48-bd43-34dd-9773-3e768a1141c3 | -4.0852 | -62.081699 | 2026-09-23 00:58:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e188fa9b-1bd5-3bf3-87cc-42996803403b | -3.4611 | -59.5592 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eedd2483-4be3-37b3-ba02-c04afe44cdfe | -6.6226 | -43.712101 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b5adc84-d1ae-3506-851a-631d5164457d | -12.4121 | -46.9557 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0520301-fdef-3a38-aff1-e0a03726d95e | -8.9504 | -50.9118 | 2026-09-23 00:58:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ded6a1-41ed-3a18-9b70-73ba55d164aa | 2.7275 | -60.673 | 2026-09-23 00:58:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d589b4e0-0365-3d5a-ba8c-3d453ea7f156 | -6.4599 | -59.9716 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42291067-ea69-307e-991f-0a82fd33a891 | -3.7595 | -59.4715 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d89b435e-8f46-30cd-a36f-d8a0436489db | -11.6897 | -50.922699 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea1b9cae-2a69-3c2c-a605-c80337383eed | -4.5542 | -54.931999 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e576ab-7638-39ac-9132-c6c88517a571 | -3.0207 | -57.9268 | 2026-09-23 00:58:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fcb43c3-b9d4-35f4-a989-363f46e1bfd0 | -11.8836 | -45.755001 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5261563e-fba8-338e-9ea6-da9f50cb20ed | -3.8576 | -58.8116 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aeb3875a-4c81-3021-b63f-520c0266e7a8 | -6.1116 | -59.874001 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README29.md)
