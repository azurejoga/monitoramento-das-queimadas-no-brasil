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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 366aa68f-88e8-336c-aaa3-521708c5165b | -5.85509 | -39.42871 | 2025-11-16 03:46:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 44789058-691c-3965-8197-cae958226c2f | -5.72081 | -41.39875 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 03c121f2-b8b1-3060-9b5b-03b79c8352a1 | -4.36236 | -45.51088 | 2025-11-16 03:46:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 600a914d-01bc-32a2-9e39-2568a6546101 | -7.7611 | -38.94384 | 2025-11-16 03:46:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| c2c98cbe-f99b-3398-b1bd-a6ae8959458b | -6.56792 | -47.90089 | 2025-11-16 03:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9ab27d9-0906-3044-8315-9cccbf15620b | -6.93024 | -39.61446 | 2025-11-16 03:46:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59c3befc-36bd-382f-b53a-dca32376fc30 | -5.16343 | -43.39991 | 2025-11-16 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 641f4f1e-5409-30a4-91ad-96022cd1134d | -6.81628 | -39.14404 | 2025-11-16 03:46:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 33924e00-62a2-380e-a7a6-b60c3ed046e7 | -5.72007 | -41.40318 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 48e3f07d-0a45-37a4-a8a0-454168b72478 | -3.78851 | -47.47443 | 2025-11-16 03:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cd6dc19-6be1-39d8-b1fe-68c2a29b1d92 | -9.85383 | -44.71698 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df35b092-3d81-331e-8326-fab31924230b | -7.02667 | -39.36746 | 2025-11-16 03:46:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f7e87091-f75c-3328-807e-feb115947cd7 | -5.99449 | -41.91973 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da54b539-e271-3a94-bea8-7516b5bbd008 | -6.90163 | -38.8826 | 2025-11-16 03:46:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 07171574-9728-3be7-b82c-7b77c31c6c21 | -6.36265 | -39.62946 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68d54b7e-0021-3a70-b39b-36333f4a3bef | -6.30901 | -43.79887 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a21658fe-d0a9-3b2a-a199-3297cbbf8260 | -8.05753 | -43.09941 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 48bdef11-8e16-3851-ad97-14d8e448d9bd | -9.51036 | -47.27443 | 2025-11-16 03:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0890ad32-4997-3561-a8a0-32c6a7b3fbcd | -10.16538 | -44.50914 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8618e1-db53-3992-af80-9c0314931531 | -9.34737 | -46.59779 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 136abba6-b146-3960-95ff-72c07184319b | -10.16442 | -44.50169 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c614d09-c61f-3828-a970-ca955d66663b | -3.99827 | -44.27543 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 151cab84-7786-39a2-8ed7-bfe9b1b41382 | -7.36399 | -43.32869 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a2486bb-ff4d-31aa-a729-49fb4e7ba54d | -8.57252 | -46.05013 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e5dd78-c8b4-3d82-9bf1-eeda12fe2c8e | -6.06334 | -41.5486 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cd9e849-80a8-363d-baf9-3e3a932b51bb | -5.48416 | -44.84622 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0cd64d3a-025d-3f0a-b45a-3786e8c2f728 | -9.99934 | -44.77763 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e8e0350-43d9-3988-87b9-d09611d8d6cb | -10.00171 | -44.76508 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b05bff60-8a40-3cc4-aa31-f934e8a4ba87 | -4.93525 | -44.53672 | 2025-11-16 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf25b3e-2bd1-32c4-932e-7484aa080412 | -9.74647 | -43.95964 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b7b738a-d2e7-3766-95a1-f0221bad0852 | -9.74545 | -43.96519 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 06cd62a2-ab0e-3a02-8136-f8a034d9980b | -3.66099 | -44.81876 | 2025-11-16 03:46:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6b4f45-ae09-3f6c-a5f0-072488c98c6b | -2.52434 | -47.81068 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 44772469-db8c-3055-8a8c-d10722072a80 | -6.45351 | -42.36974 | 2025-11-16 03:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4da8186d-5ee7-3202-93e3-c10822add71e | -4.62866 | -47.41257 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d633ceaf-460d-3793-88b2-9828b08d1ccc | -5.42169 | -43.25736 | 2025-11-16 03:46:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6dd1d374-2d9c-3881-a8cd-e1e0a52b9fc1 | -7.01486 | -45.16968 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afac58d3-e492-3164-892e-3c55994c13d2 | -5.991 | -41.91188 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 922b9ab0-614c-3c11-b8c7-ba196971046f | -6.31139 | -43.79325 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fde55464-7c3c-3836-96d9-9dd09c2c0d07 | -7.26791 | -48.0374 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94871d36-fa06-3948-a528-7cfad24d6023 | -9.72376 | -43.96512 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 26797573-9296-3ea9-8c55-96d6e93a5820 | -10.16641 | -44.50341 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b7c5ca9-f052-3532-9dad-8f19be0e14ae | -6.78183 | -43.54195 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5220b38b-af42-3ace-81ad-e37390815c37 | -5.46796 | -40.97128 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 036a5cd0-ab69-3d98-a541-cf1f4e213a09 | -6.67201 | -42.04421 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 11f0d684-d0d0-3b57-90a2-beb04420fd71 | -6.93881 | -38.79414 | 2025-11-16 03:46:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb34921e-c7ba-35b8-bc4e-ddb63cc01181 | -9.35162 | -46.59393 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 481ad260-ed07-357e-b228-69e83447b3bd | -9.06351 | -44.7944 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d86eb31-81a9-393b-9a36-c1e3c092e379 | -4.5737 | -45.81492 | 2025-11-16 03:46:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 124a2013-6313-3fdb-8706-93407cafbb4c | -9.34818 | -46.59348 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4a3ef1d-2694-38b3-8986-82118b6a51c8 | -6.67511 | -40.80529 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 516c3117-1b36-3eb9-8361-83be402b544d | -5.20505 | -43.4749 | 2025-11-16 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ffb611e-5b54-3ccd-9a94-2ca15e419038 | -9.34234 | -46.5789 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3bdf3a-bd41-364f-8f1b-28d9a93495b8 | -6.50135 | -39.5198 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9af2b557-7565-3b17-b76a-0e4cbd1627c8 | -3.32414 | -44.56278 | 2025-11-16 03:46:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35275f41-ad51-3dc2-90dc-d61d4f62cfa7 | -6.77863 | -41.44545 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f0d76336-4a64-37fc-8c78-476ea547e879 | -2.51858 | -47.82561 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9a2e700c-87cc-398a-b190-24f0539a1e8c | -5.85592 | -39.42383 | 2025-11-16 03:46:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34fff6f1-5b7b-33d0-bd65-4548e31f15d6 | -5.51438 | -40.9696 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a7b9aeb-9b06-3b48-b082-2d78f30d53a4 | -6.62248 | -41.46303 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca9c5f92-1785-3542-b6d5-673559d76ea3 | -5.53273 | -41.76536 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd7ef7ee-bfcf-3404-86f8-99219187de4e | -12.05794 | -48.20824 | 2025-11-16 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 313ad657-c6b3-3b09-9465-8ee5ac4f46a4 | -10.80672 | -47.99317 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f2c8479-cc97-3a9a-987d-41a6850f6f40 | -11.05476 | -45.15667 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d530265f-4984-3ee5-a4e1-ed3fc64536ce | -10.39148 | -49.05403 | 2025-11-16 03:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d31da3da-4887-3d20-8662-18d29a947d04 | -13.65295 | -48.74925 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afb450ac-9540-37ed-aebe-4e1b4b3fc491 | -10.54332 | -47.9948 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84d0a914-b721-371b-8efb-af0afbc1092b | -14.6722 | -46.54169 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c5d4276-48af-39f1-8da8-21b2cfd5ff6f | -12.6635 | -47.1694 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 462d856d-0298-335c-a773-d0016ace39e7 | -13.64667 | -48.74826 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e8ce91b-5778-3187-81f7-270a3adc630f | -11.70989 | -48.40025 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84609a41-940d-30f7-8d55-46f8dfc46e49 | -12.69587 | -46.79505 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb04bbf3-7648-38e8-b246-944ff573842b | -14.2141 | -39.76881 | 2025-11-16 03:49:00 | NPP-375D | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fea1918b-51fc-3263-84fb-59dbb11caa06 | -11.99791 | -49.27096 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8e0f7c31-616a-3193-b18b-26f02c79cfca | -12.67355 | -47.17773 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b775c55b-ea2b-3e70-ada1-2adaf59bd756 | -10.53839 | -47.92065 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec16179-2f5b-3019-b815-f204e37f351d | -12.39133 | -48.09417 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3d9f256-c58b-37b1-91fe-2f2094e6d62a | -12.67499 | -47.17178 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89f3470f-0995-3c17-bd3c-10394377b231 | -13.38908 | -40.65495 | 2025-11-16 03:49:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f51125fb-61cc-3fae-ac33-6acc7f81faee | -12.67272 | -47.18184 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b0b54eed-cd2e-3ce8-8a0d-992eb33cb5ec | -14.67164 | -46.54448 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0600dd27-41f7-3011-a7bb-322f81dd205e | -12.37827 | -48.09833 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db53263c-9f54-38df-a66f-5992ec338824 | -14.66405 | -46.58221 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e44a090-9059-3974-a43d-9330c77e341e | -10.52731 | -44.83792 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a55420e-6f50-346c-8cf7-af297c2bf9b9 | -12.67438 | -47.17365 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2ab725d0-5e9e-3d76-b022-7c1b94b90880 | -9.71705 | -48.90744 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05a3e1ba-f1f6-3441-84f0-0991b9ac25ed | -13.35608 | -43.64089 | 2025-11-16 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 629ad83c-8f2e-33ee-bff7-df46a2a8cf58 | -11.42606 | -43.13191 | 2025-11-16 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80645ea7-3d00-38aa-a827-3e91ce035642 | -11.41845 | -43.32874 | 2025-11-16 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4532c463-a552-3508-803c-a1e208c8974e | -12.87773 | -46.44655 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c403942-f60d-3df4-8845-64de80100b4d | -11.96712 | -44.95546 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 825c2fb3-a2f8-3c51-bf60-2eda2986facc | -13.73505 | -44.23172 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5260fae3-166e-3574-b590-d3d9639aef1d | -11.16614 | -47.45816 | 2025-11-16 03:49:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34b07db0-e9f4-3904-bbca-74c46db029f5 | -10.9369 | -44.02689 | 2025-11-16 03:49:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4da7b024-b1d8-3082-a14d-0ffa7433a3ee | -12.20778 | -49.62074 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 186c330e-fc5c-318a-98f6-46c703034df7 | -11.71996 | -48.87441 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19d315c2-00fb-3d14-a8ef-692b04ef0a1e | -11.96824 | -44.94957 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffd14d18-1b96-3ab9-a371-9d149f9d2461 | -11.05537 | -45.15342 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71bbffa6-61ee-38b2-ba42-011cd4aced65 | -11.97086 | -44.96338 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c4bf16d-80a3-37da-9198-cde73c089ebc | -12.66371 | -47.16727 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README23.md)
