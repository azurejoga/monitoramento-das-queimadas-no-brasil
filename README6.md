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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4aec85f-43f3-3c19-9518-bb5194da1d9b | -6.9422 | -44.5562 | 2025-08-14 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 60fbec3f-01e0-3df1-a17b-5fc859b45d10 | -7.8775 | -61.8063 | 2025-08-14 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 663c37dd-050a-3b61-91d8-c9a16625ae5b | -14.485 | -46.0586 | 2025-08-14 01:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b1aa9bcb-f5dc-3f56-961a-342803fff0a3 | -9.553 | -40.3503 | 2025-08-14 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 2c301aff-8001-385d-84df-fbcbd73d6a86 | -8.5211 | -43.3063 | 2025-08-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 20835601-2a65-3922-9c05-ee4d6cc55bef | -8.5208 | -43.3298 | 2025-08-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 7197df67-38fe-3db2-82a1-3dc322a13f67 | -7.8775 | -61.8063 | 2025-08-14 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8d09bdfb-d82a-3a08-b6ac-701dea54a1e4 | -7.8774 | -61.8253 | 2025-08-14 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 7b593ceb-7d64-3645-9024-e0a24966a0e9 | -6.0807 | -59.9465 | 2025-08-14 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4ca4da1d-6cbb-35d9-bb5a-3bc76e683363 | -7.6103 | -63.516 | 2025-08-14 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 35e068b6-009e-3d1c-8033-511dd33e1f1a | -6.0991 | -59.9459 | 2025-08-14 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c44b1e7d-cb22-3079-9de9-58b4d22705c6 | -9.1522 | -59.6578 | 2025-08-14 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9e8e967d-e809-34ed-aeb2-133c5fa55fb8 | -5.9899 | -44.1528 | 2025-08-14 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cf39646c-41f7-3f3d-8107-d93be58d5f1f | -7.6287 | -63.5154 | 2025-08-14 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 9547547c-b32e-30a9-a1ad-076d9ddc20ce | -9.152 | -59.6772 | 2025-08-14 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 37993fc5-5b18-3816-a194-261b37a0be29 | -6.0992 | -59.9267 | 2025-08-14 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ffcd999c-87bc-3e5f-9eb2-1e0b5440cc8b | -9.553 | -40.3503 | 2025-08-14 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 262.4 |
| a93c7efc-aa55-31ff-b338-f6f006b8bb00 | -7.6103 | -63.516 | 2025-08-14 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 9a6c648b-0bf1-3cfc-a1f2-77e9ccd0111a | -8.5211 | -43.3063 | 2025-08-14 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5ff153ba-3972-3d7c-869a-006851e51667 | -6.0992 | -59.9267 | 2025-08-14 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 02ac4819-c107-3a84-a284-7ab7bddce564 | -9.5721 | -40.3475 | 2025-08-14 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.9 |
| ad9180e3-1921-3fed-8866-e58c375204de | -6.0807 | -59.9465 | 2025-08-14 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d951f739-79aa-3d7f-a15b-bf585e369ad6 | -7.8774 | -61.8253 | 2025-08-14 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 73b5c10e-13f4-32a7-9dea-faee7953e39b | -6.0991 | -59.9459 | 2025-08-14 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 2c3f2f20-4036-39cb-a831-48ea33a8c354 | -7.8775 | -61.8063 | 2025-08-14 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 30e725c3-f4fd-38aa-b5eb-f02af007c91f | -9.1522 | -59.6578 | 2025-08-14 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0554e28e-df58-31b1-a20b-9b93a73621a1 | -9.5526 | -40.3752 | 2025-08-14 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 1babeade-496f-33ef-bc00-4097e0dde42c | -8.0939 | -61.187901 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 318d0fd2-d91f-3513-920e-56e414bc6ae2 | -6.0705 | -59.9263 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53310c64-cb97-34f8-8267-7d87f7663ab3 | -6.0943 | -59.939499 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04e04fc4-403a-3fc7-b8c2-6f7a67d18a6a | -7.8735 | -61.810501 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 880923ee-0dbf-3d23-8172-b1fd79bbb95b | -7.1172 | -59.631001 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d790d526-ce73-3860-b4c2-793b5d3bd3ca | -7.5237 | -61.384602 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a515314-8575-3cbb-b27a-0d7ea773b893 | -7.8832 | -61.808201 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e93130a-393f-325a-bfbb-52852a5887ce | -6.9093 | -59.161598 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da875221-ff69-3727-b2f0-8f1ffb94365f | -6.0846 | -59.941799 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cba5caac-9a79-3666-9d1c-3b42f0372f42 | -6.8754 | -59.149101 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34f0a96f-d36d-37c0-b2c0-f0661e817a8e | -9.4949 | -60.5126 | 2025-08-14 01:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b64e259f-c83a-3502-9cef-ce199a05c9d8 | -8.1003 | -61.171799 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c770401f-9354-3b51-937e-debc3a6098a7 | -7.8638 | -61.812901 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d76a5c89-7508-322b-9857-4fbc8b7227e3 | -8.0972 | -61.201599 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74a3d7fe-b241-36f4-ae60-f0db243f9e2e | -7.257 | -60.623402 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da89afef-e673-3f6c-a8f5-8b9ef7d53f30 | -6.9238 | -59.137001 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42de04d8-98f7-30c8-87d3-b35381bdedf8 | -8.1069 | -61.1992 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba0915ca-89b3-3c3c-8d9a-6158fec86105 | -9.1733 | -59.6703 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0f974ac-a55f-3e18-8d87-d891b18c704b | -9.1497 | -59.658501 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68934459-b3ab-334b-9608-8e1aa5672613 | -7.8765 | -61.823101 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2be7e6a5-601d-38b1-8390-a819a01301b6 | -9.1829 | -59.6679 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b567ff7-663e-3640-afbe-815754f85f81 | -9.3768 | -67.759201 | 2025-08-14 01:31:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c890fa7-571a-3faa-bb0f-85b9eb54debf | -6.0899 | -59.9216 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cef027e-0377-3e00-8928-062b393b894c | -7.8668 | -61.825401 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 339e2b73-6585-3906-b42f-7fed0efaf184 | -6.8899 | -59.1245 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffa40002-dfea-3195-8da9-3b9cbf4d52a9 | -7.1218 | -60.110901 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd027290-1b6e-34eb-960b-15de12a522c8 | -6.9141 | -59.1394 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd9c4afe-a180-37c9-84f5-04b66adceb1f | -6.9092 | -59.119701 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96c6ff9e-80ae-34a1-8cdc-9a7198e9e97f | -7.3153 | -60.6091 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09e79ce3-96f5-3bf1-be59-edf2473e5e5f | -8.1036 | -61.185501 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d34e016c-99f1-3e72-bb0f-862b2fbe9408 | -6.89 | -59.166401 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea49534-dc74-3ccb-b448-f8871a8d2a34 | -7.8802 | -61.795601 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be68bf75-93fb-376b-ba40-0aa82cf6e0f2 | -7.621 | -63.522099 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b00a1f7-7849-3069-b8fa-d632c7cc3a24 | -10.3342 | -64.4487 | 2025-08-14 01:31:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 176f65c8-fa27-31aa-9a4f-dc4a81a22c78 | -6.8658 | -59.151501 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3304e52-997a-32d7-935f-5a2bf8ce6cde | -9.1788 | -59.651199 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7b9196-2610-3b32-a5c0-25732f3a4261 | -7.8704 | -61.798 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c96f7a5-3e01-3585-86b1-a0d60c9b97a5 | -6.8705 | -59.129299 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a381a65d-2ce8-3a73-82ba-cd7792216d74 | -23.6558 | -51.8134 | 2025-08-14 01:31:00 | METOP-B | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9eec2a1a-ea8f-3e3b-914e-4fdeae59cf68 | -6.8997 | -59.164001 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 426d7ec9-ce2a-31ba-9b23-a24568dccc93 | -7.5969 | -63.507 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79582a4b-04e4-3374-b921-14dc1b80b804 | -6.0749 | -59.944199 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b264681f-d29b-3822-8ba9-4eb206adc891 | -7.6285 | -63.509899 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba98ff7f-e7f7-30e3-8bf1-6bc415d145a6 | -6.8609 | -59.131699 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4c13b1-3256-3216-a0bd-9655c018748d | -23.646601 | -51.783199 | 2025-08-14 01:31:00 | METOP-B | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23fe00b1-ffbf-388d-b171-9510582af0e1 | -7.5946 | -63.497101 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a83670e6-3b03-37cb-9a30-57b1411d35c2 | -9.1262 | -59.646702 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db919f38-342c-3470-a0fb-23bcdb23a75c | -5.7394 | -59.872101 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37a9a2f4-ddda-33d3-8dd4-007bc32deef9 | -7.3191 | -60.6245 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbbf0908-7da8-3d04-ad6f-a1b73e0a1ec7 | -6.0802 | -59.923901 | 2025-08-14 01:31:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0f28d0-62c1-394e-a77c-25ba3bd3db2d | -6.8706 | -59.1712 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f43c22f-bda4-39d0-9ef4-9b99ac4386ad | -9.14 | -59.660999 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6eb068-919c-3c4a-8069-d94221425a73 | -7.6164 | -63.502399 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7facc5cc-12e6-3386-9b15-b9cabf386f0e | -6.8851 | -59.146599 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d03c54e-0945-326a-9aeb-c53720b2b9a5 | -9.1304 | -59.663399 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c68389be-ce75-3f01-be37-6e3e614af11b | -9.4985 | -60.5271 | 2025-08-14 01:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef2e2bbf-3bb1-3310-9ae2-6df9a0312377 | -7.1128 | -59.612801 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3c83690-1f1f-3b92-924c-bcbe88b09f7b | -7.609 | -63.5145 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1d7862e-6c0f-331a-8419-29b366607201 | -10.0449 | -64.891098 | 2025-08-14 01:31:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7cc922e3-06d5-37d0-bc14-0eab8a007d09 | -7.8607 | -61.800301 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41d34943-aac3-3e45-82f8-eb97ddacfba9 | -6.8995 | -59.122101 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6899dd1-a68a-350f-b97d-67c2cfd6a9dc | -9.1982 | -59.646301 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bade2fcd-6ea4-3a54-9fd1-6c531626bc76 | -7.5992 | -63.5168 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fde4b61f-4057-34bf-b7fa-c462e4fcfd91 | -6.919 | -59.159199 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a150b960-06a2-3f9c-9d08-abb71595a1cc | -7.3288 | -60.622101 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7fd487-32cf-30d3-ab76-fa758867ecf8 | -9.502 | -60.5415 | 2025-08-14 01:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02842f99-fd7f-378a-9c5e-850e7962d859 | -6.8803 | -59.1688 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d17fcbd5-38c6-3a74-a5c1-0e9538d31c92 | -9.1455 | -59.6418 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87d694c6-060e-3f40-ac3a-a1b3ddf886a5 | -9.1358 | -59.644199 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581e79c3-8f29-34dd-a4f9-fede04800db7 | -6.9044 | -59.1418 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26200afa-407b-331e-95db-574d04199618 | -7.5205 | -61.371101 | 2025-08-14 01:31:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f29c2fe7-2d75-37fa-9357-0e218fdd1478 | -6.8802 | -59.1269 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 817b9e69-d285-3909-9d68-b64d49ec350f | -11.8699 | -63.164001 | 2025-08-14 01:31:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
