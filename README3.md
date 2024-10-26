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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 011562c6-3d57-32fe-ada8-6ad802acabf5 | -17.2733 | -57.5085 | 2024-10-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| fc5019eb-b825-37a5-b289-3cb7cf9528c0 | -17.6667 | -57.4822 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| db117479-c66e-32c7-b02c-203766c7285f | -17.6861 | -57.5004 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 6dd795e3-cd0a-319f-995e-fe1a19029eaf | -17.6865 | -57.4798 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 964118e6-cccf-30d8-b355-0925243a4409 | -17.7062 | -57.4774 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| e904997f-4e54-369c-82f7-d66590c60a12 | -17.7242 | -57.5779 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 70228833-2383-36d2-a258-76b8f94eb9bc | -17.7436 | -57.5961 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 3b90dfbd-e222-34fd-821a-f79a3d1ee05a | -17.744 | -57.5756 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 14c6ad62-d5fa-3b6d-91ce-eccfeaa806b9 | -17.7443 | -57.555 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| a5f8f5e2-5b0d-39f6-938a-b5f706e443cc | -17.7671 | -57.3673 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| ac8c88e1-822f-3bb8-9cad-a8ef338b06e6 | -17.7674 | -57.3467 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 908f45b3-78ce-31d1-a064-ef391712a957 | -17.7868 | -57.3649 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.8 |
| ad8e9a02-3cd6-34ab-a27c-7b6dd05b4b1d | -17.7872 | -57.3443 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.9 |
| 9937f62c-35d0-313a-99cf-d9cf0881243d | -17.8066 | -57.3625 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 48ce9758-72b2-32c7-babe-9aad849cbd02 | -17.8069 | -57.3419 | 2024-10-26 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| d34b5e37-2f2c-3206-b649-e5d87426779b | -18.065 | -57.2481 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 23621e7b-c6f1-33f3-bebb-8dd7c4ac356f | -18.0653 | -57.2274 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| a3781a25-d06c-3681-ad93-15c6aaa9b789 | -18.0844 | -57.2663 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| fa4593ec-82d4-3c7f-b6e7-347d764e07d8 | -18.1039 | -57.2845 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 724655d5-ba93-37a1-9b6b-fe4553c276f8 | -18.1042 | -57.2638 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 7a47e515-6ae0-3207-b581-84fbb094f16a | -18.1223 | -57.3647 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 4884ef4d-3e49-33ae-b343-3792a2ca436c | -18.1417 | -57.3829 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 9467a632-28e6-3c94-8d9a-4e6a9d3746c7 | -18.1421 | -57.3622 | 2024-10-26 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 0ead8fd3-fccb-337a-a345-38f32303af8b | -19.6063 | -56.7108 | 2024-10-26 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| b3199a4d-a496-3a16-95c6-e89bffdbbc56 | -19.6067 | -56.6898 | 2024-10-26 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 155.3 |
| 2ba5f2e1-e8f5-3850-9f0a-2861d641ad44 | -19.6071 | -56.6688 | 2024-10-26 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 638381a2-8f9c-3520-b34a-5a2c9ed8bdde | -19.6268 | -56.6869 | 2024-10-26 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 5b4281cb-57d5-3b76-8370-50a348da200a | -19.6272 | -56.6659 | 2024-10-26 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| d9351128-bd9b-38e0-a539-ff8f61364d4f | -18.537001 | -41.334702 | 2024-10-26 00:30:48 | METOP-B | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80d225a2-019a-3cca-b851-d8fff85fa200 | -17.4247 | -39.937698 | 2024-10-26 00:31:00 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf204bac-cf17-3fab-9f77-4b891c57eb91 | -17.4119 | -39.928398 | 2024-10-26 00:31:01 | METOP-B | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3c11c51-4d55-37f1-87b6-c5e2d588b0c8 | -17.415001 | -39.940399 | 2024-10-26 00:31:01 | METOP-B | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 589797af-9ab8-327e-bba4-ed3809b4e3cc | -17.417999 | -39.952499 | 2024-10-26 00:31:01 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f56de8ba-4443-3f64-8e2e-e499f98279ed | -20.304001 | -55.318699 | 2024-10-26 00:31:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9fe42de-9d99-3148-8b19-da4a8518a435 | -20.307699 | -55.341702 | 2024-10-26 00:31:05 | METOP-B | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 549ba00e-24d0-3335-95e2-77168b28b99b | -17.639601 | -42.0798 | 2024-10-26 00:31:05 | METOP-B | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c0ede3f-b1d4-382b-9745-699cd67764e2 | -17.6418 | -42.088799 | 2024-10-26 00:31:05 | METOP-B | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c5a40f1-d83e-3c6c-85aa-bc4ed9ceaa2e | -20.2943 | -55.3204 | 2024-10-26 00:31:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 15518bcf-6465-348b-ba58-44caa53ed778 | -20.298 | -55.343399 | 2024-10-26 00:31:05 | METOP-B | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1908fdd4-1b6d-3187-927c-e9f3c3854876 | -19.619499 | -56.645802 | 2024-10-26 00:31:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87903256-cb42-3491-86f3-bb0a051198da | -19.6099 | -56.647499 | 2024-10-26 00:31:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08001afb-af18-3944-b88d-ae40156e1358 | -19.5809 | -56.652302 | 2024-10-26 00:31:21 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f799574a-b42c-328f-b46a-6a5d411e4233 | -19.5422 | -56.658798 | 2024-10-26 00:31:22 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cca3b48a-5ad1-3b29-a822-e5b863703a9d | -19.528299 | -56.633099 | 2024-10-26 00:31:22 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a5335b9f-6d89-3d18-8ff9-f647208afd64 | -19.5326 | -56.6605 | 2024-10-26 00:31:22 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae92b764-0f22-3cd8-a22f-c7ef05b39f59 | -19.5186 | -56.634701 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24a48591-3051-3c77-8d93-528381f9bd71 | -19.5229 | -56.662102 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 93efeeee-2f3c-3f4b-86cd-e52c7880120a | -19.490601 | -56.583698 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c98aa7b-3cd6-363a-83f9-e6b6451b70d4 | -19.4949 | -56.610802 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c8e2d05b-349f-37a3-8047-274373b5bf82 | -19.499201 | -56.6381 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c274bdd2-e785-3dad-ab2e-3e3abad69add | -19.481001 | -56.5853 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9f3c714e-55e1-3f35-b075-dbc1e4dbfacb | -19.4853 | -56.612499 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d4bd222d-2430-3f0a-b555-961e66e2e206 | -19.489599 | -56.639702 | 2024-10-26 00:31:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 429689ea-bf1d-3871-940a-db7b553bdb67 | -19.475599 | -56.614101 | 2024-10-26 00:31:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2d43c422-70b0-3eb6-8471-055426d37b0c | -16.0116 | -41.173199 | 2024-10-26 00:31:28 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6acbbbcb-4be4-3a3e-9e6c-62490b2f8adc | -16.0142 | -41.1838 | 2024-10-26 00:31:28 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd036f80-5278-3305-8608-af12a064ad26 | -16.040001 | -43.715698 | 2024-10-26 00:31:37 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 36ea4f33-5337-3262-9528-c20e33715ca1 | -15.825 | -43.591202 | 2024-10-26 00:31:40 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66ecb326-c154-3c13-baec-e2d385158666 | -15.8269 | -43.5993 | 2024-10-26 00:31:40 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9fa2bee1-8939-383d-90cb-95e9c25e3efb | -15.6075 | -43.721699 | 2024-10-26 00:31:44 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1b118970-3b30-38b0-9b95-7d425f5c2c15 | -15.5624 | -43.749901 | 2024-10-26 00:31:45 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| b8393288-4b22-3a37-b4b4-8e2c4ded4e93 | -15.5642 | -43.757801 | 2024-10-26 00:31:45 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e8b15af3-dd00-3832-9d1d-c051c3039d42 | -15.4564 | -43.605801 | 2024-10-26 00:31:46 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d9e0428c-ebe9-3885-9937-0fd757504db6 | -18.136 | -57.301998 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1f21c0db-3a72-3b28-83c6-2575e2c40ac0 | -18.126301 | -57.3036 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d9b50382-dc05-31a0-a0e6-abf8eb23aab7 | -18.131001 | -57.3326 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d26f7563-ae93-35b5-bcbc-6e496ca3e7a4 | -18.102699 | -57.2192 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed542173-3801-3ab7-a50b-5bbc03ced05c | -18.088499 | -57.192299 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 02b06c60-bbb3-30d3-b53b-9ecbfa1e7943 | -18.0931 | -57.220798 | 2024-10-26 00:31:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4bc6b09d-2314-3949-9420-b28d0a37206b | -18.0788 | -57.194 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 512b4ee1-8584-3014-912e-3adc4aa0963e | -18.083401 | -57.2225 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed675f2a-37cf-3728-9b8a-7bd5d7617e9c | -18.0646 | -57.167301 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d085ffce-a9bf-3a80-a9d0-92f090f03eed | -18.069201 | -57.195599 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fcf925aa-c2ba-311f-a4d3-36038d6804db | -18.0877 | -57.3102 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b3ea71e-89a5-3f93-8ea6-9ca8b84f1ca5 | -18.054899 | -57.168999 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| be1f782b-3826-3f47-bac6-1a70e674138b | -18.0734 | -57.2831 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cb7097d-8576-3427-a26c-aa7049140ec5 | -18.077999 | -57.311901 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87e9146b-2954-31fe-9cfc-28004e614099 | -18.0637 | -57.284698 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c3009df6-1471-31d1-85dd-e4ac6beb63f9 | -18.0683 | -57.313499 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e50f21ed-e527-3d4f-be6b-d0ec6c3453fa | -18.073 | -57.342499 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03f1ad81-4a50-31eb-ab75-7fbb6f809220 | -18.058701 | -57.315102 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| edf6d1c8-555a-3b83-8736-e65c76b3c515 | -18.0634 | -57.344101 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c4eb2e87-2c47-3b60-8a5a-c0cda965245c | -18.044399 | -57.287998 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8eb7a84f-3a2d-31e3-bad7-2f17db0ef70a | -18.049 | -57.316799 | 2024-10-26 00:31:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06ef7148-c386-3e02-a0fc-e46dd253cd0f | -18.0301 | -57.260899 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d399a1c2-f9c4-3662-b806-94c067f5d999 | -18.0348 | -57.2896 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 59d8b6bf-7e57-3483-9463-9c58b936b17e | -18.0394 | -57.318401 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bca6fdcd-07c9-39f7-a13d-87ac2b3473fd | -18.020399 | -57.2626 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f2e2cfb9-68e6-3d49-a77d-ada818468358 | -18.025101 | -57.291302 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8975253a-c0c2-3937-9ccc-428ac2f1e14c | -18.029699 | -57.320099 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1889344b-d2ba-3afb-b052-250bc512761e | -18.02 | -57.321701 | 2024-10-26 00:31:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f56bf33d-6269-3f4b-be28-5f7f601bf452 | -17.865 | -57.4678 | 2024-10-26 00:31:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b4e738e-ffaf-3650-821c-b9a72a945f32 | -17.8554 | -57.469501 | 2024-10-26 00:31:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c857825c-63ba-31f3-9404-7ab2c17dd584 | -17.8409 | -57.441799 | 2024-10-26 00:31:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91e123c0-c0dc-3a05-a215-8132de20aa33 | -17.8312 | -57.443501 | 2024-10-26 00:31:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5d7ca52-7b40-3cc6-a4c2-ee78ec241522 | -17.783899 | -57.273701 | 2024-10-26 00:31:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6075715-3b28-3844-89ba-f9cdf09276ee | -17.7885 | -57.3022 | 2024-10-26 00:31:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d20d1f60-9ce2-31fe-a649-1f2a76d34a22 | -17.7743 | -57.275299 | 2024-10-26 00:31:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d9a9063-8dd5-3e90-bed8-7eea3c6d17d0 | -17.7789 | -57.303799 | 2024-10-26 00:31:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9161fce-33ce-3132-968c-c70695265186 | -17.0476 | -53.429798 | 2024-10-26 00:31:54 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
