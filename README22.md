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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 439bfe93-9adc-319b-852e-b654094cd75a | -12.78026 | -48.06684 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ea7e9f-682d-3483-8a05-2ab85b425969 | -12.96331 | -47.98263 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab328bcd-ff48-3fb3-a1c8-43be2c421e40 | -14.50544 | -47.32394 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb400876-4c14-3b20-ba65-12f1fe2a4d84 | -12.54083 | -45.86692 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48a0acab-114f-395d-925c-b778aac587ee | -13.57683 | -41.08472 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56c9649d-7635-35c3-bd2c-7e817d049189 | -12.9708 | -47.96598 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a3b9025-5d75-380e-bee8-c519841b2f07 | -12.79898 | -47.24968 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| beaac4d2-f767-3ace-be41-68808ccf56c7 | -20.17987 | -44.89341 | 2025-09-16 04:04:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 676f9cdf-ab40-32e4-a7c4-5dbd4aa999e5 | -15.41852 | -47.33315 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3f497eb-5bb5-3e21-964b-088631ab34e8 | -12.66339 | -47.93866 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e44439e1-5d4a-384d-98bb-04093c33c427 | -12.63203 | -45.76616 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce0851e8-0de5-30e4-8c2b-f34f1bae25a7 | -12.66801 | -48.01151 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8783c9ca-2048-3d5d-91a3-926a5f6d5d5a | -12.4458 | -49.70771 | 2025-09-16 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4fc7ad5d-ed5a-3cc6-847e-80a1e03566c9 | -15.69037 | -47.03832 | 2025-09-16 04:04:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ee5d93f-1093-3e76-ad0a-01b133e74823 | -12.8157 | -47.22866 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c72c123e-8be9-3cb5-ab11-f56c34b8f1af | -18.55425 | -49.26624 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0a4adbf3-90eb-3bf6-9c98-baa690979600 | -12.67133 | -47.94458 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f92f230-b9dd-3990-9dc3-9797c966af79 | -17.86642 | -44.44788 | 2025-09-16 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f124f99-c475-37ba-b18c-063a7edf484a | -12.84677 | -47.12767 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 480a12c3-f0e7-3e69-8ea0-f79911d5e4b4 | -15.06572 | -43.33648 | 2025-09-16 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e5d6b20-f9b0-3334-92db-8741120a4f2c | -12.84262 | -47.12699 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe707b0-2dff-3a62-bb4d-1fd1b2c3a28d | -16.81358 | -47.78151 | 2025-09-16 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef44ef23-983e-35f4-952a-c4260239d464 | -13.21794 | -47.29665 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efef5a11-c48a-3383-8234-793a684da39e | -12.62128 | -45.74208 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d8f140c0-39af-3b39-9ee5-d1183698e600 | -12.76244 | -47.96508 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 869fcef0-3777-3a6f-b132-9c3babf0998b | -15.88262 | -42.72098 | 2025-09-16 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d18819f9-21e3-33f7-9acf-9c1490b19208 | -14.51194 | -47.37927 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4055c624-372b-3461-be65-d7cd4a8c0412 | -14.54139 | -47.35645 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8b221216-606c-31a5-9f6e-3361ef1f06d9 | -14.50769 | -53.28263 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c2497e-fe54-32ed-a364-5a27e239fffe | -15.77448 | -53.4487 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9d20475-22c6-3e79-a548-2e62384cfe87 | -14.51707 | -47.32945 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d47d653c-707d-3a27-96b4-772d01eeb7a1 | -14.6036 | -46.3825 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f5b951a-d664-35d7-82d0-8e83a12fe998 | -14.63271 | -46.39701 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e14f7acf-5809-3c48-bbcb-593f0e38a779 | -16.69233 | -49.78231 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a4d3cb0-0a08-3f9e-86b6-3ebe70ab2ea5 | -14.84741 | -45.50884 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c509c604-0cbb-3a4a-be6e-c327028f7651 | -12.69831 | -47.73853 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eedbdd9-3172-3b3e-8480-8c0b504f3f2f | -17.56148 | -43.79864 | 2025-09-16 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42a73ffa-3974-3666-aa3a-34392924cd37 | -14.53089 | -47.39097 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 056ff805-2b1c-3a97-8da8-5b510b5af08e | -12.66496 | -47.92626 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ed007142-5a65-3a12-bca0-faff168eb9e4 | -19.38755 | -44.3 | 2025-09-16 04:04:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9437bfff-e693-3f44-be3c-56ace0913148 | -12.54467 | -45.86758 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3edf60d-39cd-35a2-8f8c-3be8ecff0a54 | -14.52202 | -47.39328 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84421217-26a9-36c7-9eb6-bfc774eeb37b | -14.81122 | -51.66406 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6258b515-a48a-33f4-965a-87af4d39ff3b | -14.91178 | -51.64919 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ece95f0-65a0-3c5f-af8f-54df58d7ccba | -12.66254 | -47.71465 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 484431f6-156a-3100-889e-f55574adc433 | -18.3998 | -49.33698 | 2025-09-16 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d39fb82-3f5a-3709-80ca-79243fb4b356 | -18.58103 | -48.1499 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15dc170a-4f67-3f5e-8bff-8a9d1add8075 | -16.66434 | -49.7569 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09fbf563-b4c4-36d5-a248-73427d7f0727 | -12.80663 | -47.18405 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa4685c5-d94c-3c5e-8e1c-4b973c54f294 | -12.62611 | -45.75521 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fd42ae0-f124-3d0f-a0ea-0bc16622483b | -12.78924 | -47.25589 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32cde6ac-ec99-3dec-8008-a19c2d29e2f6 | -14.5139 | -47.39153 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45d6eb3c-d90c-39a6-8f37-7d6889d4a1ff | -14.80658 | -51.65941 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de38bd75-1c0b-3d24-ba5a-d8b62bf2c85f | -12.67008 | -47.92284 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8246c2d2-9168-3a1b-8980-3597ccf62640 | -13.21263 | -47.29181 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 946ba80e-8f9a-3a14-b5f8-c355f7671c37 | -12.68606 | -47.98736 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9539939c-402e-3940-9d10-86b8a4f15cc9 | -19.38816 | -44.29624 | 2025-09-16 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9033957-df60-3f4b-88fb-1cb1c844b9ed | -17.60988 | -46.68639 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5833f9b5-c1c2-399d-8d52-007a28335198 | -12.63035 | -45.77574 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d81dd5d-a42b-3596-afae-a352c31630a5 | -13.74675 | -48.77678 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0545c582-f8d8-30e4-b2a8-57f8acd346d8 | -16.69784 | -49.77851 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eebe14f-e9c1-32e8-ada0-4a0b43468976 | -18.55591 | -49.25766 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 4e2c34fd-83dd-3d2a-a922-05bee9695bf3 | -12.92602 | -47.96475 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d81652db-b348-39c6-9c5f-9538e1cb91ab | -14.60745 | -46.38312 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56ff83e2-4626-3461-91b7-e1476f561a98 | -16.68639 | -49.76597 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3ffe9f3-d6f7-38be-b60a-3674e363925f | -12.69044 | -47.98819 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 85cc431d-b026-34e4-a0bc-4bb7a237906f | -13.78372 | -54.95354 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| af543591-1cef-356b-be7d-ef6c54d5d3ec | -12.79755 | -47.2492 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 571e83b1-b5c5-34ae-997a-ac337bc9cdf2 | -18.78013 | -47.63725 | 2025-09-16 04:04:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4d4e54f-f1de-3f80-9e28-c3665161c638 | -13.27896 | -54.24159 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 471fc31e-4614-32d0-9ebe-42e91fb0a3c4 | -12.2968 | -46.40608 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56ab0372-fcb0-3f08-bc50-7c4a6d9d65ac | -14.54715 | -47.37112 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b06a9b7-c4ca-3453-8ff7-e210b2ebf433 | -14.52453 | -47.33479 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e69d13a4-837a-3db5-852f-098ab476a2ba | -16.69338 | -49.77697 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d8179ba-9223-3af4-8849-4ecab5018db7 | -12.62738 | -45.77028 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ffa5b31-0059-34eb-b2d4-95e373b75f3d | -15.47388 | -43.21065 | 2025-09-16 04:04:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd1c27eb-4bda-31b7-945c-55cc98a6b994 | -12.78325 | -47.9281 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f9c8dc42-d7f6-3fc7-8e46-a517ad7dff93 | -12.65468 | -47.93332 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 115107da-7612-3d71-ab43-b8dbdc139e59 | -12.63151 | -47.52076 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74f57ca1-2ca1-3275-96f1-4a7bcf4a3b2b | -14.52361 | -47.33859 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c272a13-3289-3c19-aafc-d5e5e70a1ad2 | -16.17369 | -47.92823 | 2025-09-16 04:04:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55a0cb9a-5fdd-3e25-8a15-117f9364a348 | -14.51459 | -47.38777 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02f113ae-1d1c-3728-93f7-7bc1a395b0a9 | -13.22786 | -43.41855 | 2025-09-16 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b100b8cc-154d-3f55-a8c8-eb2517e6d861 | -15.78224 | -53.44109 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06567061-6df5-3423-bdce-0a310c81e11d | -12.80593 | -47.1879 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 724b7426-665a-32a7-99cc-1e1911ba9149 | -16.52798 | -43.72689 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a1aa1d-0caf-30ff-8dbe-f808080e6bea | -12.67884 | -47.97737 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d1fb801-d10d-30b0-b3cd-2732537ab4b1 | -19.84298 | -46.45452 | 2025-09-16 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5f926d8-1bb9-3a3f-861f-31b6c8733527 | -12.67758 | -48.00881 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93a6539d-1847-382e-ac65-480b8310f7cf | -15.83048 | -53.47486 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e5ca2ebe-10dc-37b0-b334-6adc4508e558 | -13.20441 | -41.98957 | 2025-09-16 04:04:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3159e90-bb32-3889-a110-8e65e8e14ca1 | -12.66343 | -47.93486 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd927c05-eb91-3d59-8535-b909535eb81f | -12.67571 | -47.94536 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e2dc052-fc4b-36e6-a2f6-a5ed14f18d81 | -14.45788 | -47.28466 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 547cba4c-e1d5-39db-9ca9-3b200cf81e17 | -12.76318 | -47.96094 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e152ed1b-2376-3b88-bf6a-dd7b53383a86 | -12.74042 | -47.2078 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ab7cb91-a071-3c21-887b-2e98c4561049 | -14.52302 | -47.34179 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b965dbe0-9949-3794-ac31-052cf9f5e98b | -15.0901 | -52.48079 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fdab8ed5-a26f-303e-864d-2bd6bb6d4a04 | -14.83731 | -51.67317 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 083c14ad-a89f-3fdb-9537-1941882b2157 | -12.95256 | -47.96735 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README23.md)
