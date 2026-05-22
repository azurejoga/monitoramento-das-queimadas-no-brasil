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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa58c93a-29b6-3a0f-b5a9-a5a7860c3884 | -8.72129 | -48.32153 | 2026-05-22 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a65e9a75-8ac9-3416-b68f-13857bc8419b | -5.77435 | -45.13209 | 2026-05-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 460ace31-e70c-3839-aa73-1eedcb17fdfb | -8.56273 | -45.98944 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9b9b175-945c-3490-abe4-267e9b3e54ac | -8.38734 | -46.24791 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0e6d7c7-1c7e-3bd5-9b4c-4f4df13819a3 | -9.30374 | -45.49751 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0b2c0885-b1cf-3df1-b66c-df468c1c99a3 | -7.7238 | -44.55423 | 2026-05-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 766fdae1-a59e-3558-abee-d6636ee181c0 | -9.29554 | -45.48562 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bfc119e5-b8f1-3820-81e3-f650616ae2a3 | -9.30036 | -45.48625 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 261cf5d1-2adb-3aa0-be95-b728261fde02 | -8.12002 | -44.18037 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d631dc-10ea-3402-a259-634e9d566f19 | -8.55878 | -45.98404 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 02f8fa12-c8e9-3187-a5e1-5490f0e96a92 | -9.40428 | -47.36419 | 2026-05-22 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f38f662c-9cd3-38b7-be20-6736d1e1f402 | -9.92721 | -48.00929 | 2026-05-22 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63305d5e-54e2-3780-8ce2-aa61ba39125d | -8.1185 | -44.17763 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a32ff4b-a7af-3388-8f7a-cabda9dfeb21 | -7.64391 | -45.30702 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 895e5a57-ac99-3746-a655-0bc4f04aed6a | -5.95119 | -43.49035 | 2026-05-22 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f62ec9e1-88e8-3953-8209-9086c1239533 | -7.64401 | -45.30064 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27832b74-caa6-3373-8a11-cd96f4b2b54e | -9.07489 | -49.67775 | 2026-05-22 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52e46c74-21c3-3d6c-8d2f-efb54538cfc5 | -8.12043 | -44.17719 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89cc23c6-cb66-3c54-a598-068fe06f6b2f | -9.22928 | -48.58241 | 2026-05-22 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f54c103-6b17-39b5-b804-1a5bf6765e54 | -8.91982 | -46.91372 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa36fa3b-4d36-3b6c-923e-68143d42a1dd | -8.6582 | -50.33401 | 2026-05-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6799913b-a46c-3bcc-a41a-f2a862effadb | -8.72048 | -48.32384 | 2026-05-22 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f3dfe3e-d666-396e-a274-30bfb7f440ff | -8.92416 | -46.91431 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1bc2f95-694d-3a32-b440-ec1b3f4e2ac0 | -9.39921 | -47.36923 | 2026-05-22 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1145778-7e37-3216-b405-ae43d334d402 | -9.92312 | -48.0087 | 2026-05-22 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc348aed-3955-30d1-abcc-cc01c6713bd9 | -5.77367 | -45.13688 | 2026-05-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f4c4278-57f6-30d1-87de-cd615d968bc0 | -8.92155 | -46.91301 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c669f46-74ec-3ca6-911a-b09e3e77abaa | -8.55417 | -45.98347 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 34dc8e4d-cbb7-3c00-8947-113f6799b15f | -8.55811 | -45.9889 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| de47e6c7-6f3e-3bc5-a711-eaa11d6189d2 | -5.91204 | -45.58138 | 2026-05-22 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35f0d413-206c-3236-b72e-35e13a61e23c | -9.07854 | -49.67831 | 2026-05-22 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08a65d82-a244-350c-82b1-3163d2a21703 | -9.92365 | -48.00498 | 2026-05-22 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d263042-44f7-3ffb-a4a2-043436e6243f | -7.64802 | -45.3065 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a11889c9-d238-3abc-9c65-13d8095cef34 | -8.11763 | -44.18394 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0239e74e-8494-3fe9-ba48-1146144c0851 | -7.05212 | -45.05738 | 2026-05-22 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 063f74ea-b30e-33e9-b9a1-da5036a5f51d | -8.11807 | -44.18079 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 771309e9-ac22-3386-aed0-df45a8d141fa | -7.63854 | -45.30501 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ef766078-a16b-305c-9325-e2f4ad2ccb69 | -8.93514 | -46.91059 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4884600e-85d8-34e2-95de-3c42a3d7bdf3 | -9.29964 | -45.49157 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 68a533ea-c366-3579-85eb-fd767481d17e | -7.64328 | -45.30577 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88adc570-c3e8-3b5e-ac54-df5377ec2254 | -7.6446 | -45.30189 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 29f06af3-02c1-34af-aba3-8a42e4c4aa51 | -6.84881 | -48.73818 | 2026-05-22 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82c0b7bd-ad31-31bf-9136-3dd8bb46b311 | -5.76969 | -45.13129 | 2026-05-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c703fa3-954e-3ab3-96b3-fd00238f9250 | -7.7234 | -44.55712 | 2026-05-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be9fb0de-badc-3e10-bb87-5d3ca16c9e08 | -7.82117 | -48.05548 | 2026-05-22 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 721dd702-a744-3d93-895b-ac5d8798e1eb | -8.93224 | -46.91968 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e465970-6835-3664-bc77-46bc456dcf8d | -8.11919 | -44.1867 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e77967f3-648d-3a92-a6d3-e6e4bae9fb62 | -8.55351 | -45.98833 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f0914db1-418d-317a-b9d1-52c5ce375f39 | -5.9512 | -43.48985 | 2026-05-22 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b59467d4-8514-3ab9-ac43-f3bbe23344f0 | -5.77833 | -45.13769 | 2026-05-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fcad49a-931c-37cd-a937-cb4e98a4decc | -11.30467 | -47.57489 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a7b3aa8-3788-375d-aafc-a6f44b563bc1 | -11.05302 | -46.71284 | 2026-05-22 04:53:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fdf2a11-78eb-3c96-ac74-0d110546e42d | -11.31325 | -47.57613 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd58a7a4-2ac9-3183-b4c8-54ff7a7133f4 | -11.43146 | -49.24917 | 2026-05-22 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 259b4818-ff89-39c6-a735-b72629a26cbd | -9.94965 | -52.46324 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa5d9274-eb27-36fc-8b71-c5a290a45434 | -10.11355 | -52.41312 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e818ba4-7e07-3a32-a99b-d077be176363 | -10.19712 | -52.33525 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1383657-56b9-32e0-9bb5-f046899d94c0 | -12.2664 | -43.51416 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f16f1a40-3ae4-3dd9-8de6-4eae3e5064a0 | -10.42922 | -52.15099 | 2026-05-22 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f41711d8-e6ec-399b-8052-4b496f2031a2 | -12.04517 | -45.2802 | 2026-05-22 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0b708c-5d03-35c4-8259-0a585f008fe7 | -12.24191 | -44.26503 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02fc89f0-0c39-3e4a-a237-1e293eacfcf1 | -12.27114 | -43.52291 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34ff08dc-76ba-3f2b-b09b-403f0116dbe1 | -12.26591 | -43.51819 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a04920c9-149d-3075-8634-68a23b5e8811 | -14.18639 | -52.88776 | 2026-05-22 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97067ec7-3ead-394b-b297-46db56880907 | -10.89122 | -53.73912 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b533f7-5670-3372-ad48-b899f9cb36a9 | -12.23273 | -44.24948 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74d699a0-7aab-3374-afe5-936522fab4e1 | -12.0812 | -48.20489 | 2026-05-22 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f01783b-0693-3df5-ae9e-2066cdd37cca | -11.06332 | -46.70488 | 2026-05-22 04:53:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9aeb3b5-fbb4-3a63-b1bb-b84c8f45a199 | -11.46725 | -52.91885 | 2026-05-22 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12fc388-a14b-3bd6-a318-a1246b12184d | -11.61369 | -47.90269 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 844a5344-61f7-3ac9-b022-ae4c927169a3 | -12.88848 | -47.23879 | 2026-05-22 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 115b783d-a419-3b15-acd4-a7cfb89745c5 | -12.0439 | -45.28093 | 2026-05-22 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fc1d522-f10b-3677-a4c2-7d167057732a | -10.88737 | -53.74209 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e0772b-911a-3a05-bfd1-1e967329b8e3 | -10.88131 | -53.73754 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4ef5fb8-65d0-3356-b143-4ecb5d01d474 | -11.6179 | -47.90334 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b997151-7970-3e1e-a622-22fd04092a46 | -10.89452 | -53.73965 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748d1a62-3515-34c9-8890-fdd7ace34061 | -10.92127 | -54.11016 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdd0e2b9-5977-3a2a-9334-333401a44808 | -10.03439 | -59.35647 | 2026-05-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f8fc947-39e2-3c59-9add-241531f551d7 | -11.44239 | -52.9258 | 2026-05-22 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a56def-cf83-35ad-959b-a1b641d3f246 | -11.95127 | -49.30344 | 2026-05-22 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2254371c-656f-3a3c-8be5-1b33a8c49c02 | -13.28705 | -54.25459 | 2026-05-22 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ba410b-9d9a-375d-bbf5-2e834567ed42 | -10.89397 | -53.74315 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e47ece-f942-3eeb-a250-e0a6dfc7b4c7 | -10.88683 | -53.76707 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 555f1b2b-e242-328d-98aa-88b16d468391 | -11.61509 | -54.17616 | 2026-05-22 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6751f6f8-c26f-396c-981f-22f880bca641 | -9.94192 | -52.46925 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfb012ea-c8b7-3713-999c-61c2da561b3d | -12.23689 | -44.26082 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2764b9c2-c7ff-3815-8988-cdd99cd2e361 | -14.15057 | -52.89713 | 2026-05-22 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0affcd93-2e52-3cda-b026-a0f9d2aeaf5d | -11.31586 | -47.57856 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a219f9-5d0f-39aa-8bb1-aa165decb5f7 | -12.26844 | -43.51318 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f9e72f3-2aba-3f4b-8ab3-42c8f8b468de | -10.88461 | -53.73807 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d906249-2de1-3bcc-a241-e2a3c584dc1c | -10.49583 | -49.36464 | 2026-05-22 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fefd7e36-7b26-3583-8a32-852005ad4e1a | -11.60239 | -54.19213 | 2026-05-22 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d49718-cda4-375b-b249-76cf53f5a536 | -12.2323 | -44.25299 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d78a37d3-bc96-39f1-a0da-222393bba11e | -11.44571 | -52.92632 | 2026-05-22 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b12a779-c937-31ce-b5f0-b57810e73e72 | -10.88682 | -53.74558 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 650ef93f-b06a-32bd-bc0e-143870c26a3f | -10.79913 | -49.40658 | 2026-05-22 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8f9e746-dc91-3f73-ac8c-354fce9eb6bb | -11.05816 | -46.70889 | 2026-05-22 04:53:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85bca645-434f-35d7-9fff-6fc758e18d69 | -11.60896 | -47.90598 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5748999b-cea2-331e-8a90-7c3be0d489a9 | -10.18992 | -54.25883 | 2026-05-22 04:53:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c88a49e-1a71-3597-a19b-09ef7244de39 | -10.49204 | -49.3641 | 2026-05-22 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README6.md)
