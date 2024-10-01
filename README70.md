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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec925d7-07bc-36ae-af91-a666ab50bd56 | -8.44567 | -46.45509 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24471365-93cf-35a7-bcd2-c008de36c4e7 | -8.44435 | -46.46317 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff5b086-2f8b-3e5d-872c-212291920f44 | -8.43535 | -46.3612 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17753170-c45d-3ce7-8c7d-be0ae1759dea | -8.43115 | -46.36455 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb414e4f-6bb3-399a-b2f6-7fa45d56923d | -8.42515 | -46.33434 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a52b0f87-eb8c-3ff8-81bf-fa23d436cc8d | -8.4216 | -46.33368 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfc1afb8-429c-3d03-96f5-a7ce971a8899 | -8.41805 | -46.33308 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 939ff423-7a13-3d11-ab4a-2600d6cd9d88 | -8.41738 | -46.33717 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b82c1b30-0bfa-33ba-bd68-a83bfa1401c0 | -8.39289 | -46.37473 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0739d404-286a-3e9f-8b61-9bcf5737b5bb | -8.39222 | -46.37877 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1d9ac41-5547-3430-a97c-66b11a496223 | -9.76631 | -46.07113 | 2024-10-01 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baf152ae-5ed5-31bc-adbb-8823f3efbdc8 | -9.53429 | -46.51217 | 2024-10-01 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75912990-d8b2-3168-a00a-f859f9387614 | -9.53364 | -46.51619 | 2024-10-01 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5dc1e0f-f5b1-3b1c-bfaf-173410a394c1 | -10.50223 | -46.31253 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85a10346-1ff5-328c-aeac-7d538e440428 | -10.4994 | -46.30804 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d955e40c-c4fb-35a8-b0db-531da7a9f5e0 | -10.49875 | -46.31197 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0d3264f-1423-34d2-973b-23ffe737b45f | -10.49592 | -46.30745 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7982365b-d4b5-347d-8c0f-daf0ff14161e | -10.4931 | -46.30293 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 865c36ae-b978-394e-82e9-5bbef64f1d08 | -10.48962 | -46.30232 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d0819c2-4187-3709-99b0-c77bcf25b6d0 | -10.24608 | -46.87196 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56290e36-4a59-30b6-b9b3-6fcf37744590 | -10.24538 | -46.87613 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc9513db-9b79-3e9d-811c-77e22c9f9b65 | -10.52514 | -46.0434 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f915a3e8-8eea-391b-824f-1d6fd2990a3b | -10.52171 | -46.04282 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b671caf5-8b94-3fa2-945b-1fdfb7998816 | -10.51827 | -46.04226 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebdb7703-2ff9-3c97-afe8-697431167d70 | -10.51482 | -46.0417 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e01c555-a269-3c21-b59b-4ec59d0ad899 | -10.51138 | -46.04115 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d3e0417-98d6-3182-9d71-858058b94d12 | -10.50731 | -46.04441 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697bd2db-9bd8-385a-9a4a-c591969eba62 | -10.50324 | -46.04767 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5509a2d8-4930-3c3e-803a-0ed318a816fb | -10.49979 | -46.04711 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54a9f7f-97be-33f3-9253-49d9482dab68 | -10.49572 | -46.05037 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 589be712-2a06-3430-af1c-c1b175616c93 | -10.37865 | -46.16514 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 036878f4-39a5-30cd-8e72-167eef44a4c0 | -10.35223 | -46.16096 | 2024-10-01 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10c619c4-c596-386c-b02b-2e660a917693 | -6.02112 | -47.4403 | 2024-10-01 04:12:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63181887-e060-33d1-9f5c-c690cf250845 | -6.02026 | -47.44272 | 2024-10-01 04:12:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc3f1cba-2a14-30c5-9e51-4b03e30764e1 | -7.68972 | -47.25959 | 2024-10-01 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7584663-badc-3f5e-8c4d-b24cca757954 | -7.68595 | -47.25896 | 2024-10-01 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10972948-a89e-3959-b3c8-3d6f500a348d | -7.48275 | -47.05346 | 2024-10-01 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0f6f627-839b-3f7e-af93-288c8c5dece5 | -6.97688 | -47.61836 | 2024-10-01 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7aa47962-44c6-3e3b-b3e8-df1f6c65c066 | -6.97605 | -47.62328 | 2024-10-01 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6ff540c-0226-3312-8757-0edaff8dba97 | -6.9632 | -47.65186 | 2024-10-01 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f953f20-809b-359b-89e3-77f0f0c15193 | -6.96018 | -47.64606 | 2024-10-01 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585a0df5-e4fd-3068-8b18-4a1317821e20 | -9.20655 | -48.65717 | 2024-10-01 04:12:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60153031-5e93-3080-b6fc-064f95a238fb | -9.20596 | -48.66059 | 2024-10-01 04:12:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7995a086-4b9d-3e5d-9744-f7d2361bfc6a | -9.20533 | -48.66419 | 2024-10-01 04:12:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0145c448-36a5-3e94-9f96-668cb2acb3cb | -8.43969 | -48.62115 | 2024-10-01 04:12:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 981ae16f-7f89-3836-973e-036927954ae3 | -8.43565 | -48.62038 | 2024-10-01 04:12:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf196e1-9f9b-32c1-853f-92d180f4d93a | -8.01763 | -48.32299 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24074188-58b1-30d7-a831-21b73fc5e426 | -8.01705 | -48.32646 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92fddc35-162f-3aac-ac6a-afc017ec6857 | -8.57955 | -47.46263 | 2024-10-01 04:12:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65ba6ed0-b99a-374b-bf4b-6743d35111a1 | -8.52398 | -47.32868 | 2024-10-01 04:12:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ace213bd-81fc-3173-9927-a821b7736e32 | -8.43993 | -47.13182 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268b475a-17aa-3172-b23a-aabf90c244a4 | -8.4355 | -47.1356 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f502662e-8bb1-3676-b6b5-a569b811c423 | -8.43477 | -47.14004 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8264a57-c4cf-3bd4-90c7-54982b89626c | -8.43404 | -47.14452 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be2627bc-a6ad-37bc-9a36-659f87d826fe | -8.43032 | -47.14394 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1481bd7f-839a-35c3-b960-d0feb17eeae6 | -9.63871 | -48.53108 | 2024-10-01 04:12:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c052c09-0499-3e36-a9ac-77c9cd0a93a6 | -9.6362 | -48.52967 | 2024-10-01 04:12:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91625178-f50d-364c-99c7-e346939914e5 | -9.63476 | -48.53035 | 2024-10-01 04:12:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a14838d-17c0-3d54-abec-947e67ed73b0 | -9.37487 | -48.59772 | 2024-10-01 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a87b79a-574b-3921-8c71-ece61377f634 | -9.92735 | -47.7835 | 2024-10-01 04:12:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f33c5c47-6f36-3008-bd74-c2bf9e61a1f5 | -10.24167 | -47.80752 | 2024-10-01 04:12:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd54911-89c8-3bd6-afa6-f33066276655 | -10.23792 | -47.80683 | 2024-10-01 04:12:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3ee8547-162f-3b40-9326-52537e34ba0f | -10.22962 | -47.81017 | 2024-10-01 04:12:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53210a1d-1f47-3e8d-9e52-85d554afe7cc | -10.22883 | -47.81484 | 2024-10-01 04:12:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 553b69ea-bbec-357d-9f63-97630b59caf7 | -4.75702 | -48.00414 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93844fad-b970-31bf-8f6b-21644ea84cdd | -4.58109 | -48.0131 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83fdae4e-5c2b-3b14-858f-f5877a6edf27 | -4.57738 | -48.03582 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccba3459-e630-38f0-8921-b5fc90557ec2 | -4.57696 | -48.01241 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a196275-862d-3e38-86e8-a6535fce6aa3 | -4.57634 | -48.01616 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c369b620-a92c-34de-ba6a-e275786e48a6 | -4.49098 | -48.11148 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 254e0f21-524d-3645-a13b-923634908f67 | -4.49037 | -48.11529 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2988173-9010-32a9-88fb-bd33969f0f7f | -4.46889 | -48.11568 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03193328-cb20-3e75-aba7-31f502486d41 | -4.46827 | -48.11951 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11b5791a-5620-318e-8f0b-3f65e3454c13 | -4.46472 | -48.11502 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 963682a0-26c4-32ab-ae22-dab8b4908b02 | -4.4641 | -48.11884 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a424bfa2-cc69-3c23-858a-b6aa11bde485 | -4.28658 | -47.95613 | 2024-10-01 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fcf0d3-49b8-3760-ace6-c9532ca300d2 | -4.19382 | -48.23517 | 2024-10-01 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d1fe100-92fd-37de-b605-6954ce41a734 | -4.18957 | -48.23463 | 2024-10-01 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 599101c2-d73a-3c89-adf7-a90e4a9fee58 | -4.15346 | -48.39988 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86c705e2-bab8-36fb-be0d-fa6a287cde46 | -4.14921 | -48.39907 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78894428-e55e-368f-bccc-8aa4ffb8cb13 | -4.14495 | -48.39831 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f0c3030-124f-30a7-9371-b9c1ffbd0e0e | -4.14427 | -48.40238 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf967465-cac4-3b57-8ef8-b7aa65270a36 | -4.14359 | -48.40641 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c03f9eaa-a379-3c96-a01a-f46d6e3b09e8 | -4.14 | -48.40161 | 2024-10-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 227fd2d3-ad12-3c47-a8fe-0c1c88dbb876 | -4.0869 | -48.27875 | 2024-10-01 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbe07166-f7cd-37eb-87da-5cc91d866054 | -7.73822 | -49.21193 | 2024-10-01 04:12:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 078d9a35-29a3-39eb-afdd-5582e3ee25c1 | -7.63435 | -49.71415 | 2024-10-01 04:12:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67bd41f2-5439-39bf-84db-00b94ff8b61d | -7.6336 | -49.71849 | 2024-10-01 04:12:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9015a20b-fd81-3bfc-90a9-91eef509c7cb | -7.46747 | -49.6077 | 2024-10-01 04:12:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bf0a7a5-78d3-3ba1-82d3-022ffd46b141 | -9.14448 | -48.96676 | 2024-10-01 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6420f8f3-f901-3cf5-872c-789a6991fd14 | -9.14038 | -48.96608 | 2024-10-01 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2645c293-b2a6-3fbb-bd3a-ba99b0f56cb1 | -9.09015 | -49.27774 | 2024-10-01 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c04c90c8-552d-3dcf-8a7a-b57c14864d1c | -9.03472 | -49.82173 | 2024-10-01 04:12:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3adc2f80-df1d-3e72-9685-a27e832003a5 | -9.03399 | -49.82594 | 2024-10-01 04:12:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 898d39b7-e850-3775-9d64-9655b7b5fc68 | -8.80626 | -48.94873 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 064a2867-d121-375c-ae98-cb263fc0f525 | -8.80551 | -48.94462 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc505c58-130b-3680-99f3-f9a39ba333e1 | -8.80486 | -48.94833 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a43114-0051-3745-b287-fd0f6d2c5f16 | -8.80277 | -48.94429 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 920faab4-afb2-35be-9bd0-e438e9b579ab | -8.80215 | -48.94801 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a5be5e5-65d1-3447-9e23-2d71d729a1c4 | -8.80075 | -48.94762 | 2024-10-01 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README71.md)
