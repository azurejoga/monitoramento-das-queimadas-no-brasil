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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19a54c15-39a4-3d89-99a7-bfad14a1932b | -7.449 | -43.10429 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b632635d-f5c9-3bcc-9beb-f1c24e1926e3 | -11.41961 | -44.55182 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e931eae-a0d3-37e3-9fa4-a5713415c34c | -8.01342 | -51.82705 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a97e42f7-44f0-390c-81f6-998f4c98c70c | -8.75484 | -49.94631 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f159abb-3d85-3411-aa4c-6bd08c61f6c1 | -7.14503 | -43.16896 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8773d25-6eff-324f-a3ae-661377e9c898 | -10.29888 | -49.95546 | 2026-08-26 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16a9623c-f422-334b-ad34-d06948c30ad1 | -11.48539 | -45.09319 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6231494f-d56e-3327-8f0c-ad511bf8cf90 | -6.88142 | -43.75027 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc19e1b9-99ac-3f69-b59b-135e9cc07db8 | -11.38125 | -45.15627 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f014a2d-33f8-3fc0-b518-12aa499e2a90 | -12.72834 | -48.37698 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b060e3f3-f826-3e94-9a95-f574fde3c2bc | -8.11819 | -47.46172 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1cdc6b2-f02c-3f5d-bdad-361089b2342b | -8.56885 | -54.81817 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e48d02fd-1702-3601-af08-5edd48705237 | -12.42571 | -42.89675 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfe41fe6-8966-398b-9ff3-a90e3919bc27 | -7.76271 | -44.76201 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80dadb50-74f5-3d0e-858c-d394c569665f | -9.67445 | -55.08453 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4fda461f-a265-3699-bb41-cf39debcedcb | -9.66892 | -55.1005 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b940ce3e-2fec-35e0-9af7-3e037b85eca4 | -6.96232 | -42.08763 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae2380fe-abbc-3b3b-bef0-1d43d36dbdad | -9.02528 | -50.78655 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b55629b5-4b32-3e25-a793-9db66403a0ca | -13.89096 | -44.26979 | 2026-08-26 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e37543b3-af99-3954-b486-ab54d5ab9a26 | -5.56204 | -50.4938 | 2026-08-26 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa7e7bd3-1e1e-3deb-810d-7f556e820be2 | -6.25878 | -53.3728 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd28fd28-4dba-319c-ab6b-0b2f8b70dad7 | -8.08015 | -37.69035 | 2026-08-26 04:08:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f946745f-f05b-3238-887b-90ab257fd2cc | -12.66926 | -48.41133 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 752ce76e-5b5a-3dd5-9508-faa557ce116e | -7.86205 | -46.11404 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88262df0-817e-3437-9452-1c0704dbe1d1 | -10.75646 | -54.01824 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0211a97a-b7a6-3cd6-928f-2f3cb0535873 | -7.43108 | -43.08092 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d069f45-cb25-3fa9-a1d8-edae9aa97bd7 | -12.03271 | -46.03561 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f006e016-55df-3743-8b9e-1781b787edf8 | -11.42251 | -44.53484 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e62a69e0-d246-3092-8f4e-a08086d3e71a | -7.20018 | -42.76263 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae6f63e2-4f24-3cdb-9d60-efa0dc12999b | -7.27433 | -45.35966 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 328dd972-9fa6-36d6-914c-4da1c3714d62 | -7.19859 | -42.7504 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f52db119-b89b-34e7-9737-8b600a3da2fd | -10.98483 | -43.70847 | 2026-08-26 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a848e7-19e2-3cb6-be60-0d8a9fd3ddaa | -12.02634 | -46.00353 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0ea7a19b-3fb8-32ba-b7bc-f6092289d3e1 | -7.20081 | -42.75874 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27728439-c05d-3275-b53f-e8ac299acb7a | -9.03642 | -50.78904 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bd6e36d3-8153-30a6-bb44-0275382b2d4a | -6.91274 | -44.66197 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e4372a8-d70c-3321-aba8-6b7f248bb282 | -8.13818 | -47.50918 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e271b5bc-ffee-3fce-9f4f-f42b72cc746a | -6.16518 | -53.49257 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36155217-f2b2-3e74-9f34-8543852252bb | -8.56169 | -54.81669 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d074c7c-2fca-348b-8f95-cef7c1bb30b2 | -10.75405 | -54.03008 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a981e298-ef5f-3a08-9976-e38bad6877f8 | -9.26928 | -45.64393 | 2026-08-26 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 90e37d07-6023-30df-8d06-341b44475b73 | -9.56455 | -49.26615 | 2026-08-26 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38878361-4729-3746-8a39-58bd8f336c82 | -11.29141 | -47.07039 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60986ebb-2934-3d5b-baf2-37971d262ab5 | -13.34391 | -48.23055 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f647e9c-1e5d-34d3-86e4-3ab8454c92f2 | -9.37465 | -40.516 | 2026-08-26 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5658cb1a-fa39-3a0e-ae86-d8b30b34ac26 | -12.69363 | -48.38909 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 794231a1-c3ba-393f-900d-92d5f8f586be | -9.67196 | -55.08513 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc5d62f5-d697-3a2d-9e1d-df982077c466 | -9.6672 | -55.08355 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb125898-f3c4-39e7-9538-f97938032582 | -6.88215 | -43.74591 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ab52284-adc2-3ab5-be07-2d2e45d2ba24 | -7.25393 | -43.12334 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b70f7554-d52c-3a8b-829d-dcb0b2cd78ca | -8.86086 | -49.72132 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cfdc742-3aa1-31c5-bac7-7229e501c3a4 | -8.01428 | -51.82256 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77a9c359-e3f1-3771-a188-8c9d052a77dd | -10.04272 | -46.04833 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa91d741-d877-3e21-848c-d55f4e0fa1a4 | -11.81899 | -47.6571 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593b7206-d7fc-34ef-b013-1218b6a8ab60 | -13.36439 | -48.21822 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac67754e-b2c3-32fa-a6eb-5c1156d06c52 | -7.44835 | -43.10828 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a605ce6-bf5b-3ede-8b1d-cac799bcd1db | -12.68136 | -48.40502 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c98649ef-4eee-38a4-b317-415886fdd1b3 | -11.01645 | -45.06656 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d11eafd-0935-37eb-aaaf-b1917d50f77b | -12.73593 | -46.48147 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 421312a7-0578-3757-b5b1-320188a5dbe6 | -6.14814 | -53.69047 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4336138-18d1-31be-b349-dce3c1c3dba2 | -8.02739 | -51.8169 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 949e3ecc-4fb4-3d03-b45f-ae9fbeb518fa | -11.26182 | -47.06525 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab2e8542-7459-3495-bd03-e2bdb74982d6 | -9.44258 | -51.67788 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 672c04e4-b304-3f9d-a92e-999440edead5 | -9.59723 | -55.12314 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 755de4de-edf8-38d0-bc21-7e1c3d4f7049 | -8.01523 | -51.81456 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb8b2aa2-7fdb-305d-aeda-599399f2a0c5 | -10.74864 | -54.02275 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5e57900-3cc1-39ec-a33c-eb2a1b37f229 | -8.13901 | -47.50442 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4940c0b2-3bbd-3e53-8dfe-38917392d8ef | -12.17293 | -50.60707 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4485e04-7df4-3039-b931-e25a7c2fd7de | -14.22341 | -42.11197 | 2026-08-26 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7498ec21-bbe8-3348-8f97-1776d65732f2 | -7.97801 | -45.24535 | 2026-08-26 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd9cbbe2-b911-3598-9ed0-440792743592 | -6.2713 | -53.38173 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63c45661-11db-3e51-8b26-f05deeb3aff4 | -6.88877 | -43.75151 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41b1fa89-97ad-325d-8edd-0f904617027d | -13.35729 | -48.23189 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fdfc6d2-989d-3a8f-abff-28f722930e62 | -7.291 | -45.35891 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfad1477-84aa-393e-bad9-0c5254ff657a | -12.71403 | -48.37916 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c39b6df6-a6f3-3150-940a-2efbbd07cda8 | -7.7597 | -44.75653 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6282602-df9b-38ed-941c-db27654ea9df | -12.14122 | -43.35212 | 2026-08-26 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eff8fb4-acf6-3d7a-a247-6825a03fe977 | -11.0046 | -51.16739 | 2026-08-26 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e92fb3a7-15c9-3570-a462-20cd99b89e76 | -13.36671 | -48.20582 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc495976-03a2-3115-a6fc-50ad9d1c10d5 | -12.15382 | -50.59518 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1116d466-d4d7-30eb-983d-2faed97a3e6d | -12.67532 | -48.4035 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34a0cc89-0a1a-3159-aa08-20f274d5c8f8 | -12.76853 | -44.25753 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a0290a5-4dd4-3840-89f6-edcb40748d09 | -11.74448 | -54.53746 | 2026-08-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1eaa40ce-74dc-39e1-9424-4155852e5ac5 | -12.66026 | -48.40971 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6058d780-853a-33a0-a05d-5d3ebbc9e835 | -9.18865 | -49.99692 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c8f3b3d-31f1-390c-8906-67d363b70bb2 | -12.1631 | -50.60167 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7083990-a074-31db-826e-8358494a585f | -6.88949 | -43.74713 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b811792b-7796-3603-ba7e-3eb843b00283 | -8.64424 | -54.75115 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb9c481c-bd4d-3ec0-9fe9-8b73bce25ddf | -8.71444 | -49.60653 | 2026-08-26 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0cc7c52-562d-3c26-b1bb-c084ff2c5e32 | -7.29815 | -44.08745 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c28c3ac-16c2-3f2e-a2fb-35b28a080eae | -12.1677 | -50.606 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48c6971c-bea9-3db2-bd01-4c1c3d4cd7e0 | -11.81585 | -47.67411 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a70651e-715b-3194-81f8-321e0cd88886 | -6.26565 | -53.37223 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b536f2f2-fa75-35ec-b165-5fde29bed80c | -9.02461 | -50.79016 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67e81af7-c182-3d2a-bd07-3c84cce234e3 | -12.42738 | -42.89698 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e114f196-c223-3e26-9ec9-2189728d87b4 | -11.84184 | -47.67922 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30f46346-cdb1-3fe9-9eb2-a37c329c4e16 | -12.76044 | -46.45831 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8015a60a-16bf-3d66-9628-0630c5e62a26 | -7.0508 | -44.89785 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90f40b12-cd0a-3543-90fc-7edb3471aec1 | -6.25072 | -53.37788 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6be14cf4-dca4-3e76-9e3d-22e775bff22f | -6.29729 | -53.58126 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README22.md)
