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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e40a93be-64ae-344d-b49f-9e4f50eb22ec | -2.45337 | -53.70742 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a552e919-f84e-3dea-bc24-fba850bf23f3 | -1.10999 | -53.39449 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85534949-c2cf-3100-a7d7-bf9670e283bd | -2.28726 | -47.31145 | 2024-11-24 05:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d7305a1-14c8-305f-92eb-ee63fd987a9d | 0.40876 | -50.85316 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 63b3e62a-13b0-3f64-9d9b-4b0d496ab1f1 | -2.45073 | -49.08741 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e1fb55d-d15e-3f65-aaff-fdd35c2b0a8d | -1.05138 | -53.15697 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b4907d7-f335-3e46-a3d3-c62f54d4aee2 | -2.17134 | -53.77988 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2e4651-b71a-3643-8b2d-a4950cf43893 | -1.4646 | -51.11636 | 2024-11-24 05:14:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4475fb6f-bbba-37b2-96db-d120f7382b27 | -2.85721 | -51.27313 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02bd1274-5bc9-31bf-8803-cb270d167375 | -3.17945 | -54.32349 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce187d0f-adcb-36c2-ab87-228961c6ae36 | -2.24658 | -53.46911 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2002e911-eda0-3e6d-b112-4e4f6fb63f93 | -3.36744 | -53.32583 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47d19982-f2b8-3b25-95db-7b89eae16135 | -0.95504 | -51.71628 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b004dc7-c091-3bd6-a598-90c3ca28c0c2 | -4.07995 | -46.82947 | 2024-11-24 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfbabc46-d635-366c-b13c-aab2d8e094b3 | -2.99922 | -51.38586 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870e7994-c2a2-36c2-aa79-87231bfb8482 | -2.82459 | -54.09782 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aef3ac22-2cea-363d-ae0d-b334b57ded19 | -1.14249 | -51.68259 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd2292c8-35c9-34d0-893c-0cb07e761a16 | -3.24121 | -54.22233 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be024174-435d-31ba-9642-233ff5ffc472 | -4.51612 | -45.72569 | 2024-11-24 05:14:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f311674-58b9-38fc-bce6-8877602546dc | -3.23296 | -54.22571 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e0c0f87-0ce9-3eff-811d-9c424ed3fb81 | -1.36418 | -53.83976 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16f3ff49-4cc0-3c4a-9de5-8c9b97461130 | -0.33218 | -51.55038 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac5d482b-b103-3035-8291-3ddd0939dc3f | -2.94923 | -51.43147 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f599dad-7ae5-3d68-8589-e1013afafd6c | -1.48424 | -52.51746 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5582d68-76a9-3c4e-8a95-29a55fd77180 | -2.74431 | -49.12135 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d550b4c-bf41-3c0c-87c1-55c2a1a4a69f | -3.27762 | -53.78163 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d94d2f-db78-340f-af99-1ec3f342488a | -3.48916 | -49.91526 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f3b278c-ac46-3542-b933-b1d0dd3cfb99 | -2.16992 | -53.78917 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f080b96-49f5-329b-b574-1d3fe622d725 | -4.07722 | -46.14987 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bae5b91a-d457-355c-a49b-22cc213b5fe5 | -2.47579 | -47.08475 | 2024-11-24 05:14:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20af86a4-dfba-3bf6-9ca5-bfd7ed5759ed | -1.61709 | -55.13618 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f83de31-c76c-39e3-ad04-0fa1679fed23 | -1.75254 | -54.51947 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35f21723-add5-3af7-aab7-f5290eeec49d | -2.56908 | -54.05313 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3bb47990-7db0-303d-8dcc-b9e5fc7f68e5 | -3.29534 | -50.36023 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3651012-9e17-3606-8a58-143dfbdb9d6d | -3.49718 | -49.93124 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58f82f2b-d95f-3bf6-84e6-15aae4c2f702 | -3.50392 | -50.46503 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba43e16-8c2d-3c07-a333-348c8613f68a | -2.68947 | -51.80436 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b7f82cd-65f7-3c22-870b-746e48f57068 | -1.11076 | -53.38961 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dc33b1c-25d0-3d51-a29b-74ac263cfa4e | -3.29942 | -50.36633 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 397d218a-5110-348b-9211-c31b56e17024 | -1.12851 | -53.40221 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f8dbb98-c869-3a10-abe2-b00992b1a5bf | -1.11923 | -53.38601 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 389ebf2a-801c-32b0-a360-d99510824cf4 | -2.88122 | -54.00017 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fdb9ee0-0bf6-3ca3-869b-e68fe0a3b946 | -2.54642 | -54.04948 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ec3c1a-d457-3a40-a3c4-ccba4adfcae1 | -3.18183 | -54.33308 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fee7f3d-04c2-3d7c-b513-a567f2dea60a | -3.73265 | -50.43697 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6320a47-6edc-3308-a456-f3531f076108 | -3.08068 | -54.5591 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4724ee1b-5ea8-3ecf-8187-59d74c80d2bb | -3.39307 | -50.32597 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 134c97af-2dcf-3431-aabf-abd3cfbd9a32 | -2.6347 | -51.89577 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22ba3cf1-caf4-303f-aad4-138181fa0784 | -2.87908 | -53.99783 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee0323ad-dcad-37a4-a0d7-8bee5476bd5d | -2.80868 | -54.02493 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52c58d12-04b9-3708-97f4-f26fd1b080f0 | -0.37335 | -51.55541 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06f7ec7a-be85-3ccc-9ae3-e3938e841303 | -3.3092 | -50.03308 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37660311-a25a-37e0-9ed7-111995ef2e48 | -1.51189 | -54.41198 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84df08fb-c7c1-341a-9c1b-ba45ae2eac7d | -3.04284 | -49.45673 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c6d75d1-8645-3dc3-b644-17a98efdf820 | -3.18626 | -54.32914 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52e13865-fded-3427-a1dc-956c797ada8d | -3.15624 | -49.89985 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 367ce6fd-3121-3bba-9973-6237f100c05c | -1.23797 | -51.79107 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba35d35-edc7-37ac-873c-00d63355bf85 | -2.82982 | -54.01395 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d206974-8123-3619-b580-f799b3621c35 | -2.44019 | -49.08578 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74336556-57a4-34b4-82f0-b3b62ecccca8 | -2.01315 | -51.1725 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccea1fdf-669d-39a0-a3b0-4ed1ee8d2077 | -1.94792 | -49.52176 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fffa35f-bed3-3fe3-87ed-f9fa335293db | -0.93107 | -53.20997 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66d1375f-3dba-3ecf-acd3-88971a2a21c6 | -1.60921 | -52.59531 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53698457-927e-3ebe-b6c1-01d7dcc324d9 | -1.61683 | -52.60017 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75c4152b-2a69-33b1-b972-2088e2048aa8 | -3.31993 | -53.28812 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 133ac599-ef79-3057-ac6c-1e7ba0f9c0c9 | -1.69217 | -55.02606 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00f5285f-4728-3481-aef4-bba52530bc42 | -1.44872 | -53.40405 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f4c407b6-afc2-3417-91a7-2426f907db9d | -1.36562 | -53.83063 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbe2f265-96bc-38d1-b32e-ef313924be24 | -2.41115 | -51.97707 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24982da5-5517-3a78-9edd-d77e62dd76fb | -1.21971 | -51.7388 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34f8b27d-5777-3491-bcd6-9c63e9eb643b | -1.44597 | -53.40055 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 040c4bfb-0a90-3e72-bf9d-e5f832bc304e | -3.07396 | -54.55357 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ba6a16-6989-35dd-b52f-8c536b4d7329 | -2.69449 | -51.80079 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b472b5a-104f-3591-a4c1-aed1e1cf9ebd | -3.28251 | -50.04062 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7936023d-b6a5-3191-af66-f5a2fbefc1f5 | -2.6419 | -46.85543 | 2024-11-24 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23411470-eab1-3ff8-b1b4-f9a7597649a7 | -2.62419 | -54.93542 | 2024-11-24 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18aa2b43-003f-3e8b-b6d4-7cacc1de9258 | -3.27631 | -53.8162 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c1e0dd7-5c23-345c-ba3e-f1ed7757e056 | -3.12319 | -53.10779 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c87944b2-822c-36de-860e-197a498d4f65 | -0.2467 | -51.61921 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd808958-336e-3481-8893-d32ac898ba86 | -1.61551 | -52.5815 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b1436a5-996f-3fc1-9eb9-6207589ca35d | -3.47601 | -51.9943 | 2024-11-24 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 122d1b10-9857-3c4c-ae35-e0d30ea16c51 | -3.05992 | -53.21975 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e143fcd4-d582-376b-982d-9fcf2f3e887c | -2.99346 | -51.45453 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aadc7050-45c0-3a03-bf03-964ea05f7f04 | -2.94282 | -54.08045 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fc02059-f2e7-3b67-8cb3-fa588d29df71 | -2.57741 | -53.99856 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31157879-4e96-3385-94c1-e782cfb2b89c | -2.20963 | -48.91665 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce1a7495-acf1-3bb4-8f6b-71160c20db7b | -1.39865 | -54.49674 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 527e497e-f145-3cee-bce4-82a2b299d8f0 | -3.29045 | -53.85303 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ca6009e-ac92-3262-b55d-4bb1341cf66f | -1.61652 | -53.30462 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3c028a27-0d52-3e5c-b46f-e337f4cc7604 | -2.99005 | -53.3572 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa078c7a-b34f-3f0f-bc91-73121e8fd6f0 | -1.61356 | -55.13565 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e335388e-a1ad-3db1-a51a-4947c163ceee | -3.19444 | -54.32588 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a77aeddf-cc4b-3680-9a9c-f8c04ab2487b | -3.24736 | -53.27023 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f55ebcab-efee-3739-a8fa-53037530d627 | -3.24807 | -50.67078 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1031a2e3-1743-3ad7-bd71-8fff12844ef8 | -2.22407 | -46.38823 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b13e7651-f8fb-383c-b632-0945524ca5e2 | -2.44051 | -49.08737 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54eed2fe-bbd0-3838-80fc-f25e2f65455e | -2.57437 | -51.88261 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11692dac-d15e-36f3-b279-717963f53e5d | -3.68017 | -50.11404 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf1a5218-5200-37d4-a714-edc5e984866c | -1.64001 | -53.87497 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d977e6-8b09-3205-9061-29141ff66878 | -3.28845 | -53.68438 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README77.md)
