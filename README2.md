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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1536e7b-a46a-3187-968d-d1d3352e4dde | -14.45322 | -45.66179 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb122432-7aac-3fc4-b1c8-af040c222d1c | -14.43215 | -45.63575 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d6dd263-6ce4-3c8b-8ecd-9585e028866e | -14.13562 | -41.69144 | 2025-02-21 03:44:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9edd4c2-9480-3427-8852-229c0559fc8c | -15.73064 | -43.14748 | 2025-02-21 03:44:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 262517d8-176a-30c7-bd52-5220c13254ec | -12.80188 | -45.01165 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c42ffb0-8fea-30af-8ba4-15d1833ae0f1 | -14.45685 | -45.66544 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6705ff22-5f91-3f24-872e-5c284a5724d6 | -12.79857 | -45.00192 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3282394-ddcc-3171-a4a8-668c9bb3dcc8 | -14.45269 | -47.91072 | 2025-02-21 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bea1f04d-293f-3590-ad49-d7c0018d9826 | -14.4416 | -45.64076 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c80e76-a624-3beb-9817-4eebd0eed1c0 | -16.10049 | -39.07517 | 2025-02-21 03:44:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6b6bee3b-b102-38ee-8834-23dcbb6fd374 | -14.83755 | -45.19638 | 2025-02-21 03:44:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ae0108-60ca-353a-b5f0-6e262aa3a7fe | -14.45242 | -45.66145 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d53e625-3ad4-3f1a-a521-20122b6587e8 | -11.85499 | -46.93955 | 2025-02-21 03:44:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdeca3e4-eed4-3236-9911-14c9d9d77a27 | -11.1306 | -38.53115 | 2025-02-21 03:44:00 | NOAA-21 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 125075ab-0bc2-318f-bd88-de48becb8cd5 | -12.80298 | -45.00584 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0644b6f9-1604-3110-baca-4dd2106f1f5e | -14.22949 | -42.77183 | 2025-02-21 03:44:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19060984-7ae2-3aeb-b65d-46cfa7b1f602 | -16.34758 | -43.69781 | 2025-02-21 03:44:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978d2304-9c64-32dd-b1a4-2dc28f8db20e | -14.45263 | -47.90954 | 2025-02-21 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 688f13b8-d664-3eb3-a9d9-a5a63c9b5013 | -14.43099 | -45.64176 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b11d5584-1ef0-3b23-b9f2-e617052930fd | -14.45847 | -47.91051 | 2025-02-21 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b73d7f6-a0ce-3d91-b3bd-47a01b51a1df | -14.45265 | -45.66481 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf214057-4b4a-3981-8863-7baea660f982 | -11.86072 | -46.94057 | 2025-02-21 03:44:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 798c6b27-18c4-3305-bd77-54c0909d7b23 | -14.43659 | -45.63976 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31049346-13b4-395e-b1b2-3e48c730cf96 | -12.35219 | -47.99013 | 2025-02-21 03:44:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 811442a4-8df9-3bfa-9750-59b4219d8e3f | -14.42771 | -45.63176 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00beaf78-6c8c-3d30-a95c-4b93f097fe77 | -12.35124 | -47.99472 | 2025-02-21 03:44:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8377a71-b664-3ed4-9a5e-17686812ecbd | -14.44045 | -45.64677 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23335b16-f52a-3a39-931b-39ae29d41176 | -14.42713 | -45.63477 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa32fe8f-fa55-3d66-857c-dcbf21141da6 | -14.43601 | -45.64276 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdf724c7-ac6e-383c-ae74-8c8b6b2d7b04 | -14.43543 | -45.64576 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0807f01-61c7-36e2-afbc-40622de8d082 | -16.34972 | -43.69499 | 2025-02-21 03:44:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26a166f9-66f5-3ea0-add1-13909043dea4 | -12.56088 | -44.74711 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afe979fc-bcbe-3e18-b458-b469dbfe49ce | -14.42886 | -45.62575 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1085eaa-0e22-3035-b8bb-58bb06e4f5cc | -12.86218 | -38.36612 | 2025-02-21 03:44:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc940550-4b5f-3659-b984-a8abcfd67b4b | -9.92914 | -37.23875 | 2025-02-21 03:44:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d56a4a9d-20f4-37fb-897a-35abce5ea4a7 | -14.45744 | -45.66244 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22145790-c636-3703-a17b-cd98a279b37c | -14.45825 | -45.6628 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fbab4a9-3bda-3132-9346-07e2ca4cfac7 | -14.22821 | -42.77242 | 2025-02-21 03:44:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a803a5e-a6b6-3bf3-8020-ef17e68e423c | -14.44103 | -45.64376 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d69a8d5-3177-3d81-87ce-2076a8a36e5b | -13.8256 | -40.47543 | 2025-02-21 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a3f5328-c190-3494-b88e-ea32aad266c5 | -12.35009 | -47.99456 | 2025-02-21 03:44:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 627ef4ee-39ff-385b-a5ac-4de3c066655f | -12.79803 | -45.00483 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 226f3c9c-301d-3ee2-a0a4-ee65c9a97c49 | -14.45767 | -45.66581 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 756c1973-5a54-3f4a-9b8d-15c84aace7ff | -18.63693 | -43.17067 | 2025-02-21 03:46:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cb8d9f8f-ffc8-37b9-bd0c-f1362993e482 | -20.19947 | -46.52836 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 769b5667-3f83-37b5-8f47-21d2bf531aaf | -22.84853 | -42.76897 | 2025-02-21 03:46:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1af6c0bb-028b-3a51-8c41-fddb996afef3 | -18.6343 | -43.17363 | 2025-02-21 03:46:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f9424863-e547-329f-bc92-f8eb321c40c8 | -17.67683 | -42.74245 | 2025-02-21 03:46:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae804dd9-e744-3cd5-b6f3-07ac72f28437 | -18.60979 | -44.25596 | 2025-02-21 03:46:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b93f9b6-add7-3c71-bca1-47722e3893ca | -22.69779 | -43.34735 | 2025-02-21 03:46:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2629b5a1-f20e-3b9d-82f7-c59005d17b55 | -18.63493 | -43.1702 | 2025-02-21 03:46:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bccc6aa8-275a-3770-b471-8e39f05a5868 | -20.20301 | -46.53539 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8159658-7116-3a66-beda-1bfa5ed598b3 | -19.19907 | -40.63191 | 2025-02-21 03:46:00 | NOAA-21 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 82857f59-fb29-383d-ae60-70f0c5625964 | -19.71869 | -40.3523 | 2025-02-21 03:46:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd64f3e0-966a-3faf-85d0-5c413c7c28de | -20.41574 | -41.36033 | 2025-02-21 03:46:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 870898cf-1b8a-360b-b3da-a1eaa877eb81 | -18.76088 | -40.00021 | 2025-02-21 03:46:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30e753ff-b450-346b-8166-52c3d5bf2a17 | -22.92777 | -42.45461 | 2025-02-21 03:46:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a39e462a-b925-33d6-9372-4c05838455cc | -20.20068 | -46.52251 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b3b0480-19a8-3350-9e69-cf6cf61b8485 | -20.30021 | -46.49786 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bbd7517-b823-3a1b-b573-6fa8a7a6e451 | -18.0704 | -39.64783 | 2025-02-21 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 50e5f281-6c92-3f36-9452-06fcf79c4a30 | -17.05128 | -45.03759 | 2025-02-21 03:46:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7588fdbf-b39b-3d99-badb-4a10ed3dfc23 | -17.46382 | -39.27652 | 2025-02-21 03:46:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6b4525d-772d-3a97-a2d0-ae085ae212a4 | -16.67999 | -43.88272 | 2025-02-21 03:46:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd8c7a48-05a6-322e-92a4-5dac0b400613 | -22.90119 | -43.75276 | 2025-02-21 03:46:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8062d122-7582-3ada-bf57-176a7c1d3e15 | -20.19829 | -46.53411 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bfab0cb2-e289-327d-88d4-bfe6b8484c76 | -20.99784 | -44.16019 | 2025-02-21 03:46:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a9a17b5-92d2-3d4f-abbb-f2a91c430cb0 | -20.94523 | -43.00515 | 2025-02-21 03:46:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 46ffa197-f6cc-3670-9fd3-e91601fdde57 | -20.45533 | -43.27565 | 2025-02-21 03:46:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c42f2836-3a54-3423-9432-98a5b7e0b4b3 | -21.9843 | -44.52226 | 2025-02-21 03:46:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3e275854-9bcc-32d3-83cf-761691f4cfd9 | -17.05495 | -45.04338 | 2025-02-21 03:46:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a20c462-4091-380a-8f8c-845cd2e42ac3 | -21.9138 | -42.26299 | 2025-02-21 03:46:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 554c940b-8a63-3206-b3bf-22b892ec1f38 | -17.05033 | -45.04254 | 2025-02-21 03:46:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2847e888-5865-31c9-bfde-a97399c0b829 | -17.46196 | -47.01624 | 2025-02-21 03:46:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd49b997-eadc-3ea0-bf6e-7da1f347c822 | -20.30954 | -46.50074 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1aa53e2-dda7-337a-b6c3-1b81d5cf897d | -21.98487 | -44.52208 | 2025-02-21 03:46:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 566af0d9-9bde-311c-96cd-a1e188a0e35f | -20.3472 | -40.36123 | 2025-02-21 03:46:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 56af8d5a-6751-3b06-bc88-f9867e393d31 | -20.7666 | -46.76905 | 2025-02-21 03:46:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15a3fd6e-1888-30a1-94c6-6971cb9efbb7 | -20.30495 | -46.49895 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddfcd998-1558-3484-8841-d9f996dfb27e | -22.78701 | -43.75735 | 2025-02-21 03:46:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e763b713-084f-3afb-8610-d835444410cc | -20.1984 | -43.28722 | 2025-02-21 03:46:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2efe2904-a52a-37e5-be72-7d1695f06f8d | -20.1924 | -46.53853 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73ec3551-7e98-30de-a5c4-0bcefbbfacb4 | -17.46333 | -47.00964 | 2025-02-21 03:46:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b1f550e-f098-3c0b-8312-d236cf1e240f | -18.63629 | -43.17411 | 2025-02-21 03:46:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| dbf08bed-87e2-3f78-b18d-2087181cbafa | -17.45816 | -47.00854 | 2025-02-21 03:46:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f85aa45-fe11-3499-9921-b316adb5d4d6 | -18.58404 | -39.83747 | 2025-02-21 03:46:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 91df5635-0a9c-3f25-af53-bb6f110c5294 | -18.67203 | -44.59708 | 2025-02-21 03:46:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a07431f-92a5-3de9-a4cd-422b817cdf42 | -22.23087 | -42.19831 | 2025-02-21 03:46:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8244d62-da8a-3a75-bced-d1d7870dd83c | -23.33811 | -46.77168 | 2025-02-21 03:46:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3776a783-73a1-3624-affc-66f0b9c86e94 | -20.7655 | -46.7707 | 2025-02-21 03:46:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 061541bc-7ffe-3f3b-9760-de58ce8e5f5d | -20.30135 | -46.49236 | 2025-02-21 03:46:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a4bcdb6-f268-34bd-90d8-e0c906305699 | -19.86504 | -40.31876 | 2025-02-21 03:46:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14660917-05b8-3f00-8122-668d57ac1733 | -20.45922 | -43.27639 | 2025-02-21 03:46:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5ebf161f-484c-385a-b623-aab0dcd4ec77 | -28.58765 | -49.44279 | 2025-02-21 03:49:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc40c412-1088-3ba4-b5b9-e7dfd5b348b1 | -29.77997 | -51.17469 | 2025-02-21 03:51:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 2b1a4de2-94ba-3656-8daf-874f5e99a391 | -29.77849 | -51.17831 | 2025-02-21 03:51:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 1283769c-01ba-344e-a9f1-a751ee2fddd8 | -29.7791 | -51.1783 | 2025-02-21 03:51:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9facfc37-b92f-3177-898c-28bb85ea2b13 | -29.77934 | -51.1747 | 2025-02-21 03:51:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 7c106ff2-db6f-3520-9e8c-ce4c986be7e4 | -6.4859 | -35.0065 | 2025-02-21 04:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 179.9 |
| c129c028-54c0-3b37-a5a2-b5fdf44d325b | -6.4862 | -34.9789 | 2025-02-21 04:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 145.6 |
| 5facac29-0c15-3951-92a7-4124c112e825 | -6.4668 | -35.0088 | 2025-02-21 04:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 258.7 |


[Clique aqui para ver as próximas entradas](README3.md)
