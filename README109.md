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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f92e0be1-1985-3e2e-a7ca-48fcbcac5d8c | -14.50822 | -53.93734 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c917a969-3338-3225-b10b-2fc4f8cc46c4 | -10.19175 | -51.69194 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c5fe1d-878b-3ae0-8e92-94c55450871e | -11.46954 | -43.69325 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edc8c8e2-714c-3604-ad29-b1711dae58f3 | -13.15648 | -45.28077 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09f47d11-8b4e-3f3b-8a69-e168fede7d6e | -13.13262 | -54.91862 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fd4ec5a-b2d4-3c9b-a13e-5d3292a369f4 | -11.18875 | -48.36084 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adeecc49-8af7-309a-92f5-0bcea92985ce | -12.91625 | -47.98829 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 976825ac-3ef4-3b7b-a702-22f6f2e5b581 | -11.34851 | -46.52335 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1bfe3f4-c2f5-34b2-ae6b-6c0decafb669 | -12.0595 | -50.94102 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6ef3c6-7573-36e0-81e5-b5e0f42e1db0 | -12.8449 | -52.95469 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59387042-43d7-3e53-825b-1d939d0f5b68 | -11.47969 | -49.25179 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aae2161e-39e2-37b6-b015-59b87c3796d5 | -11.16003 | -52.0346 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc6c0270-dbaf-3d73-a6f3-fe7ad04eca64 | -12.0192 | -47.57492 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8efd5fc-7269-3ec6-baa7-a27fb4c331e6 | -11.48965 | -43.6414 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fceee42e-6ef1-3ae7-9721-fcd33011099b | -12.0561 | -47.59256 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dfc8ad5-0cf6-317a-8948-aeb032c48724 | -11.1546 | -45.31219 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa3e4b0b-b91f-3f9b-befd-d8cdcc2963e4 | -9.77227 | -51.09744 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f142a1-ce3c-3572-a2a3-59854899ccf8 | -9.97974 | -51.70131 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c79fbb51-9f7e-3029-a724-da9a76c4aab7 | -12.94362 | -54.81114 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c183c149-4117-31a6-b0b8-79d54d362079 | -8.51712 | -51.39294 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c909665-b746-34ad-8bd4-25f5145de779 | -12.92395 | -54.77972 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3033592c-e653-3ef2-842e-184b95c0b539 | -12.06539 | -47.58358 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edc553c8-1758-35ad-b0b2-2dfbbecc87fa | -16.06458 | -49.96315 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bcaf96a-8292-3afa-84a7-a80a6ba6bc27 | -8.08975 | -54.74997 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f33a058d-cca1-39b0-a08d-56b8d00e3ccd | -12.21623 | -53.88043 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5568605-a74d-35fb-8dad-e106ee29927b | -14.1391 | -45.39969 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ea54154-5c2a-392d-83ef-ddd63d551e24 | -15.67328 | -47.03163 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b8248332-db13-36ec-9e6e-3e472f91cd7e | -16.42507 | -45.68699 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cd81b1e-10a4-3788-a610-db5c06ffdfbe | -9.88058 | -51.8786 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09ae5aba-a3cb-3f50-b1bd-cc7f0892da32 | -15.80608 | -52.2276 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd4fd6be-e30d-3c36-ad9a-e0c676d5dcb7 | -13.84669 | -47.34843 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1af8d9e6-6b71-30f5-866a-69e4cdb7d0ea | -10.00458 | -51.71602 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6392772a-99b9-3068-b218-7ed6fe4edf4e | -9.69047 | -46.79186 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af5e5387-cc94-3c92-a299-357b261533ea | -15.42351 | -53.96893 | 2025-09-11 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e5f7424-d751-30ba-8845-8a7dd7526215 | -11.96351 | -46.65787 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78f44d6a-9895-387b-b2fd-e3a81a05aee7 | -12.52948 | -45.3345 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 47280098-1eaf-3edb-8419-abf8605a6367 | -15.97617 | -49.63619 | 2025-09-11 04:46:00 | NOAA-20 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b358b5e-b207-34a5-9459-0de6507feef8 | -8.89595 | -51.05661 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b846738-206d-3245-b1ed-f1fc71151972 | -11.40882 | -43.53835 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86423d1-bc3f-32f7-8799-ace25bff4317 | -11.48764 | -43.63435 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f110ff42-017c-3284-9a7b-aef49a71cbfe | -11.47386 | -43.62047 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b7da07-9b66-3a8f-aec0-0a5ebaf22c24 | -15.09641 | -50.05622 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 358609c4-3da2-30d8-abc3-968fb1ab8de2 | -11.05774 | -51.33998 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9a7d015-e3f0-32db-81c1-acaa178ea363 | -14.89888 | -55.84471 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fe2da38-fcad-3258-b12e-9389955d5ec9 | -10.66037 | -48.63758 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc6209e0-91f7-3584-be41-ef23fa62a7fd | -9.71581 | -48.33527 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 085283ef-8ee9-315e-b2da-d2739f7376e0 | -10.39956 | -55.39791 | 2025-09-11 04:46:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9433c1c1-3ba0-3f01-8c4c-60453cdd1061 | -13.66738 | -44.22155 | 2025-09-11 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c5d273b-33bc-3e56-b0d8-2b867ffbc8d9 | -12.55979 | -46.9339 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60b4f969-508a-377f-8ca4-491afe269c92 | -11.49286 | -43.65731 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25e5cd64-a60f-35e7-bac4-52fe99bfa06e | -13.27189 | -51.72726 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7095641c-9444-3d82-9b02-93bf9e10dff7 | -11.34378 | -46.49529 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c7cafda-a542-3af4-8b6c-1d0281bdd7da | -15.98475 | -42.98555 | 2025-09-11 04:46:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 470f291d-46b9-3cfe-8662-46dda400a4e0 | -12.93886 | -54.81834 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b15306ba-35ae-3dea-ad0d-24d7ec31dba0 | -9.03246 | -49.76901 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd7d829b-b724-3920-984d-374745e4c5a7 | -10.56995 | -52.02902 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c463aa78-9c12-3e2e-be08-bb738553f5d0 | -11.13464 | -52.06644 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a8d8a1-abf9-3ff5-b0bd-cd06709129db | -11.48626 | -43.66872 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a128ad25-a3b0-3a0b-8ba4-e932f2c916d6 | -15.1479 | -52.40679 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7c2b992-7037-3a18-86c8-4530db114700 | -15.12576 | -52.4177 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed6d0e02-a94e-304e-a635-c9a0af6723a4 | -11.09945 | -48.41426 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a96bb6e-0014-31c5-9313-b74371757f5f | -13.97149 | -48.2457 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c05f7d93-85f2-306a-a1d4-a94351dbf6a2 | -9.08316 | -49.84906 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 408c231e-347c-398f-8223-ece3ae7f99a4 | -11.02586 | -45.05823 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4e91dae0-06d9-3692-94a7-c52b9ec3eeff | -12.92545 | -54.79198 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db4c018f-21fb-3d75-a9ba-463846680af1 | -16.29839 | -50.04769 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9444bae8-3e7a-3e56-bdd5-04f04e671ec5 | -12.4337 | -47.81004 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edffef9f-45d9-38ab-885d-f306fc4624a1 | -11.75721 | -51.90702 | 2025-09-11 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a1a8b64-b984-3d6d-83ab-aab06b8a118c | -14.91518 | -47.31191 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d798c18-c9db-36ca-b8d6-27507a1620fb | -15.79531 | -52.25935 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d05d33f-1441-399c-83f4-b74cac20c425 | -12.96456 | -46.73687 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d98cbbe1-8426-354a-8116-010807a671ce | -15.80169 | -52.27887 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f580bac-c905-344d-98ab-0671061724c4 | -9.06808 | -50.49404 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4081ed2-42f3-32da-861e-c2a811914a74 | -16.88274 | -45.75977 | 2025-09-11 04:46:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc99a01-92fd-3b2e-b404-2edf2937e9d0 | -14.11729 | -44.32199 | 2025-09-11 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b320c8de-b00c-353e-a20a-b8f5e5e706c1 | -15.8 | -52.2675 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdc436e7-c7af-3575-8fa8-0e5cfd5a6fe3 | -11.45143 | -43.59288 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07977018-89f1-351c-a1b9-ddc66038115c | -9.99519 | -51.71093 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcdaeae7-ba5e-3678-b67c-8ccea12d9be5 | -12.8652 | -62.12461 | 2025-09-11 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79694aa2-0606-3621-83bb-d15c78fe8167 | -12.39422 | -54.16446 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 412e4e52-02ac-3e81-b3f7-bbc24761b226 | -11.50448 | -50.40329 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 627264d3-177f-3ac7-b6f5-92a7154ec070 | -12.13649 | -44.84186 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c9836f-f718-36a7-9957-61a4a33e278c | -11.36404 | -46.53453 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aee1873c-3a0c-33b4-a7e6-4de9909ecbfc | -11.35991 | -46.53362 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4ef610b-e7a7-3ef4-9b0a-4b522c4c3e89 | -11.12856 | -52.01874 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7303af4a-0ba6-3523-b966-8595b211d145 | -11.04119 | -49.74309 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af370aee-c8f7-32d1-ac73-45737f23543e | -9.02407 | -49.52587 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c77eb6fd-e731-3c94-ba53-82cfa04d0d53 | -9.89379 | -51.88071 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30eb683e-b35e-39bf-81bb-7929c04e2768 | -12.05006 | -47.60721 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d2c0e6b-9d8d-36fb-9ba7-88fa68b1edda | -10.59772 | -49.64281 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a8935b0-7ec4-3878-8a02-79f4c740d43d | -14.92939 | -55.94414 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 369a6335-9847-3c15-97a7-ce01019ea95c | -10.89953 | -47.76684 | 2025-09-11 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f54bf4-2b6a-339a-a16f-2b860f4d1bab | -10.06369 | -50.37361 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02c4c5b7-8e32-3601-8a38-45d0b5ab7548 | -15.12631 | -52.41413 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfa3c81f-a70e-3d1c-9091-78c5aad19adb | -8.63381 | -53.10794 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c280384b-e54d-3544-ae8a-d01f2d7f70bf | -14.47476 | -46.35666 | 2025-09-11 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5c1472-2d05-340a-8e98-da39de67f92f | -11.48551 | -43.67476 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20c3a382-77d7-3dcc-bc70-7a96fb189890 | -15.50253 | -52.91976 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc4a04ed-38dd-3e1e-ada2-a830f0a8714e | -11.37885 | -43.52798 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 731a1248-b4d5-3015-960a-7bbefafa5b7c | -10.11253 | -48.17943 | 2025-09-11 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README110.md)
