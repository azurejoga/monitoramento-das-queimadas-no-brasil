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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7e0aaba-fdda-3a16-9225-fa4d36e5841b | -12.1478 | -50.0527 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca0619c-d8fc-30a9-97ac-9fab2172fa30 | -12.5442 | -53.103298 | 2024-10-02 00:31:09 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b141b1fd-cb64-3e34-abfc-0088335f9ab7 | -12.547 | -53.117298 | 2024-10-02 00:31:09 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22488148-da69-3107-b084-e8bb4b6fbfdc | -10.655 | -44.487598 | 2024-10-02 00:31:10 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc896fa-3e98-33a5-b56f-656fb05f5e4a | -10.6567 | -44.495201 | 2024-10-02 00:31:10 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73a2897a-8435-3a5f-8109-4577414e191d | -11.0109 | -46.508598 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fadc5a0f-6527-3070-8854-0894ee44676c | -11.0124 | -46.515598 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc4c0f18-487e-3e4b-8f94-07f220ad9aaa | -10.9908 | -46.556999 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a986b8e-fa17-3d95-945d-746f781ae2f8 | -10.9794 | -46.552299 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9dba0f8-536f-3557-a768-b3fe34207da5 | -10.981 | -46.5592 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd27b0b1-4c85-39d8-b34c-1bbfc4d9abdf | -10.9825 | -46.5662 | 2024-10-02 00:31:12 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f501a880-66bf-396e-9d4e-e766b5a8dead | -10.9101 | -46.3344 | 2024-10-02 00:31:13 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7ecdef7-f553-3efa-b393-fa34a3b7e863 | -10.9148 | -46.355202 | 2024-10-02 00:31:13 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48baeab9-f7c6-3bee-8142-da18dd6e43cd | -10.9163 | -46.362202 | 2024-10-02 00:31:13 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 232ad2a1-9d95-3e76-ab61-adb5ffd58386 | -9.4618 | -40.381699 | 2024-10-02 00:31:14 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f69213e6-643c-3e89-a769-0ad2b0e07210 | -11.2753 | -48.411301 | 2024-10-02 00:31:14 | METOP-B | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 264dd0b4-e295-3afd-be9e-d0d39030e6fa | -10.7064 | -46.1614 | 2024-10-02 00:31:15 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e699d5ff-ac65-315c-9704-1d239ca99ab1 | -10.695 | -46.1567 | 2024-10-02 00:31:16 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d36f01f8-0d5f-3870-ac21-1223d4f68cf4 | -10.9449 | -47.277199 | 2024-10-02 00:31:16 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db42a92f-f603-3e1c-9eb9-5597b84b7fde | -12.3282 | -54.067699 | 2024-10-02 00:31:16 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b065210-f830-3b90-8e38-d8001ede1eb3 | -12.3314 | -54.0839 | 2024-10-02 00:31:16 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13be7d0c-f750-39d6-b464-c7c90d396ff4 | -10.1193 | -43.912701 | 2024-10-02 00:31:17 | METOP-B | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d4571f8-bbb1-3092-a2fe-3dcda829575f | -10.1212 | -43.920799 | 2024-10-02 00:31:17 | METOP-B | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5487c3d-7a85-32fe-a5c4-49ab5598be27 | -9.9205 | -44.078201 | 2024-10-02 00:31:20 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d4ac918-ffce-384e-8a74-c1702ff95e7c | -11.1692 | -49.589199 | 2024-10-02 00:31:20 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff7b69ec-f49d-3991-a1c0-1ce3e700cc81 | -11.171 | -49.5975 | 2024-10-02 00:31:20 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea8c7934-d3f8-3f03-ac81-a3fb16a0a9e4 | -10.7222 | -47.667198 | 2024-10-02 00:31:21 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c53ae18-f988-3d6a-96b8-001b74688b85 | -10.7238 | -47.674301 | 2024-10-02 00:31:21 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e723ae8f-7dc2-3fac-a898-97bd6d4b9b4a | -10.7124 | -47.669399 | 2024-10-02 00:31:21 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0c3e8c3-f9a2-3bef-923c-530195e48efa | -11.1087 | -49.5937 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4903c503-7a1d-3f6e-876d-1ebf547c5801 | -11.1104 | -49.601898 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e13ac338-223b-3849-9e20-76113fd8f90d | -11.0953 | -49.5793 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1953a2-060b-3f9a-b41a-be1141758042 | -11.0971 | -49.587502 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 856b59de-d6f5-36a6-91a1-fa44e9d4c852 | -11.0989 | -49.595798 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4460397-e459-3992-a389-09cc74ffc79b | -11.1006 | -49.604 | 2024-10-02 00:31:21 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a06c289d-1911-38cf-b2cc-ba1f86f4f87d | -10.7374 | -47.9706 | 2024-10-02 00:31:21 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6148eb-13cd-33d2-a4d3-b268888f84da | -10.59 | -48.048698 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc276af-f59a-30e4-8a21-b67e0714ac03 | -10.5916 | -48.055901 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5559fd9f-19ae-37ad-92f0-13f56cae0c7d | -10.5724 | -48.0149 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6e11c07-c0c1-30e1-9d2b-a10ca31960f9 | -10.5739 | -48.022099 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc55254d-a4a4-3c74-bdf5-64272d5aa109 | -10.7229 | -48.7057 | 2024-10-02 00:31:24 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5bbda0-0286-3e48-9685-bcafbc8b4e45 | -10.5626 | -48.016998 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0fdc59-74de-367f-8fbc-b7fc0a6c7340 | -10.5641 | -48.0242 | 2024-10-02 00:31:24 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a926b8ea-c9b7-3c96-a2eb-f3c539e51d77 | -10.5528 | -48.019199 | 2024-10-02 00:31:25 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce81cde9-3257-325b-a9da-1bcab3913264 | -10.5543 | -48.026402 | 2024-10-02 00:31:25 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 750f507e-e948-382a-9d4b-3bf157a7604b | -10.5559 | -48.0336 | 2024-10-02 00:31:25 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1fd1ec4-e588-371c-8b58-2cb3e8719538 | -10.7033 | -48.709999 | 2024-10-02 00:31:25 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b77ab706-8df9-3199-bf7d-f6449e7cc521 | -10.7049 | -48.717499 | 2024-10-02 00:31:25 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0426b88b-dc68-3563-a686-7e095637ae03 | -10.1215 | -46.3097 | 2024-10-02 00:31:25 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a935853-a79d-3d61-8140-0f73bb37ffe4 | -10.1231 | -46.316601 | 2024-10-02 00:31:25 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36ad8ca2-4408-3b75-bac3-8f3acf8ce1ce | -10.9181 | -50.095001 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7ba487a-bb99-3f49-ad99-194b8efff170 | -10.9199 | -50.103699 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96a59c6d-23f7-3123-958b-9a3829cb68d1 | -10.9217 | -50.1124 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce0cc145-091c-3d7a-8971-f5008a1a8855 | -10.1974 | -46.831699 | 2024-10-02 00:31:26 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc2fdd85-f069-35b7-a933-9d7472848544 | -10.9046 | -50.0797 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9e3dba5-8f97-3ab3-8c5e-ee056284e159 | -10.9101 | -50.105801 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ff75123-c35a-35b5-b3cc-a0536fb3703e | -10.9119 | -50.114498 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d092f3d-22ff-3958-945c-02e86dd4764b | -10.9138 | -50.123199 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2501ea79-6383-373c-9171-c05b9303c0fc | -10.8948 | -50.081799 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a3888ae-a106-362f-8a69-17621173f86c | -10.8966 | -50.0905 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00ccbe36-fed0-3aaf-a7ac-2b5e2852322d | -10.9021 | -50.1166 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f0fe048-2f5a-31d8-ba81-44df69fd4bed | -10.904 | -50.125301 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb434a1-4ccb-3cf9-b3b3-f835085fdd45 | -10.9058 | -50.133999 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de78a4dd-58a2-35c0-b2f8-259b1b6f7eee | -10.3138 | -47.4482 | 2024-10-02 00:31:26 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6a45175-302d-3651-983e-74f14c27cf5a | -10.3154 | -47.4552 | 2024-10-02 00:31:26 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c16a8ce1-821c-329d-9fe5-ade228cc627c | -10.8942 | -50.127399 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac637027-fcf8-32c2-a62e-6fec711412c7 | -10.896 | -50.136101 | 2024-10-02 00:31:26 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 374264c7-0f8b-3104-8a48-a2252c2f17b7 | -8.6311 | -40.273102 | 2024-10-02 00:31:27 | METOP-B | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6f69a1d8-7411-362a-91a8-39de7df869eb | -8.6214 | -40.275501 | 2024-10-02 00:31:27 | METOP-B | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 94fb4472-c9c6-30dd-8566-8ff99e6b312e | -8.6248 | -40.289299 | 2024-10-02 00:31:27 | METOP-B | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 8253efcb-15ec-3f22-b073-0e8e1576b540 | -10.4667 | -48.189602 | 2024-10-02 00:31:27 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1233366-754e-3fc7-aeea-6f45a97ea387 | -10.4553 | -48.184601 | 2024-10-02 00:31:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e799201-eca4-3b15-911e-db86896c12bc | -10.4569 | -48.191799 | 2024-10-02 00:31:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d31f0ed1-b3e8-3d0c-b336-d0c773fdac8f | -10.455 | -48.230202 | 2024-10-02 00:31:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b667b74d-0c67-3dd3-b306-d3c9eb6f5e1e | -10.4566 | -48.237499 | 2024-10-02 00:31:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1030045-e288-3e43-bb47-f14502289fb4 | -10.4294 | -48.16 | 2024-10-02 00:31:27 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18c7f347-dc59-3f34-a36a-9d766073e8bd | -10.4421 | -48.217899 | 2024-10-02 00:31:27 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a92dfe2-4d66-3e7f-819c-06722e5cfbf7 | -9.1473 | -43.155701 | 2024-10-02 00:31:29 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de3fd1fe-62b9-3f24-9dbc-5c8a53e74ec0 | -10.2201 | -47.675499 | 2024-10-02 00:31:29 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df7d73d3-91cd-3ec4-8804-e3f80c532a69 | -10.5135 | -49.782902 | 2024-10-02 00:31:31 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77648118-7c61-39b8-987d-3c9bb07f3aa9 | -11.0826 | -52.506901 | 2024-10-02 00:31:31 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba719151-f1a2-379e-b341-fb435fe6c0be | -11.0703 | -52.496799 | 2024-10-02 00:31:32 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4caacc69-5278-3432-96f4-8148ccc1a659 | -11.0728 | -52.5089 | 2024-10-02 00:31:32 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5d0d4ee-bb58-3a8d-b622-8311ce701095 | -11.4285 | -54.280102 | 2024-10-02 00:31:32 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90dfc525-adde-39fb-9ca2-3f9285a784ca | -10.0122 | -48.8381 | 2024-10-02 00:31:36 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53ac2031-4a84-3a8d-b4a7-f7b91f4d578e | -10.0138 | -48.8456 | 2024-10-02 00:31:36 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29f1cf4a-0483-3090-b47c-1bf216e85b05 | -10.004 | -48.847801 | 2024-10-02 00:31:36 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea65c6d-e6db-3ce7-b7ba-9ea2f4210b97 | -8.422 | -41.9249 | 2024-10-02 00:31:36 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 12f69557-acaa-32a1-a59b-a7f2e2d36ca0 | -8.4246 | -41.935799 | 2024-10-02 00:31:36 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 089cb51a-e33c-302f-894d-95e89b72ba85 | -11.358 | -55.1572 | 2024-10-02 00:31:36 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a20c8f2b-8cea-3b71-a4eb-a83577f7a7a9 | -11.3616 | -55.1758 | 2024-10-02 00:31:36 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7cc3ffc-f0b8-32ba-a9bd-30578724e597 | -10.5199 | -51.069901 | 2024-10-02 00:31:36 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbfdd0ae-1c1c-31dd-9758-b837d9b1d27a | -10.5219 | -51.079601 | 2024-10-02 00:31:36 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95b3e9fc-11d4-3182-bcd3-b20fe702e397 | -10.5121 | -51.0816 | 2024-10-02 00:31:36 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84cc025a-62cc-38f3-a801-d9c832127dc3 | -10.4403 | -50.788898 | 2024-10-02 00:31:36 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d2d3711-68bb-3351-a51c-8444c729a557 | -11.4929 | -56.746899 | 2024-10-02 00:31:38 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9816a685-8cd8-3bc0-b66f-9517abee321b | -11.4832 | -56.748699 | 2024-10-02 00:31:39 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 500945c3-23fe-30f5-b1bf-5bf3ad435e8b | -11.4878 | -56.7728 | 2024-10-02 00:31:39 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90e89db9-b876-3ec6-b309-59aebbf0dff4 | -8.6261 | -44.0583 | 2024-10-02 00:31:41 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cafa0d89-94b3-365e-a3c6-f5090a488a6e | -8.8034 | -44.8241 | 2024-10-02 00:31:41 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
