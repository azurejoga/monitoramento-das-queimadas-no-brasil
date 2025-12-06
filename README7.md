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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17ace925-6e7c-3e85-9d87-b2b02ab00694 | -2.11039 | -53.45543 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66b3534c-3be0-31fb-bffd-37bed4abc80e | -2.31086 | -47.73488 | 2025-12-06 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 617c4ce2-7db5-3d17-b279-b43508ab3a0b | -4.40351 | -45.75189 | 2025-12-06 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 110ec767-51dd-3506-9260-c6a03bd9d171 | -2.99263 | -45.58581 | 2025-12-06 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe990a06-68c4-3728-ab97-e70a3b3cc403 | 1.69367 | -50.8529 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c4e30c0-ee25-3ba8-a32f-9bb8103f73e9 | -2.02218 | -46.27091 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f09a6f8-eb09-36c4-a423-88ae009eec38 | -2.29532 | -45.78651 | 2025-12-06 04:31:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d0c5e71-dcf5-347e-9545-5dc1ad2aaff6 | -3.87549 | -41.58184 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0243be3-054e-3a6d-b304-728fd9e20248 | -1.4816 | -45.58438 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 438ac6f2-5af3-30b6-ad69-41af98b85b98 | 0.12372 | -49.92248 | 2025-12-06 04:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84213cbf-819c-3464-8612-3a867a96efd6 | -4.73669 | -44.42925 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1b3c0f3-35b3-3d07-a41b-0a9213e8239f | -4.62225 | -45.63072 | 2025-12-06 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2379bd40-0116-3308-ae65-05e5a2be7da8 | -1.80893 | -54.65 | 2025-12-06 04:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02491eee-59b1-3fea-a2a8-06bfd4cfd402 | -1.47825 | -45.58386 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1640d9f8-4f12-38bb-b17f-1976809ea74a | -2.35234 | -45.75175 | 2025-12-06 04:31:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93018e57-070c-3273-b238-6fe8455a4794 | -4.54386 | -38.33707 | 2025-12-06 04:31:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a589937-ec9c-3cc7-90c1-bd396a292174 | -1.95251 | -46.47605 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58ee2a99-0743-3c1f-b6af-b3d11e966a1a | -2.08494 | -46.41222 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c47ba89e-b1a3-3621-adc1-bf9da32b1155 | 0.43295 | -50.92801 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f086ad2d-4146-3892-b357-1b661800dab5 | 0.43998 | -50.92181 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6eb314f-ad1e-3749-b3d2-8c6ad94595eb | -3.74937 | -45.18569 | 2025-12-06 04:31:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c6cb059-7180-3561-97c7-8d864b1256e1 | -3.87514 | -41.58128 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf8359a9-46ed-3da4-b64d-0e478f175d30 | -5.98423 | -41.89734 | 2025-12-06 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ebe68c9e-b6f0-38f1-bc48-913b34538784 | -5.85754 | -39.94717 | 2025-12-06 04:31:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c458d51-60a4-3c77-b497-2755ac13637a | -1.98701 | -52.89156 | 2025-12-06 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b183b5ff-37a1-3739-8359-8ff843476cde | -3.8761 | -41.57789 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 015a9b4d-2674-353f-a133-2fa2fa3d43ee | -4.74787 | -44.43849 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1614431b-6ff8-38b7-8964-3f35cd64f890 | 1.70356 | -50.84387 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a17fdbe-c091-3cec-8237-186ab498c333 | -3.06226 | -45.72522 | 2025-12-06 04:31:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21e13175-30aa-36d7-8f22-56daf8b99049 | 1.68577 | -50.85413 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b9d1fb4-a46b-3c70-8e27-392eb9ae257b | -1.84314 | -45.87558 | 2025-12-06 04:31:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9d3f9dbc-9faf-34ec-877b-bbca0746f365 | -3.83165 | -45.28666 | 2025-12-06 04:31:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf046631-8888-3591-9d68-f5544bd880af | 0.44388 | -50.9212 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae653399-fa08-39ad-aa58-30e656cde7d7 | -3.87573 | -41.57732 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a70fcda-3f84-3517-baa7-5431620ab71f | 1.69642 | -50.85017 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7734ffed-2f23-3d81-bfc5-daf152905010 | 1.68261 | -50.85981 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b908334-f604-3814-8b95-7e1867354da9 | -4.33731 | -46.08615 | 2025-12-06 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ca778c6-e7cf-3863-bdd6-b56382048a03 | 0.43608 | -50.92244 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a8af6b5-5793-35bf-be9a-387bbd719c9f | -5.8526 | -39.94671 | 2025-12-06 04:31:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f6371cb1-ed71-3e2d-bd64-dd2e2e2dfdba | -3.06339 | -45.7401 | 2025-12-06 04:31:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be1806d4-1107-3054-beb7-b0726343e917 | -4.2594 | -48.84098 | 2025-12-06 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db22baf2-a7b0-3748-840a-231c2cecbc29 | -6.0613 | -41.50334 | 2025-12-06 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc854a61-1711-3fa2-b30a-4cdf941e4988 | -1.71917 | -45.77721 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc1d2848-73a2-3aea-8096-a57b08dfff36 | -2.43725 | -47.19315 | 2025-12-06 04:31:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66198d38-e013-3a18-8635-d0d2b700a5be | -2.58847 | -45.54585 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dd5071e-618a-3ff8-bf6a-37c2b9098afd | -2.65866 | -44.98849 | 2025-12-06 04:31:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e772b5f-a19f-3ae0-816c-2b3d6ca2a689 | -4.53787 | -45.36081 | 2025-12-06 04:31:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b372876-14e8-3b90-aaff-b855f198bb36 | -4.25996 | -48.8374 | 2025-12-06 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 297a5744-4a1e-3ee7-bca1-51b56b8ff33b | -2.76858 | -45.51804 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db1093ce-cbfa-3239-836a-c79a07cf4611 | -3.87823 | -41.5898 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7dd713d7-80c9-3521-8643-85f6b81a7939 | -5.85339 | -39.94114 | 2025-12-06 04:31:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04ce39f6-f367-3bde-8b22-3e23dd4e53da | -2.10694 | -53.45679 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3781b8e2-7abd-301c-9727-5b61b8f896c5 | 1.9914 | -55.69624 | 2025-12-06 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 449c5420-48b2-3300-aa30-537b065d9dbe | -2.41153 | -46.47351 | 2025-12-06 04:31:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b48acc3-bdfb-33d1-8598-f4782b6ffb1a | -4.92602 | -44.17367 | 2025-12-06 04:31:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c41c188-e27b-334b-a992-5c19b8daedab | -3.87456 | -41.58521 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb406bc3-8a78-3992-9962-01490edb6273 | 0.33041 | -50.99201 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d52035f-caa5-391b-bd29-c54d0da10117 | 0.32335 | -50.9982 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79d05807-2eb6-3ae3-98c7-5d83e528b219 | -2.32359 | -46.16893 | 2025-12-06 04:31:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 061433f1-0564-323e-b394-e5fead2f3695 | -2.41433 | -45.787 | 2025-12-06 04:31:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 193e14e5-0525-315b-bbf4-c717665fea3a | -1.72307 | -45.7742 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89951db2-a7a3-397d-8338-d64c104d335e | -1.15946 | -46.70058 | 2025-12-06 04:31:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d08e3b-9c57-377c-9e3f-b1bfdabbd391 | -2.77649 | -45.51184 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1b34aa2-e870-31a8-a9f6-31cc1e73374d | 0.1267 | -49.91764 | 2025-12-06 04:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0469b09-174b-3b63-90e4-4d6ce4da03d2 | -1.85784 | -45.58476 | 2025-12-06 04:31:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6beb9db1-7c0c-35fe-a072-f0b6c1e91c7b | -1.37447 | -53.13162 | 2025-12-06 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35967b5e-b42c-396d-81eb-d608131928ab | -3.87488 | -41.58575 | 2025-12-06 04:31:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6088d62-ffad-346d-9d8d-1e97de368b45 | -2.65924 | -44.98475 | 2025-12-06 04:31:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede6bd11-839a-3e5e-8fcd-c6f1377307fb | -3.66059 | -43.55738 | 2025-12-06 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05162973-717c-30c8-9d21-be85445fa378 | -3.98325 | -44.319 | 2025-12-06 04:31:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3fb39748-8794-373b-84bb-f98b65696889 | -3.66432 | -43.55793 | 2025-12-06 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccdacdab-d906-342c-beca-a41f67fbabc1 | -4.31342 | -48.62391 | 2025-12-06 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a6cd01a-b315-368f-a144-a96da704befe | -2.33814 | -47.47711 | 2025-12-06 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bee9738-ecd3-3413-ad07-830d02c3e66d | -1.80986 | -54.65342 | 2025-12-06 04:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c810a728-b9b0-313e-9683-549d738bcb7f | -4.31676 | -48.62443 | 2025-12-06 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77a29f3f-052f-36e8-9676-c3111370cc0e | -4.40011 | -45.75135 | 2025-12-06 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c3a47d0-0f18-3c05-8b3c-76a9b3fcc6b5 | -11.65236 | -48.07664 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54a82616-210c-3fcc-9f02-e5ea3556587e | -11.65127 | -48.10584 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50c37172-d8f4-3008-ac07-35d151076277 | -11.63899 | -48.07452 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5033cf4-da39-3b57-9675-cf5235f41feb | -11.63954 | -48.07094 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84bccfef-febf-383d-a19a-58384360e9f9 | -11.63564 | -48.07399 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 695e7f68-6cd6-3ffd-84af-542cd4a6d859 | -11.63509 | -48.07758 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8350874f-b3f9-3400-9c1a-5627048b6f30 | -11.63454 | -48.08116 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fb6caa5-77ec-3bf1-be49-f056346de0ad | -11.65182 | -48.10226 | 2025-12-06 04:33:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5057b4c3-f572-31d1-a76b-4b3eed6175cc | -18.71023 | -55.263 | 2025-12-06 04:36:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3a2d80a3-ae1f-3dd4-b8b4-acf09f9894ba | -24.16393 | -49.57566 | 2025-12-06 04:38:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4ec4a430-819d-3511-8ba5-69564c37ca73 | -21.54864 | -44.30071 | 2025-12-06 04:38:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 36093980-0968-377e-91af-39135ac11845 | -27.31276 | -50.55979 | 2025-12-06 04:38:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b1e6837d-5459-39a6-bab8-5dc922b8a6e4 | -19.64106 | -56.83292 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 85f49d08-aa3a-3c3c-8a22-d62ebf527bda | -20.32696 | -50.19442 | 2025-12-06 04:38:00 | NOAA-20 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 524f3886-c81d-3648-a814-f7c18398cf5d | -24.09984 | -50.12664 | 2025-12-06 04:38:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9ff64fa-df30-31c4-a8cc-f193c1b18e86 | -20.92009 | -56.38472 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d4b4e3b-51bc-30c6-a97d-ea2ed0d8e132 | -22.08118 | -46.8238 | 2025-12-06 04:38:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd055afb-37d2-308e-862d-a1aa32436b54 | -23.36701 | -51.4045 | 2025-12-06 04:38:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87a7f6ca-4cff-39c2-94b1-5e51e865fc3b | -20.91617 | -56.38385 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41da1fbe-2946-3958-89df-2d2a1b89b7ef | -20.32362 | -50.19384 | 2025-12-06 04:38:00 | NOAA-20 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3e6102dd-a494-37e6-86e9-1c872f256bf2 | -20.92108 | -56.37936 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4be5358-60c2-3689-ae1d-1866e8bdf567 | -25.33267 | -49.87563 | 2025-12-06 04:38:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5515c5fd-2c73-3fdc-a450-4954c0fc48ab | -22.63834 | -52.02562 | 2025-12-06 04:38:00 | NOAA-20 | PARANAPOEMA | PARANÁ | Brasil | 4118303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 64ca5477-f3cc-326d-9a66-8390d6013901 | -22.42649 | -48.5637 | 2025-12-06 04:38:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
