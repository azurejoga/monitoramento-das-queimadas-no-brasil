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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75d6e7e3-e200-3413-84e8-f4004c2a5c4b | -9.0766 | -46.99091 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a575553-5191-3a00-8b39-e6d8b2fa6b66 | -8.93591 | -48.6507 | 2025-09-05 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83874ae5-ed13-3722-b973-91857efbcb5d | -8.52264 | -51.31342 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc61f422-2e1b-3ca1-83a4-9264b86f44d6 | -11.9036 | -46.65683 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c963694e-35a2-3a05-afea-8b19057193e9 | -7.6856 | -50.29979 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 374d5f94-c1f6-3410-ae0b-74752678cd66 | -11.65211 | -54.53416 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 055dcb42-f5b8-3ca7-b2a4-9af55085c088 | -8.91166 | -44.17497 | 2025-09-05 04:36:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41d6394b-f415-315a-9d9c-a07a8a4baddd | -11.6171 | -52.19781 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7add0ab4-e5e0-33b5-b378-976887a1b836 | -13.29339 | -46.81708 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28732331-ae8f-3cc0-860a-c3513ebe0fdd | -9.42285 | -46.78022 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2129e2de-fc0a-3361-892b-869459846df1 | -8.47673 | -45.07569 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71a1047a-b2f4-335b-99fb-d7fffd766a87 | -10.4212 | -50.27889 | 2025-09-05 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6161156b-32e9-3a54-b580-45d9b1cb47be | -7.69536 | -50.30553 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a0dd030-7508-3d01-855e-659826a8bc1a | -12.71606 | -45.07598 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 21cc414f-e2d8-3ce5-be74-df4add5ddec4 | -12.53198 | -53.81278 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2d08b40a-da75-39f8-b630-3f2c4bd98fb5 | -11.99628 | -46.76228 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a4abee8-b4ea-3462-b290-233eb14797b7 | -12.71922 | -45.08128 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 86f4a7da-b1ac-3eff-9967-457babc2004c | -12.91268 | -48.03615 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b26b5b9-6c76-3efc-825d-254f5c74ac44 | -11.57602 | -44.65783 | 2025-09-05 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91e8a68a-8f19-3772-bffe-80777619b17e | -11.60182 | -52.15581 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ce2af5-dc96-3183-b329-feae3e4384a8 | -10.98396 | -45.99546 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0681cb87-f718-3dcd-bc82-8bf7fb99e05e | -7.69236 | -50.25834 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c330180-4b3d-36a0-b423-71ee1ce7be3c | -9.98096 | -51.63519 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a41eaf8-405d-396c-970d-33dfc3e1d60f | -8.89944 | -45.78925 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b58ef6d-9804-3811-b4b8-0910b3a6e837 | -11.83739 | -44.71964 | 2025-09-05 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 087f0173-fe5b-3c20-8d65-afe844606cb5 | -12.29184 | -50.00825 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d3ad018-7b39-3b86-a3e7-e6933019af57 | -12.26748 | -50.15924 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17f96a8c-954d-3008-b337-6a32dfa16c3d | -13.66312 | -47.91375 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9361696-6177-3609-875b-7ff3383ff254 | -12.18461 | -53.89555 | 2025-09-05 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf45970b-627e-3b00-a12f-3063c6a4f338 | -12.52503 | -53.80632 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b6c250d-8dfe-378d-a46e-45354747e5c6 | -10.773 | -48.2862 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f80d5909-c61f-3ed3-94a8-6c1764019c07 | -13.3492 | -46.82947 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1626c662-c800-3dea-8092-179e6fd8928d | -11.85075 | -47.54514 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf3140b7-cc1c-341a-a50d-2dda15169c6c | -7.72473 | -50.32238 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69c4d774-4cda-3b58-9d7d-79789eb02532 | -8.18852 | -49.58818 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60dca7f7-35b1-32ce-b8c9-3327add1053a | -8.61806 | -49.8482 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 025c8868-f3e7-3975-bd95-4465f33f781c | -12.93355 | -48.05788 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab81eadb-4ec4-3e72-9d84-e5b29925300e | -10.15905 | -46.24512 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc42e0cf-53b8-3f13-8653-c5d4ff6af0e3 | -9.44847 | -46.79556 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65288b0d-3589-3e0c-b6e1-e27590e622d9 | -8.88503 | -47.23385 | 2025-09-05 04:36:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8960c75-b4d9-3611-92b1-9488a8872fc3 | -10.24388 | -50.54745 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e537024-5eb4-3886-b78a-4ce4fb30d771 | -12.96842 | -48.07829 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2bc6411-256d-313b-b4ac-819e408d16bf | -8.36934 | -52.55319 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c8b3f1a-aa8c-3bf0-8617-bf5822156e18 | -7.69883 | -50.30608 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7459c689-3852-3d52-acc7-221a5b155cd6 | -5.48778 | -60.13235 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 089cde03-2966-3cdd-bec0-4074acad62e2 | -9.71147 | -51.08089 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e8f81b6-be65-3815-a502-d2ee261c939c | -12.52457 | -53.8321 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82695859-552e-3f4a-a15e-b2d54cd1a27a | -8.02067 | -45.41523 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8614563b-3e49-3e48-a967-1ebe0c76b841 | -11.38953 | -43.59853 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9931ac47-816c-33c7-b934-151e1b27e1e6 | -8.18879 | -47.42739 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c9cea6c-6a92-3383-9aa7-5f19fce96662 | -8.8656 | -47.91909 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e0017a9-f136-3e5b-856d-338e80dd6a86 | -8.09057 | -45.33898 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7028bad0-fc4f-3c20-8e59-f8132f17f04b | -10.0788 | -48.07143 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acc5369b-f0be-3019-960c-bb444b47da8c | -10.77356 | -48.28267 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4888a81-c343-36cf-969d-f46cee23ec7b | -10.47123 | -53.62104 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efdcbce1-ccc5-321c-9935-9484b4ff2016 | -10.87951 | -55.38884 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be5fe910-cbb7-30b8-99ec-9437c2198ee3 | -9.07225 | -50.42839 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a08fd06c-e9ec-3311-8d94-dba61db75e09 | -12.9794 | -48.07937 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bf2e9ee-fea0-3bbf-8f6c-b8e015e7b60a | -7.80325 | -52.13202 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55887c54-2944-30c9-9fff-e96449cf8a41 | -10.46632 | -53.62555 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dcfba86-b74e-39cd-bce3-5b2958b375ab | -11.31725 | -55.22886 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032ac512-659d-31b1-b3ea-4de03cce63a6 | -8.09472 | -45.35066 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a82544c-afde-32f6-8108-ea59e53e7f6c | -8.91118 | -45.83133 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fc52b51-b636-3841-9f15-159d248e3c62 | -11.61418 | -52.19294 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aa2880d-27ea-3173-af01-32c0f6c606cd | -11.64382 | -54.53259 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 065d14dc-752f-3fe4-be23-2c0a600845f2 | -8.48037 | -45.07625 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd5d438f-52f5-3236-925a-26c8f99b943f | -12.91379 | -48.02892 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fb8de88-729d-31ee-8bc6-a0f9535aa908 | -10.15556 | -46.24456 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b99589c5-db1e-3e4c-ba92-79166aea9f33 | -9.07041 | -47.0086 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 66b69d2d-1077-3b76-b332-685f25e75106 | -11.58954 | -52.18425 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc976e0c-ede0-3e96-9940-e7273e208495 | -9.80198 | -48.32659 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a3ad25-f43e-3673-9a72-f681e3915870 | -8.01189 | -50.09578 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e39cca86-59c7-3b94-8dfd-d8473c8a22dc | -9.42797 | -46.79248 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82ea1975-2bf5-3279-8274-b0cca9300647 | -11.57721 | -52.16903 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28d6e7c1-ea95-3ada-9520-d03c6b7a7797 | -12.89635 | -48.02993 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 439b99a3-3435-3127-a0df-515f7834915b | -9.43196 | -46.78923 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55e512b8-9b95-3d35-b0ae-d8438f2999f7 | -10.8822 | -55.38673 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 360cc09c-bb0d-30e5-9eb8-76297921a336 | -11.02553 | -45.06304 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a36c9156-f6f1-38e5-bfc3-e4a01d797d19 | -10.2342 | -50.54198 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f1bc14c-2d80-32be-af73-6ae6cde8136b | -11.86731 | -51.45448 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81f8bec7-7718-3830-a96f-1576b714edad | -8.89299 | -45.88073 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8fbed6e-7187-3025-9965-c39e8958545d | -7.77666 | -50.97358 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 573a5021-b7c2-306f-aae5-d3bbb5e17204 | -9.33356 | -55.20575 | 2025-09-05 04:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c637fd10-c712-3f35-8375-2a4649782b14 | -9.26906 | -48.55303 | 2025-09-05 04:36:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f266c87d-0cd2-361a-8d91-daa8265d6c2a | -8.36163 | -52.5518 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7b18f38-eb38-3223-b0ad-c4a6fd7d87bd | -8.07127 | -52.35192 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7489cfeb-b489-3824-a66f-dc10755cf545 | -12.85741 | -48.00551 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da62d91-4bdf-3ed1-a397-23398397af71 | -8.89592 | -45.76532 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32f63630-c36b-3bec-8ed2-b2233ddfa25a | -12.8744 | -48.01518 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0037d6f-69e1-3445-aa97-47de5af64f32 | -11.6153 | -47.78939 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df85335f-4633-352d-9ad3-4d2dcbe9d9ab | -13.51537 | -46.92229 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1210230-b2de-394a-8a68-f9b8dd148ded | -7.74855 | -48.80431 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095e808a-04a4-3011-9965-68358380961d | -8.44068 | -45.04523 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57a4a739-14e1-3f62-a266-3c80e11d6f9a | -9.06647 | -47.0117 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dd9956e-e497-332d-8275-ba9d90d283ba | -8.88226 | -47.92171 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2522e0b-928f-3637-8ff9-bc1c48e2c3eb | -8.91988 | -45.12 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ceca6b1-b126-3096-8e7b-2616a7207538 | -11.639 | -54.53561 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c546aa6c-981c-3d8c-8f26-f1d29718e360 | -13.71828 | -46.91149 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ce0d902-1c67-345e-a940-bb57a584cede | -12.09234 | -44.7254 | 2025-09-05 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40cb3988-8a9d-31e9-a9a3-c975f1f90131 | -12.51498 | -53.84068 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README27.md)
