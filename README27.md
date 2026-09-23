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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12e6ede1-22a9-3733-970f-47ed52309e11 | -6.4208 | -59.9799 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9a04206-3db8-342c-afde-064735379736 | -8.1189 | -44.424 | 2026-09-23 00:58:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5897dd89-a1af-3764-82af-b270ccb9fbf9 | -6.6778 | -55.071602 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74534583-552c-3b88-9abe-11b3ca09bf53 | -6.7481 | -50.679798 | 2026-09-23 00:58:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09f8a675-3503-3330-92d4-22104706f04e | -3.8864 | -51.945702 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59cf6cc2-9a08-314b-ae05-240f38b19ba3 | -12.4246 | -46.9641 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8f1def3-482b-31f7-b34b-ee7f348a27f5 | -6.6648 | -55.059502 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f75311-6c71-3402-b134-cae7aba76889 | -2.978 | -50.396801 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d597e009-fcb6-34ba-9442-eeed87784d4e | -7.036 | -44.6576 | 2026-09-23 00:58:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb9573a9-40ef-3916-8518-d25e4c8800ca | -6.1544 | -57.695 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e146afa-71ef-314b-aaa5-c50b47ea883a | -5.2499 | -48.199902 | 2026-09-23 00:58:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 366934cb-24bb-351f-aa5b-a169054e0011 | -8.5948 | -54.6222 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2829dd-02aa-3a25-9a80-60696aaccbf1 | -2.4522 | -49.2104 | 2026-09-23 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021446e6-b7f6-3deb-a30a-a18982ff702f | -12.0215 | -47.806599 | 2026-09-23 00:58:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a55afd0c-41de-30c6-a4e1-694cb7454600 | -6.934 | -46.564999 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 567ec4c2-9dfd-3328-9c25-2c9439e1c542 | -5.9785 | -57.7812 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 198a0d8c-9cdc-3c7b-8a31-69a86ade4f25 | -10.0419 | -53.7757 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18cfa2aa-42cf-3476-93ae-9fdad77de342 | -6.6339 | -43.756599 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd24d23-18e0-3ade-bd31-7790955a5fa6 | -1.9117 | -58.253101 | 2026-09-23 00:58:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0332ec29-898e-3ecf-a9af-404bbaa43538 | -3.5807 | -50.0229 | 2026-09-23 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c83a248-aa48-3e14-80ba-8a05f29400a3 | -11.1198 | -48.3083 | 2026-09-23 00:58:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47c02733-7553-33a4-b280-03e6b95bef57 | -3.0945 | -60.709599 | 2026-09-23 00:58:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ceeab0e-f7dd-3b1a-9a57-6ee81f6c1845 | -11.8642 | -45.759998 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58720d2c-bdf3-3cbc-9f6b-d1b2d8569b29 | -4.3261 | -55.423199 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de10a623-9b57-3ea1-940e-9251ac34dc30 | -11.4498 | -46.705299 | 2026-09-23 00:58:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4666e1db-f118-3432-8cb3-65052b4e8e05 | -11.7063 | -50.772202 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9a4242c-e65b-3a3e-850e-cf913658fa94 | -5.7793 | -47.1506 | 2026-09-23 00:58:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9826084-fb7d-34a1-a5e8-5a1556db5f16 | -8.2792 | -54.7757 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59eba7ce-f71a-33f6-9d51-cd2d24a544a8 | -8.8147 | -44.245602 | 2026-09-23 00:58:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b35942c-e028-388a-b439-c23f563609d6 | -2.966 | -50.3899 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294bc04c-6631-32c4-a9ed-d5bb668324bc | -9.5657 | -46.527302 | 2026-09-23 00:58:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0da8b1-2418-3e10-ab9f-d11fde2ae76f | -13.303 | -47.884602 | 2026-09-23 00:58:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dedfd7a-3673-355c-a0f1-a943d309bca8 | -8.1929 | -54.711899 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286e536c-8f21-3e30-8eb9-d35dcabc29d4 | -7.5553 | -57.6744 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13173f7e-a488-3272-af5a-05964d51aeb5 | -6.7854 | -48.667801 | 2026-09-23 00:58:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| be9ab06a-1f3a-3ee8-9ed2-fffd2c0445b5 | -4.4577 | -47.903198 | 2026-09-23 00:58:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f25da6-1432-346e-a80e-9e59267cf8a1 | -6.4463 | -48.459 | 2026-09-23 00:58:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2d109d09-7937-368a-87ea-4b0f5349c592 | -11.5058 | -51.5103 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43bd57d2-d46e-3d37-920f-21fca014e8c0 | -6.5937 | -43.719398 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faaf4176-2c75-39bc-b5c1-ecdc5a52ea6d | -12.7547 | -50.8843 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8cebb24-8295-3b11-b688-bdeabd9b8d77 | -3.757 | -59.460701 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c916d437-780e-3d37-b3e2-6542a243f123 | -7.4176 | -49.844101 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2790cbc-4517-30ff-b48b-5e1e7879a571 | -2.6007 | -59.7477 | 2026-09-23 00:58:00 | METOP-C | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6db381ff-a24b-3100-ad00-a575b4b83fb2 | -3.2911 | -57.849201 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf3874c-697a-3964-a617-27cda0a742c6 | -12.7793 | -50.901299 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8fed280-df25-33fb-a771-7fca99bf8159 | -4.564 | -54.929798 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6b1666-9d6f-38f5-80f7-62158336b2c7 | -12.8087 | -50.894402 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f961d83c-25b8-3a14-a33e-44ff284c3804 | -12.4884 | -46.971199 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30586e9d-ca80-356c-9762-089fa7f6fd2a | -3.1852 | -56.837898 | 2026-09-23 00:58:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14552277-b672-3fc4-a461-d6949ebb8f73 | -2.1126 | -49.693199 | 2026-09-23 00:58:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef067948-b57a-3ddc-962c-6d1d55f2dc15 | -11.5139 | -51.5009 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b543c39-38f3-3fa2-b1d5-b9ea9d56d72e | -10.6118 | -53.975399 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4cdf8e3-5e17-325c-9cd4-b35141b21976 | -6.6008 | -59.914902 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5761b040-6c33-3fa4-854e-c4139e99baa0 | -8.9487 | -50.904301 | 2026-09-23 00:58:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87af703f-6451-3319-8041-5d850316cf3d | -3.33 | -59.842701 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04b918a4-0500-39a1-a250-af18f3133ec3 | -5.3517 | -45.1548 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 465330a2-6c5a-3c43-b173-1cb316ee1621 | -11.8967 | -45.7658 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa628322-6e6e-31f5-b02d-5365655fa216 | -11.8739 | -45.7575 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78e70208-d1fd-3ed2-9051-35a4560aaf83 | -8.7954 | -44.250599 | 2026-09-23 00:58:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 352533ad-aab5-3d6d-b788-eafab7f95775 | -8.4811 | -57.595501 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e16c02c8-a81c-311e-9b32-3a08d7a7408c | -5.4082 | -60.2094 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bff982b7-7f57-34ec-88b2-221df7084fad | -3.5059 | -53.197102 | 2026-09-23 00:58:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c0d8d4-a794-36fd-aa8f-756584dac8a4 | -3.6582 | -54.261398 | 2026-09-23 00:58:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a22412fa-b092-35b5-bcd0-22f253b08a66 | -3.81 | -58.873901 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0c1eb5f-eca2-3784-86ea-23767e676948 | -9.9737 | -50.256401 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7201d856-22b1-3035-90ac-00757f697332 | -7.5503 | -55.013699 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a27e9d7-278b-38de-8094-524c93329b87 | -7.5601 | -55.011501 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90f19c1e-8d82-3b96-95ae-b41f80519a1c | -5.8929 | -52.2761 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11510e60-4fdd-3acf-8e87-3fefb2dd1fda | -11.7076 | -50.910702 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c902998-a9a4-3578-b74c-f571bf2716d3 | -3.4832 | -59.5658 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d64e37a-eb49-36e8-99ba-9ad582225530 | -6.6231 | -59.923401 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9d4e1a7-569d-3f56-a38a-d1d1ea05ac69 | -7.3901 | -55.217098 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2474c625-0bab-31b6-9844-acae99357976 | -12.7891 | -50.898998 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb212c1c-544e-3a59-9209-6ca43defed55 | -11.6981 | -50.959 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2786a796-fc8a-3831-85ce-c593732d62de | -3.3029 | -57.855598 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf84f4c4-2d5d-33f2-9153-0d8d917798f4 | -4.4508 | -55.020599 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0524c0c5-3584-37e5-801d-7f75ff1bdd34 | -6.0775 | -57.626099 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00ae3f38-c450-3f89-b590-411b078e6baf | -9.5678 | -47.9622 | 2026-09-23 00:58:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2649ccd9-854f-3ca8-a260-78ce2af42e3e | -11.452 | -47.3825 | 2026-09-23 00:58:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93f36c62-cdde-3b94-86aa-b5d14041c67e | -11.6802 | -50.970901 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f79a3db-ffc0-3950-82f8-93ea85030217 | -7.4295 | -49.850498 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a92be98f-1675-318b-9e9b-0aaa33552c1f | -5.7339 | -53.464001 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69d5d34-0c57-3da6-a347-98754759c801 | -11.741 | -51.009998 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf2611d0-9131-31e6-9084-6b045e174399 | -5.8065 | -49.146198 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79799c6-4456-3a66-8cbc-9ca49c6781e8 | -11.8933 | -45.752499 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b807d746-7ea8-33ad-93fe-825630a35701 | -6.6844 | -55.055199 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d95b2a-2777-377b-a422-f2d9ca6017e9 | -10.3126 | -50.510799 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 532b666f-7b0d-362e-af12-c3acd422c533 | -6.6203 | -59.910702 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 376a366b-5d44-370c-a206-81369ed921a9 | -5.7482 | -51.920101 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e011af67-b3fa-34fd-b8fd-eb4b976ab043 | -11.1221 | -48.317799 | 2026-09-23 00:58:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 011eb91b-96d3-38fd-ba7b-9ab8e939e2f0 | -3.2353 | -53.947498 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6e8629-e08f-316a-8645-62665208c94b | -6.7829 | -48.657501 | 2026-09-23 00:58:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 03234580-803f-3531-afeb-fa632aa08d5c | -4.2956 | -49.123001 | 2026-09-23 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecea0d20-5019-3f95-bf20-75a78edcfa1b | -11.8705 | -45.744202 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe49572a-ebb5-37cf-99b6-e6f4f9522154 | -11.8802 | -45.741699 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85a9f66e-90e7-3330-8974-256f84f0ddeb | 2.9386 | -60.4319 | 2026-09-23 00:58:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09f8e5be-e0f1-3235-803a-509f4bcd3339 | -3.6912 | -60.539799 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39b757d0-6bff-3397-bd32-391502244070 | -8.8411 | -50.4911 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fdf0bef-638a-30d0-a225-58a59407de8a | -6.0287 | -55.344101 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e91df053-52ae-3887-9816-9ca5ffc3faf7 | -6.9209 | -46.553299 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README28.md)
