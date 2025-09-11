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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3419831-b53a-3581-b2ef-0d952b72ec9b | -14.92011 | -55.93407 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22c0c4a3-24a4-3687-b018-a1b6b368bf9c | -14.7159 | -45.34409 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 474bcb73-4943-3956-bdfb-ed5e44b619c6 | -10.32196 | -48.80463 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4f37c08-a6e6-395a-b610-eb8718800121 | -11.47111 | -43.68128 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 195b02e5-362b-30e3-9fd7-8b33be34aa6e | -14.51413 | -53.9645 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7801f044-f690-37c1-881e-58e42fab452c | -11.42702 | -43.58017 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 269ab45b-166e-3cea-a2d4-3b21c009fb03 | -11.15837 | -52.04511 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fd3a7a0-a0fc-3a4e-82c5-3ac75ac9d392 | -12.25471 | -47.32026 | 2025-09-11 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc49c27d-cec0-3f2f-9d89-1e3af8bd85c1 | -12.92783 | -54.75645 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1911a124-303b-30b9-ac69-709aa7faf3b2 | -9.19169 | -51.81074 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2c8e9895-9fc9-395e-9c07-d34eb0d63d20 | -11.45459 | -43.60876 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c9de56fc-f68b-3562-bea5-9c8e765d378e | -14.42271 | -52.94246 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7ed32dd-1172-3cbd-8f53-6c1ce6ad3042 | -9.02736 | -49.77966 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc6c5e93-0299-3bfd-a4b6-266b770973a2 | -11.08382 | -51.34775 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84a1285f-1814-3cb2-9255-b09c15254b1d | -11.46365 | -43.61908 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfa7736b-9160-31bd-b4c8-fb21585190e8 | -12.84546 | -52.95116 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d9eb8b-8dc7-3a1b-9928-23b326c5f24e | -12.95457 | -54.74523 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c7d1a06-5f8f-33bc-9d52-6b8ac8a3bd3e | -10.0654 | -50.38507 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fc9b839-5191-38bb-9fa4-f51072ab9f33 | -15.14126 | -52.44975 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 551ebde3-30ac-3a42-9814-7693a5ea126e | -10.26864 | -43.82883 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83039a28-b1ab-315d-b663-ec1bd062d33b | -16.06697 | -49.97244 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1b845f7-55b5-32e9-b786-e1c92fb8eaca | -10.02291 | -51.72995 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6617498c-cb6f-3088-9fc2-b9e19f287bea | -12.42926 | -47.81267 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34498f5b-7536-35ef-87ed-905a6cc99250 | -11.09809 | -48.44986 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ead5b14d-5c7f-3339-b188-ad65a5f3b0ca | -11.46087 | -43.60035 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac53bc22-627b-3ca8-9d7f-353b514ad6da | -8.56859 | -51.34738 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd68ed0c-fb83-3854-a5f7-92573e8723fd | -9.79066 | -51.1074 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdfcd5c3-c54b-3d6d-adb0-68365ba313b9 | -15.80055 | -52.26393 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bff97cde-0166-3232-87a0-cf70e9795099 | -15.13351 | -52.43372 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d886031-14c3-3096-9436-157b7bb35a4b | -11.16423 | -45.30928 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71204bef-6700-3bdc-bec9-daf4978cba7f | -9.60576 | -55.01344 | 2025-09-11 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8b447f9-cdb8-3a6a-8456-f9762cd042a9 | -10.57137 | -51.50168 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb2a5d5-0bd4-34a2-96b1-c5294bf1bdd2 | -14.88162 | -55.84314 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b9b717d-f843-3101-8f9b-baf2e140cb68 | -10.18838 | -46.2136 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 857d4b60-577b-3f02-833c-131e4b0f67ac | -9.09511 | -49.81674 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27e51936-7299-3c7b-a7cb-4532e5ee33ad | -13.32639 | -46.37686 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fd30a23-ddff-3e1c-bcf6-80da21685066 | -11.96821 | -46.65458 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcdd8279-a868-3a77-9271-fdea18a90ae5 | -14.4061 | -47.31827 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b163922-2448-3aba-b426-83e3a925bdd4 | -11.65699 | -48.32369 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b02afac-24a6-3ee6-8d0d-433dbd3de575 | -13.58341 | -47.70018 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5d2289c6-8e0c-3a91-b190-182f13f6a5a0 | -16.05553 | -49.97483 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdfa2d9b-4564-38df-996a-f1e7b1c46f37 | -15.13543 | -48.61077 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 017520ff-a770-3d60-ac68-2548d89ceba9 | -9.72736 | -48.33316 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff248476-8984-3d9b-a8e8-ca775f3df91d | -15.79721 | -52.26337 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e405534d-fc1b-3cd8-b074-331b8e5d35b6 | -11.40122 | -45.60121 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fd5003d1-277a-38c3-a463-1d4836fcb8d1 | -9.84191 | -47.79052 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6140fd9c-e1ed-33be-baed-1b787e932723 | -12.40582 | -63.82253 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 570be77e-d3d5-3936-af29-159492e6ad77 | -10.53668 | -49.88503 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca2b6590-eaa4-3727-9698-ad1eed7a357c | -10.19289 | -46.2177 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8611acba-5af7-3624-b2c2-974498a120fe | -9.52072 | -54.63904 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6c3d45e-2d4f-391b-9e72-6b100d5d66d6 | -15.22601 | -44.05509 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd994953-b12d-3b12-9865-26ff2dfc2656 | -11.60038 | -52.2134 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efe6e83e-d76e-3bef-abe3-a72b6ed7b491 | -11.48514 | -43.67779 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880d9708-5886-3b6d-963b-02f834ec9734 | -9.67842 | -47.52767 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30b76868-7ab5-3443-9169-2a807995ea0f | -11.36247 | -46.54597 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1bda266f-d0a1-306f-8927-5184f35b1945 | -9.01546 | -49.51294 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85d2dc18-130a-3bf2-8c75-d3785d3df49b | -11.45615 | -43.59666 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbaf56c5-6f6f-3982-9323-002c0d89a72a | -8.49881 | -51.31523 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96b38c64-be80-332d-8903-941bc9c6acff | -14.90453 | -55.87555 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3be87722-2e5a-3592-aa22-d012bd4600a8 | -12.83996 | -52.94299 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a11c7d7-f75d-3d4e-941f-1e902c6f3091 | -12.56001 | -49.14661 | 2025-09-11 04:46:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ea2edb2-429d-3d44-ae1a-ba2eb8b0913b | -8.86095 | -52.01132 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e16b722-d786-3e70-b7ea-43bae3c44f18 | -11.71685 | -50.64455 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e498b5ac-6148-3636-a631-b7ff0bcff1f1 | -15.67384 | -47.02721 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ed5a1fe0-adfb-3601-9e20-f553cd0e37b0 | -11.4762 | -43.68194 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61b8e115-dfc3-36f9-b96c-da640d5cda3f | -9.60186 | -48.06337 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61513bbb-66c0-3fb6-a037-e30d9a1054e3 | -12.92848 | -54.75258 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc97a43b-3738-33f4-bfab-1eab249a4492 | -14.44315 | -52.94222 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1eb84e8-de2d-3f35-a328-1671a9ef4d5c | -9.6007 | -55.02133 | 2025-09-11 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72db3b5e-457d-3db8-8ef8-329c65937421 | -13.26335 | -43.74666 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83931779-3a76-3714-bf7c-f26d414c3664 | -11.43255 | -49.29896 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7987e786-2197-3ff3-8f41-bd31417470ea | -13.26411 | -51.7554 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f461277-b8f3-3b8b-a366-f05b6f18bb82 | -11.35578 | -46.53259 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4cebbe7f-9a98-35f7-941a-ebee895aa334 | -11.01998 | -45.06725 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| beec953a-f817-331e-942e-9e6d61081ef4 | -14.50311 | -53.9477 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a05c8a3-f21d-3866-9b03-fd0007621705 | -14.91869 | -55.83558 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d81585a-c744-329a-b613-c2831fb3f52a | -11.21912 | -54.9992 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f64cc7f8-d9ab-38c1-bbde-b7c9c4d36628 | -9.75498 | -47.85766 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 847d362e-e276-381e-a470-fe295daad692 | -11.22512 | -55.00293 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39015c1a-8c4d-33fb-8aef-f559d7e1d992 | -13.27245 | -51.72365 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 933b5580-38bd-3999-9189-4a40827e0188 | -11.47779 | -43.63019 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c6565f-1913-3a1f-96fe-226ce8e2fdff | -12.92178 | -54.77139 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75d414a-e7f9-3431-9335-09793b346fd2 | -9.01143 | -49.51619 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2bba8d7-2d98-37ba-a86b-897c4f399abb | -15.2167 | -44.04394 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1c564e2-fd24-3081-bbb6-d19ef62e9c4d | -9.02064 | -49.5021 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae5e0b29-801a-3967-a857-12973a1a3bf4 | -11.72247 | -50.6303 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| dd44c49d-0614-397a-b7b6-44896445c790 | -14.50193 | -53.95498 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26b4eb5e-478a-3cd7-9e27-67fed8e50aa8 | -10.31544 | -48.79897 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2172db30-215f-3105-85e3-c1aacc5a07fd | -12.83332 | -52.94189 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 500f6dd3-e51d-399b-b252-597e2c0392e2 | -9.56454 | -48.29588 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c5ab947-6dee-373e-b1e2-81f4cb016a89 | -14.56884 | -48.76688 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da2c018b-45b9-388f-b3fd-a56575d5e3f0 | -9.02394 | -49.77913 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19151a90-81e8-3489-a180-9ef7868b081a | -9.96483 | -51.68821 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d42edbb8-6013-3420-8af7-e135e654af32 | -11.41121 | -43.54008 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81d58620-f0bf-3a4e-a273-20b8997aea03 | -12.85822 | -52.9351 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75f00580-4ab9-3a43-9a70-02412672d5b3 | -14.92294 | -55.83206 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f252c84-4bc8-33a3-a011-314d41a63f4f | -16.29596 | -50.06476 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1791e1dd-de7e-3f3f-8b1e-84cf7eb25002 | -11.78294 | -50.5753 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf969006-2a1b-31f6-b2be-e9006e0166d9 | -11.22334 | -54.99576 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0549408f-48e0-3fb3-b7aa-b2b2f990c069 | -11.10425 | -48.43346 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README115.md)
