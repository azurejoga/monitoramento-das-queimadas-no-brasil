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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c5ce3ae-3e2e-3337-85c7-4a156badc620 | -8.5013 | -47.8404 | 2025-10-02 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| bf6ee47f-aa99-3fb3-9320-eae8c4dcc12b | -10.1837 | -50.3128 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 001c2758-c64b-3f7e-9047-2066bcde9cc6 | -10.2025 | -50.3109 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f07cda60-6e07-3972-995e-d8f99954c0f9 | -9.938 | -43.6718 | 2025-10-02 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 396f636b-aa4c-3796-9e0c-db1b9d48bfdb | -10.2403 | -50.307 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2c9343ab-9585-3f75-b09b-44ecea2e06c7 | -10.0709 | -50.2814 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 15f3dce3-7bb7-3dd0-a0f2-3615d465b3fc | -9.4083 | -47.5742 | 2025-10-02 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 6e5c4655-ee75-3d47-bfe2-b80d0093be28 | -18.1782 | -53.3024 | 2025-10-02 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 184.6 |
| f8543ec6-770c-3681-8ca4-dabe92f286e8 | -12.7627 | -50.5567 | 2025-10-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| d2199898-4235-30a6-9a4d-e9bfb6c515fd | -10.165 | -50.2933 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 026fdad1-6473-3ff2-b477-487b2cdb3848 | -6.1981 | -43.9286 | 2025-10-02 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f2a65582-1385-37db-953e-7c2a34aa8e00 | -18.2375 | -53.3145 | 2025-10-02 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 205.3 |
| fdf584bb-588c-37c7-bda5-bd5a5e3c4186 | -9.4275 | -47.5501 | 2025-10-02 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ac55f602-3ead-3f31-90f3-8de86d554ceb | -14.425 | -46.1381 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 255ef2f6-fdba-3fcb-b3f4-44298af9aeac | -10.1081 | -50.3203 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f8fb01a6-f2b9-3e04-aeb9-f40fafb936f0 | -14.3139 | -45.8811 | 2025-10-02 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| d8c88065-b13f-358e-91ee-3741a1655664 | -9.3202 | -45.7061 | 2025-10-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 44333e73-56d0-3497-9cf5-5b17750d1fde | -7.7311 | -46.2289 | 2025-10-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e5e26d16-a8da-3306-924c-d23298b56ab5 | -8.2094 | -45.5301 | 2025-10-02 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7598a497-b60e-36ec-af1a-8d01e25f4b84 | -9.7851 | -46.2851 | 2025-10-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 4303050b-54dc-39d8-9c7f-f3127c977aca | -10.9561 | -46.6594 | 2025-10-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 5a843238-c794-3905-9e6f-bc56f42ae220 | -14.3119 | -45.9736 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1818a310-87af-3797-98ea-7715e549f6d8 | -8.5204 | -47.8167 | 2025-10-02 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| c7f338c2-442d-3dd0-b54a-664c4e932d0b | -7.8879 | -47.3031 | 2025-10-02 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 0435024a-e08b-3c16-a0d2-75276d879f50 | -7.7944 | -42.5132 | 2025-10-02 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 328.1 |
| 226d4053-7850-3f38-96b5-630fb5eac566 | -14.2121 | -46.1058 | 2025-10-02 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 2fa25d71-114b-3947-85ea-a61b1b0e8bc5 | -14.9046 | -48.3228 | 2025-10-02 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0237cf7b-2ccf-31a7-b8b8-0ebce5a74e0d | -6.7814 | -45.5929 | 2025-10-02 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 792c43e1-cab7-33d1-b3e9-435ad1a5b7ab | -13.9585 | -48.1376 | 2025-10-02 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 50efc23f-1ef2-3ab5-a0ae-7de52daa78fc | -8.1702 | -44.1377 | 2025-10-02 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.8 |
| a46e2dda-7ce7-3de6-8284-f87b6a9f6c5d | -8.5201 | -47.8386 | 2025-10-02 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 1a421f23-cedd-3aab-a547-189563cb43ec | -10.1656 | -50.2506 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 4fae7191-8b16-37b3-ade3-bd927f7b4e59 | -14.3114 | -45.9967 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 9bf7fe0a-fdbd-371b-af2a-c13033b92a77 | -13.5841 | -51.8845 | 2025-10-02 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 0a035728-8b0f-3ad6-a6eb-4a088a815bfb | -11.0897 | -47.846 | 2025-10-02 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 30b08c91-2f4e-3e2e-a7c3-9ec4eee1395d | -14.406 | -46.1184 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 346.2 |
| 8c74b3f8-9373-353e-82e2-0a7e6332644c | -12.4998 | -50.2668 | 2025-10-02 14:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 77361d0c-eba3-35c2-99f0-edc3d314eb58 | -8.5272 | -47.2437 | 2025-10-02 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5ea509ee-3c75-3609-a20d-f6fa31429954 | -7.8882 | -47.281 | 2025-10-02 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 4c9fd6b1-cea2-337c-bca6-99a6b45ceea9 | -7.5746 | -46.8 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 39682c42-6df5-34f8-b0a5-1812f9b8094a | -12.5001 | -50.2453 | 2025-10-02 14:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 2cbe6fd1-0f38-3b99-aabf-9c93dbb2c3d9 | -8.7844 | -44.8085 | 2025-10-02 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 46ea28d8-b5b3-3ef6-aca3-5408bb1a2a96 | -13.7876 | -51.1974 | 2025-10-02 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 7807664b-f62e-332a-b9b4-807ec6550a3b | -6.7816 | -45.5703 | 2025-10-02 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bb096b80-8378-32d5-a19d-10193796a71f | -15.7707 | -43.7197 | 2025-10-02 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 538a43fb-9477-3fe0-851b-d1de428971e4 | -11.6314 | -45.0646 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 4a125ca5-4334-30fb-a034-dc0a29334ff0 | -14.5937 | -48.3281 | 2025-10-02 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9eb3f3c8-fa28-3777-b57d-fb786c0458e6 | -13.9779 | -48.1346 | 2025-10-02 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 267b3c4a-0337-3021-84af-177130c4afd6 | -11.5869 | -50.1612 | 2025-10-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8f5b6012-c8b8-3c51-ba7c-3b3c37153b3d | -11.5601 | -47.0069 | 2025-10-02 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 92b2540f-2c16-33e8-97ce-472d9159bc4d | -6.6976 | -42.8354 | 2025-10-02 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 252c620c-557c-3b6e-8ec4-fa7da8dbf547 | -9.4086 | -47.5521 | 2025-10-02 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 7e9cd4cd-02ce-30f8-a98d-2cdcf06f9187 | -11.8101 | -51.7957 | 2025-10-02 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7f1656f5-0ba4-332d-b7d7-ed87ca954d5a | -8.8929 | -46.6072 | 2025-10-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 8c35f9d6-093b-3e34-962c-7b6d4bc737d3 | -13.7864 | -48.0524 | 2025-10-02 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e35bff3f-b417-39eb-8d98-443e4a7087fe | -9.3389 | -45.7266 | 2025-10-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 3f8f35b6-dcb0-3711-aa40-1690fb9711b6 | -15.1444 | -48.0143 | 2025-10-02 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2ff6aba4-b566-369d-9a51-37ff5af3af72 | -5.3379 | -43.7855 | 2025-10-02 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8b88a903-5dc3-39c7-9ef5-74f24e3fa8f5 | -11.1252 | -43.3874 | 2025-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| c8645083-d811-3f7e-a337-3c7f12c76ef6 | -5.6236 | -43.23 | 2025-10-02 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6c08ffea-a2ce-3244-804a-6324651f18f3 | -9.9372 | -43.7187 | 2025-10-02 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| d7fef427-af1f-3a6a-b376-ea0c44c6949e | -8.5016 | -47.8184 | 2025-10-02 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| e71c3a4e-6b56-3f33-ba16-59882d511038 | -11.8434 | -44.9872 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c5177a79-d653-31c1-b67d-7a6c7e21c26f | -14.4065 | -46.0953 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 452.7 |
| 1827af04-20f8-3feb-886e-2754d2af7dc4 | -8.527 | -47.2658 | 2025-10-02 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 3eb47cb1-4ae9-3583-8a7c-ce3b0bd79a92 | -9.3199 | -45.7288 | 2025-10-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 214.8 |
| e114c607-7599-3145-ac8e-76a20a0da694 | -5.338 | -43.7623 | 2025-10-02 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| aa0abcb1-30a1-364a-9310-2e7fe19f32ea | -9.9376 | -43.6953 | 2025-10-02 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| e69404db-43df-3b59-99db-54a8b7692014 | -14.4947 | -48.4329 | 2025-10-02 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 9d0a9b7f-3bcb-388a-ade7-0d83861186a8 | -6.0997 | -42.4865 | 2025-10-02 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| aa44090b-d6d1-3dd1-8fce-1665f1d91f18 | -9.062 | -46.6565 | 2025-10-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 638c931f-b164-3c48-8e6f-82d522cb51c4 | -9.4086 | -47.5521 | 2025-10-02 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| b2e9e21f-3612-3ccb-8eee-36bb1387ec1f | -11.1746 | -47.2805 | 2025-10-02 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 32f176de-1078-39fe-a992-d61fdd38de55 | -14.2924 | -45.977 | 2025-10-02 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 203.7 |
| fda536d6-9645-3b73-ae0f-7c9bb8a98510 | -7.8 | -46.78 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 44256187-1a2c-37c3-8ab3-e3c1871d2559 | -7.8879 | -47.3031 | 2025-10-02 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 90565eb1-642c-37f1-b4b3-7e98193d81e7 | -10.1964 | -45.3968 | 2025-10-02 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d57b3b95-8f93-3a3c-a3d5-90a0b472cb93 | -9.8331 | -48.276 | 2025-10-02 14:30:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8bb17aab-4b33-38e2-ab5c-2bd5359a5b13 | -11.8291 | -51.7937 | 2025-10-02 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1498361c-c36b-3c0b-8a02-e5940fd891dd | -14.9046 | -48.3228 | 2025-10-02 14:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ab1d01aa-1fad-35fa-8b12-9dc4d0d7a86a | -11.6314 | -45.0646 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 28ca1fe0-e7a8-39a3-b88f-afef0530095a | -5.3193 | -43.7636 | 2025-10-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cb0824c3-020c-3d37-878c-dd8cce039464 | -13.1739 | -47.8317 | 2025-10-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b32b9abe-6e5a-3005-acf2-e818c3e86cb5 | -10.1845 | -50.2487 | 2025-10-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9df39bbf-437c-36a6-931c-82c714854c1c | -6.7629 | -45.5718 | 2025-10-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 21712e27-b974-3f02-89e6-cea96d9f267e | -9.08 | -46.7215 | 2025-10-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 16547b1d-d8e0-342f-80a3-06330bdbdc14 | -9.7851 | -46.2851 | 2025-10-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 7b0b379c-0320-3bfa-8c1c-c12a9c57806b | -5.7035 | -42.6841 | 2025-10-02 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| e722a344-97c2-3ef6-a9e2-44a313527745 | -13.7873 | -51.2189 | 2025-10-02 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.5 |
| a707d484-c42e-3ed5-b4c1-8c1d73f63d0f | -7.8188 | -46.7783 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| bf71259a-0497-3f22-9439-36e0abb05e74 | -15.3185 | -46.278 | 2025-10-02 14:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 9e345c14-da5b-3e6d-b543-07b08ebed691 | -7.4601 | -46.9872 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e4b44561-e6e2-3e67-bf55-05fe2d9019e7 | -14.7568 | -45.1985 | 2025-10-02 14:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 25eebba5-cf1d-3114-87ad-bc429ed1a67c | -8.8165 | -46.682 | 2025-10-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3cdc7026-9331-3e68-bf43-4eef1e3e95bf | -9.9376 | -43.6953 | 2025-10-02 14:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fa75be16-7851-343e-b3f9-7f16dd0368a8 | -14.7562 | -45.2219 | 2025-10-02 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 82577e26-7328-3bc0-841b-2ad9fe7eb222 | -6.4758 | -44.2978 | 2025-10-02 14:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 9a0309c0-9dc7-388f-8cf2-bcefb8e2145a | -10.9561 | -46.6594 | 2025-10-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 8b04e509-7a08-37ef-9c52-8f1d077457ed | -13.7876 | -51.1974 | 2025-10-02 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 6d888cb1-81ef-3243-8947-50c91e10017d | -9.336 | -45.9305 | 2025-10-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 324.6 |


[Clique aqui para ver as próximas entradas](README161.md)
