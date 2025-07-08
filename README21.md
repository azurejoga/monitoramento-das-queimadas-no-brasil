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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b35c49a-a4b8-3b52-ab31-483a67557f6d | -11.4393 | -45.1154 | 2025-07-08 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b58733bf-b835-32b8-a4d7-5c9467e50d23 | -11.4201 | -45.1181 | 2025-07-08 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a55a48c1-e162-3b40-811e-11cbbedcec15 | -11.4205 | -45.095 | 2025-07-08 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0dd4043c-9663-3c84-9750-37ecdf411f2b | -11.4397 | -45.0923 | 2025-07-08 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fe791d22-c031-3afe-bcf5-14178e1bc620 | -10.6299 | -49.4504 | 2025-07-08 07:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 5c9bfed5-3184-392e-b03a-b235041c9bda | -11.4393 | -45.1154 | 2025-07-08 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a7dc962e-75a1-3fb9-8889-f62ef8b0ab99 | -11.4205 | -45.095 | 2025-07-08 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 71c8d244-9bbe-3650-9df3-3ea6a1663c82 | -11.4397 | -45.0923 | 2025-07-08 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e5e5ec32-3cc9-3d73-bb7f-c3c2acfcc4ea | -11.4397 | -45.0923 | 2025-07-08 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 76bec188-02ab-3c89-9022-76c71fd0ea39 | -11.4393 | -45.1154 | 2025-07-08 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 97c74d76-5eda-3af9-a8c1-213349970cfa | -11.4205 | -45.095 | 2025-07-08 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 942ea842-63bd-3bfe-b88c-683484436de8 | -10.6299 | -49.4504 | 2025-07-08 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| a098ad6c-2032-3fc4-bbf7-42d6ed111d51 | -11.4397 | -45.0923 | 2025-07-08 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f0a08489-aac2-3bf2-87dd-1915a70a4b9d | -11.4393 | -45.1154 | 2025-07-08 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8278465b-503e-3c32-9fb0-2a5a112f6cb9 | -11.4205 | -45.095 | 2025-07-08 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 5c626138-5ba0-3b36-8830-51745eb74fdf | -11.4397 | -45.0923 | 2025-07-08 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 23bf34c8-c726-327a-bb9f-a76429b4631b | -11.4393 | -45.1154 | 2025-07-08 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 5039c10e-7a51-3f9f-bd8e-d9e2d3b37a5f | -10.6299 | -49.4504 | 2025-07-08 07:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2eb4e876-7b00-3886-8615-4687438fe0cf | -11.4393 | -45.1154 | 2025-07-08 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6f35c213-810c-3350-a928-7612bf2c9db6 | -11.4397 | -45.0923 | 2025-07-08 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| eafb6e0e-16c2-35de-9946-efe3d13a02b9 | -10.6299 | -49.4504 | 2025-07-08 07:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 406bc5f5-38ef-3150-9ff2-070f8ef5cfe4 | -10.6299 | -49.4504 | 2025-07-08 07:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 68f08436-e152-3bd5-867e-93966372b3d7 | -11.4397 | -45.0923 | 2025-07-08 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 69967c91-4655-3756-8ac4-cd981a247423 | -11.4393 | -45.1154 | 2025-07-08 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0044fa6a-4873-3361-b85d-78f7c3721056 | -11.4397 | -45.0923 | 2025-07-08 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 18ebd289-c34b-36f7-94e2-87ae81e2756a | -11.4393 | -45.1154 | 2025-07-08 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 72fd4146-0771-31f2-a82a-97ba51fae769 | -10.6299 | -49.4504 | 2025-07-08 08:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 745f2663-8c85-3627-a9ca-f8ec9d3288e4 | -11.4393 | -45.1154 | 2025-07-08 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a00b2075-73fe-3bc9-9768-058d69ca68db | -11.4397 | -45.0923 | 2025-07-08 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a33fded3-cb54-3488-9e9b-de56d3d3a3a5 | -10.6299 | -49.4504 | 2025-07-08 08:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| c5f9e1ab-4a5e-3bad-a3ec-88ce7035d9cd | -11.4397 | -45.0923 | 2025-07-08 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9a36e923-5523-30e9-bc93-1de8b87303db | -11.4393 | -45.1154 | 2025-07-08 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 6c1c3a09-8f79-3577-9fe8-f3926b5e0e30 | -11.4397 | -45.0923 | 2025-07-08 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d9ced31d-e672-3d3c-a309-5881e9bb103f | -11.4205 | -45.095 | 2025-07-08 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 448b19af-eea1-3728-963a-60eb9dc6e199 | -11.4397 | -45.0923 | 2025-07-08 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7bd90130-b2ca-3d0b-9101-8b93c2dfdc86 | -10.6299 | -49.4504 | 2025-07-08 08:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2764c36b-6113-3d67-b089-c51bdf0aa3a8 | -11.4205 | -45.095 | 2025-07-08 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 53e041ac-655b-3216-bf4c-3c4b214d83cd | -11.43847 | -45.10481 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 0b690bfb-288f-367a-8509-f701b5889060 | -5.85347 | -39.03649 | 2025-07-08 11:49:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2e86f0c5-2842-3c76-812b-112e5346a5a8 | -8.39171 | -44.02645 | 2025-07-08 11:49:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 179e28f1-83b4-37ad-9baf-1ebe17ffd884 | -4.18989 | -38.35418 | 2025-07-08 11:49:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ff26d7b0-0bfb-3ff6-b707-6dd7236d6979 | -11.57132 | -44.84975 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 39b8b306-1c15-37bb-bf1a-382cfa54d7f5 | -11.57403 | -44.83279 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 034dfeed-85c2-343f-bdce-101850d72075 | -6.7299 | -38.66098 | 2025-07-08 11:49:00 | TERRA_M-M | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4025e82f-fd9e-3b69-8b7c-965aee5ebe15 | -11.56819 | -44.83773 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 24d24228-002a-3dc4-ba55-51e0fe555e30 | -4.48322 | -38.0385 | 2025-07-08 11:49:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3e043f3b-4c12-39f4-b2d4-6b148ccd831f | -11.57103 | -44.82084 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 8c8fdea6-daa0-3d04-a836-cb339f7728cc | -11.46622 | -45.1166 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 82706d6e-68eb-395e-bfd6-fd93776d27f5 | -7.00573 | -43.6953 | 2025-07-08 11:49:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ee416856-b75e-3c85-8986-89e01207e826 | -7.00315 | -43.71186 | 2025-07-08 11:49:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b9856268-7a82-3378-a87f-5e680cd0f706 | -6.31533 | -45.33777 | 2025-07-08 11:49:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| c47bc042-384b-31d2-ab75-0262f913ec72 | -10.9721 | -42.17877 | 2025-07-08 11:49:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 29f67bb0-9cfa-3215-aee0-e9d133cec87a | -6.31188 | -37.71955 | 2025-07-08 11:49:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 14673461-c742-3c3e-be3b-2b44e4791056 | -8.07379 | -43.11847 | 2025-07-08 11:49:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9bb21f8d-80dc-3911-9497-3e1f84535193 | -5.78382 | -43.61619 | 2025-07-08 11:49:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d694b2db-931f-36cf-803e-642ce54af514 | -8.3028 | -45.14282 | 2025-07-08 11:49:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f6dd0d9f-a5b8-3876-a020-757e6b5c98e7 | -10.97381 | -42.16749 | 2025-07-08 11:49:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 761552ca-3977-355d-b9cc-164c23711471 | -6.13521 | -43.96234 | 2025-07-08 11:49:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c975ae3f-ccc3-3ed6-8981-6e37e8a4e69f | -11.42982 | -45.11034 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 0849c592-23a9-3719-86c8-0b4b19e06ac8 | -8.38343 | -43.95252 | 2025-07-08 11:49:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 85b1987e-520c-38d5-8e4b-bfea8a4a66d0 | -5.20272 | -37.66965 | 2025-07-08 11:49:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 922b1e5a-704e-39d5-92bc-6f443d029669 | -8.39437 | -44.03794 | 2025-07-08 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ae1fe948-9f28-3e87-ae0e-f95c68411291 | -6.32589 | -45.32285 | 2025-07-08 11:49:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e377516c-d646-3d1f-b2da-4ad8b8e0b3e1 | -6.3188 | -45.31553 | 2025-07-08 11:49:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 2e85538d-4f27-31ce-a3f2-dbac629a5efb | -7.82351 | -44.19632 | 2025-07-08 11:49:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| f680af4b-a69a-301e-8efc-df0018354860 | -7.8262 | -44.17956 | 2025-07-08 11:49:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 22168194-7547-340c-956e-67d27cfa587a | -8.39692 | -44.0213 | 2025-07-08 11:49:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1abaf237-61f0-37d5-9c39-817b7c15d3e5 | -8.87976 | -39.92722 | 2025-07-08 11:49:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 15.9 |
| c04df5a5-f2f2-3eb1-b623-ac133c095e78 | -8.38903 | -44.0431 | 2025-07-08 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e888eedd-4e90-35a3-9444-b8d8a7960b4c | -6.01936 | -44.53898 | 2025-07-08 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ce9ea55d-7009-344a-a7b1-9569e92f22e7 | -5.86239 | -39.03776 | 2025-07-08 11:49:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 645e7091-4e2f-3e47-abe7-59b9484ffeec | -11.42632 | -45.10277 | 2025-07-08 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| cc06c0ff-63ca-3690-b86b-c150f2f8ec23 | -6.99135 | -43.7101 | 2025-07-08 11:49:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 04f473ed-1018-3c14-a40c-bc9ce282ccd5 | -20.46324 | -44.74427 | 2025-07-08 11:51:00 | TERRA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 30329bc9-fad3-3f39-87b8-e4936fa684dc | -18.96309 | -41.02498 | 2025-07-08 11:51:00 | TERRA_M-M | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d0016b6d-1b1e-3b39-bf20-5f2909f2f42b | -16.59494 | -41.1339 | 2025-07-08 11:51:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 4733886e-6a78-3370-92b0-4a18cafba29c | -13.61827 | -40.90795 | 2025-07-08 11:51:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 87ce1963-c9a8-3aec-bc32-5ba59976f55f | -15.40075 | -41.82541 | 2025-07-08 11:51:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fa085291-141c-3a1f-a801-e5bf3bf0ac94 | -13.61688 | -40.91729 | 2025-07-08 11:51:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 152afb01-c1de-3f97-a34d-65a6a7b1c3d3 | -16.30596 | -42.98259 | 2025-07-08 11:51:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 691cba54-f5b7-3a47-9c53-c71b1c3b2cfd | -18.49094 | -40.46002 | 2025-07-08 11:51:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d68b3559-c9d3-3736-85e2-b973f7c51a1d | -15.28625 | -39.78219 | 2025-07-08 11:51:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| ffb8a3ba-933a-3945-b453-8e7416cdc7b1 | -16.59356 | -41.14314 | 2025-07-08 11:51:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 202cf4a0-167c-3221-a6d4-38779a8f59d0 | -16.33586 | -43.52267 | 2025-07-08 11:51:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ca4eb4e-c2af-3e0f-9956-06ce550b539c | -16.68309 | -41.34505 | 2025-07-08 11:51:00 | TERRA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 8c58a133-59bb-33f2-b732-7aebd9e82cd7 | -15.74582 | -42.64285 | 2025-07-08 11:51:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 3b43cf09-758e-3ccd-8a63-5f2f99942df5 | -20.46406 | -44.73796 | 2025-07-08 11:51:00 | TERRA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| af793b3b-3135-30e8-a830-d9508f81e0aa | -22.71402 | -43.2366 | 2025-07-08 11:53:00 | TERRA_M-M | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 56ddfb27-befe-3e16-ac94-8d8dc58413aa | -22.71555 | -43.22656 | 2025-07-08 11:53:00 | TERRA_M-M | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1210f6bc-961f-36be-a353-cd871039b664 | -10.6299 | -49.4504 | 2025-07-08 12:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6f737c91-015d-3318-9320-7a54495dffc1 | -11.4584 | -45.1126 | 2025-07-08 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0452d2ed-8b08-369b-aae9-32a316cef604 | -10.6299 | -49.4504 | 2025-07-08 12:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b7ce117e-e185-346a-a54d-1554bebfc8a2 | -11.4584 | -45.1126 | 2025-07-08 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| b84f227b-2894-3b5c-b6a5-a48622c7e01d | -10.6299 | -49.4504 | 2025-07-08 12:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f22852d2-fb03-36c7-9889-59a25d8f5be3 | -10.6299 | -49.4504 | 2025-07-08 13:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 18e30f62-d0f3-37de-8f8d-26491436e028 | -11.4584 | -45.1126 | 2025-07-08 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 88a62b1a-93cf-37f1-b81b-e1a7176d2c57 | -11.4588 | -45.0895 | 2025-07-08 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9374114b-7910-3fd0-ad4b-23fed0b63e53 | -11.4584 | -45.1126 | 2025-07-08 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 10d60b2a-25db-39d0-8bd5-e6091c3cc841 | -10.6299 | -49.4504 | 2025-07-08 13:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 109fbc89-61a8-3cd4-8ae7-0c9af8c52ee2 | -11.4393 | -45.1154 | 2025-07-08 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |


[Clique aqui para ver as próximas entradas](README22.md)
