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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34090df3-b0a7-3822-97a5-e8a79708f095 | -11.69009 | -43.66323 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 383a768d-4563-3f03-882c-db3d3db40f5e | -11.28815 | -45.51741 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 17eb137a-1f45-323d-9798-524a3243cca6 | -11.69019 | -43.65258 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51a97255-0e48-309e-90e5-353117404ef7 | -9.95564 | -43.47511 | 2026-10-06 04:40:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a323e62-1dd8-3bc3-8383-94d9874cb6a2 | -6.85417 | -41.80049 | 2026-10-06 04:40:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cbee5077-955f-390e-93c7-e4d453c78234 | -9.82167 | -44.79457 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 836920e1-42eb-3cf7-bc68-6f63abdb76b4 | -11.66322 | -43.63266 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f7dcc5f-3cf6-3750-bcd1-f42f57f6fb72 | -6.6044 | -41.54791 | 2026-10-06 04:40:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07227b40-8e2e-38bc-a074-de0d8e20d344 | -11.28881 | -45.51295 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 63448115-d5b3-3279-aa5e-69cf151aacd7 | -9.15338 | -49.81645 | 2026-10-06 04:40:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 175b5784-0eba-3f2a-9622-bc367fda7ad8 | -9.9234 | -48.13906 | 2026-10-06 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 474c26c2-7f60-3d90-b326-5e66a5a236d3 | -5.6792 | -53.49191 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bebb3e5-c123-3c27-bc2c-54033fd59e1b | -6.45092 | -55.44045 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f81cce5-a0e7-3826-9ed2-b5aa087d5c3b | -7.74953 | -49.20771 | 2026-10-06 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dfb510c-36a1-30ae-81cb-8c87761435cf | -8.69936 | -45.22331 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1800f98-95f8-368e-99bf-2b17d4b442fa | -7.45071 | -46.83534 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4798cddb-ce35-3966-a0a1-1708aba2535e | -13.58011 | -44.42549 | 2026-10-06 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c14ddb20-d7bc-3f23-9809-0749aeb86f14 | -6.89732 | -43.67001 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e35a07-8b1b-3316-acf0-c97d4a5055b7 | -6.61769 | -41.57033 | 2026-10-06 04:40:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 37839aa4-5cfb-303a-bbaf-239801f087b7 | -8.90814 | -43.88374 | 2026-10-06 04:40:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df90988f-a4d1-3e52-a1cd-82004c6cfcde | -9.82855 | -44.80042 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4e06474-5444-3bab-bb89-24ee2995b01b | -7.25816 | -48.06953 | 2026-10-06 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d4bd047-07be-3aa4-9bb2-9cabf80fdd6a | -11.69165 | -43.67213 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbcbd07f-7c6d-3be0-892d-9462f5137154 | -6.45633 | -55.42846 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40325532-58ac-363c-b429-0c76122b91df | -5.82072 | -53.81319 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 286739af-827d-3af2-a4fc-aa2869146a68 | -11.27641 | -45.52021 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b2e2c13f-ffa2-34ac-ac25-db0201b2fee4 | -9.13962 | -47.98209 | 2026-10-06 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00eb09ef-a3df-34eb-b460-5fe81a863463 | -9.26227 | -45.65992 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8444bb3d-653f-3614-8e18-9dcf6693bce2 | -11.71405 | -43.42347 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f64afdc-bce0-3382-aaa6-fe3816ce76c8 | -4.4451 | -54.97341 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f10bf5e6-13d1-3d00-b8a7-171b19ba24c9 | -6.72092 | -47.79249 | 2026-10-06 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e067dfc2-8039-3a03-98cc-ea36773d4c0a | -6.45854 | -55.45235 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7131ed0-6e82-3609-8e87-9e55a5421f76 | -7.24445 | -45.26423 | 2026-10-06 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fe2d584-de7f-3bd3-a29d-50e013a183d1 | -10.36015 | -45.02354 | 2026-10-06 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 599269c4-9ecd-3639-b558-93be63566495 | -7.5719 | -46.63464 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394bb435-9879-3a9c-9bba-1240a1e0bf5c | -6.45271 | -55.43035 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a195ff6-03fc-3719-b215-547aa3d6e579 | -9.3135 | -47.62947 | 2026-10-06 04:40:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ece012ac-6ca7-39da-9648-eea0b2ab8992 | -8.32406 | -45.46212 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63a464f4-218f-3932-b349-e1d6b38d16b9 | -11.67099 | -43.63792 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 382483e4-e17b-3e74-965f-2475b5fdb343 | -8.58664 | -45.66633 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e443f47e-b44c-3683-868f-9c113c277b62 | -6.15017 | -47.12465 | 2026-10-06 04:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 728a63d3-659b-383b-9a37-277d2974eea9 | -11.82499 | -44.69036 | 2026-10-06 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9287ee76-41bf-3d85-b8d2-0f2a706cfd2d | -7.82478 | -45.3001 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9303814d-24e9-3f71-a781-53f52d7c3509 | -5.83777 | -45.01244 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 845bce69-733f-3b26-ae97-4df3120808f6 | -11.27771 | -45.51133 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 710ce1cf-2ae6-3bdc-b6e4-290629c4cd2a | -10.96779 | -45.41151 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a449ad37-36b4-3b8b-b6e8-f398ee8cef86 | -7.73141 | -45.46651 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1586c7fa-2523-3f8d-a683-82d09f9e7035 | -11.36367 | -46.68038 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5677676-e069-3f21-9173-b52befbdaa9f | -4.0558 | -56.33323 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 467aa41a-74ac-3d0c-8d0c-4853d73933a1 | -9.80324 | -44.78938 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6868501-4791-3b71-8e52-9a836f798044 | -6.00518 | -53.51388 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f9a30eb-9b45-3792-90b8-1d624930439e | -6.81229 | -39.29988 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e2837dd-0a9a-3c42-ab94-3737528a6279 | -5.58694 | -47.27208 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3ab7d03-5d24-3e17-9710-6fab42ce221f | -7.01879 | -43.44479 | 2026-10-06 04:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5efd7c9c-94ae-32a8-837a-3964cdf7083a | -9.82921 | -44.79583 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f409604-1b4d-3c47-bfd7-a6a438aec1bd | -6.0058 | -53.5101 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e3e76d-ea9d-30f5-ae67-6c0f6e115da6 | -11.68905 | -43.67095 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c464199-b151-390c-928a-3e5dd1780de0 | -12.76615 | -44.87911 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61ac78ab-ad0e-313d-836c-866642194fde | -11.71878 | -43.63984 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a16978ef-2630-3c2c-93be-3ac45aa53b5d | -3.70093 | -58.93325 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a82ef4e3-c27f-3cfa-9911-ad4f710d3153 | -6.20961 | -55.66819 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb1fef02-d2c7-3c27-8619-2795eb4c0a2e | -5.67312 | -53.50261 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2804d39-94fc-3d60-ba86-c1b982a48a16 | -6.45761 | -55.44962 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 443b8779-1f32-3bca-bcc4-b7dad2a54335 | -7.01409 | -43.44925 | 2026-10-06 04:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7f0555b-d46c-3680-9486-29c0e739b9c3 | -6.31671 | -43.34744 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b6cf455-1c3d-3be7-a8cf-e15c647738d7 | -7.829 | -45.29647 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72cd01ad-c397-3e95-b904-8f9b5fba2340 | -8.69571 | -45.22279 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b199e6ec-86d4-3671-8872-17ca75595802 | -6.92459 | -43.67391 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6db74163-5cf0-339f-ae8b-da846dc61ecb | -6.31746 | -43.34248 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4772d135-8ddc-31bd-9eaa-db92aa676c30 | -11.5363 | -44.89592 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55b78973-69c8-3ace-a109-4ba96ad737b8 | -6.34833 | -42.54601 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 23f747cf-a5b4-3d22-ae36-20b704b908a6 | -5.84721 | -45.02216 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 745cfce6-37bf-3da0-86e1-ac4fdd4dc0a7 | -8.98505 | -46.76143 | 2026-10-06 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7630107c-1c5b-3888-a115-e24924109ecd | -5.67732 | -53.50326 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d76f25e-01e3-30cc-bd13-a8d0f2bc8e8a | -6.04994 | -45.23117 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa9e1e0c-5741-3430-bfd6-fd341dd7b95f | -11.69374 | -43.66766 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f6f5c9e-79de-30ce-8f23-cd925a3ed29c | -6.93338 | -45.59999 | 2026-10-06 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fdfa87e-127e-3c23-b95a-60bfdc3cccae | -12.32475 | -47.83731 | 2026-10-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95008851-4e3a-312e-b2e1-614d9fc8deef | -6.90975 | -43.66671 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79fce373-9f0c-3a9a-9d17-aa7697e52b2a | -8.61861 | -44.91116 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eec239aa-2486-3ae1-8f28-eecacdb300d6 | -11.24273 | -45.25252 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecbdae53-87a5-3310-83d1-47798efa9254 | -12.76153 | -44.88358 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d87f92c3-4c36-3044-ae26-6bddb96aa6f3 | -6.23035 | -47.0004 | 2026-10-06 04:40:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 920c77fc-26c7-345d-90f4-7e07ca77c01f | -6.93625 | -43.67576 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40737cac-3176-31ba-821d-37462d2c6eb3 | -7.18695 | -42.0115 | 2026-10-06 04:40:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6c95f01-b21c-3a33-b739-fd1a1efb92fb | -3.99188 | -56.265 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d437526-95d5-323e-a4c6-0799d2045f72 | -6.46414 | -55.44812 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98451ab1-4a16-3db3-9a5d-6c24f81b1558 | -11.28034 | -45.49339 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9917a3e-b28d-3d6a-b675-ffd3dbb59e13 | -7.33593 | -44.37909 | 2026-10-06 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea213768-5f1a-363d-8d68-b1f69fe7b8c7 | -6.82224 | -39.30512 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 571e6630-5b44-32d7-baac-7205fcf1ec03 | -11.28076 | -45.51632 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2bad1431-95e2-330c-bd44-0820c6957b22 | -11.29556 | -45.51845 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 47867b14-b7f9-32c2-8036-83b6cec4eb0b | -10.42345 | -49.25237 | 2026-10-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 776f7ac0-c5a7-3280-a7f1-985f0d2392db | -11.69322 | -43.67152 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e33e6af-2e1c-3828-a5ad-d4a519f623ea | -11.67552 | -43.66607 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2674d594-b3d0-3607-bf1a-bbf1d5c89b1a | -6.71436 | -45.97416 | 2026-10-06 04:40:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be4271ae-1e07-3076-8da0-2a8e93a5aa30 | -5.8254 | -53.8639 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5301850b-4f24-3a36-9bab-544447da0bf6 | -3.71209 | -58.93351 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5864555-d772-325a-8522-b89645c26e1f | -5.84427 | -45.0176 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 321739fd-b47f-3e5f-a8fb-daa742755a0d | -7.37627 | -46.22572 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README48.md)
