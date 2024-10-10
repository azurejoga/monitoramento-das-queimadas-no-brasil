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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 540bc920-71ee-3b87-a718-231dcf443142 | -6.75722 | -59.32864 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b423e9e-093e-38b8-8d70-3415ff8e7d5b | -6.75503 | -59.32159 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49d24ae5-8d15-31ec-ad2c-446f10dd962b | -6.75448 | -59.32575 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3324c19d-43ae-3aed-b3c6-56eb1fee06b7 | -6.75392 | -59.32994 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 228e9a6d-e522-304a-bec3-637bbd9395c7 | -6.75335 | -59.33423 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| defe775b-3adc-3bf6-b649-68cd9446ab8f | -6.75187 | -59.3237 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 467a8872-46c1-3b6b-880f-a0f6f186720b | -6.75128 | -59.32789 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a63df9fd-5932-366e-af8c-66b4850f45c5 | -6.75068 | -59.33216 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcd731e3-ac2c-3199-a013-0ed2ca34efa1 | -6.74854 | -59.32498 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de0d39cb-bb2c-3e1d-a4c5-7e5a18aad498 | -6.74797 | -59.32924 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 924e339f-cf4a-3b5f-81c0-ffabd6307de9 | -6.74594 | -59.32288 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf2f529-55d1-3bca-8ace-bc4a13ec468c | -6.74066 | -59.29317 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a538094-8b14-3cbb-a603-8263f488df5e | -6.73825 | -59.29128 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 787a9cf8-16c8-3f91-ab0e-4c43d85bb2e1 | -6.73766 | -59.29552 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23b8e0f3-5b7a-3789-beb8-017a414b8396 | -6.7347 | -59.29247 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bcd0174-8cbd-31f2-beea-d16b958be1c9 | -6.73076 | -59.32237 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bbcaa08-4f92-3092-924a-3228f96b9c2d | -6.72873 | -59.3162 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efd5a48a-2ef0-3de0-a574-368940b5df0d | -6.72814 | -59.32041 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1457710e-2b30-39e0-8655-1170a17917dc | -6.7265 | -59.30883 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89e87fde-5b1b-38b9-9fc2-4a323b79e7ca | -6.72593 | -59.31314 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adf6e7b5-38e3-37f8-8167-8afb9b28bfa0 | -6.72537 | -59.31739 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67079764-16b1-3be5-94d3-3a450665830b | -6.72457 | -59.30256 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f22b528f-4807-3fc4-9a67-459379268ba9 | -6.72398 | -59.30685 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c091a245-91d2-3120-a6ea-e8d992e2d8a1 | -6.72338 | -59.31113 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c588199c-862d-3515-9dc4-b877f5f9334d | -6.71863 | -59.30172 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 880880a6-55ce-395e-a507-86555ff11d9d | -7.1896 | -59.77433 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04c59a6e-6537-3fe0-9624-7e2c7971bda3 | -7.18902 | -59.77849 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cc36d03-e12c-3b68-8fd2-e42d0b7d7e2f | -7.15463 | -59.39104 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc960a91-4aff-3b59-a9d9-f51877ee49af | -7.15403 | -59.39535 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb380392-872a-3f06-846c-907de44ba866 | -7.09708 | -59.41412 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f553f4c-4dc2-3548-8f42-0fcb834d07a3 | -7.09173 | -59.40899 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d0f6bdc-32c5-3c7e-8a8c-7fc28ed07b90 | -7.09116 | -59.41325 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bed97b38-f1d4-3f5a-bea2-3ef7ee32c627 | -7.08581 | -59.40815 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bf33028f-a8b1-3769-838e-eec32d29a5fd | -7.08524 | -59.41242 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a33c9a00-7e8d-3021-808f-e471cde9d0e8 | -7.07988 | -59.40734 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0a99b534-8ca0-3ee0-a1fa-df9fec274be7 | -7.07931 | -59.41162 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7aa5da7f-ce8f-3e5d-a1b6-562e9d899e15 | -7.07874 | -59.41586 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 21c816e4-c139-357b-a8f3-b1f33abfd434 | -7.07396 | -59.40648 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 19305042-e526-3b74-909b-edc1e3fdce2b | -7.07339 | -59.41073 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e12bd7f3-064f-32b2-af56-a229783a5f17 | -7.07282 | -59.41498 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dfc5dc9a-b60b-3b30-839b-45cb2c69d708 | -7.06226 | -59.42027 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b90240e5-37c9-36fa-84ad-2d62317f974e | -7.06043 | -59.41747 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6e0e4cb-9478-3370-bb39-25dbcc802d43 | -7.05986 | -59.42174 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 820521ec-761f-3a16-a461-51056ec48b2c | -7.05695 | -59.41513 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f83f59b8-994b-3960-b24b-22677335ad3e | -7.05635 | -59.4194 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db2105a0-c092-34f9-b82c-9065e02bcf39 | -7.05508 | -59.41231 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2454d4cb-e952-3a6f-bd1d-14190e0b0f1e | -7.05451 | -59.41658 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24426035-af01-308b-9e6c-5ed97de3f442 | -7.05395 | -59.42086 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff93ebf2-51b6-32f5-bd17-c033703f0154 | -9.86324 | -60.31841 | 2024-10-10 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1815768-8319-36f4-9f3e-93dc5d7540a7 | -9.86271 | -60.3225 | 2024-10-10 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d867b01-d832-3c65-98f4-5e35fc69114b | -5.49752 | -60.4578 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a476d142-e60b-3d61-9346-c6c88a47d984 | -5.41578 | -60.60795 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d5e9e35-d345-3536-87ac-da3873ff7fd2 | -5.41531 | -60.61129 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4bc3c67-f0d1-333a-9823-740a239acb89 | -7.99267 | -61.31604 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9328a4ca-4e6a-3309-88cb-108529d03fdf | -7.99223 | -61.31933 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c550ba9-509c-3404-acbb-58a44208b724 | -7.98781 | -61.31205 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dc53d45-4aab-33a0-afbb-7096bb5bc7b0 | -7.98737 | -61.31535 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d6be4a2-eb58-3e94-9a05-6854d94ec873 | -7.79637 | -61.58226 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44aaf970-fa8f-3bc4-a165-337cfdba1722 | -7.79595 | -61.5853 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73d4af6c-ab9c-3994-8f22-4e311479cf57 | -7.79162 | -61.57846 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c881f4c-48de-3a77-9d51-c618f0ce7b31 | -7.78023 | -61.3513 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665f6c7c-b868-3011-b95c-9fc772bd8c76 | -7.7798 | -61.35451 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7da800cc-85e2-3425-aa6c-7fc41c09f838 | -7.77497 | -61.35055 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c563c9-0a7a-362e-b220-8a770b3288a7 | -7.77454 | -61.35374 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64567d69-e9a4-3e17-b172-25bd85fe7323 | -7.64613 | -61.20703 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c3fd15f-b5c3-3822-bf06-3f0a564da032 | -7.64568 | -61.2103 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8f7fda4-d2aa-3b1b-afdc-73f4cd72ca47 | -7.64497 | -61.20676 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1da3e30-9f32-37fa-a959-3786cc82f70e | -7.64454 | -61.21004 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c117a2ba-66b4-36d2-94a8-32c1c68efc0a | -7.64129 | -61.20302 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adc8c07c-ec1a-35e7-be6d-e01df18b237b | -7.64083 | -61.2063 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9641265-07eb-3bd1-9e89-42d139dcda75 | -7.64038 | -61.20955 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f39a35f-5966-38d1-aa83-e79c72fc17be | -8.23954 | -61.18482 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d3e7a2-4d00-3074-895d-fa8eaaf78c7f | -8.23909 | -61.18816 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5327c70c-fb18-3e6b-a72b-faf6ad8137b7 | -8.23864 | -61.19151 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d62a2042-12fc-355f-a94d-762783be5c1b | -8.23819 | -61.19487 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c3f9315-5eef-3a9f-bd62-5c2d9d0289cb | -8.23774 | -61.19823 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe32126-741b-31b6-9b25-b703bbd9679d | -8.23553 | -61.17402 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1302fa-c932-3c32-9d35-eacb30fbec16 | -8.23508 | -61.17739 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab11bf68-14cf-31ec-870c-eca1599f69f6 | -8.23463 | -61.18076 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7529c7d1-e487-3f71-862c-5deb4b97a665 | -8.23418 | -61.18411 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f9a042a-71a1-3c61-b429-4e01f56b6ba6 | -8.23373 | -61.18745 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c55c7b5f-2263-3bb8-b911-edba83664944 | -8.23328 | -61.19081 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a49e614d-14e4-3237-90e7-29cf9616298b | -8.23283 | -61.19418 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93624113-4389-3d5d-aa1b-4a0b8be87a80 | -8.23238 | -61.19753 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 653d0fb6-94a7-3332-8138-e19affeea8da | -8.20964 | -61.20458 | 2024-10-10 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f7ed24-ebcf-32ab-a3c0-79ae40693970 | -11.15461 | -57.188 | 2024-10-10 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9341325-cd1a-3b97-93f7-9bb74ab5555b | -10.40734 | -59.14859 | 2024-10-10 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969e2121-6c84-3e87-aaff-8cfa0138e726 | -10.40167 | -59.14262 | 2024-10-10 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34c899de-fd8a-3ac1-a78e-88ef58952e24 | -10.40106 | -59.14767 | 2024-10-10 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 079fb413-b120-327c-8c88-8f4922069075 | -12.30585 | -59.1692 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c766cf89-cc1f-35bc-937a-fb53d4d736db | -12.30524 | -59.17458 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3ef7792-7afb-3803-bff2-b0758fa4c506 | -11.81867 | -58.84114 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a02505c8-8c54-3880-9e2f-3e845460776d | -11.81803 | -58.84668 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e17ede24-448d-3e1c-940b-0b7f5db7aac9 | -11.81216 | -58.84019 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11bc0492-17c8-314c-a0f6-fd7936d096b9 | -11.81153 | -58.84571 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4d3f98e-76b8-3354-8296-9b9647ed5e40 | -11.71304 | -59.28507 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2debea6c-650f-3621-8482-1a124ccdba56 | -11.71243 | -59.29012 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9ce996f-5904-3d88-a5d3-689130880ef1 | -11.66846 | -58.89254 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11b2c040-23fc-3e20-905b-06d5ecac353c | -11.6678 | -58.89804 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d431b0d-4621-3dcd-8e39-6393fd6773ff | -11.66773 | -58.89271 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README144.md)
