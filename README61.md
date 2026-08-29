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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbe95030-cf4d-3904-b3f9-cc92240f33c7 | -6.16436 | -57.795 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 307b2262-7093-3656-b8d6-c22a599a6a5a | -5.89855 | -57.75611 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 490b59cb-724e-3931-a7c0-d9c0f1a607b6 | -6.95189 | -58.9514 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a22f9cfb-39d9-3ef7-83df-89cf34383edf | -7.49634 | -55.28931 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05abe84-dc13-3a49-976b-d5bae21995b3 | -7.36175 | -55.17291 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c470db22-7477-3c9f-acaf-79c2d0ac74a8 | -6.95542 | -58.9555 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97174cc5-e623-356d-8d83-1896bf5f61bd | -6.93756 | -58.957 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e202800-d9a1-3c49-9a6b-a40c0ac8dc17 | -7.50029 | -55.29946 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4d3dd57c-408d-37ee-9518-f6280fedfa9a | -3.9358 | -59.33023 | 2026-08-29 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe67063c-03d0-33ae-be9f-b4cfca1f6f2f | -6.2523 | -55.43225 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bb7a293-8a81-3519-9169-8c501ec084ed | -7.52761 | -61.37217 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41023c9e-7f0e-337b-a2cb-69d5fb528fb0 | -7.50155 | -55.28999 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bd26104-f477-3c18-91ff-2be33b4f38cb | -6.76729 | -55.66154 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39244785-9097-3dbf-9179-655c99a15f99 | -7.50279 | -55.28079 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68693f09-964a-3595-8106-ea6d85685fef | -6.77838 | -55.6902 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a023e9-42df-331f-a7aa-1850ea4e9d07 | -7.51676 | -55.2954 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b3e618f-f089-3474-af6f-ecf733400965 | -6.9421 | -58.95405 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf76d531-56c0-357f-8fb0-4fd143b3fe96 | -6.79977 | -58.98994 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84ea3d63-4a08-3b1e-9b3f-8d9ad16281e1 | -6.20838 | -55.41371 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1845869b-a152-353f-a993-274fd99ed863 | -5.9913 | -57.67975 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c507dcbd-a881-3b04-95be-a4626db35061 | -3.4275 | -52.77576 | 2026-08-29 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf7c8b7-54cf-37cc-9a66-d4543764b605 | -8.1847 | -54.93924 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73f9386b-17ae-3ad8-9b66-690e423b8dca | -6.76594 | -59.47256 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b824dad3-3bec-318e-bc07-41ccb05412bc | -6.94158 | -58.95757 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d50738e-6bf1-39dc-982d-a9fe0d7905ed | -6.75454 | -58.73016 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 626597a0-18dc-3f3f-ae6c-f2efa2bbf684 | -6.76696 | -63.04668 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51dc154c-9aa1-33e4-8ce8-8c3976956862 | -6.24724 | -55.43145 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26e35a5e-3155-3709-9b5a-5e6d5ddd9ef5 | -6.77791 | -59.44432 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba343c4e-2de7-3e24-93d6-d58023d3e9bc | -6.73682 | -58.70902 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a325a600-377e-3181-a63e-710e005034de | -5.89364 | -57.75972 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77dc114c-0695-318b-bd6e-9f6b054bf96c | -7.50322 | -55.27759 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f7e5d67-335e-3f5f-8d55-bf827486866d | -5.77134 | -57.55352 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25006167-7cef-31e5-b2f1-2127057bb2de | -6.88735 | -59.40699 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5d2c4ce-e557-3fee-8ead-a10811804022 | -6.77915 | -55.68455 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a47a119-069d-39d6-a715-75303eb4d74a | -6.85402 | -59.44075 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a7ae89c-af88-3259-976e-ec4d76f7c164 | -6.95591 | -58.952 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d32ff987-c81f-3dd6-b277-c45260d8d41c | -5.28714 | -50.93925 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec7158c5-d544-3ab7-ac2b-36988dc0aecd | -6.7271 | -60.0113 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b701f2d3-dd13-305b-9dac-4c64e5c7e659 | -6.75507 | -58.72653 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc855e9-08de-37f3-89d6-d0d321c5d8b6 | -3.63976 | -60.55816 | 2026-08-29 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d78155e-2d6a-3fc1-b800-d140dfe7dc0b | -6.57848 | -56.54466 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f23068a-0f60-30ec-843f-ecaf70b27a59 | -4.15814 | -60.6968 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa537d6b-a277-320c-86bf-4a146e3089fe | -5.22944 | -52.02216 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4ed035a-831b-3baf-9ba0-10c5b241eac2 | -6.60082 | -55.45535 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e8635e-f215-35bf-b9cb-ed78ef40ac5e | -5.22505 | -52.02145 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6827d1ef-c252-3df9-a0c9-25a8829201cd | -6.76564 | -55.67321 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86f5c34e-0f67-3603-be7a-bb98d1aab2dc | -6.1126 | -57.83049 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3adc635b-3f30-3999-93d2-310011b20e70 | -5.88336 | -57.77016 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 594686e2-9154-3caa-9370-1cb3b657fe3e | -5.85077 | -57.75306 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f77b10e9-b669-3708-8fac-1fe1762dadd4 | -6.77524 | -55.67769 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba3b36a6-263b-33b1-a2f6-2983321b977f | -6.79597 | -59.40163 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f591a449-e837-3aeb-a469-9dd9d5b53cae | -6.00439 | -57.83191 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a76f46ea-713a-3515-ab41-5e07f0a1e13c | -6.96605 | -55.70246 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 251b5e02-c921-3b9c-af6b-73e4e339c0e6 | -6.78768 | -55.65938 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c43de745-93a6-3ae9-99ce-f66935cd9817 | -6.77531 | -55.67511 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e54d684-634f-30a0-b5f3-dd15609d7d6e | -6.16925 | -57.7915 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9b0e185-f896-3f21-9a3f-32556cf71c08 | -6.86841 | -59.39741 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7ede64a-5e7f-3dd8-bf64-12fc96cbcc60 | -4.15935 | -60.68893 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78949ca1-ab6d-3253-8082-b4580b5299c9 | -6.24141 | -55.47255 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c004d53-de52-30c6-bd51-2ba60d09ac78 | -6.10785 | -57.863 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba8f206-208e-36bd-9650-7499cc219e18 | -6.83209 | -59.42738 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c62c4e-bc76-3cf1-a0a8-4de14a2c5293 | -7.36736 | -55.17429 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 603a8492-e197-37f4-b0dc-4612b7b0559e | -6.77685 | -55.66645 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 27ca9dfa-ca0a-3d9e-8792-b9b0012b5ced | -6.95469 | -58.95234 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2589fb56-9ea3-3e85-b53c-3d2c2a9d560b | -6.53796 | -55.24502 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b80593e-b79d-3f7e-9b23-4748f7865336 | -6.7865 | -55.66812 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 72bd273c-bbad-34ec-a681-c05cb42ca90d | -6.54312 | -55.24574 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e0d73db-7f87-30e5-b2e4-4b18fb527165 | -3.43366 | -52.77563 | 2026-08-29 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d90b6b25-eb23-3318-8b92-b26941182518 | -5.98758 | -57.67489 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d473124e-f0f2-39df-b9f4-4664ace9ffe9 | -6.77607 | -55.66947 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1773fe19-8ba1-32a5-a99a-6cf3216a4ad4 | -6.53755 | -55.24807 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80f1eab0-10c8-37ab-95a2-b111ef87a5b9 | -6.15173 | -57.9456 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73f3c595-8cee-32d4-b1ce-626988b4662d | -6.78416 | -55.68533 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0890a15e-80ec-3e57-b86b-ebafd2e8f021 | -7.53175 | -61.36873 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8aa7395-360b-31ac-beae-bc913c20d675 | -6.4965 | -53.26164 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9aff19b-466e-3998-9880-52ba1b81a78f | -5.88217 | -57.7784 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd2c22b1-bebd-385c-a7c7-db732cc1f530 | -5.87907 | -57.76951 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4d0f9f9-3b0d-3e0b-8adb-7b4e0c3c1097 | -7.5142 | -55.31432 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f744777-c953-353a-9cb4-aed192a6de57 | -7.50465 | -55.30643 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b64824df-830f-3690-956d-480e4e7fba7c | -4.15582 | -60.6884 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd866af9-7624-3fe2-aaf6-11459f5aeeb1 | -7.36692 | -55.17759 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ee4b353-ea14-3966-9d5c-bdc707cffff4 | -6.09292 | -57.72366 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30083607-4935-3dd5-9f71-d5035423624f | -6.22555 | -55.6199 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab5c33aa-57e5-3532-a358-879ad5fd177e | -3.16054 | -54.62915 | 2026-08-29 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e0a57c9-01dc-32f5-87af-a6231b4e4059 | -6.86868 | -59.03602 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2896c78b-aa2a-3c3c-a55a-fa6f0582bfb9 | -6.8833 | -59.40467 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 671aeb1f-cd40-34a8-a5b7-dbbd499aae68 | -6.76352 | -55.65197 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9f9e4f18-7b42-34b3-b668-14c566cc5f96 | -6.17902 | -57.78451 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 45d27090-4589-3e45-a44f-397610f28f61 | -4.15874 | -60.69287 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d5b0ad6-4a70-39d2-9692-5243aa12243d | -6.76533 | -63.05722 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57c3902b-cdb1-3985-8d78-5c1fa637f3ee | -6.71897 | -56.34221 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da7d526-f0b9-3ec6-8048-35b652600a61 | -4.29803 | -59.47353 | 2026-08-29 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bface39-ff96-3baa-8bb5-f67de937e9b5 | -6.7653 | -55.67337 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f821bbba-2e26-33bd-8958-cb75d39438ad | -7.52821 | -61.3682 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90976618-ac91-3566-a0da-74fed6b37766 | -6.81681 | -59.45029 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb4d2156-81a0-375d-b767-3ba9e6e57aea | -7.51153 | -55.29479 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02d9d8f8-e304-39a2-a19d-eaea3c7f44ab | -6.77568 | -55.67231 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d887eb1-7598-3aea-9d6c-78e7ad9db8b0 | -6.16495 | -57.79086 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d559016-f324-3f78-8c3a-8e1d928b4cd3 | -7.5155 | -55.3047 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 62788de2-550b-3bc3-8e97-20da93c59163 | -7.5288 | -61.36423 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
