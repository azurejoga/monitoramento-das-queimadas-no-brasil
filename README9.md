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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ef9db4f-dd1a-3362-b66a-08b1ceff479f | -7.45385 | -44.74871 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e008f31-597a-378a-9f9a-0cf6ef444d77 | -1.12379 | -47.7402 | 2025-11-30 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7de5434-8669-31f7-80db-157adc15e0ce | -12.70804 | -46.79316 | 2025-11-30 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b621c3-5ab4-3de4-a8f3-fd0b899def9e | -7.74251 | -44.19013 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7bfaf303-3702-38d7-8698-2bda8d230fa0 | -13.33962 | -43.74612 | 2025-11-30 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1c36c7-4660-3720-8033-9f4b9bf4b4c8 | -7.46132 | -44.74112 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08f57e86-06ce-33e2-823c-d78bc2b7b2b4 | -9.29674 | -40.3657 | 2025-11-30 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1f0a531e-403d-394b-ae07-d980c37fcd42 | -10.51772 | -40.32889 | 2025-11-30 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8339c17-000a-3f72-b27d-ac627c521a96 | -12.65512 | -46.74929 | 2025-11-30 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca03db73-2a37-3045-82ac-80eb34c4f7d6 | -7.45625 | -44.74463 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2068211-c267-34a2-9e21-d0387b001c17 | -12.14574 | -40.36227 | 2025-11-30 03:55:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b642121b-0ed2-354a-a103-6ee612b3c429 | -2.24611 | -46.5194 | 2025-11-30 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9766423-8ba9-386c-aa98-dd1dadc5ef75 | -8.17217 | -34.98044 | 2025-11-30 03:55:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e9cef1f8-5091-34e1-b83d-6f06a08678da | -8.17241 | -43.2093 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| d2305bff-69a9-3e8c-8453-610c489ca585 | -8.49994 | -35.01391 | 2025-11-30 03:55:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5e0154dc-0249-3fce-9c81-6b6939a36cef | -8.04027 | -43.12651 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 164fc327-4be3-3636-9775-7aa33209bb05 | -7.4606 | -44.74528 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3b2070f-4b95-3a6a-8780-33e410952380 | -8.0364 | -43.12587 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 13ff47f3-4a97-37ad-90ce-c93a8e856f0f | -7.73549 | -44.18107 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 091ba8b2-f551-3ace-bb44-27f577afa9f5 | -8.04201 | -43.1251 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 52aa0ed8-eb05-3904-8186-fc907f9efd6e | -13.65232 | -44.25504 | 2025-11-30 03:55:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0f15f5-93ae-36e4-b8d5-3119a3db215c | -8.16466 | -43.208 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 381b8265-61b1-308c-99b8-54ba6a095405 | -9.87382 | -40.57089 | 2025-11-30 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5531c96c-9bef-3844-a24c-ac7d1222c6c2 | -7.9162 | -41.91153 | 2025-11-30 03:55:00 | NOAA-21 | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 01ca639b-ba05-3517-aef5-11e5b3186798 | -1.88559 | -47.92335 | 2025-11-30 03:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04dd2ecb-f763-3255-bfb3-a3fe6210ab28 | -8.04333 | -43.13203 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 773db2e6-28ab-3e46-bc1d-8b24045824d4 | -2.434 | -45.73972 | 2025-11-30 03:55:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c147634-f146-3434-9cf9-d1551d2b2204 | -6.90629 | -42.82107 | 2025-11-30 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb5c0c8a-06b6-3d52-b048-c9633f3ca13b | -8.16799 | -43.18843 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a28e54e1-1ac5-37a2-b5f5-37e8dcff3b63 | -8.04504 | -43.1306 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 340d15f6-dd0f-3914-971f-c792eb65e8a6 | -9.13485 | -35.60681 | 2025-11-30 03:55:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19501b98-952a-313a-a559-3b5f92821b68 | -11.26196 | -44.54268 | 2025-11-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 652234da-c7b0-3142-a184-8792d8dadc37 | -7.75016 | -44.19548 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b776d6a2-f892-353a-a3b6-045eefd22053 | -8.04117 | -43.12995 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 55d21f27-84e1-37c2-bcb7-f0d8a7af5e2b | -7.45553 | -44.74879 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e637434b-7b85-3040-8fbb-51c25d55a452 | -8.1677 | -43.21355 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 17be967a-70f8-333e-9fe3-a96eb9d9d92a | -9.35124 | -40.53061 | 2025-11-30 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87642618-7258-3729-96ba-6825814c160e | -2.91251 | -40.38941 | 2025-11-30 03:55:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d5e83fb1-7ad3-39a7-ade4-d99de7e8e743 | -8.04587 | -43.12574 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 24974ede-a720-3841-aff1-d4831d62d980 | -7.74791 | -44.18337 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf1c20c9-37a4-3ffa-a2f0-2ad3053dbbc4 | -8.16411 | -43.18779 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 95af0ffd-1da6-34ef-ad00-bd05fab98432 | -7.74729 | -44.18712 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2595635f-3349-38f4-9d52-c6dc5fcb446b | -1.11859 | -47.73502 | 2025-11-30 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94be7530-ac2c-34c3-a9c9-8e4dd09cef7f | -14.2646 | -44.3856 | 2025-11-30 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf3eddb4-ba24-3079-bf1c-ab84aec754a8 | -7.46684 | -39.96284 | 2025-11-30 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 611433d6-a1c2-3c6a-a308-37d38452625d | -7.75079 | -44.19175 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcfefd11-4352-35aa-a567-151bca69cf83 | -8.03946 | -43.13138 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 128cc464-4d3a-3a49-a3f2-363665f7a509 | -8.53189 | -40.23112 | 2025-11-30 03:55:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c0c30cf-9b80-37e2-be65-f39582d56901 | -12.83192 | -47.39077 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 086d0cc0-64a6-30e2-9926-638658e9ea45 | -7.74315 | -44.18633 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bd6632d1-8176-315e-9a77-61dcd158bb0e | -13.48853 | -46.71439 | 2025-11-30 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4f1860d8-c809-30e7-8e60-55c5ad6e6e01 | -10.23298 | -36.52971 | 2025-11-30 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| deca5abd-9194-3f74-b8b4-858097385213 | -2.24557 | -46.52271 | 2025-11-30 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db7914b-b890-3717-a81f-4071469cbd31 | -8.79309 | -38.60688 | 2025-11-30 03:55:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7608bedf-2455-323b-8d62-e945edc2559f | -13.94088 | -44.38398 | 2025-11-30 03:55:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fef8fe4-7daa-3c55-9c6e-380f39d71913 | -8.04413 | -43.12715 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 83e437ab-6bd1-35e7-8791-f15d6b74565f | -7.75491 | -44.1926 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fa610d7-760e-3402-88c3-5097da608bb8 | -8.1518 | -42.94251 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 534d85c0-1431-3e3d-8695-aee9fcaac62b | -7.46741 | -39.95924 | 2025-11-30 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4966650d-cea4-3f2e-82ee-1e48b8afd141 | -7.73485 | -44.18487 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88c35fd3-a24a-3447-aa70-cc5f24ed969a | -1.88489 | -47.9276 | 2025-11-30 03:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2e38f36-feee-36b1-b277-02744d5eb97e | -21.80274 | -45.84864 | 2025-11-30 03:57:00 | NOAA-21 | CARVALHÓPOLIS | MINAS GERAIS | Brasil | 3114709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66345604-b30b-3aff-a346-2290a9271b02 | -16.79657 | -53.77469 | 2025-11-30 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c97597a8-4268-3f00-8e93-fa02fa956d94 | -16.22202 | -52.18132 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e9ec8d-766f-3176-b9f3-11836f679449 | -18.9847 | -48.07811 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 766c0f30-de08-3bf8-9ac0-d1501c1de99f | -15.09373 | -50.3434 | 2025-11-30 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c2b84a6-326c-3314-acc3-817e90961592 | -22.29919 | -43.47068 | 2025-11-30 03:57:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9ddaee5-8719-3b56-9770-b257d3ce4937 | -21.15198 | -48.61059 | 2025-11-30 03:57:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3331631d-31a9-37f5-a7aa-934738b279a3 | -16.15147 | -43.89857 | 2025-11-30 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f89484de-3228-33d3-8b9b-87ced2606c18 | -18.15253 | -47.1338 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f323df61-62d3-3fbc-a4cb-daeed707c4e3 | -18.13503 | -47.1566 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d87f6e1-c226-35b5-8f6a-4a73a66fa167 | -15.09921 | -50.34453 | 2025-11-30 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86495d37-caf7-3817-8716-5168a7611ce5 | -19.93423 | -46.72824 | 2025-11-30 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea823aca-061c-3ed9-9dad-8f35edb1665a | -17.56192 | -42.08752 | 2025-11-30 03:57:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b37c4fb-8246-3858-a0bf-bb21231f4a28 | -18.11908 | -47.14976 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a614605-f878-3120-bc1d-2790f1dff962 | -18.12161 | -47.15801 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56393e8f-9ad2-3640-8b48-0f8c4fe469f2 | -18.93834 | -48.48406 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 127a9360-c4b7-3376-af02-991ba64be561 | -18.15504 | -47.1436 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee0dc978-77b3-34e0-aa8d-df3ea5db58c9 | -20.18812 | -52.38756 | 2025-11-30 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06823167-81a3-30d9-a3d0-388173a04e05 | -19.09244 | -48.59505 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dc182cc0-15b4-3e61-b100-f07679a084b0 | -17.85936 | -44.30719 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 750959b3-e0a5-31e9-8836-c3fb192e05a9 | -20.61818 | -44.39632 | 2025-11-30 03:57:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dc2049c1-f6f1-3081-9a90-b70ef263efbd | -15.09402 | -50.34324 | 2025-11-30 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04a6fa62-a0a7-3b89-8c01-6707aad91c5c | -20.62123 | -43.95125 | 2025-11-30 03:57:00 | NOAA-21 | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e6247aae-7deb-3f4c-8e74-66396c7d1a3f | -19.63626 | -47.66888 | 2025-11-30 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc2ed11-6f13-3bc3-b2cd-85a0427c39fd | -17.22843 | -42.21348 | 2025-11-30 03:57:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f35c6ce-d6f1-3234-8082-2b03b34db634 | -17.85065 | -44.31458 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c595456f-6fa9-3f90-8a98-89ecad8c4789 | -17.85785 | -44.316 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 685b4385-86ac-3302-ae89-3fad7d45c77f | -18.08858 | -40.38696 | 2025-11-30 03:57:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8417fc9-ad6c-3f7f-abee-aca23d1fdf4c | -18.4128 | -46.84616 | 2025-11-30 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e9af7b4-7e51-343f-9c92-db0a9f9d3018 | -18.0876 | -42.35266 | 2025-11-30 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0efd79b3-0190-3dd6-a33c-901798c554f9 | -18.15168 | -47.13827 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ba97bda-40d9-3530-ba79-b9091af87ca2 | -18.74587 | -44.81254 | 2025-11-30 03:57:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fc82db9-fa98-3ab0-a451-2223c46b633e | -14.91878 | -47.45115 | 2025-11-30 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f81082b4-d32f-3ded-9d99-a0d279139023 | -19.63547 | -47.67308 | 2025-11-30 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5131d35e-2b61-3f5e-b238-c5c6dd239cf0 | -16.76452 | -51.35684 | 2025-11-30 03:57:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ba07159-cb63-3e4c-b1e3-cec047617466 | -19.65828 | -46.61554 | 2025-11-30 03:57:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8dbe83b-1345-3fa5-8b20-206b2f64c111 | -19.08888 | -48.58913 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4f147364-437f-3e49-a7f3-f6b0dcbc8581 | -18.1225 | -47.15491 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6816649a-d263-39e9-be14-4f6b8a7625df | -18.62198 | -45.23216 | 2025-11-30 03:57:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
