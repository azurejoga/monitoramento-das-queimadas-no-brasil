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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76fef45e-4a32-3214-b729-189b9c493954 | -6.1853 | -43.3257 | 2025-08-30 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ee7ecabc-8205-3a9a-936a-667305489779 | -6.1663 | -43.3506 | 2025-08-30 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3b34c6ad-9b13-3197-b2fd-064d5d3012e5 | -11.8952 | -46.398 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| e3f3d179-d889-39a9-aad0-8f37f74e73a6 | -10.678 | -48.7289 | 2025-08-30 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3ee25668-5807-3285-8845-aed69ea88a4f | -11.8752 | -46.446 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| cada8809-1b18-3227-87a9-ddb80891b681 | -13.3628 | -46.9953 | 2025-08-30 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 70a46b14-d7bf-3187-bd8b-a8ae5f733e75 | -6.185 | -43.3491 | 2025-08-30 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| ddc1f913-c5a0-3b73-b765-58c6b13ac59f | -11.3312 | -43.6399 | 2025-08-30 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 608262a4-26ab-35a0-9538-e0b84a7ecded | -11.8952 | -46.398 | 2025-08-30 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| a4fc5bf0-0506-312a-99cb-5be1342d5204 | -13.3632 | -46.9727 | 2025-08-30 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 4e2b1572-510c-3854-9611-2cfba2137f2a | -6.1663 | -43.3506 | 2025-08-30 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d389770c-87f4-307f-8df1-92bb1c158c9e | -13.3456 | -46.885 | 2025-08-30 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2085327c-191c-3c2c-8bb1-3cef7be1e987 | -13.3817 | -47.015 | 2025-08-30 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4365a614-64db-3710-b1e8-f93711114e64 | -11.1523 | -54.3104 | 2025-08-30 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4005a203-b53a-3398-aa74-6dcbeec1686f | -11.876 | -46.4007 | 2025-08-30 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| a77ddfa8-5d34-371d-a9dc-d33491242934 | -11.8764 | -46.378 | 2025-08-30 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 350.6 |
| aa5fd2c4-d62a-31d2-8919-20a02ef26915 | -6.1853 | -43.3257 | 2025-08-30 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 7924da6c-9f6a-3b8d-bb19-2c60bb7525a8 | -11.3317 | -43.6162 | 2025-08-30 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 221c70b8-e5f9-3bd4-8809-ceb9ae544d1f | -10.659 | -48.7311 | 2025-08-30 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 9f265e44-35a3-35ab-a7c7-45a30862b450 | -6.1665 | -43.3273 | 2025-08-30 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 96d3c5aa-8493-3f97-9af0-a7c9ebffca19 | -5.8884 | -42.9753 | 2025-08-30 11:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| b0dd0829-42de-3024-a9d2-f160039fdacd | -9.6986 | -47.0555 | 2025-08-30 11:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| f66e5944-5164-359f-bf5c-9dcfd3f251a4 | -10.678 | -48.7289 | 2025-08-30 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1bcd2b36-879a-314e-a93b-eeffe0d554c6 | -11.1523 | -54.3104 | 2025-08-30 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| cd7cd3aa-83a8-3974-838b-abbca2323879 | -6.1853 | -43.3257 | 2025-08-30 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 3ce0ae0e-2e05-3880-8c43-ccb11da40c65 | -11.3312 | -43.6399 | 2025-08-30 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| faf2084b-6a97-39c2-9da4-8d5d902b5066 | -6.1663 | -43.3506 | 2025-08-30 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b54787fa-48b5-3e94-b3b0-4960639a1e8c | -6.1665 | -43.3273 | 2025-08-30 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 59e0eb60-a69a-379a-a7a8-f7aabd043c57 | -6.185 | -43.3491 | 2025-08-30 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 889e38f2-dff9-3600-8f03-d19dbad6b52a | -10.659 | -48.7311 | 2025-08-30 11:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 32ee8cbc-9889-3c7e-9110-5d1dda8d0910 | -11.8952 | -46.398 | 2025-08-30 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1a7500ea-2a66-3026-a6f5-09ed082c258e | -11.8764 | -46.378 | 2025-08-30 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 259.2 |
| b8d4cb1d-9627-3897-bf16-0d47503cfaed | -13.3632 | -46.9727 | 2025-08-30 11:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4ba63d1f-8906-3d29-ba22-8608735c287d | -13.3456 | -46.885 | 2025-08-30 11:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| cb12fa32-613a-3a07-aa67-54e49c22948e | -6.1787 | -43.9995 | 2025-08-30 11:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 784cd804-7da2-3100-932e-8da33ed81f67 | -11.3317 | -43.6162 | 2025-08-30 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 2de7a1d1-98e4-359f-9e5a-5718110ec75f | -6.1665 | -43.3273 | 2025-08-30 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 9e1974e7-67d5-37f3-8572-5dbf56af425f | -11.3317 | -43.6162 | 2025-08-30 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| c822dc60-ab36-3a6f-a57d-f6eea56fa515 | -13.3619 | -47.0406 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f899885e-4fd1-33cb-a876-80dbb923d319 | -7.8541 | -46.9747 | 2025-08-30 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 8e402647-3602-3ab1-8a0e-02a53a0bf1b0 | -6.1853 | -43.3257 | 2025-08-30 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 9997e7ae-91ea-37e5-9cc5-51785319075c | -13.3623 | -47.018 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| afd46319-16bd-366c-a828-0112bc944de3 | -13.3456 | -46.885 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| df1faab0-88b6-3d17-b3d2-e42fdb2c0e61 | -13.3812 | -47.0377 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 51801008-0ef8-3809-97ca-9342e60f102f | -11.8764 | -46.378 | 2025-08-30 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 457.1 |
| 1ee37849-20f3-35d0-b639-3ca1571f6013 | -11.3312 | -43.6399 | 2025-08-30 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 84636f52-2678-342c-ad0f-fad612af4c2d | -11.876 | -46.4007 | 2025-08-30 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c03605c3-1f24-3666-8f4e-727e42a712db | -6.1663 | -43.3506 | 2025-08-30 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 7f124ede-b293-3498-aba6-6bc5cb1d5f58 | -6.185 | -43.3491 | 2025-08-30 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c79c4804-12ab-36d5-bda8-cf7a974328f3 | -6.1787 | -43.9995 | 2025-08-30 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e0dda60e-f9ee-32a9-9404-2ad87445a1e5 | -13.3817 | -47.015 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7f04f7e0-80ba-3fc3-825e-937bf9e4c0d5 | -13.3649 | -46.882 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| e2c10bac-558e-367e-8ce7-9e326200d06d | -11.1523 | -54.3104 | 2025-08-30 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 6232dec6-891d-3445-8ef1-1747e980e164 | -13.3645 | -46.9047 | 2025-08-30 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 247cda93-3ee0-3fe9-9783-d662e0d31fa2 | -11.8952 | -46.398 | 2025-08-30 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 62dbe8f7-d5a4-30df-afb7-8360ad6ac9bd | -6.1663 | -43.3506 | 2025-08-30 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 9a7bbc3e-220a-30bf-af03-68edc873703a | -11.1523 | -54.3104 | 2025-08-30 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d3df07a2-3bb9-3ab3-86e7-62a9a264bc3e | -6.1853 | -43.3257 | 2025-08-30 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 253.0 |
| c519e55e-a42d-3ecc-8bf2-158bd452a432 | -13.3817 | -47.015 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 38d19811-2f1e-391b-b311-177d189499e9 | -7.8541 | -46.9747 | 2025-08-30 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 3c9df256-d25c-3569-8cc1-afbec4761f12 | -13.3812 | -47.0377 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 958036fc-154a-3202-9df6-82233f9c7a89 | -13.3645 | -46.9047 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 138.8 |
| fdcd4d26-1849-35f9-ac24-d7f7f8a82c1d | -6.1787 | -43.9995 | 2025-08-30 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1d91bff5-7173-3d5a-9683-0ee673ce48fe | -11.3312 | -43.6399 | 2025-08-30 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 5145f2da-d7b0-36ba-8e4c-37ff7205c679 | -12.6686 | -48.1704 | 2025-08-30 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 1a4210f3-e774-3f80-984a-69b087b50f38 | -14.0118 | -44.5614 | 2025-08-30 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f32004e2-f38c-3109-981f-122fd1d5f310 | -11.3317 | -43.6162 | 2025-08-30 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 3c68cf5c-fd5e-385a-866f-5d59fd799004 | -13.3456 | -46.885 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 9048f844-e58b-3a9d-b956-4cd0c0566fa8 | -11.8764 | -46.378 | 2025-08-30 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 483.8 |
| afee626a-a813-33fc-9191-df06e57c814c | -6.1665 | -43.3273 | 2025-08-30 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 258.0 |
| f689cf18-dbdd-3a20-84b6-65a0fbe30e83 | -6.185 | -43.3491 | 2025-08-30 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 390352bd-2c1b-3921-8470-28689841fa28 | -6.7814 | -43.7865 | 2025-08-30 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7da4f365-80ce-3214-8e34-a3ef69cc03e4 | -13.3619 | -47.0406 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cd87949c-dc01-3ba7-96d5-08d76710cc1b | -11.876 | -46.4007 | 2025-08-30 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 3d24037d-bc07-36d5-98f7-fd9cbd30bb20 | -13.3649 | -46.882 | 2025-08-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 334a86ad-c923-3e98-84d2-120ba9a78c74 | -7.10811 | -44.57704 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 29b13853-70b9-393f-ba5b-23da6fb40820 | -7.3248 | -44.0803 | 2025-08-30 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e8d32b01-4905-34ab-951e-640139ac22d4 | -7.78426 | -45.46591 | 2025-08-30 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 20eda796-9ab5-369f-93bf-e1672ec66b73 | -9.6679 | -45.96156 | 2025-08-30 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 905058a4-01a0-383c-a526-11f7fc06acec | -6.18857 | -43.32233 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a1a11ea2-3e6b-3afe-ad48-f5e565002d9c | -7.96475 | -46.38728 | 2025-08-30 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04c29304-69da-3fb0-acea-98d22e660172 | -7.63108 | -42.65787 | 2025-08-30 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0675783d-4570-3cb9-9587-53a8286850be | -9.55976 | -42.04866 | 2025-08-30 12:14:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| b78b0a92-0488-3ccf-ad63-b3e3ed87b487 | -4.58551 | -43.3147 | 2025-08-30 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| de377ca0-4fb8-3ff3-a6c4-ca9abc1a1b3b | -2.95566 | -42.86312 | 2025-08-30 12:14:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 12d9184e-2824-3aed-9f56-8fc286dede31 | -6.42041 | -47.85954 | 2025-08-30 12:14:00 | TERRA_M-T | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 088e69e5-d3c4-3225-ad44-cfd2a66204ff | -8.88053 | -45.07822 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a092c403-921f-3352-8006-fbbbb9411d92 | -6.30469 | -43.53626 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 605cc60b-6961-388c-a3e6-9dcb6a6ab82a | -6.95153 | -44.31484 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 295ce773-1474-37d3-8cd5-5cb19652b891 | -6.13179 | -43.31471 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 0e4828f5-0ea2-341f-b075-ef5c3678d126 | -6.17911 | -43.32103 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d059c5e8-9e29-32ff-bffd-aae1086c5719 | -8.86105 | -45.73716 | 2025-08-30 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28049d2f-fa29-34bd-8200-0c1153887f35 | -7.42488 | -44.81438 | 2025-08-30 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 100b7ebb-5dac-3165-a4f8-9da4ccfe3f5b | -5.99014 | -43.35578 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1f38ee77-84dc-38d6-b92e-6f68acc45b27 | -7.805 | -44.73255 | 2025-08-30 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b1422d51-3938-307f-a8fe-17d965fb7329 | -6.13557 | -43.95425 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 965799c0-66e7-3b34-bfe2-6dd122074583 | -7.12221 | -44.60724 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5fe2d662-737f-3a7b-9d4a-28f6206094e8 | -7.06428 | -44.36551 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9b7d9f1a-7a19-3877-ac83-6a1dd1ebddcf | -7.72492 | -50.27698 | 2025-08-30 12:14:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 494b83ff-b6fe-3dc5-84df-42247b17a5ba | -6.60338 | -43.90204 | 2025-08-30 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README94.md)
