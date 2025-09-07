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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 137b89a3-e76c-36aa-9e73-b02ebb4c7533 | -6.27032 | -53.43784 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 018923fb-a410-349e-ad23-fb2e8730937a | -8.68617 | -54.66453 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4888b45-97ac-3292-beb9-01eacd339066 | -6.20051 | -53.2588 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f9cffa4-3c12-3d4c-8f35-c528a72a2584 | -9.45992 | -56.04715 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80cd239-0edd-370f-8caf-78e8c44cb726 | -6.19992 | -53.26303 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 090225f8-105c-3dc5-a02c-d0a58c368522 | -3.44937 | -52.72395 | 2025-09-07 05:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cbef714-e769-30b2-b401-ab94929b1919 | -8.70117 | -54.67814 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf4db7a-0775-3781-8e1c-05f3aa9c8d0a | -5.96854 | -53.59935 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19c9a4ae-7582-3617-8ae5-0f744ae1abea | -6.28239 | -53.43549 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69e1b5e-9f04-3f3f-97b3-da01bd5e6333 | -8.69074 | -54.67241 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdc3b288-b696-3b9d-976a-ee4b393e115c | -8.68596 | -54.66902 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 396be7a6-a4cf-3291-bd34-1356c48d310e | -3.90609 | -54.68135 | 2025-09-07 05:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3241b3e7-c430-3c45-b9e4-77466f7773e6 | -8.69526 | -54.68061 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112c1a2b-d285-3f0f-9d34-45415cd03bc3 | -6.20111 | -53.25459 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f502a650-3ab6-38aa-a74b-2b697154d618 | -9.39356 | -54.77099 | 2025-09-07 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c330eea5-2c47-3f1a-81cc-f2c9c5379d76 | -5.85969 | -57.77225 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d17c120-3dd6-3c87-9a4d-93147540d33a | -6.27551 | -53.44271 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2197cc39-ce80-3778-9e62-65654e84b00b | -5.95551 | -53.79645 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b8e6572-f66a-3f92-a506-03d29c194b63 | -5.9715 | -53.59647 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59ba273-68b6-3f6d-91d5-25b250ff3832 | -5.955 | -53.80019 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d321546a-0b9b-35c7-a838-da6e542183f0 | -9.46118 | -56.04688 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ae6a91-014b-36e2-af7e-e41288330349 | -6.20513 | -53.26815 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45867a8b-bcbd-319e-9c8d-d389f8b7a4ab | -6.84502 | -52.85076 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f212f741-90a2-3718-9dd5-63096fa837c7 | -5.89752 | -51.93952 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0abbaf2-e034-3a62-bfa7-ac2281f19f96 | -6.28071 | -53.44745 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c3cf4bb-a044-3a2a-9d38-a54be8e22fd4 | -3.32815 | -54.90824 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 510ee8bf-e7d5-3a7b-b484-a2d9e1b85e33 | -5.9517 | -53.79513 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51f3b6a4-a475-37bd-a50b-ae585da8ad21 | -8.35366 | -52.56065 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51b14aa-bb1d-3d3a-8985-8277f1dc3a8b | -8.69145 | -54.66976 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 192fdbc8-3492-30fb-b6be-0740c54d6843 | -5.86456 | -57.76874 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b9626ea-4681-38b7-ae6c-37385c5201b8 | -3.24369 | -50.80462 | 2025-09-07 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c30cb593-8808-3970-806b-df31f92fec02 | -7.68168 | -50.30735 | 2025-09-07 05:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73d726e6-9c03-3d3a-9ef3-96fc1db604a7 | -5.95116 | -53.79888 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59e7de6c-a470-37b0-83fa-1ecc7bbc995b | -8.07019 | -52.37989 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e49d36f-ecd2-3f31-82df-07140d75de8a | -5.91141 | -57.7334 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 837bd3f6-7dfc-35d7-85ec-ee5979bd2a4c | -3.21176 | -54.96499 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28dfa567-ce43-3b00-8745-ab19f37e4c37 | -8.19713 | -50.12778 | 2025-09-07 05:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad30ea6-14bc-3ad6-ba82-24b6ad81c927 | -6.27664 | -53.43467 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 930635e7-a4fb-32da-b97a-7ec2af00266d | -8.06973 | -52.3835 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bb58c11-9a9f-3546-9b97-dcc8500ed568 | -9.45531 | -56.0521 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1017b92-5d31-3403-b900-c4baece1011b | -5.78461 | -57.55138 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 502219e5-2887-366b-bcbe-987139bb742a | -3.53554 | -53.02329 | 2025-09-07 05:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 677e4c21-1a7f-3c9f-a871-9a0f60f3a398 | -8.70189 | -54.67522 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71505f56-edb6-36ef-9a8a-86e0f9367e58 | -3.33261 | -54.90989 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcf384c7-92df-3ca6-ba8a-4263f24b0a3c | -6.272 | -53.42581 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c397582c-8a50-3d46-b952-c043b13f0039 | -9.46499 | -56.04779 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 226f960b-34e3-391a-85dd-d1ad309ae388 | -7.67762 | -50.3082 | 2025-09-07 05:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab0f670-3d7e-3633-9fbd-2434e223f1bf | -6.83961 | -52.84535 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51921004-88d5-3880-bbf3-dc8fff331b4d | -6.15121 | -57.95139 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 912820ad-1c81-3dbb-9c5f-149e9acbd353 | -9.45954 | -56.05011 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 246fda91-c147-30fa-8792-1bf8312f8d6a | -8.68571 | -54.66808 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13335d58-78f7-3cc2-859f-7beaf8bcc81b | -3.82251 | -54.12183 | 2025-09-07 05:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25573ce6-8b34-36fa-882e-6f40633ab990 | -7.67547 | -50.29924 | 2025-09-07 05:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f642ce4b-6155-337d-b8b1-1652aef326f4 | -5.78401 | -57.55549 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1455603-0176-3ba0-96c5-9d5751378f37 | -5.94991 | -53.79568 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9264b201-0e1d-3f8e-ae8d-6acc1a58d222 | -5.95448 | -53.80393 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09fa8f9d-a42e-32cc-afef-0f6b4e65d8d9 | -6.27777 | -53.42661 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f7c0932-99b2-3267-9526-93990367b054 | -7.17281 | -63.13374 | 2025-09-07 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ff3425-1e23-3339-8254-2c3b084b0fda | -5.96963 | -53.59179 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6878217-50b2-3680-a9b0-416b903bb897 | -8.69575 | -54.67687 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00f65e18-aa88-37d6-bec9-25f239db33a5 | -6.19353 | -53.26629 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd3bc25-91ff-31bf-8f2b-1c85cbf37d7b | -9.45915 | -56.05305 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5620c7d0-2e0d-33d2-93dd-2d3f31a77c88 | -5.90385 | -51.94022 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c49b545a-2f24-387f-b116-ec4740669b84 | -6.30525 | -51.41209 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 93ed6179-3f4c-3862-9ceb-4259fb4757dd | -6.19414 | -53.26193 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b8dbc8-434d-37ac-97fc-3ebe169f2a52 | -3.2429 | -50.80999 | 2025-09-07 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10371dd4-2730-3805-95b9-56e87adfe6b2 | -8.18891 | -50.13518 | 2025-09-07 05:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8cf4e9-7633-340c-a7df-5ed7216f53ca | -8.92073 | -62.99784 | 2025-09-07 05:38:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 796b7717-74ba-3662-a5f1-8d3c90d3b6e7 | -3.90011 | -54.68653 | 2025-09-07 05:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2712089-45cd-3361-9ab9-d480906046aa | -5.78832 | -57.55612 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a098072-3ad2-345a-b473-9794933777d2 | -6.8254 | -52.80631 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9477e09a-9fee-3e7d-b894-5e324efa97db | -6.83755 | -52.80755 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f830da5a-3077-3a8b-8131-5ec435ed12fc | -8.91735 | -62.99731 | 2025-09-07 05:38:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 440dbda1-d2bf-39a2-86e7-11d1dfc2d190 | -6.2772 | -53.43062 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd0e397-bcea-3c1e-a4ce-3ba2b7d9186b | -5.90148 | -51.93911 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8929b95-df1c-310c-9062-ce17f70d0964 | -6.19474 | -53.25769 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4c23eb4-8acc-3a9d-8758-48d70bed3b5d | -9.6881 | -51.08072 | 2025-09-07 05:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac31435-ff50-3c06-b730-6b06686a0222 | -6.27144 | -53.42984 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42267bc3-e9ce-32a4-9686-ae064da3c4b0 | -6.83149 | -52.80682 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288381c3-46b2-326a-a449-763bbbfc80f5 | -5.97423 | -53.6 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3320a128-e761-3d31-b2c2-d53eabbb72d6 | -8.31135 | -55.09887 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e54f3576-1ae0-3545-acfd-18685325ba75 | -9.68876 | -51.07508 | 2025-09-07 05:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39d0e0af-0bf1-3193-85a4-860f2ad3ae91 | -9.68954 | -51.07561 | 2025-09-07 05:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 467b2c07-ee85-3ec3-b714-decc0fde13b6 | -7.6715 | -50.29974 | 2025-09-07 05:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39e0cd3-929d-31d5-afb2-0a7364b721d3 | -3.2077 | -54.9649 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1574271d-702b-3e4a-a316-e83878cca960 | -6.19931 | -53.26735 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54647902-681f-327b-8ca9-29f0332c954a | -6.27607 | -53.4387 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f642c3b5-02a1-3d47-8a93-a7ef9346706a | -8.68645 | -54.66548 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f14efad-3ea8-36b6-8bc9-8967f5d5252e | -9.46078 | -56.04983 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3fc326a-a534-360f-b76d-d01ce5be763c | -6.28353 | -53.4274 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8183eb6-fe2e-35d3-88ce-a4cb0c11d9ba | -5.91569 | -57.73402 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc70cc98-8aa1-3293-b246-84d2bd670a78 | -5.94939 | -53.79943 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2131854f-0ff5-3458-a609-d6f1b7608df1 | -9.46037 | -56.05277 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 865109da-411f-35d3-8321-6b3847790f1d | -3.21265 | -54.9657 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c5cfe5e-a3cd-36e1-8042-1f0b64e78fe5 | -3.25022 | -50.80553 | 2025-09-07 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58bd3802-4c65-3ff8-ba8f-ce125ad02a67 | -9.45997 | -56.0557 | 2025-09-07 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8f3e745a-7282-335b-a637-6858a7eaa714 | -3.90565 | -54.68434 | 2025-09-07 05:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126a792d-41be-338d-9217-50c2860db3b8 | -8.30723 | -55.09859 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e088b769-a2f2-3e2b-b42b-42c7be5a9402 | -8.06926 | -52.38711 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0b951fbc-17b2-3204-a319-544e25cae4bc | -3.82202 | -54.12511 | 2025-09-07 05:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README78.md)
