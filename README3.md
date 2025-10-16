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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90bd57f7-9199-3866-8265-4d473309fa69 | -7.9442 | -44.115 | 2025-10-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3438c53e-d172-35fd-8f0c-586dcb32cb66 | -9.0829 | -47.9594 | 2025-10-16 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d246a55e-b4c0-31b9-8e2c-663a828173e8 | -4.3687 | -43.3838 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 406.7 |
| dd112ba1-0a5b-3642-b54b-b60c5e98ee4d | -7.9631 | -44.113 | 2025-10-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9a0d21ab-e262-3831-936a-0ca17325ae11 | -8.4717 | -44.1746 | 2025-10-16 00:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 784725ec-7ea2-3ae3-b3cd-3f5079d603fa | -4.1161 | -48.0136 | 2025-10-16 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 32bcf52a-156a-354d-ba8f-83b9316cec30 | -3.2298 | -43.4646 | 2025-10-16 00:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 7055f2c2-471b-396d-8b26-a56ee8279786 | -3.2738 | -45.8286 | 2025-10-16 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5b8d49dc-ca39-3715-a4a9-55d2f79ba211 | -29.187 | -50.1287 | 2025-10-16 00:30:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| f47e921a-0a10-3580-bc55-5d7b4387710e | -4.5042 | -45.3893 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 2eb4562e-de1e-353d-9114-3ab7e28765b6 | -3.2738 | -45.8286 | 2025-10-16 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a4af1126-986e-3e70-9b99-8dd65add1e9d | -4.1161 | -48.0136 | 2025-10-16 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 71740119-d3bc-3b42-9980-ab5c10dfaeb3 | -29.187 | -50.1287 | 2025-10-16 00:40:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 795191e7-7a6f-3736-be09-c9d06d4fed43 | -7.4894 | -42.7586 | 2025-10-16 00:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| ea4d13bb-796c-3274-b48c-d72467aacbc2 | -4.5041 | -45.4118 | 2025-10-16 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 81acf271-76a6-3982-b03d-d2c647f6055a | 1.84 | -55.7626 | 2025-10-16 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e7304614-2a4c-3785-b61a-d163a4f2599a | -4.8644 | -44.5748 | 2025-10-16 00:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c110da39-57b3-3144-b861-48ddc4603fbc | -7.4897 | -42.7349 | 2025-10-16 00:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 588ecff4-9838-31a0-9485-d8f5c88af6e0 | -7.747 | -34.9215 | 2025-10-16 00:40:00 | GOES-19 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| e9a9f291-d206-37f7-a770-c0bc30d4e9c3 | -4.4854 | -45.4128 | 2025-10-16 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| faa58d64-4b1e-375e-af00-090010ab6db8 | -4.5227 | -45.4108 | 2025-10-16 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| bd3cb20b-afc8-3ff5-b169-40f4ff804b3b | -9.2255 | -48.6 | 2025-10-16 00:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 95337142-d93f-39e3-8ae1-4d13a60c355c | -3.0157 | -45.3903 | 2025-10-16 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b0195244-2754-3fd5-a998-21913460bcdf | -8.4714 | -44.1978 | 2025-10-16 00:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 3d1d85d9-9c64-3954-8a83-8c51958fc014 | -8.4528 | -44.1767 | 2025-10-16 00:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 68558a8a-0ed1-3a9c-b7b2-e78e11055213 | -5.4558 | -41.0297 | 2025-10-16 00:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| dc5c3db7-f97d-3b83-aafd-8d3677ddab6e | -6.0489 | -41.9198 | 2025-10-16 00:40:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 65af282a-dffa-3574-b33e-7820c6374626 | -12.6801 | -43.4474 | 2025-10-16 00:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| dc199b4b-2aa0-3ac0-845e-81a78087d6fd | -4.5042 | -45.3893 | 2025-10-16 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 2dd31755-8412-3ce3-b9f5-c376e1c9198a | -12.6805 | -43.4235 | 2025-10-16 00:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 352.8 |
| 999c1099-30de-340e-92b8-592b5ac19c51 | -10.8856 | -48.7923 | 2025-10-16 00:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9fac24d8-9839-393a-baaa-13a396030807 | -3.2737 | -45.8509 | 2025-10-16 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b48974f0-3de2-3b2e-be15-8631c238c0c7 | -11.456 | -44.1613 | 2025-10-16 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5a96d27d-e7a4-3d62-9a1d-b6d13a2b16b2 | 1.8401 | -55.7232 | 2025-10-16 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 87a84886-a28f-322a-89f0-f1c2820ca6bb | 1.8401 | -55.7429 | 2025-10-16 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e80858e9-b6da-31f8-bf02-0726f1fcb8eb | -12.6612 | -43.4268 | 2025-10-16 00:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 7925097c-f13e-31ad-a355-443c6196afb4 | -4.3872 | -43.406 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| ce1dcfd2-a2db-3e3f-afc7-3876c9c18492 | -11.7601 | -61.0743 | 2025-10-16 00:40:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ca624ef2-f1af-3fd3-ab52-e32a0b58b147 | -7.4708 | -42.7368 | 2025-10-16 00:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 0c9eb878-4259-3760-ac5b-026d3b082eb0 | -4.116 | -48.0352 | 2025-10-16 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d254a9f8-8843-3e2b-bb0d-926dd50a04c8 | -4.0974 | -48.0361 | 2025-10-16 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 4c744dc0-71f9-35e3-8b6a-e98e0dd39bd7 | -7.4706 | -42.7605 | 2025-10-16 00:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 171.2 |
| 08089146-524f-3895-b283-4373212fedc8 | -9.2398 | -63.2489 | 2025-10-16 00:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 4023c6cf-f56c-3295-b221-746db25f2590 | -7.9442 | -44.115 | 2025-10-16 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d983b9fb-c412-3bf3-b4af-a2d6a65481f4 | -8.4717 | -44.1746 | 2025-10-16 00:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 697f587c-1ebf-3edd-b10f-3460b65cbb33 | -7.9628 | -44.1362 | 2025-10-16 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 181.2 |
| c3eae3d3-ec4a-3d7c-9f91-5bde704b29b9 | -4.35 | -43.3849 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d65858a4-1905-3987-8547-ee83777d0bba | -7.9439 | -44.1381 | 2025-10-16 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 7fd92c58-a4d2-35f2-a3c6-83a35b3b6964 | -4.3498 | -43.4082 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cf11d727-dab3-3e5f-be26-2ff56509cb8c | -4.3687 | -43.3838 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 359.4 |
| e6a1962e-bfe3-3012-90a1-0141a882d142 | -5.2068 | -43.7945 | 2025-10-16 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a9fb9beb-d3b9-37ab-aa13-8019d165db74 | -4.3874 | -43.3827 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| ea39a9ad-7be2-3d5c-96f8-464b94767ebd | 1.84 | -55.7824 | 2025-10-16 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 417f2101-d409-3995-8ea2-69f26d0e98f5 | -4.4856 | -45.3903 | 2025-10-16 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b9a7554c-7c4f-3454-982b-306157e0f0fd | -4.3685 | -43.4071 | 2025-10-16 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 288.9 |
| dd9f848d-66ff-3f15-b10a-399efcddcecd | -7.9631 | -44.113 | 2025-10-16 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a7125226-3af7-36bf-b914-974b40365e68 | -4.0976 | -48.0144 | 2025-10-16 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 185.7 |
| 6a92d926-fdef-3d52-833b-6b03734c1746 | -4.0974 | -48.0361 | 2025-10-16 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c2c7c271-03d9-3bdb-8a95-304499a88685 | -4.3498 | -43.4082 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 9b23049a-0a21-3a7a-bbe1-aec7553bfd04 | -4.3685 | -43.4071 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 2151b925-fcf9-3c36-b2ff-37e771c73907 | -4.5042 | -45.3893 | 2025-10-16 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 00ffead0-65f1-31ff-b83e-884310117938 | -4.8644 | -44.5748 | 2025-10-16 00:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| ef2fedc9-4824-3339-9492-0652f60def97 | -5.7863 | -46.005 | 2025-10-16 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| bcee1e11-8c86-3a2a-b532-e09bce478b64 | -12.6612 | -43.4268 | 2025-10-16 00:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| bfe458a4-6379-38fa-a0c3-7652a23d470d | -4.4854 | -45.4128 | 2025-10-16 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 903c0885-8a12-354e-b3f8-68aa3f18912a | -8.4528 | -44.1767 | 2025-10-16 00:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 8c4a27b5-14ea-3dc9-900b-3408df94f621 | -7.4894 | -42.7586 | 2025-10-16 00:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 3d308dd1-0e01-3817-9e69-3212ce4a27b1 | -10.133 | -44.5777 | 2025-10-16 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7d2f1775-352f-3d55-8622-e6e4e68e8946 | -5.5147 | -47.3069 | 2025-10-16 00:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2eafe87c-984b-3475-baee-75d6e4e576be | -4.5041 | -45.4118 | 2025-10-16 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 606a2bf5-0c3c-330d-bbb3-f0eb805e398d | -8.4714 | -44.1978 | 2025-10-16 00:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b17ad6b5-777b-3010-9a99-e0197d8fb05b | 1.84 | -55.7626 | 2025-10-16 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 62e1de3c-a706-34ed-9c53-6954bdef42da | -3.0157 | -45.3903 | 2025-10-16 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 96a8176c-65f2-3405-af03-961c9bc67c26 | 1.8401 | -55.7429 | 2025-10-16 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f6528660-2ff4-31a5-9353-1fe8cbb0cd04 | -8.4717 | -44.1746 | 2025-10-16 00:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 3fb167b3-b4d5-3e5f-9811-5c1af3c47528 | -4.35 | -43.3849 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ddb6c09a-be6c-3623-a7a1-7e81633c6d2c | -12.6801 | -43.4474 | 2025-10-16 00:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| eb59c753-3d00-34de-8196-048a3cc0863b | -9.2398 | -63.2489 | 2025-10-16 00:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9d8b15f7-32aa-3f9a-afc7-f20584ae98ce | -7.4706 | -42.7605 | 2025-10-16 00:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 8aec84b1-75dc-39fa-bfa6-4692290f215b | 1.8032 | -55.8815 | 2025-10-16 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8844068e-5c29-3863-b332-1d7c676ba336 | -12.6607 | -43.4507 | 2025-10-16 00:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b3bd5612-2c52-35ed-8ea4-97f0e0bc8548 | -4.3874 | -43.3827 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 218.7 |
| e18631b0-7990-37b3-8a65-752415e9dcb3 | -29.187 | -50.1287 | 2025-10-16 00:50:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| e30d512b-0c7e-3738-a42c-8183f5b5095c | -4.116 | -48.0352 | 2025-10-16 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| e2bbf887-2b3b-3e7b-b662-ffd38cb739d9 | 1.84 | -55.7824 | 2025-10-16 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 58492a50-d9be-3ff5-a811-079d7e1ace7e | -4.1161 | -48.0136 | 2025-10-16 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 5385488f-f9c6-3313-ae18-80f38f4fd5b0 | -7.9439 | -44.1381 | 2025-10-16 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 3a990a2b-be41-3731-b1d9-962f76bf1002 | -5.4764 | -42.9132 | 2025-10-16 00:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| b53d1c6b-e4b6-3df1-bb7c-8f36115aac6e | -3.0158 | -45.3679 | 2025-10-16 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 2ee0b667-bf9c-3b4e-a9f7-36c74fae6003 | 1.8401 | -55.7232 | 2025-10-16 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4bfd39ee-a17e-3037-a766-48dd321c250d | -6.0489 | -41.9198 | 2025-10-16 00:50:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| d96321c9-b8ba-389c-988a-e57c7cf3f880 | -7.9442 | -44.115 | 2025-10-16 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3cae07ac-7d04-389c-b2ce-5d7a875f452a | -7.9631 | -44.113 | 2025-10-16 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 821f9a08-554f-3fa8-aa47-e43b2a592f31 | -7.4708 | -42.7368 | 2025-10-16 00:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 7d7152cd-7fa8-319c-93f6-091a41a1c718 | -4.4856 | -45.3903 | 2025-10-16 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c3256573-41ae-3910-94b4-602c58a79e2a | -4.883 | -44.5737 | 2025-10-16 00:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| b1d80da7-9dca-3b6e-88f5-3b6adb8ba3fe | -4.3687 | -43.3838 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 368.6 |
| 80152ccd-3315-34fb-b82e-78960ce4df48 | -5.4575 | -42.9381 | 2025-10-16 00:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 2cc6e210-f356-3bcd-9684-401eed334baa | -3.2737 | -45.8509 | 2025-10-16 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 048cb7d9-e9dc-315b-ba7d-f274bfb27e15 | -4.5229 | -45.3882 | 2025-10-16 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |


[Clique aqui para ver as próximas entradas](README4.md)
