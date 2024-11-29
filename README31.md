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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 802604fc-9dab-3f92-ac9b-30e8df99b740 | -3.10138 | -53.80907 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37ad564b-e443-30f9-ad66-59f22d4a4073 | -4.04536 | -46.83628 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56dc5384-fd11-37cb-8650-82ba4f20efac | -5.59873 | -38.78593 | 2024-11-29 04:04:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 837299a0-8800-3116-99a3-367ae8f8ed4f | -3.78311 | -46.69399 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cf6eea2-4c09-30b9-935f-1f1f1006f290 | -1.06964 | -53.6383 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03f46ea2-4b51-31ff-8f90-4711377c69c1 | -3.28295 | -50.55434 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a89c6724-ac03-3f95-a726-aa8b8db92149 | -4.0447 | -46.8403 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6ee29b1-eb0b-3355-9528-ba54ba28b055 | -3.34613 | -50.51905 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1163cc46-6aaa-300e-8d31-2e676f2f88ee | -4.42896 | -46.58403 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3ace65c0-4a4a-3826-8e5c-14d47e7924d3 | -3.16618 | -46.56609 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 177b83d4-05fc-3e52-9317-664c01aa6bd2 | -0.9497 | -51.65541 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2102b54d-7486-39cd-9a27-3aa6d9791516 | -2.84338 | -46.82298 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a9fafa-5b29-3b5b-ae92-a5e534f1ce05 | -0.27048 | -51.63073 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a728a00-5864-3420-90b7-fb99e89b5e7f | -2.73137 | -48.89247 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c3b0353-c5cf-3381-8d78-a4324b3ef7ea | -3.7025 | -50.51618 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e0e7dde-30fd-371f-b99d-d58e5d9c4b59 | 0.98917 | -50.26926 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27aa2437-63b7-3bd9-9e7c-c2de0ebaf1f0 | -2.25369 | -53.75278 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab6d80ed-f9f6-3a52-9ed7-ca32d545d1e2 | -2.8423 | -46.85722 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d892ba8-801d-33af-a74b-b37cce16605a | -5.22184 | -44.92078 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 290a66c7-5862-38fd-b340-979e9f6eb65e | -3.81931 | -46.60186 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d670d42-3d0a-32c4-9d5a-9962f6557ddf | -5.00316 | -44.76604 | 2024-11-29 04:04:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50a3f67d-dbec-385e-ae42-8bd1c7958353 | -5.28835 | -43.16262 | 2024-11-29 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d125d1e7-8512-356a-b552-7a15cff56dfb | -4.30726 | -48.2099 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b26f833f-872b-3f2c-9843-3c41581914d0 | -4.64162 | -42.40387 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 753d9891-7318-347e-ba7a-09cf5cdf1790 | -4.2268 | -45.7739 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2638a15-5a04-347b-a21c-d5131f437516 | -2.60492 | -46.84788 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23ee17af-e969-35b5-bad4-f008ea002fdc | -3.68842 | -50.23063 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1105fd73-d20a-3fc6-9cb2-a65aa56299c2 | -3.04762 | -49.52428 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ece02a-b503-38f5-83ae-63e1207efe9b | -1.59308 | -52.28295 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8488ab04-dcd5-3d43-a2b3-eb340fa440b6 | -3.87103 | -47.07638 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cb50ed5-d577-3eb3-bee4-7a130df79a3c | -4.78468 | -46.1157 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f87f5176-f3ee-3ff9-8928-5047f5c6bf96 | -0.55958 | -51.70435 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2264e3c-41e3-3da6-9f84-6a8080ceb117 | -4.98407 | -41.31552 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0f99406b-bb46-3585-b668-e75028c7da22 | -2.72488 | -48.90048 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9efabf62-3e1a-3849-ae16-8798d6d128c4 | -1.58622 | -52.27545 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2abe2331-a583-30e4-a136-f82998f9184c | -4.6861 | -45.81041 | 2024-11-29 04:04:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eed851f-7684-3531-bca9-f94ae9938df9 | -3.16083 | -51.09674 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 785b467b-d58b-3de3-99e2-cfeffe6b0d2a | -2.65181 | -48.78214 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8aa507de-c742-31e0-9ba5-2962fb27959b | -4.08611 | -47.03194 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18006490-3938-3c78-8999-65399f261bb6 | -4.07783 | -46.82561 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a17d19cd-0fac-3976-acbc-33b923191e0b | -3.27968 | -50.60754 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 317d5d8a-1a17-351f-89f6-3f68bd069c93 | -2.78095 | -48.10782 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd748dbd-879a-3f14-98c7-adb2a0d9ce0c | -3.2512 | -53.6477 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e56b79d3-de10-3f5e-92cf-6311dbf2e7fa | -5.01667 | -41.83834 | 2024-11-29 04:04:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2568a7c-1f2f-3b72-992c-87c5732c6b18 | -5.02129 | -44.44985 | 2024-11-29 04:04:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a38c945-6303-3e51-9ee0-4ab974e18020 | -2.55839 | -46.41558 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 566bf72c-e777-3981-b27e-4c67d42c4b47 | -2.6097 | -46.56016 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ada5d77-a010-3297-9ac7-e34749ac7aef | 0.94029 | -50.74623 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9439cd5-d02a-3902-a0b3-9254c1428474 | -3.96241 | -50.19238 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e1662ff-e26d-35ff-9377-48fcb9f4519c | -4.07745 | -47.03049 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc20c52d-336f-354f-8123-1b7b78918dd7 | -4.18018 | -48.61252 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29753bd5-58f8-33dd-8678-bd4ac180c602 | -3.27025 | -50.62919 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 714de273-e38c-3c5f-afe5-0b087f804eb9 | -4.86554 | -41.26823 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1095b8ab-7fe2-3916-8ab7-7cfec339cdbd | -3.9385 | -46.72121 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e237571-0e1a-3461-893f-664e7004675b | -4.7869 | -46.1273 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb0c09b1-dfaf-3f47-8328-bb56afa7fed6 | 0.33782 | -49.71904 | 2024-11-29 04:04:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c6ecb1-016e-3812-bdbe-ba95921f69ab | -1.59093 | -52.28701 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d8b5f6c4-9a2f-3ba8-bb09-a5b47e354456 | -4.9139 | -47.5632 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abfe778b-a431-3404-afbb-ea34587d7cd4 | -1.71709 | -52.7757 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 665ebe9d-1b2a-33d2-849e-eb92d926b692 | -2.45786 | -46.55765 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8667e90-6515-3d6b-91b2-3ce2055dcd3d | -4.01752 | -45.96206 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0ab7dd6-a67e-3490-aad2-ba7e4bf0b30f | -3.54129 | -50.19096 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5eca888-3104-3f7c-8167-f274aee8a746 | -3.46127 | -50.53488 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8fe68051-2ada-3b7d-a3c6-1a62314bf02a | -1.53182 | -52.69878 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dc90903-9bd9-32d6-a6b0-df9f81a1c483 | -5.40152 | -41.55457 | 2024-11-29 04:04:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bc94c3c-6278-37d8-abe9-62a2cf156970 | -3.09914 | -53.82225 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce4906c4-f720-3b1e-912c-f39a6b0bc90e | -2.578 | -49.99728 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a9abda3-e953-3cbc-b5cf-d1e248035d56 | -2.83164 | -49.84444 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a50a588-70cc-37c6-852e-8bcf689cab05 | -4.64219 | -42.40029 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 453f71e9-35d0-3ca3-9c22-cb80dfa721ed | -5.8662 | -42.75466 | 2024-11-29 04:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| becf80be-69da-3536-b60a-92fa6f3f66dd | -4.74422 | -45.77819 | 2024-11-29 04:04:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bad9755c-1197-3b0b-a1ce-889dbd8d3a5b | -2.60561 | -46.84363 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55448d95-72eb-3064-87de-d95c4aca9fb0 | -3.30637 | -50.27943 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd097c75-692b-3ae8-91dc-e72998068118 | -3.79289 | -46.68738 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 045e36ea-f829-3b1a-ba36-f09874b30d4c | -3.3231 | -46.69855 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4b2238f-c3c7-35a1-b51e-14ab0641bc71 | -1.5901 | -52.29225 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4b7d071a-1526-3d9f-9f3b-140f41e2ce70 | -3.28211 | -50.62725 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55a338e-b81f-3a39-aa5e-2878d9aa8322 | -3.09978 | -50.36622 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 969b84e8-4533-3214-bdf6-1ea71fc1d562 | -5.69697 | -43.26056 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38b6fc76-6ec7-3e4d-a885-b04a584fa592 | -2.40899 | -48.54374 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2fc68d5-09ce-3a66-ad79-7a78680f4eb9 | -2.33544 | -46.86932 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 287e4062-52b3-361c-bb10-49587043219d | -2.8806 | -46.84182 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b0a974-74a2-326b-961b-12749e2bba70 | -3.92577 | -46.39873 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13163d2f-d78c-3c75-810f-86859bf6aa6c | -3.47339 | -50.53648 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5f6c234-5696-3ee0-aa2b-694e05c01861 | -3.24066 | -50.76922 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e539beca-5510-32c0-bfb4-f829cc9a91c5 | -4.25822 | -42.60989 | 2024-11-29 04:04:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75ffeacf-c965-36cd-a8bf-71c14da910b8 | -5.31168 | -43.08253 | 2024-11-29 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9434378-81eb-3599-8303-6dd83e780e63 | -2.83677 | -48.09827 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e0f1e0f-77db-3aee-8497-95df1227d78c | -4.35009 | -48.12661 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95b0940f-9a9e-32fb-9b87-febbe6a437f0 | -2.10324 | -50.34824 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02e6cf0b-c679-369c-bacb-534b6387f6c3 | -2.01254 | -51.19772 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcfbffb3-86ec-34aa-ac82-7479f0c4ca89 | 0.74015 | -50.87128 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd0acf0d-dd96-340d-a5de-ddc4640a4cda | -2.71068 | -46.12149 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee03976-3413-3130-a228-dbcd327601a8 | -4.77312 | -44.96139 | 2024-11-29 04:04:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d5d72f5-0a55-3799-abdf-d85a2e57e773 | -4.91313 | -44.03077 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cd8bd66-d66c-3f4d-a4a2-9d2c50b72b4a | -3.33231 | -53.22622 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7769a10c-5fa3-32fd-bfe4-59db1919c6a4 | -2.66495 | -48.79617 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5989e76a-df40-31fc-b77a-fad8baa7b341 | -2.97881 | -53.30061 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7cd53ba7-c68a-375c-8b85-ed21e6a42dfd | -3.46846 | -50.53178 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d4e3f9d-a89e-3644-90e3-224db9a55d1a | -1.59565 | -52.29859 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |


[Clique aqui para ver as próximas entradas](README32.md)
