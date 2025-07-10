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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1265a21-717a-342f-8d6d-b308d8d5c743 | -11.06758 | -45.86997 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28778064-9b97-3045-9353-e7085f2934f1 | -13.37386 | -47.89923 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38da0af3-cd31-36e9-8e77-d9e2d297aa1c | -10.57211 | -49.13999 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7db0486e-7e64-3029-8874-db9b28b93fec | -9.31751 | -49.22409 | 2025-07-10 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8af685cb-78c2-3886-a6a0-e90c926a22d7 | -12.99611 | -46.28445 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e44200f-2db9-3bde-9116-9da602710a24 | -9.2183 | -48.59626 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c27364ad-e50b-31ef-9482-b358b05f17d1 | -12.42952 | -43.71733 | 2025-07-10 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afd24eef-b0d4-32dc-928b-c005cc676d84 | -11.00312 | -42.7792 | 2025-07-10 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b41adde4-cf35-3498-b0d0-e0d8a55594ab | -11.73606 | -48.52971 | 2025-07-10 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a928ee9b-bbf7-3b75-a7b5-991e918cdcdb | -10.96763 | -49.2519 | 2025-07-10 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 908b943e-49bc-31bb-9877-b0fe3316873a | -8.50755 | -43.30601 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 59ca1ad7-1312-39ca-b419-65a0e97de8ed | -11.36963 | -48.70325 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b0bb8e2-885c-3543-b0a4-37abb2699955 | -10.62645 | -45.23832 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78cd5bd3-29dc-3c30-b73e-7f66a1287712 | -11.46146 | -45.10531 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05b5c3d4-c6db-32de-884f-57b739d81a02 | -8.50688 | -43.31009 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d3d610b0-ab7f-3331-87c9-7778c3f8011a | -8.50198 | -43.31764 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| f23f2664-5a91-34d8-a277-d42aade2cd2e | -9.83438 | -41.49516 | 2025-07-10 04:04:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d9ed863-1248-37fc-b5d1-7f2bad27976c | -8.5103 | -43.32171 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ce4e075d-8c9f-3312-adc5-bdc7323b66e2 | -8.50265 | -43.31356 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 222e6013-4748-3225-a63a-c00bb42a1fc5 | -8.49526 | -43.29139 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6e8f48ae-eeda-33f5-ab0b-4bde8b524f62 | -10.65671 | -49.4655 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6519fde1-9d41-3963-a24d-642374ab16f2 | -7.95102 | -49.64817 | 2025-07-10 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca00b26-9c03-3d9d-af07-df5c30c58168 | -13.38706 | -47.87664 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99ab581c-78d1-3afa-a260-47adbe9d619e | -8.50178 | -43.32867 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a2730769-cd22-34a8-82f9-f5935ddc668d | -10.63965 | -45.23075 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303878cf-220a-33a1-91c9-23e5946b4a77 | -10.57608 | -49.14641 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 381a5eb4-f8c8-31cd-9b7c-dbd7650b70d3 | -9.31809 | -49.22099 | 2025-07-10 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55c84fa2-3939-39f4-86ab-c2812347b8b7 | -11.06362 | -45.86919 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36c5c6b0-0c31-3c32-ac9b-abaf232c10bf | -13.67533 | -44.22068 | 2025-07-10 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f288ec8-0296-332e-9a39-c1f5db001c40 | -8.99518 | -47.45076 | 2025-07-10 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d0a5d88-6607-3c8d-85f9-4bc519dc9457 | -13.34157 | -52.88972 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7758af3c-82e4-31ec-b8a3-2ee076ec68b5 | -12.24277 | -40.96826 | 2025-07-10 04:04:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b50037c-d71b-36c1-9dab-55443a72bf2f | -7.46345 | -49.40274 | 2025-07-10 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b78df44e-52b9-3adf-99d9-28a3e326ed7d | -14.63161 | -46.83975 | 2025-07-10 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7a649be-e547-341b-b758-32b62bf0095e | -8.50979 | -43.31476 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 80c856a6-4893-342f-8245-2834f63b94f3 | -13.00851 | -46.32959 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 029495e7-a267-38eb-a7ec-18951099806b | -11.36548 | -48.70057 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0344e10e-26c9-38d7-bd00-095e2934e4b9 | -9.30522 | -40.24246 | 2025-07-10 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d0380be-563b-35bf-9009-788f484d5a29 | -14.73418 | -41.7294 | 2025-07-10 04:04:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e7c1323-0ff1-316c-9561-c77ccdf732c5 | -10.6303 | -45.23901 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c1bfe14-90bd-3954-b3af-9ac26ba74cc2 | -8.50658 | -43.30016 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| b5d54194-1652-3971-a45c-6ba8c65bc790 | -7.48213 | -43.93245 | 2025-07-10 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61d21350-53d9-3afe-8213-1b787f134e62 | -13.34681 | -52.89986 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4af3c939-b8c4-3ec9-82a2-2dc403261963 | -13.90173 | -42.13292 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2e629008-e615-30db-946f-89cc4b5bf817 | -8.50809 | -43.31297 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 5f4383bf-9e17-33fd-85c7-def2ac168081 | -13.90117 | -42.13647 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 86deca8c-512f-318e-b567-c490cf5a7878 | -8.50065 | -43.32581 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aef10ebb-874f-3191-9024-357b3b7c736a | -8.50622 | -43.31417 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| e0c3f913-d546-31d9-aae0-f88e2d7b494e | -7.95038 | -49.65165 | 2025-07-10 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cccc4fa-8fb3-34a8-9391-030539989ac3 | -8.50521 | -43.3083 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 6ea60674-d347-3ac6-92c6-eec2a606add4 | -8.51098 | -43.31764 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec70d5e1-ba21-348f-b0e3-57752de12a53 | -8.99974 | -47.4516 | 2025-07-10 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37d6c158-e3f4-3af8-a2e0-6b05fa928cc4 | -10.66347 | -49.45731 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 308e6677-3904-3aad-ab93-25454dd32acb | -8.49907 | -43.31297 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 414a2cd2-83e2-3ce1-af00-de34793013f0 | -8.51045 | -43.31068 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 1b491ec8-a5fe-3a20-a7d3-172751e1c557 | -9.09267 | -47.96552 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6af089e-ce82-32f6-a306-11fe1b74a3eb | -10.69604 | -37.04758 | 2025-07-10 04:04:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad8ac872-eac8-3806-bc2e-8f7c4af53fb1 | -9.2162 | -48.60021 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e76fede-68c5-30df-abc7-be670c58e002 | -13.34013 | -52.92802 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2899a533-a455-3fc8-b1f2-3381a04ca95a | -8.50794 | -43.29202 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c523afdf-5c05-3cc3-9ef2-ae3f36ba94a8 | -10.61557 | -48.07858 | 2025-07-10 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76564a10-6ea7-37f2-bfe8-1b98900a644c | -13.37468 | -47.89481 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce04548b-ce79-3eed-be76-bcf913101eaf | -8.4049 | -46.93028 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95bfdd61-67e7-3467-a699-2920051bc02b | -8.2205 | -46.96159 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e5cd7ba-845e-39dc-a302-9e4c68beba2d | -10.90333 | -46.7371 | 2025-07-10 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e244e0-fbde-3e4c-95e3-70d2ba072f33 | -8.49434 | -43.27457 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fde1dcfb-baa4-3778-a60d-4afe8e277b79 | -11.05965 | -45.86841 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eff0eec-b300-38cb-bbc7-38a4706b7df9 | -8.36059 | -43.9509 | 2025-07-10 04:04:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2650c1d-a813-3ad2-93cb-0e587b14934f | -12.57467 | -48.88239 | 2025-07-10 04:04:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d97045f-914f-3c0c-bb8f-4909401379f9 | -12.56026 | -52.21842 | 2025-07-10 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aea7b5e5-3e4a-38ef-8bb2-36937cc50983 | -14.98014 | -42.29008 | 2025-07-10 04:04:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4ea1475b-897f-30b7-8e3f-70354a6552b7 | -10.58 | -49.15311 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 90acf840-307e-3881-8e46-f30bcc33c0b7 | -8.49683 | -43.30421 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8270ed2a-86da-3465-8714-3b4901729e6b | -11.83278 | -48.21327 | 2025-07-10 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91fcb857-782f-36e2-8131-0a1c756f0e25 | -8.50536 | -43.32928 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a237927-6950-3b9e-9a41-11ab301f9045 | -10.66292 | -49.46035 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4742208-5f50-310f-9b85-3ab2825d4971 | -8.50556 | -43.31824 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 8943aa86-7f86-3602-8979-cf0bf58583e6 | -13.55364 | -40.24255 | 2025-07-10 04:04:00 | NPP-375D | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9885c2ff-2ad6-3490-9aea-67b84ef0eef3 | -13.34295 | -52.91404 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c1156dc-0fa3-3c0f-87d4-74a710a6a0a6 | -13.38194 | -47.87997 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23a23131-eac4-3b48-bc4e-4c8b7f7b3e90 | -12.22088 | -44.21189 | 2025-07-10 04:04:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 809325a2-80df-32f6-8cfa-822114d78031 | -10.56606 | -49.1448 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| bfba9918-e046-356c-b2dd-c41f3ef06976 | -8.50132 | -43.32172 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e78861b-f873-3dd9-91a9-0ccdef463185 | -13.28043 | -39.85995 | 2025-07-10 04:04:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f1daea97-274e-344c-87de-1af74334b03f | -11.07064 | -45.87601 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea789553-2709-30c6-af61-cdb184e40a0f | -10.51279 | -43.92483 | 2025-07-10 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30bf8fdd-72b6-3099-937e-597a80bdbfd6 | -8.50962 | -43.32579 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ce9626f2-65a5-3872-972e-a0e2321bfe88 | -8.28633 | -42.27172 | 2025-07-10 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1bf9936d-5029-39a1-a2ce-616c8965b8a4 | -13.36954 | -47.8982 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62f2743a-1c92-3486-ae86-228275887767 | -10.66688 | -49.46744 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90d3e1cb-0639-33db-8047-a02216a8f431 | -7.70431 | -45.77186 | 2025-07-10 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61de9ada-ba8c-348e-8459-58f7dcd2dd9b | -8.35616 | -43.95466 | 2025-07-10 04:04:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 563d2c6b-b43a-3a05-87ff-2c77cefc04e0 | -13.33877 | -52.90359 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46087863-8755-32b9-91db-16a7acfad67d | -9.30577 | -40.23896 | 2025-07-10 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 825c55b8-f2b1-3209-bb63-a6a0b1bf92d9 | -7.648 | -45.3476 | 2025-07-10 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ac1824a-cc5f-3d9a-bd5a-b02c283bdcf7 | -13.28016 | -39.8598 | 2025-07-10 04:04:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 831feb0c-5af2-3bc2-978a-0462989dfa79 | -13.01699 | -46.28201 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc015db1-6b06-3f9b-9ee8-13cb79b356ee | -10.64984 | -44.48764 | 2025-07-10 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d757b21b-2572-3be5-873c-27364282ed9c | -13.33971 | -52.89896 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb594cb4-25d3-3cea-a4e5-5cce8653479e | -12.98541 | -47.82737 | 2025-07-10 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
