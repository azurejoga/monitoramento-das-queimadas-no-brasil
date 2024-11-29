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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2761d360-5881-3e67-a2e4-851516331010 | -2.8001 | -51.58827 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd1998d-d197-3105-8330-e5b457fb5045 | -3.26036 | -54.114 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40675e15-f4c7-3e55-8dd6-ab7c626928f1 | -1.19115 | -54.01234 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c90847b7-51fb-3541-ae50-b704c03d9106 | -3.69301 | -51.37085 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68a1a296-d292-3ca7-ae5b-f5e34ffde823 | -2.98084 | -53.28888 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| a9f8301b-15e4-33f0-b80b-0c4b692370e1 | -2.36904 | -53.65717 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02f4da17-e701-36f6-916f-22ab2f08a432 | -3.57904 | -50.33147 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90cb1022-2d5d-305b-8a05-c18ef52c8084 | -2.75679 | -54.0275 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b5126c0-5c8b-3017-aec2-218b70e071ea | -3.0568 | -48.52003 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e846be-206e-3480-a695-da3f96a136be | -2.91726 | -51.71592 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95d27378-704a-3f4d-8400-75c7cf07a1fa | -2.63102 | -51.77485 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e32fd4f-754e-3960-8f0c-82ea52953190 | -3.08164 | -53.29737 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb019428-8bbe-3072-a475-85e520d6670b | -3.98005 | -46.73335 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9edd7bb-6a44-3331-ae3d-e087ab918800 | -0.27408 | -51.62786 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18e0a9df-4ea7-3636-91f1-bb5fbadb4ad3 | -3.91205 | -50.10271 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f03da44-315e-3c4e-963f-c4a1d60e9416 | -3.72998 | -49.86712 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db001db6-649e-3644-9cea-99a53dd0400b | -3.38557 | -53.50695 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0e38d34-feb8-31aa-ad06-b67fe4a053be | 1.21195 | -55.9531 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c526df52-cbe4-3f0a-838d-578b7032fc77 | -3.49461 | -53.81304 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22fcce7b-dc10-3824-a65b-4f4d270a3836 | -3.81806 | -46.59386 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cb75d49-6dc6-37c7-b0a9-6b6751931c8a | -1.15539 | -51.69238 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d729a20-ff43-31bf-8eb1-3f9ccd3a1338 | -3.1125 | -53.99584 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61d71ccd-d8db-3f24-b738-4710a8111d8b | -1.12666 | -51.67689 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceb79db8-4118-32ac-b28f-4f4cf87b7045 | -2.26303 | -53.46514 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccc8a31d-6268-3acb-9e3f-15f939a7288b | -3.22577 | -53.8339 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed5e7e18-651a-3237-970b-dfc9fc560ed5 | -3.33802 | -50.51545 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c326579-ae41-3cbd-ab39-48b7a6907f53 | -2.85567 | -54.02591 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b7dd41-f625-3ee6-a058-2729a9a61764 | -3.53002 | -52.15693 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db954e15-91c5-3a9a-8b5a-34b6a01b5f69 | -1.69437 | -52.6179 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d47220a7-0613-3cd8-a774-27917ec8b439 | -1.31336 | -51.74243 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024f2cda-666a-342c-8837-f03f9b5d583e | -2.00502 | -51.17417 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fad2104a-f1ec-3067-8ee8-c5675190488f | -4.93085 | -44.529 | 2024-11-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 670c95f6-b0cd-382d-96c0-fc8dc860cb91 | -3.03338 | -54.02177 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6d67946-b2f1-3038-85b4-e327725af5db | -3.49589 | -50.46033 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13e448a5-9aae-3cac-9f9b-02d386e56e7d | -2.0394 | -54.67574 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f15da6e7-61ac-38e4-8522-a65e5fb064fd | -2.08926 | -50.72906 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b2ce403-1a38-30bd-90b0-a5bf90d7f20f | -2.80169 | -53.04171 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84585c05-44ec-3767-b54d-d248f308d70a | -1.66244 | -52.12098 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b20b6ad7-9d86-3aa3-b48c-361c16c400a9 | 1.22582 | -55.93864 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22ecf85b-9c77-3848-9d5b-213b430a281a | -1.2701 | -52.19796 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff5fc949-6609-3d30-b1c3-c40dc3ad5644 | -2.80115 | -53.04517 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22bb300d-3735-32ea-bee6-1e581f815649 | -1.71544 | -52.76656 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b4fa18da-d620-3205-a3a4-e5a379f965b5 | -3.12205 | -51.29475 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51bc589c-fb7e-36bd-a648-4a185c00cc7f | -5.24793 | -45.87333 | 2024-11-29 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2d048fd-8366-3ab0-920a-7c9c2fd2394d | -4.12102 | -54.91784 | 2024-11-29 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bace096-720d-3bf0-83a7-41e023dcd9c1 | -2.98125 | -53.89748 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9242ee8f-d6c2-33fa-81ae-1600a2bd740c | -3.08903 | -54.03391 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e6b7c6-de0b-3895-bcbe-cab50eee069b | -2.85683 | -54.04018 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0598fc4-8fcc-37b6-b46e-f5f1d7841d92 | -2.64953 | -54.06036 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b25f08ee-5ca0-307c-b209-4cb8ef985f4b | -3.29412 | -50.61093 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7526c154-97f4-3a43-9a90-15b11cbe0cc2 | -1.32181 | -51.75479 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cbe583d-85b5-37f3-9498-0da24ad13560 | -4.17791 | -48.62482 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13f0285f-a5ab-3a3a-b872-2b2046b18394 | -2.60912 | -46.56122 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f41d766c-0b51-332f-92da-589ef6f0fe9b | -1.4881 | -51.97459 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5d5f263-672b-3f63-a307-ba014f99abfb | -2.90018 | -51.57671 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d96e7909-1216-3e7c-ba0f-e9ca2e35b27d | -1.96878 | -48.3851 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f854cc2c-454a-3169-bbb4-54a39df00826 | -6.09796 | -43.96788 | 2024-11-29 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08f3e3bc-fbd3-3f94-892b-f29529288d0e | -3.33582 | -53.21719 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 614594bb-f19f-30ac-b515-64d815f147c1 | -1.68524 | -55.00508 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633697cc-a3d9-37d8-88df-b0a8f4a1652f | -3.15877 | -51.55726 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68b85c70-6e5c-3e67-aa1f-8053443b25b7 | 0.27801 | -49.80707 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feafc534-9316-36d8-ac7f-d87d8af05341 | -3.59153 | -50.37303 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d26bb81e-c6a8-3d40-b606-36e62ef33d6f | -3.49729 | -53.79586 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 558c6547-ca9b-37f7-b115-31c06a635d97 | -2.14715 | -50.61119 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e1794ac-bf60-37e8-980c-8a3135cf34f5 | -1.70111 | -52.64026 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2256afd-1dde-3b45-a58b-ae2380fcfd75 | -4.06707 | -46.82084 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8271cc2e-7405-3221-955e-534571ad76b4 | -3.41854 | -54.9051 | 2024-11-29 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a73c4ae-ac5a-35da-8c8a-97b7dc86c958 | -2.95919 | -53.88704 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2234f1a1-f06e-3811-8094-b4a5bdefdd08 | -2.64108 | -49.90796 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e01243e-1a07-3651-89f5-1208c22d6a50 | -3.50068 | -53.8175 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c8e2543-2d20-362b-8846-ae559246277e | -1.14741 | -48.33857 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76726c18-a5a3-39b5-ba54-23e17435f84c | -1.62678 | -52.70271 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 662c0775-90f4-33e7-8980-037172030679 | -4.47103 | -46.31262 | 2024-11-29 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f31b4726-cd5a-37ea-a4d1-61e029f048cd | -2.84545 | -54.09133 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e66ca52-dfd7-380a-9b99-6d10376462a9 | -2.01559 | -51.19044 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e2701c6-795d-34db-8e01-e5b771dfdccc | -1.39452 | -55.20299 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 499f70ae-f2e9-3196-93f4-ebea0e0876ab | -2.639 | -54.82629 | 2024-11-29 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da117f99-7e77-3937-a3fd-ec69294daf39 | -2.83891 | -54.11151 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e294b48-3055-3dab-82b2-cfa34a36c5c9 | -1.44404 | -55.19927 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddbb99a9-000c-3653-babd-0907161bbf83 | -3.22246 | -53.83339 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cf74e3b-c3b8-35a2-aa88-e04402fe0dd9 | -2.60285 | -54.27248 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b517c0-a7df-39aa-86a1-fb40312cccf0 | -1.36347 | -51.44095 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6663203-3daf-3083-9495-210c68720cda | -2.77523 | -52.90641 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40148a85-9a1e-3184-b759-9576894c852c | -2.6289 | -53.99718 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7a638a3-7d12-320c-8250-6e1eae8a1f60 | -1.79627 | -52.75062 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e01224b9-971f-3f35-99e7-8cc92504be81 | -3.32631 | -50.22285 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d71a684-8e0c-3afc-8ebf-f6349932ed93 | -1.68102 | -45.80119 | 2024-11-29 04:57:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ea128c8-3fde-3d5e-baab-1e7eeaf528ce | -1.42452 | -52.9541 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03f486fc-01dd-3df5-aa7b-0c09feca7510 | -2.60904 | -46.84143 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 232406f2-c119-309d-9e84-02281e18e7d0 | -2.53154 | -53.98908 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c517eed-a9b2-36a9-b3a0-55c222089aa8 | -2.25054 | -53.63183 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a41959d2-32d7-3179-8c20-a90c51f5aeb1 | -2.87257 | -53.9827 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d92e9e95-f431-38d1-84a7-c27692f2f049 | -1.09802 | -54.12912 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656b03c5-94c5-3bbb-9d39-e356571b489b | -2.2417 | -53.62344 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78b9aa81-3d75-3cf9-b334-fa71cf7419b7 | 0.94158 | -50.73711 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 666c717a-560b-3fa7-98c2-df9df68729ae | -2.85099 | -54.09925 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04ecf68-b60b-3608-a7d0-ef211b0f7154 | -1.49784 | -52.43757 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d09f60a-15c0-30cc-bf11-a68b49452eff | -1.68344 | -54.23531 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 295844e5-e770-340a-8218-1ef0bd8eed65 | -2.58625 | -54.09653 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8ecbd8b-f93c-3d15-af85-67ff3fc0ddd2 | -0.97387 | -53.68481 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
