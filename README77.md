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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3265fb02-fc54-3cb6-9e5f-472e5b6ab2b0 | -15.63903 | -52.57277 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ad351c3-e271-3190-800c-0834429cb86c | -14.95257 | -46.81052 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5562b97f-7d11-3547-85bd-19cd795b72ff | -12.1181 | -45.12824 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51330186-f999-3425-9531-92a13c5a19ec | -15.37752 | -47.30726 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5db29e45-c1a8-38c0-932b-9e3a4e5e7c69 | -19.72258 | -43.90653 | 2025-10-08 04:40:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46e9c8ac-ea9b-30c8-8f31-de17b9d16eae | -11.16437 | -54.86285 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40c9bf23-c043-317d-8501-6625ac93b02b | -11.17557 | -54.89024 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 626d5611-ffcc-3370-a2ff-b679c619c0b3 | -11.1549 | -54.87135 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24fb69a7-012b-38eb-bcea-7ff88ff69b86 | -11.12003 | -54.03732 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da7c57a6-ac04-377b-b8eb-587d2fe65057 | -16.2902 | -45.24255 | 2025-10-08 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5876fb62-3123-30ac-98ab-1a64a175b308 | -11.16395 | -54.88811 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 09ee6556-2a7f-3fbb-9b91-43e4aabc8c44 | -15.99117 | -50.84596 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ca5b993-2ec9-368d-8954-02140db30199 | -13.27474 | -48.04295 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c677f5c2-c3df-3ce1-a911-9b93cc6f7e33 | -10.66893 | -54.69795 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7efb74aa-5008-3de3-963a-bbdaa8f514db | -14.70952 | -46.00912 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48dc7ec4-9bda-30c4-8527-f49a27a050dc | -13.34916 | -47.55816 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98815eb6-a09f-3c6e-8cdc-4ab45f86ef9d | -11.38286 | -54.3417 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a26bd994-aa65-3e16-becd-f862122079ff | -13.09619 | -47.98142 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b964cdf-f467-3dfb-a349-d9666478f1c9 | -15.64201 | -52.55439 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd4dac05-ea29-3f71-9187-d231bc3eb1f7 | -12.35077 | -50.28916 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672aed72-e2f1-3db7-99e1-f76d75c2d934 | -11.18718 | -54.8924 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83551308-ec08-3c25-9ea7-9ccda3701bfb | -13.69584 | -47.94986 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3924560c-5f87-3f04-8316-eafff86c8355 | -12.92729 | -54.71732 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0feed8d5-b232-3fad-9fff-b3d01a16906e | -18.02495 | -51.14466 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e12e4ce2-0083-3bc4-8cde-13948eff0f0e | -14.70799 | -46.0823 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1af0182e-957f-3f43-93a6-126c1dab1497 | -15.31104 | -46.15936 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 585a2f85-e9da-31d5-9936-bf9568761522 | -11.75404 | -50.92787 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46c99c35-f41d-3ea2-a4de-cea4a6b639b8 | -11.9572 | -51.46254 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5084783b-1f65-3e93-866c-73efbf615e64 | -18.02668 | -44.31367 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec50ebd-e8b0-37c9-ba57-eebfb143e3ac | -15.16668 | -45.74283 | 2025-10-08 04:40:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27b117ab-f6fb-3d49-824a-8da8c86312b7 | -19.15312 | -43.32052 | 2025-10-08 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6caa3250-3a44-3f12-a262-aff022e44b3e | -11.15102 | -54.8707 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8cc1530-f6c7-39a7-970b-d9071f24dbad | -12.24905 | -47.87375 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9a73ca3-56c5-375c-9930-ef96ab1c0848 | -11.01763 | -52.31814 | 2025-10-08 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05773175-2392-304a-bfe6-c85ea9be13d3 | -9.78981 | -59.96756 | 2025-10-08 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d374ffc9-ddb8-3280-81ce-535efdc9c0d1 | -14.61468 | -52.47054 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91581d03-0a64-3961-9dd9-35282718664d | -18.44796 | -42.90876 | 2025-10-08 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| da6c6c1b-4c76-31b5-ba6b-4fa6fd0dbe44 | -14.79697 | -41.63292 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e442997-fbf0-3cea-b63f-91cb6a55df92 | -15.70019 | -47.51081 | 2025-10-08 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d1b5d24-5426-36e2-bf93-c9acebe303b6 | -11.16739 | -54.8684 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d5f4cd5-878d-3b5d-bf76-79e5135c7241 | -14.62449 | -48.13798 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14d76353-1037-30a9-976b-ac850cc8d7e9 | -11.74946 | -51.48682 | 2025-10-08 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5913586f-d30f-37b1-94c9-30ffa2f5ed4c | -15.29629 | -56.92033 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9b00a37-be91-3eb1-a962-e3434c88feac | -13.73106 | -45.70535 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1831e190-1ecc-38dc-859e-03ad41f8d7a7 | -15.25231 | -50.20316 | 2025-10-08 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25e81c74-b91a-3471-ab68-91e67ee7a347 | -18.01805 | -44.94216 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290ed879-7f83-3f8b-8447-5dccce99c727 | -12.38679 | -51.13612 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 675eff7f-c623-3e7d-9420-57715a72873a | -14.91667 | -46.8138 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8bf4d6e-49f5-3235-8171-46a2f64e0a57 | -16.33862 | -47.04726 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdc99e50-624a-32e4-a94f-abb929c3d94d | -13.5577 | -51.80137 | 2025-10-08 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f73bf2-7b66-3b03-a2c3-cb9296cb3801 | -14.63849 | -48.31894 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ab20b0-dea9-3a15-a23a-fb6aa2421eda | -11.70648 | -50.94897 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b6be01e1-88bd-3d7c-a428-cb17d45bfa47 | -13.33952 | -48.01847 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a28c4962-fd02-39b8-bd0f-9b3f6645b1f2 | -15.63234 | -52.57156 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca048f4-9638-3ff1-9908-491efde192b7 | -14.89504 | -48.09265 | 2025-10-08 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da767bff-0d8b-3c0f-a6bf-43a6ee3fd0a9 | -19.33849 | -43.08474 | 2025-10-08 04:40:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5a695937-1f72-3313-bbe0-6533fe60b90b | -13.36795 | -47.55653 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5642731-a279-3172-964f-a868944b56fe | -10.07813 | -56.74557 | 2025-10-08 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c71c29da-1811-3ed2-86b6-e28c85e87b3a | -14.74882 | -47.86316 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea2d0c19-e45b-344a-8345-3d39372eaef8 | -15.03796 | -49.448 | 2025-10-08 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d58bce25-e07c-33c5-bb88-16af3b8a0487 | -16.58417 | -46.5536 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e755b0-2bb4-31b7-b3e4-54d466c57445 | -17.98109 | -44.9807 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ea0006-8f45-3bb1-816e-2661debe3911 | -17.36069 | -45.05656 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b7aea98-3e5c-3622-b0c5-e8841e893b79 | -13.07498 | -47.92836 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f2f5273-9566-30d8-85f7-73138df40369 | -13.64183 | -47.28162 | 2025-10-08 04:40:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb52de7a-4fa6-3caa-8b21-d4a972595203 | -14.8986 | -48.09342 | 2025-10-08 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cf26b80-ef06-3f69-9a6b-08f963214276 | -14.83904 | -48.4287 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 692b4b6a-2d80-38c8-b56d-02d31c363ae4 | -11.14714 | -54.87006 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80162ef5-3926-35d2-bf6d-f96b8122790f | -11.17297 | -54.85929 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8fd33c1-d417-321d-adac-04112cb60c4f | -14.95643 | -46.81112 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b1ef77e-2fb5-3a99-b366-fb4095608afa | -15.31462 | -46.16344 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf093217-abdc-359d-9754-5155dd0b612b | -12.49274 | -54.73428 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f8632f8-5326-3888-b8ed-cdca63985908 | -12.85476 | -43.81831 | 2025-10-08 04:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1b9d1ae-146f-3d86-b4e4-b5ca4924d4a7 | -11.75017 | -50.93085 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 23a70c13-f4d0-3872-8b7d-0e297f7bcd6b | -17.16361 | -56.61178 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2a9a0602-2898-3c73-973e-73dfc25ac6ee | -15.99839 | -50.82125 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b376e5af-2707-3695-9e6e-7356a8d2f1c5 | -17.28522 | -42.64857 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39ac6294-c711-3662-a4d0-635a5c9bca59 | -11.94101 | -51.47806 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2498cc5b-56b3-3112-b340-64649604b965 | -15.38611 | -46.27329 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa9f939-2e44-31df-a8bc-b6abc05158fe | -9.99127 | -60.01428 | 2025-10-08 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f9602b3-df1e-309f-93f2-5558fad6bde6 | -13.03294 | -47.89241 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7f869d9-c7f4-38e8-bb5e-f5d80ec884f9 | -11.14457 | -54.88472 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37231b45-4bc2-3acb-afbb-333a41fff381 | -13.33423 | -47.17516 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8320677f-e439-36eb-8e9b-9715fa86441c | -13.26088 | -48.48546 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c2a47d-067c-3974-a847-0f97764433cb | -11.1777 | -54.90096 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8d387c3a-a3f8-3743-85c4-f81f1a202f83 | -15.98895 | -50.83823 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4450f31f-243f-3614-9c65-104c9b4f6653 | -13.28466 | -48.46893 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc80cffb-8c01-38ce-8021-b4424f1300fb | -18.45691 | -42.52584 | 2025-10-08 04:40:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a704a3a-c2de-3d17-a869-a301c3b87ce4 | -16.29164 | -45.24147 | 2025-10-08 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f38390f-f5b7-30c1-85df-177d7e8c0d3f | -12.29957 | -55.10138 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d017cf-aa88-31ac-8e25-f08702cfcf32 | -14.70179 | -48.40351 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d4d803-a6be-3d5f-80ee-198ed7688037 | -19.50984 | -44.08096 | 2025-10-08 04:40:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 065fe4b5-cccf-3bc5-8401-dcb80bf18f02 | -15.94289 | -42.59995 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7002081d-055b-3b66-969b-4c538e6b0c93 | -13.38101 | -47.56865 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2510a071-b0b8-3565-8a7d-e272e1d52563 | -11.99041 | -46.77158 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75f15765-a1af-31fb-a70b-647be79158a0 | -13.06539 | -43.59059 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64df7bfb-3969-3a19-a20f-ed1fad50313b | -11.11558 | -54.04111 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ca0fdcd-0d12-3ae3-9f43-5e7d2095d8de | -13.0856 | -47.93024 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a970eb-cd91-3195-a938-7e80c198588c | -12.64047 | -50.56332 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3e749897-4575-3ac2-9057-f7fdbadabaa7 | -13.03591 | -47.92213 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README78.md)
