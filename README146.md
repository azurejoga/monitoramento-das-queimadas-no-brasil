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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5ba8c3f-ec0c-3b19-be24-759d6f5b53a5 | -16.64019 | -55.92585 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1d8e8f6f-42ec-3746-b097-f678e68030f5 | -16.63085 | -55.93847 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 84e442c8-6e2d-393f-9592-215534eb05af | -16.62951 | -56.00338 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| adeb7f41-7c9c-3879-88e3-f15f8694733e | -16.62901 | -55.92417 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a3d822a-597e-314b-bacc-024cc4493e5e | -16.62713 | -55.93791 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1e49c9f6-3cd5-359b-a012-96856ee1bd83 | -16.62341 | -55.93734 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 343009c8-60d0-3cf3-9e84-7d28c7bc1f76 | -16.62279 | -55.94192 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9cddc190-a097-3cd8-b131-8c6b4b297aa9 | -16.78343 | -55.7793 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 02c141b9-73b5-324f-9d24-bacda6cb81f0 | -16.77545 | -55.92022 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 210524e1-6907-3549-9fb4-86baa8992277 | -16.77172 | -55.91966 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2a87a770-a7b0-3116-b7d4-3bf8b6e0615d | -16.76085 | -55.77596 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 009689f0-4ea9-340b-9ccc-e90471a12ad5 | -16.7189 | -55.49134 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3f9bfbd7-522f-31a4-8d1c-1e4d8541a0e8 | -16.7188 | -55.97262 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 84244a20-a966-3387-b5d7-d276c327e96f | -16.71761 | -55.97016 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a858a67d-402b-3e00-b0d5-704565b4c774 | -16.71376 | -55.50052 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d6f71e2-a220-372e-8f16-d77a5c0ccee0 | -16.70863 | -55.50963 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6dc9f680-2321-3c68-b4c0-f789626eb3e8 | -16.70455 | -55.99376 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad49d36a-642b-3a94-84b9-3bd5dc9bd7a7 | -16.70416 | -55.51387 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0b123d41-3b7a-3daa-9dae-d5baf6163fda | -16.68489 | -55.93258 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b713bb45-a20b-3cfa-8ebe-e675e7e2e067 | -16.68117 | -55.93202 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 63c1b30f-7baf-3e6c-8307-27485b342133 | -16.67744 | -55.93146 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a2df78a5-d0a9-3863-be76-662810941cb9 | -16.67372 | -55.9309 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| de003312-6377-372c-8b56-13a91b585941 | -16.66872 | -55.9395 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8197bbf3-4441-356e-b5de-eec1a3ed07b2 | -16.66808 | -55.94408 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4b6ce972-cb18-3608-9052-f5483dfa3fae | -16.66372 | -55.94809 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 49adfb60-59f3-3c3f-92f5-149e200d55b8 | -16.65818 | -55.93323 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a6be82ca-b953-3507-9b76-8b5e159a1f8a | -16.65573 | -55.9235 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0bbce4f3-55df-34d3-b867-11d36b9dd150 | -16.652 | -55.92295 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 68c4d079-c3ee-3b18-88d5-867342e58ccf | -16.64082 | -55.92127 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 31bdf5cf-1d46-3241-bd1f-1ba5630b8228 | -16.63521 | -55.93445 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0185f3fe-04db-36f0-bd6b-0c7ac69d8e9d | -16.63395 | -55.94359 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 28926131-14a6-30e3-af1a-d1d3f028b011 | -16.63274 | -55.92473 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 123744b6-3845-3251-8c20-d5ff49865e6e | -16.63148 | -55.9339 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fbce72ef-b8c3-3c9a-a64d-9764f24a2dc1 | -16.62839 | -55.92875 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4269b79e-5282-36e2-a797-14dcc465bfe1 | -16.6258 | -56.00282 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 164af5bd-fdd4-38a6-8c27-169938abf118 | -16.6171 | -56.03851 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8842dcb3-1b40-3c3a-9501-fdc4f8c023dd | -16.61525 | -55.93411 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6794615e-d899-3e07-b7b0-cd997bd4ce92 | -16.61216 | -56.04699 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d8d69eb5-06e0-335f-8680-92ce91b83e51 | -16.6079 | -55.93967 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 285898fe-5a2a-3652-8329-c10dd20dd729 | -16.60478 | -55.99038 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| b14abc6a-1f6a-3861-a5c4-5281ab932711 | -16.60106 | -56.04531 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4c4dc342-8bce-396e-b980-d9cea14eed3d | -16.60101 | -56.034 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4f7e0d0d-2670-3bb4-a3c8-b285faf1586c | -16.60005 | -55.98762 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 259a9f16-4974-339d-831e-c6db9336e23a | -16.5994 | -55.99216 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7b344f65-5f3f-3163-b7c5-abe5cc05e6ea | -16.59876 | -55.99669 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 10d14f9d-9a40-3dbc-ba59-575c92fb5fb9 | -11.8277 | -56.84286 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e918aa6e-9b65-3c20-a414-989cd0c1bf0c | -11.82713 | -56.84658 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8668889-9b52-3a83-a8c4-45c35999892f | -11.82428 | -56.84233 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4b21385-dd09-368b-913c-7390e92a23f5 | -11.82372 | -56.84606 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f157edc-3c9a-3d4f-b6b4-624304d71099 | -11.77493 | -56.3154 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 499223c6-131f-321e-a434-11eb67198721 | -11.77204 | -56.31097 | 2024-10-02 05:12:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efafb00d-c71b-3abe-9380-72d6dd073674 | -11.49197 | -56.78076 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d43ad9-3fcf-3baa-99b2-6194eb23d99c | -11.49027 | -56.79192 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d738406-2598-3cf4-923a-5d5c35487d86 | -11.48971 | -56.79564 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f1f30fb-1987-3d3f-a4b4-8f677115e960 | -11.48686 | -56.79139 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37ca250d-26a4-35e8-acf3-ca36da351362 | -11.48629 | -56.7951 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5168d96-e963-3c44-b337-d48ef48ee251 | -11.48458 | -56.78342 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba2d9ff-376a-3c08-9a68-db5c8a9dd8f9 | -11.48401 | -56.78714 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38e72d61-8dd2-3190-9ace-10f856aa9465 | -11.48345 | -56.79085 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3595f778-ca9a-3459-92a1-75dcc53135a3 | -11.48288 | -56.79457 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2afdd9b-d165-34e0-a809-0b631142ca63 | -11.48116 | -56.78289 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63b2d66a-e411-3740-858c-5179e87aaf6c | -11.45883 | -56.28479 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f36f5139-9cdb-342b-83ba-fff8d19bec25 | -11.42184 | -56.29483 | 2024-10-02 05:12:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 289744e4-3240-32b5-ae32-16cb932298d2 | -13.28788 | -56.15612 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b36a5151-9233-335a-80e0-9376d03e9fe8 | -13.28552 | -56.14746 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d851c575-3791-340f-bbad-6bdeca34e923 | -13.28493 | -56.15153 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ab7db79-81d5-3ee5-8718-bfdb15a52a85 | -13.28433 | -56.15559 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af0d8824-5c7b-3417-8046-b8a5898596b4 | -13.28374 | -56.15964 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7befccdb-6d3b-3df9-b7bc-57d2bb529271 | -13.28315 | -56.16369 | 2024-10-02 05:12:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea385650-2db3-3b1e-88a2-bd5dc9cfdaa9 | -13.10747 | -56.42863 | 2024-10-02 05:12:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ebe12e5-5872-3183-9b26-b3a3e96e5e23 | -13.76885 | -56.47902 | 2024-10-02 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceed5e7b-ad4a-357d-9794-b79c77ee4f3e | -14.31126 | -56.84918 | 2024-10-02 05:12:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1cc10da7-3d13-3e76-a04d-a8ed4c2ed1fb | -14.30778 | -56.84863 | 2024-10-02 05:12:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37f2b8c8-3b91-3dbf-975f-bc18de4cc14f | -14.3072 | -56.85254 | 2024-10-02 05:12:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f19b1b16-b899-3500-bef4-e22546177cab | -16.61443 | -57.32699 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e7abef52-a55b-3630-b140-495281bd8873 | -16.59407 | -57.34413 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f715782e-5486-370c-a8e4-64ac5374d7fe | -16.4911 | -57.3088 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| db5cbd3e-0013-3c11-9c7b-f11d91356a9f | -16.49109 | -57.33315 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| db64f1d1-be97-36c1-917b-4557f8c5ca98 | -16.48993 | -57.31675 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cac3a0ff-036f-3653-ac69-b9d4e7e56f5e | -16.48935 | -57.32072 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 01e2a09e-ede5-3dfc-b783-1581c1bb591e | -16.48878 | -57.30031 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ffc2d6d7-d06e-3d58-afaa-351961df9327 | -16.4882 | -57.30428 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 83d5eb19-5234-3ea1-8546-558cafd139b4 | -16.48761 | -57.30825 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 105f7661-2f82-3b41-98fc-9990567e060a | -16.48703 | -57.31223 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8a404ca1-49ca-3329-8301-0ffed8d4390d | -16.48645 | -57.3162 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e8f6b5bf-0d60-3f06-aaa5-8c4638fc2173 | -16.48587 | -57.29579 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 1620fb39-0e2e-32b5-b78c-e3717f22659c | -16.48529 | -57.29976 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 948f9ff2-eb67-3736-b7ff-e7d9ec8a3fb8 | -16.48471 | -57.30374 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3ab8a5b7-d45d-3dca-a10c-386eef263feb | -16.48413 | -57.3077 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 881274da-cac6-3b99-952c-b89e6a913d4b | -16.48354 | -57.31168 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1ee971db-620f-3f01-802a-32edcf66b1ff | -16.48296 | -57.31565 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b15dc24d-63dd-3b1e-98c3-82ec9ab44c87 | -16.4818 | -57.29921 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 43c3f0b9-5cb9-393c-af43-72a603161955 | -16.48122 | -57.30319 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 37c4f114-9984-3be8-bc7e-f913e6c522dd | -16.48064 | -57.30716 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| aa451e90-3519-3970-8700-c00b56049b6c | -16.48006 | -57.31114 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e91d65bd-2aa3-30cb-a569-43e12496ac84 | -16.47889 | -57.31908 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 54b3d140-5cf5-360b-8d1e-a7957e613600 | -16.47832 | -57.29867 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a20a3d66-d719-3959-8572-09b62f6db99e | -16.47773 | -57.30264 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a83c4da6-1795-3f01-a0f0-768e5e20f79f | -16.47715 | -57.30662 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b62e04a3-000a-315e-9de5-558db46b7e61 | -16.47714 | -57.3553 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README147.md)
