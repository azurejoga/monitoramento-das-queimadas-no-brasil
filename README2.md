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
| 1049260a-77b3-3565-b34d-752525c29778 | -20.22832 | -43.90134 | 2025-10-02 00:09:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 9705b5d9-5353-3773-b30a-e74962d4f747 | -18.11905 | -42.73418 | 2025-10-02 00:09:00 | TERRA_M-M | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 5096d43e-b252-3b2a-9df5-103cce03b439 | -22.0786 | -43.08658 | 2025-10-02 00:09:00 | TERRA_M-M | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| feae1ce8-a450-3850-809d-8a89ee58b56e | -21.23892 | -44.07167 | 2025-10-02 00:09:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9039d5a6-2d74-358a-adab-5719e270f6d6 | -19.59299 | -42.47414 | 2025-10-02 00:09:00 | TERRA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 2391773b-32d1-32e4-87f1-f58e771b4257 | -19.45963 | -44.27991 | 2025-10-02 00:09:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0cfc12e4-bbf1-36a4-9258-f81e7909a027 | -20.74808 | -42.72791 | 2025-10-02 00:09:00 | TERRA_M-M | SÃO MIGUEL DO ANTA | MINAS GERAIS | Brasil | 3163805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 2dc6f770-258a-3969-b9ba-b93fc16af769 | -19.42931 | -44.19411 | 2025-10-02 00:09:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9526c63f-9844-37c0-9486-6ac096306cca | -19.70486 | -44.43689 | 2025-10-02 00:09:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1d30b542-1549-3b5c-a4f8-c69f49435fb1 | -22.02743 | -46.04898 | 2025-10-02 00:09:00 | TERRA_M-M | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 4a01bdc5-3431-3c6f-97c4-2e7ac435ee9c | -18.66576 | -43.88911 | 2025-10-02 00:09:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 315c0ee5-13e9-3097-be08-e0e50ebfc5f6 | -22.62238 | -44.49997 | 2025-10-02 00:09:00 | TERRA_M-M | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d68ccc3c-128e-3b35-86a8-9d35e31cd62f | -21.45307 | -41.04784 | 2025-10-02 00:09:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6820fd6c-b71b-3626-8cad-8a5a9ab21f10 | -20.87393 | -46.45363 | 2025-10-02 00:09:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 45db19b7-fa5c-3abc-ae07-977c5df2d387 | -17.94159 | -42.58075 | 2025-10-02 00:09:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| f7424a1b-bfec-389f-a9ea-dc3c00d4d632 | -22.07332 | -43.09317 | 2025-10-02 00:09:00 | TERRA_M-M | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 61fdf4ee-a2d0-3151-ac1b-6a7def16ac38 | -18.59101 | -43.0337 | 2025-10-02 00:09:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| bd9c52b2-5789-3f56-9f92-4f2ab04539a2 | -18.46428 | -40.57976 | 2025-10-02 00:09:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e62f47e1-032b-3f89-b3e3-b51158a3cec6 | -18.8553 | -41.9852 | 2025-10-02 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 75191348-b5dd-32f9-ae4d-4bd84cbdd7c7 | -19.41855 | -46.81371 | 2025-10-02 00:09:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8666a0d5-1f9f-3584-89b6-e704ef2fbae6 | -9.8523 | -46.8823 | 2025-10-02 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b56686b6-7ef2-3937-9293-baac5201c7d6 | -7.7755 | -42.5152 | 2025-10-02 00:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 149.8 |
| c10bdf0d-c6ce-3eb3-83cb-a5527b6670aa | -14.0133 | -53.8709 | 2025-10-02 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 47e9e449-0a28-3e7d-92b2-47a90674dc97 | -9.8526 | -46.8599 | 2025-10-02 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| bd6b2007-5d0a-3215-95c4-918129c26094 | -12.4207 | -54.3536 | 2025-10-02 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 204babcc-69d8-3f72-b70a-fc228dc611a3 | -12.7002 | -48.5637 | 2025-10-02 00:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| bf919520-b2f6-3c0e-87f3-1dd6b93fdfa8 | -6.7213 | -44.1387 | 2025-10-02 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8828c8e8-4d42-3bca-b790-840389d5a100 | -14.426 | -46.0919 | 2025-10-02 00:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ee7e5629-8659-3267-a756-0dfef25d4991 | -5.8469 | -43.3995 | 2025-10-02 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0c2fbe6b-6c26-331f-a5a6-c55a738b9223 | -8.575 | -49.5881 | 2025-10-02 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 08185230-9d54-3a66-ae61-11a7e9808f8b | -7.7941 | -42.5369 | 2025-10-02 00:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 82978af2-e5a1-3639-a289-6ce6b98131a9 | -12.8355 | -41.5343 | 2025-10-02 00:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 3c66da2c-39e5-32ea-a1c4-7b205657058a | -14.9924 | -46.9091 | 2025-10-02 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9f0a267b-197e-3b1d-a2e0-3309f2a13695 | -7.7752 | -42.539 | 2025-10-02 00:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |
| b608b97c-d6d4-39cc-a0d3-3a6e73b5d5a3 | -15.2738 | -49.3073 | 2025-10-02 00:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| bc855e84-b9d3-3e12-85ac-fc6450c00098 | -13.0119 | -45.1988 | 2025-10-02 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c81c2423-ffa9-3783-92e8-6d1ec75440c7 | -5.8657 | -43.3981 | 2025-10-02 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 746a18f0-c8aa-3f45-a665-6581b6e18b8a | -11.5947 | -47.226 | 2025-10-02 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| cc9c040d-b47f-31c1-aa49-6604f7d5f50f | -15.2547 | -49.2883 | 2025-10-02 00:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| aff3dacf-fdae-395a-a839-bec961a3fac7 | -15.2542 | -49.3104 | 2025-10-02 00:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| efedcb6f-3f1b-3974-8fca-2f8d5ed3605a | -7.7944 | -42.5132 | 2025-10-02 00:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 9ca95a05-4576-3870-b3e2-64211714ea50 | -14.2121 | -46.1058 | 2025-10-02 00:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ef3501d5-fa36-3db2-8177-96d320d0d4af | -13.155 | -47.8121 | 2025-10-02 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 83589144-fd2a-3a0f-a6db-341301476e60 | -22.5735 | -46.7755 | 2025-10-02 00:10:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 9756dbbd-e1b2-3789-b878-83f495a37d05 | -9.8713 | -46.8801 | 2025-10-02 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f6354173-5587-3fc5-9adc-b6f2ab5221bc | -14.3119 | -45.9736 | 2025-10-02 00:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 13fc4117-ab85-3268-ba34-88010a46741b | -15.2742 | -49.2852 | 2025-10-02 00:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c57fc02d-01a7-3e5d-b259-2a25a8db6444 | -14.4065 | -46.0953 | 2025-10-02 00:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c924631e-662f-34ec-88a1-7ea9e70f4390 | -12.122 | -43.4215 | 2025-10-02 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c72aa7cd-de62-3a79-a003-b7c34f75bbd3 | -8.5748 | -49.6095 | 2025-10-02 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 2d2ad329-82ad-3300-8151-5a24e71d014c | -14.9728 | -46.9125 | 2025-10-02 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 605a4ad1-170b-3b06-9275-df6f7776e9ba | -14.3704 | -45.9634 | 2025-10-02 00:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ecd261de-a0dc-39d1-a17a-40fad12e90a6 | -11.175 | -47.2581 | 2025-10-02 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 85bb2490-40b8-31f6-832a-cf8830f31697 | -4.841 | -45.212 | 2025-10-02 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1db49e27-792f-3c0e-8cbc-a2833ab7bb6d | -13.1739 | -47.8317 | 2025-10-02 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b6c46d27-18ab-38ba-98de-9723fa50be4d | -13.0114 | -45.222 | 2025-10-02 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 31e1fcc3-73bb-37af-bd59-87c974f20e4c | -13.1546 | -47.8345 | 2025-10-02 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| c5737a5b-97de-3be3-bbd2-c366f4b8b898 | -15.32415 | -46.27957 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 76f82bdc-050f-3bb7-97e1-fd30e98c167a | -15.78909 | -43.6869 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 41b98b40-8f7b-36c5-8447-6fb251523a66 | -15.28915 | -46.39676 | 2025-10-02 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1b2ef501-6ff4-3124-8c96-50076ac4e60c | -14.00301 | -45.00747 | 2025-10-02 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 75cb3aed-2013-34b7-bb69-aac53d1f47cd | -12.15451 | -46.68142 | 2025-10-02 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 467b6a8a-445f-3efa-9229-ea66dd79a3cc | -13.81058 | -47.5182 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| e2309a9b-8a9e-391e-9c7e-254f5b7151b9 | -14.36074 | -45.97719 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 0bb64678-7d4e-3d79-8fa5-b202317bc67f | -9.89118 | -46.92672 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e11f8ecf-4906-365b-9569-09fdcba45796 | -13.76673 | -48.00194 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| edd3a5cd-95ab-3e85-b6ed-41223aa67e40 | -14.57775 | -48.30976 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f74316a3-b066-3446-9734-3433827e41be | -13.36137 | -46.63354 | 2025-10-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 49e32e6c-8a1d-380d-b6b4-5d623a43046d | -13.00869 | -45.21128 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d9c1588c-30e4-3703-bc80-6f9d4c4b87ac | -11.80147 | -44.97661 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b3d267c9-7128-3c41-bf3e-71f09b8d678f | -13.76132 | -48.68143 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| dad828f5-6d33-33e3-80b6-8745e29a5400 | -13.31118 | -47.82971 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 064cdec6-bd69-30a6-bfe4-3a21df7999f4 | -11.3948 | -45.03769 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 042712a9-10aa-32c6-913a-dc09a952bdf6 | -12.87057 | -46.94193 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 35049036-a251-305a-8134-4d26e602aeda | -9.9437 | -43.69847 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a0a4dc24-8a1a-302a-b946-7a30b5fcfdc9 | -14.22373 | -46.10536 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2a1a10e3-91f2-37cf-850f-d845602317d6 | -11.44501 | -43.89661 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c0c12250-63ee-3cfc-8d1e-43ef69ce7a5d | -12.64148 | -44.85524 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 88706ec1-a5d6-397b-a496-e8bcc2c966ec | -11.6725 | -45.32067 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16c5516e-783a-3128-8c0b-b7490e3c07e2 | -14.35855 | -45.95898 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0f2be1fa-c5f0-3c07-a36c-f66e78b8e2df | -14.33872 | -47.14234 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 96115dca-0d84-3b20-8f87-acf83a756bd2 | -13.8249 | -44.20826 | 2025-10-02 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0db42995-91b9-3438-b00a-c3dd326a42eb | -9.94615 | -43.71625 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 293.8 |
| c622f915-47e4-3194-abee-1a286029579e | -14.41033 | -44.9 | 2025-10-02 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2da23cbb-60a8-3434-80c3-bc83630cc02b | -11.98908 | -50.58369 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ec152acb-6fc5-3af8-802b-a4e002da2d29 | -12.89872 | -46.91086 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 5b804cb9-4f6a-385c-9a4a-c11f93587b8d | -13.76337 | -48.69979 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d306b317-8129-3126-b5a6-f0154e1cc0c6 | -11.59165 | -44.78259 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40b25134-a286-38c5-a0bf-d3830034daf9 | -13.0727 | -47.09438 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 96206493-fb0e-349e-8ff5-ec66cb9b1dcc | -11.16725 | -47.25431 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d8e8a21b-224f-39a3-8879-95e09d7e6e88 | -11.46964 | -44.96847 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9c6029f6-f3d0-32b4-bab2-b098cbb62229 | -9.94247 | -43.68958 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 639c5f77-df46-3982-bfdc-2eb07dd6146a | -15.54948 | -48.18202 | 2025-10-02 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3c5c4a45-8bb5-3792-8c64-b537d16ca25c | -14.7014 | -49.06204 | 2025-10-02 00:11:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d2f6ead5-b308-312f-9532-941bde570587 | -14.30955 | -45.89344 | 2025-10-02 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8f1113b5-d7d1-31aa-a706-eff980514492 | -13.53938 | -47.25496 | 2025-10-02 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2e963ab1-f350-33fd-901e-e904723cee49 | -15.26096 | -49.29509 | 2025-10-02 00:11:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a6f6a412-3100-355d-af41-f305a618ea53 | -11.435 | -43.49464 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb7f328d-3498-33e2-8358-bd31da2d48d2 | -13.23791 | -47.33359 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 37fbc009-b02e-3a9c-ae66-8a2bcad3b408 | -14.97616 | -46.92841 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |


[Clique aqui para ver as próximas entradas](README3.md)
