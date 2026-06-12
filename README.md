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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e075c7d9-814f-3268-97bc-6100046212fc | -12.8548 | -44.3625 | 2026-06-12 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6cc56833-66cc-3bd0-b247-52cb1df4d3c4 | -7.3474 | -47.0188 | 2026-06-12 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 74f1cece-4544-3d14-9ad3-f41b20bd3c7f | -17.8026 | -50.4716 | 2026-06-12 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 05746c38-a526-35af-a4de-05bb9197c681 | -6.5721 | -47.9132 | 2026-06-12 00:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 787f0ab2-c8e7-3418-8da6-3a74a47689c5 | -12.4274 | -58.484 | 2026-06-12 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3168ceb5-a970-3d46-9bb1-086145da7e90 | -18.5113 | -53.5286 | 2026-06-12 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f167505a-a35d-34ce-b827-114070699b93 | -18.11098 | -50.37588 | 2026-06-12 00:03:00 | TERRA_M-M | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 94f19f5f-0c8e-37e5-8095-dd95e8657cd6 | -17.3058 | -40.36641 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 76556bbf-0e2d-3a38-bd29-fcede630cb74 | -17.29377 | -40.36865 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| 1a96fd3a-9479-3090-929a-67bec6733cad | -17.3088 | -40.38446 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 237de69c-407d-32d3-90cc-490ae97983e7 | -17.81129 | -50.48022 | 2026-06-12 00:03:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e0693e36-a4fb-305d-8e48-25edd732bc1f | -17.29805 | -40.36222 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 80a1db06-b66d-3703-a0b1-3677d26773de | -17.80061 | -50.48144 | 2026-06-12 00:03:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9218ca61-c3d7-3e2b-a600-8ec8f6d213fa | -17.29681 | -40.38689 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| c3f32493-0618-34ac-a1de-93eb6c7156ae | -17.80968 | -50.46672 | 2026-06-12 00:03:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0bf1e590-34e4-3e12-82da-252771191d34 | -17.30122 | -40.38038 | 2026-06-12 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| be5582da-ec2c-3ffe-a1ec-0d3f2d1d7498 | -17.79902 | -50.468 | 2026-06-12 00:03:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 386f7484-75d3-3091-b542-d21a8a050200 | -15.83801 | -41.90319 | 2026-06-12 00:05:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d82fa593-a934-33b5-b5cc-d70498cc37c0 | -12.85884 | -44.36998 | 2026-06-12 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 090820ee-429d-3871-a161-54cde3ac21a0 | -15.07738 | -41.98469 | 2026-06-12 00:05:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 2a27d4ec-5489-3f82-bb8f-01c4b9a0702f | -12.86047 | -44.38107 | 2026-06-12 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 545ffd6f-46b1-3125-b308-399f49e894dc | -14.2947 | -47.74265 | 2026-06-12 00:05:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 66062ed5-d440-3d9c-acb7-0e4f0bc2043a | -6.39516 | -44.18238 | 2026-06-12 00:07:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6694231d-6a48-39c0-9bb2-31a3bdbeac0a | -6.43696 | -44.54992 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2762b408-8105-3d9c-aed4-91b30c2ae0c4 | -11.80871 | -44.95266 | 2026-06-12 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ecf86774-1ec7-3a96-9695-c7302e8a5474 | -5.19877 | -47.72206 | 2026-06-12 00:07:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9ffe81f3-a574-34d1-a915-e0ca6267a865 | -5.20775 | -47.72075 | 2026-06-12 00:07:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| d9cd7b58-4e69-3a59-ad09-3ac2db23f4cc | -6.18526 | -44.86769 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 53f592ec-c636-3b27-ba9f-0f03a82aeeca | -7.3493 | -47.02072 | 2026-06-12 00:07:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 59a0ed2b-c0d3-31c9-bc6a-ca3153010516 | -10.05144 | -48.09722 | 2026-06-12 00:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05222d93-d5f2-3ea9-9229-1da992f3ec84 | -9.04606 | -45.40207 | 2026-06-12 00:07:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dbd05f10-1500-3458-a6ca-399ad30d6321 | -12.14326 | -48.44853 | 2026-06-12 00:07:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d12a77c0-e7dc-3f6a-8770-881807005e72 | -6.39314 | -44.16833 | 2026-06-12 00:07:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6588e661-4486-3a43-b32a-ddc455d1d927 | -11.31094 | -46.87541 | 2026-06-12 00:07:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d390bdd0-6be1-3ec0-8dc7-f1eb09b34a9f | -12.47861 | -45.4431 | 2026-06-12 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 987cf1ed-b617-38c1-83ff-b83c1d15d151 | -5.20647 | -47.71159 | 2026-06-12 00:07:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| fe245d7a-f57f-3b49-9e66-58a7c03450bb | -6.44524 | -44.5692 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ebc74719-0c20-3409-af77-8f5b3e36de94 | -10.62697 | -46.8674 | 2026-06-12 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6515bff9-92dc-314c-affc-33aa62be6d06 | -12.03776 | -47.80552 | 2026-06-12 00:07:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7cef3489-e24b-36e6-abea-fae759216afb | -7.62601 | -50.03664 | 2026-06-12 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8bf1f7f3-79e4-3168-a64e-0bfd08bae757 | -6.18344 | -44.85516 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1c9147b7-4395-31e1-bcf2-5e71173febb0 | -5.79823 | -45.10235 | 2026-06-12 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ceeb3b3e-4f5f-3fc3-99c7-546ddac52fa4 | -7.62729 | -50.04617 | 2026-06-12 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7c3dc669-b1a3-3c4f-9147-893023857e57 | -9.00629 | -47.99647 | 2026-06-12 00:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 251b3d8e-7172-3281-b8cc-fe47428ce91e | -6.5718 | -47.91394 | 2026-06-12 00:07:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 562898ca-0e33-39e7-937a-b70dec5266bc | -9.4645 | -48.38718 | 2026-06-12 00:07:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 627ccaac-2742-3671-8b0d-c3da089e0451 | -9.2142 | -48.57774 | 2026-06-12 00:07:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| df3442f0-a101-3e5c-98be-ed6216fd9394 | -9.62476 | -49.02083 | 2026-06-12 00:07:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aba3b020-56af-35ff-a00f-b761ab798c5e | -7.34799 | -47.01132 | 2026-06-12 00:07:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c8b95534-2c57-387c-8b1d-fdd550a7b1e8 | -6.44326 | -44.55609 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 73bf642c-5fdb-3d4a-b904-711b3fd811d4 | -8.97738 | -47.9825 | 2026-06-12 00:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9f8a19cb-2811-32f5-ba8c-6785452c6b61 | -9.21542 | -48.58669 | 2026-06-12 00:07:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 99a84b3e-e382-3901-b804-a219cf11ffff | -11.44951 | -55.9006 | 2026-06-12 00:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 3b6b0a3b-2da3-315e-80df-e0e15509b31a | -8.67278 | -46.60094 | 2026-06-12 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1b2a9182-f837-31fc-8c16-4b2738e32607 | -9.19619 | -48.64413 | 2026-06-12 00:07:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 37dabdb3-7399-342d-a6ef-764855603bcd | -5.73127 | -49.10078 | 2026-06-12 00:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e8874fb4-f32b-33b0-b888-2dcfd4ff84a7 | -6.56293 | -47.9152 | 2026-06-12 00:07:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eff11622-1400-3c0b-ae21-d07ee5e3ef19 | -11.62624 | -55.16876 | 2026-06-12 00:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 21c1247f-fc73-32b0-99a9-39ddda8796a6 | -9.31453 | -48.97075 | 2026-06-12 00:07:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3530a156-7cea-38cb-96b8-147c9fca79e3 | -5.73248 | -49.1096 | 2026-06-12 00:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 19419bb9-b885-31e0-83a3-d753a72edeac | -12.14451 | -48.45776 | 2026-06-12 00:07:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 39988e0a-8bb8-3f73-a0a3-75b411052179 | -8.03139 | -45.03624 | 2026-06-12 00:07:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f639f1f1-ea59-3f42-8729-8c02e0212137 | -6.43886 | -44.56313 | 2026-06-12 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f0eac9a8-ca1a-3452-90d2-bd6cf9cda162 | -7.71872 | -44.16882 | 2026-06-12 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 078e3309-5870-3c98-9887-f98e4124d8b9 | -5.58411 | -43.51492 | 2026-06-12 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 319780aa-04d3-31b2-8d80-b25e17fef8e9 | -7.36438 | -49.87037 | 2026-06-12 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c5be15b4-20e6-3ff5-aab8-1086baaa00b7 | -7.36566 | -49.87972 | 2026-06-12 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3580b603-ec5b-3d7b-8ddb-defc1d5a94b6 | -10.62825 | -46.87653 | 2026-06-12 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 3b10f83a-3c6b-367a-b1f4-1a9129f49300 | -7.63956 | -45.30098 | 2026-06-12 00:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 803d767e-ee06-3280-8f31-36cad58d141c | -6.72686 | -44.38649 | 2026-06-12 00:07:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ff459c01-bafb-356f-805f-1871a91f9b44 | -11.44978 | -55.90734 | 2026-06-12 00:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f34c9dbc-2862-3929-ae91-13a5a86d172a | -5.19749 | -47.71288 | 2026-06-12 00:07:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5aabc063-29ac-3951-910a-92e172090853 | -6.58192 | -47.9216 | 2026-06-12 00:07:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 59f7e057-cbaf-3174-8ca1-f37bd13a8a31 | -8.29959 | -48.28182 | 2026-06-12 00:07:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b92f4730-b729-308b-9687-2494156cf2cf | -5.80004 | -45.11459 | 2026-06-12 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 70f96329-ca9a-3b39-999b-6698ec72af14 | -10.66558 | -46.87396 | 2026-06-12 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b273e2c5-b936-3bba-9cd3-8a327e050e76 | -12.14575 | -48.467 | 2026-06-12 00:07:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8e9096c-b9d4-351b-a995-d46daffd1bc8 | -9.94956 | -48.7001 | 2026-06-12 00:07:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7d3665a2-d528-3446-8edd-ff0c5b79d6e9 | -11.62145 | -55.17446 | 2026-06-12 00:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 98c28d7d-e9b5-3850-a896-5716e5a4443f | -6.39689 | -44.17552 | 2026-06-12 00:07:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1a150387-8f3f-3ca1-9b62-a8834a8305e4 | -9.69388 | -47.70372 | 2026-06-12 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70a836b2-960a-3d8d-88d3-24cbf439de99 | -6.72493 | -44.37352 | 2026-06-12 00:07:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 0df3a5d6-80d9-3a6f-b719-b72a759a1d44 | -9.04487 | -47.74025 | 2026-06-12 00:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3f7ff626-9502-3bd5-b4d6-3567969f0c23 | -9.74375 | -47.86906 | 2026-06-12 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce3eafd6-ef6c-3bb2-b5f1-e881375657cb | -6.58067 | -47.91269 | 2026-06-12 00:07:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 710a7949-62a2-3e52-8825-ecf00ffa522b | -9.30561 | -48.97198 | 2026-06-12 00:07:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b0b08d7a-5cc0-32f0-89ab-6fb5d6c01bd8 | -9.20566 | -47.9104 | 2026-06-12 00:07:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f77c29ea-be76-30ef-b3c2-f0a8e2421a09 | -7.0058 | -43.8641 | 2026-06-12 00:07:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fe41e4e7-f274-3d0a-9f91-5e521a94bd9d | -6.57304 | -47.92283 | 2026-06-12 00:07:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9e937459-0f6f-3d64-94ae-546a3d541d50 | -8.30841 | -48.28056 | 2026-06-12 00:07:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0dec95d6-1268-3356-894b-ef02623efb65 | -11.62438 | -55.19922 | 2026-06-12 00:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 091ef425-1b56-374a-92bf-0e32ff43a0a7 | -8.56723 | -45.98784 | 2026-06-12 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6cfcb84d-5435-30e2-802e-9657386bc7c4 | -9.04758 | -45.41267 | 2026-06-12 00:07:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 877f48fa-4ae0-3985-9077-dff4f7673ddd | -9.69264 | -47.69481 | 2026-06-12 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 54ed1af2-4c38-30b8-89d9-7044e6752aff | -9.45566 | -48.38844 | 2026-06-12 00:07:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6938b09e-aca8-330e-8f11-13f8cc625cc2 | -10.05022 | -48.08831 | 2026-06-12 00:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4688cb23-e3e5-3834-b1b8-e67c8ae0c4da | -9.21571 | -47.91802 | 2026-06-12 00:07:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78b83e61-bd1f-3b1e-bcaf-c95c87d1e3d6 | -9.20688 | -47.91928 | 2026-06-12 00:07:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| d1be5624-9f1b-318e-93ff-6ae7c5f5760f | -7.47425 | -49.72936 | 2026-06-12 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70400c9a-2203-31b4-97ac-3cf6ce71e234 | -11.62898 | -55.19342 | 2026-06-12 00:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |


[Clique aqui para ver as próximas entradas](README2.md)
