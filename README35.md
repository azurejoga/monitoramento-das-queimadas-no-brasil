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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a652e4e5-f252-34d5-91c9-13f3b9489152 | -8.28287 | -38.17844 | 2026-09-06 11:10:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f841f098-3e34-3540-9d7f-c8c941b532ce | -15.23015 | -42.27452 | 2026-09-06 11:13:00 | TERRA_M-M | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 1220f030-d412-326b-87db-b5fef6fe8b0b | -14.46097 | -40.93139 | 2026-09-06 11:13:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ffd84f99-4177-309a-9126-181eceb311c5 | -14.91789 | -44.67103 | 2026-09-06 11:13:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 110.3 |
| c38075f8-d366-3c1d-bf5b-eb122dc8d836 | -14.92022 | -44.65663 | 2026-09-06 11:13:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6aa1c4ad-e2c0-3951-93b3-14466705b8b9 | -13.25935 | -40.94535 | 2026-09-06 11:13:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 4405b7dd-a330-361f-b26a-7e2839b9e3bf | -16.58165 | -39.44552 | 2026-09-06 11:13:00 | TERRA_M-M | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a3e997e1-cf6c-33be-9837-751b74828fbe | -16.18608 | -39.1746 | 2026-09-06 11:13:00 | TERRA_M-M | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c29a1a4c-476c-3de2-b6bd-089a7f26922a | -15.33188 | -39.75774 | 2026-09-06 11:13:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 849c6ad4-ca45-3c44-8f10-640ab2c865ab | -16.58294 | -39.43618 | 2026-09-06 11:13:00 | TERRA_M-M | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2a188ed8-0b02-3795-accb-806dd2ebd718 | -13.54851 | -41.5442 | 2026-09-06 11:13:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 723b78d6-0e52-3858-af25-c87dc9f0de0c | -14.46233 | -40.92214 | 2026-09-06 11:13:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 29f9dd59-8b40-3024-92e6-ccc77d2afc62 | -13.25032 | -40.9441 | 2026-09-06 11:13:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 4ac3f685-c8ce-35d4-a515-962c65b2506a | -18.48361 | -40.27346 | 2026-09-06 11:15:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e7337d28-e02f-323b-a63e-a0d9564fd08e | -5.3646 | -56.0249 | 2026-09-06 11:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e2253003-eb63-35db-8bea-da33d8627823 | -5.3646 | -56.0249 | 2026-09-06 12:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d4333e90-ad56-3b76-bd1a-6cc652363d24 | -5.3646 | -56.0249 | 2026-09-06 12:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 3c93fe72-c41e-3337-8999-0c69bc664b68 | -5.3646 | -56.0249 | 2026-09-06 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| d67ca96a-0601-39a7-91ee-98c531d82ded | -5.3646 | -56.0249 | 2026-09-06 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| bb8e6ec5-5c3a-3627-8db8-be3b46c4b373 | -5.1439 | -55.9543 | 2026-09-06 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d605a6dd-5284-373f-b06b-912463887894 | -5.6565 | -60.2475 | 2026-09-06 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 755d5d21-ac49-380d-b05c-299961159dc8 | -5.3646 | -56.0249 | 2026-09-06 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 73b68c89-80e9-3570-b334-9a56f004918a | 4.2781 | -60.19473 | 2026-09-06 12:44:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5e7d23ec-0698-3e0a-a2f6-0792ea6b73af | 4.23613 | -60.92281 | 2026-09-06 12:44:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2016e531-9893-30b0-88c1-f2f84a431099 | 3.22939 | -60.47768 | 2026-09-06 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d2d747c8-5029-32a4-88e7-d90ce5f81808 | 3.22814 | -60.46889 | 2026-09-06 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 551a476e-08d1-3e49-b44d-776ef4570b18 | 3.78666 | -59.66029 | 2026-09-06 12:44:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| adf4f036-0f9c-3915-8b5f-67f434b0ea3d | 3.23696 | -60.46767 | 2026-09-06 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f9461cb2-c8c1-3c4c-a4bb-b22a05e37174 | 3.79429 | -59.64998 | 2026-09-06 12:44:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ad7d0460-23bd-39a1-b7ae-c993985ade05 | -5.14147 | -55.96842 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 24d910f4-b4f9-3977-9f48-fe10e5d7d46d | -4.4822 | -55.09186 | 2026-09-06 12:46:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f1bd001d-0917-3c99-9e18-a3ac77f45685 | -5.35638 | -56.02794 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9025350e-1205-3cf3-8fe2-155156d3e8ea | -3.12256 | -57.69318 | 2026-09-06 12:46:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e19b4076-f652-3b20-976f-d82a5ee16525 | -2.71828 | -59.76655 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 517524db-6422-3419-ba96-6aba1707bdad | -5.14314 | -56.25462 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 828439c5-6161-318f-99c9-7f3ce0a4d07e | -2.60643 | -59.52958 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52abff4b-2c7d-3a53-8589-327fda2a23b4 | -1.39473 | -55.16703 | 2026-09-06 12:46:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 220c569e-a4c1-3461-a17a-db1f2607d64a | -2.4635 | -57.91419 | 2026-09-06 12:46:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e6b04e72-5ece-39cd-9a6d-a578a974e7e7 | -4.67717 | -55.63496 | 2026-09-06 12:46:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 959899c9-a14a-365f-a80f-9dd199380f4a | -1.39197 | -55.17236 | 2026-09-06 12:46:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8b9bc1f6-00c9-3f98-8a9d-2601af684d3a | -3.76276 | -61.75932 | 2026-09-06 12:46:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3f71d605-eb4d-318a-ba8b-a1c33df94261 | -2.60992 | -59.53601 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4e1c1b2-a44a-3111-afd4-67f44cac1fb2 | -3.77398 | -61.75783 | 2026-09-06 12:46:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6028f2ca-076c-3429-a6e5-5c37fd650a9e | -3.08049 | -61.17923 | 2026-09-06 12:46:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b19eb4c-8c80-3c11-91b4-02236f36265b | -5.14419 | -55.94757 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b47eae5a-46f8-3c0a-8a86-47b7057edb02 | -5.1405 | -56.27432 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| d5980481-b835-37fb-b607-7cbdd2c08bdb | -2.4595 | -57.90775 | 2026-09-06 12:46:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3552e3c7-75db-37dd-b0c4-77341c309cff | -3.76402 | -61.75047 | 2026-09-06 12:46:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f170cbad-32c5-379a-b1eb-1684103341df | -5.15729 | -55.94938 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8f2eeb5f-bf34-39d1-b289-a1838b6e4d50 | -4.47667 | -55.08587 | 2026-09-06 12:46:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 3b40776a-170b-39ed-8382-63ff75dda6b1 | -3.38355 | -59.40891 | 2026-09-06 12:46:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 85eae766-caa2-3853-a68c-faed456f7896 | -3.14839 | -60.63623 | 2026-09-06 12:46:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 00559a52-fe14-347b-863e-4d15a64d9614 | 0.86991 | -59.65139 | 2026-09-06 12:46:00 | TERRA_M-T | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9fe7325b-b8a7-38bc-b262-b6c5fea98e8f | -5.3433 | -56.02639 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 51a5d26d-2646-38d5-995e-7ea402ea4425 | -3.14706 | -60.64559 | 2026-09-06 12:46:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2e4780aa-1f13-3f17-9016-218a13cb1554 | -2.70884 | -59.76523 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6d5e05b4-a432-3a4d-ab1e-23f05567935e | 1.80375 | -56.05728 | 2026-09-06 12:46:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 573a330a-0015-3a2a-a638-4c9108185d9a | -2.71081 | -59.68225 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5b28874e-4de9-36e0-bb54-975d47ba880d | -3.77273 | -61.76669 | 2026-09-06 12:46:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c12aa8fc-43d1-39e2-a8c2-c15177edc5e5 | -2.70741 | -59.77538 | 2026-09-06 12:46:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b9cd517-0822-3edb-a9ca-50d04d414725 | -5.15455 | -55.97023 | 2026-09-06 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a8a056b0-9461-3f7e-b8da-b723f51191e5 | -3.33419 | -53.41109 | 2026-09-06 12:46:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 07baf2f8-acd5-3bc0-9ca5-8ecf0a7b46c4 | -3.13929 | -60.63496 | 2026-09-06 12:46:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 40e41166-a474-36a5-8aa3-7f194cc4d5e7 | -4.66377 | -55.63359 | 2026-09-06 12:46:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ad746dd6-722f-3c7f-9659-b81938ba62a3 | -2.73911 | -60.07034 | 2026-09-06 12:46:00 | TERRA_M-T | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 00ef8de6-e4fb-3eb9-8690-4fc6a62662a8 | -5.65242 | -60.24247 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| a9ecf1e0-56ad-3865-803b-058ecf6f4e0f | -6.65516 | -59.92623 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4e812049-b612-3650-abc4-14104ea8f74d | -9.54838 | -60.82787 | 2026-09-06 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d31af222-7ec4-33ed-adfd-292ce8bb449a | -5.29039 | -60.12672 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ef746cbc-0879-3adf-9915-cf1204217b1e | -6.65365 | -59.93724 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f18d84d6-593a-3fed-9660-fbbd17522dcd | -5.65383 | -60.23213 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| fbfbc0e7-68e9-3b34-b0b8-155a17f0fef5 | -8.72088 | -62.42955 | 2026-09-06 12:49:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 58c03fdd-d262-31f6-ad67-00ff5622ac77 | -9.86642 | -60.27876 | 2026-09-06 12:49:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a1a9b345-5287-369d-8c12-bc4f8788d061 | -6.66346 | -59.93866 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 34d3c195-2da9-30b8-8dae-67bca6fb7425 | -6.8743 | -55.60027 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f7a9489b-de6a-3e86-a1c3-b99813c12758 | -9.86557 | -60.28463 | 2026-09-06 12:49:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 061e539c-27b6-351a-bc25-cb9e54a751d3 | -8.7196 | -62.43862 | 2026-09-06 12:49:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b9d10f28-a775-3734-b234-21263b10c557 | -6.95594 | -59.74374 | 2026-09-06 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f460c9f7-e61d-301c-aa8e-d9d236941858 | -5.59947 | -60.23996 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa2462be-ffab-3511-8dba-6eb596b4a9f9 | -9.54695 | -60.83854 | 2026-09-06 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0477364d-7a77-3bbd-bc36-9c96bf96dfbf | -5.28525 | -60.13064 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9d14291b-f6e5-33c0-8b5a-480381cfc6d0 | -6.87986 | -55.60773 | 2026-09-06 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 91e2a183-60bf-3c3a-a88b-c81d0642252c | -6.95751 | -59.73221 | 2026-09-06 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 03f5830b-9c40-3fa2-a4bf-53765cd456a7 | -6.06977 | -57.79357 | 2026-09-06 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 01d4cd37-a613-34c7-8676-f32628a8ed9b | -5.6566 | -60.2284 | 2026-09-06 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ec6383d3-448a-37bf-9d51-568cf6b0cd7f | -5.6565 | -60.2475 | 2026-09-06 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 01f9bb5d-9c0c-3ca9-a27b-73ff72d5d0d9 | -5.3645 | -56.0447 | 2026-09-06 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e4511bbf-4139-3f49-8675-8465e72bad2e | -5.3646 | -56.0249 | 2026-09-06 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| e44ad1c7-ea25-392d-8eb0-3f411c453e19 | -2.7098 | -59.7636 | 2026-09-06 12:50:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| db2c9e8f-dd56-34d3-9144-d5881efe1182 | -5.1439 | -55.9543 | 2026-09-06 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1ba4fa84-d247-3934-b9f9-1e24597b10f1 | -5.6566 | -60.2284 | 2026-09-06 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 10c16ed2-a0b3-37c6-b4a5-f55438ffc257 | -5.1439 | -55.9543 | 2026-09-06 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2c9d5555-c26c-3910-aeb6-5adef71275ef | -5.3462 | -56.0256 | 2026-09-06 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c45f34c1-40fb-3b84-809b-d655ffa4c83e | -5.3646 | -56.0249 | 2026-09-06 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 9301af58-9132-345f-9c24-5e8701729c81 | -5.1438 | -55.9741 | 2026-09-06 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6c0e3014-d331-3e41-b398-78ef8255acbf | -5.6565 | -60.2475 | 2026-09-06 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| fb7dca4c-a3a7-37a8-a707-cd57419ea720 | -11.2955 | -45.7087 | 2026-09-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 701ad369-5f0e-32ad-9a0d-23a274d6bb00 | -5.3645 | -56.0447 | 2026-09-06 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| febc2219-a9bc-3066-a16f-612258e1432b | -5.1438 | -55.9741 | 2026-09-06 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2e9d9750-cdb0-30f9-bf8c-a218510cfb22 | -5.3646 | -56.0249 | 2026-09-06 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 252.8 |


[Clique aqui para ver as próximas entradas](README36.md)
