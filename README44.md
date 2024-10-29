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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2014852e-9bf9-3078-967a-24a8e01a9d1f | -2.42572 | -49.16508 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c50ab127-6f38-3b04-a630-a29fa618c484 | -2.4224 | -49.16456 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f78232d2-3d82-3855-a371-454ffcfcb445 | -2.42186 | -49.16802 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de9856b0-5c58-3c36-be15-6e7c83ddde7b | -3.49839 | -49.93902 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392aa88e-d0c0-355f-a85a-cbb010414cd6 | -3.49783 | -49.94254 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1468ca65-f60c-3ef0-83c4-752819668708 | -3.44355 | -50.09041 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33110445-3497-3419-89b9-7f6519e2606c | -3.44298 | -49.68575 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54327da4-39dd-3047-86e1-ee69ad44379d | -3.44019 | -50.08989 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b37fe757-9c3d-39f4-b01e-f8c392f8651a | -3.44007 | -50.15574 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f0a5c55-fbb7-31ff-a629-c6f627e1d90e | -3.43542 | -50.25046 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00323d3c-ed06-3d56-adcd-1d5d66c6d98e | -3.43485 | -50.25406 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dfa7de9-f0d3-38da-a658-92a8df617596 | -3.42934 | -50.20167 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df112ffb-9a81-3141-b697-d5068331f650 | -3.40522 | -49.6227 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08c57bc5-f5ec-3451-8a58-7239e4f1e8ed | -3.37308 | -49.56769 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed94b6ca-45c4-3315-a738-d4776257920e | -3.37144 | -49.49189 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 182a5fe0-f2d1-352d-9a1e-7fba3a164ed3 | -3.36875 | -49.53064 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c766e5-42cb-3783-890d-252df771e98b | -3.36821 | -49.53412 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45f009b0-4868-3cfc-8ca0-d45f3a64e6d7 | -3.36434 | -49.53708 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 993916c7-9d96-3007-9e34-5e4ea85732db | -3.36282 | -50.17321 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8263b096-eb13-3fbb-9da8-1eae66eae5ff | -3.36225 | -50.17681 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e998a28-7546-3c0f-a0ce-25a81ecf192e | -3.3617 | -50.15839 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c870dd-e997-3b31-997d-60e6a30dbe9c | -3.35945 | -50.17269 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a03b6c-02c2-3197-b61b-7debd48b3593 | -3.35888 | -50.1763 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3532deda-8d70-369e-bf74-c733ab000355 | -3.35834 | -50.15788 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2286674-ae81-3a2c-aa56-68e90188b55f | -3.35778 | -50.16143 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe1da67b-7d96-3492-aa49-fd5f6dda6130 | -3.35554 | -50.15378 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f1ace68-bc36-3248-9180-e1d2902138f9 | -3.35497 | -50.15735 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9577b1ff-92c4-3f31-8e50-5a9b93f8ef67 | -3.33124 | -49.91676 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06fbc80f-b643-3ee8-b840-e89f3b48f6c9 | -3.33068 | -49.92029 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e85d8fe2-5d7d-36cb-a17a-13bb4a93771c | -3.3279 | -49.91623 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0b57e5b-5f73-3488-9095-3377c58925a0 | -3.32734 | -49.91977 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbb33903-48ed-3229-b10f-70a2bbeb0157 | -3.32114 | -50.24032 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e752de2c-7fe8-3e34-b018-1a48e0283872 | -3.31834 | -50.2362 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d73cecbb-4910-398b-bc80-c364c4b45537 | -3.31496 | -50.23567 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f004be2-0af6-36a4-95a0-a903efcbc499 | -3.30839 | -50.16839 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f8a4f4a-3bcf-30b9-93c4-9e3f6606661f | -3.30746 | -50.08767 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efb68b4a-4e4e-38ad-9348-2c70e2b9cb61 | -3.3041 | -50.08715 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a0acc2-4d2a-3cb5-a266-37dd3b424bec | -3.29402 | -50.08556 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37ffba67-0fba-3611-80f3-399ef06a18c5 | -3.27078 | -50.02298 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a2e1eb-f510-3bc6-ab54-e22b76ba9012 | -3.27022 | -50.02654 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d4631d-fb3c-32ec-9af7-2833582bf41d | -3.26182 | -49.49612 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e587359-3597-3610-ac97-cc2cad3d4f05 | -3.2585 | -49.49561 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c9ebcc9-f300-31ba-9d5f-fa10b8a30e5b | -3.25518 | -49.49509 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e09f1c1b-88c0-3d2c-98ca-25e6499bad66 | -3.21905 | -50.17599 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4833cff7-6db7-3f94-a4a4-b6408f89ab80 | -3.21848 | -50.17958 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8105beb3-c6a9-3735-bfa1-456a7476b55a | -3.21791 | -50.18317 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3148b9e0-754a-35e3-a3fe-9de9a1946a70 | -3.21511 | -50.17906 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09a95aea-11ca-3c73-8cd1-db0df64ea02b | -3.21454 | -50.18265 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60db5a13-1f48-321e-b9f6-b52a68ff2b78 | -3.21345 | -50.16776 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a101d574-fb8d-3009-895f-d5a0318fd94c | -3.20883 | -50.21863 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f4d6132-53e0-3511-9b1e-92cd27f3d9eb | -3.20763 | -50.24797 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44ee7514-5bb9-3b07-910f-2fc72f4499f5 | -3.17444 | -49.53244 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cfab9ef-7388-31c1-a66b-836601d861c3 | -3.17388 | -49.53593 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0eb8c3f5-0a64-3502-a928-62366f25f029 | -3.17167 | -49.52844 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61fbbf34-f248-3cd0-8b77-f0c787c316eb | -3.13726 | -49.72364 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4939e142-0c5a-334f-b465-1f3e08ae0fbb | -3.55617 | -50.30605 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a2150e-c287-3ad5-a98c-f2a6fd0b12ce | -3.5528 | -50.30553 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaa7c035-3b94-32b4-a346-46dee9f3a741 | -3.51008 | -50.29145 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3a52e5b-1070-3194-a752-964a7a728b6d | -3.50951 | -50.29505 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52b11cb7-e656-3c21-b93a-5a29c71f8737 | -3.49405 | -50.37036 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4953e56-4c8e-3b89-949e-ffb482aa137a | -3.46989 | -50.34803 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 546c7ef9-e2fa-3c02-b03a-eebf7ffbb4c2 | -3.46651 | -50.34752 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97fabd2e-0df2-3dc1-9d59-d7ca03076a4c | -3.46486 | -50.33617 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ffd60cf-2416-3c60-982e-959bcc192fd2 | -3.46428 | -50.33979 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d560fb94-c6a0-384c-a075-a5a8162fceef | -3.46341 | -50.33611 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a48e072f-daa2-38cd-bfe9-12930c4b5c1e | -3.43809 | -50.32106 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475e7acf-db70-329d-a0a5-919e9745dcbc | -3.40775 | -50.29414 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d82eb4e8-7993-3d88-9282-cd64e0ac24fb | -3.40437 | -50.29361 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f144bfda-7277-3b18-a4eb-7e75e434ae9d | -3.37884 | -50.34515 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6790906-fe5a-3cbc-8c82-0ece94716e5d | -3.32494 | -50.30372 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b01e5e4-12b1-3f2c-ad60-7c280939abfc | -3.32437 | -50.30734 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e0a027c-97dc-3395-9bb5-db1e8e37b159 | -3.32213 | -50.29959 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b483eba-70cd-3524-8b85-83c9fe451850 | -3.32156 | -50.3032 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 594108ea-4bcf-37b9-841c-f15714df88b9 | -3.32099 | -50.30682 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4e4ddfb-0ebb-31c5-a35a-56dc228e8144 | -3.31875 | -50.29908 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 981d2822-7a3a-3013-a0e5-b5e83f8d4975 | -3.31818 | -50.3027 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da4fb695-f7d7-3bbb-ae71-236dbd8efed8 | -3.31761 | -50.30631 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39867ecd-a431-3d18-b669-8ff333786bda | -3.31594 | -50.29496 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed029e0a-259b-37c4-9fe1-3574d3f5ee65 | -3.31537 | -50.29858 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c0bb373-0f2f-3629-b53f-41864ebb84d8 | -3.3148 | -50.30219 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0590962-3899-3c90-9610-e21b084f6dab | -3.25427 | -50.35572 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed6a419f-f8ee-3c59-897c-707819080a22 | -3.25369 | -50.35934 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435f4847-b8d0-3f50-8984-1cedaa021844 | -3.25089 | -50.35519 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06cdf511-1035-33a1-a9b6-e7ee05363769 | -3.25031 | -50.35881 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e936e75a-9af1-3e9a-97c3-e1a9b688862d | -3.20731 | -50.38142 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2baefa3-d702-34c8-9d54-21c136d47cfd | -3.19337 | -50.31606 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4b39fdf-9bb8-3a07-afd7-f80d7a6bd393 | -3.18524 | -50.38916 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91038c93-4cfb-3c8d-9733-bd0166e2c2ef | -3.18242 | -50.385 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3219073c-ec8d-3a0a-a178-b3e4111a6b37 | -3.18185 | -50.38863 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 068b15e2-395f-3a76-b43b-e329b490aa50 | -3.18127 | -50.39228 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 48f1f40c-153e-3391-8b4f-aa8cedc3d55a | -3.18069 | -50.39592 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93cf38ec-dd89-339f-93de-77420b67755d | -3.17903 | -50.38448 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 93ef93fd-6709-3461-aaca-8fc262d011e0 | -3.17846 | -50.3881 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c86b81b6-5953-3ec0-b8ca-3b8023239852 | -3.17788 | -50.39175 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c546ff9a-1c9a-33cb-83a6-80dada91a161 | -3.1773 | -50.39539 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 319ceffc-4099-3dfa-aacb-86f7ba9681bc | -3.17564 | -50.38395 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1043b54a-d448-3679-9e6e-6a7f8c7793ab | -3.17506 | -50.38758 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5dc65c7-f978-331d-9f19-5e0635cc27a0 | -3.17449 | -50.39122 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d0e10fb-ab63-35ed-bb9a-17e62d0bdc41 | -3.17391 | -50.39487 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30d01548-6e8b-3205-8227-91d801085086 | -3.17167 | -50.38705 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README45.md)
