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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b6b3156-9a78-3333-a538-d3d20fe37435 | -12.4228 | -62.9807 | 2024-10-03 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| a6559c8c-e666-3117-bfba-24191c2e3a50 | -12.4227 | -62.9999 | 2024-10-03 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 5fa64d2d-552b-3314-a429-0db18fe0f661 | -12.404 | -62.9817 | 2024-10-03 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 3e117eee-3029-3447-97ef-5071047bd11a | -12.4038 | -63.0009 | 2024-10-03 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 213.7 |
| fdd5b29a-93cd-3ddb-829c-fc4926f17d1b | -12.6484 | -63.1214 | 2024-10-03 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d3c652a1-7e2e-3504-9620-6e6547e0b288 | -12.8999 | -62.4527 | 2024-10-03 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8d399298-d241-3f0a-b3fa-12bce082d1a7 | -12.8998 | -62.472 | 2024-10-03 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 62181e77-4ba0-36a7-ab71-4bc9dae3063a | -12.8996 | -62.4913 | 2024-10-03 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 4884b63e-6d80-36f3-bf59-d4c36003ebe9 | -12.881 | -62.4538 | 2024-10-03 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b9c585bc-50a4-32af-a2f3-e865d809f121 | -12.8808 | -62.4731 | 2024-10-03 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b20dc31e-e534-3135-9356-4400233b3054 | -12.9741 | -62.6409 | 2024-10-03 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 87cd14ee-4f0f-34bf-97c5-2f65c35c162b | -7.6352 | -67.207298 | 2024-10-03 02:46:21 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6dd070a-1d7e-39eb-acae-6f1204fa6d6f | -7.3703 | -68.013397 | 2024-10-03 02:46:28 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cffe273b-0a40-37ae-b13e-bd7a8d24e9c5 | -7.9276 | -71.469902 | 2024-10-03 02:46:33 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc34793-39bd-3da6-8535-a96c4c423597 | -16.4533 | -57.4392 | 2024-10-03 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| b8e8e1fc-a274-318a-89a8-7096ab8d4efc | -16.7802 | -57.749 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| a8351439-8d80-3f15-983d-197a825824bc | -16.7793 | -57.8102 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| ce5427b1-c3c9-3391-bad8-d1b2ff63d491 | -16.779 | -57.8306 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 5b0e9cf7-9459-3b89-a50e-2eb04c30c0e2 | -16.7606 | -57.7512 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 996424fb-83ab-3bcc-bd17-f1938ba6b4d3 | -16.7597 | -57.8124 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 7476ab0e-1cf8-3c93-862e-2a18db69b13b | -16.7594 | -57.8328 | 2024-10-03 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 1c00d3eb-7c3a-3273-944f-ab9a24532b13 | -16.9179 | -57.6926 | 2024-10-03 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 5d3ef881-d777-333b-a954-48ef5d2b7a42 | -16.9176 | -57.7131 | 2024-10-03 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 0de9c976-8150-3157-9ecb-d508f3e8288d | -16.8983 | -57.6949 | 2024-10-03 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| bc700283-fcb4-3dd0-b23c-eadb5ab985f8 | -16.7985 | -57.8284 | 2024-10-03 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 7f640f09-3402-38f6-af65-0c294640cd4b | -7.4289 | -72.724998 | 2024-10-03 02:46:46 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43e3ac19-8aa3-31a5-942c-08278c1ad362 | -19.0344 | -43.1944 | 2024-10-03 02:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| de89faac-72ac-3df0-aa95-4a92f449ee95 | -19.3159 | -42.5976 | 2024-10-03 02:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| c3ca6ad3-9289-3f10-9fff-82cb287bc2ca | -19.9009 | -42.1074 | 2024-10-03 02:46:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| d18c4724-4a96-387f-9661-6c6287828baa | -21.2854 | -47.6277 | 2024-10-03 02:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3852d246-f909-32db-904f-6341a07fc74c | -21.2861 | -47.604 | 2024-10-03 02:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| adf1119f-79e6-3f0d-baa4-b8a3c67abb76 | -21.306 | -47.6227 | 2024-10-03 02:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7335f44e-f952-3486-9859-eb384680cd8d | -21.3067 | -47.599 | 2024-10-03 02:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a70406c3-b602-3149-9cd0-179538941c66 | -21.3675 | -47.6311 | 2024-10-03 02:47:03 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 76277f40-c514-3ed4-ac5b-186798c810cb | -21.3875 | -47.6497 | 2024-10-03 02:47:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 587b99aa-2bbf-3bdf-a1be-eb846f56b63e | -21.3882 | -47.6261 | 2024-10-03 02:47:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 87339b9c-97ed-3b61-b510-3eaf95c54bbe | -3.404 | -42.2858 | 2024-10-03 02:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 192fc565-2bcd-3ab2-8df9-b8f1415097ba | -4.1134 | -48.4886 | 2024-10-03 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f4f408ba-7cf3-38bd-a798-8506f0e057a5 | -4.095 | -48.4679 | 2024-10-03 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ca73ce0b-4b79-318f-9de0-9b210e3fcc38 | -4.0949 | -48.4894 | 2024-10-03 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2ead2544-08ee-3d66-9aca-b91d2a916593 | -4.5031 | -42.8854 | 2024-10-03 02:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 60058390-211b-390c-b530-e3cf10c5f336 | -4.4845 | -42.8631 | 2024-10-03 02:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 58e72954-a457-385e-a7fc-eea0a042d6d1 | -4.4844 | -42.8866 | 2024-10-03 02:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 763e699c-b7db-3ff6-a64a-cab58b45bff6 | -4.4657 | -42.8877 | 2024-10-03 02:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 619a2471-ccdc-30a0-a6b8-f967e7461d74 | -4.5373 | -43.3273 | 2024-10-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 055938ca-c1a8-3984-bac8-10abd0e6f3b4 | -4.5375 | -43.304 | 2024-10-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 06fb782d-4e0d-3962-9025-96dcb578914e | -4.58 | -48.0132 | 2024-10-03 02:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 78044b6b-b1ec-32f4-aa28-e1424f113852 | -4.9451 | -43.7888 | 2024-10-03 02:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5645990e-d553-38ca-9ff1-65cddc4f0309 | -4.9265 | -43.7669 | 2024-10-03 02:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 9efb421e-b38a-38a0-9fab-be32f115d14e | -4.9264 | -43.79 | 2024-10-03 02:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 49bb9258-e36e-31f6-b121-846edba35d20 | -6.8777 | -59.0504 | 2024-10-03 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| f1573c8c-3c33-328a-8666-793eb405af0f | -8.4259 | -46.2968 | 2024-10-03 02:55:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 54bddaf3-cb20-3b77-b403-e565f078726a | -8.8695 | -45.5066 | 2024-10-03 02:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 8e6b0f75-9b70-33f8-986e-8e33187df8a5 | -8.8506 | -45.5086 | 2024-10-03 02:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 775965f0-fa90-33b4-8615-1a6a6824af37 | -8.8926 | -62.3348 | 2024-10-03 02:55:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 554239ff-4d00-30e8-badd-f96aab85f746 | -9.1566 | -61.6758 | 2024-10-03 02:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 297af882-884c-3139-920f-30fa4fd584f6 | -9.0515 | -67.871 | 2024-10-03 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| bc35e058-1519-36d4-a2ff-9f824f211db9 | -9.0149 | -67.7423 | 2024-10-03 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d7ffd4d6-35e4-3624-ab33-043b65ff8370 | -8.9976 | -67.4094 | 2024-10-03 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a0e2dd82-c275-3b0f-9782-ea64ef354e22 | -8.9791 | -67.4099 | 2024-10-03 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 510643f5-f0c9-33de-9ee3-188ba4d69afc | -9.4866 | -62.3849 | 2024-10-03 02:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 11df5842-3667-3b68-b654-ed698c06bf10 | -10.7161 | -46.1942 | 2024-10-03 02:56:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| bbdd58a6-b9ea-3204-9ce1-34f05e6f62b1 | -10.7352 | -46.1918 | 2024-10-03 02:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 01c668d3-b9bc-3acc-a25e-118726556e8a | -10.8942 | -63.8971 | 2024-10-03 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| aff971e0-61db-3c04-8f22-c7aff1752466 | -11.2565 | -60.6019 | 2024-10-03 02:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 47db3bdd-6ac6-3ad0-a063-f33615b05823 | -11.6932 | -64.9785 | 2024-10-03 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 577b0c18-b103-30d1-be10-8022b7205246 | -11.6931 | -64.9974 | 2024-10-03 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 104.4 |
| b35466fc-50e6-3063-af63-6cbd26383ab2 | -11.693 | -65.0163 | 2024-10-03 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1822dc48-abe0-3f9c-8044-c4d640685241 | -11.6743 | -64.9983 | 2024-10-03 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c721713b-d477-367d-b9e9-b7f346e2490a | -12.4228 | -62.9807 | 2024-10-03 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a9953489-27b3-3442-84d3-c4ee2229a2b9 | -12.4227 | -62.9999 | 2024-10-03 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 729df6c5-1c6b-3c60-bdcb-884753ec9947 | -12.404 | -62.9817 | 2024-10-03 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 141.5 |
| d9cb3809-87cd-360d-8222-e2c5d4d0fa3e | -12.4038 | -63.0009 | 2024-10-03 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 806616dd-eb81-345c-9081-5eead53fc097 | -12.3849 | -63.002 | 2024-10-03 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 94b399b0-58ec-31a1-b4f8-5871e7f80081 | -12.6484 | -63.1214 | 2024-10-03 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8f6581bf-21b3-3d60-aea4-ebe33475a9a5 | -13.0402 | -51.1432 | 2024-10-03 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 288df54a-f281-3d35-a0d5-fdcd305c5d7e | -12.8999 | -62.4527 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 184982b0-0c53-3f9c-8837-6d0a9b9d056b | -12.8998 | -62.472 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 9bf02806-7c7c-3ca4-b0c3-79b472a77101 | -12.8996 | -62.4913 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 9f2ae64b-a06a-3c3e-99a8-136ca37a042d | -12.8994 | -62.5106 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 56a3a624-af77-32b6-bb0e-d028f7f54894 | -12.8991 | -62.5491 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 6cdb5ea5-bdc5-39b9-833e-f974027c7cb3 | -12.881 | -62.4538 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 5b4dd3cf-b0d2-3a02-90f7-90eeb48693a7 | -12.8802 | -62.5503 | 2024-10-03 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 6de050c0-f2ec-31ce-8d80-360282b3b688 | -12.9741 | -62.6409 | 2024-10-03 02:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1a393c2b-038e-3db5-8ef4-2824e2ad1282 | -13.0975 | -51.1575 | 2024-10-03 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| eb8ccd3e-9703-3b2c-8944-8ae90457db37 | -13.0594 | -51.1409 | 2024-10-03 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1c8da531-2b71-3f00-a9b4-3314e213924f | -15.7417 | -48.3842 | 2024-10-03 02:56:34 | GOES-16 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a8527f32-9096-33bf-9da2-d458c2a39110 | -15.7221 | -48.3876 | 2024-10-03 02:56:34 | GOES-16 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4373bb00-d23f-3426-b902-dee46583e28a | -16.7805 | -57.7286 | 2024-10-03 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 59d43087-13f0-3881-a941-361b47f7f473 | -16.7802 | -57.749 | 2024-10-03 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 17470fd2-27a2-36e6-aeee-e7aadd2e38ee | -16.779 | -57.8306 | 2024-10-03 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 73eaa4bc-b007-3061-86a7-1fe23b0a3c12 | -16.761 | -57.7308 | 2024-10-03 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| f3fb2842-6e1e-37b1-aa36-b6d80056fe18 | -16.7606 | -57.7512 | 2024-10-03 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 0d66ba3e-a10c-3020-b959-c3c07ff4496b | -16.9179 | -57.6926 | 2024-10-03 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 4fc57e07-ae6a-3d88-9547-ccea31c6a307 | -16.9176 | -57.7131 | 2024-10-03 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 35856c41-fee6-3420-89da-9263afd931d5 | -16.8983 | -57.6949 | 2024-10-03 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f2b30114-fe14-3971-b029-cc3d84dfa7fe | -19.0344 | -43.1944 | 2024-10-03 02:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| e5f726fb-e948-34e9-b263-97a9763af85e | -19.3159 | -42.5976 | 2024-10-03 02:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| f999d6f9-896e-3950-98c7-467470b72ea6 | -21.3067 | -47.599 | 2024-10-03 02:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8edd6eb1-0517-3373-8fa8-7558dcf5d5a3 | -21.306 | -47.6227 | 2024-10-03 02:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 87.4 |


[Clique aqui para ver as próximas entradas](README57.md)
