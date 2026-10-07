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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2f316fb-f6a6-3330-80e9-7ab79ef27b02 | -13.85403 | -40.64492 | 2026-10-07 16:35:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 342e590c-b5d6-3b45-b130-dfaac22059cc | -11.71063 | -43.66098 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a155a02f-9b33-3d0e-8f98-a8c7ed02623c | -11.72626 | -43.65128 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 1cdf408a-9cde-3022-a1a7-33857e626626 | -18.22211 | -42.92646 | 2026-10-07 16:35:00 | NPP-375 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 52331886-ee61-372f-8d5a-f9934785613a | -11.22758 | -44.86303 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8b30d018-9b99-37bc-8e47-aeffae9f6e21 | -12.31541 | -41.6619 | 2026-10-07 16:35:00 | NPP-375 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 123792d7-9a75-3d45-83d2-ca83fa5e6dc2 | -11.62141 | -43.67181 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 919fa8e6-80aa-3f0c-babf-19ba9c89af88 | -11.73628 | -43.64973 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d65be597-1c6f-3fd9-a31f-e5c8b12cae97 | -20.44088 | -51.98826 | 2026-10-07 16:35:00 | NPP-375 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73d411ea-7146-3deb-bb12-e6fed5b94e36 | -13.0191 | -47.19271 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 99f32616-03f5-367e-b187-990217fd6a1e | -13.57212 | -42.43353 | 2026-10-07 16:35:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 83a40c79-ea3b-3b20-8c0c-8a9fd4ed5944 | -13.68431 | -49.09536 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 6fb3b69e-2c9e-346f-bc73-513fb41cf893 | -12.16533 | -44.72561 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dfce0c2b-fd3a-37b0-b98e-58d42b5a8b9b | -13.67395 | -48.79652 | 2026-10-07 16:35:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4b1fed60-3100-3c06-9b4d-ff6ec66217ce | -14.36805 | -55.03156 | 2026-10-07 16:35:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae634f2c-f018-3c6c-85dc-6218f22f1c3a | -12.16422 | -44.71801 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b6a83190-96ae-3e37-82e0-fc02006e5d2a | -21.92761 | -48.95973 | 2026-10-07 16:35:00 | NPP-375 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 1985304a-ce65-38f6-a13d-92a551dd24cb | -11.37522 | -39.89603 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 6913dadd-4327-3284-81a6-ceab800b710d | -14.19556 | -40.2717 | 2026-10-07 16:35:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 12c8a045-4cb9-30ac-96df-429c07ceca5e | -12.93265 | -48.6166 | 2026-10-07 16:35:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 753a67e4-1395-374c-a790-53967ad821a8 | -11.73402 | -43.65737 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8d711228-149c-3be3-9025-e1d4c1bb567b | -11.84395 | -43.54131 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 291cda1e-1bc7-3ace-b19d-bd4ce42d9f42 | -12.531 | -38.67474 | 2026-10-07 16:35:00 | NPP-375 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d4fe5d1a-1ae0-3afd-92da-ab7c0ebe75a7 | -12.14024 | -43.30833 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8658b83e-f4c4-38d9-93c3-d58317a2781b | -12.18753 | -44.75721 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cdddef30-eea7-3550-be7a-b264a3696af8 | -11.62725 | -43.62003 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| a44de782-4d1f-3946-893a-10a2d8c25b7c | -12.18743 | -44.7806 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 377dd459-7142-3cce-a0e2-60f1a4bb918e | -15.32097 | -48.00983 | 2026-10-07 16:35:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2475ea44-b810-37a6-8e0c-056bc27eaed0 | -12.18343 | -44.77731 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 11c83685-d746-3a68-ae75-4fa2792fa103 | -11.78106 | -46.7811 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 121e7189-3826-35b6-9eeb-6b9db4e63e68 | -9.90646 | -36.1692 | 2026-10-07 16:35:00 | NPP-375 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 63a51fff-13ac-34b5-ad3c-7f520db40941 | -12.13006 | -44.95853 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 033070c4-1539-30bb-9c1c-220df18db94b | -11.83447 | -47.34876 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 921a6c22-9802-3595-bc73-0ee51d18bbc2 | -12.18297 | -44.75012 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 37ce0d63-3b1a-3990-8230-9597107a4c11 | -12.18576 | -44.76916 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| b68c5713-ff76-31d3-8567-4deca1dd9d7f | -17.49679 | -39.87816 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| d03c4b98-6b01-3483-bef6-3293a7d00af3 | -12.22655 | -44.72017 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 244a1b73-3756-3375-891e-e50b2a803da5 | -13.68898 | -49.10748 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 96f428e5-eb2e-3112-a267-f093d60b8be3 | -14.43526 | -40.80765 | 2026-10-07 16:35:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 88fd8303-c5e8-3a9e-a67f-b96f23d652a9 | -21.96449 | -41.15344 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 651fd3ff-2a27-3347-8440-3cdc19b9f729 | -15.14794 | -47.18627 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5053a690-31cd-38b5-9259-91266a44a6b5 | -11.82257 | -43.54902 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0bc45b52-750e-3c15-9b3e-1231e9525820 | -14.41347 | -41.33708 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 154.2 |
| ae9acf20-c20a-3fca-b3f3-00dda678d1ff | -10.49253 | -40.1657 | 2026-10-07 16:35:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b4c7a3d0-413f-3b0a-a605-4ab1494829e1 | -21.65142 | -41.35346 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ff0d8b95-8a3d-3b13-8c38-46643501fc4f | -18.03813 | -44.5729 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47def55c-a671-3965-96ea-1e96c51eb639 | -13.39475 | -43.87422 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ae60bb4a-acd2-392e-a6d7-37f6e8ee08c3 | -12.12638 | -38.39152 | 2026-10-07 16:35:00 | NPP-375 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 80c93b2e-43d5-3877-8abb-8efc202a2dfb | -15.14793 | -47.1868 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 522d2c25-5165-3041-b2a7-1e1ef97b69b7 | -18.2093 | -42.31857 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 46839f76-ba1f-3c45-ad17-d283e0107e46 | -12.17211 | -46.88401 | 2026-10-07 16:35:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b09e81e7-502c-3aaa-914a-509fb24de248 | -12.2271 | -44.72398 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5be7fa4c-b703-3932-a37e-83a528a72eb5 | -11.63873 | -43.68289 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6b584252-66bb-3642-b13d-d7ccc89b5f05 | -13.65237 | -44.78554 | 2026-10-07 16:35:00 | NPP-375 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2e6b16c-6a4f-3df2-8114-4f20957787a0 | -13.69837 | -49.0981 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b4c44c6c-c52a-3e6d-afc3-151c3b29ce74 | -16.85021 | -40.59778 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 48021f7f-1c21-3c58-b72d-f85bbbf61e28 | -14.41012 | -41.33765 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 154.2 |
| c2ea43f0-4f19-35cf-807d-a9aaf4971e11 | -14.40949 | -41.72847 | 2026-10-07 16:35:00 | NPP-375 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c4039b23-0dc0-3e3e-8172-80a45dacda22 | -11.84314 | -47.38153 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4bc45761-1429-3fc0-93e0-5608e13e36cf | -12.2249 | -44.70876 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9d69311d-c6fb-38b2-8e81-5b235a958cc6 | -13.73647 | -48.48003 | 2026-10-07 16:35:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2def3f7f-19d9-33ab-8c36-31dbb02daf62 | -13.39861 | -43.87323 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6c99abcb-57d5-37ff-9605-05450439e950 | -14.3625 | -49.53659 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ba7ca12e-b564-34a2-a3e7-1f59b28226fc | -11.58323 | -42.58253 | 2026-10-07 16:35:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 33b2fbb0-6c26-307d-9591-b8a7dd54fb6c | -19.18761 | -41.65817 | 2026-10-07 16:35:00 | NPP-375 | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 53bf4752-fbdf-3fff-81e9-f735212089c3 | -11.8394 | -47.38375 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d781a9ab-93f0-3313-85eb-28461e0257ab | -13.10039 | -39.0888 | 2026-10-07 16:35:00 | NPP-375 | ARATUÍPE | BAHIA | Brasil | 2902302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| be79ba50-947e-3228-bddf-51300b95f84e | -19.80937 | -40.63644 | 2026-10-07 16:35:00 | NPP-375 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8e905a50-6060-3fe6-8f78-c2ae4fd2550d | -12.22153 | -44.70165 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a8147b1a-3c7e-304a-a4ec-9fdd57e47728 | -10.91657 | -40.17749 | 2026-10-07 16:35:00 | NPP-375 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 810cdf50-9eb3-3da4-a099-98fe4f744ec8 | -17.43805 | -43.63965 | 2026-10-07 16:35:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1061c7b5-053a-32bf-bdf2-03791f0f5a4f | -11.83715 | -43.56432 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 0ef47a23-96e2-3684-a539-12e0cf20c926 | -12.95971 | -47.07454 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 94c274b0-4bc3-324b-9097-fd56e140159f | -11.85043 | -47.37711 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f1ec2ba-6588-3035-8733-40cae8f1effb | -13.44809 | -43.45135 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 042646b4-a1f6-376f-8495-ebc98036554d | -10.96828 | -38.80653 | 2026-10-07 16:35:00 | NPP-375 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 2962feb3-e0a7-3084-b88a-4ca0194e84a9 | -19.76585 | -40.26889 | 2026-10-07 16:35:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| 2e6c13ca-6ccd-3b55-a959-f0e5dd8d6c15 | -12.27667 | -47.17305 | 2026-10-07 16:35:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7d81ea8-b124-3e0c-ba5d-cdf7f317e67e | -17.49788 | -39.30854 | 2026-10-07 16:35:00 | NPP-375 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7f1ba2b0-3325-35b9-a50c-a4eae0e080c0 | -11.22908 | -45.2922 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 84f6228d-a545-3f46-8bce-798083749e9d | -12.22545 | -44.71256 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| dee5dbfe-e97f-3d29-b463-c7772df6e147 | -13.40204 | -43.47733 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7a3c5dfe-55b1-3263-b703-22d3130021fe | -11.84261 | -47.37819 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f246db12-8339-35d9-b1b5-e3c3bbc408b0 | -13.41478 | -47.22783 | 2026-10-07 16:35:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f286d25-03fd-3561-aee4-bb19a7cbee50 | -11.71171 | -43.6681 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 243cab29-a608-393a-b8d7-a6c99019dd10 | -13.68938 | -49.09935 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| ed2c29ff-e133-3e29-810f-cdcc6b50793a | -11.84638 | -47.37596 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 84af4a6f-dbda-3afe-b016-3858c6a24b85 | -11.55142 | -42.43953 | 2026-10-07 16:35:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b6eaddb-f390-33d5-aa79-ee1c8881bf4b | -12.45205 | -38.57768 | 2026-10-07 16:35:00 | NPP-375 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3fe42dad-e298-3cf2-b7d9-cbe594e230ac | -10.44988 | -36.84667 | 2026-10-07 16:35:00 | NPP-375 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 031afa3c-85ae-3ade-bbb9-873c2648148b | -14.24581 | -41.39437 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 38509655-92b9-3251-8cbc-566a4b31fe08 | -14.854 | -44.23674 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d82822a-c994-3e23-b7fb-cf9c28e58826 | -12.14078 | -43.31188 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 286edfe5-b5ff-3390-b256-29f36f8c1846 | -11.78421 | -46.7761 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0ca26b4-e5fd-3952-aa8e-70975b05f4df | -12.23452 | -44.72672 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 68e9caf8-4a10-3cf4-8633-8f6402eb1b82 | -12.20367 | -48.42345 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e5a1312e-554d-3673-95ee-6c01293be8b6 | -12.21362 | -44.67189 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 83230cf1-9db2-3132-b2c6-18cd4d418da2 | -11.22551 | -45.2612 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09e29087-58d9-3473-9bb7-3dbf3dcef1e2 | -11.22824 | -44.84368 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b59649b1-a098-3525-a8f0-f11c08f1b15b | -12.21817 | -44.67892 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README184.md)
