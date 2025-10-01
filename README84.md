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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14492d5f-cf5e-3d6d-8914-23356f9a3828 | -5.85941 | -45.78298 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32e4bee7-35c6-39fa-a92f-46e8a67cb81e | -6.91457 | -55.4537 | 2025-10-01 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb751d8-2cd4-3267-b88f-042b4d11712d | -6.40458 | -42.81039 | 2025-10-01 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb1ac4ce-e817-388d-b0af-cfd3e7ffeb63 | -3.91297 | -54.56577 | 2025-10-01 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c271af1-86dc-3b47-8ce4-56b5735c5c99 | -7.8405 | -47.06724 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 596dab28-df75-3d17-b812-4de06d69dad6 | -3.46995 | -50.09532 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2742e79c-37e9-3e8a-b768-c17ce0097280 | -8.28531 | -50.80352 | 2025-10-01 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bde1ed7-50bf-3f1e-95a5-083309901cde | -5.95464 | -45.86328 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dec9f58-e3d3-35f6-ac65-3cf6c0f7caab | -6.67499 | -42.80184 | 2025-10-01 04:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 284cc3d0-509a-32e3-8b5e-3d788b191fcb | -3.10172 | -47.01078 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ce36affc-ce72-3d7a-9ab8-e68ce42e3fe0 | -6.28449 | -43.662 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d15bbe2-5897-35b1-a4f7-26945fce7fd2 | -5.93761 | -45.8933 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 615eec0b-41f2-3cd6-b540-2cf82baa0032 | -4.4007 | -50.84105 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47fbfead-c653-334f-991f-c605680baedd | -5.70365 | -42.68857 | 2025-10-01 04:49:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9489cba9-d32b-3a67-b2e7-e0f223d0d736 | -4.25684 | -48.55779 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 414e6102-85e2-3587-929c-d6a42b6cdf88 | -8.24459 | -45.47804 | 2025-10-01 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| def7bf00-552e-3961-be67-e50eb89339fe | -8.64665 | -43.98301 | 2025-10-01 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75796ed3-5480-3aa5-9e12-4e3a8b29e8f2 | -6.46533 | -43.93718 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dbd09e17-25f7-3616-bf4b-1e9f06e0656a | -6.3261 | -53.17477 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8a23ee8-a6b3-3587-a866-aed7506a9733 | -7.62727 | -46.6755 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 899bf133-fa47-3e87-b36b-272387c04849 | -4.79067 | -50.81036 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 830115c6-08b9-3d6b-b55b-cec834a4aac1 | -3.35642 | -43.19477 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c37f9c4-3b86-35d4-aee1-8fd444075ad0 | -6.23665 | -45.33558 | 2025-10-01 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86e0a932-ceea-3838-a1c2-36efa8f6327f | -4.25914 | -48.55731 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 392d8d37-a08c-3b5a-b0c8-16c025cfd2ed | -3.93065 | -41.57635 | 2025-10-01 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d44d868-a6a3-36d6-9454-5f07ff65a3fd | -7.02366 | -44.46906 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6765a1a5-aeff-3c4d-bc5a-03004a6abbf2 | -3.46052 | -50.0903 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d87bda55-d3bb-3a2c-82b1-57b2e0e50d55 | -5.9015 | -43.9175 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34f94237-05e9-3bca-b277-a93ba3cd149a | -6.1037 | -43.12955 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1645eacd-e570-336f-981d-985166481bc8 | -5.23819 | -45.5927 | 2025-10-01 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddd45197-60d0-3f06-88ff-316ad32c6243 | -5.70213 | -42.66294 | 2025-10-01 04:49:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 46a2b52b-90dd-37f7-bf86-23f9a40c38bb | -8.8999 | -45.04226 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 870ef5b0-d305-31b4-89fc-269096339b7e | -5.32033 | -42.77203 | 2025-10-01 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 74fd2299-3877-3ef4-bc40-1d455b3c03fa | -6.98969 | -42.80102 | 2025-10-01 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd05592c-a26f-3692-9ed5-c2e7d2e52bf8 | -3.35097 | -43.19896 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fbb687a-77a7-3695-b07c-7098669a9fc7 | -2.82131 | -54.03349 | 2025-10-01 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 122eda05-0756-3ef1-ada1-f4a4bf4f66da | -7.88419 | -47.27836 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abb05ef2-0d4d-3c3d-b1a7-c0b0528032f7 | -5.80169 | -43.73441 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f178a39-1884-385e-bb78-f62e4e2d62f5 | -5.24128 | -52.03719 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7e7d7d5-9f7f-3c86-a3af-dd56a13ef22d | -8.15212 | -46.25755 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02a08972-e483-3983-afb0-7f7e60eb0d1c | -7.17623 | -41.69882 | 2025-10-01 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71f76cc3-8a12-3869-813b-a224743a8215 | -3.09311 | -47.01812 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d71588b1-2449-3f67-9919-bebacecf9c23 | -7.0206 | -44.48517 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 692e86dc-1aa5-3b30-870a-19388b2f5b58 | -7.47952 | -46.47398 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52c34089-7ca6-354c-85d6-9b276b87934c | -3.81367 | -47.58919 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3864c3d3-565c-3741-a06b-014c397172fa | -5.89691 | -43.3083 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb80887e-c56f-3a2e-bd9a-c3aa28db1c7e | -3.53825 | -51.15365 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db95c70-aba5-31c2-b2c2-366839ccb6c5 | -6.36036 | -43.9539 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0387667b-7469-3788-9cea-86b02c138b6b | -6.09157 | -42.47268 | 2025-10-01 04:49:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a1d36260-7b95-3aaf-b07c-d15ef2bf2b5b | -4.95823 | -42.0379 | 2025-10-01 04:49:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a57c21f9-b9de-34c8-b31c-26af3000fcff | -7.78747 | -42.51177 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 615d9158-0445-31ae-945c-c7cd88605084 | -3.04922 | -51.10566 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be645c81-a5d7-3f39-8042-33778633ae54 | -6.47376 | -46.48922 | 2025-10-01 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 823f3606-845e-3aa9-84d9-b8621e973059 | -6.55787 | -46.5952 | 2025-10-01 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfa29af0-ce55-3e23-a5ef-017272c57a1d | -6.05462 | -44.43642 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a559b599-c273-30f9-84c6-63ba955b2c93 | -5.94703 | -45.85848 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adabc366-042b-39f7-83d8-cdb403aafe35 | -3.50054 | -52.46227 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74dc96f2-ade1-3fed-93d5-ca77604cdb1c | -6.05278 | -38.308 | 2025-10-01 04:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f25edc08-38de-3ffa-8bb7-6cd8f2203fe9 | -3.09363 | -47.02003 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| adee5c7b-a702-3b37-9e8c-04361fb03287 | -2.5928 | -48.12435 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9859791e-e90d-37f0-95ce-13ef403c1fe0 | -6.58105 | -51.67798 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a22bc2f9-d077-39d0-add5-c3adf8c04087 | -6.79447 | -44.73857 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a37dc4bf-d05f-39d6-a00f-bae83f6dfa46 | -5.9484 | -45.87694 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae35cb50-acba-3e23-969f-b54f389134da | -8.55433 | -44.71331 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc6af8e6-567f-38f2-bab7-faadef572d97 | -6.49137 | -44.28207 | 2025-10-01 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba3f570b-abf6-3b04-b194-8399776df75a | -6.04786 | -42.44715 | 2025-10-01 04:49:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4aadca6-edca-341c-b573-b7fdc769cde6 | -3.4211 | -51.23233 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8b157ad-d680-31b6-8b15-5f9a7d0ace85 | -7.68508 | -49.63222 | 2025-10-01 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adc9424e-645f-3da9-b819-0ca89f1a52a8 | -7.47134 | -46.46624 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b933ec36-c6f2-32e6-b8ad-c556bcb9f64a | -6.32157 | -47.21986 | 2025-10-01 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de84b0d8-d83a-33ff-8db2-2df42a66ce38 | -7.81708 | -47.06211 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f45406bc-1058-37c0-92b9-8ab3e54a0c6b | -8.23123 | -45.50952 | 2025-10-01 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b16eb0cc-188c-3ce9-9d43-393a89429734 | -5.76865 | -43.29662 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac22657d-3e2d-3896-86cf-044b57b208e4 | -3.45301 | -53.83135 | 2025-10-01 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0552552-3705-3432-8a4c-22b50348e0cb | -7.47457 | -46.47202 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3154f1f-f1d5-3776-a222-054b180e6904 | -8.28178 | -45.37434 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b8c16ed-ac67-36a5-b0ea-ebbf3ddbb3bc | -4.29163 | -48.26826 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf5d83e-6636-3989-bfa7-657792a3fb11 | -8.64187 | -43.98199 | 2025-10-01 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41e296e6-65bf-3a5d-9b51-13d59f996b00 | -6.87953 | -44.52942 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 543d0143-e87b-3cd0-a174-024de4a23d13 | -3.42166 | -51.22883 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0b4c5f7-d9de-3c9c-9dca-a34d15fd013d | -2.79241 | -49.62351 | 2025-10-01 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c72374cb-7688-3860-b7c7-4733bd5f2dc5 | -2.54971 | -48.40353 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ade6de8-c8ff-3aa9-8e79-ecf572ecec4a | -8.33637 | -50.8618 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02699c4c-f75b-31f8-ba8a-07ef44dc96d2 | -3.51422 | -49.44505 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29894d22-9f69-3b52-92df-0b86119f011b | -6.14138 | -44.74225 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6d1bb7b-fbf2-31ff-abd6-1bef961a2f31 | -6.81812 | -44.47425 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7baeffe7-ce1e-3502-b2ad-dd002c90cee7 | -8.85878 | -47.65658 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50f56c65-85dd-34d1-b770-792c94a7551d | -4.80604 | -50.73472 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4da690f0-0fa5-3eb5-9f1a-8c67b8abccd0 | -7.15984 | -50.54417 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3932f6e4-184e-3520-9bdf-4cabf6500b7b | -5.81318 | -42.85109 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 29ecd7a9-5add-3827-b5e9-da7941f87af3 | -2.54993 | -48.40405 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e610de-cb1f-33ff-863b-6da471d9285d | -7.16376 | -41.7077 | 2025-10-01 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d080c4a-720b-3342-acb6-2bc7618b01f3 | -5.95355 | -45.87043 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 463e8ad5-a721-38de-ad4a-27fd0b33a758 | -8.55566 | -44.67062 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb3895ad-0f62-3476-a2ee-56c7b27c27a0 | -7.83186 | -47.06918 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c32d628-fed3-3339-89f0-e67644663847 | -7.54685 | -46.11815 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64d7e4fb-7664-31f7-8991-4d7ffd84b9ef | -5.6205 | -43.23697 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71531705-3d5d-354e-a1b4-f4aff99764b2 | -7.75967 | -46.77895 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e756e1f-aee9-348a-84f1-7771384ebebd | -3.87931 | -42.5204 | 2025-10-01 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0f47c4c6-93af-3533-b9ef-a7e8c906b435 | -5.99211 | -43.4348 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README85.md)
