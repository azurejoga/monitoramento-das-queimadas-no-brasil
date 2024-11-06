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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7b6f08-bb54-34e8-bc85-59d6e0b0a4e2 | -3.01223 | -53.43837 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e5b27964-5f88-322e-845f-548b337c95b6 | -3.51428 | -51.36254 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b742930a-83c8-3e1f-99ed-411601673e73 | -3.05866 | -50.50394 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7263f243-325d-342d-9447-d57481bcc803 | -4.13511 | -48.88349 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52da5823-aaaf-31a1-8c58-727b04bc9d05 | -4.99369 | -44.88108 | 2024-11-06 04:36:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f40bd7ab-e513-3986-af97-ca570d4433d4 | -3.49141 | -50.2932 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab388f5-2bd4-3f93-9dc6-68a918b839d8 | -0.39919 | -51.99781 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5e7b1be-32de-3b8f-a8a3-33bc0d35ab15 | -2.43663 | -51.58196 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebb4d711-16ee-34c1-84b2-d038fed209c3 | -3.10276 | -50.25043 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d4ae7c3-d819-341a-ab35-d5bbe76d1218 | -4.07514 | -53.94097 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b8ae1945-b3af-3620-a8c5-c3f8d403eee2 | -4.34558 | -45.89298 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24425f76-da5f-352a-a8e1-c3073c389307 | -3.11307 | -51.10756 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e5b0cad1-25eb-3553-a12e-5ca8b01e3414 | -3.06002 | -52.49709 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b665efc7-c58d-3dfe-8f57-9ca8a6ae44b4 | -2.81236 | -51.49244 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b0b084c0-047b-3dbe-b6c9-f4da40a8447a | -2.93225 | -51.05716 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00fd7417-e3e7-3265-b8f5-589508e6fec0 | -3.52757 | -50.35762 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07843764-a451-3ccc-a65d-8ee73c8e14ec | -2.78989 | -48.57743 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8f1ae96-e441-37a9-a002-d04782d2f78d | -3.96971 | -48.16117 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fc7c6ee-0815-3b4e-8cd0-9e7d6c1cbd96 | -3.24791 | -50.19611 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50185d14-8e51-3c59-882f-3fb8290273de | -2.54195 | -49.2257 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125ca1f8-60aa-3d5c-a754-a40bd7d9b1cd | -3.25414 | -50.9265 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6b29a5-b19d-3cb6-ab7e-83951ba6d9f4 | -4.13292 | -43.58356 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 17e02f29-7dcc-3b44-9df3-ab796b3d5e08 | -3.74999 | -51.31516 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7686d0-9719-30e0-ab12-5dbc95f8e661 | -3.13109 | -54.25387 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d80a86-1fd3-32a1-8ff8-23a7b934adae | -2.67436 | -48.51368 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b49f273f-3b84-32c1-b18a-cbe88051e04d | -3.5247 | -50.37562 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae435be2-8c6d-37ed-b3bd-047fabd1b7e8 | -2.92078 | -51.03964 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37ffc3ba-b7f0-31b5-9f86-5e2ed6d386e4 | -2.64497 | -46.77481 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0290f274-b806-341f-892e-095fca7a4fef | -2.6068 | -51.30646 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| add192c3-ccf3-34f6-9a79-196620244052 | -3.24293 | -52.21317 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f0d1eb-c3d5-365f-a1e3-28320ba9ad2f | -2.64799 | -49.88712 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66abd443-c8d8-3058-8cec-50515841fba2 | -2.9423 | -54.79772 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2105208a-c33d-3281-ade0-07d67333d46a | -3.18325 | -50.57994 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57006c6e-5be5-3522-859a-f4aefda77f9a | -3.69248 | -49.81616 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ab6819-b42e-3fd7-a055-9d1f3cb9594d | -3.62391 | -50.25131 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dce167e-11f4-3f56-ad29-8ec3f526ca93 | -3.0987 | -45.93657 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96018f4c-dbb8-395c-aa62-ce4b20b73d49 | -3.96259 | -49.93401 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68f8900-3869-39e1-8008-6f75b2fe2f3b | -2.95004 | -48.64093 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71a4ec6-59c5-366f-87d5-03dfc165123c | -2.42977 | -50.50957 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eac9b8b-2765-3911-ac2d-41a57bee5828 | -4.73704 | -48.96764 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8651000-e39f-3f1f-a248-fdc6350530ac | -2.85306 | -51.77624 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 657903fd-4ae6-3855-8965-caee363fc6cf | -3.01385 | -53.42812 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9f5e990c-f5e2-38b8-97bb-7db0d720ebe8 | -3.97411 | -48.15474 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07ba518-b0fa-3afa-9106-62f1f00ce5c4 | -2.88233 | -51.30405 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ab1023-ddc3-3394-8fac-891b4aa0a7c6 | -3.30695 | -50.04092 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83fa8ca4-f47a-3777-b8c1-a1b907959fbc | -3.101 | -45.94504 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb64ae5f-2a0e-36e4-8203-2b89eb4229c7 | -3.24609 | -53.40392 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb3504aa-e14a-394a-a17e-3bc24f22c1ae | -4.35022 | -48.61789 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8a88166-281c-37c5-88cb-84db7e527871 | -2.85122 | -51.77803 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| c8cf915c-1888-384e-9917-52abf426e274 | -2.81531 | -48.43724 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69321cd3-affa-3dac-afeb-cf0dbb409685 | -2.31339 | -46.47472 | 2024-11-06 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e246aa2-d27d-34f3-bcca-b0f0fb0f96e8 | -3.35103 | -50.25258 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae76c470-701c-3569-9b1d-016bd2e390c5 | -3.01169 | -53.43484 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2f414c17-3bfc-321c-8e86-edc7b7ed90e3 | -2.84762 | -51.77745 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 44c1f8d9-a6ac-3cc1-acdd-ef72cf5cf5dd | -5.22868 | -44.91564 | 2024-11-06 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08defd4b-bc83-3d9b-ab18-7dece237659d | -3.63799 | -50.14019 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74d8f12e-28bd-38c5-a231-2a7324277b4c | -2.87896 | -51.6168 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3bddba-0465-36a4-954e-38361423fea5 | -3.53513 | -50.28878 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d3de498-db5d-381a-a1cc-1377f149f858 | -2.34576 | -48.94025 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b851fada-7156-334e-8a19-4d6b91341efc | -4.2473 | -48.03666 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dda17ef9-4b7f-360e-bb71-c9fed45fbc14 | -3.22559 | -46.53739 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07490288-b697-38c0-87b2-ae22e1eaef1a | -3.09424 | -53.71673 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b00efbfa-1ab4-3c0e-9b2d-8059afa419b0 | -3.73186 | -52.2716 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a4f5496-11d5-3be7-9d8a-8351de73b66b | -2.85008 | -49.4691 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0cc7201-a0f7-3d3a-a89e-4c3330ffd09e | -3.17648 | -53.85038 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16873880-eaa1-315f-b5ec-513cda597fa9 | -2.8431 | -51.34629 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2746c24-a38c-39e8-bf14-b53ceae9df99 | -3.83809 | -52.16994 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2af19c79-53fd-39d9-9bd6-44ced2b5c62f | -3.87336 | -52.36922 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 867c8880-5734-38ac-bd27-7173e062738e | -1.48134 | -47.21803 | 2024-11-06 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23e38871-854e-37c1-ac69-780d81726b9f | -3.57992 | -53.52711 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ea561d-4eea-38a7-bcbf-a778ab66ce11 | -2.39262 | -50.32333 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eeb843d-0b00-3c43-b187-3a3a43545e64 | -3.08888 | -50.26394 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4480aa35-40c4-356a-a1f9-d09d7abbfa4a | -2.84946 | -51.77567 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 2b4b0b6b-15a6-3cbb-a852-37684b676fe7 | -2.37989 | -50.40394 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ddb9c9-6955-3f14-a73f-6fc4d2995ee1 | -3.05731 | -52.49958 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32355b26-0b05-31fa-b6e8-e2aaf1b96447 | -2.5185 | -46.30108 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a43b0ef3-ac90-3548-adde-86ead8a8cd07 | -3.23907 | -53.39757 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1c9eff2-e1dd-3053-a449-d218112c57c4 | -1.0872 | -48.21209 | 2024-11-06 04:36:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b9f6409-e55f-3ac6-8779-836608e8d839 | -4.1277 | -43.5729 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36cf69b7-2944-391f-985e-ff9ff716d4c3 | -3.29204 | -51.04517 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3518cc0c-69ae-3500-915e-332d75488d92 | -3.01732 | -53.42532 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2060a503-1108-32a8-abff-4ac12435f347 | -3.65352 | -52.33832 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e6d39c6-a729-389d-8387-ca1307b1e6e6 | -5.62398 | -44.18456 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a263d6dc-50c6-316a-9457-385d1956a843 | -3.54517 | -51.3037 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4140edf1-f535-3b39-91d4-58758814d8f2 | -2.38671 | -50.40501 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 632c513b-f31f-322d-8eb3-f42776cba82a | -4.0872 | -51.04597 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09a777bf-aaed-30e5-a5be-5790f0bdc448 | -2.87914 | -49.32788 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d759fee-9250-3886-b3e5-075b7040e2c6 | -2.34065 | -49.12306 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42cf4cc-4953-336a-8f85-87921f2aa4b8 | -2.65529 | -48.57047 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27e6893c-1ef6-3a5f-b7ad-f6bde36135c6 | -3.83663 | -44.13414 | 2024-11-06 04:36:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eb2c3fd-4835-35c8-83b1-4d026cbb27d0 | -3.11792 | -50.26388 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 442759a1-dab9-331a-a7b0-bdb3bbd9f7ba | -2.53918 | -49.22171 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf8cd96a-f7ed-3b0d-ac8d-5336819f9b57 | -2.99218 | -53.85435 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6f5465c-bfde-3f60-b14b-411ce1d571ff | -4.05334 | -50.35142 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842f33d6-9e86-316a-b4e5-d612e939dca8 | -5.20812 | -47.44508 | 2024-11-06 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 849d23e0-92cd-348c-95f5-896dd2f1c535 | -3.34429 | -50.25151 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2289db22-f6e2-3fdf-a6a8-563dcdc12835 | -2.957 | -50.99061 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 778546a6-a26e-30e2-be3d-2a0d1d31ca1b | -3.81394 | -46.4638 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3136a590-349c-3b6d-8172-3fe6633e939b | -3.6595 | -50.25647 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a9152e-b4fa-30b2-a9cc-349dc6f0c52d | -3.32818 | -50.0807 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README50.md)
