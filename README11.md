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
| f296031a-ceb5-32e5-a916-ad5bf67049e3 | -5.1423 | -56.2703 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0ad9e91b-4fcb-3fd2-8752-a0bb2a797bb9 | -5.383 | -56.0242 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9a5528d3-5a93-3936-b71e-8791e5d79181 | -11.2955 | -45.7087 | 2026-09-06 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 8ab01235-7ef5-3005-bf88-56d3e8e5e09b | -5.1439 | -55.9543 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ca64e6c9-a6b8-3e77-9184-976bb41792f6 | -5.1438 | -55.9741 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ec18e2b1-7d6d-3fd7-9bf1-7325a61b94a5 | -5.3645 | -56.0447 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 96ad70cf-70b4-3ffc-825a-e6bcecebf7e3 | -10.7492 | -60.7097 | 2026-09-06 03:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3e34d5cf-8d1d-3fe4-af14-7b394ed22802 | -5.3646 | -56.0249 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| cbdd821e-2c72-3996-b2bf-10a1c2d6d899 | -11.2764 | -45.7113 | 2026-09-06 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 414e7f28-e37f-3b0d-afb9-c71627ba7e24 | -14.9246 | -44.6744 | 2026-09-06 03:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b4ee0985-22f9-38cc-a32e-1864dbbf31db | -11.2959 | -45.6858 | 2026-09-06 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 69f97558-87f8-3850-8e0b-b9767e43992f | -6.6513 | -59.9642 | 2026-09-06 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b7f8c2d5-f4d1-33f0-8ee9-179afdfa77ed | -6.6514 | -59.945 | 2026-09-06 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2f504863-b02b-3a5c-af48-cd20bc254bd3 | -5.3462 | -56.0256 | 2026-09-06 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 77fa0f11-e66c-3dc6-9a94-909fecb8d65a | -5.3646 | -56.0249 | 2026-09-06 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 1875c9da-10a9-30af-8647-4d2f847ad6cb | -5.1423 | -56.2703 | 2026-09-06 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 77acf9b3-9e0e-3c80-861b-e5c45e5713dd | -6.8813 | -55.619 | 2026-09-06 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c0830cd3-f5df-396a-9aa0-8553c91459bf | -14.9246 | -44.6744 | 2026-09-06 03:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9d7ca5fc-ff50-3ba2-89b7-7583aa66401e | -5.383 | -56.0242 | 2026-09-06 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3f67c658-470c-37db-a126-f4a41e25b8a9 | -6.6514 | -59.945 | 2026-09-06 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 3e261f93-c522-3d8d-90b8-ec4766440d45 | -10.7492 | -60.7097 | 2026-09-06 03:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 459f19a1-ce69-3075-b4c7-3f8ec47b4ebc | -6.6698 | -59.9443 | 2026-09-06 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| db3ce083-058e-3882-b152-4d123cb0b538 | -5.3462 | -56.0256 | 2026-09-06 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| db4af0b3-d82e-3727-9853-5c2d8919f960 | -6.6513 | -59.9642 | 2026-09-06 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| be14ec0d-26fe-3c6d-b0bf-123f7e4d075e | -5.3645 | -56.0447 | 2026-09-06 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 875b07b6-ddeb-3122-9d1e-4ddbb4a2e841 | -3.33917 | -39.77216 | 2026-09-06 03:40:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf84e0e0-c72c-3e10-b479-b2f7dcb99407 | -3.87962 | -38.49868 | 2026-09-06 03:40:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39ea3310-e466-3fc8-8ff3-dabb7f1d2fdb | -4.98628 | -38.02981 | 2026-09-06 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94d2ac4e-0784-3db5-9382-e453f0b0a856 | -3.85514 | -42.94512 | 2026-09-06 03:40:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d80ff46d-a8fa-3591-9a9c-256189e19d35 | -4.98743 | -38.02787 | 2026-09-06 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dad50c1-e7bd-383e-a59e-52aaeaf6bcf1 | -4.99067 | -38.03063 | 2026-09-06 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46b921b2-2510-386c-8f96-06e495bdac53 | -5.15503 | -37.34518 | 2026-09-06 03:40:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d4e26c8-84c9-3ba4-bd6a-49c5cb4a7fb1 | -5.4689 | -37.33017 | 2026-09-06 03:40:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 489d36a8-c517-3a5f-af00-226f44735ab6 | -9.39528 | -40.5068 | 2026-09-06 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a07b43bb-f92d-325d-b445-1c421bca84da | -5.74325 | -43.27904 | 2026-09-06 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81974aae-f950-379d-8819-a016659e5386 | -5.73712 | -43.27777 | 2026-09-06 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d55a123-b0c4-3057-96b0-90b8b6d42ef3 | -6.33271 | -43.35307 | 2026-09-06 03:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc7227bf-6770-30f2-b7b0-aad9c42407fb | -10.70367 | -45.90845 | 2026-09-06 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bb09e7b-336d-3dbe-be78-5005f971544e | -6.87494 | -41.04709 | 2026-09-06 03:42:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd33d48c-446d-3cfc-8b06-490c2c22812e | -11.22287 | -41.86116 | 2026-09-06 03:42:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c54cc70-83da-3c19-bfb6-e0b2681c4e41 | -6.88072 | -41.0449 | 2026-09-06 03:42:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ed74338-8b83-30be-926c-677ccc989bf9 | -6.18557 | -40.87619 | 2026-09-06 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 16efcc94-54a7-3095-a11a-9d4bd1a26cdc | -10.6807 | -45.88541 | 2026-09-06 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab8fa9fe-00b6-3be9-a594-40a839bba0d1 | -7.13951 | -38.28293 | 2026-09-06 03:42:00 | NPP-375D | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dba98313-f1d9-3d82-bb03-30956576c4cc | -6.8755 | -41.04391 | 2026-09-06 03:42:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f7e56a9-fbb6-3c63-866d-09cafeda9997 | -8.31543 | -37.26832 | 2026-09-06 03:42:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| afa10ae3-eaee-3bd1-9052-ad9e644279bc | -10.68186 | -45.87969 | 2026-09-06 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b35995ba-c9c5-3db5-87d2-7c642e0a7757 | -6.18499 | -40.87951 | 2026-09-06 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a62e6257-1144-333e-b2f5-0bfddc70ad56 | -11.10839 | -38.6412 | 2026-09-06 03:42:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e15bd8a3-fe2c-37d9-92da-91c053da7551 | -10.70481 | -45.90283 | 2026-09-06 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a6d67db-bc23-3a31-8553-c80fd559de30 | -10.93032 | -38.81472 | 2026-09-06 03:42:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6540bd32-c2ac-3bfa-8100-e3b1e0d1af31 | -9.5703 | -40.35702 | 2026-09-06 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3ab72eb0-e36f-34da-9539-3aca48356fd6 | -10.71135 | -45.90467 | 2026-09-06 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fbc0816-2885-3a22-9374-c8a6a99e763c | -11.22228 | -41.86425 | 2026-09-06 03:42:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5756fbf1-e894-386f-b261-67ef61df936f | -10.70802 | -45.90475 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3011b17-c440-3cef-952d-2df21a9863fe | -11.27946 | -45.10865 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17eb66dc-47e6-3adb-bda1-046cb747c5a5 | -18.38852 | -39.95808 | 2026-09-06 03:45:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 46087269-ddd8-3155-9a47-24a62af3ac30 | -13.43054 | -41.88625 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| cb4824c6-e599-3d17-aae0-0711519df6e6 | -13.42069 | -41.88432 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66348464-351f-3819-9811-0816d90fb3d4 | -11.27857 | -45.71178 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a7a3534e-689b-3b01-a3c3-734cf38ceef0 | -15.71724 | -43.69702 | 2026-09-06 03:45:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cad9ad62-0b4a-35a0-8fb6-003d9e49b426 | -12.71652 | -43.20325 | 2026-09-06 03:45:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab718fc9-9c52-35f6-9593-36bd983517cb | -13.86295 | -44.30143 | 2026-09-06 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 878bfab8-faaf-3adb-9306-a42ce2a6103a | -11.29765 | -45.71025 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f0bb628-eed7-3d86-a9d5-669c62f26013 | -11.28043 | -45.10385 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efab2893-7888-3313-a5af-755e2818a579 | -13.43345 | -41.89782 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 98ecf4c9-57c5-3133-a85b-e1186f5e36dc | -11.28567 | -45.11028 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56759c58-0af5-32a4-b8ed-204ed96100a4 | -13.42561 | -41.8853 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ec7711b8-59e3-3b8e-a3c0-99cdbb859024 | -15.32719 | -43.65001 | 2026-09-06 03:45:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9959701-8378-35e7-8f0f-935c6bf07d6e | -11.29476 | -45.69863 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c9fe20e-bab8-3db2-a773-e9246f53d51f | -18.38758 | -39.9562 | 2026-09-06 03:45:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 34a8406d-be6d-3010-a37b-cc13457b7238 | -11.28666 | -45.10534 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80f2914e-4f3a-3e18-8c5e-70878ba6f184 | -11.28471 | -45.70731 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39c6f462-525b-3d34-b32f-3dc4eb986d1c | -12.94668 | -42.41632 | 2026-09-06 03:45:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bc0c52f-4dcb-3a23-976b-42697b31399b | -12.9518 | -42.41749 | 2026-09-06 03:45:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f56920e-ce74-320b-bee8-598987fd0f99 | -13.42956 | -41.89137 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1017675b-5a33-3f27-902f-51f301228c56 | -10.70687 | -45.91027 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e7bab2e-9276-3aaa-ac1e-6c1cd24607e9 | -11.27969 | -45.70622 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90eaf6cc-dde0-38e4-b9cd-4290353da2f7 | -17.4315 | -40.02461 | 2026-09-06 03:45:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f58673c-c378-3486-8b99-b7b6192f35f3 | -14.8669 | -40.91444 | 2026-09-06 03:45:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23bd56ef-313c-30d9-a3a2-c2226b83adb2 | -14.2865 | -42.69523 | 2026-09-06 03:45:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9d0e02eb-3dbd-3509-8c53-242912513597 | -14.91235 | -44.67492 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4f7426e0-437f-3b95-aeec-6082774fdf5d | -11.3303 | -45.06675 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e49c7e-9581-36ad-be90-d324908946f2 | -11.32919 | -45.07219 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4026ee7f-4c5c-3a2d-8683-7df07fd8dc6a | -11.33807 | -45.07619 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98044aef-69fa-38f2-bb96-31617c260b47 | -11.29375 | -45.70361 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6ec5cae-0961-3563-ab34-15693c99d2f6 | -13.86778 | -44.30688 | 2026-09-06 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b354075e-39d2-365e-bf78-3bcd2fdc7989 | -11.29161 | -45.71425 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10c108fc-508d-3c47-ad91-e95c95b8c9bb | -14.91891 | -44.6721 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1c08d4e1-f5e4-3a5a-893c-fd913930f3bf | -11.28511 | -45.71291 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb6e6b0b-0b60-3d37-b8c5-5a5be122e31d | -16.7531 | -41.71775 | 2026-09-06 03:45:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1e52e495-d964-356d-ab7f-89a49b7b7faf | -11.29333 | -45.69846 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a7f15d7-9f4b-3e5a-8ec1-2900135ea93d | -11.29297 | -45.10643 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d3f253c-04ca-31a2-b338-40110d43bc6a | -14.90579 | -44.6777 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22e1b8bc-fea1-393d-9810-8cef010a4eeb | -11.29912 | -45.71055 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36041cba-4e88-3357-9cbd-6c94d946707d | -14.90666 | -44.67353 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d05543d-e7fa-3b20-8a8c-3126c5888603 | -11.29008 | -45.71406 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 416e06c3-312a-3a12-9e8a-843cb0913105 | -11.28728 | -45.70214 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 392ef503-b318-3e8b-b0a4-304834889fb2 | -11.2883 | -45.69713 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a30e6e0-ee2e-3ed8-9acb-d63cc5f17c4c | -11.28622 | -45.70742 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README12.md)
