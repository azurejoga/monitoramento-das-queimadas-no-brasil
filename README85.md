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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032c11b2-f17a-3d59-8e02-8e80f055c98c | -8.9109 | -63.54249 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ccdf90-3439-3ef3-beb2-d256c204b599 | -8.81279 | -63.17709 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb96ac11-1ba2-34d9-ae5b-841f1fe688bc | -8.80778 | -63.17611 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fce93b81-7295-391e-8ae9-c9384f50c611 | -8.80426 | -63.10892 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c5cb7c-8b75-3c3b-837d-806bdb5a64e0 | -8.76847 | -63.22117 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73884134-2f9c-30b3-b99a-69970afd0f89 | -8.76793 | -63.22416 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e250009-56b9-336d-9203-b48a8ca8100c | -8.68797 | -63.09575 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19e5e034-348a-3873-a4a7-75567c701011 | -8.68296 | -63.09484 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c724fb4a-cdb2-389f-8899-2b8e1a3911e7 | -8.68252 | -62.8708 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3d332b3-9376-3d31-b55d-9bb6799d7f47 | -8.67795 | -63.09394 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0a900ec-e8e3-301c-b828-e45984df8392 | -8.6586 | -63.25878 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f25cf499-3a7c-32ce-9832-cc1b68e11a2a | -8.65806 | -63.26178 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 590f2e25-8266-3161-aa1c-ea390b44adeb | -8.65643 | -63.27082 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 266bae96-2c8e-3a1d-b339-6047b18d09ad | -8.65589 | -63.27383 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48baff62-d7b6-3721-9cb6-6b96bfccd62f | -8.65484 | -63.48564 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 635f9b9b-fa9e-31b1-b665-4a2b38df6989 | -8.65427 | -63.48879 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26e06c1-c8d9-3854-830d-ede27c3c3a1e | -8.65353 | -63.25785 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 962c8d3f-f6c0-3e0d-b05b-dbf16e467b91 | -8.65299 | -63.26086 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c9d1370-32b9-3655-9849-c15344aa934f | -8.65136 | -63.26989 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bc5526-294c-37a0-80b5-641dcd27f417 | -8.65081 | -63.27291 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 808ee5d0-8918-31f6-a5d9-78e85a4d408c | -8.64846 | -63.25694 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc0d5c47-1738-3b48-88b3-b133ea2ebf6e | -8.60502 | -63.09779 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5735745-e6af-3e67-9e18-b9855ece46e4 | -8.6045 | -63.10073 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865877b4-d2b0-3364-ad62-f693212ddce8 | -8.60232 | -63.26009 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4d521b5-5b82-32ce-b10a-a84d38419ee7 | -8.60115 | -63.25782 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d6da893-991d-3a7c-9f95-590b80990dc3 | -8.6006 | -63.26082 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b967d5f9-dc46-3317-aa61-91d12a71eae4 | -8.6 | -63.09689 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a252ec35-2c36-3be6-88b6-ac31c63bd788 | -8.59948 | -63.09983 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04ac7768-b01b-315c-9021-5803ebc5441b | -8.59777 | -63.25617 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa22b8eb-4948-3ff7-ab53-0ec910e79f87 | -8.59724 | -63.25918 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17ceb1e-98c7-322f-99f5-28c988b7e0d7 | -8.59663 | -63.25392 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6985d08-918b-3382-94ca-26e834815c9c | -8.59607 | -63.25692 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7887910f-7a57-3ba2-a31a-322d1c42ae90 | -8.58044 | -63.09036 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de8704c7-cd23-35a0-ac2f-31b80c3bb27b | -8.57991 | -63.09328 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c060dc4-c336-3ad7-8a94-25902677fbf9 | -8.5776 | -63.41404 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a98208ba-1b9e-3dbc-83cc-234d69b0f91b | -8.57535 | -63.41278 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 112666d9-cf93-3db4-829d-dc30aae97fb0 | -8.5748 | -63.41588 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a480a42-2768-3eaa-b3ef-dd86e398b5e2 | -8.57247 | -63.41314 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d643e96a-8be3-3e9c-b506-3a03ed150a10 | -8.57021 | -63.41187 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983f5477-67b9-31c4-be03-7328e990c61c | -9.82502 | -63.63041 | 2024-10-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be1885a8-e426-34f0-8d55-46fc81e4eaf6 | -9.81993 | -63.62949 | 2024-10-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8325fc62-a7f9-32a0-a88c-1d55ae9842f1 | -9.81936 | -63.6326 | 2024-10-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e8c3d9b-ab8d-38df-b616-1a4c50ec69c6 | -9.80722 | -63.85498 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ebf206d-7d97-37c6-8e73-ae7ccf5c8428 | -9.58931 | -64.09366 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad4a8d4d-fa39-3d53-b466-a4fde21e9ec1 | -9.5887 | -64.09697 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 420eea67-51d9-3a35-a686-8fb93f8b1330 | -9.58406 | -64.09255 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9dc79515-8f0d-3bc7-b68a-1c6b57adfd59 | -9.58344 | -64.09589 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9bcf998-dde4-32be-8211-f983bc5b85ae | -9.58282 | -64.09927 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a67680d1-e421-38c2-81eb-8ef0a6c522b1 | -9.58219 | -64.10264 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf2c913-d364-381b-bfeb-7339f1379fb8 | -9.58158 | -64.10592 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d13dd84-f807-3271-bd2b-38845e5da719 | -9.57694 | -64.10154 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf322f9a-4dd0-3318-91da-722a0a43eb79 | -9.57633 | -64.10483 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe9ec25f-3d71-3045-a62d-c36dfebc1258 | -9.55894 | -64.1984 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7dd5699b-0750-3d5a-9cea-428f184634ae | -9.51134 | -64.30544 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51d64c3-6fde-3cb3-b2df-b275baaee149 | -9.50533 | -64.30792 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bee1d7f-cbb8-34f0-8aec-5500dc00eea6 | -9.49167 | -63.13015 | 2024-10-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| feccbfc0-5616-3dba-b4fa-4ff8bdf71e28 | -9.45993 | -63.70592 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba568c78-567a-3507-8fec-fcbdcf50fa7f | -9.45936 | -63.70903 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8100db2-86d7-33d4-98de-fa8bee01d612 | -9.44232 | -63.37808 | 2024-10-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3258db5-bef5-3252-b894-3d4304898e0b | -10.70184 | -64.1114 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e22ff16-3d0b-3205-966a-55295f27a77a | -10.69662 | -64.11064 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1295e6bd-ce21-3484-98b0-418ee13a868a | -10.69603 | -64.11385 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f53a48-8540-3d07-94fc-10687de03b75 | -10.69539 | -64.11732 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87fe4bf3-f220-36d2-a8d2-f560d31829c4 | -10.63665 | -64.43388 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a42dd6d-08ce-3402-8650-8deb6de79438 | -10.63087 | -64.43545 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5920f45-e63e-383e-8806-dec6276e8d6e | -10.6295 | -64.4428 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f110186-0b48-3301-9ad5-65f435823e75 | -10.60533 | -64.39647 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6dff453e-7abb-3cc1-9dd8-8a5416368463 | -10.57981 | -64.04014 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 518a9121-2d4b-39ca-99a2-84c58510a977 | -10.57526 | -64.03592 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e03a856-ad0a-30c0-bf38-dbaad45ad51a | -10.57464 | -64.03925 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da1a078c-811f-3ca1-a16c-8373558da7d0 | -10.56942 | -64.03858 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a1b82e-4140-3f5a-81b1-d0f2ea801baf | -10.54698 | -63.83194 | 2024-10-12 04:59:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1579988b-9eae-31fd-b11a-6f17e815ec47 | -10.54645 | -63.83479 | 2024-10-12 04:59:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 578b3487-01fa-38b0-9f4d-5f3724a97d9c | -10.49906 | -62.98169 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc560ae1-85b3-3e32-aaa0-71228f5761b5 | -10.49419 | -62.98109 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e6200c6-a49f-316a-8d98-6c8429316542 | -10.49349 | -62.97886 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c76d2ee-c401-3089-abbc-6b9d844dc60a | -10.25977 | -63.34031 | 2024-10-12 04:59:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2efb922b-e3d1-3b53-bbde-f7201b40505f | -10.2129 | -63.3119 | 2024-10-12 04:59:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83b678a1-bfac-3a08-b771-f73fe1a90241 | -10.16304 | -63.22133 | 2024-10-12 04:59:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0af8e2-f76c-3fbf-be92-e8d9df6074e8 | -10.15812 | -63.22042 | 2024-10-12 04:59:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb7d4bd-1a7e-315b-b098-6bc599153c70 | -12.1652 | -63.34533 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a944bfaf-dcfe-352e-a1d2-63f5c3c440fa | -11.75921 | -63.81358 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebaa7675-751d-33ee-bf03-2a937aa7609f | -11.75147 | -63.827 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 034142bb-ed61-310a-977c-6a470bd77cf0 | -11.75038 | -63.83271 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d03bbe8-863d-3299-ac16-077da373f499 | -11.75016 | -63.83287 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad6236bc-d972-3e7c-b7fd-c6d12f369ee6 | -11.74984 | -63.83552 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68c2633a-bced-3390-b390-61c361e993fe | -11.74965 | -63.83568 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e1e8c42-f6ce-34f6-a279-078ccf60fee8 | -11.74651 | -63.82592 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a385c26-a934-3ca1-96ac-d1190353bc94 | -11.74491 | -63.83429 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05b108d2-7dea-37aa-a9cf-bad2b0e808d5 | -11.74471 | -63.83444 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ca14628-2af8-3a25-bb6e-c7a16b203800 | -11.7403 | -63.83037 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7124f24a-a8b9-32c7-8a3b-267b0e4d9057 | -11.73975 | -63.83332 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e0e076d-28cb-3927-90bc-ce7869d1e80e | -11.73091 | -64.29375 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c20ff12f-d30c-323c-9348-3e41e8e8554e | -11.72516 | -64.29595 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b621e6c1-e65e-3ad4-ad9b-78852569d614 | -10.96682 | -63.59798 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8aa4ca96-de62-396e-bf74-d90e94788fc4 | -10.96627 | -63.60093 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f90aaca9-3266-3b37-9a47-7d310f922ce4 | -10.96188 | -63.59686 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e906cff6-90f1-3ce3-b1bc-2242b112f0d0 | -10.96135 | -63.59972 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fd89ea6-cdca-3cf4-91a3-23775f650a54 | -10.96081 | -63.60258 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94038dd4-af87-302e-a93c-039b5a4ca8f7 | -10.93827 | -63.86279 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README86.md)
