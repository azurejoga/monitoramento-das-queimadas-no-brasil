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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc26f45d-6266-341b-82be-84b923c31958 | -4.26066 | -43.22544 | 2024-11-13 12:25:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 513882f1-33c2-3081-a631-b432d095e40c | -5.0094 | -44.0986 | 2024-11-13 12:25:00 | TERRA_M-T | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b63f1fce-94d5-385d-898c-e8c4730981f7 | -5.60565 | -44.88587 | 2024-11-13 12:25:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e0c577c-40b9-3f4c-8ea0-2bfb3fa60f97 | -8.13351 | -43.80823 | 2024-11-13 12:25:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3ee1348e-665f-3bd9-bbca-64c6b63b366d | -3.07446 | -42.43632 | 2024-11-13 12:25:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| af8b414c-9c99-3527-a385-6445961d3346 | -3.27958 | -43.11942 | 2024-11-13 12:25:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a1f72505-588d-330e-8bf0-2b0865d9c047 | -3.68639 | -42.42185 | 2024-11-13 12:25:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 198.9 |
| 2b3d6764-ac89-3397-aa6a-93ded19a1625 | -3.57447 | -42.10695 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b010fc00-d95b-3e11-a374-b5ab27460c16 | -3.56564 | -42.10572 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| f8805a60-e10d-3143-8b27-3583e348326b | -4.19734 | -42.32741 | 2024-11-13 12:25:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 19646edf-173e-34c3-8e97-f2343fc8f231 | -2.31336 | -45.06489 | 2024-11-13 12:25:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 73675242-ad3d-3251-b777-25075741c431 | -4.56234 | -44.25671 | 2024-11-13 12:25:00 | TERRA_M-T | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3e5c210d-2c82-3ef6-88c4-978f9acd18f3 | -5.549 | -44.32025 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9fa0809e-8879-354b-a6a5-9f49ed4f8f48 | -7.62952 | -37.70264 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 39248539-b8c8-363c-b0d4-aa33ba01ec31 | -4.81535 | -44.78355 | 2024-11-13 12:25:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 536453ab-44b5-3760-bc2e-b4555cfe0bd9 | -3.00792 | -44.09859 | 2024-11-13 12:25:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5c5cb8ac-52d3-3a56-afcc-7ac4c2132f34 | -4.74186 | -44.09931 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3bf9f067-3667-30df-804b-78a774ebc5a5 | -7.40495 | -37.56142 | 2024-11-13 12:25:00 | TERRA_M-T | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 65faa901-eb1d-3f77-a944-8f2bdc394cd5 | -5.2086 | -44.06275 | 2024-11-13 12:25:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e9c5dcbb-c448-3e92-8f44-03871ba95dc6 | -7.97103 | -37.80277 | 2024-11-13 12:25:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 1839c2d3-526d-3db7-9a9a-8e81f4a753cf | -7.81361 | -37.75914 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 840ebd9d-3eab-3a9f-a052-81db6ab6c5ab | -7.6389 | -37.69215 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 7911b83f-8f9d-320a-ad1f-d85ecbaca5a0 | -6.46447 | -36.24448 | 2024-11-13 12:25:00 | TERRA_M-T | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 32.9 |
| b24b94f3-3c0b-35ca-9945-8ead19536a50 | -4.34805 | -43.82947 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| bd7c113e-96fa-330f-b75e-26181c31754c | -6.33834 | -43.91191 | 2024-11-13 12:25:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be4be7d9-987a-33ee-9436-f4e68ead58c8 | -3.06561 | -42.43509 | 2024-11-13 12:25:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| bd16210f-06c8-3225-b5ba-0f29ca24caef | -7.81154 | -37.7753 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 646b8be8-8387-33f2-805c-2eb0f0790833 | -3.56691 | -42.09694 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 7cab2913-9eda-3ee4-a609-350ea978952f | -17.96502 | -40.20598 | 2024-11-13 12:27:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 57e51cac-a62e-3f6e-97e7-0393c9f111bb | -17.78684 | -43.18407 | 2024-11-13 12:27:00 | TERRA_M-T | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2ff9667c-7e09-3838-b594-044344ff5269 | -17.9632 | -40.22166 | 2024-11-13 12:27:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| e77c8f5e-63b2-3a33-9ba8-56f935cfa56f | -17.64765 | -44.46518 | 2024-11-13 12:27:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e99e421-61c2-39f8-8aba-011fe8aa7a21 | -18.23329 | -44.36474 | 2024-11-13 12:29:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9e208085-9734-319b-b6f0-b4ce0049b733 | -18.93666 | -41.93647 | 2024-11-13 12:29:00 | TERRA_M-T | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 393fb302-82b6-3919-9d21-f7dade8c3b84 | -18.25803 | -44.25183 | 2024-11-13 12:29:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 45c01a77-affd-32b5-a645-cbcb423079fe | -18.25934 | -44.24227 | 2024-11-13 12:29:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d14abf3-476e-30a9-8265-77ba8f47faea | -18.93513 | -41.94886 | 2024-11-13 12:29:00 | TERRA_M-T | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 7ba02667-4511-33ff-a964-0ad6637751b5 | -3.2909 | -42.48 | 2024-11-13 13:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 9cdc37d3-f309-3980-b9aa-ca25f885fbe3 | -7.2552 | -48.7295 | 2024-11-13 13:30:00 | GOES-16 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 98.7 |
| c52205f3-3d64-3a0f-97f6-98a046c06841 | -7.2552 | -48.7295 | 2024-11-13 13:40:00 | GOES-16 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e6a66f82-db64-391d-a225-f80e9ebf7cfb | -1.3873 | -52.3964 | 2024-11-13 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |


