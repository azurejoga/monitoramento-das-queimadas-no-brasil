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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fffef175-5f5d-3cfe-bc2e-88122091e63a | -16.56496 | -55.94135 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d4f36bf9-1c60-377a-baf7-e5034ec81a6d | -16.56448 | -55.91794 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4abfe19b-716c-3d3e-8af2-5c7dc2dc4733 | -16.56319 | -55.94308 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6a14cce5-70e6-39f6-a588-9da03be3067b | -16.56125 | -55.94079 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f38180ee-63a6-3b00-b4e2-cb3732ceb604 | -16.56076 | -55.91738 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4c4c72eb-1931-3708-b109-8cc67f80b1d4 | -16.56062 | -55.94535 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 95c5d210-d697-3b91-91a3-b720d25456e2 | -16.56012 | -55.92195 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 44360b11-d548-3ebf-8446-e301623e36c2 | -16.55691 | -55.94479 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7378d5fa-6151-3178-a6da-c33e12ab0e03 | -16.55577 | -55.92596 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd831513-b5e9-3f39-baa8-513c040e1d11 | -16.55513 | -55.93054 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a519133f-6e38-32d8-b02c-b5bb896183f3 | -16.55321 | -55.94423 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 33725443-40aa-3315-a920-12c032b0516e | -16.55014 | -55.93911 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 24d58287-73b5-3b55-9cda-5f487020f1e7 | -16.5495 | -55.94367 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e5dc4e2-fc22-32d7-bd5f-cf74c3a80732 | -16.20241 | -55.9951 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b1f4951f-2ebd-32a0-af89-2052df21f6ef | -16.15218 | -55.92327 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fe5ec805-f10f-3d09-84d8-1b7fdfa94263 | -16.15156 | -55.92782 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 40fd0ba4-f2f9-3f3d-97ed-9eacc15ec1eb | -16.14849 | -55.92278 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bce34102-7ca5-30f6-9735-a519865da257 | -16.14788 | -55.92719 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| df1513b0-0cd4-321a-9ccf-988ae80b66fc | -16.14479 | -55.92223 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c0fcb005-bd16-3118-a4e2-2ddb78147df1 | -16.1442 | -55.92659 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bca5b152-57de-3093-abb8-6885aa2fcc1b | -16.65368 | -55.55546 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| db1c1b0a-2b07-3d77-a3ea-821adcd303cf | -16.65117 | -55.54538 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 87eb4520-5959-3c0d-a3e3-7afe48fd376b | -16.64924 | -55.55965 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 40a88adb-71d4-3873-ae3c-511de594b641 | -16.64865 | -55.53535 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 446648c8-3dd5-3205-9e0d-84459e661296 | -16.64801 | -55.54012 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1e16bc99-5274-34b1-aeac-fb7f1df34c89 | -16.64737 | -55.54482 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 31e56174-16f1-3000-886d-62927dbac8c4 | -16.64674 | -55.54955 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 12eca9b3-73da-3967-bb72-5a4332be3cc7 | -16.6461 | -55.55431 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ccacf03a-4072-3fdb-8cf2-5df7e040ca08 | -16.64553 | -55.52972 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 68832dc4-5366-33e3-80a3-e04140b54902 | -16.64545 | -55.5591 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c809bc4c-9451-31aa-a375-52f5e6ba792a | -16.64487 | -55.53463 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 820025a6-a1f8-360f-975c-dfff44cdb3bd | -16.64481 | -55.56387 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dfeca373-26a9-3be4-9ce3-d7261f6bf896 | -16.64422 | -55.53948 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 23f69d81-e569-3644-9ae6-91651da88e08 | -16.64358 | -55.54428 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 64b690db-c068-3dd5-a513-f34209d8b036 | -16.64294 | -55.54907 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ac4f44bb-7bcd-33fb-a89e-ac02af26e359 | -16.64229 | -55.55385 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 76b94e78-a71e-352e-9f0c-21b354bd7d00 | -16.64174 | -55.52911 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e83850ec-1294-33fc-a5a6-1867a5dcfaa6 | -16.64165 | -55.55862 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4356db0f-46a4-3329-ac8e-61bd08c538b0 | -16.64108 | -55.534 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 38f395e9-5d5d-3132-8396-c8fa3a2e698e | -16.64101 | -55.56337 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 532d7334-bff8-3d4d-ad6f-2469c3cf0ae6 | -16.64043 | -55.53888 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4515d594-79c3-30c7-a3f8-afc3bb22dd58 | -16.63978 | -55.54376 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6f6df391-b787-3e59-8432-648be408c547 | -16.63914 | -55.5486 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4d81e905-1042-3107-aaaa-bd89c2c3bbbe | -16.63849 | -55.55341 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57fd8420-b717-3b9b-8ed2-2648a7b83bf3 | -16.63795 | -55.52853 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 62318426-ef05-3d14-89c0-c39528502844 | -16.63785 | -55.55816 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 3e3da42c-5866-355f-8344-756f4021147c | -16.6373 | -55.53338 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 94b75d36-cc76-380c-aad4-46cc1d714056 | -16.63665 | -55.53824 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7ecc9118-1f32-3f32-ac19-90c839311c3c | -16.636 | -55.54315 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cde3ac98-6d52-337e-bc5d-246a2371c1c0 | -16.63535 | -55.54799 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cc0ce275-be50-3a8a-908e-8f3283a39545 | -16.6347 | -55.55281 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 757a8b4c-e8f9-3701-b958-176fa27ba260 | -16.63407 | -55.55759 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 45cf1355-31a4-3843-898a-a30fbefcb0b6 | -16.63157 | -55.54727 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 68214db2-65b3-39db-a406-a87abfd455e9 | -16.63093 | -55.55213 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f5c21f5b-0d56-3465-8de5-7f7f82566f04 | -16.63036 | -55.52732 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6f63b080-73a8-39e1-b823-6b4f06b23ae3 | -16.63028 | -55.55697 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d4c796d3-6df8-3025-8d1b-7068454fe6ec | -16.63027 | -55.53053 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e0f313d0-2d4f-3944-8ea8-adbc11daa9c2 | -16.62972 | -55.53214 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e7ebc4a8-52c5-37de-9f3a-fcdb2144fd77 | -16.61908 | -55.21362 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0aa13da3-e2f4-3bfe-8e99-b75514e0616f | -16.6184 | -55.21863 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 358d1eb1-4090-3fbb-86d0-aa8ceca6b9b9 | -17.14672 | -56.47992 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bef6d630-a144-390a-949a-9c554f649e5a | -17.14631 | -56.47748 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 62d0e832-577f-34c4-9b2d-bada161d619f | -17.04004 | -56.68198 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e01883cc-26fa-3a13-807e-be6f32cf2a3a | -17.03945 | -56.68626 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ef021c0b-ddd5-3817-a831-64e59806613e | -17.03227 | -56.68516 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 1d1f5a80-9b8d-3833-92ec-12b8b8dfe477 | -17.03048 | -56.69798 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4a12bab6-16d2-3c97-b072-37bae5a6e4ce | -17.0251 | -56.68406 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 93d4e125-e916-3a51-8a0e-fe820e764006 | -17.01733 | -56.68722 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7861f04f-1659-3f8c-a7a9-bcc35761132a | -17.01614 | -56.69577 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| db7079d3-97db-30a4-bd46-1d9e7753a67d | -17.01375 | -56.68667 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| cfea32eb-f840-3cfb-a6d0-254e2fa24c4c | -17.01075 | -56.68184 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 0e8f32d0-8b5d-34bd-96de-9d52b2b39e28 | -16.96359 | -56.61102 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9de75218-df67-3aa9-8b12-2caf63ff1ca0 | -16.96298 | -56.61531 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 532618e6-88a2-3300-a442-db466b346153 | -16.9516 | -56.61795 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| aaeca417-2dea-3dfe-be9b-3d469866de21 | -16.94501 | -56.61255 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c3c7458f-efa3-325f-a6a6-a2b9160aeaef | -16.94381 | -56.62114 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3b3c5214-6dee-374d-b057-0c469d9f556d | -16.94321 | -56.62542 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 24e30c15-66c5-35fa-b220-dd650babd8ba | -17.15494 | -56.15119 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c3e67fb7-9ce2-3117-baee-b6bef0a1a105 | -17.15241 | -56.16932 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f45149b7-7fdb-33aa-9ddb-0c6904f5bb1d | -17.15125 | -56.15063 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d25b9fd2-d167-37c8-9998-e047d23eeea3 | -17.14998 | -56.1597 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb14e0bc-4236-3d99-b7ae-23fd6428483b | -17.14935 | -56.16423 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 836e3bd2-c365-34ef-b871-e54eef7bb631 | -17.1463 | -56.15913 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cf853d97-a5eb-3072-9fc1-e22f26a39d67 | -17.14567 | -56.16366 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f88a6a38-58ce-3e2a-90b0-e5e9c65f291c | -17.14261 | -56.15857 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a032656a-93c6-316a-9359-0438cc7f34ab | -17.10949 | -56.09779 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 31e18f4d-f487-3021-aaa3-061a3db60e24 | -17.10579 | -56.09723 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 654309bb-ba78-355b-bdb4-052e03648efb | -17.06663 | -56.06142 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 785ecdc9-a5cf-3235-906c-babbc5249739 | -17.06599 | -56.06599 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1857f073-11d1-3e50-b29d-0985a89b3c86 | -17.06292 | -56.06086 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e56a0fbb-356f-3028-a464-db5f094c7c8e | -17.05986 | -56.05572 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2260d369-1430-3e86-9b72-688a8d7db175 | -17.05922 | -56.0603 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1b43a2b0-23f4-3595-a17d-96986b752b4e | -17.05615 | -56.05516 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d5ebdb8d-a55b-36e9-8261-55265d995e1d | -17.05552 | -56.05973 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f459acfd-1468-3083-8054-7e6fd3d3a01e | -17.04739 | -56.09113 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 65b7c957-9bfd-3dcf-be69-923182aae2f1 | -17.04369 | -56.09057 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1fffd470-3be0-3929-a9c6-545a5fbc9bb2 | -16.97356 | -56.14196 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d02044b8-1344-3f08-b977-7e657d376e66 | -16.97288 | -56.14009 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d5bac10e-3cf5-3544-8dbf-280ce0740a31 | -16.97226 | -56.14462 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a5fa2f39-e1a5-3610-8996-ee53f764d65a | -16.96988 | -56.1414 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README117.md)
