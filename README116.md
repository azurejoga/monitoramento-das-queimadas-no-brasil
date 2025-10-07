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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e97825-1edc-3448-93a5-18b5a9a519fa | -16.0468 | -50.97487 | 2025-10-07 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bb5fb56b-ecaa-345d-ac8f-218b6f6d1d2c | -13.66676 | -48.72651 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 97bc1928-5d99-394b-856a-048fb151c4cf | -13.07815 | -47.83277 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4d00aaa6-6b6d-3a34-a765-e08a374858b8 | -11.85522 | -44.91352 | 2025-10-07 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| de9cf26b-0383-323b-b4fb-a61860a5f807 | -10.94893 | -51.11419 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f2f943a3-593a-3a17-91a0-09c424a1a046 | -15.4889 | -47.94204 | 2025-10-07 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9efcef3c-c275-3666-abf6-f9a18426a2b4 | -10.42922 | -50.38486 | 2025-10-07 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a0ed4219-5b1d-3eeb-85fb-9f3d2354c91b | -11.40577 | -50.86041 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 24435552-0f12-3566-95a8-a1650a6f8f5f | -16.27946 | -50.98264 | 2025-10-07 12:38:00 | TERRA_M-T | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1edb6870-a612-3901-b56e-f22eb6b0e926 | -10.742 | -46.65426 | 2025-10-07 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 13a58f2b-b178-3dae-8e0f-b075f6b6df7e | -11.22347 | -47.84959 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f8439693-4bc0-3c13-991c-64bae3c1cacd | -13.59366 | -51.82591 | 2025-10-07 12:38:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fcc977c6-9d19-3986-8f74-bbda333cdeaf | -12.21631 | -44.24801 | 2025-10-07 12:38:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7b198702-a7ea-32d8-b62f-64246515210c | -12.88958 | -54.75355 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b95e91fc-8c5a-3d47-951a-e381ef737518 | -12.38213 | -51.12391 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ec803806-6192-36fa-a6ee-5dcf023ac689 | -10.10142 | -50.517 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 690cfe02-18b4-346c-8cd5-5bdf3f402f01 | -13.07714 | -47.94078 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 41e44c12-c1ca-352a-bd24-d549efd2d670 | -12.00684 | -47.18321 | 2025-10-07 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 643970cc-f50a-3e6c-9146-a53bc2125212 | -14.50235 | -46.91811 | 2025-10-07 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 3476ec41-d57d-3c09-9d84-d61f29066f0f | -10.15459 | -53.71849 | 2025-10-07 12:38:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b2659a91-1c66-3541-ac9e-dfd8bbe5b665 | -14.75588 | -46.04065 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b69f23f9-837b-30b0-99fd-18d4643e86d4 | -11.7183 | -54.18594 | 2025-10-07 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a015ec01-ef71-32b9-9a0c-7dda70d2c954 | -11.31668 | -51.44423 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 16849fa9-36fa-37e9-8fb8-c08dbe9bddb5 | -11.95184 | -52.6412 | 2025-10-07 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 59a5c0b0-3ad7-37a3-9865-da953d5957e5 | -13.08125 | -48.00521 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 74ffa720-a404-3b5f-8404-3bfcd8f1e101 | -15.36704 | -47.31867 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 760c4955-7ce8-31e1-b319-76f51963c4ed | -13.29024 | -48.0493 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 97a56066-cac5-30ce-8e71-e21b66b4a40d | -12.38961 | -47.16529 | 2025-10-07 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6582974a-f8c2-3d48-bc22-ba0e9a1ce6a5 | -10.09056 | -50.52599 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c83734d9-187a-31bb-979f-6fc310c96bf5 | -10.86522 | -47.97436 | 2025-10-07 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 33c9eaa0-93b0-3e26-9df8-6c022e42df87 | -10.39377 | -51.59272 | 2025-10-07 12:38:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cb08c5b1-0295-3f20-b8ba-db5aa871cebf | -11.6586 | -46.41099 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 2125ce17-f23e-3e35-8a0f-1fec082301e5 | -12.43228 | -50.28403 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 408c5c08-4e40-31b7-aeae-f68b74ab82e1 | -11.6898 | -46.3552 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| bd992b3b-4741-3316-be67-08b94cb95140 | -16.38986 | -48.98454 | 2025-10-07 12:38:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 76553f0c-505a-390b-88c2-35cd28f6cdf9 | -10.47147 | -48.36442 | 2025-10-07 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 361.1 |
| 0088b3f2-a559-373b-92d9-995256a127e2 | -13.265 | -48.45656 | 2025-10-07 12:38:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ac146f9f-b5d2-3187-8b1b-1b3442fac9e8 | -12.98176 | -46.77227 | 2025-10-07 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 62815d11-ca05-3210-aae0-8085502cbe9b | -14.5125 | -46.92479 | 2025-10-07 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 63a04396-3cd9-3568-ac01-edbcaeddfd36 | -12.11803 | -45.12997 | 2025-10-07 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| a45d5b62-2c1c-3afa-a1d1-d629c0442e1a | -12.38563 | -47.17761 | 2025-10-07 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9bef53f3-28c7-3922-95a0-17f626ed3793 | -12.40211 | -47.16684 | 2025-10-07 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 984af774-784b-34dc-aeec-af384eb6bb9a | -13.09496 | -47.99133 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8e168b10-2452-3230-b91b-d6b5f753287f | -13.29526 | -48.04423 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b9682557-7b05-35e9-98aa-01c344527979 | -13.07514 | -47.9571 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 920e1f87-9e94-3be9-9f68-67c2fc970662 | -11.85163 | -44.93805 | 2025-10-07 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 28101418-03ee-3c20-b577-a78f37217b2d | -16.04832 | -50.96276 | 2025-10-07 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 74a71f4f-7420-3b8b-a5d7-b4171dcdb56b | -11.27234 | -52.74257 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 37d360dc-4b55-346d-99a7-e30287668bf3 | -10.43737 | -50.39668 | 2025-10-07 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3935b6df-78a3-3ffa-a75d-fa7eac609ce0 | -11.99444 | -47.18164 | 2025-10-07 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 199904ba-c376-30df-aa92-a605429ee06e | -10.43589 | -45.40036 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 688342e7-4812-3835-8a72-19f5d87af8c4 | -15.16759 | -52.76328 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d950e1d8-6aae-3cde-a6ed-5bb1387c8636 | -11.24732 | -50.28256 | 2025-10-07 12:38:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ccf2f185-2fcb-3a74-b089-585df3015b91 | -11.56075 | -52.79969 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e5734444-6a3e-35e1-845d-fd12703b2c27 | -10.58599 | -51.46908 | 2025-10-07 12:38:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d07b8a2d-1c87-34e9-8581-6fb4bb4da1f5 | -10.92389 | -47.07126 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7249ebfb-b48a-35ef-88cc-d5f5ab56ee0a | -10.41076 | -45.37244 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 6614474e-41f7-39a1-aa36-ea1c8c2a049a | -15.1995 | -44.50476 | 2025-10-07 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d95f1a55-b8ca-3221-a60c-7498f6b90f6f | -12.38351 | -51.11369 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cf361c82-9de4-3619-84cf-e313b48541cb | -11.23576 | -44.77112 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a1354c5c-9541-3647-b26c-f7cd88e92313 | -14.758 | -46.0335 | 2025-10-07 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 61674128-5a53-3344-8b71-ead1d3b60043 | -10.9109 | -47.1129 | 2025-10-07 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 26e1ea4e-befd-3364-b46e-dc960a0969de | -8.8717 | -46.7878 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5f110b00-0063-3907-946e-fff4bfb3da48 | -8.5395 | -46.2406 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ff764959-ecc8-3e4f-9756-40d89fb16def | -14.2953 | -45.8382 | 2025-10-07 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 490bb7a2-0815-3b54-b38a-90b6772b4342 | -8.4821 | -46.3136 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5ad45882-3d26-3480-a551-8e31294e67a8 | -10.3854 | -47.9956 | 2025-10-07 12:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ae263c32-a5b9-3c20-b3a8-b00910c25188 | -12.9816 | -46.7824 | 2025-10-07 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 346ad865-34da-37c5-8307-0f0bf9604230 | -11.7217 | -45.3738 | 2025-10-07 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e6a54bb8-2213-3785-a6a0-d39e00eadbb9 | -13.0231 | -51.0171 | 2025-10-07 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7b8c9258-e321-3b32-857c-77d5a4ea2547 | -8.1055 | -44.7891 | 2025-10-07 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 82ea70a5-717f-3529-b4d6-75ee7dcc7103 | -11.6859 | -46.3366 | 2025-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 33ff7c91-8766-311a-88d0-8764b93bbf12 | -10.1379 | -45.4954 | 2025-10-07 12:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| aa08ee95-2a4f-3e73-895a-7912aa7c1b58 | -10.4245 | -45.3907 | 2025-10-07 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 383.7 |
| e69d335f-dc2c-3f2a-aa94-b59029e6a7a7 | -13.3044 | -48.0575 | 2025-10-07 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 00a7435b-b844-3f7c-955e-11fdf171ee21 | -11.8447 | -44.9176 | 2025-10-07 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d648a6b2-0110-3a6c-9d50-0a395a5bfb2a | -10.8919 | -47.1153 | 2025-10-07 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 09e59e5f-d195-393e-940a-2bcd3e3202ab | -11.0451 | -50.9047 | 2025-10-07 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 96e03170-bc62-3119-989b-1b83534cccf6 | -10.4746 | -48.3805 | 2025-10-07 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2aa230f9-3414-3a42-8e4c-63ef2afa9d62 | -11.7221 | -45.3508 | 2025-10-07 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| febbb799-b548-32e4-86eb-5799bca53d5d | -10.1569 | -45.493 | 2025-10-07 12:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d7b2b35d-5d4f-36d5-8323-d708ec8ee6af | -12.9619 | -46.808 | 2025-10-07 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7d6ce13e-b2b6-3578-8b7c-6e8b8d3533b5 | -18.0187 | -44.9725 | 2025-10-07 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5f4fcfba-b7e6-3520-b9c0-5a1f77ad3680 | -9.7463 | -47.7144 | 2025-10-07 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 066b3402-eecc-3f9e-a1d9-3f0179c6e4dc | -15.3742 | -47.2973 | 2025-10-07 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 03068e3e-1beb-37f8-9a3a-df3c39185ae6 | -13.0779 | -47.8234 | 2025-10-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| defdbea6-2d16-3399-93de-d376f7134767 | -11.1455 | -54.882 | 2025-10-07 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 550616af-3809-3092-a790-682c58f1fa6d | -15.3737 | -47.3201 | 2025-10-07 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a9691afa-a9fd-32f0-a5f6-bb96c550a78f | -10.4054 | -45.3931 | 2025-10-07 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1e122f90-5828-3d3a-a28a-194669a57709 | -8.4824 | -46.2912 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b8c5af08-de8f-3e54-bc5e-f1ce1556f858 | -10.2506 | -44.3538 | 2025-10-07 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 867b2275-3425-3e67-9122-7b7bf67b0053 | -14.7575 | -46.0566 | 2025-10-07 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e3c24964-676a-3311-8e0d-c778fb812626 | -12.9101 | -54.7558 | 2025-10-07 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 048d45a8-f1c9-3b76-903e-cd59b516f6e9 | -12.9103 | -54.7352 | 2025-10-07 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 96e8c960-21ac-382b-ad6e-7da8fd8abc87 | -11.0262 | -50.9067 | 2025-10-07 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| dadfce6b-6615-309a-8219-c7fbe5526740 | -13.0775 | -47.8457 | 2025-10-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ba62e340-a8ca-3a82-8a06-52dea82d9dd0 | -8.6798 | -47.0738 | 2025-10-07 12:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ec403337-ffff-3360-b31d-95d2690f8ac9 | -19.5789 | -44.6198 | 2025-10-07 12:40:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d4832c75-94f9-38ff-895d-76735cf9e14e | -10.2502 | -44.3771 | 2025-10-07 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 6af54d6e-9fcc-340c-a922-1deb24eb0078 | -16.2946 | -50.965 | 2025-10-07 12:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |


[Clique aqui para ver as próximas entradas](README117.md)
