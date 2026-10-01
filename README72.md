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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 586cfb82-a707-34ad-81ab-d40c6767fc77 | -4.26359 | -50.76913 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3e776af0-a12c-3faf-ae19-13a5dc9d1f97 | -2.99222 | -51.02811 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b6a30850-fe83-309d-90a5-c5cead3a9040 | -4.26517 | -50.75816 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 33fbc427-2118-3722-b6f2-b92a366b8903 | -3.98415 | -56.08824 | 2026-10-01 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04fb555a-a979-3187-b382-43a38c22bf27 | -2.99003 | -51.04325 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4950f5f-7767-3f18-a2a0-545ab2c00d2a | -4.30361 | -50.76958 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| fc3be63a-c70d-382b-a43f-afadebe4817e | -4.6351 | -50.60691 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a3882f74-2fc0-3c42-ac81-a2b3782af1d3 | -4.63765 | -50.62442 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3655376c-2a96-3147-8f04-ce96e7c6539d | -2.50046 | -56.90874 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35a0c031-c400-3c20-bade-ef0aba9d1610 | -4.63015 | -50.60593 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8480a2d4-ced4-3584-91b7-60cf92100274 | -2.8966 | -54.13704 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df118d0a-53ab-3afc-ba72-66bb7356cdc2 | -3.02958 | -53.86805 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7476f596-9891-34e8-a4f5-bdddcf546496 | -4.29628 | -50.78536 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7b5ed9a6-52b9-3339-863f-300ff35a557d | -4.29139 | -50.78461 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| faec826f-a157-36c5-851b-4fc7ba13f5fd | -2.9815 | -51.02518 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 334bb349-58db-3554-8f6e-9858bf79a04f | -4.27747 | -50.77702 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 133fa62f-f5ac-30bc-9b07-2729133f23d0 | -5.18386 | -46.19088 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1808860d-c453-3798-8af6-cd5aa28d486f | -4.05951 | -51.09556 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9261bc-57a1-3e1b-b34e-fb92a7664545 | -4.63805 | -50.62164 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab0d5915-74c7-3e20-85d9-372678bbeaba | -3.18074 | -51.2487 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 814c5f35-dc15-3de8-8478-1ce5fb66ca43 | -4.13092 | -46.86948 | 2026-10-01 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1de4e366-126e-3fdc-b4cf-4c3d8025a561 | -3.16934 | -54.08085 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aabdfa74-69f9-3279-bad0-2654b85259b8 | -3.15008 | -54.07788 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43fff70e-8757-3887-abe1-956ed221a850 | -1.81706 | -57.1033 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee1fe029-4e60-32ef-9629-c6baf1906c89 | -4.28649 | -50.78386 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| d8c3327b-e365-384d-8937-9b04c79e01b5 | -4.63387 | -50.61536 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3953ee1c-0259-3ebf-bbe0-8906362ade71 | -4.45455 | -47.92216 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1b156eb4-5a4e-36ec-bda8-7e8e78a3ff65 | -4.13022 | -46.87457 | 2026-10-01 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44cf6a82-ceae-34aa-9b18-975bdf8d43d1 | -1.79907 | -55.3511 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a78124d9-7b29-3d66-af6a-eac8544d29b6 | -4.63429 | -50.61248 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb2f9c8b-fc68-3ef9-8b4f-f936441a4c2a | -2.97526 | -51.03454 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c01ed24a-0320-39e6-870b-bc6338194981 | -3.38105 | -50.94587 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 598542c6-f83a-35a6-bed1-1483f21b03e0 | -4.63345 | -50.61826 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 991d92a2-41b8-36fe-844a-236a6898e9bb | -1.91849 | -55.04928 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e36e2665-b918-30ea-a9b1-7d4ad01ab121 | -3.56949 | -51.47832 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| be62a8e2-d3b9-3189-9704-48ab5b29c1c9 | -4.1639 | -48.89961 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a4fb06-c075-3097-94db-bfccd608c76b | -2.99149 | -51.03318 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5156dfc-10a0-31ba-8215-2a96b71291d8 | -2.90911 | -51.31539 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e44d4ddf-5463-3e4c-b00e-002e1dc86461 | -4.27499 | -50.75961 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 89005105-c8c5-3f1d-a034-2c0bb58ef89e | -3.33143 | -59.38971 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 114ff53d-8086-374a-a5c9-c6837b218ce9 | -3.16067 | -51.35483 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52011115-b5e6-3f54-8b86-8437c9232a20 | -4.27659 | -50.74858 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a1a79b31-b641-38b4-9783-8f945fc2c97f | -2.96734 | -51.023 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eed562af-7882-3767-9e8d-8d95309fa099 | -4.83407 | -50.68356 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe033622-84cb-34c2-a109-8fb2eb2dc88e | -1.9149 | -55.04873 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a102499f-80fd-3ab8-bb75-722be1f2c613 | -2.85962 | -54.12952 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86d49480-9297-3827-a1e6-8c8e0bf76cf9 | -4.8897 | -48.37173 | 2026-10-01 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bad312da-a0be-3e7c-94e8-0da2141dbc61 | -4.26267 | -50.74069 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a4148cde-afd2-308e-a303-dfc5c0921c46 | -4.30198 | -50.7807 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8db6ffba-8017-33f3-bc1f-624376c77fbb | -4.28081 | -50.78851 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 4bafcfbb-68ea-31ec-b24b-aa80c5a058a6 | -3.80917 | -51.03312 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d3842fb2-0f51-3b41-a883-cc745179a547 | -3.10836 | -60.67843 | 2026-10-01 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61c2a602-c32f-367c-9d6d-910a7dd486ef | -2.02975 | -56.78223 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4d22e4d-1e7c-3f17-810d-af361dc93fb2 | -3.92894 | -55.75808 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e090df-6683-36bd-bd90-2c182a86f9ca | -3.37702 | -50.94004 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24fcdea8-a210-3777-82a5-b7f19d08c661 | -3.27424 | -50.70293 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4852217c-e8e7-34df-960b-9241617419a3 | -3.00998 | -54.23336 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eab0083-72a0-3192-8dbb-f190b1ecd035 | -3.83296 | -55.79365 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4259ecb-4e08-350f-93a8-e8f771135096 | -5.53817 | -50.04101 | 2026-10-01 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06292123-dae6-3743-93f6-c37985b4e406 | -3.95654 | -49.05186 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c2cda5a-0e76-3a5f-8fd1-15a398aa1f08 | -3.18082 | -60.06421 | 2026-10-01 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 404ca3e7-f808-3006-9942-cc8045ebec4f | 1.70507 | -55.90911 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e061d5aa-1ab3-3972-a87a-e1eb32cff66e | 1.81032 | -55.62067 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f295b7f-9a04-32e9-83bd-b94a7fe35a4d | -3.15853 | -54.0742 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6adcf95d-e701-3b15-ab43-f8b53702e519 | -2.9745 | -51.03956 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63c7b27f-1529-391c-98a7-000b7d4a67c5 | -1.6386 | -55.12216 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e69da7-9ea8-3bdb-8946-3bed6eaa786f | 1.70899 | -55.91215 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65e20d77-19f5-3b6d-be53-b939027f25ad | -3.16476 | -54.08506 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e0c5982b-d1dc-3010-b8f7-f92b8f1f58c0 | 1.85661 | -55.55385 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a49b2a12-58f8-37c5-b2a9-b8c89dfd027d | -4.06279 | -51.10629 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99659a2e-3d02-3e5d-ad6e-4a31b17f4aa0 | -3.15779 | -54.07901 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8af2b20-2eb6-3cde-86e2-e05261e4b1d2 | -4.29708 | -50.77991 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 4967cf7e-a479-3669-bf26-89de8c2b3dde | -3.92549 | -55.92434 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80eab977-8f87-38a1-8452-8ed8086e9f7f | -1.83338 | -54.99146 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a71e56a-7f77-3bf8-b723-6dc634b02cbe | -3.25103 | -50.11918 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbbd2bea-c971-312d-9a02-ca13af1ede84 | -3.01958 | -53.88167 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f00749ff-7010-3a39-badb-fab128a96c62 | 1.71738 | -55.92179 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ebad07e-47bd-397e-92ab-f86b13418d7f | -2.78651 | -56.49037 | 2026-10-01 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e69f68-a1d0-33bb-92c1-b85f26d1ab21 | -2.41891 | -49.29903 | 2026-10-01 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7cec3b1-1f51-3c13-b730-394c98df5185 | -3.0076 | -54.22334 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77db6886-a8eb-30a3-889c-94f1866315d1 | 1.78947 | -55.64245 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c26e40-bb72-3de7-8097-a17816cba0f9 | -2.90354 | -54.14294 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e6559c17-aa3f-3c9d-a661-5b58f99104f4 | -2.90064 | -54.08427 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4896752-1765-309e-84f5-85823066d07d | -2.82326 | -54.57144 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04fddba9-4bfc-317f-a5de-874269c40e13 | -2.97054 | -51.0338 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0700ac5d-6f46-3e50-8841-294c6854921b | -4.30117 | -50.7862 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 59f8a687-2038-3caa-94f7-32be1cdcbcd7 | -4.27103 | -50.78688 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7b27e9f9-89d2-313c-b9cd-4e4601caae1e | -5.17916 | -46.19961 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51b3c780-aed6-3673-a6ec-a82cca993459 | -2.85834 | -54.13113 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d033ac8-0831-3acb-8216-7a79c16ee0f7 | -1.21193 | -49.28608 | 2026-10-01 05:16:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e68b23a2-b854-3500-a01a-9ceea30b8ca2 | -4.30279 | -50.77515 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ac6ba0df-868b-31de-a641-316526540e78 | -3.2035 | -54.73702 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b68afad-ab96-3f42-930e-0e47d43ae49e | -3.15706 | -54.08383 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee0aecd-7d37-3c1c-a649-b4fa2b59f949 | -3.01122 | -53.87873 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9a8e155-8858-32e7-b5e3-40fbec744953 | -3.22571 | -54.3187 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a66f4743-9795-3f71-9814-3f1f027c8935 | -3.16639 | -54.10009 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c953a56b-efa4-30c6-b642-dcb1db8edbb0 | -3.27073 | -54.27497 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab1163e7-ebcb-3c8b-b29b-b8f966544a4f | -2.15202 | -59.22977 | 2026-10-01 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b87ec2d0-762c-38fb-9335-86b53b6de279 | -3.4925 | -54.72993 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db5f63ad-3fed-357e-bc4b-3ca138320dc5 | -4.25127 | -50.75027 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |


[Clique aqui para ver as próximas entradas](README73.md)
