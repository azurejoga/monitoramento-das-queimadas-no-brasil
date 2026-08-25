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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4174d71-b67d-3805-874b-fbd4c64b3764 | -6.82831 | -58.6595 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcdb5405-c9c7-354f-80ee-8c408dd96b58 | -11.49297 | -52.91957 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea01d7a0-c950-3980-88fc-1160e1fe502a | -7.47985 | -55.2853 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbac87e4-46af-39d5-bc31-a018963207dd | -12.75695 | -46.45351 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a5f23cf-3288-3fd1-a8ac-8b1590537249 | -6.14851 | -57.70373 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0891bd34-d730-3b78-8c1f-511ef4970d46 | -6.14135 | -57.70615 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5faaa06-9dad-3904-8cfc-bd2ceaaa7f11 | -7.21224 | -60.61563 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 117882df-ffd1-31e0-9aea-074160a0107a | -6.14202 | -59.91944 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 895cbbfa-4b15-3618-a751-9c044503937c | -6.14552 | -59.92001 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 76b0031a-98de-334f-9235-727b6e309920 | -6.99883 | -59.24931 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 823c5f2c-5096-347f-ba43-6dd170ec8522 | -9.96591 | -48.32369 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 673dde3c-0317-35a8-b1db-002e988f5197 | -6.8174 | -59.45773 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1563fa7e-afa0-3292-aea3-6a7b2be93e75 | -6.99823 | -59.2452 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 57fa9893-e18a-3382-8cf5-f7de337cf777 | -8.22441 | -55.02555 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4809098-bc2f-39d3-8233-430c6ce3191f | -6.99542 | -59.24102 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| c3b6eb29-27e3-317c-a66d-270f21f3d836 | -6.14189 | -57.7027 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| caa4e3d2-5310-3376-89d3-65ea8ffe1837 | -9.17043 | -59.61093 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e83a3d1-b3ae-3817-aa6d-1ad9d8f0a3ff | -11.97636 | -45.9064 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3752a4b5-22dc-3fa7-9bd4-c3c6d73d7359 | -10.79827 | -50.92306 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bba2ab45-c839-3f5b-8d93-08c23038a455 | -6.80106 | -59.42857 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cb1b53f-ee00-3fd4-a0d4-30716e532fad | -8.57591 | -54.84783 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3ac1fc20-e2f8-3c77-bdb0-0b94251d0f0f | -7.56771 | -61.2047 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e11333e5-1990-304e-ab96-b56bdbbb7ada | -12.75755 | -46.4479 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 63260adb-a7b0-341f-b4f6-d6c4494b1dc5 | -6.75708 | -59.65887 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d493aaaf-3fa6-3d62-b360-dc7e2fb9d9d4 | -6.97281 | -59.07771 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e45370c0-88a7-3c0b-ae51-9ce6459950b9 | -8.2256 | -54.99281 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c3a7fa-e73e-3485-bcd8-30457cb80a41 | -12.14331 | -50.60595 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4a52738-b5e8-3af7-baa1-e60c26cdad8e | -10.03349 | -46.42862 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 923a554c-10f3-3131-a0a1-6a65962714b7 | -6.84668 | -58.99139 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c0f36d-da7d-3f1d-a8ee-ad8c5e8455b0 | -10.78995 | -51.02171 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3342f8-d32c-38a5-90f3-036c652bcc24 | -8.22022 | -54.97985 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41949856-3f7a-3fcc-a6ae-924d44c24869 | -6.3507 | -55.86584 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6eeb091-c50d-3c3a-8030-b5dbb8565583 | -6.14959 | -57.69682 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2e05716-9faf-32c5-89ec-085365b6a929 | -11.99183 | -45.91957 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04309f9d-8764-368f-8d57-a68eff686c98 | -6.9937 | -59.25193 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 64b5997b-daff-350d-a04c-42a9299409a3 | -6.18656 | -57.74499 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f60c7ba-fb9d-39ca-84be-08e7a6e35eaf | -6.1495 | -57.93788 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71a42321-72ae-3f25-b6ac-e9cd0f715953 | -9.67456 | -55.10178 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a78a079b-d66a-3e62-ae0a-073056cd70cd | -7.01063 | -59.26237 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af031763-db65-3b00-912b-bbe2a924baf9 | -8.16057 | -46.69881 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfae3dde-f9de-31af-a7d8-409066783ea4 | -8.57228 | -54.87269 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4fd7d9a-f307-3802-841f-551b10a1ff6a | -6.94298 | -52.80017 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fe96baa-eae2-3b9e-8f3e-1cd58925db2e | -6.93975 | -52.79445 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b711d74-46ac-3b4d-bcdf-87d0694fbbec | -7.22886 | -60.6425 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8568e6ce-ea74-3edd-8751-29295e5c1603 | -9.70054 | -46.05798 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a35e1ae3-b6c9-36e1-ad68-7d3f5fead541 | -6.39382 | -54.97711 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26bdc6c5-c442-3eda-91ee-23fd657fdb77 | -6.94199 | -52.77895 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d62c88d-1e3e-3cc6-b1e0-35bb3656fc94 | -7.35545 | -55.66468 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4ad85a4-c0da-34f3-b595-47fe20cc3a45 | -8.22499 | -54.99691 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2783bc0b-2663-357c-a1d2-c1c5df416b64 | -6.26591 | -55.40797 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22d7e94-b3cf-3691-993c-2e9a5ebc3a5b | -6.73461 | -59.6669 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a97b092-9f06-3b30-91be-217cac9789b8 | -9.04667 | -50.80487 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 20a2b569-3a01-39ab-b490-2beadf69bc29 | -8.61847 | -54.73394 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f6b0fda-54e4-313d-a94e-39178a52d2f7 | -6.75183 | -59.66956 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e379c7f7-8875-36b0-9d5e-045bc795b532 | -6.76276 | -59.4491 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dab21584-d93e-3248-a419-af8a7ad7679d | -8.09743 | -51.67551 | 2026-08-25 05:12:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d6980d6-9555-3746-8f06-e1668f2490a9 | -11.16219 | -54.00001 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52da9606-0a09-30fa-af8d-07c476ae69df | -6.79822 | -59.60001 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73d62eb-3337-3320-b491-0a889ce199cd | -7.009 | -59.25089 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 783e490a-0bd4-3f2b-a52d-b7532f41b513 | -6.35698 | -54.78695 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a97a425-8bc6-3a3c-bd1c-5af22c1bf4a7 | -6.63382 | -58.49104 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c894ae51-fe50-3bc7-98ae-57b207a13c74 | -6.38805 | -55.91625 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff8b1419-c749-3057-b8d9-8cbf545075a4 | -8.57777 | -55.2772 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c72be2d6-f61a-3584-96be-9b0c9f174976 | -9.431 | -51.67669 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99769321-865c-32f4-ac34-5512d1bde7fe | -8.11591 | -47.47549 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff895d1-9df8-3ded-bc51-44d2774a45b1 | -6.5114 | -55.22349 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1abc6e3-2961-3b4f-91a4-ce672fd8ee55 | -6.82001 | -59.59572 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb59f8e-6474-371d-8b10-e803c6e8d816 | -7.0028 | -59.24621 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67fb1189-86a1-3fa6-aec8-e8b9bcdf7bd3 | -6.73866 | -59.66368 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 883d9c52-eb64-374b-b255-10a3d41a4857 | -11.97705 | -45.90035 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b1f3555e-dff6-3b04-958a-558c90406d31 | -10.06114 | -48.45606 | 2026-08-25 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f43a71a-384a-3186-90ac-9796484d39ff | -8.92992 | -60.71398 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a483163c-af50-39a8-813f-9d10beacad8e | -6.79224 | -59.6375 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb45441e-f9df-3715-893f-fdf45946cb2c | -12.88677 | -48.48413 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0036b687-a92d-3a24-9001-cf73e1273aac | -9.16917 | -58.33036 | 2026-08-25 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83fee8b8-b34b-346b-93c6-9903454bdc0e | -7.49202 | -55.35733 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35317d0d-1c04-3c09-8183-a5eb1fbf027b | -6.82893 | -52.49742 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 840be2c5-e801-3333-8332-3a25eeb693b1 | -11.1663 | -54.00235 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbe57946-2766-337c-9c95-0179116e9eca | -8.56993 | -63.02566 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d663fa6-62ef-3d65-b65b-c8017b774732 | -7.00059 | -59.23838 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 609cfd64-8115-3758-a43c-d20af855b45a | -6.80285 | -59.59306 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0cd46329-0475-3aad-897f-4ec7589a7b03 | -6.84414 | -52.5066 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f1909a-7e88-3b2b-bd1f-abeafe0ec670 | -7.53798 | -61.3605 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37a02a78-9992-316f-893f-a6fe962e5a0d | -12.88713 | -48.48106 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 69ce0c0e-c8bc-3a73-bb06-e5fde5ca8ac1 | -9.96408 | -48.32188 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bc0682f-9ba4-3df7-9c02-5f7822fe5538 | -7.54167 | -61.36111 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcdef94c-24bf-339e-902a-1e57d6a3557a | -6.75647 | -59.66264 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cfa8f74-1a2c-30db-933d-69f12b87e538 | -6.94049 | -52.7893 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca907b6b-367d-347e-bac2-6bb514405616 | -6.79104 | -59.64501 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07fe826f-21ae-3b30-a55f-416d750dc9a2 | -6.97224 | -59.08132 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e59012cb-4cce-31cf-9df8-682bbb5a7be9 | -8.61386 | -47.15227 | 2026-08-25 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aea02796-3592-3ff1-b9da-35d8ee594d7a | -9.9403 | -48.34536 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f9f49d-e2bd-3ff3-aa90-7dcda3719538 | -5.91905 | -61.30035 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cafebfc-efd8-33de-8544-0ed9156a9529 | -6.81658 | -59.5952 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4405037c-8ac5-32af-8f49-a4ece69be40b | -12.7406 | -46.48275 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6080b841-3935-3f49-89a1-6a4368327c04 | -8.60697 | -54.73655 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26f0d544-ecc5-31b1-95df-167ab86016e3 | -6.00431 | -57.67046 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97992f28-7ea7-36f7-8089-c0caa27b74fe | -6.83553 | -52.50911 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea921c6c-0b00-3b1a-9f45-6195f3c1a4d5 | -6.85915 | -59.41506 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c704d75-0029-36bd-b698-86fe0fdba40f | -8.61785 | -54.73816 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
