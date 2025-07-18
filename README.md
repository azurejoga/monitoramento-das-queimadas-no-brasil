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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e248d71b-d25f-3f78-893f-60c4d4a76fcd | -8.1075 | -43.1411 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| d85446f3-c100-3dcd-83b0-433611077066 | -10.8217 | -49.2777 | 2025-07-18 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f051ff51-62a4-34da-8538-30184f6896a5 | -5.6379 | -43.7175 | 2025-07-18 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 216.0 |
| d16f0a9b-9d54-31aa-b567-000827c531fb | -5.6569 | -43.6929 | 2025-07-18 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| c0c9d605-ad2d-386d-95c2-597353f46b5e | -5.6754 | -43.7147 | 2025-07-18 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 60892ed5-5344-314d-8b2a-0b7b56157471 | -9.7703 | -48.7405 | 2025-07-18 00:00:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7839070c-ecd0-38b8-9409-84649d59555e | -20.9166 | -49.0607 | 2025-07-18 00:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| 9a4fdf31-be1f-3b88-b011-b99776ddb678 | -8.0883 | -43.1667 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| 256f428c-6716-325d-af51-0acfb930211a | -8.0696 | -43.1452 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 59578cc4-c4b9-3822-9159-867f36dbe3a1 | -3.1198 | -47.0075 | 2025-07-18 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 631ae551-2b18-3fd5-8c6a-ecce7392d867 | -5.6567 | -43.7161 | 2025-07-18 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 381.3 |
| 3bde8e91-4a37-30e3-bcee-08e0c8f7521a | -11.5587 | -47.0966 | 2025-07-18 00:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1f875942-e1ec-357d-9e9d-7ed3282a6d1e | -8.0693 | -43.1687 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| cebf3846-bc49-3cab-be64-29f33a8977d9 | -8.1072 | -43.1646 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| fb708e1c-df35-3dc6-ab4f-f3d35df70eb3 | -11.5778 | -47.0941 | 2025-07-18 00:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a3bd9bed-d6c3-3818-b407-be2b67960aa2 | -3.3958 | -47.4785 | 2025-07-18 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 189.8 |
| cef1a998-07ae-3d99-8668-a6408888dcd4 | -11.7508 | -48.1825 | 2025-07-18 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a5325fee-5c75-3ea6-bf2c-33391ee485e1 | -5.6382 | -43.6943 | 2025-07-18 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 38d47d06-33a3-39ed-8c07-e915d7f7d083 | -3.3772 | -47.4792 | 2025-07-18 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1eaf694d-a7bd-3963-881f-03903081ddb8 | -7.3588 | -49.6013 | 2025-07-18 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2044b65b-8faa-3b0a-af60-ed12842f7480 | -11.5782 | -47.0717 | 2025-07-18 00:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| d7b32421-3577-3821-8272-80ef18dd6665 | -11.559 | -47.0742 | 2025-07-18 00:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9f9f8ff0-6d6d-3837-9935-c4c427631f03 | -9.77 | -48.7623 | 2025-07-18 00:00:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 629669bf-0a24-3083-9cd4-df960be1f569 | -11.7317 | -48.1849 | 2025-07-18 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f00ed62a-4319-39f3-babc-5a9d31ee9500 | -8.0886 | -43.1431 | 2025-07-18 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 265.4 |
| b9a98c64-1fcb-39ba-b9cd-ac6e21f3da50 | -3.3957 | -47.5003 | 2025-07-18 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3456362f-2f7c-3906-9c1f-e18feeb1c0dd | -11.5782 | -47.0717 | 2025-07-18 00:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| fd93f95a-45f7-3c7e-8c3a-2ed7a26ee7e2 | -3.3958 | -47.4785 | 2025-07-18 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 0ec6bc38-cae6-355c-a23a-02389bbefbd7 | -8.0696 | -43.1452 | 2025-07-18 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 2b4398ad-f807-3c14-baab-78888d29e9f6 | -8.0883 | -43.1667 | 2025-07-18 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| 31d82dd2-d1d9-3266-a2d1-44417c6e6590 | -11.5587 | -47.0966 | 2025-07-18 00:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 614cd2ea-5fdd-35c6-9c0b-ca755f84a247 | -11.7508 | -48.1825 | 2025-07-18 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 11b5e6e9-8ba8-3a8b-bdac-3e8db0ba57a8 | -8.1072 | -43.1646 | 2025-07-18 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| e470667a-df0a-3983-a3e5-c1fce19f9f49 | -3.1198 | -47.0075 | 2025-07-18 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 6d445be0-affb-3033-a4ec-b6b7093ad130 | -9.77 | -48.7623 | 2025-07-18 00:10:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| dc2d6aa0-7a18-34d6-925e-9e6e5b7a2aee | -5.6567 | -43.7161 | 2025-07-18 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 454.0 |
| 1088255f-6e0e-33bb-8b0f-d2a897b27964 | -11.559 | -47.0742 | 2025-07-18 00:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d529fabb-d07f-34a0-99a1-33ad037893cd | -8.0886 | -43.1431 | 2025-07-18 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 251.4 |
| 91d481ba-3fd8-37ed-b234-96d4ccf7fada | -3.3772 | -47.4792 | 2025-07-18 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a587a653-ade9-3266-aec5-28d5d40cb809 | -3.3957 | -47.5003 | 2025-07-18 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 945cda78-7876-3322-9820-283a697367f4 | -20.9166 | -49.0607 | 2025-07-18 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 761dd158-d79d-34fb-a03d-bc7ca5c71785 | -7.3588 | -49.6013 | 2025-07-18 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6dc32630-b719-3bbd-8abf-129d537ab724 | -11.5778 | -47.0941 | 2025-07-18 00:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 52407e0a-2df0-3b8a-88a1-2dd4eeee8812 | -5.6569 | -43.6929 | 2025-07-18 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c335381d-9dbc-3c6d-ae31-2d62c42c3a64 | -11.7317 | -48.1849 | 2025-07-18 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0c7e74a5-4066-3ea3-99e0-35e29852f480 | -8.1075 | -43.1411 | 2025-07-18 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 6063e064-e6fd-319c-8042-169c5c0a3a87 | -5.6379 | -43.7175 | 2025-07-18 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9496f77a-0e74-386b-90f8-2fe51acba6db | -5.6379 | -43.7175 | 2025-07-18 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cc5f69d9-b135-3587-88b4-bd4b68ed77eb | -20.9172 | -49.0376 | 2025-07-18 00:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| 66c1acc0-e494-3fff-9b67-898600ca37c3 | -8.0883 | -43.1667 | 2025-07-18 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 0d7fb6ff-a18f-39d7-a43b-26cd84a0eaf0 | -9.77 | -48.7623 | 2025-07-18 00:20:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 05d57418-3867-3056-848e-87d33f37ea2b | -3.3772 | -47.4792 | 2025-07-18 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c7898b5c-7acb-3364-9683-50e94c082d74 | -3.1198 | -47.0075 | 2025-07-18 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 857363f3-25d0-3d5e-9f65-9516ccc5f1c6 | -8.0696 | -43.1452 | 2025-07-18 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| eb699a79-09b0-322b-a39a-a2fa13e4de22 | -20.916 | -49.0838 | 2025-07-18 00:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| 3fde3842-13b8-3419-98c9-07eed8478a07 | -8.1075 | -43.1411 | 2025-07-18 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| c70383fe-e1ca-3c75-b1ed-cf7ad22a7372 | -5.6567 | -43.7161 | 2025-07-18 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 365.4 |
| a8dd4875-b22d-3bb1-a7ff-2d3da3340de4 | -20.9166 | -49.0607 | 2025-07-18 00:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 235.9 |
| ff1a69ea-9e5b-39d0-a642-3f0808191ac4 | -11.5587 | -47.0966 | 2025-07-18 00:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c2df2215-4004-3d8e-9de5-e08af439931c | -5.6565 | -43.7393 | 2025-07-18 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 29c6ef49-16b5-3077-a28b-944e6630756b | -11.7317 | -48.1849 | 2025-07-18 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ec5fa047-20d1-3e61-a76f-b6950af3b02f | -11.5778 | -47.0941 | 2025-07-18 00:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 139151e2-c7c8-32dd-9662-8235af800b2d | -11.559 | -47.0742 | 2025-07-18 00:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0f8dcead-eb87-3ba0-86b2-167907aa2d28 | -5.6754 | -43.7147 | 2025-07-18 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3509113d-7d27-3292-898e-3b42e5d6736f | -3.3958 | -47.4785 | 2025-07-18 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 65f5c872-1311-35ff-82cc-d96473ff8566 | -8.1072 | -43.1646 | 2025-07-18 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| adbd6085-d449-3393-bc33-f5225fe5c513 | -3.3957 | -47.5003 | 2025-07-18 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 17a7cfe3-023b-395d-8afe-b6bdee9b4a13 | -11.5782 | -47.0717 | 2025-07-18 00:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9e3526f1-0c45-3fbb-9b62-62c2cdfc3f3d | -5.6569 | -43.6929 | 2025-07-18 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 8f93b9e2-25b9-3125-a9a9-fc0e871270f3 | -8.0886 | -43.1431 | 2025-07-18 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 215.1 |
| b16e96d5-f5e2-3ef8-9b7d-7a09534610e9 | -9.7703 | -48.7405 | 2025-07-18 00:20:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| b4ea455d-4cf6-345d-b864-a58fd1e8ca48 | -5.6569 | -43.6929 | 2025-07-18 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| bd13be49-1203-3b5e-a083-13b0f8764907 | -11.559 | -47.0742 | 2025-07-18 00:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 55d0f6bd-2569-3b15-9fed-95406ccc5d28 | -3.3772 | -47.4792 | 2025-07-18 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 39fd842e-7b79-3e78-ac4a-20e14b2bcf26 | -5.6379 | -43.7175 | 2025-07-18 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 716de407-b2ad-3511-81b6-4dc9773c02b8 | -11.5782 | -47.0717 | 2025-07-18 00:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a76db23e-11a9-36b7-b1d3-2118d120d8e9 | -20.9166 | -49.0607 | 2025-07-18 00:30:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.3 |
| 5d8a6424-a664-36c3-8816-c0b886e08d85 | -20.916 | -49.0838 | 2025-07-18 00:30:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| db1b0b6f-fb14-3d25-a433-def8823896f9 | -4.301 | -48.1133 | 2025-07-18 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| aaf62db5-9058-382f-9323-2f38b074953a | -11.7317 | -48.1849 | 2025-07-18 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 039ed77d-0759-33a9-b3f4-b0fcb0609fdf | -8.1075 | -43.1411 | 2025-07-18 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 9b0b8b28-3782-3987-9519-e92b47d08ec7 | -3.1198 | -47.0075 | 2025-07-18 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ddf753be-6869-319d-9a4b-8f8525f294bc | -20.9172 | -49.0376 | 2025-07-18 00:30:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.6 |
| 9f1db0ed-bece-342b-a326-ef7e823c4763 | -8.0886 | -43.1431 | 2025-07-18 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| bfbcb5bf-6f11-3ed8-9213-d429719ade1c | -3.3958 | -47.4785 | 2025-07-18 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 856e6985-1134-36f4-96e1-34aa6e09c014 | -11.5778 | -47.0941 | 2025-07-18 00:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8e72a6f0-4376-3d8a-ac5d-d66eb90e4392 | -3.3957 | -47.5003 | 2025-07-18 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 47eefc5f-7edd-386f-bc02-0225b9f9375a | -9.77 | -48.7623 | 2025-07-18 00:30:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| caaed042-93dc-3845-9d3d-2b9f2568650d | -8.0883 | -43.1667 | 2025-07-18 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| cb02dc37-8f31-332e-9c07-63bee4bc8082 | -5.6567 | -43.7161 | 2025-07-18 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 363.9 |
| 8e5f4184-4e8d-3d0f-9a62-6b7cbebcea61 | -11.5587 | -47.0966 | 2025-07-18 00:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d4ec8944-9e64-310b-abc1-a977eff5ac35 | -5.6565 | -43.7393 | 2025-07-18 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 41e75e85-6ead-3140-8026-c64d5978c41b | -8.1072 | -43.1646 | 2025-07-18 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| db61ac19-cd68-3d0b-8be9-018d0cf04328 | -8.0693 | -43.1687 | 2025-07-18 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 4bf60758-f5db-314a-b1f0-50440b93c388 | -11.559 | -47.0742 | 2025-07-18 00:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 68697f67-22b1-3062-b2c1-628e225b358e | -20.9166 | -49.0607 | 2025-07-18 00:40:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.0 |
| f4ae234d-c75a-3a52-b1ba-230e71994e2f | -8.0886 | -43.1431 | 2025-07-18 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.0 |
| a491809b-42f0-3e40-b5ce-811e64ecec31 | -21.0789 | -50.6188 | 2025-07-18 00:40:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 241.8 |
| d7cfa6ce-2e2b-3d0c-a9ab-19ecfdb4d8da | -21.0795 | -50.5961 | 2025-07-18 00:40:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| 91566783-acaf-3b93-ab0d-e821ba3a9bb4 | -5.6565 | -43.7393 | 2025-07-18 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |


[Clique aqui para ver as próximas entradas](README2.md)
