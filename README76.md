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
| 964574fb-07e2-38a4-96ba-171601ad21af | -4.1095 | -48.25134 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 540f74a4-f39d-3cff-9c90-433448daa028 | -4.10676 | -48.24427 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3b6b9fc-d887-3771-a1f5-088231279e45 | -4.10604 | -48.24898 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a81f9e4-f799-3d72-bcf5-e335128afd3c | -4.10559 | -48.24594 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8aa41e64-a0cb-3c86-b89d-fa7494351c53 | -4.05558 | -48.24084 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d5484ed-97b7-3b40-be4b-ad8f073ce4cc | -4.05171 | -48.23535 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25beb19e-f0d7-3dea-9622-5ccf8f992d15 | -3.98256 | -49.0277 | 2024-10-13 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32ff7c3a-75a9-3ddf-9f06-cf15e47dcc01 | -3.92202 | -48.35088 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 658ff8a5-ca92-3f35-8ad1-9b19a71fbb91 | -3.92135 | -48.35543 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d92ee14-262a-3224-8395-bacf0ef02c3e | -3.92067 | -48.35997 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56cf5bc2-97c6-3dff-b5fb-f327384b4a9d | -3.91748 | -48.35017 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c93b6ce9-8055-3ffe-b816-bbca0fb0a670 | -3.9168 | -48.35472 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b2dd660-d70b-3c4c-bbb2-9b09663d2d56 | -3.91612 | -48.35928 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db872183-1726-390d-8fca-68a67ccc9e96 | -3.91158 | -48.35858 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed9c2386-2a49-3840-ad24-37ca4578ed19 | -3.90769 | -48.35343 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6959cf25-e20e-35bb-9291-6ff2f4dece49 | -3.90702 | -48.35795 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd84d1e2-f45c-3f85-a883-8ed9ee8c3155 | -5.643 | -48.6438 | 2024-10-13 05:01:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 723e688d-0adf-32b2-ae25-0ba0c7fa6101 | -5.6427 | -48.64537 | 2024-10-13 05:01:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57102dc2-9e70-3101-b42d-496ebf924765 | -5.64234 | -48.64848 | 2024-10-13 05:01:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14f7b4d5-435c-36a5-842d-a73bcdd32cc2 | -1.90733 | -49.51969 | 2024-10-13 05:01:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46633801-fad9-3d24-9f24-2870a882bb28 | -2.17531 | -48.8441 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc19a0ed-58f5-3b93-9eca-568870761069 | -2.17392 | -48.84245 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02c4f345-db53-3ade-966e-60fab08efe62 | -2.17332 | -48.84646 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dac0edc-05eb-3872-83d9-40effe3cee94 | -2.17103 | -48.84345 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf42c466-4322-3ee8-849a-1fd8897eecff | -2.1704 | -48.84745 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202ee5fe-b21a-3d82-89bd-ddbd26a001dd | -2.16675 | -48.84276 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 469333cd-4913-37a8-9157-d7a966fe6002 | -2.15944 | -48.83345 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f3325a7-6e83-3c62-8c7e-dae902ce2732 | -2.15757 | -48.84542 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00caea5e-ef02-3c37-94ed-c3b092522a4a | -2.15454 | -48.83677 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd8d8e87-32ab-3757-9b15-ec8120cf8bcd | -2.15392 | -48.84074 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74cab79a-54e8-38c2-9505-dde5c5584bbe | -2.74376 | -49.52158 | 2024-10-13 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 247e3d78-9103-3f0e-aef0-eead58da1bf9 | -2.61951 | -49.51729 | 2024-10-13 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe4516dc-3380-32d0-bed6-e2d24efe1f07 | -2.52134 | -49.67724 | 2024-10-13 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80483fd7-3fd9-306c-9864-50ccfc818697 | -2.51727 | -49.67663 | 2024-10-13 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd2366aa-7f7d-39e9-86f3-67370cd45086 | -2.42473 | -49.62977 | 2024-10-13 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4f54127-0e7d-31d9-ad2e-c1f463754776 | -2.79547 | -49.29176 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc47dd9f-9ce0-3a58-bb31-52219ba65058 | -2.79489 | -49.29558 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c7b054e-7586-3d01-a662-7fd0b61c7eaa | -2.79432 | -49.29939 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68646233-e45a-3ed0-bf85-0398af46aa83 | -2.79128 | -49.2911 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82b142ab-7083-3193-b849-5446e9df8940 | -2.7907 | -49.29494 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 70d4690c-cbe6-3d9a-b2d4-d95b326f1143 | -2.78709 | -49.29045 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f88f4f9-54d7-3b86-8a77-5a778be08ba2 | -2.77624 | -49.3624 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 07de1a0a-53d3-35d1-b9a4-18ce7220fb22 | -2.77567 | -49.36616 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7527a2ba-1635-3e06-9c20-1036d796487c | -2.62007 | -49.08438 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa21b7b-8d8b-3aa8-afe3-ba1bb3811e3a | -2.5864 | -49.2492 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6e1cd40-a63a-304e-b91f-9d716f637ab9 | -2.57011 | -49.12944 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4b3dce-ae98-3d2c-9836-f5a3fce5cfc0 | -2.56953 | -49.13237 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ccaf4fa-d0c3-3c0a-a309-34576a8d050a | -2.56951 | -49.13328 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 353e666f-6676-353d-8d6e-d19397f9655a | -2.56589 | -49.12877 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f175954-e666-316a-9b6d-971c60242b1f | -2.56531 | -49.13169 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a578ed8-9f08-347d-afe6-060b1f2a2660 | -2.46695 | -49.01912 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b4ef35-799d-3a15-a069-669bbb1daf6e | -2.4627 | -49.01846 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02a19b7d-671b-34e8-b965-befb513ad94a | -2.40424 | -48.94496 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2023c5eb-b7ca-3df5-9097-8964946852d8 | -2.3807 | -49.12943 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d41893e-bd14-3c0b-b277-bd09ea44a6d4 | -2.37649 | -49.12877 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 123e2af7-d505-3019-a9c4-817567e38c45 | -3.3359 | -49.15775 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6db16c17-6ef1-3937-a36e-ecc27e853964 | -3.33531 | -49.16171 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0090c5d5-c255-3338-b858-7aa3af674f87 | -3.29667 | -49.11255 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54684fb6-42fa-3ad8-a266-7468f03e6534 | -3.18995 | -50.45171 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee8bd94-1ca8-3899-9975-57dc1215dd55 | -3.18919 | -50.45669 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6166961b-086f-36a0-a837-b8232176677c | -3.18841 | -50.46176 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5b2d908-c527-3759-8c6e-8767134e07b1 | -3.18604 | -50.45112 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7c199c8-757b-3f6b-b8e3-3a55f72412f6 | -3.18527 | -50.45617 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3d4b530-daa3-3e28-ac70-3db8143bb5b6 | -3.1845 | -50.46116 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9447aea8-ad5d-34b2-844e-cbd27c0e3f7a | -3.18212 | -50.45061 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d90bc4-98f2-3378-9bbb-3eb51250db73 | -3.18135 | -50.45562 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a1629dd-4700-3387-ada0-6c1c2de4d680 | -3.18059 | -50.46056 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e34cd06-2361-3d70-a34a-18454d311997 | -3.17984 | -50.46548 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2701a70c-865f-3b7f-96e0-4c228f437013 | -3.1782 | -50.45005 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe5d1271-5ed6-3d30-b19d-ff3f8e1bf940 | -3.17744 | -50.45507 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dff8cc6-18ca-3f18-ac6b-5c9d7c556677 | -3.17668 | -50.45997 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b2cee894-84e6-397c-9cad-6b36479c9911 | -3.17593 | -50.46489 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5add7915-250a-3bc8-a22a-ab72e1aa5cc3 | -3.17352 | -50.45449 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30bf5939-7ed9-3ac0-baca-9cef532c4b02 | -3.17277 | -50.45939 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e31226c6-54f7-36bc-9081-587dff75f189 | -3.17202 | -50.4643 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 80e6f9cd-de37-34d6-8787-f84e689a7626 | -3.17127 | -50.46922 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ff8aa58-7dab-39e9-846d-a9c1930603aa | -3.16961 | -50.4539 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da23641d-cdb6-389b-8c3b-b9631630e17a | -3.16886 | -50.45881 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27fc8bad-8667-3602-b4d0-9584465f6196 | -3.16812 | -50.46371 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9319f0c0-fb5d-3a7d-964e-d548673bca61 | -3.16737 | -50.46862 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d39b264f-6c03-3adb-80cd-a4411fa1c77d | -3.16495 | -50.45823 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1103af8-d8d4-390b-a3b8-a35535bb788a | -3.16421 | -50.46313 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c90b8fac-322d-323c-97b1-faf22de38f89 | -3.16184 | -50.34653 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ba0d33-4c10-340a-9d8b-45c665973c20 | -3.1611 | -50.35147 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65239cda-0367-3599-b6e1-d79e9253aa14 | -3.16035 | -50.35643 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fec9217-252b-3028-b996-158f3d1be779 | -3.1579 | -50.34595 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8033cadd-e069-3d1e-9cf8-7e3483e0bed9 | -3.15715 | -50.35092 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 481a678e-20ca-3658-82d6-fbc89bbe8f1f | -3.15641 | -50.35586 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a34abd98-eea0-3012-832f-2a975a1714f7 | -3.15567 | -50.36079 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8568cc0-0be3-332d-aaa9-94cad87f5d04 | -3.15491 | -50.36578 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6dd928b-d0d5-34b5-887b-5e55bd9307c6 | -3.15416 | -50.37081 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45bbfa5b-f6ba-3e88-8fc5-834ddcf29cc5 | -3.15341 | -50.37576 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1d2ff00-a58f-35fb-82e9-b2f27cb7179e | -3.15247 | -50.3553 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f0250e4-2dd2-33d2-967d-493da7896b1e | -3.15173 | -50.36022 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7f01b51-db81-3ba3-974e-1c40d0749d40 | -3.15098 | -50.36518 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0da20d-5720-37ab-8efc-6cd8565276b8 | -3.15023 | -50.37017 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8031b7f2-f3be-3e25-bcc5-ec054c7a8442 | -3.14949 | -50.37512 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f31b8d0-5a7f-3633-b348-0083d1557dd5 | -3.14705 | -50.3646 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d4dc245-eba7-3188-a26a-44ef8498695d | -3.14557 | -50.37448 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17c39d98-b631-3f65-a1dd-7537967d0c19 | -3.14482 | -50.37947 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
