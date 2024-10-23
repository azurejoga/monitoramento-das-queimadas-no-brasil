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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03eda933-6789-3e5f-a7af-21ca474cc5b8 | -6.19305 | -43.43349 | 2024-10-23 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91e1bc41-5f61-3bbf-9d15-c5fa81d21fdd | -5.6183 | -43.28722 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b39bc0b4-9a53-3c18-a301-17ecd9be645f | -5.61762 | -43.29107 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc78a315-f586-3175-aefd-bd729e16e1f3 | -6.6388 | -43.44976 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5226d67-59d8-3233-ae75-cdfa6bff7534 | -6.63813 | -43.45345 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d54753cf-5b4d-3705-9e0d-ffdbe6e8ba88 | -4.12502 | -43.00763 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b327bf9c-58e1-338f-bfe5-8615f93ec1c1 | -4.12436 | -43.01156 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6c8a7fa-3d02-34bf-b97c-ab4a3ea0668e | -4.12041 | -43.00921 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dfd8537-f6b1-33a8-802e-0c9f98f5dc76 | -4.11869 | -43.01049 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66640986-12e2-32ed-89ad-692d5b8f36aa | -4.05614 | -43.98561 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0f95a35-128a-3c8a-ba1e-be460056c197 | -5.51151 | -43.69508 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ac9b477-0fed-30c0-9426-81782a476d3f | -5.51085 | -43.69257 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70703a81-1909-3133-84a5-f23d48ea1356 | -5.51081 | -43.69918 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d31bf8ca-5a21-3b8b-b2a8-263f5dd960b6 | -5.51011 | -43.69671 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2e09386-4689-3a02-a01a-a76a55839d08 | -5.5101 | -43.70328 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1df87768-f93c-372f-9f3d-6abc9e86e591 | -5.50937 | -43.70081 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 200b2e3b-0c48-3735-bb96-ea8808cdc19c | -5.50864 | -43.70492 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d79e228e-ded9-3925-bb19-411343d86016 | -7.47773 | -34.84322 | 2024-10-23 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 87271385-218f-3bf9-ab2c-6b38fbdd5847 | -5.16019 | -43.962 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f4499c-b549-342c-aa46-6631683a41a4 | -5.1594 | -43.96647 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7276f49b-83e1-3ebb-88b9-0d9fc32245cb | -5.15501 | -43.95669 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b992bf6d-7866-3b22-901a-4cc0040c9655 | -5.15423 | -43.96111 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20085fd4-278f-36c2-8c70-0d74af88143f | -5.15344 | -43.96555 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a666b8d-55cb-34bd-a40d-1fe8f77cc469 | -5.15265 | -43.96998 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 901aef69-4fbb-3525-a82b-2b1c4d25bcd4 | -5.15133 | -43.96033 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1692e810-3507-3104-b9fc-d5836649c0d8 | -5.15058 | -43.96476 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40ae92c5-0285-39f2-aa94-d4ba1ebc41d4 | -5.07284 | -42.56731 | 2024-10-23 03:34:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dfa951dc-a076-3f8d-9b1d-8d5b31ad9586 | -3.30805 | -43.51586 | 2024-10-23 03:34:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a24dd4-7ae6-351c-9c94-4b5f8481fb58 | -5.14983 | -43.96916 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6beef259-d00a-3cd2-bb35-453b14d6c496 | -6.23411 | -35.36686 | 2024-10-23 03:34:00 | NPP-375D | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 511a1721-ede0-377a-a77b-588ab55a24ae | -6.30756 | -35.21066 | 2024-10-23 03:34:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e07e1ab-1759-3123-a271-453de5e8e64f | -6.30414 | -35.21012 | 2024-10-23 03:34:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 250c9967-b60e-3278-a648-50774b2a84df | -6.30013 | -35.21329 | 2024-10-23 03:34:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fece15f5-82c6-3e09-80bd-0a38151a05b0 | -6.29671 | -35.21276 | 2024-10-23 03:34:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 889e2464-ea20-3c0a-9349-6a3dd216743f | -6.17225 | -35.29198 | 2024-10-23 03:34:00 | NPP-375D | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 287f8e4e-38d8-30e6-bc4d-bf4d14e2c338 | -5.8986 | -35.43346 | 2024-10-23 03:34:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20d814ff-4d21-3d97-82eb-f8c131e8784f | -6.50627 | -35.25687 | 2024-10-23 03:34:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 10aea83e-8ef8-3853-b24d-7fc332ba3d28 | -6.74331 | -34.97718 | 2024-10-23 03:34:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3ca9044-126e-34bd-aefd-0d66c9fc5ef5 | -6.74274 | -34.9808 | 2024-10-23 03:34:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b8a38f3a-24ee-3e9a-9b63-af9c71dcbf87 | -4.91966 | -41.97189 | 2024-10-23 03:34:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8dc3cf8e-d015-3cd4-a52f-e8a0d7e71c18 | -4.91912 | -41.97507 | 2024-10-23 03:34:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4d68e82-c989-3aa1-a5ad-6d535868d80d | -4.72392 | -42.66015 | 2024-10-23 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e8ab1dfe-82e9-3bb2-976b-8740b9656cf6 | -4.72389 | -42.65982 | 2024-10-23 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ddab869-297d-3bf2-9015-a614852cc420 | -4.72333 | -42.66372 | 2024-10-23 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b4fb8684-afa9-335b-bb60-941e48ab8e01 | -4.72327 | -42.66338 | 2024-10-23 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 905f1dd4-14f2-3d2d-9a7b-005d28ed2032 | -4.71843 | -42.65916 | 2024-10-23 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 113d7080-b971-35d2-ae0b-79432e67e5b7 | -5.07886 | -42.56492 | 2024-10-23 03:34:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f51f322-8d7c-30a8-8398-da461fb97eed | -7.78375 | -37.92017 | 2024-10-23 03:34:00 | NPP-375D | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eadd8a86-cf6e-3cb5-b93d-9d885aa0c461 | -7.20436 | -38.98083 | 2024-10-23 03:34:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e52d4829-203d-31d3-bf77-0ca925e139bf | -6.99983 | -38.77 | 2024-10-23 03:34:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5283aa8f-0bdc-361f-8603-cfb3e577578e | -6.99888 | -38.77005 | 2024-10-23 03:34:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9dc98d8d-0c55-3927-9386-22c82f1b7b54 | -6.99578 | -38.76919 | 2024-10-23 03:34:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7421df30-e208-34ca-bd1f-d9b9814992c5 | -6.92661 | -38.13847 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3288b615-47cb-3fef-a9ab-23ab0777a4d3 | -6.71831 | -37.51204 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3088ca7-dc9f-3728-88de-20a763d83c3f | -6.71452 | -37.51147 | 2024-10-23 03:34:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7292306a-efc9-370a-9874-d4e967d98856 | -5.74983 | -39.78127 | 2024-10-23 03:34:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42aadc41-0046-38ce-a892-ce296fc82a0d | -5.74827 | -39.77877 | 2024-10-23 03:34:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c9e77aeb-eb56-363e-ba55-34e405c737cb | -6.7328 | -40.48951 | 2024-10-23 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59739f06-9568-38e0-9325-9ff9c5576614 | -6.73147 | -40.46998 | 2024-10-23 03:34:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52808183-84f9-3a64-bd6e-3cd9aa69ae18 | -6.72852 | -40.45985 | 2024-10-23 03:34:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 884c5ebb-3348-312c-89b9-772c2406b591 | -6.7274 | -40.49338 | 2024-10-23 03:34:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e21f8190-c164-34f3-95f7-628d1f73897d | -6.71737 | -40.49671 | 2024-10-23 03:34:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0d4d5fa-7eee-3b67-9e07-7237a10da6cb | -6.66278 | -39.61762 | 2024-10-23 03:34:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20245470-e1a9-3bea-bef6-247edc1cb81a | -6.65845 | -39.61687 | 2024-10-23 03:34:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0447b650-cf1b-381d-9d0b-315b228e4f00 | -5.27051 | -41.19529 | 2024-10-23 03:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 872e2139-1a24-384d-b3db-759acf7b810f | -5.26558 | -41.1944 | 2024-10-23 03:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4679961c-7e37-3135-8bae-1ab86486c505 | -7.00796 | -41.30878 | 2024-10-23 03:34:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e322d437-b9ec-3f6e-9fca-6eddd67b6498 | -7.00584 | -41.30946 | 2024-10-23 03:34:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76893082-3ece-3864-951a-e78df285a1f1 | -6.89942 | -40.82716 | 2024-10-23 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 449b1a5b-6355-3764-95d7-e9523d8308e6 | -6.89856 | -40.83212 | 2024-10-23 03:34:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96fb4231-67e1-3ebc-b49c-14225250c972 | -6.44939 | -41.79209 | 2024-10-23 03:34:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bbde353-b49c-302a-a67e-4f6130ae30ba | -6.44887 | -41.79512 | 2024-10-23 03:34:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c56d4dc0-f4ae-327f-b703-e05bdf1f2924 | -4.71183 | -42.92544 | 2024-10-23 03:34:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f573ce97-d8a2-313a-885e-4671d8c73dda | -4.70623 | -42.92453 | 2024-10-23 03:34:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b6259a6-9d86-3873-b392-47c976037b6f | -4.31253 | -43.02599 | 2024-10-23 03:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e67b7d6e-daf3-3d81-a052-d12941a039ef | -3.71722 | -41.68396 | 2024-10-23 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7fea97ab-2098-34b7-aad0-ee384db554b4 | -3.71668 | -41.68715 | 2024-10-23 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 8348b54a-8177-3442-a7ed-c0e75789758d | -3.71231 | -41.68499 | 2024-10-23 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67369588-c6c0-3eb0-8815-72c34557f0fe | -3.71199 | -41.68304 | 2024-10-23 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc3e925b-a6cc-3d3a-a98d-69d38bdb6fdb | -4.13069 | -43.00863 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac21603d-a53d-384c-bdbf-847914d57860 | -4.12609 | -43.01019 | 2024-10-23 03:34:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28d0cb41-253c-3d8b-a672-347230977c21 | -5.92263 | -42.71413 | 2024-10-23 03:34:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6e90b40c-aaff-3999-a8b8-e59391800d47 | -5.53769 | -42.21956 | 2024-10-23 03:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf842d7e-2b47-3da2-a401-064b94038a11 | -5.53646 | -42.21898 | 2024-10-23 03:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3f138208-4107-3fb0-99de-e1073c4e0c4b | -5.533 | -42.21524 | 2024-10-23 03:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7960881d-7f67-3d43-8919-b03a3a6af8f9 | -5.53247 | -42.21835 | 2024-10-23 03:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0324bea1-c752-3f94-abd5-6f248f686226 | -5.58046 | -43.25881 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| eb378ec8-e0e9-3dc5-ac0b-35eb7d4a8cf0 | -5.57889 | -43.20049 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a63ad29e-81ae-3bb3-aa56-adf4bcfc85e8 | -5.57785 | -43.25307 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 274a65d0-6a5f-3ec4-b6b9-347748262737 | -5.57719 | -43.25675 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 22bf3b5e-3222-3b60-93b4-1fc64dc876ab | -5.57652 | -43.26046 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 09f270ad-4512-3022-bf40-f0364246c075 | -5.57609 | -43.25049 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7c6ca29-9a0e-3016-b219-6d3375caea59 | -5.57545 | -43.25417 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 17124210-2154-342b-84e5-aef3fe593051 | -5.57481 | -43.2579 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 72c6806c-7cd4-33b6-86a8-f6ae711c019c | -5.57417 | -43.26165 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| c04ada0d-9598-3948-8ea5-1f13b6acc305 | -5.57221 | -43.25208 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35637df7-0b29-37cb-a821-7a56b54bcbae | -5.57155 | -43.25579 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f0db9452-5b0d-3db6-a143-bfa2a88f1709 | -5.57087 | -43.25959 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9a978e84-f821-32b0-af38-25ffb78fd83f | -5.56981 | -43.25319 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| dd3c343c-ebb3-304c-a94d-bddc0b76c864 | -5.56916 | -43.25697 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |


[Clique aqui para ver as próximas entradas](README14.md)
