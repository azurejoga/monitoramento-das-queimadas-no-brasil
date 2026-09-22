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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfd16073-56f6-32cf-82e0-c7279602c68f | -7.1273 | -48.4366 | 2026-09-22 13:30:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| aeb62c7a-744b-3abc-9936-8b013fa4398f | -8.5982 | -54.6341 | 2026-09-22 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 81cc5f07-14fb-35fc-b850-174ddaa747de | -13.4335 | -46.326 | 2026-09-22 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| fc6a6f99-b689-3263-ae91-582a203afccb | -3.6946 | -60.5835 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a2032aff-ab55-360e-9fcb-6d7a6181ddde | -3.4781 | -59.5588 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 03a6432c-6a7e-34c9-beb6-1f3000cd12bc | -13.9311 | -48.564 | 2026-09-22 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9cf9ed8a-5c42-339e-a887-4e132fab2d2e | -7.1203 | -43.7323 | 2026-09-22 13:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| a09139e4-86db-37c7-b3c7-8847e1b33b17 | -3.6947 | -60.5645 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 19ec528d-8c56-3005-9c27-79d617ea169e | -12.1027 | -50.0355 | 2026-09-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 0a79cbb0-ad0b-3f70-8dec-767b9388f891 | -8.6169 | -54.6328 | 2026-09-22 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ada7ec23-aa68-36dd-b9b9-10c640021c30 | -9.2759 | -46.1852 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 653dd1d3-2ec6-34fa-b31e-53003be399eb | -11.175 | -51.1031 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ea627fb7-99c4-3c89-b613-8a7e0f15831c | -3.7856 | -60.7525 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 98705b84-2675-3f19-ab49-d6952911fc94 | -12.6796 | -50.974 | 2026-09-22 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| fa14c531-4c92-3420-8e44-eb037d60706e | -12.0836 | -50.0378 | 2026-09-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 259.7 |
| db4f7f6e-da7c-3ccc-940b-e11260b25e47 | -8.6135 | -62.5171 | 2026-09-22 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3a59551c-1aa6-33ce-950e-13bf18a05922 | -6.7354 | -55.3074 | 2026-09-22 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 14849230-c960-3910-9918-4d197c7ccdc2 | -12.283 | -50.7011 | 2026-09-22 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 706a84c4-a31c-348c-bdaf-ee538647a99b | -7.4474 | -44.7392 | 2026-09-22 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e67560d4-ed25-39f7-8091-80fdf3910029 | -3.6398 | -60.5846 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 173bca41-283b-3fad-834f-06aa9980be41 | -12.9481 | -50.9195 | 2026-09-22 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9ae1bded-cf98-3a4c-bd50-566c940b1923 | -12.9273 | -51.0291 | 2026-09-22 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e9c1a634-28f1-347a-bc7e-d1da40fc43d7 | -10.7262 | -50.7044 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 77fa9814-43a1-33b4-863c-dad296472802 | -3.7856 | -60.7335 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8d7cd79d-a182-3ea7-ba70-e78653307153 | -11.4113 | -46.7798 | 2026-09-22 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 268.7 |
| 7f594d62-4756-3bd5-871b-7aaa99ee7b1c | -3.4057 | -59.273 | 2026-09-22 13:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 99caabfa-47bc-38a1-8eaa-721054d3fc4e | -6.4486 | -59.9717 | 2026-09-22 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b9951fa3-c97a-3a86-b81b-53585abe1450 | -6.384 | -55.285 | 2026-09-22 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 7a7138f4-25db-32e2-93b7-55f628790cc0 | -8.5984 | -54.6139 | 2026-09-22 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3b5b2705-a4fa-3fd2-8f4e-c8c6f14650eb | -13.8957 | -45.4681 | 2026-09-22 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 44a432bf-1685-3a0a-a874-769f7541c5c6 | -9.6298 | -43.9453 | 2026-09-22 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 665b5e1b-1c13-3671-8da8-8f5492abb41c | -10.7437 | -50.8089 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7145b6e3-676c-3758-80a6-899951ca29a5 | -11.3603 | -51.4009 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| d400917e-ffcc-3b3f-b6d9-47f65a67d943 | -8.6171 | -54.6126 | 2026-09-22 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f2a9fa8d-2110-33a7-815a-88bc0c742550 | -13.2983 | -51.7713 | 2026-09-22 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 639b8fdb-1b02-37b7-a41e-9ba93e2c7ea2 | -10.4541 | -51.2827 | 2026-09-22 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 955fd0b7-532e-3dfe-b35c-4dab027cbc22 | -3.3867 | -59.5223 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 501a0480-5c4d-384a-b08a-81fb49e85528 | -12.2827 | -50.7226 | 2026-09-22 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| cc490a29-d1a8-3732-8935-c420b7468095 | -12.2726 | -50.1441 | 2026-09-22 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 095ba149-37b5-3db5-b19a-ee7bd5eafb4e | -11.7079 | -50.9811 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 56d2cc15-ab13-39e2-a059-944c4602c832 | -3.6763 | -60.5839 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 65685069-9837-3297-ad6a-96fa402b2ce7 | -6.2396 | -41.6634 | 2026-09-22 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 710109d8-8869-351d-b7f7-40dec48ac32b | -13.8952 | -45.4913 | 2026-09-22 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 1982ea59-30e3-352c-98f4-1c882d9165af | -8.8105 | -44.2757 | 2026-09-22 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| eaf9bc21-56cb-3733-affb-046c3af528a5 | -9.8404 | -46.3911 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 18d7014d-a9ef-324d-b574-35a77981367a | -6.9411 | -42.9306 | 2026-09-22 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 59e308d0-b4a0-3c92-8d35-73b3e8a44a1c | -5.5717 | -42.7414 | 2026-09-22 13:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 8e413b23-d7d8-32bb-bc66-af0dd062a031 | -10.5558 | -46.732 | 2026-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 784d01aa-b751-3a6c-bdf4-cefbfbf570c7 | -7.4765 | -45.4872 | 2026-09-22 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 40069f37-0ea4-390b-b65b-a5ce340c2de6 | -11.4209 | -47.3603 | 2026-09-22 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bb5b1202-0dda-3791-b68c-5643cec4b1df | -11.4404 | -47.3355 | 2026-09-22 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c127f0d2-c9cc-3871-9b65-c0631c28089d | -11.0052 | -53.996 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 65ede1e8-29d5-3cd1-ac15-4fc3ff5d6f93 | -9.2762 | -46.1627 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 611cec41-e45f-3abb-b0fa-a444478c2fcc | -10.9112 | -53.9635 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5e3aedcf-7f02-3e8a-bdce-b96eebeeaacf | -6.0172 | -45.2462 | 2026-09-22 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 551cf68b-8998-3d28-abd6-f6de7f439543 | -7.0352 | -44.6396 | 2026-09-22 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| f252df71-5a25-34ee-86fb-86a45bd8690c | -12.0839 | -50.0162 | 2026-09-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 001be8b0-161f-324c-841c-1f40cc07c2ec | -9.0276 | -44.9875 | 2026-09-22 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 260.5 |
| a01d9cf9-b590-3b89-ae06-63d9dd84f2ad | -8.7912 | -44.301 | 2026-09-22 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 778298e6-c9a1-3a73-8fd8-deb472862d90 | -10.8858 | -56.196 | 2026-09-22 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a9d7e9ee-9cfb-3434-bdfe-b40063c72cdd | -13.2979 | -51.7926 | 2026-09-22 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 96f9bffa-1774-36dc-a817-36ac05262ca4 | -13.2791 | -51.7737 | 2026-09-22 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ad459a04-3697-3637-b271-94e5190ada1d | -3.7673 | -60.7339 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 68147c6a-5f54-3460-852a-5a16d8b900fc | -10.6878 | -50.751 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| e092d280-407f-32b6-8aae-53bcac809a85 | -10.6094 | -53.9902 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 12a2ee1e-b86e-3b0e-bad5-0d8e9e32d7b9 | -7.547 | -42.6817 | 2026-09-22 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 7a8d65f4-3a53-36cb-bd70-48fc4d415d13 | -6.7989 | -43.9008 | 2026-09-22 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 77625cdf-193c-379e-b2f3-a57ba76ef2ac | -14.6878 | -45.6762 | 2026-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 49695f75-7a05-3055-be91-8c81670f7421 | -11.4213 | -47.338 | 2026-09-22 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4289de2c-0a05-348f-802e-21f90a8dc523 | -10.2635 | -49.984 | 2026-09-22 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| db2b1aa0-8256-36ef-b669-c2b6d80814f0 | -9.0286 | -44.9187 | 2026-09-22 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 63090edf-09be-30d9-acc1-c6aedcfbfeb0 | -10.7262 | -50.7044 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eb28ed23-5712-376a-b843-a721d7f9ad71 | -12.3293 | -50.1802 | 2026-09-22 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 730fbeed-5c3a-39dc-b04a-97feaa8ea705 | -7.2996 | -59.5151 | 2026-09-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a3534aa2-cf09-32e4-9024-959891c683aa | -11.3229 | -51.3626 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ba4b8989-08ed-3eb9-82d3-cd90be5eb3b0 | -7.5889 | -57.6757 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9d56552b-3988-3354-92ef-60be9d1df458 | -11.7675 | -50.804 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 265c7cc9-c8f6-339f-8310-eae2ae36b989 | -7.5945 | -43.4296 | 2026-09-22 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 22c4cf4c-6a4c-3fa3-beb4-1c94858fd011 | -12.8 | -44.2073 | 2026-09-22 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| cea0ae48-a92a-3167-9d9c-6d7cf15eb390 | -13.8762 | -45.4714 | 2026-09-22 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 369e63ef-d5ff-3d05-b486-3a5403ffc31c | -6.1109 | -57.684 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 4c88776a-b292-3175-96b9-9d9017a07325 | -6.7989 | -43.9008 | 2026-09-22 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 3076dc17-5a1c-3b29-a14c-d82a04657336 | -12.1458 | -47.3974 | 2026-09-22 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 36d7ce98-bdbc-31dd-8dd4-d05c850c4566 | -10.6875 | -50.7722 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 231cbb3d-bc03-3fed-a5c5-215a6fd095d2 | -8.2574 | -55.2604 | 2026-09-22 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f4949444-cb28-3b47-a832-a8a96274d92e | -6.5315 | -55.3576 | 2026-09-22 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bbf80af6-9c35-394c-8141-d9411cade86f | -3.7856 | -60.7525 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 523.6 |
| 02d4e896-b627-3ebd-a144-9b9a63ab003d | -13.8957 | -45.4681 | 2026-09-22 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| af8a9752-1332-3f01-ba9d-ca80725b226d | -11.0052 | -53.996 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 418.2 |
| 626f8e17-3d6a-3f6d-a769-dad85cf66984 | -3.6946 | -60.6025 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 64cc9a29-2277-3a40-a40a-81fe0c1165dd | -6.2396 | -41.6634 | 2026-09-22 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| a209a6d7-ae94-39f9-b0c4-fff5516ef02b | -3.7129 | -60.5832 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0e681c49-647c-343d-b9b0-f75d146b0bef | -11.4404 | -47.3355 | 2026-09-22 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e731dbef-053b-3ddb-b034-e3d882a5512e | -7.4765 | -45.4872 | 2026-09-22 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 3c1bbf7b-493a-33f8-a59e-b89667c74cf2 | -11.7079 | -50.9811 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 98f36340-d0bd-3799-926d-6bb908b80c8e | -13.2791 | -51.7737 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2c9050b0-036c-321d-87c4-d374bc4892ba | -11.3603 | -51.4009 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| df5a080e-907c-3c2d-bbdf-6743d9b02785 | -11.3416 | -51.3817 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 51474241-b5a1-3453-833e-edaabf10d42a | -8.6169 | -54.6328 | 2026-09-22 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f19ce900-1a89-363c-9521-c1cbb7d42dc3 | -3.6763 | -60.5839 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README130.md)
