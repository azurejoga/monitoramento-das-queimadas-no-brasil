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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54603b80-a348-3cfa-9d6a-62547505abdc | -15.06607 | -48.7197 | 2026-08-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04bd68d6-ce70-3352-ac6b-e7e6e887529b | -17.35531 | -45.61979 | 2026-08-18 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20899c05-c885-3564-bb3a-6d72220ef32b | -14.8113 | -46.65216 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| f24f9182-2120-35c7-8311-1ee48a339315 | -15.91778 | -55.54233 | 2026-08-18 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73ff967f-9efa-3fee-881d-f3641d1fa1ed | -17.10297 | -46.58459 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2a57dd-01fa-345d-a7e7-533539a448fa | -11.12168 | -47.27028 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 35a402f3-c2ba-3e76-98d8-eb335656d99e | -11.11735 | -46.49832 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efd173ca-38a7-3e5e-8fd7-fb509ff0718e | -11.52529 | -46.6319 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16a410bd-c881-3fb9-a57a-90010db3ec08 | -14.16011 | -52.91673 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 01b7de61-9f09-3311-9da8-897b6361f02b | -14.47819 | -45.67321 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca2f7855-f7c0-3a45-a784-d820a125b662 | -13.28095 | -51.65639 | 2026-08-18 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 272221a1-d9b6-38e1-83bd-e05a16563817 | -14.84527 | -46.64351 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2be58dc8-ffcf-34bd-9373-61668662b793 | -13.44425 | -43.84246 | 2026-08-18 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 312f6a59-5f94-3a3f-a149-a10a8253cc49 | -14.04642 | -53.69244 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85100ea0-f32b-362c-8e9b-012f33d9fdb4 | -15.06519 | -48.72447 | 2026-08-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e12ba2b2-597d-3276-ac46-49fdbb906720 | -14.84916 | -46.64422 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7166e9d-c450-36f8-845c-270e8062e2ab | -12.54135 | -47.84491 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5858a6-dfc0-3570-abab-0a864adfacbd | -12.51769 | -47.87352 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b1e6c57-3d74-33c0-8b84-c3db6dc4308b | -14.35402 | -51.93951 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08fe9285-7698-39c4-ba01-e7a41aecff28 | -11.13656 | -47.28651 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbf9705-c757-3083-bf13-3981e1935d20 | -17.46004 | -47.86596 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b886aa5b-ec0d-34b8-86ce-08dc8664aaab | -13.45819 | -51.79729 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe5efac-43d1-3491-b353-cdf62da6918e | -12.76543 | -48.42557 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c53d145a-bf3e-3d1c-a3c3-081ee4351683 | -15.91442 | -55.5574 | 2026-08-18 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 80e6792a-3432-3d60-ad1f-3e270123a0a7 | -13.4212 | -54.38992 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c573cd09-8118-35a8-941b-711b8600b81b | -14.81295 | -46.64414 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5cac8162-521f-3cdc-8d23-63de3001d4c2 | -14.23373 | -45.41282 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d69e33a7-1ce9-3458-afda-627c86ee5f8b | -14.17882 | -53.05434 | 2026-08-18 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce272b87-8ce7-31fc-91ac-3234af7aa55c | -14.80916 | -46.6413 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1ce2b9a6-f125-3cde-bd2b-bc6452845de2 | -11.33837 | -45.93185 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70229c4e-5a80-31f0-a570-5afa58092473 | -17.9767 | -44.42793 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71960365-2cfc-34bf-ba3f-16ddd011e046 | -11.508 | -46.60969 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3408c4c9-2128-3877-be0c-fba0fc9ac302 | -14.42255 | -51.88433 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84b0db60-b1ef-390a-a908-4823fc4f6ed7 | -17.98562 | -44.43731 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81fc44a8-a7a1-350e-bb8a-fb52d6263a41 | -14.42329 | -51.88065 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c581bf7-8c31-34c4-9565-46286e103ec1 | -11.12677 | -46.49255 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78d44391-1948-32ec-9bba-f2a686c5638a | -14.83138 | -46.63117 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 771dcea5-0892-3e91-90dd-adb592b15380 | -11.53562 | -46.63844 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf85d8b-54f4-36fb-959e-f7c88aec2189 | -14.50041 | -45.67725 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d4d19de-9e2e-3b9c-82aa-ff1069e9212f | -14.26764 | -51.91478 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0432e8-d224-30cb-8de2-299569196b22 | -17.10307 | -46.58702 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f91462c3-90f9-3780-808a-6de4124698ef | -14.16528 | -52.91156 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7128b253-b4ed-39ea-a337-3996e6a1a127 | -11.29782 | -46.32641 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e610dafc-fa88-3184-bed4-a9e1c7d5481d | -15.38888 | -52.79593 | 2026-08-18 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c632e938-f274-3874-8888-f1167d57fb9a | -11.12358 | -47.28447 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56f1edf6-3d68-31bb-9181-782c0bc0b391 | -11.12521 | -47.27541 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 0602ce97-3d18-35c9-901b-f67690c1d781 | -14.81308 | -46.64192 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ccccc375-fa28-3cbc-8aa1-192dce19c0b2 | -14.18016 | -52.92857 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5d0cebfd-48b8-3057-90f3-deca301046b1 | -14.35951 | -51.94079 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba3bb977-73bf-3080-9b4d-6cfbc70a425e | -14.49379 | -45.67135 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdffc677-cb4a-3876-ac1d-7447416e203e | -11.3625 | -46.38615 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a098ba20-67b3-3550-9c3f-267e57777279 | -15.24517 | -56.48177 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc4e024f-ea25-31bc-ac5d-d2b26e4eefaa | -11.5322 | -46.64094 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0f135dbe-638d-35e0-839f-bdde30c6fd02 | -13.42086 | -54.38816 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cec2f0fe-9415-368e-86d6-4a480777c701 | -14.35602 | -51.93252 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc8078e3-fac5-398f-8f44-522328b78df5 | -14.81387 | -46.63902 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 27d68f85-bafe-34aa-8a0b-0f08a3909a54 | -11.62359 | -46.77925 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 417245c1-5f49-3a0a-bcb2-612a3efae59b | -14.35676 | -51.92878 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f64cff6-9c69-3624-918d-37d4594e94c3 | -14.36217 | -51.87223 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11832d15-2e8d-383e-8d94-006b5f507296 | -11.12611 | -46.49643 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3763da4-f3cd-323d-9b11-2132bb38555f | -14.35454 | -51.94003 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e60b7e98-90c5-37e0-b801-f9e4a216311c | -14.18102 | -52.92438 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2ff53d88-9a7c-3aa8-89e7-4c9b2b03c0b4 | -15.29045 | -56.44569 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10a55f97-0675-31c2-9446-76a724517842 | -11.53287 | -46.637 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| be278ec5-716d-3e80-90e0-91f648972bc6 | -14.2724 | -51.91966 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63f7ab50-1b3f-3431-97f0-c3bbd8f6e918 | -12.54571 | -47.84573 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8008591f-fa68-30a4-b147-84809af50a82 | -14.16286 | -52.90306 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 916c0a35-09fa-3e97-8499-bab3a84a3700 | -11.12874 | -47.28053 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbc51a1a-2085-3f99-99fa-4618a4d22dcf | -14.80828 | -46.64638 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1eae7ff8-904d-3bff-b803-c8b4a261fb0c | -14.35479 | -51.93575 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1901bd27-1538-3cb8-8108-87f0df862814 | -14.82268 | -46.63482 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d4abb3a0-9ca1-36bc-8033-39796101a83e | -14.16837 | -52.92621 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7015c032-4c4c-34f1-be5f-1a87a6f3fa8e | -14.17834 | -52.93731 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e3c9f3f-1fb4-311c-939c-30877f21970b | -12.46897 | -54.20123 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae06a8b3-1f01-36bb-8b04-6f26d6a368c1 | -17.95044 | -44.43897 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2adc310-024a-31ef-92b4-1dffda3567de | -11.30464 | -46.33501 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b420a869-c35b-3616-b7bd-04b2fb273ab6 | -13.41592 | -54.38266 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5d4900e-7f0b-35c1-8c1d-537f095df34b | -15.07407 | -48.72601 | 2026-08-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5909f08-a499-3261-ba77-2175bf9e0f26 | -13.41711 | -54.37692 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ad30df2-3566-3be9-8ab8-d2ffbe1ca73f | -14.83549 | -46.65316 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8feb89e9-ff0d-3bae-b7c8-76eddf0cd154 | -12.75618 | -48.42499 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89339fd8-ee3f-3103-b3b1-a0055fa6772a | -11.20441 | -54.82077 | 2026-08-18 04:04:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 668cc0cb-fc0d-3ff4-99ea-ad57e1b76162 | -14.87424 | -46.63878 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 717b4bb9-b91a-35c3-a95f-9f0bf5e747b4 | -11.51911 | -46.61875 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5681b4ea-7497-3e3a-886d-601a1fcc5591 | -11.11332 | -46.4972 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2647ba15-9cac-3894-9b5d-089df4a1ac2c | -13.28324 | -48.69344 | 2026-08-18 04:04:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7880a80-0c60-3522-9c01-f6e79f3274e5 | -14.43205 | -51.89402 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf5bbb70-1ed7-3b1d-88fd-adce3b88fcb6 | -12.75773 | -48.4166 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9c65fd6-eab6-3ccb-b0e6-1a077ea916c8 | -14.17788 | -53.05892 | 2026-08-18 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f855a59f-0a4b-31c7-8ad7-2c92dd6163e9 | -17.45602 | -47.86517 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6ac493f-0281-3e47-a000-fec2b5c5113d | -15.43895 | -41.38533 | 2026-08-18 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d954a5c-9826-3af5-80ed-f974e61d9ece | -13.30758 | -40.79419 | 2026-08-18 04:04:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b16e9962-7ca1-3fa0-9f21-e1a907b23f58 | -11.62133 | -46.77942 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39282ad0-2102-3114-b125-f000b603c6fc | -13.79203 | -53.8441 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d966e1de-aa8f-3f2e-a890-fb8554b837dd | -11.5087 | -46.60563 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68996222-3b9a-3b93-b4d1-f8417ab47b2a | -14.82744 | -46.63068 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 354f965e-7ea7-3265-a107-36324d0ce4fd | -13.55734 | -51.6998 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbccc9f5-dfbf-317b-8eff-50b0a2f18273 | -11.46 | -46.57044 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09498afe-0785-3d41-898f-d5b3ee314077 | -12.01309 | -46.4985 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef89b289-db54-3515-a9b7-ba85cf43773e | -13.7847 | -53.84788 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
