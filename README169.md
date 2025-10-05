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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02393fb6-27bd-3f94-ad84-f3d3ff1c58c5 | -5.852 | -42.8608 | 2025-10-05 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| b37019ca-fb7e-3224-9eaf-6330a8a336fd | -6.0616 | -42.537 | 2025-10-05 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| aa996ceb-84d1-37b3-a04f-1fb2fd57499c | -10.2212 | -50.3303 | 2025-10-05 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 6a7ef2f8-51f3-333c-a757-99a3e365f7d3 | -10.3419 | -51.2093 | 2025-10-05 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b74f9d65-eedf-3ffa-b41a-9b29dc772116 | -10.1943 | -45.5339 | 2025-10-05 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 278.9 |
| 908c0623-11f7-3ffc-ac52-3f243c317989 | -8.4683 | -45.9106 | 2025-10-05 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c55982bc-d902-3368-96ef-7fee78e484e6 | -8.5576 | -46.306 | 2025-10-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 125e97bb-de91-39c5-bc10-226317f1b2b2 | -11.0911 | -47.7573 | 2025-10-05 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 38233d66-d327-3758-b6e2-5705c78e2c8d | -17.8617 | -57.6024 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 5242bf48-9a36-3efc-8e7e-e4af4394e600 | -8.1702 | -44.1377 | 2025-10-05 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bf01d840-1879-3479-bc4e-a1d94bbab76b | -6.2156 | -44.0658 | 2025-10-05 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b5495046-45fc-3322-850c-1a7a8757c31f | -14.3348 | -47.6981 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 2b70c504-939e-378d-8df8-9f84c1c073b9 | -15.6015 | -52.5102 | 2025-10-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 357.0 |
| fcaeee85-be7d-3684-a17d-95154de83892 | -6.8335 | -45.9932 | 2025-10-05 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8d58d854-ef2f-3f64-a9a1-fd5098e42e8e | -17.9661 | -51.1474 | 2025-10-05 14:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d5b78f5b-1da8-3c06-b307-3a51c63c00d4 | -16.0021 | -50.9238 | 2025-10-05 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7b8f79d1-c488-3f63-8594-ae48ba73bc6e | -7.0369 | -42.78 | 2025-10-05 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |
| a022046a-7fc9-38fa-92a7-a90da6984c01 | -14.5751 | -52.4789 | 2025-10-05 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| c3436bb9-946a-34a9-9d3c-28937bf1cbcf | -1.2085 | -49.1051 | 2025-10-05 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| c11a29c4-50d6-3561-b3a0-cf60775faf70 | -16.0016 | -50.9456 | 2025-10-05 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| c206040f-a85f-3f08-8faf-4ae4f627263f | -15.2208 | -56.821 | 2025-10-05 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9815c794-340a-3519-a94c-b5f8bbc3a4ca | -5.4734 | -43.2646 | 2025-10-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b6ed0957-9820-3db3-b697-52ec22a019e3 | -11.5091 | -54.4824 | 2025-10-05 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| adf99e1a-481e-3fc7-8f20-4e3ce3c3f482 | -9.3276 | -54.5215 | 2025-10-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| e7d3a2f5-c205-32a1-88de-5032a2a3702e | -12.3154 | -55.1416 | 2025-10-05 14:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 8f8c728e-63f1-3e0b-a1cb-adff48eb1e20 | -10.3721 | -50.3363 | 2025-10-05 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 3c882dd2-acaf-3a9a-8955-345ff1b118c2 | -10.1946 | -45.5111 | 2025-10-05 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 36b2d281-6319-3c8d-9b50-b90c57b366d2 | -11.2238 | -47.7851 | 2025-10-05 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b9c3f984-2294-3d01-a3b7-6ac6baa1eb95 | -5.9692 | -44.3612 | 2025-10-05 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6b32b1c9-58e2-3cd9-b2ad-008986c7e22e | -11.1165 | -49.8707 | 2025-10-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7bef722c-7fea-3783-bf12-97b3dd1164fc | -11.0978 | -49.8513 | 2025-10-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7b873c95-e72f-36dc-8a95-cde4270622b4 | -12.2967 | -55.123 | 2025-10-05 14:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 176736ec-c4b5-3911-888c-fa5da2ae7f28 | -11.8033 | -45.0856 | 2025-10-05 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 233.3 |
| d0c07998-81eb-3294-876a-fcf1aa7168c5 | -14.5561 | -52.4601 | 2025-10-05 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c67d56f1-443d-34a3-aec9-73e46612ec67 | -9.9313 | -50.8898 | 2025-10-05 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 5954bff4-730d-3ff1-b8f2-63d2e3acef1a | -6.6129 | -43.7317 | 2025-10-05 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 345.3 |
| 5ddde52c-1c81-360a-92f2-7df32d1f6efd | -7.8121 | -47.3759 | 2025-10-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| bc231037-57c9-335c-be63-eb85a71c255d | -9.2439 | -51.8133 | 2025-10-05 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 248cd736-c27c-3b2f-b0de-7b6cf0dc0b83 | -5.8069 | -45.7796 | 2025-10-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 216ecf20-95c9-36f6-bb2c-97a9041262a2 | -8.5953 | -46.3022 | 2025-10-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9ddc80c5-6220-31e6-9676-d2f9710cc259 | -9.0124 | -50.7199 | 2025-10-05 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 526ae2a3-0ca5-37e7-8250-962586cde2c2 | -8.8618 | -46.0949 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| efda2761-e834-3c0a-ac1b-380833745ac2 | -11.1168 | -49.8492 | 2025-10-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| f1c35ebd-9ad0-3185-acf9-932f7cb273e1 | -12.5733 | -48.1393 | 2025-10-05 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b4339f7c-d25f-3e67-97a0-88a634992311 | -8.6139 | -54.9558 | 2025-10-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 32ccaec7-ad59-3945-a165-faf120732b88 | -10.3907 | -50.3557 | 2025-10-05 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 33d61740-c1c3-3723-9974-a3c114450d11 | -5.7882 | -45.7809 | 2025-10-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e6150a13-77a9-3867-b94a-86299162b0ff | -5.9229 | -43.3003 | 2025-10-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d5123cbd-3b6a-3a9e-be50-7f38dcf11248 | -6.8148 | -45.9947 | 2025-10-05 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 194eb5ad-814b-3592-bd99-2a089126de9e | -17.9006 | -57.6388 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| b3753b00-288d-3964-86a1-df23b5fcc713 | -8.5578 | -46.2836 | 2025-10-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f3e8478c-e533-3e2b-8dc4-39f03c21996d | -6.6069 | -44.3098 | 2025-10-05 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3643bf98-1adc-304c-b808-023168da8c06 | -6.7167 | -42.8101 | 2025-10-05 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 50fa3f66-49bf-3ccd-a455-892afe6dc1c7 | -10.8093 | -48.8229 | 2025-10-05 14:40:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 6cbe6753-9f8c-3e4f-b944-2e7e3c69bab3 | -10.1497 | -45.9709 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| eaebf878-d4e9-3eec-8b54-302679163fda | -12.5926 | -48.1366 | 2025-10-05 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 29a06302-90c1-3620-a2ac-5a9880e34a0a | -11.4535 | -51.5177 | 2025-10-05 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 28a9e66c-6285-3c32-b4c7-35168b99001b | -8.8991 | -47.6042 | 2025-10-05 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2c9d6067-7d42-3fd7-9d46-1d4e0902d8a3 | -17.8614 | -57.623 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| abf6bb7e-f6a3-3627-a6fc-dbcb7b493234 | -13.2552 | -47.5962 | 2025-10-05 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b604452f-1a33-3602-a48c-926fcec84567 | -5.9879 | -44.3598 | 2025-10-05 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3117b5e7-890f-3c9e-94c1-916258798c38 | -7.5332 | -43.8319 | 2025-10-05 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4b103339-1f75-34e7-b362-f45a379ec5cf | -17.9404 | -57.6134 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 1578b3f3-b6fb-3223-b391-5d4f39aa1f94 | -18.1769 | -53.3669 | 2025-10-05 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 73c614c6-4296-3c7a-a971-607f3951cf34 | -9.2973 | -46.0026 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 2c42a93f-cac9-3d4d-a2d4-4aef0a1ff662 | -6.6416 | -42.7934 | 2025-10-05 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 5d811620-1fde-34c2-9adf-423ab406186c | -14.3158 | -47.6787 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 137.3 |
| ec5ecdb2-d591-38a5-bde0-362e158496ea | -7.4464 | -46.5223 | 2025-10-05 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5790e00d-009a-3ac8-bcf1-b33552c3ce77 | -5.8439 | -45.8219 | 2025-10-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e370f35c-6c0a-3dd9-a9c5-4192bb456e05 | -16.3627 | -51.4752 | 2025-10-05 14:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6ef691ff-fd97-3587-88a3-a387f3ee0ba6 | -9.1713 | -49.9622 | 2025-10-05 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fe6a2fa6-dd46-3bd9-9dfa-c57384c18f08 | -6.4161 | -44.6466 | 2025-10-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0a23f5e0-e765-375c-a5c0-c9395cf5454e | -21.6888 | -50.0559 | 2025-10-05 14:40:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.9 |
| db3fb706-2416-3444-9370-bc3f71afb361 | -6.1966 | -44.0904 | 2025-10-05 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ccb3bad8-989b-358b-b942-405937dc9462 | -7.0558 | -42.7782 | 2025-10-05 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 74a76e5c-e89d-38cb-ac58-ef34df154f52 | -6.4134 | -43.0489 | 2025-10-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 1f4c3e26-8840-3e25-8188-e846760588a4 | -11.2429 | -47.7827 | 2025-10-05 14:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ea1ad64c-1e26-3d3f-9d52-8de3edda0897 | -7.6622 | -47.367 | 2025-10-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 99ff9f3e-4c26-3a15-aa54-ce1c9c406aef | -6.2408 | -45.3424 | 2025-10-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d10afac8-3cbd-33d4-86a0-af8294b43377 | -6.7048 | -42.1712 | 2025-10-05 14:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| d248d6f8-58d1-32de-bc32-3383d37c9d5e | -8.5405 | -47.7051 | 2025-10-05 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 46a4315b-ed2e-3d7b-91f5-744b060c1520 | -5.9584 | -43.5072 | 2025-10-05 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 750b603f-f49c-3ee1-a5f0-3c3f6654043c | -10.5838 | -48.696 | 2025-10-05 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fc355c07-db1d-3e36-8a3c-99904aa46d87 | -16.077 | -51.0859 | 2025-10-05 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 65dd1c58-5893-3ce6-9ade-4b62fbcc4241 | -5.8764 | -44.2764 | 2025-10-05 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a0805d13-6482-3dd9-a80f-68e28b8f7bb5 | -3.6205 | -43.6322 | 2025-10-05 14:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d938a082-5e58-3567-be2a-ff0425a19e8a | -5.8256 | -45.7783 | 2025-10-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d68baa03-2120-3caf-8f3e-a098a75a20a3 | -12.9103 | -54.7352 | 2025-10-05 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f3c55a1e-b918-3d79-9a6d-876a8959f82f | -5.4556 | -43.1491 | 2025-10-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4397a94e-9aa3-3ab8-8cdc-b80872b65e93 | -5.5691 | -45.1878 | 2025-10-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a3d39c73-23bc-34e8-92ce-545a6e25c377 | -11.0975 | -49.8729 | 2025-10-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2e5eb316-347b-3506-9891-085572d0eba9 | -12.5487 | -54.7307 | 2025-10-05 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| fa0bb722-0563-38e1-8ac1-8696ca654044 | -8.5581 | -46.2611 | 2025-10-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8213ecc9-8cc1-3021-b7f2-2a219d858b64 | -14.1611 | -53.0377 | 2025-10-05 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c06d5fe5-5aee-3000-9e96-b19c31c781ff | -10.3605 | -51.2286 | 2025-10-05 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 56a8dc05-fb23-34fa-a508-061436a318e7 | -8.541 | -47.6611 | 2025-10-05 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ca49ebe3-ff49-30b9-92da-bc79ee12d568 | -11.5301 | -47.6798 | 2025-10-05 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c75d758c-337c-3acf-8a5e-e23e742420a4 | -7.646 | -45.4489 | 2025-10-05 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 64ec9141-a6b3-3a82-93a8-d911fead43e0 | -8.6138 | -54.976 | 2025-10-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 642df1dd-2d89-3751-b058-07053c55cd6f | -8.1705 | -47.2112 | 2025-10-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |


[Clique aqui para ver as próximas entradas](README170.md)
