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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04c03030-474d-3dcd-9b6c-e07c4fae0d72 | -4.56095 | -50.46423 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbe1d4a0-f8d2-338d-9def-b828c1c0c523 | -11.29611 | -44.92796 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86f7b13a-d654-352e-b2cc-beac83158c63 | -8.33693 | -46.2294 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a7cfd10-848c-34a5-a6a4-a085d71e98cb | -5.85353 | -44.31042 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 106f98f7-77df-3048-ac37-b530b4092689 | -5.50742 | -45.9174 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 303b1558-6b0d-3be0-beac-5a020e5b65fa | -7.43652 | -43.14662 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7c289d6-3593-3844-b837-eabf13e0203b | -7.45832 | -43.02938 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ec91f82-7a9b-3d7d-8434-2347fb72ef27 | -7.44573 | -43.14185 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21f86e53-d367-3201-ab69-4adaa121e6ad | -8.2557 | -49.29128 | 2025-10-08 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9edf1b5-8451-39a3-83d6-9f4f81ff0e4d | -6.59722 | -59.11937 | 2025-10-08 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2099a8aa-b8bd-3594-abc8-d4322329ccf8 | -4.49726 | -46.36104 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3ab62b8-3f2c-3981-83e5-cf680e17ea9a | -6.11685 | -43.88897 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea527647-bb0e-3571-ab55-43b28df1ddb4 | -9.0441 | -50.62069 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e6ec1fb-1344-32c4-91cf-d451dff55386 | -7.35207 | -43.8667 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5df7b6dd-7a25-3686-8ebb-a4f0a5108e6c | -9.17393 | -47.82571 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d79dab1c-80a4-3199-81f0-e9ace9a647e5 | -7.44453 | -43.15042 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f19995a-f9bb-3c97-ba14-e61237b78fec | -7.4441 | -43.12579 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19715f57-6d42-3e3a-8274-9ba49da47b31 | -5.31136 | -44.9982 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 226b93bb-5f11-3ff6-bc28-565c7c9dd10c | -6.78351 | -44.97519 | 2025-10-08 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7143873f-4a70-3a0e-a2cc-01beadffc9cc | -11.34028 | -44.88342 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2b15f5c0-9869-3ac8-9a72-7c1b89dc937a | -8.10972 | -44.77756 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1528a72-7e63-3baf-b821-ab55f539484d | -8.54937 | -46.23193 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 736f6d9f-e233-3952-8b75-0f2a8cbf2981 | -5.42218 | -43.1885 | 2025-10-08 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9426eee3-da8a-3e2f-94b2-0e625c519863 | -5.59482 | -44.42917 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 282de822-bd66-3c91-af4c-dac1a31c72c8 | -8.22855 | -44.18898 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef13d60b-251c-3b9e-99ba-5dc8e38957f6 | -9.1806 | -46.91448 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d65473bc-8885-38d0-8c78-c6ab00b7e3b4 | -4.11022 | -51.09112 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ba56c5-15ac-330a-8fe6-da65234b5afe | -10.2352 | -52.69669 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac319b85-81ce-30c1-b47f-3edc6ccea3b3 | -8.54842 | -46.28892 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5c16861-3c3c-34b4-ac6b-4ad86a06cdc0 | -9.25061 | -47.7167 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16577c20-b4b8-3b5b-973a-a26ab38aaf35 | -11.67025 | -46.39897 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 874a6eb0-2735-3cbf-90d0-627214c840fe | -9.09003 | -47.96426 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2a93e78-9fc9-3396-ae94-0460e7f40070 | -10.38726 | -48.13024 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1bbb48cc-216a-3a4e-9d8b-858b564804ea | -10.24569 | -52.69847 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5a7a9dc-3c28-3bfd-8eb5-76f3896d3e26 | -8.68219 | -44.72513 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca6bfa2-c940-3164-bdd3-30e9814e2292 | -5.83022 | -44.96875 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 617aeb3e-5f50-3d59-bbbd-fff589d30b2b | -9.18944 | -47.79326 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6aeb0198-864d-340d-9dd6-e7bbf55b727d | -9.91543 | -52.9409 | 2025-10-08 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e924f98-4d77-386e-b8f7-2d3a0e85aaa8 | -3.57862 | -49.43761 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 497191a5-0605-3116-9194-42c6adb6d9f1 | -10.58613 | -51.58048 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a474cd1c-83da-357a-9865-ae03de2bd162 | -7.47527 | -43.12415 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eb66d5ad-27f7-3c97-9598-71891e6994a3 | -4.68793 | -49.49181 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29847134-9428-3a46-a61d-aeea0e32e81f | -11.25758 | -47.7647 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c6332e0-1f72-3ea6-adf5-042734a36407 | -11.78599 | -45.14098 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc25df70-866d-3f3f-891d-4172f40313a6 | -9.17279 | -47.83327 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c36e05-6d56-3c78-86b0-1bb1745ccb77 | -8.12263 | -44.77295 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db9ccba-f6c9-3039-8890-48effef23570 | -7.44834 | -43.15533 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0b4b9a2-ec7d-3068-84d5-e4edb302eb5c | -10.3575 | -50.28707 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3f8c210-034e-38c6-8fe4-eaacb6cdaad8 | -4.25129 | -48.55681 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab0105dd-32cd-3641-b26f-a024ffe6b15c | -11.70367 | -46.35546 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3a8257-bd8a-3f33-bd90-b9e767a9782b | -8.37484 | -47.06098 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f543a91b-254a-3722-9163-e5fa9539effd | -7.72691 | -42.40601 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ca1f574e-039b-32ab-b590-50d597ffeb1b | -10.86596 | -51.02105 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26debcc4-50be-374d-8e50-1adc3b941b91 | -11.66646 | -46.39837 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b705360b-2e85-370e-a065-9bba33161256 | -4.50365 | -46.36605 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a01173e8-bfe1-33c8-a535-9fca6637f359 | -6.17334 | -44.68599 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4206338a-103a-3b93-bb78-0c536557c10e | -5.86258 | -44.30452 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ea966b2-19ff-332b-a550-36ec9a44044e | -9.03965 | -50.62718 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce2f90e7-5b32-390f-8000-ce19894449b8 | -8.60434 | -48.25258 | 2025-10-08 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc7611c4-6f27-30b7-8f8c-dcb0daa85153 | -4.68434 | -45.84516 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc716b4b-89ce-3a06-b139-376bf4d10054 | -8.60715 | -44.9046 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a80884c-073d-3a3b-8562-59ad63743855 | -7.78693 | -44.22688 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04d23be8-3db2-369b-a397-8d4577e1804e | -8.20142 | -44.20052 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d96fad9a-9862-3b60-9f6b-369de641e51f | -9.32755 | -49.81843 | 2025-10-08 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca2d9833-33cb-336b-91f9-ce8ec8ec1aa0 | -9.39652 | -45.93927 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb69673c-3499-352e-b9f5-e7b2dad345b0 | -9.77957 | -48.28453 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a96095e-2f2a-3b27-b973-919dfe3add84 | -8.86126 | -46.77641 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dddf4855-a849-3e6b-8a1d-e23c25917796 | -10.39349 | -50.23228 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b15f52-3324-39ab-a203-bc066060bb68 | -7.44012 | -43.14977 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7a457864-a558-3eea-a692-0fd247a59d6f | -5.73462 | -43.61242 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cf864cc-479f-31ec-a90f-6f72db3ba7f1 | -6.182 | -52.78149 | 2025-10-08 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ca16ac-aced-3242-a50e-224865f0627a | -10.39404 | -50.22878 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2357c821-f190-34e7-9370-f314474ade16 | -5.25761 | -45.27338 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffda4730-9ee2-37a7-a33e-7e82d072041e | -8.40234 | -49.7416 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2a6c512-8ec6-392d-9d8c-7e3fe9a3324d | -7.78445 | -44.21502 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a0d0792-6f22-313d-b2cd-035fc9616ce3 | -8.44897 | -54.71674 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949e173b-5155-3120-ad91-4fbe5c0918f3 | -4.96166 | -48.01397 | 2025-10-08 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a490d0e-fb72-3e9e-a0fa-91f20814a111 | -3.45645 | -50.09523 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e4fbe84-6ec9-3abd-98f6-8861284be869 | -7.29457 | -47.15563 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 214bb046-84cd-3b0f-b04c-b2548e19d1a6 | -11.79012 | -45.14142 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 745e518e-c0ed-388f-b6ac-25d68a1edbc2 | -8.18621 | -43.33331 | 2025-10-08 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 28dcb9ff-14b3-3fe7-80d9-2d66a874185e | -9.8454 | -49.30883 | 2025-10-08 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b58ecef4-da51-3fc0-be51-fb473459c329 | -5.88996 | -45.55514 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2d0ad16-cab3-38a9-9b16-eb5eac7eaee1 | -7.47012 | -46.85416 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c76ad94-fd58-349f-9197-537ff5845e5d | -10.64581 | -47.80082 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f3ccb5b-d949-3730-ae3a-54a83565b6f6 | -9.25919 | -56.29061 | 2025-10-08 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba45e079-77e7-33f8-8433-e30be9cf8fdb | -5.77252 | -45.74233 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93869332-c877-34dd-8e5b-019bec1a8310 | -8.41359 | -46.80796 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64c2bf2b-4be5-32aa-96bd-0be89800b7ac | -10.38274 | -48.13689 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70144ae8-fbeb-377f-bc10-389c0e636155 | -11.8754 | -44.94183 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac9c23db-e2df-3db8-949c-488183b74873 | -7.80202 | -44.21012 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b33690b-c0c6-3cd9-b115-ecab748f3d9b | -9.39514 | -45.94857 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cda9409-7606-3d3e-8ccc-13be561dd554 | -4.47983 | -49.71253 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8dcdcd57-eb56-3af2-9154-73c7721c0ef1 | -5.4033 | -46.2295 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b84b4e-5a22-33b0-ac56-11ca8b803a45 | -5.41029 | -45.29277 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01093d93-9870-3f77-8d93-254603f2fdbe | -7.47071 | -46.85023 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39c292c2-63d8-3990-9819-ac00d8a3fabc | -7.7861 | -42.41032 | 2025-10-08 04:38:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 661732db-36c3-35c2-be7e-8accda93fdcf | -8.92721 | -47.3534 | 2025-10-08 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc189ae5-be0c-3a71-a068-b887b311b1ae | -5.74508 | -46.04801 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07783622-f3cd-3460-8ec7-01481643b518 | -9.12243 | -48.76009 | 2025-10-08 04:38:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README68.md)
