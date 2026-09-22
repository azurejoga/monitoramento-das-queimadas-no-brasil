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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cda393ee-bc9d-32b3-a9cf-6b834df63e75 | -6.73673 | -55.09162 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3eb93bb-20b9-33ec-b166-7c8a509f6666 | -8.79751 | -48.72985 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe8a204-295d-3b31-bf71-c8f8a093aec4 | -6.87343 | -42.86921 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2066c15e-e51a-35be-ad92-d7aa4ae6501b | -6.25454 | -47.63839 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3674868b-924d-3ea7-a569-3f37c3c5d153 | -3.06091 | -54.40358 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef3d9af1-03ee-3f46-8773-832d566a3e33 | -3.22223 | -53.9474 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3659527a-3915-38a8-9538-17a56d84c837 | -7.59145 | -57.68507 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08fd600b-df96-3ec0-a219-5eeee5cc0935 | -7.5849 | -57.6711 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6f507e8d-4abc-35e4-ad3b-da6ce30cd67a | -9.97378 | -50.2577 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e667299-a08d-3035-9df1-ac985b8086d4 | -10.87143 | -50.16132 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4267417f-343c-398c-81e2-df7e4def231a | -6.67167 | -50.937 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbea7a58-6394-3879-9b0e-4ade59dc4e87 | -7.42326 | -49.85095 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99525763-86b2-3224-9e80-b1aedfbd23a6 | -7.59216 | -57.6809 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abdba924-740e-3129-9bac-31d9536cbb29 | -6.73969 | -55.07333 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 571c6c47-9c34-3f20-80a3-15f227a98255 | -9.68728 | -54.32399 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d686447-cb1b-345f-8d64-bf097e167871 | -2.95346 | -57.7253 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c61d4c0e-8a6f-3e70-9fe3-49291949f81c | -9.29574 | -58.91754 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e195bdcc-829a-351e-89fe-10c0ba88911f | -6.38144 | -60.01288 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953f0f21-6795-352d-a5ef-e308f635c3f6 | -3.50932 | -55.4894 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fa30cd4-feef-3ea3-a3d0-6f55bf8129cd | -11.38322 | -47.11156 | 2026-09-22 04:46:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7abc49d-d30e-35cb-ac23-f8afa5ffba40 | -8.80043 | -48.75945 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d308b0c-614c-3cb2-9bcd-a503a95113f2 | -11.34702 | -43.37917 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c64857a1-abf2-3bf9-a6e8-2843d919cdf6 | -3.78338 | -60.74753 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5738e3ee-f147-3423-b2e3-9cbfed1f8a2a | -8.34379 | -50.87499 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2242362c-b59a-328b-b1c3-0bbe1d5ddd9f | -6.01064 | -45.24689 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4f75661b-209b-3da2-9857-cfe6c64cfbb2 | -5.64878 | -43.36445 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e7fa913-14ec-33ff-9f09-64c2e5b495cb | -10.45437 | -51.34207 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8127bc8-72e0-37d9-8363-cd7700a48afd | -5.23041 | -49.30344 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa10a206-4771-3d02-a839-8fb954071856 | -5.82969 | -52.05286 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfec4f90-db5e-3473-b5c5-8dac8dd2cd80 | -6.5722 | -44.9008 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e026e2be-390c-3f23-bfa7-802556a9c309 | -6.01147 | -47.90921 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2182c47-c6da-3315-94df-bcb506d59cc1 | -6.98565 | -52.85673 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ece252e-8eda-3d6f-a0c7-9421aa8bb4e2 | -4.07915 | -55.32175 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff0cf7e5-94a7-3a4c-8634-582745556823 | -5.88178 | -53.63907 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7599b8be-eed9-300d-b394-c32087d3e5c8 | -3.90535 | -51.8907 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 116f2427-c835-3039-bd20-34298e66b383 | -5.8789 | -53.63461 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed21b942-1239-3590-b5d9-e3cc1fa2566f | -8.14052 | -46.82406 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1df5990d-a187-3048-ae09-2ebfea4435fb | -6.31131 | -57.74404 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad08abe9-71d3-3281-88e7-e76b86a4776b | -3.23634 | -53.95253 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 54d19aac-d92a-3080-a444-1906ac75ee36 | -10.37944 | -48.91225 | 2026-09-22 04:46:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 479badf0-c7d5-3449-a07a-e0a1876b670f | -6.09898 | -57.68229 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 135dd37a-a6de-37ea-8d68-63a096090c48 | -11.41417 | -45.36907 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d867688e-ba2d-337f-a2e7-522bc0638bb2 | -8.80295 | -44.2752 | 2026-09-22 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de010870-a679-3951-8abb-0b7c59de2fa7 | -9.30117 | -58.91358 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68e16d3f-e5d1-3bdb-b760-41eff0fb7d9f | -6.9328 | -42.89001 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2709d784-8151-3d35-aff1-b55e7f41ada0 | -2.95504 | -57.71538 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9c59f6cb-fedb-3b2e-8442-560e0539ce1e | -7.06721 | -49.91146 | 2026-09-22 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c40b093c-e6aa-300b-a7be-5e5bf5b168e6 | -9.24174 | -57.14594 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a0c84a-40ce-3d97-8482-1dd2b9d8301d | -7.4239 | -44.7275 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d8b350f-c386-3cb2-a662-34c7cf048b00 | -5.89516 | -52.09193 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eab838de-763a-3424-83b7-5b7284018521 | -6.64573 | -50.06985 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0a26a25-f3ad-3827-b55f-57d22b55ee91 | -11.09473 | -48.32527 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5621dd90-87de-378a-bf1f-89cfa76f4800 | -9.24457 | -57.15381 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 450e33bc-e299-31ce-98a2-7cbefb37248b | -6.59636 | -39.13786 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| dc3be31b-9b24-395e-b836-243051f58554 | -4.70518 | -48.30906 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e949eac8-55bc-3949-ba8f-520f851b0840 | -3.44159 | -50.66502 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f01db35-ff8a-3388-9b0b-44ec11b4f4ae | -3.07023 | -54.3985 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91086b98-c959-307e-ac5b-9c958321a0d5 | -3.44524 | -50.26838 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71f674d1-82e4-3327-8955-c79a399e51b5 | -2.9653 | -52.14113 | 2026-09-22 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d14d4fb7-74c1-352c-b063-64a0fa1a0444 | -8.10426 | -55.35459 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e586a89-5b01-34f7-ad3b-a07936b6bc4c | -7.05264 | -49.91668 | 2026-09-22 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fe97dff-6758-357a-9cfb-9f0215302c74 | -11.10357 | -48.31702 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bc3a2bc-fe3f-3886-8b9a-f917d9fa8a21 | -8.25223 | -55.24838 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff36a9dc-f696-3b87-90c3-50dda59f1a11 | -8.62577 | -54.62389 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfd3e598-6482-30d0-a20e-7ae0a49658f2 | -5.86743 | -52.02992 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b4a5e51-41c3-391d-b027-22ac102a3d08 | -5.65171 | -43.41334 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0790a8ec-96d0-32d2-9781-19d6a97201c1 | -3.93254 | -56.05078 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acbbd8ac-6995-3bf0-8496-ac41d0a9a716 | -5.87125 | -51.9411 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672113a6-c74a-3d2d-85bd-0c6926d424fe | -11.34662 | -43.38239 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e4f8fdb-68c8-363b-8685-11961e38c3b0 | -7.2369 | -55.59635 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17711e53-edb3-3cc1-bf32-c1c684edfb27 | -9.97038 | -50.25718 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d29b787-14e3-3520-ab6e-9f4eb505fa72 | -4.18423 | -51.24351 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 584ce931-4623-3995-abc2-2ac05c9f45ab | -6.42476 | -59.97861 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18f9a0f8-e0c1-32de-bd30-5cd1337debd9 | -10.83935 | -50.14085 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20b42237-62cd-334a-ad35-0525c7851cb3 | -6.06647 | -57.8698 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43c5300f-f1d0-3a37-9f91-d54012ae3f18 | -6.24174 | -51.01085 | 2026-09-22 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1769107-00fe-3d76-820a-f2762305b5bc | -7.37547 | -45.42703 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8f3aa77-bd8e-336f-ad5d-c647350d5e4b | -9.58071 | -55.11504 | 2026-09-22 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fd070cb-011f-35f2-9cab-f7d29e3422f8 | -5.8304 | -52.02787 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9be429b8-e78c-3c14-be3c-7b27aaf6c057 | -6.35129 | -59.96368 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b6263f-7175-3b26-8ca3-dcc59777d71a | -3.11816 | -51.59777 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630e9365-40c3-3415-b6da-9cc5d9352892 | -11.1488 | -42.83918 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10628eb5-d5b6-3ade-bac4-6bbe307b1e3b | -6.65042 | -59.92343 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f105de84-9747-3f6a-ac82-381498ac6c9b | -6.08894 | -57.69471 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2f65ff1-b7df-3e04-a786-1e2bfa925f28 | -5.87295 | -52.05969 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15da98e9-06d3-38fa-94d3-007c5cfa6e74 | -3.55715 | -50.29259 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca78228-1a9e-3021-92c9-0eef51683c61 | -7.4227 | -49.85457 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43505dcb-e68c-3515-86d7-7901fe60837b | -9.23854 | -46.15773 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ac0f1d7-7960-3351-aee4-4b4a5df7c2c8 | -3.48086 | -59.57742 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ff6735c-1a73-3510-8aaa-5844f49a05e8 | -5.8355 | -53.54808 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f59e7c50-c452-3c2f-95d1-f0c875a77d10 | -5.46627 | -60.21815 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fac2c31-5377-3dfc-993f-ff2f6e54d247 | -9.23801 | -46.16158 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7deefc23-5405-3827-b211-787f7f681fd9 | -5.83913 | -53.48151 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4199a6a-0265-34c0-bf36-cb500d1ffc4a | -8.61377 | -54.63028 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ac8d1b3-c59a-383b-8ef6-d77f77499191 | -4.94739 | -47.47029 | 2026-09-22 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eaaff7f-43b5-3354-b7d3-b88f0ccaffa2 | -3.87267 | -51.19082 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22f1c33d-9c32-3576-bb78-1f101f46d516 | -3.48643 | -54.68232 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c17df2cb-6a4e-3922-95ea-8f1458f411fd | -6.67997 | -50.94891 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2abeb41-3115-366b-bc60-ac51c9dc5631 | -3.34167 | -59.86825 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0fe628a-ba35-3b64-ac44-0d0eb21872b7 | -5.98973 | -44.7279 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README51.md)
