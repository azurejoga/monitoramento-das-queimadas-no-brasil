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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b997bcab-27ab-3d6b-8d72-3789643008e0 | -5.9185 | -48.0449 | 2024-12-12 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 0ef82c4b-666c-35aa-857d-351c49d8be46 | -18.0659 | -52.9766 | 2024-12-12 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| f91894d4-d2d4-3ad3-bb55-a91e3af98778 | -14.7457 | -52.6683 | 2024-12-12 03:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9d7b19e3-13cd-3d5b-9cfd-3f24989b448f | -11.1959 | -53.8348 | 2024-12-12 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c01ac1a8-4539-3008-8c26-ee3ad7c3fe57 | -3.2503 | -46.8709 | 2024-12-12 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 21211a22-2bea-3de7-9367-06875dc8e8d1 | -5.9369 | -48.0654 | 2024-12-12 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| b76da8b5-cf6c-3ac1-ba6c-3e9a7d4148d4 | -5.9371 | -48.0437 | 2024-12-12 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d425acac-3524-3df7-a04d-55c3155acfcd | -1.8788 | -54.6908 | 2024-12-12 03:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 625d6bd4-aba6-3302-8f55-7a3d9a6d79a0 | -18.046 | -52.9798 | 2024-12-12 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 137.8 |
| d89c0454-c62c-3307-ba01-6646f76b30ba | -18.0663 | -52.955 | 2024-12-12 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 2945e35d-3986-35b0-9b0a-2764b3bd1386 | -14.7655 | -52.6446 | 2024-12-12 03:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| eda0f7bf-a53e-3ea6-a53c-e8761ed2c7cc | -11.2148 | -53.833 | 2024-12-12 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 420dc3d1-9593-3cb1-a51a-02f2f18226f9 | -14.7461 | -52.6471 | 2024-12-12 03:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6d0bcb55-57e7-380e-a92f-185f6914e92b | -3.2502 | -46.8929 | 2024-12-12 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e62ea06d-9c20-3c7f-b344-72601bf8bf18 | -18.0464 | -52.9582 | 2024-12-12 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a1936f6e-8c94-39fe-b99f-cda17737cff3 | -4.18377 | -42.43661 | 2024-12-12 03:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8dd80de-4736-36f4-a877-cfd4f41ba6ac | -4.5415 | -43.56825 | 2024-12-12 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23adc57d-dc2c-3ab5-9b72-3a8df6dc8dac | -3.82776 | -41.57782 | 2024-12-12 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a2205a4f-bbaa-3b2f-a304-5afc5cdf5aab | -7.69529 | -35.26191 | 2024-12-12 03:19:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f6eba9d7-8168-3b31-a1f3-020bb4b32c08 | -5.38572 | -40.66537 | 2024-12-12 03:19:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec6b823f-10b5-388b-a03c-7f45949a9848 | -3.66601 | -39.21679 | 2024-12-12 03:19:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8733cc0-9f63-3ee9-bece-9d857f128c4c | -5.29659 | -43.28807 | 2024-12-12 03:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34cb4ba5-9b6d-36a4-b427-69ecb55653be | -3.84948 | -40.45066 | 2024-12-12 03:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 71ea7f31-60ff-3079-a0b7-ee6eb5214a0f | -3.84872 | -40.45501 | 2024-12-12 03:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ca70357-f3c0-3d5f-80a2-73b6a7d113fb | -5.59085 | -39.45068 | 2024-12-12 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a9cdc09c-65fc-35ee-8672-a7065d6c236b | -4.85948 | -40.75866 | 2024-12-12 03:19:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c2f674d-dda3-313e-8f77-ed7e7f6aee4e | -5.59628 | -39.45147 | 2024-12-12 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e5e769ba-a39e-3f4a-a73c-677c9168b90b | -5.23436 | -38.50527 | 2024-12-12 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7ea76ec-38d1-3181-a882-43313e42a98e | -5.59547 | -41.38887 | 2024-12-12 03:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| df56be53-5c30-309e-a4b9-4786e54387c4 | -5.30348 | -43.28928 | 2024-12-12 03:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb4ac7cd-a701-33e8-bbfa-8c54f992096f | -7.92445 | -35.19041 | 2024-12-12 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d5ae07a8-3ef9-3387-8569-c76b7f786a78 | -4.54464 | -43.56955 | 2024-12-12 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cba3bac7-e94c-3424-b6e8-7e460e9a1d6f | -8.11397 | -35.07046 | 2024-12-12 03:19:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bdfe84c8-0fd7-345f-897c-1122f8258cec | -5.23682 | -38.50647 | 2024-12-12 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 450cd98c-0b01-3e1d-abb1-776bb98f3c3d | -4.38753 | -42.15265 | 2024-12-12 03:19:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 508c1280-d2d4-31fc-9e26-c0675b342139 | -3.82618 | -41.57617 | 2024-12-12 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ef51bda8-b736-3ed1-9cbc-27b0db0b3601 | -4.18481 | -42.43068 | 2024-12-12 03:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9d9831e-2e4a-3e02-ad2c-fb5f80bf9139 | -6.12653 | -42.54241 | 2024-12-12 03:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9fb84e4-0a61-388e-ab63-8ee4fcfb5e57 | -4.55048 | -43.57779 | 2024-12-12 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c94b86b6-8a79-337b-908c-6f9103923a70 | -5.23945 | -38.50623 | 2024-12-12 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e10da776-0b49-309b-81ca-a95ccba84a6e | -4.90086 | -42.07716 | 2024-12-12 03:19:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 978931ae-20ba-322a-8f78-c675594e9601 | -4.08768 | -38.47281 | 2024-12-12 03:19:00 | NOAA-20 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 84803df1-80fd-3ee3-8269-4ecc8721d38f | -7.69613 | -35.25688 | 2024-12-12 03:19:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e591a34f-1295-3186-80d4-1be33235bff6 | -3.85466 | -40.45603 | 2024-12-12 03:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24a39730-f8bf-3632-829e-bdd08d625023 | -7.70008 | -35.2575 | 2024-12-12 03:19:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 61a16de5-7d30-333a-8f6d-8a1af687c41f | -7.9236 | -35.19547 | 2024-12-12 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9dd3f2ad-cfcc-3bb3-bd07-6ca6128c0b91 | -7.7507 | -35.1472 | 2024-12-12 03:19:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 428af7db-d067-37ee-b057-21202bd32f39 | -3.8287 | -41.57256 | 2024-12-12 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f4021880-47c5-380a-8dc3-1715b2f4c27d | -7.92836 | -35.19107 | 2024-12-12 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8718cd93-873f-3ccd-bb3a-24caa6057bf1 | -5.87443 | -35.41563 | 2024-12-12 03:19:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 49a67276-89ed-3a45-a8e7-5688864eb6c2 | -5.39159 | -40.66641 | 2024-12-12 03:19:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60ab40b1-4e38-3c9b-b9df-7eff9a7604a5 | -7.92752 | -35.19613 | 2024-12-12 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 73ba5d8b-ad4e-3ae4-957d-b08cf9629775 | -3.82708 | -41.5709 | 2024-12-12 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5c0a7fc8-aa14-38f0-8b0a-1ecef8f09925 | -4.38024 | -42.14939 | 2024-12-12 03:19:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2d68379-2171-317f-adeb-037b73de6d43 | -4.54728 | -43.57655 | 2024-12-12 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55e4269f-c615-3bb5-a35d-952fd5bf300b | -6.12655 | -42.54545 | 2024-12-12 03:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c134c3e3-ea32-34f4-9804-7b45b077fe4f | -6.68478 | -39.26237 | 2024-12-12 03:19:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6ab5f72-01a6-34d0-8f64-aa0080dd3535 | -4.381 | -42.15149 | 2024-12-12 03:19:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e1444a1-912a-3349-8f2f-d631b73830ce | -6.1255 | -42.54792 | 2024-12-12 03:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f0e25f16-d634-3f8b-b5b0-98865d0e35f9 | -4.19042 | -42.4379 | 2024-12-12 03:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2aa9c333-2147-39f5-8425-e07673604f91 | -6.12552 | -42.55114 | 2024-12-12 03:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 11dd0729-6a3b-30fc-97cc-c8e4def93664 | -7.75128 | -35.14325 | 2024-12-12 03:19:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0a08eab2-fa6c-3252-8c9a-ba2cd4d75226 | -6.68532 | -39.25924 | 2024-12-12 03:19:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93c18bd6-0786-3d7d-89eb-34bfe5edcc2e | -7.75154 | -35.14215 | 2024-12-12 03:19:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 19ad610e-7735-3402-85aa-e20ea0130a78 | -5.23735 | -38.50348 | 2024-12-12 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02449f0f-b632-3b6d-aea9-010e93d38945 | -5.59533 | -41.38826 | 2024-12-12 03:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a7b3a31b-2e9b-352c-b1ee-d2cc88106e9e | -6.02691 | -35.50471 | 2024-12-12 03:19:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b34afb2-e11d-3c0c-b497-aafc2e5b6758 | -3.85541 | -40.45168 | 2024-12-12 03:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 89f5396d-c148-36a7-9ab4-b884cfa43f05 | -4.38677 | -42.15052 | 2024-12-12 03:19:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7264b200-4890-3e7f-814e-2c78a2f0f4aa | -1.8788 | -54.6908 | 2024-12-12 03:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 93d65cfa-3987-3fd7-b642-03cd27b73b66 | -3.2317 | -46.8716 | 2024-12-12 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 69671d00-cc46-372c-a58d-0a65f5a37f0c | -18.0663 | -52.955 | 2024-12-12 03:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 11295b16-ae21-379d-9499-85c148a9338f | -11.1959 | -53.8348 | 2024-12-12 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 18ec523b-27ad-34a0-8b84-13d394514d13 | -18.0659 | -52.9766 | 2024-12-12 03:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8afa05fe-a1a4-342f-962b-3f22fab5db6c | -6.9156 | -43.5418 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e44bfc37-2cb8-3e08-a9e5-e1c2ec119492 | -3.2503 | -46.8709 | 2024-12-12 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| bdc96135-51a7-3041-91ff-dd78b929b6c1 | -9.7018 | -36.1652 | 2024-12-12 03:20:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 677eb8db-bac1-3956-917f-a1d17f237183 | -11.2148 | -53.833 | 2024-12-12 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b387d39e-3563-3fb9-b436-536a67c870bd | -18.046 | -52.9798 | 2024-12-12 03:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6606df2c-6c4f-3d73-b9ca-02e33ea5c60f | -3.2502 | -46.8929 | 2024-12-12 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9f0daed7-5e20-3d84-9676-91afc475cc19 | -6.9158 | -43.5185 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 47ad87f8-4f73-3464-970c-04c26c80e17a | -6.9161 | -43.4952 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 74fc5a0e-de3b-3df7-9cab-f52919e414a2 | -9.7013 | -36.1923 | 2024-12-12 03:20:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 0e196021-bd9c-3d82-966b-e962930562a1 | -6.9349 | -43.4934 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5552a55e-6e15-3222-82b5-4db0c38d2251 | -6.9346 | -43.5168 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 442.6 |
| 60e94a41-501e-38b9-8a11-e63220986738 | -6.9344 | -43.5401 | 2024-12-12 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 18e5426a-9c78-3f7d-bb8e-14cbd536d1b1 | -12.36411 | -41.18607 | 2024-12-12 03:21:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5bcba630-8b56-33ef-9304-62110d896245 | -6.91792 | -43.51585 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| da3b332f-b522-3011-acbc-8279cbca2b05 | -6.93146 | -43.51882 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f23349ed-4dd2-370b-be32-347a359cb50b | -6.93239 | -43.519 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6e4d6438-773f-3f0c-8b91-09adf3f01caf | -6.92692 | -43.54356 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| afdd516e-2a31-3426-8f11-380663d38684 | -10.53279 | -44.68375 | 2024-12-12 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5314ba8-be31-373a-a73b-8867eb5f48a5 | -9.39135 | -36.04958 | 2024-12-12 03:21:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 43973f61-1a82-379a-bfbb-7c9ff859eb77 | -14.04765 | -43.30378 | 2024-12-12 03:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fdab448-a634-3b97-b01c-c994b126805f | -10.49474 | -36.84948 | 2024-12-12 03:21:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bdde706c-b924-3474-8aaf-40a6d57b4001 | -6.92806 | -43.53735 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| db2ae2d5-40c0-3b36-ad85-ada17b4ed021 | -6.92444 | -43.52374 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 92ffcfa8-b0ce-3b0d-81ec-2b21ad324568 | -9.69417 | -36.18396 | 2024-12-12 03:21:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 90d2e886-e1b8-3328-84b2-ff68cb8471da | -6.91528 | -43.53476 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3c38cc90-e616-3de8-8002-64b8b80e7ac3 | -6.92919 | -43.5312 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |


[Clique aqui para ver as próximas entradas](README11.md)
