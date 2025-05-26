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
| e8f03297-66c1-387a-9178-5452d8b902d3 | -8.0123 | -43.1984 | 2025-05-26 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 7708e4b5-0c78-3f7a-b1c1-8beb1dd0d6d0 | -19.8744 | -54.3601 | 2025-05-26 00:00:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f3b1392c-98c3-3aa4-be17-5403aca1e686 | -8.07 | -43.1216 | 2025-05-26 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 642623b3-89bf-3ef7-9ec4-931de707c154 | -10.443 | -47.945 | 2025-05-26 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 949df9a5-62cb-37b7-92c9-9d45d24d1c55 | -8.0312 | -43.1964 | 2025-05-26 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.2 |
| ac11825b-5208-3ae6-ac0b-9c59d11a38d8 | -7.6574 | -46.1013 | 2025-05-26 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ef63df7f-ac52-344f-a6ee-0e955b66b826 | -10.462 | -47.9428 | 2025-05-26 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e0cf4114-a070-35ec-80d7-becdd2fa7313 | -8.0315 | -43.1728 | 2025-05-26 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| fa9e852d-be01-3d1c-9e2b-fd8b2a55f64f | -8.0123 | -43.1984 | 2025-05-26 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| c45691ec-68d0-371f-8b22-e6fde926fbb8 | -8.0312 | -43.1964 | 2025-05-26 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.7 |
| 8fa10acf-0c4e-3112-a717-dfc16e92430c | -19.8744 | -54.3601 | 2025-05-26 00:10:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3c7ec1e3-36e0-364a-8ce4-0d7c4bd25de7 | -8.0315 | -43.1728 | 2025-05-26 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| 94c9c93a-1d11-3e5d-bc42-890ddafaf39a | -8.0123 | -43.1984 | 2025-05-26 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| a0fcee6c-747f-3bc0-89af-0f0698348efa | -8.0315 | -43.1728 | 2025-05-26 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| f3ab64b0-9d28-3d0b-aa27-6eecb1a87c89 | -19.8744 | -54.3601 | 2025-05-26 00:20:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ceaf679e-6d58-332f-b759-239d2269f8c5 | -8.0312 | -43.1964 | 2025-05-26 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 4bbb926d-149d-3ab3-9e28-04e5ae56f189 | -8.07 | -43.1216 | 2025-05-26 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 36d2736a-a54a-3eac-aa63-22c9e2e7ace7 | -8.0312 | -43.1964 | 2025-05-26 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |
| bbfc4c65-48c8-3ed3-a44a-45ea3f4703b4 | -8.0315 | -43.1728 | 2025-05-26 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 0263bf5d-d7fd-3aa8-9fc5-2d4d7e805245 | -10.462 | -47.9428 | 2025-05-26 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| d30c8c9a-00b2-3c71-8e5f-598eb8ecc45f | -8.0123 | -43.1984 | 2025-05-26 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 3693d1f2-b100-304b-8292-7724a287a8b3 | -8.07 | -43.1216 | 2025-05-26 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 601fb36a-9434-307b-8e45-1ce517e3ed84 | -14.88033 | -47.85448 | 2025-05-26 00:35:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d76ae96d-cd4a-3466-8a2a-fa81211c91a3 | -13.6555 | -41.87196 | 2025-05-26 00:35:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a937b2c4-3c3c-3fee-bf67-210b2e5b8100 | -14.25192 | -47.14423 | 2025-05-26 00:35:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3c57ed86-9ffc-3306-b912-78e4d30232e9 | -22.66266 | -47.45233 | 2025-05-26 00:35:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 72d0288e-58f5-3bf0-89cc-58d1efc6134f | -21.27361 | -48.62043 | 2025-05-26 00:35:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| faa60b8f-c693-35d1-aebd-62b56d53b687 | -19.87072 | -54.37323 | 2025-05-26 00:35:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6e89fec8-ddbc-3428-89b9-665ded959ef7 | -19.87953 | -54.367 | 2025-05-26 00:35:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 111.3 |
| cc184a91-6308-3a80-aebb-c3c2cb61c31a | -23.16632 | -46.98046 | 2025-05-26 00:35:00 | TERRA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 99a7926a-e96a-352a-aa2e-d83d84aa7aea | -14.879 | -47.84436 | 2025-05-26 00:35:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 45336c18-0a61-3ead-8037-6bedb6562313 | -21.51529 | -41.24024 | 2025-05-26 00:35:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 79c524db-d9ce-3257-a3d1-8b84a85844c7 | -21.27204 | -48.60671 | 2025-05-26 00:35:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 20543856-1a36-3f90-b471-d9a53fcdb958 | -20.61357 | -48.86747 | 2025-05-26 00:35:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 3cee8c03-8369-3a51-b3f8-49f55be9ec49 | -21.51796 | -41.24534 | 2025-05-26 00:35:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 706bba2e-b88b-385d-9ad4-66cc45cc8047 | -13.61425 | -48.94388 | 2025-05-26 00:35:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1196878-ec67-3509-97fa-b38459295576 | -10.45611 | -47.94089 | 2025-05-26 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| cd82a6d8-7ab3-31f2-ab50-7cb37b2246dd | -8.04609 | -43.17702 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| dd2b0a8b-8ff0-32e6-81a7-61b288a38833 | -8.02481 | -43.18036 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 8e48c5e0-e7bc-3932-90c0-275c7c7681f7 | -7.54317 | -45.82258 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f7cd634a-14b9-3132-9280-88c8ead5ba5a | -10.49136 | -42.42505 | 2025-05-26 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f088d79f-6541-37f7-8399-79f4cf6fcfbd | -8.05287 | -43.14906 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 98d8f99d-749a-3ee1-90c6-5072bcb16dda | -8.44475 | -49.6281 | 2025-05-26 00:37:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d8133fc8-c315-3ba6-b552-13f90d4db1bf | -8.02677 | -43.19348 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.5 |
| 9c278e72-d703-3e52-92a2-4b26fcac71cb | -8.07611 | -43.12616 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 71d07563-83bb-303b-a932-e49c8988f772 | -7.54455 | -45.83212 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2891aac1-eb2b-30a7-ab91-3f5331781a32 | -8.0374 | -43.19182 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| c8760452-92bd-3513-af73-1be167825536 | -8.04416 | -43.16398 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 95712e24-3037-3c1c-8614-544025e08a06 | -11.14522 | -53.92772 | 2025-05-26 00:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9f7de806-b5e2-37ce-9ef2-8d71e0443b75 | -11.86629 | -52.25154 | 2025-05-26 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| aa966055-0030-3c3e-b1af-36a9a0679bfb | -8.0548 | -43.1622 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| ea09e7a9-f22e-374a-899d-809a6f62e008 | -9.3793 | -48.42106 | 2025-05-26 00:37:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6facb0d-d671-3c82-9dd8-ec985608af31 | -8.03545 | -43.17869 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7d6b53ea-dc7f-3791-bfa2-700d1fcc9aa2 | -11.3026 | -54.02091 | 2025-05-26 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 54eff0a1-bdc9-3e77-af6f-83b5c6326432 | -8.44611 | -49.63837 | 2025-05-26 00:37:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 07a91c69-e339-3f0b-8d64-00f878c6a971 | -7.65822 | -46.11184 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 07439662-5295-3fe6-a7b9-7d8abb734cc2 | -7.59962 | -46.28051 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 997fbf2f-42ea-3698-a935-425a4a7a4f64 | -8.01616 | -43.19527 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.1 |
| c6d842aa-bd84-33dc-96f9-3920163b1ada | -10.65594 | -44.50011 | 2025-05-26 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 84dd65e5-2342-3a4b-bac0-24866252023d | -8.07814 | -43.13947 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 330e1ef7-9b0c-3dc4-bd79-29d10d412b45 | -9.37805 | -48.41171 | 2025-05-26 00:37:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e24fb6f0-ad66-3b76-9611-015ef19eec0e | -8.01812 | -43.20833 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 74ed9d5b-3c51-3d11-b936-1a0116b70f3e | -11.87349 | -52.25622 | 2025-05-26 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 78271b68-cc0b-3e94-b230-41ea42a323cc | -10.49574 | -46.82049 | 2025-05-26 00:37:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0467fe7-77e2-3beb-9e8c-0cde0ead76ff | -6.83496 | -44.62518 | 2025-05-26 00:37:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e0c41010-43ff-3506-b9fa-e75a4a2fdd85 | -7.66674 | -46.10431 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 460eb27c-79c8-3513-9c58-5888f7660223 | -12.25498 | -46.68557 | 2025-05-26 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 289bae09-a00c-38b9-bfd5-c2feb2c6fe48 | -8.02874 | -43.20666 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| fd7329ce-023d-3373-8e69-28354bb9f0e4 | -8.90565 | -44.77801 | 2025-05-26 00:37:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 668401da-55d7-3c9d-867a-68e138fd2a12 | -7.59831 | -46.27133 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4a8df81-e0da-3f93-9d5e-4f3f0daf6738 | -12.27361 | -44.60033 | 2025-05-26 00:37:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 27803416-2a8f-3049-9a07-f6d8ba7c972f | -13.31114 | -48.88195 | 2025-05-26 00:37:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d3e043a-4dc6-3f6b-810f-7dcd90139bf7 | -10.65447 | -44.48986 | 2025-05-26 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6611895-bcec-3970-810a-2114b29e6ac9 | -8.06746 | -43.14104 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| a997576f-04c2-3faa-b53a-bf66fe963266 | -8.06544 | -43.12781 | 2025-05-26 00:37:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 4dcd5c54-c12c-3a91-8022-374e0880bdb1 | -7.65693 | -46.10263 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 64ba6353-d0ec-347d-a646-a869bc77916b | -10.64657 | -46.96835 | 2025-05-26 00:37:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1fdde8bf-1c61-32dd-b529-39f5ffcb0fe0 | -10.45736 | -47.9501 | 2025-05-26 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7377df52-6ffe-3e87-ab59-dad8b9376d28 | -7.91036 | -44.48022 | 2025-05-26 00:37:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f28b2660-48fd-3681-b059-d3d0e1ed6500 | -10.48816 | -46.83068 | 2025-05-26 00:37:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc65f712-0dd7-33ee-9947-47cc2ada6077 | -10.17443 | -47.22772 | 2025-05-26 00:37:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 424db6fa-060e-3938-885a-ed6ad7991212 | -7.66806 | -46.11355 | 2025-05-26 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b4d2042-5279-3383-be7e-27fffdfeac85 | -10.49697 | -46.8294 | 2025-05-26 00:37:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b1cbd9e0-aa92-3583-94d7-b500caa487bc | -9.98074 | -52.13966 | 2025-05-26 00:37:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eaa8bba6-9d62-374d-bd37-f94f09a08faa | -8.07 | -43.1216 | 2025-05-26 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 383b715c-c479-377e-acf9-4f3ab4bbce4f | -7.6574 | -46.1013 | 2025-05-26 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 231ae918-39f0-365e-9d83-4f0c5b470fe8 | -8.0123 | -43.1984 | 2025-05-26 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| e74f1a38-ed7f-3f89-a002-499acb3772d9 | -10.462 | -47.9428 | 2025-05-26 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9c7b06ec-5abe-3c53-b8c4-ecb509dc7737 | -19.8744 | -54.3601 | 2025-05-26 00:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 9bc4f871-0fde-33a8-bb26-cf33d0434cdb | -8.0312 | -43.1964 | 2025-05-26 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 13dbf467-4276-312d-a663-90f4dea0402f | -8.0315 | -43.1728 | 2025-05-26 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a97b97dd-1d64-36a8-85b0-047f41c451fe | -13.785 | -54.305599 | 2025-05-26 00:44:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f08cc8ca-f5c3-38a0-abcc-290bb3275306 | -19.886101 | -54.361698 | 2025-05-26 00:44:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0c05cba3-2172-3b8e-915e-11e1e45d8761 | -14.0453 | -55.125999 | 2025-05-26 00:44:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5be92b47-2767-3e22-bf18-9c1f0e02ed96 | -7.6472 | -46.0877 | 2025-05-26 00:44:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0efc0b-f7e8-3709-ab56-a464feccff3d | -19.874701 | -54.356201 | 2025-05-26 00:44:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e80feda7-cace-3e63-9621-76ff25a53982 | -21.274401 | -48.607399 | 2025-05-26 00:44:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d0822f3-3513-378d-9a2e-dc20e3ac64b4 | -11.8709 | -52.250599 | 2025-05-26 00:44:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2be1f217-b8e4-3f56-a7ea-27f21071680e | -7.6521 | -46.107399 | 2025-05-26 00:44:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 879cf27a-04b2-3324-a3be-2a981df0f216 | -8.4376 | -49.625999 | 2025-05-26 00:44:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
