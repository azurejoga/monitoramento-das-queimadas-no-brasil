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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06f95bda-d806-3ab1-818b-8f4e764a5bd6 | -2.89289 | -50.44573 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa04ce49-597f-36f7-a5a0-c9029f55ef2f | -2.90549 | -50.40896 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 295b009d-292a-30d5-ba33-bc3003e1f4d3 | -2.89725 | -50.41823 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 54f0c238-e838-3c2c-b217-006ce1d3d817 | -2.94086 | -50.46381 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 320a4d70-468a-353b-9042-70928e35edb2 | -2.93027 | -50.40227 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4efd9052-63e2-3f10-88e1-8ea67d7002a6 | -10.6818 | -54.17803 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99f348f5-20a1-3cce-ae40-01d6c3148d46 | -10.94603 | -48.36076 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aaef65b2-007f-3d14-8cba-a9fe76f89462 | -6.11332 | -57.67463 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eafddef8-2697-358d-a463-e5026de7df3b | -10.67712 | -54.14247 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ecc4a18b-5081-3f97-91d1-935c91cd0898 | -3.41343 | -58.21349 | 2026-09-14 04:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f89b3af7-6a62-300c-a0cb-3c32317c79ef | -10.6534 | -54.13902 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0a0c9d9a-b078-3b38-96c8-7e247b13587f | -9.44298 | -50.12267 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16e07bcb-8c3b-3054-84cc-c34a3b2cd02f | -10.48625 | -51.24121 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faaa519f-6b68-3914-9f7e-a579b0b14248 | -6.28249 | -59.93581 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2992365c-865b-3896-8a59-0390c62455c5 | -10.68895 | -54.156 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fe823b0-764a-36cd-aa0b-9f03705b8ecd | -10.68304 | -54.17049 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13bb4394-b4cb-3dfb-b6d7-b6289752f2ee | -9.71257 | -54.37798 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfb96470-5ff4-393a-bd6b-d8d787e18631 | -10.37694 | -46.65068 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3caa5c43-4d8f-369e-9e7a-4598230471b5 | -7.11758 | -41.78605 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43dc9ea6-23a1-34e3-91ef-3d9eab720395 | -11.17628 | -46.39183 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf6860eb-e70f-3e25-a6fc-770b7d8b5649 | -6.07192 | -57.86475 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e94bebf0-57dc-3b74-adfc-00aa669744d8 | -5.83865 | -52.11055 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f77fc7-e960-333b-a3b4-e36890ca14f1 | -16.30411 | -53.84334 | 2026-09-14 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70a7f1fe-0e8f-3f19-afca-243866dab092 | -6.85638 | -47.42616 | 2026-09-14 04:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58ec1167-1833-3291-825a-e5142b04be6d | -10.03529 | -52.12624 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dedacd0-01d2-327e-bbe8-3a33319c6917 | -3.71105 | -58.86375 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc450715-3be0-3704-ae15-9d4fdc847e60 | -16.23022 | -52.64679 | 2026-09-14 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74cf030c-ad00-38f7-b13a-606a6346e2f8 | -6.0772 | -57.86096 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e6090e0-0ef9-3a40-97d7-9b497d884174 | -10.67371 | -54.14188 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e674313-af41-36f6-af1a-dec33d219bd7 | -10.66957 | -51.34951 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d261c5f-e430-34b1-8528-a0c2a36a0445 | -8.45697 | -46.86407 | 2026-09-14 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5c496a4-e91f-3ba3-8540-1f22f71b729d | -10.47358 | -51.32298 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a97db3-add7-34eb-bf2d-92e02461a57c | -10.97928 | -51.43161 | 2026-09-14 04:53:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52e4016e-a364-324d-bcb8-6178c0e07400 | -3.59867 | -59.07571 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29c664ec-8795-307c-87fb-3b1a8f02fbda | -7.07904 | -43.545 | 2026-09-14 04:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9443a1b-598c-34d8-8b7d-2e492d30eb0b | -8.38891 | -46.29466 | 2026-09-14 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2589fdcf-c92d-3a5d-8d14-a8f192930fb6 | -9.79478 | -55.30837 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4a44ac46-bce1-3e7e-b06c-0da9d0a000a8 | -9.40506 | -50.16244 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| a0febb69-99f8-3069-b023-c71db18ab02c | -4.53254 | -54.9683 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc3da920-0824-3416-b0a2-636a3960d69d | -10.48291 | -51.24068 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbadc358-e0c2-324d-867d-0b52d4be3d73 | -3.81178 | -58.90555 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5da8159f-bc42-3f67-834e-68c4a4502d48 | -10.96215 | -58.95811 | 2026-09-14 04:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d061f7d4-aa51-3856-aa23-2cdf5d26115d | -4.13749 | -54.02397 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4df8b336-bb67-3deb-a65f-83bee6e63806 | -10.66003 | -54.13954 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdd39cbf-d9d4-3e88-b7ef-7c3d2a805377 | -7.52283 | -47.33668 | 2026-09-14 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58428c72-f229-35ff-aa85-62f3b2d7e8d5 | -10.66375 | -54.15948 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 549cfeb6-8c2f-3293-9364-e5b6bd7beb70 | -10.7497 | -54.08544 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e33490b-3273-36dc-b0ff-eee6eef81aa9 | -7.11661 | -41.79324 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a39f1e3d-3bd8-380a-83fb-a4da120e7b96 | -9.44871 | -47.87592 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2d6ffeb-8a81-3b8f-954c-b49bfb53148c | -9.43462 | -50.12912 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90925a0b-7cca-3b7c-a909-3d31af298e30 | -10.53911 | -51.29685 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bc34331-b899-3327-ae38-94cdd954e850 | -8.50402 | -54.64727 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9469371-a136-3347-951d-0489c6e78d72 | -9.68282 | -54.84114 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1391b7b0-b281-3bbe-88ab-c08b4e8c2052 | -10.54744 | -51.30912 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e053f4-eeca-39e9-9eb4-205e66a508f7 | -6.67984 | -58.88076 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b88612-33b4-3162-89cc-3038d64fd852 | -5.9315 | -53.65245 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02e9e55-15dc-31e8-8126-0b048a6dbc19 | -10.67059 | -54.16066 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6d9fe7f6-f209-39fc-8480-ff290552c78f | -6.29126 | -59.95484 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b654ad9f-152c-39df-b3b1-228e757cecef | -6.37386 | -58.30476 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 672d2b49-e64f-3a93-9113-e90c6cd157d4 | -7.08731 | -43.55707 | 2026-09-14 04:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75f9b0ab-211a-3423-9cea-9be1fbaf1e14 | -9.36703 | -50.16033 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb953040-d936-36c3-a388-5268957ff503 | -4.77914 | -56.15368 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43a77253-d881-3413-bb4b-32858f1b77b3 | -5.1249 | -55.95016 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a31d48c-29e6-325a-9437-258f520cf305 | -8.23145 | -49.9628 | 2026-09-14 04:53:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0032f731-753b-38b2-b9d1-bd1f7e493a35 | -10.53522 | -51.29988 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a34c05fb-e12d-3f9d-93d1-3bd45d996e18 | -3.72142 | -61.75684 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b5e8a2-4fc5-3194-8dba-eee7ad04fa7e | -6.69063 | -43.14191 | 2026-09-14 04:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd9e4202-7155-3079-9173-5ab51018de7f | -6.2907 | -59.95795 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2fa4672-4353-35e4-a988-ffa24c34d6b5 | -11.24426 | -54.15143 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3315f1c-2c5c-3d6e-9f4e-23cf0ea02430 | -6.30666 | -55.28547 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20034d1f-7170-39e6-a119-611a3b10eaa8 | -10.57687 | -51.33569 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 663aa044-e9b1-3f4d-861c-90933f943e50 | -9.70627 | -54.37276 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b135ba21-a2bf-3666-9a8f-8a258cc992b3 | -9.58237 | -55.1436 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d44668-14e6-3e7f-9b09-30cccecc9249 | -6.10659 | -57.63354 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfc8bf8b-bbaf-305a-8ce2-a7e27977b0e3 | -7.86546 | -54.71696 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78f3b38f-24ec-3ae7-b7fb-bbf325e1a83c | -10.67184 | -54.15314 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9a5f77ac-36e7-300a-bcff-b36591418a1f | -5.81975 | -52.10027 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e30cf067-52d9-3767-8ed5-631ecc28a2e0 | -6.10216 | -57.63276 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f6add75-6715-3439-a668-f35dcff2625a | -5.80136 | -52.1082 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a343a503-4c5c-3714-b55d-6f6d63402424 | -10.47528 | -51.33401 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898054cc-37fd-3e17-9f02-78c3fc0846fc | -6.29985 | -55.27951 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b3df3dc-5a79-3b71-89e7-49cd3698d176 | -6.6901 | -59.13078 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45d95cce-f7d7-3d13-87c3-87750648651e | -10.11297 | -48.8523 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e99d206-5f03-354c-b440-ce1ea41ce508 | -4.3697 | -55.03727 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 722cedc8-50ec-3876-a7b5-83fe4ea242d0 | -6.66438 | -50.91084 | 2026-09-14 04:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38bc60d6-77fd-370c-8d58-db1e2d4bbfa7 | -6.137 | -57.69701 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84e9e273-4504-3bf6-94cf-fefdb3e218ac | -6.58183 | -58.85099 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6be0b1c4-25d9-3958-922f-4f8cea5137b0 | -6.27732 | -59.93493 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03ca6260-3aa1-3eb3-9d7a-8b70a88a54ee | -6.11478 | -57.66601 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e55b24f-7fb5-30c7-b411-780e305e1cb5 | -9.4352 | -50.1254 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff2fb14f-6d67-3f71-974c-e78b24e6b9b0 | -8.12105 | -54.79976 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cc43409-538c-301d-bc5a-858d36cffa7e | -8.54001 | -54.69527 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e86a88b8-4a5e-3450-9fa0-71bf9fb0593e | -6.84552 | -55.56357 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b272e23-50b3-35b4-8e70-2662f17a5206 | -9.39371 | -50.16825 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86757011-0619-3c08-b4c5-5f77ec083f1f | -10.40843 | -57.22708 | 2026-09-14 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 684ec5af-0f63-34e8-a0ad-15279d43905e | -4.39004 | -55.21068 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 048d298e-d78f-3aff-93f6-b7e8849d6cb5 | -3.17851 | -61.12079 | 2026-09-14 04:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ea0899-00c9-3b9f-89c5-ce306909c658 | -6.3143 | -59.97523 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c1096d-8545-3a65-8034-0409b556a1a5 | -7.86185 | -54.71637 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491d13a9-bc93-305a-a53e-f1b98fc61991 | -6.29682 | -55.27427 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README39.md)
