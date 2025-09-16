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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3ac60d2-8fa7-3a4c-9c9a-48e9c7396927 | -9.74478 | -47.8465 | 2025-09-16 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa418c58-bd7e-33ad-8b1d-21597ed79910 | -8.43874 | -55.61629 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ffdff20-ef13-3f03-ab1b-d2b7fc6c397c | -14.36273 | -52.92068 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d69bbebf-8b49-3cc1-b63b-5d0d1ec9c407 | -14.87713 | -51.63715 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7929d9f2-519d-3d7f-972c-21a74b05f78c | -10.42414 | -50.65104 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8923bcf0-66c8-3b7e-8d82-7f0b84d46882 | -8.60296 | -46.40908 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfb9605b-4eb5-30b1-a817-0eec9f619e9b | -12.4412 | -49.71048 | 2025-09-16 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f0d4d5-c88d-33d8-a756-219e91472b59 | -10.04921 | -44.34621 | 2025-09-16 04:51:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b02b0dc6-9a8e-3179-8830-c850f1dbf771 | -10.71785 | -44.74698 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65c10e60-43ed-30cd-b8f8-e30fe27475b6 | -14.80841 | -51.66604 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 6db4a8d2-c090-3602-899b-93ad39c0bc30 | -12.26107 | -53.91921 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91bdc33a-8be4-3b7b-97f2-1bd92122554f | -15.07848 | -52.48361 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64fe0be6-aed8-311e-8960-42b87068e927 | -14.65486 | -52.06882 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a2066ac-f05e-3c39-bdbb-d84dc123f7db | -13.21641 | -47.29083 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a43f3a74-71a9-3545-a9fa-8933b1a51e0f | -10.71894 | -44.74674 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 745b8166-d450-3fa9-b780-f3a05e1583f6 | -10.71819 | -44.75272 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a48dba0a-235e-33eb-91d5-ef234047fbd2 | -12.96932 | -47.96762 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1863639-a5ac-30dc-b80d-906d5b0718a1 | -9.05123 | -44.85394 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f04d5909-b279-3ec1-93b9-c33a51b14060 | -15.09224 | -52.48591 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b7e840ea-eff4-3653-ae1d-23e5ea7d7083 | -9.73346 | -55.37266 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7430d25a-adc6-359a-a324-cde000e77151 | -11.11248 | -45.33817 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0d72f44-aeb0-354c-b588-1657e015690d | -11.27951 | -50.79353 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0910f196-cd96-3cf2-809a-ffe630fa4b11 | -12.64144 | -47.95768 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6db67591-5feb-37a3-9735-7f22bdff2c42 | -8.88527 | -46.19457 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1669cd28-89d9-39f8-8fec-0dd4e625d919 | -8.76377 | -46.09239 | 2025-09-16 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b40fc629-7f6f-3ac2-9f99-cb8fc314c01b | -9.07421 | -50.30719 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b461ca49-774e-3d10-94b1-426ad2caf047 | -9.06354 | -47.02657 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6a037247-5801-30af-922c-273a7f1953a9 | -11.13183 | -45.34669 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32fdf75e-f470-3b45-8bdb-6ca7d3299dfd | -10.63755 | -48.74668 | 2025-09-16 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61b11012-0c78-3dad-9964-d062cf0f1006 | -13.7473 | -48.77254 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff98194a-4185-3dc9-8d7e-498f4a6907e0 | -11.12643 | -45.34888 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fce72dff-4758-3765-baf7-9752921e6d5b | -14.29971 | -49.53294 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 822d4cf6-cc37-343f-bee9-f33a7a16155a | -12.61864 | -45.74546 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb674302-5e93-36c0-a77d-fc90feb0ea23 | -9.10003 | -44.86571 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 11b5e82c-b7bf-3f1c-9c76-4ae8f3cf9f1d | -12.6694 | -47.94498 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc8125ec-e0b6-3689-a719-397cf9e71656 | -10.55245 | -51.96626 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 282ac6a9-8ae3-320f-ad22-f8265c20d421 | -9.08661 | -44.85046 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 966822c5-5dc6-3806-af7e-69a4011756a1 | -10.40295 | -50.6226 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4643f7df-19b1-320f-9d5e-664fba9efaad | -12.97361 | -47.96836 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 229a3e19-76ce-37f5-b329-9a6122b31d46 | -9.07347 | -50.30626 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26c2b211-7d05-34b4-ba69-19911b7be82a | -14.82613 | -51.66318 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d49f391-0cc3-309e-8bc5-6df3668d557a | -9.04815 | -44.83876 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7032daea-c995-396e-98d6-7566416b8f5e | -12.61361 | -47.95031 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cd49f4d-7c3e-39d4-beff-6872d19fd38c | -12.81796 | -47.23058 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0445972-08cc-332a-90a4-242b68484bdd | -11.11363 | -45.32924 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2341778-fa0c-3621-8023-b2cae6a89510 | -12.00732 | -46.65458 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83727021-3345-3bc5-a4fd-e7c4347df0e3 | -12.62571 | -47.98989 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a5e885-0200-37d5-b041-71e4c5253e8d | -15.62472 | -47.36822 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 635986a5-6840-3ec9-9c85-2ea70dfa2c20 | -12.66414 | -47.70892 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2ceaa3b-dcd2-3766-99cd-74b42a5c478e | -10.63975 | -46.23102 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd7e921b-4e46-3d8e-b6ad-e81879cfd5cc | -13.00448 | -47.94897 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71cc87ac-7326-38e9-81e7-9a3aae02ea71 | -15.62639 | -47.37172 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d36846c3-05d7-3b65-a706-6042aba832f4 | -14.51762 | -47.32747 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e846528f-f025-38d0-ad46-d3a926d48153 | -17.86494 | -44.44604 | 2025-09-16 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39632b6f-7575-3d80-94a4-44b281ee1d8b | -16.51765 | -43.55529 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b0ef628-b9dd-3056-8950-4dfff50ddde6 | -16.66381 | -49.75983 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fc4bab0-4583-352c-897b-a3a3dc3525f3 | -16.02373 | -59.45288 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed1b0830-6493-33ae-b439-6d4be05cd754 | -16.02163 | -59.24242 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08953500-c888-3bb4-90fc-973902c777f8 | -15.99982 | -59.40755 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5454fb00-6531-3093-9bd9-3f6863e4987a | -16.92889 | -44.07158 | 2025-09-16 04:53:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4f102fc-6c60-39e9-a13f-0dbfdd55b138 | -15.78007 | -52.20396 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d2db2db-a409-3fa2-a563-0b59b94b0365 | -15.99507 | -59.25772 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b1fe9e4b-3f9e-3346-924c-3b72a2aa23db | -16.48024 | -55.11189 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8850bd53-ba44-355b-93ec-9404226b3db2 | -16.47444 | -55.10751 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cbd1be8c-39cd-3334-a4f0-66aebc0f5543 | -15.83579 | -53.47245 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04640e33-33cb-394f-9f62-a8cd58d03d09 | -16.7232 | -54.94954 | 2025-09-16 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f2e808-bd1d-3ee4-9797-7c956fc22cc5 | -16.01951 | -59.43165 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14e0c8df-354f-30df-a040-82709a902def | -15.82178 | -53.474 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5095fd16-3551-3403-9c73-57753e3bebb2 | -15.80047 | -53.45547 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e78b2767-c243-3520-975b-aa8db9bac093 | -16.47693 | -55.11132 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7e76b67d-5c19-3972-8f70-23cb97fa945d | -15.84196 | -53.4772 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfa544cb-05c7-3fac-ac4d-07ac8e12f15f | -15.78238 | -52.21265 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45c0cca1-7e5d-3810-8b1d-1ff93c42d0b9 | -17.08066 | -45.83363 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 72c7a5fc-10bd-30e2-9159-12b9255890c0 | -15.83187 | -53.47562 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73d3d4d1-2d2a-3278-979d-159ffecf4fcc | -16.69066 | -49.77456 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4158b828-9947-3967-8152-5a967e87695a | -16.68404 | -49.76255 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa9279f3-07d5-390a-84c3-f723a79b2f19 | -18.16972 | -45.19478 | 2025-09-16 04:53:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ace7744b-80d1-3c6b-adc2-c8481d965bc3 | -16.47854 | -55.12265 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dea50a61-4642-3ac8-bc3e-6789ec3d36d0 | -15.79051 | -52.18148 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88364596-f04c-36c3-be1e-02008b2bfeae | -16.72651 | -54.9501 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4fd66b-e472-36f2-aea3-1b21c6877b23 | -16.6902 | -49.77801 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42fde321-ddfa-3bd4-b51c-2e48747e18cf | -16.67762 | -49.77977 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 555362ff-757c-389f-818b-6f3b77d6295d | -16.69742 | -49.78557 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c8744d5-3c7f-3d1f-8889-8f98e53cc111 | -16.57881 | -55.15461 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 05a08a24-4b5e-348f-971d-e76c27301657 | -15.79809 | -52.17871 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f7a9fc23-c081-3d99-a080-5eebeab92d7e | -16.03712 | -59.44522 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4cfd3d5-dddb-3223-8c6d-93170a859e20 | -15.83504 | -59.42498 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 981588f1-2b03-3a94-8630-16ffd6cf6369 | -17.30243 | -40.68642 | 2025-09-16 04:53:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d455a4b1-a991-30ea-8259-404b6621bfb7 | -15.01335 | -55.34412 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7bca620-515f-3aa2-85e3-d3f29a2958ca | -15.99893 | -59.41244 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3733ff24-e3d8-3cbb-80d7-46563b3a86fb | -16.58947 | -42.90607 | 2025-09-16 04:53:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fe117b8-5a5b-3d7a-ac53-3ae0972fee47 | -15.62792 | -52.78644 | 2025-09-16 04:53:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c56154f-6657-316f-9a38-48b0955ee0a1 | -16.71605 | -49.23134 | 2025-09-16 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8af9bc31-3f2c-3d2a-9588-11cf42766f62 | -16.68613 | -49.77769 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 949e2b6f-2547-3e06-abc4-94170eedca32 | -16.48138 | -55.10471 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 85206229-1990-3a6a-9e1f-6ff4afcca437 | -17.07574 | -45.82983 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 037e5154-4cba-3674-99cd-e6b22aa4c03e | -17.72725 | -46.77401 | 2025-09-16 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39d0cd9d-6640-30c7-b24b-8bad2331ed1e | -15.99359 | -59.2564 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7676343c-de34-381b-928c-4e1577e3039e | -16.47501 | -55.10392 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 742d489f-381a-3b87-9cca-676d22ea5231 | -15.78812 | -53.44593 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README78.md)
