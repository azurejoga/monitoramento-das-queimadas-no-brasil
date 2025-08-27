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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea10925a-a2df-3dd6-bb47-440e12f04e65 | -13.6097 | -48.2126 | 2025-08-27 12:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| a73b0e13-5c3c-3c78-84e0-b1f403833b39 | -8.948 | -65.9429 | 2025-08-27 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| e0dca1d2-ac36-3d72-94f7-d47c073e3f0f | -13.6102 | -48.1903 | 2025-08-27 12:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9511d666-747a-3664-a8f9-c87ef92ed16b | -14.1297 | -45.4043 | 2025-08-27 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 212a9b84-6322-3961-b8a6-35bec0e00253 | -8.9479 | -65.9616 | 2025-08-27 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 193.5 |
| b5c1ae23-3c35-3e7b-a725-7f8ea939bbfd | -14.1297 | -45.4043 | 2025-08-27 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e8600a38-597a-3984-bae9-c4e1d237a6be | -13.6097 | -48.2126 | 2025-08-27 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 0846a220-1fdc-37f7-9ab8-21e8d3b3dfdc | -9.4062 | -60.5326 | 2025-08-27 12:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 58c68951-565c-3e2c-8122-34bacb3d02a1 | -9.4064 | -60.5133 | 2025-08-27 12:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| b60c3596-5ecf-3c4b-a0e7-1fa01a3119eb | -8.8841 | -60.7699 | 2025-08-27 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| d0bd945e-d66c-3d38-9826-fee1f9af6386 | -9.9249 | -54.7192 | 2025-08-27 12:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 48bc7777-4d1b-320f-93d0-a0251717fa2e | -8.9479 | -65.9616 | 2025-08-27 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 244.2 |
| 2ec984e0-a091-358a-b880-8d9e6b8ac811 | -8.271 | -45.1149 | 2025-08-27 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 587.0 |
| 49994d67-0b82-3319-9d13-4906d1423a43 | -6.4355 | -44.5764 | 2025-08-27 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 71da4ece-c65b-37b6-b5b1-782ee840aabc | -6.4353 | -44.5993 | 2025-08-27 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 67037845-18e5-32df-b085-2d99dcdd2a26 | -8.4596 | -43.6645 | 2025-08-27 12:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 40975396-0990-338e-a31d-84a3460971d7 | -10.0977 | -62.9085 | 2025-08-27 12:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 147.8 |
| d54246dc-9494-3a0b-a1d3-c3ec872afcf5 | -13.4617 | -46.8669 | 2025-08-27 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9ccd41f6-0b68-3739-ac0d-54f8e5efc676 | -8.4593 | -43.6879 | 2025-08-27 12:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 9a3188f3-20c0-3637-a35d-0615fea399a2 | -8.9664 | -65.961 | 2025-08-27 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e5ed2de3-f205-3e90-ab06-53e8e6f25bf7 | -13.3838 | -46.9017 | 2025-08-27 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| fa7daf99-56da-36bd-91d0-4572b7f140a1 | -12.784 | -48.1543 | 2025-08-27 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cafb05c5-df4c-3b9e-8459-5e421f54b52d | -8.3936 | -47.411 | 2025-08-27 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f23b6cdd-632f-3810-a309-5ac27271c010 | -11.5694 | -47.6081 | 2025-08-27 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f8d19129-1aea-3011-aa52-9e7287f1f893 | -8.948 | -65.9429 | 2025-08-27 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| bd454b4e-b285-3c9b-a000-e08a6a3519ad | -12.7447 | -48.2041 | 2025-08-27 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 89ea2989-3916-3ce6-8987-4bdeca8f25af | -9.1009 | -49.5621 | 2025-08-27 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 2767da96-f866-3149-98bb-f9142d781c65 | -13.6097 | -48.2126 | 2025-08-27 12:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 151.4 |
| efff4349-6d73-32e1-b138-bc045370ab98 | -8.948 | -65.9429 | 2025-08-27 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 38e27761-6cb1-32a0-81d6-5b67cce30852 | -9.1009 | -49.5621 | 2025-08-27 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b5c1ebd8-f8ab-363c-94c4-65d1e51c1999 | -9.4064 | -60.5133 | 2025-08-27 12:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 24bb9c9d-4964-3ca9-be91-b81ff35776b0 | -12.784 | -48.1543 | 2025-08-27 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ca8bcdc0-5ee2-387b-9606-6e605f956f49 | -8.9479 | -65.9616 | 2025-08-27 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 316.1 |
| 3ceee748-2668-344c-baf0-0429f1978f49 | -14.1297 | -45.4043 | 2025-08-27 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1fff173c-8c10-3fda-b7fa-b7f29d9c258d | -9.9249 | -54.7192 | 2025-08-27 12:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a02389b0-612f-3ddc-a081-68ebb520abc5 | -6.4355 | -44.5764 | 2025-08-27 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 58def19e-5121-3132-b535-896b125970b6 | -8.9664 | -65.961 | 2025-08-27 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d58b30fc-5800-36fd-baa6-35d1d72a0bf7 | -6.4357 | -44.5535 | 2025-08-27 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 13e4bc0b-c809-3583-b869-8db014191624 | -8.4596 | -43.6645 | 2025-08-27 12:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 248.4 |
| b8796166-9370-339b-b22c-9b0e4b059592 | -7.4414 | -42.0501 | 2025-08-27 12:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 263dc5a1-f30b-3fe3-900a-c01805d73fc4 | -8.271 | -45.1149 | 2025-08-27 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 4479e98f-34f4-3e6a-9891-ab1f83936a02 | -11.5694 | -47.6081 | 2025-08-27 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d3ea80d1-309f-3d30-b6fc-dc443f8ef2d3 | -8.8842 | -60.7507 | 2025-08-27 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 237.8 |
| 5d72b6a2-6655-3f60-b0d8-7861f7b33e11 | -6.1783 | -44.0457 | 2025-08-27 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8e090ae9-51e1-3f41-843f-587dfc92e2c4 | -15.0975 | -48.4029 | 2025-08-27 12:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 797c5685-bc96-3ed5-8da0-a878b2d3b57e | -8.8841 | -60.7699 | 2025-08-27 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 450.9 |
| b11cfe49-7168-335c-ab92-cba5a60bba73 | -8.8839 | -60.7891 | 2025-08-27 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 83f26e49-6da7-3a27-b091-883babc4e09f | -8.4593 | -43.6879 | 2025-08-27 12:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 3efa2ea5-2233-3aa0-b45f-a2bf5ce02cb6 | -9.4062 | -60.5326 | 2025-08-27 12:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b221565d-3405-3651-9166-15b077790205 | -9.4064 | -60.5133 | 2025-08-27 12:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 0a39c32d-57f8-3fd8-a053-80e745385494 | -12.7843 | -48.1321 | 2025-08-27 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8f36cb31-67e2-3709-abe4-ce2ae160bdda | -10.308 | -46.8068 | 2025-08-27 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a5ef0eac-11b7-319c-89a3-7039628aa01c | -8.8841 | -60.7699 | 2025-08-27 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 510.4 |
| 1c4c1bb6-8b4f-3c9c-a2cb-6c703e2a8e50 | -10.2743 | -64.4907 | 2025-08-27 12:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f97537f6-445a-3d6e-9f94-5b17a4c0a5a1 | -6.4357 | -44.5535 | 2025-08-27 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e925b5ac-712b-3ec7-bc77-a2b1ee79497c | -8.948 | -65.9429 | 2025-08-27 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 170.6 |
| dfae5820-825b-3b0f-96e4-152f0a66d450 | -10.0977 | -62.9085 | 2025-08-27 12:50:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 201.7 |
| b444bc9d-576b-3839-b3ec-83121062c2c1 | -8.2707 | -45.1377 | 2025-08-27 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c435b62b-66ab-3182-b836-bb0dd3968c88 | -7.4414 | -42.0501 | 2025-08-27 12:50:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 93f77c00-9f68-3f79-a88f-a9e65b90ad2f | -13.6291 | -48.2097 | 2025-08-27 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| dffe48bb-916b-3ce4-a511-32cfd803562c | -11.8115 | -46.8158 | 2025-08-27 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7edf36bc-73d3-3eab-b02c-7d5e16939055 | -6.4355 | -44.5764 | 2025-08-27 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| ae291bd5-ed74-3422-b172-cf941323483d | -14.3912 | -51.9508 | 2025-08-27 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2fb084a9-e15b-3f4a-acb5-12e2ed15383b | -12.784 | -48.1543 | 2025-08-27 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 153ce089-2b04-3579-937f-8f22d835c521 | -9.4183 | -48.2537 | 2025-08-27 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3e522c47-e772-3973-ba00-7614c7fe2240 | -14.1297 | -45.4043 | 2025-08-27 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 54d8e7fd-9cf7-3077-8aba-41326ad73bea | -11.5694 | -47.6081 | 2025-08-27 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bf8939a1-457a-3af5-b28f-63317b801d2c | -8.4596 | -43.6645 | 2025-08-27 12:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 250eba04-6ac5-316e-b543-92ee7a36a7a3 | -8.9479 | -65.9616 | 2025-08-27 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 412.1 |
| bcf012fe-d792-335b-b458-224031ec95b4 | -8.9294 | -65.9621 | 2025-08-27 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8e1e596b-8416-3a2a-9521-17f4a8596d1d | -10.2742 | -64.5096 | 2025-08-27 12:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 5cd76572-da1b-3996-b0e8-dfc79efa1266 | -8.9664 | -65.961 | 2025-08-27 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| fc542449-3602-360f-aeb0-76d9a9b7c1e0 | -13.3838 | -46.9017 | 2025-08-27 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e79208a9-9ec4-3467-856b-099453d596c8 | -9.9249 | -54.7192 | 2025-08-27 12:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| e1f065db-486e-3efe-a6c8-e8812d1cba44 | -7.6414 | -42.6718 | 2025-08-27 12:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| bda5e54b-6f12-3861-8f8a-c648075bdde8 | -9.4062 | -60.5326 | 2025-08-27 12:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 5be56cd1-7ece-3a0c-9431-511e9133f7bf | -13.6102 | -48.1903 | 2025-08-27 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| db47b662-f4b1-3564-ad93-9dbe1f661f98 | -9.1009 | -49.5621 | 2025-08-27 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 893f7547-acba-34eb-a571-a9938f13984a | -6.1783 | -44.0457 | 2025-08-27 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 18b7026c-7bd3-3d57-ada1-18e3cbe6be0b | -6.8772 | -43.6152 | 2025-08-27 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 684a7eb3-cd4c-3ed3-a641-8e223a9f061c | -13.6097 | -48.2126 | 2025-08-27 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 279.9 |
| 04471192-4fef-3f89-a9e2-5f51cfa026b7 | -8.271 | -45.1149 | 2025-08-27 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 59dc9df3-6709-3248-a646-d884ff252a02 | -8.8842 | -60.7507 | 2025-08-27 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.9 |
| 9d13a48c-3ad9-314e-bcf6-8cc337fa0678 | -6.8774 | -43.5919 | 2025-08-27 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 403.2 |
| a32af5ee-76ef-3ac7-8b6d-8917437ce3a5 | -9.1007 | -49.5835 | 2025-08-27 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 77303af2-acf1-35eb-9c0b-40619ba6379f | -10.079 | -62.9094 | 2025-08-27 12:50:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f9120e21-9e5a-37e4-b318-2df9f962e18f | -8.4593 | -43.6879 | 2025-08-27 13:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d5c680f0-8200-312e-bd91-b15b07b1c287 | -8.9294 | -65.9621 | 2025-08-27 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f7e53736-0700-3fac-9cc4-970f4d5a11e5 | -7.6414 | -42.6718 | 2025-08-27 13:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a9805332-0c24-386c-82a2-b0fa56f5e56c | -8.8842 | -60.7507 | 2025-08-27 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 597.3 |
| 8f9f8688-705b-3d84-8ba7-5a5f2f795b3b | -8.9028 | -60.7498 | 2025-08-27 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3439c149-91f8-3c60-86d9-097212d84b65 | -8.9026 | -60.769 | 2025-08-27 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4f858460-a6df-361e-a8aa-9b7df4cb1d69 | -11.3146 | -43.5008 | 2025-08-27 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 63976e05-a7df-3f9e-8a53-c128f59e48fb | -9.1009 | -49.5621 | 2025-08-27 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 0cca3280-6196-3715-84e9-dd067e2a8fc0 | -6.4355 | -44.5764 | 2025-08-27 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 22f7425e-5085-3ef3-a117-35ab26754c5b | -9.418 | -48.2756 | 2025-08-27 13:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fc36f511-634e-3f12-b8ff-db83e6bc7dad | -12.784 | -48.1543 | 2025-08-27 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fe129ccc-8479-3242-bc47-4530935d857f | -8.271 | -45.1149 | 2025-08-27 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5d0a7008-7dc2-335c-89c3-5f7c39e6cda8 | -8.4596 | -43.6645 | 2025-08-27 13:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| a95d866c-02c1-3b68-b254-f00d142e89c1 | -13.3838 | -46.9017 | 2025-08-27 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |


[Clique aqui para ver as próximas entradas](README93.md)
