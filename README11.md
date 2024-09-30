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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c92df0e-4795-3935-b372-6c0060a7fe88 | -12.7133 | -54.087002 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9226b622-cb25-3b5d-b1ee-b59ead5d6989 | -12.7151 | -54.094898 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d773d7c8-63c8-3c76-a56c-daf9c1366b4c | -12.717 | -54.102798 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31b3c958-12ea-34e0-a381-649f14b0e5b2 | -12.4873 | -53.168201 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7fe276-bcd0-35cf-b8a5-1a4650e0cecc | -12.4894 | -53.176899 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71c5546e-1226-3553-934e-12833b23899e | -12.5622 | -53.485699 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7cf5d2-4ee0-3d58-b5c8-93ff9b3370ad | -12.6998 | -54.073502 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 393f8a5c-6f28-3862-8742-aa957fcc81eb | -12.7017 | -54.081402 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02559ef7-085a-311a-bc6a-227604bbbd2a | -12.6863 | -54.060001 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 834d4ffb-76a1-3ef9-9720-eb7e6bf7f6eb | -12.6882 | -54.067902 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1af2c57f-527a-38cf-91b7-2df041987408 | -12.69 | -54.075802 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5ba9239-01ae-3ee7-a69b-a698a3e9411d | -10.6501 | -46.088699 | 2024-09-30 01:11:55 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5954c88d-7986-3af6-9dd6-0309e9399635 | -10.6571 | -46.115101 | 2024-09-30 01:11:55 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 443c2aea-75b1-356b-bca1-0eb5f63fa47c | -10.6406 | -46.091301 | 2024-09-30 01:11:55 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe04d5c-2d56-39f4-a5b9-69599ef0c28c | -10.6476 | -46.117699 | 2024-09-30 01:11:55 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c62cebe-96b5-3ca8-a361-2f1285bb1446 | -10.6545 | -46.144001 | 2024-09-30 01:11:55 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cbd9c90a-1db7-34e3-8d6c-963b61d7d263 | -12.6728 | -54.046501 | 2024-09-30 01:11:55 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1712d381-71f7-3a99-bf46-d98b06930a6b | -12.6747 | -54.054401 | 2024-09-30 01:11:55 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9feaff3e-0e56-348a-a0f5-c2887fb70467 | -12.6765 | -54.062401 | 2024-09-30 01:11:55 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee6e94e-36ad-3d9f-b5a8-fabd4e7acffa | -12.6649 | -54.056801 | 2024-09-30 01:11:55 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 486b88e7-05c6-3006-8ccc-910f01e12c70 | -10.638 | -46.1203 | 2024-09-30 01:11:56 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e08dc3cb-e020-3d9c-b333-d7994b1843d5 | -10.6449 | -46.146599 | 2024-09-30 01:11:56 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 459690a0-e845-321a-b274-8c1b99e5e6f7 | -13.1092 | -56.414001 | 2024-09-30 01:11:56 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| feff3c6b-a98b-3421-aec0-83260ada9fc1 | -12.4213 | -53.457401 | 2024-09-30 01:11:56 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 048a1446-5c9a-3eae-b45b-d47e3287d20f | -12.6917 | -54.662701 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 738394bb-caf0-37cf-ae06-a81f2a209a21 | -12.6802 | -54.657501 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60238622-32b2-350c-8811-06436919268d | -12.6819 | -54.6651 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44830edc-ea3b-3bc9-b3a7-fd11aa3c5a1c | -12.6675 | -54.692299 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcfb90a-c97e-362d-95ab-556ada85aa81 | -12.6561 | -54.687099 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0d7d4a6-4d51-33e2-8ec5-6e36539c8553 | -12.6578 | -54.694698 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba910fb-3c89-3dc7-a73f-95dfbe512fd5 | -12.6445 | -54.6819 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23c2539f-ff23-3bc4-9e69-2667adeedf8a | -12.6463 | -54.6894 | 2024-09-30 01:11:57 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46c240f5-791a-385b-bc53-e7d67db54058 | -13.046 | -57.291801 | 2024-09-30 01:12:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84a071f8-39f5-32b1-b6b6-65c5723bea47 | -12.2543 | -53.978199 | 2024-09-30 01:12:01 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89a31dbf-69c9-3bd9-8409-cbd6cd776bfc | -12.2562 | -53.986301 | 2024-09-30 01:12:01 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fcbd4f1-79dc-37cb-9725-4d63120052b1 | -13.7146 | -60.684502 | 2024-09-30 01:12:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1f53ef5-e2b5-3a4f-bbdc-9f574927bda3 | -10.7039 | -47.9534 | 2024-09-30 01:12:02 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e806bf3-ce88-3b75-a1c5-d24ab62b1280 | -10.7443 | -48.717098 | 2024-09-30 01:12:05 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1a743b6-7cd5-3d56-8e89-4306edd5f1a6 | -10.7487 | -48.7346 | 2024-09-30 01:12:05 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dda0f8e3-7822-319a-8760-85a0959ac63b | -11.4523 | -53.816299 | 2024-09-30 01:12:13 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50c334fc-ae5e-3ede-87c5-ce2b7685ab21 | -11.4543 | -53.8246 | 2024-09-30 01:12:13 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 242d00b4-b5c0-3334-9da1-eefb029aec8a | -11.4426 | -53.8186 | 2024-09-30 01:12:14 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0459c8-c092-30aa-b589-847ee82a1b53 | -11.4445 | -53.8269 | 2024-09-30 01:12:14 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b402211-c36c-3a4e-af1e-5ff6d4f03658 | -11.0819 | -52.471199 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1b81b2-9450-3c11-a8a7-849b4e9f5adc | -11.0842 | -52.481098 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e11cc60d-bf7c-3c4f-b34d-b37f00d55df6 | -11.0866 | -52.491001 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f16e1f4-337e-3e58-aab7-02796a186241 | -11.0626 | -52.433899 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12c60df9-306b-3e84-a704-524e67fb27ce | -11.065 | -52.443802 | 2024-09-30 01:12:14 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 189a7df6-3e14-3cf5-a72f-0bf24a2dde31 | -11.0674 | -52.4538 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 211e4ef2-8d6c-3377-9316-775b64abae0a | -11.0698 | -52.463699 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bab49e59-75f9-37d0-8abd-fbfc8c2f3ed2 | -11.0722 | -52.473598 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3312357a-f33b-3fcb-8446-ebfcf67f01d5 | -11.0745 | -52.483501 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58117d58-d8b9-30db-9d0e-d67224474069 | -11.0769 | -52.493401 | 2024-09-30 01:12:14 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76b70d6e-cb57-3545-b793-305e71a3fd26 | -11.0528 | -52.436298 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6cf0ed-2d35-31a7-82e5-5f32835272fe | -11.0552 | -52.446201 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63afae9b-4c24-3385-afc3-e31bcc0ec374 | -11.0576 | -52.4562 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6a6442c-8004-3d0e-9c14-452d9b93268c | -11.06 | -52.466099 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58f0d1ee-eb07-3882-8a5e-f6a20be6e6db | -11.0624 | -52.476002 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5072aaf0-a487-39d6-9249-33a364b599b5 | -11.0671 | -52.4958 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 201cc26b-b8bd-3acc-aa71-fac549b43a57 | -11.0431 | -52.438702 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a67e555d-2282-3e9d-b3aa-1f15b1cb96e7 | -11.0455 | -52.448601 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08510a7d-dacb-32e7-9f30-b2c566aa2102 | -11.0479 | -52.458599 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26395d04-61e4-347a-9762-32ade3d99314 | -11.0503 | -52.468498 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31aa3a7f-6415-330e-93dc-6f4f19a7d5dd | -11.0527 | -52.478401 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61432e7c-bd29-392e-b30e-1377befae814 | -11.055 | -52.4883 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4d7e758-dccc-3fab-87ba-80f4c2bb1ff0 | -11.0574 | -52.498199 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 197ec3ef-0ee3-3827-b2fd-331b16ed8b29 | -11.0405 | -52.470901 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa37ae2c-4440-3f4a-b101-417ce07e2659 | -11.0429 | -52.480801 | 2024-09-30 01:12:15 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccc387aa-904a-3cdd-93ac-b7c2b555d326 | -11.2216 | -53.845299 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee7c01c-8d29-362d-8d45-cbcf31716451 | -11.2236 | -53.8536 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9a728c9-346d-3628-b317-61d01c0638ec | -11.2256 | -53.862 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c837316d-f009-3c41-944b-8d3a6a4fa5df | -11.2275 | -53.8703 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 212f950c-50f0-3204-863d-d9a281c33dc6 | -11.2079 | -53.830898 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78f2527d-be74-3f2f-89a1-7eb7f5f44143 | -11.2099 | -53.839199 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4a306cc-0c6f-3b69-8a68-d485560fb6eb | -11.2118 | -53.847599 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc1f5cd-e9c9-3a07-bc2e-474c503f4a4e | -11.2177 | -53.872601 | 2024-09-30 01:12:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d568c08-a5b1-31d2-a8fc-026a8460eb65 | -11.2002 | -53.841599 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0f2aebf-e69b-3c22-ade6-6cc1b39e0760 | -11.2021 | -53.849998 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0364d64d-b9bf-34fa-a7db-b3ed1fef039b | -11.2041 | -53.858299 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8627ef-5070-322a-a123-c51760848f45 | -11.206 | -53.866699 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94070fc9-3b41-3c60-95f1-358c01e8aaae | -11.208 | -53.875 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b42cf0dc-35ac-3730-a828-64b9f64c6bae | -11.21 | -53.883301 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e36fdc6f-94b6-3e01-99cf-d4df2b9d2a7e | -11.1963 | -53.868999 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6b7cbd-1b6e-3a27-9474-1e5340790279 | -11.1982 | -53.8773 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0271fd8c-e1b8-3893-b14d-a17437ea0a94 | -11.2002 | -53.885601 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac43c4f7-caab-3867-bf14-8baf9e14451d | -11.1767 | -53.873699 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8ffb2cf-20d7-3c5e-8472-dcd7bb68b47c | -11.1786 | -53.882 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27d5aeed-f9e2-3e43-96af-3dd698759a4f | -11.1806 | -53.890301 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b41cc123-d686-3b9a-be55-75ea6e164b54 | -11.1961 | -53.9566 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1538429b-cd3e-33ca-92ed-f2cd783ed0c3 | -11.1669 | -53.875999 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50f930ff-853e-3bad-9467-7039b6ab56a3 | -11.1689 | -53.8843 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8773a058-4a22-378b-86b2-01b124a789d7 | -11.1728 | -53.900902 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7e1458-fdb5-3069-8c0f-2f6d4af026ec | -11.1748 | -53.909302 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec654745-d36d-3239-9101-a7a467c49fd0 | -11.8503 | -56.864601 | 2024-09-30 01:12:18 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 090b4b08-3efa-310e-92bd-77a4c694428c | -11.1552 | -53.869999 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c203873-97ee-3311-9ba1-318ed755816c | -11.1572 | -53.878399 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2fb396b-c254-32b6-ace3-65a025fe3c9a | -11.1591 | -53.8867 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dabf17b0-18c2-33ac-9a53-a4a5fa1cb9cf | -11.1611 | -53.895 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03170a90-423b-3b1e-8ef9-fb9e31e06704 | -11.163 | -53.903301 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07580660-3113-3568-b5ba-afe4378160e5 | -11.165 | -53.911701 | 2024-09-30 01:12:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
