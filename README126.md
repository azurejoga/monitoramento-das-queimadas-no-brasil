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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448514a5-369f-3a0a-a158-4e9f1afccf82 | -14.95048 | -51.45124 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c2fb368d-603e-3481-a047-ceddc154caf0 | -14.94454 | -51.44491 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| eb667afe-69b4-323a-8bbf-1f9831c3c8e0 | -14.94396 | -51.45052 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 20bbc717-b1b2-3e35-b548-26f68e2c49ab | -14.94339 | -51.45612 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f8416870-0fec-35de-9c8d-7b522ec1b661 | -14.93744 | -51.4498 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d6ff2bdf-ec26-394c-8827-50c27fa1521c | -14.93687 | -51.45541 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 863bdb83-ebe5-396c-bad9-d354be832c11 | -14.93629 | -51.46099 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c2f45a95-abc3-342d-a8dc-9033832fc7cc | -16.12273 | -52.02147 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89fef8dd-3885-3e4d-be81-6615e0283515 | -16.10983 | -51.95532 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 674119be-0afb-36bd-9254-07582ddc0e0b | -16.10929 | -51.96085 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6442fc5b-42b3-3fa0-b79a-cd7676f13223 | -16.10876 | -51.96628 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 931a28af-7497-3c72-9fb8-a70a2b916a6b | -16.10802 | -51.95557 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 44c56394-3e3a-30a6-8004-56ed4d456214 | -16.10743 | -51.96117 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87d4caea-793b-36fc-bb93-f150bd25638a | -16.10687 | -51.96655 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53ce47b5-e52d-3181-8bb2-8bc297926b0b | -16.10399 | -51.94883 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ad7724b-629f-302a-ada0-56c3d47529f0 | -16.10339 | -51.95501 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6273b37-6cf4-3949-86b7-6570b346e560 | -16.10282 | -51.9608 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17ca9208-4ebf-3537-8302-b77a94a5121a | -16.10231 | -51.96614 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98554b6d-0900-3e46-8c23-18e991b9b4b6 | -16.10225 | -51.94872 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 27e2dc68-8dcd-38ac-96a5-717b18faeef6 | -16.10162 | -51.95479 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffc7e625-d2af-3681-8ce2-6829e1094e7d | -16.10101 | -51.96071 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b955976f-5e86-3075-9dfe-4004ef73389b | -16.10045 | -51.96609 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abf16db1-53c1-380d-b7b2-69c181c5bc29 | -16.09765 | -51.94728 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98e1f4dc-cf11-3014-9153-4bb2ed9a3b61 | -16.0971 | -51.95303 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 558f2d00-730c-37ca-92e4-ab68e04f1799 | -16.09649 | -51.95937 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b7948478-095d-352e-bd65-756b5f23a145 | -16.09592 | -51.96523 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc4bb423-6a36-3553-aaa8-95494a6d0de3 | -16.09592 | -51.94724 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d905caa-ffc2-3acc-b178-09e9d78c718c | -16.09542 | -51.97042 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ecaff494-68c5-3ddb-95bc-b01056e38ce2 | -16.09533 | -51.95293 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 69c4969f-217f-3199-9775-a3a0c37cb112 | -16.09491 | -51.97573 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed67f1f0-5eae-3562-8875-06f56c2e6066 | -16.09467 | -51.9594 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2a5094ea-3700-3d6e-bdf4-a9ca64145516 | -16.0944 | -51.98098 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e63ee36-fd3c-39df-8ea4-1837902875a3 | -16.09405 | -51.96533 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 11489736-5efb-3410-8bf8-b71e159a6e53 | -16.09351 | -51.97056 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cea776be-34c3-31a6-8407-30d16594fc44 | -16.09298 | -51.97574 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72d1f370-4d03-3601-9a49-cb00333dc87a | -16.09245 | -51.98084 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dc31380-8414-391b-b7b4-778464afec89 | -16.09127 | -51.94629 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c12290c-00c2-34c2-8cbc-2efdd417a843 | -16.0907 | -51.95218 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09fc063c-a9ab-3bc8-8fb2-1e5fa2de4529 | -16.09008 | -51.95872 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f030808e-25df-3595-8133-2e4c1e088466 | -16.08949 | -51.96487 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f41a3043-f9ac-3ac4-9166-2186b4b2860b | -16.08898 | -51.97009 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eb4b88e1-13aa-33b9-8e09-05d195bd08d9 | -16.08824 | -51.95896 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06780e7a-53df-3c2a-866c-842d4a0e2b56 | -16.08805 | -51.97983 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13d3ab09-fac9-342f-ad95-cd0357e23c8e | -16.08761 | -51.96503 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a74669ad-e9c8-3b11-abc7-2899a0aa951c | -16.08755 | -51.98497 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ef65f02-b4a5-396c-9d2b-a311bffe75e5 | -16.08708 | -51.9702 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| acf38a27-20b7-327c-81f7-fda97e142fed | -16.08556 | -51.98491 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8327fdbc-4c71-30f5-a2cf-cfed864e65f4 | -16.08503 | -51.9901 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 031afe25-1828-3fc2-94da-dde91576bdc7 | -16.0831 | -51.96397 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2c4b8146-7839-32af-b46d-476e6a24ba33 | -16.08261 | -51.9691 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1824770-ebbf-3efe-9669-e369ecf7bfa7 | -16.08125 | -51.96396 | 2024-09-27 05:29:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e7ff70c3-d041-3483-a8b1-f7c679967bc2 | -17.11331 | -56.18661 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 055fd1dd-c7c9-3b0e-8c84-bc0fd9769a6e | -17.11267 | -56.19238 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5ad26287-e682-3033-99da-f47a4a749c7a | -17.0923 | -56.37492 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e7554a28-2534-3ad1-a8c7-bb214d35aaa2 | -17.03059 | -56.15104 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fde014c6-700a-3b8b-920b-1c1182c6f92f | -17.02994 | -56.15685 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 33163ca6-904b-3e79-a9eb-b159f6cede60 | -17.02968 | -56.14996 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c7debaaa-90a2-35cd-a2ee-0b26a0fde7f3 | -17.02433 | -56.16206 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 818f5988-dcba-38fa-8670-87bf2a09ce36 | -17.02334 | -56.16097 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ebf699bb-5f40-3790-81f4-b9204035c228 | -17.02068 | -56.1498 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 18e5a155-7e5d-38c5-be3d-cf66c48a7c84 | -17.02003 | -56.15559 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 980c2b5d-e1fc-31d2-989a-80554f753914 | -17.01938 | -56.16142 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e59963fc-e2e6-39d1-9cd8-324b71863e3d | -17.01908 | -56.15453 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5721fe48-28ad-3f1b-97e8-22c76a7e8805 | -17.09719 | -56.37553 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 586c6338-4730-33f5-ae87-2f27100e6476 | -17.09394 | -56.379 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8534095f-38b4-3ade-8293-31123d619d19 | -17.08906 | -56.37838 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 864a8ab3-71fd-35d2-840f-e463d021acea | -17.03423 | -56.16332 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 58669143-d98b-3d6c-8661-a93a0aff86f2 | -17.02928 | -56.16269 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e49f5cf0-0cea-3b3e-a744-ce93ae3ae9da | -17.02898 | -56.15576 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 16a6b507-3a53-30a4-95b8-5a00f10471ad | -17.02828 | -56.16159 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e68fe37f-5a97-33a6-8a99-1c3eb2e6b6c8 | -17.02563 | -56.15042 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2950413f-ce4f-3db3-9ae2-e608ad792aa4 | -17.02498 | -56.15622 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f6d66f8d-06fc-3925-af0e-aed06e1d59a1 | -17.02472 | -56.14936 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d1c5c89c-c2b9-3507-b26e-8b6b3a6ff7f5 | -17.02403 | -56.15514 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9a3baecf-74b7-3476-89b5-f5b364efa59f | -17.02264 | -56.16673 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 84315f87-8244-3764-ab86-7797462f6e77 | -17.01977 | -56.14875 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d8dc7084-9a34-3d20-b77b-f2ac8845e272 | -17.01839 | -56.16034 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a533aa9a-c10d-361e-a3ff-26212515fa80 | -17.01573 | -56.14915 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b364e8fd-4254-36f5-8504-d3343915e3f6 | -17.01508 | -56.15496 | 2024-09-27 05:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 29dc5675-0e5c-3666-9919-cc0f3dd3d350 | -13.95953 | -56.16387 | 2024-09-27 05:29:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bacb6fe6-2d9e-386d-85d6-d51a699b35ad | -16.968 | -57.94104 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e90d135c-6540-31ef-a92a-956573c7d66f | -16.96416 | -57.93604 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3224b71c-cf4e-3d69-b194-9cf7ee6798f7 | -16.90193 | -58.00784 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 16d2c4b0-71e4-3905-9ab8-b1032255c965 | -16.89374 | -58.03022 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 390ae9da-efca-3e38-ae4b-5717e3c43fdc | -16.89105 | -58.01661 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 44722aa9-523d-3380-bd9c-54d0d09abc59 | -16.89049 | -58.02095 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 82fb7637-3be6-33e4-aa85-299f76ca1f3e | -16.88938 | -58.02964 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9f86f96b-c7af-375e-86c3-dc653386b170 | -16.88772 | -58.04263 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0b4b6953-e549-30bc-a74e-03e66c55076c | -16.88669 | -58.01602 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c2db6ed8-fef6-3b15-8f07-a3e2b444e36f | -16.88613 | -58.02037 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f78ac669-b4ad-3d6a-90cc-5953b3b9f0a7 | -16.88558 | -58.02471 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c34c0196-25e2-3adf-abdd-dabe16c5c05d | -16.88503 | -58.02905 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7ba01e54-77f8-314f-b105-9a101fc811ac | -16.88177 | -58.01978 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 60fd301d-02ba-3b43-b43f-050403e81a10 | -16.88122 | -58.02412 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ba053634-831e-36d3-a573-37a0e3c3e81a | -16.87631 | -58.02787 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 628223b3-f0f7-3b96-a722-38d9acaaca11 | -16.84052 | -57.7393 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 66d08668-59fe-3a34-85b3-0ba3ce416edb | -16.90145 | -58.00473 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c84149aa-18ea-37a5-ae5c-7561d69710b1 | -16.90089 | -58.00908 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 58ea0170-5745-35fb-b195-3c4061d00c0f | -16.89978 | -58.01778 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 16c05a4f-5bce-3114-99de-51bdfb4da692 | -16.89653 | -58.0085 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README127.md)
