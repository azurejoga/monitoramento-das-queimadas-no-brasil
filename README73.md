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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d13d25de-aecf-3a2d-9709-87780ed3762f | -14.21462 | -46.08451 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1e66814-f6e9-3b4f-abdb-21c47c4b17c5 | -13.19511 | -48.51674 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdc1ed4b-2d0b-39d0-a152-c36d838616a4 | -11.16003 | -47.1815 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc376beb-5c54-33e0-9c71-73ebae3b0c17 | -13.77172 | -47.5527 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddc76715-d9ec-3b97-9de1-aede67c3e0d5 | -11.81293 | -45.03102 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fef33d62-0aae-3594-9a8d-e7ce447adcf3 | -13.80375 | -48.05118 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 384fe494-c68e-3fda-b529-8b125f014ecb | -9.06096 | -46.65315 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f37b899-35f3-3cfc-8546-348ecdf2f6e9 | -12.68749 | -48.54431 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51697160-bd41-39c9-b4de-b7b816f9bc63 | -10.11129 | -50.27205 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2b6ed72b-7841-388d-a7ea-8083e1c1c9bf | -9.92594 | -43.77312 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b7ac524e-bbf9-31d3-9e6d-8f198442f4d7 | -11.45014 | -42.23216 | 2025-10-03 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bb771dc7-126d-31f9-84cc-b75ea0d74387 | -11.14632 | -43.3814 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 753184cc-867b-39bf-b3ea-67978d0dca36 | -13.08784 | -47.08361 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26b3ee65-6f97-3e02-acd4-0a73641e79fc | -8.90969 | -45.0414 | 2025-10-03 04:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b53f2e7e-3f5a-3826-9625-98f03dadc8b0 | -10.88987 | -44.27354 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7bcf021-6e37-3d5e-a7df-f74b9bfbe71e | -11.43243 | -43.49378 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41880b74-338d-304a-8b92-a2e0ea08e439 | -11.85295 | -44.96194 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cde4fee4-f846-322c-b0c8-8d98e6b74c08 | -13.39993 | -42.64622 | 2025-10-03 04:12:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 106373a7-1f0d-3efc-a7c7-661862e72b14 | -8.5336 | -47.24067 | 2025-10-03 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8682b282-9462-32cf-8513-e67587dcd3ac | -12.06413 | -44.86701 | 2025-10-03 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535e47fc-b12c-3619-ac22-f9e10393963b | -10.21706 | -50.32357 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0019988a-29c7-37f8-b0cd-8c7ad04a6423 | -11.13562 | -43.40528 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c7b477b-601c-38e5-a579-6fc84de70d65 | -11.80795 | -45.01808 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7239a26-ad2c-38a8-bb1d-4949db115270 | -12.11108 | -43.44059 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3b58e4a-7e6b-3660-99bb-2de4c88c6774 | -15.08706 | -42.12497 | 2025-10-03 04:12:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d47a8f5c-0b8a-35c1-b9bc-4d102a9a4d99 | -9.90213 | -45.9646 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f6ed41a-9881-3dc9-a4f4-c60957cc7224 | -10.84095 | -47.21751 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 590103c9-ad93-38b3-9064-7cb5804031d7 | -9.76432 | -46.22638 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f394db4-f87c-36bb-84d3-fdb1cf380832 | -10.34519 | -48.18159 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddceba27-d3dc-3fa5-87fb-6f4e1832fcfa | -12.06003 | -44.87032 | 2025-10-03 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e485dbd-94ce-3a4a-be59-77c3586677c4 | -13.24484 | -48.49914 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f009753-2dca-3dcf-aa22-8cf2e84e318e | -13.79415 | -47.58283 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 659c5ce9-878c-3928-bba4-2e0c5925d74d | -12.62632 | -46.97789 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 51b7f45d-880e-3abf-a548-03d5aa905c50 | -8.37691 | -48.64804 | 2025-10-03 04:12:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48a68f3f-fca5-3de9-a165-8a4431933dd4 | -13.4752 | -47.23595 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92ef0da9-ae6a-352a-b2b6-4f3a04ac78d2 | -13.47247 | -47.23331 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60fbddc1-11f1-3ac4-9d8d-d8707d078b8d | -13.77065 | -48.03974 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b97ccd3e-c71a-3b8b-a5df-b471fd4ab288 | -12.2395 | -44.03131 | 2025-10-03 04:12:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 844510b0-295b-329a-8dae-aaae19f83c5c | -13.1397 | -47.8988 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e0e24352-11f6-3c62-a657-1eabda2949e1 | -13.3006 | -47.26231 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77cf5c12-c088-3356-a09a-ed936f5f772c | -11.59834 | -47.65511 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e5f710c-fcfd-3df0-bbb6-cef11fe14f6b | -11.64431 | -46.86215 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ab3083-8254-3f17-a483-2ad0b3b80b72 | -10.27902 | -44.3313 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc4ddc2f-20c3-3458-9bc0-1ae82ccc7755 | -14.31987 | -45.87046 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab24d3cf-efed-3ddc-bd8d-7f5eb333027f | -14.46171 | -48.4061 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2866d3b2-9a06-34c1-9366-4d689739a1bc | -12.37306 | -46.51376 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fac2ce9f-0961-3324-b022-57517e1f4c57 | -11.81338 | -44.90041 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a98641a8-2b22-38e9-a4ce-6c689910d8cf | -11.82473 | -44.91764 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 289b85fd-ea8f-3871-ba46-c5ba3b962517 | -14.20212 | -46.07925 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b7eab61-dc42-3d9d-a4bd-9116805a6609 | -9.91828 | -43.73438 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ab9bebc-c289-3fc8-97c9-56c9c1215fee | -10.34138 | -54.19153 | 2025-10-03 04:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a63193c-fe88-3e1c-b418-e22c59362f33 | -12.3826 | -46.52486 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9a092b2-c258-3416-bca8-c23b316da8eb | -9.94684 | -43.73553 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6378894-ee48-356d-b63c-24d2cfead09c | -12.62954 | -46.95907 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c826ebf-4017-39c6-ad0c-66b2e0da7efb | -10.00635 | -50.24104 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2589e002-3811-370f-b185-f83d0a3c84be | -9.92373 | -43.76525 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5183ae3c-93a2-3015-95a0-a9dee9e6da8e | -14.29127 | -45.89026 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d91e1c3-dfa5-3379-b807-748866f92c9c | -14.22735 | -46.0953 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79a0e734-fc8b-326f-a4db-8ba7fd44fee0 | -11.90702 | -46.30537 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2bdadf15-1b85-33b8-92d2-b42d5b6fe5c0 | -11.86424 | -44.97985 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6b2fe45-6a07-334e-aca4-85d7b626b06a | -11.76987 | -46.8287 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b86ce6c-34a3-3c98-b434-93132f6279ee | -11.90262 | -46.30892 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3af98894-4525-3750-80ad-20752762b803 | -9.44879 | -47.58763 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bde3291-8788-3f5d-b9f9-abfa7006287d | -13.18685 | -43.79695 | 2025-10-03 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1187d99b-a36d-3eef-ac97-566f2a9bc736 | -12.49935 | -48.00359 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2ab9248-5d51-3f5e-89b8-4a7db9ef0a84 | -13.20008 | -47.81136 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1811f46e-16c5-3be4-9291-0e7399bccf5a | -13.77242 | -47.52642 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f9ab711-5ca8-3514-b8d5-ca4e59aaaaa3 | -12.37522 | -46.52343 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3c943cd-2834-33a3-a1f7-e70884da34fe | -12.37382 | -46.5093 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0d30230-562c-3b12-b210-add25785ba55 | -8.90567 | -46.60529 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 800154a1-0c49-3980-9666-413db6292af6 | -10.84876 | -45.38013 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edadb1bd-6352-3585-b648-be8fbceac25f | -13.34398 | -48.10574 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e85e84c-ae44-3fa4-a097-3c50dedce78c | -12.2938 | -45.37495 | 2025-10-03 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d4ab498-8115-3b23-8eba-903bf2f9ace1 | -11.60218 | -42.87499 | 2025-10-03 04:12:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b78eda79-0a43-3686-9ace-661882ac7c3b | -13.96991 | -44.86314 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51a2251d-aac5-3700-a871-4b591e3879ec | -11.08595 | -47.87397 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 578bcbba-339b-33ac-84d3-d8dee8f177f7 | -10.76192 | -45.337 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 836ddc39-d6a2-3b7e-a0d5-fa42e9f3e7b5 | -10.91928 | -46.73685 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 156afd38-c17d-3efc-9b07-2c9f90c28bdc | -12.93434 | -48.43177 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4650a9c-33f4-36dc-bdd1-fecae95476b3 | -11.86986 | -44.98903 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f398b38-b012-347e-bba2-bb4f2e1ad468 | -14.42385 | -46.092 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8474772a-7dd5-3efb-ad03-5b0d42d5ce5e | -13.13954 | -47.83872 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc5771cb-2e85-342a-8b51-24564c23a8d9 | -9.95022 | -43.73609 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c87b5ee-e7ff-341d-8ffc-e31418b48b26 | -14.43983 | -46.37818 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45f065dc-4ee6-3155-9484-202e9abbf21d | -13.21425 | -48.52839 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbec6c53-90d5-3292-a544-f127fcbf379d | -9.05789 | -46.64762 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acaceeb2-f674-3e44-b19b-0ac9060d6889 | -13.5359 | -47.29105 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e29b53c8-45a1-316e-bd1a-c1bb57ef082b | -9.94785 | -43.75063 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64529c65-5386-3833-8974-c1e9f1005590 | -10.85752 | -47.2153 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fe6b731-de81-3f0d-b5e5-d8ff5c8da3da | -11.91517 | -46.28006 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 84909a1e-9c0e-3b12-a0ca-4177ed81516b | -8.88786 | -46.59198 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b5717eb-226e-344d-b649-65ca68745c09 | -11.83592 | -45.04312 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6147c0f-f042-3cfe-a089-c0585623505c | -14.23304 | -46.10473 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4f3befe-533d-3780-908e-6475694dcffa | -12.23113 | -43.76363 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56f6214c-85f6-3248-a932-ca3b018b42fc | -11.29191 | -47.83654 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adbddda0-40da-37c7-8f50-83fac0dbc840 | -12.643 | -46.88035 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57509577-efad-3655-b2b2-ee88b54dabec | -13.97978 | -48.16401 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e055027b-545b-3b23-aa10-65703f650c9c | -10.34859 | -43.73307 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c89e04be-1548-3abf-a1bf-52ef6c1ea867 | -13.28968 | -47.19064 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9acf8385-e312-3ed0-b0be-8c9a202d9af6 | -12.11386 | -43.44461 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
