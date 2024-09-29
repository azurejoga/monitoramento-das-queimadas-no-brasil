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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfe01635-580d-3f4f-9a9f-9da8306925f5 | -3.32234 | -50.30813 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 348ea0b9-a71c-340d-bbc9-f0deb4d941c8 | -3.32179 | -50.31172 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d5df072-a1a7-3853-9f35-abf2b28bf070 | -3.31841 | -50.31119 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 224c16ba-eea0-3a3b-8422-72d7b08dd9cd | -3.2719 | -50.15659 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05bb95fe-3b26-39b3-82eb-f9d909b57bd5 | -3.26851 | -50.15607 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088d9e86-1b77-3a2a-99d7-d59051c10846 | -3.26795 | -50.15969 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed7f0a21-e860-3892-bb4b-9a2654ca7503 | -3.24039 | -50.01817 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 305c7128-7ec5-36ad-aba3-ce4deb1d634a | -3.23756 | -50.01401 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dd6d4dc-ec42-3aed-9fe7-67639005f0ac | -3.23699 | -50.01765 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15af25c6-d0b9-3eba-bc5b-401bf0121e8a | -3.23359 | -50.01714 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2897a8ec-a920-37e7-9648-7e681f9607fd | -3.22873 | -50.3234 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34d778c9-d908-311d-9598-69ac0cdbd7d9 | -3.22536 | -50.32288 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cafe489e-1842-3e88-bcf0-48d4064f66d6 | -3.21606 | -50.44946 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfee71a7-1a23-3cc1-bd93-6d9a5134fa6e | -3.19701 | -50.43921 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213ff843-e692-3b83-ac6a-12bb808d31b6 | -3.19646 | -50.44274 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7767d804-291c-390f-bd6b-ad6a36554d83 | -3.1942 | -50.43514 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c28a0da-35bd-36d5-bba1-8b3deb2aded9 | -3.19365 | -50.43868 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1970cf26-32aa-3492-8862-f26fe8c183ce | -3.1931 | -50.44222 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7259ee70-0f1b-3bb1-a8f6-84966ec3788c | -3.19255 | -50.44576 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b79c1bb3-33cf-3fce-b898-71eff199e1a2 | -3.192 | -50.44933 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e3a5718-cf08-3e46-9b97-6b1188d04e96 | -3.18919 | -50.44524 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a4dcad0-37ee-3022-ab53-bb635196d85e | -2.83932 | -49.87479 | 2024-09-29 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d188d81f-8ff0-354b-9621-d7d69e3cda3b | -2.80148 | -50.27667 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95f2ea4a-a384-3f4e-9964-d8c9ea0c71fe | -2.43924 | -50.29799 | 2024-09-29 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e1de2ac-ca25-368c-be76-9d44e279f082 | -4.05902 | -49.95914 | 2024-09-29 04:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5867dc1-296e-3085-8144-e6881849580e | -4.00857 | -50.44211 | 2024-09-29 04:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ae52aa-3123-36bc-a631-1a16de121fb9 | -3.97223 | -50.06777 | 2024-09-29 04:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883d0be4-ca6e-3ea9-bd69-276578cf8607 | -3.68387 | -50.18953 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc6314bf-297f-3f92-813c-2cc4fdd52ba8 | -3.57451 | -50.39469 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 687fe993-4df7-31e8-8dc3-f552af4612e7 | -3.57114 | -50.39417 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c72b267-6655-34c7-8f46-2d6dbd6b79c9 | -3.57111 | -50.37215 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a694a0a-debd-3dcc-875a-30f00ea0e4e4 | -3.56774 | -50.37162 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0bc1c6f2-fcc4-333f-a3e9-86b8714b2a67 | -3.56718 | -50.37523 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82333445-22be-3d54-9fb5-482393c7b153 | -3.56437 | -50.37109 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 38ebd40b-aaa2-3aea-9f99-b84e537bd732 | -3.56381 | -50.37469 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5d2a0a45-aa7a-3ffe-a274-634adaf9bda1 | -3.56325 | -50.3783 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b05c1869-1043-3572-82ec-3ac197a6dcb8 | -3.56099 | -50.37056 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5342fe67-9f3a-3a61-af9f-5acfe5880156 | -3.56043 | -50.37416 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96c675cd-359d-3613-8344-fa7e358c5496 | -3.55987 | -50.37777 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1215e2aa-a78f-39f9-b6e3-a9555fb8097c | -3.55923 | -50.31501 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74a47348-3919-333a-ab16-bc0e5f808ec5 | -3.62332 | -50.62512 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1792f171-ecc6-37e2-8bd6-f92a4b2b4db1 | -3.57691 | -50.55587 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732333f0-6377-3b77-80f4-1dbf7d2e1d7a | -3.57299 | -50.55893 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a4c94b3-f101-3553-92e6-2b96b9af2f04 | -3.57132 | -50.56962 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6480b308-9e78-330a-a3cf-2450c31f47f3 | -3.56965 | -50.5803 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5481167c-d2b5-3ce1-8677-b7fdb38f1eb3 | -3.56909 | -50.58385 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e04ede40-a306-3586-a1f3-ad465adfb547 | -3.5674 | -50.57267 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a886c9f-b943-3ccc-a868-b3d3928b5e43 | -3.56629 | -50.57979 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a0d821f-d886-3a9a-bd68-9e898a54fec7 | -3.56573 | -50.58334 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c54fd28-665b-38ae-b5b9-1848ba7f44fa | -3.56293 | -50.57928 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22810955-a347-3f4d-9ebf-1250994bb6a8 | -3.56238 | -50.58283 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d590a43-31bc-3f8a-bee7-47216552d290 | -3.09516 | -51.29004 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdf69c3a-332f-37e2-bd89-33f1fbb0c053 | -2.2066 | -50.62962 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 321a965f-7d58-34fa-a6b9-0a330bb2cbf3 | -1.62318 | -50.53923 | 2024-09-29 04:46:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2e7a33b-c56f-3793-9612-377f245306e9 | -1.52147 | -50.62328 | 2024-09-29 04:46:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21877f81-2a76-3d76-a54e-8a444ad0e265 | -3.11909 | -51.6358 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d37f8a-e871-3bbb-9753-3093db0dadd0 | -3.09901 | -51.2871 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 811e93e2-128e-30d8-8ee2-99f7ea0031a2 | -3.07329 | -51.34311 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb645351-4a25-3258-ba2d-fa955b16a616 | -3.03726 | -51.20346 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38c868bb-c083-3762-bb87-19e9cd388281 | -3.02491 | -51.13066 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ba78fb-0135-3658-b647-4e499744fef7 | -3.01936 | -51.12271 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aa2a327-35b4-3db0-aff2-48f242f0ca56 | -3.01584 | -51.05835 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8acf14fc-352b-314c-83d9-5702473f3a84 | -3.01529 | -51.06182 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1765ab80-1210-353c-a6c1-6fc154ed6b9c | -3.0136 | -51.0509 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84efd915-027d-3e98-b982-cd89b0c792e5 | -3.01306 | -51.05437 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2add8d7a-f58c-3dfb-be0f-5c39e5f4d77a | -3.01252 | -51.05784 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4420833-a298-3adb-bad5-64f75a425e53 | -3.01028 | -51.05039 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5bc6e6a-b35a-33db-b494-006e6419c8e4 | -3.00974 | -51.05386 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e2f846-bf5a-3c83-ba33-5a5bff39c82c | -2.9604 | -51.64996 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c63248e8-c37f-3f2f-ade2-c0d34d928978 | -2.95763 | -51.64601 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 36133226-ec4f-311a-888c-a7816f987bb3 | -2.95709 | -51.64944 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| deadfa6c-cd66-3933-8360-bf0cf0bdcefa | -2.92668 | -51.77843 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b482416-7acc-33ed-85a3-351b16ba459e | -2.88669 | -51.57857 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44ba18c6-39d1-3c4f-b7e5-a4d0e1e2209c | -2.88615 | -51.582 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7909b95f-74c7-3c4f-91b8-5080e8fe909c | -2.88339 | -51.57806 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c07efde7-7ef6-339a-b245-1e5a7532c0ee | -2.88332 | -51.38433 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bfc0ea2-ba02-336a-b9c6-e9c5e48ce82e | -2.88285 | -51.58149 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 953e31a2-7a90-3b0b-8661-0bbd654554ac | -2.88278 | -51.38777 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32472fbd-bc1b-34d4-941a-ce1443553a9a | -2.88007 | -51.66563 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41113416-53e6-361c-bf99-f3086b4ec16c | -2.88002 | -51.38381 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 620acdf2-fea0-3854-ba38-7410ee1d8125 | -2.87953 | -51.66906 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b298466f-f4ba-3b2c-b3e1-75f5de275222 | -2.87846 | -51.67593 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7062f9b3-2f0f-325e-ac11-9146f786f2c5 | -2.87792 | -51.67937 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae431ea-e743-31e6-9824-0eceb8af3052 | -2.87725 | -51.37986 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9be24111-4737-3019-b573-6fe29ef7c77b | -2.87671 | -51.3833 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 303f0a1b-8e3c-3f25-8b66-0ea85c8dc4e4 | -2.87651 | -51.66496 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f648408-a760-3da9-a947-73c67a7cac74 | -2.87597 | -51.66839 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6048224-28ba-3a88-88af-00596e3aa975 | -2.87489 | -51.67526 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d93ff95-46e5-3fc1-b4a9-0c9c13cedd90 | -2.87435 | -51.6787 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d313f2fb-6503-35b5-8ec1-bf4da779c5fd | -2.87267 | -51.66788 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f75a7d-2adc-37be-8c66-19c5b70f3c04 | -2.87213 | -51.67131 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36492c4f-aff7-3394-9fc4-ed3394b4fe73 | -2.87159 | -51.67475 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7abf048-8b50-3d78-9107-0d2f0e092108 | -2.87105 | -51.67818 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1225d40a-128d-3813-b4d1-1bceb4c645dd | -2.82479 | -51.34703 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14495c62-9f79-32ef-8e0e-e7ea7f15756b | -2.69925 | -51.34472 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd039b4-9e1c-39dd-acf1-6bd1d4ff9d12 | -2.58489 | -51.92186 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b703ab3a-ac4c-3069-8e3a-e889fb963be4 | -2.58104 | -51.92478 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99a9078b-e28c-35d1-be88-740086c54161 | -2.30277 | -50.84085 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21dc325e-49c7-37b0-867c-04cfa1cd8a9b | -3.63817 | -50.79372 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcc4b56a-1582-3bad-bcdd-d1d55440e23b | -3.63762 | -50.79724 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
