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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796ba470-1d10-300b-861f-67c8b71fafb6 | -3.30711 | -42.27935 | 2026-10-07 04:19:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24550b1a-d03a-3adb-adb4-3a868d4decea | -3.50138 | -54.66506 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 000a165a-a198-3a37-ac66-58b9ff57d8a7 | -3.05751 | -54.20966 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed5e1f07-eb92-3694-9009-b7faa74beb8f | -3.52685 | -52.7534 | 2026-10-07 04:19:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf818e77-f0a8-3ff4-a9b5-261e7d70be56 | -3.5026 | -51.69181 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9541fd4-818f-3ef7-a55a-3cf53b021b24 | -6.71887 | -45.26316 | 2026-10-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eddf50f7-45f5-3382-902d-1781e9084abd | -5.68874 | -40.89034 | 2026-10-07 04:19:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b8d41a9-da01-3ff2-bb56-a2cbb445eb83 | -8.3379 | -44.73969 | 2026-10-07 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd4d76e-544b-3d52-9509-89f8a997a8dd | -3.53242 | -54.63766 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61778ddb-84a8-3fad-8339-aab3ec889367 | -3.05417 | -54.22962 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e858d0-d919-34e5-bdc0-38bdf2eddb37 | -5.1079 | -45.88417 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b751749e-6169-37b1-93e6-0bd1dfc63df5 | -3.51983 | -54.67309 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec745e1d-fe3b-3182-a3c6-433e49e6845b | -7.29633 | -47.26439 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e307c1-76ce-3ebc-9ddb-4079329fd22c | -3.84339 | -50.99176 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efd8d82b-85b1-3875-aebd-ba7a529c7148 | -4.99415 | -56.05107 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 529e06c3-ca5a-3616-a1b1-f97eca38ec60 | -3.2869 | -54.03237 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a1994437-ac34-3d80-9cc0-bb3c7cde86a5 | -6.12121 | -53.05751 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4893eb12-0261-351a-8f3d-e577efbe7536 | -3.02011 | -53.90899 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 06316e59-20b8-3510-b096-81fb624defe7 | -3.03559 | -53.92325 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5cfacb9-a0bc-32e0-a182-2363071a858b | -7.40764 | -44.45916 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9459a3e-2a20-3753-a22e-03dcf7faf3d7 | -4.14983 | -55.15857 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6db62a28-b52c-315e-81ef-f8a77eeebefc | -4.79076 | -45.80659 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deecc806-46bf-3bd7-8241-9fc6bac76de0 | -3.13408 | -51.02977 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4ce4344-627e-33e6-9902-2c1e564540ea | -5.75968 | -42.03887 | 2026-10-07 04:19:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22f41beb-277e-3a12-ad64-165eb585ac38 | -4.99528 | -56.04467 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 887bbebc-6bcb-3f6d-997e-d699eff02d5a | -5.0146 | -49.94291 | 2026-10-07 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46c59358-58ba-34e8-b5b4-f64389fd8815 | -3.28971 | -54.05265 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a2bb55e2-1e7a-35bf-b19a-c572952d968b | -3.04212 | -53.88525 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f9462d5-962c-3b02-8935-45d469b9a7e3 | -3.2916 | -54.07824 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec6e5336-39db-3a31-bb30-3f42098a3eb6 | -3.29879 | -51.1142 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 730942c8-aa37-3251-b5d6-a5b0f0b215c6 | -5.97196 | -40.92068 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27fdd4d7-2901-3f43-a885-366d7c19fa41 | -3.13395 | -54.36633 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 066cea78-f721-3dfe-84e6-d6b3999a3467 | -3.03271 | -53.90308 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17bef95f-d354-3d54-9354-a2b517a151af | -6.40731 | -52.72047 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68eac2f-f94b-39b2-8a4b-af0ee461e3fc | -3.18269 | -50.55138 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0544bec2-fa40-31c4-8ec2-0d66dd46056d | -2.99078 | -51.05432 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a370d809-7965-3753-928c-b8b0666cdee2 | -6.23009 | -41.98506 | 2026-10-07 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 97a05dc3-2980-3c07-bde8-0985887a9a0b | -2.94076 | -54.17412 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29e32e8a-76ba-316c-af41-583b4ada6bb8 | -7.16822 | -43.76862 | 2026-10-07 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35f0c6d3-6b3e-3c47-9614-d56ebae07344 | -5.23582 | -50.91408 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48ea33a0-1ac9-3e69-bc2e-be73a2edc7ee | -4.28614 | -43.6445 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32a2eb27-31da-34d1-81f2-0844db64ebb5 | -8.03767 | -47.81592 | 2026-10-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8763e36-d4eb-3402-b891-2e700716030d | -2.77589 | -54.11491 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c72ce49-6901-32f0-906f-f1ec32122a9e | -4.35541 | -47.7784 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3fc7d54-b72d-3bba-88ae-f9ea4efd9e3c | -3.03395 | -53.93282 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 441858ce-5066-3434-8408-16fe74d5693e | -7.25273 | -48.06937 | 2026-10-07 04:19:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6602d2c-c5df-3ae8-95ac-efda049030ad | -2.76335 | -54.11272 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2a6d0a7e-1f27-3389-8be3-eaaf13489032 | -3.07762 | -54.24426 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26dd5377-3323-3ca7-aa5d-6b90748c92d5 | -1.56381 | -47.74086 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105ce0f5-5c8a-32df-947d-37f47bf4293a | -6.9871 | -43.21845 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 968d8305-7dc9-36c2-a62e-e0ab8332f2eb | -5.67811 | -53.50308 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f8e788d-bd72-3ce4-920c-ed3a2b4455d1 | -3.06252 | -54.17973 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37caf799-4a31-3796-bbeb-a573eebf8c13 | -3.21861 | -48.81631 | 2026-10-07 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa332a41-b1cd-3040-89f2-6ba68e0dcc46 | -7.24896 | -45.26084 | 2026-10-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44ea2d54-243b-360f-988a-de26010ddcd9 | -5.97018 | -40.93217 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cb04a5c4-4275-3266-b927-c1fea7341956 | -4.45366 | -47.92149 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 247c96e2-2ac5-3078-a0ed-73a2f61b267a | -3.60361 | -50.98002 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d968e35-4c80-32ae-b2ea-3679b8854cb3 | -4.25142 | -46.37677 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 945da3fb-5b0f-3d1b-9b73-04ac04585ec5 | -3.18175 | -50.55695 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cc1498a3-400f-3260-981a-d5c895e0ac01 | -3.48202 | -55.44098 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e37b76a-5b16-3ea0-88e0-695bc2fd87cd | -4.18825 | -51.14155 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b37e4e4-79c2-3965-a287-91b3fdae407e | -7.87806 | -44.19678 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d9eee2c-2800-3c0e-8cea-ad3f73a4e39b | -5.30821 | -46.68683 | 2026-10-07 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a0bf0fd-da76-3e68-85bc-09f5baff37c6 | -6.71545 | -45.26257 | 2026-10-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b427ac0c-7961-3247-be1c-686e8624c5ab | -3.27924 | -54.04745 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b03570f6-4f54-3ffa-9814-541d309c00cc | -2.25845 | -47.00571 | 2026-10-07 04:19:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| faf1360c-5825-3988-996a-1c9b5ad725e9 | -3.52249 | -54.65739 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 988af40a-427c-347c-946f-88a5d1b185d0 | -7.19329 | -44.29473 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b32e70e2-cd4d-3216-8c6f-f8a7c53b623f | -4.51466 | -42.89311 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2d7857c2-a444-3d0e-b5c7-6b5b7fe4dc36 | -5.74442 | -43.27945 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0c2f9201-f79e-3151-869d-1711e85baad1 | -4.14602 | -46.83957 | 2026-10-07 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93b71c9e-1628-38dc-950f-98df89c6ed92 | -4.3148 | -42.99586 | 2026-10-07 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee1bdfae-e26c-3ad3-b66a-d2a2a10aae47 | -6.28031 | -46.4293 | 2026-10-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7f7bade-68f9-30d4-95e4-17a40c1d27bc | -6.28144 | -45.84421 | 2026-10-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d83a3c90-dafd-360c-bde2-3d542ee378f0 | -5.73036 | -41.72871 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 92a9c728-a8b4-399f-b3e3-0f515b23fa20 | -3.81018 | -47.4949 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3be153f-5943-3f86-a4e0-0979c8f152c2 | -3.84884 | -55.98813 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 626ce753-7097-3d0a-97e5-f12eed982675 | -3.06959 | -54.2536 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e71e4977-a7f1-3845-b193-10a4a78c2439 | -2.76508 | -54.10275 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 78414362-d071-3694-8495-f2ab58ab2c56 | -7.60247 | -42.37199 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 699b37b3-88b9-3f0a-842b-6d94d4a412bd | -8.64045 | -44.86477 | 2026-10-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c029ccba-35bb-34cc-9f18-306da6928c2e | -7.18026 | -52.61669 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059611c2-5ca7-3cdd-aa65-92a4be919f78 | -3.94202 | -51.01539 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36954772-ff18-3fc3-bc3c-5dbcd594f568 | -3.18082 | -50.56252 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 394500be-7866-3db0-a2ab-f7e56ac3bc97 | -3.29419 | -54.06351 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 29663e54-3c3f-3b60-8684-f279d66764a1 | -2.75124 | -49.53358 | 2026-10-07 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82497119-ddef-3810-abc7-9f8bb29a160d | -3.03805 | -53.90896 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 550ea99f-f318-35f9-ba9c-8150f787466f | -3.26519 | -50.41826 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c21fad3e-770e-3290-836f-49f4c565523d | -3.98522 | -56.22182 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31499774-986d-38d0-9e78-8f59be2cbbce | -3.12639 | -53.76253 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8057ac4b-bc14-36a4-90da-bf166de28f1d | -3.12005 | -44.35065 | 2026-10-07 04:19:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c95bbb25-7ea1-3c37-8222-4452a94d9eb6 | -4.92307 | -55.86267 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6e4e57b-a6a6-3f74-bccc-f030944a5e7e | -3.5095 | -54.66191 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a170bf4-f5d3-3909-91c3-b9464ccf8cd4 | -3.29371 | -54.07527 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 48abd00f-63e4-35ec-9001-2af0365d3681 | -6.84883 | -41.77384 | 2026-10-07 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7dc1bc7e-a9cb-3087-ad6c-ede060e0d334 | -5.01361 | -50.93847 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 771a5131-34d2-37f9-a090-9a77e54a6e24 | -3.61832 | -55.28954 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 886e37b7-427b-31a9-aea2-f2cc486b2d7a | -7.30076 | -48.61667 | 2026-10-07 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e283120c-db15-3305-a6fc-c76210982cbe | -5.97128 | -40.94787 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53636d30-4388-3936-a4f8-2256fa675c62 | -5.97769 | -40.92943 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README44.md)
