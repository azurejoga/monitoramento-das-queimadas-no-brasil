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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07e76d90-fcd1-3a28-86a4-967a2ed40124 | -10.6514 | -44.488201 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab8adc6-9fe2-39b8-a1a3-40e5847cad38 | -3.3296 | -53.531399 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca9bf20f-4d70-3c9f-9a8b-b544e2d075a3 | -3.66 | -50.709999 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7900b2-b854-3f2a-8e71-f70c382e0421 | -4.5465 | -45.713299 | 2024-12-01 00:34:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab854543-118c-3e19-a40d-b621cff07d6f | -2.5872 | -53.970699 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 760620f0-eaf3-37c5-ab97-9da591e6a33f | -2.4447 | -53.612701 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edcf3c1d-458a-3105-929e-bb28c642c965 | -2.9321 | -51.4501 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47987745-7574-3e50-b20c-e17d97a13245 | -3.0374 | -50.235901 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7991c1-5bef-362a-9728-3877fa7f2b14 | -3.1067 | -53.270302 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbfa4ec-9b3e-38d3-b679-a8d584b42f0f | -2.66 | -51.884399 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ac76a4-801c-3c45-829a-0f98c8ab3ea3 | -3.0505 | -51.064098 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edf0eb1a-f230-3797-b3ad-cbb9c1cbe579 | -2.1117 | -50.334499 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f38d3b55-1c8b-361f-b5dc-424a4135f0c4 | -3.5018 | -53.842201 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54cf0d59-29ea-392e-9046-9828b3c57d69 | -3.2987 | -50.025799 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa32c4e-c305-3df9-bad1-f7039abae3fa | -3.4971 | -52.129601 | 2024-12-01 00:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5e10f7-6517-3330-869f-cd308e64d87e | -8.9332 | -44.254101 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b792387b-d09d-3831-b434-e70926dd112f | -3.2709 | -53.6353 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c0d0b3-33f7-3444-bcab-47e9d21bdf07 | -2.9223 | -51.452202 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09f7910-7bae-348d-a0ee-28e80f72db2d | -6.9264 | -43.5425 | 2024-12-01 00:34:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ba1debc-11cc-362d-a795-f9a76d86a75e | -4.0351 | -48.3274 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70dde026-c46b-3c4a-81b4-cc5590dece31 | -4.0367 | -48.334202 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c09861-0f4d-3f8c-80ad-bdafd8bd6052 | -3.332 | -53.542198 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 765cff70-8262-3129-a695-0e0922aa8526 | -4.5447 | -45.7057 | 2024-12-01 00:34:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e35dfb69-cd86-3e98-8bb4-3eead50f4835 | -2.121 | -46.554501 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb4ffede-f104-3cbb-9878-ff147ae70a03 | -2.9204 | -51.444099 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4a52d1-cd2b-3daa-aaf6-5c543bb09065 | -2.4632 | -46.562599 | 2024-12-01 00:34:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0059cbfe-780c-3b79-9536-fc2c2a624ee6 | -11.6947 | -44.6203 | 2024-12-01 00:34:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 874e9466-ddf0-316a-b8a1-f2dd2073edd3 | -3.5232 | -50.4697 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9495f004-ce15-3401-b45d-083cd72e336b | -3.8883 | -45.014198 | 2024-12-01 00:34:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd4e369d-9c26-3d2d-87aa-fb3cfc870fd6 | -2.6434 | -49.908401 | 2024-12-01 00:34:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c18388-b558-3458-82a1-096eff9c39c8 | -2.5759 | -51.876202 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3abc04c-22de-3f09-9494-e430fc4eb869 | -3.2562 | -53.6157 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d02db7d-738e-38d8-a632-a1116394239a | -3.7554 | -52.272598 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e13ddf-0c70-35d5-8b85-e9cbff37c95c | -2.4471 | -53.623299 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf63ceb-9c7a-3705-8e68-c6681de2614a | -6.9122 | -43.5266 | 2024-12-01 00:34:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91a9d80c-69d4-34ee-8a59-b87f72a09e23 | -4.5412 | -45.690498 | 2024-12-01 00:34:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ecf51f57-a7c7-3ad9-aac8-40499051f559 | -10.6647 | -44.500999 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1ba7da9-e7b8-3487-b027-3be5e808c706 | -3.7375 | -51.827499 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5555e00-a780-3ee3-bf8d-0292e03f673a | -2.6218 | -54.215302 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d90b1e-5c45-3c35-b8b4-00070b3012f5 | -3.4646 | -50.256699 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b395087-b5dd-3969-a242-7daa62092060 | -4.2609 | -47.602699 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80481562-85b7-3399-943b-405d2353f0c3 | -3.2415 | -53.641701 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad9f6b27-6a80-30dd-adf1-015b06884bb6 | -3.3184 | -50.0214 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6f84f7-b195-3f05-917b-c2f2324883bb | -8.1265 | -44.468899 | 2024-12-01 00:34:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc7a392-2385-3fd8-bf0b-b6f8ca2f0c81 | -3.1313 | -54.521198 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89873749-4fcc-33dd-a1c1-929272720dff | -3.1123 | -53.797199 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 779291b2-bb2b-3a3c-acfe-35e2f3c01bf2 | -4.9002 | -41.3256 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f76306bb-2362-351f-af7c-6deb27f764b2 | -3.3012 | -53.862099 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8a9f7d1-b496-32c5-9805-406919bea8b2 | -3.2071 | -54.173801 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b02083e7-2ac4-3315-b3f7-e8657f56bd4b | -2.833 | -49.8811 | 2024-12-01 00:34:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e8236f-b942-36ce-ada0-afe84e558db9 | -3.1608 | -53.2369 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2677de6b-faf3-3857-b250-afc9a1891c0b | -3.458 | -53.875599 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2484393-4cc1-3224-8691-c4411b16e29f | -3.4247 | -49.990299 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c470a55d-c5f3-375e-b2d3-172aa11077d4 | -3.1807 | -54.3302 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756a79d6-1fe0-30c8-80cb-3eddc418db8f | -2.8428 | -49.878899 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2b37aa-857e-3dba-9282-efb40b4fb8a5 | -6.2956 | -43.8428 | 2024-12-01 00:34:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5094ba-204b-378c-a7a8-e1d2ab372f2d | -7.3819 | -45.8339 | 2024-12-01 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05d54ff0-d237-3838-936a-2376ff8fa429 | -3.3631 | -51.536098 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a60669-277b-35fc-a221-19bc77c42f5b | -1.2667 | -47.861801 | 2024-12-01 00:34:00 | METOP-C | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4eba026-cb7c-39cb-8c83-da168c4a5e19 | -2.947 | -45.711498 | 2024-12-01 00:34:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee438c9b-6f50-387c-b445-dd5eb773d520 | -2.6399 | -46.122101 | 2024-12-01 00:34:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 409d8b40-b3d9-3522-8ae8-4c805c38d996 | -3.635 | -54.438 | 2024-12-01 00:34:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bea0af-887d-3633-ad24-b0ca1714e5a5 | -3.3201 | -50.028702 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbebc922-f2cb-3ce5-a8c9-87c38ae39f7e | -1.5611 | -46.765598 | 2024-12-01 00:34:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a33b6e-3899-34f5-9203-b23842c5bfaf | -2.4747 | -46.567699 | 2024-12-01 00:34:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2049ae3d-a58c-3321-84fd-45c7087ed262 | -3.4152 | -50.175301 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6eacb1-8911-365f-ba07-34d8dea71b1b | -2.8346 | -49.888199 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d17ff243-fb1e-3f21-9c45-73207b2fe159 | -3.5194 | -51.1348 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a98dd9-de05-3a0f-920a-4fec143b14ec | -3.4993 | -53.830898 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4428e3e-6a7a-352d-ba47-07821fb3f25c | -3.7415 | -52.256401 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 223b75c1-22c6-3526-bf3e-daf7f2b43410 | -3.1243 | -54.535801 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02177412-457d-320e-9808-96a1b1019c5f | -3.5412 | -50.185799 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73425981-3046-3f9f-9839-dcc34bc009ab | -1.9451 | -45.838699 | 2024-12-01 00:34:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16213648-c186-36c2-a765-8ab8182f1551 | -3.0071 | -51.781399 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de7e63e4-535f-386e-a80c-18cf6deb384f | -2.9011 | -51.585701 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8db87b9-9f72-3850-a885-32351cd23dc1 | -1.7234 | -45.771301 | 2024-12-01 00:34:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f366672-83f8-3b41-91e3-f047bf2502ca | -4.1709 | -48.605598 | 2024-12-01 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 050c71b7-999a-3916-9647-50309a3a0eac | -2.3178 | -50.6502 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319044da-25a9-33e7-830e-2d58772294a5 | -2.6361 | -54.187801 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64ec9aa-9c07-3041-9c68-6c12f445a773 | -2.6244 | -54.226898 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545d4161-a800-3c58-a684-ab51426b2426 | -3.2697 | -50.215099 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3645852e-fe8c-3a72-a310-2d91fbe4c7a0 | -1.2683 | -47.868698 | 2024-12-01 00:34:00 | METOP-C | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0a56ca-ca05-385a-9ab3-a7bd9364d9d0 | -3.2628 | -50.048901 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c36613-bdf6-383f-ba83-045ac8ecde3f | -3.0109 | -51.798302 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9889b7b-7e61-3a73-934d-b93ea6ba4a60 | -2.7277 | -49.375 | 2024-12-01 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25a4dd7c-fe30-3edc-9768-d337f812d78b | -6.7567 | -46.521999 | 2024-12-01 00:34:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45eb7e44-1981-3924-8694-29d4c36df857 | -2.1456 | -50.618401 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d24250-ea4d-33d2-a3ac-d8a8bf3980b2 | -6.7129 | -47.273701 | 2024-12-01 00:34:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa642340-7f32-3938-a98b-1d53841e6e70 | -2.9694 | -48.043201 | 2024-12-01 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bae0dec1-a1fb-3ab1-8901-688a151f7c41 | -1.2782 | -47.866501 | 2024-12-01 00:34:00 | METOP-C | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3d39f46-52d8-3b6b-b474-64315dc8a456 | -3.0688 | -50.328899 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11a8814f-b491-3017-9255-8f64d5205e9c | -6.7145 | -47.280499 | 2024-12-01 00:34:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a31ea355-068e-3a49-ad59-b6be32822bae | -5.188 | -43.958599 | 2024-12-01 00:34:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00e68f0f-9773-3055-83e0-0b06c922f4f9 | -3.3855 | -49.8633 | 2024-12-01 00:34:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81236c1b-799c-3d5b-b3f5-47db327c76d1 | -2.2012 | -48.3368 | 2024-12-01 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5a9b25-170d-3c41-bbcf-dbf84e4d0fe1 | -1.7215 | -45.763302 | 2024-12-01 00:34:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22b18ed7-e70c-3358-9b3f-89727a0bea12 | -4.1772 | -48.632999 | 2024-12-01 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b5f83a-dce9-3a85-8e95-149b8f896489 | -2.5116 | -51.819901 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbe1ec13-9898-3ee8-9614-bcf15ad8412c | -3.2629 | -50.094501 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7716c2f-252c-31d9-a4cc-a412c90cb6f8 | -3.3221 | -50.218899 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
