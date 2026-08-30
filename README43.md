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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7321e61-fcbb-3fdb-992c-37b0315eb12b | -11.27309 | -45.33533 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ad8ebe1-c2bc-39ee-b8fe-1aee7fbf00ff | -11.22326 | -45.08854 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0198d41-fb34-370e-928b-a6093869eb3a | -14.14742 | -52.81273 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e429ed3b-b7e0-3ffd-a48c-5b1fd2b4fa23 | -14.19287 | -52.87271 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2c0205a1-7893-3661-a1ac-fa91f7a54b69 | -10.14343 | -45.69696 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6311a6e-1b61-3999-b25e-2036b9359390 | -11.24658 | -53.99068 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65184405-8685-3568-a153-10a9280c7d14 | -14.25079 | -54.65361 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d57a3f27-583f-39b1-8a62-ae07615bdecb | -10.76709 | -44.88082 | 2026-08-30 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecca38f4-efac-3bf8-89d2-49144eed87b9 | -8.55306 | -54.71569 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 931c9218-aea4-347b-9665-ae3abd11f765 | -10.74855 | -54.03977 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bf51d4e-699b-3bd7-8576-6475c704785d | -8.49635 | -55.30552 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb75c157-756d-3f04-8dc6-b071321e8e3c | -10.75218 | -54.04496 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61c369bb-9467-39b3-9cf2-ca729d6ea3c0 | -7.23541 | -60.62621 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95e8b8cb-de89-33bd-aadf-b1a6d2b43ca8 | -9.88823 | -60.27423 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1eceed1c-4e3b-3e84-89bd-9fc83817e94d | -11.26851 | -45.31871 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d5ead2cd-f353-3dda-8e41-e6f24b11bbf4 | -11.34802 | -45.15411 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 276b1171-e0e9-322e-b036-ad22eb3961b4 | -9.89491 | -60.27559 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 788415da-e84d-32c9-817e-627a5f946601 | -11.51522 | -45.53516 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c51cb0b5-c2df-3154-8630-38ed117673f5 | -11.80907 | -51.04753 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 43b45d74-d733-37d0-919c-431386089d1f | -11.80544 | -51.04689 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 51f87058-cf81-31ff-8f6e-2b97dec0bf11 | -11.35151 | -45.15463 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6183571-c346-360b-8738-938bfa596b7c | -12.89507 | -45.87379 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 276231cd-1f1b-3f95-b88b-c85e73f178c6 | -9.06901 | -60.48859 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cc88d5a-fd47-364b-b537-4d9c92584c51 | -9.7066 | -60.72457 | 2026-08-30 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c15da685-7fe9-30bd-b4bd-6585a3984eb0 | -11.23732 | -45.09819 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 210d95f5-5d5e-32fe-a792-15f8aced5ac9 | -10.94836 | -43.02986 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 2e4a4f1d-3bdb-37a2-8862-8a4f2f079c0f | -8.50245 | -55.30045 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74318eae-8a30-3057-a1e3-7c9376b5000b | -9.16553 | -59.51085 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07a02a33-8dbc-31ca-86a9-1f45717c7f37 | -9.72086 | -54.82477 | 2026-08-30 04:34:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c35db9e1-9e84-30b5-b662-28a42a8fc8df | -9.06769 | -60.49511 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a3ff637-d528-3401-8ebe-1264544949f7 | -14.75235 | -48.74015 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 080c11a8-60a0-32f1-8373-960033d5875d | -7.23405 | -60.63338 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94a6407f-04ba-34aa-adfc-acd9e3f2abe9 | -10.34442 | -49.97758 | 2026-08-30 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0711379-ce0a-3550-9b53-f73a6c360216 | -11.62887 | -54.59486 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe6bbaf-c668-329f-becf-c2d17364c03e | -9.76207 | -48.16382 | 2026-08-30 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4d61545e-c4ec-3623-8f63-89997a41b0cb | -8.499 | -55.29092 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d91edb-513d-3355-ad07-febcc98d489a | -14.25352 | -54.66306 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 684eb11e-56fc-34c8-896d-fdf220f3123c | -11.3416 | -45.14926 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5c845db-f189-36a9-8bf6-266060894118 | -11.02629 | -57.2425 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d3d1c7e-1c44-3493-951f-c07c098be23c | -11.21046 | -45.07854 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce290133-51b9-3292-893f-b275eac72b3b | -14.39662 | -52.57036 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bef3d8b8-a38c-3bef-8631-1a8e933a7285 | -11.36025 | -45.16792 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 497e7c82-1348-3b7c-9dc6-3aed8fda2952 | -11.78948 | -51.05291 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3578e3d1-6a0e-3926-b67f-fe6fe18f58ac | -15.36144 | -52.67912 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e38a85a6-1eda-3103-ace7-ea657dec0c1f | -11.163 | -51.31796 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22043aa6-9c49-38a5-8203-f1c8ccef5190 | -16.34659 | -50.98066 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b99f52-9526-31fd-8344-debb9ad71898 | -11.20814 | -45.07019 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7083124c-73e6-375a-bbc0-9682d65e66fe | -10.73909 | -54.04922 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc756e70-1be5-38a6-bf28-ae5582c54215 | -13.39373 | -51.76648 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2de178d-06a6-3608-ab2d-58a796a2cd7b | -14.44648 | -46.23051 | 2026-08-30 04:34:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 213002eb-c01c-39d3-8e1f-b39eb44fc46d | -9.069 | -60.48869 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21308e7e-12ec-38f0-8cc6-ee94927be9ce | -10.73808 | -54.04693 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8a005fd-ff87-3359-a048-e3197d0082f3 | -11.79819 | -51.04561 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 39a6e00c-0e54-33e3-bc94-6f04c8c65438 | -12.92948 | -45.87914 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6bc8771-e9b9-3ac0-8146-d1f30f38fcb9 | -8.60798 | -54.76988 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78e5e04c-e8c3-378e-9666-91b17636cc96 | -15.12743 | -50.6315 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52af6132-4bc9-3493-a372-73930bb677f6 | -10.93995 | -51.41787 | 2026-08-30 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68d09ec9-d1f0-335a-bcb5-25d87ff2c5d6 | -15.36229 | -52.67439 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aee0e95-27e0-39a4-af38-85015ae4c01f | -10.73543 | -54.04401 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b1447c22-304b-33db-9cce-eb33217491c3 | -10.06594 | -48.69867 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4ab2471-37fe-324b-abe5-66815bee2c4d | -9.197 | -51.55526 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419e2bf1-e4d3-378d-aa10-143f2f1f81b3 | -7.30771 | -60.61333 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a59cb182-537a-32f3-938f-5bb7466a36b5 | -9.93805 | -60.53003 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02b0ad5f-e63e-3ff0-8286-aac5022fcb1d | -15.40758 | -52.68269 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a16b82a-58d6-300d-8b94-e967289594ab | -11.26237 | -45.07389 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dcd1600-09f1-3799-a80c-5bfaa3f7a2ee | -12.93235 | -45.8835 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa18287-3495-3a85-8f67-bac88f633bdd | -8.55482 | -54.78791 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fde8415c-427d-3da1-baee-cb4bddc9bc7a | -10.78719 | -45.32954 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c72f3c-0f27-3257-9c6a-1ed6fdcf0d46 | -10.75153 | -50.86972 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8c7eed4-13cd-3f36-8f0b-cde941160606 | -11.23786 | -53.98888 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b26b63f-4300-3c38-aa7e-e9900ed6c434 | -9.10092 | -50.60566 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6a9712b-6f87-3022-a4ca-5a51e127993e | -10.81306 | -45.3218 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fac55b1a-d6c3-30ce-ae13-9a07a24088b9 | -10.80961 | -45.32127 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1799658-495d-326b-9ebf-8fa0166b18ee | -14.75898 | -48.74124 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53b52638-3bae-31ac-a760-3f4329186540 | -10.81969 | -50.49399 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9882057-22fe-35d9-a7ab-132e261ddfd0 | -11.04067 | -57.2296 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98211784-25f6-3383-8894-07e4c1fa0663 | -16.3494 | -50.98508 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cbae68d-195b-3e1e-b6bb-90ce1c055ef0 | -11.44281 | -61.48939 | 2026-08-30 04:34:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 83aab17f-d402-35aa-b23b-6f2942059717 | -16.33766 | -43.44007 | 2026-08-30 04:34:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9a5bb63-d91b-3d05-b8ef-733bbb764384 | -11.19282 | -55.10629 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed20d4b-da33-3ba7-9aca-29ea6b23c0b4 | -9.93501 | -60.5166 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0e4707f4-1bff-3cf9-98c2-b5fddb971f40 | -11.1875 | -55.10353 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8907b7d9-635a-3a47-9a7a-54b524c9f303 | -10.48243 | -59.60833 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea4ec539-d211-363e-9685-03e17127fe6d | -11.23604 | -45.09861 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53dc6fed-2989-32cc-9568-6fd344ccad9e | -12.77878 | -46.46122 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c9c07ee-5691-38f1-8fc1-d9bd0fd803f3 | -12.90884 | -45.87588 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d5eaca-f038-3b51-b3d4-bd69aee445a5 | -11.8134 | -51.04701 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f8a42e1b-d2a1-39a4-8574-e8e1ca5dbde6 | -9.66286 | -50.84951 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142ec0c4-1285-3893-8b67-8e8cec35fd64 | -12.07995 | -47.19152 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dd0b53f-336d-3a88-a315-d25c50a17180 | -11.49865 | -50.27541 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a3087be-cc69-3fd6-a79c-75d0a9a37501 | -11.53476 | -45.49887 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 70e6f1dc-9f8d-3baa-a28c-5f3713eac226 | -14.20817 | -52.85739 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebe50fea-61cc-3f6e-8810-5dad23d26ec1 | -17.27926 | -46.01118 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78e63705-763a-3a94-817e-99d3e7f0efb8 | -8.50403 | -55.2917 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca172fb3-d4a3-3531-85d6-ab5d0a7db0e7 | -10.81039 | -50.51463 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27e2866b-4f07-3eec-b54c-3e41a7fac9e1 | -14.16293 | -52.81549 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95a6375c-2f3b-33c4-af19-2259ada02cdf | -10.94073 | -51.41329 | 2026-08-30 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc5f253f-8c1d-3eac-8787-6f7113f5d651 | -7.39733 | -60.58637 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b5190780-1531-3b7d-ad3d-5168c538222d | -11.03523 | -57.22854 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d8d344-2ad8-3d41-91ff-c766cd67e38f | -11.02354 | -51.40687 | 2026-08-30 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README44.md)
