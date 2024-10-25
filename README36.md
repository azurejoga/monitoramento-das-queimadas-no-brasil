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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fda59b8-074c-3fcf-8b76-fcb3108ca059 | -3.0985 | -54.15125 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3844849-2fe8-3226-8e2e-fafc488c99f4 | -3.09764 | -54.15613 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8719d164-35b4-315f-948e-84459798a411 | -3.07542 | -53.82422 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 430305a5-b41b-330c-a6e9-545f1f0e2321 | -4.19616 | -54.98428 | 2024-10-25 04:14:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e13fe657-d726-3370-bdee-8048fa206fb3 | -4.03263 | -54.62112 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74117084-6c28-382a-ba8c-67b3bdb58ee2 | -4.13089 | -54.63333 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| cb4425be-8dba-3205-a767-1dc24937dbd4 | -4.12995 | -54.63865 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f8ba5c94-a6e5-3976-9f88-1920cd6a4dfc | -4.03351 | -54.61613 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b4b3d17-31cb-34a6-a48a-23d9eb4c345a | -4.02706 | -54.61521 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ce3232b-50be-32fd-bbd3-3c8a70bdb9e4 | -4.00771 | -54.45066 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10578b1d-17a9-36a5-ada1-b9ed01e5de21 | -4.00683 | -54.45582 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 718020d9-8af7-3140-bf57-b907787cfa18 | -3.96434 | -54.66429 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc93de13-e654-383b-8374-21aff28a964b | -3.89638 | -54.13846 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f26cb4eb-df02-3d1c-8774-62169bdb856d | -3.88926 | -54.14244 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c6f7608-030d-3d34-aff4-42193d4ecec9 | -3.88838 | -54.14745 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f75fcb-180e-3ecf-b4c7-a977420def02 | -3.86386 | -54.36156 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a83ee55-e7fd-302d-8345-979ee3bf6f7c | -3.64748 | -54.794 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40755766-d512-398b-b70e-fd0924c582e4 | -5.24698 | -55.96416 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 886b6b8f-b39d-39a2-8b22-9722434c489c | -5.2458 | -55.9705 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43934e8d-3e53-3a1a-b0e2-dad3cd099099 | -5.24526 | -55.9663 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c4edc277-31c5-3a28-b1ae-16ac97b8e850 | -5.23899 | -55.96925 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6906742a-9e65-33dc-8d02-8379fe222d61 | -5.24412 | -55.97265 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 97d2651f-cee8-3bc4-b8a5-8b4996727bd7 | -5.23845 | -55.96499 | 2024-10-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcd3df91-403d-37a8-be7a-a59b1157b439 | -1.1834 | -53.6771 | 2024-10-25 04:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 20c87098-40ad-3021-b882-e55d0ce6e087 | -1.1834 | -53.6569 | 2024-10-25 04:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8c9de06c-f437-39dd-bc0d-c96ac0149c95 | -1.6062 | -53.3087 | 2024-10-25 04:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 01eceb52-29a6-3729-8572-dcfe1aef2466 | -3.2135 | -46.8063 | 2024-10-25 04:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ebf5b298-836d-3309-b15f-87b4baf00ef3 | -3.2136 | -46.7843 | 2024-10-25 04:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ae59ea6d-e2ad-3c11-a128-ae45d61dd81f | -3.1949 | -46.807 | 2024-10-25 04:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1a0b1a86-f34b-360d-8c10-344bb889b2be | -4.2429 | -48.5474 | 2024-10-25 04:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8a33db82-2732-3e6f-81d5-4603c74460c1 | -4.3351 | -48.6292 | 2024-10-25 04:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f3f89811-5b0c-3af1-8581-b665c1f4377b | -5.9788 | -45.3621 | 2024-10-25 04:15:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 78f8961b-eaa5-3ea6-b820-cfa71efdb1f7 | -12.3782 | -63.8821 | 2024-10-25 04:16:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1a0eafe5-51d6-3d6c-a1ee-a4fc437e7037 | -12.3783 | -63.863 | 2024-10-25 04:16:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 318069ba-87ad-3e4c-b040-08c4bd249e4f | -12.4591 | -63.1704 | 2024-10-25 04:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a82c2fb1-060d-3b07-a1b3-b92881b82eb2 | -12.5356 | -63.051 | 2024-10-25 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6636a4c9-8916-3c57-927c-bab5ec541352 | -13.4959 | -61.6203 | 2024-10-25 04:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 674e6c0f-7505-345f-99ac-f9aad19b241b | -15.6785 | -55.9926 | 2024-10-25 04:16:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 8844a168-24be-3164-b774-c2abb17a09c0 | -15.6788 | -55.972 | 2024-10-25 04:16:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 6eaac8b2-8f3d-317a-9c26-a4317e2ff643 | -16.9596 | -57.5245 | 2024-10-25 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| bcb1d766-51f1-3b2f-b2be-076d27fb4403 | -16.9792 | -57.5223 | 2024-10-25 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 953c2f18-a520-37f6-ae0e-7743ce6efc9a | -17.0381 | -57.5155 | 2024-10-25 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 825f7078-04c7-38c2-9cc1-c63236a3641a | -17.215 | -57.4744 | 2024-10-25 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 5974286a-27c4-3774-aada-8c757cd0d3c5 | -17.2386 | -57.2256 | 2024-10-25 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 71627821-778c-318b-b462-dcb6a94083eb | -17.2537 | -57.5108 | 2024-10-25 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| d2063d5d-d843-368a-aa4b-5bd2a2cc09a2 | -18.3199 | -56.2404 | 2024-10-25 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 38547ab8-041e-34e7-ba1b-fe76d1a6da04 | -18.3398 | -56.2377 | 2024-10-25 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 692be5b1-09ea-32ad-9592-81e167ffcc5a | -17.77029 | -57.35949 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 9c9e20e6-f2d0-31ef-a418-3dbce91ebd9b | -17.76927 | -57.36414 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 033e0892-69b7-3028-b543-148ac6efa1de | -17.76723 | -57.37348 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 7873873f-89f5-34a7-9423-7d4ff1c7a246 | -17.76621 | -57.37815 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| e3a279e9-7dc5-39e6-b935-b4e132c4b6f9 | -17.69717 | -57.33974 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| d4742008-1e39-3166-a070-56cd769a7aaf | -17.69383 | -57.33657 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 3da95594-92a8-34c5-bd94-937e06722d48 | -17.69279 | -57.34121 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 10a91914-cdbd-3746-ac12-d11933656d32 | -17.69175 | -57.34585 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 80191815-363e-37b1-a8ee-2134bf0951ff | -17.69121 | -57.33832 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 2fe108d5-abfb-3e7c-81d0-ce7fade2720a | -17.69021 | -57.34297 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 178be05c-34fe-3a2b-89c0-d7e5c6cfb57f | -17.67532 | -57.47557 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| fec97930-dbb9-3184-96ba-85fdab2f9659 | -17.6746 | -57.47302 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 66f7da82-584e-3048-bcd9-2a82a4f4ee77 | -17.67357 | -57.47778 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 2a969791-64aa-30d2-b416-a759d38a7bce | -17.66963 | -57.46682 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f8d920cf-347d-32ca-af79-5a408e39914e | -17.66932 | -57.47414 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c0458773-4055-3fe4-b129-5160ab0ef26a | -17.6686 | -57.47158 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 727700e6-a8e2-316f-bcab-5e55c9276629 | -17.30041 | -57.29004 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 39acf0f5-e4df-3023-b1bf-fa19234c2e2d | -17.29937 | -57.29473 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7adcfb72-1d3a-38f1-8b46-2fc9eae1e908 | -17.2853 | -57.30135 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2ea1b624-a7e1-3ceb-a6b4-eff5f477167d | -17.28423 | -57.29868 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 565d51fe-e72c-33c2-8308-ccf4468a226c | -17.28321 | -57.30342 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c4be0756-c01e-3bb8-b305-44acd636dc85 | -17.2793 | -57.29996 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ffbae476-7120-3874-b00a-6349d08a7267 | -17.27825 | -57.30467 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e6dc936c-cb43-3009-958b-c9621a006857 | -17.27722 | -57.302 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4252205b-aee1-3823-b6f8-bfdf7c2a5d23 | -17.27463 | -57.26433 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f0fa0f00-772a-3f7c-93e2-9a22bff08129 | -17.27335 | -57.26151 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 98493904-b668-366e-847d-5446604be4b9 | -17.27234 | -57.2662 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bd892c2a-057a-3287-924b-2547fa12cf65 | -17.26864 | -57.26294 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 137038e7-7a7b-3bd4-937e-a1b61c5ba909 | -17.26731 | -57.29718 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a34475e4-7ccc-3d4e-8c52-0e650375cd39 | -17.26389 | -57.51259 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b7e812ab-733b-34b6-b2a3-57ca7920dc5a | -17.2589 | -57.50633 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 84caf2cf-d773-3d7d-a996-6a56e8cbc4d7 | -17.25855 | -57.21386 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5e5d96c1-3e72-3fad-9e40-9a443fbb1b7e | -17.25782 | -57.51117 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1104d25a-e974-385b-9120-b1d4d9facb3b | -17.25674 | -57.51603 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| f216082f-6473-34ac-862e-0b7aa3d68bb3 | -17.25283 | -57.50489 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 358435ac-ed7b-38dd-a1ed-335b606e6d42 | -17.25175 | -57.50975 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| efcff31f-eb9d-371b-bf03-e71fcd826b04 | -17.25067 | -57.51461 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 072107bc-4edd-3edc-95bc-1c4dea40b80b | -17.24959 | -57.51947 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e7591c70-da62-3918-a3aa-70d8296b345d | -17.24676 | -57.50345 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2a5922cd-0574-3aee-8b79-47386acf6d83 | -17.24134 | -57.5278 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a099ca06-08a9-30c4-94c9-e68fd7c61f96 | -17.2376 | -57.22364 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 212c1ade-d724-35f9-889b-8b97fe6713b1 | -17.23659 | -57.22829 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| bd5d1e7e-7a8a-3d25-b59b-f2f0ac32e666 | -17.23635 | -57.52152 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3e2877e6-42c1-3d3d-82d2-cc3c8b7a0fb3 | -17.23567 | -57.52428 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b4d0b09e-ecce-324b-addf-270693d5d175 | -17.23526 | -57.52638 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 10a8fdb7-518c-3d2d-a333-8655ce625401 | -17.23462 | -57.52915 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9474324a-a10a-3efa-b72e-84c11cf7716b | -17.23417 | -57.53127 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 647c1279-7a5c-3471-a03f-f539324ab2c9 | -17.23061 | -57.2269 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 35b6ceff-bcd6-344c-bb29-c8f1425dc88f | -17.22963 | -57.49437 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9dd856e-9643-32b5-804d-c32de5e34164 | -17.22959 | -57.23156 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 3570125f-f097-3425-8813-60bad1111951 | -17.2288 | -57.49702 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2cdbc3f3-d998-38dc-9a1b-e9e8e7bac500 | -17.22857 | -57.23623 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 2f66ee95-d4af-396c-81f2-0ca9f7f614e3 | -17.22854 | -57.52773 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README37.md)
