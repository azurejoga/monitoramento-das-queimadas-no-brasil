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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9579cc-b482-390d-8a9a-64e3ac4c774f | -2.2662 | -53.7825 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 37a16804-946e-39b8-a4df-99a2edf61ff8 | -2.2663 | -53.7624 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e0c89057-0802-3218-a198-45d1fcc9b8a0 | -2.2845 | -53.8023 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 329f5148-9159-31ae-8821-d4e13e4ea5c6 | -2.2846 | -53.7822 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| ffad52ad-050a-3091-a973-58a8b38dc933 | -2.2846 | -53.762 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0d04f8e9-715c-335e-88ce-7aac8d46388c | -2.3919 | -48.5484 | 2024-10-28 01:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 70c8e4e0-035f-3707-851a-ab33775e131b | -2.4104 | -48.5479 | 2024-10-28 01:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 08c68fe2-3ef3-360b-a0f1-0c39d2313e81 | -2.6399 | -51.7374 | 2024-10-28 01:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0b516909-084a-3aa3-af20-45838d20a442 | -2.7033 | -49.33 | 2024-10-28 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| f687db32-9a5f-38a4-9c9f-9f32eab320bd | -2.7034 | -49.3088 | 2024-10-28 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c2d7667b-4492-3c21-af1e-567dbaf41f9f | -2.7219 | -49.3083 | 2024-10-28 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c11ea022-5bf7-3007-b21a-8bb9269fbe27 | -2.8555 | -53.3459 | 2024-10-28 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 47aada5b-a8b7-3f76-a1bd-c9807625e7dd | -2.8556 | -53.3256 | 2024-10-28 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 4c66b7b5-e347-3397-82d5-9172f733618b | -3.0538 | -49.4895 | 2024-10-28 01:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a7abbb46-c7e7-364a-9cd0-26c782d51cad | -3.272 | -46.2072 | 2024-10-28 01:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| edb4d8d9-46ca-350a-ae2e-b5e00fc9e8b6 | -3.4014 | -46.3131 | 2024-10-28 01:55:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c5c517f4-d28a-35c9-82aa-ec7deadb9a40 | -4.0681 | -50.024 | 2024-10-28 01:55:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 45a68a70-162e-3646-abab-26b71e22ab51 | -4.2796 | -45.5587 | 2024-10-28 01:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c3a21c88-8512-30db-9b2e-6694dba9a59d | -4.2797 | -45.5362 | 2024-10-28 01:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 257.7 |
| f95be918-6e61-337b-b066-7c48231aed14 | -4.2799 | -45.5138 | 2024-10-28 01:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 229c37d3-27ec-36c4-b89e-57afade7a1dd | -4.1771 | -44.1109 | 2024-10-28 01:55:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 60bfaf1e-128d-3168-95a9-f940037a25ba | -4.4094 | -45.6416 | 2024-10-28 01:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cbbb54d1-81ab-3c24-af5b-cd2091448b13 | -4.428 | -45.6406 | 2024-10-28 01:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 23e430ac-fd42-340a-a0ab-634cc0bad281 | -4.7766 | -46.4022 | 2024-10-28 01:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 937293ea-d400-3b69-b249-8218c73fc7f3 | -4.7768 | -46.3801 | 2024-10-28 01:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 45293854-9f46-36a0-9989-51eb34135345 | -9.4323 | -44.4803 | 2024-10-28 01:55:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| efbc3365-6765-342e-a8e6-63df3a5beb1e | -9.4512 | -44.478 | 2024-10-28 01:55:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d24a5421-2fd3-3e37-b5ba-11cd8f7f7afc | -1.1836 | -53.5158 | 2024-10-28 02:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a5ba77e5-109c-3b55-9012-4b180ce428fc | -1.1836 | -53.4956 | 2024-10-28 02:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ebc44b07-11ab-387a-88b6-c87e88c63b99 | -1.5349 | -52.0874 | 2024-10-28 02:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c134ecab-965a-3205-8783-f3f2dbd56c3d | -1.5532 | -52.1076 | 2024-10-28 02:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| cd193546-fcce-3656-92ca-8b9042c50574 | -1.5533 | -52.0871 | 2024-10-28 02:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7deb6204-716a-3a65-8381-e2e9d8164f2a | -1.9763 | -52.0804 | 2024-10-28 02:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2f015baa-015d-3f8e-bcdf-5f875a250702 | -2.0499 | -52.0791 | 2024-10-28 02:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 91803bf6-78e1-38cb-bfca-afbe070a1e05 | -2.2662 | -53.8027 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b6aede48-5a2c-3680-86d9-ad4795d448a2 | -2.2662 | -53.7825 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| ac97f512-066a-3fee-aa1a-bc58b2ee0898 | -2.2663 | -53.7624 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 986ffad7-f2c4-37c7-9626-c29cff2e90ae | -2.2845 | -53.8023 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 23175719-725c-33ea-85bd-a98e2ce77aa4 | -2.2846 | -53.7822 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 8b953e0c-a7b0-360f-87fc-ae2432c83a68 | -2.2846 | -53.762 | 2024-10-28 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| dbb5cdf9-2f29-3684-ba8d-ab70ca4012c8 | -2.3919 | -48.5484 | 2024-10-28 02:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a3fc4531-3a5f-348c-9b27-e931d51e7e1e | -2.4104 | -48.5479 | 2024-10-28 02:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 27924f9d-4430-3a0a-a34c-ac3c98a4e2b9 | -2.7219 | -49.3083 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 0a29fdc8-3d1c-3ae7-8121-b2a3f4520c5a | -2.8145 | -49.2418 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7e02bf20-addc-3448-8270-bb9270258a30 | -2.833 | -49.2413 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 77468986-6c78-3aab-8e17-3aa340b19745 | -2.8514 | -49.262 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6ea4fa44-ea70-3b2c-abac-06bbad19e169 | -2.8515 | -49.2408 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f7b17411-6322-3853-a1af-3bbd894c8638 | -2.7034 | -49.3088 | 2024-10-28 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0a35bf72-fe95-3c94-9cce-fde600bd3862 | -2.8556 | -53.3256 | 2024-10-28 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c9fb3ff5-0dea-3442-a7b3-1af9371fb300 | -2.8699 | -49.2615 | 2024-10-28 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3fc17773-9ba4-313d-abfc-7d880f2f83bb | -2.87 | -49.2402 | 2024-10-28 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3b066168-7b81-32b1-8d47-14d994a6bbf6 | -3.0317 | -50.4176 | 2024-10-28 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| bdc4f10b-5177-35be-b6c3-dbca697c9c9d | -3.0538 | -49.4895 | 2024-10-28 02:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8017d685-6a3f-3ad1-a075-c6d78342e9f0 | -4.2797 | -45.5362 | 2024-10-28 02:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 486be9dc-e5b5-3d15-8a8e-09614a044deb | -4.428 | -45.6406 | 2024-10-28 02:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 8ce9b804-a189-3d0a-b468-efadf2f15c7b | -4.4279 | -45.6631 | 2024-10-28 02:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4544e828-337b-34dd-be02-a00b0d739c83 | -4.4094 | -45.6416 | 2024-10-28 02:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e51a59b3-0e67-3342-9348-cfaedfaa6b36 | -4.7768 | -46.3801 | 2024-10-28 02:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 971f9f17-4017-3fa1-b6d9-231ee810aa96 | -4.7766 | -46.4022 | 2024-10-28 02:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 3de36e4b-1ffc-3182-b89e-f28a29533854 | -9.4323 | -44.4803 | 2024-10-28 02:05:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 4fc942e9-a282-3ebb-8129-3657c1e9e5d3 | -9.4512 | -44.478 | 2024-10-28 02:05:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| ea1abd1a-3169-3f68-a5e2-b311e7bc0ce1 | -1.1836 | -53.4956 | 2024-10-28 02:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 93467e3a-b20c-3b2f-8cef-20e9506d5fee | -1.9763 | -52.0804 | 2024-10-28 02:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| f7866693-f97c-36dc-a429-dc6241f754c6 | -2.2662 | -53.7825 | 2024-10-28 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 4e0abbe3-7684-3197-af26-e767e9e55024 | -2.2663 | -53.7624 | 2024-10-28 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 10967f38-6ff4-3f96-b912-416a89ec44e0 | -2.2845 | -53.8023 | 2024-10-28 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a8e37f42-6329-3aad-afca-dddab7bc76d3 | -2.2846 | -53.7822 | 2024-10-28 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| d9448fcb-f482-382a-b96a-3e18fb3d1151 | -2.2662 | -53.8027 | 2024-10-28 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7d66fc7b-5c8f-397a-8b0d-55b581ba921b | -2.3919 | -48.5484 | 2024-10-28 02:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 87ae1c57-a59f-3a45-a965-95865ddff1a5 | -2.4104 | -48.5479 | 2024-10-28 02:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 64bc1d7f-e69d-363d-bbeb-0a51e9bf5260 | -2.6399 | -51.7374 | 2024-10-28 02:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 16a581e1-7911-3f80-a4e4-7645a1f3cef2 | -2.7034 | -49.3088 | 2024-10-28 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 18cfaf61-88ae-3a13-a57c-1acb53fefe61 | -2.8145 | -49.2418 | 2024-10-28 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 44cbf7e5-9d50-32d6-b3d3-9633363ab09a | -2.833 | -49.2413 | 2024-10-28 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5de0be32-fcf0-320a-ac0f-5dce8def95cc | -2.8514 | -49.262 | 2024-10-28 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 34b49816-c346-30fb-895b-372b24489799 | -2.8515 | -49.2408 | 2024-10-28 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d9d320ab-15c2-3a29-a560-b94efe92b14d | -2.8556 | -53.3256 | 2024-10-28 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 88340bb5-430e-394f-95c2-4357116c61f8 | -2.8699 | -49.2615 | 2024-10-28 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8905b009-8593-3667-87cc-ca17a03a33ef | -2.87 | -49.2402 | 2024-10-28 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 19fe80b3-ce11-3d64-929f-0304ba483f4e | -3.0317 | -50.4176 | 2024-10-28 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1923df01-e1de-39fc-b0a3-e3350793254c | -3.0538 | -49.4895 | 2024-10-28 02:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 622c2653-3fff-391c-b7d4-a7c84dec7f61 | -4.2797 | -45.5362 | 2024-10-28 02:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0911a344-5417-3abe-95cb-c81c3de9c79e | -4.428 | -45.6406 | 2024-10-28 02:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 71376436-6ce9-362b-88d3-32d7e2b06d24 | -4.4279 | -45.6631 | 2024-10-28 02:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1aa3af00-2a6d-3399-814c-64706ab5f2c5 | -4.4094 | -45.6416 | 2024-10-28 02:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 48c68aa0-e043-3a30-9469-a3c24b65909a | -4.7766 | -46.4022 | 2024-10-28 02:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 95d1c9b7-a72f-3b5f-98f7-859da6b48e89 | -9.4323 | -44.4803 | 2024-10-28 02:15:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8321169f-23de-35e2-885f-1468c561ff1b | -9.4512 | -44.478 | 2024-10-28 02:15:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0ff36006-66a5-3979-b325-cb268558178e | -1.1836 | -53.4956 | 2024-10-28 02:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fc08ee34-75cd-371b-aaa2-1b42408f21cf | -2.0499 | -52.0791 | 2024-10-28 02:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 798a4292-9527-37d8-939c-6cdf57181637 | -2.2662 | -53.8027 | 2024-10-28 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a5551a66-357d-3306-9083-7872fa0a3c53 | -2.2662 | -53.7825 | 2024-10-28 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| ab1d2f48-1d20-3f33-8c39-0bea62a9b4a9 | -2.2663 | -53.7624 | 2024-10-28 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2fd54603-41d6-30fc-b175-4df08b076daf | -2.2845 | -53.8023 | 2024-10-28 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7d5da2ec-2e2a-3a91-a158-350403e7b87e | -2.2846 | -53.7822 | 2024-10-28 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| a4182602-359b-3222-aff1-3329e3393db1 | -2.3919 | -48.5484 | 2024-10-28 02:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| dc08ac91-d537-3777-9f38-f97725555c17 | -2.4104 | -48.5479 | 2024-10-28 02:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8d29103a-76d3-3331-b83b-eafdcf48d4b1 | -2.8515 | -49.2408 | 2024-10-28 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fc2450a6-a9fb-346d-8e20-5df4df1ca696 | -2.8145 | -49.2418 | 2024-10-28 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1d6f25be-3c13-34f0-b47b-ba03531ba7a1 | -2.833 | -49.2413 | 2024-10-28 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |


[Clique aqui para ver as próximas entradas](README21.md)
