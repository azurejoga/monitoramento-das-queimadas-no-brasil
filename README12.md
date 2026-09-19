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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c00bcd3-9fcb-3386-a786-884720030dc6 | -11.98247 | -52.4699 | 2026-09-19 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 37d50754-9164-3a08-bc6f-a5d6bd258951 | -15.58673 | -56.53791 | 2026-09-19 00:39:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| dc6c5124-1745-3772-854a-c2f772f7e048 | -11.94153 | -50.11452 | 2026-09-19 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 42cabb9d-a139-3e8b-b1ea-1dfef499be4b | -14.6861 | -46.6657 | 2026-09-19 00:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ca924627-6b21-3025-8509-de846e14da1e | -10.6926 | -60.7516 | 2026-09-19 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3e929479-966a-3fc1-901f-43592dc68b01 | -10.9301 | -53.9618 | 2026-09-19 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0de17c49-4451-3950-96f1-0763c0a0030c | -10.7115 | -60.7312 | 2026-09-19 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 9ec1b84f-aedb-3dc4-a3df-d571ea770479 | -5.5062 | -43.7966 | 2026-09-19 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 7353b9ec-3bdf-3d25-aaf7-0c0ae6f410a5 | -4.5774 | -42.9512 | 2026-09-19 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 05e0e58a-a8c6-3d24-8899-c08a80d555f6 | -5.5251 | -43.7721 | 2026-09-19 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 17c844bc-21eb-3b0e-8dc4-00f7df063363 | -7.6386 | -46.103 | 2026-09-19 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| bf7e45ca-7cfc-368b-843b-1adc6da3fc06 | -4.596 | -42.9734 | 2026-09-19 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6b474932-8bd5-3160-bac0-24f070f7b6fe | -7.6574 | -46.1013 | 2026-09-19 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5222ea61-a42a-39c5-854b-3025321ebef7 | -3.3311 | -59.8101 | 2026-09-19 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1d01f42a-8fde-3c8c-a7fd-56021694c3d1 | -5.5249 | -43.7953 | 2026-09-19 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| bd879d84-8e06-3128-b79a-0d82387017b0 | -10.867 | -56.1975 | 2026-09-19 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1acd4a69-0ce0-3f15-949a-d5da742bfec9 | -4.5961 | -42.95 | 2026-09-19 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 3eaca318-1da0-3a24-94c6-a1fecfcd90f7 | -2.8286 | -50.4444 | 2026-09-19 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0f9aa380-d4e4-3f21-9c45-e15767874ba6 | -10.6928 | -60.7322 | 2026-09-19 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c891f494-444b-3a43-b17c-3a4a62f7e490 | -4.5772 | -42.9746 | 2026-09-19 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 7d3e457c-df8c-318c-991a-9c14f1afc198 | -2.8284 | -50.4863 | 2026-09-19 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 47a4fdf7-09b2-3c7e-8289-43451610171a | -2.8285 | -50.4653 | 2026-09-19 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 57f1cc65-ba66-3e76-98ad-d0cacf2482ec | -3.3638 | -50.4492 | 2026-09-19 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d0e02a79-61a1-3af0-b6b1-778146f010e3 | -10.7114 | -60.7505 | 2026-09-19 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e2be74ed-b405-312a-99a5-74eef96c8f2c | -5.5064 | -43.7735 | 2026-09-19 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2b406135-e502-35c4-bac8-c028ca6ddaa2 | -2.8101 | -50.4658 | 2026-09-19 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1c88ec7f-2ee4-3e32-9558-0f8933846aa9 | -8.4983 | -57.6271 | 2026-09-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 38e22123-c890-32a6-b27f-d067706ec4ae | -16.7962 | -46.978298 | 2026-09-19 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a844167-a448-35a1-9b1f-fb638c3ceec6 | -8.3607 | -47.222801 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44593bd5-1e0e-369d-98cf-48b6bae0e28b | -12.3512 | -48.2015 | 2026-09-19 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 075972b1-0d78-3aef-9a7d-3c8c43b880d6 | -10.8614 | -54.105 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0b110cd-2804-3387-94ba-58ce466052ba | -7.6447 | -46.106998 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17150e0b-c7b3-30bc-8802-ca07d34c06d6 | -3.3583 | -50.451302 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fdcf242-7cae-3598-b9bd-4262919a4297 | -6.4874 | -43.8111 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5b1473-4710-3094-a9f2-edc4c3dc75b0 | -13.641 | -46.9347 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efecc407-9930-3fc9-a8c1-984279d69860 | -11.8328 | -46.836498 | 2026-09-19 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd5d4cd-b593-3bce-ba25-014dc2a9ac7c | -11.1284 | -49.039902 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e64cf053-a864-341c-86cf-8fad00583352 | -10.2397 | -48.8452 | 2026-09-19 00:41:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce82d94-2d3f-3ead-b2d6-cac5a06f615f | -13.8708 | -48.595001 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d709d8b-dc47-3073-b89b-07a5dcd61bb3 | -10.5317 | -46.747002 | 2026-09-19 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 569988ac-4a69-34cc-922e-6e74d11f49f3 | -11.2969 | -51.722698 | 2026-09-19 00:41:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 149dfd4d-6fa0-3206-a334-75f4c09f7736 | -15.0254 | -48.558498 | 2026-09-19 00:41:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71690b8f-0958-3433-b9ad-ebe02ec0aa63 | -1.2231 | -47.7234 | 2026-09-19 00:41:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc039f8-e51e-3d5a-8dbd-86f0de4d8a39 | -5.3342 | -48.994701 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f5d5bee-e77a-35e1-beed-719153640416 | -6.1891 | -47.516701 | 2026-09-19 00:41:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af58fa91-2230-3f29-a554-83f663505858 | -8.4378 | -45.7486 | 2026-09-19 00:41:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf2a6bc2-e0e6-34eb-8733-ba573f443159 | -7.5727 | -57.686001 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6869ff20-2118-333d-b38f-e9561fae81cf | -8.7751 | -46.9188 | 2026-09-19 00:41:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f839ea6-c2ac-3249-94f0-831aee40a944 | -6.005 | -49.1749 | 2026-09-19 00:41:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac6997b-693b-3ce3-b5f4-22439717c89e | -5.9116 | -46.331402 | 2026-09-19 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2969f006-8266-31b0-a7c2-4c791a229638 | -10.8336 | -50.911701 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 213f4fbe-d911-38fd-8d99-a0518e944497 | -14.1316 | -45.178699 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e25e5206-67da-3c17-b03e-d120ec054104 | -11.0627 | -49.759499 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c60dd563-827a-3f06-a588-02e3f4563192 | -8.4808 | -57.617298 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e63745c8-5f9f-3936-99b8-9d23cebd2f29 | -3.4548 | -50.6026 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4544b22f-cf58-35fe-87e2-e93bdbae492d | -9.752 | -45.062801 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55161866-9aa1-3959-9a66-319e14c103ba | -7.1913 | -47.876598 | 2026-09-19 00:41:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f71148a5-f8f4-3529-b9f8-8e3d7117e389 | -6.141 | -51.724499 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84987217-eacf-379b-8a4d-0763ed132af5 | -2.6255 | -49.104301 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd400fa0-ea8d-3015-884f-70a94dc3e5cf | -1.6718 | -54.930099 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd368a5-d06a-3f24-86fa-ecd6106eb3dd | -12.127 | -46.992699 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbee1d9-6df4-32b3-ad9c-a4fe0cbe9dd4 | -13.3842 | -48.029701 | 2026-09-19 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08a18f0d-bd62-35ba-ae83-e888a140b3ea | -3.7412 | -51.4049 | 2026-09-19 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a93bc9-2078-3425-a1ae-2ff399862e30 | -10.606 | -46.093601 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c912cc8-5a99-39fb-80c0-363e88350dc7 | -8.7656 | -48.6647 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed30645-c26f-3d80-80c9-2c6c13c180dd | -7.224 | -49.635601 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eeef011-6368-333f-96cf-efd496abdc4d | -11.9122 | -50.114101 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ca81449-3062-38d8-a699-ce9f8efb9ec9 | -1.6003 | -54.436501 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec5c92c-fbc3-31b6-969b-c902e76b660a | -10.0974 | -45.645802 | 2026-09-19 00:41:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fec5d512-50aa-32d8-a616-a78429158d05 | -12.701 | -45.952 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40268e35-e392-3ecf-a6ea-332550797297 | -10.8589 | -54.093102 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2f0092f-a94b-32b6-8c18-3721a62262d8 | -4.3727 | -55.255001 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2073ac1-5e1b-3c9c-9a1e-39dcb77dd878 | -6.017 | -51.767899 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f774ab-6136-3fe9-a567-a500280ac537 | -14.6705 | -46.653198 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 17a34298-0988-350e-8cc6-00f6f33ff8ff | -1.6391 | -55.147301 | 2026-09-19 00:41:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f67aef-e414-3c87-9633-6f2839a93175 | -7.405 | -49.842201 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a68a7354-da51-3514-b296-0d044bffe17b | -1.5786 | -54.431599 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35146f57-8de4-3cf6-b3dc-d3bb78b9d0a6 | -12.1368 | -46.990398 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d47700e-735f-3aba-86ed-7829fb9d3995 | -9.5605 | -45.473301 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b06a6e79-4172-3aef-891d-12b07e732f29 | -2.8262 | -50.469601 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3399a04-9063-3e5c-a1b4-0aef4022f983 | -10.4568 | -51.254501 | 2026-09-19 00:41:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb848ba4-953a-36c1-b014-770b8126cfdb | -14.6868 | -46.679298 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5059a1bc-95a2-3872-9469-f13d05988266 | -12.1335 | -47.021099 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5eff920-f725-34fd-b5ca-9bfa8adc7b46 | -12.5813 | -49.091599 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15cd6fe8-2379-3da4-8c22-ac3b116de1a3 | -11.305 | -46.786598 | 2026-09-19 00:41:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56f8baa0-ab85-32a2-9000-cb866edd89ce | -12.3496 | -48.1945 | 2026-09-19 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b84dc78a-eef2-331b-84e1-319ae00be442 | -14.7971 | -48.549702 | 2026-09-19 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e59879dd-551a-35f6-a11a-0b8e32183c0a | -11.0578 | -49.737701 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89fa8e67-d1e8-399a-91f2-3e4965cfbc39 | -12.2873 | -49.1581 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c4b88b4-639c-3840-bf66-65e5bab44f3b | -5.8917 | -53.553799 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de13124-3679-36e7-afe6-09be5d8a0d95 | -10.8612 | -56.178799 | 2026-09-19 00:41:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 474b71ea-cda6-3224-81c1-0d3de1bfd391 | -11.069 | -48.320301 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 314335d2-bc59-343c-b35c-3da89b9bb909 | -14.6607 | -46.655602 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee576e8c-4630-3d22-b0ad-b0c0f2a187d8 | -12.502 | -50.0387 | 2026-09-19 00:41:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe0b686-09da-32e6-82cb-6497e284860d | -5.8504 | -51.942001 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227785b3-2601-3d61-a738-cf212e440cd7 | -9.6092 | -45.3741 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd839d7a-4178-3c8f-9f6c-3c1e9740ca32 | -6.9967 | -42.178398 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3371aca8-7f85-3e97-be4d-6f07f4f1429b | -9.9358 | -45.313499 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbbea17b-4e14-3239-a645-e2faaeb66dc3 | -7.78 | -44.894501 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9931fc80-9a1c-3949-a819-f6bd29c83153 | -11.0205 | -54.1343 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
