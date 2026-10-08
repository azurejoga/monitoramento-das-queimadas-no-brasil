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

## Dados Diários - Página 360

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32d456e1-592b-3a1a-a742-c402fe6a3a8b | -3.34102 | -59.09675 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85f8076c-9ee7-363b-8773-09f1ab0305b4 | -2.13644 | -54.46626 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba851862-0021-38a2-8f34-4ce54a83228c | -5.68138 | -53.4917 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b3ceadc-e3d9-375a-a9c7-1195aac673b1 | -5.69931 | -53.44842 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 87ecb778-07bd-3320-89e2-4abf569efda1 | -4.74831 | -55.65347 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d3d26e6-3bec-3a06-be77-975acda72fda | -2.0791 | -46.5827 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ea3cfa58-89d0-3fdd-9616-7a00bdd41bc0 | -3.02332 | -54.07708 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 84f17954-1e80-3185-8add-cb3d7171adf8 | -6.39643 | -54.95639 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 311cca3a-e6a8-3984-861d-54af0754c4e6 | -1.50794 | -54.81548 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 765e0665-a92e-3fb5-9afd-8b644ea0155c | -3.73562 | -58.85886 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4e5ade8d-617f-3e63-9833-5cf34a79e273 | -4.68993 | -42.92244 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c24cb0d6-8349-3f4b-8190-2ec7560f6684 | -4.32135 | -41.22768 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b2affce5-3919-34a5-9b77-db14f5c740d3 | -3.27261 | -54.17852 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 7c6a0b73-03c9-3a37-b0e6-4b2e97754f15 | -6.74138 | -55.13337 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6642e355-1b1b-3576-9026-9cfe91b04df6 | -3.52679 | -59.33555 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 7e58a025-b790-38ba-bc5f-5db3e812e17f | -5.71022 | -53.45712 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 42344e0e-fb61-33ae-b718-4802bf56762a | -2.8247 | -57.60854 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f44bf35e-5850-332d-ba4c-e086623c89b1 | -2.39483 | -57.22645 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 27d3f8b1-195b-3faa-a2aa-0874400bfeec | -5.32378 | -42.81193 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e80e53cc-f7d8-3e13-9ce3-a0f4b0e3975c | -6.13449 | -51.75191 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 090213a8-552b-361e-9661-cae6fe15023a | -5.2799 | -47.91258 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 551d67ca-6cc3-3861-ba20-c8cf973a56b2 | -1.1487 | -54.21734 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 07e01121-ab41-3171-9b06-36213f6ede28 | -3.56985 | -59.48961 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8dd1086e-e0c2-3c3a-81e8-901df036426c | -3.77967 | -51.91245 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 33994c82-d81e-31c7-905a-7397dc70945e | -2.7471 | -56.61029 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 32444261-78db-3350-ad22-d37a2363ccf1 | -1.21603 | -55.64342 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8a12aee5-8430-36cb-88b3-247507191b32 | -4.15485 | -55.15914 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cadcccb6-88f2-34ee-86a7-ac8498642866 | -7.22692 | -55.10102 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f977a0a9-93f6-3dd3-b402-2af3e607d6af | -4.44559 | -55.86281 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2728719b-8df7-390b-b1c8-9fdc26415101 | -2.40223 | -56.11514 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c42b1b1d-0582-335d-8c07-19ee7c738808 | -5.92656 | -53.8096 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1ec32ee5-113c-3b00-bd06-5e07afd745f6 | -6.04024 | -51.72498 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36284860-9673-3b37-93b0-02d7f53dd471 | -3.16045 | -57.67742 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7cd3f3a9-6710-3075-a1fa-8e2d7b7cdf2b | -6.41209 | -51.94508 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3292f91f-b249-3c0e-914b-4d7f74939f23 | -4.38314 | -43.95436 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dae1653d-d731-3874-8c0d-4755f79dddd0 | -5.83581 | -43.43021 | 2026-10-08 16:39:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72a56760-36b2-3868-97a3-d50cfcf06f32 | -3.82051 | -44.68631 | 2026-10-08 16:39:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8895ca6b-3cd2-35e1-8e24-82d0d3ef4abf | -3.18231 | -58.83482 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c9873f04-14ee-35b3-90ef-5238cb660781 | -4.02424 | -44.82329 | 2026-10-08 16:39:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9eb0ccd0-5813-38fd-b7ab-caa4fbf14cc6 | -3.03948 | -57.49385 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a1dca945-aaaf-3976-b016-3a2b2471852d | -3.30208 | -43.06451 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7411379-0814-3f08-9ad4-69eb020cf8eb | -5.97025 | -55.34551 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1884c896-5f45-390e-942d-fb57a427e079 | -4.35767 | -43.79053 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 9082409f-11de-3ed8-8dd4-86335bb8941a | -3.48872 | -59.37757 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c5d4c68d-53d5-35dd-8259-1f7ddd4a07f8 | -4.32022 | -40.34786 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5a83f8a3-1ec0-3775-8af7-1db30cb93d1f | -1.61737 | -55.10975 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c5594728-1477-355a-8350-0a05a046b246 | -3.39786 | -40.2512 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9af50ff2-afc4-3494-bdc2-2ccbd4a7f18e | -6.74723 | -55.13599 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7bb9d798-78d9-3b56-8081-d8351f5786f9 | -4.08483 | -44.10737 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3344db60-f6dc-3511-a014-158ffc8330ce | -3.51182 | -54.63204 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8edfd040-f7d5-36c2-9e02-f5601395a523 | -5.49106 | -41.39812 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| fda83ca5-76f6-363a-9683-705d8359c22f | -2.82716 | -58.35585 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| e32692c4-4cd9-30af-aae1-a6435f5d8513 | -0.03071 | -49.63662 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 94e3789a-3296-336c-b612-5d745ab610c7 | -5.09952 | -46.2025 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 90e82082-1952-34c1-b84a-cd07a767750d | -6.32329 | -55.32466 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a7eab89d-4dbd-3ddf-8ee1-b5946790c153 | -2.7853 | -57.63236 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 478c33a9-afb2-319f-a0ec-6d49ead71b79 | -2.56874 | -56.16677 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1594eeb5-1c7e-3dd4-ac53-3815bcf868aa | -3.68968 | -44.81195 | 2026-10-08 16:39:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 07d2225f-fed7-3338-ad67-ffc910cd60ea | -4.69423 | -56.22716 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| cdad0d8e-64f3-30dd-b5c4-7add1787d3fb | -1.68834 | -55.27754 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2efef89-dfaf-302f-bdba-802e8f6475e9 | -3.30409 | -49.13406 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92180dc8-906a-310b-bb57-292ed06591f7 | -1.88127 | -54.72167 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 381c2e56-d3f0-3725-8241-1c39ea96db4b | -5.63079 | -45.79333 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| bf9be733-16ae-3313-bbb1-6c406e88bea3 | -1.0201 | -48.89349 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 412a1fe9-8667-306c-a2a0-a566fa7767f6 | -3.46955 | -60.25212 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 796eb317-5372-3ccc-92b8-566e1b94276a | -3.30609 | -43.09057 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42826de0-1b80-36ad-b06e-8bf75162e59e | -6.14952 | -52.87181 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 891dccd2-63fe-3ea2-9312-ef3f83b2dcab | -3.89706 | -55.64766 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3f11fb48-24a5-32f6-99bd-7fcfc7380302 | -0.98472 | -48.63994 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c56cd60-b231-3259-b55d-90a4f1d79fe0 | -3.00769 | -54.0768 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 05d76451-2a3f-35cf-9b57-f939f732f24e | -1.37797 | -55.45308 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1a31a6ab-be5e-35b2-b6d0-879026064702 | -5.89873 | -51.1693 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e07d03c-aa79-3c47-9aa6-672d2d5225ed | -3.092 | -53.95465 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fa2e4bec-dc75-3243-a464-1f68b208d588 | -5.0888 | -46.22254 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c245f850-e82a-341f-ac63-28c494188f25 | -3.08323 | -57.50109 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 887bd8e6-5a6c-324e-a0c6-8b447ebe495c | -6.73762 | -55.10553 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3706da37-5e64-3c6b-98f2-9e721a0be462 | -7.51273 | -55.57256 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 530020cf-2f14-38b1-af78-ed7da18bda1c | -2.87894 | -45.75585 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c52ad2ea-3efb-351f-afa0-29582b490564 | -3.29239 | -53.70393 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84119427-da68-35de-a078-a85a8bcf362e | -6.48821 | -55.30537 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 51a026fc-fe9a-3056-aee6-6f0c7130ed70 | -3.09596 | -59.19411 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9f108c4e-e879-3b9b-9cde-2b18a06f28fb | -2.5806 | -56.17209 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8d369e3a-cdc0-3b8a-a273-5cb9f7eca563 | -6.3112 | -54.80264 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 44d4ac44-e51b-3a0b-b60b-8a0b140ba025 | -4.52216 | -44.01215 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f01ca62d-9b92-39f2-bd90-e785b70aa7d9 | -1.38842 | -55.46304 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0a968c9c-356d-3b08-ad49-66b98bf3030a | -5.78533 | -45.38497 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91f45627-6245-3898-9b93-92d6f71ab7b5 | -3.89886 | -55.6448 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7c7f0838-6ae0-3320-b2e2-63a4a893fb32 | -6.01418 | -53.53098 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6220a758-89ab-3d3f-b34d-ea4fe4e211ec | -2.78403 | -57.62349 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c49d4a74-f158-3a23-8d40-c17ff0b0e038 | -1.5359 | -54.54122 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9ffcee19-d933-3c32-9f2c-933cd6cf3ec6 | -2.14016 | -56.70565 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 26f1dbf3-603f-3938-a472-5fd326b1266f | -6.14764 | -47.9365 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb6ced6d-04cb-3bae-aa5c-7088b82837c9 | -3.81418 | -44.60031 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| eeb04c64-ad8a-30e0-a2a5-76a8b33d0e0a | -6.91853 | -59.27148 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f2fa88db-3ffa-3324-8bd3-057d556dc7ff | -2.39295 | -56.12697 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac1ded04-9b96-3ffc-88a7-0bea9e619d14 | -2.8556 | -57.46494 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f75d4062-a2e8-3554-85c2-9ebcd0b3a6f3 | -4.08135 | -44.10792 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 28c50a06-2ccd-3548-9147-020ff8b880d1 | -3.0157 | -51.01048 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 31265cf7-9dfa-311c-941e-ab626997db38 | -3.65632 | -40.92866 | 2026-10-08 16:39:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1087592e-30f0-3ed3-8de1-91d83fec382e | -2.57546 | -57.44594 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README361.md)
