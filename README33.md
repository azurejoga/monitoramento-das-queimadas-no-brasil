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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d01d4d38-882c-32c8-9a86-3c38e9823f9f | -11.658 | -44.644 | 2025-06-20 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5e337a4a-7c10-3d4c-873e-72db11eb8759 | -14.2247 | -45.5036 | 2025-06-20 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 96ce91a6-c79b-3297-b29d-ed64604e60a4 | -10.5241 | -47.5822 | 2025-06-20 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8c981b42-bf4d-3a40-a672-ab7e115a7dd6 | -11.7756 | -54.3551 | 2025-06-20 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1966b869-b727-3430-b8d6-c514f285afae | -11.5842 | -47.8723 | 2025-06-20 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 7fb3f539-d5f2-3078-8d02-25cd56cd8874 | -11.7754 | -54.3756 | 2025-06-20 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0863e542-1885-388c-8f13-170cafbd6958 | -14.0404 | -53.3669 | 2025-06-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dd554963-3d2f-3fbe-a158-20e7df1c29a5 | -10.876 | -53.7614 | 2025-06-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 01ae1a11-c6d5-34e3-819b-b2765daff67c | -10.5241 | -47.5822 | 2025-06-20 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 03794c74-5e7d-370c-9df9-e80265e5d7a1 | -9.465 | -57.8252 | 2025-06-20 14:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 30971bcb-8173-3604-8e5e-ab34727ffd19 | -8.5911 | -51.5537 | 2025-06-20 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a80babcd-4f14-31ce-87fb-b9a09263b73a | -11.7754 | -54.3756 | 2025-06-20 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5c49467f-e46e-36bb-b191-d91eaab6a044 | -11.658 | -44.644 | 2025-06-20 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8319bb36-330d-317a-8032-3a75d51d1b87 | -11.3232 | -45.2009 | 2025-06-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 12406287-824c-3e33-8faa-2f018506187b | -11.9246 | -51.7621 | 2025-06-20 14:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| ba11b970-c210-39e6-a87c-a00434ba2b91 | -11.5366 | -56.9847 | 2025-06-20 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| f7a89272-013e-318f-bc7b-07c719a772c3 | -11.6584 | -44.6207 | 2025-06-20 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| c5e32f40-2f0c-3f3d-a56e-453813948567 | -10.8571 | -53.7631 | 2025-06-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4794082b-3e45-30c4-b303-e6379b8bde18 | -14.2247 | -45.5036 | 2025-06-20 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 1dcac47b-f1f0-3674-a347-cd256b2f2ec3 | -11.7756 | -54.3551 | 2025-06-20 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f8826a3d-5f55-39ce-9dbc-3e9de8e2d9bf | -11.5842 | -47.8723 | 2025-06-20 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 2d1fcc52-736c-3e68-b4a7-40aa0fd30691 | -11.5177 | -56.9862 | 2025-06-20 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 66a39c14-5dac-333a-acdd-a0cacbe23036 | -14.2242 | -45.5269 | 2025-06-20 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9b4d22e3-9c7d-396c-aead-5f1d0fde76f4 | -10.5521 | -46.9785 | 2025-06-20 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7c74522c-3544-36a2-9f12-530ef103be2a | -11.658 | -44.644 | 2025-06-20 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 354725f8-94fd-3f0d-92e1-e99baba92ac3 | -11.1382 | -53.9223 | 2025-06-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9bb7cffd-5024-3a9c-a0f6-1f8a286cdeaf | -10.876 | -53.7614 | 2025-06-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 59ccd9bc-31e5-3361-9ffe-2d394a3698a7 | -11.5842 | -47.8723 | 2025-06-20 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 04a74ee6-8093-39ff-9a6e-0dbae6939bf9 | -9.465 | -57.8252 | 2025-06-20 14:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8d31b953-f222-36cf-9658-109410932715 | -11.5177 | -56.9862 | 2025-06-20 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 56c7cb61-5dbd-3360-aa16-c9a856f7a4b4 | -12.9682 | -54.6883 | 2025-06-20 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ca2cd275-092e-3f85-b974-0d6ade375e51 | -14.0404 | -53.3669 | 2025-06-20 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8b9f251b-7bee-3195-b12c-ab931ace4c39 | -10.5521 | -46.9785 | 2025-06-20 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 75db5ed3-deb8-3362-a13e-429e79e89211 | -11.7756 | -54.3551 | 2025-06-20 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 18cd8ac7-1906-3ca6-b0d1-eabdce2a1afe | -11.5366 | -56.9847 | 2025-06-20 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| e1045844-e76c-3f37-ba81-896a63472da7 | -10.5241 | -47.5822 | 2025-06-20 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 58af5812-f494-38f4-a925-870e25a041be | -11.7754 | -54.3756 | 2025-06-20 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 3bfb3d8a-a6d6-3b5c-b173-db134db84e94 | -8.5724 | -51.5552 | 2025-06-20 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 75e93f57-e0ef-39a4-a5c5-ca36bc6e02ae | -11.6584 | -44.6207 | 2025-06-20 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 349b7df5-95d9-3549-a06e-522919a470f3 | -11.9249 | -51.741 | 2025-06-20 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| e702f6ba-a835-34e0-8336-4a753e6f5911 | -14.2247 | -45.5036 | 2025-06-20 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 0eb50751-82de-3bde-97fb-e55c4c9a116f | -10.8571 | -53.7631 | 2025-06-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 27a8cbde-dfc4-34b2-bd5d-b8600861f301 | -9.4648 | -57.8449 | 2025-06-20 14:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 623f4fe9-277a-3fa8-9626-2099b6f632c3 | -7.2713 | -45.37 | 2025-06-20 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e3ba6d65-8b8c-34c1-b248-460fef3fba47 | -4.8519 | -43.7486 | 2025-06-20 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 14bdd0e8-8fc8-3097-b05c-9b1de12e15d6 | -14.2242 | -45.5269 | 2025-06-20 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5337a0e3-7765-389a-b77d-c081c8f11578 | -11.9246 | -51.7621 | 2025-06-20 14:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 169.5 |
| ebe46b60-2204-3f33-b8ab-30c1532d1698 | -11.1382 | -53.9223 | 2025-06-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| de3da752-ae59-30c4-b3cf-6166e73ebf29 | -10.5241 | -47.5822 | 2025-06-20 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bf4ebcff-3c83-3c99-b7ea-c6fbc5ca2794 | -8.5724 | -51.5552 | 2025-06-20 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 76a6c279-ba46-33b3-8c9d-a04583585758 | -9.465 | -57.8252 | 2025-06-20 14:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3714ffae-3138-3bbd-b67f-77a53797d691 | -11.658 | -44.644 | 2025-06-20 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 799b19b4-1c90-35a3-a703-aa0c4ab20612 | -12.9682 | -54.6883 | 2025-06-20 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9242a720-8159-3812-b769-1c717f2d1bb4 | -14.2242 | -45.5269 | 2025-06-20 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b086fb42-c9ef-394c-94a8-9a3c61db84e7 | -7.2713 | -45.37 | 2025-06-20 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3e1c08f8-6f54-3fa3-9e90-3f215dad5cea | -11.7754 | -54.3756 | 2025-06-20 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| d3a382af-77e5-3b59-b0bc-af5e4eefd607 | -11.5177 | -56.9862 | 2025-06-20 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b78a0f86-a0fc-32e2-9e5f-99460881be8e | -9.4648 | -57.8449 | 2025-06-20 14:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0e3bc28c-5eea-35a0-9bb7-8afffa906eac | -14.0404 | -53.3669 | 2025-06-20 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| de11d191-98b5-3222-8513-2672e36f07cc | -11.5842 | -47.8723 | 2025-06-20 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4971cea5-e6b2-3ea4-af96-e23ce9485730 | -11.7756 | -54.3551 | 2025-06-20 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 23f8eeff-84f0-34b7-a3d3-af2b8016d9cb | -14.0212 | -53.3692 | 2025-06-20 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c8577df9-030d-3aec-b1c1-70a223423e70 | -10.8571 | -53.7631 | 2025-06-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 5864c392-d9bc-3ee1-934a-02bbeed49be2 | -11.5366 | -56.9847 | 2025-06-20 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 6fe2bed8-96da-38ab-938a-f2fed93c9060 | -11.6584 | -44.6207 | 2025-06-20 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 260.1 |
| d92d9423-c2b2-3268-ba99-ade736934427 | -10.876 | -53.7614 | 2025-06-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 46677f4e-fd45-3ff0-a57c-628025614f00 | -14.2247 | -45.5036 | 2025-06-20 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| a41a6da8-b7b3-3247-b12f-1991b17a2a09 | -7.0675 | -43.4111 | 2025-06-20 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| e5368e0d-ee5c-3dec-acde-47591ecad9c8 | -9.4648 | -57.8449 | 2025-06-20 14:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| be225232-08a2-3de9-bf83-ccd5bdca37fe | -12.9682 | -54.6883 | 2025-06-20 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 661e4816-f496-3b44-b2c4-e7b76dc7e6ac | -11.7754 | -54.3756 | 2025-06-20 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1f1e853c-c331-3640-bd75-f8d2dc2caad9 | -11.5366 | -56.9847 | 2025-06-20 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 7a51a72e-3b66-3748-ba67-8a532989c7ba | -11.5177 | -56.9862 | 2025-06-20 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 68c6b2a5-c3a9-3d0f-b12e-67b5f9e22893 | -11.6584 | -44.6207 | 2025-06-20 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 485.7 |
| da3b28d1-71ba-3b73-91a6-3bc7ea94b05c | -14.0404 | -53.3669 | 2025-06-20 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 74431497-fb46-3282-b2ba-c944e16222b7 | -6.1487 | -47.2651 | 2025-06-20 14:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 565ff361-2248-373d-9545-827b534d429c | -11.658 | -44.644 | 2025-06-20 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| d8e01776-af36-3ee6-b700-b9e1db27b2c8 | -10.876 | -53.7614 | 2025-06-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 90d81e06-27da-31ad-99fe-c023d6060c17 | -11.7756 | -54.3551 | 2025-06-20 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 77fe5343-46b3-3d79-bec5-4a7d00484867 | -11.5842 | -47.8723 | 2025-06-20 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| dd76d1c1-abda-3e8c-8511-99c218ff0478 | -9.465 | -57.8252 | 2025-06-20 14:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 5c92edea-6ac4-3354-883e-925bdc0b8450 | -10.5241 | -47.5822 | 2025-06-20 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 544423e9-b994-3008-9695-6117905962ff | -10.8571 | -53.7631 | 2025-06-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |


