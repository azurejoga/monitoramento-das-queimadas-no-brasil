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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b567a5cc-338f-3500-9de7-2da0e09cf732 | -2.95025 | -48.5954 | 2025-09-13 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83a1d725-1f5a-3e77-a77c-72e5b84bb471 | -6.45791 | -41.74854 | 2025-09-13 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cc9196d-ea93-3302-946b-0daab26ca11b | -7.06017 | -34.96608 | 2025-09-13 04:06:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d4107c1-d0c6-3e99-8d49-ea36e1b6d2ed | -7.31495 | -43.92477 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d03481ea-5f82-3dba-b1ce-35d4101ed39d | -6.85549 | -45.6565 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a96025b-dbd8-3ba2-896c-db6f7c216419 | -5.64883 | -42.60343 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0edf1382-364f-3d98-b550-eb10bc59f85b | -6.68928 | -44.12004 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 278c8ed5-a21e-36db-9c48-75194094cc50 | -7.41432 | -44.35873 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9cf72b1-b2fb-3d35-8633-8d30a842994d | -7.43173 | -44.85545 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 029dbde9-7d7a-3ac7-9e35-38045f41ab7e | -6.06627 | -43.55812 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9ace530-08c3-38e5-bb99-c0234ac2679c | -3.81166 | -52.08652 | 2025-09-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3516fbb2-d10c-325e-8e15-02e34ce327d1 | -3.26321 | -39.40686 | 2025-09-13 04:06:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5465f565-7a5c-3980-9749-7feb3adda9bf | -4.98137 | -43.04455 | 2025-09-13 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd141e11-e4cf-3fbf-ae87-e8a99aad1d45 | -3.48241 | -48.4347 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4656dfd3-e4bb-3821-9606-70a335dcdb58 | -6.83344 | -47.86782 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d55927b-14ee-3547-8ade-9637e7f9134d | -6.68901 | -44.11655 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba6d7581-594c-3e56-b3cf-ac0fd6897149 | -6.35648 | -42.5369 | 2025-09-13 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c506c643-f132-3c06-9962-fdaacd3ac70c | -6.88043 | -42.8314 | 2025-09-13 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2557a61e-26b3-3b51-af15-e299b9b4c505 | -3.22112 | -47.12531 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4d27722f-80c5-36b7-963b-cbe4166064e9 | -6.0977 | -43.36367 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39bbae4a-22ed-344e-818e-200426da1cf9 | -5.71197 | -46.44912 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f913cdfe-249e-3946-8b1b-2de1319c5bec | -7.42739 | -44.41279 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a51f662-48cf-3e3f-b81a-f93acc92e771 | -3.22834 | -47.6277 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| be2211c8-7062-34e1-97b6-251ee187c219 | -4.64711 | -47.55595 | 2025-09-13 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce9ed72f-30ca-306c-a4d0-adaef2403d43 | -6.25211 | -43.42963 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f413034-8cb1-3ea1-a2b0-0b522c50665b | -7.06872 | -44.12352 | 2025-09-13 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ebf928c-b186-3121-b54c-a3cfa284cd3f | -3.51192 | -47.22074 | 2025-09-13 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d75059b-c332-3910-9238-b6e2de256dfa | -6.44303 | -41.75682 | 2025-09-13 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d234b3cf-6111-39fa-b629-9b1dba2ec28b | -6.83494 | -47.85923 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f565aa2f-0667-3750-b079-69de31739e62 | -6.25424 | -43.47916 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6060a79f-8a90-3ccc-9c35-53f040b00c24 | -5.41607 | -43.41397 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daf5082b-6d1c-360a-b548-1b92e4e3f49d | -3.68525 | -39.33135 | 2025-09-13 04:06:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df677bc5-b560-3ffe-98a7-71e077cc2d68 | -7.52437 | -44.37527 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87c9c644-26b6-3855-9f0c-370692c40891 | -5.30945 | -45.0321 | 2025-09-13 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c018eec7-ac85-30bd-a545-43d2f5951411 | -5.62139 | -46.66394 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cca7a6cb-f759-3682-9901-291bd288e97a | -7.45038 | -44.44919 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db080c68-0ca1-346b-a02b-fe1b0f85fbe6 | -3.26265 | -39.41044 | 2025-09-13 04:06:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50fcd806-80b1-39de-a6f0-891acf9423cd | -4.54909 | -43.73091 | 2025-09-13 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0024a29f-e9b4-35f4-9ca3-46ce3d8dc446 | -6.21485 | -43.44271 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18444ddf-3d84-31e4-a82b-e18bfded4b8b | -6.4337 | -43.32502 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b01b7d5-f7ae-31eb-b628-2f99cf314944 | -3.23306 | -46.78156 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcfa71ad-f5b1-3329-8c80-aa4e9c332374 | -5.1113 | -46.07109 | 2025-09-13 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0683ca3-6b11-3b5d-ba0e-288e31b2a1cd | -5.49199 | -42.67745 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71df58a5-cad3-34bf-b779-ecddb609abee | -5.19541 | -43.04354 | 2025-09-13 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d1df43a-07df-3171-b34f-8c04b665ae90 | -7.25628 | -44.59703 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4125b1c-85b9-3914-8c8d-b5dbb571e02c | -5.54535 | -46.42136 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d94e6f4b-0e2b-3320-a4b0-06f24b474367 | -6.17873 | -43.25153 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7686eca6-1157-3a95-96cb-17869b599704 | -8.17902 | -42.44012 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 15ecc3bf-03df-3549-a228-033f8d866855 | -7.07222 | -44.12405 | 2025-09-13 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3add852a-dcb8-38d7-9908-7d8886b353db | -5.40252 | -42.82576 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ddf586c6-dcdf-3899-b6a8-d910ee52a77e | -3.23601 | -46.7904 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e1d0e20c-98c9-3306-a716-954f88fa5d23 | -6.17596 | -41.12317 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d272cad4-6a56-3cf3-ab40-dc60f42e86f6 | -5.95463 | -42.79425 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2f8d1286-3f23-33fe-86a8-2bdee8cc9cf9 | -3.21766 | -47.63568 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7d246ed-5505-3b4f-8fd9-52404e23618a | -6.20277 | -43.45222 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 416dca07-7579-35de-97ff-192ee03bf285 | -7.46482 | -44.42731 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29ebd11a-729e-3cf8-bbda-111cf8dedca3 | -7.21925 | -43.97647 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e93c13c8-8780-3ee9-88c2-c111b6fc34e6 | -8.08181 | -42.56075 | 2025-09-13 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0bce5a43-2307-3b3d-a660-bb0c8d90dedf | -3.67003 | -52.17962 | 2025-09-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cd56501-33ff-3e68-a435-4e70b41daccb | -6.99649 | -41.62836 | 2025-09-13 04:06:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43279f96-312c-3410-9b5f-6677dc896247 | -7.43402 | -44.43851 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0b27b13-30bd-3931-8c66-32f0e650b7eb | -6.91705 | -38.25359 | 2025-09-13 04:06:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 59335203-a763-3d89-8694-775357c198ed | -6.53714 | -41.35366 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28616aaa-0d83-3765-abf7-4c5f1ffc2540 | -7.21986 | -43.9727 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab08f153-530f-3e03-8f61-3ce43025c5e4 | -7.85113 | -43.86286 | 2025-09-13 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af2c2fa9-112b-38e9-829e-d8e55d9de61a | -5.25213 | -45.57852 | 2025-09-13 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 832a8586-c5b8-328b-8a48-e46a5bc8f5a1 | -2.27842 | -43.6684 | 2025-09-13 04:06:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17940c7d-6460-3169-94ec-986b84cc0740 | -5.18306 | -46.1682 | 2025-09-13 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b924724d-0f4f-3ad3-86d6-52e4cd41a48b | -5.96053 | -43.21302 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e14cd79d-3997-3d07-bb6d-ea1e642fa8fa | -5.08452 | -41.15266 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8ae1276-6fa2-3570-9430-37bde91b2bc3 | -8.03079 | -43.68498 | 2025-09-13 04:06:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e3b6a08-6ca3-37bd-8ea3-b977da15c9f2 | -7.55654 | -42.63829 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a74c174-ff7c-3bfe-910f-2b53ce987165 | -2.9095 | -40.40508 | 2025-09-13 04:06:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4e469c08-c3f8-3284-a3fa-ac0c8555154a | -6.56124 | -44.77286 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bfa040a-bf85-3fe8-9c7f-fcc77834aef4 | -6.77115 | -41.59297 | 2025-09-13 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c985cba-7147-3f72-8e16-640d475f63bd | -7.98267 | -43.65815 | 2025-09-13 04:06:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105a49ff-3418-3e9c-a716-7a11d3d28d62 | -6.56638 | -50.87207 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7e7cbeb1-6fa9-361a-b980-f4b688ddbf11 | -8.18676 | -42.43421 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44d5638b-5c56-3188-b28e-1a66742e22f1 | -6.03534 | -43.59596 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b4cd354-22c7-39b3-ade1-582ed1b66289 | -5.68421 | -46.3429 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32def52-9c49-3029-a4d9-812dea911c69 | -3.48153 | -48.43987 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 752b5d1f-2f2a-3260-8c7f-821ee4080008 | -6.55762 | -44.77223 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77f2387f-1806-3015-ae76-99972f70206d | -6.59648 | -44.3085 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96d2b265-eae2-34fb-8d17-9c7d2605ddf4 | -5.30078 | -43.06376 | 2025-09-13 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcb4060d-4487-3462-98d4-8f37c2d8089a | -5.95357 | -42.77938 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7c4b84c8-9b67-39e2-aa8a-0b08663f1e2f | -6.10531 | -45.94381 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 81ae298d-ac12-33f6-9eb5-2164fc74014f | -5.53519 | -43.04457 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e7bba1a-22d5-3b33-829b-de9abf04da0d | -6.62341 | -44.0775 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc022678-9d24-3f36-81ec-a22d2244b52c | -3.22225 | -47.63621 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 08c2eac4-b413-333b-8300-a4bc2044b442 | -7.56931 | -42.64394 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63040d5a-39b4-37d2-acf5-1756a3ce3c82 | -6.08517 | -43.13517 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c31ac41c-696b-36f3-bf72-f06bca42218a | -6.62216 | -44.08517 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2274decf-986d-39e8-8bf1-73b10520e13e | -6.87822 | -45.6362 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ef0dba-dc5c-35d2-b4e7-0d08658cb927 | -7.06808 | -44.12751 | 2025-09-13 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3143ae54-cf62-3883-afe9-7472f83def75 | -7.56041 | -42.65694 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 18029c85-5524-30fd-9634-daf2e23e21a6 | -6.16884 | -41.14687 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2088938a-d766-300a-a099-1a5d2cc25e1c | -6.3294 | -42.21618 | 2025-09-13 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5a20a429-1dd0-3e52-9b54-452bfb7797db | -7.14505 | -44.34465 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 631d2483-2bcf-3af3-85ce-0a5f2257217c | -6.56584 | -50.87508 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db689782-4f94-3e1b-bb09-2e7db3e7efdf | -7.31371 | -43.93235 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
