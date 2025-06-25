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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb29482-08cd-34a3-a022-8426de77a5ce | -22.09918 | -56.17258 | 2025-06-25 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6646f8e0-42da-3584-8aef-11cc81f57fa9 | -16.02884 | -58.61409 | 2025-06-25 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 41fefedd-ede4-3ed8-8483-07098f6a631d | -21.81067 | -56.29431 | 2025-06-25 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bde11222-18f8-3c6e-b4c2-133f86ed878b | -6.1791 | -48.0712 | 2025-06-25 05:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b4cab854-16ad-3d0d-81ee-bd05127649f7 | -10.443 | -47.945 | 2025-06-25 05:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 89f6af18-1d62-367e-ba09-7c2a83f537c0 | -6.1791 | -48.0712 | 2025-06-25 05:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 776c9acd-3f5e-35ca-95dc-40c431caf34e | -10.443 | -47.945 | 2025-06-25 05:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ff88365a-f887-302d-a560-72d245bc28a4 | 2.7531 | -60.36843 | 2025-06-25 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d426a9f6-cd1c-38b1-ba85-d08a480d8aed | 2.75181 | -60.36615 | 2025-06-25 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9a4bccb5-7c2c-3dee-ba6a-7a409899807f | -3.61358 | -47.52815 | 2025-06-25 05:46:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d2e4b28b-063f-3d9c-b174-47781a224678 | -3.6122 | -47.53718 | 2025-06-25 05:46:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b57bbb0c-eb52-3d83-87e4-e9a9d26cc434 | -9.3824 | -57.55988 | 2025-06-25 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0438741a-bc82-3a7e-a77f-3870cce3ab1f | -7.94472 | -63.00983 | 2025-06-25 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3881208d-ec8d-302e-b7ef-db3bcba5f718 | -7.096 | -49.16948 | 2025-06-25 05:48:00 | AQUA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d2d6ca05-dee4-39cf-84b4-f7abcb7731e0 | -9.17306 | -61.40389 | 2025-06-25 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 423bd84a-8a1b-3257-a133-71808fadb9b0 | -10.83369 | -54.04501 | 2025-06-25 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d3b6e0-d808-3d8c-bd3b-e5ad81ecca17 | -7.01698 | -44.5589 | 2025-06-25 05:48:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| e2244c7e-47ca-380a-a31a-3bbb2cbbb596 | -9.51366 | -56.10956 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 314baffb-70be-3330-adb8-682b1476a7cd | -4.52935 | -48.00541 | 2025-06-25 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fda72368-3dbd-305d-9f37-e4b3997a8cec | -9.56557 | -49.10324 | 2025-06-25 05:48:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| c7a483a7-2d7f-3e9d-a783-57e46f77f67e | -4.53836 | -48.00666 | 2025-06-25 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f43a740e-45e5-3f12-91fe-6b71762622a6 | -9.50343 | -56.10017 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d18905ba-44f9-3937-b39e-0eafdfc27a8f | -10.83287 | -54.0522 | 2025-06-25 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2813cbbf-0c66-3c58-b11f-750ae8cdcfce | -9.38292 | -57.55593 | 2025-06-25 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef8ca1d4-b63d-3664-94a8-fac0cd80cf1b | -7.90104 | -61.52084 | 2025-06-25 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e1ee087-38aa-3d45-9048-5f55ee2375d6 | -10.44197 | -47.95198 | 2025-06-25 05:48:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b33cb4db-69e2-3fa1-919f-320392c8c652 | -8.44173 | -63.83989 | 2025-06-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfe717fe-7d9e-36c2-bd5a-9b9aab11e16a | -6.18203 | -48.07471 | 2025-06-25 05:48:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 57c56615-d7ae-31e1-a365-531736189f2e | -6.17311 | -48.07339 | 2025-06-25 05:48:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a991e800-cfe1-316f-8342-62542ccb0eb9 | -11.86456 | -54.69762 | 2025-06-25 05:48:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e86a1a4e-8905-38f6-8c9d-b8b6a30c986d | -6.17449 | -48.06428 | 2025-06-25 05:48:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 81b1b1c0-42ee-35aa-935e-ec05d8a83b9f | -6.17585 | -48.0553 | 2025-06-25 05:48:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3ccdf85a-bfa1-347d-ab79-a6caabbba81f | -4.53974 | -47.99749 | 2025-06-25 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f469daac-7a52-3cdc-afff-b91a7c559522 | -6.29348 | -44.23675 | 2025-06-25 05:48:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 04d913af-21be-3a83-ba10-2b6e90f54b7c | -10.82652 | -54.04445 | 2025-06-25 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c674a98-9e43-32ca-8d85-e9f3cc0919a7 | -7.02504 | -44.57103 | 2025-06-25 05:48:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5a6f9933-4798-3123-b71e-a44d910f13ac | -10.4521 | -47.94442 | 2025-06-25 05:48:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0e622427-a94e-3001-9837-960333697856 | -9.50405 | -56.09539 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21f5d229-7922-318f-b1ec-6f5629995f50 | -7.90134 | -61.52044 | 2025-06-25 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd47f402-32fe-3524-bc20-6d0b35eee999 | -9.57313 | -49.11392 | 2025-06-25 05:48:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e19d022-58bc-3c51-b641-7b81a92c053a | -9.51426 | -56.10472 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1c56d3b-994e-3d66-a1b0-5ef8a9eac3c2 | -8.47486 | -50.28246 | 2025-06-25 05:48:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 68fc6142-3d70-3b8b-b5ff-baee30a1e2f3 | -9.56412 | -49.11254 | 2025-06-25 05:48:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d50373bf-7b0a-3070-a4dd-5abd1ac2ef3d | -10.44331 | -47.94309 | 2025-06-25 05:48:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5fdb9cdf-00c5-34b2-8b90-2a811c5f644e | -9.50806 | -56.10382 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0d95ec0-3ce5-325b-ac2d-5ca9e417896b | -7.02659 | -44.56014 | 2025-06-25 05:48:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 84ceb195-ba15-3223-ab6a-0492f5fda155 | -6.18341 | -48.06563 | 2025-06-25 05:48:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a72c9ed3-2f7f-35bb-bb9f-c9841ebd5072 | -8.47655 | -50.27172 | 2025-06-25 05:48:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7ef32aa0-7801-3362-80c3-08e2f0eec263 | -9.50304 | -56.09333 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ece62c3c-9073-3874-8d53-fce4ea89d1ba | -9.50864 | -56.09911 | 2025-06-25 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ce539da-b27d-358b-9dbf-8bc53be0cb78 | -10.45077 | -47.9533 | 2025-06-25 05:48:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 69baa4be-30f6-3975-b0cf-319d34cba0e5 | -10.443 | -47.945 | 2025-06-25 05:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 45fa175d-511b-3711-abec-84f9df5c402a | -13.29017 | -57.0786 | 2025-06-25 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8ad361-9679-38d8-b3b7-3eafcd524956 | -12.80095 | -48.73478 | 2025-06-25 05:50:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bbecef32-792b-3ff7-a4a9-9f1aae5bc21d | -11.5741 | -47.4268 | 2025-06-25 05:50:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d162df25-604b-35c0-a123-ca6f2561d6fa | -13.04528 | -48.82851 | 2025-06-25 05:50:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c1f541e8-37b1-3d9c-9789-7a1c1de4b6e4 | -13.29016 | -57.07908 | 2025-06-25 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0fd96ac-93a7-3130-badc-aae8afe6d537 | -14.71511 | -48.40669 | 2025-06-25 05:50:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f5a95e5e-7507-3c69-8f56-955d55ad7bd7 | -11.18339 | -48.61282 | 2025-06-25 05:50:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5643f27d-8d1e-36c1-8dd7-b7fe6e2b4ad0 | -13.28966 | -57.0833 | 2025-06-25 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33aba05e-f0cb-3b5f-956c-58ac77a3c469 | -14.80503 | -48.29659 | 2025-06-25 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1581d55a-246a-3bb3-b5fe-fcbc54d122cf | -14.80638 | -48.28746 | 2025-06-25 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a306c18d-7811-35d6-8608-02f043ca6333 | -10.443 | -47.945 | 2025-06-25 06:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 50272609-2b94-303c-8063-da60fefd4d82 | -6.1791 | -48.0712 | 2025-06-25 06:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 4239a8d8-17f4-3e99-a83d-02556f4c3e4d | -10.443 | -47.945 | 2025-06-25 06:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0299a262-ad56-3e95-8d24-1239750e3927 | -6.1791 | -48.0712 | 2025-06-25 06:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 4ddda000-be99-33a4-9cb3-bd8a5e34063c | -6.1791 | -48.0712 | 2025-06-25 06:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 322e2cac-ca7b-30a2-b556-bf09fc6aee07 | -10.443 | -47.945 | 2025-06-25 06:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5498df8d-53b4-3400-a85c-ad1968215b06 | -10.443 | -47.945 | 2025-06-25 06:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 04106111-1697-379f-8ffa-0eafefc124b8 | -10.443 | -47.945 | 2025-06-25 06:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6cff5895-2807-3242-9c58-326bf4a120f8 | -10.443 | -47.945 | 2025-06-25 07:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 0e810056-6faa-3afd-8aad-3e4779210776 | -7.08496 | -38.44285 | 2025-06-25 11:28:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 13.9 |
| fd166987-0c7e-3e34-a029-f52b5a74f5ff | -12.86485 | -44.3233 | 2025-06-25 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3fd7eedb-f9eb-38a0-9009-ffc5c053797b | -7.0171 | -44.5725 | 2025-06-25 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 747c463d-739d-3759-9b9d-d5f238860f64 | -7.0174 | -44.5495 | 2025-06-25 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 6807a319-c139-3ead-9290-f58c8cf8492d | -7.0171 | -44.5725 | 2025-06-25 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 427ae1fa-99bf-3729-ae13-78ed8d177f5d | -7.0174 | -44.5495 | 2025-06-25 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 0bbc8056-950f-320b-b2dd-64bb5524508a | -7.0174 | -44.5495 | 2025-06-25 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d497dd1d-30c2-3bc4-9230-c524bb958351 | -7.0359 | -44.5708 | 2025-06-25 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5fa777a7-0639-3e87-8ff3-216c43f6c359 | -7.0171 | -44.5725 | 2025-06-25 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| fd3adec3-b3a8-3de5-8e46-7d8a808f4987 | -7.0174 | -44.5495 | 2025-06-25 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| af8aec72-09a1-34e9-b3fe-9e76e5b92c24 | -7.0171 | -44.5725 | 2025-06-25 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6cfe5dfe-5ceb-3f1c-af60-6c23fc512bd7 | -7.0174 | -44.5495 | 2025-06-25 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6eb6dca6-f7cd-3b7f-94a9-291892e6652d | -7.0361 | -44.5479 | 2025-06-25 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 73179de5-eefa-385a-9ad2-130f90affebc | -7.0171 | -44.5725 | 2025-06-25 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| d3e5d929-d4f0-3c1f-b63b-d836fe1c0eea | -7.0359 | -44.5708 | 2025-06-25 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f95990a4-1760-3cca-896a-966f2bacda04 | -7.0171 | -44.5725 | 2025-06-25 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 38a0e0f3-4559-349c-a1e9-93a9b5d1e824 | -7.0361 | -44.5479 | 2025-06-25 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ca661c3f-ffda-3637-b064-6bdf654799be | -7.0359 | -44.5708 | 2025-06-25 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e83df604-1236-32f8-a723-c0d497bd3a96 | -7.0174 | -44.5495 | 2025-06-25 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 52ae768b-7898-3f2a-a1ed-70bbd569d311 | -7.0171 | -44.5725 | 2025-06-25 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| f4d81974-679b-3e23-91fb-18f43ecd0696 | -7.0174 | -44.5495 | 2025-06-25 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e03578a9-6cd3-3c53-bd07-a4a75e8b5da4 | -7.0359 | -44.5708 | 2025-06-25 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 42500de1-7faf-3245-93ec-a26a6aa28483 | -7.0171 | -44.5725 | 2025-06-25 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 04db33cb-9c78-3d0b-b7d6-43efc001b3b5 | -7.0174 | -44.5495 | 2025-06-25 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| f0084552-a9a5-3067-a802-5d9e0e9fda31 | -8.0696 | -43.1452 | 2025-06-25 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 4f335165-f1e5-3863-892f-db8cff006c40 | -7.0171 | -44.5725 | 2025-06-25 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| f55413e1-cea5-3990-9985-073f3ffb5211 | -8.8006 | -45.0128 | 2025-06-25 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| faf65379-e9d4-3468-ba0b-92bd74446212 | -7.0174 | -44.5495 | 2025-06-25 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2a0db010-6a3a-32dc-bf53-dd2067cfd8fa | -8.07 | -43.1216 | 2025-06-25 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |


[Clique aqui para ver as próximas entradas](README19.md)
