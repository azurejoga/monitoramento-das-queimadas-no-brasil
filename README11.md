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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76448745-575b-3fa3-9f1d-93b2ef421c4e | -5.03962 | -43.60332 | 2025-11-17 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 82af80bd-6303-380d-bafd-7d6d3947b1f5 | -5.33448 | -43.03656 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97d85f24-5f1c-35ee-9ec9-6041b18726d3 | -6.57884 | -35.12585 | 2025-11-17 03:25:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d8ea7085-671d-3b22-8a55-2f1cbb654adb | -3.34927 | -43.49611 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6ff29260-170f-3d90-95be-7be032442e41 | -5.46933 | -40.96936 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e0aacde-74d0-3344-9d2e-7ce4332c4730 | -3.59395 | -43.60079 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4592d46a-908e-39da-9ddd-723ecfa949b8 | -3.96667 | -38.46743 | 2025-11-17 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd784eaa-57d3-39db-acb5-c85f71da164c | -5.472 | -40.96885 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7749bad4-5c33-360c-84a9-ca9a71356330 | -5.47281 | -40.96441 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42887586-85c0-3350-8099-c9b3544f6bff | -5.46252 | -40.97329 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 371d5d2f-3480-3739-b2d5-781242f8e6e0 | -7.26875 | -34.87595 | 2025-11-17 03:25:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 841f4440-e49a-32d8-b558-de39fa4f4668 | -5.33561 | -43.03042 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4bc9415e-83a5-3c10-8d16-efb9201b9e47 | -3.97182 | -38.46835 | 2025-11-17 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cfb8a0e5-3434-352a-83d6-730609abfcb8 | -5.4169 | -41.02347 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8910b446-c960-3743-9b6c-05e867bdbdab | -11.40768 | -43.33593 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 92aa53f3-ae2d-3deb-b240-e834d299d5b6 | -7.7032 | -42.94672 | 2025-11-17 03:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b20785d0-bf60-3eb0-829f-6ac8de7cee68 | -9.73754 | -43.96775 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99b992c3-3975-3d67-8bd8-e64a23d352a0 | -6.77385 | -41.45181 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 893aff9d-c222-380c-b29e-8fb0101c1d42 | -8.68683 | -39.69652 | 2025-11-17 03:27:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6fcaea44-60ff-3a61-9206-1eab0ab41c85 | -9.71776 | -43.96305 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 45b6af14-b7f9-37ea-a161-68c96edff067 | -8.11855 | -43.52951 | 2025-11-17 03:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21a55be0-d5bc-3b32-8457-ab7fde7d82c1 | -8.28144 | -41.43131 | 2025-11-17 03:27:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 148368e0-4759-3955-9cc3-d885afc5df58 | -12.88716 | -46.46537 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd428239-8ffc-3249-9959-e00333601bfd | -9.72555 | -43.97752 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b3ac25f4-4f93-314f-b391-7ad576ddf057 | -5.88162 | -43.97923 | 2025-11-17 03:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cc3508e-cb5a-34e6-b23c-7c8b63393de1 | -7.08879 | -42.73762 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eb6fc9b0-4e3a-333b-88ba-d86735b2ddf5 | -5.88869 | -43.98049 | 2025-11-17 03:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1792976e-4389-3e37-a572-7924b64cc80f | -12.3198 | -44.2224 | 2025-11-17 03:27:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24df17b9-1a4a-3c12-bc30-903f9414bb52 | -6.68691 | -42.04462 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| a2cab431-d0fa-34c0-9e05-cbd0b8fdc26b | -9.73329 | -43.9734 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9bc7335-3a8e-329c-83b0-1d6ccc49a04c | -7.61879 | -42.57637 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdc19ffc-f872-3470-b4be-168554f83be2 | -9.72124 | -43.96464 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 96de5b90-c926-3e08-8204-c43afa2510de | -10.96512 | -44.53505 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ecd128b-5d92-3d8b-9a68-2ad2f29f2462 | -6.89425 | -38.87757 | 2025-11-17 03:27:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6651efc-8305-3d3a-a7f3-11c2b5fefb17 | -6.68157 | -42.03853 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e2c817ab-ded8-3d83-9e90-abfa2c990983 | -12.86503 | -46.04004 | 2025-11-17 03:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba85a052-5dcf-35e1-8d59-c56016dafbec | -6.67866 | -42.04225 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b8498038-78bf-3b4e-b576-195852b4973e | -12.87778 | -46.04956 | 2025-11-17 03:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bc26681-b503-3152-8c50-c65eb65c038f | -8.11423 | -43.53349 | 2025-11-17 03:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c5086a6-e934-3011-863b-44f3e5ba3e27 | -6.68069 | -42.04343 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 76106c7d-925c-3005-9617-7880cd170f7c | -8.28227 | -41.43311 | 2025-11-17 03:27:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1b6529d0-25ee-34df-8a87-9b58ca811432 | -12.43081 | -43.17813 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aad0773c-ba44-3109-9d6a-f3f9f900b550 | -6.77148 | -41.44241 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 814991a2-3094-3753-9e3e-50ebd450d5a5 | -12.41274 | -43.17401 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afec60ad-67c4-353f-8d94-734d81ac5315 | -12.84649 | -46.47339 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcce7630-a827-33d7-b3d1-7728e48be96b | -8.28067 | -41.43536 | 2025-11-17 03:27:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 080383da-adcd-3ea4-8cdc-7620674dd363 | -11.68306 | -44.72888 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5072e7cc-8185-3881-a462-aec48bdcd189 | -8.12189 | -43.52937 | 2025-11-17 03:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da97d98a-1566-33b6-a8db-a6b3a2a7939e | -6.92582 | -41.83039 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5d74c77a-3510-3fc5-a9d5-a42c2ea16080 | -11.78992 | -44.6519 | 2025-11-17 03:27:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac2edcc-32ef-3cc2-a4d0-d36ac3f1378b | -6.89272 | -38.88634 | 2025-11-17 03:27:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a36c0759-c627-3b9d-98ce-bdb0442f4608 | -11.96139 | -44.30463 | 2025-11-17 03:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c795ca8d-da90-33c7-875c-a1d057b46b1c | -11.9588 | -44.94178 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcb5374f-6e12-3fab-9a86-8ba754b96b73 | -6.71775 | -42.93627 | 2025-11-17 03:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ba6353b3-9383-3aa4-a870-0c3ecec4de11 | -6.92565 | -41.83293 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bba0a083-ae2c-31d1-bcfe-00637b0f3b74 | -6.77071 | -41.44657 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cb50781-3c36-38ed-b1fe-683cd7efde0c | -10.78583 | -44.3288 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03ffff86-4d71-39b2-bbf8-b310e12f36d9 | -6.69018 | -42.04948 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 0d8161b0-5e25-377d-8505-84befb0e6dee | -6.67444 | -42.04246 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 82edc44d-977b-36d3-bb9a-57c9faa23677 | -12.42479 | -43.17673 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 833b91fc-1fa9-3109-94ab-3e5f7c81ca55 | -12.40574 | -43.17746 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecfa209d-2bbe-3644-bfb8-03c7aaf4ddf6 | -6.93169 | -39.61274 | 2025-11-17 03:27:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d6b6cdf-ab20-3af7-b91d-c1d4b1d1b008 | -9.73641 | -43.97353 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51c43ed3-5939-323c-951f-cba3210ce8df | -8.3634 | -40.967 | 2025-11-17 03:27:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a177efdf-ef6a-3943-b0c6-c760c70cc2f9 | -6.67956 | -42.03737 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d68c0d67-7dfa-3ef2-81e5-b90a60803847 | -11.95769 | -44.94699 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa30f686-93be-3512-be5d-e412f5cb20f0 | -10.81863 | -44.31753 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b70ffba5-2610-31bb-aed3-4370fa875337 | -6.67678 | -42.05232 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5f614cde-9b28-3d3a-a355-b0bad6c96eb0 | -12.86981 | -46.43507 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9be7280-ace6-3cc6-83d7-999e7e542e79 | -7.08976 | -42.73248 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d742c0d-0b1d-32d3-85cc-ad883a6991c7 | -6.87324 | -39.84571 | 2025-11-17 03:27:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcb3aef1-cfbd-33f6-8014-7224c99a3aee | -10.03128 | -44.07034 | 2025-11-17 03:27:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 684dacfe-0f1e-356c-9bd6-447620688f67 | -10.96755 | -44.52306 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa6afeae-d470-3e54-b44b-981712a2987e | -11.96789 | -44.30608 | 2025-11-17 03:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d6c666fc-50bd-329e-aab6-fce77c27bd12 | -12.80202 | -46.43903 | 2025-11-17 03:27:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e116fb0-d2e9-37d7-8a10-555394d562bf | -9.71469 | -43.96294 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a41a74c-c4d8-3c2e-ada3-6da2f4639442 | -6.70495 | -40.80478 | 2025-11-17 03:27:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0acf2df-ab2c-3659-9648-332cd767d50c | -9.72549 | -43.9588 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a94a286c-740f-3c1e-97f2-ab648707856a | -11.40345 | -43.32471 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71b65c8d-8f0f-3812-9853-e1956276c0e7 | -11.96905 | -44.30042 | 2025-11-17 03:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 25826659-157a-3cd6-a580-ffb17f9649ee | -6.77585 | -41.45221 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c9b2138-1dfc-3341-9dc8-8340d4e72954 | -5.88405 | -43.98308 | 2025-11-17 03:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca1d385a-14b3-3dcf-9044-4c3a86fb3413 | -12.87055 | -46.04873 | 2025-11-17 03:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75861fb9-f9a1-3ae9-83d8-60f1a4f83393 | -12.86819 | -46.4427 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d51708fb-ab60-39af-87bd-4b0550aa6f28 | -7.09738 | -42.7284 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c5246aa0-19a2-309e-86c7-792c86ce1111 | -6.92648 | -41.82832 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8979f36e-43ac-3ec4-8bda-bdcd369830ef | -6.70569 | -40.80069 | 2025-11-17 03:27:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6e73389-2efb-37ac-a5ed-b8211f704334 | -6.68397 | -42.04829 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 64fa7fa2-c24d-3121-a580-17d849df8faf | -8.11737 | -43.53555 | 2025-11-17 03:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44f42398-d552-30d9-9a54-54e2cb13310d | -12.87983 | -46.46423 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b61ddbf-d82e-3f14-a824-54645a6938a6 | -9.74999 | -43.95895 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d88ed7f3-0f91-391d-95ec-bce05d6275e0 | -10.96634 | -44.529 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5bb4a1d-5e90-3817-ae21-94ae7ed9c424 | -6.93118 | -39.61555 | 2025-11-17 03:27:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 43664e1f-36a6-390d-8fe8-48f310901a40 | -7.0972 | -42.72844 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0c8c098-e1ce-3a28-b0a2-91cbc61d42c4 | -9.71344 | -43.96907 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e399436-f26f-34b6-8673-fb307c09a050 | -11.40966 | -43.32602 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b69f56e3-7fb8-328f-8316-b28af3feb449 | -11.62133 | -43.90348 | 2025-11-17 03:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44fd625e-fead-36ae-b6c7-769a977551ed | -11.40867 | -43.33098 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49d31c49-d7b0-35bf-8f6f-c3e5543a63f5 | -11.67453 | -44.7258 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edd64f18-73bc-3787-b468-acfba77ce336 | -8.24804 | -41.42225 | 2025-11-17 03:27:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
