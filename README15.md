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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f1929b7-09a9-3a32-a1f4-ec9613da2330 | -12.8782 | -62.7815 | 2024-10-02 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| ebd09eda-0258-3425-b92d-e5eadbf6ff05 | -12.8784 | -62.7622 | 2024-10-02 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c9ad1858-e00c-39ef-9150-7f2f40206ccf | -14.83 | -58.6154 | 2024-10-02 00:36:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| dea7cb39-cc88-3771-88ba-41df569c8126 | -15.139 | -55.8285 | 2024-10-02 00:36:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 5eb36feb-8b80-39a2-be53-e20de8ef9ff3 | -15.3708 | -55.8431 | 2024-10-02 00:36:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 91eb8d51-8f53-3413-b935-db57df3d7e30 | -16.3319 | -50.1057 | 2024-10-02 00:36:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| e698d62f-d00a-3fd2-ac74-c51e9b0cd528 | -16.6108 | -57.3398 | 2024-10-02 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 9199ca55-d084-385d-a582-d74a24e65d2f | -16.6303 | -57.3376 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| dece9244-f1f5-363d-a65a-f69d52823224 | -16.6306 | -57.3171 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.9 |
| 1298d7ac-d48e-3d06-bd3c-934cc4170579 | -16.6884 | -57.3718 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| cccf4f25-c464-3e71-9bc3-657f9b7da95b | -16.6887 | -57.3513 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| d0ca7531-afa1-357b-9b79-79588f012a2a | -16.7063 | -57.4718 | 2024-10-02 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 3d43525f-2dc7-30c6-a173-d5944e286f33 | -16.7082 | -57.3491 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 49a5bd9f-72dd-35d3-8cfc-25b4d704e512 | -16.7265 | -57.4287 | 2024-10-02 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| c8c95ba6-3951-3ac4-ac29-a524e4983a0e | -16.7452 | -57.4878 | 2024-10-02 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| e3dd70d7-b3c2-397a-8cb5-fb19d90a5a74 | -16.7455 | -57.4674 | 2024-10-02 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| d907effa-ce7c-3fc4-9e34-4c3610d5470d | -16.7461 | -57.4265 | 2024-10-02 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 6439a9b9-b4e6-3b0e-a90b-6731ac653378 | -16.7663 | -57.3833 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 5608c51d-b78f-385d-865e-dd703e3c77a8 | -16.7666 | -57.3628 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| aaac0536-405e-3277-a1e2-138180f5adfe | -16.7862 | -57.3606 | 2024-10-02 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 746cc551-04f1-3e75-b600-b0d93dd92443 | -16.8039 | -57.4811 | 2024-10-02 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 04d201a2-7279-3563-9d77-308453cc3806 | -16.8184 | -57.8058 | 2024-10-02 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 8bab650f-0776-3048-8428-ab491a240d5e | -16.8234 | -57.4789 | 2024-10-02 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 9b85ee1a-22e3-3684-89e3-8384fdaf0bd2 | -16.8238 | -57.4584 | 2024-10-02 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.6 |
| 20c9860b-10f5-33c4-b269-cbe9dbc13e00 | -16.8386 | -57.7628 | 2024-10-02 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| f31b73d2-313a-3fe5-bd97-feb51a8f829a | -16.8695 | -55.848 | 2024-10-02 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| c83a6088-5284-3e2c-8956-89b5f7012279 | -17.0612 | -56.0931 | 2024-10-02 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| d7f07bff-b60f-32cc-8a25-7d2258753acd | -17.0705 | -56.7114 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| e29b9a29-b9ba-326e-983c-3b58dfabda5d | -17.0709 | -56.6908 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 95cf84db-b967-3235-914a-dde10e16a2a1 | -17.0902 | -56.709 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 992b4582-e2ff-32d3-90a8-aded49a621a4 | -17.0905 | -56.6884 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| e1956192-ce2f-37c5-be55-290522d10e07 | -17.1098 | -56.7066 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| fca45d88-8b28-383d-b0a9-87fedc8b855c | -17.1101 | -56.686 | 2024-10-02 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 9d78aae5-c226-3f40-bb0f-d57af7f7b5c7 | -17.1577 | -56.1844 | 2024-10-02 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| b38f3aed-346a-3ad4-a097-e009a989ba44 | -17.1581 | -56.1637 | 2024-10-02 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 99a24cae-bff0-3078-9cb6-55179af61792 | -17.1971 | -56.1795 | 2024-10-02 00:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 53fd214a-e356-386c-886c-a2d49337c6e5 | -17.1974 | -56.1587 | 2024-10-02 00:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| c1d5d8d4-bf08-3f3c-be56-7794afa56b39 | -17.196 | -56.2417 | 2024-10-02 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 9e65b344-941e-3426-b778-9e6e6425ca30 | -17.1964 | -56.2209 | 2024-10-02 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 2dcd6d3d-c1fe-3257-82ce-1960251e45dc | -17.1967 | -56.2002 | 2024-10-02 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 8a1bccb1-a7c9-378c-a087-03d31b28fbaa | -18.0652 | -42.6027 | 2024-10-02 00:36:45 | GOES-16 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| 49026123-e3b8-36fe-8d15-7e77fda285b2 | -19.2317 | -46.8687 | 2024-10-02 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 9e74fb92-0eed-39b2-aeae-b1a60b8ba307 | -19.2323 | -46.8452 | 2024-10-02 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 7b88dc54-b518-3894-ad7b-df9fa856183e | -19.2519 | -46.8641 | 2024-10-02 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 131.0 |
| c54f2804-d778-3a82-98e5-825bb25e51b1 | -19.2526 | -46.8406 | 2024-10-02 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 463ed892-e8de-39a4-bc1a-9d7efaed1dce | -19.9921 | -55.4728 | 2024-10-02 00:36:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e2f3699a-aeef-3ece-94d3-87d64d0c7460 | -20.5266 | -46.2783 | 2024-10-02 00:36:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8b0c25d1-56e7-3d65-9589-7ca114d2c174 | -21.2861 | -47.604 | 2024-10-02 00:37:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c38aa301-edef-37dc-9563-ae8bfca02bba | -21.3456 | -55.6841 | 2024-10-02 00:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3e563035-492a-3037-803b-0ad3fd00f593 | -21.6275 | -50.796 | 2024-10-02 00:37:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| fae079cf-efb9-39a8-b8ca-4ed7c49981af | -21.8079 | -48.7626 | 2024-10-02 00:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 46f35939-ff83-3586-b796-74b9ad3cc3fd | -22.9277 | -43.7243 | 2024-10-02 00:37:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| ac7a033b-c28f-3b8e-b03f-03563a391ccb | -22.9006 | -45.1029 | 2024-10-02 00:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.3 |
| 7bbd78a3-a98c-32aa-a8c4-01bcf088bcac | -22.9014 | -45.0779 | 2024-10-02 00:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.6 |
| 216a4b4a-bdab-30ac-a6dd-6078c5b3be30 | -2.6496 | -54.6172 | 2024-10-02 00:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 50e8c281-f1d8-3376-92a1-5e8e7b07ba86 | -3.128 | -49.4235 | 2024-10-02 00:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ff77a608-208c-3ca8-a5aa-5648e9d24fe3 | -3.2136 | -46.7843 | 2024-10-02 00:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 41d810fa-8e91-3c0e-8c25-86e3892ce0a3 | -4.4865 | -48.1261 | 2024-10-02 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c7f7af9a-5562-33cb-82e7-52e84a7a26b2 | -4.4866 | -48.1045 | 2024-10-02 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 44782674-d518-38fd-aa38-752cbb01f16e | -5.9788 | -45.3621 | 2024-10-02 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 20632679-8951-31bc-b21c-453eea37e04d | -6.1373 | -46.4484 | 2024-10-02 00:45:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| fb8681da-c60b-32b9-ae54-f6a0d631543c | -7.1796 | -46.9444 | 2024-10-02 00:45:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 5a44bdd6-5eba-3227-a81d-505a68659e44 | -8.205 | -44.365 | 2024-10-02 00:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cc1ca866-ad67-33fe-bfa0-c3ebe3136ffa | -8.2053 | -44.3419 | 2024-10-02 00:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1635bee7-a72f-31ad-ac63-cfd43a8176e8 | -8.2239 | -44.363 | 2024-10-02 00:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 84658402-fdef-33bd-8710-1c82ad619f73 | -8.2242 | -44.3399 | 2024-10-02 00:45:52 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7671d9ab-8f7f-3d18-8915-a8b570603443 | -8.4643 | -62.7124 | 2024-10-02 00:45:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2f4cc25a-cc32-3568-af63-d14989b26408 | -9.5398 | -62.8005 | 2024-10-02 00:46:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d2c01479-5399-30a2-b0ea-959f7c47ebd0 | -9.5584 | -62.7997 | 2024-10-02 00:46:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1e1e1253-6ef1-3a9c-b791-aa7403a44a99 | -9.9367 | -64.9179 | 2024-10-02 00:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 198.3 |
| bb47b77f-6363-307c-a90a-ca07cd659c5e | -9.9368 | -64.8991 | 2024-10-02 00:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 185.4 |
| b50458a2-be4c-3e6f-94e4-fcfc9b85c55b | -9.9553 | -64.9172 | 2024-10-02 00:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 209.1 |
| bb4381b0-77df-3a00-a000-434953a822e7 | -9.9554 | -64.8984 | 2024-10-02 00:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 7804d5b2-c7ce-34bf-9248-61c2dc13b20c | -10.626 | -55.8752 | 2024-10-02 00:46:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e1e52cd5-1a0c-3da8-a29b-62ac58e58b0f | -11.4822 | -56.7892 | 2024-10-02 00:46:11 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1fe6f94c-429c-3670-9258-3ee26f121c67 | -11.6554 | -65.018 | 2024-10-02 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| dfae03dd-bc18-395f-9032-d916ca1fcdfb | -11.6555 | -64.9991 | 2024-10-02 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 89ca8287-ccb4-3efa-98fc-aef77f764a9c | -11.6556 | -64.9802 | 2024-10-02 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8ec2b77b-55cf-3d9e-afc9-b3bf378fbecc | -11.6743 | -64.9983 | 2024-10-02 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 908faa25-c87e-36c5-ba88-d7845b91156d | -11.6744 | -64.9793 | 2024-10-02 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ec77f93b-a47e-39bc-952f-c235dc4ad296 | -12.4433 | -43.7242 | 2024-10-02 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 5541ca2d-f6b4-357a-8930-69afb759cd38 | -12.2754 | -47.6473 | 2024-10-02 00:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e6b76787-8251-314b-8b82-44dac50f9cc3 | -12.2946 | -47.6446 | 2024-10-02 00:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 88d35bf3-61d5-3cb9-9b9f-0030881365f5 | -12.6484 | -63.1214 | 2024-10-02 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 2a5343e3-e4fb-301c-b293-a2aadb0b35f3 | -12.6486 | -63.1022 | 2024-10-02 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 825c8768-67fb-350d-a666-80c846a4e84b | -12.7054 | -63.0798 | 2024-10-02 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 18642e9f-9fd5-30e3-8226-d8689e25c69f | -12.8593 | -62.7826 | 2024-10-02 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9380a784-1074-31cb-9bd8-03034dcf7d18 | -12.8782 | -62.7815 | 2024-10-02 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1f266d5d-36f0-35ae-81ba-131a8e7063a4 | -12.8784 | -62.7622 | 2024-10-02 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9356e07e-f591-3336-b562-8712a6458fb0 | -13.0933 | -51.4139 | 2024-10-02 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| eef243c7-869d-3f39-b5f9-9bf463fa5c0e | -15.1197 | -55.8307 | 2024-10-02 00:46:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f0f66c14-bba5-3006-aaa0-d138d28b1d5b | -15.139 | -55.8285 | 2024-10-02 00:46:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 1f167dc4-9c66-3c90-b563-616c99bfa857 | -15.1393 | -55.8079 | 2024-10-02 00:46:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9e16965f-bb4d-38e7-ba9f-d4281752e619 | -16.109 | -53.5215 | 2024-10-02 00:46:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 101ff90d-be26-349a-add1-aae7e07744de | -16.6303 | -57.3376 | 2024-10-02 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.3 |
| 263b1454-6b10-31b1-b59e-4fc8fed95990 | -16.6306 | -57.3171 | 2024-10-02 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 42320b70-25b3-3b07-9305-f43119962b54 | -16.6868 | -57.4741 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| dbec6b5e-343a-3571-8866-256500471823 | -16.7063 | -57.4718 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| d6e39496-1bf5-3a21-b7c7-953fe6307d37 | -16.7265 | -57.4287 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| a3f96377-3cce-3e9d-a5c6-0216c308875d | -16.7452 | -57.4878 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |


[Clique aqui para ver as próximas entradas](README16.md)
