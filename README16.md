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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7da497-5e80-3b03-b005-43b53526193e | -9.4992 | -60.547 | 2025-08-15 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 92553eb6-0dbd-32e6-94fb-a5564bbc676a | -7.5292 | -61.3254 | 2025-08-15 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6569fe9a-26b4-3e13-a14c-2d2756c7a415 | -15.8998 | -50.1757 | 2025-08-15 02:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 12dc9109-c6ae-3e10-b705-e999c135a824 | -6.0807 | -59.9465 | 2025-08-15 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9c83b883-09fd-389c-8aaf-7a3ac79a88ab | -5.762 | -46.6741 | 2025-08-15 02:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c0e76f5a-b7c8-3ba0-b49e-11a49e9ddf9a | -9.1892 | -59.6752 | 2025-08-15 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0e72c35b-e5bb-3d53-af29-1529cf58a1b5 | -9.1708 | -59.6568 | 2025-08-15 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2063d582-1585-3ebe-bf68-a7f698a072f3 | -9.4994 | -60.5278 | 2025-08-15 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 1c623e37-c794-33c8-b2d1-bc06bd2388d5 | -7.5291 | -61.3444 | 2025-08-15 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f6fca219-714d-3782-a371-bd71edc911e3 | -9.518 | -60.5268 | 2025-08-15 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| c28e6ad2-a2b6-3156-9bac-d4f9b2c5e8e1 | -7.0797 | -59.2157 | 2025-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 81b9e1a0-f725-3f25-9066-bcff42d20062 | -9.1894 | -59.6558 | 2025-08-15 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b6a8c64c-b82b-3a19-ae66-0764d904993a | -6.9303 | -59.5305 | 2025-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 05a5d6bf-ad6f-3bd3-8b7c-38f55cb112d7 | -11.3657 | -55.4107 | 2025-08-15 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 34e2e76a-e7be-3bad-b14b-9ae15f83cbf1 | -6.9461 | -59.9912 | 2025-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1a394136-01f8-3c94-a3f5-1fc62de78c1b | -11.3466 | -55.4326 | 2025-08-15 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 32fecd0e-814d-36f1-a725-56d6355d1d1f | -9.1894 | -59.6558 | 2025-08-15 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| abd908bb-1a42-3784-959f-4ef679c3e0bd | -6.946 | -60.0104 | 2025-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| eb81fe4a-34d1-3dfc-9005-1f4b5d725fc0 | -11.3468 | -55.4124 | 2025-08-15 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 89bd5fec-dfb5-359e-8db1-4504a8d7923b | -6.0807 | -59.9465 | 2025-08-15 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 32e0efd9-721d-3544-87e6-3323062b60b1 | -11.3655 | -55.431 | 2025-08-15 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| eab0f1a6-97ba-385e-a559-4b057aa0a675 | -9.4994 | -60.5278 | 2025-08-15 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| c885b8d1-d7be-3348-b9bb-02c5b3babf2e | -5.762 | -46.6741 | 2025-08-15 02:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a2fee875-201e-33fe-84bb-92a3adcfea61 | -9.1706 | -59.6762 | 2025-08-15 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6ff598ec-8296-3b63-ba37-b673e4912a7c | -6.9645 | -60.0097 | 2025-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 346306a9-142a-3b19-b1b0-2ae6230bef85 | -9.5152 | -40.331 | 2025-08-15 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.1 |
| c80a0029-8dc6-367c-a95d-f839636448ec | -7.5292 | -61.3254 | 2025-08-15 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 97cd14c2-fafe-3d1d-8242-0c6b9750f4d9 | -7.0797 | -59.2157 | 2025-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0ea2654f-8ecd-3a80-83e5-3c575c980da0 | -9.5147 | -40.3558 | 2025-08-15 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 15ea7370-ce9f-3703-a306-19135f6d91b6 | -9.518 | -60.5268 | 2025-08-15 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a06286c4-c73f-32a8-8f30-87718bec6cb7 | -9.1892 | -59.6752 | 2025-08-15 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6ece882e-e9ee-3615-80e2-f6e17bce2392 | -7.5291 | -61.3444 | 2025-08-15 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fc5c4ccc-5cc1-3b01-967a-27faabcf2a10 | -9.1708 | -59.6568 | 2025-08-15 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 86693075-fa30-31ca-86a6-d0dbc7217619 | -9.4992 | -60.547 | 2025-08-15 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ce0364d4-2835-31b2-aadb-f8a054db67e1 | -7.5291 | -61.3444 | 2025-08-15 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 457745dc-fbb3-3dc3-b0c1-f54fef13b4fa | -6.0623 | -59.9472 | 2025-08-15 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8d88a831-2ba2-3445-9eb0-68f7d6f264fd | -6.9461 | -59.9912 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| cc230389-0b0e-3460-8f24-a5a41a82873f | -6.6576 | -58.8274 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5af4f0f6-5658-3562-b0c9-ba0b6a9fbcbd | -6.0807 | -59.9465 | 2025-08-15 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 48258a2d-95fd-3ea3-9f55-cf4d992e06e8 | -6.6945 | -58.8259 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 84365be6-78ea-3dea-9f4e-6940323d7797 | -11.3466 | -55.4326 | 2025-08-15 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 64fa571b-8711-3886-9bea-c5912f5b0460 | -7.0797 | -59.2157 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 33f109a0-d2f1-3225-b421-fc288d039719 | -16.2957 | -52.923 | 2025-08-15 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e08ef260-68d4-37c8-9af6-59bac0ce3a12 | -9.4992 | -60.547 | 2025-08-15 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 84b2619d-829c-315b-9a1f-3eee762cb188 | -6.9276 | -60.0111 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 192f775e-e0d5-3a83-8550-a7474fcce371 | -6.9646 | -59.9905 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dd8d9c9b-b95d-3c7b-8cb5-d1128fa00a49 | -6.676 | -58.8267 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5aa6869d-7fa9-3245-a8e4-847fd769c7ce | -6.6944 | -58.8453 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4175dbcb-4bfc-3bb8-a347-bed885a4a34e | -9.4994 | -60.5278 | 2025-08-15 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 9f5a7cf5-08a8-38f5-a2a8-05af2c9849eb | -6.6577 | -58.8081 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| aa86ab3e-b19b-3090-9a61-62d658163d79 | -6.9645 | -60.0097 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 93a04e1b-d54d-3f45-8aa2-66efa3412009 | -7.5292 | -61.3254 | 2025-08-15 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 50e18523-3494-3aa2-8001-2b9a47a7ff5d | -11.3655 | -55.431 | 2025-08-15 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| bd4bdcd9-f03a-35f6-9e1d-b3f46e7ef421 | -6.946 | -60.0104 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 255.6 |
| 85222cdb-66cd-3ce0-913d-822392af4ef9 | -6.0806 | -59.9657 | 2025-08-15 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 099a99e1-e94b-34e4-87be-05444cf714e1 | -11.3657 | -55.4107 | 2025-08-15 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 53b799b1-ed90-351f-bc6f-0140386d4b18 | -6.9303 | -59.5305 | 2025-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1ce0c12b-1b17-391b-86bd-5cb058506fb2 | -5.455 | -60.1391 | 2025-08-15 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7ed82ed0-6545-3281-8ffc-da0266e41bf9 | -9.1894 | -59.6558 | 2025-08-15 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d631d7c0-f7ce-3af1-86bf-4029cc41299b | -6.7129 | -58.8251 | 2025-08-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ab15f06e-d5e7-35e3-a9a7-586e940dd794 | -9.1708 | -59.6568 | 2025-08-15 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4c4f3db8-7612-322a-b1f9-d9527d162414 | -9.208 | -59.6548 | 2025-08-15 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 058d66b9-b734-3ce0-b162-a4091f404311 | -9.1706 | -59.6762 | 2025-08-15 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 47c9dcdb-c15a-3a42-8df7-5373e65d152e | -11.3468 | -55.4124 | 2025-08-15 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 3c1185b2-d562-3079-8563-4f0958843947 | -6.6576 | -58.8274 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5d758981-5c0b-37c2-8735-1f5fe28d591b | -11.3657 | -55.4107 | 2025-08-15 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| afa5ca54-4607-3eb4-9034-6be09f1715c0 | -21.2122 | -48.74 | 2025-08-15 02:50:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 267ba847-8c5d-3056-b5b2-c50a754903f3 | -5.455 | -60.1391 | 2025-08-15 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3775f43a-c6fd-3ce0-b001-13f4435b94e0 | -6.7129 | -58.8251 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e9505a2d-6540-3499-b86e-98ac45366e92 | -9.518 | -60.5268 | 2025-08-15 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d4d019ef-29f5-3ec3-9ec2-7938795a6a44 | -6.7128 | -58.8445 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5e44d3b0-12ab-3f88-9b06-f80509108450 | -11.3468 | -55.4124 | 2025-08-15 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| c8b0e75c-08d0-379e-b364-4655958f1a88 | -7.3116 | -60.628 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b45c8105-aa00-3a22-9086-3b3191bb97e3 | -16.3153 | -52.9201 | 2025-08-15 02:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1cc272bb-6337-3d2e-a61e-21f8c2255153 | -6.9645 | -60.0097 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9708f1f8-2a75-3b41-94f3-519950e13f8c | -9.4994 | -60.5278 | 2025-08-15 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a9eeb19a-afa9-3a95-bbcc-003b6e245b52 | -9.152 | -59.6772 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ad0343df-0a40-3b7a-a5da-8a4e37c9bce7 | -6.6945 | -58.8259 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| cdf446c5-edca-3cc9-b9e2-0d92848ff67a | -6.676 | -58.8267 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 08048472-3806-3b42-9aef-efa76f8ea63e | -7.5291 | -61.3444 | 2025-08-15 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 10534fac-bf53-3b7c-a092-e1c80904895d | -9.4992 | -60.547 | 2025-08-15 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| fae590fe-6d7c-3a74-8e31-54eb4f51f54c | -6.6577 | -58.8081 | 2025-08-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| df0a5128-5327-3331-8c47-ed8c64f60223 | -9.1894 | -59.6558 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 40be96b3-af23-3f5d-a73e-09457514c101 | -9.1706 | -59.6762 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| da4d3ba4-40f7-3b44-b0e2-888188cc7791 | -7.0797 | -59.2157 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a28c58f4-a645-30a7-a3c8-1a128b85aebf | -9.208 | -59.6548 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b9584d74-5817-3b55-810f-6cdfd7eb1391 | -11.3466 | -55.4326 | 2025-08-15 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 65718196-d469-31fd-bc7a-5c7dbfc90a9a | -9.1892 | -59.6752 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 076703f4-73db-386d-87e4-8c8cf7212905 | -6.9303 | -59.5305 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a233e600-7149-37ad-bafa-fa9ac9780378 | -21.2115 | -48.7632 | 2025-08-15 02:50:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 6c916a2b-15d4-3ebe-8c46-4169a83dba53 | -7.5292 | -61.3254 | 2025-08-15 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5f754498-d1c9-31ac-a2d5-6920f19bca1e | -6.9459 | -60.0296 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 026cbbea-8285-3cb7-a201-6f7192766940 | -9.1708 | -59.6568 | 2025-08-15 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a62f3647-aceb-30f4-9c8a-0918cc7ad518 | -6.946 | -60.0104 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 273.4 |
| 02fcde85-5593-3efa-8a99-47e1026953d4 | -6.9461 | -59.9912 | 2025-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 60836450-cd76-3092-9d31-d169495eb6e4 | -11.3655 | -55.431 | 2025-08-15 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e31a2f4f-4ef9-3905-b28a-52bfaa507398 | -6.946 | -60.0104 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 29bcfd94-ad1b-3157-a27c-701a2269086d | -6.6944 | -58.8453 | 2025-08-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7d866c1c-c573-36ef-b754-2bbf10533a13 | -11.3468 | -55.4124 | 2025-08-15 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 504519c6-0b39-3b52-8497-f98e9cc8dc9e | -5.455 | -60.1391 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README17.md)
