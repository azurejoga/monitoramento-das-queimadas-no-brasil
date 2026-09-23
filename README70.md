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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b06bc0e-fd32-310f-b288-a0815808c064 | -12.1049 | -50.04092 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea82ea2c-38b0-36fc-8be2-e87986611975 | -10.51524 | -44.87766 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc7f1732-e945-3016-a85a-5378b1e270f1 | -6.88995 | -46.56662 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad75a479-308c-3d21-9262-5e54d0997b93 | -14.63753 | -45.62203 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2118249-db51-3f55-96f2-a22f60bfbbfa | -9.05545 | -45.77694 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| becd5cd5-89b5-30e2-a058-5a471307d847 | -7.48783 | -45.46622 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4536405a-e4a4-3413-ba73-f835d85f9f36 | -6.93118 | -46.56244 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8424150-244d-3fb2-8315-5182dfea8f0d | -8.81398 | -44.26719 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bc1b5f2-05cc-378f-9286-3b6881f2582c | -8.76022 | -45.83718 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be6816f4-e389-31e8-8a34-6031cc481844 | -7.09665 | -52.75356 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bdde718e-ac4d-380d-9125-1c718b2ac0f9 | -12.12322 | -45.63989 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fef43abb-edf3-3d04-80a5-a3e0b731008a | -11.45414 | -50.23675 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e229d9-120b-3371-bac3-4be926a4b5bb | -12.11634 | -45.63886 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5f0bf9-f4a7-39ae-b046-379bd3e7f89b | -5.89543 | -52.28086 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2217d71-e256-3075-b18f-4a186c5cbcd7 | -8.80692 | -44.26608 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 012f7533-0031-318c-a226-346c134ad852 | -10.61664 | -53.99002 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 215bda51-f4f0-3495-a8e0-3e3a8ed36881 | -12.12379 | -45.63608 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f30bdc58-f102-3d7b-affb-9db38a728b4a | -7.13179 | -48.42705 | 2026-09-23 04:27:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 07dad13e-8bea-3309-ba21-30210715d7bf | -11.2602 | -43.41928 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a458890c-c137-347c-b3b9-86056fc6ad0b | -7.9865 | -47.46901 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec49f0dc-9d6b-3485-a7ff-7d94d8ee4178 | -11.9388 | -49.7701 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab995400-4e5b-3ebd-9c1d-38f72f5adf55 | -7.39793 | -55.21671 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83788b0a-6aba-34a1-8595-9f225de2278e | -11.75311 | -47.61765 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff3a10a-367f-3fa1-8536-ed10c666680e | -13.85367 | -48.58139 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31ac7a0c-488e-3ef6-a4dd-45a90620765b | -6.10179 | -57.682 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6c38218e-8fbf-39ea-a1e1-f91df3cee34b | -12.07068 | -50.35345 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0e8d47b-5efe-38c7-80b3-cd6f9b23905d | -10.21494 | -44.15749 | 2026-09-23 04:27:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf88397-916a-3ab3-95ed-817009e46bf5 | -6.19245 | -57.77762 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 569bb54d-62cd-3a8f-9f57-fd390fadd8e2 | -6.78825 | -48.68274 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ee37865-99a7-3d84-b6e0-b5932e8d01af | -11.28897 | -44.04296 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 016d04c7-162f-3a6d-9a17-9f1873a45ce3 | -11.44635 | -47.36029 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49182554-a0a3-38cb-a536-2519b15787c2 | -6.67526 | -58.56898 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1540513a-fa8d-3350-b0c9-d9024ffe4399 | -10.51037 | -44.8538 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d234669f-e4f7-304a-8931-7ecccd277fbe | -11.39974 | -44.05265 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e432171-4985-386a-96d8-e523c6f52169 | -8.80925 | -44.27472 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ff446f36-da24-3e62-85d1-305399dd3176 | -8.45711 | -51.48383 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f44ed407-15b8-312c-96d5-bc04c3ed1d61 | -11.65179 | -43.4399 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 529b32bb-e945-30d9-a402-021407fc64b5 | -12.4374 | -46.99419 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9f2b24e-6013-3e6e-9b67-7f9af59e1f43 | -8.78252 | -45.84802 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21bffec9-1a6f-3976-9f50-95778bc98d9d | -11.35887 | -43.38071 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d1da84c2-f1c8-3ccc-9814-2475b3ce9db7 | -13.92665 | -47.832 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91279fd7-8ee0-368e-9432-164c360a06f1 | -12.80607 | -50.91095 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13c69679-5d1a-3192-8c0e-22f9c746ec75 | -14.62629 | -45.62122 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 236573a1-bb64-333b-a280-faa15c21f2b5 | -6.77693 | -48.66551 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2ac61be-3848-3c1b-af23-dfd5e0de3416 | -8.08607 | -44.33777 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419fef0d-49bf-3a62-a22b-c72691a82e5b | -6.68067 | -58.57544 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61dc9e79-9a2f-3e38-a005-b80697a7b3e0 | -14.63333 | -45.6223 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e1a72a25-7ed1-3c9c-b334-70b9c45d1b0c | -6.07099 | -51.7294 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94ef77f3-f02e-37a6-9ac0-62123a8f7496 | -8.45628 | -51.4888 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a41efaf-4b06-3931-86d4-ebbf09904da7 | -8.37636 | -45.59196 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 369a604c-2245-3415-9713-6ce3f6d81313 | -7.14982 | -48.44503 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39e479ca-3b7c-3d16-8e12-246805375d19 | -11.12632 | -51.05127 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79b558b4-e1cd-3ed2-90ea-36ef41d614be | -12.78471 | -50.90726 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5308ad92-4313-37af-af26-9830a0d7ffa5 | -10.26631 | -49.97607 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faac27fd-189f-34fc-9193-9994e5ed1cb3 | -12.86903 | -50.85778 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 747a9a49-78e8-3f42-a8bd-130bd1b75739 | -12.19754 | -47.02903 | 2026-09-23 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 301a2ef3-644d-388f-9032-443c2ea86062 | -14.63641 | -45.65525 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9bd925a-763a-352b-b3d5-55a62c8ae0c9 | -14.59634 | -45.62928 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 280787f8-7763-3002-80bd-b7abaff6e738 | -7.46583 | -45.50336 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0deb2d0f-b0b6-3591-b74b-d4f78c288f67 | -10.02656 | -45.20134 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f75439-6093-3966-aa96-92b7dbe3013a | -12.04834 | -50.35784 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e73ca3-1745-34a6-a2bd-66b89c5b2e94 | -11.85862 | -49.96106 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba2832e3-23ad-3da3-a994-2328d79ed098 | -10.26148 | -49.98343 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce763479-ef40-39b0-9563-a95c181669b6 | -6.07411 | -57.80328 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f56b74e2-4a2d-3dee-a383-9f47a8c77377 | -6.62246 | -57.98498 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2be5a8e-0c7a-3a28-87c1-ef743c0a6d95 | -10.70606 | -48.70694 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35907b15-a9d2-3033-8dbe-da678e56dea9 | -13.85754 | -48.57838 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20017405-30ee-3493-b073-791b07ca9d09 | -11.86207 | -49.96164 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63324bda-a7e5-3601-b55b-025039b0c32e | -7.32922 | -55.59244 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47c41c2d-67f0-3161-9d7c-1f10324f2bc2 | -11.89021 | -45.76802 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 09940e23-3ca8-3a7c-892d-9fe6d295f35a | -9.06974 | -46.52385 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc78e0c6-e3bc-3d7d-8860-03ac2d5f566c | -12.78025 | -50.86828 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69781dae-1011-36f4-a413-418bfdd43394 | -10.41826 | -39.58869 | 2026-09-23 04:27:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e19f8fd-122e-3eed-8cc6-bd617e619a0e | -11.68582 | -43.44196 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e499e1db-540a-3542-bdfe-6e31af711883 | -6.67429 | -55.06575 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e749ade8-f944-37bd-90ed-5ef7635d333e | -12.42127 | -46.96607 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 58963173-12cf-3406-b5e5-28ffabb2406a | -11.1548 | -42.845 | 2026-09-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8e37764a-97b2-3dba-a75c-e8c861bf457d | -10.69246 | -48.72722 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cb57199-a0d7-3198-a645-292320d48370 | -11.84197 | -50.1501 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3f86964-6282-340c-842b-1902728f67d6 | -6.66504 | -55.05853 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50ca035f-445f-3f58-a1d9-adbad7fb8e24 | -10.70706 | -48.72203 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 637118cc-d28c-325b-8520-d053ef2c6644 | -12.10555 | -50.03705 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a873985-8bda-3562-8c38-d63a9fdc6dac | -12.77887 | -50.87652 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7c352f2-7039-33dc-83cc-b9c5ac43c5c8 | -12.79045 | -50.91677 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c08cb31-f425-34a0-9b1f-53d5ead4042d | -10.31239 | -50.50592 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c674f3a7-d5c1-37b3-8dd4-0cffd0490628 | -11.65916 | -43.47017 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20672eb6-216a-33ba-9757-f5a67b457cf1 | -11.40342 | -44.0532 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2034bee9-2a29-3d8b-978e-53215a427448 | -7.55807 | -55.01551 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a83b3be-e2b6-3446-b8d8-00a561d4a88b | -12.42181 | -46.9625 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| efcee0cb-7022-3ad7-8244-07d13c551ec5 | -12.41189 | -46.98283 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c05c78e7-f68c-382d-9911-aeee892fbeca | -14.6069 | -45.63087 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 218f07ae-2fd1-3467-9f29-5cb8e58c6fb1 | -7.429 | -49.83465 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 103f8324-f147-3dc5-861a-c3cbacd708a4 | -10.70941 | -48.70747 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 630a9179-3fee-3945-bafa-d15b0d7cbb37 | -8.48585 | -44.74953 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e85e9023-b5c5-3c65-b078-e22fd4f1e719 | -8.48641 | -44.74573 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29dec7aa-813b-39e6-aeb8-5f6753842c01 | -12.05625 | -50.08502 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9384e0a6-9b85-3cab-b865-6c73f4c01b13 | -11.09395 | -48.34599 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2967144b-880c-3984-ab1b-a41c6faa9916 | -6.13056 | -52.76549 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15a666d-be14-3730-a8db-9d5092d10876 | -14.63584 | -45.65931 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1413cbb1-44dd-3522-991e-36f938ef6862 | -14.38301 | -47.25007 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README71.md)
