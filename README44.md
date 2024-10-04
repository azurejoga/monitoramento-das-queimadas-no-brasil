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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78e2eb0f-1c89-34e7-ad15-4e3d086dd1fa | -6.9733 | -71.665703 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fdc4015e-4921-3d59-9dcb-93b2316514a8 | -16.0732 | -50.3014 | 2024-10-04 02:26:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2f311ccb-b50e-39c4-8f26-ba89920d45a5 | -16.5938 | -57.1783 | 2024-10-04 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 13fc9a9c-4d55-3bee-b527-8bb58c01500a | -16.5935 | -57.1988 | 2024-10-04 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| f572e9d1-031e-3d01-9ec4-05176c492cd2 | -16.4151 | -57.3823 | 2024-10-04 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| be22d713-95ba-3d68-9ab2-08d83fb18d4b | -16.765 | -57.4652 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 7791fd2e-d700-3e65-933f-f6f5ce29d6a2 | -16.7647 | -57.4856 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 3e5597ec-3a73-383e-a16f-030715a558f8 | -16.7606 | -57.7512 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 71ab47cc-aa6b-35ef-b969-cab58f3bcb19 | -16.7455 | -57.4674 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 4085741c-b87a-35e9-9582-b10be7c830e2 | -16.6871 | -57.4536 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 2ba56cf4-e248-384f-b52a-4334a2842935 | -16.6868 | -57.4741 | 2024-10-04 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 88f3b21d-ec16-39b4-8984-0931f9da9ab0 | -16.6133 | -57.176 | 2024-10-04 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 3f96ac0a-ad57-32d7-8122-0151a290434e | -16.613 | -57.1965 | 2024-10-04 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 0951cefb-f17f-3e82-af20-791ef419957f | -16.9287 | -55.8197 | 2024-10-04 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 7d03be77-ec98-3711-b62d-25f1920008bb | -16.9283 | -55.8405 | 2024-10-04 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 9b71c8db-bce2-3381-9624-2bf4d8bb48ed | -16.9087 | -55.843 | 2024-10-04 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 9fa9941f-1355-3ee3-bfad-f41c154960f0 | -16.8433 | -57.4562 | 2024-10-04 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 50ef7cfe-d3c1-357d-9262-0187436902df | -16.843 | -57.4767 | 2024-10-04 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| ebc75c65-3253-39ee-b2f3-5578c7728f71 | -16.8055 | -57.3788 | 2024-10-04 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| a3b8b16d-9cf7-3cb4-ba60-430fc5734d83 | -16.7843 | -57.4834 | 2024-10-04 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 6ab8bc21-a739-34e9-9cdb-99b8a440c3c7 | -17.0616 | -56.0723 | 2024-10-04 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| bef35a3b-0d79-3f2a-bb44-e888b1969632 | -17.0512 | -56.6932 | 2024-10-04 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| ebb65b1d-e175-3235-8bb8-d0963978cb99 | -17.3844 | -42.6235 | 2024-10-04 02:26:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ae45ccb4-5665-38c3-91c0-866377a7bdbf | -17.1771 | -57.3969 | 2024-10-04 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| a668d697-f688-33b1-9571-da985853fc29 | -17.1574 | -57.3993 | 2024-10-04 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 47af0903-7a6b-35d6-bba0-d6cf46152812 | -17.7508 | -43.8079 | 2024-10-04 02:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 24cabc80-043a-3a6b-8ba0-4ee65961fefa | -18.9285 | -42.0259 | 2024-10-04 02:26:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 104f60b5-4bcb-3d09-aae7-07a83fbd59e7 | -18.8613 | -43.5837 | 2024-10-04 02:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| f8a354b0-9f7e-3f2e-a061-b25a164f2a0b | -19.3167 | -42.5724 | 2024-10-04 02:26:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.7 |
| cd08182d-70fa-30b7-8d01-bf077fa6d876 | -19.3159 | -42.5976 | 2024-10-04 02:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.2 |
| 630fe7ff-dff6-3d12-a2d3-5cec10c3ea79 | -19.8516 | -42.3738 | 2024-10-04 02:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| 85e6bb94-98b3-3631-b5be-33872a79b595 | -20.121 | -43.5219 | 2024-10-04 02:26:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| 17e457d3-5736-342d-a683-bddd8827431d | -20.0111 | -48.6869 | 2024-10-04 02:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4fec9c45-5360-3677-b035-c5b8eb1e4301 | -20.0104 | -48.71 | 2024-10-04 02:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e9cd83cb-030d-34ac-b99b-7f4c4de7e1ff | -20.1416 | -43.5162 | 2024-10-04 02:26:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| b1454eab-977c-3db2-b12a-f83034418860 | -19.9907 | -48.6913 | 2024-10-04 02:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 161ee9b1-8663-30de-a14f-1fe1cac51820 | -19.9901 | -48.7144 | 2024-10-04 02:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 81896271-40ce-31b3-a8a8-a16b712a7140 | -21.8397 | -48.3826 | 2024-10-04 02:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6cb7d789-3942-32b9-b498-0d627aabe4f9 | -21.8196 | -48.3641 | 2024-10-04 02:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c2e63166-1544-364f-9a3d-7dde2021bbbd | -21.8072 | -48.786 | 2024-10-04 02:27:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 476eecda-4706-3b84-bad6-b6725aa05c94 | -21.7988 | -48.3691 | 2024-10-04 02:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 132.0 |
| bf1ad96c-20f9-3335-b3b5-849bfaff8f3e | -21.7981 | -48.3926 | 2024-10-04 02:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 831daebc-2798-3d34-b0d9-72b48c0aa1f8 | -22.269 | -51.4714 | 2024-10-04 02:27:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| 01e47453-a96c-37d4-9653-9d4e39dd4214 | -22.2684 | -51.4941 | 2024-10-04 02:27:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 9d4ab880-178b-315b-9b8e-7ced07eb6e13 | -3.2349 | -50.3695 | 2024-10-04 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5068d56e-92d8-31bb-8e71-cff037af6916 | -3.2534 | -50.3689 | 2024-10-04 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 30eea8de-9fed-3607-96fa-50066d5b82a0 | -3.2899 | -50.4725 | 2024-10-04 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 355b8382-8b07-30d5-bfd4-e3bf72b8b396 | -3.2899 | -50.4516 | 2024-10-04 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 61185868-e589-3414-9c7a-5626f699a092 | -3.3083 | -50.4719 | 2024-10-04 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 388f389e-1fd4-3a91-a14a-e28b0b3aa8de | -3.3084 | -50.451 | 2024-10-04 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 198.1 |
| e079480a-6634-3e5b-b1ef-3855090c3e8c | -4.0763 | -48.4902 | 2024-10-04 02:35:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8343d820-b29f-3608-83f6-2a31596444b7 | -4.0949 | -48.4894 | 2024-10-04 02:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| b9f073e3-f0aa-357c-9899-c1f82e829f6b | -4.095 | -48.4679 | 2024-10-04 02:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e24fb6a4-b74c-3b8d-bbad-5a4f5e2d08d6 | -4.5375 | -43.304 | 2024-10-04 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 93f5f166-d7fa-3bb6-9451-2372658941c0 | -4.6684 | -45.8961 | 2024-10-04 02:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 99aa3b6b-634c-3309-9406-51791afa8cb0 | -4.6686 | -45.8738 | 2024-10-04 02:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 9803193d-5b04-30f7-9044-9b6201b10ffd | -4.687 | -45.8951 | 2024-10-04 02:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 281.5 |
| 61fa0004-e91e-3005-96c9-d4cbbcf73ae3 | -4.6872 | -45.8727 | 2024-10-04 02:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 437.4 |
| a20e5d0e-700f-3e29-8856-438cfd2af9de | -5.8214 | -44.1426 | 2024-10-04 02:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 68f43a85-8d9b-3b38-b9c6-fc7a5eb0da00 | -5.8216 | -44.1196 | 2024-10-04 02:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8919584d-f299-3d07-8215-a65276668c83 | -7.0529 | -71.7726 | 2024-10-04 02:35:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b03e5ebf-8322-33e0-aa59-9b640928d96c | -7.0529 | -71.7544 | 2024-10-04 02:35:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| fdf4b341-6152-3514-9e62-0b77f9ee6471 | -7.8539 | -45.3611 | 2024-10-04 02:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 71d0fd5c-d7fe-385c-8e35-00c0fa4ac99a | -9.0853 | -50.9036 | 2024-10-04 02:35:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 8577f837-be49-39e3-b441-3deb3441bd07 | -9.1039 | -50.9231 | 2024-10-04 02:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| a6cc71a0-542f-3053-9e67-bade9c94bd36 | -9.1041 | -50.902 | 2024-10-04 02:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 4d956948-e2a4-3ddd-9e43-96af7d9cbc28 | -9.0898 | -67.4997 | 2024-10-04 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 51831ad8-cabc-3187-a6a7-4cfb93c9f847 | -9.1084 | -67.4993 | 2024-10-04 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e2d15241-27be-32c5-a47f-e5e36de5b019 | -9.3115 | -50.8203 | 2024-10-04 02:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 9891d803-c850-3092-bcd6-4f976066f059 | -9.3118 | -50.7991 | 2024-10-04 02:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 3cefc2bc-20a9-3638-a667-9f125ca20a82 | -9.312 | -50.7779 | 2024-10-04 02:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f6ab44fe-52dd-3bb4-8d3a-239c7cd0b41e | -9.3303 | -50.8186 | 2024-10-04 02:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 26dea0d4-17a5-3398-a1ce-556bae4f94f2 | -9.3306 | -50.7974 | 2024-10-04 02:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 177.5 |
| d70a3cdd-97f3-3e23-9a33-7a3374d2b8eb | -10.4424 | -50.7336 | 2024-10-04 02:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d719a772-8de3-3930-9be1-dc62e5982029 | -11.6181 | -64.9818 | 2024-10-04 02:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a768624d-47bb-31a2-8fed-9538cd27e062 | -11.6369 | -64.981 | 2024-10-04 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8c3bb06a-9c4c-3f76-99dc-4568b7b61903 | -11.6932 | -64.9785 | 2024-10-04 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 47ea1925-dab1-3f34-a744-7328ea0ce0c4 | -11.8242 | -56.6009 | 2024-10-04 02:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d920104c-9294-36b6-86e6-9b2adfd3ccac | -12.4225 | -63.019 | 2024-10-04 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5dd0d717-9b5f-3ce1-8150-4966e2f59551 | -12.4414 | -63.018 | 2024-10-04 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0533c58f-bc4b-33ba-a649-9d6a44b08ec2 | -12.5898 | -53.1359 | 2024-10-04 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| a4c05003-aca5-33e7-8705-cf06bba619f3 | -12.5901 | -53.115 | 2024-10-04 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| c791e4ad-e53f-3a40-a1fd-36d8952c1539 | -12.6092 | -53.1129 | 2024-10-04 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 90c79172-37e8-31e5-89ee-3fbe0a03cd93 | -14.7939 | -48.0275 | 2024-10-04 02:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0ea45616-f6af-3fb1-a988-995f729ed06a | -16.4151 | -57.3823 | 2024-10-04 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| ca1e6fd4-eb75-3578-bccc-69f1bfce6c69 | -16.5733 | -57.2419 | 2024-10-04 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 896c3375-186f-3b2c-832f-42d550cb5e09 | -16.5935 | -57.1988 | 2024-10-04 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 3c612705-de70-3e30-ac30-00b5ad42353b | -16.5938 | -57.1783 | 2024-10-04 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 8dc9101a-26a0-33d5-84db-265380f0737b | -16.613 | -57.1965 | 2024-10-04 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 38e8ff9b-6b5f-3472-89b8-c533c1c4d4b1 | -16.6133 | -57.176 | 2024-10-04 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| d53009a1-616d-38ee-804e-d093503438fa | -16.6868 | -57.4741 | 2024-10-04 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| ca24d14b-9826-33ac-89b7-49d3b4944450 | -16.6871 | -57.4536 | 2024-10-04 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 23625845-2acf-353e-8722-fac08b2fb3c5 | -16.7455 | -57.4674 | 2024-10-04 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| dae7f577-2920-3341-8da6-fff3444d4626 | -16.7647 | -57.4856 | 2024-10-04 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| c9c05870-0454-3175-a037-1e4f65643900 | -16.765 | -57.4652 | 2024-10-04 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 9831e1c4-b945-37c9-add3-5014eda57d9c | -16.7843 | -57.4834 | 2024-10-04 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 2c2696e4-1b5b-3f3e-a12d-dd848b2b2803 | -16.8055 | -57.3788 | 2024-10-04 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 58a7e2af-dd03-340f-8510-0b03e546c572 | -16.843 | -57.4767 | 2024-10-04 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 0f7f1021-0303-3018-b55f-baeae902d8a2 | -16.9283 | -55.8405 | 2024-10-04 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 87e3dfd1-8c83-3ccb-90e4-016a09cd7661 | -16.9287 | -55.8197 | 2024-10-04 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |


[Clique aqui para ver as próximas entradas](README45.md)
