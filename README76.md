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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3ebe921-8d4c-3d52-ba25-54f35bc13a14 | -22.57965 | -49.21885 | 2024-10-08 04:38:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebf57af-d8f9-35ec-9b0f-7d9f69ae21c1 | -22.57907 | -49.22298 | 2024-10-08 04:38:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b92a459-7201-3b75-9a71-885edee765aa | -22.5756 | -49.22245 | 2024-10-08 04:38:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a2910b5-48e9-3fe6-89a3-a4e3d6999fc1 | -23.28832 | -50.08461 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23eea8a1-6903-3356-b423-37bc9248fc3d | -23.14878 | -49.81779 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd22f32c-1b61-3689-94c8-f435fd7ed1e6 | -23.14536 | -49.81727 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a86461f9-f490-387c-9456-46944a263243 | -23.14477 | -49.82138 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f85ff2dd-0448-38d9-9d24-d3e165cd6dc5 | -23.1431 | -49.80853 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cfa4c6e-97f7-3321-9baa-4b1f43b6f25f | -23.14252 | -49.81261 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 059536bd-5061-3151-8948-864b5c1bf9c6 | -23.14193 | -49.81674 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f62ff46a-07a1-370b-8778-051a0f43a781 | -23.13968 | -49.80794 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7c741e0-d1ce-3cb1-ac8a-4c37af23d880 | -23.1391 | -49.81205 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c73eab42-274f-3403-b33a-57b95b475dec | -19.7152 | -50.38123 | 2024-10-08 04:38:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 9ed0b734-be0d-3bf1-aaaf-ade3f98f7c33 | -23.56666 | -51.41838 | 2024-10-08 04:38:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| adb25884-5ca1-3900-b67f-5f1ad709e3dd | -23.31671 | -51.62815 | 2024-10-08 04:38:00 | NOAA-21 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 19e2161c-abb0-3f9b-b1a3-548fda94c145 | -23.21072 | -50.89882 | 2024-10-08 04:38:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3f1d2e39-22cb-3185-b6a9-c29b56a19279 | -23.00808 | -50.41803 | 2024-10-08 04:38:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 660ca00d-960d-319c-a18d-8e0da4f62934 | -22.87491 | -51.20851 | 2024-10-08 04:38:00 | NOAA-21 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2fd229ee-4c2f-3f82-b32b-8cf27e9c895c | -22.82115 | -51.55597 | 2024-10-08 04:38:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f914afc2-60ba-38d7-8078-ad5be34f6530 | -24.87824 | -52.23561 | 2024-10-08 04:38:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| feebd8ba-6421-33fb-9480-96ea2488cb93 | -24.2429 | -50.74046 | 2024-10-08 04:38:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5686a917-6c65-3b29-8f31-ce2073e4ca9d | -26.61204 | -52.4812 | 2024-10-08 04:38:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d367e960-11ff-3ed2-a88a-cf7c4df7716b | -19.40498 | -51.68154 | 2024-10-08 04:38:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfa3123b-8759-3991-97dc-9e960c59fa22 | -19.40166 | -51.68095 | 2024-10-08 04:38:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042d8d4b-207b-3515-ae79-86239839c9a9 | -19.39264 | -51.69446 | 2024-10-08 04:38:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd70289b-398c-3508-a0c2-a2b800084837 | -19.38873 | -51.69753 | 2024-10-08 04:38:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c2010cf-75f4-3f84-b037-1afc414d8d7b | -23.7049 | -53.21801 | 2024-10-08 04:38:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| aca35e7c-f320-3ac3-ad70-3e338619d8ce | -23.70155 | -53.21737 | 2024-10-08 04:38:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| de6687e2-a855-3ec2-b120-6dd19772d7b2 | -23.47378 | -52.07996 | 2024-10-08 04:38:00 | NOAA-21 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1cba92f7-6ece-34ed-ac45-600ad8594a77 | -23.12171 | -52.40919 | 2024-10-08 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f1c6eadc-20c1-3288-87d0-946684e83075 | -23.12111 | -52.41295 | 2024-10-08 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 510ffc36-2aca-3e9a-9308-cc97d0a01534 | -23.1184 | -52.40857 | 2024-10-08 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 031eebca-60ce-3e2c-b603-61b78b6d4f4f | -22.72733 | -53.23326 | 2024-10-08 04:38:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5137ccb2-bd4f-3a16-b713-a2805854f3cb | -22.72462 | -53.22875 | 2024-10-08 04:38:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c78b41af-61f5-3d34-a7e9-a0b4e9bef9c6 | -22.71194 | -53.24229 | 2024-10-08 04:38:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f939e805-07b9-3ace-8e7a-169688176863 | -22.70857 | -53.24164 | 2024-10-08 04:38:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 55a7e78d-e329-3afd-9dc8-a4c8f420235f | -25.47496 | -52.89462 | 2024-10-08 04:38:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5b651105-9d90-3304-8a8c-fc5572ffd6c3 | -22.90346 | -53.69108 | 2024-10-08 04:38:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ea253a32-7a2f-3e70-af75-c3c2efc7f53a | -21.91234 | -54.60688 | 2024-10-08 04:38:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d59956d3-5bd8-3b1b-8592-6128708fd765 | -21.90804 | -54.61049 | 2024-10-08 04:38:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0937116-ef3d-373a-bf0c-99874916cce8 | -21.91534 | -54.58963 | 2024-10-08 04:38:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d696db28-8225-3da3-91b6-89e6638b1c2c | -23.35332 | -53.90398 | 2024-10-08 04:38:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 044fb419-9188-38e4-b6b0-dc96e704db19 | -23.35263 | -53.90798 | 2024-10-08 04:38:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2c9c704f-7945-3130-8e79-b47a93c2d45a | -23.25671 | -54.93425 | 2024-10-08 04:38:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45f63f1c-33f3-3e07-b1a3-852824b0b139 | -23.25317 | -54.93354 | 2024-10-08 04:38:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18ecf99d-a1ff-37b5-9ba3-79edc7611f0e | -22.90006 | -53.69041 | 2024-10-08 04:38:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7c7a50b6-eef4-353a-b6ad-cf12dd3ac5c5 | -25.01986 | -54.08539 | 2024-10-08 04:38:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f65a90ca-7dbe-3f9b-bb88-6d2b766a3370 | -25.01786 | -54.07654 | 2024-10-08 04:38:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 955a978e-0f58-366b-8b61-8969898573de | -25.01649 | -54.08467 | 2024-10-08 04:38:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 946127e6-15ac-3ed1-857b-4491868d6d8e | -25.00837 | -54.07064 | 2024-10-08 04:38:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3fb95dfc-4e08-3792-bfd7-fa9ce17d273f | -25.00769 | -54.07464 | 2024-10-08 04:38:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 09b88e41-38e2-355e-ad78-de3de4a0d36f | -24.25065 | -54.26023 | 2024-10-08 04:38:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 382d8c3a-3dea-3221-8089-39e9c9ac85e9 | -24.24723 | -54.25953 | 2024-10-08 04:38:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 7e08d5b2-7b12-3f8e-98d7-10cd215b4f3e | -24.03528 | -54.09765 | 2024-10-08 04:38:00 | NOAA-21 | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a2f3ee7-cd91-385e-8a1a-c802cb41b3d7 | -23.904 | -54.22655 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b4b0c1a6-6ae7-31bd-bc5e-6ddf11939e89 | -23.9026 | -54.2347 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8662b876-12af-3430-af2f-f480b4bfe4d6 | -23.9019 | -54.23877 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| b0617f08-ae60-3711-b9c2-386ff5641dc2 | -23.89856 | -54.21695 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 41a5239c-9ab6-344e-8623-3201354716c0 | -23.89786 | -54.22101 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84f4eb34-83a2-3ab9-a2fd-251fd5fb47a7 | -23.89032 | -54.22364 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4dadd5e1-c878-33ef-8d9b-e478d58c3e74 | -23.8876 | -54.21886 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a668cfac-67ae-396c-8c40-c55e14aac457 | -23.8869 | -54.22292 | 2024-10-08 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 27ead706-4ca1-380f-8a42-bac2d3de148c | -19.39235 | -54.42287 | 2024-10-08 04:38:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91c7ceba-11b9-306f-9b97-08658b6a926a | -18.92408 | -54.5581 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce199a5a-662c-3778-a1b7-461140ed4dcf | -18.92043 | -54.55728 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aa50bf5-b225-3765-a33e-162d71169af0 | -18.91676 | -54.55653 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3debb20-53b3-3378-8a2d-2f062e05f65e | -18.91223 | -54.56059 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3888bd50-95a9-3190-92d8-499f331812fc | -18.91141 | -54.5652 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc7a82af-3cf0-35ca-a058-5232bda53272 | -18.91061 | -54.5697 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc60becd-5e47-3f0f-a59e-83e3d0c19362 | -18.90767 | -54.56483 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef4f92a-f0d5-34da-9b16-f76a6b22ef6d | -18.90688 | -54.56924 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c25c0af8-e0d8-3254-a6d5-99fc6ce401fd | -18.90478 | -54.55971 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4940fe7a-657a-307a-9023-8ba1c4548e73 | -18.90393 | -54.56442 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3657db3e-aeb0-3755-b245-01558bbb9d64 | -18.90282 | -54.54937 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa7cad4b-7185-303f-9fec-3d9a5f4112e5 | -18.90195 | -54.55425 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9da725-6a4f-30a9-af18-388e2c5dc32c | -18.90189 | -54.46972 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac094de1-32e1-3fe1-8280-70c1583617bd | -18.90152 | -54.5779 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c18e47ef-06d8-3008-b13e-fcd5519204d7 | -18.90109 | -54.47423 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c14f742-5fbf-38c1-914f-ddc172475305 | -18.8991 | -54.54892 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d40a8c4e-9a18-3910-90d6-7c59bc7934bd | -18.89901 | -54.46468 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bffe8c53-5a77-31b3-a377-6cd9d46e8cf0 | -18.8982 | -54.46919 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c82025e-c7ca-3fc4-a7de-1cccd64cb5bc | -18.89782 | -54.57733 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d4c5e96-231c-3cf8-a47f-03124df05114 | -18.89698 | -54.58196 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed9bccb-cfbf-3c28-b94d-0e33f74820bc | -18.89579 | -54.48264 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72aa3544-ac8d-315f-b7be-2da4740afa8e | -18.89531 | -54.46415 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a52fdba-5b92-36ee-92bd-c9f94201c8ee | -18.89499 | -54.48706 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9109b6a1-088c-3d54-8cf3-d9b70960587b | -18.8937 | -54.47314 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7fd57ae-440f-3b0f-b7e1-e4408966ec82 | -18.89289 | -54.47762 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23dee8b3-d3f4-37f0-a1ee-baff6cbf4480 | -18.8921 | -54.48204 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 989e5576-7845-34f3-aaad-f0607ac27562 | -18.89163 | -54.46356 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a892390-af0e-3d33-b192-138556355312 | -18.8785 | -54.57878 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68948785-15dc-310c-af07-40a068512f87 | -18.87564 | -54.57349 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a935f0ae-8b41-33e4-82bd-7a0b5db4958a | -18.87479 | -54.5782 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58c44756-31d6-3512-989f-1808179ee31e | -18.87193 | -54.57293 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffc21a98-44d6-31b2-91a4-99ed4aa6b8ea | -18.869 | -54.57474 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3284291d-be49-374a-8d42-0a3d4f6cdd59 | -18.8653 | -54.57412 | 2024-10-08 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae0d069-b82d-3b0c-ac21-e92b0f4caefd | -20.78796 | -54.83543 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9814e77-b90f-3041-8b70-3077fe5f39ae | -20.78765 | -54.83808 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 65e6db62-6133-30ed-9f26-a37d228d8792 | -20.78714 | -54.84009 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b24efc32-1b17-39ea-a143-aab2d6abe945 | -20.7868 | -54.84271 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README77.md)
