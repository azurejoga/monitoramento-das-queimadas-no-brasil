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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bb0c717-faa5-3cad-9b7d-63ab12b55405 | -14.1628 | -52.9323 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 001e4120-a436-36db-a97b-f369e6af271a | -6.7478 | -59.1716 | 2026-08-18 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 29fe7003-99c5-3ce7-a94c-89c1041ce0b7 | -14.8228 | -46.6419 | 2026-08-18 05:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0cf5590f-6b3a-3022-8509-ed157ef20af5 | -14.8033 | -46.6453 | 2026-08-18 05:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 970dbc93-68be-34d7-996f-8d688ebef5fb | -14.1821 | -52.93 | 2026-08-18 05:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| df9fb1d4-c729-3a0b-8040-28982548b6fe | -6.7478 | -59.1716 | 2026-08-18 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 06346386-85fd-34eb-9121-1fd7e2daf8e9 | -14.1628 | -52.9323 | 2026-08-18 05:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2192a283-3561-3466-91b2-df5df7d381cd | -14.8228 | -46.6419 | 2026-08-18 05:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 148.5 |
| aadde7a1-6cd2-346e-b946-846dde20ea89 | -14.8233 | -46.619 | 2026-08-18 05:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 15001271-c4fd-3b92-bf30-eaa8ff8bb20a | -14.1824 | -52.9089 | 2026-08-18 05:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 3eed3a4b-7ce1-3d64-92db-ee4827f70b77 | -14.1631 | -52.9113 | 2026-08-18 05:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 28101a70-f8a6-3091-96e6-8c77d65a15c3 | -6.841 | -59.0132 | 2026-08-18 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b3e0ab2c-9194-3bd9-9415-3acc4348f7c8 | -8.222 | -55.0418 | 2026-08-18 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 79ab0d21-e118-371b-adca-d2a60c8c6d3b | -14.8033 | -46.6453 | 2026-08-18 05:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9e85b8ea-b561-34f1-96f5-b42207a66678 | 0.30008 | -60.44667 | 2026-08-18 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7610eb45-3ac7-3f98-86e1-8d605467efa1 | 0.87586 | -60.48598 | 2026-08-18 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64d1242f-5804-3570-a7b3-791cc6627ec0 | 2.5583 | -60.30799 | 2026-08-18 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 013fdd48-edd9-3182-83e8-2a0308410ac9 | 0.49463 | -60.59088 | 2026-08-18 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7215c28f-f5e1-3bf1-b017-3edc07e1f68a | 1.67891 | -60.13393 | 2026-08-18 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fa1bea-3218-37a0-a7dd-f0c864ca67dd | -6.87368 | -56.41923 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3856ae81-8c96-312c-ac77-a70b28ab7cc5 | -6.7002 | -58.95105 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b932db4e-b206-364f-b0d5-72a8a397153e | -6.7402 | -59.17675 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc09bc86-9dd3-3c3f-803a-a96c09c550fa | -6.6088 | -58.9626 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 036308bd-cfed-3427-b6cd-3cf5209e98bd | -2.50499 | -56.07903 | 2026-08-18 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 711ac5c1-9412-3621-aec9-9787f840dd07 | -6.85817 | -59.00575 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cd10c43-05b2-344a-93e7-d1478d55cfab | -6.60374 | -58.96629 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d435e95d-20c5-3c13-9835-0fd66eccacd2 | -6.99595 | -59.05038 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a59946b-7b5a-3788-b49f-4999785aaaef | -6.86473 | -56.75984 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 896eac64-f5cb-356f-b4c4-0e60a82e7911 | -6.74635 | -59.1647 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 13c2bbe4-78f7-3f04-babd-ddbe5515fa69 | -6.77052 | -59.46326 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb764f19-783a-3738-9ced-d05682a73fff | -7.37567 | -55.49268 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3468b8fe-1cfc-364d-bd8f-9f54b5a82d62 | -3.20846 | -61.47446 | 2026-08-18 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab821884-7d93-3b4b-ad15-ea2ddca39b55 | -6.75253 | -59.15257 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3ed2afe-5c43-38a4-89c5-269dc997467d | -4.2088 | -59.99145 | 2026-08-18 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aa2e022-38d8-3d4a-8456-aab432b7da4f | -6.10808 | -57.73127 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4246ec3d-8560-3dea-b2a8-790790b412da | -7.38806 | -55.48665 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba2198d-1d0c-39ba-9de5-97ce52245886 | -6.84158 | -59.00173 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10a1465e-eeba-3024-ac33-4dc6441b60ab | -6.75388 | -59.17495 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a89cfaa2-e9e9-3021-bde4-4fabaf96a891 | -6.76623 | -59.46255 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224b3d13-3a01-3651-9e23-071932fc9b13 | -6.10734 | -57.73658 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f55233f-2b7e-3a69-9a4f-76233f630e3e | -6.7396 | -59.18103 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c496db-9488-35dc-9c23-c53d10f37e83 | -6.39885 | -54.95007 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05d1a7a9-7523-3235-b81f-a73ca7f0b228 | -6.84667 | -58.99792 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 66380ed7-07bf-33e7-a81f-eaca5ae2f2a9 | -6.74376 | -59.15106 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad1f22d1-8df5-314b-87dc-e0ba0566a13c | -6.74576 | -59.16895 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4ad5e310-6ac4-372c-9ae6-c73e7cb13fac | -6.8524 | -58.98969 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3122b8bb-5754-3e9a-a191-b864543b8d0a | -6.75132 | -59.16124 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2f0c4589-0deb-368e-b1db-cbbff2b55fce | -6.75012 | -59.16983 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f627706e-877e-3a3d-b86f-25de4b4f6bda | -6.77542 | -59.45978 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df57ccf9-8af2-34b2-aed3-da8dc786ec3a | -6.43545 | -54.94263 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 321c92b4-8c95-3652-b51a-20c99fffc9ee | -6.74894 | -59.17831 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 276871e7-d118-34b3-afc3-2c99b8228c87 | -6.61018 | -58.39481 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3da8881d-c368-39d0-80a7-e22c3781e505 | -6.96284 | -59.02748 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 773b93c0-51b1-33dd-aab3-7a038dd1e74c | -6.85177 | -58.99409 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca99721f-0a24-38d2-9016-a8f9cca2103d | -6.63267 | -59.07845 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cff739c-5db8-3124-b1f2-8d5329fb8772 | -6.75072 | -59.16555 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eaa8d04a-666f-37af-ae81-719e4d5968ef | -6.73911 | -59.18203 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f42a33-d01e-3615-8fc9-a5741cf7921f | -5.14576 | -56.27905 | 2026-08-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a271ba-c521-3508-af49-fa0e69e6590c | -7.39996 | -55.48442 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c30aa42e-1fd3-333d-84bc-ff5f930b676e | -6.74953 | -59.17407 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b00c751f-7e52-3cfc-a7ef-87e73da5d19e | -6.73974 | -59.17778 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbc4f5c7-a76a-3ab7-804f-6aa154482482 | -6.99656 | -59.046 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 244e1ae9-9049-351c-ad70-c1168bed24d1 | -6.3994 | -54.94596 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03ec4431-6b4b-3903-bbbc-738d78b3c6ed | -6.88006 | -58.9458 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a83e8a3d-d336-36ed-858d-cec46add218a | -6.73938 | -59.15035 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5341aa70-f475-359f-8212-f5471b7193d1 | -7.53928 | -55.58596 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ecb3942-f536-38d3-8e3c-4b8b89ce85ec | -6.75329 | -59.17917 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| abb93220-882e-36f8-9e9f-98317e8acfd1 | -6.76011 | -59.16246 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d62ed519-295a-3634-8756-b35407451b5e | -6.85113 | -58.99852 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 129a4a9f-31f8-3415-8fe5-ceee91d364cc | -6.96162 | -59.03633 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ddcef41-5a0f-3150-af1c-bc6658d9fd6b | -6.99717 | -59.0416 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be4a2977-6954-353b-844b-57dee9cb6b9f | -7.39944 | -55.48833 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba4a7b2d-11ea-3fe9-8c71-c1d09d039599 | -6.99151 | -59.04972 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46486ebb-88b5-3b3c-89bb-cee7b19b63e4 | -6.44128 | -54.94344 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8d3344d-2af3-303c-92f7-7948f95d4ec9 | -6.85301 | -59.01683 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7b9dc531-7778-3929-a613-a65ea315660b | -6.84919 | -59.01192 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42163ba2-19ab-38b7-8785-2f6eb41e181a | -6.77171 | -59.45507 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 898cb6e9-97eb-3b5f-99bb-39c11ab2a1e6 | -6.02875 | -57.80844 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 338a1805-e325-3143-8f14-5c47fef3492b | -7.39479 | -55.47966 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21648215-eebe-3b7f-95d9-7260082b85e8 | -6.74349 | -59.15217 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20f574fd-fa3c-3aac-83e4-232facb34c2b | -6.85558 | -58.99914 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6c52ad8-4771-3d47-bbcb-e07723e2f73c | -6.77954 | -59.76074 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a621d13-d0ff-3364-af6c-28e3140cdb99 | -6.65129 | -58.95129 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2cea1c9-2ff6-3646-8fc3-f05882a4e54d | -6.96298 | -59.03458 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79320c15-96e9-39a9-8ac7-7145153f4787 | -5.14621 | -56.27582 | 2026-08-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca4db211-a305-3436-8f5c-896933d93809 | -6.84983 | -59.00748 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 22f79bca-bc6a-31cb-9467-b27fb091cf91 | -6.71612 | -58.93502 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8266f03-947e-3a9b-923a-7a6d60204844 | -6.59595 | -59.11531 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf2a6d1-1bf2-3c8a-ac9f-577beb1109fa | -6.40633 | -54.93862 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee6e4771-0c56-32d8-a82f-4b804e540e2a | -6.78643 | -59.44456 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bcc4179-3e64-3daa-9bdd-4611e99ca91d | -2.50036 | -56.07518 | 2026-08-18 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0730e20f-54a9-3249-b3a4-b39aaa475546 | -7.37 | -55.49175 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc847c0-fa64-38af-aeb7-972754f6be99 | -6.79443 | -59.45002 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b1ffb3e-0a16-3891-9a87-e2842def89d9 | -6.75192 | -59.15691 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be18b252-add7-3cd4-992e-cae1afa2f544 | -6.7053 | -58.94719 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9883c3a8-d412-39ce-ba5f-db34046adfae | -6.63327 | -59.07413 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd7d21d-4ebd-3f97-9187-f272133e41d1 | -7.38186 | -55.48968 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bd65a6-fd9e-3dec-97ff-84662d3f5d38 | -6.84731 | -58.99348 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e490606d-557c-3351-ab25-4c9c230bdcaf | -6.96171 | -59.0434 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c279af7-5f80-3b64-be31-96a5ed984e4e | -6.74835 | -59.18252 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README53.md)
