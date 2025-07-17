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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb0fd225-3285-3680-9d37-ae5a9436a3c1 | -5.65712 | -43.72393 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 82187a7c-49d9-31ab-89b9-463646fd67b8 | -7.23517 | -43.50074 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b1233571-68d7-3127-bf32-befd8fd5d97f | -11.75974 | -47.8464 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dd7f132-0b6d-3f49-aa16-34681e075492 | -10.96942 | -46.46855 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c7074bc-7c33-35eb-b59c-f65d626234b2 | -10.05313 | -59.10056 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56a3a36d-8f56-32eb-9e20-4d07b596a277 | -8.88255 | -44.79536 | 2025-07-17 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cc29baf1-2958-32c0-a91b-aa5f5cc1796d | -6.97899 | -42.81292 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ce3656dc-6f2c-3a21-8c0c-131ce62d7f1e | -6.85001 | -44.7693 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c06dea04-d8f5-3e29-9d44-e429923eae4d | -6.43728 | -45.32053 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69c4208a-16cc-3099-b164-27dd810d43a8 | -11.15067 | -49.70191 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa42c6d4-7120-39e9-bc84-edc6db109f31 | -7.18721 | -43.1159 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bb148ecc-63d5-349d-930d-8d042a22092e | -6.46304 | -45.34764 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a928d5f-9030-3db3-b598-cc072841a154 | -6.8865 | -47.24081 | 2025-07-17 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85bef5e1-652a-37a3-ad5b-7c84e6f15abf | -8.877 | -47.27092 | 2025-07-17 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a91fd8bd-f5cd-30c9-930f-bbe00991ab25 | -8.09716 | -43.15104 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 953fa7bb-9f30-3ca9-9816-4c2796f21dc2 | -6.72797 | -44.32931 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2d2dd9a5-1274-3fa7-be6a-75086b86e030 | -5.53047 | -43.88862 | 2025-07-17 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ac3b7ead-7ff7-30da-9713-b49da2603cf5 | -5.66181 | -43.72473 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9d2f79f1-c01d-39f0-8949-98a715c47c4d | -5.91055 | -45.58289 | 2025-07-17 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90904cc9-ce91-34dc-9ec7-0b5862c8d40f | -11.1127 | -46.99923 | 2025-07-17 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdbc3a2e-a52a-3202-b8e4-a4fc5871f0e8 | -10.89721 | -49.20814 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2725ee4-64a2-35b7-bcb3-5a0960288ab5 | -9.02001 | -61.22626 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ab7a238-c677-369e-923d-5b3a493e4aa9 | -12.47571 | -44.50265 | 2025-07-17 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01269763-80de-3e78-be44-f8988203223e | -9.23838 | -48.55885 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd6e446b-cd97-3e4f-99c2-b686cd58a8d2 | -5.59212 | -45.79795 | 2025-07-17 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1294fcf9-afef-3ae8-a4af-ffe455e9756e | -5.79423 | -45.10481 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7b721e4-34f0-3ac6-8da2-87ab389a4af4 | -9.20467 | -49.67309 | 2025-07-17 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0481915-479f-33a2-8ed0-84dad2537b3c | -9.13393 | -40.54374 | 2025-07-17 04:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4da1b2e7-028a-3553-a846-f5da5a1aa13f | -8.05989 | -50.10467 | 2025-07-17 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 376811e0-9ff9-31a9-be09-9646b39d708d | -10.6182 | -48.07737 | 2025-07-17 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47ae12e0-2115-3f16-a8d3-6317a9768598 | -6.70583 | -44.31844 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a4ecf80-8b3c-3f3c-9315-12877994db68 | -5.79483 | -45.10077 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b711ebab-5562-35e9-b29b-f2e63c91363b | -7.56876 | -48.41176 | 2025-07-17 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3866ab8a-0962-3bb1-add3-c07db9cb680d | -11.39611 | -48.70033 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c2426bb-1b69-3c56-bd96-e8100e634682 | -7.09266 | -49.17658 | 2025-07-17 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a49575b-e9dc-3a57-bd6a-2912243f4b10 | -6.71816 | -44.33269 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 432d55de-31fd-39c3-959e-5d0be0f4b21c | -10.68162 | -56.54736 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15cfde55-90f3-3233-bb9d-35fd6b4518c3 | -11.91721 | -49.38347 | 2025-07-17 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 945f2c0d-551b-388a-9767-75d26f07e200 | -12.09771 | -48.19748 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66282c98-1945-323a-b0aa-593f89e92973 | -6.67246 | -43.03115 | 2025-07-17 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5d5d39-6776-33de-847c-e8970498d178 | -9.38066 | -40.62302 | 2025-07-17 04:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e98376bf-fb1e-3943-b1bb-f482521ffc29 | -8.03942 | -49.88909 | 2025-07-17 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d1434b1-ddbd-3091-90c2-3694a7d4d4c7 | -7.19725 | -43.11731 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| de8e97c2-fef3-338f-8d31-12ec27555a3c | -12.02501 | -47.78161 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 171681d0-b4b3-3a5a-ae1d-8b73b7eeff15 | -5.65783 | -43.719 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 65bf942a-288b-3f72-bf62-e91c37234c20 | -5.44967 | -42.62918 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ae065d1-df87-319f-9a40-2e4b0f7695b3 | -10.96996 | -46.46456 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43c7942d-0413-3147-8a9a-b6f2e14ba315 | -8.88766 | -50.15183 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90bd006a-483e-3916-b3fe-335ac56b0404 | -10.5485 | -46.51577 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80bb67fe-168c-3ae9-8592-7066b27c1917 | -9.41292 | -48.41195 | 2025-07-17 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adde3dc3-9e05-3bd6-ad2b-efe1b81ddfaf | -8.87799 | -44.79461 | 2025-07-17 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7c44b3f2-4908-3166-a81a-694674416085 | -6.99968 | -43.74714 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 31550546-f1a6-3909-81cb-e71b3ed2788b | -7.21181 | -43.16074 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f014c7ef-171f-3835-896b-542cdb5c6b3a | -7.0656 | -44.05153 | 2025-07-17 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 97d2004b-ab24-38cd-9700-ffa57a964412 | -11.11487 | -48.86466 | 2025-07-17 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c724562-878a-3ecf-a00b-6b154b5edbde | -7.25462 | -56.27267 | 2025-07-17 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8afe0749-0ce3-30a4-9d57-be5ed0009822 | -6.4401 | -42.67849 | 2025-07-17 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a6407d5-e869-342e-958c-6df44c8d1ef8 | -6.70641 | -44.31621 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 13be3b3d-ddc8-396b-a4c7-91d1b1eafca2 | -7.35383 | -44.20024 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ac899b9-c3a2-374b-ae99-39f1309f5521 | -7.20528 | -45.3312 | 2025-07-17 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4e73238-bd54-36d3-a685-2d54cb435380 | -9.24563 | -48.55994 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9bb9163d-ef7a-36d7-a3ba-6c810ce5fb09 | -11.47585 | -47.32076 | 2025-07-17 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b9c7d83-0f36-3a15-938a-e8de991db3bf | -8.88821 | -50.14817 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 935f3e96-d22a-3836-aaee-218eb69ce63f | -10.64449 | -45.22345 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc69569-493b-3612-9058-6c5a39027d03 | -8.75471 | -46.59928 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aa89efb-8d8c-3923-a573-935d5b69207f | -12.09655 | -48.19509 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cc657aa-fffe-33d8-824e-fed98f16cc4b | -6.72273 | -44.33337 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 829121a5-59fa-39ac-934f-cd52d9b6a876 | -7.06312 | -44.05348 | 2025-07-17 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 13875166-279a-3ef1-aae6-9c43a1120ac2 | -10.24414 | -59.27294 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ec1cd5-03c8-38d4-abf7-df6c9dc2af0e | -8.21855 | -44.91807 | 2025-07-17 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 209b3c2a-6014-3508-891d-10def0ab67b7 | -11.36225 | -48.7267 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 568a69c2-6133-30f9-ba24-84b6d4b0c441 | -6.72339 | -44.32864 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a5712319-5169-360a-a0bb-55ced5bd3c51 | -11.11122 | -48.86409 | 2025-07-17 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ea9d39f-25b0-3093-81f1-7b7ea72f10ae | -11.32854 | -51.43826 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3adbca96-0d58-3e10-ab52-2f55d3950a40 | -6.66311 | -45.19479 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29bc8432-3b75-3660-a5b6-328dd00fbc43 | -9.31112 | -44.84346 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 311d94d3-f0ce-3a47-aa75-9e00a1db4f42 | -9.24138 | -48.5637 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f0249919-d4a9-3af9-b799-31212608f84a | -7.19223 | -43.11659 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e15311b6-f378-39f2-bc2d-5fc4eb42a6f9 | -7.18761 | -43.11427 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9c7c2a3-0524-34b2-a3bc-9076fc8fa86f | -11.91876 | -49.38708 | 2025-07-17 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d9dcbae-4a86-33a1-a568-39670b44d1be | -8.75116 | -46.59509 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dac20f0-0255-3795-ba98-4663730eda8f | -9.38676 | -40.62382 | 2025-07-17 04:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1ba04ba-60a1-33a4-9ff5-36ef35da3fef | -10.67777 | -56.54672 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 57a50ca1-28c5-3dd4-bcfe-07079b5f1384 | -10.97203 | -46.48091 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 46ff1602-39f1-305a-9441-b7208dad2758 | -8.04337 | -49.88595 | 2025-07-17 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802007d6-9426-3488-a0b3-70946e8bf9ae | -6.13975 | -47.31255 | 2025-07-17 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8fb8aac0-5ed6-3e2b-89a5-152748d89ce5 | -11.24186 | -49.49881 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08ba26e9-c3eb-3928-af12-d885b80fe4af | -6.85349 | -42.05283 | 2025-07-17 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59f1224a-70c9-3984-afae-3eb83a7d7b5d | -10.56711 | -49.14138 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b2e56a8-e8f1-3b99-9fec-f0a569db7b29 | -12.47363 | -44.50231 | 2025-07-17 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba9578f-dde7-3e56-96e6-b886ca725be0 | -11.94573 | -48.42161 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acee50ce-aad9-35a7-af32-e419509d9dac | -5.57094 | -44.28945 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c892a1d1-2780-3b1a-adb0-4a552b60ac18 | -10.12016 | -52.34434 | 2025-07-17 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27c4c680-7216-31cf-8b6a-9a0557d439de | -6.70965 | -44.3266 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03822b5e-b6b0-3cd2-ae03-2948d50969e8 | -7.15507 | -46.0943 | 2025-07-17 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2a786bf-c96d-36bf-998d-6b593c805af0 | -11.35861 | -48.73204 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 170a93d9-3e01-3393-8271-00c060c45506 | -6.63429 | -49.74361 | 2025-07-17 04:46:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f39917-736a-3546-96f4-a3ca59ca04d8 | -7.5897 | -46.33725 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 745c9602-0cda-37f6-8f12-6fd57b9a361a | -8.53813 | -47.85311 | 2025-07-17 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a3d293d-d357-3db6-ba4f-047b6a436a06 | -6.62944 | -56.28061 | 2025-07-17 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
