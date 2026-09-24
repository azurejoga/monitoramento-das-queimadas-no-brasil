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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 324707b1-324e-37ce-b37b-c585729a080b | -11.42394 | -47.40481 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7722926-f6c4-3f4e-bef7-b2e0fc075b81 | -10.88338 | -45.08175 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 690766f6-2fa7-3f45-974e-2693bb6bdabd | -13.06937 | -43.28146 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6bce129f-d2f2-3c00-a245-b421529dd179 | -14.70631 | -45.58064 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f034c974-47aa-38d6-b5c1-14ea9efe6db3 | -12.05249 | -50.29076 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd47e323-3c68-38ff-a37a-9795ec4352dc | -11.8961 | -45.77408 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4355232-f032-30c7-8a41-80a9639a7bfe | -10.08292 | -46.00819 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b588435d-e192-383e-bf1a-499055295786 | -11.42779 | -47.40564 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 048b6298-dbc5-3e4d-ac34-1a30ebb397b1 | -11.23613 | -51.39913 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23cec734-ba8e-38aa-b411-21fc2631c6c2 | -14.74836 | -45.60298 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 89e91752-5ad9-3e36-be06-e05bf577aaf9 | -14.5647 | -54.12395 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 136ea0f0-028f-3855-a883-fe205b8c4d12 | -10.46253 | -44.94668 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 171b5af9-8683-3682-aced-7b9a066c0c1b | -11.48933 | -47.33508 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d97dbf6-0b43-3341-a988-2e1fc99db8f9 | -11.69447 | -43.47906 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d181fc8-874a-36a2-80b4-2aa3f6aa0714 | -10.41649 | -49.34906 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd8b234f-c56f-3849-a0f4-eeb226606a40 | -10.26597 | -49.95758 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 086b7d04-3dfd-3824-9f89-d0728a351cd6 | -11.22827 | -51.38524 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 000d7806-048d-3d14-adbc-9fad0167deeb | -11.48418 | -47.33188 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4390d0c-941b-3eab-9e80-a87b67a22079 | -10.73876 | -46.28613 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7469b06c-6460-3c1d-bb26-895598ec3e50 | -10.08807 | -46.02214 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 349c5cf8-519f-3cdd-a624-72ea60adc1bc | -13.08128 | -47.40815 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23cfefd4-2376-3dfa-9f87-427de82d2795 | -14.75267 | -45.61935 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c15b0937-656f-3b9a-8894-c7153923ffb5 | -14.70568 | -45.58444 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d1a4e61-ebee-36e0-a788-94b18ed15ad2 | -10.08361 | -46.04843 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 771938f0-5730-3cb6-961c-120d2ad17a3c | -10.27532 | -49.95926 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b0923a3-1760-3281-92f8-143cb04c2d76 | -11.69834 | -43.47608 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aeb562b3-a4e8-3026-b023-da2c7c9784f6 | -11.22997 | -51.37624 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3a67dbe-2929-30d8-9c0c-3c97459af7a7 | -14.56878 | -54.13303 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 856b7d0a-5d54-3fbb-81f1-a4796a576f62 | -12.68095 | -46.37906 | 2026-09-24 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef491a39-6036-3bf1-8440-2fcb61a67b24 | -10.61446 | -53.99729 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3760dde6-77be-3d55-bac2-9c974cf2eaab | -14.56619 | -54.12724 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f8ec0e6-2daa-37c4-bc4c-3f187092b40a | -10.27152 | -49.95344 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c11817a-fef4-3893-9912-312548b45c9e | -10.7206 | -48.73959 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 339a9f1d-5855-31bd-87f3-ec715d9e0d48 | -15.16696 | -43.57116 | 2026-09-24 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 99799a6d-ad34-3abd-a8a9-b3f9d2440066 | -13.06882 | -43.28498 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 06f328d4-f27d-333d-9fee-cf51b09481d6 | -10.09969 | -46.06458 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63f3b0b9-a7a3-335f-94c6-08dfdc878c3c | -11.79726 | -50.99119 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18029cfb-4258-3db6-9cea-d2938da85c9a | -14.56873 | -54.11507 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f056a3b-b3d2-3a67-a6d5-6539de547f9a | -10.20955 | -44.14317 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 728be406-94f9-3a2e-a917-bbdd656cadd5 | -12.1338 | -50.74331 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 992e5514-76a3-323f-b75f-388f5f60d988 | -9.84466 | -48.50382 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd2bd38c-a825-3984-ab72-e15715bafd68 | -9.84109 | -48.49903 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fe6d619-b034-3ec5-8b72-e678bd5b2350 | -16.87128 | -43.20482 | 2026-09-24 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52ab6cda-2773-3d99-bfa0-dcc17de215a1 | -12.12075 | -47.38384 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72c95fda-542c-39b1-94df-86ec1649f390 | -15.33754 | -48.11348 | 2026-09-24 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 289f3af0-0225-3167-b582-ef6d5135dc41 | -12.11427 | -50.82182 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f5f73cc-95b4-3a04-bf72-c129b2c2f51c | -11.69946 | -43.46904 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92241b61-6ff8-34da-862a-48d3c208d2d5 | -12.92585 | -50.9216 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ceb4a8e-7cd7-357e-ab86-d0de0f81f874 | -9.86245 | -48.50266 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d84dbf6-2610-3291-bf96-1755aab48e26 | -12.0054 | -50.31258 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e80480d-4d33-3230-aac0-154e7dfed607 | -10.45292 | -51.29893 | 2026-09-24 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71525e5-14b7-3cff-b7ec-33cd4499c242 | -11.94042 | -38.29176 | 2026-09-24 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4c95e819-f8b1-3802-841d-39cd209d8d51 | -11.60522 | -46.80276 | 2026-09-24 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 888685fe-18bf-3bae-a507-021f9ecb786e | -12.15285 | -50.74691 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 712aafd9-d1df-3686-93bf-3ac4588a246c | -10.72418 | -48.74422 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 821b9e1a-0f65-3062-a480-e5c4f5b928ba | -10.08295 | -46.03019 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31d9855b-73fe-36d1-b797-d67ae0fa8afb | -11.48859 | -47.35287 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e28e681-3a82-39e0-9300-234feabdb565 | -10.07712 | -46.02031 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f38df57c-0b6d-35b0-afa9-0d5b370be88f | -14.56219 | -54.1181 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99bac3dd-d921-3bbd-9509-eaed1ea1d015 | -12.41611 | -46.94771 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7857752-f4c6-3cd9-bea7-fe231ca50d7a | -12.4183 | -46.95752 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ca25a4b-3b2d-3b0c-b4ef-b95cb838367e | -10.91005 | -53.94749 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7045e4bc-3b07-3e9f-b12b-d41ea440891b | -14.74217 | -45.598 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2799b93e-c7af-3be9-a85e-a567be854fd5 | -14.56131 | -54.12227 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60c54a8e-d20e-38e1-b689-325118d30492 | -10.10682 | -50.18885 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 381594c0-bb4e-3798-86b3-1ffaa6ff5fd0 | -11.9274 | -50.73758 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7bb5422-59f3-3c4f-b327-bd4068ba3ff0 | -11.69503 | -43.47554 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f09ebf30-b4c6-3568-86f3-34c6969ea1a2 | -11.10662 | -48.29662 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2435158a-74a1-3b72-a8ac-90dd2cb69e3e | -10.6239 | -53.98779 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ef05014-797b-3cc3-9b98-6e83da9529d9 | -12.01378 | -50.31927 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82cd1f60-918d-31b1-8ed5-7f7157ded973 | -13.82411 | -51.85495 | 2026-09-24 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c605159-48da-3d0d-b24a-8f637d5b6d4a | -10.07784 | -46.01603 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 93302435-b5eb-3705-b119-f1c454e5922d | -10.11434 | -46.02219 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb0beede-834f-3c97-915b-c3a1a60f565c | -10.08631 | -46.0101 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 27163112-4823-33ca-a4b2-332cc10fe6c4 | -10.4903 | -45.20301 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6d07565-51c4-3b76-8eba-662ee43ba917 | -10.07856 | -46.01179 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 558e0769-0147-332c-b688-9984f90aca38 | -9.59291 | -47.77501 | 2026-09-24 04:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b53605a-485e-3e39-96c6-a8b0a7edc1cf | -11.40733 | -47.36235 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 486f0594-7bb1-340e-9f22-d1b69a66701d | -11.79472 | -50.04193 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8415a7c3-e976-3469-b4db-b45658bb2fc9 | -11.23391 | -51.35529 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df6b9a68-25c2-3b1b-86b8-2c889d99232d | -11.23839 | -51.35923 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0b676cf-d391-376d-9513-a8a350d8ab16 | -14.74672 | -45.63407 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 394f4347-92ae-3d6f-a0e4-340271b58361 | -12.41085 | -46.95622 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 393c7ec3-02d7-3844-9677-4e5a1030305d | -10.45907 | -44.94612 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d33cc015-5d18-323e-a289-43d50ce9c021 | -10.91085 | -53.95507 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f833bc8-63ea-3b8a-bd84-c9f5972d0cea | -11.48803 | -47.33258 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df8609fe-a448-37e0-b413-f67bca898798 | -13.7338 | -48.97076 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ae99a5-bf17-3a9e-9b22-42b75d2fca47 | -14.75393 | -45.61177 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1362756-c888-38da-94b8-0e8bb13c58b5 | -13.29333 | -47.91148 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 120399d9-04ea-3229-9aa8-924e005bfa71 | -10.56295 | -46.70523 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed105437-03a6-33e2-b606-8d86e28f13fa | -13.52442 | -47.65639 | 2026-09-24 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a262841a-da3d-38cd-b985-7f4dbf1b5414 | -11.96303 | -50.75843 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb1387d3-e8c1-3003-8d7f-7a0f0b8b8ccd | -11.23446 | -51.38018 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e95ae9-c9c7-362b-96e9-35ad46ab998e | -11.98382 | -44.94749 | 2026-09-24 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf98a1bf-42be-3465-abad-66baf980ee2b | -10.90916 | -53.9521 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c62539e1-ef9a-37d8-b0d0-c1e678bbaa6f | -14.75141 | -45.62698 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 000eb205-1aef-3ee6-bc96-00da0daf1357 | -13.08047 | -47.41288 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fea1da7-7495-30e7-9def-4a3f711b9864 | -10.72132 | -49.01112 | 2026-09-24 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 299a05b3-a12f-3581-afc3-80859bfd2248 | -11.65498 | -43.49075 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 47c36cdb-7a64-3646-aac0-52fa23b88ff4 | -10.08588 | -46.01292 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README37.md)
