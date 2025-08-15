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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 673234d5-f1ff-3d22-a399-8e321f8ca5e4 | -7.81807 | -61.32602 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceb9fad6-1113-3da2-9670-3c5ca1803454 | -12.59065 | -46.95372 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce3745f9-e695-3da2-ae47-71593741b2db | -9.5341 | -63.57888 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b05b0a-7427-3dd8-ad74-8a117acafe82 | -9.16857 | -59.67153 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de6f6322-0c37-3ed3-8631-ecf5f3b753de | -9.15682 | -59.6871 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bdd80a0-2f69-32ca-996e-073df6f77c3e | -12.58533 | -46.95827 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3a6103c-0ea5-3c2a-9cdb-35ed890593be | -7.26606 | -60.631 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c8dbba4-1570-3645-b2ee-361d4f20a70e | -13.56682 | -46.96177 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff8b22c9-c687-3d22-a1ef-5c5d710fba0b | -8.04655 | -61.60017 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa99b86c-781e-31e3-815d-d787d36fb3a3 | -7.12092 | -59.62465 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 771518c6-5262-3849-a393-de214f51bb1a | -9.18532 | -59.67886 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 144aad6a-862e-37df-b795-c88173fef138 | -11.94091 | -62.83702 | 2025-08-15 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cae8e9bc-4ada-31de-8f65-eb598bf5d2c5 | -7.87656 | -61.81623 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90c6a879-0aee-3381-aa42-38950a2da9f6 | -11.77875 | -47.39778 | 2025-08-15 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87e09cb3-4c72-3958-85c4-3203753327b9 | -7.52671 | -61.37542 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5356bc76-8726-3a96-8de9-9811c587e878 | -9.16271 | -59.67926 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2777687-0e12-35aa-bee2-071bdd936d92 | -5.88924 | -57.738 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ebf527-0e6d-3bb0-890d-3b8efc80837d | -10.33865 | -64.44688 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 452a2aa0-40ca-3dba-90ce-550d342df6d8 | -7.09553 | -59.2212 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71a3b1af-10db-375b-8ffe-ce90da2c2b1e | -12.58662 | -46.94853 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9445af9d-4580-3345-b5c3-1a549d5eeca2 | -7.86627 | -61.8223 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c6fb9f5-d977-319f-bd89-0bc84e8f6d25 | -6.66005 | -58.81524 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8bee445f-540c-3f23-9051-0615a0cab1dc | -12.58266 | -46.94284 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e6ccbe9-7df2-3f37-9214-4fcc3735ef5a | -14.2398 | -44.58081 | 2025-08-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 00921920-a32f-39cd-9f17-733beff65f80 | -9.16346 | -59.675 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6b552eb-2c5d-37fa-938e-0fe094e851dc | -6.8806 | -59.1574 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5238b3e-67f4-3a21-950c-fd77c834ac94 | -8.52604 | -43.30698 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4339e52-c9ec-3789-abcf-d477c53bac61 | -12.58931 | -46.96381 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9ec8a51-672f-3a6e-88bb-43846946c0d5 | -9.50165 | -60.50912 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb728ae8-117b-3d7a-878e-5f433a3ae1ce | -7.29103 | -60.63017 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccee5167-626b-339c-8f24-937e356e0c57 | -9.72585 | -48.02787 | 2025-08-15 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17caa571-24dc-3e17-88eb-7757274c50f1 | -11.34703 | -55.41022 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 017abeb4-554b-325b-8da3-bdd14a2fc835 | -11.34803 | -55.42551 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 798ddeaa-0620-3846-b22a-976b70f01551 | -9.19858 | -45.33611 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e34d148-47fe-3549-8212-1b9ef0df98e6 | -7.08807 | -60.03609 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e1985f8-3b50-3562-b8c0-2971af1f97f9 | -12.3505 | -49.90904 | 2025-08-15 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ebeb9f4-f93b-36bc-9c04-1914a6e657b7 | -13.56977 | -46.96088 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3708b59-65a9-3a13-afdb-da7bf4b4432c | -6.90245 | -59.13496 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78584179-1450-36c2-8377-b5c259ee911a | -7.86685 | -61.81915 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39ace16f-aef0-342b-9984-a1cb3c7c3d74 | -6.9277 | -59.14632 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b00cf1a-6121-3ae0-b75c-fab0b80d58af | -9.19267 | -59.66254 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5354a937-7379-3dfd-b96f-9d44701bb478 | -7.01832 | -59.83833 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4773b1a7-c91a-3f7a-ad7a-e9375343fba0 | -7.07944 | -59.20963 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4ebb3a9-4443-3046-bccd-18a0094d8ba9 | -7.87085 | -61.81837 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9bd318c-263a-32d0-9f7a-1210fd108133 | -7.53175 | -61.34136 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2e89514-b97d-394e-a073-0f27ea6e6370 | -9.50373 | -60.52438 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 028c19fb-4aef-3937-af2d-552c11d1c46f | -7.87719 | -61.82097 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ed853d-b15c-3af3-a8d4-45b2116694fb | -9.83346 | -60.7596 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0427c101-ff9f-3838-9fe1-b2ebe0cd1db6 | -7.33134 | -60.62094 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c231c4c8-bfbe-370b-a51b-356f5f1ef43c | -9.1832 | -59.66516 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f04a865-8cdc-3de1-b3b1-ebcce3fa7f34 | -14.23379 | -44.58406 | 2025-08-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01b0b90c-b567-3c14-9af5-8336cf8f79e2 | -9.15135 | -59.42835 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44e67622-5b56-3313-877b-54f47663a099 | -12.57805 | -46.94202 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 031ef0b1-ef1e-316f-ac3e-06c9247b42da | -6.48394 | -62.93766 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6b2873d2-90ca-3858-867d-079d72cd74fd | -9.16993 | -57.00062 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40decfdc-699d-34b4-9561-5f281656ccd4 | -7.33801 | -60.61654 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa016889-8300-34a1-8bb0-088b92bca6d1 | -6.91343 | -59.15005 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24ac839-7d0d-3e58-8e0c-bc5a72bcf214 | -14.90287 | -45.18596 | 2025-08-15 04:51:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bcce0da-6fc8-3d93-a696-e08f9f98c384 | -13.11501 | -57.16129 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45dfe98d-77c3-361d-9085-5ee5e5c916f2 | -7.60322 | -63.52936 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50d250aa-89c4-374b-96e4-fc30d1b5a1a3 | -7.08091 | -59.22739 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e62c2fe6-f693-3d30-a7d8-7388e605e355 | -6.66795 | -58.82078 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae127da-cf2d-3ec0-a182-69bc594f440f | -11.34863 | -55.42183 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 34cadd3b-34b8-3730-b8ce-e8e2a0371a35 | -9.18907 | -59.65735 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5b7f841-22fb-3f3e-9be6-d27b322a0df1 | -13.57044 | -46.95573 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2aedd84-6b8c-3971-ada8-d8e33eff13ee | -9.0353 | -40.51839 | 2025-08-15 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fbe9b2dc-0172-3b08-b70f-41feee4cc1a0 | -8.31217 | -45.01771 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73b84ec4-4523-31e4-8dac-f78961835add | -7.53227 | -61.33844 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d125a51-20fc-36a6-8b3e-9ce099461df7 | -6.48516 | -62.94057 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fd8a229-0c7d-3412-ab45-a24b461b5cb4 | -7.13579 | -59.64631 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 220cfe38-9406-3a31-9007-4b7528c3676a | -8.19448 | -42.26241 | 2025-08-15 04:51:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd4ad8d1-a34c-3e2d-b045-d1ee556fbe28 | -7.09114 | -59.22044 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e08631bf-10b0-3f0f-97e7-3b068aca5428 | -11.40546 | -58.54638 | 2025-08-15 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85f35521-123c-301e-8a87-339274ccf450 | -11.35937 | -55.41985 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25bfa49b-1a80-35ff-9cd4-27255192848b | -7.32749 | -60.62006 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87ce457b-787f-3ffb-9a64-75c7e541dff2 | -7.27095 | -57.65908 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 943ca147-d97a-3043-847b-c705256be68b | -9.18851 | -45.3227 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f608b40f-3973-380e-91f6-7a9855163b70 | -11.34246 | -55.41703 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45a7d7cc-0abb-3e07-ac91-8310593ec5fc | -6.70802 | -58.81939 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99560c3a-be8d-3072-8f24-77a00d7233ce | -7.42621 | -60.0133 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6967cbef-875d-35e4-8553-1ca06b4b5f84 | -9.02784 | -40.5234 | 2025-08-15 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1ee87dd-e025-3da2-a43a-3a14268defb5 | -7.42976 | -60.01483 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d183fceb-604c-3cef-9745-cf76309ec27c | -6.08036 | -59.95312 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ba2aec-69d5-34ed-ba0a-d430bfcc5899 | -11.40635 | -58.54127 | 2025-08-15 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11985b17-e6db-36be-aae0-1a065cc355bd | -9.2123 | -59.6531 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6da0670b-ca80-3d27-85a2-a8546b314dff | -7.07285 | -59.22168 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05f5f909-2673-3d33-a309-c6857abdd1d2 | -6.93263 | -59.54026 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 818af6cf-7215-3bcb-ae5e-d87a244f8fbb | -7.52734 | -61.34172 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01e2bb05-1654-3322-a2f6-021ce53513ca | -6.67295 | -58.81749 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 495b7c35-b295-384f-be72-d15cf0a2a975 | -12.57738 | -46.94704 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ffbce2c4-f08d-3650-8472-fd38b33beb31 | -8.29802 | -45.00994 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5115f478-13ff-3ba5-a85a-7e989238d917 | -8.09543 | -61.18815 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19bac95f-fdc2-3d00-b926-4064bba2ae22 | -6.93342 | -59.53569 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 39bdd173-46b4-3f40-834d-004eada481e9 | -11.35699 | -55.4346 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20730e2d-46f9-3737-83e5-394bd689d33b | -9.63049 | -63.09706 | 2025-08-15 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bb87c02-7350-3e74-a72b-94088f778aac | -9.19118 | -59.67111 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46c66852-dcbd-398f-897b-f2e7a1b24df6 | -12.58201 | -46.94776 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 39b4b58c-17b7-3ac3-b75a-3c9bc5e6206e | -6.70244 | -58.85214 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4283c39-8893-3edd-85b6-49032a908cf8 | -13.11285 | -57.15238 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c141ec10-b875-3add-9496-5e42718ca2ce | -9.92071 | -63.18655 | 2025-08-15 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README51.md)
