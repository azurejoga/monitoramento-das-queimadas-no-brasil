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
| 22ece3b3-050c-37f9-a863-ea6cfba2bae9 | -12.34861 | -50.03894 | 2026-05-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cb7cec6b-8d8c-345c-86a4-b2b03c17280b | -11.8884 | -43.80736 | 2026-05-03 06:08:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 14a3f166-7465-3e7d-a277-41043c55763e | -12.37 | -50.0242 | 2026-05-03 06:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1e1a9565-23a1-3b0e-8341-36f3a9531c43 | -13.2183 | -54.5388 | 2026-05-03 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 4abf2173-28dc-382a-bf14-fe34029ecb10 | -20.18916 | -46.45752 | 2026-05-03 06:10:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 83a8a181-75cd-3f27-9ef3-2e712f600e3a | -13.2183 | -54.5388 | 2026-05-03 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| aceab8a8-921b-3c20-b84b-9653eb97f535 | -13.2183 | -54.5388 | 2026-05-03 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 74edf2c6-9efa-3989-ab8c-148b60322596 | -13.2183 | -54.5388 | 2026-05-03 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 47d43862-f43b-3582-9aac-99e8226d8924 | -12.37 | -50.0242 | 2026-05-03 06:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 45171b99-157e-375d-9e1c-0a5f5a305283 | -10.9815 | -45.0874 | 2026-05-03 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 29e6b802-5175-3019-ab83-410be36a7f9f | -13.2183 | -54.5388 | 2026-05-03 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 69c68a5e-ff0c-3c13-af9c-77edb3da2de4 | -12.3508 | -50.0266 | 2026-05-03 06:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0731d215-e30a-383f-ad4d-c041ff5e61b8 | -12.37 | -50.0242 | 2026-05-03 07:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 953d89e8-930f-33f6-b6bd-cffb6520e917 | -12.3508 | -50.0266 | 2026-05-03 07:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 66da663c-04f1-38e2-baeb-8664437cf881 | -12.37 | -50.0242 | 2026-05-03 07:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 22166650-90e7-3928-b611-f46951bbc0df | -12.37 | -50.0242 | 2026-05-03 07:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 41fe4cee-91b5-3957-9f10-71dc411210f4 | -12.3508 | -50.0266 | 2026-05-03 07:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f3a565b2-302f-37e8-bc68-e0cb7ad09165 | -12.37 | -50.0242 | 2026-05-03 07:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a8ec0938-6f18-3bfb-80d3-86c0d0b48925 | -17.9466 | -52.9955 | 2026-05-03 07:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| cdaa364a-bb73-3ffb-ac2b-b76dbdc56d4d | -12.37 | -50.0242 | 2026-05-03 07:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 3f05c650-b6d2-34ec-8bec-25c2be7dbaff | -12.37 | -50.0242 | 2026-05-03 08:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c7bf348b-fa9f-38ba-963e-4c077b1bc131 | -12.37 | -50.0242 | 2026-05-03 08:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1168b6c6-6b9a-3731-adb3-0fedca54897b | -12.37 | -50.0242 | 2026-05-03 08:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0e15a703-e5a8-31a3-a1c8-18be647fade2 | -10.9815 | -45.0874 | 2026-05-03 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 9a5273c8-1606-3c22-9074-ace83975c184 | -12.37 | -50.0242 | 2026-05-03 08:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 72cd89c7-3e97-342a-9231-6acffac0f677 | -12.37 | -50.0242 | 2026-05-03 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| bc7f4c52-b5a3-370d-ad01-67426650433d | -12.35755 | -50.04426 | 2026-05-03 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 58f66389-6dd3-3f82-a444-07653eb82ea7 | -13.21122 | -54.53822 | 2026-05-03 12:40:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d62e8a64-a553-3e93-b53c-fae892e1f161 | -12.36255 | -50.00889 | 2026-05-03 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 654822fc-1165-34a0-9558-b4bc629af12f | -12.35918 | -50.03779 | 2026-05-03 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6e6d6a56-3439-3880-853f-2de8ac73189b | -12.36072 | -50.01533 | 2026-05-03 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5766232d-7d75-3ea5-b12e-e10aea9099d3 | -11.44607 | -55.10475 | 2026-05-03 12:40:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 134d0c0a-c5b1-308d-93f6-4e08a6790180 | -17.9984 | -52.97381 | 2026-05-03 12:42:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4971c6fd-331f-374c-aa5e-420360150946 | -17.95942 | -52.96935 | 2026-05-03 12:42:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 70cf4a7f-1ea5-33cb-a5f0-79b7d851bbfe | -14.07078 | -53.39716 | 2026-05-03 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8d6f77f0-7f24-34f3-ae02-33c6cfcf3ade | -12.37 | -50.0242 | 2026-05-03 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a730f8f5-1263-3c11-95e1-788dcb8ab332 | -12.37 | -50.0242 | 2026-05-03 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 37214eae-f12f-3cd6-b75f-affbb0db95d2 | -12.37 | -50.0242 | 2026-05-03 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 341064cd-c3f1-3a61-85ea-98f5735c3b3a | -12.37 | -50.0242 | 2026-05-03 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2f5112bd-11a8-36a0-8ce6-1eda3884ac52 | -12.3508 | -50.0266 | 2026-05-03 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3487724b-d547-33a7-a4fc-5d1357fbba44 | -12.37 | -50.0242 | 2026-05-03 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 01c2be9f-e749-3d7b-9c0c-4322101e081c | -12.3508 | -50.0266 | 2026-05-03 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8b37cb0c-4aa2-3bb0-bb24-78ad4d0ba1ac | -12.37 | -50.0242 | 2026-05-03 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a11f85d9-0da0-3385-9f22-ff2ce8ae7012 | -12.3508 | -50.0266 | 2026-05-03 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 46f71bdd-680d-3a86-bf1a-c50674f00e17 | -12.37 | -50.0242 | 2026-05-03 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 46aab643-3fb2-3a74-9b38-36077179e99b | -12.3696 | -50.0459 | 2026-05-03 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b4f5bc42-59b8-3dab-8e9b-ed337af8e6fa | -12.3508 | -50.0266 | 2026-05-03 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a0d57029-1f6f-3a9f-896c-7552edf98b5f | -12.3508 | -50.0266 | 2026-05-03 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d0e36bc9-ef8f-3e90-bb47-6ece8fcf0a17 | -12.37 | -50.0242 | 2026-05-03 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| ddf7140f-5ff3-327f-a8b5-feb56a98d0c9 | -12.3696 | -50.0459 | 2026-05-03 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c5c23893-c271-328a-ae25-f5a9cd7041d5 | -13.2183 | -54.5388 | 2026-05-03 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4f0a742d-327e-3df5-af79-867699d12875 | -12.3696 | -50.0459 | 2026-05-03 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2fcae9c1-6f71-3e8c-8bdc-18ef69ed3919 | -13.2183 | -54.5388 | 2026-05-03 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 57596c2d-8777-3517-9206-1aa59cd37dc7 | -12.37 | -50.0242 | 2026-05-03 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| d879ea53-8594-380b-a5db-272c772ba8b7 | -12.3508 | -50.0266 | 2026-05-03 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6870a8f5-4738-3342-bc4c-b203ba7e5133 | -12.3696 | -50.0459 | 2026-05-03 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ec261771-db89-3980-a90f-1c41ac3f5a78 | -12.37 | -50.0242 | 2026-05-03 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 89ae12f3-cce4-3004-815f-f5aad26a70e7 | -12.3508 | -50.0266 | 2026-05-03 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 36d39c71-10ce-3993-a0aa-828172f8b287 | -13.2183 | -54.5388 | 2026-05-03 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| be0cd11b-88fb-3065-a080-2300acc9a16b | -12.3505 | -50.0482 | 2026-05-03 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6878c32c-09d5-31d4-8ae9-3a5485939ca0 | -12.3508 | -50.0266 | 2026-05-03 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 5126d46b-6f80-3a37-ad6c-7e63c4bfdb64 | -12.37 | -50.0242 | 2026-05-03 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| bab7f5da-f6ab-39df-b281-1701895809ef | -12.3696 | -50.0459 | 2026-05-03 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 9b8684e3-10e4-3097-81d4-d550fd76622e | -13.2183 | -54.5388 | 2026-05-03 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |


