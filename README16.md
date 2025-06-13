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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 107dbf03-1439-3492-834a-2db094b7d639 | -9.87921 | -61.40105 | 2025-06-13 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e327854-5bcd-39e8-beda-517204b7d23c | -11.55877 | -54.57391 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fa5875e-a953-391c-935b-092933d87308 | -9.14695 | -49.04199 | 2025-06-13 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8f2c408-7c66-3016-9876-b70bfa9068ef | -10.36596 | -57.50549 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f338bded-3fad-31b6-be15-66283abb32d2 | -10.18487 | -49.49908 | 2025-06-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9171c68d-ba43-370e-9f4b-24b5dee10718 | -10.86205 | -54.30549 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f4deffc-a5be-3c2f-a683-03ab8e969d83 | -10.70158 | -49.49979 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9fc5284f-5cbd-3c1b-9974-b59fbb5fad58 | -7.20249 | -45.34995 | 2025-06-13 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b9ece3-d63f-377f-9071-d8560475e774 | -11.3701 | -56.55474 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8623146-a56e-3f69-a284-1aabd2f3b970 | -10.6453 | -49.42549 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cf661390-1a96-3c05-a61a-8ebb1f221183 | -10.64643 | -49.41846 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ddb8c9-9b5d-39b0-9f59-7c23ade8f145 | -7.23865 | -55.41173 | 2025-06-13 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02e587f9-d877-3294-bc51-d92d1fdbb4a3 | -10.81296 | -56.95708 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48e502f-7a7f-3b66-8aa0-15493e3714cb | -10.94085 | -55.32563 | 2025-06-13 04:32:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 91670ed2-f4d6-3bcd-b707-d006c61cc307 | -12.00014 | -45.13372 | 2025-06-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 58384881-d176-3aef-88e8-3dd3067a5141 | -11.56838 | -54.56785 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 598af4ba-57d3-3465-87d6-fcb1478947d8 | -10.65582 | -49.4236 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b750fc1d-3ad9-334a-8f01-6e07987b115a | -10.36538 | -57.23414 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6c053e-543c-3471-8a25-85fabf30887e | -10.64506 | -44.48475 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f89ce3f-eaab-30e3-8cd8-34ec91227202 | -12.13944 | -54.66619 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36e5b9b4-727d-3a99-b488-17d853ce95cb | -10.94008 | -55.33 | 2025-06-13 04:32:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 062e298b-40b2-3a9d-9df0-d3b1d1ef70f1 | -7.46245 | -45.51981 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c9c2843-598e-34ab-9c82-53a5debc7702 | -10.85156 | -53.78652 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d54f541f-ebee-38b7-b4ae-61445671359c | -7.96565 | -47.63763 | 2025-06-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5777b7d5-9ddd-3e72-9019-8abc2e299c72 | -10.84558 | -53.77359 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f9135ac-5dd6-320f-86f2-52ba3e0f1690 | -9.98714 | -48.49795 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5cc4b8c-bc7d-39fe-9d3c-1c3265f8b410 | -9.40035 | -57.54894 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 682b3de7-6ac3-351d-9344-ddf585c0cc53 | -11.57455 | -47.4343 | 2025-06-13 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f934b2-6d64-3f95-b0a9-ebb1597371ec | -10.91787 | -56.83931 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0de87ee8-61d0-3130-8657-9a13b8713456 | -10.88313 | -54.75703 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ebc830-d691-3ec7-8ef4-4eba5257b9a2 | -10.92376 | -56.83466 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 56b494a3-3cad-3ef5-8ca0-156a74c37d75 | -10.6525 | -49.42305 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe514cb7-6677-3236-8ef4-5e2ff9bce560 | -11.12441 | -53.95104 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ca4e664-70b5-35ba-887d-9a02947c45ff | -12.10492 | -48.87411 | 2025-06-13 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd317ab6-b887-3f10-9471-db768c19badd | -11.91961 | -54.82084 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87decd02-4809-3c18-847a-90dd8fcec9bb | -12.2895 | -50.10664 | 2025-06-13 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a532f780-133d-33ff-97fa-25fe37d731f9 | -9.01726 | -48.16452 | 2025-06-13 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b00bbeb2-def4-3d35-b36f-84756ef75b85 | -11.81883 | -54.50026 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aa3ee35-6508-3372-97fd-79953d7d6b2d | -10.65031 | -49.41548 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef5e4e39-b237-39a6-a6cf-8397a1bc6431 | -12.00391 | -45.13428 | 2025-06-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41cd804a-1b4e-33f5-a5f0-9de3a603c559 | -10.29462 | -52.83801 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e5b944d-7977-3507-8ae7-8fd54024b2f6 | -9.88766 | -47.81017 | 2025-06-13 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc961c52-7b27-3490-9608-ab7c0d57f2e6 | -7.45954 | -45.51535 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fcc0505e-4567-32f3-ad05-1de38652f12b | -12.09667 | -49.48567 | 2025-06-13 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9111e311-a142-312f-8484-d9ae648a7fe5 | -10.6489 | -44.48532 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8dc80712-c39c-312f-888c-851401b5a676 | -10.81193 | -56.96269 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c62b59e-8b4b-33ea-9c9f-1cd1b7ce30c3 | -11.37446 | -56.55311 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e456f9-1a29-305a-814f-18db473fff8d | -10.29372 | -57.14284 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8861947-7a4e-3ef8-9cc0-5e15a85cf791 | -11.17212 | -46.88162 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e775d863-4016-37ea-9ad5-84b59178b4e2 | -9.88433 | -47.80966 | 2025-06-13 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062468cf-a565-3a7f-98dc-4ed184372b2d | -10.36654 | -57.50238 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07e601f1-25b1-3a77-9b79-188789b29cc2 | -10.07027 | -52.74266 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5154eddd-9750-3c88-b984-4ed1b6bb98df | -10.65194 | -49.42657 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d95b60ec-fece-3be2-8637-f6345651ddc7 | -7.72299 | -46.61563 | 2025-06-13 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56110236-08ef-3690-a19f-dfb1ff2db44d | -12.29284 | -50.10719 | 2025-06-13 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 711b5e2b-0d01-3a6c-a2b4-007f19751625 | -11.12856 | -54.21591 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d0408e-24fd-3248-ac4f-66e089f68a95 | -9.88525 | -46.2775 | 2025-06-13 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e0f9d0ed-11dd-3d5c-ab29-a5c9c2c9eaf8 | -11.3775 | -55.10723 | 2025-06-13 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bae813e5-6c63-3d6a-9e77-be51a1b8d4c7 | -7.45544 | -45.51871 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 162e8665-6f38-3478-b4e5-fc483ed364e0 | -10.36141 | -57.22727 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0794b1a1-cc7e-3393-996d-1476c5f1e773 | -13.22663 | -47.20253 | 2025-06-13 04:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06cbc969-4b19-36e4-b447-10f0173afd49 | -12.28559 | -50.10966 | 2025-06-13 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abc764b7-e262-3690-86d0-3899d8e35894 | -9.60695 | -49.01235 | 2025-06-13 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a1fd091-e86c-31b1-878f-f84d938bc00b | -10.9189 | -56.83374 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 86a8dbea-5c42-30e0-acd9-73b3bca48e5e | -7.44493 | -45.51707 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1d8f2a2-9114-3cf0-9fa9-aec0abfdfb17 | -11.13364 | -53.94549 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96748638-55c8-3e6e-a2bd-4677b29b6f2e | -9.2465 | -57.53292 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba2aad0-5cc2-3083-9127-9c6ddb7fa5b1 | -13.09629 | -52.28535 | 2025-06-13 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7107e481-c953-3128-a24b-eef176ce2a17 | -13.35553 | -52.27765 | 2025-06-13 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f259fd-95ac-3e55-9d35-c24994c7d841 | -18.89746 | -54.72308 | 2025-06-13 04:34:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3b6ea5a-2448-3cec-8bbf-c658231e066e | -17.38601 | -53.81836 | 2025-06-13 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0580dc49-5702-3c2c-9c75-46d105c40312 | -16.73888 | -52.31233 | 2025-06-13 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3655d96d-c03d-307d-a2ef-1caab40f7e04 | -12.70426 | -58.03772 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc9087ef-a921-3e8a-82b4-bdb234a96c22 | -14.84139 | -48.30834 | 2025-06-13 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0643593-88e4-3b7d-b962-88187eb85fc1 | -15.38858 | -47.87529 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91bfe3bb-967e-36be-8219-46651b3ffa4b | -18.97651 | -52.87557 | 2025-06-13 04:34:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 338fcbda-4743-30b2-b554-24eaab75f28d | -13.90065 | -54.62857 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0498dd6-7534-3d9a-b04e-7bf71771e545 | -12.51407 | -58.34301 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c4ced69-90fe-3fda-9b04-d6f9e42ba9d9 | -13.90001 | -54.6321 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d23962e-8c64-3e46-8b6b-2c7cbab617de | -12.43131 | -54.8727 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9c2adc4-b93d-3218-a094-5a0196fe2652 | -13.98061 | -56.01569 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6511d966-f94f-3670-ac9a-abb884900f3b | -14.20094 | -57.40536 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| baa951ff-1454-31db-840d-107d5703284e | -17.65517 | -47.45388 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325a418a-20fa-3085-ae54-2263c5d4b1f2 | -15.38802 | -47.87907 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1081035-5442-3017-9552-e6215d84709c | -13.89473 | -54.63846 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3231e7a9-c626-3e6f-aa45-a2963d5338d7 | -13.98494 | -56.01666 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b007cbd-eb67-364d-9aff-01be2b01c501 | -13.88996 | -54.61925 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b83e6ff3-4974-3bda-a80a-6c0a041f0d80 | -14.20192 | -57.4002 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5894c951-820d-3e40-8e0b-acbb5fa1556e | -19.69958 | -54.61408 | 2025-06-13 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1f0845d-33b9-349e-a2fd-03ecddf8f06d | -14.67448 | -53.36311 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 691ffe12-2abd-3461-9ec2-eb66c0dc37ab | -13.89794 | -54.62075 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e0a7f3f2-8291-3589-9e3a-0f793a942535 | -17.6629 | -47.45074 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a00f147-90dd-32aa-95cd-c9e4544f117e | -14.20765 | -57.39603 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37e43b56-93ec-38e4-9334-77018197f555 | -12.51688 | -57.23175 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c2bedde-9e0f-3962-bd4d-5475e07def7c | -15.37259 | -47.86475 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2910acf7-cd36-35d5-b23e-dfbad9667395 | -14.1952 | -57.40954 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7eba1c0-f9bc-3af5-ba83-cf63919f1df1 | -11.91994 | -57.47265 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c40bea7-cd78-3e19-b570-9730383da0ba | -17.65398 | -47.46243 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d666037c-e1a4-3d30-b5f8-495d4413fb23 | -12.51928 | -58.34412 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 160cd018-8d09-31f2-a273-646d2b0cf777 | -11.91887 | -57.4784 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
