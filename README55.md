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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2459dbd-198f-303d-baa3-17873ef5fcca | -12.4357 | -45.1284 | 2025-09-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 272.7 |
| ed1bbce8-de9e-3e7e-820d-8836b05b213b | -14.788 | -51.3621 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 58b8701b-c8ae-3c89-a0a9-a4341b646aca | -14.8479 | -45.4846 | 2025-09-21 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| fb466733-1680-3214-bbaa-a0b284088edf | -14.7877 | -51.3836 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2359538c-6878-369c-80b1-5e2ad6b7c45e | -7.5275 | -44.3182 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 531b4e80-c85c-312e-aad3-9ed5aada52ff | -9.8822 | -46.116 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| b280ce3c-985d-3c6b-8046-921cfe568fc6 | -12.7486 | -47.9818 | 2025-09-21 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d262ac9c-d69d-3384-af31-c7fb409c7d1d | -9.629 | -46.617 | 2025-09-21 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| fbe85440-eaeb-3f4a-98fd-32b8be766b34 | -12.455 | -45.1254 | 2025-09-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 761.7 |
| 825acaa1-6a7c-3233-b633-9dec162d6caf | -9.8629 | -46.1408 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 93a52f41-c042-3191-93fc-f667646cf9f3 | -11.4477 | -43.5514 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 1978ee5a-4d05-3d49-bbc0-12ade1d837c5 | -4.4084 | -43.0551 | 2025-09-21 14:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 004786ff-5ff2-3ad8-adbb-f8c191a07875 | -12.7337 | -47.7391 | 2025-09-21 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 57af657b-420f-3197-a17d-bf12cb010a2b | -12.7302 | -46.8651 | 2025-09-21 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4a9a57e1-ddc8-324d-8661-bb62c1a5731b | -7.5603 | -44.7285 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d9ad3ec9-14ae-31b8-8e21-af2c4d81c73d | -12.4361 | -45.1052 | 2025-09-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 10b0ad3c-f0f4-3e46-a1ab-a99fb18e8fac | -5.139 | -42.9376 | 2025-09-21 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5dd65c2c-3ac7-3392-985e-8302519a8431 | -12.2983 | -45.2881 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 5aa1fd56-743a-3137-9be6-ee113ad335cf | -11.4853 | -43.5929 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| f65a9caa-e1b1-346e-970b-cd66727cf593 | -7.7336 | -44.3902 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 84928d57-8d46-30b0-ad49-e9ca7af218bb | -7.5791 | -44.7267 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| bd2ab199-92f0-37a2-8560-7d81d85bcacd | -13.2421 | -51.6933 | 2025-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b4c872a9-de97-34d3-854c-2ab0115c3696 | -4.388 | -43.2896 | 2025-09-21 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| dbad0f12-142d-343f-9777-2da51eefe1e2 | -17.1173 | -45.9491 | 2025-09-21 14:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 234e06e3-66ba-36ee-a932-edf49a7976d0 | -7.7148 | -44.392 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| e238014f-6765-334c-9e6a-9a407c08f47a | -12.9349 | -50.5565 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 78f6be3b-e7ee-3cb3-ac83-a6af98ff2cba | -10.0128 | -46.2583 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3682d880-027a-3ff6-bdb6-1fde92a4eef7 | -5.3711 | -42.0937 | 2025-09-21 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 1a26bc44-e9cf-3f05-be88-c188f3c85670 | -16.8727 | -43.8894 | 2025-09-21 14:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f43c0b0a-b4e3-3614-8b7c-09b4b9e7a4f2 | -12.97 | -46.3759 | 2025-09-21 14:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| df3a2156-4c71-35d2-b188-dcca6676798f | -9.1937 | -45.2886 | 2025-09-21 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f29c37b7-fbda-3b80-bb6b-4af652e3d2dd | -15.0508 | -55.283 | 2025-09-21 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 54b70d83-eeff-3444-acdd-b735f29a31b8 | -9.8439 | -46.143 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7e5f9061-8334-3adb-a778-52b96dd13d99 | -7.5272 | -44.3413 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 65f6974f-a94c-37ac-baa3-61ac726ed563 | -12.0767 | -44.8131 | 2025-09-21 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e58327b4-3f25-381f-a169-fe74cd727ec3 | -12.711 | -46.868 | 2025-09-21 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d238151c-374a-3369-a17f-bccb9d41cd87 | -7.6007 | -44.4952 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9e556338-6713-3cb2-8d9e-adbeff965aab | -11.4665 | -43.5722 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7b1c039c-ef31-35d5-bd88-17594d43b89d | -10.2811 | -46.0679 | 2025-09-21 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 94d4cc5c-846d-39af-9661-6b7f2f208d1b | -8.6074 | -45.3529 | 2025-09-21 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 354d04a1-ec59-3fe1-898f-33ac9f2cfce8 | -9.165 | -44.6273 | 2025-09-21 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ac904aec-65ac-3291-93e0-929e7b10efb3 | -2.9903 | -42.8689 | 2025-09-21 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9e5ccaff-ae2e-34fe-8d1b-86271908c99f | -13.6775 | -47.6891 | 2025-09-21 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cfdb91c9-c4da-358b-a1c7-d29093ad5575 | -12.279 | -45.291 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 28d3b68c-3ef0-3e0a-ba0a-758c5a12b7f6 | -7.7334 | -44.4132 | 2025-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4aea2547-3458-3084-9d76-5cfce6aaa46e | -14.7682 | -51.3863 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 444f910a-b3b8-37e3-94c9-cbdbecae8f4b | -8.8467 | -43.0326 | 2025-09-21 14:20:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| 43fc1d9d-9156-36d4-b8a0-c4c257fd27a8 | -10.0314 | -46.2786 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b7776b8f-ef55-391a-8b98-b591d4e48975 | -18.1071 | -44.6649 | 2025-09-21 14:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fec87538-f3b6-3b0a-834f-68a44b17c65d | -15.0511 | -55.2624 | 2025-09-21 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d4a93697-5adb-3ca2-a492-7e9b07e7dbf6 | -9.8819 | -46.1386 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 3491da3c-00b5-3ca7-bfe0-cdfad154e081 | 4.3344 | -60.7406 | 2025-09-21 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c04c9218-1a9a-3bd0-aeb7-c564caa2af8d | -12.1156 | -44.7839 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 77db45fe-6996-3c0c-b168-e20833aaec9d | -14.8071 | -51.3809 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| da27152e-4e4d-3a76-afa1-675d51c62109 | -11.2306 | -46.1722 | 2025-09-21 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6270fa4a-c55b-3039-af21-d3cb88706f1a | -7.966 | -43.8809 | 2025-09-21 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 76c93384-c3a7-3d08-b42d-08aecdeaa730 | -12.7341 | -47.7168 | 2025-09-21 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 277.4 |
| 6043ac0d-335e-39fc-a95a-f310e93ea480 | -6.704 | -44.0017 | 2025-09-21 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1919e406-ed4d-3bc1-8489-336100d64e42 | -12.2941 | -49.9904 | 2025-09-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| dd59ca17-a6f5-38d3-a8f5-868cf63ac046 | -9.8632 | -46.1182 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 005139eb-37e6-324f-9405-f3bd3a4ae38e | -2.953 | -42.8704 | 2025-09-21 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 63c8bc5b-3903-3da9-b47c-e8d70364f6c7 | -12.8965 | -50.5614 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3787cf67-6643-3d79-980c-4a80b7ba23a8 | -4.5695 | -41.5047 | 2025-09-21 14:20:00 | GOES-19 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 24023e55-d602-3b49-90e8-0b469f3a1ca5 | -11.429 | -43.5307 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1118a1e3-b77f-309e-9b57-23b863c92817 | -10.598 | -46.4573 | 2025-09-21 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| a929cab0-ef75-3a1c-9d43-f1d56a15f7ff | -14.8675 | -45.481 | 2025-09-21 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 315e7b13-1117-311c-9e78-f9bb4d740090 | -12.7114 | -46.8454 | 2025-09-21 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| e7494c15-8d70-3059-9d3b-2d8caa30ea01 | -5.5583 | -42.1507 | 2025-09-21 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| f30b8c20-63f8-3a2b-853b-3769ebe099f0 | -10.2621 | -46.0703 | 2025-09-21 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b0565072-e0dd-3908-a235-0c584a0d5b81 | -11.5041 | -43.6136 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 00bc4b00-694c-3a32-80d2-07484e860e91 | -22.2611 | -56.0044 | 2025-09-21 14:20:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 977895bc-6ac4-3de8-ba67-28a2674ad015 | -12.8969 | -50.5398 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 1bbfb2ca-7a81-35c3-86e8-db246bbd533e | -12.144 | -44.2899 | 2025-09-21 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 341.0 |
| fb445184-725e-36f3-8330-b0c0e7ad2eca | -10.6741 | -46.4477 | 2025-09-21 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 588ea242-3c5b-3f4c-bf89-7ead35596945 | -8.3509 | -44.7636 | 2025-09-21 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2b0f55f0-db86-3d3b-9ddd-24fac0936a76 | -12.3133 | -49.9881 | 2025-09-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 14ff7ea2-288e-3d63-a26c-f050e57a2645 | -16.8926 | -43.8849 | 2025-09-21 14:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 141.3 |
| f4f9d0bc-48ce-32fe-a599-6e35624a1a52 | -6.077 | -41.0013 | 2025-09-21 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 5abe0044-3193-3291-b314-57604c660ee9 | -12.4056 | -51.4113 | 2025-09-21 14:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| addfa083-7a24-3fa9-826a-02e3dcd86013 | -11.4482 | -43.5277 | 2025-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 4f9b121a-2f9b-3f87-878a-7030ba4856d8 | -12.1344 | -44.8042 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| d2a27619-300f-3283-97e3-a2c2f6afd2a6 | -10.7115 | -46.488 | 2025-09-21 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7f56d76f-3bf5-3776-8390-acf98d3ac83b | -6.8192 | -43.7599 | 2025-09-21 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0abc65ec-9ea7-33c0-bac5-55a41ed86519 | -10.7564 | -46.0533 | 2025-09-21 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 513e5a13-465d-390b-b871-6a957c8e00b4 | -12.9157 | -50.5589 | 2025-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 09af88fc-9a98-3e45-8124-164fd74db49e | -15.8829 | -47.2973 | 2025-09-21 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6ad44384-e8a8-36be-b9b7-ace3c83abae7 | -12.2794 | -45.2679 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 02b83ca5-177f-33da-8ac9-3c4a32b95265 | -10.0317 | -46.2561 | 2025-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 3318f4ba-3815-3959-bf6f-12d21509d470 | -9.1837 | -44.6482 | 2025-09-21 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e50e977e-3753-385a-b7c2-7ccf27bf2f18 | -12.8965 | -50.5614 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 78c87415-c469-3096-b0f4-ad73dc3f0192 | -5.5583 | -42.1507 | 2025-09-21 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 634dc3fb-0c3b-3ea9-a32e-4391f420fd2a | -12.8969 | -50.5398 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7ea407db-02d6-3c9c-97ad-d397b01a8ced | -14.8479 | -45.4846 | 2025-09-21 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 70ada49d-2768-3cac-8f19-91b9400dd76b | -10.946 | -49.8682 | 2025-09-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1a8464ce-714b-3837-a8cd-667c94e36d59 | -10.6932 | -46.4453 | 2025-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| ffe42074-9f36-39dc-9801-24b960ece367 | -14.6047 | -49.7624 | 2025-09-21 14:30:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 546c3a57-66e4-3412-b875-edab22538b82 | -9.165 | -44.6273 | 2025-09-21 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 96a1b9a4-ded9-340f-a58e-04d3d23edbb6 | -14.8675 | -45.481 | 2025-09-21 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5062e116-874a-303e-83fd-af9a19cad1f2 | -16.8926 | -43.8849 | 2025-09-21 14:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 5d50e053-a7ca-35fa-9c10-4078983b38ed | -13.2421 | -51.6933 | 2025-09-21 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |


[Clique aqui para ver as próximas entradas](README56.md)
