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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd7354e2-9dc0-3b6e-95b0-704de6d6b29f | -2.48607 | -55.72128 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68bc8314-edbb-3780-951c-89663f49d74d | -2.48255 | -55.72073 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c27cd9b2-77ed-3f0c-bd02-196711c034c7 | -2.42536 | -55.69262 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf4e077-79f1-36c2-8b51-a4c39a85226e | -3.94214 | -56.06859 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45e6e3d9-8a19-36b8-ab11-42d7505a3195 | -3.90384 | -55.39801 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 475abfe9-f0e9-3371-881e-12f821a1a32c | -3.71431 | -55.48665 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fce9a941-fb4b-382e-8569-db8cd4fb5943 | -4.81514 | -55.85188 | 2024-10-24 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23c8bbeb-6af9-3b1e-8e0c-727d0af3da4d | -4.81301 | -55.85215 | 2024-10-24 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5f067f2-2015-30fa-a58e-c40197abe391 | -4.53813 | -55.75169 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9c0396e-9d4e-3484-8ab4-786a3e7e6fe3 | -4.53468 | -55.75114 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b65f155f-631a-3652-9905-aaebe373aab8 | -4.52904 | -56.00772 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8986b249-214b-3443-876a-b4420bedad9c | -4.51144 | -55.66287 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b98b771d-485c-3358-98de-4a5f46297ff4 | -4.32115 | -55.90908 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebb85dae-b188-3986-adba-8390307b5dc4 | -4.20362 | -55.55494 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86ee958c-028e-30dd-8233-0ab72a271fd5 | -4.20018 | -55.55437 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53a8fb03-816f-3cde-b62e-5a747bcb2e7b | -4.19959 | -55.55809 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1a6de2e9-c17a-3ef1-ba9c-3c94e695473b | -4.19546 | -55.68743 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 762561f4-468a-3844-aeef-7ec8336faa48 | -4.19324 | -55.68772 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f5e58ff-4047-3a46-94fa-b59f8c503416 | -4.01388 | -56.0481 | 2024-10-24 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5c4a55e-498d-342b-aae1-a3166bda080b | -4.01298 | -55.71744 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da97b8e7-3cbd-3760-9f65-1037bb7864c6 | -3.96856 | -55.67211 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d0e981a-f34c-31f7-bd87-47c512b9e78d | -2.10733 | -56.59059 | 2024-10-24 04:55:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcfb2e56-ce9c-375b-82c3-2b1c5c3dc6ba | -1.43703 | -57.92167 | 2024-10-24 04:55:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91e82bce-63d2-3d8d-9cdd-394a5628737c | -2.33428 | -57.0251 | 2024-10-24 04:55:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd5dffdb-04fc-3ddf-b256-5f8f149f6ace | -2.25487 | -56.81767 | 2024-10-24 04:55:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bba76e42-026f-3c8e-a148-4f6912cd1660 | -2.50049 | -58.13098 | 2024-10-24 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8bf3704-8ba7-374d-b5be-182916e797a5 | 1.1208 | -59.44428 | 2024-10-24 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8332ed95-f7c6-3990-a717-1b3854ec7b22 | 1.03379 | -59.60414 | 2024-10-24 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcd8a3b3-cae8-37b9-b64e-f0f0d9989ee2 | 1.0291 | -59.6049 | 2024-10-24 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a01d6cc-851f-38f7-97ae-ada42ac7d7e8 | 0.8705 | -59.61707 | 2024-10-24 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72b06499-bf4c-3bfb-8495-de16490b89dc | 0.86858 | -59.61528 | 2024-10-24 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f415fc2-208a-3f2e-ae2f-eb75bb12cac7 | 0.74815 | -59.80922 | 2024-10-24 04:55:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e2161f-5954-3159-917f-132900b8a44e | -1.41821 | -60.40785 | 2024-10-24 04:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa958d9c-3927-31d1-9e35-9e6c592c0a7b | -6.73531 | -40.4799 | 2024-10-24 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2279c45-5001-35bf-b13e-323dc56b0856 | -6.72813 | -40.47931 | 2024-10-24 04:55:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb9b390c-0521-3af1-85f9-ab5e39d360c1 | -3.85272 | -40.69929 | 2024-10-24 04:55:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e27d5d54-4070-3ef7-b9ae-0fc1fabca8bd | -3.71536 | -41.68304 | 2024-10-24 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a9432113-1bf8-3172-b365-059d6cc07220 | -3.71464 | -41.68819 | 2024-10-24 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0cf747e9-9d2c-3542-8be4-6312a0208fc3 | -3.71358 | -41.68223 | 2024-10-24 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c794a58e-7121-355d-98da-c9dbf798addc | -3.71282 | -41.68736 | 2024-10-24 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 23736db9-f30f-3643-808d-21d5218fd2eb | -3.70644 | -41.68641 | 2024-10-24 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7ac31255-35e7-30ca-b5f2-3062fe329fcf | -5.90868 | -42.88595 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5324f68-093e-381f-8d62-328fd840f059 | -5.9084 | -42.88431 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7225bf76-5137-35d2-8978-4950e477e79e | -5.90777 | -42.88878 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4846449f-036a-3f25-ab7f-729f9eedbeee | -5.90258 | -42.88503 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30fcb408-cfc8-3b05-ac65-6755d52f8003 | -5.9023 | -42.88346 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16655618-3968-326d-9396-a14c79cbbde4 | -5.90169 | -42.88774 | 2024-10-24 04:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39bc4aae-5d0d-3852-84bd-7c65cd955212 | -7.72134 | -43.77108 | 2024-10-24 04:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44ddef66-3070-3125-afe4-f92940d9a0ff | -7.71542 | -43.77031 | 2024-10-24 04:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbeacfd1-c233-3191-9292-f8c49f09c191 | -7.06834 | -42.55373 | 2024-10-24 04:55:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e22252a8-105c-34d2-95bc-b3100bf90241 | -7.06769 | -42.55857 | 2024-10-24 04:55:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7f6833f9-69ba-3381-b89a-203ec4408fb4 | -3.52834 | -43.61219 | 2024-10-24 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c64684ec-236f-38b8-839f-8c1c0c2882de | -3.52779 | -43.61588 | 2024-10-24 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cdecfc1-c3ac-3f8a-a13e-dde4c117ed5e | -3.30132 | -44.08065 | 2024-10-24 04:55:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5a11b31-a78d-39d2-9ece-7495bc3913ac | -3.30081 | -44.08412 | 2024-10-24 04:55:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 613174df-dd59-3fe6-a2ad-a6b1c6f824b5 | -4.66647 | -44.61102 | 2024-10-24 04:55:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c45a6565-063f-3609-a841-cb06f3c0f7e7 | -4.66597 | -44.61441 | 2024-10-24 04:55:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b5b933e-7322-37ba-bb04-3de6f41071fc | -4.66112 | -44.61019 | 2024-10-24 04:55:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61f85835-ed17-31d9-909d-bcf4a7a0f468 | -4.66063 | -44.61357 | 2024-10-24 04:55:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b82d8f1-a6de-32c7-a8fb-d9c5d5942f2a | -4.57076 | -44.00166 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f65ce63-846e-3260-8ca6-2546bfcd12e2 | -4.57021 | -44.00535 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a0e3bffe-6397-34e7-91f2-59a4adea2187 | -4.56912 | -44.00009 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7c78e0ad-5960-321a-8bdd-ea0ffc10914b | -4.5686 | -44.0038 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1cd88b8a-5eaf-31d8-8b08-c2e59c81e606 | -4.56807 | -44.00751 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 45d682b0-f31b-3440-ba4e-23bc14a7e172 | -4.56519 | -44.00083 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c7d673f-0941-310b-9381-7d6d3ff23fbf | -4.56464 | -44.00454 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 895ebb67-660f-35c3-97c4-7b8bb59d5aee | -4.56409 | -44.00824 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1c53a5e7-5642-3423-ac19-415084d8d5cd | -4.56303 | -44.00296 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 842f6032-2765-3543-b875-571fbfa2e30c | -4.56251 | -44.00668 | 2024-10-24 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19abc263-6eab-3d95-848f-d1bece133cfb | -4.22152 | -44.26868 | 2024-10-24 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d5b0f24-e109-3739-8072-aa8e12158ead | -4.21804 | -44.26412 | 2024-10-24 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0663cb7c-23a9-317e-8422-38d51d793abe | -4.21755 | -44.26759 | 2024-10-24 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 621e553f-af69-3bfb-bd60-e3a4452827b8 | -4.21659 | -44.26445 | 2024-10-24 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 408a7fa5-e2ab-3089-a4bf-3d2e099afd00 | -4.21607 | -44.26791 | 2024-10-24 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e3c989-34d5-3361-9171-ee97194f7455 | -6.07366 | -44.62552 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82d3eb57-c56f-353c-9c81-c494f430e1f2 | -6.07249 | -44.62609 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0c6f248-2a2a-34ca-86ad-ddb7f194e040 | -6.06866 | -44.62136 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b6628e-5df2-3115-8ab3-7a10e8bf3c28 | -6.06819 | -44.6248 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 404e1250-354e-37ea-9c6c-6b2f26b51c28 | -6.06773 | -44.62821 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 467e343e-4410-3fe2-b59c-3e77b07fc491 | -6.06752 | -44.62193 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 324228dc-d120-3130-afcd-bb962ba0cc1c | -6.06703 | -44.62536 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77816631-d3f7-36c4-98cc-278e5d777657 | -6.06654 | -44.62878 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7a9296a-efef-3c55-825a-0d3174ad149b | -6.01681 | -44.86064 | 2024-10-24 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1123af8f-6d72-35e0-9eba-3f7938e55c63 | -6.01632 | -44.86402 | 2024-10-24 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c75549c-2e10-3923-8c9e-b9a719ed8f46 | -6.01584 | -44.86739 | 2024-10-24 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df4a66df-74ea-39b8-897a-88616d898f1b | -6.00881 | -44.52296 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6064cebc-8fc0-3660-91b4-0709c5ba99a3 | -6.00834 | -44.52636 | 2024-10-24 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b175df53-7436-388f-a8cc-f15601344bf8 | -5.71912 | -43.83603 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ea4923a-627f-3b1f-9f8c-73fe1e9a905f | -5.71451 | -43.8273 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39bcfd3e-46e0-3883-8abd-789c6956926a | -5.71395 | -43.83123 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8fb054e-8a03-3c49-b286-e1e8006aa2d8 | -5.70936 | -43.82235 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56d60376-e65a-31f6-ac82-c6d2e832cda0 | -5.7088 | -43.82629 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5771229c-192f-3598-a788-87e1c3983e08 | -5.70825 | -43.83023 | 2024-10-24 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37a8c0a9-66b9-3fe4-a8d9-37a13b180878 | -5.508 | -43.70067 | 2024-10-24 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d959da-c6c5-3e45-817f-fbc72f7f2608 | -5.50745 | -43.70461 | 2024-10-24 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd56820-8f8a-3c50-8030-e8316ea74229 | -5.25999 | -43.99334 | 2024-10-24 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a32512a9-99cb-3e3e-919f-5371b025549f | -5.25945 | -43.99717 | 2024-10-24 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b382667-eeac-32ce-b653-37c1ff918ba1 | -5.6245 | -44.83349 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ce8f42-29ab-37e8-ad9a-916398cd7020 | -5.62181 | -44.8298 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63e77d0e-c6b7-3c82-8c24-4c8931517c0a | -5.62132 | -44.83318 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README74.md)
