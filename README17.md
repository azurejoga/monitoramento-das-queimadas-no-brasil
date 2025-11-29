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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a9514f-012e-3a0a-b581-781faee2427e | -5.35242 | -44.88778 | 2025-11-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb81ab5-92b4-3c8c-8f96-e5e8aa602212 | -5.11942 | -41.11536 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 735631c8-a379-3e87-8853-6935b1967548 | -4.42711 | -46.2946 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e0dcffa-dfe3-3f44-91e2-6543044d4f07 | -3.84443 | -44.12777 | 2025-11-29 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 223d9dc9-46f3-3b4c-a4bb-9451db085a10 | -5.00453 | -38.53854 | 2025-11-29 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a237bc42-bff3-3adb-9f74-c595c5490790 | -5.26476 | -41.97552 | 2025-11-29 04:14:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6226737b-8313-34a2-92c3-52ab0307b6a4 | -6.69877 | -41.4741 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35a9a7c7-9ad1-3aa5-bc6c-2c9646305eb9 | -6.70102 | -41.4595 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1a1da370-04ef-3463-9652-1e0c4c959d05 | -5.62033 | -45.25175 | 2025-11-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56104b01-3ec4-33f4-af66-329b3fa85ec6 | -8.04646 | -43.13252 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0b56532c-f4a3-3aa0-b22a-5002d3521ea0 | -4.25754 | -46.36456 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee794d0f-33cc-3fe5-9968-9fbfd6bf5ae7 | -4.89544 | -40.99979 | 2025-11-29 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14e13c82-e5e8-39f1-ad63-343b4175f91c | -8.16996 | -43.19089 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58f931b8-6e98-3847-9de4-0cc9504cfb1c | -3.81377 | -46.56263 | 2025-11-29 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59eeb83e-30b2-30dc-aae7-72d50844effb | -8.79764 | -40.43105 | 2025-11-29 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f16e2042-f3a5-3fbe-b54a-6c835343cdba | -8.03985 | -43.13148 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d78f4dee-7f1c-38ea-a11c-56070681aae6 | -4.16965 | -42.73803 | 2025-11-29 04:14:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fbefb280-8859-3194-b4ef-62a6b89b974f | -6.70951 | -41.472 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88ef181a-fdb0-3508-a842-14288c40e8ad | -4.74164 | -41.99379 | 2025-11-29 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c73f066a-4312-30c9-ba35-bd7a3e4e202a | -9.89574 | -36.13562 | 2025-11-29 04:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 10610992-0f81-3130-982f-ef711090f47f | -6.60232 | -43.68718 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d4c6eb0-d853-3f60-b4b0-cc509245353d | -3.22425 | -50.31987 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a24421c-9029-3fc4-b247-1295ee4cd160 | -11.55481 | -42.18233 | 2025-11-29 04:14:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eabe5dec-f57e-377c-9d42-4cd32c5ada9c | -4.68986 | -44.66175 | 2025-11-29 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 845c1cc5-5c5f-3546-abd1-3f90ec0524db | -6.70046 | -41.46315 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 322bf423-8adb-348e-99c9-f0b686e335bf | -7.61245 | -47.02172 | 2025-11-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db4170f-7d23-3312-9883-8b112e6eaa03 | -8.48123 | -44.43277 | 2025-11-29 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca4b7630-7f84-3804-9af5-198de252ece6 | -9.49866 | -40.65018 | 2025-11-29 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9082a979-a188-36a2-a6f6-eeebfc528f47 | -4.74094 | -44.43208 | 2025-11-29 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57a61c6a-d99d-39ea-a5af-11a850b2c0dd | -6.46582 | -41.73056 | 2025-11-29 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26df51f6-4da4-335b-970a-27ae83f75143 | -3.55467 | -50.31198 | 2025-11-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 478e64d1-f0e3-3b1b-b82a-6e6971122a12 | -11.02211 | -43.96068 | 2025-11-29 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1214ee6d-3f12-3cda-a985-802dc6ae947e | -4.94102 | -41.14037 | 2025-11-29 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 548993ec-5fa0-3349-92fe-5b0617cbf252 | -7.22714 | -42.19024 | 2025-11-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25bd398f-ad03-38b7-91be-532a6e266278 | -8.036 | -43.13443 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f8eb3013-d2f5-3448-a706-2ff74cc185b3 | -6.71639 | -40.8123 | 2025-11-29 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e870ed3a-3385-3163-8331-eb36fde74346 | -5.26983 | -42.70705 | 2025-11-29 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c3ec73e-9c37-31a7-a909-8bd7f3db0e92 | -3.22917 | -50.32066 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c61c7140-9350-3cce-a89a-93824d0dbdcf | -4.51187 | -44.16931 | 2025-11-29 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5458745-0f28-3af8-a32c-9b6d9fb903bb | -8.25764 | -35.82955 | 2025-11-29 04:14:00 | NOAA-21 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94d75566-691e-39f9-82cf-7290231689fc | -5.73845 | -40.43949 | 2025-11-29 04:14:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b59df8e0-5bef-3af1-a03e-bd2540988488 | -5.07346 | -40.82265 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 911e74cb-5779-3f81-9311-53ba33d08cb1 | -6.73116 | -39.30223 | 2025-11-29 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bb901b9-a198-34af-8482-7f6668201736 | -3.1744 | -52.42167 | 2025-11-29 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b3966ea-8aa6-3f88-ab2f-2a72bb8d7a26 | -8.14068 | -49.5108 | 2025-11-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8711c97-3da7-31c0-8a73-53f1e396b004 | -4.96315 | -41.19924 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca3c5089-a6d1-3bae-ad38-42dc8dd07b9a | -6.48416 | -41.95981 | 2025-11-29 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eda14d85-7ba8-39e1-bb5f-6dfe37e8f703 | -5.36597 | -43.02615 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e00e2f05-fc73-3718-988d-5e98a719c25d | -8.17772 | -43.20633 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c00ccd6-59ca-3bbc-962d-1ab86926952e | -4.93575 | -43.46859 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0da6af42-f85f-31b8-9ded-b120b44c0f30 | -6.38829 | -42.22918 | 2025-11-29 04:14:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c53db62d-6ed5-35a7-b93c-f900e8d81968 | -4.16647 | -43.75241 | 2025-11-29 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22c70760-51cc-3ada-9c3b-205a8c4d373c | -5.54618 | -37.50706 | 2025-11-29 04:14:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d23cb517-bc6c-35b1-8be1-e1499f7a5064 | -4.85088 | -38.73974 | 2025-11-29 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0027c3c3-ee2b-32e2-b8fb-a7f5f9dc5544 | -9.42662 | -40.35072 | 2025-11-29 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14921ad9-ef69-33db-aaca-35de5a832122 | -4.13293 | -43.83436 | 2025-11-29 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be7eb8e3-dc85-33f3-9474-5d490d8d8266 | -6.97953 | -42.47196 | 2025-11-29 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb0edb1f-d5cf-314f-9b79-5a92af81fcc1 | -4.95695 | -41.19457 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49514176-0120-3d30-b7c4-19098a0b939d | -4.63532 | -43.99035 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0ff602-8ab5-36b9-a955-377e3d6a49ec | -3.11152 | -50.35877 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b5ec879-6b0c-3881-af0b-b0806f913d5e | -5.61409 | -39.72759 | 2025-11-29 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e4382cf-658b-3a93-a315-6b59e3af7c84 | -10.48498 | -47.34008 | 2025-11-29 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d55565a4-a938-395a-af1a-c7538a243ec8 | -14.48857 | -46.99389 | 2025-11-29 04:16:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f525b6f2-ac4f-3f2d-a6fd-f1fa154194ea | -16.76027 | -51.35333 | 2025-11-29 04:16:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c558c5-33f7-3951-8bbf-36edb6a96b15 | -18.12427 | -47.13221 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15236c79-542a-3233-97c8-089c26f07427 | -16.74115 | -44.15711 | 2025-11-29 04:16:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbc7ba37-45c5-3c8a-8c58-f58d5ed018b0 | -16.67671 | -46.65538 | 2025-11-29 04:16:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd7ca958-fb0b-3b50-b71c-aa8f45cef2a5 | -18.17066 | -47.24035 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caf945a3-f1e0-3e0e-9a0e-cb411e4ad640 | -12.39138 | -43.67793 | 2025-11-29 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd8e4e22-6324-3232-9d92-680361729b0d | -11.27577 | -49.4692 | 2025-11-29 04:16:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dd47aea-2730-3773-9a0b-18f7f5a693a0 | -18.13907 | -47.13823 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4449820f-8f91-3fa6-9e4a-36205cf8a51c | -18.17402 | -47.24096 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d2ea3f-72c4-36a8-9642-b76f015d6b0c | -11.48714 | -48.5059 | 2025-11-29 04:16:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 503e4b3f-db02-3ea9-b20c-4ca68b814db6 | -12.48292 | -43.92206 | 2025-11-29 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dac5fcd8-e909-321d-9522-268b9f06cd60 | -12.39247 | -43.67081 | 2025-11-29 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 357a44d9-a5eb-3602-b162-796eca27ca28 | -16.78451 | -48.85866 | 2025-11-29 04:16:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8735dd-8bc4-39f1-99c6-5a1cd281b2d1 | -17.12798 | -48.72328 | 2025-11-29 04:16:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2b7ab51-c051-3ea7-98a5-4a04032e5dc8 | -18.13099 | -47.13339 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d35ca1ed-d504-316e-b5bf-0bc1ac00d78a | -16.76371 | -51.35807 | 2025-11-29 04:16:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31dc66f1-d233-3591-9e27-b630b7e259ab | -16.76444 | -51.35421 | 2025-11-29 04:16:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8744e29a-c5c8-32ea-a691-559ff32458df | -18.12763 | -47.1328 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83741201-b75c-3ff3-93e9-c250421890eb | -16.67731 | -46.6517 | 2025-11-29 04:16:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 681d2cfe-c4f0-3233-a815-1a2c280b8ce3 | -16.28409 | -43.91734 | 2025-11-29 04:16:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d8911e-5b5d-350d-8be0-b21aeb8cfe61 | -18.59754 | -48.09888 | 2025-11-29 04:16:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ca7ec47-41cc-334a-b71d-717fa85dba6a | -18.13509 | -47.14141 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab13278a-7298-3e79-9012-b9a3efee142d | -11.48631 | -48.5107 | 2025-11-29 04:16:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b25c2382-0de8-3994-8bb2-0697f6efce3c | -11.0842 | -54.77669 | 2025-11-29 04:16:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f94b6248-bdbf-3cf8-bc75-74637ab8336c | -17.00462 | -49.1714 | 2025-11-29 04:16:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f418e6-ae28-3ba2-8b9c-99eeb878e5fa | -11.80082 | -44.17654 | 2025-11-29 04:16:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12175652-e085-35b1-8daf-fd02e7d5e36d | -15.09727 | -43.2536 | 2025-11-29 04:16:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c839946b-9a1d-3717-8099-a36e5df48158 | -17.19439 | -47.65717 | 2025-11-29 04:16:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31988e48-0f8f-3f76-97d2-c5ced8c840d8 | -18.80047 | -44.81784 | 2025-11-29 04:16:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbcb6cb3-88c3-3afa-9895-cc81263d82c4 | -15.57389 | -43.53529 | 2025-11-29 04:16:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e670f173-43cb-3774-85dc-9aab9c211c88 | -18.13312 | -47.14154 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73baeec5-a607-3a07-ac3f-9caf90c9838e | -18.59686 | -48.10294 | 2025-11-29 04:16:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0044a756-6cec-3085-9b48-f3ef78e737a8 | -16.01245 | -43.52922 | 2025-11-29 04:16:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b84dff65-e4fd-3073-aeef-0b74a2196298 | -17.75083 | -42.34417 | 2025-11-29 04:16:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26b60eba-739b-38a6-a070-e0a434169129 | -16.01301 | -43.52543 | 2025-11-29 04:16:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bab456b0-37a3-382f-8b32-0b8fe416ba93 | -17.41141 | -49.23235 | 2025-11-29 04:16:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6197123-c83a-388e-943d-8674609320bc | -15.43781 | -43.27065 | 2025-11-29 04:16:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
