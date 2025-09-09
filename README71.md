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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5fd132-e585-3b4a-b0f4-3aec1848c61b | -22.8387 | -52.6532 | 2025-09-09 06:10:00 | GOES-19 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 38fb2cfc-0dab-3602-a903-bf53792a7191 | -12.1988 | -53.9024 | 2025-09-09 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 58afdc28-b1ab-34cd-9501-3ceb832b20f5 | -12.1991 | -53.8817 | 2025-09-09 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8a427f8d-0795-32df-a323-3f06df92472f | -21.4762 | -48.8406 | 2025-09-09 06:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 78de56a9-56e6-320d-915f-e7e7c8c0fcb8 | -17.2757 | -46.7538 | 2025-09-09 06:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f57ba4cc-f0df-3821-bc08-194819f0f74f | -9.4739 | -60.48169 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ceccd90-8a27-3e41-bb16-73e2262e6ae3 | -9.16946 | -60.79916 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e995cb4a-0b46-3b2f-8c1e-9ed2f147a1eb | -8.77042 | -61.44601 | 2025-09-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb302327-83cb-3102-ab5a-e4e46ae5447c | -9.6968 | -64.19072 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1310837c-8a17-3775-be9d-dcdb6d890665 | -9.37307 | -65.93817 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69bc3e23-bb9d-3d5b-9c12-6cb6a805ac6d | -8.74647 | -71.03134 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d631de5e-8e3e-3bfd-be6d-51baa45889aa | -8.61878 | -70.98878 | 2025-09-09 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36558ae5-ad9e-3ebb-afdc-67ab4312b92d | -9.13265 | -65.95472 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79c2be1c-0772-3409-b5ca-4b56ab9943a0 | -8.24487 | -70.15257 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd4ab391-4913-34b6-9745-a6a50da36f81 | -9.22213 | -60.82541 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 69fe450b-ac53-3a23-8f08-d523c36b0810 | -9.13758 | -65.95543 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 784d2a66-71cf-30ff-834d-19f34bb4e928 | -9.45588 | -60.5135 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e9c2204-c88a-3c18-956d-e38dfb570bd4 | -9.0814 | -65.41338 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45c9ff14-98e5-3119-b4ec-d29e8930ce6d | -9.08692 | -65.41106 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c94bf209-9b3d-3da6-af15-a90193fb8b33 | -8.44917 | -70.13341 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8510ace1-10fa-3aee-bb92-84b6bee798d7 | -9.12454 | -65.96349 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae2412e5-8959-3bc7-bbfa-cd6985574d61 | -8.75002 | -71.03189 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56d91f14-40a4-3ce0-902a-2175895af39e | -9.39355 | -65.94659 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 247c6e1f-529f-3d8b-bfad-ac672b8639fe | -9.34519 | -65.45491 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b80e6c4-5909-356f-81c5-420a0ad5dab3 | -7.82926 | -63.57618 | 2025-09-09 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75e3f16-cc8d-36db-bd7c-48d60855c54b | -9.13518 | -65.95916 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8e26728-b759-3c57-900b-57c09b816b08 | -9.34638 | -65.44576 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| daf989f3-c80c-33e9-b5a8-1b8ba646bdcf | -9.47932 | -60.49598 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc577003-188b-3c4c-88b3-d1cf665cb183 | -9.22291 | -60.81899 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bab1526a-8e48-34ed-b172-f6b7a2a7c38c | -9.2402 | -66.10654 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f606206-c955-3545-aee4-a3c15489ba73 | -9.13442 | -65.96471 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ba136cf-ed88-3743-8997-4a7fcbae7839 | -9.26078 | -67.60898 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a2e945-6ed0-3fb2-9ee3-f81c7e3327a5 | -7.87871 | -61.32797 | 2025-09-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5cecf37-a932-337a-a086-c98a98b667b8 | -9.3448 | -65.45795 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7349b441-23c5-3042-97dc-dd3843c40a53 | -9.47151 | -60.50178 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69554288-945f-392e-88ff-79ec323f5765 | -8.7694 | -61.44279 | 2025-09-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13a88c2c-eedc-3a57-afb4-f3604a1b9d81 | -8.88042 | -64.03349 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f90a9e3b-f6a8-350e-ad31-ce814820c4d6 | -9.34126 | -65.44498 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08a42596-4e25-38a6-a619-be039703a5af | -9.21603 | -60.8182 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e8ce76a7-c375-39ec-b0e6-31e13026b7aa | -9.13179 | -65.94716 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fd9f3ec-2e12-3d7c-9b41-f4cf65c41b55 | -9.08386 | -65.39498 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40512686-004b-38b9-9a28-e799f2899594 | -9.08633 | -65.37654 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3ec9e606-e355-3d2c-87a4-2af222c42517 | -9.13101 | -65.95287 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc098ea0-f8e8-3549-90f2-201d6e352723 | -9.20515 | -67.55769 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a812baa-11e3-3ab7-a6f0-ea3dc2af2de6 | -9.05806 | -62.34795 | 2025-09-09 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f756c0b4-8c54-381e-90df-bf50164ac016 | -9.16263 | -60.7979 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b3d777d-473d-35f8-a79d-464608d6e53b | -9.12621 | -67.87241 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8aa2de-1a8d-3c71-8b72-00a86fe71819 | -9.38859 | -65.94592 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fa26e79-a2bf-362e-af57-349c74be515f | -9.00489 | -69.40489 | 2025-09-09 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f91ae07-5aee-3e12-9dbb-8eec79cb992f | -9.2237 | -60.81246 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70943a9c-0c39-336e-8cac-f01638b6db03 | -9.13121 | -65.96592 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1160fbd-1518-354e-a2ce-10d174e9423c | -8.74941 | -71.03594 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a21da92d-b2c2-371f-8446-fb4eed129cda | -9.6985 | -64.19074 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098932bf-8d8e-36eb-adba-be2e20e20614 | -7.56012 | -69.90469 | 2025-09-09 06:14:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5953c22b-436f-3b10-a455-acba3bbccc73 | -9.16872 | -60.79753 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1908e2b-f236-376c-9f36-f97c4b89ec63 | -9.13672 | -65.9479 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b200d2-8415-3fab-85bb-ed8bd074e1d3 | -9.08181 | -65.41032 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5cb0019-210b-39bc-aa62-c99a2fe5ff66 | -7.91376 | -70.2201 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3922cbe9-dd17-3ab7-a2a7-380c2cb1bbb4 | -8.88048 | -69.34703 | 2025-09-09 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82482c70-3bfb-3561-b595-c62164662d64 | -6.91869 | -62.93949 | 2025-09-09 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e0b49f6-048a-3886-b2e5-dc9f2e27b443 | -9.13594 | -65.95359 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3c76def-2eea-3bfe-b0e9-4be34914471a | -8.45041 | -70.13589 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b8b1ac8-dbf9-3b1a-86fe-9321eeb622ac | -9.13338 | -65.94901 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6da9846f-1ea4-3c37-a791-455e6b35ec14 | -8.72986 | -69.11119 | 2025-09-09 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abb0316-33ef-3598-9583-fadc5a5f20c1 | -8.50489 | -62.67847 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6c070e5-787a-3af2-b623-719efa2c9cd1 | -9.44808 | -60.51932 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40ab6907-498c-39b5-9b50-bfc44400f472 | -7.55575 | -69.90859 | 2025-09-09 06:14:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37c622e6-80b0-3405-98ff-3d9768cd1606 | -9.44888 | -60.51252 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5f1c1ab-c06d-33c0-b6d7-5a83f8c07ac4 | -9.08898 | -65.39571 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8be986-4dea-3380-a9ed-923ec0c46647 | -9.38364 | -65.94518 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61b04ce7-0737-3117-ba61-896067b0c1ae | -9.37802 | -65.93887 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 563ad746-a37e-3d1e-8f29-2fca5f66e890 | -8.27097 | -72.78815 | 2025-09-09 06:14:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0cb920f-5ec6-32e9-964b-755d7bde44a1 | -9.08939 | -65.39265 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04c59aa-78fc-39f1-8d9f-d3bbc1228ca1 | -9.47054 | -65.51572 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9905a43b-95df-3375-a58a-ee0036da1dc3 | -9.13891 | -60.52248 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ab4b92b-ee14-3458-817b-7ec9339329fc | -9.08592 | -65.37964 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ab02fe84-0260-3732-a431-eafc532c694d | -9.08651 | -65.41412 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7b6ffee-f9b7-3560-b953-eca44001eec8 | -7.40287 | -61.63265 | 2025-09-09 06:14:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74593ca1-d68e-3b43-a9c0-2788ac1d0697 | -9.13832 | -65.94975 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89550448-f905-378b-8fae-90b0f78c4c65 | -9.20957 | -67.55835 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c494a568-baf8-356b-9b51-1e47bfc3b848 | -9.69634 | -64.19448 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504117ed-6830-3919-bbef-225bc8cd50e9 | -9.47309 | -60.48844 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5327ea4-603f-3068-92ab-8d016861be25 | -9.06146 | -62.33784 | 2025-09-09 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85719cc7-9b22-3b7c-9a43-d91f8a941bd0 | -9.20455 | -67.56204 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 041f4c35-518a-36c5-8481-a304a5650c06 | -9.26137 | -67.60463 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 134feb93-39f7-3d43-b4cf-ce15d7454050 | -9.20575 | -67.55332 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 152437e2-1608-3ccb-bb57-ca61ff04d276 | -9.20896 | -67.56271 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7cdc19e-204c-3bd6-888a-04a89f9b585e | -8.29204 | -72.75875 | 2025-09-09 06:14:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ae13f46-bc41-37c5-ae2f-f059815fe9c5 | -8.27151 | -72.78461 | 2025-09-09 06:14:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2021a5e-0c50-33d6-be01-7cfdae24206e | -7.55947 | -69.90916 | 2025-09-09 06:14:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58d6a0d-8f39-34e0-aa4a-923b9664abd3 | -9.69241 | -64.19373 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e699e3db-90c2-3eaf-be54-b0d3f90098c6 | -7.82358 | -63.57538 | 2025-09-09 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5588ed54-04c8-39c1-aeb7-e463aa1c076c | -9.08427 | -65.39192 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10742482-145a-3c2e-aedf-d8f4901d86e6 | -9.48011 | -60.48936 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4996330e-27b6-384e-9f9f-96b900282b4d | -5.50235 | -60.13813 | 2025-09-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40c7f600-1673-32fa-adee-e2e7e49cc5f0 | -9.13024 | -65.95855 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ead1ac3-e5e9-30c7-8fd0-fedef63ec9a1 | -9.46449 | -60.50091 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e369c51-b7c4-31f0-8f0b-e9afa419eec1 | -9.13193 | -65.96036 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb75a148-a772-3e11-bd81-75f56ca4b6a0 | -9.12531 | -65.95782 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4018c54-1484-3f92-9f2c-9b22ec614401 | -9.44727 | -60.52618 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README72.md)
