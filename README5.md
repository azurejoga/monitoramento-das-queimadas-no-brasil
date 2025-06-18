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
| f45f33fa-5c8a-3f7d-8184-6c816bebb7a0 | -11.1249 | -53.936199 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 015a68fc-7a18-3235-af4c-c169300048ee | -10.2945 | -60.530499 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70f81ceb-8cc5-3e37-bde5-6bc7eda71349 | -12.5265 | -57.216301 | 2025-06-18 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66dc7f5f-3175-3201-a9c7-3c7531306e81 | -11.6394 | -54.137001 | 2025-06-18 01:08:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2ddadcd-925c-353d-bdae-53d6fab5db8d | -12.511 | -58.348499 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1beddfd-f0ea-31df-b877-efab48a039b3 | -10.6234 | -54.920101 | 2025-06-18 01:08:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d37e935-8b6c-3a42-9409-4b1af4233e14 | -10.2863 | -60.5397 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff74d57-f648-3cdb-9ac7-ee3ec26f5a49 | -20.9863 | -47.380299 | 2025-06-18 01:08:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 336116a3-958f-3c52-b8db-7b143e4291fe | -10.9168 | -56.828499 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87e5a13a-8227-38d1-8f19-42e61971c601 | -8.7165 | -49.0247 | 2025-06-18 01:08:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbb796e-45be-3f26-a633-89f856dc494f | -9.4925 | -56.0924 | 2025-06-18 01:08:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f21435f1-c140-334b-91f5-e5d5d4552fcf | -14.8445 | -59.822601 | 2025-06-18 01:08:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 527b7f6f-72e5-394a-9732-f894a1602127 | -9.4623 | -57.842602 | 2025-06-18 01:08:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8d581c-3544-35b4-9388-c2c741c87159 | -12.5245 | -57.207699 | 2025-06-18 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7513d226-6551-39b9-a9c9-fee233710130 | -12.5309 | -57.765202 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd6a2da3-9246-3ba7-880f-6fa3a733bdef | -16.315201 | -58.241501 | 2025-06-18 01:08:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 129b00f0-f386-31d3-8777-3e90bd19db8f | -13.5885 | -59.227901 | 2025-06-18 01:08:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28b16771-07b9-3941-95b7-4da9880b21c5 | -14.0308 | -55.120098 | 2025-06-18 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 856a691f-aef0-3674-88e7-7f7403597016 | -11.9598 | -58.734001 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2149bc6a-0201-3627-9d34-e1779204382c | -16.3169 | -58.248798 | 2025-06-18 01:08:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd4f0f73-cffa-3258-9532-5dd132c80151 | -12.5833 | -56.974602 | 2025-06-18 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6dcca76b-bad5-39c6-b075-8b2b123cd9c2 | -11.958 | -58.726501 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6381ef64-b402-3780-9320-45f469324602 | -11.1444 | -53.931301 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1cb6048-1486-3f1e-b403-19ed53558a25 | -10.2847 | -60.5327 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72aa7d28-a903-3d56-b708-3c93a38e25a8 | -12.6495 | -54.1273 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0b6f94f-2542-3440-ac1c-b3fd018ebd47 | -14.0686 | -53.3909 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eccf2e5b-7e02-3806-8450-39369278e725 | -14.4249 | -48.882702 | 2025-06-18 01:08:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab98368-d83a-33d1-bfdf-21f2c81c5dc7 | -11.119 | -53.9446 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 7b95efb3-a3f8-3936-a1af-722bf97af8ec | -11.1568 | -53.9411 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 178ed8e0-fbf5-3247-989c-b12643ba8715 | -14.4467 | -48.9063 | 2025-06-18 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9c78ddd7-a70f-3e47-b17e-c18de1b36237 | -11.952 | -58.7376 | 2025-06-18 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 9365f494-e67f-3a57-b39a-080d6ad29383 | -14.4273 | -48.9093 | 2025-06-18 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 70c937bc-c9c5-38ab-ad6c-e10c22d722d2 | -11.1571 | -53.9206 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 68cc1597-3acd-380e-ae5f-453ca8c9e470 | -11.1382 | -53.9223 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 10d58091-5a37-3b89-956b-191a4d919e32 | -8.7314 | -49.0367 | 2025-06-18 01:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 59bbeec1-cdd2-3818-a742-2d0305e3e4d0 | -11.1193 | -53.9241 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 398bac67-053a-3cd8-99f7-946c279f654a | -20.9845 | -47.3955 | 2025-06-18 01:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 41.2 |
| b8f3afd6-f7ac-358e-bcea-bd507bcd1e53 | -8.7317 | -49.0151 | 2025-06-18 01:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 20adb9ca-bc68-3c5d-827a-6f27d8c18a5d | -11.1379 | -53.9429 | 2025-06-18 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 416.8 |
| 4e3901ee-7c0c-369c-bfe5-1f18a21d8f88 | -9.4994 | -56.0788 | 2025-06-18 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f8375d8f-7405-37af-ae22-cc350bc5926a | -9.4807 | -56.0801 | 2025-06-18 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| a03f1451-d36e-351c-af0d-2f7f8b6c7e07 | -5.9028 | -43.4418 | 2025-06-18 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2a8f76ed-85f8-362c-ad43-bd57899c78d8 | -8.7317 | -49.0151 | 2025-06-18 01:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 5d2c87ef-2c15-311c-b05b-424576956164 | -11.119 | -53.9446 | 2025-06-18 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| acc2e41e-1481-30c1-bd4d-8f7afa232ca1 | -9.4807 | -56.0801 | 2025-06-18 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ac6af414-fbc8-32cc-a09c-3e518226ad84 | -11.1193 | -53.9241 | 2025-06-18 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fbfe7d3c-7b62-38c4-a02c-14fc462ad1d7 | -11.1382 | -53.9223 | 2025-06-18 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 278.1 |
| 67caec82-ea90-3ec4-be75-f01cd821fa25 | -9.4994 | -56.0788 | 2025-06-18 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 9cb48fe3-02ac-3ef8-b06d-4b093001a6ce | -11.1379 | -53.9429 | 2025-06-18 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 471.7 |
| a21b0c64-6200-33e3-bedf-e3b47469c66d | -8.7314 | -49.0367 | 2025-06-18 01:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 17a540ad-3eed-3fa7-98e7-47d97898f95b | -11.1568 | -53.9411 | 2025-06-18 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5436011c-7d8c-3214-9edd-05adbabef4b8 | -14.4467 | -48.9063 | 2025-06-18 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b9f170d0-da71-3702-9539-b7be95f19057 | -21.0051 | -47.3904 | 2025-06-18 01:20:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f97cd085-76b4-3304-9c7e-7826a733f033 | -8.7129 | -49.0168 | 2025-06-18 01:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 31856b65-4163-378a-bb9e-6cdaa4a559ba | -11.1377 | -53.9634 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dc53051c-e815-34df-8075-2731d97fdd4d | -14.4467 | -48.9063 | 2025-06-18 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1161dda5-356c-3e7b-baef-34b3eaa35241 | -11.1382 | -53.9223 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 248.9 |
| cb1355a8-23ee-32c6-b4b5-24dd74fcb2b5 | -11.1568 | -53.9411 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 913fffdb-ac8b-32f0-bea1-a3355df7759b | -11.1379 | -53.9429 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 407.9 |
| 76c08c5c-b1a7-324a-b81a-2f9664fe4206 | -21.0051 | -47.3904 | 2025-06-18 01:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 6791a290-eedf-3322-95b1-fdc6ad4d10cb | -11.119 | -53.9446 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 90e31fb4-d854-3b65-9cc3-6c474ecbc6b9 | -8.7317 | -49.0151 | 2025-06-18 01:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ea8697f2-4671-359e-bd31-e816d05d896e | -11.1193 | -53.9241 | 2025-06-18 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4d420b78-7be4-3465-a556-42fc62cf298b | -10.6501 | -49.3617 | 2025-06-18 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bbda7664-fca8-30ce-82d5-86dfb5d290fa | -11.1193 | -53.9241 | 2025-06-18 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 1bd0cc08-9313-399f-af00-7cfd8cfa4ea3 | -11.1382 | -53.9223 | 2025-06-18 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 4ee011e5-0103-33ae-9258-600c68ec1f9d | -11.1379 | -53.9429 | 2025-06-18 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 387.8 |
| 76d1aae1-0443-3bff-b5e1-b3fcded8927a | -11.119 | -53.9446 | 2025-06-18 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0ee2fa62-1498-3e41-8fbe-6cd4dc35afce | -8.7129 | -49.0168 | 2025-06-18 01:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8b60c0ed-7c68-3ff0-a2c6-79ef9f6436cd | -11.1568 | -53.9411 | 2025-06-18 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3c6984aa-7d6a-34bb-8bf7-0807af304363 | -14.4273 | -48.9093 | 2025-06-18 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| db451744-765b-3949-bf4b-c0ca7b108622 | -11.1193 | -53.9241 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4e83221e-0d7f-31f8-935c-4cce3b0463f0 | -11.1568 | -53.9411 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| b9febb27-3606-3f68-9d0a-86cd1494fd7f | -10.6501 | -49.3617 | 2025-06-18 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 0c070457-2767-3d7a-b60e-26fe5530fc5c | -11.1379 | -53.9429 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 309.5 |
| ac47a2f4-6d8b-39a7-8044-eaaf90b331b7 | -11.1382 | -53.9223 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 219.5 |
| 7f73dfc6-2091-389d-b2ca-2252bb335f55 | -11.119 | -53.9446 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a588f7c3-6d47-3957-bd4d-f57a4deb26b5 | -11.1571 | -53.9206 | 2025-06-18 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a86b8352-75bf-3c63-968c-570112182423 | -14.4273 | -48.9093 | 2025-06-18 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3182448c-93f9-3d24-878d-f63f4b5bb0d5 | -8.7129 | -49.0168 | 2025-06-18 01:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8d7f183d-bd8d-31bd-9114-e01768cc1a2b | -11.119 | -53.9446 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6a48632f-6032-3365-b2ae-13120bda059f | -11.1382 | -53.9223 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.7 |
| 04481e45-7d49-3a79-93d5-d8b8101395b7 | -11.1193 | -53.9241 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 00d1aa50-cad7-3e42-924d-a662572f0615 | -11.1379 | -53.9429 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 311.9 |
| 2abd5f65-eb3a-31b1-be5e-9ef469e12fff | -11.1568 | -53.9411 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4e43a228-5a2c-3448-b95b-82ceae6409d8 | -10.6501 | -49.3617 | 2025-06-18 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 297c83fd-69f7-3a98-aad6-692620879bd3 | -11.1571 | -53.9206 | 2025-06-18 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f76a56b5-7b77-3ada-9fa8-edbc8d4804e4 | -10.2811 | -60.537899 | 2025-06-18 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18d2df9b-596d-39da-a140-3da8f0020c3d | -10.928 | -56.837002 | 2025-06-18 02:00:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f49c097e-a211-3a4c-866a-b0c508ba29f0 | -10.2848 | -60.552399 | 2025-06-18 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fecd692-742d-34ee-9b62-5e82a28833ac | -10.2908 | -60.5354 | 2025-06-18 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 492b51c1-5d1b-3213-abdc-1c9c46c7d60c | -10.9347 | -56.862099 | 2025-06-18 02:00:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb10422f-147e-330b-88c3-c8ad48841ef2 | -11.9621 | -58.7173 | 2025-06-18 02:00:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eaf4551f-5b7a-354b-9a18-27087f743f97 | -9.9703 | -64.974403 | 2025-06-18 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9311a23a-0159-3609-8308-20afae677e4a | -11.9669 | -58.735401 | 2025-06-18 02:00:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95e685f4-2772-39db-83b2-e7cf87e85ff2 | -10.9184 | -56.8396 | 2025-06-18 02:00:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67bfa5de-6bdc-3293-836e-c6932807d5c0 | -11.1377 | -53.9634 | 2025-06-18 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 5c25eafd-e67a-387a-91ab-abb93c7dd35e | -11.1379 | -53.9429 | 2025-06-18 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 346.0 |
| ccf4c014-52e8-352c-9606-1c380be52a8f | -14.4467 | -48.9063 | 2025-06-18 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c56bfc4f-d68b-31e0-9b50-3cb80afba5f8 | -11.119 | -53.9446 | 2025-06-18 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |


[Clique aqui para ver as próximas entradas](README6.md)
