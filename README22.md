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
| 34a1be5b-e8fd-334c-b40e-e6f101c83a40 | -5.11318 | -47.14774 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f5927e9-0ce7-34e9-9dd0-5f5a82651caf | -3.9776 | -46.42249 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f865ae69-2259-31e7-a4c7-5bf79ab9d521 | -4.25163 | -47.57895 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 41bf8865-ec41-3b42-a51c-64d124877c7b | -3.78641 | -46.14184 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a307239e-d6e4-3f98-b96d-88e527cfb97f | -3.55415 | -47.38123 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a487bb2c-d297-301e-8c30-152df94c4f0f | -3.28914 | -46.41971 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80d3878c-8ee0-365d-973f-895d8e9f437e | -3.54963 | -43.57637 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9759f884-1c04-399d-bddd-f5c673f2a1dc | -3.54542 | -43.56882 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53affb39-8168-385e-9d26-520f015dc68c | -2.10474 | -46.20669 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 803f5c1d-65f8-3928-86fe-6f79257a477e | -2.36261 | -46.86771 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12b75cb4-4b82-309d-87ce-f82fe151d0ae | -3.2919 | -46.41347 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 327d4f62-3a13-34a2-bc25-ae653e03a292 | -6.21223 | -41.66566 | 2024-11-09 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f622cc0a-b4c9-3f4b-933c-b520412e95c6 | -3.29 | -46.4145 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d67fb7-7cf2-36ee-a5b3-c8a858593573 | -4.42108 | -43.38594 | 2024-11-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cad561c1-ebcc-3808-b4b1-513cfa08305e | -5.73352 | -43.51305 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4f3d2cc-8312-3f43-b0cf-47609bf0fa34 | -3.25944 | -46.3238 | 2024-11-09 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2325704-2699-384d-a604-b9c1bd87a385 | -4.24593 | -47.57178 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 7b894135-4f98-3dad-849b-92e6f161d0c5 | -4.05447 | -46.94059 | 2024-11-09 03:40:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34201526-a11b-3b42-b798-276b34a7be1b | -5.71112 | -42.71225 | 2024-11-09 03:40:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba5d1016-c719-3aea-9e83-37dcf806c80f | -4.20001 | -45.86395 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f48802c-c677-33fe-9a82-ba08ab30ddf1 | -4.62766 | -46.54292 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60c32581-42f1-3e1b-84d9-30fd2e2826f7 | -4.43693 | -43.64536 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efb1710f-7d25-3114-8379-5fc03d747840 | -6.43427 | -36.89143 | 2024-11-09 03:40:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e17083db-832a-39a2-8f3a-caedd391e91d | -4.73945 | -44.1045 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46894a13-4a06-3867-b23c-caedb612dcf2 | -4.15458 | -44.40074 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c404dd7-fc61-3080-8af5-d1cbca024189 | -5.94013 | -35.62089 | 2024-11-09 03:40:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 838efeab-3c97-3a38-8879-8ece17a7cc08 | -4.25064 | -47.5847 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8bbe739e-3042-3185-b5e6-fd4331450823 | -4.9429 | -45.56709 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f88f940-4f10-3493-a3b3-3faa1014873b | -5.73312 | -41.99608 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a9b284c-4133-317a-8a34-8d254b5fe83a | -4.05352 | -46.94595 | 2024-11-09 03:40:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff624593-bdf1-39c5-9f36-1a8e89f8cdb4 | -5.97903 | -45.3711 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ccd2a7e-77e9-3a0f-9ff7-ee48f7d00e8b | -2.37018 | -46.86318 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d43a122a-84c0-3ffb-b294-abf81c2bdb9a | -2.82171 | -40.28428 | 2024-11-09 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90afcbab-3a61-3415-bcea-3bb4ca26a54d | -4.44162 | -43.64944 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 971b24b1-ad52-32ea-8f50-174d48c86c19 | -10.51046 | -42.39467 | 2024-11-09 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6dbfcc6c-9866-3bc5-a93d-61b8748e4425 | -12.30355 | -43.17075 | 2024-11-09 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57d48769-93c5-38f4-aa16-62675125237e | -10.66127 | -44.50235 | 2024-11-09 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7601408-9f1b-39c1-9488-e000a1350582 | -9.41297 | -41.19195 | 2024-11-09 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fae4d3f7-8365-35eb-939d-1f909cacb0e1 | -11.06588 | -37.59144 | 2024-11-09 03:42:00 | NOAA-20 | BOQUIM | SERGIPE | Brasil | 2800670 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a035ceda-c489-38e3-a11d-cd106439ca3a | -10.02198 | -36.47363 | 2024-11-09 03:42:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b2d668b5-e40d-342b-b1e1-103cc072e841 | -8.85233 | -47.68371 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0339816-c6ef-38c4-a432-3bcec53558b8 | -8.85336 | -47.67842 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a6e6ff2-0c84-332f-a743-f700edc3be42 | -8.84705 | -47.67727 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2935d74b-bf89-3027-b350-366cf967cf3e | -10.33849 | -37.42414 | 2024-11-09 03:42:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 461c5bd6-e117-303e-9a8c-a3c853a056bc | -13.40203 | -43.01438 | 2024-11-09 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e316bc8-796f-360b-8f6c-dd10070552fd | -10.21419 | -36.24694 | 2024-11-09 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 7823eb1b-51f5-3b47-ac45-93896ca1f284 | -10.02142 | -36.47713 | 2024-11-09 03:42:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e06a16ab-7701-37f6-83ee-2f2b55220ec3 | -11.08002 | -43.3521 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b355f147-d837-33ae-9665-91cd9b04fe30 | -10.33908 | -37.42053 | 2024-11-09 03:42:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f8fd41a5-43aa-3607-8f07-191471ffccae | -11.05871 | -45.38714 | 2024-11-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd456302-e2de-308c-9cc9-328da5272d13 | -11.08634 | -43.34342 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 10876037-b0b5-30d8-a230-5f726909fb08 | -10.21089 | -36.24641 | 2024-11-09 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| d573be7f-8711-3021-a2eb-707650951958 | -11.08263 | -43.33781 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 06483154-ed65-3bff-af39-b470f052f549 | -8.84417 | -47.67796 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b718ea81-d06c-3eef-8dfd-ab5775573ab9 | -10.21474 | -36.24345 | 2024-11-09 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 2891d605-9ec2-3a73-ba3d-3a257ca695e9 | -8.84851 | -47.68968 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f51511ed-c6ed-3243-98bc-bdadb3b149fe | -9.79501 | -41.9664 | 2024-11-09 03:42:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 53b7fe62-81df-3507-8180-057df863e9ae | -12.01029 | -44.14079 | 2024-11-09 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1a5c89b3-4626-3b30-bc46-7dfc882874c2 | -10.66625 | -44.50333 | 2024-11-09 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cf72895-dd99-31a9-8ac0-a106216d946f | -8.84319 | -47.6832 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d43eb08-6bf8-3bf6-a470-f2d54622a867 | -10.21144 | -36.24292 | 2024-11-09 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| af1fd3cf-ad17-3a54-840d-d579c5524be6 | -10.87226 | -44.02741 | 2024-11-09 03:42:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2c078fc-064d-3f81-8eb1-1a9bd5a126a1 | -10.21034 | -36.2499 | 2024-11-09 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| ad7f32be-14c7-3e3f-9f60-ce7d37e17f43 | -11.08547 | -43.34818 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7468e571-b5ae-3be6-9078-1a1cc0ff25b6 | -10.5148 | -42.39547 | 2024-11-09 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fb180246-30c1-34b0-a25b-3e970b135790 | -11.08088 | -43.34736 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 310a660b-3eca-36d9-95da-56fffa175a94 | -10.01867 | -36.4731 | 2024-11-09 03:42:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 43801ee0-f1c2-30d0-bc35-29543c737a07 | -8.84949 | -47.68442 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4bb4c6c-51f3-34b4-9eec-23fb611588d0 | -8.85048 | -47.67911 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 367d639c-7bb0-3078-ad12-aecce3cab85c | -8.85131 | -47.689 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f7d156b-d49e-39a0-b192-47d03efbb2b6 | -8.84502 | -47.68774 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6f35b0d-5cf0-32d4-8742-6d2d41708104 | -11.08175 | -43.34259 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 42ee0beb-592b-3796-9fbe-b011a17e2a7f | -8.84221 | -47.68843 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19d9e318-724d-3184-a9d8-b39b198ac257 | -11.09637 | -43.34033 | 2024-11-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f674eb7-daec-3f03-8e41-11403ff7008f | -8.84604 | -47.68249 | 2024-11-09 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e951eafd-d00f-33f0-a056-e71e452fd33e | -14.80031 | -42.8683 | 2024-11-09 03:42:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 730473be-b2a7-3b5f-ad02-0cf774ee7433 | -15.98424 | -38.91653 | 2024-11-09 03:44:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ded3b84d-a3bb-3554-87c6-13ea4297f795 | -15.98362 | -38.92026 | 2024-11-09 03:44:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be113dfe-0e79-3de2-9e3f-8474a9c53c63 | -23.88477 | -54.05833 | 2024-11-09 03:46:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1f6a848b-677c-3f4b-a771-7dd5d53db093 | -23.88298 | -54.06518 | 2024-11-09 03:46:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c97bb798-b7bf-3a0c-97d7-d67041164ef2 | -23.89151 | -54.06047 | 2024-11-09 03:46:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5d77ea47-53c9-36e4-bda0-075ddfa8d424 | -23.87804 | -54.05616 | 2024-11-09 03:46:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7ddfb3c9-55fe-3bbe-b28c-e5bb39b6a2aa | -3.9853 | -48.1924 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b79a8c7a-e54f-3491-84a7-8289a18caf31 | -2.2295 | -53.7631 | 2024-11-09 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 893a0af9-70b6-3a62-95b1-297e085cd50b | -4.2484 | -47.5947 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| dd652740-7d6d-3b97-9b4c-146394aca1f8 | -11.0881 | -43.3219 | 2024-11-09 03:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 9e08df93-f8ff-344d-ad9b-5ed0f1e665d9 | -3.9854 | -48.1708 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4051792b-0e87-31d9-aed9-d0ae44a2fb7e | -2.4104 | -48.5265 | 2024-11-09 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5405316c-c370-339d-b469-f92d120270ff | -2.2318 | -46.5287 | 2024-11-09 03:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| aedb349b-688b-366b-a763-064350396d86 | -2.2295 | -53.7832 | 2024-11-09 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8d83e095-e27a-35db-8278-7bdd6cd326ef | -3.1511 | -52.9731 | 2024-11-09 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8762c5cc-e515-3951-95f3-be547325e180 | -4.2033 | -45.8538 | 2024-11-09 03:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d61f65ee-016d-3b48-a20f-6ae090fc4aa7 | -4.2486 | -47.5729 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 69a55b04-e62d-3b88-9424-54e14233900a | -1.5163 | -52.1901 | 2024-11-09 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 752a4a91-26a6-37dc-b058-6ee102d71668 | -1.5164 | -52.1696 | 2024-11-09 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 720d331e-4c9b-3592-9869-90f4e3ec1a8e | -4.2058 | -48.5491 | 2024-11-09 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5cfabd34-d5a6-3c7f-89dc-c8d8bc309fd6 | -3.0865 | -50.5625 | 2024-11-09 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 15a8188f-b7fb-302d-8a6b-477bf304cb8a | -3.735 | -54.2292 | 2024-11-09 03:50:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5593eab6-2b11-3511-be3f-486ce0692e49 | -3.5818 | -47.3621 | 2024-11-09 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e562b854-26c8-3b25-9516-645a049b0acd | -3.9669 | -48.1716 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 240.6 |


[Clique aqui para ver as próximas entradas](README23.md)
