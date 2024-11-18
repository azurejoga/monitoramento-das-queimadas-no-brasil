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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d95905c-d014-3ad4-8a7b-1eb820aa9cd2 | -3.1543 | -46.588299 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9f6f7ec-e01a-3120-9b9b-1a1ab863bc23 | -2.7475 | -52.6167 | 2024-11-18 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| d5ff06b8-10f7-31ea-bffb-772943bc32ca | -3.6593 | -50.439 | 2024-11-18 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a3dec7ab-5f53-355f-9056-7ab3d03f4114 | -3.3452 | -50.4917 | 2024-11-18 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| dfb64840-effb-3adb-9def-ba4a33da2dd4 | -4.2685 | -50.5832 | 2024-11-18 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7f2131ea-5380-319d-a34d-4b67d77268f5 | -3.7563 | -45.9645 | 2024-11-18 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 295.9 |
| 468964d4-b344-3055-a396-b27a12d09ae1 | -2.7659 | -52.6163 | 2024-11-18 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 271.2 |
| cef76ba5-487a-3181-8719-39f94d59e6f3 | -2.68 | -45.7158 | 2024-11-18 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c3fc14d1-eb85-3ed7-8211-17e4273a2794 | -14.2857 | -57.6442 | 2024-11-18 00:10:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| de9c5f06-c71a-3982-a40d-55d3778bfb9e | -1.2964 | -51.7204 | 2024-11-18 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0b46592f-1eb8-3a40-a32d-b9e6d3c17ad8 | -2.5847 | -51.7181 | 2024-11-18 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 89538396-e7e9-33e9-a686-c3f0c2f0395d | -2.7843 | -52.6158 | 2024-11-18 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| c657de8b-cbbb-35ee-a245-78c52b41b795 | -1.2964 | -51.7616 | 2024-11-18 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cba39070-9a09-3916-89d5-b9e7be6d573f | -2.5846 | -51.7387 | 2024-11-18 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d683e535-1206-3352-9506-345edca4069d | -3.6592 | -50.46 | 2024-11-18 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 06956062-3150-356f-a04a-6d1675165924 | -2.8792 | -51.7726 | 2024-11-18 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a2d6b5f9-5e6f-3798-9070-8f126b8ef32e | -3.6778 | -50.4384 | 2024-11-18 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| efbf8d6f-7663-38d7-84ca-6635d87bb94a | -2.6986 | -45.6928 | 2024-11-18 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| bea3224c-84ab-3c32-8aac-ec8ade9e9186 | -3.7749 | -45.9636 | 2024-11-18 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 130.6 |
| ef9a4a23-2ab0-3501-913f-05f5a7488de1 | -3.775 | -45.9413 | 2024-11-18 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 323.3 |
| f81e2edf-0d51-3126-9c4b-fb34d802b1fb | -2.8608 | -51.7731 | 2024-11-18 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2294d5e3-b076-37bd-86b0-4d8a2f13e567 | -3.3287 | -46.0048 | 2024-11-18 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 734a051a-4218-3ccd-b3bf-8594e1c847e2 | -1.6962 | -45.8311 | 2024-11-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 860546f3-8360-3d50-ae75-398e8e99f345 | -1.3148 | -51.7408 | 2024-11-18 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e5f616d9-0198-3997-8353-bc4e13df5546 | -3.1869 | -53.2361 | 2024-11-18 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d9a1aab0-de0e-3c0d-8dcb-f6d95dfbac2b | -1.2964 | -51.741 | 2024-11-18 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 222.5 |
| bc8ff946-236f-3d8c-94c7-ad10d0b86fcb | -13.021 | -56.4544 | 2024-11-18 00:10:00 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3c6831d0-754e-3a32-ad9f-7e08b67fc756 | -2.7476 | -52.5963 | 2024-11-18 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| dd559da9-efec-3c5f-a6bb-9a9644399717 | -4.5771 | -45.6325 | 2024-11-18 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 92badbab-d507-38f1-99c7-613e8b932184 | -5.9556 | -48.0642 | 2024-11-18 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a9b32612-1cbd-3290-aa74-899d2358d75f | -1.7147 | -45.8307 | 2024-11-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 3f78164a-e8cb-33da-8fec-b779b1dc7e74 | -3.7565 | -45.9198 | 2024-11-18 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 09128635-cd77-35ed-8ad4-84cb11b79aed | -2.6583 | -51.7163 | 2024-11-18 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2e5e4340-db70-32a7-91ee-8c10410ebbe6 | -3.0764 | -53.2796 | 2024-11-18 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b0c7ca95-230f-38e5-bc4b-09e288d42234 | -1.4408 | -53.3917 | 2024-11-18 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| aef52f4e-3d23-38a6-91e0-7159f599868a | -3.0542 | -54.4081 | 2024-11-18 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7041e13a-278b-3d74-aa47-00674971d512 | -1.4408 | -53.3715 | 2024-11-18 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 780f6208-5e00-3bbb-9429-a4e4b643e41d | -3.5678 | -50.2534 | 2024-11-18 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 8c5cca07-3b60-3526-a8a5-a92bcdf67f10 | -3.3152 | -53.3744 | 2024-11-18 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1c2cfaf9-f5f3-3348-b1b1-fddec2947f6d | -3.7564 | -45.9422 | 2024-11-18 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 813.6 |
| eb91581e-ab06-3dcc-a3d1-231576ca9c39 | -4.776 | -46.491 | 2024-11-18 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4c883e4e-0a88-30b8-b6a1-f734c0017f71 | -14.286 | -57.624 | 2024-11-18 00:10:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f3d6742b-510f-3c71-91dc-e5d6fd1c096b | -4.7946 | -46.4899 | 2024-11-18 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 39cf5f4a-05d3-38ef-9c4a-1e72fb79e645 | -2.6028 | -51.8001 | 2024-11-18 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| cb0f2b9a-767a-3252-ae48-31ebe03bd539 | -2.6986 | -45.7152 | 2024-11-18 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 63920096-469b-3744-b9fa-84923ee6cd3c | -2.766 | -52.5959 | 2024-11-18 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 1f525403-a16c-3d12-a4ae-dec714faf5a8 | -2.8607 | -51.7937 | 2024-11-18 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 268986be-dca3-3e47-90de-39df5fbdab3d | -2.8791 | -51.7932 | 2024-11-18 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 48ec1f2f-e689-3a5c-bf1a-490e2e15804d | -2.6801 | -45.6934 | 2024-11-18 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5e26cb50-1dd8-38b2-a601-d2a2fd8585bc | -14.2857 | -57.6442 | 2024-11-18 00:20:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 264823dd-4dc7-38ed-8de3-60c8014654ec | -3.1828 | -45.4289 | 2024-11-18 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 837cf0e2-9254-3834-96df-eb2b86e7f944 | -2.5846 | -51.7387 | 2024-11-18 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b8560ec5-3dc6-3d4c-b48e-de6a66f6825f | -1.7138 | -46.1866 | 2024-11-18 00:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 43b96c86-c9cd-33e4-960b-928c11f715c3 | -6.5407 | -35.1917 | 2024-11-18 00:20:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| fe8aacf3-fed2-3b92-abf9-56420f7154ba | -2.5847 | -51.7181 | 2024-11-18 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| fcc076bc-6744-3b54-ac4b-72769b6c24db | -6.5216 | -35.194 | 2024-11-18 00:20:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| df484505-0484-3ecb-acbc-72fd74265111 | -3.0542 | -54.4081 | 2024-11-18 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fb4b2273-5348-329a-a477-292f0e966c83 | -2.8608 | -51.7731 | 2024-11-18 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| a56a4f5c-8216-335c-abae-e907a5131b39 | -2.6028 | -51.8001 | 2024-11-18 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f092ddaa-b9f9-3cd3-ac7d-a98356ca8b26 | -1.4408 | -53.3917 | 2024-11-18 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 38c3849c-d4a4-3880-aac7-e181f9d3fc86 | -3.6593 | -50.439 | 2024-11-18 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 58da8540-abc7-3b1e-8ba4-be6df81f297d | -2.68 | -45.7158 | 2024-11-18 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| dd485351-3e54-3920-a5cc-0c6a133f571e | -3.1827 | -45.4514 | 2024-11-18 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ccd9161e-8810-3ae0-a301-f7013282cbbd | -1.2964 | -51.741 | 2024-11-18 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 255.0 |
| 9e9d17b8-4bb9-30eb-aef2-5212acf033d4 | -2.8607 | -51.7937 | 2024-11-18 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 11d09028-20b4-3ac0-a7c7-fcf5c648788e | -3.0764 | -53.2796 | 2024-11-18 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 869a5070-812a-3c9e-bd4f-b1d3e2314063 | -2.6986 | -45.7152 | 2024-11-18 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| c35ff7aa-0edd-3167-b0a4-fdc94b615a88 | -2.6583 | -51.7163 | 2024-11-18 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3953fb1d-a73b-3c53-8b77-87b7be345a1d | -1.2964 | -51.7204 | 2024-11-18 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c12bdd2d-687b-3ec5-bb93-8dfd5ab80f48 | -1.6962 | -45.8311 | 2024-11-18 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 9a7f2e83-9ea8-31a5-91c2-342dda25f172 | -5.9556 | -48.0642 | 2024-11-18 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2b2a9e00-1509-3731-b6ec-de85f521ef45 | -2.6986 | -45.6928 | 2024-11-18 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8e6715cb-855c-32b0-8d13-6247b77db0e2 | -13.021 | -56.4544 | 2024-11-18 00:20:00 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7a507a1b-fd5a-3b02-9454-2490dd141663 | -4.5771 | -45.6325 | 2024-11-18 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| eee2a870-ef5c-3c8f-b58c-7d3a1c93a9fa | -14.286 | -57.624 | 2024-11-18 00:20:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4173a77c-e78d-3994-8a67-6771c9151b40 | -3.6778 | -50.4384 | 2024-11-18 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7e1fd692-1d3b-3e9f-818e-ef1f9bb65d39 | -1.3148 | -51.7408 | 2024-11-18 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a1f36ceb-2e2b-3d7d-8b15-271e5faf5adf | -1.7147 | -45.8307 | 2024-11-18 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| c3d2c9d1-df73-34d6-b6fb-3e3cfe8285c3 | -2.8792 | -51.7726 | 2024-11-18 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d224998d-d60c-3878-8227-ff59a7ac00cf | -2.8791 | -51.7932 | 2024-11-18 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 64c81040-0313-38f2-81c3-89539d97ea76 | -1.3148 | -51.7408 | 2024-11-18 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| e1901047-e665-300d-a3ad-1c61d0476d1f | -3.3267 | -50.4923 | 2024-11-18 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1e36bd36-5e77-35de-8b0c-1402df2e73bf | -14.286 | -57.624 | 2024-11-18 00:30:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 32784b16-0534-35ed-a9e5-dc5490ceca5f | -3.0542 | -54.4081 | 2024-11-18 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 294faa35-77cf-31b4-8292-56121f275195 | -2.8792 | -51.7726 | 2024-11-18 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| b6da98fb-cb64-3a96-ac45-a525c1d564c1 | -2.7475 | -52.6167 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| ef7f8674-b09f-34d3-a28c-81b814e0604a | -2.6028 | -51.8001 | 2024-11-18 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4699ddd3-4889-3b7a-b1f9-9758d959cc8d | -1.7147 | -45.8307 | 2024-11-18 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 165.9 |
| d2387125-a3e3-3555-a9a1-5ab64938b4f0 | -2.766 | -52.5959 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 174af68b-7257-3100-bb4f-3a9c4ef5c5ed | -2.8607 | -51.7937 | 2024-11-18 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| b760e046-fdf3-3d9e-a159-458e47dfd869 | -2.7476 | -52.5963 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 10733989-94b8-3119-9bcb-3a11ba168f58 | -3.775 | -45.9413 | 2024-11-18 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 3612ac5f-631d-3994-a575-854f5d83cc7e | -3.1828 | -45.4289 | 2024-11-18 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 96ee76bb-d737-397a-936d-e11ca61d92b0 | -2.6986 | -45.7152 | 2024-11-18 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c7433fe6-3fc9-3664-85ee-033d840faa61 | -3.7564 | -45.9422 | 2024-11-18 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 8e19fa06-f848-3600-97ff-87f421a611c2 | -6.5407 | -35.1917 | 2024-11-18 00:30:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| 66411acf-3394-35c3-ae59-18c4ff084e72 | -1.2964 | -51.7616 | 2024-11-18 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 400e89b8-60fd-3794-9be3-71091f17fef6 | -1.2964 | -51.741 | 2024-11-18 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 336.5 |
| 971d6f57-f12a-30af-b509-cddb2073efb0 | -5.9556 | -48.0642 | 2024-11-18 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 49399871-75f0-3171-930a-f0f01f70c1bd | -3.7563 | -45.9645 | 2024-11-18 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |


[Clique aqui para ver as próximas entradas](README6.md)
