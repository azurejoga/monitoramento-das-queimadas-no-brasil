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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 055f6142-04e8-3d9a-91ab-4c3649d341a2 | -1.164 | -53.66144 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8c5b0903-d7a1-3e29-9baa-0e78aab5b450 | -2.71542 | -53.99044 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3d658a4-0f32-3edf-93a1-757d8607fe71 | -2.71074 | -53.98986 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2dfcb646-5eac-3837-a46f-42696934890d | -2.63226 | -54.32747 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 643c3f3a-e672-3c5b-b09c-9773a0cb80d0 | -2.32313 | -54.39059 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80054aed-ebd8-35f3-b8b5-a32ea2d941fb | -2.3212 | -54.37779 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0525272-43fc-361b-99ec-4651b536cfa6 | -2.32037 | -54.383 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18868ac1-5492-3f38-991a-d3605fdfe7a1 | -2.32006 | -54.37939 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4efe01de-3037-373c-bed6-6ee25b861dc9 | -2.31954 | -54.38821 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a0c9689-0231-3d99-8542-869f67641be3 | -2.31919 | -54.3846 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 892bab06-b4a0-3508-b755-d2014258809d | -2.31871 | -54.39344 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4593f721-6b72-345c-8fda-7dffe3193f40 | -2.31831 | -54.38981 | 2024-10-20 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cf0d706-70e7-33f8-8b68-b611625c187f | -2.28043 | -53.72371 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4862940-757c-306d-be89-4c9ac1c0366b | -2.27967 | -53.7284 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9040673f-71db-3b2f-b5fc-7d75bdd8af02 | -2.27584 | -53.72292 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa7f1376-1d9b-3e9a-b405-28d44a04aa10 | -2.27508 | -53.72762 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17a14cf1-fd0e-3957-9c84-026ee526dc5f | -2.27048 | -53.72686 | 2024-10-20 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26668a6-bfe9-37c0-854a-ac8f65c5eef6 | -5.5906 | -42.93275 | 2024-10-20 04:32:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5178a71a-b08d-3895-a6ff-693f30ef9683 | -7.81133 | -45.44469 | 2024-10-20 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e8fee7e-bc25-38eb-96c8-924e6f890e7f | -7.80721 | -45.44806 | 2024-10-20 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcff6212-955c-37c1-a555-56c453dfa331 | -6.60628 | -43.42852 | 2024-10-20 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40945985-979f-3763-9b57-de32800cc042 | -6.54021 | -43.03962 | 2024-10-20 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6067e14-8fd5-3375-b306-2a28f16e7962 | -6.53946 | -43.04476 | 2024-10-20 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2788bbd3-6aaf-3843-9621-832cc4da273f | -10.5934 | -44.2865 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba9ed0bf-0a84-3dbe-b500-eaa021d97440 | -10.58952 | -44.28593 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8fe9e7d-547e-3a25-838c-7d7ee70b5db6 | -10.5888 | -44.29088 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de85ad61-0f51-3a47-b6c5-40d7c2d18894 | -10.58492 | -44.29032 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00b97b8e-7c85-3951-9573-12d0a9dc41d1 | -10.58421 | -44.29522 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29e2b326-8c43-378d-84f2-b387f725d52c | -5.3769 | -43.61728 | 2024-10-20 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a022915-c784-3f89-a05f-2ad89678da91 | -5.36482 | -43.56872 | 2024-10-20 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bbfd92b9-a82b-3a8b-baf9-ac1613e66226 | -5.36415 | -43.57326 | 2024-10-20 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea68c441-8c61-3232-bd20-83223d7bac07 | -5.36103 | -43.56817 | 2024-10-20 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| adc4af27-67f8-3dd4-b402-e3835f9092fa | -5.36036 | -43.5727 | 2024-10-20 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c69b4667-1a51-3b53-91c4-3f38c6dd3911 | -5.26568 | -43.98916 | 2024-10-20 04:32:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90cbd873-5eb6-346f-b628-e3bd0ce084bd | -5.26366 | -43.62585 | 2024-10-20 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d03065-1bae-3c46-b846-6e7f8cc612fa | -5.26199 | -43.98857 | 2024-10-20 04:32:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 205a0bb4-fdf5-34d9-83c9-0faa5c00964a | -4.74714 | -42.96767 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ac6d023-fc3c-3f2e-9bfb-b65d1f7ca6f2 | -4.8621 | -43.24373 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b746cf8-b7ec-3d15-9a53-1dfd7714c565 | -4.8614 | -43.24843 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb7841a4-6726-35c8-b771-663efe1a2ffe | -4.86003 | -43.24618 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caea5904-467f-34a1-9a83-f5a3b7edbf59 | -4.8593 | -43.25089 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4baa0512-0239-368d-a990-31c9875a1e4a | -4.85757 | -43.24784 | 2024-10-20 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f893ce5-7dec-3e56-adaf-9ac6461b6078 | -4.58461 | -43.98424 | 2024-10-20 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a94369-fb49-33be-ad27-56da87ec066e | -4.58031 | -43.98789 | 2024-10-20 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1ed3269-f5d6-3dd9-9b7a-d813b5ecba7a | -4.40054 | -43.84974 | 2024-10-20 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c92c80-9b89-3ac2-bd98-a941e8eff572 | -6.14588 | -37.81126 | 2024-10-20 04:32:00 | NPP-375D | FRUTUOSO GOMES | RIO GRANDE DO NORTE | Brasil | 2404002 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 33839a04-04ac-33d4-b6aa-ac54f5efeaed | -6.14026 | -37.81038 | 2024-10-20 04:32:00 | NPP-375D | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8f40e6c7-509d-3083-b074-d14fb97aae76 | -5.95012 | -43.38639 | 2024-10-20 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ea96f798-d4ac-30a5-97ca-d7ea59060288 | -10.58033 | -44.29465 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc213c92-7fdf-321f-9af4-1d9ebe0c8abb | -10.57645 | -44.29408 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 278db1ad-e429-3582-a79e-efdd9156403b | -10.57327 | -44.28862 | 2024-10-20 04:32:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce9b1ffb-c1a7-3d26-ab0a-a2062c9e6778 | -5.93123 | -43.84754 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb759ecc-4213-30a4-a6f4-b4803574d464 | -5.85525 | -43.74114 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad0f2c47-baf8-33c3-8b68-7ad2189ac53a | -5.85454 | -43.74573 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 228eab58-d519-3c79-8002-eb07a242d04e | -5.85453 | -43.74325 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14a84af1-2fd6-3b04-97fa-e1d2a6017b27 | -5.75533 | -43.4831 | 2024-10-20 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e74e6f97-d04c-3901-b983-1490322891f0 | -5.72844 | -43.8123 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3be6929-2ca4-304a-805f-813bfa85c715 | -5.72267 | -43.77465 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4ab6fbb-2e9d-3e1a-8d10-dd44a0fbf167 | -5.71959 | -43.76962 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cee359f-1633-3b1f-90e5-7f0ed4edd4cc | -5.71891 | -43.77409 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4396a71-97b6-3d3c-8f5a-57f8e325ef02 | -5.54558 | -43.90522 | 2024-10-20 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c000ed6-d252-3d0c-8569-145e736ad1a5 | -5.54491 | -43.90968 | 2024-10-20 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76c0dec4-33c5-35e8-8528-8262a338f784 | -5.54252 | -43.90022 | 2024-10-20 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30f7c645-939e-3d33-acc7-8921f73be2a9 | -5.54186 | -43.90464 | 2024-10-20 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f3f07cf-c279-305b-9a90-db26cd749ef6 | -5.54119 | -43.90908 | 2024-10-20 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54a38051-b9f2-31ca-bd1a-1a2aa69c2f44 | -5.52648 | -43.95657 | 2024-10-20 04:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5d109f-4594-37e1-979d-93dc316c2d36 | -9.9237 | -36.19026 | 2024-10-20 04:32:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a2ab4857-0524-3a00-96d3-e8d96c48f665 | -9.92302 | -36.19588 | 2024-10-20 04:32:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d2567ced-fdc7-326f-b0a9-d5ff39c3fb94 | -9.91712 | -36.18949 | 2024-10-20 04:32:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 74c6829d-b321-313a-a882-b9c5fd49d44c | -5.94556 | -43.39054 | 2024-10-20 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4c1ef8a8-d8d6-3225-be3b-2df20443f5ff | -5.92911 | -43.36842 | 2024-10-20 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ea51f5af-af9d-3a3d-917a-3de2e09a1c4d | -5.9224 | -42.95752 | 2024-10-20 04:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 558cf3dc-9861-3b7d-9d09-b11e7b935e5a | -5.91844 | -42.95694 | 2024-10-20 04:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| fb00f451-ab34-3753-b727-7ca5ea499a54 | -5.6172 | -42.781 | 2024-10-20 04:32:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 115be2d8-eafa-32ea-b425-262ded04d139 | -4.89954 | -44.63056 | 2024-10-20 04:32:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8001ee7-cd89-3903-b5df-6040ddde66c8 | -4.89892 | -44.63464 | 2024-10-20 04:32:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bb221a2-3ff4-3ed5-a91e-412e55fb076c | -4.81914 | -44.354 | 2024-10-20 04:32:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa873111-ced3-3e53-9977-a6b33283375e | -4.48826 | -44.58892 | 2024-10-20 04:32:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a071a178-a72a-37a9-8d45-cd71750fb8e8 | -4.3126 | -44.25371 | 2024-10-20 04:32:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04118567-18fd-3a50-80d7-04edab377a11 | -4.29008 | -44.51968 | 2024-10-20 04:32:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25e8ee70-a0e5-31e2-906f-fa3aa1fcfcca | -4.28946 | -44.52369 | 2024-10-20 04:32:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 538d5e32-18f5-3284-92af-ddd6d133f5b1 | -4.28652 | -44.51916 | 2024-10-20 04:32:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38b8c0d4-a2bd-306c-b925-9222b7c5afb3 | -6.41994 | -44.59777 | 2024-10-20 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94876c97-dc87-3de9-8b4d-c5bb375c0346 | -6.15898 | -44.43008 | 2024-10-20 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e033e50b-9d69-39d0-9ef4-6720c45a6ad8 | -6.15535 | -44.42947 | 2024-10-20 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51598b9c-5e8e-3731-af10-4b8bdd2d8ddc | -5.82897 | -44.0454 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f684918-40c3-3d79-a9db-6b693c0b9cc6 | -5.82832 | -44.04978 | 2024-10-20 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34acf7b6-335c-3f28-ab4a-be128a449fed | -5.4718 | -44.17518 | 2024-10-20 04:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5219dc44-a604-37cb-80a3-dd22d9bdaccf | -5.4714 | -44.17418 | 2024-10-20 04:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d2d6780-7e0f-39da-92d5-baf9a59f8796 | -5.47077 | -44.17845 | 2024-10-20 04:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd13d45-7ff5-3abc-9942-e71fec51db6c | -5.30782 | -44.12599 | 2024-10-20 04:32:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ef36e8f-76a4-3fe8-8e1c-eac586d57957 | -5.25051 | -44.20861 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a44f8a-6a49-3859-8fd2-716371f91af8 | -5.25029 | -44.21022 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78167a8d-f029-3e02-943a-602a5437a8a1 | -5.17913 | -44.03785 | 2024-10-20 04:32:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a423fc45-efe3-3df9-825b-f741ca5a7b36 | -5.17848 | -44.04217 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52dd27b1-b235-3dbf-abc9-db8bc1283fc8 | -5.14562 | -44.16611 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44c9c794-a5e2-333d-bbf6-91d19f029156 | -5.14529 | -44.16409 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e52583d-769e-384e-aa4f-67ca45ebb5e9 | -5.14465 | -44.16834 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6673ab5-c8c2-3bdc-a82b-dc8883ca8fec | -5.13487 | -44.09023 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc0ac266-39f7-3991-983c-354ea45b21cc | -5.13421 | -44.09451 | 2024-10-20 04:32:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README32.md)
