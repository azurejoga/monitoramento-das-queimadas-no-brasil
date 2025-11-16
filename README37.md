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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcbd5563-610f-3be3-a469-5361712b9599 | -12.65967 | -47.16873 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d6b19db-dc9d-366c-9c7e-fed61aa09a8f | -9.85254 | -44.71311 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1b7b2fb-e564-3b5d-b2b0-78a131f7aeee | -6.85728 | -42.84607 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49dfb871-3551-3ff4-910f-8161e88d6171 | -12.04936 | -43.51053 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 262fa542-d71e-33b5-9d82-b1f676046957 | -7.25783 | -40.17212 | 2025-11-16 04:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3a1e2eb4-f5c0-327e-b6f4-bb317ed5f5d5 | -10.6209 | -44.59326 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c38be28-df24-359b-896e-e03aee28576f | -10.51082 | -44.83169 | 2025-11-16 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f23e89e-33a9-382f-bc0e-9a397b69c096 | -9.72511 | -48.88917 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d12eba2-1e27-3265-b658-11e59ff4bb15 | -6.28137 | -41.72311 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26ecb23e-1296-337f-8435-c81a71842686 | -6.95506 | -39.52493 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ca280a46-ec31-31d0-949d-e0499d02740b | -12.05721 | -48.2055 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 187089ef-019d-30f1-89a8-f6fc57fca51f | -5.28242 | -44.7398 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8be79b93-5a4c-3c56-989e-a0bfb5b9ba9a | -10.99048 | -47.73022 | 2025-11-16 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d197776c-1842-3037-8224-74848a27d8a6 | -11.35976 | -49.79794 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d35c4bda-d446-3981-92ee-1a646586ff4d | -8.20904 | -43.56494 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8280f3-a842-3cdf-be13-cca468c72c1b | -7.04483 | -45.92618 | 2025-11-16 04:08:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fca88ad-4b0e-335d-a3e1-160fe2b5c492 | -11.71852 | -48.8722 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c04493da-0ae7-3b6a-9833-c4c3d667aac4 | -8.74065 | -48.31513 | 2025-11-16 04:08:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2228f069-971c-313d-a0e0-20188dc70f35 | -6.70985 | -42.12826 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5427d455-81be-3ee0-96fe-15fd9384f898 | -10.31543 | -44.5903 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8f260f9-d41c-32e8-96c0-9ece6ddd9b23 | -11.96939 | -44.95123 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76f0a2d0-f310-3942-b3ba-fc037d86b47b | -6.25502 | -41.41837 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57698192-247b-3fe6-9c82-4207820f9eb7 | -6.46007 | -42.33094 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0dc55c47-1890-3d3e-88ef-cfdb3f4ae4e4 | -10.93915 | -44.02273 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfd6ea59-6d51-3681-9821-031381cac1bb | -8.30697 | -43.80402 | 2025-11-16 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38a1be07-8581-32fb-bd2e-7a5237915740 | -12.00296 | -49.28304 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 3e1e3b57-bb0f-35e6-b74d-58a89fbce742 | -11.70716 | -48.86136 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2c07909-c016-357d-b7de-8fc28eb149f6 | -6.29999 | -41.84236 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 76f69822-fd45-390b-b141-b78dfe0b007a | -7.19619 | -39.20764 | 2025-11-16 04:08:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82b18ea1-9be1-3f06-8e0a-32194bee1db9 | -11.41827 | -43.33407 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9367d042-4add-3fac-8135-aa7ce9715f24 | -6.09227 | -41.6078 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 642dcfef-85e3-3f8e-b987-ad19f140f83c | -6.30825 | -41.83303 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3915c3d8-c961-35a9-ac78-f5b5d5406dd2 | -6.74278 | -48.19204 | 2025-11-16 04:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24e84d97-267c-3a22-b05f-053c3a398ecb | -8.49961 | -45.4858 | 2025-11-16 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c93d131-3b45-353c-8ab5-78bbb9157577 | -6.44862 | -47.28068 | 2025-11-16 04:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9050af-a83d-34fd-afb4-04a7f3e61559 | -7.13019 | -41.66319 | 2025-11-16 04:08:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 34b1d40d-93c8-3c49-9cb5-2515c08e1485 | -7.44016 | -45.22718 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ec41359-6760-39e0-aebd-c0f8e544f49d | -9.35031 | -46.59801 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 70ab0790-d64c-3103-9431-29115815830a | -10.99452 | -47.7309 | 2025-11-16 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07deebbe-89e5-3661-a079-0d7591935ab8 | -9.73993 | -43.96626 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7e1f9f81-b3fb-358d-95be-56863aa92cd6 | -10.663 | -49.36958 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f499053-d689-34ff-be92-f20d5acad4a2 | -9.11258 | -40.45995 | 2025-11-16 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5cb3bf0-b163-343d-9367-3c929af7d217 | -5.53809 | -49.59721 | 2025-11-16 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5467450-4664-3cbb-bc19-f2f26d75e6ec | -7.04798 | -42.24647 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74676a76-229e-3c51-8a95-639c4b71c2ae | -12.2246 | -49.63639 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 257d7209-2db8-39e1-82ae-75c9cd7ff2a5 | -9.34125 | -46.58147 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e3a9ce-774e-3df1-990c-4bcea988f83d | -10.91895 | -44.84556 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c239f74-4ba6-3bb0-8fe9-f7665825aede | -6.5073 | -47.63037 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ceb9904-5f7e-36b4-b6f9-e6d85e8a1512 | -6.26272 | -41.41251 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32130064-a628-363b-8db6-44197ba874a4 | -10.62668 | -44.59672 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ae0919-026d-3a12-b728-5396c654fb0c | -6.07694 | -41.662 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 061f5951-9d87-395e-9d4a-769fc39c072c | -9.83177 | -47.07836 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d7e308e-7ddf-36d1-aa45-52aab58bc10e | -11.85262 | -44.72134 | 2025-11-16 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 099c58b9-24fd-3567-8e7a-d1e87a3fe201 | -6.71316 | -42.12879 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 641017b5-f03b-3050-b2c8-20ce9ff2b696 | -9.7175 | -48.90622 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b81d943-0371-3568-a161-b69134a688b2 | -11.71127 | -37.64825 | 2025-11-16 04:08:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 269790d9-6155-3d64-a7c2-572b30f6aadd | -11.97437 | -44.96408 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f5b12e19-7f50-35c1-aa7c-0d91cc78822f | -9.10919 | -40.45941 | 2025-11-16 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0be7588-3ec5-37c8-b89d-347ad4c01f82 | -12.39485 | -48.09201 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 578b6582-a0e9-3c09-a2f9-d5eef7b734e4 | -9.7417 | -43.95523 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f24f9eda-a05c-33dc-9714-6a02e019fec3 | -12.38078 | -48.10104 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9176b5cd-2876-3b0c-9670-ec9bc50de25c | -11.70497 | -48.87369 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0bc675c-91c4-3f4f-85e7-96208e74dd67 | -6.07196 | -42.86837 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b554f015-941f-37e1-be4a-5d2a5f24820c | -6.36209 | -46.15448 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45f14e0c-cf50-33cc-ab12-36c1d253816f | -6.38067 | -42.31845 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf8f1328-8831-3a43-ba9d-9fccd198a3e4 | -10.53853 | -47.99512 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14f9c098-d9d8-384d-8487-15ec0b84035d | -11.70652 | -48.39646 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70beb8e9-c564-32cd-8924-6ba2de29290e | -10.77057 | -43.97643 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c342837a-18d6-3a98-bb31-ba87ed5a9285 | -10.62042 | -44.59189 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f01cfb1-3146-31e5-b662-05e1e7efe991 | -5.99015 | -41.91047 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ae066df-a951-3f94-9038-42890aafc5d3 | -6.07688 | -41.61951 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be54e449-6e75-33f6-bc1c-3ab9107319dd | -9.15988 | -37.91392 | 2025-11-16 04:08:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e7d4a9a2-1481-3bbd-b89e-af9c3b65089b | -7.97175 | -38.63797 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb13c461-b8a2-338e-a610-296dc41eb8e7 | -7.09585 | -42.73558 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b06f9e8c-a343-3211-80aa-962594222059 | -7.29482 | -45.10802 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fac7c38-6d45-3464-a6ce-b9ca7691ab6d | -8.20786 | -43.57222 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53c830c0-c4c8-3052-bdf9-41cc12a129b2 | -10.54569 | -47.92988 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8061cae8-5db9-3dc0-bfc2-c574d2bb2036 | -9.15894 | -37.91157 | 2025-11-16 04:08:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f05f1dd-d236-3963-9e50-59a14e7a5860 | -5.63948 | -47.74437 | 2025-11-16 04:08:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d4621bb-e2fe-39ed-9ff1-7322f65d8a1c | -5.36329 | -44.90746 | 2025-11-16 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 751f3183-dc77-3e23-b6af-ddfe4c8da5e9 | -10.16515 | -44.50347 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a70483f0-d3d7-3a07-abc6-6f8fcb181551 | -11.05401 | -45.16121 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5ce8c75-fc96-3f68-b1c3-32974f7a8720 | -12.39766 | -48.09975 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 686da7ae-a007-3038-abb8-fec1b4a644e6 | -9.65968 | -43.90378 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eb728854-674c-31f0-8b7d-e81582706c0c | -12.6562 | -46.743 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 014c7f24-936b-34ca-8f94-450598f700ec | -6.20871 | -44.64529 | 2025-11-16 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdb8cfd9-87b7-3649-acf8-d422e2a7e5f9 | -9.50167 | -47.27132 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbb76066-d3c4-362f-bce0-addb5f943ea8 | -12.39933 | -47.55636 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac1e7227-0255-366e-9285-f1f71d424f7b | -8.5733 | -46.0507 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d21c469-b539-3922-85c1-babb75b36f7a | -7.84668 | -47.17776 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62fc8654-a0a4-3850-8583-0a4670aff6ef | -6.71592 | -42.13279 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70ae89ed-9c7c-3fd4-bcb7-37262794f8b7 | -6.59054 | -42.89573 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090087aa-b677-3085-86d7-0775d55d2c0f | -6.54473 | -42.20509 | 2025-11-16 04:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c65fc0be-7efc-3ad6-b736-d7cbbfe31b09 | -6.10218 | -46.72947 | 2025-11-16 04:08:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89285220-5ac5-3cff-8b45-a54d5ca3e39d | -6.54418 | -42.20858 | 2025-11-16 04:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 762543ba-4e38-3a5e-b21a-3dba309111b7 | -7.05074 | -42.22907 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b9e31d9-d721-3bd2-8d3e-76f1236f9231 | -6.93009 | -39.61792 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96cef545-d8e6-3ddf-bc6b-f6cf2d1d8a0a | -11.05336 | -45.1652 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f660d0d-d1b1-3515-b9d4-318b7b96f2e7 | -6.07538 | -42.99839 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74645f6a-415a-3c90-bcdb-af8fc8e3872d | -7.37113 | -43.32277 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README38.md)
