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

## Dados Diários - Página 209

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c180f5-39c0-3b74-8db7-96bdb980328a | -12.4416 | -62.9988 | 2024-10-03 10:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 122.2 |
| fade0057-eb05-31b4-9ed0-465ba7582ca3 | -12.8996 | -62.4913 | 2024-10-03 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 5c5a3423-38a7-358e-b9cb-0811e016ecdb | -12.8998 | -62.472 | 2024-10-03 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 237.9 |
| 5a81a9e0-c183-365a-b8f2-ae9c1f5d8f06 | -12.8999 | -62.4527 | 2024-10-03 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 3286ed8d-5aa4-3b53-9400-7954b9667d6c | -12.9186 | -62.4901 | 2024-10-03 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 23408f1c-9469-3c7c-89b3-d000713f7e4f | -12.9187 | -62.4708 | 2024-10-03 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 117.0 |
| ab822570-454a-33de-8d88-1389356dc4fa | -16.6502 | -57.3149 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 382f2443-8e91-3232-a169-31eb0c1f8441 | -16.5928 | -57.2397 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.4 |
| 6f7b24de-6974-33ed-b7f4-0a4688a50627 | -16.6297 | -57.3785 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.3 |
| 76cf873e-29cd-3b40-92d9-c5934f0bbeb0 | -16.6496 | -57.3558 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.1 |
| f7b6e707-7d0d-3745-ad6b-ff12858c3080 | -16.63 | -57.358 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.7 |
| 9bc7b2a6-1c78-33c7-b5a6-5421104822b5 | -16.6492 | -57.3763 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.7 |
| 7361f758-f99c-355d-b87b-87ce00f764dc | -16.6893 | -57.3104 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.2 |
| dfa4e1d7-a27f-3072-a3dc-5477b0a4147b | -16.6701 | -57.2922 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.8 |
| 5bd18e51-ab07-30d0-bf98-5e1b13b04ae2 | -16.6698 | -57.3126 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 432.5 |
| c76e2b17-1132-3718-8e63-b262aad2a996 | -16.6694 | -57.3331 | 2024-10-03 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| b3ba990c-4faf-397f-b39f-92cbd602b70e | -16.765 | -57.4652 | 2024-10-03 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 8285b800-3637-344b-908e-fbbab980f96e | -16.7455 | -57.4674 | 2024-10-03 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 8e23bf12-a994-32c9-9b70-a6cb5713b8ad | -17.0309 | -56.7368 | 2024-10-03 10:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 355.9 |
| bdb60dd3-ed06-33e8-a82a-47653e952323 | -17.0306 | -56.7575 | 2024-10-03 10:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 760.7 |
| 0e217f20-1e41-3387-a2cd-fba1c97b142d | -17.0303 | -56.7781 | 2024-10-03 10:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.7 |
| 1ebe6b77-0a0c-3a3f-9d6f-765f13c9634e | -17.1774 | -57.3764 | 2024-10-03 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 256.2 |
| 18801e25-db30-3cf1-b6bf-c602e39f84e4 | -17.1771 | -57.3969 | 2024-10-03 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 280.1 |
| 40d3f80c-014f-31ae-ab79-4a1b9fb54fde | -17.1577 | -57.3787 | 2024-10-03 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 171.7 |
| 0c00face-11d2-32a1-82c3-904eb251c5aa | -17.1574 | -57.3993 | 2024-10-03 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 191.2 |
| 58797c15-507c-36e6-b84c-c32e19f96b2c | -10.9571 | -46.5918 | 2024-10-03 10:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 88475403-0735-3738-a0f8-c9dbf74ca305 | -11.2567 | -46.9123 | 2024-10-03 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 21b4b8bd-d17c-3920-9902-89a56aba7e7e | -11.2563 | -46.9348 | 2024-10-03 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 4122c84f-7299-37c4-bf6a-b8c9dff88587 | -11.2758 | -46.9098 | 2024-10-03 10:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 0e476337-c90b-3e6f-9bba-061c5c3ef757 | -11.2754 | -46.9323 | 2024-10-03 10:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 275.0 |
| c73475c5-a66c-3d1e-90e6-b005e6ac3f6f | -12.4038 | -63.0009 | 2024-10-03 10:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 54ea76ea-e977-3979-84ad-b21567ef272b | -12.4225 | -63.019 | 2024-10-03 10:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c0bb9913-8577-3210-99fe-974f5859ec28 | -12.4227 | -62.9999 | 2024-10-03 10:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 388.2 |
| e7d2aaa7-7072-3aec-b983-10a855338b02 | -12.4228 | -62.9807 | 2024-10-03 10:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 5bb9961b-139d-385f-89f2-a19aab27ff10 | -12.4416 | -62.9988 | 2024-10-03 10:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 41a0dc9e-05f8-38a6-a29d-0fff167854fc | -12.8996 | -62.4913 | 2024-10-03 10:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 12d8d7c6-e4b7-314a-90e1-df91f3b5ee7b | -12.8998 | -62.472 | 2024-10-03 10:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 8bb13abf-cf4b-3dec-98a2-d77f945cad85 | -12.8999 | -62.4527 | 2024-10-03 10:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 190.1 |
| d17e9589-4394-3c1b-bdfe-44e23ae71397 | -14.6929 | -45.4432 | 2024-10-03 10:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8893c1f8-26c4-36f3-b022-3d99f77e619c | -16.6496 | -57.3558 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.8 |
| bf2311c4-277c-3511-a682-d695c67397cb | -16.5928 | -57.2397 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 7437941a-8291-38ba-a45d-359ae4a05bd8 | -16.6297 | -57.3785 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| a71b642c-7b9a-36ff-afe3-f1191dad12bd | -16.63 | -57.358 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.7 |
| c339dfb0-789d-3d0d-a057-e5b1aaf73b8f | -16.6492 | -57.3763 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.0 |
| 186d5752-2c0a-390d-8c7f-d731c6d72122 | -16.6698 | -57.3126 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 287.1 |
| c7bd6905-96b5-3c6c-b21f-0723b2db15b6 | -16.6701 | -57.2922 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 552f1b7d-071a-3688-9c04-256d57d0f2ac | -16.6893 | -57.3104 | 2024-10-03 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 19c9934d-4ae7-30a3-8b3b-3e9255d03ea5 | -16.7455 | -57.4674 | 2024-10-03 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| c62fa8a6-eb36-3341-856a-509de042a748 | -16.765 | -57.4652 | 2024-10-03 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 5ba8c317-3e04-3b4f-bc2b-2931a48676d9 | -16.7654 | -57.4447 | 2024-10-03 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| f4048e1b-0f28-3e40-b6a9-371b21cfd84d | -17.0303 | -56.7781 | 2024-10-03 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| 6cb39a54-c69e-3a3e-914b-a667fba05711 | -17.0499 | -56.7757 | 2024-10-03 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 4c76f45c-398f-3d8d-b355-2929a2657d61 | -17.0502 | -56.7551 | 2024-10-03 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 228.6 |
| e9baf702-c906-3cce-ae73-5cf5f3b91a01 | -17.0506 | -56.7344 | 2024-10-03 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| ff523d4e-61e1-3eae-9600-28976769bc25 | -17.1771 | -57.3969 | 2024-10-03 10:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 280.3 |
| 95018b87-e795-3a7c-b124-8fff3b00fb54 | -17.1774 | -57.3764 | 2024-10-03 10:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 279.8 |
| 0be72fb6-4d5d-31a8-a4b0-47f572a4b296 | -11.2563 | -46.9348 | 2024-10-03 11:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 1a00226b-fc9f-36cd-a92f-41e97a0d9d07 | -11.2758 | -46.9098 | 2024-10-03 11:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 191.8 |
| fc6bb2a4-3191-36dd-87f3-53fa16f76497 | -12.4228 | -62.9807 | 2024-10-03 11:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 81e3052c-2cb0-3eeb-b083-18872f3aead5 | -12.4227 | -62.9999 | 2024-10-03 11:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 388.9 |
| 25f65c4f-681d-36d1-9d76-27c8fb9617cc | -12.4038 | -63.0009 | 2024-10-03 11:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| d1c81755-c2cb-3389-be63-3ec7c7e8d261 | -12.8998 | -62.472 | 2024-10-03 11:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 574c65e9-1f88-39e0-bace-1b31d5129a5d | -13.1976 | -48.6489 | 2024-10-03 11:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1798f6f2-6898-3fac-96d2-a9dd87b3cd06 | -12.8999 | -62.4527 | 2024-10-03 11:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 370d2d56-fcb0-3643-9cc4-87a2f01061c5 | -16.6496 | -57.3558 | 2024-10-03 11:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 0013204d-13aa-3abc-8db0-56667ad318eb | -16.63 | -57.358 | 2024-10-03 11:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.6 |
| 50be0469-3e00-3421-a3c3-3cc047bd76b0 | -17.0309 | -56.7368 | 2024-10-03 11:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.1 |
| 7a2ed450-fb2f-3b88-ab05-b69f05974fd1 | -8.9244 | -45.6367 | 2024-10-03 11:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 96cb1969-8067-3f82-a4ef-08093fa95564 | -11.2563 | -46.9348 | 2024-10-03 11:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1402eaeb-d29f-3510-b586-f449bcc7e1f8 | -11.2758 | -46.9098 | 2024-10-03 11:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 715548cf-0021-3b98-834a-4faf0da531a4 | -12.4038 | -63.0009 | 2024-10-03 11:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| ed52cf96-27ac-343f-a257-daab3aef9f39 | -12.4227 | -62.9999 | 2024-10-03 11:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 22c9d151-10da-3601-b575-0afb9affd18a | -12.4228 | -62.9807 | 2024-10-03 11:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| aad3e764-d1bb-3116-8fb1-4fa45adf3af8 | -13.1976 | -48.6489 | 2024-10-03 11:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 94ad7395-a20f-3eb3-b15d-9a38ebc28d44 | -16.6496 | -57.3558 | 2024-10-03 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 7856e2e6-7b5b-37aa-92df-415d6a9fa186 | -8.9244 | -45.6367 | 2024-10-03 11:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 121aa5c1-0b30-367d-9e74-1c07636ca016 | -11.0345 | -46.5143 | 2024-10-03 11:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 12ee32cb-7d01-3bb5-b78e-84daaeb89e5f | -11.2563 | -46.9348 | 2024-10-03 11:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 8bb6e2e9-ed3e-365d-aeac-75e452384557 | -11.2783 | -43.388 | 2024-10-03 11:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6e7f72ce-8157-3c8d-b8b0-d3575a92b11d | -11.2567 | -46.9123 | 2024-10-03 11:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8463996c-b6fd-3ae3-87c0-16c5568e1926 | -11.2758 | -46.9098 | 2024-10-03 11:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 30bf6e59-7917-3af8-8eee-17863bdf4f1d | -12.4228 | -62.9807 | 2024-10-03 11:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 21a2c6bd-b99f-3be7-84b0-d2898c85cc74 | -12.4038 | -63.0009 | 2024-10-03 11:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 75e53d00-214a-339e-96e0-7fc099dc6b56 | -13.1976 | -48.6489 | 2024-10-03 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 816abcb3-4749-339b-a1cd-0c5bacffe8d8 | -11.0158 | -46.4942 | 2024-10-03 11:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0b5c47fc-3d5f-3655-8e8f-eb3226c2c246 | -10.9381 | -46.5942 | 2024-10-03 11:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7c514300-ecf2-3e3d-b571-d94e04f82663 | -11.0345 | -46.5143 | 2024-10-03 11:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| bba45e51-67ad-3ba0-9d59-dc0ddbeb6f64 | -11.2563 | -46.9348 | 2024-10-03 11:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 88153504-972d-3cba-8ee7-20a5aca1ed71 | -13.0594 | -51.1409 | 2024-10-03 11:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f2c61029-fa98-3275-9461-2757c1a12f42 | -8.9244 | -45.6367 | 2024-10-03 11:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d833ccd6-de3f-3e76-b488-e0e918343497 | -11.0345 | -46.5143 | 2024-10-03 11:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 8392d45b-da01-3024-bb7d-295bd71d6dc5 | -11.2563 | -46.9348 | 2024-10-03 11:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 9b27b531-f813-3ad1-9d34-9aa43674e868 | -11.2758 | -46.9098 | 2024-10-03 11:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 467f5571-af35-3d89-9d82-32a9e5641afb | -13.0021 | -44.7123 | 2024-10-03 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 78156ebe-06ba-3645-8239-a5321d980d9c | -13.0017 | -44.7357 | 2024-10-03 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 6792c76e-e374-37dc-9563-0a4997248205 | -13.0402 | -51.1432 | 2024-10-03 11:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4c36f297-32a7-34ab-afd1-3b2a5af11e35 | -13.0594 | -51.1409 | 2024-10-03 11:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e3f3202c-f8e5-3303-87ed-df1e36c057af | -13.1805 | -45.4489 | 2024-10-03 11:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 68f00692-31f7-3fe6-ad3b-f3f9f08047b5 | -8.9244 | -45.6367 | 2024-10-03 11:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 46a813a7-a5f0-34b5-a827-c51e9ce38c33 | -10.7165 | -46.1716 | 2024-10-03 11:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |


[Clique aqui para ver as próximas entradas](README210.md)
