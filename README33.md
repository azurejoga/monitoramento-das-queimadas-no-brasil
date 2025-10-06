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
| 75bd5217-2de0-3ce2-ba35-4f2213c51a55 | -5.09082 | -42.62333 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0b92f44-4857-37e4-bc79-225a94461963 | -7.36202 | -45.2227 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1005f51-fdb6-3289-b8b9-1313a7e45246 | -4.5152 | -50.29606 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd57a9a0-0714-3faf-9674-ea4aafa83890 | -5.48048 | -43.16573 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fb59427-cddc-33b0-b51b-6c9b12411d7e | -7.7237 | -46.24866 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5af24b8-14bd-3956-8f59-39c38c195d5e | -7.01393 | -42.29828 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a9b4ad3-27c8-314f-ba27-8e2eb2e4ae59 | -17.09495 | -45.63631 | 2025-10-06 04:27:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27dee938-ecdb-3435-a9a1-ebea953cc8d5 | -10.24125 | -50.29549 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6be87bd-a41e-3210-8754-b7396b09e973 | -13.04781 | -47.90789 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a6ad0dd-70dc-3b9c-846e-7f1a4e5c6d23 | -8.8958 | -50.92543 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0be478d-ef20-38c4-821a-bcdcdc2d1d4a | -9.62421 | -50.55062 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 361d7dab-0139-3b0b-aa48-0619687f49ff | -12.40785 | -51.11583 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 827b4210-3f7b-3642-8a10-ae54181f078a | -11.03986 | -47.7813 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51dfec3f-a388-3943-8779-ff55f1f17956 | -15.29635 | -46.30424 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 021939b7-c569-3d45-bacc-629c6e085842 | -14.55788 | -46.64658 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56a25661-120d-3592-a4d7-0027a386e3c7 | -15.7486 | -46.25248 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14cd9f35-f6e8-365b-8331-d19b5afcd5ee | -9.91563 | -50.2438 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b478d02d-dfaa-3c06-9d7b-ff802f3f888e | -13.09528 | -47.93356 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a138cb-1144-39ad-bdf8-334b9e318540 | -8.61085 | -54.96151 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 949120a1-2652-37e3-bb64-465d40f6e756 | -12.57504 | -46.74562 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead9dafa-a6c8-316b-ae26-22cf5e4bb334 | -11.06894 | -47.87584 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464a40ae-26f7-34c7-992d-49fd3b04518e | -16.05462 | -50.99406 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 454d3f70-1fbc-3e20-b0ba-dcd50a5c58ad | -14.70681 | -48.37326 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7904ebd-1451-3f69-852f-516b9ecca827 | -15.49487 | -47.92395 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e04decc-5cfd-3f4d-8a03-7cea1fea89cd | -11.48853 | -45.04657 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c776916-ba5b-35d4-80ee-1edc5a09a49b | -13.29647 | -47.77521 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff711ea-02ac-385d-a78e-8c83f7dff919 | -11.08114 | -47.75568 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0d8172c-0246-3702-8d0d-cec3a51a48a7 | -15.18868 | -56.82877 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e204a542-81d2-35bf-9db8-721b78a1dcba | -11.45992 | -43.5099 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bad1143-7674-3d2f-8907-21c8dcbd9bde | -14.70407 | -48.36917 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbdc536b-4296-34bd-a242-07585839ca9b | -14.63436 | -52.53049 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 84f8e49f-955e-31b1-925e-2e6498869d1f | -12.90614 | -47.28942 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a71c31e1-fa29-3ed8-840b-ffec5427efc3 | -12.11751 | -46.66943 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18299d7d-4f6f-3d71-b214-5eaaa55774de | -15.59769 | -52.5491 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 191005d9-809b-36c9-8453-aa92125fcdb7 | -15.81442 | -43.6707 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c9b96fb-9a2e-3fce-89e1-61d9ee011c89 | -14.92112 | -46.82426 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 516584bc-deb4-3a5d-918f-c7c809953858 | -14.60825 | -52.50048 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23e9b02e-8030-34a6-8798-d15b68a54b2b | -13.25738 | -47.61361 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bb5d7a5-4192-3aa6-abec-072a51ca6f92 | -15.37707 | -47.98169 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26430868-e712-3297-9808-7ce00e538ad9 | -12.41076 | -51.12079 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8729cac9-a046-3e63-9f42-d0981d4d6d49 | -12.42269 | -45.14473 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00722aaa-1a1e-3b20-a113-0e56fcc52b21 | -11.42184 | -55.0727 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abcda9e3-ef0f-3544-8643-5bed16b938f4 | -11.71688 | -44.3033 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c997193-8c73-3370-8282-a314e03cff74 | -15.37376 | -47.93728 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b164464-db30-39d9-bb2f-338b9a405a6d | -10.3288 | -46.95469 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1709ba7d-6c19-3e45-9edb-bba9523b8c66 | -14.6188 | -52.5074 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60d74f59-057e-351b-937d-18cae17d347b | -15.36 | -47.98252 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 911eeded-228c-3f6e-abfa-4930770f0385 | -10.597 | -48.69943 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0984de5-2f48-34e0-be02-c010ae76cf4e | -11.8209 | -45.09865 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e145213d-c366-397f-8e77-e6d92d4ec7d1 | -16.15833 | -43.67323 | 2025-10-06 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 246880cc-b21f-36d3-8d22-cae23402f0dc | -11.08212 | -47.92113 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d3e8604-c891-320d-bb85-a9a4c2f84c03 | -13.29426 | -47.81094 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c1896d2-8c1f-3651-91d8-ca78081ff604 | -12.25937 | -49.20194 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20377aa2-7ce0-359a-ad98-9a3acbe5cc59 | -15.74778 | -47.6936 | 2025-10-06 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7ecd402-ec95-3b85-8192-08570e83b9c3 | -12.58002 | -46.7354 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5bd9ed2-bd50-3c63-8220-813eea53fe6d | -10.73884 | -47.87572 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 107d6f1c-48f7-323d-ae54-3adc6c1922db | -17.07637 | -43.38711 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6585077-8e82-3bd5-a037-6eb96c736f0c | -11.80753 | -45.11689 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6845a50d-3815-32a8-b5dc-85ec55b1e1ef | -13.08319 | -47.88117 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 363e7309-8329-342b-92ea-1220152b04f6 | -13.59759 | -48.69474 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6db65119-06cc-316d-82e9-a28296e17d2e | -12.61529 | -48.12923 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab88bc62-1c26-3617-b9b2-732001672300 | -11.51525 | -47.67918 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 024bd7e7-05a8-37c7-b5c9-1bb2bc681041 | -13.04726 | -47.9114 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78fb3eec-b556-3508-904c-d76b8e2a815c | -10.43092 | -50.35498 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1a267d4-7827-3418-9c18-7f65d8f42f48 | -11.926 | -47.03092 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcd8dca7-2987-31db-993f-17e076fa08fe | -12.30755 | -49.22508 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63e4461-8975-39f9-a5da-9a2300a5b708 | -13.68309 | -47.95807 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae7bb24a-dad5-3ede-9e95-4f482b913be9 | -13.08923 | -47.84251 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24ec5443-b86a-3f56-bd20-88921633fe69 | -16.06934 | -50.91914 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a15161c9-ef09-3c25-b92e-a8c2bcc62a57 | -14.67927 | -48.39779 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b371535a-cbec-32aa-82ea-b662a294b6eb | -9.07833 | -59.02211 | 2025-10-06 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c20847-3e0e-3505-9ce2-fd69c7f77f13 | -12.4064 | -51.12449 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab3f4d95-0dce-33dd-9521-32261464c102 | -14.93362 | -46.92385 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca4d98e5-c9fc-3267-b728-7968d3f90581 | -13.08595 | -47.88522 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30394792-998b-3f98-82ed-eed9ba5de1af | -15.333 | -47.31586 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d2eedb6-e3cc-3a97-b2bf-3d90cc9471d4 | -15.21588 | -56.825 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c253b9-d443-3634-b2ad-9c14f84d0638 | -11.91578 | -55.91304 | 2025-10-06 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49549d49-6e06-37c7-a329-ae0d30f965be | -13.38496 | -47.55879 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43e19113-edfd-34e4-8ba4-acf18c912231 | -15.57245 | -52.44516 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1e8c63da-597f-3d44-b291-5bfbaefa134e | -15.29305 | -46.32674 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fb296d2-2c19-33b6-8e0e-d2657bc7dbd5 | -11.70865 | -45.4059 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ca64689-ed12-3df4-b6d0-3c134592c9ca | -14.71563 | -48.3602 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee1c3104-5fc0-3ecc-a022-e5fc8057b2a1 | -15.55484 | -46.83126 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c5a551-08c4-36b6-9d40-7b7165284a13 | -16.2917 | -45.2414 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7aa87ed2-0ba8-325a-8857-7b55c5a4aad1 | -11.13134 | -47.7636 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ab07ab6-8dd4-30fd-88bd-2f2b22dbecb9 | -13.26839 | -47.62983 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c894c9d9-a2f5-3aa5-8545-a2d776e30e6c | -11.91198 | -46.22996 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4a9cc45-fa13-32d1-a4dd-e1a40a5eab2e | -16.05142 | -50.94887 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a71ce53c-56df-33d8-ad5e-244045ba6563 | -15.45764 | -44.30676 | 2025-10-06 04:27:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1cc88144-c467-3751-a38c-eec0328daa2a | -13.78535 | -50.78752 | 2025-10-06 04:27:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad1c84e5-6001-3947-b498-4334056d6d8d | -12.59718 | -48.11143 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 66f33ae2-e5d6-31c5-8bef-8b7245a580f0 | -15.61902 | -52.53811 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e21ba9cc-b4d0-3a7a-a77e-90219dc534ee | -15.20612 | -46.39283 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c2f4084-7ede-3994-9d2f-0d7aaea43730 | -14.56044 | -46.68785 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d321cb39-7f9f-3fef-aa77-f4278a8a8dea | -13.36627 | -47.57038 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea0096bf-a589-3ebf-b7e9-2ce28d71176f | -11.84358 | -45.06572 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71d9a4b4-d613-3505-8538-de9679a1f77a | -14.84964 | -51.48272 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e115dd-aa54-3036-97b2-b83ce3036f3a | -13.28324 | -47.62141 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f95917a-4492-37d7-b7ab-9f499e80de4d | -9.68776 | -48.21197 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf7a177a-03a6-3b30-af83-f97393dca4ee | -13.37335 | -43.62342 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
