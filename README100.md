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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a521637f-7f81-33f4-be7c-5d49f6d05a10 | -8.2476 | -45.481 | 2025-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9e91ef95-e369-3dc7-b8f2-dd87de2bcfab | -9.4007 | -54.6984 | 2025-09-29 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| f193ac23-1678-3f76-b58d-5e5bc894b29a | -9.8848 | -45.9349 | 2025-09-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c1e04c4b-9afb-3fc9-935e-f3ddab82bc40 | -7.8019 | -48.3173 | 2025-09-29 14:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| da0037b0-9103-3eb1-bb70-7dbae61b4e80 | -6.4602 | -45.8884 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| dfcb7c2a-4b7d-370f-9e16-a5d5a5d61ae5 | -7.5089 | -44.297 | 2025-09-29 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5bbf36cc-4c0f-3054-bfe0-747628c6ff48 | -13.3158 | -50.7011 | 2025-09-29 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 46d2569c-30e7-35f6-8ed5-ea7da4a4cba1 | -11.6649 | -45.3361 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 797cd278-1c38-39bb-b056-ea56f096d705 | -6.9048 | -44.5366 | 2025-09-29 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d1530faa-f1e9-3e9a-a908-1fc74dcf8f39 | -8.2958 | -55.1174 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 192da785-ac32-31d7-bde2-3c8f5b6b307f | -7.6062 | -47.3498 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9b91582f-d343-3d0c-8f1c-c48c77d4e8e5 | -5.8646 | -45.5958 | 2025-09-29 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a4aef30f-84dc-3813-a68a-684131e67e8c | -5.5504 | -45.1891 | 2025-09-29 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| aeb1eb42-f64a-33b9-9e7f-191fb38fda0b | -9.4005 | -54.7186 | 2025-09-29 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| d79757fe-a380-324b-b23c-b0cf7469ac43 | -11.383 | -45.0543 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7340f62f-8071-3589-9ce4-1aaca29c0874 | -7.7416 | -46.9626 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d530a52b-8df3-3038-a986-1f9cf30e602a | -6.0609 | -42.608 | 2025-09-29 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 63d2b24a-095a-3995-9a59-e73e3740c417 | -5.207 | -43.7714 | 2025-09-29 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 07ccb8ac-c19f-33df-9db6-117d6654a7b2 | -8.2102 | -47.0305 | 2025-09-29 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 177ea674-66e1-32ae-b4f2-399e3a915890 | -4.6828 | -43.8746 | 2025-09-29 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d0a82b0b-f6a1-338f-93b9-cbfa0b0bad1e | -11.6249 | -52.8416 | 2025-09-29 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| add33863-b109-3120-a4c9-d6d520d98833 | -6.6192 | -44.9493 | 2025-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 840c70e0-596a-3cd5-a3ae-221fe99ab464 | -8.2662 | -45.5018 | 2025-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 79afad53-8716-375c-9dd8-e6a91d966dfe | -5.8998 | -45.8404 | 2025-09-29 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 23c40cfb-525a-3395-9bb7-4c30108829ba | -8.71 | -54.6467 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| cedcad78-7437-3d35-8558-0b5fbdd8d2fa | -9.4458 | -47.5923 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 388ce9d8-566a-366e-a130-827a83215a51 | -8.2848 | -45.5225 | 2025-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 164a86c9-c6c8-3cfd-91bc-2f49d6a35c62 | -9.4554 | -45.509 | 2025-09-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 0f36cb52-6c45-3cb7-99ef-1e839a6a793c | -5.7917 | -43.2872 | 2025-09-29 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1fa3e50a-deea-3b3d-83d0-30dd8f315a29 | -11.9782 | -47.1296 | 2025-09-29 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 6ac9eed9-7fc8-3d5c-ac71-0ada84ac6bb0 | -9.0871 | -47.6294 | 2025-09-29 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2c0be785-5bda-3bdd-b2ab-24e15d8c1ee6 | -11.4417 | -44.9767 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 93217fe5-12c5-3ae3-8403-e7b6ca46e0c9 | -5.843 | -45.934 | 2025-09-29 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ce2a59cc-fcaf-3ae0-a54e-2812563f5ff9 | -7.6617 | -47.411 | 2025-09-29 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 82d7ceca-73c7-3c86-b8e6-53d637c92fcb | -7.8378 | -46.7544 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 525424da-e751-3225-958c-747457cb473f | -10.1628 | -50.464 | 2025-09-29 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 02b3fb13-21fa-3209-b54f-1e1b74255e5d | -11.807 | -48.2414 | 2025-09-29 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| deb8ffe0-03a1-3e58-a512-c51c8dd572dd | -6.2968 | -43.4331 | 2025-09-29 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 438978ab-f8a0-37e2-bd06-95531df92f02 | -7.8165 | -46.9781 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 64e39232-897f-3935-8aed-4ec93f7a3161 | -10.3896 | -49.0437 | 2025-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 202b0054-4feb-3f1d-ba54-55f7157a4eed | -8.5224 | -44.6305 | 2025-09-29 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f877ef56-ad94-3d15-9309-47981c661768 | -11.3834 | -45.0312 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 11d71bee-717b-39d6-bbb8-ca5995a9e962 | -9.4196 | -54.6767 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8c8724c1-6f91-31f1-b1dd-9617624c2ae2 | -6.3154 | -43.4548 | 2025-09-29 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ecf134c6-31e7-31ff-a7eb-f6bc85737131 | -8.2854 | -45.4772 | 2025-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9a705ae6-cda7-3ed4-a657-35a13f342288 | -13.5933 | -48.0593 | 2025-09-29 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| afc144d5-b4d2-3a92-90a1-36572abead44 | -4.4792 | -43.6094 | 2025-09-29 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bdc79faf-3a71-39bd-aefb-feb36d034214 | -6.0797 | -42.6064 | 2025-09-29 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| e785a02a-2d10-3290-8f1d-b649e9c1ac20 | -5.572 | -44.8472 | 2025-09-29 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 09779c99-cf96-3525-a42e-31f44cce68d0 | -6.797 | -44.0859 | 2025-09-29 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 56498138-b584-399e-9e10-7864eca096a7 | -10.8429 | -45.4044 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| f2d12aa2-3020-3456-adeb-d20e251c5eee | -12.9543 | -45.185 | 2025-09-29 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 9aea8384-2b58-32cd-92c7-f61c2014c435 | -15.5571 | -47.8764 | 2025-09-29 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 228595f1-7c86-348a-80c8-9676fd8a8a15 | -9.7864 | -46.1949 | 2025-09-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d6d39f6a-eeba-3575-a98c-07f4e199dba7 | -11.3642 | -45.0339 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 6a3502a2-6c8a-338d-8b8c-69a861f8858c | -9.8921 | -46.7437 | 2025-09-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f3ee2f24-e114-30bd-aaf0-f068956f6ce3 | -6.397 | -42.8152 | 2025-09-29 14:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 6520b30a-20e8-3d65-8161-8a2011f7ce1e | -13.7889 | -47.9181 | 2025-09-29 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 248.7 |
| ad021544-cb0d-3e16-80e2-f213881ff3d5 | -6.4604 | -45.866 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 58bbf4b8-e76c-3279-b257-5df4ef682c7f | -7.8163 | -47.0003 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 62da8f81-3157-3868-b2fd-6f51c4fb90f2 | -9.0913 | -45.8673 | 2025-09-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c55d2ec9-5ee1-3f92-b21b-a215ebeed767 | -6.5422 | -45.1601 | 2025-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| b201f8c4-f67f-35fa-8223-702120f90100 | -8.8059 | -50.7377 | 2025-09-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 46254a68-a116-3abf-8837-9e2e560713d7 | -9.501 | -47.6966 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 42203617-adae-3705-8a2b-3d210884bd48 | -10.3257 | -48.2001 | 2025-09-29 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| aa939e96-5d84-3508-a367-89eff36cd566 | -7.9006 | -44.6035 | 2025-09-29 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| f1ddb03b-e6f9-3053-9a93-82798ba814d7 | -9.3202 | -45.7061 | 2025-09-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4a3be8c9-b212-3ba2-8596-6bd2fd4c093e | -6.8266 | -44.8407 | 2025-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a38a13fd-93a1-3354-8ba1-4c3d913a76b3 | -9.4744 | -45.5068 | 2025-09-29 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0d42f3d9-01c6-3953-bcf3-493577f67003 | -9.2821 | -45.733 | 2025-09-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 4c425de6-77eb-3f3d-82ac-00e2e3cd74de | -14.6942 | -48.1557 | 2025-09-29 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 4abb7355-8919-30b6-afa9-a262295d66e2 | -8.5413 | -44.6284 | 2025-09-29 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a7b45f4d-6c82-3e35-9acc-97a57ae1b247 | -9.4009 | -54.6781 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b1fabba9-501d-351f-ab6e-f7b0f22a6e88 | -9.0425 | -46.7032 | 2025-09-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1ee499da-e1c5-30ae-a704-b78405673641 | -10.4022 | -48.1476 | 2025-09-29 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c2a3924e-8303-3a5e-9155-179e720e778e | -5.6223 | -43.3701 | 2025-09-29 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ae991ca5-ec75-3e67-b7eb-818db09d897e | -6.8256 | -44.9319 | 2025-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 7383730b-b908-3ba9-b9f2-f90799edb6cf | -9.0016 | -51.6875 | 2025-09-29 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 711cdac8-a650-3da3-9e47-ac20c2885190 | -0.1012 | -51.2738 | 2025-09-29 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 0dbebc45-7b65-3cff-aa3b-c9c8efa4b0c2 | -8.8896 | -51.6549 | 2025-09-29 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c0781830-1a26-3ab5-b237-e0482af8e478 | -6.6558 | -45.0373 | 2025-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a2cef9c7-ea01-30e9-8388-755b3777b0a9 | -9.7454 | -47.7806 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 7666f46f-db90-3290-ba8d-f5ab1cd02b73 | -5.8853 | -43.3032 | 2025-09-29 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0ff2dacf-db89-341b-9c74-19dcb452504c | -8.5221 | -44.6535 | 2025-09-29 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 99224dab-7503-32f0-8c5d-a2bfbf99e149 | -9.7264 | -47.7827 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9ddcfa64-f61c-3632-b4a1-5c3badd35874 | -17.4055 | -47.1199 | 2025-09-29 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 5e47eec9-7c5f-3984-ba04-16c97f6dd929 | -13.7893 | -47.8957 | 2025-09-29 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b0d36952-1e75-3635-8d91-4f2ddae0638a | -9.8852 | -45.9122 | 2025-09-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4185f5a6-c32f-36dd-b490-80cb45605b77 | -8.9456 | -51.6712 | 2025-09-29 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| aabd99d0-0c61-38ce-8e00-c4c2fde8fe88 | -9.0874 | -47.6074 | 2025-09-29 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 07f2db2f-5581-3dc4-9313-27a225b46c2c | -10.8425 | -45.4274 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4c0036f6-a396-3ec8-9f45-47d5a2f4b1de | -7.0291 | -45.21 | 2025-09-29 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 930c470f-fff3-37b2-b751-35547034a895 | -7.4676 | -46.2974 | 2025-09-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f01f2e3d-fb62-302d-9344-df6addfecad8 | -14.5668 | -44.9763 | 2025-09-29 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 330.8 |
| 8d70f030-9449-3259-ad09-3b06375c4e1c | -9.0685 | -47.6093 | 2025-09-29 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6f46814e-2838-3d6e-a833-e97c4bf5424a | -4.1759 | -44.2945 | 2025-09-29 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| df109ce8-8903-37d0-bf99-2dd0ddd26639 | -11.3451 | -45.0366 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 84c6c96f-ff7a-3008-adf0-8ba7a0c2c5b8 | -10.823 | -46.6538 | 2025-09-29 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c85951dc-78b9-340e-86fc-9ee58b9d4b6d | -6.4112 | -45.148 | 2025-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 996fde8c-0ce0-3685-aa5d-c9e20dcee02c | -12.887 | -44.6846 | 2025-09-29 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |


[Clique aqui para ver as próximas entradas](README101.md)
