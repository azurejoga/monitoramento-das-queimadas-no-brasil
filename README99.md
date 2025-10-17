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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 375b6af1-2923-308e-9726-1d152622329b | -11.48692 | -44.20679 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61aee955-c0bf-3b12-b763-fcf9e1a9c6be | -8.40276 | -46.2304 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f3c3762-10e7-3166-a698-b432fdcd2f24 | -11.75633 | -61.07384 | 2025-10-17 04:51:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8a6d5ed-f362-3d7c-94ac-8742a53dd9f3 | -10.5066 | -43.43517 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6d4bf59e-a007-3afe-8533-a929b1516602 | -12.41971 | -51.30486 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 033ff6d1-f01d-35f9-ad7f-75fce0cd54b6 | -10.26475 | -44.03451 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e19914f5-b25d-34dd-8078-6d8c5d04f31b | -10.27535 | -44.03031 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17f4b18d-c317-360d-a8bc-f12bb74bb236 | -13.24044 | -47.10683 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f7f0d9f-dbe5-32a2-854e-f38044f25516 | -12.31905 | -45.6412 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d7c1f05-55cc-3069-a76c-6fb5f89ac27f | -8.45531 | -44.18068 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 159b96e3-9e16-3cee-8480-eb1546384377 | -11.46275 | -44.04037 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8edc34f-5000-3737-a939-843e1eb30359 | -11.45618 | -44.05185 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a96d3ec-8d83-3116-8aed-cbc974d39759 | -13.74039 | -48.21423 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75aa8ecd-b79f-3b51-a70d-be7f4f3d59f0 | -13.44462 | -47.9626 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3df9ca5a-4035-3573-86ff-6dc46534c14f | -10.16136 | -44.54203 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ef2a621-31e6-3fd1-802d-f2b465810b0a | -14.9192 | -46.73415 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed18eb36-62c0-3bfa-9f9a-e2ccf1e654be | -11.49619 | -44.05735 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1540a50-d66c-3a12-84c9-e26f20b297b9 | -15.03964 | -47.31299 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33fef95a-3a5f-35d9-beaf-4ae3a85835b9 | -8.26259 | -44.06837 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af5b0531-3108-35e1-b1ed-5876d0176767 | -13.42879 | -47.96032 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 539257a0-8179-38e9-9ecd-8faeb0ca4b0c | -8.47219 | -50.10162 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 903625e4-35f9-3da9-8ae7-4a602d51af7d | -11.39032 | -44.20431 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 384d7b52-ecb5-3f95-a479-f2e9d6eafcbc | -14.92517 | -46.72267 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83fa295d-ece6-3dfa-b83e-735f503fea02 | -9.07517 | -45.91055 | 2025-10-17 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 805e15ed-364b-3e58-af45-cbe09f64c6f9 | -10.50666 | -43.39428 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2e10297-c865-3e7f-9c46-271ac9febca0 | -9.50021 | -47.27206 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2706ae0b-cef3-3e21-a4a1-e9fdfccedeb0 | -10.11999 | -44.56242 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2c27506-fc1b-3f85-beb0-dbcd9b6000f8 | -13.43272 | -47.96108 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72ccc628-7697-3372-8876-aa418f33c5e9 | -8.82444 | -50.05452 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53030e19-015c-36e7-8e54-1d418cba8520 | -13.23942 | -47.1143 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d28c18a-73d3-36d5-a8f4-3ca8267935de | -7.71388 | -47.84587 | 2025-10-17 04:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cd58112-09ee-34ad-a103-43a2a93a9223 | -12.31062 | -45.63523 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 949f5c2b-6a96-369d-9028-80768833818f | -7.72129 | -47.84697 | 2025-10-17 04:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1945ce65-9f67-37e6-921d-2588d0daa22c | -10.12293 | -52.34702 | 2025-10-17 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1bad461-c805-3c02-a8f6-28d469ec7bb1 | -10.51069 | -43.40369 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faddaedc-01d1-32e4-b35c-d634a73306a4 | -13.45554 | -47.94226 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70fca499-7462-3071-a83a-3bb4853c14f1 | -8.41145 | -46.28694 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c1da4f56-3f4e-3b65-8887-eaf956794374 | -8.61974 | -54.56236 | 2025-10-17 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12cc314-6483-3bb0-b312-01ac3b5b91d8 | -13.75549 | -48.22048 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78ce3063-425d-3f60-b98b-2793a459e7cd | -10.53596 | -49.55147 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f637f1b8-6485-3af6-ac5f-de90da06c8e4 | -8.38417 | -46.24279 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d2b2a72-10bc-3b8b-9581-5aab8287bb3a | -14.34764 | -51.44266 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebea17cb-e034-3977-ab26-deb0e822951f | -11.51955 | -49.1454 | 2025-10-17 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a26862cf-5a9b-3da3-b582-ae6c6ba4f65f | -10.26555 | -44.02868 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1af6fbb9-d131-3420-8067-c83d07e26e9b | -10.26109 | -48.82812 | 2025-10-17 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c8bbe68-8e2a-39b6-ac61-83028b8bfc78 | -8.37044 | -46.25069 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bb77491-5842-3c08-af01-e5a845abe1e4 | -10.29526 | -44.03937 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 1f883e5a-8897-37d6-a4d6-f8060c39ff44 | -8.25865 | -44.02581 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49e82b72-52fc-3ec7-b151-ef77405851b6 | -12.30773 | -47.25616 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd4044c6-d568-3878-949b-53e4b4150e95 | -8.26048 | -44.08385 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7de1410a-511f-3567-bc35-461719d9912e | -11.40589 | -44.20071 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc98ff4a-66ce-3b68-a61d-a4942a8d4191 | -8.82523 | -47.30468 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23c28b6f-4d32-39f2-a932-806a55cc06c6 | -9.10028 | -46.67066 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cd7d16b-7702-34f0-9034-c2da0c804e6d | -12.37655 | -51.33886 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eac52d9-7089-3267-98a7-af8945355464 | -9.50449 | -47.26932 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc482c17-90e4-3e98-b156-9dc3fe7701d3 | -10.647 | -45.24689 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1550e0ff-ed4a-3d86-83fd-62f239d1a663 | -10.98249 | -47.91096 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5fc77f8-0ca8-3ab1-baa9-40bdc5e5e2bf | -9.88409 | -49.11995 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23f25f67-3ac5-3c2b-8697-f496495ca029 | -9.13779 | -46.64002 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ddf8358-3c30-3b29-aae3-334fd208cb96 | -13.38925 | -47.21699 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f75664f0-b06c-3108-bce5-f9c7bad8b9f7 | -14.33293 | -51.42508 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cabda12-1359-3cb9-b805-7191aee547dd | -9.13831 | -46.63644 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0f3cf04-9d99-3eee-ab21-729abb065323 | -8.38828 | -46.24351 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eeac55bb-4a28-35d9-b24b-96e553642d0a | -10.6159 | -42.31704 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f973d1af-f499-33d7-871c-9a2a2f913b46 | -14.34256 | -51.45325 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c63e6a31-d046-3e9a-a1b9-7a3a908c3d7f | -13.71278 | -40.99017 | 2025-10-17 04:51:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 91b45b02-3c70-3845-94a7-3245c07a6e42 | -9.24825 | -44.35562 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c12c45c-1fa2-3d85-936d-e2614c98fa9d | -10.28029 | -44.03091 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8326d54e-61a3-3167-9a36-e765df070f83 | -10.72659 | -47.58203 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d54033d6-5917-332f-888e-4047f810bef5 | -11.39872 | -44.21685 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ece65fe-999d-3d64-8c57-bc3d58dc0549 | -13.44885 | -44.28825 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 542b3e96-bd14-369d-9dca-93410b94ed2b | -11.36029 | -45.2692 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73420cd1-d48b-30af-8f67-385275f8887c | -10.15658 | -44.54168 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94986088-ff95-348b-9ead-8133935d8347 | -10.36637 | -51.57684 | 2025-10-17 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52d3fbf3-7db8-35e3-8a4e-f085c46ce38f | -12.04626 | -51.37587 | 2025-10-17 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a55dc4-8744-384c-b91a-6b3bc62ba2b5 | -7.94614 | -47.8099 | 2025-10-17 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c2d9f64-7cd0-3813-a109-1f2a15094e44 | -8.38565 | -46.32073 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bba0c39e-5b75-3fc7-8447-aa8663570ebf | -14.93074 | -46.71434 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 493b59df-f69d-35a1-997b-05f2b3ee0bfb | -8.1555 | -47.98078 | 2025-10-17 04:51:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f551a977-12ac-312d-b331-d7365f5d7507 | -10.26498 | -44.04109 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83fd067a-3b82-3c53-b143-5453787060f7 | -9.88265 | -47.67895 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f71e1b2-17f4-357a-aa16-28fd976789b8 | -10.50775 | -43.42627 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3f0f8d65-2b6c-3f0f-8d5f-296447c1031e | -12.43684 | -48.70663 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 891e8e93-d259-3ff4-af4d-d0f08914c186 | -10.57525 | -44.53342 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dedc667-5888-3d23-bc1d-0b4770f8b94d | -9.88456 | -55.91221 | 2025-10-17 04:51:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3b1c7b60-ce3f-34b0-8acd-f464f73134b0 | -9.2421 | -44.36507 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9e3dd62-8134-3938-a6f1-34786ab741ed | -10.27979 | -44.04274 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c87abebf-0952-3eff-be93-490f290d3ed5 | -9.09873 | -48.91489 | 2025-10-17 04:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 935fe1c7-b877-3733-8f95-c85d92a58fb1 | -10.14299 | -44.53488 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4413df97-0f46-3b15-b7b7-f483e1931d4a | -12.31842 | -45.64579 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ff9ec72-2a48-3ee3-8921-1b704f8a2d3f | -10.52573 | -43.36889 | 2025-10-17 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7efc4486-7d32-3329-bb24-88d23eb43d45 | -11.45578 | -44.21396 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 701ca088-5bed-3813-b49f-61e366472234 | -9.71354 | -44.54856 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00b78a3-3c13-3e5c-a46b-ce31bb26fae2 | -18.47293 | -46.54419 | 2025-10-17 04:53:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb6ec453-cf9c-3062-9419-ff7c44be6592 | -18.09369 | -42.4472 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 354868e4-c502-3470-93b2-d601d86cff08 | -18.38134 | -55.46069 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 487e41e5-f6df-3988-aa02-3321acb09f0d | -14.86986 | -52.44099 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0054214a-e732-3661-bf77-51a0b55d3649 | -21.43346 | -54.15992 | 2025-10-17 04:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9354779-1405-3e0f-81dc-c58fdbc6e8fe | -18.33292 | -51.6925 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d9068e8-647d-3bfb-824a-d13d42b6b343 | -18.27139 | -51.30576 | 2025-10-17 04:53:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README100.md)
