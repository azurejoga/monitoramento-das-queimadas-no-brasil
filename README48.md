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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae08a01b-f590-367e-8cc6-e032373a90e8 | -10.98708 | -49.20188 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1cda8a36-994c-3db3-ac4d-b6f70fee8c57 | -10.97427 | -49.30397 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b12ee09-bbd6-3aa3-b9a1-cf601ded1e37 | -10.97371 | -49.30747 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c314fb1-866e-3d13-a35a-9ede62ad3980 | -10.96522 | -49.42487 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1972415-7392-3dda-9be8-f3efa2da811a | -12.16638 | -49.68301 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a16bedd2-9112-3776-9bd8-81651b8208f6 | -12.16363 | -49.67894 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dce7b22-839b-3d5f-854a-fa429e0cef29 | -12.16307 | -49.68247 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da18d68d-c67f-356b-b0a7-5fc14f52555e | -6.41459 | -50.78729 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb65114-3be7-3e23-b61c-1df7e5e0588d | -6.22958 | -50.90222 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a95edc9-c659-368b-a136-24ef7f201324 | -6.22864 | -50.88515 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d76b4ffc-3bd4-37f2-80e1-a16ed4f9c8be | -6.22665 | -50.89753 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28993a6-fbc3-3346-9b9c-53804702f86b | -6.22573 | -50.88038 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3caef443-94f2-3f30-80bd-8ca719b56790 | -6.22506 | -50.88453 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d2259d-af5a-3e9f-8113-719ac3a4d3ca | -6.22306 | -50.89695 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81a92881-d4c0-39ce-9504-37c54c7c2b86 | -6.22215 | -50.87975 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d817c20a-5b70-3a3e-9be8-52bea45a6738 | -6.21856 | -50.87918 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f5a003e-5d4f-3ff0-9526-e3148c8a0be1 | -6.20979 | -50.86516 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3d998d4-9796-38b5-9cb9-00b73ed117fe | -6.20912 | -50.86931 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ea770bd-9abc-3d9f-9f5b-75becefe710b | -6.20845 | -50.87344 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 759b6fa4-7bb2-361f-906b-0b936f3b35f2 | -6.20688 | -50.86044 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd307cc-a3d1-3488-a4cb-a65bb1e6283c | -6.20621 | -50.86455 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a05172fa-7514-3951-a85c-802690158a71 | -6.20329 | -50.85988 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce461b55-6c54-36bd-9314-b858377bdfd7 | -6.20263 | -50.86398 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9cc94586-537a-32b7-b3bf-631306faa726 | -6.19903 | -50.86349 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c0cecac-00e8-31e4-a259-cda9bf4ec4f2 | -6.18826 | -50.86184 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0659f9f-b94d-35ad-9370-a95177c5f0ea | -6.18468 | -50.86126 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c1c66fa-4dcb-3d48-9260-5b391697859f | -6.18042 | -50.86481 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2def789c-833f-36e5-9cdb-8bd58ec874fe | -6.17549 | -50.87246 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2687ecf7-396f-3ece-82b0-c35b8543196f | -6.14307 | -50.93501 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 607b7e58-7914-321e-843b-2262a2bce90b | -6.11366 | -51.18081 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1e6e906-32ab-32e7-b2d5-4a11912dcfb2 | -6.10353 | -50.96367 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a54ac367-aea0-3b63-ae00-b847d6385100 | -6.10287 | -50.9678 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c61cbf36-14eb-3f7b-9735-3f2ea5da0028 | -6.10219 | -50.97197 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbab7df1-8e88-3673-9294-adb9422a6f6d | -6.09925 | -50.96726 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f535156f-31e0-39c7-9015-a0d2483f2e0b | -6.09858 | -50.97144 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f95f232c-b7cc-3c0b-8b07-3193d1437e27 | -5.95343 | -50.87596 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa66ab2-0781-320d-b420-5dea5a995fbc | -5.94985 | -50.87526 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1173852-e31f-3c93-bb68-26e026cbfba3 | -5.94629 | -50.87452 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d64520f-75b3-330b-b5f8-1dc87e6eaf11 | -5.93061 | -50.99242 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c33aabb0-36a3-34a4-bcec-d246405f8a78 | -5.92993 | -50.99659 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57f3e2ee-07ca-30b1-a9d8-c2d0beb0d79f | -5.30009 | -50.96783 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34225f05-45d4-32f0-9b7f-0fa8359a3461 | -5.24419 | -50.8947 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7ad317f-7680-3f78-bc62-c871fc9be175 | -5.24259 | -50.88151 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f745236-1c97-35c7-960e-c46442c0c630 | -5.24124 | -50.88992 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd127182-578c-33ce-b5c1-2a572693904d | -5.24056 | -50.89412 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a796e9-a236-380a-a94c-9dcf0a0ffa7e | -5.23693 | -50.89355 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f928bf7-7a4f-3ae5-a48b-07becafeca6f | -5.2333 | -50.89297 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca15bf10-cff7-3d56-82be-2221600f0d1e | -5.87599 | -49.90531 | 2024-10-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f24354b-9890-36ca-b86f-e901a75e3b27 | -5.85704 | -50.15336 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e8b3b20-d12b-3bec-a52d-c84da20e4bca | -5.80012 | -50.16394 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 550edb8c-bebf-3369-8c5c-31fd4d1d6e75 | -5.79664 | -50.16335 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41566821-c1f4-37cd-ace3-884cc4e0f629 | -5.79602 | -50.16721 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d784155e-1f19-3b25-b905-78eaec61550b | -5.79315 | -50.16278 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f14736a1-15de-3468-9e3b-9b7a680a0e36 | -5.79254 | -50.16664 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 928a2e2c-a9c2-3667-bf05-6a986afdd7ed | -5.75521 | -50.22061 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4137b11d-fde1-3947-95f9-eaaaf1a0b933 | -5.75458 | -50.22453 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc772cc1-63c8-31bd-93b5-b8a6043ba9bd | -5.75395 | -50.22845 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 672b87c1-9930-35b5-afae-3ae6aafccbf8 | -5.75108 | -50.22399 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8625a29-91c8-348b-837c-e93e6eff3aab | -5.74902 | -50.10423 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 059b0057-6b81-359f-91a1-40b56fafa0e9 | -5.67952 | -49.94827 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4431399-7ea4-34f4-ae19-ed6a1574f18f | -5.67891 | -49.95206 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcdc2c5b-3d3e-3b2f-bf96-eceeb721a474 | -5.64795 | -49.73083 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e69a267-58ed-3166-b79f-df99686e7bea | -5.61482 | -50.00542 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bf28db3-5546-3cb7-bf8a-ae3529ff95bf | -5.59194 | -50.10428 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8925b63f-5a31-362f-a61f-6743f6fcaead | -5.49702 | -49.57683 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74906ba2-bd7d-38eb-92a0-ad84391e5d01 | -5.34169 | -49.51475 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52e0d080-db60-3f1a-9f1f-c247eac6a103 | -5.2185 | -49.95136 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f695ce67-cf21-3a55-9876-2519d65eb261 | -5.21503 | -49.95078 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1af00988-c977-3933-ac41-349bba20ea40 | -5.19786 | -50.16687 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d70f16a-7e6e-3627-b2d3-557247960b1c | -5.18097 | -50.07211 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2af732f0-b04d-37f6-b2fb-8d15eb6675cf | -5.18033 | -50.07603 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 47bce0be-feb7-3008-96f4-bd20b86277d0 | -5.17954 | -50.07256 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b89634af-7237-3de0-98d2-9baa01ae2a30 | -5.17891 | -50.0765 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0136960c-b736-3b65-a0b8-2fa42fb9610b | -5.06516 | -50.4486 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0138fe2c-96cd-3f17-8f47-e5cc56db0c0b | -5.06161 | -50.448 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a52a9b-15dc-3b12-ac18-5a7574555ca6 | -5.06096 | -50.45202 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a50eaa4-1a0b-370b-821b-14858e6fc211 | -5.0574 | -50.4515 | 2024-10-24 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15cf8490-54f8-350c-aaa2-f043a428a4f0 | -5.01118 | -50.85141 | 2024-10-24 04:34:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5df622-b343-3d1f-801d-e511beca1208 | -4.98749 | -50.8825 | 2024-10-24 04:34:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71688d6-b801-3ec6-b50f-7894f6443ae2 | -6.81923 | -50.86541 | 2024-10-24 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0a1553-c387-33f8-a9b0-1614518e89e1 | -6.81076 | -50.87242 | 2024-10-24 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ec59c4f-7d05-3a1a-b5e0-ab693ba922a6 | -6.80977 | -50.92277 | 2024-10-24 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5d3e2ae-18ea-3d5d-b016-ed7752460163 | -6.80718 | -50.87197 | 2024-10-24 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ba08909-8dd9-306e-b1f5-1780bf50f0c8 | -6.79951 | -50.89619 | 2024-10-24 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8e3c62b-f44b-37f3-bd49-1abda1af6473 | -7.57064 | -50.70877 | 2024-10-24 04:34:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2634519b-6f45-3e66-8dbc-7258aba77e53 | -6.67505 | -50.41553 | 2024-10-24 04:34:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c7b8da-c49f-311c-8464-bf65d6e4f57b | -9.29441 | -50.77972 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f69e250b-9fe9-347b-9b4a-b158ef343082 | -9.28345 | -50.62932 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9482d964-6314-3a79-9dea-9182f1708af9 | -9.25839 | -50.39402 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6341bb22-c608-3d11-a976-b99dd47e39ef | -9.18158 | -50.5431 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6576063-10af-3e39-b9ac-b165325348de | -9.18097 | -50.54687 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99df1e14-71ba-339b-ba3e-dfc141748b36 | -8.72115 | -50.62899 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d812d511-b676-38d6-9b99-ced6bc966224 | -8.32523 | -50.89587 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9151a54-b2d8-3f53-8f1b-03c16443b108 | -8.0618 | -50.99426 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49ddc6f8-a57b-3c6a-9a78-cb2363846e69 | -8.06114 | -50.9983 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31b78559-c4ad-32e0-89cf-e3973ce3be79 | -8.06049 | -51.00234 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d15b3bd8-1107-31e6-bc38-75b6abb2daca | -7.99117 | -50.69084 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57ccf371-bad4-3348-9b5e-4c5424be86a4 | -7.99054 | -50.69474 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31ea04b2-93a4-3447-a12e-c55cdb436471 | -7.98832 | -50.68636 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5806cf1e-8965-3f41-8349-f4b4f1b12972 | -7.98768 | -50.69026 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
