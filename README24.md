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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66668cf4-a210-37a2-9ad8-62ca00f0ada4 | -7.4975 | -55.0055 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f3d01ac0-6370-3ada-9c9c-e0d097742385 | -18.9222 | -47.9105 | 2026-10-10 02:40:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f99f6944-af7b-3e96-aa22-162a2e719676 | -14.453 | -43.9598 | 2026-10-10 02:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 453f6b17-0096-366e-b5ba-e9e8742648a2 | -5.7565 | -45.1293 | 2026-10-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cc0c5a13-aee8-344a-a0bd-e77bad58ab2b | -3.839 | -55.7997 | 2026-10-10 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e1957176-1899-309c-ae67-4b09b41104bc | -7.5162 | -45.3024 | 2026-10-10 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 79023cbf-43b3-35be-9323-c9cfa4356fdc | 2.727 | -60.2586 | 2026-10-10 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 49e264ee-cc9e-392a-ab76-019016e55de7 | -12.2154 | -57.1287 | 2026-10-10 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a81085a9-f7e4-3e26-9641-f60be91059f9 | -3.6048 | -54.5936 | 2026-10-10 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0d604f37-dcc1-377a-9c8c-8cfa08004a20 | -3.2204 | -49.4205 | 2026-10-10 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2f901398-ce8b-3106-8a8c-58a12e9b1972 | -3.9912 | -59.356 | 2026-10-10 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2463c7ee-32fc-3431-86c7-5c6212dae62b | -3.839 | -55.7997 | 2026-10-10 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0d3a35ca-895c-32c5-b66e-948172d57727 | -3.6048 | -54.5936 | 2026-10-10 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| de2f5a05-f48f-3fa5-af8f-b9fb3a596574 | 2.727 | -60.2586 | 2026-10-10 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5099bc23-c5e9-3a9b-bb22-97ad6d78a4ea | -6.4595 | -55.0615 | 2026-10-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e4bc375f-9a9f-370b-a4d2-158bf050cffe | -3.7494 | -60.6014 | 2026-10-10 02:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| ebd8d828-7c37-3039-a05e-828b55cdcfa4 | -6.9566 | -44.9662 | 2026-10-10 02:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bc08afb5-5925-3915-97f8-86e0c3e2e9bf | -7.5162 | -45.3024 | 2026-10-10 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 03fafeb1-793a-3a71-8ac4-65416f36bc89 | -10.8909 | -44.8001 | 2026-10-10 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3d01af72-0018-3102-9612-308e30dbed16 | -4.4025 | -49.7774 | 2026-10-10 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 37f76205-d39b-37df-b166-ddcc18b6cb70 | -7.5871 | -64.5845 | 2026-10-10 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 683e61df-a67a-3722-9f3b-ae9166434d33 | -7.5159 | -45.3251 | 2026-10-10 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7fc1a5ae-7e9b-3909-9b55-011d80faf6b3 | -12.3051 | -47.0392 | 2026-10-10 02:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d6d2e002-2a0f-33d5-b994-9bf8143a41b1 | -5.7565 | -45.1293 | 2026-10-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 93bf2b75-a551-3dd8-8819-b2193260600f | -12.2154 | -57.1287 | 2026-10-10 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 803f2487-5268-3680-82c7-3f6197ae1c48 | -9.9384 | -44.8791 | 2026-10-10 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 634fce14-510b-383d-987a-8a209313abe1 | -4.5929 | -55.7168 | 2026-10-10 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 662dd5d8-de86-3645-bf11-0bbc2a2f4202 | -7.535 | -45.3006 | 2026-10-10 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a6815c2b-8946-3fdd-bfed-f8d171364606 | -6.4411 | -55.0424 | 2026-10-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 935def92-9092-3223-bfe1-ef4e0a112dbf | -3.5676 | -54.6946 | 2026-10-10 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ea2673e3-1a5f-3d85-a84b-81930595bf62 | -10.9097 | -44.8206 | 2026-10-10 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| bbe3989d-44cb-3e40-baf8-33908b466226 | -7.4975 | -55.0055 | 2026-10-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4aa637f2-fe78-3fcc-9e9d-06b398762a04 | -7.5347 | -45.3233 | 2026-10-10 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 11471c9e-2108-38ba-95c9-51bb13fe4f88 | -3.9911 | -59.3752 | 2026-10-10 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fb3a0ae4-5c0e-3f9f-8729-34f790d8c9d3 | -12.2152 | -57.1488 | 2026-10-10 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 57257e14-3f52-39af-a5b4-0f31465f13b0 | -3.9912 | -59.356 | 2026-10-10 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 37a18333-e3db-3cc9-aa99-9b9b1d334f75 | -10.8905 | -44.8232 | 2026-10-10 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 54c2834e-06f2-3436-8be2-46f26ed70cf1 | -6.478 | -55.0606 | 2026-10-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 80a8d669-2cbc-395b-bc4b-96c6c5f820c7 | -7.9086 | -54.7194 | 2026-10-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e469f037-3baa-328f-8664-3559d9c446bf | -3.2388 | -49.4411 | 2026-10-10 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 94bcbc2c-0cce-3920-81ed-5e259dfe2af4 | -12.2154 | -57.1287 | 2026-10-10 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 203035cf-d4b0-366f-855a-836541fb4427 | -4.4025 | -49.7774 | 2026-10-10 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a63028a9-4e1c-3db7-bda8-ca0fbdddb3db | -7.5162 | -45.3024 | 2026-10-10 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f41e1d71-a390-3c0a-8213-926106a2b462 | -3.9912 | -59.356 | 2026-10-10 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 23afcb76-c7ad-3c2c-8520-a27b24559bff | -14.4003 | -54.9657 | 2026-10-10 03:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cac34758-4ba3-3fa6-9ebd-fbd274f3da2c | -5.7565 | -45.1293 | 2026-10-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| de3b55a0-27e4-327f-b54b-ce0be2b7d9ad | -7.9086 | -54.7194 | 2026-10-10 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 77819200-68fe-36b1-9df2-8f425bf7f8f0 | -3.6048 | -54.5936 | 2026-10-10 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8a255458-44fc-3794-807d-d3296a6df0e6 | -9.1108 | -45.82 | 2026-10-10 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5645c1f8-7bbc-39db-88e3-6ddbc0c31baa | -7.4975 | -55.0055 | 2026-10-10 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 97fec09d-4094-3184-a75d-9b62bf297dd2 | -3.9911 | -59.3752 | 2026-10-10 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 67524020-024c-3946-8c6a-0444869e606a | -6.4595 | -55.0615 | 2026-10-10 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 34b3711e-b594-364f-9212-c2c408e4cc85 | -3.2571 | -54.1824 | 2026-10-10 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 46657690-2b5f-362c-a310-25085189a6e9 | -10.9097 | -44.8206 | 2026-10-10 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1bbeebe5-963a-3bc8-bfbc-056691e403eb | -3.2203 | -49.4417 | 2026-10-10 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| cc0385e6-dc46-3c15-9ccd-28c4e1689d96 | -3.2204 | -49.4205 | 2026-10-10 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| de0ff6ed-93fc-36b3-9c1b-edac2809f0a8 | 2.727 | -60.2586 | 2026-10-10 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e0baaa82-d50c-352d-a9cb-d54f59acc462 | -9.9384 | -44.8791 | 2026-10-10 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2ee1364a-45ae-305a-9d7f-b7ef537816d6 | -7.535 | -45.3006 | 2026-10-10 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| b6e6c24c-d57d-3368-a0bd-5829c70a0aa2 | -3.5676 | -54.6946 | 2026-10-10 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f3aa90d6-5e0a-3b52-8d29-de6254285f95 | -7.5347 | -45.3233 | 2026-10-10 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 52544405-bfb4-3887-9b63-5d908fec4836 | -10.8905 | -44.8232 | 2026-10-10 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 419d2dd1-8461-3932-ba8d-7b771919f8a4 | -6.4411 | -55.0424 | 2026-10-10 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 3af5fb47-1471-317f-ac03-1f771157bad1 | -7.5871 | -64.5845 | 2026-10-10 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7a080b7d-28f7-3d68-89ad-bab2b8afe954 | -3.7494 | -60.6014 | 2026-10-10 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b5b1c608-e844-305a-82ab-7f6f01aaa0d7 | -9.89612 | -36.16996 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 98d550f7-c1e9-3dea-80cc-38cef2377660 | -5.81688 | -35.38757 | 2026-10-10 03:04:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5e34ea54-8346-3387-843a-eee2176a9392 | -9.88825 | -36.17451 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2385fa17-096c-3c28-95b3-637d8c45a212 | -9.89093 | -36.17273 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f7aa7a2f-4366-30d0-8f25-6b08aa4562d3 | -9.88941 | -36.16859 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e9dfd736-53db-351f-8e8a-1bae13d2dba4 | -9.89495 | -36.17592 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 46d9a624-0857-334d-beee-b3afac049dd6 | -9.89213 | -36.16685 | 2026-10-10 03:04:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b9df70c0-218a-329c-8211-b030656c2ce5 | -6.9318 | -59.2605 | 2026-10-10 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 758be16f-e6e3-363c-831b-f80caabb1fc5 | -7.535 | -45.3006 | 2026-10-10 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b3440e14-2465-3f9a-9f08-211efa720216 | -3.9911 | -59.3752 | 2026-10-10 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| fafa9799-e1aa-3ffe-8fca-4b0462f83620 | -6.4566 | -55.5008 | 2026-10-10 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 9c7dc639-42ff-37ac-9b96-a3df49c0eac2 | -3.2204 | -49.4205 | 2026-10-10 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7cc4e29a-d8b6-3de9-a8f3-2bfb19d1c3b2 | -3.9912 | -59.356 | 2026-10-10 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 08130945-5557-36b8-931f-7733585edce6 | -10.9097 | -44.8206 | 2026-10-10 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| aa45a162-6452-3866-94da-3e80522e004f | -11.0332 | -45.4246 | 2026-10-10 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 7daa083c-176e-311d-9833-396ac0304884 | -4.4025 | -49.7774 | 2026-10-10 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5b3f6a2d-3916-3d34-b6e3-a2bda1826585 | -10.8909 | -44.8001 | 2026-10-10 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3e826a82-42a0-36c7-8731-2ba47c38b484 | -7.5347 | -45.3233 | 2026-10-10 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 50c16fa3-1790-3591-9ede-591d4e07cdbc | -10.8905 | -44.8232 | 2026-10-10 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 9556539a-1f9f-300f-814c-a0023e63e257 | -3.2571 | -54.1824 | 2026-10-10 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| cfad0a42-84da-3658-a478-188facac7c7b | -3.2203 | -49.4417 | 2026-10-10 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 8ec037b7-9eb2-3502-af02-656575f68433 | 2.727 | -60.2586 | 2026-10-10 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 736472e0-3faa-3c32-8578-23a659df9341 | -3.2389 | -49.4199 | 2026-10-10 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5fe45384-846e-3d0f-ba9d-bca6c89cdd0b | -3.5676 | -54.6946 | 2026-10-10 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6ce68648-9768-3f6c-a763-c125550c110f | -9.9384 | -44.8791 | 2026-10-10 03:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1b9a7380-0743-3e1e-9587-d54e8ef08d73 | -3.2388 | -49.4411 | 2026-10-10 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a2855b21-9005-3daa-9975-78d31aa5830a | -3.6048 | -54.5936 | 2026-10-10 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3d7a954f-2abe-3720-884c-4991772aaaaf | -7.9086 | -54.7194 | 2026-10-10 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7e24285d-454c-3052-afd8-0fec21073465 | -11.0328 | -45.4475 | 2026-10-10 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b8dad2b1-8d4d-39cb-9168-2860d8c2a49b | -5.7565 | -45.1293 | 2026-10-10 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| cb123ad9-531c-35ab-a6b0-12966d0ea8f1 | -14.381 | -54.9679 | 2026-10-10 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 570a6df2-a0e4-3c10-87b1-8d09b0d4ca0d | -11.0332 | -45.4246 | 2026-10-10 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 82459695-de5c-3737-8a8f-d444dcbfd4e1 | -12.5028 | -51.2937 | 2026-10-10 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 092adb94-226f-3f95-85c3-2d27b08a5fd4 | -3.839 | -55.7997 | 2026-10-10 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7d10f368-4d69-3db8-87f9-8e2ead186200 | -6.4566 | -55.5008 | 2026-10-10 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |


[Clique aqui para ver as próximas entradas](README25.md)
