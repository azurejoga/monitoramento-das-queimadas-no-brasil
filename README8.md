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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd63506d-1f6c-3f59-9809-a7f27680ebe7 | -7.5337 | -45.4141 | 2026-09-20 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bfa7bbe9-3ae9-37cf-b8d7-203e33ccdc8b | -7.3259 | -55.6153 | 2026-09-20 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 2344bde9-7dc5-36dd-9ce1-83b2c7238f3a | -11.0991 | -54.0285 | 2026-09-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 7e4197af-1a9a-3a96-aa9d-5b68768afefe | -13.037 | -46.9096 | 2026-09-20 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 91481378-fa43-30dd-b47d-6eda4e2e129b | -14.7051 | -46.6852 | 2026-09-20 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0ce1c0d4-549b-3800-94ed-c107ac422759 | -2.8974 | -57.8181 | 2026-09-20 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3b941d62-c8c3-3590-9276-7ee48d603b34 | -7.5284 | -45.8885 | 2026-09-20 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7171e1d3-8d61-3e2c-9ebd-c4742c6bbb77 | -2.8791 | -57.799 | 2026-09-20 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 70bdd1f6-9617-37ef-8e0c-497cf937e3e8 | -2.8791 | -57.8184 | 2026-09-20 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e9ee7421-eab6-3fd3-b787-0a0e8df6c49c | -5.8595 | -53.5196 | 2026-09-20 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 6117091b-9c29-31af-9902-81eaa8d89651 | -5.8593 | -53.5399 | 2026-09-20 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 128ac134-becb-381c-8cde-91f8ee88f59f | -11.118 | -54.0268 | 2026-09-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 9615f34f-bf40-372c-8db2-402f95f07708 | -12.7629 | -46.1343 | 2026-09-20 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6e4ee06f-5f45-3b36-8a95-1bc722d60120 | -7.5525 | -45.4123 | 2026-09-20 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fba64de0-70fa-3538-9abe-40e66088d516 | -3.6946 | -60.6025 | 2026-09-20 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 005a7dd4-9346-381e-b4ba-4a0c148c2c2f | -6.2948 | -47.6274 | 2026-09-20 02:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1420cfc2-a69e-3602-a2fb-5735b536786b | -3.7453 | -51.8288 | 2026-09-20 02:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 8c588656-8c6f-3fdd-983c-3f74940b2a63 | -14.6851 | -46.7115 | 2026-09-20 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 076f3415-7593-39a4-a84d-ede86546a33b | -11.2118 | -54.0797 | 2026-09-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7d20ac97-b385-330c-9d4d-7200a0979442 | -7.5334 | -45.4367 | 2026-09-20 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 4efba460-da40-3139-b6bb-be710a41e0b4 | -11.0989 | -54.049 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f6870a63-9cfb-3e36-aef5-ebbd0eed07bf | -11.379 | -51.42 | 2026-09-20 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fcb0b066-a6ba-3f22-ac2a-755afdffe148 | -11.2307 | -54.078 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 96f2dcad-c11f-332d-940e-40ea46e76956 | -3.6946 | -60.6025 | 2026-09-20 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| aef13105-cb18-3c62-a6ef-f8f704aeb4ad | -11.0802 | -54.0302 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 487f9ea6-dc69-3e67-89c2-f767a0a1fe39 | -10.2787 | -50.2605 | 2026-09-20 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 29c22945-51fb-31bd-a49a-7a8e1269015c | -7.5522 | -45.435 | 2026-09-20 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 4d61315d-4691-332e-a166-53bd747327de | -7.5525 | -45.4123 | 2026-09-20 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1c454dc8-39d5-37f7-9683-1621f5448dd7 | -11.8547 | -47.6596 | 2026-09-20 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c4210fb6-ec01-37c6-92da-3f2daaedfc50 | -14.6856 | -46.6886 | 2026-09-20 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 2ff4acaa-6b8f-3ea7-aa38-39c84f2d9b33 | -7.5337 | -45.4141 | 2026-09-20 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 21bb0f5c-b122-372a-a87a-2344ff77a1e5 | -13.0177 | -46.9125 | 2026-09-20 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 83f6a08b-400b-31ec-91da-0496c8405423 | -5.8595 | -53.5196 | 2026-09-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 50320881-bede-3d32-acf8-7a93a5ac08a6 | -2.8791 | -57.799 | 2026-09-20 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6dce0ca6-71ee-3d33-82b7-e9563e96fb41 | -8.1686 | -54.7634 | 2026-09-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 59ef89e3-173a-350f-b1b1-40a788f53e77 | -3.7453 | -51.8288 | 2026-09-20 02:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b9930dd8-e303-301f-b506-31c82194db80 | -8.7546 | -48.6669 | 2026-09-20 02:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7cbda6e2-11b4-3343-9355-06357c4e8a35 | -5.8593 | -53.5399 | 2026-09-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| bc443641-fed0-39a3-a710-bc952c1d474e | -2.8791 | -57.8184 | 2026-09-20 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b36359f7-99c1-3299-8587-d06e499b7777 | -2.8974 | -57.8181 | 2026-09-20 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6b75e526-a0d6-3d49-a712-8b16f73103ed | -11.118 | -54.0268 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 852a8044-1ddd-3ada-9a80-5b2bf6f5091a | -17.0284 | -47.149 | 2026-09-20 02:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 125dbd24-259f-3f33-ae1b-077bec664151 | -17.0289 | -47.126 | 2026-09-20 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6d1e9390-cfc0-36b7-8175-4b3e9d61c9c8 | -14.6661 | -46.6919 | 2026-09-20 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 3fc88b25-4750-31ce-85a2-06bdb5cf78bf | -11.3793 | -51.3989 | 2026-09-20 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d9ede536-6c98-3f63-8981-615587cfd9e4 | -11.0991 | -54.0285 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| d97129e1-8927-3b8d-bb61-e2329f32cbdf | -14.6851 | -46.7115 | 2026-09-20 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 03a87409-6ae9-315f-8f8f-a12f84240a06 | -3.7454 | -51.8082 | 2026-09-20 02:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| f5509c56-6375-3e57-9d7c-7831d9c2a527 | -11.2118 | -54.0797 | 2026-09-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8b6a725d-2aa5-3cbe-aee4-361c616fab8e | -6.2948 | -47.6274 | 2026-09-20 02:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fa22d68c-4d3d-386d-a4d5-00ebaca563a5 | -14.7051 | -46.6852 | 2026-09-20 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d03cfa2d-377b-322c-a67b-8937f2ec7282 | -11.8544 | -47.6819 | 2026-09-20 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2d6d51a5-b2e5-3d83-a116-81febc0237bd | -10.2976 | -50.2585 | 2026-09-20 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f0084459-c7ff-38df-b75c-6960e7fd3507 | -12.7629 | -46.1343 | 2026-09-20 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| be0fd4e4-fecd-303b-9dcd-e9a839e6e7de | -9.131 | -45.7273 | 2026-09-20 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 18fc480e-eac3-398b-997a-ed4c78fde0d0 | -6.3134 | -47.6261 | 2026-09-20 02:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 55d63e88-6601-3759-be6a-b1f106eb5c2c | -7.5334 | -45.4367 | 2026-09-20 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| a1a94f36-2604-3f33-bbf5-ac7d2b6ae302 | -5.8408 | -53.5408 | 2026-09-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 352cfad1-ff5d-3f99-ab39-2d5161ef8d5e | -5.841 | -53.5205 | 2026-09-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9131ff98-51de-3933-9c21-8ea84593c9ea | -11.2118 | -54.0797 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 473752fc-755d-38c9-a4c6-c97849376b8c | -6.295 | -47.6055 | 2026-09-20 02:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5cf01a89-6abd-3c64-a252-02f66f4c5f58 | -11.8544 | -47.6819 | 2026-09-20 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 1bd343be-45a2-3aa5-ad51-42376fc79a60 | -12.7629 | -46.1343 | 2026-09-20 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 57e900d2-8f80-3fb0-9ef0-114e3c582bd8 | -11.0991 | -54.0285 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 175.5 |
| bd83b771-910d-3493-944e-41666bef4541 | -11.2307 | -54.078 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 1a8293cf-e811-36ee-bdf6-936223aa824d | -7.3259 | -55.6153 | 2026-09-20 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f1fd7112-bb7d-3784-836c-661fcb24b30e | -8.1686 | -54.7634 | 2026-09-20 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9a3a1493-1d59-3950-af09-3dd560273777 | -11.0989 | -54.049 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 275a7d33-df50-39a1-88f7-71c0d0cac1ef | -2.6125 | -54.7577 | 2026-09-20 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c8dfc9cf-21a7-3a15-9878-4e388bd94152 | -9.131 | -45.7273 | 2026-09-20 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3f586b57-dbac-346e-9013-5a2657734c52 | -7.5334 | -45.4367 | 2026-09-20 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 9f3c2918-9cea-3bc0-ab4b-96411c95fe19 | -7.5525 | -45.4123 | 2026-09-20 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e45d8c75-5b7d-3713-8090-8d26c824abd6 | -11.379 | -51.42 | 2026-09-20 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 1ce25f36-a95e-3f7b-8268-0ca8eb6d1993 | -2.8974 | -57.8181 | 2026-09-20 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| aefa2e47-7c8f-3dc6-adb6-2d69525164a4 | -3.7454 | -51.8082 | 2026-09-20 02:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| bcbe2baf-130a-3631-8660-b69fe27075d8 | -3.6946 | -60.6025 | 2026-09-20 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a3d5b208-7875-33d8-8e06-5ad0f24feb5c | -11.118 | -54.0268 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| e7848f38-f32b-39ac-ad8f-6c231f141aa1 | -11.8547 | -47.6596 | 2026-09-20 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 6a5026be-96e5-307d-b2e4-0ea1063b63ae | -10.2787 | -50.2605 | 2026-09-20 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 069429a4-17ce-3167-9c5b-d267afa81d81 | -11.0802 | -54.0302 | 2026-09-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3cc1c85b-4633-3b58-8b68-c242e193475f | -11.8735 | -47.6793 | 2026-09-20 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 04478069-28f6-36ec-97b5-d381a56ec6d8 | -5.8408 | -53.5408 | 2026-09-20 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9ca0732c-45eb-3055-878e-eb347a77d311 | -6.3134 | -47.6261 | 2026-09-20 02:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d0ea4aeb-dbb4-3069-92b2-feca4307b600 | -7.5337 | -45.4141 | 2026-09-20 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2f7fe009-a8cd-334b-b7fb-6c4c31aa2eca | -17.0284 | -47.149 | 2026-09-20 02:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7fa05995-a73b-3d6c-a25e-95b8412e3b98 | -2.8791 | -57.8184 | 2026-09-20 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 257d0355-47a8-32bc-93ad-635f2893bae9 | -7.5522 | -45.435 | 2026-09-20 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 41d10e10-cd08-38d3-b1a0-905103c919ba | -3.7453 | -51.8288 | 2026-09-20 02:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 119fb876-c1c8-356f-bb8b-ff2b976f7b42 | -2.8791 | -57.799 | 2026-09-20 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ed8fce64-1b0c-392c-9277-13ea7262e301 | -11.8739 | -47.657 | 2026-09-20 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8790ae07-5153-34d3-b244-6f1e30ae40bb | -14.7051 | -46.6852 | 2026-09-20 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f6784038-a793-3cf4-99e1-4d5a9501c994 | -6.2948 | -47.6274 | 2026-09-20 02:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 31707849-887a-3f4e-bcad-97865a5a283a | -10.2976 | -50.2585 | 2026-09-20 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 92824642-602c-3644-8142-78b93244633c | -8.7734 | -48.6651 | 2026-09-20 02:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f9e82111-62ea-3550-9a7e-565fecd743ba | -13.0177 | -46.9125 | 2026-09-20 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a20257b1-ed1d-3de1-8ad2-aeb12ff8be15 | -11.3793 | -51.3989 | 2026-09-20 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 164.5 |
| df7d6045-b7c8-3e55-b650-f9e014a78047 | -13.037 | -46.9096 | 2026-09-20 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f80932d0-946c-3e89-bdf8-f4118b843ed5 | -14.6856 | -46.6886 | 2026-09-20 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 39d59aae-c042-39a6-9494-d82f60773cfd | -2.6125 | -54.7577 | 2026-09-20 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 09e5a1d3-1e75-3693-ab79-6991f532aca4 | -7.3259 | -55.6153 | 2026-09-20 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |


[Clique aqui para ver as próximas entradas](README9.md)
