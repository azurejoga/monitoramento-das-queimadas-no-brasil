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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af051c9b-92b1-3813-87c3-8cbf28a7c3e9 | -20.42529 | -47.67405 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a66164-3567-350a-a0f0-7dce7f39cd77 | -20.42469 | -47.67849 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4aeca37-9279-3bd8-b9f0-ea662865a265 | -20.42467 | -47.65125 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e220e61-b719-3321-9508-bae51edc6815 | -20.42408 | -47.65563 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ff668a0-b7d2-3ce0-a83b-8067546b6a92 | -20.42348 | -47.66002 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7694987c-2159-30cc-92f8-f168ef3c4e91 | -20.42288 | -47.66446 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1757eae3-25e2-3341-acf9-1d5f4b8da927 | -20.42227 | -47.66897 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a6b7055-5bab-3f4a-a0ae-33f0ade380bd | -20.42224 | -47.64177 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| deeaa8bf-6818-3dcd-94d1-d415b9ca0fbf | -20.42166 | -47.67347 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adba28d9-6272-3c3e-a318-7d1653f8d554 | -20.42165 | -47.64616 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d549ac3f-a355-3847-832d-44223f1060b6 | -20.42105 | -47.65057 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cdcd362-28c3-3a96-810b-6bd7a9c18069 | -20.42045 | -47.65499 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b33e3c3-949c-323c-a151-f802ee07f999 | -20.41863 | -47.66848 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9edafc1-8085-3a02-8e79-6529ea0a0a9a | -20.41741 | -47.65005 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 453aecd5-77eb-3f53-bba7-b8bd2fecb96a | -20.38923 | -47.04895 | 2024-10-08 04:38:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1630d9fa-e77e-3cf9-9a8f-035cbe513851 | -20.38548 | -47.04836 | 2024-10-08 04:38:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| addd9b50-1f1c-38d2-9982-6813c3984712 | -22.26698 | -48.53111 | 2024-10-08 04:38:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b33a46b-a477-3ace-9bc7-c80c3cef752a | -22.26342 | -48.53057 | 2024-10-08 04:38:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a6e3487-11e9-3911-a4ac-51bca4d44ccb | -21.64262 | -47.71628 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cfee462-3895-3561-a873-a3de67477449 | -21.63895 | -47.71568 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbef8080-a8dc-37b0-8a58-557dc544fae4 | -21.63528 | -47.71509 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae53112d-8203-3f3c-a3c1-897e8dce7062 | -21.60528 | -47.715 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 885bc6c7-c34d-35cb-95fa-45a5b4a26629 | -21.60467 | -47.71961 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac2281fb-c452-391f-bf60-7f434406f7fa | -21.60098 | -47.71922 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e4daf3-2366-3586-bd02-c671d980850c | -21.5979 | -47.71418 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f359f40e-1bb0-368a-b49d-e1658103e22a | -21.59727 | -47.71888 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adfdde29-cb15-32c3-9e01-da66df6866b2 | -21.59666 | -47.72349 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f26981-b7ae-392e-ae19-fea5d5fcc092 | -21.59606 | -47.72801 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af7c547f-6a43-3844-a7ca-325cf5eb14d3 | -21.5942 | -47.71378 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a757a008-265b-3dbf-8508-2ee63373df43 | -21.59297 | -47.72306 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f310270-3761-34cc-863e-e5d6a4b667e9 | -21.59179 | -47.732 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76f1a083-45c2-3e5b-bdde-e6c448ea2e96 | -21.59056 | -47.96365 | 2024-10-08 04:38:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62b6cdbb-dfd3-35d2-88f2-0de222aa650a | -21.59051 | -47.71336 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26da2353-4ef4-3b94-9add-3e671f7351d2 | -21.58815 | -47.95409 | 2024-10-08 04:38:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 652134e5-6a15-3c0f-9bfe-247aaddf6a27 | -21.58811 | -47.73146 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe98d38-aebc-33d9-a1a7-a139feb76c13 | -21.58393 | -47.93039 | 2024-10-08 04:38:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 942256e0-ea6d-3414-b712-41829c31a408 | -21.58264 | -47.74451 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6018214f-f589-3c94-b5c6-3a7e72a93a37 | -21.58151 | -47.92079 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ee9ee519-f155-3c94-94b5-3f8c149fc326 | -21.57787 | -47.92023 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0967b5b2-7f81-36dc-8cd3-fd67c70d9bf5 | -21.57727 | -47.92474 | 2024-10-08 04:38:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 06d9d175-7008-3b6b-975e-c27e3c0189df | -21.56939 | -47.92812 | 2024-10-08 04:38:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 706c87fa-610c-3f56-bee8-133e751a9dfd | -21.56878 | -47.93266 | 2024-10-08 04:38:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6da203b-6422-37f9-9848-21286d3bc790 | -21.55899 | -47.72962 | 2024-10-08 04:38:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f3e3d6-a18b-3266-bc84-4c951e0a736c | -21.51191 | -48.07218 | 2024-10-08 04:38:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e69e8da-ca80-3602-9c32-ad102cfadb61 | -21.40672 | -47.80614 | 2024-10-08 04:38:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e764774-536b-387a-920c-5e9d5c82b3ae | -21.3217 | -47.60768 | 2024-10-08 04:38:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b21387-1cfc-3781-8fa6-53f85be0b4da | -21.3211 | -47.61216 | 2024-10-08 04:38:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f154ca-710e-3ed8-af9c-fbeb312b755f | -21.318 | -47.60725 | 2024-10-08 04:38:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56faa9bd-c97c-3cc8-885d-b3e1f0b47705 | -21.31741 | -47.61166 | 2024-10-08 04:38:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b707f9ad-4d38-342e-bccd-8589b5fdc191 | -21.09805 | -47.23416 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1f07fe4-0239-3ddb-8e5e-57cd40630865 | -21.09747 | -47.23857 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62e8a5db-72b2-3a4d-a968-b62f5dd90cac | -21.09662 | -47.23619 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc8658e4-49e3-3278-930d-59d2d9a07123 | -21.09488 | -47.22913 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62c2fc8d-e15a-3082-8379-d173cadc9869 | -21.0943 | -47.2336 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ba53450-8308-37db-bd7a-0c271bb375bd | -21.09347 | -47.23126 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f92b54a-a542-39fc-99ae-1c4c4c3bfa61 | -21.09288 | -47.23562 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f41a10bb-db40-3d56-8515-e433f174c8a9 | -21.09177 | -47.22363 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51077335-f644-3542-84e0-a777b6befb80 | -21.09114 | -47.22855 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c3b06eb-c8c9-3e9f-9fd1-9448bc9ed65d | -21.09102 | -47.22108 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 863532c8-3984-3ecd-8b77-12158b8e80ac | -21.09056 | -47.23302 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9be9b7e-7fed-3170-992e-fdadf154e3d7 | -21.09036 | -47.22601 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe9f9fe7-c24b-3264-ae25-7d52a0201475 | -21.08973 | -47.2307 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19c710c4-e2c9-38ee-9d99-17cbe36d8281 | -21.08724 | -47.22078 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 970c32a2-492f-3044-ab08-57f61de51b11 | -21.0866 | -47.22552 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a731f38-018f-31e7-a7f6-48560097f88b | -21.0835 | -47.22015 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0a364a5b-1768-3670-ba87-ab30c016ee31 | -21.07849 | -47.229 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a53f121e-6a3a-3dbd-84b8-66363c0796f8 | -21.07607 | -47.21856 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f928fba3-12a0-3f7b-bf04-fc3fc6ca2353 | -21.07541 | -47.2235 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e95ebaca-c6f2-30f0-9ac0-88597cfd0056 | -21.0717 | -47.22261 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32814f66-aca5-3262-b4c9-f476c5f8609c | -21.07102 | -47.22771 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19fdc3e4-8eda-3c7e-9eb6-6fe9861bb50c | -21.06852 | -47.24636 | 2024-10-08 04:38:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b056b5a6-4d5a-3394-b513-17db3745ac73 | -21.0673 | -47.22696 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ff6c5a7-262f-36f4-862c-89a1287cbe14 | -21.06663 | -47.23199 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 66159a93-2273-34b3-9f14-fb8a1332c1c7 | -21.06476 | -47.24596 | 2024-10-08 04:38:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5b6448e-4ce8-3817-bbdd-e405fd034002 | -21.06358 | -47.2262 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9f44045f-42dc-38a7-8617-4e4139a7c2e5 | -21.0629 | -47.2313 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de1b5b29-8735-3554-8c5b-64407d97446c | -21.061 | -47.24556 | 2024-10-08 04:38:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b8d9aec-ca80-395b-b6a3-c3d6fb2d1103 | -21.05985 | -47.22548 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41e1e8d2-9080-38b6-8f3c-a560fa9b6916 | -21.05919 | -47.23054 | 2024-10-08 04:38:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c634e2d5-4f88-3b5a-92e3-7c51e7d7bed5 | -21.97942 | -47.39229 | 2024-10-08 04:38:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a2246234-b048-3a62-a9bf-e7bc4c05fb60 | -23.42716 | -48.88435 | 2024-10-08 04:38:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eaf5d0b2-9929-384b-bd32-8b078a07edfc | -22.82642 | -48.42218 | 2024-10-08 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e4eaa20-6154-350b-b577-98f7e78de7af | -22.82285 | -48.42145 | 2024-10-08 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bd21079-ceed-30f8-a581-1d528fe856dd | -22.80312 | -48.45874 | 2024-10-08 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3b5ddc7-fea4-3936-a2e3-638bb53548c4 | -22.48232 | -48.37745 | 2024-10-08 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3043e150-fd4b-3f8f-8651-e07644ff4c74 | -22.47688 | -48.36335 | 2024-10-08 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05b5a9b7-58d2-3887-b0f0-4ca843e196a4 | -22.47331 | -48.36257 | 2024-10-08 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f4ba8e72-2b64-3b00-9aa5-ab5f2e5469f0 | -20.8715 | -48.4685 | 2024-10-08 04:38:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bc28ba4-8ed1-38bb-a9d9-1a8d8ce764c2 | -20.86798 | -48.46793 | 2024-10-08 04:38:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94024597-a36b-35de-b810-07d3a10120e6 | -20.57532 | -48.49332 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62c1e06c-d20c-339a-9f19-894ccd809c96 | -20.38305 | -48.83126 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 271112ba-e2c2-3da8-be21-4c3b05b6acd9 | -20.38304 | -48.80659 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 834c04a1-8217-3672-bca5-d0c78f92136e | -20.38247 | -48.83528 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dc65d16-cf74-3691-9a9e-50152c2d7c4a | -20.38074 | -48.82269 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf1fc11e-9737-3b99-9074-c9b334a7ba26 | -20.38017 | -48.8267 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188f7082-fa22-3196-8e7e-2bb7f62d004c | -20.37959 | -48.83071 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eaa50a5b-15b7-32cf-9f1f-3982d9af6ac9 | -20.37902 | -48.83472 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2bc19161-1745-31ce-a388-798a8e5176ba | -20.37901 | -48.81007 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe0644c6-7b7d-3b48-b744-ead6d225798a | -20.37728 | -48.82215 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73c6604d-8854-3d9d-bf79-0d8396a8fe3e | -20.37671 | -48.82615 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README74.md)
