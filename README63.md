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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef3c0991-2170-3c85-a612-59539574e7b3 | -16.4624 | -45.2402 | 2025-09-05 12:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2ee39717-33f6-3dec-b58a-2a8d4b2da3f3 | -12.9668 | -54.791 | 2025-09-05 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 636f2161-9a37-3a9d-9df0-40be6dace285 | -15.7179 | -53.6165 | 2025-09-05 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 7460a002-8693-3523-8430-b2acf8dca0da | -13.0044 | -54.8282 | 2025-09-05 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 519bda40-a85c-3c22-98b8-bab187d8f6e9 | -3.9826 | -47.88186 | 2025-09-05 12:53:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 303662c4-12a8-3737-a3ce-601995314013 | -5.53197 | -57.24802 | 2025-09-05 12:53:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f41ec624-fcad-3c71-bc97-b4382af12537 | -5.99355 | -47.62412 | 2025-09-05 12:53:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 6610a106-c371-3f79-93f6-7e1054ed152d | -6.27175 | -53.43685 | 2025-09-05 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 922951c7-1f6c-3bae-95fe-ade120cd98ee | -6.09945 | -45.31647 | 2025-09-05 12:53:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 88d2d576-826d-35ba-86d7-36d9cde9937b | -5.98946 | -47.64572 | 2025-09-05 12:53:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d99ee98a-0b78-3032-91c3-8a4f70e8daa5 | -5.54111 | -57.24928 | 2025-09-05 12:53:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 34e9017d-a7e6-3682-a663-4e66e5951f55 | -5.54249 | -57.23978 | 2025-09-05 12:53:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3975ba9-94d8-3118-899e-73b323767ecf | -6.011 | -46.68163 | 2025-09-05 12:53:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 10e5b354-d508-3803-804d-bd702bf90553 | -6.22579 | -52.59979 | 2025-09-05 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c08b61c5-c73f-35c1-9b24-ed1dea097847 | -6.22439 | -52.60553 | 2025-09-05 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1d84e44d-cdf3-3bd2-8127-3d02f400c550 | -1.89486 | -55.23618 | 2025-09-05 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1c860739-64bb-3d10-875a-e39771d0fa76 | -5.53336 | -57.23853 | 2025-09-05 12:53:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c23d7adf-de6a-34fb-a00b-4920be44f242 | -6.02013 | -46.68983 | 2025-09-05 12:53:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 0340e78e-76ef-340d-873f-aa3c66744f15 | -6.19029 | -51.48211 | 2025-09-05 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8e4474be-f554-3458-ab0f-eb4707c1da4a | -5.9901 | -47.65134 | 2025-09-05 12:53:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 5b621bdf-29a5-3c4c-8a6a-02c8c328ee2c | -6.18561 | -51.48941 | 2025-09-05 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 256c8683-ba7a-32fb-a4ad-8a35bc7f330a | -6.79861 | -45.66008 | 2025-09-05 12:53:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 178d127f-0780-3128-8d8e-ae9a77bfe6b2 | -6.27031 | -53.44711 | 2025-09-05 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b17c1a6-48e6-3c2a-a0fe-91a5abdb155f | -10.41961 | -50.27017 | 2025-09-05 12:55:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c7214ffc-4375-3cd8-ba42-a313be8756af | -9.8074 | -48.29498 | 2025-09-05 12:55:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 041c8aed-8230-3395-bf4d-4001d5cf13e6 | -8.34299 | -47.48516 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 398b9d82-e719-3279-bb51-6abc9b706d8e | -9.04872 | -50.06348 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 296.3 |
| 4e3e81a2-8680-3891-a43b-461cf85d9e37 | -9.03836 | -50.04902 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 686a0191-38f9-37ac-8a34-248cfc6cdb51 | -10.31315 | -46.34111 | 2025-09-05 12:55:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b6ce59d6-06c7-3ea7-ab68-56d69051ba1c | -9.76754 | -46.90608 | 2025-09-05 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 99ec363f-87b5-3614-9fb5-c58259403f97 | -5.85978 | -57.76963 | 2025-09-05 12:55:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| da26fd55-0bdb-3580-8f12-57a6a805d3b4 | -5.9043 | -57.72592 | 2025-09-05 12:55:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8f4c6c9c-cc82-3385-b539-6d788f50113e | -8.35287 | -48.2969 | 2025-09-05 12:55:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 06f81435-4ed8-3bcd-9126-adbd05f3b948 | -8.42836 | -47.55634 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 6f68be2b-bdac-36ca-9ec0-0e7e9990df12 | -8.57084 | -54.70941 | 2025-09-05 12:55:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 245ba18d-3ff5-3b6d-9a0e-8b05be7a7a92 | -8.8748 | -47.22664 | 2025-09-05 12:55:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 18dbaaf6-7c16-328a-9992-0997a84ad82c | -9.69259 | -48.98653 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9bbee1f5-548f-3cca-8335-7323e10588f1 | -10.16433 | -46.23751 | 2025-09-05 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| bf7aa68f-2c29-30fe-ad7d-a1fc19552fce | -7.16419 | -52.83363 | 2025-09-05 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| aa337974-fa59-30c5-93e4-b7d82d7cac5c | -5.85271 | -57.77267 | 2025-09-05 12:55:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 526975f1-e7ea-3f5e-aaa2-a63793bb6c23 | -10.31524 | -46.34637 | 2025-09-05 12:55:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 97e9f08b-1094-37c7-92a5-d66342ac8679 | -9.07124 | -50.4248 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 316ea557-60e1-3562-b443-3db9f2d3398e | -9.2176 | -57.09001 | 2025-09-05 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 46432764-29a5-3f58-a50c-c3a84f12ebb6 | -9.70664 | -48.98809 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 04bead1d-dfa9-309b-9b35-e262a95fc626 | -9.06836 | -50.41859 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 0813dde6-9a25-389f-96d7-3bfce04bda76 | -9.07155 | -47.02208 | 2025-09-05 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9a310cb9-9ece-3eee-a837-bdefe176eaa1 | -9.25577 | -57.07712 | 2025-09-05 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e128b657-9695-39a7-8f00-3dbf83712203 | -9.33928 | -55.20642 | 2025-09-05 12:55:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2397c84c-be65-3d29-aad4-7778c25e1405 | -8.35112 | -48.29005 | 2025-09-05 12:55:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5c567635-fdf0-3a5a-b5d4-184fcc73c22d | -5.41314 | -60.16468 | 2025-09-05 12:55:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fa880b01-274d-30c2-986f-9b846aa8ae63 | -9.17303 | -46.04897 | 2025-09-05 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 301.9 |
| c5bf12cd-8366-3e72-96dd-bdc374341f14 | -9.0511 | -50.05056 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 185.4 |
| 4fe42bbd-c956-31e8-929f-154eda842121 | -9.69717 | -48.99387 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6019b475-dbd6-346a-9ce2-3df48cdf6f9c | -9.07578 | -46.98792 | 2025-09-05 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 8b83f658-c9a3-372a-8151-42c46e129454 | -8.9145 | -45.79351 | 2025-09-05 12:55:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3229db85-a977-3eb1-ba98-40027ae412e4 | -8.42832 | -47.53168 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e8c3f26a-97b3-3d3a-a5aa-d03463f416b8 | -8.33147 | -47.47855 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| e1d9b53b-3506-3ae0-a16e-fdfbd1cd037c | -8.42473 | -47.56238 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7853a30c-3d46-3081-8361-cfa7d8494f15 | -9.98705 | -51.62658 | 2025-09-05 12:55:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7e731440-ab65-3315-8848-8e55aa4c7891 | -9.05128 | -50.04391 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5ff206d4-09e8-33d7-9131-a7f48756d8fc | -8.31254 | -49.08527 | 2025-09-05 12:55:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 20117f50-ff5e-3a18-928b-0c739b92d86c | -9.3036 | -56.80966 | 2025-09-05 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca802833-ffa2-342c-92f1-3e38674ea3d8 | -9.17784 | -46.00873 | 2025-09-05 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d1cb0ad7-af74-35b0-a2aa-188705938580 | -9.17416 | -46.05622 | 2025-09-05 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 176.3 |
| b363d189-8a98-3264-8d02-efe79b29b25e | -5.86907 | -57.77116 | 2025-09-05 12:55:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f8615052-d6eb-3b70-8c3c-b3582967d39c | -9.08326 | -46.99417 | 2025-09-05 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 77dca09a-255b-38b5-99b9-a49274b68147 | -9.17872 | -46.0159 | 2025-09-05 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 59af6e24-72cd-3bd7-b90a-ae2bc9314d3b | -8.91471 | -45.79868 | 2025-09-05 12:55:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2d804823-3e69-3fac-b6ef-a920306d8c8b | -9.70966 | -48.96371 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| a7781db6-670e-334e-9a3d-fb8ae497a6a5 | -6.62586 | -53.3303 | 2025-09-05 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0eb7727e-02a4-309a-ba9f-91ff0e56b21d | -10.25105 | -48.51543 | 2025-09-05 12:55:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6d301a47-6b35-37b6-8a75-b5b201880287 | -9.69998 | -48.96959 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 005a0232-defd-35ca-93ba-58145d18bda5 | -5.87054 | -57.76128 | 2025-09-05 12:55:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 53c2cbd1-141d-3cef-9235-12986fe2667b | -9.26407 | -56.89523 | 2025-09-05 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f432f1b0-63ff-388a-8f65-d4f74b3270b9 | -7.62297 | -47.93486 | 2025-09-05 12:55:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| fc5d90ba-655e-3b0c-a640-f3d9b6d5937d | -9.71479 | -51.0807 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 5fa53a9c-6d31-33ff-85af-2c6d2b3ed94a | -9.71121 | -48.99545 | 2025-09-05 12:55:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c9f3f8a9-501f-302f-a3f3-13e5189712ff | -8.3275 | -47.48345 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| cbd09fe8-2eea-3227-b8cf-421dbe59f5f4 | -9.0487 | -50.07013 | 2025-09-05 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 0b1e9443-bd0f-3b43-9fc1-de35132ec0a7 | -7.16575 | -52.82222 | 2025-09-05 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b93bbe87-4f6a-3478-81d0-d55bfa817efa | -8.43215 | -47.52589 | 2025-09-05 12:55:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 89b6d9df-fb8e-3126-819f-b86830a67918 | -7.8004 | -52.12907 | 2025-09-05 12:55:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 37d70911-b0ac-3809-842c-9e67f4ee5b2a | -10.96579 | -56.21341 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4f4de48c-be0a-3a8e-8ad5-162cd22cacdf | -13.87525 | -47.98819 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 638787bd-57d7-3b01-bb5d-0cb39b699c64 | -15.75127 | -53.68389 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 93998721-7e9e-3ace-bef8-e451525082b5 | -11.59839 | -52.1859 | 2025-09-05 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4c968ace-df36-300d-a54d-f68833f9c0c7 | -13.00588 | -54.83081 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5b69483a-c940-3e60-b1dc-48368cdb4f42 | -15.76358 | -53.6716 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 1d5c7dac-5bf7-30b4-bed1-c6f99f9b8cb5 | -11.6516 | -54.53721 | 2025-09-05 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5c9f74e9-5a16-3bc1-862c-5d454cdaabe2 | -11.65303 | -54.52676 | 2025-09-05 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| efc11826-f71d-34c3-b8f4-5aaf30c80a6b | -13.33532 | -51.73119 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6b1c3719-419c-3dd1-a801-49bb9fd7c4d4 | -12.24469 | -50.14899 | 2025-09-05 12:57:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6b725985-27da-3fcd-989d-ed91a17ba29d | -13.66883 | -47.92174 | 2025-09-05 12:57:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f53bed96-abc7-391d-9fea-38c409b1cc05 | -15.06358 | -50.09904 | 2025-09-05 12:57:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 1729a3c8-e194-313a-afc0-076e4b31ad90 | -15.76525 | -53.65803 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 485d6f28-86f5-3f67-a22b-ef8d28a3d353 | -14.06351 | -53.98659 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8ba171dc-6d6d-3b19-a1b7-b716a66e1644 | -15.75959 | -53.61611 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7ac51da1-ccbe-3d4e-b6ad-d3a65c75387d | -11.86593 | -50.7034 | 2025-09-05 12:57:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1319b03b-7704-3b3f-a587-46384b5f12dd | -12.53632 | -53.81189 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cbe2e585-bc57-3fd9-87f4-ba533db16582 | -13.88689 | -47.95993 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 128.3 |


[Clique aqui para ver as próximas entradas](README64.md)
