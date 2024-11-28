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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 854784f3-56ab-309d-9e0c-a048d6c16df0 | -4.01091 | -46.33134 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b172a0e-1f14-37b8-a8ec-3ff5bcc7afb1 | -2.80198 | -51.58339 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae637c88-c742-3f46-b542-81717da94517 | -2.86326 | -46.84033 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a76de6d-3f3c-3990-af17-0e077d0b7b4e | -3.22975 | -50.31536 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9826183-3eea-32cb-81dc-78f41f369d3e | -3.3012 | -50.49569 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1877254f-3684-3c8d-a35c-f8c6b2d6e132 | -3.41679 | -53.88641 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f5d92b-655b-300d-87d9-e62fbfd48f39 | -4.1751 | -48.62344 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c391a05-0045-3f4f-9151-1f0813c627ef | -2.92722 | -51.44997 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75b453ac-2b6a-305c-8220-322e713b84b6 | -3.46034 | -43.52494 | 2024-11-28 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b6b3870-458c-3933-b283-5465b565720d | -3.84832 | -47.06018 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c0bb652-db6f-302f-8c9d-9f81f9ab0e8b | -3.63805 | -44.94432 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2287e3d1-38af-34e0-b906-8e1e4ee2c73f | -3.22726 | -53.63148 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2130587-3e0c-3038-8107-11b9272097bc | -4.17369 | -48.45492 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a1f1abe-b5dc-3ccf-ae62-0357ccc8897f | -2.8218 | -51.79534 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9124bfc3-43f4-36e9-9ac5-75ede9bbde44 | -2.47554 | -50.36672 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 150b6164-7030-3fe8-8b3e-1797867065d7 | -4.48226 | -48.11719 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c54cc6e1-a04e-37a2-b3e6-ddcd6e4259a4 | -3.11571 | -53.10639 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47836c61-2f1c-35c8-b813-cd9b2e1ae5bb | -4.11771 | -48.4868 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e37a6b9-a47d-378c-8d94-c75b61047be8 | -4.15381 | -46.61114 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f064f1-ae56-3716-860d-634ab93b9a19 | -2.47344 | -50.40639 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70bbb7a-90a3-3257-93ea-8432573ac4b0 | -3.81174 | -46.60344 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e3adb8e-5d97-3772-bb71-c24f7d9d752a | -2.60113 | -53.9739 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0796c93-76d3-3642-8f0e-022171b25ef8 | -3.6247 | -51.49635 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aba326b1-5d75-34b0-8fee-434ee400e19c | -2.86251 | -45.79325 | 2024-11-28 04:25:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eb7cbcc-a112-329f-bcdd-d13e544a38e1 | -2.61669 | -51.80965 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db2537ab-121f-3593-bbfa-d3a1a602229c | -4.35397 | -50.87029 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8536902a-dcd0-3523-8680-3b5b5ade8612 | -3.93398 | -46.64817 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d51dc62-68af-3ae8-b134-a514ca330420 | -3.46263 | -43.53292 | 2024-11-28 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15540993-08de-3be7-9dc8-970320b746f9 | -6.01258 | -38.66286 | 2024-11-28 04:25:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 626a4c93-5c54-3240-b1d4-833001c8ce27 | -4.35439 | -48.68415 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79f241c4-f5f8-33e8-b3d8-e000443b867a | -3.29082 | -51.15443 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cdb3fa6e-3fe6-3613-ae0c-4c166927a774 | -4.11896 | -48.82143 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36ebd3dd-cfd9-3617-a75e-a6b664c81b0f | -3.9967 | -46.3149 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8afe6f36-4775-3e84-be25-bee4b4702d12 | -3.9471 | -46.68974 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540bed41-dfec-315c-80fc-0fe6e4d4d8f6 | -4.4369 | -46.34496 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e264c54c-2ca0-3d0f-a169-05859df22413 | -3.08667 | -49.21739 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 519dcb89-7c2f-39e4-8e4e-e6d5575bdf72 | -5.0902 | -45.8437 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9b08b75-751b-3f14-8f55-277f1cef17e0 | -2.84693 | -46.85616 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e15c63b7-5812-33e5-aeb3-a89380b12161 | -3.45792 | -54.4905 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5f83850-4487-325e-a06b-6c4d2f500949 | -4.77553 | -44.4212 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ac12a07-b15b-3295-84c0-6c88dbcade9a | -11.95657 | -49.53115 | 2024-11-28 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87eda294-10f6-3c6b-a873-cfee6765a756 | -2.77987 | -48.58134 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 619178f0-e207-3a33-80b4-99e0005d6e39 | -3.67234 | -45.7864 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18c0784-ccf0-3a64-b06d-dd9445a0c255 | -3.28242 | -54.74545 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da64f3d4-3837-37f7-8bf0-87d3e36a2582 | -2.842 | -46.61459 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 219144e9-74d3-35b1-8fa8-ee546a31cee6 | -3.70241 | -43.43086 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62fc4fd6-3247-3f1d-9400-24903b7d9337 | -1.60156 | -55.37887 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48f9ece7-13c5-3177-b197-34a271083710 | -2.02089 | -51.19238 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a025ee7-b497-3d42-8ab2-7fa5c047b005 | -14.91847 | -52.87686 | 2024-11-28 04:25:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8e7f18d-b6b1-3300-b62e-d2eb61cf3435 | -3.24261 | -48.47644 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b028ab4a-a67a-31ee-82a7-8cd14edb8641 | -3.17407 | -49.2294 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a41f53-71b1-395b-ae0c-7a933e9980ef | -3.84111 | -46.65156 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9c53e88-2bb7-3e84-abc3-29d3723a2612 | -2.96488 | -51.00169 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 443f9ad6-463e-3e92-98d5-5f02630b7f9e | -4.10492 | -48.25017 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba3678f-b242-30f5-9027-f8eb7ab9fba3 | -3.71311 | -51.806 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79beaa1d-4709-3c54-b0b8-ea37c019ddf9 | -2.60164 | -53.97084 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ba0a9f-2e81-3998-986d-711b4c8f2b40 | -4.36823 | -48.57462 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b782f0b8-2952-381e-a6fa-e72e78c512c1 | -3.26668 | -48.76487 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e3bacdd-8a8d-3616-97a7-6f5cf6f9aadf | -3.17739 | -50.28579 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac02bf02-f551-341f-b96d-80e034bc050f | -3.85481 | -50.12485 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9424daaa-1e82-370a-9afc-21d456cf53d9 | -2.32317 | -50.67308 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 793b7e51-7995-35b8-90b5-7ecf3bac2ba5 | -2.8447 | -46.84845 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cdd4de5-40eb-3d47-880c-19a2888bdc8e | -3.32934 | -50.21877 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e194dee-9aee-37eb-b7b1-83fb6d76eeca | -2.58982 | -53.9783 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cf584c8-f2c3-3e64-9c5f-1711b267ebb7 | -2.23033 | -55.9058 | 2024-11-28 04:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72a2543d-3a6c-3fd0-94fc-64b99446a7cb | -3.7342 | -49.94669 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be021683-2462-3e0a-a5ac-3230393bbcdf | -4.44644 | -46.56374 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ca0b856-26e2-3bfa-93c4-d5f68968f149 | -3.85169 | -47.0607 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6182815e-787b-3615-b6cd-a764e1ac4cd9 | -3.91461 | -53.67115 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a02176e1-068d-388e-885f-c72f614858c5 | -2.8962 | -54.17731 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b16ff66-6662-38bb-a483-b5faf9993e42 | -3.03656 | -50.98213 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f09aaeff-4dfa-36bf-b1f7-666e14957596 | -2.69588 | -48.65968 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4430384f-522c-3ec9-979d-1168a31c2b19 | -2.8587 | -46.86905 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5938d828-d150-31b6-bd78-0be20f91f81c | -5.10359 | -44.20493 | 2024-11-28 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca2713e6-c154-351c-90b8-1c35f06f2f2d | -3.94122 | -46.89882 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d2f6023-d4c7-363a-a3cf-2881d6893b02 | -3.81452 | -46.60747 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414c21f9-8355-3085-8029-d78b9b50c118 | -3.98439 | -46.64882 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba3f5b2-6662-3709-a1c2-a45d2cb16d1e | -3.94845 | -46.91819 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 603666c1-8154-3b59-80e9-46fd1cb67ea3 | -10.09005 | -47.56897 | 2024-11-28 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11e593e3-dcb1-38d6-b0bf-8146cd3454c3 | -3.14266 | -45.50218 | 2024-11-28 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11e39221-deb8-36e6-b2ed-e6192856dc91 | -2.96426 | -51.00552 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff2be382-fe7b-326d-b780-f1faf3ee242d | -2.69505 | -51.68765 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a53b07a-fdfc-32f4-b104-db317112a350 | -3.15309 | -50.58743 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37e4174e-b9b0-398b-9be9-9bff31fd85a7 | -2.75171 | -48.65995 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56e26d8a-4d69-3c8d-9899-2fe71da10dd9 | -3.46549 | -43.53718 | 2024-11-28 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ebc8a2b-f8e1-3887-8351-7254b67fdc29 | -4.17866 | -46.51845 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a51d581f-9b7c-3aaa-805b-5579594f24d6 | -3.06709 | -54.41374 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 523b866b-a5ec-3c2a-b03e-a86dbae76989 | -3.22914 | -45.38584 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0458c0eb-058a-3945-976e-c2b300485a57 | -3.11384 | -53.75624 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d756176-3172-3a47-ad91-b70f620264e0 | -2.8728 | -46.8455 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46cc7154-8c6a-3851-b1e5-09287cc18b91 | -3.26734 | -46.43633 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 535863b1-ce0c-3aaa-813e-c541dce5054d | -1.79659 | -52.74363 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f2824d4-88d8-3dd1-b9d9-0eca317fe026 | -2.95946 | -51.00867 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6ee01e9-b614-3b46-a828-396212395893 | -4.00039 | -46.31194 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0c911be-98f9-3be0-8ddd-b81dcafd209a | -2.84807 | -46.84898 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945a0b96-f785-3f15-a607-6567d5c5cab1 | -3.81422 | -47.47521 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a5750f-7b16-3402-96d6-659b7fc4b595 | -2.47471 | -48.80221 | 2024-11-28 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19e67e2d-91cc-3e6f-86e3-afe81d345679 | -3.26819 | -45.37431 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9eb6291f-e9d6-3b20-a78b-378e02a23cea | -3.17197 | -48.58441 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27cc36dd-4f95-370f-9678-150ab259db93 | -3.70713 | -47.13363 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README64.md)
