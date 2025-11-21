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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fc76b94-3c99-3225-9549-649f34dabba0 | -15.53483 | -55.76405 | 2025-11-21 05:05:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d3076c7-728d-359b-a8fc-66b33aea4866 | -16.41306 | -54.90106 | 2025-11-21 05:05:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a048c486-1fbc-39da-9e95-f6ab7e275d7a | -12.87135 | -54.74316 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26116128-f748-3ddf-8b64-8e676b355a0d | -16.17657 | -59.08047 | 2025-11-21 05:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| db21e820-c19b-3c1f-a62b-2c7325adf67b | -15.80778 | -58.19421 | 2025-11-21 05:05:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 359f8aac-13c5-3219-b03f-95f236691712 | -16.37667 | -57.42505 | 2025-11-21 05:05:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3cd750dc-6de5-34ef-974a-55ccbdece320 | -15.0182 | -56.10474 | 2025-11-21 05:05:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7e1e957-d4c5-3efb-ba7d-224f1fa00d48 | -17.07445 | -46.59843 | 2025-11-21 05:05:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38969588-7386-3a53-98b3-7d1d9367f55b | -12.86963 | -54.7416 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59188447-d9c1-3756-a1fe-d8642baa5406 | -12.87888 | -54.72695 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9d1fad6-f02c-3b05-9461-6858092ceb6a | -16.44691 | -50.84121 | 2025-11-21 05:05:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39546a6f-9cd2-3ee7-9224-8bae6e845a15 | -12.88826 | -54.76057 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cc6408f-d8a8-3e6f-8345-a8c50b30cae1 | -12.8702 | -54.73767 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 501e416a-d0cb-393f-b607-e3989db5bc29 | -11.83764 | -57.85096 | 2025-11-21 05:05:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d458acfe-9df4-3f55-8693-1929e857bc3f | -15.12225 | -52.90357 | 2025-11-21 05:05:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b032397-13b2-3267-a1f1-c2b2da961b01 | -13.35045 | -54.34134 | 2025-11-21 05:05:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c1d6b9-46f6-3549-ab29-6651b667d9e7 | -15.9388 | -56.29992 | 2025-11-21 05:05:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b73cc68a-5ae6-3c09-8518-885bb5d09d0c | -14.97968 | -52.98201 | 2025-11-21 05:05:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9131fa18-41a2-38a6-ae58-3804be5418a2 | -12.86728 | -54.74654 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f4f146d-3d23-3111-8b57-bf86f4bbc0bb | -14.80109 | -56.66407 | 2025-11-21 05:05:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 414bd21c-0d3a-3c19-96e0-d16a79fd5e30 | -12.8905 | -54.72063 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10aba0f2-5685-39d3-a7f8-9312d021897f | -9.99949 | -65.18657 | 2025-11-21 05:05:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 061c8dba-cb13-3009-82f1-dec0cf9416cb | -11.96088 | -62.84064 | 2025-11-21 05:05:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e305769-b470-325d-8da8-4d34d9b4cbb6 | -12.86849 | -54.74946 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60ed7a03-219c-3ad7-a506-4958e29293de | -16.94037 | -52.6739 | 2025-11-21 05:05:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd5728de-65fa-37bd-9e77-a0b85ea47976 | -15.52739 | -55.76681 | 2025-11-21 05:05:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b71af6-49d7-3030-ab3a-82ac21bce602 | -11.96018 | -62.84461 | 2025-11-21 05:05:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f80ec8-5495-3419-a053-360a2cad1055 | -13.80036 | -53.37047 | 2025-11-21 05:05:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc6007fc-8501-3ec2-b969-ce99757c7618 | -16.17322 | -59.0799 | 2025-11-21 05:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e4687b44-ab4d-3dcb-97a0-a6681b1d81de | -14.41699 | -56.86456 | 2025-11-21 05:05:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4bb0f2d-8dce-326d-9bb5-4ab4e42b8b96 | -13.7891 | -49.57812 | 2025-11-21 05:05:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cce06aca-967e-38c0-b9f6-fdd706669af6 | -12.87194 | -54.73924 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28c805e3-0480-3945-b7f9-626ab6af0514 | -12.79138 | -52.02163 | 2025-11-21 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99e78a29-f023-3a3e-90d4-11a23002ba35 | -15.6526 | -55.96189 | 2025-11-21 05:05:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f274e55e-5a0b-3403-bcbd-e12541577fd0 | -13.49672 | -53.11106 | 2025-11-21 05:05:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf240b79-f6bb-39a2-86a2-b6c3969120ac | -10.84273 | -56.958 | 2025-11-21 05:05:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 423a4121-3c35-3b02-bb3a-d11c4d8ad1c6 | -14.76243 | -60.16948 | 2025-11-21 05:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae6f2f39-f606-374f-ae9d-34344ec859a1 | -16.37335 | -57.42451 | 2025-11-21 05:05:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 32b98605-fa81-30ce-843e-7849908bd022 | -16.20689 | -55.76032 | 2025-11-21 05:05:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2d5f031f-eb51-3b11-851b-c6b86ae2f576 | -9.99439 | -65.18566 | 2025-11-21 05:05:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eb11d1f-3fb2-30fd-b885-6508d70099a7 | -12.79089 | -52.02521 | 2025-11-21 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89306fb-ed7c-3846-a941-e1413b61caf5 | -14.41312 | -56.86759 | 2025-11-21 05:05:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96a6e26a-899a-3c90-b76e-8da1f845feac | -15.50077 | -58.8408 | 2025-11-21 05:05:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c05d37c6-cb15-3382-9bd5-172cd1818f31 | -10.84548 | -56.96204 | 2025-11-21 05:05:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89b52d31-356e-3de6-879d-f8c941a07c90 | -14.4949 | -59.75245 | 2025-11-21 05:05:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 038c3c8f-e79a-314a-bf44-b4b3225ae89b | -12.5494 | -54.80328 | 2025-11-21 05:05:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ab8bd9b-311e-3eca-b463-f8caedac076e | -12.87077 | -54.74709 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ef068b9-2ecc-3779-99e2-82bf271595bd | -12.87774 | -54.73483 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84b92942-7933-36eb-87bf-870fb81bc7b9 | -17.64892 | -43.88973 | 2025-11-21 05:05:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b4a63d3-a9e3-3188-a977-5e379f97ca03 | -12.87717 | -54.73877 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3274fa-dbfa-3033-bebb-6ee61f379be7 | -15.64558 | -57.58075 | 2025-11-21 05:05:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b140dd4a-59d1-3304-b68d-991a23f521fd | -15.29699 | -57.04285 | 2025-11-21 05:05:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 142effac-5707-3ffa-877c-123913d33d38 | -13.73909 | -48.45253 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31bb3f77-97ed-32ed-a0a8-d53ee1b9666b | -11.66995 | -62.6146 | 2025-11-21 05:05:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed83ee2d-0897-30be-a9c1-04334d0ca755 | -13.34717 | -54.23867 | 2025-11-21 05:05:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91b6c143-2938-3207-87b9-1943caccd77b | -13.43108 | -59.91608 | 2025-11-21 05:05:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e10d7d2-471f-37e7-804f-2b59f8d6f658 | -15.50136 | -58.83715 | 2025-11-21 05:05:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e08ea1-068b-36be-8adc-5b1ffe229637 | -15.50333 | -58.84153 | 2025-11-21 05:05:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 060fd64e-080a-3670-b536-1d121277ba2f | -12.87198 | -54.75002 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd0de607-c444-3e8a-866e-44fab4b50878 | -15.42751 | -60.27471 | 2025-11-21 05:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ccc5e2-4d41-3fdb-895e-e95e3c789883 | -15.51982 | -56.71508 | 2025-11-21 05:05:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ecea743-af9f-3e33-9fa1-6614d1bc3f4d | -13.35075 | -54.23922 | 2025-11-21 05:05:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b53e54cb-c3ec-3bf1-ad0e-6581d52355dd | -14.52653 | -59.75392 | 2025-11-21 05:05:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8ac4894-0e83-392f-a6e6-1dd4f60f8c8a | -14.95475 | -56.43472 | 2025-11-21 05:05:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9081e57-1444-3ca4-80a4-0a276295fafd | -14.44985 | -59.97776 | 2025-11-21 05:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9e366c6-b846-3c1a-94a9-0e818ccd40b7 | -11.95666 | -62.8399 | 2025-11-21 05:05:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba334e56-2d80-3f8b-b27a-b5158c486896 | -16.94321 | -52.67694 | 2025-11-21 05:05:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bb3c9ca-7a81-36cc-a5ca-0b5cee9b1e25 | -15.29226 | -53.03721 | 2025-11-21 05:05:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a6f222b-c680-3849-9210-896690227a33 | -12.88701 | -54.7201 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 859ad2f6-c577-3c74-b24a-57bd25d8e9a4 | -9.98871 | -65.1879 | 2025-11-21 05:05:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c84baf8b-ae72-3b4e-af1c-ae2ba22bceb6 | -10.84603 | -56.95853 | 2025-11-21 05:05:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a652ed8-6407-3fdb-a471-d0a2c1b940e5 | -17.58219 | -46.67766 | 2025-11-21 05:05:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2111da2e-ebc2-3fe0-ab0e-69964095564a | -12.88993 | -54.7246 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ebcc372-b2e3-333a-9aee-f3f43710b8b3 | -14.85185 | -53.66923 | 2025-11-21 05:05:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aa0576b-8b4d-3e46-82b7-54d9f0fbf81e | -12.86845 | -54.73869 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c91f62b-92b6-3a67-83c5-37d632aae869 | -14.84809 | -53.6687 | 2025-11-21 05:05:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 437ba28e-df8f-343d-918a-6d12d008ebdf | -15.38298 | -56.33932 | 2025-11-21 05:05:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6cdce2f-e789-3c63-8643-b3485675e7bf | -11.66927 | -62.61848 | 2025-11-21 05:05:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e7b1660-0efd-3314-bc3c-ced65c37e89d | -12.87311 | -54.74215 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb842ee4-3884-391c-9210-e9d27731b53f | -13.78819 | -49.57964 | 2025-11-21 05:05:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bb6006b-2b9e-3eac-b828-e50efebbf17c | -12.87255 | -54.74608 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf5609cf-0154-37f4-ab0f-5f275d449767 | -16.63741 | -51.30484 | 2025-11-21 05:05:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef32c606-3a05-3071-b909-c6aeb1da16c3 | -12.87546 | -54.75056 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9531a43e-1f5d-36ae-bc6d-aff68e915dd8 | -17.64953 | -43.88256 | 2025-11-21 05:05:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33bb07ac-8ba3-3fac-a650-3529b05600a1 | -12.53928 | -62.02263 | 2025-11-21 05:05:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 201775a8-ca9f-3748-bc0a-52664ae0b94e | -17.64451 | -43.88254 | 2025-11-21 05:05:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 029db145-a6da-3f74-9049-4f3b96ae54cd | -17.58783 | -46.68326 | 2025-11-21 05:05:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f5f0dcd-c50b-335d-9803-1e163bb23649 | -14.77796 | -53.17046 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18fa85c8-ea59-330b-acda-3e087df039fa | -13.73767 | -48.46448 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8979db5-6183-3e1e-8fee-e2c691db02e0 | -16.18328 | -55.94749 | 2025-11-21 05:05:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d85bc786-6e7d-34d5-b363-1bdcb444315f | -12.89232 | -54.7572 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdb99ed8-2f72-3919-8e4d-38cedf86a7fa | -12.54593 | -54.80275 | 2025-11-21 05:05:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ad81165-261f-3566-9c13-7f5d3c1ec137 | -12.55634 | -54.80433 | 2025-11-21 05:05:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 262bd6bf-8938-3aab-b8a8-28a0fb6e625f | -12.87425 | -54.73429 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72fb4560-fc4e-32e0-8cd1-729f446e79b0 | -16.33275 | -56.61713 | 2025-11-21 05:05:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 37e1f2ea-2a9a-3d4d-8d00-f2464383872c | -13.80625 | -50.6424 | 2025-11-21 05:05:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c592d037-9358-3672-94b2-2b77b11a37a1 | -12.79542 | -52.02221 | 2025-11-21 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 393b49ab-2368-3c67-b5e3-c4f180f1af4e | -12.86906 | -54.74553 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ead1627-1a77-30e4-a8ff-fe42e45fb95b | -11.83707 | -57.85453 | 2025-11-21 05:05:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8355fe70-3070-3c4c-9964-a734f87b1260 | -14.56033 | -52.79876 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
