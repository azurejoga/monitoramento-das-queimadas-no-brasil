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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e5717a5-2c3d-3354-a069-cb111dcacabd | -14.55783 | -48.8183 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e513517b-0b8b-3406-a9c4-32aa745b3e7f | -14.5572 | -48.82158 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2bcb47fb-a936-3016-a53c-458df4b430e8 | -14.55655 | -48.8249 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a5ab4ef9-bf2d-3253-8d22-e3a478ebadc3 | -14.55239 | -48.79201 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 532640a0-eaed-38c2-bb93-922eb494e1bb | -14.55205 | -48.82089 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb70742a-87be-3085-b7fa-8371535c08e9 | -14.55143 | -48.82411 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c65890f1-f537-3de7-b6ed-e37d1a8769b3 | -14.55132 | -48.79754 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3e4fda6-46f1-3813-b1a1-59ac40621f6a | -14.5508 | -48.82732 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3e48236-265f-3ec7-a841-7b4b85ed48b0 | -14.5507 | -48.80071 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8897c9b-5aba-36cc-a2c7-ee7fbcf1b5f9 | -14.55007 | -48.80394 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f04d99cd-55a3-3e80-8cd0-8027d165037e | -14.54943 | -48.80723 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d94bb199-e6f8-3890-8ca5-1937ca7f6cd2 | -14.54879 | -48.8105 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d24f1e37-76bd-3eac-8f4b-5dcc275a4212 | -14.5484 | -48.78545 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 808ed1f9-d4e3-31c2-bc7d-55526253b4f0 | -14.54784 | -48.78831 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bf8ff80-2ff0-324a-8e41-fd698ea8cad1 | -14.54733 | -48.79097 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a94bfcb-42dc-388a-883c-b8d03da7d8ea | -14.54691 | -48.82018 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a28c39e-70a5-3027-a261-ed9be0f56129 | -14.54625 | -48.79649 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3fc9e9e-5e01-3cbf-a89f-a3ed5fbe2204 | -14.54562 | -48.79974 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 690f5d8b-89ed-3037-a5f5-024204c8c3a5 | -14.54335 | -48.78437 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bed0eed-5db4-3d00-acb9-e2d4661f8e9e | -14.54279 | -48.78723 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3797695a-4467-33da-a505-085caa0088dc | -14.54225 | -48.78997 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33b04656-a43b-3655-8c2d-be1ecb6e45ac | -14.54172 | -48.79269 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f640a9d1-4faf-3227-a090-14ab15c81ae8 | -14.54124 | -48.82214 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8a3217-5294-3945-b569-81e686cdf24c | -14.54117 | -48.79549 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9eaf40d-b9fb-3c25-9652-691bdfab21c2 | -14.51258 | -49.26815 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea0aa9fc-1e28-3e04-8ab7-3038c020da71 | -14.50824 | -49.26794 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31c04400-9c0c-35c4-a4d7-4a62f84e8725 | -14.50765 | -49.271 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a443fe5-cd28-3002-8cdf-8d313d89a771 | -14.50726 | -49.2675 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef0db412-626d-3acd-801b-95b73de06c30 | -14.50664 | -49.27057 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e1fe5d1-fbef-3a5c-81c3-f77e8c15d61f | -14.506 | -49.27378 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e491ac0b-3e63-354e-af67-fc30a2c81ffb | -14.4802 | -49.27216 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ca6309f-b243-3ada-bd24-e69812d4ad09 | -14.47957 | -49.27539 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e21950c0-f74a-3313-89c8-6beba6804ca8 | -14.47894 | -49.27859 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb27b4af-4880-353a-8178-e47a0fb839d8 | -14.47497 | -49.27106 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2d5db7f-cf72-3809-a14e-f79a6ac6c274 | -14.47433 | -49.2743 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c00e1a16-3e83-3315-8a84-975da9dde7e0 | -14.46907 | -49.27336 | 2024-10-06 03:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef299c64-d7f4-3b79-98dc-59870393f278 | -16.17496 | -49.26027 | 2024-10-06 03:55:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d7e09a-aabd-3370-a9bf-be32bc64ec13 | -16.16981 | -49.25964 | 2024-10-06 03:55:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7f725a1-aab9-305d-8ff2-e84aeedc212d | -16.78675 | -49.19097 | 2024-10-06 03:55:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a21efa1-92a3-382c-83d0-fca81e996dd3 | -16.78663 | -49.19436 | 2024-10-06 03:55:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b79547a6-3229-3308-a654-b4017af99bbc | -16.78179 | -49.18978 | 2024-10-06 03:55:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02dea9f7-0b0a-3dcf-955b-e70dde2f844e | -16.78165 | -49.19329 | 2024-10-06 03:55:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d45689be-e1b2-3e7e-9ff3-094180e03a9b | -11.89752 | -50.1129 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dacb52b-f4e3-3870-ae9b-0785f5b29b00 | -11.8967 | -50.11703 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3012fb7b-797e-3b3b-ab4f-d7d6c992fb59 | -11.89173 | -50.11171 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72d5fed3-7ebd-3842-98e3-8163ebe6e104 | -11.89091 | -50.11585 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcbe9e9a-f258-3e4e-b8ad-665cd7e2d3c8 | -11.88099 | -50.10518 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 431559b0-3b84-3fd9-8931-82b716948fe8 | -11.88017 | -50.10932 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b85c741b-f5f5-3887-a1b3-b89bd396cca8 | -11.87108 | -50.12472 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 654f2724-fc9d-3daf-b1e3-6de84351b581 | -11.86447 | -50.12767 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f67005f4-0cf7-3362-a5c4-d4b90fba1eca | -10.97013 | -50.15517 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52c27135-8ed0-35b3-b709-77e18f97be09 | -10.96802 | -50.15308 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58fd4a0b-436b-39d4-857c-914850ccb30a | -10.96716 | -50.15741 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d7f64e1-c0de-3dc4-b515-31cd71d15e39 | -10.96424 | -50.15394 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05b5f077-482f-36be-9b4a-e97937debb46 | -10.86322 | -50.13773 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9d6e0d9-dcbb-3b7c-925c-ec72108e294a | -10.86039 | -50.13768 | 2024-10-06 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc96361f-7b3d-354c-9f56-b11a99264142 | -13.26669 | -50.62529 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a90975e-cc62-3dac-b431-e165cb7d1fc4 | -13.26531 | -50.62547 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9afbc0fa-d258-3183-833b-25cc9365eafc | -13.26087 | -50.62401 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62b74089-bd36-3dfd-99c2-e6ea663ac30b | -12.77684 | -50.52851 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bcd1047-742a-35c6-98c9-2e2a618c23f5 | -12.77186 | -50.523 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4daae302-c77c-30a7-9095-93c14fc75103 | -12.771 | -50.52727 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54d84198-73a8-3961-bc75-ad946189662b | -12.76582 | -50.55289 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6560243-ceb1-3f75-8e33-22423f7e80cd | -12.76516 | -50.52603 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7713ebd7-93a8-3ee9-8d68-1cd2670231a7 | -12.7643 | -50.5303 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c901d6d2-25ee-3f99-a815-6083e9197107 | -12.76344 | -50.53456 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c92f97d-05c5-3216-9607-f89c33a78a9f | -12.76236 | -50.57001 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4a341b3-d2d0-38b5-8a4d-52cadfffb173 | -12.7615 | -50.5743 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c5216a-5dd8-3acc-9023-154f3e07eca5 | -12.75998 | -50.55164 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38a585bb-c3fe-3e57-8d7b-5162f58c1ce9 | -12.75911 | -50.55593 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea7139b2-a71e-3d06-b208-bcbea9afd56a | -12.75846 | -50.52906 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e7f46f0-8c28-3ea0-b63d-d931ccaac2f4 | -12.7576 | -50.53332 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4fb2b97-d77e-34f1-a46a-e21ef7056891 | -12.75673 | -50.53758 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68fc1d77-9f43-3064-af3a-4a63a5731687 | -12.75586 | -50.54185 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 635bd1bc-a0e8-3f64-a7ac-69cd8c75254b | -12.75565 | -50.57302 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5058ab06-ab6f-305f-b88d-d01892b456cf | -12.755 | -50.54612 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eca3a80-87e0-303d-b94d-b9d5a03a3bc0 | -12.75485 | -50.52837 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3309b75-7ddb-3e0d-80cc-344db8d0403c | -12.75453 | -50.60875 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9809e2c5-f3aa-3576-b8e8-3fd4a2d2abdb | -12.75401 | -50.53265 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be26960-1d7a-3e70-b1fc-b513ebf85abe | -12.75366 | -50.61305 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bf29a1b-1aa5-3c11-9446-0bbc5c28f7be | -12.74866 | -50.60748 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce7b64f8-e58e-3288-a599-fdc70a91fd1b | -12.74778 | -50.61181 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a624da9-b95d-32eb-86ed-85d549c8ce2f | -12.74562 | -50.5755 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 754ea96d-aa9d-350c-8d54-78d3289efd0e | -12.74477 | -50.57982 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0b7da27-1b1b-34e5-8dd0-9e7dd3ab0af9 | -12.74393 | -50.58414 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5b619daf-6280-34df-ba4d-21395035035c | -12.74367 | -50.60192 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59dc0374-580a-3720-ad31-27ec72c041b4 | -12.74308 | -50.58845 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 05485f5e-f2de-3420-8204-28428b659833 | -12.74223 | -50.59278 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36473940-dcbc-3792-afe6-9caa64ee37c7 | -12.74138 | -50.59711 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 548c71d3-d110-39bb-b546-85ad3ee01f04 | -12.74054 | -50.60143 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1676b39-ce6d-374d-953c-d1ad97a7f3cf | -12.73722 | -50.58718 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 39cc364d-d424-34f6-a8c4-f8b5183c97d2 | -12.73637 | -50.59151 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 77bbacfd-0cf7-3545-9ace-93020d5493b3 | -12.73552 | -50.59584 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 72621d05-7a24-3559-ab4c-ef8aabe88a9c | -12.73467 | -50.60017 | 2024-10-06 03:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 970c71c1-adc4-30c5-a775-e6bd2f4cc988 | -13.68667 | -51.18681 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc4bb0c6-15df-3f7b-831e-6ba4bb8e9026 | -13.68147 | -51.18736 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd63237d-df23-3fe3-957c-327ef7fd40d5 | -13.6807 | -51.18549 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d5b3df7-d672-3199-a06e-65cff8eb882d | -13.68052 | -51.19189 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8624e07-917e-347d-98ad-e78f10d95c58 | -13.67978 | -51.19003 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6c1b781-d0b3-3a5c-abec-df03df52495c | -13.67957 | -51.19645 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README56.md)
