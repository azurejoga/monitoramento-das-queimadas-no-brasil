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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07516332-8c16-3fc4-8674-995372ebff57 | -1.78402 | -55.02745 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a0597e-a6a7-37d1-a6ec-5d6a237cc903 | -1.82193 | -55.08648 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc2cc176-9bfc-324e-a544-534be041c84e | -0.99722 | -53.73795 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c56d11a-5f1f-3a21-b1fe-f68d41a3d1b2 | -1.52328 | -54.81799 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb33fbcd-8450-3ba8-bf57-c5b8857c51f2 | -1.49675 | -55.66315 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5da9e468-6d32-3b9e-a4a5-cf7510a3aad9 | 3.74174 | -51.61863 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b699e77-4057-3d20-9afb-d3487743b325 | -3.20886 | -50.55007 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1722bb5b-eda7-3215-be66-c1de423330ef | 1.32353 | -50.84753 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd5e787e-0000-30f8-80e2-23d19d5711fa | -1.50175 | -54.82801 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 946d1fea-ede5-366c-9d72-fa7a293c55c1 | -3.17037 | -50.59663 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bba8a22c-8cbd-3d35-8b82-e23925ca5be1 | -3.17446 | -50.5974 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7862e041-5ebe-331f-84df-f7bf136af172 | 1.32912 | -50.83941 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29d0b248-78c5-3f6d-b513-68ca26f0e82c | -3.10658 | -51.24601 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7f4353-d9fa-3d1a-84bb-e6545188be97 | -3.14075 | -51.02837 | 2026-10-08 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb31b7f-59e0-3dec-99cf-46f96967f093 | 0.93961 | -50.19839 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da07b69c-b7f8-357c-9e2f-6f49b573d971 | -3.2045 | -50.55642 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| acffcc2c-49c4-3aa5-af99-bec836e32d38 | -1.5327 | -54.55391 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 41c80391-d810-3232-b0a4-bc516eca841f | -3.18019 | -50.44725 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e107e74a-2abb-3ee4-8798-5db2cc98c476 | -3.19906 | -50.56961 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd6e70eb-8289-36e7-a7f5-3fc8b215737a | -1.11067 | -54.15187 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64a5ad41-cbae-3ff2-a97f-a9142286e285 | -3.1769 | -50.44675 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ccb174-b8dc-39fa-b677-a384fc48a078 | -2.35785 | -48.88496 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d166f78-5ab1-3340-983d-132c4ef97ec6 | -1.97627 | -56.06193 | 2026-10-08 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 508d965c-6bda-3989-a8e6-f9a220139004 | 0.94346 | -50.20133 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e558c2-9a6d-317e-a626-dc28b04a6ea7 | -3.18142 | -50.55286 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc660131-ac67-387d-ac8e-eb59d999c4e4 | -3.1147 | -50.28273 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84fd2867-dd63-3705-8825-71490fd9d391 | -1.52613 | -54.80085 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dfad7ef-4e45-3eaa-8b31-9c450ebe6ab3 | -3.18909 | -50.54702 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67b6cd2e-007b-3fc2-8f02-c13a1dab4ce2 | -0.85377 | -51.85361 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feb8cf93-4111-3272-bca5-d69089b6be10 | -1.76705 | -55.03173 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 515f9ae2-ee50-3444-9812-5ff5875303bb | -3.17875 | -50.56999 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e130d842-e098-3ce6-adf2-9e86481dc500 | -1.19905 | -54.20636 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d19e2055-3685-33a5-8f4c-b0729a7d8f65 | -3.20289 | -50.56669 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a39f9254-1cda-398f-8582-3a05f41e3ffe | -3.16095 | -50.44078 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf29d25d-9a2b-3a76-9bf9-15b4a9aad5a8 | -3.20503 | -50.55299 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 06dc4345-1b33-3e0c-840c-4f69373d7085 | -3.1369 | -51.0313 | 2026-10-08 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4476e19b-aef1-373e-9f8e-6dd1547ce578 | -3.16708 | -50.59612 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03846d5c-b682-3779-9f8a-f45545b058fd | -3.27531 | -50.03662 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce25b0c-05c7-3925-8b08-39bf94558b07 | -1.20525 | -47.7793 | 2026-10-08 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 164a2319-74f1-3b8d-aaf3-4344e6234d0d | -3.19898 | -50.54854 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fffc8ed1-2cfe-37b5-836c-00cd4a4fba47 | -0.99655 | -53.74227 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ffd237-12f0-3374-bc90-af57323a0973 | -1.42289 | -54.61272 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97473cfc-d118-310a-bba3-b0689341a279 | -2.04603 | -56.37864 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cae0f0c-6125-37c4-a8c4-d9a8b6bea33e | -2.10341 | -52.06022 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf05a8fe-3f0d-3ca7-a399-fb790ee641df | 2.12528 | -50.82267 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d9b2a68-f7c0-35a2-8310-2ee53ab8f2bf | -1.54044 | -54.55509 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 103c5b02-f626-3c7f-8712-8c9139558c91 | 1.77331 | -55.54274 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a45adba0-acca-361c-b7fb-55a67e23c075 | -2.74297 | -48.4305 | 2026-10-08 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36a36b5c-d28e-32da-9038-5ee09d2998d5 | 2.02194 | -50.76881 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae4b4d99-7b54-3329-b404-b04b16f3a922 | -2.78611 | -51.67986 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57fa156e-6582-3a7e-9265-c0934be1ad53 | -2.10565 | -52.06807 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dc75f6e-ce90-3f1b-86fd-b182559b9bf3 | -2.79058 | -51.67331 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b5b0555-13c7-38e6-8c6b-6824de8ea669 | -3.15053 | -50.44268 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a39be4df-f595-3889-b2fa-56301f236c7e | -1.73863 | -53.64874 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 791cb473-c657-3899-8ab2-fa657a19c45a | -3.01686 | -51.01616 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92939289-d63b-3758-aa0e-521cbe141dc0 | 1.34593 | -56.13627 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c386254-1262-3f2c-b306-aa51fe0bf47b | 3.53966 | -51.2762 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7bce75-03cf-3b05-bd2b-178f25dfbba8 | 0.56666 | -50.79802 | 2026-10-08 04:44:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f70b1a3d-136d-3aeb-904a-3514edbeb58a | -3.20672 | -50.56377 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9d05ff6-bde4-3ec8-abd9-0309a34d6f4a | 0.79299 | -59.19791 | 2026-10-08 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4927da4-923e-3673-975f-33fdbfa5d53f | -3.17137 | -50.43888 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d9657d-d81f-3ff9-86f5-3faf9a8718f7 | -1.18048 | -50.52682 | 2026-10-08 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ac9072c-c2cb-36f9-bf80-df209935b656 | -2.69006 | -49.04887 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707bc7f6-1cdc-3eec-81fa-bb1b271076d8 | 1.31403 | -50.85262 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66c9c24-a668-3933-8d5e-1ddac86f3e75 | -1.97562 | -56.06588 | 2026-10-08 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df1f2b24-e409-3283-86f6-382215e2a1c5 | -3.16654 | -50.59955 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9276984-9854-3cc7-9b12-7b87a8702ca6 | -1.21469 | -55.64316 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170cdbeb-666f-3433-95de-f061cd3db237 | -2.99382 | -51.055 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0389bc94-44f6-327b-9c2b-81d5bb5b23a6 | -3.25984 | -50.39649 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 712cfdd0-9228-3568-809f-d441ba979972 | -3.17733 | -50.55209 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0498e5b1-fe24-3237-b744-b2a4b72b3bf5 | -2.8121 | -49.11838 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c4e0de-ff9b-3eea-9259-51ce499a146f | -2.12525 | -54.80247 | 2026-10-08 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4e9b228-f0fc-383e-930b-9fa048da8650 | -3.18917 | -50.56808 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98e0b5e7-df0e-3c45-93ec-f59c54771e01 | -2.56865 | -50.68125 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d26246e-95fb-32a7-a08a-b656c5ed6c24 | -2.18871 | -48.24839 | 2026-10-08 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d223a29-3147-3a47-b727-d494f27c61fa | -2.37332 | -56.13014 | 2026-10-08 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb4a320b-61b7-39d1-90bc-2c59ac01c575 | -1.82016 | -55.22474 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07913c70-3e4c-319f-a9b6-31dfb19176ba | -2.98099 | -51.24432 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56f143a4-0a46-3993-a278-c4d4b1c892ed | -1.41019 | -55.41376 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c74cd25-3147-3ba4-ac39-fd14ae439fa0 | -0.41491 | -52.03316 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c0a5bb9-239d-34ca-b157-eee85a163768 | 0.94292 | -50.19788 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da25942a-cca7-3ee8-b70b-6341c74fd388 | -1.45943 | -54.76439 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0b87e0ac-8550-3a29-a8da-ae937b21c854 | -1.3857 | -48.99284 | 2026-10-08 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a347a82-654a-33a1-9245-7bca6d712e70 | -2.66408 | -52.57833 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1847b839-11ef-3550-bc6c-bf7de88befa8 | 2.12247 | -50.82676 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b56c8bb-a4be-317a-9bd4-4747e2222895 | 1.70267 | -55.61321 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5e74383-1258-337c-a8c0-5bc5e462aa12 | -1.05417 | -53.59114 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87422108-0848-3191-8510-9e3f302210f5 | -2.98431 | -51.24482 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb25350e-596b-3e55-b835-f9a4c58f23bf | -3.2643 | -50.41122 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6ebc9dc-a8ae-386c-95e4-d2d21e6001b0 | -1.10539 | -54.16056 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4536bdd3-631e-3888-8de9-34ff233087df | -1.8286 | -55.04528 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35b81e16-05fd-368b-b2a6-ed4564526fe9 | 1.31682 | -50.84856 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed4a26f-029e-3a02-a9a3-e942e37acd2a | -1.15054 | -54.22004 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b873c0c-c342-3edb-b467-e993079a0339 | -2.10623 | -52.0644 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1019179-09e1-3901-86a4-3c3fe0e058cb | -3.16048 | -50.5951 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 290fb885-6811-3116-a198-c2e43fbb8f9f | 0.45038 | -60.54329 | 2026-10-08 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca9ce48-c94d-3de8-a981-c41e60d53efe | -1.5272 | -54.81865 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40319d90-50cb-3c16-b59f-9255257d8f01 | -3.18686 | -50.53966 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c6ea423-3ffe-3a00-9803-c252d2b5f14f | -3.20067 | -50.55933 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b060ded-9097-33d7-9efb-e2bbfc495502 | 2.4347 | -50.82317 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README80.md)
