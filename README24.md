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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14e61052-2d0b-3127-98f8-77cc4119b779 | -18.0851 | -57.2249 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 23954238-edb9-3f2d-93a3-81b9297b1c91 | -18.083 | -57.3489 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 1098d7b0-8912-32d3-beb8-878863d55825 | -18.0827 | -57.3696 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 9670ca7d-7483-374e-b764-48e286597fd9 | -18.0653 | -57.2274 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| ddf3f9cb-8aad-37a1-bc29-b6c092b88684 | -18.0629 | -57.3721 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 919229d4-fadd-3b38-8fd2-54ab00825291 | -18.0431 | -57.3745 | 2024-10-26 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 1fefbdc1-25c8-312f-8d83-446f9cc4fc01 | -18.2649 | -55.9975 | 2024-10-26 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| e3f090e7-899a-3313-b96c-aabf871e42a4 | -5.15145 | -37.74306 | 2024-10-26 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0257c1aa-9dab-3d23-be66-f5a14386d58d | -5.14494 | -37.74187 | 2024-10-26 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 964478c6-bfe0-3c69-8aa6-53ee2942dfbb | -6.71182 | -37.50663 | 2024-10-26 03:02:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f4056492-df2a-3870-bfc9-b6c05843d740 | -6.97495 | -39.25304 | 2024-10-26 03:02:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72326300-446b-3a91-bae0-e0badbe65ac7 | -6.9681 | -39.2514 | 2024-10-26 03:02:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f538330e-3985-3ae6-9df0-299cb9b9a809 | -8.88975 | -36.23901 | 2024-10-26 03:04:00 | NOAA-20 | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 57737626-b230-3a42-9ac8-8a45e22e0c21 | -8.88908 | -36.24269 | 2024-10-26 03:04:00 | NOAA-20 | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 408d2bc2-2f97-3d5e-a4fe-6806cd93dc3b | -8.20873 | -35.29098 | 2024-10-26 03:04:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3b9d464f-7cac-31a3-9ce9-ec5d70be0bef | -8.20816 | -35.29416 | 2024-10-26 03:04:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d1d29dd9-0c49-3084-8e48-a4783cd88387 | -8.20697 | -35.29161 | 2024-10-26 03:04:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 17b6384c-2d03-38f8-88ba-9a94c1f7b8b9 | -9.74806 | -36.32666 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 49716a02-80f6-34ec-8129-a487ffe1a41f | -9.74736 | -36.33045 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0cf01648-7261-39c1-82cc-ded014d6f241 | -9.74725 | -36.32677 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 4e130fcc-5d7d-348d-ab78-f74366d121d5 | -9.74662 | -36.33448 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| ed9d7ad6-e6a6-399e-9faa-3a521fbc57a7 | -9.74652 | -36.33057 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| dfd09685-1a7e-3ae4-9c7a-1ec32903dfee | -9.74592 | -36.33833 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| f455aca0-0997-34e1-a3cf-6ba109ac0909 | -9.74575 | -36.33458 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.7 |
| 71c62db9-1dd3-34af-a95c-2832d5a83921 | -9.74527 | -36.34184 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 540f8db2-180e-3c7b-aec9-9a020b92abc6 | -9.74502 | -36.3384 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.7 |
| e908b7b1-9cd3-381e-b7b9-187743e69a16 | -9.74434 | -36.34192 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2b140090-e728-31b4-8052-8b8680068177 | -9.74254 | -36.32554 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 74bae065-5ef1-3a9e-b876-794a0cf74d50 | -9.74185 | -36.32927 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| a3e1f72d-a0ff-3284-ab79-556855a526bd | -9.74172 | -36.32568 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| c6e337d6-4d35-3092-83c0-2cd19bc60a9f | -9.74114 | -36.33315 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| e59ef215-a5d4-3504-b8cf-0a22f0159fc1 | -9.74101 | -36.32938 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 00c5ac7c-cf5b-37b3-b51c-fb8b28427951 | -9.74043 | -36.33699 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| 171d3d50-f584-3874-a680-4af5c8fe3465 | -9.74027 | -36.33323 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.7 |
| e49fa0d0-486a-319f-b386-86bbd7fbe900 | -9.73974 | -36.34071 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6844a4cb-f1e4-3a79-b8fa-b48c9cd72ef1 | -9.73954 | -36.33706 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.7 |
| 66957806-e338-3ebe-bce8-9da034680534 | -9.73882 | -36.34079 | 2024-10-26 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17c7625b-e763-3b5f-a3fe-9a6ce22c0e22 | -8.20725 | -39.83485 | 2024-10-26 03:04:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bcf365cb-8b91-3f4a-9b2c-5c04f1fed146 | -8.20592 | -39.84153 | 2024-10-26 03:04:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| de342364-510f-38d1-90a5-3395db1ebbcd | -8.20144 | -39.83876 | 2024-10-26 03:04:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 33a5e6ac-d28e-3e87-bb7e-d850ac535e59 | -9.62568 | -40.5887 | 2024-10-26 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d38ceafb-0af8-3cf7-8dc3-ca6693a836b5 | -9.61856 | -40.58718 | 2024-10-26 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fcb91e00-1561-3ffd-9e7b-bf54c27ee244 | -2.1929 | -53.7234 | 2024-10-26 03:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f13d8134-ecec-362e-b297-ec489429ead9 | -2.8923 | -53.3247 | 2024-10-26 03:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3cb5a89c-4893-3fd8-b0e7-f191d6100cd9 | -2.9501 | -52.5708 | 2024-10-26 03:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 1e2543ac-cd89-3423-8e9a-b7640178c005 | -2.9944 | -50.5025 | 2024-10-26 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b1ae26a4-c5e9-35bd-a180-2c4eeadfdc79 | -2.9945 | -50.4816 | 2024-10-26 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 6f1e6108-41f0-32d5-8e3e-ac0575f4d04a | -3.0129 | -50.502 | 2024-10-26 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f0f745f7-8863-34dc-a00a-a00a7dc689b7 | -3.013 | -50.481 | 2024-10-26 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| a9f6fe2a-a266-3bad-a117-a8061ec8e386 | -3.4729 | -43.3377 | 2024-10-26 03:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 546a04e0-8471-3875-ac5a-ec1850f63bd3 | -3.473 | -43.3144 | 2024-10-26 03:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 42489108-f021-3bc3-a70d-573b1b3d0abf | -3.4915 | -43.3368 | 2024-10-26 03:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0630ca7e-01c1-3d3d-a5e3-17cfb9f2fb8f | -3.6084 | -45.8147 | 2024-10-26 03:05:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 4da3d35a-68fa-3f03-b82c-a44b9a260cd6 | -4.5613 | -48.0358 | 2024-10-26 03:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7196d95f-e643-33be-81fd-0aa272ac1757 | -4.5799 | -48.0349 | 2024-10-26 03:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 220.6 |
| 9758ee6f-4f3e-3fa3-9971-10438b7ec474 | -4.58 | -48.0132 | 2024-10-26 03:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 76a86f85-54f4-393c-8a46-5e9b7d63bef2 | -7.6474 | -63.4584 | 2024-10-26 03:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 37349380-5c63-37b1-b783-450dfd13c209 | -18.16011 | -42.45326 | 2024-10-26 03:06:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 451cbe5b-e34f-3337-8b8c-03c872f48681 | -18.15899 | -42.4586 | 2024-10-26 03:06:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 377ef61c-513b-3e91-b539-4cb8daaddd25 | -18.15851 | -42.4601 | 2024-10-26 03:06:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 37e2c7ce-6166-3676-95d1-2eed6bb7bbc1 | -16.02209 | -41.18937 | 2024-10-26 03:06:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4b88acd6-0755-38f2-a25c-1c38534050f6 | -16.02059 | -41.19608 | 2024-10-26 03:06:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4499f669-1312-305e-85b7-8decc4f609a7 | -16.01748 | -41.19477 | 2024-10-26 03:06:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 08571ee1-47cc-3686-a53d-e143b24c4d0f | -18.1606 | -42.45189 | 2024-10-26 03:06:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3921bdb2-56d0-3f85-8478-df5964372355 | -16.9012 | -57.5108 | 2024-10-26 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| a12113cb-c7cf-3945-ab9d-f883b7d22e27 | -16.9207 | -57.5086 | 2024-10-26 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 6b437711-e933-3e53-a93d-1ff82e2c4783 | -17.0499 | -53.452 | 2024-10-26 03:06:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b7954b71-901e-3f7e-990f-14ddeb36c0ab | -17.254 | -57.4903 | 2024-10-26 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 81f6bf0f-cdbd-330c-a7b4-f38d1c7e90c8 | -17.6865 | -57.4798 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| bed5e282-c56b-3bab-adba-2c023100abc8 | -17.7443 | -57.555 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| e45fe675-0fa1-3bcb-96e9-238aee89a7d5 | -17.7446 | -57.5344 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 352042ee-cb1d-37d0-9018-6fdcd2a9c201 | -17.745 | -57.5138 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 55d17f89-9f7f-381d-915c-3fed1ffc55b2 | -17.7868 | -57.3649 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 421f528d-e6a5-3b55-a4e6-f00e64d91529 | -17.7872 | -57.3443 | 2024-10-26 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 10a50ab1-cfc2-3154-83fd-a39aa4c4bedd | -17.843 | -57.5431 | 2024-10-26 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| e5dd57fa-3993-389e-9d1e-c37172f8c9ec | -17.9217 | -57.554 | 2024-10-26 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 6bbb5ca9-b7e7-3620-9ad4-412376f4c2b0 | -17.922 | -57.5334 | 2024-10-26 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 953fb5a3-1456-39e7-8406-455a95b55e8b | -17.9415 | -57.5516 | 2024-10-26 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.0 |
| 999765d3-4dc8-3d47-83ec-31e6362a5161 | -17.9418 | -57.531 | 2024-10-26 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 35386c32-5c86-3f4f-a579-97486bec0156 | -18.0629 | -57.3721 | 2024-10-26 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| db27c7f3-8fe2-3410-b4a0-f9ff10171dcc | -18.0653 | -57.2274 | 2024-10-26 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| eea9e5a2-53ce-3bff-9921-962aa94d9418 | -18.0827 | -57.3696 | 2024-10-26 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| d0950b04-22e0-3990-b456-24eb84237b26 | -18.083 | -57.3489 | 2024-10-26 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| bb06bfb3-2a1a-350e-a771-86abed76e87b | -18.0851 | -57.2249 | 2024-10-26 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 59ba0b15-980c-3076-a12e-56e7cf5662d9 | -18.245 | -56.0002 | 2024-10-26 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 81ba7789-c401-3179-8505-6cb2fb2ab66e | -18.2649 | -55.9975 | 2024-10-26 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 2bad71d2-8ab3-3cba-8b42-3690bf2f1c45 | -19.5067 | -56.6829 | 2024-10-26 03:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| dde14723-0c58-3a6e-9441-e6d36359dfc9 | -19.526 | -56.7221 | 2024-10-26 03:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| cf9ac795-040e-3637-95f0-f85a23fbdb2a | -19.5264 | -56.7011 | 2024-10-26 03:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.7 |
| 9af18764-a170-3297-b49d-4d9bb3921bc5 | -19.5461 | -56.7192 | 2024-10-26 03:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| e4d7ccff-09df-33e9-ab1c-a2cad41693d2 | -19.5465 | -56.6983 | 2024-10-26 03:06:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 8e219503-6e2a-3fb8-adce-86355dbfd98b | -20.85274 | -42.89526 | 2024-10-26 03:08:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f588751d-3501-3def-b1c5-b4e1ecbd47be | -20.84622 | -42.89307 | 2024-10-26 03:08:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2f3cbb4b-22b9-36f8-afd6-f167aece8004 | -2.1929 | -53.7234 | 2024-10-26 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 0803bbc1-5053-3bec-a7f2-f88afb144061 | -2.9944 | -50.5025 | 2024-10-26 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d4fa6f3f-231d-39b9-9f50-f0f3ca8e6447 | -2.9945 | -50.4816 | 2024-10-26 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d5cca41a-d415-3aa2-81f0-fcd0ab3a9564 | -3.0129 | -50.502 | 2024-10-26 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f4afd1e3-a041-3ada-a994-67c440f817a5 | -3.013 | -50.481 | 2024-10-26 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d45e85c7-a5b7-33a5-86b8-a1dbdb8317c1 | -3.4729 | -43.3377 | 2024-10-26 03:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| ed9c1053-081a-3f53-8ee7-564b3cf99acf | -3.473 | -43.3144 | 2024-10-26 03:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |


[Clique aqui para ver as próximas entradas](README25.md)
