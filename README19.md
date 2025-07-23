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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 914f575d-287a-3a14-9244-b49664126669 | -4.09299 | -46.92325 | 2025-07-23 05:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1eb1125-0170-36dd-95ca-8dd425e5ded0 | -12.50047 | -57.77151 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd4143eb-4468-32da-8e16-aa432fa136dc | -3.16439 | -49.44186 | 2025-07-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71865736-7f09-39cf-9b36-9a6eb8c45951 | -7.28022 | -47.5315 | 2025-07-23 05:23:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 205adef2-64aa-3c18-b314-3c4774c761c0 | -7.26974 | -60.17749 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2adb3153-8afc-32d5-812d-1644b05012d0 | -12.34844 | -63.42012 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 82bf2a8b-00f7-3fcf-990b-ad214921f090 | -13.72229 | -52.00976 | 2025-07-23 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5815eda-e031-388e-9c80-f12af3ed3778 | -3.03283 | -47.86613 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4948585-43eb-37ab-b148-6c3d4b249a86 | -3.03245 | -47.86461 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f94d3f8-a087-3d3c-893e-effa62b662cc | -6.21732 | -57.77505 | 2025-07-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9aff7f37-9981-30b7-b92c-e59305b0c1c2 | -12.50117 | -57.76659 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2aa5208-2cca-3610-a730-0303eced5126 | -3.18321 | -49.43605 | 2025-07-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c8c238-4f5f-3172-adc2-63f0bb551083 | -12.41732 | -57.4803 | 2025-07-23 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b79add5-ad40-3f2a-8471-1a53abf16b0e | -3.17024 | -49.44272 | 2025-07-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93b8a68b-5192-3435-9bba-e3c6d4bdf60e | -3.03357 | -47.86104 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b22215fb-9fa7-3d1b-ad17-7de80124e573 | -4.09266 | -46.92496 | 2025-07-23 05:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b60c17b-0bd7-3693-8be7-704cfd474569 | -3.74932 | -49.05106 | 2025-07-23 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c40a9e91-4875-390c-83ce-613aabef0b1f | -7.2736 | -60.17451 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 049ce2e0-d914-3a95-8765-3f3f7ae499bc | -12.35402 | -63.41695 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af201566-3ff9-33a0-8824-8bdf50bdef21 | -3.40551 | -49.53264 | 2025-07-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb3760b3-9696-3d37-9e4c-d24f578aee46 | -10.43132 | -54.37837 | 2025-07-23 05:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 592f8729-a152-347a-95a8-42560d7b848d | -10.3619 | -57.50049 | 2025-07-23 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 986691d8-cb4d-3f8a-ac56-eb228618c2a1 | -9.62643 | -61.46014 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06c66775-7899-3f89-91cc-e277885e9194 | -10.29074 | -60.53368 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c50deb15-1e96-3873-9c5f-f26acac5bcc0 | -9.46011 | -63.14706 | 2025-07-23 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e0eb95d-6e5b-3079-9539-d6d36dd0d947 | -9.91606 | -63.02103 | 2025-07-23 05:25:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2830c495-5b11-3afc-b1af-56a194aa384d | -10.04164 | -59.09438 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6962e72c-6cdb-3f84-941a-8b424fd9ddfc | -9.22746 | -60.92904 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 959ab7a4-d720-3ed5-a4a7-d5733e0b81cc | -20.29134 | -54.07956 | 2025-07-23 05:25:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56107eb2-d96a-31da-8f51-590b03bcaad1 | -10.04802 | -59.09935 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ea693e-f05a-365b-9af1-c0d86fbeacfc | -9.4595 | -63.15075 | 2025-07-23 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2945411b-71ee-3e7f-8595-a1a4551cbcec | -9.08637 | -64.17321 | 2025-07-23 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08030157-743e-35c3-99cc-43c320f91ddd | -18.66009 | -55.72571 | 2025-07-23 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| af56e697-1c6c-33a8-be5f-6b39ec6e4c61 | -9.02319 | -61.23508 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1e00111-8739-328d-a10d-2d702575e3c1 | -8.95971 | -62.21044 | 2025-07-23 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6de25774-a793-3b2b-aa5e-c14624fb89b1 | -9.01437 | -61.22655 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 551e1b55-2818-35dd-a75f-9c6c2a891002 | -9.23077 | -60.92957 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5261f412-9e21-3097-9d07-80f60e570244 | -10.05557 | -59.09653 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4229ebb-949b-3960-adff-8c59052dc5eb | -9.11941 | -60.75074 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc3b00d6-4f8e-3c00-bc1d-c9fed14e51a7 | -20.64359 | -56.55345 | 2025-07-23 05:25:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2deec79f-5af6-3024-add0-6d43c9385e9b | -20.29292 | -54.07907 | 2025-07-23 05:25:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90e456e3-c703-3565-a0bf-11704461e885 | -10.06602 | -59.09816 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 624f994a-f795-36d9-878c-a802b875f941 | -10.05209 | -59.09599 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ea11c1-7bdb-3dd8-9453-e6659f24cbb6 | -10.2874 | -60.53316 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a8eaf7e-fe93-3265-b4af-3010eef6bfa5 | -10.36123 | -57.50516 | 2025-07-23 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5e8766c-6f78-3040-acff-508d2ed5ad72 | -9.45947 | -63.14706 | 2025-07-23 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1583e7f-5c85-3c4c-8e67-76ff0c7405c0 | -10.43863 | -56.62892 | 2025-07-23 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32e871fc-11bd-3851-ab24-2be2ed3ad356 | -9.11278 | -60.74969 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c07553-f8f4-33d5-8fe9-12d341a4c165 | -9.64051 | -63.15686 | 2025-07-23 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce957e20-7c55-3a9b-9e98-3de580c8091b | -10.03757 | -59.09773 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 605b5ecc-5cf8-3bf9-8564-e335a7b7808e | -10.43813 | -56.6324 | 2025-07-23 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c82bd007-d6a4-3f7b-b066-981985982de3 | -9.45888 | -63.15077 | 2025-07-23 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a82ed6a-2238-3ed4-8ce6-c0bde6901ae0 | -21.44315 | -54.57998 | 2025-07-23 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8da9d280-2ec6-38ee-bdf1-b5e39ba1867b | -10.29631 | -60.54185 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b23dc86-7d43-36bd-b9c0-0f55ce71e2ec | -10.03816 | -59.09384 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47a481fa-24d4-3995-afd5-77a0b9aaccb4 | -18.66486 | -55.72633 | 2025-07-23 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3f7b2156-6b8f-3933-900e-2ac58362bc8b | -10.05964 | -59.09319 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad2ec747-4970-3de4-b090-962d717073bf | -9.24883 | -58.76407 | 2025-07-23 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7800d5-ae3f-3602-a14e-f0f2e222cd99 | -21.44349 | -54.57647 | 2025-07-23 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5b12c50-cf6d-339c-a77c-8e967914e753 | -10.06253 | -59.09763 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef9f4580-b591-3277-a17a-145257ac1d45 | -9.01242 | -59.75941 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b86d1f47-23e3-36df-b671-d889d635b9b4 | -10.04106 | -59.09827 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52eb0ecc-7f3a-3f12-9279-88fb3e49dfb3 | -8.72014 | -63.14204 | 2025-07-23 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eb09938-8c1e-337d-8f5d-fe2481f87ae2 | -10.06312 | -59.09372 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8f1396a-8030-3abc-a34e-71b9fde83022 | -10.05905 | -59.09708 | 2025-07-23 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8d0daf7-4b37-3a2e-b0e4-dcf2902fef82 | -20.29676 | -54.0802 | 2025-07-23 05:25:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc9aaa24-891e-348e-9f2a-d4f90d119c8d | -8.95695 | -62.20981 | 2025-07-23 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47c60867-ffa1-3115-9904-092bba8c190b | -9.1161 | -60.75022 | 2025-07-23 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85457276-ae3a-324e-8aab-8eef7ed15269 | -20.29835 | -54.07971 | 2025-07-23 05:25:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 380fa791-305e-36f0-8e43-26726d10bdb5 | -23.59566 | -54.32633 | 2025-07-23 05:27:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32c28603-a722-3cb6-aec1-3b6c3137f813 | -23.25224 | -52.19822 | 2025-07-23 05:27:00 | NOAA-20 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5b2201a-b4fa-3b16-ae71-3fe84b63d09b | -23.25263 | -52.1932 | 2025-07-23 05:27:00 | NOAA-20 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae7aaaa1-03e9-3b0d-ae00-34322a5b69d6 | -3.1832 | -49.4642 | 2025-07-23 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 39cb632b-be74-3013-ad83-6a4879cce957 | -3.1648 | -49.4648 | 2025-07-23 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5eddccce-875c-318e-8b06-fd1b8e37ee4b | -3.1649 | -49.4435 | 2025-07-23 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4d3562e4-ad62-3b6a-a5ca-31a25ea90539 | -3.1648 | -49.4648 | 2025-07-23 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0f9af53a-32bc-3d03-87b1-48ce044718e1 | -3.1833 | -49.4429 | 2025-07-23 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| fca8d0d6-e843-33e4-9a49-544c2bd97b42 | -3.1832 | -49.4642 | 2025-07-23 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 045f6a65-4480-3acd-ba7b-fe71b858240c | -4.1067 | -48.20134 | 2025-07-23 05:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 18bbc563-2972-3103-bb7e-08d518466c67 | -4.04851 | -42.50745 | 2025-07-23 05:55:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| ac5bcf56-0873-3fa4-b0b6-b8b13456760a | -3.17425 | -49.45992 | 2025-07-23 05:55:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 908694e1-3f2b-3c81-b8c0-617df421e994 | -3.16645 | -49.44856 | 2025-07-23 05:55:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d4fe1966-b6c0-373e-a239-031f2d178ab6 | -7.74091 | -44.02258 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 99d0deb7-e438-33d3-a2eb-90e6089dd9bc | -7.19397 | -45.32746 | 2025-07-23 05:55:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b0d7f88e-7dd6-3205-a5f1-d23a74658de5 | -3.17578 | -49.44995 | 2025-07-23 05:55:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2aa4439e-112a-38e8-a41b-876cf384a197 | -4.08553 | -46.92313 | 2025-07-23 05:55:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c848e5c3-bdf0-3088-80da-d3b7df26c7b1 | -7.75154 | -44.02465 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 91b516d1-2905-3371-9c0e-45ee86aba8eb | -7.19677 | -45.33354 | 2025-07-23 05:55:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| dd992e30-0a37-3e2c-a9eb-ea224cbce0e2 | -7.74685 | -44.01568 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 7c14ee68-441b-3452-a6bd-2d24ebe99376 | -9.05651 | -45.05282 | 2025-07-23 05:55:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a7276615-978d-3497-8458-2a617209fe43 | -5.67971 | -43.66784 | 2025-07-23 05:55:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ed3ec47b-45e4-3d36-ba3c-145e63af3f38 | -7.74281 | -44.0092 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7a0ceaab-2910-3a31-add5-169c1b0660aa | -7.75755 | -44.0174 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7255cc8f-a91a-3442-a046-efb590f3bae0 | -7.25262 | -44.29556 | 2025-07-23 05:55:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bfe215d7-3ea3-3732-8273-c1b08e347bd5 | -4.29833 | -48.09721 | 2025-07-23 05:55:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c969ab44-c72b-3374-a488-8bf69a952fbf | -7.88907 | -45.55227 | 2025-07-23 05:55:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1da968e5-aa32-3249-94e9-b10e262ddd04 | -3.03891 | -47.37924 | 2025-07-23 05:55:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a050fe3d-fbaa-3902-850c-fb1d4cc1f983 | -7.19829 | -45.32274 | 2025-07-23 05:55:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ac4acf4f-c565-3c11-9bb8-83db5f35d49e | -7.27013 | -44.36871 | 2025-07-23 05:55:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 96ae1a94-5e34-3b10-aaec-994e09b0a171 | -7.28049 | -44.37024 | 2025-07-23 05:55:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README20.md)
