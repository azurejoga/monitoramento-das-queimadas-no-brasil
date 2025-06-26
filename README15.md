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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5182b87-c538-37d2-b9a2-8c5413c63a48 | -9.75082 | -48.66687 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd649db9-2d3b-3578-ae62-2e8332eae22a | -7.09328 | -49.16348 | 2025-06-26 05:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f122ab-bef0-33c8-8344-bf4ef8291b59 | -10.2722 | -47.61073 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db90049a-27be-3654-b98b-7b083985d1c5 | -9.07166 | -46.91184 | 2025-06-26 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f10b90e6-f1d1-3fdb-a1ea-8542f5a5980d | -8.25696 | -47.02254 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e6589d-e382-3da6-909c-1bc69d87c92b | -9.49744 | -56.09486 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f65f88fa-26a4-3bd8-8f24-f1945fea7077 | -9.12221 | -49.44291 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0570531f-8226-399a-be79-0773e28b27ea | -8.44445 | -49.63179 | 2025-06-26 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00a975d5-f877-32af-8268-95db3f6677d1 | -9.8762 | -48.44844 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0bdbcd4-8c50-37c2-ac98-866da6ce5c5c | -9.51533 | -56.10462 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e2337478-bc83-38fb-9cc1-6de3034499ae | -9.49689 | -56.09837 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 989e6dbe-d38d-383f-8a92-46590030edd9 | -10.06994 | -49.65751 | 2025-06-26 05:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ab79487-4742-3a8b-9b68-f02acef853dd | -9.11824 | -49.43746 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 70d4bf06-a39d-340a-a76d-e00ed13ca7da | -7.36154 | -46.23032 | 2025-06-26 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ec040cd-e089-3665-a18a-0da67a6f4a8e | -9.51811 | -56.10866 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e693abef-3d5b-3309-ab68-59527076a5cf | -10.6203 | -48.08108 | 2025-06-26 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2fca62-beea-3162-a73a-634c33bf1751 | -8.85874 | -50.1563 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d26508-ec85-3c51-94a4-80b06c5f7c73 | -9.88322 | -48.05374 | 2025-06-26 05:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448850f5-9f51-37d3-9ce6-3baaae93fda9 | -9.50965 | -56.10399 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 657694d8-40dc-3a89-b887-3a9d80dc325d | -11.06906 | -46.64466 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c13b89c5-c46a-37ce-8b5d-3cab22891014 | -10.27752 | -47.61142 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a53a3ee3-042e-3429-bb25-cf5e0df32659 | -7.36102 | -46.2341 | 2025-06-26 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1e3f62-3b2e-36b5-a175-8c2c9f68bd15 | -8.97453 | -49.86929 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea45ab4-3e71-3fa6-8396-38bbfef8e158 | -9.11759 | -49.44223 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 42b910f1-3bb3-31d7-b618-232f74e8f972 | -9.36158 | -57.44025 | 2025-06-26 05:06:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38ea0241-f49c-3408-ad56-2e051dcf11df | -9.51242 | -56.10803 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 13b99093-bbdb-3261-81e6-95ed87c0e26c | -8.67294 | -49.95425 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d7c8fe-4ffe-36a4-9d72-f45d6933860c | -8.97006 | -49.86865 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9371ebc5-19bc-36ab-90a9-118acb26a116 | -7.31536 | -45.7515 | 2025-06-26 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f06ea81-e321-3405-91ff-6941a1d2ec7a | -9.11363 | -49.43673 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bb3d077b-5f92-3c8a-9e3e-577bf2960275 | -7.19914 | -43.10091 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 233c675b-12eb-32d6-a78e-152132f963f4 | -7.20624 | -43.08681 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e817d0c5-1eff-3aab-80fd-ba252a3be38c | -9.50076 | -56.09539 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 143dad97-657f-39e7-b89a-e9df3eb23a81 | -10.23217 | -47.45724 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5b19593-6b8e-39d1-90c5-9b57207f87c8 | -5.20437 | -56.04525 | 2025-06-26 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8def2e1f-3a8e-3955-901c-eb35e7ff23bf | -7.75197 | -47.61648 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feb40999-fa8c-3b39-863b-42274f66d261 | -7.931 | -61.55547 | 2025-06-26 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f336ca2a-90d0-3472-be3b-2fe3e309a183 | -5.49103 | -42.1535 | 2025-06-26 05:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1404f79c-ede5-32f3-9baa-d41ad36d75b1 | -11.07632 | -46.63355 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8637a0eb-0318-3537-bfbb-3916e470ff17 | -9.51352 | -56.10102 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1b67cd-668c-3972-b76b-7712b856591c | -9.87164 | -52.44031 | 2025-06-26 05:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f01346-d1e4-3058-bf4d-834807443d0a | -9.11298 | -49.44155 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f803f469-a5a0-337a-a6d6-eae550046adc | -7.09387 | -49.1618 | 2025-06-26 05:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dccfe320-37a0-3d68-b1fe-407c0fc4640d | -11.06283 | -46.64775 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a49622e-0588-3d02-9998-34c74ffa2202 | -8.37447 | -51.0735 | 2025-06-26 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c179ef72-b025-3ed3-bb46-c9d88fd10a2f | -11.07581 | -46.63749 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10f8f097-c354-368c-86ce-5faf00c1a4b2 | -6.18069 | -48.08002 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c8f7e3f3-9fd2-3c3a-b047-98dfd4589bff | -6.18238 | -48.08629 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcdb2574-027b-38b2-8bd6-9ffb63bee1cd | -7.20751 | -43.08976 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 418396f2-0731-3494-9dff-002b4491f130 | -10.50947 | -47.20793 | 2025-06-26 05:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90893fd1-7421-3b55-b1e6-a268b1cef1f8 | -8.11817 | -55.07215 | 2025-06-26 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9fbed45-5f8f-314d-81d3-77999fb51341 | -8.06246 | -46.96771 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a925f3dd-0de8-3512-8687-11fa414849c7 | -11.06958 | -46.64062 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7dd3833-51e3-39cb-bfcd-76679a12441f | -4.13051 | -54.89763 | 2025-06-26 05:06:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa215fd0-f482-366e-8e60-b401787d0ed9 | -9.29036 | -56.24494 | 2025-06-26 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 832cfeeb-182c-341f-90b8-863ac72bafe3 | -6.37592 | -43.75605 | 2025-06-26 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 152cc42f-9194-3946-92d9-9fdb22e7a4b6 | -9.07759 | -46.90931 | 2025-06-26 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b86ee16c-f4e9-3396-bb93-2e2104c49378 | -10.41643 | -47.50739 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeced18b-9328-3c41-bb7f-2d27f7ca81ab | -9.50354 | -56.09943 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c70283-cef5-3bca-9b4a-b30ce4bda2fd | -6.1831 | -48.08111 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1d62342c-3022-30f1-897a-f7b95e8d156f | -7.19992 | -43.09486 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a4f1cac8-e0cb-3025-a178-8fad1453839c | -7.2007 | -43.0888 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0d2330a0-b1c4-3843-a81c-d137064d0c56 | -7.74739 | -47.60016 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a75c52e1-dd2b-3f53-b959-2c67b6978d3a | -8.678 | -49.95049 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7dd2760-50e0-3905-b620-1df664198f53 | -6.17507 | -48.0845 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80ea6db1-8fd4-3f32-92b1-26621a96ba8d | -9.2441 | -50.05029 | 2025-06-26 05:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84856d8a-5eb0-3bc3-bb2d-ade7a9353dd9 | -8.47274 | -48.26315 | 2025-06-26 05:06:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9708f951-49a2-312d-b24c-8962b9d6a4a9 | -10.62547 | -48.0818 | 2025-06-26 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 114ce8bf-08b2-3e2c-b5ac-8485d6028a36 | -10.61989 | -48.08419 | 2025-06-26 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68a7c2b8-a4f8-3e57-9a4a-7a6e5ed5da38 | -6.18382 | -48.07598 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| df0691f0-1138-30a1-9a28-fd156762ffc6 | -8.48265 | -48.26464 | 2025-06-26 05:06:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22ec819c-43aa-319a-ad1e-716ef346ed04 | -7.11139 | -47.84413 | 2025-06-26 05:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d735b49-93ce-34de-b3d7-b7640a02fc7c | -7.10646 | -47.84283 | 2025-06-26 05:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 720b7379-440a-3622-b331-c12645430406 | -9.85137 | -44.7032 | 2025-06-26 05:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70b62fa7-d1cf-3259-9316-160497031fbb | -5.83777 | -48.39412 | 2025-06-26 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aac5fcc-1ab9-3537-a066-2e275e121d87 | -8.71595 | -47.85772 | 2025-06-26 05:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9e27351-1768-342c-88b3-4ba3e8de24ed | -10.5099 | -47.20449 | 2025-06-26 05:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 964bbe2c-7928-3e33-9703-da62533ce45a | -9.32767 | -47.82968 | 2025-06-26 05:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 712543f1-ff79-3b1f-8bbd-3e22f15ef4df | -7.74414 | -47.59678 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4091c1a5-942f-3612-bd06-6d3981743482 | -9.12156 | -49.44767 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 02ea8a6e-2660-35a9-a4f4-d60d200dcbc3 | -8.33203 | -49.23589 | 2025-06-26 05:06:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43abc030-4d7b-36d6-b7b7-76fd16e85613 | -9.07712 | -46.91278 | 2025-06-26 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14d1fb07-f16c-3dbc-a27a-78459bca6746 | -7.19779 | -43.09798 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 065eb76b-0aa4-3cca-9d33-83b11793e1d6 | -8.67737 | -49.95486 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc0f38af-fbe2-3f7a-a378-2288b117caf3 | -9.51019 | -56.10049 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b71c4481-3ebd-35c5-bb5f-7ece72486183 | -8.06781 | -46.96878 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde265eb-3d5b-35d2-8515-23810f3ada50 | -7.19861 | -43.09193 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 454aad6e-8030-3252-ad57-1e8fdd57c75e | -8.85436 | -50.15564 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c577b4-d5d5-33c4-b78c-7dfcac18d592 | -6.17659 | -48.07413 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8016b6f5-4844-3594-9ea3-118ac78ed6dd | -6.17896 | -48.07532 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5bfc8f9b-c012-3cfd-8297-de90efc6f164 | -8.70955 | -47.98166 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a7049d1-2b41-315c-ac96-74e798465df6 | -4.71238 | -55.99252 | 2025-06-26 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa89c68e-d38a-3605-aab6-3c788e2dd5e4 | -7.20541 | -43.09292 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f7523578-e931-326a-b2b7-941508df8dd5 | -9.50021 | -56.0989 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24066c2c-e764-31ae-b848-73ff7948d3d2 | -7.75039 | -47.61594 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36894c93-8dc9-3bcf-ba75-edb0edd5323d | -9.51297 | -56.10452 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 039a5209-24b7-3d5f-9294-c73c7b350c9a | -8.26238 | -47.02298 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a71bf0ec-8294-3e55-9634-888d3d5e69a5 | -7.32114 | -45.7523 | 2025-06-26 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a477703f-bcbf-3372-a31f-6b1e39f5507b | -9.49411 | -56.09434 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2a2bc65-aa8a-336b-909a-fb7b647f8c6a | -9.51478 | -56.10813 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |


[Clique aqui para ver as próximas entradas](README16.md)
