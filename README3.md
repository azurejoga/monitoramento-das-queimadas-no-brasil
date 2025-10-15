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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c21c27d-f29e-352a-b7b3-4fc701fb2159 | -11.51723 | -48.22662 | 2025-10-15 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0c8f54b0-2ef0-3d7b-9628-7b33d9eae787 | -10.90369 | -47.93771 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e0e5282-4d44-3959-b18c-cad65134d0dd | -11.02135 | -49.04461 | 2025-10-15 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cc9dd04-e8d3-33cc-accc-0fa49d8ba3b8 | -3.73602 | -48.36031 | 2025-10-15 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| aae40e6a-2cd6-3809-a1e1-cf59a5f757fd | -4.601 | -47.02988 | 2025-10-15 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9c8b99e1-784c-31fc-ad4c-05112f6c90b5 | -4.3586 | -48.19866 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8f06a8d-b673-325f-b8b1-ed6b34b86a7a | -3.05228 | -44.70799 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bf15ff0c-0cd1-35b3-b377-cd288b77598b | -3.59288 | -49.44071 | 2025-10-15 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b2e3816-7df9-32c0-9ab4-93496e62967a | -4.31432 | -44.53875 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 974d4ed1-c684-341b-a4fc-ebb2edad7688 | -6.34051 | -44.02251 | 2025-10-15 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 6a4b475d-fea0-3b5f-b797-a29169187757 | -4.01576 | -48.97405 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 949a6094-e5b5-3639-8c62-0fad4d1477e4 | -5.03317 | -44.74731 | 2025-10-15 00:35:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 3d63918f-deba-3460-8947-70701266e82a | -2.92556 | -48.29303 | 2025-10-15 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d4b46b77-9f67-3adc-a081-74b458bd48e2 | -5.88228 | -43.75639 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7055c24d-2d69-335a-a725-cdcbb7844b21 | -4.90486 | -43.46797 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 61372a0d-50b5-3a5a-85e2-cc51cb3bee8f | -6.88449 | -43.97 | 2025-10-15 00:35:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 1620297b-9189-37cb-96e9-9bc3db93f14d | -5.39323 | -45.45421 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 525cfd12-f6ac-375f-bf94-7f587cf2f034 | -8.21726 | -44.02827 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d9424c4b-c3a0-33ca-ac0c-43ad7306a86e | -5.60492 | -46.25246 | 2025-10-15 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a5d92637-b57a-3ca7-b86d-77b3bd6e2972 | -4.90406 | -45.50718 | 2025-10-15 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 61837e0c-e984-3347-ac60-eec37a455625 | -3.67744 | -45.22031 | 2025-10-15 00:35:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 78847c34-6745-3207-8446-c6d39f315732 | -5.11293 | -46.04368 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4599e06f-ad4a-35e1-ba03-079a2acd95fa | -2.44348 | -49.00103 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eecc3df8-d4c5-312f-9d86-2cb7f1a6ba5a | -6.57468 | -42.96824 | 2025-10-15 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 5ca961ad-3f81-30d2-9560-db2c5bf9d72e | -5.00617 | -44.48794 | 2025-10-15 00:35:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e346e115-ede5-3f7f-9bfb-d766a937fb19 | -2.94994 | -49.32782 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5c68e11c-6347-3955-a5da-78f0184c3372 | -3.73062 | -44.14158 | 2025-10-15 00:35:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| fac4beb3-b846-3a00-84d8-29b099c22e35 | -4.78792 | -46.61514 | 2025-10-15 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 644f2fab-847b-335d-a61c-f8007a1e741d | -5.11481 | -46.05628 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| cce28b99-89e9-3e0d-9d19-7e285c53d969 | -4.65596 | -43.11624 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 7d472b48-3a6e-3231-a3bc-d6743dab95b4 | -4.892 | -43.4698 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 340.3 |
| 1702278a-871c-3c92-a126-ff78bc516f57 | -3.93808 | -47.55822 | 2025-10-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d0c012e3-509f-37d4-9a19-8244a27a26a5 | -4.6459 | -43.13972 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 9525b54b-b984-399a-9825-3f0db2923632 | -2.53627 | -48.4824 | 2025-10-15 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 20b8c99d-f2f8-33fc-bfbe-dc0f651fe7ba | -5.4392 | -44.30743 | 2025-10-15 00:35:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 0c26cc29-a4d3-35b8-b0d7-a73c76e973f6 | -5.58284 | -42.83893 | 2025-10-15 00:35:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| c9c93d2a-26cd-3426-865c-01b6a5f6ff74 | -5.38136 | -43.23474 | 2025-10-15 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5c723c89-0b06-3ede-9517-8c23cf8aac01 | -8.23416 | -45.81343 | 2025-10-15 00:35:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5ee5a871-c7e6-3e15-b30f-e869c65eb6d0 | -3.57513 | -49.44323 | 2025-10-15 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3aee67f6-dcb3-3c6b-b449-169119c66982 | -3.56188 | -43.51193 | 2025-10-15 00:35:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0d0b56be-5346-3d54-9967-2041498085a3 | 0.12888 | -51.39715 | 2025-10-15 00:35:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78017cc5-0087-39b8-9ccf-59f18c5f9588 | -5.94393 | -43.74733 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f698aa19-2fe8-31f8-b15e-e6c00c065a2d | -3.59163 | -49.43179 | 2025-10-15 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cf6e385a-e46f-35de-9b67-dab1eb7f3581 | -5.15188 | -45.68846 | 2025-10-15 00:35:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| babf693d-305e-3fee-a29e-2c104a32ee28 | -8.73223 | -43.85941 | 2025-10-15 00:35:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7cef98a9-d551-3339-92f5-557aae8965af | -4.4257 | -47.75111 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 725f14bc-cd58-32e4-a887-58edd54fa196 | -5.02591 | -45.08237 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 393ffb74-836b-366b-bbe7-1c47bb10f9b8 | -7.50747 | -46.64398 | 2025-10-15 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 57142110-53f7-36b7-b475-9c0328871444 | -4.30489 | -45.51015 | 2025-10-15 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88a02206-3e2e-3aba-803b-2895de8f85c1 | -6.22074 | -47.03448 | 2025-10-15 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0c4490b9-0ec3-37a1-bf49-f95c64dad539 | -5.37853 | -44.75077 | 2025-10-15 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| eab9cad1-ba06-31bd-ac75-5bad82c93f4b | -3.7327 | -44.13477 | 2025-10-15 00:35:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 36aa22b2-14c6-3282-9b34-2100a98aee53 | -6.40857 | -42.56643 | 2025-10-15 00:35:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 596a5e9d-3789-37ee-ba6e-f7327b0e7ebb | -4.85249 | -43.20405 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c18748e1-4988-365a-a46e-e06ed0cc1889 | -5.26539 | -45.61049 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 680520a7-d96a-3959-b0a5-55d56dce3bc1 | -8.18011 | -44.01721 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6cbb96bd-9362-357f-9770-28b1335810f2 | -5.85631 | -43.86052 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d02df065-1c25-3093-8241-64aef735a045 | -4.88907 | -43.45005 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 243.7 |
| d0d69403-c0c6-301f-ada9-72a0271a6aad | -5.31999 | -42.92124 | 2025-10-15 00:35:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 95b01715-9f92-3e46-899e-3231c7e05ef4 | -5.92566 | -42.83533 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 7c47b530-1224-3df0-8514-a4c6366816aa | -6.22529 | -44.15731 | 2025-10-15 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 865d06b7-c370-395a-bae7-8422d2d2724b | -4.79775 | -45.71173 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ef0a3d0a-80e0-3ea9-a195-480a785671a4 | -6.44404 | -43.81859 | 2025-10-15 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 30374e3e-584b-3ff7-b9e3-8cd9ff1a0ac5 | -7.93195 | -44.12456 | 2025-10-15 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5e689fc4-1279-3704-91b8-889f5e9edc2b | -5.18652 | -46.18478 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e9f3a944-8452-3d19-9c3e-a65c5a120bad | -5.13255 | -46.10434 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d810bc3-95ef-3da8-a96b-80d34e603d49 | -3.98236 | -48.07883 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 87c30baa-b603-3679-bcb0-d44fb46d2f51 | -5.1173 | -46.04947 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6bf7e38d-f8cb-39ad-9035-eb3bbbfa1401 | -5.20771 | -47.68488 | 2025-10-15 00:35:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84bb3f61-57ed-36cb-8bba-08e6081d8b5a | -3.93953 | -47.56864 | 2025-10-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1ef15262-6317-3525-9303-87d0a7e559d6 | -5.60312 | -46.24037 | 2025-10-15 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| beed241b-812c-3ada-a3aa-c437b9978282 | -0.89843 | -47.54942 | 2025-10-15 00:35:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6d9296c3-3dc4-3ccf-b8ec-bb4283f61e8f | -4.40218 | -43.6147 | 2025-10-15 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2996de6d-d5b4-35ca-a34b-13f821c8bb60 | -2.92693 | -48.30285 | 2025-10-15 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fde3dc7c-720e-3369-bf60-88c08c3d41e5 | -4.91547 | -46.71991 | 2025-10-15 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff39ff0e-46c9-35c0-acd6-ab1f1c1a794e | -5.42631 | -44.43423 | 2025-10-15 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 191a924b-123e-3f07-8dff-be5d0e8a18b0 | -8.1921 | -44.09593 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 04d30e8c-d681-3dbb-8943-b77a56e6c105 | -5.34406 | -45.36934 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ec7c5f8a-c6c8-3c6e-b700-8ad7c4b11844 | -2.2468 | -47.87859 | 2025-10-15 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cdca0f62-c729-3615-80c6-1d4c1c844126 | -2.9512 | -49.33685 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e87132c4-98fe-3f11-842b-b9dc9cd65e5d | -5.16557 | -45.17522 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 41427d5a-d1f8-3f5f-83e3-0165e0b0ace1 | -5.15387 | -45.70173 | 2025-10-15 00:35:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| be4ca43a-5f24-3490-8a3c-b38f0504086d | -3.83015 | -44.53733 | 2025-10-15 00:35:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 53a251aa-12ea-3a1c-9704-3105d8e73246 | -2.62613 | -48.05883 | 2025-10-15 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cf43fa13-5d4f-38bb-9ec3-7b39a7e070d6 | -5.86846 | -43.85818 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5cc0c117-b037-3bdd-9ea4-5d1c47e28df1 | -7.25627 | -44.92177 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6c73e64b-4969-3ed4-861e-2c5c5ce57879 | -4.26016 | -45.5886 | 2025-10-15 00:35:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3c447f46-ebf4-3e2a-95fe-fcdf76d80de8 | -6.16891 | -42.62101 | 2025-10-15 00:35:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| b9cd97e2-5b4f-3aa8-a04a-e7e661778b8e | -5.60548 | -46.2459 | 2025-10-15 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 04fc66e6-bac8-33fc-9d53-5f5faf4085d5 | -0.89686 | -47.53801 | 2025-10-15 00:35:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| be31e155-fb37-3dbb-903a-6cc4ef5faccf | -6.60897 | -43.61491 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ec77e740-9bdf-365a-91df-606e11caaadd | -4.39316 | -45.08097 | 2025-10-15 00:35:00 | TERRA_M-M | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9d998f6f-a5c1-3e6a-9016-af56695536aa | -5.79435 | -43.8932 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8b368b38-063e-3a5b-ae80-4ac34d75d29f | -6.45203 | -43.82375 | 2025-10-15 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3cc962c6-56cf-39d5-9756-dee36f5a3838 | -5.71249 | -44.42276 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 98412693-1e49-3cb5-8a2c-ead0e29b289d | -2.24203 | -47.87485 | 2025-10-15 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 552f3cf0-e3de-3f98-a35e-ab8e474aea0b | -4.66512 | -43.10839 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a0efef31-5fb9-3550-8f51-8fb83521afcf | -3.08509 | -47.7359 | 2025-10-15 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6fdd950a-57a0-3294-bf99-670431f64ccf | -3.83266 | -44.55438 | 2025-10-15 00:35:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 3b82ab09-dca4-310f-8015-d3ccda210369 | -6.58761 | -42.96596 | 2025-10-15 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README4.md)
