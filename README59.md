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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82c41f3d-a868-360f-a4b4-4a125ff39412 | -11.07951 | -49.74186 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7152bc82-d4a0-39ae-866a-b8bff4d2571f | -9.00813 | -48.024 | 2025-09-15 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d63e559-8f3d-3cef-875e-435fcb7e66a6 | -11.80413 | -50.43199 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 037a81d7-f6ee-349e-9ccd-0dac70e88c98 | -5.48856 | -57.0952 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5542641-1e9f-3a71-ae77-f259c6529d86 | -7.50929 | -44.36971 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd2f00e1-34c8-384f-880f-5ede414d9ef3 | -11.71565 | -46.48617 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a3f78ee-5872-3bfe-b7d3-803c96a11f92 | -6.44895 | -44.52992 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5e4ecaa-9bb4-32a2-b295-561ae3c061e3 | -7.64118 | -49.73666 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0461b0e2-e89f-3dc8-93a4-7921a3634943 | -10.92423 | -45.60181 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a07c335-29ec-35e4-aa2b-6a9e4ec43c33 | -7.89342 | -63.70402 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfa714dc-f0f4-36d6-975b-bc493c7900a7 | -9.23423 | -45.67502 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db5b38e5-0792-3c5d-8532-d8f1efbe1668 | -7.88843 | -63.70732 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e564c31d-6548-3827-9cf0-ac442cbe785c | -8.96252 | -45.78793 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f8770ca-be77-3e0e-b68d-3fc2c72571af | -11.44399 | -46.92728 | 2025-09-15 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e05d0f3-ee98-3e8b-b113-072e791ae4cf | -4.28341 | -56.33577 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 925efc93-9d66-344d-b89f-c82c8bfadfe7 | -10.15914 | -46.14451 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68b25323-e1a5-391d-b824-629c86b3b4a6 | -11.26988 | -50.83236 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ef0f6f7-3445-3736-80f4-ae05a8fedffd | -11.8034 | -50.4377 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a79e3fe-63f4-3c77-91bf-1ec485aee3fc | -11.27018 | -50.82942 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d81be4c-3547-37e0-8e91-0a28f5472436 | -5.9366 | -44.86848 | 2025-09-15 05:10:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7bbf16d-28ff-3ed2-9c1c-31eb36ca1a02 | -11.7942 | -50.43066 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b2e46912-051e-3246-9d87-a60d4e18052d | -4.97807 | -56.1913 | 2025-09-15 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede3eac3-9b83-335d-bf64-66439cff1837 | -10.16033 | -46.14725 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51806e60-9b9f-3819-bdcd-9dc64c62dd03 | -7.78902 | -66.92175 | 2025-09-15 05:10:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93ae3cf9-6d82-31ae-84fd-e225214cce24 | -8.91626 | -45.4701 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a6ad97e-6a43-3d8d-bda4-8c34016f0d17 | -8.97671 | -45.83189 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e51c58e-5a20-378e-9e34-e449a23ee7d7 | -8.59748 | -46.36519 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a04ffed7-e0e2-38c0-9cd7-a91ed9c5b3c8 | -8.92137 | -45.48267 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fcd64283-c853-31c3-b1ca-8c4e02be36ce | -10.17956 | -46.14996 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25af6fd7-7990-3e23-a9e9-7663e1e13ba7 | -11.85928 | -50.5214 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| adfe5075-29e5-3e70-9222-7cf9fe56787f | -11.99985 | -47.75266 | 2025-09-15 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ddc72710-143d-38dc-8f1f-b09d3a9223d2 | -5.76746 | -52.36537 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26e84c52-a9b1-3224-a03e-054e67de9469 | -7.70073 | -44.67883 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d617918d-cfa1-30e6-a227-213e3a686044 | -11.7885 | -50.4357 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1dd9c124-3f81-3542-aed9-a12b3f4ae2d9 | -10.6706 | -46.23989 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29f9b8c7-e0b1-3b5e-9b52-fcb380c120b0 | -6.68344 | -45.51168 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16a13498-8f4a-3f10-beea-48b8ae512f8d | -5.7991 | -50.08759 | 2025-09-15 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bad10f2-c02d-3700-b6f8-9a98b37afe02 | -10.66415 | -46.23929 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23fb3eb3-2d94-30d5-95c0-2c6f4ce12404 | -8.60617 | -46.3468 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7945416d-4bb3-3af8-a995-cf73eec08731 | -5.69484 | -49.19783 | 2025-09-15 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d64cea8-01a6-3e5f-8344-ceaf3672748c | -7.68932 | -48.86571 | 2025-09-15 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c7c0ac-7e74-35dc-8a76-5a4cf496c15b | -7.76668 | -57.76801 | 2025-09-15 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 859b0aab-c1b2-362f-a4fd-25e641e980c7 | -7.39468 | -49.99377 | 2025-09-15 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 684d8ec0-6b76-39e7-af7d-08936dcfcb65 | -7.50322 | -55.00188 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21962853-7b3d-3d07-9264-61808cc51975 | -10.40159 | -48.61433 | 2025-09-15 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c68f3a5b-2841-3237-8780-89c885ed37d4 | -8.92451 | -54.44866 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02c37ecd-64e8-3add-9d0b-8979779b95a5 | -6.8924 | -56.564 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea75003b-6680-3b76-b00f-b4c439fd04a1 | -9.46047 | -61.00863 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 052fe132-4fa7-3d4f-a8d8-55809bc06bf7 | -9.73548 | -51.88295 | 2025-09-15 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b98bf95-8474-3b9f-b490-845b21085def | -11.71103 | -46.48158 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41c250e8-8f0e-3d24-ac7c-aaf03b941670 | -7.3635 | -44.3575 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed6e8288-50db-3565-9e3d-c2d88ce8ef3b | -11.07518 | -49.73497 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba6e9fb1-4115-302a-94b4-621f02ce1521 | -7.68975 | -48.86255 | 2025-09-15 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 378a9884-475e-302e-be26-6b5961b91805 | -6.97223 | -44.54826 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69070d02-aee3-3847-9002-a121bb9e4dfd | -8.91699 | -45.46426 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1657b7-eca2-3942-8c0a-f159761f2322 | -11.0813 | -49.74273 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57fdd9dc-2647-32c2-9c29-f59a404369a0 | -6.40104 | -46.93838 | 2025-09-15 05:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae6eb5bf-4038-388d-a092-de2a0cc15ca8 | -10.72494 | -44.78003 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 902cf757-9209-3191-b807-595226740cae | -11.83319 | -50.44167 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a07293e-72a4-3b71-8886-f28148014dd4 | -10.32437 | -58.73303 | 2025-09-15 05:10:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59d93307-ea92-3e33-88dc-5dedec1db3ca | -8.45432 | -64.13995 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 456677e7-fc94-3473-82fc-3edc154efd5c | -10.41806 | -60.45997 | 2025-09-15 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 854a09fd-9c5d-3a74-aa73-117ade6d6344 | -11.29226 | -51.14093 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4d75b2c-c674-3eaf-af24-68d1e48f667b | -5.93003 | -44.86754 | 2025-09-15 05:10:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efee022d-9725-38d4-9bff-5c44022a327f | -6.45404 | -44.52708 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ff248cb-a8fc-3bea-be8a-f337ff8bba90 | -6.40742 | -46.93515 | 2025-09-15 05:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 002dcfb4-b876-3058-b5b9-d95d332640e4 | -8.62746 | -46.36773 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0913f50e-0d83-3a1c-802b-8692ffd13841 | -12.11593 | -44.84215 | 2025-09-15 05:10:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 489a0ee4-963f-3edc-83ce-e3d856c7134f | -6.66431 | -45.55755 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c166f98e-d5a2-3f88-a5ae-b99921f76643 | -8.62658 | -45.72723 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5aa25958-4e5f-3888-bab9-2fcfd8c0ca65 | -8.98471 | -45.76824 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc649b59-962a-30c4-9915-82d533a496a9 | -9.69412 | -61.99981 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e2a2de5-8ae7-3140-92d3-1a4ccb613a01 | -11.08285 | -49.7303 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59e043c5-6d81-3f65-9366-08fcedb37daf | -9.14634 | -62.39243 | 2025-09-15 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c264647-e445-3cea-a7d3-cb89cb46e614 | -11.29695 | -51.14158 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a117813-927f-358d-9fd4-e93dd97c0af4 | -8.45336 | -64.14683 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a43231d-77bd-389a-a7c7-083ed8c11eeb | -6.9731 | -44.54174 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 749d0871-8fd2-3c80-83db-b638318db65e | -11.44065 | -46.90296 | 2025-09-15 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7652512-9d85-363d-b680-00b729a5c7ff | -8.41411 | -47.2236 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed8b1b68-4129-378f-984c-9efcb8fe4faf | -10.42731 | -60.81703 | 2025-09-15 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d483d777-6969-3799-a66e-0d578216a6da | -7.688 | -44.68145 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e98f800-2279-35e0-9cdd-99477413b664 | -8.92841 | -54.44294 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec7bea6-e138-3f2c-9186-b0e24dd13b0e | -8.97339 | -46.21324 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 30ae62b4-7cb1-33c5-a1ff-172624a5dfa9 | -11.72266 | -46.49362 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd33d194-6656-37f6-96c3-046d436ba340 | -5.63712 | -45.94962 | 2025-09-15 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55b6feb9-6c89-337e-8917-21200738a929 | -7.69454 | -48.86637 | 2025-09-15 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb4861fe-427b-3d0c-a6a4-d28093d1e8f7 | -9.73109 | -51.88257 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efac3e52-d402-3228-b835-d1e50145b627 | -8.97801 | -45.82159 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79c9ae2a-f31c-3ffe-8b88-f2afd9c065e3 | -8.61815 | -45.74228 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21c95f74-f1a9-39cf-ac72-adffc29c9753 | -10.1777 | -46.15257 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78dde5e4-57d5-3a05-b2cf-078e108936a7 | -8.64669 | -46.36555 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c2085bb-6c01-3b22-a2d7-bc2c7e9dbe2a | -9.17662 | -47.04882 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3e9a492-e1b6-3566-8e44-47e50592c2d0 | -5.75126 | -57.58268 | 2025-09-15 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a00e1a5c-d369-3b58-8c3f-89959fe404c7 | -11.79407 | -46.65694 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10aa7610-0bde-3fd2-864a-814abddcf84a | -8.41996 | -47.22453 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d39ad3e1-8e91-3758-9dec-1292db34e015 | -4.79747 | -56.10913 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0b77a33-2cbf-322e-965d-7bea33a09b18 | -10.14704 | -46.14935 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fc5e902-dd4c-33c7-a0e8-a4efb44d425c | -12.01102 | -46.66424 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bb9715a-c9b5-39cb-9b28-06409b4e222a | -8.96184 | -45.79339 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88a7dd36-eb4b-3b37-acbd-e0e8b06ee95d | -7.30586 | -43.93402 | 2025-09-15 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README60.md)
