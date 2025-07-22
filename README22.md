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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7349f26-0b32-30c4-871b-7e33e82d2b74 | -6.9804 | -42.7854 | 2025-07-22 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 903d9677-d165-3a25-bd80-dde7e2c11040 | -11.871 | -44.5189 | 2025-07-22 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 513de0fa-2d7e-3ccc-9d08-565bc63882bb | -6.9615 | -42.7872 | 2025-07-22 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 9e45a74f-7b98-37eb-8768-8e2ba979f60c | -6.9801 | -42.809 | 2025-07-22 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 2972cbf2-cfbe-367c-aed7-e465225c827a | -7.0412 | -45.8412 | 2025-07-22 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d26d290d-0ebf-394d-9995-b4a5a0433911 | -7.0409 | -45.8637 | 2025-07-22 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 870ea9f5-8970-3574-8429-0b72cac0185b | -6.9801 | -42.809 | 2025-07-22 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 13947d85-c43d-3107-b4b0-64f099a01b5e | -6.9804 | -42.7854 | 2025-07-22 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 4d2dca60-620c-3b7c-8677-d5fda0c5ced4 | -7.0224 | -45.8428 | 2025-07-22 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4e13bc9d-fef1-3ae6-94f2-1deca323a364 | -6.6684 | -45.6472 | 2025-07-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 6c9223d2-6cb7-3aca-9b67-1375e043f0a7 | -17.5548 | -47.5036 | 2025-07-22 13:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7eebb27b-45fa-32b4-8809-5f10ccb64c7c | -17.5748 | -47.4996 | 2025-07-22 13:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| f03c4002-c297-37fd-ba76-8f44e448653b | -7.2402 | -44.7812 | 2025-07-22 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 933e3902-2cfb-3032-b67d-d822bd544abc | -11.871 | -44.5189 | 2025-07-22 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 3a72f256-66db-3be5-b503-11efbaad4169 | -11.8715 | -44.4956 | 2025-07-22 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 261cdb19-f9f8-393c-beff-0d23c4f17e29 | -6.6682 | -45.6697 | 2025-07-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| b6d140db-d83c-300f-a393-7ab6ed1aeb72 | -11.8715 | -44.4956 | 2025-07-22 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 60384035-9460-3efd-a218-02622f752026 | -17.5548 | -47.5036 | 2025-07-22 14:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 11b94f05-dfdd-34c1-970f-a94aba9c3de1 | -7.2402 | -44.7812 | 2025-07-22 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cd227a39-acf7-308a-a9e3-aa80e943aa04 | -11.8518 | -44.5219 | 2025-07-22 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7e2ccba5-8898-326b-8873-b00296b182f8 | -6.6682 | -45.6697 | 2025-07-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9cbab97a-3718-310c-8916-ddf4d3133388 | -6.9615 | -42.7872 | 2025-07-22 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| b4025ea0-baf7-334a-930e-8dab54ddfda5 | -17.5748 | -47.4996 | 2025-07-22 14:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 65aad44c-17f5-3ebf-9681-66f5f1c984ca | -11.871 | -44.5189 | 2025-07-22 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 610216b3-6bcb-3ba6-ae08-282de27407d6 | -7.0224 | -45.8428 | 2025-07-22 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 457c034e-9165-337f-93b1-4cf1e5584dad | -7.0412 | -45.8412 | 2025-07-22 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| bb057563-cb1b-302e-afd6-68a055d33933 | -7.0409 | -45.8637 | 2025-07-22 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 75d75b8d-228f-33aa-a1a3-49a7cca5ce85 | -6.9804 | -42.7854 | 2025-07-22 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| ae619c7b-425f-3a21-b0e9-cbc3442177f9 | -7.0412 | -45.8412 | 2025-07-22 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| c3dca066-142d-3ffd-8ad2-b7eef8b31fb4 | -17.5548 | -47.5036 | 2025-07-22 14:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b75505f2-9926-33b1-9528-5281b3a472bf | -6.9804 | -42.7854 | 2025-07-22 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 35ba8ff3-151e-3a85-bca5-6020067ebd1c | -11.871 | -44.5189 | 2025-07-22 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| fa4ad0cf-b3ad-3adc-91c6-503e0e50dda0 | -11.8518 | -44.5219 | 2025-07-22 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 310cab74-1740-36ed-b70d-cc7ded8e7f89 | -17.5748 | -47.4996 | 2025-07-22 14:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a54849f0-dde0-3239-a653-a404f6b4e6a5 | -7.0224 | -45.8428 | 2025-07-22 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 520cde39-2a12-321c-825e-5b2e35b4bbf2 | -4.9682 | -43.2299 | 2025-07-22 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b42b6fc5-f52c-3520-9f82-26589d63e701 | -6.6682 | -45.6697 | 2025-07-22 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c3e424ec-394f-3c0b-a36c-8c24765cd027 | -17.5548 | -47.5036 | 2025-07-22 14:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a0a8e7a3-00fd-3f73-8a6e-3b3fe6e80abe | -7.0412 | -45.8412 | 2025-07-22 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| f4232aec-cc33-36f6-b8ec-53a6be5cc74e | -4.9682 | -43.2299 | 2025-07-22 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c06d4441-0ba6-376b-a1af-ca90d0b99902 | -17.5748 | -47.4996 | 2025-07-22 14:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 447ca507-88be-3c2c-9fb5-de8aeed3ced0 | -6.9804 | -42.7854 | 2025-07-22 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 75c29e09-a10b-3664-b759-a933f6a3ebb3 | -7.2402 | -44.7812 | 2025-07-22 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 48d57a1c-2f9c-3ad3-8b81-00cf7cc6e59b | -6.7994 | -45.659 | 2025-07-22 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ddd2c9eb-dbf2-3bbb-899e-363d72556a36 | -6.6682 | -45.6697 | 2025-07-22 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 1f5be753-e50b-3d55-a6ea-b28954c0bc58 | -7.0409 | -45.8637 | 2025-07-22 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e1a2e8b5-2c48-37c0-b592-077414f6e989 | -7.0224 | -45.8428 | 2025-07-22 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a683ff5f-e79f-31cb-a335-27f124554be5 | -7.1368 | -47.4766 | 2025-07-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b0cd7d73-4bc1-39af-bc20-680e2c2f433e | -17.5548 | -47.5036 | 2025-07-22 14:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| efea4e20-7e69-39f9-be10-30bee4c7df50 | -7.0412 | -45.8412 | 2025-07-22 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 74e8a394-508e-30ba-aeb5-3a77f3273634 | -6.6682 | -45.6697 | 2025-07-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 170a1e1e-a754-31a8-bbf0-779a01032ea7 | -7.0224 | -45.8428 | 2025-07-22 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 385709c4-ae63-3159-ad00-9022ef0e13ae | -17.5748 | -47.4996 | 2025-07-22 14:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7ecfecce-6939-3bfb-8f0a-0b213a6ac769 | -7.0409 | -45.8637 | 2025-07-22 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d5881203-64cf-34ed-9196-650e46353246 | -6.9804 | -42.7854 | 2025-07-22 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 1c4f193a-f505-3436-9e04-20dd803e9591 | -7.9645 | -43.9971 | 2025-07-22 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ccb321fa-21dc-35a0-bbbb-cf9756d09877 | -6.6867 | -45.6907 | 2025-07-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 9596962d-ac80-350e-8bf7-f0b36c570723 | -6.668 | -45.6922 | 2025-07-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b8e87bb9-95e0-37b5-946d-f7e3dcf074f8 | -8.3462 | -46.6621 | 2025-07-22 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8def9ae6-f6ec-3faf-b37a-6e7e1c19e486 | -6.6682 | -45.6697 | 2025-07-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 93439311-c337-33f4-8d8a-2fe598116f49 | -8.3464 | -46.6398 | 2025-07-22 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| fcf12b8c-d506-321b-98ae-90002a2a483a | -7.0224 | -45.8428 | 2025-07-22 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 87ca92e0-c577-3a00-808f-63501718f79c | -6.3417 | -44.584 | 2025-07-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| bf5ed706-5c49-3f10-9c0e-41ffcb9ed588 | -6.6867 | -45.6907 | 2025-07-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9c9c7fad-c369-31b2-815a-ec4b748dd21b | -4.9682 | -43.2299 | 2025-07-22 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9fcfdca9-4db3-3c73-90bf-f7c619657df8 | -7.1368 | -47.4766 | 2025-07-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f98f131d-65d9-3add-82db-fcc30fddfa38 | -7.0412 | -45.8412 | 2025-07-22 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 86a9122b-5fb8-31ce-8be0-4bfe86178f3f | -17.5748 | -47.4996 | 2025-07-22 14:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9069f0e7-58ef-3940-905a-346a681e760e | -7.0409 | -45.8637 | 2025-07-22 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |


