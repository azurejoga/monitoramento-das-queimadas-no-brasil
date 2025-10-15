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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bc432e5-d921-3dae-91a9-333e1895e575 | -7.9439 | -44.1381 | 2025-10-15 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4a688f4c-86c7-3238-88f8-6c8bee01353b | -4.8915 | -43.4678 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 318.6 |
| a7b18e26-434d-3b23-b99e-4ffbc06c19ac | -5.4463 | -44.2388 | 2025-10-15 03:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 60e67d96-a9a5-355a-b0b3-1630a22b1e5b | -4.8916 | -43.4446 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| b9972183-9290-3e0c-9ad9-b4a79c390d33 | -4.6509 | -43.1337 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d84e4b09-6c1c-36c3-a75b-7ab41c9516f6 | -5.4465 | -44.2159 | 2025-10-15 03:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0e4eb958-41ea-3cbb-bb77-197a98d7d729 | -8.2275 | -44.0853 | 2025-10-15 03:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d46e1cd8-922b-355e-a033-e9a811609fd6 | -4.9102 | -43.4666 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 11847223-868e-336b-b894-8d989343778b | -4.9104 | -43.4434 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 1a6449b2-9d60-3423-9e7a-8382bf291643 | -8.2278 | -44.062 | 2025-10-15 03:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0ced2799-dcfa-38a3-be66-4994a1ce7ac6 | -4.6696 | -43.1326 | 2025-10-15 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b4e86d9d-e77c-30ef-89aa-fe37a40254a0 | -5.95513 | -38.6325 | 2025-10-15 03:15:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 73d3e523-8bde-390d-a555-251b2586c4d8 | -3.94917 | -38.40125 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02b521d2-abc3-3e3b-9210-05b66473a210 | -5.43203 | -40.98634 | 2025-10-15 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c17dabc9-6ead-3d75-8e39-4b69d9c8c182 | -6.05258 | -41.90683 | 2025-10-15 03:15:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 56fb4f97-7b35-3a2e-9bf9-892daedde9ba | -5.27372 | -41.04656 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a23c4e3e-e0ef-3b53-a818-fb3f83c52284 | -4.14037 | -41.65783 | 2025-10-15 03:15:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 84a6b17b-076b-3e00-865b-011a684942ec | -5.42556 | -40.98491 | 2025-10-15 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cee1f62c-db12-3934-b8f0-02cc06e4caf7 | -5.40094 | -41.15297 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 21ad8113-dc6b-3ea8-973b-2f086661e438 | -3.72616 | -40.37875 | 2025-10-15 03:15:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 026ee507-9f47-3ef7-a96f-55eee7cc9a05 | -4.9306 | -40.13976 | 2025-10-15 03:15:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f4a24271-d741-382d-bb44-ee07a79f370a | -6.45967 | -41.83058 | 2025-10-15 03:15:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c669a2e7-30bc-370b-8e37-7bbb86c53960 | -6.05486 | -41.89445 | 2025-10-15 03:15:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fa1db97e-1b30-3f6e-98fc-4e5ce936f77f | -3.7271 | -40.37344 | 2025-10-15 03:15:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbabc6a9-a0af-321c-a603-24f84a1b94d1 | -4.92841 | -40.1396 | 2025-10-15 03:15:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b788a17d-9805-3405-a0f3-ef8f2c1f1639 | -4.14704 | -41.66001 | 2025-10-15 03:15:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 12d2a133-29b4-3760-9094-c67ad449ebe0 | -5.95384 | -38.63181 | 2025-10-15 03:15:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d65e9a3-46ac-368d-9860-9f7f0d601d19 | -7.53628 | -35.20055 | 2025-10-15 03:15:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 92498d60-764d-3dbe-a246-a8c122dc6981 | -6.90699 | -38.26119 | 2025-10-15 03:15:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4818b9e-45c2-390d-97d3-221be7b2f5aa | -5.42515 | -40.98417 | 2025-10-15 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 57daa831-11f7-3a34-850f-520e47b49c81 | -3.76505 | -41.69172 | 2025-10-15 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d3b78e81-b2b9-3f82-a5f1-b84fde2c931e | -6.175 | -42.61619 | 2025-10-15 03:15:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| d05c64d3-2449-3de7-9d32-02f5dcc636ac | -4.14029 | -41.65786 | 2025-10-15 03:15:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 25502ed7-3f52-3321-afff-27ea744f55db | -6.05373 | -41.90058 | 2025-10-15 03:15:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5e2ce12d-6c12-3ece-8bd9-78523c678354 | -5.43161 | -40.98559 | 2025-10-15 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9c4e0ebf-abc5-3ce9-aac7-743abc3271ce | -3.95185 | -38.39915 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7a039e9f-1248-38b4-a09a-b3f0e8556b98 | -3.95319 | -38.39143 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06dab97f-9476-3312-a578-51a587c4ed91 | -5.39219 | -41.1636 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d2e5d44c-3aa2-3f81-979a-ccf174b8ca90 | -5.43058 | -40.99123 | 2025-10-15 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b60ec922-f6d6-39fe-b406-9f34377e0950 | -6.7593 | -34.99826 | 2025-10-15 03:15:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b99c537d-2fb7-366f-9c10-e13624d9847b | -3.95048 | -38.39339 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6fc2532c-1ba7-3f5d-8a98-b99c17ca89ca | -5.42936 | -40.66396 | 2025-10-15 03:15:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e4fae4c9-422c-3c5e-80fa-15fac4fb2275 | -6.90639 | -38.26456 | 2025-10-15 03:15:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 982fbbe0-10f2-3037-8b45-4e2d82751e23 | -3.72556 | -40.37768 | 2025-10-15 03:15:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 483ce265-73f0-3dea-b62e-573c572c5ae9 | -6.9122 | -38.26301 | 2025-10-15 03:15:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 270f4dcb-297a-34ed-865f-d4a7db05b143 | -3.95487 | -38.40213 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 418b1e38-adea-32f6-b58a-247b60be5849 | -4.14712 | -41.66 | 2025-10-15 03:15:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c7f1417b-6d06-37be-a387-7706d9545acb | -3.95253 | -38.39525 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d91ed1fe-fe9e-3913-a3cf-a35c2d9ae08a | -6.45846 | -41.837 | 2025-10-15 03:15:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 48079e1b-551a-3ebb-a3b8-c5b6da9b7adc | -3.95117 | -38.40308 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 045b4aae-4b28-3dda-9cd3-725348f1d7e5 | -5.2727 | -41.05231 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3beeea98-181a-3504-92bc-6dc9e75f9c5b | -5.40246 | -41.15427 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2f908723-a409-3a3e-8325-bf08202ab28e | -6.8427 | -42.7822 | 2025-10-15 03:15:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a3203a2b-775b-36d1-93b8-9940e02b165c | -5.3938 | -41.16484 | 2025-10-15 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10aec8de-d057-3e13-92f1-d6a1a06fb974 | -6.05603 | -41.88814 | 2025-10-15 03:15:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e5e26e75-5371-3749-a4ae-eba29d6e4316 | -7.1609 | -42.49522 | 2025-10-15 03:15:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b93d114d-fcc2-33b6-8d60-2e852def7094 | -3.95551 | -38.39825 | 2025-10-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8e9a701-f4a4-3c6d-b1e3-bb9d751201f7 | -11.44714 | -44.1004 | 2025-10-15 03:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 28902060-378a-3e50-acdf-29f0dfc5246b | -7.48465 | -42.14751 | 2025-10-15 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 45b5f888-5e3f-3fec-ad95-82adff60454c | -7.49257 | -42.14268 | 2025-10-15 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 17bb2589-1943-39d8-83f2-56b7bbfdbd86 | -9.2672 | -35.63506 | 2025-10-15 03:17:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d2ad8ca2-3eac-3e6b-90c0-d53b69590280 | -11.45068 | -44.10206 | 2025-10-15 03:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b74d5ec7-e2b3-3159-908e-9fb66d731068 | -10.82916 | -43.96035 | 2025-10-15 03:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d27dc524-5953-333e-a109-73011dac5998 | -7.5722 | -42.69221 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 424571a0-52b5-3713-9165-eb9f61e96cad | -7.53714 | -42.69242 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cb02cdb8-ca84-3044-b21a-405731bc15db | -7.56958 | -42.70565 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f57c34e3-4e06-3ae0-bc0a-6ed8e4ec7add | -7.57197 | -42.69888 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d73d1f92-f074-3fea-bf27-8df05e997e36 | -7.50048 | -42.13791 | 2025-10-15 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30ff5b77-748b-38be-98b0-a891f09760e3 | -8.97245 | -39.92306 | 2025-10-15 03:17:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e3d8e3e-4017-3286-b366-7e2ffa003b1a | -7.57324 | -42.69216 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4cc27f61-09de-3a7b-a84e-ea8ce05ea369 | -7.7466 | -42.45593 | 2025-10-15 03:17:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0cd660e6-42ab-38db-9589-5e3c26b02ce8 | -10.82756 | -43.96788 | 2025-10-15 03:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 458aebd5-7c87-3776-85b9-e20b2bf8b53a | -10.75864 | -40.47066 | 2025-10-15 03:17:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 267415c0-2d93-3d3d-bda3-d5de8de7b87a | -7.75345 | -42.4572 | 2025-10-15 03:17:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a27c0ab-4cec-3e40-962d-666804e7ff08 | -10.51565 | -43.37352 | 2025-10-15 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44ca5556-8984-35fe-9e9a-5362fbe5599f | -10.82004 | -43.95054 | 2025-10-15 03:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb2dc04-03e0-3bcf-a5c1-6d0f040d62e0 | -7.57089 | -42.69892 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 225d2b19-d533-316a-9abc-d0e2e64142c9 | -7.49932 | -42.144 | 2025-10-15 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8f724801-701f-39fa-bcf4-356dfc5cef75 | -11.44514 | -44.0935 | 2025-10-15 03:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 82f2f9db-fce3-3236-93c7-8673e0b5a164 | -10.82212 | -43.95871 | 2025-10-15 03:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 582226d2-1a45-38fb-a64a-282c42e28b90 | -7.5707 | -42.70565 | 2025-10-15 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6b967f29-d3aa-3ee7-9358-8fadf6479154 | -11.23128 | -39.23935 | 2025-10-15 03:17:00 | NOAA-21 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 979c3403-ed1f-3f02-871e-1ada84390e9f | -13.28059 | -43.42855 | 2025-10-15 03:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65cf6387-bcc8-3d12-bcdc-9bebfdb60a94 | -8.24834 | -39.458 | 2025-10-15 03:17:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0a337e6b-5fb7-3f12-badd-7f17bbfc5e63 | -10.81298 | -43.94899 | 2025-10-15 03:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223a8d17-331e-3c1c-aed3-d52a0d5854d7 | -10.51689 | -43.36757 | 2025-10-15 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ba89b2c-fd8a-3431-b9b6-b978914da2a0 | -19.66574 | -44.71249 | 2025-10-15 03:19:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 869ffef4-f8f4-3c61-911f-f2efa55f07e2 | -14.83576 | -40.98531 | 2025-10-15 03:19:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| cb8d2b08-12e7-3f2d-8e32-92bf2ed66b55 | -14.2798 | -42.3346 | 2025-10-15 03:19:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 13a33a76-d7d8-334a-af87-91473e2b2637 | -14.54556 | -41.54226 | 2025-10-15 03:19:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e6f7fb4c-8657-3360-b9a8-55844552448a | -15.4177 | -42.01603 | 2025-10-15 03:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 19ba565e-0cdb-3665-90c6-ea457b90470a | -19.66394 | -44.71044 | 2025-10-15 03:19:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b9ee9ce0-e5de-3578-88ae-0fb6856888c2 | -15.02289 | -41.35946 | 2025-10-15 03:19:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f315224a-a2e9-38c5-afdb-201646bd7a83 | -19.6594 | -44.71105 | 2025-10-15 03:19:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5d72971c-3397-3b03-866f-026f89c3b05b | -14.12343 | -42.6484 | 2025-10-15 03:19:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0fbb2ba-cfd1-3c2b-ae64-12eb58cf308d | -5.4463 | -44.2388 | 2025-10-15 03:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ff9efad6-b43e-313a-be0b-f9edb48e5c0e | -4.6509 | -43.1337 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 765b12c9-3015-35d0-b8c6-b2e58ea350a4 | -7.9439 | -44.1381 | 2025-10-15 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| dba538f5-7e0c-37a3-bbf8-093c12ff2009 | -5.4465 | -44.2159 | 2025-10-15 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 0808444f-6740-3d78-a215-24f2db1a62ea | -4.6696 | -43.1326 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |


[Clique aqui para ver as próximas entradas](README10.md)
