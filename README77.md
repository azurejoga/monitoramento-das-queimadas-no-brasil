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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e2bda4a-7eff-3a2b-a1c7-91a88cb72105 | -12.5954 | -48.61287 | 2024-10-10 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 382fd7c0-3e57-39c6-b587-9854ab0b6fad | -2.13968 | -47.98771 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7efcf490-55c3-38d4-a13e-968d11f180dd | -2.12684 | -47.49454 | 2024-10-10 04:19:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc385b95-6c6f-3c7c-948a-d4a2fcdd3de0 | -1.78632 | -47.8433 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f70119ef-e2e5-31d3-a5a6-1c1e126109e5 | -1.78243 | -47.84268 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a2045f4-a909-3ddd-9284-978fe509dff0 | -1.5866 | -47.64021 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd21968a-5746-3525-81fe-dc0b4875b15c | -1.46517 | -47.23755 | 2024-10-10 04:19:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 914622cf-8983-3139-abe7-f4abdbc5c0e4 | -1.4434 | -48.14863 | 2024-10-10 04:19:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee423620-447c-3131-8ce8-78790dfc4a36 | -1.29029 | -48.4385 | 2024-10-10 04:19:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3476756f-9a9f-338d-96eb-19a8cd9bcd06 | -1.20383 | -48.19642 | 2024-10-10 04:19:00 | NPP-375D | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a20465e3-23d5-3219-9a3b-24f5cda85d4b | -0.70743 | -48.03646 | 2024-10-10 04:19:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9fe3b07-fd0b-321a-84e7-fb0f9951765b | -0.70592 | -48.03439 | 2024-10-10 04:19:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7040810c-322c-3060-80a8-762e67fa5829 | -2.46254 | -47.84133 | 2024-10-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e48e8ec-5361-36c7-a44a-dd706e1f002d | -2.45869 | -47.84071 | 2024-10-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6ecce3a-3833-350a-91c0-fd31ad3cd498 | -2.45854 | -47.81662 | 2024-10-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d61127e6-e4de-3af1-b322-8d381477d169 | -2.424 | -47.81093 | 2024-10-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e18671db-db0a-3e33-9756-2af44f3c2d3e | -2.33293 | -48.48531 | 2024-10-10 04:19:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 664e756b-0e68-38f8-a143-41fc48eed22a | -2.29544 | -47.89094 | 2024-10-10 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b22399f-4fcf-34bc-882b-536994d48669 | -2.2932 | -48.40034 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5a80596-b756-3eca-8cfd-1cae88b37658 | -2.23015 | -48.02425 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32e6a76f-dbde-3c71-8ec2-9e54857c061e | -2.22935 | -48.02914 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46d928d0-6f69-3004-a635-d61abb372879 | -2.22625 | -48.02364 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a389953a-021d-305d-b280-02493e1db360 | -2.20502 | -48.81438 | 2024-10-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1470daf1-5609-3706-8dbd-deae93ada03a | -2.20456 | -48.15671 | 2024-10-10 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f7549b4-6410-31d7-bfef-54e79fa02663 | -2.2021 | -48.8065 | 2024-10-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 415f5a17-e110-3341-a20f-90d036ecdd25 | -2.17967 | -48.23471 | 2024-10-10 04:19:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6162e857-642a-3bf8-a369-72da88570d20 | -7.02342 | -48.54408 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd0eef12-fa81-3385-967c-f53e431ddfd1 | -7.01965 | -48.54346 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c36fb40-e1e5-3af5-b685-f432b87d6e01 | -7.01664 | -48.53835 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb0f586e-f435-3c59-94b6-b426d7b72744 | -7.01136 | -48.54678 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77c28051-c19f-3fb2-8e6a-3e5d3bb6f48f | -7.00835 | -48.54163 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9afe5fba-e476-3232-9d35-8f979f594e70 | -7.00759 | -48.54615 | 2024-10-10 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b378e6b0-66eb-3516-b0bb-f584da356f5f | -7.60129 | -49.39804 | 2024-10-10 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6779bee9-21cf-3f4b-b773-7c6867846dbe | -7.29023 | -48.70514 | 2024-10-10 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a60bfa9f-a353-317c-bcff-811abc1ec694 | -7.62201 | -49.44249 | 2024-10-10 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84830f23-cae0-3c2e-824b-d8f9227a4233 | -7.54066 | -49.49838 | 2024-10-10 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f3a9425-8cab-3e78-b288-64cf5350d6c9 | -7.39139 | -49.64638 | 2024-10-10 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61503f60-66f6-3e71-a596-fd2a8cccfbd4 | -7.11367 | -49.15444 | 2024-10-10 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08eba19e-28d4-33b3-bf91-294850a19f9b | -9.33734 | -49.84748 | 2024-10-10 04:19:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de94629c-7a05-3077-ace4-49c778ad2034 | -9.05527 | -49.71508 | 2024-10-10 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f593e6b-efe8-3696-a413-e6720fc4e83c | -8.07056 | -49.66238 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98035bbc-8316-32c3-a005-b197d3cfa9e0 | -8.01954 | -49.77053 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fee1013e-233a-3a03-b3dc-c06a7d979904 | -8.7909 | -49.66473 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 721108f0-1cb5-3103-b3bb-91c7b14b2e90 | -8.79006 | -49.66962 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a39eae0-a2a1-3ee8-935a-6d693b50704d | -8.78605 | -49.78841 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de259bf9-209c-3399-997d-fc671b4b440f | -8.7821 | -49.78772 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e575af3b-0d8b-366c-a9b2-f2ec517ac00c | -8.75443 | -49.78289 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| adc2fecb-77be-32a4-a2fa-b802a46c7c2f | -8.75135 | -49.77716 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80879ba2-9f74-3dd2-bc3d-f187fd4256f3 | -8.66285 | -49.42559 | 2024-10-10 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b45581-e41f-34ff-b785-836c8c0f6f58 | -8.66205 | -49.43045 | 2024-10-10 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 017fe463-a581-3635-8c73-1a4f851030f7 | -8.65555 | -50.06678 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15385050-2603-301a-83d8-be45f5e78a0e | -8.62975 | -50.19466 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60d0407d-644b-34da-b9af-a665609081fc | -8.6282 | -49.03133 | 2024-10-10 04:19:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f5d85c7-d3c8-3088-86b1-6cfda9e4ef94 | -8.62743 | -49.03597 | 2024-10-10 04:19:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0aa8776-b6b3-3d15-9380-99ed595a3b72 | -8.62574 | -50.0469 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 205e0e8f-0277-36ab-84ac-4e477c6c6147 | -8.57419 | -49.21478 | 2024-10-10 04:19:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f61f7bc9-4efe-3f11-8194-083ff542a5a4 | -8.57339 | -49.21951 | 2024-10-10 04:19:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d8c1d31-c993-3247-9e70-0d6800dd2676 | -8.49991 | -48.64313 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 450f93ab-4a30-3113-bae4-1b10e40edeb8 | -8.49841 | -48.64511 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d8eb8166-b7a5-3b54-b0b0-4d521164445a | -8.4962 | -48.64249 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b221f9cc-6260-3329-9b5b-7f0511a816e8 | -8.49547 | -48.64685 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab3602f0-7bba-33cb-8d97-31d16370c611 | -8.4947 | -48.64448 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7b27593f-d8a3-32a9-9666-99d5d444e41e | -8.49249 | -48.64188 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebf3860c-6126-3d11-a8cb-4155f9a767a7 | -8.40317 | -49.56417 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92e846a0-00e2-315f-98b8-711bd051824e | -8.39925 | -49.56348 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c103b6d-3157-3f9f-b753-23a615199aac | -8.39842 | -49.56843 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 326d0163-817a-3b81-a80d-6816b1b9dde2 | -8.33802 | -49.66158 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08de1a3b-f32a-389e-bebb-855f72d4b6df | -8.32872 | -49.98085 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dadd7dc8-5f1f-3b83-85ee-782519f03a1a | -8.32812 | -49.98439 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 151f8ba6-7dad-38a8-8514-4301b2487578 | -8.32409 | -49.98368 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ca24dc5-faed-33df-9934-043ee6586557 | -8.23623 | -49.76873 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2f2654-c197-354c-879f-35ac187d964a | -8.18693 | -49.18653 | 2024-10-10 04:19:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16cce694-e50a-3cc7-8449-08aeb701542e | -8.18525 | -49.18918 | 2024-10-10 04:19:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fee4472-00d1-3171-a250-3f432fa75896 | -8.14657 | -49.08956 | 2024-10-10 04:19:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd8756f5-9389-3a86-8f7a-0730c42bfdd8 | -8.07366 | -49.66821 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ee6fb99-e059-3a06-8257-283aaeb870f3 | -8.06971 | -49.66749 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb799950-cfae-3863-be53-04b678769b53 | -7.99894 | -49.22852 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7373fa6f-5513-3912-8e11-6d3f35e44090 | -9.90337 | -50.0743 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddaf0df5-4aae-38c8-bc4c-ae296a718bfc | -9.79887 | -50.07415 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9419194-6a57-36e5-bd35-16bcab5934bf | -9.77099 | -50.11695 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2c90442-bcae-3851-8b20-8ad157f8693d | -9.76969 | -50.11529 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52c1a773-51ee-34ff-808a-0daaecde54ce | -9.76883 | -50.12046 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65fb54e1-8032-3c4c-91f3-31c2d907bc1b | -9.76702 | -50.11626 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd7bca24-37f8-3859-9ed7-927915bf8eda | -9.57983 | -50.23151 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ffddc2a-2802-37cb-b916-0deeb04a919c | -9.57522 | -50.23432 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcf38cd5-ccfc-3fa2-90db-c1a0a068ef55 | -10.06856 | -49.55009 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca84596f-dcc0-30b9-ae0f-dea4e0825641 | -10.06777 | -49.55485 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 292a87ec-01c1-37fc-ac20-bd5f7f40bf07 | -10.06618 | -49.55162 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 80b3251c-d481-3c6f-a771-4a267a0643a7 | -10.06473 | -49.54944 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f91be730-09a4-3ee0-8e2d-fdbb1bcaac66 | -9.62768 | -48.99099 | 2024-10-10 04:19:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e8f2fe8-7de3-3765-afd6-2bffb9d75e27 | -9.62453 | -48.99303 | 2024-10-10 04:19:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d9669c5f-b02e-369a-bb1a-4623a299cc24 | -9.62395 | -48.99036 | 2024-10-10 04:19:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eed029f2-f6c7-3e1a-bb1c-da37ae00b83c | -9.62321 | -48.99488 | 2024-10-10 04:19:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 487fbbe3-fe74-32cb-8741-398dc785fe1c | -9.56963 | -48.94854 | 2024-10-10 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a89ab416-ad6a-3f15-8345-2221db80afcb | -9.56668 | -48.94333 | 2024-10-10 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ab768cd-e8bf-3c0d-84e3-5f5b06f0646a | -9.56593 | -48.94783 | 2024-10-10 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f87f23a5-5418-3413-a207-c8d1467994f4 | -10.52524 | -49.10959 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b5f59254-d842-3643-a9fa-9458f24fc63f | -10.52229 | -49.10442 | 2024-10-10 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3321424-357e-3e69-b02b-7f3bde902ae3 | -10.86333 | -49.7613 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 938d681f-6b13-36c2-afc5-0bec690e475c | -10.86112 | -49.75108 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README78.md)
