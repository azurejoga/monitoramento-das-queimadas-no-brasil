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
| 38a76fdc-c5a4-3c83-aa62-c4046965bfad | -7.60774 | -45.55379 | 2025-06-20 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c39c5062-56a1-3688-823d-a424581f65a5 | -10.67359 | -51.89341 | 2025-06-20 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b44840f0-8a54-3941-bb58-173041545772 | -10.76914 | -52.7581 | 2025-06-20 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 907b4ea2-aa9d-3b1a-aa65-3f1431d5a03f | -9.31204 | -44.72277 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff5b36f7-4116-3771-bbe7-f5a32627e4ba | -9.48973 | -56.08178 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 39862053-43e6-3d26-8a0e-f0f49a8358a6 | -11.13865 | -46.637 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1453b56e-76a4-3ed4-bea4-e85c8c8a3185 | -9.4826 | -56.07653 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f5dd4d11-666c-3944-b5d4-188c1df4d761 | -6.47403 | -53.48824 | 2025-06-20 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 548e30ed-0c67-337c-bd3d-ff74f74b6d62 | -5.41756 | -47.5702 | 2025-06-20 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86f745c0-5a32-31a5-9af9-861dc4dab272 | -12.21879 | -45.53017 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9056e778-0caf-3b13-9cbd-d3769f096ddd | -7.21749 | -43.07073 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5082eafe-5e83-3c51-b998-6b66b36319be | -8.8804 | -49.26231 | 2025-06-20 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d60096b-a2dc-32ed-9ec6-769dcd415a8b | -6.64138 | -47.86337 | 2025-06-20 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18adee11-f9ab-37f2-aa87-9083cac07d85 | -7.97052 | -46.22162 | 2025-06-20 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19a5fcbd-a3e4-3dbc-a621-737f35ee51c5 | -5.45106 | -43.57693 | 2025-06-20 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23a7ef9d-e1ed-32dc-866c-bdf6ea56764f | -4.59103 | -47.89303 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2dd28f7-c447-3ab8-bb1b-cb8fa7c75f82 | -6.1421 | -47.26092 | 2025-06-20 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb65cb2-4ee8-3e71-a695-d61e4e933a49 | -7.87223 | -47.89675 | 2025-06-20 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 418d6f2a-47e9-3b31-b95b-66f1e9141ac3 | -9.30211 | -47.78613 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d170172b-76ae-3985-ba3b-9894756ce590 | -14.62642 | -48.1198 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3a504e7-2c49-3034-ac63-25cb8090e9d3 | -12.89589 | -56.98723 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e40f4ccc-ad76-35a6-b12b-9f596f35f517 | -12.35066 | -49.30715 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 19ea1ff7-088d-3864-9170-72dc5c8bdf51 | -11.9382 | -48.42812 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9efa6193-d9ea-3004-a574-90c7fe60e999 | -11.81751 | -54.50189 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87b115b8-28c9-3c43-93a7-a564943937aa | -11.13257 | -55.1903 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f858ada-ab6f-3b03-8c80-47ebcd18d303 | -16.31277 | -58.2598 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 202035ee-4409-3a69-962e-05a6244cfb4e | -11.53155 | -56.99607 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da07d61c-b7f6-3194-8cdb-dd084f89f7a3 | -14.03491 | -53.36239 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2b383be-5ac4-30c9-9b6f-7fa1c094c072 | -16.31023 | -58.26232 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 3a2aef27-667d-386d-8a91-5302d18b1d3a | -12.75564 | -44.41044 | 2025-06-20 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 545c3d5a-30a1-353a-8775-44aa15bd3613 | -11.622 | -58.29407 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1003d6d4-4f12-3681-a0ae-da32330a4359 | -14.03601 | -53.35514 | 2025-06-20 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f18985e-4cb5-3501-8822-fa71a683ab7c | -15.5717 | -47.85646 | 2025-06-20 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0338eaa0-4b21-3a6c-a5ac-76f62a78e540 | -12.52477 | -57.20863 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52689ed6-9ef3-3d7a-8080-c1d53b111ef5 | -11.62007 | -58.29614 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6300655-669b-33bc-b0dc-d6c0e035871e | -12.02469 | -57.09408 | 2025-06-20 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb121e99-0b14-3610-934d-e56d3cbae0b0 | -16.30558 | -58.25851 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 11e1948c-0b03-3012-88c7-c462b57a2405 | -12.28489 | -57.27327 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db297e2b-b1d7-3ac7-bc33-96d2ebb35240 | -12.024 | -57.09826 | 2025-06-20 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 336414af-7879-3742-a32c-29a6a41594db | -16.30948 | -58.26662 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| ddb629f6-d4bb-3134-a49b-b73a5c1f1f64 | -12.42875 | -54.87438 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81552d9f-575a-3bcc-8ec5-76dc90e33837 | -9.95593 | -64.99223 | 2025-06-20 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a814aa5c-8315-3f48-bc48-38b5f922870f | -16.31817 | -58.25929 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 58e76fbd-3a92-3423-9b59-d8429a3f2969 | -17.57579 | -47.49985 | 2025-06-20 04:53:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4905f7c8-fe2e-3682-8362-c9ba79f383b1 | -15.11431 | -54.65368 | 2025-06-20 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e2f2a17-3640-31e2-9b3e-e2e120e81357 | -16.31892 | -58.25498 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d7f5d756-7a8f-3a73-8775-e45631a6c6ac | -13.25928 | -46.81438 | 2025-06-20 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eae5a22e-fb6c-3394-8873-8923586f5e01 | -16.30772 | -58.26778 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c0cbecb0-8cbb-3956-8c14-fde5962a50a7 | -16.31383 | -58.26297 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 74f8277b-a4d2-3c97-859d-e4e65bc8a6f9 | -12.89656 | -56.98316 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bde178ac-9f22-38e6-957e-5e754cc0b479 | -15.47911 | -46.59158 | 2025-06-20 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 0a80203e-8bbf-3c65-aaad-9c148cc3d25d | -13.36572 | -54.26094 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 681a5de6-3d4a-3119-a86b-59e4cf71acfc | -12.90008 | -56.98377 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f47406-fc80-3cbe-a28f-bc9b761f3a76 | -11.95117 | -58.75594 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c04f436-a2d3-30de-8f24-df7d3322796a | -11.94506 | -58.74444 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5dcf6cdf-f0b2-30fc-a5de-077b84c01981 | -16.29981 | -58.27073 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f6538244-dcee-3133-9062-c8616693e1f4 | -14.48127 | -50.28744 | 2025-06-20 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21d9e96f-25a2-3349-a20a-32a75b127a51 | -13.09571 | -52.29197 | 2025-06-20 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c40c66-dd53-3edd-8c7e-abf3a5aeeea0 | -14.43654 | -48.91534 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bee7facc-1e14-3a79-992d-bcc0fddc4dc2 | -15.39945 | -47.81133 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 770196ee-ce28-3ae8-8a2d-34f8223ca12a | -11.13929 | -55.19139 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0b6c61d-2a10-3cd7-a892-e43d74ac12d6 | -11.13871 | -55.19501 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798b5fae-0eca-3459-88a3-55b5df482d6a | -14.03714 | -53.37016 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14f47c2e-fe68-3f52-888e-8f035956ab1c | -11.92005 | -54.8195 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8203a15-20c8-3bf3-8371-550e1a3e3321 | -12.47675 | -54.42235 | 2025-06-20 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6134c329-08b0-3192-ada6-2eb4622fb613 | -13.97833 | -58.10375 | 2025-06-20 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1979ada-00fa-37c9-b144-044bb9730446 | -14.81919 | -48.46537 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65c758f4-227c-32ca-81fb-baf0475a9cab | -10.66835 | -56.55397 | 2025-06-20 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e85af672-c3be-3a3b-8ded-110289907bb0 | -16.30589 | -58.26597 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c2033cd7-7e89-35da-8664-45a0988d933a | -12.34339 | -49.3048 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d2bc7e-154e-3e39-b63f-8c984213180e | -14.0388 | -53.3593 | 2025-06-20 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5098e158-0b4d-3de3-89a0-6d920ccd33f8 | -12.76715 | -44.41144 | 2025-06-20 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a90d8d-a72b-3be5-9d3a-eb0e2a5deccc | -12.55527 | -57.72035 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 188bdf7b-e79b-38c0-aaad-ba1e4091621b | -14.03546 | -53.35876 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fb12fc9-c89d-31b5-9fa6-3ae66bd4f6e0 | -9.95586 | -64.9898 | 2025-06-20 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ab40f00-37a5-3f9b-b9cf-4b0943e7f75c | -12.5065 | -58.35046 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3a92d63-eabc-3e27-b7ef-77f98704f157 | -14.04771 | -53.36814 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c95d5f3-4b74-39fc-96ee-cd1d21780cd9 | -12.5212 | -57.20801 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a270e36-6257-33d4-9d62-8ce1629d33b3 | -12.58087 | -56.98125 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23a4cc25-26fa-3ef9-add2-8a053188e184 | -11.91616 | -54.82251 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15da5c84-5e7e-3a54-a3a4-511d9b4bc266 | -13.77971 | -54.20246 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7af4b23-869c-3060-900a-821bb65ee712 | -16.30664 | -58.26167 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 65618985-ed86-3247-820c-dc089a2d5ba9 | -12.2304 | -54.29914 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf3793fd-6478-363f-a32c-34adea6d5f3e | -15.6234 | -57.30619 | 2025-06-20 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7eb1676-90c8-399e-8f22-7b764c5ae8a2 | -13.78026 | -54.19893 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e2491dd5-8c75-33fc-b022-e2611cc8332e | -14.02656 | -55.12144 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5225be-72fe-326b-b1ec-028f6811647a | -10.9388 | -55.33054 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fadffcd-81fb-3e69-93c0-ad88e1d6216d | -14.03825 | -53.36292 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8da4da65-c66d-3df0-a78b-1de114e55943 | -15.93519 | -57.67468 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9163622c-0ab6-3416-80b3-f71f40d1fe28 | -14.04214 | -53.35983 | 2025-06-20 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5abf9d9a-2cf8-394f-bb89-748222f0718e | -12.04143 | -63.7749 | 2025-06-20 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c63522-3ed0-30f9-b4ee-b39edffabcbe | -13.38987 | -48.45281 | 2025-06-20 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5cd01af-d7e4-395d-a119-246f38806397 | -11.82138 | -54.49891 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a09a68-a878-30d3-8a2d-69a72b0b7891 | -14.16973 | -60.05921 | 2025-06-20 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 444f520f-a787-3563-8cdb-f3fb036f3ec6 | -16.29767 | -58.26147 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6c6a212b-0a6a-3c3e-9bfe-75f9e9713807 | -11.08253 | -55.05228 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be7b95e6-4d44-3a4b-a30f-90d796fcdf2e | -12.76673 | -44.4151 | 2025-06-20 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5210a0-b5c3-31dc-8ca2-9db96dc9e02e | -15.62688 | -57.30677 | 2025-06-20 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0be893a5-a417-3799-8d1c-fb7867459bc7 | -12.49364 | -47.48097 | 2025-06-20 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e52eb3e-62f1-3747-9b22-c8d718d3aa81 | -16.30918 | -58.25916 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README21.md)
