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
| 2c55fafa-597f-384d-910c-75c63487b811 | -10.86117 | -44.43491 | 2026-07-10 06:40:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0f881afc-86b6-3424-87a1-8a57cddff224 | -8.72478 | -47.83915 | 2026-07-10 06:40:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4c6aedc-aa39-33de-9817-2d06b60a73c1 | -11.83512 | -48.2357 | 2026-07-10 06:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c897369e-b0c2-3101-a5d3-b373325283be | -8.50605 | -48.06371 | 2026-07-10 06:40:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3b639da-d767-3e18-b824-bcf40749b66f | -12.35367 | -47.4094 | 2026-07-10 06:40:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ecd3e2fd-0ef0-3ebe-ba12-7603bb12ebc3 | -21.76329 | -56.29855 | 2026-07-10 06:42:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5adc04b3-d838-3769-99e8-5f54f0a5b188 | -13.264 | -45.1343 | 2026-07-10 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f15f0313-feff-38a2-bf1b-971d7844d9c8 | -13.2645 | -45.111 | 2026-07-10 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 6f638647-910f-3019-a8d1-3347aa1c3ede | -13.264 | -45.1343 | 2026-07-10 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 07afa310-9e14-3e99-9ecf-7c2e8451ca86 | -6.49895 | -42.20072 | 2026-07-10 11:04:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 83d0e091-0347-3232-bc77-a3b7b28f07f9 | -5.72647 | -38.59549 | 2026-07-10 11:04:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f452b8be-6d3b-3daf-9781-a4327f96f6ec | -8.92037 | -39.92291 | 2026-07-10 11:06:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 56200e10-74d4-3429-af11-da5f04637113 | -13.26108 | -45.14774 | 2026-07-10 11:06:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 24100852-ac99-3518-87d5-4cdd580953ae | -8.70266 | -36.81099 | 2026-07-10 11:06:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dd7f4ac6-7442-30da-b999-6cd9048a3f4e | -8.92229 | -39.91039 | 2026-07-10 11:06:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c54654a7-3593-3930-8d93-07c5c5252b9d | -13.94295 | -42.99222 | 2026-07-10 11:06:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6f5f37aa-1181-33be-96fb-b5067c192bef | -13.25945 | -45.14021 | 2026-07-10 11:06:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 5ea437bc-f14b-3602-9db6-ab6a4a1a79ce | -18.94666 | -40.01531 | 2026-07-10 11:08:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 33100806-f027-389e-abc9-3cdf10aee57f | -18.94514 | -40.02525 | 2026-07-10 11:08:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 2a4de94a-ed37-35c9-af92-d1ec868569b8 | -13.264 | -45.1343 | 2026-07-10 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 70136d9f-da89-3c5b-9aae-28aa8df93fdf | -6.0487 | -43.8712 | 2026-07-10 11:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 235a48bf-4bc6-3e70-8a95-d7fda0379a89 | -13.264 | -45.1343 | 2026-07-10 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 180.3 |
| f6af1e12-d543-3776-b0a5-bc7bc2579311 | -6.0487 | -43.8712 | 2026-07-10 11:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| c53dc923-908a-304a-a92f-576651a2f8e3 | -6.03 | -43.8727 | 2026-07-10 11:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f693e8d1-42c4-32e7-ba48-11aa4d83d6f9 | -6.0487 | -43.8712 | 2026-07-10 11:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 65a68c4b-ced8-302a-9477-3bfadff897f5 | -13.264 | -45.1343 | 2026-07-10 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 7d56fff0-6582-329a-a2c7-599f13d46ad0 | -6.03 | -43.8727 | 2026-07-10 11:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 15ddc26a-6af6-3a71-ad15-f8addefa8684 | -6.03 | -43.8727 | 2026-07-10 11:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 14a95692-9cd5-32b8-b9f5-a3d22e0a878b | -6.0487 | -43.8712 | 2026-07-10 11:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 025f1bb0-c8c7-38c6-b07e-a5da72b83f82 | -13.264 | -45.1343 | 2026-07-10 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 10e5b9d0-f219-37ea-b34e-0ce07bbabf9a | -6.0487 | -43.8712 | 2026-07-10 11:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 2250bb37-1740-36c0-b525-dc3c4ffa8704 | -13.264 | -45.1343 | 2026-07-10 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 540a92d2-ee41-3347-84f1-d15c205d04ba | -6.03 | -43.8727 | 2026-07-10 11:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 99cf6c0b-ce87-39fa-9224-d2db52d42ce6 | -6.0487 | -43.8712 | 2026-07-10 12:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e88fd5e2-1471-3283-861c-ca6b85164fb9 | -13.264 | -45.1343 | 2026-07-10 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 4df532ea-dd3b-3a26-b3f7-365970ff07ed | -6.03 | -43.8727 | 2026-07-10 12:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 504b21d0-7976-3df5-8744-04708b731429 | -6.0487 | -43.8712 | 2026-07-10 12:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9412b350-c909-3655-84b1-58e6859ef410 | -6.03 | -43.8727 | 2026-07-10 12:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 4c06548f-7719-3af7-acc3-559c53134ce5 | -13.264 | -45.1343 | 2026-07-10 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| c42d50eb-5b07-3497-95c8-86f86072f5c2 | -6.03 | -43.8727 | 2026-07-10 12:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 2baec12b-8330-30e3-b81b-c00e02ebb92b | -13.264 | -45.1343 | 2026-07-10 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| c13d1e62-4f76-3ec7-b2e1-b2ee97b26fae | -6.0487 | -43.8712 | 2026-07-10 12:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ad5963c0-552c-3798-a36a-c0f2370254b9 | -13.264 | -45.1343 | 2026-07-10 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| dd80ab08-d630-3d5b-aa0e-c8583ef21701 | -6.0487 | -43.8712 | 2026-07-10 12:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a6535556-b3c5-3d98-b247-c5adae857ec5 | -13.264 | -45.1343 | 2026-07-10 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.5 |
| a423664f-44bf-39e7-ae4b-f55867b11ac8 | -1.88678 | -54.11034 | 2026-07-10 12:42:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ac6fa349-1630-30e9-adf2-20682519f752 | -11.64251 | -52.84765 | 2026-07-10 12:44:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9b2d0aad-87fb-350a-bb10-b8fd42667f69 | -13.36753 | -54.36266 | 2026-07-10 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| ef002135-ef51-393d-8f31-2ae764aa5e5f | -8.7289 | -54.56368 | 2026-07-10 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 831f2e89-0911-391a-b3d3-ab437f92c593 | -10.1662 | -50.2078 | 2026-07-10 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bca3c3c5-f354-37c5-bc34-b731147c7ba6 | -13.264 | -45.1343 | 2026-07-10 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 43c2bb25-6bec-3ca1-944f-f5a2fb9ced30 | -6.0487 | -43.8712 | 2026-07-10 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 06b3ee1c-2515-304a-bc46-536477d8fbb4 | -13.264 | -45.1343 | 2026-07-10 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| b3c36a6d-2d47-39f1-946b-c8d3a419fc64 | -10.1662 | -50.2078 | 2026-07-10 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2f8420b1-3f72-3387-ae07-093f1a669b69 | -10.1662 | -50.2078 | 2026-07-10 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c82155e2-1a73-3e63-9454-6caaa0ef9230 | -13.264 | -45.1343 | 2026-07-10 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9522f3e4-6874-3dac-a4a9-e04e32820598 | -10.1662 | -50.2078 | 2026-07-10 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b32bccaa-9b33-356a-9c6e-3c21c80ca47e | -13.3737 | -54.3572 | 2026-07-10 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| c94a5b06-867a-3c00-b90c-30b3dcd289a7 | -13.264 | -45.1343 | 2026-07-10 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| ff686e07-8875-39a5-b8c2-a7bb8c1720d9 | -13.3734 | -54.3779 | 2026-07-10 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 5a3beba1-eeec-3428-b7b4-6ff46d3cd26e | -13.264 | -45.1343 | 2026-07-10 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 9ced7522-96fc-34f1-809e-5e6492e6627d | -10.1664 | -50.1864 | 2026-07-10 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 96b5d44f-fa2b-3d37-827a-2ba4e375298a | -13.3734 | -54.3779 | 2026-07-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| c0a37a65-a014-32b7-9938-4ed7458ff24c | -10.1662 | -50.2078 | 2026-07-10 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 52b5a8cc-fada-34b9-98fb-448ea2564960 | -13.3737 | -54.3572 | 2026-07-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| fed22a02-ebda-3f0a-b8d5-0e0804cd4b2e | -13.264 | -45.1343 | 2026-07-10 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 66a84dca-dbb6-35a4-82c5-7ed836041457 | -13.3737 | -54.3572 | 2026-07-10 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 4d6493de-a3ae-3684-a600-e9138fa0dc0b | -13.3734 | -54.3779 | 2026-07-10 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 9c48ac9a-bf5a-38c6-9c0b-01d71bc85a4a | -10.1664 | -50.1864 | 2026-07-10 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8c5b0b36-720b-3d98-a178-a9c09c34780b | -10.1662 | -50.2078 | 2026-07-10 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0b5e75bc-b501-3a15-a27d-10bc5b0f6673 | -13.3737 | -54.3572 | 2026-07-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0a31ff8b-1e00-3f17-881e-57bef363eb78 | -10.1662 | -50.2078 | 2026-07-10 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 07d48a46-f889-34c1-b20b-57ef17cb9af6 | -13.3734 | -54.3779 | 2026-07-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 2f8bb21a-613e-3e81-bab0-6da0d4402cab | -13.264 | -45.1343 | 2026-07-10 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 6b733341-1e5f-3ffa-af7b-e7d5b1ffaacb | -13.3734 | -54.3779 | 2026-07-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4259833c-ec4a-3cd3-8bc6-43cdfb51c368 | -10.1664 | -50.1864 | 2026-07-10 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9d4d6852-0bea-35a4-9e6b-e22ff74cfbcb | -13.3737 | -54.3572 | 2026-07-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| a3488f6b-fd75-316f-b83a-1538ce1e42f1 | -13.264 | -45.1343 | 2026-07-10 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 1225e3d4-50ec-30a9-b557-943a0f57a277 | -8.1154 | -47.1058 | 2026-07-10 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| febca822-0be9-35c0-bbdb-a4de5cb76f8f | -13.3546 | -54.3593 | 2026-07-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 7f370a7d-ac9c-3ebc-adb1-379119525061 | -13.3543 | -54.38 | 2026-07-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| a51828cc-6398-3c67-8177-3d55c24fdeb1 | -13.3734 | -54.3779 | 2026-07-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 2e65f470-a4c9-336d-8430-2f732490915b | -12.5003 | -43.7621 | 2026-07-10 14:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b9b4089e-4ca6-3431-a3db-9f6b50e8bda4 | -13.3737 | -54.3572 | 2026-07-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 041dd3a0-69e5-3af4-9818-d93003719198 | -13.264 | -45.1343 | 2026-07-10 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 72c5cc76-71e0-3534-884e-be27e8578247 | -10.1662 | -50.2078 | 2026-07-10 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 76a9e088-d14e-3b99-bacc-a5f9e49143e7 | -8.1154 | -47.1058 | 2026-07-10 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 22856008-7e17-33ac-b891-992fd22d5a39 | -13.3546 | -54.3593 | 2026-07-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| cb60f9f6-425e-3612-8c01-840d5533a99c | -13.3737 | -54.3572 | 2026-07-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.1 |
| aa9f65fc-435c-3b17-8459-f958644ffacb | -12.5003 | -43.7621 | 2026-07-10 14:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5e80e891-9aea-35ac-9b5e-756d3cbac18d | -10.1473 | -50.2097 | 2026-07-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4a68d92f-ca5f-3c9f-b144-7d6edda23526 | -13.3543 | -54.38 | 2026-07-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| fc25f8ce-19b3-3abf-961a-a4dcf47ef665 | -13.3737 | -54.3572 | 2026-07-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 77fbe9be-30a1-3881-bd17-c0843418657c | -13.264 | -45.1343 | 2026-07-10 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5acbca4b-aab5-35f9-b450-37b1270a24f1 | -12.5003 | -43.7621 | 2026-07-10 14:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 7181b93c-1ddd-389e-8372-0cad440dc124 | -13.3543 | -54.38 | 2026-07-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 2614bef3-2fac-3e17-9e12-692bc049edd0 | -8.1154 | -47.1058 | 2026-07-10 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6dc612d3-9774-321d-ad25-8399756ba366 | -12.5003 | -43.7621 | 2026-07-10 14:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c73891cd-8510-3bf1-b626-45991cbe0c30 | -10.1664 | -50.1864 | 2026-07-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5e261690-309f-34a4-8400-dc37c9d9138d | -8.1154 | -47.1058 | 2026-07-10 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |


[Clique aqui para ver as próximas entradas](README14.md)
