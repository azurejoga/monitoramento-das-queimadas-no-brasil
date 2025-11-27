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
| 7e4cbb1d-a5a4-3e37-895c-d74fe56b8d36 | -3.2386 | -45.4268 | 2025-11-27 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f399d721-0dff-3be5-abb8-22ce064860bf | -1.3494 | -53.1094 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| cf01cdc0-6d6b-35f5-8b8c-8c80dd939888 | -5.703 | -47.0532 | 2025-11-27 00:00:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0590fe1e-c7f7-309a-8658-f007a10711f8 | -3.7119 | -40.8561 | 2025-11-27 00:00:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 73db49f0-8184-3b84-9a6f-fdc88c4236a0 | -1.3494 | -53.0891 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| c23beb80-6287-3aa8-a9a4-e4b325dfaca6 | -4.1297 | -45.7233 | 2025-11-27 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ee0e739f-3a62-362a-b1c3-82a169fdb70b | -3.7871 | -50.7692 | 2025-11-27 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 02e5487e-c7d6-34fc-bb6c-bdd0179a5dac | -4.7204 | -46.4497 | 2025-11-27 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 7c35f0a8-a2e5-3b2a-b8c0-c7b9b5726759 | -1.3678 | -53.1092 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d2793d47-450e-3a77-92fe-eda1b64e151b | -4.7018 | -46.4508 | 2025-11-27 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 1b100a68-909d-39ef-844f-e91fe1cb78cc | 3.1276 | -60.7647 | 2025-11-27 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cbcb5fa8-006d-38d5-b2d0-29256e0ee396 | -3.5269 | -43.6828 | 2025-11-27 00:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 906b713e-be75-303e-8caf-553234ab302b | -3.2573 | -45.4035 | 2025-11-27 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 259.4 |
| dfe8350f-9d49-3f86-974f-cd9ef8dd565f | -1.331 | -53.1096 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 2a9de5f6-1163-3092-bdc9-97deb5fa5e8d | 3.1094 | -60.765 | 2025-11-27 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| adaaa776-dc5c-368b-9624-2df13fd50625 | -3.8454 | -50.1802 | 2025-11-27 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 08bbb10a-5b33-36c0-9063-32ee50d8827d | -3.2387 | -45.4043 | 2025-11-27 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 234.0 |
| 8ce1ec98-47e4-366b-991a-1d7ef859723c | -4.575 | -43.2784 | 2025-11-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e52225ed-6151-38bd-a267-c21abc89f778 | -4.5749 | -43.3017 | 2025-11-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 216.4 |
| c8d88f1c-61ca-3e68-bcf9-40e18a8971ea | -3.3792 | -43.4117 | 2025-11-27 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 74a5b764-bce3-33fd-9891-da071313fbcd | -2.9232 | -45.3037 | 2025-11-27 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 80711314-1143-3b13-8147-1308b27f2da9 | -9.5691 | -42.9421 | 2025-11-27 00:00:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 373d4eae-559e-3404-829c-0e942733bd33 | -3.8269 | -50.1809 | 2025-11-27 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 8a824d1f-f5d9-3c04-9a88-6a513ec11231 | -1.3311 | -53.0893 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| dc2b2dcd-7ab5-3361-86e7-c52b9ab42ab9 | -2.0487 | -45.8008 | 2025-11-27 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 94042d1a-a4c4-386a-914e-850089bc4215 | -1.3678 | -53.0889 | 2025-11-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e340d185-d4bd-3af2-97a5-cfa60dc45842 | -4.7203 | -46.4719 | 2025-11-27 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 0c64dbe2-5a2d-31ae-9abc-0b054f1e5250 | -3.2572 | -45.426 | 2025-11-27 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 0f2756a4-e1d4-39ad-948a-7fdf9c132b48 | -4.9473 | -48.6204 | 2025-11-27 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f7428f9c-5e67-32f7-bd7a-ff56196b88fc | -4.575 | -43.2784 | 2025-11-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 993541cc-c298-38a3-9c31-16d7faae47fa | -3.8454 | -50.1802 | 2025-11-27 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 03478208-d027-301f-a787-873e3f8b48bf | -3.2387 | -45.4043 | 2025-11-27 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 31aa192b-58b0-3f69-a841-ae840ce57294 | 3.1094 | -60.765 | 2025-11-27 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4fdc7ed1-82ba-333a-80f8-7e3badda2437 | -10.087 | -36.1511 | 2025-11-27 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 710ec96a-419b-3fa1-86e8-9e938dd0942d | -3.2573 | -45.4035 | 2025-11-27 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 36f0bdfc-9748-3822-b4bd-152589236221 | -5.703 | -47.0532 | 2025-11-27 00:10:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3df79be2-f537-3fc7-9f4f-3a15574ba7e2 | -1.3678 | -53.1092 | 2025-11-27 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 17ebd5d9-4ce8-33eb-9950-5e0da61ceb44 | -4.5749 | -43.3017 | 2025-11-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| a4bd91f7-05a0-3cb3-a682-bf615e4cdf4d | -2.9232 | -45.3037 | 2025-11-27 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| baa8e183-d160-3e36-8b81-ace2512a69be | -3.5269 | -43.6828 | 2025-11-27 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e9a39fc7-8f37-335a-8d40-40b521dafdd3 | -1.3494 | -53.1094 | 2025-11-27 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 5562dc70-f161-3300-a17c-93049fd5b028 | -3.8269 | -50.1809 | 2025-11-27 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f6520f97-0cff-33d7-8f3e-e96ce42261ba | -10.0677 | -36.1546 | 2025-11-27 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 868d0bab-0e6b-3b93-a7ba-cdb3caff6a85 | -4.1297 | -45.7233 | 2025-11-27 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 995e0e55-3508-3910-bbb0-6b653c9574d0 | -5.7216 | -47.052 | 2025-11-27 00:10:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ab1a1d7e-f0cb-340e-badc-b73f26d65198 | -1.3678 | -53.0889 | 2025-11-27 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1237d1ef-422e-34e2-9b12-402b78a87971 | -4.7203 | -46.4719 | 2025-11-27 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| ed08f107-8a2b-3665-ba24-05319eae536e | -3.2572 | -45.426 | 2025-11-27 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5ba71855-102f-3d7d-9c76-f790da276c5f | -1.3494 | -53.0891 | 2025-11-27 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 96df6d4d-9a09-32ed-8cdc-846338bed25f | -4.7018 | -46.4508 | 2025-11-27 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a94bdf9e-e329-3144-8d88-fadbd65e19dd | -4.7204 | -46.4497 | 2025-11-27 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 149177ab-392f-37c1-8951-271a40d13893 | -3.2573 | -45.4035 | 2025-11-27 00:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| dfee86ac-6815-34cc-8ede-e86774dcf3dc | -3.2387 | -45.4043 | 2025-11-27 00:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ed967edd-c53f-3473-96e0-a075818e1c97 | 3.1094 | -60.765 | 2025-11-27 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a6a4d834-359c-396d-ab90-4fb3ff6325a8 | -4.7204 | -46.4497 | 2025-11-27 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 166.5 |
| b343a1b6-b4d2-3582-b979-2311e1e8f85b | -3.806 | -47.0682 | 2025-11-27 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f057d76c-2d45-3144-81ad-5a57bf5722d4 | -1.3494 | -53.1094 | 2025-11-27 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ad27cf3c-baeb-3b05-8dd9-069058d8fd1d | -3.8246 | -47.0454 | 2025-11-27 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 13927767-f565-37f1-83bc-ae115aa15329 | -4.7203 | -46.4719 | 2025-11-27 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| a167ddbb-170c-3ba3-ad6b-dd74b18b84e4 | -2.7105 | -47.3929 | 2025-11-27 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 46ba8fb4-d094-385e-aa1e-238da3b92c80 | -4.5749 | -43.3017 | 2025-11-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 7732a55f-419b-3e43-95a5-b2f58d9ee194 | -1.3678 | -53.0889 | 2025-11-27 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a79d042f-bd3b-366f-8531-07593228f41f | -2.6919 | -47.4153 | 2025-11-27 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 56862f72-1769-35c3-a89c-82d30ff89eff | -4.7018 | -46.4508 | 2025-11-27 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e0f258a0-b312-3b02-a2af-46b0f75721d9 | -4.1297 | -45.7233 | 2025-11-27 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7b36e673-8c7f-3a57-8d03-3dce944925b9 | -2.7104 | -47.4147 | 2025-11-27 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b23ab1dc-67b0-321b-8cd2-d2165678b62a | -1.3678 | -53.1092 | 2025-11-27 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 80091454-2fb7-3589-a4ea-242788c840d6 | -2.692 | -47.3935 | 2025-11-27 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6ff3961c-c357-3da3-bd23-7cccb94bfb35 | -3.5269 | -43.6828 | 2025-11-27 00:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 67c53625-ea7f-3332-8a16-50a6da11bb00 | -5.703 | -47.0532 | 2025-11-27 00:20:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c2bbc428-0fbb-3c65-a769-e27db0d76d54 | -3.8269 | -50.1809 | 2025-11-27 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 09f89bb0-420c-3468-b971-9f5791a712c7 | -1.3494 | -53.0891 | 2025-11-27 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 92f4f4ee-990d-3363-b1d4-b49dd66b6c8b | -3.8061 | -47.0462 | 2025-11-27 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| f5fc6d61-b972-3f4c-9434-2edcd6758c82 | -4.9473 | -48.6204 | 2025-11-27 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 752f6ab0-6802-38d4-8239-bf414aec00ee | -3.4025 | -54.5644 | 2025-11-27 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2727b576-c825-34d8-a207-42218a5e6c54 | -1.3692 | -53.091 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0de3e945-ec96-3545-a5d7-91bac17b8b07 | -1.3594 | -53.093201 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a5a2dfe-5592-3339-953c-2c231be110af | -2.7893 | -52.9468 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a200706-1112-3580-80a2-c88cb0aaff6a | -1.6741 | -53.6619 | 2025-11-27 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615b2c01-8a5a-3872-b37c-e30133e02d3e | -1.3327 | -53.156898 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf7f4bed-8a3a-3f4e-b21f-3c02c175228a | -1.3563 | -53.079498 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2876013a-1354-3804-bed1-ac38073f8efe | -1.3481 | -53.0886 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e244263c-6ae4-3004-9d83-4c9ed527e737 | -1.3677 | -53.084202 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ae890f-4ff9-358e-88a5-a7b51008d033 | -1.3579 | -53.086399 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 843d3a7e-dec5-3f0a-8491-ff61b9969b2b | -2.9156 | -54.186199 | 2025-11-27 00:25:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408e0782-d78f-38d3-8389-e93f618021c5 | -1.3449 | -53.074799 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a21f06-734c-3996-afe3-5cacec0f968c | -3.0582 | -54.543999 | 2025-11-27 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71da8816-cb76-344b-bda5-67e51867583d | -3.0794 | -52.455399 | 2025-11-27 00:25:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a24208-fa3f-31c0-8047-0efa05698727 | -1.4777 | -45.777599 | 2025-11-27 00:25:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 994f2045-9e85-3006-8339-fb0955df43c7 | -3.0566 | -54.536999 | 2025-11-27 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aea2663-dacd-37bf-8abd-7a8021aa8fe9 | -3.081 | -52.462299 | 2025-11-27 00:25:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4974ec-fded-3aac-b555-0f2ac2288547 | -2.8767 | -51.792301 | 2025-11-27 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d313d94-52e5-35c1-b16d-066f552977a5 | -2.7151 | -53.164501 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a58e6a-00b5-3a48-b97b-8178e5cdf24a | -2.7991 | -52.944599 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a7ed46-59b6-39be-a164-d6c17ca4872b | 2.8758 | -60.239201 | 2025-11-27 00:25:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 95a55e61-cfab-39d5-b37f-af4725eba00b | -1.3465 | -53.081699 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31cf77f8-eab1-3bf7-a173-676100e54e3f | -1.3367 | -53.0839 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58740e43-9f77-318b-93e1-518062b747ae | -2.7877 | -52.939999 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4754d3-5ca6-3d43-94fe-b522d92d5e71 | -1.3383 | -53.090801 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d50448-8b1a-3931-8a06-11452270390a | -2.7975 | -52.937801 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
