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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b337fd2-7b42-3baf-ae3b-d99ca55da449 | -6.63989 | -47.34415 | 2024-11-16 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 588ade91-6fc3-3fa2-995c-8fdea66a25c9 | -6.97993 | -38.47706 | 2024-11-16 04:25:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2b2f58b-2457-3cb4-8545-9765578090c4 | -6.16846 | -41.16108 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 233e9805-dd10-3844-b4b3-ca8db7073c96 | -0.10362 | -51.27338 | 2024-11-16 04:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55ca6f3a-d4b8-3b0c-8962-d49dcb0cb446 | -6.59554 | -39.54807 | 2024-11-16 04:25:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 14dec463-b63a-3635-b596-6cbc40a6a798 | -7.43961 | -46.93325 | 2024-11-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e021133-fc70-320f-b446-2782e9f5606b | -5.79568 | -42.53534 | 2024-11-16 04:25:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56bee839-a17c-36c5-8d1e-997420edfcd1 | 0.04645 | -49.52674 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f4a174-f6ad-3ef7-ab66-8c5e65c8b1b3 | -6.16896 | -41.15761 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8de01023-4217-39f4-afda-1a4b771c39df | -7.43906 | -46.93674 | 2024-11-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da41a331-4fdb-3fd3-9f5f-241d90b8e886 | -11.8014 | -47.06066 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 530ee04b-cc2d-3cbc-ba41-3d10fd31ef6f | -5.60133 | -43.69109 | 2024-11-16 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3933d58-0a36-39c3-9c02-17a1ee6cf44b | -11.86997 | -38.34816 | 2024-11-16 04:25:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e5a924e-e3d0-3bf1-a2fe-c51d1e640817 | -6.30157 | -39.48373 | 2024-11-16 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9cab361a-6313-31b5-a920-b7f17beaf699 | -6.02155 | -48.03872 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 23c4c62c-fe3e-370b-8562-cdedfffabf6e | -7.39622 | -40.39877 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 81160ad5-6000-3e64-a36f-67e4a5597410 | -11.80695 | -47.06879 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8fae19a-05d6-3d46-9bf5-84dde1754ffa | -5.40949 | -45.153 | 2024-11-16 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa8bb4e5-8695-3863-8e96-8249540d5645 | -6.16796 | -41.16455 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a06513fc-45e9-3726-8625-08e0a0cb60ef | -8.11527 | -44.14396 | 2024-11-16 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7a202be-bf62-3472-8fd9-b0627fcdf9e9 | 0.12559 | -49.84708 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50095eda-b564-3e17-82eb-260606873196 | -8.28459 | -45.97419 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be15ff92-fd37-305c-a2ca-f831fa0e1e8d | -0.65362 | -49.39664 | 2024-11-16 04:25:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a4a3a51-5fac-31c9-bc6b-e88bf638591b | -5.64598 | -43.30387 | 2024-11-16 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61a28b67-9078-3a24-a735-5fb69f40cffb | -8.27794 | -45.97313 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af634d1-81d2-3c51-8b35-89e2228a334f | -6.44121 | -47.86092 | 2024-11-16 04:25:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 75b09744-eefc-3355-9e1e-ce12fc681fc1 | -6.3022 | -39.47923 | 2024-11-16 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc524c72-f19b-3736-9fcc-f1271a295fb7 | -6.81414 | -46.73725 | 2024-11-16 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b3c39bc-eb6a-3085-867c-fc8c0c6a6332 | -6.02275 | -48.03125 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 465e8cf8-4014-30bd-a7bb-54f16942c0f9 | -5.90643 | -46.23348 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74a6e030-81f4-3dfa-821a-007581f9e08d | -10.6937 | -44.90961 | 2024-11-16 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f57986ec-cb49-34aa-be46-390801510eb5 | -10.54087 | -44.67787 | 2024-11-16 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0534db13-87e7-33c3-886e-e273f55465ff | -9.12171 | -44.41996 | 2024-11-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15334826-557d-3ea6-b3c5-d07a3e36b608 | -7.5838 | -39.04586 | 2024-11-16 04:25:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3c5fff5e-8d0c-331a-addb-c6d61c26c016 | -7.40263 | -41.43681 | 2024-11-16 04:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 024202aa-74c9-3bdf-a71f-3ee47d7200d8 | -6.17198 | -41.16512 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86d7954f-5e0f-35d0-8a1b-fa6c9ca63e23 | -5.55177 | -44.69383 | 2024-11-16 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40a2dc56-8d91-36c4-b57a-b6ae3d22fdb6 | -4.37726 | -50.71638 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d9df8a-1482-3307-9c3e-f8ab3e68eaa4 | -11.87526 | -38.34887 | 2024-11-16 04:25:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 690848ff-0845-39e6-8435-0d8c33048d92 | 0.15437 | -51.13732 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c7a4a2b-9d1c-3939-8c95-ad8e8b2016c2 | -6.66566 | -47.87778 | 2024-11-16 04:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b81179ad-cd3f-35f9-9a84-b680cf84e093 | -4.77781 | -48.07917 | 2024-11-16 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26a5da84-7202-3b73-9969-f2950f15baff | -7.27386 | -48.26644 | 2024-11-16 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c58fc777-fb1f-30fa-8ab8-890d217c8264 | -5.35063 | -45.57169 | 2024-11-16 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5ae2865-75ba-3a8a-9347-4e5160ad7bfc | -5.65895 | -45.19925 | 2024-11-16 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d4c9c25-8611-3ca5-8266-954af4ef0d28 | -5.52367 | -46.47222 | 2024-11-16 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be499622-c11f-34ab-8c65-693369360483 | -5.90365 | -46.22949 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a15f8f17-9aed-33b9-bab7-c807dc840950 | -6.98163 | -38.4788 | 2024-11-16 04:25:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b38768d2-5851-3fc5-a46b-03cd59882bde | -7.58314 | -39.05061 | 2024-11-16 04:25:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3df3b844-fa9a-36be-9ee1-a35419498ba1 | -5.58641 | -44.58185 | 2024-11-16 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 525dc081-03dd-3b85-8b2f-a791ee72255f | -7.26257 | -39.705 | 2024-11-16 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3fb8f5a-8761-3177-bf99-499c82a01b06 | 0.15663 | -51.13815 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f2af3eb-3d4d-3d9b-8ab5-1908540d39df | -7.45326 | -38.41257 | 2024-11-16 04:25:00 | NPP-375D | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e0193409-e888-3962-ab01-77f7d3b82336 | -5.90752 | -46.22655 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5daead2a-d74e-3924-823f-ae5842a5ee83 | -10.83617 | -44.46126 | 2024-11-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 557d5ba0-7516-31c2-90a6-4bd8bd46b68e | -10.54146 | -44.67396 | 2024-11-16 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798d2f2c-8265-31a5-8338-739f12143113 | -11.8086 | -47.0582 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27b6ebc7-4e54-322a-9286-c75cc70fce64 | -8.28792 | -45.97471 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26e51439-47b6-3d9d-9441-019e170a215b | -5.15726 | -47.93869 | 2024-11-16 04:25:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 685926de-7c67-3ca8-bd6a-20b12d4c9069 | -5.41569 | -47.56899 | 2024-11-16 04:25:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28aa1d57-04bb-3821-87bf-c69ddef90121 | -8.27461 | -45.9726 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b12ee352-c5b9-30d0-b445-ac4e9ca2f3b7 | -9.12095 | -44.4203 | 2024-11-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2c325d3-c614-31b4-95ed-f94891777357 | 0.11684 | -49.84473 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5769e492-9d01-3d2d-87b9-a34c1424d1a1 | -7.3974 | -40.39059 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92f093d6-97f9-361d-b5b5-d315b5238a73 | -4.46169 | -50.65746 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d681fa6-f384-3605-8b1f-04c76b72fed0 | -7.40328 | -41.43627 | 2024-11-16 04:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce58b986-f209-3020-91e3-4d5eed05a9c3 | -8.28514 | -45.97069 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddacf874-ec88-3813-a7a9-0bb8eea1b2d6 | -6.26893 | -44.54584 | 2024-11-16 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b19bd323-57dd-3c3e-b77d-15a5d4683691 | -5.58979 | -44.58236 | 2024-11-16 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed63ac50-b808-30a5-ac3f-0c5870337027 | -9.12035 | -44.42418 | 2024-11-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4090946-d3c1-3784-ba4d-2e1e31c04414 | -5.95286 | -44.46765 | 2024-11-16 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70fc0c8f-91d4-3ece-ae85-250ff8abd91b | -6.30607 | -39.48444 | 2024-11-16 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c33e95dc-d33b-33ee-becb-0464332b77d7 | -6.62588 | -48.99146 | 2024-11-16 04:25:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c3b1497-b58c-3a99-bcb9-029224bc3bd4 | -5.91084 | -46.22707 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fb747c2-4146-3e5f-afd9-48a1c725cd36 | -7.20574 | -47.69542 | 2024-11-16 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a6ccd57-7d9b-303c-8502-a0a5a23cbfc0 | -6.49528 | -41.57768 | 2024-11-16 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 53d2a0d0-9e8f-329f-8065-1293da97f4d6 | -6.30021 | -39.48141 | 2024-11-16 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 616dbb7e-2806-3951-b3bb-2d14b3d73d37 | -11.81082 | -47.0658 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3357c86d-45a6-32dc-85bd-febf8dbaed70 | -7.40229 | -40.38713 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37e65bf5-3361-3873-978a-40759d4e82d3 | -6.45188 | -44.37766 | 2024-11-16 04:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43278c2a-917b-307b-9d91-aa352267d704 | -5.87441 | -42.27508 | 2024-11-16 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aba628d1-6e78-337c-9518-e9e0d74c6361 | -4.38131 | -50.71703 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc814e7a-9abf-3905-b2e8-943f3f479b76 | -6.82135 | -46.77771 | 2024-11-16 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 294a46d8-d055-3d7d-ac0c-d213c6ec921e | -5.55335 | -45.2467 | 2024-11-16 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99b1018d-1a2b-3164-a822-b9e2af50ebe1 | -5.79009 | -48.1539 | 2024-11-16 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f38e61-d883-37c7-aabc-fce3aaf47377 | -6.24599 | -47.27084 | 2024-11-16 04:25:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b323860-c196-3ab4-9562-3df57abea82b | -6.82523 | -46.77474 | 2024-11-16 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edfb8e58-7c67-33b0-9ee9-ea368fa44db3 | -5.71908 | -44.81118 | 2024-11-16 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5edb4ab-f822-325e-a3be-cd3404926e20 | -10.66519 | -44.49439 | 2024-11-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 56c94274-f07a-39a5-a304-55a2bc237675 | -7.07295 | -49.29728 | 2024-11-16 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3b0d653-3a80-3aa9-9301-4ed9f9764c45 | -4.37322 | -50.71571 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 048ea0df-e8a8-3f64-9f4b-085b3d934cb8 | -5.95943 | -42.16814 | 2024-11-16 04:25:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 801b046c-5f57-3f10-997b-34cc0a8f8c3b | -6.02903 | -48.03611 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf92cbf9-53eb-3e7b-8a33-15ea3a6cf0e4 | -6.97666 | -39.98627 | 2024-11-16 04:25:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3f4ceb8-3b52-3f96-badc-f562f382a9df | 0.79501 | -50.73888 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da7596d7-89d5-3b52-bd62-c8d3a11a021f | -11.80418 | -47.06473 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01e91fd8-19dd-36af-a9c3-2243fa765426 | -5.35697 | -46.86135 | 2024-11-16 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcbaf9f3-2017-3a9b-a73b-10923de7c713 | -10.83324 | -44.45667 | 2024-11-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c066616-3530-314c-986a-0e6c3715c9bf | -5.71962 | -44.80763 | 2024-11-16 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 04d9583f-1dd0-37be-94e1-03f7ab9a1751 | -7.5589 | -35.23217 | 2024-11-16 04:25:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
