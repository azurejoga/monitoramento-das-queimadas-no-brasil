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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1677fae-d348-34b5-988d-598235c58a1f | -9.84602 | -43.54763 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a507be17-e0ab-3ed1-9018-3ffb13201127 | -11.69758 | -46.5086 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f86d6c45-6ea3-3ba9-b91d-d0d2223d835c | -10.53837 | -51.51934 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6753a108-868f-32e8-881d-b1c4af93f520 | -11.67322 | -46.59977 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f94910f-bc1e-3a09-a993-e6afcab4952c | -9.25217 | -57.0733 | 2025-09-12 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 347c2555-47c8-3b9b-990b-10a06a8ad009 | -6.24327 | -44.79998 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c1561fb-2ae7-36f4-9f6b-fad53786cadc | -11.14966 | -45.30987 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef68dd99-3234-383e-9de3-915bed028159 | -6.59375 | -41.44939 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a7f5206-dd3a-391b-a899-d9dd76eae5d7 | -7.62471 | -46.54671 | 2025-09-12 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1da82509-3c19-343b-ab26-5721e3ca5374 | -9.98254 | -51.70887 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9599df99-bdc2-3597-8b7f-f5e9fc073c7e | -5.92144 | -45.73761 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3b4feab-84c7-3708-8d9a-03b1e5b6ebe4 | -11.68869 | -46.52186 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a006516-bef1-39cc-8c53-0ffb5ba8a855 | -8.57512 | -51.34844 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f3c60ee-1ba9-387b-954a-2e169aab4bf4 | -6.15047 | -42.61001 | 2025-09-12 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b11f2a13-371a-3361-84f1-511d7a89afd2 | -11.18594 | -48.43937 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b7fc41b-0361-36c0-9cde-f509e2aed8b5 | -7.39894 | -44.35867 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4363cbb4-528a-3d38-8e03-eaca8d28f119 | -8.0785 | -42.56137 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdf9037e-0132-37dc-8415-2766ace947ee | -12.02164 | -43.7897 | 2025-09-12 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73b8a57d-f695-31c2-b787-854384249707 | -7.5212 | -44.68371 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43732f3a-c475-33e2-8194-9271a10bc030 | -8.39789 | -44.76516 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7639bcb3-5492-393e-9bde-8152a56689cc | -3.76459 | -52.17506 | 2025-09-12 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f66dbdc4-3850-3fc8-9804-6a6310082d55 | -10.67205 | -48.65076 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 151e24af-bfc9-3ade-9a88-1188dfa7d7f5 | -9.11452 | -46.96249 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eb0abd9-cf55-37e4-88df-32dc1264d3ad | -11.72962 | -46.51744 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36694459-6afc-3838-8fcb-bc1017eb2d80 | -9.04728 | -47.06586 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8a83f6e-4611-365e-a2de-6a94c78740d4 | -11.66934 | -46.60279 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b41aa84-63bc-373c-a96f-532d98cd43e6 | -6.65796 | -44.12926 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 869d1089-8454-3d36-a5b5-d0b66a09f9b4 | -7.84566 | -44.80383 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b25457c-dfa3-3290-8f02-53eebe8941b3 | -7.42075 | -50.65127 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97a3a410-f09e-33b9-96c0-10ef84d1991e | -9.79057 | -51.0756 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58fa5e18-2b1d-3be2-9abe-8bfe85824a26 | -10.4128 | -50.6001 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b678bd30-b405-35d6-8aaa-5a956f057e3e | -9.51363 | -54.63642 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 760834e8-7bd3-3c85-ac52-8b25d4dc88f9 | -9.65801 | -43.53244 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86efa9ab-dc98-399f-9eb8-e564742a61c2 | -10.58241 | -47.21592 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 275a6639-8d53-37b3-acc7-4fd85c836d9a | -11.49128 | -49.26264 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7ab1786-883c-3c60-b00f-91180130cfb0 | -11.68267 | -46.60494 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c61fb13-b77d-38aa-934b-6200fe6b959e | -9.07533 | -50.50425 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b73d7fbe-b7fa-3de9-8bc1-51ab33dbad6e | -8.04503 | -52.32777 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f606295-edc9-38a9-875d-326d8de4079a | -10.0863 | -48.17473 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1940a87f-279f-3cc7-a63d-4efac6cb8ff8 | -7.81353 | -55.2275 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f1ada4e-20d6-36e9-963c-6f9447c0668b | -9.90019 | -51.88185 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87775b61-3144-34ab-8154-f6968cf5a982 | -11.68929 | -46.56215 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30ba3fd7-b77f-381e-96b7-f3012cde2799 | -12.11601 | -44.87128 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 342c15ef-4de7-3f99-bb05-24b38d353970 | -7.85782 | -46.0562 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0321d59-61e1-39b3-b75e-e138c91b02d8 | -10.42077 | -50.59733 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63198f43-907a-331b-acef-0b662ed67140 | -9.45175 | -46.41536 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b55d5ddc-1c0d-3da6-b660-3c5d66c5333d | -8.08549 | -54.73866 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 350f179c-1165-3089-9d7b-afe1d89197e6 | -8.42599 | -55.63547 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85690f38-433f-368d-a40d-3c5c12f131fe | -11.69653 | -46.58161 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 929c3279-14e0-3b1b-8eda-697f4f646f33 | -8.0796 | -54.74333 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e18529fc-5144-3b8a-903f-ee7bfe8b2768 | -6.94542 | -44.7845 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45130451-72af-35e5-92ba-52c9e35f0fb3 | -6.10463 | -45.93348 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f04a765b-d98b-39c9-b2ce-ac1d0d16bdfb | -12.11013 | -44.86216 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7314548-29fc-3589-ac97-d9209c61e26f | -5.65525 | -45.9405 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 742c493b-dcb0-3dd9-b7a3-c120a648857d | -12.15251 | -43.70945 | 2025-09-12 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb90cc5d-592d-3f45-be11-33f601f33c01 | -6.95672 | -44.77876 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f6b0885-e9de-3e38-9d27-186ea9026192 | -5.64548 | -51.87179 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e00ad6d-4ffc-3f03-ab5e-b415210b0e13 | -11.51892 | -50.605 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e454c695-923c-36f3-8402-41bb7f92d6f1 | -11.1849 | -48.4245 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75047754-1b84-395e-af65-02f84f49b6fa | -6.10354 | -45.9404 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07a460a8-702f-318c-80b2-bd34a9573770 | -6.84035 | -47.88092 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33b67109-c894-37a5-a6b0-dff08617578c | -10.18839 | -48.5798 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57532568-04e5-3751-9446-a5e129d3ccdd | -11.68099 | -46.59373 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cef53ba-dfbd-3ce1-8287-8a00f8b739a3 | -6.16983 | -47.28304 | 2025-09-12 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 127e0870-69b6-3253-b525-bb3f367b0d61 | -6.48584 | -44.49445 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1272b7d3-b283-3f98-956f-eda30ed4ce79 | -9.10465 | -47.11077 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d458776-ad26-361e-8c15-894fdcdcac80 | -6.28514 | -42.39879 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b6f7bd14-3b81-3695-95b9-b201c0ec41da | -7.46644 | -45.29521 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c8b533a-1b27-3ab5-bae4-ce29b9503a61 | -11.53577 | -50.39812 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb8b50a0-3f9f-35d9-b800-9c2e4f40099e | -12.00077 | -47.56742 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17b08545-5ef6-3b4c-8b38-3bbfb54519fa | -10.37607 | -50.50599 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cadcb38-eb96-3451-b586-f7fb222d9917 | -9.88514 | -46.46638 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410def7a-e8ab-3794-8136-e996aa4da085 | -6.64694 | -53.19149 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17bc5c0a-8634-396b-9c40-ee927805e132 | -8.06432 | -52.31921 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 882fa4ac-348e-34e7-a0a7-db9216b58316 | -5.81608 | -51.70765 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59baab2e-c692-3631-9b28-2ee7533a365c | -11.08504 | -48.434 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678d815a-25b1-3abf-a37d-3bceaf3f490d | -8.17425 | -46.11741 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3711c99f-9ec9-30a9-b229-023cd11f9348 | -11.53043 | -50.60269 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6a3588ee-0221-3dde-b546-082543052ca7 | -5.64538 | -51.8713 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2c3c2fa-b731-36ca-b63c-87ea889c2e1b | -9.51839 | -54.63738 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7629b523-ccf3-30fe-b318-7335d8c1e822 | -8.57204 | -51.343 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb10515-0a54-3ed6-a478-683c28bf4e67 | -7.4863 | -54.95295 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63153838-5d30-3475-8bd5-430895bca7d7 | -6.67936 | -44.14403 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d9cf7f4-d11d-34a8-9dc2-7a783f6e726a | -8.08155 | -54.73901 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ae414ba-a272-3627-8c9f-e506b298f24a | -10.67383 | -48.63979 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8ac1b38-9203-3e97-94f2-67871583912b | -6.88245 | -43.77821 | 2025-09-12 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 473cc866-dabe-3f52-a1e1-7d975b3b01ab | -7.49246 | -54.94771 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59f9d2c0-da71-38b6-bbb2-10b13237ac96 | -11.67488 | -46.58908 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 325e12bc-b852-3ce0-8c0a-fac3544aa23d | -11.70041 | -46.57859 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8596147b-f4cb-3cf9-b2da-ab3eb3896f06 | -10.43995 | -50.61698 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 028ece33-4ff9-33bb-a624-0812de8210ef | -6.47453 | -45.15358 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdc244b2-bb91-3da1-af71-bc200eb6a2b9 | -11.6771 | -46.59676 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70eda8f9-3dc1-3130-a248-ff31403918f8 | -8.17921 | -46.10744 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea7f2f04-72f4-3e08-8e84-a57ccf5ca82c | -8.33369 | -45.41454 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b7596f1-cdae-3631-853f-b60e38f8bfac | -10.12461 | -47.91539 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 174590e6-3d73-365e-b156-83aa9144468a | -6.40282 | -42.59874 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a8e2a06-8bec-38cd-ab80-df4013bc22f1 | -10.56065 | -52.02247 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cde9532-2da6-39e8-a777-2cae2bf56bcc | -6.18228 | -41.08478 | 2025-09-12 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dd50fd5-1015-3a1f-98d2-27560d2a317d | -10.83333 | -42.75945 | 2025-09-12 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| be4bf7e4-59af-3975-86da-f39a1b84ea79 | -7.71883 | -51.07985 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README68.md)
