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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8cb0fa2-efb6-358d-a193-400fc0bff6f2 | -10.8495 | -46.1771 | 2026-09-16 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 98b8a689-9c73-3aec-9f03-d51d0a8a4520 | -13.2239 | -51.6318 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 92ff8efe-df38-32d4-9080-a80cdf267999 | -7.3561 | -44.4956 | 2026-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| bfd60026-ddbb-3cbb-b579-2b5dbe18fbcd | -13.2874 | -51.2618 | 2026-09-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cf3fdfbc-9030-31ad-ab02-517425f408a5 | -9.3893 | -60.3022 | 2026-09-16 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b3a623ab-caee-332c-861e-5c3c3c37b5aa | -6.8032 | -59.1693 | 2026-09-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 319.9 |
| 46005e64-2f6b-3853-8cbc-30292f9bdc04 | -6.3256 | -62.6909 | 2026-09-16 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 167.2 |
| a891d446-3d95-33c7-840a-87cd13cb9b33 | -13.1855 | -51.6365 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a6521e6a-89e7-33c4-a843-3e168a48da0e | -8.6188 | -44.4819 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 591.2 |
| 1c805803-cffa-34a9-a32a-6ec6bb73e5f0 | -10.3116 | -45.3136 | 2026-09-16 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 2eff9714-a0f5-3edd-a914-45fbc56356bd | -9.1337 | -65.844 | 2026-09-16 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ba8df637-cce1-33a4-945f-fd213e66e4d9 | -12.1579 | -48.9647 | 2026-09-16 14:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 5f9f58d1-b044-31fb-825e-2800b893b610 | -9.3567 | -50.1796 | 2026-09-16 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 05e16da2-6169-3a73-b52b-f953e7c9d16c | -6.3257 | -62.6721 | 2026-09-16 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 2b38000e-8578-3e21-8580-03ca34f1d652 | -6.0184 | -57.7657 | 2026-09-16 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 57d21356-5f32-3ac4-ae0f-7fd70e2db4aa | -5.7614 | -57.6002 | 2026-09-16 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7609fd2b-4ba8-3b40-8eb7-2ad3a47eb4ea | -10.8919 | -54.0062 | 2026-09-16 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| aa354c59-fbcd-3e3a-a3be-106d42996da9 | -8.5415 | -54.7187 | 2026-09-16 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a4d7480e-c619-3bda-9b48-7bdb371475b3 | -2.6966 | -57.6084 | 2026-09-16 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 418.1 |
| 58faaedc-64c5-3588-a3d0-c98259fec041 | -9.2311 | -46.7055 | 2026-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b286f89f-f185-3d3c-8cf8-12238185fddc | -9.4325 | -50.1299 | 2026-09-16 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0930e263-84c2-36a4-b781-9074e6df8518 | -9.3707 | -60.3032 | 2026-09-16 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 01157909-19f7-3615-9bcf-2c1f4587974d | -6.8216 | -59.1686 | 2026-09-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 214.6 |
| 0f9f96c5-e6aa-3a08-8578-db3dfbf54b44 | -14.4479 | -40.8379 | 2026-09-16 14:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 706ff020-8bf1-3fc0-9844-675978ae859f | -11.9033 | -43.8112 | 2026-09-16 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 2ac5cad1-917d-3254-9165-da241129c6f1 | -11.5432 | -46.8745 | 2026-09-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 31c044d3-11f6-3d45-8a6b-59ae07d7dcda | -10.8571 | -50.8183 | 2026-09-16 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5ecbe712-6121-3896-82c7-e48ebba70525 | -9.7608 | -60.4561 | 2026-09-16 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7a04a1b6-6e0c-3bb8-a66d-99d3b03b95fd | -10.5975 | -47.7505 | 2026-09-16 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 259435a8-4a96-391f-8c5d-e0d7faf073b8 | -6.344 | -62.6904 | 2026-09-16 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 767ddec6-ee85-3cf0-8689-cefc995d48f0 | -10.9875 | -48.3209 | 2026-09-16 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e0ef6fd5-2e6e-36bc-a52b-cf0996a26a51 | -10.9108 | -48.3739 | 2026-09-16 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a80ff46f-1ee5-3ba1-b4b1-6d36bd30b90b | -13.2044 | -51.6555 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6ab8dc0d-4a09-30d4-8954-63119c38043f | -11.4167 | -51.4371 | 2026-09-16 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 19ba2fdc-1bcc-311c-b3ac-009487a696f3 | -2.6783 | -57.5893 | 2026-09-16 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 0cffa853-ae46-3856-9749-1b3ca46bf63a | -9.2311 | -46.7055 | 2026-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| bb94a787-8d07-3094-865e-2e138440d767 | -9.7793 | -60.4744 | 2026-09-16 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 77475bdd-cec8-37c1-ab3b-136eea0700f9 | -13.1855 | -51.6365 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 82b9791c-b14a-31a9-a88b-e03ce987fa2a | -12.3273 | -47.9735 | 2026-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 558cfbf6-b0ac-363c-909a-dcedd008aba0 | -10.8916 | -54.0267 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| b7bd9b9b-1bd0-3159-9da8-c512937e7de9 | -6.7703 | -48.6792 | 2026-09-16 14:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a86ba39c-8bf2-3811-b09b-252be8a84c9e | -10.9107 | -54.0045 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 1ebd7c56-8bb9-3e01-babc-77ffa4205598 | -11.417 | -51.416 | 2026-09-16 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 46c560e4-b38e-380c-9a5d-1f8ff9d96767 | -9.3892 | -60.3215 | 2026-09-16 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7a62e670-8463-3974-9cbb-5a1377d0091d | -10.6829 | -54.1475 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d9ff0dfb-6bd3-3541-bbc2-2a786238ea37 | -6.8032 | -59.1693 | 2026-09-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 412.8 |
| bc30a236-0c20-3af2-a1b9-990ce8b2cd0f | -10.8919 | -54.0062 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 6c85c953-738d-3190-8473-a96ef6b285ec | -2.1052 | -52.037 | 2026-09-16 14:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d9ddca56-a954-30ef-9483-c043d20b3132 | -11.8941 | -47.5876 | 2026-09-16 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2ff8a90b-d89e-3502-b9a0-fb6a954ed3c4 | -12.126 | -44.2225 | 2026-09-16 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| cee59214-d9a3-3adb-bbdc-a379a36ba131 | -10.1179 | -45.5662 | 2026-09-16 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| d92de2db-d3e4-3d05-bb19-b088f30d6cd8 | -6.174 | -53.524 | 2026-09-16 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 41ee9ebe-834c-3281-b1c1-2bd2ad0c745e | -12.1072 | -44.2021 | 2026-09-16 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 6c570b53-88e6-3389-bba7-2c3ec9005535 | -13.2235 | -51.6531 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ab09f2d5-8aaa-37e5-aec8-ce83060b87ca | -2.6783 | -57.6087 | 2026-09-16 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 3e1bfa19-1245-3843-88b8-1bf1471bd779 | -13.2874 | -51.2618 | 2026-09-16 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2eb12c04-14af-327c-9b46-8bfa91371b33 | -9.1337 | -65.844 | 2026-09-16 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5f37880c-f524-3b57-90d3-313d320b310d | -9.7322 | -64.9067 | 2026-09-16 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d903cf5e-aa99-3ce0-9ea0-9ec98a3f97e8 | -12.0488 | -47.4777 | 2026-09-16 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 2132d038-4d90-30c5-9b58-1bc0d110651f | -6.3257 | -62.6721 | 2026-09-16 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 183.8 |
| be7d3a8d-378f-331c-8531-c2cdc1560194 | -5.144 | -55.9345 | 2026-09-16 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a5d0376a-f38a-3a79-ab66-c0547250eb76 | -6.3147 | -41.6807 | 2026-09-16 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 35a497ca-22e9-3396-9424-b5c7daaf2abe | -9.3893 | -60.3022 | 2026-09-16 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 308e7f4e-45ab-3e6e-8963-adbc1acbb043 | -10.876 | -50.8163 | 2026-09-16 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 42defd1e-a720-3b5e-bff6-08948e64b870 | -6.7705 | -48.6577 | 2026-09-16 14:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 6ddf969c-36a0-3dce-bbb2-e3a790394868 | -13.2678 | -51.2856 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2fabc247-d714-335e-aa90-b077556e137a | -6.8215 | -59.1879 | 2026-09-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 225401c8-7aaf-3982-b057-75dd1fd5bdc2 | -6.7684 | -58.8035 | 2026-09-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ebceef92-9f63-3a2e-86e9-e268b282531e | -5.6611 | -43.2272 | 2026-09-16 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 191.5 |
| 365eb6f5-c278-3b53-ab53-2a8fa9d4c96a | -13.2239 | -51.6318 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 28d21f7d-f858-3c49-add7-46ce980f7ced | -5.6311 | -51.6858 | 2026-09-16 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c87ec11b-b816-37e3-a47a-610a88484d4b | -12.1265 | -44.199 | 2026-09-16 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 76be2e37-72b1-3545-816b-96de6f59c4ff | -9.4325 | -50.1299 | 2026-09-16 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| effec3a5-09fb-3888-94cc-b9ade06200c7 | -13.3758 | -51.7193 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3ae7df5b-16f5-3821-8ae6-e83931501a66 | -10.9105 | -54.025 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 0e378a04-8bb1-3e76-8478-8deee0ce2ddf | -9.4139 | -50.1103 | 2026-09-16 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 70516e12-312e-3283-bf78-dfdd7d0587f4 | -10.9685 | -48.3232 | 2026-09-16 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8bd584d9-3966-37fe-a222-51c0831a1857 | -12.3085 | -47.9539 | 2026-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 06b39262-6b22-39eb-9c2c-7bee092e145d | -10.8495 | -46.1771 | 2026-09-16 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 86449af2-57cd-3a53-9136-56f1c675ebcf | -10.3955 | -58.2962 | 2026-09-16 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 233.8 |
| ae003613-8215-3e44-9981-9e8f3f67be41 | -8.5428 | -44.5132 | 2026-09-16 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 381.5 |
| 07887883-8048-3449-b308-5ff0d332e03b | -13.287 | -51.2832 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 4fa9d7b7-7d11-3c0d-ab9d-bed84de61a2c | -12.3277 | -47.9513 | 2026-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 336.1 |
| 1ee6ee1e-b072-3db3-a3f6-e89684ab771e | -10.3953 | -58.3159 | 2026-09-16 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 454.7 |
| d4c7cd9b-33ba-30f7-8307-5b8ea81beb05 | -8.5617 | -44.5112 | 2026-09-16 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 382.8 |
| 72a41042-e137-376f-b837-9aaa6caea838 | -13.2867 | -51.3046 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1b749a06-f875-36be-be20-44b165f2c3f9 | -13.3059 | -51.3022 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c7493f3f-f4a8-3d5a-8b64-588f9b17b18a | -10.6827 | -54.1679 | 2026-09-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 40df8fb9-6726-35f1-aa4e-701c419e0efd | -8.6188 | -44.4819 | 2026-09-16 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 186.4 |
| f223315e-81be-3427-bfe7-5b423dec6847 | -15.6557 | -52.7366 | 2026-09-16 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c9b276b1-43fb-35ed-b556-ee1fd975d6a3 | -7.3561 | -44.4956 | 2026-09-16 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| d014d3ce-cebd-31b0-8b4d-133ef9f2f32d | -8.6566 | -44.4777 | 2026-09-16 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 265f9d5f-b477-3749-8646-094cb3b3e415 | -10.3766 | -58.3171 | 2026-09-16 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| aa277e2f-b4db-3d22-aa03-6668b8997797 | -12.4145 | -48.4701 | 2026-09-16 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| caaac22e-122e-33e1-aa0a-2110b0af1231 | -5.7614 | -57.6002 | 2026-09-16 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 95a0b9e1-3f1b-3106-9d30-164cf43775ab | -11.5436 | -46.852 | 2026-09-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a1472cb2-badc-39c5-a453-da40a4e467ad | -13.2047 | -51.6342 | 2026-09-16 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ec713675-3b87-3334-8a59-6e441cd125f4 | -10.4772 | -50.9634 | 2026-09-16 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| beb917f2-4cf5-3b1b-aeb2-f15fdd5dabbf | -12.3081 | -47.9761 | 2026-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 60d7ce11-6521-3348-a158-903cf1c52cfe | -6.77 | -48.62 | 2026-09-16 14:15:00 | MSG-03 | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README75.md)
