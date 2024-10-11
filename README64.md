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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3262a50e-d714-35a5-8aee-2e81f0bbf5b5 | -12.85841 | -53.47303 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8d2c5c98-da12-327b-99b8-4eb913643a32 | -12.85778 | -53.48001 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d21000da-49a9-3980-ad97-67a22fa23c82 | -12.85776 | -53.50136 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db1d40c8-4e02-3226-ac53-c23e35894298 | -12.85772 | -53.47695 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5f4e679f-939b-35f9-bfb9-0a31143f6461 | -12.85767 | -53.45267 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bef8af76-ecd0-3360-a245-7cfde1d00f62 | -12.85718 | -53.45968 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| addbf836-b9e8-37ed-9b4f-2571dd6dc622 | -12.85703 | -53.48087 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7c182107-54f6-3f1d-89b7-098d96238718 | -12.85647 | -53.46358 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a0cfb338-88d1-3199-b87a-181b1aec8c1a | -12.85638 | -53.50928 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d3eccc-3cab-3e00-928c-88b9afb0dd5b | -12.85634 | -53.48787 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 152ec95c-1d42-30ac-8155-2f8ddccacd0c | -12.85634 | -53.48481 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3738c76c-6489-3fb6-9fc9-1175cdeb0dfc | -12.85562 | -53.4918 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f8120e88-4c8f-351d-b596-8d013e0f7dca | -12.85503 | -53.4714 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 94ed1748-94e7-35eb-84e2-93d7532b56ad | -12.85496 | -53.49269 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 12734a7b-c018-3986-958a-966b268ec1e3 | -12.85492 | -53.4683 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 6dd6ba42-0f9d-36ae-882b-d3f81ad98ac1 | -12.85432 | -53.47532 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7d5d6f41-3db1-3f56-bc6f-9d4d16a62abf | -12.85427 | -53.49663 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be734745-5219-324d-a9fc-72483034fc7c | -12.8536 | -53.47923 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 3e4101fa-3316-3cab-92e2-60a2d81abfaa | -12.85354 | -53.47616 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c4898798-7ce7-37c4-80cd-a1750f34476c | -12.8535 | -53.45187 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba5c1509-a05a-36a4-91ec-19e84c133eb5 | -12.85346 | -53.5036 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 784a5290-0207-3262-8d52-8f5ce81df7de | -12.85288 | -53.50452 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1257e672-bac9-38af-8173-87b456b1de92 | -12.85285 | -53.48008 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 4dc469b5-8b53-3022-94d0-c88bd1cc6c15 | -12.85274 | -53.50755 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ebd2c06-785c-3025-9361-2ceca2fa92ba | -12.85219 | -53.50848 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb6117d0-1d9e-3944-8624-07ddbf16968a | -12.85216 | -53.48709 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| fdce18cb-e2cd-3d82-b746-e006ed6c29f3 | -12.85212 | -53.45969 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1c6c2c86-1691-37dc-b6ec-8a6e85bad0e1 | -12.85149 | -53.51245 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 399313ed-84ae-3dc7-8706-f7b715a6bc1e | -12.85144 | -53.49102 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 9c78e2b5-21bb-32fb-9227-b0faf40bd26d | -12.85143 | -53.4636 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| f7e23a2d-b0e4-33ad-92a9-a733500de032 | -12.85077 | -53.4919 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 4363f63e-cfa8-3c73-9b64-81b95e675ddb | -12.85074 | -53.46752 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c7d721b1-d09a-33b2-ae7f-3e652bb5ca88 | -12.85072 | -53.49495 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1356ffbc-fcff-3c6d-950c-9bea72b06194 | -12.85008 | -53.49584 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| afc1ca0e-5d27-3960-8856-7375a8eb6a75 | -12.85005 | -53.47144 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2221b48a-9ca9-34d6-b582-9b7e96317c74 | -12.85 | -53.49888 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| deb4304f-99d4-349a-8dce-9e527fd51ffa | -12.84939 | -53.49979 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7d496a78-a1d1-3f1a-92cd-1819f4f1eb31 | -12.84932 | -53.45111 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3285e6f-14ee-37e6-bb83-7fe4c61ede4f | -12.84869 | -53.50373 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e1c75d8-b753-310f-b1e1-781c37e9e5e2 | -12.84867 | -53.4793 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 4ea5936e-943c-3ffd-a42d-456eb50e4096 | -12.84855 | -53.50677 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ddc1be1-9f07-3bbb-b747-4061267a2132 | -12.84798 | -53.48323 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d6d48bb1-24e7-37bf-9ddc-2f38ef9488b3 | -12.84794 | -53.45891 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e17b3de-6ceb-3ef6-b496-ae1ae35a0f13 | -12.8473 | -53.51166 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0631b335-1c0b-3676-b748-c57e87199b50 | -12.84728 | -53.48717 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 775f1af7-c0b9-3531-9c73-57a2ffc4b9d4 | -12.84725 | -53.46282 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7587bc82-2b53-37b9-8ad4-6c792e7f5786 | -12.84587 | -53.47066 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 103b60a4-6ca8-35f2-99f7-3f86842b6e5c | -12.8452 | -53.49899 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 66438358-642f-359b-b8fc-ab3571cb5369 | -13.02511 | -53.63703 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49644393-919f-3f52-ad62-ae7bbafc7c2a | -13.02019 | -53.64022 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30dbcd35-4038-3ed7-a830-6e8ad1967c68 | -12.96956 | -53.5118 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 665fc772-fef5-3495-b5f8-dad03d6d2666 | -12.96466 | -53.51495 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f846569-658f-3da5-9e60-141e76d47410 | -12.89121 | -53.48637 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 220eae89-227e-3afa-bb6b-0da937a94d5a | -12.88843 | -53.47783 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34a4ac2e-9975-3138-ad88-692f1c08f4c6 | -12.88773 | -53.48172 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e975e49-4cb9-3dfb-970a-027521dd8df7 | -12.88702 | -53.48561 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b732b024-82e7-3ddd-badd-c8d4cf66c1ab | -12.88214 | -53.48871 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e9c7a4a6-fea7-3821-b669-2ac9fe7f3347 | -12.87867 | -53.48399 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a613b77f-dafa-3a6b-ad61-386e337fc6df | -12.87732 | -53.46766 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1a1a9ce-a294-35cb-852c-65e596b9e0aa | -12.87653 | -53.49577 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 484b60a7-975d-36b8-bbbf-bb3eae1de48d | -12.87591 | -53.4754 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46d11224-8b8b-3429-a344-4cd0311149f4 | -12.87527 | -53.4552 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcad2bde-d3ed-3664-bc86-c93042e9d68e | -12.8752 | -53.47928 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a87abdea-8181-30ca-ad4b-d3dab14d1b92 | -12.87385 | -53.46298 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e01e1d-bc65-32b3-9320-f4711cedf576 | -12.87315 | -53.46685 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08c9dc2-bf58-350d-92cb-7bbd814b0352 | -12.87235 | -53.49496 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9ed38f40-817e-31ec-bb37-d3670de68a44 | -12.8718 | -53.45051 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf8e148-668f-36a2-a9e9-ef0b9efff65c | -12.87173 | -53.47459 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72e54d64-f85e-3460-8da1-89bbd970b89a | -12.8711 | -53.45438 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b752439b-4cb6-3483-a25b-b0294f863bc7 | -12.87032 | -53.48239 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1560524c-f2db-3079-b478-54a5681f8e3e | -12.86968 | -53.46215 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44284ad8-96c7-3d14-bb24-4ae3435d871d | -12.86889 | -53.49023 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 499a86d7-693d-3f7a-9328-d8d5869d5c08 | -12.86827 | -53.46991 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a013bf92-7a1b-3853-a221-cf6ed2b246a8 | -12.86817 | -53.49416 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 62741a1e-476c-302e-869f-8ce8818055f3 | -12.86764 | -53.44968 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 718ef28b-d090-3121-9c28-5fe1b007667c | -12.86694 | -53.45354 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d7ae746-aece-3cfd-b531-88e1035e68d3 | -12.86685 | -53.47768 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 93ef4f8e-1f0b-3343-9462-b3505ec75853 | -12.86668 | -53.45044 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51ce6633-ed33-32d6-bf7e-cfe05e44695d | -12.86614 | -53.48159 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4eeb80a2-d8e9-3691-b2df-7735276f0d1a | -12.86552 | -53.46132 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6fe7fa3-8e9d-3ae5-8844-eb7cd6ab136a | -12.86542 | -53.48551 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9122c1b3-b40c-36fc-b04f-0fb390537ab7 | -12.86532 | -53.45822 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24d8fbe6-36cb-3478-9ec6-635b2fb530be | -12.86399 | -53.49337 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a129ea7-824b-373a-9e15-47fb8434c085 | -12.86348 | -53.44884 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bbbcdbe-2cc0-3a57-bd8c-ed2a8503788e | -12.86327 | -53.46994 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d959072d-409a-31a8-8acd-eedc1b0ebad1 | -12.86259 | -53.47384 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 04007d6a-132f-37c7-a7c8-2ce95976c84c | -12.8619 | -53.47774 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 43a4fa35-3c5b-3e1d-9a1a-cda8b64970de | -12.86184 | -53.45348 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1a795fa-2bd2-3ded-9723-0e04dacc6817 | -12.86124 | -53.48473 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c51dca23-cbaf-30dc-b051-9e0a132a6447 | -12.86122 | -53.48166 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 60f4703e-b948-3aca-a13b-7e9625714c49 | -12.86115 | -53.45738 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ad242347-d866-3267-a647-343dfa1b3a5a | -12.86053 | -53.4856 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 9c7dfada-2c75-3698-a64a-617023eadfee | -12.86052 | -53.48865 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 52bde2ce-6b49-3fab-8800-fd0df3cfe222 | -12.86047 | -53.46129 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1043a1b2-da62-3169-b363-b89fce6bb0a4 | -12.85984 | -53.48954 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9c1c7249-7686-36df-8c4a-1beeae0dbcf8 | -12.85978 | -53.46521 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 355411c2-156a-3d08-b2c0-a132ef84555d | -12.87456 | -53.45909 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7ab2583-ddcd-3837-9745-7642fbdb99b3 | -12.87039 | -53.45826 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d21e0c2c-4732-37b1-9d37-b2af58916cca | -12.86623 | -53.45742 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c86de1ed-d0cb-394f-86c1-ce45d8821c29 | -12.866 | -53.45432 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README65.md)
