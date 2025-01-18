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
| fe9cb3e1-bfbb-37f3-b362-539aa583ca52 | 3.2989 | -59.966 | 2025-01-18 01:28:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4576cfef-6de3-3429-9258-74d7134c2ac9 | -9.2559 | -60.314499 | 2025-01-18 01:28:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 413a3104-4832-3d49-8ef3-b674ae0598e2 | -22.8409 | -53.505901 | 2025-01-18 01:28:00 | METOP-B | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9a96aae-2924-37cc-9990-89667be15829 | 3.113 | -60.763199 | 2025-01-18 01:28:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8f490005-0f2f-3c7b-a0ee-fd8074346045 | 0.074 | -60.653 | 2025-01-18 01:28:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f9592dbe-21f9-31c6-b4ac-c81cc162edf3 | -22.836901 | -53.490799 | 2025-01-18 01:28:00 | METOP-B | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc3cc164-a2b0-33af-958b-ce082c909ca4 | 3.286 | -59.978401 | 2025-01-18 01:28:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 293f1a63-0ef8-328f-8dff-5031baeb0fc3 | 0.0838 | -60.655102 | 2025-01-18 01:28:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15f6cc07-8c97-35a6-be76-5381617e3144 | 0.0811 | -60.666698 | 2025-01-18 01:28:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ae463efc-7c3e-301d-9290-f28431d1bac8 | -22.8505 | -53.502899 | 2025-01-18 01:28:00 | METOP-B | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a48ca266-b994-3fec-9687-8a25642b8513 | 3.1228 | -60.765301 | 2025-01-18 01:28:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dd496ba0-03f2-38b8-8973-e081b76b1d21 | -21.877399 | -56.109501 | 2025-01-18 01:28:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 40119273-ab6b-35a5-9a3d-565825f03993 | 0.0766 | -60.6413 | 2025-01-18 01:28:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 05a9e080-f1ba-37e0-8ee9-552d357a68ab | 3.1158 | -60.7505 | 2025-01-18 01:28:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cae14dbe-f7c3-334e-905f-bbcdbc44d711 | -9.2538 | -60.305401 | 2025-01-18 01:28:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26e2a381-609e-3acf-b860-9f8a900af4d6 | -22.8449 | -53.520901 | 2025-01-18 01:28:00 | METOP-B | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3f00363-8ecc-3b70-9dbb-a8a76b69eda8 | 3.2891 | -59.963902 | 2025-01-18 01:28:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7c327005-1eb8-369a-b66e-0a0f6d5eb1e4 | 4.1367 | -60.0093 | 2025-01-18 01:28:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 20147ec6-8c9c-384c-b23e-ace812ed0161 | -21.874701 | -56.098598 | 2025-01-18 01:28:00 | METOP-B | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c915b62e-b8b7-3769-9da2-e66fee6c3b18 | 0.0713 | -60.6646 | 2025-01-18 01:28:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aff2d892-83d9-34e4-bded-d59c05427038 | -22.8585 | -53.4947 | 2025-01-18 01:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 106.9 |
| 0755641c-2992-3f4e-a68c-8a1a3f698d2c | 0.0638 | -60.6584 | 2025-01-18 01:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 128.0 |
| a849d656-d4b2-3a23-8549-6209010a9365 | 0.0638 | -60.6773 | 2025-01-18 01:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 383c6a36-0dd7-31be-aa45-78eeacef95ae | 0.082 | -60.6584 | 2025-01-18 01:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2d4d7ed0-91a5-3d28-bbc8-88750b749001 | -22.8579 | -53.5169 | 2025-01-18 01:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 2d05c4c1-fc98-3dfa-886f-9fbd542fbe5b | 0.0638 | -60.6773 | 2025-01-18 01:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1d175b8a-1470-3ac9-b206-5fbb6bccbd2c | 0.0638 | -60.6584 | 2025-01-18 01:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 73f94314-4f68-3bc8-acfe-3b720ddf91f9 | 0.0638 | -60.6584 | 2025-01-18 01:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 2b2017ae-892b-3a54-9a97-d0c9964ec9af | 0.0638 | -60.6773 | 2025-01-18 01:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 236fd17f-6175-3f6d-b683-8e2a8c96c188 | 0.0638 | -60.6773 | 2025-01-18 02:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 02ae30b1-7da3-3e99-92a7-9218d40a6a47 | 0.0638 | -60.6584 | 2025-01-18 02:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 061482eb-fac8-37fc-ab1a-11d566fba68e | 0.082 | -60.6584 | 2025-01-18 02:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 0fd17193-330d-3adf-a885-303e1dac5174 | 0.082 | -60.6584 | 2025-01-18 02:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f714ef51-6175-3a64-bcf3-f5c704b1f844 | 0.0638 | -60.6584 | 2025-01-18 02:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5cc9deed-b814-35a9-a089-1f6b70c47241 | -22.8585 | -53.4947 | 2025-01-18 02:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| e96a3579-1cea-352a-a31b-d0e3b971e68e | 0.0638 | -60.6394 | 2025-01-18 02:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b89510b0-ec31-3b6d-a18f-753a3fcd4231 | 0.0638 | -60.6584 | 2025-01-18 02:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 1fb10352-462e-3db1-b079-42173cebdd3d | -22.8585 | -53.4947 | 2025-01-18 02:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 97.7 |
| 32175fc6-4f4e-3db2-bdd0-9de044f38582 | -22.8579 | -53.5169 | 2025-01-18 02:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| b9b26dc6-522d-3533-b2a3-54646ddadf0d | 0.0638 | -60.6773 | 2025-01-18 02:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 09c3f036-604b-396c-b8a4-a761476889db | 0.0638 | -60.6584 | 2025-01-18 02:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3cc21206-4f4b-30e0-9ccf-048b7f8b8a6f | 0.0638 | -60.6394 | 2025-01-18 02:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0e5b95c2-56d9-3d73-893b-5bae9ad486b9 | -22.8585 | -53.4947 | 2025-01-18 02:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 20b43963-b6d9-33c7-b029-c0195f26a222 | 0.0638 | -60.6584 | 2025-01-18 02:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d11d024e-b6bb-337a-a63d-c8c8f632915e | -22.8585 | -53.4947 | 2025-01-18 02:40:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| a837ccfb-2be9-3728-b80a-fd2daaba752d | -22.8579 | -53.5169 | 2025-01-18 02:40:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 05135f96-d7ed-325b-8593-42f3ace9f55d | -22.8585 | -53.4947 | 2025-01-18 02:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 281.4 |
| 35a4a29d-8d7e-3b7e-af28-28ce55f163a0 | 0.0638 | -60.6394 | 2025-01-18 02:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 3a46425a-2690-30c3-a4c3-0cf8d6ff02a8 | -22.8579 | -53.5169 | 2025-01-18 02:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 287.9 |
| e45ede4b-a258-3457-9fb5-88e0698a768d | 0.0638 | -60.6584 | 2025-01-18 02:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 77f6b0df-6304-3fa1-af19-0a63f61534ee | 0.0638 | -60.6584 | 2025-01-18 03:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3786eb83-f31a-3605-ba18-6d4b758fbcc8 | 0.0638 | -60.6394 | 2025-01-18 03:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 4242c538-bf1c-30af-a378-284598d0c08b | -11.75319 | -38.5246 | 2025-01-18 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2d80e2c-9bf0-35d6-a27a-5ea71a7c4618 | -11.74697 | -38.52535 | 2025-01-18 03:06:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c67aa15b-d72d-3871-ae9d-e01e56b94ea5 | -11.75299 | -38.52698 | 2025-01-18 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74d1f524-4791-31da-8d05-8b1ed6421105 | -11.74716 | -38.52302 | 2025-01-18 03:06:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 352aeba4-54ba-3e9b-8caf-4261fcd830be | -22.8376 | -53.4988 | 2025-01-18 03:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 133.4 |
| d8d78c65-cdba-336d-be1c-eae09ef982ec | -22.8794 | -53.4905 | 2025-01-18 03:10:00 | GOES-16 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 113.6 |
| 59a4ae00-e783-3430-95eb-0938b5f92aa6 | -22.8788 | -53.5128 | 2025-01-18 03:10:00 | GOES-16 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 128.5 |
| 494df9b3-fcda-3a62-8964-1e5ef2162610 | -22.837 | -53.5211 | 2025-01-18 03:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| 83377a8b-fe04-3ec4-897a-643f85ae9210 | -22.8579 | -53.5169 | 2025-01-18 03:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 324.8 |
| 52226f5f-5922-340a-84e5-31373819e5c4 | 0.0638 | -60.6584 | 2025-01-18 03:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cde2b69d-3f29-34de-a57e-6e3833be79ed | -22.8585 | -53.4947 | 2025-01-18 03:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 329.0 |
| 501fda6d-9c28-3e05-8a42-b383beab08a6 | -22.67697 | -42.85829 | 2025-01-18 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 37fc8564-a953-3a04-a2b7-3c6848f2edf4 | -22.8585 | -53.4947 | 2025-01-18 03:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| 19aab71f-a728-3a1d-b33a-b3c6ae891b70 | 0.0638 | -60.6584 | 2025-01-18 03:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d8f9df28-68ac-3df6-a420-ee12c2dd4e91 | -22.8579 | -53.5169 | 2025-01-18 03:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| 96a3efdf-e95d-32b1-9b5d-8f911ad0a672 | -4.92611 | -40.6896 | 2025-01-18 03:27:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64a18d45-c0de-3138-8755-246f7c7eccd4 | -9.76367 | -36.9666 | 2025-01-18 03:27:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3238be61-5f13-3085-a5a4-70393b656581 | -5.95199 | -39.68303 | 2025-01-18 03:27:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c8da029-ccd5-3ef0-9379-3c1ddc922e87 | -4.92586 | -40.68737 | 2025-01-18 03:27:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad039906-ff53-39db-bc4e-cf84bc2ab028 | -5.95049 | -39.68363 | 2025-01-18 03:27:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f097e526-ab37-3ba9-9766-8a1271908da3 | -17.3171 | -39.57922 | 2025-01-18 03:29:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 16fb6b01-9777-303f-a608-28fe7dbbedd1 | -11.74685 | -38.52239 | 2025-01-18 03:29:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91c291cc-f223-3994-82db-c156738a2c79 | -11.74621 | -38.52605 | 2025-01-18 03:29:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3617633d-cf1c-30a2-974f-9bda663beca6 | -11.7509 | -38.52322 | 2025-01-18 03:29:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4950153-c2aa-3726-a6fd-ffa53acc9acb | -22.8579 | -53.5169 | 2025-01-18 03:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |
| 7cddf73c-ffdf-3168-b44b-50eda40a0a89 | 0.0638 | -60.6584 | 2025-01-18 03:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1aeddb84-6039-3430-8484-ec634033132a | -22.8585 | -53.4947 | 2025-01-18 03:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| ba1017fb-1543-33aa-8ebd-e6430e0c3ab1 | -22.85097 | -43.52599 | 2025-01-18 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1816a1d0-70b2-3bf7-a34a-01473009c936 | 0.0638 | -60.6584 | 2025-01-18 03:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e040072a-d360-381a-9a0f-fb22cc1a6f26 | -22.8579 | -53.5169 | 2025-01-18 03:40:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 105.3 |
| 6f9b2c4e-c75f-3f0f-a5d9-46db735b9fb6 | -22.8585 | -53.4947 | 2025-01-18 03:40:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 424ab980-6114-3a0a-a4f8-4614927eb1ce | -22.8579 | -53.5169 | 2025-01-18 03:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 122.2 |
| 1ecf685f-8a2f-351d-86af-a32d7e819f53 | -22.8585 | -53.4947 | 2025-01-18 03:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 589280c9-99c4-39ee-b4b1-3a286b9bca5d | 0.0638 | -60.6584 | 2025-01-18 04:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d2fb59d6-1a20-38b9-8e63-838b7a9634e8 | -22.8585 | -53.4947 | 2025-01-18 04:00:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| ac3cd3f5-fcb8-336d-bb2a-f858b9761356 | -22.8579 | -53.5169 | 2025-01-18 04:00:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| afb44644-e3c1-36b6-9658-0314c48bc792 | -22.8585 | -53.4947 | 2025-01-18 04:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| dfbb5b32-c198-39c3-998a-53a26282b524 | -22.8579 | -53.5169 | 2025-01-18 04:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| a2164043-f38c-3d69-b453-2761d9bfb6dc | 0.0638 | -60.6584 | 2025-01-18 04:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f28446dd-1744-3661-84ab-89d209eaee43 | -4.92721 | -40.68827 | 2025-01-18 04:21:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8681f54f-3cdb-3def-8765-438b37ae32ed | -5.96946 | -43.36477 | 2025-01-18 04:21:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47a274d6-b349-30cb-be21-f6bac2dbb3fa | -8.58152 | -36.65902 | 2025-01-18 04:21:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a570eff-0fe2-3400-9c94-6a90df586808 | -7.86625 | -43.08401 | 2025-01-18 04:21:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dd10dac2-5f87-35bb-bc92-50c7af6d3bc1 | -4.77493 | -40.4707 | 2025-01-18 04:21:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22bbdf27-902e-362f-b101-dcbd1a5b1a48 | -10.8231 | -37.16658 | 2025-01-18 04:23:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8145eb7-677c-39b4-9369-7772d4b23394 | -20.3127 | -45.58323 | 2025-01-18 04:23:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd584aa1-4fb9-3fd5-bbc7-c21fd69e5139 | -22.67721 | -42.85503 | 2025-01-18 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7992b2e0-f607-33fa-9f8f-4cebcf80fda4 | -21.19596 | -44.93763 | 2025-01-18 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
