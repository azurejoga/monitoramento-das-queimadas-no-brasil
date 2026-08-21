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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f02888b2-f1b1-3033-8d1a-ec6283baaa23 | -6.38522 | -54.95037 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3c4fc86-b958-39bf-a179-5a7304219876 | -3.1345 | -61.21844 | 2026-08-21 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8db1cdb7-aa55-3f44-9fe4-66b658e9d94d | -9.11522 | -60.336 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e32efe3-b593-30ea-9d2a-40f44eb4bbe1 | -14.4347 | -52.93406 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c3c07a5-8789-3931-97ec-04bf21be073e | -8.58596 | -54.78404 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dd98f9b-b707-3557-b62c-c24466b941e2 | -8.7195 | -49.6166 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83fc5510-3be6-341f-b3e4-14a1ab64be6b | -14.71942 | -47.13935 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36d0d494-4c85-3c54-8e2c-86ffb3b6666b | -6.76376 | -59.15168 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee4521b-5e23-3914-8fed-85c011a63357 | -8.49972 | -54.86543 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c295dd9-d021-3424-9927-582fa548e39b | -6.22874 | -55.39939 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d7d73a4-1155-3c06-8140-333a0bd25927 | -3.76146 | -59.42366 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bac71e6-af1d-3b99-a9f3-f982c0d1c4a9 | -15.1619 | -48.78721 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 694bccee-fa26-359b-98e9-235eaf44a1c6 | -6.43532 | -52.74117 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf4340cb-12ab-39bb-8c40-86635825f864 | -6.95535 | -59.30613 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1395aa2b-6f3a-3e99-8cee-6e21f5116005 | -6.80102 | -59.44061 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 467283ff-a66a-38b3-b8c2-f2b65282504d | -13.74061 | -51.85894 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 624c18f2-a53e-3a1a-8d98-de709e7864c4 | -9.06713 | -50.88469 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f006093-0fae-358d-8b99-2a49b962e70c | -6.58401 | -58.96704 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 899deae5-18d5-3c09-8d7b-303d8598bc81 | -10.5263 | -50.77818 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9ab8699-1684-3835-9998-e8a1775f3e76 | -7.76939 | -61.13839 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b454c22a-58f1-3a8d-8b8d-8d8f8c4e0a64 | -7.29234 | -52.53786 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b35935a4-4a4f-335f-96dc-eb18c666b898 | -6.71367 | -59.09163 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fd69baa-892a-37ef-908c-0f2d68433411 | -6.95366 | -52.80985 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23033c17-42a2-352a-821d-1207793f02bc | -6.96708 | -50.41748 | 2026-08-21 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32c472a-d740-30d1-a7e0-fbd0d0d45a9a | -7.00017 | -59.05207 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e45ead8-6439-36c8-94a4-b6f56bea49d3 | -16.30282 | -48.90766 | 2026-08-21 05:23:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f731dd-4271-340c-86cb-baa97d648b6b | -8.09555 | -51.6727 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2869f6a-7f83-3736-8f4e-c54b34a3688b | -7.60291 | -60.94839 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9aaceb0-d52d-3123-ac26-751fd8d4ff92 | -7.89028 | -61.66492 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eafcca96-54da-3056-a0b1-64be5b113758 | -6.6925 | -58.94331 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d785fad9-ce18-3c11-a263-8496162b1d6f | -13.39558 | -54.37569 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6f02f912-0820-3b40-92db-bd4268431600 | -6.57683 | -55.44247 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aba6709-b092-3323-93b0-5a5c6a59af19 | -4.4729 | -55.40002 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbab4fb1-fe6d-363b-b550-0a9aa1504436 | -9.22069 | -59.7751 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f9535cf-5c94-3656-ba5b-2e04fcc25d36 | -6.43134 | -52.74059 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 085f097c-5dba-3d73-afea-983cc487d84e | -7.01037 | -56.54398 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f50d73-f5e2-307a-b5fb-d90c4193218c | -9.20929 | -59.78078 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e20cb59e-f3f8-3a93-88b8-0847cd03d354 | -5.60968 | -44.01259 | 2026-08-21 05:23:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba89548a-339e-3acd-8a51-21ba5770e272 | -14.44928 | -45.61105 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67afd29d-986e-353a-af1a-e24aa1bf2a15 | -6.01559 | -57.8049 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a08112b-d7bd-35a7-8c8a-4c2aacb160b3 | -6.61885 | -56.34499 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b86e40-ab6f-3429-9958-21ebbb38110b | -6.7545 | -59.46743 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51702ac0-2254-3d84-8b98-8c7b05ab9495 | -7.35978 | -45.81784 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d4b38cd2-4eaa-3652-8454-84e940d9aa10 | -6.60094 | -56.3714 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9f5620-abf3-3462-9c6c-7039ee726ce1 | -3.01424 | -51.06139 | 2026-08-21 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c85804dd-43bb-39b1-a5ed-02dd03548965 | -6.87633 | -59.42612 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a88bb98a-85cc-3f96-997a-d45ecebbea63 | -6.57711 | -58.98819 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aa6cbe4-b55b-3a57-b330-adb1c1723021 | -7.45855 | -59.99737 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f030999d-1872-3107-aa84-fe59dff0288a | -4.11064 | -54.92503 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2245f284-0228-3b02-9b15-e327cf4cf6d7 | -6.42872 | -52.74272 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e882079d-7fb4-3bb7-b2bd-30bf9b5cc0df | -7.34519 | -55.69159 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c90987-7059-31d3-85cf-85ba010f3eb0 | -6.89705 | -55.72398 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da5cced8-ed83-3f17-bfb3-e76ad9812dcb | -6.61012 | -58.3872 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| befbb717-f975-305a-9c40-dbe4567ceb97 | -6.10704 | -57.86924 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b4e956e-6727-3571-aad5-0c69849c0869 | -13.43542 | -51.80167 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c110806a-14d3-3091-b6e0-0ce65f9dcc81 | -4.46666 | -55.39531 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6903536-9e3f-3114-a65a-8c5082128c07 | -9.06783 | -50.87978 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d62dcf3-1e4d-3f33-b77a-6df4d775c94a | -8.5917 | -54.74612 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b66d5c67-8c88-3c08-9b51-c38fbc7ee1f6 | -6.43682 | -52.73087 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36980782-e34f-3f63-bfdb-b0f81172586f | -8.5787 | -54.78293 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1eef611-be81-3a2a-9600-f4990c169640 | -8.44778 | -46.95214 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503c8bff-1046-3dc7-a156-26c8ae8bad1b | -6.89283 | -59.43262 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 385f7b78-a793-3950-b3be-a90a14262679 | -8.89329 | -60.54387 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e29ff5a-ffc5-3d83-806f-3f7419a70ac0 | -6.23103 | -55.40739 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e0a4acb-5d48-3ace-85d1-b3b0a4501149 | -13.38841 | -54.36934 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3aa5da93-b4bd-3f5a-9522-e7d52456a908 | -13.93846 | -53.85371 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c234adf-2011-3f19-89c7-7af168e7c855 | -6.91958 | -59.35354 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52fdf01c-f439-3061-9450-e546e98ccc96 | -4.5829 | -59.94254 | 2026-08-21 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1c19811-edca-390d-a797-c0cc52fd57fe | -6.12336 | -59.90678 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8125a2e-0cd3-33d6-94df-856ca689ee8c | -6.57626 | -55.44625 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33fa21e2-50b0-3142-9320-cf4bba4aa177 | -6.69705 | -58.93665 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d589c43-bae6-33b2-a069-3acdaf27882f | -7.00968 | -48.03588 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc32078f-df37-34d0-bcc0-3a0d0b7718d3 | -13.44147 | -51.7921 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1686ccb6-f33c-3c3d-97e1-55acae83d19a | -7.36618 | -45.81873 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bec95e0d-06ac-3484-baef-439b6482e7f3 | -14.33887 | -51.91824 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2073a061-bf87-3657-b035-ab1940ada17d | -7.35439 | -55.67765 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2b2199-76ae-3a39-ab3f-bdd741ba7d19 | -6.34276 | -44.07917 | 2026-08-21 05:23:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56cd09d0-c915-3076-ab37-4339aeb340e4 | -6.42912 | -52.75595 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6e6c5d4-36e7-35b3-b7e9-31b93bdac9de | -6.89259 | -56.4273 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 474bdbe6-cdbf-3170-a6bf-cb089a87c318 | -8.54966 | -54.77849 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06182bd3-110f-3eec-8349-468092fe7509 | -6.71706 | -59.09217 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f63a6ad8-c8c6-36de-bfc0-72b7eafdc8de | -6.21936 | -55.48225 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46984563-1cf3-3709-a993-5813cd322d69 | -6.5793 | -56.53151 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2675d2-4c5b-340f-ae9b-54605f29ddb5 | -9.55027 | -56.79948 | 2026-08-21 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9de2f2e-f840-357b-95a9-ce8281405a03 | -7.01948 | -48.03925 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67651ed1-3cd6-32ee-a79f-c0401c52e75a | -7.13469 | -59.64262 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 167436c8-bd4f-3d8d-a8ea-e9079d4e6d7f | -6.13451 | -59.90459 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daa3c4fc-6d65-327f-b69e-6b3efdf19ff2 | -6.42958 | -52.7638 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7d8e35e-1872-337a-87c6-e77136703131 | -5.72024 | -53.72398 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88dddb23-92a0-35a2-a678-4b9b66e3d53f | -9.05232 | -50.888 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8408fdcb-5bc3-3c32-81ff-46298296cf36 | -8.44721 | -46.95659 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| face9ddc-bdc3-36d5-9716-6b31cb5d4c21 | -4.01093 | -48.06158 | 2026-08-21 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a151a734-32d5-3625-81c4-6a2ae9fb7ff6 | -13.93746 | -53.86118 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34ec4639-d16f-3706-bc76-c29d7d165f6e | -6.88197 | -59.43465 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e29459c8-26cb-3954-b7ab-a162b8fabbd5 | -6.1181 | -57.6931 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df444998-f5a9-3d78-afd6-252d9f93cad7 | -6.61829 | -56.34853 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6dbaad-538a-3276-8fa8-cd72d1afe761 | -5.49391 | -60.14016 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376b49c4-82c9-34fd-a4f4-68e521db9a3f | -14.45634 | -45.61174 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d01a3c8-8d82-30d1-ad84-3a0d132dac4b | -8.38046 | -62.70217 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e60c1b9c-5e4c-3120-9f91-3bfaaee8153b | -12.49424 | -54.75364 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README65.md)
