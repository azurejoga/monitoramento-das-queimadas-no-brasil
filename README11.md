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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3878ab-ae55-3f46-a47d-cd9076b79f6a | -3.86952 | -42.96377 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93f7ec4f-2ea4-3ec6-a64b-9e26b9aa5d12 | -3.95971 | -43.11308 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4f3f68-7b06-3099-9171-66cdc617d68e | -3.95902 | -43.11769 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34238d45-817f-3702-b908-08e874f065a4 | -6.9934 | -42.89875 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b2bbb163-f32c-3d2a-a841-34f05f0ed870 | -6.83997 | -47.89351 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2115a4a1-e2e7-3ab3-92f6-6c89775b5c9e | -6.37137 | -43.59436 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a5a2951-f8c0-30e3-8c29-a9ae24760574 | -7.36849 | -47.02869 | 2026-06-24 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dee4b00-d42f-3e3c-a53d-f98ca210a31b | -6.84381 | -47.89058 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e30edf9-c22e-3a63-957b-73425e0e4ce2 | -6.84105 | -47.88662 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e8571ac-1df1-37f0-b848-f46b1ded1a83 | -6.84481 | -47.8625 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a74a438-da70-388a-9568-c3d53ff2adb0 | -3.96349 | -43.11365 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32c0cee6-2d8b-3821-99b5-e7a2c68a2e8d | -4.66828 | -43.22 | 2026-06-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84f4f719-9d01-3344-9749-4527c77ceb3d | -3.86883 | -42.96848 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8de8a759-67a0-30d9-a31d-0f0be915574c | -6.36708 | -43.59652 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6a41c7db-a954-3536-9105-7b611a6924eb | -6.36447 | -43.58869 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 495191b9-b843-3c3d-96c1-e91ca38bf7ff | -3.87264 | -42.96906 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ef2b3c1-d286-3709-b0b2-89431002d10c | -6.8432 | -47.87283 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ed24fa-8571-316b-b7f0-423f197397dd | -7.36795 | -47.0322 | 2026-06-24 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8d59151-7ba6-3aff-bf99-855e338ee2ea | -7.29323 | -46.25007 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11e8cd37-16b5-3986-bb67-dcc68827eaa4 | -7.3025 | -38.88913 | 2026-06-24 04:32:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2823cb54-8fe6-3b8c-a300-2a41b30f1e4c | -3.95834 | -43.12229 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a9f1a7-ef67-3d0e-a4f0-ee14fe63804f | -3.96212 | -43.12287 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ac5d6d3-a800-3ef6-b315-e638ce88ec08 | -7.28985 | -46.24955 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f2e6d3b-edd2-322d-8585-0d6f96d9babf | -4.45612 | -49.14915 | 2026-06-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d407a6e8-9669-3a6f-8a31-6f252c190036 | -6.84549 | -47.90144 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6373002-fc9b-34f8-9fea-96081994aa7b | -4.67814 | -48.1565 | 2026-06-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa8245e9-db70-35b7-9ce4-5560ffa5bda7 | -6.99844 | -42.89233 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 766e9e9b-d683-3d93-a512-8d07f4973928 | -3.87022 | -42.95906 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9525f5a4-beca-3ef3-8cbe-92cb4dda7200 | -7.29378 | -46.24642 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58deb8c4-360e-3ccb-bc49-95e1429b6364 | -6.99593 | -42.7695 | 2026-06-24 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 790a3e39-7671-3d69-95d3-f4eb80493162 | -6.99945 | -42.77363 | 2026-06-24 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3fd05a4b-556b-30ae-b02b-75fa2e0aa25e | -6.37156 | -43.59233 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ece01cc3-033e-3cd2-9e28-1834d743aafa | -4.33742 | -48.96229 | 2026-06-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38aae6aa-5d6e-33f5-bd43-ed6c5187da44 | -7.37505 | -42.79842 | 2026-06-24 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa71a15a-dc32-3cad-b453-07d9c1b5f718 | -6.36395 | -43.59134 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0910fdf-faf7-32ea-af85-a6ad898a4685 | -6.36376 | -43.59339 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe8da844-f1a7-3844-adeb-4f281a145d8e | -4.66378 | -43.22409 | 2026-06-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e8c3d0a-502c-361f-8e17-4bf900799c66 | -6.98991 | -42.89471 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89ea223b-d64c-35f8-9e93-ed8f7b1becf2 | -6.84434 | -47.88713 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5914da2f-b8b8-34a0-b7ea-a94326603aff | -4.35175 | -47.76454 | 2026-06-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74dc62f3-e808-3d3d-a903-1df175d87621 | -11.25805 | -43.33255 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0c9afab-0353-35aa-9bbe-a8dc87569c2d | -11.90883 | -43.40418 | 2026-06-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1bc60e65-fa44-3874-9353-febbacb8a1b9 | -9.52796 | -48.13233 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8582bdb-fcde-3602-be57-a37f82006eb8 | -11.19286 | -48.58352 | 2026-06-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb99445a-4c39-3f7e-b4e8-8f9218e6a736 | -9.51509 | -48.06259 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e6a5481-d090-30a8-8509-83463343cdda | -11.54236 | -52.78368 | 2026-06-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2d5756f-9fd4-319c-b24b-7d4fa99ca291 | -11.31144 | -43.33053 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b00b053-16fd-3218-8d25-8911d40c43ec | -9.51125 | -48.06555 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 687a4237-7001-3b90-89de-80b5d1d614cd | -11.51551 | -56.12487 | 2026-06-24 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47e5b761-8b6f-3eb7-93d1-5b9eb1dcb5ce | -9.21262 | -47.92901 | 2026-06-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 248ffb38-d149-308f-8abf-36ee988749bc | -12.77723 | -44.43867 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd6eb30b-30ea-3276-b9e7-b151b7480b77 | -12.83578 | -44.36329 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 31992101-7fff-3a8f-93fd-b971417aeefd | -8.68684 | -47.85336 | 2026-06-24 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7d14b920-51e2-324e-9f6c-8aa0fa9df7ba | -11.27255 | -43.34927 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f01bd85-08f1-3caf-97b4-552731a97e02 | -11.41401 | -54.438 | 2026-06-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de10b4b4-38a0-3718-be42-8f05776867d6 | -11.96878 | -49.23607 | 2026-06-24 04:34:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0c92fa-60e1-3042-8e56-71eb31381ef4 | -13.18316 | -43.40015 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 57741f96-8b3e-363d-a965-8b8595c6aa72 | -11.24159 | -43.36013 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 510a5c85-6b7b-3fe0-a713-c44af7340c10 | -11.4828 | -46.73759 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3541a4fa-43c3-3663-b15c-735b22b24b92 | -12.51337 | -48.26721 | 2026-06-24 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5752537-ba7c-3f52-b393-289a3cab285a | -12.83901 | -44.36902 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a12ce63c-3a03-38e3-85de-2052c26c8759 | -8.68301 | -47.85632 | 2026-06-24 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 45dea60a-7762-3ac4-b0d6-abb845c5a41c | -8.68712 | -48.30775 | 2026-06-24 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a2f0fd6-6744-3e64-94d2-d9ee3aae1807 | -9.43986 | -48.86945 | 2026-06-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4965f9a-1b0f-3d53-ba6b-7a64ab527bd7 | -9.17812 | -58.05805 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e717a2-a30f-34b5-80d1-5b8ea18f9f08 | -12.85229 | -44.36046 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9d9e68ab-d697-321c-b33e-cbdbb19d9ecc | -11.51678 | -56.12269 | 2026-06-24 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 890522e7-cabc-31eb-9c21-1b6b234be4d6 | -9.32553 | -48.51639 | 2026-06-24 04:34:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78383ae3-1ecf-3ca5-98b3-e4ebf092eb7e | -12.87421 | -44.37113 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44826ff5-f32a-3d8c-aeae-eaf3017c477f | -10.12877 | -52.11528 | 2026-06-24 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5890fc47-3636-39c0-834a-dd85d20ef57f | -8.26645 | -49.3589 | 2026-06-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9541573-a642-3711-a54b-03658f8ef289 | -7.63721 | -50.21435 | 2026-06-24 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21dddf73-7e5b-3f65-bda7-744eb9b6ff3d | -7.59918 | -46.47473 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac6a0fe-c26e-3de0-a752-2a3ca19703af | -13.07177 | -53.35686 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e7ddac76-ba26-3a5f-a739-0c57247b8bf4 | -9.22042 | -45.34194 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbca0b78-9a4a-3d9e-86bc-9d0db4a273db | -9.40862 | -50.69604 | 2026-06-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7debddfa-b574-336f-8b8d-6a601ab68e33 | -11.54686 | -52.77973 | 2026-06-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e7b1d9-3047-32fd-9a4e-48bdf573a4a7 | -8.61456 | -45.99768 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 630035a4-2726-321f-8ba1-e46f628fa255 | -10.77833 | -54.10118 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0980bc5-b3fc-3f82-8564-f812bb7dc560 | -11.30677 | -54.7212 | 2026-06-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5de112d-f6ee-3bf1-8ffc-67b7e615e40c | -8.26923 | -49.36299 | 2026-06-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df0e60a8-e6db-394c-b6c9-9a89bd2a4690 | -11.79515 | -42.63764 | 2026-06-24 04:34:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad79fa6b-f9d7-31f0-b8a8-4d7e3b461706 | -13.11895 | -53.53488 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd5984e3-1441-397b-87df-dcd0e09558da | -15.01952 | -42.37127 | 2026-06-24 04:34:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5856c0fe-b792-3265-a870-7f9b161cba7f | -10.7777 | -54.10484 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e1fb0d-25d1-3b48-80aa-9c56a39352e8 | -11.92066 | -44.17319 | 2026-06-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 280a7802-dcba-3d95-86bb-1357edc8eae4 | -11.30255 | -54.72046 | 2026-06-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b30ea9d6-e888-3117-93f1-578b9acdfc44 | -11.04658 | -54.19502 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81eaeb93-357f-3cb0-b347-cef37eada418 | -10.39298 | -56.71774 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4bed1a5-098b-3908-9011-0e8f5eb2dbe0 | -11.19232 | -48.58701 | 2026-06-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04b13772-de50-31e2-868c-7f076b778083 | -12.66326 | -47.68159 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b562bcca-6663-3feb-bef3-debfff7a1f0b | -12.67946 | -54.57994 | 2026-06-24 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 409692d8-5f2e-3045-8258-3044b877aa24 | -11.27898 | -55.79079 | 2026-06-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb7f895-7254-3786-a93c-e165aa630322 | -9.21981 | -45.34606 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4688a2a3-ddb6-3bd8-91d4-501445511f73 | -9.3847 | -58.20316 | 2026-06-24 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e3d1c20-2663-3f54-bcea-a4a0634ed811 | -8.61111 | -45.99714 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 394a203d-9e09-3e11-996d-785f1eef5db9 | -11.29953 | -43.32504 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e19cc243-19b2-3bed-b0dd-addc46fc6bcb | -9.21593 | -47.92953 | 2026-06-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d455caf-e1e5-3f68-9617-cf1d5c5b5e3f | -8.8566 | -46.94668 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75392c4d-88c1-3a6b-a16b-cbdc6a52c372 | -11.30418 | -43.32186 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README12.md)
