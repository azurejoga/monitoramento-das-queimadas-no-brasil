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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64e1ef03-5865-37a2-9384-9c2c6ebbbf92 | -11.72016 | -44.50789 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2656f96-827e-3f09-a474-fe98e9f523bd | -13.57437 | -43.67351 | 2024-10-06 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6c5b665-1985-3ac5-a8dc-e6ac336b00f7 | -13.48329 | -43.66637 | 2024-10-06 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacfe405-9137-335e-b2cc-5a8fb6d0fa81 | -13.48284 | -43.66388 | 2024-10-06 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b797681-6000-309b-ae9f-3a62a795b7d8 | -13.0973 | -44.71045 | 2024-10-06 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07d18da8-7370-35dd-9fc8-30650d23b44d | -15.0543 | -44.11578 | 2024-10-06 03:55:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85a1da8a-f092-35bb-8c78-a65072589062 | -14.70163 | -45.13046 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71eafdce-7994-380a-8136-1187649eac0d | -14.69766 | -45.12962 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b011ee0c-89da-35d5-8bbb-4c10f257dee7 | -14.69669 | -45.13507 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c3a39c4-1db4-3549-bc0f-94deeacb31d9 | -14.48622 | -44.96138 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 582b3978-212c-396c-aaaa-d91290c864dc | -14.47339 | -44.96444 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb38908d-0ff0-3e77-ab39-0089a3410650 | -14.42668 | -43.78633 | 2024-10-06 03:55:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0652c10-3be3-3bec-830c-25d9d763c313 | -14.42605 | -43.78395 | 2024-10-06 03:55:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef063f20-c9fc-347a-a10d-92fbcbb0bc60 | -14.30022 | -44.652 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c683a4f-d65e-338a-bd14-4cd9eb1cab3d | -14.13021 | -43.71107 | 2024-10-06 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fff2f41-3ca0-3663-8ab5-d7616fa64b55 | -14.08269 | -44.47633 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b10976d2-834e-3532-a618-25ef3031631b | -14.08183 | -44.48128 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 927f5cf7-5bc3-3349-9c29-e76548b06ace | -14.07644 | -45.15437 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d363f1a-cd99-33c5-ab5b-d8d500c3bf68 | -14.0758 | -45.15801 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6f21194-416a-3027-94f8-fd35552b1c85 | -14.07176 | -45.1573 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e9e6c8-2cbc-38d2-b4b7-cde6d95033e1 | -17.81697 | -45.89751 | 2024-10-06 03:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f2fe3d0-69e7-3efd-9a71-cc17a32b4238 | -17.81599 | -45.9029 | 2024-10-06 03:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| adb62312-41a1-3528-90bf-b71ee6a5dd99 | -17.58785 | -44.51559 | 2024-10-06 03:55:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1a34c4e-bffd-33de-a0c1-046dda8d75b6 | -10.81091 | -44.77374 | 2024-10-06 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95328cb4-b4a7-38e7-83e4-5c84c6d99d69 | -10.6205 | -45.18463 | 2024-10-06 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5daa9bdb-3e42-31b2-88ec-47ac46ca6462 | -10.61795 | -45.18542 | 2024-10-06 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23f791e4-0719-362f-90c1-514d50963527 | -10.61726 | -45.18942 | 2024-10-06 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68f1fcc9-00d2-3498-9bcd-20a3c8f8ecea | -10.6155 | -45.18784 | 2024-10-06 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d923a7ca-2330-3adc-8bd3-4b728c56df96 | -10.61298 | -45.18864 | 2024-10-06 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24d36392-6f63-3ff5-8bdb-40f70550a164 | -10.48374 | -45.18379 | 2024-10-06 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 791070af-f217-3996-8282-620e9ffea189 | -11.67073 | -45.24652 | 2024-10-06 03:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a61f14-5bbc-3fc0-9948-7c6864ea4649 | -11.6673 | -45.26611 | 2024-10-06 03:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 168dbca4-6ecb-3b6e-b8db-d19703349a00 | -11.66585 | -45.24945 | 2024-10-06 03:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f8297a8-cbf8-35f3-96fa-bfc55bb96df8 | -13.10106 | -46.39383 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13ef152e-2ff4-38c2-8a63-e180b268d10e | -13.1002 | -46.3858 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b8ad40c-7be7-34e3-b654-985964e02eae | -13.09897 | -46.3671 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85ad17a5-202f-3899-8bf5-ad76beab46aa | -13.09873 | -46.34289 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30b6594e-90aa-37bd-ab25-1f41f492d968 | -13.09828 | -46.38411 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e80434ea-50c9-33ca-901e-683c1e530216 | -13.09781 | -46.34803 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be671c7c-9003-3331-bb39-6e81b26aa64c | -13.09745 | -46.38857 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68c816aa-93c2-33a4-8077-70650502f92b | -13.09697 | -46.35273 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60715854-5cc5-3775-8f5d-c2ade190caf1 | -13.09575 | -46.38498 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3225a05-25f0-3c28-bbe9-1e3a02bcf94e | -13.09533 | -46.36181 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71e1bb7a-0fb9-3574-b73a-07f45a841fb1 | -13.09383 | -46.38333 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1c910cd-e274-333c-b885-50a35b33851c | -13.09336 | -46.34732 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a656f103-0052-3afb-afd0-3e7b38b056f2 | -13.09253 | -46.35194 | 2024-10-06 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f745ca1-3c48-3b09-aeef-9dfaaa4fd97d | -12.5108 | -45.29367 | 2024-10-06 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 350ebea7-d482-38c1-afc8-d6390cd044b3 | -12.51011 | -45.29759 | 2024-10-06 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 887ea00b-1a40-37be-a15b-bdbdfe97fd94 | -12.50942 | -45.30153 | 2024-10-06 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 838ffb10-b79a-3bb2-8734-5f0a0d1c8d93 | -12.50523 | -45.30075 | 2024-10-06 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adfb9855-4465-3d7c-93ca-4e80c3b95553 | -12.50106 | -45.29996 | 2024-10-06 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c6ccaa-07ac-396b-a611-02606aa35869 | -14.20531 | -46.45358 | 2024-10-06 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15d786b2-b88f-3a0c-ba94-eff3d7309c92 | -14.20448 | -46.45803 | 2024-10-06 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f16fa06-3b30-38d5-a8b1-10e4f542d5e3 | -14.20097 | -46.45253 | 2024-10-06 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b07c1aa6-8b07-35e5-a73d-da68356ee826 | -14.08955 | -45.5013 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 127151da-bc0f-3e17-a162-bee5ba02216f | -14.08817 | -45.50901 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe85c8b-34cf-3c29-9ffa-7fab2b4a71b4 | -14.08748 | -45.51287 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce8d7a80-d938-32c2-83b1-a8a477a9f3d5 | -14.08679 | -45.51671 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583d3f5b-d2f0-3ac7-80ad-ce572e4ffd5f | -14.08612 | -45.49668 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 609864c1-53b7-39e4-9a6b-98f49d127103 | -14.08543 | -45.50052 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e2de7da-c13d-3a18-8db5-dd41626c4cd7 | -14.08403 | -45.5321 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f364f16-d811-36ed-9718-d843abe4877c | -14.08268 | -45.49212 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6010455f-816e-3a02-a7d4-a38be026cac4 | -14.07989 | -45.53133 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b53ea668-8f59-3140-a082-1cd5031cfeb9 | -14.07924 | -45.48755 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdfd185-4850-3a56-9691-7ebf6737d3e2 | -14.07511 | -45.48682 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efeb3005-dc8e-3e9d-9fe9-b71f44c8f401 | -14.07168 | -45.48226 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f94193-84d4-37c5-b74f-936185af835f | -14.06755 | -45.48152 | 2024-10-06 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a912eec-ddf5-32ca-aef0-968b304ceecf | -16.52268 | -47.03133 | 2024-10-06 03:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b84e74-e0e4-3fab-b4dc-9fcc4d13c179 | -17.62878 | -46.96334 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05ee364-3869-32a6-bcee-95d55d220519 | -17.62804 | -46.96729 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63398deb-315d-3207-b072-5e83e201cd93 | -17.62454 | -46.96237 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63093698-1cef-3ecb-a84b-7f682e8cb89c | -17.6203 | -46.96143 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26887fe8-4403-3c0d-a1b5-9498a087895d | -17.60482 | -46.94978 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0132e0b-9e6d-3e9a-a384-973dc210a7e4 | -17.58175 | -46.93172 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28746d08-c82f-3f25-9a87-0849020b77a9 | -17.57831 | -46.92657 | 2024-10-06 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebb1529e-0ec0-3b59-b5e2-070998e991c3 | -16.97069 | -47.12442 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f764b98-a86d-38aa-8fc5-62cc4499a3ab | -16.96994 | -47.12627 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07495b81-4c3d-367c-976a-ad0aea3a1494 | -16.96635 | -47.12347 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0409e755-d528-3174-85c4-8596a44d8881 | -16.9656 | -47.1253 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf1a8ff1-7b24-3be9-a730-f5570f5a7d69 | -16.9621 | -47.11989 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 559bfc30-d803-3148-adff-a632a4cb8da8 | -16.96126 | -47.12438 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f0aef30-ef1c-348b-a47f-e5b5e6a753de | -16.95689 | -47.12356 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c88e006c-d916-3786-963a-744ba96a3bd6 | -16.95253 | -47.12273 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee988aab-c726-34cf-b84e-bc949c762946 | -16.95171 | -47.12715 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49aee333-fff3-39cb-821a-39cc5d198bd4 | -16.94736 | -47.12623 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2b6623-0b5c-38d1-822a-901236ebceba | -16.94035 | -47.11544 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c438cab5-d9b9-394c-9492-700a740e43dc | -16.93685 | -47.11008 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09cec728-5979-326e-81ba-ba637657367f | -16.936 | -47.11455 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5106a9d6-dcd1-3712-95e7-a5bf45256627 | -16.9165 | -47.1699 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 20812770-5693-3786-9a83-9e3d0ad36896 | -16.91568 | -47.17424 | 2024-10-06 03:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| becfc32e-d0b3-377c-912f-aa7ba2001373 | -16.91486 | -47.17858 | 2024-10-06 03:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7dcf8b0-3319-3c7d-93c8-b0459370f064 | -16.91215 | -47.16896 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 378649d0-61e8-3f33-9097-7d04a6f1a919 | -16.91131 | -47.17334 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 85958aad-4890-392a-8464-b75f4b90aa78 | -16.91034 | -47.15456 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efac0874-2319-3426-bc74-2c9846ea5ccf | -16.90948 | -47.15912 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71cfd015-bec5-3430-9ac9-9b7a6c0e58a0 | -16.90863 | -47.16361 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9811d2b0-f676-3db1-8616-74848c9385b1 | -16.90781 | -47.16792 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cda8ad08-4f13-3275-8ad6-a8ce7e1e264e | -16.90698 | -47.17226 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c6b3b873-85b9-39ff-a9a1-4b893eff8a14 | -16.90346 | -47.16693 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8ed38324-ad34-3daa-84ff-5560c9bddff6 | -16.90265 | -47.17121 | 2024-10-06 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README54.md)
