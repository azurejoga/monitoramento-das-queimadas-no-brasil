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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e486df1-7ffe-357f-8f8b-763d7e126b69 | -8.09749 | -58.03856 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a01efc1-cf99-35a6-b4a1-d55a160750b2 | -8.09694 | -58.04205 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e9d5eeb-91ce-3029-8738-f4e7a7b652f0 | -8.09694 | -58.02064 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dba28b91-3070-359b-b0cd-3e79b9ca22d2 | -8.09639 | -58.02412 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3a88dbf-8380-354d-9dba-1382efb82d5a | -8.09363 | -58.04151 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5babc949-3eae-3eb4-86b4-d3f4c4cb4c09 | -8.09363 | -58.02011 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54eb5665-fad4-361a-b6b8-21c2522c3679 | -8.09307 | -58.02359 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea67b5ee-1ad9-3d59-b144-59a6f25e8742 | -8.09032 | -58.04099 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ebcc1d5-7584-372d-a6a2-cc66541bb8dd | -8.08976 | -58.02307 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22349711-71db-3d5a-b379-b184ab1b6c98 | -8.89704 | -58.37363 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 489cb154-e649-3116-9ffe-41cd77d938d2 | -8.89648 | -58.37713 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3bfd6a2-bd34-354c-9799-7dd103c06fa8 | -8.89325 | -58.37724 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db183c82-a68d-3e7f-b30c-69e7c974d1e3 | -8.8927 | -58.35923 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6790ca99-c250-375c-93a3-75ecf36317d2 | -8.89049 | -58.37323 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efacaa9b-8dc3-36b4-aea6-961c0e706718 | -8.88994 | -58.37673 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32eff196-19a0-381b-8350-946401b249ad | -8.67904 | -58.27097 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fee8bd6-9b31-3196-8dbb-5fb9a28e1d02 | -8.67738 | -58.23852 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4984beb3-4494-3d09-b32c-63b2c87a17f8 | -8.67406 | -58.23798 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f58bce8-976e-39c3-8fdd-c92703e62f3f | -8.67076 | -58.28041 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 979738e6-d16f-3b06-b8f3-a0639240bd69 | -8.66855 | -58.27288 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f712245-5731-36c8-8f82-e3b53f82340f | -8.66799 | -58.27637 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab74ae81-b9db-3430-89f7-3cb089ad8b23 | -9.95499 | -59.53437 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df0a594-1788-3f58-8923-3352e82c878f | -9.9516 | -59.53388 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f8518a-9473-3059-8d09-13890011bf55 | -9.66568 | -59.06985 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c94f6c68-b800-3f2e-ac42-8722bc52e74a | -9.66511 | -59.0734 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2cc34b1-5356-3045-b977-1d3fd6df05bb | -9.3863 | -59.62307 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f66e638-7939-32a2-b78e-9cb09d62abbf | -10.45593 | -59.12458 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c849508d-bf74-305f-98f8-63c62d56187d | -10.45536 | -59.12817 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da98933-9622-3c44-8418-0553a8c8ae06 | -10.22348 | -59.41082 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fa07f7-6565-3fab-8893-4d63d21289f1 | -11.67892 | -59.91277 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26bb7bfc-23f5-3083-95b8-06a22d70fb88 | -11.67554 | -59.91221 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29f06fd6-822b-3481-9600-9a119a875440 | -11.67158 | -59.91533 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09789630-c7d5-3f64-a94d-42b443a4136b | -12.15523 | -59.74109 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8057ac2-e76b-3578-a8e1-b43c0b58c2a0 | -12.15362 | -59.72968 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07456337-efa5-3643-967f-430768395c80 | -12.15304 | -59.7333 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 084d7b5e-1de3-34ba-9882-f611565fa29d | -12.15246 | -59.73691 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d56d913-b818-3b0b-ad2b-c0349acd2949 | -12.15188 | -59.74054 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96f8e59d-f788-3319-8a7d-ba4e864d32e6 | -12.15027 | -59.72913 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38c7e666-cc8a-3e41-bbb9-0e86c2892c8e | -12.14969 | -59.73274 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267d2e14-9f34-3188-816f-1a31c114518f | -12.14898 | -59.75864 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028c5c28-2a83-3fc6-8d16-e773bbc94392 | -12.02818 | -59.59777 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 624793e2-3cc1-3d94-8bd9-f54016b015b7 | -12.02092 | -59.60025 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da32f96-2cc4-39ee-a1b2-4923e6eb8560 | -12.01642 | -59.6069 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a07143ec-1a64-3b7a-8765-0f075864ce54 | -11.85202 | -59.2759 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0718b05f-e0ef-3a42-b625-3733b3496faf | -11.85117 | -59.02503 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8996542e-cd74-37ca-a135-a294d1088eb3 | -11.84786 | -59.02449 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5902167f-08a3-3645-a836-6afe3770fd14 | -11.84735 | -59.00631 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5568194-39f3-3a0c-ad55-3ccde786aeac | -11.84348 | -59.00929 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36a30809-5587-3702-91b9-3a971436f853 | -11.84291 | -59.01282 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f87c7cfe-0413-378a-b358-30b0bca82e2e | -11.84235 | -59.01635 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc572440-9d9a-372a-bf4c-dc483679cd03 | -11.84179 | -59.01989 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8a5ec5a-c7f3-32a6-a500-114ff3a72aa5 | -11.84165 | -59.06337 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2960d28c-040e-341b-8989-9de610ab1e61 | -11.84122 | -59.02342 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b18635-9098-3048-901f-8e0e7e7662cf | -11.8389 | -59.05929 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e97761fb-a368-3676-8eba-fa3bdb1f0abc | -11.8379 | -59.02289 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48507b7-de01-321c-81ac-648fb7401e2f | -11.77154 | -59.29198 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0fb2c73-7866-3e71-9282-a4fb4d00d73b | -11.76878 | -59.28787 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc99586f-210c-37be-9088-2ac6b5312b91 | -11.76821 | -59.29144 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd9b39d9-66d7-3749-9e0e-4d4d547f02ca | -11.76764 | -59.295 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604ac0ce-91bd-3eba-877e-4dc8394bc6fa | -11.76545 | -59.28733 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9d8f6acf-0ca3-32f7-86a0-66a3e928eff7 | -11.70966 | -58.88969 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 549294fd-6408-3e01-9e6c-e52b863db965 | -11.70911 | -58.89321 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db39d187-5296-3f08-bf7d-b5bc7a725bff | -11.70855 | -58.89672 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7980b42a-6fc8-39ed-bfab-ee51468ae240 | -11.70635 | -58.88914 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82ea9af3-7bd7-3006-8e1b-30a733d98fbb | -11.70579 | -58.89267 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e958dab-5615-3861-a7a6-7034246bc949 | -11.70524 | -58.89618 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a91ebe9d-5d64-3e2d-8268-45e3966c0d7d | -11.70468 | -58.89971 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1d7852f-4ce3-3d2f-9cbd-95e896f21490 | -11.70304 | -58.88861 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52397423-3273-3ba1-923b-0537b044e6a1 | -11.70136 | -58.89916 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8b1f0ae-bb11-3ccc-9c80-f205a833933e | -11.69805 | -58.89862 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc016156-cd35-3e56-b4b0-78ef1c6c498c | -11.68824 | -59.30017 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae3261f4-3289-39f5-948f-55483c1556d0 | -11.68766 | -59.30373 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed67cb35-37d7-3155-8e89-3a6ef80da9bd | -11.67374 | -58.90189 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc07a47a-ce8e-3a62-949c-c2caa4aac7c0 | -11.56161 | -59.49541 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f55f9f71-52a4-31bf-aa31-b5e885de862f | -11.56104 | -59.499 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baefac71-6303-3446-b8c6-15548f8c2374 | -11.55711 | -59.50205 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 146e220c-fcc3-31b4-a598-6c1b504b8131 | -11.50158 | -59.44902 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2237052e-ba76-38a6-bd80-b70931ba19c1 | -11.49824 | -59.44846 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87299eec-559d-3add-b591-f7836f5d789f | -11.49605 | -59.44076 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b4073cb-db94-35d7-a71b-c9ffc1296f2d | -11.4949 | -59.4479 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7111f3-ae32-3bcf-8860-98f07463306b | -11.49432 | -59.45149 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdd7afe8-4b38-3e72-86f0-03ea5bf77864 | -11.47834 | -59.10585 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd70dd1e-8e86-30c6-b706-1df5ccafc6dd | -11.46095 | -59.33958 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c503d99-6efc-396d-b164-5df7a5b91e89 | -11.45879 | -59.336 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27bde6d7-d08c-334f-8b15-c29154bccb93 | -11.45822 | -59.33957 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96ad31dc-a4cd-3abf-a3ea-4b4aa1159f22 | -11.37843 | -59.1369 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ad314e9-9e21-3083-b144-45ce047bd834 | -11.3751 | -59.13634 | 2024-09-28 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12f51c79-66f2-3591-826d-9c7435ef9e3e | -12.98987 | -60.05723 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 290e3a59-1266-38f7-9fb0-67a3f04ac1c8 | -12.98928 | -60.06089 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ead1a513-4536-3bc3-81f1-79f744babdb3 | -12.98592 | -60.06033 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1d07cc4-6a8c-384f-9723-be7d06f6e012 | -14.50675 | -59.63087 | 2024-09-28 05:10:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010fbf2d-2f5b-3358-93d2-dec79e49c818 | -13.75013 | -60.12881 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db060a85-0b2c-36b8-ab1d-c65b6a9600f1 | -13.74364 | -60.10529 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f958e9f7-b861-35bc-b0ff-b5c32ddf0a5e | -13.70882 | -60.07296 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 377398eb-08e8-3c16-8d9f-85f6f16412aa | -7.60214 | -60.58015 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f5abe89-1921-3192-b843-55fc331a104c | -7.60147 | -60.58423 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8207687c-e998-3536-833a-c494bf7e5edf | -7.60079 | -60.58834 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2eb7619-3981-36c8-96e1-46c21be0962b | -7.60009 | -60.59255 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd2a0dd-cf8f-314e-8269-39bf6e720741 | -7.59924 | -60.57538 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b69bce8-806b-3467-b2a3-e0c4b6730e05 | -7.59855 | -60.57957 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README88.md)
