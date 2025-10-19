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
| a35f6fb0-9f90-354b-bdb0-4a2e1e0be9fb | -3.28219 | -40.88414 | 2025-10-19 04:10:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b444af5-4fa5-3836-8e1a-1fe128ca52db | -4.9654 | -45.91528 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f58c34b5-8560-36a3-bc3c-f69d3ee38640 | -3.14058 | -50.25376 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b86e6f59-ef7f-3b35-9e4b-c41e5fce29b1 | -5.39898 | -42.79997 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b231bdc-9b2d-375e-99b9-484fa502efe9 | -6.25898 | -42.68926 | 2025-10-19 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4036152-bb8c-3309-9f7a-a370cc7a4f26 | -5.96177 | -43.18692 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 946a2b22-be88-3e30-a722-cd904c8c34c7 | -6.85618 | -46.92884 | 2025-10-19 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce8e059d-bf68-3b9d-b476-c65fda484bc5 | -6.0624 | -44.52224 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdacab5c-d7df-3b4f-a6e3-91ca874bf496 | -4.25796 | -48.54925 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0778a575-4683-3c0a-ad7c-a98c528cc847 | -7.15358 | -44.45977 | 2025-10-19 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e730ac5e-e7db-3d61-87a7-e1cc3e82fa2b | -3.14663 | -50.25114 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73810e61-23b4-38da-b336-5c11a406c161 | -5.6448 | -46.58541 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 358f078b-87c4-3a93-830e-e83a88afb210 | -6.43352 | -43.3597 | 2025-10-19 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cee3f00-a7b0-3b8c-aa3d-0e6ea391151e | -4.57377 | -45.8811 | 2025-10-19 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c8bf578-a112-3810-aa7b-590bfda1023e | -6.02077 | -41.87707 | 2025-10-19 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a99d544-b237-30af-8deb-82e298e4fc7b | -2.79517 | -49.65184 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3433dd84-a7f6-3939-ae3d-e9ae540d79b0 | -4.91096 | -43.27091 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec479af7-408b-3f3c-93a6-eec86d4fc634 | -6.72396 | -46.32026 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9006fed2-1570-3072-93a7-4c123a208d96 | -7.47655 | -42.74112 | 2025-10-19 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5482942-7809-3eb7-a620-fbe8a1047bde | -7.44262 | -42.69572 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f17a9fb-c76a-3190-a503-827a33821d4c | -6.56394 | -44.42684 | 2025-10-19 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 386fcd60-f4d8-3bb2-8eec-c75bfe520264 | -6.07058 | -42.26783 | 2025-10-19 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a98c5c06-1310-3baa-b493-f6afa4c6a2fd | -6.19548 | -41.5666 | 2025-10-19 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d695b058-8579-309d-859c-5be7fb8002fd | -6.17574 | -42.57772 | 2025-10-19 04:10:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bc865d6a-f16d-327e-abcb-9af4fcca0657 | -5.95417 | -42.2315 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99d4864b-5ba9-3727-bc7d-8a6ae0621b55 | -4.56935 | -46.50443 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7873887e-2aeb-3ec5-b05b-64ff3e4546b6 | -4.84194 | -42.74592 | 2025-10-19 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 696f28d1-130f-3afb-9dc7-9d791fc7fcc1 | -7.19813 | -42.1929 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7e676edb-12d1-3093-90a6-bab62526626d | -6.06306 | -44.51812 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49a1dd79-7891-32ee-816c-328112d7fc58 | -1.42724 | -49.1013 | 2025-10-19 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d9f37a0-6844-3934-9195-be9c54ef8861 | -7.30173 | -41.94874 | 2025-10-19 04:10:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0897d8b6-aa4b-36df-bc1c-61099493ca15 | -5.1005 | -46.13561 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| aeb21f17-3d44-3545-bcfb-7c211deb09d5 | -2.69908 | -49.5536 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6164a92-8365-3cee-bb31-7ddc46a721f8 | -4.72726 | -46.15899 | 2025-10-19 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 797c0f30-cf98-3149-b2d8-a139a1adc635 | -6.23194 | -44.13698 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bcc7776-c935-31db-a793-24e75506e708 | -5.10454 | -46.13609 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61751ebc-203c-3487-a3a3-c7cb76e614d0 | -4.77634 | -46.60955 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 037cad57-579b-3d23-aa0b-3ad7c8814bc7 | -7.19158 | -42.22017 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ee3f2f6-c71c-34c9-a5d5-2f4ed27aa564 | -3.81668 | -51.32546 | 2025-10-19 04:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14db410f-bf1c-35d4-a061-2d10b7e69922 | -4.23972 | -43.09743 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2c3ba22-337d-3931-bb5d-7204d3dfc0e5 | -6.35719 | -46.08805 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44467258-ad2c-325e-ae3a-598349e250fc | -5.71268 | -46.50467 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b496afc-aafe-3f42-934e-5552b3e3aef8 | -2.69384 | -49.5527 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 50c9bad5-1c48-371e-9946-62fa028bdde8 | -4.83292 | -43.01852 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7eafc34-bf63-3d76-a453-cfeb0fa129de | -4.27227 | -48.88228 | 2025-10-19 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b2d15e4-885f-3438-aa92-ddb972785bc3 | -6.36573 | -45.74818 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b19891a-0e31-33fa-8dc3-8200cf0a14c0 | -5.20384 | -42.68826 | 2025-10-19 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3f8319-682c-356d-8890-6f29f23492dc | -6.09548 | -44.02379 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af2af5ca-eb85-34fc-9d99-fc250f8551e5 | -7.10781 | -46.66245 | 2025-10-19 04:10:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07a55943-481d-3d55-b1b4-af13d6c42c5a | -6.79397 | -46.47519 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 212ae3af-0228-3979-8a2e-b5f1eac324ae | -3.52045 | -49.93347 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 421b09c7-0b33-34ce-a7ae-5d52f7ac6078 | -4.48615 | -50.56696 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98b17633-a939-34bd-a232-ada4e3c48b8c | -3.14721 | -50.24759 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61cf9c1c-50b1-30e7-9232-854b42f50ce9 | -6.00548 | -44.18148 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffa16b58-94cb-3bea-aa65-f05fd4800e2a | -5.4787 | -43.1304 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee274afc-1136-34fe-bad4-d1aa2ca52b55 | -6.05618 | -44.333 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f792e1e-c09c-3482-862b-aec2e0cdd12f | -4.24208 | -44.67869 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43759658-d6d4-3791-9945-e50908a7d56c | -5.40729 | -44.06047 | 2025-10-19 04:10:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43dd4394-3046-3f5d-9fc3-4673db54239d | -2.45082 | -49.36683 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa373f3f-99f6-3018-8964-e54ac02296c4 | -4.92434 | -45.6739 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6877607f-962a-3876-acc4-2152bb2788fc | -5.35773 | -47.2147 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1a9088d2-4431-352b-93a9-6e5fc30a9a0a | -6.43411 | -43.35603 | 2025-10-19 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4f83a05-0646-3835-a20a-4ab013a48904 | -5.89333 | -42.80751 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db90a1c4-e574-3704-97b1-40e46f2cb1f0 | -5.38092 | -46.42646 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e64b8e6-4b2e-387b-942b-f6614d00113e | -7.29895 | -41.94474 | 2025-10-19 04:10:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 248729be-9827-38af-a2a3-c814dcea41b7 | -7.42093 | -40.0723 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e94b3d1-743c-3e1b-872b-cf630db3d5c1 | -6.89607 | -39.74623 | 2025-10-19 04:10:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca11e1f6-0d15-3d59-b8aa-35cba4cc9160 | -2.78989 | -49.65096 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 388b72d2-9735-3722-9e69-6df093ab25f1 | -3.33146 | -45.62441 | 2025-10-19 04:10:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b607042-e4d0-3770-b5b7-93cb00e0773f | -5.37186 | -42.7957 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3c6520b-1030-30fd-adfc-077fd816f107 | -5.29675 | -45.08188 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e158cd0-322b-35a6-b169-4ff36decd3be | -2.4441 | -49.37535 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c234b0ba-f109-3448-b8bc-74bdc96bd3cf | -4.75807 | -45.42018 | 2025-10-19 04:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f2008f5-20ec-3e2a-b557-b0aadb31dd6c | -5.63879 | -44.81205 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9099f594-9e7b-373c-b5a5-4e7f773defb1 | -4.06919 | -47.31413 | 2025-10-19 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f01aa3d2-94dc-305f-a536-bc7bbdbf5ecc | -5.75936 | -42.70928 | 2025-10-19 04:10:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25bffa29-4ebe-369e-a78a-66472dc69cb8 | -6.15153 | -44.30114 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b1faef-db6f-355a-9be7-fa688fd5082e | -4.85429 | -44.59192 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1b3b9d2-5fef-34fb-8446-ef65aaa34437 | -7.27526 | -42.30907 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b419462-b720-3905-92f0-3814135ae23c | -2.70516 | -49.86298 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1bdc593-9e76-3b96-997c-b461cd45a7ef | -7.15604 | -42.37947 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c156afc9-8649-39ad-8b5e-f69281e7aab7 | -6.41956 | -43.91871 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 15e3f456-c3ae-377a-aefd-d4c8158943ee | -6.13062 | -44.22838 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0e094fa-a6de-3ac1-8045-76b39490b975 | -7.41637 | -40.07913 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c7ceb0e-79a3-3b7f-804c-c2f9594a71c8 | -7.24894 | -40.14745 | 2025-10-19 04:10:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f747706-205b-3791-b96f-bbe63a84c370 | -6.98376 | -39.69366 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9820f3ca-9921-37cf-80df-97cfb6da7fc0 | -4.42281 | -40.16874 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86a59eaf-002e-3129-b831-1341d7ba4a87 | -2.6886 | -49.55179 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 51e91b44-854d-3649-8c0c-07b4ff5a608e | -4.45565 | -43.23065 | 2025-10-19 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b245c2-310d-3834-be53-4e6482b24ec9 | -5.78506 | -45.99049 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d5c493d-5544-3244-82a6-08a87db318b5 | -5.37231 | -42.81435 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d1b9524-5d6c-31d9-a0cf-23975fdf9b4d | -2.83819 | -42.14774 | 2025-10-19 04:10:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad04214f-c090-32b8-9c14-2cfd7c408f3f | -5.3374 | -44.71487 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a1dcaa4-0098-3377-93bb-ffedeef70f88 | -5.17569 | -45.27594 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e6f536e-8ad8-3388-a7e8-0a43eeeacd97 | -7.19868 | -42.18941 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 80c2d729-3fd6-33bf-8b86-58c424ce310a | -4.2325 | -44.69065 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 519d360b-2842-3157-ad6b-3031bcbfda9d | -2.44613 | -49.36281 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3338898e-0e50-3130-a75e-3f133b65cfa9 | -5.35346 | -47.21391 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2428e853-fded-362c-8786-7a35d03fa909 | -2.65565 | -49.52472 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083cde38-56f5-3f43-bfbd-965beb3a9d04 | -6.06381 | -44.52118 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README21.md)
