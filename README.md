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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58ddbe39-a6e4-3851-b08b-ec8797c9fc8f | 2.562 | -60.5838 | 2026-01-20 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3676501d-5eef-3d6b-913a-d3b8cb01b9bc | -9.71021 | -47.69635 | 2026-01-20 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 94aa76a0-8b8a-32e9-9685-bd293d1b4076 | -6.59555 | -44.33398 | 2026-01-20 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e051f5d3-bac8-33ae-80c6-eb930fa580b4 | -12.65742 | -46.76229 | 2026-01-20 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 257c2f1a-6fd4-3f6c-9141-45620b2f363c | -6.1193 | -39.65549 | 2026-01-20 00:09:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 31.0 |
| e4c38a2c-f692-3f31-a9a4-ef19d8ef4d33 | -10.79132 | -48.22822 | 2026-01-20 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 453f8038-6fb5-31d0-8821-266093557396 | -9.71157 | -47.70667 | 2026-01-20 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d0996448-5f72-3950-89ac-a6c153a53954 | -6.59422 | -44.3245 | 2026-01-20 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f914e4f7-7dcb-321f-9ae5-13e948850b3e | -8.06798 | -48.01925 | 2026-01-20 00:09:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0c37112e-30cd-3e35-bf57-39324fecf64d | -12.65872 | -46.77243 | 2026-01-20 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 63e045c2-efd6-361e-9a97-48a0e22e9f48 | -6.11909 | -39.64981 | 2026-01-20 00:09:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 31.6 |
| ae21ee1d-85cd-3cef-a506-8ffd1567190a | -9.70072 | -47.69764 | 2026-01-20 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aff3a1b7-949a-3aa3-b81a-0b363df587b3 | -8.23032 | -48.18229 | 2026-01-20 00:09:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1581df70-e7aa-3f76-b54b-01ad373abd52 | -10.71826 | -37.10704 | 2026-01-20 00:09:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 710bd84b-12e9-3033-8679-99d6fd76e3d6 | -2.5312 | -47.80194 | 2026-01-20 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| be9bd2a8-4d52-315c-ba98-a2244e83180d | -2.93965 | -48.22612 | 2026-01-20 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88c0c3f4-e4ca-3ca3-a9ce-c2cbef1117a8 | -1.45669 | -46.82641 | 2026-01-20 00:11:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fc81abc-3a6a-3902-829c-b36519771ac3 | -2.60852 | -47.35155 | 2026-01-20 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74da6cbc-169f-3f39-92c4-7b3f1e0cce08 | -2.35466 | -51.88587 | 2026-01-20 00:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 405ea200-f168-311f-bdd5-505da3564fde | -2.94094 | -48.23551 | 2026-01-20 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08d83b0d-32d9-36ce-a249-614d07695db4 | -1.35683 | -46.64103 | 2026-01-20 00:11:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 55dbb0ea-c345-3fc1-98ff-6a1333141de6 | -1.36563 | -46.63979 | 2026-01-20 00:11:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed3de20c-fa1c-32b8-aebe-4cbc3d632077 | -1.45549 | -46.81767 | 2026-01-20 00:11:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e60912c7-0002-35b1-adf1-4a916c26d8de | -2.4356 | -46.9134 | 2026-01-20 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e89ba374-c380-3325-a64b-47d521c79af0 | -1.26398 | -47.17429 | 2026-01-20 00:11:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e0dc0ef6-515a-351b-9f90-f023dea3bbe1 | -1.67783 | -46.70296 | 2026-01-20 00:11:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bdf8bc25-6e0f-3030-b7bc-94c1d964dbe0 | -2.45618 | -48.05929 | 2026-01-20 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 416729d4-69cc-3d53-a34b-fc4d980aaaa7 | 2.5601 | -60.5644 | 2026-01-20 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 97571d72-2cec-3404-94e5-647eb1fda81b | -6.5991 | -44.3339 | 2026-01-20 00:13:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20ab8eba-ae0a-3a2b-b281-1afb099d07ad | 2.5553 | -60.584599 | 2026-01-20 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 82969198-30a1-335c-8950-b5e423afeee1 | -12.6592 | -46.7686 | 2026-01-20 00:13:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e140945-b434-3a98-8b3d-56789d729153 | -12.6608 | -46.775799 | 2026-01-20 00:13:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 561df02d-19be-34f5-9264-90346016885a | -20.8533 | -53.756699 | 2026-01-20 00:13:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d98b76e4-8b88-3979-97ad-0e78586720d5 | -2.9384 | -48.236301 | 2026-01-20 00:13:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e33bf9-0e65-344a-95f1-60d06f923093 | -9.7055 | -47.7029 | 2026-01-20 00:13:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36c2e95f-6d41-325a-b491-6dddbf0ac247 | 2.5456 | -60.582298 | 2026-01-20 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c1d23990-5557-3682-8724-0779730c08d0 | 3.3267 | -59.965 | 2026-01-20 00:13:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba6ceab-ca2a-335d-8904-1f502ced495a | 2.5548 | -60.5648 | 2026-01-20 00:51:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e217307a-f82f-384c-80e9-0ef759fcd7e5 | -2.148 | -54.392399 | 2026-01-20 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b562ce5-6083-3674-86b1-ec62f0602bd0 | 2.5511 | -60.580002 | 2026-01-20 00:51:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce19933c-d0f9-3efd-adf5-95fa63a7b8d0 | -2.0045 | -54.440102 | 2026-01-20 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5b5e19-2126-3f29-b9ec-378a609246e7 | 3.3219 | -59.970699 | 2026-01-20 00:51:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 98138822-2ec1-3415-bb51-51c0e69d2138 | 3.3251 | -59.957199 | 2026-01-20 00:51:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8adc5d97-293f-3bae-9de0-64968ed9e88d | -9.967 | -36.3882 | 2026-01-20 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.3 |
| a893f1ed-a523-3214-9005-6f3304efa01f | -9.9864 | -36.3848 | 2026-01-20 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 25f99f0b-8e35-3d6e-9136-34b5b20ae201 | -9.9869 | -36.3578 | 2026-01-20 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 178.2 |
| 2772e211-3283-315c-84b3-8e1f2f67e995 | -9.9675 | -36.3612 | 2026-01-20 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 211.5 |
| 3b2e315c-0619-38cc-baa3-964eddf4d004 | -19.4365 | -57.2354 | 2026-01-20 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| d1045f94-e60b-3434-9483-df1d80932ccc | -19.4365 | -57.2354 | 2026-01-20 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 3a8a1cb7-ed7d-38dd-bfb4-ea36c8988887 | -19.4361 | -57.2563 | 2026-01-20 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| f4a1287e-8164-361f-823b-64e6c96be2ba | -19.4365 | -57.2354 | 2026-01-20 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 0a7036e9-f967-3254-8dc2-84011443a05a | -19.4361 | -57.2563 | 2026-01-20 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 2a75e110-e1ff-3b99-a551-32808a0cc6e7 | -19.4165 | -57.2381 | 2026-01-20 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 81b24094-0125-331d-b836-993ee13fbe67 | -10.0107 | -36.1108 | 2026-01-20 02:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.6 |
| 71b86ba9-cf21-300c-95eb-78dcde9e017e | -9.9914 | -36.1142 | 2026-01-20 02:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 168.8 |
| e173582b-dfc9-36eb-bcba-2179f167c899 | -19.4365 | -57.2354 | 2026-01-20 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 78e436b8-cf9e-32d2-9ed4-5c6b2bcecbac | -19.4365 | -57.2354 | 2026-01-20 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| cd7cfc89-4072-31b3-9bd9-41fbaac64d6f | -6.769 | -35.2183 | 2026-01-20 02:40:00 | GOES-19 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 8854988f-5db5-3a7a-b1bb-b8b5e2d7582d | -19.4365 | -57.2354 | 2026-01-20 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 2b2bf8da-7fbf-3353-a3e1-f7ed36d85ae5 | -19.4361 | -57.2563 | 2026-01-20 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 9b08d00b-1365-31bc-8ac5-36fdbb70b81a | -19.4365 | -57.2354 | 2026-01-20 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 92251215-a9a5-3461-92a9-01c3ef9d2e1c | -6.76901 | -35.22004 | 2026-01-20 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ae754423-b9a2-3193-ab99-008bd025bb3e | -6.76818 | -35.22454 | 2026-01-20 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1d6a564a-719b-3361-b883-f4e503892e67 | -19.4365 | -57.2354 | 2026-01-20 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| f2aface7-677b-3b6d-a3fd-a6c99db8b9c1 | -7.51507 | -35.16627 | 2026-01-20 03:00:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 39b88e65-ce47-35da-a58e-8463fec0212a | -7.52182 | -35.16846 | 2026-01-20 03:00:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4479c4c6-b95c-3d04-82a9-c5ec7da8ca22 | -7.51595 | -35.16753 | 2026-01-20 03:00:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| bbf0ec14-a116-317d-9a23-7ac521b8d711 | -7.52096 | -35.16709 | 2026-01-20 03:00:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5114e446-ec14-33b9-8586-0645750c35ce | -7.51672 | -35.16322 | 2026-01-20 03:00:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 510c2da0-5d21-3a0e-93e4-fc187e57a089 | -10.13687 | -36.25852 | 2026-01-20 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ee46d735-d151-3702-8229-6924cbb1401b | -9.29203 | -35.50744 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b80ae89d-9b26-3aa2-9068-27b3bc87a725 | -9.29286 | -35.50313 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2b71ca76-d43d-333a-914f-d5a9445f2da2 | -9.29304 | -35.50214 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c4641dfe-ab35-32c1-944f-35f4e444b377 | -9.29224 | -35.50653 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 370b3f76-5b55-3db4-bd9e-2491c4495dfb | -9.2937 | -35.49878 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 008cf4a8-d249-3d51-be27-7d6cd6824137 | -9.28707 | -35.50204 | 2026-01-20 03:00:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a553f94-8ab4-31be-9169-ed8ca7707760 | -10.14291 | -36.25937 | 2026-01-20 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b85f1eb1-6cec-35ac-b513-94cc70da2f68 | -7.52151 | -35.1682 | 2026-01-20 03:27:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4389d979-ae16-390b-b764-8726e94a0202 | -7.7819 | -35.2864 | 2026-01-20 03:27:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a74df6b7-9bc8-3e45-8031-d841ef1d032f | -6.99397 | -42.87429 | 2026-01-20 03:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ef8e5859-0999-33e7-9729-4c9878406a7f | -10.7278 | -37.10368 | 2026-01-20 03:29:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a7fb173a-b7d4-30a7-a44c-2fddbd9b6406 | -10.72712 | -37.10746 | 2026-01-20 03:29:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 60d5676c-7b24-3b9f-b9ba-fa5339db1025 | -9.03107 | -35.2724 | 2026-01-20 03:29:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 437d87ca-09ee-3a36-951f-bc1d8fe8dd1d | -19.4566 | -57.2327 | 2026-01-20 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 2b1ed5b6-fc5c-35cd-a03d-0b4da775eb70 | -19.4365 | -57.2354 | 2026-01-20 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 4a0c8475-bb43-308d-b280-845bcac410a4 | -19.4369 | -57.2145 | 2026-01-20 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| afedd00b-9c4b-30f2-b26f-9ee1455b2dae | -2.85545 | -40.25192 | 2026-01-20 03:46:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb137c16-49ee-3873-87a8-b1d53ece992a | -2.93526 | -41.74165 | 2026-01-20 03:46:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d5df4d4-2b39-357c-b3ea-1889cfba0cdf | -6.99114 | -42.87376 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 983a86bf-0029-310d-bc45-1cb4972dd3b2 | -10.14395 | -36.26221 | 2026-01-20 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2d08ea48-8db5-3eb4-8cf3-5fe0405f329d | -6.97466 | -42.87143 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b60519b7-a2bc-3e8f-8222-ce46b74b5960 | -12.00035 | -38.16634 | 2026-01-20 03:49:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cd34e28-3774-3eec-8435-37c84a9145fd | -6.96976 | -42.87459 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| babe3b90-59d9-3967-9905-0630612cc54f | -7.46274 | -35.09357 | 2026-01-20 03:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6734524e-d8b4-3fcf-9849-300c4b6788f5 | -10.14339 | -36.26586 | 2026-01-20 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 608b5ea5-156b-31d4-9c62-7e9180a0c857 | -6.99537 | -42.87452 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b458fd25-1cf7-3940-b3f9-c1ef46465655 | -6.34436 | -39.85845 | 2026-01-20 03:49:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa373f7a-a322-37bd-a1e1-4210ba035e2d | -6.99227 | -42.87045 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aecb8719-93cc-3553-8ba0-5018ffe019ea | -8.48274 | -36.69564 | 2026-01-20 03:49:00 | NOAA-20 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 131c5976-ea46-35fd-b534-4bae7fd037e5 | -6.9869 | -42.87301 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README2.md)
