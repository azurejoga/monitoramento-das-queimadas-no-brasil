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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1ea530d-ce6e-3992-87cd-54d351a16b31 | -3.9036 | -46.98967 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a38b0b21-6315-340d-ac2d-f7dedaf642d3 | -3.52383 | -52.1395 | 2024-12-25 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5275f5e2-4250-3e73-a084-cd117e5f77f5 | -3.15575 | -52.9815 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c347436-9084-3155-9214-03f85a53baa7 | -3.05767 | -53.79929 | 2024-12-25 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e986677-a984-3f09-b3e4-9673f36cd342 | -4.02095 | -46.90654 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b0187c8-975c-325b-b911-940ed02fd12c | -5.48026 | -39.66346 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 838d5108-77ab-3cd1-82da-302990497537 | -3.91379 | -46.92002 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff600be-4682-3809-80a9-54f67cc3d422 | -3.83542 | -46.68825 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40b93a60-7d58-3fb3-a137-985c41138906 | -3.9208 | -47.19413 | 2024-12-25 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e42f7ce6-c624-3199-be23-5315760d3194 | -3.14329 | -53.18634 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b35170e-5f10-3cf6-b83b-942f6e4f1405 | -4.02383 | -46.91122 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6852643b-c0c1-3085-982e-acfdcdc610cc | -3.8565 | -46.67053 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87e2e2fb-a463-3f62-8804-f45d3c33de72 | -3.91571 | -46.9129 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f008cbaa-e4ff-30e2-a059-5075a2eb6320 | -5.48284 | -39.66643 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54c84e99-24c0-3905-bba6-e536cbbf12ee | -3.91931 | -46.90852 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0c6aa20-87ee-3316-b395-afba0ca08325 | -3.90036 | -47.01023 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03ad4c0a-f910-3738-8ab3-acea8f71ff38 | -3.91247 | -46.92808 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bbfad60-f1f8-3eda-ab12-1818e7e84bd4 | -3.4321 | -53.2885 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c4f8589-aaec-3b34-97f2-e2ec44396e8b | -4.08384 | -46.81017 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9788ebea-d188-3432-b974-5874ba4c3163 | -5.47938 | -39.66914 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2babf2cd-8522-392d-b548-8e825097e894 | -3.91037 | -46.98578 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93b9089b-c02e-3443-80fc-8e084e0aa71e | -3.90057 | -47.00091 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ca502b-e3c1-30a0-8026-f5c29a4ab24d | -3.14925 | -53.18381 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22f5c8f1-3c30-3534-8859-7997299b4fb2 | -4.02142 | -46.90847 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e77aac6-4cb4-366d-b6ce-649196958b85 | -3.9244 | -47.19471 | 2024-12-25 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7f3c82a-3bc2-3253-91f4-d0a678420b19 | -3.81341 | -46.71307 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25165ab2-7f73-372c-96c1-78cb639479fd | -3.90213 | -47.01386 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da601f2-e868-33df-95c3-b5c89bebf434 | -3.89699 | -47.00038 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ece1895f-1548-35a6-bf85-f6ef2b294969 | -2.84641 | -52.80327 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 123a217c-5682-34b2-aa83-f19407946ad0 | -3.83956 | -46.68493 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d7ebf0-258a-3370-8b2a-bbaa6a82a43a | -3.91509 | -46.91202 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374278bc-7102-3b03-a731-31292c439b21 | -4.3476 | -45.95321 | 2024-12-25 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fd68fec-e757-3e39-a7fe-bd378365930a | -6.21074 | -42.6378 | 2024-12-25 04:18:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4bc999c7-0dc6-3ea1-891e-dd46b806fd82 | -2.84798 | -52.80017 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c5635e5-74e5-3dc2-9632-5a606d0b6d26 | -3.90191 | -46.99273 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4256f618-de6c-3dcd-8da3-b4a32a092869 | -3.86152 | -46.59518 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e96ccd-3c32-371d-86f1-bb4c834360e0 | -4.10728 | -46.82224 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 745496fc-21ab-3786-b184-37095275a421 | -4.12559 | -46.70763 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7951de3-fc61-35d2-a0c5-e7e1649d4849 | -3.89922 | -47.0092 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 282dd1a3-265f-39db-8bf2-e212a0185ab7 | -3.91177 | -46.89166 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9183abe-7b4b-3fab-911c-1919dc37b9d6 | -4.10281 | -46.64753 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd6c999b-b453-3be0-8896-3b1e4afd4d56 | -3.91406 | -46.90021 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fccf0426-3901-356e-afbf-e18d8c6d1b47 | -3.14867 | -53.18726 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4995cfc-87dc-3fa1-b7cf-a2edb2bbda3d | -5.34804 | -42.12078 | 2024-12-25 04:18:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af04af3d-d354-3faa-b4f5-b5befa19eadc | -2.91158 | -52.38655 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1251ee69-f2cd-38da-8ec4-203bdc6d5bc5 | -3.90681 | -46.98519 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6339ca1a-6a30-3db3-ba12-139e7d9dd6b1 | -3.15432 | -52.13969 | 2024-12-25 04:18:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a72e31a-184b-39ff-adbc-4204463eaa2a | -2.91107 | -52.38953 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4ad46f-df7f-3b13-9f36-86755dde80e7 | -2.85169 | -52.80415 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fb79231-14b7-3dca-a9d3-ab4d3e6b10b5 | -2.88305 | -52.54961 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edcdb65f-beab-36b8-9071-f4a53f91b748 | -4.04822 | -47.03122 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdac2138-0773-3d04-ada6-d6f66304f643 | -4.12272 | -46.70305 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbd37b47-44c6-399c-8725-ce1b9f5fbc48 | -2.85222 | -52.80102 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07e38140-9885-3d60-9091-4e49b625cacf | -5.92011 | -45.59123 | 2024-12-25 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cbc73bd-14a6-345f-88ee-0dc8ef2ee3c0 | -12.53729 | -38.00784 | 2024-12-25 04:21:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| df6c79b7-5796-38e5-a46a-0167f9fd047b | -24.24275 | -50.73925 | 2024-12-25 04:23:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 61088245-c167-33e2-b0bc-2c47630015ef | -22.53926 | -48.81196 | 2024-12-25 04:23:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 083a237f-38b8-3185-a4b0-12bcdabbc889 | -23.3394 | -46.77246 | 2024-12-25 04:23:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24b0722e-c657-3dd1-b236-4435b1fc7b45 | -23.59344 | -47.43979 | 2024-12-25 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c32bc696-5611-3552-9a34-f4321efe22fc | -20.57827 | -44.57655 | 2024-12-25 04:23:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 44fa320a-1139-39d6-9cc5-bae54b4cba62 | -23.57815 | -46.42228 | 2024-12-25 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 105428d9-a109-3f2a-b827-4253514d3935 | -22.17134 | -49.98156 | 2024-12-25 04:23:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e872f3fa-b35d-38e3-bd5d-235332973268 | -23.39087 | -50.84614 | 2024-12-25 04:23:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6377fcab-62e4-3f4f-8fab-b09d6cda369d | -3.22291 | -39.66148 | 2024-12-25 04:55:00 | AQUA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3be94ce4-2d03-345f-96e4-abfac3f86082 | -2.83977 | -40.29436 | 2024-12-25 04:55:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2f62fb2a-3e48-3fb7-bcf8-4e8b60b2fd90 | -4.05745 | -38.2893 | 2024-12-25 04:55:00 | AQUA_M-M | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 94a433ce-29df-3aac-914c-99f461a1793d | -2.85094 | -52.80398 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85a9830a-b86f-3c12-ab88-6840f72ad204 | -2.49838 | -51.80312 | 2024-12-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c79741a-6c94-376c-92ec-6ad3fe40d7c9 | 1.6 | -61.44033 | 2024-12-25 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef0199e-dd12-337a-94f0-7016c85d10d2 | -2.25016 | -53.76562 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea82fa37-2725-37c2-b75f-096de4d7aad6 | -1.36095 | -53.68216 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a4f571-f929-3a5a-9d1c-5161c2ddf028 | -3.06741 | -53.79482 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57dfbb57-6c45-3f00-b60f-2b391cc4f93d | -3.02759 | -53.89374 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23ee519f-4c7c-3f73-9dd9-6946ff141170 | -3.14826 | -53.18635 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed919f19-f60e-36c5-91a8-f0bda081db8b | -2.94368 | -53.05554 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0b4ee6-7565-3f34-b08a-455542929fe5 | -1.5888 | -53.33516 | 2024-12-25 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 602a7667-31bc-3163-b503-c1dbcca38001 | -3.75106 | -52.03922 | 2024-12-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a131459-7f4e-3d2c-9c28-00c34d878b14 | -1.5852 | -53.33461 | 2024-12-25 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c62a349c-befa-3acc-9fa7-e7459db5f277 | -2.50586 | -51.79656 | 2024-12-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ae9b867-349f-34fe-bb6d-69968f79b412 | -1.71423 | -52.42993 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e05069f6-0301-3ca1-842f-b41a6976fb29 | 1.59923 | -61.43973 | 2024-12-25 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb72bf78-e9ff-33e2-b56f-31f76b8b9a72 | -3.87926 | -52.13944 | 2024-12-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be74555-9247-3163-a90f-978fca97c2d2 | -1.53796 | -55.24829 | 2024-12-25 05:10:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85b401c2-3d8c-3243-807d-c194ef823a96 | -2.00048 | -53.2686 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b921801-055d-343c-9613-b4941aa020be | -3.02696 | -53.89777 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7bc9c49-ae5e-3333-864d-87a0a79c08ea | -3.00974 | -53.8201 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29b56a73-d287-3839-90ad-c58fa1aeb308 | -2.85542 | -52.79991 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 63993d11-29a8-337c-8a21-a164e0fcc5c9 | -1.70048 | -52.41834 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27103674-d281-39f0-8c96-fe217fa1b761 | -3.88964 | -52.1518 | 2024-12-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56896471-0357-33b5-83e9-e22cec7f30d9 | -3.06444 | -53.79023 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90386efe-3b4f-354c-bab7-5abb076354a3 | -3.15046 | -53.1896 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8e85fb9-c883-3740-8e43-69734ed98a71 | -2.9253 | -51.57897 | 2024-12-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0904d2f3-3869-350c-bde3-d773ee5fe11a | -2.94427 | -51.48162 | 2024-12-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20e685c2-b929-3d82-ad88-eb315243b838 | -3.2885 | -53.05658 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d91fcb-9376-3580-8512-c0910cc1104e | -3.06479 | -53.7953 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60fde79d-29a1-36d7-9d5b-abcabad70bfe | -2.34465 | -53.88108 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81abea4d-9ebf-3b56-bb44-0a3d2b217cef | -1.70499 | -52.41429 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e704ca7a-9825-3c10-b4fa-8e7c1fc8ea96 | -2.88613 | -52.54859 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3f3a373-eca7-371e-a322-838501518d04 | -3.27556 | -52.9669 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 969abb41-15b2-34cf-819b-7f54132d8fe3 | -3.15303 | -52.98241 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
