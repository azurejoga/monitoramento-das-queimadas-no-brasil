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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a1f096-5672-3b72-a1bc-600843392dac | -12.5546 | -47.026 | 2025-08-12 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 443a5d49-3615-34bb-8255-67cd9f09215c | -7.1483 | -60.1174 | 2025-08-12 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 247613b5-79ed-3184-a31a-9a3ca2735501 | -12.5742 | -47.0006 | 2025-08-12 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cf7a961e-08f1-3138-971b-9a571e4ef1a5 | -3.9686 | -47.8684 | 2025-08-12 07:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e294fbeb-f2a9-301e-bdf6-61ec64da0198 | -7.1299 | -60.1182 | 2025-08-12 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6bf737b5-f5ab-3c97-bc2d-71c80778b3a7 | -12.5746 | -46.9781 | 2025-08-12 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9008f4fc-1126-3dfa-9410-22279ae6cfa5 | -17.6549 | -46.6757 | 2025-08-12 07:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 509bdde2-cd2d-3b53-a009-f9aeb29dbb51 | -16.3157 | -52.8988 | 2025-08-12 07:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 3b782112-a8c1-362a-924b-84ee302f48b6 | -3.9684 | -47.8901 | 2025-08-12 07:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 038ee1b0-20f0-3993-a55b-e72d44196cd0 | -12.555 | -47.0034 | 2025-08-12 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 35be7d65-b6dd-3c3e-96d7-23e459d9cec5 | -16.3153 | -52.9201 | 2025-08-12 07:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 2a408152-5b77-3a40-ab67-7c86bb48435c | -16.2957 | -52.923 | 2025-08-12 07:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 92dc66e5-c9c8-3679-88d7-78e36f575b91 | -12.5554 | -46.9809 | 2025-08-12 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 657a30a5-52d2-3006-897f-b4f9dc5ec286 | -16.2961 | -52.9016 | 2025-08-12 07:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a4055e86-5f71-3b02-8557-b485f9d1cc9a | -7.14249 | -60.11805 | 2025-08-12 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b16377b2-b36c-3fa5-9e62-ff7ea4f26536 | -9.39065 | -61.52407 | 2025-08-12 07:24:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 505f2ef4-0039-3ca0-ad52-cde69ecb656f | -8.93341 | -60.71148 | 2025-08-12 07:24:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 12e06b43-6984-3e66-a6a3-7bdf6ce988cc | -7.13696 | -60.10909 | 2025-08-12 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 100d68d7-bee3-3fa5-8c32-e08d05ad9cd5 | -16.3157 | -52.8988 | 2025-08-12 07:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4cb5ac2e-82d0-318a-a20b-83ce4ecdd3d9 | -12.5554 | -46.9809 | 2025-08-12 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1b1c34ce-45a5-31d0-a778-582ecdb1b35c | -12.5742 | -47.0006 | 2025-08-12 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 38b18964-ba64-3e49-aae7-dd55db1533a1 | -16.3153 | -52.9201 | 2025-08-12 07:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| aa9d1fc5-b8b4-38a7-98d0-aaa2a31e58fb | -12.555 | -47.0034 | 2025-08-12 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 25f75397-0f5b-3875-b8a4-deb026531ad7 | -16.2961 | -52.9016 | 2025-08-12 07:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| bc40c368-51be-3c61-b814-eb94438f7543 | -7.1299 | -60.1182 | 2025-08-12 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0356a983-c4c9-3b11-8029-3c469fcb458e | -12.5546 | -47.026 | 2025-08-12 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f7059bb5-54e7-3dd0-aab1-e72529dc5143 | -12.5546 | -47.026 | 2025-08-12 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 86493869-e3c6-323d-8b51-047e6d770474 | -17.6544 | -46.699 | 2025-08-12 07:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 77e36cbb-96fe-3f83-abe7-36ffdd51b777 | -17.6549 | -46.6757 | 2025-08-12 07:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 66e9181c-c236-3b92-b5f3-773a62e4cd3c | -6.5856 | -44.564 | 2025-08-12 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 14eef1c2-fb08-3d54-b13a-51cdb42268fb | -12.5742 | -47.0006 | 2025-08-12 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 706f5bd0-7f04-31ce-b793-344efd8af5a8 | -12.555 | -47.0034 | 2025-08-12 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 61d355a5-b95b-3d22-a9de-f917c9d8ef60 | -7.1299 | -60.1182 | 2025-08-12 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 0bf92e4e-4375-3328-8e24-520f337a89e2 | -16.2961 | -52.9016 | 2025-08-12 07:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 610f9c37-a018-3a13-8b99-7b4d0f96374a | -16.3157 | -52.8988 | 2025-08-12 07:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 28ac41f1-967d-3328-932f-b9ce7487252a | -12.5554 | -46.9809 | 2025-08-12 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 728505eb-3a25-31f2-98e2-30e8db0a9b97 | -16.3153 | -52.9201 | 2025-08-12 07:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| daca394c-d067-3d8a-aeb6-f0ca65c7bfbb | -12.555 | -47.0034 | 2025-08-12 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 051c89cd-d042-3098-a5e9-88794bf9643f | -12.5546 | -47.026 | 2025-08-12 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6ea32bbb-5896-3cbb-bf0e-05a01e294d84 | -16.3153 | -52.9201 | 2025-08-12 07:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 135a6c89-e8fc-3fd4-b636-0cf183181682 | -8.5211 | -43.3063 | 2025-08-12 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c903eb0e-6ba3-3c2a-a46f-b61426c52b0f | -16.2961 | -52.9016 | 2025-08-12 07:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 9e36ad9c-a08f-30fd-8f4a-73b94d679ce2 | -12.5554 | -46.9809 | 2025-08-12 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c0a0f45b-1ec3-3ab3-9129-f6e0496bd892 | -7.1299 | -60.1182 | 2025-08-12 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| aea2daae-78ff-3ff3-bd4e-f94d52a3ca20 | -17.6549 | -46.6757 | 2025-08-12 07:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9cab86a3-4c29-3e0b-9e8e-cac3af46c236 | -16.3157 | -52.8988 | 2025-08-12 07:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| efd50c01-a84b-3c76-b043-bc270dc9269f | -8.5211 | -43.3063 | 2025-08-12 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 0ec1eea2-85b6-3e23-a47a-7eb59b5ff712 | -17.6549 | -46.6757 | 2025-08-12 08:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c9b8b59b-475c-35f1-a2d4-3711822c62c1 | -16.2961 | -52.9016 | 2025-08-12 08:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| d956fa4e-1ef2-3895-8f2b-44e6a54e9a63 | -16.3157 | -52.8988 | 2025-08-12 08:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e5fadb9e-9e46-321a-9a00-776bdacac41c | -16.2957 | -52.923 | 2025-08-12 08:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 674910d3-ef3b-31aa-98ee-d1c59ba26d8e | -3.9684 | -47.8901 | 2025-08-12 08:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ffbabefc-c767-36ec-b831-ce231bf20262 | -3.9686 | -47.8684 | 2025-08-12 08:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0d488f74-9ed1-3a48-915f-01406c978af6 | -12.555 | -47.0034 | 2025-08-12 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b53fcf36-9a77-3871-a71e-7bf8576088e4 | -16.3153 | -52.9201 | 2025-08-12 08:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| ab632828-a100-39df-9313-6e515f9f5d58 | -12.555 | -47.0034 | 2025-08-12 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 50cf3da1-818b-3375-b900-2a38621fa22f | -3.9684 | -47.8901 | 2025-08-12 08:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 69c78614-c844-38fd-a92e-f83c285dd326 | -16.2957 | -52.923 | 2025-08-12 08:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 581c8e05-237a-3d40-a03c-292e384c7638 | -16.2961 | -52.9016 | 2025-08-12 08:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 3ca6c1c4-fd58-38f3-857b-8b013c5e3f5b | -3.9686 | -47.8684 | 2025-08-12 08:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ff79e1bd-3a6e-3c84-a0a5-19d7c9d57139 | -7.1299 | -60.1182 | 2025-08-12 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ef33078e-ae71-3d86-8178-22fbc15a1a3c | -16.3153 | -52.9201 | 2025-08-12 08:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 07318b3e-3cbe-3653-a3c7-7e5d3629998a | -16.3157 | -52.8988 | 2025-08-12 08:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 73f3f605-84c2-3e38-baeb-eafba82e0124 | -8.5211 | -43.3063 | 2025-08-12 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d55a71ff-2734-3897-8233-3bc68a95625b | -16.3157 | -52.8988 | 2025-08-12 08:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 1d12f08b-6b2e-3ec2-9438-701ab1150684 | -12.555 | -47.0034 | 2025-08-12 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1fb455ce-f56c-3b4c-bff5-bb5177f70fc8 | -16.2957 | -52.923 | 2025-08-12 08:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 813ee4d9-e7c0-3323-8b7d-9af288832ac4 | -16.2961 | -52.9016 | 2025-08-12 08:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c2f90667-df01-3958-a558-669301b46f85 | -16.3153 | -52.9201 | 2025-08-12 08:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7449c8a6-e484-30b2-98f2-9a075ef69c17 | -16.3153 | -52.9201 | 2025-08-12 08:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 25b6f0e2-2269-3acb-bd17-723b9b5c4403 | -12.555 | -47.0034 | 2025-08-12 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fbd63943-bdd1-31c6-ba16-b9d7b497c68b | -16.2957 | -52.923 | 2025-08-12 08:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9ac8f41d-8d98-3120-af42-fef1299ee5a1 | -17.6549 | -46.6757 | 2025-08-12 08:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| cebd2e3c-58c4-39e8-b9c1-1a98b59341a0 | -12.555 | -47.0034 | 2025-08-12 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| abbd0523-ec4a-3d47-9a79-0d457722bb7e | -16.3157 | -52.8988 | 2025-08-12 08:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 858df2e6-7fd1-3281-a9dd-078d8b51d867 | -16.3153 | -52.9201 | 2025-08-12 08:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 95bffb75-b3f1-31fc-8845-8b58dc4a89d4 | -16.3153 | -52.9201 | 2025-08-12 08:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 99cb232f-0eaf-3e77-b312-471efefc188b | -16.3157 | -52.8988 | 2025-08-12 08:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 87cd2054-50d9-3777-aacc-d7d36d5f2539 | -16.3157 | -52.8988 | 2025-08-12 09:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c82fa178-b4be-3142-85da-b99f70f7616d | -16.3153 | -52.9201 | 2025-08-12 09:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bf424147-d9b2-3753-8f11-0dbc9a835665 | -12.5546 | -47.026 | 2025-08-12 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 09998d55-0b6b-3292-83a4-0e40e98495ac | -12.555 | -47.0034 | 2025-08-12 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 77da3d69-144c-334f-92ba-6c7c49534a1d | -12.7759 | -45.4445 | 2025-08-12 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| af421c0f-2b1a-3a89-a28d-a51b725e78ee | -12.5546 | -47.026 | 2025-08-12 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 305.3 |
| dc946b32-8908-3f66-9cce-54d0f48be211 | -12.555 | -47.0034 | 2025-08-12 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| e769cd75-60f8-3636-b172-1ea7d1320eec | -12.5546 | -47.026 | 2025-08-12 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 512.3 |
| 073c63d2-b591-32c1-94ee-7fab48d92a5c | -12.5738 | -47.0232 | 2025-08-12 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| ad8a8b33-02ad-35bd-ac32-4f1b0581ade6 | -12.555 | -47.0034 | 2025-08-12 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 245.6 |
| dbc81d7b-5fa2-3d48-a392-fb2ccfd97781 | -12.7759 | -45.4445 | 2025-08-12 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 96fb0846-ebab-3c81-b17f-ab5d03fda563 | -9.6461 | -48.1426 | 2025-08-12 11:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 46e5c695-6714-3bb3-b16c-5ed8dff0b963 | -12.7759 | -45.4445 | 2025-08-12 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 428bde07-f702-3fbb-863f-47fa75887689 | -12.555 | -47.0034 | 2025-08-12 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| ad84dd8d-62b1-379e-87b8-6bcba62e429f | -12.5546 | -47.026 | 2025-08-12 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 6c6c4d42-1ff3-38b6-810c-234b8d5b642d | -5.02532 | -37.6268 | 2025-08-12 11:51:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 4832caf3-0082-3644-ae2d-da3403922b87 | -5.53182 | -35.73735 | 2025-08-12 11:51:00 | TERRA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 89cc18cf-f58a-3140-b229-4d62442b4f8c | -9.22135 | -44.51887 | 2025-08-12 11:53:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e30f40ee-537a-3cbc-bb4a-51eae9237d23 | -6.6947 | -42.04897 | 2025-08-12 11:53:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 7ad15ff4-1610-3477-be19-3efbac81e1b4 | -10.08583 | -46.39875 | 2025-08-12 11:53:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2dca19a0-02b6-3550-aa6e-e69a0ab2048f | -10.69903 | -44.3955 | 2025-08-12 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3f56dc0b-0c91-3f0c-b328-aad941046f82 | -8.81457 | -44.58338 | 2025-08-12 11:53:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |


[Clique aqui para ver as próximas entradas](README39.md)
