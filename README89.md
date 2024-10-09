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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1fafbb3-d199-3f31-a2d0-a854e25c2b66 | -20.36729 | -47.98513 | 2024-10-09 04:17:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e083642d-781c-3ac3-b40c-80ca7bdf9d79 | -20.30832 | -47.79721 | 2024-10-09 04:17:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ef87fff-b636-3877-8ae4-bd862f0509fd | -20.23724 | -47.46967 | 2024-10-09 04:17:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb76a7b7-eb25-3dd7-965b-1dd5a5ebcc2a | -20.2333 | -47.47279 | 2024-10-09 04:17:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a87e5a6-7f6a-380f-98a4-25a8d9dc4091 | -20.22906 | -47.33018 | 2024-10-09 04:17:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0445f3fe-188c-3a71-b319-db48f1d29023 | -19.62686 | -47.40652 | 2024-10-09 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a325972a-8393-30a1-8984-0abdaca7fc21 | -19.62353 | -47.4059 | 2024-10-09 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c668c64-6cfd-3165-9963-e90bfc0e801f | -19.62106 | -47.42088 | 2024-10-09 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfa9b8d4-9feb-35e8-8698-aa2d67f8a7c9 | -19.61834 | -47.4165 | 2024-10-09 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8046066c-d44d-3ef4-8644-9657da15b940 | -19.74945 | -46.65034 | 2024-10-09 04:17:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bc79183-18c3-3c50-9f28-aa49fecaafc6 | -19.64485 | -46.85743 | 2024-10-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45d05433-c6da-34ed-9034-2d23ffc4ae10 | -19.64095 | -46.86049 | 2024-10-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f2007ff-379f-3894-910e-5e105c657b33 | -20.44747 | -46.75474 | 2024-10-09 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a26c72e5-1823-3745-a22b-6861f9a3febe | -19.93125 | -46.89666 | 2024-10-09 04:17:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a41da82-5947-3e1c-91be-a7503ff28fbc | -19.64426 | -46.86109 | 2024-10-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13c69b53-ecdd-39b7-ab2f-d2ac2a318cc7 | -20.67983 | -47.17473 | 2024-10-09 04:17:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bb2f645-f877-36ca-b1d1-33af4e1a1b09 | -20.67923 | -47.17844 | 2024-10-09 04:17:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcf72219-a9d6-3887-9f11-0aa8f15c77a5 | -20.44805 | -46.75108 | 2024-10-09 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ec4face-14df-3d53-b8e4-e5e8479878fc | -20.98559 | -47.15728 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5826d796-ebf1-34f8-ae1b-cce8c09ccd22 | -20.98499 | -47.161 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce675997-8835-3fc7-8935-154a05f55b66 | -20.8026 | -47.21564 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9082c84a-43b6-3482-ab31-114d849024b7 | -20.80202 | -47.2193 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e08dd030-79a1-3905-8575-3e485dd7c064 | -20.80107 | -47.20396 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0c5f8c8-6cb8-3001-adfa-521929412d2b | -20.80048 | -47.20765 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39de06c1-6543-3f5e-8b4d-d037e6e957a8 | -20.79988 | -47.21134 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e016f6d-9d49-39d9-86a0-34e9c6d4c923 | -20.79929 | -47.21501 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31c482a3-0f88-3eb4-8e2e-bf44010c6c56 | -20.7987 | -47.21867 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e5d299-f9a9-3a93-ba24-7ba5dae9528d | -20.79776 | -47.20333 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4c9d5ac2-2e9d-373f-900d-f3f1fa9d9a92 | -20.79717 | -47.207 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21bc1352-fcd6-3556-a2cc-7060a4e05ec7 | -20.79658 | -47.2107 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c95473ca-e22c-3963-97a6-56538cb9596d | -20.79598 | -47.21438 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c14172f0-01ca-3961-954f-067f56c1717f | -20.79386 | -47.2064 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ec4cd49-88ff-3d2f-9b02-b6884b385aaf | -20.79326 | -47.21009 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5544361c-a05c-3172-87a0-04ec56f45c3e | -20.79231 | -47.19479 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f18ec1da-1dce-30dd-9817-dcd2c361de39 | -20.79147 | -47.2212 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f58fee3-ee22-31ab-85ee-239a9f2d2b63 | -20.78995 | -47.2095 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d0b691-18d2-32c1-a730-a39ffea1b7e1 | -20.78935 | -47.21319 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cf71a47-0bff-3482-850e-050ddefc190c | -20.789 | -47.19419 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d1d30cac-4f08-3e8e-80df-26a97263a6c1 | -20.78875 | -47.21691 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cec11fc8-aff1-31b7-998e-d1b07451dca1 | -20.78603 | -47.21261 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb4bf656-0689-3c46-895c-c74955499543 | -20.78543 | -47.21633 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9863c7d-ff7d-3aeb-9e48-72370dba3f48 | -20.78271 | -47.21203 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 69a2e564-7182-3257-8b64-d82fc9ab9434 | -20.77939 | -47.21146 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc4c123b-1ec1-3f87-b3f8-5cce1606833e | -20.77727 | -47.20347 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af3eae16-1c99-3224-b8dd-e9149cd2c428 | -20.77667 | -47.20716 | 2024-10-09 04:17:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a015ece-cd23-350a-bd71-b9e7177e0bbb | -21.58242 | -47.90935 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1af95220-ef26-34fd-96ae-8644b1e54dad | -21.58032 | -47.90114 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71eb7872-03a4-3ff1-be46-7fa268b6f007 | -21.58008 | -47.88157 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3183b4bb-000d-3a2e-8b1c-7e7e74991605 | -21.5797 | -47.90493 | 2024-10-09 04:17:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dca59ee-5152-37d9-a05e-50765079b4fd | -21.57884 | -47.88914 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a27eb111-97b8-38d9-8ac7-36b5c61369e8 | -21.57612 | -47.88472 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ed04f59-ab3c-3a71-b3f6-bfe1fd7c8bb1 | -21.57574 | -47.90808 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd0d3ba6-032b-3a71-a6a1-470e20b64e8d | -21.57302 | -47.90366 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f99a7094-db59-39ca-bf18-3213457eb9a9 | -22.20864 | -48.12189 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a44d55-efee-3b56-800d-b6de0caef52e | -22.20824 | -48.14536 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ffe1156-cba4-3158-82ce-5eb4b2144e51 | -22.20489 | -48.14471 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f539e024-b56d-3a89-b02f-06cb634fba46 | -22.20258 | -48.11679 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40a0d81e-b599-3337-a23d-aaa8cd360e22 | -22.20155 | -48.14409 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 986f0639-c294-3531-bd62-d1202882f946 | -22.20092 | -48.14791 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9456110e-7da3-3b8b-8c83-f5d82af80e1e | -22.19986 | -48.11232 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe62bfbd-8a98-32cb-b916-c63ac8007846 | -22.19568 | -48.15879 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 504bda09-78dc-323c-8cda-a26dc2d334c2 | -22.19296 | -48.15432 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dbf9c4c1-114d-3c69-9ff5-fe1c756f35b5 | -22.19233 | -48.15815 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dab5a1c9-1ef7-350a-8778-745c844a8428 | -22.1917 | -48.16198 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ef93f7b-a60e-3f7a-80b9-8be4cb875ce3 | -22.18962 | -48.15368 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc3cb378-38bc-33ad-922e-307cbb96f6f4 | -22.18898 | -48.15751 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 423e5129-433a-307f-b146-a74a2f3a290c | -22.18835 | -48.16134 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f8cb921-34cf-3535-bb51-272f2ce01256 | -22.18607 | -48.13326 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab40d213-32e2-391a-85c3-8633ceba66cb | -22.18503 | -48.09764 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce58b53b-e10c-3eca-8425-fa0f6214789b | -22.18501 | -48.16069 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb8fcaf-d54f-389d-96a1-97239a406677 | -22.18438 | -48.16453 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fbe4dac-e324-33a2-9650-a2fb90c82fe6 | -22.18375 | -48.16836 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11a417ad-e87c-3720-8626-ffc5c9b305eb | -22.1823 | -48.15621 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38ca2b81-5551-3f87-aa02-5ad4b42b5494 | -22.18166 | -48.16004 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3bd38e9-209f-3bce-9f4a-90b46bbba4da | -22.18103 | -48.16388 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77e4e5d-5051-3533-a1a3-6a29d82701a1 | -22.1804 | -48.16771 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fecce5a5-f187-300c-8411-c91af96cb8e4 | -22.17832 | -48.15939 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 817d6334-2134-3f59-be2d-94e4ec33d54a | -22.17768 | -48.16322 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1a7fe63-5b30-35d2-a8fc-dc616f8fb3c4 | -22.17705 | -48.16706 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82f27ed6-8699-32d2-af43-4a8f0bd9a62f | -22.17562 | -48.09197 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2698dc88-1436-3241-a18b-697855908029 | -22.17437 | -48.09959 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22b990ea-1851-3cc7-9188-164b1027aef4 | -22.17371 | -48.16642 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0627947-3601-3c6c-813a-4bb892bf3cde | -22.17228 | -48.09136 | 2024-10-09 04:17:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50b2fbb2-1159-30a2-96da-3ec17d6561f9 | -22.17102 | -48.09896 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a792ae30-0889-3761-85cd-3c99efe24968 | -22.16725 | -48.12183 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14db0040-0441-33bc-9480-4b73a9fd274b | -22.16662 | -48.12566 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd0d0756-b144-3c06-8779-f0b95780ecc7 | -22.16559 | -48.0901 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f48a9752-51a8-3019-afe3-9e9207047596 | -22.16224 | -48.08947 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8705ad80-1a8d-3b1e-92fa-4b13a2cc0701 | -22.1589 | -48.08883 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 658b3ee3-7695-3be7-b79b-c3c99ee01cf9 | -22.15722 | -48.11992 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 174636dd-87c9-3f33-9e47-762ee5e75f67 | -22.15659 | -48.12374 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 703b09cf-9108-36b0-8c74-bb088c925ef7 | -22.15619 | -48.08439 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b2da9f9-b45d-330e-a801-f80c7c07c864 | -22.15595 | -48.12756 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c23d6f5e-741b-37bd-b75c-83d362d4d239 | -22.15556 | -48.08818 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac4885d0-8b6f-36c2-9602-30694571e322 | -22.15513 | -48.11164 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 248a656a-45c2-3a3d-a18d-9d12a2b0b0e3 | -22.15324 | -48.1231 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 440769e5-81f0-3529-99d6-8d9913ac9b70 | -22.15261 | -48.12693 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4365f8fc-dd35-3700-b577-26877bd4b51d | -22.15222 | -48.08753 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75cf38c7-94d4-3c25-adb2-ec70c3d0b021 | -22.15197 | -48.13076 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40570b26-37bf-3399-8f6f-c1a7e84513e6 | -22.15178 | -48.11102 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
