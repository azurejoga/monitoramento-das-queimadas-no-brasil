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
| 3a0f7663-4b1a-3d2c-a2b9-c8c89065dde1 | -11.92819 | -44.41911 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc03056c-2a9a-3229-935d-584b43a1d249 | -12.04185 | -43.51468 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 653c7774-2273-3702-939c-8d6b5726742b | -7.11792 | -42.72825 | 2025-11-13 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3190659-48a0-37d7-b2f5-d08b234fb905 | -10.79984 | -43.78426 | 2025-11-13 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47bcddb6-1499-3ab7-8851-a20091908c05 | -7.98729 | -42.27319 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86ff3ca5-0841-3d00-bb05-9291b68d0d80 | -7.37016 | -42.48319 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6783beef-8ef2-36c8-9a4e-51b874c24417 | -5.36001 | -46.75856 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8c1c725-7ab0-33a1-96a9-fc9521ca51b0 | -7.78321 | -43.79894 | 2025-11-13 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 743d9cad-db34-3756-9365-8efe047c6ead | -7.52898 | -40.08392 | 2025-11-13 04:14:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3f97ca4-26f2-3d08-85aa-a3f68edae1c4 | -7.13249 | -41.88319 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 29f9823c-cb08-3345-8de2-5ca702cc444e | -11.79879 | -44.20431 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d176cf5e-6fc1-31f9-a718-c1561c2d9c68 | -10.52348 | -45.10311 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58551e06-9049-3f9f-9f66-4f9ea94e314b | -7.11846 | -42.72478 | 2025-11-13 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32b0517f-36a9-34af-a8a9-75e9bf3641ea | -5.44905 | -47.69413 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 338d4dbd-1ec5-3f9e-a202-1bcd53406ed3 | -10.33926 | -48.06634 | 2025-11-13 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 176a483f-df68-3bc6-8691-ef01d172b3a9 | -7.45952 | -44.74089 | 2025-11-13 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2da9c07b-d141-3937-8344-6d2e1e4f29cc | -7.16656 | -39.521 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5d9e7cb-33e3-3dc7-bfe9-3c8912d5c704 | -9.15946 | -43.15796 | 2025-11-13 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6971d315-acd2-3b0a-8a7c-77250c387f18 | -6.16187 | -48.05637 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d04c0239-99d3-39e6-aacf-c75c23475788 | -6.54518 | -43.10456 | 2025-11-13 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f58f4a-d8bb-37f1-ba2b-f3bb2dcde2b8 | -12.66391 | -46.75263 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ba285a67-69ab-3486-bdcf-ac5a2a471c3d | -9.85913 | -44.57201 | 2025-11-13 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19cc29df-eb5e-3a58-b843-aed905365c4d | -9.08132 | -40.08167 | 2025-11-13 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2e263f05-5657-3249-a84f-9cd586962d0f | -7.34387 | -38.59813 | 2025-11-13 04:14:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fdfb01b-cca3-326b-941e-a6f4b3ed9392 | -8.55356 | -48.0205 | 2025-11-13 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4f4953e-1e30-3c2e-8bc9-90c3192bc325 | -12.65069 | -46.74638 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 42c5ff0e-a58b-31b6-a713-a9366d5c1b3a | -9.32686 | -47.84161 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5dcf9ba-6411-3763-8b69-a58d98be74df | -7.80031 | -42.62548 | 2025-11-13 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f98d0669-2f56-3c26-9094-38747f047cf7 | -6.87743 | -42.8531 | 2025-11-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ea53ad9-cbdc-3bef-9c6b-76485b3b9c66 | -6.88073 | -42.85361 | 2025-11-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6ae613f9-d87c-34a9-bfc7-1bd764ab6638 | -10.37389 | -45.05679 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61a6a6fc-68d3-3d26-bb6a-c60e47e25a37 | -7.4152 | -42.76104 | 2025-11-13 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96b7a904-768e-3f42-ab29-31bec074837b | -10.72697 | -44.05523 | 2025-11-13 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9d71054-67b5-3f60-8961-1822df7a5849 | -10.92581 | -44.62639 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98c5fbf9-2e64-3b6e-bf52-a705233d6532 | -6.15781 | -48.05576 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dbc3c50-404b-329b-957d-fec21f2d55e4 | -6.47169 | -43.95823 | 2025-11-13 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 894ee60a-4ac1-3441-9596-973c1aebdc5e | -8.7451 | -44.23691 | 2025-11-13 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 951d4402-4f8a-3adb-ae09-56f7061dc828 | -7.10585 | -42.36663 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fb1d4dbe-4148-3b8b-aff0-c038aac27e33 | -10.62722 | -45.00621 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c441b241-8022-3880-bf7d-947cde9ecc95 | -5.88624 | -46.4416 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dcb2af8-e368-3ce8-9ec4-4993bddbf5eb | -10.62229 | -45.24484 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 588cf4a2-68a6-3a1d-a135-13ba3d943e1c | -7.13077 | -41.87197 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a3b6658f-3df2-321e-b5f4-21943e64d815 | -10.66951 | -45.10146 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94b19ca1-0bf6-387a-90b8-f37f9db2390d | -11.836 | -47.65234 | 2025-11-13 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351aaab0-66b3-32b3-8cb1-a160c0377375 | -6.145 | -48.0577 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35a07696-9f68-3476-a90a-d33aade1668a | -5.38647 | -46.76268 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7691eb0-1af9-30f0-b4a4-9858784621bc | -13.33418 | -43.17671 | 2025-11-13 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b317d981-127e-3fe9-9c9b-33dec029855b | -7.08082 | -41.57727 | 2025-11-13 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 624c5e4d-c44a-3ce8-8761-bdd262b0377a | -9.44715 | -44.87292 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f33d2119-9663-3f3f-9f04-e1694dd57e26 | -12.65005 | -46.75026 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 647468f8-cf5e-3604-9c4f-37178466a8c7 | -10.37446 | -45.0532 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d8e727a-6faa-3c9d-b0ff-205fee8571e2 | -12.21302 | -44.94236 | 2025-11-13 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3a0df46-781b-39d0-a536-86fc730c7600 | -7.06228 | -41.58562 | 2025-11-13 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 841dc0b4-171b-3c96-bd57-e541e03f4db3 | -7.55605 | -47.24995 | 2025-11-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f97c9e7e-9f93-3735-9feb-f3feb805ead9 | -11.08449 | -44.86985 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05d5cdac-3a0c-37fa-a083-97d92bd62608 | -10.84855 | -44.98399 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42bae846-00d5-32b5-b325-0cd960226113 | -7.22626 | -39.95413 | 2025-11-13 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8bebfda4-7cb4-3dc3-98ef-af8ee5512224 | -6.16248 | -48.05274 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34a4dba9-91a6-3ed2-b443-8a8a11fd07b1 | -6.05655 | -46.91705 | 2025-11-13 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0ed4ef2-aaef-300a-b0fb-041db1a468e2 | -6.48624 | -48.368 | 2025-11-13 04:14:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e9c291c-fa41-33ff-8f51-8d350d61cee8 | -11.69912 | -43.88247 | 2025-11-13 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb28ee74-80ff-325f-9667-84296f318321 | -7.47605 | -42.56748 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 455e080e-ecf8-315d-adb9-0f6aa1a32d28 | -8.64447 | -45.47443 | 2025-11-13 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de810dcf-d93f-3893-8fcb-4d59e9e4005b | -5.28208 | -49.27959 | 2025-11-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828a3aa0-656d-395a-ba34-648014257813 | -6.15437 | -48.05151 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b32f468-8cd9-3a93-a079-fbd5df0d9ab8 | -6.3148 | -43.81084 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6375b906-8a84-3992-8a82-c02c9aacee93 | -6.29078 | -41.74256 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6918b6b6-d919-3c15-be31-ffe0edcb4fa7 | -12.04572 | -43.51167 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c389b8d-c923-3c94-af99-180381507763 | -9.6425 | -44.54385 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc2e2b33-9d6f-3114-b36e-a9a88ead8846 | -5.19009 | -47.73677 | 2025-11-13 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c12faaf-9efd-3f88-a6ba-e7a215e87fb7 | -7.1296 | -41.85714 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61a12bdc-b2a6-30f8-9f10-b3a2f3f2a39d | -10.54941 | -44.83297 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3260dcd4-018e-363d-aac2-b2fc4163dcce | -6.28744 | -41.74205 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 277a17d2-16e2-39e7-82b8-41812f1b9062 | -10.32499 | -44.27303 | 2025-11-13 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b5256b-4ffd-3b83-b3f2-f9955e80ad72 | -6.87137 | -44.48422 | 2025-11-13 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4254cdf6-4cb7-303b-9e48-21f7e9432248 | -9.48356 | -45.26021 | 2025-11-13 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 916317e5-e172-3262-ba08-08b1c18d35e9 | -7.248 | -39.40552 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c6554b9-8466-3b53-94fc-971cbe6ec703 | -10.82245 | -44.65639 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58414e71-631c-3ff1-a3b6-ffd9aa285b90 | -7.96799 | -38.28089 | 2025-11-13 04:14:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b482124-0fef-3c97-9e9d-cf2f07ab5282 | -5.66069 | -46.28341 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afc2c626-73f2-3366-afe2-ea77dfd2d0c6 | -6.8975 | -42.08619 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3858632-d1ff-3c96-b8dd-74333ce085fc | -7.28214 | -39.35571 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 48739873-6471-3e05-a592-46e113b21ef1 | -5.57861 | -47.10692 | 2025-11-13 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 463ad2b6-dd8a-38d6-9c40-347110cc74a7 | -6.59739 | -44.23912 | 2025-11-13 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51a30514-b1bb-3efc-aecb-f289c6763f97 | -10.35794 | -47.70449 | 2025-11-13 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c29934c3-d2e4-3675-9729-08c38119d955 | -10.55274 | -44.83352 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae6ccb9f-830d-3e94-b0db-3fa3171343d8 | -10.75487 | -44.91042 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88932914-15f0-3669-8fca-1630ffc138cc | -7.82135 | -41.77931 | 2025-11-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b8c711ca-e89c-3647-8ef4-4b5904d8c543 | -12.66819 | -43.32837 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c75d68b-9db6-3e6c-8ed8-6ddbba61d67c | -7.20435 | -42.52113 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e25ae656-2a0e-3852-9f24-ea38bd2381c9 | -5.68221 | -46.00977 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25db1304-20a4-3d34-8c59-2903d49ddf89 | -4.82717 | -50.62366 | 2025-11-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a466bdda-e0c1-3981-bcf4-d23f392485cb | -7.25878 | -39.43506 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e1a4786e-86fb-38d4-b771-079358e557c7 | -9.64509 | -44.54831 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 780e1e32-4d72-3158-acc4-61a99b19293c | -11.59758 | -45.11028 | 2025-11-13 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af00ca19-2994-3b8d-9950-76824bfc182f | -5.45305 | -47.69476 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d76bea-2970-3d9b-93e8-e4187ce1a8d6 | -8.30848 | -43.64124 | 2025-11-13 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c5f682c-6515-34cc-9f41-27d9ae5e9426 | -8.41334 | -44.03203 | 2025-11-13 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bec1507b-42f5-3dd9-90f3-2fd79a49a385 | -5.76025 | -46.5225 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e824d562-afef-3fbc-9c4f-5649267f148e | -7.41466 | -42.76451 | 2025-11-13 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
