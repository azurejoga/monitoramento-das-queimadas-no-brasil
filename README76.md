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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27bfb5f6-7017-38d5-8ff5-e13fae0bacff | -14.4264 | -56.46056 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41eff92e-0bcf-3ecf-8e79-2f4c8df08517 | -14.22988 | -58.62242 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c906989-b954-3b0f-b303-5c18b8b14d47 | -15.07881 | -48.54404 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0121dd16-f42a-3a81-b4db-8c67090cefd7 | -12.0714 | -63.15134 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be8f8c9c-0baf-3812-9267-e6116332f90f | -12.22219 | -64.23717 | 2025-08-25 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4202db60-b89f-3c3e-87ec-4b9a44d7f04f | -15.11612 | -48.68365 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e646c77-0540-3d9f-b1e8-743b4cdca302 | -14.43929 | -56.46632 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3e53785-51c0-3f39-8f0c-5aee19e0fb2a | -15.642 | -52.7232 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f53f5b-1250-3d8a-a55a-305296e2680f | -14.27281 | -58.61117 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da6e5485-f318-3835-a082-9cb65e600e46 | -15.0393 | -48.52496 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a3a6ffc-aa48-3bb8-b759-a17dc28fb37c | -14.25439 | -58.61917 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58618f69-06ed-344d-acd2-d4fb4b3533f1 | -13.45266 | -46.88324 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c250d5d-96b7-3185-b99d-389df9c6edc4 | -15.14215 | -59.59082 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71940f10-5f4c-3a8d-a778-c3af587cfac5 | -14.20869 | -58.62627 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb5f4430-909e-34ff-b03f-2a4211391cbd | -15.08403 | -48.68306 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c84b04-d9bb-39b4-96ac-6f2277ea9bfd | -14.29388 | -60.3677 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79644261-107c-3f8e-9b36-18dc01fe7e37 | -15.13813 | -59.59399 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1c8d955-0668-344c-b413-435379aaa3dd | -13.01012 | -56.89079 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceff8a5e-97db-3b15-ae3f-0ba98986f6c7 | -12.487 | -53.82811 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53418260-87d4-3047-bb8e-55dbdf320c18 | -15.08365 | -48.68629 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d314c0-6518-3c6b-9e4d-33310f7c6c41 | -14.37304 | -51.93803 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0921077d-5303-3949-92ec-c3f5f10a0256 | -13.43934 | -46.89669 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c925433-8ddf-3f40-8d7b-594705adbd13 | -15.62824 | -52.70214 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02d153d8-e7cb-30fc-b728-58086884cff3 | -19.93658 | -47.49725 | 2025-08-25 05:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b18acce-63a3-3c71-83c1-9d5e85fdf94e | -19.93695 | -47.49313 | 2025-08-25 05:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f8ad3f1-9b42-3891-9594-b692895be116 | -20.38171 | -46.75819 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ceced136-f404-392d-838f-e518f6a356d1 | -20.37764 | -46.75956 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c2797482-c132-3a74-8e7f-b63062a0067b | -23.32825 | -47.84843 | 2025-08-25 05:08:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c1a7a9b5-507a-3681-8ca1-5a7cf8b28344 | -20.35852 | -46.7308 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c1726c-04a1-3b14-b123-52b1cdbdb07c | -20.38437 | -46.72848 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2db931f8-814d-3586-87c2-00dd23db39a5 | -23.32866 | -47.84339 | 2025-08-25 05:08:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f09bed19-8f86-3cf7-b4d2-f131d8d7b59f | -20.45142 | -47.41534 | 2025-08-25 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecd5cf47-e9d1-3b55-95f8-85344961db43 | -20.29325 | -47.18285 | 2025-08-25 05:08:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6044525-47a5-3052-897e-e61ef46a83c2 | -20.107 | -47.25875 | 2025-08-25 05:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1317cec-3e93-32f4-a699-995d49e73db1 | -19.92014 | -44.63176 | 2025-08-25 05:08:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f1ccd611-fd1d-3b78-a656-d5aa33030fb0 | -20.04602 | -44.47904 | 2025-08-25 05:08:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bda9eb7e-5d71-36f0-81b4-d99f09ac9d9f | -20.35906 | -46.72473 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 189cdf3b-bacf-3b8f-afc9-4d6927c7172b | -23.32865 | -47.84594 | 2025-08-25 05:08:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6e84ada4-a1bc-34d3-91c5-828e2bce106d | -19.73231 | -46.4692 | 2025-08-25 05:08:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d1b4590-4a24-337e-a4e1-0589421f886b | -19.73472 | -49.01907 | 2025-08-25 05:08:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61d4d825-790a-3941-96f8-67cdff572b2c | -20.37883 | -46.74517 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a49de231-2181-31ab-9b80-b549287b0999 | -20.39259 | -46.73368 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a47fd31-dfe9-34dc-94d0-076be0aab896 | -20.3655 | -46.72436 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c0a259a-5116-35c5-9fd5-86297213c671 | -20.37806 | -46.75447 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0f5d4505-4e18-3821-a548-9dd56dec3fb2 | -19.91308 | -44.6303 | 2025-08-25 05:08:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cfcc87f8-f5f2-35c6-b212-436e68140b32 | -20.38216 | -46.75317 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8861940e-8393-3b60-994e-528a12a32aa1 | -20.27309 | -46.65254 | 2025-08-25 05:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81559ee7-0362-3bf6-b35c-601515ca6780 | -20.37157 | -46.75564 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 176c5799-9642-3346-bed5-3eccfbf0e6f0 | -20.37569 | -46.75391 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d47d4d20-64a4-31e7-8810-c18ba4fe0517 | -19.72595 | -46.46804 | 2025-08-25 05:08:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bdd81d8-c202-3e88-b29d-995a5b03de61 | -19.91594 | -44.63705 | 2025-08-25 05:08:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e4a302b-45d5-3080-b99e-63165e111901 | -20.45233 | -47.41328 | 2025-08-25 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ae3507b-030b-300d-a38d-d324161154a9 | -20.29942 | -47.18366 | 2025-08-25 05:08:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f949782d-4d35-315b-901a-00a1c4097536 | -20.36605 | -46.71817 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fec876f7-af19-3368-b29c-2159e8b9075f | -20.3761 | -46.74931 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c37a4dd-35f6-3a28-9902-c246e915a140 | -20.38654 | -46.72946 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc475495-f672-302d-9dd2-3cc1925a018d | -20.38391 | -46.73366 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dafc5bd-b63f-35a7-902c-bd1fb0d0ab56 | -20.61793 | -45.02686 | 2025-08-25 05:08:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9c5f8244-22c1-3f71-9fab-0f452659da3d | -19.7351 | -49.01543 | 2025-08-25 05:08:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f7419aa-57fd-3103-8bc3-6b5ad8481036 | -20.61622 | -45.02715 | 2025-08-25 05:08:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 48602b13-2fd3-3e91-a7e5-bd0567bb787f | -20.37845 | -46.7498 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| afa22cf1-af46-3658-853c-ed5cd26a8aa5 | -19.94616 | -50.44429 | 2025-08-25 05:08:00 | NOAA-20 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| cf8273f5-2d32-39cf-a35e-685fc68068b9 | -20.37922 | -46.74053 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 810529b3-4c69-3480-a761-4451f8456a24 | -19.91645 | -44.62999 | 2025-08-25 05:08:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 253d141b-7d5f-332c-ae8c-551afdee4125 | -20.87171 | -55.00578 | 2025-08-25 05:08:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b67d7d83-951e-3c60-a531-613f99b79987 | -20.37963 | -46.73551 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9308e5e-f3bc-364b-9d1e-06463a368221 | -20.37481 | -46.76381 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 39f752b2-d979-3031-a396-3a89fd1827b2 | -20.35963 | -46.71817 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 246fbf58-60fb-342a-be23-763a3f3f1cf2 | -20.39039 | -46.73283 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7c1abcb-91db-3c03-90ff-039e1bbafe8b | -20.29282 | -47.18768 | 2025-08-25 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b4c3fe-5a39-3aab-8405-1ba8a3e7de36 | -20.38009 | -46.72994 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f131fb0-034b-3003-8353-9a52249e25b6 | -20.38613 | -46.73442 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aea48761-3d33-3989-ac6c-a14d8fe7b39f | -20.37526 | -46.75882 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 782eb00d-cb03-3a79-be7f-44fd31f70602 | -20.3826 | -46.74833 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97a9087a-f743-3b4d-88c6-6b757df2d57a | -20.27265 | -46.65752 | 2025-08-25 05:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b9ffd35-c466-3093-8a39-24631eb705dc | -20.38302 | -46.74352 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59aaebb6-2a53-3bda-a0d9-d54c121f579e | -20.37039 | -46.76993 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27252494-4a6a-35d1-a83b-851fd20fee1b | -20.45752 | -47.41599 | 2025-08-25 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45a169c3-5d7e-324d-aa3c-9800cdb72981 | -19.93731 | -47.4892 | 2025-08-25 05:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1d5b570-59d7-330b-acf4-dc40a98c086b | -20.37694 | -46.73988 | 2025-08-25 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef0ea1df-a9d2-3815-9459-ac214536109b | -9.0601 | -65.7157 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b53cdfc4-eeda-3ef7-9d26-9910b0881efc | -8.9689 | -65.4198 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8db9a2f3-5f31-3ab9-8495-14b017a40b96 | -7.9078 | -63.0542 | 2025-08-25 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e415e85f-7cdc-3d0a-8314-ac502d579505 | -8.9875 | -65.4006 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| fdd9760d-371a-359d-8fd9-d6a710110a54 | -6.8229 | -58.956 | 2025-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 00516d71-3ceb-36b7-a0f6-c3d81d598009 | -8.8919 | -62.4487 | 2025-08-25 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 101d8c0a-5237-34a7-93a3-88e8aaec1d7c | -14.1076 | -53.9847 | 2025-08-25 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 56fd2537-cd3a-310f-8464-fc3c0ab0e028 | -9.06 | -65.7344 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 0008827f-99cd-34f4-8d8e-93cb2a64ba0d | -9.0061 | -65.3813 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 81f18f8f-d106-3589-8dee-49114b456dac | -7.9077 | -63.073 | 2025-08-25 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f353c4bd-b873-35a2-acc9-da6bfc820775 | -6.782 | -59.6519 | 2025-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6e0a18b7-2421-36ac-8ac9-e4272dc0fcd0 | -8.8918 | -62.4677 | 2025-08-25 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 412b77cf-bd86-335d-b740-37e7948202a0 | -9.006 | -65.4 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 163b0b22-3821-3184-83c5-a4acf805e177 | -8.0681 | -49.6951 | 2025-08-25 05:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| bd153486-7fe3-342c-b7a1-bb847cae3cdc | -8.0683 | -49.6738 | 2025-08-25 05:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 22b6ff87-f5fe-3e26-8d3f-222db052a68c | -8.8548 | -62.4503 | 2025-08-25 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a9aceea1-3b38-3c15-94e9-318c60d955aa | -8.9874 | -65.4192 | 2025-08-25 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9c240707-90a7-3cab-825a-d92a5785fba0 | -10.7209 | -47.1142 | 2025-08-25 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2c3542ca-fdbb-3f26-8471-9fdce6853ee1 | -12.7459 | -48.1375 | 2025-08-25 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5b123427-1dce-321f-9755-2590f72a1228 | -6.8413 | -58.9552 | 2025-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README77.md)
