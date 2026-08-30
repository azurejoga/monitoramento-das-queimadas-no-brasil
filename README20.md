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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a389c8de-e9a8-3965-b7bf-31ce096ecd0d | -9.8927 | -60.2752 | 2026-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| cf1881b3-a8d7-34dc-b2d1-aa0e482dfacb | -6.8802 | -41.6513 | 2026-08-30 02:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 35f45338-491b-32a8-be04-a68a381a539c | -3.6398 | -60.5656 | 2026-08-30 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a1140622-ce84-3407-8bcb-e0d7ce5279fa | -6.8799 | -41.6754 | 2026-08-30 02:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 194.2 |
| 7e86f6dc-be60-36f4-9d12-362d859b4f36 | -9.043 | -65.4175 | 2026-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 6fc9808e-28c1-3532-b48a-cf3b1763239e | -4.9603 | -55.8622 | 2026-08-30 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d70f14be-78ad-380f-b7ab-a212bd17a400 | -4.3774 | -47.7627 | 2026-08-30 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 893b4d2a-e01e-389a-82ff-09319c010049 | -6.861 | -41.6772 | 2026-08-30 02:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 196.3 |
| 8cbae83f-96fb-3ebe-ab17-33f6dddc9186 | -10.7407 | -54.0401 | 2026-08-30 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 04f533b7-4208-3487-ad1c-5099e292985b | -3.6216 | -60.547 | 2026-08-30 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3886050d-4a00-3649-9df0-41cb4f5764cb | -4.9605 | -55.8226 | 2026-08-30 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 21919c8b-618f-395a-9be6-8351f2c1dea6 | -4.3772 | -47.7844 | 2026-08-30 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 84517da4-9629-36d3-84ad-f7cddbdf459d | -5.4876 | -57.1416 | 2026-08-30 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 982ed3e6-d081-36ab-ac6b-6f253961ad09 | -3.6399 | -60.5466 | 2026-08-30 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| f3c249bf-afc3-3947-b72c-e4453580d850 | -3.6215 | -60.566 | 2026-08-30 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3044cf79-cb4d-3009-b2dd-4d8b2454cee5 | -4.9604 | -55.8424 | 2026-08-30 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 14a26025-efd0-3a5e-bde5-7e6f24e08571 | -6.9361 | -55.7157 | 2026-08-30 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 24f428b2-ca91-336e-9fc4-af7256f416f3 | -10.8062 | -45.3178 | 2026-08-30 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e5bf3b78-c808-3a68-9a07-966f730667d8 | -4.3588 | -47.7636 | 2026-08-30 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 474e327c-ece7-3583-aa04-e09352bc117d | -4.942 | -55.8431 | 2026-08-30 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 582fb427-0900-3fad-be0f-be12b282a253 | -11.3431 | -45.1521 | 2026-08-30 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c7f906fe-d2e0-313d-b738-b138fafa26db | -4.3774 | -47.7627 | 2026-08-30 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3f286891-b617-3e06-9c18-70eced799d4b | -10.9401 | -43.0355 | 2026-08-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b16969cf-a8ef-3874-bbed-5d9b4ef420d4 | -5.4876 | -57.1416 | 2026-08-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f683a927-56a2-38b5-9023-be3eedf5cf89 | -3.6399 | -60.5466 | 2026-08-30 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 90a24e9e-7021-37b9-80bc-42d746b5bd4a | -4.3588 | -47.7636 | 2026-08-30 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8925f0da-26f8-3e5d-83c6-e0642119f204 | -4.9788 | -55.8417 | 2026-08-30 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a7d6e9fd-9a4d-3668-b18e-837a4f4161db | -4.9605 | -55.8226 | 2026-08-30 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d84403b8-8ec2-3f41-94b3-583c935a45be | -4.3772 | -47.7844 | 2026-08-30 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b989a2bf-53b2-3007-b276-e7bde26a5458 | -6.9361 | -55.7157 | 2026-08-30 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7dfb16af-e3b5-38fb-b49a-918f68ece385 | -3.6398 | -60.5656 | 2026-08-30 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a1167e89-d352-38e5-b010-bab64ff8cd0c | -9.8927 | -60.2752 | 2026-08-30 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 9e8ebdbe-ade2-3466-94e9-704c89ad37de | -4.3587 | -47.7853 | 2026-08-30 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 35d3bca0-eeb1-3ec2-84af-6c5587c2d18e | -7.5661 | -61.3239 | 2026-08-30 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f39bb16e-eac6-3700-8704-dab6b49d84d4 | -17.4246 | -42.6137 | 2026-08-30 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6ff4440c-dde0-3344-af50-9391b96ad68e | -6.861 | -41.6772 | 2026-08-30 02:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 34505db9-6f11-3393-8a7e-b5f7ead17b93 | -6.8799 | -41.6754 | 2026-08-30 02:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 2d709a9b-6a67-3235-8446-9597319d3687 | -5.8894 | -57.7708 | 2026-08-30 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e5ce7663-ea02-3f31-832c-3ccce7cb45a8 | -4.9603 | -55.8622 | 2026-08-30 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| da1b63df-8332-3890-9c8f-e792c9abee9b | -7.3117 | -60.6089 | 2026-08-30 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c0610d98-4e0f-300c-bd81-34d0af6b6f3f | -9.0615 | -65.4169 | 2026-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a6d85a29-d1a8-3ae7-9969-e4c3414e7b33 | -10.9593 | -43.0326 | 2026-08-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| f9c8d164-acd8-3c81-b3ef-7aae3753e85b | -10.9597 | -43.0088 | 2026-08-30 02:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 837cc315-263b-3759-8ed5-01223997f437 | -4.9604 | -55.8424 | 2026-08-30 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 32b83c73-fe7b-3fcc-98e5-443c020feb6f | -7.4952 | -55.3062 | 2026-08-30 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c3a8dcb3-aa73-3030-8eac-3ba2f8f9b2bb | -6.84 | -41.67 | 2026-08-30 02:15:00 | MSG-03 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ce1e780-a802-3438-a31e-b07d39ad4233 | -6.87 | -41.67 | 2026-08-30 02:15:00 | MSG-03 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a266447c-0e9c-31cc-8891-c3353f045762 | -10.9405 | -43.0117 | 2026-08-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| e9adeae6-a31c-3ce3-9ca1-7ff11647dcc8 | -4.9605 | -55.8226 | 2026-08-30 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d8bccf8a-acbe-362f-aaab-22a1f235c808 | -4.9788 | -55.8417 | 2026-08-30 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0568bcb8-826a-36d3-be67-e7d78ffbdc67 | -10.9401 | -43.0355 | 2026-08-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 42d8e50f-1392-337a-a9bf-28fddf7773d1 | -6.9361 | -55.7157 | 2026-08-30 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c06b2219-6dc5-31b3-9d7b-af9d42124af5 | -4.942 | -55.8431 | 2026-08-30 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 21511d83-3d0b-36bc-975b-453e212286ec | -3.6398 | -60.5656 | 2026-08-30 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2e9cde5e-db03-362e-bd29-a62e0c78c424 | -6.861 | -41.6772 | 2026-08-30 02:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| b7e95f50-d2cc-30bd-b147-ae0a1b20a06d | -7.4952 | -55.3062 | 2026-08-30 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fa0ee724-658c-3d75-9ea6-dddf161c10ec | -4.9603 | -55.8622 | 2026-08-30 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 4df06e94-c858-3023-9f36-d769383e26dd | -4.3774 | -47.7627 | 2026-08-30 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 201b6264-dda3-3ac6-a2f6-a4996440fcff | -7.3117 | -60.6089 | 2026-08-30 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4db53f8b-7ab6-30dc-a36e-79d4eff301c0 | -10.9593 | -43.0326 | 2026-08-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| fa511bfb-7b34-3716-b594-d9999e56a308 | -4.3588 | -47.7636 | 2026-08-30 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0b33007d-93da-305b-b6f5-517432ced90f | -4.3587 | -47.7853 | 2026-08-30 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8448da70-5e41-3b7f-9b90-cbe39f63ab2a | -4.3772 | -47.7844 | 2026-08-30 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 45485379-d3ca-3ad8-a45e-8c9e68d489cd | -5.4875 | -57.1611 | 2026-08-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b41591d7-7a1a-36ed-8daf-ee996289df21 | -17.4246 | -42.6137 | 2026-08-30 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9f04b106-4558-3cfc-be92-f48221a80ba9 | -9.0615 | -65.4169 | 2026-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a079d97a-b951-30f5-8ec4-d646e27f23ce | -5.4876 | -57.1416 | 2026-08-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 3d9cf8e7-e133-3e86-8edc-01dd1beca78f | -5.8894 | -57.7708 | 2026-08-30 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5fa363aa-9a38-3040-a085-0bbeb0691cc1 | -9.8927 | -60.2752 | 2026-08-30 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 6345bc9b-29a1-3a57-ae44-d4dc496f6785 | -10.9597 | -43.0088 | 2026-08-30 02:20:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b96023a8-bf6d-3dc8-97d9-655462c2d3ca | -11.3431 | -45.1521 | 2026-08-30 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b49e24cf-80e1-36a3-ac56-e9abf702534b | -4.9604 | -55.8424 | 2026-08-30 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 222.9 |
| 44ef9d55-fc13-3d40-99ef-54ddf394c89d | -10.7407 | -54.0401 | 2026-08-30 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 26a6ab98-c617-31ca-8c48-bf2cb774323e | -5.871 | -57.7715 | 2026-08-30 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a4944821-bbe3-3574-9b2b-dff303f55b35 | -4.3772 | -47.7844 | 2026-08-30 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 7cb4d441-a593-3149-8715-c74eaea6fcba | -5.4876 | -57.1416 | 2026-08-30 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b2a890cd-fe6b-333c-ad82-662dbaba41dc | -11.3431 | -45.1521 | 2026-08-30 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8ad0f1cc-4e68-3533-a887-18249464a8d6 | -4.9788 | -55.8417 | 2026-08-30 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ab644a7c-88a2-3244-89d2-08278ee9733a | -10.9593 | -43.0326 | 2026-08-30 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 401a6479-6302-3516-8b4b-c654d6d95236 | -9.0615 | -65.4169 | 2026-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6ad9af34-bb41-3e0d-854f-0297be1ffc30 | -7.5661 | -61.3239 | 2026-08-30 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b5c65aa2-8a63-39fa-aecd-80e9d3f4230f | -7.3117 | -60.6089 | 2026-08-30 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c3410194-5495-37b8-84e0-821d79a4da52 | -3.6398 | -60.5656 | 2026-08-30 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 31b00a3b-cf65-30b4-ae4a-64540d27d00f | -5.4875 | -57.1611 | 2026-08-30 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| efbb89b5-e918-30dd-8b11-319eae097603 | -5.8894 | -57.7708 | 2026-08-30 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| acf0c51e-532c-39ec-b5ed-0e10e29fb886 | -10.9405 | -43.0117 | 2026-08-30 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| d9cb74cf-fbc3-3da5-b252-8fa47fe896fd | -4.9603 | -55.8622 | 2026-08-30 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0513eda6-2eb3-3541-b6d5-086e98c4ba71 | -6.9361 | -55.7157 | 2026-08-30 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 781a234e-1629-3f7c-a110-563b2153af3d | -4.9604 | -55.8424 | 2026-08-30 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 3bf1382e-ca25-3de9-918d-d9465dd4e891 | -4.3587 | -47.7853 | 2026-08-30 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d4b0fa69-d898-340d-b6cf-e86e4b8a9f72 | -10.7407 | -54.0401 | 2026-08-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0c624edc-6ddc-3d8e-be43-d664a4b60ea6 | -4.3774 | -47.7627 | 2026-08-30 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c4082889-bf4f-3adf-83e6-43abc4f4192c | -10.9401 | -43.0355 | 2026-08-30 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 73cb55fe-4d16-36ea-bc3b-5ed16817bb4b | -4.3588 | -47.7636 | 2026-08-30 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8bf957d1-86f5-3f27-b771-85effd30540e | -9.8927 | -60.2752 | 2026-08-30 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fa6e9005-7408-3865-8613-c76c4b92a443 | -10.9597 | -43.0088 | 2026-08-30 02:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| e7eadb6c-42f4-3abc-bbe9-96d42b959961 | -10.7649 | -50.6366 | 2026-08-30 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 13f21656-387d-3356-bfea-12b140497ebf | -4.9788 | -55.8417 | 2026-08-30 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4fba18b7-e27f-3788-8522-157f4a933172 | -4.9603 | -55.8622 | 2026-08-30 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1bc1b2c5-d40e-3f49-9453-7fe91cde53d7 | -4.3772 | -47.7844 | 2026-08-30 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |


[Clique aqui para ver as próximas entradas](README21.md)
