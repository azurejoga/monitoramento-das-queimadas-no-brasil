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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 786e3fac-6a75-399a-9f59-13e79d15cba1 | -11.89288 | -39.32222 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8d2abfb1-7680-3b0f-8f1f-2ffaa4087db6 | -11.89309 | -39.91663 | 2024-10-29 12:17:00 | TERRA_M-T | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 69df443b-9582-3eed-b211-8f87f34f173f | -23.99653 | -54.12457 | 2024-10-29 12:19:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| b8a177cc-1e8b-363d-bfd3-00022f53e434 | -24.00466 | -54.12083 | 2024-10-29 12:19:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.8 |
| 5703bab3-9fd7-3359-b78a-2bdaa076310a | -11.1378 | -55.5515 | 2024-10-29 12:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 4d004d46-08d9-3e9b-a935-d58a9ab34ff0 | -11.138 | -55.5313 | 2024-10-29 12:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 337.0 |
| 8a55e181-086b-376d-84d0-50fdf7844dda | -13.6222 | -45.5838 | 2024-10-29 12:26:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 860cc50c-bcc7-3b58-a541-9079fe5d51ad | -3.3672 | -42.1928 | 2024-10-29 12:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 87.6 |
| cf47d2d9-43a8-3cb1-ba7c-8fec7b4fa937 | -11.1378 | -55.5515 | 2024-10-29 12:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 3c677663-6f81-33da-b485-85670890842f | -11.138 | -55.5313 | 2024-10-29 12:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 333.2 |
| 7b740c15-f8b2-3347-a622-d9988200a79c | -13.6222 | -45.5838 | 2024-10-29 12:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| f0008081-8b86-31b7-ab06-9ade649dd0de | -24.0128 | -54.1286 | 2024-10-29 12:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| e278a1c4-ec32-3bb7-8127-0ec6d6a7c5b1 | -11.1378 | -55.5515 | 2024-10-29 12:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 7be6ec39-1fb1-3b29-8859-36efae3bee0f | -11.138 | -55.5313 | 2024-10-29 12:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 349.7 |
| 0f49939e-3ad5-34c4-af1b-1066604628f4 | -24.0128 | -54.1286 | 2024-10-29 12:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| 35fffbb4-a11d-3941-ac3e-09101c36125c | -1.458 | -54.0763 | 2024-10-29 12:55:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7ccb383c-8800-316f-b852-6a2b055b16ae | -3.8225 | -44.1522 | 2024-10-29 12:55:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fd1247aa-9db3-3625-a9ad-adda450dfea0 | -3.8227 | -44.1293 | 2024-10-29 12:55:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d451b453-54c1-35b4-8fad-f12457acd775 | -3.8412 | -44.1513 | 2024-10-29 12:55:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| febb81a5-fce0-30da-b5e3-5f782852ca5a | -11.138 | -55.5313 | 2024-10-29 12:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 413.2 |
| 6a947a43-bea6-35f1-bced-cbbc2084f0b4 | -11.1378 | -55.5515 | 2024-10-29 12:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 7bb683b5-48e8-3884-997b-150b96b1c82c | -12.8888 | -44.5909 | 2024-10-29 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5a0b1247-671d-3db8-af24-dcea757d8d93 | -12.8883 | -44.6143 | 2024-10-29 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 2de0528c-afa4-3d90-bd5f-3ceb4fba6322 | -12.9077 | -44.6111 | 2024-10-29 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 22d06473-ed44-3b00-a065-925fb2c93434 | -13.6222 | -45.5838 | 2024-10-29 12:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c5c0e6d7-fa09-30ac-984e-fcc177fd23c3 | -24.0128 | -54.1286 | 2024-10-29 12:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 85ed6009-4c8e-3231-be65-0cea1487ad8f | 3.5817 | -51.2759 | 2024-10-29 13:04:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 68742b9a-bdb9-398c-83e5-086462ce2d58 | -3.8412 | -44.1513 | 2024-10-29 13:05:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| ccc76165-8483-36c3-a08d-4dbff91b6c85 | -3.8413 | -44.1283 | 2024-10-29 13:05:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c5cd0fd3-cd72-3255-829c-4fe2a323dd13 | -4.3473 | -43.779 | 2024-10-29 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 613.2 |
| f4931ca2-25f4-33f1-8979-599f892b8691 | -4.8606 | -42.6275 | 2024-10-29 13:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3be0fdc9-4d3b-3ded-a157-1d15a19a0b7c | -4.8619 | -42.4622 | 2024-10-29 13:05:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| e7af26a0-e0a6-3e00-822e-a59cd75fa893 | -4.8617 | -42.4858 | 2024-10-29 13:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 867ba52c-2440-3296-8020-e6f867bd315c | -11.1378 | -55.5515 | 2024-10-29 13:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 47cb894a-1a2e-3306-9e99-1935ef19a8f9 | -12.7145 | -48.8477 | 2024-10-29 13:06:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b4121fe1-5b09-33c3-8744-a6d36956b1c9 | -12.8883 | -44.6143 | 2024-10-29 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 321.5 |
| 4e5582c1-aee7-3b5c-ba5d-a23d9cc98976 | -12.869 | -44.6175 | 2024-10-29 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9ce134ab-c04f-3272-9bb3-91dea7eb5a23 | -12.8888 | -44.5909 | 2024-10-29 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 8383a026-b953-3703-8bce-5650168c4fe1 | -24.0128 | -54.1286 | 2024-10-29 13:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| af6a70f3-6e54-348a-b780-f0f2f41c21e1 | -3.8558 | -41.7873 | 2024-10-29 13:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 10b31e14-3824-3606-81ae-3df99e685291 | -3.8413 | -44.1283 | 2024-10-29 13:15:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d84d35a4-577a-3f92-98cc-ec9dae590325 | -3.8225 | -44.1522 | 2024-10-29 13:15:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c685114f-51fd-30bc-b614-31cc17edc443 | -3.8227 | -44.1293 | 2024-10-29 13:15:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 732397b7-246a-350a-b19f-afb91fbf31c9 | -3.8412 | -44.1513 | 2024-10-29 13:15:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e5029145-f2e8-32f7-b609-a360c981eb1c | -3.8745 | -41.7862 | 2024-10-29 13:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 45475485-930c-38c7-b6ac-ac4e2926ae73 | -4.3473 | -43.779 | 2024-10-29 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 640.3 |
| 2fed770f-a5d4-3f5e-810e-5d1808da9ddd | -4.8617 | -42.4858 | 2024-10-29 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 834e5653-59bc-31d0-8f92-1d235663c2ce | -4.8606 | -42.6275 | 2024-10-29 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| ff5398f3-3d92-311b-82cc-a682264ba205 | -5.2848 | -43.4179 | 2024-10-29 13:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 266.7 |
| b111ad5d-35e2-32ca-b3a5-db93f915074b | -11.1378 | -55.5515 | 2024-10-29 13:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 8f3cc553-ed59-3379-9c95-3698598c6a64 | -12.8888 | -44.5909 | 2024-10-29 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 4fd5cd97-6cdc-3a8f-af47-a7a9ca2d5510 | -12.869 | -44.6175 | 2024-10-29 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| dde50625-b8ce-396b-9a11-734226d7f8cd | -12.8883 | -44.6143 | 2024-10-29 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 319.7 |
| 9da3e945-4061-3cb8-b1a8-8a3fcaac2585 | -12.9077 | -44.6111 | 2024-10-29 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 01ecbccf-86b6-30cb-9bbd-79bf3ef0b28f | -12.6953 | -48.8503 | 2024-10-29 13:16:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7f225f34-cd56-3efc-a551-6ec29e46600e | -12.7145 | -48.8477 | 2024-10-29 13:16:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d1f3a228-0ab0-30ac-a73b-f0a26ec9b307 | -19.4866 | -56.6857 | 2024-10-29 13:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 093b0345-57d0-38d6-8434-1db3ae34bd13 | -24.0128 | -54.1286 | 2024-10-29 13:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 7448e7a8-d349-39f3-8850-c4d978c9e232 | -1.3471 | -54.6577 | 2024-10-29 13:25:14 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 52c335ae-c1ef-33f2-8171-175b8a4f9146 | -3.1037 | -42.5825 | 2024-10-29 13:25:23 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4de0601b-ee45-3e36-be8b-6fade87e2bb8 | -3.1038 | -42.5589 | 2024-10-29 13:25:23 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b42d361a-8ca8-3495-9a4c-c7a08e3b80d6 | -3.6648 | -42.4384 | 2024-10-29 13:25:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 21000728-b5ba-3dc5-9abc-8a748df1a98f | -3.8227 | -44.1293 | 2024-10-29 13:25:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ef8a8ce0-770f-32de-a15c-8cc7b023ab36 | -3.8225 | -44.1522 | 2024-10-29 13:25:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 70be580d-d508-32fb-803d-08dc72439831 | -3.8413 | -44.1283 | 2024-10-29 13:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ac367241-1fd3-3bb4-a34d-671df3cd6bce | -4.3473 | -43.779 | 2024-10-29 13:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 713.6 |
| 7db46517-94d6-3c31-acb0-4d4b0c09aaec | -4.8606 | -42.6275 | 2024-10-29 13:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| cb11f98a-60cd-336b-8420-a2609bcbf063 | -5.2848 | -43.4179 | 2024-10-29 13:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9935246e-b001-32db-94ba-09105ff3d437 | -6.3534 | -41.581 | 2024-10-29 13:25:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| f59fcb43-b5ae-3411-a16e-a3a4b33494a9 | -11.1378 | -55.5515 | 2024-10-29 13:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| c1ed4305-455b-3b38-945b-a21f1961e74d | -12.7145 | -48.8477 | 2024-10-29 13:26:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 662b4b0b-ec50-3de1-94be-d1a0b07d9b0d | -12.6953 | -48.8503 | 2024-10-29 13:26:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5dd71982-a037-35fe-a1e5-02eac706a579 | -12.9077 | -44.6111 | 2024-10-29 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2f1ed882-a897-3a0d-8091-cd8f7424b3b5 | -12.8883 | -44.6143 | 2024-10-29 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 287.4 |
| f2e8aaa7-475d-352f-9404-aa908a682b31 | -12.6956 | -48.8283 | 2024-10-29 13:26:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 638b4787-bcbb-37ac-b74f-882b9fa43a03 | -12.869 | -44.6175 | 2024-10-29 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 039bfca1-40ae-3817-8ef2-eb18bb1ea366 | -12.8888 | -44.5909 | 2024-10-29 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 338ebff9-969c-33da-8ca7-bd745ca19ac5 | -19.6067 | -56.6898 | 2024-10-29 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 22a643c4-98ef-3b45-b7a4-1849c1dd65e4 | -23.9917 | -54.1329 | 2024-10-29 13:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 1af29f7a-6989-3962-8b18-a927bb641629 | -24.0128 | -54.1286 | 2024-10-29 13:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| c6002788-9c34-3131-8c13-e87a02f15c7b | -3.1038 | -42.5589 | 2024-10-29 13:35:23 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c8ad5a01-aeb4-3704-807c-17373aab9610 | -2.9641 | -53.8682 | 2024-10-29 13:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5a29e763-338a-39b3-b65b-a284fcfa54ea | -3.1097 | -54.2865 | 2024-10-29 13:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a7388932-ac1c-3dce-9fb7-582a27e48b55 | -3.0734 | -54.167 | 2024-10-29 13:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 685b485d-bd69-365f-ab8d-bc791641fb4b | -3.3986 | -43.2714 | 2024-10-29 13:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1be0fc1e-4f98-30c5-8f93-cfe47e83d86f | -3.6648 | -42.4384 | 2024-10-29 13:35:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 3734c956-2be8-3819-8acf-8d9cb4cb0f7e | -3.8225 | -44.1522 | 2024-10-29 13:35:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| aead943b-b711-3167-8738-1623d45a649b | -3.8227 | -44.1293 | 2024-10-29 13:35:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1fd9efb1-bc77-385a-afbc-d891ca26a513 | -4.3473 | -43.779 | 2024-10-29 13:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 677.6 |
| 0dc889c1-3a09-340c-baa9-a48d4b2b164c | -4.6988 | -39.4141 | 2024-10-29 13:35:32 | GOES-16 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 9ea11899-292f-3fca-8ce0-ee9888c9d658 | -4.8617 | -42.4858 | 2024-10-29 13:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| a7799c49-2fee-3b2e-8a9f-7fc61b5356c9 | -4.8619 | -42.4622 | 2024-10-29 13:35:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| da0bd7c9-1541-37b6-b32e-fdac16d906e8 | -4.8606 | -42.6275 | 2024-10-29 13:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d13c7745-5e12-31f1-a84f-8ad5360d9a89 | -4.9496 | -43.2078 | 2024-10-29 13:35:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e4ddf60a-74e4-3287-af74-ad9eca63e252 | -7.0157 | -41.3481 | 2024-10-29 13:35:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| f779c408-bb4f-3ef3-aa00-9255fea49161 | -7.016 | -41.3239 | 2024-10-29 13:35:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 6e4cd4c5-0b76-3e3e-9c0c-4defd3d3e27c | -6.9971 | -41.3258 | 2024-10-29 13:35:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| a9b43fcb-1df6-3160-a24f-1aef9773c7b4 | -6.9968 | -41.35 | 2024-10-29 13:35:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| bab71570-7e9f-3c51-8e02-ffef907290a0 | -12.8883 | -44.6143 | 2024-10-29 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 309.6 |
| d3208991-375c-3b65-b6dd-1d29a42fbe92 | -12.869 | -44.6175 | 2024-10-29 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |


[Clique aqui para ver as próximas entradas](README109.md)
