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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8e27fd7-5427-36fe-88dc-7bea6f146212 | -12.94773 | -45.17625 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 01f2f990-e446-3cee-99cd-a699c83e33bf | -12.94002 | -45.16452 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e7f4f4e8-a35e-3b11-8506-6022ff5d4794 | -14.53805 | -48.43041 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| b6529f95-2efb-3b15-bce7-c8edfc38277f | -14.5722 | -48.23161 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f6397442-d0da-33e1-b8f0-56b9ebdf0e83 | -11.35491 | -45.06519 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03186130-30ed-3d98-8940-730d93f257bc | -15.42503 | -48.24176 | 2025-09-29 05:40:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 1dfabf7f-42cb-37a8-b4a8-abf876f6764e | -11.44688 | -44.97384 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fc19ae07-3e49-36f8-9dd5-db7298d9d27c | -17.08434 | -48.56194 | 2025-09-29 05:40:00 | AQUA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 8658b52d-14f3-3210-8a2a-0f28ecfba4d4 | -11.25724 | -47.18586 | 2025-09-29 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 24bd5e5c-58bb-393e-be52-e85d0add2192 | -11.36439 | -45.06665 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 844126e4-a300-30f2-b774-23b2b18f05af | -12.65293 | -46.92612 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 14c26984-5fad-3206-81b4-4228a211ae17 | -14.5466 | -48.44878 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 33f43170-6e5b-3012-8632-adb3fbbf1ec1 | -11.5094 | -44.85431 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 622ed4e0-33eb-370b-9a62-e26485dfb11b | -13.8313 | -47.49138 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ab287fdb-09b0-3fc3-8716-4bfefb93eac2 | -15.28453 | -49.52371 | 2025-09-29 05:40:00 | AQUA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2ca9f411-4433-3721-9788-00af43a24115 | -13.57293 | -47.28287 | 2025-09-29 05:40:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 90411c5c-850e-3894-8ef4-bf804832719c | -20.88116 | -45.53836 | 2025-09-29 05:40:00 | AQUA_M-M | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9e6acebe-643a-3623-84b6-884986f2a560 | -10.82904 | -45.38983 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fb266426-8070-3ff4-b6c1-c49b212ed734 | -11.93801 | -48.0186 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b3889354-1eed-39ab-b182-6cfb022426f8 | -13.63271 | -48.04037 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6f036210-f364-3f39-8a80-34d3dab5cb9b | -13.79589 | -47.89675 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7eaee5f3-8047-3856-bb95-3d5de3ca2cb6 | -13.57791 | -47.2896 | 2025-09-29 05:40:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0ec498a8-7a37-3575-b94e-5a8104489fab | -11.50152 | -43.5469 | 2025-09-29 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5ff78cd-c6bc-3eae-9725-64c368f1b83f | -15.33437 | -47.90877 | 2025-09-29 05:40:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 13cf1b0c-5c10-3d1e-99b9-6c1e3623b815 | -14.67794 | -48.1493 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 110722e2-b0be-3772-bb30-7504aab9cf04 | -13.5965 | -48.04969 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cab9507b-17a5-33e5-8730-c9eae193634e | -15.25674 | -48.75951 | 2025-09-29 05:40:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 46016825-6f9a-3024-b1d0-4e8108618c79 | -13.20254 | -46.76835 | 2025-09-29 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f363b491-46d6-355e-a90c-89ef3a69cec9 | -10.80273 | -46.6657 | 2025-09-29 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 79d013c9-0891-3482-be6d-2d5f7cd09f62 | -11.82615 | -51.8014 | 2025-09-29 05:40:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| e7b4adab-e0c7-3a6f-9e21-b7d7f7654f11 | -15.20662 | -50.11077 | 2025-09-29 05:40:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7878f289-0145-3fd5-87e0-34928978e3e1 | -15.54765 | -47.87366 | 2025-09-29 05:40:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 1f9dab0d-e1b9-356d-a0cc-4d984cf3cf2e | -13.20046 | -46.78074 | 2025-09-29 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 861bb0bb-4d8b-3cad-b7de-41d676ac92ea | -11.76275 | -47.55233 | 2025-09-29 05:40:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bf76369f-5b93-3831-8033-d042de07859b | -12.93839 | -45.17472 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b30f446d-0b58-3d58-9f3b-9570527a13de | -13.17663 | -47.44546 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 63a79405-f324-3876-ac87-48a0821633a4 | -13.18236 | -47.43758 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3edcf090-f220-3ee6-8a1c-845baf1d2973 | -12.57808 | -41.28129 | 2025-09-29 05:40:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 8f2b32b4-42c2-35d5-88c2-730ffbc83437 | -20.04511 | -41.3377 | 2025-09-29 05:40:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 09795532-b876-372f-acc5-980853c4191d | -15.20815 | -50.09697 | 2025-09-29 05:40:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| bb723ea9-c50f-3b49-966b-3abc5709621d | -11.92371 | -48.03276 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 85b71567-f5d4-3eaf-b318-8feccaf43032 | -11.26822 | -47.18766 | 2025-09-29 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 27fc53d8-deaf-3ca8-8c4d-7edbeb27b0a2 | -10.82649 | -45.39378 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6c7a03f4-3981-3ebb-ad5e-339a0ecbf92b | -20.04655 | -41.32669 | 2025-09-29 05:40:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 93ce7470-628f-30f1-8cd0-bc5aebd5d87b | -13.74975 | -47.89735 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3a8be428-f555-3520-8408-27e7c3757b2b | -13.74888 | -47.90514 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53e12c26-c888-3674-94d2-ed76d46f0dd6 | -14.53527 | -48.44656 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2939ea6b-b83a-351e-84ee-c8eaaeb9a981 | -11.92992 | -48.06671 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d3d5547b-11ff-3cb1-ad16-a159e50a1e95 | -15.90268 | -46.23957 | 2025-09-29 05:40:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 458a9c3b-22d0-33d4-8850-763cf8bfc76a | -14.59274 | -45.00666 | 2025-09-29 05:40:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 742a04f3-3dd0-3983-b594-caf71f5c79b8 | -15.19039 | -48.46502 | 2025-09-29 05:40:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f7cce916-7432-3e79-9ab8-d784773dc7fb | -10.81034 | -46.66015 | 2025-09-29 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0070bc60-fa34-3d30-a127-30383a4d9701 | -14.59119 | -45.01637 | 2025-09-29 05:40:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 44485a06-c754-39d5-b706-9be7e7c1fd7e | -12.93643 | -46.76714 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c0591b5b-0afa-330c-9cc6-4065b5a05f65 | -17.73009 | -46.68466 | 2025-09-29 05:40:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a20aa78e-c304-36dd-a1e3-c23986219c6b | -12.00624 | -46.62082 | 2025-09-29 05:40:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ef81e85a-4f41-38df-99c1-dc261a936fc5 | -10.80818 | -46.67357 | 2025-09-29 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 15bbd7c4-53c1-3638-841c-2a673d03e039 | -13.56731 | -47.28777 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| fe3837c7-cf6a-3059-b576-e118c6d52be6 | -10.79754 | -46.67179 | 2025-09-29 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fcdf0ece-c4a1-3559-90c8-496b5b8e20fa | -20.05639 | -41.32833 | 2025-09-29 05:40:00 | AQUA_M-M | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 13f0bdc0-bf4b-3722-82c1-1d83e007182d | -18.20072 | -53.29519 | 2025-09-29 05:40:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 41906934-1e67-305e-8a88-1efe19b577a0 | -11.41904 | -44.90571 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0c6a7226-294b-387b-a6e3-a1035ad3f9e7 | -15.28802 | -49.50389 | 2025-09-29 05:40:00 | AQUA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7335a63c-fa25-3b80-9b1f-45f78f31a789 | -12.86439 | -46.96152 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d616ec09-0f90-3ac8-941a-452f62072516 | -12.95869 | -45.16761 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d8bcf9e7-c192-3420-89b3-8b78cdd7f88d | -12.69921 | -46.90682 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7aeb0f71-7071-36c4-8c69-97ec2df5d41d | -15.53691 | -47.87209 | 2025-09-29 05:40:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9d04f2b3-44c6-3c75-b6f1-94fe98e66ab2 | -11.36276 | -45.07679 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 68fc0eaa-f6ab-3362-8163-097f2f60e0d8 | -15.60468 | -46.24786 | 2025-09-29 05:40:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6162b93f-84d9-308b-a123-50efb767132f | -15.90796 | -46.20733 | 2025-09-29 05:40:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e45918e2-1baa-3060-98ec-a45fe3c2eddd | -13.38366 | -48.14546 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| dc0b586a-8d8e-3c20-812e-8c3da42a0003 | -16.49044 | -46.04105 | 2025-09-29 05:40:00 | AQUA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02a81c16-3adb-3b6f-bf9c-011e20520335 | -13.57057 | -47.29736 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 13bdbc32-2cc6-3959-9039-db0de38fb0cd | -14.54936 | -48.43269 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4cd16e19-0a00-3918-8bb8-ccdbe7f497e3 | -12.58579 | -41.29216 | 2025-09-29 05:40:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 90b2a079-7f6a-3add-adda-d35fd2cc3168 | -15.21027 | -50.0901 | 2025-09-29 05:40:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d270bc35-ed63-34d0-b17b-ff8b73b09782 | -11.43129 | -44.95023 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 120fdf44-fca0-30dc-ba32-a8568fe37c97 | -11.511 | -44.84419 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 16cca6df-c016-3c37-b076-d34d53ee5fae | -11.93609 | -46.53009 | 2025-09-29 05:40:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0489a699-509d-3032-8c53-5c6a51bc2607 | -12.89236 | -47.09414 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 32260b71-6e94-3ff7-b27f-e8df01d046d0 | -15.27571 | -49.50249 | 2025-09-29 05:40:00 | AQUA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9a015d74-a6a0-3a4a-b852-95b2f1b42ab2 | -11.76112 | -47.55888 | 2025-09-29 05:40:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6c87fb5a-978e-388f-a376-91c62ffea461 | -14.52666 | -48.42859 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2e405cb1-649d-3526-81ec-9dfd4cd4efe4 | -11.45067 | -44.9808 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b4bbfd36-207e-3b9e-81a9-273ddab0c750 | -11.92645 | -48.01661 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3888cc19-6be0-37f8-96a6-c71763419b31 | -23.22937 | -49.40554 | 2025-09-29 05:42:00 | AQUA_M-M | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| db734b30-a1ce-3ebf-8af3-5bfdcfd41ad5 | -23.41628 | -49.45822 | 2025-09-29 05:42:00 | AQUA_M-M | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 064a8c58-4cb0-387a-b897-7d604f61e533 | -23.21901 | -49.40371 | 2025-09-29 05:42:00 | AQUA_M-M | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| e9928035-f9ac-33dc-9bb3-75f2019553c3 | -23.22141 | -49.39032 | 2025-09-29 05:42:00 | AQUA_M-M | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ab0f2c02-28ee-34b6-86dd-9a8b6a91e1f1 | -10.99367 | -57.05995 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a39836a1-0570-3016-aad4-86443ef94813 | -9.42486 | -67.55782 | 2025-09-29 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45dd6c91-dc3e-354f-beb0-9a2177a683f6 | -9.421 | -67.56078 | 2025-09-29 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77fcbddf-12c8-3cc1-a0ea-6ee62366fe89 | -10.99759 | -57.06163 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d67eacef-18a5-327e-8b71-ccc9099578af | -10.99708 | -57.06585 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dbf5d48-5974-395c-ab84-9c19832af646 | -10.22101 | -67.05033 | 2025-09-29 05:48:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 212f8de0-6e11-396c-8978-d9acd59236be | -8.94664 | -65.9219 | 2025-09-29 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22272de-55eb-384e-a345-1200a3fed859 | -10.99168 | -57.06074 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15f9ed3e-4597-3fe4-95a8-2a27b7e73b95 | -10.99313 | -57.06419 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 440aa9b6-b726-3f0b-8f8b-aef2f82116eb | -10.5483 | -68.07871 | 2025-09-29 05:48:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d7fbd34-ff46-3dce-9a2e-10124fe42a2e | -9.99514 | -67.56016 | 2025-09-29 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README81.md)
