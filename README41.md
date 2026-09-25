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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f48778-1193-3093-9da9-650333dd1c38 | -9.3717 | -66.5077 | 2026-09-25 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dfc8f561-612d-3636-88ec-5eaa96278c51 | -12.8056 | -54.0462 | 2026-09-25 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c84db149-b385-3988-ade7-f3e3831eeefa | -10.9895 | -58.963 | 2026-09-25 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| c63fcc51-baa2-35d9-9bec-fa7ad1cd46d6 | -13.3632 | -51.3163 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d9862fdb-551b-367c-8cf5-cb675caf5d4a | -13.4479 | -48.6352 | 2026-09-25 14:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e6a36d71-c3c6-3b4d-b872-68eb833f5c89 | -13.2249 | -51.5679 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4e2f24c2-3cf4-39ab-b231-1b0ada80210e | -7.6696 | -67.1451 | 2026-09-25 14:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| f2e08480-ac33-33f8-af3e-4e3d63f8fb98 | -10.9895 | -58.963 | 2026-09-25 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 1e9f66cc-f2f5-3a9f-9111-ff20e3d2a523 | -13.2057 | -51.5703 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7472777b-579c-36a1-8a12-c1627ccb800f | -6.8985 | -41.6976 | 2026-09-25 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 2d1a9b20-126b-3d2f-a023-711a63a43fcd | -13.2054 | -51.5916 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 69592182-6002-31f9-867b-5ebc25d2cd94 | -13.8151 | -51.8553 | 2026-09-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a27d0d58-9a25-3a98-b471-96c70b1684a4 | -13.2253 | -51.5466 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b08408cb-a846-34e1-90c7-489f0a5eb661 | -13.8343 | -51.8529 | 2026-09-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| cb85bc24-7ca7-3add-b143-109a3b4f7c5c | -13.3824 | -51.3138 | 2026-09-25 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 178.5 |
| d09a2344-2655-354b-a565-b363015c6c2f | -9.3717 | -66.5077 | 2026-09-25 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 32bdd7c8-d81b-32e2-bafa-e5d6512aa3ca | -12.7699 | -51.3043 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8da06c6f-b2c3-375b-9c67-b32925c3ee90 | -6.8796 | -41.6995 | 2026-09-25 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 74faf9b7-1d0f-3c6e-aed5-5bc0f3525574 | -13.2061 | -51.549 | 2026-09-25 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 475d1ce1-119f-3b7c-a551-3997c66278d1 | -6.2765 | -47.585 | 2026-09-25 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c7db3e4a-333b-3cd7-8bba-5b8b2f4b2e95 | -18.8915 | -47.5482 | 2026-09-25 14:10:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c558dd88-8b73-3a97-af8b-8a2213023f3e | -10.9895 | -58.963 | 2026-09-25 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 8d874699-fc7a-311a-9e81-ffed88ab44eb | -13.8343 | -51.8529 | 2026-09-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 43d4a72d-ed9c-301e-84ea-45a701864679 | -13.2253 | -51.5466 | 2026-09-25 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8fc9b106-51be-305d-b1f3-27ed5231807a | -13.8151 | -51.8553 | 2026-09-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8b20e106-1c5f-3e81-8ff2-8d87b691a9cb | -9.3717 | -66.5077 | 2026-09-25 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 756b11a2-876f-333e-a79b-0b8b67561fa7 | -13.2249 | -51.5679 | 2026-09-25 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 19d8e42b-0725-3335-94a0-84047ff989d8 | -14.4593 | -53.6509 | 2026-09-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b303d679-5265-3482-97de-98dcec7197b0 | -6.2767 | -47.5631 | 2026-09-25 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| ca6fc930-27db-3c5d-8b97-6f8e6fd739b3 | -13.2057 | -51.5703 | 2026-09-25 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| c32977e6-6065-326f-9b12-8613b308a482 | -13.4479 | -48.6352 | 2026-09-25 14:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 2bdfd2a8-f0f7-3a56-a577-0fe40e767282 | -7.6696 | -67.1451 | 2026-09-25 14:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| fbe0b761-4ce0-301f-945f-c4b3bb8c66e9 | -13.8154 | -51.834 | 2026-09-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| eb8a3156-d7fe-34a5-900f-998de9a2e84e | -13.3824 | -51.3138 | 2026-09-25 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 6a7fc929-3dcb-3a5c-8781-9f81fd8f92b3 | -13.2061 | -51.549 | 2026-09-25 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 23032ece-20d4-38a9-af41-739cd4d28b0a | -14.4789 | -53.6276 | 2026-09-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| f128ad88-52d0-3136-99dc-6ff7f9684b98 | -14.4786 | -53.6485 | 2026-09-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 74b9bfe5-429a-32fb-a0b7-a682da7c4473 | -12.8056 | -54.0462 | 2026-09-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 25970ff8-12d1-313a-bb9b-ecfc5abd4756 | -9.36 | -43.3 | 2026-09-25 14:15:00 | MSG-03 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77c058d6-2544-3d8c-bf81-89c66e65bbf7 | -9.33 | -43.3 | 2026-09-25 14:15:00 | MSG-03 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9fbb8f87-3105-3240-8502-a18a671e69db | -9.36 | -43.26 | 2026-09-25 14:15:00 | MSG-03 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c60fc3a-566d-3cb6-9782-69cbcb9f6af2 | -9.3717 | -66.5077 | 2026-09-25 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| bd8dacfa-f6b5-3bfb-aa3d-420fa2fc63ce | -18.9117 | -47.5439 | 2026-09-25 14:20:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1bc94ef0-7bdd-32b2-a051-17313ea0eb28 | -13.2253 | -51.5466 | 2026-09-25 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a4300379-e08a-3345-91ec-2cf906ff479c | -12.8056 | -54.0462 | 2026-09-25 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 699362b9-8884-38dc-8496-64a39a47317e | -13.2057 | -51.5703 | 2026-09-25 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 14713d2c-e70a-322a-8c9c-5a85e9e1563c | -12.7699 | -51.3043 | 2026-09-25 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bab69d51-3200-3caa-8984-5a08b5c32acb | -13.2249 | -51.5679 | 2026-09-25 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 0bda8825-ccc4-3e00-a37b-8e684f9527c5 | -13.3824 | -51.3138 | 2026-09-25 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| be3b691b-99ee-3109-a379-a072c336f477 | -14.3689 | -52.1239 | 2026-09-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d0d6bd03-ff9d-3b73-a751-78f1e0c5e542 | -10.9895 | -58.963 | 2026-09-25 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 189.6 |
| c7ccd64d-0e1d-322d-ad92-8b5ec0292964 | -14.3693 | -52.1026 | 2026-09-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 41ba1db3-9427-3866-92b9-4df5f7850551 | -11.2378 | -55.0569 | 2026-09-25 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e5740afa-2630-351e-b5a0-db72361f67d9 | -6.8985 | -41.6976 | 2026-09-25 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 1f25734e-44ba-3f2b-adab-7f3e284143ab | -10.8567 | -57.1767 | 2026-09-25 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e8300550-ba62-3f90-a981-cd9a01ae362c | 3.9316 | -60.8254 | 2026-09-25 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 620d4c95-426f-3af8-a528-1c7d1af3c0f7 | -13.2061 | -51.549 | 2026-09-25 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 469a11d5-7061-3b8d-9c36-547dcca4ac76 | -13.8154 | -51.834 | 2026-09-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 909bd1c0-5047-32c9-9466-4a60f58ef7f1 | 4.0237 | -60.6146 | 2026-09-25 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2f9147bc-82e6-311a-b927-7460201f14bb | -11.6975 | -54.5467 | 2026-09-25 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fe698f15-b2f2-39de-9dfd-75163f379bcc | -11.2378 | -55.0569 | 2026-09-25 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| ea1e0954-ef2f-3d07-9881-a8540dc6ab52 | 3.9131 | -60.9016 | 2026-09-25 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| c948641e-14a8-3314-afd2-08bbac849078 | -12.8056 | -54.0462 | 2026-09-25 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 98535edc-8e27-393f-9711-3608d384ec60 | -10.8567 | -57.1767 | 2026-09-25 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 3a5ef0b0-69c6-3ca1-9314-f5349ee0946a | -12.8059 | -54.0255 | 2026-09-25 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| afbb3c29-ddc2-350b-942d-965e9a10c810 | -6.3134 | -47.6261 | 2026-09-25 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 09885626-f293-3622-9df1-52487a32d5c9 | -13.3439 | -51.3187 | 2026-09-25 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9bde5653-d4ed-38f4-81f2-679b3afcdd75 | -13.3247 | -51.3211 | 2026-09-25 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e9eb009a-6135-3eca-ad44-33c7e1e9bee4 | -12.7865 | -54.0482 | 2026-09-25 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 55762b2c-11fd-34a7-8e2e-67ff83896b21 | -9.3717 | -66.5077 | 2026-09-25 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 38f72e07-793b-3978-873a-4afcf804d291 | -6.2765 | -47.585 | 2026-09-25 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9540ff67-ef93-3b01-99db-15d017d8a3bc | -13.8154 | -51.834 | 2026-09-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c0d083e9-ba4e-30d6-8407-f9bfec50cbd8 | -14.3689 | -52.1239 | 2026-09-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 50f2f6f4-41fb-31e7-b5d0-9174f05bb71c | -13.3824 | -51.3138 | 2026-09-25 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 8c27820a-7a12-3d86-a5ab-42070ff060b5 | -13.203 | -51.7406 | 2026-09-25 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d294209e-5fa2-3b7a-90f5-9c4c279fab44 | -13.3247 | -51.3211 | 2026-09-25 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| bb724bb2-c296-3202-bc9e-f497e2e263b6 | -11.7321 | -54.809 | 2026-09-25 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f395d344-5585-32e7-8dfc-8c4222385f6a | -12.7865 | -54.0482 | 2026-09-25 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ad108b4f-d9e7-3cf9-a9ba-a6bd45548f28 | 1.5832 | -56.0221 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| b4947704-1e58-3d36-a76d-0e14859d618c | -13.3439 | -51.3187 | 2026-09-25 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1014c935-b274-3cd9-9e33-1b6dc6f8e6e8 | -12.8056 | -54.0462 | 2026-09-25 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 4b1970ba-1255-39df-88c1-7794ff577bf2 | 1.6383 | -55.9427 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 68429b9d-7aa8-370f-a260-7eb7a11107e6 | -12.8053 | -54.0669 | 2026-09-25 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 35050b4d-40bc-3e7e-8213-5abe95ccbb8b | 1.6199 | -55.9429 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5f3ad281-89db-32a4-b689-30bc6f2eb4ea | -14.3693 | -52.1026 | 2026-09-25 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| cd75cede-a654-36bf-abab-06f7b751fd6f | -13.8154 | -51.834 | 2026-09-25 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 33845527-8227-34d8-8dbe-ed9d4971f27b | -10.8567 | -57.1767 | 2026-09-25 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b709c054-4c55-3877-beba-582728910482 | 1.6199 | -55.9626 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ef4e004b-6afb-32e2-8de9-f468473a6c92 | -11.1183 | -54.0062 | 2026-09-25 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e8c4f39f-945a-32d7-9477-45e938727c61 | 4.0777 | -60.9171 | 2026-09-25 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9383d109-5d15-3cb9-b6f4-12338e47b1b2 | -14.3689 | -52.1239 | 2026-09-25 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b115b988-bd18-3a74-bdb5-9b8afd844b76 | -18.9117 | -47.5439 | 2026-09-25 14:40:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ed3dc882-45d9-3347-995d-ce72df1f0ef9 | 1.565 | -55.9238 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 2a12ba83-a74c-31a7-9470-b2086ebe8c50 | -10.8569 | -57.1568 | 2026-09-25 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 4c69ccab-3273-3376-920b-fbfa0755c5ee | 1.6199 | -56.002 | 2026-09-25 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7b33c293-846d-3031-ab42-a51dbe44b475 | -13.3824 | -51.3138 | 2026-09-25 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 63d4fd0b-dd39-3666-a6dc-05bc2344832a | -13.3632 | -51.3163 | 2026-09-25 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| add5efe6-b4ab-3b95-ad71-8f606f2e8c1d | -7.1392 | -42.0811 | 2026-09-25 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 695d522a-cffa-381f-9d1c-588588c5e82d | 1.6383 | -55.9427 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| be40defa-55b9-3e5a-817c-df0f27efc81b | -13.3247 | -51.3211 | 2026-09-25 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |


[Clique aqui para ver as próximas entradas](README42.md)
