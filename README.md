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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f412699-d4d7-3040-87a8-fc053221f411 | -4.5243 | -48.016 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 6a542955-6495-3569-ade9-865f72b408e7 | -11.8666 | -54.6535 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 9929fe23-c40b-318f-89c8-e13a404c44ea | -13.0392 | -53.7107 | 2025-06-21 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 17b67472-8e05-37b0-a3c9-f80535962cb0 | -11.8663 | -54.6739 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 331.4 |
| 2b229f7b-c129-35ea-9fab-ad397ead71fa | -9.4648 | -57.8449 | 2025-06-21 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| c3ce3644-814c-3758-b40c-98823dc8271a | -11.7791 | -57.2445 | 2025-06-21 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 476bd3fa-6334-33e5-84fe-5f61b8a6e157 | -3.967 | -48.15 | 2025-06-21 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 7a2a5607-859b-3f2f-869f-a3a2b8e86ece | -11.798 | -57.243 | 2025-06-21 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 2f555bf0-4826-3bc9-9bab-8735ef9e6646 | -9.4837 | -57.8241 | 2025-06-21 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 44984429-87d7-39cc-adf3-69fe452eb63d | -8.0152 | -47.6656 | 2025-06-21 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 4a5c4c4c-0796-38c4-bc10-816f79cabfcd | -8.0154 | -47.6437 | 2025-06-21 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 46e9d632-1c6a-3644-9340-85b2162586b9 | -11.9518 | -58.7574 | 2025-06-21 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1795870a-4dc3-3488-8a9e-e8d69a1795ef | -7.2408 | -43.0664 | 2025-06-21 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 8217d250-004d-3905-a0c3-80d505ee89b5 | -9.465 | -57.8252 | 2025-06-21 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 1820d551-2d6f-3aa1-89b5-204587c70551 | -3.9671 | -48.1283 | 2025-06-21 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 0a17e5fd-1ed4-385a-ba5b-9c90faaa8b5e | -22.4046 | -50.3061 | 2025-06-21 00:00:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d6f1361b-8d72-3fa8-a183-611908e5799d | -3.9486 | -48.1291 | 2025-06-21 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 29cc56e3-6ad0-3a2c-bfc6-de194afefff5 | -13.2535 | -49.845 | 2025-06-21 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 57439235-2327-31c7-81d8-0ab2ef61abb3 | -9.2622 | -57.5426 | 2025-06-21 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bd854379-5e13-3888-a4e1-8bab2f2380b0 | -4.5429 | -48.0151 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 326.0 |
| 6ec9274b-2c5a-3cd6-9a52-f6938aed2e39 | -13.2343 | -49.8475 | 2025-06-21 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 905e89a2-65d9-305e-82c8-8fe0ae9d9ef2 | -3.6181 | -47.5134 | 2025-06-21 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3c7c1a12-3c6b-3144-a4a0-6214123cd027 | -11.952 | -58.7376 | 2025-06-21 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 15e441f3-0214-39e8-ac3b-b164768e776b | -13.2346 | -49.8258 | 2025-06-21 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 35f604a0-aee9-3649-8cb9-b15e9caf3d34 | -9.4835 | -57.8438 | 2025-06-21 00:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| fdaa9bc4-c432-3b86-9c5d-90d20e899412 | -11.8853 | -54.6722 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 725.8 |
| af6299ac-6e42-3ec9-8132-30dbde1c9867 | -10.883 | -56.4567 | 2025-06-21 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| eaa65f03-8d5a-3b00-94b1-401383173a03 | -11.7983 | -57.2231 | 2025-06-21 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4486dc64-48e4-3106-bfdc-a44255a4b045 | -10.1636 | -48.9814 | 2025-06-21 00:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ccb2149f-840c-3973-9009-60ad3dbb4229 | -12.2727 | -44.5967 | 2025-06-21 00:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| bbf0ce43-84d5-3ea0-96b7-20380f2f71ef | -4.5427 | -48.0367 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1779be31-c39b-3225-811d-e6f0a9fc88b0 | -13.2539 | -49.8232 | 2025-06-21 00:00:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 736ec104-4827-345e-9966-b770feae0283 | -7.2219 | -43.0682 | 2025-06-21 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 218.0 |
| 540ccf69-1af6-3ab4-ba5e-853d06768c7b | -11.866 | -54.6944 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 43159fa8-9d6e-396e-b946-2754479bdc72 | -3.9857 | -48.1275 | 2025-06-21 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| cd57ef60-3cc5-35ab-b5a3-3e72465e5830 | -11.885 | -54.6926 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 45ea9dac-4983-387c-8be7-c2379415bfe4 | -4.5614 | -48.0141 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e47c344d-0c92-31ea-af93-b0a8962294fc | -11.7794 | -57.2246 | 2025-06-21 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b6813d2f-5fcb-3c55-ab98-aa00f61c7d43 | -11.8855 | -54.6517 | 2025-06-21 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 302.6 |
| 26ff6537-de23-3042-a346-a0a242a3fa72 | -8.034 | -47.6639 | 2025-06-21 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7f94ff38-e0df-3e92-ac80-99fe5210159d | -4.5244 | -47.9943 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b72b1044-4cfe-30fc-aa72-6e96eecc79d1 | -4.543 | -47.9934 | 2025-06-21 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| d2dae8e2-59a6-3a8c-b5b4-8e54201ad6b7 | -9.2624 | -57.5228 | 2025-06-21 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ebf7f522-7de9-320d-8731-0c9cdd4c3528 | -22.3838 | -50.3108 | 2025-06-21 00:00:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b3391a99-41bf-3b83-b39e-484398024e8c | -3.967 | -48.15 | 2025-06-21 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| cc577e30-d51a-3f45-bbd5-1d5c2fb2acbd | -3.6181 | -47.5134 | 2025-06-21 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 61c762fe-00f2-3c72-a811-ce008ea73bc8 | -11.7791 | -57.2445 | 2025-06-21 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| cf60ab30-5b22-340e-a331-25b400dae7fd | -9.4837 | -57.8241 | 2025-06-21 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b41f9df4-6d42-3524-beda-e11bd3b0c0b6 | -8.0152 | -47.6656 | 2025-06-21 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ba2be170-a78a-3f74-ab69-ecc81df5d023 | -11.8855 | -54.6517 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 285.2 |
| 167cbce4-52fe-3a56-a2f4-bc1269b4208c | -9.4835 | -57.8438 | 2025-06-21 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1a664b8d-ebc3-3885-a538-281149a9fe0d | -8.0154 | -47.6437 | 2025-06-21 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 39e1e313-f440-36bc-b5e0-97cd5018e994 | -13.2343 | -49.8475 | 2025-06-21 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b5b0a3ad-1b3f-3528-bba7-194883c2e4e3 | -9.0296 | -61.2229 | 2025-06-21 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4b5f1815-d250-322d-8e50-1f31b552c4f0 | -13.0392 | -53.7107 | 2025-06-21 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fdc0fad2-3b59-3675-8582-3f9b5c8df84d | -13.2535 | -49.845 | 2025-06-21 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cfd3fbd6-47cd-333f-9064-8f67e8cbee61 | -11.866 | -54.6944 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d5385933-2a22-36e4-9f8a-a175db3e84cd | -11.885 | -54.6926 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| ee1457c4-76b6-393d-88c9-db58a65f6d1b | -4.5244 | -47.9943 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 380eb603-61d4-3b25-a6ef-d9b20121bc9f | -4.5429 | -48.0151 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 381.8 |
| 517c4833-7f5c-3138-b55d-be452380a36c | -11.7794 | -57.2246 | 2025-06-21 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 32548226-cfc9-33bc-bf46-dcd37700ccda | -3.9486 | -48.1291 | 2025-06-21 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e5843b5f-c126-37e7-8ebd-dbb083bf4479 | -11.7983 | -57.2231 | 2025-06-21 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8280908d-d4c4-31be-9a0d-b662e29c2af8 | -11.9518 | -58.7574 | 2025-06-21 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 62a4bee6-5fe0-3dc3-afa0-55289dc03821 | -4.5427 | -48.0367 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 960f47fb-409b-361c-ae2e-ad1b87c04780 | -9.465 | -57.8252 | 2025-06-21 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 886a4b94-8b39-3c8c-b212-24da61cbb550 | -4.5614 | -48.0141 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0e24a45f-094d-3d92-9943-a46fe28ea0b9 | -10.883 | -56.4567 | 2025-06-21 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 050561ea-eb64-3e17-a3d6-d54f96c76ff7 | -11.798 | -57.243 | 2025-06-21 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 7de648f6-1ef4-38f7-a571-deff7ac1ae3f | -7.2219 | -43.0682 | 2025-06-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 214.9 |
| 037920d0-4246-337e-80ab-164836eb0adc | -7.2222 | -43.0447 | 2025-06-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 77166351-3d68-38f8-b50a-d4eb85df0df4 | -4.543 | -47.9934 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 167.9 |
| f11e0567-4cac-395f-86cc-b6487c9da419 | -11.8666 | -54.6535 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 6c819217-0129-3f04-b0bc-3898a1fd953b | -13.2346 | -49.8258 | 2025-06-21 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 01ed280b-588e-3668-ae21-0004cbac3d24 | -7.2408 | -43.0664 | 2025-06-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 0a37644c-15b1-3480-ae9a-5da87cf9afb6 | -11.8663 | -54.6739 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 2c16bff3-69a6-3d78-b7b7-25b0d829a561 | -9.2624 | -57.5228 | 2025-06-21 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 23971ceb-c3d5-306f-a667-4bb38dbc15ce | -4.5243 | -48.016 | 2025-06-21 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 82335ae0-80ee-36e2-9a0a-498a38fec254 | -3.9857 | -48.1275 | 2025-06-21 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c7a1c035-4a51-3110-938b-c9d40ca58fc4 | -11.8853 | -54.6722 | 2025-06-21 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 623.0 |
| 7eef22ae-773b-3ee1-ace4-1e2ad63b5beb | -9.4648 | -57.8449 | 2025-06-21 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 32a8af0f-1dbd-3387-ad9d-8ea761a5e008 | -13.2539 | -49.8232 | 2025-06-21 00:10:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d59cb41a-6fbb-3a9d-99ed-8581ae665961 | -8.034 | -47.6639 | 2025-06-21 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 8fba3b37-bea3-393c-863e-a3b6edb29292 | -3.9671 | -48.1283 | 2025-06-21 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 197.1 |
| 2a584a86-d866-32bb-9663-0133fdcabb2f | -7.2408 | -43.0664 | 2025-06-21 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 8d8627cf-3c56-3270-a71f-ef76b76eccb7 | -11.8663 | -54.6739 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 329.5 |
| 229fa015-2c37-36b8-bca1-73d97abe2b62 | -11.7791 | -57.2445 | 2025-06-21 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 3651e76e-329b-3195-9c85-364c66e60461 | -9.4648 | -57.8449 | 2025-06-21 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| b97e35f2-e24a-3027-9489-1c02eda9c01b | -9.4835 | -57.8438 | 2025-06-21 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a744c3f3-c13f-38f7-8519-562e7238375f | -9.4837 | -57.8241 | 2025-06-21 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ab89f664-e113-33ef-995e-d97d1fded7c4 | -4.5429 | -48.0151 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 427.3 |
| a2fc84ef-1ee8-375b-a1f8-bd60058f2d02 | -11.798 | -57.243 | 2025-06-21 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 61db4ea4-425e-32dc-985a-632c8fc177b2 | -3.9857 | -48.1275 | 2025-06-21 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| ff3e023a-7101-3024-9e62-0c791ab9eb8f | -7.2217 | -43.0917 | 2025-06-21 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 9a6e88ec-2b07-359c-a834-3325ed8f2c9c | -11.8853 | -54.6722 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 681.6 |
| 50c7dcba-660f-39b9-849c-47bcbe121271 | -4.543 | -47.9934 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 7c548b30-b9eb-3462-bf79-334befc55038 | -11.8666 | -54.6535 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 66b3dae0-7ba1-3835-b6a3-202b89d84779 | -11.9518 | -58.7574 | 2025-06-21 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7669b673-2e85-36da-9df6-ba7dfe6ae8ec | -11.866 | -54.6944 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 64346be5-f57c-3a90-9059-efb9a8d69843 | -3.6365 | -47.5345 | 2025-06-21 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |


[Clique aqui para ver as próximas entradas](README2.md)
