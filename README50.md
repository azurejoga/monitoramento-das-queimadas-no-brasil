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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f233c54-9d17-3ae7-a677-e636ca4c2dfc | -3.95119 | -46.36872 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd7a6a7a-6845-37a1-bab9-4c801b6a601c | -2.05325 | -52.6674 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c91e2e10-069b-36fc-9332-9c57ddb3e084 | -3.67705 | -52.26281 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b1bedc-23c0-3d04-9383-2a36156bbf6e | -3.01696 | -48.06257 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac5e6284-3b0f-3794-b720-b181f08ce992 | -2.71675 | -46.67565 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4de22e9e-6234-30eb-b581-a94e9dbe5e14 | -3.5452 | -47.38231 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 64b4b255-a4ca-39c4-99de-1c12f9d28d85 | -4.78748 | -48.90501 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 079687b5-9010-3498-8374-ad1baab262d5 | -3.7988 | -44.03696 | 2024-11-06 04:36:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 373ce497-1e72-37d7-9afd-c7eda7a493d0 | -3.70674 | -48.99227 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e9dab5b-7d56-33bd-adca-0efd4ce4bdb3 | -0.96681 | -47.80988 | 2024-11-06 04:36:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b2a5afb0-47e8-3e5d-9b55-b95e2f3f6512 | -2.36803 | -49.03543 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b303a89f-fc8b-3c3e-ae87-116d81b9ad66 | 0.1826 | -51.06741 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 001e69cb-71f4-30fc-8785-20e0f4a89963 | -2.87984 | -51.61884 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 232f8af7-dcd4-34cf-a6a4-80301b752e6d | -4.55656 | -48.01228 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c558f3e9-ae84-3bdc-ad65-26ee73592488 | -2.65967 | -48.56411 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5998755-7328-30b6-86eb-d3f43781369f | -2.60691 | -48.20718 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0d334dd-c08a-38ee-aaf8-32a4dc68dba9 | -3.86806 | -46.43663 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce34ee74-168f-393e-a2ae-d3026354eee9 | -3.63553 | -52.33723 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aff70921-8711-3cbe-b6ee-beb78b556a88 | -3.60366 | -42.86506 | 2024-11-06 04:36:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a226107-3a9d-3aac-bad8-8402378954f7 | -3.36382 | -51.8531 | 2024-11-06 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e654c298-4e52-3a4d-b692-4329c564d99e | -3.58685 | -50.26752 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 680f344e-fbc3-3995-8e7b-6c21d46c16ad | -4.14261 | -42.22713 | 2024-11-06 04:36:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4e3a3916-2100-367d-a716-2108fdabb7b1 | -2.84289 | -49.47154 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 44c821e8-6314-346c-acce-cd7a4119796c | -2.87882 | -51.30349 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2b0189e-4c27-3d83-bc06-16551694e608 | -4.13813 | -43.57679 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2e0f6025-9f11-3e0d-8ca3-b6eda8f8f99f | -4.16861 | -45.62938 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ef98e44-d353-302f-b86f-72bc6070f0b6 | -3.18266 | -50.58361 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27360fb7-8e48-30e3-9762-2de0c13a4dbb | -3.45013 | -50.37904 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 497511eb-cbca-31dd-8fab-74fddc9d8f09 | -2.88415 | -48.62706 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32edf172-4dd6-3f19-a0f7-c3a5c15d04a2 | -4.26889 | -50.72205 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db3a94bf-9298-3617-a348-a6c28031584a | -3.293 | -50.02054 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a47cd22-8d78-37a4-b872-87cc849a4c35 | -2.91924 | -48.05798 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a73a7b1a-cfaa-33a9-b3e2-c7e2e29cdc59 | -3.42435 | -51.53934 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 684ca75c-2993-36ba-aaf3-a9c11cda9820 | -4.02039 | -48.29338 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f9c23af-0e8d-3d60-90a3-0db08cf32232 | -2.65253 | -48.56652 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59d0f33d-52c1-3028-8daf-f4f6a65a8bac | -3.0891 | -51.12359 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8835da5f-93d0-35b2-bf29-97a82c9c8beb | -2.62293 | -51.73148 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 130754a2-3d4b-3395-b9e9-d6661e7a3482 | -3.12759 | -51.10598 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57deb35c-7f47-3bd9-ac4d-838ad4719aeb | -2.94163 | -54.8018 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f79d8d0-9742-3126-851a-4bfa3356e9bc | -2.7469 | -48.72187 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12859b90-3ab8-36f8-aa7a-03a3f3117461 | -2.82488 | -49.78071 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 74d17aed-e495-3b3c-beb8-f63669f9735e | -3.40774 | -50.28726 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2211fe6f-8c4e-3257-ae37-bed208c810f0 | -3.97689 | -48.15872 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe6cfbe-cc4d-343d-90b0-a9478626c88b | -3.52359 | -51.6686 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c660360a-89f1-3219-b03d-221931b0cc06 | -1.23999 | -51.76385 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 659e2fd4-0347-3a0a-a873-45fd5eb9dab4 | -3.80091 | -51.94213 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 281a1d96-021d-347b-a27a-22235a42c926 | -2.54338 | -47.37803 | 2024-11-06 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53c0d5e0-57a8-30dc-9c94-9e2eb3659613 | -2.87405 | -51.31079 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d581036-e6af-3ffa-b91f-e67c1ded061a | -3.43067 | -51.43067 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac668200-dc82-3ab0-95d6-c392eefc1586 | -2.44978 | -49.03413 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34f9194a-6dfd-3fa0-ae7d-07e88c46c23e | -3.65277 | -50.25542 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f44a106-dc22-3d54-a6a6-17b2ca8e764e | -3.16135 | -50.20813 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 20007403-f12f-3dad-86d3-2fdb54d4bd61 | -4.03365 | -48.29541 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c36b3c5-b8ad-3744-919e-58539b36cd83 | -3.75798 | -47.60039 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c31d2bfa-31fe-3fd8-a58d-6480948d92da | -3.30747 | -50.10298 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93aed33b-0a89-359b-ad08-9f16586dd581 | -2.47015 | -48.06239 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ba61416-60aa-302f-9bbd-8675949fa758 | -2.75715 | -53.22327 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4efd1387-a1be-3bd3-8529-6e62e2df39a3 | -2.30725 | -46.73872 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 995a6cd9-3469-38ee-90f9-e86c63be3d7a | -4.42194 | -45.98307 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eadc9309-b329-3c2c-9d37-1a672ae4dad3 | -4.4651 | -50.6595 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5885a26d-46e4-3d84-b939-996062460aa0 | -2.8535 | -49.53385 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844e1dbd-f5cf-3c3f-afca-0ce06ed293df | -2.83645 | -48.67237 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f443bfb8-12ee-3e85-a34b-aaa7234dd8e3 | -2.92224 | -49.11877 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98bb9dcb-6594-3b22-a1bf-5c09765b54f3 | -3.31136 | -50.1438 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5a31e77-04e0-3c1c-b345-e8fb2f75ceb6 | -2.81063 | -51.8013 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b18aacd-b6b1-3d81-9148-cd1313b9996c | -3.39803 | -53.68825 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 889d15c8-ed35-3ddf-923e-9bab124542d4 | -3.11491 | -53.71646 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40456e5a-3927-3347-bf3f-5946feb1a86d | -2.81912 | -52.93875 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 95a89dca-8f5b-334f-a08a-f3673dcdcb25 | -3.97465 | -48.15126 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17674d43-ebcb-34e6-bd68-030ac9ca29b5 | -3.52936 | -40.91365 | 2024-11-06 04:36:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b6e8317-f148-3b86-846e-bec69a3ece3f | -3.76696 | -51.77457 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e9277a-b214-3513-b45a-f0f5d150e8c2 | -2.45478 | -50.39648 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9536f72-fdc7-3b9b-b7bb-c54be497b557 | -3.7409 | -50.06879 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 59386596-0b79-341d-ba8a-74701d0bffa6 | -2.78281 | -51.60767 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 868d1c0d-2b8f-353a-9aa4-460c3c547459 | -2.59888 | -49.27365 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21ffbfac-23c1-38c9-be8d-3ace634b3b32 | -2.8001 | -51.47816 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33748e60-6ae4-33b5-9429-c7c387b417f0 | -3.15855 | -50.20401 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2acdc710-48e0-3a04-8064-060f59ed6258 | -3.27794 | -51.27915 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 463c256e-3f3c-3720-bf81-77684cef1347 | -3.21851 | -53.10505 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99bc21d4-d253-319e-aee5-f3284c67937c | -4.12748 | -46.90983 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df12bb0-8b6d-3bb9-88bd-eaabff5aab7f | -2.97443 | -51.0271 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 170070b7-b2c2-3444-9a81-2eedef1f3c75 | -3.66685 | -50.23198 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b06db5c8-b73d-33fc-ab1d-05cc2282bb83 | -3.91268 | -47.95973 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89f6f723-6e18-3399-babd-dc31fc7bb8d5 | -2.40008 | -47.81443 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8f85fe2-11f0-3e86-94c0-3956044a893d | -4.08239 | -53.79644 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43d5f4be-4ee4-3c21-84c6-386eac4f6d1b | -3.29183 | -53.11692 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3339ca9d-8dd6-33b2-b62d-ef1774d19dc7 | -2.47014 | -50.23448 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6233343f-6bf9-39a0-918d-28d244d70035 | -2.77924 | -51.60711 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1459aba4-6fef-308e-9beb-d02df4c739c6 | -3.75379 | -44.56458 | 2024-11-06 04:36:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78130682-cb82-33ce-89a0-2f6cd6f81a0e | -3.09282 | -50.26086 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 222cbcda-e871-3bde-945e-ae14c29b6bf5 | -2.89304 | -49.36909 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db4040fd-67c3-3aa5-be58-29cf664a0428 | -3.59094 | -50.17659 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fc34eae-5fd1-33bc-b477-b35f8ea6e8a9 | -2.66243 | -48.56806 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f951549-f4c3-3cf3-a574-af567901944a | -3.95604 | -48.35777 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf0919e6-d019-3b7d-93c4-6ac371c20ee5 | -3.24689 | -53.40212 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad3ce75e-f224-3088-9a12-82780e0b6f6b | -2.58058 | -54.00552 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58eddb4-75cd-3fad-9528-5548a62f56eb | -2.91895 | -51.05112 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dad75847-4cdb-3536-9b6e-b342c18ec651 | -2.30952 | -50.67073 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 33e8942f-9d46-388d-b7e8-16eb5491c8eb | -2.95095 | -54.79923 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 344bcab7-2b57-34f6-8f0d-c133664f33cb | -4.10976 | -50.75306 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README51.md)
