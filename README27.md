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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1f72148-4426-395d-8af9-d71f59de9961 | -3.54537 | -50.3116 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29e4434b-b7f6-3f12-9bce-b354fffb9d7f | -3.54313 | -51.38198 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b811d1b5-8f3e-3f75-a346-918529e9ea71 | -3.54279 | -53.02705 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17954927-bd62-3346-b677-51dfbf8f7be5 | -3.54261 | -51.38517 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c850023d-936b-30c3-8faa-2cb5effecd89 | -3.54207 | -51.38841 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1dc0aa7d-d2d6-3da1-89f3-e63bcf88d504 | -3.54036 | -51.38556 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e19126a3-6ae2-3aad-a9f1-144da3667813 | -3.5398 | -51.38882 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 374b136a-0fc4-31be-8cd4-82209514527c | -3.47176 | -52.2185 | 2024-10-21 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2e1957-09fd-3135-8036-1db8c829c7db | -3.47113 | -52.22225 | 2024-10-21 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dc4cbb9-ebbe-377c-bfbc-eb2f39fc8ecd | -3.46616 | -52.21737 | 2024-10-21 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ae3c151-b110-3810-8af3-e8f8e4ba32fa | -3.46554 | -52.22107 | 2024-10-21 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 301a091c-2ff1-39bd-b553-d617014fbcd4 | -3.46139 | -47.67222 | 2024-10-21 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e0a078f-415f-336b-a1a8-9e6f4dc7acaa | -3.46055 | -52.21632 | 2024-10-21 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec4c2c1c-de51-3a30-83dc-9b618281aff2 | -3.45164 | -52.86274 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6006c2e-b0ac-3125-83d0-44714041e7a5 | -3.45087 | -52.86724 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c52ff3e-99a7-3fe4-933e-3989eddb3983 | -3.43132 | -49.97649 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e87a85-ad47-3e45-892c-290e327de70a | -3.42648 | -49.97572 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 499a6b13-978c-3497-a260-bb522ab0d3eb | -3.41643 | -54.27711 | 2024-10-21 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecfbbacd-32dd-3bc2-81a8-27757f2fbaa5 | -3.39261 | -49.73381 | 2024-10-21 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d997dff-d2f2-38ae-a1b9-91bfcf4560f0 | -3.3925 | -49.73569 | 2024-10-21 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642c1ece-fdac-333f-b037-0eeffc2466c6 | -3.39182 | -50.80437 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea2d3c0-c980-3e41-8d0f-57dc3aaacef9 | -3.3882 | -50.66855 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2bc8330-8ce6-3822-be73-651b737882b9 | -3.3877 | -50.67157 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 835a0366-6a83-37f3-815a-9b9e56d5e717 | -3.38629 | -50.34445 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07be5a6e-d1ea-36c0-966a-2475aec15a13 | -3.38583 | -50.34675 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01f99c22-996e-31d6-bdb2-fb156fa58ddd | -3.38311 | -50.66776 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39c6d97b-f52e-38fe-9211-d16c142114fc | -3.3826 | -50.67081 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e46e978d-13ab-3b7d-90d9-88ba17d7b397 | -3.36551 | -51.06031 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca17911-30b8-3362-bee8-8d879760b41b | -3.36499 | -51.06346 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f875579f-5fd5-37bf-9300-f7da46e03177 | -3.3556 | -50.10152 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0097f1f-9334-32a9-9246-52db97d55500 | -3.3547 | -50.10688 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81233ff8-f80e-364c-886b-8bb3733f7a43 | -3.30786 | -50.10304 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b1d198-239b-3bcf-9cb9-f7a43bbfd3b3 | -3.30297 | -50.10222 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be65104c-0334-3d58-a66d-8e37ac8d16bd | -3.28311 | -45.75126 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11f4e2ba-c8f3-3ad9-bbc0-abdd71687476 | -3.2808 | -45.75206 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f9b0a45-f6d0-31a2-a01b-b24b21632ca1 | -3.28057 | -51.05738 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6f5c44-c22f-32c1-94f6-ba41853ebf73 | -3.27686 | -50.6628 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 224fd4b9-e6e6-31e3-acbc-cbe85de77638 | -3.27126 | -50.66503 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa401ed9-b0e9-35ed-b1a2-4675d7cc1eec | -3.26223 | -53.78421 | 2024-10-21 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e11fe3e-2f58-3609-bec7-1589deb58aa2 | -3.26143 | -53.78878 | 2024-10-21 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f91d6770-42fd-3c86-88ba-fe3ef41a6716 | -3.2466 | -50.93888 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b33adfcf-0cc2-396a-b72c-35e2366fab98 | -3.24294 | -51.73528 | 2024-10-21 04:12:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 999c7ee8-2bc4-3fa0-89ce-a0ba06396bdc | -3.24036 | -50.84904 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8163877-56d9-3b72-aaa0-8894abdd05fb | -3.23985 | -50.85211 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae6eaf23-af4f-3d7d-b704-b9c0eb478fd1 | -3.2347 | -50.8512 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 104bf2b9-8038-376d-b528-1267ba62001a | -3.23452 | -51.1411 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afaff1b0-4f37-38bd-a31a-6b11eaad8faf | -3.23398 | -51.14436 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d0100af-84d8-30be-8041-79b7e6a87b01 | -3.22929 | -51.14007 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fee10f67-aaca-39b6-b3a3-77acdd6cb76c | -3.22875 | -51.14333 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ca28181-0e9f-34c5-b4d0-b386e3af6006 | -3.22636 | -51.25639 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fe9104a-7ae6-3bf3-a8a4-1fda4f250d2b | -3.22583 | -51.25967 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f13b9ed-1ad8-355b-ab4e-01d1a27581b1 | -3.22161 | -51.25219 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0544e041-39dc-3381-8e6a-6365970f5580 | -3.22108 | -51.2554 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497fa2c9-72dd-34f3-8beb-ea7080ea54a6 | -3.21491 | -51.19411 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3c27cd8-330d-3ae4-bb94-a09ae2ad2491 | -3.21162 | -50.8 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 138ab9f4-f890-3e89-9497-24548b75e4b8 | -3.21112 | -50.80296 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 74f70bb1-1575-3ef4-9d5b-8bf0a96ed26c | -3.21061 | -50.80596 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c10c0a4a-bcfb-3b10-830e-7b84e1fb1e16 | -3.20982 | -50.79893 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 66ec14f3-7ec5-382f-8cf5-016615274991 | -3.20962 | -51.1933 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04b40eff-0074-3348-9149-ba52a397f241 | -3.20933 | -50.8019 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 720a6a84-d069-33ac-8d3d-9d73c7540a98 | -3.20885 | -50.80489 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc2c3a46-f25e-328b-a580-652c49d1bee3 | -3.20835 | -50.80792 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ed62510e-770b-3315-a2fd-77c85c8f0ce9 | -3.2053 | -51.59269 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a61244cf-0036-3a43-b252-d300c647f159 | -3.20516 | -50.79509 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 239f9683-cd26-3dab-b6ac-47beddad5e2c | -3.2047 | -51.59621 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0faf52b-175d-3682-a6a9-f93e51103861 | -3.20468 | -50.79809 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a180798-1e3a-3a08-abf7-cd444245ae85 | -3.20465 | -51.59135 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2f9a408-ff9f-3aae-9120-5def0e25b460 | -3.20419 | -50.80106 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 500fe7a4-247f-371a-b182-8a84575c04b1 | -3.20408 | -51.59487 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c865f56-16d5-3025-980d-b79b9a82a225 | -3.2037 | -50.80404 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dbaf3bf8-acac-3e14-9aaa-f89b8b8afb52 | -3.20351 | -51.59839 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1293e882-febd-367d-949f-6d26a726b64d | -3.20048 | -51.58827 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fba194d-5b41-3c82-8e47-c3b986e40de2 | -3.19988 | -51.59177 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa406245-bc2d-3db8-9e21-abdfacf7c21b | -3.1998 | -51.58694 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211ac4ea-972f-3ee3-a1c0-25c5decdc9b9 | -3.19928 | -51.59528 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aa7d0d7-12a9-3b4a-a9d3-b160518da917 | -3.19867 | -51.59392 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cd85ed5-a76b-3a45-8fcc-ff41639efe0d | -3.15545 | -50.37948 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ecd8791-98a5-3419-ab19-8e10982cd723 | -3.1554 | -51.16101 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b321c75-da86-3b05-9650-0d905fd02853 | -3.15013 | -51.16016 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a6fa68c-4d2f-3d61-93cf-9e4656bc7d8a | -3.1259 | -51.34745 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bdbb559-f6d1-3bfb-904b-61620aa73224 | -3.12535 | -51.35086 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2b708d0-810c-3c63-81f3-80405ad08b77 | -3.12362 | -51.34723 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4b85b56-c267-3bbf-99dd-ff09086f2006 | -3.11273 | -53.12136 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 005d9703-a162-308d-b8ec-be445719e25c | -3.11202 | -53.12559 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a563394-897b-3020-8e4c-d35903ddeec2 | -3.11132 | -53.12979 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ea1fb66-694b-37cc-836a-b39354b34739 | -3.10792 | -54.1761 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2e7d4f4-ebf3-3833-acba-2e2116c6a336 | -3.10745 | -53.11609 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9c5a4c6-f4cd-3926-8549-4ba90020670d | -3.107 | -54.18147 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| defd203c-3b43-3896-82d5-f39435b5a092 | -3.10673 | -53.12038 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5511af0d-6e27-34f9-aa2b-e1313e6e85e8 | -3.10601 | -53.12462 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70b13ced-cb14-3b8d-a148-3eceac606963 | -3.1053 | -53.12887 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f39a2c8-2eca-352f-9b8f-d2e20410c676 | -3.10273 | -54.16274 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb452def-2c7b-3930-9331-22527fc7b100 | -3.10243 | -54.16972 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 11ba4045-ee3f-3a0c-b77f-90e750935b5e | -3.10192 | -54.16764 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5314b734-09bd-3ea0-85b0-a44c84299c17 | -3.10155 | -54.17483 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e2d80261-3d51-3d5f-86c4-ecc6d45a6787 | -3.10109 | -54.17266 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0e3297c4-1beb-3b38-903d-c4af8b09685a | -3.10065 | -54.18004 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 9e470f91-188c-31ec-bde0-2d0881940bfa | -3.10023 | -54.17782 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 69982de0-ee7b-3d78-8023-36314b3ea605 | -3.09972 | -54.18544 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 583da30d-8ae2-396c-95dc-8893fb83a5d6 | -3.09954 | -51.27452 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
