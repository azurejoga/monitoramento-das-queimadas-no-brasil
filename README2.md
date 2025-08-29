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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 255c5272-6bcb-3188-b685-8edc9793ae34 | -9.4618 | -60.5682 | 2025-08-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| a135e6fe-3f56-3013-be69-da091c6008de | -13.5774 | -46.8714 | 2025-08-29 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4a98e5ec-a3d2-33b5-ba31-05013033880a | -9.4263 | -47.6384 | 2025-08-29 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9f21a7fb-db9c-37c3-ac59-cde7d6bcfa17 | -18.1252 | -50.2586 | 2025-08-29 00:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c3fb9ae4-34ae-3c2c-9c98-8d3d45e6041c | -3.7509 | -54.8291 | 2025-08-29 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6d4423ee-e905-3f1a-86d7-0d34cd91f754 | -5.1702 | -46.0676 | 2025-08-29 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ad67c032-79c8-315b-adac-cd93162c2a41 | -9.7728 | -64.2657 | 2025-08-29 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6f2e108e-2718-35bc-8e42-7ead7248da87 | -13.5391 | -46.8548 | 2025-08-29 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9f52feea-a5dc-355f-ae9f-52c2ef5b0d9e | -18.1457 | -50.2326 | 2025-08-29 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8574a38c-8017-3708-90b7-6597ed2a7593 | -17.3636 | -42.6532 | 2025-08-29 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4f4ad21d-8b34-34d7-86b9-82441480c0de | -12.0784 | -44.7199 | 2025-08-29 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9e39c18c-1ff1-3633-8708-73b90ed309e4 | -12.4344 | -63.9364 | 2025-08-29 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f06800b7-ccaa-3cac-a065-a01384cb0e31 | -17.3442 | -42.6333 | 2025-08-29 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 145.6 |
| a03bc644-cffa-3427-a8cb-e7062fafa369 | -13.2036 | -45.2601 | 2025-08-29 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a0838659-7298-365c-bb89-729e573aa1fa | -12.9961 | -56.9201 | 2025-08-29 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e1f20a30-a02a-3d32-af9c-78fadab1b78c | -3.4254 | -49.0517 | 2025-08-29 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 202f5bc8-d039-31b4-a443-20bbb6db1cd4 | -8.176 | -61.3564 | 2025-08-29 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c4f52c72-3f31-35d2-ba40-69cda7a458c8 | -10.381 | -57.8443 | 2025-08-29 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 834412af-b435-393c-a6e6-26339403fddc | -9.4433 | -60.5499 | 2025-08-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| baef0d70-5210-3d27-b61d-2a005fd9d32f | -13.0151 | -56.9184 | 2025-08-29 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 6189cf30-e9a1-3158-a12d-177ff56e9fb3 | -11.3325 | -43.5689 | 2025-08-29 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 802796f7-e25e-3406-9c8e-96620da0fcb8 | -8.1944 | -61.3747 | 2025-08-29 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4aff6c50-115f-3aea-8ddf-8f7ce6d966bd | -5.6933 | -45.9667 | 2025-08-29 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d1dd71f4-e8f8-396e-beb1-39d68269b65f | -13.1837 | -45.2865 | 2025-08-29 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 6f8fb5c6-46b9-3bca-ab70-fe5907137b69 | -12.4345 | -63.9173 | 2025-08-29 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 151.7 |
| b099161b-cfce-3b6a-a89a-1db2180f9b3e | -11.3517 | -43.566 | 2025-08-29 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| ff6bafab-0752-34d5-abaa-4ace2e36576b | -3.4255 | -49.0303 | 2025-08-29 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 6ce6f98e-cf10-3a51-a929-831bb21105a9 | -12.0976 | -44.717 | 2025-08-29 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 3367279b-1a29-354b-b8b0-f61c113b85ee | -10.4551 | -57.9378 | 2025-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a9cbc4a7-bf75-3ef1-b998-edb4134a73ae | -12.4156 | -63.9183 | 2025-08-29 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 40a9513d-2985-3a95-9a95-9ec480fcbb43 | -13.2027 | -45.3066 | 2025-08-29 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 40474d0b-f7c4-37df-8475-4aaebf6cc924 | -6.5546 | -43.9221 | 2025-08-29 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6633d585-b627-30d3-b9d0-a25a4819c72c | -9.4449 | -47.6585 | 2025-08-29 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 944c0aa4-cfc9-372a-a845-056cbbf588ba | -17.3643 | -42.6284 | 2025-08-29 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 205.8 |
| c1e2b3b6-7feb-30a5-a19e-414142585bcb | -24.1861 | -49.5515 | 2025-08-29 00:20:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b8d9f225-80a5-3319-97fa-0378006b2be2 | -9.426 | -47.6605 | 2025-08-29 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e13eece4-dcb6-31b9-a171-59d7533b9aba | -9.2178 | -60.8689 | 2025-08-29 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 37928c31-d2ea-38c7-8456-08f785e218b9 | -13.0342 | -56.9166 | 2025-08-29 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0e6a531a-444a-33e3-9ca6-6de142dd1b9f | -24.1648 | -49.5569 | 2025-08-29 00:20:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fac3a3bf-c429-3232-8bfd-a6b26147171e | -6.5358 | -43.9237 | 2025-08-29 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 8776b783-b941-35fa-90d1-226b377e3990 | -13.5386 | -46.8775 | 2025-08-29 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 7a64ad53-1156-3d56-8d45-a93c51fe8c16 | -9.462 | -60.549 | 2025-08-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| c5a2bb21-2df9-31b8-b180-e034fd477af1 | -13.2031 | -45.2834 | 2025-08-29 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 5b2a8ceb-be31-3a9b-8505-fcf5ec6b2c55 | -8.1758 | -61.3755 | 2025-08-29 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 30d71a70-eb63-3593-86b2-9209d3ef608d | -13.558 | -46.8745 | 2025-08-29 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 166.5 |
| e9516e91-ca1b-37d1-a897-a26b58c7b205 | -10.3812 | -57.8245 | 2025-08-29 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 59d3b526-d9e1-39d2-918c-f525b46dd6cd | -8.2867 | -61.409 | 2025-08-29 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b20303e7-7220-38b4-ade0-1ae43ed09ac2 | -5.6081 | -45.0038 | 2025-08-29 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f6e826be-dd7b-370d-ae3c-7b92e11bf56f | -9.4452 | -47.6364 | 2025-08-29 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 95c6c712-ef05-38ec-9875-71dfb87c3105 | -8.1757 | -61.3946 | 2025-08-29 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 32f7e7ab-0d1d-385c-9857-99ef429bebdf | -7.0569 | -44.3623 | 2025-08-29 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e4c793c1-04e1-355c-bf99-e4c0f1a5148d | -12.4534 | -63.9164 | 2025-08-29 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 54480be0-b816-3305-aae7-71d4bf700735 | -10.3624 | -57.8258 | 2025-08-29 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 02f3dee8-ec48-37b1-9c9a-b88e94cc5299 | -9.4618 | -60.5682 | 2025-08-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 25c9e4bb-39dd-3b7a-8a3e-0fa8d7d53c7b | -13.5584 | -46.8517 | 2025-08-29 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e3451f9e-160e-33a9-9c27-420a0f8ba197 | -9.4263 | -47.6384 | 2025-08-29 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 94b4ea4a-7285-3d85-aad5-d8e48edecbe0 | -9.4432 | -60.5692 | 2025-08-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 3f18ae85-26a4-36aa-b22e-423b96e53651 | -17.3435 | -42.6581 | 2025-08-29 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| acce2587-d8d7-3ee5-a1de-ca7d33a479de | -13.5391 | -46.8548 | 2025-08-29 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 954e2762-3aac-353d-abfa-a3f046d4be0c | -13.1842 | -45.2633 | 2025-08-29 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e3462eda-857b-34e2-a0d4-5f86a985375d | -13.1837 | -45.2865 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 57a92da5-94b9-3fb9-a8d7-50d966542b3b | -22.6748 | -46.8681 | 2025-08-29 00:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 8382cadc-d646-3d9f-844f-6967be3f43e9 | -17.3435 | -42.6581 | 2025-08-29 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| fe4672c5-7960-3b26-97d1-c0ef80174b6c | -8.2867 | -61.409 | 2025-08-29 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c8f26de7-cfa6-3225-a065-da997cc5c2e0 | -9.5424 | -65.7002 | 2025-08-29 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f1993eb1-c977-3215-a3e7-51e6bcf3fdc4 | -13.5386 | -46.8775 | 2025-08-29 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 705a5394-fc91-3fa9-826b-6a615177df04 | -8.1758 | -61.3755 | 2025-08-29 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 02d533ae-7e52-3931-893c-53d70a0beaad | -8.1944 | -61.3747 | 2025-08-29 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 53484524-17e8-3d09-9294-4bfe650b6cc1 | -10.381 | -57.8443 | 2025-08-29 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7edc317d-f798-39d8-93c0-2af97677a86e | -6.5546 | -43.9221 | 2025-08-29 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 28c2d202-d0aa-36b8-9e85-bc39a6264c97 | -10.3812 | -57.8245 | 2025-08-29 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d91c88eb-a55e-3097-8a37-f855978eceb7 | -10.0227 | -51.1135 | 2025-08-29 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 99e37d12-c2d6-333e-99df-405d42b959c4 | -12.9961 | -56.9201 | 2025-08-29 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 948e88fd-465d-360d-b7f2-c91c59a44316 | -13.2031 | -45.2834 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 8c25f72d-3283-3a14-8b58-bc9984bb5522 | -9.4432 | -60.5692 | 2025-08-29 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 23ee3a79-e0e7-363d-a2c5-aed10a2791a4 | -17.3636 | -42.6532 | 2025-08-29 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a55b308d-94db-3042-b77f-eed4798ee332 | -12.0976 | -44.717 | 2025-08-29 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 270b7e67-970f-3378-8da7-1cace7be90c4 | -13.5391 | -46.8548 | 2025-08-29 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4e0eeb83-a7c9-3290-a53a-634564b6b09e | -13.1842 | -45.2633 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| f67fb2d2-af12-3420-ae91-82cdb212d226 | -13.0151 | -56.9184 | 2025-08-29 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ef5ace36-e5d1-3e00-8f8e-b5c43376ee09 | -12.4344 | -63.9364 | 2025-08-29 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c72ccc2e-9deb-3698-854b-e721436bf4c1 | -13.0342 | -56.9166 | 2025-08-29 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2212bfd5-7eac-3189-b176-9522beaa81b8 | -24.1853 | -49.5751 | 2025-08-29 00:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 018e9671-61dc-3810-8505-1eb372eb0c62 | -22.6756 | -46.8439 | 2025-08-29 00:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 97086270-bcb9-38ff-8fca-a18e9af7d667 | -13.2027 | -45.3066 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e9aca6f7-f79e-3a87-a949-e85cbafea18e | -5.6268 | -45.0025 | 2025-08-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 462147d9-183f-371a-94ce-0f97f48b4d10 | -17.3643 | -42.6284 | 2025-08-29 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9cb8bbde-79b4-3eb1-b8d4-a85da81a9fa3 | -9.4618 | -60.5682 | 2025-08-29 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| a0159bc3-3c96-3cfb-8116-40aae572c5ce | -10.4551 | -57.9378 | 2025-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 229cfdce-5fa0-378e-a91a-a06d2c5beaf7 | -13.2036 | -45.2601 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a5f0befe-c741-3c56-a81f-d8d91cbd2dda | -5.6266 | -45.0252 | 2025-08-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4a40192d-1629-3ff6-bc68-3f62cbe461ba | -8.176 | -61.3564 | 2025-08-29 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| dc81b757-cab3-3b4e-9f49-6b2850b673bf | -13.558 | -46.8745 | 2025-08-29 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3cb2f2b3-db4a-37cf-a256-bc8ec34c9802 | -5.6079 | -45.0265 | 2025-08-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0d3f5981-70fd-316c-b7dd-23e03655a936 | -11.3325 | -43.5689 | 2025-08-29 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3b26afce-33d7-397f-9278-8967c281aee6 | -13.5584 | -46.8517 | 2025-08-29 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d740e6d9-185e-3447-abd7-46a328f1877a | -13.1833 | -45.3098 | 2025-08-29 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4613518f-c02b-3185-8a86-737e9d0b3ceb | -12.4345 | -63.9173 | 2025-08-29 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 145.4 |
| d6572976-bee6-3d7f-9960-61a662a14c13 | -5.6081 | -45.0038 | 2025-08-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 80f20046-597d-37a4-9eb3-43030fb36e13 | -9.2178 | -60.8689 | 2025-08-29 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |


[Clique aqui para ver as próximas entradas](README3.md)
