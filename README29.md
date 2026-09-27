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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1c6c282-9c9d-3276-bcb3-b9831b9d85ac | -2.91026 | -54.11467 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19631f1f-696f-3906-9c01-8e1192536dee | -5.73653 | -45.03811 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02b6eadd-3a06-360c-ab9f-a02e8a65b0fb | -6.28307 | -53.3792 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34e81fa-cd8b-34d7-8e83-d0684c19cee5 | -6.87408 | -55.5859 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c702a9d-82f2-3f39-9a6c-9f61cba777ae | -2.99974 | -51.24496 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66699f01-939a-3eaa-93c4-c10d1be7ef0b | -6.07437 | -57.81071 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a726ba1-3da2-3f8f-95be-df60970cbcd5 | -2.90967 | -54.1184 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e77f21f1-0010-35c4-9e89-a8e1b597bcb5 | -3.97164 | -59.34549 | 2026-09-27 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 990441ed-9715-3ac3-a8e4-c53cd1c4bd1d | -1.6184 | -54.92356 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 089f144a-4694-367c-936a-9a52bd8a8713 | -3.0153 | -51.53783 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99debca8-a5be-33ec-a098-96a98fc0c4bf | -4.27371 | -55.25952 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3404221e-ac7e-33d8-9391-3484adcac5cc | -8.36625 | -44.16484 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| d76fa18b-3045-3c5e-995c-4c955ec1f556 | -3.44737 | -50.08823 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b962622f-90a3-331a-b0bc-c5b10d7dd9bf | -2.94694 | -57.71377 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcbdec6b-f9d2-3676-95ae-c60dcec26a27 | -8.34849 | -44.13503 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a247a4af-1ca0-3c92-99a8-ffc9d5f0ea50 | -6.47146 | -53.52277 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 250443a8-6f28-3b90-913a-d96f1de9fac4 | -5.48079 | -48.57862 | 2026-09-27 04:51:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a3891b4b-4eda-3032-8519-b03eae625e54 | -8.36756 | -44.15481 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c16dcfc5-7603-3683-9258-72b792b1091f | -4.49455 | -54.94653 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1220bc69-0e4b-3acb-803c-6fe29f6b65a7 | -5.1794 | -46.08472 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05464622-435e-321b-81af-e5da55899d55 | -2.44605 | -50.25352 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc91303-6fca-3528-8332-ffdd2c44c20d | -2.84198 | -51.38327 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94c472f0-2f02-3f28-84a3-e8dc1f1014e8 | -3.29787 | -52.08526 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2854cc1b-0bd6-3f13-871b-5009144a09ea | -8.36139 | -44.16074 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| a058e22f-dc18-3c41-a069-1931fcf51c57 | -7.47462 | -54.98567 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75e1c8ad-c856-34c4-95ee-f3171b617b01 | -6.06456 | -57.81287 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66f437f1-bf1f-3388-ab3c-b68da88479ef | -6.07077 | -57.83196 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b4dfd6-cb3f-32ad-b201-a5b8c1b294cd | -5.7383 | -45.05972 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| baf25765-746c-3139-b2cb-83b887077c7d | -4.50579 | -54.98837 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef55b3ed-999f-3306-a78d-10e6b02a5487 | -3.99095 | -50.70621 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab83ccf5-1619-3713-9fb3-85f35f951ba8 | -4.04757 | -45.33276 | 2026-09-27 04:51:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| afcb1f5d-882c-3ef6-b21c-7767312603b5 | -2.63653 | -48.55999 | 2026-09-27 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d53d6f9-eeae-3b28-b8de-37e100dfdd8d | -2.05408 | -54.48299 | 2026-09-27 04:51:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432d41bc-c41f-31c4-a2fc-4679a56a9464 | -3.74018 | -49.36086 | 2026-09-27 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0bad95-d42a-3d03-86c0-89c0c5878491 | -2.57514 | -54.01356 | 2026-09-27 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678529d5-1837-3555-8d2b-1f3c383d28ff | -2.66955 | -56.45694 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 57208777-8f73-36f7-93e4-200397a8adc2 | -3.22887 | -54.32154 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99864156-fcb9-3684-ae4b-ab8c47299ce8 | -4.97914 | -56.19428 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4685fed1-cd1f-350e-9829-d38e5aadcf7d | -2.55131 | -57.41339 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdc5b2b6-e5a9-34ba-85f5-5c3cbba377ab | -2.9277 | -45.50964 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89f3cec4-e7c8-3710-b1bd-a4f01bf55242 | -3.26735 | -50.14122 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3cce25f-8f31-3cf0-98e8-06810a3038c3 | -2.96135 | -54.08051 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c972c074-0eec-32c3-bf81-8e08802766ab | -4.54172 | -54.96583 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88d2c161-81e7-3896-b0a9-db6ea82ab38a | -1.90212 | -52.0877 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4ad5778-cbb8-31a2-b52d-9781e306badd | -5.73756 | -45.06483 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc651e5a-6a20-33d9-84b7-61841de31524 | -3.41998 | -50.42331 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13d53c4-0261-3a52-8fa8-1bdf9aaf4c75 | -2.73951 | -49.46253 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c3089625-cc93-379a-b2a3-c48a0ac39017 | -4.57235 | -54.93098 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a20ec9d2-f7d0-3525-a9a7-0a178694bc10 | -3.96567 | -50.71337 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 483e2704-c71a-3a38-a3e9-f22951c90859 | -2.13211 | -52.3557 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fd244da-6fa8-3b46-a882-4dbee4ba5076 | -3.20898 | -50.40295 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc3244c0-69db-3a2c-94f8-4cb783394319 | -2.93215 | -45.51034 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd945a9b-9195-3d98-97ce-f9883d45ddbd | -2.79648 | -57.70214 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3eb6b3ae-1a8f-39a5-948e-9b0af2a36a32 | -8.34548 | -44.15844 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 433d3d25-0d7a-3a0b-9c84-dbe643602b2a | -3.00334 | -51.30947 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61005077-e279-3dae-89ca-da579ac8b210 | -3.00719 | -51.30651 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30429c2b-5b90-34d8-be4f-df8975e74aba | -4.28986 | -55.24976 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4621a81b-2165-3613-8084-d94a1f90b89f | -8.11549 | -49.58679 | 2026-09-27 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c81b15-8dc0-3421-b6f8-df2d5008586d | -2.17697 | -55.16658 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782b172a-8df2-3493-b583-270519cc1130 | -3.04067 | -57.50592 | 2026-09-27 04:51:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6893afad-414f-360f-9a75-a763af6fe1db | -4.9782 | -56.15316 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0926ad1-1aaa-35ac-8a06-6e3bb9c7bd90 | -7.33657 | -42.08368 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dc9f68eb-ed80-3468-99a7-959eac30931b | -3.26522 | -46.61828 | 2026-09-27 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfd4f8f0-398c-3af7-8afa-1345789fd2f9 | -8.35474 | -44.17618 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| cb732c51-3e9a-3876-9ea1-d4c27f0b7bec | -8.50413 | -54.94554 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fddcecb-f5e6-3a4c-aafa-7c3d2fb9dfb1 | -3.18842 | -49.24902 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d79edf28-bd30-3be3-9508-631a1a21c2fc | -3.30093 | -54.69053 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f01d30f-9464-30e8-8d5f-c8b92ddaf602 | -6.16937 | -44.59577 | 2026-09-27 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 242f4f6d-8dcb-3bf0-aeed-00c2aaeb426a | -5.18029 | -46.04834 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002377b0-be0c-3086-8907-34af91630bb2 | -8.34069 | -44.16046 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dcd176f-5c75-31f5-83c6-2fb0b1ccc0d9 | -3.22946 | -54.31778 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1de74b3-daea-3d04-86f5-ef50fe28a6e6 | -8.34421 | -44.16833 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e5cc0c1-749a-37c9-80e0-60895492029e | -2.91271 | -45.42564 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf55e01b-df25-3a3e-80ef-495895760924 | -7.36785 | -42.12472 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 859fd042-7f08-32fc-9717-ce43c3e0ddf0 | -4.25784 | -51.04729 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b952360e-3e85-3303-b2bf-03e36490259e | -4.28859 | -55.25777 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e13ab099-6a11-3dbf-b506-51a9674f963d | -6.7057 | -47.07636 | 2026-09-27 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 867cf021-976d-3d81-95e2-27fd4ea08ee7 | -3.07455 | -54.40674 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3c8df58-70e6-3bbb-bac4-f1a643a2d63d | -7.01329 | -52.7368 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2485a4d5-0a3b-384d-b2e0-04667b721659 | -8.33936 | -44.17021 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2baa032-1b9c-3893-b261-7ca6b4aeb449 | -3.4132 | -50.42223 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b19bb3-44be-3310-85fe-1356a11327d5 | -4.24236 | -55.15976 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab6e6eeb-6f49-3423-aba3-b3e3ee708c3d | -9.08262 | -49.87339 | 2026-09-27 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52c33ea6-34a3-3b3c-bad1-8e043b372bab | -6.09465 | -57.62782 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92983501-5639-3cc0-aee8-7230f41d6bf8 | -3.01448 | -50.29881 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6aa33671-f20e-3c90-a53e-bd6805d5a8ac | -3.10547 | -50.32367 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bf26bbf-3f95-392a-a0bd-0150f14b11fd | -4.09929 | -54.32383 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5b19050-c9ea-30f5-8f71-b31d9e2c2ea8 | -4.49172 | -55.56864 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b5a02a6-1b5b-3dfc-83cc-808138f4ba2b | -2.61223 | -51.74604 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| babb9139-b0ea-30e1-aeab-a58c6fbaf6e7 | -3.97069 | -48.00583 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddb5690c-681c-35b4-b54d-3fa518fa329c | -9.10347 | -54.69277 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6929b62b-aa1d-35b7-92e4-e500044e15e9 | -6.31685 | -43.3417 | 2026-09-27 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b506fae1-95e5-3a84-952e-14ffc12edc99 | -8.36669 | -44.1615 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| db65692b-0c89-3a38-ab32-c6b46546b000 | -4.14758 | -48.22045 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd8be093-3813-380b-a2dc-778cd1b0f2dd | -2.91738 | -54.18113 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1fd4f08-81fa-3a1c-8a72-a92425bc5922 | -8.349 | -44.17865 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c3a0be0d-2a12-32ee-8c40-edf6886e30d7 | -8.34591 | -44.15513 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1798f0ce-c789-3340-9e5b-eb1e140dfbc4 | -6.13559 | -53.06113 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 393e9ca0-849e-323e-9fb8-bc0799c2dd27 | -6.7874 | -55.82763 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d4191dc-0916-347b-8ed3-48b8304c1fac | -6.05655 | -53.60714 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README30.md)
