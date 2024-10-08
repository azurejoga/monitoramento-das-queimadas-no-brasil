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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa89f71e-6c2e-3e5d-b2f2-7ae585a093bb | -18.6195 | -57.2396 | 2024-10-08 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.1 |
| 246d9d25-d8ad-3cc5-98a0-bc712f1e95e1 | -8.85108 | -72.73904 | 2024-10-08 06:37:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b37b46fb-1e60-3b32-986c-63477e8fce88 | -10.8754 | -63.9169 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 317c708c-4584-367f-a45e-d33f6c6bd8bd | -10.8755 | -63.8979 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ba9ba426-83dd-3c4e-b80b-64548126a360 | -10.8924 | -64.1813 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6a795bed-f553-3449-a195-a896e1b8d3af | -10.8926 | -64.1434 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d1245a1a-df87-3663-998a-71942238802f | -10.9111 | -64.1805 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 922b5b69-92d6-39d4-bf7d-fea6c620c5a8 | -10.9112 | -64.1615 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 97e8d97b-dee6-3add-a6df-23369a304ed6 | -10.8925 | -64.1623 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 153b5202-94a7-3665-b909-8aa803ed429b | -10.9113 | -64.1426 | 2024-10-08 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9a7941dc-8f60-317a-a322-7a765c4ddf83 | -12.4605 | -62.9977 | 2024-10-08 06:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 95e58bd9-023a-3837-9493-836bc50a630e | -12.4603 | -63.0169 | 2024-10-08 06:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.2 |
| a868882a-d8f4-3eae-8db9-b75a80dfa218 | -16.4184 | -55.9455 | 2024-10-08 06:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 6b545f7d-2aaa-3c63-aa5c-9b1c1e62b637 | -16.7852 | -57.422 | 2024-10-08 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 611cd44b-175e-3ab8-b093-9df6cb54c72c | -16.8048 | -57.4197 | 2024-10-08 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| a491dd05-c972-3241-b0b2-0683e4eb0914 | -16.9407 | -57.4859 | 2024-10-08 06:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| 76ff6cb3-d1ac-38b2-af35-ea9402ce9861 | -16.9211 | -57.4881 | 2024-10-08 06:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 78e1e606-e1e4-3e0b-86a1-17fb570ead64 | -17.1074 | -56.851 | 2024-10-08 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| dd4495e5-1467-32a5-addd-8a5ea07c13a1 | -17.1471 | -56.8256 | 2024-10-08 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 8e11eb37-b5e7-34fb-8814-02113ab7c08b | -18.4931 | -53.4457 | 2024-10-08 06:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f1486ff8-68b9-3b50-9e32-b15059d80aa5 | -10.8924 | -64.1813 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e3d9e0aa-4b0c-336f-9f92-edacd2ed1076 | -10.8925 | -64.1623 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 187.7 |
| ad310570-6682-3baf-89a3-4fb046d44311 | -10.8926 | -64.1434 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| fe1944f2-128a-387e-a4cc-ab2cb06e6f54 | -10.9111 | -64.1805 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4e207948-e25c-321a-a051-0cafd04c067b | -10.9112 | -64.1615 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f93b4352-6376-3124-bd0f-c9fd593c3316 | -10.8755 | -63.8979 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f022d242-c9a3-3f9e-8dc7-cbbb3a017cad | -10.8754 | -63.9169 | 2024-10-08 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 635bbb34-838b-32d7-b8af-229aa946e678 | -11.673 | -65.2062 | 2024-10-08 06:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| a84ce7fc-3b7d-3f8c-86db-8df9fbd3c020 | -12.4605 | -62.9977 | 2024-10-08 06:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 82e43bb0-1a61-347d-8c1f-5e03b02590f1 | -15.7068 | -59.4326 | 2024-10-08 06:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a234a0f6-da03-32c9-a0cb-f72ee05a7db8 | -15.7071 | -59.4126 | 2024-10-08 06:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 9a87f7fb-9901-323d-9f27-e35336c8d2ef | -16.4184 | -55.9455 | 2024-10-08 06:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| 06d3f152-68ef-3e5f-9037-035475ee1b2a | -16.7849 | -57.4425 | 2024-10-08 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| c1cfa5b1-8791-32aa-a005-9b34c903c232 | -16.7852 | -57.422 | 2024-10-08 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 4445b200-8afd-3abb-aca7-1cece7c99ab8 | -16.8048 | -57.4197 | 2024-10-08 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| c487b85f-e893-3a58-8076-879c4f120e6b | -16.9211 | -57.4881 | 2024-10-08 06:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 8acf43e8-2f72-38f4-9052-759ee3858750 | -16.9214 | -57.4676 | 2024-10-08 06:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.1 |
| b684ffdd-3921-3a1a-8910-903e6a129a18 | -16.9407 | -57.4859 | 2024-10-08 06:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| c242c954-01d8-348d-87cf-4113293c03f2 | -17.0881 | -56.8328 | 2024-10-08 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 09e23bdc-df2e-3570-95ac-8ada1f90a7a4 | -17.1178 | -57.4244 | 2024-10-08 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 080fc9e7-a8e6-35d7-87b7-afed3c508e71 | -17.1471 | -56.8256 | 2024-10-08 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 26febd52-028f-3806-826a-f0c6317f5759 | -18.4931 | -53.4457 | 2024-10-08 06:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 14a2182c-08f5-38a8-b833-04d22b5246c0 | -10.9111 | -64.1805 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ac0fda78-7bcd-3bbb-9987-7e4a1777c26b | -10.8924 | -64.1813 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5fc5aaf1-0cec-3c36-a2fe-4d3dee4a69b1 | -10.8755 | -63.8979 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 025cded0-5203-3a8f-b3f3-587d329ec139 | -10.8941 | -63.916 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| cffcc565-18a9-31f7-b476-f0c0e37b9029 | -10.8925 | -64.1623 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9c7cc4bf-f198-3f1d-b9cb-db029ad090e1 | -10.8754 | -63.9169 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 037821db-cdeb-3c3e-854e-fb25e628e2e2 | -10.9113 | -64.1426 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2c8879ca-1908-3da4-bfda-63bf1741431f | -10.9112 | -64.1615 | 2024-10-08 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.8 |
| afc5c6ec-4947-31bf-aac2-1b104485669f | -15.7068 | -59.4326 | 2024-10-08 07:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ee888e91-73a2-3a2a-800d-dbe1bfe2eae6 | -16.4184 | -55.9455 | 2024-10-08 07:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 9c4ba0c5-c80b-37c6-94e6-4999ae929c3b | -16.6726 | -57.1283 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| de112f3e-aca2-3220-9b52-3f4e31e2e762 | -16.6531 | -57.1305 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 391dfc27-e77b-3663-82c5-0b12b30157f0 | -16.673 | -57.1077 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.1 |
| 930769cf-2be8-39d0-92ac-b83dade46036 | -16.6733 | -57.0872 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 0f8be5d7-fd6f-3fc9-8daa-d93761e8be89 | -16.6922 | -57.126 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| fc0b1908-cdc3-3630-93ca-8d81ebbba094 | -16.6925 | -57.1055 | 2024-10-08 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 179d17c5-ec05-3184-a259-65252aff6783 | -16.8048 | -57.4197 | 2024-10-08 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 46b8b788-a03f-372b-86d9-e2c5bfb4411c | -16.7852 | -57.422 | 2024-10-08 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 692314ec-c805-3e2b-b350-974a3b8c2a78 | -16.8045 | -57.4402 | 2024-10-08 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| 69efbd70-a246-3c7e-be9d-c252a76796b7 | -16.9407 | -57.4859 | 2024-10-08 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| b44a62b2-f04e-3083-9bfb-a60846975513 | -16.941 | -57.4654 | 2024-10-08 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.7 |
| 4833b87e-c7a4-3c1d-bfb7-8220a325332a | -16.9211 | -57.4881 | 2024-10-08 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.5 |
| c6ad90df-4c37-3672-b0e9-a22ed3d8b39a | -17.1178 | -57.4244 | 2024-10-08 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 41b578e9-dcb0-31cb-a527-9f593d5cf3c7 | -18.4931 | -53.4457 | 2024-10-08 07:06:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8fd1a46e-4f78-3bac-9e13-637649ce6e73 | -20.3525 | -48.8186 | 2024-10-08 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0c750158-2029-3efa-9078-a8a83a3e79bb | -20.3519 | -48.8417 | 2024-10-08 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 517368d7-b6ae-3d55-8ded-d1d4d77750aa | -20.3724 | -48.8372 | 2024-10-08 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 71db32b9-94ad-31a3-b998-d257eba29efd | -20.3513 | -48.8648 | 2024-10-08 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2becff1f-b4f0-3cfb-8783-6d583de8b90f | -10.9112 | -64.1615 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 61e1bc06-b7d2-3001-9924-bfca2ac71b7d | -10.9113 | -64.1426 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 7ce2c835-9598-3aa3-9354-8f6f89e9b7c3 | -10.8754 | -63.9169 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8edb0092-1639-3238-b98d-e58a27677460 | -10.8755 | -63.8979 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 34863bbb-c390-3450-90b0-3eaaa0485018 | -10.8924 | -64.1813 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| db448650-09bc-3e84-8d37-230790b128ad | -10.8925 | -64.1623 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 145.8 |
| a3983920-cfbd-3578-9bbc-00ee8603dfe2 | -10.8926 | -64.1434 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6c6e5bab-cb66-31d6-a2e5-711ed6cb727b | -10.8941 | -63.916 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 6f5861f3-4da3-3985-b1c6-cbe1353a2154 | -10.9111 | -64.1805 | 2024-10-08 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 8f8a08d5-1b5d-33f1-97f7-af94d03bfd1e | -16.4184 | -55.9455 | 2024-10-08 07:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 40fd4f39-0f19-3815-972d-35cae37d69b7 | -16.6922 | -57.126 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 32cbb5e3-a754-34b9-a8ca-f3b0d49ab0a1 | -16.6531 | -57.1305 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 4523d3bc-49e3-3e32-9011-d9fa5d378ab8 | -16.6726 | -57.1283 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 43b4862b-6160-3982-baef-8506aa66a3fa | -16.673 | -57.1077 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 82a2a8a7-d9bb-3bd1-aa20-020c2ab16a56 | -16.6733 | -57.0872 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 3ed46ad9-e21e-30df-9af5-2dc6b53614ca | -16.6925 | -57.1055 | 2024-10-08 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 6517756c-4849-349b-ba72-8524caf9023e | -16.7852 | -57.422 | 2024-10-08 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 2c652e13-6e58-346f-9fd4-54b910ab7f4d | -16.8048 | -57.4197 | 2024-10-08 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| bee5d139-6b8c-376b-901a-6a27d7368f43 | -16.941 | -57.4654 | 2024-10-08 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 55f35efb-c4a9-399c-870e-3ec9963c264f | -16.9407 | -57.4859 | 2024-10-08 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.5 |
| 4be7d2e5-226c-31f5-9430-555aa71d4125 | -16.9211 | -57.4881 | 2024-10-08 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 8e81eac4-3b73-37f9-a6cc-59134e1ad15d | -17.0992 | -57.3651 | 2024-10-08 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 5e5c5025-dd74-30e9-9102-50b6289a03f9 | -17.1175 | -57.4449 | 2024-10-08 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.6 |
| cc9da1dc-9c60-3baf-acb1-fe95386e5511 | -17.1178 | -57.4244 | 2024-10-08 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 1c6d6930-ca8a-3ac0-a74b-8f003a1e905e | -18.4931 | -53.4457 | 2024-10-08 07:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 000d0a67-351e-3a0f-b226-0adf4de13df7 | -20.3513 | -48.8648 | 2024-10-08 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d441301e-eceb-3dd5-a553-091969022b78 | -20.3519 | -48.8417 | 2024-10-08 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 141.4 |
| af320688-7f6a-30db-b18c-8b616a56953f | -20.3525 | -48.8186 | 2024-10-08 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 34760dc3-7c1a-3a5e-8ac7-04c25e814ded | -20.3724 | -48.8372 | 2024-10-08 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 309ee40d-efb5-333c-a1af-0b2f94548457 | -20.373 | -48.8141 | 2024-10-08 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 89.1 |


[Clique aqui para ver as próximas entradas](README133.md)
