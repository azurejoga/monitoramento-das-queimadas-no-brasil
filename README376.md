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

## Dados Diários - Página 376

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa8e774-3352-3915-ba4f-790cd5ff044e | -4.31786 | -41.23184 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| b5ce604b-b558-3fb9-a3bf-77d893f024bf | -3.01328 | -54.75105 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1eb980ba-0450-382d-ae39-fdc447ea5000 | -4.93883 | -55.81195 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3f4e4c5d-5dda-3db5-9f1d-6328d7e344c4 | -3.17504 | -54.6058 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0223f8a7-1a3d-33ba-a8d0-d68f02523e13 | -0.75043 | -49.39669 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c9779ae8-98e3-3499-8279-b85a5089bea2 | -4.33792 | -43.15804 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e9ae04e2-936d-38a9-886d-0c138dc48100 | -3.36759 | -41.36244 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 39.1 |
| e0f34a91-d1d7-3eec-92dd-09aa16bd769b | -3.74642 | -44.70557 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d1a8d38-4e87-3444-87ba-1622e5881ca4 | -3.30353 | -54.05756 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2a42d63b-8e85-3800-a41b-a36b675e9385 | -4.62613 | -42.7551 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f16e72de-fb75-3cde-ab85-5721d2775f77 | -3.8362 | -55.98148 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9ad43760-d8bd-390e-9b7b-798b390401f9 | -6.44352 | -52.70097 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 29ad4a8b-7309-3e9e-a93d-72f64af62f5d | -5.21346 | -46.0154 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| d6965aab-7f78-3205-abcc-b360c101144f | -5.3805 | -44.19615 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ced5a3eb-34f0-3d54-af3d-0c676e3c4dea | -6.20201 | -52.84355 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f08e5825-40f8-39b1-a937-b9740ddab59e | -3.20755 | -57.87249 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2ec1f35c-ad42-385d-870a-bf045766c27d | -3.05478 | -57.47371 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cee42dc5-b55e-35dd-a512-4fceef675a3d | -2.8306 | -54.13174 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 20bfa06d-4105-3582-ba64-8bf0e53ee28d | 0.51608 | -51.66937 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bd69d88-8c90-3b2b-910e-a478f9e0728a | -3.69776 | -58.82052 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d98b8ead-5ef1-3da3-920c-859aee8b6adc | -3.47745 | -44.39211 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 69688744-fb9e-3015-afe9-3b56e95ce2a3 | -3.85956 | -51.93869 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a14a531-67b0-384a-9139-13eb6debefdd | -5.49881 | -42.85434 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 82563bfc-819c-36db-ba5c-47c20b298dfe | -2.74305 | -57.61334 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 32d233c4-4173-3a42-a2bf-07e31b730799 | -4.7673 | -43.74769 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03533df2-9eb7-3500-9ab2-01baaeb3f819 | -7.23234 | -55.10031 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 57f815e0-c313-3b69-a3bf-7e6b895e90b5 | -4.28528 | -43.65172 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1105a583-4328-39d9-be70-2022175722c8 | -5.97431 | -53.59461 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b8b7218b-df93-3635-ab43-0fc998afc3bf | -6.83236 | -55.27324 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8418db2b-cacc-35d5-ac58-f38ab7e7123c | -5.57153 | -45.65008 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 11b8290e-8917-3eb7-a014-4f38cbc16662 | -6.7481 | -55.06189 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20d9a6b1-4bd4-3925-8cb8-fced4d2f1cbb | -3.08804 | -53.96026 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 131a18e4-9b62-36d2-8a1c-1e583dfc4300 | -2.52231 | -56.61576 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c014c64a-8475-3341-954e-bbdd54a88821 | -2.92762 | -54.12473 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3ebe597a-6df9-34a1-8aa0-29b34af64d83 | -5.82102 | -53.85909 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| abfd83f4-ab0a-3d85-9615-52f8ca470ea5 | -3.2319 | -54.29827 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d2ecb41a-f94a-3a8d-b225-9ec64ada0054 | -2.69346 | -49.04827 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de429e46-bfdc-320c-b98a-d369f31922e3 | -6.22095 | -53.27005 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c37faba1-bda3-3724-9b8b-34460a723459 | -6.78291 | -56.23883 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| a9d8aa8f-467e-3508-93b3-18519de9a509 | -3.70631 | -58.93686 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 31a52d0b-639e-31f2-8564-a1be5e6aadbc | -1.82472 | -55.09206 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b522abc9-acde-3c6b-9d86-40b069174443 | -3.54854 | -54.66964 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d66c7b7c-5ce5-3ca4-9d71-d2f171360dab | -2.75614 | -54.09375 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3a907fd2-3642-35ba-82e6-715d4401374b | -6.15792 | -47.93501 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 92c771c7-3c7c-374d-aa92-21d190e8e945 | -3.46284 | -59.46754 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d646af06-c681-3259-8fa2-7844d0c7f135 | -2.76786 | -54.10752 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3e7f2ec7-6333-3592-9701-46eee8635889 | -1.26375 | -54.68506 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c058ec8f-dcd0-366b-bbaa-6afedb02516e | -3.45575 | -58.07088 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 12db8420-9c94-35f2-92ec-8ec9b4b9db97 | -2.09512 | -46.57676 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9227570a-d183-340f-b0a4-36e71711149c | -3.46912 | -39.51178 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| c46e7ece-bf4c-3869-bfa6-88fa6c9501dc | -3.13642 | -40.07725 | 2026-10-08 16:39:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df41dc13-87f8-3e56-823d-a078f33b7b2c | -2.90321 | -59.20385 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffc82e08-3343-3ee2-8d55-f5060d9d73d1 | -6.45675 | -53.69203 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1c8729d5-fd8d-3dd9-9922-79cff3dbd354 | -2.99667 | -53.89294 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| a04fc948-4e52-3860-9ab7-0c284dd30fe4 | -6.15449 | -47.9355 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 56af8f8c-f3aa-3043-bbdc-5970d3212561 | -4.31194 | -50.78182 | 2026-10-08 16:39:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| edafc6f4-dae2-3b2e-bc32-a4607e99e3b7 | -1.47903 | -54.55525 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 865ff860-5ccc-3ba3-bb82-6452f902300b | -3.1821 | -58.64888 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b380ce1a-c27f-38e0-9520-66a0f09fcb02 | -6.44637 | -55.04372 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 70e74020-8181-37c8-a994-a9c72dc23050 | -2.81573 | -49.11536 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bf2731c4-ce02-33bd-a1d7-08b28fb43690 | -1.64279 | -55.27724 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a55193f-835b-36af-8be2-0d9b3d469190 | -3.02295 | -54.04116 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4bdc24fa-3574-3d27-81c5-cdb56e07d84b | -6.46042 | -52.64798 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e7952d22-3fa2-37e4-b054-71f97295270c | -6.32535 | -46.54396 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25e5a2ae-e583-3de3-9ac6-ba86a6c1826c | -2.50556 | -56.16492 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 83292d2f-85d5-3bf1-9e48-169b600a4fa1 | -2.22713 | -58.10665 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ae851bf0-4bf9-3962-9a48-a7fe90ef3727 | -6.22096 | -52.87898 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e2a856fe-e3d1-3d56-a456-a6ecf8bf4408 | -2.90917 | -58.56166 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 143941a8-e019-3612-9285-b28f9ff41c31 | -3.57309 | -51.99274 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0639ce8-74e9-323f-8542-01664afbd1fd | -5.27913 | -55.95173 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c5f1a97f-b70c-3640-8d5a-aa8aee5d62f9 | -3.93967 | -55.71621 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f5b55f72-20c4-316e-8eac-fccc586c2568 | -5.17629 | -42.68308 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 105e7bb7-0cb3-32f2-adce-4ce0bd70f851 | -7.20469 | -55.19514 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 21ff465f-7d0e-3f24-b1bb-2541e2278ee3 | -2.78696 | -57.62056 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a26045ba-7b08-3197-a6ed-d28af7517652 | -3.45086 | -59.54374 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| df1d71a1-e9d1-3665-8a39-b5754ff28e91 | -3.21029 | -53.86504 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a2e7d8c4-d028-31db-bb38-8ccc1f1cdfc0 | -3.30468 | -43.06495 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f8d4599c-f66c-3f88-af57-f7783de654d1 | -6.22087 | -52.77948 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9875733c-c8f7-3130-a7c9-946b533235c7 | -3.1089 | -57.66201 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c1820605-800f-36c2-8e13-a00a4a664e44 | -3.48473 | -59.37789 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| aa918119-283c-3bd7-8130-79c9a130d187 | -3.01089 | -54.06601 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 1d1d0142-fb05-33f5-bcf8-7eae7ddaa00c | -3.35725 | -59.42068 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7441eada-a89f-3119-b254-d12db0e6a63c | -4.36723 | -40.41992 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 029abc57-3769-3fdd-9401-0c25aa62865e | -6.73647 | -55.13764 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 3698b738-eb01-3c54-8c9f-09038d0dbf0b | -2.99997 | -54.76429 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4a1b14de-c42f-31f5-99b6-959aec64deb4 | -4.35537 | -43.79889 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7afa4564-1f58-3580-896b-4ee3a14e1d14 | -3.46448 | -39.51247 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| b3103936-0048-350a-98df-296a493d52b1 | -3.02981 | -42.92762 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6e154a44-51b3-359d-837a-ef453ba59ff3 | -3.77254 | -52.62455 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 361af2ec-fa1d-38e5-b70c-cf8ad28f2951 | -3.11783 | -53.78864 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c673ba6a-3a91-3594-9163-7499cb930ec2 | -2.55127 | -58.05252 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| cb98e16a-729f-3313-990e-31cf4ddc31d2 | -2.07023 | -46.59108 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2798572f-88ff-3dee-b325-5516804f2ded | -3.05531 | -54.03146 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ed767331-09e0-3093-abde-7a0e1a75006b | -5.70364 | -53.47846 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 9eb8dd10-c72b-38ea-b387-60c23abae8a0 | -3.36949 | -46.36499 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e7e76848-4e8e-363f-833b-9ffd6739de3f | -4.09644 | -44.11338 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 881f87ee-73e4-30fc-9931-136f965a88cb | -0.40386 | -51.72024 | 2026-10-08 16:39:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0ffb1c66-0e49-3650-b8ac-7c3f1c7da92f | -3.10109 | -54.27555 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4a324266-a65c-35a3-9be2-0c66f8fc5986 | -3.01587 | -54.73394 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f59be7bb-2936-3b98-82ff-370cf146d68e | -7.5152 | -55.57584 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README377.md)
