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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3e23527-a5d3-3ec7-805e-baad18474742 | -9.38697 | -60.54317 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1afb1835-a2b2-3056-8693-7f82c2bfc15a | -11.4052 | -58.54108 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d683628a-1e64-3a4b-89e5-f05238e95746 | -9.34284 | -62.58681 | 2025-08-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0754ab9e-f3f9-3c5b-8290-430d7e04e523 | -9.40006 | -60.54106 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7885498-f225-325f-873a-b4d9b92cb853 | -13.04778 | -56.84056 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1350ae-c227-3ba7-b97f-05d23ef5ea13 | -7.52743 | -61.37254 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d9a973d-2f5d-3988-b6e2-0cedb66cf72d | -9.17198 | -59.69073 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2350813-c052-3da4-a714-60ba274a2671 | -11.31794 | -55.20102 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a5b5e95-4d3f-3437-8a8e-dfb0db6fe2bf | -8.61391 | -60.60544 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb7fbcf0-f0b1-378a-a0d8-9be6e40ca08b | -9.0556 | -60.65639 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72751de3-71c8-389c-9079-c686a6ad0bc4 | -9.15522 | -59.4272 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b8ce66-5889-32be-963d-fb22fed6364c | -7.59917 | -63.50252 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d4abdca4-e666-392e-88e6-b0b576342caf | -8.10654 | -61.19129 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32de5f25-7e77-3cb5-a209-3725f2ed32de | -9.14686 | -59.42136 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10fe71fb-25f4-34c1-b31d-d86efa27aaba | -13.12525 | -57.1424 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53ff5754-359f-31c4-8e94-49192c9f16af | -8.11047 | -61.19188 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 87eba00e-39fe-3f1b-b65e-2afdcab71662 | -9.39116 | -60.54375 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b0a16a1c-8a35-3813-a1ee-af266e5b35c2 | -7.95792 | -61.76573 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9083b97f-000e-3e6a-8a6c-44b118c8a128 | -8.91165 | -60.73393 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a19c4b-1ddb-36b3-a185-7c61c943da97 | -9.78845 | -61.50436 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1b95d3b-d703-32b6-8239-86b6d010b14b | -7.54206 | -63.48207 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ade32cd-3e2a-3e8f-91b4-d866809bd914 | -13.1197 | -57.14169 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 384ae2aa-00f6-3188-af90-8329c3264990 | -8.56356 | -63.91216 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcc45c6e-26b5-3081-8439-37abde85490e | -8.56013 | -63.91163 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3cb069d-5662-3a26-a911-95be26969685 | -13.11887 | -57.14895 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 074cd6a0-7abe-3f90-891e-5194ab8b75dc | -9.50233 | -60.5508 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe4a5c07-ce50-3279-bfc1-80abc117534b | -9.21718 | -59.6571 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd710f89-8f7a-3225-b29a-b992fb18387f | -9.37633 | -61.5298 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e8b48dd-24d3-350d-914e-02a44c3b875c | -13.4747 | -56.66771 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 447a5d9d-cea8-3ea2-8cd1-5f57da9a565a | -11.44087 | -61.45465 | 2025-08-15 05:44:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3d371c4f-3818-36d3-8477-02317c93653c | -9.94402 | -60.4784 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d564293-c0ee-366e-bd77-c2bed68d7148 | -9.15402 | -59.65703 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a290995-0da0-3021-98cf-e72718f99c9a | -9.18615 | -59.65298 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d87432e-9113-34c3-ab6e-9c650589be3d | -8.68852 | -62.45972 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d65156f-8f3e-31d9-9544-8c9286ea8a61 | -11.83371 | -55.21593 | 2025-08-15 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab119ba-e856-31e2-9438-b68d51c478b2 | -9.21013 | -59.64282 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33e1484d-2979-327f-af98-6f8a89f84467 | -9.16347 | -59.65387 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5981ce9a-9c80-3164-b70b-1ed72d82cc05 | -11.34886 | -55.41463 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 963ed26d-af9d-35ca-a973-9b62e88e408c | -9.8346 | -60.76416 | 2025-08-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 540b195d-87c7-310b-b02f-7d1a52740525 | -9.17053 | -59.66828 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 69aff728-91ce-309f-8182-056664cf9b07 | -10.33665 | -64.44826 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5fbfb6b-e61f-3237-a4c4-08de010270a2 | -9.187 | -59.67967 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1444868-e902-3c53-8b30-07f0ad704d7d | -7.87348 | -61.81454 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80452f21-4b40-36a7-95cd-76f215265afb | -9.51232 | -60.54041 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3188c8c6-dfc6-3954-8019-c3fb859c10d6 | -10.11057 | -64.43723 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf739cc-0e93-3fe3-9429-a15e6b9b919b | -9.7924 | -61.50493 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdb8d331-4354-327f-a0b4-cb783bac43b3 | -9.00935 | -59.53679 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91ab776b-279e-3c2b-8954-dd3331ee8ac6 | -7.59976 | -63.4987 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be3aeec1-1ca7-312c-8116-ace8058d2d3c | -7.87658 | -61.81975 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb8097e1-9532-3740-90b7-521a3dd30f51 | -8.11993 | -55.5817 | 2025-08-15 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b30c0ecc-7948-3740-848d-d1a5049bac97 | -9.95772 | -67.20788 | 2025-08-15 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b14f669-cbd0-33a8-a488-039c06152f3e | -10.35261 | -64.45847 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b104402-adc2-334f-8da2-68a5d46d2960 | -7.54148 | -63.48589 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88ec8b4-985b-388a-8279-b7fd0ff52bbe | -9.38644 | -60.54703 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7abf24ec-e1c1-31c5-a96d-1c9289bfadbe | -7.28321 | -64.69541 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3bfe2727-2b67-3951-8d81-84977d7d4ef3 | -9.39587 | -60.54049 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb77844e-4b3b-3cc4-85bc-6d742c3389c6 | -7.95828 | -63.46054 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4053582-bc40-36a1-b798-ca82419c27c3 | -11.35383 | -55.42461 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 032107a2-8ae3-3579-8e7f-9f3073d86944 | -7.59914 | -63.52594 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111804fb-b275-3d5d-98d4-aa11eecab814 | -9.15434 | -59.68805 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cb3bf6a-98e5-33a9-b66d-1235d13e4f34 | -7.62758 | -63.51827 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995055e0-586c-361d-9105-4e9694ac796a | -11.35881 | -55.43438 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fd2dc1ee-1f7a-324b-baac-3d703c6e94be | -8.48048 | -64.04515 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01699bee-9d95-34b4-a8b6-2f5b43965e9d | -8.567 | -63.91268 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c95035b-f336-35c9-8d16-47f44973f527 | -9.18496 | -59.66171 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1692c1f4-0710-33cd-8998-ecc7cc9e51fb | -7.499 | -61.31219 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4de58c8-ce70-34fd-b4a1-1d0af1db0ac9 | -8.6714 | -62.44822 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b7692a-e9f9-309f-a978-a47c8862c608 | -8.59835 | -62.66388 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 642232c3-c463-3dbc-8b5d-0a7f3251f7c7 | -9.98361 | -66.85066 | 2025-08-15 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01b3588f-4c65-3d0c-8a85-acad82d7cc21 | -7.60722 | -63.51936 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eab1f615-e6d9-30c4-803e-fc5d827075dc | -7.60951 | -63.52752 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8376c6f-0385-317e-94cf-7dd4c77e6739 | -8.876 | -63.93127 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4eef1d75-0ee9-3cb8-b265-d3ddf83eb316 | -9.15344 | -59.66135 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11b9a995-0eb8-3217-908a-82f8a911f126 | -9.16552 | -59.672 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a840f8-214a-339a-a0f1-cd4b7167ccad | -10.49501 | -67.89214 | 2025-08-15 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95842324-6c90-32c6-b241-78eb9ddcd446 | -13.11216 | -57.16273 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7de7b3ff-0eb1-3569-bfd1-d48f521447b6 | -9.18054 | -59.66102 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 387e8b77-c236-342b-af74-23fb75608b08 | -10.56368 | -67.9481 | 2025-08-15 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 739610f9-d0f2-332f-b1a7-da47543ace06 | -7.96103 | -61.77092 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9cfe5df-573d-3bab-9897-1d630ccdf21d | -11.40942 | -58.54726 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 361b4032-e7ad-302d-a81f-059de5170744 | -13.11261 | -57.15911 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6994df67-7db1-3d8e-903b-5b31368f7130 | -9.20088 | -59.67708 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eead49a-bda3-3a4f-a1de-e8a3f2a0e118 | -10.3583 | -64.44392 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdbf9900-6413-3cb2-82cd-4b215c57ce48 | -9.34652 | -62.58737 | 2025-08-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0138ff7e-a9d1-39c1-8874-9e76e6d6171f | -9.20569 | -59.64223 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e0f0c2f2-c8b7-34e1-8689-3a3cccc99998 | -9.19083 | -59.6846 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abcff6a3-b1fa-34d8-b618-86b3d05b140a | -9.1561 | -59.67501 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94b6fd82-fa89-317b-a324-8d21171ee8f7 | -9.50179 | -60.55463 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d78ecada-8c5e-324f-9bc7-cf1b6fa2ee03 | -9.79313 | -61.49979 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81219976-f319-37c6-80d9-044018832950 | -13.11681 | -57.17073 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2ee4274-23b3-36a9-9562-3bee1c692245 | -10.11819 | -57.76432 | 2025-08-15 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ed4827e-4d39-369d-9b25-e45f0c4270c9 | -7.53301 | -61.33393 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fb7296c5-ce80-3837-85ea-88258624d519 | -13.47322 | -56.66851 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d9baa8b0-74c6-3718-8f46-2e8601d743e5 | -9.91976 | -63.18703 | 2025-08-15 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86711a02-5468-33f9-b12e-de64efad0247 | -9.71886 | -61.28912 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29199433-2648-3e5c-899e-bead9b72d729 | -9.51286 | -60.53655 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6600d972-e96a-30d2-9f13-d0a4e09f6a6f | -15.39355 | -55.78029 | 2025-08-15 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 881e42c6-6958-3472-8d6c-98642e41dd4c | -7.58942 | -63.45014 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d75e195-93b3-3bc4-9535-acfcd4920d9e | -7.95103 | -61.75994 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82427c2b-255d-3c42-8bd6-e3b4a3832aec | -8.72467 | -63.14677 | 2025-08-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
