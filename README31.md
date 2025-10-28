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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 982b72ff-bbd5-3b04-97f2-5f9ac744bab8 | -10.29816 | -47.21314 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9d4ed65-8a6a-34c9-98e8-4965ae5b4026 | -8.64111 | -44.78615 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba4ad17c-3e2c-30af-9203-8e8bedc564d7 | -9.05813 | -46.94371 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3a8fc60-3a36-33ca-9ca9-1382b23028b6 | -12.01113 | -46.76271 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7a476cf-bbfd-3f0c-a474-9dc1e061d6bc | -9.25711 | -50.02239 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 499944f4-d1c5-3485-a8f0-9a1a18cd233a | -7.89595 | -45.7035 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efee5642-e855-3733-8004-5630b3252ebe | -7.68885 | -42.17871 | 2025-10-28 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28ee2a9a-4b3f-35ce-b02c-3a56fc25d0c5 | -10.77137 | -44.76819 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c6b0661-44ef-36bb-bcd1-85700a5dc495 | -6.68499 | -46.6715 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a3704e8-e3b5-3216-ba49-6b247a03cb0a | -8.71049 | -47.97983 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbafbfd3-a8a9-37f5-af17-1512c4730b65 | -7.89784 | -45.69196 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63893dd0-5638-3969-9502-3f6b30597d29 | -9.56472 | -46.97126 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 24920090-113b-3baa-8b09-4daad24361aa | -7.918 | -45.69926 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12b2efb7-1b30-3e39-b4e1-89c63b5bcc18 | -12.20586 | -46.49935 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbdb76b7-7f1d-3661-93fe-bb7b8014988a | -10.92001 | -50.25813 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4701ccdf-0236-3191-9d51-1d4c727d3b22 | -7.53757 | -46.76043 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b03ec13-ef91-39b3-b80c-b393856296ba | -10.62185 | -49.0136 | 2025-10-28 04:14:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea20f4cf-1bb2-3a60-b206-8b4ab6d322ff | -10.52571 | -44.92065 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d42f9b06-c602-3c39-a12e-0479741f9e9e | -6.23257 | -42.53437 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5cee90f1-7495-3c58-a821-4983d50b55f2 | -10.73515 | -49.78199 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d5e234a-0e7f-3019-b9e5-2f755e143466 | -7.00413 | -46.99846 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e1d5f6-c6db-3dc1-8bbc-863b0bb0dd9e | -10.58489 | -49.79577 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 9c2b759e-585c-3c6a-92a1-68e26e293c09 | -8.63279 | -47.70884 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90daa981-56e0-3401-8000-3535b87ce87e | -7.43537 | -41.85906 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d323be4d-ccee-3616-be4e-e09d98bad01d | -7.35746 | -46.98491 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d135cb0-fbbd-3012-b5c9-2d5c743e35f2 | -9.16665 | -46.36855 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84a7aa3f-89a7-3ef6-a4a1-733c92c2d77b | -6.8811 | -43.58447 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4f4577-b37a-39d0-a9ff-bf00311da05d | -8.70979 | -44.41857 | 2025-10-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 135cab4d-ae99-3fe4-be1b-2d50755cfad4 | -7.95841 | -45.53751 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff2a504b-25b8-3582-91ef-e3661bc18ddf | -7.87223 | -46.39856 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eb4b573-94b6-33ad-ac86-88bbc74bb413 | -8.30431 | -46.17953 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ce5ef3c-f309-35e1-9dc0-f34e351b22e0 | -9.25273 | -50.02162 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f15a92bc-f1a7-33fd-9b58-761926ab3429 | -6.18337 | -42.61149 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 012b57dc-1f83-3b61-8467-dd2eb540c44d | -9.54001 | -46.94143 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a562c31-0a28-3857-8dae-93c484115c60 | -11.56561 | -44.97452 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a286e169-5b77-3366-84a9-eecb1746792f | -10.91389 | -50.25728 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02b9f424-0abc-3909-9451-240c114f052a | -6.82965 | -41.20628 | 2025-10-28 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| daf35de0-8b55-34b3-b9dc-3da4cb989245 | -7.07482 | -44.93668 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47dfaae6-1fb1-398a-805a-6be6058de71a | -10.72778 | -48.13065 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d29492e-cdaf-3506-8ea3-b02814b447a0 | -7.31303 | -44.10404 | 2025-10-28 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 638a30c8-dcbd-38f3-8b8a-cdd5f16518a1 | -5.48384 | -47.75011 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 194cc63f-5e47-3a09-a234-37e5d6160b27 | -7.82616 | -46.46394 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5893cb35-dba9-380f-ae0d-8ffe4d7b742f | -8.31752 | -46.16503 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47f1c109-5a1e-3a38-86a4-29be21bf3b0f | -7.92269 | -45.69228 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8339c3c4-0d40-3c92-8c11-201f464d61ae | -9.76101 | -41.88017 | 2025-10-28 04:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89619ffa-80ac-3f05-9a31-196655dffe3c | -11.04451 | -50.34479 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57701512-0337-3496-9292-86862e088eff | -6.12815 | -42.70108 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24795903-990d-3787-b870-ac76175f9663 | -7.97951 | -46.72145 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2bf0f15-85ee-324b-85cd-93e97cefd4ba | -9.6111 | -47.78666 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0112d60-69ed-39e1-9e93-eeeffe82ebab | -9.9586 | -47.08936 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57147585-42ee-3f54-a1dc-faafca6d6d00 | -8.09971 | -45.68136 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab981493-4cd8-3087-98cd-3e7cfaa0a3ab | -6.21489 | -41.52943 | 2025-10-28 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f84a0a95-1b91-345d-9045-982f5f3a1e0f | -10.56731 | -49.79675 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 206d3ce2-b7f5-3e0e-8698-a3999d64109d | -9.22546 | -46.36549 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cb13ccbf-081c-3954-b522-54f63489d8eb | -6.1336 | -42.68781 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6d04ee24-351a-39dd-a7b3-2373eb63941b | -12.00657 | -46.79031 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b8b3a9f-ba48-3962-ba8e-bc1d85925c41 | -10.91213 | -50.25239 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c926a20-72eb-3bd4-9e70-2f11b1211802 | -10.38227 | -44.66824 | 2025-10-28 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364cb282-45cb-3717-bc63-e4fa00e65aa6 | -5.78841 | -47.71877 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e5a41f2-6103-37c2-84bc-90defe03d1a1 | -6.2809 | -44.71364 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa15442-a946-36ad-9d0e-fc4f67f1fad7 | -8.07607 | -45.95598 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a16ed166-2893-3a8a-a64f-218b1ae7c14d | -12.70007 | -46.31572 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c02db1b9-0e1c-314c-acd2-2fee0a4286df | -11.35526 | -46.0891 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e4a0e12-f338-3e3d-81fb-0b606e8fbe34 | -9.17124 | -44.57695 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d475cf08-a226-3e64-95d3-46cc433758a2 | -7.00194 | -46.99612 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d45a7cdb-91e6-3ed4-ba72-33ecc3e6a2b2 | -8.56504 | -47.01862 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d7d2c8-b051-3f27-9cbd-9c8b676bd5cb | -10.6624 | -48.49682 | 2025-10-28 04:14:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16d24c31-a3fe-3809-b76d-13c99ef13e1c | -10.87371 | -48.62955 | 2025-10-28 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2433a58-60a0-3615-a20c-87f874e1b3e5 | -7.96109 | -47.23655 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 060487c5-1afb-3dbc-a9b9-4a3bb723b6ba | -7.98033 | -46.7392 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35145c16-8a87-3dae-94ee-e214f942f46d | -8.24484 | -42.36663 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4abd1aa9-e41f-3ae3-a5e7-9d4b7d3762a2 | -11.14262 | -44.93786 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ebd1eca-1b38-3040-a420-2253b258be21 | -12.32461 | -47.45488 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2242bf-9d0d-3117-8c35-6010e1f11930 | -11.30153 | -44.88013 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef706f1c-5817-3b3a-afe7-5b511a24bf3e | -7.67877 | -43.90094 | 2025-10-28 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5237bd4f-7155-3cfa-bef6-8676bbcb621e | -7.94328 | -45.50002 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98cd4e22-a866-38da-b280-8651e0f91532 | -9.22127 | -46.36897 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce531db8-70cf-340f-9dd8-9ce7a3cff4cb | -10.58348 | -49.80371 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bebac43f-8e95-36bc-be5d-6a15550574b5 | -12.63161 | -45.0774 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8df63808-38b1-343a-9b19-3cf903cc3d41 | -10.56518 | -49.80866 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7dbe77f9-2c97-32c2-8847-a79c63dd19ed | -6.92045 | -41.87113 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f886df2-8e2e-37d7-89ff-fc0ed7ae3c2b | -5.20621 | -50.57854 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a61998-05a6-38d8-a6a4-b72db05e605c | -12.23998 | -46.52497 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39c63a67-5223-3d8f-b120-e441db42754c | -8.16371 | -46.99381 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb6ae3b8-22a6-3c35-9bf3-bf8b962defbb | -9.01486 | -43.97314 | 2025-10-28 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 410a29aa-6fb3-3d43-a855-a7cad23d0243 | -7.92332 | -45.68842 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcb72e58-ce04-3535-8624-e28972895fdc | -6.65079 | -44.60411 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 703b9aa6-aeb8-3a2c-8ffe-01d84668b5b4 | -7.24356 | -39.29062 | 2025-10-28 04:14:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5aab8c71-54ab-3f41-9015-a9b9e67212b6 | -6.98018 | -39.10369 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a1630223-96eb-37bd-8793-db5754ee9868 | -9.91983 | -47.68311 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc7d8c56-9ca8-3def-a5ea-23fbf27dc96a | -7.32708 | -47.21293 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5993bc7-ec1d-3c8b-bf82-b7dbbb338de5 | -7.9653 | -45.53862 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15b3353c-0419-3be8-bdb0-3feebd099e0c | -6.68939 | -42.04596 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 773abc20-235d-3b49-83bb-295952092a00 | -10.3183 | -48.78607 | 2025-10-28 04:14:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be1727a1-7d8a-3fdf-8538-df226cf1fd5b | -7.48471 | -44.35168 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84192266-9394-3788-9449-3e581666b3da | -7.97962 | -46.74352 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 370fe4d7-30f5-360e-8be0-a0c4db8d8e7a | -10.36364 | -47.14038 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b7e3929-3dd8-3d6c-9b65-ebd4cf7e7bbd | -10.87342 | -50.10834 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8d9a586-333c-35a6-89ee-618a1cabfc47 | -11.28478 | -45.51213 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b989f96e-7f55-388b-8c71-29af727edf0d | -7.46787 | -47.1598 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README32.md)
