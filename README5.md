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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2544c57a-a7a5-3fd0-b3a0-bf4c6e0e39c9 | -13.054 | -56.8545 | 2025-08-06 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 248c091c-73e8-3afd-a8b8-d284ce9928cf | -13.0728 | -56.8729 | 2025-08-06 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 59ec8bc7-41cb-3d4a-8b00-6ce2cc7d2a32 | -11.4389 | -45.1385 | 2025-08-06 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| fcf31c89-de5c-3707-96b2-fcdb230d9f5a | -13.0731 | -56.8527 | 2025-08-06 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0e06734c-c1a2-3523-a75f-e15522e5cc8b | -11.4393 | -45.1154 | 2025-08-06 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3c8ebd19-b3f9-3ad9-ba25-c55a68fea601 | -8.9213 | -60.7489 | 2025-08-06 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 3afae4d1-04f3-3622-bd08-1104827f42fc | -8.9213 | -60.7489 | 2025-08-06 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 1d129dcd-35f8-3282-9e4f-6dde25ab8a56 | -11.4393 | -45.1154 | 2025-08-06 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c16a11b1-cc39-3fcd-aaeb-f473db9d92e0 | -8.9215 | -60.7297 | 2025-08-06 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7a17004c-eed1-3c6a-870f-72375639b4d7 | -11.4389 | -45.1385 | 2025-08-06 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e914cf95-e871-37f7-8188-c979d645f563 | -13.0728 | -56.8729 | 2025-08-06 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8fef330b-434b-348a-929b-579ac2912d46 | -8.9212 | -60.7681 | 2025-08-06 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8e231bd8-982b-3cf8-955a-8a72d41be986 | -13.0731 | -56.8527 | 2025-08-06 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 6789b2d2-9349-375f-a5c8-9df062290109 | -13.0731 | -56.8527 | 2025-08-06 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ef3705b3-0dab-3a1e-9170-c0766ed7630b | -8.9028 | -60.7498 | 2025-08-06 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| be8a43d5-e514-3d01-91b4-dfdd62c60ee9 | -13.0728 | -56.8729 | 2025-08-06 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 52a18fab-0be8-33f7-b190-1857ff0b87a9 | -11.4393 | -45.1154 | 2025-08-06 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 04eefb7e-2474-38de-9f19-6a256e80b2ff | -8.9213 | -60.7489 | 2025-08-06 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 51281ad2-5383-3537-96a1-e7022d4013e3 | -8.9215 | -60.7297 | 2025-08-06 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b3c50785-4803-3d1b-970e-ad910ff769f0 | -11.4389 | -45.1385 | 2025-08-06 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 72dd4bfa-e3e4-3aac-ac4b-9e0a1d1fe3b4 | -13.0731 | -56.8527 | 2025-08-06 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 59d9c27e-2ac4-3d86-87fc-e49d6811603e | -13.0538 | -56.8746 | 2025-08-06 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| c35cc5ce-0019-3aa5-885d-f10839a15c5f | -11.4389 | -45.1385 | 2025-08-06 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 50bab922-e5f1-3856-9908-c5bc25e5fe65 | -8.9213 | -60.7489 | 2025-08-06 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e7e44f03-97b4-3849-86fb-f53d1937909a | -13.0728 | -56.8729 | 2025-08-06 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 83eb4858-e56d-395c-8aaf-c5b182944041 | -2.88704 | -40.39273 | 2025-08-06 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3b9df93-66f2-3e95-bf87-3399c801b4a0 | -2.88757 | -40.38946 | 2025-08-06 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3ffb40e-758a-3afb-96c7-08022ee6df12 | -2.88665 | -40.39028 | 2025-08-06 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c69b26aa-6dd0-3d6f-a8cc-01eaeeb30413 | -8.0126 | -43.1749 | 2025-08-06 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 9e7af617-dd20-3400-8aed-9d1b37ef2428 | -13.0538 | -56.8746 | 2025-08-06 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| d831688c-96fa-3bf0-a6db-bf21b9cc4ed7 | -11.4393 | -45.1154 | 2025-08-06 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2fe46c9a-d03b-3a70-a952-acd7f386908a | -8.9213 | -60.7489 | 2025-08-06 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e667f858-2c18-336e-bf92-fb523896bc6b | -8.9215 | -60.7297 | 2025-08-06 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 44a44c5a-8c99-31bf-af9b-cba40407a9ed | -13.0731 | -56.8527 | 2025-08-06 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4c2a675e-9062-3246-8e83-3450a74912ec | -10.7676 | -60.7472 | 2025-08-06 03:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1e4984f3-530b-37a2-9316-f58d3a150f7a | -8.9028 | -60.7498 | 2025-08-06 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 78bef6e4-7a55-3df0-9718-42f72d2c8915 | -13.0728 | -56.8729 | 2025-08-06 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f5e034ee-7af4-36c6-96de-4e991487ffa4 | -11.4389 | -45.1385 | 2025-08-06 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3a8ba934-8da2-3b1e-8d60-7586b1c2b500 | -8.51673 | -43.31757 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7c7b6a10-6b83-3bec-aabd-e8140d513687 | -7.99005 | -43.15627 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c54133d-de78-304e-9041-5207cf0d533f | -6.7231 | -43.58062 | 2025-08-06 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7ce88822-731d-33f3-a858-4191526719e5 | -7.99775 | -43.24056 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4901f92c-aa92-3216-9ede-af711f85e668 | -7.90541 | -45.5323 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3930a60d-d01d-36b4-b165-750faaf0057b | -5.75404 | -45.11034 | 2025-08-06 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a9f9094-fd04-3099-9c5e-1c00a842b3d7 | -8.02068 | -43.18285 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 6cd35d08-a29b-3469-bc17-29923f30efcf | -7.38488 | -45.98526 | 2025-08-06 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 410b20ad-3d3e-3081-a654-14599db49d09 | -8.02147 | -43.17866 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| e330e227-9b89-3581-b120-59b771d00f1e | -8.00361 | -43.24156 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fd02107d-ecff-37d4-9408-5e76ce621ec1 | -8.00451 | -43.24264 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 30f8e33d-9514-381d-bdb1-0c1a74f950ca | -9.2968 | -40.24001 | 2025-08-06 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 06e57959-ebe5-35dd-b7c2-fba4e9ee3263 | -8.51563 | -44.74841 | 2025-08-06 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a37e7642-e700-3b74-909d-18a44df1f2d6 | -4.194 | -38.37107 | 2025-08-06 03:30:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ea72affc-6372-3ccb-b885-18474708016a | -9.6223 | -40.59164 | 2025-08-06 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eeb4ebd6-c1b4-3776-91d3-e8a209b1aaf0 | -8.24722 | -45.06329 | 2025-08-06 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d37c6d6d-2eb7-3b0c-9455-08e5df9c2456 | -6.72918 | -43.58184 | 2025-08-06 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a4bf6c6-8a9c-340c-9f0f-5c2edd43d1e2 | -8.00554 | -43.13722 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b5c0565-b94f-3567-aea1-6059d4e55a83 | -8.00687 | -43.22426 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e46ff0a-8f22-302a-b5f7-618fee24a0e7 | -8.0053 | -43.23829 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bf0623a8-9747-396b-9593-97407bb6032b | -6.91996 | -43.68066 | 2025-08-06 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b299441f-85fb-3c4e-8138-2b0061e7a000 | -7.63943 | -44.58428 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc47cbbe-3402-3dd0-b9db-ad652df80390 | -8.51753 | -43.31341 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 31a62f13-2945-3116-89d0-20b2a5104e55 | -8.51738 | -43.31681 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5b96359b-30f7-33a3-9434-c278eb29057f | -7.08439 | -44.36408 | 2025-08-06 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e488c88-6756-371d-8e53-bd3cbfbd17d5 | -7.63407 | -44.57755 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 130631ea-2e02-38a2-859a-52f651852ae1 | -6.98875 | -42.09695 | 2025-08-06 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0858f030-2e37-3501-9a52-357fc50a9de5 | -7.39186 | -45.98643 | 2025-08-06 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 758feb3b-02bf-31a0-adc1-11e131b4a7fb | -6.13228 | -44.43761 | 2025-08-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93c8b07f-4184-3694-8079-e12517fa73fc | -6.91914 | -43.68518 | 2025-08-06 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3a490328-fe81-33df-a477-be7be77506aa | -4.77465 | -45.33086 | 2025-08-06 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c69d10f-3b35-376b-91fa-8445a75f5780 | -8.88172 | -44.79425 | 2025-08-06 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d38ba84-3f5e-3210-aa80-27a8cdc63890 | -7.90898 | -45.52772 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8d62394-806e-37f1-a610-0d8f95a13126 | -8.00842 | -43.221 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55eb1b8e-fbbb-331b-b3ae-8198e835ffc1 | -8.24072 | -45.06202 | 2025-08-06 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49cd8a9b-15bd-3256-81d9-f2f95159b05f | -7.91457 | -45.53483 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e08357c8-d9be-37dd-b495-7626218964b2 | -8.0199 | -43.18702 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 3b092711-7e13-30db-861a-bc496c6dee83 | -7.38541 | -45.9884 | 2025-08-06 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b85ad0a-6bb4-348f-ac16-636a2b3e2089 | -7.91217 | -45.53339 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55c0524a-e68b-3d21-bc91-fdd1dd6d15f3 | -8.02115 | -43.18384 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 247880a6-b45e-3704-8320-70284829aead | -7.38995 | -44.62981 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8981d509-88a2-3b62-8b22-0e052024e246 | -7.91571 | -45.52894 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0043b0c-3a58-34e0-9e6c-64bbe5e5675a | -6.4841 | -45.55233 | 2025-08-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8033c502-d801-36ac-966d-bb2683da4646 | -7.99896 | -43.14036 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee412856-48f5-30a8-9e8f-eef3478686f3 | -8.00459 | -43.14055 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7b33e88c-2f84-3247-b044-7edbbc13a6f3 | -9.62708 | -40.5925 | 2025-08-06 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1a6076ea-03c4-328b-bf4c-394009d22417 | -6.74575 | -45.30312 | 2025-08-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1529e4d8-80bc-3836-9b54-ad026f5fdca7 | -9.29895 | -40.24353 | 2025-08-06 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 4bd8fedf-f702-3f07-a8ef-693b266f2ef6 | -7.57345 | -44.9019 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef7abb2c-dab6-3e7b-a726-9d1a4dafaa36 | -8.00764 | -43.22534 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e10a5d9-2a36-3ce6-837a-b8582b03700f | -8.24614 | -45.06896 | 2025-08-06 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2badae4-0640-35d6-aa83-d8624a9cf053 | -7.63593 | -44.5769 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7049ce17-59c8-3ce7-a28a-9a3ac7c5da26 | -8.00443 | -43.23721 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 019870d4-dcbb-3f1b-a164-b9184eeb68aa | -6.91831 | -43.68979 | 2025-08-06 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4c23fcef-9423-3113-a0cc-251ce8a789bb | -4.19168 | -38.37264 | 2025-08-06 03:30:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6f4bab2-d72a-3483-b22d-0923e4ed228d | -7.63483 | -44.58262 | 2025-08-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b90faf3-36ba-3419-916f-5fbdac413f3e | -8.02039 | -43.18803 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| f88ba1ef-2e45-3539-a3f4-30eb707bdb6c | -6.13125 | -44.44328 | 2025-08-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07ad07cf-03b0-3913-8d2b-b5c06e4c37e7 | -8.0219 | -43.17964 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| ee4f44f5-4392-30c3-96e9-bfc48310ba9c | -8.00479 | -43.14133 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7525e9b8-b90f-3708-b6cd-b9b82a023b06 | -6.98938 | -42.09335 | 2025-08-06 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a309cb7-603f-314a-98b2-27502f0c51f6 | -8.00524 | -43.2329 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README6.md)
