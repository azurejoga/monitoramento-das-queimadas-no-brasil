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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d6e1468-65a8-3755-aa8c-208c9b3e5f83 | -12.40941 | -47.78282 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dae7d122-50ba-39a5-a0f2-0aadfe2fa515 | -7.82334 | -46.88225 | 2025-08-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40b29484-41ee-3d53-8417-3d91f0beff78 | -10.48438 | -44.33135 | 2025-08-08 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a20a303-247a-3ce5-ab62-073b3e6bff98 | -8.86625 | -47.27437 | 2025-08-08 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a80e9ff-24af-3cf9-8a59-36b09ef1bd76 | -12.99923 | -47.49142 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cf40ce0-bb70-3ac0-9d6e-36c6b21386c5 | -7.89252 | -45.33351 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c764306-e9fa-30f2-a8bc-ba5346b6a046 | -12.70093 | -46.3859 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00d0035f-b65d-36dd-b635-21cba93e241f | -10.63069 | -44.76106 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 7b8ee1fe-892a-32e1-8b0d-7cd5ba7715cf | -11.77358 | -47.39686 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55883223-fe45-3fff-b829-71872631c9a1 | -7.35517 | -44.69384 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79932249-1994-31f4-970a-9899405fb2d4 | -8.16193 | -42.42009 | 2025-08-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 72434bb5-7145-39f0-a933-e4df81c1a25d | -11.76823 | -47.50369 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad3c9a00-0adf-3848-bc2c-84bd8340de6d | -12.55463 | -47.13887 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c46b252-f48e-3166-a082-24a4696800c6 | -11.19141 | -51.43715 | 2025-08-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a24d2d5-8759-3285-a33f-0c85fdb6e773 | -7.2575 | -44.33595 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a82348b-7dd1-367c-9cd4-eee5acf9ee89 | -11.65539 | -46.86853 | 2025-08-08 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afc7d641-7293-32b9-871c-7a14a6ab2232 | -8.20053 | -46.98828 | 2025-08-08 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33487603-486c-3f8f-84d5-0de6600f9c4a | -7.15055 | -44.08884 | 2025-08-08 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c1cf16a-8c2d-3d49-8e03-86bf98d324a6 | -9.6534 | -43.83901 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b62b919-a6e0-3ebe-9864-c9fa1951dac9 | -9.70573 | -61.30964 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1fd857e-7aa4-3a55-abca-0f5cc1f3989b | -7.70156 | -45.52373 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e126860-da8c-342c-986c-b72b6b65cacc | -7.58523 | -44.90663 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ee779f8-c7da-3731-bfc7-dd26c7fae676 | -11.74196 | -44.95904 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d7a06ce-eafb-32aa-9a8c-78bd52e07be2 | -8.46621 | -45.7083 | 2025-08-08 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4e8de5e-5809-36a6-8c1c-c054033db6c1 | -10.63759 | -44.75908 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 964a2a4a-10a3-32fa-9f55-0a597c42fa5e | -11.43814 | -45.14063 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb84dca-cd8b-3e3e-a62c-9054a7d05688 | -11.76483 | -47.5032 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 959ad3fe-d62a-30b7-801c-f9984d20b6af | -10.83162 | -49.38009 | 2025-08-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9080020-89c0-3ca0-b17e-6bad91374cae | -10.31768 | -48.31497 | 2025-08-08 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc020585-c603-3dd4-b074-e96ad0b07ad6 | -11.02737 | -45.06697 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4c595c45-76bd-3c61-9ace-b12781246daf | -9.0734 | -45.06103 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41224f43-859c-38b1-826e-09e9cf4b5988 | -11.78361 | -47.51723 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d6c4bcf-9961-3f1b-aa35-aa9d39066f78 | -9.70726 | -61.2998 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5f408324-bcf7-3dac-80a2-ee25826ba24d | -8.0536 | -46.33998 | 2025-08-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c07f099-34fc-37ee-8b6b-9712cad07d2f | -7.10341 | -44.22356 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86ba3306-845c-348d-b033-01dae174888f | -9.94067 | -60.47347 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ecd94ae-4fb6-3f04-93cb-38711fb93e10 | -9.47502 | -57.84581 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac9b5877-4e34-39bc-9fba-6106a4f87d58 | -11.56787 | -44.85412 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eee669ae-0374-361a-bde2-bdafda113eb0 | -8.25294 | -45.07028 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3527f24e-04e6-3a20-ac39-009ef387e62e | -7.37767 | -44.64407 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cc9e9558-e8b2-3084-80d8-bf0cdc1a0e5a | -11.15871 | -49.69982 | 2025-08-08 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19c181a2-5a94-3209-890c-955bdfc5e8e0 | -9.07275 | -45.06537 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49e4b223-93b1-3373-a94a-1823a70cd95d | -6.15641 | -55.80553 | 2025-08-08 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3b657aa-9f8d-38c2-9ff2-d8042d288257 | -6.15742 | -55.80939 | 2025-08-08 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eabf42b2-a261-3d24-82bf-e0c968da371e | -13.36427 | -43.76373 | 2025-08-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 538d1627-10c2-3f45-9ec1-07d626e5b6f5 | -7.23051 | -44.65026 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a7444db-36c0-3499-9a7a-39ce265aa76a | -8.52678 | -43.31339 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 488d10e3-81ea-39a5-8416-2f2bfb954a7d | -5.81368 | -59.22577 | 2025-08-08 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 782ec5c5-29b4-30d3-85c2-1c181da4afc7 | -8.52627 | -43.31702 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40b3dfb9-9702-3bf7-8673-ad668d3e335f | -8.86809 | -47.4652 | 2025-08-08 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b990e1-0892-3fd9-9a55-25a92f451d62 | -7.70693 | -45.51222 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a953f591-6788-3810-bc97-55f7260726a0 | -12.58016 | -47.17331 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 40a9c010-f65f-3e64-86af-ac42d17504d5 | -10.64024 | -44.73999 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea2b0769-af10-3a15-996c-2cb84ac0ed4a | -7.58864 | -44.90976 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3839059a-44e4-354d-9334-779f27fbd46b | -9.93629 | -60.49059 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1808b208-7240-36f0-b6d8-19b8425361ea | -10.43453 | -44.34451 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce78c81-2c2b-37c3-b431-db28e961bd0f | -9.71472 | -62.40411 | 2025-08-08 04:34:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78761ab1-087e-36f9-861c-e327e24138e0 | -9.93957 | -60.5063 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fef07726-7bbd-3a86-b40c-aab22cd45a66 | -12.61847 | -48.11216 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d691358-e6ed-30f4-bc4d-9c84a51d2f0e | -8.06723 | -49.71212 | 2025-08-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470cfd06-317f-33d4-bf05-5b30b3dfe6b9 | -9.65643 | -43.84637 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e317af22-460c-3e93-bdc2-4e8fb50d3025 | -12.09814 | -44.73171 | 2025-08-08 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 154b8fbd-6d29-31e3-81c4-5d2697e737be | -12.49283 | -47.50512 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0637dd61-46ca-3a62-93cb-f76136581d53 | -8.10869 | -47.43126 | 2025-08-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 453cfa3b-51fb-31fd-8507-f0971d90ace9 | -6.8179 | -48.64606 | 2025-08-08 04:34:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d697e0d1-a187-3863-bb80-e219e3ca2372 | -7.59816 | -55.19855 | 2025-08-08 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc351b54-fca5-334f-9450-e8d6585eb21f | -8.06608 | -49.7193 | 2025-08-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2db3ed0b-86a6-39e4-815a-b51d92ad909e | -8.15986 | -42.42203 | 2025-08-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53307ee6-a249-34c8-8570-614fc2532039 | -11.74261 | -47.50765 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fecc522-ce4e-3410-8ef9-b459e78989a8 | -10.48111 | -44.38433 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d75ac0-5641-3b24-9812-554f5af2705c | -12.52287 | -47.1378 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b28201a-7715-3026-92a3-2264657bcc33 | -12.4934 | -47.50136 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4374120f-21c6-3818-938a-dc5efb8067f8 | -12.34031 | -46.05765 | 2025-08-08 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d96aa19f-1d12-39d9-828d-0096d0985268 | -7.38303 | -44.2445 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e00b7c1-5fd2-3486-b3b4-0ec1affde9b6 | -7.22749 | -44.64515 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81d6ffb6-e1e4-3030-ab33-832516a81fbd | -8.65253 | -47.47524 | 2025-08-08 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae6005a-b7ff-3026-a220-bdf0a165d06a | -7.88352 | -45.34481 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c89727d-4bf6-3c76-9919-1fc083173e11 | -9.55798 | -47.88478 | 2025-08-08 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5920489c-e3b1-306b-984c-e74830e547da | -9.9351 | -60.50255 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e161db9-af4c-3077-92bb-2b5b94d37979 | -8.22098 | -46.83153 | 2025-08-08 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d255263-7e48-3255-b516-de0b4a9b43db | -12.5246 | -47.12614 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca63aff1-e7de-33cf-930d-fe8cd802aa08 | -7.3844 | -44.64956 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afea6556-47e3-3bab-8c24-4c940dce7d22 | -11.77038 | -47.39321 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1b4736c-bbdd-3f15-b784-477ae18b5e70 | -10.43565 | -44.36473 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4322ac9-f7a3-3a46-b4a6-89b2e0ffda4b | -12.57097 | -47.18776 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 446dbf4d-15df-3b5d-8f6e-3b0f90bfc873 | -10.6331 | -44.76331 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12ebb966-0467-3ecd-b4af-740fcf214502 | -9.07038 | -45.05603 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e52c8f3-606a-3f71-89c7-6aaf2d468fe5 | -9.06842 | -45.06916 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e369ab8e-96b1-3a59-897a-795e3dc7c372 | -12.55867 | -47.13555 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 026afff8-2db8-32e0-9214-505d01a6498e | -12.5217 | -47.12172 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 249e5dae-9e17-3017-a415-06cbe68b491f | -10.63834 | -44.76218 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cd7caeb-357f-33f0-a50a-8405320a724b | -10.36237 | -48.85974 | 2025-08-08 04:34:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53fb884f-3905-3e4c-8f12-0195469fa89a | -7.06171 | -55.41135 | 2025-08-08 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b300b555-830e-376a-b7b0-9f5f08d9f8a2 | -12.5211 | -47.10172 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7643f30-1ad7-3a5d-a8df-b3a477ad07fa | -9.65242 | -43.84588 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4787efe9-ea0a-364f-b4d1-d06d2b19ac20 | -7.15262 | -44.07499 | 2025-08-08 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9587774d-0e33-341c-99d6-17ef881afc08 | -7.91497 | -45.54868 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5a2d943-ca14-3b37-93a5-aab177302fad | -11.46006 | -47.31525 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c55d6b6f-9079-3ee2-b952-1a93ea0245c6 | -7.9282 | -44.8155 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d15e4590-26ed-312b-8b70-f30857da2d12 | -11.00658 | -50.54459 | 2025-08-08 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
