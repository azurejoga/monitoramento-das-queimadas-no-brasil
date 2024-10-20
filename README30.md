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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaf8a3f7-9c5d-34bf-bb9a-def3b83a36c1 | -2.2639 | -51.24518 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1b1487b-29f4-3b21-951b-2675fb02e11a | -2.21967 | -51.88613 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1125ef-66b7-3781-ac18-31518b9d57cd | -3.20707 | -51.02064 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32038285-77cb-3a98-a3a1-4d05429a0705 | -3.20328 | -51.02 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57f01f6c-9ec2-3695-bede-6b4a3ca8631c | -3.16635 | -51.25434 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b40944f-572b-3e84-9372-227338ca30be | -3.15779 | -51.0365 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f385a0-4af1-34b2-80cd-ad254f61cda8 | -3.15399 | -51.03586 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d59132c2-b010-3176-bc91-2e7f4662fb67 | -3.1483 | -51.14471 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28a30fff-edd8-3894-89ca-ba88855b07e1 | -3.12799 | -51.34644 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9643f9e-fd51-3a9f-9e22-a5cb8a9f5cab | -3.12412 | -51.34575 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa4078b6-5eb9-397f-a0cd-2cfbc9f830be | -3.09242 | -51.22273 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dded7f0-72c5-30f4-9aae-bca65531eebc | -3.08934 | -51.21739 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71a5e2c1-e3c3-32b2-ad70-7272d9fabebf | -3.08857 | -51.22212 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1b98e5d-6e33-3400-903d-b9b06852bdbd | -3.08625 | -51.2121 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21e49037-1b7f-3144-a5c6-c8feed65d96f | -3.08549 | -51.21679 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 004fc326-cebc-311f-a5cb-d35730d31df9 | -3.08164 | -51.21616 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00071fc4-65bf-3c53-a19f-a31248c20789 | -3.0778 | -51.21553 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15fe42b9-08d3-3360-8fc0-bcc8fd9ddc2c | -3.07619 | -51.24953 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6773b34c-83ae-30c7-bc87-ad2cfd514f5e | -3.06648 | -51.05256 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00c4a9c5-cda1-375d-9ac3-99ca35430381 | -3.05505 | -51.05069 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1a07ed6-cdb0-31a3-af5e-69fa40ca28e0 | -3.05198 | -51.04543 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f808872-a774-3efc-b0f1-f8839fd395ff | -3.05093 | -50.97894 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca4ca74e-7813-322d-a625-02ca5935ec41 | -3.05019 | -50.98355 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dc14dee-2caf-34b4-a24a-35ca89f37cfb | -3.04427 | -51.02042 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 8831fbf9-e725-3070-a3e3-c255372eab61 | -3.04353 | -51.02505 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 03423d86-2e54-3fd4-8f2f-5e1ee43ee043 | -3.04046 | -51.01985 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c48aa58a-1af2-3846-a766-390deac82e57 | -3.03972 | -51.02447 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 17d3d0c6-a2be-3ff8-9d56-75d81a201d8b | -3.03665 | -51.01924 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d36a74a-3672-38a9-8294-45e20c397e9a | -2.9872 | -51.03506 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d4b7049-2f82-3d9f-864f-3875d0ddfe35 | -2.98539 | -51.03188 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf0143cd-9fe9-3058-8402-2cf1d04ee19b | -2.98339 | -51.03446 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21cf0d0f-01b0-3bf7-ab7b-6d3eae83ae0f | 1.11656 | -52.57677 | 2024-10-20 04:29:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077e1517-d0ef-38b7-949f-edc0cbdc3665 | 1.01116 | -52.2186 | 2024-10-20 04:29:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b86743ba-33a9-3440-87b1-300e585f3dd7 | 1.00677 | -52.21915 | 2024-10-20 04:29:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14f3c4cd-86ff-3d8e-87c2-c99f5dcb8290 | 0.65669 | -51.87326 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a56273b7-a73a-3136-b9d9-7f81317e12ec | 0.65609 | -51.86935 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ada54cc4-210a-3682-a6ff-05006e929927 | 0.65548 | -51.86549 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 102b5b47-57c1-3c9c-87db-a60e2a19ff07 | 0.65245 | -51.87389 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d8e368e-2920-31b5-865e-1a0ce5e29fd2 | 0.65184 | -51.86999 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc5acad-709c-3645-87cc-5d9a235a251d | 0.65124 | -51.86613 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a9b343-6a91-31f1-a65c-87e1a0f3b72a | 0.64821 | -51.87458 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e88cd359-761f-3a10-ad2e-b82e7ea5b1ea | 0.647 | -51.86682 | 2024-10-20 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7528734-9b93-3ab4-ac74-1e1b317e16a5 | -0.23523 | -51.52416 | 2024-10-20 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec36d667-9611-3bcd-95df-b7129bf1fce0 | -0.23466 | -51.52778 | 2024-10-20 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8222617-b809-365b-a51b-cbe3295bf689 | -0.23114 | -51.52354 | 2024-10-20 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a9c9c6-a95b-3c32-8d12-f1a5cb48bfb9 | -0.23056 | -51.52716 | 2024-10-20 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd9b6af3-a48e-3e55-8718-68c640ad2c03 | -2.04541 | -52.70028 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf364b00-8be9-3058-8bfb-134b1bbb9068 | -1.05635 | -53.01604 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1debc86e-1b4a-3fb7-a629-427792ea612b | -1.79017 | -52.05347 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c3373f4-b89f-3e30-8fb3-65c6469753c8 | -1.78957 | -52.05722 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a74c369f-279c-3987-a53b-36d47b2db7b4 | -1.78603 | -52.05278 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e19bc93e-e32f-3f30-8363-790426b47694 | -1.78543 | -52.05654 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 137120c3-0488-34e4-8fb4-433d66496578 | -1.70751 | -52.54163 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 372bf29e-a8d9-39b6-826a-1d566eb1def4 | -1.70687 | -52.54565 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ae0d4b3-4dfa-326c-bd6b-4ccdc8b51bd2 | -1.70323 | -52.54094 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09860d16-8d6b-32b4-9566-4770edfb3186 | -1.70258 | -52.54496 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fc4dd1e-3524-31be-b863-f4d697c3e030 | -1.66017 | -52.0602 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983a2815-a038-3fb3-b031-0920dbeb5e28 | -1.65662 | -52.05583 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43b9dce2-ff90-337a-b5ce-472c2995047a | -1.65601 | -52.05957 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d29df7a-9f55-3598-9667-21269fb7bc24 | -1.65247 | -52.05518 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f75da5d-acc5-3f18-926c-50f818ea70f9 | -1.54181 | -51.96598 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32ad727b-bbf4-37e6-a778-f6b7ebc6e795 | -1.54121 | -51.96968 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51a6a5cb-c02f-3790-b8de-4373258a3796 | -1.54055 | -51.96284 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a497be-e97e-315a-8c8a-bc44b6874451 | -1.53998 | -51.96653 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b5411a9-b7e8-39b2-b24b-2a0c5d135a7b | -1.53597 | -51.94993 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e81f6c05-cff4-3ed0-afd7-a6a1852e353a | -1.53402 | -51.95045 | 2024-10-20 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60f0b2aa-3835-3349-8088-fe925c7b6dfb | -1.48506 | -52.75142 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c8994b-23f0-3ef0-b2ef-42bfbb105f92 | -1.44592 | -52.2654 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faf6cbdb-4dd6-3e2c-82d0-5b8d2eb2d8fd | -1.41753 | -52.67241 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 979f71aa-744e-3b86-8d88-7e6711543a81 | -1.35797 | -52.2751 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 979ba0ef-16fd-39dc-a39b-09bc3185b847 | -1.35735 | -52.279 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c62fb11e-1e9f-3a7a-a332-9d4b33443674 | -1.3549 | -52.29459 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac9d2bd-6849-30e6-9667-dc3d1f1285f5 | -1.35128 | -52.29001 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8af221-6260-3c11-b1de-d285356e9437 | -1.35067 | -52.29391 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae95f57-8777-3481-b26f-b7b542aa40ab | -1.22879 | -52.64387 | 2024-10-20 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb416af-f2ef-3314-a1b2-a4c347d509ae | -1.12775 | -52.14928 | 2024-10-20 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e70bd993-0a06-368b-a36a-0b588bbe7a1a | -0.9528 | -52.37951 | 2024-10-20 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a45c4b41-8d8c-3062-832c-bffa89b68feb | -2.01171 | -52.2851 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f8dd2a4-d551-33c3-bd8f-c92277aca15c | -1.98988 | -52.12708 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae0a33f2-6954-3f69-b8cf-22dae815dedc | -1.98928 | -52.13082 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0182c2b-8362-34d4-879c-834c404587e8 | -2.73426 | -52.57272 | 2024-10-20 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12c239d3-aacf-3fc2-9ccc-dc432423774b | -2.73366 | -52.57244 | 2024-10-20 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6d0e43d-1df9-3be7-af07-6100e27f620a | -2.6933 | -52.06819 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 49e1868a-c05e-369d-be70-8851cb79e0b7 | -2.68921 | -52.06756 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a2de3595-6c13-3751-83e8-85d966591b9a | -2.68863 | -52.07121 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6e4be453-8687-3d9c-b1e0-670463057cf2 | -2.79224 | -52.92438 | 2024-10-20 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1032bb97-e7ff-3c67-b12f-e255543d1dfc | -2.30262 | -52.19794 | 2024-10-20 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a177a59-cb01-317d-991e-141047aca8c8 | -2.21402 | -53.70119 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2680e852-3084-322a-b4d5-6373d16d8c16 | -2.08956 | -53.57298 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb7fa04d-f3cd-3443-a8f4-580092c290a3 | -1.9092 | -54.59491 | 2024-10-20 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1270b86c-031f-3066-b577-3d841cb5b885 | -1.90429 | -54.59404 | 2024-10-20 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57233de-85be-3eed-be3b-19409d70f8fb | -1.17221 | -53.65648 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 79c0ae15-b408-3474-be10-15701978a33c | -1.17143 | -53.66129 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3a6f3a58-5259-3074-ab9b-852352edf945 | -1.1701 | -53.65294 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28321764-7c76-37d9-a69e-776159ff6abb | -1.16936 | -53.65771 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ebd0d191-6a5a-330e-b53d-f3cc0200eac4 | -1.16861 | -53.66251 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a82118c9-2682-3976-9495-01f4d65f3660 | -1.16758 | -53.65554 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8cc80839-a06f-3ca9-b7f7-f71b8cbeb0c5 | -1.1668 | -53.66032 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6e785489-e5de-399f-889f-8601af6813f2 | -1.16547 | -53.65195 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0275a1ee-0982-3bad-8f50-df74e58140b4 | -1.16474 | -53.65664 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README31.md)
