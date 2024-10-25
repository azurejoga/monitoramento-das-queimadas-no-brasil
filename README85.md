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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e476b18c-cfb6-3892-95c7-2a2a475bef77 | -2.7963 | -49.24487 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2644b0cc-0ea6-3472-9d29-6f662ffac4e2 | -2.79571 | -49.24878 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5fda524-0afd-3dfc-b7e8-62105f519545 | -2.79513 | -49.25268 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 97eac7fd-a350-373f-a85e-73c4b26bc3e4 | -2.76295 | -49.96033 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f353357-c56c-34fc-8f5d-12c2801db1f4 | -2.75162 | -49.3106 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92f9c976-127e-3b1f-bdab-87363aad8131 | -2.73791 | -49.80012 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d22b4c0-85e9-337f-9d91-e6f565b54d42 | -2.68982 | -49.32106 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acbe5371-5127-3317-aa87-178b90aa8f1b | -2.68852 | -49.04764 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af68a8c2-03a0-3a34-9664-a42ace2b22cb | -2.68486 | -49.04297 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942510ac-8663-3de4-ba4e-588fb6ed05df | -2.68424 | -49.047 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d96baed0-22a6-3261-bd2f-44b103aec810 | -2.64029 | -49.24664 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a57c75-4b6b-3c5a-8d89-7585d59259b3 | -2.63668 | -49.2421 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0da6c440-2cff-3dd7-9984-4a83d966d014 | -2.63608 | -49.246 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d4d2e351-a94c-3683-9d20-be8c015dc084 | -2.62442 | -49.09526 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a04e0a80-cd66-352e-8b10-b4b9a3d988d8 | -2.62382 | -49.09923 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1a01ddd5-99bc-340f-93aa-967a8e509cf3 | -2.60194 | -49.09991 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc11f54a-ce77-3b26-8f26-35136f9844dc | -2.59422 | -49.15133 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53552f46-8cee-329c-81f6-422fbae3246d | -2.58547 | -49.2384 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07b05f33-6b6f-35c6-ab24-84fa8282da94 | -2.57124 | -49.27577 | 2024-10-25 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1a2dbc-ddd3-3c0b-840f-e1135b126ee3 | -2.56918 | -49.23192 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6e14d99-53be-3b30-974d-0f10d36ba67d | -2.5686 | -49.23582 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea236c9-4b0d-3f13-af55-ce148cf879ee | -2.54415 | -49.05665 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24157a98-1b63-31e5-a42b-664b29c7eab6 | -2.49047 | -49.03632 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff3a340-f905-39da-b695-c2ffeadf4b5e | -2.47586 | -49.10774 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c8b5401-dc37-34f6-aa9f-34e41459f0f9 | -2.47553 | -49.1073 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91deb07a-4621-3f7f-9365-d0e916c693b9 | -2.47223 | -49.10317 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6500fd9f-34b1-3e5f-90a6-ec41432c4dd6 | -2.47187 | -49.1027 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e0e0011-c9a3-3c8d-8002-ec954c3d5ee1 | -2.47129 | -49.10665 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de782ce-42cc-3289-b38c-e4f165eb9bdc | -2.46798 | -49.10252 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71340573-d912-3661-be2e-a7ac673c330f | -2.46763 | -49.10203 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 023a1e6e-a694-3342-8549-0245a66f6eb3 | -2.46736 | -49.10647 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ec74f56-e669-33dd-98b8-44c1526a05b3 | -2.46704 | -49.10599 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f51036-7ed2-33be-a73e-04d01742884b | -2.38524 | -49.38654 | 2024-10-25 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58cbdb7f-1abd-3c80-af65-8321b5abbdc0 | -2.35534 | -48.9353 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3680d121-9b9e-3e94-a8b6-efc86e058a9c | -2.35472 | -48.93933 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3e85b22-19c4-3baa-99dd-712433b49293 | -3.07294 | -50.4962 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 415d0174-475f-3970-8ef5-cd6c4b7379dd | -3.07219 | -50.50114 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4367901a-5583-3f62-839e-df267a6cd31c | -3.07143 | -50.50608 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89b46f12-1271-35fb-9961-2753ac484bb1 | -3.06903 | -50.49561 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d21236e-cfa5-3d05-9853-cab7f59194d0 | -3.06828 | -50.50055 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc785a9b-a71a-3a1d-a5f1-172c918660e0 | -3.04411 | -50.26884 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963a8fd2-c434-39c1-8617-7343b1f4d570 | -3.04332 | -50.27394 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d81d281-9e7e-3f03-82e0-12f88a007836 | -3.04249 | -50.27055 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98b9f12c-eeb0-3ad4-8989-cdd5922f4234 | -2.98713 | -50.29684 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abaca49b-7241-34cf-b662-cd5c8fa97908 | -2.98318 | -50.2962 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1958f0ff-1e8a-34c1-a3f7-5333bf9d8cf6 | -2.96876 | -50.41743 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91e3b7d0-b4e7-31b4-93ce-eb0ec87f36b0 | -2.968 | -50.42242 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf095ebe-ebec-3bab-a9b7-457d63411290 | -2.96725 | -50.42739 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d56fcced-d4ab-3715-a97f-5426cc1e6275 | -2.96484 | -50.41683 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70173a84-4460-3e75-9c4d-33db4b845b86 | -2.96408 | -50.42182 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10b0c029-a2e1-30ad-a367-1e9004617681 | -2.96332 | -50.4268 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 252fc934-2df1-30f1-af26-c4e9a6a344af | -2.96257 | -50.43177 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6688ee65-b20f-3689-b3c1-2a6b5fc45daf | -2.96092 | -50.41624 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 628842fc-55a6-35cf-8765-bb98317a9540 | -2.96073 | -50.52241 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 975a3b05-97ab-3f75-9cab-316d01526b0d | -2.96016 | -50.42122 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2f616af-7c84-3ffe-bce5-1bf0ce7c88aa | -2.95998 | -50.52731 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaf390c9-4a7a-317c-8c80-f552ef6b76a9 | -2.9594 | -50.4262 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 82cb9d04-0243-35d5-9fba-78d926ba4520 | -2.95923 | -50.53221 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16626736-81d8-34d4-ac81-6a033f38d0d2 | -2.95865 | -50.43117 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86bb6e54-c431-3dd0-88f2-59fa20e32e45 | -2.95835 | -50.51194 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8adf899d-9313-32c6-845f-45e524839c51 | -2.95684 | -50.52182 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6085c70c-2d9e-3de2-a952-3dff74c630c2 | -2.95624 | -50.42062 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78f25ddf-0251-3e5d-849f-87511d233732 | -2.95609 | -50.52673 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39ea763c-81c4-377f-9e16-9a0a5b353247 | -2.95549 | -50.4256 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec3b7ca9-16f4-3084-9385-2bca7e99dc27 | -2.95294 | -50.52122 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b05f6f3-1497-3023-aa14-9c3bbc19f3b8 | -2.95219 | -50.52613 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c00e6e7e-a102-3d7b-9911-9492b6a0224c | -2.95144 | -50.53104 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7dfe945-fd6d-311b-9e25-4f8b22911519 | -2.68779 | -49.82922 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a557f200-31cc-32b8-9e65-2c96dde88c00 | -2.68761 | -49.82944 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b1797d5-24f0-3732-9bff-47b0bf4c5429 | -2.65349 | -49.83527 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af19b9c3-eb1b-3431-94fe-21d76ed17e1c | -2.64612 | -49.98931 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf9ed607-0615-35af-8a8c-080a147b6f24 | -2.64211 | -49.98872 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0be2048e-ae5d-302c-a231-1ab3df8daed2 | -2.6306 | -49.98343 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1be5de33-9624-3b36-ba76-c6f79ea584a3 | -2.62605 | -49.98631 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5ba2ef-be48-3119-aab5-87308f4b4bd9 | -2.62407 | -49.7832 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2c42e73c-4ce4-33ee-a624-a3e58c987df7 | -2.62257 | -49.98222 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19aee8ce-6541-352a-b568-8f8eb40ff30c | -2.62 | -49.78258 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6cf623d-7f13-3b8a-889c-5996498d5753 | -2.4451 | -50.37798 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60e8ed27-97c7-3670-9fed-5dade71dda73 | -2.43767 | -50.29582 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cf8aa9b-ffcc-3602-a4d0-be0044fbff07 | -2.42044 | -49.8081 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a425a4d4-9dd7-34f6-bf14-461c455a7bf6 | -2.41644 | -50.40878 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db2fa661-3f5f-3e42-afbf-a90eea722e8c | -2.41584 | -49.81107 | 2024-10-25 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 251019a6-3699-352f-9324-6ac26d919a32 | -2.41255 | -50.40819 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7deb69cf-f614-35f6-a8a3-d5c8a7304051 | -2.40716 | -50.41739 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38fd8544-cb9d-31e4-8a77-425530c4844f | -2.11987 | -50.14454 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f7db0765-80ba-3674-8ff2-bd2590a49f19 | -2.1191 | -50.14957 | 2024-10-25 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 41174dd8-ac52-324a-aa9b-08733a42d8f1 | -3.60546 | -50.58205 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f48fe335-2db5-3d99-a389-baa5f7428c05 | -3.60154 | -50.58151 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b480045-c58e-347a-851e-2dcfb6bf1ee2 | -5.00144 | -49.78819 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e1588c-efdc-3c5f-a62b-a2ce1cf99dc1 | -4.97364 | -49.77216 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad471c54-6b32-3189-8cb9-6c8a4c301b92 | -4.96942 | -49.77151 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 370f08a1-fc1e-36e9-87e2-378344da4add | -4.96896 | -49.77176 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9711c00a-b0a1-35e0-bd34-656a942d21a5 | -4.95293 | -49.6488 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0fc8b85-28ec-3b6a-9fb4-38ccb28cf0c8 | -4.91699 | -49.83121 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7bf4457a-5b03-3fb0-9fcc-27d11a772d0d | -4.91641 | -49.83509 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4fd5b52d-1aa5-3f16-b92f-07c98320fd86 | -4.9128 | -49.83053 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec7e2778-995f-3d54-b3b4-95b2d29f6745 | -4.91222 | -49.8344 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da7ba70b-d823-3f17-822e-606c99704682 | -4.5865 | -49.49537 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d93a25a4-4761-36c3-b601-962a801364d4 | -4.58283 | -49.49059 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b4b02fa-86a7-3189-8b5c-5eb96534ef1c | -4.58224 | -49.49464 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README86.md)
