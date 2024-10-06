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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59dcd3bb-9f4c-3c38-abe5-eab4ca0da638 | -4.82389 | -46.80154 | 2024-10-06 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a2227af-faeb-37d7-b9c8-f27fc516cb00 | -4.45323 | -47.46579 | 2024-10-06 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b60a865a-573a-3900-a75e-558ca9d70ed5 | -4.31649 | -47.70549 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfa71c8b-4935-3166-abed-d14648bff9a7 | -4.18626 | -46.85398 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d765140-66fa-3564-afac-fc143f3bdb94 | -4.18058 | -46.8533 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 545a3337-6e69-3905-a5f2-7e4cab2c6b3f | -3.85584 | -46.46227 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b975306-0dd3-3779-9ed8-07a711f76999 | -3.85526 | -46.46626 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3fdac185-ac02-3afe-a56a-f66332b56dae | -3.85007 | -46.46144 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10ec1ef4-f613-3ba5-b515-a62d56ec6c31 | -3.84946 | -46.4656 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 627d97b9-6bd8-3f93-9a08-2d63ea6ab76c | -3.84887 | -46.46957 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23d85a50-1480-3603-9859-c1ec354ad50f | -3.84426 | -46.46081 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 42790c2b-ca2e-317b-9a49-38189eaecafb | -3.84366 | -46.46493 | 2024-10-06 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| dd9dd557-83fd-3f82-967d-521cc25c7bb4 | -3.62007 | -47.51629 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 989bcdff-d90a-35a5-9829-76efd1466e5e | -3.61813 | -47.51464 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d758d89-91b2-31eb-be12-711c1c65b501 | -3.61764 | -47.51805 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea95f025-4da9-3a4b-b777-f12f104e8a24 | -3.61471 | -47.51545 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6626da1-97b1-306f-853f-ceb0fdb1a4c8 | -3.6142 | -47.51884 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a20a12-3e83-3f31-bae5-0741dd8498a5 | -3.61229 | -47.51719 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 676819b7-853a-3acd-8bc7-0d3047454fd0 | -3.60885 | -47.51799 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 999ed8f4-ca66-3dbc-b901-e820a0b01990 | -4.45922 | -47.46287 | 2024-10-06 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22cfd67c-4e4a-3cf5-920e-a2fddbb4180d | -4.4587 | -47.46648 | 2024-10-06 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 733ccceb-8ca4-3368-86fe-99be2bc45e02 | -4.31599 | -47.70893 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1420129-a229-3ab1-8bf8-f8bdaffdb9a5 | -3.77634 | -47.61566 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47fc9848-ff12-325b-a8e7-dd822e81cdd4 | -5.71719 | -47.15034 | 2024-10-06 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6af3de8e-afc6-3f42-b2f8-bbbf0f56fe58 | -6.41577 | -47.70394 | 2024-10-06 05:10:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d36150e-5f88-373e-91e0-d476096b0fb2 | -6.41527 | -47.70755 | 2024-10-06 05:10:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 180fbc62-1bf4-3904-bc33-f642c58f5357 | -5.71426 | -47.14977 | 2024-10-06 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 49124f1d-46de-394a-98dd-e26611eb12ba | -5.71151 | -47.1496 | 2024-10-06 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39212e51-c18e-3abe-9d13-37f6db3dfb44 | -5.71097 | -47.15337 | 2024-10-06 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aceb2137-e444-36e0-90cc-f34fae8221f8 | -5.37596 | -47.72104 | 2024-10-06 05:10:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 85f1b0ea-c715-348f-a272-111730566cb4 | -5.37547 | -47.72453 | 2024-10-06 05:10:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f10c044b-acea-3b03-b240-31fe36395099 | -1.69983 | -47.595 | 2024-10-06 05:10:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af18fdd-8b93-3129-9ce8-9df62c06e197 | -1.69936 | -47.59815 | 2024-10-06 05:10:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a932cfe5-2c2f-354a-8c58-8465323213d3 | -3.13699 | -48.60661 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79a5c832-3270-3330-8fc9-19f3a93ee303 | -3.13424 | -48.60096 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8c1c008c-6d77-3083-bd8f-9a045bb9fec5 | -3.13374 | -48.59479 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ed037d1-2ec0-3e2e-a81c-5d5e59f30bb3 | -3.13344 | -48.60649 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06c1fa7e-941a-319d-8e90-5780802c1e32 | -3.1329 | -48.60033 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebe83a43-f3c8-382f-9780-699732bac6c4 | -3.13205 | -48.60585 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbefe532-51e8-3671-bc7a-d30bee881ad0 | -3.13119 | -48.96163 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de6a0639-5380-3338-acd3-fbbea1d25a47 | -3.13036 | -48.61694 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1195af9-69a0-3bc6-826f-505812807b1b | -3.1301 | -48.59465 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a00fcfc8-fcc4-3221-9307-85b4f8d49432 | -3.12951 | -48.62252 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df2a42d4-6b66-3b3b-be05-1f0b9610f1d5 | -3.12795 | -48.5996 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fcf04d2-be0f-3242-a7c3-f640130629a1 | -3.12609 | -48.62242 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8e7b9fa-c4c2-365d-af76-1674586d531d | -3.12301 | -48.59884 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f478939-f079-3c09-bb37-73d8d2fdccca | -3.12116 | -48.62164 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8d5c70b-d654-3c26-9be2-4f656a262ad2 | -3.11879 | -48.62658 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce2dc154-0213-361f-89e3-6f004421e09e | -2.81851 | -48.60587 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f6616df0-6f6b-3a7d-8e00-8b1c33ad301c | -2.81653 | -48.60018 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 29230a2c-44ab-3cf0-894a-cd697f47bbe3 | -2.81359 | -48.60513 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d29460f8-82d5-3400-b8d6-f1153f1448b5 | -2.81185 | -48.70058 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8030d21f-2f9b-3d12-84cc-7853dc4ebf40 | -2.80903 | -48.69975 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 56d86ebb-797b-377c-9d44-086a355626e0 | -2.80857 | -48.6889 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c1ed6dc2-ec0f-356e-8ab4-b87e0878c445 | -2.80697 | -48.69982 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81bcbdec-4fa6-3d18-8bc7-c6c7a5e5f44f | -2.80498 | -48.69357 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 045e68d8-1c3a-3910-8048-69f74ada8d06 | -2.74068 | -48.68916 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31f3b5d1-4903-322c-89ef-d2cd70384879 | -3.69968 | -47.61784 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d8609d8-e6cf-3ba9-8ca2-9ec155dde624 | -3.6992 | -47.62122 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 139e896f-dd82-3b49-94a9-8bb8ae710ec2 | -3.69569 | -47.61985 | 2024-10-06 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f3c06f5-f79c-3c04-8aaa-36342b5a4636 | -3.49837 | -48.90167 | 2024-10-06 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f6e75fe-cbd0-39df-99af-17a63776a44c | -3.49349 | -48.90098 | 2024-10-06 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5578052-5836-319e-beee-ebb034c4a21a | -3.46347 | -47.66321 | 2024-10-06 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 90d57822-7925-3411-b2c4-405b3c1fdb8e | -3.46297 | -47.66652 | 2024-10-06 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9401fcb-02ad-3034-bf7f-4fe15497e40d | -3.21785 | -48.97173 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8ffcfad3-a34b-3265-8c5e-419e5fd8641a | -3.13784 | -48.60107 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26fb1e8d-47dd-35bc-a06a-0c40929fed1b | -3.13614 | -48.61218 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2222a4f4-bf35-3fab-bbb1-a0f10bd2b89d | -3.13264 | -48.61205 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bb19efd4-c4f4-3197-b28b-de0a9c66fb19 | -3.13121 | -48.61139 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4faa8c6c-22a3-3774-9c92-d45965304b0f | -3.1293 | -48.6002 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a275772-7cd4-353c-9847-2114f12c4381 | -3.1288 | -48.59404 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c171dc-c291-3fc3-9dbb-108dafd732d5 | -3.1285 | -48.60573 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b66eec1-6934-362e-96d5-5a61de946484 | -3.1277 | -48.61127 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8c8fe25c-7b67-3df1-9431-1f6849d1d65f | -3.12711 | -48.60511 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 69e821d6-c4e4-31fe-96d7-84ab43b9ecc7 | -3.1269 | -48.61684 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fca80931-a44c-3a26-a8ec-381db8143739 | -3.12627 | -48.61065 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 925c23f5-4598-3a12-8367-18b5f343d1d3 | -3.12542 | -48.61619 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39615a6f-f0e5-3bcb-8bb0-1b43038a09e3 | -3.12527 | -48.62809 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d47edd8-4680-321e-9b0d-1c673e402d06 | -3.12516 | -48.59387 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c271dae9-927e-3516-b1b9-3581ac4dda89 | -3.12458 | -48.62175 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b177919-118f-3856-a414-54a3f9581add | -3.12436 | -48.59944 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3d7c340b-c47f-3672-81ed-7126f44108e9 | -3.12386 | -48.59327 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8bd0518-c75a-31e7-b34b-b7e59f750854 | -3.12372 | -48.62738 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f328006-f8ad-3739-a238-4610ae4c12d2 | -3.12356 | -48.605 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a4c762be-03b0-3652-9084-73140157af80 | -3.12275 | -48.61056 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 987a0a8c-e28e-342e-ae47-a10ede4cbc65 | -3.12217 | -48.60437 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| fbe86e5d-07b8-3a42-9832-7c3ee1b4cce9 | -3.12195 | -48.6161 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 06abc22f-9d2e-3412-976f-31545d16c5bd | -3.12132 | -48.60993 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 907edee7-0034-3916-9b4f-114fdf8c2e8a | -3.12048 | -48.61544 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca92284e-b8ce-33a9-b1b4-969dd7d21cf3 | -3.12035 | -48.62728 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70e7bce6-74f4-37ec-8ed5-0b21816ee1d8 | -3.12022 | -48.59311 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0ac5b0e-6752-3074-ba68-5b1e64a496f5 | -3.11964 | -48.62099 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc291691-ba9f-37f3-b42b-cd974bbc4d69 | -3.11941 | -48.59868 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8fb27994-ddba-3b3c-9417-5b32a6d3bb6c | -3.11891 | -48.59252 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86311412-3c6e-3b04-b8d0-7a3011cb5949 | -3.11862 | -48.60423 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f946e7d7-2ad1-340b-b416-99e5308cfe4f | -3.11807 | -48.59807 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24b59fb5-50d8-3553-9a91-74f1227990d3 | -3.11782 | -48.6098 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 8df09ee6-855a-3ada-8363-122e7f23c9a6 | -3.11723 | -48.60361 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bc3c746-264f-3bf8-aac3-c0fe1fb001ff | -3.11639 | -48.60917 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6712eb7f-e111-3464-83dd-a44ca9734f86 | -2.82146 | -48.60091 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README97.md)
