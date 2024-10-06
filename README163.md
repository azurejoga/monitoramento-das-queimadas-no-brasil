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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f795dc5-91cd-3186-ace7-0477c0d61954 | -16.6535 | -55.8958 | 2024-10-06 14:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 57647db0-029f-3254-ab46-d502cc96bcd2 | -17.812 | -53.7859 | 2024-10-06 14:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 168.7 |
| a5dbe50a-b603-3258-b362-05e7b7db52ee | -17.8125 | -53.7645 | 2024-10-06 14:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| ff421d0c-2529-3821-99f9-3c997ee48644 | -17.8319 | -53.7829 | 2024-10-06 14:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e3aa04dc-bda3-30e6-a816-b445e9d4eb99 | -18.6383 | -57.2993 | 2024-10-06 14:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| d9ed5876-b911-3391-9e0e-c5ec2444b97f | -6.6299 | -42.1305 | 2024-10-06 14:25:43 | GOES-16 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 741b2ab2-8a34-3567-a449-cb8b8a192aa5 | -6.8216 | -59.1686 | 2024-10-06 14:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5e335364-8b2f-3289-99be-e7132020001c | -6.7795 | -60.1127 | 2024-10-06 14:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9bcb696d-f1df-353f-8b0e-86c715e9b1cd | -6.7796 | -60.0935 | 2024-10-06 14:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| da47c6da-ad73-3af4-a5c6-f1e37d8431b6 | -7.0049 | -59.3925 | 2024-10-06 14:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 1495d800-c0e4-3536-9f19-3756e85f59c1 | -7.005 | -59.3732 | 2024-10-06 14:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| aea17185-07d5-3623-86ea-f2cbd2319268 | -7.1331 | -42.6051 | 2024-10-06 14:25:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 34751ff0-9e91-3556-bc07-2237fe092b15 | -7.0233 | -59.3918 | 2024-10-06 14:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| e724a876-66ed-3da6-8aef-c927f07fb1bb | -7.0417 | -59.4103 | 2024-10-06 14:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5b55d93d-4151-3f8a-a3e6-5c1be85153c1 | -7.0232 | -59.4111 | 2024-10-06 14:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 9771d624-4288-38a3-a55f-c660d5100f6a | -7.6438 | -42.4818 | 2024-10-06 14:25:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 033ec540-791a-367b-aef2-308304b7b614 | -8.1756 | -43.719 | 2024-10-06 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 776bdc87-fe08-3bfd-838d-d9886c2d6c59 | -8.1478 | -44.4171 | 2024-10-06 14:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 34c07756-e2fb-3678-bed8-08c67b0d97e1 | -8.1948 | -43.6936 | 2024-10-06 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| dd3d4b6d-8d89-359f-b4db-68c44d06db8d | -8.1667 | -44.4152 | 2024-10-06 14:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a8365196-2fd3-3514-9fe4-3b20ae708238 | -8.1759 | -43.6957 | 2024-10-06 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 12d579f5-4731-3fd4-b384-20c8eeaed45e | -7.9639 | -54.7764 | 2024-10-06 14:25:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 8e5dd988-89bf-31c0-b68c-f4fa4bd1a6df | -8.1567 | -43.7211 | 2024-10-06 14:25:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| ce0addbc-fc3f-3074-b43f-33dfadbe452f | -7.9825 | -54.7752 | 2024-10-06 14:25:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 317.2 |
| 4a551b67-4cf6-3705-b05d-9a002835363a | -8.5364 | -67.1246 | 2024-10-06 14:25:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 178.5 |
| d3fc9c50-6d3e-39d5-8ad3-0f3da38457d4 | -8.649 | -66.6582 | 2024-10-06 14:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2659781e-75ba-3677-8c05-d4f53daad5cf | -9.2566 | -43.5241 | 2024-10-06 14:25:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 48a90e65-24b0-3270-b2c1-ed1933c14163 | -9.257 | -43.5006 | 2024-10-06 14:25:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| d2a54d6c-7e7e-3644-899d-7f73aa56d941 | -9.4361 | -54.898 | 2024-10-06 14:26:00 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 699ef286-3466-397b-8550-b0e624ef22e7 | -9.9395 | -46.0866 | 2024-10-06 14:26:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| dff06617-2358-35dd-b737-a943200cfb94 | -10.0463 | -45.2785 | 2024-10-06 14:26:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8755f50b-f878-3a02-bb47-d1ac613ab794 | -9.8552 | -60.2966 | 2024-10-06 14:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 47b6fce2-f975-33ba-9f69-f64d48672d27 | -9.8366 | -60.2976 | 2024-10-06 14:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 01f96742-8072-33f7-8259-f27f1d08938f | -10.2908 | -45.4305 | 2024-10-06 14:26:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b92b4fbb-9586-31cb-9104-d5e05e9f34a2 | -10.7838 | -45.5266 | 2024-10-06 14:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 0f6b74e4-2b16-3138-8137-699a1ec9b789 | -10.9187 | -46.6192 | 2024-10-06 14:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 778ea27c-cb15-3989-b945-72759d1a382f | -10.8032 | -53.5417 | 2024-10-06 14:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 39f6336a-0d84-3f71-8b95-163d29e71453 | -11.2591 | -43.3909 | 2024-10-06 14:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 7d6df82d-92ad-38ec-acd8-35e5ba40ed11 | -11.2403 | -43.3701 | 2024-10-06 14:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 118.6 |
| bb177417-b670-3d5a-9fb7-45743f1cfa92 | -11.404 | -47.2287 | 2024-10-06 14:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| cbd4d5d3-13d7-3342-b84a-e95125196958 | -11.2332 | -53.8724 | 2024-10-06 14:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 1f3e9392-e183-352e-933f-0dda7ae9db14 | -11.2335 | -53.8519 | 2024-10-06 14:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.3 |
| 733eb217-6e75-3c5b-a986-59a4ea20747f | -11.2844 | -50.0668 | 2024-10-06 14:26:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 73d7afd9-e8ed-34bf-a182-f6986c18f2cd | -11.3849 | -47.2312 | 2024-10-06 14:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| e64ca046-a872-3264-9d5d-89b1bdba5fcc | -11.3853 | -47.2088 | 2024-10-06 14:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 8dda2268-e5ae-3d5b-968e-49ee693f003a | -11.2524 | -53.8501 | 2024-10-06 14:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6ededcf2-3ad8-3310-bef9-e282b6412f64 | -11.4238 | -47.1815 | 2024-10-06 14:26:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 5391713a-4bc4-351a-ac9f-c17cc7ff3829 | -11.7378 | -47.8082 | 2024-10-06 14:26:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 31b43de6-f9ea-3639-b9b6-186f984e209f | -12.0124 | -47.371 | 2024-10-06 14:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b7cef639-6268-3428-8211-826a44fd0c90 | -11.9932 | -47.3736 | 2024-10-06 14:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 824f3698-3484-344c-a607-860cb9e0d54a | -12.1593 | -50.0717 | 2024-10-06 14:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| a0a9772c-4551-3610-8afb-9ef7114641ee | -12.6535 | -54.0208 | 2024-10-06 14:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 264bc12c-1fda-31cf-8b6f-f5a0c1726faa | -13.8749 | -44.6093 | 2024-10-06 14:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e0cad91d-c8a2-3ad0-af00-3d8962ecf3b2 | -13.8943 | -44.6058 | 2024-10-06 14:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f5323161-d2d6-3ab3-bd2e-2db0e6e60237 | -14.0888 | -45.5042 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 6a5ad4fb-bc43-34d0-9452-7fc00d82cb37 | -14.0698 | -45.4843 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| bed15e65-f40c-3994-9878-61907bd4243e | -14.0883 | -45.5274 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 4641761e-6a52-3dfc-8794-f78e21cfa680 | -14.0879 | -45.5507 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e6621fab-d319-32f8-9228-02d8f195e512 | -14.0767 | -45.1579 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 53599475-9a78-3e85-8847-cd42a08e4f48 | -14.0893 | -45.4809 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 793c5e2d-d481-3dc7-a48d-dff61aea5182 | -14.0689 | -45.5308 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e3a98337-7069-312d-829c-2804aeb93bab | -14.0762 | -45.1813 | 2024-10-06 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b322398c-eb96-3dc5-8956-35a707c88666 | -14.774 | -48.0532 | 2024-10-06 14:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| eaf89bfd-01f7-36c1-8902-f1a712dee8e6 | -15.1635 | -48.0336 | 2024-10-06 14:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 63ffa9c5-54f0-341a-8fce-bb0f8dbf1fa6 | -15.163 | -48.0561 | 2024-10-06 14:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 39510a12-66da-34e7-ad4f-f16314213b6b | -15.1435 | -48.0594 | 2024-10-06 14:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 95a29518-8b1f-3315-a67b-af513e639b40 | -16.9098 | -47.1493 | 2024-10-06 14:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fc6a2850-2436-3f3f-a0cd-5a183a6a4d59 | -16.6535 | -55.8958 | 2024-10-06 14:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 62954c64-a280-375d-8aab-5644d61f109e | -17.8125 | -53.7645 | 2024-10-06 14:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 173.9 |
| f7822ec4-f12f-3ed1-9f00-4059e86903b5 | -17.8319 | -53.7829 | 2024-10-06 14:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cffc8c94-8303-3733-87d1-ca081a412231 | -18.6383 | -57.2993 | 2024-10-06 14:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| ec58b984-1b16-3551-91ec-9fa21122ae3e | -18.889 | -54.5373 | 2024-10-06 14:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 4321ff54-2860-3663-a3a8-f947ca734655 | -0.8399 | -48.6608 | 2024-10-06 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3b2bae5a-9fac-35f2-8f91-f6522f3df5f7 | -1.3741 | -49.3579 | 2024-10-06 14:35:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 569c15a8-f560-3dba-a372-79fb65042575 | -1.3741 | -49.3791 | 2024-10-06 14:35:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d90fde8f-74c7-35bd-98ec-a40f4f1ebb80 | -6.6299 | -42.1305 | 2024-10-06 14:35:43 | GOES-16 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 74abdcfb-3b63-3baf-bf00-103be0e2ced1 | -6.7795 | -60.1127 | 2024-10-06 14:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f766a4ea-bf19-3ceb-8167-9e1a01dad313 | -7.0049 | -59.3925 | 2024-10-06 14:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 8befad26-1e29-3de3-bb08-f7461f77e6e8 | -7.005 | -59.3732 | 2024-10-06 14:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5be14ef6-c36c-3e06-99b8-9b799ac81bee | -7.0232 | -59.4111 | 2024-10-06 14:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 6c7d8c48-763e-3f0f-8fdb-1428e06bb83c | -7.7687 | -43.0598 | 2024-10-06 14:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 96c4f479-32ed-3c30-bc30-eab150c8a581 | -8.1759 | -43.6957 | 2024-10-06 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 25ba9617-e706-330b-8048-3688ae8b6cb8 | -7.9639 | -54.7764 | 2024-10-06 14:35:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 225.1 |
| 2e3b7b70-0e65-32fa-941c-e5da3a89ee30 | -8.1753 | -43.7424 | 2024-10-06 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 5302868a-1bc0-3938-a647-1aa0dadc1652 | -7.9825 | -54.7752 | 2024-10-06 14:35:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 383.2 |
| ce6031fb-16a4-3e07-874f-b26722a9309b | -8.1948 | -43.6936 | 2024-10-06 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0b4ed07f-d9cd-38ab-a4f1-4213cd8b4c54 | -8.1478 | -44.4171 | 2024-10-06 14:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| dff00edc-50b2-3038-9a09-6f49225083f5 | -8.157 | -43.6977 | 2024-10-06 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 9873d0cd-de05-315d-bc66-5bae1fe581ef | -8.1567 | -43.7211 | 2024-10-06 14:35:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| f8276a10-7370-3e03-a7a2-62c1760c112d | -8.1756 | -43.719 | 2024-10-06 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| d59fc491-c017-34c8-bd01-971c041b2261 | -8.5364 | -67.1246 | 2024-10-06 14:35:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 458.9 |
| cd7b92a1-6462-328f-886a-4f116e2cb478 | -8.7984 | -45.173 | 2024-10-06 14:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 3404f9ed-c409-3620-9e5f-4ae758e13aac | -8.817 | -45.1937 | 2024-10-06 14:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 510ce225-fa93-3845-a443-09cf3e72a91a | -8.649 | -66.6582 | 2024-10-06 14:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7c4030a5-5e15-3e1f-8058-f79c9f04195f | -8.9674 | -45.2456 | 2024-10-06 14:35:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 52b647a0-90fd-3f6c-85b8-731568527d3d | -8.9299 | -45.2269 | 2024-10-06 14:35:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d3f4029d-d0e8-3230-89dd-fca70d7d263e | -8.9485 | -45.2477 | 2024-10-06 14:35:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 4e18d062-360a-382d-bbfa-5c665099798b | -9.257 | -43.5006 | 2024-10-06 14:35:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 0d0319cc-647e-353b-8a91-6da5aa038e88 | -9.2376 | -43.5264 | 2024-10-06 14:35:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 279.8 |
| dc057760-378d-3ebf-baa3-b3b2483df370 | -9.238 | -43.5029 | 2024-10-06 14:35:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |


[Clique aqui para ver as próximas entradas](README164.md)
