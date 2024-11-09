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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8452edd-6689-3ef9-8c65-21fa5b2377b9 | -3.6003 | -47.3614 | 2024-11-09 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| c63d80fa-378d-3c45-b919-6ddb6f86cca6 | -3.9669 | -48.1716 | 2024-11-09 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 95940855-6946-355d-938b-96d575036730 | -1.14929 | -53.65708 | 2024-11-09 05:31:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6a0b2f7a-d8bb-39e1-bbfe-2ef3593e63c4 | -1.51329 | -52.16904 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 0d8e52b0-0811-3586-9f26-f6501d5479b4 | 3.37444 | -51.28059 | 2024-11-09 05:31:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f3eef7bd-ea63-314c-b3a4-1f4ec0d4153a | -2.36407 | -46.85088 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57a8a448-2944-3c8b-9bf4-ac948ef65c36 | -1.56361 | -52.27183 | 2024-11-09 05:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d5bcfdd6-599d-3bd0-961d-e0f90746821b | -1.55283 | -52.27024 | 2024-11-09 05:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 333e0c89-4d07-3617-bf8b-a4690bc4d0de | -2.37311 | -46.85223 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0445b9b6-b594-38c2-9cfc-7be643b83975 | -1.53066 | -52.19868 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 74ce6599-9047-3ee4-9dc2-3f18e2269df7 | -2.4552 | -46.30382 | 2024-11-09 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c6254959-9ffc-3b02-a3e6-126215f77629 | -2.36268 | -46.86018 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7dbda5f-d3f1-356d-b0f6-06a7e8652422 | -1.53268 | -52.18541 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fd7915bf-038a-38aa-8e42-40f41d826564 | -2.31779 | -46.48339 | 2024-11-09 05:31:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ee2d4342-b6ac-3935-ac48-f4c8cf94b4d2 | -2.37173 | -46.86148 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| dc65e685-6cd1-374b-aebc-3289ae9052e4 | -2.45374 | -46.31352 | 2024-11-09 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 59c64ece-36f3-3511-9be5-0cbfc60fe9b6 | -2.15771 | -46.68544 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e58fea8-d950-3231-b858-716cee7dc223 | 2.10561 | -50.84967 | 2024-11-09 05:31:00 | AQUA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0c48e587-fb04-3c5a-b7e8-a88d53c55703 | -2.23334 | -46.55257 | 2024-11-09 05:31:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e151fa2e-6bfe-32cb-a610-ecc6d765de7e | -2.3807 | -46.73954 | 2024-11-09 05:31:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebb8b840-41e8-3b85-9f69-f17390a1a4ab | -1.56161 | -52.28528 | 2024-11-09 05:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 31ba20bc-4c1a-3a19-8063-5a390e75c3ac | -0.22211 | -51.64637 | 2024-11-09 05:31:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cd6ac28e-3dce-3b1e-bdf8-2f106ea2c4c6 | -1.24942 | -51.7636 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7237c82f-1516-348d-a3ca-5de857ab4e89 | -2.23475 | -46.54314 | 2024-11-09 05:31:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e60926cb-58d1-3149-8261-575d401b27e0 | -2.22561 | -46.5418 | 2024-11-09 05:31:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d877d963-44b9-35b9-8031-6bd1bf4daf1c | -2.42741 | -46.29977 | 2024-11-09 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4da59b5-cfcc-3ed9-847b-cd1791688dad | -1.52197 | -52.18384 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5a89caa3-f5a6-33dd-b649-39fe20b30eda | -1.51994 | -52.1971 | 2024-11-09 05:31:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2950fb0c-3be0-3ad5-883d-4809ae1a6a13 | -0.22403 | -51.63371 | 2024-11-09 05:31:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 76d00622-96a7-3cdc-b951-d57e548c92d9 | -2.6732 | -51.82398 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0bc489a1-d527-391f-94d4-fc62d86c7430 | -2.88605 | -48.2994 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc26ae2f-c40c-360d-93f2-9d19b3ce2df6 | -3.0376 | -51.52608 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 38bd0846-6354-3486-8380-9089991e2bcf | -4.39966 | -49.40956 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2258015d-5f2a-326f-8bb5-087df4f3530a | -3.35751 | -50.25735 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 47c08de1-7f56-30f0-8730-2a1b4e49324b | -5.44521 | -43.25153 | 2024-11-09 05:33:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 090d65a0-5d87-3432-b85b-7ad4eface660 | -2.86643 | -50.40701 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6d6304b-e2f0-311d-b606-bd34efda323b | -3.15295 | -54.48149 | 2024-11-09 05:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6b0b72f5-4278-309c-ba83-1761590dcc6c | -3.29463 | -46.41664 | 2024-11-09 05:33:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b5e6703c-746d-3b61-9b1e-196823d0580c | -3.53595 | -50.86507 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e8bcdca8-434a-3535-8667-f2e7606645d5 | -3.96646 | -48.18063 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 9c4ad31e-0e15-3cea-bcee-866cbd9def96 | -3.76951 | -51.7626 | 2024-11-09 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de19d99a-e576-35c0-b6bc-9bbcd40f56ce | -2.85485 | -48.44743 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 515bdf42-583b-3b8e-8096-509bf27eeb5d | -4.7268 | -48.95895 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 723ef5e2-e581-390d-a68f-bf5db32800f9 | -3.03494 | -50.3237 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| acf280cb-d2aa-340f-ac4a-8cebfcb5a0aa | -3.9527 | -48.15154 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d933cae0-6b30-38fb-b8e3-c92b9f369626 | -2.18249 | -48.32346 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95a7a590-2fc8-374e-ab7e-6949a105e15d | -3.05201 | -47.68958 | 2024-11-09 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cbfe1764-2b6e-345d-9922-549cf79af50d | -3.01902 | -51.03504 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b9cbe726-9906-3975-b5b6-9ac2486bc6f2 | -2.20242 | -48.37123 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5b9d8987-8d13-3172-9ea9-930517239715 | -2.67897 | -46.77878 | 2024-11-09 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a12102d5-afd4-35da-b1e3-3de09a37a544 | -2.92136 | -51.67967 | 2024-11-09 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bf290475-fd6b-3b1a-951b-12bdbe2bafd0 | -4.24971 | -47.57742 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e7587dd3-582c-33f0-9a52-e2cdba95a461 | -3.22146 | -50.37376 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 60ee02ba-2863-3256-8db0-821f38549dde | -2.9809 | -47.92355 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11bc5274-16b3-3f4b-a752-d5f2c1714e2a | -5.81822 | -44.11251 | 2024-11-09 05:33:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cabfe7bb-ebcc-3785-aeea-923ca06dadc9 | -4.07615 | -48.31041 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f3dbd81-dcf7-3b50-9bd6-1a7d290a10c3 | -5.81654 | -44.11936 | 2024-11-09 05:33:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5c9c7bf1-ee37-3923-ac13-db6197e7329e | -2.15231 | -49.13263 | 2024-11-09 05:33:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c8a64f83-a033-3fa1-a0ed-9e3eff8a4912 | -2.83454 | -48.46242 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a522930-e277-309d-961c-1e1d6a039189 | -3.25467 | -48.74318 | 2024-11-09 05:33:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 005c2c03-0222-3429-9f34-f6dacbbb1e20 | -2.23755 | -50.52291 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 99ac6510-0237-3468-b33c-e897bed0ca1f | -3.02179 | -48.07352 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2424c4ff-360f-3235-abbb-28f6d766b5dc | -3.81516 | -50.78009 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dc90d62b-f8b5-38a5-a410-30284ac73a3f | -3.13981 | -52.97935 | 2024-11-09 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b2cb0b68-0fc6-3d2f-b985-0d2823e23661 | -2.27718 | -50.67192 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 84305b55-8c7f-3dff-aba4-1b2f7cf56253 | -3.82496 | -49.85958 | 2024-11-09 05:33:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| de09974e-9965-3227-a7e9-39b1304f57a1 | -3.15307 | -52.96704 | 2024-11-09 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7c29f083-34c1-3145-8315-b28e5bb1b428 | -6.13063 | -42.55867 | 2024-11-09 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 06f1346b-d241-3087-8634-46f29314628c | -3.60176 | -50.23732 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a82ff7d3-0931-3867-9a53-e89348da382f | -3.09832 | -53.31864 | 2024-11-09 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| cc4d20f7-624c-3629-a097-5a3bb675ec0e | -2.86369 | -48.44872 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86394f56-5c14-3d29-96f6-c5c8b20c24df | -4.24508 | -48.53629 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26b96130-ea63-3736-9ab7-bb4e0dda45d8 | -2.45705 | -53.68214 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 264e56df-54d1-383b-b95a-f086d94a8dc3 | -4.20855 | -50.61913 | 2024-11-09 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a6e6a786-e24e-3b81-970f-714587ea3b93 | -3.54102 | -50.32664 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98f8b41d-3630-368a-bb2a-c274c1a32d0e | -2.23025 | -48.3663 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c2987a04-736c-361f-84a2-8a33b14fe285 | -3.23902 | -50.25712 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e49dfa6c-bb95-3525-9016-cf64e602ade4 | -2.23777 | -48.37638 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5adf150c-fd74-3dc4-bf4c-44379682f2f3 | -3.58821 | -50.26468 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d1b1622e-1766-3531-9ca0-2976a030c99e | -4.21725 | -48.54122 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fae54d73-0fdf-3927-9d02-acb9902543b5 | -2.53736 | -47.30371 | 2024-11-09 05:33:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 683163d2-e26b-39c2-852b-7800cb601437 | -3.63796 | -50.18402 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 319899c7-5ea4-379b-8bb7-8a5789b8d66c | -2.63562 | -46.76586 | 2024-11-09 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| dc273dce-7064-30ef-9ffd-bfb39b5a4097 | -4.21385 | -48.68452 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a9ecb3d8-b995-3064-996c-920bdfa31d6f | -2.51339 | -47.46501 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90a3d67f-c272-390e-a45d-d5a0ab564be2 | -4.6154 | -49.57892 | 2024-11-09 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2e02cef5-d32f-3bc5-9316-765e971ed8dc | -3.19018 | -50.58155 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc551647-b3bf-3809-b043-2f2bd9083f9d | -2.39469 | -46.77008 | 2024-11-09 05:33:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2795bbac-b922-350c-ba20-bdfe4da02ac0 | -3.11266 | -45.33626 | 2024-11-09 05:33:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| db001fe8-a80b-3b82-95b4-e874165a4309 | -3.95553 | -48.99464 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8c73a271-7f31-3b20-826c-2cf635f069d3 | -3.08282 | -49.57243 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 56ea73f9-854e-3092-b6e1-a30ed7e232f2 | -4.29287 | -48.64883 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b314443c-5e68-3739-907e-93cc8b0e045c | -2.39329 | -46.77938 | 2024-11-09 05:33:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1b19e879-c283-332b-8ec0-d20433aafe18 | -2.10799 | -51.09191 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9190b96b-bfeb-30f9-9dca-dd3b9eeef0e5 | -6.17827 | -45.44147 | 2024-11-09 05:33:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a5a53659-ca6c-37e8-a441-e6eeef7a8e48 | -2.89154 | -45.38249 | 2024-11-09 05:33:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d5cc5fee-ced3-3117-82c7-eaf6ab07fdd6 | -3.60444 | -51.24176 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c5d4cd1a-beea-339a-97d1-a0051e0080bc | -2.8824 | -51.46753 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c638e30-1b08-321c-9e07-7b949b86a042 | -3.0359 | -48.0396 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 925bc424-056f-3cbb-8545-18e8ef703c7c | -4.25392 | -48.53758 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |


[Clique aqui para ver as próximas entradas](README115.md)
