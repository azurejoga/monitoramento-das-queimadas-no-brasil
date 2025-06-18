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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5df70c8f-2a57-3b9b-bc65-4961c218d59b | -12.50362 | -58.35892 | 2025-06-18 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8b4df2c9-84e9-3a63-81d1-408c00740516 | -9.81518 | -48.11591 | 2025-06-18 01:00:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 30d1342d-94ae-3179-862e-21628eaf7454 | -7.54078 | -45.6605 | 2025-06-18 01:00:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c2bf5576-6ae5-3e6c-ab9b-c9443aa11441 | -8.72395 | -49.02578 | 2025-06-18 01:00:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 8006d92f-ff86-3904-877f-2aab92e0a56b | -9.26966 | -50.04494 | 2025-06-18 01:00:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d4af0e1f-9eb6-3e68-a34b-ef017aa87892 | -11.12506 | -53.93216 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fbb8960c-08b2-3b1b-8ae0-f1908d080721 | -10.91353 | -56.84419 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b60c80aa-88dc-328a-bad1-eb34d1de0b76 | -10.29162 | -57.14265 | 2025-06-18 01:00:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 09ab54e5-1183-3655-8d23-01cf4e55c49f | -9.49045 | -56.09047 | 2025-06-18 01:00:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| ac11c1d7-f965-3b02-8b2e-ff98063026fe | -10.36453 | -57.24668 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b5b4b550-0aed-37d6-a281-806c87056515 | -10.72607 | -49.57284 | 2025-06-18 01:00:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 017bc7b0-4410-3fc7-a456-41d36034e6bf | -10.95493 | -49.2532 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 342b44d8-4110-3b7d-a974-852f3909441d | -8.72611 | -49.03976 | 2025-06-18 01:00:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 82f13e85-12f4-3799-af8f-f5bd0ff1983c | -9.25783 | -50.03473 | 2025-06-18 01:00:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cac44595-c1d6-37ef-af04-fc4829f8a914 | -10.65187 | -49.35801 | 2025-06-18 01:00:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5a903b45-2f0b-3bc5-b103-7121f489fec2 | -11.61721 | -58.29121 | 2025-06-18 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cbff1eef-6587-3a9d-a598-68082bb67427 | -11.14413 | -53.93873 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a3bb5ac3-6df8-3e13-8846-492f353643b1 | -8.7276 | -47.996 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bbdc1bec-5bef-3dfa-b92d-adacd7e92587 | -11.13397 | -53.93085 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 8e9d359c-6c3c-33e9-892c-43779460a678 | -8.72175 | -49.0116 | 2025-06-18 01:00:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 00eafd50-cf75-3feb-bbf3-6e11fb8d4ed6 | -10.92546 | -56.85543 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 0374f699-3095-32d2-aada-e78b6f9fc62e | -10.62236 | -54.91621 | 2025-06-18 01:00:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| fb38db83-e251-38ad-a85c-f5d9f577e908 | -8.59066 | -51.56692 | 2025-06-18 01:00:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 75a7bb28-2b4f-3019-a280-2fab3d6f27d5 | -10.92388 | -56.84277 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 8e1ca0ea-248f-3626-8496-890185f93f01 | -10.35395 | -57.24807 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e03f2964-4292-31e5-a67f-9d70efa0abf2 | -8.72233 | -49.03244 | 2025-06-18 01:00:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f852a5f5-760b-3d86-bca0-0da3c58f34d7 | -10.66409 | -49.36887 | 2025-06-18 01:00:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 57a56007-58f4-32d0-9d06-fb065c8b0835 | -11.13521 | -53.94001 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 609.5 |
| 37d89428-90f2-3595-8c48-f00115dee46c | -11.65105 | -54.14709 | 2025-06-18 01:00:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c337e290-02ab-3f62-ba6d-c710af2f7bdc | -9.2596 | -50.0465 | 2025-06-18 01:00:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 80e4b218-121c-3286-bf8f-456382d18f2a | -11.08157 | -55.05235 | 2025-06-18 01:00:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef0a2622-4f99-3b88-a610-4320c6902fad | -11.14288 | -53.92957 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| f3a89f02-7c43-38bc-bd4b-8d39573b1eab | -11.14164 | -53.92044 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e6ad724-7075-364c-8f8e-e40e0a80a9ea | -10.24386 | -52.23135 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 5b06b214-76d9-3287-9932-1b13a653e6ee | -10.91734 | -56.85011 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6478d91f-f6b1-3ef2-bd18-5293ccf9f94e | -9.48902 | -56.0797 | 2025-06-18 01:00:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 17ff1c97-f01b-362b-b4fa-795cdf856904 | -8.72024 | -49.0183 | 2025-06-18 01:00:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d0cd9a29-4e6e-3588-b194-1f0d7d0d84b8 | -12.51557 | -58.35739 | 2025-06-18 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ae3ad317-6f1a-34e0-9910-72efded4da8f | -10.73444 | -49.55914 | 2025-06-18 01:00:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cad42afc-6aa9-3b14-bc84-16ecb0119418 | -11.1263 | -53.94129 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5e7d3a86-a7db-3d36-aee9-cb3a19d3b539 | -10.73397 | -49.56588 | 2025-06-18 01:00:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 1c1358e0-d509-38da-b608-a8883b95951d | -11.9562 | -58.71781 | 2025-06-18 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 32e64788-fc1e-3a3f-a293-79a83f15672f | -10.27635 | -60.54906 | 2025-06-18 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| d2c28237-2595-3b6f-b6bd-214cb4c9b9bd | -11.13894 | -53.96746 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b0713ed-d1d5-375c-9176-1e1dda5df564 | -7.53594 | -45.63919 | 2025-06-18 01:00:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 658ed20c-faba-314e-a250-49581d06a9f2 | -11.95837 | -58.73559 | 2025-06-18 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 205074c6-771b-31c3-b745-80dc8683d039 | -10.65377 | -49.37049 | 2025-06-18 01:00:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3f46a450-04cf-39ac-8c8f-137969d08ea0 | -11.96219 | -58.72991 | 2025-06-18 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a38aa6f6-b07f-3558-a701-3e750c2aedec | -11.88753 | -54.6748 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 43d9bd3d-aba3-3f10-81e6-8fd9f964504f | -10.58329 | -49.6509 | 2025-06-18 01:00:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 792b0715-0199-3527-b931-a34ea30c8823 | -7.80968 | -46.57269 | 2025-06-18 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2c497f41-734d-38e4-bb11-6fdcf4606f5b | -6.38212 | -43.7737 | 2025-06-18 01:02:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3cc5c7b4-d0fb-3144-9fee-6a0adde00bf6 | -6.04504 | -44.05391 | 2025-06-18 01:02:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4264cb91-844d-38a3-aeac-db1babad944f | -7.27722 | -50.00026 | 2025-06-18 01:02:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 3c29940b-14a5-3fb7-86ce-e110c8897957 | -4.55488 | -48.01102 | 2025-06-18 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b6a50ea8-f357-3c2f-be86-1c3559a5219b | -6.04176 | -44.05894 | 2025-06-18 01:02:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| f7f49a58-8501-381c-b255-154169e511e8 | -14.0618 | -53.363602 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d2e9421-8b2e-3e50-a8dc-7bc3320f36b9 | -10.354 | -57.243301 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 405c3446-9e87-3211-9e32-30b7a7ed21ce | -11.138 | -53.947601 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad453c95-5390-37e2-9ecc-cbce667becb7 | -12.6528 | -54.099098 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7080791a-cab0-318a-a9e4-66e4b12c665e | -10.6204 | -54.907799 | 2025-06-18 01:08:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc7df55-344a-39a4-ad4c-4139769d61af | -9.4643 | -57.851101 | 2025-06-18 01:08:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecf7dc98-d489-39b6-9dc2-576a0a107e80 | -11.9661 | -58.716702 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b68f2452-f3b7-341f-beb5-98d24ba86d1f | -12.519 | -58.338501 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fff3629-d032-3400-b05e-ef9a4c59bb2b | -8.707 | -49.027302 | 2025-06-18 01:08:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fa07475-1dfa-3877-89d2-532ba6f9572b | -11.9696 | -58.731701 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1399de3a-07c8-3ad7-82e0-fc260433c3e5 | -10.919 | -56.837799 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf42c4a-ce7d-32f2-9415-b0ba1cb1a9e4 | -13.5868 | -59.220699 | 2025-06-18 01:08:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ba26d8d-d6ea-39f3-98a1-29192ef75a22 | -10.6566 | -49.3848 | 2025-06-18 01:08:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee40c5d7-2bf9-3761-ba2a-0ab26d19692e | -11.6188 | -58.283798 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff7c26f-32dc-3861-912d-e9ab134e6ab3 | -11.1283 | -53.9501 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0d94a4f-2349-392f-9edf-ed39e1aea2d9 | -11.8836 | -54.667702 | 2025-06-18 01:08:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e245255-0a03-3a3d-a26d-ad1dca9dcb2a | -12.5328 | -57.7733 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74c0415c-03a1-3b7d-95da-3b9bed0aee24 | -10.2765 | -60.541901 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08f19419-5f61-3639-a879-62d4c834bd6a | -9.4874 | -56.070999 | 2025-06-18 01:08:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9601ba7e-b875-3733-bf90-7ed39397725c | -19.179701 | -57.538601 | 2025-06-18 01:08:00 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c7b3380e-ae2e-3ffe-a33b-adc894be4f18 | -10.2832 | -60.525799 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3acf1b6a-d1f6-3d43-8814-adb95a4f294e | -11.1346 | -53.933701 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e396088-0ee1-38d0-99fa-c174e0ed3823 | -10.6626 | -59.2869 | 2025-06-18 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0c0cde4-efba-3109-ae5b-cf6792178f84 | -11.1214 | -53.922199 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 617eaf69-6996-3407-9d25-c84761033a72 | -11.1409 | -53.917301 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c46183af-8204-3bad-b6bb-add44993cef7 | -11.6206 | -58.291599 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29935390-4f88-3f90-a31b-1a0d8e22a874 | -9.4899 | -56.081699 | 2025-06-18 01:08:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17c8df78-8da4-3221-8b93-6a9db4574fa0 | -10.931 | -56.8447 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 918dd689-9e6a-3dbb-89f3-321e50578ba6 | -12.656 | -54.112 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50c771aa-c5ee-34da-ab3a-d7877987cebd | -14.4226 | -48.912102 | 2025-06-18 01:08:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db4008dd-1078-3668-8760-b508ed61142b | -20.976801 | -47.3834 | 2025-06-18 01:08:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3a1aba1-073b-3257-b88d-787246434586 | -10.9212 | -56.847 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0aeaa5-e682-3caf-9772-cfc2a3e1bd67 | -12.6463 | -54.114498 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 376ed79d-60cb-3540-bb4d-85aec2235263 | -11.9678 | -58.724201 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10acc4cf-9d79-3791-bdae-6c18e69174bc | -11.1311 | -53.9198 | 2025-06-18 01:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4e9b50a-4a96-3a54-86fc-04de065a5579 | -13.7968 | -54.292599 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1c4a15-5521-3723-9fca-d61ca7d48502 | -14.4322 | -48.909302 | 2025-06-18 01:08:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac20b259-f99d-3d5f-98af-249e92f827ee | -14.0652 | -53.3773 | 2025-06-18 01:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4c247c4-4a7f-3c94-906b-5ce324a0cc7b | -12.5128 | -58.356098 | 2025-06-18 01:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb1ab1b4-311e-3bc6-b92d-545df4b722f3 | -11.9563 | -58.719002 | 2025-06-18 01:08:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b234ae3-5f57-3a2e-b202-a01e1dca73b1 | -10.649 | -49.355999 | 2025-06-18 01:08:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 393fd314-6d6f-3808-be61-a7dbd1e2b2db | -10.4631 | -58.686798 | 2025-06-18 01:08:00 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad0315e-76ae-3e3e-a5ee-3db47a5a3758 | -10.3637 | -57.241001 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c13ac688-307d-3076-9a45-ebd85985d3ca | -10.9288 | -56.8354 | 2025-06-18 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
