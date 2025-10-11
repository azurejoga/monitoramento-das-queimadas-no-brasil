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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7c80505-9453-3e4b-9078-09e2863b2606 | -13.52823 | -48.12514 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39565fc3-8908-372f-83ae-d1baab0816e6 | -17.83174 | -57.66233 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 681cfd05-1b7b-35a8-9b84-80953112109f | -22.5466 | -52.05515 | 2025-10-11 05:25:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 51310f2f-d687-30a7-a3d5-485cac7215e9 | -10.87937 | -68.41724 | 2025-10-11 05:25:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40e6ff59-0241-3011-ac40-946ff09c5c53 | -10.42718 | -64.86942 | 2025-10-11 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5000a713-2aaf-3b49-a957-e9ac47ca09d6 | -18.07043 | -57.53914 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b535a664-a91e-31a8-8144-a4d25bb03ed7 | -10.05686 | -67.54939 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f43c4b1-aeb6-3523-b9d7-0dbe19defae3 | -12.23637 | -51.14399 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0d0a8a0-9aea-3b1a-80d8-4beeac25c839 | -10.57998 | -69.0678 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e09597-8b25-35ad-9f42-4adb4fd3d998 | -17.83678 | -57.65561 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5482eb1-f86e-3c4c-bc32-4b399f8aedaf | -11.84234 | -63.71251 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9ca01a-8dfd-34c1-8935-939af0c91eda | -13.33841 | -48.47995 | 2025-10-11 05:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42a10c4b-e172-3085-8783-ac66bdaf55d0 | -17.84186 | -57.58627 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e8a5394-ec66-3a50-b8ca-3c353dce9788 | -9.55634 | -66.73262 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adf8370b-c8d3-3864-ad59-7a05cb131c70 | -12.09448 | -64.24174 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced94309-8ad3-39ee-aa39-2ba9b5a582eb | -9.28164 | -68.77902 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db277183-bc16-3657-86c6-c23653991cc9 | -8.8917 | -66.86779 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac567a5-5503-3ec3-8cdf-f42684f9ba39 | -10.61485 | -68.67208 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64bc7b92-5e9d-333e-a104-fb837d9f0286 | -9.55172 | -66.03646 | 2025-10-11 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6abfdb1-456c-3597-8f5d-28c4458f24eb | -10.13708 | -68.99323 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da21f3a5-2863-3592-abea-5e733edb050b | -9.75133 | -67.22056 | 2025-10-11 06:14:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a45d053-978e-3b11-8292-f6c1f181c9c8 | -10.57587 | -69.06605 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e6bb611-568e-303c-8c76-6c882728f84c | -9.49648 | -67.13777 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b1e2de0-2aee-3a66-bfd2-dbfe02a85879 | -10.06005 | -67.54897 | 2025-10-11 06:14:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 330a0a30-1a6c-3eac-9c8c-b0a46cfde805 | -9.55926 | -66.7434 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af350090-8b50-313b-a799-736965567c91 | -10.70144 | -68.55091 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 717d6637-5ad4-38b3-9e06-d9b93cf92ff9 | -9.36402 | -66.59632 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b2f4d8-ff50-3d22-9c37-d519b6ac8782 | -10.87899 | -68.41897 | 2025-10-11 06:14:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 998bac2d-96b3-30a3-912a-f0254a85d062 | -10.79243 | -69.31021 | 2025-10-11 06:14:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e678a6a4-c7aa-342a-a6d9-983e249ddd02 | -10.26452 | -68.27289 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 684231bb-b652-3230-b125-c7d600084a1b | -10.66313 | -69.0975 | 2025-10-11 06:14:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80fd3df4-87cb-3d1a-be40-fba0866ea3b0 | -9.54299 | -66.46937 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef9305f-2b28-3c54-82c9-523acfccd601 | -8.87122 | -66.77764 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9aa30ec-0ed9-37e4-a022-0d79587f82e1 | -9.17225 | -68.17479 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5395781e-c04b-3c90-94e9-b0395f9c3697 | -7.91033 | -70.91631 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac645919-9cd3-3009-94dd-10bbfbe753bd | -9.3886 | -68.90364 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28cb0a81-6b23-3e7a-ba86-5d2af456ad6c | -9.54774 | -66.47005 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c774e0-8ea5-31c6-8169-2525eacc84dd | -10.00706 | -68.97428 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ebea8e8-0f0d-3ac1-a33e-9a8813b0d711 | -7.90742 | -70.9118 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22edd35c-1ea0-3f16-a5ba-4f0ab6a5eeff | -9.27761 | -68.77841 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ccbe190-271d-3d58-b05e-1c886f235a70 | -8.25725 | -71.11842 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51d30919-79a6-3d0b-9af2-6bef92ef933b | -10.26481 | -68.27112 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 942486ad-8278-34fa-9164-8b69ec7ac7d5 | -9.16916 | -68.16635 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 769fb729-ba82-349d-a1b6-c601b881a9fe | -9.6498 | -68.55865 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9786575b-1f48-3f79-a02d-7775ff5bb281 | -10.90636 | -68.25387 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a9be514-5e87-3ce5-8c90-71e4c14c468e | -9.54683 | -66.46886 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13c9ba5e-a79e-3464-a393-30b20af3256a | -10.91063 | -68.25449 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87f21f7f-c9b1-3b54-b768-78d991de5827 | -9.17952 | -68.18383 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ec8871-9939-3d74-867c-88ccad408cb5 | -9.56324 | -66.74899 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f78558-fae0-3c52-bf68-99fe33057240 | -9.55661 | -66.03714 | 2025-10-11 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9b2be14-0b3f-35b7-9b35-79519ef0ba74 | -10.87954 | -68.41501 | 2025-10-11 06:14:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bed36b9c-e6c6-37e2-9c6b-6b016d1ace53 | -8.61928 | -70.97174 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc125b20-5580-38c9-ae6a-605376c0eb83 | -8.73855 | -67.19852 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de168f83-265c-3b26-b826-054047684625 | -10.9093 | -68.25633 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69c76d7d-4494-3d7a-83ef-96c5ef283a12 | -9.50101 | -67.13843 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ca4d74-d974-3cd1-8cb2-ce1d25b9b1d2 | -9.16497 | -68.16569 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 600d7eb4-26bd-3036-adcd-2fd6a8ae588d | -8.35132 | -71.02322 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6511eef4-0caa-30b1-9d14-1b4b9a0b6e9e | -10.02726 | -68.85991 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d77cfc9-9e66-3a9f-9116-50ad4d38559b | -9.18008 | -68.17992 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f725f499-d2d8-3817-bd77-09b51daccc98 | -10.06508 | -67.54516 | 2025-10-11 06:14:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8c26099-16bc-36ad-aa78-235496a0548a | -8.89235 | -66.86307 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03bdfbd0-0e88-3f23-9122-4cfea3378789 | -10.59009 | -67.7486 | 2025-10-11 06:14:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a6ef02-d9c5-3eac-9d00-811c9873bf40 | -9.45478 | -68.0711 | 2025-10-11 06:14:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f24ac8b-333e-3ed0-9ab7-58a4b26963f8 | -10.57991 | -69.06659 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e728f86-7107-3fcd-bad9-30fbeac2d69e | -9.55594 | -66.73282 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c79620-ca6f-3a4b-87c0-3d2bbd91ee80 | -9.61625 | -67.47633 | 2025-10-11 06:14:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f178ecc6-e83c-3ac0-a163-827686c1f0c9 | -10.06448 | -67.54962 | 2025-10-11 06:14:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 347c3d42-74d4-3709-abfb-f7e2ce1f9b37 | -10.24253 | -68.08805 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd7c0921-7650-3bdb-ad99-8ec114b7e74d | -9.61656 | -67.47899 | 2025-10-11 06:14:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a4f5eba-bf90-3dd1-8896-b089612a1604 | -9.17588 | -68.17931 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b52517d-db97-3949-880d-b00d06175365 | -10.79689 | -69.30735 | 2025-10-11 06:14:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f955dfad-0201-352c-9156-c2dee0b63c5a | -8.36239 | -70.3289 | 2025-10-11 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a676f17-de59-3761-85fc-20388fc182ec | -9.72155 | -66.65773 | 2025-10-11 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 076b09b9-d67d-3b8f-aee1-7fdb08e6250b | -8.05757 | -72.46512 | 2025-10-11 06:14:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c1e1a25-9521-3819-9728-162a728f2e0c | -8.89299 | -66.85833 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff28365f-b29e-323c-ae56-790ae783d2e6 | -9.17644 | -68.1754 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20cc5532-9251-323b-9150-94ee1c9acd4b | -10.93826 | -68.39697 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f355e259-0ebd-3482-b072-e2d7f69e154c | -8.73917 | -67.19407 | 2025-10-11 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96360989-d9b9-373b-8c1e-dd130a452237 | -10.14111 | -68.99383 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 350ffd26-2fcc-32a9-af01-b1910147e952 | -9.3891 | -68.90008 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1913b68-3ab8-37ec-9fe6-018128ff148c | -9.63011 | -68.60907 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36baf45b-8aa8-31f5-994f-2427530dbb1d | -9.39779 | -68.22863 | 2025-10-11 06:14:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55b9f0b2-cef9-3a06-a131-44146f88ad30 | -8.87582 | -66.77827 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 782c97a8-fae3-352d-aabd-ca78dc2a59d0 | -8.88713 | -66.86712 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4ec799-a9b0-32a5-92f8-2d33f8461f47 | -9.40697 | -66.75992 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d202ac8-e733-3dfb-b140-f71d70cabc32 | -8.35031 | -71.02374 | 2025-10-11 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7798c62d-bfa2-3bd6-b923-b939931cf863 | -8.25893 | -72.81454 | 2025-10-11 06:14:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a071066a-7be9-38ae-b1d9-ac780dcad48e | -8.88778 | -66.86241 | 2025-10-11 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee17e3f7-a2cb-3533-8daf-2908763e484f | -10.62818 | -69.31564 | 2025-10-11 06:14:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 902139e5-87a4-39f3-8b67-4fa5f03a10f2 | -10.69726 | -68.55028 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c013d45e-83f5-31aa-9a30-5da9ce0cd3bd | -10.93402 | -68.39635 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d14b5b-b817-3ac2-849a-b35857c07ac1 | -7.014 | -71.80279 | 2025-10-11 06:14:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa82f351-3e8f-3bac-9d11-f90a18209b86 | -9.50769 | -68.53133 | 2025-10-11 06:14:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 958bc091-5f52-324a-9141-37cfac6bdee5 | -10.57536 | -69.06961 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd6b1ba4-516b-30c1-a1d4-c1832732a158 | -10.6107 | -68.67152 | 2025-10-11 06:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d042c502-1089-3fcc-857f-453ad7a69df8 | -10.08164 | -68.47118 | 2025-10-11 06:14:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654706fd-8cf8-363a-ae55-5f0a1b0bbb85 | -12.0921 | -64.23527 | 2025-10-11 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7661b99d-886f-3c47-862e-498432fbb0b2 | -10.91572 | -69.19875 | 2025-10-11 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37684db-88b6-3ff8-bc35-af45cb9bc5ab | -12.09781 | -64.23602 | 2025-10-11 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811fe4a9-296e-369f-b02b-feced23ec79e | -12.09163 | -64.23926 | 2025-10-11 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
