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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abbe75ed-02b3-334a-a629-b23ed5cf6999 | -11.64079 | -54.5326 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f8fa6b-0c8e-33f0-8bc1-5cb00e57158d | -11.38483 | -54.35972 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ea36df2-0322-3c4b-ad94-7b6b1057af6c | -11.38428 | -54.36271 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0056be62-4066-37cf-8d0a-7557eda7d454 | -11.37923 | -54.36165 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbe9fb2b-45c4-3cd6-a8ea-4a781f2e9dab | -11.37868 | -54.36463 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f079bc3e-1c44-331c-a38b-bbb6ed3dbec6 | -11.37017 | -54.32556 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf12af2-a97d-35c2-a204-7f42d85a27b1 | -11.10826 | -54.23159 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3c2e21-e5d3-390e-b22c-8294cd342b6e | -11.10769 | -54.23464 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf08ddc5-a86f-36c5-82ac-3ab9d437b37e | -11.10379 | -54.22759 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e8f2365-c203-3f09-a8cb-5409c800f57d | -11.10322 | -54.23064 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc5298ff-5fcc-3b47-877a-907e54b087e5 | -11.10264 | -54.23369 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f8253a2-c665-38ea-af89-2b5894c9b46c | -11.10206 | -54.23674 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c771ffa8-e096-3462-ad36-79527f548eca | -11.10148 | -54.23978 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2181d3c3-5596-30a3-9309-13a09b4b80a5 | -11.09981 | -54.22927 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25fbf060-1d5d-3cf4-a4ee-f090fedc0028 | -11.09926 | -54.23232 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35d24f2d-c96d-3443-8b24-964ad1df6c53 | -11.09871 | -54.23535 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00a97eb7-4987-318c-9b0d-e78997d40ced | -11.09815 | -54.2384 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6f5cb59-8bc9-3e0c-9ab1-c52fe16f7286 | -11.09815 | -54.2298 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae273a75-166d-3dac-afb2-1aa70abe7713 | -11.09757 | -54.23282 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fa222b8-86d4-3e44-8b94-523044b553bf | -11.097 | -54.23584 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1602215e-f046-365a-8bb0-ff8f59aab006 | -11.09642 | -54.23887 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84a932fc-0287-3ec0-a0b5-81760b9dbf8a | -11.09364 | -54.23446 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9defb4da-9ef8-31fc-ba93-33fe6bc8a7b1 | -11.09309 | -54.23747 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22d8d182-c91f-335b-897a-42f94be3d37b | -11.09194 | -54.23495 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e4965ef-7da3-3863-ae14-78890da5b338 | -11.09136 | -54.23796 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a155c6d7-a263-3f83-a813-38448a23d395 | -11.08421 | -54.78695 | 2024-10-06 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c7f5669-6197-3568-a56e-48844dc52322 | -11.08134 | -54.7732 | 2024-10-06 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c03d27d-7f70-3dc0-ba5a-662fd02e9e64 | -11.08074 | -54.77642 | 2024-10-06 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9044e97c-fee9-31bd-8458-c6513fc1c890 | -11.07885 | -54.0323 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3acf108-50cc-39ac-95b3-eb8ac5919c6c | -11.0783 | -54.03528 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e75296c3-c6de-31c8-9acd-0eaeae0e3454 | -10.97481 | -54.00855 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e29759b-1554-3675-988f-21fbaf3a9f29 | -10.97371 | -54.01447 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d8a6bd-8420-35f6-b113-4cc605c4a91e | -10.97316 | -54.01746 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 961d8b30-4088-3fc8-8988-e3e85f9774bd | -10.97261 | -54.02045 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720780fd-f916-3bdf-92c9-8e71e9a9289a | -16.64317 | -55.5514 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e3c343d9-18cf-382a-b0b4-06f699144c1b | -16.63326 | -55.54917 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 94c46f6e-067b-355b-8ffa-b8e395ac6943 | -16.63177 | -55.53074 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c0dd07f3-e81e-32ff-b7d0-7796a85b371a | -16.6268 | -55.52972 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 0d2eb865-119f-3c35-a2fa-1b6846c0ad26 | -16.58194 | -55.90953 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b260db0b-ddc7-3508-a271-c4f2c2064ad3 | -16.56351 | -55.92184 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cecb30ba-28e1-3927-a72e-039b06952ce2 | -16.55906 | -55.91756 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a7e84c1a-cd7d-3107-a599-50b0c61c4950 | -16.55842 | -55.92072 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a38090e3-9a08-3389-815d-3d3cf45c891a | -16.5495 | -55.93849 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f061ff43-553e-3567-bd17-8ec8c9785c40 | -16.54822 | -55.9448 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 20ef2955-539b-38cc-b0a8-e539060320d1 | -16.14901 | -55.9272 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 92a7dcf6-57f3-3e3e-9870-57105e929fd8 | -15.84299 | -56.09845 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ce02d4d3-3265-3728-a743-d3c998d08a3b | -16.6469 | -55.55869 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| a95da9e6-185f-3dda-9ac2-637d70ff0893 | -16.64674 | -55.53352 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e097ffce-b615-3123-9a91-716aeb447058 | -16.64198 | -55.55736 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5885b3e9-511f-3ebf-b4a2-6e87d4c6d579 | -16.64174 | -55.53267 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d255909d-8a76-3a67-8426-7b0d345a6e68 | -16.64108 | -55.56188 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 078af35e-d8e8-376a-a2e4-1a74a0d1305b | -16.64047 | -55.56493 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a433ede4-bbed-3927-a208-cbd8a0bf20ed | -16.63944 | -55.54416 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fce6d71a-4b66-3a20-b514-e318a885abce | -16.63827 | -55.55001 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 35f11878-4d15-3269-bc7e-8f57ad19436d | -16.63707 | -55.55598 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9b683475-aa8d-38e3-8ac1-dcb8e257a470 | -16.63676 | -55.53169 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 46da27b7-4e97-3788-ac6f-c540d7aba677 | -16.63616 | -55.56056 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b6811fa5-31b9-3bb3-a800-71a12285ddb8 | -16.63559 | -55.53754 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 5eeac9cf-3d06-316c-a3e2-45b542907c98 | -16.63555 | -55.56362 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7dd4daac-6117-3e57-92ec-ecf0aeace7be | -16.63208 | -55.55503 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ce2ab2f7-f044-38e2-a24a-8e0b27327923 | -16.6312 | -55.55945 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5ebabbb9-50cb-3df9-8f1a-b730ca0b92ee | -16.63061 | -55.56238 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e1362156-72d9-318a-9657-3eb01b78f414 | -16.64557 | -55.53939 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 20072b53-cd87-3221-a5f0-00ed062316e0 | -16.64437 | -55.54542 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5779df03-b063-397b-b055-ace1414fd895 | -16.64059 | -55.53843 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a846940b-67eb-39cf-9e7c-cf69c0d1a73f | -16.62621 | -55.55847 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 76079435-4d92-3e36-890e-c7ca9f262799 | -16.56479 | -55.91555 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3b82c424-3964-3abd-a17f-4c129a1d2aa8 | -16.55906 | -55.9439 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c7d25c21-6748-3eff-942e-cfcff4768a70 | -16.55651 | -55.93016 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 98609fb6-924d-399b-b0af-0b24c8832175 | -16.55396 | -55.94278 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8f186636-2307-3c81-8819-d689f4e542ad | -16.55332 | -55.94593 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 71c534f7-bc78-3a53-b2ed-98da6e8df9b2 | -16.54886 | -55.94165 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 33c16980-bace-3162-b92a-e29b3e7ed9c3 | -16.14968 | -55.92387 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 64906b8f-1a55-33ad-beaf-d4fdc4f1bacb | -15.84231 | -56.10178 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| c3e4396a-ddb2-32fc-b56a-c570ce5da0e4 | -16.57685 | -55.90838 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| def160aa-00fe-3979-a531-89f7fc3ab79e | -16.55778 | -55.92387 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2c47f047-609e-3e05-8838-4457c0ca0103 | -16.55206 | -55.92588 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7bee9230-f9dc-31f6-bf8a-ea803b39d753 | -16.55142 | -55.92903 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f00f12fc-997f-365c-9dfc-b87fbb4179e1 | -16.55078 | -55.93218 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 43812f62-2913-33aa-9afe-95b4fa1098e4 | -17.02627 | -56.68736 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e886b7e0-dbef-36e5-93db-0ecad656cfbd | -17.02311 | -56.68575 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0fd1dda8-9f31-300c-9dc0-217041d80f4f | -17.02241 | -56.68921 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7a7e5092-2c54-3294-9d5d-bfc60f0cc1ba | -17.01881 | -56.69651 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 911cf7ab-903f-32a1-9413-daede6bfae4b | -17.01496 | -56.6884 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 63a042f6-a2df-3a21-9d9d-78321baa7f57 | -17.01112 | -56.69023 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 663cb56b-c487-362f-92bd-9fda749eac6e | -17.00821 | -56.69409 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 33b7c405-0fec-37eb-81d2-47aa19dab4b8 | -16.96109 | -56.61022 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 50a3e667-c72c-3727-ae4c-9db7667e38e2 | -16.96038 | -56.61365 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ce5d854e-7dba-335b-b253-9cb0484a5b52 | -16.95226 | -56.62618 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6a33927b-d934-304f-8971-86f0927c3139 | -16.94841 | -56.61811 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a04c97e9-d98f-37b8-a3e8-02bb2c138ad1 | -16.94384 | -56.61349 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 61df145f-61fb-3a59-93d6-c6aa6b1f0d7a | -16.94242 | -56.62033 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4fb0fc47-cdfb-3f71-b766-4fd2fb9838f0 | -16.9417 | -56.62377 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 362fccd8-eeeb-3db3-8f2c-a5f2f30cb31e | -16.94099 | -56.62719 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c12c8a47-1959-3ce9-ab36-be7009406efe | -16.69024 | -55.91111 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a3914859-7fb8-3b28-b8ce-0c36528cbbc9 | -16.68989 | -55.5507 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f2ab3b10-d003-3692-884e-ae2e3b155173 | -16.68768 | -55.89749 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0df8a747-f3a1-3167-9f17-c20831a43f15 | -16.67754 | -55.89524 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 01460742-5d09-3343-baa5-90e506a9b17f | -16.67625 | -55.87544 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1265d027-fbf1-3d73-9a25-535ad11f2a14 | -16.67502 | -55.90773 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |


[Clique aqui para ver as próximas entradas](README83.md)
