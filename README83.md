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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f23549b7-1073-341e-a52b-0b8084ecf7dc | -11.91717 | -46.37029 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4cae199-887f-30d4-9ce7-d55a10e979ca | -11.69422 | -47.50745 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 520763a8-79cb-301c-ba7f-580e8c1947f9 | -8.21871 | -46.80937 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5352d40-475b-37d1-9872-6fccc8a4a795 | -13.56142 | -44.09934 | 2025-10-04 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4cc250-daf9-359f-a6fb-4f6efd6d562b | -11.47309 | -45.03674 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1fe4bd0-3c3a-3340-8d51-0309809ddde2 | -8.22574 | -42.91688 | 2025-10-04 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a92131b1-3876-3afd-867d-65f3ad5b06d5 | -12.92823 | -45.07664 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1edc5c8f-0e1d-38ab-96f1-f2abab082702 | -13.73173 | -47.92973 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dad3bb07-4863-31b3-8fe7-a000856f3b09 | -12.51569 | -47.31688 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cddede8-ee22-3878-9b41-f6c80e47e71e | -13.26203 | -47.21677 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e9dd3e1-1ac2-3032-a9f0-b32097cd4e12 | -14.87548 | -48.37116 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 54cbc42f-c6e7-368a-8508-a47ff7323e95 | -10.02098 | -50.19598 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20e0d050-da89-3f7a-8706-f61ebdeff0d5 | -10.86347 | -45.40917 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6195edd1-6b36-3b94-9471-6c8839e7120b | -11.79307 | -47.91853 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58aeabef-c8db-3113-87df-4acd8292ef0c | -12.2977 | -45.36024 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15857d11-9d4f-3426-a007-a0af64d9b132 | -11.92719 | -46.35258 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77fe5285-bd8d-3bbb-97c8-ff45fb5d6315 | -13.11606 | -47.8414 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 51447f46-fb22-323a-a68b-9397c878c5e8 | -13.34307 | -48.07245 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1c146c-79a8-325e-a3e7-dad0aa95c2f1 | -11.55997 | -47.68133 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd18fe34-ee76-36e7-b037-fe12eb63bae4 | -11.92249 | -46.35958 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 53975bf6-5a08-32e6-8f0d-82d50704c0cf | -7.86207 | -48.20652 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49245c20-e38f-3087-bdad-4e5cef587556 | -11.45392 | -45.13988 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11de9e8b-0bc1-350a-912f-aff1e2c2b766 | -15.30248 | -46.30061 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79940894-56cc-38b9-99bc-b5f796b39d92 | -13.29832 | -46.42454 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81609b72-9daa-3b8a-82f7-65e65fe947b3 | -11.55925 | -47.68564 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df08bfda-b46d-38e7-9456-f549f917e296 | -13.16079 | -44.63913 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03f61ebf-3a53-3e4f-ba50-475c92845539 | -10.99496 | -46.67701 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e2b3cf-c93d-36b5-82d3-83c9d5297e3c | -7.73806 | -46.27001 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6a05836-b6ad-3c64-ac76-11d80c86a8c2 | -11.79668 | -48.91869 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27f6e87c-255a-361c-a10f-a509d50b864b | -13.30727 | -47.57373 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 377b0499-e8c0-36a2-bab4-f96739150f20 | -13.39225 | -47.28465 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28108f63-71eb-394a-9e97-59d043ec678b | -15.16019 | -44.07307 | 2025-10-04 04:14:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a9ea11d-d310-36d2-bb5a-fa3979af874d | -13.74524 | -47.98106 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e47f5b09-22d1-3188-a016-cc7354509c9e | -10.06586 | -48.18636 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5cbd7cd-06f8-33fb-96cd-cf75e4c2c8e7 | -14.38174 | -48.47318 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb3fed17-fc56-3aff-ac72-8d7a76913bd1 | -11.44855 | -44.96 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a3ca72a-7eeb-3df4-9e65-d568a25a8b03 | -11.8284 | -44.9207 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a97df0db-328b-3a63-8c6a-6f45d7c21221 | -14.28391 | -45.87688 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e809b691-5119-35e3-b8df-625d3786103f | -8.1094 | -55.0912 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efd51c96-1d7e-39b1-81ff-4a22ca9c7f63 | -13.56339 | -47.30127 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 451df506-b7be-3ef5-a324-444943b863b5 | -11.91526 | -46.38169 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bbc6340-3821-3271-88b8-b8c857119d01 | -12.6548 | -46.90023 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a6369ff-2957-38ea-b31c-f4e517ea93ae | -8.83732 | -44.79841 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4201d806-3d72-3130-86b1-40f8011d7257 | -11.80011 | -45.01426 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83855cd0-18c7-3203-aa67-556e5f1e98c1 | -11.47546 | -43.50007 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c023d88-1905-3b80-bab6-a2e9ef9fdd18 | -11.83998 | -44.9335 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 620b531d-2a93-3d48-8eb2-9125308119a7 | -14.89789 | -48.39352 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6c03624-7ec0-3021-bd50-a9a501440eff | -14.89861 | -48.28075 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cd48aca-7571-3a98-b275-9afe31038d18 | -9.66464 | -48.20682 | 2025-10-04 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78d07572-67b6-3cb1-b56b-f8fb85b78004 | -15.29421 | -46.28795 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e6edb2-3105-3821-a9ab-a85c12c1ff0d | -14.6663 | -48.2998 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 184e8168-6963-36c3-81f3-3ac4c7b097e7 | -12.09485 | -45.1687 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7e592e-037c-3482-977d-5df98d2176ec | -11.11841 | -44.89864 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 540096a4-20e1-3df4-864f-7ace6981104d | -8.01762 | -55.4251 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77601c01-759c-3c59-b430-60e6cd7229bf | -11.50978 | -46.74077 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b243edc8-30b2-36dc-aeea-4bd464eb7a5e | -10.01789 | -44.02373 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 142a0f40-667f-3fd8-ace3-d9bb30365428 | -11.08234 | -47.88972 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18f505a9-098d-3df3-9726-17de7172e650 | -15.21466 | -47.18864 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0da0a1e9-04ba-3fab-91fc-7c9312dd5a8b | -13.52331 | -47.30275 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eba359e-5980-313b-a757-23ff8fdfeed5 | -8.90409 | -49.70596 | 2025-10-04 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a014f966-2311-3634-985d-200e4bde6ed0 | -14.64929 | -48.31139 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 09643af5-cf66-3755-8bea-031f5da331e4 | -9.3408 | -45.78006 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aeb3a36-4060-3fe2-a8b3-cc639ec53170 | -12.04536 | -45.17872 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e3141ea-a6e7-3bcb-b6be-a570bf00c7af | -8.58528 | -44.79883 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e64dcbeb-2a7d-3674-82cb-0e665ab4f75d | -11.10116 | -49.80884 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37699b64-7f90-3cbe-beeb-248f926f3d40 | -13.75008 | -48.06183 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfa1d36d-afbf-3388-80c0-f0ada8130834 | -9.45552 | -56.65919 | 2025-10-04 04:14:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c47d4502-b05e-3c8a-bcb4-161d07a41f0b | -12.38622 | -47.56629 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66926855-d9b5-3c36-adad-6ccad2996934 | -11.8946 | -45.37455 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ccfc07d-28ef-3a41-b099-c6e7c6164331 | -8.84764 | -46.79174 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4559b07-6a73-340d-bfe7-7d01973c2fac | -9.33517 | -45.77127 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03d8ef86-811c-3931-8b67-4f47edf2a7f6 | -13.05027 | -48.62543 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b7a9031-f055-3679-9dd0-8c75eb868bba | -13.20316 | -47.79413 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e44492da-02e6-3b57-97c4-7c2fc20cdc96 | -11.56583 | -47.66889 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cbba498-9fa3-3f5d-b760-0b550196f68c | -7.72619 | -46.29748 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93f65ee7-7236-3007-af63-18c11e95de8f | -11.44557 | -43.4953 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed8d6227-6968-32ad-bf54-207c4c5b58b0 | -11.90836 | -46.38059 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f93f90e-6b0f-3996-b096-38a1321564f6 | -8.17463 | -47.00787 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c60e6c65-b60d-3480-ae8c-82d2754546ff | -11.91269 | -46.2521 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85c8a665-db0b-3ace-9662-2453e607474a | -12.59516 | -49.88601 | 2025-10-04 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5dc0405-af84-33c3-be4d-97f6211c8804 | -11.47813 | -45.02666 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1171a067-72d9-3e97-8e75-103e992bf798 | -13.98364 | -48.12225 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c61813-da92-3b57-9a78-ab9bf952ec98 | -14.30703 | -43.86237 | 2025-10-04 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42da4bb5-5a08-3487-b81a-e1e995fcde68 | -14.91627 | -46.89225 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4ecdddd-dfd3-3843-b8c8-b239db0ce2c1 | -11.91828 | -46.40604 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a06042a8-3cc4-3731-b1b9-f5b2adbb0907 | -10.02231 | -44.01728 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 073d19ec-7350-3d26-84f2-1c8283c2a2ab | -13.22719 | -47.8275 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d8264de-70fe-3d34-ae5a-6f9f3773a8d0 | -13.92966 | -48.17451 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44348df8-4b97-3cee-9109-93bbc395ae1e | -11.14109 | -47.20849 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78d84c11-00b1-380a-b632-a072b6ec775c | -8.46736 | -47.41953 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aeac7a72-c1ce-3f94-8f05-f36dbb824e7b | -11.91872 | -46.38219 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f05c71b2-99fa-3671-929b-5bc50af69e13 | -13.12108 | -47.94331 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1bf3948-e70c-3a81-9d92-ca9713d1c2f4 | -12.91916 | -54.72844 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b272fe4-9c5e-3a00-8b3f-d49e4e55cfd5 | -14.19834 | -46.0717 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cba741f8-a78d-31a3-a0c9-8694c0eff13e | -12.95723 | -42.42502 | 2025-10-04 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7fdd892c-e735-3081-afeb-976f13bb9b94 | -8.62049 | -54.99441 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0f062e3-9f80-36c3-872d-4775937ad9b6 | -8.84904 | -46.78337 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f23548f-03f6-347d-b8e7-10bb203b84cc | -12.94245 | -50.98822 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d4d2eb4-d490-314c-97ae-7901bc350a64 | -12.03409 | -45.20615 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| edf33ee2-6536-3247-b97e-3be68b8bfc5d | -13.32312 | -48.12325 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README84.md)
