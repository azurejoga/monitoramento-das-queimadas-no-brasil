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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad7a9e1f-2b19-3e83-9da1-a798618f5614 | -2.27571 | -56.17243 | 2024-11-11 05:35:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeaee35e-8d40-3f55-9b68-722acf53c210 | -0.84333 | -52.53356 | 2024-11-11 05:35:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2af350a-1ebe-38a2-a606-6b83b865b92d | -1.24136 | -54.14449 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6c5ac5a5-7fdf-3cad-9864-1841c773035c | -1.25555 | -55.77122 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3e019a-d9ed-39c9-90cb-fec573c59eb0 | -2.84843 | -54.00151 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a957bed1-40b0-3d1f-b1c6-1d9e011620b8 | -2.71698 | -57.34602 | 2024-11-11 05:35:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed8af7ba-295c-3f89-985a-36134f34f9e7 | -3.10072 | -54.29639 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17eac835-fb64-3592-affb-1a3d1412b71e | -3.14317 | -54.47906 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55f5e915-da82-3547-9cef-3ec622c5bbea | -2.31142 | -53.81614 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29b1238a-95cb-3efe-b2f3-7be527e8348f | -2.71757 | -57.34212 | 2024-11-11 05:35:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1dcac6c-317f-352b-ab25-93e9a4cba41a | -2.23317 | -53.67431 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e1974d94-5cb6-3e11-9340-e1af1e8401ca | -2.8156 | -54.01108 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 777e4eff-2f19-39d8-a621-9527932e0fe2 | -1.40311 | -52.37715 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70371401-5a3f-3dc3-89bd-8e42659036a6 | -2.81661 | -54.00445 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a077898d-b6f0-3b6b-83c8-3b61e938e3c0 | -1.2117 | -53.6348 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2632ff5f-57c8-3fda-80be-a70743837415 | -1.31993 | -54.63636 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d6aa1bd-dfc5-3af7-ac70-a02e4250d944 | -3.46033 | -54.62286 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b23b5a89-1d0c-3014-a778-bce211b61db8 | -2.30795 | -53.81625 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d95b4b6d-767b-3312-b6cb-d761f5753626 | -1.39276 | -52.36711 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85fb888e-eda0-3936-a06c-b76b446fa766 | -3.66017 | -54.65498 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48be3533-6edd-3da1-9dea-e8a3cf64b52c | -1.44801 | -51.67117 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 909f4af8-b81f-3200-b0e4-d5b9d6e45a99 | -2.2641 | -53.74404 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2546eeb-154f-3f88-95c0-8fce7b93a126 | -2.8151 | -54.0144 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93d5b1a4-445c-3441-9f8f-0a966b9dc701 | -1.39074 | -54.64479 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf4e11bf-8113-3a74-b747-54564261d05b | -2.23117 | -53.66914 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f68b7ca8-23ed-3591-83c0-1a9e1fdaa746 | -2.24784 | -53.66822 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d41ce243-c1d9-33a1-b132-a65da74e3d1e | -2.22578 | -53.66829 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6de2fb2a-0055-3d40-8655-df648e0cdc39 | -1.63332 | -52.54319 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b93a35b6-3639-3788-b552-684527d89401 | -3.32968 | -56.99096 | 2024-11-11 05:35:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 586b9830-3cd3-38a9-97ee-6ace58b02268 | -1.38947 | -54.65313 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08eb76a8-c4a8-3545-836c-8d4b5703dd63 | -3.67007 | -54.65923 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5a13e0a-eabc-3574-91ec-0b1773ae0671 | -3.52425 | -53.50211 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43367007-3ab3-32fc-8de8-cf6c3c4e5333 | -3.65931 | -54.6608 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3466822f-7fe4-340b-9172-c5c51fc44525 | -1.30568 | -54.66956 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2774fe03-e0b1-356b-b2e5-5f9fbb634a5e | -3.14741 | -54.4861 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 773b972e-8af5-32a7-aa41-270f1be861b9 | -3.14788 | -54.48295 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 19d25f1e-7f2d-30e3-a4e9-515133bfa697 | -3.10082 | -54.2937 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 076bc283-474b-3a0b-a743-92d74eb8740e | -1.62366 | -52.52934 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2002ed09-d77f-320b-8746-213758369799 | -2.24902 | -53.73479 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c10076a-d5f4-329b-96a1-f79809a708a4 | -1.39031 | -54.64759 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be5bfc9f-8b9c-3d73-8ad4-d03f69f5401e | -2.22883 | -53.66668 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c6be84be-eec3-39e2-9d9a-82d20f2b9ddc | -3.15823 | -54.48442 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb8d2a9-485a-3245-9afe-4e515479d4b5 | -3.3582 | -53.40386 | 2024-11-11 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f01c74a-a8d3-3b4c-96bc-f8b890552f9d | -3.09948 | -53.90238 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db5d5cda-9669-33fe-aa07-1929af906475 | -2.89239 | -54.17877 | 2024-11-11 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cadd49e9-d801-3739-8af2-051126fefe2d | -2.24245 | -53.66735 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed6be808-0426-338a-a222-fda55f9e4f75 | -1.30958 | -54.67019 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258aee12-88ab-3604-8af3-2c51d58d66a8 | -3.34407 | -51.66128 | 2024-11-11 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbc294e8-5761-32a5-a533-dd2a71cf767d | -1.6244 | -53.44111 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96b5390-0f96-3aa4-ba29-25a7c85e44e2 | -1.32486 | -54.63744 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ebd08a3-9759-3823-8a5b-cd5f6c86f942 | -1.32069 | -54.63676 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a0f61de-6dcb-3dd5-88f5-219f41b3e378 | -2.25287 | -53.74579 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3ddebd6f-cba2-33e2-9bb0-bd68c046a270 | -1.66129 | -52.63883 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84a60258-257d-3ca8-853e-8a8977c110e0 | -1.40373 | -52.37306 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 382f106c-5601-32f6-ba89-9c1bcbfe21c6 | -1.6288 | -52.53426 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8284017d-abb7-385b-bd6c-bfec5cacdeeb | -0.84274 | -52.53746 | 2024-11-11 05:35:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08d4b264-aca4-32a0-a77e-20ed40174789 | -2.2248 | -53.67506 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2b3e1701-a25c-3374-9e9c-b72da6c9f3c9 | -1.44679 | -51.67024 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40f6b9ca-8849-39e0-9218-994656ee9faa | -1.32532 | -54.60183 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df35886-3746-399e-ba34-e23785a2d67f | -2.22727 | -53.67682 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cf2f82ba-d929-37d0-b0b9-a284d4518f76 | -3.44991 | -51.57904 | 2024-11-11 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c709066d-57ee-3303-a57a-b3269b49f7b8 | -3.15353 | -54.48048 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5764baa7-c2ed-3f1c-a3e8-a4a644a889ee | -1.23622 | -54.14371 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c85a9e73-5515-361a-ab0f-37fcb7154418 | -1.42429 | -51.10732 | 2024-11-11 05:35:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62bf03f0-e83f-30c4-8910-0e22d292ae5d | -2.0722 | -53.28966 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c9ca2f3-f0ee-32dd-9dde-1a647db7e239 | -2.0701 | -53.30399 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feed7cf8-1d47-33c8-8541-7e7af2af9136 | -2.23018 | -53.67594 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 988504ad-3c25-3d4f-accb-b00a5f718eda | -1.13504 | -54.1023 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dac1694-0ef7-3dc6-9818-ae85be621357 | -1.2265 | -54.17305 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04f7e1c7-c052-3955-9582-28bdf911da83 | -1.75822 | -53.75308 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f18c62-b445-344e-a1df-de67cfe5c58f | -3.66491 | -54.65854 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85a5913a-7987-313e-86a9-fda5d76ee25b | -3.10641 | -54.29403 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a332fc3-63e2-3ecf-83bd-a02eb9a597cb | -1.4089 | -52.37808 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93f72c7f-4ded-3190-9df6-5efab3ff3617 | -2.72598 | -54.14085 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07be5e97-febe-3ecc-8332-b2f40f24cb86 | -2.22397 | -53.6624 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04ec076b-955e-3ead-8a1d-def602eefafb | -0.56811 | -58.11098 | 2024-11-11 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 979012fd-9b10-3af6-8612-d5ee377bfea1 | -3.14835 | -54.47978 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c69208d-0cf0-328b-91fa-0c1bc6573cca | -1.69971 | -53.74405 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a31edeaa-c09f-34a1-90e0-f8cd70a1edc6 | -4.27836 | -50.67431 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a76b9111-4762-3f12-9bb3-5aa8b0222b26 | -2.59257 | -54.24615 | 2024-11-11 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 069338ce-44fa-3a97-80d3-ef06db2e000c | -3.11735 | -54.47488 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddfc6b99-f3a3-3d9b-8f47-a93b817ddc05 | -2.22292 | -53.66924 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b482b4d-9c4b-3b84-9ea8-9dbe8b927c93 | -3.62599 | -54.70895 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 156bd082-3192-3990-a3a4-a64fa8a0ec6b | -1.39531 | -55.6834 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e72af869-63de-3a80-b4bd-6f6a28b6b5bd | -1.63907 | -52.54409 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd23e3b0-aa13-399c-a968-68c965948404 | -2.23167 | -53.66569 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b337a987-1f30-39eb-80f1-6d34ceaf5023 | -2.11131 | -53.44205 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cca8ef2-9b8c-30e5-b265-d96b6fcfd948 | -3.6988 | -54.61959 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 807eb7d8-45f7-3bcc-a9e0-1225fc3b87fd | -1.63471 | -52.54072 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e4fe57b-3687-3475-bcec-75ec79552d3c | -3.69998 | -54.64838 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 408e14f5-b73b-3f4e-bf81-678ea34255c4 | -1.20311 | -53.6911 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecfb458b-a5e9-3518-ae0d-fd8a75bd42ee | -1.56638 | -53.42138 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f22cebb3-f87b-3806-b5a5-235d69d308b1 | -2.2283 | -53.6701 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a9e02db7-d246-386f-a0ae-38314916bccd | 0.62211 | -60.08736 | 2024-11-11 05:35:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15b470b-f4c3-3e75-a147-60aa608a6adf | -3.05732 | -57.5633 | 2024-11-11 05:35:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e25e6f9-f9fb-3c1a-b053-9cdd75efaf10 | -3.59221 | -53.46424 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede09f04-a7e8-33d6-aab5-c4de0f401a89 | -3.69955 | -54.65138 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5965cbfa-0e43-3e87-b908-2315a472a901 | -3.05789 | -57.55947 | 2024-11-11 05:35:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c929a79-fe48-338c-8649-8f87cbfa4893 | -2.24851 | -53.73818 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 018b67cb-fb41-3d59-959a-d5cdd8764411 | -2.22241 | -53.67261 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
