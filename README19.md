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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7d0a751-24ab-3a40-9a67-4ca0f5b75c1b | -6.88691 | -43.57664 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d0e5d33c-c1ac-369c-8e3c-230f9613bb66 | -7.34576 | -42.43824 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f80ddf6f-1c50-310c-ac50-949a7adc49bc | -7.42781 | -41.87565 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f98bf409-30f5-3707-ae20-b69d4cfd49ab | -8.36082 | -46.16189 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a589663-6f64-3162-acef-d8538f53edc7 | -8.65155 | -44.76839 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb84a1f0-3d1e-3256-aacd-85bbc16cf107 | -8.88182 | -44.84059 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02d9768d-2c34-3c21-b50e-058e8083ac4b | -7.43697 | -41.86632 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bca6c462-c418-34d4-9a1a-ffe45eea39b3 | -6.6764 | -41.51128 | 2025-10-27 03:42:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 232843a7-6e2b-36e3-a96b-0f9814834e45 | -7.838 | -46.49712 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40a02c82-2ee2-3145-8807-d4f184cad91b | -8.65091 | -44.77183 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d79dc88-a990-38f6-9c38-8fffd29e2aae | -10.34936 | -47.18004 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 426e7314-83d8-378d-bd09-1758edc90a1a | -6.4934 | -42.21937 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| caaabeb8-a109-3d18-b1a2-30eeca8f8fd4 | -7.67678 | -46.33966 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce7f333-6024-3f2d-b5b7-e5519792a9af | -6.49051 | -42.21622 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d45fbb01-0d75-304c-8741-362be7e3ff3f | -7.9695 | -45.46904 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8a7e08a-ace9-3ba2-a7d3-d004f4825f4c | -10.32218 | -47.21452 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c713b44e-0f84-3467-9648-24ab87b5600d | -8.06739 | -42.49148 | 2025-10-27 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 36c455d9-e3cf-3404-8c9c-47c80917aaca | -11.29039 | -45.15307 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a3f56ac-97be-3a07-8886-5651c1404e74 | -10.04408 | -48.16655 | 2025-10-27 03:42:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e4b5f3e-0d03-30a9-a490-09fdfdb51c91 | -7.09314 | -39.56369 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e75555c7-ebb4-31ec-9c14-b0a3f227f161 | -8.5324 | -45.56163 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c776368e-9e19-3e6c-ac5f-9512bc0cab86 | -7.7928 | -45.3838 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eb7dcad-f517-3d1b-83d8-7f8c1637f609 | -7.68169 | -42.18639 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13a5cd92-32ab-34c2-a920-da0925ae8dcb | -7.23504 | -44.98994 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f6376d-3f51-3a07-8965-dd819669a271 | -7.80742 | -45.39878 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9cfbc49-2f88-3011-85f5-62f85fa7bb44 | -9.57911 | -45.18979 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 556f62be-ca75-3703-a684-0ea445e8079e | -9.9863 | -47.18451 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f714bea4-fd6d-3789-b5ab-f1c0c32ea0d1 | -9.47893 | -46.85984 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c04914a-f307-3a89-a428-b8ba4c2a43a4 | -7.69235 | -42.17859 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c4f34e25-d668-3067-8b41-666bbe9d4ed3 | -8.48019 | -45.56204 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b73bf19d-e102-3093-a362-43e8d0965ee8 | -6.43548 | -42.03901 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e3e022e4-8e30-3821-9b8a-7d7c8a055d81 | -10.75836 | -44.19741 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9930d470-e617-3a4f-9b9b-66ae1ef11100 | -9.48486 | -46.86126 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b051c7-4ac0-315d-9c2a-0d9dbe8f8a92 | -8.0289 | -46.7617 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45c75be3-f224-3d6b-a676-ff4c3d84287a | -7.59287 | -45.69014 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fed8306-0358-33ec-935f-6e129db582a1 | -6.45498 | -42.34153 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 040c924f-df99-3304-afe8-a58fec53049d | -7.84231 | -46.40723 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6df7394-669b-3faa-9205-51cad9bc331b | -11.41995 | -46.10359 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3a41d29-5c34-3a1b-9646-d2b3e3a7d4cf | -10.31635 | -47.17991 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a30a95e-ef3e-3f33-be57-72b1d58877a8 | -10.64342 | -47.94609 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d08420ec-fae6-3eb5-860d-752788d02084 | -8.64595 | -47.24361 | 2025-10-27 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ffa4aa2-acf4-39f7-acee-5ac73bcded7e | -7.76821 | -45.39137 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e8e8012-bd92-32b1-90ef-8643eea65635 | -6.22611 | -41.83004 | 2025-10-27 03:42:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac19d166-28cb-35ad-aed1-1d3d5ae0b8b8 | -10.42155 | -47.64913 | 2025-10-27 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e15f717-d9c4-36f9-8805-2b20b0a30a33 | -7.84743 | -46.41294 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cb9642d-c245-3ba5-88b8-74462168e0b2 | -8.58025 | -45.11395 | 2025-10-27 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bd0e8a0-3506-346c-81fc-8723f5eed956 | -7.21242 | -35.78052 | 2025-10-27 03:42:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94a03be0-0058-3b93-bcd7-7b9b2b86fd06 | -11.9118 | -43.82222 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8281e2e4-084f-3c93-9e28-898dd92211dd | -9.52304 | -40.30855 | 2025-10-27 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| cd0dc673-1f35-32e1-b579-2c094237ad30 | -11.42465 | -46.10875 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ce8e2b-7e1a-3032-9b94-39be768cf064 | -9.29752 | -45.23183 | 2025-10-27 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d0a17f3-5fb7-31d9-8aa9-4ebec64dead8 | -11.06457 | -48.33963 | 2025-10-27 03:42:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 481db2dc-1627-37ff-83b0-760a00fd7cfa | -7.82197 | -46.44987 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bbae7fb-0b2d-3347-8934-216761a1adb4 | -7.7935 | -45.38002 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36577cb6-15dd-3ea1-8524-cc017ad6748b | -10.3179 | -47.21263 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e47aa8-bb29-3bae-8420-332ba27a629a | -8.07047 | -46.94562 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0dc5294-7a24-38e7-8896-394b3470e3b3 | -7.83462 | -46.48183 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9f807314-f121-37d5-a6d8-9b84474b1a68 | -8.65929 | -44.7562 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1fba016-52be-3913-9b34-4ebf75853656 | -9.98904 | -47.17026 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a1d3888-a8b0-30d3-b882-48b310b5df79 | -6.88133 | -43.5788 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9da3577e-feea-3986-9a30-9d2be258895a | -6.83515 | -44.00266 | 2025-10-27 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf38fe1c-b751-3b46-af2f-eb871747caad | -10.95866 | -48.06736 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 961f8129-3d6b-39f9-ad45-7954d14f7315 | -11.42037 | -46.10336 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afbc272e-14e8-3e75-a0a4-8bb57cb7134e | -10.34906 | -47.17181 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5a3a635-35f7-3292-8b78-e67dbaa042ae | -6.88917 | -45.14671 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de34bab4-46f2-3f5a-8a73-275dd1e50dcc | -8.69802 | -44.43063 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4175f1c1-0698-3a1d-bebd-180bdb5b75af | -9.98723 | -47.17969 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d076c12-b1b8-34a5-a3b3-9d318a4e6b67 | -8.58148 | -45.11471 | 2025-10-27 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f8d14c9-3499-333f-819d-241e96d39501 | -5.76353 | -45.55821 | 2025-10-27 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 235e4237-62d3-30c4-bc32-89af03ff92ca | -11.43279 | -46.12567 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0ba317c-70ec-309c-bb46-2b8a9b5dbdeb | -8.70028 | -44.44733 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cf7764a-9cf0-398e-8189-6b6b6dbdf59e | -7.84057 | -46.48323 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95e38db9-af84-371b-8df1-a7742d288a32 | -9.58563 | -44.94933 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82454398-dd2d-39a4-9906-2c6caeec36f7 | -7.77377 | -45.39268 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ad9377-8584-362a-a7e8-45bbbc6e4b94 | -9.49058 | -45.81671 | 2025-10-27 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac452fa-e5cd-30de-a264-ee61c839beb7 | -6.43631 | -42.03419 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d334ab35-4950-36ae-afd7-d420938e9f63 | -9.18493 | -44.57295 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d865eb1a-7493-30ad-a48a-25f4d7545ded | -7.78786 | -45.37916 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f9160cc-4d2d-3d56-b2e3-1e82ccd1e72b | -7.82604 | -46.49457 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 055d9a2f-1546-3133-b434-957f70af8391 | -11.41924 | -46.1072 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 534de1cd-0419-3017-9da5-da8ee71cc1c6 | -7.83041 | -46.4711 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ac314f5d-1b9b-3b48-87d5-b84350164b0d | -5.76277 | -45.56253 | 2025-10-27 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1641f19a-2855-325a-804e-ed8da3f9aa59 | -11.9165 | -43.82312 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b385a153-00dc-304c-b3ef-e7a80c96c346 | -7.82881 | -46.44641 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6b393e0-831f-33b1-8139-0b6865e30395 | -7.83223 | -46.46133 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79a9df70-9ef8-388d-8263-765d13b131b7 | -8.95877 | -47.19397 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f6c1defb-714f-332a-a117-45d50b6daef5 | -10.95245 | -48.06577 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 792e0832-9ac9-30ca-b324-ac3fb5a74037 | -10.34108 | -47.22186 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36248a39-6e29-3ddb-a2cc-9aaacd8b450a | -7.30539 | -42.47691 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8fe7aa9f-147f-3f46-a057-5ed97760cd9a | -6.49426 | -42.21449 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8aed9f2d-69c1-3f43-af16-1a60e335a082 | -7.96496 | -45.47658 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00dd8531-15b4-3950-b8e7-643153948c97 | -7.96016 | -45.47099 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 854c8ce0-70b0-3b76-854f-7a648fb0b67b | -7.59823 | -45.68694 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 950b5994-dcf9-3d53-8d8c-c67b6a901e89 | -11.42444 | -46.11209 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1db0e586-9a50-3ec7-bcce-5da1627fc4dc | -10.34845 | -47.18463 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f20a6a9-de94-3f63-9026-1bce46a4df29 | -11.70889 | -44.44212 | 2025-10-27 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bed0bb7b-a7f9-3234-a1e5-010f330933b5 | -6.85054 | -40.16326 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 583799fc-9579-3b50-a29d-08f4ad17fda4 | -9.25159 | -45.5717 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 194a4c51-6d38-30ac-ae8f-7a46c2c2588f | -7.33248 | -44.02675 | 2025-10-27 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66cb9042-82e3-3346-991a-4e8cda806a79 | -7.92892 | -47.19537 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
