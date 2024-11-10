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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9104c359-e288-3b15-bbfb-3c7f16a079b7 | -3.44642 | -50.30326 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94911abf-c1e6-30be-b482-b76d66ad43cf | -3.0799 | -50.56812 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef35528-2268-30b1-bd43-d80c1288c32b | -7.45665 | -43.58802 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74840ef3-5cc5-3816-bfc1-16f5119fec9e | -4.04234 | -48.28531 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd28779-1b9c-37f9-9849-9466320933ef | -2.67736 | -48.65899 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1903ea93-b0aa-3f55-960c-506cea88692d | -2.23466 | -50.69004 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b620a0d-2eab-3e97-8c8d-f7da1c732ee2 | -1.50821 | -54.69631 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7928a6c-e8f9-3861-8fb0-e87d07c6cb83 | -2.47506 | -50.41813 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a97d02dc-4a4f-3720-8191-fcecb8ee2ce7 | -3.61343 | -47.51929 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c24bcde-8e31-36e6-a384-125ee649fc98 | -5.33301 | -47.70481 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2c4ba8c-695c-3d35-bcbe-8dd523795506 | -3.83701 | -48.8797 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4278a265-52e1-34a9-a014-749d65fbf2d0 | -4.06498 | -50.01309 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08227c9b-b817-3449-812e-6d3a7242f0ad | -4.07959 | -48.33018 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2a6a87d-8234-3fce-a450-a76c37a97b70 | -3.13211 | -50.37149 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d69b0f72-ed95-358b-b2ff-9f6a22262acd | -2.64046 | -49.87859 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5789290a-ec52-34f9-b537-7efda061db74 | -3.6227 | -54.79339 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bcfbed2-2148-3326-a67b-33844a087260 | -3.09325 | -53.27043 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de855e5a-4646-3143-8ee6-5893763bc701 | -3.96873 | -48.17068 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8da66b95-00d0-3e2b-b808-1630126d9563 | -2.12403 | -50.83965 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85dd330b-01c5-3e87-9613-2ba0b9844f97 | -3.17615 | -50.5979 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 546c9030-d0de-3f4a-8581-464ead8bdb6f | -4.96654 | -49.3584 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c750f51-fb87-3b64-b47f-2adbf13f9aac | -3.95039 | -48.15712 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92553fd6-c463-3dcb-906c-57addc47da53 | -2.96128 | -48.01712 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da0f7f00-e2f3-300e-a847-b74fb5e44d00 | -2.2077 | -50.33919 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51256e5d-3468-359b-9ca7-739b249c476f | -3.622 | -54.79755 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60b0ea08-f613-3843-9209-da6830806a2b | -2.4591 | -50.25244 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42a87881-2f18-3d6d-b210-7ff3aa1cd799 | -4.06847 | -48.31424 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef73ad9f-7fc4-38bf-991c-99f2163ae3ea | -2.86946 | -49.22473 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2b827e-2511-36eb-acce-0c142ece79bd | -2.69115 | -49.86452 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 16a2cece-e025-30bc-9641-19df793b6bf7 | -2.71919 | -51.70963 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0885723f-60da-3ebb-b6cb-230f25a7dad4 | -4.72443 | -45.63783 | 2024-11-10 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c141635-3f72-3c54-a0e3-28448ce68a0a | -3.63379 | -50.18044 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f8a58e5-2ad5-3f9c-83d7-6e10bb6c8ed3 | -2.14652 | -50.8114 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00ee79b6-a5db-37d2-b640-4bdb43aa6b79 | -2.636 | -49.84119 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d48dc9b-be16-3165-800d-04926dd0c676 | -4.40468 | -48.6082 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b72b2d5-0f2e-3c79-be94-c7f6da66f08c | -4.89846 | -47.46926 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc70f93c-93a0-3aef-b1f6-e901b8d406ce | -5.25448 | -48.07906 | 2024-11-10 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 428c103f-2faf-3b7d-8782-0e52fea2b6a8 | -4.51664 | -43.98354 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6c82c26-68ad-333c-814a-89dc121d15bf | -2.28992 | -50.67918 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f8d5250-4591-3a5b-a006-626c50ca456c | -3.04886 | -54.86464 | 2024-11-10 04:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b712e8-d998-3c7a-9833-af2ba9863540 | -2.46288 | -49.89544 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15fb8796-fa3b-3fc0-83f9-1540d280316f | -2.86433 | -49.14911 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f21a0ca-47a7-3b1f-ae2d-29b323b53f8b | -2.84317 | -46.63597 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 321d0949-5e99-3b0a-911e-cd6c574c6b55 | -3.44359 | -50.29911 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0b14e84-259c-3e8d-abf0-9484a3eec76a | -3.88197 | -52.39296 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 922800a5-f2e6-3aff-9ec5-51120a4e0a54 | -3.31559 | -44.39455 | 2024-11-10 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4f17aa3-492c-3f9c-b5ae-cf11f4cc514e | -2.80121 | -51.47715 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 305d656f-2fc0-3603-a441-5e05d22724ad | -2.71851 | -51.71381 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27dae8ad-bc4f-3df6-a987-7ba838b14975 | -4.56683 | -48.04929 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddf363b-0208-344a-a21b-3fb1c70e0e01 | -2.59061 | -48.3314 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dbd95c7-a19a-37ae-bf8c-5a45e18c9195 | -2.43903 | -50.51209 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5db29157-509e-3e85-adab-4e5f8b70ca67 | -3.10873 | -50.21051 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 864ef416-a07e-3152-a318-668d7616c1a0 | -5.50932 | -41.68664 | 2024-11-10 04:38:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c41ab687-ab56-37ac-abc5-bb4a55555da5 | -3.60681 | -55.3835 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3968d51a-9517-3e75-b663-e019cbe27f18 | -2.06163 | -53.40998 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b1fa6e-491a-3f8c-bb3b-0b3ddcccc44a | -3.07935 | -49.56148 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f9bff38-adbb-3df7-b0e9-676ced3f4d27 | -2.24017 | -51.83745 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2e2e189-dfd4-3eec-8bd0-9af4c8061c51 | -3.07322 | -49.53532 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51e1cd76-55b7-351a-b3cd-ccd9859162ee | -3.95376 | -49.0006 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de92c0c5-b79f-3a28-a401-fa2866c746fd | -3.69579 | -45.81095 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 064ff620-41ec-3192-9e69-80a433b49eec | -3.41181 | -50.30158 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec9b0e50-ae46-38c5-97fc-6f7807653996 | -3.10069 | -45.95502 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c54a8245-ffbb-3215-8561-8a1c9e1bbab0 | -2.83199 | -52.55765 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c33d4c4-b6d5-3344-9848-2bae8640d23c | -2.9322 | -52.77774 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 2d78695b-d0a5-328b-8d22-b05354a9c8f8 | -2.83465 | -51.80466 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 988c47a4-6885-3e90-8d24-cdfac2fd9976 | -3.07797 | -50.49155 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19dd7f2d-7100-3c79-a753-140dd5bfe56b | -3.23792 | -50.27505 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a9fa9b0-e7f2-3ecf-82f0-3a7036f6a344 | -3.28573 | -46.41412 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d55d7061-2072-3108-a021-1704b5121b7f | -3.22604 | -50.26198 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43a3a3d9-8913-340d-8d6a-55de3b2d5cb2 | -3.95529 | -49.4374 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63aefc7e-f3e3-3ed8-87a8-bfb45eee88e5 | -2.72897 | -51.74121 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bf4db18-45be-3679-8369-e0bebef58a19 | -2.31076 | -50.39265 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f45bcea-d757-3b65-82d9-a413da08fab5 | -4.05972 | -49.2084 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c65fd97-cebb-336f-a80a-f834ee403f34 | -3.08157 | -49.59067 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae76ac5b-1bad-3caa-8404-1e9d4bcfd032 | -2.55946 | -50.68119 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26c77737-b24e-331e-bb85-bae2489bb3e5 | -3.52931 | -49.97657 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b87f9d30-ccb7-39e6-9208-518697bbab12 | -3.06379 | -48.03364 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 32048508-eb59-3af2-88fa-e2902abd0a5f | -3.43502 | -52.48388 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7354fa4e-0a48-3a26-9160-75aab5dca951 | -2.35455 | -49.80911 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd25d743-3d44-3c5d-b6bc-4de76e2fa2aa | -3.24839 | -48.75168 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70dda63d-ab05-3d48-944b-4658dbbf7d57 | -2.83858 | -46.64285 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97cc719-9c16-3202-9ac0-19f31e730f40 | -2.43413 | -49.87987 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ed372ff-03cc-3e0a-84bc-21d73d15f538 | -3.17555 | -50.60163 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9854e95-bd59-34be-8666-e825147daddd | -8.40305 | -44.12875 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1875c093-e6a3-3029-8c19-27ea939371f3 | -2.62567 | -49.46214 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 992af367-ec2e-3a5b-9bdb-c06c1c8ceb01 | -3.2827 | -50.23698 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f664959-8a61-3179-99e3-c91f3f3aa965 | -2.83457 | -46.64603 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a7b864-203d-3269-9b26-3e6cbf2cc81d | -5.13913 | -47.71616 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c27a63d-f573-3416-96c7-4e61c2e64a40 | -2.79452 | -48.28178 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f9bea66-3d33-375e-a288-4d7476c9f06c | -3.12875 | -50.15037 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| caf7f5c3-bd3f-3e00-a3c5-198da04887e7 | -3.96581 | -48.12391 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d81e15-0ccf-331e-91e0-a33a4c240655 | -2.89458 | -49.38218 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec6029df-e6bf-37f6-a812-dde22a52400e | -3.13476 | -50.44362 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a631d41e-1fae-3e0c-b803-942283365f2d | -2.80844 | -52.54233 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e0627a3d-9dd9-3bb2-96d4-83f65a3f46c5 | -5.21027 | -48.34185 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 604522a0-1651-3adf-ac1e-f2c02dbfa59c | -6.48284 | -47.50953 | 2024-11-10 04:38:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d9869d0-03ef-32f0-b5d9-c2f1c506dfee | -3.95789 | -46.71004 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fdbe693f-1081-3d4e-b5b0-9a2fac689262 | -4.75694 | -48.92879 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e23f4a4a-6c88-3102-a9ad-7e59b74a3711 | -3.14161 | -50.44471 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1dee0428-a001-3f1f-a308-96688b47f218 | -3.96914 | -48.12443 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README83.md)
