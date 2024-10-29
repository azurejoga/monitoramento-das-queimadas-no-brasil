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
| 8234f476-ea9c-3488-9853-a2706a077971 | -3.69551 | -51.83703 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b400ffcf-1aa3-39d1-bfc3-9eee28c99a75 | -3.69487 | -51.84127 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11348351-01e2-35f0-be03-29ef5720dfb5 | -3.69486 | -51.84297 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e96f7ad-cc9a-304b-b560-d4923ee0b1bd | -3.69359 | -51.84975 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e4aa3cb-58a0-37c9-a105-d250a656060f | -3.69353 | -51.85144 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1a666e5-799b-3de8-ae0d-5b20e6a0014b | -3.69296 | -51.85398 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21a23fd3-a8df-34ef-87b3-b91dbf24c634 | -3.69287 | -51.85565 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b2770d7-43d5-3dcf-b7bd-62c04950f878 | -3.69188 | -51.83818 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eecfd1fd-8bb9-3485-8b9f-2f43a2fc54a6 | -3.69187 | -51.83647 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 518600fd-a26b-3027-ba28-d394b02f56aa | -3.69123 | -51.8407 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c71a8682-1222-3181-b056-d4f4e91130af | -3.69122 | -51.84241 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b83c4ec-fd65-3566-aff1-5e4647e72f2a | -3.68996 | -51.84918 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87917240-9bd6-3efd-82ed-6c1b2f47d341 | -3.6899 | -51.85088 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f628186-f5ac-3e33-9f52-a27745036e0a | -3.68932 | -51.85342 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23ced2a6-5451-35ea-9d42-3253488d3346 | -3.68923 | -51.85511 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b9bc300-0af2-342f-b142-d29ca95ecfcb | -3.68632 | -51.84861 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00dbf0ef-7d7d-3bb0-b523-6e99e80c083d | -3.68626 | -51.85032 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01814949-247f-38d7-9ea5-d14125712ca1 | -3.64074 | -51.78296 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 439ab85b-607d-3de5-8b5e-15b098231b35 | -3.62486 | -51.78917 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fba667d5-bbd5-3689-b56d-2c7cca2cc989 | -3.62121 | -51.7886 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7179e37-4d2a-3a40-93c8-2c2314e5cfd5 | -3.60128 | -52.01613 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 139a18e4-5551-31f2-bcd3-a4ce612c34e5 | -3.56964 | -51.98162 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb2eb06-732c-390b-ac01-74f8463d80e9 | -3.56901 | -51.98575 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04b18d24-ddf0-3353-b62c-964f39a45c53 | -3.564 | -52.01881 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f660381e-d7f3-39f7-a2c1-ce88aa6b7c21 | -4.04725 | -51.086 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b60b89a3-7eb4-3f3b-a4ca-2981683f2b1e | -4.03397 | -50.87882 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6904551e-278d-3023-a10f-e974cdda142e | -3.97685 | -50.94312 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04aaab2-33e4-3c10-a4be-790fcef36e70 | -3.9116 | -51.19508 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0555386c-009e-355a-85a4-49876fa598fe | -3.91092 | -51.19965 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e7e653e-a405-338c-af5e-70e7051e30f0 | -3.89984 | -51.81925 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06f382d8-b62e-3884-ab91-858f45634d02 | -3.88894 | -50.9905 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a4dcc39-170f-397c-878e-c21468d929cb | -3.88824 | -50.99511 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8bfb85e-59fd-3c9f-ae21-04d67accb729 | -3.88322 | -51.02782 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b920075-6f75-343e-9e2a-ab53962e2d1e | -3.86566 | -51.82267 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d3aee4c-aa63-3a21-9ed0-943c74c2de96 | -3.86487 | -50.8903 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 022d2886-2305-3c48-a4a1-59e6bde38084 | -3.86266 | -51.81787 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f7f5125-ac7f-3d09-8268-bf64c4798083 | -3.86199 | -51.69978 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cf170b7-38a5-330a-9bf3-680edd45862a | -3.85901 | -51.81735 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f03f6540-bc7b-3ed6-807b-bb11015882d1 | -3.85897 | -51.69493 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32a5c680-5302-352c-947d-e66eaae3bc66 | -3.85831 | -51.69925 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ca483c-b0b3-311d-8cd0-9241ee6edfca | -3.84613 | -50.98871 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68d3c6dd-ce07-3885-a94d-665db09d401f | -3.84244 | -51.90105 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08a16e1c-0a06-3bf2-b608-750f797132b4 | -3.8388 | -51.90051 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4ffbffe-0c25-3dfe-b4e8-bb711cca1a11 | -3.83142 | -51.36561 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 650f2eca-a440-33f2-afe2-66b8d530bc85 | -3.83074 | -51.37006 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4966f6e8-0aa0-369b-a3cd-18c9f114be0d | -3.81374 | -51.0746 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 094090d8-4f6a-33e4-9d67-d8b95f61d110 | -3.81087 | -51.07676 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d52d4cb-e451-36f5-b8e2-aefe34e9149f | -3.80993 | -51.07409 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d31b76b-a435-3c76-aa7e-e2de313393de | -3.80115 | -52.00138 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2ab09c-d042-3edf-baf0-2fa5633aa757 | -3.80079 | -50.96544 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f584a7bf-c026-3d30-b2fd-6ed01c071ae2 | -3.79754 | -52.00079 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecf33bea-17ad-301b-a745-20a73cdc2577 | -3.79697 | -50.9648 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d9a6b3-520e-3728-8424-af58e7bea393 | -5.50963 | -51.42873 | 2024-10-29 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fa5a901-65e2-3af6-85e1-de2b021c4573 | -5.41288 | -51.56318 | 2024-10-29 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b5dd2a0-3cce-352f-b2ee-31e9597dd235 | 1.0114 | -52.21757 | 2024-10-29 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c757f7-533c-36c0-8d52-e06529ae3fe2 | 0.87047 | -52.49651 | 2024-10-29 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9194425f-b0ba-37b3-a554-61942261a8f9 | -0.31414 | -51.71726 | 2024-10-29 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1187a9e1-cbdb-31e9-9886-08f02deba184 | -0.22301 | -51.54146 | 2024-10-29 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc75a869-a2b6-3a33-884c-ebe21ae05e97 | -0.13329 | -51.56128 | 2024-10-29 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30f82b43-c9fb-3a14-8494-a649649591f9 | -2.17463 | -51.96621 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e6b92f7-cbf3-3f8b-bdea-7debb0b77c71 | -2.04616 | -52.07714 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d24fb472-866d-34be-b9f1-5dae881b73a4 | -2.04495 | -52.08503 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fb0889a-45c3-3643-90b7-9c379d895989 | -2.04434 | -52.08896 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0265ff74-d0ab-39a4-8735-45b75c4c22cc | -2.04263 | -52.07659 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a3b2f62-738a-3f35-8885-1a0c25c59ca4 | -1.99298 | -52.09417 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25132ec5-301d-3c2f-aa0a-c5a50ca23c9f | -1.9807 | -52.0802 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea2ffd46-343a-3e57-91ca-16d36f76ed65 | -1.97717 | -52.07966 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b6596cb-f875-3376-bac6-cf6fe3946a89 | -1.56188 | -52.10731 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cff551e-a91f-3f84-ab01-78b5660e5d5c | -1.56127 | -52.1112 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88781d7e-a43c-3e85-a00f-2b3e97e15639 | -1.5483 | -52.12509 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e17ccad-aab8-35be-aeb6-cd3c760f997a | -2.23183 | -52.22874 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c589982f-16ed-3dd7-ae58-c8438a4c14f2 | -2.23123 | -52.23264 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49d50ecd-1162-36fe-8e17-3ac658c15e76 | -2.22831 | -52.2282 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b65db4-cff0-38f4-b0e6-6c79a60a7c39 | -1.89579 | -53.00608 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8e4f4b8-4097-3bc8-8a08-fc8befa4688a | -1.89523 | -53.00973 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d4b0d94-a4e5-3f85-83ab-294e1098975d | -1.75367 | -52.30949 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350288c5-a91c-3182-b8cb-47869bccd9ec | -1.75307 | -52.31332 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c268b6f-a52d-3bdd-a92c-56dbf5f4c097 | -1.75018 | -52.30895 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cad3f6f-6f0a-3362-9b8b-0896609a22f4 | -1.74958 | -52.31279 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 641d979a-0b4f-39da-a9e0-da40568a506d | -1.74826 | -52.34393 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 291822fe-07ce-3f7e-ab10-f2f384eb6ba8 | -1.68622 | -52.73845 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7951226c-019a-3aff-8a9e-23e873d223a3 | -1.68564 | -52.74215 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef30770d-b6f9-3d28-94b2-56f7bbb39bd8 | -1.68279 | -52.73792 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c451ff4e-b305-36fc-a43b-3ed927968c5d | -1.65889 | -52.66587 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78d77033-e4a9-34fa-8965-d0bb3619396f | -1.65831 | -52.66959 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c076182d-7e91-3784-bc4e-80b5bed0aece | -1.65545 | -52.66534 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 844d25f2-1df4-319a-8037-3f3043f2faf7 | -1.61686 | -53.33286 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e5ea47-c402-3ad1-8cee-7aa026992fce | -1.61349 | -53.33234 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f54d921d-0273-32f2-9cb7-fc46920c3283 | -1.59433 | -53.19042 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18008948-596d-3859-8558-869b27cc2f5d | -1.59321 | -53.19756 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2bd0906-2694-32bb-ba67-aa8d41b20959 | -1.59095 | -53.1899 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9353cd0c-f7c1-3fd9-8f58-673300060965 | -1.59039 | -53.19349 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 911b09e7-94e9-3f58-95bd-bc46f63ba83f | -1.58983 | -53.19708 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c162c210-f6cd-3e8f-87b9-2fd0b33f96d6 | -1.58757 | -53.18937 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 516f0f61-9b8f-3038-b454-6d5ef5ea6ad1 | -1.587 | -53.19299 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c92f792a-56bc-3456-8c64-7b89ae737bf5 | -1.58644 | -53.19659 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fe1b2fb-385e-3df9-8e13-fa75cb2dc492 | -1.58475 | -53.18524 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d37200de-4df2-3b59-b05b-1b17171e7886 | -2.06178 | -52.13979 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 463e20ee-37e5-3213-b4c5-be6c00ceb447 | -2.06118 | -52.14371 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13eddcfe-942b-3e29-9514-68e5c873dee2 | -1.98945 | -52.09362 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README80.md)
