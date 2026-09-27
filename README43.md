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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70b8004a-6d0f-3fed-9efb-8b715f0e828f | -1.05216 | -53.56356 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9a8478a-4cd6-3903-bfe6-4d377e465bfe | -1.0514 | -53.56829 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 663af6d9-29d4-3caa-b757-2ab4fd505a25 | -2.92399 | -45.50635 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99c199ce-d919-3d0e-a773-3fde467b610c | -3.77381 | -51.9952 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3ff48c-5630-383b-bbd7-b4eb175fff21 | -3.71534 | -54.65499 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cebd4e70-56f5-3a7f-95ca-5d277c1d17f0 | -4.54144 | -54.97417 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae21b2f2-4682-371f-a4b4-e4b06ad888cb | -3.84103 | -55.90512 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1d7dda6-84c4-34aa-8a8a-7fdd99d9fdd0 | -3.94886 | -56.09039 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5ff92de-eb30-3924-a239-60036b73aac7 | -3.0033 | -50.47107 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8068534-e160-3f92-a92a-2968d30e3c88 | -6.09773 | -57.68117 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265bd9a4-2d9a-3cfc-a327-a702671d8870 | -4.5073 | -54.93975 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ebc4f28-dbd2-3f2c-8555-c909149cbc1c | -1.90386 | -52.08534 | 2026-09-27 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60fed9e9-07b9-38bd-915a-41b72373ea43 | -4.4645 | -55.43054 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfeba0ae-fc6b-30ea-8dcd-f46d34736e5a | -3.83281 | -55.90868 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c4d87c9-f3b2-3957-b1c4-0e4579deefbc | -4.29035 | -55.25357 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af3c324-ab74-380b-992b-4130ff88d822 | -4.56025 | -54.95024 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cd70639-c201-32df-87bd-678b0bcc780d | -1.80329 | -55.3156 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b00365e-687c-39f6-afc4-42d24231aba1 | -3.02255 | -51.38322 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a05fd9ca-08ab-3fc7-a743-2208ff1ba0d7 | -4.54514 | -54.97476 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23438e9d-301d-37eb-808d-1428a59a30fe | -3.88685 | -51.96177 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52afbeff-8527-3b37-9d9e-f75fad348b00 | -1.61536 | -54.92418 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4050b62-15b1-301e-b6a6-36ea0848fcb3 | -6.05953 | -53.60728 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d691e42e-4409-32e0-84d0-94fb2bdfdc2c | -2.99764 | -50.47562 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5546c742-a8b3-39fc-a87b-60913995db6f | -3.8513 | -55.81479 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a81d280-6cbc-3315-bc26-dc3a72f2af46 | -3.07832 | -58.01956 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e6a5fc6-4b01-31d6-9348-fa96eb6bc8f9 | -6.08927 | -57.62477 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c1e14b5-3728-3191-bf70-5e8cd7f588e7 | -2.16454 | -58.10906 | 2026-09-27 05:27:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b368d4d-6959-3af9-8507-e8c0fc402465 | -6.05755 | -57.82782 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42794b4e-580b-3622-a7f5-9c5886453fb7 | -2.96463 | -49.5614 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b588bf-c806-3dde-838e-edfc5e1d3168 | -6.01753 | -53.89048 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75938cce-e992-392f-9f95-8f02c1ea3fff | -4.55756 | -54.91813 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4dea96-9f00-3adf-9971-75ce3ee3172d | -2.96105 | -54.09388 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faf8d74b-0211-34d4-b861-a25c4a935097 | -4.2607 | -51.04936 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eef7b696-a8b2-3e5d-80c7-e447607fa59e | -3.67217 | -50.84602 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a9694e8-b9f0-3c95-a5d3-337394353ea7 | -4.98434 | -56.15246 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93a0f255-87bb-3b73-abf3-56f6c3679497 | -4.57917 | -54.92591 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1f4d0c6-7946-3592-af35-9ba1e58641a0 | -3.96093 | -56.12748 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e39254c6-c935-33d1-b4ad-72953180a3c4 | -2.90727 | -45.41964 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73cd4367-2233-3a91-a7f2-fdd4f845ed8e | -2.44392 | -49.22377 | 2026-09-27 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a3adee4-414d-3627-ad2f-497b4d33c1f1 | -3.78382 | -55.87718 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed81711d-2988-38fe-b5e4-9ef5880e1a4b | -2.44966 | -49.22141 | 2026-09-27 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae5649f-96e8-37b5-864f-c4f7acbc8c47 | -3.69734 | -51.36653 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2bd84966-1753-3b23-9f67-49abfda2bcab | -3.70125 | -51.37204 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4757dd7d-f331-3451-a2fd-33825912501b | -3.00593 | -51.30935 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee3f9c20-edd0-3d67-aa86-ced2b6a2a87e | -4.36411 | -55.28191 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e69f4b95-0685-3a04-9217-f93159bd0611 | -2.9193 | -54.16314 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f71feda6-7c28-3f95-9bef-d17a4e91c557 | -3.19061 | -51.03745 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36d68d7d-cfb3-3be9-880f-e3d29372fcb4 | -4.25578 | -51.05241 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6363baa8-6906-359e-808a-4bfe925c4c40 | -6.05541 | -53.60668 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 472bafea-96ad-30f9-847b-d0c86e55a5aa | -2.91314 | -45.4265 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5a7a2c-e4f4-3fe2-82b2-3c0d0931883c | -3.8728 | -52.28687 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14ba31cf-46b1-39a0-86da-ed3f00107ff9 | -2.96176 | -54.08924 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7827a53-e5aa-3621-af86-891546d9dc7b | -3.22109 | -53.95963 | 2026-09-27 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1ab057-c70b-3164-b50a-5052bbba19ec | -2.6551 | -56.4463 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a963f0c9-26f1-372b-86e0-a6e54af6fb9d | -0.5169 | -49.12409 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ca672a-1a77-3c70-b8d1-ab72e7e45a81 | -2.90305 | -54.19345 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4237f5fc-f95d-3d5a-be2a-f3a5d56366c6 | -3.42147 | -50.44115 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f03f704-16eb-372f-9351-fd4bb5631869 | -3.05217 | -51.21752 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cf935fc-c761-3723-8034-05ba10a11d0c | -3.87147 | -51.79265 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 631ccd3c-4ce7-3491-8c61-f09610b4614a | -1.8407 | -54.71717 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8617d42a-9bd0-3c09-8f64-7e0b6b451412 | -6.08815 | -57.63193 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb9b917f-2105-3403-a927-aa63e3ba0149 | -2.05876 | -56.86812 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb3127fb-5888-3e29-857d-4d2879ebfac1 | -3.96969 | -50.70876 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb21dfc3-fc8d-3eb7-b82a-0700c06e00b8 | -2.39966 | -57.64755 | 2026-09-27 05:27:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28d94c4f-e5e3-325f-9373-2f16a24b1873 | -2.66386 | -56.45832 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43be2cbe-ff6f-3496-bdd6-9b24de17ffcf | -3.0099 | -54.20526 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1fa4285-9064-309b-b5cf-93f3f85189be | -6.04715 | -53.60573 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 925b2b59-6fb6-3467-b39e-4661972d6dcd | -4.36346 | -55.28604 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5993966d-6e56-3431-84b1-a1e703b4ef86 | -2.67408 | -56.45993 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13b8c3e9-0cb9-3524-822a-bd298f7eafaa | -3.30483 | -54.6902 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce46152a-1f4b-3bce-8363-dc8112bedbc4 | -0.50522 | -49.13152 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4249c90b-61e6-31f4-bc4a-95ee43329b36 | -3.01819 | -51.53854 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a949682-874b-3b27-872c-cf9373cf0cff | -2.97607 | -54.14809 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19afae1f-8669-3252-aa71-6cc6496d650e | -6.08983 | -57.62119 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a91d262-8eff-3cdc-80a1-1f6060f6ec5d | -7.88398 | -54.72541 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63af09dc-f468-3cbe-a89d-d2139395ef33 | -6.87308 | -59.88057 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0304856-77b8-3e5e-83ea-90c44cc93009 | -9.04187 | -66.06187 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f56e3e13-b34b-3f2c-9b4b-5c7dc3ca3507 | -10.02051 | -50.13871 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7363c1af-0a02-3821-a7f1-3b7edce120c8 | -11.88279 | -50.5131 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe3d9395-0123-3892-b05c-b32937897374 | -7.47518 | -54.98071 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80921350-57a2-30fa-b8a7-7e2d5e3725b2 | -13.87757 | -49.04188 | 2026-09-27 05:29:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6a70a85-6864-3454-8fce-e6e5d755f9aa | -11.88428 | -50.50328 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8e2a2716-8ff3-3748-a1c5-0f479f28f264 | -11.99253 | -57.59971 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e263cad9-dcd1-3dcb-bf94-26301aa6e4e9 | -12.67068 | -54.6389 | 2026-09-27 05:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cee8b75-ddd4-33bd-9a00-fb61d20859d8 | -11.9827 | -50.56685 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 688cf81f-d423-3707-a46b-b21232a6032b | -11.81153 | -50.5011 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 207d8546-8df1-3ea5-95e7-69e469751c32 | -11.27347 | -54.44005 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3fb6d77e-5bd2-3291-a957-4ef1f559dc64 | -10.30993 | -54.2676 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30536a90-f94a-3c2b-ba38-c4e29c71a402 | -12.27641 | -50.30418 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 121c1e34-2606-38d4-aa29-864228f9230c | -12.13822 | -50.33828 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f87a8280-174b-334e-8029-38ca5df67402 | -11.81751 | -50.49818 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 924130e9-366e-3d67-b979-10ee80417592 | -11.70858 | -59.13388 | 2026-09-27 05:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9311bb6-d49e-3dee-89e6-a9ae33e70676 | -11.9463 | -50.49918 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b22454c-057b-30a6-89c7-ad288e84b9d3 | -11.98839 | -57.60319 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a4e7dd9-6d32-35cc-83b4-d9e1668520fd | -11.93986 | -50.50576 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8be2c9d2-ce27-3614-bda6-d9f4c19ba5f8 | -12.12591 | -50.29813 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce08f85-5573-3783-b16c-8dc4ba421ab4 | -6.64232 | -59.94849 | 2026-09-27 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 229016f7-0fb5-33d8-9bb3-c81372beaf9e | -11.88235 | -50.51675 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09b714e6-58c0-33bd-9af6-80907246cd6f | -9.08331 | -66.08768 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d83aaf3-d2d7-3c48-af36-ae8c82b1f398 | -13.10047 | -47.41059 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README44.md)
