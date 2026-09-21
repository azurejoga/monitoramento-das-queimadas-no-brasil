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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30ef5ed7-8ba1-3cd5-a59d-fd2242896eb6 | -6.13606 | -59.94918 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5c26ba-a286-3c94-ba23-fa45d223557f | -6.79899 | -58.79015 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da7a73a5-d3e1-305a-8a1a-2d0349efba03 | -6.72331 | -63.13338 | 2026-09-21 06:01:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 753b6d84-e4f3-33ed-9d94-24f3eaa010a9 | -6.72275 | -55.08002 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ffbec9f-e789-36fd-938d-0b02e342a1fa | -6.30952 | -60.01372 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e79119b6-bcb1-34af-bd1a-7adc5f31bc87 | -6.31514 | -60.01131 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6301a806-d79f-390b-8eb3-fb2bad6e07ef | -6.44797 | -59.98139 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d0974e-2c6e-3a97-af19-2a70ea109fe5 | -9.55903 | -66.05221 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 151375da-00da-3f07-a655-c9b35d273922 | -7.24724 | -55.60831 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6ce21f6-83ce-319a-b797-041095380d88 | -8.78389 | -68.84808 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f43fc65-69a5-3712-87d9-d2c9982c1b8a | -7.1276 | -59.65041 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 385e9e42-e07d-3b26-9548-cfeb93fdbc38 | -6.72623 | -55.08432 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cf12800-f757-3b1e-a735-2924d795d791 | -6.99074 | -61.34743 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cbc60eea-9565-34a5-8994-0c263469290a | -6.1432 | -59.9485 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5dc5d3-e7ec-3b30-9efd-7ff72cac1ec6 | -6.2909 | -59.92215 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d64ae1c4-d213-3ef7-9d3b-c63a35ed2c00 | -8.85173 | -62.3602 | 2026-09-21 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3139d0c8-a3d3-338d-b1d8-7e6a0b3b8942 | -6.75873 | -59.11686 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0abe5036-c1c8-3783-b0c5-150cdbac4abd | -9.27656 | -60.6344 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0e9ef66-9ed7-3051-b0d4-f81ff8c2e59f | -8.7961 | -60.79503 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4ff9c7b-65c7-3cff-ae35-6389c0ee0723 | -9.54874 | -66.04634 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4e1af3b-0cf7-3f6e-9c57-a470842632e6 | -6.43808 | -59.97663 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bfdaae6-de74-3f01-a7c5-805d85c4699b | -9.02363 | -60.36302 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d60e6cae-4077-3bb4-8a2c-d4dfbb44cad4 | -8.85385 | -68.51144 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0a63a0-1337-3647-88dc-cbaa7e85928e | -6.15734 | -57.95698 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c802332-9f75-375a-b8b4-02e4725a45b6 | -8.86498 | -68.50234 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a6377c-3690-3910-a49b-f8dcfadf5bee | -7.55525 | -61.33131 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b30c6884-40aa-327e-a05d-fd3f48fb7b01 | -6.30865 | -60.01976 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 257372e7-869e-3610-99ed-f202e163d963 | -6.28571 | -59.92135 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb419237-bc2f-3952-b136-781e1a8bd1fc | -10.46099 | -61.3121 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82e407ad-57a6-3a3e-b60c-521b6e75515a | -6.10154 | -57.68394 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d38ad3ab-3696-37d6-8b5f-9ff6be06cfa8 | -9.55691 | -66.01692 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 041724dc-6a82-3814-960f-18c311bd0ff8 | -6.45985 | -59.98064 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d795800-ad48-3a8d-8442-739773831370 | -9.56449 | -66.04296 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b70abcda-c8eb-3934-b4de-60540b0d1632 | -6.1883 | -57.77939 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eef5458-c859-3140-bd55-bc7a64ca12b3 | -6.69628 | -60.01085 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a869f0ed-29c3-3d5b-a8b8-360cc35d96b1 | -6.46371 | -59.99091 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 748341b1-075c-377b-8de1-2a8e62db3559 | -10.7897 | -69.54536 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34ad93c6-cf78-31b5-9fdb-2e27c33d5314 | -8.79064 | -60.79722 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b9bd30a-92b5-3f90-b1ce-3a7f5e9e5f21 | -6.72389 | -63.12954 | 2026-09-21 06:01:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc18b61b-d324-34fa-b63e-f164d48856c0 | -7.24 | -55.61329 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68dbde0b-1305-3bc9-90de-4f8b54d8251d | -10.09776 | -64.33652 | 2026-09-21 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3045dbd-08a8-3393-88cd-828b584fe27a | -6.45377 | -59.98637 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d97db41-16da-3d23-85a1-a280a8d1d50d | -7.24039 | -55.60682 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 751345c6-b244-363d-8ea5-5023fa583572 | -6.13742 | -59.93996 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c08f6e37-f0f0-3984-a406-c89c8296f888 | -9.56397 | -66.04419 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af89d6c1-8d70-3d1d-937c-623fb786bbb6 | -9.56813 | -66.04353 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e11b3cea-41df-3c1c-bdd5-bed67ab6d1bb | -8.86822 | -68.80785 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e61dfba0-8251-304b-b052-f3361e53840b | -10.2691 | -69.05595 | 2026-09-21 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e41302d9-21a2-39c3-8915-a3dd5a0cfeb7 | -7.25042 | -55.58801 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1109368a-529a-38a2-8b9f-64e22b6f0faf | -7.59185 | -57.67211 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce681861-2dc3-322b-b561-4e397d640ce6 | -9.56268 | -66.05273 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3688c59-c525-3e57-b4ec-2a7ca90767d4 | -9.5596 | -66.05097 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77d24e45-5bec-309c-817f-953576b44681 | -6.1376 | -59.95082 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b217fffc-665a-3c57-819a-f9fe3d2e9c64 | -6.31426 | -60.01738 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a628cffd-a2e3-30f2-9bfe-c64d79b9240b | -10.2083 | -68.75005 | 2026-09-21 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d18aaa9-2c7d-3aa4-b5a6-47655fd0a5e9 | -9.37143 | -65.47855 | 2026-09-21 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51aba19-bb48-3116-ba43-182f146a7fc2 | -7.59799 | -57.67294 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 400f4ca0-3300-3f8c-a2b4-6b1bd5c40e1b | -9.55174 | -66.05115 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8400c95-768a-3044-9c09-f06f0c791800 | -9.56324 | -66.05151 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 952fe1f0-a264-3291-9c71-e19ef6a73e9c | -9.54939 | -66.04204 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7bf9554-daed-3f13-9ffa-dac2e6b70a04 | -6.37922 | -60.01892 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 184da1e8-62af-373c-bc6f-6b0e48246aec | -6.72092 | -55.09336 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07915d2d-ba7c-3a7f-ba65-4748fac69b32 | -6.13717 | -59.95392 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aea1147e-eec3-3f08-b6b5-1e22e6dbd2bb | -7.91784 | -71.56076 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29f50510-1542-379a-a663-f094c2dc3991 | -7.24088 | -55.60665 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9512cbb0-0577-34f8-9db6-9c522f2292a7 | -10.89236 | -69.34644 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8ca2a9b-0b12-3715-bae4-3ceeefef0634 | -6.46071 | -59.97438 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7af11536-9b5b-3576-b578-6f804ceaa052 | -7.57282 | -57.67433 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de4b3ed1-f133-3a5f-824c-87fe435dac3b | -6.4948 | -58.38174 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f86a17-1cf4-39ef-bc05-14543f587493 | -7.58319 | -57.69007 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 41d00efc-d43a-3de7-b4d7-3f91ff7d9030 | -7.07926 | -63.03129 | 2026-09-21 06:01:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8937931d-3ec0-35ee-bade-0c64c23d5816 | -11.03518 | -68.48872 | 2026-09-21 06:01:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4ede59a-a8de-33cd-9ba2-fb02421d6316 | -9.5539 | -66.01208 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eae506b7-6b17-3ca3-beb6-79e8c8dc620a | -6.74268 | -59.42511 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9dce609-18bd-33a2-965c-1bddee0371bb | -6.3147 | -60.01435 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b5d4a5-7e70-31c6-9169-838e1897e99c | -6.99188 | -61.34484 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4a667e3-1ee4-3a6f-8768-f35ecf194cc2 | -6.82764 | -55.54304 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b884623e-654d-36e7-a24a-40faa9982f8e | -6.74512 | -59.42194 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9cbb4672-c7bd-3da7-b256-b8b668ad4771 | -9.55897 | -66.05527 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 112d825c-935d-33d6-b774-7ce8186da32d | -10.04031 | -68.78139 | 2026-09-21 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1790fc23-2dd2-3487-874b-c1adf131800d | -9.55927 | -66.02601 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aaf1c59-200a-3b63-9f8d-d49b08ec37c4 | -9.55562 | -66.02547 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89e46851-86c8-3404-a62b-eab866098a17 | -9.17606 | -60.30552 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25b338a3-2d48-3ddf-876f-0ead88537997 | -9.29504 | -60.53474 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56a575c8-9c16-3b86-a032-06a35f556398 | -11.99276 | -58.07793 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0c9670c5-1f32-36a9-b830-e5203aa0a29b | -9.61172 | -65.36809 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a87d56e2-14d3-3d39-b284-610ac89b8f55 | -9.74307 | -65.02039 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49006144-f258-3569-8d7d-b98955032dde | -8.2324 | -71.04859 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0573ecc-8f29-3c29-acf0-53f7de12734d | -9.54961 | -66.01585 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e22e5e33-f3e5-3e94-a9b1-378909fba099 | -9.55068 | -66.03345 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff15391a-464f-3824-9fa9-76b85f7088fb | -9.11244 | -60.94666 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8bc6f32-43c5-3d0e-8f27-a8fee2912dbf | -6.44556 | -59.9691 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b248214-ccc4-393e-b277-6e164ecbd126 | -9.55838 | -66.05647 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2af7e2f2-f6f5-346d-aed4-11e3cf439b4f | -9.55906 | -66.02901 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35fe3e32-6ac2-3ed8-b30d-4b610505fe03 | -9.56991 | -66.05688 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 333302bb-f51a-386d-a787-0aab26287c85 | -6.4536 | -59.97907 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db7c6d3-fe10-3073-a9f0-5b48bedd6220 | -6.30435 | -60.01306 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63f26a99-90cd-32f2-8708-756282321d58 | -9.56203 | -66.05701 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5d64076-331a-3a7f-8561-1fc94d350865 | -9.03787 | -61.65089 | 2026-09-21 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5899e333-402f-3ac6-9496-c70de803c80f | -6.73924 | -59.42462 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README108.md)
