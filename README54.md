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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c540c2dd-2b71-3ea6-8bec-5dddf6ac9198 | -1.2591 | -53.36541 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f3a7bb2-7432-34ff-b7de-04ee19b715f4 | -4.65602 | -49.0217 | 2024-11-20 04:50:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b500b54-8f3c-359b-b0c0-ed3b7854275a | -1.06363 | -52.39164 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d7f7b24-b161-3ea8-a4b5-038280d919de | -1.92638 | -49.52115 | 2024-11-20 04:50:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e707a4ae-7f7b-3599-a834-20e0700fd6d6 | -1.90956 | -53.33577 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b605e64-0ecb-33fc-8f3c-e307028f4608 | -2.87085 | -51.79009 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca145dc3-5021-34f2-9515-409e2dea36e0 | -6.82292 | -46.77659 | 2024-11-20 04:50:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb27e22-8bf5-36fe-bc9e-4590a7f32863 | -7.17607 | -45.03978 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d18db35-90f8-3c46-b199-533078d32133 | -0.93694 | -51.64986 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a088350f-3c9b-3cf4-b429-0a003336b33c | -3.10544 | -53.74269 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc9bc84c-3aa2-3711-9260-1f6eb8ad7026 | -5.59514 | -46.17511 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3ec22ee-bf40-3296-97d6-55bceeb57edb | -2.17965 | -48.40552 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c643e018-86ad-3f1d-b4fb-fa544839a11f | -2.7623 | -54.07675 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9bea3a0-0c70-3015-9387-ccd42b2c151e | -0.80643 | -51.49182 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5a142bc-0def-300c-a5d4-970fd5387c8e | -2.89068 | -41.76029 | 2024-11-20 04:50:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64720cec-5c0a-3323-bf83-5a074fc530fe | -1.205 | -51.77697 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7a9653-6d70-37d7-bb35-5563dd396ecd | -3.05257 | -54.40964 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b72d62c4-5151-3f6f-87b1-328f7004793e | -0.97698 | -51.71981 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7abada61-dfe5-346b-a23d-900ff12af0af | -2.60645 | -48.25027 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 611d0555-7da5-35a7-9911-04b7cea4c4de | -3.76403 | -52.13875 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ea35a69-41b6-3699-aaf7-a738565a540d | -1.97219 | -53.13858 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0acf858f-79d9-39cc-ab85-ae2a4a986839 | -3.71207 | -53.75292 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69445fce-dff8-3933-b9c2-77e149eff276 | -1.52693 | -51.51601 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3c00fcf-a53a-3495-990a-06a821d36cb4 | -2.62443 | -54.26475 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c2af21-dffe-30c2-ab95-75065f329515 | -0.8018 | -51.24067 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84292273-d8ed-3159-a242-49021895bc07 | -2.81057 | -54.02104 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce9b0418-6bb2-37cb-9c8a-4c48d4522d09 | -3.28135 | -53.828 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f5b31ba-23ad-3800-b88c-99db5de5ff5a | -2.62836 | -54.28565 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7808887-583d-3d43-9653-2e31b8ad5234 | -3.50649 | -54.70303 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5906477f-42ab-387f-a27e-79bd4378b74e | -9.17382 | -44.72989 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7d94c73-f97c-3bcc-887b-5468d48fe758 | -1.26986 | -53.40941 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbd5337-daaa-349c-a7b4-69255d0813e7 | -0.90953 | -51.78023 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28720639-b3d9-3884-8c80-91ecb9388ffc | -3.28703 | -54.11692 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 604067b1-c828-31ba-a86d-61b59444dcc3 | -1.24213 | -52.0351 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c60aa3d-ed7c-3460-b198-3bcd78fdc0ef | -1.24932 | -51.75201 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f3b66d9-a8ce-3612-ab0a-59311b89d148 | -2.19223 | -50.68173 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 994eb78e-f79c-3774-ae34-e59283d8bd43 | -1.07405 | -53.18877 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78269e79-e5dd-3f16-bd08-da8a3e3a57a8 | -1.21945 | -51.79339 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff7fef9a-49cc-3c01-81ee-9f6aa7a95b34 | -2.83165 | -54.00785 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceb88869-a196-3e1e-8674-18d1dde02696 | -2.37626 | -49.83784 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94c7126e-2ae6-3fc9-8e24-41b0d7efede2 | -1.63032 | -52.62491 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaaa5441-4d7b-341e-8e46-30876e78b717 | -2.75244 | -45.70736 | 2024-11-20 04:50:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4c98082-5630-3a73-9ec1-aa55b949dcc4 | -2.34977 | -48.60497 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc0c7341-988e-39ff-97da-8a015f8bfb11 | -2.45316 | -49.1425 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3da753-05d1-3613-9b31-d2f4d20940e2 | -2.70976 | -53.17743 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d07b7cbf-0330-3310-b2da-16fee42fb83d | -2.83452 | -54.01224 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d68725c-0578-329f-80e0-408bc2ce99d4 | -2.30207 | -49.00124 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0937cb26-fa44-3d52-90f2-90cfa36305d1 | -2.58054 | -49.20479 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554e8002-9f66-3dc3-b01c-c7aa20d81d3c | -1.85376 | -47.8258 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97fd6bab-a282-30b0-ac4b-06b795c2aa7e | -7.55379 | -45.25964 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ad755e8-18cd-3f7c-b66d-e8e633d4f140 | -3.81381 | -47.79768 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cbb6bbf-360a-32a1-a6d1-baa825f6a0b6 | -3.87981 | -52.23878 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71556973-69eb-3a34-b207-cca509e59d87 | -2.66882 | -46.61306 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 767b7d4f-c49b-3b39-95b0-8be56beb20d4 | -1.23603 | -51.74994 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c6da912-b62e-354e-8961-d69ccb7941eb | -1.66982 | -47.47651 | 2024-11-20 04:50:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 921785ed-bad9-37df-a99f-b61988c2e477 | -1.19998 | -51.76556 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa0a1f10-bd91-3a10-9720-fcf8d992e636 | -2.51466 | -48.36279 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22625295-a9ec-3903-b7da-5b3fda6780a5 | -3.78854 | -51.07927 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a1b3a0-0517-34c9-9e15-fc4f79ebcf48 | -3.76349 | -52.1422 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf9de2ae-1e6c-3401-9eda-37e6ab2ace7f | -2.57065 | -49.19933 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3392662-c108-3af4-a36b-25d647629965 | -2.16349 | -48.92095 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ea4577-e108-3e36-b595-48b51552c738 | -4.35821 | -50.6966 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8854949a-acbd-3936-98cc-b3bf6978b345 | -2.74731 | -48.56885 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72cdaceb-fe4c-3a58-af43-2c70211d4ba1 | -2.21624 | -46.48313 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad12c2dc-6df5-31d1-a535-d1278c2c79a8 | -4.32526 | -49.38992 | 2024-11-20 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30fe70ac-e12a-3b43-8681-299bfa63f853 | -2.34709 | -54.7871 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 951e46d4-d62d-3676-b1b5-facb6849ae90 | -8.73472 | -44.08727 | 2024-11-20 04:50:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a58468-e454-3b23-8034-0fb0f62bfdeb | -3.88646 | -52.23981 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8173b9f-01e8-3866-ad67-b8103bfaac39 | -1.54524 | -51.18382 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2388647-48b9-3645-8ebf-ffa3669a96e8 | -2.63492 | -49.18053 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8bd4bdc-2126-396c-9927-fff31231d4c4 | -4.24907 | -53.67001 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef826ecb-08cf-3bc4-bb91-6c21afb7d1fa | -1.619 | -52.478 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc3f03b5-ade7-3f80-a20b-025e7ee6ec40 | -3.03517 | -49.45912 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb1841e-a118-32f0-be96-44b83b134445 | -2.85178 | -53.97169 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fd6560b-deba-393d-ad21-b41421e32dd9 | -6.41193 | -47.51139 | 2024-11-20 04:50:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eb9345b-717d-3f55-8b27-73d452728ec8 | -3.29676 | -53.85677 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdd42979-25df-3fb2-bfa9-532047e67ca2 | -1.33398 | -51.85719 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ee2215-148d-326c-9360-7be260727347 | -2.26943 | -50.58256 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86605dc1-3d63-38d9-80d4-af946e075b43 | -2.92568 | -53.07086 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 3b4bce83-a9a7-3cd8-a1f1-61cbb483a471 | -1.45821 | -52.67847 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a4c144f-53f3-334e-9cc4-f5fd597d2d76 | -1.64258 | -52.68483 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5380752-0fd2-3ab6-9250-142e9e7cc76d | -1.20697 | -53.69575 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3afad8aa-ce34-33f8-bb2a-1365bf6ad7f1 | -2.26319 | -48.80973 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f96da46e-2cc6-3d6b-a67a-441d790a03bc | -1.74909 | -50.47299 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d63f002f-72fd-3e04-81af-13382bd4ec4f | -2.95556 | -48.32724 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dccb9a8-c1f7-3e8b-bb8c-caace70909fa | -2.35907 | -49.07691 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5277c5b0-c999-393f-8c40-7c59837f40b2 | -1.25565 | -53.36487 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 04cca35c-2299-39c3-8e48-fec87d4a8f0d | -3.08435 | -53.26112 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed699085-70f9-361f-bdff-c3ab76788d4d | -3.51258 | -50.22932 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18f9938c-9b5d-35fe-868a-7c59d9514301 | -2.83309 | -46.67786 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ea9e507-e312-31a6-8ca3-57ecce310fda | -2.8707 | -54.48018 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a06ee35-5a17-3251-9f64-3236f928eb3b | -3.01401 | -51.00874 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecce0466-074e-35d5-afee-8be8c298340e | -1.19895 | -53.67843 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 136e5d96-8088-3de9-886d-deba02dfb811 | -2.27947 | -50.58411 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b1ce52-641d-300d-afd6-f577614b8bde | -1.20778 | -51.78095 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 410c3b21-f162-319a-88d5-9eff9aa0c733 | -3.18854 | -54.32538 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e3e5a49-8d6c-35a5-a368-6b39b9a29d42 | -2.6843 | -46.24119 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c2bc9fa-b04d-3ea8-899b-5a1407dae234 | -2.13614 | -49.11963 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 149bb1dc-2e08-3182-ae96-bbd307c801cb | -2.16627 | -51.97 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb29d893-a569-3c05-8017-8563a62621f3 | -3.42622 | -53.28857 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README55.md)
