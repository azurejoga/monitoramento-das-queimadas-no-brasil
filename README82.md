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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f374a4-dff6-3c27-aae3-e345cbdf223b | -16.63255 | -49.7888 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a861af3-e8af-3587-8465-6e289e5550a0 | -15.69052 | -47.02705 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6287bd02-018a-3641-8b4c-8aa5339deca8 | -20.08698 | -44.48093 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb4556d3-649b-323a-8dcd-4a2b60726397 | -12.82418 | -47.96565 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d9082bd0-354e-37ec-8228-f9a2c269ed9b | -14.12478 | -45.37605 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6d2770a-098c-3f89-8d14-b3fe6ede5de0 | -14.15015 | -44.45064 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b280c4c2-31bf-33ef-b3c3-b63f29599f8f | -12.93392 | -48.00117 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7dd9a48-88fe-3598-9fb4-88f49dac7cf7 | -15.09853 | -48.03327 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c3d6613-492a-3a03-9f45-63e0414a62d3 | -15.08531 | -48.00915 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b28faf37-84bd-3eea-a3f4-2313293011a7 | -12.85609 | -47.61254 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f2e639e-c67a-393b-af3e-1ca715e710ab | -15.10183 | -52.44919 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd94a4d6-0375-3647-8677-944d0966e49f | -11.64443 | -52.25238 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92deaee2-ab8d-374d-acca-66bfaae664ed | -13.91386 | -48.26859 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65619338-f622-3710-9a1e-34dea28ea775 | -12.9847 | -48.00229 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1df072a-725f-3590-9578-fbcc2f9a4188 | -19.08837 | -46.70667 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93868bbc-ce19-3261-b01c-45f4b10b8cc3 | -15.64157 | -41.8199 | 2025-09-12 04:27:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d35a510-3ea9-3166-8fbc-18f3c8083cd2 | -17.93998 | -46.92454 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b94fd9-4e06-33b3-895c-fe69f8ae8ba2 | -15.58089 | -54.75758 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56f2abe-4076-3e24-a6bc-0d1f277cd71a | -14.43668 | -52.93724 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05c7a9a0-cc77-35d6-85c9-f62bdd541bda | -17.3376 | -46.67395 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93064a88-2ec4-385a-8fdb-9601f9ad912e | -12.86122 | -52.9523 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d7fe7b-bdf7-3be1-8d8f-ee771127e7b9 | -12.82942 | -52.9648 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d220840-6305-3c58-bcc1-ae2c4354aa3f | -15.08918 | -48.00614 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0df7de36-be55-3789-b79e-c8c3baeb5cd0 | -17.47686 | -43.73507 | 2025-09-12 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17c18d6f-8099-3a91-96da-7a80968f8af3 | -15.07555 | -48.00776 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50d81eb2-9b1d-384f-9a5f-08d1d5f75b5f | -12.39652 | -46.50417 | 2025-09-12 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 111b143e-db44-3e06-8a0d-b39d6d19a6ab | -18.15465 | -48.10494 | 2025-09-12 04:27:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 907bfdf0-20aa-3023-9c23-32ad13107c76 | -12.92744 | -54.7536 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a6d1c103-ae2f-324e-b267-ba5416cf70cc | -19.70823 | -44.23849 | 2025-09-12 04:27:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eba3fd2-7b44-34d3-8ec1-5da1e6bdba79 | -14.13123 | -45.38116 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e82b4def-758c-329e-a7be-1a308f49b58b | -20.03919 | -41.74871 | 2025-09-12 04:27:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8a53d660-4adb-3812-b7e1-c0bbcfb52c08 | -18.05685 | -45.44741 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d88c55f6-4e0f-378a-ae92-d41b30964447 | -13.3608 | -41.92255 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d3644b26-6278-37b3-8fd4-9a70d5a357df | -19.6408 | -41.58825 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc2665f8-d210-3dd7-afe2-221d489f8d64 | -14.42582 | -52.92974 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebc6d224-cb4c-3b8e-9984-7f0d30d5b1ca | -14.26356 | -54.79232 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 059b62ac-d7a3-33b3-98bc-619fa597e881 | -17.13707 | -48.49954 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dbda723-912d-3cec-b3b3-718947a43cb8 | -12.97466 | -54.75639 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd6d27e8-f5a5-3872-b5e8-2e61f7befbc2 | -18.65363 | -47.65154 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ae91b8-388a-37ba-8fee-b0ddffed0581 | -18.65926 | -47.66016 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0634eb1b-b930-3bab-b66c-d6b3119b5eba | -14.51201 | -53.90519 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b455059-e45c-37cf-a187-3999af4f99db | -13.58889 | -47.65924 | 2025-09-12 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0071e48-fcc7-38f1-a051-bdfa955781fa | -13.27872 | -51.7154 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| db8221e0-281a-329d-9cb3-9ed4c772448b | -12.89648 | -47.95951 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8267c4a-3fb1-320f-8635-c81ecf2a3b27 | -13.91735 | -47.94559 | 2025-09-12 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c37ffb2-6ffe-33ff-98dd-c3dd9d69b9fe | -18.67893 | -47.66737 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f3de9a3-4d1b-3a9b-8946-a257d23be9a2 | -11.18483 | -55.06391 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10949968-e7d3-322f-ad4f-4cab056c877c | -12.91664 | -54.76138 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2990241a-a7f6-3d1b-9a08-2b9e0c1eac46 | -18.68174 | -47.67167 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53b59548-9fb1-34fb-b10a-83a5351ca157 | -11.79084 | -50.568 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf8b53b1-45ec-3373-9827-3b89521206ec | -17.93884 | -46.93227 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26efb230-02c0-308b-850d-e15289cc9738 | -15.12278 | -48.61163 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3805547-3d67-3b9a-a066-d4541c3557b4 | -11.19344 | -55.07076 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0820879-4662-3065-beda-20c9701940c2 | -11.97298 | -51.17375 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 998e0387-105c-3b81-8ac5-5ea66b606782 | -18.08551 | -45.42544 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5e957e9-9fb1-3d81-8899-9233a1b2a50c | -16.62465 | -49.79507 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc1576b9-ca8e-3521-86ac-6f4d44865510 | -12.87386 | -47.95221 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e045725-2719-366d-9054-da2be765bd46 | -13.18934 | -51.75763 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afcbe603-a2af-3777-a54a-d9008036e938 | -13.90999 | -48.27156 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c154407e-6b8a-3a78-8a43-3f79ba004eac | -11.86757 | -58.80836 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3dc55dbd-d0f1-3088-ac78-250f9e5bab19 | -18.62378 | -44.26595 | 2025-09-12 04:27:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57ca08d8-4549-31a0-95d7-9d095b0c65b6 | -13.91949 | -48.2331 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0339131-f336-31ce-b1be-20c07ec859e5 | -16.66404 | -47.62636 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb7dbbc8-e61f-3c20-ac05-8c8283b37d86 | -15.6061 | -52.73708 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 986e80a9-0e86-350a-84e4-70efb0d8dd21 | -14.42597 | -46.40811 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8432997-2a42-39c9-836f-a2c0d1695ad4 | -19.19224 | -47.43904 | 2025-09-12 04:27:00 | NOAA-20 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9e20830-e05a-3b86-a0ca-f79178a284fd | -12.8275 | -52.9758 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f10e7d17-e474-3e2a-85c2-c0c4620a7336 | -16.49101 | -51.98948 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eb4c00e-dd11-3169-93e5-6d5903c7c1d2 | -17.95637 | -45.2865 | 2025-09-12 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5185be62-123a-32b7-9a3f-81b3f0cd3da6 | -12.20171 | -53.86131 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032afd27-25e5-351c-b441-32c0b2e6d270 | -18.66263 | -47.66074 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d497348-f326-3f42-aca2-be614f033c35 | -11.97831 | -51.14283 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bf0fd71-1b0e-36e1-a5a3-366f8052257a | -13.00512 | -48.00206 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 656f78ff-3ca8-398e-b6fb-98a1ef7b9437 | -17.83628 | -52.04957 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1fefe07-3852-389a-98fc-9aa2696c52fb | -12.93449 | -47.99762 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1daecc94-78c9-31b1-96fa-a51235b3056e | -15.53419 | -48.54457 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 785e0e62-2f30-3cb2-a006-45f3ff2cb943 | -12.82814 | -52.97212 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9083c823-9d74-3683-880a-38880a5e93e9 | -15.14979 | -52.39643 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cf27f6b-795b-3007-9c2c-0879bce1d064 | -15.10739 | -48.02012 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5fb7802-50cf-30c9-a476-c90b4ec11d07 | -15.83162 | -42.59191 | 2025-09-12 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc472e6e-1c0e-3044-9151-5f8fec5d4db3 | -12.24692 | -47.34037 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0172356-7d90-3355-a7ee-adeb96d0446f | -15.55289 | -47.35583 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37b425ef-c79d-3e61-bd0e-b2d9e8e65c26 | -12.92377 | -54.748 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4c517244-8511-354e-bc3f-0730acdcd476 | -17.35419 | -46.69925 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 494e0343-1038-3b01-ace9-8adbd06d682e | -15.57302 | -54.7518 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| feca583a-4fdc-3141-a866-483de39340c0 | -14.17733 | -46.2013 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fb76791-a60f-3f0d-8c2f-0ac527936c78 | -15.16332 | -52.408 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410df15c-d7f0-3f8b-86c0-656d31ddde7f | -18.34437 | -49.32755 | 2025-09-12 04:27:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18df3a95-c0e5-33c2-a991-be3e6de430bd | -12.8659 | -52.94944 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4f5efce-99e4-37f0-a23f-0e1a7e232b85 | -14.74383 | -46.29419 | 2025-09-12 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffd18e37-165f-376f-8043-4f0eca19c0ed | -18.77302 | -48.54128 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 825287f2-9533-3f5b-a0dd-445569e39a36 | -16.65169 | -47.62538 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0c72327-8f9d-3d22-84cc-2e553cab0f1b | -18.62299 | -48.26124 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f1e7eaae-be61-3d5d-8476-455bbed48249 | -13.16593 | -50.08706 | 2025-09-12 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6673e697-95be-3971-878d-65a25b355215 | -12.81974 | -47.97218 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 954bfb61-8c63-366b-bdbe-bb355a7d3614 | -20.1214 | -42.35063 | 2025-09-12 04:27:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f056f42d-98a9-390d-af86-4508f23336bc | -11.92106 | -50.69091 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8151c147-e532-36bb-9767-7a00027085ef | -14.17619 | -46.20896 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d0d8e223-fb41-34db-a308-f1e366b50ca8 | -17.38345 | -52.93956 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b09846b-7ca3-3c42-b3c8-14f72d90723a | -16.41028 | -45.68512 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README83.md)
