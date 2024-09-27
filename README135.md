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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a156d77f-6d1c-3957-9f5a-6fc506ec5de4 | -14.901 | -51.5395 | 2024-09-27 12:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 580886bb-0ab4-3f2b-a4ae-5c05de7b055b | -14.9026 | -51.4534 | 2024-09-27 12:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| f66d95cb-8d45-3522-8e7d-48f392dd2c5d | -14.8832 | -51.4561 | 2024-09-27 12:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 3f16d00c-4fa6-36d2-a7a4-39680a4cb5b4 | -15.0431 | -49.1672 | 2024-09-27 12:36:31 | GOES-16 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c2b7a6a1-0e9e-3915-b3c0-acbb81cf8e11 | -18.0553 | -44.3645 | 2024-09-27 12:36:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 591fcb8f-7683-3805-b231-dc6ae2639308 | -18.0547 | -44.3888 | 2024-09-27 12:36:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3228ed23-fc03-32d3-a691-4367fb218841 | -8.0886 | -49.5224 | 2024-09-27 12:45:52 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d052c690-cff0-36c9-8d2f-f4fe12102353 | -9.417 | -51.4426 | 2024-09-27 12:46:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| afe4f3c9-d7c4-3c0b-8e93-74a3c521172a | -9.4168 | -51.4636 | 2024-09-27 12:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 81b68d73-a091-38ae-848e-c60929f5892d | -9.5829 | -50.137 | 2024-09-27 12:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 57c1a901-83b3-37fe-a6c6-b09b7232465b | -10.0136 | -53.467 | 2024-09-27 12:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 8c8a8ad7-9843-3739-97ec-4395924a147e | -10.0139 | -53.4464 | 2024-09-27 12:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 550.9 |
| f79b4386-f492-3ee9-b296-ff905f3e7953 | -10.0134 | -53.4875 | 2024-09-27 12:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 5729b6c2-4222-3b73-b014-1fa268b2817b | -10.0322 | -53.4859 | 2024-09-27 12:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 8e5570b4-f71f-3815-878d-8a7e92dc77fe | -10.0324 | -53.4654 | 2024-09-27 12:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 386.8 |
| e889f2c0-d668-3706-80c5-8e1b12a1e26e | -10.2824 | -43.5551 | 2024-09-27 12:46:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bd680896-367a-340e-b34f-30ce9663267e | -10.624 | -46.0023 | 2024-09-27 12:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6281133d-74a1-3577-bbc8-a7f8dd1eff38 | -10.6434 | -45.9772 | 2024-09-27 12:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3ea32159-d44b-38df-a5c5-4d04f85d299a | -10.6846 | -50.9847 | 2024-09-27 12:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| c4bbbf21-e7a1-3d11-a657-168701bf5b5b | -10.6643 | -45.861 | 2024-09-27 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 98739ebc-1735-3e0b-a74b-cd824fe09ed7 | -10.6639 | -45.8838 | 2024-09-27 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 24b4ccde-31da-3d46-8130-0fd2e886b025 | -10.942 | -50.1478 | 2024-09-27 12:46:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c03600e0-5e99-3f62-9d97-aec7a6f2cd72 | -11.0976 | -46.1446 | 2024-09-27 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1450eed5-cdda-3ebe-b30c-6396554343b7 | -11.2025 | -45.5616 | 2024-09-27 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 96cf9ebf-065e-3e30-970e-14cb5f897d94 | -11.0577 | -51.3694 | 2024-09-27 12:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f2acdcc8-a826-37d9-bc6f-ce45c33f3827 | -11.0574 | -51.3905 | 2024-09-27 12:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| fc7c5d3f-a432-3bef-9571-7bfb5698285d | -11.2531 | -47.1366 | 2024-09-27 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b0b7bd4b-36b7-3a20-aad0-c3e86aeaebed | -11.2721 | -47.1341 | 2024-09-27 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 08a84fdc-c551-3fbb-b081-52a8485d60b4 | -11.2217 | -45.559 | 2024-09-27 12:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| becc4116-36d5-388a-b3bc-ed27ee6981f3 | -11.2534 | -47.1142 | 2024-09-27 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| aa72c02e-846d-367b-b8ac-b5775d0a5d32 | -11.6409 | -44.5303 | 2024-09-27 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 29df8d49-a24f-3a13-97f5-65a0df76f2e0 | -11.6605 | -44.5041 | 2024-09-27 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 188f1426-551f-37c2-9384-6786b6d0e088 | -12.3242 | -50.5033 | 2024-09-27 12:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6c9af988-b98e-3427-8114-60df6bd97a9d | -12.3434 | -50.501 | 2024-09-27 12:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 8a8f70ef-cff9-343b-b194-ce59e0365af5 | -12.4786 | -50.3986 | 2024-09-27 12:46:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7090a05f-d5f4-3938-835c-f527f24a557c | -12.4782 | -50.4201 | 2024-09-27 12:46:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 13a30f58-a460-3807-9784-428e0ec4ede8 | -13.235 | -45.6245 | 2024-09-27 12:46:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 463.5 |
| 0580ce1c-c79b-3656-9913-005adbe6fa99 | -13.2156 | -45.6276 | 2024-09-27 12:46:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f13267e2-ae21-3b5a-9aaa-6496a38ce4a3 | -13.1614 | -48.5215 | 2024-09-27 12:46:21 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3945b41b-d211-3d50-9ec5-fd0f11600fe3 | -13.2675 | -51.307 | 2024-09-27 12:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f8d663d9-1c4c-344a-bb4a-d23220809fe1 | -14.7305 | -45.5061 | 2024-09-27 12:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 79a1818a-ee35-36b0-bd2b-d962345378e6 | -14.7114 | -45.4863 | 2024-09-27 12:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 378.1 |
| 7af7fd0e-c61f-3911-af88-7d5116b3ccfd | -14.7119 | -45.463 | 2024-09-27 12:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 274.9 |
| c96b2611-920b-3d3b-a6dd-5d86ae2a5260 | -14.9026 | -51.4534 | 2024-09-27 12:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 2bd4c505-50d5-39f2-abe0-e5a6350b1639 | -15.0431 | -49.1672 | 2024-09-27 12:46:31 | GOES-16 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 965f25a7-41ed-39ff-b55e-bb7b325dd3ce | -18.0547 | -44.3888 | 2024-09-27 12:46:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 141.7 |
| cc0e0a6e-6916-3f76-b760-300131cb6eff | -6.3251 | -42.4908 | 2024-09-27 12:55:42 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 295d0a1c-9d70-3edf-829c-385c17c16710 | -8.0886 | -49.5224 | 2024-09-27 12:55:52 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| c2855df0-494e-3c28-a195-727c7d978353 | -8.0727 | -42.9092 | 2024-09-27 12:55:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 2d7b4b82-8c26-31e9-9752-926ac243f8bc | -8.073 | -42.8855 | 2024-09-27 12:55:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 619c9088-c168-3a00-b81f-b3b4f658c8ce | -9.417 | -51.4426 | 2024-09-27 12:56:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 1bdf191b-be04-36d7-86fd-edf99cd66870 | -9.4168 | -51.4636 | 2024-09-27 12:56:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ad8c6acb-5c04-3e77-9c48-db24927df476 | -9.6018 | -50.1352 | 2024-09-27 12:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0eb6faf5-d19f-3c03-a8f3-a118fe6dcf34 | -9.5829 | -50.137 | 2024-09-27 12:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 087a4499-5e01-3ddc-99fa-2aeb753ea381 | -10.0136 | -53.467 | 2024-09-27 12:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| a78196a2-629c-35af-8c3d-4cda25c432d9 | -10.0139 | -53.4464 | 2024-09-27 12:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 690.4 |
| f15b8460-4832-3980-bf8c-9b6b444809d8 | -10.0322 | -53.4859 | 2024-09-27 12:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 307c78e4-2cae-304c-9f1c-b52fdfbd3501 | -10.6438 | -45.9544 | 2024-09-27 12:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 46e72a6d-63f2-3103-badc-e4602e056e9f | -10.6434 | -45.9772 | 2024-09-27 12:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 02a26a78-41a9-343b-9fa7-10b329e1a926 | -10.6636 | -45.9065 | 2024-09-27 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.6 |
| ce9bd954-4a1c-3014-95a1-b7eb19a5a338 | -10.6639 | -45.8838 | 2024-09-27 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 538.5 |
| ead66a4c-2a53-3d09-865d-71c1ec2f3ee8 | -10.6643 | -45.861 | 2024-09-27 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| acb30c67-be47-3ad5-b428-f765fd18b386 | -10.6846 | -50.9847 | 2024-09-27 12:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f9b95b29-3f71-3b5f-868f-6fab064e8fc3 | -10.9148 | -45.669 | 2024-09-27 12:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 018c547b-9884-3b9f-9429-c2eecca7c02a | -10.942 | -50.1478 | 2024-09-27 12:56:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3b69983d-8964-37b5-ab60-4be2236cfb3a | -11.2025 | -45.5616 | 2024-09-27 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| e221b888-e7ef-3600-b086-d82fdf2bcbea | -11.0972 | -46.1673 | 2024-09-27 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 373.4 |
| 33add547-93a8-3212-8d24-254b452bef47 | -11.0976 | -46.1446 | 2024-09-27 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 7477e00e-806a-3021-8b20-9346c9a96608 | -11.1219 | -50.8328 | 2024-09-27 12:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 187c8e79-37c7-35df-aed1-d638a28ac254 | -11.058 | -51.3482 | 2024-09-27 12:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 838c6a8c-a586-3bdc-a137-be40e0a7c525 | -11.0577 | -51.3694 | 2024-09-27 12:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.4 |
| ee92667e-86a0-30e8-a848-7be5852e20d5 | -11.0574 | -51.3905 | 2024-09-27 12:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d8133d9c-63b5-395d-8ff0-74bd07f58c22 | -11.1564 | -49.737 | 2024-09-27 12:56:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 39e4dfda-0647-39a8-a2e0-afe365095176 | -11.2534 | -47.1142 | 2024-09-27 12:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 0012a6ae-101e-3b0e-8302-9dfe02c8c2bd | -11.2217 | -45.559 | 2024-09-27 12:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6032be7f-70fa-3380-9b34-56cbbd0d9362 | -11.2721 | -47.1341 | 2024-09-27 12:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8c7c957a-49ce-375d-8649-62b91817181c | -11.2531 | -47.1366 | 2024-09-27 12:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 1ddad2f2-72bf-3620-bb58-330458b1b9ee | -11.1409 | -50.8307 | 2024-09-27 12:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ab4bb24a-d119-3123-8a2a-a8160e3b51f7 | -11.6605 | -44.5041 | 2024-09-27 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 243.7 |
| 8b675745-bdd2-30f1-b3f8-2fdf8e16d389 | -11.6409 | -44.5303 | 2024-09-27 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 9020cf5f-fef7-39cc-bd5e-d9700c016c56 | -12.3434 | -50.501 | 2024-09-27 12:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 0958f0dc-8ff9-3cca-92a0-edb2e5f2ad7d | -12.3051 | -50.5056 | 2024-09-27 12:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3b943782-9548-31df-b955-beca17958eed | -12.3242 | -50.5033 | 2024-09-27 12:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 244.4 |
| de08b800-1469-30b5-beb5-c5c17b719ecd | -12.3239 | -50.5248 | 2024-09-27 12:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| eeb2d323-6ca8-3f5f-8d70-20ce20613c09 | -12.4786 | -50.3986 | 2024-09-27 12:56:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8faf6fbc-4074-36a2-a392-731e03acee9b | -12.4782 | -50.4201 | 2024-09-27 12:56:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 8dd63900-edba-39ab-aef8-1617bb1c24f9 | -13.1607 | -45.4752 | 2024-09-27 12:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 25e9bfc5-378e-3f57-922e-30eba7c103da | -13.1801 | -45.472 | 2024-09-27 12:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 224db6c6-4062-38b3-a951-e4caff62e4ad | -13.1612 | -45.452 | 2024-09-27 12:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0f37d0c6-078d-3a8d-8ec7-ccdb8bf08589 | -13.2482 | -51.3094 | 2024-09-27 12:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1c2f5ff3-6a53-3a99-b2a1-6ca9589409fe | -13.2105 | -51.2714 | 2024-09-27 12:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 791824ee-0918-3301-9f2d-4988b7f6c425 | -13.2675 | -51.307 | 2024-09-27 12:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 0b96ccf4-5603-3cca-9a86-058cbcd10d17 | -14.7119 | -45.463 | 2024-09-27 12:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| e292b535-261d-3416-b680-21c0836a2bbd | -14.7114 | -45.4863 | 2024-09-27 12:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 0cd52556-a1c8-3b15-9b49-3f58874e2f64 | -14.9026 | -51.4534 | 2024-09-27 12:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| d7752257-0c47-3a78-990d-c9fdfb92530d | -14.9014 | -51.518 | 2024-09-27 12:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f2d90ca7-d46f-39b3-849c-ea2f173bc215 | -18.0547 | -44.3888 | 2024-09-27 12:56:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 145.3 |
| f53b3387-4f9a-30bf-8149-4732bf58cd4e | -5.5888 | -42.9282 | 2024-09-27 13:05:38 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 66bd9ec6-4256-3f3e-bf6d-c7b15648b7b6 | -6.3251 | -42.4908 | 2024-09-27 13:05:42 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 60088da5-2aec-3443-9206-dc9deedb39bf | -6.4055 | -43.819 | 2024-09-27 13:05:43 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |


[Clique aqui para ver as próximas entradas](README136.md)
