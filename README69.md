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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12e539e8-add3-3f55-86e5-a22fc772e5d5 | -2.67636 | -46.6132 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae018153-961d-37cb-a437-1cb7bf2e9d8e | -3.30168 | -53.82719 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ccc7a7a-eaba-3556-896b-fa7a5cefe2e4 | -2.36478 | -50.4196 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ee0debc-e62c-3535-9c28-cc4239198818 | -2.63273 | -49.89959 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d949f3ad-4a8b-3b0f-8080-66bf3bf74002 | -3.06804 | -53.26593 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c34a643d-7207-3cc6-8c64-a3935adfb037 | -2.38212 | -46.78806 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed325895-3a1d-3a80-a9a8-a520a93c2dad | -3.60088 | -50.37341 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aec73557-0639-3bd1-a108-f8aa0606d0d0 | -5.31158 | -50.57057 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eca702b-77ac-34a5-8e43-6d562a1e3214 | -3.62654 | -51.49755 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7e9742-9eae-31c1-af17-ffbad0ca2932 | -2.2937 | -50.58928 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e821aff-97ea-3c11-b2c1-3469ce95283d | -1.32831 | -51.67787 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73508f46-2d7a-33b8-a8d6-9a9e811dc84e | -1.0976 | -53.36246 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 195e333c-72e0-3852-bba1-88d45450393c | -6.71178 | -47.2718 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fd02923-a320-3b54-9b3e-9c12c5a2c552 | -1.10798 | -52.30413 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4c4f992-78a5-37be-9404-edd3f968d314 | -2.08851 | -50.64631 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4194fe52-299c-385f-8d22-28a8d35620a3 | -2.63442 | -49.91046 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68f13778-74ba-3322-b191-6835c8e664e7 | -2.8056 | -49.77139 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ede5be19-0484-3b8c-9d41-cca92ef265e5 | -2.28322 | -47.91153 | 2024-12-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0a016f8-d4d1-3341-985f-a6ee99858f0e | -3.26517 | -50.05194 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 912d3421-fbc1-3345-90f8-f18d99f88271 | -1.69949 | -52.46399 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca2071b0-622f-3f36-b578-98d31a598940 | -3.20047 | -51.25715 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee93afea-537b-35b2-a09e-7c4018114a48 | -3.11769 | -53.98295 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 350f8d4f-c35a-3ae4-adb8-0b4a68b4f82e | -3.75852 | -52.44671 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da8d7ec7-0d78-3298-9e64-2a920528272e | -2.28515 | -47.50407 | 2024-12-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 923f89ea-9972-3330-b817-84fc070ab4e0 | -0.82186 | -51.60778 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd00b9f5-65a7-344e-9889-76ad81ae3c0c | -2.46381 | -46.56615 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0aa6c4d-05ef-35f1-bc63-e1a9cd17b54b | -3.37967 | -50.41958 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ee45f3f-7bf3-3c6e-ad5b-358c9209f504 | -6.18671 | -44.42505 | 2024-12-01 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710545be-7a3c-3812-9ae0-489a2a554d08 | -2.20093 | -50.57854 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3af26d21-412e-306d-b90e-e99128856393 | -3.72889 | -49.94384 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eae980b3-3081-3427-9f9c-874d084f65d2 | -0.81666 | -51.61834 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 464796c3-bc46-380e-9233-69e653723e15 | -3.28485 | -50.16459 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1783eebb-0f5d-35e9-b891-73c26e77cc8f | -0.09815 | -51.32823 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aa887ed-9ac5-3b72-b6bb-f27a31427923 | -1.94736 | -53.34247 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 977e1cfc-67f3-3e90-9ac2-b79e0088023d | -1.7677 | -45.51376 | 2024-12-01 04:44:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8574a62a-cd04-3ff5-8be5-dc2a5c4ae0d1 | -3.09294 | -53.29506 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb166c2e-a87e-3482-88a7-5a6ca20a5342 | -3.78879 | -46.69728 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 245c9457-fb70-3ee9-89e2-7cba5a20316b | -1.23179 | -53.36426 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9671d37-f4a5-31cb-92f5-f13912c08643 | -2.51915 | -51.83032 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9182f5c-6fbf-3a69-9772-a90d10f20411 | -3.1408 | -53.83735 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f256e6a-ed85-3ce0-a70e-d74cb2f77020 | -2.33782 | -51.2782 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f327eb1-4d6f-3b29-b703-261dc1ff755a | -2.10145 | -50.73744 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1122ee6-3a5c-3540-bbc6-6c9edd86b5f3 | -1.13373 | -52.09444 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a86fa5e-2bca-386a-be79-76d2f1e04f98 | -1.78826 | -52.74533 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 327049e4-e467-3438-9bce-6c9e6676fd43 | -2.83498 | -48.47225 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44fa49cc-5b4a-3cad-b030-a760558ab2ca | -4.85959 | -50.71204 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4666aa49-1474-3552-bcdd-3c0ff6b87985 | -3.33448 | -53.36913 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61601f89-186f-3e2c-8f76-4c359275dc0c | -4.54653 | -43.3021 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0aa884f-8754-31c3-982e-1668a189a25e | -3.25217 | -54.20397 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0040b63d-4682-35c1-a465-e1f3327961a4 | -1.31962 | -51.73332 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72aa3c80-7479-3e22-95c7-30ad65da5ee3 | -1.7597 | -53.63768 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdd3b779-e9f8-3928-a846-95f1c0dcc4f9 | -2.74895 | -51.66084 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 453cf74d-7593-39d6-8786-ecf8697ea460 | -1.35802 | -55.15273 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f70f63e-fc8f-3cbb-b264-7fd474cef57c | -1.39112 | -51.58941 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4305a28-c8de-34f3-abad-03497e88aae5 | -1.31503 | -51.74019 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5726f08d-b603-3d7b-b3a0-a8303e51aed6 | -1.23598 | -51.6225 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9c508ba-5e86-33ee-9e5f-4fc86c5bbe34 | -2.89077 | -55.22842 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6f8c4d-4202-394b-a034-d744ca4228d7 | -3.65168 | -50.21858 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60fc4d4b-6704-3bee-b321-cf8394a05f36 | -5.42398 | -45.11069 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ec01a04-e672-3130-b717-ba02c5ceb3ac | -3.46829 | -53.79428 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61e1d16-80b2-3c54-8ec4-c4a9f68910bd | -2.131 | -46.53547 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91a3569c-bbf6-30c9-8f4c-06ee6cf99fc6 | -3.49805 | -53.83333 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02685425-d5b2-3e8e-ad30-518aa51d9787 | -1.05439 | -53.21461 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d573248-d3b3-3378-a85f-1747faf4759e | -2.63608 | -46.8787 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c6e79ed-d154-353e-b57f-88ecc2cce26b | -3.064 | -53.6888 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ae7b651-c0a6-340d-9e54-6381abe6a616 | -3.29465 | -47.03009 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b829116-78ea-36ac-853c-87404646d64f | -4.01044 | -49.93771 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9872c902-d10c-38b9-93b1-ae86dc8ed8d2 | -2.73642 | -54.97254 | 2024-12-01 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4721739-106f-320b-b93e-4b109a52081f | -3.90928 | -49.82596 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e0677746-629b-3f6b-880a-35e2e1c542de | -4.52248 | -47.88029 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6438e63-60c5-3cec-8b97-f0452250a0e6 | -1.32475 | -51.74552 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d4324e7-265d-36dd-ab80-b1785b147fba | -3.60033 | -49.98779 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77665e8d-6c5f-3411-9ce1-716d9e098e49 | -2.60299 | -54.08593 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abaa2428-2261-39a0-ba7e-6d17f88e136e | -2.37246 | -50.39249 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a01460e-870d-3ecd-9314-ee8c83e2e26d | -1.31276 | -51.73225 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f41067f-c00d-3fd5-b504-1ab0d59749a6 | -3.32238 | -52.07521 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6b7dfbb-3415-3ccb-a02c-10a974b1069f | -3.09575 | -54.26876 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ae74436-17b5-371a-b7be-861d2b437e49 | -5.65353 | -51.47054 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c876f3a8-8235-3c62-a17f-109239b465f6 | -2.65567 | -51.874 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7e823c07-77a5-3a70-985b-df8390af79ad | -2.65464 | -51.68349 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 867848c0-f28c-389d-8c50-63f9501fa723 | -1.00703 | -51.72432 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1f5c13b-17b0-398c-9150-803a4f6b397e | -2.61668 | -51.81163 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99d6df3a-28a2-300e-9384-0875d4e6b83f | -2.82819 | -54.07916 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d1688e1a-498d-3ff3-bd8f-ac855ef479bd | -2.95321 | -51.75954 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109aa759-4850-38c7-95ff-99f3e97f64dd | -2.87186 | -46.79809 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ff7b00f-d720-3e88-bb95-d1707d6b40c5 | -0.82127 | -51.61147 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e341651-f036-3a99-b8c3-c132df0f8d3a | -2.91279 | -53.0677 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 204dd1b1-3299-319e-8988-852918e3e5c3 | -2.83639 | -52.9125 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb50961-cc59-3323-9aac-c996d032bd31 | -3.14868 | -45.36943 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 41464fd6-59c2-3e9b-a06f-dbcfe755ba27 | -1.56305 | -53.51436 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8c22293-59ce-3511-8460-d870b4d7d678 | -1.05667 | -53.22415 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bfe5929-9701-3634-8ec5-4eeaa9f4d8fc | -3.1209 | -51.31337 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff46c230-6675-36e7-9537-364c48a29ea2 | -3.30538 | -51.10435 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 387f8ee5-a9e9-3b06-a82c-b3872c5ec7c1 | -3.33758 | -53.37651 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be433799-91f4-35d0-ad21-4d2d32cfb24e | -2.67768 | -46.60449 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 797b363e-abdb-3392-8c6d-adfbf383c116 | -1.14685 | -48.32757 | 2024-12-01 04:44:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f828996-72ab-37e0-8510-992a5d0199b3 | -3.26729 | -50.21132 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16490a12-a4b5-3b66-ba76-211146ba0828 | -11.82838 | -44.22917 | 2024-12-01 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 588060ea-8ae6-35d9-a284-819ca7ecef7d | -8.93826 | -44.25262 | 2024-12-01 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cfb7041-9069-3004-9887-d82da6861410 | -15.56925 | -47.85552 | 2024-12-01 04:46:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README70.md)
