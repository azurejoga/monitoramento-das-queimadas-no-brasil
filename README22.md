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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a2ca40-066e-3176-a70e-2d04cfa52c3a | -1.33405 | -49.32667 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8039db88-24a6-345d-823a-14d74dbd7b88 | -2.47637 | -50.23809 | 2025-11-18 04:18:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d8b8674-edb9-34d5-bd3e-8f70ae02d4c2 | -2.91512 | -45.90429 | 2025-11-18 04:18:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d726f8-8281-3d1a-80b3-fe09f5917583 | -2.57982 | -46.96846 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c59caa6-bf63-34fd-8b6e-2291c9998899 | -3.17394 | -46.60209 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a09401c-3fb9-3572-a575-8ead11702d03 | -3.068 | -45.4092 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85cf0b36-46e9-396e-80e7-e86a5fa76283 | -2.49828 | -49.34072 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0185775f-89d1-3420-a804-8a50deb0b740 | -3.17471 | -49.79985 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a0be78-44e6-30b3-b07c-d394c67ee028 | -2.99939 | -45.43884 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57bf0389-cd57-39ee-93a8-797aa84bab9c | -3.60257 | -40.96415 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a467dc27-2099-3260-b48c-e8ec4592740b | -3.17685 | -46.60661 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc5e132a-fa0d-3bd8-946e-cd80192a9dee | -2.91453 | -45.90804 | 2025-11-18 04:18:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c0a2aa8-fcc1-343e-a8ce-b64e1cc8d044 | -2.82072 | -48.45502 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e269c22b-312f-3ddf-a82a-b44d3cfe430a | -3.7559 | -40.76934 | 2025-11-18 04:18:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb5248aa-d491-3d88-8d26-9722164c3cb8 | -2.92253 | -47.85042 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebd05838-07c1-34ae-9d5b-d2205bcb6c26 | -3.60678 | -43.61092 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 149c36a6-25a2-3a57-a277-9ee91e0e5f0d | -2.51244 | -47.81764 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9a39ede-e6de-3f57-b722-8255e8e2e163 | -3.17478 | -48.60601 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171bbfd0-07b6-350d-83c3-b7ef7d39eb20 | -3.59608 | -40.95872 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4bd0bc6-3780-3cd3-81e1-9da59e9b020d | -2.82575 | -48.54909 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4036b6f-0ec2-3389-a89f-b9120c11b1a0 | -3.17747 | -46.60264 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6303a0f-3790-3990-9637-b4c61058c1eb | -2.28267 | -51.9286 | 2025-11-18 04:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22008618-5fc4-39ac-87f0-4eba63751c4f | -2.3831 | -45.73872 | 2025-11-18 04:18:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb4c9edd-4932-3bdd-8e22-c8771f01a82c | -3.84649 | -40.79074 | 2025-11-18 04:18:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 33c71359-d9f1-3674-be03-736f59d3a339 | -2.49644 | -49.35224 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b843936-108c-3bfa-b020-6259b8deeb33 | -3.61063 | -43.60799 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fdb217c-54a2-3839-b2e9-9db669540a60 | -2.89515 | -51.45567 | 2025-11-18 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8270d1-81d8-3f0b-ac30-9335b223c279 | -2.5193 | -47.82348 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57cf8f04-4b7c-3c74-8441-f3f47a99fe26 | -2.45463 | -53.80444 | 2025-11-18 04:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a79be92-75c7-372a-a75e-a00b86209254 | -2.4787 | -48.22869 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c0f3be1-f77d-35ce-8c2a-b895602d3975 | -2.91496 | -47.84925 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63fc273f-cf8c-3d48-9dc7-fbe70a24e383 | -3.19608 | -46.03584 | 2025-11-18 04:18:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb8c4754-ab2e-3f2b-8805-66015a5e2db8 | -3.02784 | -44.46077 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 630b6f57-21dc-3a92-804d-d741c7ddcfa0 | -2.97831 | -44.58088 | 2025-11-18 04:18:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 157445f2-466f-3119-ba6f-222cc2514884 | -3.47522 | -46.0714 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eab7a819-12d3-3cf5-b861-0d8b3e35c0ac | -2.58488 | -45.13152 | 2025-11-18 04:18:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d45178-d256-3988-8609-a70e54010e9f | -2.83022 | -45.41665 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 525cf306-b978-3ce8-88b5-9abb2daf0ff1 | -2.682 | -49.05406 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2315b0b-d80a-38e7-b09a-d005d4e74b95 | -2.50063 | -49.3529 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a7af22f-dab9-309b-8d2e-a666614d540c | -4.09127 | -43.20839 | 2025-11-18 04:18:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8723b46-a053-3a3e-bf04-d60fb1a51a28 | -2.44339 | -49.23045 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b9c38b-cc32-37b4-b831-88c374461461 | -2.47567 | -50.24249 | 2025-11-18 04:18:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8a5c503d-7b53-31e0-ac84-4f980492b1ce | -1.33832 | -49.32733 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be245030-13e1-3ebc-af3a-0028d9f32444 | -2.61 | -49.21378 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ef1717b-b081-3cb4-9921-f10fd9f882c7 | -2.91078 | -40.12239 | 2025-11-18 04:18:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5865a1c7-9f27-3b00-ac87-0a6fea49fb22 | -3.17832 | -46.57431 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe73d77d-ff34-3e0e-a4a3-35ae2d053489 | -2.37967 | -45.73819 | 2025-11-18 04:18:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6908d866-86bd-35f0-80c5-526eb488e220 | -2.92631 | -47.85104 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aa10442-7f18-39be-93a8-e5c36417b1ea | -2.83247 | -45.42443 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 496dc1a5-1577-340e-8de6-d4504b2601c4 | -3.181 | -46.6032 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7baa2f69-116b-3143-8db4-41153e9876f9 | -3.5941 | -43.60543 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d73c9ba-c9a2-3961-b1ee-ce3fe8357b89 | -3.08027 | -50.35321 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9999cbf5-cfc6-3954-a379-b135078ac816 | -2.81704 | -48.24943 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51785721-6dde-3053-b56f-6cd16fcf5122 | -3.47151 | -40.22953 | 2025-11-18 04:18:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d578fb9-1d0b-368c-a8ae-793d1e79ac0c | -3.91803 | -42.48581 | 2025-11-18 04:18:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f62b21f3-ba4a-344b-bb67-513c21d5665b | -3.60348 | -43.61041 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b381fe-0168-3d03-b409-3226d6e5f1ba | -1.76511 | -47.2642 | 2025-11-18 04:18:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1874f126-29bb-398d-ba13-da938fea8d08 | -2.99262 | -45.43779 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe37da2a-204f-3b1a-b1d7-6ab39a7f3b26 | -3.59965 | -40.95932 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2c1b249-04b3-3017-9761-771b739b2884 | -2.81026 | -45.14864 | 2025-11-18 04:18:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d152c7-d138-3409-b3c9-87ecc9cc708b | -2.45564 | -48.90229 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95f89fd1-e442-3eac-94a0-5e98faff0ca3 | -3.87162 | -40.45435 | 2025-11-18 04:18:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e25fdac-16e3-3227-abf2-f238fe5e8c80 | -3.56178 | -47.30522 | 2025-11-18 04:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f06ed43-1c8d-36c2-ae35-98313183ea37 | -1.80662 | -54.71938 | 2025-11-18 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d5c1d73-dbaf-315e-a1fa-1ab510c971e8 | -1.9171 | -48.79876 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98b8c823-c9b4-3e7c-8b52-1f8634b7a292 | -1.9292 | -48.7946 | 2025-11-18 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9f3f4155-8d8d-33ca-bc47-971c5e83e17f | -4.195 | -44.2247 | 2025-11-18 04:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 34f8ae3b-c98d-3ff4-b5fe-4bb6cf327002 | -4.1764 | -44.2257 | 2025-11-18 04:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5336057f-1b1d-3f4a-90e3-8b91739afa94 | -9.3969 | -48.4523 | 2025-11-18 04:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 0cfc4c08-b96e-346f-ad88-7152e0128467 | -9.03416 | -45.20956 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 069d05f7-aff9-3885-9c9d-637de8ae5fbf | -9.8811 | -44.17844 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e23c1ff6-f674-3e59-b5f5-8678a0f7e0d8 | -6.21773 | -46.88131 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 151381f0-0630-3015-9969-51cb21e912d7 | -10.9622 | -48.69664 | 2025-11-18 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d10dfd9-23e6-3e28-b743-2c17bae1a314 | -8.73022 | -48.3187 | 2025-11-18 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cda3638e-34b5-3d26-900a-2761f899a90c | -7.29779 | -39.37664 | 2025-11-18 04:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 905ce42e-e94f-36ac-9d0b-fa7e6147a5e4 | -5.74869 | -49.25775 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 009d7f13-e2be-3507-8ce8-cf4a022487dc | -3.84609 | -51.05468 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07a1cea-9bf5-33b3-9a7f-88bf7a246df9 | -8.58208 | -48.64539 | 2025-11-18 04:21:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e252cdbf-8b7d-34de-b5e9-aa6ea405c7b3 | -4.98045 | -41.85336 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 0f7461e9-b177-38d1-8152-2651af91b843 | -7.97101 | -38.27802 | 2025-11-18 04:21:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8289ee1-518d-375b-b702-8217bba3e376 | -9.82852 | -46.93301 | 2025-11-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa5b77af-e0ab-3fc6-82b2-7bcb47bc8248 | -10.73572 | -48.65958 | 2025-11-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d5e3b8-b8a5-3a92-ad09-20d3f5b08537 | -4.77175 | -44.92491 | 2025-11-18 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ec8b2a-0ae4-3255-adaf-8cc35c1b218c | -11.01514 | -41.91217 | 2025-11-18 04:21:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49a7828e-9e37-34a4-a725-12daf1c240b8 | -6.05341 | -39.43799 | 2025-11-18 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d01f7a6e-0144-3e29-9a47-cb63b5e2d002 | -4.52637 | -46.41897 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0bb556e-a718-3e64-89c7-59b057173ebe | -3.33162 | -50.27972 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88ae2b5a-d28a-31a1-8bb4-e6e4b5e1f15f | -5.25376 | -50.67984 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db73cc6e-4b46-3165-8f94-408f561db037 | -4.35212 | -44.34841 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70b2bcf9-dbbf-34a0-9611-43c354864d30 | -10.85114 | -44.07624 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41f79a5-6527-300f-b39a-98c83a272926 | -7.43614 | -45.20248 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86a27cc2-c725-31ad-a2b2-cd354b64cc6b | -6.93382 | -45.34674 | 2025-11-18 04:21:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a51aea1f-413c-3891-acc2-90f5c3fc408b | -9.8772 | -44.18151 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 89a6c395-d2d6-3f66-bfdb-c4e6dcdbd23a | -7.51703 | -43.06024 | 2025-11-18 04:21:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52fbdbb5-5954-3aa5-b28f-357567b29e81 | -4.13826 | -46.76405 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61000789-c888-3878-b93b-a917948e254c | -6.70673 | -40.79322 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d4ba25f0-2250-3db1-bdce-255f0bdf5470 | -7.85351 | -42.22716 | 2025-11-18 04:21:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3472f090-2fe7-308f-8d9b-799dc9eab6d9 | -9.15057 | -40.5313 | 2025-11-18 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4d08a776-38f5-3401-a8d4-a8ffe530a4d7 | -4.70465 | -46.31107 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f359067-2761-3dfc-8573-895c7cd7441b | -5.38472 | -50.48538 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
