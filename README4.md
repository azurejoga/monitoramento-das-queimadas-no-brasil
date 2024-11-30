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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75b81d81-d109-3837-a6c2-d4764a288076 | -1.2556 | -54.5589 | 2024-11-30 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| ad323f0d-3a6a-3bb6-afa5-9553fe589f0c | -4.8525 | -41.2928 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| 389ede7b-d0be-3f84-94a9-b0f521c14ce2 | -3.4975 | -53.8137 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 25c1edec-0603-3186-b495-8544405df85d | -1.6938 | -46.7833 | 2024-11-30 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 3cd9008f-220c-3530-9b61-12caacf2a0a3 | -9.8359 | -36.1958 | 2024-11-30 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| 3e6150a7-0e12-30df-ac8f-cb42f7c6f58e | -2.8304 | -45.2845 | 2024-11-30 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ffb0422c-4c77-3bb2-8550-d7710d78246b | -1.4379 | -55.2335 | 2024-11-30 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 69936c82-a5f7-3ba6-9de3-2fd78c643699 | -3.9699 | -41.5176 | 2024-11-30 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| 827a7675-73d9-3153-81ec-0d7d0d206c64 | -4.6237 | -47.0069 | 2024-11-30 00:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 230.0 |
| a162b9ce-1b7e-354a-8fd3-611ccae70228 | -3.4976 | -53.7935 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 2d01743a-c5ba-3888-8b3d-6118c0b343dd | -3.2396 | -53.9216 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3c79f5af-fd3d-30b5-88f8-5d66c2f0e0ad | -6.0862 | -48.0339 | 2024-11-30 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fc62a6e8-7fbf-3622-a9f8-f1ba56ce402b | -17.6654 | -57.5645 | 2024-11-30 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| aa7f63aa-7018-3bc4-ab43-d9f8efa23dd5 | -2.5216 | -48.4591 | 2024-11-30 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0dbc2e9c-45f5-37ce-a3bf-98bc2deb66b8 | -1.0733 | -53.6378 | 2024-11-30 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9d233116-59db-3b1c-83fe-a4163255e7a6 | -4.8525 | -41.2928 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 297.2 |
| 2bbe17f9-90e8-3c10-af75-9db9e5fbd7de | -4.8901 | -41.2902 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1154.8 |
| 57c6a501-b6c1-3eba-947c-d828d118f06c | -1.2739 | -54.5587 | 2024-11-30 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 7eed978a-9fcf-37a4-97dd-9367c8cd979c | -1.2556 | -54.5589 | 2024-11-30 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4aa642e2-cbab-3b53-bf3d-476d0c21dec5 | -3.1481 | -53.8233 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8af7378f-8ee4-3fcb-bbf9-c1df8244444e | -4.8523 | -41.317 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 195.1 |
| 704b035f-a5ec-3087-8f8d-2b14a40b0a46 | -1.4379 | -55.2533 | 2024-11-30 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8bd8d98e-7d3c-3a87-85b3-6a217adf0d8a | -4.6238 | -46.9849 | 2024-11-30 00:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 1d4a9a7c-e806-3e2f-a0dd-be175c3d1f3c | -1.4379 | -55.2335 | 2024-11-30 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c3196ece-8317-39e9-b696-829ef425033b | -3.2591 | -53.6186 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1d6ac2cc-a9dd-358d-8f0f-9827b6ddefe0 | -3.9888 | -41.4925 | 2024-11-30 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| e76e527b-1a1d-3229-9c0c-00a83844fbc3 | -17.6457 | -57.5668 | 2024-11-30 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 0b1777c0-22c9-3ea0-9d51-9a8b76ce33b7 | -3.9699 | -41.5176 | 2024-11-30 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| 91c73a1c-8ba1-361d-94a4-2c19d9d0f5d5 | -4.8899 | -41.3143 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 533.9 |
| 497a6a77-c24b-3c41-8758-2f22d4b974a8 | -3.7021 | -45.6764 | 2024-11-30 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 37507139-96b7-3db8-a2fc-ec9e969d9eb5 | -6.9156 | -43.5418 | 2024-11-30 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 394.5 |
| b1080120-35e6-3c32-bd58-21c0fa94a1da | -3.4975 | -53.8137 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 730f986a-29a1-3c4f-8853-f2624d95a0b2 | -4.6051 | -47.0079 | 2024-11-30 00:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 362.1 |
| b6564934-92bb-396e-9c04-629681fde225 | -6.8965 | -43.5669 | 2024-11-30 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| aa11a022-1ab1-34bf-a23e-8675a86c2992 | -6.086 | -48.0557 | 2024-11-30 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4e7515da-91b8-3a04-bcc8-632d91753ce0 | -3.148 | -53.8434 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2cf554c7-7bea-3074-a227-c0a4a5128b33 | -3.9886 | -41.5165 | 2024-11-30 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 160.6 |
| e5a16ba1-b20a-33ac-9ea9-00397daabcff | -4.6237 | -47.0069 | 2024-11-30 00:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 290.0 |
| 15f0e755-e1f9-38ee-8424-cc5690182b7a | -1.6419 | -53.8731 | 2024-11-30 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c19b1bc8-73e0-364c-abc8-ae6e29b448e9 | -1.0022 | -51.7235 | 2024-11-30 00:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b658c844-75f9-35b3-a67d-ac1b3a4849f6 | -2.8013 | -53.043 | 2024-11-30 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1ee36cf0-62bd-3464-a885-cb2f0b5971e0 | -3.2406 | -53.6393 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 13c45798-9c5e-30c8-b003-2aa208da326d | -6.9158 | -43.5185 | 2024-11-30 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d9210c3f-adea-34e1-9a47-adb4088e0e1a | -1.2739 | -54.5387 | 2024-11-30 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 24004ccd-47af-32a9-884f-e6511fd76316 | -6.9344 | -43.5401 | 2024-11-30 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5d9c729b-1be0-3687-a056-eb1801011fb0 | -4.6838 | -46.363 | 2024-11-30 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 19fbb7ef-af73-36e8-8ed1-2e08ec81ee5e | -4.8713 | -41.2915 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1751.3 |
| 853c09cd-19a3-338a-be9c-ca4759ebcb9f | -6.1591 | -35.2638 | 2024-11-30 00:50:00 | GOES-16 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 2dc22a01-eb17-38d0-bdca-ad206c8a17af | -6.8967 | -43.5436 | 2024-11-30 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 42cc4aa5-0b85-341c-9595-07f4dee38061 | -4.8903 | -41.266 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 250.0 |
| 5029e533-66c8-3d39-8b8e-c5f180f1b81c | -3.4792 | -53.7941 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 439f5eaa-51e9-34cf-adc8-01021dff4b97 | -6.1588 | -35.2911 | 2024-11-30 00:50:00 | GOES-16 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| 98d34c4a-82a4-30c1-ac27-aede076249d1 | -4.8715 | -41.2674 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 469.1 |
| 01de4ca6-c890-3d39-8e73-ff9dcfc526a4 | -4.8527 | -41.2687 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| fbc5649a-4200-32c8-9b92-f5761542a812 | -3.259 | -53.6388 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 3927b7d8-6fd4-364f-91e2-12205e3de5ee | -3.3998 | -50.6573 | 2024-11-30 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| faf3ac95-d9b1-31fe-b71e-42fc45da0736 | -6.9153 | -43.5652 | 2024-11-30 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 182.9 |
| acc7760e-fc21-350b-ba48-6e888e7a325b | -1.2556 | -54.5389 | 2024-11-30 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 16d9ed8a-bf84-3415-8fba-96e3d7d551b6 | -1.6753 | -46.7836 | 2024-11-30 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6ea954cf-3ecc-3054-8773-63af4a98b433 | -4.6052 | -46.9859 | 2024-11-30 00:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 8be9d564-0c6b-3139-af6b-cd7a62c08a74 | -3.4791 | -53.8142 | 2024-11-30 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 4fcd87f5-ea0b-3547-b857-185b82c7e8a7 | -17.6651 | -57.585 | 2024-11-30 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| d06f047b-2eca-3233-a776-80524a4fed6c | -2.5963 | -53.9771 | 2024-11-30 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 657dbad9-dc7a-381b-862f-360149650bda | -1.3333 | -51.6788 | 2024-11-30 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb537a95-a1a7-3f0d-8af5-20bf834a70c7 | -1.6963 | -45.7864 | 2024-11-30 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| db3f899d-7352-36fa-b937-1b9acb2bc8fd | -4.8711 | -41.3157 | 2024-11-30 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 827.9 |
| 7ba22da7-c4e3-3b25-b8ab-109f3e14f63e | -1.6938 | -46.7833 | 2024-11-30 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| ac2808c2-e080-34e5-8725-688213826a06 | -1.2739 | -54.5587 | 2024-11-30 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 11ff4d84-df65-33cd-84fc-7c33c6b8722d | -3.259 | -53.6388 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| b1534b9a-074c-33c6-8888-e9cf42e8f8fd | -6.9153 | -43.5652 | 2024-11-30 01:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 9ebb206b-6076-31cd-953e-f9d2aa3fbcb4 | -4.8709 | -41.3398 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 9f1a09d5-8800-3131-aef2-bf704162af62 | -4.6237 | -47.0069 | 2024-11-30 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 154.1 |
| b99b6b38-6dda-395b-9013-695020cd5e7b | -4.8713 | -41.2915 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1667.6 |
| 20ba4270-b739-3aaf-9802-54b3fa4ebf6d | -3.4976 | -53.7935 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d488d1df-ea8c-3171-a4ef-30672dd5e5f3 | -3.2406 | -53.6393 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b2ec10c0-d067-3007-a5a6-3d26dbc3033d | -3.9888 | -41.4925 | 2024-11-30 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 426fe0df-76af-3762-b873-0a7e9fb81de9 | -6.9156 | -43.5418 | 2024-11-30 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 521.8 |
| 2d8922f3-d039-3e59-bf0f-90dbcf9b9edc | -4.6051 | -47.0079 | 2024-11-30 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 237.8 |
| 179c9696-f017-369d-9246-f7e72025b2ab | -2.5216 | -48.4591 | 2024-11-30 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 73c10c3f-fcb9-32b5-9de5-f9c61ea2a3c9 | -6.0676 | -48.0352 | 2024-11-30 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 651593f1-5755-32f7-8c97-77bb1967228e | -2.614 | -54.2177 | 2024-11-30 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 50f9c595-817b-36ea-a349-b429216c24ac | -3.148 | -53.8434 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 64eaad84-47f4-3915-b7bf-1867b9eee558 | -2.5963 | -53.9771 | 2024-11-30 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 49f7ec6f-73de-3112-bb6e-1b2bdca7c74c | -4.8525 | -41.2928 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 317.0 |
| 4a4b9c10-b993-36a9-a406-f3b53e5c1171 | -1.3271 | -55.8475 | 2024-11-30 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f92171be-5d04-307d-aa89-dd80ad4d5d54 | -6.086 | -48.0557 | 2024-11-30 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7aa30eea-f11b-35de-896c-ef5702ecdaf8 | -1.4379 | -55.2533 | 2024-11-30 01:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2a4c222f-6379-3e08-8b68-53d317b4f195 | -3.7021 | -45.6764 | 2024-11-30 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3d61370e-0681-3331-9d92-54eec110e488 | -1.6419 | -53.8731 | 2024-11-30 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a79bc413-ec5e-3e41-a015-db344ba30bfe | -17.6654 | -57.5645 | 2024-11-30 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| 32ea0dce-23e1-3d4a-981a-9a4f251d4981 | -3.97 | -41.4935 | 2024-11-30 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 85f762d5-c6ab-39eb-9e48-6fef677b70f8 | -3.9886 | -41.5165 | 2024-11-30 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 135.9 |
| b922d08a-ace5-3e63-825d-84d87367a9c8 | -3.2591 | -53.6186 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f00c9063-daf5-33c0-92d6-5a2cfef03f8c | -4.834 | -41.27 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| ca5ae4f6-145d-3f38-9615-239a64d305b6 | -4.6238 | -46.9849 | 2024-11-30 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| f4501e6a-e6ee-35f8-bd18-ff26061a6242 | -3.6757 | -47.1395 | 2024-11-30 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3a44b0ac-f843-3b85-9ac7-d65a00656549 | -6.8967 | -43.5436 | 2024-11-30 01:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| bf2906ba-be28-3dfe-a9b9-70f8f74db136 | -3.4791 | -53.8142 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 1986ed23-0865-3039-9f12-0699f8f577d6 | -4.8711 | -41.3157 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 866.4 |
| 5b4223b9-0159-341e-bd3c-791d2189ed73 | -4.8899 | -41.3143 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 498.3 |


[Clique aqui para ver as próximas entradas](README5.md)
