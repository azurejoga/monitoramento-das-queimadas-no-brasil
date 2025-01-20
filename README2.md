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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fe5e0ce-7488-34d4-baea-cf9f26776be8 | -12.66875 | -38.56926 | 2025-01-20 03:44:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 47b3eec8-bc01-3cc2-b599-37ee7f07d3c3 | -11.03113 | -45.05098 | 2025-01-20 03:44:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ef8be27-ef0c-37a0-a16d-c8a2d24c78c7 | -10.69483 | -37.04902 | 2025-01-20 03:44:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2c0d37ae-5e31-3a9d-8e2c-6aa2f2a0279f | -13.50909 | -44.12074 | 2025-01-20 03:44:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fdded64-d5f1-3cef-890d-4c4181190b11 | -17.84196 | -40.07483 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 44e0d24b-d3ee-3057-8701-7f0f6330612a | -20.90188 | -43.82118 | 2025-01-20 03:46:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6484d7c8-78e0-334b-81f0-e1f87367bf4d | -16.3476 | -43.69763 | 2025-01-20 03:46:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2909e441-652c-328a-832a-b2ae86846e04 | -22.78873 | -41.98708 | 2025-01-20 03:46:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1af4a9ca-4dd4-3519-acc3-43626e746762 | -17.25847 | -42.91379 | 2025-01-20 03:46:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4216497c-8258-3648-804c-3847752f897d | -22.73917 | -42.95806 | 2025-01-20 03:46:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 648b3a44-0d08-368a-83ba-cb7685ecd2cd | -17.84474 | -40.07938 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 78e52f2f-346e-34a4-85dc-46f327d81f63 | -17.84267 | -40.07584 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 57e97d39-c825-37da-aedc-f3e1f54d309a | -17.84541 | -40.07545 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 53bf7eef-197d-3d6c-b8d2-0fb5ea2dd919 | -17.84129 | -40.07877 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 13bcd106-1b57-3efe-b357-6da6bc8934ea | -19.71702 | -40.35307 | 2025-01-20 03:46:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7278d2d4-cbe4-338b-9d6a-38a759750611 | -17.09568 | -43.80595 | 2025-01-20 03:46:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79933961-435f-3abf-8d01-0bcd513f693e | -17.84202 | -40.07978 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5a4a5d5a-6b57-38f7-b38e-d07cb6cca237 | -20.34889 | -40.36249 | 2025-01-20 03:46:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 65264816-2210-314a-ab7e-50d42eebe6fc | -22.67539 | -42.85419 | 2025-01-20 03:46:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 575fe233-1e03-391b-9f37-88065029c191 | -22.67905 | -42.85498 | 2025-01-20 03:46:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 107c998c-f5a9-3e43-976b-c159ee7e89eb | -16.68007 | -43.88285 | 2025-01-20 03:46:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a72638bb-6ff2-3952-9c69-5ca35bc9a46a | -18.04 | -39.92443 | 2025-01-20 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62f0eb66-b71e-343b-8b9f-599158491a21 | -19.83995 | -40.08198 | 2025-01-20 03:46:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad55030f-6382-37e2-9036-85b65335490b | -23.47842 | -46.31718 | 2025-01-20 03:49:00 | NOAA-21 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03f2aef4-a745-3262-b07f-bb155049595e | -23.34039 | -46.77376 | 2025-01-20 03:49:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 33995ea5-6794-3303-a220-8a5d2577344f | -9.00544 | -35.54683 | 2025-01-20 04:08:00 | NPP-375D | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f42ecf3-e207-383f-9988-ed05fc1e0e4c | -5.70419 | -45.84362 | 2025-01-20 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15281da3-f764-3dba-8780-5e6737964db3 | -10.69555 | -37.05004 | 2025-01-20 04:08:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7778993b-eca5-32a4-accb-74dfac576996 | -7.93671 | -35.26341 | 2025-01-20 04:08:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c8ce1f2-2fba-395b-9314-c6812c9d99f3 | -7.85897 | -35.1887 | 2025-01-20 04:08:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4bc9448-0ef1-3b5a-a6ae-5c615d5c53b2 | -16.3498 | -43.69541 | 2025-01-20 04:10:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e6df2c8-7030-33b8-b103-0e4133e22cba | -11.75086 | -37.98812 | 2025-01-20 04:10:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9183b19d-b8b1-3a93-874d-522b211635e6 | -11.74685 | -37.98751 | 2025-01-20 04:10:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d6af5a4-e96c-3f92-9ea9-9e89d4f8d5f7 | -11.05427 | -45.37954 | 2025-01-20 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4122ceb-e1c1-3da5-bc5c-ac94d89aa799 | -12.66939 | -38.56704 | 2025-01-20 04:10:00 | NPP-375D | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6b38010f-c29f-33a1-a438-27868c5515d0 | -12.35028 | -38.19638 | 2025-01-20 04:10:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| db6f082f-55de-380c-b11f-b867d2461077 | -17.00665 | -49.78196 | 2025-01-20 04:10:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f779ff56-4ab6-329e-a08b-f48657d1475e | -17.0934 | -43.80382 | 2025-01-20 04:10:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea892848-2bd8-386d-9a59-1e9bae0205cf | -11.03212 | -45.05259 | 2025-01-20 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef65770b-08ba-32fd-bb63-4a11d6c8b563 | -15.07829 | -48.94535 | 2025-01-20 04:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e282ce1-a65e-35b1-9083-672d7db842f3 | -15.56944 | -47.85629 | 2025-01-20 04:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 872098e2-c2b1-38fe-8692-16bc9883357f | -11.23439 | -40.37886 | 2025-01-20 04:10:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8838ee2-b1f2-38e3-81f3-05800a3810c7 | -13.5084 | -44.11833 | 2025-01-20 04:10:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 395e453e-9745-3836-80d0-d9ebfcf9a039 | -11.05075 | -45.37892 | 2025-01-20 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aff4e848-53a7-3e43-b690-7820ccec5859 | -16.68141 | -43.88352 | 2025-01-20 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fc6d403-4b78-327e-87a5-72b5b738e310 | -11.03275 | -45.0487 | 2025-01-20 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b9c514c-0abb-36f8-8645-0a21e54ead58 | -11.05008 | -45.38293 | 2025-01-20 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9c68084-ec9e-3d9c-a284-d4d4f52abcf6 | -20.41628 | -43.55348 | 2025-01-20 04:12:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3945b5c4-9374-38db-b797-668beaf4d18d | -22.6764 | -42.8554 | 2025-01-20 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 01556d89-dec5-33ef-b98e-2f379d8d6c22 | -23.33786 | -46.774 | 2025-01-20 04:12:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5fcee96a-4ab2-3dbf-bed0-18fc6ee3f8d7 | -20.40651 | -49.84092 | 2025-01-20 04:12:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c601eec-b5fb-32aa-a63e-c61aa439c38b | -23.4057 | -46.55754 | 2025-01-20 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 867fd515-05fb-34c4-ba64-1a2f86677450 | -20.34833 | -40.36094 | 2025-01-20 04:12:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1ee6f582-ff36-3363-b668-0601673ef347 | -23.98176 | -48.9165 | 2025-01-20 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2dc2f629-0de3-35bd-9120-c6936af0031f | -23.98532 | -48.91723 | 2025-01-20 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af19660-b59a-385b-ae25-105896ac2a43 | -5.70356 | -45.84423 | 2025-01-20 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b34c3e60-8228-3465-9896-aa82b7a2e190 | -8.06558 | -34.97375 | 2025-01-20 04:29:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e692a366-e5d9-3d9c-9600-ddd796e8dfb9 | 0.89637 | -60.09801 | 2025-01-20 04:29:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5bf24495-7b99-3fb2-a21b-32ddde21adf6 | 1.36012 | -60.03219 | 2025-01-20 04:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2542091-6ffe-3c0d-be60-88dc676c2b70 | -8.06474 | -34.98033 | 2025-01-20 04:29:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 00709305-e254-3f6c-ad9c-7cdcc6b48e29 | 1.35903 | -60.02514 | 2025-01-20 04:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f71fc46-aa07-3601-8948-103c0715cf22 | 1.36256 | -60.0305 | 2025-01-20 04:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f453784-7cf3-3ec9-a778-e944f475bd37 | 0.80844 | -59.90474 | 2025-01-20 04:29:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e60e566-acd1-37ba-af59-ba37adcb52a1 | -1.60836 | -45.99814 | 2025-01-20 04:29:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d375446-24f1-34f5-923f-95b609cf6921 | 1.35539 | -60.03169 | 2025-01-20 04:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3bfbb69-361e-3fce-9cd3-92f15642ec1c | -11.75189 | -37.99186 | 2025-01-20 04:31:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd0a9024-8fcf-36f8-b4c3-2ca002e88897 | -12.67098 | -38.56724 | 2025-01-20 04:31:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ced58cb5-f221-3785-8f3c-7b5d61f33faf | -11.7477 | -37.98868 | 2025-01-20 04:31:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c31ccac4-5713-350c-bfe0-e62a0fbc7871 | -11.05312 | -45.37752 | 2025-01-20 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03d9ee39-5bc1-306a-bdd1-4f9344157dbf | -12.67047 | -38.57163 | 2025-01-20 04:31:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6aa67125-2e6e-3718-b774-c706202c1a5f | -11.59028 | -44.86749 | 2025-01-20 04:31:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f2f3c46-1463-3725-a0f4-09a5761164f2 | -11.58646 | -44.86691 | 2025-01-20 04:31:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b11c925-bc21-370f-aa23-af4341300c45 | -11.74587 | -37.99102 | 2025-01-20 04:31:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 763875c5-56ee-3ec9-b856-5fb508278a6c | -17.84322 | -40.08191 | 2025-01-20 04:33:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| e9918724-49b7-3501-9be3-ab9cf6663754 | -16.34848 | -43.69656 | 2025-01-20 04:33:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50af2a1c-d990-3091-b2e8-9faf9d10bbbf | -17.84365 | -40.07779 | 2025-01-20 04:33:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| cb249e70-e381-34ea-9782-b185b6f2ac54 | -20.41516 | -43.5546 | 2025-01-20 04:33:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3d5414c9-2b87-3910-b5eb-b05baed842df | -15.08757 | -46.96114 | 2025-01-20 04:33:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41c7cc5-eb47-3dcb-8c39-d5948070356f | -15.26373 | -51.47918 | 2025-01-20 04:33:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68342498-2177-31df-b15f-47ccc29a84f2 | -15.09113 | -46.96167 | 2025-01-20 04:33:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b45291-287d-3c62-b5c2-c6fe8d9f2e4f | -15.07744 | -48.94375 | 2025-01-20 04:33:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ad584b9-a64c-3eda-a93b-84d858bafc8a | -17.84408 | -40.07365 | 2025-01-20 04:33:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| bd51d342-b0c8-35e7-ad78-9b2fcd36726a | -22.67659 | -42.85548 | 2025-01-20 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 849d40c3-f053-3939-89ff-01e4c46c3768 | -22.67691 | -42.85235 | 2025-01-20 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fda04b33-08e8-3012-b691-436ef1360bfd | -23.98331 | -48.91807 | 2025-01-20 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc0b4dc4-d18e-3570-b6bf-d9f10ffe9e3c | 3.7483 | -60.63516 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dd1e932-cfb1-3b99-b45d-7440130422ad | 4.47681 | -59.96521 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea97d9c7-bba4-3ea5-aba0-384fd38f5874 | 3.77529 | -59.91881 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcbc5e47-2816-338b-a3db-30ef22d792af | 4.13796 | -59.99791 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158d63f2-ae59-3e3e-b6a1-14c4b878f071 | 5.00234 | -60.30225 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f54a848-9da4-311e-812a-7f49738fce1f | 4.94893 | -60.53562 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19a016d9-8833-36cc-8ba1-e133c97c291a | 3.69962 | -59.77561 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd89a61-62b5-3206-b042-4fa0c484e3a4 | 2.90312 | -60.77577 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bc1bd6e-5fd8-3f8b-a981-a73e5a6d4c9f | 3.73508 | -60.66462 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6efae0ab-3ece-3a59-984f-1f46494202bf | 4.52151 | -60.68862 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c60318a-5f15-38df-b932-547950c18798 | 3.41385 | -60.42577 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4ae3e5b-27bf-3f73-a39c-eb103ab67f07 | 2.87997 | -60.76366 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56d2d536-8488-3586-a20d-def3315f081d | 4.49204 | -60.70657 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e92f83c-16ff-3fd8-9386-d2bfc2c4bf57 | 4.02922 | -61.09189 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68f256cb-01ec-376b-9b36-4f7e3cbf3e5b | 3.24582 | -60.95009 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README3.md)
