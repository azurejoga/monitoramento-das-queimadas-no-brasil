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
| 693ccbb0-3a1b-3677-aa4c-d6dfe62ff774 | -10.04722 | -53.76163 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0390ccf3-bc6c-3297-9077-ee654e514edd | -12.2319 | -50.78306 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5b2fe81-41a3-31b0-a765-661172e608e5 | -8.93801 | -45.8941 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9769ce33-0d68-32c1-8f22-d2df3b74dd25 | -8.32926 | -49.51538 | 2026-09-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a01b1c5-6e40-358a-b801-833d77fcb36c | -10.6237 | -51.34667 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56a56604-833a-3c38-95dc-26b7daf5847b | -10.55628 | -59.49346 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4108152b-6ac4-3e9f-8bf4-1470bb06d5eb | -11.28204 | -51.28823 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b5139254-bd13-3f0c-8685-b37242a3a7b7 | -12.2115 | -50.74 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a8070a8-39be-356e-a8a6-abfb06488d6a | -12.23138 | -50.74323 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e391f94-0174-3c93-89df-cce8c91e6551 | -11.03722 | -54.12036 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d567c4a7-df63-3114-80fd-aa01ea9fdef6 | -12.23246 | -50.77954 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c4e9388-89ee-32c7-9722-d43c74f3f845 | -9.28414 | -45.90622 | 2026-09-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b61a6252-cf5c-3bee-9017-2c12014bc9a9 | -12.22252 | -50.77792 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7c87225d-74e6-3a46-a21d-0016d66f5d91 | -12.20873 | -50.75761 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 666fe376-e547-31c7-ac45-1c92ae74daf0 | -11.28755 | -51.29638 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b643073e-1186-340d-86f5-524bfe91721c | -10.61432 | -54.00368 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f7e9c48-a037-3862-a21a-d1bea3109003 | -10.62234 | -54.00062 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f35b28cd-cdf2-3b67-a8c7-95376c00cc2e | -10.63644 | -51.35236 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19834ddb-4dc9-3769-bf3e-03ee776bb27e | -12.2391 | -50.75895 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed469012-8a9b-337e-a82c-c4fd4f7e9a00 | -12.24132 | -50.74485 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d2fa2c03-1cdb-312f-ba45-15d5fff96282 | -9.36105 | -60.36459 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3dac6b9-3b13-3e2f-8396-c9a8f307cb53 | -6.68376 | -55.05862 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec26537-52aa-3c23-91c2-83380dec8ec9 | -10.4152 | -53.7839 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6e81bfe-7777-3628-b773-4a225a397f82 | -11.27477 | -51.31237 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b2fb4bd-6320-3202-b75c-1bcacfeb4a21 | -9.0156 | -49.64232 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9653bc4b-be15-3897-b065-b837b323af1e | -12.22418 | -50.76735 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2969278f-89b7-3e75-8d07-bb2a35f7d796 | -6.68306 | -55.0541 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed742bf-4284-3213-ac26-10fa92b9d692 | -7.70036 | -46.66473 | 2026-09-25 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f27c76d-636f-3233-b4e0-73bc354176b6 | -13.06667 | -43.27498 | 2026-09-25 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ddf90389-d48c-3f5d-807f-0fcf730634df | -11.7238 | -50.56011 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad7e8642-83a7-39ff-a30e-4b1b2bc94037 | -11.28586 | -51.30696 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfebff1b-a4f0-36bc-9114-ed601522b699 | -9.93529 | -60.72036 | 2026-09-25 04:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de202904-31ff-3c12-bd21-5550e58b3a38 | -10.55744 | -59.48712 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67402350-076a-3c21-b889-f66b14778b0c | -8.31443 | -44.13331 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efea9094-23e7-3c3b-bc9f-e30cd5ea977e | -11.28254 | -51.30642 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e3a93f-cb1e-3572-895a-61d9eb17c9e9 | -12.22363 | -50.77087 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f6fa9587-f309-31a9-9c0d-b98032b72abb | -10.89728 | -53.95196 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fa35fec-a380-3cca-8ce6-46cd6ad72b29 | -9.16052 | -59.41576 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29b86e20-3f07-3a5c-8ac0-8cde4aa663f3 | -10.55798 | -59.49021 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21295968-14fb-3e6d-9450-91082b49ae03 | -12.23853 | -50.78414 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3915ea99-7df6-366e-bcb0-9efb488fb21b | -12.22637 | -50.7966 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3dc4c54-e911-36c7-bb2c-c157887d99f2 | -12.22472 | -50.7855 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2209bf3-2da2-3f9e-8f5b-4d7dde369ca6 | -9.15018 | -59.49287 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922f3f63-33fd-3041-bc07-e1da63b8f4f8 | -6.48494 | -57.87741 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c7d4052-9495-3d7e-bf7f-7b2079cfd5ed | -11.27759 | -51.29474 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca0cd648-b6db-3a78-8b0a-52b689cc2962 | -9.01505 | -49.64582 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bdf3ae6-a0f4-3c93-8831-8ec6d3839bc2 | -5.34743 | -49.04091 | 2026-09-25 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7b118fb-03b0-3b62-b8cc-4dcea8e1a330 | -8.32865 | -44.1562 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda6bc0d-02d1-3fda-b15c-d4edee5d252a | -10.56315 | -59.49121 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91fec4cd-2d56-3be2-80db-7c669d4bf121 | -12.22528 | -50.78198 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffbb03ac-f2c2-3a8b-9348-70612090056d | -10.04752 | -53.7641 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2630e96f-0ed4-36d3-95a8-89e60777296e | -8.33462 | -44.1449 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 844ef897-434f-36b5-9ab6-1a0c065b3a4b | -11.18084 | -51.36947 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a1115e4-c956-3060-9aa7-2c37a4ae7717 | -10.89694 | -53.92696 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d085a1f-00bf-3bc0-98ca-39f7a2c02e37 | -9.02423 | -60.52839 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01d9e8b9-7b10-3b52-b49c-d54cf132d158 | -12.2203 | -50.792 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aec3a242-d23a-3604-ab55-303e15874476 | -10.28736 | -49.95532 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74f3ea17-f1ef-33e6-a238-9619314f8c98 | -8.93731 | -45.89894 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 355213d3-532d-3447-8f95-7758fb68c3b5 | -10.56894 | -59.48899 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cdffcfa-fd4e-3e36-8188-497788d4c801 | -12.20705 | -50.78984 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 87eaf9ad-8d43-309d-8b61-9e004f7467a9 | -11.97028 | -50.69762 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 822ad926-5360-3708-ba2f-c928260996e9 | -11.27929 | -51.28417 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7a1109f-45aa-3457-9a2b-7ae92167aa2d | -6.68086 | -55.05063 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af0c531-5d02-369f-8edb-93fee404d06e | -9.73746 | -54.80235 | 2026-09-25 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b14680d7-7404-3128-a674-8f9e5f6756ce | -12.23912 | -50.73727 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8927e3ae-f189-3dff-8933-5fa0ad59e449 | -12.20981 | -50.7939 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5481648-bf0c-3d81-86d9-8023623f6e9a | -11.4244 | -47.41474 | 2026-09-25 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90b3de73-ecf7-3dbd-b066-da641133c822 | -11.16178 | -50.65629 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 084737f4-23da-3881-8efb-0781fdf86605 | -12.20819 | -50.73946 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad3059bd-fb23-3fc9-8a9d-fd3aaa06d20c | -11.28315 | -54.04049 | 2026-09-25 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8496934-eb7a-3580-8ad5-31fe9789fc08 | -12.24517 | -50.76355 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a07661c0-8875-3a1d-86ec-e27698b91714 | -10.42679 | -53.8034 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 101399c0-9555-3a9a-9d6f-b7e2493fce13 | -12.17777 | -50.80312 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 42dbd9d9-14be-3cfa-b749-de27ce7c4fbc | -11.27978 | -51.30234 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8480eb14-5628-3710-98e8-ca3b1d4ed05a | -12.2126 | -50.75463 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a79062b5-da54-33c2-a2f2-dd6820670ddf | -9.63448 | -43.96457 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e54f14b-555e-33dc-8d4b-ee484887082a | -9.58238 | -60.521 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b7bc7ea-fdd6-3488-a464-0fc084d80edc | -12.21589 | -50.77684 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c67f81c5-6902-3977-b9bd-26030a3fe28b | -9.15443 | -59.47978 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ea07cf7-d0a9-3e71-a00c-5681f48ffec6 | -11.28035 | -51.29881 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab7ae369-c56e-3f85-89de-0b9bcfbdae73 | -12.23577 | -50.78008 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16c2bc04-9ab4-3373-8754-ed2c01dc8a7f | -12.22694 | -50.77142 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22d0f477-79ee-36ea-83f4-1368bce8bb00 | -12.22639 | -50.77494 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e490a50-2bc5-36ea-abdb-9846957186f7 | -12.22087 | -50.76682 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c927944e-8b0c-39a9-b8dc-3b4d06c12225 | -5.45518 | -45.87272 | 2026-09-25 04:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f5da3c4-ba53-36dd-81ab-c7d0736d5bf2 | -11.16509 | -50.65683 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 781ca779-25fc-343c-9d8a-d56bcc422ced | -11.46992 | -44.20997 | 2026-09-25 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00b36ce7-063f-37e0-9686-c59f64887aa8 | -11.15847 | -50.65575 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a37caeea-5f07-3c4b-8de5-2749a8803b55 | -12.21867 | -50.75923 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 85d2f41e-f07e-3179-bb8c-f2f16e578aac | -10.89946 | -53.93921 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92ac74d4-4da2-3709-87b3-e8d9b6f319a5 | -11.28423 | -51.29583 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63d1dbe6-9309-30b8-a8d4-f88124b82d33 | -8.33035 | -44.14423 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 553b1b85-acc3-3339-a0e6-6e1d17a5a8dc | -6.68437 | -55.05491 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afa5871d-7a60-36b1-94ab-d94112a40b9c | -12.22857 | -50.80418 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa989439-4454-3011-946d-215dc9a47fbf | -10.05085 | -53.76227 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a9f919-8b2b-3086-a01d-17c057938e04 | -12.20596 | -50.77522 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62bb222d-0c32-33fa-a072-50f5803c0347 | -8.20182 | -54.74582 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9526208-3749-375d-a8ef-88989fec6e49 | -11.18197 | -51.3624 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92f9a03d-67dd-301e-a04c-a31e38960f7e | -7.12028 | -41.72583 | 2026-09-25 04:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 05cfa7b5-acba-3af5-8bb2-2cc8b5ad907f | -9.21107 | -60.46334 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README25.md)
