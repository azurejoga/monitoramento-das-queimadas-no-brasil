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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99a846da-0846-33cb-a2a3-4c271e87af5e | -7.47698 | -50.91308 | 2026-09-17 04:40:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cde5b6cd-3591-37b2-abe1-799d6021708a | -8.73771 | -45.33862 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e7cb78d-2663-3883-aad2-6e6eef7162ce | -9.83666 | -48.35265 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f86e9116-1efb-3291-9893-75b619f49722 | -8.22113 | -55.4625 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6fa3158-71f2-375f-8db8-614f348c1e1c | -9.95129 | -45.3047 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421f53e9-414e-336f-9fac-cb94ec16bb96 | -8.47824 | -44.69825 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53220c5c-c0fc-3f3d-8e52-35384f8b5230 | -7.57777 | -46.33535 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c879119a-48db-3b2b-a127-1ee6c39a614b | -10.98947 | -48.30656 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bf92a5a-3403-3671-83f8-72ca99bedce9 | -4.53289 | -54.91916 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9830ec52-d81e-3cf9-a8ea-fcd206805a55 | -9.81921 | -46.49525 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fa16011-e051-332f-b931-fa71c39df617 | -7.59229 | -50.46432 | 2026-09-17 04:40:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec3e704-4708-3f83-9b17-2b12af3c166a | -10.11469 | -45.62781 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffb85812-eec0-3b38-ae36-d565dac2280b | -9.89049 | -48.39156 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c375aad0-c0fa-326c-8df1-e210b3400acd | -7.58144 | -46.33593 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dce22d98-06ac-3534-9945-4910be5e68a3 | -11.52344 | -44.94453 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87eaead8-3aff-3821-aec9-7a3748773cb2 | -11.57156 | -46.87481 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e07a9583-9781-31d8-8714-3a14665ca56e | -5.61695 | -45.24399 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8305a21a-cdd0-34e1-8f8f-faf769f1724d | -9.61719 | -45.348 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db6de9af-2701-318b-a9d4-f388d03d43d9 | -9.10158 | -60.9729 | 2026-09-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c89e1aa-61cc-3f41-82b7-a849e772ed7e | -9.94823 | -45.29694 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 821ce746-b680-3285-b7d2-a3659346b852 | -11.16846 | -42.79148 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9bf61a0b-3a08-395d-b591-28399d786e97 | -10.79032 | -46.1864 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d5b2871-dd6c-3773-b714-2bd3011a209d | -7.1056 | -41.82372 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d4d0042e-4e64-3386-8f0b-58123ee434cc | -8.85299 | -46.92169 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5614e756-110f-3a5d-b89f-44f8e982c7be | -7.81706 | -44.81228 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b0876ba-249a-36fb-8a06-e43af6ed53c7 | -8.77208 | -48.75775 | 2026-09-17 04:40:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a931553-9757-3dea-bcb9-f682ac76bb09 | -9.75005 | -47.09939 | 2026-09-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2efe0b5-dff2-3f4f-987d-5a72c28134a9 | -7.83273 | -49.31553 | 2026-09-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a280cd61-c2d1-3cea-98d2-613180166a5c | -5.46122 | -44.96122 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19915d7b-ea69-3877-8a12-ff1fcc36f82f | -5.98397 | -53.58061 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8d38197-26c2-376d-9f46-12ffa8a8db96 | -7.14306 | -42.08928 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 78772cb0-5d57-36ac-bfc0-22096aa3a0b6 | -9.60209 | -45.33884 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdfb1399-5ed1-37b3-9a15-8fa76bc5990f | -11.5634 | -46.87841 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d11dd782-95ba-37d8-8a97-29493fa71060 | -7.37316 | -44.48542 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8d8bc19-4bb7-329c-9705-a6f0cc1bd235 | -7.85065 | -44.8126 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb55c8d5-64eb-3568-9222-d413c675fd0d | -10.6351 | -48.70904 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8f98f78-2d24-3dc3-bf32-6bd3c4c70795 | -7.3875 | -44.50263 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb58ad5c-a4e3-3b96-8619-c6471be6d68a | -9.46783 | -45.45156 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75721104-448f-3532-b97f-57c342ae687a | -7.07852 | -47.49324 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d8e4303-dc11-3bf2-bfd5-37de70cbcda4 | -7.94321 | -44.83059 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 6f4e9e38-4f5f-3d28-985b-ebe164ff475b | -9.3947 | -60.29908 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab77b2e2-8625-30ca-b0e9-62630d6436d0 | -11.5884 | -46.89107 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19f037e0-74a7-3706-9d9d-cc3ecc05e88f | -6.88561 | -45.46841 | 2026-09-17 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32fda6f0-1de4-37bc-994c-24dbc7fd2f8f | -6.10563 | -57.63406 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95d7956d-d89a-3a58-9127-168f886092b2 | -9.12169 | -45.73544 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 256f4e07-3df4-3851-ad60-ee61c4d30a18 | -5.83504 | -52.08697 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 350737bf-1d82-34b2-9821-c4edaa0e7163 | -4.49761 | -55.50348 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f360ddf9-e92b-3063-963e-4a6a92d5ffa3 | -4.52001 | -54.97016 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f234ff44-affc-39c4-bc6d-68cdd2b28af1 | -7.09918 | -41.83402 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0290fe3d-8234-3804-b6d6-dee6ec8ba82f | -5.77574 | -45.114 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 387c0d4f-2c19-390a-bed0-bddfae8df3db | -7.12589 | -42.17361 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b2b31ee0-5e84-3787-8542-e6ed2c7739b5 | -9.4092 | -62.70522 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de4974c2-bd09-37b2-8754-9d4d483add73 | -9.59963 | -46.64616 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef052f7e-97a4-39f3-b96a-27db608f63da | -8.39754 | -42.20537 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ee484ddb-5db2-3da7-9be0-76b163901c4b | -7.7266 | -42.49403 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 23809b3b-55b5-33a5-9f88-d90e0921ea01 | -11.64112 | -47.33449 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eb44328-cfc8-3990-b6ab-6bcea7d7755f | -7.01194 | -43.34228 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e420fa21-d420-36cc-b160-165b1ee13177 | -8.28563 | -45.64696 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3f6a36d-1a14-3487-9785-472d9d1a344f | -7.59606 | -46.05654 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31539f7e-3889-35bf-861d-640144f57de5 | -8.26356 | -42.18041 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 24c12b5c-8de5-3fff-b1ce-9beab9b2f548 | -9.40716 | -62.7148 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 66a7ebd3-b411-3e86-a232-57621d54cba1 | -6.4376 | -55.6078 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3972c1da-6ac7-34d0-9cbc-0e54dca343f5 | -7.4533 | -46.16125 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45cc987e-a349-3a6c-b28e-55c7df39fd48 | -4.41663 | -55.50161 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce57cb3f-2464-3f2b-a554-43c693bfe027 | -7.09756 | -47.50779 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dea83635-000c-38d6-b441-937690683e20 | -9.94966 | -45.28659 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c56b5e37-2ec0-3bfe-a21e-daedb125147f | -8.54386 | -44.48715 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 586750c4-27c9-36bf-992d-c96a1d8be3c7 | -7.09416 | -41.76005 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 85680c1e-f45f-333e-9e8c-7ccd311be848 | -11.04239 | -48.27368 | 2026-09-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c64f24ce-2956-3f4f-9934-900bd00010d4 | -11.61376 | -50.63083 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 506c17b7-8e82-34bc-b9ae-59214b4d4795 | -10.00018 | -50.27198 | 2026-09-17 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f2f9c5-566f-38b1-89d8-1e752df2473e | -4.48884 | -55.50208 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f8e540e-3aee-37a8-a341-a85b133fa9ed | -9.84812 | -46.91511 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6db10f27-f1d8-37a6-9af3-31c58ea6a7d9 | -10.76998 | -46.20592 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddbfe4cb-8803-3389-aeb1-5de66c73b896 | -8.48646 | -44.69955 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9931400-a4f3-3888-879c-1a646b168bf7 | -9.18327 | -46.75808 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c89512ae-6bf3-33b3-8622-2285dce3734b | -11.5462 | -46.88311 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e99f4fd7-7dff-385c-a083-f5c43afa9613 | -11.59299 | -47.30648 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f1649b3-5193-37e5-b78e-a4371cdd7386 | -10.53798 | -44.8654 | 2026-09-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8566f2c6-20e6-3010-baa3-02abd4453dda | -11.89425 | -43.82801 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18ccbe70-ce89-3c01-994d-096958790665 | -9.77177 | -46.61321 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b066a0a9-aa10-382f-bf0d-a15ae4921de9 | -7.96882 | -44.82969 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d186ce94-3453-3ddd-b62c-1c69c2e98cba | -10.83064 | -46.15219 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0c05e17f-d0c4-3263-8686-8a7ecdc61ce5 | -9.11854 | -45.72987 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cb8db3b9-1b0f-3959-b484-846e44d19a6f | -10.61489 | -46.09164 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce0dbe74-19b9-39ab-809e-8e285afe3b55 | -11.6405 | -47.33884 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bb46134-1266-3112-b977-8fc8c08913df | -4.45424 | -55.43997 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e7ea1ed-67d9-3c45-a7f3-7cbd2d2e575b | -8.61244 | -44.48499 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8868f8f0-a983-3f6e-b215-a875a93b6b11 | -9.18693 | -46.75862 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 277506bf-88b2-32fc-ae6b-bf014ff52c92 | -7.44354 | -44.57789 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82097384-6c0a-3d0a-8977-b1c683458d46 | -7.04177 | -42.07411 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca151f0a-062d-3fbf-8a9a-72ec1b3cac86 | -7.64911 | -44.33223 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8dc15622-47d1-34f9-ad37-68c72b2a9f38 | -4.13655 | -54.41803 | 2026-09-17 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cff22c14-ffcf-33c3-8de1-c7f4c84e8e2f | -12.14781 | -48.25516 | 2026-09-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b353384-95dc-3f23-ba3d-ce3939fb3d25 | -6.67533 | -43.65095 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7e51104-7337-39ed-82b2-ab5db43863c5 | -5.86561 | -52.0596 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27107a45-b640-362a-a156-ff6bc15c8f6f | -5.77328 | -45.10386 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 838d16c4-b3e2-3184-82a3-75ef1d2a936b | -8.56404 | -44.55639 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e4de2e-fa27-3ea6-af9e-398f5ce3a52e | -9.83288 | -46.50656 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf26ad80-dd54-31ff-b596-b17cadd43e0f | -10.04413 | -45.56208 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README37.md)
