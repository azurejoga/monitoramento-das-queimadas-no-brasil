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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a04b6f34-6a0e-3883-bcb7-7039f0053879 | -2.9832 | -51.022099 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9f5799-b709-3516-a6be-0e05b1e35c3f | -3.4026 | -50.302799 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 939e416d-42fa-3e1d-a145-dfa4fbb678b0 | -3.0352 | -50.3144 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2109df90-53e4-3e75-a978-b96218c49d20 | -3.2903 | -51.5942 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24451b57-a7e7-363a-990b-8ecfc1e2ff13 | -3.0379 | -50.326 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e047991e-c2e2-3079-8e7c-3915ab7cd042 | -3.66 | -54.651501 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5395ac2-b3c3-321f-97a6-a769c8caf53e | -3.5268 | -54.473499 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48cdd11a-2989-3d76-9ba8-517b29bbde1d | -2.1129 | -50.681999 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2244ba6f-bd13-3a82-9dbf-5151c93bb480 | -3.5655 | -53.015701 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f40b4a6a-927b-3074-8b1d-97b6dcf1a77e | -3.8103 | -51.260601 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7c3242b-7ecf-3b83-aa05-0d2ade3f282e | -3.5716 | -52.997398 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc4400dc-57dc-3058-a340-12fdc2dd5aab | -3.7956 | -52.088799 | 2024-11-13 00:50:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17d44b13-0831-380a-a834-78c2c85bb74c | -21.0455 | -47.234501 | 2024-11-13 00:50:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d9822f8a-33cd-3f40-8a34-d73f950f29e3 | -2.4561 | -50.121601 | 2024-11-13 00:50:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ceeda4-11d3-3533-b44e-1ff73b5e03a4 | -3.5015 | -54.6796 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 393651fe-9137-3d35-ba97-859cd7d1317b | -3.2881 | -51.584702 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4f9469-ed9d-32c2-baa0-1e8e0b100c8c | -2.9929 | -51.019798 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd4590a-d311-39ba-880b-bc1c6e776c31 | -16.123301 | -43.532001 | 2024-11-13 00:50:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a79ebea4-0d29-360e-9928-ba1493938af2 | -2.8664 | -54.197899 | 2024-11-13 00:50:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a482264-72d1-341e-810f-174a2572bec0 | -3.0601 | -50.333099 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e99558ce-c709-3e59-af49-03451f82c972 | -3.517 | -54.4757 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f452a0e6-ebc2-30bc-80c7-11d2422f6fd9 | -4.3277 | -50.431301 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e530365-310a-37b2-a584-935d61045fe8 | -2.8909 | -54.169399 | 2024-11-13 00:50:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e78f59a-04b4-3313-8949-ecd90105d8e7 | -3.0574 | -50.321499 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23cb8d44-fea2-3e04-8e26-d3d2c9c0d151 | -3.4962 | -50.8381 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64f50e6-b1b8-3493-bf4f-bc107c3e2f21 | -2.8892 | -54.162102 | 2024-11-13 00:50:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce909d5-fdf5-3c3a-a12d-ca3ff620b56d | -4.1098 | -51.0872 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d04ff8-a371-3d07-8351-189b6136532d | -21.2054 | -47.124599 | 2024-11-13 00:50:00 | METOP-B | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3fc69816-9284-3064-add8-08521a9101b0 | -2.9467 | -54.279301 | 2024-11-13 00:50:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5796a3-c2cb-3e37-bcd8-409447e4c569 | -3.5433 | -51.485901 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f39c6a3-8db5-3f24-8fd1-13bb2b4d45a5 | -20.985201 | -47.4119 | 2024-11-13 00:50:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3866a933-c58f-3eb8-8168-6d633e700293 | -3.6641 | -50.145 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e45568-39bb-3eda-91cd-2b86c8cfdb40 | -3.8048 | -52.352299 | 2024-11-13 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2692dafb-2dcd-3515-9534-cd4967daf657 | -2.9881 | -51.042999 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f95e1b40-8b40-35d0-85f8-493f4731a461 | -3.4103 | -51.044601 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f566b58-5215-3ac8-b397-09f2c466283c | -21.202801 | -47.1143 | 2024-11-13 00:50:00 | METOP-B | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a5edfb4e-9ca9-3e51-989a-3622deb3b2f0 | -4.4079 | -49.631802 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6d9c0af-924b-3861-b2c5-f33d6ae552ac | -3.0477 | -50.3237 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71cada90-6769-3a57-befb-b0704d0f6b0a | -2.9781 | -53.964199 | 2024-11-13 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27821b5a-4a4f-38a6-bbce-1396937db375 | -3.4923 | -50.2458 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebab0c00-f655-38c9-aa29-d4d0169ae221 | -3.6696 | -50.168301 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd2609d-82a7-396a-a7e4-5a878e0c1fd6 | -4.3349 | -50.418098 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c55b154-846f-3250-99fd-e9270ce78823 | -10.7328 | -49.5266 | 2024-11-13 00:50:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c9e26e9-7ee5-3701-b6a4-1dcbb78c1462 | -3.0406 | -50.337502 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc85487-47f4-3d84-8508-0f3a8db8b65b | -2.9856 | -51.032501 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b086d9e0-be6d-3f0c-8b46-d39636cf84a7 | -3.3991 | -50.375801 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89eed12c-4345-3265-bc16-f22c6f2b08f7 | -5.3434 | -43.5172 | 2024-11-13 00:50:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00a224f3-65e3-3464-91f7-53e7bc0f4e33 | -3.8466 | -51.9077 | 2024-11-13 00:50:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d88bfee-6142-3c67-a888-9873329e45df | -2.775 | -50.300301 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb27e512-648f-3461-9bbf-ec729f2f776b | -2.7091 | -45.279499 | 2024-11-13 00:50:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3e39592-76ac-3df9-b6ae-a2e5f64436e5 | -20.992599 | -47.399399 | 2024-11-13 00:50:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2f23567b-132e-377a-bfe0-63fc58b96412 | -3.0672 | -50.319302 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19809e15-ca04-34ba-8e7b-1f7a4d5f8876 | -3.4896 | -50.234299 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656e26e2-66c7-3ffa-beab-545d1c3ba5d6 | -3.5636 | -53.007702 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74419e2e-2c04-3170-90e0-a55ad5ef6c10 | -3.1518 | -53.234299 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69ee675e-1594-3f32-bc71-98b02d532bb0 | -3.7977 | -52.097599 | 2024-11-13 00:50:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab8afcbe-8969-3cf0-a3d0-624aedeedbbb | -3.6669 | -50.156601 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab95f18-a380-3a52-ade6-da8a79231a59 | -4.1024 | -51.0994 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487cf303-db32-3c14-b778-90be12e89a3e | -3.045 | -50.312099 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa70eb23-d4fd-3384-a3c8-2e2c7de063f2 | -3.2474 | -50.386799 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42cc1bf0-dac6-36bc-93c6-6d2fd2149572 | -4.1458 | -48.3909 | 2024-11-13 00:50:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7615d4c3-67cd-3e4c-8f8a-a2be50d58769 | -3.4053 | -50.314301 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33a686b8-9db7-3559-8535-9f3385621d3b | -2.9833 | -51.334599 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c48e54-9c2e-369e-b1cc-d7c475466812 | -2.9953 | -51.0303 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f29ed001-2f1b-3dd8-9403-74f954bf0367 | -3.0699 | -50.330799 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f33325d7-3acc-35dd-a78d-c361841d286c | -2.9815 | -53.979 | 2024-11-13 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be3079d-9d17-3608-806c-26bfc0d25efc | -3.5284 | -54.480598 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a355b90c-4191-3eec-90bc-a46eb6761c66 | -3.8564 | -51.905499 | 2024-11-13 00:50:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0eaf692-d59b-34cb-a9ed-086175f24396 | -3.7524 | -47.468601 | 2024-11-13 00:50:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d41ddb21-108d-3096-a33e-2ba2aca03848 | -4.3543 | -44.0867 | 2024-11-13 00:50:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fdc5de6-af68-3b92-b897-b0dea4d8bf7c | -3.1499 | -50.5868 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eb8159a-3341-3247-85a9-87c728ae3bdc | -21.195601 | -47.1273 | 2024-11-13 00:50:00 | METOP-B | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e50e6c4f-b282-38f2-90f2-f4ae39c43a0d | -3.5186 | -54.4828 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcdd91f-0f21-3697-a87e-5958aa1cb738 | -3.1473 | -50.575699 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a86a5d3-3adf-3616-8ef9-dd5a6da967a8 | -3.7567 | -47.486301 | 2024-11-13 00:50:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a45db2-efcd-3b1d-8952-6333eaecb700 | -3.3964 | -50.364399 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81cdf79-9ac4-3846-8d63-8b6e421ea86c | -3.5687 | -54.612801 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa4f2c7-b77a-3137-81aa-0520aab36bb9 | -2.4507 | -48.817799 | 2024-11-13 00:50:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601769ea-db28-3035-b004-7d2dc7930b80 | -3.7664 | -47.484001 | 2024-11-13 00:50:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c73c28a0-9f75-33d0-823f-ac5ec352e326 | -2.6941 | -49.333599 | 2024-11-13 00:50:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d77d992-179a-3b10-aceb-4fe504da41e4 | -3.6616 | -54.658501 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 338a8171-6a26-354b-a448-7e8b1f2c5230 | -3.5618 | -52.999599 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6823d7ec-fa27-3de5-b624-b7f38a9046fb | -3.1536 | -53.242199 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18639627-9cb0-345d-9047-6809257d3ec5 | -2.6972 | -49.347301 | 2024-11-13 00:50:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eec6aaa-156d-3acb-be04-f56659291c8f | -3.6584 | -54.644501 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c76016-c6ed-30ee-9194-2b34c4e18017 | -3.249 | -54.520802 | 2024-11-13 00:50:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b75d6dc-1e10-3bd5-a190-8de1ac8fc110 | -4.0765 | -49.141102 | 2024-11-13 00:50:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd67cb0c-7053-34a8-8156-82e968114e70 | -2.8681 | -54.2052 | 2024-11-13 00:50:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04c99bc-4387-3be1-b046-8c49f7024655 | -2.6844 | -49.335899 | 2024-11-13 00:50:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bedd569f-ef0d-3df0-b139-6fe7cd54d2b4 | -2.7187 | -45.277199 | 2024-11-13 00:50:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c502293a-0da5-38ac-b8c9-0afe42cf2e72 | -3.808 | -51.250702 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea7de15-550a-3540-920c-30c2c121aa1a | -3.2506 | -54.527901 | 2024-11-13 00:50:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d3bad8-bcc0-35d4-8cca-cb0d6b95cd7d | -20.995001 | -47.409302 | 2024-11-13 00:50:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8706297e-2885-3755-9152-70e962232295 | -3.7312 | -54.4203 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00079fca-b051-38e0-bb89-5b1b6f676af2 | -10.7304 | -49.516399 | 2024-11-13 00:50:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 272e1516-b008-3d6b-9448-c468212b38b7 | -3.7629 | -54.6507 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082062e9-263f-3fcb-af5a-994316aac288 | -5.3338 | -43.5196 | 2024-11-13 00:50:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfd8e12-1735-3489-a63c-1b8bab167ff6 | -4.1121 | -51.097198 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c02136-5681-3e5a-b0ee-d47562c78880 | -2.7722 | -50.288601 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af2517d1-1865-3714-aa91-514e0f6434e5 | -3.9816 | -56.0746 | 2024-11-13 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
