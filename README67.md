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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b92a66e-f674-370d-9b6e-ce65e6ec096f | -11.26939 | -54.02 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37b218a3-6d37-3c19-ac6a-19c6f208c3c2 | -6.58693 | -68.8806 | 2026-08-29 05:38:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfb5fa43-d062-3d3b-a799-794aca3e92f9 | -11.62224 | -54.58733 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0643847b-1adf-33b3-a587-5cbfdcb3d344 | -9.01927 | -57.54287 | 2026-08-29 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dddf9bbd-9901-3d37-99b7-189066eb4a12 | -9.06559 | -65.41866 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52bea46f-9554-3dcb-8eb2-bfc27fbb41a0 | -9.00225 | -65.45578 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b0615f9-33aa-355f-8c3e-fc2c7c26f7e4 | -7.58393 | -61.33436 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97d85885-8a41-3ba2-8df2-3ca26718393a | -8.59984 | -54.776 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9abbd2fe-971a-3b8f-b2df-70f733a9450c | -7.00633 | -71.66129 | 2026-08-29 05:38:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f78dc1b7-d937-35b7-9d61-4a5dd20a32f4 | -9.51275 | -65.58208 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af40e7b5-61de-3cd0-b8b5-52c6772d2fdf | -6.7699 | -55.6644 | 2026-08-29 05:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| beabe08c-135c-3806-be22-63a96dbf0d80 | -6.6315 | -43.7533 | 2026-08-29 05:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e43c450c-6661-3c75-84df-b83100f1e7bc | -6.7884 | -55.6635 | 2026-08-29 05:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| b5f045a9-72b9-3da3-a9ab-d6143afcb795 | -10.4794 | -64.5012 | 2026-08-29 05:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 58d82fd4-cafb-3cd3-b910-f4b94658bec4 | -6.6317 | -43.73 | 2026-08-29 05:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f10f0b13-0c1a-33be-b52b-5d8a076b9591 | -7.5137 | -55.3051 | 2026-08-29 05:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b4aa38b7-91eb-305c-a033-5a8826b49c18 | -5.8894 | -57.7708 | 2026-08-29 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| de82d3d1-2bff-3de1-bbcf-152fce1a5a5a | -5.8895 | -57.7513 | 2026-08-29 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 02dd022f-2e0e-3d2d-bba9-da62a9d9a8d9 | -20.94655 | -57.57958 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 344ee7fc-12fe-38d0-8810-8292160696cf | -20.95082 | -57.57098 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 557809ef-e589-30df-ab9e-1584344ee657 | -20.9625 | -57.61899 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df23644d-0944-3d81-820f-54dc933d926e | -19.2247 | -57.66775 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8498aba8-8e76-36d3-8c5f-702033403781 | -19.2251 | -57.66391 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 344520b4-840b-32a7-9290-df25d600fa32 | -20.93585 | -57.57832 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9f0b27a3-a8b6-3365-aa44-a527779762d4 | -20.93621 | -57.57476 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cc70aa63-24aa-3298-a971-632068ed0db5 | -19.22592 | -57.65628 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d2d584c1-cdd9-3c08-b9fc-3f00dd52a8a9 | -19.22551 | -57.66008 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b0bb4146-0f00-3f25-a652-10220cf339d8 | -20.95689 | -57.5844 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b2172937-b37b-3a31-9ab0-b810041096b3 | -20.94263 | -57.56477 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8b878af0-6384-33cd-a91b-f99859672d01 | -20.93692 | -57.56767 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9967da82-e40f-38d7-aae8-571c0a949c59 | -19.22429 | -57.6716 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 943a6df2-a33a-3321-8ceb-44c64d346096 | -20.93763 | -57.56057 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 6c3203c7-2072-3728-98df-0b9f795a7a13 | -19.23155 | -57.65299 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 21d37c5f-6e5a-3be6-abc3-5fc746fbff81 | -19.23004 | -57.66705 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f0c32c12-7ce7-3c6f-9147-9c9f44b1bb0e | -20.93157 | -57.56703 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 1d8c2ddc-4240-39a8-be9d-d9d8ee5d8993 | -20.9412 | -57.57895 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 4baf6a0c-bdf1-3bb4-8038-80ea7c30cf13 | -20.95517 | -57.58227 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| eb1e8c1e-f5d9-33b7-810d-9e9e9230f8d0 | -20.93192 | -57.56348 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| fe43ab39-fb04-3a10-80f9-8cf0f6e6f027 | -20.95298 | -57.56958 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee38baa2-441c-3e1f-a7b3-bc2f3d9ba684 | -19.23043 | -57.66346 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8259705c-b7a1-3bf8-a9a2-b21135c63596 | -20.94982 | -57.58163 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 45969285-7fb7-37de-9a3c-bd85d967b1fe | -20.95154 | -57.58376 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c8933ade-ff88-3107-ba16-4d30f6a50394 | -20.95618 | -57.57161 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a2dc8b61-7b4e-33a5-971b-fb276bc06ce3 | -20.95262 | -57.57312 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ad97aed2-349e-3058-ac59-d8dfbe18d90c | -20.93728 | -57.56412 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| e950e015-ccae-367f-af31-40e50dc9bd61 | -20.95833 | -57.5702 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bbd17e81-acfc-3a66-a149-770214873595 | -19.22965 | -57.67069 | 2026-08-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3be879fe-55ee-3e3e-b583-3b843b512fb6 | -20.94299 | -57.56121 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5dd76eb8-6cce-39b2-9405-708c115848ad | -20.95863 | -57.62037 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 858a20e8-5293-31b1-ad18-f0a928e69020 | -20.9519 | -57.58021 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 50a35601-cb68-31ad-946c-e687009113e1 | -20.95484 | -57.58582 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b6c4c108-16bb-356c-8262-8b3f3afadc66 | -20.95899 | -57.61684 | 2026-08-29 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 59af04b6-163d-3ccc-b9e6-089b54746d3d | -6.7885 | -55.6436 | 2026-08-29 05:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 71faf3bc-6130-33a3-be82-b74ec18ad475 | -8.9428 | -63.2797 | 2026-08-29 05:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 58b941b6-be11-3a6c-af3f-a072e32b2865 | -6.6505 | -43.7284 | 2026-08-29 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e0dcac4e-47d6-32b1-a19b-2a113c4dcd30 | -6.6129 | -43.7317 | 2026-08-29 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 98e4ff97-8c3d-38a9-baf5-cca8bb86fcea | -6.7699 | -55.6644 | 2026-08-29 05:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 8041aa3b-9c3a-3baf-a572-6872720af7e5 | -6.6317 | -43.73 | 2026-08-29 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| aff3df87-6b99-32e4-a52d-bae7da2b6e78 | -6.6127 | -43.7549 | 2026-08-29 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a3626afd-7903-36ae-af17-f5f2bcd2ae4d | -5.8895 | -57.7513 | 2026-08-29 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 01bdd928-eb83-3e8e-9e0b-f1d7381f78d7 | -5.8894 | -57.7708 | 2026-08-29 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d3403413-b889-3ff2-a71a-6985b645b11a | -10.4794 | -64.5012 | 2026-08-29 05:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 29323474-8d6a-33b1-8e67-a1aa4b5e6efd | -6.6315 | -43.7533 | 2026-08-29 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| fdd730a4-4591-392c-b1d1-6d24b8b33d95 | -6.7884 | -55.6635 | 2026-08-29 05:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| d64b2596-e198-3dff-876c-a0904035e5f4 | -6.7883 | -55.6834 | 2026-08-29 05:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 31e05027-b7ef-314a-9262-41651cf4fb23 | -5.8895 | -57.7513 | 2026-08-29 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 65a8aed0-d81a-399d-b2aa-30f84ad34e20 | -6.7883 | -55.6834 | 2026-08-29 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 51c0b5f3-85d3-3023-9cfb-2035de4633dd | -10.4794 | -64.5012 | 2026-08-29 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1fd275a6-88c0-33eb-af65-6454e59d4c01 | -6.7699 | -55.6644 | 2026-08-29 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 13bc33ca-27e2-384e-9934-e4b92d1afde9 | -5.8894 | -57.7708 | 2026-08-29 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e6ad5c87-0532-3adf-8160-359e75938ccf | -6.7884 | -55.6635 | 2026-08-29 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| 07b34f28-9bc9-3997-a75f-179507f7cba5 | -20.941 | -57.5694 | 2026-08-29 06:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| d599301f-7336-3e75-b81e-b8bf94bb6539 | -5.8894 | -57.7708 | 2026-08-29 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1cc93727-2e25-3809-b3b7-dc91d0f31875 | -6.6317 | -43.73 | 2026-08-29 06:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d1d3f542-0d18-3aab-86f1-e5faa8275f9b | -6.6315 | -43.7533 | 2026-08-29 06:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| eed678cb-c32b-3bc3-851f-96d30ca1e20b | -5.8895 | -57.7513 | 2026-08-29 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a26707f2-a188-33f5-b65a-6562f381437c | -10.4794 | -64.5012 | 2026-08-29 06:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 6479d1c7-01f4-3523-8843-8da1058ace1a | -6.7884 | -55.6635 | 2026-08-29 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| fc80c270-c112-3d44-a437-62c3d335120e | -6.7699 | -55.6644 | 2026-08-29 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f2909f80-4464-3249-8ceb-309630f291f5 | -20.941 | -57.5694 | 2026-08-29 06:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 527a07f4-ce8b-3a0c-a07f-b1d764dc0a85 | 0.14923 | -60.39692 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54c1f937-c70d-3101-9093-5db7f02edb14 | 2.41308 | -60.88198 | 2026-08-29 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 507e98a9-3655-3add-bc78-8c623805578b | 2.40755 | -60.87775 | 2026-08-29 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ab9252a-cde6-3411-a1fb-f45cf00e17b2 | 3.28417 | -60.61395 | 2026-08-29 06:10:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8020e138-a9c5-39d0-aad5-4406bd23e79b | 0.14511 | -60.40356 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2830f08c-859e-3af6-b628-68c29e0ccdb6 | 3.11289 | -60.70321 | 2026-08-29 06:10:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 491269bc-c2ad-3dc7-840c-8a9d413314da | 3.23263 | -60.13383 | 2026-08-29 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8052cc8-2748-3f92-b69f-acfe3dad4669 | 0.13911 | -60.39849 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 504ed0d7-da28-386e-a159-daacd683b561 | 0.14416 | -60.3977 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 629cf242-2bda-3d23-abde-106136d754ce | 0.61271 | -60.15548 | 2026-08-29 06:10:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4ce5684-fcbd-36bb-8aba-2a61d8a9e815 | 3.109 | -60.70895 | 2026-08-29 06:10:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cabc9de-5379-39d7-9ad2-c4bb808cd09a | 0.14005 | -60.40431 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 651a452c-78a4-360f-a889-ed709afa3e75 | 0.13958 | -60.40141 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35c4932d-62c6-3892-b0fe-825591953980 | 2.40837 | -60.88276 | 2026-08-29 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bde93ffa-0aef-36c2-b642-165f1a6fb8a5 | 0.91474 | -59.62838 | 2026-08-29 06:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 623e3301-4e84-3460-b090-390c37bd7fe8 | 3.10817 | -60.70397 | 2026-08-29 06:10:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84172d10-34de-3974-ba3a-c6eef7d3b01d | 0.14464 | -60.40062 | 2026-08-29 06:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b273e8b-f6aa-36d2-b2c1-93ef2ec1b047 | 3.23357 | -60.13944 | 2026-08-29 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53021ef2-7dd2-3b16-9999-7f15ae97145b | 2.41226 | -60.87694 | 2026-08-29 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20c1d578-c125-38cc-b2fa-efa1fcb71d2d | 0.91421 | -59.6251 | 2026-08-29 06:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
