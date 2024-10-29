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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| decdcdc1-2eae-3261-bebf-098c39de9bd5 | -1.43182 | -60.39391 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6986a79c-75fc-32cb-be2d-dbf42372a3b9 | -1.43128 | -60.39736 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c1c3ce4-4254-34c7-8196-2738f2fdbcb7 | -1.42816 | -60.28703 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b9a26f4-6198-35ea-81a5-ebdbb27451c5 | -1.4243 | -60.28999 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 173bec70-93bd-3cc3-a0ff-d71a88b90f5d | -1.42215 | -60.28251 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3064149-55fb-36b2-bac6-58c6c9d96cd6 | -1.4216 | -60.28598 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb7f3b0d-a677-3dae-9bf3-69f66ace8c88 | -1.30142 | -60.22856 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582fd808-87ba-3f0b-a953-62cef34ade01 | -1.29865 | -60.22458 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b655eb6-e7a2-3325-b369-4aa5ae369797 | -1.2981 | -60.22805 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 154d03b8-c1f0-3f03-a561-445cecab1169 | -2.61272 | -59.87958 | 2024-10-29 05:25:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40f397b4-fc30-3f55-a2e9-c90a7822fc0b | 4.10346 | -61.12895 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8df1a10-42a3-3d87-a44b-ee42c3955890 | 4.10011 | -61.12947 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd59cb82-bf91-302a-aead-3c1aaf031569 | 4.0973 | -61.13353 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ead643-fe94-3aa7-b221-d7859ce1eb3a | 4.09675 | -61.12997 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17660bd3-ffc3-38f6-879e-9194b648cfdd | 4.09395 | -61.13404 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f561fea8-bc89-3a07-babf-60ae19d98e14 | 4.0934 | -61.13048 | 2024-10-29 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26668b31-876e-3ecd-9fcb-02deced2e723 | 4.06521 | -61.23717 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c57f8e1-6091-3b23-a311-97704407d03a | 4.06514 | -61.2591 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4413081-4fa7-3252-b9e2-7829e5fff90c | 4.06457 | -61.25533 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c394d944-1e42-3d22-b394-f6e5351d8c7c | 4.06178 | -61.25959 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79457f54-7df2-3e08-b11e-9ebdae3d3844 | 4.06065 | -61.25219 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17252707-74b5-3a70-9a8d-cb683ed74385 | 4.0601 | -61.24864 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae6db8ae-ef5e-3de8-8162-03ce0a77a129 | 4.05956 | -61.24512 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc727cd-f9d9-3dec-9cc8-d77b9f7cd12f | 4.05902 | -61.24168 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e82b1a-4ce8-38f5-ab32-b2d7fd0d1493 | 4.05843 | -61.26024 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26f868ae-9cc9-3cf3-8f72-9e1248b6b795 | 4.05786 | -61.25653 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f71f115-b59a-3767-b1d8-e4503ed85ccf | 4.05731 | -61.25292 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22a72ed1-0578-3efe-9a25-e7536a0a291a | 4.05676 | -61.24938 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bf150e9-ffe9-3994-81b6-46112c262ce7 | 4.05622 | -61.24586 | 2024-10-29 05:25:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c435a4e5-8e19-3e45-9597-53e4a410b25f | 3.91195 | -59.96907 | 2024-10-29 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d980b141-1ef9-31a0-983d-f060c19a93c8 | 3.24923 | -61.20614 | 2024-10-29 05:25:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009b3bf9-bb36-33c0-b247-3cfe3510ddc1 | 3.24423 | -61.19604 | 2024-10-29 05:25:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e0fce69-46f3-3dce-ba33-d21566c43745 | 3.24089 | -61.19656 | 2024-10-29 05:25:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40b3cdda-bf7b-3291-8475-5265e2f1bb86 | 2.22478 | -61.67305 | 2024-10-29 05:25:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 015f3137-34d3-341c-9e00-c423cfc1f00c | 2.22422 | -61.66947 | 2024-10-29 05:25:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e833e76-a5ec-3bff-8629-e5816cc36a1c | -0.15437 | -60.86972 | 2024-10-29 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e607737c-3e4e-3a8e-8631-7878abea5e98 | -0.15053 | -60.87263 | 2024-10-29 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a04b9c1-ea1b-308b-b182-757ecd53be8b | 0.1141 | -62.59297 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b9f42a6-c7d6-3138-9d89-aa1514afda75 | 0.11069 | -62.5935 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d1d32d1-f96f-36c0-9c4a-4d7c843a1175 | -0.76818 | -62.89046 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01c03af-2b99-3295-a98d-5a57a662d857 | -0.76475 | -62.88992 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 390db5b7-a9d0-3c33-bc9e-72a7e2c8a776 | -0.76417 | -62.89363 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5f4118-18f1-340e-86ae-6efd567d37aa | -0.76358 | -62.89735 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6f2041-f2f9-39e6-b9b5-1320fa58bef7 | -0.7619 | -62.88567 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afccd806-6647-331e-8b1c-88b7eb5b5b03 | -0.76132 | -62.88939 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba677bfa-b66e-3c8d-a0c1-a6e67801304d | -0.76074 | -62.8931 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01e48d29-c75c-3062-a324-19e734cb5871 | -0.76016 | -62.89682 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b638d8-131b-3dc3-b712-31988bf5640f | -0.75789 | -62.88884 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9205cbbf-fb44-3365-bb46-e445eb590b84 | -0.75731 | -62.89257 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7713d3e6-8fca-3fc1-8dca-5e59ca48ca92 | -0.6944 | -63.20302 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13efaa0e-bb61-3cef-9a08-eee949251e98 | -0.7716 | -62.89099 | 2024-10-29 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a17a080-22a3-30dc-9410-4a9add67f692 | -1.70917 | -54.52901 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e5befe9-a98e-3a91-8d10-02142a1dfa32 | -1.65566 | -53.40206 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5ff88b5-b640-3074-ad24-e09abed9bb89 | -1.56343 | -54.44646 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d43d8037-4cf4-3b6d-8b47-229680e07b11 | -1.56275 | -54.45101 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9e66a5a-1fd2-302f-915a-45fc52f160ff | -1.56082 | -54.44765 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d32536a3-fa27-3089-ab28-cb3f8821b834 | -1.48578 | -54.27455 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a62f9e04-72d9-3adb-80f0-929ab26e66fa | -1.4851 | -54.27912 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57443487-c2f8-3e63-8386-fff3f5c5b7a4 | -1.43618 | -54.22835 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 894bb5a1-704b-328d-9408-61cf1e57b23f | -1.43549 | -54.23284 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e44e7a6f-e2f3-36ee-8e60-dc45fe678912 | -1.43235 | -54.22295 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a80cd1d-c8f5-3c7a-a3ae-b87caf797bc7 | -1.43162 | -54.22773 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 444c5579-c592-3767-96d0-ad9092fe7508 | -1.42778 | -54.22242 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a488fab1-41f2-3045-b1da-04dae6aa3f37 | -1.42704 | -54.22724 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08770191-0eb6-390a-9199-9121891f358e | -1.42388 | -54.54508 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83816f76-cbe1-34ef-aa14-4d78c0bcdbb8 | -1.42318 | -54.22205 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d4274652-ecb2-3baf-8e7b-de344da3000d | -1.41941 | -54.54457 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e2809b-c4c3-33df-9ab0-78cba0447cc5 | -1.39001 | -54.0403 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d96f61c-61aa-3c5d-aaa7-475fedadb9c4 | -1.38927 | -54.04507 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 633861f1-c104-3cdf-a178-b736634dd062 | -1.38467 | -54.04436 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c38291c3-2d21-38a0-8bdb-ce69488a6d9c | -1.34573 | -54.61046 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7511270d-8787-3b2b-b6ea-9e1f18b64789 | -1.34506 | -54.61485 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09559dc3-c69c-392a-a378-500d1d16bbaa | -1.33918 | -54.65359 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 69a80791-e0d2-3a1d-b7e5-6048ea956520 | -1.29122 | -54.67233 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64fe0832-43bc-3b39-bd27-eeca3e893ef1 | -1.28682 | -54.67168 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1f11780-ab7d-326b-b83b-e8bc818a3ba3 | -1.2565 | -54.69309 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27e65609-704b-3d70-bfbc-5eb5455d0347 | -1.24082 | -54.53672 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e1893b-be8d-395b-9381-3dab8df1ac37 | -2.25921 | -53.55255 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45b38abd-2d01-34a9-a1f5-597e5a08c91d | -2.24302 | -53.72668 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be1f2aa5-2a66-3663-ab78-3641484a49b2 | -2.2169 | -53.67319 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 051e4108-920e-3a1f-a73d-aa5a4a552b4f | -2.2165 | -53.67496 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b62a41a2-2195-3508-a0d1-189b48c054fe | -2.21611 | -53.67832 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbd509c4-3d0f-3359-8270-20574c9c3993 | -2.21574 | -53.6801 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a1536ac-b5aa-3950-9d5f-cc535c6b72bf | -2.21212 | -53.67248 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccdab963-ca43-3b86-9ed7-3b7cb085c5f4 | -3.58909 | -54.66196 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92f7f79a-5046-3f34-b38b-883577b43b27 | -3.58836 | -54.6643 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bee45861-f1ac-3718-83f7-8d72c5cc8f5e | -3.58452 | -54.66135 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fa4f1fe-adba-307b-beee-c6a8a1591d14 | -3.58378 | -54.66371 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cadda76-25cb-3f29-84de-ddc173998a8c | -3.56868 | -54.67095 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f30c0939-58f4-3e5a-ac7b-32a40eaa48f9 | -3.56796 | -54.67566 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79f2516d-dd5e-34ed-b7c3-0b9abc240caf | -3.56725 | -54.68036 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d103fbc-fb7c-3aa8-99f3-de82cfb55c09 | -3.54838 | -54.74334 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83acc6ad-b636-3021-af4e-8e143a4bd5c0 | -3.54559 | -54.76171 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9dd32f4-a180-3f55-af7a-534a3fb48901 | -3.54384 | -54.74271 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af72843c-fd66-31d1-946e-6132c6ff66f0 | -3.54035 | -54.76577 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68958518-2766-317e-9191-3e953217acb5 | -3.47085 | -54.82928 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b99f6df6-e537-3514-989d-8539159bab84 | -3.47028 | -54.57702 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30666bf8-2a16-3844-8fbb-ed7f93d0a9ae | -3.4657 | -54.83301 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 472d0359-9bd4-38fb-b743-836ff3471964 | -3.46385 | -54.61931 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3716c85-8a34-3cfc-860b-582a21f81ef0 | -3.46313 | -54.62403 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README97.md)
