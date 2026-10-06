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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf5cee4d-3728-3b36-8c3c-bc0327946e05 | -3.2 | -50.53 | 2026-10-06 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffbef8f9-87e7-3671-90d8-1d7b9fa98084 | -9.98 | -43.56 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 225ed683-00ba-377f-8416-beb73152b56d | -15.64 | -41.69 | 2026-10-06 18:15:00 | MSG-03 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f58c4310-aa2e-3b75-af3e-5a57d5126ff8 | -9.96 | -43.88 | 2026-10-06 18:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8587b861-1db1-36d6-8f3e-a11ce818f1f2 | -3.11 | -53.75 | 2026-10-06 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3065158-d13b-3ee9-b512-7f448225c6b7 | -10.84 | -50.76 | 2026-10-06 18:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd8cd7af-586b-345f-a567-77ef7cb7ae92 | -15.61 | -41.68 | 2026-10-06 18:15:00 | MSG-03 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d1177b3-cbf1-3adc-819e-d3c9774e2107 | -4.2 | -51.13 | 2026-10-06 18:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac33926-8b5a-3ed4-ab40-5a7f8e18a544 | -3.26 | -50.43 | 2026-10-06 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ae2ee4-7935-37ec-a646-c53b7b05fc4b | -5.75 | -41.75 | 2026-10-06 18:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b25411e-d8ce-3a5c-85ed-dcdcb2e95886 | -5.72 | -41.7 | 2026-10-06 18:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b83849f-db2f-326e-b830-452a1b6ad550 | -3.0077 | -43.1251 | 2026-10-06 18:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7dee5ba2-42b5-36b3-90e1-4db446ec67b1 | -6.0266 | -42.2792 | 2026-10-06 18:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| a6f6e635-52b3-3012-bd07-4922dc8ea378 | -9.0705 | -67.7225 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 3f207b8f-139c-3c0b-bcad-cc23a660eee5 | -11.7143 | -43.652 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 1ae3b9ee-9647-3826-8efd-8af6136e9055 | -7.47 | -42.8078 | 2026-10-06 18:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 385813c4-7d74-3bd3-b719-ee15519a5973 | -9.5151 | -67.7484 | 2026-10-06 18:20:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 119.9 |
| c899032f-406a-3b20-998b-7e06a9900f3b | -6.5985 | -41.5582 | 2026-10-06 18:20:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| b3bf5ba3-fe7f-31d8-be7a-dd19a98629e4 | -9.462 | -67.1002 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 82eb05b7-3e23-317d-838e-fcc6a9c4f6e4 | -11.8296 | -44.688 | 2026-10-06 18:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 68722aa5-d102-3d79-ba54-3da15f5e0a62 | -10.4781 | -68.7255 | 2026-10-06 18:20:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 99514c30-4ae8-373b-9413-c12d503abff4 | -9.8844 | -64.2802 | 2026-10-06 18:20:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| c866fd2a-e5d8-358a-9cf0-8fad93a6f85f | 2.0713 | -50.8799 | 2026-10-06 18:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d18348ae-ec9a-3810-8706-7a513ae45d1f | -9.9444 | -67.1982 | 2026-10-06 18:20:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 92.5 |
| fa3d6b03-d188-31e5-a756-d543ac586aff | -9.3431 | -64.7143 | 2026-10-06 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 1ae634b8-aa41-35e6-a68a-a80624e48d93 | -5.5148 | -42.8164 | 2026-10-06 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 6158db88-40f0-36a9-b7b8-d9740b01c43b | -8.9188 | -68.8711 | 2026-10-06 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 48924357-1cf9-3554-818a-6c82e6141be1 | -6.6027 | -37.8944 | 2026-10-06 18:20:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 21778f43-1f52-3228-b960-f88f6a98d4b1 | -5.7321 | -41.6349 | 2026-10-06 18:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 203.5 |
| bc8997c2-e2f0-356e-831b-c9c65e5793b8 | -16.1241 | -42.2302 | 2026-10-06 18:20:00 | GOES-19 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.2 |
| 1beaf64f-5db7-34b2-96e6-e02d50a2319d | -9.4621 | -67.0817 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 11b0f31d-6e37-390c-b39e-723cc5ea0887 | -9.0705 | -67.741 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 873a5ec1-d65e-300f-bb04-149468c920cb | -11.3753 | -46.6497 | 2026-10-06 18:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 8dc5e87f-dfa2-3278-b1de-79daf5d03336 | -9.9734 | -65.0105 | 2026-10-06 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e01fc653-d6dc-3623-b90a-43240613a75f | -4.7894 | -42.159 | 2026-10-06 18:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| d426eeab-7f84-35c5-b5af-1db4213e1fad | -9.1055 | -68.3135 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 126233cd-cbe5-3aae-acb8-b4b56370effb | 2.4585 | -50.8299 | 2026-10-06 18:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 63124bf3-5ce3-38ef-96b6-8d5d3407154b | -3.0461 | -65.0844 | 2026-10-06 18:20:00 | GOES-19 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 9823f706-3758-3b3f-8269-dae77e9eab87 | -9.0045 | -65.7174 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| db4f6626-9355-3c48-ae7c-749ffb76d113 | -11.6382 | -43.6166 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3767b0b1-84f0-32c0-a17d-816513c0e40a | -9.5468 | -64.8196 | 2026-10-06 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 294.4 |
| 04ba3b23-6e1c-39f0-ab77-cc34c0cf41f3 | -9.1072 | -67.8326 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 934292a4-4e53-30e1-bff6-d5e5357c954b | -8.1949 | -70.4634 | 2026-10-06 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7911cdbe-fc36-38f0-bb34-816ce006c794 | -7.7687 | -72.2223 | 2026-10-06 18:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a24c61c6-4016-3a66-9489-82607c10056f | -9.1068 | -67.9437 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c735b9da-7158-3ba6-8b02-73ca0a93e682 | -11.47 | -43.3824 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d5977b65-fc00-380f-86c5-66f8d04f0457 | -9.1257 | -67.8322 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| c973b86c-4f7c-3630-b6c6-bd2ff36954fe | -9.4806 | -67.0811 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 946a5163-c3b8-3c31-87c8-70a6d7ce556f | -6.6217 | -37.8923 | 2026-10-06 18:20:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 3a364aa0-dbf6-334a-b310-cf93adccc9e4 | -6.8955 | -43.6601 | 2026-10-06 18:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5322db66-766a-3e65-a5c9-99ecc525e9e8 | -9.0892 | -67.6665 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 8098d6d2-5638-39cc-98f9-228f92436854 | -10.1793 | -69.0104 | 2026-10-06 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dba52ca6-44a5-3783-85c5-465a7dc8d058 | -11.8315 | -43.5391 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 07026215-0d53-3501-96e6-2c374aee9462 | -8.9188 | -68.8527 | 2026-10-06 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 80.0 |
| e9f31a14-442f-39f6-be7a-8d16212cf73e | -4.5345 | -43.7219 | 2026-10-06 18:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b9bf5425-f8cc-3c2f-a183-2885de175e42 | -3.3921 | -44.4923 | 2026-10-06 18:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 720c6b1d-68ab-3118-a621-cccc3b0722ea | -5.9838 | -40.9123 | 2026-10-06 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| 19efb6e9-cc30-3842-9ea9-c6c871285b72 | -9.1253 | -67.9432 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9ec6f532-70d2-3439-9d15-d0c8a6a44c11 | -9.2745 | -67.6433 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| a3cbdf65-03f2-337c-a2fe-33b3ca376ee6 | -3.8772 | -44.3557 | 2026-10-06 18:20:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 86033bd2-84d5-3c7e-9f14-459a62ec3fd3 | -3.292 | -42.2673 | 2026-10-06 18:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 1a1f7b37-2847-3a7d-90dd-bd27cfd98a83 | -10.7361 | -69.5905 | 2026-10-06 18:20:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 45c4ad6f-5583-3f7e-b003-f664ccca65ac | -4.0923 | -48.9614 | 2026-10-06 18:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 576fe5e8-a71e-3b11-b014-0d35f357abf8 | -8.7707 | -68.9478 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9f830d69-8160-30d8-8865-a5759023fc03 | -5.1017 | -42.9167 | 2026-10-06 18:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 62e0046a-1642-369b-a058-d7f212492d5e | -11.2267 | -45.2604 | 2026-10-06 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 6e927cd9-2645-3f6d-816a-03cce405911c | -9.8824 | -44.8171 | 2026-10-06 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 340.9 |
| 07306083-d354-3ead-89ed-b401df5cce61 | -8.6201 | -70.017 | 2026-10-06 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 6073c87d-cbf7-368c-8967-a1429ec7e181 | -9.8638 | -44.7964 | 2026-10-06 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3be536d2-470e-3156-b1d5-47c578e56713 | 3.5263 | -51.2778 | 2026-10-06 18:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0b44024e-cc6b-397e-b64e-567d208c384e | -9.5469 | -64.8008 | 2026-10-06 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 126d5313-5db0-3aae-a646-e0946faf2dcb | -7.6949 | -72.4235 | 2026-10-06 18:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ec2fbd98-740a-353f-ba78-a0b33cb3abae | -5.8509 | -45.0318 | 2026-10-06 18:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 80c1f571-994e-3781-9f2a-74045495e62e | -9.1829 | -67.3861 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 0910f0b5-e5cd-3438-bb4f-453f336a65b1 | -5.7376 | -45.1533 | 2026-10-06 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 884.0 |
| 8c623dfa-a56a-31f3-a5de-d45a819f36fc | -9.2365 | -67.9035 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 1d2c17f0-f2e9-38f0-9b30-ca96439e0f89 | -5.7563 | -45.152 | 2026-10-06 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 184b3ff1-1a7e-349a-ab0e-d57e3d239791 | -8.9607 | -67.3733 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b1acd70c-1344-375a-8e44-7fe5f3809357 | -7.4001 | -45.6072 | 2026-10-06 18:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 32ff786d-f923-3e89-9e2a-f1c0e6672fc8 | -8.7324 | -69.4271 | 2026-10-06 18:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 76.3 |
| af87fcbf-5ba7-38c0-a47c-9603477451f9 | -9.1256 | -67.8507 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 87784c44-b0b6-3445-87fc-c9854e6f28b2 | -7.5332 | -70.0148 | 2026-10-06 18:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 9b6427c4-64a8-3d45-9c54-4c656a8f9626 | -9.96 | -43.481 | 2026-10-06 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5e64686a-5a18-3843-bb61-d912c70eb081 | -11.6378 | -43.6403 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c488cae8-9801-397c-968b-0f549791dcca | -9.4435 | -67.1008 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 21f73fd9-8d59-398d-8b1d-b9e0e7a49bcd | -11.4507 | -43.3854 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 4ad4900e-f156-310e-9c70-4b6859e19c5f | -7.8606 | -72.3311 | 2026-10-06 18:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 505d69ca-cf3c-360d-845b-eb50a15e33ff | -9.2366 | -67.885 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 619ff3db-b76c-3c97-822b-833000718f58 | -3.3607 | -43.3893 | 2026-10-06 18:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 394.4 |
| 3e5a19a6-5e76-3db7-a8b1-1be0eceecce8 | -11.8216 | -47.3521 | 2026-10-06 18:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 4af8e4e8-8299-32b9-bb6f-555ccc120fd9 | -5.4174 | -39.1062 | 2026-10-06 18:20:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 142.6 |
| d33d7995-986e-3ce7-9b79-ac40a55d7fde | -11.6374 | -43.664 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 3bedf5ab-5809-3d32-abba-6f833a5a662a | -10.938 | -45.4146 | 2026-10-06 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ee3879c8-a79e-3a7a-9b58-26dc75980319 | -11.21 | -46.2655 | 2026-10-06 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 47a8cc69-2d10-39c2-b9fa-eb990d58b889 | -4.1416 | -46.8331 | 2026-10-06 18:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 55f5b915-93ff-353c-bf6f-aa200bfdecd8 | 3.5079 | -51.2784 | 2026-10-06 18:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3fc3aa89-51d8-3514-9e35-ed9de7d5b5f5 | 1.7304 | -55.6259 | 2026-10-06 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 38772b91-d9db-353f-941a-85a7c5bd583f | -10.9758 | -45.4324 | 2026-10-06 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 09ffb885-8559-3c2f-a2ea-d05a4219fb94 | -3.342 | -43.3901 | 2026-10-06 18:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2d4cc386-7161-3b47-be5c-c29f4db14d28 | -4.8081 | -42.1577 | 2026-10-06 18:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 151.5 |


[Clique aqui para ver as próximas entradas](README99.md)
