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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cc82fc5-31bb-306c-8177-c81e5134acce | -11.99938 | -47.04023 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9de695a0-dca5-36e5-8b2d-42201665355f | -7.81333 | -47.00916 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d4210053-40cd-3803-accd-589003a5275c | -7.74661 | -47.02357 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91426041-7334-3514-9ce6-4ea90690bd35 | -12.68273 | -46.88121 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9885d550-c050-3e71-ab9e-5487f6892d14 | -5.88022 | -43.20316 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 643f1e38-6760-3542-946f-8d759057c266 | -8.65208 | -43.98952 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0def640e-900b-388f-a1a4-f56607abf9d3 | -12.00779 | -47.97626 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0086e51-16a3-3bdf-8672-45a6704da09a | -11.99993 | -47.03671 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da9848db-e309-32c3-9a6e-904357c95bd3 | -8.10398 | -49.08673 | 2025-09-28 04:25:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59e877d4-b9bb-38cb-aa55-7530cb3962f4 | -11.25751 | -48.37843 | 2025-09-28 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec623d2b-9da7-36d2-825d-5a4c0f60b1cc | -9.04447 | -46.72113 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42176f6a-9455-3547-9490-ff586a15f9e1 | -10.51264 | -51.94578 | 2025-09-28 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d049893-b750-3537-bb8b-ea88e39aff5f | -6.69298 | -44.57748 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79d0c4b2-1b6c-32ed-9f60-c4d21449ba69 | -12.92777 | -45.15868 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a666090b-1fb3-3070-9403-58cfa4fb7faa | -5.3983 | -45.84841 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fef5761c-7c23-3103-86dc-bb4c0d86541f | -5.48359 | -45.10826 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6697fc83-594b-3de0-96ab-8d1f1a3d5095 | -11.4251 | -44.91692 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33ed57e1-0fd7-3d2b-ad1c-126edd4870a8 | -11.42449 | -44.92095 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 000fa3c3-2fea-3f9e-a648-731a760f83d4 | -7.81702 | -45.14528 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 317da13d-e1ac-378c-807b-b8e5d2ab18ba | -11.04822 | -45.88235 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 000a635d-708b-3464-b81d-6df7f4b94cce | -12.00447 | -47.97571 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bca17d4-6bf3-37af-9f6b-14076ae0b460 | -7.75435 | -45.74567 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6535a4e-e7a4-3b37-91e7-19f649905530 | -8.47458 | -47.80481 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 505fe1a5-d940-3742-a5e7-dd4e774b802c | -12.89802 | -45.16629 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 895bd4e9-9619-3b89-85f5-5b4f18d1cb12 | -10.18255 | -44.83385 | 2025-09-28 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba8fc1eb-fe4c-3efe-9423-1fe08a8c2888 | -6.3878 | -42.94951 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b2c5e345-41bb-3211-86e7-f6a95415807c | -11.64876 | -48.26653 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59264db2-44f7-3009-9da8-311dae986e57 | -6.70879 | -44.58759 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f37d7b74-340f-34ba-bd0b-56a3289138fb | -11.78119 | -43.76361 | 2025-09-28 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32d6e928-e71b-32b1-b6e6-f5cab7e85b23 | -7.80725 | -47.00462 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ce3daee-caaf-3fe4-9b90-fae2735cc24f | -5.88036 | -43.1976 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 10ea36d9-8db9-3085-838e-61174e36e182 | -9.40654 | -54.69651 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff914232-9373-33e4-875b-71021f044aa5 | -9.04171 | -46.71712 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82c2d98c-3a0c-330f-accd-3305d3f9c4dd | -11.98839 | -47.99117 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c996edca-6e89-35e0-ab50-1d998d7bf50e | -10.99605 | -57.06558 | 2025-09-28 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c74a4dde-5b09-3730-baa3-5ec8adf5f9ef | -12.53385 | -48.29948 | 2025-09-28 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9671b25-fcc6-392f-87b8-814df1298ce5 | -11.44869 | -44.99674 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 88662e11-c0e9-3f56-8ec3-c67a34a5476f | -5.82447 | -44.4421 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4150f98a-89f5-3464-ace3-0535be81abcd | -6.08324 | -46.50165 | 2025-09-28 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd63767d-fd35-3c07-bd0b-930165850815 | -10.90241 | -45.7552 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2af15db4-784c-3898-b4fa-210c2330f659 | -12.926 | -45.17057 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d9a4868-9b8b-3feb-99da-e3af5288a6ca | -6.15321 | -43.87487 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb0c5b0-b38d-3e9b-8056-4bab22e6e2a3 | -10.90523 | -45.75936 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b00995c-c8ef-3855-9285-4d162a2f90f3 | -9.05699 | -51.6831 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd90d0f1-17c6-3811-820b-fcf9fcf4e14d | -6.45653 | -44.02052 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e831e4e-283e-37c8-aaea-5a3cd5cccdae | -10.12811 | -45.3296 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbdb0fa7-cd87-379e-90f7-4eee6f61f4a3 | -11.99811 | -47.88774 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66a38b91-8a89-3ed3-ba5f-cc573dad464f | -6.31822 | -45.89422 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ad2e83-791f-36e3-af29-45760bf35b6b | -5.82786 | -44.44264 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d80a91f4-e2f6-3c18-b4d1-74f42de82317 | -6.15779 | -44.16483 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ffa8997-3aac-31d8-a5f1-52329b28208b | -11.715 | -44.4236 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d79aa4d-20df-3b40-9042-73109746d5f2 | -6.82462 | -44.19814 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d2c469b-ca9d-3bcd-9166-c0cfb77a2063 | -6.27022 | -42.49115 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb9ab018-1d32-37f3-a7d8-dc3eb1dd5fba | -9.67636 | -44.52715 | 2025-09-28 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55565735-2838-3956-9a6e-9f5b28dc5a45 | -10.00485 | -46.70337 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f759f72f-f676-3ebb-84c6-cd10505a2c0d | -12.89685 | -45.17421 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 29d4ffe5-defe-3dc9-9f13-e6bf923fff2a | -7.53946 | -46.09789 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71586af1-7cee-38a4-90d9-c730523121eb | -10.91622 | -45.7424 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7a4623b-a3a3-3111-9140-fff2012305b7 | -12.41777 | -44.11028 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede2c108-3598-3a76-b171-02fc092215f4 | -11.9867 | -47.8752 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63b14669-01e7-3c55-a577-b9cd6357c89e | -11.9407 | -47.92919 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22b9b28a-fb86-3211-8be5-ab3df1599996 | -7.02498 | -44.76208 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aecab721-a283-34c6-9ac7-737a70562070 | -12.69446 | -45.47511 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1fd20edc-9501-356c-9102-8af519e9b44a | -8.29115 | -45.45619 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99ed9d61-181b-3dfa-ba31-fe5f7d1d2acc | -7.17978 | -41.71644 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6737c5d-b984-3600-8977-f6ab9ea1afb2 | -11.97674 | -47.07633 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95e670c7-734e-35de-a78d-bda680fc2c2a | -11.39221 | -46.97182 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22a8e2ff-81ba-3409-a89c-f234567ff45e | -11.6518 | -45.33979 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a55bebf-e965-360b-ad30-bcc2530939af | -10.03707 | -52.08733 | 2025-09-28 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cd764ab-8300-3d7f-b3e4-8829c5166bb5 | -11.97619 | -47.07985 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6112abf-93d3-3a6b-a7d8-ad7d402c4fa5 | -9.45211 | -50.90244 | 2025-09-28 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b782a7-f8c3-39a9-aa3c-074dccbc292b | -6.17897 | -42.94616 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 75d40c88-a34d-3f3a-8f2f-46cb9f4f40c2 | -10.79122 | -49.58523 | 2025-09-28 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 817e193e-a29b-3cac-84cb-20f375325d84 | -10.72016 | -47.99719 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a2db84-df31-3cf3-af1a-dca0ea376f43 | -11.98669 | -48.00178 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e2c18e0-06a7-3061-a135-72cdd040c2e1 | -10.91422 | -45.74582 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bde5994-c225-3590-aaa2-fa2bdb691165 | -11.57942 | -45.49531 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f01e9c-391e-369f-b62f-dbac72acdef6 | -7.25013 | -44.75543 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04949a39-d432-3b49-b930-9a0f9edeff48 | -8.17166 | -46.41823 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fc43101-5f3e-3b40-99e7-aba10a6e39d1 | -11.35893 | -44.95485 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33e43e47-bbae-37eb-99f2-ca1f8b370d54 | -9.7548 | -46.13086 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11697d49-716d-3f2e-8d81-5a93879184f8 | -11.3878 | -46.97831 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e408f1ca-c29e-3306-af3e-4f0778a79fb9 | -12.00546 | -47.04482 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02e45107-e23a-3431-93a3-8b774d5e04cb | -12.89511 | -45.16179 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 119edf7c-92f0-3645-a3ec-5d5eefae3c1e | -6.76127 | -44.59128 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38650a1e-df8c-3283-b185-0760cc35bd4e | -7.50048 | -45.41063 | 2025-09-28 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc06347b-9d3a-303f-a0a2-65bcae36a441 | -8.48348 | -47.81353 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77c96f70-2a97-3524-ac82-4898a6240789 | -11.95351 | -47.89148 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87b1f176-a345-362b-b900-c9da8dedc089 | -12.89013 | -47.09623 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e9b16d-1430-3465-a32e-54cb7650d48d | -12.01956 | -47.92387 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58d2f455-59aa-3dd8-9900-acbe62c7ed82 | -7.50195 | -44.30289 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43511041-c476-3b86-9f6a-7ca85587f373 | -5.95969 | -43.76803 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6fe7f9a-7e0c-3638-8be6-adc915143959 | -5.94859 | -42.71367 | 2025-09-28 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d3dc17c-3e07-309d-aefb-f32382af27b9 | -9.10204 | -45.83002 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52590fe8-3f85-329e-bbfe-ba9b8cbee03e | -7.03173 | -44.76318 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c4d2b00-8b46-387b-b2a9-30195b460c82 | -11.42432 | -45.04055 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0801487f-651d-3096-8359-361194b01a86 | -8.6739 | -43.98863 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af66231b-3d8e-31b8-b816-d45ecaa2b246 | -9.04624 | -45.51107 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606b9491-020c-3b7f-8f37-ebcbccfd6e37 | -7.37868 | -47.02912 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa0898ec-30a7-389b-a997-227620a14650 | -9.41406 | -54.68999 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README69.md)
