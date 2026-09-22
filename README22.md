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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dff4db2d-afac-349b-b3ba-7a3b499fa5bc | -5.7756 | -45.0826 | 2026-09-22 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 62ab9524-b1ce-3b8a-9b1b-842ae8505074 | -6.0925 | -57.6847 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ed0e2c6f-3698-3ec6-95dc-055eb96c0822 | -5.9333 | -59.9899 | 2026-09-22 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 49286f99-3f32-32ef-8f3a-6571635f95b2 | -12.1462 | -47.3751 | 2026-09-22 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 88ea86ab-16cd-3e78-80ea-b678b0e67098 | -11.4213 | -47.338 | 2026-09-22 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 277.9 |
| ad9eae48-9fd1-357d-8447-155aae7ffe23 | -18.7466 | -46.9534 | 2026-09-22 01:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 69a488c1-3607-3545-ae8f-945ad291cd11 | -9.5594 | -66.0359 | 2026-09-22 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 3785b482-987a-379b-9489-28b9b54ba383 | -8.257 | -55.3005 | 2026-09-22 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 44aac10a-e969-3fe2-85c4-2e7047b014a5 | -12.8056 | -54.0462 | 2026-09-22 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a5482d92-34eb-3c78-83f6-781e38f58aa2 | -5.9334 | -59.9707 | 2026-09-22 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f2cb81aa-d04b-37be-92f9-560ebcda734e | -7.5889 | -57.6757 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 294a9046-9fb6-3a4a-90f3-e011ea023d5f | -11.3255 | -54.0487 | 2026-09-22 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 02370036-defc-344d-9846-67e250b0c490 | -18.7472 | -46.93 | 2026-09-22 01:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 7484d2a5-e3e7-36ec-a799-74bac95ca86a | -6.0928 | -57.6262 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a71b1911-3771-30a3-9af2-c0a8e32350d2 | -5.7567 | -45.1067 | 2026-09-22 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2dcbcb9e-cc03-3b1a-ae3f-8ffbe9405bd7 | -12.1458 | -47.3974 | 2026-09-22 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 8e310fac-be19-3d0d-be59-8a48800c7d31 | -6.0549 | -57.8227 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 62f93d77-eb68-3332-b151-56aba151faca | -5.7756 | -45.0826 | 2026-09-22 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 17519222-69c0-32df-ba40-918c0b6e4798 | -11.4213 | -47.338 | 2026-09-22 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 041cc76e-9f52-3e31-8e6b-c1415a86d921 | -6.6331 | -59.9265 | 2026-09-22 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 265.3 |
| 50e84e52-46a3-3672-ba96-5c522c16a04c | -5.7567 | -45.1067 | 2026-09-22 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 271c0053-bf39-3f75-8ea8-6d70187c756f | -6.467 | -59.9902 | 2026-09-22 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9adc15c3-0ced-3d39-a0b5-c995a996df69 | -11.3255 | -54.0487 | 2026-09-22 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| daabfab2-6f0d-3b81-bde3-fe5a044f09f7 | -6.6515 | -59.9258 | 2026-09-22 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 8729539e-0cb3-3192-938d-08a673b4261e | -7.5889 | -57.6757 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 2da35f27-bc83-3504-ad3d-da825a18ffc6 | -6.6148 | -59.908 | 2026-09-22 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3c9ad315-d35c-3365-b127-88f37c9095f1 | -6.6516 | -59.9066 | 2026-09-22 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9f16a236-e87b-3952-abda-2bdf412bf254 | -18.727 | -46.9345 | 2026-09-22 01:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5712bb07-20cd-3630-8978-56e355e733e6 | -8.6169 | -54.6328 | 2026-09-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c5c0146b-3ec7-3d94-9ade-bce8fac4f438 | -3.0542 | -54.4081 | 2026-09-22 01:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ed5005bf-bce2-3e7a-ade7-5d660ed2b672 | -9.5595 | -66.0172 | 2026-09-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| db909ea3-fb0a-3b19-a3a8-393f05b859e3 | -17.6155 | -46.6607 | 2026-09-22 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2c171778-450f-3ad9-9e2b-c53d127cdace | -5.9334 | -59.9707 | 2026-09-22 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 212fc6f2-17cd-3850-9373-d7f4917cb8fd | -2.4206 | -58.2712 | 2026-09-22 01:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 6d739518-88a7-32c6-b72e-3eb2dc780ac6 | -6.571 | -44.1516 | 2026-09-22 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 83c068e7-3010-398c-99a5-da3150e090ba | -9.4773 | -40.3116 | 2026-09-22 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.5 |
| e9068622-c30d-3c02-9b27-55a8843de300 | -5.7382 | -45.0853 | 2026-09-22 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e160c449-9ce4-34ab-9a7c-ad5dec786344 | -6.0549 | -57.8227 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3d8cfe3b-eab8-3fb4-ba04-104f9c1e7304 | -7.5704 | -57.6766 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7f20c3db-7a39-396d-8abd-f692434c81f4 | -2.8608 | -57.7994 | 2026-09-22 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6d6b1353-f450-377c-b601-c5b4818d5257 | -5.7569 | -45.084 | 2026-09-22 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 308.3 |
| d0b9b031-8285-380e-bfa1-548d4d86e921 | -18.7472 | -46.93 | 2026-09-22 01:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 6e093730-8ad5-38fb-96cc-a896641518bf | -5.9333 | -59.9899 | 2026-09-22 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a8f33324-04a5-3bd3-a7d0-16b193fd3a7c | -12.1458 | -47.3974 | 2026-09-22 01:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 82c391ce-9453-3f26-a264-817cf8970bb3 | -7.7144 | -61.2419 | 2026-09-22 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 31cf76fe-a436-3f6d-a1da-c3c118f8f2c0 | -3.2212 | -53.9422 | 2026-09-22 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| db42c505-4aec-34e7-9649-4132dd800695 | -6.6332 | -59.9073 | 2026-09-22 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.4 |
| dc923f75-d260-35c6-8140-de9cf5e36273 | -6.1109 | -57.684 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f0b7970f-227e-34e5-9a54-e144366aec95 | -6.0365 | -57.8235 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6e7bd92f-0410-375d-b2a9-8fb78450a7dd | -11.3257 | -54.0282 | 2026-09-22 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2c6389ce-d01b-318e-9616-76da9b5870ac | -6.5898 | -44.15 | 2026-09-22 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8436b435-c7ce-3109-9d8f-f5d673b9117b | -6.0928 | -57.6262 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6568ac7d-5f4c-3854-a17c-8af32008056b | -7.5888 | -57.6953 | 2026-09-22 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5916a604-8090-3397-8309-32d47cc7ee2a | -9.5594 | -66.0359 | 2026-09-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a8afa9c9-00b5-33f3-89d3-64dbdaa5be33 | -12.7865 | -54.0482 | 2026-09-22 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c68c7821-51db-37d9-baa3-33b9e59879e2 | -8.7916 | -44.2778 | 2026-09-22 01:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 99500cb6-e0bc-39c4-a485-ed56c4a7e283 | -6.6146 | -59.9272 | 2026-09-22 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| a218a8ce-b39b-3b77-ba84-fa50ac1638fd | -9.2383 | -46.1668 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 2e1f293a-1915-30a9-af22-285e18a2df6b | -10.5908 | -53.9713 | 2026-09-22 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 846c853b-44ce-3083-9f7b-2376ab3f516b | -2.6669 | -54.9757 | 2026-09-22 01:40:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 80c6c135-43ff-3935-b2e4-aa7dbaf77f03 | -9.2386 | -46.1443 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 80057772-2bb4-34d2-8c61-25686a10ad2a | -2.6669 | -54.9558 | 2026-09-22 01:40:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4bda6aa6-f97d-3701-b8e7-76b5c7fd8ba1 | -5.7567 | -45.1067 | 2026-09-22 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d3572158-adde-3fdd-806a-173fefb8aa2f | -18.7472 | -46.93 | 2026-09-22 01:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e24c2e05-ef28-3c75-9ba2-fd5decad4a06 | -9.5594 | -66.0359 | 2026-09-22 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 907293c4-f96f-3062-962c-5333181eb568 | -7.5704 | -57.6766 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a6c04501-a2fb-3b5c-a5e6-0b8a38215244 | -3.2212 | -53.9422 | 2026-09-22 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| dd26d526-1da7-36c8-a96b-ff2e9b3eb096 | -9.2762 | -46.1627 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 577562dc-899d-3d56-88ea-ae2e95211157 | -9.257 | -46.1873 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 4e57d750-1f09-3be8-a034-ee2c3acca7e7 | -11.7672 | -50.8253 | 2026-09-22 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 84154c19-46fa-3dee-a2f1-b3d1ff0ed952 | -9.2573 | -46.1647 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.6 |
| fd3ab136-adf8-3839-893b-e6aeebbce200 | -5.7382 | -45.0853 | 2026-09-22 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1ed5526f-0fd6-3008-a9e1-bf791256dec1 | -10.6283 | -53.9885 | 2026-09-22 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8666d5fc-aa30-3fdf-9b13-cadee5610bfa | -6.467 | -59.9902 | 2026-09-22 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 23471163-7794-34e9-a091-cde71dd03643 | -11.4213 | -47.338 | 2026-09-22 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| aa482dec-666c-3023-8eaf-d91585acb24c | -7.7144 | -61.2419 | 2026-09-22 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 52b3fedb-92aa-30e3-abbd-09d0b049230f | -5.7571 | -45.0613 | 2026-09-22 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 92a6b376-925c-3efc-b199-cf0588b79ade | -6.0549 | -57.8227 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0d474e8d-5833-3bc8-a888-9ed0051cb3a3 | -11.3255 | -54.0487 | 2026-09-22 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 34acdb6a-3d90-316a-8225-b7f038296c1b | -10.6094 | -53.9902 | 2026-09-22 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 431.2 |
| 0f0e7129-9d12-339a-8e97-4c8d124c6eae | -9.4769 | -40.3365 | 2026-09-22 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 5773330e-e5ca-30d5-87ff-97a0f9c9f7b8 | -11.7675 | -50.804 | 2026-09-22 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4eee954e-1849-389b-9ab9-2a53224493d6 | -6.1109 | -57.684 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6475b314-417c-35a7-902e-ce1a4697d3ab | -9.4773 | -40.3116 | 2026-09-22 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 183.7 |
| 75766f78-2f04-303b-9400-0e97997b02a5 | -5.7569 | -45.084 | 2026-09-22 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 267.3 |
| de4ef4f3-11f0-3df6-bc3b-5e51cb46b392 | -11.7484 | -50.8061 | 2026-09-22 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| eb1960f1-4142-33fb-b6d6-6f0ff7acee40 | -7.5889 | -57.6757 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 3e149e87-830e-3a23-9885-b544d18ce64c | -11.3257 | -54.0282 | 2026-09-22 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f427b466-22d7-3c88-9dfe-210ceff8505d | -10.6097 | -53.9697 | 2026-09-22 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.9 |
| 89c3071d-1232-36c1-98ce-cd1c9748213a | -6.0365 | -57.8235 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b5ae39b4-bafd-38d0-88a7-dcd223b8cd50 | -10.5906 | -53.9918 | 2026-09-22 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| df3a54cd-51d8-3d33-8e1e-bad96a67f4b0 | -6.0925 | -57.6847 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e02ec34a-70b9-3bb6-b58e-831007350007 | -9.2576 | -46.1422 | 2026-09-22 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 40e2a4f5-72b1-3085-82f9-fc8bf6f06d43 | -3.2211 | -53.9623 | 2026-09-22 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c0979da9-4ed0-32ef-be8a-9c5a91990c03 | -3.2396 | -53.9417 | 2026-09-22 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1a8621c3-6b38-3569-8b51-ffc139b60e08 | -2.8608 | -57.7994 | 2026-09-22 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e7ed594e-f9cb-30a7-b16e-185c051756a4 | -6.0928 | -57.6262 | 2026-09-22 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e51b1484-8614-3725-bdc6-4408b7a7ff2c | -3.2395 | -53.9618 | 2026-09-22 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| 1b50c053-4c77-34ab-98ae-c9880cc6d9cc | -7.5889 | -57.6757 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| a0d377f8-3556-3354-ad2f-e709102d54d9 | -9.2386 | -46.1443 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |


[Clique aqui para ver as próximas entradas](README23.md)
