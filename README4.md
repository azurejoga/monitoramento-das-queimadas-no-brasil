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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a95fc0c6-fcc6-32f9-a466-f07dbc1811d0 | -8.11158 | -43.12093 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad085842-f657-3c4a-a690-1e256a84ee8d | -10.64709 | -44.40049 | 2025-04-05 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8ae0bc9-f958-38d8-849a-2f99a56d1cd4 | -5.94051 | -44.35769 | 2025-04-05 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4553742d-d385-3477-949e-8870cd57fec4 | -10.57682 | -45.13454 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64b577a4-9c8d-3fa9-86b8-ec7d30bcdef7 | -10.57283 | -45.13777 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7eeb931e-595f-3d4c-9545-38765c885c2a | -8.11093 | -43.1252 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71a92857-9940-3c0b-9e13-60a32438438a | -10.5734 | -45.13402 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| be9ec0ed-8adf-398d-9d02-9def6fbdaa10 | -8.10366 | -43.12407 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1c269888-ab65-38f7-8915-012aa1d3a0cb | -10.64643 | -44.40107 | 2025-04-05 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc681cca-db36-3dcc-81e9-32ca844375cd | -8.10002 | -43.12352 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2164c623-66c4-30de-a61b-647a14e7fcec | -13.43341 | -41.76737 | 2025-04-05 04:25:00 | NOAA-20 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3b6a6c45-a2bc-3d6d-bed3-7d38bea79cdb | -13.43723 | -41.77123 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 74fcc915-16f2-3a5b-8784-bfd8d17b70ef | -13.43625 | -41.77859 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a218e52-7e14-3c85-8e72-aa67f2d84199 | -11.26569 | -52.45811 | 2025-04-05 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1ce098f-436a-3ec2-9756-3d84e2bc9a1a | -13.04587 | -45.03221 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7be2a1-c2d2-3459-a74a-273edbfd22d8 | -13.03684 | -45.01569 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1caec37e-0b48-3651-94d3-ea862c273d4e | -13.03274 | -45.01913 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0905a347-4e0d-372b-bd89-53c663f86467 | -13.4416 | -41.77089 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c359e59-96f1-3d95-a724-1874821a3880 | -13.21365 | -53.2477 | 2025-04-05 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e17b5cbb-badf-3172-adb8-5697e9881116 | -13.04179 | -45.03568 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad85a10-2aed-3c70-ac94-b0d33b546cf9 | -17.7792 | -42.80965 | 2025-04-05 04:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc1e19f-d521-3bba-b2ba-75926d022473 | -17.5955 | -43.1975 | 2025-04-05 04:25:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 868c3d5c-61eb-3102-a246-afa66ecefcd8 | -13.03744 | -45.0117 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d97211d8-b48c-30f1-9c6f-e73ce32ea940 | -13.04498 | -45.03317 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c5637bb-45f4-3f03-be10-3d77df12a352 | -13.03625 | -45.01965 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8cb14a1-ca34-3f78-a084-c9a91a9f78de | -13.03393 | -45.01119 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5193bfcd-21b0-30af-81ff-98d52fd751fc | -13.48387 | -44.03187 | 2025-04-05 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d546ffd-8a06-3cd3-b846-d3bd61057b6c | -14.12106 | -41.67814 | 2025-04-05 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7da8d269-1429-3f15-9a56-08fbbb61c912 | -14.40542 | -45.87085 | 2025-04-05 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a558f1-2771-3df2-9fcd-a13cca5adf12 | -14.406 | -45.86701 | 2025-04-05 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f1e054d-3f59-3aed-8a69-f1ca5894dc57 | -13.04237 | -45.03168 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 833b2b84-5d75-3aea-a4e4-f337362613c2 | -13.21296 | -53.25161 | 2025-04-05 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039c81b1-9c2b-3ad0-a0c1-5c5ab9caa524 | -13.04148 | -45.03265 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31ed5299-27ae-33d9-a7e8-9594ee0aa2f4 | -14.38482 | -45.8913 | 2025-04-05 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb7276de-1491-3d15-bbc5-fd7247564bd8 | -13.43188 | -41.77896 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7de885cd-802c-3dc7-927b-656f13f724c0 | -13.04035 | -45.01619 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef2127c-71ea-3a41-bee9-d4aa7552f855 | -12.06375 | -46.98605 | 2025-04-05 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fccafa0-f56e-3826-894d-5cb5646981ea | -13.43575 | -41.78233 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e30cea04-6098-3bf0-9edb-10aaa6615b0a | -13.43772 | -41.76754 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5b2afc83-cb17-3ff6-bfb6-6a42d361707d | -13.43525 | -41.7861 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9c0ed22-15cb-37ec-b713-d4798e946ba1 | -13.43674 | -41.7749 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 9dba8ceb-b373-3ebe-a160-74a44437c097 | -11.26163 | -52.45739 | 2025-04-05 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77226cc6-2e0a-3c62-83cf-59a3cf0069b7 | -17.77961 | -42.80897 | 2025-04-05 04:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb2e3df-f3aa-3ded-8c5d-7a99f1740a8a | -13.43042 | -41.78989 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a13d6cb-528e-3914-9d03-49fb5d2e7564 | -13.44062 | -41.77823 | 2025-04-05 04:25:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44a33dda-4be6-3c08-af77-c3c2616dbe17 | -13.04438 | -45.03716 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 061c2b78-bfc3-320d-b6e1-d55f40cf5e24 | -13.03333 | -45.01517 | 2025-04-05 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f706ca-639c-358f-aaab-ae7d12e42220 | -19.72351 | -49.7719 | 2025-04-05 04:27:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37e6d109-e725-36e1-a01c-b312d174a10a | -22.16027 | -56.31719 | 2025-04-05 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff72f8d4-9406-3c61-854f-aecfeeb6553d | -21.62423 | -48.7537 | 2025-04-05 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 262e300b-708b-336c-b66a-b35d323ea654 | -19.84014 | -40.54976 | 2025-04-05 04:27:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 209602cb-8e79-363a-a4e8-e603df7a5ec4 | -20.83502 | -47.75963 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f0a10e69-a741-3456-939f-f2b6a578bda6 | -20.20434 | -55.26332 | 2025-04-05 04:27:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7bb5688-0ac3-3e5e-8177-b85bf1185373 | -23.59495 | -47.43729 | 2025-04-05 04:27:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a88bd26-6aac-34d4-8d5f-936a911f4d6c | -19.72683 | -49.7725 | 2025-04-05 04:27:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0bbc39c-803c-3991-b6e9-2da498175d76 | -20.58512 | -56.04207 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe0c744d-62c1-36e3-8553-221310094ce9 | -20.82824 | -47.75846 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 096d78ac-62c5-3e1b-9435-1bc2f7154853 | -19.84048 | -40.54673 | 2025-04-05 04:27:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 86e18ea5-67cf-39cc-b3ad-1105a3c6c3c3 | -20.57821 | -56.03123 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca947023-902c-33b6-98c1-9a540fadaf68 | -20.58598 | -56.03768 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82296657-c965-35bd-82e6-93be9521c93b | -21.62089 | -48.75314 | 2025-04-05 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a425d7a-ee41-3121-b9a3-754141e5d485 | -19.61884 | -48.33913 | 2025-04-05 04:27:00 | NOAA-20 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9bebf604-6d5a-3e90-8a3e-88237dc60e04 | -20.83841 | -47.76022 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7fe52533-e3ac-3f91-8fde-fbc8acb10bcd | -20.58944 | -56.04308 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b928d82a-f8af-3432-bda7-426a4471618e | -20.83728 | -47.76788 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 65dc3105-ce55-3510-ba00-6ac2d9fd69d1 | -22.68306 | -50.47239 | 2025-04-05 04:27:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4dba526-e725-3340-9478-09d356a071e6 | -21.12943 | -47.80191 | 2025-04-05 04:27:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e967546c-a3a4-3fe7-a61b-bea54fcc3849 | -20.8288 | -47.75463 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4ebdfb2e-d2c0-3456-8710-8ce241a47037 | -21.69573 | -50.35551 | 2025-04-05 04:27:00 | NOAA-20 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 224a38ef-3dfb-34ba-9b8c-739f43f66637 | -20.83445 | -47.76346 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dae6c342-8fd9-3e62-9889-3c668c28996b | -23.14604 | -54.89249 | 2025-04-05 04:27:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8f5c1b8b-e2c9-3331-973e-f6eb371a6a73 | -20.83389 | -47.76729 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a95aa14f-87dc-3c09-8223-ff8abaa02b01 | -23.06155 | -51.07513 | 2025-04-05 04:27:00 | NOAA-20 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d016b9f-ec80-3664-8ce8-6c51f43540d7 | -20.57647 | -56.04004 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0c6788d-72b8-3a2b-8a6f-ea5f37c53e48 | -20.83784 | -47.76405 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 23a03f31-18f5-3dbf-a341-c769530017ac | -25.32739 | -51.48076 | 2025-04-05 04:27:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83e51ce6-cc9b-3a25-8ed0-1e2ba09f7d27 | -19.83511 | -40.54908 | 2025-04-05 04:27:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 83b08e3b-b2cf-37b1-affa-64807b304252 | -20.58079 | -56.04105 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 919b88f7-92b0-3005-b339-8143aacab97e | -20.83163 | -47.75904 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 92657900-00cd-3be3-8bd9-3d923f92b169 | -19.38629 | -41.46961 | 2025-04-05 04:27:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 32dbaab5-0d12-3cc8-8faa-1dace8d78ef4 | -20.58166 | -56.03665 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46b3c953-436b-3c3d-ab9c-72aeed41dc23 | -22.15511 | -56.32061 | 2025-04-05 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a8f8da0-eb4a-3795-86b6-5cecd74982ae | -20.83558 | -47.7558 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3a0efbf0-d485-3432-a1b7-9039a68482d2 | -20.5756 | -56.04442 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c42d44bf-2930-3104-93a1-27010afc262e | -20.83106 | -47.76286 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dc32fa8c-26f4-3866-b697-2ba6256cbf4a | -20.83219 | -47.75521 | 2025-04-05 04:27:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1c6fb6a7-4448-3162-812c-f9f18cd4ae96 | -20.57734 | -56.03565 | 2025-04-05 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f709191d-7af5-3adc-b5d1-e1526f33c3b8 | -30.46338 | -56.38808 | 2025-04-05 04:29:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0ef571bc-9e8e-3b75-8ebf-fea149e0ce1e | -30.14912 | -52.02338 | 2025-04-05 04:29:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 88d83e90-1ee8-3926-9d44-d56a41f737dc | -27.68632 | -48.7514 | 2025-04-05 04:29:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1086bb8-f24a-32f2-a3ea-9c049b17e896 | -11.2641 | -52.45612 | 2025-04-05 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c92788c8-3e11-3db1-83bd-d576514d8296 | -13.04666 | -53.70887 | 2025-04-05 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77ce3d0-7d85-382d-b7f2-cb77ee24ac3f | -13.0484 | -53.71196 | 2025-04-05 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5209c82-eb83-3c6b-8004-3e0dad489b5d | -11.26414 | -52.45831 | 2025-04-05 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67699333-3b8a-3207-bb67-2d16c9fec09e | -15.13468 | -51.42779 | 2025-04-05 05:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0414e577-9efd-3f42-904d-c81c47e4041a | -20.82695 | -47.7559 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e9d7c679-96b4-3c66-b66e-35d13881f600 | -21.25102 | -56.02333 | 2025-04-05 05:21:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e8b597a-988c-3d44-b83f-32ef8264eef8 | -20.57624 | -56.04023 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54672acf-0e24-3835-add5-cc0450c7e443 | -20.84077 | -47.76479 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 48b7c1bf-7fee-3d31-a9d9-b6c54f43e465 | -20.83319 | -47.77035 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 21.3 |


[Clique aqui para ver as próximas entradas](README5.md)
