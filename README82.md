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
| c92b4e6f-ebc5-3677-85b0-2cd9a00292a9 | -14.01307 | -43.85571 | 2025-10-06 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0123bcbc-8468-31eb-ae59-c6a7e7921601 | -13.63303 | -48.71609 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a109667c-faac-31e6-aab6-c5a50a83bb3e | -8.52382 | -46.38865 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eed51165-eaa2-3211-a017-7d6aad9106fa | -9.32674 | -40.43371 | 2025-10-06 12:00:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 23ed46df-e58f-3c33-a86f-4ace0415bcab | -14.35333 | -47.66937 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 098e967e-23ba-3a34-ae31-77b03a04f700 | -10.18206 | -45.99741 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d6316b2f-443a-308e-9e4f-1828e7ac2452 | -7.4642 | -43.034 | 2025-10-06 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 59c1ee2b-d15d-3c49-80e4-27301e8a7c55 | -16.43457 | -43.48668 | 2025-10-06 12:00:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ac172dcb-2670-38cf-9e8c-7d2cd37be3d2 | -15.04967 | -47.28215 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c92e88c4-76d8-359f-b950-8d417744fe85 | -15.5727 | -47.28574 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f690be7d-c6e9-3496-82b3-dfa7d890b40b | -13.58625 | -48.15552 | 2025-10-06 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 485db93d-b064-3706-bdcf-aed48f2d7128 | -14.69238 | -48.37169 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a11c4d3b-125b-3452-b118-0efa3e65097e | -7.68484 | -42.59716 | 2025-10-06 12:00:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 08c3883d-004f-3d55-9071-937ce428fe6e | -8.61355 | -46.26876 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 089285e9-9566-336f-a5ae-dc9855971c53 | -10.40992 | -45.38556 | 2025-10-06 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 13c5ded6-56ee-3e79-bc69-869b81feb468 | -8.21373 | -46.98929 | 2025-10-06 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2849cc93-cb23-34b3-bce4-7d57ea9efebe | -12.61756 | -43.17447 | 2025-10-06 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0496ac0f-0efa-36a8-be62-728ffa2ed9d7 | -14.87705 | -51.51086 | 2025-10-06 12:00:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 179.3 |
| d9b25159-8b65-39d0-96b5-b06b2dad5c2f | -7.2487 | -44.12378 | 2025-10-06 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c3a6254-6e4c-3e89-bc9c-d33a7342139c | -10.40833 | -45.39601 | 2025-10-06 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0a3c88b6-960d-30fd-b7f6-3380995fd14e | -12.15086 | -46.60179 | 2025-10-06 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 57280c12-5365-31e8-a5d0-1a6770f42114 | -13.22825 | -47.81534 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4d4c5a55-a52d-397d-af92-3ca408f1e899 | -12.44081 | -45.57335 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 77af1ee0-cc6c-36bf-9ea0-e169efd59563 | -11.2132 | -45.37679 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e0e0b51f-36a2-3aab-bc3e-d86c88619618 | -13.14036 | -42.07819 | 2025-10-06 12:00:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 5949a22c-2f21-3817-86d0-97a30ee8ed00 | -11.11103 | -47.23471 | 2025-10-06 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| cc0bff73-90a1-38be-af8b-fcb336b3866f | -16.63988 | -43.20298 | 2025-10-06 12:00:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| df434a14-65c3-3ce6-b918-afb4ce664937 | -14.0084 | -43.76266 | 2025-10-06 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b2d8283f-2763-32a7-a003-a1373c6c7449 | -14.56161 | -46.66706 | 2025-10-06 12:00:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 592a042a-ce82-313d-864b-2c9b4a8cb875 | -16.63454 | -42.23555 | 2025-10-06 12:00:00 | TERRA_M-T | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 145409cb-7757-348f-a9ea-295a6cadb031 | -9.37237 | -42.4048 | 2025-10-06 12:00:00 | TERRA_M-T | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b1278835-7b40-38c8-a0ae-8b56e7f68ffa | -11.11752 | -47.22919 | 2025-10-06 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 72a75d92-9a2e-3853-ba95-4dcf11fe8e03 | -15.75265 | -46.25404 | 2025-10-06 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ce62e08e-0d1a-3dfa-9116-d9a4d48da509 | -13.25899 | -48.46619 | 2025-10-06 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0c62cccf-5dba-3332-9dbf-92884eb71ee4 | -14.56623 | -46.97095 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1b5355e6-796b-3d2d-a74a-a630368efe76 | -14.28842 | -45.85854 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 72086176-b327-3cf1-80bb-d9a12ac829a8 | -13.10288 | -47.9935 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b59fdf0a-5b36-3011-ab3b-7da4a6e57a12 | -12.70273 | -45.86288 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 3ef0d0b3-b548-3b24-9fe3-3ab60a27af0e | -16.69458 | -41.0137 | 2025-10-06 12:00:00 | TERRA_M-T | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 58385b96-e88e-34e4-b343-8031904129ff | -7.70531 | -42.39243 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9dd8c205-2847-3923-b88b-c4d9b5a6b4b2 | -11.20673 | -45.37977 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0cac18b0-f1ce-3908-a037-623ceeefe01a | -12.9038 | -47.29535 | 2025-10-06 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6640cb59-2bcc-3dc6-9fec-bf168081c00e | -15.56546 | -41.62104 | 2025-10-06 12:00:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3f8dc3a2-7820-3007-8319-2c8d33334acb | -9.17685 | -43.06062 | 2025-10-06 12:00:00 | TERRA_M-T | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 25e8868d-d2b5-3b81-b12d-4a4763f93d0f | -14.69682 | -45.17585 | 2025-10-06 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2cffa361-0289-3256-828e-71633babc415 | -14.46791 | -46.33107 | 2025-10-06 12:00:00 | TERRA_M-T | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 957e0225-a4ef-37e4-8d47-5c0633e388d5 | -13.23683 | -48.46154 | 2025-10-06 12:00:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8436f7f5-812b-397b-9bab-6070a7855457 | -13.2711 | -47.17551 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| add92950-b283-3e84-af39-443843b90776 | -13.36494 | -47.56737 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 294c5ea6-e8e1-3bc1-aa40-854804be9e25 | -14.27915 | -45.85714 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| e8a326d1-d02b-3681-9d41-15f0a7c38766 | -14.91236 | -46.84995 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9c7ca8ae-02f1-3969-ada6-533cba6f9402 | -17.41375 | -42.64729 | 2025-10-06 12:00:00 | TERRA_M-T | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c98c9c3-bce9-3141-bb72-883be1c7b8ee | -7.85942 | -47.26214 | 2025-10-06 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c21aabf0-1794-3c71-bbbe-3c7864ad74fc | -14.56501 | -46.64526 | 2025-10-06 12:00:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aec24717-506f-3e6b-9e73-b4904e335ca7 | -13.3414 | -47.18278 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| daa91528-1612-3741-8ded-66a7a5772f54 | -9.41189 | -47.94559 | 2025-10-06 12:00:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 056dc7d4-bf55-3e6c-acfd-ddc4e170a177 | -12.23705 | -43.77058 | 2025-10-06 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ceab2973-06f8-38c9-ada4-01bf67633cf6 | -15.36191 | -47.32195 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 999b6f7a-eaaf-3d01-9dd6-9cffaeb63815 | -14.56012 | -46.99889 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1cfdacd0-ed14-3454-a8ce-df2756827aa6 | -12.44862 | -45.58491 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b771ac7-4c24-3002-9ba0-1cef76276ba3 | -13.57461 | -42.46658 | 2025-10-06 12:00:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 19a1f848-eaee-3b00-a08f-f418c799a4dc | -8.09004 | -44.79408 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 5823e1cd-0a59-3f10-888b-b0ebe9e21f07 | -7.63076 | -44.35326 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 221ce151-a833-36b2-bc80-565326cd9b72 | -9.49697 | -45.98971 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 67bc7a84-b33e-381b-a302-9dad2df332e4 | -14.53594 | -46.95985 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 721a5eba-afdc-3d86-a3ea-bcd1ece86da6 | -7.78565 | -42.5998 | 2025-10-06 12:00:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 268c91d8-5eca-397b-89ed-9881bb98e297 | -8.0822 | -44.78229 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d1e75ed9-37c8-355e-8393-f88512e9c2c3 | -7.63221 | -44.34346 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f8e5117d-7e22-3602-aea3-d28a7fe1a30b | -9.48704 | -45.98824 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 99de1586-37eb-33b5-a8a9-5ab635b06fdc | -10.62091 | -46.34935 | 2025-10-06 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8111e9e6-101f-338d-8fd5-68ffe396058a | -15.337 | -45.52402 | 2025-10-06 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d5cbe42c-af10-3a19-baab-29ec911df6d8 | -17.60657 | -44.44755 | 2025-10-06 12:00:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6bf58a66-5988-39d7-b2de-d9d2c63708b2 | -14.62996 | -48.11749 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a8e1b836-6c59-3f50-80f8-d3039c635389 | -15.17071 | -45.7695 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 0a70c663-a998-3c8e-91d1-39e092b65d99 | -13.13902 | -42.08785 | 2025-10-06 12:00:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 47.9 |
| c40da59e-6579-32b2-96d6-a41ec66f5183 | -13.25176 | -47.80485 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 945390ad-9ad6-3991-ab0c-80b381700af4 | -14.56441 | -46.98233 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 54944e3a-16e5-3d05-9c57-420b4f7884e5 | -15.36385 | -47.30985 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 13e3446f-6f33-3c5a-b5d1-6c94a9ee00ca | -15.53429 | -41.99921 | 2025-10-06 12:00:00 | TERRA_M-T | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 398e5d4b-c92e-399c-8ec2-4e5bb016ec63 | -13.26869 | -47.83506 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1c08718b-e11f-3dfa-b144-1cf6680d92c9 | -8.8799 | -44.20551 | 2025-10-06 12:00:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c7368c6d-9ebe-3ac2-a686-5e57533af49a | -15.20975 | -46.37105 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5ebe8fdf-10f8-39fc-aa3d-a850ae2c94dc | -8.52301 | -46.32495 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b90711c3-8e28-35a1-a819-c1b4a90408b2 | -14.91415 | -46.83847 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d274d904-3a42-393a-982f-bd729dd0d981 | -12.48641 | -45.56626 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| c1edb02f-ae02-3e56-bdb5-7682a9a72a87 | -7.21382 | -45.90816 | 2025-10-06 12:00:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 47c032e8-7221-379f-99b6-5a3bb9ebe852 | -15.22441 | -49.27891 | 2025-10-06 12:00:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 57bea727-fbd8-39b4-b092-fdb68cc5bcca | -12.45469 | -45.54454 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3b0c93f7-4e4a-3855-bfba-58f24061c2be | -14.55381 | -46.97447 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9a83aad1-9574-30cc-8058-fa6d680cab0e | -9.84986 | -45.75309 | 2025-10-06 12:00:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8c138d1c-0285-3aaf-a20a-1b25a4c3e10b | -15.51553 | -44.3063 | 2025-10-06 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 62189eaa-7c15-346c-8a37-471dd40371f6 | -7.26048 | -46.96089 | 2025-10-06 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 815d09e4-fb80-3435-9bcb-3094bdda4af9 | -15.5844 | -47.2757 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f4687173-eebc-341d-b779-5b65367aec39 | -14.56188 | -46.98748 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 510.7 |
| 789a2e52-3e8e-3c08-9111-97417b460f1d | -8.18334 | -44.23383 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d9a22210-71d8-3847-a5e1-128c14a4d610 | -13.35154 | -47.18446 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0b37c3f8-81ed-3ee4-9963-93d01fb0a8da | -8.46108 | -47.24888 | 2025-10-06 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ff8856e2-d5da-31a8-be71-1aba4c7e6491 | -12.70879 | -45.85935 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 42d09c22-3ffe-3b23-9bad-17d1b7e304c0 | -16.40577 | -48.98299 | 2025-10-06 12:00:00 | TERRA_M-T | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 96448194-0064-3e1c-b791-7e91dfc1724c | -13.26242 | -47.80628 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README83.md)
