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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1f201c-9158-33b5-99f8-a702504b3f53 | -3.91197 | -49.37231 | 2026-09-30 04:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08df17e0-e5fe-362d-81de-12a2d5f0d433 | -11.2572 | -43.53854 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2772c62e-3953-3efc-949e-30cd4f90c242 | -8.94349 | -49.79644 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d02680-20f3-3c14-a76a-0404fe9a0302 | -9.15748 | -45.60182 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e777bff-80da-34aa-a232-9aa83f53c8af | -11.44101 | -43.43412 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 216e37f0-8a8c-3f7c-8495-a719b24c8eee | -4.32323 | -48.62749 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c512bb42-9a2f-3547-92bc-9b612c9186d0 | -6.16675 | -44.61939 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6010d1f9-7448-3d0e-8007-69b80c515574 | -6.15241 | -51.74446 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6a6eb18-e3a8-3738-b0e7-64d26ef05ee7 | -4.02673 | -54.20955 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b69933f-32da-30c9-840a-d44db8cb29c3 | -7.45992 | -45.79051 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a6d454c-5deb-30f5-bd13-91926471585a | -8.06089 | -48.10426 | 2026-09-30 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ae2eb9-bad5-3fa0-af56-adade3c343e9 | -11.06827 | -48.9005 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7af40879-914e-3c32-ae7f-5aa104ffa873 | -11.70549 | -43.45233 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17356974-b6f4-3fc1-86c3-6caf2bb65b0d | -3.1626 | -54.09487 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 330f51c7-ab19-386e-929a-1aa5c86d04d1 | -6.72234 | -45.57897 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2dcc45dc-c293-394e-9977-a5ac40b57635 | -7.07102 | -44.36273 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4949343-c25c-3c2f-a174-2da54db45f66 | -3.3773 | -50.8423 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3de994bb-1946-31c5-b035-c5b730093de9 | -5.09086 | -46.03842 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2111a8b-3752-3d0e-9c15-e8be2d5f288c | -5.7594 | -45.17331 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e2c4ef20-c754-3b54-ac4d-ac3106f30fb9 | -3.60895 | -49.5027 | 2026-09-30 04:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1deee492-b10e-306b-a844-2f598c072f22 | -5.73313 | -45.17369 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 120c3c6a-c068-30ba-b3b4-1d7e3d2220f8 | -3.70804 | -54.23423 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c3d42e-a561-31d1-a959-887a961c894a | -8.84219 | -49.70426 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b86e4bd-4974-38f1-8142-b101f9120421 | -3.1603 | -54.08556 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8aa98eb4-21a3-3722-8944-940015c02d12 | -5.86909 | -50.16403 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b85183f3-4340-3608-b902-acb60170c399 | -7.02909 | -44.62938 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f3bf31f-8a24-3f11-bd09-c42be325a8a7 | -11.19814 | -44.84191 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 625377fb-06c9-3644-bb6a-7e4e6dbac478 | -8.36249 | -45.42043 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f41c72ce-9537-3c3f-8744-3cdad6cfe923 | -3.51955 | -53.26274 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7adf9a92-9e2b-34f8-8520-c025d49e3b73 | -10.4185 | -53.77528 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fc66284-f972-30d2-85a6-84c90276fdb5 | -10.90102 | -43.86241 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f148f214-31cc-3f8d-9727-664c81ba2ec8 | -10.13372 | -45.13031 | 2026-09-30 04:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09a409b1-ae5f-344c-8316-bcd9e316ce90 | -10.53273 | -51.43022 | 2026-09-30 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea19a763-d16c-31c1-83b2-c291e2d2895a | -8.28224 | -50.2718 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0a59be7-72c9-32e0-b88b-0075844cfb58 | -4.81406 | -45.64597 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 743f2128-1d83-33bf-aebb-8105545b5482 | -8.25498 | -45.4494 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 664da9a7-fb0d-370b-977d-e43095b75c04 | -4.45479 | -47.92051 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52d5989d-bb30-318a-a9b6-3d7bf1f75ceb | -4.84303 | -50.68209 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 942d0b11-56bb-35eb-a837-81aef8bcb8fd | -6.32637 | -51.1618 | 2026-09-30 04:53:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf57718-8a0a-3e97-9e7b-97cf850743e7 | -11.19539 | -45.11734 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4648ef59-638e-3038-ba6b-33826299d656 | -17.90801 | -45.05145 | 2026-09-30 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1d40c246-90db-39fb-8a64-0a2c52ce6ab0 | -11.39553 | -47.43805 | 2026-09-30 04:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b5e156-133f-3332-822c-35652cd919c1 | -16.35544 | -42.58966 | 2026-09-30 04:53:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e531c27-2ae1-3b86-b780-e400fdb51bc8 | -10.51498 | -50.8458 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c729316a-b11d-389a-9919-e895f82b978b | -7.13688 | -49.18033 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e2dff4-b536-3d18-a9ef-9073be7e21b9 | -10.81318 | -48.73069 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e89be41-ec79-359b-beef-03073d801879 | -4.0295 | -54.19839 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73e6b88e-1f25-3aad-bb01-b1da14bf1734 | -11.16296 | -44.77151 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bfa38e9-02d7-3bed-a841-0cedb1823df6 | -11.43934 | -43.44704 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32dccfda-c7b3-3ce1-99bd-454bcbe36398 | -6.75204 | -55.08975 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd4607a-35a3-3eb4-88c0-7ddbbdd16831 | -11.19729 | -44.83941 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f0b66085-4524-3e2c-b32e-2bdddf07370b | -3.14991 | -54.07939 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdd38b4f-cb33-3b98-b0e8-ca0ab5587433 | -6.12829 | -53.30069 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f54b47fa-000c-33de-8f47-3645c8bd67f5 | -5.72527 | -43.28226 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 143f99f2-8f7d-3846-b18b-ac269238cd3f | -10.56113 | -50.87148 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 683dc9d7-6e9a-313c-9d75-173c8bea5719 | -6.13985 | -53.2671 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be493fe-313e-3f80-853f-e3b03f00dc41 | -7.47728 | -45.7893 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9307cb4f-84f4-3094-84a1-13183940189a | -11.17569 | -44.82066 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fddf04d0-0747-371f-9b0f-d1cabb4dd0f9 | -9.77021 | -44.81992 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 893756ce-abc6-3e57-92fa-6c4e934c2f93 | -7.81733 | -45.82426 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fec80a4-b1d4-3432-8c92-2abce6141a9a | -4.84579 | -50.68606 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c70f4f-e51e-38dd-b39c-002c6f11a27e | -5.72231 | -53.46456 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ff91b3d-e261-3845-94a0-a4bc6ece6225 | -6.38254 | -52.91821 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d78105-8396-31a3-ab03-1a2c30f52b0e | -3.72129 | -54.2229 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3b334c-531b-3015-b6b5-913ad05c15df | -2.89223 | -54.09517 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0444e3da-44af-3379-a2de-3e22a8c6103e | -9.16518 | -60.79317 | 2026-09-30 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 322ef3e7-b1af-335a-b7cb-f1172ce6076c | -3.38072 | -50.94881 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e619d583-33e9-30f9-8a22-484e17e65ef3 | -6.1238 | -53.28465 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c2d3d2-90e4-352f-8080-c34cfb87fd75 | -3.01317 | -54.23103 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a1c800a-2b83-3478-952a-bffe966d9c11 | -10.72595 | -44.42702 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8b6341a-f2ac-3ecb-8f5a-89d52cde56a3 | -7.45573 | -45.78981 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bbaa51e-76c2-3d40-97ee-6d5cca3f3e23 | -5.62778 | -51.94357 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a51d56-ffcb-3d33-a02c-1ce76c32d9bf | -3.56147 | -50.25762 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6849941-04b3-3df8-8116-f4e109d75485 | -9.69234 | -47.65417 | 2026-09-30 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 597ff3bf-b6af-32a3-a18d-97c178c6258c | -9.10153 | -47.17815 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fea8712b-933e-3306-bef2-180d79e5d0c6 | -15.63537 | -43.23454 | 2026-09-30 04:53:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bb4ecb4a-b5e1-329b-abe5-2068d184d110 | -5.03091 | -43.57259 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b8fd92a-38bb-3157-be82-dd2612ceb380 | -8.32118 | -54.76309 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66d0c8b5-2a6e-343f-85f9-7f72eddd2c9d | -11.16772 | -44.77216 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce35bc1f-958d-3bfe-9776-d418e2ab4a56 | -14.50576 | -48.28863 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61c79d9a-d9cf-3f92-807f-36cd141ad7f3 | -7.496 | -55.03278 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5065d739-22c5-3712-bd3c-e5890e0e1ebc | -8.94692 | -49.79697 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abec2ef5-9f3b-323a-a62d-eee8ca6d927d | -10.81381 | -48.72639 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93271e58-96f5-3737-8ce6-cc2f1e0107ac | -8.31759 | -54.76247 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c725481-c48c-310f-ac60-f8d7857d4fef | -10.78209 | -47.25408 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290e272a-4547-3948-89f5-34274a97703b | -4.02376 | -54.20468 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e531de96-c843-3275-9c9f-9038e55074cf | -14.89662 | -51.86479 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d8ac1ca-82ac-34d1-ae65-3dc5914955b5 | -9.76279 | -54.28676 | 2026-09-30 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d81580f-c79e-3141-93c3-1d9f39ad24f6 | -7.50442 | -45.80903 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6b2b3c1-eef9-3959-8449-05b09e554d4f | -6.28317 | -43.64046 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fed6e094-653d-3d4d-8c29-b847a5ec51d8 | -17.78877 | -47.17109 | 2026-09-30 04:53:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 803c00dd-8285-3327-8d51-dd317830719e | -8.27888 | -50.27128 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3fc6fbe-5761-37c1-832b-51e0e4edf22b | -6.12484 | -53.30018 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81ea0b4e-81f9-3c43-8a71-e9423a20d9e2 | -3.37675 | -50.84574 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 058c6ef6-a9ab-3ddd-98c0-d5eb8ce0a455 | -7.84829 | -45.82092 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d4a3fa8-9dec-38a7-ac8e-da6433df4bfb | -7.81312 | -45.82364 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91e6e73e-23a9-3994-997a-110246ec5a46 | -5.02725 | -43.57392 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 923f7266-a9a3-3e9d-a101-cbf554729e3b | -8.94522 | -49.78516 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d4484f7-1a47-3d4b-aaf4-e683617aede6 | -6.1289 | -53.29689 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2155c33f-6668-391e-9ce6-b02dbb961696 | -7.55566 | -55.03812 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README49.md)
