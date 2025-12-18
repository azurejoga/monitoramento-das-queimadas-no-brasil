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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6a0ddf0-aeb3-30c2-910e-160f445d0575 | -2.99246 | -52.37792 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 223f4a86-4bdf-35c3-88c1-c2089759cf4b | -2.79183 | -51.41027 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 021710dd-afe7-3941-ba64-ac2ed13dc0e9 | -2.41714 | -49.34745 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 022b5cbc-f1a6-37e5-a7ce-da8bab555b1e | -3.85754 | -53.39225 | 2025-12-18 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef9d11e-9594-38d1-9702-3de84a2a13e3 | -3.66586 | -53.46755 | 2025-12-18 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 698f9a63-2ae9-3a29-b7f6-7c9002fb26b9 | -2.41383 | -49.34411 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edfee97b-5f3a-315a-90a5-9419a68105ea | -2.16745 | -50.26058 | 2025-12-18 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f05cc8c3-5448-351d-b30c-20006f86f880 | -8.10069 | -55.00954 | 2025-12-18 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f64b18-d812-3d22-a103-e32d43b79edc | -2.68035 | -51.67649 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6adabf03-b3d4-3e7c-b0e3-7d6442c1b3b5 | -2.78794 | -54.57377 | 2025-12-18 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7b124f-8e07-387b-be25-0bc559486204 | -2.44684 | -49.03161 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1584185c-d78b-372a-ae82-f370aa1c9d4d | -2.66781 | -46.89875 | 2025-12-18 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4bd99607-4bb3-3155-b165-c934ea7a68f6 | -2.44298 | -49.03102 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c79e4e6a-4790-360d-8c6b-9a6b2b376e39 | -2.37504 | -51.99584 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ec9edbb-8768-3839-a37a-515469262289 | -3.66345 | -47.54681 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b287ad81-574d-3b99-a4df-8ddcb6c3a337 | -2.65428 | -51.7322 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a076f74-72e8-32a5-a329-1ec9b1db275b | -3.66415 | -47.55447 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72b70721-f9c3-3a8c-b983-732ac868fab8 | -4.0077 | -50.31718 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c266ce0-2657-3795-a03b-a14fcf8d9fd3 | -2.67695 | -51.67596 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6bdcfad-37da-34df-bd23-206157281b53 | -4.01043 | -50.32391 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c767fb03-c70f-3497-9fb9-0ad6133f5660 | -3.52678 | -48.87899 | 2025-12-18 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3684fc10-66f1-3b82-8eef-6155b447820e | -2.3732 | -51.91872 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c81f6bea-4832-3436-b26a-9999bca1cb88 | -2.2609 | -53.6618 | 2025-12-18 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9a7a14c-35b9-3b40-acaa-fe7541aa96a4 | -2.99301 | -52.3744 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b89cd41-c4c5-340b-9c14-5cb7ca225a88 | -1.4285 | -55.34163 | 2025-12-18 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08337e3e-ef30-3144-8b8d-fef76eaa201e | -2.44373 | -49.0262 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5aec8c8-1caf-37d5-b814-edb770d59ab8 | -2.3949 | -51.77839 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f188a67e-476c-38a5-88a6-9774331191b8 | -3.21696 | -49.36224 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 312c0835-68b5-3405-a3ca-8b04fc22cf6d | -3.65782 | -47.55465 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ed80144-73d6-3713-9e43-2ba9aebab051 | -1.42791 | -55.3454 | 2025-12-18 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05d21a94-83e6-3d7f-b5f7-7a81025f7b89 | -3.29553 | -52.8332 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac5e98b0-0097-3a2d-89ea-6ac01f228830 | -3.68221 | -52.53127 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42aad3a9-b516-3a9d-b003-efb2f253255b | -2.26578 | -51.88724 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f18fc1ee-88c0-394a-b008-0b5035f753b5 | -3.73839 | -53.80696 | 2025-12-18 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77640dd5-c209-3225-84c9-b16dc748d49d | -1.25623 | -53.32074 | 2025-12-18 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 463d885e-41ef-3e3e-8c5c-0f4d60631f2c | -3.18619 | -50.22999 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d50035b-1e6b-3649-b7ef-3f57286779f5 | -4.25364 | -50.66626 | 2025-12-18 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43bd714-a702-3e4d-a635-eabcbedd77ac | -3.66043 | -47.54958 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d651b38-44ca-3157-a42b-9b27e99d1022 | -2.45036 | -51.98895 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e8d5a26-895d-3e93-a71b-df0c1b625667 | -3.89649 | -50.31077 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1713452c-9bf7-323d-9bee-bc34c504008c | -2.69511 | -51.64883 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f8006cb-b2b8-3da9-949e-4816def2aa77 | -2.37376 | -51.91514 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d58be9-6695-3e20-881c-dc52e7ca35ff | -3.54577 | -54.72576 | 2025-12-18 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04f9da09-03fc-32ce-ad46-ae4f0a43b87d | -3.65922 | -47.55796 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d04f885e-f067-349f-8a30-ce58c4a6fce5 | -2.44754 | -48.87266 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc5f97aa-38e6-36d7-b4c9-b42a31af179c | -2.87812 | -51.78138 | 2025-12-18 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4503a6f-2e06-3fd7-a77a-403a94f23e18 | -1.86571 | -52.05901 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a5bf7ab-00dc-3547-9089-ec07993e0f47 | -2.88972 | -53.01443 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33ed739d-dc0e-30e2-a374-4ecb0f5d547c | -2.43962 | -47.15635 | 2025-12-18 04:57:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61b24cdb-6bd5-3528-8cf4-81eca1d01e41 | -3.39946 | -49.21167 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4dfc84e-4ca3-3da5-a6f4-a7f725c52ece | -3.65981 | -47.55385 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cdba389-f43c-39de-8a31-fe421f17bf43 | -2.41762 | -49.3447 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7772d2e1-4de5-34f3-9d98-cfd8043c9c42 | -3.16684 | -53.0262 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23f84f9a-f54b-3504-8dac-e21fd74bda85 | -2.98632 | -52.37339 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b49863af-39c7-3491-84ec-e228b725242d | -2.93379 | -48.22639 | 2025-12-18 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59a3e8ff-3c1f-31e5-8ccf-0cb36004bcb4 | -3.33978 | -52.83295 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef294576-3921-3487-ba4b-f86f5dee781a | -2.98912 | -52.37743 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51ea054f-93fd-3349-8d9a-d99c0229c196 | -3.78355 | -47.74686 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2762ff77-28d1-347e-8785-98fe0a09cc4c | -2.66273 | -46.90215 | 2025-12-18 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52d420cd-067c-3b4c-9cb2-da6b30ddfc2c | -1.67267 | -52.09426 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e96328e9-fc33-3d73-be77-4561d94321b8 | -3.66216 | -47.55528 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d29006ff-16e7-3636-b5a2-5a412a8023d0 | -2.3428 | -53.61816 | 2025-12-18 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f0e7360-6227-397a-865f-db565ff095e1 | -2.25759 | -53.66129 | 2025-12-18 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82e095e0-805f-352b-a9cd-9ee700cccd94 | -3.89609 | -50.31205 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 164e2209-5aca-34fd-a834-47906b4497cc | -2.97914 | -51.24565 | 2025-12-18 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd78c4ef-2695-3c13-a0f8-ab118c2c69d5 | -3.90079 | -50.30706 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bb1931b-ff53-3fcc-9679-7e76c80888f8 | -1.42505 | -55.34108 | 2025-12-18 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81318741-bba1-3b6a-8c66-c09bebef6f22 | -5.58977 | -51.35148 | 2025-12-18 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d7a4b4-f9c5-35f8-ba8e-6b772a5b5857 | -2.95438 | -48.05951 | 2025-12-18 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a0c591f-cb1f-346a-ab89-0ca47685faa3 | -2.439 | -47.16052 | 2025-12-18 04:57:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a898c255-7a2d-35a0-87a9-c4a1088945c7 | -1.45893 | -55.2157 | 2025-12-18 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a352d8-79f6-32f3-8ee5-366bab6ba2c3 | -2.92862 | -48.23301 | 2025-12-18 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cc6b12d-0e64-3e94-9b9e-d9d916ba83c1 | -2.89026 | -53.01097 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5823ef-3b10-3f8a-8988-edde6d472a3e | -2.37168 | -51.99533 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3450f881-a583-3d3a-9873-84e81b6d528c | -2.02303 | -48.57564 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af6b36e0-193c-3e9f-bdb3-814194ae6216 | -2.27471 | -46.96382 | 2025-12-18 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c88400e7-cba4-3245-a012-7bed6e9a277d | -8.104 | -55.01006 | 2025-12-18 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 951a13b9-391f-31ce-bd8c-48e92443e391 | -5.59019 | -51.34872 | 2025-12-18 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 589e46d4-6a93-3b08-a6b1-8f634508663f | -3.66477 | -47.55022 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e85d6d03-0aa4-3d3e-b4fc-19dfa39f4063 | -3.07528 | -51.61994 | 2025-12-18 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd0c776-dbc9-3e1b-a024-9df8f86c5c8e | -2.16869 | -50.26246 | 2025-12-18 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 668eda17-bf51-36ca-abc3-5c940fdd6da6 | -2.80409 | -51.81093 | 2025-12-18 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d9ad5761-55fb-36f1-86f0-88b752eb5191 | -2.47139 | -52.11976 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe50eec4-efd1-3a20-ae44-f2faa42c8b44 | -3.87957 | -54.14299 | 2025-12-18 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da119898-e4ea-3ab4-953a-0c4977fd9557 | -3.35567 | -49.23946 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ccfb7df-0253-34bf-b24a-35a78a49153d | -14.39545 | -43.98161 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72a124c4-bf57-3c8f-8f2e-b03b9a5467ad | -14.38964 | -43.97554 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdc5f1d9-802e-326d-898c-d9ce559aace8 | -14.39145 | -43.98044 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 444dc29e-b831-3ffd-8160-1c6f7fafd959 | -10.95197 | -49.41647 | 2025-12-18 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d81d0a4-5af9-355a-a612-142a67221e5a | -14.39716 | -43.96581 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc28f1e-c6fc-3859-83df-c8de95a6913d | -14.39253 | -43.9698 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a2eef46-a023-3a38-91fc-37c7c1183275 | -12.42485 | -64.13617 | 2025-12-18 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8fc6b91-5ca9-304d-be19-5c5342d77c3b | -15.11789 | -52.94455 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07b8ebe6-330c-37ab-8561-823debafc087 | -14.39199 | -43.97511 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a185bce-3c90-3322-bf13-1c4838828327 | -14.39659 | -43.97108 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a032ffb-1b5b-308d-b33e-d7a6abb419c4 | -15.11751 | -52.95213 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bfe7355-216c-30ab-a033-69acfef0d8a7 | -14.39022 | -43.97019 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27d35bec-9f8b-3616-beff-fb034ae764f4 | -10.95239 | -49.41739 | 2025-12-18 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae3bc465-79bc-3fd3-9a52-b97757e70a6c | -15.11871 | -52.94345 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a9b3cf0-938f-3685-8e0b-68c28ad0157c | -14.3908 | -43.96488 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README7.md)
