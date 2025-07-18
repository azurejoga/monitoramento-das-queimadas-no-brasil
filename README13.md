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
| 05d22c87-f78a-39e0-876e-ffec71c9ede3 | -4.1087 | -48.21175 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89afccb9-6150-3acc-b623-ae0786494974 | -3.9439 | -48.09602 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 154ba83b-8f29-3d71-84f5-d3723a5fe36d | -3.07583 | -52.42802 | 2025-07-18 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32622ad6-37b1-3968-be5a-6e7ce9695703 | -6.54225 | -44.45435 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfad2238-7008-319f-8f6f-14188d6e3216 | -3.39964 | -47.50209 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 503adc4e-5ff3-3aba-b1e9-d970649a69c9 | -6.32823 | -43.74443 | 2025-07-18 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41bd010f-e584-3bb0-87f1-e5f6d1c744a0 | -6.71571 | -44.32615 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20e58c93-f1a6-336c-9dc6-2f3e05bcfb4f | -6.86153 | -42.76255 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5869c4f3-15e9-329f-b7f0-8a4af4d83053 | -4.3078 | -48.10577 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 535567f6-fae5-30b7-b45c-2aa8f5abea9b | -6.90582 | -44.13844 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1d2a14e-7192-319e-b87c-8c4b25080c0b | -6.97512 | -42.8054 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e21036b-05a8-316d-9255-4dd9cd231a65 | -6.29261 | -43.42594 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c2c36cf-273c-3c8f-99e2-68978b9e4cb1 | -6.18123 | -48.07253 | 2025-07-18 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddea51b8-57f2-38e9-b66e-4637209d0777 | -3.29756 | -49.19206 | 2025-07-18 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d8d2dfa-d8fd-3a78-819c-c95a3e61405b | -3.61005 | -43.54234 | 2025-07-18 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d20cd901-257e-3d28-80bf-0ffede866459 | -7.28162 | -44.22057 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe447a7b-e7fd-351e-aa27-0f1afd8bba53 | -4.79953 | -43.22383 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 583e2ce3-5442-3d1f-a99f-8670b0478139 | -5.58897 | -51.19387 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b2b8c11-3dc5-3a24-b0e8-0d697c56f344 | -7.2851 | -44.22108 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5b9a7e8-720e-320d-98a1-cf326ffa2d3e | -6.1933 | -44.09362 | 2025-07-18 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de24d90-cc79-34dc-b58d-a733d1231169 | -5.53216 | -43.88316 | 2025-07-18 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25ad0579-892d-33c9-81bc-67295784085e | -6.95027 | -44.56065 | 2025-07-18 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6db6aa6-01ea-324f-a94e-6f1eb2000585 | -7.20739 | -43.00761 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ef2fa8b-4eb7-30a1-835c-bdef6224ae97 | -5.73513 | -44.50422 | 2025-07-18 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acb52ad1-2780-3840-b6a4-1c19d4671b6b | -6.52847 | -42.60834 | 2025-07-18 04:25:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1caa37d-6d71-3ee6-a93f-1b2f060b7560 | -8.09402 | -43.15132 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 55800750-8660-3c36-b369-47ca8a3ec05f | -4.79991 | -43.22432 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 246260b2-a42e-3df9-83a0-3bec0f3c51e6 | -5.34801 | -49.10841 | 2025-07-18 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4173f9ab-b3eb-34b6-bfdd-ea8facacb421 | -7.83447 | -44.833 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f5bc2ea-c08e-3aa2-a513-72f83a1bf59e | -4.78043 | -43.37582 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3b4ab3c-5070-355c-9a8c-252959ff055a | -3.1215 | -47.0089 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4daef91b-a7e2-32b2-b969-b640c70d5d66 | -7.93972 | -43.86153 | 2025-07-18 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5d2dc98-aece-36f9-95cf-9e3218b9fea5 | -6.62301 | -47.19477 | 2025-07-18 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46061391-d990-30f3-9e02-a654d1fc9ccb | -5.16747 | -40.76237 | 2025-07-18 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87cc8ebb-5ab5-3c6e-a2b6-238bcf52819e | -7.3531 | -44.19579 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2d82531-a1d5-35c3-81c3-90d21bdce41a | -6.9984 | -44.47583 | 2025-07-18 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 145600ed-1df6-3a9d-846a-558cecb7969c | -4.59082 | -43.31226 | 2025-07-18 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 22f87640-f0b7-3360-bded-1028e3ffdfaf | -4.15211 | -48.22162 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 487a999c-8395-3da0-84dc-c02f0f2bd66b | -3.73584 | -53.99105 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da660103-12b3-3997-ae74-901aa6de21da | -3.58972 | -48.94088 | 2025-07-18 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b022cf76-a398-36f2-a729-bc0f668e626e | -8.08598 | -43.15461 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7e8714e8-b2d2-33d4-9b75-561240602816 | -3.8312 | -47.74633 | 2025-07-18 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c039372a-203d-3a53-a447-b9c0d6027bda | -6.95085 | -44.5569 | 2025-07-18 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cdd790a2-37ae-367a-a129-a3c9cd13d58c | -3.39624 | -47.50156 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37fb8a2d-916c-3799-83d9-8803ead4b2ad | -8.08292 | -43.14962 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2eaa782e-3a05-3274-9fb2-c76988cac17d | -2.6413 | -47.30282 | 2025-07-18 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f2c4dd1-5c12-311f-bd76-741c91b2855b | -3.73127 | -53.99074 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f1d1ad37-2964-3b01-be0e-1c2462a1ef44 | -4.48566 | -46.07633 | 2025-07-18 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df1ae0e1-eb85-3a96-84a3-987b9ae62dd0 | -6.88998 | -42.77626 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5086865-7dc8-3523-9935-cc9ddd9aa52f | -5.83624 | -44.09561 | 2025-07-18 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f1c0de8-5366-3b03-be30-5d18892a767d | -6.92617 | -44.12181 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a6cba8f-5863-3225-8415-e4335d8b2f60 | -6.46069 | -45.07412 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2ace72a-d294-3f88-880c-d80a5bf935a1 | -6.96548 | -43.74455 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45761436-9fba-3056-89ed-609f14cda9f2 | -3.73579 | -53.99426 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96a10396-d6a7-3784-b206-bba5ca0dec14 | -7.24785 | -44.51601 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c49af2c-7d22-3a96-a121-726e1cb342e5 | -7.61307 | -45.55405 | 2025-07-18 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e36a3017-cf1d-3d1a-851f-39e98b1efd1c | -6.23188 | -42.01994 | 2025-07-18 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 404726ac-a4da-3ca4-a6f2-257f5bfdda2a | -4.96588 | -43.22701 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf7cb12d-f601-3e1e-bd9c-9cad4388b1d6 | -7.22191 | -44.13306 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25d3dfb7-7de8-388c-b1d3-07227d2fc272 | -5.53158 | -43.88697 | 2025-07-18 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39872b89-faf8-3e32-bd56-eea4c0d722a9 | -6.93459 | -43.80535 | 2025-07-18 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4a75d2f-6064-3a46-bffa-e9078e50db19 | -3.39517 | -47.48643 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5663e68-6e19-3625-b6a4-adbcb710c82c | -6.16499 | -45.09074 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 953d68b6-eb0d-302d-8900-2e35b43f7fc1 | -7.16868 | -43.59415 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db1c314d-2815-37fc-9f89-663122b7aed2 | -7.06093 | -42.98337 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d26f947-48aa-3ae4-872f-c224747fff80 | -7.60762 | -46.31765 | 2025-07-18 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 485c2e05-f99b-3b88-8545-1dbda314eb0d | -5.83911 | -44.09996 | 2025-07-18 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c40e85f-6ab0-37e4-a990-9a6d6bd223d7 | -7.59269 | -46.30466 | 2025-07-18 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18f2f662-b20a-3b2c-8d40-5d5f65569f62 | -3.39915 | -47.48331 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 290c595b-c475-3e23-852a-1b0e35b251ed | -8.07858 | -43.15346 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 5d9c93fb-fdb3-3fd5-bd6a-24067a68ed59 | -3.03707 | -47.86046 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34b62956-1e9a-3904-92b8-cc59fff21c37 | -7.19107 | -44.07642 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df121f13-69cd-39e7-b6c9-005a300df905 | -4.4862 | -46.0729 | 2025-07-18 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ae6374c-8d1d-3a9e-a9f8-141a552558de | -7.3717 | -44.02639 | 2025-07-18 04:25:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3861769b-65e1-30d9-a7a0-b7cf20d9e4ae | -2.92602 | -48.23721 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18a95bde-a27f-320b-9268-fa943a2d2de6 | -6.26499 | -44.06535 | 2025-07-18 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a920bc-4db3-3432-ae83-ad6a1c51a1f9 | -7.60973 | -45.5535 | 2025-07-18 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 766d78db-30f4-311c-9b8e-2694db824c23 | -7.62496 | -44.29431 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5061fd4e-9ed6-3ff1-830d-8f4702510374 | -7.2593 | -44.51017 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e24eef11-041e-39a6-a51e-e393a49324c0 | -3.7354 | -53.99374 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a1ee8fa-e683-33ba-b741-77f628bb83b9 | -5.76163 | -43.39715 | 2025-07-18 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 927f3e2b-9064-3e39-8d63-e1296dd1bb44 | -4.80249 | -43.22839 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c42cd84f-175a-3f6f-b8cf-2ff7337ff182 | -7.13133 | -43.79646 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01bc0d52-1d50-3c4c-b28d-aa96a2dc4f62 | -6.66545 | -43.96018 | 2025-07-18 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 650c9b2b-555b-393f-a2bc-38522bbee934 | -5.79514 | -43.63126 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 75d01eb1-ee6e-3b75-a6dd-d80dc52838c0 | -6.69025 | -43.18805 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1f64049a-38b0-3fa9-9798-3e473fd78c34 | -3.12094 | -47.01244 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f40de402-46b8-3dbf-9bfd-eb5d13612cb6 | -3.3878 | -47.48901 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| cc470018-af27-3b0f-9b8b-53b29e9ce7be | -8.11689 | -43.15026 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af4dee12-daff-3650-bbad-2ef020fd1c02 | -6.49813 | -47.23175 | 2025-07-18 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b200a977-8c71-33b3-96f6-97f11362e027 | -7.24018 | -42.93008 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4c04f5d-8727-35a1-bd5c-4efa399f1748 | -5.95334 | -43.0357 | 2025-07-18 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df6966e0-5fd7-3e2e-ab24-8732ea250f77 | -2.63975 | -47.30629 | 2025-07-18 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b79b2f25-aeee-3514-8530-9d52179ab631 | -3.39973 | -47.47966 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f1d8b094-f1c3-3116-9960-9a0ecb7c4af4 | -2.44727 | -47.32856 | 2025-07-18 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c568f57-28ed-3695-bc55-110cbe313946 | -6.49974 | -43.46796 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 166e5b31-8415-3a1a-ae9f-c2e0902b895b | -6.52305 | -43.15294 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4de727e3-8351-3093-beba-3f2800774216 | -3.38441 | -47.48848 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c00d4ab5-52ea-3b8f-b3cb-c987720e7e95 | -5.3623 | -45.11968 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69abb2ab-e05e-312f-a2f0-c9c9f15b2435 | -7.06963 | -42.97564 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
