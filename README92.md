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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 367eb561-64fc-36a3-8ac4-0dfbfeee1ced | -1.05544 | -53.5965 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5aedd03-52bb-3f8a-8088-f2d50a3bda09 | -4.59632 | -54.9205 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a644dc99-ba3e-3075-8745-23e219781aab | -3.40308 | -49.09146 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81d7fc6e-dae8-3102-b7c9-d3409b2c1fb2 | -6.38612 | -55.26734 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbddc24d-00f4-34fb-9e64-63524463b09e | -1.44989 | -54.475 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ddaa68de-0f96-3651-9e42-c27f3d31a500 | -3.00599 | -54.04568 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17e51d7f-db11-3523-859c-a4526a43ce47 | -5.11337 | -56.1973 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 675aa768-ab15-3dda-b32b-5d765033528f | -5.95274 | -55.34251 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cb202c8-b013-3220-9248-7eeb2dee7150 | -6.09604 | -55.69722 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da17ca5a-d257-3e6a-9c45-06bcd812222f | -6.37958 | -56.2206 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8baaba3a-3e52-3457-ad81-efe486e09107 | -3.34403 | -50.41615 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7882f5ba-1d69-3033-97b6-bc5725869e35 | -2.92877 | -54.08297 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7940205b-26b4-38ea-a787-5093a767f419 | -3.59634 | -54.60786 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 595e1dc5-bb48-3127-b07e-294e327a8293 | -3.18643 | -60.05295 | 2026-10-10 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e366126-b876-33ec-9f99-a35734034bfe | -3.8462 | -55.79287 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a96897c-32a8-3649-9ebd-defe70086078 | -3.62824 | -54.23568 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027d0abd-67f8-3cf4-bbff-82348a83b3af | -2.84626 | -59.12395 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f08b04f-6949-37bb-9f03-ecffd9b0263d | -4.19205 | -59.40492 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0ff9f21-d63e-3287-85a2-d63e899fb26d | -1.31481 | -55.43706 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d72bae23-bc0f-385d-a6ac-b6d1a85456ad | -6.11959 | -55.70107 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29b4799d-94f7-3b68-b640-9f28fd44d72a | -3.43979 | -54.54447 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c07dfc19-2362-3db7-b8dc-bba763409af9 | -5.95664 | -55.33955 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c159fd0d-767d-3cd0-a0f0-931f50f0a75e | -3.31155 | -54.02684 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cbb0955-a4ac-31b7-a889-82acccb0e305 | -4.75332 | -55.66638 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75639540-665d-3a68-954d-12e9f0b45ab0 | -2.9002 | -54.19895 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132496d4-b82d-30a3-bf1b-25587fce9e55 | -6.47317 | -55.29565 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4807219-5050-3778-a4b7-94ddd4b9953b | -6.47448 | -55.07701 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f98543e3-460d-3980-8328-0fc937621663 | -3.21183 | -50.54641 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a7e523-f9f9-3355-b044-88e31d758bb3 | -0.97071 | -52.45877 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c949a56-f7ee-3df4-9a89-186eda3d73e9 | -7.44832 | -46.28164 | 2026-10-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a314b180-8676-37bc-af1e-689ba73af0c6 | -3.59078 | -54.6859 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 171deb85-2a78-3c3e-af1d-665b60d579ad | -6.32045 | -55.33951 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a01f0e56-5f22-317c-a5fc-34acbd492433 | -3.4905 | -51.59476 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b83ce6f-424a-3e87-ae7b-07b7b91038bb | -6.07257 | -44.66285 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 005a8d5f-47c5-388c-ba4f-1c2c98ec4561 | -1.19211 | -54.21132 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21a55709-ab08-3b07-a82d-1cf3cbbebac6 | -3.01986 | -54.10799 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf0e208f-7706-3f4b-a6a1-4bcbd18a71a9 | -6.38699 | -56.21806 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6882c93d-e6e2-301e-8382-899ee5f8aa7b | -3.66444 | -55.50331 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2407f60f-0826-3936-8e77-cc61b35f9837 | -6.93904 | -59.24982 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 394fbfa4-005d-367e-971f-2f9787b5cc20 | -3.73293 | -57.16086 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9526867-8cb3-388d-b515-ef49ec339f5c | -3.25283 | -50.42507 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce9423ed-06bf-3cb7-a963-ecaade26283c | -2.52763 | -56.27276 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90afbe0d-f0ab-37d4-acc5-547a3f299552 | -4.14952 | -54.03587 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14831528-6175-3045-a820-dad54cfbba7c | -6.0566 | -44.65635 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e657e7-78ab-35fb-87d1-037970ae23a0 | -3.20979 | -53.96102 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92642776-4317-3cfe-b077-267f39474e66 | -2.47941 | -56.07534 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae7423a1-8498-3dca-ab2e-f40bcca03903 | -4.5696 | -54.95923 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1018a9d-9add-37a3-b1f4-3000be5e58da | 0.01004 | -60.57745 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36f13e89-4446-3b3f-9eff-eef99f773dd2 | -7.23946 | -44.16853 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae166d7-17cd-3f7e-867e-28f79c61e3be | -5.17901 | -60.30648 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b02112e-2f33-3092-8730-8f10b8ee84e6 | -2.74872 | -54.10383 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08ca5080-7592-3205-887d-f00809fbf600 | -3.2571 | -50.42146 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af2cab13-7816-39f4-8ea5-45ca2a8f4fa2 | -3.16858 | -58.62579 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b79cc25b-a03b-39e6-ad0b-8a9490f3c8dc | -7.50338 | -54.99587 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 85808a3c-94ae-383d-9909-e64334f3a02a | -5.93268 | -51.83169 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e26cfd2-9633-3aae-96d0-8dc547adf685 | -3.03472 | -54.07848 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8059114-66fd-3aaf-ac59-f91a40c1db2e | -6.9351 | -59.2491 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d025c18d-e06b-3eb9-96e0-7a96c70829c5 | -7.5228 | -45.32163 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fbf97bda-af8c-3d3c-96a8-24cab93b1a56 | -3.1718 | -54.73172 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f047408-985f-3cd0-906e-5ffc85aedb0c | -3.59523 | -54.59338 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 613337ba-55c6-3aa4-8c8f-071eeb1e8bf7 | -3.26499 | -54.0191 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd9ecd47-984c-365b-baca-da59f2f6c13e | -3.11786 | -54.17628 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b8fb6e9-8991-30b9-b8ba-a291fb40fbc4 | -6.00934 | -53.48622 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d7a985f-680f-3a85-b3a3-356132178cba | -2.83662 | -54.12867 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b946c186-03b0-3361-bdfb-be1cb8ba1305 | -9.0107 | -44.37082 | 2026-10-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e6ac321-8223-3e89-84d1-20a2bbca9e67 | -2.07297 | -48.14723 | 2026-10-10 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac2f5f5d-902e-3bc3-a975-f417a82ae173 | -5.18455 | -60.19185 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c51b4f72-4f31-3680-9d81-22edbe8e03a4 | -3.50558 | -49.94792 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb221ee0-ca76-351b-a008-22cd26b6e678 | -6.50075 | -55.37951 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92544678-6482-3fab-b3a8-be81e3c12408 | -1.18877 | -54.2108 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a189e93-52ec-399a-8618-86b0b9b26b9f | -7.23871 | -55.07815 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 195f53b7-df04-32a6-8407-3735b65f6b71 | -5.71162 | -53.47892 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a883fda3-bd43-3d01-9e93-33de51f630d9 | -3.71921 | -55.47089 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06993490-9d11-3e39-a699-bbfd778b13ee | -7.23597 | -55.15945 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 450fdb8b-ab38-358e-87c9-af87c2d919b5 | -3.26704 | -54.69273 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9476e5-65ca-3018-95b5-7d3090bdc60d | -2.83828 | -54.13955 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd68402-f77f-39a5-a617-f8eb35f785d1 | -3.30909 | -54.68123 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1adf34c1-fb4e-3046-8edf-47b408263c00 | -6.73503 | -55.10403 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d01a234-66c3-3fec-b3e6-4a17e27ffeb2 | -3.28183 | -53.87015 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b390685f-259e-301f-91cc-61bca85bf8c7 | -4.12264 | -54.03182 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b6150b-57ff-3a5f-82f8-ea6a470d66f9 | -7.47617 | -49.40675 | 2026-10-10 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee68605-1e28-3094-ab50-50fcf373a421 | -7.93752 | -49.74348 | 2026-10-10 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18501b73-c80a-3a26-bb87-520aa73e450d | -3.89445 | -58.95966 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d554646-83ad-3025-861d-2c98b1e1620f | -2.99974 | -53.89289 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9a106ca-ab2d-3971-8411-e3330ff82109 | -5.72158 | -53.50208 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2716ec1d-4413-38b9-964f-255ae3b36c35 | -3.26312 | -54.1819 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a58b313-0167-37f3-86c0-f82a7410d38f | -3.1431 | -53.71795 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dce09902-bd88-346b-b9b9-e2c091d83903 | -1.31845 | -56.40639 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c544b89-28a6-317f-bfb8-486ba1d3b3c1 | -3.62548 | -54.23169 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45890a8c-5089-3a56-8f03-9680ab8fbbb5 | -3.30545 | -54.00117 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c00c1c85-8d6c-3cb0-bb31-588df5999835 | -3.78482 | -59.37532 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d111e89c-ee74-38a3-aa26-d44806c37856 | -6.41091 | -43.74162 | 2026-10-10 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27bc5dda-f0ab-3a0d-ae0d-fb68cbd621c7 | -2.9701 | -54.78297 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8103a8a-44cd-3064-9a62-6bc344c7dc3b | -5.67383 | -49.82573 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff81611c-3096-3c88-aa9a-90d62c50a93d | -3.72549 | -54.22306 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8d6d9d2-d88e-3883-aab5-c6d78147a9a6 | -2.86316 | -54.17537 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfce4c4d-54d4-3934-bd73-d35c1ebade70 | -5.89803 | -52.03486 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0baf5c1-2bf7-39d3-a7ce-ca007d58fab3 | -5.23622 | -50.90275 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e34085b-3a69-3765-8a46-86d8fa5bde39 | -4.4542 | -47.92271 | 2026-10-10 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1af8fee5-c7a5-3959-a44d-20df6942f561 | -2.75149 | -54.10781 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README93.md)
