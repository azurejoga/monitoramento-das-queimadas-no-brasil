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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ded400e-3126-351a-9aac-1cc2ae117160 | -9.4192 | -40.3695 | 2025-05-23 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| b44e7676-bc8c-3296-9cfb-0c1e008ed8ac | -9.4383 | -40.3668 | 2025-05-23 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 36818f94-b79e-3ad2-9104-217c717f61b8 | -13.9818 | -56.0151 | 2025-05-23 01:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 027cd86e-c8f4-36fa-baf5-d6bf566a579e | -9.4379 | -40.3917 | 2025-05-23 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 3c8a86dd-61fd-3f5a-b08e-a8676bbf8788 | -11.7796 | -44.2762 | 2025-05-23 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 6d42cb57-fb8c-323d-95fa-38ba0e311040 | -7.0695 | -44.9335 | 2025-05-23 01:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fa0ce48a-3e85-3fed-8524-e2f584c1f15d | -9.4188 | -40.3944 | 2025-05-23 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.9 |
| befac986-25d2-3ab0-9df0-a64b9c2a035f | -20.85551 | -53.76616 | 2025-05-23 01:52:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 56cc4473-b52b-3c28-bee7-53f06b98db83 | -13.97767 | -56.0056 | 2025-05-23 01:54:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ae6c0081-fc95-3177-a6d7-7108efda1f0c | -13.986 | -56.01067 | 2025-05-23 01:54:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 193.1 |
| a4367ce1-07e9-3488-8d0a-e1f8e80858f7 | -13.984 | -56.03978 | 2025-05-23 01:54:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8d471da4-fb10-39ea-91bc-1dde98747f95 | -13.99208 | -56.04489 | 2025-05-23 01:54:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| a598bb8f-97c3-3e2c-aad3-d9085c29c1f8 | -6.2224 | -43.3693 | 2025-05-23 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 620bd92c-91ed-3c04-8bf9-f6e767d1b738 | -7.0695 | -44.9335 | 2025-05-23 02:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 361463a4-54a3-3da2-a885-9471bae295fa | -13.9818 | -56.0151 | 2025-05-23 02:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0592a065-3fff-31be-a830-0078ba185438 | -13.9821 | -55.9947 | 2025-05-23 02:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 481acbfc-0a65-35bc-aa3d-26b92893ebc7 | -7.0695 | -44.9335 | 2025-05-23 02:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c3af0381-35d9-320d-9d64-5e218c2e2756 | -12.3324 | -49.9857 | 2025-05-23 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1d3b2962-6684-3afc-ba6b-429c472099c3 | -6.2224 | -43.3693 | 2025-05-23 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b0318d00-e972-3d61-9ee6-bb77697326cc | -13.9821 | -55.9947 | 2025-05-23 02:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 70f282f4-93e1-3931-b004-d88bf3a7b8ae | -13.9818 | -56.0151 | 2025-05-23 02:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fe78eb20-eb7a-3618-9f85-ee0c31b15e7d | -14.001 | -56.0131 | 2025-05-23 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1244be50-8842-3d25-8e0b-2a383ca6de32 | -13.9818 | -56.0151 | 2025-05-23 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 0c1ca081-948a-317d-aa9e-adb61caeba09 | -11.7796 | -44.2762 | 2025-05-23 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 79c4811a-c996-329d-a7f6-b094976577a1 | -13.9821 | -55.9947 | 2025-05-23 02:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 2816a34a-ad61-35d2-b550-8089a7573d85 | -7.0695 | -44.9335 | 2025-05-23 02:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7a3fc398-1931-3005-a3cb-f4dd191c4cf2 | -6.2224 | -43.3693 | 2025-05-23 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dca7ab42-ee1e-3abb-9708-7a110ebf1105 | -13.9818 | -56.0151 | 2025-05-23 02:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 35b0a332-afe2-39d9-abc7-dcdfb89f62aa | -9.9639 | -49.8002 | 2025-05-23 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 23041219-7146-3c61-bc65-4fa8679ed5de | -13.9818 | -56.0151 | 2025-05-23 02:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7abe30ba-52d3-309e-a204-ba0374a5d664 | -7.0695 | -44.9335 | 2025-05-23 02:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9ee5964c-8704-398a-bfe1-0b406598e9df | -6.2224 | -43.3693 | 2025-05-23 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9ff6da09-ff1d-34b6-b2ec-734c1ada4117 | -14.001 | -56.0131 | 2025-05-23 02:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| bea7e39b-4fe9-39f7-8d50-1fdda30d3062 | -13.9818 | -56.0151 | 2025-05-23 02:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3c7a996f-cd18-34b9-9ca7-d7c605b47565 | -6.2224 | -43.3693 | 2025-05-23 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 2023ea11-d73e-3078-b65a-af1bb88b9c28 | -6.2224 | -43.3693 | 2025-05-23 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 00febbfa-a6ce-3203-b818-b5e9c9504fa1 | -13.9818 | -56.0151 | 2025-05-23 03:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 7e812b08-4ced-3223-b997-cd1f5827577a | -13.9818 | -56.0151 | 2025-05-23 03:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4de609c2-e058-343d-a035-812769b9a122 | -6.2224 | -43.3693 | 2025-05-23 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| da870f3a-c2b0-31d5-bca4-17a487744263 | -13.9818 | -56.0151 | 2025-05-23 03:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| af89d70f-727f-3040-98aa-a186acf1b51a | -7.0695 | -44.9335 | 2025-05-23 03:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 89adc7d5-4146-367c-a741-c3a738595165 | -6.2224 | -43.3693 | 2025-05-23 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f092f148-5f30-3c86-9838-60e6c9a379cd | -13.9818 | -56.0151 | 2025-05-23 03:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e6476b22-ed5a-3ffd-9cd8-d8a634728bcd | -14.001 | -56.0131 | 2025-05-23 03:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 23cbce98-73db-35bb-9184-175eba0473c0 | -6.2224 | -43.3693 | 2025-05-23 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3009f668-93d7-3b12-87fc-b5d8854c3ada | -7.23723 | -43.11018 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| aabdd9f1-4531-3a48-a395-063fb39da503 | -5.75947 | -43.48509 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2282b011-27e0-38a4-9769-f25a463d02d4 | -6.94783 | -42.79501 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 947775a5-e7bb-3173-8f64-4ee815f558db | -9.04436 | -47.75421 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ff82eb7-32cb-3a6b-be55-c1ce744adc81 | -7.21145 | -43.13037 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f20e2867-1107-3412-b260-f96e5e1672ed | -6.23066 | -43.36087 | 2025-05-23 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19dacdde-4221-31ec-866d-66013ccf4ccd | -7.20364 | -43.09401 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2c6abf6-5d5a-3932-a6a7-180d7e6cf577 | -7.06745 | -44.92777 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f700ba5f-1893-3e8c-a4e2-b2e0e1da55ee | -7.21374 | -43.1308 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e4cc5245-f893-3739-b3cf-15ff4b5f7a4b | -7.7178 | -45.66018 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d4184ac-171c-3598-a570-10cd2f7df8b2 | -6.94897 | -42.79131 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8149d1d-5df8-3b2b-a7ce-d16130a7b00e | -5.76144 | -43.48736 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b319679-4401-3e63-8ac6-c09e45f9e4aa | -7.24356 | -44.72046 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ed79f8-55ad-3993-8494-5dc2d3949092 | -7.2376 | -44.71949 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4755905a-a74b-3870-8ab1-32c9fccafd67 | -5.76077 | -43.49124 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfda64f-60aa-3037-b4c9-6f389f68a0d9 | -6.94316 | -42.79348 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ac5a176-163a-3d53-97b5-e2fa9944eb73 | -9.03931 | -47.74546 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb455a0f-c69d-3374-80db-298d04f76f27 | -7.65536 | -46.10646 | 2025-05-23 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c9752c9-c157-3332-9408-25e93e0a6267 | -7.65613 | -46.10818 | 2025-05-23 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce0285af-fb14-31aa-9f76-9b94744e6890 | -8.50012 | -41.01135 | 2025-05-23 03:36:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e218c8a2-1cef-3af2-8f7a-d8569aa5babc | -7.71689 | -45.66515 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa01fafc-9364-3161-930c-6136f540ad2e | -7.21434 | -43.12738 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3b2dcbeb-3a01-3333-b855-b97fa625812a | -7.20959 | -43.09153 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 613f5832-9de9-335d-b5b0-63d5f822bd89 | -6.94841 | -42.79454 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b4958195-5975-39d6-88e7-66aa21408bb0 | -7.21207 | -43.12696 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 96fdb936-9fc0-30fb-900e-2b70c90ac718 | -7.23245 | -44.71408 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5755bd2e-c7f1-328a-b3ab-a8cc52ce25d1 | -7.07706 | -44.94343 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 96a64f71-f88f-3ac7-9a72-6b7e29a92426 | -6.94842 | -42.79178 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51801de3-17c3-3bf7-be71-001bb2de40ca | -9.03874 | -47.74656 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8a84d0f-a52c-3487-8d5b-a8e1474fb4da | -9.04498 | -47.75315 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f4f509e-10c2-35de-8951-6040af93b834 | -7.71528 | -45.66166 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ac6e87ea-8d94-322a-a6a5-3f6d861b3a2d | -7.65721 | -46.10252 | 2025-05-23 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b466f202-fbc9-3e8e-ae02-c49538b68e14 | -7.20777 | -43.13335 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1091fa3-648f-35b4-84cb-55dbaaa2638b | -7.06656 | -44.93267 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e2b01739-d0bf-3cc0-bc42-8aaceb0112e1 | -6.23001 | -43.36451 | 2025-05-23 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f61df0a5-f383-3662-b6a1-102ca197b1f7 | -5.78768 | -43.6211 | 2025-05-23 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cb6c7a0-e02c-343b-9970-b8250f1bfd1f | -7.71064 | -45.66401 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d851711e-9f49-3f76-843d-890e2a97a1ec | -7.71622 | -45.65672 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1c83f0be-6a1b-3646-90d6-39687907c8c0 | -5.78338 | -43.61235 | 2025-05-23 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1279f687-8bcf-3cb1-9ea6-9a51f4d2002c | -9.04565 | -47.7478 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8b0f0ea-f85f-3fa1-85b5-152e993b826a | -9.02491 | -47.74407 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e62834ce-7751-305b-a51a-6b62a052f5f8 | -5.75879 | -43.48894 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2b3eed8-0825-34e0-be08-5b230de4a445 | -7.71156 | -45.65903 | 2025-05-23 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c64cf95-578c-3826-bc33-c143f694308a | -7.20304 | -43.09744 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ecc992f-6fb5-3b5f-b482-e6cd97633c1d | -7.20837 | -43.1299 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1f3adad1-294e-3001-9805-882ad167a5ab | -9.02298 | -47.75574 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0096e57d-f118-3949-917e-7063761610d0 | -9.02424 | -47.74929 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b3ad4de-c600-3613-a8cd-46267cc19380 | -5.76444 | -43.48972 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4599165-56ab-39dc-b5b3-cfcd5a4be191 | -9.02362 | -47.75042 | 2025-05-23 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0a283d3e-3062-3cb9-9fd9-50f19f17ce76 | -6.94372 | -42.79027 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58b820f5-454f-3e44-a3a1-457dca150a4d | -7.07183 | -44.93793 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 840276ef-b852-3da6-a7c6-9b87a33bf9d5 | -5.7827 | -43.61621 | 2025-05-23 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a45c13e-6fb6-3511-8904-a808a3e8157a | -6.94784 | -42.79778 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3cacad2f-1f49-3f41-9fa8-e57054fb9a10 | -7.21744 | -43.12783 | 2025-05-23 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 06cd54de-eb91-3991-bae5-07f2330e1ac2 | -5.97419 | -43.75241 | 2025-05-23 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README6.md)
