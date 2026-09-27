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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b788ea0-677b-3d8e-97bf-f78f45c4a443 | -11.89097 | -50.51262 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dba8a8fa-a2cd-33fd-94b5-af043a7b5a8e | -12.57105 | -44.13924 | 2026-09-27 04:53:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6acfc642-0c53-36de-bbc1-4dd84f162e74 | -8.33441 | -62.86115 | 2026-09-27 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 230edbdb-5fb4-3e3e-9cef-54b483bf0ae8 | -12.29389 | -50.27574 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ef62785-abac-3f57-bb34-a62560bf0560 | -11.04572 | -51.75105 | 2026-09-27 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4c12c1cd-8786-39f6-9f95-3d08313a5375 | -12.28012 | -50.29235 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f589a59f-090d-383b-9458-2df74b3387f4 | -11.87805 | -50.52413 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3353717b-7265-3135-959a-047b7814379f | -13.87945 | -49.03862 | 2026-09-27 04:53:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 00aa475a-3ff1-37f0-97f2-771832193dc2 | -11.90059 | -50.52093 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 301e428b-390b-3bb6-8486-e0d168597d7b | -11.34578 | -41.84955 | 2026-09-27 04:53:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d739f561-59ff-3e58-a8e7-6f1296807284 | -12.26027 | -50.69858 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b40d6cb-4e00-36d4-b9ba-87d09c2ddedd | -13.09735 | -47.42413 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4de0428-1054-319a-a1b4-8b57906175de | -10.81759 | -57.19397 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82790424-c5b8-3a50-80f8-7c97226b38bd | -9.93227 | -60.72208 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22059a82-2c36-3182-a2cd-b59ccb1ada8f | -13.33615 | -51.3304 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be45de2-5417-3c10-ae28-2d7a48825771 | -12.28951 | -50.27976 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f8cedbee-379d-3839-a090-b62a8f7dc979 | -11.88172 | -50.52468 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 934671f5-a001-3b59-be10-54ddbb463a11 | -13.33913 | -51.33512 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b98ce72e-3c5f-302f-af08-c5e98bb53310 | -12.29706 | -47.17587 | 2026-09-27 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b7baf2b-a96c-3581-bf71-4ef8c2a9b257 | -12.02758 | -50.60114 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6b76059-b07a-37f2-8045-59a9853319f3 | -10.40749 | -53.80714 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3465b42-cac1-361c-8f0e-25899b7e0fbd | -13.33501 | -46.80478 | 2026-09-27 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f0a4cad-85d2-378e-8109-8488e5dc119e | -11.89225 | -50.50384 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0cf0dae9-e86a-3a0d-bbf0-de164ef599c8 | -14.40126 | -43.77742 | 2026-09-27 04:53:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07a1c4af-f105-36c0-905a-413f8b78b462 | -12.47666 | -47.4841 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2d96a9c-82ea-371a-8deb-38aac0f72fa3 | -10.0209 | -50.15752 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 661008fd-1230-3834-afe8-3c0a9c82cbec | -12.7042 | -47.31741 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2851381-f2ad-396c-a4ba-b176e3833b5e | -12.17641 | -47.38111 | 2026-09-27 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce93636c-310d-3230-85da-c16e593f2cd0 | -15.47855 | -46.15072 | 2026-09-27 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b7b96b3-902b-3cb7-8e10-fabdd8c396a1 | -10.42561 | -53.77787 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99e8ee89-dbb6-3da1-8e9b-b5961cd58aa1 | -11.93675 | -50.50389 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 188f562b-045a-39b1-b3d6-715352d5e12e | -11.81632 | -50.51039 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e789d5-a4b9-3938-9058-4bbff6fb42ab | -13.34211 | -51.33985 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9426d31-1d87-3e40-9b5e-d0f9586c57fb | -11.27967 | -54.42872 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d639e23-ed2e-3ac4-b912-8cfc93aa9fb8 | -13.0042 | -48.67228 | 2026-09-27 04:53:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fb0963a-c6df-3973-812f-75e7aef95a5a | -11.87629 | -50.51042 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ac56535-4e26-39c1-819c-614b540acf3a | -11.88603 | -50.52084 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd913d0f-95b1-30aa-a914-6c0ce819f373 | -13.37795 | -51.31963 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d9c4ff7-d60b-395a-8edc-f1a710eeee1b | -15.63452 | -52.69213 | 2026-09-27 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6607a7a5-8d34-3f2c-8532-1dbd946f0526 | -14.41313 | -52.8084 | 2026-09-27 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc63b95-0301-3fb3-933d-d08458545f46 | -12.59141 | -51.95481 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 689d3546-c47c-3aff-8dc7-818f53f1ed01 | -11.88236 | -50.52029 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a7d14ed-c0b4-35d4-b342-3204b6b69ee7 | -10.10889 | -50.19588 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6772c89-18d3-3e0e-93a3-db28e3f9b260 | -12.25662 | -50.69803 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b013fd0-34a3-372a-8a99-5f54463822f2 | -12.89286 | -61.71951 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87793992-e6f4-3925-9206-2915cdbda745 | -14.81904 | -49.27316 | 2026-09-27 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8721fa1-1657-3d86-b55e-72f49ae20c29 | -9.93773 | -60.71814 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a49a2bf-56cf-3452-89e9-caaef6e0e3c9 | -12.13994 | -50.32975 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 108cdabc-1026-38b0-916f-a4de4a9f00c3 | -14.49744 | -48.32663 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2688061-a739-3827-ab37-c1259db51e49 | -9.5719 | -62.70789 | 2026-09-27 04:53:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34b9effc-e185-3b60-a548-b381b12edb55 | -11.98487 | -50.56046 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c81759e-ec54-3948-9f04-545b86f18844 | -10.72567 | -53.99424 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2e9b961-03d6-326e-a679-09bc05452c33 | -12.29518 | -50.26659 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09e34e3f-1b62-3a30-ade9-5c188b801372 | -9.93686 | -60.72292 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82687a61-c322-3a51-a8e4-8a16eda99cf3 | -11.9697 | -50.53579 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c90b1c19-d06c-32f9-9473-e46ba33fe5b7 | -12.0282 | -50.59677 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c0373285-e0e3-357e-8d5d-d0ae1bdaa85c | -12.28887 | -50.28433 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07948d93-65c4-3bf6-b95d-d931af6978a3 | -10.03937 | -62.45527 | 2026-09-27 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 153f15d0-9d38-3ef3-bb3c-4d3ec57842f1 | -8.33507 | -62.85758 | 2026-09-27 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e19d8dc9-c9e5-3f03-9bd7-4f4f98cab36a | -12.27949 | -50.29691 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b055f323-aa62-3d50-862c-d03c068f1365 | -11.85833 | -50.55693 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f6b77387-8a23-3bbd-872a-caa61fe5bbd9 | -13.33734 | -51.32203 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 077407d8-bc6d-3d85-8846-88682b99f438 | -10.82484 | -60.72629 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1308568-9dfa-3261-a826-04e653fd24bc | -11.7738 | -51.01327 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 133df4bb-5086-3e92-b252-4f62294725cb | -11.98458 | -57.60582 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ecb1818-0caf-37d3-8470-1370d50e3f30 | -11.89657 | -50.49999 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 427b4513-142c-3c05-ae4d-b859d26bb1c0 | -11.89465 | -50.51316 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a79a2daf-70f6-388d-96c6-05d350220524 | -11.87742 | -50.52851 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5e61d5d7-4798-3a51-a551-5ffdac550ccc | -10.68299 | -57.6325 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d3a6d8-4f4d-3ab5-b969-7910e75e2ced | -10.57592 | -51.28467 | 2026-09-27 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf5b52df-a093-3cba-97fb-db08d625b030 | -13.71927 | -48.81143 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdc4e326-426e-3521-88d6-eb48533f39a6 | -12.256 | -50.70237 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1e0b368-c4d6-3bf5-b5ef-6bfa7ef26bd8 | -12.6814 | -47.31478 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 227535ec-e2b7-30c3-85ce-c8140199c270 | -11.85175 | -50.52466 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ad1b201d-5849-3cee-8301-ec3f18a4ef18 | -15.42239 | -47.9142 | 2026-09-27 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7eec7942-bfcf-358c-92cf-886ab658dfe9 | -12.05142 | -50.59132 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5326ee6-1a0c-3f97-ac37-3446da66f018 | -15.4236 | -47.90438 | 2026-09-27 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6cc1a63b-e211-30ee-9a6e-573c31c76446 | -11.85605 | -50.52082 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3af6369d-99d0-37a2-98b5-f8208d4d10e9 | -12.7036 | -47.32207 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d51009c-ae0a-3423-b372-abf68d41928e | -10.42292 | -53.81675 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54e0e5cc-4f7d-36b7-aae4-a6cf61d94067 | -14.7949 | -45.95833 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81e943be-08a0-3127-b872-71e7ca506dc1 | -12.90404 | -52.06804 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3de1d2b-e2d0-3a70-be18-105a83f59807 | -11.88539 | -50.52523 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0340d421-ba21-320e-b17b-841aa414f402 | -9.54764 | -57.39482 | 2026-09-27 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e8c4cd8-8771-3644-b1b1-f94c63b26f62 | -12.03248 | -50.59294 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 2150ca6b-1d36-3557-bc02-f8bed2a11bdb | -10.25136 | -59.12624 | 2026-09-27 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 783540e6-6b09-3d56-8c16-b51e385960d2 | -12.67294 | -47.30841 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35d9448e-c529-3a99-8a08-89f7fe448e07 | -10.22586 | -49.9847 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e52314d-d4c6-3d83-ab6a-69fcd4942d9e | -11.85896 | -50.55256 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58bfd87e-845a-3d03-9f05-0f6493dc90a4 | -10.02162 | -52.09988 | 2026-09-27 04:53:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f96fc648-8d54-369c-a58a-56279e745892 | -12.59198 | -51.95092 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6a5b00-304e-3acd-a90d-51b02df4dae1 | -11.03759 | -54.04117 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 592edbde-6b65-3d00-8b09-b2fb1888810d | -11.57798 | -50.50518 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6ee8e8b-291e-3904-a511-2e5c9974b651 | -10.04142 | -62.4549 | 2026-09-27 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16b5354d-7123-3729-8da9-606b2a0bdca9 | -10.41246 | -53.81865 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76873d91-fa4c-367e-a71e-56bcf77e036b | -11.8873 | -50.51207 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08cc735b-f637-3fb5-b33a-cb17c32c4598 | -12.03186 | -50.59732 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d9f2d923-6b4f-3c09-b413-05476798634b | -11.89767 | -50.5181 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b88327c-c3d9-3555-bbe6-7baee9a3d0da | -11.71109 | -59.13241 | 2026-09-27 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9c73bc8-1eac-3b83-885a-764cb6df9a93 | -14.529 | -48.32256 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README35.md)
