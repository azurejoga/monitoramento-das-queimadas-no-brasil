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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a49c8e50-8985-3239-afa0-91a3461057e2 | -12.4788 | -50.57064 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 069aae42-6475-3028-898c-e7d62edc0062 | -13.32702 | -47.47309 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c81b261-e083-36f4-a812-853a350e6554 | -11.13548 | -51.0694 | 2025-10-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3124009b-2e1f-384e-9550-f3e18fc01b78 | -11.84436 | -47.92574 | 2025-10-30 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e59d2b9f-a5cb-30e8-a922-3282af423416 | -12.49694 | -50.55841 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c85afda-afce-375e-8348-118bb26d2fbc | -13.30195 | -47.69989 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e24a513-6a21-37a7-a208-f42120f54528 | -12.48123 | -50.59655 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3b4a43-a391-31c8-a513-db11f3fe2eb4 | -14.249 | -47.31945 | 2025-10-30 05:18:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 587aadc0-ce01-385b-96d5-187eef1e33b9 | -10.91463 | -47.79329 | 2025-10-30 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 278741e3-841f-329f-970b-5d6a74ae083f | -12.49017 | -50.56849 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 838bb45b-6ad7-30c1-aef5-9b684f69c622 | -12.3653 | -50.14964 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fbfcd89-07a6-3335-b1d6-1dcaea832e63 | -12.50745 | -50.56348 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b87b3cef-9c19-3b5b-90bd-0d695f33232a | -12.50198 | -50.56275 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2848105d-3814-3e74-85f5-c5b2062543a8 | -12.30288 | -50.25922 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ee6fc39-365a-37f5-813b-2c5535d1a5af | -12.84669 | -48.62763 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8109d15b-0fd5-397a-8e07-fe8ec87994da | -12.18077 | -47.75481 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ce873f2-27a1-3188-95d3-ba192748edc0 | -13.37486 | -54.32742 | 2025-10-30 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9db757b-9224-3d12-b285-f1942d1c7150 | -12.48513 | -50.56415 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0c709596-c841-3e6a-b673-42b48d0ccfa6 | -14.24978 | -47.31182 | 2025-10-30 05:18:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df85f447-f673-3b4f-bfa0-d72134e2c041 | -13.16529 | -48.45971 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 501c32a9-7d00-3375-86d5-e6d2ff78142e | -13.16576 | -48.45555 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f0568d8-c8a1-3efd-a80b-ec8c57f4a3f9 | -11.13029 | -51.06868 | 2025-10-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52e69e08-b133-31c4-86b8-0ccacecc0cb2 | -3.7867 | -43.9011 | 2025-10-30 05:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4608c795-f273-3724-906e-9779b2dfddb5 | -4.2544 | -43.7149 | 2025-10-30 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 60e88518-d2b1-3d21-9fd5-92f7b0c48f5b | -4.2731 | -43.7139 | 2025-10-30 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e1222c5e-8a07-3da4-96b9-52d2522e38dc | -3.7867 | -43.9011 | 2025-10-30 05:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 33f46b42-960c-3a75-abfa-45caef91015a | -4.2544 | -43.7149 | 2025-10-30 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b477aacf-5b0c-3984-8e53-7a0c8afcf732 | -4.2731 | -43.7139 | 2025-10-30 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 54fcd93b-f5fe-323d-8046-595f2e7e48eb | -4.2544 | -43.7149 | 2025-10-30 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 932c57e3-eef8-3504-9934-576a5e242e6e | -4.2731 | -43.7139 | 2025-10-30 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 53fdc6d2-79de-30d4-9b5d-f8db31fc0df1 | -4.2649 | -59.6558 | 2025-10-30 05:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c5d393cd-2421-386d-a161-0374cec358e9 | 4.48636 | -60.72421 | 2025-10-30 05:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd8f8ef0-ed8f-38c4-a078-cd19083a82ad | 4.48945 | -60.76584 | 2025-10-30 05:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9785bc-850b-3727-9b2e-f6b98b1e1408 | 4.48983 | -60.7238 | 2025-10-30 05:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c46c47ad-5f51-338e-a1e9-a22942abfb6a | 4.16236 | -59.85804 | 2025-10-30 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f93c692-a9f3-344b-a0c7-d69c9bc9fdec | 4.15874 | -59.85854 | 2025-10-30 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7accea58-ffc7-3b63-b170-16d3642d6cc0 | 4.48539 | -60.76261 | 2025-10-30 05:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28b9df01-e55d-3b6d-b370-aa15d6a6fcfb | 0.44833 | -60.47531 | 2025-10-30 05:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf54da45-5f12-3849-835c-2d7e49743b35 | 0.83272 | -59.316 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ca45917-5ecf-3513-8e12-ea0b06e5808b | 1.60729 | -55.68687 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9470b3e-e9f4-3c6a-9185-cb74183b7483 | 3.75496 | -60.98105 | 2025-10-30 05:44:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 987bcb5f-ec1e-37b1-84f5-c21636df213d | 3.83221 | -59.84674 | 2025-10-30 05:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f1060c-90dd-3b80-9936-ef6c40e99243 | 0.31866 | -50.9276 | 2025-10-30 05:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4345fb7f-959c-3f01-b81a-5fe08121808e | 3.21955 | -61.19437 | 2025-10-30 05:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1782e1f6-dc1b-34fd-b911-12c3f232e026 | -2.052 | -56.87514 | 2025-10-30 05:44:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8b44b44-f1e1-367b-89a9-a71b54ac2c98 | 2.34186 | -60.21323 | 2025-10-30 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f2c0962a-bdc1-31b2-963e-58f452e1ffb9 | -4.52809 | -54.96581 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df694461-d1fc-3bd6-a976-9af8515cb648 | -4.53938 | -54.96786 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4913aeaf-6d15-302a-a0a5-44d0aff4c1b3 | 0.31807 | -50.92725 | 2025-10-30 05:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb9163c0-86bd-3d14-a8e6-b30f76cea1d3 | 0.44534 | -60.48015 | 2025-10-30 05:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6998fb65-3915-3606-ac74-0718950cade6 | 0.84205 | -59.3245 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8104a9c-d0da-39c4-8acc-4313336e7458 | 2.34548 | -60.21263 | 2025-10-30 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c6196602-5489-3fd5-b154-a04c39abba53 | 1.31425 | -60.40905 | 2025-10-30 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f16eb06-95e6-313a-afae-3976ce50bb4f | -3.42761 | -59.65239 | 2025-10-30 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eb7281b-726d-33f1-8d04-523366b81887 | 3.82859 | -59.84732 | 2025-10-30 05:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ba39c4-0fa7-3b4c-9d76-5f017cc8ce76 | 1.78471 | -55.67273 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b39ca89a-77cd-3172-94f7-768bfc584385 | 3.14396 | -60.69923 | 2025-10-30 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b25bf428-80cc-3507-97e4-00d1620dbc4f | 0.83739 | -59.32028 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fef8e7e-46bd-3fdc-a425-b606b9fab013 | 0.32547 | -50.92655 | 2025-10-30 05:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df7ee778-0288-37b2-81b2-869a2a6ded42 | -3.94302 | -54.75861 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adbec6ea-c1db-389c-91e1-ac33a354b56c | 0.44468 | -60.47589 | 2025-10-30 05:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 402c195e-b7c2-36cb-bc6f-ce75d334facf | 0.44827 | -60.47692 | 2025-10-30 05:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79ed11d5-ac9b-3462-9940-31a00c3f01b1 | 0.8335 | -59.32087 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93d6fd6a-1cbd-3dbf-a048-8b9ed91ec5b7 | 1.61583 | -55.69542 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 367da805-fd14-30b9-b961-4f78fc8299ee | 3.13983 | -60.69588 | 2025-10-30 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85146828-bda4-3acc-9f23-b1d88b1bfbc0 | 1.67827 | -55.64598 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6721e998-0ffa-3039-9af5-1cfbbe4d7712 | -1.21149 | -54.07518 | 2025-10-30 05:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d07a330f-fad2-3f1a-a270-9c83b6e486cd | -4.24537 | -55.87531 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c549fbf8-a655-35a2-8ef4-b67e42119f34 | -3.42815 | -59.64884 | 2025-10-30 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 594dd868-a059-3c79-9db9-c3b310402f81 | 1.61092 | -55.6962 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8790f70c-db3e-3c90-8b77-e55436bc4031 | 1.61391 | -55.69686 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f217454-9677-3a18-865e-0ac3590e01a9 | 3.62572 | -61.04764 | 2025-10-30 05:44:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc856190-3e6a-390a-982e-d3beb6cace5b | -3.94872 | -54.7594 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 030cecaa-f6c6-3ea7-bf07-36b66f6a4949 | 1.01395 | -59.52527 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3929557-455c-341e-b770-9a17c952ceff | 3.14334 | -60.69535 | 2025-10-30 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 505e7322-c158-3ee4-b860-73dfad260cd7 | -4.53374 | -54.96682 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32609829-79ff-3a17-a410-a8746eb2bc50 | -1.57994 | -60.37999 | 2025-10-30 05:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a2b5f41-e9b4-364a-938e-4a767be9a9fd | 1.64476 | -55.65703 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44e043ae-842b-37bc-8750-0b1088962d75 | -2.93771 | -58.34821 | 2025-10-30 05:44:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8fa7f2d-4b7a-32f1-9808-a2e67715e3f9 | 1.61305 | -55.69146 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d204bd9-6913-3c99-874b-965b3ca1ce27 | -4.24491 | -55.87852 | 2025-10-30 05:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc5a6053-2a60-3b16-b70e-d4ac4eff5886 | 0.44462 | -60.47751 | 2025-10-30 05:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e3cfde1-9342-397c-b6d0-517d1a52752c | 1.61002 | -55.69081 | 2025-10-30 05:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9d0cfb9-03c0-3081-abf4-2cd9742b48f6 | 0.32488 | -50.92617 | 2025-10-30 05:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 475f7cb5-0875-3bf6-9867-5d09ec1ccaac | 0.83661 | -59.31541 | 2025-10-30 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be823265-4ee8-3170-8afc-5ed093121a11 | -4.26815 | -59.65658 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6be47967-dfc3-3a72-aa6b-c99e1686cf28 | -4.26706 | -59.66385 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17305559-26e4-36d4-bd72-f992537303b6 | -4.27635 | -59.65781 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32e08223-9748-3f32-a475-fd21b12798c4 | -4.2687 | -59.65295 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ccd0e1c-c4c3-3596-906a-a8326dc741a3 | -4.27746 | -59.65054 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26f60f3c-7d42-3f90-b579-d0e89629592a | -4.27336 | -59.64992 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ca09b6c-42f8-384c-8f1b-cf724271c9ab | -4.27116 | -59.66446 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 828ec6e7-d9ef-383b-aa2d-1218fe26a5a6 | -4.26651 | -59.66746 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc6076cf-1d6b-3aaa-9d7d-8bf7e411f3ba | -4.27225 | -59.6572 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a66b7a1-7d24-3321-beb9-83cfe9d2681e | -4.26761 | -59.66021 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ed8c2e4-22fa-37ef-89f1-e3fc3d743fd2 | -4.27391 | -59.64629 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c8181e-4919-364d-a524-2d46b89c9441 | -4.27691 | -59.65418 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c87bdea-27aa-368d-96ff-317a6cacfacd | -4.27281 | -59.65357 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b962a09-df3a-3c77-9fcb-4e8d18a7e1cc | -4.2717 | -59.66084 | 2025-10-30 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd7cf714-8332-3e1a-aa16-e35fc8af48fe | -4.2544 | -43.7149 | 2025-10-30 05:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |


[Clique aqui para ver as próximas entradas](README66.md)
