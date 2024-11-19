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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e42d8e6-f78e-3ed2-a37c-068d69db0e30 | -2.80971 | -54.01931 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2df58f27-e9b7-3f1a-8cbf-c19523739e69 | -1.65868 | -52.53324 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d583b460-841a-3eea-a60c-b70bf4b3e5c2 | -7.14638 | -49.29976 | 2024-11-19 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d0b7c42-5742-3378-85e4-b52ba472ec3a | -2.19206 | -50.68294 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b2f3c8-56a9-38c6-a93f-4bbd53abdba6 | -4.63608 | -45.1186 | 2024-11-19 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e1eb264-6bf6-37d6-896a-8169c39f3fb2 | -0.3508 | -51.40676 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ef2af25-cdae-3943-92c0-1c299a90fd1b | -4.34272 | -50.45735 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b181c0-d4f1-3f60-9632-7cb3ce321130 | -1.37948 | -52.07892 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 95629943-7b39-30c3-adb0-5bc80f8a1aa0 | -2.61309 | -48.21804 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9771e8a2-383f-3be5-88a4-58ef9be000b1 | -2.00534 | -44.79653 | 2024-11-19 04:46:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b9ec2c77-0b27-3bff-9498-7b117f429700 | -0.89801 | -51.72034 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eab16e38-4bbd-3fb1-bd72-785076e4748f | -3.76677 | -52.14165 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1d6788f-dba1-3f42-8660-83e0f2536f59 | -2.20295 | -50.28389 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21ccebad-9f8e-3583-9bd1-ab1bcb2566e0 | -2.58008 | -51.72251 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec31ed15-be23-390a-8b84-8b32dd64ee22 | -0.83003 | -52.8658 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8143f76f-255c-39d5-8e31-ea8685887f60 | -2.23666 | -53.66002 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1868c646-625f-3021-b8ae-599d9199ecf9 | -7.47717 | -47.17998 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29afca84-8842-3701-83c0-32b5278f3d34 | -8.26811 | -44.03544 | 2024-11-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecb92398-11d2-3b2e-8ff3-fd26c1f22e5b | -6.29406 | -43.8485 | 2024-11-19 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e070f9c1-504b-3488-a34a-7ddf0fb20c16 | -3.66402 | -54.65675 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cedd010-0049-3eef-8e92-d5725ffe77fe | -3.66209 | -50.43892 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0fc85c3-1c86-302e-ae96-add1f8ff42f3 | -2.25721 | -50.46084 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede80b38-6f73-3170-8f6a-ec4d2c5ff3e7 | -4.55437 | -48.01208 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bee998a1-0ba8-3a94-9a7f-077f93942643 | -3.34447 | -53.31236 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab0406ea-5106-3008-9472-6c704db079d7 | -1.92176 | -53.34666 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3288ee83-30f2-3248-9454-5b2a7f15a638 | -3.374 | -45.33361 | 2024-11-19 04:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d1bd898d-12c1-398d-ac9c-e39a0d2f658c | -2.92892 | -48.33048 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8601e9db-9414-317b-8c0f-050e3a2463f7 | -4.22524 | -46.53335 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e990169-ca8b-3236-a1c5-3e13d0ea53a0 | -3.51718 | -50.23268 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a6fb406-df9e-367c-8cc3-154c01e60799 | -6.04837 | -46.6048 | 2024-11-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9e45978-cd7b-34df-b091-3fa18c4d2029 | -4.10963 | -43.58861 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e4aafb3-12ee-3b36-b543-856708090085 | -1.37606 | -52.07839 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4396d455-bd51-3f53-be2b-42b466afe88d | -0.93384 | -51.63287 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28d94d0-6d5e-342d-bcdf-38962de71d37 | -1.94948 | -53.3341 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11c5a194-351b-3cdf-88d1-a278d04f83f0 | -1.22531 | -51.78905 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 321ffd8e-479e-30e9-a253-cf9f53e3b6de | -3.37957 | -54.75888 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b77b525-82c4-332b-b65e-3d636b4ad175 | -3.01114 | -51.4466 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09a3c5a5-6385-323e-a732-3e4734e9cecd | -7.99835 | -44.36874 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2166fd7d-9843-3975-bfd0-3c9cff270fd3 | -2.29073 | -49.19535 | 2024-11-19 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 616f5060-3206-354c-912b-7e2e8aca929d | -5.97494 | -45.36555 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6b8dce5-0def-3487-a9b0-7f42d00793c6 | -2.94967 | -48.32956 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 672e1b98-f805-39c3-9a05-42414ad7cd3f | -0.82387 | -51.74996 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84f8f2bd-a272-385d-a1af-a02c911975e3 | -3.66156 | -50.44236 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c76e92b-ab82-34a3-bd81-0fd57dbc2369 | -2.86538 | -51.78878 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8faf871a-2569-3279-8c90-def1243ee6db | -3.7796 | -51.99357 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98e8373a-e30a-396a-8e59-304778643964 | -2.54353 | -47.33461 | 2024-11-19 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 191bc074-31ba-3a97-a186-b93c0e1f2cad | -4.0566 | -50.00192 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deb77913-d8ba-3d98-b070-1ddc972bec09 | -2.95451 | -53.71725 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce681e6-422d-3ad9-92a7-4d97cba8a0e5 | -1.42163 | -52.4392 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1b620b0a-0660-374e-a897-db6fb2f4a614 | -1.30557 | -51.74196 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db490cba-21a9-3c13-99fd-d053ad6cfba3 | -1.04616 | -51.74269 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d893d69e-d658-3e1c-8463-a6022611c788 | -3.7768 | -51.98949 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef8b72e-935a-3844-ba67-4b755a4e1852 | -1.72775 | -52.693 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f43ad17f-e77f-3ce5-aafd-15b46758c5e0 | -2.95929 | -51.40993 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 711be693-3cbc-3211-9a25-9558666ae396 | -4.86112 | -49.26587 | 2024-11-19 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4193ff75-68b8-33fd-bdba-5e92b3a08c5d | -3.24806 | -51.5198 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e1bb90-6b0c-38fa-9dd0-80bbb6efa1a3 | -3.05976 | -51.33266 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23111fc4-6a3a-34b3-a581-b417bd4fdd71 | -3.72663 | -52.44753 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6970707-1586-3cbc-a195-22c19b132c7c | -2.60755 | -51.78876 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58c7f49b-8e00-33d2-92aa-8a70668c07eb | -1.07493 | -53.36821 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16136a9a-355f-3501-8073-1d03e15e533e | -6.05552 | -44.04236 | 2024-11-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2f067387-28e6-3443-9299-63944a5d33fd | -1.5454 | -52.0289 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5356bd0d-3a65-3e9b-b869-2247b2981ab5 | -3.66432 | -50.4463 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ab6d1b8-94c9-3bfb-93bf-e945a62b5be4 | -1.95092 | -51.59204 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afd5623b-9ee9-3172-b819-526c51b5114c | 0.3868 | -50.86038 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95331392-994e-3023-95b3-52901270a272 | -3.76615 | -51.92596 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d78ed1-7039-3cbd-992c-447191376129 | -1.4738 | -51.96931 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede2ff69-2843-3fec-872d-a7d7eacf30d7 | -2.0832 | -48.53689 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 736b1783-8cae-3d47-b634-c5ab6a1ac028 | -2.76834 | -52.60022 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 849b0fcb-88ea-354a-a0b6-652a71d23fcd | -0.93098 | -52.49836 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85d1aaf4-780d-30ba-ab47-337c2c48c8f6 | -1.59362 | -50.44122 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fd8a5d6-32f7-329a-8235-cbb58d9e3753 | -2.95076 | -48.32614 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea513683-7074-30ce-b541-0cd8ab171175 | -3.14506 | -52.25998 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb1e5df0-fbca-33a7-923b-59a780c5baaa | -5.86052 | -39.66391 | 2024-11-19 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c508d07c-d67d-3286-9691-d464df816ac9 | -3.35729 | -44.7868 | 2024-11-19 04:46:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9240e7fa-c3b6-32d8-9d73-06345d823c82 | -1.50379 | -52.1816 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53ea73c3-81a9-3f79-96cd-d053976a6321 | -5.65346 | -45.19879 | 2024-11-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d9fd811-16c7-3db4-a9d2-462c26057c0d | -2.60699 | -51.79234 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16c5d808-da43-341a-8786-0501adbcec54 | -2.28998 | -53.62938 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e6d29edc-bf49-3e5e-bb0f-7ce36deb26a3 | -1.04956 | -51.74321 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e448e489-4998-3c84-b485-3655e648e1c1 | -1.20557 | -51.77497 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59e7e58f-df0a-3eb5-ba74-5961fcc608d9 | -3.48119 | -48.25304 | 2024-11-19 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a09ce67-a798-3edb-9682-10d1bb1aa091 | -2.26269 | -48.41767 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78ecb5be-7c8a-3854-a6fa-3d8123b7669c | -1.95174 | -53.33327 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0052314-aa70-3fad-a220-783e80cb3e38 | -2.44677 | -50.40301 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17f2a20c-60fa-3140-9a44-093b819f6bd0 | -2.26365 | -51.09436 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52faee38-33ad-3362-8a13-0b21b9722e5d | -2.71255 | -52.00027 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fecae1b-32b5-3cf7-8e10-a51e8a241132 | -2.66575 | -51.71745 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ecdac4b9-55d1-3dca-b939-88113b814c46 | -1.22541 | -51.74448 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5523232d-66df-30d6-94ba-af1bc47418d1 | -1.21456 | -51.7911 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b9b6dbf-444a-3f80-a894-fd647b2eea5d | -5.97858 | -45.37022 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 019f6ebd-766f-36ee-b9ab-79a64d34df4a | -3.06354 | -54.40503 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 717811b9-749a-3bcd-8c44-63d2d7d7868f | -3.55519 | -51.53564 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c78dab4d-e567-3ef5-8169-552a7170131a | -6.93473 | -45.08364 | 2024-11-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aafcb07f-bf24-34a7-8395-6f3e1f0dac2e | -6.34279 | -46.37385 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50f2239e-5942-308c-9ec6-24510e7c9bc3 | -3.34156 | -53.30782 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de0d777a-1ec1-322b-8963-2fbcc042c1af | -4.86056 | -49.2695 | 2024-11-19 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e53a226c-bc8f-3996-b77d-e52e96c62f8d | -3.70672 | -51.82916 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b4d3e2-a2f7-3914-a90a-b6ce4c4f5e57 | -3.94944 | -46.69545 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553d1ff0-d6e7-398b-a923-2a1052f721da | -0.25283 | -48.5237 | 2024-11-19 04:46:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README32.md)
