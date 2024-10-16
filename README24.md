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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bde976f-7110-39f6-87d6-0ad62ef40acf | -11.7103 | -65.2424 | 2024-10-16 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2bd681db-5e75-37ec-a3df-e293108dddce | -11.6917 | -65.2243 | 2024-10-16 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| dce9e4ce-9fa2-399a-a90a-3ca0f95a9a38 | -12.3795 | -63.7103 | 2024-10-16 03:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e4d6c814-7338-3978-aba0-2d56037c74e2 | -17.1664 | -56.8439 | 2024-10-16 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 3e6a731a-c044-35c8-a3d9-b677cf3634de | -17.2277 | -56.6922 | 2024-10-16 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 89c7cf56-a1f5-3e37-bc5b-918e08c602a2 | -17.2081 | -56.6946 | 2024-10-16 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 29fd7ed0-8b5a-3b8b-8460-f327e5e94c91 | -17.1951 | -57.4972 | 2024-10-16 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 089b332a-23fc-3d96-a7b2-5b8cf6ac84af | -17.904 | -57.4328 | 2024-10-16 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 962bcc64-0e9d-3239-9b17-5032ed27526a | 1.0199 | -52.2162 | 2024-10-16 03:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 99cb1e22-fe23-3b66-a566-884273e5856a | 1.0016 | -52.2164 | 2024-10-16 03:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ed5ba7a4-9ed7-3721-8170-63b28c94c514 | -2.6118 | -49.0985 | 2024-10-16 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 51d79ef4-cc8f-36f2-865f-fa098bababa2 | -3.1098 | -54.2464 | 2024-10-16 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1801b034-9933-3e3e-ae20-b36999e45213 | -3.1099 | -54.2263 | 2024-10-16 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 176fd319-8a66-3dc1-8466-d70b2f0ef7d8 | -3.1282 | -54.2459 | 2024-10-16 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 81efee64-c528-3727-bac4-492c7fb21e53 | -3.1283 | -54.2259 | 2024-10-16 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| dad0c7ad-608a-3761-9354-72ac2cf49f06 | -3.958 | -46.4442 | 2024-10-16 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 779fcb17-d1ca-3146-86d9-d508e1b2902a | -3.9581 | -46.422 | 2024-10-16 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| fe930283-a411-3519-8ca7-126cddacde8d | -9.114 | -47.0074 | 2024-10-16 03:25:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 735a5ea0-6eec-30a9-b4f8-c28c6f86bb60 | -9.1142 | -46.9851 | 2024-10-16 03:25:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| bd3cd84f-3110-3477-b0a7-69baa358203d | -9.1517 | -47.0034 | 2024-10-16 03:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 36e27930-a4f6-3178-bab2-71a1acce1e49 | -9.152 | -46.9812 | 2024-10-16 03:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 359ce8fc-2402-300b-b100-d6020d61930c | -9.1706 | -47.0014 | 2024-10-16 03:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 55ed2428-b4e9-3d9f-929e-6c5483ca90f0 | -9.1709 | -46.9792 | 2024-10-16 03:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| e46e6ed8-49bd-33ca-a6d9-0ad2ac8e7987 | -9.1728 | -65.3945 | 2024-10-16 03:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1d0e8127-3877-3dba-ba30-6be560dfe6c5 | -10.822 | -49.256 | 2024-10-16 03:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6e76a026-d575-3b1c-bdad-53b9599f6d47 | -11.6917 | -65.2243 | 2024-10-16 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 38f5492d-d331-3773-809a-e83a14081052 | -11.7104 | -65.2235 | 2024-10-16 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 87c63a72-4fe9-387a-a328-75d43cceb59d | -17.0262 | -58.2912 | 2024-10-16 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| c0938a6c-766e-34da-a6ac-6857c62ae286 | -17.1664 | -56.8439 | 2024-10-16 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 387066c1-d593-3d31-9a27-b2b3c59ae685 | -17.1951 | -57.4972 | 2024-10-16 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| f945f947-8e13-329b-97b5-63780eaa13c1 | -17.1954 | -57.4767 | 2024-10-16 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| b21072c2-1770-3d82-9a7a-06308d23fb22 | -17.196 | -57.4357 | 2024-10-16 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 3f39180e-31a7-3fca-8a97-2f42de56096d | -17.2081 | -56.6946 | 2024-10-16 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| b0d994da-1b6d-31a3-94e9-467098941606 | -19.5808 | -57.0071 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.0 |
| dd09fcd0-c312-3444-a831-dd6375177bc2 | -19.5812 | -56.9862 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 343.1 |
| c86c374c-6658-30e2-b7b1-67ea2ff7d46e | -19.5816 | -56.9653 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.7 |
| a400b70f-2779-3bf6-abdb-cd08608187bc | -19.6009 | -57.0044 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 634f42d1-1164-3748-9205-290af0c03e5a | -19.6013 | -56.9834 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 334.5 |
| e5bd5a0f-ac03-38e6-b18b-78b97cc966cf | -19.6016 | -56.9625 | 2024-10-16 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 071b905f-a288-378f-aedd-20e12114cf4a | 1.0199 | -52.2162 | 2024-10-16 03:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 01e2ec1a-bc53-33ab-b44e-ac8ddaa67212 | -3.1099 | -54.2263 | 2024-10-16 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2dbd99a9-cf56-34ca-a31e-1303349e1810 | -3.1282 | -54.2459 | 2024-10-16 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6524ccdb-b478-3772-bbf0-78b8fb6de1b3 | -3.1283 | -54.2259 | 2024-10-16 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6561dd3c-ea79-322d-a550-a88a3856e5d4 | -3.958 | -46.4442 | 2024-10-16 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.3 |
| eb9bf3e9-e8fd-3e1e-b6b2-3fd8631d1be2 | -3.9581 | -46.422 | 2024-10-16 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7c02aa36-ec13-3fc6-9b35-3b01f47fba3b | -9.114 | -47.0074 | 2024-10-16 03:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a1305c5a-025e-348e-9fe7-35cf9f96adea | -9.1517 | -47.0034 | 2024-10-16 03:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7705d2c0-d792-3f34-9b03-cf8916da9faf | -9.152 | -46.9812 | 2024-10-16 03:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| c2ae7245-a63d-3a67-b1e7-542ad12bfdd1 | -9.1706 | -47.0014 | 2024-10-16 03:35:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| af083005-8bfc-39a8-9771-bec1ac64ea7d | -9.1709 | -46.9792 | 2024-10-16 03:35:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| fc9596d2-e5cc-3cac-9796-f65479c2772c | -10.822 | -49.256 | 2024-10-16 03:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4f86d7cc-12c9-3049-93bc-4bfb683e51e0 | -11.7103 | -65.2424 | 2024-10-16 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a0158d67-b802-3a75-9925-790d5635598d | -11.6917 | -65.2243 | 2024-10-16 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| bff78da5-5539-3a9a-874f-240f22111b28 | -11.6915 | -65.2432 | 2024-10-16 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e1251ec3-711c-34dd-b6f6-0f9786397a34 | -11.7104 | -65.2235 | 2024-10-16 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 28c18382-8900-3b52-be87-8e1be96f0a58 | -11.7292 | -65.2227 | 2024-10-16 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.3 |
| a2024c91-442f-3dd3-b611-b61b9a942111 | -16.9596 | -57.5245 | 2024-10-16 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| e09abf0c-7c48-31c0-91cc-fc23544df774 | -17.1664 | -56.8439 | 2024-10-16 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| f67de1b3-8973-34bb-842a-5c0079dbe83a | -17.0262 | -58.2912 | 2024-10-16 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| af58c6cc-8542-3941-a361-957899877bdc | -17.196 | -57.4357 | 2024-10-16 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 8972cc75-28f7-35a9-abe4-041dacc33df2 | -17.2081 | -56.6946 | 2024-10-16 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 36c354cd-13c5-3240-9ac3-ca92cbc31ffa | -17.2177 | -57.3102 | 2024-10-16 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 40dce50b-9ad7-3a9e-97e1-c05267e3c2b4 | -18.254 | -56.6029 | 2024-10-16 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| a9e2bd0c-90fc-34e9-9670-3bec034a58ea | -18.2544 | -56.5821 | 2024-10-16 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 735947df-a725-3c80-82fb-f0d42a30cf81 | -18.2739 | -56.6003 | 2024-10-16 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 8539882d-5358-3956-9957-65b72ee52613 | -18.2742 | -56.5795 | 2024-10-16 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 36edf592-18b7-3d6f-aaa1-48bc41895bca | -19.5808 | -57.0071 | 2024-10-16 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 1c770768-4cd0-30cb-bf09-a70672a56047 | -19.5812 | -56.9862 | 2024-10-16 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 264.5 |
| 95310e80-49c7-3d9f-8867-50bf81f1cc99 | -19.5816 | -56.9653 | 2024-10-16 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.3 |
| 2d52be89-30d6-32b8-86ee-a245528dba9d | -19.6009 | -57.0044 | 2024-10-16 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 64c05be2-1ea8-30a5-a33b-cced5bb1d62f | -19.6013 | -56.9834 | 2024-10-16 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 197.9 |
| a7b069d9-514b-34dc-9ee5-a0154ee5106c | -5.04799 | -46.08344 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| acfafa8a-d4b4-337e-8fcf-a666539785d4 | -7.53143 | -34.84575 | 2024-10-16 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6c0edde7-00a9-33b2-a421-44626b32d370 | -7.47739 | -34.84444 | 2024-10-16 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fab0dd64-e542-3beb-b8ad-8f2d0d604bbd | -7.3945 | -35.15467 | 2024-10-16 03:42:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 65c7e540-bb0a-3883-ae44-4c94f12b98cb | -7.39396 | -35.15813 | 2024-10-16 03:42:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 8f6047a7-8cc2-3d18-bc9d-26bba3f8b6a9 | -7.39066 | -35.15761 | 2024-10-16 03:42:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 93ffb497-fd87-3990-b1df-bdc43b258db0 | -7.36885 | -35.23206 | 2024-10-16 03:42:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f3b79557-acab-31d1-ac1d-f35ab3619ee9 | -7.16727 | -35.15029 | 2024-10-16 03:42:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1a8b00ad-e05a-31a3-b913-56e19c5cf388 | -7.01741 | -35.04526 | 2024-10-16 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ea9fdb2-73a0-3faa-a382-16232f6621d5 | -6.84741 | -35.2408 | 2024-10-16 03:42:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd69cc55-0c87-3cb9-a61c-847530a5a2eb | -6.5697 | -35.12299 | 2024-10-16 03:42:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf6a40ce-e91e-3562-9cc2-9e7d0ad22edb | -6.56694 | -35.11903 | 2024-10-16 03:42:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e99f851c-2e37-3f1d-8e11-12d996d17516 | -6.5664 | -35.12247 | 2024-10-16 03:42:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 858e3cd7-8021-357d-a020-e5245590c436 | -5.45949 | -36.71394 | 2024-10-16 03:42:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f627e32e-58bf-31f2-bb44-696e0a01af7b | -5.45891 | -36.71761 | 2024-10-16 03:42:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31131c98-559b-3591-a2b6-0ddd976e6237 | -6.64648 | -37.37341 | 2024-10-16 03:42:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f6b2474c-da66-3e0d-9a07-e728a1454dc3 | -5.02195 | -37.65024 | 2024-10-16 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 74f7aa90-203d-3b6f-b1e7-fe96c219bf42 | -4.99198 | -37.41067 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93596158-cee4-36d4-819b-87e719b836fe | -4.98848 | -37.41013 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 37447796-7b7a-307e-b7ae-fc1518f20e8d | -4.98785 | -37.41402 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ad080abc-c2d4-3c12-8a94-85187fff3df1 | -4.98498 | -37.40957 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 105df580-fad3-3bb6-8ed6-18ed7694aafd | -4.98435 | -37.41347 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3df340a4-843c-3051-bc6d-5a7b5c63b044 | -4.73063 | -38.45935 | 2024-10-16 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 58e77c15-b419-32c3-80ea-8dc6c5abf287 | -4.72323 | -38.45818 | 2024-10-16 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a884abb9-d84a-39f7-a484-a0623df05420 | -4.7225 | -38.46261 | 2024-10-16 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 95757172-c6c5-3f20-ab2d-686223bc7f93 | -4.7188 | -38.46203 | 2024-10-16 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9542dcd9-d824-3212-948d-f7d7040cc281 | -5.56176 | -37.34437 | 2024-10-16 03:42:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9c740c41-8202-31e8-a4b5-47934b5104e8 | -5.33026 | -37.83303 | 2024-10-16 03:42:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 007d8719-17e1-3566-bd5d-05efb4fea045 | -5.19913 | -37.31177 | 2024-10-16 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README25.md)
