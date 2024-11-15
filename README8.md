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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d300362c-5e65-39aa-b99e-9e896c1d5257 | -17.5686 | -57.449299 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68bd1d81-97c0-3052-aa9d-e210274cd44a | -17.578199 | -57.4464 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d17a9249-d90c-32c4-b59e-eced3e994c32 | -17.704201 | -57.527 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 756e7ed1-147e-3d12-929f-50088908c32f | -13.4803 | -60.662701 | 2024-11-15 01:51:00 | METOP-B | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3af28d94-5fb0-3864-9289-bc295bcbce7d | -17.584299 | -57.468399 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62518483-4ce9-349f-b375-59296cf88359 | -17.5832 | -57.540001 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6ca760e-40d6-3aae-b1ab-8af5b2d5dca7 | -17.7006 | -57.551601 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9615ada1-d92f-3455-878a-6367cdcc0fed | -17.2374 | -57.452801 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c6dd02a-db2f-36ee-8418-ccc6ce53721a | -16.939501 | -57.614498 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 989d05f7-114c-3650-9369-350aea655ffb | -17.2313 | -57.430302 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 869e8f40-f181-30b0-955d-8a3d436d4bce | -17.5856 | -57.5863 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 614c7f13-266a-36e2-9e9e-78782ae692f0 | -17.618 | -57.553101 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0bc89d58-bfd0-379d-bf93-3c1342085926 | -17.6371 | -57.547298 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6606ad3f-cbf9-3787-8d6a-f7415f8ead5a | -17.573601 | -57.5429 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2008021-f9b6-3f09-bb6d-0dfa265a8128 | -17.697001 | -57.576099 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53a5e518-c298-3b06-b1cd-2f4cfa162822 | -17.253201 | -57.472301 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 906f1b5a-7a37-340d-a21a-e36d53868ead | -17.563999 | -57.545799 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dae09dff-bbf8-3bb6-83cf-1702390b0f47 | -16.9359 | -57.6394 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a20d94bf-9045-3986-9df0-148067c18e0e | -17.576 | -57.589199 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bbd7b4e-ce97-34d2-903a-9b40a6a1843f | -17.247 | -57.449902 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4557b9b6-dd81-3db3-b19f-b0b6d9c6fae0 | -17.2279 | -57.4557 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52ea1855-da68-3c36-813d-f47f18d53db2 | -17.684999 | -57.532799 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b0065d4-13fb-385f-b7e2-149905a6c490 | -9.3836 | -67.212997 | 2024-11-15 01:51:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e820bdfe-169f-36a5-8f3c-7a5251df32cd | -17.5676 | -57.521 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ab124ca4-d2b5-3ad4-af8f-4984923a767c | -17.574699 | -57.471298 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73109ce9-a1e7-3ab0-bae9-64c07a33b6ed | -17.558001 | -57.523899 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 084206fd-d99e-363e-b720-6e3ddeb9d15d | -17.694599 | -57.5299 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf9211b4-a2a3-345f-835d-3cbfd650b499 | -17.579599 | -57.564602 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d06644e0-48df-3a89-8bfa-db136e714e5b | -17.554399 | -57.548698 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7386a2e-c892-3c60-9efd-654b49e65bca | -17.243601 | -57.475101 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c1378b3-4561-3b36-93b1-c50ebca8d8d7 | -17.5604 | -57.5704 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6f92c88-4729-3afd-ab89-ba99bf778fdc | -16.929899 | -57.617298 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45f39ee9-8249-3a61-91e6-932784ae6077 | -17.691 | -57.554501 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7e83213-ddc8-3355-9796-acb96dd90dea | -17.589199 | -57.561798 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d56b0048-e9d2-3247-96a6-2e276b3dc5a0 | -16.945499 | -57.6366 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ad1560f-7e2f-3bca-9b30-2bc85d1fc200 | -17.57 | -57.567501 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84f37f5d-491a-3e7c-8a95-d01882ab3bb8 | -17.548401 | -57.526798 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 089a3c8b-ef36-36ab-b841-4cd3e40c2ac7 | -17.6311 | -57.525501 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32cf9b4c-6bb7-37c1-b4ec-06ac3f11a0e5 | -17.688601 | -57.508099 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13bc88c8-61af-3c81-abfe-36e54cc38549 | -17.221701 | -57.433201 | 2024-11-15 01:51:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c60e399c-e7c7-323e-8f2f-c1e1bddbc281 | -17.621599 | -57.5284 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6e544b7-f4b1-34f3-8724-f547c6e73933 | -17.6276 | -57.550201 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68159953-f16a-3680-a567-36424a972a29 | -17.580799 | -57.493301 | 2024-11-15 01:51:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86bafebb-b0c0-3cdc-ae76-7e5b2f874dc0 | -2.641 | -46.1849 | 2024-11-15 02:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b71b76f0-a785-39c0-afe6-77bb352981cd | 1.3035 | -60.4074 | 2024-11-15 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e1b88e5e-8c2e-361c-9e0d-f98456722f68 | -17.235 | -57.4516 | 2024-11-15 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 99429fb2-5e5b-3264-bb34-f88de2ee0df2 | -17.2547 | -57.4493 | 2024-11-15 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 756fcb4c-5a99-35bf-a35b-3bbf091c974d | -17.2543 | -57.4698 | 2024-11-15 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.0 |
| 5fe8d4cb-90f2-3405-aa33-f76ec33f847f | -3.8054 | -43.9002 | 2024-11-15 02:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2ba18a04-0ec7-3158-b174-040f0e6ba95b | -2.6595 | -46.2065 | 2024-11-15 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 3aacb2bc-452d-3d58-a5c0-9509aced4949 | -2.6596 | -46.1843 | 2024-11-15 02:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 8d6d4464-ac67-32f4-a2ce-d0e7e6ae4002 | -17.7048 | -57.5597 | 2024-11-15 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 2648c241-e89f-3914-bc2b-2b8c12bc2cc2 | -17.2347 | -57.4721 | 2024-11-15 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 577f14e0-2a9f-3268-84ea-ed0ba4959c12 | -3.7867 | -43.9011 | 2024-11-15 02:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6ce3fb79-4bac-3eb1-8399-791b95b93a4a | -17.5882 | -57.4711 | 2024-11-15 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 88166ef7-4fee-324d-8640-b2d65c559ecf | -17.5879 | -57.4917 | 2024-11-15 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 9063b49c-8ba6-3f08-9a5d-70b0a1b4115c | -17.7052 | -57.5392 | 2024-11-15 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| a1a3158d-755e-36ce-8fcf-e9ea6fb15da1 | -16.958 | -57.6269 | 2024-11-15 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 1967310e-03c5-32fb-8cb9-f01e0fb3c673 | -17.2547 | -57.4493 | 2024-11-15 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 7e87d930-7fb4-3fb2-94b3-2e0428ad388b | -3.8054 | -43.9002 | 2024-11-15 02:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 01f275dd-7187-36a9-829d-086497af4ab6 | -17.7048 | -57.5597 | 2024-11-15 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 8417b130-f57b-39e9-a08f-f63610f9632f | -2.6596 | -46.1843 | 2024-11-15 02:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| f5f10fd9-68e7-32a9-94fb-9860be322fd0 | -17.5879 | -57.4917 | 2024-11-15 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 4a14ce6e-1bc7-3609-a5bf-0faab4f4d59e | -3.7867 | -43.9011 | 2024-11-15 02:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4b1c0f17-be11-354a-9bbe-adebe5527d4a | -2.641 | -46.1849 | 2024-11-15 02:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4e5949b4-64ab-34c2-84b1-318aa121e49c | -17.235 | -57.4516 | 2024-11-15 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 2b151364-051a-3d16-9de9-bb7e1606f7db | -17.5882 | -57.4711 | 2024-11-15 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| e376df9f-efa7-38bd-89ea-2f600756b7ce | 1.3035 | -60.4074 | 2024-11-15 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dab1ebfb-8e60-321c-b9ac-d1aef0a6b77f | -17.2543 | -57.4698 | 2024-11-15 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 152.6 |
| a58862bf-3277-30b3-b2fc-18ea9458d9bb | -17.2347 | -57.4721 | 2024-11-15 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| cad96518-b1ca-33d9-a360-59e73b6799e3 | -17.7052 | -57.5392 | 2024-11-15 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 9ffa4bdf-cb22-31c3-a0ba-1b4518a9bae6 | -17.274 | -57.4675 | 2024-11-15 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| d00ee955-6df0-328b-9215-73ff68bfc6e1 | -17.7052 | -57.5392 | 2024-11-15 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 25369b32-0471-39d6-95c3-8ba9fe19e700 | -17.2347 | -57.4721 | 2024-11-15 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 012ca48e-e035-34d4-8ea1-74f085dd3909 | -17.7048 | -57.5597 | 2024-11-15 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| d14881bb-87e2-315f-966b-be6da339029d | -2.6596 | -46.1843 | 2024-11-15 02:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| db7f67e5-14e6-3b86-8671-42c585edfb3c | -17.2543 | -57.4698 | 2024-11-15 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| 90bceceb-c7f8-314c-8a5c-0a41ffc06db2 | -17.235 | -57.4516 | 2024-11-15 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| d3706480-5382-345f-a094-0e6c1254fba5 | -17.5879 | -57.4917 | 2024-11-15 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 673ce9bd-4a74-3adf-9b1b-426d9e3109d3 | -17.2547 | -57.4493 | 2024-11-15 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 804fea24-87d2-3b75-969c-aefdd1c85945 | -2.641 | -46.1849 | 2024-11-15 02:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 393a573b-0890-3cab-8d13-166d57344a1f | -17.5882 | -57.4711 | 2024-11-15 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| e215fa09-90cf-3037-a675-c72052a2aa74 | -17.274 | -57.4675 | 2024-11-15 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| a8bf544b-75c8-31f8-8a63-c5c45857c240 | -17.274 | -57.4675 | 2024-11-15 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 12dcb3c1-4035-318b-bb6c-ba5a32a0357a | -17.7048 | -57.5597 | 2024-11-15 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 89fbd0b2-8159-3c2e-aaea-25259dcbb938 | -17.5882 | -57.4711 | 2024-11-15 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 96e45fc8-f41e-3d74-8f3f-e24da1c2ed19 | -17.2347 | -57.4721 | 2024-11-15 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 7a7545ed-0b75-3819-a883-9ce051803231 | -17.235 | -57.4516 | 2024-11-15 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| d290a4bb-ff01-38dc-a292-562cc6c8729e | 1.3035 | -60.4074 | 2024-11-15 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| dc995242-7bc7-3e93-a8fb-5846678859eb | -17.2547 | -57.4493 | 2024-11-15 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| e7286119-2e3d-3612-b541-f0a3aa5dbcd1 | -17.7052 | -57.5392 | 2024-11-15 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| e6be7848-d776-382f-92d6-99b84bb73075 | -17.5879 | -57.4917 | 2024-11-15 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| ddb0ca39-d89a-3bab-9283-763a49edc4f2 | -2.6596 | -46.1843 | 2024-11-15 02:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f275fab6-ae77-3473-be05-283771423d15 | -17.2543 | -57.4698 | 2024-11-15 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.0 |
| 4b2015b8-3667-3b38-a7dc-a10096117bcb | -2.641 | -46.1849 | 2024-11-15 02:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9938eacf-4cfe-3d19-ae16-1badeb70f427 | -17.5678 | -57.5146 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| cbdc9ff7-be08-3656-b929-ae50fe1d5318 | -17.2547 | -57.4493 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 2be84bb9-32b9-374a-808c-97af1881f018 | -17.5865 | -57.5739 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 344.0 |
| 1a9a21cb-36d2-3038-8e79-e7cd76629c90 | -17.7052 | -57.5392 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| ad55639b-88b8-338b-95f5-07eae6a4bb4c | -17.5869 | -57.5533 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 279.4 |


[Clique aqui para ver as próximas entradas](README9.md)
