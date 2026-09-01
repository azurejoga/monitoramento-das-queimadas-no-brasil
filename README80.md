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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de9ab5e-a1b8-332a-beb9-31bc38ef67bc | -11.10385 | -51.54323 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c4f1b8fb-e723-3b0c-8239-03aa8785cfa2 | -9.93998 | -60.51285 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9553c67a-79c2-3dcb-a73a-f4e69e6ca3dc | -6.8047 | -59.57181 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0162a3c3-8b75-30cb-9a1e-ecedec5d61fc | -6.24329 | -55.4846 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42aa1d54-d505-37cb-a580-bcb635c972af | -8.59075 | -54.77555 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f862fc8-7dcf-3c63-89fe-b75b51f17fb5 | -8.93816 | -62.36463 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2eb1378-e5de-3db2-8771-1639dd147050 | -10.90106 | -61.67977 | 2026-09-01 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe06cd3-cf05-3a58-81da-cee38763388d | -9.154 | -59.53908 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dba7f8a-8f2e-3102-a444-7eea2d55c8a5 | -11.69036 | -54.54684 | 2026-09-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54d4e00a-063a-34b3-a03b-c81bc8f7eb87 | -6.95991 | -55.63908 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 374a01dc-4712-3f56-b7f1-a698377f9c33 | -6.76489 | -59.47465 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cb4c6fc-7d38-3b28-94dd-b4d6fcdc599e | -8.68352 | -62.81666 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a221fa50-4865-3a49-9ba5-2aeb947c6e68 | -8.95454 | -60.60197 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3095342b-ebf4-3491-8395-33d097631bb3 | -11.48148 | -58.51951 | 2026-09-01 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597638a3-a3c5-3113-b20d-e3ff37149dff | -11.25823 | -50.56666 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a35e0f5-677b-3a4a-8b5a-cf5c604c5da4 | -9.89444 | -60.285 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfc119a-51fa-360b-85be-70f56ea4940a | -7.29341 | -60.5735 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd524e90-b31f-392a-84c8-df1f2f9afb40 | -6.90448 | -59.48681 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40a7c569-4c65-3ec5-bce4-8da1656db0de | -8.26918 | -54.93206 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d4c61334-b71f-3e39-8f11-165f78c39845 | -7.01757 | -59.59838 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a740491-a3ec-3ddd-b89e-2bd301eb533a | -5.84937 | -57.75215 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537c67f4-aa60-3a70-94b9-b83f1b2b0b17 | -8.12299 | -54.96422 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0a249084-ee6e-3d90-91d3-fb9b74b53e13 | -6.94943 | -55.64715 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc944c3e-114b-393e-a40a-fd8b827c9b9a | -8.77081 | -69.34083 | 2026-09-01 05:36:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c27b18c4-cccf-312c-b72c-e5d4aba684c2 | -11.31137 | -50.57919 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 486e48d7-4d82-333f-9be6-619ae2f25f41 | -6.6841 | -58.75152 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef5c0ad7-5e50-3541-9d5c-21e9d33c420b | -7.183 | -55.48703 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1199263-dc96-3787-bafb-023fc12d0db6 | -6.95079 | -55.6379 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b0ae944-d49d-3c0e-aac0-7376d466c3ff | -6.18804 | -57.7379 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20c30de0-bb36-3de4-b751-a1bff0460bf7 | -7.01982 | -59.65134 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78d1c0a9-6aa2-300d-b067-5760c2c0d7db | -9.15529 | -59.53043 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4245dc40-cf04-31b9-b94e-2bb4ecd7179d | -8.69785 | -69.41822 | 2026-09-01 05:36:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f93f094-0caa-3c27-a3d3-e695da04ce65 | -7.56094 | -60.47117 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88903107-9c36-360f-bcdd-fe2fd6406e14 | -6.59962 | -58.59521 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdbdbed6-4947-3cca-99a6-241406da81fe | -7.59573 | -67.41977 | 2026-09-01 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10069c63-62de-374c-a194-1ac8004a51c3 | -7.19698 | -60.67649 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e7c293-c045-300a-ae2a-f28cbe855bc7 | -6.88444 | -59.45029 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c200d8a0-c32b-3c00-8811-a08096703eb6 | -7.05066 | -52.71559 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b693e378-841e-3136-8fab-82b97e782ebe | -9.03346 | -65.42902 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b7e130-4127-3cce-88a3-cf646e7e7221 | -9.32622 | -68.88745 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8550dc2-1aef-3f8f-8d8a-fdd73aac58f1 | -9.13517 | -60.5261 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83a7b9e9-2f58-3612-9bc0-3aefc0d08742 | -6.80772 | -59.09366 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 483b3694-5705-3dfd-9d31-d00f8e09441a | -8.87082 | -66.77422 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 248c4334-fd19-3345-9fe5-275892e1d02a | -7.59011 | -61.34651 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6534e21-1f9b-3118-a6bb-3573723fc26f | -7.34936 | -55.19788 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aef0ccd9-fbb7-35bc-a74b-92013ed9b0e8 | -7.52975 | -61.381 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75d451a9-7efa-323e-a6bb-9cca90f4b55e | -5.85494 | -57.55511 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 10d5fb4c-35d0-3903-a567-abce580ba793 | -5.59184 | -60.23069 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbdc47a4-6dd2-3abd-97ed-d0e96df1dea7 | -11.24877 | -50.58992 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaeab70f-79cf-3a32-9a39-19257a9b4bb2 | -8.37543 | -62.72499 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69841c83-f852-3f94-bc50-7cd749425f7a | -7.28013 | -60.65891 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5484c325-abd6-3c3a-97c9-3a1f890843e8 | -9.00643 | -67.80251 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cde8d63e-ea95-3b5a-aca2-10a471076993 | -6.95129 | -55.64086 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b50ca4d6-b70b-3ded-981e-7dde8e69140d | -7.02677 | -59.56252 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a244ebc5-8d90-3b19-9d25-454219b43ba9 | -9.02669 | -65.44804 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5472a3f5-0acb-3dcb-bafb-e5659911d43c | -6.13206 | -55.63895 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e276de77-0a7b-3ba7-a801-a876fe841ba6 | -6.94624 | -55.63723 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7422dda-6cab-34a2-a73b-2fcf2078f3db | -7.58506 | -60.47501 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eed7f083-afd0-3c3a-a9d4-4c40beb01f49 | -5.94337 | -57.68668 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc3698a6-5fbe-3447-bfdb-d5b1339a75cf | -9.00317 | -65.43295 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da740f89-6dae-37ea-a733-911a53b3c4a5 | -10.42099 | -57.23362 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b42d07-7c93-3be3-aec4-3447c67edcb2 | -10.21433 | -50.3165 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4be2cdd8-e64b-3dbb-8440-a37fb881eada | -7.32012 | -61.14376 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793e276e-8636-3c04-9bb5-0cf707bfe7e7 | -5.94263 | -57.69162 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b29beb2-5440-3a9f-8e32-c95ec26285fd | -7.57416 | -60.4771 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9191cef6-9fbf-3cd2-8e3a-814564e76fa6 | -7.03434 | -59.22514 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d84b3cb7-6ca9-361a-8395-bd0f46e3cb24 | -6.18098 | -57.73172 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8845c7d7-8d63-37ff-a7e3-1d46aee4193d | -8.89378 | -68.90046 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6a45376-6a7d-3ec7-9265-c658f439e3d0 | -7.59195 | -60.47615 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc39dcb-3319-3d06-af6b-22af59df6a79 | -10.51429 | -57.43154 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd55c02e-a256-3c67-ba48-dd495d561763 | -6.41449 | -52.20109 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66148ba8-87cc-312e-80e3-223f6138afc6 | -7.57154 | -57.699 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88cc7449-594c-39c4-bf23-f668ff56bf42 | -8.12715 | -54.96999 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08a6bbef-fefe-3cb0-8d26-c76fa702fd2a | -7.34991 | -72.95587 | 2026-09-01 05:36:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66403d5f-55ec-3eca-bb45-6f50b1d1a7a6 | -11.25324 | -50.58231 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2054b8bf-d59b-31a7-88ff-7a64b7b51eae | -7.34015 | -60.58807 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bb54a1f-1489-3eea-91bb-e7291204e990 | -10.75296 | -54.0696 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43c11ccb-01ff-39e8-9189-fcb19e711257 | -7.58278 | -60.46688 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a30304-ab39-3251-8007-5b66ef68a8f1 | -7.28297 | -60.66315 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d35b47f8-0d4d-3323-a653-e01f123704df | -7.56898 | -60.46473 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cea3405e-46fd-330d-af25-b42b2d753333 | -8.80854 | -71.28853 | 2026-09-01 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a4e8f7a8-9070-3726-9686-284b292c0093 | -7.32703 | -60.60508 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bab2fa7f-5987-3f86-be9c-8dc8c1872ccd | -9.25357 | -68.18638 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43ca83f2-79d5-31fe-b819-888ba138899f | -7.57358 | -60.48085 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d692d5f5-f574-35d4-bb99-93464d860524 | -9.03455 | -65.40108 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e809d64-84a7-359f-95c6-43650f8e53d8 | -6.35558 | -55.86523 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fbec8c4-053f-3c8d-943c-558051b18822 | -6.11565 | -57.68646 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f856f9d2-3f1f-3980-a30e-58c90f101e31 | -11.26427 | -50.57351 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d0dadc1-f559-3301-892e-2dedf93a1521 | -6.15486 | -57.40403 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3deae7f0-b10c-32bd-b190-f29042ef7a3b | -9.83558 | -64.97523 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 866271a8-f178-3bed-a9f5-4443e869366c | -9.48038 | -57.02693 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60d0b41d-9546-3ccf-89b7-2ba5779c7943 | -7.58623 | -60.46742 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a6e153f-e7d7-3bce-8051-cac3b24165b2 | -10.33449 | -50.00378 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a622baa3-77d0-3a7b-9295-5fa6293797f1 | -8.92876 | -63.28421 | 2026-09-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43748f92-1b57-39fc-b521-25505328c05c | -7.18675 | -60.67486 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50eade82-087c-3cd2-b22d-a02500711f51 | -8.93539 | -62.3606 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48d39e5f-bf03-3d00-93a3-79602cb9fe77 | -8.78817 | -62.47691 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6beecb09-9cf3-311c-ad44-a8f9a07f308b | -8.12876 | -54.9682 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b5775a1-89b5-357d-ac38-e9100b283a00 | -8.71762 | -67.10931 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7151f571-d442-388c-90c1-101f0d2ee035 | -6.18413 | -57.73732 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README81.md)
