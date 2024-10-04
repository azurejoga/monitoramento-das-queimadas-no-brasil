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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c10cb48-c523-3f27-8bdd-561314431bbd | -15.77414 | -54.20473 | 2024-10-04 04:34:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc4ef9d-d3db-3b1a-86c1-525923e108e7 | -10.38519 | -53.79376 | 2024-10-04 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ed9c3c-d844-3299-81be-9cd3c1654293 | -10.38115 | -53.79299 | 2024-10-04 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e16c03-7922-34f2-aafd-74bb3406c83e | -12.14695 | -54.26526 | 2024-10-04 04:34:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2db7799-e2bf-3713-a316-2513f2c78d8f | -11.58861 | -54.48294 | 2024-10-04 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 032ecc8a-1bfb-370f-84fd-b33ef2f5a26e | -11.58794 | -54.48676 | 2024-10-04 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 39447215-31f4-3395-b1dc-1c6954113a55 | -11.58447 | -54.48215 | 2024-10-04 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e1d2bf6-b4ab-3e07-94f5-32322882ecd3 | -11.5838 | -54.48598 | 2024-10-04 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73d9d525-f233-364d-a3e2-0962a7e6542b | -11.35475 | -55.19339 | 2024-10-04 04:34:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fef0a358-3eab-3021-aa73-678865b8182a | -11.35039 | -55.19257 | 2024-10-04 04:34:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1435d73-da14-3fe1-b643-bb0e79e5e0e9 | -11.34963 | -55.19685 | 2024-10-04 04:34:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c570fc-9822-35db-ad74-41032bd3521a | -11.10164 | -54.22169 | 2024-10-04 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3cd286c-1907-38b2-80c1-f38ea95489b9 | -11.10099 | -54.22546 | 2024-10-04 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08014bd6-8943-33ab-acfb-49f42f539be1 | -15.39958 | -55.81756 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95bd796d-3506-3c8e-83ef-fb9e37e98c34 | -16.57249 | -55.92317 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3141e04a-bf43-3930-828a-da3b98833d70 | -16.57243 | -55.92271 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9dfc08a-03f8-3b36-8863-f59ba0ac759b | -16.57212 | -55.94736 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| be6ddeef-83f4-3175-b0b5-8c3490b9404a | -16.56903 | -55.91834 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c44de0b1-bd9a-3dcc-bf74-99a3f6237c8c | -16.56831 | -55.92231 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0de82fe8-27fe-397f-a6fb-874e579f28c9 | -16.56825 | -55.92187 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 53cb5c33-d2a8-302e-9f40-e5e7f88455d3 | -16.14047 | -55.91478 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a9d67283-0975-3f02-bf95-f861846bd205 | -16.13974 | -55.91405 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a2cf85fa-1398-3a53-90fc-c2d9079a6f09 | -16.13625 | -55.91395 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cf5ddb2b-a45e-335e-ac42-a38c0edfd026 | -16.13551 | -55.91805 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 233f59ee-58e9-3e48-9e90-8457dc32014e | -15.39575 | -55.85516 | 2024-10-04 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63033e5d-a53b-3039-a82f-6f5add2a20f2 | -15.39351 | -55.85122 | 2024-10-04 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b4bca03-26e2-3a39-8982-2e2d18a2868d | -15.39269 | -55.85576 | 2024-10-04 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ee6d2c-a1c1-395d-b429-f9994c908850 | -16.14322 | -55.91872 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 571f7e7f-b422-3c78-a995-786b8e1390bd | -16.13974 | -55.91878 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a2875298-88e7-3c8b-a51d-46d5c8d318e3 | -16.13898 | -55.91806 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 470082f4-58de-3ccc-bd66-398c24b125db | -16.13475 | -55.91731 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1e52c815-96c3-3c04-9f6c-873972c3202c | -16.98021 | -56.15422 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 568bb3ef-7acc-3da4-bb08-70e7b1d761aa | -16.97944 | -56.15827 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 93e4140e-231e-3738-855a-822b25333309 | -16.976 | -56.15335 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4a2810d1-f7d4-3f86-8935-fcaf0db6e04a | -16.97533 | -56.58174 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5d69e9a6-3703-338d-b0df-24d5d752c8ca | -16.97179 | -56.15249 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cea55756-2006-3a0e-94f3-e2906e81ea9b | -16.97102 | -56.15654 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ae164ba8-718a-3950-b899-3ec35ac5ed87 | -16.96757 | -56.15164 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 19013603-4279-38bf-b471-aa77980df274 | -16.9668 | -56.15569 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 969befad-335c-3b25-805c-db61ab0a4e69 | -16.77603 | -55.76011 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5a283113-8c0a-3cff-bcfe-954035392591 | -16.76082 | -55.77302 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d442ad92-be5f-3aef-93df-80e186c797a5 | -16.75741 | -55.76832 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 797b8b55-fe1b-3599-ac69-d2f90a3bbdc9 | -16.75669 | -55.77218 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 52ad82b1-f006-3429-9788-ba56df9d270d | -16.73044 | -55.48472 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8e851a87-ae67-3190-b21c-1d994c44b28b | -16.72098 | -55.46744 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ad81514e-d889-3c2f-8539-ae17b484774e | -16.7176 | -55.46297 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ac2dfcc-ed44-3a95-a6a8-46cd29e0c1da | -16.71693 | -55.46659 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cba324cb-63eb-331e-a6e3-bc0c499fb796 | -16.71355 | -55.46214 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bb96e9d9-0948-37be-af3c-bb558437e66c | -16.71288 | -55.46575 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8fcff88c-f960-354e-8ffd-b5531b911480 | -16.70951 | -55.46128 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 924493e7-950e-3698-9caa-1501af5208c1 | -16.70884 | -55.46487 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6355cbb6-5379-32ff-9598-9382a4a53f2f | -16.70481 | -55.46399 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e0fbac66-6ba7-3c92-bc02-60baf33324e8 | -16.70142 | -55.45953 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fa0db666-3f4f-390a-ac6e-8843c9ee7b1e | -16.69738 | -55.45869 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 11fd64f6-dd4e-35f5-8f5d-f2f065a3ef08 | -16.69669 | -55.48528 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a232cddc-8b3a-32a8-b90d-34f3d399dfa0 | -16.69602 | -55.4889 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4d3d7419-b926-3a51-b29b-af305d786bb9 | -16.69328 | -55.48097 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b8d43ef4-6ac0-3326-b41b-354e2a3e88d7 | -16.69265 | -55.46156 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8aad3d75-44f9-31a9-bd84-287378d5a015 | -16.69261 | -55.4846 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4dd88ec4-84b2-3ea3-8e3e-1cffae7cc11f | -16.69196 | -55.46529 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d264845d-535b-3fd3-9300-859c637db01c | -16.69126 | -55.46907 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fbd800d5-ab5b-3ee4-b942-e3bbf97ae966 | -16.6892 | -55.48027 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 30197f56-4136-3edd-9825-12b9dcc53ca4 | -16.68787 | -55.46466 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 201d3acb-871b-3de5-857f-d3e7e3a23382 | -16.68652 | -55.49479 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56660952-5be0-314f-be63-9c58c22b67d6 | -16.68224 | -55.54086 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 12b527db-357c-3c54-b7b4-a149ed3270cc | -16.67818 | -55.53998 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c28935d8-0b23-3e62-a507-35699e1cea41 | -16.67412 | -55.53907 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b24f4827-89d3-3fff-b968-ad7506019953 | -16.67226 | -55.50356 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a586c4f4-7cdd-3bf5-9b7e-ead94b30b94d | -16.67159 | -55.50718 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 64ffd380-6a6f-3ac2-b064-ba8ef7394175 | -16.67078 | -55.53433 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0322a75-92e1-35f2-9d3d-ab911db17c27 | -16.67008 | -55.53811 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a45c0a4f-7fc5-30ad-b376-c246fc6eadec | -16.6688 | -55.52222 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 65d67a8b-5f0f-3d81-863d-73eaea6e6a04 | -16.66747 | -55.50665 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cc6d1191-605f-3e5d-bad7-f165288de967 | -16.66742 | -55.52968 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d6e7f70a-76c2-387b-81e1-878bb59511ea | -16.66679 | -55.51031 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f2bf027f-cd5b-3f3b-9e45-d659afa491af | -16.66673 | -55.53339 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9088aadd-69f1-3a49-9060-4d01c3d86222 | -16.6654 | -55.51783 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d865e3c0-8464-39a6-92b2-cdac4172e846 | -16.6647 | -55.52156 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 46111b2b-b107-3034-9b86-d0cd2bc149a7 | -16.66334 | -55.52888 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fd36f4ac-5b26-3949-ba12-0e9b36481d4d | -16.69197 | -55.88847 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6b0a8a05-b072-3a0d-b12a-375a7cb24450 | -16.68855 | -55.88371 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c57e3405-22bb-33a4-801c-4542f54cb65d | -16.68767 | -55.88453 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d2225659-12b7-3f3a-8a70-91f6fa387ecd | -16.68513 | -55.87895 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 44c562fb-d65e-367c-8639-c8bc4812340a | -16.68422 | -55.87975 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 13514831-2aee-30ed-932d-11e78837b50e | -16.68266 | -55.91212 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 94bc11dc-74f7-399e-8628-35d9da26f8c2 | -16.67849 | -55.91128 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1af191d3-0727-3574-b70a-d99ac1dcce91 | -16.67618 | -55.94777 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8ce592bf-f8c2-38f0-b6fd-7f0f89ad5f04 | -16.66943 | -55.91353 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8ce8897e-0c20-30a0-b9ea-964b65212659 | -16.66871 | -55.91749 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 36776cb7-5ff3-390b-9238-9e59586d1ff1 | -16.66526 | -55.91269 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e54c8fab-aa48-3af2-9591-5442197f9579 | -16.66454 | -55.91664 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d32fa66e-a8ed-33da-9597-7d85c2d2caa9 | -16.66109 | -55.91184 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 91106f90-baa6-3b55-be4e-5bad04fed3dc | -16.65619 | -55.91493 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 38d67c12-03fa-3c12-9a6c-996191e9d6cf | -16.65547 | -55.91889 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5cf7a5e8-0867-32a3-b31b-52f75c96dca5 | -16.63878 | -55.91552 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 037c6e69-411b-3b6b-bb73-fe17154b6853 | -16.6346 | -55.91467 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2de2cf86-27c5-39ab-aa15-137562f0d79c | -16.63043 | -55.91382 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dd714c52-6b49-318c-85ce-187b0c812577 | -16.6297 | -55.91779 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 20246080-34f6-3923-9e34-2c3b793a2a8f | -16.62626 | -55.91298 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54010f6f-686d-3200-b625-b534d1b9aafb | -16.62552 | -55.91694 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README126.md)
