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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cacaf3f-4c93-33ad-b8b7-41fdc0b34698 | 0.89462 | -59.54188 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08a16db0-1e62-331f-af0d-d3336164f1aa | 0.87246 | -59.5141 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aee67fc2-4fdf-3a9c-a068-622d1881a57c | 1.06592 | -59.40779 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca2b7677-b0d1-3e90-815a-75cb730fd905 | 3.60527 | -60.93649 | 2024-12-22 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61bd5a49-9620-3d4e-8bcd-fd1c6bece5c2 | 0.93289 | -50.78336 | 2024-12-22 05:12:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af7cbdab-b65f-3420-b38e-8cedf1f49056 | -3.74946 | -47.18689 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923aaaa2-ae3d-373f-87b8-254338277ef8 | -6.00459 | -45.41887 | 2024-12-22 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31384079-6abd-35fe-901e-82c8273aef80 | -2.5738 | -49.44373 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a1da486-dc7c-3f99-a948-1fb4accf8ea8 | -2.57663 | -49.45966 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 808d5b31-dca2-3998-86a4-d2a8037fa71a | -1.18975 | -52.54695 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcfd8ec9-b02e-305c-b823-2a52a7df222f | -3.065 | -47.76931 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b9d69b5-fc02-3283-a5f0-0d7927f45b60 | -3.06976 | -52.84718 | 2024-12-22 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dc69a68-091d-3dd3-9637-94a442c0c1b7 | -1.7152 | -52.59228 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74cd9a0c-2481-3b7b-8c05-71d26100f187 | -1.18513 | -52.54988 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e3ab7e-3028-3339-a996-6aaa80d01005 | -2.62775 | -48.0383 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5ff5ec3-3fe4-352d-9453-e746aabe8f69 | -2.62887 | -48.0307 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51940b34-1690-3787-998f-9ba80cda6ee1 | -2.07594 | -53.32988 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8edb3c22-484b-30fb-aa6d-cf5089ecafe7 | -2.51749 | -54.22593 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87e3c68e-c489-3ecc-8c1c-4d08736b78f8 | -3.31513 | -54.91572 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e826334b-46a7-3fc7-9600-d5ffb341635c | -1.36732 | -53.70639 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 16788f22-16d5-3340-9fb1-43ce5c9d5933 | -4.2803 | -55.74508 | 2024-12-22 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b56b1b4d-5b52-3bc2-b731-143a5d7ce010 | -2.44894 | -51.78431 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6133de6f-e96b-31c1-a4ad-17de6c7257d9 | -1.85483 | -54.13134 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4721936b-ed65-3567-80bc-825168075cc5 | -3.08276 | -46.56475 | 2024-12-22 05:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0960b397-f307-3460-b71b-d1a968896e5c | -1.25973 | -53.52602 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c0a1481-f176-3763-a533-7360d64db9eb | -2.68285 | -54.84466 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c136b91d-bdf8-38e9-89a1-8af41d02031a | -1.49328 | -55.10098 | 2024-12-22 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66470ebc-52d2-34d1-ae52-2d7c12c802fc | -1.2977 | -47.75134 | 2024-12-22 05:14:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19b98a14-b633-3550-8fc7-3918d1f2c98b | -2.50275 | -49.06254 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7263eb7e-c6c4-39c5-ba96-1e6b7f78595b | -2.24832 | -48.31906 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75a6abb9-ca7f-3686-b510-fa8eb732169b | -1.18214 | -53.77911 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1183db76-7000-3f2e-93d2-38c742ada32b | -2.05502 | -45.48289 | 2024-12-22 05:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24e10a9e-9e45-3668-8316-9b5810e5559b | -1.37322 | -53.69348 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 257a086d-2ce0-3654-a4c9-353ddec2d991 | -1.30854 | -53.48959 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8093c216-b463-3987-bd06-f6b4cd9101e7 | -2.67924 | -54.8441 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed17c0c9-3911-37f7-8658-7e7825f9b13b | -3.18619 | -50.40001 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b08ce50-968d-3791-a062-59f1d0157c87 | -1.71796 | -52.57413 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69f13cb9-b141-34fa-a311-c1d40d41ba01 | -2.0437 | -52.10869 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc8f658f-7016-36b4-80ae-9ec5f633a033 | -2.05672 | -54.37259 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ad8d541-6c40-3a80-b04e-1228384ea242 | -3.94558 | -54.63311 | 2024-12-22 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a27e984-550d-3cb2-886a-77eb6bbaf0ca | -1.2934 | -53.12487 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7e26c81-e205-3410-bba3-410d8f5dfcd4 | -2.97786 | -48.07583 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b898e0e0-ac30-3629-98df-1f23911f2508 | -2.50236 | -48.06331 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4f897d65-ad83-36f6-8877-b79036ba4fa5 | -2.82196 | -52.86543 | 2024-12-22 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5221dffa-9092-324b-b871-8356d8d39ab6 | -2.69008 | -54.84577 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7da08a19-ff6a-338e-a35c-f5588d165988 | -2.75815 | -45.56406 | 2024-12-22 05:14:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97f08076-3ef8-3997-9f78-9d79f330ce3a | -1.36873 | -53.69735 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ef0324d-6cb8-3dac-87e3-8333d6aef4cb | -2.0607 | -52.05481 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3cb06e-8c1e-30f8-98f8-44542914f246 | -2.58224 | -47.54361 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4684b276-3881-30cf-bbe4-519883fb0f8a | -2.57334 | -49.44677 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a7760f5-d09d-3592-b50a-348d77e06761 | -3.09857 | -54.55045 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f197c8a9-e07f-3595-b6e3-c1cb0cb4187c | -2.66393 | -54.87161 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f14daee2-55e6-3cee-b5cf-c3aee4421749 | -1.25967 | -54.15446 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea97a39-4880-3f4f-a8a0-63f870c10acc | -1.49681 | -55.10149 | 2024-12-22 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e029cfa3-de70-357f-a8c5-d131c81d2c17 | -3.26223 | -48.89312 | 2024-12-22 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46289fcf-f192-3553-9440-e780b29828e0 | -1.4104 | -52.03709 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21315a41-7c72-3cb7-83e8-b43cc49521b9 | -1.28857 | -53.10374 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1e60c61-50c8-3f8f-b6ee-9ce89978f732 | -4.01354 | -47.05117 | 2024-12-22 05:14:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3ac951-dcbb-3e45-b27d-b88e48259408 | -1.15181 | -53.59813 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f203bd15-d8bf-3e72-b46d-de012f9ecfbe | -1.18162 | -52.54564 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62ee825b-cd29-33ce-87d4-60e027747244 | -2.88725 | -51.80219 | 2024-12-22 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cc143a5-a6a8-3c71-974f-069ab5643f06 | -2.49652 | -49.06813 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb4d4e9-0b78-3071-86af-6e4d76f06125 | -2.44327 | -51.79206 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f27b88-00d3-35db-9998-a0d2796c594b | -1.71057 | -52.59528 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1fdb18c9-eb3f-37e7-ad21-01f4cb2802e5 | -2.97612 | -48.08749 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28852549-9e51-3142-b039-6b9559c5f96a | -3.6007 | -50.63256 | 2024-12-22 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e09c6201-15a7-394f-9b42-dd5bf9f535e1 | -3.6546 | -53.43978 | 2024-12-22 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e88f939-9e0f-30e8-ab6d-a2354bdaea24 | -2.50178 | -48.06704 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f078c02-ed30-37b1-b1d8-30f089f60a26 | -2.58176 | -49.46043 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a232a8-2a9d-3733-8888-be0d8473c40c | -2.58202 | -47.54818 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 316cbb36-5cc7-377f-941f-057a36e56cae | -2.49947 | -48.06683 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 97ca4612-8f82-3463-981e-140486656093 | -4.01285 | -47.0558 | 2024-12-22 05:14:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e6c966-6153-34bd-9241-e70a406b4ace | -2.22558 | -53.81367 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 977681fa-b6d6-367a-ad36-76791ae85a80 | -1.2559 | -53.52545 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d7929c-1885-3b78-ad3b-b3bdbfdddac8 | -1.71442 | -52.56988 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34bf138d-21ac-3ab4-a966-821f400e010e | -3.75007 | -47.18268 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70c89dc4-f08f-3f1c-ab8c-c211e98288f8 | -3.17437 | -53.96024 | 2024-12-22 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2f5689e-5fb7-3f08-9e21-dbf8f85ef39f | -2.82042 | -52.9823 | 2024-12-22 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 198c4bf7-e50c-3b5d-a90e-bfeeae63bf2e | -2.57426 | -49.44069 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7c49ef7-59d1-36b9-b347-cc5b26c60768 | -2.57848 | -49.44749 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 418ee3b8-45c7-362b-bc7a-6d5f154a4df9 | -2.57941 | -53.97737 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaeef30b-198e-356f-be0e-826f686d5a90 | -1.65461 | -53.43139 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d198a0e-3be4-3896-b175-eb2ccb9a9a82 | -2.75365 | -45.5654 | 2024-12-22 05:14:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd7d1d64-2650-31dc-b540-7f0138d8062b | -2.14709 | -53.59644 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65e323e5-f320-39a0-9663-232145c62903 | -2.58223 | -49.45737 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628e5e65-248e-3d5f-9e2d-37236e82fc3e | -1.71497 | -52.56625 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20b10e24-b3b2-39b2-af52-7168ff9f077a | -2.44949 | -49.02753 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7639f8f2-8025-3cab-b7d8-6f409ea5bf50 | -2.05033 | -45.47955 | 2024-12-22 05:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ff182b9-7eb0-3669-a06b-3a78189c1e53 | -3.5903 | -55.4355 | 2024-12-22 05:14:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e939f1-c8e7-3bcf-a363-25caf4bf25e1 | -1.70121 | -52.41883 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c2fddf-cd13-3c5d-a8d3-22540efacc6a | -2.06009 | -52.05874 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6850dec7-56de-363a-a959-96f17f03a382 | -2.05645 | -52.05414 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a880469-ed4c-36a5-b134-ad8526e26c0e | -2.49615 | -48.06621 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53f060d9-a0d6-31d6-b64f-e3129460ae32 | -2.90127 | -54.49738 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca0bfb7-8df5-3f48-8108-ff78f6b1c274 | -1.17701 | -52.5486 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c83d166e-c89a-3e44-83e4-d4833400708b | -2.97728 | -48.07972 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 986a4dd5-616e-3fc5-9f5c-6d543c335c3d | -2.79851 | -46.74977 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51cbb67b-450d-33b5-8d8f-330305f799c0 | -2.51124 | -54.19258 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d6d91fd-e101-3314-9824-b07be3e69b23 | -2.0431 | -52.11259 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e1730783-20ed-308d-b270-02e0436db25e | -3.7603 | -47.19756 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
