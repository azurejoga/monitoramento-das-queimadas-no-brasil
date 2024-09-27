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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fee1b70c-1277-378d-90d3-57bccf5c32b5 | -14.72077 | -45.50165 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e53bbd2-94e9-3c92-a5bb-35b42869b69e | -14.72025 | -45.50564 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e3689e7-6407-3d5f-a7cd-c3e0e4a8d528 | -14.7176 | -45.493 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8b4e9f1-bf59-3b25-ad06-608f98d1c9a8 | -14.71708 | -45.49699 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f45952f-ee5d-3431-b955-9fce423fe22e | -14.71391 | -45.48838 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73a1e9a2-7c14-3666-9e46-b03ab83d68be | -14.71021 | -45.48384 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d616d9b5-c972-3e87-bdff-67d3805dd6ab | -14.7065 | -45.47931 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77f5e2cb-8b45-3071-81ec-58a237f291c6 | -14.70329 | -45.47088 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daff639b-8177-3b1e-b195-a5937b029441 | -14.70243 | -45.47267 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f67d120-9ecd-3f0b-9c60-6cabbe5dd690 | -14.69908 | -45.47029 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1416a6a-47b7-3f3a-9d3f-5a3d3c47088e | -14.17317 | -46.44294 | 2024-09-27 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 907cf77e-dee0-352f-a311-3fb94c0466e2 | -14.16992 | -46.43734 | 2024-09-27 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b49ed86e-b951-3c02-871b-55fd23e5b8ab | -14.16924 | -46.44239 | 2024-09-27 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd93cf0d-c4d7-3883-8b83-d813cfa56ef6 | -16.54772 | -46.93022 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb49548a-a4e5-3ac7-9c7c-fa6de62b68da | -16.53451 | -46.93897 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a70f17ed-e694-3736-9d55-09b60ac7433e | -16.53131 | -46.93293 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8539c5f9-2b18-39fe-b3fc-2c8ffde1a837 | -16.5306 | -46.93822 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 041d7925-c330-3d6e-9ff9-df3a0d227c45 | -16.50354 | -46.96081 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6aed780-7df0-3238-b10f-01608dc166e2 | -16.49962 | -46.96019 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e70f708-c098-3ec2-93fd-0522a4d6120c | -16.495 | -46.96484 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b881262-2b02-38e9-af43-5ae4fcd2b69e | -17.84051 | -46.50661 | 2024-09-27 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cba77c7b-9847-3b1d-a64f-fb6cc36db051 | -17.4996 | -47.01824 | 2024-09-27 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37400ffc-58e5-3f19-bc7c-4b801324910c | -17.24342 | -46.28563 | 2024-09-27 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba4b6ca0-0c52-39db-bd1e-78db5cc1906a | -17.24291 | -46.28952 | 2024-09-27 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d62980ee-5735-3247-b906-c8a62e938ac1 | -17.23928 | -46.28505 | 2024-09-27 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6495eb70-b7b9-3936-91cd-ec4f47a12fdc | -17.23878 | -46.28895 | 2024-09-27 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 021182a9-ed6a-3908-ab3d-075708db2831 | -16.98878 | -45.91795 | 2024-09-27 04:42:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21e6c48b-4088-34a8-b0d1-fb0515cbae5c | -16.6193 | -47.29795 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8aeffc86-45ac-3e33-a13e-2fb76c31539d | -16.5786 | -46.93626 | 2024-09-27 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e976c5a-e2ad-302e-b5d8-57d9d892fc98 | -18.91666 | -47.20345 | 2024-09-27 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02d68a75-4ede-3dea-83de-fe934eba1d85 | -18.91266 | -47.20289 | 2024-09-27 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad647e5d-55d7-3974-89b3-f74379a2e876 | -18.89557 | -47.1007 | 2024-09-27 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 843e17e9-aa5d-3ab0-827c-daba34d0072e | -18.60142 | -46.41375 | 2024-09-27 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d472a152-9909-3339-869b-0ef424ca4121 | -18.57673 | -46.74448 | 2024-09-27 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd6ec7a0-c8e5-3f37-8210-d82d8ed2d3c0 | -18.54582 | -47.26732 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f694744e-f780-3c9f-b9da-21fc4d90b1e2 | -18.54088 | -47.08829 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d4bd1fd-ac31-3360-bce6-cb4f6c7d1c80 | -18.52937 | -47.08272 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1799f0f-c72e-3f72-99f6-6f5f3cd761a1 | -18.52538 | -47.08198 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e990f9ac-794d-3b18-bf2f-f8f987e207df | -18.52043 | -47.08886 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f25d6a8-5d4f-3486-bf1e-daaa32e93d85 | -18.51996 | -47.09248 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 861150b5-bfb5-34de-800a-db3b8e88a6af | -18.50753 | -47.09415 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab26e4e1-dd73-34f6-8187-e6d9949ec6b7 | -18.50706 | -47.09784 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a9c513a-93a2-32e0-8e24-290e79056349 | -18.50215 | -47.10447 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4265962-1571-393f-8e54-6f8c679a893a | -18.49817 | -47.10374 | 2024-09-27 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e373e3b3-5ea0-3ecd-a11a-db291d95de1e | -18.09432 | -47.44495 | 2024-09-27 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46608a6d-cdad-30d8-9da7-b0527d9167a1 | -19.98682 | -47.1596 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9ab69b76-58e5-33d4-bacc-8e3cda9960fe | -19.98276 | -47.15902 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f81ad2e4-ced6-394b-8147-d741a4915c29 | -19.98229 | -47.16288 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab2b1e9e-e153-3751-92ce-fc5699db0749 | -19.83549 | -46.94464 | 2024-09-27 04:42:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e873f2-fcb4-315e-9b86-bf499c3b7271 | -19.77958 | -47.02644 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feac4e37-4596-3fe3-b8a6-2a9817a491df | -19.75953 | -47.25682 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6745d44d-255a-3f4c-a6ef-a7e4b6ad217a | -19.7555 | -47.25626 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2573a9f-b004-3def-a601-c108283022c7 | -19.75505 | -47.25993 | 2024-09-27 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eac46b36-c26f-3ad7-adfc-7a2f9ad59d98 | -19.5994 | -46.97778 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d731660-3ee1-3b4c-8b9e-b9b4dbbaebb2 | -19.59892 | -46.9816 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d86fe28-5b49-321a-96f7-c88dff0c013a | -19.59845 | -46.98539 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09b13f67-8e00-30a9-9a7b-78e54c43cd7e | -19.59578 | -46.97335 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07645462-1785-3e99-8d8b-787b5dfc75f9 | -19.59531 | -46.97721 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91fe3e36-7a4e-3dcb-893c-173c014564c5 | -19.59484 | -46.98101 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 388233de-ace2-3eb4-9ec8-b2f51d2379be | -19.59437 | -46.98478 | 2024-09-27 04:42:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a82a315-8e37-33fc-8196-4fe61bb6a4bd | -19.56477 | -47.79226 | 2024-09-27 04:42:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86dd10f5-0abe-3726-bb12-3af32e2118b7 | -19.53175 | -47.88444 | 2024-09-27 04:42:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b263f46d-8d03-3ca0-bcc8-34f00e397487 | -19.52788 | -47.88386 | 2024-09-27 04:42:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 834c024e-2b62-337a-b6b4-1d4143f959b3 | -19.52402 | -47.88329 | 2024-09-27 04:42:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e90f13e-7b36-343b-80ce-d5830e2dfef9 | -14.60615 | -48.16052 | 2024-09-27 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5567a5e8-14f2-397b-af24-23363d8694d5 | -14.60314 | -48.15599 | 2024-09-27 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6df3673-12e6-30ed-b478-57c220924c44 | -14.60255 | -48.16005 | 2024-09-27 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9bb73d2-5705-3647-b3c8-aa26eba0fa1d | -14.59896 | -48.15952 | 2024-09-27 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b5bd4f7-778a-3c83-8e56-ae87a8177dea | -14.19045 | -48.18787 | 2024-09-27 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6d8440f-1ee0-3450-8659-db86f259b48d | -13.83654 | -48.03133 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4773e144-d27a-33ea-84b4-6e881b443dc5 | -13.83296 | -48.0308 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c567090b-7b83-34ff-843b-783f58d1dc8c | -13.82938 | -48.03027 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d875cc-4510-36c6-b244-2cce88f09de7 | -13.81197 | -48.12709 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e864256-36a6-35ed-80d6-f0ab91107cbf | -13.8114 | -48.13102 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fddff4a-6577-3ecc-ace9-f49b10a62f07 | -13.80787 | -48.13029 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe9b08c6-2b9f-3a9d-9b2d-99782b4a69ff | -13.80433 | -48.12956 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd852729-03a5-3341-a2ca-a6f042be4186 | -13.79726 | -48.12799 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ba60353-ca70-3c44-9c76-45cf75094e71 | -13.77891 | -48.10965 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea1ee6a3-6d9e-3408-b938-37abb3340e0a | -13.77358 | -48.09626 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b807cf4e-07fe-3786-8b6f-0a7973086133 | -13.77297 | -48.10039 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eabc8ecc-5164-3043-8b18-cb93eccdb656 | -13.77238 | -48.10451 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c1c3dfd-896d-3c3f-854a-0453f9ab1ad5 | -13.76882 | -48.10387 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f49cfe0-7601-3b3f-84ae-1160f3f8828a | -13.76824 | -48.10792 | 2024-09-27 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9f0cbd8-a645-349a-9ddd-d229ad113059 | -13.73205 | -47.58232 | 2024-09-27 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 220d2bcb-e112-3883-a0e5-923f4173b798 | -13.73144 | -47.58653 | 2024-09-27 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8ea897-cd52-3f42-965f-84e76e4ee9f3 | -16.51473 | -48.05143 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c87be4c8-d1fe-3bd8-94a0-9a947501633b | -16.5141 | -48.05607 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db6bb55b-efff-371b-8da2-8825e2116bd6 | -16.51157 | -48.05283 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 59a5deec-b9fb-33e7-82b2-bcd90a996b4b | -16.51105 | -48.05084 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b319345e-781f-3ecd-b1ad-cbb4d3c63102 | -16.51042 | -48.0555 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31aa096c-baa6-30a6-b9b5-3e33fcb4f29b | -16.50789 | -48.05224 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3427c90f-6db4-389a-b974-edee299dc677 | -16.50674 | -48.05491 | 2024-09-27 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73a464eb-461e-35cf-a2e5-051e47e07f94 | -15.73187 | -48.31569 | 2024-09-27 04:42:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2e4f77e-7586-33c9-a50e-90bcdf9f60c7 | -15.67445 | -48.19002 | 2024-09-27 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7270bf7-7036-30f2-9aca-26509235c5da | -15.61363 | -47.23551 | 2024-09-27 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bd4e957-2dd4-3fef-803e-c23db88ede97 | -15.56849 | -47.85666 | 2024-09-27 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a0c92b8-1ed8-3a39-a85b-1d9fab236360 | -15.50792 | -47.30149 | 2024-09-27 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b25b60d-f178-3eef-891f-5650e12ec231 | -15.37772 | -47.45977 | 2024-09-27 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4bfb52-1605-3336-b9a2-1fb36d032b63 | -15.37635 | -47.46957 | 2024-09-27 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1a528c-7fdd-386d-8b7e-f752bc9d4a69 | -15.37095 | -47.45336 | 2024-09-27 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README103.md)
