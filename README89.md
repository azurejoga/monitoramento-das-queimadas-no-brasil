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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a444b860-449a-376a-b0e6-726629daea8d | -2.43925 | -58.01783 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b7a47f9-f509-3456-a181-1a763e1b0389 | -3.9395 | -40.73231 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6c8c8fd4-aea3-3ed7-98e4-f144b7a86041 | -3.29911 | -43.94896 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 879aa614-c7ed-33d3-ab7f-8479c9792dff | -3.2856 | -60.11403 | 2026-10-05 16:39:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b89de369-dde2-32a2-80dd-b74bfa166309 | -3.11746 | -40.1645 | 2026-10-05 16:39:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 22.2 |
| d2f7cabe-b0da-3030-88bc-115fdad48372 | -2.63409 | -49.30611 | 2026-10-05 16:39:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 943861eb-ff35-32f8-af92-1f1e8b2f21ba | -6.04315 | -45.22988 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f4ab2a12-46bb-31d8-9e58-ceec5d92a333 | -4.05409 | -59.36758 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 675df183-0faa-378f-a5c7-068ae28667f4 | -2.98468 | -54.03241 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 378f2ee2-c229-3911-b3d9-fed04943a001 | -3.49908 | -54.62637 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| fedc970b-9465-3c1e-a900-dd8e9c04c204 | -1.45686 | -55.27023 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ce13f5a1-f974-302f-8785-f4fb9c543ce7 | -0.12613 | -51.56802 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56e98542-4bc6-3c64-8034-c740cdd28956 | -4.91177 | -41.73708 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 27a4721d-8c92-345e-ada1-d95c5d4bda40 | -4.95748 | -40.55916 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 7fe56d30-1622-3a06-a210-43cd6d98c5dc | -3.28296 | -54.17543 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 27eab148-c86c-3f59-b724-9efbd1c1fec8 | -2.89792 | -54.1198 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e1be6694-ff23-31f0-858f-94a57edd4260 | -3.20974 | -42.44532 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6065fa01-b64f-339c-bf03-387069ba4951 | -3.17042 | -41.40241 | 2026-10-05 16:39:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 18db22af-7ba7-3a61-b335-06f943b4c3d4 | -4.82598 | -43.38343 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9297ac22-bf03-3987-b4c7-c91a94d4eb83 | -2.89472 | -42.39863 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a51028a5-767e-31af-a3e4-de5dbec662d9 | -4.84227 | -41.81155 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| d139f3fd-2503-355c-b9a2-439266d42665 | -2.06657 | -48.21242 | 2026-10-05 16:39:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8083fb45-bd00-318e-b61b-27ec5d1a71a7 | -1.09482 | -54.11035 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c54d9480-99cf-3e42-a918-b2b62f644ea4 | -6.70698 | -55.21613 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3bf5658-ebba-3711-88e3-bec885df9ab8 | -4.34132 | -44.37434 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d2dfeb72-bacb-3f4a-a54f-8515382cebe0 | -4.28861 | -38.61961 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRA | CEARÁ | Brasil | 2301950 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 314aad4f-c064-3f90-9302-891ca4347b88 | -1.56683 | -50.47623 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 63e191ad-7377-3f12-bcf3-9046480ef829 | -1.33824 | -50.47743 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1f4b832a-24b4-37d8-8102-26b707f69525 | -4.46835 | -54.97422 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 04147207-09e2-3111-bec7-c03032dc4cad | -5.48184 | -39.56525 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1b3e88b0-7ccd-3bb8-9239-969cf321d57d | -3.95662 | -41.55343 | 2026-10-05 16:39:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 0abfe540-343c-321e-9660-19eecd6293bf | -1.63037 | -53.65655 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63603488-c5a2-3175-9d7d-e31fef6642a4 | -5.95556 | -41.35462 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.7 |
| 59bcce13-566e-3d61-bdf7-670944c314d8 | -3.54411 | -60.51876 | 2026-10-05 16:39:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 02006e3d-f093-349e-afb5-4c94e5fc18a8 | -3.79631 | -59.31957 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5f28af1-e4d8-387e-8d68-501626d877c1 | -3.48612 | -59.72606 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1800fea8-34a8-3346-ad8c-938f48d742c4 | -5.62894 | -41.29034 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| a7638f05-d921-30b0-a152-d036380596cc | -2.02311 | -56.88961 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f87e8f8f-cab2-3fa8-8f85-e1612ece816c | -7.21171 | -55.19135 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a6007811-1d6b-37e3-b0a4-b5c7b7c16710 | -3.10329 | -41.83353 | 2026-10-05 16:39:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8e4fecd9-c947-317a-a4ef-f8a79f647797 | -3.2107 | -39.91864 | 2026-10-05 16:39:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 90d4ea7a-4ab3-3cc9-88af-e3ec029ce424 | -2.58394 | -44.97037 | 2026-10-05 16:39:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3c02f46b-e841-322e-a4ed-6a356484b7c8 | -3.49045 | -59.72383 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c98a6932-d38c-324b-9277-9fc65932e263 | -3.57035 | -43.89136 | 2026-10-05 16:39:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ec5c719-6d48-3759-a089-70683ca29e02 | -2.77692 | -57.66343 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f1a77d76-d79a-3d8e-ad77-46b7e71091d5 | -3.05513 | -54.21543 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4a480dfd-4f05-31de-ae69-07d9f3606605 | -3.76972 | -58.92631 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b4f6fdf-68f2-3795-8237-9c476c8172f6 | -5.98753 | -53.63414 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d0fe6752-e3d0-357a-9875-2cdac2f535a6 | -4.89883 | -45.6775 | 2026-10-05 16:39:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ecdf9317-59ee-3f4b-99ef-cc334f34a09a | -6.32864 | -43.81373 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 404d5d95-c56c-358b-b9db-e96b2e1bd458 | -4.38174 | -43.92422 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ea839d6-c8dd-3da6-860d-87b57b2039bf | -5.74265 | -41.621 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 050b8a51-3082-3bdc-965b-845ddd93f5df | -2.83831 | -54.06878 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19af19a2-2df1-3332-959d-abae20a6be1e | -2.6625 | -57.28609 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d69fba67-ecdc-3dd1-a218-37293a8d882e | -1.08772 | -54.11897 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2848454d-b577-391f-931a-ba37348256a2 | -1.66195 | -47.6297 | 2026-10-05 16:39:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d97d8379-3ee0-3f09-aefd-1ce4562f44e0 | -3.96108 | -41.55268 | 2026-10-05 16:39:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 899daf8e-fcba-3b85-9bf9-7b2c32a63353 | -4.3671 | -55.42477 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c7ca921a-3b7f-33c0-80a0-30b643ba41e5 | -1.9162 | -48.60917 | 2026-10-05 16:39:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 83cec478-1537-3c44-9036-b30134b64796 | -5.94027 | -41.34382 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ffbe5edb-09c4-36bc-8c8b-fe3c107c7cb7 | -1.32716 | -55.27916 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f6a073d-bc23-32c0-92b5-9df641efcf11 | -4.56674 | -46.5851 | 2026-10-05 16:39:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 80f1b7f7-6baf-3194-934f-defe038a4e19 | -4.79089 | -42.57562 | 2026-10-05 16:39:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d8745e20-0053-3628-9982-a0069ee6d2f0 | -1.22076 | -47.72367 | 2026-10-05 16:39:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4aefe164-7277-3e24-91ef-0069014ab10f | -1.88158 | -45.07874 | 2026-10-05 16:39:00 | NOAA-21 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| feb4c899-9b29-3512-a50a-ef0cabee8cc3 | -0.33399 | -52.02831 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec96375c-fafd-3cf2-8f21-2066e5159a07 | -2.75644 | -51.55547 | 2026-10-05 16:39:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53c52c49-0e40-3abb-ba26-7a7c2bc596bc | -3.93865 | -40.72725 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 4ffe460f-da0c-3707-9442-1b8c0e24352c | -4.35166 | -40.2551 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c6dc77b6-adec-3861-bb47-b6928b946e2e | -2.23744 | -49.51374 | 2026-10-05 16:39:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c201d34-a6b9-3416-a37f-248e924986e1 | -3.99045 | -55.8215 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 261ead80-17b1-36cf-8a5e-c6a330b008b0 | -1.79935 | -45.2742 | 2026-10-05 16:39:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e3cb0ad4-07f6-3e6b-9ada-72db5de11a26 | -4.39298 | -59.55575 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e50cf521-290c-36e5-956d-9c0ecaf21e35 | -5.73308 | -45.05349 | 2026-10-05 16:39:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0236847a-6658-3bc6-894b-3dd04daf8427 | -5.94097 | -41.34806 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 070aa140-1d5a-34cd-babc-001eae810a11 | -3.27211 | -41.84335 | 2026-10-05 16:39:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e4c14031-f9e4-3714-a9c9-2d8051e4b4cd | -2.96165 | -42.90641 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| ebca9a82-3fdf-31bf-af30-1dc9b50d2ec4 | -3.5054 | -54.60772 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f66c2d54-ba38-30b5-bde8-79a5d60bd78e | -1.36501 | -47.44524 | 2026-10-05 16:39:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8b96347c-66bd-31e7-8e5e-fdac27cf628c | -4.33094 | -43.81984 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3a70c2ab-4f01-37e3-8706-3146610b673a | -5.84862 | -53.82019 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 474d9890-242b-3b3a-b7e9-5854affc1311 | -1.48937 | -55.67405 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| b40cf4e3-e720-326c-b792-3f4f74f1df34 | -1.45007 | -47.66672 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aebd0f31-245f-3025-a1af-bd473067cd3e | -3.29987 | -53.85325 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c8be9436-61dc-38de-bbc2-0a86e7c29834 | -3.65429 | -39.67234 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1fb682bf-ac3c-3214-b5c1-136db0c8eb4f | -4.17422 | -44.30667 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ad9a9a9a-8de0-3969-a42b-f1a28c42e95f | -5.3017 | -43.21563 | 2026-10-05 16:39:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ea3ab735-323b-309d-b489-aa42ca6288de | -1.68609 | -45.14659 | 2026-10-05 16:39:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d9fd590-f2f3-3351-97a9-c86b3599e826 | -4.20858 | -53.46861 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 31af4fec-1ef2-36da-aa08-5bc517ab038d | -3.21072 | -42.87867 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 25f6a6b5-db3f-35ea-ae18-5b3eda612e3a | -3.77003 | -39.84919 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1b2ac2c9-2dfb-34cb-9291-b1e8d92783a7 | -1.87277 | -50.04454 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dfc7a91e-4b86-33a0-9e99-d5bc535e42c6 | -3.20791 | -56.83035 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a7f58b3b-a8d7-3319-b13c-a972194c6fcd | -6.17726 | -55.35144 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 21ab87b5-e244-3e7b-b42a-629b935c964a | -2.93299 | -54.12287 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a909214d-f8ae-32e8-b9b0-bbc2f7ac0ecc | -4.53538 | -43.52835 | 2026-10-05 16:39:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0a0a24ed-1d7b-3da0-826d-6768c9bae65a | -4.89082 | -43.46395 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8ec00c47-5f25-39c5-9876-3dd3eeb53285 | -3.64703 | -55.25739 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1e8a2966-87b0-32e8-8981-243a61ed6522 | -3.17794 | -45.28957 | 2026-10-05 16:39:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a245462-0b33-3d27-a89f-278cb5d5bb42 | -3.20486 | -42.44204 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |


[Clique aqui para ver as próximas entradas](README90.md)
