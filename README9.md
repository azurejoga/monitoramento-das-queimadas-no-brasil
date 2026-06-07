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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b2bde30-7f76-3f1a-b490-7254e6a8faf7 | -14.287 | -57.5434 | 2026-06-07 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 18aeaaa2-4372-3514-9a8a-84cc90a80969 | -14.2873 | -57.5233 | 2026-06-07 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 85f432a4-82d2-39a3-94ec-dca0ceb5c8fb | -10.8573 | -53.7425 | 2026-06-07 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 01afc60f-7b47-3b7a-9945-d22d53219bc9 | -21.3229 | -49.1758 | 2026-06-07 13:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.8 |
| 125f5da6-3fd3-38ab-aded-f0d4b2e0a980 | -21.3223 | -49.199 | 2026-06-07 13:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.2 |
| b08b26a0-2045-34c0-8747-7df6a498b068 | -14.3062 | -57.5416 | 2026-06-07 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| ebe3b69a-b20c-34c9-826f-0d1a1fcdb5f5 | -10.8236 | -60.7633 | 2026-06-07 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 6187dfe7-1696-38c4-9d2f-5e7cbbde35b4 | -14.2873 | -57.5233 | 2026-06-07 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3780a68b-5975-3353-909f-a6cecdc4a55e | -10.8573 | -53.7425 | 2026-06-07 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 152182eb-fba8-34f2-a5fc-c222356e4dca | -14.287 | -57.5434 | 2026-06-07 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 186c9b8a-bbb7-378a-a355-d2de1f49f093 | -14.2873 | -57.5233 | 2026-06-07 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b1c3abf2-738c-3c30-b8c9-bf7feaad8e30 | -14.3062 | -57.5416 | 2026-06-07 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 662ac83d-9101-3615-a62f-6ae1425c9430 | -14.287 | -57.5434 | 2026-06-07 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 8a517517-0da7-35e7-83b0-05730c3dbb32 | -10.8573 | -53.7425 | 2026-06-07 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f1bca9fa-1b6c-3b7f-8e06-3b66f8d5c07b | -14.287 | -57.5434 | 2026-06-07 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 71f1bd96-76c4-3a21-a343-62ffef861cd8 | -10.8573 | -53.7425 | 2026-06-07 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3363bb1c-8f3c-31d7-b115-aff3f5a024fd | -14.2873 | -57.5233 | 2026-06-07 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 4877bdf9-f040-36ba-b8cf-acd869ce07f8 | -14.2873 | -57.5233 | 2026-06-07 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cb97c9f0-9b36-3ce6-8715-d6ce6d3c028e | -14.3062 | -57.5416 | 2026-06-07 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 00f03444-8c19-33f6-ad8d-9a4c27d5a837 | -10.1196 | -57.7633 | 2026-06-07 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 207a6162-e327-3e48-bab4-9699f2693eea | -10.8236 | -60.7633 | 2026-06-07 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9c24340d-ddc1-31b2-93ea-478120151503 | -14.287 | -57.5434 | 2026-06-07 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 4a7ec163-206f-3e3b-840a-62cda1ef23db | -10.0956 | -47.0772 | 2026-06-07 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0671773a-09ad-37be-b53d-400b2612ee27 | -7.871 | -43.9371 | 2026-06-07 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fc5e56b9-112c-3383-a86f-5a1795360c28 | -10.8573 | -53.7425 | 2026-06-07 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4851ac83-faea-35e7-bca1-2ad108ea495c | -14.3062 | -57.5416 | 2026-06-07 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| f14a9fa0-f35e-3838-9736-52b4515986f6 | -14.6366 | -58.7133 | 2026-06-07 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 23273277-fb5d-379a-8990-6025fa799164 | -10.8573 | -53.7425 | 2026-06-07 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 57ebd04c-a5f9-3c53-9b52-a4fc35233f0d | -14.2873 | -57.5233 | 2026-06-07 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d4c065b7-5264-3f52-a4fe-9acde48804c1 | -14.287 | -57.5434 | 2026-06-07 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 2d9aa57f-5622-3d11-a7a3-8db76f1953a3 | -10.1196 | -57.7633 | 2026-06-07 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| aa954499-8829-3fb3-a845-78a7b404e04c | -14.287 | -57.5434 | 2026-06-07 14:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| efefd27f-a3b6-3ebc-b9d4-18abac8795f2 | -7.871 | -43.9371 | 2026-06-07 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 68b186b0-20a4-3c3b-a3bf-94cae6f30147 | -10.1196 | -57.7633 | 2026-06-07 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 39d35224-ddc0-3089-b022-4ca20cb00d57 | -14.2873 | -57.5233 | 2026-06-07 14:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8262474e-6567-3ffb-af1e-d92916d9eab9 | -10.8573 | -53.7425 | 2026-06-07 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f12d97fb-a17f-3a79-906f-38fe911d37d1 | -10.8573 | -53.7425 | 2026-06-07 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 886c094d-1145-3d63-96e0-403b1cc53e72 | -14.287 | -57.5434 | 2026-06-07 14:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ae06f97c-d98f-3aa1-a656-c5112bf02aa5 | -14.2873 | -57.5233 | 2026-06-07 14:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| fd3d2f4c-2844-30bf-9145-aced167bb1dc | -10.1196 | -57.7633 | 2026-06-07 14:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 7f1691b5-593f-3d9c-9b24-a58503beff38 | -7.871 | -43.9371 | 2026-06-07 14:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| c43b0653-98f2-3e48-9b87-f9072c1416b5 | -10.0956 | -47.0772 | 2026-06-07 15:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9f07cab2-bc98-31fc-989e-b566e7abd606 | -7.871 | -43.9371 | 2026-06-07 15:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| b0aa2fd6-82b8-3b1c-b258-78e0cb89604a | -14.2873 | -57.5233 | 2026-06-07 15:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1993d107-66e4-3d2b-9015-335c9a0bad2e | -10.1196 | -57.7633 | 2026-06-07 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 8a106cf0-e4c3-3507-b3f0-3506e4eb420d | -14.287 | -57.5434 | 2026-06-07 15:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 206fe76e-621b-3440-a2e4-49672763322b | -10.1196 | -57.7633 | 2026-06-07 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f147e1eb-3aec-389b-9a3a-5bf6029790a6 | -7.871 | -43.9371 | 2026-06-07 15:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 4beab6ca-bf96-3219-ab4b-3f482930a566 | -14.287 | -57.5434 | 2026-06-07 15:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 0ed04d22-ac78-314b-924d-b08d94a6bcb8 | -14.2873 | -57.5233 | 2026-06-07 15:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ae93d18f-036a-3da2-8a3e-9ca3de79623a | -14.5392 | -58.8219 | 2026-06-07 15:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 960cd87d-c9e5-3fb7-b3c9-bf9dd480f3bb | -10.8573 | -53.7425 | 2026-06-07 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b7580915-c1f7-33df-b4af-30bed0f1e099 | -7.871 | -43.9371 | 2026-06-07 15:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| beabc66a-bf91-3a44-b73a-76b6eaac3669 | -8.0339 | -46.0436 | 2026-06-07 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8f98207b-7a60-3c06-8127-e3bb076b34c5 | -10.8573 | -53.7425 | 2026-06-07 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4f07694c-d1a0-32a1-87cf-ae04a516e5fe | -10.1196 | -57.7633 | 2026-06-07 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 41e26d71-2856-30a7-b2ed-347916bcade2 | -14.287 | -57.5434 | 2026-06-07 15:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dd1f024d-4e5d-31e8-9ce8-3f491a17686f | -10.1196 | -57.7633 | 2026-06-07 15:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 398f8002-995c-31e7-96e3-c824379f4661 | -14.287 | -57.5434 | 2026-06-07 15:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 59493f89-9be3-3c98-98d4-1517799f2505 | -14.5392 | -58.8219 | 2026-06-07 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8ee431a9-bdc4-3671-8ff3-7203a3c7228d | -21.9807 | -57.6063 | 2026-06-07 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 61.3 |
| adb8377c-1bd9-36c5-a2a5-72f53ace21a1 | -14.2754 | -58.4467 | 2026-06-07 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a8dadc2b-01ea-38ca-af56-cd5a3818c3cb | -14.287 | -57.5434 | 2026-06-07 15:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |


