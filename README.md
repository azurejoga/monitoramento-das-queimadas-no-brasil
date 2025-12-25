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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a73a242c-ad44-33cb-8d88-f18301ecca76 | -12.9041 | -52.515 | 2025-12-25 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 70491af9-8246-3385-b781-9cd651cbea09 | -11.7589 | -43.3136 | 2025-12-25 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 0ba0dc7a-cb2b-35bc-a35d-6a8203d9072b | -11.7397 | -43.3166 | 2025-12-25 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7d707163-634c-36e6-8b6d-ca1f242b568d | -11.7585 | -43.3374 | 2025-12-25 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 39811747-75fa-30b9-9c7a-bb2cb2539d6d | -12.9041 | -52.515 | 2025-12-25 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0f472ef1-8213-3eab-bb15-8d3e908cabbe | -11.7585 | -43.3374 | 2025-12-25 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 2fe337c5-03ba-3f96-aa9a-eabfee2b86fe | -11.7397 | -43.3166 | 2025-12-25 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4be0f481-2e03-33c2-8e9f-77b85a373885 | -11.7589 | -43.3136 | 2025-12-25 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 9395d3cd-cd6f-3238-abb6-9ef02925ab40 | -11.7585 | -43.3374 | 2025-12-25 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f7ed2428-6a04-332e-8563-2a679d442aa0 | -11.7589 | -43.3136 | 2025-12-25 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5571d4a4-76a2-3dac-800d-ef75d7d27594 | -11.7397 | -43.3166 | 2025-12-25 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d3aa44cb-d190-3b6b-8c96-e4bcfc5d39ff | -12.9023 | -52.5289 | 2025-12-25 00:48:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71f29661-c415-3db1-837e-aed4b7604fee | -15.5122 | -51.862999 | 2025-12-25 00:48:00 | METOP-B | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e457e62-29a3-3928-b129-db82553a5a2f | -12.8999 | -52.5191 | 2025-12-25 00:48:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0d4e24e-fa56-3f36-8b6b-0f91f1670a7c | -25.513 | -49.468399 | 2025-12-25 00:48:00 | METOP-B | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ce05f83-7568-370f-95bf-60e708321b2a | -11.7589 | -43.3136 | 2025-12-25 01:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a3a2c10b-2750-3e83-9149-bf2aa02b587b | -11.7589 | -43.3136 | 2025-12-25 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b1cc929e-61e9-36be-b8b6-23b449365fde | -11.7397 | -43.3166 | 2025-12-25 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8b1b556c-7991-3516-9a37-ef4ccfd9d585 | -11.7585 | -43.3374 | 2025-12-25 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c1c861b1-e852-3c81-aff3-e95b8e41b551 | -11.7397 | -43.3166 | 2025-12-25 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 24b3b409-294e-3447-9037-3f2008dd7bec | -11.7589 | -43.3136 | 2025-12-25 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 323e1c6c-bda4-3b38-990a-d977fcad2138 | -11.7589 | -43.3136 | 2025-12-25 02:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 611b222e-5480-3c40-b998-f647171d1590 | -11.7589 | -43.3136 | 2025-12-25 02:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5c07c455-02ff-365e-840c-dd1df7031e07 | -11.7589 | -43.3136 | 2025-12-25 02:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 663eccce-8b79-361e-9994-489b210a50c3 | -7.46159 | -35.11641 | 2025-12-25 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9ce8ba9c-6053-309a-8fcd-36c67457c813 | -7.46453 | -35.12387 | 2025-12-25 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fe279eb8-4993-39cf-b32c-a03d3b8f5ee3 | -7.46024 | -35.12352 | 2025-12-25 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fed5dada-51c8-316a-9f3e-0b991f5c5e7e | -7.46591 | -35.11683 | 2025-12-25 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4241d5f3-fe41-3f37-8380-66b26516bbab | -11.7589 | -43.3136 | 2025-12-25 02:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 78855684-794f-3fcb-b80f-5f9abba1e7d4 | -11.7589 | -43.3136 | 2025-12-25 03:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 400b3da4-8859-36d5-9595-63ca15e4fd80 | -3.72447 | -38.54646 | 2025-12-25 03:14:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e294654f-1c10-33c4-bcf4-4a4c234f1900 | -3.72358 | -38.55156 | 2025-12-25 03:14:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 997ab55b-5061-35a3-aed0-bb492e49b4ff | -5.37216 | -35.45001 | 2025-12-25 03:17:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63640a87-e50a-39eb-bbe1-fe2440bb3837 | -10.55817 | -37.87931 | 2025-12-25 03:17:00 | NPP-375D | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b20ced6c-73a2-35e3-9dc3-7cee41bb97df | -10.55273 | -37.87834 | 2025-12-25 03:17:00 | NPP-375D | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a39d51e4-79da-3c2b-9f3e-f586e9db216f | -7.20969 | -35.2876 | 2025-12-25 03:17:00 | NPP-375D | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0c37b48e-fffa-395b-8a9b-302828150553 | -5.3671 | -35.44919 | 2025-12-25 03:17:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6aa99941-62ea-3c73-8d42-eaecb5079683 | -21.00606 | -40.8357 | 2025-12-25 03:19:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 431a95d9-6050-35d2-9c2f-1bde0e77a333 | -20.09766 | -40.22385 | 2025-12-25 03:19:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cff096a-974c-399e-b6da-b9ab4dfba0ce | -20.09242 | -40.22249 | 2025-12-25 03:19:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4ffb9e4-4627-304d-9292-c4467e1f4fdb | -21.0007 | -40.83436 | 2025-12-25 03:19:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 76a94bf4-c477-353f-b91e-20d89d62c508 | -5.26443 | -39.31825 | 2025-12-25 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 050446e6-ae19-31cc-82d2-8620001f98d5 | -5.90233 | -37.82589 | 2025-12-25 03:36:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9d2d3ef-59a5-3825-923d-26bb5ef35597 | -7.09028 | -37.4026 | 2025-12-25 03:36:00 | NOAA-20 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a135f7a1-5f33-326a-8377-95ab6f8ef5a9 | -5.70711 | -35.54586 | 2025-12-25 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eaf7cd92-b203-3ccd-8a7a-1ab4722a06c7 | -5.50694 | -40.56849 | 2025-12-25 03:36:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80711f36-9f1a-3d62-9132-2149d9ff69d2 | -5.36817 | -35.45112 | 2025-12-25 03:36:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eaf8132d-5e46-3e4b-a767-5a5f9038cfe7 | -6.68277 | -38.56901 | 2025-12-25 03:36:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f30ebad-88cf-35a4-8a8b-eaac15e05ded | -7.46649 | -35.11715 | 2025-12-25 03:36:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd2d4ff4-837f-3523-8a1f-b0c0c7dadd3e | -3.72347 | -38.54791 | 2025-12-25 03:36:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5bd0ece2-8080-33a8-9921-16d87d3bf9db | -7.21164 | -35.2853 | 2025-12-25 03:36:00 | NOAA-20 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7fea0102-eec2-3b42-99d8-d2d9ed3cf7dd | -5.36877 | -35.4474 | 2025-12-25 03:36:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8266aa96-87c2-3e41-83f8-22f4664f6057 | -5.67634 | -39.26638 | 2025-12-25 03:36:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61f570b5-83fb-342f-aebf-93401a73ea13 | -7.20827 | -35.28474 | 2025-12-25 03:36:00 | NOAA-20 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60a96f80-cbcb-3587-8f6c-d33d00886df5 | -5.67568 | -39.27031 | 2025-12-25 03:36:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85ced5d6-b675-3848-8493-52ab6ccedaab | -5.67503 | -39.27417 | 2025-12-25 03:36:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b06ec073-af41-3063-a9ff-37b36da0968f | -11.84379 | -43.7974 | 2025-12-25 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af053c03-18ee-33e9-b02a-98c6454d668a | -11.76211 | -43.32604 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81d2a817-e919-39ab-95b8-c082a1821477 | -12.5091 | -48.38224 | 2025-12-25 03:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be9e123c-57de-370b-95aa-266aa037a23b | -13.85468 | -43.97176 | 2025-12-25 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a791851c-a501-382b-91b0-7e65c46f4902 | -11.761 | -43.33186 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8271abb9-89c3-3e28-a03c-51e71d21bba2 | -8.88085 | -37.05002 | 2025-12-25 03:38:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14b7d4f5-c35c-3349-824b-6c015e338b1e | -11.75163 | -43.32661 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 290d672a-cecc-3d20-a9de-ecde952d468b | -11.75215 | -43.32407 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f08795ee-0d03-3071-965a-e3398a2fe327 | -13.37841 | -44.38447 | 2025-12-25 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e1c8d85-4ac3-3114-9b5a-63d111174c03 | -11.75661 | -43.32761 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b26caad3-664a-3b75-a33e-e8c3e0bc2d65 | -8.47086 | -38.56297 | 2025-12-25 03:38:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fdad601-4a91-3576-b078-7a83283cfa15 | -12.087 | -43.76867 | 2025-12-25 03:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf8a8944-1eb8-344e-aaec-ee4c97259f63 | -11.83983 | -43.79015 | 2025-12-25 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa9a6c40-aebe-3837-8f26-045a42971b13 | -11.74829 | -43.31729 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 28203505-ae71-3a4c-a6c4-b5bb937b989b | -11.75327 | -43.31826 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fb2938be-c94b-3867-b7b3-976647a8b109 | -11.75351 | -43.31643 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd8ab12a-07c9-3e27-87bb-795a9f654e39 | -12.51032 | -48.37646 | 2025-12-25 03:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5805e23b-051a-340e-a51e-950dccd3b955 | -11.75109 | -43.32954 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfc5761e-458a-3f79-9b86-a5cb4248961d | -11.75713 | -43.32505 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99e60065-3809-33ce-b9dd-f66ea5d5caf6 | -11.75602 | -43.33087 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5c02d63-6020-3c9f-83e3-a0d21470492d | -13.8541 | -43.97472 | 2025-12-25 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5b1dd87-af21-3a9d-bed6-334bb22e224f | -11.74746 | -43.32126 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33a582ef-8995-3ecb-ad9e-260ce2e9d7c9 | -11.75104 | -43.32988 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8d6db69d-48dc-3f14-82d3-9d05f99f62c2 | -13.37779 | -44.38773 | 2025-12-25 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da8faf21-a908-37ff-aab8-88dadda7ee81 | -11.74665 | -43.32562 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3c30bd8-0412-30df-8b7c-0add73de06d7 | -11.75608 | -43.33054 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bb6a078-0d9e-3d43-9454-38211e1934e5 | -11.75244 | -43.32225 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 70e9805b-5178-344f-b08c-27e2859353c6 | -11.84438 | -43.79427 | 2025-12-25 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c12f1183-e9c1-32bf-873a-61e8f4c5b11d | -10.5547 | -37.87722 | 2025-12-25 03:38:00 | NOAA-20 | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa9f80a9-2f70-3f40-bda4-4cbe3b76d883 | -11.74853 | -43.31545 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5192701b-bbd3-3205-a0d5-2d7d81c6301f | -9.43192 | -39.67013 | 2025-12-25 03:38:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dd57dc6c-6204-3567-8c18-55b3815c9379 | -11.74718 | -43.32309 | 2025-12-25 03:38:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e143d13-524e-3813-8ce6-612155eb522e | -11.83924 | -43.79328 | 2025-12-25 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aed81b56-c3c8-3a77-ad23-4726c1982f44 | -18.59303 | -46.55192 | 2025-12-25 03:40:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d7c7e08-26b1-3d42-809d-fd62b59c7854 | -22.38905 | -41.84105 | 2025-12-25 03:40:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c6ae307a-0c59-318a-9b8e-850ff348dfe6 | -20.37904 | -41.71007 | 2025-12-25 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a76ae68-4014-3b31-a3f6-3adefaab9823 | -21.00193 | -40.83406 | 2025-12-25 03:40:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7de9a4b0-3339-35b8-b6e5-aeee5ca82c38 | -17.78179 | -42.11748 | 2025-12-25 03:40:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 13b82a4c-6108-3fdf-80c8-fc385be605b9 | -20.0953 | -40.22388 | 2025-12-25 03:40:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9eabfe3b-6ad9-3954-aaa5-d1ea772958e7 | -18.59091 | -46.55553 | 2025-12-25 03:40:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d1f3b8-25a0-3408-9d39-cb08781273a3 | -17.01296 | -47.25851 | 2025-12-25 03:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 869a6a9d-e9ef-3fd7-8100-74034c8c48df | -21.00559 | -40.83482 | 2025-12-25 03:40:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 18e16a87-1c24-36f2-9d5b-07406b51e232 | -22.16351 | -43.30287 | 2025-12-25 03:40:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 278d6011-11df-392c-8830-c7ceee676673 | -21.00513 | -41.54518 | 2025-12-25 03:40:00 | NOAA-20 | APIACÁ | ESPÍRITO SANTO | Brasil | 3200508 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
