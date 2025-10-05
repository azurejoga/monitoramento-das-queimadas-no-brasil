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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63e4a730-d535-37b6-895a-0e197392aa65 | -8.5407 | -47.6831 | 2025-10-05 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| cd53c165-cdf3-3a8d-9778-e0381642d88f | -7.7935 | -42.5845 | 2025-10-05 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| ca78f5ff-56a8-30a6-9ac6-8d61a4bb745d | -7.7885 | -44.5228 | 2025-10-05 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0e35d2a1-4c00-30b4-b9e7-eb7443696f6f | -12.895 | -47.3134 | 2025-10-05 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ddfcb899-a386-348f-a5e1-c9c2db75f5d5 | -16.077 | -51.0859 | 2025-10-05 13:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ba754161-ebb2-3093-9769-0bf6a49e6c41 | -9.6287 | -46.6394 | 2025-10-05 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a7372bc1-3487-3bfa-8742-bb648de4e7d4 | -12.3993 | -45.0183 | 2025-10-05 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1e539270-5026-3d6c-ad9e-32171978f423 | -19.0155 | -50.6045 | 2025-10-05 13:00:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 287.0 |
| d8c3d112-9cdb-3f92-9f30-7463e2e41f68 | -12.5866 | -54.7474 | 2025-10-05 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 75dcbb2a-7030-3efc-8ae5-daefe6c7afdf | -15.582 | -52.5129 | 2025-10-05 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 200.6 |
| e336708c-2e70-3e6d-a52e-2c760a6fad4e | -7.7932 | -42.6082 | 2025-10-05 13:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 247.2 |
| c7786def-fc6c-3fc5-9704-4a60c1b564dc | -17.986 | -51.144 | 2025-10-05 13:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0ab19c00-69a1-3f92-ad41-12787b40858a | -11.0316 | -46.6946 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e16f7997-dcab-3b50-aa1c-371bf214a062 | -15.5824 | -52.4916 | 2025-10-05 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| e1ec21be-a021-369d-9428-f083738f63fc | -11.0151 | -46.5393 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 320.8 |
| a3476059-5e2e-3dcb-b19b-e2ec2f18109c | -12.2688 | -49.1907 | 2025-10-05 13:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 7d79fedf-8cec-34c0-8a2f-6800b988d0c9 | -17.9661 | -51.1474 | 2025-10-05 13:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ecfc0566-25ac-3ea5-ba85-dddc7eed127f | -22.27785 | -52.1933 | 2025-10-05 13:01:00 | TERRA_M-T | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| d64d4013-c2d8-3c55-94e4-90dcade22964 | -22.2728 | -52.24635 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 460.7 |
| 15d934ef-a442-32dc-a214-2171f793ef42 | -22.26237 | -52.25113 | 2025-10-05 13:01:00 | TERRA_M-T | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.2 |
| ebdbaa91-6b62-3c3b-89c6-9792a7dd2ece | -22.26467 | -52.22486 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 216.0 |
| 53349af4-7872-31d0-9877-79bdcfe80029 | -22.26099 | -52.21911 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 6f8de90d-4415-3cc3-a4dc-73735f73167a | -22.27665 | -52.25206 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 206.9 |
| 67e8e9d0-1c5b-3978-9ded-177820fa3c1a | -22.25854 | -52.24517 | 2025-10-05 13:01:00 | TERRA_M-T | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| e6fc1a11-4aba-3d54-bf3b-75d89e9c1e47 | -22.27898 | -52.22575 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 619.0 |
| 6a86aae9-36ac-34ed-b3c5-825171267c0d | -22.27531 | -52.22003 | 2025-10-05 13:01:00 | TERRA_M-T | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 572.9 |
| bba3f980-26c6-363e-966b-ea103a297f15 | -8.1891 | -44.1357 | 2025-10-05 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6311d4d5-926b-3b3a-8641-3a83eaece6f8 | -11.863 | -44.9612 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 51617141-ad1c-35fd-9515-3d038efb4851 | -12.5863 | -54.7679 | 2025-10-05 13:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f159ca0c-66e8-3441-8f55-91a00057ea9f | -7.5267 | -41.2699 | 2025-10-05 13:10:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| c023cde2-e5a1-3172-b8cd-2f91797b2b6f | -13.7476 | -51.2883 | 2025-10-05 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| a958a2ac-6a1c-385b-b323-6da99cdd3572 | -7.8127 | -42.5587 | 2025-10-05 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| dfc82f6c-4229-3614-8c11-c19f77508e3e | -16.077 | -51.0859 | 2025-10-05 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 5180bb37-86ae-34f5-8e72-55d0d85ad8b9 | -7.4276 | -46.5239 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| abe9301c-d986-387f-a6fe-3ddd949641de | -15.6015 | -52.5102 | 2025-10-05 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 6e7284b4-e022-3402-9428-518f92814e22 | -7.7885 | -44.5228 | 2025-10-05 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e5594423-7f35-3332-a5bf-baa15cb0b9a9 | -15.9829 | -50.905 | 2025-10-05 13:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 125.4 |
| dffe9225-7cb5-3499-9d61-9648cdb96483 | -8.1888 | -44.1588 | 2025-10-05 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 91cdbdf5-8bb0-3134-b12b-8de33e03c2c4 | -9.6287 | -46.6394 | 2025-10-05 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| bb90b447-33ee-3e64-8698-ac642bf5d3ca | -11.0316 | -46.6946 | 2025-10-05 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 257.4 |
| b874fdf4-eef8-3889-a864-5017e749132f | -13.728 | -51.3122 | 2025-10-05 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 288.1 |
| 90c99240-8bc6-3b93-8227-9b0c9bf91809 | -7.7306 | -46.2737 | 2025-10-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 22e109ac-ed22-33a9-8d4d-39e5e7a0e3ef | -15.582 | -52.5129 | 2025-10-05 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 312.5 |
| 7e2cac8d-a2b0-3497-bf3b-8ad2f262e75a | -10.8093 | -48.8229 | 2025-10-05 13:10:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0b060a70-710d-3c4c-bdc9-3aabe1f3ceb9 | -17.9408 | -57.5928 | 2025-10-05 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 80cd1d99-e769-3404-8760-b15e4e02dae2 | -17.986 | -51.144 | 2025-10-05 13:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b53a511a-dc56-3f47-bda9-1f0bea9af3dd | -7.4672 | -43.0438 | 2025-10-05 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| da499c10-72f1-39a8-ac80-602ee83b7148 | -7.7118 | -46.2754 | 2025-10-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 653d0432-9f6b-3e62-8c08-4d329c1ed18d | -15.9825 | -50.9268 | 2025-10-05 13:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 244a165a-760b-366e-80f9-10f79dcabdf5 | -7.7932 | -42.6082 | 2025-10-05 13:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 738079eb-40fc-3551-8df0-c9d6f4d39423 | -16.0408 | -50.9395 | 2025-10-05 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3e69dc87-3d3b-3ecb-8d3b-ef29cfdc61e1 | -11.8823 | -44.9583 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ede8d7e4-3ee4-390d-b61a-4f7669e2fc58 | -8.5407 | -47.6831 | 2025-10-05 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 334.1 |
| 16e54a49-fcc6-3d93-8414-d492510a6f79 | -9.2973 | -46.0026 | 2025-10-05 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3d301670-8ed0-3ff3-91d5-f5f5688f8ae5 | -10.0504 | -50.4113 | 2025-10-05 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bda027ee-dd21-335d-85bf-45e33b559776 | -7.7938 | -42.5607 | 2025-10-05 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 5b7a21e2-775f-3fe4-9fbc-7bb6b7d3d7af | -19.0155 | -50.6045 | 2025-10-05 13:10:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 475.3 |
| 92f1a3d9-c710-3900-9523-d9538ab78a20 | -12.8954 | -47.2909 | 2025-10-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 0de22797-d41f-3062-9944-c8c0446bd733 | -9.9207 | -50.2323 | 2025-10-05 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 02988e2b-9768-362e-b785-7fbbbe08dd48 | -7.7935 | -42.5845 | 2025-10-05 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 39dba2df-41f0-38f6-8510-5e1562ac68df | -12.2876 | -49.2101 | 2025-10-05 13:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| da516a11-3729-382b-8f05-568e835b6bd8 | -7.4279 | -46.5016 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f40c2767-b32c-32c8-86cb-e101d37f6b43 | -7.7743 | -42.6103 | 2025-10-05 13:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 253.5 |
| f7bac95e-3dcd-354a-b778-ec83ed695460 | -8.541 | -47.6611 | 2025-10-05 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5618f421-c40f-35c7-82c5-107f3aba374f | -12.8765 | -47.2712 | 2025-10-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1ca60391-9f2f-3735-936e-a7fbd7c248f7 | -12.6913 | -45.8482 | 2025-10-05 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 5feac373-75ff-32a1-a4c8-7d1608b75e59 | -7.7746 | -42.5865 | 2025-10-05 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 6c7d0666-7776-37a3-a17e-f631aee9e2fd | -13.7473 | -51.3097 | 2025-10-05 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 324.5 |
| 6a2d0bc9-6f3d-33db-9452-db0d3f3a529f | -11.0126 | -46.6971 | 2025-10-05 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5cc2e1be-b664-35a8-84af-58222d9819aa | -11.8033 | -45.0856 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2fd7a86b-7dd0-38e2-bcf7-227cba54d7a7 | -16.0805 | -50.9116 | 2025-10-05 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 21e42888-258f-3335-aeb5-1a976ed3ed2d | -11.8418 | -45.0799 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 324e0a79-f507-31be-9cff-527c93864c46 | -18.1968 | -53.3638 | 2025-10-05 13:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a634ef4a-923b-3ade-8695-8357cc495537 | -12.1274 | -50.9118 | 2025-10-05 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4bac6585-8d51-3257-bb5d-74d158c0e74e | -12.4673 | -45.4925 | 2025-10-05 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 53d98783-f355-3131-87d4-a867074bd41a | -7.7308 | -46.2513 | 2025-10-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0834161b-c857-366e-83d9-c685f6b28723 | -12.895 | -47.3134 | 2025-10-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 1f6ef431-ee6f-383c-bb59-184b7bb7decc | -11.526 | -46.7645 | 2025-10-05 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 114f7bd1-a342-388f-9394-b94b1e72bebe | -7.7123 | -46.2307 | 2025-10-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 692561e8-d014-34e5-9c01-7c1d53ccab4a | -7.712 | -46.2531 | 2025-10-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 069f1eba-2487-32f5-aaec-d3ce33a975d5 | -15.5824 | -52.4916 | 2025-10-05 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ec76a2d5-3bb9-3208-8c51-a22c19932004 | -17.9661 | -51.1474 | 2025-10-05 13:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0d78be4f-fb53-3ccc-8bf5-787ac40a46dd | -11.8422 | -45.0567 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 2349bd17-84dc-3ca9-a6b0-c05009d8c39c | -16.0021 | -50.9238 | 2025-10-05 13:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 48ec73df-4a6e-34f4-8fcd-2e05760ff0f2 | -7.6993 | -42.5708 | 2025-10-05 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 4edab3c4-c873-3b1e-ab64-33dc0f4cd4b8 | -17.9612 | -57.5492 | 2025-10-05 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| af6edc68-43cd-36e8-bf54-6b1fb3b8af56 | -11.1168 | -49.8492 | 2025-10-05 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 983b265f-d358-3e8c-a9cf-e5676b4c4798 | -7.2577 | -44.8938 | 2025-10-05 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d459b826-031d-3e4c-8059-6e4d1e37429e | -9.5794 | -46.106 | 2025-10-05 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 680c233b-6e71-3931-9d8e-2e146c45c0de | -12.7106 | -45.8452 | 2025-10-05 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| c1f7c8e1-f15a-3a75-a5b0-28e116432dbb | -14.5755 | -52.4576 | 2025-10-05 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d2ec8f5a-a554-3ef6-bc8e-64def882a55d | -13.7284 | -51.2908 | 2025-10-05 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| e4738ff0-1247-363e-8981-97e283e0e0cc | -12.8761 | -47.2937 | 2025-10-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 164b6265-1d6d-3183-b808-24b012b25993 | -11.823 | -45.0596 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| aa4099e1-de61-3251-9315-1a2460668553 | -8.5596 | -47.6813 | 2025-10-05 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 0488c983-452e-3679-8622-a68c30fb7767 | -12.4669 | -45.5155 | 2025-10-05 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ee625d07-8e3d-3e18-b050-852e217bbb0f | -16.0966 | -51.0829 | 2025-10-05 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 360f35a9-b727-3852-968c-0dcd66422db8 | -10.93 | -47.1106 | 2025-10-05 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3dfa080e-6c67-3978-9c80-502e981d195f | -11.0978 | -49.8513 | 2025-10-05 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6764af39-5f43-342d-859d-f0b8ba233cc7 | -7.5078 | -41.2719 | 2025-10-05 13:10:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |


[Clique aqui para ver as próximas entradas](README157.md)
