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

## Dados Diários - Página 296

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27fea1e5-d664-352b-97da-a7ed13d3104a | -3.13445 | -42.93551 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c837bf49-4d07-3a68-9838-b71cb0a34852 | -6.18448 | -44.10589 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2d71f9b-5497-39f8-bc3d-5feb70675742 | -3.62853 | -44.80983 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f504b5b7-85c4-376f-9dc2-dbb7b5e9b1ca | -6.53769 | -45.36734 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f87cfa7b-973e-3385-bf60-0697bbf12825 | -8.34582 | -47.65992 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7aa9a1fb-deab-388c-ac95-2c438c796442 | -2.2509 | -49.81285 | 2026-10-08 16:20:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 61ff6bd0-56d5-3e25-ac62-488df175fb34 | -6.81302 | -44.18505 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad8800ca-2071-3289-b1f5-adcadaae7c4b | -3.52904 | -44.31141 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8350c838-ec51-3e4f-903a-c3704735c447 | -3.30465 | -49.12734 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 20038a5a-cce9-322d-8d19-e71ac87766cd | -7.38111 | -46.23015 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 56272cd8-622c-31c1-aa4f-675fd8b13c76 | -3.90735 | -44.38446 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 443d722b-e7b0-3c27-8c5d-269acd7fb10a | -6.09913 | -53.50438 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 65fbded2-df6f-31e7-9292-87a7038c1815 | -6.3214 | -37.75085 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| a081ff9f-4171-3a27-be21-105cf9c9187f | -3.41819 | -42.9116 | 2026-10-08 16:20:00 | NPP-375 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5ef018c-49b9-3103-8597-d3cc65de740f | -4.15732 | -43.19427 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f14ef200-28a3-3ab9-ad7a-80bd828f513c | -7.408 | -43.74572 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6de60853-f467-3e29-999b-63e4c89729ec | -6.15227 | -39.43767 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| ef73c3ce-c8e8-3221-ad75-508ebd60b618 | -5.99089 | -40.94228 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 2596dab5-83c6-3670-8db0-3a3cf938b243 | -3.4146 | -42.91211 | 2026-10-08 16:20:00 | NPP-375 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5daae480-2fee-3a22-bbe6-19d37fe81a4e | -6.82157 | -39.54795 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| d7c2fba3-4afb-36e0-bae8-99cdb88404cf | -3.90025 | -42.11629 | 2026-10-08 16:20:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| b02139a9-a6ab-379a-9c27-833d181951b4 | -2.46705 | -46.01514 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 001123b9-c5ee-355b-90b2-25081a0c9242 | -4.93661 | -37.37915 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 324de6c7-f1fa-3a00-a8df-90501dd117f0 | -6.37653 | -42.52841 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 7ed90394-43dd-3005-ae9d-400281037520 | -5.37365 | -45.92422 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 629f8436-5382-3e3d-96ef-8063c91867c5 | -6.19811 | -45.40898 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4aa7574b-2145-37fc-89dd-3dd3c853ca55 | -5.30013 | -45.72524 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f37e15a1-505f-3d29-ac81-8564db867f0a | -6.82437 | -39.54399 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 59f622a4-dc89-354a-8565-b0f295c05743 | -5.87054 | -45.96255 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 60a2f155-1826-346f-9c1f-766f109d1c53 | -5.7429 | -42.0634 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c2060680-649b-3410-b07c-30095193463b | -7.70546 | -44.74634 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4d0bd42-def4-3787-8d46-a57a021a21a3 | -5.97195 | -40.9082 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 676b929f-150c-3c4b-ba7d-83a16d7010bf | -6.3345 | -44.87395 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 494db5fe-d60d-3084-913e-902c31ea819a | -6.90407 | -45.89442 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cec6040b-0cee-3374-a1d7-dd04b95f7381 | -7.11445 | -42.53671 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| d43bba0a-d206-3885-b183-b9c8e803aa88 | -6.61685 | -44.91995 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a159d512-9cee-342e-b6d3-6756230a3b28 | -6.59429 | -44.85217 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dacc8d78-48e3-3027-b760-f993c8b86407 | -5.50935 | -42.85101 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| f5fe7ed9-7836-3859-8427-0f7e6e1db042 | -6.24431 | -52.88364 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a146b994-09a4-37d3-bae0-da8ddbf6e0f0 | -7.53502 | -42.08366 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| fa42eeab-4a65-3ea7-b6d1-595cc8c9aaa4 | -6.43875 | -45.93089 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc76a9b3-9fa0-3fa7-984f-8020aaf2c2d0 | -4.0863 | -44.13387 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a3deb8cd-2359-3c6e-bd44-df58a5f357ab | -7.06529 | -40.94899 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 335a1e69-caa3-3eb4-a2cc-42f6fdb4eabf | -7.39623 | -45.64737 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fd0d75d-fef1-3133-894e-51615417d7d4 | -3.96512 | -51.86442 | 2026-10-08 16:20:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3f95f7e6-b896-34a2-afbb-4d286dae5c1b | -5.7529 | -42.05791 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b204ed78-81ee-3d90-8f9a-bf26b10f0ccd | -7.39494 | -45.63838 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 01c63321-bf55-3c85-b29d-bd6f1f5909f3 | -5.93308 | -44.2791 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f758845e-44ce-39c1-aaf5-9a77edd7e569 | -3.8517 | -44.12369 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 48516e19-a33e-391e-88c9-7765b8369dbc | -5.74555 | -41.72156 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| f41ddf0f-6e40-3498-a25d-f8a3629419a3 | -4.15 | -43.19541 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d69159f8-38ac-3ea7-b56f-aca9e4abfdd4 | -7.4573 | -42.83095 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5714b443-a820-3f83-8040-21a3a76471a8 | -1.16704 | -49.34813 | 2026-10-08 16:20:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bcb7e88-e590-30f2-97f9-30f04decd48c | -7.10221 | -42.52976 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 5f9dc20a-b6f2-36ed-b087-c20e94a5c183 | -6.97679 | -43.29053 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5c2e79bb-8d72-3f2b-a990-5e52d6fe6c93 | -3.51742 | -44.31313 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d8e01d57-25fe-3541-bc28-405292083be6 | -4.59529 | -43.58771 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3bb7d3fb-5241-3420-b246-8a82ede194b4 | -6.8545 | -41.74515 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 2dae0b9a-358d-3e31-a35f-e0f3bd16c157 | -2.80595 | -51.72692 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7d7b939-f6de-37e8-9287-c3a188546028 | -6.68369 | -45.08272 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 430e792b-7b48-32bc-9766-4c18cd3d07d4 | -4.74901 | -40.50198 | 2026-10-08 16:20:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| edeaae43-5466-390c-828a-5aae13ef71ff | -7.21015 | -46.5289 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1e15b5b0-d51f-3345-a162-19defde8ff3a | -7.18774 | -44.28602 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4299522d-c2ed-3cbb-9eaa-da192d98d399 | -3.91126 | -44.38388 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6a5a343a-d879-3f2d-b6c5-47a8a8410f6a | -6.89499 | -45.89545 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1cb82425-1f3d-3678-a157-065257e2ecde | -7.76175 | -44.16582 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73c4a2c9-f564-3170-a957-862b94276334 | -5.51261 | -42.85213 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 265a220f-0304-324e-8abb-efdfc79574b0 | -6.93388 | -44.88464 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9474cadc-42af-34fc-bf8c-23cddb8868cd | -5.35314 | -45.72178 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebdc2eb8-e2ff-38e6-952b-043e540836d3 | -3.85243 | -44.12848 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2f59b0e3-fe08-3c81-91b4-e37c08731187 | -6.10366 | -47.04476 | 2026-10-08 16:20:00 | NPP-375 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 68a48209-fcbb-336a-8be9-32c107fc041d | -5.34067 | -45.72802 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1567751a-c5f7-3c61-9e66-6267305c409d | -4.36518 | -40.41945 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c42a086d-7be2-3d74-88c8-4a958e9c8bec | -4.7259 | -37.74482 | 2026-10-08 16:20:00 | NPP-375 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0da6c363-30f9-34fb-98cb-dd2c4f20493b | -7.74919 | -43.8152 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a7409cc6-6cae-35a3-af94-ed67222995b2 | -3.5982 | -39.14271 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1b62b653-8b26-3c41-849d-e7676624b2c0 | -5.69843 | -53.47424 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 3c7775bf-aa56-37b2-b0ee-5106b1473e83 | -3.29189 | -42.28785 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 95e5236f-2e42-3beb-b9bd-211a472c1d2b | -6.14787 | -47.96025 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac17a6de-a40e-30d4-99b3-463641f453ca | -3.85311 | -44.12046 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2688637f-bbe1-3fe2-94c3-02fd102e84aa | -6.16729 | -52.64833 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ffc07276-7dd0-3dd0-ba74-410285ede40b | -7.08515 | -52.6771 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| fc9d035a-7204-33c7-acf5-369c0810dba2 | -5.95743 | -40.93291 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| d7360d7e-d4b8-363e-b263-3337c418a197 | -2.07932 | -46.56779 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 480.7 |
| a6b3c09d-b74c-3fc0-9ff6-fa998bde85bc | -6.94967 | -44.4169 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 722c73f9-2091-30d1-8c4f-2d5a8b1b971e | -7.25876 | -45.34519 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 14bef896-a094-3239-880a-9bdd17e79ab1 | -3.00528 | -54.09643 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a9874f89-344e-3898-9576-76ed41ef3179 | -6.05461 | -42.91356 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 175f8365-92c3-3820-a7b6-cb6b5b70636b | -8.01767 | -50.15045 | 2026-10-08 16:20:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 137a2441-0618-3ee3-b65c-ef83bc6ee58e | -3.81459 | -44.6001 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c1303e9c-7d87-37c1-8d0e-addb700e161f | -6.38516 | -45.04424 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bd9409b-4274-3873-9b93-4d1127c9bfdc | -6.625 | -37.88117 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66b4bac9-8fd2-37bb-bf28-958fb651f465 | -7.19065 | -52.62174 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 62d588d2-cf02-307a-a616-c60eb4b1c186 | -3.29719 | -44.68034 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f87a258b-2354-3e08-9c0e-8190e5bb2cef | -3.79578 | -52.39661 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 48c2a44c-e096-3c86-a72d-9bd05b2bd9ba | -6.15944 | -39.44012 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 591524cf-c594-3606-ae9e-76369fdc9008 | -3.79926 | -40.45489 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6bb7d9b6-7f73-3b21-b18a-ddfe5d6709f7 | -3.52129 | -44.31256 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4b62e7f9-4221-3588-84b6-ee18d4e58d66 | -6.02911 | -42.71994 | 2026-10-08 16:20:00 | NPP-375 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 19d65389-8786-3e98-afc0-20bdf21f62fb | -6.96152 | -47.66744 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |


[Clique aqui para ver as próximas entradas](README297.md)
