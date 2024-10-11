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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d91f2170-5738-351b-911b-57e3a23c4941 | -9.53246 | -42.98888 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 72909173-d590-301d-9cae-730e5a8fade1 | -9.52353 | -43.00542 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 919622cf-c166-3358-a691-70ebb547246b | -9.52345 | -42.99886 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 81.1 |
| f6b43cd0-7381-3af5-88b0-aec992ed638e | -9.52132 | -42.99079 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 1cc43528-4410-3aeb-a261-1c98ec86cad7 | -9.52112 | -42.98415 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 97a10635-daf6-3eed-8f29-a869c0dcf374 | -10.30097 | -43.41925 | 2024-10-11 00:54:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e118437b-8c72-31e0-954c-3fdef483d989 | -12.23327 | -44.39949 | 2024-10-11 00:54:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cee0c7ba-73a8-3c4a-905a-fdc1b632059d | -12.23161 | -44.3886 | 2024-10-11 00:54:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cf5f6fd2-8d72-3ff5-81cb-e3412a8259e4 | -12.2295 | -44.39477 | 2024-10-11 00:54:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d7df8c87-06e1-320b-8492-edb8dff4a698 | -11.89864 | -43.89047 | 2024-10-11 00:54:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0aa46ed9-1744-352e-affe-1ac35a41c117 | -11.78718 | -44.49965 | 2024-10-11 00:54:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a5bb6703-1f24-3215-9a46-0ceb11a8cda8 | -13.37386 | -44.78473 | 2024-10-11 00:54:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0db10cb2-22d6-33aa-8aaa-d8f86019234b | -13.37236 | -44.77454 | 2024-10-11 00:54:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d8ad3394-f899-392e-ada9-24b966424bc0 | -13.36452 | -44.78625 | 2024-10-11 00:54:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cef9ea1d-3a37-3ec9-93b1-cb5d93db8a75 | -13.36303 | -44.77611 | 2024-10-11 00:54:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cdb368bf-fdc7-3cba-a164-384adc9e7503 | -13.11766 | -44.08321 | 2024-10-11 00:54:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d574d8d8-f6e1-3552-9fe3-2511af076c81 | -13.11596 | -44.07212 | 2024-10-11 00:54:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cd8c6098-fcdf-3bf0-8845-91e575e5adf1 | -12.84888 | -44.61455 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9239d39-eed3-3ca1-ad8c-a3e269a3a667 | -12.7888 | -44.89365 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fb553555-b543-3ba0-8183-52dc839df3e9 | -12.78728 | -44.88349 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f4341ed3-9bbd-3041-94b5-52c9d7c4fc5d | -12.78577 | -44.87336 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 60179f03-34e9-3f95-a15c-37614e2d9ad2 | -12.77945 | -44.89509 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 69e32a9e-14a8-3c57-9cd8-6e370fdc030f | -12.77794 | -44.88498 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 35ad8743-d982-3eb9-935d-076ac2b9eb40 | -12.77642 | -44.87483 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e9407cf0-002d-38a5-b085-61fa0e9a231e | -12.7749 | -44.86465 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3d42a4c3-9c8f-363a-8f06-46333b92da16 | -12.77163 | -44.90666 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3925b343-aaf8-374a-8f91-c54173468a96 | -12.76859 | -44.88646 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 966.7 |
| 1964b5a4-eb25-3856-aefd-1171ab125621 | -12.76707 | -44.8763 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1917.0 |
| 8fe8f550-ad9c-3efb-a9c0-733fd35f508a | -12.76638 | -44.91376 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 11a04acf-6992-3224-bc7c-668ef3dba444 | -12.76554 | -44.86613 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 0248fe6b-605a-3633-90b4-c78dd7595602 | -12.7649 | -44.90365 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cb337584-d1d3-3aa0-ab80-be1f4d9ea2e0 | -12.76343 | -44.89354 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8c9b58c0-1b13-363b-a1b8-dea73edc5499 | -12.76195 | -44.88339 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1005.8 |
| 94bdb33e-e765-3e50-9562-5cea50fa779c | -12.76046 | -44.8732 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 701.0 |
| 0d9df5dd-93f8-378e-ad0c-3697118232d4 | -12.75898 | -44.863 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3ee009f5-789c-3f0f-a5ae-4eaad4c92cb9 | -12.75408 | -44.89503 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0aa56f66-32ba-3e46-b4b8-ee03e670ca96 | -12.7526 | -44.88487 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f94c0cc2-b852-3ae3-b815-d7a9f3ab8281 | -12.75111 | -44.87467 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 06961769-fac2-3d3a-b359-c184030ae4c0 | -12.74961 | -44.86447 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ff64bd7-6092-3c9e-bf77-011f62b900d3 | -12.58761 | -43.36911 | 2024-10-11 00:54:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 214551e1-6311-38c9-9ddb-835c1d929b6b | -12.42959 | -43.74367 | 2024-10-11 00:54:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0af98f53-46f6-319f-a63a-f1a174575bde | -12.35877 | -43.74969 | 2024-10-11 00:54:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 65030e96-62a5-3e2d-ac6d-afdddc28d76d | -12.3506 | -43.76358 | 2024-10-11 00:54:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 72173cd5-60e8-38a6-bf4c-6e792132133a | -12.34876 | -43.7516 | 2024-10-11 00:54:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7e34c5b6-9e48-3d7c-9a29-99cd402e5e87 | -14.18662 | -44.37158 | 2024-10-11 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77b4871c-b3d8-30a2-a0d5-369c6cbb157c | -14.08914 | -44.14387 | 2024-10-11 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2f6ef973-5015-340e-8719-a25f48157538 | -14.08752 | -44.13311 | 2024-10-11 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 246fe90a-2255-3ac1-8f1b-7c563760caf8 | -14.06888 | -44.94322 | 2024-10-11 00:54:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 483f8ee4-bfb8-3be5-b84a-2e9726ef492e | -14.04389 | -44.04024 | 2024-10-11 00:54:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25a3a9e4-d40f-3655-8323-7e02f4f707f1 | -13.92554 | -43.80403 | 2024-10-11 00:54:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a09b3d26-4aff-35c1-9ff4-b279cc4a5a1e | -13.91748 | -43.8169 | 2024-10-11 00:54:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7ab0d7f3-6e04-3f96-aab1-07c75f4119cd | -12.31745 | -45.32042 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 81992ae3-8050-3ce3-a4ff-4aafac764227 | -12.31601 | -45.31061 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| dabdb185-8609-3022-a415-9f92a212911f | -12.31457 | -45.30077 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e8b718e2-6198-31d1-b094-40dbabdcaf81 | -12.30679 | -45.31198 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 44839ec5-1fbd-3c59-9a3d-24cc70d4eef2 | -12.30535 | -45.30217 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 34b71515-128a-3244-b08f-827e26d0e9ce | -12.27273 | -45.32367 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2103096-9d81-3b4f-9356-5bc22d1af214 | -12.2713 | -45.31377 | 2024-10-11 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3299baa1-305f-3f10-8346-557077f23946 | -12.96008 | -46.19004 | 2024-10-11 00:54:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2a24a49f-91da-3cb6-9b57-c66b0b67270c | -10.47365 | -46.79017 | 2024-10-11 00:54:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e6432cc1-9d45-3623-b271-b1b31497c1ed | -10.47235 | -46.78111 | 2024-10-11 00:54:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5ce9d4e5-cccb-33cb-8010-a6bd96cc08bb | -10.46346 | -46.78246 | 2024-10-11 00:54:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8ccffffd-ddba-3d32-b092-9537ba0bb335 | -12.21791 | -47.13927 | 2024-10-11 00:54:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 546d7f09-a722-38c5-bd31-cba526fb53f5 | -12.21666 | -47.13028 | 2024-10-11 00:54:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c3dbaf6-40a9-385f-98f6-8d1c11e50ff3 | -11.39533 | -47.18736 | 2024-10-11 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eccc6463-e1eb-319f-a586-6e5f91dc8067 | -10.6322 | -47.85614 | 2024-10-11 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e39e45b1-37d7-3508-a56f-e2eb0aff2a16 | -10.63097 | -47.8472 | 2024-10-11 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 83ceabcd-f3a9-3e6d-add5-e298725c160a | -10.61237 | -47.7129 | 2024-10-11 00:54:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 979cf8ff-3538-39ef-97f0-2754cc6c8ee2 | -10.61113 | -47.70396 | 2024-10-11 00:54:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8d15e250-4d14-38a3-8558-15d50a951101 | -10.60229 | -47.70524 | 2024-10-11 00:54:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be2f0933-bf86-3b90-b191-103dda415a07 | -10.62212 | -47.84849 | 2024-10-11 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 411b67ab-a80d-3b18-84ee-546e3b5627c1 | -11.68527 | -48.48976 | 2024-10-11 00:54:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ec1e594-8ba1-31f8-9893-19fe29f5980a | -10.93689 | -47.9312 | 2024-10-11 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb0c8d2a-f9d5-33e3-8796-7d1080e6a9e7 | -10.54581 | -49.95134 | 2024-10-11 00:54:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e50c65c4-948a-3fa6-b67e-54fe4d19fe42 | -11.25927 | -50.97152 | 2024-10-11 00:54:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e8515ca6-cdf9-31c8-adf1-d6a79156b1e4 | -10.89535 | -52.34649 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 0cb6ee76-8edb-3773-a697-bc545051f201 | -10.89347 | -52.33159 | 2024-10-11 00:54:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a573892e-413a-3dcf-8a52-d1d1a08f8214 | -11.26008 | -53.26918 | 2024-10-11 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e007d81c-541c-3224-8ee1-d04780fb2a22 | -11.24785 | -53.27072 | 2024-10-11 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 23a7bd97-36c3-3b4a-8fb5-b0a7bc379c8a | -2.6533 | -53.3506 | 2024-10-11 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 20a49545-207e-32b0-9919-789602208bbc | -2.6716 | -53.3502 | 2024-10-11 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 7fecfa28-49f1-39ff-93eb-df32562734ac | -2.7663 | -52.4937 | 2024-10-11 00:55:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e983b014-d94f-31cb-81cd-596b489109aa | -2.7664 | -52.4733 | 2024-10-11 00:55:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e4d5c0e4-4051-3e2d-aa3d-33cf627bab9f | -2.7847 | -52.4933 | 2024-10-11 00:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 1aa30045-b7d8-355a-96ce-468f780d2899 | -2.7848 | -52.4728 | 2024-10-11 00:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 365b606e-1a83-3d25-acec-c090091f016d | -2.9673 | -52.9169 | 2024-10-11 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 12958de5-1723-35ba-9465-5e1d9d7751ff | -2.9673 | -52.8966 | 2024-10-11 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| ee883d83-b555-3870-aaeb-95c5d7ec54e1 | -2.9728 | -51.3568 | 2024-10-11 00:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 597cc2e4-7e25-3629-996a-38cdf4588210 | -2.9857 | -52.9164 | 2024-10-11 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 5b5777ac-e335-3192-a9b4-a048f2ec7717 | -2.9857 | -52.8961 | 2024-10-11 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 5aad50b1-0180-314f-9e9d-e12bd0b0e91c | -3.0343 | -61.6918 | 2024-10-11 00:55:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 701bab44-5e8c-33b8-aac7-db1b9638d6a2 | -3.0343 | -61.673 | 2024-10-11 00:55:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a3c4e3cf-5e0b-3b7d-b11f-b6007a335344 | -3.0525 | -61.6916 | 2024-10-11 00:55:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 32435d8d-34af-365b-8c2c-8c5681c1b986 | -3.0525 | -61.6727 | 2024-10-11 00:55:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a582776d-a7d4-37a5-8940-62e779f2dbe6 | -3.1422 | -50.4562 | 2024-10-11 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fa9975d6-e10b-36c4-8ad6-5756f72f812b | -3.1423 | -50.4352 | 2024-10-11 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| fe3b8fbf-f3fc-39b0-b8aa-b4c1ba1ea1a8 | -3.1607 | -50.4556 | 2024-10-11 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| df1f2d5a-03a4-3147-bc06-13271baf1096 | -3.1608 | -50.4347 | 2024-10-11 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| fcab08b2-d571-3944-90f5-ba9a3cf9551e | -3.2911 | -46.0954 | 2024-10-11 00:55:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 587f839e-55d2-3586-b5aa-89d4d298cf29 | -3.2912 | -46.0731 | 2024-10-11 00:55:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |


[Clique aqui para ver as próximas entradas](README15.md)
