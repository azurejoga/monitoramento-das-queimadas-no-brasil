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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1249d06f-98c0-39ed-b9ca-3bb24573c4e4 | -4.11457 | -50.05314 | 2025-10-09 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9827ef6c-456e-35ff-9649-146968b2ea35 | -5.14574 | -56.07457 | 2025-10-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e35dacba-522e-3d47-b7d9-6b1a0e1fff80 | -6.69056 | -46.3089 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f98a1712-73b9-3185-a622-d80cf217e083 | -3.09804 | -47.01732 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f29baefb-87e2-3fc6-b348-20e1f84088a3 | -5.46156 | -43.51093 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 830c8596-766d-399a-a50f-9312ec44157b | -3.10302 | -47.02183 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59fd19a2-af0b-3eb8-94c0-0c5ff73ad215 | -6.6982 | -46.30624 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4ba49a27-5196-3f50-8ee5-5031070c22a3 | -5.72011 | -44.82242 | 2025-10-09 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7aa3cb6-d594-3587-8353-725195075bb7 | -3.47379 | -50.02472 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31b89157-5455-3c47-aeb0-71654d2239e2 | -4.5014 | -46.35537 | 2025-10-09 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f383c7a-c0b1-3631-b06d-064c301b1f40 | -5.31097 | -45.37499 | 2025-10-09 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1807a94e-affb-3025-a3ae-987328c4250e | -6.62329 | -62.87538 | 2025-10-09 05:10:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c1e85c3-d552-307f-8d8a-c9a345a398bd | -3.9595 | -49.89145 | 2025-10-09 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca8f96c-8380-35c3-b69a-111705c6691c | -7.20595 | -45.91642 | 2025-10-09 05:10:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0f95a68-f4d7-3495-acfe-84b0232c78b4 | -5.31387 | -45.37553 | 2025-10-09 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6df87efb-f5d1-3088-9d71-cbca63d5c684 | -3.47196 | -49.26459 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14bff61c-3ffa-398c-ab51-845708445329 | -7.57171 | -49.65325 | 2025-10-09 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f827129-1fb6-303f-b80d-49e86910856b | -2.18936 | -54.47228 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08d236c9-4e37-3764-ae5d-c5588f887191 | -7.78535 | -44.18649 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 432067fa-9c38-3f5c-98e1-816b37e83ddf | -7.76295 | -44.03712 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6a4fb9a7-2d91-3259-a0ba-096e1852ab19 | -3.11198 | -47.80043 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 212ee275-638c-3888-960a-702441c7c6e6 | -3.39271 | -50.13633 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09083cd7-985d-36eb-bece-be8ce96615fa | -3.53915 | -48.91933 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a12738db-337b-38b1-90d6-ab2ce06c8931 | -3.69762 | -49.56548 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2de3ada2-4a71-3b28-9355-8d2fb1900003 | -4.77151 | -45.59699 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdd460d3-b917-358a-8dae-f7481ff8499c | -3.5927 | -49.34897 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0e6b167d-3f05-367e-9550-5f14e095ff0e | -3.84037 | -49.26228 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eb8a875-0954-36c9-abd3-a3c23f1dd170 | -6.69336 | -46.29588 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0938637e-e077-31fb-af68-a5733d021cc7 | -5.153 | -46.10157 | 2025-10-09 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5db7a81d-27b9-3d47-95e2-af69ae4934ab | -3.11292 | -47.79404 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15ec9745-7deb-3f5d-967c-d7baf865668d | -4.21708 | -48.36437 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e75eaacd-e188-3052-b9e4-b58579920af2 | -7.77932 | -44.24744 | 2025-10-09 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 493b0688-921c-33cd-b783-a8103c59e5bf | -4.25861 | -48.56812 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a7e1845-48ec-3d69-9a31-a55bd9749c9a | -5.64553 | -43.60684 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae82b80d-adcc-3aec-a79f-97b05dc2cb7e | -7.80449 | -44.20481 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c05e591b-2ed4-3612-9ead-d8c6662ad98a | -5.15417 | -46.09313 | 2025-10-09 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c2994c3-1196-3dde-9c36-3b17bd7497aa | -4.2757 | -48.88233 | 2025-10-09 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5e230be-6b7d-3bce-a6fc-e839ed3c0728 | -5.12305 | -49.95074 | 2025-10-09 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c66873d-163a-394b-8cce-ed363b869782 | -4.1131 | -50.05499 | 2025-10-09 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74e9472d-f66b-3309-9380-85ad6572fc7e | -2.16488 | -54.47227 | 2025-10-09 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a55a30a-8ea7-3b39-ab28-06ad89fff67f | -4.30861 | -48.06928 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5b970b7-4908-33dd-b044-5e760f6e10f5 | -5.45759 | -43.50658 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1ed9797-108e-3b9a-84f9-46e07dc71157 | -2.78761 | -49.59402 | 2025-10-09 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1549b814-eb30-3249-9e45-55ef47ec54cd | -2.18993 | -54.46857 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9c2b5da-bae2-3fe4-ba23-bb41a4c1ec7b | -5.45668 | -43.51321 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32e4313f-09c1-384e-9801-d8110eb751a2 | -6.69185 | -46.29955 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0dc4e6d9-5f25-320f-b261-02002588257d | -4.22175 | -48.36818 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d193d43f-96b1-3c18-a91e-9d15a5fc0f6e | -5.71351 | -44.82171 | 2025-10-09 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d68a0cb-7947-33ce-8739-c09380418a3c | -4.30338 | -48.06853 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c702716-a0e5-378c-a4f3-b231c3bd2d39 | -3.58723 | -49.35329 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 59c84e77-320e-3e30-a333-73a857430db8 | -5.13192 | -46.25391 | 2025-10-09 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4776e494-4d51-315c-9c8e-a10e75929e0e | -3.59195 | -49.35413 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bd021fea-d45e-3e0c-8838-cb6616886f32 | -5.15358 | -46.09735 | 2025-10-09 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6cfb86d-d06f-3259-aab8-2655efa22f09 | -6.46162 | -44.57634 | 2025-10-09 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7723656d-1523-3aa7-b61d-5daf21199f07 | -2.78735 | -49.5972 | 2025-10-09 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc331b44-9e6c-3781-874f-c3f7e1a36c70 | -2.8848 | -50.72932 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f78f8343-3dd3-3564-a6db-fd017cd50988 | -7.76997 | -44.0384 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 505844b9-f224-36c4-a687-0991806cbc18 | -3.38742 | -50.17205 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bac634fb-dd82-3ca6-9157-b35fc3f93b82 | -6.68666 | -46.29977 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c3235b2-f7e3-3ff0-94fc-0af02bdce104 | -7.45466 | -47.17495 | 2025-10-09 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a8df608-e585-396e-97b5-bf43dbb4ad65 | -6.69727 | -46.30514 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03f86825-422d-316b-af0d-428ef19c42ae | -7.76917 | -44.04483 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6a930013-3247-38b1-aa43-76ac623f0a8f | -4.82218 | -47.34168 | 2025-10-09 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86bfb6e0-d450-3f79-82f2-a0be59f8ab3f | -4.51352 | -49.24828 | 2025-10-09 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0939dd2-5831-3afe-9a77-d0b2f15c4ab0 | -2.17171 | -54.47335 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b6ceaec-da0e-3270-9770-8b8e43fbbcdf | -6.69151 | -46.31001 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 17de4021-2c81-3e27-bd06-020b5561380e | -5.63848 | -43.60577 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c0b5b12-2e42-3ec2-8fa7-2411bdbca71a | -5.44712 | -44.82567 | 2025-10-09 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0235dfbc-8908-3ef8-bc79-716435bc2caa | -4.22606 | -50.15676 | 2025-10-09 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 375c0dae-5e7d-3521-bcd4-f7993613fee3 | -4.2256 | -47.78246 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b4cc944-0d2b-3d30-a741-285147527e95 | -2.89757 | -48.07659 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2d1766d-256e-32f3-bc02-ad9980f1f4ea | -10.19707 | -44.55745 | 2025-10-09 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba417709-bf2a-3153-a3e6-a71115f929b3 | -4.25902 | -48.56522 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 634f8b60-cf1b-31fb-8120-8e5d252fc411 | -2.90064 | -48.0765 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69723092-f665-386c-9069-515e8ceb2209 | -4.23042 | -47.78685 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b13b8cdc-9c9c-313b-a324-2a8158ae6062 | -3.69689 | -49.5704 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ff736e75-42f2-31cb-84fa-9d2c066e9b04 | -4.25561 | -48.553 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbbcfc8c-db55-31a4-bc17-eec05fe1da62 | -7.80013 | -44.19592 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3354296-531a-3d46-82e7-6b045a75d0a1 | -3.09751 | -47.02095 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9578159-98d4-3f69-a726-a5fb1d82025f | -6.92977 | -44.50996 | 2025-10-09 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c916576d-0e86-3639-b267-3d6418d86b80 | -5.13726 | -46.25932 | 2025-10-09 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10dd942d-5a97-3611-83af-401ef588580c | -7.77702 | -44.03952 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b11a7465-1331-3d56-aa16-293187dd5bc2 | -7.4599 | -47.18004 | 2025-10-09 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1575a13-bcf6-3426-a001-005e81bab4ec | -4.03586 | -49.49955 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6060d200-2f5e-31c4-a096-54c0019842a8 | -6.92905 | -44.51566 | 2025-10-09 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b94b6d18-b010-3218-829f-ffb3e75045b9 | -4.30814 | -48.0696 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d40faf42-92a5-325d-a212-f28717a34b4b | -6.69662 | -46.30984 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4564188-c046-366a-ac70-72a931837041 | -6.79057 | -50.48776 | 2025-10-09 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4ee0691-c45a-3973-82de-76f80cfaa800 | -2.3778 | -47.71212 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c90fc32-c932-38fa-abbf-5d9b7c456a21 | -4.81409 | -46.82148 | 2025-10-09 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d1dc1a-6a48-3c3f-9ba3-4226a869e70a | -5.45447 | -43.51 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a98783d4-7bc0-3023-a8af-d5bb2bc59257 | -5.31318 | -45.38064 | 2025-10-09 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72789d2c-7b3f-33f1-aa84-63ce6b9e8112 | -4.68776 | -45.83703 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b714fee7-c1c6-3c11-8f14-47283b35da5c | -5.65481 | -43.60782 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b1ec829-9b54-3ae3-9e33-da25497ccf0d | -4.72961 | -43.35422 | 2025-10-09 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e738acc5-55a2-3be5-907a-8cc75d76f40c | -3.47153 | -50.02253 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce5974ca-beea-3929-88c8-93b9e71e4148 | -4.2268 | -47.78387 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 20dd178a-5132-3ad9-a27a-339abdb5a042 | -2.37827 | -47.70897 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62400221-7bba-3b66-a95b-c81112ac4c7f | -4.25396 | -48.56454 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd868c8b-31a4-3481-b6b3-e43301bce348 | -3.58797 | -49.34815 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README53.md)
