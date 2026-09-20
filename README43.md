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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdb821e9-73cf-3dc1-af50-6e658e9f16b3 | -12.28689 | -47.12481 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 081fe97d-39d0-3de5-af6a-58f205680b50 | -11.86702 | -47.67085 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c847a7b9-6c45-31a7-99a2-cde9edb3a027 | -11.77404 | -47.43901 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b520101f-36eb-3374-820a-0f803051c4f8 | -11.88336 | -49.00098 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f818974-8cfb-31ae-beeb-1e43d26620d0 | -13.58385 | -46.94784 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55b90bb3-f31c-302d-a5c3-d5e45f2b3073 | -11.86786 | -47.67252 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31958bd4-211b-3ce0-8f19-a441ac99b725 | -12.56742 | -49.10567 | 2026-09-20 04:21:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a16407e-a72a-3199-b52a-6116c1432e55 | -12.87873 | -51.00742 | 2026-09-20 04:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 091f5d74-3d93-37ea-92dd-b88199c971c3 | -11.21644 | -54.08599 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d33588a7-cf19-377d-9221-4c6162f96f6d | -17.98506 | -49.20459 | 2026-09-20 04:21:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6f9b357-0e3a-3e5c-99ec-5bcfaf6ac0a7 | -10.90317 | -53.98095 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702dd0e7-8878-3c6a-b429-791f04f04782 | -18.3749 | -49.39813 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9c65540c-3e80-3b82-89eb-1f426e195f3a | -15.59315 | -48.0924 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d941cdb-104d-3a27-b725-569a5fc57181 | -11.39194 | -51.38567 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa21f6f6-da0d-30e7-bfcf-72c6bb3d7b77 | -16.95118 | -48.96811 | 2026-09-20 04:21:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892ba337-6c03-33d1-9950-8f56c1806192 | -11.03106 | -54.16278 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c81642bb-303a-3b08-bbd6-922a8dbbfbcf | -11.88359 | -47.65356 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bca38ecb-e959-3a41-b4d0-2bbd6c0a9ffa | -11.71407 | -54.56431 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9565705c-2ac8-3de0-b0c3-7d4e0f2f11c9 | -11.20595 | -54.07679 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65c4aa1-3986-35e3-b818-a82961656eea | -13.24927 | -51.74318 | 2026-09-20 04:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eae587a-5b06-3ffc-b1d5-9b1c0872d6f1 | -15.47702 | -48.42202 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d78cc703-1e81-32b2-9751-793a78b32e58 | -14.10739 | -44.83547 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6839c1a5-d7f8-38f0-8107-d42f57f4f46d | -13.01234 | -46.91998 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721014e3-9618-3ae7-8980-302985769429 | -11.20412 | -54.08617 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b485591f-fab1-30b3-81fb-3bac9687e934 | -15.86677 | -49.91602 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dbeeb9b-73ba-3418-8ee9-ec80fc42d501 | -12.53385 | -50.04082 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bca24afb-a6eb-3711-973c-f4ffdc0c3e09 | -14.59146 | -48.0974 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4701841-b91c-3eab-b941-e5c63a16800f | -19.1936 | -46.84052 | 2026-09-20 04:21:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4e6d945-1c41-3c22-bd33-11e43526da99 | -12.11919 | -47.02489 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 591a0ee1-0260-34d8-af54-d8ede55a3e44 | -10.87067 | -54.08246 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 227a1e1f-8232-365f-be8c-e953cb326879 | -14.67081 | -46.69044 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8058e1c5-de8c-3c58-92e4-a70c9d471d89 | -15.06032 | -48.58368 | 2026-09-20 04:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a63296bf-bd48-38e8-8c70-dd5e4339cec1 | -14.04152 | -52.08741 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b943af1a-a914-3cf6-a2a6-e618becbcd9e | -10.87493 | -54.09335 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3881b67-431b-33f9-9023-33bc1f3fd7ad | -11.41938 | -51.46483 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b302201e-51de-37fe-848a-729ac4175f1f | -12.87574 | -51.0083 | 2026-09-20 04:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00e7d6c4-19d2-3c55-9986-61216c5abd3d | -14.0466 | -52.08865 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f98e956-5848-3a14-8de8-d4648e60f2a1 | -11.12732 | -54.0255 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 693a455d-2ede-3862-83e5-eae62e9d6033 | -14.69042 | -46.68514 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a518ded3-bac2-3317-9b91-8b16f097a0cc | -14.05052 | -52.09589 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d0a96d57-0984-3a0c-9a26-84947b1be3d2 | -11.22 | -54.0698 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d780b0aa-d6f8-3238-ba0c-2cd4dfe197b9 | -15.48001 | -48.42806 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4925169-3d01-3d2c-b031-02c887bad62c | -12.12384 | -47.0208 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15d692f5-647f-37eb-8864-f7b79cad8312 | -11.41878 | -51.46798 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d00c6df-4403-3860-bbd6-7777c5c6a126 | -11.08791 | -54.03616 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f233047b-725a-3b1c-9f33-7486035ee2b9 | -11.12028 | -54.029 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a9e14d6a-a582-3401-aeac-aaa4f53877e5 | -11.21117 | -54.08258 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f744a903-d31d-3fae-a213-9bc8d2136c8e | -11.0466 | -54.1813 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a37c77dd-6457-328f-b4d4-b70938912257 | -11.85576 | -46.87264 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ee9ff63-b55a-33c6-b40e-82cb3658defe | -11.22017 | -54.06748 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d721c190-a33d-38d4-9371-9320d0acbe88 | -11.09495 | -54.03259 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6f570aac-8c79-3a9f-99d7-76185bc5c4aa | -12.34769 | -50.69118 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22a9c75b-3112-3bfb-a00b-ac40d4354100 | -10.88196 | -53.98765 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f642b8a-6e1b-3fa4-be7e-5a4298e5e41e | -14.60004 | -48.09474 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f437930-b0d7-350e-859e-e0864cd36ef3 | -13.03039 | -46.90512 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1e0d648-e433-37f6-ac23-007056f076a9 | -14.79125 | -48.54636 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c616404-7c0c-37b8-bac4-4b612222a8ed | -14.66928 | -54.4633 | 2026-09-20 04:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78e4bda0-3a14-3af4-aa93-a4ed010dbd84 | -11.78825 | -49.82696 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03605ddb-5718-31d1-b9b8-de4fea0fbcfa | -11.85778 | -47.65993 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e5c7117-6e8c-34f6-b6aa-ae15db061c1a | -13.73283 | -48.7921 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddbbac70-2936-3e01-9a6c-f5f6b5bcd131 | -10.92792 | -53.94833 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68c42a96-e465-3e88-ab3b-efc13b4412c6 | -11.21126 | -54.08016 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 304a7b30-afd9-3e39-b9d5-3526253f758b | -10.88119 | -54.08593 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fac095d-9afa-3fa6-990e-437442a95142 | -13.01188 | -46.96714 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e48ee45-fe80-3f7c-8465-56fb828fb897 | -12.29101 | -47.11269 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c25078fe-f85b-308e-b536-04be65b3909b | -11.23051 | -54.07915 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 55864e73-1cf0-3c65-991f-f00854ec5abf | -11.21388 | -54.06866 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 923a19f2-7ce0-3ef4-b388-9ff40a4d18dd | -11.85107 | -47.66801 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 109796a8-7b8d-3f09-a574-546be424accc | -12.3155 | -50.72933 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a4dcb5fd-9fe3-39e2-8d2f-b17efa2184bd | -15.47015 | -48.41491 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 909d06cd-ee97-35c8-a395-bc7311594579 | -16.59728 | -45.33803 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5dee2a4-7735-3dab-942c-a74b3eba782e | -12.28938 | -47.12225 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9447673e-b481-38c2-bb31-50a0945967a9 | -11.85814 | -47.67468 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cd031eb6-3674-3d6f-ae38-71d16f6815b4 | -11.75234 | -54.56749 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2abac221-2e5c-3a74-a1af-3494ddf852b7 | -12.74433 | -46.17756 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b75a61e-4150-357a-b85d-fa6d17eaf1f3 | -12.64795 | -50.92436 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abd408ce-56bc-35cc-b07a-22c5dbd3abc2 | -14.89028 | -48.15381 | 2026-09-20 04:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22118e81-7435-3d21-b044-db088ba3cf4c | -13.72863 | -48.79158 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 544ee56d-7c8f-34fa-ba05-981abdf30439 | -11.09589 | -54.02778 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e6133e0c-2cbf-3e36-996d-3e4385e46b56 | -12.75942 | -46.13229 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b7ea4e0-9a29-37bd-8ae4-c2005079ea6e | -18.66237 | -47.35704 | 2026-09-20 04:21:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 860eff27-92e1-358a-be69-9c813152f015 | -11.27968 | -54.11938 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d315d4-3906-310b-a783-7f2c7ed15afc | -11.74712 | -54.56113 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07953dd8-9fd9-30aa-a7db-7b5fb1e0a7b1 | -11.74416 | -54.56289 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fb9d98d-dcd5-38a5-bfbf-e9a6b0c5bac3 | -12.77178 | -52.85902 | 2026-09-20 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b5301c4-c907-366f-9530-2859cbec8cd7 | -14.13745 | -45.56106 | 2026-09-20 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b3c7c07-c295-3842-8f72-516a045c7ed5 | -19.95656 | -44.05887 | 2026-09-20 04:21:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5827ad5-0cc6-3bf3-9053-48d5997c56fb | -11.37646 | -51.40483 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b27956-a88d-3ca4-9d8e-ed53b5ad8d12 | -11.22442 | -54.07788 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef45934c-d5d8-3bf7-a074-06a7c957e663 | -13.02589 | -46.90878 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e02f5c-a829-36c1-b448-5fb05e759dd4 | -11.48062 | -51.48009 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e2a711e-32d4-3da1-98b6-17dd5a5c0e35 | -13.27721 | -46.73117 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64810d38-2520-3561-9a76-57511e7e45ac | -12.15955 | -47.04203 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e71e4b87-0cb4-3b10-a26c-c2f4cad72fc2 | -15.46526 | -48.41943 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43c41ea5-03ee-3dfb-851e-cc2419495a05 | -15.47418 | -48.4378 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa0813c-c112-3e48-8766-d2feca7a9ac9 | -11.86394 | -47.6649 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17cb4dbf-46fd-316a-b423-ec03cc5ddc93 | -12.75961 | -46.21964 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0889eb4f-fdc1-3b27-8a58-28b0484d87cd | -14.12328 | -45.60292 | 2026-09-20 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d45bca4b-f859-3d3c-b48b-759699a868de | -10.877 | -53.98504 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6c9adf5-212d-329b-b121-08756eba6d49 | -11.38053 | -51.38306 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
