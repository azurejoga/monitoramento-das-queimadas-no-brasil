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
| b785e1ba-2f63-3ee7-b33b-3749bb3dee90 | -7.22922 | -42.74932 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a676eb44-dff2-3703-b249-fecae65779ff | -3.85177 | -52.04043 | 2026-09-02 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aa0e544-4ce4-3562-96d4-e59e7b7ca142 | -2.8305 | -48.65599 | 2026-09-02 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f12bf735-3366-3e74-98c1-9aeb47132ad2 | -3.37769 | -52.79471 | 2026-09-02 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3efcd8c6-4d6e-3beb-b8a1-5ec68acaf77a | -3.12692 | -61.23186 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a655346-51e2-3385-9108-4800553facd6 | -3.65423 | -58.91365 | 2026-09-02 04:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71a1985b-eb44-3107-855f-0e350421a3fc | -1.35473 | -55.38737 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac834482-5afe-3d45-9e49-679014695ed4 | -1.50596 | -54.95934 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d03e8204-6525-360b-be25-1f799c150fc5 | -4.49382 | -45.90755 | 2026-09-02 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 011e21d5-3b5b-328d-9c21-42cd1359169d | -2.30701 | -48.63168 | 2026-09-02 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae34eba2-9027-360f-8e61-87d50aa217f3 | -4.0946 | -50.42819 | 2026-09-02 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab63384-1a2f-3d7f-acdd-bca7c92f35e8 | -4.96726 | -55.84814 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c218b53d-472f-3856-a785-b02a612adae4 | -1.0217 | -53.72459 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4078f56f-9875-3a3d-955c-784be3846bd8 | -5.2479 | -55.90948 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf27f8b-5876-3ed0-93a2-1575237a7ce6 | -6.85219 | -41.65404 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 35f2d94e-16b0-3d1f-8c53-ce585378066c | -1.5054 | -54.96284 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63382136-8703-3cb6-b075-cc9993a33405 | -1.25484 | -55.73891 | 2026-09-02 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8fce6a4-2746-3b78-8384-7ef8f2866f01 | -3.3498 | -51.11208 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93654ca-443d-3a3c-b320-9b55f1b816a7 | -3.62319 | -60.55691 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d44764-63ce-368c-a260-7c9ad39e97a0 | -6.83675 | -41.68451 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 495eea04-c754-3d70-b0bb-cf52ff82ccc9 | -2.12247 | -56.8171 | 2026-09-02 04:55:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dd5bbe9-2598-33a2-b8b1-37c3cd8378c4 | -3.44422 | -47.26981 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11290819-49d5-32a5-8cc0-da37f213dbc2 | -5.24849 | -55.90597 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1d37e83-2b14-3925-bd78-1dbfc7da3a38 | -4.97189 | -55.8453 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ca5b01-07ee-301d-a46d-f88730d674bb | -4.12388 | -51.03169 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa1524d-fb0a-3ccf-bd27-511a7db4bb8a | -1.0176 | -53.72605 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d617af8-6163-324f-a487-5e35e2153508 | -3.11844 | -61.23252 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb605c7b-b541-3d02-8d2b-e9af29ab9881 | -4.96843 | -55.84103 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01e860fd-5fd6-36e9-b52f-f27a9ff2a79a | -6.85201 | -41.65466 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a11ab9d-caaf-3e8d-9079-9c9b5880231b | -6.8079 | -46.20042 | 2026-09-02 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26d339c1-bf83-3828-b9ce-774b0eda1727 | -5.86415 | -51.71088 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9792f49-c824-3dab-92a4-a6289425025e | -1.51001 | -54.95989 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf728c7f-21a9-3eb4-822f-c0dcbbe63700 | -7.22523 | -42.75024 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6105428a-34e4-3547-96de-a43b75d2e255 | -4.97131 | -55.84885 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16341ca3-107b-338d-bb1d-970425a97d3f | -3.12095 | -61.23076 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 276e816a-6d25-3d2f-9907-5fd54ed22bc5 | -6.42945 | -46.27015 | 2026-09-02 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3487066c-add5-3964-83f8-dac8e8009825 | -1.96284 | -48.3782 | 2026-09-02 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b85977-6a40-3596-8103-16fb62f53b62 | -4.16223 | -47.83453 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cda5904d-7dd0-3c9a-9f49-4440017160d5 | -4.51874 | -48.74957 | 2026-09-02 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a865b06a-2aaa-3588-99d4-9af3a44e923f | -6.29724 | -47.46712 | 2026-09-02 04:55:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa9fc166-dd13-3804-987f-23898556e0b7 | -3.57559 | -58.7448 | 2026-09-02 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7367e3f-b3b9-3fe7-a300-4c897ec70a3b | 0.97586 | -59.38313 | 2026-09-02 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6af1fa5-e4ac-35d7-a0c8-9dbfc822674a | -5.24502 | -55.90177 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6413026-5e57-3871-9e15-c41df130b2c5 | -3.55745 | -59.0397 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f8e79e-749a-3515-a1f2-65d8832abf3b | -6.58214 | -44.78835 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6292aa1-43ea-3187-9c00-f9754cfcf208 | -4.96146 | -55.85809 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26790146-9518-382e-90ab-70287af80c4a | -5.7996 | -52.05066 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 363a68f6-2eee-344e-9230-615751860f2b | -4.26689 | -55.15963 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 687215e2-e4d2-3067-be33-ca50b7890d53 | -3.84837 | -52.0399 | 2026-09-02 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1816ab15-4291-3c10-833a-727361bafe65 | -1.01489 | -53.71889 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82a65fe9-ab9e-3d2d-a0ad-279361231177 | -2.83815 | -49.51305 | 2026-09-02 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dd88385-7b6b-3097-83fe-577dc45d117d | -4.70035 | -56.05445 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da82c54e-7a1c-3f3d-9fe8-b87fdbf5ff25 | -5.25201 | -55.88484 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17eba56f-a0b8-3d0a-b658-27f803e0baf4 | -3.61816 | -60.55204 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58d5954-11d7-3d5a-bb97-24ffb18f8871 | -5.93181 | -50.21078 | 2026-09-02 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73762bc5-1b01-331c-bfb7-a9673cf2320e | -1.50945 | -54.96335 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 12ef2664-8be7-358c-947c-1fea0bbe48f6 | -6.34753 | -44.09772 | 2026-09-02 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8c845df-a703-37ae-9e87-6a968abf2d4d | -6.68027 | -46.16947 | 2026-09-02 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d3f3463-47ef-3f9b-9572-1498901312f7 | -2.31041 | -48.6322 | 2026-09-02 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cadfd8d7-a142-3a15-9a0a-28f1b4cc403d | -6.09806 | -47.38228 | 2026-09-02 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ad2f78-4c47-3bfa-a241-1886c65352eb | -6.67532 | -43.41227 | 2026-09-02 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 03f0ee90-fc6c-3bd4-a72c-2d42cd49e6b3 | -3.23941 | -47.24911 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 38d8eb82-57e6-3b97-bc67-0a4d0abef28c | -1.59183 | -50.43652 | 2026-09-02 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54d5949f-2576-32aa-ba53-9873170aec03 | -6.85248 | -41.65116 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a8097d66-3185-362a-ac23-495d9cb9f826 | -3.62122 | -60.56858 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6bea905-274b-3891-b153-a7871a058701 | -4.95917 | -55.84668 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6135dc89-8717-3a2d-8fbc-3f9a450df456 | -6.58657 | -44.78897 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e4fb2b-d1d9-316c-9dbb-ea89d037343e | -3.44445 | -47.27258 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93116a51-7854-3c2f-9973-66b7e13aef5a | -5.63684 | -43.55508 | 2026-09-02 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8976b7a3-4081-3c9c-905a-60a9edbd46f1 | -3.75162 | -59.32235 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4b0f933-dcb2-3cfe-9ef0-327818aa2bf5 | -3.11171 | -61.23588 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef6899ce-ee26-364d-b301-880b2b4edfe7 | -7.22996 | -42.75409 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffb7b36c-9f80-32dc-bb1b-7de38b5cca3f | -1.59238 | -50.43306 | 2026-09-02 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e597fd00-5e3c-3121-987b-4b65b44ff69c | -3.9745 | -55.6418 | 2026-09-02 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b231758-348f-389f-bc2b-ade4941eb2f1 | -5.87491 | -43.52595 | 2026-09-02 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bd96050-80d8-394a-b59e-c73740108dc6 | -4.97073 | -55.85239 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d682efe5-1986-3340-94a8-648a9199f66a | -4.97247 | -55.84176 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f3cc516-2239-3c5c-b98b-9a17743b3fd4 | -5.89932 | -52.10322 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429955b0-7a4e-386b-a886-7fda3d1138b1 | -4.18223 | -49.40435 | 2026-09-02 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81a3336b-0585-3289-9e5c-8c069162b090 | -4.36944 | -47.77359 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 82929087-d0e4-3f91-b1bd-93939834f61e | -4.12443 | -51.02822 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46505d9c-4f95-3a0c-92f3-9b99747d1f07 | -4.95859 | -55.85023 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc5d3282-e1ce-3e4c-8de3-5182b290a47d | -4.96901 | -55.83749 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b3612f4-6ffb-3ddb-aa5d-e44cef0ebf70 | -6.84272 | -41.681 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c98b698-b3e2-3a29-9c1b-f6dded6150b3 | -7.23171 | -42.76857 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f538ee5-b30f-3e70-985e-2ce6a22ff2f1 | -5.86082 | -51.71035 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44308d22-b8de-3ea2-adf7-e1d590641fe5 | -5.73977 | -52.18719 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e40c0e6-f257-3781-a850-efd8a9378d3a | -1.62232 | -55.16745 | 2026-09-02 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c78e0521-10ef-390b-abf2-7411e2b8201d | -6.76856 | -41.17144 | 2026-09-02 04:55:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0d56fa8f-b8e3-33a7-9ed8-591f44861387 | -7.22877 | -42.75246 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 04685fc9-9ef4-356a-a63f-d37277732ca2 | -6.91558 | -45.71299 | 2026-09-02 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba3c518e-e459-3511-abbd-7c7ffb990ccb | -6.67612 | -43.40673 | 2026-09-02 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 74987d3e-7479-3c37-98b0-f8683f52f153 | -3.84839 | -44.05136 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06e36c3d-78b0-3eab-b00f-d1068e155d7b | -3.61882 | -60.54817 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9281b7ac-868b-36a8-8457-aaaa4748585b | -4.97536 | -55.84956 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6bc6f93a-9be1-36ba-998c-018010b06292 | -3.6175 | -60.55593 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 851dd970-5f59-3644-a010-1c9c698bf5f4 | -6.83621 | -41.68735 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a6092078-9a49-3be3-b4e3-47caebc3690b | -6.14076 | -44.45446 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff9b3e79-4ce4-36ae-967d-be4f05209eeb | -3.85285 | -44.05216 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e73af48-8b30-3c0f-97ca-09fe6e93baa6 | -3.24239 | -47.25382 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |


[Clique aqui para ver as próximas entradas](README31.md)
