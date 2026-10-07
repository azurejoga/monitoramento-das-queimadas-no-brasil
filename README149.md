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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3575ad3f-ecaf-349f-acf3-a1285bc872c1 | -10.77772 | -46.54232 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| db705623-ec67-39ac-a1bc-bcdc338ab79f | -10.52044 | -47.2785 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3be4dc4c-b590-3783-af1d-96b62ff1f701 | -9.86163 | -46.06234 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| bfa8e5e0-b33d-3047-8534-7cd9a50db414 | -7.26077 | -35.0409 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 27f08c4f-a492-37c7-800e-ba1252e9d966 | -10.4905 | -47.26936 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 34ccac82-2271-3f06-88fa-91fe2e11ff72 | -11.37962 | -46.68827 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b933e666-471a-35e3-b186-8cc3c8f3912f | -10.34412 | -46.23666 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ed707496-9357-36f8-9ea5-0d4aa49627a7 | -10.99263 | -45.41589 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| db3a00e3-4f78-336a-a0ee-cb5333717576 | -8.78099 | -47.58186 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fd652236-b0d9-3918-a84f-b026fad19e6d | -11.83704 | -43.56102 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d158e902-dd20-367a-8985-af23e83c008b | -11.06684 | -45.86047 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d5d9a525-e308-3a53-9e84-d5588b12908b | -8.31727 | -44.14831 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| dbbc463e-30cc-3e50-a0b5-6f6e0443443d | -11.83286 | -43.52969 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 738a6d4b-74a6-3dc0-8025-b7d8fb07d135 | -13.783 | -47.2675 | 2026-10-07 16:01:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c1fe7b12-3148-3d91-b274-df3673661a7a | -11.40345 | -41.82829 | 2026-10-07 16:01:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 33e9adcd-b72c-39ef-93fd-1d2e5679f3dd | -11.10986 | -45.69825 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| fa9a6080-e517-3861-b686-6191d570d254 | -11.09252 | -47.61463 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8b13e1dd-03c8-353e-8659-cbf2b5812c01 | -7.61972 | -40.48256 | 2026-10-07 16:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 91276d06-6c4d-3306-a123-ec412543d203 | -10.41577 | -47.54246 | 2026-10-07 16:01:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7329854a-f764-336d-aa9e-13badf806459 | -11.23093 | -47.34234 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 658d31d9-0342-3163-91e1-f8d003fa3ebe | -9.98457 | -43.56861 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a05227be-bedb-3cea-aa9a-94a5c3399805 | -12.40202 | -38.06913 | 2026-10-07 16:01:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 699563d1-6749-33c5-99aa-ddfcffc0bc13 | -8.67236 | -36.30518 | 2026-10-07 16:01:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 9696997a-6cb3-3856-9d48-64f49d11b9ff | -12.22545 | -44.73037 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ad2e3e5e-f8ed-365e-80f0-2c2289326b74 | -10.349 | -46.23287 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c1f8922a-5e35-34de-8596-e5d717ed9aff | -10.99881 | -45.424 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cf3203e3-518a-3928-9920-4ca2e336a3f7 | -12.20699 | -44.665 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 825f299b-acbc-31cf-99db-6506d0141053 | -10.4798 | -47.25346 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 489496d6-03ac-3686-ba27-75679398af22 | -9.92096 | -46.79594 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 49b594db-2e44-3724-9498-28a759a20285 | -11.07647 | -45.6406 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ad5436eb-2127-3bd3-bfdb-3f39ca62eee7 | -8.74249 | -47.88134 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9d1f3086-10bb-3f08-9401-044093a62cc9 | -8.64953 | -44.86486 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f53d84e6-76fc-3295-b54a-ffad085ffd79 | -11.06381 | -43.17609 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 10953b2a-6fcd-3191-ae19-21d4fd971319 | -11.06441 | -45.80838 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 99b93fb5-d257-3f19-adb4-3679d6a09e8e | -11.08974 | -45.66316 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ee41b30b-5828-3893-8777-4cce7ccf579b | -10.9877 | -45.49726 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78b25f88-2cb9-315e-9468-790e0929769b | -10.18331 | -43.31633 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 01db4d4c-b812-33e8-b554-e13970affcb8 | -11.09329 | -47.6148 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 81d874d3-d735-3842-b37b-1449483fb838 | -12.03859 | -43.39008 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6d6574a4-3525-31f7-9c42-7e0eb143f929 | -12.22214 | -44.72399 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| a1dae081-c927-306f-9504-e4bd817a5240 | -12.19308 | -44.64861 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 94856532-b40e-311c-98f1-801161802f92 | -12.17498 | -44.76455 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 2208a2cc-e883-3fee-aafb-79a4adc424b3 | -9.91647 | -46.80399 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2ba392eb-bbdc-3771-a711-c960ba63f38b | -10.77811 | -46.54552 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 83f9588f-2799-357b-9fb6-23d67a886edb | -10.19005 | -46.69983 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 799e2cba-e01d-3d11-81bc-a030301ae1d8 | -8.31284 | -44.14912 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5c2b0580-841f-3eb4-9991-21072eaaf0c1 | -11.04956 | -45.81593 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6e86003b-d7bc-3018-9abc-1c641c012449 | -8.59153 | -45.68442 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 63f2366d-76ba-345c-87d4-61ef59bc0307 | -9.77697 | -45.91142 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 75e5b606-d1e5-36af-bc24-67c196a7067e | -11.73593 | -43.50834 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0eb1ea49-5aaf-3b6d-bcae-a96e6093829c | -11.29401 | -48.00818 | 2026-10-07 16:01:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deb18932-3ade-350d-93e8-715f187c1d9f | -9.32616 | -47.40542 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 749a1294-f800-319b-b16e-db6a47e51c5b | -9.87247 | -46.06447 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4216ee5-bae5-3bb5-96a7-e443b0d8b4d9 | -8.58498 | -44.86417 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b3b5b4f4-f9d0-3a5a-aac0-ac63ea4c99b1 | -12.57016 | -40.33322 | 2026-10-07 16:01:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7b3f85f3-010c-3edb-95eb-5e522f40c406 | -8.58833 | -44.8724 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c0ac65c0-ec0f-3ea5-9f4f-8b12ff82f358 | -13.11442 | -49.00002 | 2026-10-07 16:01:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 36613de9-0f88-352f-9e21-9cdfbd517f7b | -8.98844 | -45.93747 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e84edd0c-b377-3ded-a829-44db309f04e5 | -11.72386 | -43.65802 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1203f0b5-78a1-3a01-88fb-738fb0bf10d4 | -9.34546 | -45.43055 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 06574f64-d7ec-3162-ba88-207e09685b4a | -11.22119 | -46.23717 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fc1d3fde-5270-3a98-a1b6-4d5de682054e | -11.0994 | -47.62259 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 658c239b-2e19-3269-b912-b154c6fc628b | -12.18552 | -44.76891 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 510.8 |
| 27b073cb-da10-33da-ad14-c3a2c83704ba | -9.9691 | -43.55327 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c380b543-f7a1-33b0-ab04-c8011d478e7b | -11.72325 | -43.65343 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 617c305a-74c8-384c-b04e-7d05e31500f0 | -11.05964 | -45.85311 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb228f25-8574-3cf5-b17e-f07081298343 | -10.99161 | -45.48755 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f98ea972-c7da-38a4-8cc3-02b7fa271c8a | -7.1738 | -35.17743 | 2026-10-07 16:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e96f247b-1e12-37d8-b07d-c54575219311 | -11.06611 | -45.86227 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec208088-2c51-3094-9c1a-2974d8ab0253 | -10.49299 | -47.29018 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a8733cdc-3a0c-3cb4-8edb-2e03126ee9c1 | -10.4803 | -47.25738 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0d354bdc-2d29-38cf-ac2d-9051a3fe333e | -10.92805 | -41.38923 | 2026-10-07 16:01:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 25a165d4-ca65-329b-afe0-f15333970ed7 | -9.86179 | -45.74416 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 505e3c4d-21cc-3d93-af10-260f05276274 | -10.30448 | -36.41467 | 2026-10-07 16:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0c6207f0-8891-3663-b747-2a21e14a793b | -13.07265 | -43.60473 | 2026-10-07 16:01:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2a19c4ff-c5ad-32de-93a5-e16aeb04525e | -12.16866 | -44.75399 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 90b91e87-7dfe-3b47-96e7-a460b483a692 | -11.55291 | -41.95508 | 2026-10-07 16:01:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| bba040ab-fd88-32eb-9bbd-22c8bb8a6173 | -11.1058 | -47.62642 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| b2982ccd-d817-34c8-919e-51f661039989 | -9.98399 | -43.56435 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14bb38c8-b6cb-3267-963b-e9929d6623cc | -11.20319 | -49.42154 | 2026-10-07 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0242bc25-531c-3a85-8898-628ae04b497b | -12.57974 | -38.98079 | 2026-10-07 16:01:00 | NOAA-21 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 890f1d9b-9b7d-3a8c-ac63-a4f611400bc5 | -11.37371 | -43.25251 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8ca10442-7c7b-3005-839e-0bd126fa80ef | -11.09792 | -40.14073 | 2026-10-07 16:01:00 | NOAA-21 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ff5b70c-6a2e-3124-a487-5b9091ee2348 | -11.10094 | -47.63553 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 546e32cb-1bec-3b8f-a3f2-8a027194f930 | -10.60876 | -47.57034 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 54f3ca1e-d1cd-30e2-b14c-ab92aecb9e83 | -13.27257 | -44.00087 | 2026-10-07 16:01:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0539fc45-380e-3c09-a20c-39b06f2876f4 | -9.86597 | -46.0551 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 41b22e60-9e61-3eeb-a1e4-54028f2a4634 | -9.93089 | -46.95632 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0337e76e-f946-3236-af2e-5c6f3adb4b8e | -11.22662 | -45.25277 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 92a0cbb0-e317-374e-b501-0ea2627b4550 | -11.22524 | -46.24117 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 79e8bf34-a8de-3e55-9c52-835d19cec5a7 | -10.1305 | -46.84497 | 2026-10-07 16:01:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| be9fcf54-39c0-39bf-b2e2-1878f5182668 | -10.99667 | -45.48683 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 7b245c86-479e-3fb1-8c5c-1dc8b59eb91a | -10.49266 | -47.26398 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a83eff93-0b9d-3bed-85e6-2d203115b53a | -8.77673 | -39.83395 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f9a6b217-359f-3f77-abe9-8029ad8e5976 | -10.858 | -50.66096 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 117895c7-1699-3f6c-9343-6173cb30983e | -11.01164 | -45.44356 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12dd8fa0-ced5-31b2-a89e-341a58423d54 | -11.15383 | -47.2985 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7cbb2c42-8259-3fe2-8f7b-ea0ab2b3f809 | -11.146 | -46.11318 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e3b0da9a-1f5f-3f63-a972-db3416c86355 | -10.52711 | -47.28587 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8b63b09c-b91d-376b-bb0a-0a99cbf3ebaa | -11.15964 | -46.17944 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README150.md)
