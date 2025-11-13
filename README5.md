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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5596ce15-4aa5-3be7-aff5-502d0d36d772 | -7.8138 | -41.775799 | 2025-11-13 00:14:00 | METOP-B | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3bd5a8f-2333-3388-bfa8-4f3bfc2e3f81 | -3.7751 | -45.999802 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92cff4b8-0554-39d8-880e-e07ee2033a69 | -6.1461 | -48.052799 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7e5966d-49ed-3761-8e03-c87f7fb33f1a | -1.9391 | -52.0807 | 2025-11-13 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 695da2b3-84e7-3313-8244-34b0b14dd59c | -3.4368 | -45.563 | 2025-11-13 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9796f43e-1bd9-34c2-b4f7-a2b462260c95 | -5.4523 | -47.680901 | 2025-11-13 00:14:00 | METOP-B | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17feb43a-7cf3-3141-81e9-bc9fb68ffc85 | -11.7972 | -44.1926 | 2025-11-13 00:14:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1bc2081-3360-3ad1-ad88-3ecbbe33d0d7 | -13.7306 | -49.123699 | 2025-11-13 00:14:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 55446a0c-b6a9-3dc1-acd2-2f6620fd1a8c | -10.3682 | -45.045898 | 2025-11-13 00:14:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7788f76e-27ba-3246-be96-76e695ed5a16 | -5.3264 | -45.187901 | 2025-11-13 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03aa6fcc-66ea-3bcc-90cf-e0bea6eb950c | -3.1027 | -49.2603 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54d24923-c9f2-3928-a60c-c89ebed91d81 | -10.9333 | -44.598801 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eae6c022-174a-3e31-92cb-f9e23327b8d5 | -10.9182 | -44.6217 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59b0c49c-93b9-3d7f-aa5f-6f0cac96c285 | -10.5511 | -44.815201 | 2025-11-13 00:14:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8667b23d-ea75-3d6f-984e-f421e860efee | -2.9473 | -45.5383 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73470da5-50eb-3373-a27f-803d1129b403 | -3.4729 | -45.8517 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51d75e46-3067-32a5-9ce2-633735969c54 | -13.3283 | -43.1702 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b4f90f89-8dc7-3840-aa4e-dc332b511231 | -18.029301 | -51.026402 | 2025-11-13 00:14:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7f0a2ad-8ac5-31d7-9ea8-33d3be7e7688 | -22.4736 | -44.182598 | 2025-11-13 00:14:00 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbedcfb2-42de-326e-ba1e-7eb4890700ac | -7.674 | -45.8769 | 2025-11-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8281928-2051-3ffb-a420-3612c2e38b1d | -8.4122 | -48.042999 | 2025-11-13 00:14:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 990bbf3e-ea28-3799-9de4-fbd1d1a8bb42 | -10.4468 | -47.334599 | 2025-11-13 00:14:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebe53a0c-b9f7-33db-ba66-5c1a3d20c624 | -6.3046 | -43.7938 | 2025-11-13 00:14:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1de17a06-6683-38c3-8de8-486729dfa6ff | -14.1698 | -43.57 | 2025-11-13 00:14:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba525bed-326c-39a7-892b-b5d0c7043603 | -3.1548 | -45.5014 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2368c05-cc3f-3c50-8891-702d0675347b | -7.6623 | -45.8708 | 2025-11-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8099f564-cb3b-3dc9-9df1-701df36fdbc5 | -4.5178 | -46.402901 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b83b8b13-4ae1-3467-9c8d-4371d1a809de | -3.0337 | -50.271702 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c569d94-34a8-3613-9ab4-cc432dbf91d4 | -11.0243 | -44.633999 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c24c391-62a9-3bb5-a262-d43c39993926 | -3.2109 | -50.189201 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14150f08-a9d8-36e6-a8ee-07b8dbad3fd2 | -10.6283 | -45.228699 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef7f7f23-e01b-3e69-b89b-03e2a0852bbb | -5.3603 | -46.7467 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db2a969-02a0-32a6-b503-df8bf2cbd52a | -4.9292 | -44.289299 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cce660d1-f9cb-3849-8b37-cfc402c16448 | -21.038099 | -48.510502 | 2025-11-13 00:14:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b95c4dfc-16be-3abc-9b8b-dd41e18bf78a | -20.758801 | -47.118401 | 2025-11-13 00:14:00 | METOP-B | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0ae1592-4a88-32f7-965f-50ef960c4326 | -3.3423 | -48.368801 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513f3a05-9a34-334e-aebb-63b603d38071 | -4.5667 | -48.493999 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8753356-eab0-343d-bae8-9e533b0ffc5d | -10.685 | -44.987801 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23d2f07d-cc3c-3eb3-871e-56e5c3b45253 | -14.1064 | -47.8862 | 2025-11-13 00:14:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b39597c-353c-3010-b8c1-33639c2750fa | -3.7079 | -49.021599 | 2025-11-13 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cef1c8-6072-3455-bd4a-757b0602d9a8 | -8.2538 | -44.358101 | 2025-11-13 00:14:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c45d25a5-cd2f-35d8-b449-bd8e08ee90aa | -6.1657 | -48.048302 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc67dd8f-6e7a-32c4-89e8-8d9fed2666f0 | -4.5336 | -46.426498 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e98da7ce-75f1-3f99-bdf6-49833c443897 | -3.871 | -49.783298 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250509ca-4d5a-3e03-a97b-9aa0967a2adf | -2.738 | -45.479 | 2025-11-13 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5833b980-a58e-35eb-b819-880c8be9397b | -10.7507 | -44.916599 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe6f22d-d862-3029-9ca5-d1f4f7431e33 | -22.6448 | -44.900101 | 2025-11-13 00:14:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ddb29eb-d1ce-3bca-8628-d0e599bd7a77 | -9.3451 | -46.583099 | 2025-11-13 00:14:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c24dae9-c3b1-3ed4-a18f-a576a734411e | -3.265 | -50.019299 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db78456f-53e7-3ac5-9d13-4a3ff54702bd | -5.3818 | -46.750301 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8279003-9289-3366-a615-fe5b0fd88d72 | -6.6944 | -47.791 | 2025-11-13 00:14:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 185d1c01-97f8-3535-a1a6-54f4efa1a438 | -3.4603 | -43.163799 | 2025-11-13 00:14:00 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f43adb3-182c-3ea2-b0c0-bdf271f5f459 | -4.1453 | -47.645699 | 2025-11-13 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42922b61-9043-309a-adc1-6016a2e18b1f | -10.2924 | -44.943501 | 2025-11-13 00:14:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f836bc7-5983-3f92-bbf9-8b0f30572c70 | -2.4515 | -49.252201 | 2025-11-13 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0a3185-5f05-307d-b0bc-78041483fccd | -3.0915 | -49.2972 | 2025-11-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| bd78d36f-5a56-3e7a-9326-43cd8f61cfd7 | -3.2378 | -45.5839 | 2025-11-13 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6ab34502-ea28-3b06-bf3c-b8c090aa4b19 | -4.7018 | -46.4508 | 2025-11-13 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c628a22e-e2a8-38c3-8e86-bab3292b398f | -2.4634 | -49.2727 | 2025-11-13 00:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 08500234-b4e1-3e33-9f59-afc3d560e801 | -4.2157 | -50.0812 | 2025-11-13 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1a58747c-9e96-3ae7-be46-1593349030fe | -4.7204 | -46.4497 | 2025-11-13 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 143.1 |
| df4cfaa4-783d-3c6a-a71a-1ede2e183fa4 | -2.4635 | -49.2514 | 2025-11-13 00:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 00716b61-03d4-32ab-83a3-2601a2279b3e | -3.8658 | -49.7998 | 2025-11-13 00:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 64b3c0eb-276d-3d60-ae4c-3f39f0fc3f23 | -4.3188 | -48.2422 | 2025-11-13 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c5306bb9-e77c-300f-ad71-426fcba446d2 | -4.2156 | -50.1022 | 2025-11-13 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| e43f34cf-7c57-39bd-bd9b-6b292d7e8249 | -3.3729 | -48.4107 | 2025-11-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 075df781-aa86-3e20-a081-3a7aea8ac562 | -3.2192 | -45.5846 | 2025-11-13 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 07b8e147-d36d-3414-bdb8-979da99e6729 | -3.0731 | -49.2765 | 2025-11-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3ec8fcb6-2ef0-3d1a-a4cc-e7caf8de75ea | -3.0917 | -49.2547 | 2025-11-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9163ccbd-ee53-3b30-8753-fcfd2883ab99 | -4.3003 | -48.2431 | 2025-11-13 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7dd11099-5caa-300b-a55f-108fd23fb31a | -3.0916 | -49.2759 | 2025-11-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 042607fd-04d8-3c41-9f48-5642a00cb229 | -4.5344 | -46.4376 | 2025-11-13 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 1f7f35b6-57ef-3bc6-bdd3-7ccf1686308d | -4.1161 | -48.0136 | 2025-11-13 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c317e2b7-5c62-3b09-8c3e-b324a3947ffc | -20.4693 | -53.0457 | 2025-11-13 00:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 845312f5-4a2b-3710-ad7f-ff2ff5cb66bf | -3.1453 | -45.4978 | 2025-11-13 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 481a9e40-858c-3a04-9d24-a5a39ca389ce | -2.8297 | -45.4419 | 2025-11-13 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6e2c8cbb-459f-3ac0-a9de-30ec195c8765 | -3.1101 | -49.2753 | 2025-11-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 46270392-b8a6-351c-9ec9-8336b4ccb8ff | -5.3885 | -46.7645 | 2025-11-13 00:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 215baae6-c4f5-3082-81c3-6acfb2137411 | -4.7206 | -46.4276 | 2025-11-13 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 01cb7f6a-a123-3df9-aaa6-c93013cb5059 | -2.8111 | -45.4426 | 2025-11-13 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8db9978d-1534-3c8d-ab17-9c7e56312df1 | -3.7745 | -46.0305 | 2025-11-13 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 03747eb9-5b08-3ebb-97e5-7752cd0f003f | -3.7746 | -46.0082 | 2025-11-13 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 131.6 |
| e599de2a-5499-3a69-855c-9d85dedb3f1b | -3.7932 | -46.0074 | 2025-11-13 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 57b9bbb8-0045-36f9-b49e-0b21f209880e | -4.7206 | -46.4276 | 2025-11-13 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fcafa4ff-5e68-38cb-8622-c99b752afedf | -3.2192 | -45.5846 | 2025-11-13 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 5a53de7e-f54c-31b5-b09f-68320621a0ed | -3.0917 | -49.2547 | 2025-11-13 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0c4366e5-d5ec-3eec-9393-7937b822c5a7 | -3.8658 | -49.7998 | 2025-11-13 00:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 0956903f-d84e-3727-9ae7-2324107d12d3 | -4.5344 | -46.4376 | 2025-11-13 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 32368416-9ef0-3493-97bd-841ab61ab589 | -2.8297 | -45.4419 | 2025-11-13 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d53f738b-f840-3e96-80db-06bee02dadb6 | -3.1639 | -45.497 | 2025-11-13 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 53810dea-42a0-3344-85db-c074f66eb484 | -7.66 | -45.8764 | 2025-11-13 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 148eb396-5497-3bd1-96fd-874a0f2658b2 | -4.7204 | -46.4497 | 2025-11-13 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 1a0aa5f2-03d3-3ba0-8567-459e7d493f3a | -3.0916 | -49.2759 | 2025-11-13 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| c73c8034-e003-3f71-b2a5-527078609f4a | -2.4634 | -49.2727 | 2025-11-13 00:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 81656bbf-d3c0-3b6f-889c-078c5992beaa | -4.0976 | -48.0144 | 2025-11-13 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| e0f0bbe3-5dec-38ba-bbe5-f90d62fdd648 | -4.7018 | -46.4508 | 2025-11-13 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| af4da727-3c01-3668-b0cc-88367b582c10 | -4.2056 | -48.5706 | 2025-11-13 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 784549a6-03f1-3f97-9b49-c029186ee884 | -5.968 | -35.3397 | 2025-11-13 00:30:00 | GOES-19 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 64.7 |
| e7741976-ccb0-3136-b0b1-29551c8e746c | -5.949 | -35.3418 | 2025-11-13 00:30:00 | GOES-19 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 2b439ee0-4114-3f76-9b60-6d365453b57d | -2.4449 | -49.2731 | 2025-11-13 00:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |


[Clique aqui para ver as próximas entradas](README6.md)
