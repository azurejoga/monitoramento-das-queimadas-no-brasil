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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7c28efc-ba47-3019-9350-b5b036015a89 | -13.16224 | -47.28209 | 2025-07-10 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 526e0688-0d00-3c68-867d-71c810e5ebf7 | -13.90257 | -42.13479 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 4490ab02-61e7-3550-b27e-11401b75aa59 | -11.87664 | -46.7646 | 2025-07-10 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 801fdb60-ac97-3300-a66c-10f1576e95db | -13.8976 | -42.13195 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 86aa3947-c7f3-3d99-9be1-25eb93a55d95 | -13.00069 | -46.28461 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7179b504-1b0e-3758-96ee-11d8190cf5ef | -8.5022 | -43.3085 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 281.3 |
| 59e918e3-ca89-3b1b-b287-1d1404e7f45c | -10.5776 | -49.1316 | 2025-07-10 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 141000ce-4433-37bf-a07d-c021fcffc640 | -8.5018 | -43.332 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| e620f125-fee3-316b-9124-bf1daa077ddc | -10.6675 | -49.4679 | 2025-07-10 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 47eae569-d127-3621-8033-c36d4145131f | -8.5028 | -43.2614 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| b7d030bf-bd6b-30d1-ab19-072f5a870924 | -10.5773 | -49.1533 | 2025-07-10 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 1e2f1bc4-512d-3d4c-855d-35f5c83112fc | -8.5211 | -43.3063 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 60a600b3-9514-3cc0-a3a7-ccdf64e31439 | -10.6678 | -49.4462 | 2025-07-10 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 647dd321-99b5-3157-96b7-64e4a2c92416 | -8.5025 | -43.285 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 270.6 |
| 5740b571-46b9-31bd-b439-62cd5829d332 | -8.5214 | -43.2828 | 2025-07-10 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 5b80ba85-07fa-3a36-a1dc-9bdfb43ec8df | -21.18333 | -44.27483 | 2025-07-10 03:40:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fc4c8f43-408f-3987-bea3-88a2414ea9f5 | -22.24536 | -49.60971 | 2025-07-10 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ded9655d-2f9a-3fe7-9cff-383553f5a083 | -15.68463 | -47.84953 | 2025-07-10 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a033ee53-6e0f-3c44-805c-5c3aba2a6fa6 | -19.45546 | -44.31593 | 2025-07-10 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b78aeff-9370-35c9-ad87-4eb8d6691b5b | -22.2495 | -49.61369 | 2025-07-10 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7bef5ffd-a2b1-322e-8a40-de77ec75504f | -18.78938 | -47.96222 | 2025-07-10 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c271656b-73b3-3217-9579-eec6a9dda0f8 | -19.86353 | -48.97339 | 2025-07-10 03:40:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59a17ca8-b6f4-343c-9d40-777a81523ff9 | -19.45038 | -48.54073 | 2025-07-10 03:40:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ee078854-6a35-303c-9c04-29d136710f36 | -21.348 | -48.62552 | 2025-07-10 03:40:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4cba0fff-0ee7-3664-ba24-6e01f6f41041 | -21.7653 | -48.12628 | 2025-07-10 03:40:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a81c010-b3a3-386a-92da-cf72fe7724b0 | -16.6806 | -43.88243 | 2025-07-10 03:40:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d133a566-f548-32e9-acab-8bd7c44d5c1a | -16.58292 | -43.64932 | 2025-07-10 03:40:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff6c8d1d-4353-3154-a219-306c259975b3 | -19.05747 | -48.34069 | 2025-07-10 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60b215ce-d84a-3f0b-9a9c-eda3c7a2f600 | -23.11304 | -47.21141 | 2025-07-10 03:40:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d6353f5b-c8ec-3709-887f-b93a090fa5bd | -19.44792 | -48.54242 | 2025-07-10 03:40:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 10a47a69-3444-36e8-8037-824232385cb3 | -22.24362 | -49.6117 | 2025-07-10 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c9a85f3e-52d1-3fe0-86cb-e259a285c9cc | -19.69866 | -44.61852 | 2025-07-10 03:40:00 | NOAA-21 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4c6c65b4-9924-352e-9e99-f51737df1371 | -21.34896 | -48.62132 | 2025-07-10 03:40:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 51b46650-a69b-340f-b2df-fd8ed3ddc978 | -19.97954 | -47.185 | 2025-07-10 03:40:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0f37a01-e739-31b2-9404-1a7011b4d92d | -19.97961 | -47.18284 | 2025-07-10 03:40:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74887724-361b-37c5-b78d-436bd6fa639e | -19.06074 | -48.3375 | 2025-07-10 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 092aa37c-127d-3a9d-9ea0-27ad901ee1b1 | -22.24421 | -49.61449 | 2025-07-10 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7f8fbed5-f732-31eb-b793-9656b1c50deb | -19.05851 | -48.336 | 2025-07-10 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee61dc9-ede5-3efa-8307-bbf93984df36 | -19.44908 | -48.5372 | 2025-07-10 03:40:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 313175c0-8d2f-371f-970f-f9e02406945a | -19.45153 | -48.53569 | 2025-07-10 03:40:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5a0a1ffd-6d96-3281-aae8-e3db41faddf8 | -19.97882 | -47.18656 | 2025-07-10 03:40:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38409cb5-21e4-3f12-8d17-8bfd0672fcbb | -8.5018 | -43.332 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 1c352fbe-da78-317f-8705-e8fa46391214 | -10.6675 | -49.4679 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d4f78234-169a-3cab-9177-8c15a51cc923 | -10.5776 | -49.1316 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f70d2823-30bb-3a03-a3fb-48165535e7be | -10.5586 | -49.1337 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| de8749e0-c56f-3726-9c52-63621926e142 | -8.5028 | -43.2614 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| fe2343ed-6419-33c5-9cb9-3eb6a7352ebd | -8.5022 | -43.3085 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 265.5 |
| 4572d1f2-8dba-3dba-9583-90c79c2671e6 | -10.5583 | -49.1554 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a47dba6f-a7bb-3abe-833f-9e3779305e91 | -8.5214 | -43.2828 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 5354d975-21cc-34fd-9e5c-489151e4cbbc | -6.8485 | -42.7979 | 2025-07-10 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| fc1b9ff0-47ec-351a-8097-7abac7a81dde | -10.6678 | -49.4462 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 739557ea-0d70-3e9a-a111-dc3082743ce8 | -10.5773 | -49.1533 | 2025-07-10 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 18fb3fd4-697a-3d13-894a-72797c7c389b | -8.5211 | -43.3063 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 691f67fa-0cef-3897-ac41-7a17a0df6201 | -8.5025 | -43.285 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.0 |
| e4bb4938-707e-3434-b520-e0e658627cd0 | -8.4835 | -43.2871 | 2025-07-10 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 6f53b770-5af4-3743-8254-db1d88dfc4ff | -10.6678 | -49.4462 | 2025-07-10 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2b4059f3-d619-32ec-b4c6-3c31593b7e5d | -10.5773 | -49.1533 | 2025-07-10 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6ed0fe83-0ffa-3fa3-99c8-958b570bf5f8 | -10.6675 | -49.4679 | 2025-07-10 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| fbd59ebc-09ac-3d02-9e51-7fdb637dd0c2 | -10.5776 | -49.1316 | 2025-07-10 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c3eedd5c-4e5d-33e9-8ae2-cde5ba633df2 | -10.5586 | -49.1337 | 2025-07-10 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ac45ff95-5e2c-3097-a755-bf5e313bddc1 | -7.23056 | -43.07937 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dc5f928a-cd8f-35c8-9f11-fe6fa0108f5a | -6.17351 | -48.05151 | 2025-07-10 04:02:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 507a30c0-b1e3-3153-a862-68a96da5b252 | -6.7003 | -43.10751 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98b9b609-42d6-32e1-9392-05de2ac9bdf3 | -5.45221 | -40.61969 | 2025-07-10 04:02:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 077957c8-67aa-333c-b319-99a828b47ff4 | -6.50388 | -43.34625 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9574c2a4-a14d-3b31-80e4-c26886117c2b | -5.02972 | -47.96924 | 2025-07-10 04:02:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfd5d5f3-7d32-3f6a-8a9f-aa7537dc4876 | -7.22406 | -43.07408 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a7a8820-4491-323c-95fb-c6615aa3d897 | -2.44274 | -47.32573 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40ceeb6d-7373-389e-9426-81cc77dcecbb | -5.44887 | -40.61916 | 2025-07-10 04:02:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1977583-37d1-363b-94d2-2b373db519f1 | -6.85669 | -42.79593 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7036ca6c-6994-3e22-bb56-44c61790f5fa | -6.9906 | -43.49438 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4dc04fc3-e96b-346e-95f6-90be3c4f3f78 | -6.67634 | -46.30692 | 2025-07-10 04:02:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4bbf06c9-9026-32ac-9ec3-340012709f4c | -6.85419 | -42.79687 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 854a8feb-b8bc-3fff-bd3e-c64323b16e77 | -6.72487 | -43.90474 | 2025-07-10 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f258a0d1-08d6-30bf-9644-fc5f4fa2d2a1 | -6.57273 | -42.90333 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eaeb9660-8300-30fe-ad9d-45c5daff265e | -6.95679 | -42.71805 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47c3836b-0a7d-3bef-9e76-445e87bb5c8a | -6.13652 | -42.96774 | 2025-07-10 04:02:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a09ec956-8a9e-3cd2-9ae2-776539b04b25 | -6.93397 | -43.02838 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e32aa777-df7e-343c-aba1-9ea1c7ac700b | -7.32675 | -43.98267 | 2025-07-10 04:02:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baaadc7d-004f-39ef-af49-87dd05e337e8 | -4.86758 | -45.31889 | 2025-07-10 04:02:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21877533-19c7-393d-bdea-dcdd76e7df13 | -7.00172 | -43.51834 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd18f419-c1ea-385f-b2b4-c21e74de86f7 | -4.22597 | -47.21484 | 2025-07-10 04:02:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed2ebc4e-13e2-35ea-b5da-3789dd50cbc5 | -2.31209 | -46.99325 | 2025-07-10 04:02:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06acc117-de20-3136-8ca5-f23bf41bf9aa | -3.45292 | -48.88385 | 2025-07-10 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01b7be7f-95fe-3d5d-a0dc-9739204b2809 | -5.75985 | -44.97592 | 2025-07-10 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6042b411-9668-3a0d-9ab3-1d90cc795f57 | -5.89092 | -45.57935 | 2025-07-10 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1e4f3c5-a59b-385a-b00a-139f6c6813ea | -6.85645 | -42.80546 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| c7798aba-9c3b-3c3b-8d5e-63a261843f90 | -6.8547 | -42.8079 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e7acd83f-216b-3aef-a66d-1f426b036999 | -3.45871 | -47.67802 | 2025-07-10 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 826f73c8-102b-36c2-bfcc-2941336785dc | -7.00598 | -43.4926 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9119b557-e6f0-32e8-83e5-ec149e48dd6d | -7.0974 | -43.94383 | 2025-07-10 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d455a43-8a70-3cac-a766-c2a83aa3e851 | -6.99426 | -43.49502 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e9faa21-a04b-32cf-aebc-4198ed261238 | -6.85709 | -42.80147 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 76ff0d91-cf25-3a81-af9d-78cadb0b7d42 | -6.85 | -42.80025 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 40f0c0e2-f5a0-3dd2-9a68-85c207a6aabd | -6.96096 | -42.71471 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a25c9716-9229-360f-ab0c-46a2a6e93928 | -6.17452 | -48.04987 | 2025-07-10 04:02:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0de36f7-7399-322b-8b8b-666cc0cc17f4 | -6.13584 | -42.97193 | 2025-07-10 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 561e5e0f-e13c-3786-a2d6-2085943139dc | -7.01331 | -43.49384 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac92ce66-a04d-3fd8-a3e8-8c544e838dd4 | -6.49948 | -43.35015 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92c3e3d6-fd00-3119-b857-7ea1e8cc2cef | -6.72564 | -43.90012 | 2025-07-10 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
