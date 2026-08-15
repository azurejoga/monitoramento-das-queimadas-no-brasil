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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 608804df-4ca8-3120-a8c1-8c5bbba95a48 | -6.60927 | -56.34259 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75597d93-b094-3332-8b9c-aa264695c36d | -3.59318 | -58.62178 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ad5291a-8761-399e-93f2-52b30e8b3048 | -3.59806 | -58.62254 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 325bf24b-4b07-3608-ab43-f86f93063d2d | -6.94853 | -59.29846 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9fc3fe-ca40-3893-ba85-bde90ccfbc2d | -6.96892 | -59.29574 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 134548e6-d421-3fb4-92d9-987fe6608297 | -6.6202 | -59.08087 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fce40e70-a9d2-3e03-a284-7a0dbe371dbd | -8.02905 | -55.13566 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 47ee5556-9f44-3727-9f42-fc0842e1a0c8 | -6.78575 | -58.74694 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb57934d-1e48-3f32-942a-d04225911f95 | -6.62181 | -59.06964 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e92ecd6-f131-37a5-a5e0-8e708164b1ee | -7.50831 | -72.82552 | 2026-08-15 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cdf769a-1149-3c26-a73d-7531631a37fb | -6.5418 | -55.18183 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 432fe025-a1f3-398b-a8d1-0bb8677b92e3 | -8.6102 | -54.6782 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62bf9e00-4257-3950-8a45-4991adc322d1 | -6.85996 | -56.40239 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd4757d-0cf2-3ce2-a0c7-fb4afbcf9ec8 | -6.59803 | -56.36245 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65231ab1-8b3b-3fcd-ad16-03da58bc54f3 | -6.61733 | -58.99447 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 554d591d-d124-3d28-9dcd-6448561a98b4 | -6.60078 | -59.00359 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdcb92e4-e764-3f9f-adda-dc34718907d8 | -8.89199 | -60.55631 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9503d55b-fe9d-3cd6-b520-24f7cfa52816 | -6.78618 | -58.74393 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffc265f2-2531-3137-8f61-b6637ccecf3d | -7.55325 | -61.16644 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e78c20-d547-3403-9b4d-8995560c924b | -8.25886 | -57.34544 | 2026-08-15 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec623f45-f039-36f0-8c40-3fb898b4e665 | -6.85875 | -56.41127 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b7d3194-9feb-30b8-914c-edd71acd68f1 | -6.59928 | -56.35312 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a27fac2-2614-3e67-a46e-7b648569dc03 | -6.85039 | -56.42823 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c346cea7-adc3-3a7f-8618-83e2c786fe6a | -6.85169 | -58.96343 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b37e2c7-6791-3447-8233-ed2d4094d16d | -6.79175 | -55.84627 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc60dad1-09db-36a7-bbf7-5cfeda4fcf49 | -6.82377 | -56.44637 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c7075b3-4a2d-3861-9c77-ad452fd7182b | -6.58783 | -56.36581 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdaca5a3-8b9b-3626-96e3-3f252a3a306b | -6.95344 | -59.29911 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 160f7f31-9e7f-310e-a130-9aff0cde9004 | -7.6888 | -55.15943 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3ceebe2-0400-33f6-99e5-f65c331fd514 | -6.85695 | -56.42453 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 377e62a3-8caf-36f0-9d6e-bbc84d78ad99 | -7.58896 | -61.2269 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06054a6d-aa12-339d-b19f-c87a36af0f16 | -6.60215 | -56.35009 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e78bc5-287a-3db2-9558-a02300da242c | -6.61284 | -56.34229 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44d1ab1c-d4e3-3a71-a2bd-23750e87644d | -6.96136 | -59.29876 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf8d9c18-6b80-3c54-8ee4-4eabe3f6190d | -8.02829 | -55.13809 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f0459bfa-0b19-36d6-93b3-749c99a6da32 | -6.96056 | -59.30421 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c679f879-2ef0-3d2b-990a-7cbe02d55e01 | -7.39164 | -59.99846 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 459664f8-3479-3c61-a710-ae05bd17ce13 | -6.83262 | -56.42547 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6f0743d-0dbf-3b9a-a545-841798475d9a | -6.72337 | -58.93228 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87ad5a95-c80b-316e-b513-f4a31e8e61aa | -6.79723 | -55.85192 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9101610-a544-32f3-b3b2-0298d10dd4e4 | -6.59581 | -59.00283 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc1cdfcf-2004-3ad8-b0c8-d36fbfa9e245 | -6.95987 | -59.28878 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d64be03-5626-3429-9169-d0203ee4b1d6 | -6.95315 | -59.28639 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36533e21-f9d7-3fb3-9449-216c53834ed4 | -8.64966 | -54.70934 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea2d8cc6-5899-3654-a629-8a175e41523f | -6.79348 | -55.82911 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8e66d1b-7cf5-3052-8cf6-35eba5de30d6 | -8.26455 | -57.34628 | 2026-08-15 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdebb3a1-6b2b-330f-b710-573f1d887a4e | -6.71795 | -58.9344 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6219b932-7128-3497-a55b-a69adda857f6 | -6.59963 | -56.36802 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddae6d41-fe5a-3cd4-b323-3f32cae3dc7a | -6.70004 | -58.95286 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c89e0633-54cd-3d19-bbfb-c576d505e3c6 | -6.63507 | -56.26716 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7498b5-8e35-3602-bec4-e7318cf07412 | -6.61845 | -59.05777 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9242cd6b-e578-3a9e-86e6-dc694a6d63ad | -6.62501 | -59.04736 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b586f633-4a28-321d-bacc-7eae3f28cf7c | -8.6475 | -54.70865 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82368e38-5105-3575-bd6f-400b44689e49 | -6.79083 | -58.74765 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2660d443-96e2-3634-b14e-ce6f84056752 | -7.58284 | -61.23869 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a175af0-7d19-372c-901a-4fbf025a69df | 0.89506 | -59.69672 | 2026-08-15 05:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d999429-4cc7-3125-8222-cdd819b83b96 | -8.97388 | -60.53568 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e373bec-9b3e-3158-a8b0-9e8333d4a0d0 | -6.61348 | -59.05713 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 426061be-efc7-3c85-ac5a-db5874ffa6c8 | -6.79285 | -55.83386 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2b33a4-d2d6-3d46-b62f-f1fc0e47203e | -7.58463 | -61.22629 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a5476ea-0729-3a69-8bf2-ea626621613e | -6.95497 | -59.28806 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72dd2687-9503-3a5b-8623-64726f993e33 | -6.5425 | -55.17649 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c048a25-f87a-32f6-bfe8-72a30f138926 | -6.79789 | -55.84723 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad4c795e-1051-3872-bc79-61f202d90cb4 | -6.60864 | -56.34709 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e6a368-cde7-3aab-888b-aac5579e49e5 | -8.98315 | -60.53708 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92b65a42-be8b-32f9-b313-8c082a29cc5a | -6.53612 | -55.17544 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 538a58f7-8b75-30bf-8484-6b2b4a4baaec | -6.60736 | -58.99302 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e02a5aac-af96-352c-9f25-568d01061c40 | -6.61924 | -59.05223 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5dd5426-d6f7-3e17-90b1-f4a9c2027430 | -6.61766 | -59.06332 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d232b783-a0c5-3524-a5d9-bedb8c0e3c89 | -6.79837 | -55.83954 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3983269-4caa-3d39-a1db-5a6134616bbc | -6.83797 | -56.43068 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a64a40e6-d910-3c86-9759-797572eaab9b | -8.95866 | -60.50867 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d43a37be-c3bd-3c14-b2d7-6a8017d29fb7 | -6.79308 | -55.83679 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a9b5059-e275-3cee-b782-1f499fbae676 | -6.61269 | -59.06263 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48f69b43-a8bc-3c8b-8c2a-2a988a5774bd | -6.60339 | -56.36766 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb97c092-8392-3e6b-9a56-55221097f221 | -7.58717 | -61.23932 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f41db08-da15-3a0b-9c17-b841e1e46008 | -8.96331 | -60.50932 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b60b796-b659-37d8-aa55-cca0737853c0 | -6.59215 | -56.36119 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3882ee5f-2f1f-3446-b5ef-8a9bc3951273 | -6.85935 | -56.40688 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96a4df73-7651-3119-90c4-321c978fb222 | -6.60088 | -56.35916 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b391c92e-3efa-3b5c-a325-45ee30523405 | -6.85815 | -56.41565 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9215ad0b-0778-3e58-b971-58c9097c8957 | -6.61506 | -59.04606 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31dc1717-a489-3a25-bb8d-54c35f7a0674 | -6.69462 | -58.95508 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872867a8-0c92-35f1-91b6-3eb8ff5674a0 | -8.95533 | -60.533 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a84c321-ad55-3c30-a90e-62839134600c | -6.20583 | -57.76851 | 2026-08-15 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 86c04341-801e-3682-9f99-4a7b281710fe | -3.59659 | -58.61529 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 489cd0d9-a87c-3fc9-819a-3b48658ce076 | -7.45734 | -55.30765 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a99a2f29-c9ae-3f72-a68b-52a2185edb41 | -6.80127 | -58.77182 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e7bf198-012c-392a-ac2e-409053b37ec5 | -8.60397 | -54.68988 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c5a3337-6045-3fe6-96b3-ee3d803428d8 | -6.61153 | -58.99945 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| db3329d6-de43-363f-8f9e-70e674f97a73 | -6.70587 | -58.94765 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71f15dec-138e-39d0-99b0-c2a2472dbd0a | -3.23599 | -61.1669 | 2026-08-15 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf7e6c2a-1d31-3495-ae04-d994008e908d | -6.85755 | -56.42006 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85847172-d08c-3344-a7dc-3c004619bd85 | -8.60266 | -54.68335 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26b9ce0c-3173-3487-beac-6bf3b453d903 | -6.8492 | -56.43703 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f895d03-6075-32d9-a088-17663ec29da6 | -8.26403 | -57.35009 | 2026-08-15 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44176d48-7df8-304b-bf37-93f3a9402145 | -6.79159 | -55.84337 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d948b7e7-1ea4-301c-8d71-3bb5d211ed19 | -6.80255 | -58.77422 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00542336-d7c5-389b-8dc6-0a649ce2bf7e | -6.65866 | -59.10434 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bf590c1-d7d9-3548-a264-c1ec59875823 | -6.79748 | -58.77341 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README45.md)
