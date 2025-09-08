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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c17b4e6f-9614-3bd8-aae5-366d83e7966a | -8.8821 | -64.2238 | 2025-09-08 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 86b201df-c282-3c56-95f8-cbebc33923b7 | -6.4793 | -43.9516 | 2025-09-08 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0555cd9a-0342-3082-9c77-92b35ecb8cd7 | -7.3799 | -61.6353 | 2025-09-08 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fc273b03-4df5-31c9-8d9b-a036918d8a84 | -9.4531 | -61.8147 | 2025-09-08 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 129.1 |
| ef1c8e44-bf33-36da-b9cf-97e661a9dd03 | -9.4345 | -61.8156 | 2025-09-08 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 370c5999-c1bd-3470-8514-7142b94f2447 | -9.4344 | -61.8347 | 2025-09-08 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d47c7022-5173-3ac6-8530-606539140e08 | -5.8982 | -46.0196 | 2025-09-08 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 031c793e-136b-3123-a75b-aa23085581bc | -17.1564 | -44.4266 | 2025-09-08 00:00:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| fbb3e2df-9e0a-3a7a-ba29-5a1a560ca6ad | -7.4168 | -61.6339 | 2025-09-08 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 78b4e447-5156-3885-aab3-9319cccc27e4 | -11.3748 | -50.3783 | 2025-09-08 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 804e826d-a7e5-3b9c-9196-65f6ce23dc9a | -11.2007 | -54.9992 | 2025-09-08 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 389816ce-7184-3304-820b-2d4f56ce710d | -7.3982 | -61.6536 | 2025-09-08 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c4c3b55c-92b6-374e-8fba-ed9fc65f2934 | -11.2834 | -46.4365 | 2025-09-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 43c7d302-1841-32ab-804d-0de9e7999997 | -7.3984 | -61.6156 | 2025-09-08 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 1f500a4c-e655-3eda-b31d-a1c4de013f86 | -12.9286 | -54.7949 | 2025-09-08 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6a8d2557-74f7-34a5-8e41-0d3989197bf9 | -9.481 | -60.4902 | 2025-09-08 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| d52f345a-6098-311b-9ef9-092c0a28a130 | -12.9289 | -54.7744 | 2025-09-08 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7b0013ea-c29e-3153-b796-3c7439076a3f | -7.3983 | -61.6346 | 2025-09-08 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 314.9 |
| 2b87fc68-83d0-32d4-be69-b586634471da | -9.453 | -61.8338 | 2025-09-08 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| cbe40d7e-fe6e-3814-b6ac-3e4ea9be44b8 | -20.6463 | -42.4728 | 2025-09-08 00:00:00 | GOES-19 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 876877bc-a8f6-3907-9e0b-41a887a0900a | -5.8796 | -46.0209 | 2025-09-08 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c9ec0469-8b11-3762-9a35-322916355aba | -12.0056 | -47.7728 | 2025-09-08 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 5fc9e622-4628-3172-af35-600d3a26572d | -12.9474 | -54.8135 | 2025-09-08 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e6d4ead4-205e-3a92-b130-d7f6693ddedd | -5.211 | -43.2833 | 2025-09-08 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 14d909bd-31aa-3b0b-9c70-2629ad4ea5bd | -12.948 | -54.7724 | 2025-09-08 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 3b9c2b0b-e5c9-3d0a-a0b2-f05f7d1e78c7 | -9.1728 | -59.3853 | 2025-09-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f1c350c7-c2b0-3b34-94d0-28cee1d350b2 | -6.6384 | -53.3566 | 2025-09-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 42560407-8d35-360e-bfc8-51078afdf9a0 | -5.8794 | -46.0433 | 2025-09-08 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 583607a5-886d-3c4a-822a-fbb35c0e82c0 | -11.2831 | -46.4591 | 2025-09-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c59bd387-3c33-304f-ba60-1fc952efac51 | -6.4605 | -43.9532 | 2025-09-08 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| ea34e5e6-eb65-36f0-a06f-b7cc671f04c8 | -6.6198 | -53.3576 | 2025-09-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cc7b2be7-ae9e-37dd-9657-bfa36640dc2c | -16.3541 | -52.9359 | 2025-09-08 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 62194d22-e6bd-30d9-ac12-7ff626800492 | -12.9477 | -54.793 | 2025-09-08 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 168.3 |
| b2efb86d-0ee3-39c0-9bbe-e5989785dd33 | -11.2005 | -55.0195 | 2025-09-08 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 1241210c-8fb2-3249-864f-95db83ca74c5 | -11.2196 | -54.9975 | 2025-09-08 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 60dd1795-b946-3893-9621-5bb3b785177e | -9.173 | -59.3659 | 2025-09-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1bf2882a-5662-32ae-99f4-84fb509a20be | -11.3745 | -50.3997 | 2025-09-08 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 78a8277d-5359-38a4-a05c-2ed960ed56ed | -6.8282 | -52.7938 | 2025-09-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e6ccb633-281d-3f60-a5e2-08eb4be4d805 | -14.527 | -48.7611 | 2025-09-08 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e43f4442-85a8-3d88-b049-90954320fec8 | -6.6382 | -53.377 | 2025-09-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| aa39114f-478d-30a9-92ea-bd65c42f0b5f | -8.6219 | -40.2058 | 2025-09-08 00:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 3c010b68-2cec-321e-9ed7-90e126a6ee79 | -9.4624 | -60.4912 | 2025-09-08 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| baf76905-b36f-3c93-849f-fa79c3bf3f0b | -20.6255 | -42.4789 | 2025-09-08 00:00:00 | GOES-19 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 22625645-661a-3096-8194-3fbbe5d23ec9 | -14.5072 | -48.7863 | 2025-09-08 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8780fc6e-46f6-3c57-af44-2678a3a172f0 | -11.3742 | -50.4212 | 2025-09-08 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c4204ee1-8dd4-3f20-a956-61b724e2268e | -8.8821 | -64.2238 | 2025-09-08 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3a844c69-0406-39d7-87a4-3ace19875972 | -6.4605 | -43.9532 | 2025-09-08 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| d75c063b-56cb-38b9-89ef-12c2d66a5885 | -12.948 | -54.7724 | 2025-09-08 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 55889f3b-4c11-34b2-b71b-aa7ad3310299 | -8.6219 | -40.2058 | 2025-09-08 00:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 257bf4f1-ae85-39a7-8d92-56277b31f380 | -9.4345 | -61.8156 | 2025-09-08 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3e2e2b19-8826-36c3-ab30-17f9cc67cbe9 | -17.618 | -40.0889 | 2025-09-08 00:10:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| 0d814646-5d90-3af3-8007-2e38295e8d41 | -11.2005 | -55.0195 | 2025-09-08 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| fef6618e-5ee2-3420-a78c-d9c031357399 | -6.6198 | -53.3576 | 2025-09-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0777f95d-43dc-3262-ab18-1d85906a5a4c | -7.4169 | -61.6149 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ed21f3cf-a196-3072-8798-32f2b6f389c0 | -12.9289 | -54.7744 | 2025-09-08 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 87ab3f1e-79e0-3da3-8aab-1c8bb54b1f4a | -9.173 | -59.3659 | 2025-09-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c121796b-d207-3cbc-99c6-97609efd900a | -6.6382 | -53.377 | 2025-09-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 56c3f265-5ba2-34df-9432-abf071bfa667 | -9.481 | -60.4902 | 2025-09-08 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 89ed2bcf-1c2a-334a-a428-d299560f779f | -7.3984 | -61.6156 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 7b21ca62-09de-335e-acb1-578bd306aa92 | -7.3799 | -61.6353 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d7fae0ef-cf92-369f-b084-676547e81536 | -10.0495 | -59.3547 | 2025-09-08 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a9a55c29-f94e-3ae7-8abe-e90f54284ded | -9.4344 | -61.8347 | 2025-09-08 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 17a34923-8f1f-3897-8ca4-9246b93ee8b7 | -11.3745 | -50.3997 | 2025-09-08 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8a7b9155-f249-3573-b743-97bce8524048 | -15.6666 | -48.24 | 2025-09-08 00:10:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 543f9cd4-31d5-3757-86a7-e9de92c90dff | -11.3748 | -50.3783 | 2025-09-08 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 352dea4e-061d-3a81-bda3-95cf93c6e162 | -12.9474 | -54.8135 | 2025-09-08 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8ca8fd8e-84bf-35ef-9006-9014824b0cbc | -8.6223 | -40.1809 | 2025-09-08 00:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 9eff8bcb-9d23-3952-8d82-b0dd776dda5c | -9.4624 | -60.4912 | 2025-09-08 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 53600b5c-95d9-3f3b-820d-3e5ccd670612 | -7.4168 | -61.6339 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| c1c1bfdc-7313-32d1-b8ee-df3aacab0cae | -9.453 | -61.8338 | 2025-09-08 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 58b86290-6fe9-37bc-8e5b-b1eda3607f99 | -12.9286 | -54.7949 | 2025-09-08 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 90415f3c-40ea-3654-8ed4-1892f6401351 | -9.4531 | -61.8147 | 2025-09-08 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 16607e7a-f3bf-3e85-8d7c-6eb772ffb2b0 | -17.6188 | -40.0628 | 2025-09-08 00:10:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 87bdd1b7-b980-3581-bef1-f3a2ae19edcd | -7.3982 | -61.6536 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7d8d673d-f7a9-3f98-ab9d-9a0b6b9f553a | -11.2007 | -54.9992 | 2025-09-08 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 4184868b-d132-3f97-8af4-ab25e0d4380e | -6.6384 | -53.3566 | 2025-09-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 788d961d-08f4-32ff-b738-8c1e416a551e | -6.8282 | -52.7938 | 2025-09-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| df9019e6-fc92-3c08-9a91-0e03ebcaee4f | -7.3983 | -61.6346 | 2025-09-08 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 267.2 |
| 9ca3956c-88f6-3c8a-9783-805d3b898a30 | -12.9477 | -54.793 | 2025-09-08 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| a53239ec-605d-31e5-83b8-d026501c130b | -9.1728 | -59.3853 | 2025-09-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 385b8ef0-63d6-3a88-b77a-090aea36384a | -9.453 | -61.8338 | 2025-09-08 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 210bdad6-4391-35f1-a7dd-65861b1d92a1 | -10.0493 | -59.3742 | 2025-09-08 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c3f4f26a-9b87-3dee-b4bc-1c921423fa29 | -11.3742 | -50.4212 | 2025-09-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 114727a0-5bc4-39bf-b2c0-e2c81ae3fc69 | -8.8821 | -64.2238 | 2025-09-08 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1994f9bb-4307-361a-8136-c56d1ef7a84a | -11.2005 | -55.0195 | 2025-09-08 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| eca81a99-e255-3734-99af-8f87f607747d | -6.8282 | -52.7938 | 2025-09-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a3a4ebb4-15be-3cc3-b350-22e988054e20 | -9.4624 | -60.4912 | 2025-09-08 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d58567ff-b632-30f6-992f-161d1d25ab16 | -11.3748 | -50.3783 | 2025-09-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b03de11a-abb4-3955-aef3-52058d75c97a | -15.758 | -53.548 | 2025-09-08 00:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8622c8a1-08c2-3aba-abb6-a76d3527f304 | -6.6198 | -53.3576 | 2025-09-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e4e587b9-5937-32d0-aed2-343e42809ee3 | -11.2007 | -54.9992 | 2025-09-08 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 80953b8a-ba52-386f-946b-6aed45760b1e | -11.2196 | -54.9975 | 2025-09-08 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 953f2e15-b453-319c-9af6-4bf1635701e5 | -9.4531 | -61.8147 | 2025-09-08 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 6e847efb-325c-3bb2-b80f-6658fc30c679 | -12.1699 | -43.9338 | 2025-09-08 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 55b35722-bf38-3cc4-aa3c-535ccd8f3375 | -12.948 | -54.7724 | 2025-09-08 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0a374f3e-d118-348d-8964-91ee276a91fd | -8.6219 | -40.2058 | 2025-09-08 00:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 92.7 |
| a48b27de-d376-3dc6-baec-9875bfc1c043 | -11.3935 | -50.3976 | 2025-09-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| cc87c129-6497-3bfb-b1ef-c753c1f31a0e | -12.9286 | -54.7949 | 2025-09-08 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4e4a8477-d96e-3693-b959-cf8dc92298b1 | -12.9474 | -54.8135 | 2025-09-08 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 5b9379df-5d53-3e20-b0bb-2a40b7391fc6 | -7.4169 | -61.6149 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README2.md)
