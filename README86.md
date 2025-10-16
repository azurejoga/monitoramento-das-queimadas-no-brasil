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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a41c5e60-2c76-30ce-b23a-ca9c23a569fa | -7.67658 | -42.37298 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 00d7576a-ab3b-3ea2-9cf9-7291a9c85e10 | -12.3102 | -45.64354 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1028.2 |
| a136424d-328f-3f98-a0f9-b86d39915abe | -7.49222 | -44.65768 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| cbaed192-09ca-3e2f-b9ad-4b40314369e7 | -11.57484 | -44.06492 | 2025-10-16 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 03638688-57e6-3270-93d5-52c2ed358f86 | -11.42705 | -44.12294 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4dba6955-705b-3b05-8b0b-4d2ea6a46101 | -8.25161 | -44.07065 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f80fbd64-ba9a-33d4-a23b-8a7c039290e7 | -7.3342 | -41.20866 | 2025-10-16 12:00:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 5e39dc7b-e53d-3aaf-8515-66cd3ad51d15 | -11.42934 | -44.16942 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 249.9 |
| cc664676-9bc5-3b11-90b4-a74369239b62 | -12.2955 | -47.15331 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| aaee2b84-6d68-316c-b57c-8076278b751a | -6.54855 | -43.91522 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1e6d7427-9ae2-36ad-92fc-af83c4744a8c | -12.39067 | -40.76254 | 2025-10-16 12:00:00 | TERRA_M-T | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3e778592-5f72-31f8-846c-f7b2051e1408 | -15.78375 | -43.64716 | 2025-10-16 12:00:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eb99dc24-d27f-37b9-b3f2-58ff0efa8d45 | -8.47366 | -44.19107 | 2025-10-16 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ca60ee2b-2134-3d2b-a946-4505e300b47e | -16.29926 | -44.56347 | 2025-10-16 12:00:00 | TERRA_M-T | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a27e627-b3ab-3632-bacd-536fd130591e | -6.56711 | -42.96844 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a9d50134-98ec-3477-846a-c5277e03a59f | -14.21315 | -44.69282 | 2025-10-16 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8418d29-d403-3ad7-947c-8417f02b7883 | -13.78701 | -43.62161 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d5cdb65-c008-383c-a416-9fbc6e0177b8 | -6.42818 | -43.09044 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4ce41faa-9810-32c7-a31f-2fb285b7c939 | -8.45702 | -44.179 | 2025-10-16 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 29907a6b-148f-3b0a-a631-1be77b6b7158 | -7.18979 | -42.36365 | 2025-10-16 12:00:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| fb7a1f7d-a788-34d6-8104-0a875bf8f316 | -12.28895 | -47.13342 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 5fb56898-22e9-3087-bc4a-54c37b2642ba | -13.88812 | -43.55898 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 62f1007d-a9ee-30bb-9e3e-9387e4e1ccf4 | -12.29739 | -47.14135 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 6b273354-705e-3489-8715-ee433ff45bfe | -11.43821 | -44.17072 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4db9a399-1022-3d20-a513-9a655353205f | -13.91389 | -45.59391 | 2025-10-16 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f3b10bf4-4236-3fcd-81e8-55a62662d361 | -10.12645 | -44.56133 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d1e39b0e-1c58-3a88-90c6-678fa6383bc2 | -8.62549 | -47.07327 | 2025-10-16 12:00:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 55d9bd13-f0dd-310b-8fe1-887d4c7e7a81 | -11.43197 | -44.15134 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| bb404af4-76ef-3b9b-bbd4-85e8c7005dc2 | -8.83827 | -44.4094 | 2025-10-16 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| a9b8e0fa-0f17-3b25-82b5-0f042717ae88 | -12.98625 | -47.33183 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| cde37fb4-0122-3b2f-9c55-b92555884f58 | -7.65632 | -37.63607 | 2025-10-16 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 45.9 |
| bcfcf722-87d6-3259-a18f-fbf418b9f98e | -11.43295 | -44.20692 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 03c8ba21-4063-39c6-8999-deaa53538a9c | -8.47501 | -44.18179 | 2025-10-16 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| d80017c9-d30a-321f-b381-dc399bb34df1 | -10.82506 | -43.9452 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 67450383-7f85-375d-8480-77cfcfda5cfb | -8.46599 | -46.25228 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1da16ae7-2c62-3de8-8cca-a49974e2df9c | -11.43558 | -44.18882 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 2ed847d9-f104-3cb4-9b9b-9b7ae061f75e | -7.48326 | -42.74815 | 2025-10-16 12:00:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 212e2e40-d226-367b-99a1-93ad8450656f | -6.35693 | -45.49491 | 2025-10-16 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 24115903-3224-318a-9ec0-78d64d2da012 | -7.12107 | -44.71651 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| af81641f-d144-3348-912c-555090a39da9 | -8.27288 | -43.35672 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| df6b1d46-4403-3c66-ba67-bcc19d130307 | -8.38311 | -46.25758 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 03bee842-afe8-3912-9c41-c88fdea9cd1e | -10.14861 | -44.53601 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4eb2c3dc-c107-3ec7-957d-12be51a84779 | -6.59418 | -43.91856 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ec84ec25-fb05-3ea3-bb4c-9be20ab9c2b5 | -7.04438 | -42.73335 | 2025-10-16 12:00:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5694716e-7db4-3c2c-9746-71d3601bc958 | -14.77128 | -44.34967 | 2025-10-16 12:00:00 | TERRA_M-T | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 521691cb-44c9-37b3-b4a6-121b19a66eaf | -11.50924 | -44.06765 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 120fcced-2101-367b-abc3-9a610e0a7850 | -11.58369 | -44.06621 | 2025-10-16 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 031e9cde-5cd1-35ac-aa6e-503097ffa9fb | -6.58455 | -44.10886 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 0bd023b2-42b7-3432-8aaa-7933cd4ce29b | -13.96458 | -42.81727 | 2025-10-16 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| ab1da5d5-50ed-3108-8160-e5147522d1fb | -7.11433 | -44.71904 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 37d0bf87-9cfe-3c68-96a5-5b8324826ee2 | -6.58593 | -44.09956 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 214a09a5-f7dd-3eee-a20a-a6686501ff2e | -11.44379 | -44.20567 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 327a7051-08a0-3be8-b2f2-3d4a6836f426 | -13.45014 | -47.94971 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e4a2cd50-277a-3998-aa26-ce30bb4f0c42 | -6.79974 | -45.47153 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 4d5da96e-583c-3dbe-af76-c262cfcf2807 | -8.39318 | -46.25911 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6983ae2a-5a51-395f-abf1-979ccacc3679 | -14.17302 | -47.94073 | 2025-10-16 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6b267d19-1f27-33dc-ac1b-c9282d9f27f8 | -8.29923 | -43.42422 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 257.0 |
| 917ea079-d37a-3332-8dc9-73c82e2a9615 | -10.82637 | -43.93618 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b2d76a8b-2472-3de4-9737-dccad1d4660e | -6.67004 | -45.0349 | 2025-10-16 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 894667b4-3c24-31b7-b260-7e406fe8af69 | -11.47835 | -44.1553 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 76af467b-0379-35e9-a981-78540d54bbb0 | -12.86548 | -42.5721 | 2025-10-16 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fc1d5417-2c0d-3de7-ba3a-6df606d3498c | -12.26881 | -47.13017 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 556516f9-1f0b-36bb-bdb0-c465d9fcfd23 | -11.89872 | -46.80609 | 2025-10-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 723e9f48-b882-372d-ac54-e1d8fa67dfac | -9.37093 | -46.95958 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 341aaeef-b302-3ef0-a06f-fc90d07bb337 | -7.1759 | -42.19324 | 2025-10-16 12:00:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 004281a3-af6a-3fdf-b6ab-a70fe7ae7eb5 | -13.14975 | -43.37483 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1cd42224-26d0-3cfe-a121-0593bf901b73 | -7.19364 | -41.61396 | 2025-10-16 12:00:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 1bad7755-1562-3385-814b-6967f6a60a90 | -12.79333 | -45.49862 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b9a6f9c8-750c-39e7-8bf5-2758ece51aa0 | -6.74782 | -44.37954 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 01acbd47-3668-3654-a130-10252226c69b | -8.44687 | -44.7461 | 2025-10-16 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e2787d84-0c3f-395c-8460-2e58b8ef81a7 | -6.51457 | -43.70549 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b06e8ebb-07f1-3640-a3de-8ee940ea4157 | -10.60264 | -47.41133 | 2025-10-16 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| db868980-f1b8-3f2a-9395-47e9bfb8cd90 | -10.12086 | -44.599 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 79bc0393-9337-3843-a96b-7b4370e90cdd | -13.00038 | -43.06233 | 2025-10-16 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| f5324453-eb08-3529-953f-b16aed98f945 | -10.61692 | -45.23822 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| bdff9daa-9827-3b63-bb02-c26423ab5e0f | -11.42179 | -44.15908 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 298.6 |
| 184c108f-de5f-3e3f-bcfe-84d1f15542c0 | -10.72198 | -47.58619 | 2025-10-16 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1496db72-1392-3ee7-8a4a-8bb65f99da82 | -6.68804 | -44.28601 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| debdafa8-948a-388c-b173-cbb3cfee005e | -8.25652 | -44.09964 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9ae2aef7-c92f-3d65-bea1-e45c8b0fc946 | -8.23498 | -44.80252 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a838cd00-8267-3c29-b592-078b7d408a1d | -11.35701 | -45.28955 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4439464d-9ace-3f07-a206-5e4c2ccc7943 | -13.63092 | -47.86572 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 236f790a-2e60-3dd8-8b0f-895375412b49 | -7.47758 | -42.14518 | 2025-10-16 12:00:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 22a50528-d7bc-3aaf-92ab-8564646e50a9 | -8.4483 | -44.73651 | 2025-10-16 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bfafe66e-72c8-34ab-a9a8-b80a340ef6db | -10.03951 | -43.83628 | 2025-10-16 12:00:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a7b26453-35f1-3e14-9fda-e03e1070215c | -11.47081 | -44.14497 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 655a46fa-cb27-3cf6-af5a-4cdf1071aaa5 | -11.90684 | -46.81917 | 2025-10-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f48d733c-647e-3018-b7f3-eb8f5bf69bef | -8.24806 | -44.03252 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 45e261c7-3341-364d-9987-f4f9fd36ee5a | -9.28759 | -45.36081 | 2025-10-16 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6f0c4421-60b0-3eab-9522-581d4084c900 | -11.21569 | -43.99659 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c887d2ed-9496-3377-96d9-8ee189cb1e14 | -12.98436 | -47.34407 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f2c8f4d8-886b-3837-b1ad-66544bf88a07 | -13.93258 | -43.50046 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de8bb77c-9be1-3f10-95d3-2c0f9ef9d75a | -7.11287 | -44.72906 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 01cf2c5e-add4-31fe-a555-859a42ecf2b0 | -10.12226 | -44.58957 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| f54993f4-91c9-38fb-b6e8-47827a812578 | -12.3069 | -45.60255 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f9ec28fd-161b-36a8-a0f6-c6d3dfe942ed | -9.34453 | -46.94883 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f5a3a476-49d4-328e-8ae8-011a6bc19799 | -6.76926 | -42.8469 | 2025-10-16 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 98e6ab13-2da3-3446-9384-51ebbf7c7ff7 | -15.3406 | -41.06335 | 2025-10-16 12:00:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| babe369b-f606-3cc8-895c-4c34f5c4a4b4 | -12.67169 | -43.43174 | 2025-10-16 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 396a0b86-ddee-3782-b0a3-3f8c8bd1617b | -10.51174 | -43.37296 | 2025-10-16 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README87.md)
