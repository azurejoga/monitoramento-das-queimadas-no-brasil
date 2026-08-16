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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0abba821-1349-3bc2-b72f-99b9a8efbab6 | -6.1108 | -57.7035 | 2026-08-16 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 01f41187-64ba-3ee9-9cef-08c878f9596c | -6.6194 | -59.0609 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 233342db-8faf-3a71-a3c9-75cc5edfc2df | -6.6193 | -59.0802 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 1572d9ee-e469-39c7-9204-0b533dfe7e10 | -8.9041 | -60.5577 | 2026-08-16 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9b9bf7d5-f659-3a3a-8d8d-bacb726213bd | -8.4275 | -62.676 | 2026-08-16 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8ae39bbd-6e13-3c69-ab47-abc2a253d4a8 | -6.7124 | -58.9219 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 40d801ff-2d83-399f-a29b-41278835a7d0 | -6.82 | -56.4551 | 2026-08-16 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b6062224-83c3-3171-9075-fd9d936db977 | -6.8412 | -58.9746 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e4d198e1-dc39-311b-b77e-8fc7b235a234 | -6.6193 | -59.0802 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3966117a-3646-3ca7-97cf-d4027e67b03f | -6.6378 | -59.0602 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fc76d916-cdc5-3b06-b2ad-1aeb068fe6f8 | -13.6864 | -46.2395 | 2026-08-16 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 27f6fff1-4154-3343-9da2-c2841995cb7c | -6.8597 | -58.9738 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7c1f5207-2e35-3777-8bd9-c83e4b03fa88 | -6.1108 | -57.7035 | 2026-08-16 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| df6caf19-6eb2-332f-8280-3bd55152b3d4 | -6.6937 | -58.9613 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 786ac665-b412-3273-a954-84438d3d04c7 | -6.6938 | -58.942 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ec366d63-3339-39a4-891f-d407d4d8c78f | -14.3919 | -51.9081 | 2026-08-16 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5651a6f4-fdc2-3474-940b-59bb181a5f75 | -6.7123 | -58.9412 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 05b0a0a7-05cd-3e92-91a9-df4039437a1e | -6.6194 | -59.0609 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| c960a05a-5177-34a2-a293-a250a4fd8436 | -6.6014 | -58.9844 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4cb9333c-e108-3189-9349-a312eeb84c95 | -6.6377 | -59.0795 | 2026-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c77c9a89-bfbf-3916-bced-10d020e39180 | -8.9041 | -60.5577 | 2026-08-16 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 88ee5f23-a3cb-3764-b7cd-1102a39127fb | -6.8385 | -56.4542 | 2026-08-16 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 17bab155-da72-316b-8468-1e57bc72aeea | -6.8387 | -56.4344 | 2026-08-16 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9c3f9948-081b-338a-9de2-8251c37ba44b | -6.0923 | -57.7238 | 2026-08-16 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 03ab1eec-cf32-36be-98bb-09dde61a69c3 | -6.1107 | -57.723 | 2026-08-16 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 7565bc5a-56ed-333e-808d-77683f2c9743 | -6.8387 | -56.4344 | 2026-08-16 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1299d8f2-a230-3e62-9ae9-3ba2b00b49de | -6.8385 | -56.4542 | 2026-08-16 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4ffadc5f-fa3d-39a6-a78a-bb237b1f5dfa | -14.3923 | -51.8867 | 2026-08-16 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 400a8c4f-7f0d-3290-b9c7-94b40814b167 | -6.6938 | -58.942 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3f1163c2-8387-30fd-a2c1-1e81f7a7b12d | -6.6193 | -59.0802 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 6946b120-c3d9-30b5-94fc-398b4b475cc2 | -6.2192 | -47.7419 | 2026-08-16 02:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6b4729ad-6537-34db-94a1-f577bc64989d | -6.82 | -56.4551 | 2026-08-16 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8fd25f63-2340-3d08-8ab5-c071917bf995 | -6.6194 | -59.0609 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 354d13b0-28c3-38f5-9c24-a133f74b8aee | -6.0923 | -57.7238 | 2026-08-16 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2667f1fe-7775-35ea-9a48-93664effd4f7 | -6.6378 | -59.0602 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5e63c914-3043-3e5e-b951-bdacaa06eefc | -6.8597 | -58.9738 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e90bdaa6-3ff3-36b8-91d1-6188a9861a3a | -8.4275 | -62.676 | 2026-08-16 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a0678134-599b-3877-80f1-c2f864d28e0a | -6.6014 | -58.9844 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 239a749e-1d1d-3ac0-9c5b-58576754464b | -6.1107 | -57.723 | 2026-08-16 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b665385f-9904-39c4-bfd7-d7efdf5e843b | -6.6377 | -59.0795 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 91d3016c-3c18-3f71-9228-18dd9dea4f90 | -6.7123 | -58.9412 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| e9cec23b-48b9-3d81-a17c-84ccd7827205 | -6.7122 | -58.9606 | 2026-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ca2047c6-7474-3c99-80a4-488b9d33efa8 | -6.1108 | -57.7035 | 2026-08-16 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 53359ce9-5804-3299-850f-baba3aedd367 | -8.9041 | -60.5577 | 2026-08-16 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 57e36b4a-bd97-3e4f-a01f-2541917dc832 | -14.3919 | -51.9081 | 2026-08-16 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4d79d73c-02af-3aa7-9135-b9025a565b5a | -6.6937 | -58.9613 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 11eebbe1-93ee-36ca-bc73-2aef9ffbd9c9 | -6.7124 | -58.9219 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 835f79f8-8624-384e-a2ae-07d52197ea97 | -6.8597 | -58.9738 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| be1e6cc6-48d6-3faa-82d2-52e0ab38f16d | -6.8387 | -56.4344 | 2026-08-16 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b1a37944-c61c-3069-b532-5308f16e564f | -6.2192 | -47.7419 | 2026-08-16 02:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| bf7a3f85-c3d9-33e2-b8d9-c02f0b2819a9 | -8.9041 | -60.5577 | 2026-08-16 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f812e181-7550-3fba-a722-7558d1e16c3d | -6.1106 | -57.7425 | 2026-08-16 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| da2617f9-9f36-3824-b397-5954652af8f1 | -6.82 | -56.4551 | 2026-08-16 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4ab96872-6ac3-3c2e-8186-99dff8e800bf | -6.7123 | -58.9412 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0d0e9409-c9bb-3ab7-b65b-ed36f2741e21 | -6.6193 | -59.0802 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a4b8505a-3b1e-3907-b376-a6b4f95fbc29 | -6.6378 | -59.0602 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9e508546-a526-3644-aaaa-f8b08b5d2bfb | -6.1108 | -57.7035 | 2026-08-16 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a2bd7257-50c8-33de-95df-646ae97c2316 | -8.446 | -62.6752 | 2026-08-16 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7405c87b-ce28-368e-abf3-f7cdb4346891 | -6.6377 | -59.0795 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 08e15771-a911-316b-8327-4ff2eac57ef9 | -8.4275 | -62.676 | 2026-08-16 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 78bdaaeb-4d20-3c16-a914-0f8d2b86fe7e | -6.6194 | -59.0609 | 2026-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a2ea6989-f08c-3731-86fd-ba0ebd9a1c6f | -6.1107 | -57.723 | 2026-08-16 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| c197f3b5-130c-3f34-b71b-fd12650949a1 | -6.8385 | -56.4542 | 2026-08-16 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2327339e-ab30-36ea-90e9-816960b0daa5 | -12.7017 | -48.4753 | 2026-08-16 02:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1eb26906-8fcf-33fc-9ed5-62496ab92f5d | -6.6193 | -59.0802 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1f509e85-322c-3d4f-8c78-0088dde1678e | -6.8385 | -56.4542 | 2026-08-16 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8fa6db7c-4e91-3f47-829a-da7e9849d4e9 | -14.3923 | -51.8867 | 2026-08-16 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| b1cbc8fa-89fe-37b1-a7a7-01bd0ef9f3c8 | -6.2192 | -47.7419 | 2026-08-16 03:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a644021c-eec6-3aac-a704-7164cfdbaa79 | -6.8387 | -56.4344 | 2026-08-16 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b3bc6162-0d27-3cfa-8763-3e95ade7e74c | -6.1107 | -57.723 | 2026-08-16 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 487eeb87-b375-37de-919c-77f941bf2d08 | -6.6194 | -59.0609 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 690d929d-aaa1-37ba-bbb9-a86f9fd2d7e0 | -6.6378 | -59.0602 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 597a7d2c-d60e-3043-8533-ad267ed9c096 | -6.7122 | -58.9606 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5fd24e29-2460-3058-afff-12f414b5b2c8 | -6.8597 | -58.9738 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ef0f6a0a-9b80-3c9f-86c0-07b5c29abe72 | -6.6014 | -58.9844 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 37316f4d-12f5-387b-bcc4-b4cf42fd30f7 | -6.1108 | -57.7035 | 2026-08-16 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e34a21f7-65e2-3e24-a798-72131dc9da72 | -6.7123 | -58.9412 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| d28b0197-9d5b-397d-b3f4-eddc209e01be | -6.6377 | -59.0795 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 0378d920-f211-361d-bf30-85f406415253 | -6.82 | -56.4551 | 2026-08-16 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8371ffac-74bd-359d-9e2e-edaed85ff9ce | -8.4275 | -62.676 | 2026-08-16 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d9058386-d1a9-3231-813e-f3ff230ad6a8 | -8.9041 | -60.5577 | 2026-08-16 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6e61f62c-fe99-3bb6-a916-7cc145d395f5 | -6.6938 | -58.942 | 2026-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0e61abeb-2814-3382-933c-87daaa889548 | -6.8385 | -56.4542 | 2026-08-16 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fe0f4fc8-9224-3319-a10e-4901a6d6ec9a | -6.8597 | -58.9738 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4965f408-7ee9-35ce-a6a0-7c802e3e9cfc | -6.6378 | -59.0602 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b1eb5b2a-4f96-3dc6-a979-5de815895b37 | -8.9601 | -60.5165 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| df9926f5-1284-33fc-8c80-76cbf0360769 | -8.9041 | -60.5577 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b3853f41-5164-3149-92c8-efdfddf7a0ef | -6.8387 | -56.4344 | 2026-08-16 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cd4f245b-26cf-3928-9118-ea0e821404bc | -8.9415 | -60.5174 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a350e021-0fcc-32a1-ba4d-87314bda4f59 | -6.6193 | -59.0802 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ef57e70d-f71d-3f48-8cab-5800a38f6360 | -6.0923 | -57.7238 | 2026-08-16 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 94396faf-d808-38e9-bfdb-b127545178a8 | -6.82 | -56.4551 | 2026-08-16 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 21164bc2-d216-3725-b691-00303eed9257 | -6.6377 | -59.0795 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3718a904-54c8-33a5-b41e-546500cddd2b | -6.1107 | -57.723 | 2026-08-16 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0596ccad-b7cd-3432-b465-1b510343482c | -8.9785 | -60.5349 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 87b24179-1e4f-387b-a8dd-7626aeaded93 | -8.4275 | -62.676 | 2026-08-16 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.1 |
| ebd0f3bb-dc7f-34df-8362-7094deb6702a | -8.9788 | -60.4964 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a7f2a387-bdf5-31b9-af04-409014083b9b | -8.96 | -60.5358 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 21ebb50e-3085-3bc0-b5cc-45fb8e68759d | -6.1108 | -57.7035 | 2026-08-16 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fc5ff84f-ac92-3ba6-8e1b-b104782ce706 | -6.0924 | -57.7043 | 2026-08-16 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |


[Clique aqui para ver as próximas entradas](README7.md)
