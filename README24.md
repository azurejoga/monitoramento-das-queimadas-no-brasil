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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56a3e409-aa45-3930-8edd-c8d1b831d5d1 | -11.21384 | -45.08359 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3c78dd-4e3e-3767-b3c8-e54dff6c8cd0 | -11.35522 | -45.16784 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6b8afd7-21a2-3800-89d7-27980dd9732a | -10.13141 | -45.6989 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ad4314c-d709-39f3-9ca4-653336828097 | -11.36168 | -45.16481 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df82ba5d-845c-3ec2-9dd8-40d9e55f77be | -11.35681 | -45.15968 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b414e6db-fdb8-3a3f-adc5-2172408508be | -10.13378 | -45.69935 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d68b1f74-b390-3d1a-8a09-638ac0c4520c | -11.356 | -45.16383 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57d4163d-b4b2-38da-9e09-4b96df335d63 | -11.26771 | -45.33639 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17dfc4bd-aa5b-387c-8015-4a417ebe2e29 | -12.78302 | -46.45956 | 2026-08-30 03:38:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4c85b4c-baee-374d-83d4-716f9be5410b | -11.27074 | -45.32062 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b35ee162-ad5e-3680-b361-324dea8b0edc | -10.787 | -45.34 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2a07f3f-94a1-32ce-9064-0cdf639aa52a | -12.78568 | -44.61648 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47503eb3-29b9-391a-ae6a-2051bf5e38bf | -10.14212 | -45.7077 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8b9cc77-06a0-354b-bb0c-03ad6bda6ac3 | -12.90467 | -45.87692 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1efb20de-d942-3c32-baf6-67cc8d21e0d1 | -10.13287 | -45.70397 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b1da683-9353-3e3b-abaa-8774656d8837 | -14.94869 | -40.83332 | 2026-08-30 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4741a591-3664-3d4c-9a45-f089b9cc1f84 | -10.80835 | -45.32248 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7ad36be-f3a7-317e-b041-64993f6ac451 | -11.51544 | -45.54546 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ca2b8412-2429-361c-9c96-7ae36edf88b3 | -12.92405 | -45.90162 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08899c7b-93da-3d49-a614-a68c5cfeace7 | -14.33759 | -47.22726 | 2026-08-30 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ffaf234c-86cd-326e-87be-41477841e232 | -10.95731 | -43.03479 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89ac16c3-f3a2-3839-b59f-be16c47d86b3 | -11.34396 | -45.15282 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f870b2d-bd34-3e9b-b035-45587634f3bc | -11.24872 | -47.05401 | 2026-08-30 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31c498aa-be59-3507-9342-34071d7a706b | -11.21951 | -45.08452 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66865810-875d-3f9e-a0a8-ab00eadbb22c | -14.33661 | -47.232 | 2026-08-30 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e673644f-4d31-3d3b-be64-603d8348a2b1 | -9.21701 | -46.0715 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 33a41a74-e47a-375e-9c4e-d08a8e680b73 | -10.79028 | -45.32315 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 82102a16-4c77-3d2f-b81d-aaee4db324ab | -11.26846 | -45.33249 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fea60fef-4d5e-3cf7-9d82-2b43ed5e73e5 | -12.19303 | -40.40535 | 2026-08-30 03:38:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7167fa96-033b-3e4f-a2f6-405a50a3597f | -7.94908 | -44.26403 | 2026-08-30 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 903abe4d-0a89-3eba-bc22-0ce5e4389ca6 | -10.94816 | -43.02416 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a94ce8ab-a4db-3c25-8542-21efe37615a0 | -11.26579 | -45.31554 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 054e48eb-9c9d-3d78-aea5-197cac359468 | -11.51778 | -45.53353 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baa0ebaa-2f05-3607-959a-4da9ffedd1b2 | -11.23676 | -45.10096 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2555feb8-ed87-38de-ac37-3cd76488eaa2 | -8.14158 | -45.47086 | 2026-08-30 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b150a6af-1c19-356f-9d4a-940b13bc32ee | -12.89813 | -45.87974 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 092fccf9-e7d3-35d9-9424-2b91e844c20c | -7.94832 | -44.2681 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8629c788-c2cd-354c-978d-592c63ea4198 | -11.52618 | -45.55191 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b07ff55-edf2-3b8a-9c78-609683bf40ae | -11.48411 | -45.06225 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 628eed69-fe45-3212-957c-53badb2cc1d2 | -7.99647 | -46.5081 | 2026-08-30 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86723637-b654-300c-80a9-de8f5a114b70 | -10.14313 | -45.70236 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6625a0b5-2716-3256-8b35-4ffd6375acdf | -12.19239 | -40.40904 | 2026-08-30 03:38:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90c656bc-634a-327b-8761-36bd1c3bab12 | -11.48483 | -45.05856 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 022b9bec-977c-3ba6-87ea-0ea529584d53 | -11.48554 | -45.05487 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6846c835-b43b-3a0c-aea8-4dabb04dfee1 | -9.76725 | -48.16628 | 2026-08-30 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b0f3a8d-1379-328d-a975-a25f075aff2e | -8.20653 | -44.81372 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1bd3bdcb-a476-3b57-8068-7a13e46816d2 | -11.51699 | -45.53755 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ad0e558c-3fb6-3757-a34c-be6634e2065d | -9.2108 | -46.07034 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f9844a3-3b80-37fd-bedc-bd4fc11b7b82 | -11.33757 | -45.15559 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 101b24c2-88ed-393d-b360-f8a25314f14b | -11.352 | -45.15428 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3a3c55f-9780-3754-9f9b-2e9a658f6144 | -8.22369 | -40.77057 | 2026-08-30 03:38:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b92e80f-9f47-3539-bcea-4074db0190e1 | -12.08795 | -47.20072 | 2026-08-30 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acee9c46-a41a-32fe-96d9-592dc16dd8ec | -13.13579 | -42.01478 | 2026-08-30 03:38:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ebb66005-2412-3a29-90bd-e56a1d802488 | -10.14405 | -45.69748 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dc10b6a-09d1-36b2-b592-601bd9d5f8af | -5.4876 | -57.1416 | 2026-08-30 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5fd2ae88-0d7f-34df-9e99-5beac32ede8e | -9.8927 | -60.2752 | 2026-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8b97d081-438c-3ab1-aecf-c833da0f88bd | -4.9603 | -55.8622 | 2026-08-30 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5ce7a097-dc29-30a3-921c-6f4d483061e0 | -4.9604 | -55.8424 | 2026-08-30 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| c7802a5e-269e-3f53-a597-07a38fae047c | -16.27718 | -42.57344 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80c2d947-4144-36b7-9e7f-7269eebac169 | -16.27688 | -42.57621 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e25d9691-c6a2-3430-bf23-d7781d86d00a | -18.52605 | -42.15277 | 2026-08-30 03:40:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 878b2b63-1af5-32ad-8a85-7f81d6597fc8 | -16.7183 | -47.63644 | 2026-08-30 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 134e764a-d102-3fe8-b88f-f922e679a8d5 | -17.86287 | -44.29371 | 2026-08-30 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d996b3d-b31a-3653-8ea4-3f311d405330 | -18.66298 | -46.84862 | 2026-08-30 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3db82077-6204-3e43-85c4-4de691648931 | -18.66376 | -46.84492 | 2026-08-30 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 780db399-f76d-3cc7-aa8b-e1aa37cbbfcf | -16.2816 | -42.57404 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 111fec06-1f83-3809-a396-4c68fd474427 | -16.27329 | -42.57125 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d188dd15-f2e0-32e2-baca-a308719f3bca | -20.51125 | -49.04965 | 2026-08-30 03:40:00 | NOAA-21 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 826f9c22-aaf6-3604-b93e-44fe8bfb4710 | -17.29159 | -46.0127 | 2026-08-30 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18b4a1e7-36d6-3dd7-9d19-c1e289ccb24a | -20.11455 | -48.26922 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 62bf7da8-38f8-3093-b874-90c84c15e6d8 | -21.19376 | -46.82134 | 2026-08-30 03:40:00 | NOAA-21 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f5dd252c-8c8a-3a3e-983f-d261cf8d311c | -19.74597 | -48.97675 | 2026-08-30 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c10846e5-2344-3767-b5ed-57713d7934f9 | -17.79129 | -39.70848 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2d4c0025-e3c1-34d1-9034-518a579f7576 | -17.41659 | -42.62763 | 2026-08-30 03:40:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ba4dbc67-edd4-3ca0-9a0c-fdeead547e43 | -18.81795 | -47.45674 | 2026-08-30 03:40:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85fc0162-663a-32eb-8e67-7e5fafbedfd5 | -18.45956 | -44.89896 | 2026-08-30 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7dac486-b78c-39d5-825f-266e9b34d830 | -14.77417 | -48.7346 | 2026-08-30 03:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46e93d52-c452-30c9-9a6d-5047bcdeca1c | -20.20313 | -40.39631 | 2026-08-30 03:40:00 | NOAA-21 | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e0882dc-f2e0-321b-a72e-eb468c12a1ad | -21.19447 | -46.81802 | 2026-08-30 03:40:00 | NOAA-21 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a1e863ab-251f-38f8-a155-a0a9e5e6c1ba | -14.9011 | -47.74863 | 2026-08-30 03:40:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67ffa29c-adc5-3f9f-93aa-99fc1cc8bd84 | -20.11499 | -48.2711 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eba8d428-4b18-3b19-a6f1-f12ca0f87094 | -19.23216 | -46.73373 | 2026-08-30 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14a7aa2d-9f02-38e0-af29-34f1f1d702b9 | -19.0962 | -46.24027 | 2026-08-30 03:40:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d951e27a-9e98-30b7-8c34-1cbbd189e13e | -20.59304 | -47.65582 | 2026-08-30 03:40:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26d03f94-2715-3156-a5f8-9fb6c02fef09 | -20.59393 | -47.65185 | 2026-08-30 03:40:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 537d68e1-3bf7-3915-b7c7-702b7736681f | -16.71926 | -47.63198 | 2026-08-30 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 438749b0-93d7-3abc-8925-6893c7bb9901 | -19.74003 | -48.97396 | 2026-08-30 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71c71d23-6bb7-3a36-bd74-c4a49cd727c6 | -19.74601 | -48.97589 | 2026-08-30 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fa27cb1-3dd0-3200-bead-75c1bafcd7df | -17.79567 | -39.7048 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b1413ffd-1564-3daa-b420-d390f6d1dc4b | -17.7949 | -39.70916 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5eaa33b6-00e6-363e-9279-b44039eb4d22 | -16.89249 | -39.31733 | 2026-08-30 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 278f46b0-6f6c-399e-9066-8154188d3f2f | -20.11352 | -48.27373 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c34363c7-8d60-38e9-b012-e8471ea9eafb | -14.75194 | -48.74162 | 2026-08-30 03:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e85472b4-07aa-3089-a8c6-89e3a2ea1f83 | -17.85238 | -39.76511 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7a8b18f2-3527-36d7-a92c-debbac481071 | -18.4644 | -44.90018 | 2026-08-30 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 719c8b1d-44ed-3f6e-a7a8-c807b391acc8 | -16.1412 | -43.05359 | 2026-08-30 03:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66f1b3ff-8e82-315d-85b3-494cda2686f5 | -14.89753 | -47.74525 | 2026-08-30 03:40:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19a6604d-6dc7-3cd7-97f0-bcf9e4613b3b | -14.77307 | -48.73966 | 2026-08-30 03:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dae2e20c-8d83-36de-a240-d59a7df341e2 | -17.35676 | -39.41186 | 2026-08-30 03:40:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e590d7cc-80e9-3f02-9196-5aa046bd1317 | -19.10143 | -46.24149 | 2026-08-30 03:40:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
