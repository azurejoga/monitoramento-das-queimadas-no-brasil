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
| 5e5c8cda-7c0e-3e6e-8d77-993b97ad3cbf | -11.1382 | -53.9223 | 2025-06-18 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 08b53557-5878-3e3a-8880-ca546fe16f12 | -11.1379 | -53.9429 | 2025-06-18 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 395.0 |
| 7d00873e-2f71-3725-8979-1ff1094a46ec | -11.1382 | -53.9223 | 2025-06-18 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |
| d4de79a1-9037-3dec-a191-6a0713a10072 | -11.119 | -53.9446 | 2025-06-18 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c06c432b-01a0-3fa6-840d-7d3825d600b1 | -11.1193 | -53.9241 | 2025-06-18 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| abadd215-5ccf-36b3-ab18-05255c5c8540 | -11.119 | -53.9446 | 2025-06-18 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 64cdd75c-e531-3eb6-8aa5-20f3dc77fa54 | -11.1382 | -53.9223 | 2025-06-18 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 07904f98-4e5f-38da-aac1-11e58049e986 | -11.1379 | -53.9429 | 2025-06-18 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 286.4 |
| b51b1849-12b6-381f-8d31-d99c3d08af5d | -11.1568 | -53.9411 | 2025-06-18 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2aabc552-f79a-386d-aa07-e8bfe3e01d45 | -11.1193 | -53.9241 | 2025-06-18 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ed9cc073-ddcd-30bd-97fb-f9214ce4cc1d | -11.1379 | -53.9429 | 2025-06-18 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 332.8 |
| 9808fb0d-a687-33f1-9545-a957c6570cc3 | -11.1382 | -53.9223 | 2025-06-18 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 94dc47d5-2fe6-3d02-b5c0-1d7d34111211 | -11.119 | -53.9446 | 2025-06-18 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8e6863b6-7193-32fe-9ecb-249e8d90639e | -11.1379 | -53.9429 | 2025-06-18 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 304.7 |
| 6c7e8b1e-08ee-3c73-aef6-0e4142ff1cad | -11.119 | -53.9446 | 2025-06-18 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| caff7103-9730-3930-98cc-f98f756a1e45 | -11.1568 | -53.9411 | 2025-06-18 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bdc0b5cd-ca83-3dc0-9027-b11fc441679b | -11.1382 | -53.9223 | 2025-06-18 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 3893a4f5-074b-301b-812c-e8ab81a65884 | -11.1379 | -53.9429 | 2025-06-18 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 286.6 |
| 7d8df326-de6c-3b26-898d-de853a12dce3 | -11.1568 | -53.9411 | 2025-06-18 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2c58b1b3-906b-392e-bf8c-db01c34950b1 | -11.1193 | -53.9241 | 2025-06-18 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 88eb71d8-d8e6-380e-81ee-10ea76f10426 | -11.119 | -53.9446 | 2025-06-18 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6c6bffb9-db85-384f-8fe8-4cafd199f9ee | -11.1382 | -53.9223 | 2025-06-18 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.0 |
| ba6613ea-5c52-3c9f-aae6-0e981f3ccc76 | -22.67785 | -42.85645 | 2025-06-18 03:02:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f5a6951f-4ffe-3ef5-89c3-d39dd340299b | -22.67522 | -42.85729 | 2025-06-18 03:02:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b0f5c7f1-d6e2-3f7d-93cb-c6371dc9d7a1 | -22.67599 | -42.86369 | 2025-06-18 03:02:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3b7a1dd3-9ca9-343d-b611-aeb4d7b45409 | -11.1568 | -53.9411 | 2025-06-18 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8b039218-acc5-39b4-b198-cdaa472a82ae | -11.1379 | -53.9429 | 2025-06-18 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 269.5 |
| 243c5ece-e7cc-36e1-8616-2671aae6a5fe | -11.119 | -53.9446 | 2025-06-18 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7d025f79-9680-316c-bd1c-41a434bd55e8 | -11.1382 | -53.9223 | 2025-06-18 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 84da3156-5a03-3a71-92c7-fa522fa992e0 | -11.1382 | -53.9223 | 2025-06-18 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 61de2992-93c1-3c0e-93bf-ad30d5bed98d | -11.119 | -53.9446 | 2025-06-18 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 73c9bf38-30c6-3e75-ae7c-79415a51ff4a | -11.1379 | -53.9429 | 2025-06-18 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 276.1 |
| 36bfd978-e544-3b2a-a955-f2d23e428e5b | -11.1379 | -53.9429 | 2025-06-18 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 4965be0f-8ef6-3c74-bd1d-5da8e4be9195 | -11.1382 | -53.9223 | 2025-06-18 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| dd57e51f-1211-3029-a137-10d92ea3a6aa | -11.119 | -53.9446 | 2025-06-18 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| dd47771f-b088-383a-930e-d00a653181f5 | -11.1193 | -53.9241 | 2025-06-18 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8eb5c25d-98cc-3013-bce5-63e0d8cbc27e | -11.1568 | -53.9411 | 2025-06-18 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ec2f7b0c-64ad-3f5a-97d3-b82fd8301efd | -11.119 | -53.9446 | 2025-06-18 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 4ac5d457-1487-368e-b2b4-e9e93e666ad8 | -11.1382 | -53.9223 | 2025-06-18 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 82f33904-4334-3f11-85a0-1a16c8df9da0 | -11.1193 | -53.9241 | 2025-06-18 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 45677258-ad6b-33bf-839d-7d33194d2ea8 | -11.1568 | -53.9411 | 2025-06-18 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6ae50a7e-7c2b-3dd3-ba35-60ae48207c68 | -11.1379 | -53.9429 | 2025-06-18 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 20ab26c2-5681-3003-87c7-441c5dd485a9 | -6.67567 | -43.22088 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41a30aca-22e3-3900-91cf-fc4e63fe825c | -5.05849 | -43.24474 | 2025-06-18 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0daf01b-3758-3728-99d5-80f0492e0924 | -6.11521 | -45.941 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94826e84-1686-35d7-bb5b-ccca0fc41dbf | -4.55733 | -48.01094 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1d08f74-7336-305d-b013-0aae38187935 | -5.91242 | -43.45074 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3a56f27c-6092-3cfc-b3f2-c73a7ea50ea7 | -5.90794 | -43.44997 | 2025-06-18 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bfcf882d-251e-3f84-82e8-c6d60a3afef2 | -5.85081 | -43.64081 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 982d6ff5-b921-3fda-8b0a-0642b76a17c2 | -6.12671 | -42.52719 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fbbef8c7-0a00-376d-8cdd-0b297e0b188d | -6.12541 | -42.53496 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cec0f7a3-c66b-32c6-84f9-2523bc0d132e | -5.90993 | -43.45203 | 2025-06-18 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3383eeeb-1580-3c96-901a-f44ecd5d224b | -5.61218 | -45.97802 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6ba456d-b8db-3090-a6a7-6ed8a8e82799 | -6.1146 | -45.94439 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd48f233-43bf-345f-961c-b8ac1c6c2547 | -6.67199 | -43.18937 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a9eb2622-1756-3b7f-aa22-2c644edbda97 | -5.06021 | -43.24809 | 2025-06-18 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8859ecf-155b-33c8-ac24-50684a3c3226 | -5.07339 | -43.72599 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cd0128c5-d0d2-36ae-a35e-f91f6f7bb657 | -6.87065 | -44.83744 | 2025-06-18 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d01a9a69-99bc-3ca5-97e8-2cec2cf8491c | -6.11608 | -42.51327 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fcf2f901-4317-356d-86ac-6d2c5cbf50f3 | -6.14399 | -42.96833 | 2025-06-18 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 29fb42fa-6d6c-3203-8291-70434967a58f | -7.23433 | -43.10069 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e43347c3-b368-3ff9-bd43-524041cfa526 | -4.81468 | -47.3256 | 2025-06-18 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5611d9d2-8c25-3d54-90c4-7d0011b4b50d | -4.38294 | -48.07345 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30106507-8393-36e0-8a47-cee5befe14c6 | -6.41737 | -44.79692 | 2025-06-18 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10ad8f7e-9f02-3b08-af91-9ecd0587f865 | -6.12834 | -42.54337 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 312fee95-14fe-3ad5-a2e9-c12dde4b2d90 | -6.41975 | -44.79562 | 2025-06-18 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbb3061-ba4e-35dc-a010-2ecf1ea25a6b | -7.23073 | -43.09589 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20b374a6-ce1d-3553-a7e4-8f0df0805fa1 | -7.16743 | -43.47045 | 2025-06-18 03:47:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0146df5-c90b-31d9-82b9-2b35e835f7a2 | -6.12185 | -42.53041 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 28f3ecd3-ca84-3093-8724-f4146830e48d | -6.13896 | -42.97177 | 2025-06-18 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c05a643-c516-37c5-abfb-b61d046e63a7 | -6.12121 | -42.53427 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8b9a7b6a-0a88-3557-b707-c0117b5d695d | -6.68002 | -43.2217 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8e842755-0b7c-31f7-9f96-4d4ade195b41 | -2.91554 | -48.23315 | 2025-06-18 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46eb5f1f-d14a-374a-b1dc-25e178fc9ba3 | -4.82688 | -37.91364 | 2025-06-18 03:47:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e1624b2-9705-3e5e-ab60-229cb93be311 | -6.13825 | -42.97597 | 2025-06-18 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 679de5bf-37f5-3f83-87e7-c6b03f6bfbab | -4.82065 | -47.3264 | 2025-06-18 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a5ceea8-f15e-3d7d-8040-776bf714b213 | -5.61278 | -45.97459 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f193d2a7-4560-3f5e-a466-60036c8358e1 | -7.23501 | -43.09664 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ebd0d7a-415b-3831-8262-48f55cbbf4a5 | -6.24023 | -43.36533 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 839c2d8b-b3e9-35c6-b4d3-f711d9fea457 | -7.21349 | -43.22443 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 55200700-3d67-3036-b558-e31063a33794 | -6.41395 | -44.80017 | 2025-06-18 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcf858f5-acb7-3737-aa22-b17915d08d13 | -6.12898 | -42.53952 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4c3b01f2-c650-38a4-ab52-45f7c67d4305 | -6.24334 | -43.36859 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73dd4111-907b-379d-8d84-a7519b1e970c | -4.55288 | -48.00747 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1efdaf0c-f357-31e5-91ce-d1b99f78de7a | -5.91322 | -43.44611 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 676004fd-470c-3e2f-a16f-57ccc9a9fcc2 | -6.66397 | -43.1838 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65b71afe-fc74-30c6-8d9c-b0e8d320759e | -6.66256 | -43.19213 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f3f4ef46-f01d-3563-9920-64653bccbb70 | -6.66326 | -43.18797 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cd2f1f98-ab86-3b75-a05a-d4d2a4dd1f46 | -5.61337 | -45.9712 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da8a1274-b239-365c-b96e-b0b5ee7ab56b | -6.12477 | -42.53883 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7ba085db-262f-325b-8da6-8767cb348c89 | -6.6363 | -41.71458 | 2025-06-18 03:47:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbf91f05-d9d1-3375-a3a8-ba65330d0a3e | -6.67705 | -43.18589 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5da35d7b-265a-3b26-8ff6-c63672969df0 | -6.12056 | -42.53814 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| fa8cebec-a234-3877-9b49-87cbda59fb5f | -6.68073 | -43.21746 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 554f5154-4432-3be7-90b3-91c25089144b | -6.12251 | -42.52647 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5e031def-c100-3520-8956-96e34eb478e4 | -4.55116 | -48.01737 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 754e53b0-23e5-3d78-871c-59a68d614bbb | -6.37455 | -43.75 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 04ae6152-55df-3dea-8228-2472dbc51402 | -6.11598 | -45.94387 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5166092-a011-3381-91a3-8e02d71907a4 | -6.6582 | -43.19141 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 294a1d89-c2f8-3658-9831-1aae813f774d | -2.91578 | -48.23519 | 2025-06-18 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README7.md)
