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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63941af1-778e-3bae-8448-e2d971e641ba | -16.8096 | -55.9177 | 2024-10-02 01:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| b9ff10e2-b8ec-3d4f-a8bb-1e339f255668 | -16.7647 | -57.4856 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| a49ba856-e525-39bf-bb83-318b7313f5c2 | -16.7452 | -57.4878 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 192ca1b0-8b2c-3aee-81cd-97f436b26bc8 | -16.8695 | -55.848 | 2024-10-02 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 5b9024e8-500c-32df-bd18-aaeb3294f4d4 | -16.8491 | -55.892 | 2024-10-02 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 6dc12fa4-f6ea-3fcf-bf5f-5b51b1b24240 | -16.8234 | -57.4789 | 2024-10-02 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| a3428561-162b-369c-aea1-df072b6e99c6 | -16.8299 | -55.8737 | 2024-10-02 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 53205837-32f0-324a-b34a-d12ce0ca5277 | -16.8295 | -55.8945 | 2024-10-02 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.3 |
| b4910e7b-c526-3c6f-b01b-a2d938d93105 | -16.8292 | -55.9152 | 2024-10-02 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| cd8bb775-7cfe-3bcf-8cd2-a1025d7017d2 | -17.1581 | -56.1637 | 2024-10-02 01:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 663e1fc8-1762-3b8d-9ba6-0118e7096793 | -17.1091 | -56.7479 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| b52f8ed4-5354-3ad8-b1b9-fbd2cfbdaf24 | -17.0895 | -56.7503 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| d26dee68-09ca-3079-bf2c-269360a88dd1 | -17.0892 | -56.7709 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 320fbed5-6caa-38e6-a825-458141f05f70 | -17.0709 | -56.6908 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 0252523f-3e0e-330e-9554-3c8c1ca2b019 | -17.0705 | -56.7114 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 58d588e5-1aa0-35b4-95a0-a50d1790b0f6 | -17.0502 | -56.7551 | 2024-10-02 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 96a12887-ffb9-3898-be71-c710f539e515 | -19.2317 | -46.8687 | 2024-10-02 01:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5cd6957a-88b1-3504-906b-ed271aaef16b | -19.2323 | -46.8452 | 2024-10-02 01:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7aca990b-d764-3a22-bb32-6a7454cc8c28 | -20.0424 | -55.9738 | 2024-10-02 01:56:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| e73bdb9a-ee34-3b71-8717-7847419a8954 | -20.5266 | -46.2783 | 2024-10-02 01:56:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e397fd3d-1257-332d-97f2-bdd5a4e72c33 | -21.3451 | -55.7056 | 2024-10-02 01:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5e9d4807-c36c-31fb-b8a1-05952a98ae73 | -21.3456 | -55.6841 | 2024-10-02 01:57:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 112.8 |
| f916c9b8-2a85-3d4d-9716-5bc277bde5b9 | -21.3661 | -55.6807 | 2024-10-02 01:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0587b906-1dbd-3b2d-98fa-2b4649fb1240 | -22.3713 | -49.3011 | 2024-10-02 01:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| 960aa0f4-3ec6-31fa-bd1e-ec1b4f2dca72 | -22.372 | -49.2777 | 2024-10-02 01:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| 05e25d15-48b7-3d82-a345-c04f962c6744 | -22.9006 | -45.1029 | 2024-10-02 01:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 4d102dae-07f4-3ef5-80f2-b1600306c4aa | -22.9277 | -43.7243 | 2024-10-02 01:57:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| de280c21-1f74-3cf5-a4b1-4022c5d4345e | -22.37 | -49.34 | 2024-10-02 02:03:15 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44814dd5-a6a7-31d6-ab95-b7167359a29d | -22.37 | -49.28 | 2024-10-02 02:03:15 | MSG-03 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9877189-e154-3c2d-9380-3809c3a46a61 | -16.56 | -58.24 | 2024-10-02 02:03:52 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 461a87b2-2ffe-3c40-a1d5-5a58ff98ce04 | -16.59 | -58.26 | 2024-10-02 02:03:52 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 223532ef-3e9f-3502-b26e-e948e32f1398 | -13.11 | -51.42 | 2024-10-02 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39a76437-56b7-3b9c-94c1-af8621844df2 | -13.08 | -51.47 | 2024-10-02 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8445059-d529-3de9-9254-0cdefe1effd8 | -13.08 | -51.41 | 2024-10-02 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9230b280-b60e-3ca6-8b05-ed62af5c2f2b | -13.11 | -51.48 | 2024-10-02 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f20c7a47-92ab-330e-8981-d0e0d1b72daf | -5.9788 | -45.3621 | 2024-10-02 02:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d42f368a-3e7b-3fa7-8ed8-11b5175c0f5d | -6.1301 | -47.2664 | 2024-10-02 02:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 185f778b-99b5-34ed-adcd-b1bd6ad613db | -7.1796 | -46.9444 | 2024-10-02 02:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a1c56d49-2832-3384-8738-0ce85151f6a4 | -8.4643 | -62.7124 | 2024-10-02 02:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 665a9dd3-701c-3fe4-b184-47bacc23be92 | -8.4642 | -62.7313 | 2024-10-02 02:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 19930a70-b2a3-3c93-bab1-9044c7029972 | -9.9367 | -64.9179 | 2024-10-02 02:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| ed1e91b0-1015-35a5-9ce8-f732cc37f2ec | -9.9368 | -64.8991 | 2024-10-02 02:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 65b8e698-4b22-3bb5-a845-3f84a30651e6 | -9.9553 | -64.9172 | 2024-10-02 02:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 57b8ecec-04e1-3203-9f33-a70f047e7596 | -9.9554 | -64.8984 | 2024-10-02 02:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 93870f76-34d7-3bed-a0d2-2189a0fbb771 | -10.626 | -55.8752 | 2024-10-02 02:06:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5f09de42-33f4-3fb4-8b62-9fde12ee9b2d | -11.6554 | -65.018 | 2024-10-02 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 31677e70-7839-3d9e-a5a3-7035c8d89057 | -11.6555 | -64.9991 | 2024-10-02 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d560d731-2bfe-32fd-b842-4fe302b238e5 | -11.6742 | -65.0172 | 2024-10-02 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2650c867-b2ed-3175-9311-20bb40d86bac | -11.6743 | -64.9983 | 2024-10-02 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.3 |
| f86b5816-c616-3102-b783-65496423db07 | -12.2946 | -47.6446 | 2024-10-02 02:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 705237c7-4d51-30d9-a5b9-bf0bb8e5c93d | -12.4433 | -43.7242 | 2024-10-02 02:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| dbb6856e-c2b7-302b-b831-879644e72b7a | -12.6484 | -63.1214 | 2024-10-02 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 3c0110d2-4370-363f-b81b-879879ac4d5b | -12.6486 | -63.1022 | 2024-10-02 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ea48f46c-b2ef-342f-b5c6-592ab57134a5 | -12.7054 | -63.0798 | 2024-10-02 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9da33883-c9e2-3bfd-b8e7-8ad01e8f3140 | -12.8615 | -62.5129 | 2024-10-02 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| dc654368-c434-33c1-a368-2d848da54d63 | -12.8423 | -62.5526 | 2024-10-02 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |
| ccb2f65c-4a80-3719-a961-d6b96b6eff1c | -12.8614 | -62.5321 | 2024-10-02 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 11b5e12c-64eb-3984-a3d0-7ee83a255675 | -12.8593 | -62.7826 | 2024-10-02 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bfc257e3-2292-3ac7-9bca-3666e618abae | -12.8426 | -62.514 | 2024-10-02 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 25881176-38f9-3f3e-9818-1f98f5b75d8c | -12.8424 | -62.5333 | 2024-10-02 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 862e66ba-3afd-36fe-b6f8-ccc346861ffe | -12.9548 | -62.6806 | 2024-10-02 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e6e07200-b2b6-3bcd-b8cc-1cf7ba1425e8 | -12.9546 | -62.6999 | 2024-10-02 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 5180eb86-af3a-3135-a95a-dfbd251fb7ca | -12.9357 | -62.701 | 2024-10-02 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 3105bac4-bb75-3760-8a50-1006c9609af1 | -13.5965 | -51.1367 | 2024-10-02 02:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 081499aa-d7c2-3f75-98a3-b355858765cc | -15.139 | -55.8285 | 2024-10-02 02:06:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 0d18787c-fd8c-37ff-9af2-24f90553fe99 | -16.6124 | -57.2375 | 2024-10-02 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| b6791593-4521-397c-934a-fd66f1be910f | -16.4536 | -57.4188 | 2024-10-02 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| 82ce2154-24fc-3816-b8c6-1c77e5201c9b | -16.4533 | -57.4392 | 2024-10-02 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| 7924b267-de9e-38a0-b1a7-fa2af3bd02b5 | -16.7862 | -57.3606 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 1db54720-2812-363e-bba4-fbf8daabd77d | -16.7461 | -57.4265 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| e431d601-42d7-338e-b9e2-b94e76836b54 | -16.7455 | -57.4674 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 8274b90c-77f8-352f-8848-e8b6e77a8f85 | -16.7082 | -57.3491 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 4efc66e0-79f0-399c-bf34-cc986bc2c364 | -16.7063 | -57.4718 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| a97215c2-d84c-3009-b824-d473521cb2b6 | -16.6912 | -57.1875 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| b6033894-749a-3653-bddb-a6bf894f3550 | -16.689 | -57.3309 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 03ae937d-861a-3f33-a810-76d270890ab0 | -16.6887 | -57.3513 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 5c19d817-b772-3727-b069-06f1e695ab27 | -16.6884 | -57.3718 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 855ab55e-a740-331b-93ca-3c356b389089 | -16.6717 | -57.1897 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| a4776d92-031f-3cf6-9478-78d2d54e3617 | -16.7452 | -57.4878 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 346665e4-ea4f-3efb-8688-7e2debbd3781 | -16.7269 | -57.4083 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.0 |
| 7116fea7-570b-3d24-b5ea-1731d828fa45 | -16.7265 | -57.4287 | 2024-10-02 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 4ef6a1b7-e637-3cb9-81ec-525777a11908 | -16.7086 | -57.3286 | 2024-10-02 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 1571e50c-672f-34df-ae9b-1d98fae805f0 | -16.8295 | -55.8945 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 132.0 |
| b34e41b7-fb59-3657-98a9-c3d06350dff4 | -16.8292 | -55.9152 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 9f4e66e4-25cb-3f29-b997-0e6abeead6c6 | -16.8891 | -55.8455 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| ee6a11f9-c033-3475-9be7-4b8d33df244b | -16.8698 | -55.8272 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| a6e5a37e-810e-31b2-b383-4030a1221633 | -16.8695 | -55.848 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 16c860fc-fde0-397f-8c56-6c3755854acf | -16.8491 | -55.892 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 06fe03a0-aedc-32b9-8305-04686685bb84 | -16.8299 | -55.8737 | 2024-10-02 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 83531648-c179-3c74-9c12-918aebf24ffb | -17.1581 | -56.1637 | 2024-10-02 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 96ce8a78-5066-3c35-bc15-9844f43b20f9 | -17.1577 | -56.1844 | 2024-10-02 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 4478bd9a-efe3-3ab6-abc2-801ae507c719 | -17.0895 | -56.7503 | 2024-10-02 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| b888dca9-175a-3086-bff0-3e5b6c807482 | -17.0892 | -56.7709 | 2024-10-02 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| e09c78ba-be88-384f-990a-9cbe470aeea7 | -17.0695 | -56.7733 | 2024-10-02 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 30b6b4ea-7ee7-3bbc-a96d-1f39dc4165db | -17.0502 | -56.7551 | 2024-10-02 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| ae936fec-7d8e-3f7d-b264-8551f625a792 | -19.2519 | -46.8641 | 2024-10-02 02:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e2977b26-7a81-3e61-82cb-6a37f6778ab9 | -19.2526 | -46.8406 | 2024-10-02 02:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4b5376f3-3f9c-38be-a70f-8353b03df3d9 | -19.4435 | -43.0612 | 2024-10-02 02:06:53 | GOES-16 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| 03660a50-12c3-377c-ac02-45776304c153 | -21.3451 | -55.7056 | 2024-10-02 02:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e1fb4e22-2493-35b3-b10d-f4c4c5cf1c16 | -21.3456 | -55.6841 | 2024-10-02 02:07:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 134.7 |


[Clique aqui para ver as próximas entradas](README42.md)
