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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 921cfbd5-733f-3230-94d9-797064cdf2a7 | -9.58779 | -63.49867 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc50fd5f-67af-3b66-aa5d-b11e0b90002d | -10.30134 | -68.86116 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61fef1ec-3daf-35fc-8abe-0153f60ef6a5 | -9.00407 | -65.93868 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b230086-f5ff-3f8c-af6f-3ad5c3a8922f | -17.6846 | -52.25654 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad775665-c2db-3c88-9a70-29e66681025a | -14.82252 | -54.70798 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b88ef1-a56b-3001-9d35-c495b059a5ec | -10.30636 | -68.86803 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92bbf318-8568-3771-a32b-51617d27653a | -8.99528 | -65.9314 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7f47f9e-5af0-3b6a-890e-6bd6fe92748a | -15.49246 | -52.95017 | 2025-10-21 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed1b304-3dc8-387e-8fc0-2df0d3d8a9a9 | -17.4147 | -55.0601 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd3739bf-8c15-3aaf-a2da-55af4b79f112 | -17.68106 | -52.24525 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cca7248-e4d5-38d3-8a7c-a54b304147fd | -9.72343 | -67.48505 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d6eb381-e072-34e0-bded-1e660bdd80a5 | -17.40603 | -55.06425 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7ceba4f6-eab0-3e16-bf0a-095090541c13 | -9.72278 | -67.48849 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ac6e088-3c3b-32f5-95c2-096c6c3c1381 | -12.04058 | -54.24269 | 2025-10-21 05:16:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77072f03-6945-3689-afae-6e2f8b4d757f | -9.3152 | -62.0138 | 2025-10-21 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89d1b801-93c3-3cf0-ad49-54f7b603c364 | -8.78354 | -66.72281 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b54ed50-6e30-30cb-898e-1d5e97548ce1 | -9.9909 | -64.7757 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8e85335-9310-34d8-80cf-3ef80221595a | -16.24511 | -52.5479 | 2025-10-21 05:16:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f69a9e72-f7fb-32d3-be09-acc1d8171291 | -16.5332 | -53.72902 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 663db7a1-245e-3269-8085-23ab51806a7c | -9.00994 | -65.93409 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9f98d08-7555-38fa-b048-5749d1b1ea86 | -9.59212 | -63.37838 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea99b250-bfa9-3b1a-aa64-6e6042d03ad3 | -9.5678 | -65.22038 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cc10de1-0cc9-3e14-9d78-1478c99697cd | -8.9943 | -65.93686 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5cca931-2995-3314-acc2-d847bbc2cb32 | -12.42326 | -54.49645 | 2025-10-21 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 197d3b26-ac7b-3a39-824b-6a1db8ca79af | -9.64068 | -65.25557 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 705fdfd6-9fa8-3d6e-b631-63038d0f4544 | -9.71555 | -67.4833 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83d9a001-7e95-3113-8a60-a5969746d29f | -9.7181 | -67.48396 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5359fb5b-3de5-3a0c-aaf7-42962624be0e | -9.37823 | -62.63196 | 2025-10-21 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e931ded0-5bb6-36de-8005-044ad3982eb6 | -17.68588 | -52.24577 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92017d3d-50cd-3a2a-85a8-31d251abb5a1 | -15.89566 | -59.60894 | 2025-10-21 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d80ab1fd-ce77-3504-957b-c5f3abbc6a3d | -9.71276 | -67.4829 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a22edaf-a83d-3c0d-a1de-b9363919bb65 | -9.64991 | -65.25726 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 729e3e9b-d4d0-3e57-bebc-0c45831b779c | -16.5337 | -53.72509 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c338b1-9b18-3af7-91c9-ed62db209946 | -14.8304 | -54.70907 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4cde8373-0648-3ccf-906f-c866bbbf2e13 | -9.24772 | -63.63337 | 2025-10-21 05:16:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c879e6e-5d19-304c-85bf-f2ba6a29f9d5 | -9.3774 | -62.63693 | 2025-10-21 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0743fff-547d-3532-9622-f8a4c06a9036 | -9.72152 | -67.48094 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffd7d817-08a4-3472-80ec-b5bea2dd0140 | -12.4216 | -54.41984 | 2025-10-21 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90856e9-2107-3b3d-9862-97b5298a8ee2 | -17.41939 | -55.05535 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 914ba5f1-422a-3af0-9470-785343fe2e99 | -9.58378 | -66.47727 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb6307f1-2a48-3107-a0ca-a84c33ef52a6 | -14.82576 | -54.71356 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10ea9f45-7f9d-377d-8692-d7abc71c14c5 | -17.41212 | -55.04885 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57e8ae56-4293-3755-9794-c326e2dcbe0c | -17.44217 | -55.03689 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8dfe9f77-25cf-359d-bf14-55c9cc1f25e4 | -16.52889 | -53.72856 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e136a762-8974-3f3b-8264-94d899ba3357 | -17.42761 | -55.02389 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 196c1efb-ea07-36e6-9319-5f7398c08e88 | -9.16656 | -62.58034 | 2025-10-21 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51d9692e-60c6-3b89-8643-74ec15aa0c80 | -17.43277 | -55.04641 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0281a887-2a3c-300c-9417-9ea8c09d6fe8 | -17.43818 | -55.03631 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fb2800d4-2342-3a76-868e-0ce3ad47cf30 | -9.04613 | -65.70203 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e046b539-80f2-360c-9ec5-0b4b136a3fed | -9.74664 | -64.19888 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 971b69b3-1252-3c86-94b9-f59d8bc11a17 | -14.79888 | -54.70487 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25c087e8-5809-3b4a-ad2b-6b680e268e42 | -9.80031 | -64.96728 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d640224d-dd3e-311c-af04-d3c7d5ba4af7 | -12.42251 | -54.41656 | 2025-10-21 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaabb958-4213-36b9-92c3-971f612e283e | -12.42184 | -54.42144 | 2025-10-21 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da4afbee-1980-3026-bf15-f76603b84291 | -17.68649 | -52.24058 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7cdd990-6c13-3baa-968c-70213959070f | -15.44217 | -60.21996 | 2025-10-21 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a90f6aa-6614-36b8-93a3-3a5e2e945089 | -8.99919 | -62.10081 | 2025-10-21 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6966940-74b0-3091-bcec-e2bb95c92b3d | -9.71493 | -67.48672 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb8c599-e620-3f38-a6cb-13b450803a6b | -16.53421 | -53.72114 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd55a6f3-78f5-3a6b-8345-95e5256341f7 | -9.18609 | -61.38581 | 2025-10-21 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e7d98a18-b878-3f22-bac7-8e150cff94c9 | -17.40743 | -55.0536 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 014815c0-eb14-30e1-916a-1d9341404d61 | -9.71746 | -62.06033 | 2025-10-21 05:16:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2250c1b2-4831-3133-b751-884f72bcf50a | -17.44617 | -55.03747 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e3bc817f-5686-3692-8cd1-0a0490d6a2f6 | -17.41142 | -55.05418 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90642476-4a8f-3b5a-b09f-5df776484e76 | -14.84848 | -52.43178 | 2025-10-21 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fd54101-f0cb-30dc-bc54-ff398839b2f1 | -9.25084 | -60.33317 | 2025-10-21 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2f356d5-8698-3707-bde8-5b56f9bee86e | -17.68336 | -52.26702 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b1ad1554-bddc-30e4-9b63-8f312290d114 | -10.30139 | -68.86258 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea88c75f-7b43-3f9e-b651-b577085c585a | -9.37073 | -64.34026 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48424087-a6af-35f1-9ec7-42933984981c | -9.6453 | -65.25642 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acb69b6d-8938-3156-b393-9afd6c9e06db | -16.5294 | -53.72459 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c65e3cb-1a0f-39f0-950d-5f3e60eb1bff | -18.17438 | -52.97232 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec817b43-2173-33ea-8ba2-2ba8786ecf8f | -17.9554 | -57.63667 | 2025-10-21 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2e974951-0c67-3f3a-998e-2777dc22c779 | -18.8017 | -47.01975 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4be1d6c7-9910-3cfa-8d33-859724c146b6 | -18.79674 | -47.01293 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bd884d9-586d-3c93-9d7f-51812b6be770 | -18.17282 | -52.97336 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bb3dbef-f107-3904-95a4-f32975d37b19 | -18.1907 | -52.98062 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b94cfeb-e857-3be9-9fe9-066808b8622a | -18.80358 | -47.0128 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 085083b6-f5b0-302d-92b7-b405d55940aa | -21.3672 | -55.93201 | 2025-10-21 05:18:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 537e0817-2a6d-3dda-97b6-a3eed0061714 | -18.80223 | -47.01395 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a0aa1f5-4033-3057-87f6-e237579884a9 | -19.09595 | -57.54335 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b0bcb266-d55f-3b11-b1b9-23c22cfe6781 | -18.59742 | -51.71871 | 2025-10-21 05:18:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0efbc40c-4bc1-388a-acab-5a3720c2faf0 | -19.09002 | -57.53379 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 605d02b1-a4aa-3d4b-b20c-1edad43b6383 | -22.29959 | -51.50812 | 2025-10-21 05:18:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2010253f-3188-3cc1-a95a-d681c79956a7 | -22.30494 | -51.5088 | 2025-10-21 05:18:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c60793a-de3f-33e2-9224-57ee357802ad | -19.10011 | -57.53971 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bd6df3e4-2f27-3b3e-adeb-67e89def0025 | -19.09655 | -57.53915 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d521f17d-28b9-3eaa-8ec3-8830fe966c94 | -19.09952 | -57.54392 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a8a97940-63e0-30cb-a49c-746fbda02886 | -18.8031 | -47.01849 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 517b1e6e-8d43-3fa0-928c-7a71043fc2dc | -21.36322 | -55.9314 | 2025-10-21 05:18:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ab4012b-6974-3908-8fbe-1dee4fe7ab00 | -18.16708 | -52.98249 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4329f5ff-cd7f-3f3c-9ff3-fbba232afb8a | -18.16917 | -52.97657 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3caf0e72-793f-36f0-97ea-07da2a6aed00 | -18.19184 | -52.97085 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81997ef9-d576-3ac9-9a4a-f464d6cd0f40 | -18.18261 | -52.96968 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6a0426-9c15-373e-9d61-7c5996abfb8f | -18.79623 | -47.01905 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 986abc3a-3858-3506-b90e-0a8af16af38d | -19.09358 | -57.53437 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ec4efd17-75c6-3b74-9e68-84523fb030eb | -18.17959 | -52.96806 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87712d68-27f3-3acc-b592-48eef951946f | -18.16764 | -52.9776 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd3a81b9-65fb-33ba-9349-a0b88cd1c84d | -18.16397 | -52.98082 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cc6dfea5-4e08-34e4-9554-66b720db62c0 | -20.48233 | -54.67833 | 2025-10-21 05:18:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README22.md)
