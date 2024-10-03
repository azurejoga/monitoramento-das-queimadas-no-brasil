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

## Dados Diários - Página 215

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eeed503-036a-346b-9d37-a140c6155d02 | -8.817 | -45.1937 | 2024-10-03 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9b26779b-e030-3b8c-ad96-7078f5676509 | -8.8356 | -45.2145 | 2024-10-03 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| c30010dd-4106-3819-83f2-a5009ccc9d6e | -9.0227 | -49.8262 | 2024-10-03 13:45:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a2c436a1-ac75-3583-8443-6537149cca22 | -9.0229 | -49.8048 | 2024-10-03 13:45:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| aab75e3c-408e-38ce-8221-fc419ea9d2d1 | -8.8771 | -61.8409 | 2024-10-03 13:45:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 385dcc9a-2822-3eaa-875d-a2ef417036ac | -9.0149 | -67.7423 | 2024-10-03 13:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 406975f4-25fc-3464-88ca-76dbd9619a23 | -8.9791 | -67.4099 | 2024-10-03 13:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c7a88338-b2bb-3068-98e3-4955536ee7fa | -9.0515 | -67.871 | 2024-10-03 13:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| bba61d1e-e64e-3adf-bdab-e47f114f4561 | -9.3833 | -68.3256 | 2024-10-03 13:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 115.7 |
| ca599dc4-99bc-382e-9065-7a8c2e3c9784 | -9.3832 | -68.3441 | 2024-10-03 13:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f686dd75-20bc-3b33-ad71-99d84e1e1ed8 | -9.6012 | -50.1779 | 2024-10-03 13:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 522a24fd-43ef-39db-b91f-4c76b78f861c | -10.2195 | -47.6839 | 2024-10-03 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8cb01141-cd14-3021-850f-7e458df3a220 | -10.6116 | -48.0795 | 2024-10-03 13:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 95504a39-b6dc-3565-87df-6dbfbb3ea82b | -10.5926 | -48.0817 | 2024-10-03 13:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c3b5a5d2-68ba-3aff-9200-61eb11fd4df4 | -10.5736 | -48.0839 | 2024-10-03 13:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 345c5e7d-3f35-3f39-93d4-67e2c5075eee | -10.7168 | -46.1489 | 2024-10-03 13:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 537ae40c-b94b-3830-a858-57d36ebcb607 | -10.7161 | -46.1942 | 2024-10-03 13:46:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8a6055d3-afea-34cd-abbc-b2544e23a783 | -10.6978 | -46.1514 | 2024-10-03 13:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3992ba56-4acf-3819-9052-766066c9f2b1 | -10.6319 | -53.6805 | 2024-10-03 13:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4c193c80-e5cd-3a08-b1e9-61b6e15ce4c6 | -10.6317 | -53.7011 | 2024-10-03 13:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3e87be70-e238-37e6-901c-da86a3e9e91b | -10.7309 | -47.7126 | 2024-10-03 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c0b7ac2e-43cd-3a7f-b0a6-a3bb10582083 | -10.7122 | -47.6927 | 2024-10-03 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| f03e5ddb-e506-3640-9e46-220f7c719130 | -10.7312 | -47.6904 | 2024-10-03 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| acadc301-7d63-345e-8ef8-07125ee57416 | -10.7502 | -47.6882 | 2024-10-03 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| db0a399f-e5af-3d7c-b2da-5fdeccee02d1 | -10.7459 | -47.9757 | 2024-10-03 13:46:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bdfeed0f-2955-37d4-977d-1884071a7df6 | -10.7352 | -46.1918 | 2024-10-03 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 513d0830-07fd-3435-9fb3-65ef98457b40 | -10.7118 | -47.7149 | 2024-10-03 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8734895f-0ec1-3ea9-96ee-e522f9351106 | -11.0345 | -46.5143 | 2024-10-03 13:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| f01270da-d2b5-3add-bd7a-b4ebae96ade2 | -11.2783 | -43.388 | 2024-10-03 13:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e032b702-3cc8-32bd-ac94-3b87b577e744 | -11.2779 | -43.4118 | 2024-10-03 13:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 1466264b-28eb-394e-828c-865d91a0b521 | -11.6243 | -64.0339 | 2024-10-03 13:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 310c49b2-3647-359b-b14f-b917903b41e9 | -11.6241 | -64.0529 | 2024-10-03 13:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b8a2ad81-a43f-35f6-b781-b38be1a52640 | -11.9737 | -47.3986 | 2024-10-03 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| e78ff0fc-c264-38b8-9958-ef10e9a51cbf | -11.9671 | -50.181 | 2024-10-03 13:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e302a032-9c45-3ebc-83fb-b1df3d16e74a | -12.0128 | -47.3486 | 2024-10-03 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| e401b1f5-9565-3fab-bf14-89d10ff4fc84 | -12.4125 | -50.9635 | 2024-10-03 13:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 678997b0-fc29-3f15-974b-287dd4458513 | -12.3937 | -50.9444 | 2024-10-03 13:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 83b50142-7514-3d29-861b-4a459f247174 | -12.3934 | -50.9658 | 2024-10-03 13:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 185.7 |
| f918a0da-2311-3901-abaa-1d92ffb5b855 | -12.762 | -50.5997 | 2024-10-03 13:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 477313de-24fe-3059-acd2-0458862043c4 | -12.9831 | -51.129 | 2024-10-03 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d0c24afe-21e2-3050-a311-69d7f554bf72 | -13.1351 | -51.1955 | 2024-10-03 13:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 899eeafe-52ff-30c2-873b-551e1b9c77ca | -13.1976 | -48.6489 | 2024-10-03 13:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| c55d3d82-ed70-34ef-9d2b-946e6c6113ab | -13.2169 | -48.6461 | 2024-10-03 13:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ea14596c-d4ea-371c-aefc-33a02c139fa8 | -13.198 | -48.6267 | 2024-10-03 13:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5c1f6795-d668-332d-98bb-3f44bc4b3fc6 | -13.0406 | -51.1218 | 2024-10-03 13:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 6fa0c06f-3016-3755-a7ab-a5a7f447f262 | -13.5195 | -51.1467 | 2024-10-03 13:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 9a8502b8-7a32-3ec7-8d6b-d070af5603ab | -14.7017 | -48.7559 | 2024-10-03 13:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c68d9aee-d0a7-366d-aa3e-0875141d98a6 | -14.8181 | -48.7598 | 2024-10-03 13:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 920e68a7-21da-328f-af4a-b06679ecf6cf | -15.4252 | -47.6509 | 2024-10-03 13:46:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| db867523-1c9f-38fe-9716-e4324ceff0e8 | -16.1286 | -53.5189 | 2024-10-03 13:46:37 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 7b2aaa79-f415-310a-886c-caadc13244e9 | -18.3079 | -43.2326 | 2024-10-03 13:46:47 | GOES-16 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 82c9c9a9-e1c3-34fd-8f12-556db1b279a0 | -18.8406 | -42.9235 | 2024-10-03 13:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| 1ea566ee-49b6-332d-ac99-7a1884306abb | -18.7663 | -43.387 | 2024-10-03 13:46:50 | GOES-16 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.3 |
| fc4b0843-0f0f-37a1-90ea-c47e7f36f1aa | -19.0141 | -43.1998 | 2024-10-03 13:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 174.4 |
| 8911c58e-4877-3a3b-b215-bfa7ca4800d3 | -19.0148 | -43.1749 | 2024-10-03 13:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.5 |
| 322fa8f0-d7c2-3f2c-8a7e-72394a498975 | -19.0932 | -48.2876 | 2024-10-03 13:46:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 17295979-ac33-34d6-9fa1-9259683eea28 | -19.2962 | -42.5779 | 2024-10-03 13:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 186.9 |
| 0ffc6813-e607-318c-9671-fd3152219e5b | -17.03 | -56.78 | 2024-10-03 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f34efa7-e66a-35ac-9671-7c869ca06ce3 | -17.03 | -56.71 | 2024-10-03 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 890bf288-e5a8-321a-ade6-76ffaf2e7851 | -6.32 | -43.43 | 2024-10-03 14:04:50 | MSG-03 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41dcc7d-65cd-3a1c-a0c9-78355d57383b | -5.9599 | -45.3861 | 2024-10-03 14:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9390948a-2bd9-36de-b195-80288694c07f | -6.1138 | -44.9213 | 2024-10-03 14:05:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 513a4767-a266-3f4d-b5b6-5b2cbd31e73e | -6.3008 | -43.0351 | 2024-10-03 14:05:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8353a347-32b1-3545-8d2f-f546c9d897df | -6.2968 | -43.4331 | 2024-10-03 14:05:42 | GOES-16 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| f72cdf7d-6e82-3ec4-9ee3-5bf4f7c06704 | -6.4275 | -47.399 | 2024-10-03 14:05:43 | GOES-16 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a72cbeed-da53-3bc8-b8ee-ac6fee44f526 | -6.6341 | -45.3339 | 2024-10-03 14:05:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6d9164cf-be27-3571-ad4e-3d3136a12fc9 | -6.8885 | -44.3083 | 2024-10-03 14:05:45 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f470bcba-4c98-3590-8bbf-51d693d824f3 | -6.9479 | -47.6668 | 2024-10-03 14:05:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 73f07434-385e-3fc5-b886-0050ae5fa9da | -6.9075 | -44.2836 | 2024-10-03 14:05:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 223fcaa5-95b9-3e82-884a-02260a5578da | -7.0752 | -48.028 | 2024-10-03 14:05:46 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ad94412b-7535-3c25-b40c-93ad2f87bb65 | -7.1523 | -44.2385 | 2024-10-03 14:05:46 | GOES-16 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8346b987-0544-30cc-91ae-8fda4ab54cc8 | -7.4587 | -64.4388 | 2024-10-03 14:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| facefcc7-db5d-31cd-82b8-e5c7e2274ad2 | -7.6441 | -42.458 | 2024-10-03 14:05:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| d27f43d1-2a83-3e08-b2f7-b69cb728a591 | -7.5834 | -44.3589 | 2024-10-03 14:05:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| dbe02dda-0583-37f8-8063-cc13eba99701 | -7.6444 | -42.4342 | 2024-10-03 14:05:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| a815820e-dea0-3c15-801e-f37bc188a9d4 | -7.8149 | -45.4782 | 2024-10-03 14:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 63599abf-82c9-33cc-8e33-b249cf2e466b | -7.8629 | -43.0733 | 2024-10-03 14:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 84f137fd-cbf2-3e5b-b87b-d72c7a49e843 | -7.7498 | -43.0618 | 2024-10-03 14:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| c8d18584-f652-3d43-88ae-703a18b7de3b | -8.1762 | -43.6723 | 2024-10-03 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 016ec458-1ee6-3ecb-ad5b-4f0b63c7fe0f | -8.1759 | -43.6957 | 2024-10-03 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 08d9e9b7-8aef-3342-8661-944d14120a7f | -8.1567 | -43.7211 | 2024-10-03 14:05:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 7f35e567-2ae3-35eb-8153-d4ee5696fae8 | -8.1573 | -43.6744 | 2024-10-03 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 83d0ab31-f21b-3164-a93b-d6484cb2668d | -8.1909 | -42.5406 | 2024-10-03 14:05:52 | GOES-16 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 56be3572-a624-34bc-8d72-a1aa651b72e9 | -8.157 | -43.6977 | 2024-10-03 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 546966c8-796c-342d-a1ad-ce34ff9c1f21 | -8.1937 | -46.8324 | 2024-10-03 14:05:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ac4a5bea-bc92-3899-bca6-b9bd66999a3f | -8.4256 | -46.3193 | 2024-10-03 14:05:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7f3fa381-5ac5-3abd-acd4-9d06140d8c3a | -8.5076 | -47.3118 | 2024-10-03 14:05:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 1cb242f7-e9d0-3eb0-abe3-05e19c897972 | -8.4259 | -46.2968 | 2024-10-03 14:05:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 3df3da79-68e2-3314-8c20-b740ad67067b | -8.7225 | -45.204 | 2024-10-03 14:05:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e8394ac8-b202-3284-b60a-2e2520329fa1 | -8.6113 | -46.5243 | 2024-10-03 14:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0fcd02f9-0654-316e-93d9-fb2c4f9cde66 | -8.7228 | -45.1812 | 2024-10-03 14:05:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 242b3a77-74fc-314c-9f53-bb1dd5922cdd | -8.8186 | -45.0794 | 2024-10-03 14:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8a255c14-80d2-3d02-b6e5-580c6b0330af | -8.877 | -61.8599 | 2024-10-03 14:05:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c1b851a2-457c-346f-ac15-c862771f7c88 | -8.8771 | -61.8409 | 2024-10-03 14:05:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 123.5 |
| a749b162-bffc-3fb7-af17-111b08ea38a4 | -8.8312 | -67.3951 | 2024-10-03 14:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 902fdd6a-51bb-3769-8984-ed465410b81a | -8.8497 | -67.3946 | 2024-10-03 14:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 564fdee8-7b10-3458-a9bb-3ad1287ae957 | -9.0515 | -67.871 | 2024-10-03 14:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 6c094c3c-d951-3811-89d2-72b121e04bc0 | -8.9976 | -67.4094 | 2024-10-03 14:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9e91c44a-dd13-39bd-a35f-a588838bbfbe | -9.257 | -43.5006 | 2024-10-03 14:05:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| b8028f19-ffcb-32e8-a319-afc47dcda537 | -9.0149 | -67.7423 | 2024-10-03 14:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |


[Clique aqui para ver as próximas entradas](README216.md)
