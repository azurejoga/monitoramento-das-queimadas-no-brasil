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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b994195-1cf7-3b95-acb1-3702bf4de6cb | -9.98934 | -36.38065 | 2026-08-28 16:07:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3f206e06-13cb-3d1d-8c65-42908efa90d9 | -9.6617 | -45.7155 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea7de5c-20d2-3b69-979b-842a13b11837 | -11.84307 | -47.21962 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e4c9a8bc-5300-3eec-9dee-db2504b81a24 | -10.91727 | -46.62958 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 687f1e33-223b-3954-a062-7f177dc9455f | -9.49945 | -45.64404 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b9e4a261-9d6e-3d2e-b87a-2933ced1b509 | -11.48007 | -46.95688 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f80f3361-1e1f-3e45-a595-13f167f52bfb | -12.32505 | -50.58871 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 508c3d86-590d-3d40-b990-01d121b6cc43 | -10.023 | -45.62819 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29fc072a-a297-3bdc-ad9a-785929dbdc20 | -9.84109 | -46.32064 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5118ed5-9f62-35ae-8126-f8d9014d6b7e | -11.48362 | -46.93938 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ae717ee-0e16-3c1e-bfba-1811d275228a | -12.32925 | -50.55975 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 110d9212-efd7-347b-9b75-cad57926df8c | -9.04077 | -41.61164 | 2026-08-28 16:07:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 98286163-981b-3172-9c8a-0d1778ea692a | -9.64553 | -36.88025 | 2026-08-28 16:07:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 261fbbeb-4002-3ef1-9a70-1193a812796d | -12.05784 | -47.18999 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86e48ffd-95d8-33fa-be36-0662767a8177 | -11.19636 | -40.83719 | 2026-08-28 16:07:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 594e94fa-817c-311f-ad46-116d0101cdd3 | -1.78573 | -47.68752 | 2026-08-28 16:07:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34f89372-036b-3fbc-9f17-778eda0fd737 | -10.17804 | -39.30273 | 2026-08-28 16:07:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 20181850-f517-305a-a215-d9bd90ae8529 | -3.21886 | -48.61031 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9c15f69-5b14-3140-a758-fb8fa3f955e4 | -11.82624 | -47.22576 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f8c90961-241f-34fc-9a05-7e8ff0ea7826 | -11.3559 | -48.39441 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f65b37c1-ed59-3631-9859-4e62c3646be5 | -1.85957 | -48.36798 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb827d63-1f59-3af3-8e48-5a0703ca63eb | -10.56016 | -50.41891 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e4cdcf0b-27ed-3b6b-9fb7-9c3f3e7c728d | -11.34971 | -48.39507 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3b990500-c966-3067-8fe3-9b4761e580e0 | -9.43775 | -37.83224 | 2026-08-28 16:07:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d79c4a0f-6ca4-341e-96f4-09d44eacbfe4 | -10.96966 | -50.26333 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 51bdeaec-6203-3401-b61d-94c31587f880 | -10.95876 | -50.29066 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f48ce93-4dd6-3780-9e13-75120f3e98f0 | -10.95949 | -50.29712 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d1d56175-3e78-36c3-91b4-3ae87baf4732 | -10.2494 | -47.99237 | 2026-08-28 16:07:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 24440134-cab4-3f1a-b571-376c3daf892f | -9.87195 | -45.84927 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3195d20b-57c5-3058-a223-100d4224e38d | -12.32606 | -50.56416 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2e9b9fcb-4acc-3877-a9bc-3641be8f8073 | -10.08829 | -46.99027 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de698a50-9e27-3a8b-b0f3-804f969f0a9b | -12.07954 | -47.16829 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c322e283-8f9a-3ec0-ad6d-e770a58660bf | -4.08385 | -40.12153 | 2026-08-28 16:07:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 13830e76-a429-3738-b430-e2ecbb5f5fe8 | -11.24239 | -45.05404 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ac0db78a-19cd-34d5-9cfe-08945e12b52d | -11.77835 | -47.65479 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 788a71b9-f7bd-3501-8f46-93d5f7f9b89b | -3.07751 | -42.74306 | 2026-08-28 16:07:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3db1cfb-e899-3497-8abd-a4bc1bc2fa85 | -2.72914 | -47.04605 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1b508624-98fe-3bc0-9983-2328f4c04224 | -9.87624 | -46.34254 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 017f654c-8aa9-3e67-9b82-8fc7b31ed7c4 | -11.54737 | -45.49447 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08f6d32d-d8b4-373f-a0ae-f14ab1e14e2f | -10.06832 | -46.96649 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a36a18e-014f-3b72-8249-1b54999968e9 | -10.91809 | -46.63007 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a7329bca-bdc0-331d-8c0e-3312828cfe50 | -9.6205 | -39.31566 | 2026-08-28 16:07:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 223cc225-40ea-34a6-a5c2-1f6b894e53e0 | -10.46976 | -46.18505 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2cf7dff9-f8a7-3520-8291-e78e82ec0fb7 | -3.93118 | -44.89886 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 47a2c08f-dba2-3a86-bc50-065ce9ce8942 | -9.69608 | -46.55864 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c8e1c60-a98c-3103-971f-1087c53d1a8d | -9.80184 | -41.95425 | 2026-08-28 16:07:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b24f8963-7436-3a45-b0cf-f9997d4e34f0 | -9.88598 | -46.33442 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bba52c5e-463e-3682-b1e5-e51e10b6549e | -4.37204 | -44.99931 | 2026-08-28 16:07:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41eb0d50-31ae-369e-9cd2-ef031bd2bc91 | -9.701 | -46.55443 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f17a589f-aa1a-3d60-badf-134cb6bd0b48 | -12.31894 | -50.56491 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 75f53939-c0f8-32a4-abf4-fd3f285c2efb | -11.25168 | -45.0394 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a5feb795-583f-392e-8332-474134feaf80 | -3.46313 | -39.60014 | 2026-08-28 16:07:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3777874f-ee59-3000-9fd0-bccba9bf3182 | -10.08487 | -46.96363 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5180a5d9-e74c-3db3-bb3d-86f32e2545dc | -1.13972 | -48.03419 | 2026-08-28 16:07:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e9bbbc5-3877-3d30-8b71-011d1875e41e | -11.07709 | -47.11964 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c156e8fd-2e9a-3a11-9c62-89a5e856745a | -2.89873 | -48.27243 | 2026-08-28 16:07:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 66a3d4a7-2764-3638-9252-397f8e71f9da | -10.08256 | -48.68433 | 2026-08-28 16:07:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 6dbe1ce0-1817-3d76-a9a1-3d1df78faefd | -10.56169 | -46.41828 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 439bd878-02f5-3b24-8d82-d586e5235e43 | -12.32125 | -50.58601 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 87886f5f-610d-30ed-970d-56b211ed0236 | -12.30862 | -50.56914 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| e4104a53-6436-30f4-b277-fa66aaf4eb47 | -4.89945 | -43.6327 | 2026-08-28 16:07:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83d74312-d9b0-3047-90bc-b6f8840c9719 | -11.23671 | -45.04914 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b8663315-54ce-306d-b050-7cdc39d81ceb | -1.88262 | -48.26342 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a9d7543c-35e6-3514-85a7-1d6daafe8508 | -2.72377 | -47.04514 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dbd931d3-2e71-34e0-9e8b-908559a67da7 | -12.31574 | -50.56836 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0c674135-1306-3bd2-b73a-3aa15a5e5c17 | -10.56665 | -46.41413 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9b9b9e0b-a45d-3ac6-bb47-224f9b67a042 | -9.79585 | -43.55032 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a49a849d-b67d-365f-b30e-d1afe9704499 | -0.90702 | -46.69004 | 2026-08-28 16:07:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3adb1be2-eede-355e-85c7-8d62c354b798 | -9.88303 | -45.85424 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1f7c3a43-6d97-3763-aaa6-048e616f133d | -0.88491 | -48.19354 | 2026-08-28 16:07:00 | NOAA-20 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 707215c1-3522-3aa6-bc9a-5a1e8c9ed8e9 | -10.09193 | -46.97911 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c695c2a-f993-32e8-966a-39965f8bf9fa | -1.58381 | -47.73825 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1436d04e-2bfd-351d-b555-ebb71b6967f8 | -2.23383 | -50.53279 | 2026-08-28 16:07:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9eb6b6e7-ae87-32f7-90a4-846809b5284a | -11.81022 | -47.19033 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9ad4513f-716f-30c8-947a-2ff3b4a86ad1 | -2.35156 | -47.05484 | 2026-08-28 16:07:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d10ff3b-6c56-3c4a-9c30-ad5da077e755 | -9.69563 | -46.55518 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d19f842-69f3-32c3-adc3-9f64aca09902 | -11.66492 | -46.73168 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a634588-3b55-30dd-b931-2bb583567d55 | -9.65663 | -45.71619 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 882ec866-db45-39a7-9752-8fe7881eb66f | -11.2502 | -45.06814 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5e1905cc-1f72-36a2-8135-07267a0f6fc6 | -4.37401 | -45.00208 | 2026-08-28 16:07:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 83312049-4ae4-3694-a171-f0b026ceb1e1 | -9.84335 | -45.84842 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49d6ffe1-21ad-366c-a560-85f32dd3073b | -11.35051 | -48.39634 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ae425f58-e77d-3821-adad-76384929819d | -11.65715 | -46.7258 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 37270d0a-61ed-3f66-b465-ec0e8cd158fc | -9.50133 | -45.65881 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1da2b9c8-b269-3d75-8570-c1d15bae2001 | -11.76383 | -47.63423 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 50eb29bd-b110-3ec1-8308-00b55521df74 | -3.53854 | -48.17749 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 441e6017-ec52-307a-9afa-8a28565f626e | -3.53243 | -44.31776 | 2026-08-28 16:07:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7e4fb0d-51d7-344b-bab5-58d314cd9725 | -10.24991 | -47.9966 | 2026-08-28 16:07:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4ca3f0b7-64d7-318c-b2e3-6fc7d67a8aac | -9.43722 | -37.82874 | 2026-08-28 16:07:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e2c2af79-8f06-35ad-ac52-8db12652250a | -1.58004 | -47.74824 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 54b9e439-7349-369f-9415-7c97956cd198 | -10.54158 | -46.2533 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ee4165a6-83ea-3ae4-959c-0b3070aad86e | -2.0123 | -48.33869 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7362ea01-f888-308f-a61a-63518e59184a | -11.32892 | -48.37762 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f81f035e-3969-3223-ad3e-5dc0a60becf9 | -10.8632 | -44.80415 | 2026-08-28 16:07:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fbaf88b8-cf7b-3506-97af-a2b7855b8ea8 | -11.77507 | -47.64801 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0428eed7-a940-38dc-86d9-55024ac00c3e | -2.72325 | -47.04096 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 878c7a48-057a-3724-b185-d6027b4677d3 | -1.60999 | -45.46279 | 2026-08-28 16:07:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8447f8f1-c284-33a5-b868-423f04c28df1 | -10.08364 | -48.68557 | 2026-08-28 16:07:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7024ee95-94d3-304b-84fc-8196810a78a7 | -12.30078 | -50.56289 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 4c8b6bb9-7eba-3f1f-b4a3-520111e20648 | -10.96204 | -50.50964 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README97.md)
