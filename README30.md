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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad116b0b-62cd-34e7-9712-a3b8b367500b | -12.46609 | -46.98348 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 191dc0f2-99ae-33c2-aecf-61e3b700c8af | -9.3505 | -50.25597 | 2025-08-16 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daa422fa-fd44-34e2-8102-fbd0d015a350 | -7.41928 | -44.90972 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb2f537d-91c4-3ed8-9ded-1612b2b607e1 | -7.70479 | -46.18764 | 2025-08-16 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75c18480-a8db-3521-91a2-1cc129d6c2ef | -11.54592 | -47.26764 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef8ece2-8906-351f-918a-cd19eea789e3 | -7.39584 | -44.89287 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3f662ce-a4aa-3300-b79d-91c16c055cf7 | -12.60641 | -46.95636 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e06e6b3c-2a8f-3e71-8690-349a69a80dc7 | -12.48835 | -47.49947 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9e74c33-56ea-3d8a-be18-dcb7560c873b | -9.87514 | -47.4135 | 2025-08-16 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7ada3d3-123c-383e-bfd5-51852ed62b9a | -8.19255 | -45.02174 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fd520a9-c26c-3441-8cb6-cc8d520be688 | -12.59963 | -46.95015 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c7e42da9-8deb-3409-987b-6b21aba71397 | -12.55275 | -46.97139 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| cb0af4b9-3bcd-3e19-a6ec-a9d7e96e126c | -7.40385 | -44.88972 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc37d0e9-83b7-3777-a35d-8137f58f7e33 | -11.30839 | -42.1309 | 2025-08-16 04:10:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c6b4140-3251-34ac-ad38-191933e2e024 | -6.5493 | -43.03723 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98c0b1a2-9179-3c71-ad87-a71637ce134a | -11.07289 | -48.35815 | 2025-08-16 04:10:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1630d70-eec8-3b77-816d-d1ac40a532f9 | -9.80301 | -48.53766 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6dc2cf4-74b5-331b-a855-55dc53c2640e | -7.08307 | -43.84774 | 2025-08-16 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58efbaf4-734c-31e5-a10c-23677523f742 | -11.92952 | -44.12365 | 2025-08-16 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e380fd0b-6ff3-3147-b7e5-e0161967128e | -12.55359 | -46.96655 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1d6ff51f-2c60-3368-b5f8-24703173013d | -11.36019 | -55.42748 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 684a75e4-17b9-30f3-a8b8-df024b2363bc | -9.34075 | -45.9833 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed5dffd0-c453-3fd0-ac27-5914ef0f1bb2 | -12.60075 | -46.92083 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 40cf3b4f-4faf-3738-82b2-b12c9864db57 | -12.60047 | -46.94527 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef4bbe45-025d-3256-8166-2b13a46ea445 | -12.8462 | -46.05323 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaf200a0-6f3a-318f-9b02-161d5624cae3 | -6.85959 | -42.80439 | 2025-08-16 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1243bb68-f599-3600-bfb2-78bcf5388a2e | -12.5375 | -46.96868 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 152247c3-129b-3738-ae46-a859aae3ddfc | -11.07715 | -48.3589 | 2025-08-16 04:10:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10135cd9-f1e9-3070-849c-bd426db7b60e | -10.3576 | -49.9302 | 2025-08-16 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da98ee2-5108-35be-b7b0-97b6a4f8b810 | -9.16503 | -45.32479 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a99b223-3f16-3740-bb23-94619768c505 | -12.82165 | -46.02265 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fd28166-2099-381e-bb85-1bb3a4b4d1bf | -10.17424 | -42.28681 | 2025-08-16 04:10:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 227a2f22-394a-303a-a5fd-bef58442b78c | -8.38133 | -47.005 | 2025-08-16 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b28199e-ffa4-3257-84d5-7d6492bf80c1 | -7.54775 | -45.42166 | 2025-08-16 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c7caf32-aa5d-3916-a889-6cd480badb3a | -11.35744 | -55.42714 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9538a42-3a32-3292-8b73-903878606b45 | -9.85608 | -47.81736 | 2025-08-16 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dba58c2-b57f-3878-b568-d9378f380bc4 | -12.6085 | -45.23288 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65249672-3edc-3bd6-b9fb-abdf8164e3bd | -6.54813 | -43.04452 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9373d148-69ee-34d7-965b-fddc314bedbb | -7.01741 | -44.3173 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 583dd8cf-ea36-310b-b521-4d973590dde4 | -6.55153 | -43.04508 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f65073fa-df8e-3572-bcfe-a1a6882cb9a7 | -6.54871 | -43.04088 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24fa1f68-58a1-389a-8d94-131a42bc2c13 | -6.56487 | -43.0507 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bed9e401-81e1-3fc5-a558-6448000b2516 | -11.34959 | -55.43176 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 618d745e-82c1-3c60-8133-5a357817dc61 | -12.47454 | -46.9801 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7579bb1-7dda-3fe6-96fd-165811de4890 | -7.44198 | -46.13137 | 2025-08-16 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54e8fbee-ad44-3bee-8ebd-a6fb97bdd33c | -12.30023 | -50.00698 | 2025-08-16 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e70dd3ca-5ac3-3b18-b8ee-c5997586fc63 | -13.6506 | -44.2023 | 2025-08-16 04:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c992fad6-f470-3667-8be8-047cf33f0619 | -8.9497 | -45.80233 | 2025-08-16 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6dfe1f4-8694-393b-80ce-92690cbfe9f1 | -6.93871 | -44.56074 | 2025-08-16 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 534d99c0-a002-3e15-b44d-ebfed674e7aa | -12.59997 | -46.92538 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 9b53f1f9-890b-37d2-a935-bd2a2276edf7 | -7.59772 | -45.21103 | 2025-08-16 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2972ddd-4ec9-3bfd-96c8-acd013e0f989 | -7.5334 | -50.524 | 2025-08-16 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d33b1942-ab22-3d48-9682-97ae90e29a2c | -12.92761 | -46.95724 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea215d65-4da1-3631-860d-bb4661655948 | -9.85958 | -47.82212 | 2025-08-16 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3424aff-c2c2-35fd-930b-b7e21e7b8cb8 | -9.8074 | -48.5385 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ca5c0a4-2062-3c97-af0c-dab8adf43973 | -13.57105 | -46.97415 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1a8a74e7-63e2-31aa-a51c-5f12d65ae63f | -12.29743 | -50.00816 | 2025-08-16 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 967f9de6-9c6a-3aa5-83d0-80f4b5de7a6c | -11.3111 | -42.06995 | 2025-08-16 04:10:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3fd14248-cbc3-3607-a56b-37134647e47f | -10.95458 | -45.18636 | 2025-08-16 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed9a8b84-7c9a-3197-b058-691a7a7c3f96 | -8.38538 | -47.00582 | 2025-08-16 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad3ec639-6838-3bb1-a1cf-1d54f393552a | -9.17668 | -45.32238 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d021b134-6975-323c-93ed-992170e698b2 | -12.60889 | -46.94186 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 63e4c267-6362-39a8-9170-b5a6a27f662c | -6.54531 | -43.04033 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34e23dcc-5f5d-36da-b27d-3356d0475633 | -12.55741 | -46.96722 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 75df9339-7210-376f-92ae-aa039d51783d | -13.86946 | -45.55647 | 2025-08-16 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 691d34fb-bd42-3538-9c9a-8c077b36a0b1 | -9.26345 | -44.55873 | 2025-08-16 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d09179a-156e-3693-b75b-9461207c9f85 | -9.06732 | -39.15974 | 2025-08-16 04:10:00 | NPP-375D | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b0d1584-35f1-3132-9807-efa73effa7d4 | -12.59917 | -46.92999 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 64abfced-63c9-31f4-8aa7-228507794eaa | -13.87013 | -45.55252 | 2025-08-16 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4000d212-3d73-39bf-8756-c0a8ce4a9af1 | -8.34365 | -44.94269 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba81c1e7-3bf2-3d54-8269-9eea8a125fa9 | -10.45831 | -48.80891 | 2025-08-16 04:10:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c6f0a44-4aa0-3f62-bef6-9c73dd83f821 | -9.1621 | -45.31993 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fe49a9d-375f-3f9e-9012-6e6a57b417f0 | -12.8267 | -46.01485 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e48cded8-7aa7-3477-ba76-1a6bdcdc9c80 | -12.92383 | -46.95649 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf262e3c-c060-3f9f-81ba-9c84a33cc4f5 | -6.7818 | -44.35203 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8ebacd1-10cc-35a1-84e1-a1c3c530f686 | -7.62109 | -44.93141 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 060c179a-4194-36b9-a02f-d1de5eff8b68 | -8.18774 | -45.02682 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb7a80b0-ccbd-3c03-863d-604d5889ac96 | -11.34834 | -55.43797 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6529c5b-fca4-3ad8-965b-eb1764af14c7 | -9.80663 | -48.54281 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9e93e09-4d9d-31bb-9b3c-11e0d02600c1 | -7.69027 | -48.00127 | 2025-08-16 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a3a7e43-5ff7-38f1-a9f8-63625bcd3ede | -12.83464 | -46.03372 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 759fc09e-4b10-394b-8fdf-987e8bdd2364 | -6.9199 | -44.16816 | 2025-08-16 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 679ca04f-ac01-3d6b-ae66-5ddf95fd2934 | -12.58018 | -47.04018 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f592e335-6f6d-33c5-bc2b-a6c3f3c277ce | -13.6512 | -44.19865 | 2025-08-16 04:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 016d5e3c-9786-39c5-ac6b-7f3646bdda36 | -7.38732 | -44.92175 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85866cb9-7ab8-35ca-a4dc-ad7749f001f8 | -12.46991 | -46.98416 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8401d7b-fa7e-3d7d-a706-790bf90ebabc | -13.57796 | -46.97894 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b20bb10-1903-3d35-826a-db89b82a3b07 | -7.38409 | -43.79702 | 2025-08-16 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e8b5805-b4f9-3422-801c-3bdd72e1ad46 | -6.55046 | -43.02994 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93a9f08d-0286-3c49-8ab2-6bbe2cf812b9 | -13.64784 | -44.19808 | 2025-08-16 04:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9766cd5-0b4f-39f6-8b45-2ec24dfbf41b | -7.41183 | -44.88673 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6017c285-7c17-3d4f-ac53-736be5bb56b3 | -5.62686 | -51.29885 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9227a8ec-a2e0-3c46-8b52-2f26aebc0a96 | -7.63082 | -42.32399 | 2025-08-16 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c319bfec-2016-3a99-87a1-06c4dcf7b7b5 | -6.61702 | -42.75072 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6b128cda-4c74-380f-87a1-df57a369881f | -8.17027 | -45.01955 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4afaaae0-b441-3241-a05f-d4315fd2df88 | -11.50661 | -47.24295 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 801b73dc-7d79-3b2e-890c-06810573731e | -12.82742 | -46.01064 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f65c6733-63a0-3c78-a968-e70cc069047a | -7.38366 | -44.92119 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e9455fa-11e3-3a39-83ac-d163c43a3e00 | -11.90357 | -43.43627 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cb2b8d5-9073-3564-ae88-40f0b3476f91 | -13.45512 | -47.06211 | 2025-08-16 04:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)
