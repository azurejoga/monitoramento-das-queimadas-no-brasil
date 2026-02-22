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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7423400c-9119-39f3-8035-5422df63d779 | 1.42742 | -59.9629 | 2026-02-22 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a852c488-631f-3640-bb39-cdffa2650605 | 3.22867 | -61.19651 | 2026-02-22 05:10:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ff2bf90-3169-3f58-99c4-a19cf194700a | 3.24453 | -59.93522 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d0fd31a-d3bf-39c4-a72a-e193c0511a26 | 2.76895 | -60.29084 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a5eb53-1a62-3dbe-ae41-37f7e32486c6 | 2.77293 | -60.29022 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c553197-07f1-35ce-95e5-06b8c9d791a0 | 0.74401 | -60.07178 | 2026-02-22 05:10:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62bccbdc-a287-372d-923a-e620a48eeffc | 1.98499 | -61.4325 | 2026-02-22 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31a90043-abb2-3570-bb7b-8f489ee68138 | 1.43507 | -59.96169 | 2026-02-22 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7038d447-33f5-3018-942b-e3340019c39d | 1.0306 | -59.57331 | 2026-02-22 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c045cbeb-0a05-35a2-9f15-d8332755b08a | 3.48862 | -59.82637 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4c10ed8-b4e6-3f34-a85a-968c7f5c8643 | 3.21389 | -59.9705 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eb0384be-84dc-3a07-9bee-65581d8af434 | 4.177 | -60.88958 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cc2741a-750a-3a2e-93a0-fd8225525611 | 3.43507 | -60.3492 | 2026-02-22 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91f653c0-f79d-3418-9816-972c938da488 | 3.21704 | -59.96489 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| daa5c4d0-51dc-3654-b2fd-59810f583682 | 4.15832 | -60.93711 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db88e57b-2695-358a-9fb9-96395b42f5e3 | 3.24421 | -59.93336 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2084a10-bb5d-32d8-bd19-4811f3ae4146 | 1.00389 | -59.51225 | 2026-02-22 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ac75599-716c-34f1-b1cc-7f55c01bae6a | 3.1964 | -60.42603 | 2026-02-22 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc5536c0-3f25-3e2f-bc5c-cab161cefece | 0.89385 | -59.7935 | 2026-02-22 05:10:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b86cca6-cd5f-3df2-a488-46dd9c43d509 | 1.00497 | -59.47155 | 2026-02-22 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df835256-8c43-3afe-abe8-e79e422f5617 | 4.14813 | -60.89917 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f15a0f9-cb8f-3c2b-bc55-4ba5fc27c062 | 1.42287 | -59.95876 | 2026-02-22 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da3d080c-80c9-3a0e-8f82-b9e7cf2c32b8 | 4.14806 | -60.89867 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67b64721-90f3-337b-90fe-7213b584f636 | 1.43434 | -59.95694 | 2026-02-22 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39e7998f-6938-336c-a0f5-2ae442a0e88d | 3.48471 | -59.82697 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d05284b-3263-303e-b544-707a3aef173e | 4.14566 | -60.88315 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3747b792-6abd-3be9-ba13-da0d224727c2 | 4.05632 | -61.11832 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6892d95-8959-35aa-9484-481470cd7aba | 4.14276 | -60.89203 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f59d6100-620e-31a8-b70c-ce3dc31dbd7e | 4.09957 | -61.15554 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9682f37-1d80-3a21-89f0-ab682cf813d9 | 3.24061 | -59.93582 | 2026-02-22 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abfca37-cefe-3a5f-9ec5-b42a8b700b9b | 3.44972 | -60.74553 | 2026-02-22 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf29290-787c-3c2b-a3eb-d6ce34b9e9f7 | 1.00389 | -59.47367 | 2026-02-22 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 380788eb-b488-3027-a1cd-09ac38850043 | 4.14264 | -60.89157 | 2026-02-22 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13f014bf-f474-3130-8655-8634683b9485 | -11.20443 | -55.92396 | 2026-02-22 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5ff8d43-c18f-30cc-97b0-d1831bd39a54 | -19.8889 | -57.85672 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 29134445-80e1-35f9-b258-12b5644f7a0d | -19.94427 | -57.87406 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0a46e49a-5cab-3b38-b1cc-cdf2b5199ca3 | -19.88477 | -57.86036 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 373fdc7e-fc23-3b0c-be02-e656df3e345e | -19.90304 | -57.85895 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b0b509a3-a866-3914-8844-d0a83cf0f07d | -19.91246 | -57.86902 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 51bd9843-50bd-38aa-a6e5-1d439d55db36 | -19.90657 | -57.85951 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ddb8c456-15f4-37d5-89f7-2c7aed840c00 | -19.88538 | -57.85839 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 63bed316-8f2a-3d30-92d5-d98273fb0dde | -19.94781 | -57.87462 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f12104ce-69eb-30a1-91c9-ef2ce9abfd9f | -19.9378 | -57.86874 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ee95ca73-faff-340b-87df-7faeeff51890 | -19.916 | -57.86958 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 91dba2e8-4cf9-3efc-8197-fe8928c816e2 | -19.93367 | -57.87238 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9a5bc946-cb40-3687-8c06-65d8a5b93d71 | -19.95074 | -57.87937 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 492ea715-5859-3552-abbb-7f64fdc04d36 | -23.70537 | -54.97477 | 2026-02-22 05:16:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc4f5683-2c15-3b6d-a20e-e9eecc7b0de1 | -19.94721 | -57.87881 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 23fb6dd0-3a9f-3e38-9a0f-7f02356a3dfc | -19.94074 | -57.8735 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e1cf77df-6c98-3fdb-b3fd-607eb8e8888b | -19.95428 | -57.87993 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 597aa843-5a8a-3429-80af-742c243885bc | -19.90952 | -57.86427 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ad46524f-e3ee-3c1b-8256-85a0b7875972 | -19.89243 | -57.85728 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bc54345a-78c8-3622-940a-9e7227eef433 | -19.94133 | -57.8693 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c51902a0-c59e-38df-9c6e-a6df0cfc04f0 | -19.8995 | -57.85839 | 2026-02-22 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d6aaf18b-c6ce-3662-9fe5-f750e3b5682f | -23.70572 | -54.97702 | 2026-02-22 05:16:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee26a8ce-686e-3513-9b36-b53a14f22c3a | 0.89339 | -59.79023 | 2026-02-22 05:59:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0d029fe-484a-3890-a558-8f154a58abb2 | 1.42343 | -59.96096 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97ab774e-4a7c-379d-9c54-b2961c419da8 | 1.43406 | -59.96226 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59a4db83-557c-3a4a-b351-1d2d9518eff3 | 1.45247 | -59.94709 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6fdedf2-25a8-39e5-a3bd-281b5b863c4f | 1.43867 | -59.95854 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 386fd0c9-6e7e-3f07-bfcb-829e783baeef | 1.4382 | -59.9556 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f32d00a-2578-3984-8b65-16e2cb300317 | 1.44233 | -59.94892 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258711b0-a443-3ffb-aa1f-4cd34e555b4d | 1.42247 | -59.95506 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cef65412-88ba-3846-b21c-545d758bdc8f | 1.42295 | -59.95801 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 13a7de2b-dd5d-3622-aca6-80215f1816d1 | 1.44787 | -59.95094 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ba3be82-6efb-3c00-9447-c316a5d3aa14 | 1.43358 | -59.95932 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da861d18-802e-38f4-9cc5-87900d0eb70b | 1.43311 | -59.95638 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e813566a-baac-3197-a73b-888503b7b54d | 1.42802 | -59.95716 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce98ebb1-083a-3872-a167-111355b1e9c2 | 1.45343 | -59.95309 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d8abc23-2d4e-3015-9811-9d2d44d1ef47 | 1.42707 | -59.95131 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2264a5b-11d4-3f2b-8eed-f9c7dbdc3444 | 1.45295 | -59.95009 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb31f20b-b70d-3cba-ab3e-841eab69800c | 1.42755 | -59.95422 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0467ea7e-585c-3fcc-bdab-868d1b55bd95 | 1.42199 | -59.95211 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74b211b2-2762-3303-90e3-37bb49753c62 | 1.43773 | -59.9527 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f00caa-feb0-38d0-8323-88b603fc3759 | 1.4285 | -59.96011 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81fbd06a-eabc-3165-84d3-eaac6ffce715 | 1.43264 | -59.95345 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59f69b1c-4189-301c-a271-4eb571c58bdd | 1.4474 | -59.94798 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b10c1574-b869-3039-858e-aae029540209 | 1.45391 | -59.95609 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98dbb84e-e283-3edd-8272-391511ec56b1 | 1.44835 | -59.9539 | 2026-02-22 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b336ee9d-ee9a-355f-9fd3-068142e455b9 | 1.4316 | -59.9503 | 2026-02-22 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e7bf0cb0-6230-3641-a86e-251567d7c0d7 | 3.22852 | -61.19273 | 2026-02-22 06:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e370ab3-3547-345f-8e7d-83a980b78fad | 4.15409 | -60.93661 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c6ae0c4-5abf-3ca8-a78e-83d5600d5764 | 4.1524 | -60.87568 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2ef340-f0eb-3d26-8055-5d738917d8a5 | 3.24461 | -59.93455 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 971078e8-1ab1-3507-854c-f815dd8ad02e | 3.22174 | -59.95002 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e10904ae-0830-3e51-b04d-4dd8401da4a2 | 3.22318 | -59.9491 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 695ae106-010f-30f9-93f1-3bb397dfa3fc | 3.19069 | -60.42853 | 2026-02-22 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54d2fac7-6c60-31b2-8a23-7dee7109e342 | 2.70818 | -60.24106 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c6fc0666-881f-3cc9-a2c3-3db9eac42a8a | 2.70242 | -60.23642 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb37a5d2-b9b6-3e30-9466-6421f2501370 | 4.09231 | -61.15943 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a743f5be-4c42-37f0-ab4e-95901f537eb6 | 3.04416 | -60.14132 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e1cce4a-e31f-3b91-98f2-7df51f786076 | 3.19069 | -60.42649 | 2026-02-22 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c3964a3-b1be-30ce-be5c-f7481b3ebb5c | 4.08558 | -61.14676 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f7107ed-4c5d-3c73-bb6d-71445149f006 | 4.14785 | -60.87648 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 332e632f-1200-3fad-b6c9-3f19bc408ad2 | 4.1529 | -60.87422 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74756cd1-b90d-3082-a4b3-1a651e5921cf | 2.69088 | -60.22709 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| feb5a854-e87d-3eae-88a5-88600ce1b57d | 4.09602 | -61.1541 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b360e91d-5552-3d77-8a73-6da76259d686 | 3.24102 | -59.93455 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1991370-3737-3579-a421-8c4179ad7e3d | 3.2827 | -60.09321 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75c6d1cf-518c-3248-a0a3-557936104988 | 3.21459 | -59.96849 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README4.md)
