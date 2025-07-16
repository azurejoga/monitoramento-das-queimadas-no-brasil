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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73fee0e9-f286-3542-9d07-1f1bd059f8e1 | -10.09564 | -46.6852 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ef6f608-1a83-3e1e-9167-4babb7efea98 | -12.07372 | -43.48095 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eccccde4-d857-310c-87da-f3bca1aefd6b | -8.91199 | -47.34209 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44069c74-4913-30d6-a3de-6f0543d2cb6e | -11.40293 | -41.71315 | 2025-07-16 04:14:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 328d5815-664f-3865-9d90-04527bd5f362 | -13.12367 | -43.48941 | 2025-07-16 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5feed788-5055-35db-81b1-23b849c4e44b | -8.24198 | -44.92163 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c38c0dd7-6aec-3345-8eb0-2953355d1a04 | -10.31917 | -49.91584 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36b0d5ac-d080-3820-87c4-9a847b0e7fe8 | -10.3903 | -49.75998 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 951e2e2b-a452-3f03-8c35-3f5daeede47e | -6.38026 | -44.75375 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55871047-8554-365b-98f8-9138af3aa4b4 | -6.94578 | -42.37634 | 2025-07-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de45c207-1081-343e-afaf-e7e3d4a32088 | -10.32202 | -49.92449 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba83630a-cf11-326a-8657-8195c9b8d789 | -11.49252 | -48.07788 | 2025-07-16 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16285c61-3f5c-3c98-8778-8a53d0275fbd | -10.27617 | -47.61523 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70b1b2e5-f37b-3aa4-ae3d-c60e4c6adb68 | -11.78135 | -45.2133 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d5f0991-dbcf-3e2a-86a4-48f08bc30f42 | -9.0492 | -49.30095 | 2025-07-16 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6f96224-6f8f-3973-9785-2e1cf9c14fbf | -6.49781 | -43.47941 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75711490-98eb-3ba7-bdda-6648953dd57a | -12.59211 | -44.79576 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 518808b9-8f0f-3022-b595-deea7f5fa563 | -6.73288 | -44.33062 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7e9442f3-3bb0-3263-a5cd-a0d42faf1849 | -10.32938 | -49.90915 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e8229e4-d10c-3262-859f-86458f96b313 | -7.21712 | -45.33387 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c9965de-6708-30a2-b202-a9cb879872ec | -11.171 | -48.62514 | 2025-07-16 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f67d528-4859-3641-b809-ab764247e4e3 | -12.49093 | -46.92194 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62997416-e069-3ce5-a84d-9f27a70f91e3 | -12.48617 | -46.9291 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b14225f-b9de-377b-8b81-43ccd09ab6e8 | -7.30882 | -45.76656 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d7b1d5e-ac74-38ff-bde7-b4603abcc8c3 | -7.19973 | -43.11978 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 15510c26-6dbf-3f39-b968-6d589d646788 | -12.01925 | -47.78131 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78674371-ae7b-328e-b54b-a60192bfdb03 | -7.50524 | -46.69072 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e106f99-d6b6-3608-9cb2-25c214729493 | -12.07038 | -43.4804 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f20e63d9-a2cb-3118-bc0f-d467293caeb0 | -7.08888 | -43.69413 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f895cbe6-f273-334f-82c5-d85bc1e0757e | -10.2827 | -47.61943 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae8909cb-46bf-3a3f-ad25-fab7bb8e1bd5 | -7.20407 | -45.32788 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f9c8832-5cb1-3ed9-8fce-1a1411636336 | -12.02719 | -47.77834 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bf493be-dd4a-3b25-8782-f53eee69ce84 | -11.72843 | -47.4624 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faa1561e-226e-3cec-ae85-d5c3d51ab4a3 | -6.78327 | -43.02577 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db98c28c-858e-32d4-ad72-26816bca7cca | -12.01997 | -47.77708 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c61670e-5be5-377a-acb0-a5eb9662bf85 | -8.75826 | -46.59505 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dd15729-a94e-3862-8abe-9c884817f2be | -13.0188 | -45.06136 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 11caa681-d6ec-32e9-bdbe-adf234c421c9 | -12.47795 | -46.93567 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b57225d-2fae-3a0d-af10-fb32dd7682b7 | -7.19697 | -43.1158 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dca457ad-0c14-3d8f-b984-9b3eb4af2045 | -8.33049 | -46.81905 | 2025-07-16 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fc38d43-d39d-3827-bd6f-f3f64ce236a2 | -12.07093 | -43.4768 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 466a3603-b334-33b0-b6ee-1999a3ef96a1 | -10.89188 | -49.2149 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92810075-fb23-3d58-9573-ef3cc18eaab6 | -8.90832 | -47.34148 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c1ed108-77f7-3070-b9be-093920aaac6e | -6.72232 | -44.33254 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3d860fd-9b90-31ff-8534-9f975f5bb448 | -8.75471 | -46.59449 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f008084-40ba-3409-93f3-fd26066ecc2b | -7.90527 | -55.42396 | 2025-07-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c39e7818-00b6-3ff4-ba5d-fa1e9273bdbe | -7.05172 | -43.47915 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11a0ea56-a579-3362-b96c-3b83fbc9b3a9 | -13.0535 | -47.80719 | 2025-07-16 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cd3a2df-3d58-3b47-93ca-91b70b19a24b | -7.19642 | -43.11926 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 41af0317-a23a-3e76-9216-39a5f6b80fd3 | -12.99482 | -44.86951 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ecfda6e-9404-3b48-8595-78fc7972a9b4 | -7.26252 | -39.19672 | 2025-07-16 04:14:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05566eb4-3179-3282-8846-a26ad75b77ab | -13.01219 | -45.06027 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9fe37c71-0eb8-39e9-91f7-3b91d53b1614 | -9.70132 | -56.18298 | 2025-07-16 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0d109b2-ae42-33d8-ae98-135088f93b4b | -13.01438 | -45.06787 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6e48f689-f266-35e0-9acc-231739768da4 | -9.30844 | -44.84615 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86df6ce5-4c7e-3f81-a4a8-11cf87e53cd9 | -7.1832 | -43.11719 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba805e3e-5b6e-381f-bb94-9c779dd78dd1 | -11.7293 | -48.51704 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c07b0216-7d8f-3f34-8d5c-d9fdb1ba99af | -7.10591 | -43.65071 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2f56408-cf68-3608-8b66-98a5973a4390 | -9.43316 | -40.36293 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| a652b303-81c7-3ff7-9d68-bd2ed282f9c0 | -12.57869 | -44.751 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03ea5b25-2c16-3fd0-80ae-ee9c64cf0b3c | -11.59064 | -47.3143 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d749631c-b0fc-3c41-a086-b1a739c3c908 | -6.94339 | -44.94377 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a80cbb2-7c3b-326b-af89-a3cdab44fa13 | -6.71232 | -44.33094 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ac25296-bab4-3007-96a4-8b58839a2507 | -12.03623 | -48.76814 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3392451a-610c-3008-a302-d25169db397f | -7.46691 | -43.83961 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cd8bf30-85ae-398b-9799-b88519f12efc | -12.48552 | -46.93298 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8081a78d-f407-39a0-a743-f8cd720b2fa7 | -13.04992 | -47.80661 | 2025-07-16 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2d328c-6696-32a0-9984-d9f330ef973f | -8.53281 | -47.85257 | 2025-07-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4217ccdb-bca1-3251-bc66-e40dc46dd63e | -10.64539 | -49.47348 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8a20570-3f9f-3f37-8ec6-0545fa5ffa11 | -8.32759 | -46.8142 | 2025-07-16 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55b1963e-325a-3c8c-add6-618925942b86 | -10.64882 | -49.47783 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4ba0810-4dc3-354c-a8e3-d697d51a762d | -6.88354 | -42.77509 | 2025-07-16 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56a3bba2-7a9b-3511-9538-ea33d7466d08 | -11.47356 | -47.32063 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1f8f8ff9-6514-31be-bbe1-d5ba3f7aee86 | -6.91348 | -52.85663 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c364fb4-029a-32a8-8c20-d3e9a0ec0f27 | -10.89648 | -49.2121 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29ca70ea-f26b-3963-89a7-b50f2c03ba15 | -7.21772 | -45.33015 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2062ccc-9b69-3bbb-8c48-81d26b03040b | -12.48401 | -46.92075 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de0efe59-b389-3df1-9b94-b6c0e5ec0942 | -9.3151 | -44.84723 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04fa389d-55e5-365f-a0e5-de8e9c319ed5 | -7.04842 | -43.47862 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce3db970-6fed-3d32-ac00-3cf178a46d94 | -11.456 | -45.10098 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 676c1cbc-d577-3c2f-beb9-a39e199af77f | -12.99315 | -44.88007 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 088b1499-5fd1-3267-bcdd-cb0f3c99d276 | -9.70772 | -56.18412 | 2025-07-16 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3c314e1-5b9c-34ff-a79e-8e863091a257 | -6.70955 | -44.32689 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0e15a65f-b560-3774-94f5-d57a471cc277 | -11.47424 | -47.31654 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 423833b0-df64-3f57-8541-ba590a82e6d9 | -11.47137 | -47.31184 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b7e1ead-660b-38cc-9ac2-03de0fefbb88 | -6.94281 | -44.94738 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 225c9be7-3732-3dbf-a3e7-383f944b5649 | -10.33358 | -49.90991 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b180e42f-fc77-350b-be27-0e75e803b651 | -12.99259 | -44.88359 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f4ed0a4-abc7-3bb1-883b-f11300f94bf8 | -12.15595 | -44.67437 | 2025-07-16 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c5d0932-99c2-33df-81f4-985c7dadc3f4 | -6.43154 | -43.53266 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15d23b7e-a280-3d94-ba36-a8d363a5cdb5 | -11.49621 | -48.07853 | 2025-07-16 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dfc9110-81a5-3d4e-af8d-d136bd3f6cd5 | -9.73983 | -48.63726 | 2025-07-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed1182aa-29a7-3368-8d43-53454a1ad074 | -12.02286 | -47.78192 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a02916c3-e669-339b-a71d-bc3a36ffe008 | -6.18215 | -45.87838 | 2025-07-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af04518d-9956-3e61-bee7-da42da857fdf | -6.86667 | -41.73117 | 2025-07-16 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ab8dbb27-2701-3438-a14d-b5d9f2d022c3 | -10.32237 | -49.9241 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a2d78a3-3eef-32c6-bf28-0dde4f3f30d6 | -10.56473 | -49.13803 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e17aee5-8e28-3caf-a922-6373ac2cd28f | -11.87399 | -55.45046 | 2025-07-16 04:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e32933a-842e-3946-9906-1649628827b5 | -9.60239 | -43.85028 | 2025-07-16 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| caee9e49-d428-35fc-8eb9-ab9e18ae2574 | -10.90047 | -49.21273 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README18.md)
