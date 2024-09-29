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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 235dc59e-5cbb-3e5c-a702-be0a8b5e34a9 | -11.06 | -52.44 | 2024-09-29 08:04:21 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6b19ad-f22b-307a-ac16-ecf0d2a503a8 | -11.03 | -52.49 | 2024-09-29 08:04:21 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 015146b3-2326-3e8d-a171-41d75b59e765 | -11.06 | -52.5 | 2024-09-29 08:04:21 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd268e9-2014-31ab-a446-5a39fe56b871 | -11.03 | -52.43 | 2024-09-29 08:04:21 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4c1b38-bee0-3636-bebc-8bcd42486c4c | -11.06 | -52.44 | 2024-09-29 09:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57f7c517-e6ee-379e-ab14-a7a181c18e85 | -11.09 | -52.51 | 2024-09-29 09:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5db77e45-ac5a-3241-9da3-6a3a329746f1 | -11.03 | -52.43 | 2024-09-29 09:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b78af71e-13b6-3809-9cc1-9418b996babe | -11.06 | -52.5 | 2024-09-29 09:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 408d6d33-6dba-3f3b-b561-ce1215cff87b | -11.03 | -52.49 | 2024-09-29 09:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24816a7c-c826-3e7a-af6f-fb1732904bc1 | -8.76 | -45.16 | 2024-09-29 11:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 413751ed-a348-3f81-92f3-31b049cf8e55 | -8.79 | -45.16 | 2024-09-29 11:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1c41baf-e403-39ad-9aff-3aaa54870213 | -8.76 | -45.2 | 2024-09-29 11:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab0dc995-0c85-3a91-a008-8ebfe974e139 | -8.79 | -45.12 | 2024-09-29 11:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbbc4ed5-397e-39e2-b05b-47b1923149cf | -11.07641 | -45.55181 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 1442660b-293b-315b-942d-f8d78e7703f7 | -13.35532 | -42.05904 | 2024-09-29 11:53:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 2c97e86f-4e9d-3f0f-8fea-347abcb8a6fd | -12.32473 | -42.60659 | 2024-09-29 11:53:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 42.1 |
| a081d0b1-f6f5-3efb-bb72-53c586540edf | -12.31087 | -42.60411 | 2024-09-29 11:53:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 14f7cb73-f7fe-3333-93be-343cce0bf6b5 | -12.30659 | -42.62831 | 2024-09-29 11:53:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 33.4 |
| 1005bf5f-c35c-3f5e-b7f6-b7f89f29a56d | -15.40983 | -43.7905 | 2024-09-29 11:53:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 08676e1e-c702-36b2-84a8-1338fca8d9e2 | -15.398 | -43.79422 | 2024-09-29 11:53:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0b458d81-9a0a-3e4d-8903-6bbd156616f7 | -15.39556 | -43.78778 | 2024-09-29 11:53:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4fb2a5bf-4ba8-36d9-8e99-9763df6cd7a2 | -12.82376 | -44.84061 | 2024-09-29 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 5acab7e5-eba1-319f-9aa8-4d11de5a28eb | -12.81706 | -44.83348 | 2024-09-29 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| e74271f1-1ba1-3734-ac91-145e4b793aec | -14.49227 | -45.25278 | 2024-09-29 11:53:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 4764219b-0df6-301e-8906-33758f0ba013 | -14.48593 | -45.24396 | 2024-09-29 11:53:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| f7b1efe8-935d-3572-9011-e37a7b5ec0d7 | -11.76096 | -45.50823 | 2024-09-29 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 30367e09-7bdd-3293-b1bd-9b3d33337470 | -11.12044 | -45.60929 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a4d1478d-6133-3098-9bfb-5eb40893c995 | -11.10163 | -45.51342 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 2538a480-25ce-3ae3-9910-59860fdc423a | -11.10159 | -45.50811 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| b5fc38d7-ae0b-329a-9e81-fccaef0a657f | -11.09445 | -45.54872 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 404.4 |
| 6d2606be-a7c4-3eef-b599-49221dfa711a | -11.09425 | -45.55381 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 385.8 |
| f7582065-7b23-3b47-a80c-cd1e751ae7d6 | -11.08413 | -45.50989 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| afa5521d-5b67-38bc-92a9-f32aaa9d78a7 | -11.08412 | -45.50439 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 06ec5325-b194-3c50-bea1-c5632b1bcbc7 | -11.07667 | -45.54643 | 2024-09-29 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b5791143-e04c-3e4a-bb8c-b20fc6d8842e | -15.94013 | -43.51424 | 2024-09-29 11:55:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 60b6e8da-3099-36a2-b26c-8139624d3c90 | -15.82815 | -43.42928 | 2024-09-29 11:55:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 117c462f-2179-3663-bdf9-105333ec97f3 | -15.81945 | -43.47796 | 2024-09-29 11:55:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 76f47266-7ea3-37eb-9d2b-d6ee8933f391 | -21.90706 | -48.20767 | 2024-09-29 11:57:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d3baed3a-03a7-3e25-a98e-e4dc92be5c35 | -21.90884 | -48.21415 | 2024-09-29 11:57:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e3a45da0-53d7-3dde-846b-d73246b1eb3e | -21.9162 | -48.1646 | 2024-09-29 11:57:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 41.7 |
| c523af3c-ca1c-34f4-b091-ae699402898e | -21.91825 | -48.17115 | 2024-09-29 11:57:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 2efbfd8a-4a6a-3365-b305-bc0482eba6e3 | -22.95838 | -47.16007 | 2024-09-29 11:57:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 449a78da-9c86-35f8-9d83-6abdd04d6871 | -14.49 | -47.45 | 2024-09-29 12:04:02 | MSG-03 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c59cd9ae-d1df-314c-aec2-7330483e212d | -14.49 | -47.5 | 2024-09-29 12:04:02 | MSG-03 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 235d3852-15eb-3cab-b6a8-8ef35c4f4ed0 | -11.06 | -52.5 | 2024-09-29 12:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96d95690-6197-3874-a428-627129ef04c1 | -10.86 | -46.01 | 2024-09-29 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 987e854d-8e8f-3a84-af20-49ea2736f66e | -8.79 | -45.16 | 2024-09-29 12:04:34 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78c182f6-d39a-3575-aac2-d373c155f9be | -8.76 | -45.2 | 2024-09-29 12:04:36 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 251e0534-7dde-3e77-a2b1-0f82d13e94b9 | -8.52 | -44.74 | 2024-09-29 12:04:36 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b14eecd1-4247-38c3-b2d0-bc8771d4eff3 | -8.76 | -45.16 | 2024-09-29 12:04:36 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7bfd04af-1a6b-3227-b118-b096697f2a6b | -16.93 | -58.03 | 2024-09-29 13:03:51 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b654b8a4-d077-3a0f-9e1a-60201138bfa8 | -16.92 | -57.95 | 2024-09-29 13:03:51 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0c9f9b8-3541-31d3-b52a-33a2f4939a9d | -12.81 | -44.81 | 2024-09-29 13:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4e1a203-9cd2-36f8-99de-7157c1763cf2 | -12.84 | -44.82 | 2024-09-29 13:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce4ba5d-ba00-3e3b-b698-5fae12fc8ff6 | -11.06 | -52.44 | 2024-09-29 13:04:22 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee967bc-e955-3628-8fad-d7d71a5b62e3 | -11.06 | -45.82 | 2024-09-29 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af5a90b6-75d3-3ba2-95ae-ff0aee6db886 | -11.03 | -52.49 | 2024-09-29 13:04:22 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 165839fd-a4d0-3daa-8ae1-8f3e59d547bf | -11.06 | -52.5 | 2024-09-29 13:04:22 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96996c77-2c83-3676-b26c-bfd27ef5710e | -10.52 | -46.36 | 2024-09-29 13:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b649cd7-8d91-36e9-9f03-0ad887c8d47b | -8.52 | -44.78 | 2024-09-29 13:04:35 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 116ae0c9-9d29-3392-817b-0acdb0ad60e2 | -8.52 | -44.74 | 2024-09-29 13:04:35 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 241c8054-8e65-3825-a0a6-acc659624541 | -8.51 | -44.69 | 2024-09-29 13:04:35 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4ee19c-7996-3e02-8bf3-7b1e09044760 | -8.54 | -44.74 | 2024-09-29 13:04:35 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee4dc7d6-76a0-3bcc-ac9e-9fb911459c78 | -8.76 | -45.2 | 2024-09-29 13:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17c65090-1ea2-3f7c-b109-da142a95772e | -8.79 | -45.21 | 2024-09-29 13:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a30bb17-2fe9-3f80-b9ec-97298448a165 | -8.79 | -45.16 | 2024-09-29 13:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |


