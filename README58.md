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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c677acd-1616-38df-ab8a-6726f4a88d85 | -2.99958 | -57.93064 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4585ad-bd1e-3ef3-9f36-9758ed2570d5 | -2.92137 | -50.41376 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 286215ef-1512-350e-9ba0-2bc09b6952dd | -3.3487 | -59.38475 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2dab61d-d452-3276-9630-5ef009314459 | -2.89716 | -50.39175 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64806225-3850-31b2-b34c-9ac78f565604 | -6.64396 | -58.82135 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8764691c-e74b-35b6-ae12-374ef092ad20 | -2.91397 | -50.3701 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e127af0-216e-3a70-be84-3d0af3f799c7 | -2.89209 | -50.42718 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4c5a37e-1f4d-364b-92dc-b6b456fc9f0b | -2.66486 | -57.50398 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f320ff9-0b11-3a7b-aafa-2f41236eb9cb | -2.90811 | -50.3632 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eca6002-fada-36e7-a6ce-75ae47cf3f49 | -3.52927 | -59.06731 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fb99270-1487-366c-a9cb-dbc2aaf9051a | -5.12645 | -55.95311 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96acb336-2c22-310b-a9c2-a94634cf11ed | -2.93388 | -50.42181 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd298d50-e9a6-39fb-a16e-1eb65fa17e7b | -6.6959 | -59.12717 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5677044b-cf0e-34df-b649-7bc81738c8dc | -4.1232 | -60.68665 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| aef55a76-aaa1-390b-8ea4-423b00479b65 | -3.81357 | -55.89284 | 2026-09-14 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ab36b97-e816-36f8-ac72-a13ea0e72f0e | -7.87755 | -54.71957 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5cda399-1a26-3210-add3-c2eaae1c93fd | -6.29709 | -55.27402 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fa65dbb-2e0b-3d33-945c-b24fb112e526 | -3.41488 | -58.21418 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9156d80-2863-353e-8336-d3782931f78e | -6.01946 | -59.9491 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 330035eb-117c-3d75-9821-b20a39ee70b5 | -2.67211 | -57.53996 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| afdbc511-725f-363f-82e9-f7b81082bc0c | -2.9265 | -50.3783 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b21a45f9-674c-3d35-938a-b78256e80d62 | -8.23755 | -55.23 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77e322de-f565-33a5-9b3a-b80a155079a6 | -2.22936 | -60.04427 | 2026-09-14 05:36:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d046f7c-0418-39f1-aac8-762b5b4f9d09 | -2.89882 | -50.40493 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 13206b1c-ae35-3b7c-bdac-65052fe4b529 | -3.1651 | -58.6402 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fbf002aa-1ac0-3272-b866-50a533e26838 | -2.91265 | -50.35866 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e697cfa-d45f-3896-87f7-bdfaf1720d8d | -2.90021 | -50.44118 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 26185902-a17c-33b4-b248-5fb5fa6ceced | -6.74377 | -59.43478 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8871663-cfd8-36a1-9a0d-86615adad254 | -3.72419 | -61.75306 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319e22e0-9744-31b5-a332-0577a2f1c2a1 | -3.22593 | -61.20683 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f01c89-12d9-3e30-b9fd-063804a3f871 | -2.91087 | -50.37043 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69173b23-a1f0-3f65-a08d-6fb3d2c3fd31 | -6.79207 | -62.97704 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2611b11-b88b-3b8b-bf63-5a0e93fcf75d | -6.8439 | -59.02035 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ee935c5-2cd1-355b-820e-40f91ef73b3b | -2.92736 | -50.37237 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 539e835c-ae27-3f8a-954b-ad16acf25dcd | -3.17562 | -61.12363 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c076af9-9afa-3f27-9649-312e1d5c89c1 | -2.9725 | -49.56134 | 2026-09-14 05:36:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d6bfc3d-d363-39b9-9fa7-61ead01f69c6 | -6.59597 | -58.86207 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9031bf9d-30fb-34b5-8b36-fdc00abe04b5 | -2.70667 | -57.54813 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2eafcde9-f6b7-3515-be58-903ef5a4eee3 | -2.88771 | -50.4334 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e6562ad-0560-3a47-bec7-81f463c2605c | -3.18364 | -61.1172 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 063e1f8c-9fb4-3f38-8755-515a7c11a514 | -2.91882 | -50.43132 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8170e166-a272-396c-8c00-82b3e7d23cd1 | -8.11874 | -54.806 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 238a4eea-514e-3f84-b56d-11af048ff352 | -6.37448 | -55.26344 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ff4f093-d0d3-3bbc-975d-3a2d756f6247 | -2.89293 | -50.42131 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0313b6c-772e-3428-bd6c-e68e2c86b3a5 | -2.69588 | -57.53487 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f51b4a15-a830-3306-97b5-0660cd6787e3 | -6.29576 | -55.28362 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dabb55e2-298c-399d-be72-f6065b4c62a8 | -2.91981 | -50.37718 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97f1204f-d1bf-3918-9d71-aed75434f869 | -2.90196 | -50.42954 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 903efed5-cb0d-3fb5-a2e1-4e6235967cad | -2.90108 | -50.43541 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b4d4ee8b-d19d-378f-b274-5a31c669a3ae | -6.32721 | -60.01646 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d487181-6902-3c1f-b4e0-bd803788fc81 | -6.30693 | -55.27859 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26cab2ea-55b2-3bea-90fc-2f2d078c9a69 | -6.8586 | -55.57026 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9218e054-8b15-3182-8554-547199ae3a13 | -5.80765 | -52.11313 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 992d6f7e-e9b1-30f8-b27d-b0206572c148 | -6.79776 | -58.79324 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 850f306a-416e-3048-8ee6-26b674d7056d | -2.91797 | -50.43722 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 24b8d08c-5198-30e4-a930-069adb213af6 | -6.10702 | -57.8618 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cdd0ef4-e946-3213-90fc-d9bca7407664 | -4.38423 | -55.2005 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19a6601c-eb7d-3351-9d7b-a4d3f261a1c2 | -2.90504 | -50.36357 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e5d686e-7689-342d-a17e-8ec667700e6b | -2.90629 | -50.42345 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| dba60acd-2954-3bf0-bd84-f788010d0fe3 | -3.70618 | -58.8643 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bae6edd0-dca1-3ce9-a567-d80a1380e846 | -6.59742 | -58.8581 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f70261b-dec5-3399-b66d-45a8b110c6c0 | -6.32364 | -59.98825 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83629bb1-7e53-36d2-ab74-6bc623b72854 | -2.89793 | -50.41087 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fed91963-f59f-3b88-80a3-6e548f3debd6 | -6.91713 | -55.63334 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d62d7de-0bd3-3788-b7b7-33dd26257e59 | -3.63742 | -58.62485 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2b5215e-fcac-38be-a4c7-31c3e3599c52 | -2.67511 | -57.54813 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1a554e8-93a3-3ff2-8f28-432a5b8d069c | -2.90593 | -50.35765 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f52cc599-ff43-3f07-bddc-1ebaf4f247e0 | -6.59702 | -58.85501 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1ca91ff-fdf7-3875-8ce7-a18fcfdf1a79 | -6.64801 | -58.82198 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afb1bbb5-0577-3191-a2f7-37266dad6973 | -6.68797 | -59.12585 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aebc11f7-8913-3148-b250-471c14e1330b | -3.80891 | -58.90169 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 117b948d-3628-3e9a-9f3a-4bf0e5b45b54 | -4.55294 | -50.45919 | 2026-09-14 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 984cb160-3363-313e-b0d4-fb0cd20b4619 | -3.38545 | -50.39501 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f48fdf02-73ec-3e3b-a867-28bd6e089554 | -2.91054 | -50.39391 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| db19ccb4-3d8f-3f4e-abb2-6a4f4c4e071a | -3.22742 | -50.59367 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51c0271a-3b53-37e5-a38d-056606355cf9 | -4.55473 | -50.45507 | 2026-09-14 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3f07bb5-197b-30b7-829d-3b49d87bd6a4 | -3.17677 | -61.11616 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f09224e9-84b6-35b8-bafa-86783dfe0d64 | -5.84607 | -52.09324 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 219392c9-12b4-3663-a069-7f950ee74a68 | -6.32119 | -59.97868 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83ff7d1f-b336-3422-b8b1-6a378a3e7f4f | -2.66011 | -57.50714 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6db34c6e-869e-31a2-b157-ba4396610eec | -3.60274 | -59.06599 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 117a28db-abda-3aff-a217-fcfa0b168ade | -2.88377 | -50.38965 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91555111-aa25-34b6-b279-72784f694448 | -6.32112 | -59.97192 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe1674f8-b6a2-3286-a98a-725a3b6ced05 | -5.80065 | -52.11752 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78778cde-78e4-3341-8d8a-423307bbdaed | -6.84846 | -55.56872 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a33774b9-0062-3cae-9cb3-43007e73c5bd | -4.09243 | -54.43481 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c832055-3c0e-3fdd-9ae1-c066c1ef60a5 | -3.45753 | -58.40547 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e9e22c9-e2dc-3df0-a757-d2f9e6e7a352 | -6.01638 | -59.94399 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d069e94b-32bc-3381-9f93-c66529173be1 | -2.74675 | -60.2368 | 2026-09-14 05:36:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebbb9dd7-9cdd-393a-9e97-fe34e5feee30 | -3.3804 | -50.77105 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a68c5634-3840-385b-8934-efd296b2eea0 | -3.37727 | -61.33968 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f455050-20a9-3de7-9a47-00a21eb85092 | -6.1066 | -57.66603 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fc7f0d8-c4b9-3bd9-bdc0-ba97fc3e98ae | -3.11026 | -60.65585 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bdf72a4-8b75-39db-862f-c031fbfe0804 | -3.14589 | -60.63348 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba24f1bc-6930-3c03-85eb-65a7f8c5ef8f | -3.72701 | -61.75719 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485cc4e3-8a10-3d5d-9b2d-f5da2cae1791 | -6.27397 | -59.92749 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beca63b2-22cb-3e27-8e40-f5d50af04ecf | -10.65721 | -54.14447 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 460a381b-f159-3bdc-9b2d-96742170b1a9 | -10.67843 | -54.11665 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60037f1b-1ec0-3787-add5-0640f55778d8 | -10.68122 | -54.15489 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 0e8f0dbe-ff19-3391-935a-9473d57ccb6a | -10.68769 | -54.13955 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README59.md)
