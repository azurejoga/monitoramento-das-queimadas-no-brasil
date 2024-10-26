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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 724587a7-bc6e-3108-a98a-6e153eb708aa | -4.08065 | -45.56869 | 2024-10-26 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0c198c-99f5-30b8-ba97-d131d23f429e | -4.08012 | -45.57217 | 2024-10-26 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 654a9978-c423-39b8-929d-5d4f6975b8e0 | -3.60564 | -45.81371 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 22027a6c-327f-3391-8caa-f5312010203f | -2.03757 | -46.96948 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| df783802-10af-3261-9138-f538f6d2a040 | -2.03692 | -46.97358 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc075464-a325-3565-a2fd-63caf7e95892 | -2.03587 | -46.96793 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c69f6624-459e-3d0a-9cdc-4a0ed0a0d3a5 | -2.03525 | -46.97202 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6cac720b-63b8-34ae-b2c2-43daa5625704 | -2.03398 | -46.96892 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 856f3ec1-c8c3-3c38-89ea-4d4f6211c74c | -2.03333 | -46.97301 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3f2d8e44-7ce7-3158-b00d-4fa20827a0ae | -2.03165 | -46.97146 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 441918cb-a7ee-3fea-a8df-77bdfbfde4f7 | -2.19423 | -46.32649 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 774ef1a0-dd4a-340a-8daf-fc1dc3a0f6d3 | -2.05704 | -46.53674 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4467512-34bb-33ab-8a98-687ec728c367 | -2.01027 | -46.54722 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3c28d10-54b9-3bfb-a2fb-beb64e4357d5 | -2.00961 | -46.55153 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 868ebc5e-6257-37d0-9ed9-0a1bdd081359 | -2.00594 | -46.55096 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa5999e1-3a72-3318-9ce1-9c133f8672e8 | -1.95967 | -46.6329 | 2024-10-26 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39fd491e-ca6f-3f71-b235-9ebaef0b68e6 | -1.95601 | -46.63235 | 2024-10-26 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 656e4ce3-556f-3da7-87ac-85f1e5e8c724 | -1.77855 | -46.30696 | 2024-10-26 04:42:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52e9e75-f745-3a3c-a6b7-30360eec1dc5 | -1.17412 | -46.72498 | 2024-10-26 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c88a41d4-8e6e-3703-960c-9ce4261fae8a | -1.11308 | -46.83332 | 2024-10-26 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d1552e5-59f9-38cb-833b-54e77d2fe436 | -3.29878 | -47.02201 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3a31c3b-9ddd-3c1d-8619-512a77d8c65d | -2.95615 | -47.36095 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2732926a-8aef-337e-8633-d8efa04a758a | -2.6556 | -47.3636 | 2024-10-26 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee4fcd19-f6a4-3bf6-98ab-bb6048ed320f | -2.57083 | -47.25706 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 139e2b36-ccc9-36fe-a733-8a038ae427d5 | -2.56726 | -47.25653 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5519ac53-114c-3393-bfad-d4080a9d5d49 | -2.48515 | -47.27352 | 2024-10-26 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94886f28-7c7a-3a50-ab65-36a297b6a1b1 | -2.15558 | -46.94319 | 2024-10-26 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17f76e62-3429-38bc-9ec4-95a2c6e1967e | -3.54432 | -46.41179 | 2024-10-26 04:42:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71278b6c-b793-38d1-87f3-ceb90ba478d5 | -3.33251 | -46.27634 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93135aea-6f92-3785-939a-6121191b3889 | -3.33248 | -46.27831 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83c00249-668c-3347-8870-fdf2bc5b8a7d | -3.1891 | -46.17801 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfc9cad7-8a02-3bd8-b52a-d6a5d5acbc41 | -3.18838 | -46.18267 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f45011-14e1-331b-959a-8e478f92f516 | -2.72438 | -46.69304 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a67675-ca21-3668-84f4-bb1e3c529189 | -2.72188 | -46.68992 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4db912-dfbd-3c4d-a1f8-51d8e7a50862 | -2.7212 | -46.69423 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fb84914-242a-3d14-bee9-9e37636b6b34 | -2.58741 | -46.13884 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39928a8b-dc39-3feb-bf26-9adab9b0bec5 | -2.37818 | -46.16357 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b46433-ec2c-3fb3-b70e-569ec69c812c | -2.37801 | -46.16595 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf1d606f-4790-3a66-8234-b7c73958f7ed | -2.32023 | -46.64718 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4ac6f0-ef12-3d17-8ba2-b75b552c0ecb | -2.31892 | -46.65576 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b3ca6a0-9407-32eb-9dbf-c160d96232ab | -2.31721 | -46.64233 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc5081a6-8ebf-30d5-98a0-4faccac7257d | -2.31656 | -46.64662 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4358d0b1-78b5-3da9-82ac-6fbabe486174 | -2.31591 | -46.65092 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a4e604-745a-37df-922a-ba927e23764f | -2.31525 | -46.65522 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be814238-a41d-3d53-ade3-2e082f537508 | -2.31486 | -46.63312 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e61691e-df68-3c9e-8cef-4e4e073ac5dd | -2.31355 | -46.64176 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef034e8-a449-34af-a6bd-cdc6b9059464 | -2.31185 | -46.62822 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3711163e-0478-3401-a157-fe66844ae52a | -2.31158 | -46.65467 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94f2f804-d39b-3c5c-ab3f-0ea59f0a4e62 | -2.31119 | -46.63255 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfc36ac2-a48d-33ec-bdc0-a433a91f4358 | -2.31053 | -46.63688 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224c6603-7686-3617-8ada-ee0b12a0214d | -2.30792 | -46.65412 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17f8252a-94ff-38b1-a284-6a80142d0bc8 | -2.3049 | -46.64927 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b21a3572-bf6e-301d-8375-a44bddaabf6c | -2.29775 | -46.6499 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a77244d4-e7d6-3c10-b179-8febe29b9133 | -2.29757 | -46.64815 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abd78045-d081-3056-8c67-7429bed8cedc | -2.28569 | -46.7513 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13baf331-0a62-3a00-853d-407dc160d08d | -2.28527 | -46.75284 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123f34f0-a512-3456-85fe-565324b28470 | -2.2814 | -46.75499 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e82737-e640-399d-841f-ba582d244fa5 | -2.28132 | -46.73048 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ee84ac2-c309-3143-ad33-9e84f49f215e | -2.28095 | -46.75652 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9325cbc6-d7ae-3597-855e-60b1822b7b0d | -2.27767 | -46.72991 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 955b1cec-9d97-3cfc-b3c3-c22ad2beec58 | -2.26971 | -46.73306 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b74c3c8-aff4-3cf2-856d-864f4db14ab2 | -2.21746 | -46.78133 | 2024-10-26 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d929af2-0a4e-321e-8920-c87c3670b9ab | -2.19395 | -46.42631 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 657421de-9c15-39a2-af82-af904a16cc00 | -2.19093 | -46.42133 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40854685-cef3-3400-943f-906a126fbac2 | -2.19025 | -46.42573 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 249593a4-1558-3b3e-b852-ed736a98b747 | -2.18723 | -46.42075 | 2024-10-26 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60c23777-22b5-326b-ac5b-9ad9713f0b40 | -3.81687 | -46.93537 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95fd1473-001e-3cf2-88e9-a5e6ce5cf61c | -3.81319 | -46.93484 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e610f3-9c01-3b44-98a1-12b58470fb19 | -3.81015 | -46.93002 | 2024-10-26 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7678cf9b-f174-3d1e-9e5f-86d3e1eeb6e0 | -3.77497 | -47.54419 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e95bb010-66da-3605-9832-cd027e2edbe8 | -3.60921 | -47.26172 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c662280b-3006-3ff5-b985-5e237c4e074a | -3.60559 | -47.26125 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22458d74-e1cc-3903-8de6-d5708aae7ac8 | -3.60495 | -47.26537 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78378148-7bab-3dc2-8b7e-b663d93147d4 | -3.60431 | -47.26944 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7834a14-4402-3286-b0fa-d5e35a4c5285 | -3.6007 | -47.26895 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0b82da6-9d31-3ad9-a81f-587c72740eba | -3.59709 | -47.26843 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8ddfb2-82d4-3eb0-ab91-0beb33c133f8 | -3.59645 | -47.27258 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5143feda-ed20-3a1f-ae0c-abda17b14183 | -3.59349 | -47.26788 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437dc240-efaf-367b-adac-8ec8aa749831 | -3.5501 | -47.35824 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eddaf12f-9039-3541-9fe8-c167d4533f1b | -3.54652 | -47.35769 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8567bd77-b060-3c70-95d7-840fa7c9d942 | -3.5459 | -47.3617 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e87df2b-501c-3c80-9f9c-d43a1958ad57 | -4.18556 | -46.87447 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 433f9c23-2e2c-3130-9bcc-a8d68ccbbd0f | -4.15013 | -46.83292 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25535237-c722-3736-8931-7d4fe8b63e59 | -4.14642 | -46.83234 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03c9e059-676c-3e50-b4bc-6933d8b3bb29 | -4.14272 | -46.83169 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e588d4-d861-3a2d-a560-c214e39249cf | -4.18574 | -46.62239 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5484777-2f96-3327-9e26-dc9f69564733 | -3.96149 | -46.41525 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4956607e-ddc3-352d-ad09-6665c330f801 | -3.96145 | -46.41728 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d096cb3d-6ca1-36f4-827b-07ffdc3f7ff7 | -3.95496 | -46.43312 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7824b000-6029-3e59-b53d-c6d6e6980730 | -3.95173 | -46.42992 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4742dfcf-8927-3682-9880-8ffecfda16f6 | -3.95099 | -46.43466 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aefaf1d1-580a-39d8-8be5-43d9142a80e3 | -3.91759 | -46.42487 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abce4dfc-feba-3bcb-9a58-a3ad9ebfca42 | -3.87171 | -46.4463 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63833e6-c1db-35fc-b387-fc3d91b53450 | -3.82491 | -46.47445 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66e034cc-dbc3-3ec6-b12d-c5c1335165f6 | -3.87548 | -46.44699 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcf793e-0e6d-3cfe-bf32-f71df8db5e3e | -3.25598 | -50.05906 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a08365f-c97a-34fc-8112-0b7a7d649388 | -2.10042 | -48.37055 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a57816-a6bd-3149-b47e-5b185707eed8 | -2.052 | -48.67996 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8743025-2281-3b5b-8dc4-f4cef13f6de0 | -1.98065 | -48.68374 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5234cd83-5360-3f02-87a7-139b751c4cef | -1.0225 | -48.06927 | 2024-10-26 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README64.md)
