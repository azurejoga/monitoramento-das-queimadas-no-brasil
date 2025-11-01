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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e1cd838-a1d3-3397-9d84-cb84e78a419a | -6.5833 | -48.7356 | 2025-11-01 01:20:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 29e35e8c-2c88-3bf6-911c-0181aa2bba3b | -8.2383 | -46.2481 | 2025-11-01 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8afbc8c8-908a-39b6-b194-93434b1d2cbe | -10.926 | -51.3196 | 2025-11-01 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 27d528aa-d16a-31fd-82ca-6226494101fc | -11.3963 | -48.9284 | 2025-11-01 01:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4dd5857e-431d-3944-ab32-871dda470ab9 | -3.2156 | -50.5795 | 2025-11-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 83d48240-50a4-3209-aa53-8a8424f1801e | -3.234 | -50.5999 | 2025-11-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 31cd5618-50bc-369e-96da-771ae82aca8a | -11.3776 | -48.9088 | 2025-11-01 01:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 09c6b435-e2e3-30fd-9ee7-d5588b3ceaf0 | -8.2383 | -46.2481 | 2025-11-01 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7a1f950b-186a-34dd-a8ae-64ea2dff5528 | -10.9257 | -51.3408 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 5eeb0758-b9b2-36ae-8a2e-2ca13805837d | -10.926 | -51.3196 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 15cb1563-7423-3251-8ec2-5799d160161e | -10.6313 | -52.1891 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f02afad8-3ce9-3b72-b6b0-d00aa1bfbfd5 | -3.234 | -50.5789 | 2025-11-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 346330d9-c4af-3557-b8bd-bf45cd331c30 | -11.3773 | -48.9307 | 2025-11-01 01:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 706911da-fb89-32f8-8dd5-defa0d482740 | -3.234 | -50.5999 | 2025-11-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4670b811-e6cf-34bc-a627-c418ccb91b4a | -10.907 | -51.3216 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 65bc84b1-b7b1-3820-b8b0-741ca15a3bcf | -10.6316 | -52.1682 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6085e612-d0af-33a7-bf8e-835a139e3060 | -6.5833 | -48.7356 | 2025-11-01 01:30:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 24c828e5-2925-3a24-b5b2-ccc4a3b0a6b2 | -3.2156 | -50.5795 | 2025-11-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f6b0fb4f-b594-39bd-9e6c-da6ccedaf065 | -10.6502 | -52.1873 | 2025-11-01 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3b893afd-77f8-330b-a633-d3fcef5fd577 | -11.3963 | -48.9284 | 2025-11-01 01:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9e926d5e-a9b1-3881-8bd2-9e3f26f75367 | -11.2607 | -45.5078 | 2025-11-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cf37f861-bb51-35c9-a498-499eab52612f | -10.6502 | -52.1873 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3bf1a5cd-df28-360d-ab5c-06b1637e5597 | -6.5833 | -48.7356 | 2025-11-01 01:40:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 33d63c8d-44e6-3757-9572-59bfbcba9d7e | -10.9446 | -51.3388 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 81b0b397-2af7-3fa0-b348-57d527b76d55 | -10.907 | -51.3216 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0a0375b0-dcac-3032-be33-27570709e312 | -10.926 | -51.3196 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 8f36b173-11cb-34d4-9360-d2a086e0cc9a | -11.2607 | -45.5078 | 2025-11-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 41ad8aee-7c5c-3b9d-9cce-7bda844505af | -11.3963 | -48.9284 | 2025-11-01 01:40:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| fb1bca4d-7c5d-323a-93ae-d07f648dfcf0 | -3.2156 | -50.5795 | 2025-11-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 40cda463-b596-3f82-8ee4-51a1beee21fe | -4.776 | -46.491 | 2025-11-01 01:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| fc07de19-3fdd-3756-8e62-561335da640b | -10.6313 | -52.1891 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e7e2dd7c-23cd-39be-8565-dd8802ec07fc | -3.234 | -50.5789 | 2025-11-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 8456c6d3-c1be-3147-b602-3dcf9927f9a3 | -11.3773 | -48.9307 | 2025-11-01 01:40:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 58d47f36-6178-3bdc-a4b2-38aa5bb80a98 | -10.9254 | -51.3619 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cd8530af-d921-3078-b0a7-bf02248f74ec | -4.4563 | -44.2102 | 2025-11-01 01:40:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e0c5c0b4-61f6-383d-a48d-a31d5f7e8f2f | -10.9067 | -51.3427 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 4490dab2-5fdb-3cde-8141-23282b86f907 | -10.6316 | -52.1682 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c2d6f496-1b8f-3218-abd3-021d9a017b11 | -8.2383 | -46.2481 | 2025-11-01 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4847d653-4a51-30e1-b2f9-c1f9cad4f58f | -10.6124 | -52.1909 | 2025-11-01 01:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 89f686ca-799b-39e6-babd-f869febdaa29 | -10.9257 | -51.3408 | 2025-11-01 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 0589fa1f-c73a-3563-b366-7d1fd3e69d43 | -3.234 | -50.5999 | 2025-11-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 44f79ddf-81a7-3b5b-bb32-0407784c3c79 | -13.32433 | -60.72643 | 2025-11-01 01:49:00 | TERRA_M-M | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 30.6 |
| e9b9b2da-e5e0-3a7b-963b-16e2fd080559 | -13.32827 | -60.70723 | 2025-11-01 01:49:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 493b3af6-5843-3db2-8b79-08851c990fa0 | -11.4389 | -45.1385 | 2025-11-01 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 104d797f-08b1-3959-bd56-8491c65a422b | -10.6313 | -52.1891 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4ca6b430-294d-3ba4-9c24-72c1da199479 | -10.9257 | -51.3408 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0b04bffb-6659-303b-9fd3-ee987b99225f | -13.6011 | -42.9001 | 2025-11-01 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 6e001c90-df1d-3c8f-8bff-465b0194bbb2 | -6.0737 | -47.3142 | 2025-11-01 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 322ad780-e070-3e93-9c17-cadbd9760ce5 | -10.9067 | -51.3427 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9bf7eb50-2c01-3387-8f2c-e971c492dc61 | -13.5816 | -42.9038 | 2025-11-01 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 84.3 |
| ebb29fa5-ba8a-3832-bcd1-3ffb00235b59 | -3.2156 | -50.5795 | 2025-11-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f00f357e-3025-3c02-a08f-545eb9b65f54 | -9.7419 | -36.0772 | 2025-11-01 01:50:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 3813497f-b2fc-37b6-bfdd-3cb192e25602 | -3.234 | -50.5789 | 2025-11-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 3c3d25b7-64d7-3a60-b0a2-853183f933ae | -11.2607 | -45.5078 | 2025-11-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3e4d3f06-4c51-3199-8e8f-130159e2930a | -11.3773 | -48.9307 | 2025-11-01 01:50:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 33fa9f66-b0ad-33dc-883f-a1ded5edf7b7 | -11.3776 | -48.9088 | 2025-11-01 01:50:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3eebc03a-1906-3299-ab7c-c8720f98d0de | -13.5821 | -42.8796 | 2025-11-01 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 62f38b7a-cc11-318f-bac6-fb14f6b76fbd | -10.907 | -51.3216 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9cdab998-3722-35fd-9623-84d7f05c0447 | -13.6016 | -42.8759 | 2025-11-01 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 69.0 |
| ef702be8-fb53-3b7b-a669-fc834013b8f2 | -10.6316 | -52.1682 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 69faf2d1-51f8-3161-9dfd-4eb8f3525277 | -10.926 | -51.3196 | 2025-11-01 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2560d3d8-ae00-3742-b358-957aa24f09d8 | -6.0735 | -47.3362 | 2025-11-01 01:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e782e888-74cb-3844-a395-86d0935807d3 | -6.5833 | -48.7356 | 2025-11-01 01:50:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e63cc1b9-1a78-3134-849a-8c527e358973 | -12.56056 | -62.04013 | 2025-11-01 01:52:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ab53ac6a-7ae0-30fe-a049-78325091c17e | -12.84542 | -62.16856 | 2025-11-01 01:52:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 07704b7b-9694-38cb-82e7-561cdf3ab9ba | -9.22949 | -67.61596 | 2025-11-01 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 42f5912f-dde1-3935-a8e8-56bed5d19045 | -3.2156 | -50.5795 | 2025-11-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7155f585-1f76-3593-bdaf-639a8e3dc4dd | -6.5833 | -48.7356 | 2025-11-01 02:00:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| abe5cec5-db31-3834-aedb-5b36a5f92a3d | -11.2607 | -45.5078 | 2025-11-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e48996cf-ac19-3ddc-8e76-98d7b7963f8d | -3.234 | -50.5999 | 2025-11-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| aaaa13c4-68e7-387f-99a6-4b732cfbb824 | -11.3773 | -48.9307 | 2025-11-01 02:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c9d611ef-03bc-3aa8-9a47-ac11d74d2e81 | -10.6316 | -52.1682 | 2025-11-01 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d2f6d970-92c1-38f6-ac43-980f0220b3ae | -10.6313 | -52.1891 | 2025-11-01 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 6f41b957-9a03-3f9d-bb11-f470b53810a3 | -3.234 | -50.5789 | 2025-11-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 0841ca5f-a386-3bfc-b978-e3fcc23518e5 | -16.9328 | -50.4894 | 2025-11-01 02:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 74c6aa6d-59f0-3b8b-b303-51479c5f3242 | -16.9131 | -50.4927 | 2025-11-01 02:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 45048954-69de-3575-b703-cea985d73fae | -11.4389 | -45.1385 | 2025-11-01 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 20700e37-b3eb-311b-9bea-e26bc33e925c | -10.6502 | -52.1873 | 2025-11-01 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 40d69d44-7335-3d36-b60f-cab56d01d410 | -11.2607 | -45.5078 | 2025-11-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1644b655-fb65-3435-9436-7483450db8af | -3.2156 | -50.5795 | 2025-11-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 45342bd9-fb25-32eb-8b7f-e6165b9f78e5 | -3.234 | -50.5789 | 2025-11-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 43e6c683-6f0c-390d-84ce-4395258bddbc | -10.4222 | -44.331 | 2025-11-01 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5cf3537c-de17-3505-b53a-824486d17527 | -10.6316 | -52.1682 | 2025-11-01 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c5b34034-e26e-3985-80e4-44d68c9e2dba | -3.234 | -50.5999 | 2025-11-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| eae4a38a-96dc-3fce-8e32-7bfe9edc6180 | -11.3773 | -48.9307 | 2025-11-01 02:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 49bd3c00-331a-3076-a6d4-ec4b97bbdcb9 | -10.6313 | -52.1891 | 2025-11-01 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 70a170ce-2aa7-3458-97de-2f376e7eb6b9 | -8.2383 | -46.2481 | 2025-11-01 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| f9d5d1d7-3783-329f-8c38-464f68906130 | -11.3963 | -48.9284 | 2025-11-01 02:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 94753ba5-a10f-3fb8-80f6-0f5c0a41fa43 | -16.9135 | -50.4707 | 2025-11-01 02:20:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 63327174-1633-3533-b868-84d6f9cb8b61 | -11.3773 | -48.9307 | 2025-11-01 02:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b5f14d2f-a466-34c0-860b-c4e0e9dc3ee2 | -3.234 | -50.5999 | 2025-11-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a9a145cf-958e-316d-b68d-1da4b34ce630 | -10.6313 | -52.1891 | 2025-11-01 02:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0947ce55-31da-3e26-84b7-200fc4648fc4 | -3.2156 | -50.5795 | 2025-11-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a44da4be-7a21-3141-8a08-3861a4a941e6 | -11.2607 | -45.5078 | 2025-11-01 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 99462141-c60e-3fae-9de7-00b14089941b | -11.3963 | -48.9284 | 2025-11-01 02:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1b68c9a0-8f3a-3afb-91e0-88bbc2ac4b3a | -3.234 | -50.5789 | 2025-11-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 3fab6196-f782-3165-9390-d574850da713 | -11.3963 | -48.9284 | 2025-11-01 02:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| efa87359-922b-386c-b9ac-ef7f951706e4 | -3.234 | -50.5999 | 2025-11-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5779a56f-d87f-3d3e-98c6-9eb120be56fb | -3.234 | -50.5789 | 2025-11-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| ea3e16ea-ba67-37d0-ad50-0b8ea701b0db | -3.2156 | -50.5795 | 2025-11-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |


[Clique aqui para ver as próximas entradas](README9.md)
