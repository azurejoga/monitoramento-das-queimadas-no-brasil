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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 850464df-15a4-3646-a9bc-f600788d025f | 2.67638 | -61.0952 | 2025-04-27 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 808f5c4d-c760-3356-9a52-57791d91c220 | 4.35662 | -60.80993 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed243a1e-7255-394d-be34-aaee9b4c2c55 | 3.70286 | -60.04455 | 2025-04-27 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b126267c-1bea-3b6d-ab89-b155201f879c | 2.68308 | -61.09417 | 2025-04-27 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54203ef6-eabc-395a-9d86-f5add1a8478e | 2.54205 | -61.33284 | 2025-04-27 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bde0adea-d212-3f6e-8f2b-2fed07f2b48f | 2.67973 | -61.09468 | 2025-04-27 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25b72897-406b-39ac-9755-4b98eb8be551 | 2.42168 | -61.67378 | 2025-04-27 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34daac51-afae-3e63-a987-528145f39266 | 4.35772 | -60.81699 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5f17dfb-a813-39c1-9a57-3d3d5efc0a89 | 4.36447 | -60.79411 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12efa3f2-a6b2-3e85-9912-2699d7010972 | 4.35942 | -60.80583 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6edad161-b628-35fc-ab0b-cbb0b7e76567 | 4.36052 | -60.8129 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b8afb1c-8c07-3040-9e0c-8a2f923f2905 | -11.3963 | -52.9477 | 2025-04-27 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b4242977-4350-3e88-9186-dee710ece2b9 | -9.93085 | -59.90311 | 2025-04-27 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9ed3c29-6bd4-3a29-bc15-e049386314d0 | -11.39784 | -52.95192 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48f7f2fd-4db3-3b1e-b179-ae8565cad22e | -9.92356 | -59.92744 | 2025-04-27 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2076da28-d587-3116-a4ee-3f942366b8e3 | -9.22542 | -60.33858 | 2025-04-27 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 414727e8-0dbf-3468-a73f-7180ff708070 | -11.39833 | -52.9479 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bc78a8d0-14e9-367d-aecf-fd4d0b4bc516 | -11.40991 | -52.94917 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 60b8a83a-7e7e-344c-b2b9-0533f27acbf5 | -9.22191 | -60.33806 | 2025-04-27 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 61ca0ed3-fafe-3690-9dca-d585873d2b7b | -11.39305 | -52.94312 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d8db58f-9b1d-3be0-960f-120ee981dac8 | -11.39883 | -52.94384 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a9f70f56-c1f6-3d22-8841-82cd95ed38b3 | -11.27488 | -52.47058 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad761c2a-53fd-330b-8417-9bb244ff2f7d | -11.39933 | -52.93971 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f43e5217-2dc3-30d0-8a11-ffc2556517f5 | -11.40313 | -52.9566 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 357c93d7-c093-322b-a8de-0ab936c2ef29 | -11.2754 | -52.46633 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128b7518-86c7-3a85-a2e7-6557398162ee | -11.40411 | -52.94859 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf55c8cd-771e-3058-81f7-a70490e195d9 | -11.40362 | -52.95262 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f8fcbe50-ce50-3f53-9ba6-9b81bfb9a014 | -11.39355 | -52.939 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1c5f9b09-87c2-3e95-ad83-562b41bf68e6 | -11.40461 | -52.94451 | 2025-04-27 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 505a3b58-a722-3cbc-9e8e-dffc53e3820d | -6.5631 | -51.1126 | 2025-04-27 05:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bb6a72a0-f72c-33ab-ab75-0465c64ad15d | -11.3963 | -52.9477 | 2025-04-27 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6631e67d-2b02-3b01-9a33-f13d3b668eaf | 2.68218 | -61.09399 | 2025-04-27 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83fb16a-65ad-3659-ac1e-67e143546d49 | 2.4225 | -61.67231 | 2025-04-27 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd16a6a1-ec9d-33bd-854e-4036d247bb27 | 2.41973 | -61.67513 | 2025-04-27 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f83fae18-f768-3089-b910-c31c26aa1287 | 4.3593 | -60.81399 | 2025-04-27 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d765ce5a-66cc-3cfa-b550-e5f6e3700173 | 2.6781 | -61.09469 | 2025-04-27 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97965bdb-d5e3-3e9f-8f46-2a2dff4120f1 | 4.3587 | -60.8104 | 2025-04-27 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7ffd3aa-0b79-32c3-a849-79470af59ff1 | -9.22382 | -60.33722 | 2025-04-27 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 08b8f3a0-33fa-350a-a4bd-6d0c36c57127 | -9.22342 | -60.34035 | 2025-04-27 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6b0fe1c-96ba-350f-aead-cbfb796a3e5f | -9.92274 | -59.92709 | 2025-04-27 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bfbf5e6-5cbc-37e5-a98e-809601befffd | -9.22195 | -60.33719 | 2025-04-27 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91a2edcc-5a8b-37c2-ae2b-6a5681b0b1cb | -9.22152 | -60.3403 | 2025-04-27 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f327c01-eae8-3712-accb-74d667ae18d4 | -6.5631 | -51.1126 | 2025-04-27 06:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0a793cf6-cd10-3c7f-bfde-e7b4d88b41dd | -11.3963 | -52.9477 | 2025-04-27 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f8b29b43-77e7-308f-a46e-5c553513e8d4 | -11.3963 | -52.9477 | 2025-04-27 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d8de34a2-f74a-358a-a4a6-1487173f1f71 | -11.3963 | -52.9477 | 2025-04-27 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 518f0b29-a870-3148-a679-215ba5fdece5 | -11.3963 | -52.9477 | 2025-04-27 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d866b775-6adb-32ef-989a-15dd9ef1a694 | -6.5631 | -51.1126 | 2025-04-27 06:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d80ab289-1341-307b-86be-0a5611555e3e | -11.3963 | -52.9477 | 2025-04-27 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 9d19c31e-ae46-3863-9891-cd7ab84390ae | -11.3963 | -52.9477 | 2025-04-27 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d7514d0b-e25a-3121-a38b-476148cf93bf | -11.3963 | -52.9477 | 2025-04-27 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| ec81d06e-5024-3d58-9663-8b42c12916ef | -11.3963 | -52.9477 | 2025-04-27 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| df434099-0b9d-3f75-a8b7-b4c3376267b2 | -11.3963 | -52.9477 | 2025-04-27 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 6aa0feb6-68df-367a-b00a-d588896fbada | -6.5631 | -51.1126 | 2025-04-27 07:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7e9e698f-7a63-35db-ae4f-8a613fe11cec | -11.3963 | -52.9477 | 2025-04-27 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 015a9634-7645-3357-810d-f9af431d06d3 | -11.3963 | -52.9477 | 2025-04-27 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 0427cc94-8c16-353e-a621-fcc231a3b092 | -11.3963 | -52.9477 | 2025-04-27 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2163a11a-4357-33c7-b8bd-f3c6db5424ff | -11.3963 | -52.9477 | 2025-04-27 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| aca888e0-4e13-3a12-a17a-bd917116ea6c | -11.3963 | -52.9477 | 2025-04-27 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fbb9a5d4-0887-34d5-a147-b8521f2b01f9 | -11.3963 | -52.9477 | 2025-04-27 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3649b9e2-0487-3008-af9e-c9c35246c70b | -11.3963 | -52.9477 | 2025-04-27 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7fda7bf9-6766-3b8f-bab7-699e56d0d4a1 | -11.3963 | -52.9477 | 2025-04-27 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 43217229-f2d8-3598-af68-ffae01c6ef95 | -11.3963 | -52.9477 | 2025-04-27 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f5edd87c-8149-3f7b-ab65-7dfe60e3a011 | -4.82736 | -37.898 | 2025-04-27 11:55:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 81da4a62-cf34-3077-b643-6724d9ebfa04 | -4.8261 | -37.9068 | 2025-04-27 11:55:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 7bbf8b24-7f0e-3054-8dc3-8accf1670397 | -4.99386 | -37.96059 | 2025-04-27 11:55:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b902bc44-7c3b-3569-9858-acd20123b328 | -11.82975 | -42.11435 | 2025-04-27 11:57:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9ad4530d-01dd-3e91-b0dc-791bf7569dbc | -10.06581 | -37.36862 | 2025-04-27 11:57:00 | TERRA_M-M | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 323a9906-d99e-308d-94d2-0d684d0ad861 | -9.20042 | -37.75684 | 2025-04-27 11:57:00 | TERRA_M-M | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 8d1ca64b-3731-347f-ab6e-d1e4cb3061d7 | -9.77445 | -36.8847 | 2025-04-27 11:57:00 | TERRA_M-M | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9d0e3d43-248f-3dad-a206-15536bc75b5d | -12.4091 | -40.46935 | 2025-04-27 11:57:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7c74bfe6-d6e5-3687-9c31-ca258e116132 | -9.29046 | -40.58659 | 2025-04-27 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fe78f61e-b608-399a-9eb8-b09e938c71ef | -9.77591 | -36.87426 | 2025-04-27 11:57:00 | TERRA_M-M | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c93a93ae-dedf-33fe-874f-71e77ec8eb33 | -9.19913 | -37.76616 | 2025-04-27 11:57:00 | TERRA_M-M | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 9.0 |
| dc5fec7d-0542-30ae-8bb0-8487b2169c31 | -8.48421 | -44.47619 | 2025-04-27 11:57:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 14202b8b-61af-38bb-811e-60fc1a77da87 | -14.78656 | -39.04886 | 2025-04-27 12:00:00 | TERRA_M-T | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6614d92d-63e6-3c58-9e38-e20624fd77f3 | -10.3109 | -38.5901 | 2025-04-27 14:20:00 | GOES-19 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 24ed44d3-670e-3ad4-b1d8-4f904109cc8f | -10.3109 | -38.5901 | 2025-04-27 14:40:00 | GOES-19 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 94.4 |


