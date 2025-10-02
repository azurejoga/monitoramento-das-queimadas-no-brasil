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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2ed6a75-84d4-3309-a11a-ef878fc69385 | -15.21545 | -47.17043 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3bc7e35-2bba-3caa-b30c-3b6985915c82 | -12.69026 | -48.57674 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 652b0805-7695-33ac-b62f-05723d0e0fb0 | -13.32431 | -47.22268 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 766d095a-536b-3140-8023-c418449b39a7 | -11.09731 | -47.8218 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| effa65a5-df56-341e-b50d-27fa7a9722cd | -9.42075 | -47.35546 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 668a6fd9-b412-3147-89da-ad4428ce1139 | -11.46972 | -44.97858 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7540303-23fc-3b0a-9414-38eda4a174ed | -15.23662 | -46.96298 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e959e4e-0381-3a49-a9e9-8091b140991a | -13.06672 | -47.0207 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b81a692b-b176-3728-8adf-adde6e507e99 | -13.80186 | -47.52994 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af21b2dc-f3d9-3afe-85fb-4a4f30f472e7 | -14.42574 | -46.11134 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ced19bfa-f5c4-37d1-81fa-4d12396dfc3b | -13.30209 | -47.85117 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f533e29-7be2-3cf9-9f58-87ae3d8495ed | -11.01156 | -49.57854 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa33c049-b6fc-3de6-b812-2ff8755fec17 | -15.20784 | -47.9996 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53152040-ac17-3cc2-9593-92b53a1e1e61 | -10.78335 | -45.3502 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2105f079-3fd0-3b3f-851c-ee188422ec03 | -15.17216 | -52.80509 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c921bcc-4261-32ce-861d-6b7f4107ca3a | -12.46361 | -54.32307 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f474683a-8b2d-3471-99f0-bd20385bf34f | -11.17837 | -47.18657 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4341cc18-81f7-3b25-9ad6-13d68874d470 | -13.55035 | -47.28585 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f58ef9f-07ae-3d9c-86ee-97352d953e2e | -12.87089 | -47.01915 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96c90704-23dc-3c01-aed4-aeb3647d5020 | -12.27717 | -45.37406 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92aa8c54-b78d-357e-a6e4-07b667f07f9c | -13.74865 | -48.00631 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70fe4e7a-f5b7-316e-84dc-728d13b16dee | -10.84166 | -46.62069 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f581b7d-30a9-3e16-a876-48023c8c8992 | -12.24658 | -47.8294 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d1d3cc0-1690-3d50-9877-1181fae77c33 | -10.46882 | -62.45492 | 2025-10-02 04:51:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b44918e-6d20-3992-bf90-9158079dbeac | -14.88407 | -48.33284 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6f78650-0a8a-36a8-836b-94d47970b527 | -10.86635 | -46.60972 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52e0316c-dcd4-3b31-b906-d26f426c7db6 | -13.40467 | -44.39024 | 2025-10-02 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e58e360-b7e4-387b-9142-cfebdad5c98b | -9.44827 | -50.90001 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 533e4e4e-4a6d-38cd-8142-6746db939449 | -15.25491 | -49.30881 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 885822f5-cb74-3425-aa73-ebfcb4e3ac21 | -14.42504 | -46.11724 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f6aa148-8e5d-357f-9df2-9de9b8f55ea6 | -13.90897 | -48.07239 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6aeb9f8-2c8f-359c-b91b-1fbe258478eb | -14.31176 | -45.99915 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 37e82b3e-4246-3425-88b8-96c9720de530 | -13.75465 | -48.70427 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13f391dc-ad46-30d2-990b-30fc183ba13c | -11.17334 | -47.19046 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bccd66e5-43c6-37d6-882b-9e073279e900 | -14.28447 | -45.9735 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae240d08-f305-37db-a976-611add007628 | -10.83517 | -45.37927 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87cc2482-55df-3461-bc11-b1dd06703c72 | -10.15695 | -61.94867 | 2025-10-02 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06f0fad-4f8c-3200-b3a6-7396075180d6 | -14.4115 | -46.10382 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bbdd6a6-652f-3f0f-8740-51397dcc4bad | -12.47881 | -47.27087 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9b7fc26-5275-34b2-bca3-93d64c9fc2d5 | -10.21758 | -50.33739 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 374f426b-3782-39bc-a1a8-da98609db61e | -10.2895 | -51.07386 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9011ef86-13c2-36c3-a609-e726d3b39fcc | -14.42232 | -46.14003 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a051e591-a652-394b-8378-b7d47e6e260b | -12.42483 | -45.17018 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63e28256-d279-341e-af80-f103e990e511 | -13.86269 | -51.24851 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cf229b7-c717-3e4b-adc8-59fc418e3755 | -11.15952 | -47.19296 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 019f1c1a-a7b0-306e-b031-c78455ea6b8f | -13.05942 | -47.00507 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37c1bc04-35ff-3c73-a3f0-fce5e358122c | -11.42559 | -43.49978 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8770fafe-6cca-3070-add2-b0450ac09e0f | -9.81276 | -48.26415 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c507ea58-1a34-3533-aff3-f85ce2a707c8 | -13.8003 | -48.0488 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b22af8d-487e-3a44-a7fb-1b2f7f97a538 | -14.59729 | -48.32931 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82e69c31-20df-3db9-b9c5-243fd5e04659 | -13.57464 | -48.19357 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d083071-dc62-395d-b3d6-4fdb1004c10e | -11.15016 | -54.12272 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 629071c7-9d20-3b47-862b-d25f60f304c5 | -11.87167 | -45.01489 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9ad30de5-502d-302a-8d8d-ecf1d51dcf27 | -13.80513 | -47.53957 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 700b0adb-8059-3905-9dbb-c2f372f7f179 | -14.91456 | -47.23026 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba83bfa4-26f0-30b6-876e-1d50ce1c3ae3 | -9.91523 | -47.70965 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a26db3fb-0cf4-32eb-bc3c-0b1c2b6499a4 | -14.70562 | -48.21949 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1e2b7f6-c679-37d9-9d6c-c27a00f2684f | -14.36857 | -45.94994 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 851f5f17-4240-3e18-a5d3-24c190b5be37 | -10.66977 | -48.52306 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e73a62d-3d7f-3ba3-aea9-82203cf59704 | -13.16796 | -47.81938 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62005309-afcd-3da6-8fa5-940ea2ab6f6a | -13.01105 | -45.21181 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6124bedc-052c-384f-ac7d-84f78b7a8dce | -12.70249 | -48.57896 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 10065402-e8a7-336e-b7aa-c38f22f6d16d | -14.70612 | -49.61902 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 6a24a575-bd48-3523-a3be-72360cf7a888 | -11.19326 | -47.75153 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1371b5d-33ed-3d61-bd60-3b52ead5a4df | -12.42151 | -54.35241 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f833ea3e-419f-3bb3-870e-48814a7c1aaf | -11.03783 | -47.8159 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2e069f2-5a85-3efc-9632-681376c2e520 | -9.93199 | -43.77668 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 590f42c3-e5fa-32ae-9d6c-9632f5fb7517 | -14.4793 | -48.44226 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b85c529-2538-3f07-9fa3-cc976218bb19 | -13.07443 | -46.99727 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5474b951-219d-36fe-a384-6b347f2e6c9c | -11.01053 | -46.58011 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 963bac8f-d22f-3276-ad22-c53409ab6df9 | -13.15387 | -47.82561 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f806410-99d6-3695-b06e-36167fdab944 | -12.80613 | -46.90792 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f5de679-c986-30dd-bd9b-00268a975d31 | -14.32883 | -45.98444 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4f99fbd-c374-38a8-b99b-65767292a926 | -11.87403 | -49.91351 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac68f16c-1fe4-3aff-a1b3-891ae6910807 | -14.4163 | -46.13759 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 592ce5b5-6880-3b51-b901-5289097479a7 | -11.87312 | -51.22781 | 2025-10-02 04:51:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 658ce3bd-4c7e-3b60-8c4a-6f09af23a909 | -14.18309 | -46.67092 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c8e9969-b2e9-3634-b6e2-22370e8e2f18 | -12.84162 | -46.9578 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5865d0f2-5160-3fa7-99cb-f985f2beb164 | -11.46661 | -45.01966 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462c8a66-38a5-348b-afd5-d322957cc036 | -13.57834 | -48.19833 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 879d4e62-60b9-3c42-984e-c2fa2f06413d | -11.83075 | -45.00645 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1da5cb0-8cf4-3a00-9fc5-309ed36fa3fa | -9.71237 | -48.95325 | 2025-10-02 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c92334a-0624-3ac2-9feb-2ed23bfa6edb | -11.58673 | -47.64411 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dd423eb-5211-3fe1-855c-26b0c3f64d41 | -11.59933 | -47.22294 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcf08df8-7a84-3609-a7be-c482f7b47add | -11.45746 | -44.96705 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 912e963e-6455-3aff-ab6e-9430f68a95ca | -10.9994 | -46.59337 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0e9f45e1-495e-3db8-b5c2-5b0e4b8d097d | -11.91179 | -47.88399 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5f904972-d591-37c9-a3c9-5532b30579fd | -12.7066 | -48.57955 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b9e106a7-232a-3172-8535-ac9aa0cd7adf | -13.81152 | -47.54792 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c1cd7b81-5a37-35a8-9383-9fe47f20f3d1 | -13.24518 | -47.33422 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ce2591d-17be-3888-ab60-7793a3072b8b | -13.16606 | -47.83376 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10d665de-7b15-36a0-ab53-960bd0371c95 | -14.22361 | -46.09945 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0d3b55e-14ff-374b-8931-42020019aa5c | -10.77129 | -45.3655 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d93d526f-5e01-3f18-b660-a3318de04c07 | -11.00399 | -46.59389 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e92758c-2f37-3be5-a343-a3c59e26a03a | -12.40112 | -51.0772 | 2025-10-02 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398b247d-a61a-323f-85b7-564ae6f06174 | -14.614 | -48.23405 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 467ee6ad-fc73-3b15-a081-2d18aacf45b7 | -13.5087 | -48.20518 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4159e17a-5d9a-3782-8dd2-ee36f5a1a492 | -14.10635 | -45.64173 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba40ec2d-d66c-3308-8d51-c5e9e7f46c5c | -12.575 | -49.902 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a795d01-4213-3c9c-a635-a3124c7ce45a | -15.22894 | -48.72939 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README117.md)
