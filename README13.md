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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13ec9239-3956-3861-bbd1-e687c6546c00 | -12.7746 | -44.5162 | 2026-06-19 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 7c007b7d-ad9a-3a9a-991c-aefc0b2d73fa | -12.7939 | -44.513 | 2026-06-19 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 37ef555a-e813-37b1-b167-eb799260979d | -10.06502 | -48.08833 | 2026-06-19 12:10:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6f4356be-fd8f-3605-a83a-208751c15c6e | -10.78173 | -53.57259 | 2026-06-19 12:10:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0f996ce4-f207-3954-ae24-5c1eafec67ea | -10.7971 | -53.59423 | 2026-06-19 12:10:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cae6cc20-7871-32da-936f-55fb3282bb8a | -9.74643 | -47.87924 | 2026-06-19 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 70671979-ef12-396f-94ba-d30352d749d1 | -10.90837 | -46.33628 | 2026-06-19 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f5fe198c-27cd-3734-ad07-e5d270a62ad5 | -10.25411 | -47.34645 | 2026-06-19 12:10:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c673089b-2d99-3067-82b3-6c2364bfa425 | -8.48292 | -51.53941 | 2026-06-19 12:10:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e28a4f6c-e6fe-36cd-8bdc-aa5341286621 | -11.06194 | -52.48416 | 2026-06-19 12:10:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08b88c2e-e710-3ae4-9f64-cdeb7a18db0e | -10.05467 | -48.08707 | 2026-06-19 12:10:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 99040e09-853d-30e6-a6b5-122bb343ed6e | -8.4754 | -51.52935 | 2026-06-19 12:10:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 2ad660b3-a0b8-3a16-a961-72e86f9ca4d6 | -11.93553 | -43.40961 | 2026-06-19 12:10:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 3e9f231e-a258-34d7-94e2-ff2285e67709 | -10.55428 | -46.33801 | 2026-06-19 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 46ffa3bb-41be-3c84-b7be-1fbf44e430c9 | -10.54198 | -47.70466 | 2026-06-19 12:10:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3c7b424f-069d-3d44-90c5-272806a83531 | -11.9315 | -43.41628 | 2026-06-19 12:10:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| cf073837-d28c-3131-8412-9bda789c5bcb | -10.05303 | -48.09957 | 2026-06-19 12:10:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 75b13c0d-063d-3f13-9b9e-c1276a91cf45 | -11.93482 | -43.38519 | 2026-06-19 12:10:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| bd1649f2-2872-37f5-932b-9dda81708cc4 | -10.76692 | -54.10397 | 2026-06-19 12:10:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7634b914-0bad-3e74-aeae-1b210468d4b9 | -10.76658 | -51.63829 | 2026-06-19 12:10:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 77fb8512-e29f-36de-98b2-dfc0d9606810 | -10.47307 | -49.0913 | 2026-06-19 12:10:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb7d0edc-fea1-3297-995f-0ea5d8d38abc | -10.75296 | -50.21429 | 2026-06-19 12:10:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f654ac0-7650-3d00-b36a-72ba0f963b0e | -8.47413 | -51.53817 | 2026-06-19 12:10:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e1372d07-7647-3bad-ba0a-caf8091af125 | -9.74814 | -47.86652 | 2026-06-19 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3baf1aba-1e0c-32bc-a57b-d7cad691c8b1 | -10.55641 | -46.32097 | 2026-06-19 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0f266f1f-5313-388e-befe-3219e84f1e57 | -8.48419 | -51.53059 | 2026-06-19 12:10:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 29a00485-34c8-3107-bbef-5507bd09c83a | -9.75388 | -47.87375 | 2026-06-19 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| edce0eff-f985-3057-a264-4dd825ef08ad | -11.06583 | -52.45734 | 2026-06-19 12:10:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da6dc283-60c3-355c-9083-65c4001266e9 | -18.17522 | -51.49616 | 2026-06-19 12:12:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a613cdbd-1616-300f-aa3c-a09cbdb7e5f9 | -12.79826 | -44.50535 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 307.0 |
| e8988505-bb23-3a0d-8f38-38a4e8cf2602 | -12.87347 | -44.3526 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a5d39419-5e14-3841-8239-37ff9800ed56 | -12.54826 | -57.19746 | 2026-06-19 12:12:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 45151f77-fa52-3cd8-b664-6e5f6db1b214 | -13.94034 | -53.5617 | 2026-06-19 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1e810a8d-9544-34f0-b474-ff7f712e6995 | -12.87048 | -44.37957 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b6a108c9-7d18-388c-83db-14d4ffd5b7ea | -12.781 | -44.49836 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 7da51e3f-58a7-39b6-9877-e4957a30a69a | -12.66448 | -47.68592 | 2026-06-19 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e3688c47-bcaa-3efc-8eaa-57eb2d6ece00 | -14.06972 | -44.48069 | 2026-06-19 12:12:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 86a2e19a-f056-3350-af25-cd2f352c97f7 | -14.20501 | -54.70507 | 2026-06-19 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5390bcd-4c3c-377c-8bca-a8315daaf628 | -12.79539 | -44.49991 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 594.2 |
| 1a958d39-23c9-365d-8567-3a66a7b1566a | -12.79837 | -44.47371 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 4037e5ff-05b5-3dad-9c80-79173ab2810e | -18.97708 | -52.44484 | 2026-06-19 12:12:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 921f635e-e28b-340c-a323-18dbda627c42 | -12.13324 | -48.26318 | 2026-06-19 12:12:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d0465272-34e4-37f4-b220-636eb49f9aef | -12.43096 | -48.7254 | 2026-06-19 12:12:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2732c3ab-b6d7-3a6f-a353-e8f4eba9298f | -14.0551 | -44.47866 | 2026-06-19 12:12:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 569e53f0-eb96-34c9-a799-892cf4741cf7 | -13.3293 | -45.15715 | 2026-06-19 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 3b07f044-d90f-3a1d-9e29-3af7776d7270 | -12.6663 | -47.67126 | 2026-06-19 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| e9218830-9a82-3cce-ad5a-5c41ddb1c8cf | -12.54833 | -57.20348 | 2026-06-19 12:12:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 674c3d2c-a580-399f-9b57-15395cca7504 | -12.3532 | -47.4254 | 2026-06-19 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b2835304-a598-32fd-8172-fdbca9b6f366 | -18.97575 | -52.45457 | 2026-06-19 12:12:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 302cf6a0-25d2-3f6f-b48f-2731cbd9457e | -13.56099 | -43.57604 | 2026-06-19 12:12:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c4ec26c0-b6ca-3a0d-8fa2-2273be5afe65 | -13.31551 | -45.15586 | 2026-06-19 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 310.5 |
| af01756a-bda5-37d5-8b6a-692dfcde8989 | -12.80106 | -44.47916 | 2026-06-19 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 2ad09bdb-ea6a-3f6b-b9e0-4b7e178794d2 | -11.52061 | -54.25774 | 2026-06-19 12:12:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 47270042-96f4-3d44-bac9-94f4e7cc814f | -10.562 | -46.3266 | 2026-06-19 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 2d99cda0-bd06-3b24-b56f-65d4879da3d6 | -13.3217 | -45.1479 | 2026-06-19 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| c06fb6b6-5a77-3ef7-8d3a-d85a227ae63a | -10.543 | -46.329 | 2026-06-19 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 96d7b546-1358-3c88-8a26-5cac12eb5300 | -12.7746 | -44.5162 | 2026-06-19 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 02d2571a-4ac7-3702-949c-a33b4f2ed707 | -12.7939 | -44.513 | 2026-06-19 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 6f539f19-3cc3-356d-bebf-18aaec691e35 | -12.7939 | -44.513 | 2026-06-19 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 2c95ca2b-9a24-3882-86d7-4d5b9f2ee546 | -10.562 | -46.3266 | 2026-06-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1abf85d2-76c6-3206-9d6e-1b19a692cf66 | -10.543 | -46.329 | 2026-06-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b76e26ab-e761-3c72-aa6a-d9f3fe7e2f6a | -13.3217 | -45.1479 | 2026-06-19 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| ba7595b6-42ee-3617-b897-ecc62a8cf7b2 | -12.7746 | -44.5162 | 2026-06-19 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 872f9e74-1975-3150-a30a-846c21efd336 | -13.3217 | -45.1479 | 2026-06-19 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a7ccb3c3-53f0-3164-b728-ebeb97de1b29 | -12.7939 | -44.513 | 2026-06-19 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 6084c10f-7630-35db-b256-77d7727504d9 | -12.7746 | -44.5162 | 2026-06-19 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 994f93ab-4335-3b1b-bc8b-5480fba4e990 | -10.562 | -46.3266 | 2026-06-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3a549cb2-d437-3f00-ad4d-0311e5b341bd | -12.7939 | -44.513 | 2026-06-19 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| edcf0cf9-9339-3c9b-b360-14e3c7d5f5b3 | -10.543 | -46.329 | 2026-06-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e78207f3-64f8-343c-a67b-d5ca8c985cf3 | -12.7746 | -44.5162 | 2026-06-19 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 95865dff-f016-3489-b104-039efc2bccda | -12.7939 | -44.513 | 2026-06-19 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| c6b4c181-44f6-3baf-a7db-00888237b7b1 | -12.7746 | -44.5162 | 2026-06-19 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 3665e7ed-8b37-3817-8cea-29f4a4a1f3ef | -12.7746 | -44.5162 | 2026-06-19 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 00f76d60-b947-37dd-8225-5f57b450b7a8 | -12.7939 | -44.513 | 2026-06-19 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 303.6 |
| 89e6cc38-eb45-3ace-9a5a-78ba9d6ec16f | -12.7746 | -44.5162 | 2026-06-19 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 789daf28-7089-3a12-975e-6722bb72a091 | -12.7939 | -44.513 | 2026-06-19 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 5fdd7a9e-ed2a-3ffb-b292-3bd1f87af414 | -12.7746 | -44.5162 | 2026-06-19 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 365eaf60-8e17-3865-858b-dfdd0a517cb2 | -12.8741 | -44.3593 | 2026-06-19 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 35f567e1-df2b-3f4e-9a4e-d00d3055ac09 | -12.7939 | -44.513 | 2026-06-19 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 338.2 |
| 3c61e4de-0c2f-36dd-b045-9e5dcbbdda9a | -12.7939 | -44.513 | 2026-06-19 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 513d4d15-0ed3-3e69-93e8-411c86da6f43 | -12.8741 | -44.3593 | 2026-06-19 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 193c5815-5a78-391c-8822-6a4dfda83156 | -12.7746 | -44.5162 | 2026-06-19 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 55ca503f-41ad-3ed3-afab-96e734e23cb9 | -12.7746 | -44.5162 | 2026-06-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| e64d3c6e-35f6-3641-9f09-4b4ea474e567 | -12.7939 | -44.513 | 2026-06-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 3deb5959-7bc8-392b-a51b-ffbd23e4c836 | -12.7944 | -44.4895 | 2026-06-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 650.3 |
| 5966affe-54a6-3f54-934c-f98064a86407 | -12.7949 | -44.4661 | 2026-06-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 7d066c95-c9d5-3529-bf72-b199bb4017b9 | -12.7944 | -44.4895 | 2026-06-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 607.8 |
| 67707cfb-410d-382e-b63b-32cd641336e8 | -12.7746 | -44.5162 | 2026-06-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 042f7d04-3f28-3fae-96d8-fa18f3bd51b7 | -12.7949 | -44.4661 | 2026-06-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 04a0d429-386b-3d63-9b7a-8ac51d27f5d6 | -12.7939 | -44.513 | 2026-06-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 0917a50b-d44a-3a5b-baf9-16b065032aad | -12.7949 | -44.4661 | 2026-06-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a5f65ffb-b748-3186-9b00-116c62e0780e | -12.7939 | -44.513 | 2026-06-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 7661cb6f-ab15-3bd5-9366-5a2d7ca3b42c | -12.8741 | -44.3593 | 2026-06-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 51dbc80b-6173-3954-b8d9-79acec555ddd | -12.7746 | -44.5162 | 2026-06-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0d20d221-94c6-386b-9036-cb79bb00190d | -12.7944 | -44.4895 | 2026-06-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 656.9 |
| b19b1992-2a3d-3b68-8f11-1d3b49658b06 | -12.7939 | -44.513 | 2026-06-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 7833458d-d040-3452-81f7-777e780783bb | -10.2432 | -47.3491 | 2026-06-19 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| c3c81a18-eede-3103-97aa-fffff1320605 | -12.7949 | -44.4661 | 2026-06-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 9815c17b-0df0-3da6-bca0-160d9f770d73 | -12.7746 | -44.5162 | 2026-06-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 83f80377-6bed-35c8-9548-9603efe511d2 | -12.7944 | -44.4895 | 2026-06-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 785.5 |


[Clique aqui para ver as próximas entradas](README14.md)
