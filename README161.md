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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8994fbaf-06f3-3340-ba95-8f70409d370a | -5.08876 | -39.76727 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 202.0 |
| e3e5842f-0c9e-3e54-b08d-04c7a73961d0 | -5.08806 | -39.86974 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 13b584b4-2010-3c89-a539-fd9436c26c16 | -5.08798 | -39.76277 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 202.0 |
| a4b6b6ec-dd79-3e5a-ad85-c415a1793052 | -5.08734 | -39.86563 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| fe14b12d-be5f-3527-8f4e-64b9ff185966 | -5.08722 | -39.75837 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 0aff1e8a-0ca5-3ae8-bdbf-08f397193037 | -6.30185 | -39.90873 | 2024-10-25 16:52:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 41.8 |
| fad46f80-1c9e-34ad-8357-8f96dc0b4e8d | -6.20173 | -38.88101 | 2024-10-25 16:52:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 5feed92b-6c10-3ed7-9df3-0d9f1c7e285e | -4.99235 | -40.14629 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 10ab901c-a9c3-3194-a296-fe912d9d5ee7 | -5.02554 | -39.91652 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0e936306-2209-3d73-81f6-e369d7323820 | -5.02283 | -39.9177 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 47e207b8-c21a-33a3-bb43-a3e45f8f7756 | -5.02201 | -39.91317 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 10920a66-8d3f-3d11-bd71-e77295e40d12 | -5.02035 | -39.92204 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 6e759554-dbf1-3fca-a87c-42f7d57fba6b | -5.01957 | -39.91749 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 79.3 |
| fb781665-9d5d-3d6a-aeb3-eee17bf0100b | -7.99057 | -39.74999 | 2024-10-25 16:52:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 6f6ecbbf-d81e-3a73-a14e-ed6ea27d59c8 | -7.68389 | -40.5402 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c7a3cb03-2dbf-3339-8f02-6a8eb0ca6891 | -7.67843 | -40.54126 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5617d3dd-c487-3277-8b86-a8928a5d761c | -7.63603 | -40.61842 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df16801a-d10d-3a3a-a5f2-24e0c02c2c79 | -7.63485 | -40.61738 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cfbfea23-4b61-30d0-9abe-4be94f7b0533 | -7.86505 | -40.53397 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 59b9332a-d392-33e0-bc52-73c47a35eb59 | -7.72302 | -40.31586 | 2024-10-25 16:52:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 42da9893-aede-3853-863a-54e4d6d0c351 | -7.20479 | -39.25256 | 2024-10-25 16:52:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| fff35b93-689e-3792-b3b1-22c969e88639 | -7.14788 | -39.2578 | 2024-10-25 16:52:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9a0eb8c4-924a-39a3-b385-78e16d4a9933 | -7.05313 | -39.26021 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f67a2c54-ea16-3d44-8c22-f8692d7957b5 | -6.9786 | -39.19213 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fd9a8473-2727-360e-9a53-57049ee7a3ac | -6.97411 | -39.23546 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 005256d7-91da-388a-9480-286cd9c9496e | -6.97324 | -39.23073 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| bdfd3a79-c9f5-3abc-b24b-a4bdbf412fd5 | -6.97313 | -39.23951 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 9ba2871a-7a51-33f7-b0bd-e9cdb2136c9a | -6.97229 | -39.23478 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 147.6 |
| f8526273-c0c3-3ac7-9ba7-9f39db4c0b87 | -6.97144 | -39.22998 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 0ac42fcd-d8e7-31e7-97da-ac49c94f370f | -6.96904 | -39.24169 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 072c63b1-8436-3540-896a-58640689fec2 | -6.96818 | -39.237 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| a24afd9f-8717-3687-9ddf-9f948f52b48d | -6.96727 | -39.23212 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 14861d9d-99d5-396f-957b-dc8a7e361682 | -6.96716 | -39.2409 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 53.9 |
| b51af3e5-5f51-32d6-b842-1ae24e2a8376 | -6.96634 | -39.23626 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 69.6 |
| bc3a8f69-0c06-3048-81f6-c5376e2e8893 | -6.96546 | -39.23131 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 9b56dcea-5e7e-3c4b-8b92-6e64925922dc | -6.94921 | -39.26883 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4ef15079-987f-3696-8430-5b98d03ef3a9 | -6.94802 | -39.27287 | 2024-10-25 16:52:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ab0f2325-5329-3eca-a059-d6b8486c8e7e | -6.86444 | -39.05244 | 2024-10-25 16:52:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e3344748-7c40-3885-8515-3dcf5643391b | -6.60648 | -39.20075 | 2024-10-25 16:52:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e20071d6-3c13-31fa-820a-76edd6d57eb0 | -7.12637 | -40.30882 | 2024-10-25 16:52:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3e9bb916-2d31-3bcc-92d0-8f7460ec7968 | -7.10701 | -40.49052 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c13974c5-2e2a-3bdb-90f3-8da9a6e98147 | -7.77949 | -40.34328 | 2024-10-25 16:52:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e18743a4-560f-3b8b-9196-ba470c0fbc3f | -7.71814 | -40.32055 | 2024-10-25 16:52:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e20fb0c8-45cb-34d3-9a89-4c5fe9acc4b9 | -7.35041 | -40.38899 | 2024-10-25 16:52:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1710b7ab-d7a5-3ac1-95bf-d5508cac12f8 | -7.91083 | -39.93759 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cbeee1f2-d0e5-3715-b9be-672131a65a6c | -7.85709 | -39.64099 | 2024-10-25 16:52:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 19.5 |
| eb54b3e0-75df-3f81-a4ac-e5d0f2ecd92f | -7.8105 | -39.81585 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 73634f79-a1e6-3e6d-9fcc-29666374b241 | -7.80655 | -39.81865 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ac350b84-f1e1-3a71-a904-3b344f06f3ee | -7.80581 | -39.81467 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f95b9319-d1ef-30ed-abe1-32fd6de418dc | -7.8048 | -39.81701 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0fa361f9-4113-3c5a-b219-8bd87dbb7896 | -7.79715 | -40.09873 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| bae29f44-bb13-34ea-a884-8d699df9b39c | -7.76165 | -40.00043 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 20.4 |
| aef900fb-5b50-3428-8037-7993a5b3ac17 | -7.76093 | -39.99651 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 5e65a29d-7676-3ba1-8197-1f0715372c21 | -7.75922 | -40.00114 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fec3a20b-cbaf-3d4a-a8ec-761076f37bd1 | -7.759 | -40.04945 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8f8825ac-131b-33d3-ad53-cb493ca263a8 | -7.75853 | -39.99722 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 959d7f0a-9461-3880-93a0-caa01b543a47 | -7.75624 | -40.05029 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 94683424-41ce-3ee1-b02d-77234170783c | -7.75129 | -40.05524 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 65ab807c-d96c-3a19-98e5-facaeb7c6d2c | -7.74916 | -40.05931 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ae2fd8e9-6c08-3e63-9fcf-f6453e962f71 | -7.74851 | -40.03958 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| de6057d7-7fac-31ab-8138-bf03fb2b12ab | -7.74844 | -40.05539 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9edb7495-f0ec-3309-8089-7b2622bc8c84 | -7.74564 | -40.05624 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4f83b999-5701-39c0-b689-344d4bed8a3b | -7.73413 | -39.85099 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 34fb288a-5bf3-31a1-be2d-733318dc582b | -7.73274 | -39.85132 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 462d321b-8a07-3ff5-9e00-fc4e2841ff6d | -7.72369 | -40.31956 | 2024-10-25 16:52:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eb91af9c-6b30-355f-9d91-cb15e689936a | -7.67641 | -40.46687 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9a8867ff-0b02-34d6-9fe8-68952d7082c3 | -7.65967 | -39.80684 | 2024-10-25 16:52:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 304c5ced-0e90-3623-b2f2-4de1ee15ab2e | -7.60345 | -40.12522 | 2024-10-25 16:52:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 28.7 |
| e2ff27fc-7116-3922-8e94-a51ad66a0b46 | -7.58227 | -39.67733 | 2024-10-25 16:52:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0c8aa286-8385-36cc-935f-9be661451fb1 | -7.58222 | -39.6777 | 2024-10-25 16:52:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7b2df0f7-6d94-3c99-b0aa-73695a9caf96 | -7.58165 | -39.97231 | 2024-10-25 16:52:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 809ee165-3aa6-3823-a5f2-fe2d78c375d6 | -7.57203 | -39.82063 | 2024-10-25 16:52:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 4a4e8e34-f67d-3bcb-875f-a75a9580ed58 | -7.34483 | -40.38987 | 2024-10-25 16:52:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 325779ef-caf4-314f-a328-aa916a9b652a | -7.23251 | -40.02451 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 161.1 |
| e24404a9-4f36-3b01-9c09-2a275d36083c | -7.23178 | -40.02051 | 2024-10-25 16:52:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 842aa7ab-b281-3a13-8880-633191f5737a | -7.08799 | -39.79059 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a53cafb0-8400-3832-b149-d9763ea89c46 | -7.07242 | -40.45183 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ae696e8a-60b1-37a9-a97c-afeb92a6a9cc | -6.91569 | -39.89708 | 2024-10-25 16:52:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 72515739-be46-346a-9a45-7afa1f1053ed | -6.89961 | -39.77424 | 2024-10-25 16:52:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4856c2b9-78f9-32cf-892c-b11efb109988 | -6.76348 | -39.84724 | 2024-10-25 16:52:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ea56601b-57ab-30e5-9214-d9cf33251cf2 | -6.76282 | -39.84552 | 2024-10-25 16:52:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 8455c9e2-1774-3bf6-8e25-dbf5dc27c208 | -6.75763 | -39.84805 | 2024-10-25 16:52:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2da995e0-a383-35d0-941a-9ab2eeed3280 | -7.16151 | -40.50761 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 430da02c-9082-373c-adca-4f2d014a64aa | -7.16088 | -40.50403 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 489e8ca9-2b23-3010-8c3f-7f827c0ed928 | -7.11193 | -40.48602 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 8026f554-3536-3306-a05b-8af6f223eaa1 | -7.07187 | -40.45477 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9a523125-1c63-37c3-976c-43e4633f008f | -8.21213 | -40.31643 | 2024-10-25 16:52:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ef82b95a-d4d3-326d-a47e-b6c7b6de0416 | -7.9834 | -40.34016 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 98c292ac-0c5f-36c4-a2e4-9e09c198fcbe | -8.07459 | -40.0869 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e52688e6-3dca-3793-8cae-464b6c55f4fe | -8.07326 | -40.09024 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3d521545-88be-3e99-ab76-9aa41f32b7af | -8.07257 | -40.08649 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b0336cf9-afb5-3bd3-887e-f18ae9e27a50 | -8.06896 | -40.08776 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1f9e6e97-eae7-30fa-b975-6ec31645fa22 | -8.05239 | -39.3299 | 2024-10-25 16:52:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 06d80483-95bd-354a-bf55-9507d19ffbe6 | -8.01509 | -39.88546 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 42647a7e-0f9c-3ff5-8a00-8df97eb746d0 | -8.01436 | -39.88147 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 54.4 |
| c19f6042-ad50-3b6a-9f1a-79c36dbc2e83 | -7.99273 | -39.76191 | 2024-10-25 16:52:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 1a1ad483-2167-3390-81c2-81494768b8ec | -7.99201 | -39.75794 | 2024-10-25 16:52:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 15ce835d-d5e8-34e6-843f-639d29f8f4b5 | -7.99129 | -39.75396 | 2024-10-25 16:52:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 9ac29f74-ae00-3bd8-8f62-a848c81d828b | -7.96184 | -40.37841 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b5baec18-1ca1-31d7-b8b5-b74308f7fd7e | -7.9579 | -40.48123 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README162.md)
