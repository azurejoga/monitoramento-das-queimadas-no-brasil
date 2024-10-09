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

## Dados Diários - Página 213

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d18362b6-ad22-3a2e-a948-52bd6885af4c | -10.19998 | -61.96311 | 2024-10-09 05:55:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313ed5ec-acbc-3831-807d-6c15e95488fb | -10.14225 | -62.11163 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7bebc2f-34e9-3ef5-a354-0046c605f0ca | -10.13856 | -62.11395 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9dcb6ad5-54a0-3e74-a85f-7b45dd695808 | -10.13759 | -62.11105 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bbebb66-477b-3932-bc70-c89de6c904fb | -10.09411 | -62.51238 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fff0d54-b3e3-341b-8f3e-3ab6451c60d0 | -10.08958 | -62.51177 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9b29aab-ed36-36fe-99b7-2aed1e707355 | -10.08897 | -62.51641 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59370bb0-f0b4-3678-a1cb-4f36f3976309 | -10.08758 | -62.51355 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ba37148-d5a7-3a8a-a7f2-7ebdc9f5b52c | -10.08692 | -62.5182 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac65b452-d9e6-3147-8edd-8878ee8d8f42 | -10.08445 | -62.51577 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5300106e-5d43-32cb-95d8-400c1ccdd5fa | -10.08306 | -62.51291 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be6f6d55-201a-3ccb-aede-550abb0e52de | -10.08241 | -62.51755 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4626fee5-63ad-3763-9b1f-2dfbbcb9fdd7 | -10.07993 | -62.51512 | 2024-10-09 05:55:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4217cff4-03ae-37cb-bb37-96d47960fcff | -10.77618 | -61.51278 | 2024-10-09 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e41963f7-9ad1-3646-9596-4c404b4bf85c | -11.89438 | -63.28067 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e09192a1-cfbc-3a55-9a23-f1fafc208214 | -11.89057 | -63.27564 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46815262-3fa2-3192-81c6-7951c0f2277f | -11.88998 | -63.28006 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2b1294a-ca78-39ac-bd9e-41270af66237 | -11.88557 | -63.27944 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 028e1690-dc36-34f2-a717-69ad5af665dc | -11.82819 | -62.62499 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79ef6728-39d8-3307-a1fc-4324530e9590 | -11.78519 | -62.88332 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c604a00-e2a1-35f6-a886-92a69b55b20d | -11.78067 | -62.88274 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e979390e-27a8-305c-bb5d-cf7871343309 | -11.77615 | -62.88213 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb15d2ea-1938-36e5-b740-15ca06e1b455 | -11.77163 | -62.8815 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b0f6b93-88a9-3018-8a31-10c1a4f82585 | -11.76711 | -62.88083 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c41106a-1935-3497-bd66-242962120317 | -11.7626 | -62.88016 | 2024-10-09 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b196bfbc-1897-379d-bd71-97d1cee57499 | -11.72698 | -63.02698 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 528ce34b-15a4-3546-96c0-5234c1c894c2 | -11.48256 | -61.97599 | 2024-10-09 05:55:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 097d317a-65ad-31f9-81c1-5c3dfed0df75 | -10.14543 | -63.66953 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 123e3cdc-9336-368d-ad7b-d7570c8f1a13 | -10.13964 | -63.67033 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 035c16b5-5d80-3084-b048-1198771f2a9a | -10.13654 | -63.67224 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0ae63cb-6b4e-3ff5-a52d-4bee040bd1ea | 1.11546 | -60.51619 | 2024-10-09 05:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a50d0f65-2a3d-37e2-a99d-a6f147c1a324 | -5.69703 | -63.17523 | 2024-10-09 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aba701d4-9477-3ee8-bc24-f85debf2d508 | -9.31756 | -63.74546 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ecec4c7-6b29-3add-affc-aaf527d255e9 | -9.38587 | -63.41259 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5ead9cc-e9c6-3a9e-b361-4ef1955291ec | -9.38533 | -63.41645 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81389919-8363-349a-8026-e532ff00f9e4 | -9.29332 | -63.21017 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ffe21c6-bfad-32a7-83f8-85bd099b918f | -9.29276 | -63.2142 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c821d764-7a1e-3195-bd81-0c54ac05e700 | -9.13152 | -64.14977 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 883aa27c-90c2-38a1-ab9b-3c9096aee200 | -9.05652 | -63.23524 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b279a0-0074-30e7-befd-fd03cdf24abb | -9.05597 | -63.23922 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65874248-aca5-35c0-898b-dbd872f5ebba | -9.05229 | -63.23462 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1d915a9-67ec-3a49-a508-6538672dc1dd | -9.05173 | -63.2386 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef746e76-d9ae-3a85-a6b3-a4b9f05f2d14 | -9.04749 | -63.23796 | 2024-10-09 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9353a337-46ac-3b42-a938-b8b1951ecb0a | -8.76913 | -63.2211 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dd0be13-8e51-3715-8636-0973bdc63f04 | -8.76857 | -63.22503 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15364ee4-9497-355e-986c-96db5a88e27a | -8.60421 | -63.01575 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f35523c-43f3-3470-8f80-048653dea542 | -8.60312 | -63.01491 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 033b0208-30c5-3c31-99d9-05de6faaa636 | -8.10144 | -63.69957 | 2024-10-09 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1104c42e-8bf5-30ac-b801-8027d488250e | -7.91623 | -63.48033 | 2024-10-09 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dab6900-f704-350b-8ec6-3ae2b2367eb1 | -9.80413 | -63.85878 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a4dbd5-d5cd-3e1f-ab7a-130577d7f946 | -9.80363 | -63.86234 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1675f297-77ec-3850-8195-45e38d753df7 | -9.79954 | -63.89202 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017bf01e-e184-3a2c-a5b6-6878758d7c66 | -9.79544 | -63.89138 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a506da0-5c80-376c-a839-a6a7e56edd68 | -9.36226 | -63.81369 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87e08ade-3e19-3819-bf05-ccf793e67801 | -9.36171 | -63.81268 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49db764c-bd23-3ad6-8c1c-0397ce753a47 | -9.35872 | -63.80925 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1c7be5-6c09-3e55-9212-0599745435b7 | -9.35816 | -63.81312 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97fccb0f-6c81-333f-a9c4-560b3ef1b03b | -9.35761 | -63.81213 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4468a223-bbf4-3eed-982b-3226c92e4c5f | -9.52143 | -62.93174 | 2024-10-09 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3007e270-d45d-317a-b01d-0e0aa83ce4d1 | -9.50658 | -63.5434 | 2024-10-09 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c6cc53-8c80-371b-befd-2c7188c99590 | -9.50509 | -63.54367 | 2024-10-09 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dfea734-d9e7-3d60-9098-69cd0930d40d | -9.40409 | -63.65773 | 2024-10-09 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d7622d-1934-358f-91bf-8c750cf13932 | -9.40047 | -63.65337 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4d9d361-856c-3f98-923c-42be9f1d8829 | -9.39996 | -63.65709 | 2024-10-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c65d8a2d-9677-3961-af2e-2e7480406a3f | -10.70138 | -63.64193 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96bdd86f-3909-3ae1-8091-4b170d1cd735 | -10.69767 | -63.63758 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a6f41a-8e74-33e8-ac6d-2a8cf8d7751c | -10.69714 | -63.64146 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0623fce2-88a9-3b30-a234-c79fff65fb48 | -10.69663 | -63.64523 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa8de315-1883-388e-b5e7-d69022981b69 | -10.6924 | -63.64474 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2ac8d40-917c-3b96-ba36-9e1ca0404012 | -10.46184 | -63.15156 | 2024-10-09 05:55:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efbb4da2-3c48-356e-a30e-6643f8f6fb71 | -10.14594 | -63.66583 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8baa1ee-3ea2-3254-b80e-8d3164efc68c | -10.13604 | -63.6759 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11299201-adc8-3d27-bf4a-538b88e71646 | -10.13493 | -63.67348 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8325349-9511-392e-afd5-746ee3bf7eb1 | -10.13441 | -63.67713 | 2024-10-09 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af856a90-efc0-3f30-bf46-f66ed7737604 | -10.05567 | -63.25649 | 2024-10-09 05:55:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d073bd7-a1cd-3704-8a4b-04ac3a879898 | -10.03362 | -63.47571 | 2024-10-09 05:55:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aee085b-16c4-3b5d-87e9-b90736df02b3 | -10.03307 | -63.47963 | 2024-10-09 05:55:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 025faf45-242d-3041-b4d5-164979b118ef | -10.02884 | -63.479 | 2024-10-09 05:55:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6ab4fd7-dbac-31e1-9005-ed50d15003b9 | -9.81812 | -64.23058 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec52aea-7fa8-3c97-8053-cfc05644c811 | -9.81411 | -64.22998 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b988d914-5b3e-357d-8ab9-17199c8f429c | -9.73467 | -64.22975 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df5e034-cd08-3aa7-8063-234964814928 | -9.73415 | -64.23331 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae1ac5d-7a0d-3ffb-b8ea-c3f6dec8c536 | -9.7324 | -64.22889 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9dfb0dae-a98c-343d-8467-d0868521e4a0 | -9.73192 | -64.23244 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3205b7f-40e6-3e71-9bcd-ba53e776da79 | -9.73065 | -64.22924 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1e870e7-11a7-35d8-a04e-51693cec1d57 | -9.73014 | -64.23278 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9a7bb86-bbd0-3f40-83b4-1ff5ee774b16 | -9.72562 | -64.23573 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0539e652-9010-3785-89d7-ace70e5f3553 | -9.72512 | -64.2392 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00be136b-defb-38f0-9749-fb1ce954b3b6 | -9.64549 | -64.19479 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b10282bf-df84-32ee-bc3d-ab4404b56b69 | -9.58192 | -64.11027 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971522bc-ac62-3c4d-b5e2-dd938ea29367 | -9.57789 | -64.10973 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7443a554-5412-3195-9dfe-92c147964f2d | -9.57687 | -64.11697 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc228456-fb11-3c38-bf0f-4209b9c87f1c | -9.57645 | -64.29266 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65255695-1df1-3841-b47f-696a3a4ee56f | -9.57385 | -64.10918 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c7dc3e7-28ed-37a3-8b6a-b1c4f1047a6b | -9.57335 | -64.11278 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 854ffd9f-84ee-3aa5-a06b-6995b05ce340 | -9.52296 | -64.05484 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea3e0bf-6aa8-3c66-bce9-f2991fc9b506 | -9.51891 | -64.05427 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 584195f5-04a9-3a4c-9bc7-e9ae561df26d | -10.71435 | -64.15681 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb55378-877e-3e87-8328-da967782fe7e | -10.71432 | -64.15807 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae68949f-1a68-3b49-b36f-07cb88d722b3 | -10.71385 | -64.16051 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README214.md)
