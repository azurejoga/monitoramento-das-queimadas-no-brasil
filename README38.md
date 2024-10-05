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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bad164e-429e-3687-a044-f884b6b5b1f2 | -18.6981 | -57.2915 | 2024-10-05 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| e82b9403-c063-30c8-80a9-419ba5cd9208 | -19.0944 | -48.2415 | 2024-10-05 03:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 94ed9b9d-0347-3dce-8539-04a74c75b6c0 | -19.095 | -48.2184 | 2024-10-05 03:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a4eeb923-f300-339d-8ad2-6fe609333044 | -20.9378 | -49.033 | 2024-10-05 03:27:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 1213e5ac-ec25-36b2-a4af-038d39856828 | -20.9385 | -49.0098 | 2024-10-05 03:27:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.3 |
| e4ee76d1-6eac-36fb-8c47-8ffbdc965982 | -21.6711 | -54.8324 | 2024-10-05 03:27:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e9de667c-859b-3c5a-b869-5a103db61ac5 | -4.0794 | -47.9502 | 2024-10-05 03:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b5375317-7496-313e-b714-c21969cfab63 | -5.8214 | -44.1426 | 2024-10-05 03:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 51332358-99cd-3743-bafa-22a78e7ed3cf | -5.8216 | -44.1196 | 2024-10-05 03:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8bd5fb14-152c-37b9-8b18-3922d65c3a56 | -6.9514 | -59.0666 | 2024-10-05 03:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2e3566c3-bb79-3c0f-8a23-b2bd05a88592 | -7.5193 | -63.2558 | 2024-10-05 03:35:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5d054f81-b151-31b0-b642-dfff472e8c67 | -8.7652 | -44.8335 | 2024-10-05 03:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 201da7a5-3372-39dd-8bee-62926f363fb7 | -8.7655 | -44.8106 | 2024-10-05 03:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| e62efa28-962d-3949-9146-13baf5756457 | -8.7841 | -44.8315 | 2024-10-05 03:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ce8aae73-d6a1-3b54-b094-de4e3d313473 | -8.7844 | -44.8085 | 2024-10-05 03:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a30cd125-5b18-3f14-b753-63f6535345ec | -8.7584 | -49.9566 | 2024-10-05 03:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| da706203-b24d-3efb-a8b7-27ecd4918df2 | -8.7772 | -49.955 | 2024-10-05 03:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 96bea062-07b1-39e7-925f-cb976a2cfca7 | -8.7959 | -49.9533 | 2024-10-05 03:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 95556fe8-5aa0-3bdf-a8cf-e6feced2d11f | -8.9851 | -49.8297 | 2024-10-05 03:35:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 868b1a72-e69d-3627-a4e0-ad35bceef77e | -8.9853 | -49.8083 | 2024-10-05 03:35:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7e06dfb6-2f89-37cb-91b1-ffbb2e722d7a | -9.9505 | -44.0908 | 2024-10-05 03:36:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 540fda81-3898-3534-b281-e6b01264e47f | -10.294 | -50.536 | 2024-10-05 03:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| fd9b23fe-b030-3ef6-9aed-66f3c034157f | -10.2942 | -50.5147 | 2024-10-05 03:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 54e86893-e3f6-3ffc-9d4a-a6fe0206691b | -10.3129 | -50.5341 | 2024-10-05 03:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 45f0b2e4-2e0a-369d-a1b9-ebeb26514e5a | -10.3131 | -50.5128 | 2024-10-05 03:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a3b25ff9-d9aa-3deb-9d66-eecbff6748f7 | -13.1047 | -46.3778 | 2024-10-05 03:36:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 389f5e26-00d2-330c-bef7-dc9f1bdf94fa | -13.1052 | -46.355 | 2024-10-05 03:36:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 1f7566c7-1bd4-3299-9fcb-190d9a61e393 | -13.1245 | -46.352 | 2024-10-05 03:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ce55d5bb-c696-3ab7-a38f-5e74f19aa237 | -14.0373 | -45.1882 | 2024-10-05 03:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d7e7b250-a24a-3d9e-b356-620ac7f6d6c9 | -14.0567 | -45.1847 | 2024-10-05 03:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| dfca1e17-63d9-3e71-aa50-21baef59a7a0 | -16.554 | -57.2237 | 2024-10-05 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.7 |
| fd614ea3-8084-35bd-8f52-28423d5c2699 | -16.5345 | -57.2259 | 2024-10-05 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| da422294-6c50-39ca-86f2-2e581e995770 | -16.4155 | -57.3619 | 2024-10-05 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 91c27699-a7ca-3e50-a5fd-c27074ea9237 | -16.765 | -57.4652 | 2024-10-05 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 23e40d19-a111-36d6-824f-88ca81b81c96 | -16.7647 | -57.4856 | 2024-10-05 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 132ba2c4-315a-3eb1-8db0-24e4491d76e1 | -16.7644 | -57.5061 | 2024-10-05 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 90041c3b-2b8d-3f81-815c-153a96cf6871 | -16.7843 | -57.4834 | 2024-10-05 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| efb37fd3-895e-3f24-8c97-18d81bb651c7 | -17.1375 | -57.4221 | 2024-10-05 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.2 |
| 106deea4-be6c-3676-991e-5bf8b610fc82 | -17.1378 | -57.4016 | 2024-10-05 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.8 |
| 05296b7d-931e-35d4-8c56-3e12baa0fecd | -17.1182 | -57.4039 | 2024-10-05 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| 3dd4e93b-7424-3d5c-9aac-3ad52da4a478 | -17.1178 | -57.4244 | 2024-10-05 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 674825f6-d8b0-3b5e-a907-7219a7629bc2 | -17.7112 | -43.793 | 2024-10-05 03:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b83d707f-9637-3784-9847-d7a9731799aa | -18.4853 | -52.8659 | 2024-10-05 03:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 6918ced0-0c77-32f0-b924-4af05463dd4e | -18.4858 | -52.8442 | 2024-10-05 03:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| bb1b5b04-f49e-30b0-a890-842fb066ceee | -18.5053 | -52.8626 | 2024-10-05 03:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 8d947c01-e6a9-37d4-9397-45baf30e10cc | -18.5058 | -52.841 | 2024-10-05 03:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 31878caa-058f-3874-b8e9-5ad64b59870e | -18.8606 | -43.6084 | 2024-10-05 03:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 1efce108-ae1d-3aa5-8cbe-00c265b080b5 | -18.8809 | -43.6032 | 2024-10-05 03:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| da13a4cf-6e0c-3dc9-8b7d-8fb19ea576d0 | -18.8816 | -43.5785 | 2024-10-05 03:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| 83e0b052-22a8-3fc4-8c2c-dc1f82103364 | -18.6582 | -57.2967 | 2024-10-05 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 32314731-5507-3cf5-b001-3107d60f7d8f | -18.6586 | -57.2759 | 2024-10-05 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| ca48b9a1-35cd-375b-9731-2f62eca23525 | -18.6782 | -57.2941 | 2024-10-05 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| f1127012-c9dc-3ca1-8485-318f60843301 | -18.6785 | -57.2734 | 2024-10-05 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.9 |
| 4e6888fc-0f76-310b-870d-2a15c1580c8b | -18.6981 | -57.2915 | 2024-10-05 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 2988941b-7aa2-3755-be87-f1a4d354c8b9 | -19.1374 | -46.6325 | 2024-10-05 03:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 073922ee-0915-37b0-a253-6c36a55b473b | -21.6711 | -54.8324 | 2024-10-05 03:37:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e5ccf801-4e96-3758-8d6c-be9c521f4e5c | -3.3083 | -50.4719 | 2024-10-05 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 3215db3a-1d79-3069-b056-851b16cee25e | -3.3084 | -50.451 | 2024-10-05 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 4d272a89-9037-386b-8c56-5ae06bd12254 | -5.8214 | -44.1426 | 2024-10-05 03:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 6f80c861-d419-3567-af43-c21bc7b0c6b5 | -5.8216 | -44.1196 | 2024-10-05 03:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7d1ae94a-73bf-35aa-ab3e-6d3704f9d8c0 | -6.9514 | -59.0666 | 2024-10-05 03:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c9e9e1ba-d37e-3da5-9361-d233652d5736 | -7.5193 | -63.2558 | 2024-10-05 03:45:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 236f6691-23b8-3b3a-994c-527465f841b4 | -8.7652 | -44.8335 | 2024-10-05 03:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 5c00ef7a-da22-322e-9f75-77aceef06e6b | -8.7655 | -44.8106 | 2024-10-05 03:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8fe5deb7-ee62-3871-a301-deb164961d74 | -8.7772 | -49.955 | 2024-10-05 03:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 375c5a56-cdb7-3b0b-a558-0c5e551332b2 | -8.9851 | -49.8297 | 2024-10-05 03:45:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4bacf8bd-f848-3fbf-b774-a6a89bc5ebd0 | -8.9853 | -49.8083 | 2024-10-05 03:45:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d9af6ae8-e08b-3585-9689-a034d71323a2 | -9.1759 | -61.5794 | 2024-10-05 03:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 543a7d38-4976-31f1-bef7-e87ca4157404 | -10.2569 | -36.3362 | 2024-10-05 03:46:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 2ed29035-8c89-3dd3-a03c-48aa201f9c63 | -10.2762 | -36.3327 | 2024-10-05 03:46:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| 1ecb1a52-3623-3f54-ae3c-ec1996dc2219 | -13.1047 | -46.3778 | 2024-10-05 03:46:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 507612ce-6164-313e-af48-e27579031826 | -13.1052 | -46.355 | 2024-10-05 03:46:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 1c5c620d-9bb8-3faf-aa9d-a8f2e8f381e3 | -13.1241 | -46.3748 | 2024-10-05 03:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c4e3e3d8-bc38-32c3-a087-d9030eb6d46e | -13.1245 | -46.352 | 2024-10-05 03:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d368d15d-ca07-37b4-87b4-17eaad31ff5e | -14.0373 | -45.1882 | 2024-10-05 03:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5e9c6d94-432e-389d-9443-dfd500b1320b | -14.565 | -48.7995 | 2024-10-05 03:46:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 83a58009-e2ac-35eb-8cc8-5dde9dca3cd3 | -16.554 | -57.2237 | 2024-10-05 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.2 |
| 087d8a88-b943-3b4e-9bae-8b0186f70399 | -16.5345 | -57.2259 | 2024-10-05 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 0548ef82-c536-39e9-b2a0-a960b980d6b5 | -16.6601 | -55.501 | 2024-10-05 03:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 04dbad09-50e8-330f-b180-11bb7f621ae6 | -16.7647 | -57.4856 | 2024-10-05 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| 9eb8b832-6dc8-3c7b-bd24-22a0d5c42638 | -16.6871 | -57.4536 | 2024-10-05 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 9b07906b-e86f-38ad-867a-e32a4d31f879 | -16.6402 | -55.5243 | 2024-10-05 03:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 36d3d5f6-8458-3e80-b04c-7c235e458847 | -16.6405 | -55.5035 | 2024-10-05 03:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| afe4ea6a-5324-3777-83e9-ab7883509ed7 | -16.7644 | -57.5061 | 2024-10-05 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 47b3abaf-239e-3243-848a-35481a824b4e | -16.6598 | -55.5219 | 2024-10-05 03:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| db6eaf6b-6891-375d-9197-22cb1414a552 | -16.7843 | -57.4834 | 2024-10-05 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 4ee84624-c9ae-3c65-ad48-4af0fd965ae4 | -17.0888 | -56.7915 | 2024-10-05 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 72f4e586-6d83-33ea-bf1b-262b432d1181 | -17.1375 | -57.4221 | 2024-10-05 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 8eccbab0-5822-30d8-a603-577ae2288c1b | -17.1235 | -51.7238 | 2024-10-05 03:46:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 9d90d3b5-cd5b-34c0-8ace-2c215e1ef933 | -17.1433 | -51.7206 | 2024-10-05 03:46:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 200bc509-0321-3d81-a1b5-c5f8aeb1af33 | -17.1178 | -57.4244 | 2024-10-05 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| 68b149a5-8e23-3e71-aad0-526789acf4a1 | -17.1182 | -57.4039 | 2024-10-05 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.3 |
| f7c0ee3a-40ce-32d5-9204-efcaf4fe004c | -17.1378 | -57.4016 | 2024-10-05 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| c0cc8926-b0ce-37d1-8c1e-044d4d21307d | -18.5058 | -52.841 | 2024-10-05 03:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e1eae9c7-84bd-3a18-a974-1014e3e99cb8 | -18.8606 | -43.6084 | 2024-10-05 03:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 578bd86f-fa3a-3641-aca0-09ebf0a0d51a | -18.8809 | -43.6032 | 2024-10-05 03:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| c03eae89-b19f-35ff-8e1e-3f834fa2ca84 | -18.8816 | -43.5785 | 2024-10-05 03:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| b1fd1b2d-33b6-3f43-8903-73b024f5b8ed | -18.6582 | -57.2967 | 2024-10-05 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| ec9c70ec-4dc4-3a2f-a7f4-514dffa3c1a9 | -18.6586 | -57.2759 | 2024-10-05 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 3e390845-f1cd-32e3-bebe-ab5fc096c100 | -18.6782 | -57.2941 | 2024-10-05 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |


[Clique aqui para ver as próximas entradas](README39.md)
