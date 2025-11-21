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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 790f3cf3-ecb5-3735-b01b-3ea9a4824ad3 | -6.163 | -46.10555 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de6cfae0-08cd-370e-a99f-6626011968d2 | -5.42659 | -40.67306 | 2025-11-21 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 34497e32-ebc8-3ff0-8224-a4a72ba5afc6 | -4.56894 | -43.40221 | 2025-11-21 04:14:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4fed4fb-a7d1-39e5-b1df-c513d14a6084 | -6.2823 | -39.6896 | 2025-11-21 04:14:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e6d7b617-cc63-3d83-a272-8876d9b70f59 | -4.89032 | -40.44587 | 2025-11-21 04:14:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e037509c-a8e9-3e07-9479-8b1ccbb598ed | -6.22388 | -48.07953 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0beba0a9-9c5f-3967-b799-d465b1e8944a | -4.14176 | -43.67479 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86884adc-f24b-378d-b3d0-f9f7928f54ba | -4.37644 | -45.52328 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3596fc44-2265-3409-967c-8dc14b1d55a9 | -4.16781 | -43.67916 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d149032c-9957-35dc-82d8-e6ce733da810 | -4.15177 | -43.67638 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36743654-02d9-32df-aee6-5f7bee45f5cb | -4.14565 | -43.6718 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ed71ac-949b-30d5-92f8-b0e3360afe82 | -6.2123 | -46.08755 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b19241b-20e6-3bc4-8b2c-a8c1332c1eee | -6.66164 | -43.77061 | 2025-11-21 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fd818c1-9879-3030-a8fa-26a2b7726f04 | -5.74755 | -45.10905 | 2025-11-21 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7d46a8e-770c-3948-9826-58bad1f3111d | -4.16122 | -43.68148 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca772f15-b314-3f5b-98aa-17a4f3dd9e87 | -4.37289 | -45.52271 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ea9503ce-5a74-3a28-872f-c66d27ab7691 | -4.89181 | -40.44643 | 2025-11-21 04:14:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 044b27d2-4eff-3d24-8137-7f073b866331 | -5.73264 | -39.39358 | 2025-11-21 04:14:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1b13749a-2234-3ea0-8664-62b036c51098 | -6.11382 | -46.18198 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faca07d3-02ba-364c-8b03-b78e958fd8fd | -4.91716 | -40.00625 | 2025-11-21 04:14:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e04d8bec-f236-3526-adba-fe64b254050a | -5.35412 | -40.60023 | 2025-11-21 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aad50660-299f-3f85-9162-52d08706b1c8 | -4.15232 | -43.67286 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 241bd74e-d8a5-393a-aaf8-bc9117501c5d | -4.16678 | -43.66793 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2fc2438-f688-3de2-a2fc-c47555943075 | -4.16511 | -43.67849 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89ad4419-992c-354d-8de8-8f25fa0a44c9 | -6.66495 | -43.77114 | 2025-11-21 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 085956fb-2471-35ea-9787-669b2ec008cf | -4.16894 | -43.67213 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ed6685d5-b4bd-365f-90be-c63e96995bb0 | -4.36934 | -45.52214 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0d026f47-0184-3f8d-8609-ac435c3aa926 | -4.14342 | -43.68588 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe3de2ea-659e-334a-bdf9-b0f2e0bfb577 | -6.60092 | -43.85366 | 2025-11-21 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc8cc620-63c4-3f25-963a-056b3c982643 | -4.88923 | -42.08404 | 2025-11-21 04:14:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac2bb5da-5ffc-30ee-93a9-b16d0db18196 | -4.68623 | -40.68387 | 2025-11-21 04:14:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8048bbc-e4f2-388a-a1c9-6589627a8fbb | -5.88369 | -45.54657 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf2bcdab-4f21-359d-a72f-080804c453f3 | -4.14509 | -43.67532 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c9d4ea1-63c4-3a93-b4fb-0dec592e6e36 | -6.22623 | -48.06545 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d696f7d-af6f-343f-bf67-c906e3649caa | -4.36674 | -40.61977 | 2025-11-21 04:14:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b21673b-71db-366e-8a5d-88399877075a | -5.42372 | -40.66871 | 2025-11-21 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b467e4c7-5000-3a93-bf42-f9d429b86b97 | -4.38501 | -45.31279 | 2025-11-21 04:14:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 275a3a35-3a04-3a7d-a223-0162066fa1db | -4.16567 | -43.67497 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ef919a6-a29e-3db1-b7f2-46c55613a189 | -4.17171 | -43.67617 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ddfb7b4a-6469-391a-b370-195a507f141f | -4.14231 | -43.67127 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89e38766-3b76-3b88-8c84-d0d867945611 | -4.37999 | -45.52386 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0fd912f5-afed-31b9-b810-227d43a82c60 | -4.5717 | -43.4062 | 2025-11-21 04:14:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7689ba69-b1b4-3587-b064-92fc36e9a731 | -4.15566 | -43.67339 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80540fb7-4418-3f0e-bdc8-9597a840d433 | -6.59792 | -44.31758 | 2025-11-21 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 727d3f95-d0a6-3795-ac52-6994312c814c | -6.16008 | -46.10086 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05dc1ffe-c36c-33ef-9973-ef62a3665560 | -5.42718 | -40.66924 | 2025-11-21 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1fc0bc6-01db-344d-9978-b3558fb34042 | -5.73198 | -39.39796 | 2025-11-21 04:14:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9dcb9e2-d7f7-312b-b19a-7a638be335c8 | -3.99724 | -44.17046 | 2025-11-21 04:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c48875b-da72-3f54-9bd0-d5daef684869 | -4.1695 | -43.66861 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c244d316-daeb-3e7a-8163-403d11cec3ac | -4.04881 | -44.08623 | 2025-11-21 04:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ee605b9-1379-3b46-bbcc-b8c06c706602 | -4.159 | -43.67391 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44daa2dc-2c9f-39b4-abc4-53759843984a | -4.53639 | -40.52263 | 2025-11-21 04:14:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b989d10-0551-3b9d-b231-8eb5f20c69aa | -4.16178 | -43.67796 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0918634f-9bcc-3288-8309-6fdc5aab7070 | -6.21988 | -48.07882 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e3f3ead-0d91-3f68-ac82-c5f1c9a3cefb | -5.9067 | -46.37401 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca88597-781f-3910-b730-0167dadc3091 | -5.8252 | -46.48066 | 2025-11-21 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e983a11-1dae-3462-8170-5244d2da3399 | -4.15844 | -43.67743 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb682fad-5672-3329-b992-1ab5596e46a9 | -5.4243 | -40.6649 | 2025-11-21 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e046cca-ea9c-35d0-a790-d7596fad20a6 | -4.0238 | -44.54996 | 2025-11-21 04:14:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9000930c-30b3-3363-ac23-7adb979531b5 | -5.70533 | -47.0658 | 2025-11-21 04:14:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4df0cfc9-1af8-38c1-8c10-226fae1bb9ac | -6.22682 | -48.06194 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40ccca3-72db-3585-8ca1-243613c1c2c2 | -4.16233 | -43.67444 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81aa9aac-5a82-37d1-8807-ce3a0e77273c | -5.91146 | -46.20338 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 967b3a42-9536-31e9-a3c9-396ccee6f3eb | -4.14008 | -43.68535 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3be68d86-c01b-3566-ab77-0094721c1539 | -4.46272 | -40.81473 | 2025-11-21 04:14:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a2e2335-4354-3588-9f7b-0e40fa35ff9c | -4.14508 | -43.69696 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d31531f3-b9fa-37d6-8414-91f71752bda1 | -4.17227 | -43.67265 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ac3ecbca-3785-3953-ad95-bb6a03f47c47 | -6.22447 | -48.07599 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65c87080-6e88-3a7f-be4e-eeaea252fc33 | -4.59049 | -45.98704 | 2025-11-21 04:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed18392d-547f-3807-ad4b-2ccd0c2a5b04 | -5.9209 | -38.12592 | 2025-11-21 04:14:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b7c1d30-bf45-3b30-b862-e15877e9dcf8 | -4.15788 | -43.68096 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c23dbdeb-f929-3e2b-8df5-3a019e29c6d4 | -5.75098 | -45.10965 | 2025-11-21 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cb17af8-a861-31fb-b746-a6d88fad9407 | -4.89255 | -42.08455 | 2025-11-21 04:14:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ade2ba74-0814-3263-a68c-ad3c39d01f2c | -4.16623 | -43.67145 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d10a7714-69ef-3c97-853c-a4db2820a324 | -4.36331 | -40.61924 | 2025-11-21 04:14:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e26c545b-7027-31c9-b24f-b82c81253a57 | -6.16365 | -46.10146 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cee3c382-d8ce-3c6a-b0a8-8d76a9e3b1b0 | -5.75382 | -45.11401 | 2025-11-21 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8439a524-ab37-3a8d-81b7-ab6dd99b2714 | -6.51686 | -39.26989 | 2025-11-21 04:14:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c62402a9-3915-35a9-8f84-9d464d0ccaa9 | -4.14175 | -43.69644 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8184a06a-9b67-361c-9630-bddc7213fca2 | -4.16837 | -43.67564 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7306e236-d382-392c-b93c-2ea63e8ac101 | -4.37709 | -45.51927 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 874ad23b-fbe2-3a8d-be2c-ccec726ab550 | -6.16535 | -46.10505 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5c8745f-12ba-36e4-b719-22c525d6b91e | -6.27864 | -39.68903 | 2025-11-21 04:14:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 288014f5-eabf-38c4-b99e-4a6a5264e8a9 | -4.1551 | -43.67691 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9899bf1e-904f-36c9-a8c5-9cd0b0a0feb9 | -4.15955 | -43.67039 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eba16de-95e9-33ca-8af5-f01292bad682 | -6.3186 | -43.81223 | 2025-11-21 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c63e221-ce34-3b4e-8478-8b19f5eac4ea | -4.37934 | -45.52789 | 2025-11-21 04:14:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92bf8600-5f21-3c6f-aac4-2910b2b33995 | -4.14843 | -43.67585 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32538fed-af13-3d7b-b715-31d415497efc | -4.15622 | -43.66986 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 216402ca-4353-3abb-9f46-a8521de61980 | -4.14842 | -43.6975 | 2025-11-21 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 803c2f3b-c507-35cb-8bbf-6099cf77c9da | -6.22258 | -46.25015 | 2025-11-21 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1baf76c-3b43-3bc6-9f34-ad9160df3f18 | -6.22048 | -48.07525 | 2025-11-21 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 354048e9-376c-31b6-a698-1ce7e9b8919e | -4.88834 | -40.44591 | 2025-11-21 04:14:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5971c5b-bcfc-3212-80f0-018d9f6df061 | -6.31418 | -43.81865 | 2025-11-21 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea966fb1-5ecf-34fa-adb7-8646676e8c25 | -16.38615 | -44.0605 | 2025-11-21 04:16:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcf9ed55-e614-3b8d-a863-a4ea274615d1 | -19.16587 | -45.33344 | 2025-11-21 04:16:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca09e49f-36ca-3d06-bfee-19d73ce63b8c | -18.60958 | -44.26211 | 2025-11-21 04:16:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e2befb-b2ff-3a3e-bb70-b782cf370c61 | -15.77663 | -48.04377 | 2025-11-21 04:16:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c5f7587-5ceb-3055-ba46-f4cfd747cc32 | -16.94662 | -46.16384 | 2025-11-21 04:16:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03f5d3f-ac0f-364b-a512-b6e77841fe1b | -14.53164 | -49.33897 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
