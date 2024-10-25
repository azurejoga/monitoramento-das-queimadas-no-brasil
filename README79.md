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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 769d4a70-f3cb-3807-9405-dc39937729a3 | -23.81466 | -55.27813 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98fa824a-8bee-31a0-9680-3fd84f96353b | -23.81399 | -55.28209 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 35a87edf-5e6f-3846-b11c-8b737573cf73 | -23.78947 | -55.30196 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 522c6bf0-1b3d-3160-abdc-0fad2ad846b5 | -23.78538 | -55.30527 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 65bccda8-0db1-3f60-a767-41639e007e24 | -23.78265 | -55.30061 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c99d3d85-9201-3324-a1f4-a3a58d9ff45a | -1.1834 | -53.6771 | 2024-10-25 04:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 59531269-bcb1-3a05-ad92-0ceed81ad8dd | -1.1834 | -53.6569 | 2024-10-25 04:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 378ff59d-65c6-354c-94c2-6836982fbc96 | -1.6062 | -53.3087 | 2024-10-25 04:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 22ad9a54-d2f6-3f70-ac42-d4f2b108d0ea | -3.2135 | -46.8063 | 2024-10-25 04:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b7166a5e-b019-38de-b025-980d0ce0ad94 | -3.7575 | -45.741 | 2024-10-25 04:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b9ec24d0-c2f3-337b-b8e5-4152c2a92588 | -3.776 | -45.7626 | 2024-10-25 04:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 7cdd1fcc-433f-39e7-8355-99022ab18a9a | -3.7761 | -45.7402 | 2024-10-25 04:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 279.0 |
| ef78e450-6be2-3d3a-9968-4968a93471da | -3.7763 | -45.7178 | 2024-10-25 04:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 134ab67d-4525-3406-908c-b2baad0a720d | -3.9581 | -46.422 | 2024-10-25 04:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 32ff34f1-083d-3e5b-8e8a-dae088c189d4 | -4.3351 | -48.6292 | 2024-10-25 04:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3558b36b-0769-3e51-9b5f-02313ad01a0b | -5.9788 | -45.3621 | 2024-10-25 04:45:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7af5b61c-5099-394b-bdba-700da549c596 | -12.0012 | -63.9013 | 2024-10-25 04:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5d6d61d0-7570-3f2c-a824-9192c8e44776 | -12.0445 | -63.1356 | 2024-10-25 04:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6ce56026-1efb-374b-a700-7d8eb35573e1 | -12.5167 | -63.0521 | 2024-10-25 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7f9b5ade-4a89-3cf9-8397-4c45bfa933f7 | -12.5356 | -63.051 | 2024-10-25 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4cb03653-e7db-3abf-b08f-0d1ad7085575 | -13.4959 | -61.6203 | 2024-10-25 04:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3799d94b-a563-3cbf-ad77-d74628fddf8d | -15.6594 | -55.9742 | 2024-10-25 04:46:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4aca1133-55c5-3b14-b354-085b044a48b0 | -15.6788 | -55.972 | 2024-10-25 04:46:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| b327b820-f268-3ed2-a621-53f69f1e7c3d | -16.94 | -57.5268 | 2024-10-25 04:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| d58fe376-5d04-334b-b7e0-e49f25338fb8 | -16.9596 | -57.5245 | 2024-10-25 04:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 1174e10a-b416-3ca0-96e6-7d6caec0669f | -16.9792 | -57.5223 | 2024-10-25 04:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 15875330-2cb9-3101-a890-9f2eafa62352 | -17.0381 | -57.5155 | 2024-10-25 04:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 2cce055b-0bea-3c44-8283-e7ad7f5e2444 | -17.059 | -57.4312 | 2024-10-25 04:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 06657886-5be9-3dd4-a0bb-5ad9d0778235 | -17.219 | -57.228 | 2024-10-25 04:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 035e7198-996a-3a30-87ae-6b9f52698f9f | -17.2537 | -57.5108 | 2024-10-25 04:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| f2ca3ea2-db43-34bb-9bc3-fb97e9c3b516 | -18.3199 | -56.2404 | 2024-10-25 04:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| ae53b6c3-6d95-3878-be9d-514b9c1e4adf | -18.3203 | -56.2195 | 2024-10-25 04:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 518dd5f1-e4f9-3278-8dfc-221d3b5d6a5d | -18.3398 | -56.2377 | 2024-10-25 04:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| c682205f-a190-34d5-8f42-4acf4d1c7166 | -1.1834 | -53.6771 | 2024-10-25 04:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6e8a3b46-3ee9-332c-9809-73d41cb09b28 | -1.1834 | -53.6569 | 2024-10-25 04:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7e34d9e2-d227-303a-ab96-0d6422f8476e | -1.6062 | -53.3087 | 2024-10-25 04:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 62297c07-39a3-3f72-91ce-f2804b5fab7c | -3.2135 | -46.8063 | 2024-10-25 04:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5ba45a0a-0100-30bc-a0b9-a4525071496b | -3.7761 | -45.7402 | 2024-10-25 04:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8a0366f5-74e5-3b45-9701-5102845647a2 | -3.9581 | -46.422 | 2024-10-25 04:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 835932a6-c41b-312c-b1fe-2503cf55c628 | -4.3351 | -48.6292 | 2024-10-25 04:55:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e9e3f1e3-c688-36ca-8506-1837e8b2dba7 | -5.9788 | -45.3621 | 2024-10-25 04:55:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ae3dbb5b-f1ba-3996-a5db-5aaaa0436f68 | -12.4591 | -63.1704 | 2024-10-25 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 685bb048-f89a-3540-9c56-f01263486eb1 | -12.478 | -63.1693 | 2024-10-25 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 73b6687d-d97c-3a61-a467-4c8d11bf8d2d | -12.4781 | -63.1501 | 2024-10-25 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ed720048-51ab-3204-abd8-21f3474e7e4a | -15.6594 | -55.9742 | 2024-10-25 04:56:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1179c8dc-608d-3ae4-8435-0acf654434f2 | -15.6788 | -55.972 | 2024-10-25 04:56:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 0cdc5f83-4978-3dab-8e85-a8b2470ad88b | -16.9596 | -57.5245 | 2024-10-25 04:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 38188d13-2e60-3885-82de-29c3d297945b | -16.9792 | -57.5223 | 2024-10-25 04:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 88389eec-310b-37f1-80ae-22a4f2bcd221 | -17.0381 | -57.5155 | 2024-10-25 04:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 3204faa0-cf38-36e6-b6aa-a1ceac51b5ad | -17.219 | -57.228 | 2024-10-25 04:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 8734a102-31d4-3e73-aeb4-f3bcd09491cf | -17.2537 | -57.5108 | 2024-10-25 04:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 30952282-8b2c-3d57-aca8-171d4590a3dd | 3.4782 | -51.24892 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d92d5185-7065-35fe-8b47-e107952ae804 | 3.47534 | -51.25328 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5595f32-fa01-36fa-84fc-2d19cf0bc602 | 3.47248 | -51.25764 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86dd081c-4761-3f19-a99d-01fb968872a9 | 3.47187 | -51.25383 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18a1a41d-b4f4-3bd6-ab68-5cc4ffde81aa | 3.46901 | -51.25819 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc249904-923a-3ea5-86dd-461312633568 | 3.46616 | -51.26255 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22662df8-aa05-39a8-b219-e3ad5a7cc4c3 | 3.46555 | -51.25874 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8b068e9-8921-3d15-b9b6-614ef3026439 | 3.4633 | -51.26691 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1c525338-9790-3609-8754-947b86393e58 | 3.46269 | -51.2631 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f59165e-1a76-333d-af98-50230c7002ef | 3.42195 | -51.29684 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1f514fc-14a0-3d4c-926c-de1c0c1d741b | 3.49326 | -51.25436 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c08ff58b-0e99-3596-b487-fff0fc81207f | 3.4892 | -51.25109 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57615a43-e702-3298-97a7-789846407f51 | 3.48166 | -51.24837 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 71b809ed-87de-37cd-bb99-9b25de8371b3 | 3.4788 | -51.25273 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8b7f282-caad-3484-a655-7723c2ab4630 | 3.41849 | -51.29739 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bebfdd7-4bb3-30ed-a853-6ed59e6a11cd | 3.41788 | -51.29358 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69a2fcf0-544e-3964-8bd7-a098c29697f4 | 3.41503 | -51.29793 | 2024-10-25 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5af6a94-4b1e-39f6-846b-a0acd6a84174 | -1.04736 | -47.61794 | 2024-10-25 04:59:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1eaa19c5-b0ca-3b04-97a1-2ca478c96ede | -1.04662 | -47.62267 | 2024-10-25 04:59:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 791046ea-839d-3626-8b26-4ba912edc750 | -1.04276 | -47.61721 | 2024-10-25 04:59:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1de3956a-45f5-3a90-8cf9-4f6d1df845ff | -1.04202 | -47.62195 | 2024-10-25 04:59:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b22966c-93cc-3b03-a405-970c6744accd | -0.66437 | -49.55086 | 2024-10-25 04:59:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1d3023a-c45e-322a-a372-d0f41d51b173 | -0.22947 | -48.80148 | 2024-10-25 04:59:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1d93f88-2362-3e9f-8e8a-4fb4fc3b4a21 | -0.22528 | -48.80082 | 2024-10-25 04:59:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0625bcf9-ae1f-3265-b932-dea2e7204f40 | 2.63761 | -50.88217 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c484a38d-98da-3393-93fd-3768a5f21aaf | 2.6347 | -50.88674 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1579c297-f006-3eb3-9c93-9087fcc0478c | 1.93415 | -50.88157 | 2024-10-25 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddbf4208-d031-31e4-9755-221490d44278 | 1.93349 | -50.87748 | 2024-10-25 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7db92f7c-5d4b-3136-be41-5687a65d07be | 1.82387 | -50.9553 | 2024-10-25 04:59:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30481aca-15b6-300b-86d8-0c6dfc53b1e5 | 1.8152 | -50.46965 | 2024-10-25 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ceb5ae14-45a9-3e25-ba1c-d8e53840c9a1 | 1.81452 | -50.46534 | 2024-10-25 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d975a796-dc27-34bd-ad75-e8e75d77c3cd | 1.80284 | -50.46276 | 2024-10-25 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b938c649-ec0c-37fa-9a86-4e0e63c01c92 | 1.39602 | -50.66022 | 2024-10-25 04:59:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b65a80c8-6ed7-3775-9e82-6710d0c715a6 | 0.27597 | -50.8699 | 2024-10-25 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dade2423-6a8f-38dd-bc31-5a12c40d7945 | 0.1321 | -51.07293 | 2024-10-25 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e11a0d9f-f692-32ae-8588-1308740af486 | 0.12848 | -51.07349 | 2024-10-25 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b7bc8e-df3b-38d5-a068-aa8ad17f51d1 | 0.00499 | -51.22234 | 2024-10-25 04:59:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8950adf1-1563-3435-8a7b-d16c70f2d4db | 2.8048 | -50.93142 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c00919bf-266d-3fa9-bdcc-1e51b5ecc1e9 | 2.80126 | -50.93198 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f39237a5-6a29-34d8-8b85-c9569b23ed1f | 2.80119 | -50.93136 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70ea9779-d950-3f42-8c68-609e6927c922 | 2.79765 | -50.93192 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b6650b1-c96d-38d1-9f38-0bf0c3a9db24 | 2.35338 | -51.51691 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de51b9e7-4654-333f-a1de-bec98c2974dd | 2.35208 | -51.51781 | 2024-10-25 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98360e24-f84d-3092-992f-e1fa99e6f723 | 1.31984 | -51.25211 | 2024-10-25 04:59:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e262ec0-f355-368b-a4ee-788d0b3a14f8 | 0.54553 | -52.28571 | 2024-10-25 04:59:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b1a6bc4-20fd-342b-a0da-932694dae431 | -0.09389 | -51.63356 | 2024-10-25 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6269fe4-d711-327b-8b62-0c47a1ad1585 | 1.57646 | -55.65881 | 2024-10-25 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74530857-b5e3-3cde-9430-8b420bb611a4 | 1.57589 | -55.6552 | 2024-10-25 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f94c271-4dfd-316a-abf6-55be263aa171 | 1.5725 | -55.65571 | 2024-10-25 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README80.md)
