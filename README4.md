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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0714165-3dfd-3876-ae65-06cc6dc66c59 | -18.36353 | -41.78879 | 2025-08-16 00:26:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 8d39340b-2d8e-386d-b5a3-4179c806b58e | -14.93906 | -54.72694 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 8a949050-12d4-3972-b2ae-f8f9d4af07e4 | -12.81402 | -45.99239 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46800730-8c33-3a7a-9ca7-215a02545aa7 | -16.23718 | -51.11311 | 2025-08-16 00:26:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4b90946a-2302-33fb-ab5e-0c7447d19c6a | -14.60103 | -47.93307 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a5d71676-3f6d-3511-ab94-b59e02f2ce83 | -13.573 | -46.97449 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8e27ccea-3190-3f31-9ac3-7c30f8c15c41 | -14.59021 | -47.92396 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 64efc8ff-5b51-3b11-91ba-3350da8000b1 | -19.29913 | -46.20931 | 2025-08-16 00:26:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 37c67c16-e5cc-318e-8b3f-d332fe55179a | -14.73666 | -43.96639 | 2025-08-16 00:26:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 306b5660-bb51-3e50-84c0-1fc1e986ebcf | -13.42109 | -43.67171 | 2025-08-16 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 834c15c2-d1d8-3422-8745-9caac7cee6c2 | -13.57425 | -46.98381 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 038a637c-83d6-3cdc-bfce-3b669dcddca3 | -18.51708 | -50.75741 | 2025-08-16 00:26:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0f2472fb-25f2-3119-9819-d2df99654b65 | -20.05466 | -44.63981 | 2025-08-16 00:26:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ddd28e0f-c493-3816-bc0a-ca18bb6872cd | -18.36028 | -41.78397 | 2025-08-16 00:26:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| df3a4e11-7c7f-378f-b401-9f076ac9353d | -19.552 | -44.06395 | 2025-08-16 00:26:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8dcbfc1b-8624-304f-9ab5-662e74b67e77 | -14.61997 | -47.93061 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5c792934-973a-3353-b888-b20e0f0ba872 | -14.62285 | -47.91275 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3849cd69-6ff8-3a9d-86f7-51f8b5639a6a | -17.3345 | -46.56971 | 2025-08-16 00:26:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94759a48-5a11-3dd5-bb2e-6c4213b2e9b9 | -14.61857 | -47.91998 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 270ebd6a-c0ba-3653-9cb7-a2063a50c905 | -14.94529 | -54.73137 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 5309d3f8-23ce-3969-8b22-8d9b71231718 | -13.47179 | -43.757 | 2025-08-16 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c0f363e-202d-3a6d-a4ad-cb3b26e11c57 | -13.6552 | -44.20004 | 2025-08-16 00:26:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 11c0f3eb-737b-34a5-a994-4c6412e69ee3 | -13.64657 | -44.19738 | 2025-08-16 00:26:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3fb6ae73-9c12-3af2-9d62-9c8bdc19684e | -19.1572 | -44.59641 | 2025-08-16 00:26:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c099df2-8653-36e4-b7e3-9c4e772462a0 | -14.60243 | -47.94384 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 58b44aa8-e986-3146-91a5-b4862fbb4327 | -18.52591 | -50.76202 | 2025-08-16 00:26:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 1f853d11-346d-30e6-a691-54dce4ec7d8d | -14.96087 | -54.72731 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b7206b54-ea53-360f-bc33-7bd8ffdbd956 | -16.22711 | -51.13342 | 2025-08-16 00:26:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b3d2a5a3-83e4-30dd-b8d0-ad67d5832ca0 | -15.58079 | -49.67403 | 2025-08-16 00:26:00 | TERRA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a3638d54-fc7b-3c71-848d-42ab696c7f06 | -14.62421 | -47.92345 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b2f083ef-5ead-3fea-acaa-77b363da1b81 | -17.60631 | -46.68414 | 2025-08-16 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4545ba47-91e8-336b-84d2-b276a0b96f4e | -17.6181 | -46.70284 | 2025-08-16 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 04cd7cdf-8825-31df-87fc-01bc5fecbbc1 | -20.05337 | -44.6304 | 2025-08-16 00:26:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 53b9615a-ba4d-398d-998b-620215b98d1a | -19.86777 | -44.95053 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b1fe1c68-7f0b-3add-bca4-57679f73be74 | -14.59829 | -47.91208 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 67152534-f7a5-38b5-b5d4-49b194077e34 | -17.6076 | -46.69416 | 2025-08-16 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b4c57ac7-3acb-3de3-bcbe-28ffb7ec90aa | -19.78131 | -42.03407 | 2025-08-16 00:26:00 | TERRA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| eb2984fa-0ab4-320f-8ba9-8d40b6b2326f | -19.78293 | -42.04488 | 2025-08-16 00:26:00 | TERRA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| d09f3937-a554-3a05-8868-6a9e954dc1a7 | -15.57575 | -49.66677 | 2025-08-16 00:26:00 | TERRA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cad4b380-8eaf-3266-8da3-9dae082a657c | -13.62012 | -46.91355 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b452d39-3c91-3188-bd43-9248e5c83f80 | -16.23926 | -51.1317 | 2025-08-16 00:26:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9172e52d-c7b8-3ff2-9b75-642fa6d93826 | -14.95472 | -54.72344 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 0fd13b11-9649-35f6-9ab3-2f1d4dbae2dc | -19.30043 | -46.21935 | 2025-08-16 00:26:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b5c177e-e52a-3acc-9ead-17649c317ba1 | -13.64795 | -44.207 | 2025-08-16 00:26:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 40979969-e13a-3a9f-a329-16471562f9af | -17.6194 | -46.7129 | 2025-08-16 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 84b8b99d-2593-37ce-82f8-450ebb7f905b | -14.59157 | -47.93439 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 077fd25c-ab7c-3e54-ac69-9325bdb8d3c5 | -20.15446 | -48.92275 | 2025-08-16 00:26:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7fa6e0d1-6b8e-3ac9-9488-d3fefbc60e87 | -17.60502 | -46.67413 | 2025-08-16 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e67674e-607b-3f06-a49a-19e0d4d7226a | -8.16169 | -45.0305 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5f666741-64c1-33fb-ae58-36814cad85f6 | -11.20136 | -50.45813 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c8e0c44a-2815-3bde-9e88-e028db35b99b | -12.80393 | -45.98468 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2ee0b0f8-66c1-3c66-91b1-e7fb9442c546 | -6.56253 | -43.02547 | 2025-08-16 00:28:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ac81f591-990c-3b19-8300-3d56075f97d7 | -11.98952 | -44.53331 | 2025-08-16 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d3a74915-d481-3738-afd3-9847ca3dc3e1 | -8.93773 | -46.74259 | 2025-08-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3cfe0721-bc96-34ba-ac3c-cf00af292ab8 | -12.61235 | -46.94534 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a14d2d71-5914-3515-8a79-a957ccc35001 | -6.92728 | -43.00005 | 2025-08-16 00:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| a9ef2514-9dab-311d-bd8e-f1bcbb0ec57d | -11.92966 | -44.12199 | 2025-08-16 00:28:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 2586609d-fc85-30fb-a014-e409d63bacf5 | -12.59319 | -46.93853 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4cb2a435-8076-3f15-9b69-9c0b8005c00d | -9.18191 | -45.32661 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| bbfe754e-1fe8-3ebe-9e04-83e2df3e59d0 | -6.96081 | -42.85678 | 2025-08-16 00:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 63fdbf8e-9c29-3e1b-84c5-11a03eee1ad9 | -6.86141 | -42.80803 | 2025-08-16 00:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 2f5f10ec-1bc1-3f10-8f8f-f0fdb97ec09b | -10.1751 | -49.51394 | 2025-08-16 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0c44826c-013d-32e7-ac82-1510be7d135f | -12.6034 | -46.9466 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| d8ebd49d-b5b6-34b9-87b9-cbfad5c1846a | -7.70992 | -46.19073 | 2025-08-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c82f21fb-68c2-3470-89ce-b301670d0c7f | -11.2689 | -50.47657 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7c7d4d45-31fa-3cb5-8123-104d0f812d82 | -8.1802 | -45.02785 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 83f1c10e-7d2d-3e9c-ac12-702e38132a08 | -12.80518 | -45.99369 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 043b2c82-fa08-3ff2-9df1-3a2c1861bcc9 | -8.7445 | -44.04429 | 2025-08-16 00:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc0929b9-6cc0-375a-ad5a-8797ff358459 | -12.59445 | -46.94786 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 537f465d-df17-31b4-8c30-c6c56d5ff973 | -11.19971 | -50.44477 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 79dc083d-66f3-3ee8-8f4b-638f5cdd7d2a | -7.39192 | -44.91588 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 17201a7b-3cdc-3e48-be23-23533eac8fba | -11.41258 | -44.68394 | 2025-08-16 00:28:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e03edd5e-4b5f-3bf4-9c49-3b6286951fd8 | -8.19085 | -45.03625 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7bddc517-fd4c-3f26-8e9e-d0f36c408e8c | -7.59839 | -45.20662 | 2025-08-16 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a31c6dfe-d1d3-3460-a2b4-568a2e9f0fbf | -7.24318 | -44.78835 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c0bd024-6f52-3199-b163-9b84c1da79b1 | -12.6141 | -45.22393 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81e2c87c-09e2-3384-b697-5b4dc9c588c5 | -12.55869 | -46.95881 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 5c81910f-985d-38de-a3f5-ff80f6b3130a | -8.34394 | -44.95059 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a07998b9-cf89-3c22-9ba8-16313a9b780f | -10.50787 | -53.59268 | 2025-08-16 00:28:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 2af79b7a-d5e8-394b-b24c-ce7a41f81eb8 | -12.56124 | -46.9774 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5a802924-b0a2-3dfd-bc1e-9a460dd4d577 | -11.41395 | -44.69352 | 2025-08-16 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8a27c9e8-c40e-300f-8858-cd5039e79768 | -11.99865 | -44.53192 | 2025-08-16 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2ae8982f-6858-3e59-b902-a8ff115edb74 | -11.745 | -44.94773 | 2025-08-16 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51dbb764-25b9-3e2a-9236-7bcc0bc6dbe0 | -12.00004 | -44.54153 | 2025-08-16 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3f2e6abb-8953-3fbd-a176-58e99b1060c6 | -12.29922 | -50.01451 | 2025-08-16 00:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a94c69ff-dc11-311b-900a-f7ed8c214fbc | -11.34436 | -55.43989 | 2025-08-16 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 0396d7f4-e607-3df3-89e6-c335760d85f0 | -11.90156 | -43.44176 | 2025-08-16 00:28:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3e8faa54-75a9-3ed6-8138-5809c05b5905 | -12.59842 | -46.90976 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a2f85b33-de32-3b26-9959-90cd15c05775 | -11.3536 | -55.43196 | 2025-08-16 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 07bf13d6-f351-3e9e-ac6c-f4814dc5651d | -12.55998 | -46.96816 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fd322ca8-c02c-394e-a986-c46ecf6cdfd6 | -9.16245 | -45.31989 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cea2e28b-9cdd-3aa1-978c-74eca8681f99 | -8.18945 | -45.02649 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5ff61216-958c-3c60-a768-1a03c1ed24b7 | -12.59966 | -46.91892 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 5a9931ae-0774-3acd-b8b8-8c64d12c0b29 | -12.6136 | -46.95457 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ca2ecf31-9283-3b41-b065-45d9ae91f8d2 | -11.9112 | -43.44028 | 2025-08-16 00:28:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48e1d10b-50f8-3aaf-8ef4-c64f9f0eacd1 | -12.60858 | -46.91752 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 358cc4ee-b865-3dce-9317-a32391a68715 | -7.38398 | -44.92739 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 186d22f5-4127-3b49-81ec-24360068ca96 | -12.4113 | -47.78336 | 2025-08-16 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7e5d767b-4dd3-3b3a-a944-f904e6b10676 | -12.56761 | -46.95171 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0da48fb5-1693-3bb0-a3c2-d913a699c2a7 | -11.25992 | -50.49142 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |


[Clique aqui para ver as próximas entradas](README5.md)
