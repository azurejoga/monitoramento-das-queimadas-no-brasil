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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3519ac2a-d4d1-3af4-bfc8-409ace829e82 | -21.59744 | -47.71849 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0b6d8ef-57a4-3aca-99e8-878cd83da03b | -21.59707 | -47.72223 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36f9f1d5-bcc2-354c-92c6-8acc5e42d895 | -21.59673 | -47.72574 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c456d7e8-9054-3ae4-9eca-c916dcc654b2 | -21.59639 | -47.72922 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9392808-29eb-3bca-bb5f-3ddff2a40e85 | -21.59229 | -47.71478 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f17bac4f-b15a-379e-b470-35d0778ff7cf | -21.59156 | -47.72223 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ade2fba-4ab0-3744-8a82-20968a02d8e4 | -21.59124 | -47.72554 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a60bdd53-0f82-37aa-911b-119049bd5c34 | -21.59059 | -47.73225 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a72a0fdc-c83a-31b1-a376-29a3e8aab31a | -21.58478 | -47.73529 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d2a7436-7163-3f52-b4a5-05dc0a6631a9 | -21.57866 | -47.74168 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a20859f9-7442-345d-8304-7c56c5dee830 | -21.57759 | -47.91985 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d9efc5d3-0590-3922-8fac-607546031cca | -21.57724 | -47.92342 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0adf2fc2-4f7b-36cf-bca9-d518da2336f2 | -21.31878 | -47.60965 | 2024-10-08 04:59:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6d59af-75ee-34fe-9100-f0d710de9fd6 | -21.31844 | -47.61297 | 2024-10-08 04:59:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08834bb2-e800-3952-a6f4-16b61ec5d786 | -21.31326 | -47.60944 | 2024-10-08 04:59:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f38f007-8cfb-313b-9efd-825468e3e7b0 | -21.09472 | -47.23008 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef6f8ba-cf9b-3bdf-9840-7d3e01bf22c4 | -21.09443 | -47.23322 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb45db3f-efb4-3181-9ae6-4d12f875d0ac | -21.09413 | -47.23628 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de07e697-a4e5-340c-bf20-021933696cae | -21.09382 | -47.23951 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9287fd86-34d3-3367-aa83-26ab1cdfd8ef | -21.08988 | -47.22159 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f5a7cb6-7699-36e4-9be8-34c9a9eca248 | -21.0895 | -47.22564 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8644223-740b-3ee8-88af-45568db36ff1 | -21.08914 | -47.22941 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73141d46-a477-30b0-a960-91a70ceeb765 | -21.08884 | -47.2325 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54edb0c1-1b62-32ba-bca1-0c4553139ae3 | -21.08855 | -47.23557 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d6a8514-b614-335f-a70d-3c38263a57db | -21.08466 | -47.21708 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd19a0c-3a4d-33b8-8c08-9554f2a07304 | -21.08425 | -47.22138 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73616b80-878a-3430-891e-ae119f83ff13 | -21.07797 | -47.228 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faf0f1d5-03fc-31da-88da-ca498c6fce5e | -21.07285 | -47.22236 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8047585-f1d2-3381-b2ff-23c72e1fadd3 | -21.07242 | -47.22692 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdfd1133-4beb-3977-8628-fcab38f7de20 | -21.06942 | -47.22358 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5156323-d17c-3f2b-888a-97fa78864569 | -21.06893 | -47.22839 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0927fcac-8938-3c5c-a007-4907d9517787 | -21.06709 | -47.24665 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 840c9913-e3ee-3168-b503-eb0750e23687 | -21.06691 | -47.22545 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8a2244a-5b0f-3eff-8d19-3abce71a1303 | -21.06647 | -47.23012 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe50fdc-3c90-34fe-819b-124f2eaa0ed4 | -21.06606 | -47.2346 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e40d896c-db3c-3b36-a262-09a7e2c2afba | -21.06507 | -47.24504 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28afa5de-e5cc-38d1-852d-4f8105fcb7e4 | -21.06476 | -47.24837 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdbbca52-3c65-36ee-8a87-40a0be8f58a1 | -21.06343 | -47.22692 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48041d42-e3bf-3b15-8121-7a6d159a6c33 | -21.06295 | -47.23163 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 274cdbc6-96d6-3999-89f2-478784e1e33e | -21.06145 | -47.24664 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77adaa7f-51f6-35ae-bb68-30283115e120 | -21.06111 | -47.24997 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2136f608-eca5-34ae-9adc-ceb49f991f12 | -21.06096 | -47.2287 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 647fd8ed-772f-338b-84a6-ced98cab2073 | -21.0605 | -47.23359 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4182586-544e-3999-b57b-202dfcea5855 | -21.05944 | -47.24496 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 228a5fca-c9a7-36dc-9e77-d70e72156eef | -21.05912 | -47.24834 | 2024-10-08 04:59:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee302aa6-d6c6-3b74-9ad9-d9bfd3208f46 | -21.05791 | -47.22562 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a73511-4416-3443-a79e-8ad04c690c8f | -21.05745 | -47.23019 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 906470ad-683b-32e3-9b69-06c41e00ae51 | -20.4016 | -48.80746 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58ca3de0-bb58-36a0-b591-6f6d0e0c051e | -17.51627 | -49.07323 | 2024-10-08 04:59:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc69c7d-5cc1-32cf-8555-97ca6a1a41ea | -17.51151 | -49.0728 | 2024-10-08 04:59:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 400fc293-eb0b-35c6-b5a4-77265cb31e86 | -18.16815 | -48.52289 | 2024-10-08 04:59:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ac78162-954b-3b82-9553-8e0d1b6737b5 | -18.16783 | -48.52267 | 2024-10-08 04:59:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55fa6d2c-2fe2-35b6-8daa-297fea913cba | -18.1672 | -48.52803 | 2024-10-08 04:59:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 252652eb-88ba-3802-b881-3ff20d333810 | -18.19171 | -48.14096 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0152e53-9b8b-34a7-a654-d6507883fc31 | -18.19138 | -48.14389 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f116021-cec3-3eba-a7a7-0cb41e1b2e96 | -18.18693 | -48.13771 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c91e6b9-e146-37e0-8d0d-97a5a62c6c35 | -18.1866 | -48.14062 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d8e4f9c-7bf2-340b-9e9b-f6ced70eb65c | -18.18626 | -48.14355 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec48863-bf60-3bc2-a509-73cc0446520b | -18.18152 | -48.13996 | 2024-10-08 04:59:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb7cb81b-86ea-3bc9-a01d-696439d99487 | -20.87174 | -48.46578 | 2024-10-08 04:59:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bda0784-c153-3838-bacc-c2076a363d78 | -20.86659 | -48.46516 | 2024-10-08 04:59:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49ac8405-2cc3-30a2-b27e-664c3ce5943d | -20.57639 | -48.49593 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdaa983a-974d-3497-955d-97339c5f9e0a | -20.42096 | -48.8161 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1809146-d74d-3e05-b843-420b706b20a3 | -20.4166 | -48.80946 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6698177-91e9-3cd8-b669-613f12020636 | -20.41596 | -48.81542 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4aae0fa2-eb35-3c62-8e06-933a6c69aff1 | -20.41532 | -48.82137 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3a2f1cac-9f18-3a2a-a45d-93cb335cf6d0 | -20.41096 | -48.81476 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 406cdc20-9456-37fe-ae5f-a730310fc0f5 | -20.41032 | -48.82071 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1787a4f8-3245-3068-9134-9f50871ad42f | -20.40968 | -48.82665 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 602d8587-e79b-3318-93fb-51990bf7ccb7 | -20.40904 | -48.83265 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 305ad05c-0b02-3e61-abe9-912893ac0fd6 | -20.40596 | -48.8141 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bb230532-5cb6-3939-967f-fb1df1bf2686 | -20.40531 | -48.82014 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01b7ee7b-4a32-35e3-ad79-8364684fd228 | -20.40468 | -48.82606 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f280bd06-47e5-3d45-ad74-d3dd6ae45c74 | -20.40404 | -48.83198 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 00eb7a29-d90f-3e1a-b198-3b83a1e677f7 | -20.40341 | -48.83793 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 148a6155-16f9-3876-8180-9af13acf32c7 | -20.40277 | -48.84388 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 0596168c-30b3-384c-8d19-2346b849f902 | -20.40096 | -48.81341 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1110b8b0-e454-33de-a5b2-693f39cf71b5 | -20.40031 | -48.81947 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 30c772a1-d16f-3f6c-bb85-fdc145f14d55 | -20.39967 | -48.82548 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6aaceddf-63eb-3b5c-8cd0-9fee1a5fc259 | -20.39903 | -48.83146 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c9cc6ff0-fd68-3acf-b2a9-ce38c7506472 | -20.3984 | -48.83739 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a6c1e2ad-607e-3522-8740-d969e024e32e | -20.39777 | -48.84323 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b5ffdc28-5a53-302c-babb-e8af94251564 | -20.39722 | -48.80088 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94700f30-158a-3e4e-931b-c72f1db2600a | -20.39714 | -48.84913 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 04e6a7d2-f4e9-3c41-ac15-c48f173fcc18 | -20.39659 | -48.80682 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fd51b6f-bf32-33fe-8886-40a1f66b74b4 | -20.39596 | -48.81271 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6fb74e13-e3f6-3967-843a-c2f4a91cb8cb | -20.39532 | -48.81876 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fb83c3bd-05f8-3cc0-8a7d-aae60bb15f6f | -20.39467 | -48.82483 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0ede91b1-bec6-3e44-83cd-f727e106fcb4 | -20.3934 | -48.83675 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a65985f-9f39-34ce-b456-acb89107f524 | -20.39278 | -48.84258 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28af91b9-6df5-3f5d-941f-6e90e3d4d98f | -20.39222 | -48.80016 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b46639ed-8553-38a8-9344-3f74c6e10d01 | -20.39215 | -48.84848 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8594f789-f109-3d83-b961-2bd3690aec45 | -20.39033 | -48.81801 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 58f2473c-9f04-3246-9c3b-9d4f1f55e0f3 | -20.38969 | -48.82403 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c7c5793f-53c0-3189-bfef-f490796e907d | -20.38905 | -48.83003 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 11e059bf-3229-3609-b710-c9a3a22a3436 | -20.38842 | -48.83599 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7bb5bfc-f741-3ce3-a686-16e18ac388fb | -20.38779 | -48.84191 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8865a061-2405-3635-9215-bedce0a95230 | -20.38716 | -48.84787 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7f5e9501-3687-3b25-822d-734623d3d5ee | -20.38659 | -48.8054 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0589f8d4-79d1-33ca-98cc-8dd769b9d877 | -20.45102 | -48.81953 | 2024-10-08 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |


[Clique aqui para ver as próximas entradas](README93.md)
