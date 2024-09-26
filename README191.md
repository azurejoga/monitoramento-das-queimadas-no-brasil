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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20edfabb-c9a6-30e6-8cab-a2858524b28c | -6.841 | -59.0132 | 2024-09-26 15:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3b7ca918-9666-3422-8b65-5fae78f23d26 | -6.8395 | -59.2643 | 2024-09-26 15:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 645c7a38-41f1-3c1b-838f-f0a1dddb2841 | -7.2007 | -60.6515 | 2024-09-26 15:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| fb9c6227-22d7-3e2f-aaff-e3ce26f1ee25 | -7.2906 | -61.0869 | 2024-09-26 15:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 211.5 |
| a9416fab-e5c0-3241-a137-7378ea70bddf | -7.3157 | -44.7515 | 2024-09-26 15:15:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7e740851-408f-30b4-84ab-90465682c211 | -7.3854 | -64.3662 | 2024-09-26 15:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 07d61ba1-3f55-33a3-ae31-1b0a0ab1b3f7 | -9.6563 | -53.5376 | 2024-09-26 15:16:01 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 11bb2de3-b6df-3cc2-a9a4-ad2dd0d69134 | -10.6654 | -51.0079 | 2024-09-26 15:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3f70b7f6-f31b-30ea-a37a-e70471bd882f | -10.9776 | -50.3152 | 2024-09-26 15:16:09 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bcb9f5f1-4ef9-3e42-ae7f-4bd9635c2a6c | -11.0059 | -53.9344 | 2024-09-26 15:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 2ae61d6a-5441-3c34-a46a-c6c0d22083fb | -11.1332 | -51.3826 | 2024-09-26 15:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f0fc2928-9b2b-32d3-98f1-d429cda97b95 | -11.2633 | -50.2194 | 2024-09-26 15:16:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5f7c8d81-5f99-35eb-8e84-122f6edd200b | -11.7659 | -50.9107 | 2024-09-26 15:16:13 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 050f5397-ea79-37c1-93fb-9b79aac0a244 | -11.7238 | -49.9084 | 2024-09-26 15:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b7a4b8a0-a5bd-3fab-a99f-a45b2b75d1f2 | -12.3427 | -50.544 | 2024-09-26 15:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 90fffdb9-f8e4-3b7a-b81e-4a49472cc26f | -12.3048 | -50.5271 | 2024-09-26 15:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b629ed20-8412-3edb-88a5-8a617d84630c | -12.5273 | -53.5168 | 2024-09-26 15:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c30841a1-4181-31a9-9b41-17bfa4decc1e | -12.4974 | -50.4177 | 2024-09-26 15:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 40195a6c-f495-380d-8d9d-65876d8f4f67 | -12.5464 | -53.5147 | 2024-09-26 15:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 87c29269-92a4-3ec9-9a72-c927409c804c | -12.8825 | -51.4396 | 2024-09-26 15:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| bde7fc2e-e8a9-3d2b-9df0-37b0919dd3a9 | -12.8082 | -51.2997 | 2024-09-26 15:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7647ee82-d485-3e8c-8c56-601bcee40611 | -14.0191 | -51.1668 | 2024-09-26 15:16:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 568bff77-17e1-368a-b52a-4ab9e7df48ae | -14.8163 | -48.8488 | 2024-09-26 15:16:30 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9f374eed-1102-35b6-95eb-e2063b64c108 | -18.5223 | -47.0952 | 2024-09-26 15:16:49 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c88a4e05-12d9-3359-8f38-6efbf9ed8638 | -3.4295 | -64.6358 | 2024-09-26 15:25:26 | GOES-16 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 97d9d502-b165-3ddb-8cb8-9c29374ebded | -3.4295 | -64.6173 | 2024-09-26 15:25:26 | GOES-16 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d181979a-b600-3b00-82a6-41b4c71136b0 | -5.1843 | -49.2505 | 2024-09-26 15:25:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 26cdf1c8-21dc-3327-bf73-0ce5b33c34cc | -6.583 | -58.9658 | 2024-09-26 15:25:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ea749f77-f91d-38ee-b3da-9926ea97e426 | -6.7839 | -59.3245 | 2024-09-26 15:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 66d34333-697d-3334-aee1-8573b51d2b1b | -6.8223 | -59.0527 | 2024-09-26 15:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 052aaa17-679c-37c7-a9ec-6d9524f203d1 | -6.8224 | -59.0333 | 2024-09-26 15:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3c521b89-d83e-3d12-9ffe-c2cf0a864bfe | -6.841 | -59.0132 | 2024-09-26 15:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e556137a-a169-3283-bc25-33aeaeb1d728 | -6.9682 | -62.916 | 2024-09-26 15:25:47 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 0d9d929a-ebbf-337c-8a12-a0ba66b23eff | -7.2007 | -60.6515 | 2024-09-26 15:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 142dd26b-45a9-3ce8-a7e8-03ea37ed20af | -7.1822 | -60.6713 | 2024-09-26 15:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d9bc9de3-3d89-3c63-8715-98629e88f3b7 | -7.2906 | -61.0869 | 2024-09-26 15:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 6277c7da-d5f7-341c-9aa3-f23893a32226 | -7.5068 | -44.4813 | 2024-09-26 15:25:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7982e711-e856-33ce-9179-67bdd41066c9 | -7.3854 | -64.3662 | 2024-09-26 15:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1acd44d1-b3c2-3f55-9978-203e44cb021a | -9.6563 | -53.5376 | 2024-09-26 15:26:01 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e30d4e95-e9ee-39be-a553-a33c65b5a6fc | -10.7843 | -53.5434 | 2024-09-26 15:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c2c3828c-346f-38b9-925f-dfee3b56ae7f | -11.0059 | -53.9344 | 2024-09-26 15:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 58cae600-4862-327c-b0dd-df16d30bfdf2 | -12.5464 | -53.5147 | 2024-09-26 15:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ad834fae-fe0f-305f-8419-4676b60b03b7 | -12.7911 | -51.1739 | 2024-09-26 15:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4c97cec2-c4c5-3dec-9a7f-2ecb7c13207f | -12.8102 | -51.1716 | 2024-09-26 15:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b380b747-7653-3d0f-9909-a353d9cb452d | -12.7908 | -51.1953 | 2024-09-26 15:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 80829b5e-22aa-3555-8756-842dc506fec0 | -12.952 | -45.301 | 2024-09-26 15:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| fa5d1b7b-81ed-37aa-afc9-bdbc077666a2 | -13.2156 | -45.6276 | 2024-09-26 15:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 367.8 |
| ecfc1212-2192-3b2f-994b-8674b432134e | -13.9616 | -51.153 | 2024-09-26 15:26:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 20c74347-8eed-3e27-be80-3369ae944e1a | -6.7836 | -59.363 | 2024-09-26 15:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 23c1f7be-0be1-382f-8cbf-fd89b752932e | -6.7124 | -58.9219 | 2024-09-26 15:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a767bd61-832f-3981-a85e-7379d103ef47 | -6.7839 | -59.3245 | 2024-09-26 15:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 26ecedc8-71ce-34f1-9135-f03b047523e5 | -6.8224 | -59.0333 | 2024-09-26 15:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8398be94-02eb-3c96-813e-b1269a3b4956 | -6.841 | -59.0132 | 2024-09-26 15:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8d31cc86-062f-3a8c-b7cd-df9df72fee04 | -6.8598 | -58.9545 | 2024-09-26 15:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c6738abd-cdbd-3a30-8f88-810397252807 | -6.8581 | -59.2443 | 2024-09-26 15:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8995c73a-ea7a-367a-bd71-ad7c77c687c5 | -7.2007 | -60.6515 | 2024-09-26 15:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 58752893-5bcd-3749-8dc5-0d276bb25554 | -8.1591 | -58.2915 | 2024-09-26 15:35:53 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 339f5a7b-6e06-319e-b5bf-7274b72719c5 | -9.6563 | -53.5376 | 2024-09-26 15:36:01 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 47fa1e5a-5ee3-3634-90ad-4a609c3aaa0b | -10.7843 | -53.5434 | 2024-09-26 15:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a31c31f3-5870-35f8-af2e-a856129fd764 | -11.0059 | -53.9344 | 2024-09-26 15:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 94b27517-009b-353c-8f77-7cdca4fae698 | -11.0245 | -53.9532 | 2024-09-26 15:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f82d55cc-f4b5-340d-bd74-318a59407e7c | -11.369 | -50.7846 | 2024-09-26 15:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 42d67b4d-eacb-3d70-bed2-ffc18292f1b6 | -11.3886 | -50.7399 | 2024-09-26 15:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 099993b9-6a28-3262-8fe3-b86dc2a11dc3 | -11.3877 | -50.8039 | 2024-09-26 15:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| d150c350-20ac-36da-9a2b-ba1e5267fff2 | -12.3048 | -50.5271 | 2024-09-26 15:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1606341d-baa9-3d63-82cf-b134b4d92dfd | -12.4974 | -50.4177 | 2024-09-26 15:36:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| af53cbcf-ab71-395e-80d4-199001862b00 | -12.5464 | -53.5147 | 2024-09-26 15:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 83e59853-a1a3-3f1d-a29e-3778037fefd8 | -12.8452 | -51.3803 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2976cd98-f71e-3782-bbf8-2ba2da2a2669 | -12.8086 | -51.2783 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 83d2bc64-76d3-3cd2-826d-2ce1e63e0752 | -12.8449 | -51.4017 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 01fada43-7b08-3a89-b5a3-f49607a0c273 | -12.8062 | -51.4276 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 9a3637f4-7464-362c-85d0-a63b0d27cb29 | -12.8643 | -51.378 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 493a16ea-96c6-3af9-a31f-2237c58d881d | -12.8257 | -51.404 | 2024-09-26 15:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| ace178a5-ac8b-3bc7-ad09-f0df8106e0d1 | -13.1796 | -45.4952 | 2024-09-26 15:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 46cd693f-0df5-37cc-8f58-7f94b38895bd | -6.7839 | -59.3245 | 2024-09-26 15:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8eed6b6f-b193-3ebb-8945-854610acc68c | -6.8397 | -59.245 | 2024-09-26 15:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f0aa822c-3821-37b9-939e-10a09597dc92 | -6.8223 | -59.0527 | 2024-09-26 15:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2d0d4624-95a3-3d6c-8bf5-01b4e4b44649 | -6.8224 | -59.0333 | 2024-09-26 15:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 018857b9-4a96-36a4-af05-3f7b2ae8c285 | -6.8598 | -58.9545 | 2024-09-26 15:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5739d998-a98b-30d3-9de5-588111621405 | -6.8581 | -59.2443 | 2024-09-26 15:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c5ed3c8e-9ce9-3e53-91d0-011dc56d34c7 | -10.7843 | -53.5434 | 2024-09-26 15:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 33d64798-c261-32e9-8bbc-a2fa62a86cc4 | -11.0059 | -53.9344 | 2024-09-26 15:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a48949b6-6160-3dcf-a1cf-1804881a1b14 | -12.3048 | -50.5271 | 2024-09-26 15:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ca3540e2-ac5a-3a32-bb19-1c4a959f80c9 | -12.8106 | -51.1502 | 2024-09-26 15:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bd173cbc-cb7f-3feb-b265-a2939d5e1004 | -3.502 | -64.82 | 2024-09-26 15:55:27 | GOES-16 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c33c9576-6a62-3db0-a766-01f6cd809782 | -6.5588 | -60.0444 | 2024-09-26 15:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6b93a706-b73c-382a-870e-e4254a9c1373 | -6.7839 | -59.3245 | 2024-09-26 15:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f0633d96-ba63-33e5-b58c-de453988ffbf | -6.8397 | -59.245 | 2024-09-26 15:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 13c1b16e-241b-325e-9304-2a0051518bc1 | -6.8224 | -59.0333 | 2024-09-26 15:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c291ce86-c6ce-3fb7-8fbc-3dd983099c6f | -6.8223 | -59.0527 | 2024-09-26 15:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fdaed4d6-f796-33e2-8337-3d369bff4422 | -6.8581 | -59.2443 | 2024-09-26 15:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 13de12f5-ba19-39a9-beb3-936d56669db3 | -12.3048 | -50.5271 | 2024-09-26 15:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| eb4828c7-8ad0-3d15-9583-cd3b1f9e6311 | -21.55 | -50.78 | 2024-09-26 16:03:22 | MSG-03 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ab02ce5-8783-3aa7-9888-db9134d5d520 | -21.55 | -50.84 | 2024-09-26 16:03:22 | MSG-03 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4feab698-99a0-39cc-afbc-b953c44edb30 | -21.25 | -49.23 | 2024-09-26 16:03:22 | MSG-03 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b617539-0863-349c-9024-a638148e5953 | -21.34 | -51.0 | 2024-09-26 16:03:22 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c623e8a9-d726-3a84-b2ef-e6df756dee83 | -20.88 | -48.92 | 2024-09-26 16:03:24 | MSG-03 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1c51146-1514-3846-84ae-f5fdf1e08ebc | -20.85 | -48.9 | 2024-09-26 16:03:24 | MSG-03 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbb3eb9f-73ee-3864-aafc-dcdf4abbebce | -20.84 | -51.29 | 2024-09-26 16:03:27 | MSG-03 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd0d9945-7dd1-33fe-aa82-9a93e78bbc19 | -20.84 | -51.35 | 2024-09-26 16:03:27 | MSG-03 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README192.md)
