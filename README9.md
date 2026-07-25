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
| 93bc2f8f-19ef-30d6-965b-800280b7e678 | -10.02368 | -59.34432 | 2026-07-25 12:42:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a866666-d09e-3a37-9655-927ae7000c21 | -9.47851 | -57.32203 | 2026-07-25 12:42:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6d79dbe4-d239-3333-8ae4-aabf30436664 | -9.5274 | -47.141 | 2026-07-25 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 49cfaf72-d661-3d67-bab2-f36183539fc4 | -10.6755 | -46.3574 | 2026-07-25 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b601a6a8-9978-3054-bb21-9a8d44dadabc | -9.5277 | -47.1187 | 2026-07-25 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 89b9cacf-3dc1-377d-9dab-abb60e14df9f | -10.6759 | -46.3348 | 2026-07-25 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ec8ee62a-e6d1-3fbd-aecd-7a521ba7d3b3 | -11.807 | -47.0858 | 2026-07-25 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 85d94d6d-74e7-3a56-a9d4-084cf8817fac | -10.6755 | -46.3574 | 2026-07-25 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 32877325-4725-32b1-85e4-98dce268dbed | -11.807 | -47.0858 | 2026-07-25 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2dee424c-152e-39c8-b4aa-a4795cc3d83b | -9.5277 | -47.1187 | 2026-07-25 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 144f70d3-b476-38b7-b953-06e0cf02c76e | -10.6755 | -46.3574 | 2026-07-25 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 9da34e74-5a8b-35ec-82e7-342f7ab5a9b9 | -9.5277 | -47.1187 | 2026-07-25 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| f721203f-ba62-34c2-bf24-9b2571a12687 | -10.6759 | -46.3348 | 2026-07-25 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| de35e90d-a786-3c2e-bbe7-2ae34af89112 | -10.271 | -46.7441 | 2026-07-25 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8394165c-cab6-358d-81ce-7e65d8188b6b | -11.807 | -47.0858 | 2026-07-25 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 248a3600-4077-33b2-b76d-cc3f094a5300 | -10.6755 | -46.3574 | 2026-07-25 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 0a91beb4-a06b-3fb7-bfd9-482320317626 | -10.6759 | -46.3348 | 2026-07-25 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 06715c5d-5d3c-3411-a6af-2ad0c73f73f3 | -9.5277 | -47.1187 | 2026-07-25 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 20b7608e-471b-3e37-842f-272df62c4ec0 | -9.5277 | -47.1187 | 2026-07-25 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| cd7a403f-0e20-3203-961d-2572ccafb566 | -10.6755 | -46.3574 | 2026-07-25 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cb93154c-ea8d-3ab6-888f-de4065a090f8 | -9.5277 | -47.1187 | 2026-07-25 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 1ef1ba74-2c45-331a-a455-9c0f34d8d841 | -10.6755 | -46.3574 | 2026-07-25 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| a1ef41d6-ec5d-355e-91a3-ddfd8e3ce145 | -9.5277 | -47.1187 | 2026-07-25 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 2eace9c3-5ba5-3896-b614-90386b8ed446 | -10.6759 | -46.3348 | 2026-07-25 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 68ab9779-75f9-3284-a007-7f1e95b3dd88 | -10.6755 | -46.3574 | 2026-07-25 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 218.5 |
| b01c9538-1ff7-315f-81d9-ca9fefc9e025 | -10.6755 | -46.3574 | 2026-07-25 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 95ab6c68-cc6b-36d4-8215-6985f3bdb779 | -9.5277 | -47.1187 | 2026-07-25 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 2581b96f-619a-3896-af14-270144e13dcc | -10.6755 | -46.3574 | 2026-07-25 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| fbaedba3-6744-3f50-9130-d207eb69e259 | -9.5277 | -47.1187 | 2026-07-25 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 94de0b99-0839-3a79-b290-fc0ff15b653f | -9.5277 | -47.1187 | 2026-07-25 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| f69fbe15-1c55-348d-9a82-9f7d4c2baa4d | -9.5277 | -47.1187 | 2026-07-25 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 32f0a705-2182-3b8d-827c-f6618864c3ac | -10.6755 | -46.3574 | 2026-07-25 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |


