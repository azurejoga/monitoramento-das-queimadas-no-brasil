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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f68685-219d-31aa-b08d-33dc67e8833f | -3.10028 | -54.28251 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a2f5d113-c6e9-363a-b39f-9286cdf31c10 | -2.87003 | -54.20872 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 133267d6-f0a4-3398-8966-88a1fc8d2145 | -8.33732 | -44.74325 | 2026-10-07 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f728a9-9c4c-3dba-8ddb-d858731462bb | -5.72136 | -45.16381 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36e7c76e-83a7-3cc0-ad81-8ef532b4361e | -2.41489 | -46.03528 | 2026-10-07 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af6c9a45-0842-36d8-97ba-fba310007b20 | -4.62451 | -43.50543 | 2026-10-07 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f863388-14eb-381e-8a45-2828a60d1b38 | -3.05655 | -54.16145 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1515767-63a0-3b1f-864d-21ae07db1a0f | -2.77944 | -51.6723 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e876187-1cfd-3c25-bf95-8ade37858eb2 | -5.24272 | -50.91958 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| affeba24-8d4d-33d0-9861-d09e7cf05b82 | -3.21221 | -53.88348 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6183ef3-453c-3b23-a000-b54f60ca90db | -2.56541 | -50.68166 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8feb1c46-bcb1-3f86-9617-dc42777d1a36 | -5.09438 | -45.83749 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 758cb7a5-7a1d-360d-bb4f-3ae65d26613c | -3.18362 | -50.54581 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 53cbf593-0e38-3921-be4d-b3a3d5cd7114 | -6.92023 | -43.66183 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e1ecb96e-1e4c-3512-8d62-3a55ce7abfce | -3.20774 | -53.87294 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41748846-e645-3c93-b9f6-b07f14087921 | -5.73228 | -45.1617 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17b0cf0b-29b9-35b2-a316-e47cad825377 | -3.58786 | -54.30897 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7efb8398-5165-3b1f-952b-b199b91c85cc | -7.20271 | -44.29988 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7b1c91d-c8a3-359c-8df7-d7551ac68332 | -3.03024 | -53.9174 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1651263e-68a8-3bef-bc60-d47f03ca69f3 | -3.05039 | -54.21356 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a671f23-30a8-3b9f-ab74-e148bcd984e3 | -3.18481 | -50.56903 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0915b731-0393-36ee-b24d-f745e93d8166 | -7.37721 | -46.2139 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a89aab41-8700-3119-8e56-5709e147d4eb | -3.50874 | -54.66061 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe8aa79f-e564-3c49-8864-e3fb4ef02f79 | -7.47789 | -42.79716 | 2026-10-07 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a79556b-45d1-3fc0-bbe2-66a7000becce | -5.73167 | -45.16546 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 227d4411-ddf0-31dd-bd28-130bfd7da93c | -4.76416 | -55.67664 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 300e54dd-9bd8-32fc-84e8-ccc64dce6db2 | -2.88096 | -51.03428 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b18324d-7e11-3d2f-a3fd-d5eb9cfdc4be | -2.15049 | -51.98147 | 2026-10-07 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7940874-3c2c-3609-85d4-717b180bd332 | -7.18963 | -52.62566 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b30a7239-73ed-3db1-adf5-809b1e8be48b | -1.27855 | -54.56298 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27447e43-adf4-37ad-a9da-67ed684d5c78 | -5.38058 | -44.15693 | 2026-10-07 04:19:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d62223e1-6f0c-3b40-a568-3a6fc11ad129 | -3.41232 | -39.28423 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8a967ca4-0005-3ec5-883d-654e692e2152 | -5.06943 | -45.58879 | 2026-10-07 04:19:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8afd1102-015d-3323-b9ab-84cd75cc827e | -3.20693 | -53.87754 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e4443c6-f2b1-316b-b543-4ddf799c3ad4 | -5.72763 | -45.16867 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2cde6c2f-40b0-3058-9c71-275a5ac8925e | -3.14852 | -51.62602 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bcfee12-521f-3b5f-bf2c-8c7dcdf6f31c | -4.25441 | -46.38172 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544a68e3-2b6c-300a-9d95-9cbcb4ea278a | -5.71854 | -45.15948 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fd2cd2f4-be7f-3f06-ba7b-94679521993f | -3.28004 | -54.07127 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 16f58151-f634-3f75-9578-2a169153cbee | -3.27178 | -54.0163 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03e231ff-caa1-3588-ae03-25e329b9959d | -4.28495 | -50.78742 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69737ca6-0048-331b-8c29-9f0abb112b74 | -5.73877 | -41.65281 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8aaddf15-0b95-3000-841c-8560b3a6b4d5 | -4.92003 | -55.86631 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6e52174-37db-33b7-bee9-a9f09a410760 | -3.53067 | -54.64803 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97f450a4-ad7e-37be-ac13-1d142afd06c6 | -3.06325 | -54.2528 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b598109d-f708-3033-b7ef-aeccf876d006 | -7.56074 | -46.73322 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06bde829-57c4-3fb2-8cd7-fa4e63e73220 | -6.92135 | -41.23489 | 2026-10-07 04:19:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6f73687-2c2f-3cf6-a8a2-7388cbbf1e6e | -2.87365 | -54.14768 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9daa4ff8-16d3-3364-8fdc-29754aadab4e | -3.10851 | -51.24866 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 178e1e4c-5b3b-30c4-89d8-a3999fa6a7e8 | -6.98655 | -43.22191 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6bc510e4-adb2-38be-8240-73a9ca9fb90a | -3.0515 | -54.2272 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05b5d213-1911-33ad-864d-7425a9767af2 | -3.02468 | -53.91973 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be60a7f3-3da4-34b1-9b2e-c4b1eeed1159 | -3.54276 | -50.09919 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff35c4f-1ceb-30c5-8153-79a156bbcb62 | -3.18576 | -50.56337 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f66bbb55-355e-3921-803c-825345f02551 | -3.09243 | -51.37884 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a111eb68-a69f-3935-b292-402d51a362b2 | -3.06589 | -54.2562 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4cbcc687-fd72-32f2-98fe-37d4a579ff32 | -4.3445 | -47.76951 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d56386-d760-30d3-83c4-beda71ae3c67 | -3.51607 | -54.6563 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58d65ce8-fae5-3241-8db0-f680a482bc99 | -7.46607 | -43.00269 | 2026-10-07 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d6cda2a9-a741-3b56-a215-e3bef08370df | -3.29504 | -54.05865 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 698498db-9792-3121-bba2-3cb04de8846b | -3.21752 | -53.8893 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddab7a7f-a027-3417-98f0-54684d005001 | -5.72305 | -41.68716 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 055d06b2-36ed-3ec1-a72f-61102b9f814e | -3.07135 | -54.26209 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d8a1804-15c9-3b2b-ae0d-daece873dd5c | -3.18762 | -50.55222 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71672eed-65d7-33f1-8d66-f85cb4c9523b | -3.08867 | -53.72374 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 597f3a24-d176-3495-a0ec-c3a4136c56a1 | -3.28858 | -54.0228 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9b77bdd6-939e-3ca3-84b9-cbf8201385de | -3.10673 | -53.76528 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61958d41-f0b0-3770-b874-9dd2aa62152c | -4.91507 | -55.86839 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a967e2eb-6fe8-336a-9e7a-394d4d877349 | -3.27008 | -50.41907 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83d42891-2825-3f60-8873-abf556d764cd | -3.02863 | -53.89579 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4f16b0f-6c27-3f23-a99e-b6fb28a27ac1 | -3.62601 | -55.28481 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2041ab4-354f-3211-8d2a-01b718ac79f9 | -4.91322 | -55.86551 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8489cd9-e4c2-3049-a7e9-af3443e48d14 | -6.44221 | -55.02635 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8787cec-2caa-3de7-9a27-1ffe8158b2f5 | -3.16319 | -50.44482 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48f07271-efb3-3dec-a9b3-15a1255ae5e8 | -7.20938 | -44.29722 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e054abe-3904-3ed8-ba90-547b975e96f4 | -8.58543 | -45.67225 | 2026-10-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d3d4e75-2e0d-398b-b2f1-b6ed3eff9b52 | -2.99956 | -54.13286 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 578ec8fc-ea74-3fc9-b1ca-36e95b58e710 | -2.86632 | -54.21131 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad32378f-453a-32d9-b597-8dc1e98f95e8 | -3.49567 | -54.66536 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 679ae506-4b56-315a-b0ef-439f59e05b21 | -3.09225 | -54.29149 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e3ef446b-3deb-3943-99cf-872a068af251 | -6.21106 | -52.83619 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 042a79ed-4f13-3ae1-a230-355914d7b97c | -7.85007 | -44.20296 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8ea787a2-1fdd-3a78-b230-3d931658b2e9 | -2.86649 | -54.15194 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e2dc271-70d3-30da-854f-b1f914677caa | -3.08396 | -54.2642 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eb3fe3a-ef48-3d3a-9441-a47a847ce593 | -6.73022 | -45.80217 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa632b87-a506-3b0d-b957-ff7392a8de51 | -3.22988 | -53.891 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e36108-28b5-3561-86ed-aab7d81da305 | -6.03133 | -42.2763 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2533a217-edee-3024-8c2c-03dd13c19506 | -8.2128 | -46.35709 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0380ba7-95f4-3da6-8d2e-78dffe8e5a9c | -3.27843 | -54.05228 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2488e72-f52e-3246-a223-dbd1780f36f8 | -3.04549 | -53.93968 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 571a7232-22eb-3330-8d16-3dc6ac28a43f | -3.27304 | -54.04644 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 88306a22-73fe-30e7-8c6a-343df21b3354 | -3.27096 | -50.41363 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a94b2b7-6c9e-36bf-b2d8-04476f9b3667 | -6.02298 | -42.26419 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 345c0f50-388d-38d6-b5a4-7c791a7b3a2b | -3.06875 | -54.25864 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b48d64d-9672-3a84-9853-8400232baff0 | -1.28411 | -54.57011 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca99bf51-9fe3-3b46-bddd-3cf940c457f5 | -3.0249 | -53.91153 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b81e151d-acbd-36d7-815b-b5e8d53b4c2f | -3.06211 | -54.22083 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8d19dbb-6bd0-33ce-a4c2-1eb8caf97754 | -5.72884 | -45.16115 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7c68d5fb-27c3-3e0f-b5d6-6bac0856b5f0 | -3.02627 | -53.91009 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ffa05e38-0dda-335d-b59a-4360c716f1be | -3.99844 | -56.26017 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
