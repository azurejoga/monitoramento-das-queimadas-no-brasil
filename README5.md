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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ceb7be7-41df-31cc-8978-e3a8816684d8 | -5.14524 | -39.46688 | 2025-12-30 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb3b611e-4674-3213-94f6-7bf61789d3d9 | -2.2248 | -48.11916 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a778a59-b262-3ead-9b18-49664af7cf58 | -3.98737 | -48.39943 | 2025-12-30 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4d9140c-dc56-3383-a201-d94b3d01a8a8 | -2.89613 | -49.50853 | 2025-12-30 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63f3b684-46ec-3496-8d08-652cad7a8df9 | -4.20146 | -43.63404 | 2025-12-30 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a00187-8195-365c-8292-9c79325be56c | -5.81991 | -39.08282 | 2025-12-30 04:31:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 08c5c925-a6fa-378b-86d1-be84382d50a1 | -2.09622 | -48.37471 | 2025-12-30 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e079c294-5dd9-3779-b105-34fd2fd2117d | -5.17478 | -42.89719 | 2025-12-30 04:31:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ef784e1-6967-3d6a-9262-6db70b339118 | -4.72995 | -47.13593 | 2025-12-30 04:31:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c1bea5c-79aa-37bc-9bf7-12b8387ed665 | -2.18304 | -48.01913 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7f9ab6-a5e8-3c07-9ded-fac8c730237c | -4.51567 | -43.69131 | 2025-12-30 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0376e8e4-2d18-3b1c-8444-7ec8ac5e7639 | -2.23281 | -47.72364 | 2025-12-30 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0724147c-4f1d-3aab-a7d1-303cf63f7fb8 | -5.31336 | -45.18121 | 2025-12-30 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f336ed95-da67-3f36-8c88-ed10871300ea | -3.09126 | -46.91398 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4773b74a-1063-3a40-9e9f-d902e60ae4f4 | -3.55324 | -43.60004 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4907d155-482f-3ea2-86f8-91dd8809fd08 | -4.61011 | -46.59705 | 2025-12-30 04:31:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fce28c33-69c0-3bbf-aff7-543ba23deeb4 | -6.0907 | -41.81819 | 2025-12-30 04:31:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7520b0a-2ca6-3c8d-b10c-aec5c2f89676 | -0.53176 | -48.52171 | 2025-12-30 04:31:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b7b9af-be27-30aa-8b89-126a4396efe6 | -5.31044 | -45.17681 | 2025-12-30 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 011474d5-6381-3cbb-a307-23a5d42c49f7 | -3.54447 | -43.60786 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bf0acbc-a2a6-391b-9749-b639dd99ba65 | -2.17915 | -48.02211 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 613fe34e-4498-347f-a3d4-06fa351e5b1a | -5.39643 | -44.68156 | 2025-12-30 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3f821376-cd48-3206-992d-84549752a5ef | -1.4914 | -46.09423 | 2025-12-30 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93c6aadd-3d5c-3230-9821-02c28e523f1d | -4.34312 | -44.12152 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d26790b-8258-31dd-8481-4081921c7e91 | -3.54819 | -43.60841 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60f671f9-3480-33eb-9460-24733ffc1f98 | -3.09456 | -46.91449 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02d566b0-4f02-357d-9031-0c0e2a4a8b4f | -4.60732 | -46.59304 | 2025-12-30 04:31:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80c92426-9abd-36c7-b6a6-1b1d7af806f4 | -4.17489 | -48.63481 | 2025-12-30 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e14358a4-0e49-3225-9422-968b8e4d9840 | -1.49636 | -45.88806 | 2025-12-30 04:31:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b08d436-cfe3-390d-8ca4-41af098f99ad | -2.98741 | -41.88169 | 2025-12-30 04:31:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3496a6ee-198e-34c6-88fa-55e97f9423d7 | -3.01986 | -49.43755 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51ee3008-715e-309b-8783-58e5222946d1 | -6.0816 | -40.42501 | 2025-12-30 04:31:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57973be3-9a1a-3417-a253-eec6db36deb0 | -4.00807 | -44.21165 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 508d7f2f-b6fe-3b17-8ae2-823e70939b2d | -4.3441 | -44.11615 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d8cfe36-109a-3209-b32d-3e4747aa2e70 | -3.55106 | -43.60192 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ac9f4da-b4a2-3daf-bd2a-19a7d3f5410d | -5.81946 | -39.08592 | 2025-12-30 04:31:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| acbbb1de-dfa8-3ca6-8dd3-bea75c498fce | -2.1408 | -48.00542 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ef28da3-462b-3f47-99d2-8f5fae5c7d1b | -4.21964 | -43.64841 | 2025-12-30 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0620fd15-0cda-3376-ba33-86a6b266aca8 | -4.33947 | -44.12094 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e9b0e78-e716-32d6-aaaa-adc4ee7c0c41 | -2.22015 | -45.5211 | 2025-12-30 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db868d7-2539-36af-a87e-bb4a6e3a96a9 | -2.13801 | -48.0014 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 948c56bd-7ae4-343c-9ee1-d0e06f80b3bc | -4.16569 | -46.76375 | 2025-12-30 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c296524-2ad6-3c24-aaa6-809ab61eebd7 | -3.02392 | -49.4343 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eef4d68d-bd1e-30c3-be3d-f2a01569139d | -3.17482 | -48.02843 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74e3cba6-2d09-39d8-80d9-c046bcd7d8c7 | -2.90021 | -49.50524 | 2025-12-30 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0ffd721-3013-3962-90ea-4e8168034748 | -4.45855 | -43.62973 | 2025-12-30 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 170f1751-bba1-3e8b-9e04-7d72e23df30b | -6.08082 | -40.42398 | 2025-12-30 04:31:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69901112-ca9f-35d5-88a7-b973f681a79c | -3.17149 | -48.02792 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce7f0c19-cbd9-3b8e-af3c-1481645ef03c | -1.84874 | -46.39809 | 2025-12-30 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf897cd-ce6e-3916-8ff8-a34926674b54 | -2.22814 | -48.11967 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57c415a8-ab87-3026-9cec-9e2256d9c052 | -3.02963 | -49.44296 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f1cb99-8ceb-3e21-9b14-2f897b80a619 | -2.22758 | -48.12318 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 857a1981-47a0-3079-90bd-c88f73d8b1fe | -4.34347 | -44.12041 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1963d4e-c1aa-3b18-8bd1-66bd311c9cb0 | -5.31395 | -45.17732 | 2025-12-30 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0f4d954-7099-3d39-a0a6-b56163414a9d | -5.4637 | -40.69727 | 2025-12-30 04:31:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 719016e0-f7f1-3128-a88a-752bb0a0c55e | -4.33982 | -44.11983 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87ab6ff4-8ebf-3b55-9b99-c94d58e71699 | -3.02271 | -49.44188 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb720c4f-3ad3-39ec-bee6-4cd0b8a18253 | -3.02617 | -49.44242 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a340b00-caee-3cd7-8efa-a43dbe052ca1 | -3.18533 | -48.0265 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 88126fa1-99c7-3faf-ace0-254795ccb3f4 | -4.34378 | -44.11728 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7c01ed8-85b7-3107-99c4-eee42694dc6f | -4.34649 | -44.12518 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1add22e5-18fd-3ecf-899f-556a1b35fb34 | -5.17311 | -42.89925 | 2025-12-30 04:31:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee673d1-233b-3dc0-93b1-fd429ca37af1 | -3.39499 | -42.1068 | 2025-12-30 04:31:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 51d66851-19e2-31ea-87a5-5c72c46df550 | -3.02903 | -49.44675 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b2ca3f0-22ae-3bdc-80f9-4f2ccc0a6cc0 | -3.5539 | -43.59562 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb9d678-0db6-32ca-bcfb-9d43b3a711b5 | -3.55037 | -43.60638 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12b9197e-a01b-3f7b-addf-21b8ee6aae23 | -5.3958 | -44.6857 | 2025-12-30 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 13b5f217-1b80-35ea-8a8a-db41e4ea36ce | -2.14135 | -48.00192 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85f2e527-c9cb-39fd-a555-63d6af850db0 | -6.24121 | -40.29662 | 2025-12-30 04:31:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 235667c3-c7d1-38eb-9db6-78dfb651cbeb | -3.55174 | -43.59752 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 206ebc51-15e8-3535-bea2-229efe4366d8 | -4.51782 | -43.69417 | 2025-12-30 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 259836ef-91c9-3c8a-8a05-2b7580fed3fc | -3.55697 | -43.60059 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a0f20f-ece0-3c26-b896-9766f1dd0185 | -3.01925 | -49.44133 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4cde93-dde4-3859-91f4-4bd0690aaed4 | -2.1797 | -48.01861 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc05ac1-2092-39a4-8600-bd958ad3d3ee | -5.48823 | -38.04966 | 2025-12-30 04:31:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b90a7aa1-f985-3252-8cbf-426e9fbee440 | -3.54886 | -43.60392 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ed49b59-bebe-3866-b9ba-5e256463302e | -3.02557 | -49.44621 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97fcf9d8-11b3-3237-a609-21ace5831434 | -3.17204 | -48.02444 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf29a7ca-2e4c-3f13-a5c0-9d81681a6648 | -4.26415 | -48.8384 | 2025-12-30 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79b8e53e-4f88-3a1a-b6d6-a47e7fc88835 | -3.02046 | -49.43376 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9c58565-3929-3e07-900f-539e6ce6de61 | -2.28961 | -45.6195 | 2025-12-30 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d8c2fc2-134d-3905-84cc-c49ad4448209 | -5.38385 | -43.18705 | 2025-12-30 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a02e1de-3601-3316-9194-5d01120acf82 | -1.84927 | -46.39463 | 2025-12-30 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 079a6c0b-a118-3683-b7b0-2e96afff79d3 | -3.5386 | -39.17468 | 2025-12-30 04:31:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3ebcb8d-5b2b-39d1-9e7f-32aa93a5990e | -4.17824 | -48.63534 | 2025-12-30 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2e7b5b3-5e85-34b3-bdc8-23b4bfd78419 | -4.60677 | -46.59655 | 2025-12-30 04:31:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8586813-1c82-3199-b1a3-46ca996de355 | -4.20229 | -43.63641 | 2025-12-30 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3826eda7-65b5-3073-a8f7-4e00c3b427d8 | -2.35113 | -48.07394 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ea308ce-510c-3182-ae1f-afa6a7f96267 | -5.38777 | -43.18759 | 2025-12-30 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90275ae5-9c63-37d8-b69c-4e83a2574cb9 | -3.55018 | -43.59507 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64b4a276-d756-33b8-a0ff-f3eb1280cb1f | -6.09305 | -41.81633 | 2025-12-30 04:31:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bd4d243-5dab-3857-90c0-e65c872cbd40 | -3.93209 | -48.05878 | 2025-12-30 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5c27dcd-c53c-3de7-b2b5-9a32796bb916 | -1.49303 | -45.88755 | 2025-12-30 04:31:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c61661e-edd7-38d2-bc6b-8278838181ee | -4.16515 | -46.76722 | 2025-12-30 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 914ce7e8-38e3-30fd-8813-5a6696249805 | -4.72446 | -42.04421 | 2025-12-30 04:31:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6465d38e-8449-39cc-a137-e138c97f8db6 | -4.34712 | -44.12097 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 175dcd38-4639-3093-861e-47ae830aafd4 | -3.54514 | -43.60339 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c20d7adb-2d7f-32b7-acdb-27740d24256a | -6.0913 | -41.81411 | 2025-12-30 04:31:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9940a193-8255-3d19-82ef-538f6166cadb | -3.54664 | -43.60583 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 81fd9e6f-e04a-3ce7-b6e4-e1a490d8cd5d | -5.34069 | -44.71077 | 2025-12-30 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README6.md)
