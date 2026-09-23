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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcee6396-2590-313b-a14b-c8a601428279 | -6.0895 | -57.680401 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2e3fc8-3dcc-3ae6-92c3-c22aff9409df | -3.4881 | -59.177299 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 953168e4-2c6c-3c2f-9e1e-bc69f93b262d | -6.6064 | -59.940399 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9d249a-0aaa-3d53-882d-bb024a6b41a2 | -11.7097 | -50.7869 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1235c47-eb42-3e54-ae8f-281983b76583 | -5.8214 | -52.057201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0809f08e-c9da-318d-a017-86ff6dd363a9 | -6.9174 | -46.5392 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70b45ca2-2333-32b8-a012-aa3c313795b1 | -12.8394 | -50.8489 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7defeb98-4b16-3858-86d1-0bd61eb752b0 | 2.9289 | -60.4296 | 2026-09-23 00:58:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 602d7b62-e6ab-3294-93ad-902fc1fd7b92 | 1.4364 | -50.803799 | 2026-09-23 00:58:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a7334bde-e75f-3d18-8708-c9551504c0fa | -6.6134 | -59.925499 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f99380bd-3eb5-3b78-97db-c256cfcd2855 | -13.8554 | -48.584599 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23c92879-747b-317e-a4fd-72b3add6d4f5 | -8.2482 | -54.775002 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503e0439-0335-319f-a408-4724f42a9d8a | -6.1786 | -52.7971 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b492ed0c-e59a-395c-ab65-8af68ff35730 | -7.8673 | -61.164299 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3678e218-eae3-39f2-bbec-24fe42cf9934 | -4.5609 | -54.915901 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a00da542-5c97-3da8-b627-c2cb1b969ff6 | -12.8134 | -50.8703 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb0281c5-08c3-3523-a1ae-b257ee0cbe4a | -11.7507 | -51.007702 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bfa4abf2-e551-35d3-b0b7-a45b52810d57 | -3.4533 | -60.254902 | 2026-09-23 00:58:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c82fc949-d915-3e75-bc76-53c299f3e33a | -4.5214 | -54.968498 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5fcf11f-53ff-337e-94fa-e6da168af6b8 | -11.8608 | -45.7467 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1216e1-2962-3c64-9c23-4d89db66ba6f | -13.8709 | -48.562599 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d107f138-77a6-322f-a4de-dcd9ff970512 | -9.5123 | -59.746601 | 2026-09-23 00:58:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90f969ac-b812-3960-8d8e-01a901836cb3 | -6.1281 | -52.757301 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e240489c-b78d-3ca7-9eb7-acb3102da0be | -8.1697 | -54.7925 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eedc35c0-3679-31a4-9b5f-68850301ac45 | -8.2387 | -55.2379 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be7b9da-09ab-3186-a4a1-ce8e98e4d7c3 | -8.3638 | -45.598499 | 2026-09-23 00:58:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8a1a4c1-4419-33f8-9cbe-c66c7be344c3 | -12.7661 | -50.889198 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7efa778b-6da4-32d4-b551-567d4813807b | -4.4391 | -55.059799 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9a2881-89cc-3538-9e57-0033b97a2df5 | -6.4428 | -54.9893 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be266943-34fd-3a34-83eb-08345bfe22fe | -7.8639 | -61.148102 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35618abf-08c9-3881-8d75-073e268ccfee | -12.1242 | -47.3815 | 2026-09-23 00:58:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7ba86f0-5964-3d2c-9a2b-f766e62c25f9 | -8.4909 | -57.593399 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6f040c-7541-3d1b-8d2b-ee8d28947461 | -3.7278 | -59.421902 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbd1a26-ea43-3660-8dfd-d39765f9fc10 | -2.1004 | -49.685001 | 2026-09-23 00:58:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0881a4b-e379-3d2a-b241-f11821d463ce | -11.7768 | -50.986301 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efe0e28f-a92e-383c-ac9c-8ce228dcd1b5 | -6.4444 | -54.996399 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5344ff1d-30ed-3c1f-baef-6ef43df34c9a | -7.877 | -61.1623 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d882730b-4bde-39bf-a4b1-d6892f2067ac | -3.8096 | -52.3699 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4aae360-02bb-3cbb-a0da-eb6935c470ee | -11.4583 | -47.3241 | 2026-09-23 00:58:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddfc20f5-727e-34a0-a348-e5c319e87d42 | -8.8051 | -44.2481 | 2026-09-23 00:58:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf4a38cc-1a39-330b-85ca-a071a7fc50ba | -7.176 | -48.618099 | 2026-09-23 00:58:00 | METOP-C | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6f331c8b-ffce-3888-b918-f0577c0368f5 | -3.8062 | -52.355301 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f5e2d5-ca1c-37db-9616-ea64be5a93f0 | 2.941 | -60.421902 | 2026-09-23 00:58:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bfb61a06-6b11-32dd-803a-2760703b0776 | -1.9235 | -58.259602 | 2026-09-23 00:58:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 614357d5-fb27-334c-9fa8-5e551317e944 | -7.1398 | -43.085098 | 2026-09-23 00:58:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1317ddd3-2ec4-36a1-ad2f-0196cac39deb | -6.1091 | -57.676201 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba00a248-eacb-3711-94b5-ee5f042c4182 | -3.3831 | -57.9375 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98a0693f-6ec4-348b-93f6-f29752d4dc30 | -3.1834 | -56.830299 | 2026-09-23 00:58:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba7388e-8854-3f6c-95c6-194318cc8d67 | -3.2931 | -57.8578 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87825916-a419-303b-a277-4a923a25c63b | -5.5033 | -51.7108 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fbecca-77fb-3a96-becf-0630c30673a5 | -8.4707 | -48.678299 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e61a63a8-051b-38f1-8639-8d3cbca6cfa7 | -10.3802 | -54.4142 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e184aa41-f511-31e5-916a-b1756d9df25c | -5.1244 | -48.794701 | 2026-09-23 00:58:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a5d725-72e0-3b2b-ae67-4a1037ce068e | -3.8478 | -58.813702 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3fa071-4c60-3d94-a56f-8cacbd502c9e | -11.6718 | -50.934502 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22fed2cc-8144-3b1f-9697-9965adc8c2c0 | -3.5075 | -53.204102 | 2026-09-23 00:58:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc14c7b5-a104-3816-8e20-8829548702d0 | -8.4731 | -48.688099 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e4e48d17-861c-36fa-bcfc-91b9a0f57472 | -3.6814 | -60.541901 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72db6e5a-3b2d-37eb-a0ea-fe980f0d0ad9 | -9.5755 | -46.524899 | 2026-09-23 00:58:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f738cf-1603-3d11-9737-d9d35f8a017c | -5.9829 | -55.3694 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c279ca-d54b-3c0b-b93d-106956aee74b | -2.765 | -57.028 | 2026-09-23 00:58:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27955b89-4b58-301a-968c-6ab4eb629a23 | -11.3098 | -51.376499 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d96528e-238b-3dce-9311-8f6b2df95b2c | -11.461 | -47.334801 | 2026-09-23 00:58:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f88cd0b-6a9a-30b9-b634-7a4f0e5342e9 | -3.6033 | -60.5588 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a19c9cd-a8bf-3f91-97b2-18e74986a7f8 | -3.1825 | -59.688702 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8629251-9c44-399d-8950-c1b23489c8f1 | -6.0993 | -57.678299 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1816349a-2641-3271-aa33-8485ba4c518f | -6.0065 | -45.227299 | 2026-09-23 00:58:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e83f4bb-0548-3753-b00f-4ece9cb950aa | -9.9639 | -50.258701 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcfa38ae-9339-3797-900f-5b7783584d01 | -12.8509 | -50.853802 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7f5a9a-b3f7-36cd-8e5d-a20180bba88d | -12.4743 | -46.997898 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4b836d-055a-3643-b6bf-acdff5b5e05f | -12.0191 | -47.7967 | 2026-09-23 00:58:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3929b59-39df-3f4e-beba-19f39d3808d4 | -3.0779 | -54.384201 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6199d1-56ee-37fa-a31c-315fc96678fb | -6.0873 | -57.624001 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d4b7b4-f0c1-3a59-b9d7-5a1d7f35e10f | -3.5321 | -59.6008 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8531bff4-9d7c-3c25-97a5-7c174b96ed90 | -6.6033 | -43.716999 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8237fc-f53f-3296-b315-0289cb87b1c6 | -2.1028 | -49.6954 | 2026-09-23 00:58:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b62cb47-66dd-30ab-85ee-053b96e80eec | -11.3146 | -51.352798 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 401c191b-3d8e-31d4-b61b-db14e64589d1 | -6.6717 | -58.551998 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d654148a-ff11-35c2-845e-2c54b6dbecbe | -8.4853 | -57.614899 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff547206-102c-3c16-8b36-1736b9a8c513 | -10.2648 | -50.2202 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9335fd7-88b2-3492-8c7d-c821785f95b7 | -11.8866 | -45.7258 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4aa66d-a609-3f75-9acd-dd874f239289 | -3.8122 | -58.8839 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb05e3a-6cbe-34be-ae59-e230d90fe1f2 | -6.0875 | -57.671398 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03be4fc0-6f22-3c11-a5c9-a1f0c1242581 | -11.5253 | -45.361698 | 2026-09-23 00:58:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 289d1a91-b4b7-3888-8adc-305262a097c3 | -8.3103 | -54.776402 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd80a02b-db84-381d-9118-4d619991f85a | -2.9454 | -54.077301 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a053ea7-ad97-336a-99de-3d384a015ba6 | -6.298 | -57.740601 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a23e825-6bcc-3c9e-b3b9-0412e0ae422d | -7.5651 | -57.672298 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc5469e-68b7-3c27-8906-2f828a5a2160 | -4.5312 | -54.966301 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 053e4e67-5e6a-31f1-9062-13350fa9a8da | -3.8598 | -58.8214 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab3ca943-97f8-3762-b343-1f7a99e39515 | -10.2594 | -49.978802 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a76f046-11d5-361c-b5bf-b2655c57368e | -8.5964 | -54.629398 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5517ceff-a7ed-3324-a411-1b9d66872a77 | -8.1961 | -54.726299 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4f46922-9d51-319e-84fb-d7cbcb3748b8 | 4.1033 | -60.999901 | 2026-09-23 00:58:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6c404a-37c7-3f03-bcf4-a4965b5190fe | -6.5993 | -43.741699 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b80e3734-c47e-3cca-b44a-266e83f26f3f | -10.9122 | -53.938 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81d19678-cc1f-37c4-a93e-20bf92e9d090 | -6.177 | -52.790199 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748184a5-4923-37a6-b5cb-3a67b4739a1b | -11.8773 | -45.770901 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdd896eb-2296-3149-8048-7ad4c3f5b9ae | -6.89 | -55.327999 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4124e5e7-c6d9-36ce-9121-10656222808c | -6.3077 | -57.738499 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
