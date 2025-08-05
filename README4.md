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
| 59082a3e-3877-3846-9f8a-dad63b9768fe | -11.9399 | -44.9497 | 2025-08-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fe00bb25-2b0f-3830-9376-3fd641f5b276 | -11.9211 | -44.9293 | 2025-08-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 27db221a-03b9-3452-a73f-e21dbe6d0d8f | -8.9478 | -46.7354 | 2025-08-05 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 78c18206-8c08-3bca-a639-0781ec06641a | -10.3311 | -47.8256 | 2025-08-05 01:00:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5ec38651-a0c3-3d9e-9ab7-8945b68bc0e3 | -3.1833 | -49.4429 | 2025-08-05 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| ac7863e8-4404-3f74-9676-89dd95351bab | -10.4406 | -44.3749 | 2025-08-05 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a92a7279-76a4-3377-8708-9e427b57542f | -9.3989 | -45.4928 | 2025-08-05 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7ebcfd9a-7dbe-38b0-bee4-560b221eb262 | -11.9211 | -44.9293 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| cbf65ae6-88f5-3c3a-969c-986819fc757f | -8.9478 | -46.7354 | 2025-08-05 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0ecaf51e-69d7-3580-bf0a-0cb2a9c88026 | -13.0535 | -56.8947 | 2025-08-05 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7a485a70-9999-32db-a66c-1b0861ab493c | -14.308 | -54.7078 | 2025-08-05 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6cb87e54-eef7-390c-b750-67bffe66b748 | -11.9015 | -44.9554 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| fe68b3b2-ce7c-312d-a493-333a2d24f7e7 | -13.0533 | -56.9149 | 2025-08-05 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e00bbd25-018e-3802-98f1-10829951156f | -11.9019 | -44.9322 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| afec1f1d-9ff7-33c5-a9ec-633e0682c3c0 | -14.3083 | -54.6871 | 2025-08-05 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4a2de78b-7c47-3df0-9dd9-9c61723fda05 | -10.3311 | -47.8256 | 2025-08-05 01:10:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6b003456-9312-3508-bf13-9cf736a42f4a | -13.0538 | -56.8746 | 2025-08-05 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c671144d-5bc3-36be-bc0d-788fc95c5a2a | -7.994 | -43.1534 | 2025-08-05 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.7 |
| d8710416-e19a-36ee-8b20-a72f8c5d90ba | -9.3985 | -45.5156 | 2025-08-05 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f22ef5fb-98a5-3dcc-914f-ae60a88bbbcf | -9.3989 | -45.4928 | 2025-08-05 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 73fed986-7d32-3ae9-8483-73cadec07178 | -11.9399 | -44.9497 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bd6b3e17-5e93-3cc7-8a1e-07e474c9aba0 | -11.9207 | -44.9525 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 0aea734c-8b38-3676-87c4-28e761f2254b | -11.9403 | -44.9264 | 2025-08-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 55b16e7a-8e7e-3360-9fe3-35a44d2c1e12 | -13.066 | -56.888401 | 2025-08-05 01:16:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0130e0-2781-38f6-bacf-2f864c7bbb0f | -9.7136 | -66.047897 | 2025-08-05 01:16:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b75e6493-a449-3977-9a20-cd2f7276e782 | -13.0532 | -56.878201 | 2025-08-05 01:16:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2b4eee7-f9f1-3b88-99b5-d2a8cc4cdf6d | -8.9166 | -60.545101 | 2025-08-05 01:16:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1643a090-e876-34bd-b9be-ac05e6ed9b2a | -13.0629 | -56.875702 | 2025-08-05 01:16:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0ec2156-eef3-3239-9e70-92e492202e7f | -8.9227 | -60.571201 | 2025-08-05 01:16:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6ce7a39-e904-3c86-862b-c69e68a7290e | -8.9186 | -60.553799 | 2025-08-05 01:16:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c36450eb-a316-36ec-9283-a0e01d1f3907 | -8.9206 | -60.5625 | 2025-08-05 01:16:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62d414f8-8bbf-3a3d-804a-b884fca3b42a | -13.0597 | -56.862999 | 2025-08-05 01:16:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3061c995-9f15-361a-8ed6-3bf249e38471 | -13.0563 | -56.8909 | 2025-08-05 01:16:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfb4df8-e3cb-3e8c-8146-f5ddfa0f371b | -3.4906 | -59.363701 | 2025-08-05 01:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaee097d-7a47-3ea8-89b8-89eb745df5f9 | -8.9145 | -60.5364 | 2025-08-05 01:16:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52c1ba57-0523-3ddb-804e-bcd0cdf3e461 | -7.994 | -43.1534 | 2025-08-05 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.8 |
| b8158afe-81be-3ca4-ac1b-a30ac32a5a3d | -9.3985 | -45.5156 | 2025-08-05 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c64e69da-f53f-3a19-ad5e-7c9941f5cca1 | -8.9478 | -46.7354 | 2025-08-05 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3608a059-5aa8-31c1-bea5-a045da2f2c59 | -13.0914 | -56.9114 | 2025-08-05 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3c1b0bb5-6f83-3b5f-b69d-d1ce4452daa8 | -9.3989 | -45.4928 | 2025-08-05 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 5c0340b2-dc87-3f4b-9856-1d3ff59c64b6 | -13.0726 | -56.893 | 2025-08-05 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e076f734-1783-33bf-83ee-cc6e45a7cd53 | -17.2256 | -44.817 | 2025-08-05 01:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 531c79b0-ccbd-31fd-8143-a5450c4c411b | -17.2056 | -44.8214 | 2025-08-05 01:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4284f595-ec9b-35a7-8318-d37a61653a3a | -10.3311 | -47.8256 | 2025-08-05 01:20:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7d362fdd-98df-3633-b4a4-88235a2db207 | -13.0723 | -56.9131 | 2025-08-05 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 950448c1-d866-3a5e-b3d5-8e133c8a98f2 | -13.07594 | -56.89124 | 2025-08-05 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8a417f75-6fd3-335e-bd74-db88f7a18a7c | -13.08768 | -56.90129 | 2025-08-05 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6bfc0aed-7549-364b-8897-8012ff39b717 | -13.06419 | -56.88124 | 2025-08-05 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1a1b4b5f-c3e2-35c8-a2ed-e93927e9c9a4 | -13.07772 | -56.90297 | 2025-08-05 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ac497579-5690-3a33-be2a-c5a188022477 | -13.07949 | -56.91463 | 2025-08-05 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 2a934181-7673-313c-83ad-b3e261863af4 | -6.63734 | -60.00162 | 2025-08-05 01:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8ce3a7a8-5ee4-3240-86ae-8e8c673aca5a | -6.62156 | -59.95577 | 2025-08-05 01:26:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5fc6ff9-ee8f-35d7-b09a-34b5e1626161 | -6.62423 | -59.97467 | 2025-08-05 01:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ab458a38-61f1-38cb-bfb4-561a49f993fb | -6.62289 | -59.96523 | 2025-08-05 01:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 324fc764-7aeb-3f4b-be19-6c18ff54ad29 | -9.70809 | -66.06512 | 2025-08-05 01:26:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f5551b8e-1a62-3ca4-8ddc-f651a18c7d01 | -6.15532 | -57.91454 | 2025-08-05 01:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 70b4d6bb-85a4-3350-86b2-a082495606a8 | -6.65528 | -59.10228 | 2025-08-05 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3b368e3f-4564-30d8-8e53-8947cc5d03d1 | -5.98855 | -61.35446 | 2025-08-05 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd30a716-d274-3c72-9c0e-a5ce749ba115 | -3.4907 | -59.37937 | 2025-08-05 01:28:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f57e4699-7e35-32fd-90ec-1423b4599c08 | -3.48917 | -59.36853 | 2025-08-05 01:28:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fb34ce77-59c9-3996-9005-ed546a08a66f | -3.49891 | -59.36711 | 2025-08-05 01:28:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c74398d8-8303-3e23-ba98-5607b731c91c | -8.9478 | -46.7354 | 2025-08-05 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3c900dad-7c39-303f-b902-476dc36071ce | -17.205 | -44.8454 | 2025-08-05 01:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c7f52b30-a09d-3619-b1a0-6c107d6655d5 | -8.9227 | -60.5568 | 2025-08-05 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3fded113-1638-3fc6-909f-04c0bf088386 | -9.3985 | -45.5156 | 2025-08-05 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6020b877-39f5-374c-94bd-9d2c0e750b19 | -17.2256 | -44.817 | 2025-08-05 01:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 62a977bd-f234-30f0-832d-a12dcb090d21 | -10.3311 | -47.8256 | 2025-08-05 01:30:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a8f94835-3ac9-350f-8f89-a9aec88a6df2 | -8.9228 | -60.5376 | 2025-08-05 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| aaa5732e-7ef8-36a0-ba57-f758898aac1d | -11.9207 | -44.9525 | 2025-08-05 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| afdbc632-6ecd-3546-8ab5-211d8eaa3331 | -9.3989 | -45.4928 | 2025-08-05 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 09c165f3-1d83-3016-9692-66c71b1b573d | -17.2056 | -44.8214 | 2025-08-05 01:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 68be5275-ce7b-3da2-aea1-2e95cc79121e | -8.9225 | -60.576 | 2025-08-05 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 35bbe750-f0ce-3def-a613-f1565e860c67 | -11.9207 | -44.9525 | 2025-08-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 6125a44f-4647-39f1-af89-003397ea5bf2 | -10.3311 | -47.8256 | 2025-08-05 01:40:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 49cd793f-28c7-3de0-8b4a-d9a91676e3da | -8.9228 | -60.5376 | 2025-08-05 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| ea1a31c6-1384-35fb-8598-603410da3abe | -9.3985 | -45.5156 | 2025-08-05 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 44c31dee-591e-3d68-b343-0109c2c4b511 | -8.9412 | -60.5559 | 2025-08-05 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 32265f6c-d087-387a-b8ea-da0d8de716d1 | -8.0132 | -43.1278 | 2025-08-05 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 6c681a76-f634-3edc-b3ca-6d0281ae5c10 | -17.2056 | -44.8214 | 2025-08-05 01:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c99f6823-9349-3d27-8847-331aaa4d752e | -8.9224 | -60.5953 | 2025-08-05 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ea8c1bfa-0a3c-32f9-bc8e-49ecda3ed504 | -8.9478 | -46.7354 | 2025-08-05 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 678398a6-3ab4-3325-8bcc-d95b455055ff | -8.9227 | -60.5568 | 2025-08-05 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 8e6eca01-23ff-3c2d-af56-a59308636da6 | -9.3989 | -45.4928 | 2025-08-05 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 70eae5de-eb0b-36ef-9ad5-628ee6537c3b | -17.2256 | -44.817 | 2025-08-05 01:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 841c4faf-9192-3efb-84ed-86fa9e7ddc3d | -7.994 | -43.1534 | 2025-08-05 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.3 |
| f849a8cf-a5f1-3b9a-a38d-04a4fc19d7ab | -17.225 | -44.841 | 2025-08-05 01:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 4b7d5298-04ad-3266-9b0a-f888bfd6783a | -8.0132 | -43.1278 | 2025-08-05 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 783825dd-31ae-3eb9-96e4-85e02d94636b | -8.9225 | -60.576 | 2025-08-05 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 65ad390c-813d-3210-bf24-4df4b9de7db5 | -7.9943 | -43.1298 | 2025-08-05 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 213bcda0-69ca-3c8f-9a74-1f8c45b34f36 | -17.2256 | -44.817 | 2025-08-05 01:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8c184854-f529-3347-997f-b9b6cf2e928e | -8.0129 | -43.1513 | 2025-08-05 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| a7b272a7-9133-39e2-a24f-a0d8793799a3 | -8.9228 | -60.5376 | 2025-08-05 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 8a9817cb-7d0f-3ccd-a0ab-0691011d8d7a | -9.3989 | -45.4928 | 2025-08-05 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4c28dce9-72e2-3896-8f41-d7d216ed5237 | -10.3311 | -47.8256 | 2025-08-05 01:50:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 35777ab4-2335-3331-9fb7-8f599a6c73da | -8.9227 | -60.5568 | 2025-08-05 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 47aeb66e-4f20-3025-81a1-f00427691d33 | -17.2056 | -44.8214 | 2025-08-05 01:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 97330d5d-3a3f-35e7-9918-287383bc2a0a | -8.9224 | -60.5953 | 2025-08-05 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 11560dbd-4a3b-3612-b969-7fec632bd760 | -11.9207 | -44.9525 | 2025-08-05 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| cd0282b4-6a12-3499-9657-753953058d7f | -8.9478 | -46.7354 | 2025-08-05 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| dc0f2f2e-d0fb-32c7-8c12-9d28b15c6619 | -7.994 | -43.1534 | 2025-08-05 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |


[Clique aqui para ver as próximas entradas](README5.md)
