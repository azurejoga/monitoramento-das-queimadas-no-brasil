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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18a88d37-01d3-375d-ba0c-cc4974ed13f1 | -11.28588 | -54.57851 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e783cc-f578-3090-a837-a443db324d6f | -11.2824 | -54.57793 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d1100d-e477-32a4-855d-bb81fe349e98 | -11.28174 | -54.58187 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7060d43-2f1e-3520-b646-03afc51a8e91 | -11.28107 | -54.58581 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7b1dd73-2e67-3931-87ca-e8c04c2be2ef | -11.281 | -54.57933 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b28f17fc-ccbe-38b1-afe8-3b66ccb6b16d | -11.28036 | -54.58329 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81fd2820-4b15-345a-bc01-9fe23fadae75 | -11.27972 | -54.58724 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cab1488b-ec62-3857-bf08-be83ea64b448 | -11.27825 | -54.58127 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1854b22-0316-3188-9784-408091024c90 | -11.27759 | -54.58522 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d162db79-0dc3-3c00-b30b-9727033d892d | -11.19125 | -54.88396 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d58069de-4245-3213-878e-dfd9eb2d97c2 | -11.18771 | -54.88333 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad767fc-535f-3f73-81b1-d2ea6396eb3d | -11.18242 | -54.76242 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebd0d3b8-6bd8-3943-a5f2-287ac9f3591f | -11.18176 | -54.7664 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2603b62-c1b4-38c0-9e0e-a74de9eb903c | -11.1789 | -54.76183 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb24bec5-31b0-3398-905f-24ebd66f65d4 | -11.17824 | -54.7658 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 183da8d4-3b0c-3b39-b5b0-552a4d92a091 | -11.17472 | -54.76522 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b05c7d9c-4b97-3c3c-9258-5effff0372c7 | -11.17405 | -54.7692 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40360ff5-4600-32a5-b432-294977f6e6a2 | -11.17272 | -54.77718 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28f51c0d-4730-3b7e-870a-bb6144af2408 | -11.17205 | -54.7812 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e94cb98c-519e-39e2-8ea0-6c3dd2292b86 | -11.17137 | -54.78524 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72b44e6d-fd62-3258-8f34-ba8cc1b5c892 | -11.1692 | -54.77659 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91666975-00af-37e1-9da0-9b74faac6a97 | -11.16853 | -54.7806 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a2c5cb8-48f9-3605-9ff2-e17f84609c32 | -11.16568 | -54.77599 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f99ecd-0cf4-3c7b-b475-6a790d4906ff | -11.16501 | -54.77999 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d4c5318-cd7c-3482-a066-8f1d63f80ecc | -11.16216 | -54.7754 | 2024-10-10 04:44:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7892a50-f184-3053-aa8a-9f66c70ed3e7 | -3.62551 | -54.05203 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a931063-1829-3f40-8c3b-7fdd335f700d | -4.32634 | -55.19642 | 2024-10-10 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed409675-03c7-3536-8464-c07bfd772b5f | -4.12943 | -54.89956 | 2024-10-10 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17bb0433-aebc-3f74-9d5e-b93ec38a3cb4 | -4.09439 | -54.72598 | 2024-10-10 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e1cb5ab-d7a5-3372-a77f-986d5a7ea04b | -3.9252 | -53.86239 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05fb4028-4a98-37bd-a9f8-b32e7bace14a | -3.90211 | -54.43335 | 2024-10-10 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ced41fa-f88a-3d6a-8715-648d6984038d | -3.76808 | -54.27833 | 2024-10-10 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f17abaec-f2a3-3237-a724-014b66421dc9 | -3.70845 | -53.9288 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df9300f9-5dc4-3038-b42e-5da003811b2f | -3.70478 | -53.92811 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9851d778-debd-38c3-bab7-3100fbe48137 | -3.68569 | -54.06947 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50864ae6-9ab6-3649-bfde-c9d38281ebc3 | -6.43462 | -55.62768 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d63cc10-fd6c-30e4-b2b7-ca2d1647aa6d | -6.43432 | -55.63033 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 748eeafb-bc80-3662-ac17-0425f0f9d2a8 | -6.4304 | -55.62966 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f581bf99-f268-3246-b8ac-dd9e53c94deb | -6.37473 | -55.13488 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc2c0210-1828-3a40-b50f-e182de947057 | -6.22396 | -55.66009 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa70034d-92b4-3114-ae3b-b763cea5c5f5 | -6.16887 | -55.48419 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09b686a8-9c32-3feb-8ff3-3f7a065aaa47 | -6.16579 | -55.47865 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e0c3341-a4d4-3fdf-bd13-eb72ce1ec741 | -6.16189 | -55.47801 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd05c29-f3ad-3316-9592-d3965d5afad3 | -7.17109 | -55.55155 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 432dec9b-f662-371d-89d4-a85b465222c2 | -7.16803 | -55.54605 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 883926e0-f63a-3d66-89b5-16689c770372 | -7.16723 | -55.5509 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b9c2aba-bfc9-31f4-a0ab-fe536b63c7b8 | -6.8926 | -55.05178 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebf83558-ca3a-3a1d-b8a4-bd40a61cfc6f | -6.87434 | -55.115 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdf6859d-d724-300f-9752-78d306e5a36a | -6.8614 | -55.14598 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d8e5569-d2b5-3c3c-a7da-7cc217195bc7 | -6.85305 | -55.14936 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8e22fbf-1cd1-3851-918d-7f9097c9f5cb | -7.97163 | -54.83149 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d35a3c-d632-3370-a25d-ee48bfca6d5b | -7.97152 | -54.82887 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41774077-ff6a-3e90-9085-a590a2c49b3d | -7.97092 | -54.83586 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05124fe3-5f26-37b8-bfea-aee8dd2592d4 | -7.97078 | -54.83322 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c803b7d8-4c80-3b5e-956f-93e0f64441c6 | -7.96797 | -54.83089 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e950630-c6e5-3977-b200-17a87abe8225 | -7.96599 | -54.75083 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da71d8e2-c873-334c-8be6-892dfa639645 | -7.9643 | -54.8303 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201259ff-647c-39b0-9fbc-8eae8860507c | -7.96235 | -54.75023 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10aa9301-bed6-3dbd-990e-d8aa18226ce0 | -7.96178 | -54.77659 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d5c03e2-6004-39a7-8472-841e15eaa287 | -7.96108 | -54.78088 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbb2a426-9c49-3442-a422-d0e3caf9af1c | -7.96038 | -54.78516 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1a8c0bd-026b-32ac-98d3-e565ee95a7ed | -7.95813 | -54.77597 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b32cba6-2e9a-3478-9e94-442bd1045aa5 | -7.95743 | -54.78026 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646c774c-a1e0-35db-af00-ad2b49545d23 | -7.95673 | -54.78455 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c57fd2f-5fbd-30e2-acf8-1720b6dfabec | -7.95659 | -54.76248 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca99b159-bce1-3d21-a655-a10c207e3e8b | -7.95589 | -54.76677 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f7430e7-df89-31ca-847d-a7c3bbd6b6d7 | -7.95575 | -54.74474 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 406023b8-932a-3b4c-8cef-894a7ba88a25 | -7.95504 | -54.74903 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd96506d-9a60-31eb-a390-92dd29e98ddd | -7.95448 | -54.77535 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bb1d022-ac73-3d3d-b6ca-46a09bd89602 | -7.95434 | -54.75331 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909ee2e2-3810-3f07-876e-e071b509ad88 | -7.95377 | -54.77965 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fbd0f0d-4b1d-37f1-a823-03d0a50cba4e | -7.95082 | -54.77474 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da054adf-aa60-3380-bfd6-3933f82f9845 | -7.95069 | -54.75269 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc9f3a3-1ff9-339c-ad9f-714f6604caa8 | -7.94717 | -54.77414 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69feb1a-b958-3246-90e4-2d722296cf42 | -7.94352 | -54.77353 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f3318fa-0a83-3d48-a925-5647af8b7091 | -7.8945 | -54.72977 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc33b823-b5cd-3b0d-a229-62318a123553 | -7.87995 | -54.7271 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be24f26f-18a2-338e-b202-91e36705e494 | -7.86537 | -54.90338 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eacd2f61-a978-34a1-8671-2aeeb17d3246 | -7.86095 | -54.90714 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76688306-3cc4-313d-9c15-82b46617857e | -7.86088 | -54.8905 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c8b62b8-9cb4-35f1-802c-702011ce90bc | -7.86016 | -54.8949 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3151b1dd-3565-39b5-aa57-79500308e899 | -7.85949 | -54.89335 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 532bd790-d499-3c71-a382-f7cccc581dfc | -7.85648 | -54.89429 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac7a7cd-19c2-34e7-b4a7-571fcbfb7f71 | -7.84768 | -54.90186 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c57851f-ef79-3d67-a84b-50cd7e3feac3 | -7.844 | -54.90124 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66ac3e82-49b9-3f54-a286-c2c422210c93 | -7.82353 | -54.72754 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b4c959f-79cc-36ef-b034-c10b164a4eb9 | -7.82279 | -54.73196 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6f9b5d2-234b-3eef-979c-d08f931e4609 | -7.80739 | -54.71179 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d5ce703-f318-3482-89ff-bcff71c1932c | -7.80372 | -54.7113 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7ceafc2-d785-33eb-b1f3-1c3f521aad8d | -7.7907 | -55.22773 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9182f29-8d23-3fc2-9d0f-f8328a5c664d | -7.72444 | -54.80665 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7b6a1b9-58bc-397e-92ce-66b843bc63ca | -7.68634 | -54.83159 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d52ad7-f241-31d5-8695-33ae44d79760 | -7.68562 | -54.83593 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82e2afef-b26b-3db5-8e3f-daff023be8f1 | -7.68266 | -54.83099 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8a5e6f9-ca32-371f-9092-922291f0b37f | -7.68194 | -54.83534 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bf4068-ff02-317f-82ae-d4da3c077af7 | -7.67898 | -54.83038 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933e0f7f-fb8d-3f50-b054-431f3d62f60f | -7.67826 | -54.83475 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84312a8c-43e1-359e-a36f-e27a826657e7 | -7.67753 | -54.83911 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88d6bd37-4d50-3377-9b8d-aef3d037bb04 | -7.62661 | -54.97203 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e77c310-88c8-3a15-8c91-59637c8a50d7 | -7.55521 | -55.36336 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README112.md)
