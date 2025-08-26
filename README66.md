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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8a3f8a-b412-3681-8747-ea740d73c57b | -14.33053 | -48.64938 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7cda5fe-8efd-3222-8655-668b74187435 | -13.44723 | -46.86309 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d0dc95-ca85-34e1-a06c-6cb7aaa0290a | -10.39498 | -57.6976 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4955734a-889a-3fe8-9761-a092e9b5db99 | -8.99974 | -65.41366 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfe29c32-d72b-322e-ac96-84f27308b7ec | -9.18821 | -59.50904 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdd77714-9c46-3b19-90db-fc29ae679845 | -9.40132 | -48.24451 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a2a0457-7fd6-30ed-b0cd-728573b112f2 | -15.49079 | -47.88667 | 2025-08-26 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a570003d-73f1-395e-9626-1cdf3ff2c307 | -13.35311 | -54.39663 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f01bedfc-988a-372e-acb6-8610adae0a83 | -12.77209 | -48.12609 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1345df68-4e42-316d-b61e-dd8e628b10dd | -8.57166 | -62.63868 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ea81d55-01cf-381d-8a34-1584ccb292a9 | -11.50123 | -52.13589 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c15c831a-44be-3285-bd71-00b0aff52989 | -8.85881 | -62.44732 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 47e34a06-621e-3865-9ad1-900e8c7cf80f | -10.61238 | -54.89533 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed2c3dfd-a484-3e01-974f-0581a3d3aae1 | -9.16925 | -59.45469 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02a9c162-9c6e-3bba-a7e6-01b1545db648 | -8.53761 | -62.65522 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5daa254e-3dfc-3e3d-b711-a52a514c4d16 | -7.47221 | -61.33315 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f99f04bf-521a-3e52-89b4-883568a6f0ac | -9.17836 | -60.79862 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| effbc732-4fdb-3fe4-ae4a-80dffbecb1fe | -15.02832 | -48.51329 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65d662ae-044f-378f-8844-41c2650c9b66 | -7.88104 | -63.01775 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4482dfb7-1e79-3fff-8b34-4150e5b9d582 | -8.98045 | -65.43787 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c09f41c3-1239-3767-adfd-b527fa14ce3e | -10.54001 | -46.80983 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 25418fe5-eab3-32ad-8f98-a259f663ff4a | -9.04368 | -65.73324 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 652ed5ef-f55c-3bcd-863f-e551058a6f18 | -11.14715 | -44.77168 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fa1dc73d-18fe-3401-9848-5651ea517086 | -9.405 | -48.2451 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73773722-e5fb-347d-82bf-6268f866c2bf | -10.53038 | -46.78984 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 634b16f3-182b-3afd-b33a-d157c90a301f | -14.84622 | -47.15031 | 2025-08-26 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c9dc2b35-71fe-3e6e-8da0-eb371f137a81 | -14.59402 | -52.02013 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb2a16fa-21e4-314b-802d-74c6c9f18767 | -11.54538 | -52.13583 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cfb77f6-4c35-34e8-a849-a865fc8a8b72 | -9.17664 | -59.51789 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88c4cdc2-ecc7-3bfe-9257-346316717682 | -13.05579 | -46.31578 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4f6ed3a-0bd6-359d-9ba8-1068fed1ed0c | -11.51778 | -52.13857 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 19183ee7-2a06-39cb-8e88-16f27f9045c0 | -8.3297 | -50.57508 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed34a8eb-b1fa-37cb-a397-09e836bea9df | -9.31312 | -63.43968 | 2025-08-26 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e030bed-1512-3184-8b40-45801aa27171 | -8.87366 | -62.45483 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d09627a0-b96c-382a-a6ee-5c1356aec678 | -8.90469 | -45.72176 | 2025-08-26 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d695bc8-c7a0-3fa2-bc81-f91eaf1cb9af | -9.16011 | -59.55363 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f7ad7521-a423-3b3a-90e7-e7ed188f06a7 | -9.80164 | -64.25657 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49558375-0aa6-3043-bca0-8932c0c97237 | -11.56469 | -52.09935 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92ba207c-6195-399e-be3b-5bf41d810c34 | -8.83537 | -62.44253 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29ba2cdd-e0ff-3223-aae2-67915a20d6d0 | -11.53323 | -52.12667 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| aeea0650-41e9-38d1-8051-4b6e5781765d | -13.44041 | -47.01413 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca189ad9-5c57-3f02-9648-8cdeb16e9c7a | -7.62072 | -61.04686 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94f08887-17c6-3ac9-9e66-297a6ed277ec | -9.16038 | -60.77846 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 816f37d1-4d55-34e6-9e83-46d484fe508a | -6.75374 | -62.86981 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2dc9e34-7afc-37d5-ac09-c3cac9a99c8d | -14.42178 | -56.44734 | 2025-08-26 04:46:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c28b29-bd31-3b0c-94ad-c6dd6cb391d1 | -13.64467 | -45.70854 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eaf7391-c948-3263-ab5f-46749a6a0149 | -11.1587 | -44.75746 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| ecb6f99b-f237-339e-84bf-d9db236bebff | -11.5531 | -52.12988 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca76ce6c-1158-3db2-ad0d-ed146489b8f1 | -9.15527 | -59.56246 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 168b9462-ebcb-3e50-96d3-a030749268a8 | -11.40174 | -47.60379 | 2025-08-26 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0883b3b-8767-3afd-99f3-96099c86a2e9 | -7.47646 | -61.34166 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a8b9bbd-bedd-3f97-b9da-dd082f63fc12 | -8.90221 | -62.46486 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f19937b-40f3-300d-80fa-40e5f0ba89bd | -8.57844 | -62.63546 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6584e76-303b-3678-8773-30b3d92c19da | -11.50509 | -52.13292 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3e85b93f-898c-3e3a-a41c-1250fea5ae86 | -9.04687 | -49.55618 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0924a9be-8447-3429-b068-45e2f3ac287f | -12.74814 | -48.09115 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e30988-a582-3afc-80c1-2704a71b195f | -15.08426 | -48.54407 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4e63151-a04c-3ee1-8158-751569c6f87a | -12.74665 | -48.15634 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0937ea2e-d4a1-3bf7-acbc-b0e0ef9a3b0a | -13.41537 | -46.9075 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e27c815-37d1-3421-9cf9-87c0fb831fcd | -15.06282 | -48.70231 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d5c907c-9dd3-32ad-80b1-83e8768e4bc0 | -7.47789 | -61.36567 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75dc934a-3d27-3072-9190-3b92d2c84a5d | -11.5425 | -51.91578 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24506f1e-fb70-3328-b70e-d51de0d81461 | -9.16765 | -59.52039 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b950cb5-346c-3546-81db-8fe0c9a9a40c | -12.73969 | -48.09493 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3d36174-d701-3e5a-9cfd-4df4b5d5e78c | -11.552 | -52.1369 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ec28dc0-74e1-35f7-b50d-5dc47b9ccf84 | -8.8668 | -62.42693 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb94b9df-5590-3120-b9ae-9a2fbc90288d | -10.5442 | -46.78058 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81b19e91-2aa6-39ef-8d56-edff79b35e92 | -9.1825 | -59.45861 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 10fa5415-0d7a-3e03-8e27-ef946bb47c8e | -6.76735 | -59.67288 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c31c58c9-3610-3a49-ba1f-18a353daea99 | -12.38848 | -45.00867 | 2025-08-26 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78b896ad-4ffb-38b7-bf84-0852b4027d52 | -9.1807 | -59.44592 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64dfd02e-65c9-32b4-b4b3-3e0070aa58a8 | -9.61756 | -55.35851 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd110ff0-601f-3527-820c-284e677a6917 | -14.39995 | -51.93718 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a61e06-41d8-332a-8823-b893f67b949c | -12.75523 | -48.13393 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23df7020-7627-306c-af23-bc89bf7317be | -8.60744 | -62.64583 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebcc1a3b-0ea8-36ea-be52-7ebc6bf578ee | -14.5271 | -53.10448 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 181d0505-2698-3b05-8ef1-0415ee87f8b6 | -10.8588 | -47.34416 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3b84eea-7fda-3577-8136-2be7bcaef23c | -11.56248 | -52.1134 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55ac8e01-d067-3c18-b7ac-69e554b5763d | -12.44104 | -48.71843 | 2025-08-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58e6afaf-b2a9-3cb7-8e53-d07658c2438b | -11.1594 | -44.75231 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 794d8980-6757-3ddd-b7eb-ed79a68e806f | -11.55476 | -52.11935 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc5b8ca2-4f01-3912-92e5-f8510c527ca1 | -10.86671 | -47.34528 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f19fbc66-110c-3f06-9d19-8cab54a82fe0 | -9.23012 | -60.92577 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de25039-0f49-3b71-acbb-a0314be74d81 | -11.51226 | -52.13048 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e232aa4d-c41c-312b-aaf7-98f50ecd8c4e | -9.17858 | -59.50723 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65ae060e-f680-3fe6-ac02-5fdd3cd10c71 | -10.41358 | -64.38702 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0425af9b-499f-387e-b8aa-31cdc4c51ad6 | -14.47586 | -51.94943 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 204cb4df-102a-35a1-9f61-c03265751b8a | -10.64259 | -51.5922 | 2025-08-26 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ecb817d-7120-3b24-95b5-d3fe46d39e41 | -10.59597 | -54.88428 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b54cfeaf-ac81-3613-92dc-fcae03db39d6 | -12.72663 | -48.15863 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46ef358b-b113-33a6-b2f1-2754717abdd7 | -11.552 | -52.11531 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd446694-7bc0-3e83-b6c0-5b77a2b0950c | -8.85295 | -62.44614 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fe6123ed-8324-3f5f-b792-508fa02f1e21 | -14.64141 | -49.07317 | 2025-08-26 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7cea55a4-0f0a-333a-ae3d-ccfcaf7b4337 | -9.07336 | -62.66676 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a256d0b6-a777-3012-a1a3-1b8b13dcce34 | -6.87709 | -59.90157 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2f80698-f4b5-384c-bb92-73b11a6f4c2a | -9.56059 | -48.78563 | 2025-08-26 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908fa526-0bae-3c84-983d-3e3d9afcf809 | -7.37944 | -64.35941 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a18fba22-19ef-332d-b85e-0f50d97f65fc | -11.55145 | -52.14041 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f96836a5-cddb-33d9-96ea-bf3ae075c592 | -12.4981 | -53.8297 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d533a39d-8fd3-37a9-a9fd-066a13f287b2 | -7.48 | -61.35406 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README67.md)
