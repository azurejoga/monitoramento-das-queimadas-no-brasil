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
| d85b4049-ace3-3ebc-8399-59b426787135 | -9.7328 | -43.4168 | 2026-09-07 08:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| bfdf5dad-798e-39e1-8072-8a567673a40b | -11.5001 | -49.6109 | 2026-09-07 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1d9816ec-59c5-3fe3-98ed-7a7e8f02198f | -13.3004 | -45.2442 | 2026-09-07 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c351e3be-38ce-3cd1-a754-9819b4a859d1 | -13.3198 | -45.2409 | 2026-09-07 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9dd20c6d-1d21-3e59-b98e-1900f113a118 | -11.5191 | -49.6087 | 2026-09-07 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8e99c2e9-6f0f-309a-ac73-2be565f81996 | -9.7332 | -43.3932 | 2026-09-07 08:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 35c6c95f-7fd0-3aa2-8f41-26b38cc083a8 | -3.1462 | -60.6506 | 2026-09-07 08:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| dfaaa068-081c-3d86-a34f-2ea594a69cd5 | -13.3009 | -45.2209 | 2026-09-07 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| be508c80-b6e7-304b-82cc-f57f9ad50646 | -13.3009 | -45.2209 | 2026-09-07 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| cbdab0d5-ddcc-3a5e-9257-56ba01b394ce | -11.5001 | -49.6109 | 2026-09-07 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7cc7e0ca-bc60-3303-88b8-50747e177047 | -13.3004 | -45.2442 | 2026-09-07 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 125bf84a-1bea-3c72-8369-574b6ee982e6 | -9.7332 | -43.3932 | 2026-09-07 08:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 73.6 |
| a792fc40-e0a0-3905-b08a-26a761589b13 | -9.7328 | -43.4168 | 2026-09-07 08:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9a2bbc78-9b19-3500-ad6d-64b2aa8a9a68 | -13.3203 | -45.2177 | 2026-09-07 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 241cdc05-2ebc-3bd9-be1f-161cf88661f7 | -11.5191 | -49.6087 | 2026-09-07 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a4a347ee-db63-3dde-8073-7fa1887c7e64 | -13.3198 | -45.2409 | 2026-09-07 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c5879242-b3a9-3758-93df-f6b1e6b46f10 | -3.1461 | -60.6696 | 2026-09-07 08:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| f6969d25-2c07-3978-892d-9d5f9fa4bf91 | -13.3004 | -45.2442 | 2026-09-07 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| dd0dfbce-2514-3728-aaa0-0c0d0a5a6769 | -11.5001 | -49.6109 | 2026-09-07 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 84451cb2-e9d6-3eea-8106-6d5acf747860 | -13.3009 | -45.2209 | 2026-09-07 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b177f5ad-5027-3f0e-b73c-0ced229389cc | -13.3203 | -45.2177 | 2026-09-07 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d50af494-f43b-315b-81b9-507d8a00f2bd | -13.3198 | -45.2409 | 2026-09-07 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ad6b3e6a-d9db-33da-9773-19cd30cded12 | -3.1461 | -60.6696 | 2026-09-07 08:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a203e2cd-b57c-3088-8b15-437fb29b6dc9 | -9.7328 | -43.4168 | 2026-09-07 10:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c89c5912-0e82-3841-825c-da66d2542c4e | -9.7141 | -43.3956 | 2026-09-07 10:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 73dd787c-a6e8-339c-b659-fbd8a80c926b | -9.7138 | -43.4192 | 2026-09-07 10:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 749075f7-86e0-39e8-bd0e-a33b25ba3cec | -9.7332 | -43.3932 | 2026-09-07 10:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 5d7b778f-79f1-308f-b0b2-9fb8704e7724 | -9.7332 | -43.3932 | 2026-09-07 10:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 93.1 |
| cbb85f12-630b-3804-8f15-1513a26f0cad | -9.7328 | -43.4168 | 2026-09-07 10:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 638fe60a-2d5a-3c2e-9e1b-174907b29a4d | -9.7328 | -43.4168 | 2026-09-07 11:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 2b933afe-2d99-3d06-b224-e3abed64855d | -9.7332 | -43.3932 | 2026-09-07 11:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 62c3517a-3469-32a6-a712-29318494298e | -9.7328 | -43.4168 | 2026-09-07 11:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 319.3 |
| 84bafd24-c8b9-3747-8c17-12edf61137d1 | -9.7325 | -43.4403 | 2026-09-07 11:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 49d561ce-0627-3123-a707-c7bfd501dae8 | -9.7332 | -43.3932 | 2026-09-07 11:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 192.3 |
| bef81b74-db96-37dd-a1e7-61b74daae752 | -9.7325 | -43.4403 | 2026-09-07 11:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8732e161-b3eb-3180-af52-68b26940a39a | -9.7328 | -43.4168 | 2026-09-07 11:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 9cdae751-eb2f-37df-a087-28ca7fcb8d1b | -9.7332 | -43.3932 | 2026-09-07 11:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 38648a5f-f5f7-3045-8faf-cd56290d893c | -9.7519 | -43.4143 | 2026-09-07 11:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 86a2d63e-cb36-3d2b-9182-0d86a82a8ed1 | -9.7325 | -43.4403 | 2026-09-07 11:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 4f6f2afb-2670-3d35-a507-0d3128d0a579 | -9.7332 | -43.3932 | 2026-09-07 11:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 184b8e19-0ef9-3a0e-9bea-dbf46baa31d5 | -9.7328 | -43.4168 | 2026-09-07 11:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| d32bfbbc-1464-3066-ad99-921e490f4edd | -9.7332 | -43.3932 | 2026-09-07 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 97.8 |
| b2e71e9a-6e20-33b6-afcb-49cbf89744b0 | -9.7325 | -43.4403 | 2026-09-07 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| ccafeff8-d68d-378a-9aeb-0c89483e5ff8 | -9.7328 | -43.4168 | 2026-09-07 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 32914992-019a-3a81-a536-881731d298a1 | 1.72618 | -50.98059 | 2026-09-07 11:47:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 75858592-0b00-3de5-9b92-7451898a903e | -1.46122 | -47.62276 | 2026-09-07 11:47:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc21ceae-c6de-365e-9cf9-3c46efa7bbf5 | -1.60237 | -47.73613 | 2026-09-07 11:47:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1e0a4dc8-6bb1-37dc-8737-93c9aabc5e02 | 0.21674 | -51.27938 | 2026-09-07 11:47:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 24.4 |
| a86a2b78-a9c6-34aa-bf0b-e204829aa496 | -2.6263 | -46.77472 | 2026-09-07 11:47:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1ccc54ca-62d2-3c25-9214-1330ff4c64af | -2.6364 | -46.76713 | 2026-09-07 11:47:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5b9a52cc-e9dc-3b70-884c-453b206433ce | -2.63515 | -46.77594 | 2026-09-07 11:47:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 88350180-8404-3797-a768-28c599f67555 | -1.87089 | -47.98322 | 2026-09-07 11:47:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d58f17c8-881f-3b15-b604-f0f29ec31ddc | -1.70073 | -47.7562 | 2026-09-07 11:47:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 643f77ec-f409-3ca9-9c31-13d44f55a386 | -2.62756 | -46.76592 | 2026-09-07 11:47:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 181898ec-8894-3175-b59d-de8bfaa62b90 | -2.8842 | -50.43069 | 2026-09-07 11:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 93fcc8bf-3570-35e9-8c33-c572ef611bde | -4.28233 | -46.53532 | 2026-09-07 11:49:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58180e1b-d5f1-39da-a637-e8952859dc4c | -11.50622 | -49.61182 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 85b0abaa-86dc-32d0-b345-9fa601d0e9b3 | -4.11418 | -49.06421 | 2026-09-07 11:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c3bf7e39-7409-3ba4-8f26-9a40c2ac93f8 | -11.27985 | -45.09916 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9ac787f8-c6f0-3e6a-8b27-76769a26b04b | -9.74301 | -43.41999 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bc08d5d0-56d8-3c6f-8fe2-f67df6ffe824 | -13.31395 | -45.22685 | 2026-09-07 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c9fc3360-9889-369c-be41-d681c8f19c18 | -11.33948 | -45.10053 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c0071f10-50bb-3954-8239-de874a24aea3 | -3.55139 | -48.17078 | 2026-09-07 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5975c94f-3ee2-3b28-9457-e44ec66d7d27 | -11.57133 | -50.61897 | 2026-09-07 11:49:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 621d1a49-a128-3408-a720-af54a8cbc986 | -3.95975 | -43.1185 | 2026-09-07 11:49:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d7890b15-f86d-3ac8-a04c-039dc059719b | -11.51378 | -49.62211 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9b9e042a-0e48-3b9e-940c-41174c94b74a | -3.55011 | -48.17966 | 2026-09-07 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3f38deba-e6c3-36b4-b1d4-d5135f02b3d5 | -9.73131 | -43.41846 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 50a86909-ad57-3ba9-a494-55098a5e0089 | -13.30148 | -45.23904 | 2026-09-07 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| bb86f0ed-32f6-332d-b24c-288670b76727 | -13.3122 | -45.24038 | 2026-09-07 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 69096843-1e9c-388b-8a33-3913d22e7708 | -6.63107 | -43.74056 | 2026-09-07 11:49:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9393b344-5039-330f-a350-10f95a83d509 | -13.30695 | -45.2319 | 2026-09-07 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9795c935-b77a-3895-b748-e333258834f9 | -13.30322 | -45.22545 | 2026-09-07 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| cceb0ab9-4fac-3cc2-bbec-d410fa822eb7 | -2.82567 | -49.2298 | 2026-09-07 11:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 61ca26a2-5b6f-37ec-aeb0-5c6d46dbcdd9 | -11.85368 | -42.71963 | 2026-09-07 11:49:00 | TERRA_M-M | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 13081eb5-d844-3dac-af69-2f8f2515c77d | -4.28362 | -46.52629 | 2026-09-07 11:49:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ffd6e830-126f-367b-87de-6a1ae9890a14 | -3.60743 | -49.44925 | 2026-09-07 11:49:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fa44a669-966d-3304-8aed-9b527bc34bbb | -12.50007 | -45.26363 | 2026-09-07 11:49:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f0c4303a-003d-38e5-b329-f7955dd52bb5 | -11.49866 | -49.60153 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ca4c7aec-8a1f-39d3-a7e2-e72a3bd4c870 | -4.35903 | -48.96534 | 2026-09-07 11:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6329391-fff7-3b42-9edc-609bf5fed6a1 | -2.95733 | -48.7069 | 2026-09-07 11:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9da0bb1c-6e44-3112-9e96-231cfa0ca78f | -3.60603 | -49.45908 | 2026-09-07 11:49:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb78c18e-6482-3c4b-a389-d03490ae2317 | -4.21502 | -48.56014 | 2026-09-07 11:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e641aad0-c34f-3c80-afe2-1562b6278750 | -11.56992 | -50.62847 | 2026-09-07 11:49:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4dd03d88-49fc-305d-bbde-22c8fbbc37ea | -11.54242 | -49.62354 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 321ff02a-6554-3e9a-863f-6fb1d8f279c9 | -9.72163 | -43.40092 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 41461b8c-25ef-3b02-beec-aac3e9ac8056 | -4.10509 | -49.06293 | 2026-09-07 11:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 647fc033-ac09-3b4e-a82f-622f1b977c33 | -4.34865 | -48.97331 | 2026-09-07 11:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67f83921-fb8e-3f86-aefd-bdc08827a9b7 | -2.87263 | -50.44058 | 2026-09-07 11:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d65f9368-3ec4-3e10-9886-e52d7e89df2d | -6.62858 | -43.73364 | 2026-09-07 11:49:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 30d7f17c-d34e-35a7-9726-7279f2de59f0 | -11.92437 | -42.01406 | 2026-09-07 11:49:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 293b561c-365b-3a02-b7da-1016cb056bd0 | -11.49996 | -49.59253 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 83231da1-4138-3807-9b57-bfdc74ab8723 | -9.74096 | -43.43605 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8535a312-971c-365b-a4d5-ac0c836bb3b5 | -11.51508 | -49.61311 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 61fbbc9a-eb2b-3d30-86bd-17527ba1533e | -11.34113 | -45.08753 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a6f09191-54f9-34a1-8abc-7c755dc87bea | -2.87099 | -50.45189 | 2026-09-07 11:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9f98569c-1e29-3970-a953-4329c4d86d2d | -4.35769 | -48.97459 | 2026-09-07 11:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a063a905-04db-32cc-b670-d33db43ad151 | -2.88256 | -50.44199 | 2026-09-07 11:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 088ce675-bdcc-3ed2-8fec-56f903689fcb | -11.43041 | -45.10569 | 2026-09-07 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9b07313c-9630-306e-8c3c-68e48471cd91 | -11.49736 | -49.61054 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |


[Clique aqui para ver as próximas entradas](README39.md)
