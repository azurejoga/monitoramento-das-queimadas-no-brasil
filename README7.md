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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7994176-65f4-3140-99d7-251a97433e41 | -7.5476 | -61.3437 | 2026-09-04 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8eb05c55-3c86-3400-973f-6ec887e96baa | -8.4483 | -54.725 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f15ae833-594c-3190-8a5f-8c88fd78dc56 | -18.7363 | -48.908 | 2026-09-04 01:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5433d7ef-00b7-3846-bd85-cb5637ad9e98 | -8.505 | -54.6404 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 332.3 |
| 2de2dbea-4f92-371e-a486-0cdb06d6dffe | -8.4861 | -54.6619 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| cc8e2300-0748-3d7a-851d-d180c99ea178 | -5.5793 | -43.9992 | 2026-09-04 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 096ba5c3-b6be-35a8-91b0-45c4ae7a997b | -5.598 | -43.9978 | 2026-09-04 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fbad2a0e-f6aa-347c-8794-92ad43f15d03 | -8.4479 | -54.7653 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7df229ad-ea98-366b-8466-6f42d3433d67 | -8.4668 | -54.7439 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 285.5 |
| 15f62091-c4ae-35ff-b97c-1219afbe6314 | -4.6668 | -43.5053 | 2026-09-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2d12ef11-575b-35ee-b1fc-69ac45afca42 | -8.4481 | -54.7452 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 242.0 |
| 9c8535b5-03b5-38ff-9999-d5b5698e4dd6 | -7.566 | -61.343 | 2026-09-04 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| c7ee13a2-7a4b-329a-9b98-990b2f4fdce2 | -8.1126 | -54.7871 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| fbefd66c-4f57-35e3-b511-cc4c04bf25db | -8.505 | -54.6404 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 289.2 |
| 6c61ed4b-9650-3a31-87bc-58637c6d6215 | -8.5046 | -54.6808 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cdcdd509-a5bd-3713-b102-e48e5ee4b238 | -18.7363 | -48.908 | 2026-09-04 01:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| dfd423aa-5796-3591-925e-9aaf44c2a459 | -7.566 | -61.343 | 2026-09-04 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c189e725-d340-3785-ae9f-14fb92d25a26 | -8.5048 | -54.6606 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 351.3 |
| 0e637374-f913-31ab-b345-c8db4073d790 | -5.598 | -43.9978 | 2026-09-04 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9b5316a4-bfdc-337d-9291-228d3b12e16e | -8.1126 | -54.7871 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 13e8abe3-851b-3f9b-b4ce-56e28b94a0b6 | -8.4863 | -54.6417 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 74d8db50-42be-371c-869b-5c2c403b954b | -7.5476 | -61.3437 | 2026-09-04 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d4548886-f4c2-3628-8c52-5a6a7fb66862 | -8.4861 | -54.6619 | 2026-09-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 6405f69d-fbfe-34a3-82de-1e8cf957b736 | -8.5048 | -54.6606 | 2026-09-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 313.3 |
| 2543d5d4-b5ca-3832-877c-986c7abf2dcf | -8.4861 | -54.6619 | 2026-09-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 283710a0-05ad-30f9-8dce-38925a9f6dc3 | -8.1126 | -54.7871 | 2026-09-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 33c85093-1063-3361-ae72-ae7d20b37847 | -8.4863 | -54.6417 | 2026-09-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 58cefaee-f5ac-3156-86cc-8fde577cf6e6 | -7.566 | -61.343 | 2026-09-04 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b364920a-cf48-3c64-a8d7-050189804d08 | -7.5476 | -61.3437 | 2026-09-04 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 58d47f59-efd7-31c5-8fc0-0b5c2bd22d52 | -8.505 | -54.6404 | 2026-09-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 222.2 |
| bfc1451c-a9b4-3b8f-b7b3-ed5331ee865a | -8.5916 | -67.1788 | 2026-09-04 02:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e7907e87-1566-3197-a659-5ca732ddc163 | -8.5048 | -54.6606 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 257.7 |
| e4a3e9a0-b96a-314b-8ec0-48e59a7876e3 | -8.1126 | -54.7871 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 5203a261-97f1-3bee-ad5e-d86fd99b74ce | -7.5476 | -61.3437 | 2026-09-04 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| c537c410-6df4-3019-bb6e-f56f950e01b4 | -8.4861 | -54.6619 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 07b10e0a-60db-3fa0-9932-ed0cd943ff27 | -7.566 | -61.343 | 2026-09-04 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f171b54a-b864-3aa7-a949-037852998271 | -8.4863 | -54.6417 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 2871864f-433d-3f9f-9694-2ab7cc66e28d | -8.505 | -54.6404 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 2bd62877-9761-38e8-9ed2-cb85b3d2b51c | -20.997 | -49.1116 | 2026-09-04 02:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.6 |
| 3652df34-9298-313d-818d-cff7be27a7d1 | -10.8441 | -51.7913 | 2026-09-04 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9a285cbe-73eb-3736-9391-7e92d439e9ac | -8.5234 | -54.6594 | 2026-09-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 11c7ac32-26db-3cd4-822a-de5f92f2efa5 | -7.566 | -61.343 | 2026-09-04 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7029277d-f367-35f5-ab17-2f27c146fae8 | -8.5048 | -54.6606 | 2026-09-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 234.5 |
| 056cd697-e253-39dd-97fa-fd728a62cf02 | -7.5476 | -61.3437 | 2026-09-04 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 22e11bf9-e456-3274-9fe5-8898c8386e12 | -8.1126 | -54.7871 | 2026-09-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 0a4e8e01-8021-3273-b192-c454cc3efd86 | -8.4861 | -54.6619 | 2026-09-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 216e6bb3-65af-3402-b007-7c0c1b7992d0 | -8.4863 | -54.6417 | 2026-09-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f201c3f2-7e9d-358a-abcc-7e947ccb307c | -8.505 | -54.6404 | 2026-09-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 029341f6-ffdb-35a2-a22c-0705db79eb42 | -9.5913 | -40.3448 | 2026-09-04 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 017b4605-5a3e-345b-ac3a-8a9aee1870ff | -8.5048 | -54.6606 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 244d1b07-adca-3eaf-a6b5-0b330cff803e | -8.4861 | -54.6619 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 2094fdf4-b355-36fe-80a1-752c4fbf6089 | -5.565 | -60.1739 | 2026-09-04 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4cfc51cd-a9ae-3b9f-baa1-c854e8b7d451 | -8.1126 | -54.7871 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6ba1672d-12d8-3306-a644-55b5ae894c0d | -7.5476 | -61.3437 | 2026-09-04 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| dab2f52f-8889-365f-90c9-6364919ae00d | -6.6881 | -59.982 | 2026-09-04 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3ca3897d-01db-3bb6-b24a-4a24fb08dbb1 | -8.505 | -54.6404 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| dc72132f-0faa-32aa-b0ed-57ab175c7374 | -8.5234 | -54.6594 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5fd758f8-480c-3dfb-9c90-847e714a092f | -9.5721 | -40.3475 | 2026-09-04 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.1 |
| af153da6-cf4b-3e3c-8ce2-f45e60947a02 | -7.566 | -61.343 | 2026-09-04 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6620a94d-5403-35f8-ab39-b077d55777de | -5.5651 | -60.1548 | 2026-09-04 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 49647ea3-66db-3afc-b68e-9be105c6552e | -8.4863 | -54.6417 | 2026-09-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 79c421a6-410f-374d-95e4-73a73e246765 | -8.505 | -54.6404 | 2026-09-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 24bbc5cc-256f-3066-90ac-3f5c0bf756bb | -6.6881 | -59.982 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 24c1b938-abfa-3028-85e1-964da8c953c2 | -7.566 | -61.343 | 2026-09-04 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1e54745b-69cb-358c-96b8-11bf37c95851 | -6.1543 | -59.944 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 06a3077a-1749-362e-a76b-092d547cecd0 | -6.6882 | -59.9628 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 92a05d32-50e3-3b68-86d4-6aabb16398be | -10.8438 | -51.8123 | 2026-09-04 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6cf86839-af7a-3def-82ef-aebdeb74c415 | -8.4861 | -54.6619 | 2026-09-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5edbe736-43da-3a22-b167-f34a1745b600 | -8.4863 | -54.6417 | 2026-09-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 21e96b60-fb0f-3c05-9643-bc0f27c9b705 | -8.5048 | -54.6606 | 2026-09-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| c1b499c3-6f31-363f-9b69-5bee452118e3 | -5.565 | -60.1739 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7210beb8-dcbc-32a8-bef3-efb00f2e3ca5 | -7.5476 | -61.3437 | 2026-09-04 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e8ce4794-6734-306f-870b-e26ef658da85 | -8.1126 | -54.7871 | 2026-09-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6941d9c9-283a-3d83-a115-83bd23662327 | -5.5651 | -60.1548 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 36f349b2-deed-3a0b-b4a3-197f2babc4e3 | -10.8627 | -51.8104 | 2026-09-04 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| b250cbca-1be3-3045-b707-2767539fae28 | -5.5649 | -60.193 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 3d386357-62cc-3883-8a69-503a3fd2db18 | -10.863 | -51.7894 | 2026-09-04 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 329581b9-bb62-32f1-92d2-49e763465812 | -5.5466 | -60.1745 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3c707ec2-1b00-350c-81db-de339e84e024 | -6.6697 | -59.9635 | 2026-09-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 7bd1c6c4-99e2-3fca-a546-28de4e72e00b | -7.5477 | -61.3247 | 2026-09-04 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| bc266b24-a3c2-3865-8d8a-b1ffdc8e86e3 | -7.5477 | -61.3247 | 2026-09-04 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 051da7b3-ef67-3c7d-b9e5-6670c1786de2 | -8.1126 | -54.7871 | 2026-09-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1ebba5ae-abae-33a6-8566-ac49a3a404bd | -8.4863 | -54.6417 | 2026-09-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 742ffcdc-0825-3fe7-8224-b342c765dbd6 | -5.5466 | -60.1745 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f3510e5d-f94e-3e53-8e5d-11b8549bb686 | -6.7065 | -59.9813 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3112cf23-3484-3a3d-a777-d18124282e89 | -8.505 | -54.6404 | 2026-09-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 34ace4ae-0e8c-3bc0-80b3-e5c0a92a76f8 | -8.4861 | -54.6619 | 2026-09-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3dfd7215-9eaf-324b-828c-d64470d3efca | -5.565 | -60.1739 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e2ce8c32-79fb-302b-b23d-fdff3a29dfa8 | -9.5721 | -40.3475 | 2026-09-04 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 477bc773-6513-3a0a-b029-2e17cc993b41 | -6.6697 | -59.9635 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4e77175f-d2c9-3df3-b755-584ff538c3b2 | -7.5476 | -61.3437 | 2026-09-04 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a4c5288d-6f13-37dd-aad8-320318d63d35 | -9.5913 | -40.3448 | 2026-09-04 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 72cdf964-5420-3da5-a261-3595fd2ae307 | -6.1543 | -59.944 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 4ca56681-ca43-3e1a-8941-3a00ad1d4fc4 | -6.6696 | -59.9827 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fcd69ca5-ccf6-386f-a283-9a1879ffaeb5 | -8.5048 | -54.6606 | 2026-09-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| a4ea3844-42b9-34be-aad8-31e82517992c | -6.6881 | -59.982 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 94d238fc-42cb-3ed2-87db-cc2670472b5d | -7.566 | -61.343 | 2026-09-04 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 493f902f-660d-3e61-a4a6-0e53e2c7821e | -6.6882 | -59.9628 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 7f172b5b-6734-3d33-a715-556d089e1f53 | -8.5916 | -67.1788 | 2026-09-04 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0f5de666-4468-3c20-a386-15ac3b25b230 | -6.688 | -60.0012 | 2026-09-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |


[Clique aqui para ver as próximas entradas](README8.md)
