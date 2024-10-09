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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 194f7c1b-6a3b-3b74-b0bd-6d79be1bd4bc | -17.15371 | -57.45812 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a18e2151-2c7e-3285-b613-fd1a40b8980d | -17.15263 | -57.42062 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2f2eb979-abf3-339b-bcf9-cc8e6851d2fc | -17.15261 | -57.44301 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e63ba8cd-9e91-3640-8bed-f410cbf803ce | -17.15206 | -57.44666 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| bcfdbf29-3847-363a-81be-7b61448cf3c8 | -17.15152 | -57.42789 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c0cd8166-5e94-3304-b2c0-2c7c3bb525d6 | -17.1515 | -57.4503 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 55a01ed1-2896-3242-bdda-a0b9985299d8 | -17.15096 | -57.43154 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e343ca6d-8c4b-30cf-b4e4-aa2c708f6364 | -17.1504 | -57.43518 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6f7c5cfe-454a-3af0-b195-d0530d93a978 | -17.14984 | -57.43882 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 80b15cf8-b63c-33e6-a949-fef8b7c1dd5e | -17.14928 | -57.44246 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 85de2ad4-5026-3f86-9ede-e60fa039dcac | -17.14874 | -57.4237 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7cf97b8c-e186-30b5-aa02-23878b260539 | -17.14706 | -57.45703 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 86bc8ace-4761-3980-8cae-0664c4aa6ab7 | -17.14651 | -57.43827 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| af01d426-8337-3065-94cd-ac3170ddf454 | -17.14596 | -57.44191 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 37badfb9-3b57-31ab-91c0-a6566ed83b3c | -17.1454 | -57.44555 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5900dd4-874d-3c56-8f5c-1ccb237eae38 | -17.14486 | -57.4268 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d89ff3f-69c5-3462-a264-9eeb0d6c7903 | -17.14374 | -57.43408 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5508479f-5283-3ad7-90e2-19d458caff35 | -17.14207 | -57.44501 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1bfec6ce-3e6c-3541-a7db-bebaa3c11c2e | -17.1404 | -57.45592 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9d7678b2-d0a5-303a-95b3-9fd739fed1a5 | -17.13819 | -57.44809 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e4ddefb3-1e43-3c76-8d92-73422ad2b119 | -17.13653 | -57.43662 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 78ee5186-0608-3c00-9df9-d0aab7635399 | -17.12987 | -57.43552 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bf959801-2b99-3f56-aac7-652909963ae6 | -17.12821 | -57.42404 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 756969d1-b4af-3885-9b56-4935e1def3d9 | -17.1282 | -57.44644 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a9dc4967-2e92-3dc0-bd1a-a77ef51e5ee6 | -17.12766 | -57.42768 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 72da2050-e993-3d47-a216-8709ef3f8989 | -17.12765 | -57.45008 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2c16327a-3abf-3362-aebc-cefbdf7e9900 | -17.1271 | -57.43133 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f3611625-6a23-394c-980d-bca88fcab2c6 | -17.12377 | -57.43078 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dcc1ea4e-e26c-3a14-8559-1b0b33c6c059 | -17.12376 | -57.45317 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| faaef433-938e-3dee-827f-93089de86b50 | -17.12321 | -57.43441 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aac28e95-a44b-3da2-b360-dfc11aa0fb74 | -17.1221 | -57.44169 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2ac86c84-7515-3592-b736-f6e329a1176b | -17.12044 | -57.43023 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 510fefbf-8ce2-3b40-98d0-2a2c6b34b678 | -17.11877 | -57.44115 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5d92916c-fb56-3f75-b635-4f6f141d2bc4 | -17.11766 | -57.44842 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bee89ce8-1ad1-347d-9ec6-4b3985e6b656 | -17.11711 | -57.45206 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 40c5edba-7ffb-3ddc-acd0-278bc42140bc | -17.116 | -57.43695 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 28f0a26a-d6c6-31ce-a8b1-5da4f2879ebe | -17.11545 | -57.44059 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e387a779-579c-3405-8dc1-5f069192df01 | -17.11378 | -57.45152 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6c184947-d441-3469-9faf-3937c58ed520 | -17.11267 | -57.4364 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 5d8db452-fb9e-3d2d-9208-c4567ff18ce2 | -17.11212 | -57.44004 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 342327b2-062e-33b7-8159-6b246a3afd80 | -17.11101 | -57.44732 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 6ab7145b-6b1c-3101-9a7c-716840b73a17 | -17.11045 | -57.45096 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 7db0f250-7714-3094-a11c-6ad2746878b2 | -17.10935 | -57.43585 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| ce59193b-4c68-3918-ac5a-665e1eaa13b2 | -17.10879 | -57.4395 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| a5b4ce9e-f25e-33a0-896b-3bf5a756a3ca | -17.10824 | -57.44313 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| c340e09b-8070-36dd-984d-d3a8c0efe384 | -17.10602 | -57.4353 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| af205bf5-b401-339f-ac48-10c41d915d30 | -17.13097 | -57.45063 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 67a6eadb-40aa-3c35-b5e5-b058a8fc14a8 | -17.13043 | -57.43188 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cdfa7ca7-3f12-3a72-8b85-ce227fd5dcee | -17.12543 | -57.44225 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8e4e6f0c-01c7-3fee-93f6-eb4afa290714 | -17.12432 | -57.44953 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5b7e8c78-34b2-3da2-a917-f7c9821233ae | -17.12266 | -57.43805 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 062ad618-1d16-3718-8560-80b51ed3889d | -17.12155 | -57.44533 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b81d269a-b505-3fd4-ad69-7490df6e78a5 | -17.12099 | -57.44897 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 261e8cc7-a291-3fa3-a6b3-a668bd067602 | -17.12043 | -57.45261 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e59bff93-4044-365b-b8eb-8afb1aa16bd7 | -17.11988 | -57.45625 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 8978d440-1090-3a41-93aa-782f9a6238e4 | -17.11822 | -57.44479 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| cc25881a-01d5-3f1e-b113-fdc8c6c801c0 | -17.11655 | -57.4557 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7494c546-2db1-31dd-b29a-967f3f2e5c82 | -17.11489 | -57.44423 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4f52cb97-e189-3135-b387-5b6bc523b78a | -17.11434 | -57.44788 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6f5e52f5-dc62-38fe-bc8c-fbf3f93a5f5b | -17.11323 | -57.45515 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 96ddabd1-df3f-3f21-9962-0e9214219cb7 | -17.11156 | -57.44368 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| f64befca-bbaa-37a8-b8c2-912170a04968 | -17.1099 | -57.45459 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c8f28873-8802-33d9-9694-c192b974e16d | -17.10713 | -57.45041 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 5ded3395-b846-3383-9add-a9fdbfbdfe6a | -17.10546 | -57.43894 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ee3b7f22-4ab0-37b3-b971-3e2be8088fc1 | -17.10491 | -57.44258 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| d09084d1-d00d-3e4e-9305-4b1211c90d00 | -17.10269 | -57.43475 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8579a5d7-00a6-3510-b0f8-573a78c2ada9 | -17.10213 | -57.43839 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 0bd41487-caa5-3583-ab46-e6204108da6d | -17.10158 | -57.44203 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 427d141a-f475-362b-b615-4ca9b1583d59 | -17.10102 | -57.44567 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f2d438dc-0138-38ad-810a-afebc74da92e | -17.10045 | -57.43063 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1a10b66c-8c8e-39f7-b175-cfbca963d686 | -17.09821 | -57.44518 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 180d55cb-aac0-39b0-b70c-173c7e2ec024 | -17.09765 | -57.44881 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 7cb9950a-b850-39c3-9918-86ccb2b050c8 | -17.09656 | -57.43372 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1adb12e7-1948-3f47-b9cc-c37207748a18 | -17.09544 | -57.44099 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 0f2e1948-0b4e-3697-8d14-1cb5311a5db5 | -17.09488 | -57.44463 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 26b31cb1-632e-3dbe-b393-e57cb72785c4 | -17.09323 | -57.43317 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1bbc95b4-0c00-37c3-9730-7ada58f9811c | -17.09267 | -57.43681 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dd705500-cd27-35d2-8148-47819b89a9ed | -17.09211 | -57.44044 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 10e1be4a-ca35-3374-a5b3-9aa641ebc938 | -17.09155 | -57.44408 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 89041f58-4fab-3b18-966c-d6a2248a5bf1 | -17.08935 | -57.43626 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b0d5c709-c5a7-34b4-8c4b-d18b39a53ae8 | -17.08879 | -57.43989 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| f195faae-9595-320d-9f60-002710a23d31 | -16.98452 | -57.47879 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| cf66b5fd-86f9-3f8c-8224-4631bf9e0db2 | -16.98287 | -57.46736 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 19e0e17a-dfa0-37fd-a62a-873721795554 | -16.98232 | -57.47099 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3be0114e-9d69-36f8-97f5-200da4b55be5 | -16.9812 | -57.47824 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 989cfd7a-445b-3932-a9fd-0e53aa064177 | -16.97731 | -57.48132 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2d2c5045-b8b9-3645-80bf-abf4888a0fa2 | -16.97455 | -57.47714 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a275b282-2007-373c-be5e-0f9a8b9541bc | -16.97399 | -57.48077 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 76583050-05b1-3667-a35b-22cf8aa684fa | -16.97343 | -57.48439 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cdd613aa-b831-3d41-ba4a-cb5120688a14 | -16.96236 | -57.46768 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7e81185a-bd7e-3afc-bd59-9d45a3b07fe3 | -16.95904 | -57.46714 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cceb7f27-897f-3b83-84b3-5a0309f5c521 | -16.95848 | -57.47076 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 54591907-53bc-33b1-8b60-ab029e34c154 | -16.95792 | -57.47439 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6228c6e2-9afe-34a9-af9a-71763e27a9fb | -16.95457 | -57.49615 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9b4a7d6a-8f69-38d4-9435-969673239621 | -16.9496 | -57.48416 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e545ac71-a859-3f14-b95a-14efac9bb098 | -16.94904 | -57.48779 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3480f8eb-37b4-368e-ae4c-193ca1257ebe | -16.94683 | -57.47999 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8bc66ebb-97f8-33c1-9566-71985456dd89 | -16.94628 | -57.48362 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a97ea97f-4c5d-356e-831a-d84823f74013 | -16.94351 | -57.47943 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 29ef5d21-6d85-3fea-ab5c-da8e1537d57a | -16.94295 | -57.48306 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README200.md)
