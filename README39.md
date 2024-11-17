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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57692a2f-39a7-3c8d-842c-d6c32017810d | -4.55728 | -48.01035 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a218991-fb4b-3280-9962-d411303d0978 | -0.77493 | -49.47631 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9e156fb-8d7e-3508-9209-a8b123842ba6 | -2.63002 | -48.56761 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 057d9e0a-b4cb-3e01-b9df-7159730154c4 | -1.62224 | -48.6856 | 2024-11-17 04:29:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c421c35-ea58-3a89-85e8-7565be2895c5 | -3.93738 | -49.99517 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79030973-39c4-3b76-aba7-a286e38f8671 | -2.68459 | -46.82722 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d8c2a6b-f4da-348d-920b-3db647a3d745 | -2.18082 | -50.33998 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e51efe-4001-3c64-b4c5-f5ddaf06be96 | -1.90964 | -46.56827 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d941789-bbcb-3196-9de8-390851e0b03a | -5.46131 | -42.15239 | 2024-11-17 04:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bc672cd5-a32a-3ac0-a520-c5aafbcc66d9 | -2.45277 | -48.48894 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 015cc8e0-432d-31c8-bb79-7f0b056b7d33 | -2.77506 | -48.57939 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e9c143-9e6f-3d17-99b8-25736807d73f | -2.53113 | -47.13375 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a79330-f698-3908-ae86-3f5a480b1739 | -0.12708 | -51.62562 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc23b69a-e8db-372e-ba89-eb355fbb8597 | -4.57883 | -48.02438 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d6aa488d-4bf0-3d00-b02e-1ada6f81758f | -2.79123 | -45.95323 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34ff7aa3-1091-36a1-a15c-e9ac62da32d5 | -2.68182 | -46.82327 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48add0f9-d80e-3203-a667-c5db5ec274d1 | -3.58601 | -50.52177 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb76c6ed-c77b-3b57-b5d1-7e7d177e3718 | -3.56463 | -51.64719 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cacd881b-454e-3a00-928a-5407fdf728d1 | -3.79578 | -51.36976 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb46fca9-207b-380d-b552-cab3cd996bc0 | -2.29218 | -49.12893 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44232371-78d7-3aa3-bcac-cec4aefb866d | -2.79457 | -45.95374 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e878a866-747b-30bb-a5a2-6a82c5cb0809 | -1.23189 | -47.35669 | 2024-11-17 04:29:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9a2f7b76-cafe-3374-b682-8b9202436682 | -2.12776 | -48.9453 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52b514b0-4cfe-3261-b3c2-ce1944e3c364 | -1.1056 | -52.31569 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f6335b6-07eb-39d7-a310-53bcf26bbcb2 | -1.36771 | -51.11454 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b202bcbf-ec20-3889-a56a-b3fc7880053d | -3.78206 | -46.67425 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa4de3d-ce10-3514-a9f2-bc25a0eda2c2 | -2.28574 | -47.48285 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ed6dfcf-c70e-3a2d-8513-120afc0fb6a1 | -1.99874 | -46.58604 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b2f76fd-6218-3771-999b-34f27ffdf81e | -2.34017 | -54.83093 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e32de9ca-9586-3d5b-8274-9671e7eb6835 | -3.49776 | -43.78892 | 2024-11-17 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5263eca7-c01e-34d7-8b87-9d9f258e3340 | -3.56528 | -50.25796 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf333932-8b54-35de-ae1e-262fdac40537 | -1.62008 | -47.52383 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe77cf19-4049-395f-9d0d-ace8f0671169 | -0.31646 | -51.50917 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 11a63094-9374-33f4-bf38-df1918502fb5 | -2.4602 | -45.61218 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22cf345e-6507-3c91-8534-7b3dc70eed53 | -2.635 | -46.5588 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58ef75d5-98c3-38aa-b407-0406558323c8 | -1.67279 | -52.97469 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6c7e548-142a-3850-956a-e5e7cd105ad4 | -3.00798 | -45.42735 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c43c4f5b-a5c8-3f7c-a46f-af2044cbca78 | -0.1049 | -51.60734 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 887d99e0-a2c1-301c-a48a-34b0844d7c5a | -3.52175 | -50.26463 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d06793d-71a1-3355-aea9-8e277c6708dd | -3.09193 | -45.17794 | 2024-11-17 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 158edde8-029d-3008-aa7f-d28037b50e3b | -3.78444 | -46.04826 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02cc6204-0fa6-3c09-b368-f5a3d6510c18 | -4.13916 | -42.13019 | 2024-11-17 04:29:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a65ba202-1dc4-3ae5-bd77-7b4d71544cd3 | -1.94817 | -53.33379 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f38e3e-63e7-3f77-9deb-8170b00807e7 | -5.51336 | -46.41915 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d78219c-40f2-3085-b211-b318934a0441 | -2.07475 | -48.86114 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe2566e8-fb6d-3960-ace0-17d1a99a8905 | -1.91261 | -48.66652 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5ed967f-1316-3080-ac96-304e1e80a965 | -3.71767 | -51.84245 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc717a0a-1088-3b60-9440-64d07cd5bd9b | -1.31939 | -50.64247 | 2024-11-17 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c32270dc-e2a7-3c17-9d5e-285639fb32bc | -3.11182 | -45.98779 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb1c95eb-299b-37ce-9d64-cd30325629c4 | -1.13781 | -51.69233 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44662cfd-109f-3a1a-85a6-58a734c06529 | -1.37297 | -47.25833 | 2024-11-17 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9fc137-ad67-3e2e-bae1-726549e1711e | -6.9354 | -42.81463 | 2024-11-17 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e23bd0f8-13d1-3a94-bcb1-ac6033bad1a0 | -3.81078 | -46.51172 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c923f07a-8542-353a-bfc2-9640a5587bd6 | -0.09801 | -51.44202 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065a21da-5953-3408-9d26-e102bbf47582 | -4.53753 | -45.25604 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6420fbba-9d6f-393b-8f56-89281513b5eb | -2.03504 | -49.00042 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9936a86a-0545-35cf-b55d-10978a7ca077 | -3.32741 | -50.50044 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ecce871-7ae8-3f9e-a395-0bce3991beb7 | -3.53668 | -50.45776 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d25e32f-19f0-3194-9c41-62ffe77754d2 | -2.13095 | -46.52215 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76ff94c-6023-3077-96d0-462b9ae93c2e | -5.33912 | -44.99474 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 683eb9b7-d21f-3ca9-b837-87b2171c2608 | -3.93802 | -49.99122 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ea3e1b-c124-372c-9289-3077b6fa8e0d | -2.90509 | -46.85082 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7607b8bc-ff6e-32b9-b533-7a1c22d870b8 | -6.94655 | -42.82333 | 2024-11-17 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| df4f17ad-bc09-3a2f-99ff-83b0cb638abd | -2.64994 | -46.20303 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5107be69-2531-3740-9d1b-76f5094dfba4 | -2.00644 | -49.13544 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f8cd863-91d9-335b-8fd0-ada997c68fcf | -2.61078 | -46.25745 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 27f3221c-615e-33a3-9946-ea2ef67ae4d5 | -3.88242 | -46.64015 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f864a95f-82d4-375f-a6df-02a749b63fd8 | -4.29824 | -48.07912 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b89fa849-3527-3b5f-b33c-b1b2709b4c11 | -2.90232 | -48.30974 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc1ce341-9962-3d6e-aa81-be10fc8a52df | -2.34105 | -54.82544 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 105d6b14-bbd4-3659-b7b5-0f09a49eec98 | -1.2079 | -51.77253 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df87c346-616f-36e5-9601-893d1aaf0e9d | -2.62045 | -48.5624 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f14ef0-1781-3fae-9414-11376772f949 | -2.8464 | -46.66199 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c658dc7-5b71-3ef3-a752-a9ad67e00218 | -2.40664 | -48.47432 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b98da5bb-f850-35cd-ba12-da8c31d4c784 | -2.2347 | -46.85827 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a355552e-8f34-3914-af5f-5d7ec70b7028 | -2.175 | -48.55705 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a988027d-7155-3099-883c-2667be9ca8a7 | -2.82548 | -46.6658 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb051071-38e4-3f42-bf33-914d644a40c2 | -1.13435 | -51.68816 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 660f98a3-bb7f-38d7-a715-ad85c1548cc5 | -1.99652 | -46.57866 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a1c5e17-5252-3ce0-8c57-cdbff2dc1545 | -2.39696 | -49.04063 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 659e10c3-1c99-33ec-8c1d-6a3c2fee1f21 | -2.63309 | -46.82968 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 817a28cb-f936-32ad-b9c1-17e289405e7f | -6.38365 | -45.68337 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c50f4de8-0223-30c6-8c54-58737a3ac79f | -3.62919 | -50.2261 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e57088bf-59c4-3858-8a83-e029e88ec908 | -3.61584 | -50.14885 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fa6fcb9-c367-3118-807e-47ba356f289a | -1.671 | -47.97624 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8281fa1b-c224-32b5-9478-b5fb97c062e1 | -2.18646 | -48.2639 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 526bed64-7b7f-305c-bc49-d323a50141f0 | -2.63397 | -48.56454 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d7d1c40-368c-340a-a5c1-d0dc31dcde7b | -2.61246 | -54.32842 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0537cfa-8199-3dd2-a813-7277883804c0 | -2.60289 | -47.56108 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73cfbcaa-358d-3d6a-a6a1-85a15b552040 | -2.14959 | -48.5419 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74918162-c56a-30b5-b5bc-d0a246164355 | -2.27835 | -48.41382 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42cc490e-dc3a-37ce-8ebf-e5d6445a5cc3 | -5.34889 | -46.07887 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 964351df-5fa5-3c85-9bae-7286b6a726d6 | -3.61162 | -50.15236 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e77b474-a050-3268-9f27-56db86e991c7 | -4.16966 | -48.71915 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 30487d4b-e52b-3da0-a850-2603e71c4c8a | -1.10934 | -51.91949 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fccec328-397f-3b58-9dcd-4aed53a3fd09 | -5.17773 | -46.17035 | 2024-11-17 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84e6c844-baac-3ca6-bf6c-6fd725ba9605 | -1.08699 | -48.21118 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7827cb12-7da3-3e76-8966-e302980d787a | -0.94036 | -51.72635 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e04a3d-3cee-3752-a4ad-5cfeddb092d7 | -2.67477 | -46.21786 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 583856c4-dd05-3c06-8911-4f5920a53504 | -3.41273 | -45.86429 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
