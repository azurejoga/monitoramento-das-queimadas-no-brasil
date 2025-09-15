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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2a81bb2-d89d-3bac-9ba2-2738d85f42ff | -10.2251 | -48.6267 | 2025-09-15 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 6b3f9e20-9f03-3a4e-b800-dfa179aeae0a | -6.337 | -43.1727 | 2025-09-15 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 70fb7526-f236-3d62-866a-e4ae731e8ded | -12.9984 | -47.9685 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e0b7a1f5-95bc-3b54-b72c-b09d6cdcadc8 | -10.935 | -45.5978 | 2025-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| a74a15b5-d10a-3463-a75a-95480e28f757 | -10.9667 | -47.1952 | 2025-09-15 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| aba0b82a-ab78-3d05-a111-0afb4ccf7643 | -5.9459 | -44.8657 | 2025-09-15 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 6cccd71b-01b5-31ae-8ace-043daa7d35e0 | -5.8399 | -44.1642 | 2025-09-15 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 95cb3c0a-ef05-3f3b-aa45-3cbb06de0aee | -11.6434 | -46.591 | 2025-09-15 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| cc0ae7cc-0ae2-38ef-9f19-fdbf92123c98 | -11.1306 | -45.2966 | 2025-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fdf699ae-cd95-3a50-aa1e-55f375ac3dad | -8.917 | -46.2015 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 9663fbff-df79-36bd-aa6b-00e16e861862 | -17.0001 | -45.8799 | 2025-09-15 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 142.1 |
| aa43c24f-6616-3e0c-aadd-e1b8a99a349f | -15.9039 | -49.9775 | 2025-09-15 14:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8f2392c5-90bb-377b-999a-b96eea0a5a53 | -12.6764 | -47.725 | 2025-09-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e1195c9d-70e7-3150-8807-519377827786 | -8.4329 | -45.7337 | 2025-09-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5ee21444-0676-3cb7-8a29-8b04455e2478 | -8.651 | -46.3637 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| e9eff409-f5a8-30f0-bcad-a1057a4d5241 | -11.3338 | -43.4979 | 2025-09-15 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b89afb31-2c4e-3981-9d25-29e051e66264 | -5.7673 | -43.9161 | 2025-09-15 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a1fad414-6d36-3085-b457-df4b7f6d5784 | -13.9463 | -44.901 | 2025-09-15 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 422d433d-d27d-379b-a2d6-4a7d3e3bb3f9 | -9.5164 | -47.9589 | 2025-09-15 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0bbb4b3f-e320-394b-ad60-a2bfa624c1ad | -13.1842 | -47.2704 | 2025-09-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 249d4f18-48d1-3a84-bac1-fed9f8c9054a | -14.5631 | -53.1979 | 2025-09-15 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 9b8ed220-6556-3cdd-afe0-c23d76e06191 | -8.9604 | -45.7686 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 855345c5-9ce1-3eec-84d9-0517450d5578 | -9.0867 | -44.8203 | 2025-09-15 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 49f93279-d9e4-379a-b44d-87d6d2a70afc | -6.3989 | -42.6263 | 2025-09-15 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| a3e30493-b179-3b27-ba9a-f054f4feef88 | -7.7285 | -44.8267 | 2025-09-15 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 44273c46-d74e-3898-a7d9-8be2f4fe1b5f | -8.5944 | -46.3695 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 344.1 |
| c1504eaa-82c4-329c-87bf-4e1007a68b6f | -7.7025 | -48.8667 | 2025-09-15 14:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f7de68e5-abef-3e21-bcce-f3a3d3effbf2 | -6.3372 | -43.1492 | 2025-09-15 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f19b8e76-1c2a-3c23-93b8-137566e5a026 | -5.8399 | -44.1642 | 2025-09-15 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 69daff26-b2c9-37cf-a143-8c03ce087d75 | -5.9459 | -44.8657 | 2025-09-15 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2432777a-0de5-3680-815c-a3436158e7b2 | -11.4569 | -48.7026 | 2025-09-15 14:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 167f6895-2abe-3410-ae4d-d10c4ec471b4 | -5.2379 | -42.3174 | 2025-09-15 14:40:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| bf358765-0369-3b84-82a6-7dbbdade3c42 | -7.6838 | -48.8682 | 2025-09-15 14:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a0efd9af-6347-3639-a91a-c10cd473bdf3 | -11.6959 | -46.8765 | 2025-09-15 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3756b3e3-185e-3e4f-b92f-88e7e2218487 | -8.9412 | -45.7933 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 1837438b-a4a7-3454-ad59-681146a5954e | -11.6626 | -46.5884 | 2025-09-15 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 9997ccd7-f756-30ab-96d5-c5af77e61bbf | -12.1668 | -44.0988 | 2025-09-15 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 88c43977-c661-3e88-b691-32485f4ac136 | -8.9784 | -45.8344 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 0cf94ee3-2028-3936-9acc-36493285715f | -8.9176 | -46.1565 | 2025-09-15 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 970da1b5-fe07-3348-b99c-56e50f93376d | -8.9601 | -45.7912 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 461bd962-93a4-3c66-90a4-4a67cf7cf3b6 | -12.0051 | -46.6763 | 2025-09-15 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5f4d59ae-119e-3d21-92bd-6a8fa0065522 | -12.7818 | -47.1952 | 2025-09-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| bfc7af5a-fa2c-30f9-b1d1-4cac1241d3eb | -10.8612 | -45.4477 | 2025-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.8 |
| dbad48b1-121d-32fa-af20-5c8647609307 | -8.9076 | -45.4797 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 90032500-8c56-3923-bca4-1cc455ff78ac | -8.6507 | -46.3862 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 708f7fda-7fa8-3737-b80a-4f8d3516994b | -5.9271 | -44.8671 | 2025-09-15 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 32a77e55-58ed-38da-ad79-9d4db692e4e3 | -8.5947 | -46.3471 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 70e4c8f1-69b6-3d02-a1d6-c499523ae800 | -11.1306 | -45.2966 | 2025-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9e88e564-4c6b-36a6-bcf4-ccf579485bed | -8.8987 | -46.1585 | 2025-09-15 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| d9075a14-c396-3a9e-8c22-9bb7b06ace66 | -9.0162 | -45.8303 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 593738eb-1c0e-34a2-a6e7-1b64b884cca2 | -9.5167 | -47.9369 | 2025-09-15 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| edc86d75-e6c7-3dfb-bea2-ba340ab99a37 | -8.6513 | -46.3413 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d536ba71-ffa4-3e89-95d5-91dd5d1582b3 | -8.6133 | -46.3676 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| b3e448ad-1f14-3244-985b-af45099908c3 | -7.4349 | -45.8519 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 1b603da5-3db7-3de0-9c43-2bdaca103bd1 | -6.1693 | -41.1872 | 2025-09-15 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 277.0 |
| d8cbb867-7c79-30a9-ab5e-df4720d16212 | -12.6345 | -47.9312 | 2025-09-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 2060383e-fdc2-3295-85b7-067c05be8e1b | -10.8803 | -45.4452 | 2025-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 3751386c-fe0d-39c6-a01c-8df0bad2daae | -7.6317 | -46.7284 | 2025-09-15 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 68ef4f7a-efc6-372e-988b-110e00282e16 | -6.9986 | -44.5512 | 2025-09-15 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 59d9aae0-d409-33e5-b7d4-8161a21404a6 | -10.88 | -45.4681 | 2025-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 63fffc74-d0e0-300f-b714-06a4506bf2a1 | -10.9346 | -45.6207 | 2025-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.8 |
| c12bc04c-0652-3b33-841e-3e2090614a2f | -5.8397 | -44.1872 | 2025-09-15 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d1f24dc0-599a-3e8e-8f71-06a41cadc35f | -11.4469 | -46.9322 | 2025-09-15 14:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b768558f-f0f6-3000-a891-e5fd4f0ceb3b | -6.4177 | -42.6246 | 2025-09-15 14:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| da4ae63b-bb2d-3feb-af7d-4faab1804cf3 | -7.9634 | -45.6449 | 2025-09-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 714bd348-c57a-3584-98da-861c19c0b6aa | -13.9288 | -44.8106 | 2025-09-15 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| c61ef879-447f-32e7-8c42-df11a48d5970 | -6.003 | -46.8567 | 2025-09-15 14:40:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ce7d816f-2978-3b06-81ce-9a22ec923478 | -6.6696 | -45.5344 | 2025-09-15 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| bee0be4b-2a48-304c-ac85-1b23e39b8bfa | -8.9265 | -45.4776 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 935da3c1-8d3d-35a2-ad15-4bf1afe7efaa | -8.7868 | -46.0578 | 2025-09-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| af0879e1-c809-37c3-91ca-45a5139aa0a2 | -8.9262 | -45.5004 | 2025-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 1773f8bc-c0bf-329e-8d1b-9e37ffa29f46 | -12.8204 | -47.1896 | 2025-09-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| eba04341-a899-311a-8d8e-1b138241e251 | -10.2251 | -48.6267 | 2025-09-15 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 0b2a8d96-4355-331c-94ae-01f79c472148 | -5.9457 | -44.8885 | 2025-09-15 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dee5aef6-cbdb-31e3-ae22-3ab6ab5bce51 | -8.6136 | -46.3452 | 2025-09-15 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| fe5dd233-469a-340c-8ecc-28ebf1e8d004 | -3.7333 | -40.4406 | 2025-09-15 14:40:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 200697e7-afff-3a8f-9030-ba2766e9464d | -11.6434 | -46.591 | 2025-09-15 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| c2095a20-5a28-3474-80f4-73113bb819db | -6.337 | -43.1727 | 2025-09-15 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 54519df4-9d5d-3c01-be39-d8bfec78d1b8 | -14.8218 | -51.6362 | 2025-09-15 14:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3232beec-16bb-37a9-8ce8-95fb15bfede2 | -12.8404 | -47.1417 | 2025-09-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ab10f869-d3ec-39dd-86cc-6b4bab6b4bf3 | -8.7677 | -46.0823 | 2025-09-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 29983732-dc17-3a35-b646-20da07ee5403 | -7.676 | -44.4879 | 2025-09-15 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9b4ffb04-05bb-310e-a1e4-811d2c6b3390 | -12.1147 | -44.8304 | 2025-09-15 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9cd471ae-50a4-39a6-a74c-1fb449b514cd | -6.6693 | -45.5569 | 2025-09-15 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 300.3 |


