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
| 857da034-9ac9-3c91-ad29-efefef953184 | -14.3231 | -47.3171 | 2025-09-09 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 539fac97-be11-3114-8c94-b76183f926c7 | -12.2181 | -53.8798 | 2025-09-09 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 7fe056b8-4493-3ac8-bb2e-dd985527e8d7 | -11.4469 | -43.5988 | 2025-09-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6b856703-d80b-3e0a-b1cb-f0d00a66d81a | -12.2178 | -53.9005 | 2025-09-09 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 415b7bf7-bbf5-32d2-9d83-760a91cc595e | -5.5506 | -45.1664 | 2025-09-09 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a5c60991-628f-37c5-8a0c-8a47112542e4 | -9.0934 | -45.7088 | 2025-09-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a455f3f3-0e49-3544-8a0a-8e2f1e2c72a1 | -12.18 | -53.8836 | 2025-09-09 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0f844722-f8cf-3721-a83d-5a8034392abd | -17.2563 | -46.7346 | 2025-09-09 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 04f73a7e-aa6b-37ab-9a55-7cd0cf47bfb7 | -11.3552 | -50.4233 | 2025-09-09 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 33cca9db-17fb-32ae-be60-6c48416bf1a0 | -5.453 | -43.4525 | 2025-09-09 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 6b04cdb9-de45-3a04-a04a-e30a1453c4f6 | -6.2226 | -43.3459 | 2025-09-09 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6c4c9ee0-982d-3f50-9410-7d267cc4da11 | -11.3389 | -46.5419 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4192dd72-b766-3050-a2f0-6db4080a078b | -5.589 | -42.9048 | 2025-09-09 13:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 305.8 |
| 5a9ce177-bc9a-3189-bc1a-0c1bc92ee9db | -14.2752 | -44.9592 | 2025-09-09 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 18b245ff-b86d-32dd-8998-0caefac0ea08 | -5.8406 | -44.0951 | 2025-09-09 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 23937fca-a9f1-3d2a-94ee-cac3bec617fc | -11.4277 | -43.6017 | 2025-09-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a0079676-7e9c-3cae-a3f6-2f5b1dbc87ce | -11.3014 | -46.5018 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b8581029-81d1-3795-b049-4a33ddd03a0e | -5.8395 | -44.2103 | 2025-09-09 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 515aec4f-85e1-33a0-94c6-febef21710fb | -8.4119 | -49.0869 | 2025-09-09 13:20:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 186ec089-9936-313a-8499-b3121940a91e | -11.4272 | -43.6254 | 2025-09-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 99ea6a04-7006-34dc-bddb-f8a2f0541a3d | -9.7203 | -46.8526 | 2025-09-09 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c6910429-bdad-3cbf-9934-0f0482cefce9 | -15.8205 | -52.2444 | 2025-09-09 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 120bc07f-89f9-3337-adbf-f33019de42eb | -12.0298 | -51.0722 | 2025-09-09 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f3bb2754-e6d2-37e4-ac13-7683c8f9a510 | -12.0291 | -51.1149 | 2025-09-09 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| faf67ded-47d8-3c04-b0e3-6566b3a34036 | -7.789 | -46.0891 | 2025-09-09 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| bc3acefc-8f22-3fd2-9d7b-691c7b528f7c | -13.2215 | -51.7808 | 2025-09-09 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0d9f73f7-bae4-36da-819c-a263819a4121 | -11.3549 | -50.4447 | 2025-09-09 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| e8e9e895-a950-3898-a87a-a1dd4ce930cc | -12.1988 | -53.9024 | 2025-09-09 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 193.0 |
| a6ca677e-b298-3293-805b-a86a5f6a3b5c | -7.5611 | -44.6597 | 2025-09-09 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 94fef924-a0fc-333b-85a1-ff8439581f35 | -11.3018 | -46.4792 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 7dba031d-606f-3c65-8e34-07290f4adff1 | -12.0295 | -51.0935 | 2025-09-09 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1f7dce58-406a-3b18-81ec-255fd8d3dcaa | -6.9321 | -45.5126 | 2025-09-09 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d4d841b1-bfc8-36d1-8a0d-9ceb6eb18c92 | -8.0606 | -48.6423 | 2025-09-09 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8adc08c5-3033-38f8-95ed-43c6ac3813e8 | -7.5799 | -44.6579 | 2025-09-09 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 7910dd84-9143-3828-bd49-6b9b493cbe84 | -5.5504 | -45.1891 | 2025-09-09 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 5bba5e12-04a0-33f0-ab24-a9429ec9e65d | -13.2023 | -51.7831 | 2025-09-09 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 820ff8df-ae74-3930-a7be-3ec461841fa5 | -6.2224 | -43.3693 | 2025-09-09 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cbf4d6ce-a6cd-30b5-8cbb-49da1044f8ec | -5.4343 | -43.4538 | 2025-09-09 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 331.5 |
| 55f062b7-e33c-3d38-a0dd-8770a958d7ea | -5.589 | -42.9048 | 2025-09-09 13:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 290.3 |
| d50464c3-2b40-338c-9c0f-2e343dda20a1 | -17.2768 | -46.7073 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a087e3f3-b88b-3715-987a-dd1149fd6928 | -7.5799 | -44.6579 | 2025-09-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 371f165a-94cc-3ce7-aa75-6309b3b5767a | -5.5504 | -45.1891 | 2025-09-09 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 91b40b78-1b48-38ef-aa0a-bc1f4b9b983d | -11.4465 | -43.6224 | 2025-09-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8d4950e8-ef52-3ca7-bdec-3998785cf7a1 | -5.8395 | -44.2103 | 2025-09-09 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 97e698ce-2c67-3f89-bbf2-e0dda26d952f | -5.5702 | -42.9062 | 2025-09-09 13:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 342.2 |
| e13fefae-4f5b-389b-ae23-0baa3f8077fc | -11.3549 | -50.4447 | 2025-09-09 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 1d43c425-ed7b-3e91-bbf3-9910f13d9f18 | -12.529 | -45.2756 | 2025-09-09 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d994308e-6554-321f-a21f-9678119a3e21 | -6.9321 | -45.5126 | 2025-09-09 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f70712b2-aa83-3647-abd4-0242cc667a36 | -11.3389 | -46.5419 | 2025-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 9f8bd485-76ba-35e7-a889-345cbd8449f1 | -8.0794 | -48.6407 | 2025-09-09 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 34ad71b0-53c5-3b1c-a803-b5b3d18ad0d9 | -13.0357 | -48.0298 | 2025-09-09 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 02b80840-65ab-334d-8abf-4ab8bc89ff7e | -5.8218 | -44.0965 | 2025-09-09 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f87de30c-ff59-33cd-869b-246f9772f75e | -14.1901 | -41.8111 | 2025-09-09 13:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| c1ef985f-e7f1-35c4-9120-cd2c7911bdfb | -12.18 | -53.8836 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 3afd9eaa-dc4d-3f7b-bd6e-32936510b15f | -11.3552 | -45.5634 | 2025-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 42b4ff68-ae1c-3cee-86a9-40260207581c | -8.4116 | -49.1085 | 2025-09-09 13:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9a92c7b2-5ae7-337d-a12c-9e93a65d0367 | -15.8205 | -52.2444 | 2025-09-09 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 7a5a2974-f782-32e0-a1f3-543a92e9ef46 | -14.3231 | -47.3171 | 2025-09-09 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 23b2b8b2-c579-335b-bd35-e5f4177f79ba | -17.2757 | -46.7538 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 323.8 |
| 272759d8-b3d3-3e2b-9d3a-2557246c030b | -4.7346 | -44.4457 | 2025-09-09 13:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| de99f7ec-063b-31f4-bded-c7158321344e | -8.0606 | -48.6423 | 2025-09-09 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 16dc7bf7-fa02-30e9-a68e-d46624b4e7f8 | -6.199 | -45.8186 | 2025-09-09 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b9bc1d99-8d5a-3c07-bd0f-7b576a3e61cb | -11.4469 | -43.5988 | 2025-09-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 38e6f196-94fc-34e2-b107-f186ebaa72cc | -6.527 | -44.7974 | 2025-09-09 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5a247196-5996-3e64-abf6-77fd891a6e78 | -11.4277 | -43.6017 | 2025-09-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| eebbec3b-bda3-315f-80e3-79e7f24d0417 | -9.9653 | -51.1822 | 2025-09-09 13:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 481a2ebf-9ef8-3c55-b62b-df18699b7f13 | -17.5794 | -49.8243 | 2025-09-09 13:30:00 | GOES-19 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a2d7b9ea-f08d-3ac0-9360-0767f39fa9b5 | -5.3669 | -44.793 | 2025-09-09 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| afb024f5-5bae-340f-acfa-615dee27f0a0 | -11.4272 | -43.6254 | 2025-09-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 591894d9-dbd9-33d4-8603-c0f565b716f6 | -11.3552 | -50.4233 | 2025-09-09 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| b6bae1ff-8572-362a-80e3-7d27566aca37 | -13.055 | -48.0271 | 2025-09-09 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 938036e4-8b80-35d9-b170-d8ae4464e755 | -6.2224 | -43.3693 | 2025-09-09 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 6cee26e4-586b-3c1c-85e5-b068308a9ab1 | -5.975 | -45.7901 | 2025-09-09 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| b2b0a9e4-90a1-3b18-918d-77611071d691 | -16.3602 | -43.0349 | 2025-09-09 13:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 15441a36-2963-3846-8baa-aeb9ce04bccc | -12.6343 | -56.9725 | 2025-09-09 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4f9aa28e-5762-3ea9-b02e-db8360c06a7b | -17.2762 | -46.7305 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 400.1 |
| cec78dc7-4dda-31d6-8e8c-e2b6d7309673 | -6.1896 | -41.0398 | 2025-09-09 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 2e821c54-baef-3ef8-bfcc-d7825f56da45 | -15.7778 | -53.5242 | 2025-09-09 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6b85821d-6b0c-36f6-b1f0-a7cd8d50efff | -13.2023 | -51.7831 | 2025-09-09 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c6366ebb-8ff4-316c-ac83-8e39322f66cf | -7.789 | -46.0891 | 2025-09-09 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 314c088c-087c-32e1-83fb-21df69bdde29 | -5.8582 | -44.2088 | 2025-09-09 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 1d8ef94c-f5e2-381e-b7c8-c70290548a30 | -5.9362 | -45.9498 | 2025-09-09 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a2a2b8ee-3ca0-3b71-8bfb-d89ad15ac652 | -16.3403 | -43.0394 | 2025-09-09 13:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 0ada376c-e141-3d25-bdfb-4339ffaa767a | -13.2215 | -51.7808 | 2025-09-09 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8ddf764c-4fb3-3705-aaf7-6c70940e5570 | -21.127 | -48.8519 | 2025-09-09 13:30:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.0 |
| 72d45f41-9179-30f2-bdb3-639714ec716b | -17.2967 | -46.7032 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 7c273268-b3b2-3c30-95bc-dd7de649dfda | -12.1993 | -53.8611 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| bb196bb1-a4e1-3fa3-a2c9-91eff48e3f50 | -12.1988 | -53.9024 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 192.4 |
| f6d28de7-4fd7-32d6-9fa1-1a72dae7e922 | -17.7328 | -44.4637 | 2025-09-09 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c5d49e77-35d4-301f-b744-c23b35cc93fd | -17.2563 | -46.7346 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 348.2 |
| 5ac64b4b-535a-3f99-a74b-0115b4ead193 | -6.2226 | -43.3459 | 2025-09-09 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8c9ac337-86cb-3c82-b1f8-8897989f1c01 | -15.7775 | -53.5454 | 2025-09-09 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9ab7b591-e351-3960-b485-f0b30864b2a5 | -5.5506 | -45.1664 | 2025-09-09 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3eea3821-7b5f-3bef-bd70-58f5399a3308 | -5.453 | -43.4525 | 2025-09-09 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 503.7 |
| b11fc38f-c2da-34ec-8061-1f45ba514b0f | -10.2982 | -48.8148 | 2025-09-09 13:30:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 3112f9b4-2675-3767-953c-d21937aa7af5 | -5.8397 | -44.1872 | 2025-09-09 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8ba0a668-fc5c-3795-9b0b-33b19930eda0 | -7.5611 | -44.6597 | 2025-09-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 9639fbb1-4171-351d-9242-900f7604390a | -8.4119 | -49.0869 | 2025-09-09 13:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 60332d88-796a-3bd9-944e-737eda81be73 | -5.4587 | -42.797 | 2025-09-09 13:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 58d1aa6f-d782-3f8d-a560-4be0233d0615 | -5.3482 | -44.7943 | 2025-09-09 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |


[Clique aqui para ver as próximas entradas](README79.md)
