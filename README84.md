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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a51e1fb-52d3-30ec-a5e5-6f25b5c79fce | -3.52262 | -55.3941 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd1afde0-e1e0-362f-8003-c17bf6ab75dd | -3.51342 | -55.43139 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7c218f5-b150-3e49-aa99-2ef261d206dd | -3.51289 | -55.43483 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83e21a1f-b808-3f43-a017-99b4c747cd33 | -3.20381 | -56.56185 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a1a28a-a301-3e16-872b-1eccad835d39 | -2.34507 | -56.506 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df62b87f-afb7-300e-840d-3f884edb1210 | -2.34443 | -55.66201 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e249ef58-5b23-3d1c-bc74-19267880b5cf | -2.34001 | -56.4941 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b81d4c91-8e3a-32a2-8429-21c56e14c9e6 | -2.3344 | -56.46363 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bda8dca-ec68-3335-9a81-8a6ae033ded7 | -3.74077 | -55.59074 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24899d82-dafc-3181-92e8-1f69908796b5 | -3.72517 | -55.5565 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f785b5d-c254-327e-9741-9e83e04c5b2a | -3.70373 | -55.56375 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0be6f1ba-383b-3aa7-aade-3b41030c0b07 | -3.70043 | -55.56324 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdbd971-5a79-3075-83bb-ce7043ff5c84 | -3.85059 | -55.38584 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 074b59e2-fa15-37d4-a631-8a689cb2170a | -4.85303 | -55.98127 | 2024-11-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d993e19-92ad-3c5c-af28-c138109b69d7 | -4.62304 | -55.84279 | 2024-11-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64880201-7345-3344-83a6-79db0fb14cdc | -4.56815 | -56.19295 | 2024-11-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0916993f-7a8c-3482-a9be-89a024b6800d | -4.3074 | -55.57779 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7967bd81-1161-3de2-ade3-ffc18cccc65c | -4.25665 | -55.50927 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eedc8fb6-8c6a-3ded-af58-df2593c773f3 | -4.21892 | -55.72913 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4423e8d-8092-31ab-a64d-d1780b48d2d9 | -4.19072 | -55.69299 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863cf56e-5a0b-3549-8e2e-9199baa54d27 | -4.18505 | -55.64272 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e77bb2e0-5ebe-31b5-b542-173874e11473 | -4.17993 | -55.58904 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93341e0b-2748-3207-820e-620a6a5dd9f9 | -4.17498 | -55.77182 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1b9c9cf-9202-3ad5-93a8-ac1f6ce09832 | -4.09968 | -55.81671 | 2024-11-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8058aad-0ed6-3a33-8300-4b3610cef36d | -3.99103 | -55.72901 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e795e18-efb1-3dcd-a9ed-a137bdc8651a | -3.94605 | -55.79983 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b789de7-3e5a-3a82-932a-2df47e5bdaf7 | -3.93943 | -55.79881 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b41c2d8e-e7fa-37e2-b78f-f77ac520db00 | -3.93889 | -55.80226 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cef8cb31-9351-384e-bf8d-c18d0cdab6ad | -3.9377 | -55.43814 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16732df-7afe-3be4-a028-5cdf6ecd5012 | -3.91429 | -55.50142 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbbddd52-d055-3f63-a2c5-3edfda57ac03 | -3.91153 | -55.49747 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6aefee9-7abf-3400-b457-abd051d53ef8 | -1.05832 | -57.40422 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c625e46f-d3d6-3e21-a155-31c05838ec41 | -2.58638 | -57.07164 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a068a38-a740-3473-acf0-831f95c400df | -2.58499 | -56.99083 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 237a5d62-2756-3aa4-a424-0daa6e0e4009 | -2.5844 | -56.99456 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3df146d1-531c-3008-9dde-aefa5b634a39 | -2.58381 | -56.9983 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17f97162-15c1-33b9-b2a9-de99c7946106 | -2.58293 | -57.07111 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 298ea396-30cf-3f8c-910e-66dce8db57b2 | -2.58234 | -57.07486 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ae3ff8f-1921-3cc8-8ee7-492502e46d6b | -2.50859 | -57.63615 | 2024-11-02 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91f0a370-3155-3595-905b-e2822e39aef6 | -2.42807 | -57.20634 | 2024-11-02 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93b30212-20d2-3913-99bc-f0a5adadc9ff | -2.83583 | -57.67689 | 2024-11-02 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb79e776-dd5d-3d3f-9972-302d1ab7e36d | -3.68752 | -58.50968 | 2024-11-02 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62f018cc-70aa-36b0-8a17-735ad95deb02 | -3.23152 | -59.87024 | 2024-11-02 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b87edb2-ae74-3c5d-96b6-9bb7a83a32fb | 1.05452 | -59.72897 | 2024-11-02 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25201d2e-bb5c-3a14-961a-51abd57826a5 | 1.05342 | -59.7294 | 2024-11-02 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a2f619-a08b-3e36-b109-c550e9977694 | 1.38398 | -60.80458 | 2024-11-02 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88b8086-b450-3247-99de-8bc03a889e33 | 0.38954 | -62.68292 | 2024-11-02 05:04:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c664625b-7b1e-3a39-8fed-654561c5bf30 | -1.2014 | -53.9184 | 2024-11-02 05:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 9e800602-f836-3bdb-8aa0-fb474eca025e | -2.2663 | -53.7422 | 2024-11-02 05:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fbc0c281-a178-36f3-a167-063394b43f99 | -3.0726 | -45.1405 | 2024-11-02 05:05:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8eed228b-fae9-306c-a9c4-a931db44b748 | -3.1281 | -54.266 | 2024-11-02 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 40efd1d6-8070-3a55-bf37-ed58ced67237 | -3.1282 | -54.2459 | 2024-11-02 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| edd9860c-41cf-3892-b204-bf7758d868c4 | -3.2047 | -53.4179 | 2024-11-02 05:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 867d5b8d-7c6f-3758-8dc8-e5e4e00ac892 | -3.2231 | -53.3972 | 2024-11-02 05:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9a4ecb04-6225-3433-ae62-25890b07fb03 | -3.2415 | -53.4169 | 2024-11-02 05:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 29e6c146-0ed1-3de5-b71a-cb78ba3dc1f6 | -3.2415 | -53.3967 | 2024-11-02 05:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6cadab2e-b3ed-3a93-a7e1-3e9f8784cd7c | -3.2599 | -53.4164 | 2024-11-02 05:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6a9c8706-ab60-33e1-a9f0-cb8ef4b3565b | -3.2599 | -53.3962 | 2024-11-02 05:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 58af83a0-b0d9-3e88-aeaf-e4e51528f600 | -3.7701 | -43.5554 | 2024-11-02 05:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b9595aa8-d3a3-38b8-a77c-f7251c7f75d9 | -3.9473 | -48.3666 | 2024-11-02 05:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e32d7109-f9f7-36ae-9857-4bac3e98bcdd | -3.9474 | -48.3451 | 2024-11-02 05:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 95d4c773-724a-38e0-8e35-c462f1892e91 | -4.3537 | -48.6068 | 2024-11-02 05:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4638a250-f5b3-398a-8594-8c1f7bb3ec02 | -4.5577 | -43.0928 | 2024-11-02 05:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a9f2f444-0690-3b0d-b84c-518ede5f4f56 | -14.03341 | -43.56404 | 2024-11-02 05:06:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9e1594a0-c038-3752-ba14-f7704e19bceb | -13.22927 | -43.9697 | 2024-11-02 05:06:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d08682c-bfab-36c4-86a9-e4db82a786bd | -13.22863 | -43.97615 | 2024-11-02 05:06:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8235d172-9474-3dcf-9d9b-564d60711dca | -13.22831 | -43.97227 | 2024-11-02 05:06:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 25c80813-6c21-3fde-9ec2-24942c9a880b | -7.90927 | -46.69619 | 2024-11-02 05:06:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f39d711b-be74-3ab3-b34a-cb993f48c1a2 | -7.9088 | -46.6997 | 2024-11-02 05:06:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb5e6597-f194-3538-ad21-5c46107f0bc5 | -7.96771 | -47.17703 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4feef15f-7ab0-3fc0-a0db-ad842950167b | -7.96729 | -47.18011 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a276aba2-e935-36e8-9e97-69714fc2be30 | -7.96684 | -47.18339 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ce387d-b73d-3ed5-a2cf-cf2ad1613aef | -7.96203 | -47.17937 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 627c79a5-66cc-3221-ad19-4deb0d8ca9e6 | -7.96159 | -47.18259 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70290ae1-ef38-35f8-a781-78a9a7a1fe35 | -7.96115 | -47.18589 | 2024-11-02 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb491380-019c-3e7b-8bc2-b2c5b0271e45 | -8.84084 | -47.70041 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e629557-c446-3fff-9e59-b4a23a18c3e5 | -8.8357 | -47.69967 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fc519d-4a63-344f-9f4f-96e154106bef | -8.83528 | -47.7028 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e35ca1f-160d-3764-847d-12d59d4cc6ee | -8.82933 | -47.70828 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00bf7ee0-87ba-3a55-8db2-5184cea1c85a | -8.82891 | -47.71142 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 394429f4-2ab2-3ea3-aab9-95b4c91fb96c | -8.68406 | -47.95557 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd1ff447-4a7b-39cd-a9d1-e5df11e41fc3 | -8.68367 | -47.95851 | 2024-11-02 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33062f2b-ed4d-3444-b3ad-8285b99ebfde | -6.22786 | -55.65489 | 2024-11-02 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23d4ee99-5a6d-3561-8561-2215c223eeff | -6.22732 | -55.65834 | 2024-11-02 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95980fad-c888-320a-af17-f04415479eb6 | -6.22456 | -55.65438 | 2024-11-02 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2042198e-9ca1-3738-80a4-46b053b08ef9 | -6.22402 | -55.65783 | 2024-11-02 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 80a55bb9-4404-316a-ba05-f30a879a5dce | -14.03022 | -43.56464 | 2024-11-02 05:08:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| efbeea03-35f9-3862-80a2-8658bfbfdbc9 | -2.2663 | -53.7422 | 2024-11-02 05:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 26f69465-8213-38b4-9bd5-302d0eec1f14 | -3.0726 | -45.1405 | 2024-11-02 05:15:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b5bdfb7c-674d-3ebc-b06e-c6b0c88863d7 | -3.0734 | -54.167 | 2024-11-02 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9bad9515-98c8-3996-9370-4036ce599b00 | -3.1281 | -54.266 | 2024-11-02 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 91b0fa27-b9f7-3dfe-ad27-e7235015020a | -3.2047 | -53.4179 | 2024-11-02 05:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bf3b4719-68c0-380e-93d8-caa3ab7be53a | -3.2231 | -53.3972 | 2024-11-02 05:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d869ecec-d1a5-3829-a749-0975d11adc97 | -3.2415 | -53.4169 | 2024-11-02 05:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 31cfd397-2886-3d12-a8a2-d2ca57194894 | -3.2415 | -53.3967 | 2024-11-02 05:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 69220104-45ca-3a99-82ad-4cbac23e49d4 | -3.2599 | -53.4164 | 2024-11-02 05:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 538d6470-7222-3567-82ad-0bbb15273cea | -3.2599 | -53.3962 | 2024-11-02 05:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| af66354f-d0ae-35ea-a8e2-d9c2e1dc261c | -3.9474 | -48.3451 | 2024-11-02 05:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fe78c482-fb58-30f4-b113-c6b18eda526b | -3.9473 | -48.3666 | 2024-11-02 05:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 6d489808-09d3-3862-a8bf-400dfda9911e | -4.3537 | -48.6068 | 2024-11-02 05:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |


[Clique aqui para ver as próximas entradas](README85.md)
