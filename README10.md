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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea7a70b5-fdc5-36e9-b516-d6f23274ad6a | -12.83381 | -47.4071 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d1244f-8866-345c-920f-060d58477db9 | -11.16014 | -48.6795 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a594974-b084-387f-89c1-969f5f1dcdaa | -7.08061 | -44.91814 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae49b12-4800-303d-b54a-e4b04f9255b5 | -6.72294 | -42.12293 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5503a0de-3646-3eb3-b362-dad6268f418b | -13.30813 | -45.37891 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3f2b100-9f6c-372c-a909-bd1a6149e3af | -10.47802 | -49.1407 | 2025-05-17 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 052250d7-fa6e-309a-b8d0-e8abf89ca5ae | -6.70658 | -42.13603 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 340a0bbe-aab5-381b-ac85-9981b3d36fc3 | -13.35943 | -43.08862 | 2025-05-17 04:38:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 94e00f90-a3cf-3245-b7f6-a54a45b8e7bc | -8.69423 | -49.02716 | 2025-05-17 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b96063d5-0d23-34b6-af27-d30a322600c5 | -6.74924 | -44.53123 | 2025-05-17 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1632f4bb-a3d3-3067-9346-35f3c160e481 | -9.03575 | -47.76559 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4709c13a-5871-3137-9554-6d5beb833467 | -11.97359 | -48.10712 | 2025-05-17 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8a26244-3868-36fb-9bc6-d1e886c69159 | -11.64649 | -48.02361 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a4c79f6-5cca-366d-b3d4-d2425ec0caa5 | -11.64591 | -48.02757 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b52e4c8-a466-357a-99fa-4aea223e28f7 | -11.35829 | -52.96106 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e9c0845-949d-3921-8f0f-c0b17e024a97 | -11.94406 | -51.62843 | 2025-05-17 04:38:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24a36b4b-2872-3a35-b8bc-57183dbae8ea | -10.27301 | -46.80043 | 2025-05-17 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82a2ab37-ba90-3b2e-aee1-244bcc3fc48f | -13.30032 | -45.37379 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c50bbf4-972a-3143-9b44-9e699808c1e7 | -11.39717 | -52.95112 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d2b2f39-f22f-373c-a6a5-553084b38b73 | -11.1573 | -48.67525 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 605fed29-7d59-3807-9650-c4db9f8c735e | -8.33616 | -48.01211 | 2025-05-17 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a94dc2fe-746f-353d-b852-58e1aa186097 | -9.31353 | -44.83336 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e8a2010-4837-3829-8979-9858f4633e25 | -11.69221 | -44.62311 | 2025-05-17 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19be8a9e-0e28-336a-ace3-40fe1c529c90 | -13.30552 | -45.3667 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7593f997-b908-35fe-8230-365225306b54 | -11.96292 | -48.2508 | 2025-05-17 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2123d6e9-6d78-3b4a-a844-68fbfc772913 | -6.78636 | -47.59418 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a8f13b5-9e30-325d-af71-e8450b7bbd68 | -6.71203 | -42.13168 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 28d613d0-f1e0-33ac-b202-e2e33d213a85 | -6.17027 | -48.063 | 2025-05-17 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ccb40e-ff51-3641-b301-b51823232af7 | -11.42033 | -54.32439 | 2025-05-17 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e87cf61-c591-3983-a7b0-3f1d38406f51 | -13.0538 | -47.82509 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07def1ef-ba54-33cd-b51a-a6aef001ee08 | -10.02672 | -48.7006 | 2025-05-17 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b3cd8f50-0a50-38c6-8096-403f2acca660 | -13.3099 | -47.46613 | 2025-05-17 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fb03c5d-3b72-3a69-9b30-8060ad21b411 | -12.35239 | -49.96908 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e15f4eba-0e93-33dd-8caa-3d2478c809db | -13.30397 | -45.3783 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feb8bff9-a20a-392b-8da8-d4c741131582 | -6.7073 | -42.13102 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91557752-14fa-32f8-98f4-4efa00207d98 | -9.42296 | -55.78251 | 2025-05-17 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 301ad739-1b90-3532-bf7a-949575506c5e | -6.71941 | -42.12494 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 829cbe5a-57bd-3692-8f1a-07d8e8b3ceec | -8.74771 | -49.74957 | 2025-05-17 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee2ce38e-808a-33a1-a7e6-c27d079b6440 | -9.42295 | -49.34037 | 2025-05-17 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd20f491-f2e1-3829-9bbb-9010f03269c5 | -6.7113 | -42.13667 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e968fa76-4891-32f8-8749-3def4d02c137 | -10.53706 | -56.39125 | 2025-05-17 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b044ab0-b343-31ce-a7d1-b03a084e2e24 | -13.31477 | -47.45813 | 2025-05-17 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ee99fba-04ab-3fd2-933b-d78e141be90e | -8.69811 | -49.02415 | 2025-05-17 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 165aa5e2-e6eb-396c-b635-8078e62695bd | -11.64181 | -48.03099 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a62d3c0-d8b6-3a48-b25f-1436900ae6cb | -13.31126 | -45.38724 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92755585-5a65-3387-bf2e-76ef557cf207 | -7.95166 | -49.75839 | 2025-05-17 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03d1d603-3b22-3785-95ce-8d8ef0cec070 | -7.90353 | -44.4795 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 685e1773-762b-370d-98b5-eb0b1e656758 | -8.69478 | -49.02363 | 2025-05-17 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b3726d2-212a-387f-8bfe-3e0edf1d0e65 | -13.305 | -45.37059 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83ecab57-a8e0-3db1-b52b-cd4b63d26dac | -11.16071 | -48.67578 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15200579-4c66-3730-87b3-1883f26fcfd8 | -13.3071 | -45.38661 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a5040be-6837-35ee-b5b0-aa948237d695 | -6.62412 | -48.01455 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e8db20b-6282-3a6e-8dc4-4aa456cd3c12 | -11.38693 | -57.82338 | 2025-05-17 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe2ac2d-df43-3ad6-ab26-306e7b43d021 | -13.14601 | -45.39251 | 2025-05-17 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b6f48f0-3a9a-3c9f-a54c-33041db3104e | -7.72253 | -46.30295 | 2025-05-17 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 900c76cc-0c5d-3747-a886-c2c46d855a57 | -11.36242 | -52.95774 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c42c9527-83b7-3de8-80c3-8baf6505ca80 | -7.7262 | -46.30344 | 2025-05-17 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae91a7c1-4109-3adf-83cd-5e1389e6e32b | -11.973 | -48.1111 | 2025-05-17 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b19f4838-3bbe-36c5-a66b-2b28f373267c | -11.57925 | -47.62177 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c7ce52c-8a55-34a8-a968-604c802e6422 | -11.79295 | -47.40403 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05247c9-aff0-3aec-affa-ec4d8d9f17bb | -11.78726 | -47.34233 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3d0862d-eb32-35cc-983a-fb4bbad89693 | -11.35893 | -52.95715 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2bf2e62-f619-39ec-9342-730d45530a3e | -12.35349 | -49.96196 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c630d2ed-f328-32fd-8755-5886ecf475e6 | -10.63917 | -55.31702 | 2025-05-17 04:38:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6646002e-5508-3055-b83e-647c3e62ecf3 | -13.30865 | -45.37505 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bdf05dc-7ba1-39f4-908b-fe33d5c573cf | -13.31542 | -45.38784 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 918f5e9b-12dc-31fc-abb1-3b8059e48f62 | -11.64298 | -48.02307 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b5eb536-c60b-3a09-9bdf-a1480c289172 | -11.58045 | -47.61353 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb882364-241b-352b-acac-312dd070fde7 | -11.57389 | -47.60839 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35a607f5-7dd7-3598-8730-bc626f034675 | -9.30997 | -44.82913 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59aa43a0-b630-37d1-85fd-ab5e9375baff | -7.9478 | -49.76133 | 2025-05-17 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0a3d108-c9d7-37fd-8996-538213dcc7a3 | -11.16412 | -48.67631 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a955aec-7126-3d83-a4e1-15ddfb7cf907 | -6.72485 | -42.12048 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b707a89a-75f5-3cc8-8353-561279a8c34c | -11.35957 | -52.95324 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9b7ec6b-9463-3777-94d9-678ec66c449c | -6.78578 | -47.5979 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b861c72e-cacd-39e0-a177-87f966c9364e | -11.41842 | -44.7082 | 2025-05-17 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 991f0691-92bd-39ed-a21f-e0f9fa944719 | -13.30969 | -45.36727 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6440be37-fb9c-3e82-bf7b-7f740aec14ad | -13.32375 | -45.38898 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f900901-8fcd-351a-8a92-4e0ed5ea69b9 | -13.31281 | -45.37564 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b77da8-0afe-3a91-8f3d-bcc9a47d60ad | -11.15389 | -48.67471 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 252e6e1b-876b-3e45-a385-3984f0a5e496 | -11.78236 | -47.35033 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db3611c6-ff93-3080-8907-a8cdcf85b0bb | -6.71872 | -42.12999 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cc37de0a-f8dd-3c39-b643-4684c2d59a21 | -10.47466 | -49.14016 | 2025-05-17 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3738183-8ae6-39f7-a01e-2c9f07c0f9d8 | -11.4211 | -54.31988 | 2025-05-17 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 669e7215-3272-3fb1-82ef-108ae30038ab | -9.66787 | -47.5587 | 2025-05-17 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f30d4bff-bbff-3fb2-9f0e-b293d32d50e6 | -6.72414 | -42.12562 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 299182bd-4b68-3518-ab4d-b79c2bc3244e | -13.31646 | -45.38008 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68133470-7c0d-39b4-b4fb-e044d48cfef1 | -13.32011 | -45.38453 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e04ae73-9e47-3005-871e-8b6fd66fbba9 | -11.27298 | -52.47328 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd23e0d-2d26-3b0a-bd7e-c833a24885ac | -7.23453 | -44.71231 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03cadf2a-4067-3298-8bd9-7f4f09ea83a7 | -6.75326 | -44.5318 | 2025-05-17 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17329b7b-7048-3228-bf62-c20057991f78 | -7.07731 | -44.91663 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfd4c28c-a484-3f74-8e99-9f6fb3ffc267 | -10.63977 | -55.31351 | 2025-05-17 04:38:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09df1fac-ec7a-3ab4-b0c1-cd8fe8d70446 | -6.7222 | -42.12799 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1004166c-53ca-30fe-b37a-53c58b763ef5 | -11.78663 | -47.34658 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b520478-651a-3187-be05-643cebbaeb75 | -13.31854 | -45.39616 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c4ffa5-bf1e-3d8e-b40b-6b17736b1b96 | -11.57886 | -47.87128 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41e2455f-8d92-310b-998d-1321143754e7 | -8.37103 | -49.63989 | 2025-05-17 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71749109-73af-3156-a397-99c8c77ef91d | -7.90299 | -44.48314 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9da7074-5ae0-322a-a6d9-d03eebbc1e32 | -12.35294 | -49.96552 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
