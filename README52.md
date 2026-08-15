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
| 6ebcb1b1-4942-35ec-8d7f-0455917cf83a | -6.9334 | -43.6333 | 2026-08-15 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| ad171fe9-1834-3ff6-a0ce-7564bba86013 | -11.9347 | -46.3244 | 2026-08-15 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 200bbeda-ee61-372c-a577-9f2577112c42 | -12.4456 | -46.6811 | 2026-08-15 13:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e9872671-1ffa-352e-b015-d0b92fd9c23d | -13.2807 | -54.1814 | 2026-08-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 70bf714d-2674-33b1-a455-395e33fc97fa | -13.2616 | -54.1835 | 2026-08-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 681c2a56-85b6-3121-aac1-a4e9ccadf247 | -11.3992 | -46.3532 | 2026-08-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a896aea2-00e4-3024-a636-9b48cef8c95e | -6.9334 | -43.6333 | 2026-08-15 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 0b5db803-6239-3cff-89e3-b55d9dddf8b5 | -11.9347 | -46.3244 | 2026-08-15 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5bb61f41-1cf7-3925-9842-c9ecd7bed1e9 | -12.446 | -46.6584 | 2026-08-15 13:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 287.0 |
| c591a912-edc1-386b-8585-e609a3101a1b | -10.9743 | -50.5505 | 2026-08-15 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 72908e40-0e2b-3d80-8638-7e34c0e93141 | -14.9792 | -46.6145 | 2026-08-15 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 50e41ca8-8afd-3d66-97b0-58a0aafb76ea | -6.9145 | -43.6351 | 2026-08-15 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 629f21f4-6d80-3349-85e1-9200989d8722 | -7.2786 | -44.7091 | 2026-08-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 289e683b-68ea-3711-bf9b-2f1d0d2f59d7 | -13.5507 | -46.2615 | 2026-08-15 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 0b814d28-e7e8-3cc6-964d-018282376a51 | -11.4184 | -46.3506 | 2026-08-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| c0d75e86-a40f-3790-b5d5-add446fbbd15 | -7.26 | -44.6879 | 2026-08-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 96294f8c-244a-350d-9afa-71e3f5e7fca0 | -9.9896 | -53.9404 | 2026-08-15 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 596fd060-8bd8-3b87-982a-8f78950768cd | -6.9336 | -43.6101 | 2026-08-15 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 93252b4a-2c06-3453-937e-c822785bc7bc | -11.3996 | -46.3305 | 2026-08-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| bdf26cb1-1b21-3ef0-afcc-cbc7647208a8 | -7.2788 | -44.6862 | 2026-08-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 9fcba57f-d43a-324a-80aa-6717cd12d7a0 | -13.2613 | -54.2042 | 2026-08-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 3ea1e447-a243-3237-89e3-c277ec6e48c8 | -13.5511 | -46.2386 | 2026-08-15 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f19e0c44-2bdb-37a9-afec-c0b26a2b767e | -6.9331 | -43.6566 | 2026-08-15 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d9eb2521-5ac5-363a-b444-02f672ec4644 | -13.2804 | -54.2021 | 2026-08-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 3d0bbd82-1590-32cb-8b17-f17b923922bf | -10.5281 | -44.8492 | 2026-08-15 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a9f4639b-b69d-3659-90c7-a0ffff5525db | -13.5507 | -46.2615 | 2026-08-15 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 181.0 |
| ea12fd26-fd78-3ff8-9d07-fbf3dcaea943 | -6.9334 | -43.6333 | 2026-08-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 4f37ee91-2de0-3536-b9b9-cccdc5f141bd | -9.9708 | -53.9419 | 2026-08-15 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3ae8baf3-4d47-36c8-9f56-eb7a824978ca | -13.2613 | -54.2042 | 2026-08-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 5b1623d5-84d5-3009-9978-515a7da834b1 | -6.9331 | -43.6566 | 2026-08-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d43da669-4d38-3013-b033-22875ac013af | -11.4184 | -46.3506 | 2026-08-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 1266074f-9c57-323d-b439-beaca8d952c8 | -13.5511 | -46.2386 | 2026-08-15 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c38c38e7-5810-3b2e-96c4-07ba0c9d5e4e | -7.2974 | -44.7074 | 2026-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bceb4c07-854e-3c46-bda3-933843cbc6f4 | -11.418 | -46.3733 | 2026-08-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ca267b95-bc87-310f-91df-4cce32c1b5d5 | -11.0803 | -47.2255 | 2026-08-15 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b305c9cf-8362-374f-8760-fef8cff45906 | -11.9089 | -50.2524 | 2026-08-15 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 259eb219-b32e-3494-9af2-7c1cbd52612f | -7.2598 | -44.7108 | 2026-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9059ea90-ea17-3b72-af8b-af27e2fe2bcc | -15.5346 | -52.9866 | 2026-08-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3fbb5ff2-4d1c-3032-b8b8-28dd6017ebc2 | -13.2804 | -54.2021 | 2026-08-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6875bf2b-c3dc-3393-8474-2b7c948d85e3 | -7.2786 | -44.7091 | 2026-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 3658c6bd-a08b-305c-8700-312ab4c72087 | -11.8898 | -50.2547 | 2026-08-15 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 3d287616-d868-37f3-8437-e02ed7a46b32 | -6.9145 | -43.6351 | 2026-08-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 37a599db-c6c2-3146-aef4-6803168262e9 | -7.2788 | -44.6862 | 2026-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 82e43257-eb96-3fa8-9249-8eee2ff634e1 | -15.5152 | -52.9892 | 2026-08-15 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3a8ec7a1-94fa-3d4c-ad93-d7c9ed257a53 | -10.0887 | -46.2493 | 2026-08-15 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 737ba290-15b5-3bb5-933a-c3ea7c8e0499 | -12.4456 | -46.6811 | 2026-08-15 14:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 652180f5-9b61-32d0-8bb7-dd8c96617998 | -11.9436 | -51.76 | 2026-08-15 14:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| ae34a21e-e44e-3a29-9967-b19e4296e23a | -14.4499 | -51.9004 | 2026-08-15 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bcfad5e6-3712-3668-8862-6d72b796cfdc | -7.26 | -44.6879 | 2026-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e7817ea3-9fc4-33ea-9cd1-26777692ca77 | -11.9347 | -46.3244 | 2026-08-15 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a41573ce-827a-377f-a3b8-ab7a1ae90ed0 | -12.4456 | -46.6811 | 2026-08-15 14:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d7757bb0-2891-3c57-a9e1-c015b42133df | -6.9145 | -43.6351 | 2026-08-15 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3b3e1287-0ad4-3da3-a013-421a4e5aa055 | -7.2788 | -44.6862 | 2026-08-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b1dc3a50-9d75-3d29-815a-64e5c11582fa | -14.0994 | -54.5248 | 2026-08-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f0e38025-dde5-3c92-9303-6d55a2808e36 | -6.9685 | -59.2976 | 2026-08-15 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b42b9d42-8690-3c11-8134-429f8eab60da | -11.4184 | -46.3506 | 2026-08-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1458f36c-0709-3824-96e2-7b8e073e39ce | -13.5507 | -46.2615 | 2026-08-15 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 6ed3409e-9ca2-35a9-b320-61cc64eb4e1c | -7.26 | -44.6879 | 2026-08-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b9a5bdd4-a656-34b9-9218-2696b9316db0 | -8.6535 | -54.7111 | 2026-08-15 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| c0a7688f-aeb5-3e80-be53-f18299a0944d | -8.635 | -54.6922 | 2026-08-15 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f7e2747b-ce90-3ffa-8400-2ac464f5ede4 | -6.9334 | -43.6333 | 2026-08-15 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 6181bb47-78ef-3e85-b5fd-d0080d8f48a3 | -13.7053 | -46.2592 | 2026-08-15 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f1e01b51-8c2a-348a-8d43-06831068190a | -13.2613 | -54.2042 | 2026-08-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 589773d6-3270-3d16-a119-73f463bb8770 | -10.0887 | -46.2493 | 2026-08-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 56f40ff6-d1d5-37aa-84bb-062acfeee2ae | -13.6859 | -46.2624 | 2026-08-15 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2ec9a786-5936-3fdc-8867-971c13b35e54 | -11.0803 | -47.2255 | 2026-08-15 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 447658e7-8dfc-347c-a606-16bdc3261df0 | -6.9842 | -45.9134 | 2026-08-15 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7b860df5-0bac-36cf-b451-260154061f89 | -15.5152 | -52.9892 | 2026-08-15 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| eb265b00-e168-36b2-b1a8-1b0df42092b6 | -15.4373 | -52.9997 | 2026-08-15 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e814ae09-664d-307e-bb0b-15253cf591fb | -14.9597 | -46.618 | 2026-08-15 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9d3a33cc-eab3-3c58-b7b9-6ad3fa9ae306 | -11.3809 | -46.3105 | 2026-08-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8b0f639f-c5fd-3a99-87a2-e379c1b1fdd9 | -15.1427 | -50.0313 | 2026-08-15 14:10:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d4c6330f-7f51-3c3b-9162-3206d1c35a57 | -8.6536 | -54.6909 | 2026-08-15 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 317735a8-e681-33db-87e4-7151f972e65b | -9.9708 | -53.9419 | 2026-08-15 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8336fee4-8e11-31c9-9a21-1241fba6481c | -11.3996 | -46.3305 | 2026-08-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0258dc6e-9c94-375d-b446-d04fd3c85fd1 | -7.2786 | -44.7091 | 2026-08-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |


