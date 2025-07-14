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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ae05c0a-a285-33a7-add9-ecbb097ef90d | -13.65248 | -46.81093 | 2025-07-14 04:29:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e8fd0ec-2171-30e0-892d-e953c9e3632e | -13.10261 | -47.3047 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27ccf20f-f97d-38f9-9f08-413438a40929 | -13.12533 | -47.26826 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b3d21f5-591f-3876-b8bd-41f4ed9f4f53 | -13.03596 | -47.81676 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 633c60aa-a284-35ba-911a-11245aae858c | -13.1481 | -47.31923 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c55d0c3e-dc3f-3e27-8d9c-d7d6472367d1 | -14.50126 | -58.59825 | 2025-07-14 04:29:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0efcc6-485e-3d77-94fe-87e6746dde4f | -13.03928 | -47.81731 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42ee59b1-1819-34ff-878b-9fdc1f361275 | -13.03872 | -47.82085 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f049aa9e-d321-347e-9be7-e9eb1e627fa8 | -13.14755 | -47.32277 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 884abe1c-f12e-3c7f-a745-ff446d6c0d3b | -13.02326 | -47.81103 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0a78b30-4cb5-3394-ba7a-da7791f3ee81 | -13.03376 | -47.80914 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edddc422-fda8-35c6-b042-d86bfb93ba1d | -11.86952 | -58.7081 | 2025-07-14 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e3fc03c-6f98-3a0b-9f6a-4d0a4beb376e | -13.10316 | -47.30116 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c2cc9c6-2c47-3f1d-802e-69e8872406fa | -13.02214 | -47.8181 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a45841ba-17da-360e-b873-4f1aaa2f09b2 | -13.18691 | -47.26724 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75825b2c-1fa4-3c87-8e3c-5460c21ef1ed | -16.28184 | -49.96487 | 2025-07-14 04:29:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fd43a79-0c0b-37da-8dcb-f4ea71c7d71c | -11.86352 | -58.70692 | 2025-07-14 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b224c255-1c01-3288-b5cc-5f1c100d019f | -13.18636 | -47.27079 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79fd0083-d9e5-3474-a02f-ca58c455db9e | -13.03043 | -47.80859 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0af08a6-692c-3745-8d4d-74307572cd06 | -16.68005 | -43.88253 | 2025-07-14 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f53e68-d082-357e-bc58-b5fbb475bd97 | -13.12477 | -47.27183 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006ac3e8-ad01-3ae2-905f-74f1952d4669 | -13.14477 | -47.31872 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 728739e4-8dd5-3183-afc2-62b172aa0826 | -13.84869 | -46.89737 | 2025-07-14 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d0f0182-5af3-3226-8276-1536e9e1bba9 | -13.02496 | -46.64925 | 2025-07-14 04:29:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00e0f0d2-110e-3bb3-baaf-5ae92f208239 | -11.58193 | -47.32378 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb9a871a-c69b-3862-a64d-70d9dff897cf | -13.00692 | -46.31021 | 2025-07-14 04:29:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e597ba-aa68-3b03-929b-9a0e6e609cc4 | -11.71712 | -47.04249 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f47ff14-bb8f-36f8-8866-3567a53f8b5f | -11.03266 | -47.06972 | 2025-07-14 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e50b4983-d632-3cd3-9047-82d817c50dee | -11.58377 | -47.328 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7ec2d76-2d53-308d-a869-028c9219d45b | -9.46835 | -57.33182 | 2025-07-14 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d51c8230-5969-360f-a0d5-7ac07d4fd133 | -12.13201 | -45.89591 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 297e0b05-ed04-37d2-a33d-3be37e1ca406 | -12.13257 | -45.89218 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b69488bc-f5f9-379c-9346-8cc9028bae8c | -10.58002 | -49.15072 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd1f214d-1aa4-38b3-9bf0-a85fa70b38d4 | -10.57281 | -49.13025 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3ded43-c2c3-3f4b-ac64-6c3475f340d6 | -10.99227 | -47.08843 | 2025-07-14 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33aaf3b8-4ac0-341e-809c-9c132c85fde0 | -10.56938 | -49.12968 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f73844af-f137-3e0e-b2ab-b1df8a1d84e3 | -12.41596 | -47.50555 | 2025-07-14 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f431c3a3-755d-3628-9c8d-56b753ddbe92 | -12.12804 | -45.89911 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe28dfbf-5515-383e-a781-07dd0547672b | -11.031 | -47.08026 | 2025-07-14 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3be9584-2835-3e06-bcec-ea15b909f363 | -10.65762 | -49.44482 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac1ae295-ad0e-3be5-8f14-7aeb033bd001 | -11.58138 | -47.3273 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be32a496-0657-3c2b-9db9-b550b987ed14 | -10.57343 | -49.12647 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94927632-f01a-3f14-b7c3-e849766a0882 | -10.65416 | -49.44424 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5430cc91-1043-392c-b63f-fe0c95568167 | -12.10541 | -46.43513 | 2025-07-14 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44defabc-93c6-3e75-a8c2-78bfef28473e | -11.71434 | -47.01671 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98930df0-d641-34a4-92ce-6969eefdb8fb | -9.4691 | -57.32783 | 2025-07-14 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8365a7cb-3a3d-3364-930a-efdf010bff80 | -11.71879 | -47.05361 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8719413b-c3e1-3d24-9825-04b15cdd15d1 | -10.57062 | -49.12214 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c45f6f24-051b-3a5a-898f-241fde84906d | -12.12829 | -45.89594 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c7ccd60-82fc-39e3-b0e9-15e080aa49de | -11.71547 | -47.05308 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d3c88ca-5c18-39e0-b489-438488d36a82 | -13.03845 | -46.2854 | 2025-07-14 04:29:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51293d43-d92e-331c-baf0-d3738bea9c4c | -10.58064 | -49.14695 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee02a868-6e6e-3109-9591-8b67efead7fe | -10.99337 | -47.08141 | 2025-07-14 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5e6619b-342e-3138-bdc6-bb3234815de7 | -10.70112 | -48.30094 | 2025-07-14 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd52f6b7-14a3-39f9-87d9-c07d7a844421 | -11.58248 | -47.32027 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b5c321-809d-3897-8c0c-7d7050ff0872 | -13.03507 | -46.28485 | 2025-07-14 04:29:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb46bca-c2fe-3578-a08f-9fc2571ee28f | -11.71602 | -47.04955 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4df7fc4-0cb3-374b-9230-6aafff9a788d | -11.58432 | -47.32448 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40606b35-b078-35fd-8136-98bc5f1d855c | -11.59692 | -43.20876 | 2025-07-14 04:29:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13fc3810-9a37-323e-9d8b-975efb5c6e8f | -12.13145 | -45.89964 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bcc11157-0f31-3a1a-bc9d-c66fefc38af9 | -12.12771 | -45.89966 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bd71fdc-6f3a-3a4e-8a85-0a8f391a633e | -11.71768 | -47.03896 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8a708b0-045b-390c-b118-df8deaf7e04a | -12.1286 | -45.89537 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f4da282-7198-3b2a-b4db-cc60c62fe14d | -11.03155 | -47.07674 | 2025-07-14 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b1183ff-6549-3e39-a6e9-dea411ab0ee0 | -11.93923 | -45.76402 | 2025-07-14 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b6930b1-2889-3ba2-8dce-9a71068f311a | -11.70993 | -47.06665 | 2025-07-14 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d7c83f-bb30-3818-a256-58c4c2be3fb4 | -11.22865 | -46.41966 | 2025-07-14 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03faa132-dcd4-3fc6-94a6-137a40222557 | -10.57 | -49.12592 | 2025-07-14 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dc5f0b2-3a3f-3c12-b1a6-951fe5e444ce | -11.58488 | -47.32096 | 2025-07-14 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eebc1ce5-7db4-347f-bfbc-38dfb3b45c8d | -8.0451 | -50.1016 | 2025-07-14 04:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d02bc51e-a67d-3292-b151-a34df64f0e8b | -8.5022 | -43.3085 | 2025-07-14 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 2afcf002-f03c-3b2b-98d9-bf1a52273d1d | -8.5211 | -43.3063 | 2025-07-14 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3d61df0f-f92e-356a-8111-54590f15518b | -22.19909 | -41.64852 | 2025-07-14 04:32:00 | NPP-375D | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fc238d06-a7b6-3316-90da-a5a93b960fe3 | -23.08392 | -54.19006 | 2025-07-14 04:32:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ab2d323f-66e9-37de-bea4-ae9d25f58a51 | -17.92053 | -45.56639 | 2025-07-14 04:32:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba733224-1f61-38be-b670-ee9fab22f2bc | -22.67562 | -42.85877 | 2025-07-14 04:32:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ee85d556-6c31-3dcb-b6e4-bcf0b7c4a171 | -17.91034 | -54.1208 | 2025-07-14 04:32:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 095f3d5c-1722-393b-b3e8-791d3f7588e8 | -22.67617 | -42.85382 | 2025-07-14 04:32:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 01014164-fa12-3ba0-bf3c-be4779d32572 | -21.48483 | -54.26498 | 2025-07-14 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 673cf390-ac99-3ec0-a8ec-55d1c863e406 | -17.90632 | -54.12002 | 2025-07-14 04:32:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3544dd8f-55c9-3be8-9362-505b022aa5a5 | -16.72916 | -51.75919 | 2025-07-14 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f52103f7-ae1e-3ba3-8ff7-58d97f50dc7e | -18.99944 | -49.47606 | 2025-07-14 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3c9e45-2095-3e8f-94ca-e35eb93a7261 | -16.73201 | -51.76411 | 2025-07-14 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 876fbaab-2c57-3609-af9e-864cb1fb037d | -22.19972 | -41.64269 | 2025-07-14 04:32:00 | NPP-375D | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7f0edbce-6180-38e6-aa6b-e3130d891654 | -22.90216 | -43.75287 | 2025-07-14 04:32:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d97dbf53-53cb-30cb-8fda-0eccbb0f4301 | -23.98314 | -48.91887 | 2025-07-14 04:32:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edaa770b-6bff-38be-8ff2-278366e8e6cd | -20.14066 | -50.7199 | 2025-07-14 04:32:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f41ba638-fb35-3379-ba84-ff61f107e218 | -17.22601 | -49.55624 | 2025-07-14 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cdd77b6-a6ba-38b3-a95d-bf1a792a834d | -22.07529 | -43.21474 | 2025-07-14 04:32:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae53f7ad-c3a9-3d44-93ca-7fafa6a280c9 | -21.48865 | -54.26578 | 2025-07-14 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 619c7261-d8be-30c1-b504-a5157ba93b9a | -19.88545 | -42.60916 | 2025-07-14 04:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b529c581-91f9-311a-9695-c430650991b9 | -21.48389 | -54.26999 | 2025-07-14 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0902ea8-e480-37a5-9ca6-92eb188046e0 | -17.22541 | -49.5599 | 2025-07-14 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd32596d-e36f-3b29-8afe-a71a3b85a971 | -16.73275 | -51.75987 | 2025-07-14 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 713f9a4a-c988-3015-ada4-edffc728870e | -21.62027 | -43.64686 | 2025-07-14 04:32:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83850955-60da-30dc-9763-3061e5e371a7 | -20.41743 | -43.55412 | 2025-07-14 04:32:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40b0c12c-fbf8-3b44-8298-c655661bf746 | -21.79033 | -50.7892 | 2025-07-14 04:32:00 | NPP-375D | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 841943b8-3500-340c-81e4-542bb0886367 | -19.88809 | -42.608 | 2025-07-14 04:32:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23ee9c16-a07a-381f-92cb-02e28b3f2d15 | -22.4185 | -43.00715 | 2025-07-14 04:32:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 401db6c1-86d0-369f-b687-f137d12c61e3 | -21.61977 | -43.65108 | 2025-07-14 04:32:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
