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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b25fea99-fd84-32b9-aba7-e5b7011db2ed | -10.15049 | -48.73984 | 2025-09-07 06:12:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b8da39da-e1e6-3589-8b76-3628ae86f505 | -12.79066 | -48.01353 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c89fd575-10b3-3de6-8743-ef2261a68bc4 | -12.93507 | -54.7647 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 228.3 |
| db529d0a-d086-3a14-8a11-a902de625f97 | -12.84084 | -48.01428 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| afa6baf4-284f-3b11-b7b7-bc6e239770eb | -12.47596 | -53.85504 | 2025-09-07 06:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7834b0a6-efc8-3777-8a94-0c21af0438a0 | -10.71605 | -48.58646 | 2025-09-07 06:12:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 300b7729-5b33-3f89-babc-7ae55809e914 | -17.40669 | -49.30447 | 2025-09-07 06:12:00 | AQUA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 59e8e65e-f9a7-3895-86d2-c9c0c57652dd | -13.5458 | -48.10134 | 2025-09-07 06:12:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1bb76e85-f24a-36e1-9389-9fae7dfc3e4f | -12.19147 | -53.90351 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9c4e0093-0919-3736-be77-f81b8a7ea56b | -12.84394 | -47.99094 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4a320b69-f5b6-37b8-8ac3-bfaa942d98b5 | -15.17268 | -47.97535 | 2025-09-07 06:12:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c35c71ca-eec7-31a8-bee3-5367628fd328 | -11.10607 | -52.01715 | 2025-09-07 06:12:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0b0bfc71-7d5a-3761-88bd-88fc7cac14ec | -13.82132 | -46.26387 | 2025-09-07 06:12:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 45797b73-8fdb-39bb-89f3-5acdc44fe524 | -11.15575 | -48.38559 | 2025-09-07 06:12:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8dd479c5-5564-3629-b13e-3b1e35037aad | -17.39493 | -49.31548 | 2025-09-07 06:12:00 | AQUA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d1cee554-6392-36ee-93cc-1389644b54aa | -15.69434 | -53.56252 | 2025-09-07 06:12:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 80708d4f-f4cc-32fe-8c72-eea25d46bb09 | -10.58151 | -48.47092 | 2025-09-07 06:12:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1376c831-ba78-3403-9491-4f105a14321b | -13.93959 | -54.01906 | 2025-09-07 06:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7757374-13c8-36db-b224-d68fe89611f2 | -12.93331 | -54.77574 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| a08224de-a152-368b-96e7-20174d345f34 | -15.69146 | -53.58107 | 2025-09-07 06:12:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49309d00-e1f6-34a2-a5a1-c638bc6efd7e | -12.94928 | -54.76136 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b4066f6-54b5-3ca9-abb2-4df0b0b8ac97 | -13.83347 | -46.26465 | 2025-09-07 06:12:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b7b9ec9e-b902-332d-9323-60d7a831d407 | -15.1745 | -47.96129 | 2025-09-07 06:12:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f8344b07-13eb-3bcc-b165-e698e58a504e | -13.81928 | -46.28029 | 2025-09-07 06:12:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 34ab9497-84a9-3393-a766-ce2116673f5c | -12.92537 | -54.76312 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 53d9d6ec-e050-3815-b4fc-3d37c8164d64 | -13.90281 | -54.01307 | 2025-09-07 06:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7f3b09c1-2f5f-3cf5-92ef-bbbc6e7316a4 | -11.21237 | -55.00407 | 2025-09-07 06:12:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 75a5e93a-eccf-3fb6-8f42-98d50fc071e1 | -13.9044 | -54.00313 | 2025-09-07 06:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 042cb89c-660f-3034-8c64-415746d72ff7 | -10.79752 | -47.71742 | 2025-09-07 06:12:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6db139d2-57d6-3163-b605-442652733840 | -11.00024 | -52.04937 | 2025-09-07 06:12:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 657c55df-5ef7-3455-8f02-6c748f5211ba | -15.09858 | -50.10329 | 2025-09-07 06:12:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8833dff4-17b4-3b32-acce-548d6f58bcac | -16.33416 | -52.94771 | 2025-09-07 06:12:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c7cbd0a0-6cf1-36b4-8887-c908738e66a2 | -11.0904 | -52.06066 | 2025-09-07 06:12:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 54cc5496-5adf-3285-9a73-640a94219d1a | -15.69578 | -53.55325 | 2025-09-07 06:12:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6a74e5b0-364f-3ab3-9345-a91b4afc27da | -12.8113 | -48.01676 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8a30dfe9-0f36-3715-8175-0caa4b76f96e | -11.04921 | -54.1675 | 2025-09-07 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1c09fe41-092f-3cce-816f-9601f0c68de8 | -14.58673 | -48.08114 | 2025-09-07 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 778e7ee1-fea7-3a73-9ed3-e8207a864130 | -13.90911 | -53.97364 | 2025-09-07 06:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6743e359-a810-3e9c-b8f1-8767adddd32e | -12.82314 | -48.00718 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4521e788-80a5-3ff1-8db2-df326760151d | -10.46027 | -53.61176 | 2025-09-07 06:12:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9bbde758-8838-32fc-a91e-da5b718a05e3 | -12.80263 | -48.00306 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3a9d3ad2-5a71-3bb6-b697-5bb3d7420eed | -14.477 | -48.76004 | 2025-09-07 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bf59fc51-cb2f-3f93-9d15-eb2cc18d05a3 | -16.32673 | -52.93721 | 2025-09-07 06:12:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d2d6948b-b183-33c6-a5fb-5081496020af | -11.21044 | -55.01609 | 2025-09-07 06:12:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 76e2a062-cda4-3b1d-8eb1-e037787d1ebd | -14.49707 | -48.76329 | 2025-09-07 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4b80c7eb-a67e-3c5c-a0c0-4f9d100cb086 | -12.93779 | -54.77074 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 75d675b2-f4e5-3366-8b63-98bd298408f4 | -15.72769 | -53.53547 | 2025-09-07 06:12:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2eabcd2d-b8f8-3c32-bc69-e4d97913b2d5 | -15.83647 | -52.27282 | 2025-09-07 06:12:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 29afc8be-6233-316a-a47d-a716ddc920a5 | -11.14587 | -48.38454 | 2025-09-07 06:12:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 199d68aa-0a96-3a55-a78d-b7bee64f4fdd | -11.03962 | -54.16589 | 2025-09-07 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c6a4b881-63ae-399a-a4b9-286106cc995d | -11.1047 | -52.02612 | 2025-09-07 06:12:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fa63560d-f4cf-3489-82e9-23daa31bb7ee | -12.93959 | -54.75977 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 7877b7d6-efb4-3032-b26f-fdf10f81def2 | -14.82001 | -48.19353 | 2025-09-07 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86d1693f-18c6-3882-b845-797a5e2a89a4 | -14.82173 | -48.18068 | 2025-09-07 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c252545f-d9e5-3241-a66d-4a860bab597a | -20.00575 | -48.89983 | 2025-09-07 06:14:00 | AQUA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 0c9a605b-29fa-3862-8d51-b10d25da428e | -19.86169 | -57.87919 | 2025-09-07 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 277777fd-4ffa-38c6-a7d3-a7d47b460f5a | -12.948 | -54.7724 | 2025-09-07 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 88ac0e9f-4af8-3017-af67-3fef115f7b02 | -12.6191 | -44.5882 | 2025-09-07 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2b0b8e01-a526-3610-b053-3aed15ad105c | -12.8248 | -48.0155 | 2025-09-07 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0f434761-b8bc-3155-b292-0506ed821ee2 | -12.7153 | -56.5632 | 2025-09-07 06:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| b994b3c7-65ba-3033-802a-f7c69d1e5da1 | -12.8055 | -48.0182 | 2025-09-07 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 3a3127ff-eee2-3104-ac5c-229d2a4c9a13 | -12.9482 | -54.7519 | 2025-09-07 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 281bb162-de02-3872-90fd-ffa38eaaf720 | -12.6186 | -44.6116 | 2025-09-07 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 74e4f263-c440-3c3c-afa8-0b42f5f107ee | -12.9477 | -54.793 | 2025-09-07 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| efd657f0-743d-3df5-a298-fd5c6cefb06c | -12.8059 | -47.9959 | 2025-09-07 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 741ba053-5a9d-3521-9451-eef93e2c5ae8 | -12.9289 | -54.7744 | 2025-09-07 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 4fac4997-68ce-34d7-a1e3-8581fee58313 | -12.9292 | -54.7538 | 2025-09-07 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 51deaf88-f017-333d-aa1f-ba4abc14f87c | -12.6186 | -44.6116 | 2025-09-07 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 73f844a2-85cb-3869-ad3e-b4b95afa6dfb | -12.8059 | -47.9959 | 2025-09-07 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3806f264-e5de-38ac-a787-4d03730eee13 | -12.8055 | -48.0182 | 2025-09-07 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d786a2d3-8e20-358e-9674-b06ca0ec5314 | -12.948 | -54.7724 | 2025-09-07 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 4c55fe30-2ad9-3274-9d92-4ffcae9dbb57 | -12.7153 | -56.5632 | 2025-09-07 06:30:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 25fee23b-977d-3149-842c-d85571b78e55 | -12.9289 | -54.7744 | 2025-09-07 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| c4610e09-9267-3b85-b1a9-928d59b712ed | -13.8407 | -46.2598 | 2025-09-07 06:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0a8cd8f8-8e76-38da-b2c5-9cc66bffbe56 | -12.6191 | -44.5882 | 2025-09-07 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| dedbc92c-48c1-3b48-a1e0-2ab897d399a8 | -12.9482 | -54.7519 | 2025-09-07 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 18c43daf-bddf-322b-bd19-8d80bc25d245 | -12.948 | -54.7724 | 2025-09-07 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 181.2 |
| f799095a-f15f-374c-aa10-59606c3378e9 | -14.8609 | -46.681 | 2025-09-07 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 13ead598-279b-37ff-9622-10ef9d93e4db | -14.8414 | -46.6844 | 2025-09-07 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f31543c1-9c00-3cee-b0fa-f9bf7df258cd | -12.9477 | -54.793 | 2025-09-07 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 82f77951-93ce-371a-8195-e038e8eb388a | -14.8604 | -46.7039 | 2025-09-07 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6907c9ca-b018-3a99-9c3e-7813ca8fc1c8 | -12.9482 | -54.7519 | 2025-09-07 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4529bde0-d81a-387b-a9e6-dd5199e84a5e | -12.8055 | -48.0182 | 2025-09-07 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 8ad057d5-2057-34b5-b848-29426d2ae745 | -13.8407 | -46.2598 | 2025-09-07 06:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c7f34152-1dc8-3825-8619-34aba4747d2b | -12.8059 | -47.9959 | 2025-09-07 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| eaecf487-72e5-3e53-88e9-b481f863f142 | -12.9289 | -54.7744 | 2025-09-07 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 122f626b-7cab-3eb8-9064-a4d9f6719915 | -20.0049 | -48.9172 | 2025-09-07 06:40:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| df7142b7-3d61-3e41-9407-c795db24e2a1 | -12.7153 | -56.5632 | 2025-09-07 06:40:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| e9cbf444-9180-371c-b3d2-393149ceb5d0 | -12.8248 | -48.0155 | 2025-09-07 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ed07f6c7-fe8b-305c-8313-1d2e853b7dfd | -20.0055 | -48.8942 | 2025-09-07 06:40:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e1031789-7e1f-3b57-8b1a-6a0adcbcbbdf | -12.9289 | -54.7744 | 2025-09-07 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| df2cc90f-4b13-3762-9635-24f221a52959 | -12.8055 | -48.0182 | 2025-09-07 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cb1a95be-d242-3310-b7de-03d6ca525e42 | -12.9482 | -54.7519 | 2025-09-07 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 722604a1-9f20-3b3d-999e-9de84a7efa4c | -12.948 | -54.7724 | 2025-09-07 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 08380842-3b7e-32c0-a3b7-f093dda8c908 | -12.8059 | -47.9959 | 2025-09-07 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| babce47c-19a7-3947-b260-cdff48214e4a | -12.8059 | -47.9959 | 2025-09-07 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9594bc4b-9e7d-388e-9227-fd77510ab700 | -13.8407 | -46.2598 | 2025-09-07 07:00:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 84e224b0-0669-3331-b549-fbdc401ea645 | -12.9482 | -54.7519 | 2025-09-07 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| ef65bb66-38ac-3ac8-8709-3c8817a243d9 | -12.948 | -54.7724 | 2025-09-07 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 216.6 |
| d7f15c94-c62a-36ae-8787-8f1fc4150ac6 | -12.9289 | -54.7744 | 2025-09-07 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |


[Clique aqui para ver as próximas entradas](README83.md)
