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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326bc60d-7bd3-3e13-82b8-b7a2a3694bbf | -13.64303 | -47.03909 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13b9c930-2217-36ef-a022-4ee7920eee2c | -17.03781 | -47.05397 | 2025-10-29 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2402134d-b0da-3515-9604-eae3c790f454 | -19.33252 | -43.0564 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 08b936c6-937f-3ca5-82d1-5b2ce8b23bcc | -13.38016 | -47.40843 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd64b2b5-82c9-3d5a-b4bf-4bc4f049fe24 | -12.43975 | -43.75652 | 2025-10-29 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5da393d1-5971-3510-b8a1-948376442725 | -11.97206 | -43.29068 | 2025-10-29 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d0b6878-2912-390e-a8ec-b5f8fb8a7fab | -14.23519 | -48.11804 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f67c227a-8198-397e-ada4-46b638a7e378 | -13.64716 | -46.4622 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247d98fb-3971-3dd5-8860-b17686c2e66c | -18.19913 | -44.33615 | 2025-10-29 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dd5332f-fa52-3334-ab31-4cb45a123507 | -13.62222 | -46.46899 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 577c4b62-d3bb-3f1f-a483-ad51fd40d930 | -13.20839 | -47.79361 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74e3a033-015f-3b1e-a493-7571d594bb60 | -13.3612 | -47.38732 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d19f4b1-7754-3dd4-8054-fd77d5347a92 | -12.52345 | -44.89017 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7245cd80-aef1-36db-b75e-2c01a9b39b53 | -17.47962 | -44.06607 | 2025-10-29 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3039e88-f55c-33b2-a4cb-da9c16947767 | -11.73503 | -49.33013 | 2025-10-29 04:25:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0196b96e-32ba-307f-9f48-9fea70293822 | -13.30851 | -47.0751 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc1ace2b-78e3-39eb-a7e7-29edd8038ad3 | -13.91271 | -48.46378 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5324fff5-8e76-31fc-96ae-c33ce951f144 | -12.09783 | -47.16273 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b55b1a76-4b5c-30d3-a0a6-c8ae23818754 | -12.00666 | -46.77937 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5160fb5a-be46-3a90-9f6c-fa51b5456e3c | -10.85064 | -49.14417 | 2025-10-29 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95c2d795-a5a3-3035-821d-bd51537868bc | -14.27934 | -47.31404 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 136471b4-4386-314d-892d-510839584f45 | -12.97765 | -48.39127 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa1fd334-9ab6-38d8-9b1e-4258ed453f32 | -15.0962 | -43.84037 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 96716b05-4862-3574-a0ff-c121eea9e57f | -13.94513 | -48.48191 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e34499-7188-3ce7-a076-abb6b1325999 | -18.92687 | -45.05313 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 842cdeab-3e6d-3c61-8f46-b457f2e3c0d8 | -13.55333 | -47.3263 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4adc8827-8572-344c-bd16-84a0ec40553e | -11.41764 | -51.40438 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 276fe2e0-33e8-3c17-9243-6a6b0ef585f9 | -13.57396 | -49.61353 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aaea5864-1b7b-3e71-8391-7b359327523d | -14.48193 | -45.26328 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 983cd7ef-e59a-3b6d-9ba3-baec6fa20db6 | -12.40729 | -44.71507 | 2025-10-29 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e45638f4-7de9-35e0-a1f2-6fe5324b9a6e | -13.60876 | -46.47431 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffdd8c77-20d8-3b8d-b9dd-44d6136bb171 | -13.54605 | -47.32878 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3a39517-ce14-3ea6-8644-bbf69b7d75a5 | -13.54998 | -47.32576 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15e89842-fe85-3488-9614-b3d8f49d823e | -11.35546 | -47.02219 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62a73b24-9d52-34ae-8a0e-1726e5f0d8b6 | -17.43725 | -44.36548 | 2025-10-29 04:25:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657ce75d-6d06-3e54-94e2-79cb094271d4 | -18.92746 | -45.04903 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83b221fc-8f5e-3844-bc52-b1ca11f604ba | -13.37245 | -47.39228 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4b3f6da-235a-379e-8f29-2c3d5e1510b5 | -13.22206 | -47.06841 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81ff3945-99a2-36ec-a94e-4cf14b1aeed5 | -12.87714 | -48.2801 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8fe7d72-80c3-39d5-a5f4-53d30e020d69 | -15.10149 | -43.84011 | 2025-10-29 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 86b6380c-d843-397d-96ac-dad112ad733c | -12.00217 | -46.78596 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abcd1643-12ab-33a1-a7a4-faff25d39f40 | -13.57321 | -49.61788 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c086f5ef-6522-3d60-a2d2-ee401a474e33 | -13.2321 | -48.56061 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adf95a0e-d2b4-3606-a92d-d8291e90acdf | -15.8004 | -43.65116 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06aaa6bd-e8e2-3111-b3a8-8c7ddd5ae707 | -11.43602 | -47.71054 | 2025-10-29 04:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a2dd822-c327-3bf1-99d8-46ca4a60cec7 | -11.9328 | -51.33788 | 2025-10-29 04:25:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e93c2cf-dac3-3fd7-b9aa-1245b7615e3a | -19.33319 | -43.05123 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90054ce5-50e8-3a70-80c9-23ccd0179bf0 | -12.43625 | -43.75598 | 2025-10-29 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e51d64e3-f115-3918-b61b-fbe1b2a49bb9 | -12.69827 | -46.3032 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eaab85b6-ac64-38be-ba05-dd36b97b0a92 | -13.24317 | -44.11377 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84a615a7-1568-35e6-aa19-6d75e8169247 | -12.95931 | -46.49516 | 2025-10-29 04:25:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13f8c276-c9c7-388d-99b2-ea8f4abc1727 | -13.6376 | -46.52254 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c273f74d-b4a5-3284-a792-9646a9b8bcf5 | -10.8607 | -50.09811 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8a297962-6b6e-3975-ad13-4a1368b3c632 | -14.19858 | -48.35917 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 112fbda3-f14f-3833-b199-528a0797a217 | -13.4741 | -47.4536 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 902c8536-29af-36ff-8ef0-5001bae78a46 | -18.92274 | -45.03156 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 864c597f-c315-372c-bd88-de941adb9f50 | -14.41923 | -47.87105 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc48a309-6bc4-3ea7-81d4-51ef5fc4a124 | -12.39655 | -46.65025 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b30a32a3-f8d5-398e-87af-1a5a9dc7a9b6 | -14.60478 | -48.40104 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fea05a34-ad96-36fa-a3d8-7967f06f6c87 | -12.3619 | -50.15586 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1e872e9-7309-359e-a8bd-691bdc0ea453 | -12.52682 | -44.89072 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43f5db38-40e9-3339-b121-f12cea46d68a | -13.21101 | -47.05183 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2262d05b-98d3-301f-82b3-a3bdfb3dd362 | -14.62291 | -44.99977 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67736cf-7cb9-38b9-96da-16366b424f08 | -13.55178 | -47.14443 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c25d955-018e-3cdf-b696-cc17f4e1c36a | -15.18499 | -44.06205 | 2025-10-29 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c3a6030-85a5-3f1f-a739-3d46d8dcc9ab | -17.69347 | -43.96998 | 2025-10-29 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0ee052e-0a4a-3ea3-9c6a-8757662dd706 | -14.99271 | -47.86629 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a372536-faaa-3ea4-8178-1bfdfceebe54 | -14.24045 | -48.10741 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00c5c82b-20df-3e00-b7b9-5f168ac8e1e8 | -12.35666 | -50.15697 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c4a919e-6665-387f-88df-e8ada84054fd | -12.19204 | -46.71819 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3945584-adb7-3b8e-aee9-41fd76d548b2 | -13.57339 | -49.59514 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1a69a9a-cae7-3239-9bd3-41a00a719f58 | -12.20147 | -46.49398 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecbdab4e-c309-3ebd-be21-e89244d21be0 | -12.72804 | -46.7084 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d6c2444-df44-3dc0-a193-8826ce264b94 | -17.13964 | -44.81177 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a2bd808-f304-373f-a2f5-b673f13f1058 | -13.36632 | -47.38762 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c15f826-47dc-302b-928c-6c3dc5b730c0 | -13.90864 | -48.46699 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d14619f-e607-3fd1-ad94-9df7d160e923 | -11.53141 | -47.10285 | 2025-10-29 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 131bdeb0-75ce-3e07-8956-15314bd364ab | -13.64154 | -46.49769 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0d5fc1c-14e6-3798-9f7b-965e6fcede6b | -13.26659 | -47.86374 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f60dda9-35f3-345c-b23a-a67d218d1410 | -13.5656 | -47.33549 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a9f65b5-14cf-3acd-b219-7dc009533972 | -17.9478 | -44.29606 | 2025-10-29 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c9cb7b0-a9f0-37b6-86b9-6b076e9636a6 | -13.2209 | -47.07557 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17182840-69b6-321f-ac76-0790dcf5b6ee | -13.44255 | -48.62046 | 2025-10-29 04:25:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8c2c3da-30ec-3de6-9ae3-f3dce464e320 | -14.13115 | -44.06732 | 2025-10-29 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43520fa3-6c24-30ac-944b-e08b43b5469a | -13.41959 | -47.37787 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1bbb8c9-c5fc-33a6-8083-4ac8f7b23488 | -14.93042 | -49.65665 | 2025-10-29 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f94316ce-ccbf-3887-8fef-ee3575351ca7 | -13.53625 | -47.13445 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c3b235e-0cee-3ae7-8f36-7668d77e4803 | -13.54663 | -47.32521 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0faac6f4-14df-3bd0-a7d6-d3725c336b01 | -13.28793 | -47.3714 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 380ce3cf-dc4a-31a8-8488-e302756767f1 | -13.87046 | -48.4837 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d6f43b7-51f8-3be8-a4ee-51610280dbf8 | -11.25703 | -47.81693 | 2025-10-29 04:25:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da9fa213-2dde-37e7-8f41-3e66e4ba03f4 | -15.57413 | -43.54692 | 2025-10-29 04:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96821177-0a50-3e17-87f0-8dc6d56cfe0a | -13.63331 | -46.46355 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3cd336c-d9e4-349e-9ebe-237e29cbe272 | -18.82698 | -41.95041 | 2025-10-29 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2cbe1217-9880-3c99-af36-4f6b5540cb9b | -12.69439 | -46.30618 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 995f79d7-f761-363c-b8c9-bf2b6627554e | -13.21756 | -47.07503 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cac0e02-d675-3e6c-a7d9-d86256efaee6 | -12.20559 | -46.52731 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d221eb5c-e93f-364d-83ad-122bb2cae8c4 | -11.78389 | -44.16127 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c1411f5-1876-3e49-88b0-9ceb83051ec4 | -13.5325 | -47.34871 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c72317d1-f7d9-3380-93cd-d419f25c7b82 | -15.21281 | -47.21655 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
