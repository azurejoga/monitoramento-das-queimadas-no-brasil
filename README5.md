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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 504ac8e9-daa8-304d-b79b-bc5b5f182dd9 | -12.24761 | -63.84312 | 2025-01-24 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888211f5-7816-356b-bc08-c04c41b486b5 | -11.6544 | -58.20281 | 2025-01-24 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c379473-4ccb-3c5a-870e-fbd462a832cc | -12.37911 | -64.00381 | 2025-01-24 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf23dde9-a8e8-3c05-b190-87da4e290a49 | -15.24687 | -60.22314 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71358e1b-1062-300a-98f5-4e4bf6712e71 | -9.26253 | -60.3173 | 2025-01-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4ba1ceff-2ecb-3c7f-9015-8844df7235d2 | -9.25789 | -60.31665 | 2025-01-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2fd3105f-81d3-3f44-b0bb-c7d2d58dfd8d | -12.78864 | -61.49847 | 2025-01-24 05:50:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d19d1d3-7a95-39e3-bd96-617277a8c02c | -12.79113 | -61.49739 | 2025-01-24 05:50:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13a207e3-d94e-31ba-b658-e54d3ddcb274 | -9.17927 | -61.94571 | 2025-01-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 842d0459-2d4c-3a18-9244-789bbaa3f0f5 | -9.2632 | -60.31238 | 2025-01-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 107d953b-01d0-3d66-89e1-83225db68ea9 | -12.95265 | -61.34183 | 2025-01-24 05:50:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc2dcadd-18cb-34de-99b0-76911c69f348 | -16.17862 | -60.14292 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4c3f689-ee70-33c1-ba17-4b809bc706d6 | -16.10274 | -60.07075 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd1fa358-c38c-38a6-92fd-2d9fb1fe94e0 | -16.17271 | -60.14858 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3828620f-e354-3f92-8a01-6dd4072820f5 | -16.17307 | -60.14543 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4972e31e-cc46-37a7-b5a5-fe3070a2d7a8 | -16.17344 | -60.14227 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c111976-092f-31f6-aba5-468be0dd01ec | -16.1749 | -60.14618 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f80f35e0-ff76-3976-a047-83b389b8bed6 | -16.17525 | -60.14302 | 2025-01-24 05:52:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a56b0531-6e5b-3efa-b117-df8197d3dac4 | -9.259 | -60.309 | 2025-01-24 06:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a1645cdb-e8db-3b0b-b780-090770675ca8 | -9.259 | -60.309 | 2025-01-24 06:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4578176f-7f08-3d67-80de-d865ef86bc88 | 0.87934 | -60.15656 | 2025-01-24 06:12:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1c321d6-ac5e-3599-9f7a-52ac26d35be7 | 1.11182 | -59.4612 | 2025-01-24 06:12:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ebd6ae-2366-3982-8839-3a54aa183ae4 | 1.10528 | -59.46236 | 2025-01-24 06:12:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 721ba100-99ac-33f9-b672-c98fc2dbe198 | 0.88561 | -60.15541 | 2025-01-24 06:12:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1452233-2fad-3331-bd92-fed166987d98 | 1.11105 | -59.46313 | 2025-01-24 06:12:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 081b88aa-0239-3169-8cc4-1bb9239cf05b | -9.25884 | -60.31508 | 2025-01-24 06:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 658743d7-36b8-3559-821c-cdbfd9f52d7c | -9.26259 | -60.31371 | 2025-01-24 06:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1247a556-85b4-3c3f-bbfe-5a384716bebd | -12.37755 | -64.00439 | 2025-01-24 06:16:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3027f8d2-686f-3017-95e8-a380d70d0866 | -12.94994 | -61.34356 | 2025-01-24 06:16:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee97d1af-b15d-32da-b7c3-d8c54fd1f5ed | 0.88551 | -60.14487 | 2025-01-24 06:37:00 | AQUA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 19ddb506-ebe5-3e84-a451-083b9b128f50 | 0.88694 | -60.15451 | 2025-01-24 06:37:00 | AQUA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a2cd5e11-f467-30f3-9871-c08f70b8508f | -9.25902 | -60.30888 | 2025-01-24 06:39:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 8fd4d6b1-d894-3b9d-b309-0dc62f722431 | -9.25724 | -60.32174 | 2025-01-24 06:39:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 155f6e4d-ca02-3e7e-955b-1821dee314dc | -6.5631 | -51.1126 | 2025-01-24 07:00:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1c334bc5-2697-3c0c-bcee-7a58ccd7cd76 | -15.83 | -43.46 | 2025-01-24 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c31fa5e-eb06-3ba7-87b7-084fe90ce4bc | -15.39 | -43.83 | 2025-01-24 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b758c99c-0597-3e24-8e92-1488e27c5ea2 | -8.16393 | -43.94645 | 2025-01-24 12:44:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 41fb1c67-d907-3b6d-ad78-0e376dcbac3d | -11.80569 | -46.78209 | 2025-01-24 12:44:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9367a70b-36f9-30bc-95c3-41cbb35c2b88 | -9.22757 | -40.01255 | 2025-01-24 12:44:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 51.3 |
| d8970f3c-453b-3942-b1f6-7d0cb7ffd845 | -11.48621 | -46.96283 | 2025-01-24 12:44:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f0a26f9-8c80-3c75-85aa-f2b843e56d98 | -9.81539 | -48.42805 | 2025-01-24 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 95d694b8-1361-38f9-b2b4-6cccd13cf145 | -12.79717 | -44.83797 | 2025-01-24 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| afea7184-014e-3b76-987d-6c540abfb670 | -10.71069 | -52.01538 | 2025-01-24 12:44:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 67570fd7-8183-30e7-b27a-290dbf36d21b | -10.91993 | -39.56641 | 2025-01-24 12:44:00 | TERRA_M-T | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 40.1 |
| 8dc98afa-8dfb-3518-9a70-fda11eae0bbf | -11.49436 | -52.92407 | 2025-01-24 12:44:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d0255c7b-ca22-345a-8906-70714227cadb | -10.21069 | -44.21587 | 2025-01-24 12:44:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3dd3b879-7fb6-3448-9609-8b2dcd8f3b60 | -9.22033 | -40.00487 | 2025-01-24 12:44:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.4 |
| d0802bef-66dc-3122-a8a8-1b1d57a5dfdb | -18.0694 | -49.96469 | 2025-01-24 12:46:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c00b5e51-0d01-3154-aa48-a125263f55ea | -16.87824 | -49.2546 | 2025-01-24 12:46:00 | TERRA_M-T | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e04c211-639b-3f5e-945b-876c3f9d7ff5 | -13.2337 | -52.53896 | 2025-01-24 12:46:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 29cc12d0-ca09-33b7-8341-d54353cbe733 | -13.40209 | -54.49454 | 2025-01-24 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 616cc330-47f9-3dbd-9572-bf0f345756b4 | -13.79088 | -54.30067 | 2025-01-24 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9b98452a-491a-3108-b7e7-680d15356dc0 | -19.05397 | -53.45102 | 2025-01-24 12:46:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d16cc6be-4185-3c3b-b711-5ec8f5e3d4c5 | -14.11057 | -45.68644 | 2025-01-24 12:46:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a82c5e9b-b2e0-33bc-b2a1-e3e6ca52fbe3 | -13.09082 | -52.26421 | 2025-01-24 12:46:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e613b437-f0cb-3ed0-ae41-c5ed2b396c56 | -16.40127 | -55.15054 | 2025-01-24 12:46:00 | TERRA_M-T | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ee3aa8e9-97cf-3ac9-820e-342b2d26f6d5 | -18.0241 | -50.42731 | 2025-01-24 12:46:00 | TERRA_M-T | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 31a8f217-b133-35b2-bb9b-e62fe9d39cd2 | -15.27568 | -51.47206 | 2025-01-24 12:46:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09f6ac2d-34bf-3daa-a8cd-d4bcafa5d7dd | -14.25755 | -45.78688 | 2025-01-24 12:46:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 552e39a4-e6e8-3a07-8d1a-7bbd93327d88 | -17.69609 | -50.07207 | 2025-01-24 12:46:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 22dc358d-293d-30f0-83e9-97e7a72df7b0 | -12.87861 | -52.51094 | 2025-01-24 12:46:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5b8dd5ac-d1f1-3a2a-819f-f1a0220b50bb | -14.11054 | -45.68036 | 2025-01-24 12:46:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| d1a75da6-72bb-3076-ae64-da5a9d5af001 | -18.57808 | -50.14921 | 2025-01-24 12:46:00 | TERRA_M-T | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 7a252fba-ec93-3e99-9c63-8c767cbc0272 | -14.2458 | -43.61883 | 2025-01-24 12:46:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 749b1290-c193-3b2f-b18f-4dd52aee0876 | -20.59122 | -48.51847 | 2025-01-24 12:46:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a9855d86-3ba5-3bb9-8849-a288e339be82 | -21.01244 | -47.66913 | 2025-01-24 12:46:00 | TERRA_M-T | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e736d141-e6fa-3b26-a58f-a7ad65439497 | -17.72715 | -50.04726 | 2025-01-24 12:46:00 | TERRA_M-T | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9e00bc5-5633-3ba0-aa7d-337e1690a4e3 | -14.10863 | -45.69539 | 2025-01-24 12:46:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| d90cb18d-ced8-3e8e-8040-349e8ae44ecd | -20.58971 | -48.53061 | 2025-01-24 12:46:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cff33fd4-f511-3f50-9a9b-e8105df16871 | -22.72023 | -47.01321 | 2025-01-24 12:48:00 | TERRA_M-T | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| d095b025-8f8e-3659-a5df-cbcbad053eac | -22.80056 | -47.11322 | 2025-01-24 12:48:00 | TERRA_M-T | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ae73793e-5a14-3619-839a-86a7bb62680c | -22.06593 | -46.96718 | 2025-01-24 12:48:00 | TERRA_M-T | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 33abd146-70cd-3c7f-85c9-6a31797b0723 | -22.7229 | -47.00767 | 2025-01-24 12:48:00 | TERRA_M-T | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 2e813550-da19-3996-b957-82b74ce242b3 | -22.83782 | -47.59741 | 2025-01-24 12:48:00 | TERRA_M-T | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 2246d3d9-7e84-33a4-8386-d0801b089573 | -22.22404 | -47.7831 | 2025-01-24 12:48:00 | TERRA_M-T | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6a1983db-8556-3d4a-98bf-8f2eb25aa417 | -21.58031 | -50.78883 | 2025-01-24 12:48:00 | TERRA_M-T | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 36c3e0b1-a155-37a5-98e1-ef2261fbd664 | -23.32744 | -47.2984 | 2025-01-24 12:48:00 | TERRA_M-T | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 59eb8be5-75c7-3eb3-8d09-eab7a0e87953 | -22.80262 | -46.28756 | 2025-01-24 12:48:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |


