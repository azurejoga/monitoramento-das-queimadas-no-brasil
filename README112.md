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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa6811d-548f-3ab6-89d4-de6bde96984a | -10.00734 | -51.72003 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 665cd2b3-a181-3c2a-95e8-44869598831f | -13.65785 | -45.72998 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5fc2c00-cf5b-3501-8891-92b8f6fd3936 | -13.04626 | -48.0019 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0414ca48-6468-3aa7-8481-a07b2682c1ad | -9.79807 | -61.52163 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbd9fe64-07f0-30c3-9e5e-3d0b4bee01b1 | -8.08247 | -54.74877 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26dad375-c778-35af-b466-459d5a6b7058 | -15.81331 | -52.22515 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9ec0230-cb19-3b0b-98bf-f47d372fd6b0 | -15.13863 | -48.61601 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 56de75e3-d9ff-3e13-8a79-d8a9309351c5 | -15.11197 | -50.09982 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b14222-4ab4-3db3-a64a-9153b1b5198b | -9.59487 | -55.0118 | 2025-09-11 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d03b279c-a5d4-3573-96cf-db9085c96f6a | -10.02236 | -51.73345 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd3a133-80cf-36c8-9398-e31d7106cf08 | -11.41634 | -43.54079 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c016945a-d27c-3f1b-8cb5-edef80203b1c | -11.38871 | -43.53242 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceec6085-3ec8-3d2d-8da3-a1eff0d7b2e5 | -11.35838 | -46.5136 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 48967597-f9e8-30f4-a781-1545deed1103 | -12.92243 | -54.76751 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59dd6f96-63a1-3699-a815-f3d86a3b02e8 | -13.16517 | -45.28712 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc339a18-7a1f-37e5-82e0-f4449ae1d23b | -9.77892 | -51.09851 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f50e95f-3a8e-303c-bfb4-1736e0b81514 | -11.16169 | -52.045 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 302df0e4-1e57-3227-8747-cc5377d3d7e9 | -13.26855 | -43.74731 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 071d29c9-3045-37de-9491-4bdb28e08eb3 | -11.22401 | -54.99169 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dbae842-e71c-30ec-88d2-a1f5ea785dbc | -15.25037 | -44.02839 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ad0c18d-a4cf-3670-ac26-8255091a72c9 | -12.38279 | -54.17014 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8472b8-2082-317b-a712-d935f8d85d3b | -13.0377 | -48.00617 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89c78a13-f354-3e04-8e72-ea7d05071bb8 | -12.03149 | -47.54525 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 259e0475-675f-3c35-841f-b01ce92f6d15 | -12.85372 | -52.96341 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8695a057-fd25-327d-bbfe-ff6a57f74f26 | -9.02792 | -49.77594 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fe9e15e-b096-3003-a7db-ecd499412f5a | -10.00017 | -51.72247 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa83f150-daa5-3ed4-99ce-654a90f455b8 | -11.71741 | -50.64086 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3d6dba66-6ccd-3dbb-b9dd-cd263191243c | -8.57955 | -51.29922 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 934215bb-2ad8-3241-bf71-1257cbc6a827 | -13.19079 | -51.76566 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f689a0cf-f395-3be3-8495-a62e2b700de8 | -11.10188 | -48.4237 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a9cb5f7-641a-3cb9-ae52-406860c45afa | -11.73037 | -50.62397 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 14f84b6a-fa3c-3adc-9a77-2e6cbb7dfe73 | -14.88678 | -55.87246 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e30422c9-fd51-38c6-a070-9717391489ad | -12.58191 | -44.78707 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5086403c-90a2-3213-a860-81530cd731f2 | -10.37631 | -50.52542 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7363806a-593e-3cb6-a9e1-620d7b797c76 | -12.84813 | -47.96022 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b43a82e-fcd3-37aa-824e-825dd50562ed | -10.56443 | -51.99945 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f86b54e8-0a3b-3690-a23e-f51b47ecb46a | -16.05974 | -49.97123 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd9cd4c3-c2df-31f6-ae65-f4b40f8718d4 | -10.57106 | -52.04354 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 463f5161-61f2-31e4-81be-2326fe0d1781 | -11.74387 | -46.52795 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1e1761d-5542-329b-9db2-984c13e6103c | -10.73009 | -46.13591 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2157e04-dc9c-35b6-8bd4-7f0d014c966c | -9.01577 | -49.76279 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d94e635-abf6-3016-a6d7-46c593648e9c | -9.89703 | -49.92873 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deeea413-2a73-397c-bd14-d19c652544f3 | -8.87444 | -49.56536 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| e59bb203-4074-38e3-a498-f167d6f2e7e3 | -10.38955 | -48.5757 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cee0043a-2db5-306b-ad10-33a7cb99c761 | -14.42659 | -52.93946 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 224f4ede-2177-39bb-b8f3-06eaa1f79d63 | -12.84596 | -47.97535 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dafca113-9f40-3d0b-92d1-d30ff0b6d27b | -9.71521 | -48.33932 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68944fac-5153-3649-8f01-80c8f3c568dc | -12.84828 | -52.93346 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cefa8da5-5d9f-35d0-b768-4c5856f82d27 | -11.9973 | -47.58743 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90049d68-ff2d-3ede-bb10-5035d0295eee | -11.1396 | -52.01334 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e9e068f-37f1-348a-81d2-481ab3e3034d | -10.20001 | -51.68252 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 511cd9b9-ff7e-32f9-8ab3-4026d996d645 | -9.98691 | -51.69888 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50171aa5-f721-39d4-a0bb-770a9bb28963 | -9.7617 | -51.056 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b436bb75-9dc8-3f27-a614-2348431da662 | -9.30412 | -46.76047 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da1757df-f6f3-3428-9895-6c5fccda002e | -11.48168 | -43.67962 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb90ff2-89c7-3ac0-bfd2-2eab7c06121c | -12.47631 | -47.4957 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b49c39-01ab-3c32-b2e1-f2ddb5652696 | -11.15584 | -45.30315 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f9e0871-ef68-316f-8d74-badbe9607d06 | -11.49248 | -43.66037 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6d26be6-a29b-36c6-ad62-02b9a85954db | -15.11257 | -50.09571 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b246329-1c6d-3d9d-bd56-3030a4c31389 | -12.04611 | -47.60664 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb1f345-6e42-38d6-b6bd-a03c8c95da6e | -9.51936 | -54.64739 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b43c88-b1fc-30d1-b4b8-c410840c284d | -13.2471 | -43.79284 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c515cb1c-f48b-3d05-9b04-26566c71a5dc | -9.60033 | -48.06137 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02aff183-1995-39ec-b7f4-5a8f6fcfcdd1 | -14.50744 | -53.96339 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 427e64f5-8317-3823-801a-eef56fef6b60 | -10.54319 | -51.50798 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f99869cb-2d3b-37c7-abcd-0833aebccd20 | -12.95112 | -54.74464 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b742e7b6-234c-3624-bfd1-93a7a9a3e7e2 | -9.0319 | -49.77274 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d98381ab-d0a4-3a70-af92-12ca6eddef79 | -14.30198 | -54.74718 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b81eb774-7b91-35a4-bfd4-78a60cc3876b | -11.607 | -52.21447 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06fa8b9a-a21d-307c-a53f-783586bc53bd | -14.30236 | -45.0382 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b93a7f84-c6dc-3689-ba62-75838f578686 | -10.15979 | -46.17347 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d5f8885-8400-3e46-aa9f-4f06992e00b3 | -11.6529 | -46.90693 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 535c9a8d-3e1a-371d-8773-1f0031753658 | -14.90879 | -55.872 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 290b56a2-c4a5-3706-8ac0-21574f6a67f4 | -12.13385 | -44.86222 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5c176f9-c9f5-3c34-be79-6d7a057c81ce | -16.37249 | -49.41346 | 2025-09-11 04:46:00 | NOAA-20 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbcee9ca-93f7-3703-8dbe-4ad0660f1333 | -12.13861 | -44.86268 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa633657-4fff-319a-9d7f-cb2562f8914b | -9.99188 | -51.71041 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5379d927-ba4b-3eab-841f-91906fa8f981 | -11.14867 | -45.28806 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07cd419c-b8ce-3306-b0d6-ae17d975ed37 | -10.02234 | -51.71198 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a62ba6b-f1f1-370c-a4e9-4ee339af8942 | -11.48331 | -43.62775 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e16dc01e-0b1e-38be-a3a9-0d5084eed45d | -8.09269 | -54.75482 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2420dbcc-4646-3b33-b14e-19fc4b5b0ad7 | -11.77954 | -50.57477 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31e53462-c718-30fb-9d82-d5d76ffd83b7 | -15.22079 | -44.0544 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e94db45-5379-388e-92ed-1838e90b55e3 | -14.57266 | -48.76734 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 742c7ead-558d-334f-8548-c9f59b096451 | -15.21595 | -44.05043 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f2054a-d306-33c1-aa67-8921ec768793 | -10.54762 | -51.52312 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd01c507-a5dd-3af4-9c9d-e4a9e0e19f65 | -10.94 | -46.81494 | 2025-09-11 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7988c0fa-4fde-317d-a85f-c29c0454349d | -11.41159 | -43.53698 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83382582-d340-3f38-97e8-02de3307a539 | -14.14183 | -45.41553 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73192e07-3b91-389d-93bb-67ac0222caa1 | -10.5515 | -51.5201 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21f5fb8a-f1bb-3d06-9eb6-9a407db2f2a1 | -11.16797 | -45.2822 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ee1e3ea-479d-31f9-b9dd-2ef0789fcc1c | -12.12434 | -44.86118 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f814e2de-cb54-3543-a8a5-e03296d73883 | -11.72591 | -50.65352 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cbeeff6-9ba2-35ad-8daf-d0bf3d0ae449 | -11.1534 | -52.03353 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b76649d-c416-3837-9947-7578b5c7ac7c | -11.9919 | -47.59723 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ab2d1dc-3f40-3d8d-afb5-818f8fed8090 | -11.72814 | -50.63875 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44fe364b-a6f3-345d-864f-1faa7bd5328c | -12.2079 | -53.8677 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f9e25a9-9a0d-3fce-b19a-f5630770449f | -11.47819 | -43.62716 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09d2950d-7cbf-3a54-b938-6ce562efc77e | -10.02567 | -51.73398 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6177f84-0dc1-3273-bf21-62e72bb6a12e | -14.31159 | -54.75281 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README113.md)
