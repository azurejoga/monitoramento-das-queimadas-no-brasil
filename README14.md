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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 988c02be-e677-3cb7-94a8-9c398520c306 | -11.1548 | -54.1054 | 2025-09-30 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6329514c-e7d2-3013-822f-1d607ae5d67d | -10.1855 | -44.8709 | 2025-09-30 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ad0c4ef0-311d-376f-80a0-caec6cf63a18 | -11.1735 | -54.1242 | 2025-09-30 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b2373cab-f4df-3b8f-99ed-62914d65a05e | -10.1851 | -44.8939 | 2025-09-30 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 547baedb-53ab-3fb3-a4ef-65f440c7354f | -17.7149 | -46.6631 | 2025-09-30 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2c1b7da0-e319-323e-9a3a-baf2874cdfa3 | -14.6603 | -46.9663 | 2025-09-30 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 292.7 |
| 7b861d07-f5ed-3b15-930d-319c50b9c63d | -12.1928 | -43.7415 | 2025-09-30 02:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0290068b-9073-390b-8863-a24606233d37 | -12.8429 | -47.0063 | 2025-09-30 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b7590b13-ac92-3796-ab8b-e028074c0c74 | -10.1847 | -44.917 | 2025-09-30 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b411d65d-651c-3474-aea5-0116bc796790 | -5.5241 | -43.8878 | 2025-09-30 02:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5a6f423a-1e8e-3be4-95df-220359bfda47 | -11.1735 | -54.1242 | 2025-09-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b0bb7388-1bf0-3f01-84ff-c30b90f9f3af | -14.2782 | -52.9391 | 2025-09-30 02:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4b127144-f9c6-32bd-a3bf-0e1647f5db0b | -14.5327 | -48.4715 | 2025-09-30 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c5dc3cc8-d079-3b0a-910d-6003e1488641 | -11.1543 | -54.1465 | 2025-09-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e3b9e01e-2775-3fcf-b84d-fc6291b4daeb | -14.2971 | -52.9577 | 2025-09-30 02:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6fa083b6-5f0b-399c-82cd-e7f438c34cfb | -13.0215 | -42.8137 | 2025-09-30 02:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 24aa0fc8-5ec0-304d-b130-f6279b596a78 | -11.7519 | -44.7461 | 2025-09-30 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 0cd1b56f-c09a-3468-8968-f060052311b5 | -14.6603 | -46.9663 | 2025-09-30 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c65327bd-67a5-3370-b9a6-cf3bbaa1d871 | -11.2516 | -47.226 | 2025-09-30 02:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 7dca0420-965b-3c07-83dc-6eeb2b92a4d5 | -10.1851 | -44.8939 | 2025-09-30 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 5b4b700f-fa9e-3a32-afa3-9204594f9847 | -11.1546 | -54.126 | 2025-09-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.5 |
| 69362ad2-1095-3948-ab3b-ded51b486ecc | -10.1855 | -44.8709 | 2025-09-30 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 889c9fb0-43d7-3844-adef-51d2c95bbcf0 | -4.4013 | -44.0755 | 2025-09-30 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 344d7493-8f6a-36ca-ac95-bfd444f0fde4 | -15.3792 | -47.0689 | 2025-09-30 02:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 826f8868-1bed-38e7-9cde-da9e6bf6d147 | -21.2388 | -47.1209 | 2025-09-30 02:30:00 | GOES-19 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 735addfc-a40c-3f3b-9461-04926c02fa25 | -7.9191 | -44.6245 | 2025-09-30 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| fcb8161b-7e45-35d3-9f15-c470bd33d787 | -11.1548 | -54.1054 | 2025-09-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4777652e-1bf7-3567-9852-b9719a651c20 | -14.2778 | -52.9601 | 2025-09-30 02:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 728aa8df-395e-3d42-b190-28cbe88ef2e8 | -10.2041 | -44.8915 | 2025-09-30 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| c153fa34-0f91-34e1-9288-5b58d0a760b5 | -14.5522 | -48.4684 | 2025-09-30 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 5e77a275-e4f6-36a5-971b-3a7120855a12 | -14.7465 | -45.6656 | 2025-09-30 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 55c13511-f84a-30cf-be09-b5c3c74a16d5 | -14.5517 | -48.4907 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8d86a722-b535-3861-a2e7-6b75022bba2d | -10.1847 | -44.917 | 2025-09-30 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3173b55f-88ed-3254-9d12-bbc4749c664f | -13.2158 | -50.95 | 2025-09-30 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 12d84ded-310f-3303-81ad-4eba78a4916d | -14.5137 | -48.4522 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 588a3f6e-2c9d-3f47-9513-12fccefc0779 | -10.2041 | -44.8915 | 2025-09-30 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| cb34f7aa-697d-3d16-9461-e55fd1dcf0c2 | -14.5327 | -48.4715 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 8eeadfa9-1cde-3cbc-b9a4-0d19912a7682 | -4.4013 | -44.0755 | 2025-09-30 02:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1aaca9e4-968a-39ad-8956-acfb9392d6ee | -14.5331 | -48.4491 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| df40d95d-5d64-308f-8a72-e3f24e979f0d | -14.5323 | -48.4938 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 736f0fbf-9951-375a-b6ab-0f8f190e4d45 | -12.8429 | -47.0063 | 2025-09-30 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| eddc32bf-71c2-35b6-be7d-9d1719ed2a53 | -14.5522 | -48.4684 | 2025-09-30 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 75f9389f-0b4f-3e1f-8546-3610b8ea2f23 | -5.5243 | -43.8647 | 2025-09-30 02:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6456921e-4f29-3a1e-a0a6-bc372a4db836 | -5.5241 | -43.8878 | 2025-09-30 02:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 7608e66b-e07d-3351-97a9-8728bf76b0f6 | -17.7155 | -46.6398 | 2025-09-30 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e7f31013-a607-3194-8e9d-0f6908604099 | -17.7149 | -46.6631 | 2025-09-30 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| eaccac1e-d199-35e2-9882-45a7d73f725d | -11.1735 | -54.1242 | 2025-09-30 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a3f0841c-c38a-3842-bfea-62e4717873d3 | -11.1548 | -54.1054 | 2025-09-30 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| bcb3fc75-fc1a-3772-983e-64cf18268c7e | -15.3792 | -47.0689 | 2025-09-30 02:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 040e7b19-1cde-3ae5-a6d3-b36a1d0ee4e4 | -7.9191 | -44.6245 | 2025-09-30 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1b3d1c3c-8747-3486-ac24-506727007856 | -11.2516 | -47.226 | 2025-09-30 02:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| afe38595-9b7c-358b-92ba-e8bc90878fba | -11.7519 | -44.7461 | 2025-09-30 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 87c8215b-ddf3-3828-a8f5-ee646a1b2344 | -0.1012 | -51.2738 | 2025-09-30 02:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 26.7 |
| f38c3751-5bba-3764-9ddb-97c81e8ecfb0 | -22.5205 | -44.597 | 2025-09-30 02:40:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| b381a396-ebb1-3611-b0d0-bcd962bcf072 | -17.7356 | -46.6356 | 2025-09-30 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 82cc4547-cba6-3737-9dee-c4ba583d457d | -11.1546 | -54.126 | 2025-09-30 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 667f456f-bbb2-39d8-a53e-e4f4aa94ffaa | -10.1851 | -44.8939 | 2025-09-30 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 307.8 |
| 3aca8d36-5342-3eff-8267-6fee03185266 | -3.1013 | -47.0082 | 2025-09-30 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 88682c93-c745-3b4f-b914-83c68608d6c7 | -10.1855 | -44.8709 | 2025-09-30 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 99b2957f-023f-3dd9-a748-b3e718f77121 | -14.5137 | -48.4522 | 2025-09-30 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a3d2892a-4f9a-39a7-b0e6-b57f71d4d2a7 | -14.5327 | -48.4715 | 2025-09-30 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| dbf65651-1d9f-3adb-98d0-3dce37b2f971 | -10.1847 | -44.917 | 2025-09-30 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| fe739715-469d-36b9-897b-78b0d5cd9dfe | -14.5522 | -48.4684 | 2025-09-30 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2f1fe18c-88cf-3730-a1e4-39f0ea25d23a | -11.1546 | -54.126 | 2025-09-30 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 89d52521-f74e-35e5-86c9-8116b1f22e50 | -10.2041 | -44.8915 | 2025-09-30 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 9e596aa5-97ca-33dc-99ac-064cce67bd82 | -11.1548 | -54.1054 | 2025-09-30 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 08dee902-072b-35e5-8dde-7884834ba950 | -5.5241 | -43.8878 | 2025-09-30 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3de9a3f1-2137-3e7a-9340-3b421c50609a | -12.8429 | -47.0063 | 2025-09-30 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c7c5947c-e148-31a7-8ebe-8245d2ce44e3 | -4.8915 | -43.4678 | 2025-09-30 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 4cde1da8-9814-33cd-946f-4f6c7219a576 | -14.7465 | -45.6656 | 2025-09-30 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e730654e-5146-3a13-b783-c33a608bd59b | -17.7149 | -46.6631 | 2025-09-30 02:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1525531c-458b-3aa7-b2c6-1120c1d8d10d | -11.1735 | -54.1242 | 2025-09-30 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 624bb3d7-4bd6-369f-9ea4-90ca01f21e1d | -11.2516 | -47.226 | 2025-09-30 02:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| fc030cb0-3d0f-3b37-9984-9cb5e48af41b | -13.2158 | -50.95 | 2025-09-30 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b4988db5-27d6-3a25-868c-80291f5f93d7 | -11.7519 | -44.7461 | 2025-09-30 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 39bdaeca-c45c-3e7a-af8d-70320e95d21a | -4.4013 | -44.0755 | 2025-09-30 02:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3b0c93cb-f0f5-3674-9a5c-c24a4f85e8c9 | -14.5331 | -48.4491 | 2025-09-30 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7f398bb5-ffc4-322f-ab65-3b4a9aa19f5a | -10.1855 | -44.8709 | 2025-09-30 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| bc53930d-d519-38ea-84db-20088fe40d5f | -11.1737 | -54.1037 | 2025-09-30 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 077e46ba-87a9-332b-8832-4ee202b01728 | -10.1851 | -44.8939 | 2025-09-30 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 399.1 |
| bf9acd00-c950-3924-a138-ed481eca152f | -5.5243 | -43.8647 | 2025-09-30 02:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 13dd33f5-78ab-3b00-8086-2e6d5b65266b | -0.1012 | -51.2738 | 2025-09-30 02:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 28.4 |
| cc06ff51-4552-316c-9c8a-e3d185671da1 | -6.7675 | -37.89973 | 2025-09-30 02:58:00 | NOAA-21 | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b23e835b-3efc-3581-9532-d6eaadb22090 | -11.2516 | -47.226 | 2025-09-30 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 39e621bc-dbc0-3d50-8297-2671b1f80cfa | -5.5241 | -43.8878 | 2025-09-30 03:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3eda5020-8abe-3db0-bda5-5abecfc9a273 | -10.1851 | -44.8939 | 2025-09-30 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 334.1 |
| e43653d4-7c0f-3a32-bba6-9e0572fcf1c7 | -11.2707 | -47.2236 | 2025-09-30 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3dd00a53-f68b-3e71-bdae-fc1eaab8abb6 | -14.7465 | -45.6656 | 2025-09-30 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c7a9941b-ffb8-3616-913e-a9624bba8eb8 | -11.7519 | -44.7461 | 2025-09-30 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 64eb0c7f-0115-3608-a1f2-04438b25596e | -10.1847 | -44.917 | 2025-09-30 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| dc948233-4205-3be7-9f77-2826fc179cd7 | -10.1855 | -44.8709 | 2025-09-30 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| dceedbc6-dd7e-3ef4-88d2-7b5a2f2d167c | -11.1735 | -54.1242 | 2025-09-30 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 91f777ca-7cc8-3b2b-98a7-8ef5b07c6f52 | -11.1548 | -54.1054 | 2025-09-30 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 06b9e379-297c-358f-a284-223486f8e0f8 | -5.5243 | -43.8647 | 2025-09-30 03:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2c074f33-8c93-3daf-be7b-e6771331ae9e | -11.2513 | -47.2484 | 2025-09-30 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 79595023-c314-3d25-8096-ce1863fd999e | -10.0717 | -50.2173 | 2025-09-30 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e670a875-9ca1-3509-a878-ef4012a07083 | -14.5522 | -48.4684 | 2025-09-30 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1d2f8523-9b55-3d76-8dba-ec163d0af572 | -11.252 | -47.2037 | 2025-09-30 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8b28982c-7eb8-3ce6-b9ba-240f9e018325 | -12.8429 | -47.0063 | 2025-09-30 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 34736dd7-733f-3006-a6bc-4cfb900534ce | -20.0491 | -41.3251 | 2025-09-30 03:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.3 |


[Clique aqui para ver as próximas entradas](README15.md)
