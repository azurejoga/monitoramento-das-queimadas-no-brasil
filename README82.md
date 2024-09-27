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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6352e4f4-1831-31c0-b7db-96743bf99577 | -7.55778 | -55.12086 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3102538-e022-3f66-af02-bd77c9780a83 | -7.55714 | -55.12454 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69bdcac0-4cf4-3640-a672-cadc1ac4ed59 | -7.5565 | -55.1282 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb1c7a7-7056-3183-83a7-ff3988df0383 | -7.55501 | -55.12072 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50751764-f89c-3c1b-add5-ded9de7180d0 | -7.5544 | -55.12441 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3c93711-9313-39a6-b7ce-6c9834463be5 | -7.55253 | -55.13565 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ebbe9e1-2c0d-3978-9a0c-05a49bb25686 | -7.5484 | -55.13494 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74a9a16b-d582-3b91-bf8e-4da452febc28 | -7.45019 | -54.94603 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5055ebf-e054-31fc-a534-31541a22d40b | -7.42045 | -54.94809 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd7a86c-7ccf-3b3a-8572-ee69ea52a5fb | -7.30063 | -54.91385 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fee4d2c-8542-3ad8-91fa-ad3724525b5f | -7.29662 | -55.11179 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 561191dd-3a4c-3d7d-985a-331ba9af13dc | -7.29644 | -55.31691 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 865135af-5654-3d77-a1a1-f7fdec943190 | -7.29249 | -55.11105 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18ec5df3-bc66-3900-838b-dbf5f1cb2c62 | -7.19219 | -55.03667 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1efc074d-6838-3030-9d5c-51d18640f2b6 | -7.19155 | -55.04043 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03c5493b-a434-3e84-8b64-062a25d48425 | -7.18807 | -55.03598 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b303be13-4122-3723-ac8a-cd0de983c6d3 | -7.18743 | -55.03973 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8c0fd89-3733-3b79-ab0e-776a9199bf9f | -7.18647 | -55.02038 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ac94c39-f130-30c1-857a-da6a4256e371 | -7.18584 | -55.0241 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac579aae-4058-307c-b3c9-1e9c3a6e5aea | -7.18395 | -55.03523 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b02fcd4-0c94-3113-afe1-4a3ea38d6e98 | -7.18332 | -55.03897 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 068d6de3-946d-34bf-851d-f2a110fbbe50 | -7.18236 | -55.01968 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f3b701a-fe8c-3b30-9f4a-d79ee8d3d7f5 | -7.18173 | -55.02337 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da47f93f-2840-3f57-81e2-ed88bf377c73 | -7.18048 | -55.03072 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94cae8e6-f468-357d-bca5-b4439d9b2683 | -7.17984 | -55.03446 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4db501e-4abd-3b28-810c-1e551c92abf2 | -7.1792 | -55.03823 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4733970-958a-3059-9242-9e2752d05efa | -7.17761 | -55.02267 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56a45171-150c-390d-a1d0-288dc2f44687 | -7.17635 | -55.03006 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37179ad8-2f67-3c40-8880-622cc0ab1f74 | -7.17507 | -55.03759 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c422a12b-9ebd-3960-bdd7-ef24802f1457 | -7.01871 | -55.11588 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21cccfa7-5ec2-397f-a3dd-e4cbb839c352 | -7.01693 | -55.11594 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8baba05-2745-38e5-9675-a8c649fb7b08 | -7.01088 | -55.12666 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8096c22a-5774-3274-afdb-6da75632a9b8 | -7.8758 | -55.51699 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3276ce74-046e-317b-8388-f0194e3f517f | -7.87244 | -55.53668 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd98a515-dcee-39d3-8996-5cbcb4327382 | -7.87227 | -55.51231 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2530862-24b7-30ca-a645-3a881c5a9c63 | -7.87176 | -55.54062 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 913f89c2-0f5f-31ba-8eac-3c5810384072 | -7.8716 | -55.5162 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f34e491e-e5a4-3084-a147-c4b300711af5 | -7.86755 | -55.53986 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1de9da47-e63b-3cc3-998d-d01dcf20fb46 | -7.86738 | -55.51556 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a9c9b9c-c04a-310f-ac5b-a7cd93be45e4 | -7.37532 | -55.49508 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f14d7dc1-cdce-3f16-827c-447eaeaf0c42 | -7.37465 | -55.49909 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91bacf3d-11e4-3416-a3ce-1922ea0fd006 | -7.37398 | -55.50311 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd0de304-d09e-3239-81ed-60e9fdf150ea | -7.37107 | -55.49442 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37156e23-2b2f-34e7-9d34-c377fa6193c8 | -7.36907 | -55.50637 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c31022-c3cd-3a00-914c-8579641ef96c | -7.36616 | -55.4977 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4057fe9e-f29c-3a45-813a-ccab9b2edf7b | -7.3655 | -55.50163 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8487d30e-d0f9-3d2f-a6b3-c45833b10bb4 | -8.94438 | -55.09005 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7afc2d9a-a51f-3273-bcd1-c377f8a45277 | -8.75305 | -54.98404 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2225a75-cb27-320b-aa92-59c8f2be2f20 | -8.11662 | -55.35565 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c2170a7-1567-31ad-83c3-c0b2ca21fb6e | -8.10178 | -55.39232 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b49b565-8c36-39c7-bbba-164d68780249 | -8.09827 | -55.38781 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce22594c-84c6-3df6-9220-2c112fcb3574 | -8.09762 | -55.39159 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23a405dd-8c84-3cb6-a412-1a5d20f031d3 | -8.01262 | -55.70677 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb26bcbb-fe8a-31a9-a6f6-deb9c9479e87 | -8.00983 | -55.70205 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6bc301b-463a-3886-a7bc-bda20a315b26 | -8.00905 | -55.70214 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bcf9838-0fd6-38e5-b275-c7dd3ade3122 | -7.93778 | -55.76456 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48204098-1d44-39dd-9e85-ed79212cf1a0 | -7.93705 | -55.7688 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8faab5-561f-364a-b49a-23b5d565ddd8 | -7.92992 | -55.75906 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdabbb11-d1e0-3042-a843-4254b8f17a49 | -8.11914 | -54.79898 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e636dec1-d03f-3a78-941f-48d8e64ee97b | -8.11854 | -54.80249 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a9344f-56c6-3398-9120-2d3b92ecf590 | -8.11795 | -54.80602 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d215ed9-a42f-305c-8a3b-63d6484e30b7 | -8.11735 | -54.80955 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aedc1c7-301a-3b3e-8c8f-aa4390c5600c | -8.11631 | -54.79134 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdebdc76-5436-3a7a-ad2f-4bb83ab6592a | -8.11514 | -54.7983 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de236822-cee1-37ec-a5a5-636c46a55e93 | -8.11454 | -55.07449 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87068e5f-298a-3b45-9747-01a5bcfc4be3 | -8.11418 | -55.07532 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 671320d1-a23c-358f-9645-eed5d5e3e5d5 | -8.11394 | -55.07813 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 056379a1-107e-3664-98bf-101691362185 | -8.11355 | -55.07895 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d76fc49-f90b-31e0-9030-5edc571c29f7 | -8.11273 | -55.08541 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd4e5fa0-7547-3bc7-aa6b-0203aba690f0 | -8.11229 | -55.08622 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e56d29-eec0-3a28-9734-5d984449167a | -8.11172 | -54.79417 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f23f7029-fb4c-359d-b378-4d9a7ad7175d | -8.11113 | -54.79765 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e057f664-0055-3d38-bb34-fcd61428d494 | -8.11107 | -55.0702 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bdf11dd-c02b-384f-836b-df7e55539edf | -8.11073 | -55.07104 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f414ea7-df04-32c3-8b65-0bdc5292d4f6 | -8.11046 | -55.07383 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cebd0b5d-a807-30e3-840d-37bd00d9f532 | -8.10842 | -54.86256 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbe8102e-3d68-3462-bc9d-7b2a9f5698a9 | -8.10026 | -54.96024 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8408ddd9-518c-36a9-97d8-c1ca88e8a072 | -8.95244 | -55.09138 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128a2eeb-afcc-3cb8-93b9-8652c3e45692 | -8.95183 | -55.09497 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9231356b-4dbe-36a5-9ff0-180a8efe99d2 | -8.93633 | -55.08872 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf4492f3-6647-3f27-b17c-9d87c671e0a5 | -8.79202 | -55.00592 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2367e13a-3799-3447-805d-9068ea1b3d4d | -8.78861 | -55.00177 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddedda92-b537-3d69-80df-000420e54700 | -8.78801 | -55.00525 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 236d86bf-4f9f-3c87-b9d4-5cb4bad00cd0 | -8.75245 | -54.98755 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e47a9932-ad80-36bf-a481-e2868dc98caa | -8.75186 | -54.99109 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 601a2c0c-cda0-33bc-9041-f797b93d3ec8 | -8.74902 | -54.98343 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e385b44-dc68-3740-93ce-71af63c7db54 | -8.74843 | -54.98695 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a72d0e9-eb08-3c4a-a058-f795c0ad170b | -8.52239 | -55.18616 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e6abf6a-c181-39da-ac8d-a0d7e9c403c3 | -8.51707 | -55.19283 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce94b25c-e392-3cf5-88d0-7723fc380a54 | -8.51645 | -55.19653 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8226c3fb-f204-36b4-9381-b2a72420c48c | -8.51423 | -55.18475 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f0b5af8-fe8f-3d8a-a650-8640aad44e67 | -8.51362 | -55.18843 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c190b4-070d-3b8a-8196-38fd1b77f036 | -8.50137 | -55.1864 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c6da536-473c-3ba5-8b8b-2d64005e493e | -8.50076 | -55.19002 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b413886-7c0c-31dd-8e80-0dfd014880b2 | -8.49668 | -55.18931 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b31abf6b-fab7-31a4-b3c8-08d51d9314f6 | -8.4094 | -55.06173 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b497d64-aecd-3d14-aec9-6282676436e2 | -8.52177 | -55.18986 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3e368b1-89f2-3816-8b2d-2733539d3b8f | -8.52114 | -55.19356 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0bd72b6-be51-39af-8262-5d81a91f99c2 | -8.51831 | -55.18544 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 951ff259-eb71-368e-ac9b-bcd00bbaa119 | -8.51769 | -55.18913 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README83.md)
