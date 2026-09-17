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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f70f484-03dc-3077-a86c-01fcd9835039 | -10.57626 | -57.6904 | 2026-09-17 05:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 442242b2-57bc-3eb0-a3f6-03fa9c62fe2b | -10.24982 | -68.76526 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83344f8-c202-354d-bec7-2af6a803408f | -9.06096 | -65.9149 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c152081b-2d63-3ec1-9905-4213802d8487 | -9.10572 | -65.94683 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ac9b75-601c-3299-9d16-b61b9a97b11c | -11.98402 | -52.4716 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 028887c1-fde5-37d2-9b37-9ae8387eb689 | -11.60275 | -50.63776 | 2026-09-17 05:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7df0147-cfd9-3cb2-824f-9281e38f8f69 | -12.1422 | -61.16855 | 2026-09-17 05:38:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52da6eda-971c-380f-9407-b8ad7d750adf | -9.05913 | -65.91787 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f219e845-5e6b-30de-8772-df7a1952fa97 | -11.80663 | -58.17517 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| d7b46a2a-c50f-3bca-9181-896f4f318d25 | -9.54052 | -62.37227 | 2026-09-17 05:38:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2110a025-baa9-3fe2-a072-679e307a5d47 | -12.66493 | -50.78734 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a7d9365-ef3f-33ec-9e94-a315584cd28e | -10.39842 | -58.30687 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4885f140-3eaf-3220-9a8e-754a5a4be548 | -12.11484 | -57.18983 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aba805f3-84bf-3784-bf66-45c0aa899b97 | -9.00245 | -69.40115 | 2026-09-17 05:38:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 729536e1-7d1b-3ec1-a5b6-bfbecc620b22 | -11.19648 | -55.03712 | 2026-09-17 05:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c340e6c-502e-3b5a-8802-3c3bfc852cf9 | -11.61017 | -50.63254 | 2026-09-17 05:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0dc139bc-0234-39ae-b1ff-7239f07f7c22 | -8.92206 | -68.57973 | 2026-09-17 05:38:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcfa927b-a54d-3bb2-970e-9675739d328d | -13.39076 | -57.0228 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3971119a-be9e-3932-9416-2f34f12f30d0 | -9.03614 | -65.93186 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d86742e8-6e52-3271-8dca-7f9c5423e94f | -14.82436 | -59.55117 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c91a6f8e-dc46-3fa5-b08a-d98243ffe2cc | -10.77085 | -61.26825 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6184682e-6877-39c7-bb3b-19f1ea08f099 | -18.02356 | -50.9476 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30bc2379-0dcd-34d0-a433-e836ad289e52 | -12.65347 | -50.76746 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8d7672c7-9748-3379-8f35-338bd871b732 | -13.38558 | -57.02698 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 903d3bf9-dd8e-38d6-9391-8ed29c1c5c00 | -11.98633 | -52.4648 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8655d7a-11a8-365c-b94d-80325facb4d1 | -10.87755 | -61.3924 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1651b947-7727-3005-94ba-01244411d613 | -18.03307 | -50.95293 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d1dc6e0d-6808-3776-8e4f-37a35e914579 | -10.26109 | -68.79854 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56883bac-96c3-3cdb-8704-e5085aa911c2 | -11.81128 | -58.17192 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3e420e4-9324-398c-8446-a188cc44933f | -12.51522 | -56.90394 | 2026-09-17 05:38:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8697ae0-550b-3a4a-96c5-192cf997454c | -9.62294 | -61.81749 | 2026-09-17 05:38:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca858297-68b7-38eb-833a-251c7f1943ee | -9.61958 | -61.81697 | 2026-09-17 05:38:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23358c0-416c-38b7-8c91-1ac064654478 | -10.88497 | -61.38972 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad45e372-685c-30de-83c1-c0dda9598ce5 | -9.00115 | -69.40347 | 2026-09-17 05:38:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58af3306-b45d-3667-87a4-15d2ab02778e | -15.60923 | -56.54556 | 2026-09-17 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86060b71-ff9e-39a0-b436-3b44180cd3da | -13.37587 | -57.03044 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b776d4dc-4be6-36ba-ae96-5457e5455f8d | -11.1922 | -55.03058 | 2026-09-17 05:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7de1c3e9-3fe1-3159-acda-2b665de4d077 | -14.84167 | -59.5397 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48d31510-c735-3db6-a1f0-de10ec35e710 | -9.10777 | -65.93449 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f14ac0f-190d-31a8-a03d-9d814535f7f4 | -14.86568 | -59.51082 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92bc92d0-61cd-340f-b564-92249e3baa37 | -11.60344 | -50.63173 | 2026-09-17 05:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c86774b5-a920-3c77-a90c-76f6d7de5dca | -12.10983 | -57.19594 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38ad919a-a309-37fc-aff2-baa044f842a2 | -14.82046 | -59.55037 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cda771d-d365-3bbf-be5e-5b5227774bc8 | -9.10846 | -65.93037 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78cfb5de-77d1-3268-b78f-64a1d5a34088 | -10.38593 | -58.30851 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41a95e50-8bb1-3552-891c-0473a3a39ffa | -10.39392 | -58.30974 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 810b7a86-0c29-375f-b6e9-aff91685e320 | -18.02601 | -50.95211 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cb20598c-5392-3ffd-a122-d055f020d520 | -10.57987 | -57.69508 | 2026-09-17 05:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52f974aa-3b12-3ea8-a9ce-d508c510de71 | -10.14647 | -61.1823 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83cca06c-a9c8-396a-92bc-7c8c803b87e7 | -9.34731 | -65.93427 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ae0ee89-f319-3601-8e5f-75cb5771c7ca | -10.52315 | -57.45089 | 2026-09-17 05:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f3e605b-cee8-35fe-b84a-dbc59a9d6051 | -9.34444 | -65.92951 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f26335d-21e6-36ba-a9fb-b40b6afd9dc1 | -10.5976 | -59.4164 | 2026-09-17 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57941d40-de3b-3c73-8b6e-f2071b917b97 | -9.06132 | -65.92667 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8fdd230-e8de-314d-900d-a42c03273e14 | -12.10543 | -57.19527 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ced8ac95-eac1-3266-979c-87c4b1c4e1c5 | -9.05982 | -65.91378 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c55beaf-30a5-3af1-b12e-d2b9ad62773f | -9.10145 | -65.95036 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc6fe35d-3e5a-3d24-aa25-27af17c206e3 | -10.57571 | -57.69435 | 2026-09-17 05:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c668c1-d3fa-3953-998e-367920f7d695 | -14.8409 | -59.54543 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d725b29b-e5ff-3a12-a46b-a42e66c505b6 | -13.37526 | -57.03513 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8f7467a-8911-366e-b51b-57129462a737 | -10.38943 | -58.3126 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f05c431-3f92-36f6-a796-d2a993790707 | -9.11203 | -65.93099 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5df4ca3d-20c6-3bfd-a3a7-3f3f4b319574 | -11.9858 | -52.46935 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f14b2ac5-1153-386d-aa22-700486c2c560 | -10.76076 | -68.33167 | 2026-09-17 05:38:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33a1445f-da14-36f1-b1f3-5f429919aa7e | -9.50476 | -63.56664 | 2026-09-17 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 514891cd-472b-3305-983b-052d458be7b6 | -10.39042 | -58.30566 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 157733d7-7058-36d5-9dc5-2ec16a088af8 | -10.39441 | -58.30627 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adee5173-fa7d-3322-86c4-b283fc522bee | -9.09348 | -65.93206 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb33b90-61a1-3c2f-9177-2bbf90659351 | -10.29965 | -68.85577 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41b7b924-0493-3a2b-9570-8aa45d8954da | -11.98029 | -52.46399 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33724f8e-af31-3085-8587-6e65502b9cc1 | -10.88041 | -61.39669 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29458592-452b-361f-bb0b-3d08096f2741 | -15.46312 | -53.77737 | 2026-09-17 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5c5b28e-c85c-37fd-9b75-a9e686bdf6e8 | -10.14703 | -61.17857 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 206f5826-66b9-3f35-8a2e-92c7841872d6 | -15.60438 | -56.54501 | 2026-09-17 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b3af553-8712-3a6b-b765-39e806af2695 | -15.46845 | -53.78243 | 2026-09-17 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2b8f3cd-fea3-3ccf-9ce5-82e8f142b5d1 | -9.10283 | -65.94209 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 531c2682-d018-326c-a518-42771daaf2f4 | -14.82377 | -59.55357 | 2026-09-17 05:38:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e01ce003-a1b9-31a0-a7e6-51e19f556e11 | -11.80611 | -58.17895 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| a2714cbd-1758-3612-8a5e-2c40794967a3 | -9.11491 | -65.93573 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3888995c-bb67-3309-9a29-18dd70cf513d | -9.10214 | -65.94622 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6d271a7-1e32-385a-a494-941ca684fdab | -11.19609 | -55.04004 | 2026-09-17 05:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4572488c-4fce-38bd-8047-2b589c78b709 | -15.49075 | -53.79348 | 2026-09-17 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b1b372d-7e37-3aaa-bf75-ba287436b75f | -9.18349 | -66.02155 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a87786b4-9d08-3818-9567-b0a68b0f4c36 | -15.49028 | -53.79772 | 2026-09-17 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74183944-efe2-3f49-a307-619de02383e7 | -11.08103 | -60.70263 | 2026-09-17 05:38:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d9dad90-dde3-3b49-971c-19fd00ef0cdb | -9.11066 | -65.93922 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66cd8e2-c131-3010-b785-93b6dab2acff | -10.39491 | -58.3028 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adabdab6-d518-320b-a874-c01485829f98 | -11.81075 | -58.17572 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 48da14be-57da-3005-8f71-2490aa6718ec | -12.13807 | -57.18425 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e53e6c1-1226-39fb-b9b7-187c4095ba03 | -10.17577 | -69.35955 | 2026-09-17 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5727a8b8-f0f5-3472-9337-0f1318b5db84 | -13.3862 | -57.02221 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb2a2b5b-2693-357a-b094-5b5538fa11da | -13.37649 | -57.02568 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad4e998f-53bd-35ff-8406-0ca018f9ea46 | -9.05672 | -65.9184 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b848e254-2fe8-3f6c-8b47-252127f1762a | -10.99018 | -59.13813 | 2026-09-17 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de6640a8-4899-35e6-b825-a32ca2772e2a | -10.59318 | -59.42038 | 2026-09-17 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d287fa-cef9-3040-add1-bc4e065d0178 | -9.03682 | -65.92774 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 923cc9fb-3ee6-34d0-889d-81cc2d71810f | -10.39235 | -61.19988 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cfe91a3-793b-3a98-83b3-74809cccd4bb | -9.11134 | -65.93511 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43b81b3f-589a-3a1d-ac0d-163140826bc4 | -12.11544 | -57.1879 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c53ee034-a5d3-392a-a1dc-3f8a7873976d | -10.88098 | -61.39294 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README80.md)
