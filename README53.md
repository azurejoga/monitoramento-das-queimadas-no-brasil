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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4444c9bb-b1d3-3fec-9d3f-6aba65327771 | -12.80981 | -48.57634 | 2024-11-22 04:38:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc983fe8-2bce-3131-bb92-c488c8fe8a45 | -7.71194 | -45.66281 | 2024-11-22 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0279491-ff24-39bc-8e48-185ed87314b2 | -7.65156 | -44.50066 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa0814d5-3a4b-382a-81ec-df9a2bcb7a21 | -13.86851 | -42.91934 | 2024-11-22 04:38:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fbaf2ad3-881c-388f-b710-f6e45d5cd5ec | -7.02979 | -47.64192 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bffda180-4182-30a5-b61c-b006afbe52fd | -12.18461 | -41.34847 | 2024-11-22 04:38:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8767f256-4c08-36f1-8d46-68be53fcbddd | -9.16941 | -43.16562 | 2024-11-22 04:38:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5c49717-64f3-33fc-9292-5589bdf73d86 | -13.24946 | -50.88551 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c4817e6-bb19-3ebd-9663-a5b3745c0b50 | -6.03375 | -49.79109 | 2024-11-22 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09e927b5-dc03-3ca8-beb3-ab8aed0d6eb4 | -11.53634 | -51.27918 | 2024-11-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9adfaff9-bac3-3e46-943d-bb80096404ea | -12.33833 | -49.99947 | 2024-11-22 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91c8a9a2-2cb3-3195-8f03-d5dddc478b40 | -7.59572 | -45.26477 | 2024-11-22 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6c1fce-a4d5-337d-aa7f-2a3359a402e1 | -7.03434 | -47.63498 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09a99db5-31f8-35c0-bca9-e5baad24d50c | -12.18413 | -41.35231 | 2024-11-22 04:38:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e535b7b-3efb-335c-be2b-dc470d976837 | -10.6549 | -48.1068 | 2024-11-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 463f015b-7569-3dd9-b36e-75b7f1eb3a28 | -7.28991 | -45.08249 | 2024-11-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ef9e573-4132-3834-93a9-6f2102a27af6 | -13.25497 | -50.89365 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6d50cf79-842c-340a-8164-bca78632fbc0 | -11.73853 | -47.23822 | 2024-11-22 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3e882a5-6bdb-3e89-b05f-3e19ab759b5d | -13.24284 | -50.88443 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c6ca3ed-5968-3529-bba7-75a75e2d3ef9 | -7.71572 | -45.66337 | 2024-11-22 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b62983a-e8d4-3fb2-a85a-d2e3a60fabc0 | -9.16913 | -43.1633 | 2024-11-22 04:38:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8bbb3987-5513-3948-82ff-289e45da287b | -8.72596 | -44.02182 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef964b84-274b-3b0a-8e34-668e8f13e8af | -12.65371 | -48.82391 | 2024-11-22 04:38:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d241117c-dd51-3a4a-99c2-d5c19ec41c66 | -10.73367 | -49.53274 | 2024-11-22 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 614b5545-8941-3c69-a5c6-7fb14319a2ea | -13.16821 | -50.99245 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38d01a45-a808-31b8-b270-0a5e4c663e6d | -12.77645 | -49.30951 | 2024-11-22 04:38:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d9a81b-88c5-3bae-9d00-b922d8e54e17 | -9.30048 | -43.12947 | 2024-11-22 04:38:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6839e3f-0286-361e-b926-442565bf7fff | -11.86326 | -52.34908 | 2024-11-22 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d5f14e4-b296-3488-9c08-392168c74a1f | -11.37099 | -57.57557 | 2024-11-22 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c75a3b35-207f-30ac-8181-943e3c838224 | -7.00422 | -45.61309 | 2024-11-22 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 612a4bd3-6159-3005-95d3-ca69dff0b81c | -7.73905 | -38.61323 | 2024-11-22 04:38:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 945d14bf-355d-379b-9ee3-d733714bb425 | -8.39151 | -48.05721 | 2024-11-22 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5aa6f66-401a-35e8-8e5f-7578fd997e75 | -7.6673 | -44.50665 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 320ca193-1d81-35f8-9f2f-33205e993e52 | -8.92721 | -44.24996 | 2024-11-22 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e808fee2-0f93-398a-ba5d-ab6e27dc1103 | -11.51184 | -48.12755 | 2024-11-22 04:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594dc826-9a02-3d5b-9e29-1de1ce1786c5 | -11.37013 | -57.58027 | 2024-11-22 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e511b6fd-f6cc-3809-a5a6-6e022ebbbe9f | -8.7231 | -44.01799 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deef8f2d-551c-3430-baca-7c578338c62d | -7.59643 | -45.25982 | 2024-11-22 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3952cd7c-7f02-3f86-b3c5-53718cd740de | -7.03035 | -47.63823 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 748e510b-4bca-356f-b4ba-6d51b0771331 | -9.16612 | -43.15552 | 2024-11-22 04:38:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35b6258c-37ae-32cf-9be0-28dcb49aab48 | -7.03378 | -47.6387 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaca495-3ff5-3d6b-9f0d-d18df460f24b | -7.21799 | -45.07931 | 2024-11-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a0a3561-0c06-3b99-92a6-5cee7aede5ed | -12.42568 | -46.63774 | 2024-11-22 04:38:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68913e2b-1363-3f7b-8a55-f7ade1040504 | -11.73791 | -47.24255 | 2024-11-22 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f75219fe-a795-30e0-9273-d19b3cafcca5 | -12.44507 | -46.66473 | 2024-11-22 04:38:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c778639-33c4-3600-a249-2705717097ec | -8.72278 | -44.01329 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc7c8db3-90fb-3aad-8372-c6a9a9434b4f | -13.24615 | -50.88497 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9400ac3a-5ac5-3a47-b99d-45c9bb85ff0b | -12.01057 | -47.46791 | 2024-11-22 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bdd46f-4eb6-3e20-a1fd-24967230abca | -12.18711 | -41.34883 | 2024-11-22 04:38:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7bc02df4-b599-3a9d-b334-f936aabd05ab | -10.73312 | -49.53628 | 2024-11-22 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e9b8d44-c824-35cd-bec1-44ebcd78a773 | -7.03148 | -47.63079 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b9d03af-9a37-37db-90d2-3d408bc72be2 | -7.65103 | -44.5043 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c537a567-d866-39d7-809c-ecfdd3b87946 | -8.72367 | -44.01405 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ad362f6-243d-3a85-8357-e5bd89b68297 | -13.24891 | -50.88905 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68dd9422-ff8a-3a88-bf01-88c5d2f7ae14 | -11.36559 | -57.57929 | 2024-11-22 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d12492f-d359-3198-b8d5-005051aef6fd | -13.2456 | -50.8885 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7e6c0a-a54c-3086-aa69-771049be923c | -7.65563 | -44.50124 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c36be40b-175a-3227-9caa-a6b161a43393 | -8.93142 | -44.25062 | 2024-11-22 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b3a8088-0efa-3228-999b-9661c24d4724 | -8.93088 | -44.25449 | 2024-11-22 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71493fbd-550e-3244-8bf4-d0bd79f8ecf4 | -13.17263 | -50.98593 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f9e920a-93a8-3271-bf33-a722ca963183 | -6.92002 | -46.10837 | 2024-11-22 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52382794-d494-3ef4-9115-80b1100306eb | -8.92667 | -44.25382 | 2024-11-22 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 863766d6-03d4-39df-9057-622e91235026 | -7.65509 | -44.50489 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afaa0fed-476a-36a8-b77a-a057889c9ce8 | -8.93509 | -44.25512 | 2024-11-22 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81bbded3-dd92-36e7-abea-e2dbe12e1c17 | -11.85986 | -52.34851 | 2024-11-22 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9709d139-197b-35b2-9181-41d52d2896b7 | -8.39435 | -48.06148 | 2024-11-22 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f290f9fa-2d38-3b9d-be67-d8cbe53d6502 | -13.25222 | -50.88958 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac0576d3-aed2-39ca-82f9-7fbfb1f9423d | -13.25387 | -50.90072 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48316295-53e6-3beb-8026-e861f823441e | -8.7217 | -44.02117 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56343308-0f1d-3d44-8624-33da3fbf1958 | -11.86047 | -52.34479 | 2024-11-22 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d814dde-25a0-3f72-b5cb-08ac6604d2ea | -8.71144 | -44.00827 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2005dbdd-e411-3825-af8c-5f8cf62df16c | -8.72679 | -44.02258 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e8a913-7f77-3793-a7c1-b223ba1e36a2 | -9.16125 | -44.30256 | 2024-11-22 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c2b7a4c-09e1-3ee8-b646-d7df913728ba | -13.25166 | -50.89312 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7a91c6b-8a47-3ee8-bf49-9871a651f5cf | -7.66676 | -44.51029 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af00b92e-efa4-376e-b113-0d2eb0754372 | -8.72224 | -44.01723 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9028fe7f-16dc-343e-aafd-669cebe12cbb | -6.8167 | -46.77979 | 2024-11-22 04:38:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fee9149d-35e8-36be-b125-d7dfffc44fca | -6.79205 | -47.38903 | 2024-11-22 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f2d2fb9-f011-3a98-9af7-5cbf626b9e44 | -12.34111 | -50.00356 | 2024-11-22 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efabf747-c1fc-39f8-af7a-ca7f1ce80f23 | -10.90894 | -51.78255 | 2024-11-22 04:38:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18348bc6-6e77-372d-902e-9d06701efe78 | -10.87644 | -51.94174 | 2024-11-22 04:38:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8109189-e0b9-381a-9bf3-c0674a264ef0 | -12.77701 | -49.30582 | 2024-11-22 04:38:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa5029bd-17c5-319c-80b5-08c0a8656fe0 | -10.72489 | -49.0363 | 2024-11-22 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ed23ab-7ac6-3165-81d5-0f4f93be5545 | -6.92303 | -46.1133 | 2024-11-22 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a99ddc-fa61-3414-ac94-e1e0e6167645 | -6.81729 | -46.77583 | 2024-11-22 04:38:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2fbbb649-8f80-34c1-b359-08fe8110bee1 | -13.11199 | -50.11164 | 2024-11-22 04:38:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a9af0c2-fe92-3019-80ac-a765d430ec2d | -7.66784 | -44.50299 | 2024-11-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eadea0cb-f8d3-34ce-92c7-84bc42e40473 | -7.03091 | -47.63452 | 2024-11-22 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5c096a4-69b2-382d-bf8d-7005f746949a | -6.4363 | -55.5889 | 2024-11-22 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f602772d-0a90-3d90-ae33-7aadbdfb414b | -13.10262 | -43.32106 | 2024-11-22 04:38:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 626c7bee-4622-37ee-8372-089b7d03e153 | -8.72253 | -44.02193 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 170ae07a-e0f3-3bd8-9eff-c8c015b62857 | -3.2569 | -54.2426 | 2024-11-22 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 430a99db-f46a-399a-96e0-b367eed7af5a | -3.2386 | -54.223 | 2024-11-22 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b4af6e00-a3d1-3e1f-aeed-f64fbf090361 | -1.2041 | -51.9478 | 2024-11-22 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9177ce3b-5dd4-3998-9188-04692a13138d | -3.22 | -54.2636 | 2024-11-22 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f4358000-e728-3795-a7e7-89a085f00a01 | -3.3452 | -50.4917 | 2024-11-22 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 524515b7-351f-3825-8f68-f9be08c644b0 | -3.2201 | -54.2436 | 2024-11-22 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| daefeca6-066c-3a82-9aff-486f574a112c | -1.1287 | -53.3951 | 2024-11-22 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b624d173-456c-39c6-97a5-22d98781dcaf | -3.8535 | -52.3596 | 2024-11-22 04:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0f29a83b-a71d-3b47-bf3d-1938e6b24739 | -3.3451 | -50.5126 | 2024-11-22 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |


[Clique aqui para ver as próximas entradas](README54.md)
