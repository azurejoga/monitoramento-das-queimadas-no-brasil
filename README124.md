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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a026b63-d5e8-3f2b-a426-90771c0752f8 | -7.83995 | -47.06849 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95b13025-e83e-3d3f-a35e-cbd07a881ec3 | -10.08455 | -50.19761 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e780336-9271-3d4d-9b7a-c31e4b80ac18 | -11.80658 | -46.6268 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8a1f7b5b-94ab-3567-8fc0-7cfcfd722804 | -8.92651 | -47.58071 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab77eef9-efeb-3995-952e-1c732d43450e | -12.70378 | -46.8966 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 362f60f9-1921-3152-bb2a-c891d53da314 | -11.60676 | -45.05466 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4f1686c-7e1b-3761-8351-fff0d67febd2 | -12.82833 | -47.01406 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61c44b7e-dd8e-39a5-bca7-1d3f750a0c65 | -11.4673 | -44.99119 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f259b11-030b-39b3-89ea-0705fa17d566 | -11.83444 | -44.95849 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55fba465-5186-3495-82a0-e3f32593923f | -12.42979 | -50.17865 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e1cbf57-0243-3b22-940a-a50c9edc530e | -11.14761 | -54.30922 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d2d9b6a-339f-3d7b-bba9-55594399af93 | -5.51721 | -52.08541 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79acd2ef-f4c5-3711-af0a-b04c7dc8dc07 | -8.17053 | -55.1673 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a06da851-6df7-3c5b-88c6-3cd7f53b110d | -10.60533 | -49.63914 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc0c76d0-4721-3c22-9820-9e4d3c411421 | -12.44425 | -50.18661 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3c5972d-ae83-3571-97f1-873604189978 | -13.33939 | -47.33558 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6355b2af-90bc-3762-8683-850c4d269bc7 | -12.69118 | -48.56248 | 2025-10-01 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5f8b2cb-c96c-3ac3-99db-0b4062fa0fbd | -11.79405 | -47.59729 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1d93636-d90a-36b1-bc8b-e7f82d796b84 | -10.84332 | -45.41222 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 288b67d7-6f5a-360c-a5f2-e0a02988bbc4 | -10.63131 | -48.59343 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e4f341-7499-3348-b587-e3450bb6a1b5 | -10.57013 | -57.81363 | 2025-10-01 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d55d1b-2d02-3657-ae64-24608c61d33b | -12.82164 | -47.01714 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c4e6801-8512-38e1-ad8e-e1fb4a822228 | -13.33016 | -47.84702 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 014a4cc4-35c1-3916-935f-fc4fe12e13e8 | -7.83034 | -48.19815 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c82cbbd2-4b28-37f7-9e69-bab73129512e | -13.31385 | -47.22602 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a8a642d-ec79-3f35-b137-775df4f6a398 | -13.32775 | -47.8676 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a070dd58-f20c-378c-8f2f-ade519a0131f | -12.82383 | -47.01515 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb5c8031-93dd-3c73-8123-434b02419101 | -11.85503 | -45.01646 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c34a9b4d-5224-30a6-bcc5-889830abab5d | -11.76695 | -46.84944 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba150b66-3dba-3752-9c51-e2fd4172624c | -11.7945 | -46.62047 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ee0e3d2-4cde-3ea4-9296-d57dcf090427 | -11.62507 | -52.24391 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b217a892-9186-392d-9738-31ef297a07ed | -7.87185 | -47.27302 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c87f63db-1071-357f-99c4-35507ca7779b | -12.87787 | -46.91292 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5504b4e-5015-34a5-bc38-0695758f61d9 | -11.67187 | -46.96036 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0fbc3dca-6d9e-3fcb-9df6-a4f0ad66d358 | -12.83054 | -47.01202 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3786071d-0c75-3840-8d60-c3495afbe123 | -12.90722 | -46.8238 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 821b1f16-e36f-3bdb-a9cb-d4f14dd3095c | -13.23053 | -48.44365 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2065980c-a583-3dec-8ddb-cc33a219feda | -11.4702 | -45.08434 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 151a182a-34b9-34e2-b324-39420a684ab8 | -11.62448 | -52.24814 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 214b43df-36f3-3c97-a0a6-cfe63fa2186e | -8.57768 | -44.76017 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33f44c6f-89c1-342f-acf2-3f9eb0a0872d | -11.5684 | -50.19071 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33accdec-936a-35eb-91cd-fff6f7918cb6 | -10.64403 | -48.53668 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 753d46d3-d2b7-3c86-9d54-b16879ab1ed3 | -13.53894 | -47.27158 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d695038-4fb8-3da1-a79a-3bc25e0a0a50 | -12.85234 | -47.02606 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 579a6008-d52e-3d6b-af88-b5f0c465bd3c | -10.92797 | -54.33362 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b9b1e2f-ca1a-349a-b011-24f30675954c | -8.92701 | -47.57682 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fde547c-06c5-3b5e-a4cb-de1920689c24 | -10.80871 | -45.35717 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9efc33c0-1207-3358-a368-3a8ea04c603b | -13.36942 | -48.1126 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ee4126f-d84e-379d-8e30-44a473bccf9f | -12.4307 | -50.18042 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f442a5-45bd-371f-8592-f4e4728e6fd1 | -11.7996 | -46.63142 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 023c9c90-eb66-34bf-a0ee-fb7645a46c80 | -12.21541 | -47.80098 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bc84537-c2f1-3a01-8eeb-ccef2d0a7e69 | -12.83245 | -47.03391 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f83359c8-594e-3e7b-8bd9-a9939bb02f01 | -11.20086 | -47.76097 | 2025-10-01 05:10:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10638f73-26d0-339e-a819-fd1b0b03a5f4 | -13.30914 | -47.21149 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7824e16-2dbe-30af-b113-9b6abe6f9841 | -11.73886 | -46.87271 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da918d4d-6abc-3587-8575-371b198aae17 | -7.47535 | -46.46523 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b36000a-3c91-33ba-bd10-9ac8b73dcff7 | -12.83823 | -47.03883 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f24dd531-43f2-33c1-9874-508998486967 | -6.72413 | -50.9496 | 2025-10-01 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23b41ab5-b656-3dee-9f16-92bd5752207f | -11.19495 | -47.76075 | 2025-10-01 05:10:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1b89990-9bbd-3333-81b4-123116feec94 | -10.23803 | -52.69413 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5bc31fd-78cf-3899-bead-e0ca3bc359ba | -10.43978 | -50.86796 | 2025-10-01 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5eeff47a-d7c8-3d93-9f93-7d8ca86a0c90 | -8.26036 | -54.95782 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf2e7de0-c631-3681-bb4f-76f6dea8192f | -11.83721 | -48.06086 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebbb6b46-f877-3e7a-9a8d-a3d94927553d | -8.16288 | -46.26423 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c322c18-53a3-30cf-a994-bde548c71afa | -8.55634 | -44.76498 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2df30079-97e5-3ae7-9656-dabdf5b88427 | -11.79843 | -46.61311 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2649e388-5a63-3c3b-94b4-bfb867f1c31e | -11.09318 | -47.72605 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87308dde-19ec-3e6b-894c-02e713dfb3c1 | -9.81156 | -47.86325 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b10a6597-f835-37ee-a124-2ddc51a00b73 | -12.78162 | -46.88536 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5834643e-3f53-3a44-a72f-5a89cc3ef1ea | -10.8269 | -45.37738 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20a96c2c-03e7-3a2f-8112-dba3c80763cf | -12.77531 | -46.88461 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d90099a2-8b11-3cd7-84ac-513f4e0dd5ff | -7.83929 | -47.25274 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db59312d-b5ba-360a-ac2e-79c05de9dc5a | -5.61464 | -52.15704 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 867b91cf-94fe-3236-b27b-9c701d21f709 | -10.06623 | -50.26194 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5624f1be-37b5-3064-91e5-9f38e9affa93 | -13.27731 | -47.22846 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6de14d76-cacf-322d-9e6d-0d3a9204d9cc | -11.17128 | -54.11504 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f88e2c6-493b-38a9-ba5c-05c714e9c27a | -12.17354 | -51.41916 | 2025-10-01 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 884a48f1-672e-334a-83e6-de493c46f1b9 | -10.06677 | -50.27097 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fd11b01d-9688-318c-9412-2f68d73d1f91 | -7.15812 | -50.54497 | 2025-10-01 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4120ee2b-b0cf-33dc-b1b9-110439c84f68 | -11.051 | -47.82835 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c399d97-f4ce-3691-ad12-944fec054ec2 | -9.43382 | -54.71022 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5be0af80-44b2-313d-bc37-200d7fb5c18a | -9.42545 | -54.71012 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbf42c38-7f00-3683-bc23-d756d3837a97 | -11.15843 | -54.12297 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d424337d-8838-39c6-96d4-41657c5229c0 | -8.89486 | -46.63845 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42962fc9-b135-38a6-bfef-e6e9633244d2 | -11.81684 | -44.98963 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16ed3675-64a4-39bd-a505-90f8b0ae8e1c | -11.85023 | -45.00687 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3ad56e3-809d-381c-a478-c2f8636204a9 | -10.06751 | -50.26555 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 32c5ce0c-bec9-3882-8a4e-5ec268a4b6a8 | -12.96075 | -48.43733 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99258f2c-f068-35cd-bcb8-0bf19dcd8b44 | -6.04005 | -51.89433 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd097ef2-ec6d-350c-853f-3275893f5e9f | -11.18926 | -47.20351 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0c9c661-2dff-38ac-987b-ed67f639b5ad | -7.4724 | -46.47658 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a832b9-b0c4-3a0e-8684-10a9966b8d59 | -11.60733 | -45.04962 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd49f649-5bde-3475-bedf-d09b2097f1e4 | -12.97985 | -48.42297 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbeca3be-726d-371f-9623-ab92b9b8e58f | -13.30066 | -48.70259 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7860023-f02d-3777-91a9-819ea8cf152c | -10.84635 | -48.0015 | 2025-10-01 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 163112b5-79dc-3c50-8ce4-0a7034702eb8 | -13.36915 | -47.29375 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b3a40f6-45cc-3575-9a49-f5f690ef12b8 | -7.05547 | -46.41457 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be34b374-9d2e-3ff5-b700-e5ec6b4caa5e | -7.82291 | -47.06223 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fa8f409-9127-37fd-8efe-a6f9dde34054 | -12.84763 | -46.955 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b68d916-f6bb-3ad3-88c4-29adcf89ef34 | -8.55551 | -44.71541 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README125.md)
