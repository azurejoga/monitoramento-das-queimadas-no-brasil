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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca9b3b9-338b-3e99-bb4d-ab1be85b17f0 | -5.1648 | -44.3727 | 2024-12-12 01:20:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fd7a6f6b-b896-3804-8dd3-2b330aa7bc7a | -18.046 | -52.9798 | 2024-12-12 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b946ae9f-4f23-3985-9c6b-94ed14a587b0 | -3.2671 | -51.5345 | 2024-12-12 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| dd87702e-d4ef-3c1c-9d7e-3c6639eac343 | -3.2316 | -46.8936 | 2024-12-12 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bf2194c8-b643-3a01-9b25-339a28871a58 | -6.9156 | -43.5418 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| e9e766f3-8184-3ca5-aaa5-ee8c66836c95 | -18.0261 | -52.9829 | 2024-12-12 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 37af6237-d786-3b3a-a7eb-3bdbeed8edac | -5.9369 | -48.0654 | 2024-12-12 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e78705ea-edcd-342b-bafc-a5a93135cbe8 | -6.9349 | -43.4934 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 5bcc51fd-c247-3a5c-9b89-afa431e47675 | -6.9161 | -43.4952 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| a8307d5c-8edf-3527-8b62-d2ef4a26ff5c | -6.9346 | -43.5168 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 478.4 |
| 79967341-0a33-3f49-b91d-d1cb225b6822 | -15.0867 | -59.6288 | 2024-12-12 01:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9cfbc395-2628-346a-8364-9500a9ff48f1 | -5.9371 | -48.0437 | 2024-12-12 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| c700ffd6-4ed7-3f94-98c3-dc4f4230a92b | -11.1959 | -53.8348 | 2024-12-12 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 89276290-e9c6-35c2-97c1-5a34042a23d0 | -18.0469 | -52.9366 | 2024-12-12 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ded3859d-26cf-3798-a7b9-08bdf2e46c6c | -14.7461 | -52.6471 | 2024-12-12 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c2d2b87d-df98-311c-8273-afc2918d4a7b | -14.7465 | -52.6259 | 2024-12-12 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a254efb5-efd6-348b-814f-9a482d7795d0 | -6.9158 | -43.5185 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 526.3 |
| 882b1caf-e176-3395-b4d4-1d623f577f42 | -13.6933 | -54.7555 | 2024-12-12 01:20:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6aa48501-a008-3343-9c08-be56c1f2aeff | -6.9344 | -43.5401 | 2024-12-12 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 19357638-70b5-3cd7-9ddc-3e54ac87d8c3 | -18.0663 | -52.955 | 2024-12-12 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 71739e7a-5638-3025-af71-3a369c1327e9 | -1.8788 | -54.6908 | 2024-12-12 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d499b652-845f-38ea-8528-ac87aa8766c6 | -3.2503 | -46.8709 | 2024-12-12 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| acc7e2e6-793e-389b-bd54-b99a0fc901c1 | -5.9183 | -48.0667 | 2024-12-12 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a8baf19a-ef02-393f-ace7-228ee349bf09 | -3.2502 | -46.8929 | 2024-12-12 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 13c1e570-5bb0-3e77-8003-e4cfaa5f224a | -5.9185 | -48.0449 | 2024-12-12 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ee6e3057-94b7-3f60-a3b0-3a38b02e6a97 | -11.2148 | -53.833 | 2024-12-12 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 20693268-07d0-3f4f-b49a-b027c08bcb45 | -3.2317 | -46.8716 | 2024-12-12 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fa475d40-3d3c-3a69-9028-aa9929c30f9b | -14.7655 | -52.6446 | 2024-12-12 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b778d643-54dc-3f7f-a2de-ff4b588b876e | -18.0464 | -52.9582 | 2024-12-12 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 0db8f471-1a5a-3237-bb1a-4f694e42a3fb | -14.7457 | -52.6683 | 2024-12-12 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 1ab00dfe-5b5c-3e4e-9f38-273b2159d28f | -5.9369 | -48.0654 | 2024-12-12 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8d6a9914-82ad-323b-8159-f2f4969f10dd | -15.0865 | -59.6487 | 2024-12-12 01:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ed1fb939-7407-3ac1-9f4f-dbe6876216ce | -1.8788 | -54.6709 | 2024-12-12 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6e49ada8-be9b-38c9-9c4a-72f225123931 | -11.1959 | -53.8348 | 2024-12-12 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 289048cb-5de9-3eb1-92b1-65b0a213dc16 | -14.7655 | -52.6446 | 2024-12-12 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 53409970-09b3-38d0-870d-cd2216fc6a40 | -3.2503 | -46.8709 | 2024-12-12 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 3e525abf-4d47-3e46-9ff5-cc75a56f7a19 | -11.2148 | -53.833 | 2024-12-12 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 37000585-3e87-3509-9a8b-66549e014b9a | -5.9185 | -48.0449 | 2024-12-12 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6f862e25-2840-37ec-9017-351aee9cac9a | -6.9156 | -43.5418 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| fb522c34-0d72-3bb1-a650-cade1f7bce14 | -6.9346 | -43.5168 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 506.6 |
| 6dc2fa8c-355a-3859-ade3-209fb3eaa116 | -6.9349 | -43.4934 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 8e552013-b5cc-3829-9f71-bd1b366370c4 | -5.9373 | -48.022 | 2024-12-12 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a78c53b4-6904-382b-bdde-2ef2ea65bcce | -3.2502 | -46.8929 | 2024-12-12 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4a20fe6d-16c0-3bd2-abd7-a9f716d498c2 | -6.9161 | -43.4952 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 181e41ad-1107-378e-a275-46a53e6d7f9f | -6.9158 | -43.5185 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 479.2 |
| 054a3969-d346-3422-bb10-0ede99c8ec87 | -15.0867 | -59.6288 | 2024-12-12 01:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 77bde42b-8948-3207-81e0-5f0746320a28 | -1.8788 | -54.6908 | 2024-12-12 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c0062148-1002-3984-b58b-e8943d5de0d5 | -14.7465 | -52.6259 | 2024-12-12 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1d423a14-4039-3340-b83f-023f1558e879 | -6.9344 | -43.5401 | 2024-12-12 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| f223d690-499f-3784-987c-e0f1970ae949 | -18.0464 | -52.9582 | 2024-12-12 01:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| d06ee6e2-7b1d-3dff-b2d1-44daa8a8fb95 | -5.9371 | -48.0437 | 2024-12-12 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 8ea67838-8ecd-3a11-87e4-c6475a804b62 | -14.7461 | -52.6471 | 2024-12-12 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 6ac741d9-e0d4-36db-bc91-3a97222b89de | -3.2502 | -46.8929 | 2024-12-12 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 71fb33e5-6e4a-3777-9109-4bc74121f6b7 | -14.7655 | -52.6446 | 2024-12-12 01:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bbfdcf59-28ae-3797-b40c-597dd8687672 | -5.1648 | -44.3727 | 2024-12-12 01:40:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 45197c9b-8670-3565-83f3-ca1be61ee772 | -11.2148 | -53.833 | 2024-12-12 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 267dd1a5-7eec-3aa8-b38b-4e379de339c0 | -18.046 | -52.9798 | 2024-12-12 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 53592109-7f29-3544-b2c6-2b1980f5b1d8 | -5.9369 | -48.0654 | 2024-12-12 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ca29825d-5f0e-39a3-8664-a35ced2e3ef7 | -1.8788 | -54.6709 | 2024-12-12 01:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 243a8731-1394-341b-9749-cbf84143bc08 | -14.7457 | -52.6683 | 2024-12-12 01:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4a892f69-0a25-3df8-9749-d30449675098 | -3.2503 | -46.8709 | 2024-12-12 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 432dcd49-d435-3fd6-b3f0-9c58dbf88d54 | -3.2316 | -46.8936 | 2024-12-12 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 62e28288-ee58-3e52-8a60-b7bd99d75106 | -1.8788 | -54.6908 | 2024-12-12 01:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 508e6737-3179-332f-a975-07ab168fcc46 | -18.0663 | -52.955 | 2024-12-12 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 274c15e7-882e-3184-bdbc-db7c252bea31 | -1.8604 | -54.6911 | 2024-12-12 01:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 06b8bb28-e227-38ae-90d6-0bf206edb79e | -5.9185 | -48.0449 | 2024-12-12 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3a75110a-69b5-33d8-ae62-13ac7f5bbae8 | -18.0659 | -52.9766 | 2024-12-12 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3fd6eb25-8d45-3c77-a9c9-a975b1d2c904 | -18.0464 | -52.9582 | 2024-12-12 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 8dcd84bb-09f6-39a3-8dc6-b7d321132c72 | -11.1959 | -53.8348 | 2024-12-12 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 83cdf903-d349-35c5-8bfc-7da380f97e99 | -14.7461 | -52.6471 | 2024-12-12 01:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| af439c3c-ee34-30cd-ad5f-7090e68e9e02 | -15.0867 | -59.6288 | 2024-12-12 01:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3ca2a73b-3605-3ea4-87e7-a58bdf3c76ce | -5.9371 | -48.0437 | 2024-12-12 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 205.8 |
| d233fd92-44bb-368b-8396-7f7b77e5464a | -18.0261 | -52.9829 | 2024-12-12 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| da220bc7-46c1-384d-ab7a-cf7e61446f7b | -3.2317 | -46.8716 | 2024-12-12 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| aad1b733-2d5d-3fbe-a3ff-03796ae95444 | -15.0865 | -59.6487 | 2024-12-12 01:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fbb1bdcb-93cd-3f2b-9b80-efa3e3c0e005 | -15.0867 | -59.6288 | 2024-12-12 01:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 064612b9-7536-3248-8c39-c4cdb9989d41 | -5.9369 | -48.0654 | 2024-12-12 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| aa732b05-e298-3e4b-b8a6-7c5867411fa4 | -5.9185 | -48.0449 | 2024-12-12 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 827a23d9-c0d7-32f3-8f11-e51f20bee46d | -5.9183 | -48.0667 | 2024-12-12 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ade85664-86f9-3e69-8e88-5dff462d5691 | -5.1648 | -44.3727 | 2024-12-12 01:50:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0154bd52-03f3-34ad-8b91-2adceb37ca3f | -14.7457 | -52.6683 | 2024-12-12 01:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c93debec-3f87-357b-b0ca-697cd444465b | -6.9156 | -43.5418 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| cc880aaf-02bd-3f31-9aa6-cfeeb7d3537b | -6.9161 | -43.4952 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 469a7f16-e829-3e54-b7bb-9e4ef226be5e | -14.7655 | -52.6446 | 2024-12-12 01:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f673df22-e208-34d2-9aa4-f9515780fc24 | -3.2502 | -46.8929 | 2024-12-12 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ac3547f8-2775-3438-a1ee-ec30a4c2f5a4 | -6.9344 | -43.5401 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| cfb7b8a4-de27-36c6-8715-521559d08bb9 | -3.2503 | -46.8709 | 2024-12-12 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 93af99d2-70be-3ed0-89f7-1e287deabb57 | -1.8788 | -54.6709 | 2024-12-12 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| adf7e730-a8e0-3531-98cd-f7897482ff24 | -1.8604 | -54.6911 | 2024-12-12 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ae8277d6-0004-3f3c-bbcf-0ff8feb19e44 | -14.7461 | -52.6471 | 2024-12-12 01:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 7e1df890-4a61-3800-a497-b69cf1539906 | -5.9371 | -48.0437 | 2024-12-12 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| b2589af0-2ef9-3daf-9365-667810573fec | -6.9346 | -43.5168 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 530.1 |
| da141832-616d-3ef8-b05d-1f96f4518d37 | -6.9158 | -43.5185 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 424.8 |
| c690f552-cb98-31cc-b94b-35e31c2244af | -3.2317 | -46.8716 | 2024-12-12 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b17eb554-05e6-30aa-91e8-49f31b2c5fa2 | -3.2316 | -46.8936 | 2024-12-12 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ffea8fea-776a-3b4b-b3af-0476ad112f44 | -1.8605 | -54.6712 | 2024-12-12 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e07d76f8-fb70-30a6-b889-a3ba014ab4ea | -11.2148 | -53.833 | 2024-12-12 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2b861897-ddb9-3273-885b-5173148e53cc | -11.1962 | -53.8142 | 2024-12-12 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4afe02fa-cc40-3824-a880-33298106aa5d | -11.1959 | -53.8348 | 2024-12-12 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 38f3dbee-53e4-302b-a1e6-0d95213a184d | -1.8788 | -54.6908 | 2024-12-12 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |


[Clique aqui para ver as próximas entradas](README8.md)
