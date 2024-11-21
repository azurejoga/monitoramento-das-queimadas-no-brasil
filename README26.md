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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9846ecae-78da-3f7e-85df-8e1392cf913f | -3.54543 | -50.53194 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca13837d-4a17-3f95-b761-a7e28e2493a2 | -2.23921 | -50.16495 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86995cc0-1890-38d6-974a-6dd97327af37 | -2.51613 | -48.34505 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28f6e592-f958-3ff6-9b59-1d14468de93b | -2.62303 | -48.07171 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fdc3545-02ad-3dd2-9070-25d0ff3c5dfe | -2.76534 | -52.11061 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 995b3945-658a-353c-b466-65b404276b55 | -2.89135 | -48.2737 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0897fe84-5b70-3776-85ec-4853a177c787 | -1.70784 | -50.20372 | 2024-11-21 04:29:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cec2326-5860-339b-8df2-14cec239020d | -2.84233 | -46.68504 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2d1a46f-e223-3fa3-83a3-abf2ee5f5b52 | -2.51411 | -46.21212 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6d3ab6-5a50-3ae7-8c58-d3446a0a9f2e | 0.14111 | -51.09932 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e72aef-0b17-3645-858c-587a50f9af83 | -2.09747 | -46.38816 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ba0b86-77b7-3203-9b11-65bb82e2fa85 | -2.24642 | -50.51374 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8badd545-7160-36a9-823c-f9846c055463 | -0.80105 | -51.78523 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 275553eb-7214-3af0-b4ff-3565e8df83b6 | -1.7869 | -53.61758 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b9470ac-8e12-3070-93d3-0bce250242b3 | -1.64829 | -52.68824 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8674db42-944a-33be-8371-109fafe7ad5e | -0.94765 | -51.64274 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c28e0fcb-d95f-3f51-81ef-e388b62461f7 | -4.24059 | -46.11656 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d54cd37b-4d5b-3ebf-9d6e-974363470412 | -2.63089 | -48.06566 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3d2ac8f-e01e-3bd3-add1-62bff6183236 | -3.18098 | -50.38817 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd2f9387-36c0-3e6f-89b2-e80b00dc8d86 | -2.26734 | -48.74968 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcbb9070-75ee-337d-9901-2d570eb11db0 | -3.94238 | -46.70441 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 415742dc-81f0-393b-b6c6-30593539ec54 | -2.82296 | -46.67849 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af0f0ec-3427-347e-8a9a-66e48ea4add0 | -2.66512 | -46.60749 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5266cdc7-9664-37f2-a7c1-e1be5d3f81a0 | -1.54696 | -47.21374 | 2024-11-21 04:29:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5771e2-6ccd-3bf0-81be-d190f214eda9 | -3.27899 | -48.79844 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ae96d14-4dae-3ba3-bf59-eba6ba967014 | -2.55808 | -47.28689 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b64fb343-2a84-3f38-8b08-ec7d1b4b1c45 | -2.93021 | -45.27087 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c0da2269-1741-32b7-a39c-f970219c6a3e | -3.32867 | -50.25585 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bac7689-4994-3029-bb9f-e966be173940 | -1.73105 | -52.39611 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62d313c6-0406-37bc-b4d2-147d274978f9 | -2.63734 | -46.56782 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d80ff2cb-9f10-319a-81ae-cbc38d0f45cd | -2.81759 | -49.15362 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8eca732-f6bd-3064-b527-eeb84ee7e528 | -2.22417 | -48.38105 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c877656a-a927-3745-ab6b-c55ef84b3f64 | -1.63854 | -55.68 | 2024-11-21 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aab336d-52d6-3a66-887e-4099267170b0 | -2.91884 | -48.3184 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1c38167-c131-3c26-bb7b-f8b7f449ac15 | -3.08835 | -45.97906 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6f2a1f6-d6db-3729-883f-22014c33566f | -2.29167 | -49.05836 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1a7c57-8e4c-3ce0-a046-06c7710cb893 | -2.90494 | -53.05362 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac1894f4-a602-3cb8-bc21-adf6233cdbc1 | -3.94407 | -46.71531 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c27a6f1-c711-39b3-9080-0890dfe2fd39 | -2.21119 | -53.71455 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3857f8d1-b3bf-301a-a613-c3fa77966cc3 | -1.64733 | -52.66701 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d795e926-860b-31df-983a-c7810300de60 | -3.23308 | -46.43739 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18618ce-e4fb-3b97-bd84-4cc1b93bdf61 | -3.95628 | -46.72429 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c07c1859-a3da-305f-b319-a33d955b246d | -3.55331 | -50.2757 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b509c77e-55bf-34dd-bd08-e267ea684ff4 | -2.19966 | -48.84261 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb70632-45aa-358a-bcfa-3ad315a6b793 | -2.68392 | -46.24895 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af86a389-e7f3-314d-b4cb-45642b14d02a | 0.44775 | -50.7954 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0933970e-08cb-3f0d-98d3-b6dc20d6dc78 | -2.00414 | -46.31356 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f399cee-e939-3ed1-960b-7cfa3a92ed25 | -1.64388 | -55.68086 | 2024-11-21 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21a26f02-c66a-308d-af41-b403a63cc865 | -2.09693 | -46.39161 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd70b5e-6d14-318c-b72e-bca408ea961c | -2.63841 | -46.21703 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9bca1c2-92d6-3a9f-8414-a5a507671f46 | -1.28806 | -52.46743 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 732b3742-190a-3259-bf76-a252bf7a3c2e | -2.60765 | -48.21181 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 449a0c1a-010d-3906-991a-50d3db3a4c59 | -2.2504 | -46.87475 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ab09714-edcd-32c0-9b66-3353217c2c09 | -2.18464 | -52.12897 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a672733-afe9-3aac-ac0d-8b0760376acb | -2.68595 | -46.19232 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b7dd7da-9bd3-30c9-9cb2-b4f0d7606d38 | -1.6418 | -52.60861 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd5073d5-9205-325a-a656-3e326a748844 | -1.74683 | -52.06062 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc207b46-9b78-3da7-8027-078cb1c115b1 | -1.55033 | -47.64717 | 2024-11-21 04:29:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a47f05bc-42df-3d4a-a93a-0557152bd6ed | -2.61895 | -48.18424 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af190aa9-d3f7-389a-9ab5-b79d9cbd70fe | -3.26649 | -48.7889 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef72284c-5fb2-346d-9a04-d377d1ac9fd8 | -4.15809 | -42.0217 | 2024-11-21 04:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| c981601f-f41b-3f21-a2c1-389cf80efd9f | -3.64453 | -50.21743 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e904b32-e6e2-354e-a151-5e3bcc0271ce | -2.57264 | -48.20652 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b41ba017-bc61-3936-964e-b0d87b2ff078 | -3.1895 | -46.49805 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f014289e-431a-37d9-8f1e-99bb7c0f1d99 | -1.59524 | -47.4924 | 2024-11-21 04:29:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34497cee-e1e8-3676-9825-367080cdc4c4 | -2.47698 | -48.59265 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f2adec8-976a-3427-a88e-69e6c363b0c4 | -3.03862 | -49.46739 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98e2d32f-8df5-3df8-8455-8a8d5e19b148 | -2.5127 | -48.36676 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310c3960-a578-31e6-a6da-8328aa9a22d8 | -3.07392 | -50.96405 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ead8766b-4543-3d6b-9b49-218cb1a65855 | -2.70949 | -46.08535 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d137a11-6071-30ea-87a5-ae5836bee5e2 | -2.14184 | -50.48998 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8081a068-f9ef-35c8-8f2f-ffbb078c6d46 | -2.834 | -46.67314 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1f3753e-8925-389c-a088-1efb293af2ce | -3.08611 | -45.9715 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f810675b-635c-3004-b088-5145704ee1d6 | -2.65043 | -46.14052 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b98364a-2860-32cf-823c-d6c061362f75 | -1.64689 | -52.6893 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efd75cc9-69fe-3614-9c34-86e9ccfdface | -3.17047 | -49.15707 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc24777e-66b0-3563-9826-0bd012bc6a7c | -2.23453 | -48.33808 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39616f29-e05e-3c2e-832d-20c195b9a1ef | -1.36353 | -55.69812 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5217bd6-db4d-3e99-8616-65b974177898 | -2.72924 | -47.97552 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63626c5c-3552-3e5b-babb-56b3f43eb558 | -2.31651 | -49.08189 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0edbe0-5aaa-33a8-9bb5-2feee8a838a6 | -2.92989 | -54.09013 | 2024-11-21 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a821b364-098d-3921-b084-b838db18d4f7 | -1.54558 | -51.2324 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b1026cf-40e8-3240-8d41-e4bad4a5f52c | -2.27637 | -49.56027 | 2024-11-21 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 584723a9-d2b2-37d1-93ba-b3829e4f1248 | -3.35496 | -46.63422 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 389d2d69-3705-3be2-b727-f72654d5b81c | -3.36396 | -51.05507 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cc7ec79-19f9-3f0d-bdcb-fa9fdd2476c7 | -3.16109 | -50.58535 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df24bb66-5800-3f1a-9630-0564e08ab6d5 | -2.16999 | -51.96846 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c629412b-775b-3e7e-8992-ad4fe14b5b94 | -2.84602 | -49.15419 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c52f803-e509-3373-adfa-cc8c606da698 | -1.25144 | -53.36352 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2a1d30d-a771-36d5-9890-41a502a7c636 | -2.13337 | -49.80057 | 2024-11-21 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445d90fb-6cab-3d1a-9e5d-c86da6ff3560 | -2.94939 | -53.71995 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e7f9bbbc-b05c-3872-b450-f388ec98aca1 | -3.39984 | -50.25425 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3740b59-1caf-349d-94d1-a66072938752 | -3.1022 | -50.20232 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bfaee14-5ed5-38ae-8871-4aec167a38d8 | -2.84287 | -46.68159 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0960d58-e632-35d1-aebc-5d1bfa34ecf1 | -1.55239 | -53.44366 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62bbb084-eb99-38b3-ac59-c2089abce326 | -2.62436 | -51.79946 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 968e7147-296c-38ad-bb8d-601e058ea1ae | -2.17928 | -52.13574 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcdb2d93-d92a-39bb-a32e-2bc59913f8fb | -3.26176 | -50.63089 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cf78ef8-89d3-3521-8d68-145bff595cba | -2.8752 | -51.79408 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ba0fa1d-c2fe-38d7-950e-5ceca2b1011c | -2.24319 | -46.81668 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
