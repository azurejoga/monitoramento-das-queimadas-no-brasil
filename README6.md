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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7aa614c2-d677-3273-bdb3-e71c0d0beda9 | -14.15221 | -39.01271 | 2025-12-04 03:32:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d081526a-4601-321d-abcc-8b294d7d563c | -13.00623 | -40.54424 | 2025-12-04 03:32:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0e3114e-66e0-3d75-bdfb-c7465b16e027 | -15.46372 | -39.23704 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 203d5403-137c-3651-bdad-befd13cab656 | -15.45846 | -39.24342 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5648c0d8-ec55-3d4e-88d3-70717d13df16 | -15.4591 | -39.23985 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2279789d-d47e-317b-b923-f296494b9b57 | -11.41489 | -40.82113 | 2025-12-04 03:32:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94cda731-a194-3b3c-a12f-832081758e58 | -15.45512 | -39.23909 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 20e7bf5d-5c89-3734-a6f8-c1f304c4413e | -19.6442 | -56.8311 | 2025-12-04 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 76c38a89-8d3c-314a-b331-9e85a8d8933e | -19.6241 | -56.8339 | 2025-12-04 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.9 |
| 8b8f131d-6312-3dc7-af6a-d4388b8f6c1a | -19.6237 | -56.8549 | 2025-12-04 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.8 |
| a8a2f196-fbad-3621-831d-43421571cb27 | -4.4079 | -43.1252 | 2025-12-04 03:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| bbdd4dd2-2650-3bbb-ae92-ed160fa8995e | -3.7212 | -45.5859 | 2025-12-04 03:40:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0407180d-59ae-3d28-9417-f27c66858e31 | -19.6241 | -56.8339 | 2025-12-04 03:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 672b1a14-92d3-31bc-9e79-0f479d678c2c | -3.2239 | -48.6094 | 2025-12-04 03:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c2446140-90e1-3701-8976-ecc9d2defd12 | -2.5367 | -49.4618 | 2025-12-04 03:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 178c05a1-327f-3b39-a21d-10a118336fc6 | -4.4079 | -43.1252 | 2025-12-04 04:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f69e5c01-8d7c-3f74-b8c7-ec32a0df526f | -4.4079 | -43.1252 | 2025-12-04 04:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 898f8cb1-0a71-39ed-9a95-f3b44edf613d | 2.91546 | -51.00994 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce3187af-ad59-3164-960f-db1f431d46a2 | 2.52654 | -50.8456 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf3db645-0576-3b68-84ff-ed5bfd6ddb07 | 2.52282 | -50.85493 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bde40715-ae58-3c5c-ad29-654e240d58ea | -1.69594 | -46.14814 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1b6d52a-6a76-32cb-80a1-5001b0179cd7 | 3.67238 | -51.28458 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a874442-a4bc-349b-8395-cd7ca9cffef2 | -1.69534 | -46.15202 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a284aef-47f3-3522-b276-583637a7208c | 3.58146 | -51.28831 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5603e6d6-efec-38e5-af44-6b004c655761 | -1.50335 | -46.07994 | 2025-12-04 04:18:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd890b9-5355-307c-b284-b6aa08a24aac | 0.41122 | -50.757 | 2025-12-04 04:18:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d625b373-b697-3e9d-8be2-98830e961f78 | 2.52611 | -50.84279 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a746f82f-ad18-37bb-9643-53fecf3ff0e8 | 0.18272 | -50.03222 | 2025-12-04 04:18:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af6143a4-95b1-3562-a745-aee158c3e35d | -1.69884 | -46.15256 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc21991c-322d-3ebf-b562-b3adb28378a4 | 0.3239 | -49.73119 | 2025-12-04 04:18:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e264159-4b79-31c4-a1b8-8b282a2edcca | 3.46942 | -51.25675 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df6b44d8-3dd6-3782-84ce-b816779dd4ab | -1.29803 | -46.12387 | 2025-12-04 04:18:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d87f87ef-224d-35d1-a93d-d404796ca8b0 | -1.67386 | -45.79239 | 2025-12-04 04:18:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5f6d94a-44f2-34c3-af2c-0ae6e99e371e | 2.91591 | -51.01291 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fd95aff-a8d7-3ec7-be77-83a1b710385f | 0.41127 | -50.76022 | 2025-12-04 04:18:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5d31ddc-4a88-3a11-9018-e8815cc42650 | -1.69473 | -46.1559 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f48873e-2f94-3fbb-85f2-1bdff31ee749 | -0.37377 | -52.05014 | 2025-12-04 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3eea0397-7e1e-3305-8340-d4bb4e51aecb | -1.12167 | -47.7402 | 2025-12-04 04:18:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba783e7b-1298-32e7-b478-b87ec020f5b2 | -1.62998 | -45.42852 | 2025-12-04 04:18:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc65fe21-2559-36b5-9013-11f06402e7e7 | 3.46467 | -51.26064 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c2c78fa-d529-3635-bfd2-0fbb3ab673a1 | 2.91636 | -51.01587 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4888c5d4-1a92-3483-9c76-5fee5f5cd945 | -1.74992 | -46.20021 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34219870-099f-30bd-97bf-5b24be7f36b9 | 3.46514 | -51.26381 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fcb7017-a228-3077-a1c6-4cdbe0572833 | 0.41048 | -50.75497 | 2025-12-04 04:18:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e0b8409-62e9-3253-9e9c-c940cf246434 | 2.52239 | -50.85205 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56929c01-874a-32ed-8869-c3aa9c1690c3 | -1.69823 | -46.15644 | 2025-12-04 04:18:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e2c9aec-16d6-3c97-8fa8-464c6f7ab86d | 3.46895 | -51.25359 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93aa0903-e7a0-3b63-bd7f-3eacfb27d2e5 | 2.53112 | -50.84209 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfb48e24-0ce1-3a4c-9bc4-7cc0e1d48cb1 | 0.30879 | -49.81096 | 2025-12-04 04:18:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc73762-b155-3b80-872f-38979de7cc7a | -1.16399 | -48.86314 | 2025-12-04 04:18:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21c7f131-9766-36e1-b4e5-cb279087e616 | 2.5307 | -50.83927 | 2025-12-04 04:18:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbe543a-908f-3090-a71a-e0cf641513a1 | -1.6704 | -45.79186 | 2025-12-04 04:18:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 945d6425-9e25-3d59-983d-928bf5a31d74 | 3.58623 | -51.28438 | 2025-12-04 04:18:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efed9497-85a0-3ab1-bb3f-378dd4bbd2c1 | -1.67326 | -45.79615 | 2025-12-04 04:18:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 869e12c6-2ddf-3e4f-bd68-31f67e84fef6 | -2.00624 | -45.33389 | 2025-12-04 04:18:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 775416ef-fc49-3d09-a9f7-8b31062bded1 | -0.78281 | -48.63182 | 2025-12-04 04:18:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eea2d7f-ca94-34a5-aec3-63efafe7c671 | -2.5328 | -45.3618 | 2025-12-04 04:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 822424ff-d5e4-3e2e-b1a2-1bf91a6c0871 | -2.83375 | -48.02098 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c5bdf4-04a7-3b9f-a240-aa335364ca24 | -3.51874 | -47.20269 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fcc9fc26-6204-337e-98a1-e5766397e40c | -2.8759 | -45.36234 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c6dc784-c4fe-3264-b1bf-e83a14cf13b4 | -3.04854 | -48.42761 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 71e9614c-250d-32a2-99d8-df6f9cd55a69 | -4.40243 | -43.13239 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2715f230-cbb1-3d12-9822-b96442cf96eb | -4.59394 | -44.34531 | 2025-12-04 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71bf10bc-1d26-38f0-aaaa-3c14c606a3ce | -4.24413 | -40.34776 | 2025-12-04 04:21:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c126c7b1-ec3f-33d9-8f32-287ff3764fe5 | -1.12191 | -53.44724 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f881fcc-6538-3aa2-96b1-b5db91cb1917 | -5.34691 | -42.12163 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85019d4b-06be-3547-834e-a422497298a5 | -5.02951 | -43.97621 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb1ed324-4039-3209-9667-503130190823 | -4.21142 | -44.24973 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8638d3a-5410-37ad-bbbd-06fdd4adb3ff | -5.83695 | -43.26622 | 2025-12-04 04:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4157219-bef5-3d19-b8ad-f9a42fba605d | -3.23689 | -43.345 | 2025-12-04 04:21:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0e2aa6-0e77-3710-b09d-316dad7e6ef6 | -2.38699 | -49.39202 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45ad8ff3-3e49-38a3-9c79-101a31408654 | -2.64039 | -48.54113 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 460884ec-3699-3ca6-8b34-8cdedaf05a5d | -3.19924 | -41.50047 | 2025-12-04 04:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34621456-baa1-3937-bce7-c7b48eae68c7 | -5.55639 | -45.38551 | 2025-12-04 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e5f55c9-cabc-329f-93ec-2a3409697047 | -4.39912 | -45.83611 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e28bddb0-01f3-35e6-a2a6-e19ea7a2d4e3 | -4.55102 | -45.80473 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17041195-3a73-38cf-a80a-ea709d25c08b | -2.17337 | -48.36598 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bca9f8f9-a731-33c7-86d2-daffd4e87ac7 | -2.42063 | -45.7998 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ebc9e3f-52ed-31e0-9e1a-21ea7795d2ab | -4.41677 | -43.97865 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e69c1404-d075-3e8f-a114-071e9ae879c6 | -2.38587 | -49.39226 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9816c691-7782-32e9-90f4-6c3eacea328e | -4.26009 | -44.15511 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 373e9111-e762-3a06-b1a0-70a6c550836a | -3.9384 | -46.73794 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59972b2f-fe98-36e2-82eb-831ad92c04a6 | -3.13725 | -49.4129 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d212f36-07eb-3d65-8851-de7e9924e2fc | -3.93503 | -47.20609 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fea1564e-626e-37d9-8428-38c47223bd28 | -5.34461 | -42.11342 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36e2e77d-6263-3381-9e6a-9217c8490c4f | -4.70027 | -46.43486 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb89efd1-c83d-3124-9d91-79feac7961d2 | -4.52973 | -44.23666 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 417a41ec-3975-3c1c-a5de-94070e8b9064 | -5.34808 | -42.11395 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dcfc2a1d-b853-391b-a1db-24f7f07b2c10 | -4.47873 | -44.25677 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2741397b-a81d-3265-858f-a712b71e0a93 | -2.07655 | -45.31485 | 2025-12-04 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1918f01b-c55f-3586-9ac3-78d9cdd56627 | -4.33113 | -45.81834 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e636ff-8307-39d5-910f-67164ea7196a | -2.38845 | -48.66036 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c9eb3ef-27ae-335e-ab71-c6ca90c25190 | -4.53242 | -45.618 | 2025-12-04 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9850bd-c560-302c-9a94-878c269bc588 | -5.02153 | -41.01439 | 2025-12-04 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6bd41f7b-09fb-39cd-9698-ae31bdd0a7da | -4.7239 | -45.09927 | 2025-12-04 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf690c01-660b-379c-b518-4f2e45cc987e | -4.73993 | -44.43571 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49976bbf-8b4b-33c3-95f5-c77f24d0d774 | -2.06684 | -45.35409 | 2025-12-04 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0eeb6e9-1b4e-375b-8acb-17fcb9769fec | -4.55334 | -43.23495 | 2025-12-04 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed689d78-e324-3a08-a2b3-915b540a8c87 | -7.1476 | -45.43475 | 2025-12-04 04:21:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eda3738e-2c33-3dec-9dc9-82a76de1b09f | -4.69972 | -45.70624 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README7.md)
