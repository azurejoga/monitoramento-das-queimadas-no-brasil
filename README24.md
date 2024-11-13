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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d40ffc7-1a6d-3e19-9b0f-c2dc00cb48d2 | -4.65374 | -45.11714 | 2024-11-13 04:57:00 | AQUA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6f9786ef-dcb1-3d54-b431-4bf5b4bdc9cb | -3.25319 | -43.25973 | 2024-11-13 04:57:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 655d16c5-037e-3283-a7db-47f127551f00 | -2.72371 | -45.28139 | 2024-11-13 04:57:00 | AQUA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c8fed15b-35ab-3a1e-8568-f14307ff87b7 | -3.34431 | -48.92385 | 2024-11-13 04:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1c92afe7-737d-3df1-b145-dbe3820afcb5 | -3.25135 | -43.25261 | 2024-11-13 04:57:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1aacc45f-1966-335d-ba01-422c6c90c226 | -5.35452 | -43.53288 | 2024-11-13 04:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25189ff9-9390-3903-9b45-fafbdd8bd9f0 | -3.33832 | -48.96151 | 2024-11-13 04:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6bfef2a6-0167-31f6-bb2f-bbb9dc793e35 | -2.73654 | -45.28346 | 2024-11-13 04:57:00 | AQUA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5365a36e-1204-3b2e-81ec-ef6a65d4b16f | -3.34328 | -48.96717 | 2024-11-13 04:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 417565ec-1081-3d4b-b6a5-7a5f221ef831 | -2.73428 | -45.29065 | 2024-11-13 04:57:00 | AQUA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 55c94b95-83fe-3075-8be6-1a4120ac8094 | -2.97792 | -45.16135 | 2024-11-13 04:57:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c9cdd3f5-215c-3cbd-b5d6-d768dc63d933 | -4.65086 | -45.13525 | 2024-11-13 04:57:00 | AQUA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dca8c1cc-8e96-33ad-812a-ce3de0f6c5f3 | -3.24932 | -43.26615 | 2024-11-13 04:57:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dd4d4935-5e91-3821-ba69-bbf6ed530996 | -3.34952 | -48.92951 | 2024-11-13 04:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 107407f0-a32d-3a7b-b770-a551c3e48d05 | -2.06713 | -51.46605 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34762788-48a7-35ee-923e-85ad37257304 | -1.38552 | -51.40506 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc348ded-0f83-35ed-bf1c-4b0b774b7d25 | -2.77851 | -52.86719 | 2024-11-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b7acbd9-40ba-3e5d-9dbd-1d592b4c7386 | -3.02322 | -50.97536 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58077a41-fbb9-3d76-a795-f08a2b942083 | -3.122 | -54.17927 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d18d51d5-4985-3924-a298-504089f13628 | -2.91789 | -49.24657 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f088d102-d0ab-342f-a3bf-1f68b5a63f45 | -3.85448 | -51.91175 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aaffde1-6b48-3203-839c-27cda5110d0a | -3.26383 | -50.42876 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 198f6f3c-cfe4-35ac-859a-ae6cf5d9032f | -3.016 | -51.43112 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bbea630-5181-33d0-910a-cff0dbab490e | -3.34332 | -48.95267 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b92425de-ade0-3d2f-8335-b77a4cb5b3ad | -3.80284 | -52.26992 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d749c7-8334-3bfa-8f4f-1cf4146de541 | -3.27541 | -50.50587 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5ef286d-93d7-3ba3-bfa0-7a521b47fe26 | -2.79943 | -51.49506 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a90718db-0436-3510-844f-6c73a6c1b17e | -3.86869 | -52.11309 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4639d8f-2bd3-3169-987a-5811eec39a8b | -2.60798 | -48.25227 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2558576a-8a04-382c-8259-4953349ca721 | -1.81178 | -47.9761 | 2024-11-13 04:57:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08fed528-d7fa-32df-9492-29b08db21cb4 | -2.30819 | -50.67739 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f03acf6-aa4a-37c7-97b5-bac06e174553 | -4.61804 | -47.95298 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d958da-00c3-3128-b33b-7c307bbd6c37 | -2.11821 | -50.68734 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84890b09-9a61-3b7f-94f5-aeb0800783f7 | -4.47064 | -49.63199 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f3b35c8-7a74-3d41-a629-1d0109cf8e5f | -1.39874 | -52.18162 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038d9aee-6e41-3c21-b58e-4b56277f372f | -3.26069 | -54.53073 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81527869-a581-3a28-834c-52e09c672d8f | -3.06472 | -50.33983 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54954a78-a912-394f-ab13-c994a7032cd1 | -2.28035 | -53.77199 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53a961f-7501-359b-9f0e-30490b49b4b8 | -3.0275 | -51.44834 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 093a60c5-4148-3a1c-89e1-177f96e5a502 | -1.47436 | -52.5048 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de417778-601e-36e4-8a08-4dbc3979bdbe | -4.33981 | -50.42361 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09ca36b4-8d44-31d2-b347-7394dbd33d75 | -3.17542 | -50.44941 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65eaeb3f-e8a5-3c50-b77d-9ca30e170355 | -3.29295 | -50.75248 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4d6fb6f-bb59-338f-9d5d-cd6ad6fdfad6 | -1.69478 | -52.70533 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53519bf2-58d3-3691-9b65-94e5e44ee125 | -2.58397 | -54.02739 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c46611-33ff-38e1-bb80-d033695dba83 | -4.95407 | -50.03168 | 2024-11-13 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5feb4154-1511-380a-adeb-b61bba50ab58 | -2.62436 | -54.27078 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ead733-1883-33d2-88c0-c78761100c90 | -1.61904 | -52.38436 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f33ba5-3685-36ba-9b22-5830084c10d2 | -4.2236 | -46.45584 | 2024-11-13 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb0e036e-c6ad-38cc-9a2d-2c26f92302b4 | -4.3754 | -48.08181 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e1911b4-faf0-3750-ba73-21e8ba13ab8c | -2.81945 | -54.00044 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5646951-587f-34c4-9917-5dcf0bb97857 | -2.03891 | -56.6597 | 2024-11-13 04:57:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10101fb2-6165-3079-aed9-380e1a3512c4 | -0.95211 | -52.34183 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041c6f3d-1bc8-37d1-a56c-e21a02e28856 | -2.88831 | -54.17057 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1e1a359-274d-34b0-b208-1f18cec3e79f | -2.4623 | -53.97975 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9cd2c09-3ee9-3a79-9057-5e0aa47ecaf8 | -3.59279 | -54.69008 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d7c176d-4832-3dd2-bf63-8b5166cc2633 | -3.66646 | -54.65494 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d575321e-51e4-39d7-8b89-8b1c016d3d12 | -3.66354 | -54.58671 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80a31453-d6a7-3fc2-8d1b-44827883ba4a | -3.74396 | -50.45142 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e957c27e-977b-3906-853f-9df20bbe6fc3 | -2.93574 | -54.4549 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7b39b54-4eff-3525-b3cc-59d2fb82be13 | -3.03407 | -48.07763 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9ee2d92a-c7d4-31fc-b658-eab3cb0aaeb8 | -2.96863 | -53.8764 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe133754-2b2b-3f30-bce9-6763f3fe359e | -3.09471 | -53.26295 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c417ce4-eda8-3ad4-a777-0a7b3bf642b6 | -2.2516 | -49.3256 | 2024-11-13 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a582941b-5666-31b6-af11-640a4d7fc45c | -4.49965 | -47.82936 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b873ea6-6f14-3880-ae41-14ad5802cb54 | -4.21715 | -46.82639 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| caf09f5d-9a1b-342b-ac4f-fc318a3ec015 | -3.26015 | -54.53421 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c463fb7-ee20-396f-99b0-63da9a30cbe3 | -3.41329 | -54.90322 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87da9fd0-4a01-3309-a656-68b09f0f73ae | -1.1361 | -51.9463 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c459cbcf-572a-34d9-a7f6-81039d17a6b6 | -1.65494 | -52.5467 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74497c83-53ce-3040-8035-e38f0e90fd73 | -2.66489 | -47.00141 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0245eac-71cc-3f28-9dd1-04f576ee886d | -1.28504 | -52.47522 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c35121-2d6e-3868-9ec5-abea712a767a | -2.73345 | -54.13898 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19a8e55b-9593-3722-b942-fb0902355957 | -3.0609 | -50.33598 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 546fa63b-94fe-31d3-92af-ead16ae3258b | -2.32146 | -53.88051 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b678ae4a-295d-3528-9111-b47585f5623f | -3.77638 | -54.64764 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1e8b9dd-14bd-382c-9c0c-05262a01e4e9 | -3.04177 | -50.56644 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91fa07b6-c61f-3535-8a03-db1a8e3bf034 | -3.09244 | -51.06915 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e267d710-e1b9-3c14-b13a-0b39fa9809db | -3.23405 | -53.39351 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a130482-396e-3442-9008-479d745dd153 | -2.39571 | -53.73011 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4cd20ae-950c-35ee-b39f-316ee99cb588 | -1.20713 | -52.12369 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ecf899a-d3f5-3fb1-9364-8d29f60c545f | -3.64173 | -51.4269 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5dcd7e4-ca9f-3ffe-a8be-12113e8e4c70 | -2.29525 | -53.52483 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ba31126-5680-37c6-a04a-0633e928e188 | -3.02262 | -50.97931 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1facea2d-614f-3d64-8d67-72540ec6e15c | -1.8838 | -54.19786 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe6b1599-c1e4-3586-970c-45f5a1065da4 | -2.44614 | -53.93143 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 588ae1c4-b8b3-3ed4-af76-8f2aadc1378a | -3.53598 | -54.48872 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50997bf3-93e3-3c6c-ae1b-180ada2bba04 | -4.51984 | -48.66307 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b91c93e-f3f9-3e3d-97a5-599dd6111565 | -2.12987 | -50.82526 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 023506a1-df25-3df8-bc9a-2e042f7a00fc | -4.8178 | -48.75876 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99817c44-6509-3e27-b214-d10f2b644a2b | -2.90433 | -48.30348 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e3c403b-0b2a-338a-81d1-ec8a52bb2851 | -2.40231 | -53.73112 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b00e6957-1570-3939-81a0-d6e58c4c285f | 1.58036 | -55.76474 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e684c766-ab90-39e7-a754-63c29c612a2c | -2.06258 | -53.40392 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b461d294-2daf-38cb-aa98-688a4583a066 | -3.45828 | -47.66433 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0efcd65-0798-3363-8850-76d19c4d946e | -3.17329 | -54.61012 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 666d11e4-4b67-31d1-bb4a-936d13b3a6fc | -0.78586 | -52.66664 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1cea16f-0518-3d48-8d55-d7c5985e56f2 | -2.99048 | -53.97474 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 762f0910-64c1-3c45-a6a7-3565fa73fe0f | -2.56351 | -54.0066 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7474480-11c6-3fa0-8850-a9bce112d1e5 | -2.73323 | -45.29013 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README25.md)
