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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c313fe96-030b-3f99-bff7-d1cb1c5d68af | -14.31299 | -60.34822 | 2025-09-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 605ca73f-b091-3d42-86f3-17c606f5a274 | -6.84866 | -52.8105 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94c9c452-f1b1-340d-a89b-16cf944b517e | -10.50127 | -68.10567 | 2025-09-01 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29707b14-cdca-33ad-8de7-5486bea20ebd | -10.57772 | -67.75698 | 2025-09-01 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793d4f3d-11b3-3b0e-a109-d8a816d1830f | -11.59275 | -55.55103 | 2025-09-01 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff782ffa-4b06-3ecd-b932-169841df7161 | -12.86784 | -48.07507 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 06cd6dae-09b2-30bc-a4e9-0704da33854a | -12.58288 | -48.20543 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d33ec164-04ac-3f82-8f5a-549551c13aa1 | -9.02373 | -70.66422 | 2025-09-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 981a92bb-a199-3b58-b2f2-8722f03eb560 | -15.62748 | -55.92715 | 2025-09-01 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6beff1-2a32-3e8f-af9f-b35570e10ad6 | -15.15621 | -52.34627 | 2025-09-01 05:25:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea88e3a-a0b8-3185-8731-d7cf1c7816f6 | -12.5795 | -48.20913 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2fa646a0-b641-3a9b-8ef4-018a6b1b7074 | -12.42241 | -63.90676 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ab146f5-068a-3ef3-9820-d45337516877 | -18.65836 | -52.59941 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c15c42a1-87a4-3664-8b74-aba23d40ccb3 | -15.70425 | -48.89189 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c751aad2-818c-3800-ad35-9c82b1aca002 | -14.60288 | -54.48816 | 2025-09-01 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 414d8e79-1600-30d2-8b56-b02e467cda5b | -8.87064 | -71.27735 | 2025-09-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb9a6e9e-673d-3246-8a72-f82bcd909c1b | -12.95508 | -48.10213 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b2f640b-30a5-34b6-93dd-fc889612e4ed | -18.65756 | -52.60211 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4784fe66-3c72-32a1-8cfd-ffe5d33c0a7b | -15.60903 | -56.00029 | 2025-09-01 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213f772b-fb7e-36f4-b59b-6b760ef820ab | -15.70353 | -48.89974 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f10c0b77-bf87-3ac8-8ffb-b33e32240d59 | -6.1958 | -53.76374 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a29180-8701-37d1-9af5-2483370a4bf1 | -21.72807 | -50.74988 | 2025-09-01 05:27:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5815dd1e-3183-33dc-a76d-d9a99d424c8b | -19.97527 | -50.41648 | 2025-09-01 05:27:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ac689090-87aa-34c2-9727-6268aab62477 | -26.3278 | -52.70781 | 2025-09-01 05:27:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 11894fbc-588e-32a6-8e00-ba2d28bcfac4 | -26.71229 | -52.45002 | 2025-09-01 05:27:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e31b9e29-397e-3f61-9c03-217179490aed | -19.97477 | -50.4226 | 2025-09-01 05:27:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 55140a39-354a-3545-b714-f3e7ceb807a1 | -26.7062 | -52.44439 | 2025-09-01 05:27:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1deed677-370e-32b1-8f68-733d05131a7d | -20.9009 | -55.14345 | 2025-09-01 05:27:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 667f8bfe-a9a7-3012-9633-afc0e70dc2b9 | -21.72855 | -50.74337 | 2025-09-01 05:27:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1816e14b-9c05-34e7-8391-e0495dd39850 | -26.32813 | -52.70288 | 2025-09-01 05:27:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0c944048-d296-34e6-ac57-e7df04221042 | -20.8961 | -55.13983 | 2025-09-01 05:27:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdcf56d8-0139-3183-83d7-22f3a320db3b | -26.71263 | -52.44453 | 2025-09-01 05:27:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c857b53a-332f-3e0b-9ce6-867b7f7715c9 | -21.73529 | -50.74415 | 2025-09-01 05:27:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 01d9a106-94d9-3147-9cce-028addc1c104 | -11.0565 | -45.1691 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2be946c4-9d26-3648-be96-d81db6be4f38 | -12.8625 | -48.0545 | 2025-09-01 05:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9f9674f3-b09a-36c0-99cc-240ea9d248c5 | -12.9194 | -56.9672 | 2025-09-01 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 40bb4ad4-debf-395c-9e2c-a68a1e6f82d5 | -18.6704 | -52.5973 | 2025-09-01 05:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 17c7babe-dccb-3888-9574-b4b2ac94f61d | -11.0568 | -45.146 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 314.7 |
| bfa67660-cacb-374e-b545-958c4be60a5c | -15.5862 | -48.3435 | 2025-09-01 05:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5f770db2-ea4f-37ab-8b29-372c897275ab | -13.1644 | -45.2897 | 2025-09-01 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 65f41614-ab29-3d29-9046-0d9b7818c76c | -12.5722 | -48.2059 | 2025-09-01 05:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 905d46bd-85ec-38ee-ad47-d0e2748cf578 | -11.0381 | -45.1256 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9bb1077b-06c2-3d23-8d51-2a6555282c75 | -7.0757 | -44.3606 | 2025-09-01 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 42b5f580-bdb9-34bd-a016-ee25740ce050 | -11.0377 | -45.1487 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 324.3 |
| 2e170c5c-2855-32f2-94af-bba7e833d0ae | -10.6128 | -44.3284 | 2025-09-01 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| b7c0af88-da09-3249-96c9-4466e1bec551 | -11.0572 | -45.123 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 930d26c5-cbc4-39ce-8784-5b0c7c6b0b79 | -14.7422 | -46.7701 | 2025-09-01 05:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f0f5cb1d-57ad-38a4-a22d-409ee582b50c | -7.076 | -44.3376 | 2025-09-01 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d7258e31-cf8a-3d62-9e39-2e4024ba2713 | -15.7289 | -48.9892 | 2025-09-01 05:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5ea16cea-4fab-3e66-9627-5463fe73e816 | -7.0948 | -44.3358 | 2025-09-01 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f2a3ac77-80f9-39bd-9f55-79ad09deff13 | -7.6783 | -61.0908 | 2025-09-01 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 3030f879-3a2d-3df1-a2d7-2ce5f0aff169 | -12.5718 | -48.228 | 2025-09-01 05:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f0dcf5f5-4069-3f7d-85d1-a7e7845c27c4 | -18.6503 | -52.6007 | 2025-09-01 05:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 2d731fd2-69d2-39ad-abc7-ef8228062b8a | -6.8281 | -52.8143 | 2025-09-01 05:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f4a870c9-921f-32c5-9ccf-4f789e76aa23 | -11.0373 | -45.1717 | 2025-09-01 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e70105fe-fc3f-3756-bd07-668df5fd59bf | -10.5937 | -44.331 | 2025-09-01 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 99a510d1-fa66-335b-9376-9a024a6d6749 | -7.0946 | -44.3589 | 2025-09-01 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d01f8d56-1cf2-3097-a481-93da0231c5f3 | -11.0461 | -46.9842 | 2025-09-01 05:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e6cd97a9-4b4e-3103-922a-76cd3dcc1a33 | -6.84102 | -43.32981 | 2025-09-01 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| dd5cbea4-c275-3f14-87b0-e35fa0c5e3bd | -6.7603 | -43.79189 | 2025-09-01 05:33:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 48b834c1-0b01-39c4-9029-93a4c958cc09 | -7.07351 | -44.34391 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| eba2e581-d284-36c4-b463-7f8b14ed7a2b | -6.31271 | -43.63142 | 2025-09-01 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc02860d-8576-387c-b792-a70dd1f94e97 | -6.83221 | -45.68799 | 2025-09-01 05:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 69f6e473-fb23-33a2-951e-8748e875d0dc | -6.46999 | -41.74688 | 2025-09-01 05:33:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d257145c-7fe4-3832-aecd-35c85b97a994 | -7.09689 | -44.3438 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| dee643af-e960-35f0-b07d-30a98abc6c6d | -6.29559 | -43.55917 | 2025-09-01 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dd484ee3-35ce-30f7-8917-371994ef8b5d | -7.09854 | -44.33339 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 37701132-aac3-37fb-b1ee-5ac59ed6d641 | -6.83193 | -43.32843 | 2025-09-01 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| d8e0bb7c-539c-36e8-9b61-a75f169ee51a | -7.62769 | -44.03743 | 2025-09-01 05:33:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8ed06feb-8c1e-3317-a539-9f51690670d1 | -7.09094 | -44.3576 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 70aa3fa2-b246-374f-953e-ece8e9de94a1 | -7.95848 | -46.451 | 2025-09-01 05:33:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 05829a6d-f729-35a8-8a4f-2c1519e06a6c | -6.84247 | -43.32038 | 2025-09-01 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 438d440a-dbba-36ba-ae5e-7afa67654298 | -6.25975 | -43.91008 | 2025-09-01 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e04f8baf-7522-3261-8708-fc579396350e | -6.42751 | -43.95832 | 2025-09-01 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c8c6623a-6ccf-3101-8b12-c995da7d612f | -7.24631 | -44.23369 | 2025-09-01 05:33:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4db718ef-306e-3cd8-83ad-877d815548cf | -7.08142 | -44.35602 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 165746f5-c4fa-3051-a646-3878ac4eeab0 | -6.28846 | -43.56118 | 2025-09-01 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 858f9266-dc64-3014-abcc-58dbd0c6f743 | -5.6645 | -43.6419 | 2025-09-01 05:33:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51595262-902c-3c35-8204-01f9677cfaeb | -6.75255 | -43.78059 | 2025-09-01 05:33:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8618ee88-0ef0-3e97-9ac5-0b355d20f333 | -6.31118 | -43.64128 | 2025-09-01 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0ae4be63-5f89-3a85-9231-c268f8e7928b | -7.09417 | -44.33652 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 15368a5b-c34e-3a62-ab60-58a4ed2d3b18 | -6.30651 | -43.61043 | 2025-09-01 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| fd447c19-55c2-3619-9692-1209f63d2966 | -7.07512 | -44.33349 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 934cc258-6918-3d4b-9b8c-7990eff80d4b | -7.2447 | -44.24402 | 2025-09-01 05:33:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8a195476-28e2-350e-9291-3b75bc845e0d | -7.95614 | -46.46509 | 2025-09-01 05:33:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 9b7be943-6c4a-3c6d-b113-b98f0acb6b86 | -6.71883 | -42.24998 | 2025-09-01 05:33:00 | AQUA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c5f39b26-677e-3f9f-a0b8-109c28298d35 | -6.83016 | -45.70086 | 2025-09-01 05:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9461e42b-b22f-3d1d-b9af-4ad490e26c0d | -7.5052 | -45.83307 | 2025-09-01 05:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7a3c30a2-3b89-387d-bfca-52e91c710085 | -7.95349 | -46.45871 | 2025-09-01 05:33:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 395d9236-0650-36ef-bf32-acafe475686d | -6.57994 | -43.70113 | 2025-09-01 05:33:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f02a9983-37a7-397f-8c9c-a1e29483519c | -7.08304 | -44.34543 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d358bab8-066f-338c-ae99-eed83bf0f979 | -7.09257 | -44.347 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| f4a58194-f26d-3d5d-b0a8-fd7436cb8490 | -6.45416 | -43.97262 | 2025-09-01 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d921fb0c-5ee0-3cf6-bc85-c8a4b5edd7f7 | -6.75101 | -43.79049 | 2025-09-01 05:33:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b20beb9c-0caf-3e80-a4b8-9fafce741d97 | -6.76183 | -43.78199 | 2025-09-01 05:33:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3ed39405-0c8a-30ef-8cfe-de76b4d03206 | -6.30498 | -43.62021 | 2025-09-01 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8c3e0a1e-16af-323e-b79a-d41a070f7c0f | -5.89469 | -44.32164 | 2025-09-01 05:33:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 764d019b-e42a-387f-a975-8e03ff266531 | -7.09521 | -44.35436 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 9a2f5caa-4275-3b01-9df7-0397406a7db9 | -6.83338 | -43.31902 | 2025-09-01 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 8d3b2ab1-5499-3b9d-b904-a45678345a8c | -7.62925 | -44.02753 | 2025-09-01 05:33:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README85.md)
