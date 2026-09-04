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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ffd781-b3fe-3f58-871a-1abf7e6f2742 | -11.34651 | -61.55165 | 2026-09-04 05:25:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9718d6c2-a3b2-3f45-9476-328835ea7d5a | -8.9912 | -67.02361 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37feb46d-f2fc-35c0-9d2a-9ee4df6d4db7 | -8.8182 | -68.67429 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b307d55-ddc9-332a-93de-89b8cc4abe25 | -10.28792 | -68.8453 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51348ffd-11ee-3cf6-bdd5-ee58cf021398 | -12.01024 | -60.52466 | 2026-09-04 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ca9b47-9e56-3c5a-9ead-d6e2a0e24b65 | -8.98803 | -65.38789 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff2806f2-bc65-34ef-898b-9ddd9d2cbdf1 | -10.32088 | -59.14373 | 2026-09-04 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931da12e-b6ed-3e17-9224-2a637d543272 | -10.28615 | -68.85512 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d57e90a7-9b58-3f31-b321-c88e0ac67b0c | -6.15653 | -57.75743 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d35e298-d2d5-310a-a184-d47b4a6d972c | -9.04242 | -65.74332 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fa0bb53-c421-3aa6-8aa7-f42e191417af | -8.70767 | -69.99966 | 2026-09-04 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2613068f-eb08-3859-acc2-ff4277c8ee50 | -3.97694 | -60.0309 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 536faf59-856d-352f-bcb2-68550158c5b7 | -8.66914 | -66.94944 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30057c7d-e35b-3cdc-9841-e2af3d2b72d8 | -13.30814 | -61.10125 | 2026-09-04 05:25:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01b454df-3d02-3b6d-abc3-a31a894d89ab | -9.576 | -64.293 | 2026-09-04 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 80314c77-e704-39c8-befd-7fbe66fca71f | -3.75648 | -61.75969 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1cd97f44-3937-3d5a-b7aa-3a6cc6e9b034 | -6.15947 | -57.76204 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468f38d6-3975-3521-94d4-8a127cbb664f | -18.13484 | -51.79842 | 2026-09-04 05:25:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03fa7071-dc5b-3476-9233-673c1f64583f | -3.76152 | -59.31453 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf8fe972-ee12-38b6-a41b-33e3379ff3fe | -8.59609 | -67.17022 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91f3bd0a-a1a1-37c7-bb7e-9dce8f014f5c | -4.2942 | -59.95669 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97be2bed-84e9-3ca9-ac67-c6fe200355cf | -3.78136 | -61.75612 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fcf7c7a-1008-3fdd-8ce8-b3f491331e17 | -7.88495 | -71.73766 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b25763e-d188-339e-b88c-231e161d913d | -8.87497 | -66.67059 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 195614dc-469f-3392-9477-3a015d218f72 | -17.09886 | -56.85905 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5cac9e21-b606-388a-a675-87880ce4d619 | -6.12533 | -57.69885 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a372cf-5d51-392c-ac18-4b969e9d5348 | -3.7588 | -61.27159 | 2026-09-04 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11d516c1-ef3e-382e-8fde-eac429a480da | -7.88022 | -71.763 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c699cb5f-477f-396d-8a3f-7d561eaf83d0 | -3.75706 | -61.75606 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c983087-918c-3148-8aff-22fef4666989 | -4.35453 | -55.03936 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 602bdac7-c241-3844-8958-f7aecce69778 | -5.56681 | -60.17036 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b6f4c96-5b73-39c0-8698-70e7320c962b | -11.22585 | -53.98071 | 2026-09-04 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ce1bd98-d24f-3fae-b7e4-b8ccd6eeaafc | -10.19894 | -69.08975 | 2026-09-04 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c3c8e39-b5f5-3625-a59d-ad9f4f8a6382 | -3.61683 | -60.57034 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b987c7d-654e-36cd-800c-82ee4e9ca0aa | -9.53635 | -63.5613 | 2026-09-04 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b94a8f8-233f-36ef-838e-94a98acd5e41 | -11.14082 | -62.84012 | 2026-09-04 05:25:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d61fd6a6-ceb8-3433-b2e4-8556f97f8923 | -3.62014 | -60.57085 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a0219de-7c00-3e37-a744-2ba42e1c4606 | -17.10664 | -56.84495 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f29b5011-8911-31d0-8c00-1e2b7e871c4d | -5.5635 | -60.16985 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6816c5b-2f96-3038-bfe6-c8a02c7554e7 | -8.87525 | -68.61006 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fc4dc66-c9ef-3e55-b834-39ee6c5bd517 | -9.64923 | -68.61337 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7de82621-abe8-333b-8f33-1ff50e7898ba | -5.77192 | -59.17196 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39761578-006d-38a0-89d3-295fac64a201 | -6.31174 | -56.03955 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61eb4be0-1e32-34b3-94f6-320de1e0924c | -6.31099 | -56.04454 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e3797f-9a1b-3ea1-a60d-460a19b2cce3 | -3.38995 | -61.32287 | 2026-09-04 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0133b323-1c6a-33f9-99f6-067e90e74f2c | -3.20035 | -61.23174 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d8e35a8-5064-3642-8394-a2f27652d513 | -4.47956 | -55.40767 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ad5331-61a0-329d-9f79-490e382a6992 | -10.45473 | -61.20879 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 238e8699-8723-319d-9679-85f4e2e4c6c1 | -17.10374 | -56.85536 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7619ee49-5a96-31f2-b7b6-630c625f7f1d | -17.08805 | -56.8401 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6761651e-e769-3412-aefc-2a4594a378fe | -11.94662 | -55.91753 | 2026-09-04 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50249bc2-dcdd-30a7-993f-cef753ffbfd0 | -10.45142 | -61.20827 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f27e45-30b6-320d-8a15-327f0bfb7b00 | -17.0959 | -56.86092 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7eaeaaed-3972-3072-8b74-c30af4f5efca | -11.50367 | -61.37185 | 2026-09-04 05:25:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1eb1da3-2667-3c08-aa70-a54751f93f87 | -6.14941 | -57.75643 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b1f437-ac73-3aeb-9820-7844756ea92b | -11.52186 | -58.51473 | 2026-09-04 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2960e89b-ebeb-3df5-b11d-33115b7aace1 | -8.60323 | -67.17975 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 80af0b25-5a13-3cee-9fef-8ef1d0f5c130 | -11.38714 | -58.33476 | 2026-09-04 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e9cd607-63e9-3fb3-9f3e-6e75b23fc481 | -15.90715 | -50.16329 | 2026-09-04 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea48f22c-0ef6-3dcb-809c-4dc916e5ca24 | -4.69239 | -56.06248 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7208606c-4964-3bc0-a8d8-d2aa6c84020f | -3.78323 | -58.84622 | 2026-09-04 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1972e536-8ad4-3bf9-889b-70224dfd7742 | -6.14879 | -57.76044 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6a7a61-03a8-3c8f-bc20-56534f0e06ce | -8.92539 | -69.47392 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abc3a5a8-1961-3bd3-8ba9-e08fb8ce637d | -8.60253 | -67.1838 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 99b986cb-59b7-3c36-8de2-014a4a6c2e93 | -5.14749 | -60.30958 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d01e85b-f436-3df1-8f38-2bcc1baffe03 | -8.59825 | -67.18307 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e4b4bb2-64bf-316d-bc3b-86aaa222c607 | -11.07903 | -60.70575 | 2026-09-04 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5737c0c6-256f-3dd0-a4fb-684abdc17117 | -5.3274 | -60.13618 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1e3ed7c-32fb-3716-b63a-fe8eb4a71bb4 | -9.04781 | -65.74254 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dd2722f-004c-3fab-9c36-c1ac178c1717 | -15.90889 | -50.15944 | 2026-09-04 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bea895fe-dcfc-3081-b014-43f11a51421f | -5.33017 | -60.14015 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f81be495-f6d4-3daf-935f-223ecc5be062 | -3.43485 | -60.40709 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b78d50c-1605-3575-a8a2-dea3468e2a66 | -8.87758 | -68.4994 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46f0af2f-4102-31e8-b67a-fc66478a84a5 | -4.09962 | -60.66008 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8c0964c-7a9a-3c92-ac5b-bc9ec55c0f79 | -4.14882 | -60.69247 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cdba68d3-f4b8-31d9-add0-a88ff8af1499 | -5.55966 | -60.17279 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1c136ac-7f14-3ba8-b682-d1962d8b2085 | -17.09996 | -56.85048 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 881f16a5-7d34-3850-86a2-53a15d208c4e | -3.78268 | -58.84976 | 2026-09-04 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef66f1e8-115c-35e9-a229-546d2296ff7a | -17.09832 | -56.86333 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a76ccaad-dad6-31b0-883e-4f1846b83f2d | -3.45707 | -59.74143 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9ce89c-ad60-3961-b880-18e93a7dd2e9 | -8.87628 | -68.49766 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46505440-12df-3326-a6f2-4e1ebf1fa311 | -7.87598 | -71.7598 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f20475a2-7cb1-339d-a2af-2ac49eeba742 | -8.86464 | -68.85979 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8288e6-d5c4-3c30-953b-b1e7cf4b2aeb | -17.10429 | -56.85108 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0b02a67a-4687-3733-bd65-4796b465de24 | -8.8057 | -69.02293 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 577249ce-5085-3039-8940-48e177604d18 | -3.61568 | -60.55602 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ba15a45-5f9b-3ccf-af42-3a670211e7a7 | -4.48892 | -55.08658 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9c279c6-417c-3963-8d8c-83d1684d9ad2 | -3.9105 | -59.60366 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a759beb9-e68f-3e1f-9050-8bfc200019fe | -9.04478 | -65.73698 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f1fdc5e-8b9a-3681-a917-89017d135f3c | -9.02502 | -65.44468 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1e84787-a7f0-3f08-a537-3d0442c0f966 | -9.1726 | -65.55798 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525c37fa-6902-38f8-bb5d-1ec38a1c590f | -8.87272 | -68.61123 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3de098a7-764f-3d17-84d3-38bf43dc1185 | -4.24189 | -62.2422 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4be78d8-4b33-3a42-b594-9f220911cbc6 | -9.03242 | -65.73166 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aea739b-c66f-33ce-a635-d8a686596d0f | -10.20368 | -69.09053 | 2026-09-04 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f17872bd-f497-3ad1-ae37-d5db335ebf0d | -11.51519 | -58.50936 | 2026-09-04 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b521bc9-c2a4-3bda-bffc-6e31f7f2a833 | -17.0992 | -56.87011 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7d935670-39de-3437-bdf0-658cfdfc1ba4 | -9.17713 | -68.26941 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20fc87ef-07b0-31ff-a728-1d9b9f434670 | -5.77473 | -59.17606 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318985aa-bf72-384c-94e0-a8c69e1aafb4 | -10.64402 | -61.76156 | 2026-09-04 05:25:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
