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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8be46f3-911e-3cf3-b243-ef56249891d3 | -11.77466 | -47.39672 | 2025-08-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59563433-3320-3e79-9390-d3effeecae4b | -9.65755 | -43.8515 | 2025-08-09 05:04:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a9274aff-da87-3494-a8de-33ab79dea5a8 | -9.93484 | -60.50845 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf464338-e439-35d9-89b2-00a7830b74e9 | -7.0785 | -59.1611 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2b629c7-da7e-3d9e-ac7f-2a5bddc5ba55 | -7.07864 | -59.18239 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 46193856-bcbe-387f-a280-16fc4ac96b5f | -7.05882 | -59.18088 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| e9b80964-1a50-3c5f-8ce0-d46ba55cdf55 | -6.59308 | -43.40084 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b11fed78-b044-3901-80bd-8908df1b2590 | -8.86704 | -47.27296 | 2025-08-09 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b22cb503-f252-30ef-8027-fdc346aa7a56 | -7.05681 | -59.19328 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 41abc7b8-45e8-3f75-b2ff-601c341807ab | -7.10801 | -46.10404 | 2025-08-09 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 477845e5-1c95-344c-80d4-5ab1f3442865 | -6.6247 | -47.28689 | 2025-08-09 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4dc7282-b759-300d-8999-fd9a98d043d2 | -7.08874 | -59.18838 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 45b5a529-048f-3d09-b561-85553b4a6b05 | -6.58885 | -43.39827 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df972154-3e6f-34c7-996f-56a32187bedd | -11.19252 | -55.014 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaeec5e9-117c-3331-8455-6b3af3910506 | -7.08311 | -59.16782 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ce4486f9-25d1-3079-b304-8a58a1a3718f | -7.07657 | -59.16253 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8e1bda00-6b9e-3ec9-807e-58dbcaa18443 | -7.0775 | -59.1797 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d97deca8-5b0d-3dec-aa61-efa7d14379ee | -11.25298 | -50.1878 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deb07b01-d71b-3eca-8233-af77b4af268a | -7.24405 | -59.99715 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7880d029-583e-35dd-ad4e-48d6b64eded0 | -6.17128 | -58.06997 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5656b5c1-1f31-3752-8ffa-1c49c2b92b6e | -5.63148 | -57.32739 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0067a0b-a129-3e31-940c-22bd40e88d5c | -6.12889 | -42.96165 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 4643795b-9247-35f9-bd7f-88309c1326d7 | -12.68208 | -48.20201 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec8f3419-cbdf-3d72-a07e-330cf8a496af | -8.92508 | -60.73611 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77e66fa2-24ca-3b6b-988a-dd8178cf2233 | -8.92345 | -60.7457 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bf2d886a-c53a-3270-9e26-856cceb94431 | -7.07683 | -59.18385 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 118f2dea-fbe2-325f-b6ec-57ab89736f66 | -12.5868 | -47.17502 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ecdf2a8-1cf2-3677-b9c0-1d9a64644682 | -11.93895 | -44.54868 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85a8fae6-bbc6-382b-aca8-308e5c5daf0f | -6.34198 | -55.56282 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49ea2ef2-5f34-3fa1-b6ca-43c28028e544 | -6.66887 | -43.33933 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ddf6912c-7607-389f-8db1-fe84378632ea | -9.71069 | -61.29914 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd44050a-eec9-3f2e-8a4e-0ef5b3ae4a46 | -7.40484 | -47.13927 | 2025-08-09 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c300f58b-b93c-3b4d-aeb0-ce1bdcf1fb56 | -13.04235 | -43.84986 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8224f8c2-d2d5-3f2e-936a-a57cd6472d6e | -11.38236 | -54.35566 | 2025-08-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8407eba-2f6f-37f9-a841-eb54ebfb32b1 | -7.0021 | -59.66139 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dae7b89a-5d31-3200-95fe-a1f57f8bebd7 | -7.07323 | -59.18325 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 163360e2-2eb1-3202-bfb6-24b5297d040f | -8.91911 | -60.54426 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bc3a283-a1a0-3858-91b7-842074ddf675 | -7.63115 | -56.73656 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed2b8d27-a389-33fb-b7d9-92011e46cf1c | -6.09148 | -59.92697 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae5112fc-34cd-38e5-b8f7-f82272891ab8 | -9.93342 | -60.49432 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 670b06e4-5cfa-3ab4-979f-d880196dcc50 | -7.06376 | -59.17324 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 479428af-87c5-30fa-9642-a6716857f791 | -9.54675 | -62.71891 | 2025-08-09 05:04:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82998ab2-1da6-3f5a-b721-3e13e5787d43 | -11.32274 | -55.21762 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d7a56a-6b60-3c30-82ce-dce409a35578 | -7.39624 | -59.99508 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6e7b278-fcc2-32ad-bdde-f6feefc46a5e | -12.56538 | -47.11452 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4146797-8d37-37f9-938a-8ca613f0983e | -7.07655 | -59.19487 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3624a79c-9e49-3ad5-a184-f96773c7fed2 | -8.92589 | -60.73132 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d9c96fc-24b7-316f-9a87-c78d417d3c73 | -7.00303 | -59.66387 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08c448b0-d689-3400-956f-8c5bd10da249 | -7.07296 | -59.19424 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 55faaeeb-3717-3cad-b473-4c27b947e4dd | -8.93657 | -46.73715 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3629621-d49b-3a83-b431-cba47436d35c | -7.2497 | -44.32732 | 2025-08-09 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92ee785d-e7bf-365a-8f84-ec69bb2be5f7 | -7.07933 | -59.17825 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| bacf0751-e99f-3b27-8330-4517d462dbdb | -9.94238 | -60.48664 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931a176f-7cd6-36d4-9681-15828530c0be | -7.08514 | -59.18776 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| f595df97-7d1d-33d3-a2d1-f32310865b3c | -7.40897 | -60.01105 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f768863a-28c0-3ec3-9f1b-6a0277eb3a65 | -6.12025 | -42.96006 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e73f43e9-6f34-3333-b2cd-700874d632c3 | -11.32615 | -55.21814 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e63ccc54-b9c6-35d9-85de-b0c761793a6c | -9.2639 | -60.77783 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19403c34-9b82-3847-b4ef-48623b2b975b | -7.05116 | -59.20528 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 306badac-dd2f-3d8f-b2c5-7c5b5e4196b2 | -7.07725 | -59.1907 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c73ada92-3b23-322f-90af-c4a1f56254b3 | -8.92125 | -60.73546 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 398b8303-4338-3dd8-b787-f647b3616445 | -6.60382 | -43.38765 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c26f5965-0f5e-32eb-b371-7d1dbaa33835 | -7.05455 | -59.18439 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4cae15d0-d921-30bf-8c71-ab8f1b404ecc | -7.07616 | -59.188 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| fba84f14-ade4-37e9-8207-9b757146e906 | -11.08338 | -50.46262 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 931601e9-3c19-3e33-9205-329f63160e79 | -6.92984 | -60.06667 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a62829d8-5043-31e6-b2df-ed8d7c76dfea | -10.06245 | -59.6656 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec0a8f9-05bb-346f-afcd-012e8d63e9bd | -7.05815 | -59.18497 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ef251faf-157c-38f2-9c59-d34c9e8d7419 | -7.05905 | -59.20224 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5d0e24f2-a19e-3401-a00f-87181a0c6fbe | -8.90319 | -60.54636 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38dbd81b-128d-34a4-be5e-e563f95e119a | -7.06198 | -59.20703 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 534642ae-8a13-3ded-9759-9b7e1d3a1845 | -7.39548 | -59.99962 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8caaf6b-03ef-3913-8d24-ee10d7b5d021 | -10.06601 | -59.66621 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a24b74bd-39f0-3696-8588-ce478e696ba9 | -10.32503 | -58.72023 | 2025-08-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be64055-c93c-305a-8b16-eef0171de694 | -6.59459 | -43.38918 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c5547b86-4162-3518-9ea0-2a75cc46ff83 | -8.92264 | -60.7505 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c9bc7489-d615-3e85-8236-cc32c11a9264 | -12.55037 | -47.09539 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a05426b-98fc-3684-a981-2bb530ea338c | -8.92484 | -60.76073 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 170fb2e1-718d-3427-a863-901556f9a792 | -7.06083 | -59.16854 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a8e2fc0a-31f7-3fef-944a-138ff867aec4 | -6.25486 | -44.83092 | 2025-08-09 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7df0c6b7-bdb4-363a-ba99-0865953df800 | -7.08072 | -59.16994 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| dd077af1-3829-326b-a8c6-7c3568215bb4 | -9.02637 | -59.75508 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60fe261d-003c-373a-8c79-80bdde2419d4 | -11.73549 | -47.48838 | 2025-08-09 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3544e553-23ba-3699-93f7-77d84b33c879 | -7.06176 | -59.18557 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 571.5 |
| 11533bd1-642f-3bf9-b091-ea6dd09c09f2 | -7.06626 | -59.20346 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2487f04-6458-33c5-96f7-31b7f73bc9dc | -6.13568 | -42.96247 | 2025-08-09 05:04:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ea7be6be-2208-380f-a648-986e125cad49 | -5.88033 | -57.74716 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dcf0c68-261a-369c-bae6-819f3d89a579 | -7.0759 | -59.16667 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f37335a2-e24a-36ad-b994-0abca8849034 | -7.25231 | -59.9938 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06c10b55-73bb-3c96-8cce-0c5085470a53 | -7.05589 | -59.17619 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| bfaab4dd-2dd3-36a2-b237-5c35e2b3322f | -13.06548 | -43.8319 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3360f38e-12f1-3c1d-a21a-d9d703665c1a | -7.05388 | -59.18852 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04372f80-cdb8-3355-ba37-926736570a86 | -8.6138 | -60.60276 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7085feb-b83c-38c1-8905-52811942a3ef | -7.07795 | -59.18653 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 6af791bb-6802-306b-ad59-983b28045a9e | -9.52082 | -45.4097 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7718138-2edb-361d-b79a-a8aee40211e1 | -7.06334 | -59.19865 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 89a1d03b-ca13-3c86-8f34-7a9e5fa9f8a5 | -7.40674 | -60.00135 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ce3dd9c-b62f-3d24-aca1-89d93332d889 | -9.65821 | -43.84605 | 2025-08-09 05:04:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b8d4c313-e88d-3f6a-ad3f-dea4a9b764a6 | -8.93645 | -46.73542 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 234d2b30-608f-304f-967e-4fc3eaffab1e | -13.07132 | -43.83377 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
