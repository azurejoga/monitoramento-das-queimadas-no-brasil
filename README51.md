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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 845f82ba-d83d-3e27-bf3b-9cdc2db24e2d | -21.57881 | -47.73954 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b69f2d15-dad4-331a-ad61-4a48510df355 | -21.57785 | -47.74381 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ba64c3e-dcb7-3e21-9d90-5b5714c9f02b | -21.57593 | -47.75236 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2a425c47-8393-3837-94bd-e0fdd0c1dc7d | -21.57182 | -47.93525 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dfc5b363-df2f-364d-8305-af6cbf54e3cd | -21.56212 | -47.76143 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 061dc17a-86db-360e-88fb-03d8584c719f | -21.55474 | -47.74191 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b55204f6-9c43-39fc-8672-a9d3af99bf4e | -21.40609 | -47.8053 | 2024-10-07 03:40:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1d4b5ab-c2ba-3984-a686-96db854c5b14 | -22.48135 | -48.36742 | 2024-10-07 03:40:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 167460d1-dc92-3611-83bd-ad5b56a33905 | -22.48025 | -48.37214 | 2024-10-07 03:40:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb8edc23-316f-3456-bde6-7d0ef837006d | -22.38717 | -48.59137 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dd6167cb-c3cb-3091-97c0-59648b3ca840 | -22.38137 | -48.59008 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 16a12540-054b-30a5-80ca-a10bb9e6fb80 | -22.38034 | -48.59455 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2940e3fc-68c7-358e-ad35-b4a3343832d9 | -22.37933 | -48.59893 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6f4260fd-b5e2-31fe-8080-80f692dda9fe | -22.37834 | -48.60325 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 08209a41-2e08-36c2-9ad5-955a57bc12f3 | -22.37356 | -48.59751 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 066539cf-393c-3fb8-ac54-2e6b50246966 | -22.37256 | -48.60186 | 2024-10-07 03:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c8b3839f-c106-38de-a560-78cccbd347a5 | -23.86067 | -48.18474 | 2024-10-07 03:40:00 | NPP-375D | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d78c4e4-f995-3799-9550-75fb67ec7a5c | -23.85977 | -48.18866 | 2024-10-07 03:40:00 | NPP-375D | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f524fb92-d8ef-3e5a-b5ca-137d34da9170 | -20.75924 | -49.47494 | 2024-10-07 03:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 6561c5cc-477a-3d89-b914-a5fceff6000b | -20.75797 | -49.48034 | 2024-10-07 03:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 7cac43c6-a2f1-3155-b623-125a0e18281a | -20.75671 | -49.48572 | 2024-10-07 03:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d074580c-6bc2-3d2a-a8ca-dc55ca2de700 | -20.75175 | -49.4786 | 2024-10-07 03:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 007ed977-3338-3e41-80cb-0073507c6950 | -20.75048 | -49.48403 | 2024-10-07 03:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 8dfae8ca-83aa-37cf-a37b-563ad4da320e | -20.70759 | -49.63791 | 2024-10-07 03:40:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bf44dd83-a32f-3daf-b1f3-8b1ceb321402 | -20.70629 | -49.64342 | 2024-10-07 03:40:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 48a51652-278b-395e-a6aa-20a0172d3d16 | -20.70498 | -49.64896 | 2024-10-07 03:40:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 0de90515-16bb-3daa-866f-54b92843beb7 | -20.60609 | -48.48367 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9a045dc5-1a7e-3c70-9141-967c6eb7f37d | -20.60506 | -48.48815 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6b052eb8-d4df-32ab-9e79-18b4c645821d | -20.60399 | -48.49276 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 827872b6-ae0c-3179-b7fe-d5bf021bfe15 | -20.60386 | -48.48655 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a2b36f42-3445-39ac-abf6-b570ab166cae | -20.60291 | -48.49742 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 28fcac0f-b3b2-3c25-abe0-e7d58cc06ad6 | -20.60183 | -48.50211 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b561569-abad-3a28-845b-5288dc86723f | -20.60179 | -48.49583 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| eb674055-ef95-3a2b-b201-7a217d634ec7 | -20.60074 | -48.50684 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86072a12-b05a-39c3-aafc-bd070f2253dd | -20.60073 | -48.50054 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| b55bb6f7-c1ae-3879-ac4a-167e245cfc81 | -20.60016 | -48.48221 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0bdc381e-a9cd-39f3-92a9-76b8090f2053 | -20.59967 | -48.50527 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3dcffc73-3a95-3d62-8d61-d16c1be6fcd9 | -20.59913 | -48.48668 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b41fdaeb-cc9a-3d2e-88b4-ea656d2e36b5 | -20.59793 | -48.48507 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 89264e40-4612-370e-ae71-2e4774393628 | -20.59694 | -48.49612 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 165.4 |
| c0832ce1-7e8e-32a0-b262-1ad15fb66372 | -20.5969 | -48.48968 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ec5aa3c6-1c1d-3f65-b86c-ed5bc3b0d948 | -20.59585 | -48.50085 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 43.4 |
| c5fb19ce-9588-35c8-bd47-873fffee822a | -20.59582 | -48.49448 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 735da515-8b57-34f9-8416-3b12c63267a3 | -20.59475 | -48.50558 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 3848e7f2-f0f1-36ad-9bd1-1cc60e07515a | -20.59475 | -48.49925 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| d278430f-0644-3043-87d1-d0037a393f8f | -20.59369 | -48.504 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 43f03fe4-84d3-3051-993f-c3eb24061f14 | -20.59366 | -48.51029 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cea8200c-4a23-3604-a38a-1439874a17d6 | -20.59318 | -48.48527 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| dfae04c4-680e-3347-9c1b-7e727d62469c | -20.59263 | -48.50869 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4d33c708-d019-35e3-80fe-0ed30da15a2e | -20.5921 | -48.48995 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 165.4 |
| ccd41132-f59f-351c-8a97-74ec1a94a359 | -20.59199 | -48.48367 | 2024-10-07 03:40:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aa0eb13c-bd0d-3c2a-b268-79309c23e4cd | -20.59097 | -48.49479 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 8e2962a7-c72f-35b7-9a36-aa4626abf147 | -20.59095 | -48.48828 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7c762c4b-97d3-305a-b385-075594ba04ba | -20.58986 | -48.49958 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 43.4 |
| e5627bee-3ba0-3f89-ad85-a09047861510 | -20.58986 | -48.49311 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ac26b797-de68-36e8-80d6-2502691fa755 | -20.58878 | -48.49794 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 88facd88-56b5-36f2-a907-b3c07cbfe3f8 | -20.58876 | -48.50431 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 43.4 |
| c5d5933f-14e7-3b63-a0b2-38e2d1ed8c7c | -20.58771 | -48.50884 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef7db3c7-ce04-335a-9bfb-bb5bd35464b6 | -20.58771 | -48.5027 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9f116c51-8d69-35ba-9e50-ba37bf621d76 | -20.58668 | -48.50727 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0a669ae8-d50a-38dd-a404-1eba6bf296a6 | -20.58614 | -48.48859 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8154928-1e70-3bb6-957c-d0270786afc4 | -20.58501 | -48.49345 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abc59f1a-9608-3efb-bbba-9cf9e740e727 | -20.58391 | -48.49816 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 413e925e-345b-3ab8-aeb9-41d88cfd7e07 | -20.58389 | -48.49176 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| aa5aeef0-b6ce-3627-96ed-a7d83a47e2d7 | -20.58286 | -48.50268 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 31f59e21-8dd5-35f2-93c5-ff49c6ca80df | -20.58282 | -48.49654 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3361a16b-6d37-332a-b480-1e3d49a46117 | -20.58183 | -48.50712 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 32eff313-c631-3967-bdfd-98f20c4cdef9 | -20.58181 | -48.50104 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 859ad92d-440d-318d-9a62-072cf3806ee9 | -20.58081 | -48.50547 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f8d8410d-5cc7-3efa-88d7-c98731ebdcd8 | -20.58079 | -48.5116 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1326dd48-6e3c-3fca-95b4-5434b8ba7b82 | -20.57979 | -48.50998 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2f03e5a4-770e-3b5a-80b0-8823dbae20c9 | -20.57874 | -48.51465 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| eb98026d-2c4a-3bcf-b167-9fac2008413a | -20.57588 | -48.50569 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 90f9556f-a0cf-31fe-bece-9f424fb5d8b3 | -20.57481 | -48.5103 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0230dbb5-e2c2-33c8-b49b-6a3fcea713ed | -20.5738 | -48.50873 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c3e1e08d-e5b5-34c1-af45-85ab5a0a2d88 | -20.5737 | -48.51506 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 2ccea0a7-d85d-30c2-8a3e-89e52eac5f34 | -20.57273 | -48.51342 | 2024-10-07 03:40:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4717550c-01e1-36f7-8b3d-b8a2b4456b03 | -23.14442 | -49.81012 | 2024-10-07 03:40:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e970b4a0-1b91-31e6-9093-6b571d48d4dc | -23.14338 | -49.81442 | 2024-10-07 03:40:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 27664a90-ba95-3c92-b704-92c5fa2b4e80 | -23.14239 | -49.8185 | 2024-10-07 03:40:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8b82c35d-38dc-3db3-9595-6dcc5cb48416 | -23.04497 | -49.85276 | 2024-10-07 03:40:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b63aa0e1-7ebe-3032-918b-dcd9303564bb | -23.03889 | -49.85105 | 2024-10-07 03:40:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| adc3b6e6-3b48-3924-8c1e-1b4787215ce7 | -23.03768 | -49.85608 | 2024-10-07 03:40:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e5e58428-7e77-357a-867a-2c1f225a8dfe | -20.19346 | -50.96855 | 2024-10-07 03:40:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b075a27-0746-39ce-8ca9-3dabb53dffd5 | -20.19242 | -50.96675 | 2024-10-07 03:40:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c35c7306-be78-31b8-b622-c28cf24eba7a | -20.18668 | -50.96651 | 2024-10-07 03:40:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8d7cf326-7cf7-35ca-b49e-774a71fcbce1 | -23.05632 | -51.4576 | 2024-10-07 03:40:00 | NPP-375D | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 512f1305-1fab-331d-ae5f-02bc361ac0fb | -25.6229 | -51.42926 | 2024-10-07 03:40:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4868ada8-d188-30ee-8e9d-bfa9df61f04e | -2.8569 | -52.9197 | 2024-10-07 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ef613af4-f3d9-3432-a156-95b26633deec | -2.857 | -52.8993 | 2024-10-07 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c7887a5d-2471-3e72-8faa-3f4846991207 | -2.8753 | -52.9192 | 2024-10-07 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 39ff135b-87a6-3dba-b969-2b37ab983975 | -2.8754 | -52.8989 | 2024-10-07 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 4fddadeb-7836-3062-ba45-6b864c8c9140 | -10.8754 | -63.9169 | 2024-10-07 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 44c75209-7353-3a92-87ac-a87fffa48601 | -10.8755 | -63.8979 | 2024-10-07 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c5e08e1b-0d08-37db-8d01-34e6e1ca34aa | -11.2847 | -51.3878 | 2024-10-07 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0b462c2b-c080-369c-ad18-c875c5c18364 | -11.285 | -51.3666 | 2024-10-07 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1fa9cca9-f1be-3a05-8ddc-b31e19969719 | -12.1086 | -50.8926 | 2024-10-07 03:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b519cffa-b002-37c2-928c-e7cac4bb7c91 | -12.1274 | -50.9118 | 2024-10-07 03:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b0932c2e-f890-3741-89f8-d59898a3a9ec | -12.1277 | -50.8904 | 2024-10-07 03:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 45006be5-5d45-3206-b219-ff21c1285d33 | -12.1468 | -50.8882 | 2024-10-07 03:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README52.md)
