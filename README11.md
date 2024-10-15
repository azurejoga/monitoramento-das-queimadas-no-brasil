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
| 7bf7a5ef-ed35-32ac-97af-97d44bab0115 | -13.1473 | -62.3408 | 2024-10-15 00:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| f0624536-d6e2-3de3-b66f-249973466ff7 | -13.1475 | -62.3215 | 2024-10-15 00:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 178.9 |
| de85a49e-0cd4-3ad4-8d81-6fe579e34a8b | -13.3594 | -61.9789 | 2024-10-15 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8a4dc194-f85c-3582-900f-bdcfe5d8ac02 | -13.3596 | -61.9595 | 2024-10-15 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4a34c649-56a2-3309-b5e4-412c7bc9dde0 | -13.3655 | -61.3376 | 2024-10-15 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 047c7e75-b6f5-3bd9-b203-cad159c893b8 | -13.3786 | -61.9582 | 2024-10-15 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 98123459-b50f-36e0-9af5-c1c43911537c | -13.5136 | -61.7552 | 2024-10-15 00:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8e484ddf-7b2f-3f8d-a2d6-992a55db44bb | -18.8361 | -42.402 | 2024-10-15 00:36:49 | GOES-16 | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| 0729cda7-037a-3bee-a576-15fce00ec487 | -18.8565 | -42.3966 | 2024-10-15 00:36:50 | GOES-16 | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 324f44dd-daf9-3f3c-bb60-4c211d838952 | -1.8577 | -47.8493 | 2024-10-15 00:45:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ac5debbb-e96b-3116-8c2d-00e7f539cba1 | -3.0397 | -53.2603 | 2024-10-15 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6759adf1-35c9-3f72-8b73-ffb5ee4291a5 | -3.1099 | -54.2263 | 2024-10-15 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| fa574f47-d49f-3a8b-98e6-b7d6c760639a | -3.1282 | -54.2459 | 2024-10-15 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ed3a5194-9b1e-3f5c-a54a-1a9643639ddd | -3.1283 | -54.2259 | 2024-10-15 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 2fd5634c-be88-3454-8574-7ae2601b237e | -4.3617 | -47.2835 | 2024-10-15 00:45:30 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| dfcef2cf-bdfa-3378-972b-d1da609085f1 | -4.3774 | -47.7627 | 2024-10-15 00:45:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 385dd8c9-37f0-346e-a8ba-593dcac28969 | -4.3959 | -47.7618 | 2024-10-15 00:45:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f4c80ad4-41e3-363d-80b9-085b516394e0 | -5.1983 | -44.8497 | 2024-10-15 00:45:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| de0b4677-6569-377f-a4d8-71d1672634c5 | -5.217 | -44.8485 | 2024-10-15 00:45:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 2b0cfa7c-3cf2-3b29-9b58-64387a1a43cc | -5.2172 | -44.8258 | 2024-10-15 00:45:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3cac2813-1998-3435-be41-78d8d40c5af4 | -5.2982 | -46.3936 | 2024-10-15 00:45:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 663780d8-9257-38bd-a990-e091d1aca773 | -5.5345 | -47.152 | 2024-10-15 00:45:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d3810fd7-5560-330e-9107-83f38e5e96b3 | -5.5531 | -47.1508 | 2024-10-15 00:45:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 79ea1968-e2b3-3dde-a27f-58cc452bdcec | -6.5505 | -48.2408 | 2024-10-15 00:45:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 45e72c7b-18ba-3208-808d-46fc2ffbde2a | -9.3493 | -63.5846 | 2024-10-15 00:45:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 791d2e43-2bae-314c-958a-7a11663e91f5 | -9.3494 | -63.5658 | 2024-10-15 00:45:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a8ab7732-3184-30b5-9b24-09da78c195bf | -9.5909 | -46.6437 | 2024-10-15 00:46:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 445fc4f9-80fb-3bf7-acf6-f24b33f97f19 | -9.6878 | -46.476 | 2024-10-15 00:46:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f6805228-4625-35a5-94cd-18be67a52dcf | -9.9777 | -47.3795 | 2024-10-15 00:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 94b9bde2-5543-3eda-8d0f-a8a9db359003 | -10.0495 | -47.6589 | 2024-10-15 00:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d10ea01c-ba50-395c-bf98-e5406347afe6 | -10.0415 | -54.3442 | 2024-10-15 00:46:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4305d0a6-1c06-3fd4-b34e-31a871402823 | -10.3524 | -61.1946 | 2024-10-15 00:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d90ba59b-9011-308c-8bce-58b41fb5d816 | -10.3711 | -61.1935 | 2024-10-15 00:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 69b5c770-43e0-3b67-99eb-48b693068434 | -10.3713 | -61.1743 | 2024-10-15 00:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 0b589e8e-96fc-3582-863d-3853d596cbd2 | -10.3898 | -61.1925 | 2024-10-15 00:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4367a56f-73c2-36ab-8310-73280860c429 | -10.822 | -49.256 | 2024-10-15 00:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ad6931f7-4057-30ba-ba58-581674f94917 | -10.8224 | -49.2343 | 2024-10-15 00:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 767a001c-c93e-30dd-be25-ac38468e87e5 | -11.6915 | -65.2432 | 2024-10-15 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2d37c3e1-805c-30f6-92ec-171cdb04a7d7 | -11.6917 | -65.2243 | 2024-10-15 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ae88818a-2d6f-3d5f-9869-22dc7ec3f115 | -12.3793 | -63.7294 | 2024-10-15 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| eb55c579-904d-3bc2-bbfb-a132137ecf3b | -12.3982 | -63.7284 | 2024-10-15 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| f364a6ce-ab3a-3aa6-a470-75e1a32c7b22 | -12.3983 | -63.7093 | 2024-10-15 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 506b35de-1b66-3b13-8d4e-8d5cb0c46e71 | -12.4603 | -63.0169 | 2024-10-15 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| adb237ed-3857-3cac-8d4e-235916c3d522 | -12.4961 | -63.2641 | 2024-10-15 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 20a9add1-6bf5-3c6f-a371-02f3969753e2 | -12.515 | -63.263 | 2024-10-15 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 86b3f8e0-c123-3e31-b478-3176591f001b | -13.2026 | -42.491 | 2024-10-15 00:46:19 | GOES-16 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 8f6e51c7-7604-3d5e-bc76-812840dce248 | -13.2031 | -42.4667 | 2024-10-15 00:46:19 | GOES-16 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 34df05a0-1a26-3377-abd1-c5e4058bcee3 | -12.9538 | -62.7962 | 2024-10-15 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b0ea6260-f495-3264-af87-0a69a235bcd0 | -12.9728 | -62.7951 | 2024-10-15 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 43e01ba7-f9ef-3267-a583-9d9669c80555 | -13.1285 | -62.3227 | 2024-10-15 00:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f7dab49b-b591-3e69-adc7-c9a272bec09b | -13.1287 | -62.3034 | 2024-10-15 00:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f00d9190-1802-38fe-890c-1c00907aaece | -13.1473 | -62.3408 | 2024-10-15 00:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0e4e4496-28ec-386f-96d2-7232210ca588 | -13.1475 | -62.3215 | 2024-10-15 00:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 361953d8-123b-3d45-8bcc-555d5af63068 | -13.3594 | -61.9789 | 2024-10-15 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d431ccf3-2775-3f2c-9bd1-8d3ba68ceb28 | -13.3596 | -61.9595 | 2024-10-15 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e9b3abef-58cd-327a-a349-966af104c0c2 | -13.3655 | -61.3376 | 2024-10-15 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 62ceee9e-f16a-387b-a266-5e88b53a1df9 | -13.3786 | -61.9582 | 2024-10-15 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 110.9 |
| a153b1fa-9141-385e-a12a-57cc042bcc6d | -13.5136 | -61.7552 | 2024-10-15 00:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 247fb236-2dea-3fe4-b290-28c83d356a3b | -1.8577 | -47.8493 | 2024-10-15 00:55:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 7f46b8d6-3254-3f84-afc0-9104344883af | -1.8578 | -47.8276 | 2024-10-15 00:55:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| db93cdf1-5e7c-328a-af80-4f0fc49e5ec6 | -2.4418 | -50.2447 | 2024-10-15 00:55:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| cc0ffc8f-c4ac-3690-b8b6-0aa60a55264d | -2.4419 | -50.2237 | 2024-10-15 00:55:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f9648d33-03c5-321c-b0ff-332cb2e607aa | -3.0397 | -53.2603 | 2024-10-15 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 28553cd3-fe2a-3716-8e7f-7f8f56e08f04 | -3.1099 | -54.2263 | 2024-10-15 00:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 01d46099-d594-3466-a7e1-03e5544214ae | -3.1282 | -54.2459 | 2024-10-15 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d4ebde39-daad-3548-847a-de675249fb7f | -3.1283 | -54.2259 | 2024-10-15 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| acc07438-6204-3b85-8966-38625e634dc3 | -4.3959 | -47.7618 | 2024-10-15 00:55:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c26d2253-7188-3a1e-99a0-ff574ac04bb8 | -5.1983 | -44.8497 | 2024-10-15 00:55:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| e9feda98-8421-3001-a74b-37352024927c | -5.217 | -44.8485 | 2024-10-15 00:55:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 7f72f272-4387-36fb-a20e-08b3f896875b | -5.2172 | -44.8258 | 2024-10-15 00:55:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 32edd3f3-774c-3199-998f-0c71f380b973 | -5.2797 | -46.3725 | 2024-10-15 00:55:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 012bec46-736d-3f6b-b18b-2fa685460140 | -5.2982 | -46.3936 | 2024-10-15 00:55:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3ac588ee-3046-3fe7-ae78-8521618dffbc | -5.5732 | -49.3995 | 2024-10-15 00:55:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e634a2ec-15b4-3f81-96bd-301832ab5746 | -6.3162 | -45.2914 | 2024-10-15 00:55:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| bc4bb82c-4342-35fb-b142-80892cff0389 | -6.3349 | -45.2899 | 2024-10-15 00:55:42 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b260ade7-4328-37e4-8ff7-161729d4b4ec | -6.3351 | -45.2673 | 2024-10-15 00:55:42 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ee25824a-2130-35a6-b722-54c0f0968e59 | -6.5505 | -48.2408 | 2024-10-15 00:55:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4e558484-09df-3474-b0a9-bc1a38ceca5a | -9.6878 | -46.476 | 2024-10-15 00:56:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f6588088-abbf-3a24-9f0a-f95a5cefd0b3 | -10.3524 | -61.1946 | 2024-10-15 00:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7d884696-32d2-34fc-956e-1b054fd7ed12 | -10.3711 | -61.1935 | 2024-10-15 00:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 6a764df3-1e65-3b4d-afb0-c761f0feb51f | -10.3713 | -61.1743 | 2024-10-15 00:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 2a13e38b-0380-367c-9ed9-9aac3ffd8eba | -10.3898 | -61.1925 | 2024-10-15 00:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b96e8dbd-52d8-31b1-b68a-d64add3ddbe3 | -10.822 | -49.256 | 2024-10-15 00:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8d46e388-dc58-348d-b770-14eac90132d5 | -10.8224 | -49.2343 | 2024-10-15 00:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 24449520-d0ee-3fd3-b0e3-090c4bddcbbe | -10.9473 | -54.1037 | 2024-10-15 00:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a3f0a385-63c1-3a3e-81a6-e61282e8a9f0 | -11.6915 | -65.2432 | 2024-10-15 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 104b5da6-9cb0-3025-b48f-29511ec8e50e | -11.6917 | -65.2243 | 2024-10-15 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f3da55b9-d236-3a25-91c0-3a4bd6967bc7 | -12.3793 | -63.7294 | 2024-10-15 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 62a0d38d-8de4-33c5-bdf2-a3cd1cf2ab3b | -12.3982 | -63.7284 | 2024-10-15 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b23011af-38c6-3574-a908-0a3ec0d09f00 | -12.3983 | -63.7093 | 2024-10-15 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 52de2520-fd11-384b-952a-f1ee365a2008 | -12.4603 | -63.0169 | 2024-10-15 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5264fab8-ce5f-3960-8dec-98e4e5256647 | -12.4961 | -63.2641 | 2024-10-15 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c268f1c7-eb45-3f0e-a59c-f5e80d757a20 | -12.515 | -63.263 | 2024-10-15 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.2 |
| b004e035-5871-3f56-93ed-7df4c5bf0774 | -12.889 | -53.5402 | 2024-10-15 00:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 71043ce6-6dad-38c7-8c6c-b13e7101ea0d | -12.9538 | -62.7962 | 2024-10-15 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a0c9dda8-5504-30a4-a3d8-0058743ee2c9 | -12.9728 | -62.7951 | 2024-10-15 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 585b2427-eab2-309b-a5ff-f0cb328c12a2 | -13.1473 | -62.3408 | 2024-10-15 00:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3a829494-21f7-3176-9c9d-fe46727d6a65 | -13.1475 | -62.3215 | 2024-10-15 00:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 410b93eb-bb46-34f1-a126-ab413651b250 | -13.5136 | -61.7552 | 2024-10-15 00:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7fa24b72-6d27-3493-90a7-223853f82f55 | -14.3103 | -53.3342 | 2024-10-15 00:56:27 | GOES-16 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |


[Clique aqui para ver as próximas entradas](README12.md)
