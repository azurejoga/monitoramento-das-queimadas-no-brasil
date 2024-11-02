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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e527a252-0269-380d-ae1c-1a8f33642d39 | -2.71326 | -49.27993 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4d72b23-91d4-3dc1-ac0f-c17e896094e6 | -2.71273 | -49.28753 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b766be1-f357-36e5-afc2-7d58b14d070d | -2.71248 | -49.28466 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a4f131-6993-3cef-810c-50c7026030de | -2.71197 | -49.29231 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82b02469-2c6a-381b-b95d-d6434896a2bf | -2.71169 | -49.28939 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11bf44be-8015-3a56-a03c-e9687fde18df | -2.7109 | -49.29416 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b1a417-389e-39b6-bb31-e19c49aced70 | -2.70887 | -49.28207 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f58a6b-431c-31cc-af47-6b0a5c2b29de | -2.70812 | -49.2868 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8ac41fb-3da0-35c2-b7e2-57b1029e8a59 | -2.70736 | -49.29157 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67edc2cf-3592-3474-a539-f2b509ff8a54 | -2.70708 | -49.28867 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35333ceb-bf45-3b03-9782-23e005a69fb2 | -2.70629 | -49.29343 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71633326-19b8-3ece-9331-6ca7fee27ae3 | -2.70275 | -49.29083 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d3b644-c814-3f92-b056-cacd9b12458a | -2.70167 | -49.29272 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469b6b0e-d458-3bd8-bb6a-b1d518cb6a67 | -2.66389 | -49.84256 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c341d08-7767-3821-8954-340f18a6058b | -2.66056 | -49.2594 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f1424ff-d9a6-3bef-90f4-9389b9095b27 | -2.65911 | -49.84175 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9845f160-6b27-32ba-a877-5442d374f160 | -2.65826 | -49.84694 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 166d8e0e-bb27-3e08-ac37-d30913c298b0 | -2.6575 | -49.24917 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edfa3d3e-1dbd-3cce-8600-4b568013c7a3 | -2.65673 | -49.25389 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4eca12-3681-3ffc-806d-ad08c726ea71 | -3.54796 | -50.31502 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d42f469-1e14-368c-b956-2db945aca50f | -3.47609 | -50.36978 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f9c428a-39bb-323d-b5c3-0712986e4a69 | -3.47208 | -50.36349 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3205eb71-6a01-3f21-97a2-30860e48632e | -3.47029 | -50.37441 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34c4bdd3-31d4-3a44-bd71-4795c26b80f3 | -3.46939 | -50.37996 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7c9f30b-13e3-3ac5-af4c-1b64909087cb | -3.46629 | -50.36812 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78bef2d3-c633-3de9-bd1e-9f056488000c | -3.46539 | -50.37358 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6785fce3-b162-34d1-8a26-651336df22d1 | -3.46139 | -50.36732 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47553f07-fec8-38b3-894b-5f0568c15cd0 | -3.4605 | -50.37273 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c1ef9e3-ed5a-3294-9ce0-fa81529c6546 | -3.44392 | -50.38157 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b968e51-5de5-3947-920a-77e48e9ea4e1 | -3.44343 | -50.4151 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad4a5b6-88bd-30fc-aa5e-935dd6e50b99 | -3.41619 | -50.29121 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea5eb8af-dafb-30ea-8653-4d95436d8642 | -3.41362 | -50.29202 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8caa66a1-9801-3e47-b988-3bc1025f4a9d | -3.41219 | -50.28493 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc3315c4-80b5-3269-b009-cd6cf2d70b71 | -3.41131 | -50.29034 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 676ab463-6667-3abb-8712-a0d4209b424b | -3.40967 | -50.28571 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c7104e1-e2d6-38ce-8e18-219ba3ada48b | -3.39465 | -50.34485 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c5af43d-69d2-39c8-b281-6d48ea5d44e2 | -3.27553 | -50.3383 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a07c0c-a4f4-32ac-9490-3a27ee88400a | -3.27241 | -50.33993 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ed6d914-8aa4-313b-bec1-e6703568136a | -3.27148 | -50.34541 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 729cbed7-64f0-3559-9602-1529e7562506 | -3.26974 | -50.34295 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b8b665a6-5551-3886-90d7-53e3fe0ef538 | -3.26884 | -50.34847 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c0f447c1-9add-304d-85c6-cb96cb926e42 | -3.26393 | -50.34764 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a6e3626f-6790-3372-a176-946191f03ffa | -3.25992 | -50.34132 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ddf586d-248c-3242-82a9-fa25855bb320 | -3.25902 | -50.34682 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e6a5121-1443-323d-a789-2be7702d2a08 | -3.25411 | -50.346 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fe75cbf-08c2-3297-ba11-a6443775af09 | -3.2492 | -50.34521 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce90b5cc-1f34-380d-a99b-72f2ba6bce15 | -3.2483 | -50.35068 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf13476-38b1-394d-9e80-8e55325be431 | -3.18342 | -50.58985 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7f1c7cc-bb7c-39a8-bdde-49021a0dcb4e | -3.17986 | -50.58039 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc5d3bd9-6243-306a-87c2-b4f88454e9de | -3.1789 | -50.58614 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65e6f802-aeef-3a4d-8f2f-07c9ca43cff9 | -3.17842 | -50.58902 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d6e485-6a72-3887-bcff-be1869a1f297 | -3.17795 | -50.5919 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb4fa36-d2b0-3128-8e0d-328d4c6f715a | -3.17439 | -50.58242 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d6afe0c-b799-39bf-99c2-b9059e2ef0e7 | -3.17391 | -50.5853 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bafe05b-4582-346d-8f4a-2c82f7f0fed7 | -3.17343 | -50.58818 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b27222-747e-380c-98b5-e5817107080e | -3.17295 | -50.59106 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40fa0058-77a7-3828-8626-5044e5a84db6 | -3.16891 | -50.58446 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c7b1088-7ca3-3190-bcc1-4560efe49820 | -3.16843 | -50.58733 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85a3bdc-16aa-3adf-bcb1-664e0eba39ef | -3.1449 | -50.3548 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39500a6b-f8a5-352f-b964-37b559c4eaa9 | -3.13997 | -50.35401 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a6a01a52-d42c-347b-9be4-b4aafb0ef266 | -3.12317 | -50.42566 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96d03e7b-9c68-37c8-bf8a-6a1fcadfe4fb | -3.50163 | -49.94361 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13f60125-f084-3279-b718-42a1e19d0a18 | -3.46418 | -50.28934 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36ff5925-3874-3d4a-b24e-c7d0802381d6 | -3.45931 | -50.28853 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 393c8c72-bb7d-363e-a5d9-18be44ec9bbe | -3.45859 | -50.17269 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcbbb652-89c8-3bfd-a409-76a611a68391 | -3.45842 | -50.29392 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4300595c-774b-3dbe-be8c-ad77fa9f2f3a | -3.45665 | -50.30463 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98cecc8a-9850-3622-a4fe-bbc6bfc2d1e2 | -3.45555 | -50.16111 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9b89e74-b148-3896-a241-15bdfc6cd741 | -3.45464 | -50.16655 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44f7e200-7b1d-35a9-8c81-6cadb5fd0590 | -3.45373 | -50.17198 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c9ac930-96f9-37f7-9dc5-08d6450fda94 | -3.45158 | -50.15516 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5222690a-baf8-302c-9787-7e51b18cf4db | -3.4498 | -50.16579 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaf63d28-21d9-3953-8839-8cc0d7d999f4 | -3.44627 | -50.1869 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4c684ac-33a1-323a-a8ca-81b87308e7af | -3.43348 | -50.32326 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d3e700-aa53-36a3-bcda-2a0467e0f85f | -3.4258 | -50.24945 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8601f2e9-2f07-3692-8664-5c35848c016e | -3.41942 | -50.28736 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 994052a1-3035-3b4c-b511-dda8c8ee2199 | -3.41706 | -50.28575 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b73f5471-158d-30ad-926d-e9a14d448394 | -3.41455 | -50.28655 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e09b6be-07f4-37ec-b787-c493fdac8d55 | -3.40875 | -50.29117 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b56b3cc-02d5-3588-80bd-b38eceee55d1 | -3.39764 | -50.34412 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba6f37e-adbf-32c3-bf75-a0daa777459f | -3.39274 | -50.34328 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6083adf-ec1e-34c1-9827-677011a84d01 | -3.38975 | -50.34402 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d69c94b-35ee-39d3-8503-9f3a9be28457 | -3.3652 | -50.26588 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ad25ee1c-5917-34db-a1eb-39119f7467d3 | -3.36262 | -50.16062 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69f079a8-5502-3a3f-9997-2b76c035eb7b | -3.36175 | -50.16583 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26c070d6-4817-35b3-81c6-da8339c6d168 | -3.35532 | -49.23436 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 142b9915-0b0e-37df-beca-c0aee5e4044c | -3.34263 | -50.25101 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5a192c82-dde3-3b36-a47e-f94dd5c0145a | -3.33687 | -50.25554 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d04e3e4-e57a-3af8-9c11-9236cbcb8913 | -3.28996 | -50.23678 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1a8c45e2-2d0a-3563-abef-187af912e300 | -3.27764 | -50.23266 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f317c0ce-6c26-331d-abe3-0aa6091973e1 | -3.27334 | -50.33448 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b99141db-dc37-3fc3-9643-071762dc465b | -3.27063 | -50.33746 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f651a342-be0d-3a24-bb2a-254d169ee28d | -3.26572 | -50.33667 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8c88c52a-b197-3ff3-8cab-534085761811 | -3.26483 | -50.34214 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cdf2db71-596d-3f6b-b306-f1601d9cff42 | -3.26081 | -50.33586 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c91d207-15fc-3f67-a079-8893fd9f4f8c | -3.25591 | -50.335 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2921e7f7-73e8-358c-bbf8-8b0cad536b9a | -3.25501 | -50.3405 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5c938b9-a1af-36cf-a11a-9e6e540b31c7 | -3.25349 | -50.04748 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27247bd8-a502-3a59-91ad-d9e852916ab8 | -3.2526 | -50.05281 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d54bb93-8878-362a-bd28-f42b4dc97bff | -3.25101 | -50.33417 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
