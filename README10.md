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
| 75204e07-d935-38e0-89bd-2124f98c22cb | -8.97656 | -47.97645 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88e9c5ac-ccb0-3e66-913f-10a33d9d3011 | -7.72079 | -44.16344 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25076e56-9586-365a-b360-12ffb674b411 | -10.77146 | -54.11071 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de408c8a-4954-3130-a212-74c571e2fd97 | -11.81088 | -52.52374 | 2026-06-18 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 668dd54c-20d2-3ae8-8db7-704f79ce9f78 | -10.55715 | -46.22936 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71951a93-124f-3be9-b9de-c71127950373 | -10.98889 | -47.74685 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c5b736f-2111-38fd-bb44-989bd1e8b7ef | -10.64118 | -51.80051 | 2026-06-18 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f48c66-4a81-3308-8fb9-bcfb8b501a80 | -8.98022 | -47.97702 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38beae96-179a-36e0-89dd-50637b4282e1 | -8.61607 | -45.99593 | 2026-06-18 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8e681f4-fe28-3c80-a894-3a55d2ebc108 | -8.61384 | -45.98928 | 2026-06-18 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5594e66e-d4e2-3080-bd5f-65ef9d135652 | -12.44638 | -44.75191 | 2026-06-18 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e95fb4b-ed7c-3bf2-ad59-547ad308a07d | -12.05521 | -49.76444 | 2026-06-18 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3eae3fe7-81d5-3a58-82e5-f8c519517938 | -7.83853 | -55.40288 | 2026-06-18 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8dcbd80-071e-3b46-812f-ee49fdbd1603 | -7.72014 | -44.16822 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0931707a-c40e-3384-a47b-f2c511ac411f | -5.80611 | -45.06921 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a443b8c8-55af-3f92-9f1f-dc43344a68f0 | -10.91442 | -56.85744 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 327d91b9-89ef-388d-a348-08ee0682762f | -6.97885 | -42.8827 | 2026-06-18 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e083b4c-52d7-3ce4-a869-8ae05ca20a46 | -15.65101 | -58.01789 | 2026-06-18 04:49:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb9655e4-5095-32e6-82fa-78d498cfd76b | -16.45473 | -53.65489 | 2026-06-18 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b64f77fd-b387-3c51-961a-5f34c8270588 | -9.94264 | -65.01681 | 2026-06-18 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f85643d5-fdc7-3132-a3a3-ff3a88132940 | -17.94849 | -44.41169 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea4ccdf9-47eb-306d-9b72-bdbd3efc0826 | -13.20648 | -50.34 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ce1daf1-39d4-37a4-91df-0ac01278d1a8 | -17.94757 | -44.41412 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 286b612c-2c00-3878-ae4c-bcaf1a17bdc3 | -13.20249 | -50.34327 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e21af7b-6f82-30e0-b230-d6a19cf0a87d | -12.20718 | -52.77295 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09245582-125a-3fe8-ae1f-01fcab6b402a | -14.09557 | -59.46031 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f65cebd-c353-3143-b890-0ffafe328e48 | -16.17316 | -51.95292 | 2026-06-18 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999694e5-2c48-3a4b-b981-df787377009b | -12.20551 | -52.78352 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f35f9bbc-5c2f-3018-9082-a2703ed14ce1 | -13.19906 | -50.34273 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bc63d9b-7db1-3d38-902b-5e488c00bd01 | -12.20993 | -52.77702 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceaad3fc-3749-3cf5-ae86-06b5938c67be | -13.20592 | -50.34381 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ade378a6-abba-3f7c-b407-5e8a43fa2be0 | -16.02856 | -43.42125 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c8046c6c-9178-3dee-a764-a79f4ff8dd2f | -14.08939 | -59.4686 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7390f006-1c64-3795-bf5e-947e5446006b | -16.02456 | -43.4243 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79525711-4d20-39b5-a8c0-77ca71fd03db | -17.31613 | -43.64694 | 2026-06-18 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b86ebf22-3eab-3444-b414-20ce408edbdf | -16.17991 | -59.3348 | 2026-06-18 04:49:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a95605bc-a746-3f77-b324-9ab072ab641f | -14.09113 | -59.45939 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd081d27-30de-3d37-8158-3cfd21c224ab | -13.65331 | -60.62123 | 2026-06-18 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa64918-e1d9-3009-b400-5a4105a235cb | -13.65239 | -60.61679 | 2026-06-18 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dcff3f5-d9d1-3424-804e-79e96dd1a4ac | -14.09026 | -59.464 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3745f7ca-4a22-3802-8b03-012ed35377ca | -13.20305 | -50.33945 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c3e895e-6d29-35a3-b1f1-45e7f82f8bd8 | -11.66875 | -56.76311 | 2026-06-18 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a94632-90f0-354c-940d-36d4803c65d4 | -16.03037 | -43.42147 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ba58e59-4a69-3935-a113-b6fe75a5e670 | -14.09199 | -59.45478 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1637268-421c-323a-a5eb-b29f5465c451 | -16.48059 | -50.91164 | 2026-06-18 04:49:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efad8472-51f1-3070-8569-bc80cd86dfe9 | -12.21324 | -52.77755 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ba0c1f-70fd-378e-a7c9-36770f3dbc06 | -14.0947 | -59.46492 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e745c39c-0e5f-364c-b6ec-33ddf78d01ff | -17.32195 | -43.64407 | 2026-06-18 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fffc0933-750a-3a1d-8ff9-d590eab81f71 | -14.20438 | -42.75499 | 2026-06-18 04:49:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37eb0ae7-73f0-3920-a8c0-380ceef726bd | -15.64707 | -58.0171 | 2026-06-18 04:49:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f45aac6-4f5c-38f1-ad93-be2a348a4e92 | -12.24855 | -56.17284 | 2026-06-18 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcf79516-2a08-3857-ad1f-1832a2b1bdb8 | -13.1985 | -50.34655 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63a33394-5d90-37ba-bf29-4ddef95f6ffa | -11.79625 | -57.35408 | 2026-06-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43c5456b-5ffd-3009-a32b-2bc287477721 | -16.17705 | -51.94979 | 2026-06-18 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e846e246-fd2d-3fcf-ba41-abea41075e49 | -13.65132 | -60.62231 | 2026-06-18 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 689031b0-43e5-3b19-8d41-ba3283e99878 | -11.51805 | -56.12109 | 2026-06-18 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16136fda-d737-3e8e-8af4-ca19f7a9a9e5 | -16.02816 | -43.42478 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 48dac5b2-5929-3d96-b0ab-a90a0fd13006 | -15.64772 | -58.01994 | 2026-06-18 04:49:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 011a702d-802f-3d35-b617-8012dca0e8c0 | -14.06102 | -44.47837 | 2026-06-18 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e93397-724f-3084-a45f-70e12b5b2bbc | -14.2943 | -57.54176 | 2026-06-18 04:49:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af55eb3d-a681-3b0d-af13-26b3818291df | -15.72528 | -49.12214 | 2026-06-18 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05413d45-327b-3a95-8010-4e2d1ab65209 | -16.79311 | -49.30795 | 2026-06-18 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2f7d2dd-81a2-3879-93e5-8cb396ea34f3 | -17.79628 | -44.57725 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d7d6267-893d-3aa4-85af-e07ccdd67c59 | -12.21655 | -52.77809 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9aa7731-0d46-30bf-b0d2-efd74eeaece1 | -11.51273 | -56.12974 | 2026-06-18 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71b0f62c-4913-3c91-9fe9-890f808f1013 | -13.4183 | -47.99655 | 2026-06-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e4bf9b2-a857-360e-bbd1-adb704306ac9 | -12.21268 | -52.78107 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c7057d-9418-3764-948b-ec5afef4e920 | -14.90221 | -47.75772 | 2026-06-18 04:49:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2e81c09-198f-3de5-a088-f32ecbfbbef2 | -17.31651 | -43.64323 | 2026-06-18 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b067402-5154-38bd-9eff-3fca11aef7cd | -12.21599 | -52.78161 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5f2654-7eb5-3598-988f-bfb4339e2f1e | -13.19522 | -50.34629 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5934807-63cb-31d9-92d3-5b85fed6a542 | -13.19507 | -50.34601 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49885280-08ad-39dc-a2a3-7a1bf1aa4c4f | -12.20937 | -52.78054 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60fb0352-6e39-3d7b-bb65-58748871d61f | -12.20662 | -52.77648 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8743281b-bdcb-3e06-bd05-0b0e52f75def | -16.03 | -43.42502 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acbadd5e-a6d3-341b-86b7-5675c89cd6f0 | -17.94816 | -44.41488 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39dfa0a4-e1b9-37d6-a72d-48f00e05f07c | -14.08873 | -59.45631 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7b401e5-517f-39e7-8f86-8f01f5123a15 | -13.19579 | -50.34247 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d26b36f0-d890-3b54-888f-ff55e8ef8c01 | -12.20882 | -52.78406 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d334b3d-869b-3e19-aec5-1ef670d48df0 | -15.64862 | -58.01483 | 2026-06-18 04:49:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed1f36cb-63c2-3d90-8da7-d4feb337c534 | -16.23388 | -40.13491 | 2026-06-18 04:49:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e464bae1-e4fe-3b7a-811d-dec79baff5cb | -17.79593 | -44.58041 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b977727-aa6a-3551-be1a-f67d364b41f4 | -12.51639 | -54.38484 | 2026-06-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17781b4c-5229-3715-b9d0-af966b6c40d8 | -13.19563 | -50.34219 | 2026-06-18 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7648570-9419-3d1f-a8d0-fed13ad52ead | -12.20607 | -52.78 | 2026-06-18 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1801db32-2a75-31d5-812e-aad2f8e3daa1 | -17.94883 | -44.40849 | 2026-06-18 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b5b1faf-bdfe-3908-ad81-f7ac0ea8a17f | -16.02494 | -43.42073 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 11b61c4a-0cad-3b4e-892d-4e81aa2ee217 | -16.02273 | -43.42407 | 2026-06-18 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43d35581-d2dd-37e4-b3af-42a209537223 | -11.51345 | -56.12769 | 2026-06-18 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad5d8b1-5aff-35d4-b4e8-f49806815a3c | -14.09383 | -59.46953 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca89732f-8338-365e-b5d1-edacbc0ddbb5 | -14.09915 | -59.46579 | 2026-06-18 04:49:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58eda7e9-2697-3fa2-b07d-dbfc37a4d2b6 | -17.32154 | -43.64789 | 2026-06-18 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4581c18-f7b4-39f4-9c20-c00bd866236a | -12.8354 | -44.3657 | 2026-06-18 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0b6db61d-2d67-3b16-b1d9-5366e5666a1d | -18.82867 | -51.47417 | 2026-06-18 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eaec57b3-a6cc-3ecb-bce5-33e220238cee | -18.82289 | -51.46514 | 2026-06-18 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21999868-a6e3-3546-a557-0c9d71e096f9 | -18.82578 | -51.46965 | 2026-06-18 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4704c57-85d6-3770-83a8-ecc7b1ce1d40 | -21.58314 | -53.8105 | 2026-06-18 04:51:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bcbee67-c70b-3102-94e1-c2d2baacbed9 | -18.98717 | -52.45762 | 2026-06-18 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c341e42f-c1ec-30d7-b789-67c3a28a3a15 | -18.98997 | -52.46194 | 2026-06-18 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc76bb6-6c8b-398c-9980-e9ac4aba66b4 | -18.98662 | -52.46139 | 2026-06-18 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
