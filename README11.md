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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d11f2247-545a-3155-80ad-69c89dddb60b | -3.1158 | -47.9232 | 2026-08-03 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| dd1bcf9e-af2b-31f7-afc3-349675565be2 | -7.9532 | -44.9188 | 2026-08-03 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d65cbdee-bec7-3211-904e-504fe4738173 | -6.0131 | -47.8648 | 2026-08-03 13:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5c7caf22-f7a9-3912-adf1-0f0ca5fb11d5 | -11.6047 | -50.245 | 2026-08-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 198e5831-5565-3df0-943b-23f49a29cbeb | -3.1158 | -47.9232 | 2026-08-03 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f6325633-48c7-35a1-bb6e-c66f1895bd64 | -7.2445 | -59.4596 | 2026-08-03 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5d7ec21d-89f6-37d6-8795-1fe74c23d9ac | -14.2687 | -45.2636 | 2026-08-03 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| df94a5b9-68ab-3adb-a979-f4c9213e45c5 | -6.0131 | -47.8648 | 2026-08-03 13:50:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 753a5517-89bc-32c8-8e35-170cf8a40bc8 | -14.2687 | -45.2636 | 2026-08-03 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c8fba115-7d4e-390e-81da-d27a4118c7c7 | -6.5514 | -55.1569 | 2026-08-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4b9f2c34-2d24-34ad-a255-7b6c9d3cd792 | -3.1158 | -47.9232 | 2026-08-03 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ef7bde33-13ff-3eb9-95df-b8ed619183dc | -11.6047 | -50.245 | 2026-08-03 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1fdeab2d-fa7e-3c32-ad87-7783d38cb47e | -6.5512 | -55.1769 | 2026-08-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f05d0484-092c-3692-bd28-20f7a8d18555 | -14.2687 | -45.2636 | 2026-08-03 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 8ee29aa8-b721-3474-8306-8b46def656eb | -10.2053 | -50.097 | 2026-08-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 504b546c-20e1-36aa-b701-730a970d3c5b | -1.6591 | -54.4543 | 2026-08-03 14:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 69a77754-e32f-3eb8-a5b1-3bcfdae28447 | -6.5699 | -55.156 | 2026-08-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2877c51f-bb4d-395a-bbd0-338c7f794f9e | -2.9581 | -50.3569 | 2026-08-03 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6268e3dd-fb88-3b92-84e1-c1a15c5c73c3 | -6.5514 | -55.1569 | 2026-08-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7226e22b-4c81-3cad-a2e5-af119d05e06a | -3.1158 | -47.9232 | 2026-08-03 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9cd76eb5-ed99-31bc-9e50-d1341392f95e | -9.9565 | -46.22 | 2026-08-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 013e9480-78e1-3a25-9aa1-2893f57ed194 | -6.5697 | -55.176 | 2026-08-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 292ead07-38af-3da1-b1e6-558cf944f4ec | -14.2692 | -45.2403 | 2026-08-03 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 266c851e-7ec7-3646-8706-1f970e4212a6 | -9.9568 | -46.1974 | 2026-08-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9ba1b34d-990e-388f-8717-edab47fcdacf | -6.5512 | -55.1769 | 2026-08-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 8ee37a4f-ab38-3f79-8060-5f9249576dff | -14.2687 | -45.2636 | 2026-08-03 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5409b77c-080d-3d52-be8c-678e190214c6 | -2.9581 | -50.3569 | 2026-08-03 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9d58228a-f4cf-3479-aab6-a37ab4c4595a | -3.1158 | -47.9232 | 2026-08-03 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e2fcd0b2-cbcb-3aef-ac95-cf4f5672fb30 | -6.5699 | -55.156 | 2026-08-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 02d072bd-6dce-3f76-be8c-707d49498adb | -7.6502 | -45.0852 | 2026-08-03 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5d71e8a1-64c1-3286-a6fe-bc7150c8a836 | -10.5741 | -46.7745 | 2026-08-03 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 04ea4626-7ac8-358d-9b11-22567ceb245a | -10.6312 | -46.7675 | 2026-08-03 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| d5484bb9-a212-3b24-9230-3ce6ddab8da6 | -6.5697 | -55.176 | 2026-08-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 745b507f-252d-31f3-92b7-0e2fba90e0ec | -11.4537 | -50.1765 | 2026-08-03 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c767519b-80b4-3242-bfda-c4bd60384556 | -6.5512 | -55.1769 | 2026-08-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| eb0fa3e2-2fb5-32cf-bcc8-61ea12261901 | -1.6591 | -54.4543 | 2026-08-03 14:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| fc6941de-7f71-3cb5-adf7-4425e1610379 | -6.5514 | -55.1569 | 2026-08-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| f4246906-a209-35fc-b752-ecddbb477231 | -9.9375 | -46.2222 | 2026-08-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 23233e22-25ca-3b7c-8c52-7ccfbf9d44e8 | -11.6047 | -50.245 | 2026-08-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e4a5fbea-5667-36bc-bc07-a031bca77c96 | -9.9565 | -46.22 | 2026-08-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2896c5ba-873e-3ef7-a4a2-9daa9ce61bc2 | -7.3873 | -45.0643 | 2026-08-03 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4cce4a17-e7da-3cf4-a0e6-b78577227a34 | -6.5697 | -55.176 | 2026-08-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1907032f-93de-350b-a08c-b32f5fba5aee | -11.6047 | -50.245 | 2026-08-03 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2cd88424-9212-31b7-a907-3550ee84a1d3 | -6.5699 | -55.156 | 2026-08-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 70dc40aa-bba4-3165-8c61-d2b8403ce553 | -6.5512 | -55.1769 | 2026-08-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.3 |
| d5af53ae-1ea1-3ec1-8440-9a6250bb8eea | -9.9565 | -46.22 | 2026-08-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8c3750f3-cc58-3806-b8b8-3ee1c6c67d5f | -3.1735 | -43.5365 | 2026-08-03 14:30:00 | GOES-19 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a6f8b010-7dfe-3c3b-80b7-8953ed676eab | -7.3873 | -45.0643 | 2026-08-03 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e551f27d-237a-303e-a5fb-c2f86d10adb4 | -2.9581 | -50.3569 | 2026-08-03 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ea0d9d00-0d58-36d3-8e92-2521adce857d | -6.5957 | -45.4275 | 2026-08-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 76834a72-3b2a-3596-8c73-141d2ec8d8df | -6.5514 | -55.1569 | 2026-08-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| cd395067-be62-32ff-84e4-345c556baacf | -10.6316 | -46.7451 | 2026-08-03 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d908a0ae-0fed-3cd9-adb1-65ba4caabe8e | -3.1158 | -47.9232 | 2026-08-03 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cde8ab95-1b89-3c17-bfbc-0a8c5f4ddbb4 | -14.2692 | -45.2403 | 2026-08-03 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 148f951a-a308-3243-9987-05af62421782 | -14.2687 | -45.2636 | 2026-08-03 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| f19b3f96-e7e0-34db-ab9a-2ac8dcb0a080 | -12.4594 | -50.4009 | 2026-08-03 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3c6635f9-6160-3672-b6f0-7e3af93c126f | -1.6591 | -54.4543 | 2026-08-03 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ba368685-4209-39f6-9ef2-4221d2eb0e40 | -6.0131 | -47.8648 | 2026-08-03 14:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4e05b8a1-a7ca-303a-b2ba-e33758c40885 | -6.5512 | -55.1769 | 2026-08-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 69606972-3d20-3d60-8592-6f67258d7a80 | -1.6408 | -54.4545 | 2026-08-03 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 240f61c8-505f-3fb0-84dc-64065d91756d | -2.9581 | -50.3569 | 2026-08-03 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 25a56be1-cf37-3ae7-9e5a-f8001d3e7c02 | -9.9375 | -46.2222 | 2026-08-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 94289c9b-07ea-3dcc-9608-7dd4f721ace0 | -6.1485 | -45.2137 | 2026-08-03 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9978a55b-8bfb-3b77-a372-c34df94b7d93 | -6.5957 | -45.4275 | 2026-08-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a7eec407-4a11-33c8-a615-0a4c71cd8e2a | -6.5514 | -55.1569 | 2026-08-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| ce6d37f3-3b74-3cba-9962-ea5592cf4270 | -6.5699 | -55.156 | 2026-08-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| db9ad8bb-2505-3a98-8583-40f22e57f142 | -9.9565 | -46.22 | 2026-08-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 84e4ed26-7e88-3542-b535-6e08a7fa3c89 | -6.5697 | -55.176 | 2026-08-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| ae482f24-b4fa-3f35-9504-79e50df8ee97 | -3.1158 | -47.9232 | 2026-08-03 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 977b3210-6075-3ff4-8fd6-268987076448 | -7.9721 | -44.9169 | 2026-08-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 26be3cdd-0953-3aad-9855-80adc26979ea | -2.9581 | -50.3359 | 2026-08-03 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a3c3f2cc-62d8-37e2-a8d3-8ba9ab4663ae | -7.3873 | -45.0643 | 2026-08-03 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9a26ff86-bc3a-3754-902f-42991579cda0 | -6.5514 | -55.1569 | 2026-08-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 5ee03614-a6fd-3544-ba94-0586417931df | -6.5699 | -55.156 | 2026-08-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 41ba9055-143c-3754-b956-ca9774c2aad0 | -2.9581 | -50.3569 | 2026-08-03 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 585e419a-9d9b-3714-a8c8-4f62b6d9a20f | -6.5512 | -55.1769 | 2026-08-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| ce909adf-71ee-338f-8028-ea4e69c0ee1e | -9.9375 | -46.2222 | 2026-08-03 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1661fcd1-0b2c-3e32-85d2-861204e56c90 | -6.5957 | -45.4275 | 2026-08-03 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 0a83af0f-d31b-38d9-aae6-e150060fb38b | -2.9581 | -50.3359 | 2026-08-03 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c95a1e37-56c1-30e4-a59f-b79dd3bffe15 | -7.9721 | -44.9169 | 2026-08-03 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 563.4 |
| 49ecb966-e877-334e-8d37-58ce7cde8c4f | -14.2687 | -45.2636 | 2026-08-03 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e4b76c0f-e8c7-38a6-b6a7-9dbc379efdb3 | -3.1158 | -47.9232 | 2026-08-03 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| dc453ac6-5a67-304f-8638-a0b529e276c7 | -6.5697 | -55.176 | 2026-08-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| df99e067-f128-3525-9201-d605ab297e12 | -6.1485 | -45.2137 | 2026-08-03 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f0e9b4a7-0832-333c-8530-7dad28224bc1 | -1.6591 | -54.4543 | 2026-08-03 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 46b77c64-077c-3c9c-80be-5843da4c13ab | -11.6047 | -50.245 | 2026-08-03 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| a4a6fb91-678a-3d47-a7b3-025fe84680f1 | -9.9568 | -46.1974 | 2026-08-03 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f17aa15b-dedd-3c50-a378-62d3fd8aeb22 | -5.9442 | -45.0477 | 2026-08-03 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 972c39e8-cb73-3386-a4b6-d812a164d3e5 | -7.9532 | -44.9188 | 2026-08-03 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 6fad2274-a0ea-3b68-a6e8-d76b6ebab30a | -9.9565 | -46.22 | 2026-08-03 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| f7c844dc-b3d7-3f57-a5a6-5c4503c49ba5 | -7.9721 | -44.9169 | 2026-08-03 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 5b4dd107-9381-3e71-8b8e-9eedb0e152b7 | -11.6047 | -50.245 | 2026-08-03 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fdd24572-f576-340e-bbbc-a13dac3d99a0 | -6.5514 | -55.1569 | 2026-08-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 29c25844-ee06-3367-8a9e-c1b6ee31c2cd | -6.1485 | -45.2137 | 2026-08-03 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c66e766c-b5e1-3684-9984-5d7bd477328f | -6.5699 | -55.156 | 2026-08-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| f29737c8-d1ed-303a-8b5e-c5fb09043781 | -3.1158 | -47.9232 | 2026-08-03 15:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 80c0c6d5-50ed-3bc2-86cf-c4f454740fbe | -10.6312 | -46.7675 | 2026-08-03 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 214affbd-c311-33ac-8b21-c877e9afd742 | -6.5697 | -55.176 | 2026-08-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| b21e1ac3-1146-3cc2-b290-2237ff8d052f | -6.5957 | -45.4275 | 2026-08-03 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 027705eb-7b8f-3975-9fbd-1b0997de069d | -2.9581 | -50.3569 | 2026-08-03 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |


[Clique aqui para ver as próximas entradas](README12.md)
