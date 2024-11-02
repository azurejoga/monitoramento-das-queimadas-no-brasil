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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 981f46c7-a0f7-3e28-852e-c142d9b7782c | 0.03115 | -49.53357 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8020159-e141-36b7-a613-5dae6f96f34e | 0.0288 | -49.5346 | 2024-11-02 04:10:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60974e31-7898-3ecf-ba32-e92dbd0d904c | -2.07329 | -48.82227 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbdc483f-e8ef-34f6-aaa3-9652c2f34f45 | -2.0584 | -48.8571 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63e80ca4-2961-3e05-91d8-1e075a30c0fb | -2.05766 | -48.86166 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54353d8d-a74a-333e-84f7-4721ac5811b2 | -2.05388 | -48.85636 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9a55b58-01a9-311e-b99c-ed52688ebc2b | -2.03642 | -49.71785 | 2024-11-02 04:10:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1f360e1-5552-31b8-b483-85f1d79a3f80 | -2.23457 | -48.84834 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b70e05ec-a19a-3147-bffd-4b9fe03d1cce | -2.22781 | -49.14562 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23aceee-f614-33f4-9696-956a32e33ebd | -2.22321 | -49.14486 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f19c62-4540-3658-9cde-8295aeff82c3 | -2.21169 | -49.15763 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 245e0f0f-8628-3f41-861d-64d84ea0fff7 | -2.18804 | -48.98289 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e5a77a-f80f-39bf-bd13-bb19aa4f6cfd | -2.18731 | -48.9875 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c732cce-998b-3928-954b-0d71f1b263c4 | -2.14926 | -49.53877 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 090b2166-89fd-3541-8929-8b1564b248d7 | -2.14659 | -49.12468 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2000822e-d9f8-3401-a777-30c422763b96 | -2.14583 | -49.12941 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c617f91e-dd1e-3828-8c17-4b6c42d94706 | -2.14537 | -49.53292 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f9fe9ef-bbc2-3066-85b2-6dc7d27abe76 | -2.14148 | -49.52708 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d8b784-b5d5-3a01-814b-9c335166bd92 | -2.14064 | -49.53213 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a917274a-3d31-3a13-861b-b030c95dd67e | -2.13579 | -49.52361 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce55949-c3eb-3043-8591-f2dd58948f9d | -2.10351 | -49.51321 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 504227ee-c1c8-3c6b-b7d5-d892802559b7 | -2.0729 | -50.34841 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5fcce19-c8ab-3ccf-a690-c4954c8f8038 | -2.37805 | -49.66928 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 612b865a-f8ba-3c86-9dc8-288b93f94881 | -2.37723 | -49.67438 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 279ca308-bcc4-3f3e-9eba-501208d88167 | -2.37003 | -49.10843 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1534390-f57b-39d0-9c50-09180df24e5a | -2.36729 | -49.33294 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f677eba2-5e7b-3c39-89d1-7cf8403d70af | -2.3662 | -49.10305 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63f00733-9259-3da6-93d9-cd681117c525 | -2.36545 | -49.10773 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f84c3c3-f335-3b29-aa10-77128d3b7173 | -2.35529 | -48.91215 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4115d830-7547-35dc-8645-9ca48cace16f | -2.35484 | -49.17357 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7919aaa9-e099-3bab-9915-e1bc8562dbbe | -2.35408 | -49.17827 | 2024-11-02 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 573533fe-c860-34df-953b-c070bc432398 | -2.35227 | -48.90232 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547b6775-3aa3-37be-9f0c-3c42e84c4081 | -2.35153 | -48.90686 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c582d2e1-75b7-37a2-966d-ebdef1ce98c5 | -2.34776 | -48.90159 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b61c6a40-88a2-3b12-9e2f-f8db51afc565 | -2.34702 | -48.90612 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2709d80-7897-3528-8823-457f0fd1076f | -2.32588 | -48.94232 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16d6254c-bb19-32ea-bf46-4aca3ecffefe | -2.32294 | -48.93956 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e68d011-20cd-3e7d-b3ff-b9595c3ead95 | -2.31766 | -48.94337 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b4aec86-bfba-3c7b-9fcf-25ad570d05cc | -2.21764 | -49.57253 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1dff0a8-76d9-3ec0-b286-01738e6db514 | -2.21696 | -49.57057 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1202daa-94e9-3f48-b65a-424f299ae838 | -2.19562 | -50.31827 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a85b0702-8661-3412-a0bb-61817606ef23 | -2.19064 | -50.31744 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0807ef5f-3f4f-3750-842f-1472912e9cd1 | -2.15767 | -50.14438 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eecf1f6-5edd-333f-8553-7d57916d86cc | -2.15274 | -50.14356 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5e33e62-a6d6-325a-8a98-bd99f64cd66d | -2.14781 | -50.14277 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe19efd4-3197-363c-bf5d-6fbd31d77d76 | -2.14689 | -50.14835 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edc59903-e2d3-354b-bbd2-262671129566 | -2.12224 | -50.14426 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98ea7bba-dfb8-374f-94cf-86875c1671b1 | -2.12106 | -50.14278 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d2ce592-661d-3835-9309-cfa05c26b62c | -2.11731 | -50.14345 | 2024-11-02 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 641b0c05-dc5f-3b43-8493-fb0f5808766e | -2.56988 | -49.12236 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e37a861-3344-326e-bb22-6be67dd221a0 | -2.56757 | -49.07906 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccd7147f-0dc8-3105-ac2e-0d42302c4314 | -2.56591 | -48.97538 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6449aec2-e8cd-3a37-9d9a-e1b1a3aa98e7 | -2.55989 | -48.95561 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ded7ca2-d910-370c-bde7-4b104f5bfbd8 | -2.55389 | -49.22086 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc896265-1292-3221-a891-aa3724f6f94e | -2.55389 | -49.13421 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18139791-7319-3d51-93c9-6e4e2e133cf7 | -2.52242 | -49.24015 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c52d3b93-22a2-31ad-8e38-c56de01b4ec6 | -2.52164 | -49.2449 | 2024-11-02 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 73fc6dcd-fa29-307c-b92b-2a88e9aeab6f | -2.51781 | -49.2394 | 2024-11-02 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14eaf32c-f93f-30a3-abd4-213144138e92 | -2.49232 | -49.07878 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e32f3d73-6b8c-34bd-8598-26ee9b3949ff | -2.49157 | -49.08345 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 37d753ac-9f0a-361e-b3f6-e625e69b1d3a | -2.48777 | -49.078 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 04b17bfa-332b-3a6c-a1d4-ce7c34891fbd | -2.47464 | -49.61914 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8649eacc-fb19-31c2-bec5-d95ada7fcf17 | -2.46135 | -49.7904 | 2024-11-02 04:10:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b694a4ea-b1c7-3838-bc59-47755752fb21 | -2.44298 | -49.00914 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c01f2dee-5010-3598-9a04-7f85f9797aa9 | -2.43092 | -48.96959 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3be0d051-04c8-322c-b39e-730257fcedc0 | -2.42881 | -49.65674 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ae5ace7-b864-39cc-b4d3-68dc1d99842c | -2.42447 | -49.6578 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be56f98b-eb1e-3036-9ff3-0f10bfb2b113 | -2.42406 | -49.65596 | 2024-11-02 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b2d47a9-77ad-3b77-889b-a21d4fd4e94d | 1.79235 | -50.44069 | 2024-11-02 04:10:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc17b122-0b23-38ae-8b52-f37fbe9a4a16 | 1.79031 | -50.44298 | 2024-11-02 04:10:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfba0fe0-4d43-3324-aecf-813e27423c02 | 1.78981 | -50.43958 | 2024-11-02 04:10:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bd7a27b-48a8-3745-b3ba-2f937758c38a | 1.787 | -50.44157 | 2024-11-02 04:10:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9248059-b07f-3eb0-b365-edb97e7eb83b | 1.78648 | -50.43819 | 2024-11-02 04:10:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38c09717-8745-3335-bda3-a7a64aed998a | 0.10061 | -51.24851 | 2024-11-02 04:10:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1aa9e91-8d93-364b-aad3-ec932624f19c | 0.10052 | -51.24905 | 2024-11-02 04:10:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ddeffba-7b85-3f1f-937d-c67668c20cb3 | 0.09993 | -51.24542 | 2024-11-02 04:10:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de02ebde-5ba9-34ea-80ac-3e731b866bba | -2.26302 | -50.44211 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e8470b-9b28-38d3-a93d-64e8cd8fe622 | -2.25799 | -50.4413 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e372fed-02f9-3f6e-bade-b24f4453c7aa | -2.25753 | -50.44417 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2374ab6d-c1df-3c21-804e-3e72a5251da0 | -2.25706 | -50.44708 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f422b923-9de9-3e4b-b259-c01b5230fce7 | -2.25658 | -50.44999 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a757348c-6f77-34b7-ad3c-0a6e99f795ea | -2.25297 | -50.44049 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2225356-9440-3c91-b369-a0c87d0e007e | -2.2525 | -50.44337 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da34f69-423c-3078-b153-11a430e117b5 | -2.25203 | -50.44625 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 134d3e7e-5313-3c72-8e7d-3d17492c4e23 | -2.24889 | -50.43386 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9004fd2-0052-309f-8e05-d7542310ccc2 | -2.24842 | -50.43673 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8efb6ccd-2452-3e53-96c9-7c2fe9a21fa4 | -2.24795 | -50.43965 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67549e16-8814-33a2-9bdf-b1b68c5229d1 | -2.24748 | -50.44254 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85117866-6500-3675-8ee5-ac7ec6f03b97 | -2.24339 | -50.43596 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aff6cc6-97f7-3b5c-9324-256a4e850af5 | -2.24292 | -50.43884 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b052b14e-1dfc-36ab-a69b-583e9aac7c92 | -2.24245 | -50.44174 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aec255b-89a1-33bc-9f97-84729c22fd45 | -2.18952 | -50.79839 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ac1c15f-a559-320e-9608-4d1fc8c27dee | -2.18902 | -50.80149 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97230fa2-fb3f-36fd-8b22-7b86651be229 | -2.15522 | -50.91067 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87222c27-b906-345e-92e3-99a5353458fe | -2.1459 | -51.00018 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce952a4a-ea6e-3fc7-a40f-54450b559538 | -2.1427 | -50.82537 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e64e0dcb-4296-3efc-9551-10665b7e7bf0 | -2.14016 | -51.00243 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5124fc73-be37-3502-b296-740bafb7e194 | -2.13975 | -50.70045 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ee0d929-2a2e-3235-ac96-6e8ee26d26b3 | -2.13927 | -50.70349 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc257bb8-3485-3a0e-80fd-96225359c36f | -2.13701 | -50.82766 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README34.md)
