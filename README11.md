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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32c8e139-9580-3bbf-a912-6481560adba4 | 1.0901 | -59.431198 | 2024-10-31 01:28:51 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0dc18ec-3f69-305e-bb4e-0b5b8cbeb666 | 3.245 | -60.4268 | 2024-10-31 01:29:30 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14746a8b-0295-35f4-9db6-84f6c2d1a51d | 3.2434 | -60.433601 | 2024-10-31 01:29:30 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 31572a50-b5ff-3528-8269-3964eea3a30f | 3.2419 | -60.440399 | 2024-10-31 01:29:30 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 84b549f3-8c79-39f4-a499-6f44eb3a0c0d | 3.143 | -64.2117 | 2024-10-31 01:29:42 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0484e96a-04d6-3fd2-bf43-e57ceafe9019 | -1.9684 | -47.9552 | 2024-10-31 01:35:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 58346f77-7edf-3ae9-95d6-20f3e83fa487 | -2.1718 | -47.9506 | 2024-10-31 01:35:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3bd1a397-53d6-30e5-a800-513044294d9d | -5.0464 | -45.1768 | 2024-10-31 01:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 3a20ca44-db72-303c-8a43-548ecadeb56b | -5.0466 | -45.1542 | 2024-10-31 01:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 15b7b865-819b-3968-86d8-19d5bb37da0d | -6.1229 | -43.9578 | 2024-10-31 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0b086687-6ddf-3483-b6c5-ca4b85b79ea1 | -6.1416 | -43.9563 | 2024-10-31 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 912b7079-2ec7-3973-b2c9-e796bade0677 | -10.0118 | -64.8023 | 2024-10-31 01:36:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7b56c133-1271-311e-8f9e-373d436754fd | -12.4433 | -43.7242 | 2024-10-31 01:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| bdc90857-c32d-38e4-9e3a-9650a143626e | -19.5087 | -56.5779 | 2024-10-31 01:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 5ac0333a-93a0-3d0b-a186-207310a8dcf4 | -0.7552 | -62.8933 | 2024-10-31 01:45:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 38cacfea-6f2d-33fe-a1c6-39d3d07254f5 | -0.7734 | -62.8932 | 2024-10-31 01:45:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| b7a2b2c7-ad6e-322d-a626-00ffa482ebf6 | -1.9684 | -47.9552 | 2024-10-31 01:45:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f33e6612-18d2-3f80-b5a9-293d1b48f327 | -2.1718 | -47.9506 | 2024-10-31 01:45:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e78a2a32-476e-3eba-b004-e36759bf1721 | -2.5216 | -48.4591 | 2024-10-31 01:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| e863c199-0650-3483-8b88-24fd6b1481ff | -2.5215 | -48.4806 | 2024-10-31 01:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 17e980c6-b26f-33b0-ae09-3a5c0396c8fc | -4.2749 | -43.4357 | 2024-10-31 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a4642dc6-7875-3b2c-85b3-75074f1cd34e | -5.0464 | -45.1768 | 2024-10-31 01:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e19e4835-a17f-3574-b79d-c4b48ff5d879 | -5.0466 | -45.1542 | 2024-10-31 01:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4e12fe45-927c-3dcb-8320-f667475c386b | -6.1229 | -43.9578 | 2024-10-31 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 50e7e669-375f-306f-8a3a-1780c25a3c3c | -6.1416 | -43.9563 | 2024-10-31 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| bfa01d40-302b-31f4-a534-e3d513bf4abd | -10.0118 | -64.8023 | 2024-10-31 01:46:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3ff70cce-05a5-3469-a45c-d7d1916ad57a | -12.424 | -43.7274 | 2024-10-31 01:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b72abc39-05bc-3efe-9db5-18241c1b3477 | -12.4433 | -43.7242 | 2024-10-31 01:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 7c23d1f3-791b-3eb8-9d2a-04b2ccc4dafa | -2.5031 | -48.4596 | 2024-10-31 01:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7974ed40-ae7a-33e6-bac6-c061256eb8f4 | -2.5215 | -48.4806 | 2024-10-31 01:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| eb5ad5f6-e878-3c4a-8b91-ac4f33beebd9 | -2.5216 | -48.4591 | 2024-10-31 01:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 163ed697-0398-3267-b413-7cc7a1f97a73 | -4.2749 | -43.4357 | 2024-10-31 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2f5c6903-3ff8-3e2e-8cef-b7d4d343792c | -5.0464 | -45.1768 | 2024-10-31 01:55:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f91d855e-4cb3-3318-bf36-f1f6422e8950 | -5.0466 | -45.1542 | 2024-10-31 01:55:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 075ef6e9-d4b6-3b1c-9bf2-290a17d2eee7 | -9.8562 | -36.1382 | 2024-10-31 01:56:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 113.0 |
| 5926b98b-05d6-3030-85ac-4692081bc3f7 | -9.8567 | -36.1111 | 2024-10-31 01:56:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 337.7 |
| 1d9fa240-d21f-3554-a8fd-40bef010aa76 | -9.876 | -36.1077 | 2024-10-31 01:56:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 91bc3a81-a7d1-3681-a973-af1d1cc179ea | -10.0118 | -64.8023 | 2024-10-31 01:56:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 93461871-92d2-3a52-947f-02d877da4094 | -12.4433 | -43.7242 | 2024-10-31 01:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 511e397b-49bc-38ee-9c95-0d7606d6d315 | -12.424 | -43.7274 | 2024-10-31 01:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0683b547-0073-3e02-ba17-c7993057dfdd | -0.7734 | -62.8932 | 2024-10-31 02:05:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6cbe5725-28e1-30fd-a6a8-dbee577b29cd | -1.8475 | -52.1236 | 2024-10-31 02:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3adb1fba-84b2-32ee-85d1-5f6ef191f13c | -1.9684 | -47.9552 | 2024-10-31 02:05:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f41180dd-b587-36ba-9fa0-eb90373fae02 | -2.5215 | -48.4806 | 2024-10-31 02:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 1f6bd5ad-8385-3f13-b509-4095d5bc868e | -2.5216 | -48.4591 | 2024-10-31 02:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| f3b4dc99-80bd-3a86-9109-e3504e906f1a | -4.2749 | -43.4357 | 2024-10-31 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 687104d7-d3d1-3d52-9810-cc948677697b | -5.0464 | -45.1768 | 2024-10-31 02:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 13d8bc91-7ce7-3346-a9e2-a61fcc8fdd74 | -5.0466 | -45.1542 | 2024-10-31 02:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| af95bccd-4491-3605-8e42-b06e85fed13d | -6.1416 | -43.9563 | 2024-10-31 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d06d0cf2-f4d0-3daf-a1be-e8b603fd0f32 | -10.0118 | -64.8023 | 2024-10-31 02:06:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| fe1e9880-7ebd-38ee-a794-2d7291939fb6 | -12.424 | -43.7274 | 2024-10-31 02:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8a10b577-5876-3cb1-9ccd-c5b844f4ea53 | -12.4433 | -43.7242 | 2024-10-31 02:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| cdfd4338-21ff-305f-8727-fb508517cc86 | -19.5087 | -56.5779 | 2024-10-31 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| adf3b00f-327a-37b8-98f2-6fb17244b7ff | -19.6075 | -56.685799 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e4b82a7b-87da-3074-a66a-b3e3f90dc488 | -19.617701 | -56.719898 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e38e99d7-8ca4-370a-97da-9601e8f11f26 | -19.598101 | -56.688999 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eef3a089-c87c-36f8-bcda-72a37aed5bd9 | -19.608299 | -56.723 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ea1548e-4475-3947-b389-fa4a71ead047 | -19.588699 | -56.6922 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c49cfd8f-33fa-30a7-8606-36a2568d1d73 | -19.5989 | -56.7262 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 056cd865-d195-3c27-88f5-8aa433c7e086 | -19.608999 | -56.760101 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae800519-f98b-34b5-bbe0-a9f97e834891 | -19.579201 | -56.6954 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c35f3cef-9cfe-3ca7-9602-2f7659e5ed4c | -19.589399 | -56.729401 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 671287e3-8a97-3c0c-8b82-685a377e0819 | -19.599501 | -56.763302 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 17c1071f-8076-3c66-82b6-efac6811ae70 | -19.569799 | -56.698601 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 190a40e1-1ee8-340f-826a-839740bd01fa | -19.58 | -56.7327 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0d5cb3d0-8044-32f8-be77-ac3b453dc977 | -19.590099 | -56.766602 | 2024-10-31 02:07:04 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0e9acd8-b5ce-35cf-97fb-2a010f462b96 | -19.560301 | -56.701801 | 2024-10-31 02:07:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bd2aa44-b7e9-39f2-9b99-3f12337bddd3 | -19.570499 | -56.735901 | 2024-10-31 02:07:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 43edc214-88af-35eb-bbca-d28096bba1ce | -19.580601 | -56.769798 | 2024-10-31 02:07:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9180d972-4ae6-338c-bac3-fbb06434c20c | -19.5508 | -56.705002 | 2024-10-31 02:07:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 426dc273-8579-33d7-b105-27e57ab99461 | -19.561001 | -56.739101 | 2024-10-31 02:07:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b164e09-5949-345c-b2be-963609d64c33 | -19.490499 | -56.573299 | 2024-10-31 02:07:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9238de95-59e0-3488-a86d-836b5df0c1ee | -19.522499 | -56.7146 | 2024-10-31 02:07:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c8e4a610-c932-37cf-b36d-52d4e262556f | -19.5028 | -56.683601 | 2024-10-31 02:07:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e54d75de-1bbd-34c0-8ffd-379ebd06197e | -19.5131 | -56.7178 | 2024-10-31 02:07:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72cc8627-ad1a-3ad8-b8a8-69ff3a718966 | -19.493299 | -56.686699 | 2024-10-31 02:07:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c39ca6fd-00a7-3830-b614-f2681eb84b49 | -19.503599 | -56.721001 | 2024-10-31 02:07:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cc6e74c8-cb0b-3bea-9c96-0c4e7d0fbf3d | -19.4632 | -56.620998 | 2024-10-31 02:07:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b629c247-2637-3d82-994d-3eef69cb5ccc | -19.4839 | -56.689999 | 2024-10-31 02:07:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 29c27f20-5051-3b20-a61b-e00c16f75093 | -19.617001 | -56.682598 | 2024-10-31 02:07:44 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 50243dbe-ff2d-386d-972e-a2f92b783a2a | -19.627199 | -56.716702 | 2024-10-31 02:07:44 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8ff27aba-7f22-32b0-a028-b1223a9dcd74 | -19.6185 | -56.756901 | 2024-10-31 02:07:44 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f2bdb1b7-72af-3e53-b2f0-807c1ce0c982 | -19.532 | -56.711399 | 2024-10-31 02:07:45 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ce41946-1736-391b-9c1d-57a100e45c5d | -19.5 | -56.570099 | 2024-10-31 02:07:45 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 346bf21b-4c2f-3054-9ea2-0d9260c79cee | -19.5123 | -56.680401 | 2024-10-31 02:07:46 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d9f2570d-5f36-3cd1-b110-facac84dacb6 | -19.4727 | -56.617699 | 2024-10-31 02:07:46 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5c4db55c-3d71-31b6-bb5a-5bf4f51ecc25 | -10.6821 | -64.999001 | 2024-10-31 02:10:04 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 012cec1e-ecfb-3b66-a534-83dd4094609f | -10.0014 | -64.792 | 2024-10-31 02:10:14 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b143d4d-a153-3fab-9619-50623f1f1cff | -10.005 | -64.806702 | 2024-10-31 02:10:14 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc8afea-92ea-3af6-bd8e-5e5487c5297d | -10.0939 | -68.378601 | 2024-10-31 02:10:26 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ec4a031a-32aa-34a5-93f7-9b3d967316e6 | -8.6208 | -69.717102 | 2024-10-31 02:10:55 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 13065656-f347-35b8-9a3a-f72f7a942895 | -8.6226 | -69.724998 | 2024-10-31 02:10:55 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee286d3-55fb-3f0a-9254-6320db7602d7 | -1.8475 | -52.1236 | 2024-10-31 02:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 71a1311d-cf83-3729-b5ce-6f18f56fd83e | -1.9684 | -47.9552 | 2024-10-31 02:15:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 27a58366-f7a9-3ead-8d07-e09e0014e603 | -2.1718 | -47.9506 | 2024-10-31 02:15:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5da0a3e7-a352-311f-9b93-6b19f65ff24d | -2.5215 | -48.4806 | 2024-10-31 02:15:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 7d7aaa80-d16d-3c56-b9f3-206b7fc2f6c9 | -2.5031 | -48.4596 | 2024-10-31 02:15:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d05d5483-e43f-3ba2-bb07-b7cf5e96f327 | -2.5216 | -48.4591 | 2024-10-31 02:15:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 65161eae-a193-3c9b-b0b0-d01965bccfbf | -4.6049 | -44.3161 | 2024-10-31 02:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d1f4d4de-fb15-3635-bf6c-3dd8f912a11c | -5.0466 | -45.1542 | 2024-10-31 02:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |


[Clique aqui para ver as próximas entradas](README12.md)
