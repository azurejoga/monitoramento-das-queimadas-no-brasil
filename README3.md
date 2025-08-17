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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9de361f-d1ea-3de7-9bbf-00924c1c4f52 | -7.1362 | -44.631401 | 2025-08-17 00:26:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4849190c-d345-37ae-8541-b86790b5337a | -10.118 | -57.756001 | 2025-08-17 00:26:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8603698e-1f02-34c5-9be4-d0d2d3d44d86 | -14.6321 | -54.888599 | 2025-08-17 00:26:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2ea007-e2c4-35d5-bd5f-bc52dd007bb6 | -10.8372 | -45.3158 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c74e6d88-0808-3373-b544-1222724a31d1 | -14.9595 | -54.741299 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea29440-38f2-3abe-8abf-d02385ae0305 | -9.1949 | -59.606899 | 2025-08-17 00:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18c56c20-b0c9-3b94-a2a6-ddf4acfd5f39 | -20.821501 | -44.503899 | 2025-08-17 00:26:00 | METOP-B | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f66ea751-8ef2-30a1-838f-c88c732c7f88 | -11.8681 | -48.193001 | 2025-08-17 00:26:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3fcaadc-36d2-3619-85d9-45d5417bf8d6 | -3.822 | -47.726898 | 2025-08-17 00:26:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4678b1ca-a7c9-33d0-83a8-aef2ef4c4f29 | -15.1832 | -48.7784 | 2025-08-17 00:26:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7a6388-13ee-332a-874e-2a0e3cd10ac9 | -4.9086 | -43.2332 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c92fba8e-8a82-3e0d-be0d-be25273e40e8 | -6.1771 | -45.424999 | 2025-08-17 00:26:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08a16be3-b3ad-33ae-bafd-158b169b4e4f | -14.1864 | -45.322399 | 2025-08-17 00:26:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 109462d5-3580-313f-878d-594f6f64cf8b | -9.1883 | -59.6245 | 2025-08-17 00:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a490053-15db-32f3-8272-b43fd0134524 | -13.5873 | -47.7747 | 2025-08-17 00:26:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84068497-27b0-3876-9f84-0403f01a5b48 | -4.929 | -43.274899 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70196ca8-258f-3cd0-8760-e222328cf5c6 | -11.3612 | -55.380699 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25fc461a-c6b4-3d77-9c8d-42fe5b080ba4 | -3.4521 | -48.9734 | 2025-08-17 00:26:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c31f27fc-8b8d-37cb-83d7-617062415ff1 | -12.5523 | -46.938599 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1e83ddc-3901-3170-97ee-7cb0a2a382e9 | -12.452 | -46.994099 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e20e222-c8ad-3b12-9189-ca1a72ac2773 | -6.5443 | -43.015701 | 2025-08-17 00:26:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 951a520f-1295-394e-b2e5-84daed987d3b | -12.5621 | -46.936199 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cf45764-eef0-3348-9fed-991e2649d8fb | -3.8273 | -47.7495 | 2025-08-17 00:26:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d80c4bf-7cd6-3302-9fda-e832b62c2114 | -21.068399 | -50.3022 | 2025-08-17 00:26:00 | METOP-B | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| affc8397-0dc3-31c5-a043-4c812d85e555 | -8.9788 | -60.4964 | 2025-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9975b8cc-db6a-3b78-97e0-d5b8f5cb833d | -6.5453 | -43.0138 | 2025-08-17 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5526d326-2cd4-332c-a910-add88233f8d8 | -9.518 | -60.5268 | 2025-08-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 73213e42-b55d-3345-962d-855b84746a68 | -4.9118 | -43.257 | 2025-08-17 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 3f62d20c-8977-3f6e-b1b8-d8b696b624de | -4.9305 | -43.2558 | 2025-08-17 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1c5e853f-c10a-38ff-ac99-b933a5702e72 | -6.1838 | -45.4371 | 2025-08-17 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 96a3e954-cb3a-336f-833f-aafce316f94b | -14.9625 | -54.7559 | 2025-08-17 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b9c3de99-a532-32d6-8f83-1f9551bd3ff7 | -9.5179 | -60.5461 | 2025-08-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fbfc3340-7fa7-3100-b811-8ee50a0894f3 | -6.545 | -43.0373 | 2025-08-17 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 61145dc5-39e7-3359-84bb-1c1fd7771bff | -9.1894 | -59.6558 | 2025-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 29c58b98-fe15-37b8-af11-882ea4773744 | -9.4994 | -60.5278 | 2025-08-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e37b85a6-05bf-3c10-b436-bbac6c1e8b19 | -9.4991 | -60.5663 | 2025-08-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9a29e7a6-6b7a-3d44-bc0e-5769b2e76de7 | -9.4992 | -60.547 | 2025-08-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3b7063cb-4ef0-3721-8ca6-b758533fa542 | -9.1895 | -59.6364 | 2025-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 96b3677e-11c4-398e-97f4-33e4c0e9bed0 | -8.9787 | -60.5156 | 2025-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 259c2a5f-d2f4-37c7-a0bc-23426364d4a3 | -9.2082 | -59.6354 | 2025-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| de3108e0-617f-3286-b994-517abaaab6af | -9.8863 | -67.7758 | 2025-08-17 00:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 66cc24bf-1f88-37e2-9487-d83a659fd3b3 | -8.034 | -47.6639 | 2025-08-17 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d7fdb7ae-a297-384c-bba2-79f966a5db84 | -15.1873 | -48.7671 | 2025-08-17 00:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9187c8a3-7b1d-3af2-8251-f792f67372aa | -14.9251 | -54.6774 | 2025-08-17 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cdab1523-a63c-396d-8b39-fd639fe430d9 | -14.9819 | -54.7536 | 2025-08-17 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b7e3abb2-1bda-3673-bc34-a9ada1d82067 | -4.9118 | -43.257 | 2025-08-17 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 3905b1a8-7ae6-35da-af4d-b271748b55a0 | -9.5179 | -60.5461 | 2025-08-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| de0d3b1f-a5a7-341e-9fa7-4817841c5302 | -9.4992 | -60.547 | 2025-08-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1a9e9707-50c3-3fb0-aadb-005733bac9f3 | -9.2082 | -59.6354 | 2025-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d54f7a20-c6f4-372c-94b1-2ffa0a146e66 | -9.1895 | -59.6364 | 2025-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| dd97c58a-f011-3fff-92f9-c3b96d0ebdb5 | -9.1894 | -59.6558 | 2025-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ff9b4a06-8e9b-3b56-80de-52375a1fa40e | -8.034 | -47.6639 | 2025-08-17 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 38ec6f9d-ed83-3239-a387-46d253c2a8ae | -14.9251 | -54.6774 | 2025-08-17 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 2126648a-ffbc-3e0d-abff-c71a2d955ba3 | -6.545 | -43.0373 | 2025-08-17 00:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 34541ec1-4980-3231-8d97-b3f18af40ad1 | -9.4994 | -60.5278 | 2025-08-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| be08fa08-8db9-397e-8896-c2f8173b8e0f | -6.5453 | -43.0138 | 2025-08-17 00:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 633f663b-1eb5-39d4-8845-0887f7919856 | -9.4991 | -60.5663 | 2025-08-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b58a0fb3-9276-3e42-999d-125b7a002c7c | -9.518 | -60.5268 | 2025-08-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| dc6850fc-4928-3050-80d0-4ab93ed64409 | -8.9788 | -60.4964 | 2025-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ef5c2296-aba3-3486-8b6e-849021c60d1f | -4.9305 | -43.2558 | 2025-08-17 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e285176e-2cb9-3ae5-b8eb-39088bfbd4e7 | -14.9445 | -54.6751 | 2025-08-17 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 815f49f5-4d63-31f8-b1b0-ca03a5148974 | -6.545 | -43.0373 | 2025-08-17 00:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 87da48f8-ba9f-3da1-84e1-f97374bd0343 | -4.9118 | -43.257 | 2025-08-17 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| e26e5ab7-6465-3f67-86fc-496257658f95 | -9.1895 | -59.6364 | 2025-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 91763dc9-5784-357d-aebf-2e744d2517c7 | -13.0122 | -42.3321 | 2025-08-17 00:50:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| b08d3f94-c4f8-3cc6-a3b8-98a5c9f31f06 | -6.5453 | -43.0138 | 2025-08-17 00:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5465b83b-3fcf-3a30-a005-2bb82b0f2f0a | -9.4992 | -60.547 | 2025-08-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5e5eedb2-b593-37ea-a1a7-a3059ba1bf22 | -9.1894 | -59.6558 | 2025-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 142f8e26-62fe-3a98-a413-2a5c81835f78 | -9.518 | -60.5268 | 2025-08-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e8a8cf1b-d96b-35ab-98a0-34e2b83accbe | -9.5179 | -60.5461 | 2025-08-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6e87851f-b330-3511-bc5e-c78c1723a2a1 | -9.8863 | -67.7758 | 2025-08-17 00:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1de69d7f-8c08-3572-a95e-c30dee7956d7 | -9.4991 | -60.5663 | 2025-08-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9d61c440-ac10-35e4-8c82-6375da9edccb | -8.9788 | -60.4964 | 2025-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 32688a7e-b29d-3675-b597-02e969be1b25 | -13.4421 | -45.8898 | 2025-08-17 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 23777236-e6c6-3609-a2b7-bb0fae568204 | -4.9305 | -43.2558 | 2025-08-17 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b8598e44-6690-3b14-b234-0312e36a684d | -8.034 | -47.6639 | 2025-08-17 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6efa1d98-3a8b-34af-adee-e1e7d4ae49f0 | -9.4994 | -60.5278 | 2025-08-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d0efa633-7433-376a-961e-c057afa799f7 | -8.9788 | -60.4964 | 2025-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| de790b55-f50e-3242-9cc8-8cf7d24fc62c | -19.329 | -49.2864 | 2025-08-17 01:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e6af3b08-c2bb-3a7e-ad27-efd748060b43 | -4.9305 | -43.2558 | 2025-08-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fb13e192-e288-3966-8839-c40c81df8a94 | -9.1895 | -59.6364 | 2025-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7af13b24-0040-32f9-8687-a699a143e2e3 | -9.5177 | -60.5653 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| da609bd1-91ce-3f2d-83ec-8e87107b9944 | -9.4992 | -60.547 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9b83ba0f-5cb3-32dc-8d17-d13db7ffd45e | -18.7575 | -45.0866 | 2025-08-17 01:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| fdabc856-1c7f-3599-89cc-7af5ce2a40bf | -10.8444 | -45.3126 | 2025-08-17 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6d50abb5-a04f-3955-85cf-cd2916848a45 | -13.4421 | -45.8898 | 2025-08-17 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 54596c12-a0f5-3be9-8817-cfca67f295ef | -9.1891 | -59.6945 | 2025-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| dab22693-ea69-3507-9cd8-9a1b02ce15f6 | -9.4991 | -60.5663 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 50a5c3a1-b2ba-3242-97f0-80dc1c16622d | -9.2082 | -59.6354 | 2025-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1b1c7d1a-dd26-386d-8131-2841f7f59185 | -9.4994 | -60.5278 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 916b2b75-ff32-3ef8-849b-a028817b0d85 | -9.5179 | -60.5461 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6a9c85d3-4b1f-32d8-b27b-86e8bf56a9af | -6.5453 | -43.0138 | 2025-08-17 01:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9d154bfa-87dd-3562-b8bd-4ba20aded0a5 | -9.1894 | -59.6558 | 2025-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a4991733-4186-32a6-ba5d-a24102f304b3 | -9.518 | -60.5268 | 2025-08-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e41c2e94-692e-38dd-b61e-9da8ce32f61a | -6.545 | -43.0373 | 2025-08-17 01:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3207e175-3d40-3d3b-b298-9c950e3df71f | -4.9118 | -43.257 | 2025-08-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| fc6bfb8c-c47c-32b4-aac1-6868af81f168 | -9.5351 | -63.5771 | 2025-08-17 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fe889b98-38fd-39df-aaa2-9d5a570e833e | -20.47813 | -49.35945 | 2025-08-17 01:05:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| fe9ae89a-4eac-340c-9e11-6d820e727e5b | -18.76169 | -45.11475 | 2025-08-17 01:05:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 40.7 |
| b6e7a740-9823-3849-b6d1-f5b595c7083c | -20.47563 | -49.34444 | 2025-08-17 01:05:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |


[Clique aqui para ver as próximas entradas](README4.md)
