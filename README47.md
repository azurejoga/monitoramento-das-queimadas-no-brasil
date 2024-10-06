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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d41ac7-82d6-30a4-b30d-709351527a48 | -2.85288 | -50.46946 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50a4dd29-81ea-31b7-b3d9-2a3623d8bc37 | -2.85175 | -50.47605 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95e20de8-4895-352b-b582-97416f69daa7 | -2.84708 | -50.46222 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1df3a770-10c4-314b-9cc9-85922b8bdf71 | -2.84602 | -50.46519 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eef1809b-1d2a-31b3-b752-fd2592b27daf | -2.846 | -50.46847 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50ce5f01-15b9-3804-96e1-2370aa7755e8 | -2.84497 | -50.47152 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aeca31e-bc2b-323b-b989-b12b356ee407 | -2.84489 | -50.4749 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82ed700d-a42d-3887-90b9-fbc265ceaccd | -2.69334 | -49.06872 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90c0dffe-9824-3179-9c7e-fb5efd76759e | -2.69249 | -49.07378 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c149936a-acfb-3ad7-b0f2-1aee2bb3bf46 | -2.68702 | -49.06766 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ecd41e8-fdef-32e6-8f21-bd19f6f303e8 | -2.68617 | -49.07273 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| affa5483-e600-328f-af73-f5d8a7eaef52 | -3.1287 | -49.17794 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ce925d7-5382-30d5-b0ec-ef563ae9ea0e | -2.89679 | -50.71243 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6743fb68-e039-3eb6-8446-7329c3ec719e | -2.89545 | -50.71056 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c869e6f3-e73d-3a8b-8a29-2796c6691df1 | -2.89432 | -50.71705 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 821903c0-f5f6-3e6c-9cb9-781d7ab07b92 | -2.88986 | -50.71118 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3723101-0d84-321c-9a67-e2194a9968f9 | -2.88852 | -50.70935 | 2024-10-06 03:51:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d25d02d2-5a0f-37d3-bc8c-1cb8483e6efa | -7.4735 | -40.1778 | 2024-10-06 03:53:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d51e1cb7-954b-3abd-9fd8-81c20a1cf12d | -6.5087 | -43.78024 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83f5455b-171f-3e18-9edf-a49b7ef49dee | -7.5376 | -44.98654 | 2024-10-06 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 662fd9b7-b656-3d36-b1cd-d35600eaaf96 | -7.5368 | -44.99109 | 2024-10-06 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5d9666f-b388-311e-891b-2c39f06f5e35 | -7.44605 | -44.73861 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cabdb9b6-6e73-37bf-896c-c66c29991326 | -7.44179 | -44.73642 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 224251d2-f8ba-34d5-9559-76a30961ffff | -7.44165 | -44.73793 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1613eb99-1c27-3137-a2d4-d89aa30c93d9 | -7.44104 | -44.7407 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4592e94-3a61-3ed9-8e2f-d0e51b7eb9b3 | -9.42174 | -44.12579 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a65149a-5610-326c-8144-ed93d09b765a | -8.36572 | -43.66143 | 2024-10-06 03:53:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 475f07b8-6e02-3628-980d-216b2aaea329 | -8.1997 | -43.6834 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e08cc815-5a2d-324d-b2b1-8a486e3f746f | -8.19568 | -43.68261 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b905ea2f-2edf-39bb-95f9-1b4277aa3962 | -8.15729 | -44.40641 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e8c7c09-8d00-34a4-a31d-c51d93bc4252 | -8.1538 | -44.40578 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffc21cf9-0900-3380-86b4-79d27aeb5686 | -8.15314 | -44.40977 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e789352-585a-316c-a3e2-b52940f19a09 | -8.15306 | -44.40565 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd165491-b544-3fb8-ba25-81fcffad74fc | -8.15236 | -44.40964 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ba27ec8-8f13-3594-8317-d03315ba5f28 | -8.15095 | -44.41765 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a79f035-9ca2-386d-b14f-ed938ca3d131 | -8.1489 | -44.40901 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6db8f28b-5e99-3588-80e7-04035ad5c2cc | -8.14672 | -44.41686 | 2024-10-06 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db1074ae-9794-30c5-b1ee-a275c856e9db | -7.96128 | -45.00835 | 2024-10-06 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99307170-2e21-3434-87b2-0c3b8397d75a | -5.88824 | -43.97748 | 2024-10-06 03:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59547f4f-9c36-361e-bbdd-5dcf9bebef01 | -5.72503 | -43.79355 | 2024-10-06 03:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05dafaf-cc6c-39b5-b96a-7539398c16de | -5.72081 | -43.7928 | 2024-10-06 03:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24352caf-2936-3163-8aee-0a864e158339 | -4.85158 | -43.17371 | 2024-10-06 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb338b3d-9c90-38f8-a3a1-1cf7575441dd | -9.82422 | -39.49749 | 2024-10-06 03:53:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bba11989-9f8b-33d7-94cf-855909429d2b | -7.73765 | -43.05748 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b11dcb92-0d6f-3904-a188-0db94ee20fcd | -7.7371 | -43.05951 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8beabc13-8f8b-39b6-99b7-50fbc9b3c8ad | -7.73682 | -43.0625 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| bf1cadce-da39-3dcf-b44f-8d601c633428 | -7.73623 | -43.06459 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1e157c0d-25bd-3039-bc73-0d82fb50b490 | -7.73598 | -43.06768 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| c6304208-0cb9-3e16-a899-9bd51abb8851 | -7.73535 | -43.06976 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 16bcbbeb-f7e2-3a4a-8333-c1f65b920db8 | -7.73373 | -43.05683 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c650e861-4696-3820-be01-63c4e93e59a8 | -7.7329 | -43.06189 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c3c8a49-dd40-38f0-b22b-46b544ff9794 | -7.69917 | -42.97491 | 2024-10-06 03:53:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1dc787f4-9c45-3bf3-83e8-cc3ec1325807 | -7.69836 | -42.97974 | 2024-10-06 03:53:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d6edaef1-2ed7-3a6e-b4d3-763d1ab7f0bd | -7.69529 | -42.9742 | 2024-10-06 03:53:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 50e853d1-1b8d-38f5-aaaa-da9204311fb5 | -7.69447 | -42.97907 | 2024-10-06 03:53:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| afc2879f-aeb0-39e5-8770-b483f4c1c1a2 | -7.69365 | -42.98398 | 2024-10-06 03:53:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e4045a7d-2ad4-33ac-803b-fff5b2cd8918 | -6.82895 | -42.8115 | 2024-10-06 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f34483b0-3767-359c-9dc5-69eedc7b049c | -6.82504 | -42.81086 | 2024-10-06 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1e0628b4-87fa-3b92-9a9c-7b6b26ff9485 | -9.41824 | -44.12179 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b203be2-6375-3738-81f4-9cc3a4059962 | -9.41763 | -44.12528 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93e917a8-f2cc-3493-a654-358eab16998d | -4.85098 | -43.17735 | 2024-10-06 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76540eb5-6cd6-37ad-a292-9551eafcefaf | -4.84866 | -43.16575 | 2024-10-06 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a51d2bb-087c-3be5-a47f-075c72737c9d | -4.84806 | -43.16937 | 2024-10-06 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fc394ba-c864-3dc5-8064-54c67085100b | -4.81011 | -42.77098 | 2024-10-06 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3a64177-4b5b-39df-9cbb-f6293b87333f | -4.80955 | -42.77438 | 2024-10-06 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ccdeca5-8564-3d68-8f9a-cb36dfb02c08 | -4.80609 | -42.77036 | 2024-10-06 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6087265-3a02-3f85-8d0d-c5344f104c60 | -10.9277 | -39.48853 | 2024-10-06 03:53:00 | NPP-375D | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8014daa9-62a6-3292-908a-5b1c50591641 | -7.18917 | -34.79613 | 2024-10-06 03:53:00 | NPP-375D | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0adbdefd-df7c-3115-b41f-0ef14d80a179 | -7.0883 | -34.99036 | 2024-10-06 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e70a27c-fb72-3d42-bcb0-ba06a6cc981d | -8.12063 | -35.25197 | 2024-10-06 03:53:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 260af703-248a-3231-9415-c6216cd3f275 | -9.87773 | -36.38564 | 2024-10-06 03:53:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e9905b61-dd1d-3eb4-bbeb-5d097cd0d765 | -9.87748 | -36.38504 | 2024-10-06 03:53:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9da85742-5534-3069-ba17-a962da1afda7 | -10.69574 | -37.05005 | 2024-10-06 03:53:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a3336ea-7702-3451-9db5-5d758cb570f2 | -6.64644 | -42.12365 | 2024-10-06 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c1d820ad-5b0d-36ab-83a7-7b5896844edb | -5.70563 | -35.50276 | 2024-10-06 03:53:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2175fb47-39fa-3f4f-89bd-c2464f7ee44d | -5.34854 | -36.13392 | 2024-10-06 03:53:00 | NPP-375D | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a31751a8-b135-30c5-b21e-9326e21b377b | -6.98059 | -36.51815 | 2024-10-06 03:53:00 | NPP-375D | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86206aed-99c2-3468-8f32-cbc734bf6273 | -6.40363 | -38.01798 | 2024-10-06 03:53:00 | NPP-375D | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 77cc8c55-58b3-3672-a474-40112fce0448 | -7.73975 | -37.97403 | 2024-10-06 03:53:00 | NPP-375D | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26d4569a-4ddc-33d0-a032-232d6f029cc8 | -7.24152 | -38.54144 | 2024-10-06 03:53:00 | NPP-375D | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b332efd8-e551-36d3-abaf-fd017a643ae2 | -7.2382 | -38.54091 | 2024-10-06 03:53:00 | NPP-375D | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d4f3d534-3ee0-314e-9947-b911db0627dd | -7.64427 | -39.94334 | 2024-10-06 03:53:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c787cd7a-629e-33bd-a2d0-f96f0cd88932 | -7.47631 | -40.18203 | 2024-10-06 03:53:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec8ecff1-1492-3cd9-b3eb-64da831cff7b | -7.36798 | -39.17652 | 2024-10-06 03:53:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| beec2976-ae61-364e-aa3b-ed8664f71ef0 | -7.34684 | -39.15875 | 2024-10-06 03:53:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ef3e723-6250-37e5-b414-e1c4fd7c3767 | -7.34628 | -39.16225 | 2024-10-06 03:53:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00548444-6739-328a-8ca4-c4af2f3965e0 | -7.3435 | -39.15823 | 2024-10-06 03:53:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d46fb105-5815-3f80-8fec-77edd5fd69f5 | -7.34295 | -39.16173 | 2024-10-06 03:53:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c6bbd27-c6b8-3d17-b803-d9c8c77eb325 | -6.87249 | -39.20235 | 2024-10-06 03:53:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b782efe1-f1a1-34ba-830c-4fe46b44d3fd | -6.64038 | -39.49336 | 2024-10-06 03:53:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5327d4b0-bbef-343d-9ac4-3a1825664bf4 | -9.34364 | -40.56038 | 2024-10-06 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ff307344-bc16-3d6b-b5d4-962e92265f8f | -9.32585 | -40.6905 | 2024-10-06 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbc245a5-cb9f-37af-ac21-1bad597f0782 | -8.64403 | -40.52437 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5651e444-420c-3e38-a5b1-d02b144cbefb | -8.49841 | -40.55813 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 875e67ec-4c7f-3845-b43c-365423455f9f | -8.49475 | -40.58054 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59e9c730-9386-3b48-afd0-2ea06001af45 | -8.48267 | -40.69788 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12ee0063-0a22-3564-b997-294d55e347ba | -8.41315 | -40.461 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a1650322-e1c2-365d-ab62-fd99595fee40 | -8.40973 | -40.46044 | 2024-10-06 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fbe754d7-676e-3437-9245-3c11186403ea | -8.33804 | -40.62458 | 2024-10-06 03:53:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6da41f9-b23a-37f8-a23b-eaa6f261a249 | -8.33743 | -40.62833 | 2024-10-06 03:53:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
