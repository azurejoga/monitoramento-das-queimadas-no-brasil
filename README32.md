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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55267b8d-e8a6-322a-9f81-a6c997ae573e | -1.03646 | -47.56689 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 69f17652-ac81-3e8c-a676-6b8115064b1e | -1.03643 | -47.56391 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 080a5036-3c55-328b-8ab4-41ad6534342c | -1.03583 | -47.56777 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b1b740c-37a9-350a-8e1b-a55736676868 | -0.94275 | -47.55692 | 2024-11-02 04:10:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f507f190-646c-30e2-a48c-c2082d7fc91c | -0.94213 | -47.56079 | 2024-11-02 04:10:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 640cabad-7e28-3720-854f-c3069c02c744 | -0.93793 | -47.56008 | 2024-11-02 04:10:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db4b17c1-5663-3a2f-8f19-774542afa9f3 | -2.11512 | -48.28694 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b8571d57-9697-39c3-839f-87c34b722854 | -2.11444 | -48.29107 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| edf2c287-e9ac-3615-ae50-df53d97ffb43 | -2.11353 | -48.28759 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| bffd7a3f-93e4-30d6-a75a-d14e269f00d2 | -2.71773 | -47.99564 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81fefdd7-8798-34e9-a0fe-01cb31ebb45d | -2.71288 | -47.99889 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a5327c7-ea69-3f47-8e4d-b779e8d6dbbc | -2.67466 | -48.13095 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 940a5ca9-768a-39ae-85ea-f4adf5833701 | -2.67403 | -48.13493 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a409287f-dd14-3ab8-8220-0e35c8c19e76 | -2.6739 | -48.12971 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23f7b1dd-cb83-375e-aa76-30768db8d69b | -2.67325 | -48.13367 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53e922f3-a2ea-39a3-86fe-e550db63e382 | -2.66833 | -48.137 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c55f2f8-436b-3c88-ba06-c6711405a749 | -2.62666 | -47.96978 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 892b45b8-d303-36d9-8b36-51c2a52303f2 | -2.62048 | -48.33395 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f3662a15-7820-3348-88e4-42d3091bde7b | -2.61617 | -48.33323 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 32a2f9b6-bc6a-32ab-aac6-4367bd5572a0 | -2.61551 | -48.33735 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 086af914-ad18-354b-9ec9-efbd94ad73d3 | -2.61448 | -48.31608 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fbb177d-49bc-343d-8c90-131e822670c1 | -2.61382 | -48.32018 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5877e0c7-3874-36b3-bcf1-a201e8fc74b8 | -2.61185 | -48.33253 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 934d1259-2c5d-3ac7-bbe8-94895b5cd219 | -2.59453 | -48.22086 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48530f0a-ac15-39eb-9486-84da2cfd9c4c | -2.59387 | -48.22495 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f51cfcc-0178-37f5-9c81-0081a2ef44c5 | -2.59157 | -48.21206 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0af489f4-cf0e-34be-b8fb-5b7fc035d215 | -2.57326 | -47.97739 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714a9079-602a-3ab8-b37d-10ac45af8ebf | -2.55459 | -48.17788 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d8a1bd6-8065-31eb-9bed-1cbf8bd2f9d9 | -2.55339 | -48.17704 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c3406d8-54ad-391e-bccf-2ecba1e7f60b | -2.55032 | -48.17711 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 136298a7-bccf-38e8-9cae-f6ad3fc8d60c | -2.54669 | -48.17232 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81b49790-f248-3c39-acc9-b41c704899f9 | -2.53925 | -47.37852 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee35094-90c3-357c-9ac9-86f269eb2c2b | -2.5352 | -47.37784 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b3f67eb-2eac-36df-a153-ecc0e7ba46dd | -2.53419 | -47.51518 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525aa1ff-4c00-3bf3-94dc-945fbfbc6fab | -2.52607 | -48.47666 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ca2b47-716c-3405-8aeb-45f142c4fe9e | -2.52367 | -47.44982 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5b2edd-d325-33be-a428-0b221c5c9a4d | -2.51785 | -47.46006 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 484f6655-aef2-3998-98b2-dd5a2dd82a48 | -2.51726 | -47.46371 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab8896e-3d19-3789-b83d-ec50738d5eb8 | -2.51378 | -47.45935 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 691e4c22-a19b-3f5f-ae25-14032f380cf6 | -2.46366 | -48.49772 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0abcbb5f-c335-3805-8125-1294fb355c00 | -2.46298 | -48.50196 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f938cf-831f-3850-a96b-db25bae17a44 | -2.4623 | -48.5062 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 280400c9-3edd-3bae-a4e8-dc5ed7c42f99 | -2.45928 | -48.49701 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4947e651-ef1b-3383-9b60-f888e3d710e8 | -2.45148 | -48.51754 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 587944a1-2f4d-3d4c-81e7-826d97ff2411 | -2.43001 | -47.8201 | 2024-11-02 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac89bf1-a2dd-3c30-9541-a5fdce1d7d24 | -2.41362 | -48.52882 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cd33396-1d1d-35bd-bfc9-552123f62bcf | -2.40376 | -48.58886 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6663285-1212-35ac-9da8-9bf2e06ef362 | -2.40149 | -48.57518 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8db6dce3-ad6d-31d2-867d-a2790ae84082 | -2.40078 | -48.57948 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f634e7ae-bf7b-3a9b-a764-6622bbf739c6 | -2.40007 | -48.58382 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91e4adb9-aa3a-3920-adf4-e2eccb0b5e9f | -2.39946 | -48.22442 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9b74d70-4379-3ffc-9768-33811fb52b4a | -2.39936 | -48.58814 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 199b5117-6b51-3ea0-9771-938b755123f6 | -2.39864 | -48.59252 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81ce3b0f-b54e-3e4a-aa19-1fd07f1d4d48 | -2.45562 | -48.84843 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdc78b6d-8ac9-3206-915d-ac954cb45523 | -2.45308 | -48.84958 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01c66ab0-c19a-3a3d-84a1-58be219e415e | -2.45114 | -48.84768 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 078b2eb6-d293-3809-b4c4-f801fdfba965 | -2.4486 | -48.8488 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 889f012d-52ac-38e3-b309-2e22470569e3 | -2.44666 | -48.84694 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdae715c-4c63-38f5-b9f1-20ccbd77dec1 | -2.41144 | -48.87953 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b0249a7-c020-315c-a8af-c9bb618dbd98 | -2.64686 | -48.56416 | 2024-11-02 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d1c3e84-8670-3f1b-b52e-75a562862f13 | -2.36491 | -47.63155 | 2024-11-02 04:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5842d0ce-5d00-32af-b073-ebad1046629a | -2.36431 | -47.63526 | 2024-11-02 04:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa41022a-33d2-35c1-9cd0-8f804fbe8a9e | -2.36077 | -47.63091 | 2024-11-02 04:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0904de6b-bcff-359e-9698-d0bfdb3e5f18 | -2.36017 | -47.63462 | 2024-11-02 04:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88984dcb-6270-3296-88d9-8ca97fd6e885 | -2.35957 | -47.63834 | 2024-11-02 04:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87afe6ec-384e-3045-b1ac-11ec0ac23c21 | -2.35926 | -48.69321 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb9ec653-d9d0-36d2-a9fc-c59616a99aeb | -2.35892 | -48.56125 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e88e018a-7dfd-34c9-93c8-ea4b88e39ebe | -2.35656 | -48.69016 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b6f46ef-61ca-346e-ac20-a4e2f21a2262 | -2.35379 | -48.42517 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0698901a-75fa-358b-b169-a1ab347e5d98 | -2.34942 | -48.42449 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0db2a331-dae2-3348-a846-b6edcd24f613 | -2.34294 | -48.5763 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c4ca8f-7f6d-3a27-938c-d6f112e0027b | -2.33572 | -48.50909 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa368bb-1267-3168-9b84-e35838415f48 | -2.33086 | -48.6232 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09cf8141-7fc2-33fa-9e0d-04dc86f28f43 | -2.32993 | -48.60087 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5952bb10-4ad2-3507-8885-48bc710d6d32 | -2.32922 | -48.60525 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95eab549-6665-3aef-8ec5-00f50167811f | -2.31098 | -48.52264 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 762f5834-4739-3d97-b74b-85db2bba0cd6 | -2.29797 | -48.54689 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00a9ff4b-3923-3802-8259-29c4672f815d | -2.29062 | -48.81585 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7ce6c53-4f97-3233-8864-2b46853303c3 | -2.29009 | -48.45806 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e42c36a4-039f-3124-a6f9-0c070c8ad419 | -2.28943 | -48.45904 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f38ff791-2b97-3393-9f3d-a989a44ee668 | -2.2831 | -48.80545 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f35b477-08e9-3573-bb8f-8cbf73a2e864 | -2.23981 | -48.84457 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eb5f0d2-4535-3af1-a90c-a4fc603b5081 | -2.23759 | -48.8458 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23743611-2f25-38bb-9e1d-435f6a5b4c09 | -2.23531 | -48.84385 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da054c80-7d90-3343-b66d-7b1625ae96c1 | -2.22246 | -48.2384 | 2024-11-02 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54e63623-736c-36ef-834c-97a922edbd0f | -2.19898 | -48.35356 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c208118-1276-30b8-b934-03c97005167d | -2.1976 | -48.36188 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76ef6b55-8aa2-33a9-8196-b72e937cccc4 | -2.19632 | -48.36432 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78d717a3-421c-3b67-b1d3-981d3d6a06c2 | -2.1734 | -48.72949 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de953cff-1fbf-3a48-badc-738e6855e6f2 | -2.17267 | -48.73397 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1efd8a38-672b-375b-92e4-84dffb3432bc | -2.16893 | -48.72879 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f84bc6b-467e-386f-8cd2-356b4117ad8a | -2.16674 | -48.74216 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84febfa0-a750-3733-9cf2-659df77eb1ea | -2.16634 | -48.82935 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc3b59cd-6cb0-3841-953e-5720abf05575 | -2.163 | -48.737 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb920a91-35c6-3d74-9021-eb40d0fb9894 | -2.16227 | -48.74143 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d50f7bdc-0bc3-30a0-a95c-4d6e229f9e7d | -2.1525 | -48.27596 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| effe49c8-8929-37e5-8b6e-5c571a286226 | 0.09209 | -49.86486 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83ebc341-4cb6-3ddc-b07f-00451fa562bd | 0.09194 | -49.86456 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f8f910e-c4ae-3477-8259-116b1f60ee92 | 0.08708 | -49.86565 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 408e2aeb-c137-3301-9790-33e539caebfb | 0.08693 | -49.86536 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README33.md)
