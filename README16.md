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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad4b2c6-6c8b-3ac7-ae7c-bf05f91c3761 | -20.619499 | -41.233299 | 2024-09-28 01:04:56 | METOP-C | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c51f055-1b9e-364c-90f4-7c7bc4efbd66 | -22.569 | -49.192001 | 2024-09-28 01:04:57 | METOP-C | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1546d730-a3f9-35fe-95d0-75030be9b32f | -22.3563 | -49.301601 | 2024-09-28 01:05:01 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 151e787f-a3fc-3447-b6e8-e6062b7dc57c | -22.358 | -49.309101 | 2024-09-28 01:05:01 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd1b8b21-cfa5-3cbb-bf69-a45d11e32365 | -22.3482 | -49.3116 | 2024-09-28 01:05:01 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ee046cb-b08b-3643-be7f-7fddcbf5cfbf | -22.349899 | -49.319 | 2024-09-28 01:05:01 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cda542e-038a-3eb1-847a-b36ba5abc6b9 | -22.3515 | -49.3265 | 2024-09-28 01:05:01 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9cf08b4b-0544-3aaa-86c8-a05b495a4da9 | -21.8477 | -48.2015 | 2024-09-28 01:05:05 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21b9bf13-8b3f-3741-8501-da1593d05e85 | -21.280001 | -45.7934 | 2024-09-28 01:05:05 | METOP-C | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 984630b4-2d49-3d0d-bce7-8c86709ef795 | -21.282499 | -45.803299 | 2024-09-28 01:05:05 | METOP-C | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a2f2f6e-5a40-32a7-b0bf-76830fcd3479 | -21.849501 | -48.209301 | 2024-09-28 01:05:05 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7a905fc5-ee7d-370c-b533-a5f5d325a9a1 | -21.8379 | -48.204102 | 2024-09-28 01:05:05 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 99e1a9b0-9438-3a4e-a2fa-05db99c67110 | -21.839701 | -48.211899 | 2024-09-28 01:05:05 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fefb248a-a87f-3c10-a227-0ed5f47795ae | -21.892599 | -48.486 | 2024-09-28 01:05:05 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 976a2f17-8fdc-3799-ab1f-edc4c604f21c | -21.8944 | -48.493698 | 2024-09-28 01:05:05 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 13a57be3-70ee-3926-b2dc-e59a5f822d24 | -21.8962 | -48.5014 | 2024-09-28 01:05:05 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87fa0f1a-3670-3104-a757-f91531e3f1f9 | -21.8829 | -48.488499 | 2024-09-28 01:05:06 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0300cb61-d708-3f8f-bce1-da1e9b2c79f6 | -21.884701 | -48.496201 | 2024-09-28 01:05:06 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f2fce115-b172-302b-ab61-1e971cf5719a | -21.886499 | -48.503899 | 2024-09-28 01:05:06 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| df922dd8-37df-36f4-982d-986c24e7379d | -21.627199 | -47.744598 | 2024-09-28 01:05:07 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a23909d3-4ab2-35eb-b69e-1c01f560f0b1 | -21.629101 | -47.752701 | 2024-09-28 01:05:07 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e89bc9da-0a13-3e57-9286-92491a61fdb3 | -21.617399 | -47.7472 | 2024-09-28 01:05:07 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c45bec46-2bc5-3305-b7d1-e4267517c822 | -21.619301 | -47.755299 | 2024-09-28 01:05:07 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1b44efae-fa05-3367-8637-c0d87798b6fc | -22.711901 | -53.2309 | 2024-09-28 01:05:09 | METOP-C | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03a0ff76-e3e6-3fdb-9442-b2be5e4a4698 | -22.703899 | -53.242001 | 2024-09-28 01:05:09 | METOP-C | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f86b048f-1d45-3f47-9578-97ebdd30afb8 | -22.6889 | -53.217499 | 2024-09-28 01:05:09 | METOP-C | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c972c952-403f-310f-b9f8-a173a075c7f3 | -21.4151 | -47.766499 | 2024-09-28 01:05:10 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 00a3f781-2391-3035-95da-f39bb2cb7f54 | -21.417 | -47.7747 | 2024-09-28 01:05:10 | METOP-C | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3b16ce5-4a14-335b-aa59-b5602b492fd5 | -21.4189 | -47.782799 | 2024-09-28 01:05:10 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3c29258f-936b-3a41-a249-2dd07720f69f | -19.9161 | -42.119701 | 2024-09-28 01:05:11 | METOP-C | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| acf8a78a-f550-3771-b47d-6f657add406b | -19.8727 | -42.1516 | 2024-09-28 01:05:12 | METOP-C | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a1ff317-ebda-3122-b9e9-ee893328b674 | -19.826599 | -42.403 | 2024-09-28 01:05:14 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 962c890e-20cc-36b5-8254-2a788348f4f4 | -19.866199 | -43.169201 | 2024-09-28 01:05:17 | METOP-C | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| becb4586-db22-3761-be5c-44846772685f | -20.500401 | -45.872501 | 2024-09-28 01:05:18 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b21c466c-6729-391d-a08a-ff69b0eed023 | -20.502899 | -45.882599 | 2024-09-28 01:05:18 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae56f17d-b14a-338a-b985-a895dbc455c7 | -20.5054 | -45.892601 | 2024-09-28 01:05:18 | METOP-C | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38a2d599-f25f-3064-8d26-e3c5e271a22e | -21.1586 | -49.069901 | 2024-09-28 01:05:19 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b14dde85-5fe9-39c5-a9e8-91903b680ea6 | -21.160299 | -49.0774 | 2024-09-28 01:05:19 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ad7e038-176d-3cd4-9651-68156c531212 | -21.090799 | -49.134899 | 2024-09-28 01:05:21 | METOP-C | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bd88035-a93b-31b4-a6d7-4f33947b539b | -19.5179 | -42.878601 | 2024-09-28 01:05:21 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90d08802-e0a8-3f9c-b9c4-72d59e37e73e | -19.383301 | -42.5723 | 2024-09-28 01:05:22 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 616f605d-6510-3ba9-955f-0d9ac83259f3 | -19.387699 | -42.588699 | 2024-09-28 01:05:22 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45810fcc-df21-3103-941e-506eeb72c35c | -19.373699 | -42.575199 | 2024-09-28 01:05:22 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 437b0720-ac89-37b9-8d2a-37108f1fec6f | -19.378099 | -42.591599 | 2024-09-28 01:05:22 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5817bd1f-6bf3-3118-9885-0048154715d2 | -19.3641 | -42.578098 | 2024-09-28 01:05:22 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6badf15c-8709-3abf-aa20-08ac4792eb67 | -18.6947 | -42.068802 | 2024-09-28 01:05:31 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bfe8e7e7-46b8-3ff8-beac-fcd9829aaf4b | -18.699699 | -42.086899 | 2024-09-28 01:05:31 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5444a81-1b9f-3dd4-9079-93b8141fb48d | -18.4935 | -42.2076 | 2024-09-28 01:05:35 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61b4dab2-dba5-3a64-b9f8-554076aca0d9 | -18.474001 | -42.1744 | 2024-09-28 01:05:35 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| daf39622-7dcf-3052-9172-757dbc3f1516 | -18.479 | -42.192501 | 2024-09-28 01:05:35 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd908788-a321-36b2-bb82-b88fa39ebcbb | -18.4839 | -42.2104 | 2024-09-28 01:05:35 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67271e11-9b24-3a77-861d-d0765114fd85 | -18.3559 | -42.735001 | 2024-09-28 01:05:39 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b76b28c-bd89-3443-b30d-051b7698b935 | -18.360399 | -42.751701 | 2024-09-28 01:05:39 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0895138-2486-34cd-b4e9-2b11bbd7cf12 | -18.364901 | -42.768398 | 2024-09-28 01:05:39 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 136fd940-a623-38cb-8bae-e708dae05417 | -18.3508 | -42.754601 | 2024-09-28 01:05:39 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3506e4b3-6a09-32df-9156-6948d341b2ec | -18.137899 | -42.3909 | 2024-09-28 01:05:41 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c8d2ff6-c022-3b7c-8549-033aa9eca556 | -18.1427 | -42.4086 | 2024-09-28 01:05:41 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c24e690b-e3ba-306d-91b1-717e9cca4943 | -18.1283 | -42.3937 | 2024-09-28 01:05:41 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 892d423b-7e94-3171-af09-74cd7176aeed | -18.133101 | -42.4114 | 2024-09-28 01:05:41 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72b9c8cd-6e95-357f-9a2e-bb8664ca3ac8 | -17.7878 | -43.251801 | 2024-09-28 01:05:50 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5c74df9-b9cf-369e-abfb-540bb9d1150b | -17.792 | -43.267601 | 2024-09-28 01:05:50 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d58d1a64-1d99-3c8d-8510-a0adc40f9705 | -17.7962 | -43.283401 | 2024-09-28 01:05:50 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82b81e0a-56c8-3fbd-b602-6a1c83195eae | -17.778099 | -43.254601 | 2024-09-28 01:05:51 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0af9020e-5e7c-3508-a206-52080ee06a44 | -17.782301 | -43.270401 | 2024-09-28 01:05:51 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ebfa6ed1-b821-321b-8b91-8084563e3f56 | -17.786501 | -43.286201 | 2024-09-28 01:05:51 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd3afc2-4f41-395b-98dc-1b4b069cdc20 | -18.061899 | -44.3713 | 2024-09-28 01:05:51 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b583417-57dc-3a5c-8f62-93c89485cd3a | -18.0488 | -44.360802 | 2024-09-28 01:05:51 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd49d95d-9751-3af1-a3ed-b556987bbf5f | -18.0522 | -44.3741 | 2024-09-28 01:05:51 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6230b3-ad47-39df-9c16-20807cdac9c3 | -18.0557 | -44.387299 | 2024-09-28 01:05:51 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13b551b8-7f9e-3765-98b2-eb16337f1090 | -17.4452 | -42.595501 | 2024-09-28 01:05:53 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7415ab68-bdce-3c2d-8f0a-d61cbf076997 | -17.450001 | -42.613098 | 2024-09-28 01:05:53 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f453aacd-c0e4-36ab-a265-18c949feef67 | -17.4356 | -42.5984 | 2024-09-28 01:05:53 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecfb296-9161-3e1e-ba7b-fd8fc5c7f706 | -17.440399 | -42.616001 | 2024-09-28 01:05:53 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 09dbea11-7434-3464-8c78-dafc237249da | -17.836599 | -44.463402 | 2024-09-28 01:05:55 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a4a9174d-336d-3f7f-9745-4d634c48b622 | -17.8456 | -45.8797 | 2024-09-28 01:06:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd8df707-3ec3-35ea-99cc-67cdfde1f450 | -17.848301 | -45.890499 | 2024-09-28 01:06:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3b1e21f-9c1c-37af-afdd-ff91d7c288a8 | -17.8358 | -45.882301 | 2024-09-28 01:06:01 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7915e0c0-f851-330e-9931-d0eb49a8dea7 | -17.8386 | -45.8932 | 2024-09-28 01:06:01 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bdb4b40b-75c1-3395-882f-2ab3949daf9d | -17.0432 | -43.2248 | 2024-09-28 01:06:02 | METOP-C | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23de4cbb-0ad9-3948-8ca9-dde027e2454c | -18.164101 | -47.980598 | 2024-09-28 01:06:04 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b279993-cd08-3522-a8f3-73645be16e91 | -16.882 | -45.3111 | 2024-09-28 01:06:14 | METOP-C | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8646fb8e-bbe0-346f-9b67-2fa0dfd0f906 | -16.885099 | -45.3232 | 2024-09-28 01:06:14 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8c4db66-2010-3f37-ab66-8705665f6275 | -17.0054 | -45.920502 | 2024-09-28 01:06:14 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 27626f31-dfcc-3378-b70a-f0428b2c499a | -17.145599 | -47.6203 | 2024-09-28 01:06:19 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24d3e519-1e48-3708-a6ea-ba5a27f955ba | -17.1478 | -47.6292 | 2024-09-28 01:06:19 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 563915ba-8f54-31c8-aa26-23e379a09712 | -17.135799 | -47.622898 | 2024-09-28 01:06:19 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95d21d0a-9575-311a-b197-3f0ccc102701 | -17.138 | -47.631802 | 2024-09-28 01:06:19 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1700f7a-915e-35df-89f2-665b59334eaf | -16.8274 | -47.6745 | 2024-09-28 01:06:24 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b528a9c-24db-3aa5-b0a8-c516eb29d7d5 | -16.822001 | -47.694801 | 2024-09-28 01:06:24 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23bafd12-5e97-3ca7-9cf9-8541f2502f8b | -16.8241 | -47.703701 | 2024-09-28 01:06:24 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57444020-7057-3a50-9130-8fbd078aaa9b | -15.522 | -43.551899 | 2024-09-28 01:06:28 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6da4e51e-5e7d-3eff-9eda-6d705cb01ed7 | -15.508 | -43.5382 | 2024-09-28 01:06:28 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c3f81fc-4895-35c1-9db4-e065eacb927c | -15.5123 | -43.5546 | 2024-09-28 01:06:28 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc8ab03d-c92c-375a-ac25-28d8988948c2 | -15.5167 | -43.571098 | 2024-09-28 01:06:28 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b857e96-d0ac-38e7-b9bd-b91634b8f7ef | -15.3635 | -47.445702 | 2024-09-28 01:06:47 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9227322-2c14-3f69-899f-3f1d82407b39 | -17.1171 | -56.170399 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da25b947-8f77-3214-b7dd-ea27ec14d17e | -17.1192 | -56.180901 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b7f9920-8813-383c-bfcd-63bfecf70328 | -17.1073 | -56.172501 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d9281f3-c94c-3dfc-a29a-3381402db467 | -17.1094 | -56.182999 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10d379f4-6812-3274-8465-5ae787ed1556 | -17.1115 | -56.1936 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README17.md)
