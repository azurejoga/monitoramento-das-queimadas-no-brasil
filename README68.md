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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09869636-3f36-3146-948b-f437fdacb2f7 | -6.20127 | -53.2631 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 178ed9c1-6bae-3d77-8d7a-90d007c4dd1b | -6.19719 | -53.27045 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf27b81-17df-3d27-925c-79495905028b | -5.89946 | -51.94252 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5115b177-739e-3cc8-8782-7219c6928340 | -6.83785 | -46.39152 | 2025-09-07 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d14f1d7b-a90b-3e2e-be69-67e98d194c31 | -6.20441 | -53.26849 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c63f867b-cc22-3d0f-ad5b-2bb9b31337fe | -6.78482 | -52.80438 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c71b0055-e948-397d-ae33-ceecca74105d | -6.84398 | -52.83514 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44227408-f5a0-3c42-8b9a-b898513244e2 | -6.81986 | -52.8057 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 061da1f8-d791-3a35-a8d7-7b5c00798572 | -5.69655 | -53.75375 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4be2b22-7581-3941-b777-979e42200705 | -7.68167 | -47.32764 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8897a590-6ab7-319a-8087-375a614e169e | -6.82128 | -52.80448 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bc42fe65-73a9-35d9-894d-3d0611f28908 | -5.48136 | -45.9142 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 906d5d14-b273-3bb4-b324-c1530607d931 | -3.59421 | -47.51301 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3b9ec160-647b-3102-9b3f-d5bddf0bde08 | -3.21035 | -54.96129 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3209975-ab46-31a1-b534-65366553e6c0 | -3.59426 | -51.54521 | 2025-09-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eca594c-c268-3e56-a888-cba63f2271bf | -6.83692 | -46.39511 | 2025-09-07 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b80c5a76-72cb-35df-a741-a6270a835de2 | -5.21322 | -43.69978 | 2025-09-07 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd54d2df-45ba-3d6f-b404-62342a412987 | -5.71845 | -53.70743 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ab3b3d-e566-3c13-a55a-658ec14c822a | -6.30044 | -55.19112 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10b01d22-c725-36de-8fc4-d7ff97bd5e76 | -1.94184 | -56.59449 | 2025-09-07 05:10:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d1e6b0-c903-37a2-84df-ac3252fd3e4b | -3.32683 | -54.91151 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0857a314-9079-3fc0-9e1b-47d13dde7621 | -3.40821 | -52.72645 | 2025-09-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a7e621d-accd-31c8-a949-72031c48c8d9 | -5.97011 | -53.6004 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ef44ff0-88bd-38ed-9a8d-2d416dca10a0 | -5.98929 | -44.14832 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7a1ada73-09ec-3acc-9a82-2089b2ce03f2 | -5.5883 | -51.90955 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e87c4a-7a4a-3b7a-a032-8f36564b0212 | -5.9677 | -53.59087 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a48e74a4-0d7a-3f71-a581-4d517b9ece2d | -2.82057 | -49.19854 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 883994f9-1d5b-37bc-b46c-d39b61b8eef0 | -1.29228 | -48.43641 | 2025-09-07 05:10:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170b7b16-5593-3362-8449-b9157d19b50b | -2.98661 | -49.30106 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 012be913-0db1-3617-9a78-4d2c0fdcd935 | -6.20466 | -53.24688 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 398a3c98-3dce-3f49-85c3-ede30dba08d5 | -6.60892 | -44.08348 | 2025-09-07 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c87edf71-f457-3b0e-8fcd-fe6abfb3ced6 | -3.24137 | -50.8066 | 2025-09-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 990a3877-1e30-3347-98e8-2f1c00ba157f | -6.84102 | -52.85561 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53b1d71-a99f-31c2-8807-61fbc3af520d | -6.8126 | -52.80833 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93871fa6-12ef-3baf-8e6d-3cf3c24e0b27 | -6.30441 | -51.41258 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d62bb57c-bfa6-35e2-a662-384940650281 | -8.08664 | -44.80844 | 2025-09-07 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b484081a-fcba-37a8-aeff-9c52c603acd5 | -6.91671 | -45.20408 | 2025-09-07 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef452100-4957-307e-9713-b100f92f5e3b | -5.89699 | -53.84441 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66736afa-c001-3b57-b57a-aee5f72bec9c | -3.32741 | -54.90779 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18eb2e0c-52de-3354-afa7-67696f0d1a1c | -8.34343 | -46.97734 | 2025-09-07 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08217466-ef36-3fed-9d53-a8871129377c | -3.8261 | -54.12177 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 691bf216-2566-3ba8-9ec0-d9ee9ef9c546 | -5.78993 | -57.5531 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 518e06b7-bbe7-377e-8079-910acdd16e11 | -5.07092 | -56.0732 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d75ad61c-c827-38fc-9b80-f4f45ab7fe31 | -5.10838 | -56.14037 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ecba9d-eefc-3929-8ff4-ff20c75d0023 | -3.58827 | -47.51568 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7edf02fe-cca0-376c-85f0-47700746b26c | -13.01272 | -54.82447 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17e49089-d856-3b07-a400-f00bc98eed21 | -13.01653 | -54.82503 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d99a5ba-cae1-311d-96a8-cce6d95821da | -12.15374 | -60.70986 | 2025-09-07 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| facbfdaa-912b-385f-98b0-e7d7048f08f5 | -11.18255 | -55.05228 | 2025-09-07 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19a401ff-b7cc-365d-b1d7-ca6dbe152e27 | -11.57762 | -47.76256 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3fb15de-9959-3cb1-a651-a347983c0e67 | -12.64117 | -56.98163 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a289a13-d9c1-3b24-aa4a-f4c886170b89 | -10.32872 | -46.38374 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bdd4357-0254-3fb7-ade0-c51adeccb472 | -10.38459 | -44.96829 | 2025-09-07 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 399c765c-070e-3914-b215-6e7c1d372b02 | -11.02573 | -52.03906 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032592ec-3744-3001-9649-06d91dc6e5c3 | -11.48296 | -55.55641 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f7795be-43bb-3398-97fb-66cc533cbf8f | -10.72308 | -48.58561 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94907150-5e41-33a0-b2d5-f368165b8f1c | -12.47965 | -53.85788 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3bf55afd-c145-35f5-acd3-7ca1797244b9 | -13.71352 | -46.8857 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 849610aa-5d9e-3ce0-9277-b798f885379b | -10.32235 | -46.38269 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1350dad6-8d39-379b-9fbe-f00d986666bf | -13.00963 | -45.21525 | 2025-09-07 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 969d7a36-2fe3-3c2c-8d9d-35b4bf66438c | -11.97641 | -50.40491 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c9394bb-0016-3973-a229-c817f17c5a45 | -9.83418 | -46.54482 | 2025-09-07 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6a7adda-8807-389f-a24b-8b72a1c8610a | -11.1592 | -48.37261 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f19e28c0-6879-3a7d-bc5e-0f6cbb4d836a | -13.02041 | -48.08225 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a1e1fce-48f2-35d4-b02a-024b7f11d6ec | -9.45949 | -56.04478 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 300d3bf5-8c61-3049-afdb-838d50771206 | -13.82919 | -46.2614 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b3aadb9-5079-3f45-85bd-bb8129385631 | -9.97329 | -51.65834 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19448b0c-db67-3932-94b0-9cab28425a1d | -9.9887 | -51.64611 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54df6b87-5ac0-33ff-bbd3-9965dce7d806 | -12.94696 | -54.76591 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75a9ab74-b9a5-3a59-b78a-6fb4e3e66183 | -10.1523 | -48.74236 | 2025-09-07 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abeb1715-d8e7-3849-89c6-19ed2393a562 | -12.94997 | -54.80053 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0da4cc3-4fdd-3755-afba-344c26fdfc09 | -12.95194 | -54.78625 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ad7f514a-40c1-330f-8d43-574186e4e9e4 | -8.07622 | -52.34283 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 956a6eeb-69c2-3249-8832-bb73f6c52360 | -13.01001 | -54.84352 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52164023-96ed-31b4-9868-720461d1590e | -12.79742 | -48.0188 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 29b79eb8-defc-34cb-9bd4-ef918dbbe2ec | -11.60683 | -47.15998 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e316b382-f962-3026-85aa-bfceaace4a38 | -13.55134 | -48.10743 | 2025-09-07 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71da7f77-2951-3619-9781-4c15761ddee7 | -11.15043 | -48.39656 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba5059fc-c079-3336-a8f5-36ac6b9dd68b | -10.06567 | -58.38098 | 2025-09-07 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8676d91c-39cc-30ec-96a2-b1aeb0dbbd63 | -12.80286 | -48.02392 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e2fb9fe5-81e8-3a3a-b841-21996bf344fc | -12.94563 | -54.77554 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| d9f9dc7a-11a9-36a3-8bab-0e992997afff | -11.21462 | -55.01216 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef51e05b-83cf-3ca6-8a14-7852230fe32e | -9.39301 | -54.76255 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87579216-3c30-351b-8e10-6bcd5d98bba7 | -13.05594 | -48.06583 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cc8154d-bd94-3a57-8453-f8c08d20206a | -11.0454 | -54.17015 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10962615-245e-3521-b881-1dc2cceba2a4 | -9.09239 | -46.99244 | 2025-09-07 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 30c98ab4-b53c-3a34-bd45-037b36f0b9fb | -10.33899 | -46.40597 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 502bd7e5-b4b8-3c1b-84b8-2a9225d24972 | -8.96915 | -62.9607 | 2025-09-07 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 562c5f71-a8d8-3856-b061-901e71bfc796 | -8.07772 | -52.34583 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60688fa4-c2a6-3bf8-b868-ca927830eb54 | -12.81553 | -52.91549 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 20c9a433-5040-3939-990f-ceb2a1586a04 | -11.20725 | -55.01104 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a93b467b-a0f6-3176-a4b1-7dbf011f9d2b | -13.7145 | -46.87626 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60accda2-2f1a-3c83-a01c-6d7e1c479e9c | -12.84299 | -48.0186 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6c2171d-1d4d-3c5d-9f82-29cd2f4de091 | -13.85803 | -46.24456 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9706afe1-64ef-3098-920b-4c8240508113 | -12.4781 | -53.83949 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1617d32-2a85-3d5c-908d-f7d3ecbe9723 | -12.94247 | -54.77017 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c9fae80d-79d8-3218-9052-0cbc0773f9ec | -8.69018 | -45.30954 | 2025-09-07 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f0bf521d-b0a2-37f2-a52e-85faf741b28e | -12.88181 | -47.9965 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5c0e111-786f-3deb-8bff-f5d2d90f1f7f | -13.02445 | -48.0776 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbef8aaf-e2b2-34e1-becc-4d20ff7fa6b3 | -13.77324 | -52.76599 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README69.md)
