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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ddca66c-5093-3a48-92c6-ef24b1bd20a6 | -7.61551 | -45.26131 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5093e2b-4d12-3785-93b6-a4e9a4d99c5a | -6.34094 | -43.42207 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3066d89-7bda-37fa-810f-04759a39a325 | -8.49906 | -44.74024 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55537cfc-4495-3706-940e-fcc03aa3be7c | -5.46215 | -46.47137 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cbf858d-15f4-37be-904b-160d8bcac83b | -7.22773 | -45.17827 | 2025-08-22 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4abf223-f521-3c4b-9e53-afc594b9fdab | -5.34485 | -45.22742 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 323d271b-0bc6-3098-a53a-1d67089356c0 | -5.88358 | -53.63309 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55160c22-cb73-380c-9c64-3f876b909b39 | -6.51012 | -45.5269 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aae7aa8d-f366-32e1-8408-02f568162667 | -11.63558 | -51.61404 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 051c652e-b82e-3c76-8fa3-6d6445f70d70 | -5.88058 | -53.61922 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6953adee-5a10-3f9e-b8aa-9dad982a5e78 | -9.69437 | -47.92831 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90aa61a0-0e79-3a2c-9ddd-05917eba658c | -6.43638 | -44.51006 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dff36ed-32f7-3076-bd12-7b195c8bc4d1 | -5.79158 | -45.06678 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8bb195-8032-3e98-8411-0b1b6dd1fea0 | -9.81608 | -49.81002 | 2025-08-22 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06d4b763-41b5-32e6-a60c-c08a2b34d02e | -7.02582 | -44.6281 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e20efcad-63a5-3a90-9c52-e62bbde5ba04 | -6.71053 | -43.20472 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2305ddc-d200-3384-b1b3-27494e48610f | -6.08486 | -44.1317 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ef1363f-a3ca-3130-a2bb-0076741073ff | -6.93751 | -44.39018 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16609da3-f050-34b6-9fe9-22449d8b0b26 | -11.00378 | -45.63602 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a0607a8-cc2f-31e5-8274-0e149fec4cde | -4.83182 | -55.77134 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3afe7df1-f8a0-36b3-b156-b2f3af2fabdd | -5.79434 | -45.07077 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| da6395ff-ceb8-3faf-a338-17b12deab18e | -7.46106 | -44.45163 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa480de-1904-3f95-a24d-6a0b95070984 | -6.28464 | -43.87387 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10658f5c-e67e-3f7b-a2b6-5ea8a1da3f79 | -10.96702 | -49.56817 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c7db35e-d32f-31dc-8714-f5f3f1cb0a54 | -6.0379 | -44.36577 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b31bb2f-ba20-36f1-ad0f-e0e2b3784fad | -8.79606 | -45.42176 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dd4de1b-5fa8-3f99-bb59-c164df6a62ad | -10.86828 | -50.84837 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96c29e77-4add-3004-9503-dc33de02da33 | -6.04248 | -44.44442 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a050f35-81e4-3313-8e1e-c3bb24c36b61 | -6.49648 | -43.11708 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a739c6a-4aa9-3f14-906f-8f80a9ec6b3e | -6.41801 | -45.48726 | 2025-08-22 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39bc4555-efa5-31de-884e-fea7a14a8865 | -6.29138 | -43.69851 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3409e705-612a-3a0b-a0a3-dd036072a4a9 | -11.30981 | -44.95518 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50085be3-8814-3522-818c-41aa060f982f | -7.84906 | -46.9815 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d27b79f-b104-338f-a490-2d8a60ab74e7 | -11.08842 | -44.81123 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 985a9124-90d7-3237-9f78-27a01d8e92dc | -7.16953 | -44.44828 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec681b92-bb76-3b99-8441-9767c9cb8d5d | -6.43751 | -44.52441 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad2bfbbd-2f72-3cac-82ae-36a1b112e049 | -11.44355 | -47.31072 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3da342f-2b1d-387c-a774-2cf00ba541d1 | -9.31528 | -40.22635 | 2025-08-22 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc78a5e2-2a82-314f-a235-65f99abed807 | -10.26772 | -46.75866 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d52b0645-a238-3c03-b5c3-ab83a95287ca | -6.29137 | -43.89634 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf89f4db-dc3b-3207-9da9-ae4846b8a1f6 | -6.44953 | -53.39083 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb3ad48a-1d71-3dd7-a798-a8de09e02542 | -7.02859 | -44.63208 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a7601a3-88d5-3a3b-ac32-5865204fa105 | -6.29416 | -43.90034 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 651c00aa-476b-3c94-b534-19af6cbbca46 | -5.87306 | -53.63126 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f0e3c5b-06e6-37fa-a1dd-e99c07df2d8c | -6.28144 | -43.71852 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4344995-ab3b-3a65-a53f-b3571423d39b | -7.81778 | -46.87009 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d7166f-c47c-37ae-847a-876f2e7e86ab | -6.70816 | -51.41796 | 2025-08-22 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5c1b980-55ef-3db0-b12f-7458d331f07b | -7.95771 | -42.63897 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 67181af1-2724-3dba-8f32-ab44a97e670e | -6.54754 | -45.52593 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22ad4ab3-b7df-3958-ab17-b7273e2a1312 | -6.55763 | -42.99107 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24db7ad-e170-3139-be78-2c2fae2a7754 | -11.4396 | -47.31379 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8ad96d6-ec73-3033-abd4-0d46e8d5156b | -12.60438 | -47.08406 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 075d3ba7-4ad9-39b7-b0ba-db4cb7ce02a3 | -7.16837 | -44.67214 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a424494-d275-3a80-9a74-5cd9a1219328 | -4.32489 | -55.13778 | 2025-08-22 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94c72127-5c97-3502-80bd-6d25544481fa | -6.0207 | -42.81622 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a19f3489-8173-34f2-b11e-18cba0a8afef | -11.81091 | -44.25865 | 2025-08-22 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e79c30e2-aa29-3241-8c80-236f9b265c55 | -5.86479 | -45.67277 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c06c74a-bbd5-3f21-968c-386a837c7f59 | -6.94509 | -44.55857 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc0cf0c1-6ea8-3d8e-a464-96d039fca4db | -6.02756 | -42.83976 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3873c11-9075-3f8a-be99-2cff63d1ab23 | -7.60113 | -44.38039 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f3f0649-2cd7-30a5-848b-54d811485494 | -10.8603 | -45.20709 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42752f81-0a41-3da0-a5a0-2ee3f530cf4b | -7.84564 | -46.98097 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47302e5-9f90-3eb8-b38a-41282c7f9087 | -7.03575 | -44.62964 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bf53515-ee03-36d4-9112-29f9888dc330 | -7.64843 | -46.24789 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 453e96f5-dad6-31c2-9ad5-90c7fea02d17 | -7.95364 | -42.63532 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4eaa5bb4-7dae-3017-96b2-4bd85adba8ff | -10.28786 | -46.76154 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8f1add3-5b76-370c-8ff5-6b16323fbcea | -6.93942 | -44.29097 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b65df1b5-1866-3b0e-b6d8-cc1e1dc4fe0f | -7.51581 | -44.96851 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b01df1ab-0fbc-38a9-a517-c7821b988d2d | -6.0423 | -44.35937 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60278263-9448-36ca-9c5c-065531483dd9 | -0.75132 | -47.75298 | 2025-08-22 04:19:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cf66c9a-7b1c-3c6e-8301-9853fec1eb88 | -0.74916 | -47.75532 | 2025-08-22 04:19:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bf67150-6c26-3a88-807c-5fe128455e55 | -6.05137 | -43.99822 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70c0139a-ed27-312f-9fb2-d5cbbda36597 | -10.28567 | -46.75386 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a01224d-baf6-3ca9-a56b-d8a46f080059 | -9.13844 | -46.38546 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 98f6141e-ecea-3db7-aa66-5036d4285052 | -8.78565 | -46.72133 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adaeca89-3282-350e-9351-6e869b2bc804 | -7.02528 | -44.63157 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a91e2fe-d1d4-376c-a4d9-05d0847bd48e | -6.42133 | -45.48779 | 2025-08-22 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86dd8a11-a27f-3c48-97be-872ba1126034 | -8.30057 | -46.96621 | 2025-08-22 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1bb775da-ce07-3103-8eb9-debbe29a6799 | -5.87774 | -53.63548 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a337de29-40bb-3659-a420-a27bd62dbd29 | -6.51801 | -45.88158 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dbb8ded-5ca2-33ee-b15c-662fecbd711d | -6.29857 | -43.89391 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ffac2b2-b856-3712-8697-567894b5211a | -3.7377 | -53.9803 | 2025-08-22 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f31fe352-2002-33a9-91d2-a49919374b2c | -5.39769 | -45.15025 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c237564-fe64-3b09-8ead-237bd24d76e3 | -8.51508 | -48.82412 | 2025-08-22 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f92bf85-7c47-3285-bc8d-a1d9a7d2c03a | -6.07105 | -44.13312 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3441e171-5c22-371a-ae13-5500f68b6aaa | -6.53557 | -45.45218 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a6f5c9b-3984-35fd-bb1f-c0b8be211d56 | -7.87177 | -46.99284 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb022246-5eb1-37ea-9775-26d587efa5e4 | -10.67428 | -51.56675 | 2025-08-22 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0266f5b-5777-38cf-b92a-f67f5e38cf21 | -5.87299 | -42.41016 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2593410f-4ae7-3c85-8d85-d4ea78af7836 | -7.28382 | -49.29058 | 2025-08-22 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27c0a501-f03f-3395-83cb-6f7a69f9983a | -11.31534 | -44.94144 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 033b4109-7b80-3c63-9050-8cc53a4e6d90 | -7.84671 | -45.1954 | 2025-08-22 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5337cf38-0695-3c87-aea6-a017dbdc5404 | -7.15844 | -44.67058 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8757ba8-840e-3cce-8fe2-c32327a55eea | -6.03041 | -42.84393 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d68b01bd-8e06-382d-b57e-dc3ccc4501ee | -8.7531 | -45.47902 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 993f95ff-ede1-367a-80cd-5bac2aac74df | -11.12575 | -44.71724 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fbd077f-0c66-3f1e-b78f-c8c22eb025f0 | -9.54476 | -47.9365 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21611f1-bedb-3e03-be22-3a8062391d48 | -10.18136 | -47.56714 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da646b0a-ef67-3aa8-ac8b-e04b053be71e | -11.29447 | -44.92728 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9acd8eaf-ae69-3fd1-b0cc-cb8c2c3c68a4 | -6.29246 | -43.88937 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README30.md)
