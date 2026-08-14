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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9272f59f-bd85-3376-b6c2-ab283cc95630 | -9.19366 | -66.10173 | 2026-08-14 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47007d91-d3f3-30f5-9662-b9fc18eb56e0 | -10.06626 | -67.55917 | 2026-08-14 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58152ef0-b269-300e-b30e-61c3fbb1f56b | -6.96703 | -59.2915 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae3ff897-55c1-3e3e-ad70-a7167544c70e | -9.76214 | -60.76031 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b157ed5a-0e39-37ad-aa54-967f8af4a725 | -14.2945 | -51.9635 | 2026-08-14 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0282b850-97bd-30f3-92fa-9362a7b52482 | -1.82862 | -54.49806 | 2026-08-14 07:29:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| dfb9a9c8-488a-3e92-871a-68d3f6f18582 | -11.0635 | -50.9452 | 2026-08-14 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2712089b-3b3d-3e88-8088-43da1e5833a9 | -11.48675 | -54.61066 | 2026-08-14 07:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 2acade06-fcd7-3ae5-97c4-3c2afb3c7958 | -6.62222 | -59.0383 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e9e435de-d1d8-30d5-ac0f-4ca46ca0383a | -11.05223 | -50.95794 | 2026-08-14 07:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| b341f384-b451-3e23-b951-ad591f3932ba | -8.88982 | -60.55479 | 2026-08-14 07:31:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82350900-9ac1-3ee7-bb5e-a0a819293437 | -6.96377 | -59.28671 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 85b20bd1-a459-3c0d-8f56-d5cac22e113c | -6.62088 | -59.04725 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c822678c-5071-3ac3-9c60-0b7acf50b0f3 | -6.7007 | -58.94621 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b375ddc2-a12d-324c-93fc-24a3106630f3 | -9.97645 | -53.95225 | 2026-08-14 07:31:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4a1e71b0-27c5-3f68-91f6-b838cb29dc83 | -3.23939 | -60.11869 | 2026-08-14 07:31:00 | AQUA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a585ff8b-e9fb-37f6-a2c4-90242fce41a5 | -11.05688 | -50.91993 | 2026-08-14 07:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ab7bdcc9-641a-32ef-a9fc-fa3ebec08e90 | -9.58383 | -60.50185 | 2026-08-14 07:31:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f910342-d410-3dd3-b596-4fb07a4beb38 | -6.62007 | -58.99217 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 558a038b-8343-3087-8474-46a2598a02b0 | -11.48454 | -54.62313 | 2026-08-14 07:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 897a2809-1766-397e-8522-8f827352d49a | -11.06048 | -50.92801 | 2026-08-14 07:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e88c1fc2-bbf7-373b-80b8-dfec222a4d04 | -6.61336 | -59.037 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| caf8fe05-acb4-3675-949a-8f3b5b2578d4 | -6.61202 | -59.04596 | 2026-08-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 69dd385e-961b-3dd2-a687-50bd64b2abf9 | -16.91159 | -54.14575 | 2026-08-14 07:33:00 | AQUA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b600868c-8485-3e81-a71f-62a2e9911f74 | -14.0799 | -53.62107 | 2026-08-14 07:33:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c4927e93-3552-3094-842c-678757d39df2 | -11.0635 | -50.9452 | 2026-08-14 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 96a0bbd3-bbce-3e27-8e93-2b71d301a180 | -11.0635 | -50.9452 | 2026-08-14 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 29d41717-bf21-3a24-8a45-51c93ef43ab1 | -11.0635 | -50.9452 | 2026-08-14 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ba7511cf-310f-3b97-9c52-25b58b0e7f03 | -13.2801 | -54.2228 | 2026-08-14 10:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 6d199c6d-105a-37e8-87f1-275de9482924 | -13.2798 | -54.2435 | 2026-08-14 10:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 98321a5e-3664-3f56-993d-11052ab19eaf | -5.05769 | -38.13717 | 2026-08-14 10:58:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 34.8 |
| d257f3dc-2409-39f0-aa76-6b5727c9a154 | -7.07627 | -37.28735 | 2026-08-14 10:58:00 | TERRA_M-M | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d7429dcf-2ab1-3181-b798-d2b6f6282c13 | -5.06339 | -38.13057 | 2026-08-14 10:58:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| d4079a6f-81c2-390c-812a-f9e6b59f7ede | -11.4681 | -44.5558 | 2026-08-14 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1ab8e7ad-ecc1-3d33-bdb6-a8af972c16a5 | -11.4677 | -44.5791 | 2026-08-14 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 5a14b2ad-d860-39ae-bf90-3ce7e4257f2d | -20.27783 | -40.77349 | 2026-08-14 11:00:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6f29705c-9e4a-30e9-9187-ad9d0357ece2 | -19.13128 | -39.9854 | 2026-08-14 11:00:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1ba5dbf8-df4a-3ad8-b26a-50de81a365ab | -15.01641 | -41.63696 | 2026-08-14 11:00:00 | TERRA_M-M | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| e2afde5b-d41a-39c5-b57b-c85feea47443 | -11.47731 | -44.58894 | 2026-08-14 11:00:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b87a3bb5-46f4-38b9-bd73-b6ddfda0a8a6 | -14.62956 | -41.9568 | 2026-08-14 11:00:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 777ff99f-c4f9-301d-bd9d-e21cddd01ccf | -17.51347 | -42.37085 | 2026-08-14 11:00:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b44707df-0789-3d64-b536-5216793fab51 | -15.01346 | -41.65424 | 2026-08-14 11:00:00 | TERRA_M-M | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| f87d2cb1-0a08-3362-a621-a84e3e0ead75 | -18.89495 | -40.1818 | 2026-08-14 11:00:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 30.4 |
| 74c45047-e065-3418-aac3-92ad3f0a38e2 | -19.1349 | -39.96255 | 2026-08-14 11:00:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 6bcb024d-8fef-3e48-9af1-c162bddb5e0c | -18.89306 | -40.19351 | 2026-08-14 11:00:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b2220593-91c5-3fd4-8b82-c62dc5c34e4f | -15.00699 | -41.64705 | 2026-08-14 11:00:00 | TERRA_M-M | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 0f8a388d-dc7f-3bfa-8745-12c9a9aaf42c | -19.13309 | -39.97398 | 2026-08-14 11:00:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 0d0ae44c-eed2-3bf5-98c0-66ce82f38bad | -11.47014 | -44.59502 | 2026-08-14 11:00:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a15bab98-e7cc-337e-8736-1f8989ccf3c7 | -21.5944 | -45.2835 | 2026-08-14 11:02:00 | TERRA_M-M | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| e9951813-fd42-3a45-82ec-56e6b988ab4f | -11.4677 | -44.5791 | 2026-08-14 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 55022ff8-2480-3fd0-bb8b-712626176d32 | -11.4681 | -44.5558 | 2026-08-14 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 728ca188-b384-34f3-ae00-a5d5414bc696 | -11.4869 | -44.5763 | 2026-08-14 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 28e096b8-a937-307b-b5f8-c78e349d263d | -11.8839 | -45.9453 | 2026-08-14 11:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| de3145f6-73d1-31d2-b279-fcff4ebec743 | -11.4681 | -44.5558 | 2026-08-14 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| a38cfc6c-b9bc-3904-96ae-d8269c8d975c | -11.4677 | -44.5791 | 2026-08-14 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 26a48202-32e1-3476-b614-11d667524598 | -11.4869 | -44.5763 | 2026-08-14 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 598c3919-3b63-3db5-9bbe-4ae8f17e8052 | -11.4873 | -44.553 | 2026-08-14 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9b010c5a-9740-3d20-b157-af387dc45451 | -11.4869 | -44.5763 | 2026-08-14 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| be9f53e4-bc84-3c38-aea8-670a04d5678c | -11.4681 | -44.5558 | 2026-08-14 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a81601ec-556c-397a-a24b-26019352737a | -11.4873 | -44.553 | 2026-08-14 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 7ef6a245-a778-3555-b598-a3efd1522706 | -11.4677 | -44.5791 | 2026-08-14 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 574e2aa6-979f-398c-8d45-d3459bc11fa2 | -11.4677 | -44.5791 | 2026-08-14 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e90526c3-7153-3e23-9490-a2825d51ff19 | -11.4873 | -44.553 | 2026-08-14 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 5a88bcde-8a11-3adc-9502-7f3cfe6f9c23 | -11.4869 | -44.5763 | 2026-08-14 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 5a3f8082-bba8-31e8-a9bd-b3256ec3bb3c | -13.2801 | -54.2228 | 2026-08-14 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6cb581aa-e0be-30e5-8885-a883ed87a8a5 | -11.4681 | -44.5558 | 2026-08-14 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 68c6b6a8-b82b-3813-8ecc-517ea60efbfd | -11.4873 | -44.553 | 2026-08-14 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 468a120a-7073-3404-a34d-1526e2550165 | -12.029 | -46.4017 | 2026-08-14 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 13137984-e98a-3d21-b476-3074cc3cfe22 | -12.0099 | -46.4044 | 2026-08-14 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 05f6bb65-5055-3aed-a930-146fc5235b68 | -11.4681 | -44.5558 | 2026-08-14 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d47b1043-e8b4-361d-8694-d08a99c5ff76 | -11.4677 | -44.5791 | 2026-08-14 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0a8f01ea-62df-3885-98b2-df7e6b1d4850 | -13.2801 | -54.2228 | 2026-08-14 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 417.4 |
| aef4b79f-6ba4-3bed-bd13-2becd2f9d8fa | -11.4869 | -44.5763 | 2026-08-14 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 9e615165-73a1-395a-8dd8-cf3d7462911f | -13.2801 | -54.2228 | 2026-08-14 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 308.5 |
| 967742f5-d935-3cbd-89a6-3318aa62b1d5 | -13.2804 | -54.2021 | 2026-08-14 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| e604cd30-e517-3011-bcb9-3c2dbb214bac | -13.2798 | -54.2435 | 2026-08-14 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 98a14146-fecf-3084-9dc4-6236962deb29 | -11.4869 | -44.5763 | 2026-08-14 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d812e532-8b22-34b8-9ae8-4ec7e08bbb2a | -11.4677 | -44.5791 | 2026-08-14 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 57254ec8-b2f3-3bf3-881c-b2cfb29b8f90 | -11.4681 | -44.5558 | 2026-08-14 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| e3fc45d8-b6b5-34ad-9759-b2a9c8aa5d17 | -11.4873 | -44.553 | 2026-08-14 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| e576a206-c420-3fd6-ac7b-d060fd1dbd35 | -11.4869 | -44.5763 | 2026-08-14 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 67f586ce-98da-390a-8da7-170f929f35f2 | -13.2801 | -54.2228 | 2026-08-14 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 277fc757-5c18-3354-bd49-c320b0a9024f | -11.4681 | -44.5558 | 2026-08-14 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 35da48e9-715e-384e-b187-20404a528d7a | -13.2798 | -54.2435 | 2026-08-14 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 03bf6b4d-faa2-3fab-afef-e719fda854d3 | -11.4873 | -44.553 | 2026-08-14 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| dc886eca-b80e-3cb8-8987-0842a9a38397 | -11.4677 | -44.5791 | 2026-08-14 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 08766f8e-eb37-3cd7-851b-66b6af3838ad | -13.29 | -54.27 | 2026-08-14 12:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1a4eda1-9df4-3d5e-91d3-514f7074e891 | -13.29 | -54.21 | 2026-08-14 12:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22f1604e-dba9-389a-8172-c57a7ae475b3 | -11.4677 | -44.5791 | 2026-08-14 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| dd9d39df-b178-38de-876f-fef81b6da1b5 | -11.4873 | -44.553 | 2026-08-14 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 65c0d47c-23a9-3838-9e13-bb8db0afdd51 | -13.2798 | -54.2435 | 2026-08-14 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| c9b33c72-eec6-388e-83ec-8b1dd65ec825 | -11.4869 | -44.5763 | 2026-08-14 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| dbfcd170-0e84-362f-9e68-aa8f8a6394ac | -10.7099 | -50.5145 | 2026-08-14 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4974bceb-53a3-389e-9a82-1cfb6d4bfc70 | -13.6859 | -46.2624 | 2026-08-14 12:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| fbde2a30-1118-3c64-807e-7af1fa3f355f | -11.4681 | -44.5558 | 2026-08-14 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| dba8ffda-c380-3070-be80-47d96bd0edbb | -13.2801 | -54.2228 | 2026-08-14 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| e42d8f84-2b7b-3625-b811-2fc613037ee1 | -13.5701 | -46.2584 | 2026-08-14 12:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| be2ab72a-b88b-3ead-a687-4d3c11db09ae | -11.4873 | -44.553 | 2026-08-14 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 215.6 |
| aee85fc0-5edf-3bf8-b87e-fc9bcc7cb081 | -11.4677 | -44.5791 | 2026-08-14 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 4a71d130-b836-3027-b238-7ffd129e4a89 | -11.4869 | -44.5763 | 2026-08-14 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |


[Clique aqui para ver as próximas entradas](README38.md)
