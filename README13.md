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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7633336-d886-3c32-92ef-bd2978b45c78 | -5.7515 | -45.16634 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f42b35c-b82f-363a-b84a-47a00df34a41 | -11.71213 | -43.44667 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 103c4ee3-9248-3631-a141-dc3bd1e6463a | -6.33353 | -51.15701 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c46596b-9c62-37df-9139-de3aea9b47c1 | -9.0144 | -40.99995 | 2026-09-30 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50d9c619-7fc7-3ce4-9c95-24e4ec37c173 | -8.84088 | -49.70485 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 31bcc00c-aa15-35e7-b8ed-6c111520954f | -7.46111 | -45.79141 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6776062-2025-36d0-9126-9abdb01cdef4 | -5.74092 | -45.17405 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5939397-f9eb-35f9-9c76-055428be4bf2 | -9.32418 | -46.41838 | 2026-09-30 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bd2fea66-5697-3e7e-b887-9c24512dfa4d | -4.80703 | -49.46728 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9872e4d4-db25-3de4-adde-0038b0f4148e | -9.06824 | -49.86635 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f43f97a0-e7a2-3ca9-a888-68f65911dca2 | -9.93027 | -50.16065 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a7e5f2dd-3404-3736-84bb-4f9f5493d57c | -10.82888 | -48.7009 | 2026-09-30 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 101cc563-00dc-3386-b927-950c920f432a | -10.70035 | -44.43901 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61d6d15f-dd2b-3c03-8aa9-d0019356f45e | -5.73085 | -43.50519 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7fb51bc-eb75-3e04-afff-2ae867022128 | -8.32664 | -44.16221 | 2026-09-30 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 862308b7-9978-3f4d-9dc1-ac4a9f231d1e | -9.10285 | -47.16497 | 2026-09-30 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2c7dae0f-399c-3349-9636-d8c5aad4ee26 | -10.83918 | -48.70395 | 2026-09-30 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47bf770f-5fb8-34ae-a1dc-d23cb1bb6a2b | -11.1957 | -45.1242 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 077a1cb8-72c7-38e6-9f0b-c5a86553b8c2 | -7.06765 | -46.57276 | 2026-09-30 03:55:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d03c7e-0832-306f-8356-a09659d8deb1 | -8.84011 | -49.70899 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 378785d5-4348-36d1-8c15-05c6c84951dc | -6.16439 | -44.61827 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4ed8fd0-7989-35ad-bc2c-74dd91552f85 | -7.84713 | -45.82529 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 0855c4dc-9248-3898-8c1c-ee8db137c4a4 | -7.84255 | -45.8246 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c717b598-4b66-3143-a850-ac2f71037141 | -9.10091 | -47.17594 | 2026-09-30 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b3e52ad-c1bb-36c6-915a-14526f0c7800 | -9.84648 | -38.92739 | 2026-09-30 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7841585-e3d5-3464-919f-e329e55d5b39 | -9.67755 | -46.71088 | 2026-09-30 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d4ecb4c-7815-3e1c-a115-77cfdfc7b7d4 | -11.42808 | -43.43278 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0f3a884-1286-30ca-9f0f-2adf1e0be523 | -5.27273 | -42.63527 | 2026-09-30 03:55:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ac10c0-f2b7-3725-b194-5e4702501e89 | -9.78003 | -44.81157 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fffef3f-a381-3672-90a1-e68fbb17eb33 | -6.86299 | -40.93978 | 2026-09-30 03:55:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bd4e1bb-0848-39bd-9d2f-79fd16252451 | -7.84639 | -45.82616 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dd6e7a76-ecbb-359e-9dc7-bc39aa9b9d94 | -11.39455 | -43.39203 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2659794-3c29-3695-9611-f0090f536f27 | -10.77602 | -47.71772 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a560a1cc-5267-364c-9d50-77bc9b110981 | -7.02754 | -44.62561 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dfb739a-d3b2-3e08-9e45-8ebed9440b96 | -10.18805 | -39.66329 | 2026-09-30 03:55:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 141ea398-c960-3f18-9dd5-d7181c1b4802 | -9.09991 | -47.18156 | 2026-09-30 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c25e330b-91c3-3a2d-b217-c7ee0f2133dc | -11.16937 | -44.76778 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0f2d942-27d6-37a5-93bf-d988c969a698 | -11.1769 | -44.82087 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f7508b77-c794-343c-bc64-4946e6a6cccb | -5.09342 | -46.03875 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d8003bf-998e-37da-ab1e-cf7c6b082a81 | -10.70812 | -47.82918 | 2026-09-30 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79da5063-0963-305a-8542-6ec70c7d53a4 | -5.74135 | -45.06192 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2be9cdba-850e-3835-8ba9-518440cec31a | -7.0804 | -41.74926 | 2026-09-30 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f8a48ca-0eda-3b24-b15e-173034b2af62 | -4.45523 | -47.92356 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9cd32d7b-e4d3-3804-afe4-c8cfaa94868f | -7.20171 | -40.12199 | 2026-09-30 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d803fa07-f984-342c-9601-27dc95d1df9a | -10.77 | -47.72263 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 00ab2aaf-f420-36ef-aeff-da34350e348b | -11.1211 | -45.91572 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9d24b3c2-280d-3192-8715-3ba55779a111 | -11.70919 | -43.44157 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 168da2ca-a29b-3bba-afcd-ec27ff898e6e | -10.70245 | -44.45033 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb9438e-cdba-3afd-94ab-74484bef5880 | -8.83431 | -49.7079 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c0a69127-3606-32da-96fa-d11519ba8cc7 | -7.84181 | -45.82548 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 16481270-319a-32b1-b4b7-2ed756fe05f4 | -5.81834 | -46.22358 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e78fc82b-eca1-37f7-92db-1d27cb7b2f25 | -9.93191 | -50.15209 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3573ca3c-2609-3e6f-9ddf-9333b4d31274 | -7.83266 | -45.82405 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bb3d9402-f176-3393-a212-5768440a7c7a | -10.82825 | -48.70426 | 2026-09-30 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcae1bd1-328d-324c-b26f-d255169da562 | -6.7102 | -45.99288 | 2026-09-30 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0efc225d-205e-3edb-a9ca-35a8d437f73c | -5.71526 | -46.19265 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a84e1b6-9068-3b91-8c6e-744b68738a78 | -11.38646 | -43.37231 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49a8297d-f50e-3531-9e62-4301eadb7fd1 | -11.16876 | -44.77134 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497fb427-6d84-367f-99fe-63025145a8e1 | -7.04283 | -41.5558 | 2026-09-30 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ea7609c-4fd2-3e83-a21e-d1bf67e9297e | -9.96823 | -47.98421 | 2026-09-30 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1da83de-e335-3f51-a4da-628216e5390d | -4.81552 | -45.63766 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ecdf6659-ec3d-37a9-bc60-dd19913e2991 | -11.41852 | -43.42194 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 30627e6a-fe84-39bb-b275-3f9dc2299733 | -7.83723 | -45.8248 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2361201f-e5a6-3627-b3db-12d4a82471ff | -7.38632 | -47.01133 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1449289-9a0b-3c67-8608-882002b6c417 | -11.66915 | -44.51 | 2026-09-30 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88825c97-592f-330f-8f8e-a3edb380f9df | -4.45585 | -47.91983 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| feeecfb0-2b04-3166-8cab-532225c63aba | -11.42222 | -43.42258 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dcc6a37-46f6-31ea-bff9-ce640fc10265 | -7.07973 | -41.75335 | 2026-09-30 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d2beffe-6720-394d-9cc5-bd32299591c3 | -11.40034 | -43.47129 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7ece7feb-403f-3a85-b11b-5e457c0545c9 | -11.63493 | -42.92519 | 2026-09-30 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aeb5677d-8e07-330f-9edd-7ef9760f4d70 | -11.3592 | -43.35389 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 633e4441-2103-3d2d-a148-ef3aeadfc81b | -11.43472 | -43.43853 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e85d9ca-cd3f-3972-99eb-d4f4a78c590c | -11.62307 | -43.50034 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba5f3cb5-10e6-338f-8bcd-231c4c5dee8e | -5.71617 | -46.1963 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0b1b9c4-3c14-361c-8c9d-75e928fcc3df | -8.97676 | -44.17648 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be628e5b-577f-3728-9466-76ae5af52a9d | -11.44136 | -43.44426 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b87c15c-15a9-3447-87d4-d931182c52ca | -9.76319 | -44.82002 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75556736-513c-3ddb-a864-3d939bd7d4f2 | -3.381 | -50.95423 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 29b1df7b-1e87-3ef5-b5a8-ae3e1857349d | -8.36747 | -45.39402 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133232bb-4eaa-3d1b-b845-ef6753f95c58 | -10.65394 | -40.2887 | 2026-09-30 03:55:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a049500-9ca1-38fc-b4e5-e3d58435cf16 | -10.77104 | -47.71713 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cd0a0e10-956b-36f9-a62f-41a68f5a901c | -10.77361 | -47.25318 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 59073d3d-6587-3657-8a54-8b7cffd4b29b | -11.17286 | -44.82014 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 94b9cf3d-ab02-3513-81b3-e3ac03ab51ac | -6.3041 | -46.06313 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87d4592a-5f49-3dcc-9251-d593ea49177d | -11.70844 | -43.44603 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4f58db8-dff0-3453-b259-38037f171b7d | -11.41221 | -43.48074 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dafc616-fd90-35e6-a49a-2ded80fb1e6d | -6.71018 | -45.63137 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f462e8ce-94fc-3c50-b71b-470e16c981ab | -10.71939 | -44.42366 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 82e7054d-3f2e-3a13-9317-917eb65f426d | -7.27219 | -44.3121 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf93871-5617-37ad-9e14-6a301a508b1b | -11.704 | -43.44984 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 80812920-4a5c-300c-aa42-11c9f71796ce | -11.70625 | -43.43648 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d4a0dc-9752-3109-be2d-9ca076a78eee | -7.38581 | -47.01426 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ba8ffea-7048-310a-983e-6b0d0c0a417a | -6.52821 | -47.11846 | 2026-09-30 03:55:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6713336e-6908-3d50-94ec-577f7bae2772 | -10.15319 | -36.2428 | 2026-09-30 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 7592dfec-c139-396b-82a5-d6449e7ca77d | -7.0761 | -44.36331 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7e80f06-8a86-3866-ae12-262a33e811a7 | -11.39367 | -43.46552 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10b674b1-571b-384e-ab62-92662b9cd588 | -10.69779 | -44.43828 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99e0d9fb-35cc-313d-943d-5c5cee227a1a | -11.40561 | -43.41686 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c5e3e74-e240-3186-8a07-53f389752130 | -8.25508 | -45.43995 | 2026-09-30 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7286a264-70bc-394d-8764-dfcf71c99e01 | -12.25483 | -43.48189 | 2026-09-30 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
