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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0458f65e-d9c5-3b74-8797-706b92938b32 | -11.0264 | -45.052799 | 2025-02-01 00:01:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a92d7ca8-6f69-3e43-af10-301bfad2e160 | -11.2657 | -44.490601 | 2025-02-01 00:01:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0898e173-4ed9-37e4-98b4-73e5cdae82ef | -11.2639 | -44.482399 | 2025-02-01 00:01:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 541c1e38-ebac-3923-b19f-e2a05dcd6e8f | -10.0425 | -36.253201 | 2025-02-01 00:01:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84ee6831-a1e5-3b9a-a99e-1e9b78d1bf64 | -10.1874 | -36.5117 | 2025-02-01 00:01:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 2d6a3187-82ed-3ee0-87aa-70c4c6427948 | -10.1901 | -36.522598 | 2025-02-01 00:01:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb694741-74d5-37a6-b919-8710e2693c9e | -10.0355 | -36.266899 | 2025-02-01 00:01:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1aefec8-1b58-3f8e-a1e9-b69b4a4eda89 | -13.9199 | -41.793098 | 2025-02-01 00:01:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e5536b0-b66b-3854-94fc-2c11cea89591 | -8.322 | -35.326099 | 2025-02-01 00:01:00 | METOP-B | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0caaf7c2-9c0d-3325-a28f-3817be1e79b5 | -7.386 | -42.775299 | 2025-02-01 00:01:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb63e642-5e04-3f2b-ac1a-31547e1327ab | -10.0383 | -36.278301 | 2025-02-01 00:01:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64af0bfa-ef84-3231-8751-e7924eb0ebba | -10.2751 | -36.4902 | 2025-02-01 00:01:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 805017b9-2e78-3c7e-b8e3-f51b9af53a06 | -10.0452 | -36.2645 | 2025-02-01 00:01:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea2a2a3f-3055-3b79-8b43-33173a59902d | -13.9215 | -41.800301 | 2025-02-01 00:01:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 826bd28d-8125-3cfb-9152-27eb65306bb3 | -10.0328 | -36.2556 | 2025-02-01 00:01:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a0f7791-ec08-338d-8d48-6c6fb5afcec1 | -7.3875 | -42.7822 | 2025-02-01 00:01:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59fd094b-8beb-3469-a5fb-36f48ea51204 | -10.5399 | -36.9044 | 2025-02-01 00:01:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0947ac8b-1dc9-3ca5-853f-550d81c0cd3c | -6.7905 | -35.166599 | 2025-02-01 00:01:00 | METOP-B | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94c8585a-2f27-367a-82e1-8ae508935c9a | 1.4134 | -59.9504 | 2025-02-01 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 64bca70b-eafc-3505-97e0-3f9b54452faa | 1.4134 | -59.9694 | 2025-02-01 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 364a0432-2d3b-3b0c-b795-09357a8e3d67 | 1.4134 | -59.9314 | 2025-02-01 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d0af805c-3907-3539-a387-cb12e096d56b | 1.4316 | -59.9503 | 2025-02-01 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 57c519e2-d71e-3fa8-a06b-35ac089fcfba | 1.4134 | -59.9504 | 2025-02-01 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 85cd68df-11fb-31a0-9759-c9fdedd60df8 | 1.4134 | -59.9504 | 2025-02-01 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 28fc5251-0fc7-3981-90de-7d23c509d34e | 1.4134 | -59.9694 | 2025-02-01 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 94e959ec-2bfc-3615-818d-0ca581558a5d | 1.4183 | -59.958 | 2025-02-01 00:54:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a0dfc3bb-9470-34df-b5d2-16203f4d0625 | 1.9443 | -60.3881 | 2025-02-01 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 98dec3bd-8273-3e03-93d2-9ec8ec027545 | 1.4212 | -59.945499 | 2025-02-01 00:54:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 325eef33-1cff-3f06-abb1-3628e75da823 | 1.9473 | -60.375 | 2025-02-01 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce0b3eda-6ef9-32cf-8067-0c420e03a184 | 1.4241 | -59.932999 | 2025-02-01 00:54:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 998c5493-c990-3f20-84d5-0530f0066f79 | 1.4134 | -59.9504 | 2025-02-01 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| db9511cf-66e1-3041-aa4a-9bc1cce46c70 | 1.4134 | -59.9504 | 2025-02-01 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 82b4eca1-52c1-3485-a308-4892196ce6ff | 1.4134 | -59.9314 | 2025-02-01 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 24c0ec35-2e20-3c54-995b-7a13403e4458 | 1.4134 | -59.9694 | 2025-02-01 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2aa7b143-4517-3fd5-abb8-c0e8e5b6710c | 1.4134 | -59.9504 | 2025-02-01 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| dbd52fc7-d58e-3ce8-8295-d09a341431a6 | 1.4134 | -59.9504 | 2025-02-01 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2ab549e9-0a95-3ff4-9a87-9fbaf09e9d96 | 1.4134 | -59.9694 | 2025-02-01 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 69191d5b-df65-3d25-af60-db45d7ebb3af | 1.412 | -59.985802 | 2025-02-01 01:39:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3c03f8e9-8fc8-3a57-b134-fa3f706d3a28 | 1.4169 | -59.963699 | 2025-02-01 01:39:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ff6ea5fd-07f8-30e4-811e-ddd7c7a6d64b | 1.4134 | -59.9504 | 2025-02-01 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8a8d5610-6654-3415-9fb2-bf504996909a | 1.4316 | -59.9503 | 2025-02-01 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 2caad6af-9673-3697-9ee5-dad760693668 | 1.4134 | -59.9694 | 2025-02-01 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 5bb76060-607d-3890-b2d9-760e8e5353a3 | 1.4134 | -59.9694 | 2025-02-01 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6000207b-1b94-3b45-8ce6-6d94fdb1b651 | 1.4316 | -59.9503 | 2025-02-01 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| ef4a340f-7f48-3267-b006-aa739a5f274b | 1.4134 | -59.9504 | 2025-02-01 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e0ce5acf-fff0-3e8e-b09d-370081c3dc81 | 1.4134 | -59.9504 | 2025-02-01 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6df03d1d-788d-3815-99af-afcd4ff718ad | 1.4134 | -59.9694 | 2025-02-01 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 5b7f6016-8e0e-3eb5-a529-5277a3edc6ff | 1.4316 | -59.9503 | 2025-02-01 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 47373105-a67b-3ac7-94d8-fb04a67362df | 1.4134 | -59.9504 | 2025-02-01 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8dddf411-7a84-3d1c-9eab-8821949b238b | 1.4134 | -59.9694 | 2025-02-01 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ceb3cce5-3853-3312-8f47-d4dfe2d70c45 | 1.4316 | -59.9503 | 2025-02-01 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| db0d9b29-2a15-3a31-a39f-9af1f7372a91 | 1.4134 | -59.9504 | 2025-02-01 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f0f156fe-3cbb-3956-b3f2-b4e49d8df479 | 1.4134 | -59.9694 | 2025-02-01 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8803b1f0-a5b5-3323-9186-550bf1b01225 | 1.4316 | -59.9503 | 2025-02-01 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 73189d5d-1d76-30a7-b776-5dff51260291 | 1.4316 | -59.9503 | 2025-02-01 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 41dd47d8-1cd5-3849-a280-3c6a1e07aac5 | 1.4134 | -59.9504 | 2025-02-01 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b556143c-cedf-389d-bbc4-d98eb33f8261 | 1.4134 | -59.9504 | 2025-02-01 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 92dd2ddb-4e94-3f4d-9fcd-77d5c6f37000 | 1.4134 | -59.9694 | 2025-02-01 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 314af64e-d9cb-34f7-a1f9-c2feff860a74 | 1.4134 | -59.9504 | 2025-02-01 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5c1caa64-5fe2-39c4-aea2-2c79a93c8157 | 1.4316 | -59.9503 | 2025-02-01 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e687ea8d-0c50-3c67-a7cc-eb6c1660101f | 1.4316 | -59.9503 | 2025-02-01 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 59091faa-8e46-3ca0-a0c6-381a80379f6f | 1.4134 | -59.9504 | 2025-02-01 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c300d8bd-747d-312e-a1a9-ee5df4a085c9 | 1.4134 | -59.9694 | 2025-02-01 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c46915e6-3263-31a7-a56d-3c9b8c646299 | 1.4134 | -59.9504 | 2025-02-01 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3e008c09-940d-358e-9d28-4040bc233481 | 1.4134 | -59.9694 | 2025-02-01 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8bd35a2b-3a72-363b-84f8-e5962d944eb8 | -7.84643 | -35.19813 | 2025-02-01 03:17:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23ed87a3-93c0-3033-90c9-48d165d6ddc7 | -8.47569 | -35.33082 | 2025-02-01 03:17:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4e1e5ff4-365f-34c4-b769-d03ee97c3b14 | -7.47559 | -34.84529 | 2025-02-01 03:17:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 209de62d-7731-3572-b92a-d3f6ffcb9115 | -12.12676 | -38.16866 | 2025-02-01 03:17:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 39a07d6c-5649-3d11-be53-2a8d1d9c866b | -5.39016 | -36.81756 | 2025-02-01 03:17:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d91110d-49d1-32bb-9be5-508b3309d9fa | -7.35362 | -35.22536 | 2025-02-01 03:17:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6f808417-3169-3fee-927d-b8abb20694ce | -7.8421 | -35.19748 | 2025-02-01 03:17:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca2e6a04-7a5b-3678-aed2-6e4a497e52d2 | -6.56036 | -37.43909 | 2025-02-01 03:17:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a4ec563-0db1-3502-b66b-ff22db75890f | -4.85257 | -38.33639 | 2025-02-01 03:17:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 22830468-c1e0-3b3b-a165-a39286241b0a | -5.36653 | -36.83491 | 2025-02-01 03:17:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| eab4f9c4-3258-3945-b9dd-714b02e287bb | -7.81834 | -35.18062 | 2025-02-01 03:17:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22720984-afc7-3eb8-81fe-2d8e33611cd7 | -7.35435 | -35.22112 | 2025-02-01 03:17:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| aced1ee1-4ee2-352a-8059-c307577ee239 | -8.47139 | -35.33003 | 2025-02-01 03:17:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 51d1e354-b00d-38a0-b1cf-b88038d12500 | -5.36603 | -36.83783 | 2025-02-01 03:17:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b0be897-4877-3e3c-b6fc-8881817cf5d8 | -20.35289 | -40.85961 | 2025-02-01 03:19:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cb9e0358-164d-377c-8a08-a6c86397cfeb | -10.51763 | -36.92119 | 2025-02-01 03:19:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| de08e67b-c870-39da-a18e-05203f9823e1 | -9.00612 | -35.57136 | 2025-02-01 03:19:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d2fca764-50a4-3e82-8fb2-1ac84205767d | -9.00448 | -35.57239 | 2025-02-01 03:19:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 952fe13a-7896-3a65-a919-c7f93c61f6a3 | 1.4134 | -59.9694 | 2025-02-01 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f9057ddb-cc25-3d91-918e-146581507c5a | 1.4134 | -59.9504 | 2025-02-01 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 59705503-ea38-32e9-805a-2f8a6ffab91e | 1.4134 | -59.9694 | 2025-02-01 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 42fb73f1-b0e5-3e65-88c7-bd684a8d97d6 | 1.4134 | -59.9504 | 2025-02-01 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| bb290408-4602-3f85-b79c-b8ea406dfd1f | 1.4134 | -59.9694 | 2025-02-01 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 64b4bf76-b27e-3c61-a356-6d10bf3307d8 | 1.4134 | -59.9504 | 2025-02-01 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d36b45f2-29a4-304e-a174-dde053ffef5a | -5.83359 | -39.06787 | 2025-02-01 03:42:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96f8215f-7c8a-3d1e-a00f-eb14105b17a5 | -7.934 | -35.19154 | 2025-02-01 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a59b18c1-ee6c-3ab9-a661-b8db219fcf97 | -5.75316 | -38.15079 | 2025-02-01 03:42:00 | NPP-375D | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85667a89-3627-335f-b9e0-a6d0d296537a | -6.5606 | -37.43796 | 2025-02-01 03:42:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94ecc0bc-07e0-3fda-b37f-b8f00680fa75 | -4.85518 | -38.33332 | 2025-02-01 03:42:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e29d479-9358-35ca-82f8-f5e82d6aa81e | -7.47744 | -34.84254 | 2025-02-01 03:42:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5aaa370a-f3e7-375f-835f-2825f4427059 | -7.93345 | -35.19503 | 2025-02-01 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 01894369-930d-3ff3-b940-cbaf7776199c | -5.36598 | -40.22044 | 2025-02-01 03:42:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 97f5cfe9-4cd3-3690-b45c-7eb6b27739ac | -5.52831 | -37.10373 | 2025-02-01 03:42:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9064e5b5-ee5f-3d30-8341-4372e2441b14 | -4.85152 | -38.33274 | 2025-02-01 03:42:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 757a399e-ade7-3979-b50b-fc2640707350 | -5.84196 | -37.4829 | 2025-02-01 03:42:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
