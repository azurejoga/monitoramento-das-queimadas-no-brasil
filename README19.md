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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7ab3079-99c2-3fe5-acd2-7a762158c581 | -7.83669 | -47.6507 | 2026-08-24 04:25:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f89e10c7-374a-35f2-9de7-fd0c4ce0675e | -7.44997 | -46.91745 | 2026-08-24 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 89f756ce-c6bc-3eec-a9f3-8b8e0c42e11c | -9.67558 | -55.09642 | 2026-08-24 04:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1004545a-7de7-3382-8237-9e9bc1d1077d | -8.54247 | -55.28365 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fc99db1-9ab1-3bc8-9ea9-f33d6b5b4b7d | -7.36822 | -45.80871 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f114dca5-8d2e-316f-81db-b968de5c22bb | -11.10377 | -38.5971 | 2026-08-24 04:25:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cefc4523-ac13-3bfd-998d-8ac466ad3715 | -12.22514 | -43.17311 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 271645af-2738-393d-8ee2-3be8a3871776 | -6.35019 | -54.76823 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ba4839c-aa1c-3933-a75d-7b0441a4441a | -5.57489 | -45.2949 | 2026-08-24 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fa1c58a-f769-3a9e-b19e-84f7d3c4b403 | -6.33864 | -54.76107 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4aa056b-07e4-3d84-bfe8-ebf77afb5c1e | -10.73623 | -47.97559 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37c10503-eecb-3c95-92c5-e68481f5df38 | -10.69597 | -47.74072 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5a2489-a944-3429-b592-91443f8fbed0 | -7.36123 | -45.80757 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05a17489-e3ff-37c1-94dd-71cc2675b5a3 | -6.84497 | -52.50156 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9683e43f-1d17-3792-b3cf-9b8a3ec94b18 | -10.82402 | -50.9435 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 632b700b-5220-327c-b9fe-0b5b7c5fdd4d | -7.48549 | -45.13198 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d732d6d-b01c-3d9a-ba72-6a35fddd066b | -10.63129 | -52.25301 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab026c7b-4201-3386-ae0e-d293e3176cd7 | -7.1692 | -42.74139 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24abf556-cf8e-3e22-82c2-262a4f197983 | -7.15487 | -42.78934 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5004890a-2468-36d5-80d9-a5f20014ba0a | -10.73101 | -47.9838 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6411fd3b-059f-3554-9649-9cc74f64ffca | -8.31099 | -47.58566 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc00314-3fec-3b25-9a0d-91a1c0b3844d | -7.48832 | -45.1361 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a7f3e87-6207-3ebe-9de8-7f14297b42de | -10.04277 | -46.43359 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0373a33-72b8-399e-848f-ac08597fd2dd | -6.84435 | -52.50501 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 372c7a0a-06ae-3079-9ad4-39dd6e0a9274 | -7.17254 | -42.74192 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64a9d323-b74b-39f6-84b6-e6e302df27d5 | -8.92847 | -45.73653 | 2026-08-24 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54bdee22-e842-3273-b76c-dd3e895d4b48 | -6.17701 | -53.52673 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dfb9692-622f-33fd-9ec5-7fd6147690a0 | -7.97046 | -43.92508 | 2026-08-24 04:25:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8201a041-b008-3f9d-b548-fc265b9ab903 | -8.81396 | -46.60872 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2032d214-8620-30ce-aa14-95d7e0a0c7d0 | -8.09618 | -47.48596 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c2dd739-5dfb-314f-adc6-fb92e18e8d03 | -9.33511 | -50.35257 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b354b180-0a82-30f2-880a-88403a2487ae | -6.19576 | -53.5218 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59e1dcf1-f45a-3a02-8a2a-bb70bd79e74f | -7.8992 | -46.33236 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c57b81e8-27ed-3a0f-a071-ccf560dbedf1 | -7.19143 | -42.75209 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c7837e7-53a9-34a2-8a91-ff551f11785b | -7.36599 | -45.80041 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21700b65-b156-39a3-9627-5bd16f2eee06 | -8.34863 | -49.17703 | 2026-08-24 04:25:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71840178-98ba-35a9-a735-7ce527e7f4a7 | -7.17587 | -42.74245 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd17af9a-1b9c-368e-a622-21ca435955e6 | -7.26699 | -49.88961 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f76e51f-87b0-38e8-8cca-6f0ac7bd9ff3 | -6.83844 | -52.5072 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 791e63aa-07f4-3b58-bc27-cee9c5c70ed1 | -7.26023 | -44.19504 | 2026-08-24 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da3f34d7-3ed3-3018-9427-fe6b2323f863 | -7.1571 | -42.79685 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d77e153-4cfc-3ade-aa41-ce719390be11 | -8.79118 | -48.31515 | 2026-08-24 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2890dbd1-8daf-3421-bea8-aba32be6fd59 | -7.15432 | -42.79283 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d61dac7a-9282-3fcc-b223-db2b95a725d9 | -8.57527 | -49.9826 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e165069-4b35-3c48-be5b-bfac439f45c0 | -7.30862 | -42.97863 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4ad5a14e-8e19-3d60-b07e-bff2b2eee292 | -5.00622 | -56.13975 | 2026-08-24 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 081ac2ff-6561-3c7a-9f44-6415f090c9fe | -5.07222 | -49.37072 | 2026-08-24 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81a6aa4f-cbc1-3e8b-8f41-d99140da7e90 | -7.31139 | -42.98264 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5be994e-6d9b-35a3-8725-27bb74b9f3f7 | -12.1378 | -43.39426 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c9c79ad-a1ba-38b9-a2ff-a7c8e7d7e082 | -8.54987 | -55.28806 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f90b9d-f464-350f-871c-72a8fd0d7b0a | -4.93583 | -45.79771 | 2026-08-24 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 633e9252-a1e0-36d0-ac76-15d90270f98b | -10.7295 | -47.96993 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 275a90e4-6c67-3208-82dc-7cfe8524c37c | -7.36663 | -45.79655 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c89bb83d-f016-3641-a186-f874baf2892b | -7.26413 | -44.19208 | 2026-08-24 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fb7d846-004d-3a9b-8152-7bac4603631e | -8.31275 | -46.8975 | 2026-08-24 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dcb9db7-eba4-3f25-85f3-5f86ebbaec2f | -6.18701 | -53.53465 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c955a74d-dffd-3636-854c-ede606b84a9c | -7.36948 | -45.80098 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95bbc219-d427-3a46-a655-4e9ef511e88c | -5.87824 | -52.10851 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 868f1d6a-57db-3ef1-8d97-17a844e3edc0 | -7.3587 | -45.82305 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d273a655-f1c6-3c14-bde5-d99500a05d60 | -12.15572 | -43.40047 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f3def24-1db3-3f65-859b-7fc82925cfea | -9.05505 | -45.19729 | 2026-08-24 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc0881b2-8594-337e-9f55-1dc91ee01de2 | -10.6285 | -52.24797 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55aa8650-f5a7-3833-bf3c-49666d123fe3 | -7.97901 | -45.27854 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 167eaeb8-3637-3eac-8e8d-b44ed0f4f847 | -7.97059 | -45.26584 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90f6f14b-2adc-3576-8c3b-ac8db3381470 | -8.97995 | -46.02145 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5ec2c8d-f8a4-3a89-8613-b3e0ea460c50 | -6.80437 | -42.67679 | 2026-08-24 04:25:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24d88911-1215-3a44-8477-7e0ee00ca307 | -7.15811 | -42.74682 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e1226d18-af01-3f97-b624-bf57254f4197 | -8.38333 | -46.46679 | 2026-08-24 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fc20697-fc4d-3305-8659-897ae8c5de0c | -6.34042 | -54.75142 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55e4ed23-9e91-3f6c-8df4-3e1b38f1cdbf | -7.14492 | -42.80926 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| af03921b-6e20-3af7-9b66-f96473b60f76 | -8.95527 | -50.75262 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 508f4be5-b017-3a14-b9cf-f27940f87604 | -6.19504 | -53.52589 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ddfe7c-1cdf-3533-93b4-fabf548a087e | -6.5972 | -52.45552 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f52a30c3-8934-3519-aa65-aeedd74b4360 | -6.34487 | -54.76219 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bc85a63-14b8-3995-80ac-85ccfe5533e6 | -10.72876 | -47.97435 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 797fad70-6122-3d24-8202-739d5153e553 | -10.47023 | -49.51761 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75033eca-72c3-321d-99b0-9a3c6143e5e0 | -7.26423 | -49.89106 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0835f23b-2a9b-3cc4-a344-f3371c1a310b | -10.73024 | -47.96557 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 077a00d2-94fc-3210-83af-8058f7b44fd1 | -8.10148 | -47.47729 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58917284-7835-387d-b5d7-3ca86e3d5107 | -10.45925 | -46.40184 | 2026-08-24 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a840b77-9c59-30ce-9491-ba1bebfc8449 | -7.26613 | -49.92034 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fef381ae-9b6a-35f3-a2dd-4f857ce3acba | -10.01701 | -46.82602 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4710f32b-8261-384d-9c9b-d90c60690f5f | -12.27358 | -43.19572 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ad8f332-08f5-389b-933a-a8acc5339f94 | -7.48608 | -45.12837 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db509ed8-e91f-3562-b897-d66500bed12b | -8.09131 | -50.05065 | 2026-08-24 04:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eb1139c-29b3-3e81-8483-461ac43397a0 | -7.64955 | -42.74502 | 2026-08-24 04:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b64e3f8e-485f-35cb-b3c5-09f3fdec8598 | -7.36981 | -45.82091 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f48d317-8e38-34f6-a74d-fe9dc29f303c | -7.26349 | -49.92243 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d8512bb1-ed34-30f8-b61f-e374ff137789 | -11.62101 | -51.09146 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ccaecea-984a-3b2f-8a03-567041c2d9dd | -7.37266 | -45.82539 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4df32cea-ff6b-38fc-8601-afe02fb36cbf | -6.86783 | -45.01779 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aa134fe-593a-3a75-9348-b2b91d069179 | -6.83964 | -52.50053 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 28d10749-1130-3d00-8ff0-8028ace42be6 | -8.53746 | -55.28579 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70628d7e-e9b2-3332-9ade-ee7347f679a6 | -5.91672 | -52.13835 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65788e1d-8a56-3c52-9bc7-ab487d8d724b | -10.29567 | -48.20021 | 2026-08-24 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2048d0b-e605-3ae8-9990-9381a22d7258 | -5.92869 | -50.10772 | 2026-08-24 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883ce15a-5304-3253-afc9-605e149d4619 | -9.05454 | -50.77159 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dded1d92-d323-3b4f-9c32-59d23319b1d9 | -10.43152 | -50.44173 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46af3693-fd48-31a3-b9d9-e4b65b1c1e5a | -12.25496 | -43.11427 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbdbe99f-046c-35c8-90ff-48b970ece261 | -6.77891 | -44.89868 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
