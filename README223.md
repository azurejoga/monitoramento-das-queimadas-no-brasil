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

## Dados Diários - Página 223

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 753b3445-a973-3edd-8ed6-c8042ec8c3f9 | -9.40359 | -66.5464 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aac7624a-b2dd-3d07-81cc-ba7ee9c0d554 | -9.39933 | -66.54088 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2609e2f3-6969-357d-baab-d93279fe48f3 | -9.39892 | -66.54406 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83bea3d1-4b4d-3c00-82b3-b287e7d91317 | -9.39879 | -66.5425 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10cb3f93-7fc0-37b1-9d00-1b3975fcb4a1 | -9.39852 | -66.54723 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b498cd88-8278-36a0-84d4-ee75b74ea3fe | -9.39836 | -66.54566 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c13363-2dc4-35d6-8e2d-1314a707b37b | -9.39806 | -63.65572 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b13e036-18b7-3ab2-873f-927dca49ab19 | -9.38894 | -63.41436 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79f34df0-b677-3f40-8aa3-ebaf589ca5ae | -9.38833 | -63.41938 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecfcac88-2cae-39a3-9bda-30c4945ca808 | -9.3874 | -63.4136 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3eb9b69-d7f5-3b5c-b8b4-1004e96d770f | -9.38676 | -63.41859 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00b84815-2ede-3a14-9097-3745124fc92d | -9.38194 | -63.41842 | 2024-10-09 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdcec427-5015-3987-aacb-5559822912aa | -9.16983 | -66.05247 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dfab0c3-4f97-3847-a00b-6fec98b868ae | -9.16446 | -66.05161 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75da2f4-d5ef-3d70-ae87-9e473df4de84 | -9.16396 | -61.57053 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 089c960c-16ba-37dc-9aa2-a1538687b4b4 | -9.16127 | -62.21949 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d47002-bae4-3c6d-b919-ae4224e191f1 | -9.16067 | -61.56864 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4fcd029-0590-3105-a152-b88a1572fc19 | -9.15987 | -61.57558 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c04f027-69f5-320b-b7cd-f788f09d58cb | -9.15951 | -66.04744 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f12c58-8766-3eb0-a2de-1915847af4a6 | -9.15907 | -66.05083 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9db905ac-12b8-3655-a86c-28fcafc8b4ff | -9.15862 | -66.04105 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596fe377-93b2-32c7-b8d1-852f7c24ac87 | -9.15769 | -66.04784 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcbf8e1-729e-345d-bc34-792b69d6dae5 | -9.15723 | -66.05122 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58c6993-663b-3138-8fd1-844e0466f5c2 | -9.15684 | -61.56954 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 127eaabe-9549-34fb-895d-0e384d3f3ce6 | -9.15498 | -66.03995 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5a4eb26-e26d-3118-88f8-23e24801641f | -9.15455 | -66.04335 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a7fc39a-8c50-349d-aeca-b498e38abd22 | -9.15442 | -62.21851 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd0b011-e437-3b5c-80fb-108b94fcfd90 | -9.15411 | -66.04675 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36ea965-96e0-3f72-a9b5-4d3819d69201 | -9.15368 | -66.05012 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f0ebb24-936b-39c8-b7b3-752f0c5b58a3 | -9.15322 | -66.04039 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb16a681-ef9b-3469-a6b9-98eafcfe40c7 | -9.15275 | -66.04379 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d83ee02-a98c-3969-9ab5-92a19a31e343 | -9.1523 | -66.04716 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94ea0ce9-5cd7-3f37-ab59-3d87f00ff35e | -9.14915 | -66.04269 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61ca7fb5-92c4-35df-a62d-4f4c9bb1bb54 | -9.14872 | -66.04605 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0a1166-671a-3116-837b-3d003bfccf00 | -9.14829 | -66.04941 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 877de9d6-aa9f-39a1-9333-a19c3f6fadb8 | -9.14735 | -66.04314 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c04ee3fd-90e1-33fc-b144-da7444a61363 | -9.1469 | -66.04648 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50cf3ade-8f19-34b8-bd1d-fc36b3b63df7 | -9.14332 | -66.04531 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f41eab3d-f4cc-30e6-8ff1-d9208921286d | -9.14152 | -66.04572 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 203f4a61-3dbd-3ce3-bda3-14feeb90635a | -9.09804 | -61.13793 | 2024-10-09 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9412db34-4f7f-38fc-bfe0-aeabd3054b94 | -9.09076 | -61.1369 | 2024-10-09 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 220ecc21-e93d-3e9f-9f0e-e2d9d9234cb0 | -9.05491 | -63.23721 | 2024-10-09 06:20:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d9c880b-b2a6-38a6-aa24-5136de873480 | -9.04846 | -63.23634 | 2024-10-09 06:20:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adef62ca-f4d3-3c6f-8d1c-860399785e97 | -9.02041 | -67.26806 | 2024-10-09 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8bf16c4-edca-3bfc-80ac-420bf09adb71 | -8.929 | -72.83856 | 2024-10-09 06:20:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e34d889a-3505-3353-a88e-18aaea527a16 | -8.52128 | -70.0464 | 2024-10-09 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13d76636-103e-3541-b219-908d5e010fbe | -7.35735 | -64.66487 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87be24bd-0c2c-3946-8749-fd85ae805820 | -7.35681 | -64.66888 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d63b5d-dd1b-3e02-8977-7501e857526f | -7.35627 | -64.67288 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ae04ef8-6329-3c92-9f48-45eb293564cb | -7.35574 | -64.67688 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25613304-eba6-321e-b7b3-9ca775b5587b | -7.35105 | -64.66808 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a1d0ac-710e-3c60-8780-56b4802fa86a | -7.35052 | -64.67207 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ef66e3b-e7a1-3ef8-8973-d09124c84d8f | -13.40901 | -61.92155 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25fcb41-c312-3c71-b747-ceac74c14910 | -13.40882 | -61.924 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 882036f0-c755-3bb7-884a-e2c4d52d7dde | -13.40169 | -61.92071 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cfb429db-5f5f-331c-a649-b889d803801a | -13.40151 | -61.9232 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b2a7c41-3395-33dd-8779-f327d9272725 | -13.40095 | -61.92828 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86210ada-c267-34da-8a18-4e1bd2a9feee | -13.39419 | -61.92239 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfad5c78-e026-35d4-aed4-1b249f07d57a | -13.39364 | -61.92743 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 510e2eaa-0361-301b-a45e-1fad2289e869 | -13.39341 | -61.92991 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d82b413b-4128-38e8-b25a-b4eb82c55fd7 | -13.38224 | -61.96665 | 2024-10-09 06:20:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 06da426e-2120-301c-bdb4-9ce85ac4ed86 | -12.96495 | -62.48529 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd512612-b95f-3aee-871b-94ada73f4f55 | -12.95789 | -62.48446 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe538e84-c874-322a-961f-6f132e66f753 | -12.95718 | -62.4913 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c3806d1-f214-331d-92c8-4c0d62210109 | -12.9539 | -62.48548 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec535162-726e-3d30-abcc-babe70376e8a | -12.95315 | -62.4923 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4019d9a6-c02c-3e28-99d9-c5d31d167464 | -12.93644 | -62.44881 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c474b003-221e-35bd-94de-15ed53058ef2 | -12.9357 | -62.45565 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be03625d-8bf6-389f-a2f1-a1b650827ead | -12.86965 | -62.80534 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e32c6238-3ee7-308c-aaca-6e9e59bfb60b | -12.86273 | -62.80455 | 2024-10-09 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87acede3-7389-3e4f-a2ff-181bd001a760 | -12.76447 | -62.26873 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a699994d-bb65-39de-b94c-c32ff57b7a00 | -12.76225 | -62.26356 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ee97685-53e2-3dc8-9cda-50f6363d8d37 | -12.76148 | -62.27054 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f01ff9b1-3a72-30ce-bd21-f8e4a25349b0 | -12.75877 | -62.25391 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee4a483d-4374-39b3-a92e-7df4238d2ac2 | -12.75806 | -62.26088 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f04699c7-8c06-3ac9-866d-43ca562aa1cb | -12.75734 | -62.26788 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cec25f2-e179-3abb-9d4a-1073ae151a34 | -12.75588 | -62.25574 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f94f964-6e65-38e2-bb0a-d97ba07d79ba | -12.75435 | -62.26973 | 2024-10-09 06:20:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2aec64ff-1149-3786-8678-a50779800f58 | -12.13958 | -63.36388 | 2024-10-09 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ef98fd1-b335-302b-a5ec-b7f6d7364003 | -12.13559 | -63.36066 | 2024-10-09 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb9eb3d6-0b1c-32f9-ba60-2e013ff71ff9 | -12.13492 | -63.3664 | 2024-10-09 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2e49628-d260-3bcb-bbcb-aae453470fd6 | -12.13294 | -63.36308 | 2024-10-09 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aad1cdfe-1403-3705-b0b0-e3165e114cd0 | -11.89465 | -63.27922 | 2024-10-09 06:20:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a04eb9a-6cf8-3fba-ad70-0ade340dbda0 | -11.89399 | -63.28501 | 2024-10-09 06:20:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cf66e42-bfd1-38b9-8342-0c79f4a8a8cd | -11.88732 | -63.28432 | 2024-10-09 06:20:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d957726d-b92d-32fa-82b8-4fbcc3be4406 | -11.78044 | -62.88351 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c68c883-66a8-3ea7-a8e8-0b99456c364c | -11.77861 | -62.88409 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b42cea76-2dfa-3163-91a7-adba73184c5a | -11.77362 | -62.88277 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15ab5f7f-9284-3d84-a83a-28744227eb63 | -11.7718 | -62.88335 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 989eab32-31e9-3632-a558-305d1bd750cf | -11.76682 | -62.88189 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb438937-2fdb-3af0-a7e9-59ded5509718 | -11.76501 | -62.88244 | 2024-10-09 06:20:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e124ff2a-dec4-305b-91c2-41d23508a70f | -11.71532 | -65.00281 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d158f4f1-6985-35af-8e1f-161c19ebcb86 | -11.71477 | -65.00726 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1751b4c3-7b81-3805-b7c4-84a0e08f43de | -11.71208 | -65.00406 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b7ab315-5402-3290-a4fd-ab6100e38753 | -11.70935 | -65.00201 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e6d3c77-e5e2-315c-a445-84afdc718c96 | -11.70881 | -65.00647 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a259c080-8251-335b-a731-5ec5c1110783 | -11.70825 | -65.01096 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 351032d5-ceb8-380a-85da-548399923157 | -11.70662 | -64.99886 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f9eda3f-1ff4-30de-b739-54330222314a | -11.70611 | -65.00327 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 031011c9-9baf-3638-bbd9-31c8437a1a27 | -11.7056 | -65.00776 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README224.md)
