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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11eae0ee-653e-3f19-a77a-45d5d65abf81 | -3.55019 | -43.59434 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f3206b9-0621-35bd-ab6a-a3f4ec408e54 | -2.14012 | -48.00065 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b7fdc8d-4efc-3782-9c47-3e40627c6aa4 | -3.02936 | -49.43803 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 189636ac-6985-333a-a811-19ba313978af | -3.54346 | -43.61163 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae476ed9-6d81-3d34-90ae-45d3abb8c2c5 | -0.52939 | -48.52151 | 2025-12-30 05:01:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9baace2e-fda4-3d99-840e-ec3d2dd539dc | -4.33969 | -44.11916 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7919e557-c4d9-383f-8648-37ff711932eb | -3.54781 | -43.61006 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e916a3c4-5e92-3496-a439-818653df4f5d | -5.39725 | -44.68093 | 2025-12-30 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f02bbabc-6a6f-3389-bbe6-87156c8b580e | -3.54268 | -43.60533 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b9c66b9-a7f8-3229-93db-d9d5554601dc | -3.55092 | -43.60038 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 362caba4-4bfd-32d0-846e-4a25ee815c75 | -2.22872 | -48.12014 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6565f5cb-e90c-3011-8fbe-b793feee340d | -1.80788 | -53.48009 | 2025-12-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56fbac34-891c-3f13-8ab9-85c5d096cd4d | -4.34476 | -44.12367 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52f35620-9a04-3b6d-8779-c114c677d347 | -6.92832 | -44.57734 | 2025-12-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6abd4264-bbd4-3a20-b69c-b8e4055c2be0 | -3.54842 | -43.60601 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e172d39-cc9a-3cf4-bf10-aebf082779f7 | -2.1409 | -48.0047 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 280c758e-60f8-324b-a084-ef402bff20b5 | -3.55592 | -43.59512 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91d5ffed-5f31-3fa9-83cb-4743af99673a | -2.13732 | -48.00037 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c218614-3516-35e2-84de-0985efdf3ed0 | -4.34109 | -44.12044 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 949686fa-8d6d-3c74-a86b-85cdf70d8edf | -1.00616 | -53.09331 | 2025-12-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f803f87-42ad-3805-9c5f-70666bdcbf7f | -3.54404 | -43.60759 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6755389-4d63-3903-8abe-9196774dcb15 | -3.92559 | -54.58888 | 2025-12-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55db8a95-c33d-35b2-9f83-7e41e919a828 | -2.14146 | -48.001 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61574159-a7d4-311b-860c-f0d658ae375f | -4.34056 | -44.12402 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c7d1547-0d4f-3c39-b195-b7c9d8b7e59c | -2.17646 | -48.02169 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b288685d-5722-3925-930a-8eb16524fef9 | -5.26103 | -44.72976 | 2025-12-30 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5888279-0fbb-3e68-bf7d-652595385e88 | -4.33917 | -44.1228 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b47c7c4f-f6a9-3c57-aa34-60bbaba9a1fb | -3.54207 | -43.60936 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d295873a-5aaa-3131-a1df-af1bf627dba8 | -4.60921 | -46.59935 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 556f9952-7814-3461-b64c-1dc76802311c | -5.39673 | -44.68453 | 2025-12-30 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 743bd537-fde1-310e-80e3-0aa201910626 | -1.8112 | -53.48061 | 2025-12-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af03cae-bc99-3a83-94f4-d43131032774 | -1.47745 | -54.20082 | 2025-12-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eab3069-5846-3c45-b7d8-c66a3bae587a | -3.17488 | -48.02957 | 2025-12-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc4b9b23-52c1-393c-8dc9-a368bf0fa23c | -2.3735 | -55.86497 | 2025-12-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db28faef-3483-3718-9a2e-10cdf48a68d8 | -3.02482 | -49.44213 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf2c819f-9fc2-39c9-a615-6218ebd9af7b | -3.5496 | -43.59819 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e526bcc0-2613-3014-9290-f44a016b5db6 | -5.30861 | -45.17822 | 2025-12-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0ef5555-d363-32cd-8488-9751c047c5e4 | -3.17068 | -48.0289 | 2025-12-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dead9b2-e323-3de8-b51e-3c98b7996d95 | -2.18117 | -48.01861 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e3a8896-2098-3a43-88c5-79f5b1387c52 | -6.9326 | -44.56995 | 2025-12-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166ade68-954d-30ea-9039-389fbf29249c | -1.78788 | -54.24974 | 2025-12-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4632963-2481-3ca0-82fd-34ef858bda25 | -3.18807 | -48.02768 | 2025-12-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0839ba1f-ffe4-376b-a4de-916dddef150f | -3.02793 | -49.44739 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a862b54c-cab1-3171-8b61-f621bc4fc111 | -1.16037 | -53.50921 | 2025-12-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e38fe94-c6b4-3d57-a97e-9212ab9d7e67 | -3.0217 | -49.43686 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be1efd5c-56d5-365d-9fd9-27238fdce893 | -4.60517 | -46.59379 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01a45e91-5feb-3c40-99a0-ec671eda4203 | -2.22679 | -48.1228 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3844064d-0425-348b-a507-a082a5f3cf64 | -5.58749 | -50.40668 | 2025-12-30 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50a766f6-bdea-314e-8caf-0e0a8237362f | -3.55148 | -43.5965 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76356b88-f351-347f-b3b2-88bd319faeab | -3.54462 | -43.60356 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf20013b-7684-30ad-8e77-1512b54d5d94 | -4.3458 | -44.11637 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1415a2cf-6d44-3311-a519-030244732267 | -2.13954 | -48.00434 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a8e969-bb8f-31e9-82fb-e87efb3d1c6d | -3.89983 | -42.55708 | 2025-12-30 05:01:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3ed541d-2a95-36ca-a000-86a888d603e4 | -5.0302 | -56.19338 | 2025-12-30 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44367ae2-c1c3-39fb-9d15-356f68197591 | -4.26472 | -48.83905 | 2025-12-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eee5d8e-f627-3ddb-91c8-1eb7ed9eca7a | -4.60994 | -46.59429 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c857dcd2-27b7-3d3d-83eb-875b2eff1fcb | -6.60602 | -47.61898 | 2025-12-30 05:01:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 918e7498-b0aa-33aa-87f1-e83f0f031999 | -4.09819 | -47.74049 | 2025-12-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d289ef9-f386-376d-8fde-cb34b6876df6 | -3.0241 | -49.4468 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497a8dc0-9acf-3fea-85b2-582baa43143e | -11.56896 | -52.09598 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b32b9b1a-e4d0-33e5-bc9e-7abcaca664c5 | -12.66241 | -46.75914 | 2025-12-30 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64745fab-1813-337b-b7a1-e537c5f243cb | -12.5109 | -43.68955 | 2025-12-30 05:03:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e582df9b-468d-3b23-8f93-eac980967d50 | -13.47882 | -44.02249 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 965f4766-0810-32ab-93e6-db5e811729a5 | -13.50816 | -46.70509 | 2025-12-30 05:03:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e23ec40-1ea9-347b-b41e-af6aadc5bf33 | -13.47365 | -44.01093 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93756996-608e-3db5-9b73-ce2a3cb34f20 | -6.21712 | -55.65316 | 2025-12-30 05:03:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff331bab-ecdd-3037-9e51-642c13d23e16 | -8.06489 | -54.78226 | 2025-12-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c29aa2ad-8645-30ab-b76d-e3871bc92d0c | -12.51143 | -43.68952 | 2025-12-30 05:03:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8b529f5-29cd-33fd-8379-f20d5399341d | -13.47307 | -44.01619 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ad42627-ec74-3947-a93b-bd9bbb189b2a | -13.47249 | -44.02146 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab16b641-fe65-395e-9ab6-b479cec0e8d0 | -7.577 | -49.39594 | 2025-12-30 05:03:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95fdc97e-47bc-3bcd-ac1d-e5f45dba1c71 | -12.65756 | -46.75507 | 2025-12-30 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e0c5b60-d704-301a-9ae9-2b43cc5ea290 | -12.51731 | -43.69032 | 2025-12-30 05:03:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9e71117-a0d9-34b2-ae1a-97ab6286bd3b | -13.50279 | -46.70445 | 2025-12-30 05:03:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28ba4530-39de-340f-8d61-b83ecf9901d3 | -13.4794 | -44.01724 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6bca605a-38ee-39f0-b5dc-df74248659ab | -13.50774 | -46.70848 | 2025-12-30 05:03:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 051797ac-05c6-3cb3-81ff-ab627290abaf | -13.47998 | -44.01192 | 2025-12-30 05:03:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70a8993d-7a79-3962-8c03-cf16dfe08919 | -15.13563 | -45.28181 | 2025-12-30 05:05:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cec90bac-99db-39c0-af4e-80f80e0b6e13 | -12.36773 | -64.01554 | 2025-12-30 05:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7e2bf9e-5803-3e21-8510-d555054548da | -15.37115 | -53.0398 | 2025-12-30 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f935a9b0-0737-33c0-aac9-75c0fb6d28e8 | -15.54418 | -42.94076 | 2025-12-30 05:05:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 891e8231-1c2a-3e8c-beb1-a840f4caf2bb | -12.36724 | -64.01688 | 2025-12-30 05:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09529a4f-b9fb-3444-808f-9e78a2df763c | -15.13612 | -45.2773 | 2025-12-30 05:05:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe3a1d2d-c134-3a84-8a33-d56260b242cc | -15.1169 | -52.94616 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f935d250-3015-367d-8189-7e0bfd6a349e | -16.59175 | -58.21301 | 2025-12-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 721bf5a3-98a6-351c-af07-d214fe601d4b | -17.16021 | -47.72024 | 2025-12-30 05:05:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c567b31-3157-3e29-88ea-c7e0ff2e8108 | -16.50605 | -58.14062 | 2025-12-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7e452795-52e9-362e-b891-d8a8751361f2 | -17.16547 | -47.72086 | 2025-12-30 05:05:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f4e63d2-3dea-3281-b894-146e87f7caa3 | -15.7297 | -55.6944 | 2025-12-30 05:05:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e4b486a-f677-3d75-8f67-e53df26b59b4 | -15.50671 | -59.39243 | 2025-12-30 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe8f77da-68f0-3f8b-ae0e-facc75bf4074 | -15.74866 | -52.29775 | 2025-12-30 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c6a37f-0d4f-3982-b438-9a4b1ffdb508 | -18.11244 | -51.15609 | 2025-12-30 05:05:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75e19604-3b0d-302b-b92c-98625251b0e3 | -15.12851 | -52.94341 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ba2a9de-1a17-34b2-9a20-84288ff517d4 | -15.72889 | -57.9984 | 2025-12-30 05:05:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3517f9a9-e472-3eaa-a46a-c97b181ab751 | -15.54357 | -42.94719 | 2025-12-30 05:05:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 535b405a-9a5e-39f3-82bd-ac2ad96e19ba | -15.12964 | -45.28102 | 2025-12-30 05:05:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f978da9-0faf-3e79-81bb-30ad8d70a381 | -15.7221 | -57.99721 | 2025-12-30 05:05:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2697c1b0-d178-3bb8-bfa1-fb782e56d444 | -15.12915 | -45.28553 | 2025-12-30 05:05:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d4e6c79-4c89-3be8-bd5f-b6225672a6e9 | -15.12422 | -52.94728 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 905ea624-b86d-339a-8b9c-c846ff61807c | -15.12788 | -52.94782 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README9.md)
