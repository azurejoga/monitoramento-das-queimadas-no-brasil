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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe61cce6-f8aa-3d76-afff-d6e176f84660 | 3.26481 | -60.08107 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d0e3f7-ec50-3f50-a61b-7825ba0c9654 | -1.51355 | -45.90269 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd014e86-b1c2-3f19-9618-b5a4e68e58d1 | -1.18849 | -51.77324 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4dd71ff-8036-3142-ae81-4dd864febeb0 | -1.18613 | -51.76303 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf15169e-c7f0-300f-a08e-412bac3bed4b | -1.26945 | -51.82211 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd2ebbfc-c0ab-3c17-83ee-090d9947a14c | -1.27782 | -47.9053 | 2024-12-01 05:05:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fbde192-5e90-368d-9f7a-f4909512a474 | -1.07476 | -53.64292 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bda0ff7b-222a-3aae-a67d-dd228c498fc0 | -0.84585 | -48.53621 | 2024-12-01 05:05:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ad0a57-ce0d-31a2-852d-65bf294d8918 | -1.02663 | -53.55254 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ff0ffa8-c2e0-3fad-8266-d062500a3e21 | -1.26506 | -51.74775 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4ff1d05-4c97-31d5-8cb2-ceb9d3520b10 | -0.99661 | -53.69867 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d8693cd-c186-3498-bbf8-879efbbab0ac | 0.94365 | -50.75069 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dcc50fd-3a6a-366d-a23e-1ef31daffdf5 | -2.10068 | -47.62685 | 2024-12-01 05:05:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd03026-63ad-3657-b3a3-ec57cb6ec888 | 1.16074 | -55.97075 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a33158f-66f0-328c-a13d-090de626f527 | 1.17935 | -56.00307 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e51ea3fc-2bb0-3cfb-940f-e83929747769 | -1.14837 | -53.67439 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8346feb7-367d-3dbf-a96a-2c64876ec88e | -1.14611 | -53.66608 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b845f8d0-e41d-3da7-97f5-567a96953a09 | -1.24863 | -51.74305 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88f18931-73c8-3960-b856-31c19b448b19 | 2.73806 | -60.39391 | 2024-12-01 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f3f81fb-4910-30ea-858e-78271909ca48 | -1.18999 | -51.76363 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea08c438-c34f-34ff-8cb5-e88cca70fc44 | -1.17646 | -53.38231 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22498ff7-4830-38b1-9be5-8f9f166d9ed8 | -1.12707 | -53.19074 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f80555c5-b4e0-389c-a085-00a4305442c0 | 0.95579 | -50.22115 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56a4ff8-48f8-38b0-9292-a3f62140a597 | -0.58693 | -51.68731 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a0b4d37-317c-3bc7-98fa-25f8d1405812 | -1.25072 | -51.78984 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de567ab2-b525-36db-8859-8e06f144fa4d | -2.28821 | -45.59971 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 95d052a3-1706-3337-beb4-367427c0b8e5 | -1.07318 | -53.23209 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfb805af-0bf9-372a-8fd2-3539530c293f | -0.6008 | -51.69912 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d0412e50-8898-3e13-8c02-7cc14ccc5932 | -1.51818 | -45.90686 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf7ba42-b097-3dfd-bf03-bcf471167d69 | -0.72331 | -51.69772 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82e68a91-9809-3663-b8b5-33e11e2ab2be | -1.20608 | -51.73654 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44841707-7a1a-3666-89f9-6c67218d5338 | -0.61411 | -51.70257 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5324afbf-5a9d-3248-b8e5-1010beb5b55a | -1.18463 | -51.77265 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c2f39a1-72a8-376f-bb52-d15f13be169b | -1.09473 | -53.60628 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e00ad1-c222-32c1-9866-eaf4128ecc81 | -1.29172 | -51.36984 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f14affc1-75ca-37ca-8b72-9979c0cd9944 | -0.82331 | -51.61467 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3db4fbb7-a8bb-3f02-8a84-d2d785971c2c | -0.95838 | -51.65509 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db3442ed-6b8f-343c-8ae3-17d21d730f44 | -2.12208 | -46.58172 | 2024-12-01 05:05:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1abefacb-61a4-3875-9674-73d8ad141ea7 | -0.94931 | -53.21428 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9420e78c-027b-3423-acad-3d98753bbbdc | -1.09663 | -53.19866 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37bd442e-4f8d-389b-8ac7-f366a3d02709 | 1.19608 | -55.9371 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65fc04c0-5cf7-3a4a-b2a1-9b62e807096b | -1.1744 | -53.41841 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ba94489-7856-3d0e-b8bd-c73046902c46 | -1.27256 | -51.82747 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db5c4916-a3b8-3543-81e5-b7c3ee4f87b5 | -1.14262 | -53.66556 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6fb81f9-c74b-336d-af82-ba39e5e3d30f | -1.40835 | -46.6011 | 2024-12-01 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d223f52-abd8-3706-9905-ac64e0153a55 | -1.70785 | -46.14943 | 2024-12-01 05:05:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18640733-b98a-38d5-8fab-d9564a672ca7 | -1.51243 | -45.9059 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fbc82bf-d8d4-32e2-bc06-88b3d5ec2540 | -1.08061 | -53.39238 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a304aab1-65c7-3c0b-822b-e167b62f3547 | -1.05122 | -51.75521 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8961060f-b5f3-3f51-a4d2-dd99777ef61f | -1.0893 | -53.64126 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8e92517-520a-320a-be84-33ccec9b8a66 | -0.95523 | -52.98704 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9d59eb3-6f3d-30dc-81e8-3453457245c6 | -0.963 | -51.65084 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebce9bef-6cd1-3ec6-85d3-a1dba7319bb0 | -1.07998 | -53.39637 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52a5485e-8b22-3f2e-8ecb-d49b492511e4 | -0.76288 | -52.41608 | 2024-12-01 05:05:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a233e60e-f283-3c93-98fd-56d6b6583078 | -0.87268 | -53.68353 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15b79a86-f22d-3ebc-9932-8c3b17464120 | -0.60156 | -51.69437 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d7bad79e-2c8c-35f2-ac20-b0ad514eccd0 | -1.00203 | -51.73077 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0698c6d9-22de-34f6-89e6-5a14e31310c1 | -0.96612 | -51.65629 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| decd6b69-e3ef-32be-8be0-c14e78b5b923 | 0.93748 | -50.73751 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 040d3a0b-a548-3432-8124-7563706e81d0 | -1.23696 | -51.80244 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24c34ff3-4208-3428-a921-ed35ae876522 | 0.94044 | -50.20456 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d70dd0d-fbde-3d96-96f5-da5320959bbd | 0.85767 | -59.45449 | 2024-12-01 05:05:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7fd5aff-7c77-39a8-858e-fc68d97b9ec6 | -0.60257 | -51.70078 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8088f2b6-9e59-3cea-a340-a146ef04163d | -1.09976 | -53.36275 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d800a6fe-c4db-3e2b-a735-d95f2d8e88ca | 1.17658 | -56.00702 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be057c64-59aa-3dd0-b5f9-73d19e4acdfd | 0.98503 | -50.12463 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfb3d5a3-f818-365c-a36b-b21c17d6daae | -1.06422 | -53.38179 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cc1484e-32f4-39ef-914b-1a2b45d5e2df | -1.14768 | -51.67803 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c2a8279-2232-34ca-b60c-1cda048b753f | -1.31375 | -51.74041 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dba9a5e6-19f9-326a-8a89-80aec17911e4 | -1.03013 | -53.55306 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3038d218-d878-33fa-9293-48066649b79d | -1.23311 | -51.80185 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca8bdadc-6549-38c2-8f4a-107997685b9f | -1.0105 | -51.72717 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bdea4c21-e343-3c0e-85d0-d44f2faa90f2 | -1.17087 | -53.41787 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07b966a6-5759-3f52-aa13-af68af818f55 | -1.05072 | -53.21273 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ef7ba38-ad4c-3eb6-b5df-72266fae5ed3 | -1.01436 | -51.72777 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ef34f30-4bb7-3f7f-b99c-2d2c769cbb2d | -1.20994 | -51.73714 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d8760c1-bbfe-3b2b-8a59-dcd9f74f3ce4 | 0.78077 | -59.75888 | 2024-12-01 05:05:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef2b97b-7773-38a6-8533-4ed78dd4dddc | -1.09471 | -53.39455 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9be1a2cc-4f16-366f-910f-a737644b0e5c | -1.54929 | -47.1608 | 2024-12-01 05:05:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf962004-cfc7-34f3-8105-97e1e51fca42 | -1.32283 | -51.68218 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f531080-609a-3bce-812a-f15b981369ba | 1.14986 | -55.98956 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 683d263f-cdf5-3006-b923-22aa52e9bd68 | 3.28275 | -60.064 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0e40381-5dea-391e-a333-d7c8629ee94d | 0.98877 | -50.2426 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d8b708a4-393b-3187-85d7-b4f7bf61c50b | -1.09928 | -53.39056 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8b737ca-2512-367a-ab1b-e8ea6a60c781 | -2.28757 | -45.60407 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 70b98ac3-bdf1-3870-b676-db612c6baeba | 1.14932 | -55.98612 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc6075bc-6f83-33fd-b869-03734306febf | 0.99339 | -50.27217 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f71a8ca4-7c8b-3490-a421-36049af86aba | -1.27991 | -51.65064 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1c5898d-e50c-3683-b5c7-0d46c63f5981 | -1.40839 | -46.5998 | 2024-12-01 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fb96919-8436-3dc6-8f17-1df194197f0a | -1.15449 | -51.70216 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7159667-d83d-368d-9f3d-b5fb04fc7487 | -1.07657 | -53.63121 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ed9c0b8-44c2-34f4-a66a-a594c0fd9f01 | -1.00278 | -51.72599 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90a0bbf3-135e-328a-9e1e-9b2c89439b8c | -1.20146 | -51.74076 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a108e633-eabe-3eb5-bf42-760dbc1b764e | -1.32198 | -51.66206 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6a3dc65-b8f0-32c5-9775-4f228270e400 | -1.28202 | -51.74049 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f23a0269-27a0-367b-af6c-9fb7f66ffd19 | -1.10911 | -53.42048 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3653c5f2-6f0c-3331-ba22-983cca0b9032 | -1.19684 | -51.74498 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1088ceac-3731-38cb-a920-2ecae9bb86ca | -1.36127 | -51.85348 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a069936b-127b-3805-80c1-bd69ecc0b81b | 3.27928 | -60.06816 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8cb8da4-8533-3706-aa9a-cca5d2f904fc | -1.29569 | -51.37045 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README75.md)
