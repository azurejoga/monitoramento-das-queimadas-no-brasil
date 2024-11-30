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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 136f76e6-5e4c-3206-866b-057749567671 | -3.43542 | -59.28627 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93ff62cb-755d-3fe3-b217-94b49c166b9e | -2.92195 | -54.26265 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a96dbcf-5619-34c2-a6d5-f5966db9c01f | 0.97977 | -50.26018 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abe0f91d-f1f0-3606-a864-bd388b59db5b | -1.36162 | -54.66047 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4712e77-6f67-3997-879f-ba8c3be299f4 | 1.21514 | -55.92992 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d88de8ad-7873-3b14-8166-45cbd56d4a26 | -3.63994 | -54.44723 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7fc90cf3-00a5-392e-9479-ad3a56bc8037 | 1.90718 | -55.70726 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a2ec8f5-90ab-3a50-9fc3-0bff67cf7a85 | -1.54832 | -52.27964 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a242b85a-afaa-3914-837e-9d2bfe4cef22 | -1.5309 | -52.66203 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6135979-523d-3b86-9062-058e60bb1a33 | 1.19885 | -55.95236 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1e6560c-e815-3d71-9530-7631986c6f92 | -2.3469 | -53.81419 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d441ad8-6f20-31a9-b19b-0d635dc3d1e0 | -3.29575 | -50.37962 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 169ab9fe-0e64-3cae-8913-cdd4ade4f07b | 0.89036 | -51.98781 | 2024-11-30 05:27:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5461a859-f8d7-3bf2-b042-f1821dcf8301 | -3.58534 | -50.36355 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 499e0b14-603c-3292-98ca-7f7987ad5fab | -3.25028 | -53.85802 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96a8175b-2797-3901-92a2-f2209e6ca954 | -1.25289 | -54.54745 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adf9f228-7897-363d-875f-d629bcc532b0 | -2.59452 | -53.98364 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93ff4405-f989-3820-8dfc-e1e3cba51539 | -3.79879 | -58.97696 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858cd81d-0f89-35c9-befb-9232cafcf0dc | -2.14177 | -54.88432 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1182321f-036b-38fb-af4f-ea438bada24a | -1.60144 | -52.2891 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74cebfc5-dee7-3906-8d9d-564491fdec02 | -1.66759 | -52.40956 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4496cd8d-a1ea-3891-a6bb-06609ee8b010 | -1.25166 | -52.18235 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3882897f-b741-302e-bdab-e7408fe44cbc | -2.60757 | -54.207 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7e237ef-575e-3913-be35-8b5ff2393c22 | -3.31928 | -54.18038 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b32fb3e1-5ff7-36e0-9402-65ecfc8e5fb0 | -3.28441 | -50.62548 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5613cba-cce2-3ca2-9508-e7e58fb84ade | 0.9409 | -50.74338 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d842bc92-0ea1-3af1-b4f3-4701256ad214 | -3.29399 | -53.82903 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53d4f6df-3381-3665-903a-9a7d3a88744a | -3.41388 | -50.16756 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed2e70da-7db2-3a0a-8926-ce661c57049e | 1.18567 | -55.96914 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63592b65-d599-3501-863b-bef984e72e41 | -1.57928 | -53.84167 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8cdb7e0-508b-33e1-acaa-0aaf37112ab6 | -1.9914 | -53.28989 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9efd1e4-02b6-32f2-bd58-125d0189f4b4 | -2.82546 | -52.96938 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 138f99c2-7653-3939-b5ec-4170efb94529 | -3.30202 | -54.16819 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d44b5732-1123-30b5-ba6f-a880d9081fdb | -1.9715 | -52.89478 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3206bd11-a17e-376d-8c37-04ee0cb2beea | -1.37622 | -53.64849 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c30d481b-350b-3f9d-aacb-0f696723be2e | -3.05583 | -53.1738 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7925980e-fdb5-32ac-9ff1-196ce65184e2 | -1.70245 | -52.64293 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dad59951-4dde-30ba-bf3e-098871d1376c | -0.883 | -51.7192 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2080c05a-9e9d-3c7f-8ce3-b6dde39d247d | -2.19316 | -50.58348 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22f5ec3-a5a1-3202-8db2-67b42ada61ef | -1.74712 | -52.6557 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4595988a-ebb3-3fe7-b5cf-ba1dc328841d | -2.89131 | -55.22943 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd71835-976a-3e4c-8031-eaf1c4e4a5cc | -2.79824 | -53.04889 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8a9d0e4-47ac-3614-a243-98ad02f2c296 | -1.63679 | -53.87008 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1144a1df-2c89-3e59-8196-3e08ae63dd77 | -3.41935 | -50.43289 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25fc3de7-40a7-34e8-ac64-6700b5d34d09 | -1.59914 | -52.2937 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9481c1a6-f675-3962-b779-3d8b24300037 | -1.63229 | -54.35923 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a950a360-f36c-304d-a846-a31f47b4def3 | -3.24507 | -51.34661 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ad92ba7-72e8-381b-8adf-88725e04770e | -2.61809 | -51.81622 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28bc2ec3-1841-343c-9e0f-c6152a2cbd5d | -3.63526 | -54.44436 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b9c2c8c-5d2c-3ebb-af53-48205db835ef | -3.38096 | -50.69579 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9bdb404-aa46-36d0-a0c5-b39856e68730 | -3.24872 | -50.59777 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c422ae7-dd0d-34f1-8b30-e8014c69284b | 1.20505 | -55.9414 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3f2bf99-1e26-31b9-9801-603ac77b7a3f | -2.95159 | -51.69988 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f2d601-fb9c-36b2-8cde-6c37b04542ef | -2.31567 | -51.96061 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e78d814-a1dc-38ab-9d5e-6c27f20e6bcc | -3.86057 | -50.15667 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14425750-0a63-37bd-a80a-40d5a31c0c46 | 1.90408 | -55.71276 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2514a40-b6f2-384e-81e7-37761ca2090b | -1.0976 | -53.39423 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d3469e28-b6d5-3518-9f90-77a07409b6d0 | -2.61666 | -54.20625 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6af396ba-8e87-32e9-83a7-b9abeda85432 | -1.08941 | -53.64283 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef5d64cd-a900-308a-ac57-61ab6cc4590b | -2.86091 | -53.9967 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13cd0234-519e-3438-942d-344aef80013c | -1.5148 | -52.63273 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b8fb496-a07d-31b0-a168-a274b2d64e9c | -4.20171 | -50.68737 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67ac75b9-bbf7-38a4-8152-1d9843812cf3 | -1.04124 | -51.742 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63986210-82a5-3df3-bc99-e509eb8c0cf2 | -4.07847 | -50.03868 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ec4e437-5e82-3ae1-b9d4-e43c7fe790ca | -1.35228 | -54.63328 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c03c971-7b33-36b3-a074-5847fb47605e | -2.37864 | -47.88153 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c80cc1d-1c5b-3deb-b59f-f30b0cb8fd91 | -3.91286 | -53.81171 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6ea5904-f280-3199-8ad6-e064d2c17e51 | -3.50413 | -53.83008 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f65166a-01c8-3b1c-841f-795c36ac6090 | -1.08278 | -53.63951 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c788aca1-e941-3d67-b315-a4b5d435faf9 | -3.25329 | -53.63989 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 35565d3e-9c98-354e-93cb-cd19bae925c0 | 1.50742 | -55.97133 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0111d8b5-4fb7-3846-861e-0eff9ae8b03e | -1.25118 | -52.18547 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c617d4-5673-3284-a31a-f7de803f5164 | -3.25408 | -53.63452 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 74237063-26b6-3cce-8ead-29b4c0481bd8 | -2.60722 | -51.81466 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| becca664-fb5a-3e96-a21d-1a574fec4779 | 1.21589 | -55.93475 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aa227ee-5103-3d70-8144-c143db6f4491 | -1.6573 | -52.40801 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77c5db9a-3fe0-3217-b904-27c0dcfa8d2e | -1.31985 | -54.63856 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95e8c977-3162-33a8-853c-9754fb411d3f | -2.3005 | -51.98915 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8159aa79-19d0-3b5f-aeb6-6367345ac834 | -1.20647 | -51.74468 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a34eec8a-f47a-3a50-ac86-767c7430ac1e | -4.00266 | -54.62108 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b002cf77-2db8-3f19-8511-dc1724657206 | -1.05727 | -55.2398 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a56dfc5c-34e8-3a84-956e-0ddb7c5a8982 | 1.44403 | -55.88033 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ce1ff61-5679-3621-aa69-d3c3624daf34 | -1.07507 | -53.62776 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 86449cb5-9482-35fb-8b38-125b3288c53b | -1.7029 | -52.63998 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d829fbd9-c023-37f7-9720-145f0fe05ff8 | -3.25488 | -53.62912 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 01603343-8da5-3183-9c97-5561a5f47e0a | -1.38088 | -53.64947 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5198ad3d-0a7f-3ed1-bc88-1ff38bf3f160 | -2.62993 | -51.77518 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fc6ecbb-8a0d-35d4-8c8c-31a3d64d7635 | -2.98778 | -49.59029 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a54db2e0-5f3a-33b7-baa2-557e24c95787 | -0.26946 | -51.62541 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c677cd1-8ca0-3edd-afe3-e41936173d03 | -3.31672 | -51.62921 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2b8736f-1dbe-35f5-9ec9-fecf2a53aa7f | -3.05576 | -54.0534 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ea9f9e2-0311-3951-8b7f-7cd42cee19fa | -3.06483 | -50.33248 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b6318002-5747-39a0-8490-9a67532d700e | -3.03152 | -51.54143 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 545a51b0-3482-3fe1-85ee-e0f9309d856f | -2.19378 | -50.57928 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d81e7d4e-20e2-360d-ada2-c7645ab6240a | -3.50142 | -55.40616 | 2024-11-30 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ff6b3e9-fa01-3d46-9475-7a4b4f63303a | -3.09846 | -53.72788 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2705749a-8ce1-3416-90b7-9937eef0d476 | -4.06606 | -54.48125 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49478006-cdbc-3dcf-87c8-f0a9c263e694 | -0.57985 | -51.70045 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 813242e7-a335-3883-8db8-04a2ec901b10 | -2.62823 | -51.74976 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c997d15c-6002-3fd0-a5ad-360157705fd4 | -4.44253 | -48.5739 | 2024-11-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README124.md)
