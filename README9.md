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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e07b61-4f3c-3788-a0ab-b62165f37089 | -7.80875 | -37.59762 | 2025-10-11 03:40:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b5f24d5-7a2d-3659-b5f5-8872a28a90c4 | -6.22477 | -42.48195 | 2025-10-11 03:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ef9098c3-5d69-3aca-a335-183ed20d5c47 | -3.69237 | -43.20019 | 2025-10-11 03:40:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b257c0a4-bb27-32c2-94ab-b1f93a25cc15 | -6.91748 | -43.58122 | 2025-10-11 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0fabcf04-11f5-3039-b3ff-5621d1923ebc | -4.41089 | -43.47366 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a055d013-58a4-31f5-8352-cd53049783ba | -5.94015 | -42.27996 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5d159970-617d-308a-9c2a-dd1156985e35 | -5.32646 | -43.09227 | 2025-10-11 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9a9bf2a5-2994-3a42-99f8-598985e8f31a | -7.14368 | -44.13322 | 2025-10-11 03:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a8be41f-deae-3216-bd77-885b869aa055 | -5.48322 | -43.07459 | 2025-10-11 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7becd59e-47d3-305f-bac3-e8937515ead1 | -7.36476 | -38.76028 | 2025-10-11 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 08427e03-ef34-3237-9acc-e8dba76be130 | -2.51569 | -44.12192 | 2025-10-11 03:40:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb533770-f134-3129-8bf6-ab70b9bbb8cf | -6.4616 | -44.23458 | 2025-10-11 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c778d5a6-5785-35a2-b1fb-231fdcaa4ee7 | -6.75829 | -39.67326 | 2025-10-11 03:40:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee142c90-b525-348a-b547-7ce150595a2f | -6.74248 | -42.81544 | 2025-10-11 03:40:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a4d3a531-ed30-3f54-b9b0-a7140ea0af43 | -4.41178 | -43.46937 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad6aa2f4-0b44-32cb-b06c-40645c908b32 | -4.41668 | -43.47145 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c6d4ec56-3089-3a4d-88ac-a4db9a886070 | -5.8562 | -42.85184 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 11d9b64c-429c-36eb-b0d5-c6fbac5d5604 | -6.81788 | -42.80339 | 2025-10-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 11536fe4-6fe8-33a7-9b3f-189ec6fc36fd | -6.04367 | -42.50557 | 2025-10-11 03:40:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2335d928-2b86-3639-bbae-b68c4b33b85a | -6.42255 | -43.59469 | 2025-10-11 03:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 257b1f12-91dc-3c1f-976d-ad9c4afdedbe | -6.04278 | -42.51075 | 2025-10-11 03:40:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 97728f28-ab54-3d1a-b462-105aca8f7d39 | -5.59017 | -41.10892 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5cc2634e-309e-38f1-9fab-16b8f69d40cf | -6.2474 | -42.75325 | 2025-10-11 03:40:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| cdf49b38-07e8-3578-a762-829bfa3e1874 | -5.22125 | -45.65271 | 2025-10-11 03:40:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a61d86-6295-3ab2-ae67-a4b046d53723 | -4.42604 | -43.47978 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15eaf58c-90c9-36a0-a87d-2fda8b019e34 | -5.86208 | -42.84706 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 53ec132f-0d40-3b59-8aa6-98320e812bb7 | -5.28366 | -45.27116 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fed523e-d0fe-3aa7-a382-4fcad8545453 | -5.86014 | -42.85835 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 1796917c-4678-3080-9ede-ec06d0b14b4d | -4.53638 | -38.46469 | 2025-10-11 03:40:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9c21dbe3-23fb-3d35-b19f-6583693d46fd | -5.48823 | -43.07549 | 2025-10-11 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0012e9e-4229-33ca-9500-6b23aff9914c | -6.00548 | -42.88753 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7a2e372b-b983-3f15-a9ef-d486e5dd38ba | -4.89906 | -41.54303 | 2025-10-11 03:40:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e61855d-aed6-365c-acba-e8236967de12 | -6.91696 | -43.58413 | 2025-10-11 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6bdfa6e7-827f-381f-9907-9d43a8905a29 | -5.27829 | -45.27189 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e72bec12-d348-353f-bc89-71e736784e3a | -5.2841 | -45.27303 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 398dc1fd-8f8c-3f7d-85b7-a3dcf862218c | -5.87654 | -45.29644 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d9dd822-deda-36e7-b058-6e9153322381 | -6.25713 | -42.97452 | 2025-10-11 03:40:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9fdf91a8-c343-36ca-9aa4-31c10a60796a | -4.40566 | -43.47265 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af84d0e4-0f10-3448-ade6-6c8c3d64bbd6 | -6.18617 | -42.56473 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6024fddb-8e05-3904-9d15-649c2e1076f5 | -4.41125 | -43.47258 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5897c1bc-ce26-3266-9b63-6fac6eef18cc | -4.42687 | -47.60447 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d157dcbc-a06c-335a-acf5-e43cc7ec9e07 | -6.80913 | -44.64035 | 2025-10-11 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1df16318-ed6d-3c55-80e6-7cfb1aad71d2 | -5.84617 | -42.30989 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6cad72e5-371f-3cf7-84e9-0ce4e7691960 | -5.22045 | -45.65718 | 2025-10-11 03:40:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b7cfd2-3dbd-3fa4-a780-469c3b72380a | -6.32799 | -41.60713 | 2025-10-11 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32364402-c05d-33a3-a474-d598f98a06b9 | -3.84649 | -42.16864 | 2025-10-11 03:40:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45a40b16-e73e-3f92-82f9-af695f30519c | -5.86697 | -42.84805 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| ca050422-2a2a-3188-86a9-f1a09ceab388 | -5.40072 | -40.97458 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4cd4c077-d93d-396f-a37b-1694771ec743 | -5.86506 | -42.85915 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| d9c2f51c-3002-343f-a7c8-59f018b785c4 | -5.85717 | -42.84624 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| fdf3977c-4263-388a-9415-1efc5a833c95 | -5.46324 | -43.5277 | 2025-10-11 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52d5bc69-a166-3e95-9315-7a6b31dfea03 | -6.1819 | -39.70609 | 2025-10-11 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 166be0cc-d382-3b35-9727-16bb053ebb49 | -7.14727 | -44.1434 | 2025-10-11 03:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dde20e96-6e0b-34fb-95e4-1dea3f4d8d3c | -4.48114 | -42.86363 | 2025-10-11 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da51e63a-75dd-3434-b49f-0d00a02fddd5 | -5.42923 | -41.36368 | 2025-10-11 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1022147-a3bb-3c09-b762-55a0cabf854e | -7.42228 | -42.97435 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a5de8424-0299-33e1-883c-61a838c77b59 | -7.3363 | -43.86592 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52fd74d0-d8ee-3803-ad06-435a5f31f4bc | -13.49926 | -43.67025 | 2025-10-11 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48f1863d-e68e-314d-b671-24d911e77ffe | -12.45038 | -45.07616 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f36bb136-158d-347f-88a7-4399c7eea610 | -7.52969 | -44.29857 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b0aa94b-7ca9-328e-973a-eae4a31baa72 | -7.79922 | -44.12128 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26784a8a-4cfa-3210-a302-a561152e1a5f | -7.49934 | -43.10446 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09da0e49-db78-36c2-ac24-a64d7087d29f | -12.75901 | -45.88429 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99d6134f-70d7-3f72-86a3-d708f7b9de7f | -7.85689 | -44.49169 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60923fdd-16fe-3751-a736-920158afaafd | -12.92022 | -45.05343 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e927d33-b315-3a28-b58d-e2a5fa9bcb6a | -10.17739 | -44.54492 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90760831-8434-3109-9c1d-680a4b170440 | -8.58126 | -44.89306 | 2025-10-11 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 867c1e31-3865-3a3d-8c75-caf36855a766 | -11.45085 | -43.48064 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bd76dba-db06-3d93-8e1a-dab1d6b48e84 | -10.87678 | -44.19527 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 484432bc-963c-3029-8ef2-c335e604abed | -7.80248 | -42.43073 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41624117-41df-3b0a-8e0d-5b703995d451 | -6.94505 | -45.60233 | 2025-10-11 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 088edb3a-39d0-3aaa-848d-dde9aed97dd8 | -8.20658 | -43.34684 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| eb27a29a-9fcf-3cfc-ac86-1e364a90c4f6 | -11.02558 | -44.64353 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62ba94f1-6725-32bd-924f-30f168e633ef | -7.86519 | -44.4759 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e2df727-3939-3f5c-98f2-555c3a378d23 | -10.51823 | -47.35635 | 2025-10-11 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70ddef79-7244-391d-ab94-bb473534bd1e | -12.63269 | -48.32246 | 2025-10-11 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 78f93b12-e466-3ce1-a399-f8d28893e044 | -7.85987 | -44.47508 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44de084b-4278-3792-91b0-53e46849a650 | -7.41261 | -42.97275 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 096b54e1-8df0-3fb9-96b5-e72c1907848f | -8.4981 | -40.75415 | 2025-10-11 03:42:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b564545e-e991-379d-b31c-44c005be2b8a | -11.77319 | -46.37764 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4601752-ea7c-3164-a543-29346e6abc1a | -9.10678 | -45.03274 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc610d88-303f-304a-abfa-12b7cbbbde2e | -7.85279 | -44.12654 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4afef0ec-bd1d-3591-8261-51b4eedfb520 | -6.94433 | -45.60643 | 2025-10-11 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcf9672b-5320-3275-ad6b-c708c8b4e5b3 | -6.94486 | -45.60276 | 2025-10-11 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 311cecf1-d062-3cd6-b01a-7f13b7759c27 | -10.15105 | -44.58984 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c0d3898-1bb4-3adb-af63-278f346bb048 | -7.85392 | -44.4778 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5f62f1ac-c494-3be8-a9b6-cb370e56bea8 | -11.75919 | -46.36032 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbf9a973-a598-3dfc-845f-e83d53a3fb89 | -12.22092 | -43.79264 | 2025-10-11 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fc35e02-2fd5-33b8-981c-4f21a5509ae3 | -8.49402 | -40.75343 | 2025-10-11 03:42:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 621e20d7-9059-3556-b042-05046b308b1a | -11.87583 | -45.4968 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcc58fc4-be2f-33cd-a3ae-800f661150e0 | -7.40121 | -45.9216 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbd2ae06-ee9a-3f51-926d-31e5bafead1b | -12.18246 | -48.81301 | 2025-10-11 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1c11710-0266-30ea-b6b9-6afc44324cf3 | -7.4072 | -42.98293 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c99fb287-b3cf-3c29-b5d1-c62e3bc69b32 | -11.91331 | -44.17666 | 2025-10-11 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 904bfadc-892f-3c96-94f6-b4617cde004c | -12.22182 | -43.78778 | 2025-10-11 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ccebda7-861f-399e-bcb8-1c3c116986e6 | -8.40675 | -45.09423 | 2025-10-11 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bad8d23-d42e-333f-9d3d-a024d32f08ba | -10.19193 | -44.60899 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fdfaf72-d965-3065-b302-bc0163dd9d54 | -7.85749 | -44.48839 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f6cf907-f1f3-3773-9100-f247559b555d | -7.41068 | -42.98355 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 20cd0eeb-cbcf-3ed9-82ad-0879ee15b310 | -10.14771 | -44.59 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
