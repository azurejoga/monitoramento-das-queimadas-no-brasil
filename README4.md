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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c944f559-2f16-3383-addd-c6a2c7b01e8a | -9.4289 | -44.7113 | 2025-09-21 02:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cf3a2680-2165-3ee0-acdf-e7ee170d1ea1 | -5.5243 | -43.8647 | 2025-09-21 02:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d8938d4b-e4a7-3e8f-a314-6e00b63789d6 | -6.0959 | -40.9996 | 2025-09-21 02:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 2eb4736f-b387-3bf6-8d04-6e2940474c75 | -11.6377 | -50.5839 | 2025-09-21 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b1b81187-acf3-371c-aa95-92b59a2fd5a5 | -11.6183 | -50.6075 | 2025-09-21 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b10d5ed8-f2f6-3f8a-a21e-491290db3279 | -13.541 | -42.9835 | 2025-09-21 02:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 937e82ec-8059-3402-b0a7-2ffc3968aed7 | -11.6374 | -50.6053 | 2025-09-21 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a1cfa670-93bd-3876-9026-6d74dbd82f18 | -12.7114 | -46.8454 | 2025-09-21 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 612ac3dc-f9a7-300f-bad0-3c8d940dc374 | -12.7114 | -46.8454 | 2025-09-21 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 344f518a-b88e-3a98-bd68-0fbc39768e15 | -7.9445 | -44.0918 | 2025-09-21 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 23f3acec-74e4-3e68-a82b-cb4dea55e35a | -7.9256 | -44.0937 | 2025-09-21 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2ed94046-1363-35e6-90b4-a6edcbc83738 | -11.6186 | -50.5861 | 2025-09-21 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b0896965-d81b-3aca-93f1-e54654405017 | -12.7306 | -46.8425 | 2025-09-21 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 89a487b9-395d-3ff4-83e2-5d0da0f1a40c | -12.7118 | -46.8227 | 2025-09-21 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 3d37fef1-b87d-3f99-b431-5fa6dab3f4a2 | -13.5405 | -43.0077 | 2025-09-21 03:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 8a94aa24-2317-3555-8e54-fd795cd69b95 | -11.6377 | -50.5839 | 2025-09-21 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0f1c559d-c6de-3aa0-b6e8-dfff42ccf443 | -13.541 | -42.9835 | 2025-09-21 03:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 8a08673d-c71f-3500-aa78-7ebde08b299e | -7.9253 | -44.1169 | 2025-09-21 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 704fa71b-4d51-33e7-af5a-948e1da435ba | -7.714 | -44.4612 | 2025-09-21 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| cc416c5b-0be2-3c6c-8c00-08688d8ea93f | -5.5243 | -43.8647 | 2025-09-21 03:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b7506d60-237c-3c86-8020-e16191f2ae82 | -11.6183 | -50.6075 | 2025-09-21 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 235cadf4-b7e7-3d23-9185-022589cc9596 | -7.7328 | -44.4593 | 2025-09-21 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b82b2452-7b0c-3496-ad92-828246d62729 | -11.6374 | -50.6053 | 2025-09-21 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f8c020bc-8440-35cb-bda3-bb3589b25424 | -13.541 | -42.9835 | 2025-09-21 03:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 81d20b66-1589-369c-8770-e11d5f82cf66 | -7.9256 | -44.0937 | 2025-09-21 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cc7ec533-e2bf-378b-ad72-adb3982b1b69 | -12.7114 | -46.8454 | 2025-09-21 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 19410ea3-d55b-3289-a5bc-87059e5a766d | -11.6183 | -50.6075 | 2025-09-21 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 37a53b1a-25c3-3be0-a449-544c5d2cbe3e | -11.6374 | -50.6053 | 2025-09-21 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c850deee-8191-3dbd-81aa-85b8b6040a4d | -15.9586 | -59.4288 | 2025-09-21 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2276dfa7-8ee6-3102-817f-d2576e0c4f09 | -13.5405 | -43.0077 | 2025-09-21 03:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 76a71fdb-f9e0-31df-8f6e-603167ec224a | -11.6186 | -50.5861 | 2025-09-21 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 70f072e2-634f-3288-9b29-b63ef16c88d0 | -5.5243 | -43.8647 | 2025-09-21 03:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a7797a7f-783b-366c-8d54-733ffcd2d2a2 | -11.2499 | -49.8341 | 2025-09-21 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3dbd7a3a-1dca-37af-b5c1-46abea51f0b9 | -10.3681 | -47.8875 | 2025-09-21 03:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7a98a1b4-cdc4-3fe5-bac0-d8a5769d873c | -7.7328 | -44.4593 | 2025-09-21 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4ac05847-e2d9-35d6-95a8-1e45bb330f92 | -7.9445 | -44.0918 | 2025-09-21 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7a3c093a-8f6d-3fc3-b27a-2531dbb3c35a | -11.6377 | -50.5839 | 2025-09-21 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b45a3722-09e5-3d8a-90ad-0f394a0abe9b | -10.3677 | -47.9096 | 2025-09-21 03:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f5313ca6-d5ff-3334-acb0-073b20f2b807 | -7.714 | -44.4612 | 2025-09-21 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| fc71f08e-dd6f-3857-ae6c-26e391b21f4a | -9.4289 | -44.7113 | 2025-09-21 03:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7a841e15-7ae3-3e52-91a4-12720843bdb6 | -6.0897 | -41.00869 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9bca2aa8-73ce-323b-9526-0c933e504d2b | -4.61419 | -38.6875 | 2025-09-21 03:15:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cccb2009-14c3-3fe5-94e2-49e27a2c2234 | -7.33919 | -39.71391 | 2025-09-21 03:15:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e783f39-8a5b-39b4-b924-22fbb2dbdcab | -6.08481 | -41.00051 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8c2127c-21dd-3aa2-a86e-741811615904 | -6.08383 | -41.00598 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a326dbf3-9a76-3999-9b76-12f044273748 | -6.08435 | -41.0014 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d30fef0-1d81-3fe8-987c-6bf4746aaab5 | -6.08333 | -41.0069 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 976aced7-7d37-397e-87a3-815e84b26da6 | -6.09021 | -41.00777 | 2025-09-21 03:15:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4976c5b0-5d66-3e67-aeb9-74e37aa0099e | -7.33997 | -39.70967 | 2025-09-21 03:15:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e882a24-f746-309a-b486-034779b0ac06 | -8.48158 | -39.9362 | 2025-09-21 03:15:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 870b01c6-b4d6-3488-9707-ee7a0629c0f6 | -4.61488 | -38.68354 | 2025-09-21 03:15:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 755d8cb5-aec9-3b28-9dc7-2aa44e9a8803 | -8.48234 | -39.93208 | 2025-09-21 03:15:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3ade8a3-a0bf-39e9-a83a-623295d67159 | -11.20253 | -42.20087 | 2025-09-21 03:17:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b7e8a3d8-9918-352c-8798-d73ef3fcebc0 | -11.45969 | -43.54543 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4357b2d6-5a4f-36fd-98f4-857da9dc2bb3 | -11.49893 | -43.59673 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c76378b2-5d3d-31ca-866b-28e1352ce160 | -15.53387 | -42.17863 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5882990f-9fd0-3d0e-a379-aa09067702f9 | -13.53856 | -43.01101 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 5afb6a51-4677-3776-9121-6621f2132701 | -13.53336 | -43.00365 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 065a858e-3fed-3910-99e4-e5c8c192f31f | -15.52796 | -42.17728 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e755b6-7d56-3abc-a8e8-323638ea6219 | -11.49425 | -43.58696 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49b00341-baca-349d-9241-b8f8036ea506 | -13.67763 | -43.82177 | 2025-09-21 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f66aaebd-4f7c-30d2-a183-cf6e89993635 | -14.25228 | -44.38274 | 2025-09-21 03:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85fb3f53-8be9-30f0-8ed7-d222d46b7ebb | -12.35163 | -43.76067 | 2025-09-21 03:17:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fdb66f9e-a8cf-35c4-8f32-5163b6290519 | -14.97611 | -44.41832 | 2025-09-21 03:17:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b22af454-7147-3287-9faf-08b27162ed59 | -13.67879 | -43.81631 | 2025-09-21 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ef78354-192c-3462-b272-1e6d5b483497 | -11.50029 | -43.59025 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06d3c542-a587-36fd-91e8-b4ab953f4135 | -13.3628 | -44.2836 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d5d6925-6a18-390b-a79d-92d0a07e662a | -13.36285 | -44.29106 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddbedd81-b2c8-3f42-a637-aba8ac32a42d | -11.20421 | -42.19706 | 2025-09-21 03:17:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9af48f06-cc44-3685-b47f-09dac02ffd05 | -13.68217 | -43.90661 | 2025-09-21 03:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96e770ba-775b-31c5-b684-2fc3e2c2453c | -13.53942 | -43.00799 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 2dee73e5-ac21-3ec6-a7f6-fb50ba8d5d94 | -15.90393 | -43.04901 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7731d51-9c79-33f6-99b2-d1773063f002 | -11.20357 | -42.19565 | 2025-09-21 03:17:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9a280a75-ae58-30b0-afea-651ad9608890 | -15.4838 | -41.92131 | 2025-09-21 03:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0f3392fe-78a4-3af5-b45d-2eb46b0724f3 | -14.25085 | -44.38921 | 2025-09-21 03:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2e325ea-dce5-35f4-918e-e4654131708c | -11.27572 | -41.84939 | 2025-09-21 03:17:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc543d5d-957a-3e23-b16a-43d6ab091be4 | -15.53479 | -42.17418 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4451c17-95d1-3e64-a8c3-c75cd48341ca | -13.36429 | -44.28433 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90be3acb-e2e2-343b-9013-a209dce2cb0c | -14.97472 | -44.42471 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15bb057d-521a-31f6-9c70-f2bcb41e37c0 | -14.02088 | -43.74009 | 2025-09-21 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e18593fe-3fed-3afb-853b-6ea9e7dc1760 | -14.96798 | -44.42294 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87e2474-91c3-3f08-94a9-d029a88f298e | -11.20894 | -42.20209 | 2025-09-21 03:17:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03cb9997-04a8-3979-83b9-514f2bcaf282 | -15.53184 | -42.17323 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1287819-b1ad-32c7-9e93-d395fceae700 | -13.53219 | -43.00929 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 19c2dd40-b02d-36e3-9fc0-d22b92908f32 | -12.33424 | -44.10658 | 2025-09-21 03:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 577942b4-a76d-38f0-b61a-f7aa4db8138e | -13.35594 | -44.2894 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25fd0091-3267-3a35-b039-4e31dae4cabd | -13.54065 | -43.00224 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| de9f26d0-2535-3ea9-959c-81c8781a223a | -13.35441 | -44.28868 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3ae8e20-cb82-3ee4-be1d-1abb4a0fc0ed | -14.9751 | -44.42682 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b6433c8-ed33-3ce2-81d4-db0ca470c8b2 | -13.53975 | -43.00527 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 10efaa11-918f-3eb0-a349-e3de8f5d448d | -13.24995 | -44.11371 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d7bb6d2-2868-3693-90f0-4194c3647556 | -14.97334 | -44.43107 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6f7e3e2-79c4-3f54-b64f-dbd9164fa271 | -15.48573 | -41.91811 | 2025-09-21 03:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0bc107c-c024-34af-9140-ce248a6a7873 | -13.53303 | -43.00636 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 3d00c84d-0899-37c4-ab87-2bb4482d0547 | -13.5382 | -43.01368 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 4539977f-3927-3c76-9492-8cad19c51fa7 | -11.51257 | -43.63474 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb590192-183e-351d-9fe6-d49273b3880e | -11.51391 | -43.6283 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc0b3d3b-0b07-3bd7-91b8-14fc48d3155c | -15.52891 | -42.17274 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e79292a-e5ca-3ed9-bc59-4d7c86d2bc29 | -12.33788 | -44.10093 | 2025-09-21 03:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0be6035d-228d-3f56-816b-9a76cc18c53e | -11.5084 | -43.62019 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README5.md)
