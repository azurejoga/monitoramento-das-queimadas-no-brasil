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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92922120-2614-3562-ba24-2045d96a5b99 | -2.59643 | -48.12144 | 2025-10-06 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 599a6208-602b-3920-a9f4-e8f54fc30eb9 | -5.61945 | -45.4063 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 929c3638-a9ed-3a7c-981a-f22e679affdd | -7.88049 | -44.12991 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2bde323-e0f8-3598-894a-ad8b3287aec1 | -7.48162 | -42.62112 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86e35b87-4b34-3673-bfe7-9b25c614e0c4 | -5.64712 | -46.38219 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7db56295-493a-31e8-aaa9-8e82496bbca3 | -4.56919 | -48.60469 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98f4dcd9-74ff-37ac-b1c4-08fe43f0b28f | -6.30754 | -44.46227 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1bf595a2-5799-3eb0-a965-c2ccbec5ddad | -4.82241 | -42.86776 | 2025-10-06 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a2ed9977-11b5-3c2a-a1f7-906bf08668d4 | -8.5158 | -46.3596 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4a939de-c9da-3dd6-9380-0e1a7f506088 | -8.61738 | -46.27636 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d92f1209-d715-33f4-ac52-1eca75bb1ffa | -6.3549 | -43.91983 | 2025-10-06 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a49f7819-bb08-37b4-a269-8bda1656b591 | -8.9634 | -44.61494 | 2025-10-06 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3319d0b7-1eda-3a84-ae58-3a9b53762f15 | -3.78139 | -51.87225 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f26e7072-1230-3404-8a64-1b695e8e6477 | -6.40899 | -43.80923 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 354e6959-5d72-36ac-ad9a-015b5aad04bc | -6.60141 | -43.72852 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a35a9fb8-6e79-303a-8116-558342079569 | -5.23782 | -43.74346 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e15de36-bf27-3900-b31b-79a4cc1d35a7 | -6.61945 | -41.97887 | 2025-10-06 04:25:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22a720f3-99aa-3b9e-b16d-80929ca8b6b8 | -7.35768 | -47.25774 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb06ad03-e053-391f-a0bc-6ede85a233d6 | -8.25459 | -47.0099 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2475a22b-247f-3b3c-b021-cc5615ec707d | -8.18889 | -46.99252 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04680898-6e22-34fe-b2a5-203e5435e077 | -5.23123 | -49.07261 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 603c1e91-fb4b-3dbf-a28f-34ac3867643f | -6.08789 | -43.9897 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa21f44-6c79-3208-b084-b44344dc6241 | -8.19245 | -44.19911 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d24dfa0d-8fcf-33ae-9d42-a6b2306451e9 | -8.31472 | -49.72976 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd62462c-8a5f-3599-a02c-e2e056e3ba7f | -8.6318 | -46.31422 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| af0b335c-2915-3f93-916e-5d022bb98a8c | -2.59291 | -48.12091 | 2025-10-06 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 83599dd1-5533-3df4-9d68-0b4abee4e51f | -6.34403 | -41.63946 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cff656d2-d738-34f8-be3e-df19330d4e72 | -5.59974 | -45.70813 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 818ebb5f-9d7e-3cfa-976e-c0d2b9006146 | -6.09308 | -43.42545 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b680a8e9-aa96-31b0-ab09-d786a3fb3d55 | -7.41488 | -46.52872 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2adb8ca-f24f-3d96-8df8-ae810848225e | -5.80486 | -45.81124 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3881141-cd8e-365a-b224-9acb656e0c51 | -8.93044 | -46.60706 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a20e6212-03cf-3d4f-a6f7-c44355082f84 | -7.01952 | -42.78907 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d9840220-6304-3528-af72-1f1c8dc0a00d | -8.68487 | -49.47067 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e6f266-06ee-31f5-bade-0a872988edc5 | -7.79006 | -42.6039 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cfcc7d48-dcc9-3c23-a65b-83c56dc46cb0 | -8.86636 | -46.79582 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b298336-54c8-374c-b446-1cdf551237b9 | -8.19699 | -44.17915 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6daa2c5a-79a9-36ce-bbdf-292a28a9fc0a | -6.06708 | -42.55023 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c9f50354-9bfe-3a44-8e8d-64183807739e | -8.61636 | -46.30467 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 593c43b0-b4df-3d6d-b81e-17063b60da41 | -7.46579 | -43.03714 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a912899c-593c-3888-bdc8-db7b9e7cfa8c | -4.31314 | -48.23845 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 426e020b-64bf-3139-a49e-40c1a50b75e0 | -7.36036 | -45.23341 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ac0d2c-8c19-342f-9a91-be8557189121 | -9.31748 | -45.99498 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acaa3287-c046-3019-84e6-3a2463ac9330 | -6.69538 | -42.17277 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f80ea9e3-98b8-320f-a3b6-a8591108edb6 | -5.808 | -45.48242 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d59b0202-8a7b-36d8-8172-912d89f09453 | -8.63624 | -47.26676 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 010f0e86-838a-33f5-b354-8f58c42a029a | -6.22524 | -45.77817 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f15d9fe7-6b2d-3eb6-bf4f-1eca79eff837 | -5.69873 | -44.82874 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a442deb4-1778-32cb-a058-99fb2d090fdd | -7.80471 | -42.58256 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 61ba1e62-a78f-3ea2-8d8b-e90bc71a7186 | -9.30934 | -45.66917 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 691b8e80-9d88-3027-a22e-ca3cb3e6f865 | -8.5672 | -46.25069 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 001de1a4-7d78-3b14-b7d6-4047d3b2362d | -7.27254 | -49.31037 | 2025-10-06 04:25:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76378c02-c7af-318a-bf40-a706f1ea0176 | -6.45332 | -43.43958 | 2025-10-06 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e437f3ec-48be-3ff7-a814-cdcb06e83d1c | -4.94657 | -44.58924 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c54fc9cf-3ae6-35d1-b295-fed941d5612f | -7.42099 | -41.134 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 707ba444-7e8a-31a2-b49f-f94e2ac495dd | -8.56295 | -47.25512 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f22ce9c6-0343-3f46-b564-3d9ac3d52242 | -5.99508 | -44.25296 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 47b50700-239d-33b7-a82c-c207c29a11e3 | -5.70208 | -44.82924 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a42ef972-4378-318a-9526-112e8b3809c0 | -8.65321 | -47.15911 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcbf326c-c477-345a-a716-20ccabbbdeaa | -8.61798 | -46.29424 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8cb952c-24fe-3b39-9e8f-9af83aa0b69f | -7.71932 | -46.25508 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56ce166c-3e1e-3c00-afec-d34d054e6272 | -5.8947 | -38.48862 | 2025-10-06 04:25:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c63d24d9-8194-39d2-a133-fcbc3252c7f7 | -5.70488 | -44.83331 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c11a5681-036c-34c3-86e3-74501ce08641 | -9.3147 | -45.99091 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74455342-2d32-326e-bfd9-23101740a24e | -4.56972 | -48.60472 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e53ebc3-1579-36b8-a215-8472b9f7339d | -9.31972 | -46.00255 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7a032da-20f2-320a-8bf6-9c76a916ac1c | -8.67749 | -49.46564 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bf59aaf-86d1-3b7f-9d99-dea7b91a0e82 | -3.74077 | -52.3758 | 2025-10-06 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d519cfd-2328-3f63-bb9f-d503b361a14f | -4.65401 | -43.19111 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bb802da-35ab-3cd3-9fc6-826710b5b336 | -4.74551 | -44.4374 | 2025-10-06 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93a0c9be-1133-3f95-9615-d2c17fbd919d | -8.18659 | -44.2142 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 804f7823-552d-31bb-82d7-9a027e79268a | -4.56567 | -48.60412 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39efd500-792a-3a57-b232-3d7d48187bf6 | -4.84909 | -45.45974 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08a67a02-5e42-3d34-9bd8-c0f78eab21b0 | -8.56666 | -46.25417 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c59c533a-3194-3568-a0dc-7c13d3315e0b | -7.42259 | -41.12301 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c66da4b5-904e-3e7c-9d9a-c57fa7edeafd | -4.36389 | -50.85904 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22f6ef0d-94a5-380f-a92e-65994b5ec3f9 | -6.59089 | -43.72685 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 842d9ec3-5e40-3d65-9a13-b9aedc83d21b | -6.56312 | -44.16505 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e7ca4e9-048e-32f9-9af8-4c76c9ce8092 | -8.17251 | -44.25991 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7818abef-e40b-3e81-b45b-c161cf5fac25 | -5.18338 | -46.21673 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd53bf3-35bb-3da4-af57-e4687afa3077 | -5.70267 | -44.84752 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dc8ac5b-3c9d-3291-b333-ac2681817fad | -7.68678 | -47.52269 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8b62854-c2be-3935-b439-12f18f8f8434 | -7.46968 | -42.62402 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f82568f-7a02-3a13-b70b-ae8815b25539 | -5.64248 | -45.9588 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 90c30344-28d7-3430-8c2b-62cddc4d0832 | -7.41872 | -46.52579 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d540f0a-6b9d-3d16-80fd-5e5bea02b8d5 | -6.69289 | -41.39178 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5d95dfe-633a-3fe2-b7c5-2ac5f9f73d7b | -8.62742 | -46.32064 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b945ca97-38ac-3b16-b1f9-9bf0a42f88e4 | -5.27848 | -42.91919 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f51670a9-6d7d-3819-acf5-00ad99c83f20 | -7.41812 | -46.50801 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b6137fe-c9a4-38c4-ba53-01b219d04158 | -7.24954 | -42.98128 | 2025-10-06 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f93b7bdb-62cc-3c76-aff9-699210bf3220 | -6.82398 | -45.97193 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 137579db-288c-34d2-a5f4-f09d7aa06182 | -9.25462 | -44.26646 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e1cafdb-6058-30f4-a0ca-f6267b1fd4cb | -7.53456 | -43.85793 | 2025-10-06 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ffc247f-da73-3b53-a03e-2dc3b33751f8 | -4.9254 | -47.31071 | 2025-10-06 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d17402a-a61d-3a0a-87da-35ad20794541 | -7.62638 | -45.47089 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2be9e7dd-f582-3c62-bb2e-1035e87eab14 | -6.56261 | -44.14544 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa321e02-6916-33ae-b032-f769c383eb35 | -5.79175 | -45.83039 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b7b5a37-6e79-3c54-ad7c-4e881665d853 | -5.49638 | -44.92479 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a94129f2-7215-3c99-bde1-43516e2626a1 | -6.75566 | -42.2386 | 2025-10-06 04:25:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f0f4734b-574d-3941-9e67-6ab914d31650 | -5.22971 | -43.7032 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README33.md)
