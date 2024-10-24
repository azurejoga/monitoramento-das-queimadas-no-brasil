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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5031549e-b267-314e-aed8-4768937f2712 | -3.10734 | -53.12965 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f449995-a424-3c78-9dfb-00aa150ff6ed | -3.1068 | -53.1331 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a57115f2-8f31-341d-a439-f476c32df6f9 | -3.07671 | -53.238 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9d9932ac-cebc-3c96-9c86-08a20e79bcad | -3.07617 | -53.24144 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b43067fc-4ea3-3f23-b829-d16c85ea00fb | -3.07563 | -53.24489 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cc3ca71-22aa-3cd1-b758-7bd89440dafd | -3.07508 | -53.24834 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0dc5aa0-d9a5-3ade-ad5f-0bc73b862265 | -3.07339 | -53.23748 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 563ef379-b582-3285-98eb-8d075d37c6b1 | -3.07285 | -53.24092 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a0c8ae34-2dff-38cf-a636-38da5630f34a | -3.07231 | -53.24437 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aff3cf79-0ece-3b28-85bb-81ed4c2be774 | -3.07177 | -53.24782 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1850ddf2-f66c-33b6-9887-0dfa03f02298 | -3.07122 | -53.25127 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d89643c-ed12-3f61-86bf-3c3dc64259fe | -3.06899 | -53.24385 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1608767-4431-3550-87fa-a9eaece942b0 | -3.06845 | -53.2473 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 730a8e01-a30d-3ea0-87c5-ce2e2b306cdc | -3.06567 | -53.24334 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13f485f3-1eb2-3da8-ba81-886e0fc7fee0 | -3.06274 | -53.24237 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec11364-a459-3058-b8b2-d2a3459d8126 | -3.5589 | -53.22863 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 238a19bd-e738-3196-8f3a-97c724a24b19 | -3.54163 | -53.01346 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a98c3e59-9996-3bad-babb-ebe3c980ecbf | -3.52158 | -53.50909 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65bfa9ed-322e-377d-880e-655e6764ab98 | -3.52063 | -52.82479 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52e0d7fa-21fb-36b1-bb78-8193f2b5da7b | -3.50919 | -52.89766 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04897270-05b6-31fa-8722-94fe968985d4 | -3.50586 | -52.89714 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a649550-0784-3e86-92c8-02dcdfeb3f31 | -3.47339 | -52.79965 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eabed404-148d-3580-b089-1925b8ab4c25 | -3.47284 | -52.80312 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef4e36a1-527a-3ff6-a5de-6ff60d3045ba | -3.41766 | -52.72709 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79ec0a62-4118-39da-a334-956f70710624 | -3.40918 | -52.86817 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a5f5659-e80d-3167-9703-5fb49f08e7e5 | -3.40863 | -52.87164 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce6cea09-0187-395e-a185-aa2be7a20116 | -3.39593 | -52.88741 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60c0b7f9-d62a-3566-9cb0-8f1d18b9af03 | -2.95916 | -52.48109 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138fec12-877e-338b-be73-5949264d60ab | -2.77855 | -52.09996 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c51d2f5-34c5-3f75-926e-333b6e27fb20 | -2.77799 | -52.10351 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0a0c20d-53a4-39f7-8dac-819b54bd604c | -2.77744 | -52.10705 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1819e727-090d-3628-887f-82d641303d0d | -2.77463 | -52.10297 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c618e9f0-6c18-3501-8069-415f092ed224 | -2.75215 | -52.04843 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b3cbc65-58b5-3089-a3ef-80f258641dc4 | -2.6125 | -52.03022 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aba59f7-292b-3b60-afb4-0e9a552acbbe | -2.39719 | -52.00117 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03e296b3-4499-3425-9844-030a4b466c7b | -3.6322 | -52.28847 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cc96874-fefb-3c3b-9134-3d846fdc191c | -3.63164 | -52.29202 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 747aa6b2-6d2b-37b1-a0b5-ec2dcb4fc9c4 | -3.63108 | -52.29557 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 975b8265-65d6-379b-853a-050a9835c6df | -3.00086 | -53.44112 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 807d8db7-d514-3207-9a23-e73a160bf97f | -2.85194 | -53.33342 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a2ee989-ba00-3c74-a3e6-f165573f69e1 | -2.84862 | -53.33291 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bfe0ddd-dd00-3487-84f3-38273beeff74 | -2.84639 | -53.32549 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183b787e-a294-379b-b314-67af76b582c1 | -2.84307 | -53.32498 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 761eea7c-ce2c-3f6f-984f-15f084529bd0 | -4.19855 | -53.63265 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f31137b-5401-3050-b323-a38153ec5350 | -4.12293 | -53.83675 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 306f7294-59e6-3973-99f7-14ad5c4388a9 | -4.11962 | -53.83623 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1062be94-20da-3e4f-92ba-b5a9e5ff50f8 | -4.01627 | -53.7387 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5401ca6c-f741-311a-9495-6b96b7c89349 | -4.01573 | -53.74215 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3e8c4d9-b1d1-3ddf-8616-cdc89ccb42f4 | -4.0135 | -53.73473 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46cb69ba-7755-3c9e-bc55-beb9bbd1f629 | -4.01295 | -53.73818 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d2f69fe-3b63-3601-a0ee-5070292b81a2 | -3.91364 | -52.39035 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73efa006-fb13-37e6-b8c3-81f669cf3bbe | -3.91308 | -52.39391 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67732940-7380-3b97-a337-9f78180cedff | -3.91084 | -52.38626 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a635f949-6ac4-3df2-a3e0-9fac332c4e3a | -3.91028 | -52.38982 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ead717f-6a70-3189-9c12-898b483b5f40 | -3.90973 | -52.39337 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b0f17b-9d49-3e48-ae2d-767740a4a851 | -3.90637 | -52.39282 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf4eeb14-7c8d-3550-9d7d-f1c6b1cf712e | -3.88277 | -52.34545 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1b3f520-010e-3e27-a727-efef29ab4232 | -3.87941 | -52.34493 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d6682d4-9be5-378d-8a20-4baa6a081d02 | -3.79153 | -52.38961 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b43ea8-c3c5-30e5-ad41-40425a1f52c8 | -3.79098 | -52.39315 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96d70557-7732-348f-b914-55652d19a98b | -3.78873 | -52.38555 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67526bc-80cc-3273-8454-616fe77f40b0 | -3.78823 | -52.41077 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 359ee2a2-a87b-3295-8f6f-0c0040df64a8 | -3.78818 | -52.38909 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17deab1a-7048-3de7-9181-d58704147cca | -3.78762 | -52.39265 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7781883-a183-3ed3-b718-1fc58f05c942 | -3.78537 | -52.38502 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adcebb23-5341-389f-949b-e648d7ba94fb | -3.7775 | -52.36929 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c72aba0-daf7-3a3e-90bd-dfe9951f969c | -3.75545 | -52.28947 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3da13cfe-5289-3ed0-b62b-6c657f6ecac7 | -3.7549 | -52.29302 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e104aee-7a5d-3727-862f-efdbc7205a4d | -3.75429 | -52.28962 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0cb138dd-2017-3857-b7eb-dae8caff14a5 | -3.92671 | -53.66468 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d46b34c-708b-359d-bf5a-66d7c681cb25 | -3.92617 | -53.66814 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5114d3d-ec42-3ec9-abd9-359e4ac7b403 | -3.92285 | -53.66762 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c023a0d2-2b5b-3ace-b64c-468f33cdcc02 | -3.84479 | -52.76476 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23830b29-ea51-3303-bf50-49bf57d239de | -3.81565 | -52.68863 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e95e1d7-406b-33f0-8bcb-c8dbdc337b32 | -3.8151 | -52.69214 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdacf677-6d30-32e8-97dc-2eacd7e356d4 | -3.81231 | -52.68812 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 034a3730-d9d6-3f1b-9b79-121a394c70f9 | -3.73195 | -53.78589 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc37b8d4-c808-33a9-a55a-b1682cb684aa | -3.67776 | -52.68908 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c98d7c6-5efb-3d84-8cfe-61f190aa7da5 | -3.67442 | -52.68856 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07bdc60-d63f-36e5-9728-33e4ab975d02 | -3.60874 | -53.7064 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952c263e-7350-3244-9174-966efe961a5a | -3.58771 | -53.49455 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 399c7e07-3902-3ef3-a72a-8fd91ddd5d54 | -3.56568 | -53.52647 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ae53fd-72fc-3edc-abd3-2997f797d4ca | -3.56406 | -53.75247 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1dd8bf7-4da3-366c-81cd-8c0ece125949 | -3.56351 | -53.75593 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9edbcb4e-a318-32d7-b542-8eaf877a531c | -3.56128 | -53.7485 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b502a1b6-ee28-3a7b-855a-a2329c83f1cf | -3.56074 | -53.75196 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bb9cf4f-4f4f-330d-ac72-e13dab009e39 | -3.56019 | -53.75541 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2242ff4-d00c-33c1-8c5c-4c8b12ba0820 | -1.95201 | -54.04507 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 494c904b-65d6-3809-bca2-b62727b7e104 | -1.94715 | -54.56488 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4215d785-6f4a-351f-b4dc-463cb7733413 | -1.94601 | -54.57209 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abdbd900-f479-37fe-8184-e95282cb4e91 | -1.90588 | -54.58428 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976ba1ff-857f-3067-a1c0-cf0d47d0c57d | -1.90531 | -54.58787 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8505a6ac-167c-3c22-97c7-bffa9990cc46 | -1.69454 | -54.26207 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b8de29d-973d-392d-b6de-be1ed4cee2e5 | -1.61073 | -54.77348 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34da108c-f442-367f-8787-7bd9530213b5 | -1.61016 | -54.77715 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0166636-2d56-3b1d-b892-1305c4e149fa | -1.49434 | -54.18018 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f11356e-01d5-32ea-aebb-b2526f5a1994 | -1.49378 | -54.18374 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a7474ea-1b70-3ea6-bd4a-9c03ac24c6cb | -1.49322 | -54.1873 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eac5e9a3-8518-3c80-97c1-1becb02f42ee | -1.49098 | -54.17966 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4df8bd2-31ce-3d21-9ee5-12d12dd4577f | -1.49042 | -54.18322 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README69.md)
