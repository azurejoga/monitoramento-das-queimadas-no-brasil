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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e79b79f-91a3-3737-8526-30438f570b78 | -6.627 | -43.95522 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36afc870-0447-3c32-bb67-11272d1165d3 | -6.98187 | -43.10225 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f9f59e4-4e19-3406-90e8-3d9ec63ec01e | -8.3878 | -48.28549 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3352550-d5bc-3d7e-ad57-7858411af017 | -6.97404 | -43.10098 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ce2ea2f-c69c-34ad-9c66-ade36498dc58 | -7.80407 | -45.4627 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 535f1b63-c352-3c04-b5f4-454b014fd327 | -6.91412 | -44.36612 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8645b08-c7b1-3840-b46e-158037c274ed | -5.94287 | -43.7226 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b41e3e-4586-32e1-b526-6ae6b23a3817 | -5.8105 | -43.22433 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1e5559b8-b0fa-34bb-ae1b-16b0fed59a96 | -8.07625 | -47.60937 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff51151-bb12-371d-8679-92964bbc6883 | -8.8808 | -45.83022 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16a314bd-0638-38aa-b008-ba49e9cd6a3e | -7.92757 | -46.43339 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae5c095d-8854-34c5-9f95-45e975a30f64 | -6.77059 | -45.87874 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 136346ff-5f6b-3920-82dc-02b0d360cc93 | -5.60971 | -45.02448 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3721f743-eca7-3780-b9cc-8f50152755c6 | -5.94574 | -43.73073 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d545d832-c1ae-3f12-a80b-1f979a7497e2 | -7.48969 | -44.81913 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b3c0da89-aebb-3c03-bacf-093d3cd4def8 | -6.26413 | -43.30501 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6141a9cb-267b-308b-9143-0221385c0faf | -6.25221 | -42.60935 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f147eb9a-7af2-305d-ab9f-e8967cfb57a9 | -7.55398 | -45.71027 | 2025-09-03 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117158bd-7a68-3c9a-a75f-6eae162a5161 | -6.7907 | -41.78354 | 2025-09-03 03:53:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d12e7804-7302-3f2b-96ae-137db5f13ceb | -7.93065 | -46.47258 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2faa06-215d-3165-8d82-5a1b15ea8a60 | -8.8194 | -45.80298 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff059183-1971-325a-a438-408c8300411f | -7.11945 | -44.76171 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21672863-07eb-3928-ad71-120386000649 | -8.91043 | -45.11956 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19903d8c-83dc-3c7d-9abe-5a0f55c19cf9 | -6.78616 | -44.29984 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba6b2b99-c86f-392f-9fe0-9c8df94bbbc5 | -7.28817 | -45.2846 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c9e89fa-e1f1-32f6-95d2-3a0332f39a54 | -8.54493 | -47.47524 | 2025-09-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 775ae054-4a93-3a23-b128-30a1bec92bad | -8.45731 | -45.05005 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de380c7d-b566-39dd-9671-1aff4feac6a8 | -7.47824 | -44.82763 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f643d0ae-33e8-3885-9355-371fecdb4049 | -7.48384 | -44.82698 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd9a2241-415f-3d67-9e9f-47350f1c9ec7 | -5.95857 | -44.29034 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb731f76-f2d9-351c-b3f0-0bc866acf115 | -7.90558 | -46.44565 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad47ee77-d836-392a-af30-4b639ffaab0e | -6.78238 | -44.48002 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce70f686-4f06-3fd8-b2fb-1e6494bcce21 | -8.87178 | -45.82832 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a01c0214-d5d6-3a73-800a-622eb72b2240 | -7.70645 | -48.72632 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 721840a3-5722-341d-86a1-7f933edeabba | -7.92588 | -46.47147 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88345472-aa24-31ff-b819-893b19ad5487 | -6.53835 | -44.56444 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64476a93-158c-3905-ae59-c950deffd9f4 | -6.12675 | -44.11969 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2f70a57-ef58-3e51-9170-ac731d466ad5 | -7.28877 | -45.29242 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff0bb8c-92fe-350e-b2d0-bd03802c120a | -8.87467 | -45.83841 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16ef869a-58be-3293-a231-eafc8f2989fd | -7.50643 | -45.34072 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4608cb22-16ab-3531-9945-def3bae2abf2 | -6.24899 | -42.62854 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f6aeb550-a7b6-3dfd-a905-d18b72b92d2d | -6.87815 | -45.56483 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d5ec21-e247-318f-b9a9-6e3f45843a59 | -8.02335 | -44.08824 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f7b5325-a286-3ea0-ba3d-9d9b99e589c5 | -6.69845 | -44.17691 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 787e35e0-f0ec-3fd7-bc7b-291be330866c | -5.80505 | -45.62651 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ed08a6d-ade4-3760-8172-0c941f6eeb17 | -6.9486 | -43.27798 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35920778-e664-332a-9b27-bd42c810f549 | -7.90944 | -46.45188 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d985727f-08f4-3fc0-be9a-9985898eb21f | -7.01984 | -44.35512 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78f5a31a-d759-307e-a1fb-539dd1fafa1a | -8.43655 | -47.34305 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87815867-79b9-3354-976f-5001e32d63c5 | -8.42643 | -47.34112 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e98e4d7-2b23-33d7-b85e-e8f0495408ca | -5.6903 | -45.95237 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee1776c7-bb6b-301f-8589-3a6658782462 | -5.6125 | -45.01346 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d5b9765-6e97-39ad-b684-ec5247865edf | -7.03332 | -37.307 | 2025-09-03 03:53:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96c65026-811d-3956-8955-8819b7c09065 | -6.41239 | -43.76384 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53ef4ee5-f7a9-3105-8d07-d5b070f2475e | -7.69797 | -48.74089 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7723484b-bb87-33d4-9740-54d2a842fe52 | -6.54642 | -42.9644 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4f81838-9de2-3d01-9dd6-d20f279e2fcb | -7.00233 | -43.2424 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 83b43016-c588-324f-879b-8befc4a64cbb | -7.63123 | -42.64806 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0df4362d-5b24-3b18-9103-e3e1c0a86ffd | -6.22754 | -43.39951 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 509718ba-bcf3-3896-9f13-9367555f2a5d | -8.0769 | -47.60981 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad1933b2-773c-34b1-843a-eb5ce27cbeec | -7.00606 | -43.2249 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bab266ae-bed2-3339-ac89-78bd7bbfc216 | -7.92481 | -44.94088 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 281bc8c8-25de-3f0f-a501-6d68dcefe8c9 | -6.54027 | -42.95322 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92349e54-0a1d-31ff-99d0-d2814aa01b61 | -6.68997 | -44.17582 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4806903a-bd67-3e0d-a701-2d45e5a04e24 | -7.71659 | -50.25039 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13f51ae9-2649-3772-9714-2323c19652c1 | -7.72147 | -50.25146 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdd9c5ff-6807-375d-b13d-e92cbb10a686 | -8.36658 | -48.31043 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c400cab-5bd3-3678-a107-f39b05a95ceb | -7.90571 | -46.47307 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ed810c-02da-3a2a-af5f-4442e42649e8 | -8.36723 | -48.30681 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a67344c-7177-3dfc-888f-ca76ca58c309 | -7.69546 | -44.98596 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83dcefe5-9122-3557-823c-7a6aec072b34 | -7.47674 | -44.80997 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 407ec031-1165-3cb8-8156-b81b63dfb64c | -6.17404 | -43.31855 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ae841672-4116-3a7c-bad2-3160d1e2c248 | -7.49043 | -44.81486 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5df4aa74-8614-3405-9bf2-d089bf252f80 | -5.93603 | -43.03569 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5940262b-64ab-3adc-af91-88a267746e5b | -6.22532 | -43.38816 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dc6ddd2-82a9-368f-ba25-3612341fdf1f | -5.89184 | -43.35757 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11795397-0652-386b-87be-76a39e0b5c57 | -5.93998 | -43.03637 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b8191bc-5146-3d43-a3b9-97e92e600d5d | -5.81509 | -43.22157 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d421dc8f-9a15-3805-8d00-f6e8221db6e6 | -5.80188 | -43.2265 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ccb6019-599a-33a9-a8b1-01a9b444fb5f | -6.03429 | -46.01096 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f8b1e37-856b-37d4-ac3c-c39a145e07b4 | -6.45188 | -42.38981 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 09a0b4a8-b811-3c2a-b30a-25d87e042983 | -6.9311 | -44.26259 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49350740-09f4-37a4-8cac-90fdfa8d5f43 | -8.37198 | -48.31145 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6127e4dc-fbf0-3381-bec1-086f8cde6efe | -7.91053 | -46.47391 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5b79b86-2dbc-364e-ac72-ac4c5f7b83d8 | -5.89299 | -43.35046 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 718576ce-cb9d-3fae-a366-de1ed19961ec | -7.93384 | -46.54016 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 51097d1c-7a75-3c22-ac8f-7a6ae846cc2a | -6.28677 | -43.59194 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9892406-5d96-3e67-ad12-e91c4b86f553 | -5.89355 | -43.22052 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f29ea6a8-3a2e-3ee1-ac28-ecb804566922 | -5.9844 | -42.37805 | 2025-09-03 03:53:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8159e75e-7f88-3c71-868d-6d8c2bab0f40 | -7.71701 | -48.73211 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34230d46-8713-3188-b00e-31536b0a4390 | -6.73064 | -42.25647 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7063ec39-9d51-309b-83e1-068704985921 | -6.95965 | -42.97161 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3f34a097-9df0-3924-baba-453bb0a9be7b | -6.11983 | -44.13476 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08931105-943c-302e-bf89-e713f5d6e949 | -6.66455 | -45.92093 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63a3100d-e6bd-303c-9156-11ce7b712c79 | -6.34552 | -43.76901 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc1c4d5b-3cea-32c3-af48-7b26813ec68d | -8.36977 | -48.29269 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89386890-fa5c-3b67-a73a-f6060af49cf7 | -6.40828 | -43.7631 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 783670f0-8959-3c54-b485-91a9521aba64 | -8.05634 | -45.37574 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e7d0ba-b6ec-3305-8b3e-970a4c7cb095 | -7.4761 | -44.84037 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e4b11d4-97f8-3367-8af1-ec3937ccae3c | -6.95577 | -42.97097 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README29.md)
