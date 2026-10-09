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

## Dados Diários - Página 248

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 415afb66-6769-32a6-bc2d-bc3120559211 | -2.3848 | -57.9044 | 2026-10-09 15:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0bbc5e71-1ac8-3416-a372-0404d0613e56 | -6.755 | -55.1465 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7ef68626-61dc-30fc-9ad3-d18f3fcada0e | -6.7366 | -55.1274 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 701e4410-9f2a-362b-bbc2-5250acd8885a | -6.6628 | -55.0912 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f1f40624-0fb0-3bcf-95d3-31e0582da004 | -1.4753 | -54.756 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| fd4e4e04-d663-32cd-918a-a5433f7a62dd | -1.7682 | -54.9911 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 99f87fed-dd13-348c-856a-4cc5c4f8b4a5 | -3.3105 | -54.6616 | 2026-10-09 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c8c20b55-9f14-367c-b0d9-71dc9d868d1e | -1.3264 | -56.398 | 2026-10-09 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 172ed44d-e509-3857-ae11-5773aac858f0 | -1.3932 | -48.9961 | 2026-10-09 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| bad2ef99-5f64-3182-8cc7-b1e440ad6484 | -3.1541 | -57.6772 | 2026-10-09 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c6024414-b29b-3808-a03c-d465921bf502 | -6.0624 | -59.928 | 2026-10-09 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 891c313c-3b2f-3184-8ccd-6c370e1e2770 | -2.3849 | -57.885 | 2026-10-09 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 51ec96db-667c-3196-93e9-44a40d4b8b3d | -10.9384 | -45.3916 | 2026-10-09 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 339.4 |
| 3a68db0f-b78e-3380-bd79-a17703fa5008 | -9.1012 | -45.1393 | 2026-10-09 15:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| d2952d6b-e184-3083-868d-ccb01a0fa433 | -12.2123 | -44.7457 | 2026-10-09 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 613.8 |
| ed182bc5-eead-3d50-bce3-7c108f42ae6e | -10.7475 | -46.6184 | 2026-10-09 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| be3d9f1a-292e-3ae4-ac1e-15d6f3769755 | 1.6938 | -55.6066 | 2026-10-09 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 3c4ffd01-b69d-3342-88b0-dde97ce006dd | -2.7429 | -54.0945 | 2026-10-09 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5bf4a675-f019-3268-bb66-f5aab1256725 | -1.2175 | -55.6512 | 2026-10-09 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 580.0 |
| 9f3f8682-b896-349d-8cac-02466d787788 | -11.0758 | -44.0299 | 2026-10-09 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 4c830994-4192-31f8-a91a-1ba1521febdb | -11.8783 | -47.3892 | 2026-10-09 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 321.1 |
| d575ebec-35f3-3dd1-a170-2d35235ace47 | -2.4623 | -56.0879 | 2026-10-09 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9e8efe24-a966-3530-8f91-a2b12b41ba39 | -1.5307 | -54.5159 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e382377a-3394-33b4-8921-c02c0b8ebdba | -3.8199 | -55.978 | 2026-10-09 15:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ddb02a20-23e9-33cc-ac34-9ec7cf6168b0 | -2.1544 | -54.4668 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 878c9142-0a93-33a5-b0df-ec98958566ac | -11.2849 | -45.2063 | 2026-10-09 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| e09f2c09-60f6-329c-b228-905c8eddd677 | -2.899 | -57.2155 | 2026-10-09 15:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 12dafdeb-c605-3fe2-9537-ac9cc86970a0 | -10.9193 | -45.3942 | 2026-10-09 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 646.6 |
| e0309367-cf15-3915-85f9-a2ac475dc1c4 | -3.1285 | -54.1657 | 2026-10-09 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 17734026-7cbb-36f0-886d-5b475e2f20c9 | -2.1361 | -54.4671 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5d046912-0233-3865-852d-18e228ef757d | -6.7366 | -55.1274 | 2026-10-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3c5df7f8-4094-3212-bfd3-547323ab6d66 | -2.2381 | -58.1194 | 2026-10-09 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6c07f2bf-548d-315c-8698-39057888895f | -1.5123 | -54.5361 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| e0b031d8-58d0-3ab2-9231-4051b7e69f4b | -2.3481 | -57.9824 | 2026-10-09 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9deae100-5624-3fc6-a687-b58d65b017bf | -1.5306 | -54.5359 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f320f457-8668-3384-b9e4-7f2a95c80674 | -2.8306 | -49.8768 | 2026-10-09 15:10:00 | GOES-19 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f9d2bbc7-b28a-3c55-861b-2a13eda5cdce | -6.495 | -55.2796 | 2026-10-09 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ffd09781-7b4a-384e-a86b-14f1a14e616d | -6.6814 | -55.0903 | 2026-10-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 967d3592-479e-3f36-9fce-154231fdb1fe | -13.7657 | -48.1224 | 2026-10-09 15:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e4ac1a37-bd78-3476-91af-688c97b9c95e | -1.4118 | -48.9318 | 2026-10-09 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 40371225-2052-3029-9954-29cdbeb2ac35 | -7.1994 | -55.1827 | 2026-10-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 8525b892-d6c9-39d6-9c4b-a81bf1d0b122 | -9.1015 | -45.1164 | 2026-10-09 15:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 4b9da5d0-9269-3000-92ed-02bedbbcb573 | -6.7365 | -55.1474 | 2026-10-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7a1604cf-58f3-3f10-98dd-0629f91e4233 | -2.8434 | -57.4696 | 2026-10-09 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f66093b8-2b2a-3640-a78a-e1a44996054d | -4.1011 | -54.6385 | 2026-10-09 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a7e0974c-8ab3-36b8-bd5e-ce3aa392ff80 | -8.969 | -45.1313 | 2026-10-09 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 24b160c2-6b95-3c71-b557-f5b60e9b7d7e | -2.4623 | -56.0682 | 2026-10-09 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 82f28f20-0dea-3cf7-aedb-e02d1c686c48 | -2.5492 | -58.0373 | 2026-10-09 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6be1af24-f716-3b86-a0ce-cf1949c1d86a | -2.3848 | -57.9044 | 2026-10-09 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b47cf1c9-1f29-3c39-932f-375453ed1b45 | -8.8899 | -45.3907 | 2026-10-09 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 22d4a435-2b32-3cf4-9dbc-b0e711a1a4ed | -7.4697 | -42.8315 | 2026-10-09 15:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 28e56ac0-96ec-36ed-8949-bb4081deede5 | -12.1549 | -44.7314 | 2026-10-09 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| b7d4a43a-973c-373b-8c8a-e1c9c2d3f248 | -13.1447 | -54.3405 | 2026-10-09 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 660cdd4c-8ab6-306f-91bd-8013f91f8a9b | -6.3842 | -55.265 | 2026-10-09 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9423f96f-c103-3054-900c-d60fe1e15bc4 | -12.2127 | -44.7224 | 2026-10-09 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 326.8 |
| 12310996-9695-337e-8d50-7140467838d8 | -2.348 | -58.0017 | 2026-10-09 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 90be96c9-8c3b-3c4f-af2e-0ab67f7085d6 | -1.494 | -54.5363 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 40622d3e-a083-39c2-a362-bf1ccb2f8f1d | -12.2508 | -44.7397 | 2026-10-09 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 54a0d4d9-ead5-3997-a52d-adbd9d906822 | -13.1644 | -54.2972 | 2026-10-09 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9624a148-990e-3435-8cc6-849dde295ba5 | -1.7682 | -54.9911 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 254743b7-1b7e-3c15-836b-2995d71bfec7 | -13.1444 | -54.3612 | 2026-10-09 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a4c46cb2-e40b-3f22-adb1-7b297349003f | -2.9819 | -54.0488 | 2026-10-09 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6d50a226-b975-368b-a9b3-3d344d741e2b | -1.3829 | -55.2142 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| e78b4378-e8ae-30d3-84ec-c87f26647393 | 1.1139 | -50.7279 | 2026-10-09 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6e3ae027-3d37-3927-b719-7e96b2c021d6 | -1.4569 | -54.7562 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a538c887-74a6-31d4-850a-568e0ba2a975 | -9.9798 | -45.9236 | 2026-10-09 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 3a420001-b286-356f-af3d-150e6d0205da | -1.1094 | -54.1802 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fd33ea9d-05ad-3c4f-8a62-9110fecb2e0d | -1.4569 | -54.7761 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2e36070d-9b0f-31ce-9bcf-1186f5c35bff | -6.755 | -55.1465 | 2026-10-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 09be9b6c-2b72-342c-9fd7-776c0ace45d4 | -3.9511 | -55.3209 | 2026-10-09 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| ea8a7381-4d78-3fe7-9422-488bbc8e68fb | 1.7121 | -55.6261 | 2026-10-09 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ade2278e-3c2b-3e10-aa1f-913e92909f63 | -8.3011 | -45.7245 | 2026-10-09 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 63a0ba9a-d961-3177-a9bf-140b483f4255 | -12.2316 | -44.7427 | 2026-10-09 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 5edf2b4e-e783-3a17-b71b-538f349728ef | -3.0809 | -57.6593 | 2026-10-09 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 93ce7d62-56e2-3ca8-83c6-9c4fefc10d4a | -1.1827 | -54.1795 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6c95a747-ecae-3554-a780-e985d6d49c15 | -14.3608 | -55.032 | 2026-10-09 15:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 1081ed29-2b1c-341c-bfbe-51358fd1f210 | -3.0605 | -58.4145 | 2026-10-09 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 77787cf9-61ca-32f7-88fd-74266160b38e | -1.1094 | -54.1601 | 2026-10-09 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 01323356-843c-3158-9634-8054cf260d46 | -1.383 | -55.1944 | 2026-10-09 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 212.4 |
| c12fbf11-5867-3e94-9a19-9c0b80fcf4af | -2.9327 | -58.3011 | 2026-10-09 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6a0ac712-1eb7-310d-a1a1-b0eb554658a4 | -1.3277 | -55.4525 | 2026-10-09 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0a72b9fe-443b-3f9c-937e-f20b187f2e01 | -1.3447 | -56.3979 | 2026-10-09 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0687678c-58c3-3953-9af7-4b89f65945bb | -3.2357 | -50.1805 | 2026-10-09 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5b295a13-93b0-3ca0-a184-0b337d71cb31 | -2.9703 | -57.9136 | 2026-10-09 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1274d430-8cce-3ee9-9e9a-3a44015f9069 | -8.9958 | -45.9454 | 2026-10-09 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 7a90404d-5629-33fb-bae4-5b52a6fb4c7a | -14.3611 | -55.0114 | 2026-10-09 15:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 200.9 |
| ac96e801-d34b-3c9b-9d9b-424d5e841a57 | -2.9704 | -57.8942 | 2026-10-09 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e3dbd6ac-ff93-32db-aa31-be7f6791ac69 | -6.4027 | -55.2641 | 2026-10-09 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 283a2cae-ebe4-34ee-9c46-f574f1f8c900 | -3.0799 | -58.0083 | 2026-10-09 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9698218f-5577-33e6-a647-5974f8b9d232 | -11.245 | -45.3037 | 2026-10-09 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 7c507617-c4d7-33bd-a7cf-2a6d53ed2c4c | -8.07 | -45.64 | 2026-10-09 15:15:00 | MSG-03 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8319a05-f30b-3897-bc5a-25cc9f34f450 | -15.38 | -41.97 | 2026-10-09 15:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36479f82-f357-30f2-a273-0a337e7af87c | -3.26 | -50.43 | 2026-10-09 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eef433e-459a-3341-a775-7ed839e88bb6 | -5.7116 | -53.5065 | 2026-10-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0c4c35b4-9940-3149-81c8-d2178a0d69f2 | -12.672 | -54.0602 | 2026-10-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 690aa32e-2389-3d69-bf48-121d4a9a0f25 | -1.494 | -54.5363 | 2026-10-09 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 40fd6e37-59a9-3dcf-87a1-abc016bd82b1 | -2.5492 | -58.0373 | 2026-10-09 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8e1b2742-dad7-3caa-bd33-e3434b0230f9 | -3.571 | -59.0777 | 2026-10-09 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 022585d5-6f81-3b6f-b220-fa0d98a5c3b9 | -2.9173 | -57.2151 | 2026-10-09 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7ea63d31-3ada-388c-a269-7e71ec2c8bb2 | -6.495 | -55.2796 | 2026-10-09 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |


[Clique aqui para ver as próximas entradas](README249.md)
