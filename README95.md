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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04ca3405-acc3-3b67-b431-41015a24f694 | -8.0866 | -44.791 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| beb6d073-bd69-374e-8d56-a690c5c18463 | -8.6253 | -43.9952 | 2025-10-06 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8c455e35-65ac-36c7-8dd2-b2dc5ce65f0b | -7.2723 | -45.2792 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a1659945-3959-3088-b807-cd1c8a3c2311 | -7.7885 | -44.5228 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 13541471-3d3b-3b2b-99c0-0cd8e2f63570 | -6.6303 | -45.7178 | 2025-10-06 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9a2384ee-d5ef-355d-b929-7257a4f1a370 | -6.5989 | -45.1101 | 2025-10-06 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2ddfd8fa-5ac7-3639-b88c-3014f6478bc3 | -14.8634 | -51.4804 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 6e9de634-3078-34a0-b724-a245d273ec5c | -6.6503 | -41.9853 | 2025-10-06 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 6af064ba-9fb3-37ef-8625-94c29c448431 | -10.1393 | -45.4039 | 2025-10-06 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 62e00472-c259-3377-9d47-ff632bb5e79f | -7.5969 | -44.8165 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9157f05a-75e8-3260-9297-9cb3f7520f05 | -15.3545 | -56.9287 | 2025-10-06 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6b13c653-dcd2-3579-af70-e11fd2b2a8b6 | -7.8262 | -44.519 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7cc813a3-23d2-3f68-a07c-d8422efeeaea | -7.2094 | -45.8942 | 2025-10-06 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ee9eddc9-67e3-391f-bb43-6efc45993b84 | -12.5733 | -48.1393 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 29bf04d5-57c4-3d73-8dfe-775445e0aa74 | -13.0377 | -47.9183 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bb78a8bf-cc94-372c-b694-b49f7dbfc6d4 | -13.6389 | -48.7178 | 2025-10-06 14:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| d1598c54-f66b-35a0-9674-41f769edb422 | -7.6993 | -42.5708 | 2025-10-06 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 9e142733-fed0-3eef-8a19-563a410124de | -7.4276 | -46.5239 | 2025-10-06 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c358d60f-4f5e-3a63-b5e9-27240aed0c78 | -9.9024 | -50.1914 | 2025-10-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 935375d0-e7be-3e96-b2db-8e4402f93418 | -17.3816 | -53.5947 | 2025-10-06 14:20:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 883068dd-31fb-392c-8e39-994ea43ec59c | -20.1001 | -44.1921 | 2025-10-06 14:20:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| 24d4508e-76ab-3300-b7d1-1910f9b94360 | -15.9838 | -50.8614 | 2025-10-06 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 46c396f5-cf3a-3bd0-93f9-67e8e37236eb | -7.3101 | -45.2531 | 2025-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 47c48435-6cd0-3656-b665-29d302421146 | -11.9327 | -46.438 | 2025-10-06 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ade4a0dd-2e8d-33e4-9c8b-b688eef11563 | -11.0697 | -47.9147 | 2025-10-06 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2724e03f-ab13-3c0f-88e1-f005d8f46047 | -7.0558 | -42.7782 | 2025-10-06 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| cda53ce5-e09a-37a1-ae8a-4c0f9ead0e55 | -7.6648 | -45.4471 | 2025-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 630c9730-26db-32aa-8b64-9483c90b2e52 | -11.1181 | -47.243 | 2025-10-06 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 85dc1572-021c-3770-954c-10662934b531 | -10.391 | -50.3344 | 2025-10-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| ceaf9f29-050b-360d-a238-cc498f39b2db | -13.0033 | -51.0624 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 438def44-fc42-3223-93c7-ba245eb18a33 | -9.6801 | -48.4232 | 2025-10-06 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 0ea611cc-fb04-3b3a-a9b6-750b6b63da59 | -9.3162 | -46.0005 | 2025-10-06 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 2326e912-d385-335f-bbed-57db101d252a | -12.5929 | -48.1144 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7448b582-8669-3617-9125-e301dea9522d | -6.8388 | -45.4753 | 2025-10-06 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| db7fc0f4-b76f-3526-b5d6-a4215e83e9cf | -6.523 | -45.207 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5d2f3f5f-6be2-3497-b3ca-50c5d8cfa593 | -6.7818 | -45.5477 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a911b105-1d9f-3af9-93ae-29d772a66947 | -6.0616 | -42.537 | 2025-10-06 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| a27f82c4-d2d3-3766-92da-3215489f38df | -12.1458 | -50.9523 | 2025-10-06 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 19a9209a-0af5-3298-b9e2-e40ef1fe9a59 | -8.5193 | -46.3547 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e9b425da-13f7-3d92-85c9-28aeb963ef4f | -6.2179 | -45.7947 | 2025-10-06 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d2ce2734-4c51-3016-a9b3-f40cf1a37aca | -12.3726 | -51.0749 | 2025-10-06 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 37491ba8-dab0-3400-9990-06fc3a863d29 | -13.0759 | -47.9351 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f1a452f3-de09-340b-951c-da14f0e2a896 | -6.7707 | -44.7998 | 2025-10-06 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2ab471aa-1124-3005-82aa-40e4f9ed7e97 | -7.2723 | -45.2792 | 2025-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d2f76843-4e34-3d02-90b1-86124413c01c | -12.9841 | -51.0648 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 221.4 |
| da94ac88-9754-3181-8531-9e627db8969b | -8.6835 | -49.9419 | 2025-10-06 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ff16e800-cc58-3ec8-8c2c-84cf36c320bb | -7.0369 | -42.78 | 2025-10-06 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 68701b4e-d023-3e44-ae41-8e1ba0bde3ae | -10.8597 | -47.9842 | 2025-10-06 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 1d9a3778-30ad-3746-8a96-83fe8bdf086a | -8.539 | -46.2855 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ebac7cce-19bf-363f-b189-ca39f1804486 | -11.655 | -47.039 | 2025-10-06 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1729fc3f-67ac-3255-a5d9-09c04d1bb0c5 | -8.1702 | -44.1377 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9991a61f-600c-3661-b670-c2580d60dfa7 | -11.7908 | -48.0669 | 2025-10-06 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8e588994-cbf4-3942-a44d-e87577f0d368 | -6.6567 | -44.9462 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 74f3804b-297e-3798-b9a2-5e35d0902e8b | -12.5538 | -48.1641 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6b728f34-3227-3bf7-94eb-56f33cfa2dde | -12.184 | -50.9478 | 2025-10-06 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 9ea5f5eb-cf00-35c0-adad-e94580204c89 | -6.7705 | -44.8227 | 2025-10-06 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3b834e53-197f-3f5d-97ca-80649786d89f | -6.7821 | -45.5251 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 6b603701-dc91-3fe9-a675-6c68cc39c535 | -11.8038 | -45.0624 | 2025-10-06 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d2cf61fd-11c2-37e6-9218-90768ac610da | -6.3586 | -42.8892 | 2025-10-06 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 7121ee39-36e2-3ae0-a5b7-dd6abe7c9e88 | -8.2664 | -47.0474 | 2025-10-06 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5cfaf955-2dc9-3c4a-b3fc-0348e35ffcd6 | -19.5986 | -44.639 | 2025-10-06 14:20:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d4c40bd9-80fb-317a-adbe-afaf93cf0bdf | -12.9653 | -51.0457 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c15c40fa-0bc8-3332-9824-75223f14ebfd | -14.882 | -51.5207 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 3ccfe439-2dfb-3ad0-9d7a-07597705f177 | -8.5576 | -46.306 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d0b01a87-2ce2-3049-b341-028d3a516c4f | -15.5699 | -47.2854 | 2025-10-06 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4653847b-caf8-3294-b555-85bdee25e86d | -6.5989 | -45.1101 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0fbd088a-547c-3172-ba04-d5845c3c2685 | -6.6758 | -41.3819 | 2025-10-06 14:20:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 270b6475-7dce-33b8-a131-7e0afd730dcc | -7.8265 | -44.496 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b41d0d82-78c5-344a-ae2f-37ad41c4f327 | -7.2964 | -44.799 | 2025-10-06 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 95358c50-8355-3cdb-9ba9-05b4f39acb20 | -10.3864 | -45.3955 | 2025-10-06 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a7e9c903-4ad5-337c-8cb6-da3b97fc9cd6 | -13.0763 | -47.9127 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| eae538b0-0fbe-3949-977b-6bc4009b9e07 | -7.7179 | -42.5926 | 2025-10-06 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 09709b6e-ce87-335a-b51f-73227370939c | -12.3914 | -51.094 | 2025-10-06 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| ae314c51-a32e-3d69-8131-fbe186a0f1bc | -7.6272 | -45.4507 | 2025-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| bf920214-943f-3544-a927-68772b4530fc | -10.386 | -45.4184 | 2025-10-06 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 83e7c616-b392-3902-9491-5e0efb7fac09 | -16.0038 | -50.8365 | 2025-10-06 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 323682b6-a9e8-374c-9ee2-ac736c62e09f | -10.3247 | -46.9612 | 2025-10-06 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c143bbda-1cde-398d-a087-656c8fb8a4b2 | -13.0574 | -47.8932 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| ed4d0045-e47b-397c-b130-318487899880 | -12.4665 | -45.5386 | 2025-10-06 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7ec982fd-a279-3f76-9c07-b10138fb5d36 | -10.86 | -47.9621 | 2025-10-06 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 781f1f5c-f477-3221-abb5-d589d3fa74bc | -13.057 | -47.9155 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 18c6e8db-b8f2-3bcd-abce-5308a0ad7dc3 | -16.0083 | -56.0155 | 2025-10-06 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| d5505dce-edbc-36cc-b2b0-514f0fd57676 | -7.2662 | -44.1356 | 2025-10-06 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 593f728c-6ef7-3688-8464-c13d8e8cf0d8 | -7.0604 | -45.7946 | 2025-10-06 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5b0e16f2-daf3-3127-a455-8174ce1989f2 | -12.4468 | -45.5646 | 2025-10-06 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 0f3dfe43-b4b2-3b53-9d44-ea22d981fb38 | -14.5438 | -46.9633 | 2025-10-06 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 24410d21-9603-3c34-9d47-07271d9721ed | -11.1185 | -47.2207 | 2025-10-06 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9b408677-cb75-3314-8c29-549b82274d4f | -6.5799 | -45.1344 | 2025-10-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| df3f08e7-1ad1-30df-aaee-89fdfd32ae00 | -11.2056 | -45.378 | 2025-10-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f5178ff9-bf28-359d-b2f8-23d71c795fd3 | -9.6614 | -45.6667 | 2025-10-06 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0ef5de6e-43a4-3a65-b84e-eab45326568c | -7.7885 | -44.5228 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5132a376-c0ac-3059-95ef-c83ac0fdf8b8 | -11.8033 | -45.0856 | 2025-10-06 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f1aea8ac-5653-3eb6-86c8-0bcf104e5307 | -10.4099 | -50.3324 | 2025-10-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 56ddccf9-28c0-35cc-9f9b-60aa77025f8f | -14.8637 | -51.4589 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e2705c56-e53b-3426-a3fd-1e8e33a692b8 | -7.2776 | -44.8007 | 2025-10-06 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 67a41628-229a-308c-bfc7-36c0e6bc7e50 | -8.2074 | -44.18 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 74673c33-4329-3d6d-96d7-a8bc0bf83a81 | -14.5433 | -46.9861 | 2025-10-06 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 3f642e4f-271c-3d80-ba60-b581221b9441 | -14.6321 | -52.535 | 2025-10-06 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4e347999-a049-3aa2-b6cf-e930ec4c809e | -15.9842 | -50.8395 | 2025-10-06 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d2cdb17a-e260-3002-85f3-6de078099317 | -7.7743 | -42.6103 | 2025-10-06 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |


[Clique aqui para ver as próximas entradas](README96.md)
