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
| 1be59256-65f7-3982-94fb-e3c612c8a699 | -20.9601 | -56.5967 | 2025-05-18 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 33394544-1e84-3b03-b04a-3cc6d72fb568 | -20.9597 | -56.6179 | 2025-05-18 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c72c48d5-23fc-3605-98f0-e806aea3c8ef | -20.9398 | -56.5998 | 2025-05-18 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 23b6568b-88e0-38b3-b2ca-da000509d883 | -20.9393 | -56.621 | 2025-05-18 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 628241aa-a445-3ae1-8d47-f493606890ed | -20.9597 | -56.6179 | 2025-05-18 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 43c3f68f-8add-329c-9b9e-aa58ecc7262e | -20.9601 | -56.5967 | 2025-05-18 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 146.3 |
| e0ac7d28-e74a-3189-b6ac-688909d2cc13 | -10.4967 | -46.505001 | 2025-05-18 00:10:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2273371b-3814-3d0e-a308-44fe20b2b79a | -17.1474 | -44.793701 | 2025-05-18 00:10:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 016dbd7c-db17-3e7f-9557-fa2a3474d6b4 | -20.935101 | -44.394699 | 2025-05-18 00:10:00 | METOP-B | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd5350ae-a490-3074-b634-e8d0ab76c373 | -11.5775 | -47.599899 | 2025-05-18 00:10:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee8fb648-a552-37b4-b5eb-d4a3995d346b | -13.303 | -45.3713 | 2025-05-18 00:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac960d5-fcd5-3238-a3a4-b83496e8e740 | -12.5969 | -45.436501 | 2025-05-18 00:10:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8da068b-e579-3830-b553-ffd1d41eb32a | -6.6396 | -41.978802 | 2025-05-18 00:10:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16dfe4f5-1c5d-381c-9e26-4a35d0d78a5f | -11.4209 | -54.2715 | 2025-05-18 00:10:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91a4684-b3b1-3ff7-9e45-efb61ea84e20 | -10.4801 | -49.136902 | 2025-05-18 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36b8bcda-23a9-3c32-aff9-2e4973bfbf3d | -11.4873 | -43.800098 | 2025-05-18 00:10:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1fc7e8e-08e3-3e35-a3b0-0b07e0b3862f | -12.0305 | -54.928001 | 2025-05-18 00:10:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3ec6a1-541e-3bbf-a4fb-1618eba4a353 | -8.1162 | -46.445999 | 2025-05-18 00:10:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c67c72fc-326c-39be-8161-4dd1fa230962 | -10.3429 | -46.694401 | 2025-05-18 00:10:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ba09132-db8e-3c87-b5e4-b3160edaaaca | -13.5653 | -43.5042 | 2025-05-18 00:10:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6187ac66-ddd9-37d9-a61c-b12cf6a0d763 | -17.391399 | -46.632301 | 2025-05-18 00:10:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b3883c5-aacd-3d5e-b132-a2d7f5774aae | -10.3445 | -46.701401 | 2025-05-18 00:10:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c271571b-d2b4-35aa-8588-82827b0b59f9 | -8.0104 | -46.802898 | 2025-05-18 00:10:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc8a3604-61a8-39dc-a682-d2c403efb46e | -12.1039 | -44.748402 | 2025-05-18 00:10:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d62f081-f599-3057-8fe2-41766bfb0e96 | -6.6442 | -41.998501 | 2025-05-18 00:10:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5c156c6-5441-38c4-8b76-1d99086944ba | -10.4783 | -49.1283 | 2025-05-18 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 342b6f97-9ae4-3519-9dfc-80ae8db8827a | -13.8916 | -43.442299 | 2025-05-18 00:10:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 251cb95e-4f7c-39a3-a345-f7bfdf92f2c2 | -12.1023 | -44.741402 | 2025-05-18 00:10:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6c0dce3-6f62-3093-80a0-458678feca3b | -17.149 | -44.8009 | 2025-05-18 00:10:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 007b968b-5a96-375e-804d-29eab4ed2647 | -11.5617 | -47.861198 | 2025-05-18 00:10:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ead7050a-e496-3b24-98a6-6bedb820fdab | -6.6516 | -41.986301 | 2025-05-18 00:10:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30e88744-2438-3098-8506-c1c615679781 | -6.6419 | -41.988602 | 2025-05-18 00:10:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a80e0fa1-cd5a-3576-a44c-9e86a071f586 | -7.079 | -44.9072 | 2025-05-18 00:10:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa54224-1cb8-3b74-b611-efcfbee7d476 | -11.5791 | -47.607601 | 2025-05-18 00:10:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d82f213c-f71a-306f-b635-1d541633b249 | -7.0714 | -44.376701 | 2025-05-18 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11dc6788-6b28-39e2-8672-6f5f44c1d2d1 | -10.3346 | -46.703602 | 2025-05-18 00:10:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| add7a16f-db49-39f8-a21e-9d3d08e784c6 | -8.1147 | -46.439098 | 2025-05-18 00:10:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 364e6426-8527-35cd-bb2a-d420633eada2 | -8.0089 | -46.796001 | 2025-05-18 00:10:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 809a3b4a-7477-311e-bee8-06eb9e677191 | -7.0806 | -44.914398 | 2025-05-18 00:10:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 866e5c83-d877-3798-a025-17c375510e6b | -10.346 | -46.7085 | 2025-05-18 00:10:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 642ed338-d069-310d-87ea-b1ddd60a9dc8 | -6.4953 | -47.488201 | 2025-05-18 00:10:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 090804ed-bb83-316d-9f6e-8afb721530a9 | -12.169 | -48.793499 | 2025-05-18 00:10:00 | METOP-B | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63920c28-2482-393c-8417-c151360560c7 | -11.7961 | -49.310699 | 2025-05-18 00:10:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ebe17a-006e-37a1-876d-6df27ef32e7b | -17.150499 | -44.808102 | 2025-05-18 00:10:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 42020b3a-0e01-3758-b9a5-c98b083ffdcf | -20.93249 | -44.40565 | 2025-05-18 00:11:00 | TERRA_M-M | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 6a0c69e5-4fb9-3997-8a89-34d2f554273b | -13.30128 | -45.37924 | 2025-05-18 00:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 523f2da6-496b-3cf1-a920-1e95dfe8cb0e | -17.1448 | -44.81478 | 2025-05-18 00:13:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2dfa5fef-2bb3-3ced-a946-f75655900d18 | -13.89663 | -43.45321 | 2025-05-18 00:13:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 54ae735b-ede8-3442-a8b1-89d88abe2e1c | -11.58484 | -47.62294 | 2025-05-18 00:16:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 535c27a5-aa4c-30d1-9cb0-aded460e23cf | -10.3404 | -46.71185 | 2025-05-18 00:16:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| ef3e63b3-ee53-370a-86fd-cc9059a32c92 | -12.1025 | -44.7482 | 2025-05-18 00:16:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf9f0702-87af-3549-a7b3-f4fc72e7dd58 | -12.10405 | -44.76075 | 2025-05-18 00:16:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b9bf4073-f5f3-3123-a798-a447d0e70949 | -10.4994 | -46.51578 | 2025-05-18 00:16:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 94a12274-9c5c-3b39-ae35-f1c3b82531cf | -11.58241 | -47.60275 | 2025-05-18 00:16:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6bf86625-f306-3dbf-8694-d8e311954fdc | -7.07379 | -44.91739 | 2025-05-18 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 361fe039-f16b-3bb0-b0d4-be09178ac577 | -6.5024 | -47.5015 | 2025-05-18 00:18:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c91b22ac-73b9-38a7-8677-2176d373a85a | -8.12016 | -46.44668 | 2025-05-18 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2b5abf0d-e9ec-3038-b547-7b38613ab5f2 | -6.6481 | -41.98824 | 2025-05-18 00:18:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 60ac7282-ca4c-3e6c-a5a3-729801cd819b | -6.64051 | -41.99832 | 2025-05-18 00:18:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 22c5c3f2-3645-3e7f-a29f-b532467e02d0 | -6.64932 | -41.99706 | 2025-05-18 00:18:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| 15aedb02-6a37-3366-a16a-c28aba6ecb66 | -8.00557 | -46.80309 | 2025-05-18 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e5749ce5-dcd7-3888-8e10-c8ed65b3fdfc | -7.07641 | -44.3867 | 2025-05-18 00:18:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c302af2d-22b2-369d-99b1-2cf47007848d | -20.9393 | -56.621 | 2025-05-18 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3663eb0a-f554-395d-bf7b-c76dad44497c | -20.9597 | -56.6179 | 2025-05-18 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 85.4 |
| da09d6cc-1a61-32fb-a8b9-48b8b6900fa9 | -20.9601 | -56.5967 | 2025-05-18 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a656da1c-7b70-3f51-86d3-15d2ad140538 | -20.9398 | -56.5998 | 2025-05-18 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ac092c62-e6c3-3ed4-bb8d-e213595f6c91 | -20.9601 | -56.5967 | 2025-05-18 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 631d4b0f-7eab-38c0-896f-694146030db7 | -20.9597 | -56.6179 | 2025-05-18 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a47ec567-7774-3ede-b2bb-8cf9c48c0988 | -20.9601 | -56.5967 | 2025-05-18 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3e0b326c-bda4-3f8c-bbd3-6b878ef9472c | -20.9597 | -56.6179 | 2025-05-18 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e9eea65b-3092-3b79-8493-86df96889d4c | -20.9398 | -56.5998 | 2025-05-18 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e5451685-d45b-321e-be71-4b3fe6315af0 | -20.9601 | -56.5967 | 2025-05-18 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 2b62318f-a59c-3820-b3c5-fe19f7ce9da7 | -20.9597 | -56.6179 | 2025-05-18 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 23aeb663-b709-3588-9b09-48fb063cd1d6 | -20.9597 | -56.6179 | 2025-05-18 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ae46edf1-c40a-3fa8-9b64-bb71af7f99ca | -20.9601 | -56.5967 | 2025-05-18 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d7c95f57-6b96-3b63-a32f-62e719a33fed | -20.9601 | -56.5967 | 2025-05-18 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 781f4a12-b58c-312a-8e9c-e32ddb08ecc7 | -20.9597 | -56.6179 | 2025-05-18 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5339a972-7489-3feb-b348-159a41163171 | -20.9601 | -56.5967 | 2025-05-18 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1f93d2c7-3dd3-3a5e-bac0-ce46ad6a61b3 | -20.9597 | -56.6179 | 2025-05-18 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0783bff0-b111-3cbc-a904-b59a0572b805 | -20.9601 | -56.5967 | 2025-05-18 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| be48d98f-c65d-3604-978a-171287bff059 | -20.9597 | -56.6179 | 2025-05-18 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d7c32587-0004-3049-aedc-cbe9e668c245 | -20.9597 | -56.6179 | 2025-05-18 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 20b7bd82-119a-3b9a-941b-5b265d073229 | -20.9601 | -56.5967 | 2025-05-18 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b559c6ee-3231-3662-8640-4ceecdc0ed6e | -20.94414 | -56.60227 | 2025-05-18 01:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 248ace8a-b2f0-3e0f-a849-9514fc6a16bc | -20.95833 | -56.61538 | 2025-05-18 01:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ee9659a9-ac6d-337c-9b4c-922945e6038e | -20.95424 | -56.59324 | 2025-05-18 01:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 44.3 |
| a93d5dbe-215c-30ca-8a96-d52a1ea0e652 | -20.9601 | -56.5967 | 2025-05-18 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b4538e6b-e7dd-3f2f-9ef8-c41435d97f80 | -20.944201 | -56.625 | 2025-05-18 01:50:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fc8dd690-256e-3e1c-881a-a6b1adc79045 | -20.935801 | -56.596298 | 2025-05-18 01:50:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9928d92-dfab-317a-b9b3-88d81458d7b9 | -20.953699 | -56.621799 | 2025-05-18 01:50:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6c334353-a89b-3d2f-b394-8885ab59ef31 | -20.945299 | -56.593102 | 2025-05-18 01:50:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a1887518-96d9-3759-b420-1d8b5e1a517c | -10.0541 | -64.997 | 2025-05-18 01:54:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 60a12306-4da2-3241-8dc2-08041a590388 | -20.9601 | -56.5967 | 2025-05-18 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 68e084d9-ea7a-3e29-a488-b941666782d5 | -20.9601 | -56.5967 | 2025-05-18 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f940860d-714b-35f2-83df-c3cccea48a42 | -20.9601 | -56.5967 | 2025-05-18 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 54.5 |
| b58ed576-0674-36c8-933b-28941dcf9b13 | -20.9601 | -56.5967 | 2025-05-18 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2e207fba-e1c8-369a-af2b-424414fdf9b8 | -20.9601 | -56.5967 | 2025-05-18 03:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9bf9c87d-b82e-3f03-bc34-731bd6a9e32e | -7.07455 | -44.91793 | 2025-05-18 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4895a3f-b2c5-3ec9-844e-acef9c270a2f | -11.4836 | -43.80558 | 2025-05-18 03:30:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9e0babd-4336-323b-ac4c-790c5ba36531 | -7.07483 | -44.38324 | 2025-05-18 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README2.md)
