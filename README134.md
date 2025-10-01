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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21cccb66-fa6c-3ec5-a6bf-915c490408d2 | -14.89783 | -48.13647 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5aa91eff-68cd-3aea-8674-703c3b1fce68 | -14.4968 | -48.44967 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 380f6c84-eac3-3f37-9672-f2bcfa135ec7 | -17.89977 | -57.62279 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 82ddd357-4e51-3243-b46e-4a421b990a86 | -14.67812 | -48.12515 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 361837e7-cf25-35a0-8ea0-9359f7965d78 | -15.30541 | -56.7902 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7800ad64-c6ed-3927-93cb-a813b8224b87 | -14.72287 | -48.15847 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abc0263c-799f-3b51-ae76-507b15ed715d | -14.1378 | -49.1972 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91cea317-f560-336e-a090-5121a495d3ea | -14.18081 | -46.11898 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af2fb68d-691c-390e-a3b1-517270d81e3b | -13.94694 | -48.11335 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d747aad8-a35c-39dd-a29b-ef528ea65817 | -14.90092 | -48.10899 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 79aa5128-0dc4-3f35-b0e8-b2d0a53a5ce5 | -13.75524 | -47.93969 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4418b195-9bb9-37e8-9fb8-e6729b6aa2ff | -15.24111 | -56.83842 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f01dcac-4655-397f-ba55-2d31c63c80b0 | -13.30049 | -50.66674 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7ca3ed8b-abca-38b4-8ebf-fb297e667fae | -16.01779 | -59.49112 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 493b9cc1-1619-3e2c-99c6-d955c8fd6424 | -15.31333 | -46.40626 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebecf3e1-733e-31ee-8706-a52e344f047c | -13.66629 | -48.08536 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b32539a-bebb-3072-b2e6-ebfa944a1fa2 | -13.93626 | -48.10196 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05da3c2b-3ca6-3e22-898a-633393a35e0a | -16.3998 | -47.04569 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73aa8739-888a-3aeb-8d82-19bcf132ead4 | -13.76221 | -47.95969 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e620805-d318-3655-a2ed-80958eb4f8b4 | -15.16623 | -49.10123 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c7fb2bd-5497-3cc8-867b-67c4d691ea43 | -13.79724 | -51.2336 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25ca9189-f273-39a1-9f6b-2ca85f70b3c8 | -16.37723 | -47.0723 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ef6324-a7fb-3b29-85e7-72dbb29b53ed | -16.08276 | -51.04646 | 2025-10-01 05:12:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fd482de-12a1-34fc-afdd-1218794d589f | -16.0179 | -50.90801 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e0c3366-1ccf-36a7-ac66-05f795fac321 | -13.62854 | -47.64301 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb2936a6-bbac-3144-8fdc-41253d6372ea | -14.89512 | -48.12982 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68036630-d3fe-3902-9ef4-5f72ebcdb8a2 | -14.6559 | -48.13615 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1786d435-2a0c-31cb-a722-336a9ebde12a | -14.98197 | -46.95731 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24c8bbce-24d8-3f6a-8d9b-0909013ac818 | -15.37938 | -49.19537 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ce6c928-6da6-31e7-a751-c58c77d4ebfe | -13.77229 | -47.97791 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60d8ef4d-1283-38f2-bdeb-c2f2b02e33a3 | -13.76 | -48.40366 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b7e29bf-b4fd-3b31-a57d-329fc87bf710 | -14.35861 | -47.14069 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86537342-f4ce-3e6d-931d-e46882a1f656 | -14.79431 | -45.78176 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1301bb6f-3be4-3e45-b46e-8fc18b359702 | -14.18691 | -46.12562 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83fd123e-84d5-3563-b347-f46367e56a9b | -15.34139 | -56.96532 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21b72df4-c3d5-3fd9-a77a-42336b9a9747 | -14.68077 | -48.12999 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6044091c-bce0-3988-a371-ea289ec217a6 | -13.77466 | -48.32737 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01f3f30a-5ca2-3024-b7af-d7d3473a2750 | -17.89196 | -57.59008 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f945287c-c405-35f2-ac32-5f1c118f4f64 | -14.51835 | -53.12163 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d161ff49-6492-3404-bcc3-bd20a03b2346 | -14.73234 | -46.83043 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38585db6-9303-3d64-aa99-792bb5fbf6db | -15.48761 | -45.90694 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 25896b6e-2d7e-3323-94aa-528fdcc017af | -14.5986 | -48.21888 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98d34a8f-4725-3909-9a0c-103997391c42 | -14.89428 | -48.13781 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a28bfc93-8207-3b60-a004-b485720dc0c3 | -14.79293 | -45.79542 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 414f783d-7e97-3e25-8573-0d954a01561e | -14.684 | -48.23951 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2b7f556-882f-3e82-9a07-02e2163db3f2 | -15.15541 | -48.01311 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1244b0c1-4449-3a02-a2c8-1fb8bda624f7 | -14.0508 | -47.97606 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c9c6863-591c-37bd-910a-c7b2d76e2ad1 | -14.87248 | -49.71625 | 2025-10-01 05:12:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687afdb9-73cc-3b06-9838-211abb667e77 | -13.67218 | -48.08626 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1a0af69d-fd29-33d7-82a5-201798691222 | -14.51142 | -48.47718 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99b50de0-a5a3-380b-8e48-99baaf161f40 | -14.78605 | -45.7947 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e6d316d3-f013-391e-ae8e-f5d64f46643d | -14.68438 | -48.12309 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 882ea823-3f62-3df7-a372-517c92d4aeea | -14.14293 | -49.20126 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3896416b-d670-322b-8c51-1b1d30c3e604 | -17.89721 | -57.57859 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 226ae522-0d64-3f1e-bdfa-3d4402833ec2 | -14.9641 | -46.8779 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f594f3af-0fd6-3bb7-a827-bb4647d128a0 | -14.05744 | -45.04113 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 417f207e-1292-3b33-924f-f219b8e72d71 | -15.16018 | -49.1042 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d83947e-345a-3a28-8b5d-8f846a1ba0b0 | -14.88202 | -48.32917 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d7fe94b-0328-387f-916b-b335923efbb3 | -14.34749 | -45.91434 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bf6e3d3-73d5-345c-a959-9df25fa456b5 | -16.00099 | -50.87642 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59e1c7a1-a72a-39bb-92d7-835d469bb463 | -14.79155 | -45.80907 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2aef7334-ff11-3b39-99b1-c985485b90ca | -13.97947 | -44.91546 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7718ab74-421c-3eb2-827d-fa89b28ac3be | -13.76474 | -47.96193 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d1bb3aa-5866-306c-afc2-b62808040347 | -14.88832 | -48.32643 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3953bce7-c434-3b36-94e4-c7a53de62b8a | -14.91397 | -47.82676 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a22299f9-66ba-3b8f-b92a-fcba7b388fa1 | -14.88772 | -48.11846 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 126eb41b-a6f6-38ac-b8ff-cf9d8c05c2ea | -16.40451 | -47.06233 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f812bb4e-4861-3a7a-babc-f1a72cb5a666 | -14.98738 | -50.77162 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5a42f6-b9f6-32f1-bb78-ca0fe035688e | -13.79244 | -51.23296 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 709877fd-13c2-3ea9-849f-a4da8f7d6854 | -14.76245 | -45.75138 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aec14993-a15c-39c1-a744-aa75baeba2ee | -14.68587 | -48.24387 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78fca449-0455-3d5c-8f84-016dc71080e7 | -14.92759 | -47.81936 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e885e47b-a94e-326e-9b5d-4986e21624e8 | -13.81264 | -47.49686 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 099f1b4e-75f3-35c4-a78a-8430056f0248 | -15.94406 | -48.13046 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 26e0bf01-b2d7-3bbe-a852-09a855b33a2f | -17.93559 | -57.57132 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0770862d-5a7c-3663-afc4-ca1ef4a35002 | -14.59314 | -48.23182 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b25b8505-4c60-3b8e-aafe-94db5017e6ec | -16.196 | -49.99467 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 926ba7b4-7e56-3795-bf0f-6dcec15d3887 | -14.18479 | -46.11265 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7dd1514-7cfb-35e3-ae51-debdf7fc7763 | -14.35546 | -47.14319 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f7e452b-68be-3bb4-aec7-0ac02482808c | -15.39144 | -49.18956 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd05b9d1-8357-3de8-945e-86c53b7e0e89 | -12.92116 | -54.7295 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b133e1-1536-3cd3-9bbb-39252bc94d5c | -13.94033 | -48.11865 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4513b552-67e4-31fb-901e-a54fbe84d2fc | -14.88252 | -48.32472 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 719e08b1-b478-32b2-9812-8b8f44e38274 | -14.92683 | -47.82225 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47a003c3-3bcd-3a7b-8d0a-3077e26cea87 | -16.00634 | -50.87476 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3494061-4d33-3b36-a4f3-e361f3bd18a3 | -13.93453 | -48.11695 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afa66703-781a-386e-b5ac-c68422a0fba2 | -14.71805 | -48.14729 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d7c4c5f-6f41-35c1-89a8-e880eda92f94 | -14.34627 | -45.92619 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd9c2e6-bdd7-313f-bff2-2f3b46689841 | -14.10091 | -49.7557 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5503649-07f0-3c15-82d5-ac58842e5f77 | -15.25335 | -56.77919 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d15c0f80-7ed8-3855-8f2b-ba738e436ff4 | -14.68401 | -48.12662 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31358d1e-9e1f-3363-bbeb-945ff6211cce | -16.37161 | -47.06581 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a01ba89-c7f2-309a-9aab-31c65b493bdd | -14.89003 | -48.12065 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7ab75850-a1ff-3d1b-be51-ef0fc688a815 | -15.23999 | -48.75472 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ddfe2e81-adee-3bd9-8304-5a57835b8c1c | -14.50266 | -48.45015 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f60e102-8381-31bf-b647-9d52206380f1 | -14.50468 | -48.48461 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 061ca85f-57c4-3cff-8b24-fd1e2a2c1a1f | -16.11374 | -48.40588 | 2025-10-01 05:12:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9649de1-f6fd-3271-b2b3-958fbbda0171 | -14.54945 | -48.24673 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe081025-9b1c-38a5-b39a-2e804bebca15 | -15.54766 | -48.18648 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 315fc62f-55df-38ff-ad86-ef3e8eadf365 | -14.51093 | -48.48154 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README135.md)
