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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efcda450-9674-3bb6-b488-e5ca64e5297b | -2.6496 | -54.6172 | 2024-10-02 00:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 63989a99-26a4-3934-906f-024544004142 | -2.6679 | -54.6168 | 2024-10-02 00:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0d7855db-3962-3f11-a120-19c90577ad17 | -2.8879 | -61.8822 | 2024-10-02 00:05:22 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 942e9b50-b97a-3624-b93c-0da056359c21 | -3.2136 | -46.7843 | 2024-10-02 00:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d53f6e62-9b78-332c-ba68-d17cd5e3fd37 | -4.447 | -42.8889 | 2024-10-02 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 6005e4cd-feda-3be9-a2d6-ee281d4824a4 | -4.4655 | -42.9112 | 2024-10-02 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f873c02b-fbc3-36bf-94e4-1975b55ec6d7 | -4.4657 | -42.8877 | 2024-10-02 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 305.8 |
| 62595d77-d868-359c-8211-01f27c32c81f | -4.4658 | -42.8643 | 2024-10-02 00:05:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ec6430d9-c8a9-35c7-88b4-00afba1ddab1 | -4.4679 | -48.127 | 2024-10-02 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7323a981-ee52-3b03-98e5-5738d58f221e | -4.4681 | -48.1054 | 2024-10-02 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 9a43fdc5-5f8c-3d7a-b4f3-25f476ee168c | -4.4865 | -48.1261 | 2024-10-02 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9348fa42-ca55-32de-abbf-344407d8816f | -4.4866 | -48.1045 | 2024-10-02 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| fe84d3df-1c20-33d2-919b-4a527729204e | -4.58 | -48.0132 | 2024-10-02 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ef16d04f-0ae7-32b7-9700-ba76db8557eb | -5.9786 | -45.3847 | 2024-10-02 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cc454551-c8f8-30cb-b2ed-154ab078a18d | -5.9788 | -45.3621 | 2024-10-02 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b6ab4186-105e-3236-ae5a-ae7d8d7c6591 | -6.1186 | -46.4498 | 2024-10-02 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 1d276a6e-bce2-3558-a000-d2b886fe217c | -6.1371 | -46.4706 | 2024-10-02 00:05:41 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 82c0eb7c-cc89-3d11-a452-852bf896d0cf | -6.1373 | -46.4484 | 2024-10-02 00:05:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d34bb59f-3a25-310c-9503-4d1323a13521 | -6.25 | -46.3735 | 2024-10-02 00:05:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| d857965a-0505-3bf8-9070-6538c59f7359 | -6.9647 | -42.503 | 2024-10-02 00:05:45 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 6b201d14-18fd-318a-abd6-d78fbdbe6d68 | -7.1794 | -46.9665 | 2024-10-02 00:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 07811373-7818-3049-aadd-3696771b3758 | -7.1796 | -46.9444 | 2024-10-02 00:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 500fce88-2e83-358d-ac80-6a4c05d8a872 | -7.7129 | -42.995 | 2024-10-02 00:05:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 34f55ac9-4aea-359d-9160-8b2efe2bbca5 | -8.205 | -44.365 | 2024-10-02 00:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ca66b1f1-d659-3af8-9d52-67edd11c01a9 | -8.2053 | -44.3419 | 2024-10-02 00:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8e159fa4-f6b2-3144-b316-329146df7d5e | -8.2239 | -44.363 | 2024-10-02 00:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a9793699-f857-3cbc-a6f6-32dca2f7e81c | -8.2242 | -44.3399 | 2024-10-02 00:05:52 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| be04e72e-59ef-3d3d-8ec8-8fd9285d25ec | -8.4642 | -62.7313 | 2024-10-02 00:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1cce501b-7fff-305b-bc9e-a3e463b34fb4 | -8.4643 | -62.7124 | 2024-10-02 00:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e3118f98-a545-38fc-aeed-353af5c7bdf2 | -8.6844 | -45.2309 | 2024-10-02 00:05:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 60667b0e-37c1-37fc-afd7-46881c446d29 | -9.5397 | -62.8195 | 2024-10-02 00:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| e2b5baa8-38ea-38b3-801e-e3c9ba1fed1b | -9.5398 | -62.8005 | 2024-10-02 00:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 128.1 |
| ce35c2bd-b22b-3ae0-b9ed-bed34b6ffdf2 | -9.5583 | -62.8187 | 2024-10-02 00:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9a4f0375-60a4-3305-a7a4-0b2457450b4d | -9.5584 | -62.7997 | 2024-10-02 00:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| d473bc04-f0f4-32c7-9bdb-30dae32801c4 | -9.9366 | -64.9367 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0f82d1b0-47fc-3a61-bb21-a144e1b2947e | -9.9367 | -64.9179 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 326.5 |
| 4776b72a-7799-3359-a603-26e9d9cbbea8 | -9.9368 | -64.8991 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 258.3 |
| 97951f8a-a7ce-365b-902a-661ec56677c5 | -9.9553 | -64.9172 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 303.0 |
| 6e4024b2-6246-339d-934a-c0ba173df8b0 | -9.9554 | -64.8984 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 259.7 |
| 194a5285-beca-3842-89e6-43209e96e699 | -9.9933 | -64.7654 | 2024-10-02 00:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ee2a9d82-256f-3977-918e-bc5e72d6ba35 | -10.626 | -55.8752 | 2024-10-02 00:06:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 8766512a-be58-36b5-837b-bf89149f2b46 | -10.9044 | -50.1304 | 2024-10-02 00:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c5e7a5a8-3860-39da-9320-bd037ba431db | -11.2565 | -60.6019 | 2024-10-02 00:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1ea4d3ee-883b-32a7-8837-3e13f60e998e | -11.4822 | -56.7892 | 2024-10-02 00:06:11 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 35e3172e-2bcc-34e8-8b51-a6f1b494e57a | -11.884 | -43.8142 | 2024-10-02 00:06:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6bf5f7de-0b94-39be-aa46-d02a753104ec | -11.6555 | -64.9991 | 2024-10-02 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e84b44b4-7a6c-3a6a-a5cf-125c46257998 | -11.6556 | -64.9802 | 2024-10-02 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4f2c376b-534f-3a7a-a4fe-92570dbbfcc8 | -11.6743 | -64.9983 | 2024-10-02 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ee209f1b-ae5b-3604-9bdf-986d6d4f402f | -11.6744 | -64.9793 | 2024-10-02 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b24c1a38-ae36-3fc4-a3e0-a3917b2fb810 | -12.1597 | -50.0501 | 2024-10-02 00:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6b7187c4-9314-3fe9-a1e3-f82eb5cf3b9f | -12.4433 | -43.7242 | 2024-10-02 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 930ae88a-8ad3-39c1-8e42-e973c97e97bb | -12.2754 | -47.6473 | 2024-10-02 00:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3c6a5c91-66f1-36ad-afb7-24f414b3f20d | -12.2946 | -47.6446 | 2024-10-02 00:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 31cf0eb8-3b92-3efe-941e-33e54f497cbe | -12.6484 | -63.1214 | 2024-10-02 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 146.1 |
| dca26dd4-f1f1-33dc-b50e-a9c34c54a2b3 | -12.6486 | -63.1022 | 2024-10-02 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 29601a1c-2538-397f-abdc-a40173a8eab7 | -12.7054 | -63.0798 | 2024-10-02 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3dbe82c2-e5b2-3c91-98b5-b1327baedbb9 | -12.8593 | -62.7826 | 2024-10-02 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2925f440-7522-36fa-990d-7e7684f14a70 | -12.8782 | -62.7815 | 2024-10-02 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| efbaad3f-bb49-36e9-a529-32d6f8fae982 | -13.2173 | -48.624 | 2024-10-02 00:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a46842d4-7308-37f3-8393-8460804342df | -13.2177 | -48.6019 | 2024-10-02 00:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 156c78b1-0cc7-3f06-a0e2-c64fb24f52a7 | -13.0933 | -51.4139 | 2024-10-02 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9d28cb69-fe3d-3187-96c0-f5d8db7ebf31 | -14.7787 | -48.7882 | 2024-10-02 00:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 13cffa03-61df-373a-9565-4194e97eec88 | -14.7986 | -48.7628 | 2024-10-02 00:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 578d0d96-8aad-3872-9d56-576b17ee36ff | -14.8181 | -48.7598 | 2024-10-02 00:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ccc25f5a-27c7-3a82-9944-22e3e6137194 | -15.139 | -55.8285 | 2024-10-02 00:06:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6eed4147-50d8-38c5-ba43-01ff76397379 | -15.1393 | -55.8079 | 2024-10-02 00:06:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c930eb6a-56d1-3296-b8ab-238923cdf264 | -15.3708 | -55.8431 | 2024-10-02 00:06:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 77a7ae83-7d13-3be9-aa6d-cd16dc89acf8 | -15.3902 | -55.8409 | 2024-10-02 00:06:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bef05917-48d1-339f-80e5-52e2f0e20919 | -16.6124 | -57.2375 | 2024-10-02 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.5 |
| 36d61bff-7572-3fc9-896b-74c89241922f | -16.6127 | -57.217 | 2024-10-02 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| e0b24504-57bf-3e75-961e-ff8643c832e3 | -16.6303 | -57.3376 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| a2413ba3-8f3e-3eb1-ae7e-43f15ed7e9cf | -16.6306 | -57.3171 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| a3a0be54-0339-3c44-90fc-584b9c14b6e1 | -16.6319 | -57.2352 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 59f4983b-c2b5-31eb-b1c8-ed4e1c1e7862 | -16.6322 | -57.2147 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| a7440cfe-dbdc-3dbf-a3d4-7e4e80d8b673 | -16.6713 | -57.2102 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 60156e96-d903-34b3-8d1f-7827302d1637 | -16.6717 | -57.1897 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 8b7e579f-d791-364d-b149-083700b0a357 | -16.6884 | -57.3718 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| a17ced13-da4e-3c85-a6a6-7ae48182acee | -16.6887 | -57.3513 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| b6853464-b1c1-3df6-b5f9-5a41f9d3dcdd | -16.6909 | -57.208 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 6404fda1-f544-3a49-93dc-deb3d67910d9 | -16.6912 | -57.1875 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.6 |
| bfdc1de5-377b-3696-8c9e-eaf39468a2b1 | -16.7063 | -57.4718 | 2024-10-02 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.4 |
| f781c1ea-5fa6-3d6f-a56a-88cb2f5121de | -16.7079 | -57.3696 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.9 |
| e82e4622-caeb-3457-b007-cb16b4532d08 | -16.7082 | -57.3491 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| f4519fc3-c1fe-3591-a2ed-a679eb44d471 | -16.7265 | -57.4287 | 2024-10-02 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| e597df26-15fd-3c3f-ac4b-10ff7cac5221 | -16.7452 | -57.4878 | 2024-10-02 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 4f47ebf9-d18e-329f-ae52-1ea88b0c5b24 | -16.7461 | -57.4265 | 2024-10-02 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 431c5a72-b804-34cc-8221-974f4b75bce1 | -16.7663 | -57.3833 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 26d65a2b-f162-341e-87d4-38dd8c98b2ff | -16.7666 | -57.3628 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 682d67fb-0afe-3ff1-81b1-13c2d60f2946 | -16.7859 | -57.3811 | 2024-10-02 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 82cc33e1-783c-3068-bd65-2b795e07cc04 | -16.7862 | -57.3606 | 2024-10-02 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| e2e2d0d3-337f-3fa8-aeb7-5a61457978b3 | -16.8292 | -55.9152 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 136.9 |
| 9a992c5a-8195-3704-a5ea-f27cbbbd355b | -16.8295 | -55.8945 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 177.2 |
| 79cbf4b4-d610-3434-a27d-ded2753c3b2a | -16.8299 | -55.8737 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 332e3d0f-05c0-316a-82d3-d33a1ed75431 | -16.8234 | -57.4789 | 2024-10-02 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| bf78b771-6f46-3db4-a626-5b650921caf5 | -16.8238 | -57.4584 | 2024-10-02 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 0008d007-b8a6-343f-8f26-d8360a0d6598 | -16.8488 | -55.9128 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| f7d1fd47-52ee-34cb-b150-fd4ed9c08fcf | -16.8491 | -55.892 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 154.1 |
| 69bedffe-de22-3ca2-a018-6fdc0ed49859 | -16.8386 | -57.7628 | 2024-10-02 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| cde7e64a-cd56-31f7-a12c-d7571e84368a | -16.8684 | -55.9103 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 7b34f9d6-d40a-3b2a-ba47-8391c42dc27c | -16.8695 | -55.848 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |


[Clique aqui para ver as próximas entradas](README2.md)
