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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66447b16-2f18-3369-9488-7cc876c0c15e | -6.00133 | -45.41512 | 2024-12-03 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41654c8a-aab7-3e46-a3c2-a66135873226 | -5.81377 | -46.47923 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d8842feb-fca4-34ef-bd93-42ff5bd3ac60 | -3.31861 | -42.7874 | 2024-12-03 03:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4bd9d30-ec9a-3e5e-84e1-43a43946dd0f | -5.45331 | -44.82706 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3184a4fd-8803-3615-8168-e3f83091771f | -5.16948 | -43.73886 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| def8f38e-60aa-3200-8ad4-998bab156f4c | -5.78905 | -46.50614 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a0dadab-9a28-3fee-8298-c53bc93c6732 | -5.80526 | -46.48518 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4cca48d8-fb2a-3a8d-ac5c-1679e665f12a | -3.33646 | -46.0593 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3ef3f804-4e0b-337c-8f65-c8f41cefda1d | -6.98828 | -43.52071 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 6b29c692-c974-32a4-bf86-b38cbce0a0b5 | -5.16896 | -43.74189 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a42b7f7-d2e8-39f1-b485-5fa67878e829 | -4.94184 | -43.77593 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7da95947-09ff-37e9-91ca-129733977291 | -10.65201 | -44.4867 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69a56a29-7db4-3a3d-8f54-3c1ee98744bb | -4.4746 | -45.72271 | 2024-12-03 03:44:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a81f6da8-6935-3775-83fb-bf4cca9394e8 | -4.08117 | -47.35616 | 2024-12-03 03:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb02582f-658f-3595-879b-e176371cfa69 | -3.75251 | -48.15782 | 2024-12-03 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4eff01ea-3099-331b-a9ca-a20e7b91dc6b | -5.43236 | -45.54227 | 2024-12-03 03:44:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a66d099d-5659-31a0-be4f-edbfd45602d2 | -4.34964 | -45.99913 | 2024-12-03 03:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 117cd519-e4ca-36af-853a-77f4fbde6307 | -4.74079 | -45.11509 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e095343c-3bed-3aa2-b387-6351b4dc13f1 | -5.79833 | -46.48905 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4c68859-7b60-36a1-be29-1e8297e89dac | -3.34945 | -44.36339 | 2024-12-03 03:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58f7cccd-e968-3d5f-bc53-2c838d6706aa | -5.11534 | -43.21347 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| cd5bec97-05cb-3628-9dce-92f253e07882 | -5.81981 | -46.48038 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eb3a7dd-f59c-37de-8c2c-b28fa3a56b43 | -5.7883 | -46.51041 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 347467b5-f0fd-3885-ba37-f0c88dfb33df | -7.8034 | -38.73261 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b9b1fc27-7a3c-3c97-b89d-297e98d50fe5 | -5.12032 | -43.21412 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4eb24991-fc49-3676-bcd1-c2740ad91009 | -3.26533 | -46.93156 | 2024-12-03 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 068ae11f-a44b-3555-bfb4-4dc5cc4d3a7f | -3.26356 | -45.375 | 2024-12-03 03:44:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 490832f0-b8ba-30ba-9621-93916fdc3513 | -5.46737 | -35.5524 | 2024-12-03 03:44:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57cd7184-5047-39cf-b6ca-dfcc71054cf3 | -5.80886 | -46.50033 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7c0b7c6-552a-3b22-9fd1-483fe58f35c0 | -5.80356 | -46.49487 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2c3ee70a-44a5-39bd-b636-38c46cfe0201 | -6.81527 | -46.77481 | 2024-12-03 03:44:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e796a18-1c65-3e6d-80a3-c5d860f1e417 | -5.56804 | -44.88686 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43e8317c-9574-30c2-9c1d-dd434c7722ea | -5.19662 | -43.73429 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdd18586-c6f2-32f9-96b9-fbcf22830d28 | -5.45394 | -44.82341 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22aae117-bce3-3052-8ea7-febeafd6cb67 | -4.94699 | -43.77687 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab9f4d56-7ac9-3f38-8f6d-616a3c0173f9 | -4.80537 | -44.99612 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee43ffdd-c76e-3352-9276-41e4b18c74fe | -6.11884 | -43.96677 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 58c0ee72-4dac-3316-bbe1-8558b6bef549 | -2.8572 | -45.83624 | 2024-12-03 03:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1fe84cc1-ad35-3927-8ae6-54feb487615a | -5.82153 | -46.471 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92feeb4a-d17f-3c40-ac80-831cc4c5be05 | -5.11728 | -43.20224 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 97318ac6-9667-307f-8407-1429d21fd900 | -4.25871 | -44.14637 | 2024-12-03 03:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8bab24e-a829-3f38-9d14-f747520a4950 | -6.11987 | -43.96077 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b77fe3a2-c2f1-3848-975c-17f39a2706c4 | -10.64997 | -44.49779 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e490eb55-698e-3280-a54e-fa5a928a5068 | -5.81027 | -46.49836 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b638c377-0352-35a6-aeab-0a9c814872af | -6.11373 | -43.96579 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6631c238-202b-34bb-a075-05de63096c57 | -5.14709 | -43.23635 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4bc1420b-65ab-3c38-9acb-385e17b1d488 | -3.96815 | -46.62676 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9d80f27-2fba-3b16-b8a6-b48273aaa626 | -5.14117 | -43.24118 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 817bd484-8fb9-38f7-b9ff-d24404e04ad1 | -6.12038 | -43.95783 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a1cf5883-2c5d-3a2d-99e5-87489150c1ad | -3.34348 | -46.0542 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d922d8c9-1162-3780-a44a-57d0d69699d6 | -11.87204 | -38.35201 | 2024-12-03 03:46:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9148bde-5e80-39f5-83da-5db22af92590 | -12.49633 | -46.35169 | 2024-12-03 03:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64dded24-c7fb-3ac7-9ae5-e74ecdc92824 | -12.12747 | -39.39237 | 2024-12-03 03:46:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e1851a1c-80be-3d58-863c-eb650d9ce615 | -13.2428 | -39.98031 | 2024-12-03 03:46:00 | NOAA-21 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61a2bc3f-8c8a-3295-b40d-4732cc262d6c | -12.50171 | -46.35265 | 2024-12-03 03:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 292af497-169d-38b3-b60f-7a41103be181 | -12.12396 | -39.39176 | 2024-12-03 03:46:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a49b2d63-f111-3894-b341-3c5c09e39d94 | -12.71274 | -40.211 | 2024-12-03 03:46:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46b72c0e-4de8-3ddd-8b0e-6a09e45d6b7d | -15.64409 | -39.18397 | 2024-12-03 03:46:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1efa1174-43ee-3a8b-8d72-19dd7d083b3f | -13.57597 | -44.51715 | 2024-12-03 03:46:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63ebb978-ac3e-3a19-97d6-19354f91ac35 | -15.60709 | -39.32471 | 2024-12-03 03:46:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a63a4f04-a2ed-3d2f-9c68-a46bc666085a | -11.87603 | -38.34886 | 2024-12-03 03:46:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c11ba99c-8ce6-3085-babd-57ce22d14594 | -16.13395 | -39.09473 | 2024-12-03 03:46:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f64b74e2-c490-3abf-9751-92a0795a5069 | -16.76033 | -39.32529 | 2024-12-03 03:46:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df89fc24-b3ed-3c76-9f9f-7dc3b5c6c472 | -12.4345 | -46.67112 | 2024-12-03 03:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ee7ae1c-d432-3f38-8713-97d885bc1182 | -12.43378 | -46.67482 | 2024-12-03 03:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dffa80e7-5f64-3e7a-abcd-3caf7100a4e6 | -20.41582 | -43.55509 | 2024-12-03 03:49:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2660716-3152-32f3-a87a-f48e5b4db1ae | -2.8013 | -53.043 | 2024-12-03 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2fdbc214-7a31-3358-aee9-28d0ec94a035 | -6.1229 | -43.9578 | 2024-12-03 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 47d00570-5d89-3f78-8ab1-17fed80104d8 | -5.1181 | -43.1964 | 2024-12-03 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 09a4ddab-37fe-3b8c-8c9e-659c5005c1b5 | -3.1831 | -54.3247 | 2024-12-03 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 807c457b-a584-3638-98d8-cf6f1b35ab54 | -5.8009 | -46.4941 | 2024-12-03 03:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f541ac4c-fb8f-3ecf-af86-9b8f669e2473 | -2.8197 | -53.0425 | 2024-12-03 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ef0d259f-64bf-31da-a472-1cb3f53aeea2 | -4.1914 | -51.1914 | 2024-12-03 03:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c249a103-f8af-3736-b9fb-b8344a89cecb | -3.259 | -53.659 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f233a31f-f67a-328d-9cd6-0a8d7d324fa6 | -3.2958 | -53.658 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6a102b43-4368-3738-ac75-24d092cf4412 | -3.2774 | -53.6383 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ffe6395b-9fb2-3d13-b1e5-515f19f81779 | -3.183 | -54.3448 | 2024-12-03 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7bec8ebf-3f59-3de6-9800-ca85c8fbfe04 | -3.347 | -46.0486 | 2024-12-03 03:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 8df397de-1e5e-317b-8a82-8c8f7e190789 | -5.118 | -43.2198 | 2024-12-03 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5be001bd-8e1c-3af9-a818-ffe78c69ede1 | -3.259 | -53.6388 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5f634471-eea8-37d3-bdbc-afee9996cb3e | -1.0736 | -53.436 | 2024-12-03 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e16aae76-331a-37fa-a8c3-375c919c3bf3 | -2.8196 | -53.0629 | 2024-12-03 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fe9e6026-1f13-356a-a3b6-99cde143e925 | -5.801 | -46.4719 | 2024-12-03 03:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 277237e2-fd2f-31db-a5b1-5ce5140430dc | -3.0944 | -53.3804 | 2024-12-03 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 1169f1c2-fd61-38ba-be0b-c76510b73a56 | -5.8195 | -46.4929 | 2024-12-03 03:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 543e6941-f7ff-3a58-94d7-fe452e84edd6 | -1.0919 | -53.4561 | 2024-12-03 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 0edea47f-f433-37b6-a1f9-cef51bc3e5b2 | -3.2775 | -53.6181 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f2400af0-8d57-3e03-867c-8e14f2d2dbec | -3.2591 | -53.6186 | 2024-12-03 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| cd8bbf47-7049-3143-a2bd-8a9500e72cf3 | -3.076 | -53.3808 | 2024-12-03 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4e0b9350-d765-3c35-9ba4-ab7cb6515ee5 | 2.7267 | -60.3916 | 2024-12-03 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 46fb8540-7006-3ab8-847c-2c80ce63b086 | -1.0735 | -53.4562 | 2024-12-03 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 044cfaab-6537-3dfa-b9e7-230500978342 | -5.8197 | -46.4706 | 2024-12-03 03:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 8dd48b9e-98cd-3040-9cf7-303d97e2203f | -3.2775 | -53.6181 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cbbce35f-791e-376e-af38-68208f14a9d0 | -3.183 | -54.3448 | 2024-12-03 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 718c25c9-e94d-3aa8-ac93-71a1cec353e6 | -5.118 | -43.2198 | 2024-12-03 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3451abe9-edb7-3e43-9174-517ae895d6a6 | -4.1914 | -51.1914 | 2024-12-03 04:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4319503d-ac4a-39c1-9385-c6360f3e6ce3 | -6.1229 | -43.9578 | 2024-12-03 04:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0ad3f424-94fb-3776-8c68-e4618cfd7db7 | -5.8195 | -46.4929 | 2024-12-03 04:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e9f008dc-a1af-31cf-aea6-da696b18ed32 | -2.8197 | -53.0425 | 2024-12-03 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6ea3c660-3666-3af7-9d82-38777a6ede6f | -3.2774 | -53.6383 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README24.md)
