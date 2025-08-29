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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41b45012-85e2-33df-aecc-f11b466b4d4c | -10.3812 | -57.8245 | 2025-08-29 08:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| dcf193b9-f374-32bd-a329-cf41f5722188 | -9.4618 | -60.5682 | 2025-08-29 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 595d962a-0a35-3afc-9cc8-69c1f2389e98 | -9.1155 | -65.7699 | 2025-08-29 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eff661e4-7103-3642-be4d-495ccffd4549 | -10.3624 | -57.8258 | 2025-08-29 08:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ad7d0046-e5f4-3845-9533-def6aed85d5b | -10.3624 | -57.8258 | 2025-08-29 08:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| cb4ce189-7618-3b1c-9300-24b557a886b2 | -9.462 | -60.549 | 2025-08-29 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 759da3e5-8900-3bb2-b9b5-dd18914c05ba | -9.1155 | -65.7699 | 2025-08-29 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fb18b67b-87ad-3cf2-a23a-f79ffb5ada5e | -10.3812 | -57.8245 | 2025-08-29 08:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c40a929d-8585-314e-bcae-a8489d1fbb41 | -9.4618 | -60.5682 | 2025-08-29 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a99fc7c5-5ef3-31f5-8a29-342a92199239 | -9.462 | -60.549 | 2025-08-29 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 542c3548-785d-3edd-9598-337bf98a548c | -10.9705 | -46.949 | 2025-08-29 08:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f82c2a81-28dd-3799-b5b4-2932aa24fb7a | -9.1155 | -65.7699 | 2025-08-29 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6781b070-6f87-3864-a278-55e08734184f | -10.3812 | -57.8245 | 2025-08-29 08:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3783f050-d501-3540-955e-87049a59f9dc | -10.9896 | -46.9466 | 2025-08-29 08:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 301c5eae-ff81-3d01-831f-aad6ebe37800 | -10.3624 | -57.8258 | 2025-08-29 08:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 68cd420e-f3c9-3f1b-9559-2593f0bdba30 | -9.4618 | -60.5682 | 2025-08-29 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| dc9240e1-730c-33f2-a3a3-65c2aa0d6cf2 | -10.3624 | -57.8258 | 2025-08-29 08:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e52720ff-be30-3be8-832c-914f616d27e1 | -9.4618 | -60.5682 | 2025-08-29 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4d2646f3-ed15-3987-b69d-d0456b7a7882 | -9.1155 | -65.7699 | 2025-08-29 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d81964b5-da18-3625-ac78-37d39852e34b | -12.6875 | -48.1899 | 2025-08-29 08:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a056fbdd-92aa-33ef-b76e-926b10375f60 | -10.3624 | -57.8258 | 2025-08-29 08:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9d35af17-d7f7-3926-bfac-8fe68c15929f | -9.4618 | -60.5682 | 2025-08-29 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4f37df33-2dea-34dc-a3e2-80b7c89803be | -9.462 | -60.549 | 2025-08-29 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d3392a58-5965-3968-b636-ea7043eab95e | -9.1155 | -65.7699 | 2025-08-29 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 500b81b3-e7b8-3f66-84ef-4e7f06729967 | -9.4618 | -60.5682 | 2025-08-29 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f1d8f348-2e0f-3634-ac15-e41baf21f533 | -9.462 | -60.549 | 2025-08-29 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2b59cfb1-f605-3978-b210-b8fb2f55d360 | -9.1155 | -65.7699 | 2025-08-29 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 56a5b360-977e-3f12-9da8-e72a7ec18653 | -9.1155 | -65.7699 | 2025-08-29 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0ea387d3-370e-36c7-9dbf-609d79382ed4 | -9.462 | -60.549 | 2025-08-29 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 4677a59c-0bdc-3603-8294-965ae6078203 | -9.4618 | -60.5682 | 2025-08-29 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4018c594-0f1e-33e6-943b-aa024ecb46a2 | -9.462 | -60.549 | 2025-08-29 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5819b8dd-9696-3a84-8d36-a5deee9b951a | -9.1155 | -65.7699 | 2025-08-29 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a1c31b0d-82d8-3d79-8431-26a906ec1057 | -9.4618 | -60.5682 | 2025-08-29 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 011073e3-774e-3de5-80e0-f7df76623842 | -9.1155 | -65.7699 | 2025-08-29 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5e3577fc-bcd2-36fa-964d-8fdbadc5cc87 | -10.9896 | -46.9466 | 2025-08-29 09:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| f623fd42-49d8-3a15-831a-12dcb132f4f0 | -10.9893 | -46.969 | 2025-08-29 09:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| ecc8c142-d66d-31fa-9a88-13ba99c6aee3 | -9.1155 | -65.7699 | 2025-08-29 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6f8c1381-015a-34ea-b57f-4335d8121ba6 | -9.1155 | -65.7699 | 2025-08-29 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ee5f8326-f3e1-31b4-9154-e8ca893d0a9d | -10.9896 | -46.9466 | 2025-08-29 09:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| ef97dd18-ac6b-317e-b201-351796c3e0c0 | -11.3517 | -43.566 | 2025-08-29 10:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 71d4e8c6-c536-34df-8ae5-78f49badcd28 | -11.3517 | -43.566 | 2025-08-29 10:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 19dfa592-77ed-3a2e-bcbe-de1cb1aa16af | -11.3517 | -43.566 | 2025-08-29 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 11e00aab-50ec-3e8f-8796-b90031ed9d1b | -9.462 | -60.549 | 2025-08-29 10:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| e942aab1-9f80-3f77-803d-37b34988db98 | -12.6875 | -48.1899 | 2025-08-29 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 951a77eb-46a8-3e9c-8f9c-d814e63037ea | -11.3517 | -43.566 | 2025-08-29 10:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f3f97867-5fec-33f3-8e77-6582a6e3c84d | -11.5519 | -46.3551 | 2025-08-29 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| b1aec60a-be3c-3ac6-9c3f-b20d023b4cf4 | -11.5707 | -46.3751 | 2025-08-29 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 98bfe319-3683-370a-834c-ca5620b5b772 | -11.3517 | -43.566 | 2025-08-29 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| acb2eae3-e662-3ba5-a73a-78679e99678b | -11.5515 | -46.3778 | 2025-08-29 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| accd4141-a314-3d51-a3ba-8a8fe5bb0748 | -11.5722 | -46.2844 | 2025-08-29 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 45953cac-4860-3a66-9875-5d5bc1e946e0 | -12.8994 | -48.1381 | 2025-08-29 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 12a32788-8088-32fe-93fe-c165e1485dfa | -11.5515 | -46.3778 | 2025-08-29 11:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3197cf16-9911-32ba-8f3e-d37916f4c0c3 | -12.8994 | -48.1381 | 2025-08-29 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| deee71a5-5bbf-35ca-b9ec-f4210d6c0e5e | -11.5722 | -46.2844 | 2025-08-29 11:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 8c8e7505-a020-3542-86ef-6801cc828542 | -11.3517 | -43.566 | 2025-08-29 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 47bcfef9-a529-3032-a259-188972ce5698 | -11.5707 | -46.3751 | 2025-08-29 11:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 264.1 |
| 108b8045-35b3-3093-a000-c12271bfc04a | -11.5519 | -46.3551 | 2025-08-29 11:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| e658a09f-9adb-310f-b683-efd7a274e569 | -11.3513 | -43.5897 | 2025-08-29 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0a1e2c60-837b-3ab6-8a63-ea3b1f81fb72 | -9.5637 | -45.882 | 2025-08-29 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 2b173228-1186-385d-a624-9cdaf97293c6 | -11.5898 | -46.3725 | 2025-08-29 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0afa05b6-f6fe-31ab-a689-4ec465413c80 | -11.5515 | -46.3778 | 2025-08-29 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| c5de2731-78bb-3e1d-b304-ce6c303ed798 | -11.3517 | -43.566 | 2025-08-29 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| cb9c5dfd-3019-311a-8ecf-214eb77b5a5f | -11.3325 | -43.5689 | 2025-08-29 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 48b61cc6-bf3e-3831-98e9-c3f60474733d | -12.8994 | -48.1381 | 2025-08-29 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 9dcef556-3dd2-3abb-b18e-4ec50c3801d9 | -9.564 | -45.8594 | 2025-08-29 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 068b4261-d678-338d-b6a3-3c1b0a2e547a | -11.5722 | -46.2844 | 2025-08-29 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 224.1 |
| d3616870-a0af-3ea6-b6a7-5c68451f906e | -11.5707 | -46.3751 | 2025-08-29 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 558.1 |
| 878debb7-da04-379d-b173-f4bbf8df137e | -11.5519 | -46.3551 | 2025-08-29 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 7256a3f5-a6c2-353c-a47c-b4fb92ea6d0b | -11.5515 | -46.3778 | 2025-08-29 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 8ef9b5db-8fe3-33eb-a9fd-fcce6521d9f4 | -11.3513 | -43.5897 | 2025-08-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8b853f98-3702-3f4a-9ee4-9b2fd9b83f51 | -11.5707 | -46.3751 | 2025-08-29 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 248.0 |
| fff73d1f-0b30-3b19-a531-cce53800015b | -12.9182 | -48.1576 | 2025-08-29 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c257863c-8af7-3ef9-8a76-f09682296d92 | -11.3521 | -43.5423 | 2025-08-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e9f3c117-f66f-348e-a66f-ab74424216cd | -11.5519 | -46.3551 | 2025-08-29 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d98ec4ff-d249-3375-8d1e-63961f680343 | -11.3517 | -43.566 | 2025-08-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 369.1 |
| 2f86fb33-ae83-399f-ba28-6c8eeb6bfddd | -11.3325 | -43.5689 | 2025-08-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a20ae76e-5834-31ef-9346-702ae0217d14 | -12.8994 | -48.1381 | 2025-08-29 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| da8d16b5-92ce-35e6-be8b-3af5545b9760 | -12.9186 | -48.1354 | 2025-08-29 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| cac37718-6167-398f-8665-962632d09bba | -11.5722 | -46.2844 | 2025-08-29 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 23f0590a-c800-3229-92d0-d79ac5334d12 | -6.28808 | -35.47357 | 2025-08-29 11:34:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 02ef038c-e2b7-3811-a645-1489965c670f | -4.13999 | -38.71814 | 2025-08-29 11:34:00 | TERRA_M-M | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 617c7630-e1d2-3292-9355-fc93d3b430db | -6.54386 | -43.92182 | 2025-08-29 11:34:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 65bb42c9-99c0-386b-b118-98067f823ed2 | -5.5989 | -38.28485 | 2025-08-29 11:34:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 863b7f8b-6995-31c2-b354-64d931fb33a5 | -6.51156 | -43.53208 | 2025-08-29 11:34:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 768143fa-9188-347a-b467-8aa94a1ff75d | -6.19273 | -44.00996 | 2025-08-29 11:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d29a288b-5c81-35de-bf45-6de170d4da92 | -6.28682 | -35.48241 | 2025-08-29 11:34:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2c62cfdd-62d3-3ca6-b899-8dac290d449f | -5.78882 | -42.26949 | 2025-08-29 11:34:00 | TERRA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 7ee3499a-ea31-3194-9ac2-4be8f7e1380c | -6.1931 | -44.00434 | 2025-08-29 11:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 81e6e2b1-95e9-362e-9f1a-e0a3b08fd068 | -11.57982 | -46.35695 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 817f0cb5-f42b-3ce3-8517-c2b28f5932a2 | -8.11043 | -44.99901 | 2025-08-29 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1b8e7d91-d47a-3012-b695-042db23028cc | -11.57141 | -46.36216 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 452.7 |
| fd7a304c-ee42-3b91-8937-d6482fc41f73 | -13.55584 | -46.88575 | 2025-08-29 11:36:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 4664a453-a76d-3983-b81d-3b27dde97e4f | -12.90519 | -42.58421 | 2025-08-29 11:36:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 7e422210-b3d3-36a3-ab97-87308374c9e8 | -9.5667 | -45.85956 | 2025-08-29 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 1ed3b6f8-e3f7-30db-a7e8-ea2a788c5d9f | -11.57419 | -46.38971 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| eaf0266f-58dd-3bae-a358-b7f370e21caa | -12.09432 | -44.71867 | 2025-08-29 11:36:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 86e7b4d8-f541-3536-ab90-939fcbb6bcb5 | -11.56394 | -46.35326 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 468.8 |
| bf1c7375-a7fc-327d-a3c0-35b47d02d704 | -11.36119 | -43.56948 | 2025-08-29 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 23f59f8d-6763-3891-8b94-09f8b0a097f5 | -11.56772 | -46.29099 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 413.7 |
| 0263252e-b729-32c4-956e-a610d5efee20 | -8.1056 | -45.00561 | 2025-08-29 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |


[Clique aqui para ver as próximas entradas](README92.md)
