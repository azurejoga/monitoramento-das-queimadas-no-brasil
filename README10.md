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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46522aaf-e3d8-3eff-be28-944d77e756c7 | -4.85304 | -42.93197 | 2026-09-29 03:30:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aec9c07-b045-32c2-b8f7-d1c88ca6e805 | -5.85031 | -35.30496 | 2026-09-29 03:30:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9ad31c26-0bec-3997-917d-5b0a288c4518 | -4.31997 | -38.73619 | 2026-09-29 03:30:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bd38bcc1-79e9-3629-bf56-fd13d77f6bce | -7.67698 | -44.89863 | 2026-09-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ccbafc9-28ea-34f9-b5ec-9239a88d78b4 | -7.99277 | -43.26413 | 2026-09-29 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 89b0d9f3-11c5-3fbc-b4db-8ccf88dc7ff9 | -6.28325 | -43.64095 | 2026-09-29 03:30:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cf7bafb-6411-3ecc-9258-5f8853ae64ac | -5.42792 | -43.45279 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d4f90f4-6796-3396-afcd-47979b42439e | -6.19209 | -35.25039 | 2026-09-29 03:30:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 15a16a9c-43d1-33ae-b248-742e4a63bcbd | -5.41998 | -43.45794 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc5d2c4c-310b-3002-a927-e35fe8b31798 | -5.36021 | -36.85128 | 2026-09-29 03:30:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ae50823-2d93-3429-8232-81e76dc918b8 | -4.85649 | -42.93327 | 2026-09-29 03:30:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb588e42-59d9-36d4-956e-7934b0f0edc6 | -13.37188 | -44.01283 | 2026-09-29 03:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66d1e812-4924-3c55-9d2a-9fa8e507581f | -15.21947 | -46.16914 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee207ee0-c875-349c-993f-3b865450c683 | -14.4898 | -43.26702 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6b700f2-9496-32f9-a0ba-19419e6881a8 | -11.42016 | -43.44077 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a332da89-d925-349b-aa15-1e04a0513205 | -11.17233 | -44.79524 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c63c4b3c-369e-35b0-91d5-87421c7106d1 | -11.40142 | -43.44475 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d84cc2f-ff61-32f8-9555-cf5204850a0d | -11.19004 | -45.13715 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ee1a309c-d0b4-3438-8932-87294589a970 | -15.241 | -43.26893 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 58c53650-1783-3ba2-ad70-d5dfa8b55067 | -11.43564 | -43.45918 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a4241419-21c2-36df-b984-b8b79e9a8bce | -14.48493 | -43.2615 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 30095c0c-ecd4-361e-9dba-9b3fc6e6c89e | -11.41403 | -43.43941 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cfac5a32-beb0-3b1f-8260-e07fa312d08b | -15.46343 | -46.13702 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05b5159f-e1d9-3db9-8bff-c8681dd9559a | -11.42785 | -43.44063 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4e2aee16-2f09-3f03-9f6f-3d3903bb1393 | -11.4285 | -43.46272 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e59072de-42a6-3aa9-8b91-be47de3f22ac | -14.44873 | -40.75016 | 2026-09-29 03:32:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1416aa49-7b3b-3812-a2a2-877fb945f579 | -11.43444 | -43.47233 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 983f9ec2-3ef5-353f-948b-d0815ce4234e | -15.2183 | -46.17441 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58a62150-db05-3775-8144-a1ed5dd06f7a | -12.00617 | -44.93218 | 2026-09-29 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6973dd2-6132-3fcc-b0b0-d9ce3a765f0a | -10.28204 | -44.64446 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e061311-8ee1-3c79-9333-044f9263b034 | -11.1735 | -44.78937 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b2e61bef-8554-3e26-aaa5-56bb86861f3c | -11.99955 | -44.93067 | 2026-09-29 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d25aa11f-24da-3f7c-a7e1-a37221bf591e | -15.82876 | -42.5633 | 2026-09-29 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 760bbaae-de5a-3e2c-9aff-25ac9d1ae992 | -11.45113 | -43.47771 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b09fc868-1a83-3a76-ad7d-bf1ca6e31487 | -11.44498 | -43.4764 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 078b629e-5193-393a-be91-71a90083c6f8 | -11.42266 | -43.43446 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 52e469ba-ca21-3c41-8c51-0114f86d2a41 | -11.18846 | -45.14114 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7de060bb-70cc-3873-9070-c369cf76ec2f | -11.37513 | -43.38409 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88886c94-22d7-3614-97df-4d0f03335f43 | -15.13155 | -43.62512 | 2026-09-29 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d79443ac-3c0c-3c94-bdc3-c1d2407a9da9 | -11.18029 | -45.1464 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c14d6f32-c48a-382d-8a49-e4904a7e8131 | -11.39334 | -43.45317 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ab7c03c-18ab-3e94-8d16-7cf2f6c1ce60 | -11.3988 | -43.4511 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afc689f5-977f-3777-b0f1-4514fa59c64f | -10.26856 | -44.6418 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6bfc8b7-3d08-3969-af0a-d166d9a43473 | -15.46523 | -46.14046 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17fcee80-fa81-3ccc-b343-14cfeae78d0f | -13.86324 | -44.00448 | 2026-09-29 03:32:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 577b67c8-9b73-3aba-9a9a-d6b4f8676a8f | -11.71425 | -43.46369 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04ae5de9-d0b1-39d7-800c-1cd83690dbc6 | -11.41178 | -43.45717 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5bbdcf61-3677-361a-a75f-d381a3f45f7d | -11.43539 | -43.46748 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2349615-ec58-33f4-8c49-5c0ea6d85ad3 | -13.86423 | -43.99973 | 2026-09-29 03:32:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53f1969a-04db-3d7f-a402-414b6ac62714 | -16.35505 | -42.58848 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a0e4182-18ad-3dd9-85ff-47b29e80682b | -12.31764 | -46.40914 | 2026-09-29 03:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1758a6e3-da8b-33c7-9897-fb3e33d67847 | -11.42531 | -43.4469 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1c3fda4-2693-39e2-b647-cbf75fbb5fe1 | -15.22338 | -46.18341 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 243b2895-628f-3d4c-b5be-47a372cc3603 | -11.41368 | -43.44753 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a2d2786-e28b-363b-b1b0-dfd8d21890cf | -15.64821 | -41.35648 | 2026-09-29 03:32:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c9ff8d2c-6a17-3dc1-86f2-e2365f74842d | -11.42595 | -43.4503 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18d8dca2-0388-3af9-b6e9-1f868a7b5ecd | -14.48406 | -43.26567 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6b335d43-68af-379d-b8f7-07176d73957a | -15.16837 | -46.13708 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23f14af8-cd53-3949-a5d9-dbac795431be | -11.40046 | -43.44958 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b6054d5-98f4-38c3-b501-17ca543e0f39 | -11.40427 | -43.4304 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e1463c8-4244-3c2b-aad7-4c2571d3b1ec | -11.41623 | -43.45998 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7fa31e70-bcf3-3ba0-9fa2-466f53a6b4c2 | -11.42076 | -43.44411 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4f36b8cd-ef38-3c30-a0e2-341a933176cb | -11.4079 | -43.43805 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 995ac51e-7ea5-3c79-b1d6-73ecc8088fb7 | -11.3845 | -43.40117 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18e1d8cc-22de-3c8b-b21e-7d1c3ea6463d | -11.43785 | -43.47988 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 264f028d-f998-3941-903f-7057895ec966 | -13.73519 | -43.66898 | 2026-09-29 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d1c5074-bfef-32bb-93f7-3eb673a15249 | -17.51817 | -42.12955 | 2026-09-29 03:32:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7cd736b0-90c3-31e8-a00d-9cc012263dc9 | -16.35153 | -42.59118 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf9df64-dce7-3aa2-ad53-8ee137af58ed | -11.42212 | -43.43114 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 21e45b9b-b02c-3509-8c1b-bc072bb3146b | -11.41273 | -43.45235 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48c0279a-4262-3be6-a3c7-33bb8a6837f8 | -11.18876 | -45.14325 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ca18430-8af4-38eb-ad59-9db9b568d754 | -15.24502 | -43.27834 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 74bf86a2-dccd-37be-b6ca-00a26b2c988d | -16.35435 | -42.59199 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c03280-c7d7-3e75-bab8-9a85241fae72 | -11.40756 | -43.44612 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fd186ad-84a6-314c-9177-57c75c5aaf4f | -10.27667 | -44.63635 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eeca0e02-94b3-3c3b-b04b-19c96adc0df4 | -11.41501 | -43.43462 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4abce9bd-b52b-3003-8d5f-ab8734b52b6e | -11.38029 | -43.39024 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adad73e9-1f96-3674-b8bf-e0dc6c30efe1 | -15.45515 | -46.15379 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d13295ab-a22b-3eb7-8898-dfd30d32acfd | -11.42171 | -43.4393 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 02126ded-bf56-35d8-b521-14b0bf0d41c5 | -11.39812 | -43.42909 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51d83270-5ac2-31c0-b8f2-9d5a02cda179 | -15.44816 | -46.14249 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2283ebe0-11ec-3cd3-beb2-8a6292c6ee75 | -15.47002 | -46.139 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60856b62-34b0-3fdb-a89d-79cc5f2d26f9 | -14.08177 | -46.31266 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c40c555d-bbba-3d14-ae17-603e8f342fa5 | -11.40274 | -43.43194 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78fef999-95ce-385c-a512-76275d4fb926 | -13.38051 | -41.34161 | 2026-09-29 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d36e24cb-c927-3776-95d3-863a6ba3bd5c | -11.30272 | -43.55167 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b533ae16-873a-3ee2-b32f-8cd9aa12afed | -11.42829 | -43.47098 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c022fb0b-4ba1-3a32-8a44-0165f066fbd1 | -11.40522 | -43.4256 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f911d9c-c686-3198-aaf1-95e7b2c1d61e | -12.31054 | -46.40726 | 2026-09-29 03:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f6eda55a-8738-3bba-8736-02814fcb40e1 | -11.37933 | -43.39503 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 302df86f-e9b0-3032-be74-e022bf1d6ceb | -15.24172 | -43.27295 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 2adc3734-1dd8-3195-ab8a-76791ab24dec | -11.39431 | -43.44827 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6f054d2-fe79-3788-9360-bf5ffadec4dd | -12.14078 | -45.00236 | 2026-09-29 03:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6815bf89-91ea-3653-88fd-e51b244c3b77 | -13.43662 | -43.8252 | 2026-09-29 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a0af6c1-dacd-3ece-969b-9dd783b185a6 | -11.42214 | -43.46965 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7b39c98b-6dbf-37d5-85b1-7d72a611a502 | -11.64739 | -43.50983 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa8633cd-dafc-3a4c-ae04-37f72b688b91 | -11.16808 | -44.79477 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34174f6d-f5a6-3bee-af84-4e6db67f2894 | -10.71852 | -44.4372 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9db8155-7f57-3f7f-9f0f-4ac5ada82326 | -11.17479 | -44.79604 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4fa419c6-9740-3773-8aab-e4245cb6773d | -11.64125 | -43.5085 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
