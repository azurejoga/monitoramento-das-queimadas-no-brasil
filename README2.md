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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 962d766a-fb50-378e-a762-94fa53904f03 | -5.1178 | -43.2431 | 2026-01-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| fdfefeca-b730-34b0-9e7b-5bbfc7cc0772 | -12.8659 | -52.5194 | 2026-01-14 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| a39c4f54-c223-37b4-afa1-a2ab3b01c542 | -12.8276 | -52.5238 | 2026-01-14 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ade58bdd-5544-3c9a-86c5-bf3d72f57cf9 | -5.0992 | -43.2211 | 2026-01-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 378aacd0-1901-371d-8f64-6684d23b28a7 | -12.8659 | -52.5194 | 2026-01-14 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3774b0f4-2b92-3eeb-acde-f8513d0d7087 | -12.8468 | -52.5216 | 2026-01-14 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| cf6466d8-2ae9-35bd-ac29-154820dcc32f | -12.8471 | -52.5005 | 2026-01-14 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6df69ed7-84e4-38dd-b528-9d35f822a395 | -5.099 | -43.2444 | 2026-01-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 410907b8-37ee-3652-89cf-1ce5a833032c | -5.0992 | -43.2211 | 2026-01-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e4c2c1bb-fe93-3797-ba62-1e04e2955c32 | -12.8468 | -52.5216 | 2026-01-14 01:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 72c5b9d9-1355-31a0-9ad8-f1d791105b4a | -12.8468 | -52.5216 | 2026-01-14 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6cb8ba51-5312-3ff4-bc52-c57388517d02 | -12.8659 | -52.5194 | 2026-01-14 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 07c43958-8a02-3635-8b3d-7cd25e677abe | -12.8468 | -52.5216 | 2026-01-14 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 86ec97a6-fcd4-3764-9cf5-51545d2385c6 | -12.8464 | -52.5426 | 2026-01-14 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a4673790-a1f7-324c-b09b-1c1d672c52c0 | -12.8276 | -52.5238 | 2026-01-14 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 68212385-f425-36f5-b73f-aa6ee1841f35 | -12.8468 | -52.5216 | 2026-01-14 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 206.9 |
| c92fe072-57cb-3b23-9106-0bf540f76b30 | -12.8471 | -52.5005 | 2026-01-14 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f6521a8a-9e39-3f34-aecf-0d008e65b289 | -12.8659 | -52.5194 | 2026-01-14 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 17f6dd7e-a5f2-3b1f-a616-b85353bc2eff | -12.8276 | -52.5238 | 2026-01-14 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 1549b6ad-5c44-3fda-9d52-b477a88e67f0 | -12.8471 | -52.5005 | 2026-01-14 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4ac810a2-0e6e-3a1d-abb4-fb3e65d2fcbd | -12.8662 | -52.4983 | 2026-01-14 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5546658c-f0fc-3588-ae0d-e1069b51f102 | -12.8659 | -52.5194 | 2026-01-14 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f1839f25-9b80-3220-9652-9d3b06841ea9 | -12.8468 | -52.5216 | 2026-01-14 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| a1518ada-132c-3955-9c13-c176958f2ac9 | -12.8662 | -52.4983 | 2026-01-14 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7b941f17-452a-3f02-805f-2b02c5dc6ddf | -12.8471 | -52.5005 | 2026-01-14 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d089580b-f889-3830-8936-0b2bd8e11c24 | -12.8659 | -52.5194 | 2026-01-14 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 6b890495-25b5-3678-a8fc-45b94bcfdb56 | -12.8276 | -52.5238 | 2026-01-14 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ff2ed370-5a22-37a4-b620-55d9ce10126a | -12.8468 | -52.5216 | 2026-01-14 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 319ad6e1-215a-3245-85dc-27cea8e9ce45 | -12.8468 | -52.5216 | 2026-01-14 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 231.4 |
| f8220446-5f72-3c50-a46e-c778c46e1db8 | -5.099 | -43.2444 | 2026-01-14 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c4a3936d-c838-3bc8-b61d-cd6ea32a43f8 | -12.8471 | -52.5005 | 2026-01-14 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| da0f4a1d-b734-329d-a88c-79688dba2a87 | -12.8659 | -52.5194 | 2026-01-14 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 6b8db836-7833-3d0c-96b7-0bd17985a959 | -12.8276 | -52.5238 | 2026-01-14 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 25077331-1838-3bca-840b-28df73dd7899 | -12.8468 | -52.5216 | 2026-01-14 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 7e04785c-fcdb-3885-8ec1-16d465998542 | -12.8276 | -52.5238 | 2026-01-14 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 934c936f-c1d2-3f10-94de-88c9f7e688e5 | -12.8471 | -52.5005 | 2026-01-14 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5dcd1e6a-9994-31bb-bc15-183a8dd10440 | -12.8464 | -52.5426 | 2026-01-14 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ccef49c0-3ae7-3cd3-9d57-2e391ff5c462 | -12.8659 | -52.5194 | 2026-01-14 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 57676101-f93f-36c6-9585-49a9e845524a | -12.8468 | -52.5216 | 2026-01-14 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| bb52fa78-c6e9-378c-806b-b1e9d3479832 | -12.8471 | -52.5005 | 2026-01-14 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 06901804-cac6-3578-8303-e74c774ef1b0 | -12.8659 | -52.5194 | 2026-01-14 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 494767bd-c3ad-3ed7-ba05-455a7eb94d36 | -12.8464 | -52.5426 | 2026-01-14 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 435779f2-2a52-39a6-8ae7-aee01c6238f7 | -4.21354 | -38.11898 | 2026-01-14 03:10:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f4d37f36-cc12-342d-802d-cc8d6d713c10 | -3.89868 | -38.67284 | 2026-01-14 03:10:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f32ea01c-811e-32d6-9f60-3438f1274797 | -3.89234 | -38.67179 | 2026-01-14 03:10:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7049c615-de19-364e-838b-b369cfed4f3b | -4.21276 | -38.11892 | 2026-01-14 03:10:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 183b232a-3077-38d5-87d4-05b329852308 | -3.89496 | -38.67376 | 2026-01-14 03:10:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd9da7df-6c77-36de-85d7-b444c771608d | -4.49962 | -38.42943 | 2026-01-14 03:10:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 846fa7ab-1627-362d-9ee4-3143bb5a500d | -5.52314 | -37.77645 | 2026-01-14 03:12:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 57c11600-6166-3c65-83b5-f17864be3840 | -7.34261 | -35.10331 | 2026-01-14 03:12:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 690b064a-f416-32ab-9818-43a96c9967a4 | -5.66822 | -35.47108 | 2026-01-14 03:12:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b937f62c-a44c-3a78-bbe8-4450ebb8004c | -7.7437 | -35.31664 | 2026-01-14 03:12:00 | NOAA-21 | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d14cd0da-ca9c-31a1-be0d-86dc34bebd9f | -7.01524 | -39.65331 | 2026-01-14 03:12:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9425b752-0d05-3dd6-b673-1e2dda64cb1e | -10.19934 | -36.39277 | 2026-01-14 03:12:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 45fa30a6-fa62-33b0-9e89-e40efac0eb1d | -10.16448 | -42.21567 | 2026-01-14 03:12:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0da3f5de-6113-3691-bed3-31a872375cde | -6.48641 | -39.78965 | 2026-01-14 03:12:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ddd3b72d-06ba-364d-b770-ec7e89dbc85a | -5.66771 | -35.47402 | 2026-01-14 03:12:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84f570b8-7fe1-3030-a3b4-e4343a0af305 | -6.1213 | -39.21576 | 2026-01-14 03:12:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c13a7b2-8ae6-3521-a9ee-f3c455dc4362 | -6.5667 | -39.42895 | 2026-01-14 03:12:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c3f9fa3a-1e30-3dcc-a25d-2fc2b335b602 | -10.19443 | -36.3918 | 2026-01-14 03:12:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 46d140c8-d1d3-369a-bdf8-fcb54d8460c2 | -7.42958 | -35.28084 | 2026-01-14 03:12:00 | NOAA-21 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b8b15682-b75a-376f-a0e5-b774a313a7c8 | -6.12041 | -39.22071 | 2026-01-14 03:12:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fed24a8c-9919-3986-abf2-e3c62d840eeb | -10.16877 | -42.2169 | 2026-01-14 03:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f96ac610-043e-3dd3-87ce-73252ed6b61b | -10.17022 | -42.20995 | 2026-01-14 03:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f361cd31-d675-354f-ba70-4adc50840866 | -20.30635 | -41.62583 | 2026-01-14 03:17:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 791e9049-7046-331d-bf97-4664be36208c | -12.8468 | -52.5216 | 2026-01-14 03:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7d08bdd6-c499-3611-951a-c064c7095666 | 4.0578 | -61.4661 | 2026-01-14 03:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a7dcf5d8-a18a-3cb8-bffb-a3ca5d4aa75a | -12.8471 | -52.5005 | 2026-01-14 03:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 042a3ebf-7726-3e61-9019-d8a8adb280f4 | 4.0578 | -61.4473 | 2026-01-14 03:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| cd8bf73e-a57b-3c46-acd4-6e47232220cf | 4.0578 | -61.4661 | 2026-01-14 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9ea669c8-866c-3645-8416-1b1056ae685d | 4.0578 | -61.4473 | 2026-01-14 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 16705d8d-3fe2-3219-877a-f3cdf22a24e9 | -5.099 | -43.2444 | 2026-01-14 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ba5c72d2-2735-3472-846a-cd31c029f5fc | 4.0395 | -61.4665 | 2026-01-14 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 22c519db-5fc7-3554-9514-781baabe7817 | -5.099 | -43.2444 | 2026-01-14 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 10b26bfb-7ab8-342c-b5a0-119b582f70d1 | -5.49543 | -39.16336 | 2026-01-14 03:40:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b87eeae-cdf2-3f32-9b5f-342a44ab4556 | -3.89253 | -38.67318 | 2026-01-14 03:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a63a14f0-d8e7-36ba-9b94-83709353cbd0 | -4.46464 | -38.40991 | 2026-01-14 03:40:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c3b7336-9690-371e-8213-014ee208bdb2 | -3.97025 | -38.35881 | 2026-01-14 03:40:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44f4690d-0317-3a12-b3ba-04f0ded02b64 | -5.5234 | -37.77563 | 2026-01-14 03:40:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7d053f7-d3ae-31d9-a3d0-cc07f50b7bd7 | -4.50301 | -38.43088 | 2026-01-14 03:40:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5742cb9-031d-33cb-96ed-1983781417f3 | -4.25878 | -38.06898 | 2026-01-14 03:40:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4906d800-e504-3209-9465-3a8e016c9220 | -4.21349 | -38.11922 | 2026-01-14 03:40:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dd669272-8073-3836-81b4-c2fa2a4b9336 | -3.89316 | -38.6694 | 2026-01-14 03:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b345a23-fab3-3ecb-91b1-f917df92a1dd | -5.09676 | -43.23575 | 2026-01-14 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25f343ab-826b-3c71-87be-e4d0dc999562 | -4.5036 | -38.4273 | 2026-01-14 03:40:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c795a0fb-cb05-37ee-85d5-0a717d79e513 | -3.89734 | -38.67009 | 2026-01-14 03:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 37863a53-2dfc-33ae-b92f-c2798c34b502 | -3.89671 | -38.67386 | 2026-01-14 03:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22777f44-6211-318a-8fe0-7aa8bffc3637 | -10.16833 | -42.21405 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8b420d40-f496-3fbc-ac82-f5bd12a8eed1 | -7.6109 | -38.26106 | 2026-01-14 03:42:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15742515-7c52-3519-b95d-6f1032622b9e | -10.17311 | -42.21495 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 316de968-b6a7-34c6-a9fd-95ea0ddd1ae7 | -7.26443 | -43.05098 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 833d836e-ff17-388f-9bda-d63b63cf0d49 | -6.48259 | -42.94012 | 2026-01-14 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dabb407-ed2d-355c-9386-d615465ddcc3 | -6.12075 | -39.22054 | 2026-01-14 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51e618f1-031d-3865-8d26-3ac94bada864 | -5.10788 | -43.238 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1765050-c01e-372c-9ba1-a231a8b8139f | -10.2053 | -36.35574 | 2026-01-14 03:42:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cde48dd-9b53-3c32-9997-f1600987f886 | -7.17886 | -39.0527 | 2026-01-14 03:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 68d29055-6f2d-3542-94e0-bf98e1038737 | -10.20872 | -36.3563 | 2026-01-14 03:42:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 708d2211-3447-3cdc-b7d9-5e7611371350 | -10.48654 | -44.92955 | 2026-01-14 03:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3cde5e1-6190-307e-8c6e-25d7b45e343a | -7.24726 | -43.05478 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 63d8ff5d-13f9-343e-b402-ed8dc4e754a0 | -7.73915 | -35.31879 | 2026-01-14 03:42:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README3.md)
