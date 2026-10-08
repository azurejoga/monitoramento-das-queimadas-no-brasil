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

## Dados Diários - Página 236

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78cdbf4b-bafc-39f7-9869-08206c70205d | -8.9438 | -45.1664 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3726941d-7bdf-30f2-bc21-2c9f6c5d94d1 | -5.7789 | -42.0558 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 14e02031-fcfb-385f-9eb4-216d04545b33 | -8.95508 | -45.14021 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 4af930e8-3e9a-3bee-87e0-6d5b5da7ccb3 | -11.22483 | -45.26433 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| fae6bd37-afcd-3d4f-920c-b9b47f3c2ec1 | -6.65053 | -43.76434 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 400c75dc-5ebe-3933-ab71-04c30d675090 | -6.15913 | -42.5903 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 768eab7a-d720-3ff8-9cb8-7767067446a8 | -5.69578 | -45.28967 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b46d59c3-891b-3bb8-a4d3-f8306156737f | -5.38173 | -44.1878 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ea843c56-f161-3b2e-8c2c-7dcb2b60e752 | -6.75629 | -45.13725 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a82ecd4f-c49b-3139-9a27-a8d2b4340509 | -8.93306 | -45.17707 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 326.3 |
| 6f2d1aec-bfe9-31ea-ab6e-0a385ebe2fbb | -10.16677 | -44.67737 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2887a440-5225-30f0-ac0c-5ed0084364c7 | -7.45997 | -42.82595 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| b1ee9a67-8d51-3adb-b6af-0c789c0975a3 | -6.06845 | -44.1047 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 71b7ac2d-257a-3834-b182-ab27270e8263 | -10.03596 | -45.60476 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1e996b50-77df-33bb-aa65-cbeb06ef0ad9 | -7.47473 | -42.85678 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 319d423d-e7b5-3099-8ea5-b2d1bba0ed8a | -5.30928 | -45.72194 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9c224512-5eff-3c5d-9128-ea3b808cd798 | -10.60543 | -43.84089 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 149c7def-12a7-32be-8a3f-e520f8a386a0 | -5.70437 | -41.73426 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 0e0aac5e-eaf2-3429-aac2-a5a49d3977a8 | -7.08423 | -41.50704 | 2026-10-08 15:41:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| faa885ef-4323-3ba3-9dd5-0ab96bb48cdb | -5.43227 | -46.64208 | 2026-10-08 15:41:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 8c0a8505-e94b-31af-8f6b-2d946cdd15aa | -6.691 | -45.29879 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 4b376ee1-00bd-3300-b8aa-f2d49ae65f96 | -5.33022 | -40.9016 | 2026-10-08 15:41:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d8b875ff-b6ab-3259-8d20-5fe0fc869aea | -7.39441 | -44.47403 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4321f081-589c-35ce-9cab-ec2464187169 | -6.15098 | -39.43439 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f02ab046-6d62-3c25-a0b1-e65d82d7abb5 | -11.08777 | -44.02082 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 31f5200a-00c5-38bf-9a71-b5c0f2b19833 | -9.89656 | -44.84599 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 2ee842c6-2abb-35f5-80c9-8f0bf76fffd4 | -6.91197 | -45.46667 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7663955f-34da-37af-8e04-553316f9f508 | -5.74704 | -42.06858 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5178c20a-ddaf-3980-89f6-1c44303e8cdc | -7.77755 | -43.82197 | 2026-10-08 15:41:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e1dc52ed-9629-34a6-816b-6393a05add84 | -6.33073 | -35.12557 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| ff35aeaf-c6a6-3fa8-b231-6470ba55fc46 | -5.16186 | -45.17622 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0138396b-5281-3e06-9f6b-07842c0702c8 | -9.89072 | -44.85251 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 187802df-f21c-3f22-889d-52a0674a53d4 | -6.97406 | -45.1305 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 49d823f8-697b-3405-9dbb-9c1b8ca36664 | -6.66587 | -45.36233 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 383864e0-fdda-3cdf-8490-b2fedcc2eadc | -5.55438 | -45.57196 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e20914d-2439-324c-b70c-e4b8d6010bbb | -10.5695 | -46.29703 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3e527849-ba05-3328-80d7-ba9b5514946b | -9.89787 | -44.80157 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 06ee2212-baab-3408-8089-6eb0cd85c7ae | -6.1542 | -39.44144 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 8be699cd-ab7a-3ba3-985b-a2fd55ecb71f | -9.82993 | -44.78761 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 831561bd-cba2-3136-b96f-0dcea2af4fe2 | -8.12653 | -35.9164 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| db4670d4-8f0f-33eb-9c96-b80990264f46 | -6.81619 | -45.05202 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a6917a48-916a-3803-8e8e-ebbdfa628e6d | -6.42181 | -44.92096 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef21a053-952a-38ea-9887-0b69e80689ab | -7.5372 | -45.86982 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 85b0683f-1f10-3351-8332-ce80bcffc471 | -8.84102 | -45.44836 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 5c54ee56-95fe-35b9-ad88-956f71027147 | -6.39294 | -44.94399 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7c934da2-9ac0-3765-8e2c-ddcf225920c6 | -7.05002 | -44.33644 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4f929087-e957-3c62-b246-d1565dc91efc | -6.88941 | -43.68859 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c69180b1-8b3c-3458-b036-6386155ce1dc | -5.69893 | -41.73215 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 99ee10b3-40a5-3e9c-b4f0-6c7588985934 | -9.53133 | -45.63037 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 81056431-3788-3e71-86c5-0fdddc970599 | -10.92925 | -45.38403 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| f6b68d12-ce11-3634-8239-4980f88e4780 | -9.03023 | -44.37214 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 22954769-6d26-348f-a770-2b5a311bf820 | -7.24913 | -43.76307 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5290935-6a98-3aea-a94e-4981e979ae11 | -6.31534 | -35.13918 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| 2f2b0b7d-f76c-3ef5-847e-edafbe8b6dbb | -5.32415 | -40.89276 | 2026-10-08 15:41:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 30852bc6-9619-35d7-8768-98b5341ad62c | -6.68048 | -41.76357 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d6a0e40c-926b-34be-986b-0727eb0118a4 | -5.95626 | -40.93367 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| f8b22015-826e-3623-a454-d5d692194282 | -10.87254 | -45.55929 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 710fae5a-0bae-3af8-9d02-ae49b9265c63 | -6.94999 | -44.89847 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37fb192e-3e5f-3b75-8b57-606655054c83 | -5.37697 | -44.19678 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 9b4c8bc0-9d40-338d-bfb5-1c2649649f1d | -9.89003 | -44.84676 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d3139585-5123-37a1-b0fc-608543f4f6ae | -8.89461 | -45.39011 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8bc33e45-dd90-3add-b295-fa874a1c88d1 | -11.08718 | -44.01579 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| f2352232-0b5c-3f11-9bb8-af2053b8592a | -6.57577 | -44.86485 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2434defe-8bec-3ddd-b9cf-43a117a44330 | -4.85918 | -42.99731 | 2026-10-08 15:41:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d4e8461b-46f3-396d-9349-c7a92c1471a9 | -6.14866 | -39.43375 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0ea63603-bff0-3cbf-803c-19013776988f | -9.97581 | -43.49571 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 5f4268e2-0894-377a-9c9a-58f320941f25 | -7.69466 | -35.22578 | 2026-10-08 15:41:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d1d795a7-1825-359f-a802-a57a21b09b28 | -6.92756 | -43.6632 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 851ea609-2437-33ac-b013-d75d72caa33f | -6.67308 | -45.36684 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 4f64d24b-3e6b-3dcf-bacc-f26bf3129d04 | -5.74224 | -41.7148 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cc1299f8-c072-3025-a6da-1366b59768bb | -9.78465 | -46.27496 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6cfa50e5-fb95-3a3a-bc8a-483b790d9913 | -6.50378 | -42.03283 | 2026-10-08 15:41:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| b0e01d51-c47e-3172-a2e5-e9bbcb70c022 | -6.15573 | -42.58188 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 795b93b7-b3da-3724-b26f-4d6d36a5091d | -5.38706 | -44.18292 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e8293252-4fdc-3267-b714-b2903fb873c9 | -10.37883 | -46.3056 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 381.3 |
| 0d85b693-2cb6-3fb8-84bd-a73531ccee0c | -9.13596 | -45.84546 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e14fdb2d-9fa3-3e15-8b95-96ac79e5f026 | -6.41251 | -44.94696 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c75ec994-af60-3a19-bf91-6ad1fa08aea5 | -6.86314 | -39.15604 | 2026-10-08 15:41:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bb6069e6-f0f9-38b2-ba7f-1dae7f095253 | -6.68603 | -41.76598 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b4887287-0863-33ab-8979-3354c2d09fda | -7.70104 | -45.43211 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 77a8e238-70a6-3455-8ec8-fb682546c5df | -7.26124 | -44.22262 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ebf579d2-1284-365e-9178-c9efdc519ccd | -6.32093 | -35.15343 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 18b42c9f-83b8-3ebd-aaac-f3aee13041e8 | -9.89913 | -44.81215 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| c9150e13-0d54-3874-b1b3-3988d88f1855 | -6.63007 | -44.88951 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 313da742-b228-3a02-ad23-de7653d066fa | -5.74881 | -41.65172 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b5b6e3e3-e979-3972-89d6-a60755c6786a | -7.06723 | -40.94204 | 2026-10-08 15:41:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4a85ebd0-74d1-3e00-b964-dc9598a6dd9f | -5.72174 | -41.64052 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 64ac88dc-1914-3b60-8dc4-526ea44904e5 | -5.50298 | -40.53581 | 2026-10-08 15:41:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 194ac430-4fe8-3430-949e-96eecd0d5aa9 | -6.57268 | -41.6147 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 5ce1079e-b878-317c-8616-bd91f8e5f2d4 | -6.73514 | -38.32672 | 2026-10-08 15:41:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 08bdaccc-1ebf-353f-860a-963ff8ba32b4 | -5.71731 | -41.64677 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b60390fa-830f-3523-a173-a36f6e5f29d0 | -7.04488 | -44.33719 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7f97f6de-3a44-3e09-90fb-27bed211efdc | -9.0296 | -44.3672 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6c05e22c-677b-3cb7-8285-674615f7abc5 | -8.6049 | -45.63317 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| af578deb-7473-33ca-bba8-813f94f76c3e | -7.48986 | -42.79914 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3b88f5de-4335-397c-86eb-ddc5b72c5f20 | -6.85403 | -41.76873 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 01dc0cc0-5584-3593-9855-700b969fc957 | -6.15646 | -39.44212 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 3bcc6b72-015d-35d4-9388-e64f1910ea41 | -5.70774 | -41.75777 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 19e97c4e-5609-364e-b6f7-30f855a098e5 | -5.7132 | -41.75996 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6d789680-333d-3c05-842d-1d7e3386ef0e | -10.34494 | -46.23079 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |


[Clique aqui para ver as próximas entradas](README237.md)
