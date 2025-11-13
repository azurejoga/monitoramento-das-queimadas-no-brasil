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
| aba8e8e1-01e5-34fa-aa13-f47b3a5d3519 | -1.70262 | -54.67482 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f01fd57-9aca-3aa9-a148-2996ef21a236 | -3.26202 | -50.03052 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d40868d0-1b7e-338a-a769-e199c9805eaa | -3.3982 | -50.1804 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1baef108-00ad-3cde-9753-9ec5ff1277d4 | -2.45429 | -49.26274 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19151d74-43b0-3735-88cd-29b3730d5a84 | -1.35572 | -55.45244 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3151cc4-66d7-3557-aef7-f58ca47935a2 | -3.39275 | -50.27139 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 991ad4fc-d500-3518-81f8-eb5269df6ad8 | -1.74431 | -55.63811 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e86704ec-ddab-3a9c-838e-d1c752b3b4cd | -2.03252 | -47.04415 | 2025-11-13 05:01:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1b5482-420a-37a3-9d6e-5c33ec6501ca | 1.46475 | -55.84198 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e3ee7bf-464f-3c7b-9072-3177abee1966 | 1.45909 | -55.85035 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b185d94-308a-3d30-aa65-52d036c58a07 | -2.31536 | -48.45139 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56641703-e50e-39e4-b21a-09ca3073a663 | 0.79534 | -50.86652 | 2025-11-13 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 769cc89e-14b0-3eff-ba9a-d8176d299808 | -2.63808 | -49.21896 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bbb3a4c-e8df-395d-97aa-d4146cce1071 | -3.16246 | -50.62662 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea8022d9-3c71-36b7-9201-7630e1e0ae71 | -3.14061 | -50.27519 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae096b6-15f9-3cf5-bc62-c630f0db2554 | -3.76872 | -47.72681 | 2025-11-13 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edcb29f7-e75e-315e-9541-d4cd9962c248 | -1.67832 | -54.22773 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79a821aa-75c7-399c-bb16-f03d2cd33174 | -2.31469 | -48.45574 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be132bc2-350a-3e51-be5c-08246313a596 | -3.15306 | -45.81536 | 2025-11-13 05:01:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5d568e7-a640-33e9-8426-49b1bc0aa631 | -2.52152 | -47.81146 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250006ad-441f-3716-8e56-b47b35a1567e | -3.15858 | -50.62603 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb708149-c8b3-33ed-98cd-503858e56cc1 | -2.63144 | -49.20593 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c75240e5-71de-386d-b3ba-5250b621fd32 | -3.15316 | -50.2633 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd0b409e-2d18-373f-b899-0f3ea4b970f0 | -2.1692 | -48.37358 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0c7d70-d366-32ff-94b8-422051b79434 | -2.86552 | -53.80614 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03db707e-3446-3897-a8e5-380eda96de65 | -2.86374 | -51.47477 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e48f4edd-53a9-3f60-a4af-f12ace16c9ad | -3.08788 | -49.27552 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 537e309e-c92f-33b6-bdd0-15b2ad6619e6 | -1.83224 | -53.81126 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b4aff69-bfde-3d1f-80ef-ca69a5c7d8e0 | -2.86959 | -51.48242 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c0a454a-4c06-3e7c-925d-391fc98e0d64 | -3.22533 | -45.59543 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48d497e3-d902-30b8-9002-c1b00d9b23d1 | -2.33438 | -55.73095 | 2025-11-13 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 959a3c19-1b00-37a1-9052-72421eca6c28 | -3.7689 | -47.72863 | 2025-11-13 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 068dabaa-c604-3b7b-9a83-909af37f5115 | -3.08304 | -49.2788 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d78aa7e6-eeff-3c83-9f52-53e638af878f | -3.40325 | -50.17403 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ee4069a-4d1c-3043-a741-10e59f091134 | -2.63285 | -47.30547 | 2025-11-13 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4de5be31-0f59-345a-b422-3937ed914a7d | -3.33934 | -48.37989 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f36a8e6d-0316-3c80-93d8-e8e98475127a | -3.1541 | -50.2668 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c32c10fc-e9a0-36ff-ad71-ca48109f397f | -1.41412 | -55.3199 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7b181e9-233d-32fb-9d66-90b6653ff88a | -3.03815 | -51.03263 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14a28ef0-b974-3712-a0be-b02bb1346885 | -3.0891 | -49.26766 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6720411e-8267-3789-b89d-c2c4045db103 | 1.45967 | -55.85401 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f82ea57-cda4-3cc3-95f8-b573665a9a10 | -2.29124 | -47.87543 | 2025-11-13 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79bf1a28-5140-31bb-981d-10b2591fe31f | -2.52618 | -47.81207 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59065bc3-9039-32d6-9535-4b33fffd0bfc | -0.88484 | -52.06169 | 2025-11-13 05:01:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7d11c5-ae02-3ba3-b419-15bbb12129d7 | -2.86723 | -51.47319 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 444a8c92-dfe3-39f5-8ec1-1cecceff05da | -3.2264 | -45.59349 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6cea38e9-cd30-387c-8552-c3cde9c83c50 | -3.23621 | -50.03733 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b9bbde-458c-3549-b865-c4c910b4687f | -1.35849 | -55.45644 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e27f5e16-d1cb-3803-832c-4af6f9da5c18 | -2.46225 | -55.43837 | 2025-11-13 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ae6e2220-a855-3f77-a404-bff14309ddb7 | -2.87177 | -51.47156 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0e611baa-c19c-3e11-9d59-4281a4c8cf7c | -1.41743 | -55.32042 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d80bfddb-5343-309e-a547-6a00d3b90c9e | -2.44952 | -49.26594 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f7f6c38-c381-3046-9fa4-8904d554c8d5 | -2.6338 | -47.30337 | 2025-11-13 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb13c8f7-f32e-3fbb-a7ae-171376ca1e8b | -1.90682 | -54.56603 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4beffdb9-d2e6-32fa-bb11-05916deb070e | -2.15195 | -52.76246 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19e0210c-8650-3059-92d2-6fbf917cbdec | -2.45067 | -49.25825 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0c13281-b1cf-35aa-9e38-d958b738d872 | -2.7204 | -47.40907 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654be697-4d4f-38e1-9b63-7b43903f56a3 | -1.81004 | -53.80067 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 519c6da4-8d36-35a6-b33e-3790dc17084f | -3.14538 | -50.27066 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5311ac7-8952-3ad1-854b-94134a35e1a3 | -3.0915 | -49.28009 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56f5787c-5cac-37ca-96e3-737a52663996 | -3.78066 | -42.75964 | 2025-11-13 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bb4072a-1385-3f9a-8b4f-d3488621eb80 | -1.42503 | -55.7032 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf6236f0-3efa-37d1-98c2-d15d2d0d298c | -2.45894 | -55.43784 | 2025-11-13 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 702452bc-a46e-3c15-ad59-a371c9f0d8f3 | -2.45354 | -49.2634 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09abb888-60d1-391b-9735-81bd740a483b | -2.63204 | -49.20204 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c9cc4fa-1132-365b-94b6-8e2bd3b6e2b3 | -2.87458 | -51.47434 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2607bc58-3880-3ce4-9249-33b879669bb2 | 1.4659 | -55.8493 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7ff91d5-ad9f-32f9-9428-2d9e9dacff56 | -2.37102 | -55.8009 | 2025-11-13 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbbfc083-2165-3808-b74f-c955794a8485 | -3.21189 | -50.19755 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5addef7-0340-31f9-a661-49124047604a | -2.86741 | -51.47532 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2dfdd758-59ba-3dbe-a928-fd8932aac7dc | -3.34767 | -48.38585 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b657bf5-cdb8-3904-8d5d-d66988b5c3e7 | -2.15538 | -52.76301 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47d06f9-9371-3792-9b02-b5daf965ae29 | -2.37444 | -49.41475 | 2025-11-13 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25da80f6-2b11-3876-b803-44bbeb4832c3 | -3.09273 | -49.27223 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 818527e8-6744-3b97-a7a1-df51dc6fc353 | -2.7199 | -47.41066 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e29e403-c2d2-37f2-b0e3-f093a40f8b36 | -3.34244 | -48.38974 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fef7762a-582e-3947-b307-e712b5e460c0 | -1.77485 | -55.98146 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b658456e-e5df-361e-8540-b48f2952d346 | -1.35904 | -55.45297 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 170f088d-634f-39ee-9bb0-f867eb4db35d | 1.02354 | -52.06679 | 2025-11-13 05:01:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e14b42-3ce3-3721-8112-5f3283cb74ca | -1.37442 | -55.39848 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db0db7e-bf1a-30be-afa5-36fa349d6e67 | -1.81227 | -53.80817 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44c60b63-b664-3283-bc42-53c683401d8b | 3.30608 | -60.12949 | 2025-11-13 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40638bb2-3c6f-34b6-93c9-a9eaac46a676 | -2.893 | -48.08051 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d841692-c5c9-3268-8454-0e0a2a579ac1 | -3.09089 | -49.284 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb90bfe2-4293-3895-a604-b11aecc7f110 | -3.14934 | -50.27127 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35935680-804f-3aad-a3fc-36b5d3c319b3 | -3.09561 | -49.27974 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6556aade-1dc2-34aa-bd34-dce855a16c38 | -3.09079 | -49.28302 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca35c19f-7f41-33e9-819d-0a552714852f | -3.7815 | -42.75381 | 2025-11-13 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c7bc344-2662-3752-8044-6332528c0cc1 | -2.72677 | -49.58055 | 2025-11-13 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b697f3d7-1893-3449-98ae-03b202a62934 | -1.76412 | -54.13506 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 499b0cc6-d608-329f-8107-777d83119772 | -3.45949 | -43.18393 | 2025-11-13 05:01:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30162e04-f667-3b8d-8dd2-15aabb30707b | -2.43363 | -48.61998 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba89a05-3862-370e-ba3b-f0ef8e9e3ee3 | -3.41741 | -49.99602 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96448111-391d-3d73-a7e8-0f3369f36b1d | -2.63021 | -52.08288 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301c2393-1ce2-37a4-923d-c9be3eacf0a6 | -3.40521 | -50.26978 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fd7c63e-56da-35a7-8cba-c69d0960a6aa | -3.12454 | -46.04012 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d1f63e-d72b-3d25-bba4-4ef36014f2b3 | -2.97075 | -51.04338 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c69d726-dccb-3967-a12b-a311e32d220a | -2.45294 | -49.26723 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e930ed4-28c4-3a8e-b926-0971ce0f5623 | -3.08365 | -49.27487 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34d529bf-ccb5-3c72-802a-7da856b9fd9d | -3.09635 | -49.2768 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)
