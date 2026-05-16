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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29bfbbcb-1a54-3d28-b8e7-9a4e6c5afa1c | -11.86407 | -63.72211 | 2026-05-16 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99c560a-7083-377f-8832-80c7c3f6b3b6 | -12.0249 | -47.80197 | 2026-05-16 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a39dd3f2-13ae-3d88-8478-cecd517106b7 | -10.98227 | -45.09453 | 2026-05-16 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53568e88-067e-3c60-904d-7f1f50f05725 | -13.03272 | -49.93747 | 2026-05-16 05:06:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab0066f3-0925-3ee2-98bb-4c23acfa2ab7 | -10.97999 | -45.09949 | 2026-05-16 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0178ea98-0792-3387-8929-6ad322815c17 | -13.31958 | -47.51036 | 2026-05-16 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df0ae980-907b-323d-b775-0e6acaffb5e5 | -8.85804 | -50.21642 | 2026-05-16 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbf8e654-d293-317d-a10d-2e0ab6835e12 | -11.74871 | -54.79603 | 2026-05-16 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c415f1c9-769e-3b5c-b248-8691f53f1026 | -11.94097 | -54.097 | 2026-05-16 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d2f234d-5b66-375a-823a-bd829d1f84d7 | -11.46594 | -55.12223 | 2026-05-16 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63faa26d-e448-3c19-93c4-7aa842a8b20a | -12.85493 | -43.75732 | 2026-05-16 05:06:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84d03cf5-3212-34b6-8459-8c21df3a4545 | -11.04267 | -48.92019 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67556630-4936-3482-ba9c-0be5b1aa9062 | -11.44212 | -54.0957 | 2026-05-16 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c72a04b-6789-321e-aa2c-64baff4b75c3 | -10.98055 | -45.09464 | 2026-05-16 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a472a06d-6a62-3153-a61e-3d1ec633efe6 | -11.31332 | -54.03638 | 2026-05-16 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1064954a-e968-3c4d-8a5f-9cac27007d2f | -11.66779 | -54.5833 | 2026-05-16 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 615b497c-71bd-3058-8d56-49f732e6c1c6 | -11.04562 | -48.92691 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b0ab711-0631-33c6-8659-f90749c57340 | -11.04081 | -48.92598 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 227d86a4-da3e-3cbe-8dd2-7efa4f698e6f | -11.04192 | -48.92581 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad6dfdfe-6ab4-31c2-aa1c-ae5fa59e0a75 | -11.59623 | -48.02768 | 2026-05-16 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d4ebcb0-8c3a-3b51-8e8c-fb37c681fafe | -10.6651 | -49.70515 | 2026-05-16 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 14c1528d-ae6b-3228-b71c-ab98e388044c | -11.04119 | -48.93122 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 132cefd4-5b3f-3a76-9e36-5658233a8409 | -9.45786 | -47.82235 | 2026-05-16 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a629bf16-9e31-38ff-a46b-edd491492719 | -9.23714 | -46.65251 | 2026-05-16 05:06:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55953d12-3d5e-39c6-bc9a-6da12432b816 | -10.98168 | -45.09938 | 2026-05-16 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ee12f79-51ab-3049-9a6a-8a61a3827e2b | -9.45007 | -46.10715 | 2026-05-16 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e6e5d9-ddf7-3ff1-8645-fdce43bb3965 | -11.74471 | -54.79931 | 2026-05-16 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef8051cf-57fb-333a-96c0-d18de71e78a8 | -11.94445 | -54.09598 | 2026-05-16 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa6a9f21-c9be-32c5-a18b-121f6d67097e | -9.4537 | -46.11029 | 2026-05-16 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b33aba9-a00d-3f89-978e-464e566f0db9 | -9.4558 | -46.10793 | 2026-05-16 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44649bb8-ba59-3a0d-9b9f-63c737a03204 | -9.45576 | -47.82326 | 2026-05-16 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66ff3b8e-deda-3848-bf6e-732f36548f91 | -11.93678 | -54.09896 | 2026-05-16 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1202514f-4975-37da-807f-3ff60c033a70 | -11.94033 | -54.0995 | 2026-05-16 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ac08b1d-f330-3c70-98e4-2a0c67f92528 | -11.85959 | -63.72127 | 2026-05-16 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c86d55fa-b6d1-3178-83ac-90d8f3011bf8 | -8.85861 | -50.21228 | 2026-05-16 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6073a36-94d8-391b-8464-4cb7a9f64419 | -9.45614 | -47.82026 | 2026-05-16 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af51ba8-2963-3d5f-a894-10132666c16b | -9.79074 | -48.07892 | 2026-05-16 05:06:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb89a41f-42be-3803-9c35-c62ba58b938f | -11.59066 | -48.03007 | 2026-05-16 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1650b0d-ff7d-3dcf-813d-f0e98a57f240 | -11.59584 | -48.03085 | 2026-05-16 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e24bfea-5b65-389a-93a1-8e0289741c69 | -11.97819 | -47.36767 | 2026-05-16 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1138f8a-99c3-36a5-990d-60ab9525f371 | -11.04012 | -48.93139 | 2026-05-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf4bf156-d9e2-374c-95ae-558d777939cf | -16.17126 | -58.48 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 27acdc25-6a3f-3393-8477-1183311ea9ae | -16.16576 | -58.47142 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 806aa780-0fe3-37b9-a513-349c003d6d4a | -16.174 | -58.48416 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f20dd80f-4580-3612-bff6-4f5e276b6ae2 | -16.17183 | -58.47641 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 13760a5f-70e6-3dde-afde-eefdfea24b4b | -16.42652 | -52.79687 | 2026-05-16 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e926163-cfff-33f3-9ce1-cf7333002d80 | -19.67925 | -51.37869 | 2026-05-16 05:08:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a622823-3c19-317a-808c-5142e8697251 | -16.17069 | -58.4836 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3c050a13-86cc-3a31-aa76-fd5fffa179df | -19.68808 | -54.35354 | 2026-05-16 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e21d5132-02e7-3f56-a5d0-50005e293f32 | -17.86221 | -51.78354 | 2026-05-16 05:08:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d412ce32-9e66-3258-ab6d-433cab0dbb72 | -15.99317 | -56.22332 | 2026-05-16 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4c4d1290-dc0c-3618-9eb0-07868db065c6 | -19.68373 | -51.17057 | 2026-05-16 05:08:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27678bad-c980-3977-9fd1-c2025008537a | -15.4202 | -56.31025 | 2026-05-16 05:08:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 751c9716-b26a-387b-9640-42c6d28eff2b | -17.86217 | -51.78527 | 2026-05-16 05:08:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 510c6ad3-4867-36ad-976c-389b6e2171e5 | -16.42249 | -52.79626 | 2026-05-16 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e824a125-f0aa-3185-975f-5aa3c1cf3998 | -16.16795 | -58.47945 | 2026-05-16 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2c3d4f56-b080-3995-a1ac-0aac6df91f0e | -19.68971 | -54.35222 | 2026-05-16 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb87b147-628d-331a-90ee-300c17c01320 | -21.97413 | -57.60551 | 2026-05-16 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0e690b08-a7f1-33bc-bcb3-2125fd41a07a | -6.5631 | -51.1126 | 2026-05-16 05:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1a0edb02-1ed9-3ad8-8239-09bcbf8b31e7 | -16.16844 | -58.47731 | 2026-05-16 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ce3075f3-f43d-3eee-999e-7b4fb71f6d1e | -16.17275 | -58.47791 | 2026-05-16 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a81d387d-3621-3ed2-bbba-f57f1a6c764a | -16.1722 | -58.48207 | 2026-05-16 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bf38a7dc-a412-3b87-89b8-027ec55ac898 | -16.16789 | -58.48146 | 2026-05-16 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c79b1a95-2f7f-3b71-9dd7-f3079936be84 | -11.44304 | -54.09711 | 2026-05-16 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e01e5098-8cc8-3721-92d5-edb8144632d9 | -11.86336 | -63.72332 | 2026-05-16 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 475ff936-001a-3856-a255-1baf31cd3484 | -11.8606 | -63.71925 | 2026-05-16 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f9afbcf-6c30-3ae8-b5b7-8897e0da3a89 | -11.86004 | -63.72277 | 2026-05-16 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c653db-23f7-3247-af6c-df988540f27b | -16.17165 | -58.48626 | 2026-05-16 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ef33a79c-0d93-37bc-97ed-db25deee0f56 | -10.66283 | -49.70597 | 2026-05-16 05:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ed4cb5c-29a8-3402-ac9d-711f33261082 | -10.66681 | -49.7046 | 2026-05-16 05:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ff65c83-aff8-38f2-9412-05b3af983d2d | -10.66989 | -49.70682 | 2026-05-16 05:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a17ef4f-c48c-3172-ad34-df2f4c4c24d7 | -10.66605 | -49.71137 | 2026-05-16 05:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4db55d-8c84-3bb4-b609-949c701105d1 | -11.44347 | -54.09366 | 2026-05-16 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1e58cd8-93d5-348a-a845-6fc75707d94e | -11.86843 | -43.86544 | 2026-05-16 06:10:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 721a4208-2ae0-365b-8627-ddca9214d1d5 | -8.10168 | -43.1562 | 2026-05-16 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| da7e42e8-b660-30d4-9dbd-53ee475b4125 | -8.10303 | -43.14735 | 2026-05-16 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4ada42a9-a419-3497-8633-be5b858b74c3 | -17.35001 | -42.62236 | 2026-05-16 06:12:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e3bdc542-ce65-301c-9192-ac0e442b5e77 | -17.61485 | -42.59818 | 2026-05-16 11:19:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 875ab315-6bb0-3043-8f84-cc466b62042a | -13.46661 | -42.42001 | 2026-05-16 11:19:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6e7508f6-226a-3429-b343-ebd2c054205a | -13.46474 | -42.4321 | 2026-05-16 11:19:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| db3d8d85-7fbc-3d72-acc4-e2135814abdf | -9.4468 | -46.1211 | 2026-05-16 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8895c97b-b974-3b7d-b1de-db9389d67491 | -9.4468 | -46.1211 | 2026-05-16 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| b0bd79c8-9637-3043-8154-7fdc891ec28b | -9.4468 | -46.1211 | 2026-05-16 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4e7c33d6-0e71-3081-89f6-0051b9876a23 | -9.4468 | -46.1211 | 2026-05-16 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 18e14695-0f46-320c-bac4-71d8e2a5e80f | -9.4468 | -46.1211 | 2026-05-16 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 26aa8960-46d6-3033-bbc7-265cced31968 | -9.4468 | -46.1211 | 2026-05-16 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 4ff8807f-b676-3708-9eb7-5d86d6a3340a | -9.4468 | -46.1211 | 2026-05-16 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| fa2c7f0c-c7d2-37f9-952c-ea0f3c6f996d | -9.4472 | -46.0985 | 2026-05-16 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b859396d-8a83-3643-93d7-f77bf7fcd2c5 | -9.4472 | -46.0985 | 2026-05-16 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c9b3eb2e-2f22-3faf-8777-70f7fdb8f3ca | -9.4468 | -46.1211 | 2026-05-16 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| eae9af6c-894d-3811-80d1-6ef140b13d22 | -9.2317 | -46.6607 | 2026-05-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 80f36b3c-3396-3902-b2ea-90f57dd767b8 | -9.4468 | -46.1211 | 2026-05-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| f94375ba-0616-34ca-ba81-94597d78f714 | -9.4472 | -46.0985 | 2026-05-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b5344cc8-c938-32c0-bd2f-f86e0c490dec | -9.4472 | -46.0985 | 2026-05-16 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 9981d9e2-265b-33d7-9b04-c50c2091eba7 | -9.4468 | -46.1211 | 2026-05-16 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| e0a70cd2-0450-3ddc-8d3b-40d7747b2869 | -9.4472 | -46.0985 | 2026-05-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 36482c1c-e351-36cf-897f-29000fb96d86 | -9.4468 | -46.1211 | 2026-05-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| e75c5685-6323-3275-adf9-aa1b473d76ed | -9.4468 | -46.1211 | 2026-05-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 2087fe37-1fe5-3fec-8a07-cdf65d69e7e7 | -9.4472 | -46.0985 | 2026-05-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 800f78a1-f7c7-3a73-91c6-4c7d173daa4d | -9.4472 | -46.0985 | 2026-05-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |


[Clique aqui para ver as próximas entradas](README6.md)
