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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6f7ea16-619c-3e4a-81fd-4847d13bf7ff | -20.582 | -49.3635 | 2024-10-06 01:57:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 3ad874de-3cd1-339a-ad53-3c286ae3572a | -20.6024 | -49.3591 | 2024-10-06 01:57:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0d4a1984-23c8-3e54-a504-d0ca7047f4d0 | -21.5218 | -50.9088 | 2024-10-06 01:57:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| 74da7d18-4ae5-3fff-b1f1-84b51dfa451d | -21.5425 | -50.9045 | 2024-10-06 01:57:05 | GOES-16 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| bfcd420d-68c3-3276-998c-febaaf0672cf | -10.42 | -50.75 | 2024-10-06 02:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a60d4db2-af2e-3606-ae5b-bad87e449597 | -10.42 | -50.69 | 2024-10-06 02:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6ca2180-380b-3fa7-b873-132ecff9ebfa | -10.45 | -50.76 | 2024-10-06 02:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 111e95a2-b97f-34b6-94ab-ebdda747a9b7 | -10.45 | -50.7 | 2024-10-06 02:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8876ce2b-561e-36cb-bccc-f6b709061918 | -1.7668 | -47.1984 | 2024-10-06 02:05:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0a79982e-b3dd-3e17-9b66-f2141fb94e0f | -2.7981 | -48.6873 | 2024-10-06 02:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0f240657-3a96-3f36-ba89-9f0dbd48aea4 | -2.8165 | -48.7082 | 2024-10-06 02:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 15adac55-7dc3-30e2-8ee4-73f034b46bc9 | -2.8166 | -48.6867 | 2024-10-06 02:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| e5692316-5421-33ec-b56c-37519d5e19ae | -2.847 | -50.4648 | 2024-10-06 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 93fdf5cd-321b-3008-9144-37f4b82a7271 | -3.1053 | -50.4573 | 2024-10-06 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0f90448f-c21f-305e-b1b9-c882cade7064 | -3.1129 | -48.6131 | 2024-10-06 02:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1e04533f-0712-3453-a607-30034baa6e20 | -3.1314 | -48.6125 | 2024-10-06 02:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 8875ba45-7c2b-3509-b428-2f308d653dc6 | -3.1315 | -48.591 | 2024-10-06 02:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1affb685-9f8d-3856-9240-aea49eb4b118 | -3.2223 | -48.9733 | 2024-10-06 02:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| cb728581-c0aa-3ed1-bedd-563fdc77d925 | -3.4195 | -50.3844 | 2024-10-06 02:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3243f254-bda8-35a2-9d27-47fcb7f4f1b7 | -3.7066 | -41.6997 | 2024-10-06 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 968b8335-ce7b-3bea-86ea-ee7a632e8c56 | -3.7068 | -41.6758 | 2024-10-06 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 469fe57b-7f74-37d0-8c26-33763be4111a | -3.8008 | -41.5989 | 2024-10-06 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 6ba9c7d3-6bec-3726-95c3-1eaad41d8c89 | -3.775 | -49.4643 | 2024-10-06 02:05:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| b1a87a11-40c2-368a-94b9-c9f96c588d76 | -3.7934 | -49.4849 | 2024-10-06 02:05:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 166d6aeb-16d8-3f3f-851b-814ccedfb313 | -3.7935 | -49.4636 | 2024-10-06 02:05:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 78a6e4a9-c251-3f8e-a0ab-ad223a79a4be | -3.9103 | -48.3466 | 2024-10-06 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 945070ec-c69e-3ad2-883c-6397589a3f8e | -5.5716 | -44.8927 | 2024-10-06 02:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 673d9c56-cf38-3526-b554-f574e6731d7c | -5.5718 | -44.87 | 2024-10-06 02:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8dfa4f16-b811-3e6e-8898-af86b973c90c | -5.5905 | -44.8687 | 2024-10-06 02:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c404f00e-10ae-3597-a215-0486b4417efe | -6.9514 | -59.0666 | 2024-10-06 02:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 24e44f30-061f-35d7-921f-3bcab03e8ef3 | -8.2139 | -61.2022 | 2024-10-06 02:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1c06caec-1b76-3f18-a098-71ed79e606a5 | -8.8724 | -48.2424 | 2024-10-06 02:05:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b26b12d9-4fac-3c75-9041-5efdaf0bf6fe | -8.8727 | -48.2206 | 2024-10-06 02:05:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d1e02783-92c2-37e2-8f0d-5d9cf8816279 | -8.8913 | -48.2406 | 2024-10-06 02:05:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 9446cbd7-2510-3458-b5ea-897b0b7f12b6 | -8.8915 | -48.2188 | 2024-10-06 02:05:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 3d73887d-7da5-38a2-aa2f-f353bd3b8dd4 | -9.1449 | -60.6612 | 2024-10-06 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 09bf8212-9fbc-3bf5-93c3-c40d53d94b5b | -9.1573 | -61.5803 | 2024-10-06 02:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| aa316e72-ef21-3bdc-9c59-33e8b9398a91 | -9.1574 | -61.5611 | 2024-10-06 02:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 5e7d431a-8c7a-38fd-a881-481b385c4a3a | -9.1759 | -61.5794 | 2024-10-06 02:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e23a6861-172f-31ac-ba0a-17dd3c785add | -9.3278 | -46.5385 | 2024-10-06 02:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 547b6420-60f0-3274-af13-2a4c9caa8eb6 | -9.3464 | -46.5589 | 2024-10-06 02:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a770c8ee-2b8d-3924-80d7-eabbdeccb2cc | -9.3467 | -46.5365 | 2024-10-06 02:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 039d5fc7-8567-3b7e-87b4-33ff3fa25396 | -9.3647 | -51.0898 | 2024-10-06 02:05:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d807e952-9ae7-34d7-91ff-a9eacaa3400b | -9.365 | -51.0687 | 2024-10-06 02:05:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4212a9be-8654-3b3c-a36b-309afbb8b29d | -9.3835 | -51.0881 | 2024-10-06 02:05:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 027780d7-a85e-3996-88e0-20e1057b7239 | -9.8552 | -60.2966 | 2024-10-06 02:06:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5f0fe063-3fe3-35d5-a508-cebc5111c419 | -11.0966 | -54.2336 | 2024-10-06 02:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c4d6bb30-7708-3d18-86d9-c425eb4f9ef5 | -11.1155 | -54.2319 | 2024-10-06 02:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7e465de4-0341-32d3-90fa-9d064eea47eb | -12.0211 | -63.7478 | 2024-10-06 02:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 7019c0bb-4fd8-3432-9522-d657d9e22876 | -12.6089 | -53.1338 | 2024-10-06 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b6bb7570-b855-3496-873f-b237aa79d56a | -12.6092 | -53.1129 | 2024-10-06 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0bea78c8-81f7-3246-832c-1681acfa6155 | -12.628 | -53.1317 | 2024-10-06 02:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 60277e90-0656-3a28-be21-9d098d05302a | -12.6283 | -53.1108 | 2024-10-06 02:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3e08ae91-bc3c-3882-ba1b-90aa6d2113f8 | -12.6532 | -54.0415 | 2024-10-06 02:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d885d1ff-2409-3bc0-9825-144dca5d0c95 | -12.763 | -50.5352 | 2024-10-06 02:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 46a947ff-178c-36bc-a82a-a1fc3695e19c | -12.7634 | -50.5136 | 2024-10-06 02:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4eaf5842-02ef-3519-a840-845d8c53c3ab | -12.7822 | -50.5328 | 2024-10-06 02:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ca336f15-e5b8-34a0-9d34-45fde6284966 | -13.6724 | -51.1911 | 2024-10-06 02:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ef0da616-33ae-3003-b4c2-7a477a2ad8a1 | -16.3956 | -57.3845 | 2024-10-06 02:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| a6ff4d7c-95f8-3fa7-af34-583f35ab4ef9 | -16.3959 | -57.3641 | 2024-10-06 02:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| bebbfe85-ee8d-3551-9084-aa6f1685d36e | -16.5553 | -55.9287 | 2024-10-06 02:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 0da1c20b-e4d5-3161-b045-5ed56911dbe9 | -16.4151 | -57.3823 | 2024-10-06 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 6c3dce49-72e9-3689-ab56-3cf94d7237ed | -16.4155 | -57.3619 | 2024-10-06 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| e0157a2c-ef5b-3ee4-a6fa-38d7bcd1e616 | -16.6923 | -55.9117 | 2024-10-06 02:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 2fcbd9f4-91f5-378b-b4c1-d13aecb708ac | -16.6398 | -55.5452 | 2024-10-06 02:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 8796afec-caa8-3bd7-b719-8ccb5bca11d0 | -16.614 | -55.9214 | 2024-10-06 02:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| aff3b252-5602-3340-b77d-a083ea80af4a | -16.9348 | -56.625 | 2024-10-06 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 43bce5c9-90f8-3c38-b551-2129378a48a7 | -16.8238 | -57.4584 | 2024-10-06 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| faa2b2a7-ea3e-3f58-88a7-5212b44315df | -17.1284 | -56.7661 | 2024-10-06 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| f6922a68-88db-3785-b4d9-13bc7a68375b | -17.1182 | -57.4039 | 2024-10-06 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 754c96f7-4a5a-3afc-ac90-59e2ba6deb0d | -17.0207 | -55.0371 | 2024-10-06 02:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| df6d9ce1-bfaa-31d9-b14b-17b12c3e0ac2 | -17.0203 | -55.0581 | 2024-10-06 02:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 22b803bb-e89f-34e6-8851-7b69e657532d | -17.0007 | -55.0607 | 2024-10-06 02:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e76c9f0f-c803-33e7-96ed-ddee9b4a70f2 | -17.1571 | -57.4198 | 2024-10-06 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 57815926-4d7a-3ebd-9bf2-6467d5849dbf | -17.1375 | -57.4221 | 2024-10-06 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| bfb8f1ef-8fa0-363b-974a-a5181f69cd93 | -18.659 | -57.2552 | 2024-10-06 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 5daf2baf-9221-3aae-bffd-c8dfe60a5f31 | -18.6586 | -57.2759 | 2024-10-06 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 0a51c704-f6bb-33d3-bb3d-a07301fdd94f | -19.8516 | -42.3738 | 2024-10-06 02:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| 7dd6cc83-bfd0-3318-bdca-bcd5f777cd33 | -20.5813 | -49.3865 | 2024-10-06 02:07:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b89ee190-d931-3417-bb71-cf42740aed4f | -20.582 | -49.3635 | 2024-10-06 02:07:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 101.1 |
| fa412c2a-7768-3b3a-a6db-7554754aff66 | -20.6018 | -49.3821 | 2024-10-06 02:07:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1bcce83b-4fbe-3810-bcf1-d06a7a38da78 | -20.6024 | -49.3591 | 2024-10-06 02:07:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e9696aea-1288-3d87-b6d2-78fb76ea122a | -21.5218 | -50.9088 | 2024-10-06 02:07:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 08c884f1-ec4a-3010-9dd7-3beab04fb6f7 | -1.7668 | -47.1984 | 2024-10-06 02:15:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fa941643-346b-352d-b52b-77b9831c5b37 | -2.7981 | -48.6873 | 2024-10-06 02:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9b9ecce6-74fb-3335-bac9-cbf844f61a1e | -2.8165 | -48.7082 | 2024-10-06 02:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e7139e0e-d2fa-38a8-afe6-41fed5ccba78 | -2.8166 | -48.6867 | 2024-10-06 02:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| bc6dcc2a-5d97-38ce-adc7-4356f5568e2d | -2.847 | -50.4648 | 2024-10-06 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b1274703-884d-3345-bd52-b3c4b914ced7 | -3.1129 | -48.6131 | 2024-10-06 02:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| cf11531d-8e4a-370e-9a3b-62fd70babafb | -3.113 | -48.5916 | 2024-10-06 02:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 713902d0-6927-328a-a0fd-a0480ebdada5 | -3.1314 | -48.6125 | 2024-10-06 02:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 132a0b4e-e1cb-3817-bfaa-2a77d6dc5f33 | -3.1315 | -48.591 | 2024-10-06 02:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0ad85157-a662-3e43-bc6a-7826f3941d9f | -3.2223 | -48.9733 | 2024-10-06 02:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2c4795d4-c759-3455-ad51-7fe6e5ca54ea | -3.4195 | -50.3844 | 2024-10-06 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9509dbf8-f802-384d-8c3e-4c29005c3de5 | -3.7066 | -41.6997 | 2024-10-06 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 4c81c2a4-8745-38f0-ad10-47deb25d1d61 | -3.7068 | -41.6758 | 2024-10-06 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 88cd2a47-21a6-3c15-9b8f-1c7eeab031c6 | -3.8008 | -41.5989 | 2024-10-06 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| b63f1365-76b0-365b-a074-db00e1c11c9d | -3.801 | -41.575 | 2024-10-06 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 8c844daf-9a9a-3fc0-959d-e93e9f34526b | -3.775 | -49.4643 | 2024-10-06 02:15:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| eb66ab76-16dd-39ce-adb6-0c7c3b682a53 | -3.7934 | -49.4849 | 2024-10-06 02:15:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |


[Clique aqui para ver as próximas entradas](README35.md)
