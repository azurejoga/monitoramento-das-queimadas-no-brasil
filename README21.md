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
| 18904cb8-8f2b-3011-8ac9-47835d95dcf2 | -6.16421 | -44.05972 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89b639c1-dc7f-361d-88af-9dabf23d7c0b | -9.19435 | -44.43652 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd2d7287-3461-36a8-8f49-cdf36a6ba65a | -8.08377 | -44.98632 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ee662b9-ed65-3f84-a47d-1cf2e1767875 | -6.22695 | -43.35915 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7097a90e-580b-32a7-aa89-6c3b431ec5ec | -4.40328 | -40.49026 | 2025-08-28 03:45:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c15c6f1-4fe3-32ea-873b-bacd55f8ba9e | -7.17778 | -44.8734 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cc06f81-2639-3b09-a789-7b662cd5555e | -6.85902 | -43.61726 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf961b29-39c8-3118-9298-a455b6631b56 | -5.68812 | -40.97665 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a86c8c1e-f0e2-3b6a-835c-21a7ac3d959e | -6.94965 | -44.08611 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acdeeee1-2312-3ff4-8941-a573999bcda3 | -7.05956 | -44.3687 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5c448cc-fd3a-324f-82a4-c442844624d8 | -6.28098 | -44.48497 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45263b1f-8afb-3981-ba5b-c3f3b7f29faf | -8.38648 | -44.97251 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 014d7e71-91e4-30a5-b664-30a118777f5c | -7.39585 | -39.69481 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a129d2d3-1709-3af2-a13b-9adedaddc42c | -6.4397 | -44.57417 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1feeb216-f3eb-3e1a-8fe3-76159daa37a4 | -6.43766 | -37.13266 | 2025-08-28 03:45:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 03f23f0c-25c3-3d61-be4a-f3061a787272 | -7.05697 | -44.36845 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 144f77aa-7ba4-33ac-b0bb-64a0213e3641 | -7.45923 | -39.96282 | 2025-08-28 03:45:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5b0d8c1-6822-3491-b0f2-ef0b0f8317e5 | -9.18984 | -44.43563 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3871a1ab-9d39-3b71-9bf0-129c452cd6cc | -6.33094 | -43.75433 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7568c03-89ce-360f-baa5-c0a0139d68bf | -7.75161 | -44.04988 | 2025-08-28 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d58f18ff-b95b-3d60-b790-c62a2c46d381 | -6.80671 | -44.35119 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab39a5e6-3150-3826-b48a-bdea09693452 | -8.4434 | -41.45027 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 246cce50-e49b-3931-bac8-9b5ccdc557ea | -7.20129 | -44.06116 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 986220dd-43da-3c6d-a334-f7114c3a3743 | -6.57129 | -47.37802 | 2025-08-28 03:45:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af86c92e-a0ef-3d0e-b3e2-6df125da3b6f | -6.15593 | -44.3898 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bc33792-fdad-35ab-a8cf-89125a8f159e | -6.44581 | -44.57148 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37ce69bd-2b3f-3258-bf04-cfb3eb4ecafa | -6.28163 | -44.4814 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bae5122-c4e0-36fd-986a-d7499f763447 | -7.42463 | -42.06136 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51a4e807-9d2c-3fcc-92ae-ab5d29cdd9a0 | -8.0914 | -45.0066 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dda9082-37be-3919-a830-6e3ca44382d5 | -3.78367 | -45.03853 | 2025-08-28 03:45:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbaddcad-8504-3030-b49a-b6902c46bb3a | -9.19556 | -44.43361 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1d0ac66-4c8d-3826-973a-d1605cdc3f8d | -6.07651 | -44.00821 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cef5431-026c-308d-94fa-894504fc8785 | -6.87695 | -43.62083 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d02b0d3f-58fa-39db-9ace-913c115eb754 | -7.94539 | -42.65397 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 765ac1dd-8f55-3a83-81ae-15645168be10 | -5.07106 | -37.71693 | 2025-08-28 03:45:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c084e234-2599-3a61-87b3-5409a2a8760c | -6.88767 | -43.61957 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6b3876c2-3a4b-39f2-a72b-4d8798f48018 | -8.43701 | -43.67524 | 2025-08-28 03:45:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47a97132-20a8-3efc-a253-7cd8e65dc8d7 | -6.28004 | -44.48513 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8197df0-dcc3-38f1-a914-77a4a097206d | -7.40135 | -39.68571 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 31f87da9-848f-371c-814f-7f765429886a | -6.87104 | -43.59525 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c33e79c-dd45-3d22-8c0b-ef793bba4d3a | -6.2645 | -43.82732 | 2025-08-28 03:45:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15130194-5b12-3269-8c50-ab51899f7eb6 | -7.62681 | -42.70741 | 2025-08-28 03:45:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dc3684f-4293-3ead-b901-96aa0ab9663a | -8.45098 | -43.65415 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b95c99cb-fc47-359b-b801-84f2125681fa | -6.08233 | -44.00616 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ea07e16-ac5b-3905-a9b8-2da05bbaef76 | -7.62647 | -42.6814 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1898348d-d9bd-3f93-9c71-c5909e255f65 | -6.87561 | -43.59897 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e56774c8-377a-33df-952d-b78e2b06101e | -5.54924 | -45.37442 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8df418fd-86cb-3727-8627-7f2c84664558 | -5.74523 | -40.4472 | 2025-08-28 03:45:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20c245e0-f8e1-3e57-a678-e14332a7508a | -6.46058 | -43.72117 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd39e272-ebcc-3fb5-9f3b-8711ee317c7d | -7.94073 | -42.65303 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e094a34c-3831-3c16-8595-84174fbecca7 | -8.44412 | -41.44619 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 584f5edb-150e-306f-b430-a2b8c1950954 | -6.86968 | -43.63212 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e271b78-a1ef-30b7-905a-d3c91a838d07 | -3.2343 | -43.44394 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 904d198f-544f-38e8-8ea4-44bf1d7bddb3 | -7.2014 | -44.06185 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf0a36ee-ee81-3582-ba69-03a6bab78b32 | -7.63848 | -42.66818 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad6fe569-794e-3f83-aed1-ae5abaff4459 | -5.68379 | -40.97589 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cefb5509-c71b-3e4e-8339-228bb02e1a73 | -7.26023 | -45.3558 | 2025-08-28 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 80514534-79fa-352f-b9ae-cfcff46fe72b | -7.78969 | -43.18139 | 2025-08-28 03:45:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28d2fb4c-702e-33ba-b7f0-6e38c1563310 | -6.44269 | -42.41931 | 2025-08-28 03:45:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 34d68127-7456-396d-80e1-598ccddd0224 | -4.79001 | -47.26256 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d92aee-165e-3ad3-9d44-5f4e3f0c83c8 | -6.86674 | -43.6192 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e36d768d-ee7b-3c2c-8514-dffe8d30ebae | -7.63206 | -42.67723 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 66921fd7-047a-3d7f-9d27-c0ff25affa27 | -5.20832 | -44.31885 | 2025-08-28 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecb4e409-47a1-37e8-88e5-051ef3a66014 | -8.02176 | -44.79782 | 2025-08-28 03:45:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f071f53-2860-3b34-8174-7a381047c9df | -7.40054 | -39.69059 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c008e2d8-2d4f-3415-80b9-319b78437e6d | -8.28959 | -47.21802 | 2025-08-28 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cff1c058-ca92-35bd-89cc-f35feb98bf3e | -7.39666 | -39.68993 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 73ce5bbc-3d77-33da-a225-c336f6f40310 | -5.19455 | -46.06884 | 2025-08-28 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3a922e4-3087-36c6-944b-86613e985838 | -6.26398 | -43.83033 | 2025-08-28 03:45:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b90bf4f-f642-35de-8ae6-5aff5153cbf8 | -6.18928 | -44.01051 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 980f2f05-3e5d-37dc-bd38-cdcf4029662d | -6.07704 | -44.0052 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7950d959-92a4-37d7-985e-bf4b56c36574 | -6.18451 | -44.16258 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1410f84-d19b-32b2-be32-e1cff1108bf8 | -6.15651 | -44.38647 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd291bf-3073-3320-ab8d-bc343eee00ba | -7.17713 | -44.87218 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a1128c1-3d0d-3efd-b419-927af7d8b46d | -6.17798 | -44.16843 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 450ddb71-8a8e-3dcc-a1ff-141fab10afe8 | -6.86057 | -43.62437 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c06e3618-a170-3196-a2d2-bef1f00105be | -6.17872 | -44.00863 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b74a2c2-b1d1-39eb-99a7-e4cd3e5aedce | -6.1585 | -44.18519 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66926546-b680-3120-8c1c-a120be198ba0 | -6.82175 | -44.35982 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 990e01c5-8da0-32d9-ab2e-ca2e762d544d | -6.88366 | -43.61264 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 7c781e06-7802-30af-8092-7cfe44baba4b | -3.23537 | -43.43738 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91002c8a-0af9-322f-88f6-34baa51283d8 | -5.69347 | -40.97604 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dbea89c8-1142-3372-8648-80eb8e6529a0 | -7.39359 | -39.6844 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 8df0c152-5060-3ece-82b5-0a433879e9b6 | -6.88204 | -43.6217 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a69f0af7-8dd2-34f9-bf0b-c71c841a89e9 | -6.88071 | -43.59977 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b73c87bb-42eb-382c-89e6-41439e48c6c1 | -6.08179 | -44.00926 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26802477-1aa1-32e6-8ffa-ddadc398e753 | -7.24506 | -39.18145 | 2025-08-28 03:45:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a37d9747-c6a5-3025-8d23-27a334e963e4 | -6.16894 | -44.06393 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d77cb870-3636-3feb-bcfc-2239bf3cccb4 | -6.43798 | -42.41843 | 2025-08-28 03:45:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| af9d38cb-3e7e-3443-9683-a45945ad6789 | -6.87911 | -43.60873 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 94c8c987-defe-3a7b-92a5-27d27351fdc8 | -4.78807 | -47.27351 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f824be9-332f-3b53-9437-2a52a905e5e9 | -6.15051 | -44.38881 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3208965-1a24-33fb-9198-416dfa6aee22 | -7.62594 | -42.71244 | 2025-08-28 03:45:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6b92513-121f-37ae-9ef7-8a5f2eb36df6 | -6.18874 | -44.01359 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 650630f5-aea8-3a42-8a56-58a1b34eb4d5 | -6.22595 | -43.36498 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7651873c-ed9c-3627-92f4-1d4188d2a661 | -5.90128 | -45.56481 | 2025-08-28 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b452946-35d4-31fc-b1dc-6d8d51fa22ee | -6.19706 | -44.15365 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33d76f3f-320c-39e6-8e47-b81b9b522b93 | -6.81098 | -44.9983 | 2025-08-28 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db0b92a5-fa41-3163-bf64-d72dbaf6cded | -3.88556 | -41.03262 | 2025-08-28 03:45:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff7c88fa-fcb6-3ba9-ab8f-699e122cefec | -8.47245 | -43.64836 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README22.md)
