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
| 026ebfd7-11a4-3a9e-9983-5a9d897025a6 | -12.5373 | -53.476601 | 2024-09-27 00:34:14 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e804578-ac3d-31e2-bb58-5322f1212a83 | -12.5398 | -53.489601 | 2024-09-27 00:34:14 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d016312-2e8d-3d9a-87bf-be80b88edac4 | -12.5424 | -53.502602 | 2024-09-27 00:34:14 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6bbb899-56fc-3abe-b04b-1f139e2f5265 | -12.53 | -53.4916 | 2024-09-27 00:34:14 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3bdf993-d44f-311c-a4e9-6392de26e08e | -10.2877 | -43.5219 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 450b481c-8545-3162-86b5-f5cedc22e12f | -10.2899 | -43.5312 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05aaa5eb-4c70-36bb-8e84-0f568e1de861 | -10.2921 | -43.540401 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5686b32-b1e6-3e5f-a3b5-c4968d550b9f | -10.2801 | -43.533501 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3077d3d1-4966-3fcb-ac60-02886240d0ba | -10.2823 | -43.542801 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df0da98e-6926-388a-998d-218457b30ff2 | -10.2845 | -43.551998 | 2024-09-27 00:34:15 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9769b6-85a3-3e03-90b2-338103979289 | -12.6894 | -54.660198 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84b72cd5-426d-3ed8-aca6-157861e7bad3 | -12.6924 | -54.6759 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a43836f-7b52-3452-9f51-ef6f6939f322 | -12.6735 | -54.630901 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be5a2502-b74a-3b83-8a54-201407dd6b1a | -12.6766 | -54.646599 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0262176-0d84-37b6-a3f3-bf03a0c143ab | -12.6796 | -54.662201 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8cb9be-9110-3a0b-9ddb-1b8915f4975f | -12.6827 | -54.677898 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95978410-6d0f-32bb-b08b-43ef46a5ebbe | -12.6638 | -54.6329 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b42d4181-9ab6-3b20-b3d7-c99b1b42a8cc | -12.6668 | -54.648499 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0f5eedb-e527-372a-ae27-553eb0061fcf | -12.6699 | -54.664101 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8796f9a-6e64-3cf3-bf47-9d7e882827c6 | -12.6729 | -54.679798 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbcfffc3-0d98-3227-8cf3-3e5241ec93e5 | -12.654 | -54.6348 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b47111bd-1b43-3d8a-8f99-3f6859b8803f | -12.6571 | -54.650398 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 110e2dbe-44c1-339d-a2ea-181cb08df84e | -12.6601 | -54.666 | 2024-09-27 00:34:15 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30980de0-9b5c-33c5-baf1-727814821772 | -10.5206 | -44.865601 | 2024-09-27 00:34:16 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbc4907-9ab8-3033-a0cd-cdfa8b361d11 | -10.8032 | -46.001999 | 2024-09-27 00:34:16 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a675575c-21e7-368e-b2e2-3659ec5b4f7b | -10.6635 | -45.842602 | 2024-09-27 00:34:17 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a38c7d33-e751-3f94-9f2f-c29f1b79f2aa | -10.6652 | -45.849899 | 2024-09-27 00:34:17 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94180797-06ba-3860-b695-0caaf8de1b77 | -10.644 | -45.847198 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38c2a975-9e1e-396a-924f-051c94e5838d | -10.6456 | -45.8545 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b211294f-6f6a-3de5-83f2-006986f71675 | -10.6473 | -45.861801 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26d55636-cb87-30ce-9351-56429450636f | -10.649 | -45.869202 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d737c264-142d-3dc1-8b4d-cd4e32b0f8bf | -10.6507 | -45.876499 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dfe78c4-7cbe-3963-8451-870ee2c01bf3 | -10.6461 | -45.946701 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 347e8fa9-c57d-34e9-996f-097a5472c75f | -10.6478 | -45.953999 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92876b2c-eab2-30b3-81ee-b103b618a7f1 | -10.6494 | -45.9613 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8b0731-d153-3c7d-92ea-53d833bfde49 | -10.6363 | -45.949001 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe5eeb4-c6f8-32b6-992c-f2a28374f272 | -10.638 | -45.956299 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09584fd9-bbee-34f5-a924-13cf6f173178 | -10.6396 | -45.963501 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99fdcd3c-305e-3c62-9403-3feae35dc7d5 | -10.6413 | -45.970798 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8a75074-dcf9-34f8-abc9-9bd0ff45e299 | -10.6298 | -45.965801 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74d8d807-c88d-3b5e-be78-2e53ca93a4ba | -10.6315 | -45.973099 | 2024-09-27 00:34:18 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4154efe0-b0c3-3fe4-acb9-eac8caec412d | -12.4469 | -54.9743 | 2024-09-27 00:34:20 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f29f64a-119f-39eb-bb22-26f50d09e3c4 | -10.4147 | -45.792198 | 2024-09-27 00:34:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1c9ff09-1e23-3eae-8afd-7ad29c02637f | -10.4164 | -45.799599 | 2024-09-27 00:34:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8970e394-5faf-34ed-9c25-12990fec39f7 | -10.7179 | -47.357201 | 2024-09-27 00:34:22 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8838a59b-baf9-35fb-b4f1-cac814f3b4e8 | -11.1629 | -49.7108 | 2024-09-27 00:34:23 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c69e317-2aab-3cfe-917f-4c637de07de7 | -11.1646 | -49.718498 | 2024-09-27 00:34:23 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 779cc4e5-c86e-36f9-b4c8-6c04d70b5841 | -10.7074 | -48.562401 | 2024-09-27 00:34:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd8524be-d66f-3187-b3a3-ebd30e35d8cb | -10.7172 | -48.747101 | 2024-09-27 00:34:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7298c4e-eace-34ff-a245-d3523d4d6861 | -10.7187 | -48.754299 | 2024-09-27 00:34:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b049501-c15b-3d10-b4c4-04f463d1873e | -10.7074 | -48.749199 | 2024-09-27 00:34:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67299305-2673-3e4e-b109-f91ab60855e7 | -11.0137 | -50.162102 | 2024-09-27 00:34:27 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2ee31e4-3be6-31de-a6cf-63f198962607 | -11.0154 | -50.170101 | 2024-09-27 00:34:27 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ba509e2-71b1-3c60-bce2-d153cd1317ff | -11.0171 | -50.178101 | 2024-09-27 00:34:27 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0455fad5-0a30-3878-898f-538043b47db6 | -11.0056 | -50.172199 | 2024-09-27 00:34:27 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42a69f78-97ed-3361-b0cd-282e3f791211 | -10.5338 | -48.055698 | 2024-09-27 00:34:28 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae1b6e07-10cd-32d2-9f3c-54c4b45bdd46 | -10.5353 | -48.062698 | 2024-09-27 00:34:28 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff6f43e-68fb-393f-8316-4873f79505f8 | -10.9941 | -50.166302 | 2024-09-27 00:34:28 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d35520cc-1515-328d-9b34-56e5b5dd31a7 | -10.9958 | -50.174301 | 2024-09-27 00:34:28 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93e32209-ed92-322c-afde-9dbb76e22ad1 | -11.0992 | -50.658798 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2c4708-8d50-38f6-8704-1038bf0eb2a2 | -11.1317 | -50.812099 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fda4bca4-4b04-39c3-8553-9ded88ea099c | -11.1335 | -50.820702 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8879e6cb-b351-343f-aef6-9b098c07c41c | -11.1219 | -50.814201 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1a195d0-a02e-3b3b-812a-f107c19a99a8 | -11.1237 | -50.8228 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| afe98023-1648-326c-8fc4-daad3b531310 | -11.1256 | -50.831402 | 2024-09-27 00:34:28 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbb7693c-442d-3fce-9840-7b95ff9a3dbe | -10.9463 | -50.134998 | 2024-09-27 00:34:28 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3dc3e12-5f28-3e16-bedc-11c7b1d180ed | -10.737 | -49.213902 | 2024-09-27 00:34:28 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc3c4464-17c4-37a9-96a2-76386bd71f8c | -10.8726 | -50.125999 | 2024-09-27 00:34:29 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bef93f9-fc88-3f7b-8e6c-5802bfd851c3 | -9.273 | -43.291599 | 2024-09-27 00:34:30 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d0fe83af-9d4a-39e3-9fb3-d4d927994e1d | -9.4663 | -44.064301 | 2024-09-27 00:34:30 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7feb99cb-2948-398a-84cc-214b4c23f255 | -11.67 | -54.424099 | 2024-09-27 00:34:31 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b00cada-e4a6-3eb0-9df8-5d09b3ef5da3 | -10.6372 | -49.890499 | 2024-09-27 00:34:32 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd2f2864-2b09-3e9d-b685-c7f02cc018e9 | -10.6389 | -49.898201 | 2024-09-27 00:34:32 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c417fe55-be90-3f2e-8d89-8809272fced9 | -9.9637 | -47.484901 | 2024-09-27 00:34:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e646c971-3322-3b8a-9a25-ba81aa2a4e6d | -9.9652 | -47.491798 | 2024-09-27 00:34:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb8cfec-7df1-313f-b54f-a5b6a7d191a0 | -10.6405 | -50.5746 | 2024-09-27 00:34:35 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21d5f8fe-adec-34d2-b942-66ba2eddfa2b | -10.7258 | -51.071499 | 2024-09-27 00:34:35 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 180a1fe1-7c39-3cbe-ab0c-e276efff3d72 | -10.7276 | -51.0802 | 2024-09-27 00:34:35 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf196303-187d-374d-a35f-01a9ee3a601c | -10.716 | -51.073601 | 2024-09-27 00:34:35 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab123c5f-1002-3193-a485-bd60a78808b3 | -9.8759 | -47.461201 | 2024-09-27 00:34:36 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbdfdcf7-2ee4-357d-bc97-5b3a9ebf7efd | -9.8775 | -47.468102 | 2024-09-27 00:34:36 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d659e80-8267-3cd9-b047-156ff5449a5f | -9.879 | -47.474998 | 2024-09-27 00:34:36 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98aa94cf-76d8-3d2c-bdab-f8963308c11f | -9.9359 | -47.774899 | 2024-09-27 00:34:36 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84250b65-108b-39be-8d9e-677885675392 | -10.6199 | -51.103298 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81b87608-dc39-354b-8cd3-70fe9699c0b8 | -10.6218 | -51.112099 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2d07cb-8367-3847-8053-24b4a61ab34c | -10.6236 | -51.120899 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28c3a63e-d391-30d4-9a67-fc1814c43f1b | -11.1964 | -53.885899 | 2024-09-27 00:34:37 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d653fd20-8dd8-3cd3-b76a-c673986c0d62 | -11.1991 | -53.899101 | 2024-09-27 00:34:37 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56da78fb-1bc3-3e32-b845-36ba6c30fdcf | -9.5511 | -46.299801 | 2024-09-27 00:34:37 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4406648b-ab81-3fa8-955f-24a3f0299430 | -9.5527 | -46.306999 | 2024-09-27 00:34:37 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf70392a-d66b-3e71-b74c-dce915a51cb7 | -9.5544 | -46.314201 | 2024-09-27 00:34:37 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b008be63-2bd0-3133-9f64-a238167759ab | -10.6083 | -51.096699 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7504892d-aa89-37fa-bd10-2b712c558fb5 | -10.6101 | -51.1054 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dc3b120-d568-319f-b0a7-957c94152de9 | -10.612 | -51.114201 | 2024-09-27 00:34:37 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 269722e0-48ab-3158-b5b5-6f5fee63d19e | -11.1867 | -53.887901 | 2024-09-27 00:34:37 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91f28599-127e-3bb3-a8e7-483fbb4c3a16 | -11.1894 | -53.9011 | 2024-09-27 00:34:37 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3212d82e-ab7c-3143-aaef-5d93dfab4ba0 | -10.5672 | -51.096401 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3193b7-a3f4-363f-b188-4ada502aafed | -10.481 | -50.739399 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b8d63ab-3db5-363d-ad5c-8de09293e39c | -10.4828 | -50.747799 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a98525f7-29dc-3035-a63e-5af30c195091 | -10.5537 | -51.081001 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
