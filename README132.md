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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eddb2c4d-6d0e-35d8-b360-701b991f6313 | -11.51342 | -65.10548 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b99553-f3c3-3463-b676-1c02534ad2a2 | -11.51171 | -65.09408 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e553c99-a7c7-3c7d-bda7-60bad9af9b6f | -11.51116 | -65.0977 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d63954d-d137-3da4-a7a4-6e1a71e1bb15 | -11.51061 | -65.10133 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac1c9c09-9538-3634-bbb0-ca13a215cd7f | -10.91636 | -69.36768 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8439bda-5437-331c-895f-aeefedfe4316 | -10.85511 | -69.3928 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1318ea-a2fd-3040-92ca-57a67d34c41c | -10.84912 | -69.34031 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065f39e0-4f95-37f4-b2db-2cf758624884 | -10.84554 | -69.33968 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aabb9f07-1ef4-33e2-9a85-edb1ff4092fd | -10.84485 | -69.34383 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ecda93d-539f-3e3d-aacc-20f0a4d57e23 | -10.76672 | -68.83196 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2bd6fad-82cf-340c-9223-46ead87017cc | -10.68437 | -69.02395 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0c6789e-5ae1-3931-8c30-0e3ac6262e17 | -10.68098 | -68.87045 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 404915c7-9803-3abe-98ff-240f78bb82bb | -10.68032 | -68.87443 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07d0ed0-d386-354f-9347-5c8f9c3ea55c | -10.47654 | -69.05302 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff91dbf4-d7a3-3d3f-8faa-899bbdf2d60f | -10.86237 | -68.24439 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b32eac95-0a0d-338b-969a-e40ad3cf824a | -10.85894 | -68.24384 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7c6ad07-fa94-341b-9c0c-8b4eb5f6fa2d | -10.83019 | -68.3557 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 804bbfda-09e7-3a75-807c-aa4f5b730e0d | -10.82957 | -68.35947 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| db9e87c7-d75b-3eaf-a5fc-4d3296ccc784 | -10.82675 | -68.35512 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa3aed85-6ac5-34bc-85e3-2fa59b10b2b9 | -10.82613 | -68.35889 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 78b0fa1c-7c50-3c42-976a-6ae61c5fcb58 | -10.82552 | -68.36268 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 422ebe30-27a4-3368-b002-4fab51e402f6 | -10.82208 | -68.3621 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a367007e-cf8f-38f2-8e38-98f3974a3a79 | -10.88911 | -69.12292 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a42f3905-b42a-36a4-b30f-51a1762e897b | -10.88556 | -69.1223 | 2024-10-07 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d72c6dd-2ee1-3044-9aab-4205abea9b7a | -10.97865 | -68.45352 | 2024-10-07 05:42:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aac0fd64-dc85-3f4d-94a3-60d00fd57a84 | -10.95361 | -68.35181 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59b98e0f-eb68-3469-9f1d-92e412cda839 | -10.95017 | -68.35125 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc5b823d-643e-3a1e-bb65-528382abf7ac | -10.92809 | -68.4218 | 2024-10-07 05:42:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 562fa063-d3fb-3c15-adb7-3c088bcba18f | -10.92227 | -68.24164 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68dd7f3f-bdc1-3771-a5a1-58de969b4f8a | -10.90519 | -68.28139 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e987ecc4-589c-3fde-b0a3-b8b49802b882 | -10.90457 | -68.28517 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d084920-f541-3b4b-9419-9653aa37c4d6 | -10.87311 | -63.89822 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef06841a-1c17-39bb-b5e3-64ff383ef757 | -10.87304 | -63.92232 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daa302da-1866-3f06-895f-d074b522fc29 | -10.87253 | -63.9021 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e58a7601-222f-3a7c-850b-fb46fd9e0a2e | -10.87193 | -63.90606 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9319f92-a67a-376c-9b8a-c3827911237d | -10.87133 | -63.9101 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9fee4af-2f7e-308f-b650-2cc25991f003 | -10.87023 | -63.89373 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96d59460-9343-3804-a8ad-d171b9ad6bb8 | -10.87015 | -63.91793 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce0f952c-d978-358a-8ed4-aa9ce6b1ff89 | -10.86965 | -63.89764 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b38500f6-c937-36d2-b4b4-602b53c86ac6 | -10.86957 | -63.92177 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cb6f344-40a9-37ac-9275-5141fe9782dc | -10.86847 | -63.90544 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac57427-312b-32e8-95ca-4680c319b7fe | -10.86787 | -63.90947 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cb747ff-6812-38f3-8232-9b657a7e1584 | -10.86736 | -63.88921 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d361feb9-006e-3b9c-a8de-28cd3d5ce461 | -10.86727 | -63.91345 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d95554bb-61bc-3b00-b4cc-dd7b2fed444f | -10.86677 | -63.89314 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3de5117-36c6-38b1-83f6-7a889c25bfcc | -10.86669 | -63.91732 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8d43d35-f3a0-35ed-9c9e-eca69ad4496c | -10.86382 | -63.9128 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02e6195-8417-3d73-b625-89defdda3fb0 | -10.86323 | -63.91669 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105fce46-ffe8-3ee5-8a9c-ffa5050304f2 | -9.28946 | -65.3335 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1111ad67-33fc-3bf9-ba80-c81380aec9b7 | -10.21321 | -64.46654 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdcee33e-ac9e-33b1-96cb-7ced95a156c1 | -10.21266 | -64.4702 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f256c460-a0a7-34d6-920d-3f29c2f504c9 | -9.67518 | -65.53793 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c8b4beb-e891-3951-9d20-6f94244ad771 | -10.80696 | -65.18061 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8a8e57-03fb-3f4c-a58e-ce2c282e4c5a | -10.80641 | -65.18417 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4952e4a-f9db-37e0-b4f6-fc90ac7dc3b0 | -10.80586 | -65.18771 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 089ea78f-ac74-35a2-b7bf-f15666218969 | -10.80532 | -65.19125 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1203364-2867-3302-ac10-34195c536359 | -10.80197 | -65.19074 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5ffe11-4e66-306f-9740-b91dca94e34b | -10.80026 | -65.17963 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c6bec6-486c-31e4-af34-52ddff1f5f90 | -10.5597 | -65.39634 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0dac01-6bf4-3b44-b3a1-8586aaddc559 | -10.45788 | -65.22076 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 706bd7b4-0769-3c0c-9d58-70ab94859a4a | -10.86878 | -65.26279 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 085afb7b-8c64-3bb0-b888-7aaa461f33c5 | -7.92276 | -72.49249 | 2024-10-07 05:42:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b6bbb95-ae80-3dad-8a41-8a0ca0043d13 | -7.88513 | -72.46652 | 2024-10-07 05:42:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b960135-07f1-3ef2-a8f2-73b97a756868 | -7.88411 | -72.46829 | 2024-10-07 05:42:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2303b52d-ffef-37cc-b75a-42730c509196 | -7.46515 | -72.68668 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32bcbaad-9885-31b0-83f9-c226966e5911 | -7.46052 | -72.68578 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 111c65ef-d536-3aab-b572-8bb18bf59b6e | -7.34794 | -72.90617 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5ced082-8062-3365-9589-243326cd4de6 | -7.3613 | -73.22656 | 2024-10-07 05:42:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9983ee29-9042-37a7-b0e8-1cf712d1c96e | -10.0368 | -68.46416 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42529751-b2c9-3a7d-8fd8-0a40b769e8e9 | -10.04028 | -68.46474 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e542defd-cdeb-3476-aef1-bc64ff3f3ef4 | -10.05547 | -68.3718 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c37bd4e-053a-33ac-b094-1166b1ac2014 | -10.0561 | -68.36794 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db506067-751e-3f7d-9a16-bd8c0671289c | -10.06382 | -67.75863 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eac8f16-0310-33fb-9c12-556263d75ad4 | -10.11426 | -68.01073 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5002113a-3d97-3175-a4e7-776b01e66108 | -10.11889 | -68.00379 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a711626-bc38-32a4-940c-b773c67343e5 | -10.141 | -68.019 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f5434ea-7e9d-378d-948f-6593aeb21077 | -10.21415 | -68.28357 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a4b68b-7145-3705-91aa-83ee7349bf3e | -10.21665 | -68.28325 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8d738e6-6fb7-36dc-85d1-ad3f2edf63e8 | -10.2176 | -68.28415 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b7d6ac-bba3-3cab-975c-093b7e0a0ff7 | -10.21822 | -68.28033 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bce9bac-f5c3-3ec3-a410-d9936b954c2f | -10.22009 | -68.28383 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f35fb02-a9c8-3ea4-87dc-c3bfce11c9aa | -10.22073 | -68.28001 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c5f97cc-ad86-345d-afbd-ac30e5626048 | -10.30767 | -67.96542 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9661307-5428-33b6-a02b-50c68d621e5c | -10.30828 | -67.96169 | 2024-10-07 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 903ba95b-279d-361c-873c-e966dbb4fd3b | -10.3325 | -67.98486 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18f596aa-2cdd-3b41-8ca3-5e899590afe0 | -10.34114 | -67.97478 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9634127f-7bc9-3855-84ca-9ee937b0929a | -10.38279 | -67.958 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3523a91-07ea-3ac9-a2d6-652897e2716f | -10.38558 | -67.96229 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74419515-1f2a-3c8f-b425-39f103145ede | -10.38619 | -67.95858 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a0de50f-9337-3315-b59e-fa015e964b69 | -10.38955 | -67.89133 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cc8e4ed-e402-3ab0-ba7d-28f29c1dfe98 | -10.39035 | -67.89072 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42b296e2-5a60-3279-ab40-e9ed25805097 | -10.39375 | -67.89127 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d60b166-e1aa-33d6-bf7c-db26311c9987 | -10.47662 | -67.81023 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5a67328-d04f-3473-8fae-ce5fd401eaa3 | -10.48001 | -67.81079 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b79a774d-8173-3368-85d8-dd3517796c15 | -10.49923 | -67.88596 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ae344f1-e426-320c-a60a-c816e3892638 | -10.49932 | -67.88931 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e56f09-ab0d-3f30-9413-609608abd1b6 | -10.49992 | -67.88564 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24f2a703-182c-322c-bc5a-c19368ab9fe8 | -10.51289 | -67.89157 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05a8240d-0276-3fae-9969-920ae913f454 | -10.5135 | -67.88787 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68c64e6b-4498-3159-982b-87da25c03f99 | -10.51629 | -67.89211 | 2024-10-07 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README133.md)
