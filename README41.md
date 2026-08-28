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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a90705-adf3-3838-99ed-3b3809233b26 | -13.43693 | -51.85713 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7b419ad-9399-319e-b13a-4e3ccd112311 | -9.66879 | -55.07719 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96121eed-0df4-3bc3-b597-60c36e2bb2e9 | -12.2844 | -50.59815 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f56c1b6-715e-3407-8cfb-40ad81ba5c00 | -11.72618 | -54.546 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07fd34bc-959d-3748-b8f7-496ea4f59b7a | -9.46384 | -51.72002 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 410b8326-ce9f-3bd8-bf1d-a7a3bd390773 | -8.60705 | -54.71981 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eca5b8ac-0e22-3349-bcb3-699b4a5ccb03 | -10.75862 | -54.04224 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7ab16de7-8d75-3e7d-85a0-7ed649c643f5 | -10.98827 | -51.08848 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0883ac49-dd06-3ca8-a994-dcddbc59b5eb | -12.50707 | -43.80674 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9675d933-a55f-3a7c-9ac3-2477ce0382d0 | -11.73364 | -54.54734 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3125375-733b-34f3-8ee1-4783dd8a69e6 | -14.8756 | -52.5923 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91ac20c6-2fdb-3fd1-a358-eca862d74d29 | -14.15239 | -52.82526 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4435c137-baab-352e-91e5-879d0d99168e | -9.21927 | -51.54634 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63948a79-d7e7-3708-9550-d1f39eb0e212 | -13.61532 | -51.84633 | 2026-08-28 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcbc8627-2147-3884-a533-9d18bd7eec6b | -12.26222 | -50.58729 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398751c1-45d4-30ae-bbb0-e095cfb0b2db | -9.403 | -51.64301 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b96a0db-e58f-32a9-ac76-628e11f9aa8a | -11.0135 | -45.07332 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 918ee5b2-550b-3f99-943e-4f8ef38cfaac | -8.0483 | -54.04049 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd224c42-c603-353e-95de-1b25956d1ec1 | -9.08014 | -53.0403 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b1b99de-0e98-3528-97a2-6dc903fd7d62 | -6.77735 | -55.6897 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30e36bd5-0f11-34ee-bd2d-83dfdee78f8c | -11.27586 | -54.03002 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 263607c8-77fb-3894-8c29-84aec241b26e | -12.42323 | -43.41015 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2663a1d5-7c2f-35fb-92d8-afc760f1e4ed | -10.06413 | -46.94335 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00946212-75b8-33c7-beff-f103b81caa13 | -11.73672 | -54.52931 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2261cb93-91a6-3979-82b7-4b6095d9d13c | -11.64202 | -46.7442 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83f591d3-1f74-3a83-b7fe-205e234045fe | -8.95523 | -50.17003 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38857aea-8936-3587-bd42-ea372a30f9d6 | -14.88507 | -52.59771 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9c6dcae9-f47a-3d05-b7ad-225083cfbf1f | -11.773 | -47.63237 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6022fedb-f069-3ef8-804e-1462d0099cde | -8.81106 | -50.07857 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78b400a7-e271-3a53-b9ef-e0d53fe2bb66 | -11.77286 | -47.65811 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59568524-dbbb-386d-9ef6-904262a765ee | -10.79463 | -50.64585 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0b90cbd-82ef-3c5e-9455-91fb840473af | -14.29708 | -51.73264 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9147e44-e2fa-32ea-ac0f-26fa287b1345 | -9.22544 | -51.55109 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb1d1926-a73e-3310-8482-f7fe340ade09 | -12.27609 | -50.58592 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e752f2e-0b9c-3d77-b0e8-17eccac25e3f | -8.58909 | -54.75291 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5ef5fd7-5618-31d8-a0b5-574465885820 | -10.49443 | -64.50014 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f2e1c98-4394-3dff-91f3-d53cad69cfdc | -12.79152 | -46.45205 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f5c34f0-4e8a-3fbe-afee-716186f46913 | -14.88843 | -52.59829 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8250cf0a-d235-330e-b4c8-05bcbc06b4b5 | -13.42518 | -51.86618 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5db8e8f4-9d14-3ff4-bcb5-7303d976f3b3 | -11.72541 | -54.55052 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26867d89-f8ce-31ae-8a4c-689b49a01fda | -11.29484 | -54.02893 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7a20a549-81d5-344e-922d-e643e63a4217 | -14.5533 | -51.97025 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd26fc0e-b337-3586-8b11-a65b90c12475 | -11.81595 | -47.21502 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e1af968-1ff4-389a-8799-dd53402d46f5 | -6.82322 | -55.61209 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cc7fbb4-743e-38aa-8d99-fd1b512556fa | -11.7195 | -54.54014 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0839cdf7-ee46-3879-a981-79fcd9630f0f | -10.96108 | -50.29794 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c529d8-dd71-3708-9f37-affee7d43cec | -13.32556 | -48.1976 | 2026-08-28 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60619c23-e457-36d2-b971-817bd0ed149f | -11.17139 | -55.82128 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66a4be31-0c90-32d9-9114-303e454c09fd | -12.24393 | -50.57343 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 86d9be7a-13b3-31c0-8f32-cd8981039d77 | -11.65539 | -46.73198 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f676a9d4-9f2b-389f-8050-27bd417ab2dc | -8.95355 | -62.39571 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c158037b-ad24-3d18-b25a-b9dcd8f7f93a | -11.81354 | -47.20564 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fdc475e-92f2-3bcf-826a-f99c3c19d015 | -9.61456 | -55.11903 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 51194b4b-7469-39e8-b0dc-9b5e32b0a7bb | -12.28218 | -50.59054 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83f3a7d0-7f31-39e3-a12f-07093d5c6591 | -8.79611 | -50.04399 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a46c64-d0ea-38ae-91c0-89057fa038f6 | -8.78449 | -50.07431 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e819eadc-2ec0-3c58-8fee-5cafb3e39340 | -8.23399 | -54.96988 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3ad2848-1dc4-3908-a041-9801e0e4a3b4 | -11.28463 | -54.02264 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e18c22f-5c33-3f74-a5f2-05b887cb9e84 | -8.01277 | -48.02205 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e70af0d-d7bb-3875-a7b9-38aad37e09f6 | -11.56863 | -45.50555 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42126385-d0a7-3bae-9f62-3de0490c893d | -9.40359 | -51.63936 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cc59a30-080c-3c3d-a1bb-c29f4ea37365 | -13.2832 | -46.63492 | 2026-08-28 04:51:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fabe1ed-0349-35d5-9f01-aada21484b2e | -11.83137 | -47.21299 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca205e3b-be39-3a1f-a27e-bc7a502f0679 | -9.23335 | -51.54501 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75650549-afab-3cb8-a01a-8c2fb7f0ae06 | -9.66269 | -50.82916 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e671a6a0-9777-390b-af81-6749e74d0a69 | -10.53408 | -50.77613 | 2026-08-28 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 990496fe-64bc-3e07-bf3b-c00a1ab43899 | -11.56915 | -45.50176 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1e47d9-9a03-3c91-8efc-378d198de88f | -11.27733 | -54.02139 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a935988-2bc1-3218-b87e-c88b62e47323 | -12.43686 | -43.41716 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3820e752-e6f8-33a3-b90e-9d128dc2d3bf | -13.37401 | -41.3517 | 2026-08-28 04:51:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 216b1a3a-99eb-379d-9579-b31cc03b4147 | -12.25945 | -50.58321 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d896ed2d-6266-3b28-9f96-ae4cc16aeb2a | -11.49292 | -45.11258 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5577cd3-8cd5-3d93-8823-7c60d866c9f2 | -10.80018 | -54.01145 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 583e9a29-cb6e-3457-a930-61fb096ea3c2 | -12.01938 | -47.16835 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5549c96-93ca-3049-ae2f-8740271efe7d | -13.40326 | -51.41291 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0efa902-14a7-3e89-a68f-e70cd44545f3 | -14.87512 | -52.63756 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f27314a6-d722-3501-9a87-26d7392dc452 | -8.81051 | -50.08205 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2965e707-06c2-3f30-bac4-755839fb0fef | -11.62159 | -54.59038 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 31774689-3852-3788-ad13-5e9c69567060 | -8.32833 | -47.63062 | 2026-08-28 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0190f49f-bf63-30a6-b419-a6968222310c | -10.9206 | -50.53285 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a4197c1-bcd0-394f-a9be-d8da21cdf7e3 | -11.57221 | -45.50985 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38f5fb43-efde-3724-9ebf-54b0aa97f113 | -14.41894 | -52.58629 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 652aa8fc-5382-3fa7-8d29-b55f3cd17295 | -8.80442 | -50.07751 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff344b13-3cbd-322e-9585-39c9f0593da0 | -11.27513 | -54.01216 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f58a3ae-1796-3839-bc51-a90494d41d3d | -12.43754 | -43.41203 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29826a51-9f29-3159-97e8-b1e71658bac0 | -10.8457 | -50.51732 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49352e82-fbbb-3083-916e-e0ef84aa65d6 | -10.93666 | -50.53905 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 17d5d92c-ab0e-32c6-b7ea-db2d196163f1 | -8.99679 | -52.38925 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e06aa13-c50b-3543-96a4-4fb624c79704 | -11.23427 | -54.00948 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c55867e8-cc72-3f00-b470-c3f591dd230d | -11.2063 | -55.09472 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1492d26a-587d-3f6c-a48f-a98a975f2318 | -12.29105 | -50.59923 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fb6dc4ca-323f-3024-98c1-36f00add0dd6 | -14.92107 | -52.59588 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dbfac49-e6a3-36d0-bdf1-dff33525d594 | -10.55321 | -50.48422 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad0c1fd-305a-3610-a7fc-499cfda0e5e2 | -12.27276 | -50.58538 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8fe43b86-80c1-3710-92ac-4fe837e334f4 | -14.58525 | -53.16797 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e45bf6b7-1005-39cb-a274-c63ba9e0952a | -11.33897 | -48.38696 | 2026-08-28 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526ea8a9-339b-3ed5-8eb0-410451a876b0 | -9.16078 | -49.96299 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e19335f-3865-3a9d-8558-6e3083856752 | -13.42168 | -51.78869 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d672ceb4-a79c-374b-ac25-510e07631f9a | -11.81048 | -47.20066 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c94cf12-b296-3332-982a-6235c547123b | -14.96313 | -52.59193 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
