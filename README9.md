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
| c4ac30ca-ada8-3a9c-b4cd-90b98786b25d | -7.10046 | -46.51696 | 2026-06-10 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8aa38b44-c02d-3d6f-bdb0-c4b13f2d9f36 | -5.83144 | -43.58944 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5e24933-0711-3f31-ab9a-c6171b225cd9 | -3.60403 | -49.45559 | 2026-06-10 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2397e6-0040-379c-afc1-009d76170411 | -5.30234 | -47.24337 | 2026-06-10 04:49:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7deabf36-f4d4-3fcb-aa85-3085184069cd | -7.14711 | -44.06412 | 2026-06-10 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0150f8ba-9700-3c06-8d27-64142812d048 | -6.39308 | -44.16949 | 2026-06-10 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a53f0a24-8663-3098-848d-2536b2e7aae8 | -4.571 | -48.02438 | 2026-06-10 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4546cf8c-e955-3cc6-85fc-22eef33eb86c | -7.71699 | -44.56585 | 2026-06-10 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e60edfcd-c431-3d16-abe4-d970381aab0b | -6.95667 | -44.54997 | 2026-06-10 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40fc1c06-7ba1-3e75-bc97-e16209c83ca6 | -3.80329 | -49.18298 | 2026-06-10 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f54670e-04f3-366a-82cd-099532b4e65c | -5.73 | -49.09932 | 2026-06-10 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d21c079-e784-3e52-bb31-143058afb005 | -3.81568 | -50.63322 | 2026-06-10 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 266adf67-50b9-3151-97f3-bf97cc76a8a8 | -7.16109 | -44.06609 | 2026-06-10 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cad4c5f1-4ce5-373d-ab14-4156bb58655f | -5.7976 | -45.11299 | 2026-06-10 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32be0db1-4414-3a32-9b8e-3d56e2600f51 | -3.80664 | -49.18351 | 2026-06-10 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da94acf0-ed75-3991-b08e-84811fc40b4f | -7.2697 | -46.81114 | 2026-06-10 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c6fce3-306d-352d-8970-8b9a6db39c5b | -3.8072 | -49.17995 | 2026-06-10 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa5d877a-4f90-3a8b-8dc8-7d2893ac7cd5 | -6.95601 | -44.55458 | 2026-06-10 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8361e1f-19e9-3b38-aaa5-afc7bfe438e9 | -3.5058 | -48.03484 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e25c4355-f1ce-3a79-adf8-edd8dfda2503 | -3.49131 | -48.03639 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f55cd37-5b02-3786-88fa-4f6788a71451 | -7.10513 | -46.51253 | 2026-06-10 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d1425c4-fa47-3b96-a0b1-78d3d5c66a94 | -5.61342 | -37.534 | 2026-06-10 04:49:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 422b6c92-d715-3326-a6b3-b5382c5e5537 | -5.76481 | -46.04235 | 2026-06-10 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82cc9854-ea8b-31a5-b71f-53f00ed58a46 | -5.82672 | -43.58877 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9882a37-2f19-3a1e-a9d0-a15e5ce06a7c | -7.16574 | -44.06678 | 2026-06-10 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38a3fb46-45a1-3fd2-a378-731d3c52ef24 | -7.10119 | -46.51191 | 2026-06-10 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a08f7439-ec4c-3379-b740-c712f265b4bc | -7.71635 | -44.5704 | 2026-06-10 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5df630b4-3324-3924-ab9d-157d380d54b7 | -5.93499 | -43.48221 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c40d9ba-1dec-3847-ba70-217bcdcc5133 | -5.93021 | -43.48164 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9542868a-c66f-3f31-b725-e63520b8eb83 | -4.43132 | -47.73153 | 2026-06-10 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 798db765-6b2a-330e-8904-62f192e71c31 | -6.86275 | -45.04044 | 2026-06-10 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 278179d3-fd21-316c-87df-b1a036d14c6a | -6.90883 | -42.85245 | 2026-06-10 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4bdf8d5c-71aa-329b-b712-fa6713e7c912 | -3.91847 | -47.82109 | 2026-06-10 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0557d0-2a60-34f5-b387-c8541786b523 | -3.49478 | -48.03698 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52f9bdc4-8169-3733-bc3d-e373b03544a8 | -6.86456 | -45.03987 | 2026-06-10 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69754c51-2560-36f0-b38b-a15dc4edd4c0 | -6.00961 | -47.07555 | 2026-06-10 04:49:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2b3b66a-3a65-34e8-90e9-9cfd2dd460a3 | -6.39765 | -44.17013 | 2026-06-10 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8bd48a17-3de9-3138-a595-191cc72fa315 | -7.16505 | -44.07158 | 2026-06-10 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c0218e4-461b-3286-99aa-42268ba6324c | -5.92949 | -43.48672 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30bef064-4fd5-3aeb-b2ee-7601d194359e | -3.76172 | -47.50464 | 2026-06-10 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c43964a4-8fc1-3c19-a1c4-10408b679464 | -3.5052 | -48.03867 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce7dc505-ce42-3da7-a1bd-3dd5d90dc5d8 | -5.80186 | -45.11353 | 2026-06-10 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97142b01-799a-3c32-92b6-2892588c1669 | -3.50639 | -48.03097 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82ddfa12-f14b-389a-bddc-9ff9c18b2a76 | -5.73057 | -49.09563 | 2026-06-10 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f6bd681-6b30-3a3c-8baa-3f0899f4e2e8 | -3.80385 | -49.17942 | 2026-06-10 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d404a2-70eb-3f38-a6aa-a20181dc82c8 | -6.3924 | -44.17416 | 2026-06-10 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 95f9bc37-71f8-37ed-95b6-3cbb5a564e10 | -3.50232 | -48.03427 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 925c1394-e47f-3b94-a502-093e6c16a792 | -9.3234 | -45.4787 | 2026-06-10 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 260c8eea-4c32-3b92-bee8-666b928681cc | -9.3048 | -45.4581 | 2026-06-10 04:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b5050f3c-196e-3393-921c-818616ccf929 | -9.3045 | -45.4809 | 2026-06-10 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 9c4c6731-d671-3c9d-9205-497a646db3f2 | -11.47184 | -47.33818 | 2026-06-10 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c39e73-6be2-35b6-a796-2b4153d3b9be | -11.60149 | -55.34216 | 2026-06-10 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08b82124-6076-3453-a762-d5b408c95344 | -9.30675 | -45.47946 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eb589168-71be-3049-b3a0-69444ae2efb6 | -9.31925 | -45.48547 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2ab1803e-3f74-36d0-89e8-935d3400a4c0 | -14.63201 | -47.97451 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1bb3f7-704b-3906-8343-f5ad9e0ad6d6 | -12.85094 | -44.37421 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8a2810c5-703f-350e-8c09-45f075d5a239 | -13.90108 | -51.82774 | 2026-06-10 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 715ff8b9-6f67-3295-9e5e-a267ea016d7b | -8.60758 | -54.92084 | 2026-06-10 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6db58055-c098-38f7-a235-2bdab8857ea6 | -14.6244 | -47.99997 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f1dfb7a-f35c-3d47-bbd8-0823ff271b12 | -8.99568 | -45.73627 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea3b1d98-eb0b-3a0f-80f6-e70453c36c18 | -13.51444 | -47.81625 | 2026-06-10 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee2da8dd-9188-3c51-88dc-021674600cc9 | -11.64957 | -52.86272 | 2026-06-10 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5ab12eb-298e-3dfc-b63e-c4e0e2662bf2 | -8.29856 | -48.23484 | 2026-06-10 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acfc694b-f5a7-3ba7-9a2f-2d4c07de21d0 | -13.41954 | -43.73597 | 2026-06-10 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9701841-1e3b-3fe5-b58b-cf701e1eab0e | -9.07847 | -50.60006 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 833aae96-c918-3a61-a4f2-21e0b139327e | -8.3022 | -48.23535 | 2026-06-10 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87692979-2f81-3e31-a1a6-93325f7daf12 | -10.5795 | -49.64244 | 2026-06-10 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fa5792d-39d2-3606-8484-bf186a548610 | -9.34233 | -49.14745 | 2026-06-10 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdb8543d-8b83-3d3a-b4f9-c587cebd473b | -10.85054 | -53.73938 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ec1f0dd-626e-3676-a988-1c0a5ca319e6 | -9.12906 | -49.65109 | 2026-06-10 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a2b09aa-aaf9-37ab-859a-5531a658b6e5 | -10.67466 | -51.75078 | 2026-06-10 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24103aef-9eaa-306f-a95d-07f0f622eb20 | -11.80113 | -58.1673 | 2026-06-10 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ef19e7-1c7f-3d13-9837-c651dbd3a1ae | -15.17493 | -43.85284 | 2026-06-10 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 914b4710-98ca-3848-917b-c5e45897ab87 | -10.56868 | -48.02841 | 2026-06-10 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38545492-4b0f-35f3-8192-61514d98296b | -13.41433 | -43.73527 | 2026-06-10 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| caa9aa4b-ac22-32e6-9c7b-f74665eaf03f | -9.74804 | -47.87978 | 2026-06-10 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bce0f26e-e241-3d33-abde-a92c50196ab2 | -9.31508 | -48.96836 | 2026-06-10 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ee5da6d-03d2-37df-9933-2fe3a25f5755 | -9.11281 | -47.96386 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 028c977a-bde4-31fc-882c-f4f05b89783d | -14.63128 | -47.97975 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bf45b6c-f454-358e-abf2-e4ec3c5fbfde | -13.90497 | -51.82467 | 2026-06-10 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38436312-7795-33a9-acad-9467495551d0 | -15.17984 | -43.85686 | 2026-06-10 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad69689d-2a99-3d62-bcdb-54eff7f6f400 | -14.37261 | -45.56263 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 999d813f-0b4d-38a8-a19b-d42e533389b9 | -11.60507 | -55.34278 | 2026-06-10 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64fb47b7-5df6-31c7-8ccb-80509c2aaae9 | -13.26555 | -45.57729 | 2026-06-10 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e3a4eac-339a-32b9-b604-8cbe8c4b07aa | -10.67852 | -51.74781 | 2026-06-10 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba04f3ec-dd18-3eca-8ed9-d9e03e87ed96 | -10.57891 | -49.64633 | 2026-06-10 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a11e2f3e-8568-3d51-be49-9417abd94a12 | -10.51559 | -51.94057 | 2026-06-10 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 987d70dc-58cd-34fe-89d1-18f32f65708c | -14.41569 | -45.58057 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40bfe99e-f390-3d90-8641-49bf7f3f0c3a | -9.34197 | -51.88708 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05441a8c-f352-3117-ad30-a972a0fc3f22 | -9.31052 | -45.48429 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d264507f-54fd-32bd-8c41-7840cdacd97b | -9.30734 | -45.47521 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5da6d617-007b-3703-8a03-d51e343de58c | -8.29494 | -48.23432 | 2026-06-10 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d2678cb-1dcc-34f5-81bd-f759a0aa9166 | -10.85333 | -53.74362 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6a1c8cc-6cf6-35a6-bb3b-1fdb65917049 | -9.31155 | -48.96783 | 2026-06-10 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57049cbd-5c92-36e3-98f2-bdf156f64abd | -12.40442 | -47.49926 | 2026-06-10 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46f86d3-fb1c-38fe-b0d0-d97d1b12297b | -9.74872 | -47.8752 | 2026-06-10 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e494f18a-f9e3-3946-bee3-b6caa5fb146d | -10.85793 | -53.73685 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37088c7-cdfd-32d4-b81b-9c42e3f102b0 | -8.29621 | -48.22588 | 2026-06-10 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6995019f-3acb-368a-968c-f3f3aff91d7a | -8.29557 | -48.23013 | 2026-06-10 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bfa0c75-ee02-3e35-8e7f-c2a131de5b17 | -15.17532 | -43.84948 | 2026-06-10 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README10.md)
