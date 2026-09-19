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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bad6456-1aff-3fcd-8964-3f61e80931bf | -10.7133 | -50.258 | 2026-09-19 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| eb1a5596-6f28-3926-9672-b7e3e614f3c4 | -11.4354 | -51.4563 | 2026-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 02476d03-c61c-365f-8225-83293047dda2 | -11.8934 | -47.6322 | 2026-09-19 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 65d10ff8-a824-35db-b38d-f1e662ae696e | -9.8066 | -46.1023 | 2026-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5cbedf67-2442-3544-a0e5-36052bb4128c | -11.8746 | -47.6125 | 2026-09-19 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7ddec0f3-5225-30e6-a21a-6b7ec8c141b4 | -6.2773 | -41.66 | 2026-09-19 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 20b8d4be-81df-3a5d-be2a-cec211e7198a | -3.3493 | -59.8288 | 2026-09-19 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 11af12e2-d717-35d0-803a-10bdd9b7445c | -11.8746 | -47.6125 | 2026-09-19 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1f046991-bca7-33d8-9179-299b5f9e8f23 | -12.0267 | -50.0231 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 3d719579-f09e-3caa-b240-1e8dc1afa90f | -8.4503 | -45.8448 | 2026-09-19 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2de1cafc-2d70-3b7a-8059-024fe7ed8f9c | -10.567 | -51.3137 | 2026-09-19 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 8037547f-17d5-3af0-bbc0-e65322a76a1e | -12.5952 | -49.1046 | 2026-09-19 13:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 563.0 |
| 13b26f9b-42e6-38ad-b6da-33d93d29bab2 | -11.1035 | -49.4623 | 2026-09-19 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 54f4a2e6-3582-3a4c-a526-1711b082db97 | -12.6037 | -50.9405 | 2026-09-19 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1c80a418-3aa0-3be2-b0dd-be972c08926f | -12.7089 | -45.937 | 2026-09-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2036b859-5e63-34c0-b156-5db5d35c818d | -11.318 | -51.7218 | 2026-09-19 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 674bf576-210b-3c32-8e7b-0c045d809bbe | -9.2567 | -46.2098 | 2026-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| e00914c2-8044-3517-b171-79bbb2f93266 | -11.4354 | -51.4563 | 2026-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 034dbc3a-f33c-39e2-a159-a9ceba2b0984 | -2.8974 | -57.7987 | 2026-09-19 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 270.8 |
| 03a5c298-00f5-37c8-8fe9-949df92fd210 | -7.6087 | -45.4298 | 2026-09-19 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| d001c9cf-74d1-3d61-8354-795bacdc294a | -11.3604 | -44.1521 | 2026-09-19 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| fb5068c0-991e-3f8c-b349-711006a4d363 | -11.836 | -47.6398 | 2026-09-19 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 124df7c5-0c54-33eb-8228-97dfddefe4bd | -6.2585 | -41.6617 | 2026-09-19 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 273.7 |
| d6bede87-7072-39cf-8653-c6cc908fca15 | -2.8975 | -57.7793 | 2026-09-19 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a9890968-8060-3eed-8a5e-c27b7218191d | -2.8791 | -57.799 | 2026-09-19 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 785f657b-1312-3111-8514-9d7c7c519607 | -12.2688 | -49.1907 | 2026-09-19 13:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 12948f91-be52-35f1-b455-371b37a0c5be | -6.001 | -51.7903 | 2026-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 26ada8c0-8971-31f8-aade-00b39fb218a1 | -13.286 | -51.3473 | 2026-09-19 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bc18e0b5-8e8a-32e9-9c7d-a43550327c84 | -12.5949 | -49.1265 | 2026-09-19 13:40:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 8f752c34-e2a3-3133-ae03-26bde1b5906a | -12.2879 | -49.1883 | 2026-09-19 13:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 512a73dc-d981-3217-bf99-0db4fcd4dda3 | -11.0608 | -49.7909 | 2026-09-19 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 6486a82c-cf76-361f-af0e-f9317caf38c0 | -12.0076 | -50.0254 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 997c16b6-4d7f-324a-92da-d7b63ecf1508 | -5.6408 | -43.392 | 2026-09-19 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 18328dac-eb41-3ea5-979e-185b57ba191d | -7.7629 | -46.7389 | 2026-09-19 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 3fc7fb19-5263-3edd-a5f6-1b9c40b3e872 | -11.4673 | -45.7077 | 2026-09-19 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9f6bee3b-d582-3398-9052-d5782ddd65c6 | -11.8742 | -47.6348 | 2026-09-19 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 67c3218c-f495-3642-a95a-05ec16f9d675 | -8.8827 | -45.935 | 2026-09-19 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 2953a5f3-f7e8-3992-9246-0e67f3973ec3 | -17.3184 | -46.6293 | 2026-09-19 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9f521694-d577-3f0f-827f-0386288fe15e | -9.2414 | -45.9411 | 2026-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| c31153ad-72ea-39be-88cb-62d51eead5e2 | -11.1228 | -49.4384 | 2026-09-19 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| fc06e9fe-e13f-3814-a594-b36b01e1f3ee | -12.1531 | -46.9707 | 2026-09-19 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 792873d2-2e0d-3360-a89f-01f20231f2c2 | -10.5667 | -51.3349 | 2026-09-19 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e23a5c44-d2a7-3608-a841-84b55486bce5 | -12.1336 | -46.9959 | 2026-09-19 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5c5085d2-a058-3f45-b596-a9a3761d6430 | -8.4983 | -57.6271 | 2026-09-19 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 727cccac-08e9-3732-88fd-9c85252a9412 | -3.7129 | -60.6022 | 2026-09-19 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| de7be495-e8d7-38e1-84e6-ff0587494b67 | -8.45 | -45.8674 | 2026-09-19 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 204.8 |
| c5ae1a1e-1802-30f8-af4f-6bec7a28f1bf | -10.8282 | -50.1601 | 2026-09-19 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6701aa6f-bdc6-332a-9beb-c556f4d04a5e | -11.234 | -48.3571 | 2026-09-19 13:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 111a6d4e-9aa6-3a3d-83b3-aa80e4afd028 | -11.3355 | -43.403 | 2026-09-19 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7ec39440-f726-39c6-8a0c-c3bb0c5136c5 | -6.941 | -55.0366 | 2026-09-19 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 06bfc641-aa3c-3cdc-82ea-8db119f69e86 | -2.8974 | -57.8181 | 2026-09-19 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 635e8a45-f6ad-301f-bba4-56f8505b130d | -8.7731 | -48.6868 | 2026-09-19 13:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 215.1 |
| ed417901-6508-3283-9d9a-d27252fb9e56 | -11.1369 | -54.0251 | 2026-09-19 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 526.9 |
| db68d48d-3c87-3f2e-beaa-778b80037ece | -2.9157 | -57.7983 | 2026-09-19 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 179.1 |
| ec2d2dea-1568-3ef0-a30f-6a40b65fcae3 | -9.0358 | -48.727 | 2026-09-19 13:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 94.9 |
| f086bed7-add2-380c-8d89-5ca30ff64f2d | -11.8546 | -50.0653 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| fb7a28a5-9970-33c8-95ad-da872a6fbc15 | -12.0082 | -49.9822 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 2fa7a2be-0799-3683-8306-d7c270232b0b | -8.7919 | -48.6851 | 2026-09-19 13:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 233.7 |
| 05a5b932-38b5-3906-bf17-57694603dd12 | -8.8639 | -45.937 | 2026-09-19 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 99582b80-8771-3477-b996-248b4fe678b1 | -8.4314 | -45.8467 | 2026-09-19 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cc74579c-8ae0-34f4-b013-7bcff542ed4a | -13.2222 | -51.7382 | 2026-09-19 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ba273b20-d08d-3d35-82b3-c653bd1dadaf | -10.9133 | -50.8549 | 2026-09-19 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| c0ea0b41-972b-3c73-87df-a879e49f0ae4 | -11.083 | -48.2875 | 2026-09-19 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c72712aa-9eee-33e5-b044-d0e66880bee4 | -13.2414 | -51.7359 | 2026-09-19 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 47cbc043-0c9e-3251-88d1-3585cad5bc3e | -10.8279 | -50.1815 | 2026-09-19 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 7af77d7c-5a76-360f-b2ed-30c0900c26e8 | -8.9412 | -44.3995 | 2026-09-19 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 9bae21e8-7928-3808-b639-9932ecd54b09 | -3.3494 | -59.8097 | 2026-09-19 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a764d48f-e8e5-31c5-b525-c7f5144ae2a7 | -7.4479 | -44.6934 | 2026-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 25398204-a0cc-333d-a800-8829f7eee6eb | -10.5368 | -46.7343 | 2026-09-19 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d845b9f3-8a75-3194-b8a5-4c35961613a0 | -11.3166 | -42.3313 | 2026-09-19 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 106.6 |
| f5621c06-6b2f-3393-b3b2-8493083f3866 | -10.8469 | -50.1795 | 2026-09-19 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 9594e5a2-8e54-3fc9-b7d4-e9a2c0744049 | -12.5032 | -50.0508 | 2026-09-19 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 9687aed2-3c95-3dc6-b3bc-81e88b3731ed | -10.8466 | -50.2009 | 2026-09-19 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 4bb488ea-6111-3f76-ac9e-d56b19e0fc1c | -3.7128 | -60.6211 | 2026-09-19 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b6f847e5-6bf7-369b-a9de-9ebb74e6f9de | -7.0448 | -42.0906 | 2026-09-19 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 241.8 |
| f02ae4bf-b82e-3f44-bb2e-f13cd0f24b0c | -3.3311 | -59.8101 | 2026-09-19 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 3f505aa8-7d63-3c93-b801-c749710d40ae | -11.0611 | -49.7693 | 2026-09-19 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| f238428d-497a-3dfe-bc0c-b086a174871d | -3.331 | -59.8292 | 2026-09-19 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| b6ea58af-6d07-384e-b82a-a3161074d91c | -9.0096 | -44.9209 | 2026-09-19 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 7756286b-4f47-3d98-92ee-30caf51984a2 | -8.4296 | -54.7262 | 2026-09-19 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0522e59f-b6ea-312f-b9a8-eedd31bab65b | -10.6703 | -50.6465 | 2026-09-19 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 18fe7393-4ac3-3ed4-a889-16e39fd64bfc | -11.7823 | -49.8152 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1ef4ceaa-fd7d-3e1a-9d44-659a20a12d7b | -5.6596 | -43.3906 | 2026-09-19 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 427121c5-e3b4-32d2-9fb7-7b9b5d55217d | -7.8598 | -44.8595 | 2026-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 178.1 |
| c78698b5-5906-35ac-97a7-9fd5684b2f83 | -12.1535 | -46.9482 | 2026-09-19 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 357085e8-1d92-39d9-ad4e-fe128068a6e6 | -12.7085 | -45.96 | 2026-09-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 091e624e-5021-36bf-88e2-5cfd842ddffa | -12.604 | -50.9191 | 2026-09-19 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 66652543-848a-3d72-8836-a24c4b56cfd4 | -12.5761 | -49.1071 | 2026-09-19 13:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| eeca9834-7dd9-30c0-98d9-a2bc94679278 | -8.411 | -54.7274 | 2026-09-19 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 133d7157-e6c4-3eb1-a816-20b9f9496089 | -11.8549 | -50.0437 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c61497c3-be47-3ecb-8ea0-ec89c500d20f | -7.0029 | -49.7551 | 2026-09-19 13:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 25b297e1-6c2a-38d6-8d7e-f59e5dca00ec | -12.1339 | -46.9734 | 2026-09-19 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 1f1908e6-3772-3ea4-9ebf-dfa84b0f9804 | -3.6946 | -60.6025 | 2026-09-19 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 18ff5405-c680-3190-b4af-3dd920a5c6f4 | -7.8595 | -44.8824 | 2026-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 25f9f073-124b-32d4-89fa-e97486ceefdc | -12.4841 | -50.0532 | 2026-09-19 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| d968067a-26bd-3970-939c-c2cbfc5e0a00 | -11.8934 | -47.6322 | 2026-09-19 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 07a1ee10-ac14-3f72-9703-9d93f3890d3f | -3.4455 | -58.2134 | 2026-09-19 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b9148016-ed59-3ce4-bfa9-53bf915bed63 | -5.9344 | -42.0966 | 2026-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| e53480e7-94d2-3670-b728-dd37c4f1158e | -12.0273 | -49.9799 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6e9e1367-39af-3cd6-a568-5e91ad3b8d58 | -6.2582 | -41.6858 | 2026-09-19 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 235.9 |


[Clique aqui para ver as próximas entradas](README111.md)
