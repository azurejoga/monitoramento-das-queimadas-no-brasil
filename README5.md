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
| a97012f5-9760-3af5-aaeb-c851b3cdf767 | -10.94614 | -48.15257 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10d902c8-b1b2-3066-bdac-292f5416e526 | -11.75633 | -54.22854 | 2025-05-26 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee21b15f-9ffd-3e39-8fce-939c063d18ae | -11.57628 | -47.61794 | 2025-05-26 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9746bbae-b598-3b0f-ac95-3a45be318d9b | -11.36976 | -55.11872 | 2025-05-26 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a6edc43-04c8-3fe2-a955-d26d052661e9 | -11.55815 | -47.61469 | 2025-05-26 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5247ea75-34a1-3e05-8862-78bb44a82b66 | -11.14348 | -53.92749 | 2025-05-26 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bac0d3ab-807d-3fd1-9f32-efd458cba18f | -12.25182 | -46.68302 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d80135d-6195-39f9-8cd1-d2235de138fd | -17.09679 | -43.80415 | 2025-05-26 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9099ac0d-9868-3b5e-bcf6-773db05c4a75 | -10.95025 | -48.14928 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e72103d6-8d85-300c-b001-a1a0531910aa | -11.36913 | -55.12204 | 2025-05-26 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e49686d3-7b25-3a41-998f-2654c778474a | -16.68162 | -43.88566 | 2025-05-26 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4c281c7-5c26-3c0e-80f9-3732f4c112fb | -10.70218 | -48.58978 | 2025-05-26 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4947f038-3eba-3215-8be4-b350563c3c2b | -16.81934 | -46.82467 | 2025-05-26 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eba30b2b-938e-320e-a4ce-90716661d31b | -10.45332 | -47.94477 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb8c0ded-5f15-372e-a9cb-723c3169d02a | -11.57079 | -47.92835 | 2025-05-26 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70de2fd6-3364-3a3f-b3e6-5ccfc2e68a45 | -10.69792 | -48.59344 | 2025-05-26 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4a51db8-b4dc-3fd8-b7f8-9e83668bf0ed | -14.88372 | -47.85292 | 2025-05-26 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5399cd4-6c5e-3cc3-9017-c44a87c3a762 | -11.11097 | -44.63458 | 2025-05-26 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14dc5614-5783-368a-aeec-6001250129aa | -11.69673 | -55.45702 | 2025-05-26 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2f1d1ba0-13ff-3a5b-8483-099725f22c6d | -10.64725 | -46.96729 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45da2735-8763-3f60-b8e9-f270bc5d9ccc | -11.57508 | -47.61748 | 2025-05-26 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df28fd34-183c-3a14-be8b-cf717059f87a | -15.60824 | -42.57153 | 2025-05-26 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4f467c9-2e0f-318c-8f81-e27c440d92bd | -11.86972 | -52.26049 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c3d796e-c849-31da-b69b-72d196c5f963 | -13.32955 | -49.21984 | 2025-05-26 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddc558aa-ca43-3604-8b77-d94852bccdf7 | -13.78677 | -54.31445 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72fc7cca-04f7-3617-b6dd-3f2620ced688 | -10.45741 | -47.9415 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e112b28-1024-3c46-a1d8-db2900b60f8b | -12.25457 | -46.6871 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc3159cf-29cc-34bb-a977-e4b4ce86c48a | -16.97613 | -48.97292 | 2025-05-26 04:21:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 466b44ab-e1aa-31d5-9bee-d610e8ff4ab6 | -15.92688 | -46.06273 | 2025-05-26 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8292266a-1d6d-3f7a-966b-b708334b1efe | -15.42925 | -42.16636 | 2025-05-26 04:21:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0c09faf3-c879-341e-b3a4-6f554c16a1eb | -11.87046 | -52.25624 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 43ce4af7-83a8-36d9-bae8-bbcf8824ad98 | -10.46023 | -47.9459 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5074121c-87f9-3bfa-8dee-7fb4d4823649 | -10.64783 | -46.96368 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc02632d-ec9f-3c6f-994d-541fd6f5ec1f | -9.97452 | -52.13908 | 2025-05-26 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3767ba88-910f-34b5-9394-97cc79bd306b | -10.65452 | -46.96479 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6900bea-4e0a-3e16-a088-f48f896c4bc7 | -11.01172 | -45.1277 | 2025-05-26 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37ac7afd-9372-30dc-a5e8-aa9679a3e95a | -11.99592 | -52.47104 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 018bc470-9555-35df-bda4-9a7bcb67ab49 | -16.14855 | -45.94555 | 2025-05-26 04:21:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee3e3a29-54ad-34b4-968f-52eb04af22ad | -16.36071 | -49.33135 | 2025-05-26 04:21:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0841d728-9f71-36b3-8b3f-c1b7e739d4a1 | -13.61132 | -48.94662 | 2025-05-26 04:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a875b7c0-1bf1-3467-a513-f21f72bcfb9c | -13.78571 | -54.31992 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0f7e417b-dfb4-35aa-986c-0a244cec169d | -17.75663 | -42.89791 | 2025-05-26 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 229b694a-cd5d-30dd-93a3-ba54ef787beb | -14.57848 | -48.34806 | 2025-05-26 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12f5b034-e4bb-3340-9b3a-d964e15aed84 | -11.99513 | -52.47537 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9622d92-28ea-3018-beed-19bd653a3ed1 | -15.5709 | -47.85466 | 2025-05-26 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69d96489-9192-31c1-a601-f0e8a86cf52e | -11.86804 | -52.25443 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90cabc53-8dd5-3029-be0e-3f9928d6499e | -13.65523 | -45.5588 | 2025-05-26 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 517868ae-3a78-3366-9028-81145d98caba | -13.48031 | -44.05038 | 2025-05-26 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8bbb95c-6b27-3e0a-8418-afb01099358a | -15.07743 | -48.94639 | 2025-05-26 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf15217e-d4f0-3267-9d3d-5f79e7f79dcf | -11.29809 | -54.01931 | 2025-05-26 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccfe9ada-cd7c-3e90-b8fa-26bab4c19de5 | -9.97373 | -52.14352 | 2025-05-26 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26e35050-f7af-32cc-b3c1-b288a2e762dc | -15.29992 | -45.5797 | 2025-05-26 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fbbe984-17ea-36e6-9386-5217a7023b97 | -13.78214 | -54.3159 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 08b35203-baea-3795-8af2-38b082bbd2e0 | -10.65117 | -46.96424 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c6953d2-6f60-33c5-a6d9-4ea62647c683 | -12.25513 | -46.68356 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22176ce7-9a98-31be-9a12-9063e3a8e2ab | -11.14017 | -53.92995 | 2025-05-26 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 20f89b44-4d39-3d1d-9eef-1f3cc57820f4 | -11.86726 | -52.25865 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f1bbe46-3d34-36e4-8623-651f3009a94d | -13.35489 | -48.0232 | 2025-05-26 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b543a6d-fc67-382c-8000-1b813b397335 | -11.69738 | -55.45359 | 2025-05-26 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| efbb2719-10f2-3984-87ec-1249718941ac | -11.29914 | -54.01363 | 2025-05-26 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe1f5e91-8637-3c49-8402-acbe9879b9c8 | -11.8712 | -52.25205 | 2025-05-26 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1581d66b-c6c7-36dc-b995-c86a99090eea | -10.45678 | -47.94534 | 2025-05-26 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a60961b-d848-3698-b0b7-f29cc6e51d8c | -17.91661 | -45.5372 | 2025-05-26 04:21:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a260e5e-b638-39f5-ae56-c347619fe786 | -23.63221 | -46.42531 | 2025-05-26 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7c66026c-3d46-3d46-943e-6ddb0976b134 | -19.43757 | -44.34019 | 2025-05-26 04:23:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd488ed-c66f-39ca-81c2-991df23b6fad | -23.98318 | -48.91764 | 2025-05-26 04:23:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5710c03c-160c-33fa-a52e-0ba2cd674f69 | -20.60767 | -48.86868 | 2025-05-26 04:23:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1984e813-d9c3-3372-9d13-931d9210bcfe | -21.27522 | -48.61126 | 2025-05-26 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| eedec3e9-1fc2-3863-aa4b-360f5c0cd597 | -20.60827 | -48.86496 | 2025-05-26 04:23:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7d107928-98e8-39a6-881d-b6bd3385dbcb | -23.04666 | -49.89583 | 2025-05-26 04:23:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3cfabb4b-c0cf-3ac9-95e1-00bf1a626449 | -20.22185 | -50.75465 | 2025-05-26 04:23:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 131033d9-6a87-3240-bea3-45b31a8c9c62 | -17.37609 | -52.01736 | 2025-05-26 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 644a9d1a-f508-38ab-92ae-f55e59416580 | -23.61518 | -46.30515 | 2025-05-26 04:23:00 | NOAA-21 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39c8e428-35c0-3fda-afca-4eae3be1b12c | -22.85727 | -42.98186 | 2025-05-26 04:23:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ce162cb-ddc7-3baa-a179-4ab810ad1bcd | -22.90088 | -43.75395 | 2025-05-26 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ed97a8d3-8f3b-30db-99e4-201e9161788a | -20.47945 | -53.67591 | 2025-05-26 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e763d893-b2b2-3964-8035-a00193d39c1f | -20.60079 | -47.54942 | 2025-05-26 04:23:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a88e59b-d9a3-35c4-b761-84c022f3707a | -18.6872 | -47.38961 | 2025-05-26 04:23:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2c8a8db-0d25-3143-9ffc-ff9e3e9f22b3 | -20.61099 | -48.86927 | 2025-05-26 04:23:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 11256cbe-453d-3e11-9a08-6253e33b2949 | -19.88114 | -54.36797 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f47477b6-bd5f-3039-9cb9-b379642e1259 | -23.98648 | -48.91825 | 2025-05-26 04:23:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25aa3139-c7a8-3d63-9a90-e8319c6fe5e7 | -20.61159 | -48.86556 | 2025-05-26 04:23:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 046006ec-9bec-3264-9134-30f760bf2392 | -19.71329 | -54.61759 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a38d1156-1775-3932-bff7-7038e0e9327d | -21.84864 | -50.55851 | 2025-05-26 04:23:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7cd9cbab-aef8-3767-a580-af46a078866c | -19.87683 | -54.36709 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5d361b38-3d38-3b83-add2-3a48dbf55e05 | -20.28079 | -50.74897 | 2025-05-26 04:23:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3003cb55-6aa5-3667-a146-d38c40b5b955 | -18.54859 | -44.88729 | 2025-05-26 04:23:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05d54dfc-1751-3b5f-9417-f2b94a7c050f | -19.64643 | -47.16664 | 2025-05-26 04:23:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85a1d495-976c-3439-aa3a-d3a46af21851 | -23.33829 | -46.77337 | 2025-05-26 04:23:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e831e1bd-5a22-3fdb-b09a-e3295da0cac4 | -19.87913 | -54.36892 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f87d6cd-5ced-3244-8fc7-ea5c45f9f09a | -20.60353 | -47.55368 | 2025-05-26 04:23:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c953795-d3b9-3b9f-b708-472028fc64f4 | -21.27735 | -48.61924 | 2025-05-26 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 219ca204-bc01-3737-85a2-29e6592795c6 | -22.53975 | -48.81457 | 2025-05-26 04:23:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ade697-204d-311d-96ab-21edc206d8e9 | -19.87998 | -54.36445 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 070808a3-8a24-3ccd-a6c5-dcf7fabacbef | -21.85275 | -50.55515 | 2025-05-26 04:23:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1487cb0c-1881-3c5d-b7ac-ed373e8f09da | -19.87772 | -54.36263 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ac3baaf5-e8d7-3801-83c8-7a9fda327f3d | -22.34215 | -41.78441 | 2025-05-26 04:23:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f236a59c-be38-3550-a120-388a4e1b1fb8 | -22.85271 | -47.62222 | 2025-05-26 04:23:00 | NOAA-21 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db9c6616-c855-3ffc-964b-78480b34bd5e | -20.93929 | -56.59643 | 2025-05-26 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b38771d-8a29-3607-a9b6-5389ffb1de31 | -22.78846 | -43.75583 | 2025-05-26 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
