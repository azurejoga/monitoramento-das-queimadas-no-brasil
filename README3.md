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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00c6774c-8400-3968-bc13-05f612e81331 | -12.70802 | -54.92558 | 2025-01-26 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d9a81ca3-4bd9-3b1c-be25-3a0cf01789fc | -9.26234 | -60.31395 | 2025-01-26 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e85feaf1-e32e-3ab2-a561-b7ba9f15464b | -12.27037 | -57.60653 | 2025-01-26 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c171c261-1f19-3089-b063-3e78c1e1ba32 | -9.25824 | -60.31724 | 2025-01-26 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13688a68-a1bc-3aa5-942b-d62aed9febaa | -9.25887 | -60.31337 | 2025-01-26 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 368056da-7942-3664-b406-fc60d5ef5f20 | -12.70058 | -54.92441 | 2025-01-26 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 355797f1-e3e0-3c21-bb4d-61690916abde | -9.26171 | -60.3178 | 2025-01-26 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 434652c2-da97-37bc-ba71-e95a6a9f66cf | -12.71109 | -54.9307 | 2025-01-26 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f81fbf7-523f-3a23-ad1b-f273a02bd604 | -11.91743 | -55.90006 | 2025-01-26 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11e47961-6f0a-337c-90c0-fddd8b644b44 | -12.26703 | -57.606 | 2025-01-26 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aa3c4d0-e3dd-3b54-9150-de51463b4df0 | -15.24762 | -60.21848 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be79c30-479d-36a7-8110-8853164d71e8 | -15.52776 | -60.10654 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91feab4d-9c1a-36cf-af24-2f8352f32510 | -15.25095 | -60.21903 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd8643fd-39ef-3ca9-ad1e-184141b6f0e8 | -15.25485 | -60.216 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89669c93-2d57-336b-83aa-06db743e87f8 | -21.61715 | -57.04584 | 2025-01-26 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda159c1-0961-3655-86f8-d7debd6562d8 | -15.25543 | -60.2124 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7db98a22-d18d-3ef6-b346-dd4766a5d523 | -15.25817 | -60.21655 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 028dae82-c78f-33da-9c52-4586c9a9b781 | -21.37325 | -57.19785 | 2025-01-26 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4654c85-d724-3ee9-9889-232fb2a9ddb8 | -15.25152 | -60.21544 | 2025-01-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f11cbd07-a8da-360d-ab45-b8dce8556765 | -21.37388 | -57.19311 | 2025-01-26 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e70274cc-63b0-3504-9bcf-e927bf53f745 | -2.91239 | -54.28916 | 2025-01-26 05:35:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d343aadc-6139-3111-87c6-4b6d93f178c5 | -12.26493 | -57.60701 | 2025-01-26 05:37:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1469c194-4f2b-3234-bd15-173f6e856e73 | -12.70694 | -54.92934 | 2025-01-26 05:37:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c8d17a6d-92f7-393a-b538-7955398d54eb | -9.26051 | -60.31622 | 2025-01-26 05:37:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6c04b99-4106-33bd-be71-771e35db78b5 | -9.77024 | -66.60976 | 2025-01-26 05:37:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3880545e-6f95-3383-bcf6-bf01442fa833 | -12.26973 | -57.60768 | 2025-01-26 05:37:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ba5e950-346b-3feb-94f2-ac1fe775fd89 | -12.70742 | -54.92523 | 2025-01-26 05:37:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f33da0c9-bc56-3c87-8ff4-630a1fb52ffb | -9.26259 | -60.31825 | 2025-01-26 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b20e6bb-3eac-3922-8d88-6c67be28355e | -9.77207 | -66.61072 | 2025-01-26 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81277ac8-821d-394f-b568-661f696440e8 | -9.25679 | -60.31749 | 2025-01-26 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e9f59f-0b12-3d00-9173-37c5d8b18869 | -9.26731 | -60.3136 | 2025-01-26 06:20:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 447fb464-94e8-3f99-883a-317bd0634b5f | -12.70607 | -54.92564 | 2025-01-26 06:22:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ce9c3723-c2ac-3072-9a3c-330a2ccf79da | -15.42 | -43.79 | 2025-01-26 12:00:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eeeb906e-3925-3a6f-a556-a966ae9d3586 | -15.73 | -45.95 | 2025-01-26 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0636fad-8503-3754-b423-04a0b5745ab2 | -15.39 | -43.78 | 2025-01-26 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d927aa36-b2cd-3eb9-8a1c-0a0cefd61d87 | -8.67048 | -44.16205 | 2025-01-26 12:25:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d24f89c1-df2a-364e-9dad-b7367ed6d9cc | -6.67626 | -44.05203 | 2025-01-26 12:25:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3f43a5b-2e58-3ea6-93e5-2c77101dbef2 | -7.23154 | -44.30069 | 2025-01-26 12:25:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 100642ae-b8df-397e-a22d-cf6028280176 | -7.57148 | -44.50039 | 2025-01-26 12:25:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e47ff979-d17b-3c53-9f9f-dd2825847e7f | -6.15876 | -41.14231 | 2025-01-26 12:25:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4d4572fd-1d67-32e1-b00d-3217da72a6b9 | -6.35689 | -43.39243 | 2025-01-26 12:25:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7dd568d8-a559-338c-8260-088ef099fc8f | -8.12423 | -43.14195 | 2025-01-26 12:25:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| f66e6e0a-ca53-39fc-8cab-382b09d6e720 | -8.21887 | -44.79925 | 2025-01-26 12:25:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6ca862b1-7568-3d09-b187-546ff71a258a | -6.35817 | -43.38347 | 2025-01-26 12:25:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72091cc1-efb9-3100-ae70-5a85f2d2e584 | -14.57611 | -47.89352 | 2025-01-26 12:27:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b7aad00-29ae-31ab-af73-e8e484536871 | -9.1987 | -43.16673 | 2025-01-26 12:27:00 | TERRA_M-T | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b894caf0-13fd-37a4-8013-41a81015a8c4 | -15.35133 | -43.70855 | 2025-01-26 12:27:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 65c0aade-7fd0-3e88-9ee1-b780092d4313 | -14.26525 | -42.81636 | 2025-01-26 12:27:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 298ba3e9-7ad9-3271-b71c-641f3df7a2b8 | -15.04939 | -45.17432 | 2025-01-26 12:27:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1cb12525-be4b-310c-9b82-405da772d544 | -11.58389 | -44.86509 | 2025-01-26 12:27:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| fa643399-7234-32a4-97d8-25b37511da95 | -9.20004 | -43.1572 | 2025-01-26 12:27:00 | TERRA_M-T | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| a9bd8fce-7979-3108-87a5-ce19c104fcdc | -16.3856 | -43.5255 | 2025-01-26 12:27:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d3df33e8-a0fd-38e3-bb1d-eb4d37eb70d6 | -11.74854 | -46.32801 | 2025-01-26 12:27:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed282230-36b9-3515-a112-8adf1f68f852 | -15.05069 | -45.16504 | 2025-01-26 12:27:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b3b2fd1d-0f38-39c1-9227-59dacf7eaafe | -15.14653 | -45.6612 | 2025-01-26 12:27:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b8661718-7da1-3e22-8ba5-80922d3311b3 | -12.11452 | -43.63867 | 2025-01-26 12:27:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ec37f4d6-11df-3a9e-b62f-e7e8780bd0e8 | -14.26673 | -42.80505 | 2025-01-26 12:27:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 38176953-6315-32fe-9e71-be516ca0fb4f | -17.69971 | -50.07722 | 2025-01-26 12:29:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6aa3942e-1a49-3d8b-a092-23ff5a56e51e | -19.81968 | -44.08455 | 2025-01-26 12:29:00 | TERRA_M-T | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1fb86303-52ee-3f43-b078-9f43d2c893f8 | -21.61793 | -51.77671 | 2025-01-26 12:29:00 | TERRA_M-T | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |


