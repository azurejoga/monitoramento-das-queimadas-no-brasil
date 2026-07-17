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
| c9f90674-b746-3945-9e8e-012de743f998 | -6.01116 | -46.32178 | 2026-07-17 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b403eeb1-7a8c-3308-b229-56dc0b4cce2e | -12.03993 | -40.6742 | 2026-07-17 04:02:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3f1d206f-bb22-3281-aa55-83d531e82a3e | -7.91727 | -48.2579 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bff8f9fe-d52a-3dfc-8b44-07da5ce04e4b | -6.49935 | -42.21137 | 2026-07-17 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6ef3ed1e-602c-329a-9ba7-a32e8730651f | -10.03895 | -51.66239 | 2026-07-17 04:02:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a644d35c-baf6-391e-b4e9-ff1ee029f719 | -9.19433 | -43.1447 | 2026-07-17 04:02:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83bff8b9-8227-3cc3-9a86-94375b648d0b | -4.65789 | -42.42365 | 2026-07-17 04:02:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b106451-fc87-385c-8000-5dde798d5fee | -8.76437 | -43.93887 | 2026-07-17 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7653b007-7fe7-3dcd-b338-78c12bb60d22 | -9.47547 | -40.30525 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 185c9d62-74bc-3974-81ff-a65a674c3af8 | -9.95403 | -50.55543 | 2026-07-17 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65309a2e-0615-312d-bc3c-e8d8d2527e25 | -5.91414 | -46.67185 | 2026-07-17 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0e1afae-92aa-34d1-b495-316e67fa37db | -10.83755 | -46.57497 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55b582d9-04ee-3f19-8c73-e2ac51afe320 | -9.47823 | -40.30925 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 1bed5cb5-d541-39ae-8ef4-07108627ab4a | -9.85726 | -40.29794 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2f938cb-d28b-3ba2-9ee8-6db97df048d6 | -9.69586 | -47.69186 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65ab6f91-8b4a-3393-b570-9d0cd3541e24 | -9.47217 | -40.30473 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 347f62c4-1ae2-3e3f-b18a-eaff566162f8 | -10.84769 | -46.46986 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a6d440-a0d5-38ea-8fa5-a1ffd9f557d0 | -10.82177 | -47.39743 | 2026-07-17 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c42e3b7f-4ebe-3348-8e22-0413c45950f8 | -5.80313 | -43.63695 | 2026-07-17 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00bea8b8-45b5-34be-9b11-f514d250b8af | -8.76365 | -43.94231 | 2026-07-17 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebefff2c-c6d8-3457-a735-3538f95d23bc | -5.60772 | -36.86845 | 2026-07-17 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1b1e48f3-0bf8-3155-ae32-b45ee994712d | -10.04404 | -51.66777 | 2026-07-17 04:02:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd059dab-370f-3184-8a13-3dee605f43be | -7.73366 | -44.56047 | 2026-07-17 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcb04ecc-1c4c-3814-ad62-79443d435511 | -9.57094 | -48.67059 | 2026-07-17 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f62941de-8b3f-39f4-8c5c-5fc8ab4e7040 | -10.86495 | -46.49278 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30b89ab7-948e-3b4d-bd60-2007687b4ff4 | -10.86156 | -46.51199 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cca1675-c2bc-3721-aa7f-1c880278c4cb | -10.81857 | -45.12969 | 2026-07-17 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b0e4723d-2a39-3725-8bba-9ff8b9e84f20 | -9.95953 | -50.55651 | 2026-07-17 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da4c0ca3-539f-36b8-be6b-fbbdefb7d470 | -7.9635 | -49.64785 | 2026-07-17 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad400c75-4e80-3d2a-aa51-79ac71be0526 | -8.50796 | -48.07378 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a01f39b8-bdd8-3493-9d58-797ff5f9b2f4 | -7.90958 | -48.26051 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f08aab66-a56f-3b81-90ca-86ee50e1279a | -7.69028 | -50.60002 | 2026-07-17 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c675d885-6826-38fb-ad8d-70e5258b1533 | -10.81776 | -45.13448 | 2026-07-17 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0df806c0-efad-3cfd-9c22-3b5842005d1a | -5.89876 | -46.21048 | 2026-07-17 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 798cf358-37e7-3808-b363-d425a0e1f9e6 | -10.82254 | -46.52918 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6519f683-9d26-3453-9b78-fcfd8216f17f | -8.51183 | -48.07979 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8a91c7e-5be3-328e-a020-088c1037bd0f | -10.47733 | -49.14379 | 2026-07-17 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5b2d10b-0754-3dc2-8aff-baa8ba48bfd0 | -10.82603 | -46.53378 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76926cb2-8a35-3f6d-92ae-94df9857b93f | -9.56604 | -48.6697 | 2026-07-17 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd2479cc-a76a-3ebd-abac-94b0d4bb496e | -7.91546 | -48.25567 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c97ffeb7-9ea0-3fe7-97ea-4f5681ea3974 | -10.86359 | -46.50047 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7494010-e5c8-37c9-b815-17ac0058fcc2 | -9.51726 | -47.14151 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8b122a2a-2bd2-3837-a1ee-dc1055342769 | -7.96887 | -49.64889 | 2026-07-17 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0356c0dc-5821-3ba9-a22d-8f79134476c0 | -7.29306 | -46.25274 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b571f19-09c7-3d2e-b1ca-bc734819b7fe | -19.1807 | -47.35086 | 2026-07-17 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11c4bd3f-c18d-3f5c-a4be-e327137f6015 | -12.6973 | -46.51026 | 2026-07-17 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81a54449-451b-311e-be24-c8b21199bd41 | -13.28212 | -45.19809 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d5c5903-0abc-37ae-b509-5bc9cc9fd202 | -13.38028 | -43.67818 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7293a95-692a-3b2c-9792-34de3aeca641 | -16.52336 | -47.73244 | 2026-07-17 04:04:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 224f0515-2bd3-32c3-aba9-ed5c0dcdf164 | -14.72996 | -47.14467 | 2026-07-17 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41c0c1a3-a1fa-3089-a520-2a8dc2f75704 | -12.45846 | -49.58706 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25aa3737-40c4-3bed-9a64-05a780e4f451 | -13.4391 | -43.85491 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 43a0d6c7-6fba-38b3-9f07-ebd624dcac59 | -13.56437 | -47.80912 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a27dc73-1b9c-3d8c-9dcf-2aa2ce9ba0bd | -17.59422 | -44.60023 | 2026-07-17 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa64b87d-7de1-3b95-ba5c-d1eee059571c | -12.89265 | -42.45728 | 2026-07-17 04:04:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32ce2f86-fb43-383f-8975-c9504ab94329 | -13.536 | -47.75738 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f1cc184-8038-345e-9d18-6ee51d972ccb | -15.65687 | -43.32161 | 2026-07-17 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85ca304e-f907-3753-976c-c1e006019ddb | -14.88968 | -48.47239 | 2026-07-17 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a62843e2-eca5-3239-97bb-d494a7545177 | -18.42477 | -43.72262 | 2026-07-17 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ca83ebd-ea38-33e6-9a57-25fbf79a4dc0 | -13.54616 | -47.78715 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 891e47fd-d20e-31de-91ae-106ff5ef723b | -12.45243 | -49.59175 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 157939d6-2277-3ece-a6f2-a68ded315d9b | -12.12265 | -49.94026 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8ef20ee-a93a-3468-aef3-3cfc0b2d2ce6 | -13.44194 | -43.85933 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e8c51005-5a7f-31df-a726-5bfa3b8d95bb | -13.50389 | -44.27807 | 2026-07-17 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43c75a36-ebbc-3437-8954-b564597c3619 | -12.50471 | -46.34476 | 2026-07-17 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f09b32d1-c2f5-3f41-96da-3f01476e5b9e | -19.17983 | -47.35575 | 2026-07-17 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0dc57270-ce27-321c-b54b-3887bd150c02 | -18.42084 | -43.72575 | 2026-07-17 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d90d9c9-4ac2-308d-b48c-62265c86049e | -14.14624 | -46.26776 | 2026-07-17 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d179a84-23db-3d2f-a2a8-6c6101cae957 | -11.78637 | -47.09295 | 2026-07-17 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbbafacd-6a2a-3701-a442-88bf5a9473cb | -13.25472 | -45.11504 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 459a7d8a-eac9-3672-91c7-94e05ada0816 | -13.4413 | -43.8632 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb79f6fa-8c54-379a-a73b-7bd449b122ca | -17.59443 | -44.60104 | 2026-07-17 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37297be5-966f-3942-9e2d-bcdc8c76c1d1 | -13.56937 | -47.80613 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ef2f86b-be7a-3217-9931-ba0dfa3b13c6 | -13.49747 | -47.65206 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 150e6248-6195-3cf5-bb6b-4b33dc3c08f1 | -13.64277 | -45.54578 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b5345e0-a78e-3c4f-be48-b2cdf808ff80 | -12.45206 | -49.58862 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bda0a6eb-c411-35bb-9260-b65627238c0e | -18.42145 | -43.722 | 2026-07-17 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ff8426b-6ee1-3115-8718-ce2d475b53a8 | -13.56589 | -47.80087 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c80bbbf4-d0fb-33b0-82b4-afdbd25d7353 | -13.53526 | -47.76151 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d7c0324-d36a-39f8-9fe4-04eec69190f1 | -13.56163 | -47.79981 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d8d57c4-6ceb-3685-b946-2245cef48649 | -12.45312 | -49.58287 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 961c5561-1f0c-3eb3-ae4c-5dd69ce52e1c | -13.54509 | -43.61493 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17fcd397-b486-3b54-beb1-d10989003320 | -12.45737 | -49.59277 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efec06ff-8973-3a53-bff7-d989aec1b537 | -18.57486 | -40.34419 | 2026-07-17 04:04:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 659ec857-a133-3045-ac0a-c5918686fce0 | -12.68396 | -48.21047 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b979a79-8075-37ba-938f-287faef0e606 | -12.88931 | -42.45672 | 2026-07-17 04:04:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 05d979c2-11d4-3e3d-b897-3d0b12200df4 | -12.44087 | -49.57191 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a69d0ad4-6c76-3f8a-9c5e-f10266b32e64 | -13.61199 | -46.15474 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 568671c3-d66b-35be-8fee-516d558e2f5f | -13.25169 | -45.11551 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8a3acc4-6806-3930-bbf9-8c5d2d121559 | -17.82259 | -41.59268 | 2026-07-17 04:04:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f670bb3c-83ba-3316-be57-933b4dffca20 | -13.43846 | -43.85882 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fb695766-a623-3ef3-81df-ec021904bdca | -12.44427 | -49.57534 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38cd8fbf-47d1-32f9-942e-26ad0d1e3a0c | -12.43977 | -49.57765 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fad2c4c-996d-3a6f-908b-d340c6c55d89 | -16.14725 | -43.63375 | 2026-07-17 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1403f5af-5df1-3486-96bf-54987a71ad41 | -13.25104 | -45.11441 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2875e392-fd38-338e-8a70-71c016d9ed20 | -13.43975 | -43.851 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37e47bc2-c41c-33f5-92bd-430142acec40 | -13.54966 | -47.79228 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33e8967-17db-3150-b356-897eba95fe78 | -18.03797 | -44.42685 | 2026-07-17 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1f2ec45c-fc7a-3caf-9e5e-229efb8608ca | -13.6126 | -46.15707 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c163691-69aa-33d5-834d-d5ae9342175f | -17.00514 | -48.28529 | 2026-07-17 04:04:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README6.md)
