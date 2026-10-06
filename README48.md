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
| e10add87-c677-3053-b01f-55adcb4ed629 | -6.92878 | -43.67664 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b733f596-40b6-36dc-9465-dbf7740b6af8 | -7.38073 | -54.99903 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f428648-0333-3790-b25c-d84d15174661 | -6.15405 | -47.12167 | 2026-10-06 04:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e695c4fb-6d68-3879-bb2a-73cbc1abf23c | -8.86799 | -45.37172 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a744d34-64b5-33d2-8898-7a1f5db661d9 | -11.68601 | -43.65203 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 575aba19-6769-3c3c-a8ae-9708d2a18b24 | -6.45408 | -55.47759 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b17d134c-45ec-3b3c-a207-e443ec92d568 | -9.16362 | -61.4094 | 2026-10-06 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4c4131d0-f6fb-35a1-8c16-3481fd41c9cd | -4.29133 | -54.801 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17f0e146-802d-3ce4-8af0-2f0ae8cb26f1 | -3.70504 | -58.93725 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59fa2542-dad1-313b-a2cd-ff8c071b433b | -7.48205 | -42.814 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d15f6d49-d19d-3a5c-8070-f1716ecb1e33 | -7.81932 | -45.312 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e79eae8-3638-30e9-bb43-421a40f254d8 | -11.36078 | -46.6759 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5caa911d-b4ef-3372-8912-80a2c8491805 | -6.81663 | -39.30267 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea924f1d-4363-318a-908b-4dbaaf3de8fb | -11.29185 | -45.51793 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d444a99c-a5cf-397d-bd8e-d5887bae600c | -11.27032 | -45.51021 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 83effa2b-1212-39ea-94c0-f886434512a0 | -13.02582 | -43.11881 | 2026-10-06 04:40:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 13a6ea13-0def-363f-94b0-bdd773169a71 | -6.61135 | -41.5829 | 2026-10-06 04:40:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e790ce48-8197-39bf-bcde-688664a1b9da | -6.44906 | -55.44277 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dc5ff22-d84d-3aaf-926b-b1fbe4267038 | -5.84783 | -45.01814 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c1cc38a6-93c8-3c3c-8208-2e938eac7741 | -6.18651 | -44.8601 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| adbea2a7-1337-3341-8665-565967a0dd4a | -12.76935 | -44.88471 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a7ace06-385b-3dc7-b55f-525711e03e35 | -7.73202 | -45.46251 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3a684b5c-cf4f-3f12-8b72-a9452a6f9fff | -9.95512 | -43.47879 | 2026-10-06 04:40:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3cd131f-5a69-3b34-8291-9ad5f0d879a5 | -5.5908 | -47.26912 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e8dac6d-af08-3cea-9cdb-0f6b7518da7d | -8.52122 | -48.90836 | 2026-10-06 04:40:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878bfe66-2cb9-3875-810f-547792806412 | -7.46644 | -42.99705 | 2026-10-06 04:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c007f11-1361-3e63-9cdd-e9ac2f80291e | -11.26837 | -45.52353 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7afa2b72-720f-3997-8f58-d398ffff3e67 | -12.53148 | -47.58243 | 2026-10-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b824dbb2-715f-3ee2-88e8-f3c08bb6d605 | -7.7759 | -44.57261 | 2026-10-06 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b68f5845-f1b9-3107-9793-7088543a80a0 | -9.80968 | -44.79737 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc329ec6-7026-31bc-9a32-f0fea6a1107c | -13.02963 | -43.12381 | 2026-10-06 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4b2e02e5-c276-3105-b793-7abe27312dff | -11.26533 | -45.51852 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 100e07f6-02e9-3707-86c2-12f9520068f1 | -7.01484 | -43.4442 | 2026-10-06 04:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8460679c-5a01-3ee4-8f49-a9eec666c123 | -11.65932 | -43.66043 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ece0c532-06ca-30f2-b6c8-359061e70d91 | -6.81706 | -39.30404 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7dffb9e-aa9d-3fb7-a197-35edac9f435a | -7.47958 | -42.80207 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b0ba07b6-0c9f-3d43-84cc-9a6d2a5db033 | -12.13908 | -45.10624 | 2026-10-06 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3772066d-7a7e-3256-b829-65bbba1ce7ff | -12.76223 | -44.87854 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4349f57f-f7b0-33ef-80c3-6d81bbf23972 | -12.13699 | -45.10378 | 2026-10-06 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 233ac724-b74d-379f-b990-512033a697c6 | -11.11864 | -45.95648 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5f90644-15b1-33cb-9def-ed5af2ae9b79 | -4.27723 | -55.76216 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5706b402-b58e-3271-ad78-f2779d27790e | -6.88346 | -43.68291 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2b301db-f74a-3c5f-84fe-53e8d90a93bc | -3.96773 | -56.12592 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec123a3f-3382-3179-94b3-59c680958781 | -8.58489 | -45.65398 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 201e2b53-cec2-305a-a0f7-bdb14949d2cf | -4.45149 | -54.96419 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f137ea83-7e85-3936-a737-4c3c8d30ba02 | -7.47542 | -42.80155 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5df1254-4407-3288-8957-a1ea646660f9 | -6.72374 | -44.28149 | 2026-10-06 04:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07d0c417-903a-3758-ab8c-937ed022c7de | -4.29052 | -54.80599 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd6b6d01-a306-3b67-b024-63310570c1fc | -11.67497 | -43.66993 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c71dd510-b6ae-3923-8a09-edbde2067f27 | -6.00897 | -47.39583 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a515952a-25b7-37c9-9978-f0322a11685b | -6.44151 | -55.43872 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2656fa8-b596-3901-a8c2-1d3121db9fe1 | -6.45182 | -55.43538 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97bfc737-da28-3d9a-a22f-f6bf824eaf84 | -5.76482 | -47.08968 | 2026-10-06 04:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e5ecfb2-5f8d-3fbc-9b17-5d994aab3ef1 | -9.8588 | -44.80487 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11de597b-a9b2-3975-b85c-cdb625782bf8 | -6.33631 | -46.95217 | 2026-10-06 04:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b4eee6-d858-3e45-a0ff-6e5535c30c10 | -8.58596 | -45.66513 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8444a96c-e25a-3fe1-89c7-c96ab048a91b | -6.17679 | -44.29097 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51249002-1b80-3057-95fb-dd6a31e8a1aa | -7.28894 | -47.26649 | 2026-10-06 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4353b4c-f869-38f7-acd1-f819de16a8b8 | -4.06104 | -56.33398 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4a5605-c318-3b6f-a0e6-0a477a222d58 | -11.27402 | -45.51077 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6e398448-55f5-33cf-a7c1-15b189ba3c7b | -12.26561 | -47.4192 | 2026-10-06 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c7cec4e-9187-316c-ac5d-5f464aa1bbf7 | -3.55486 | -59.48413 | 2026-10-06 04:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e4500c2-3c2f-39e7-b14c-df6dd47efc56 | -3.24637 | -60.73513 | 2026-10-06 04:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed79985a-b595-3d9d-9bd5-e53e71427a91 | -5.25574 | -49.79099 | 2026-10-06 04:40:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc8e58b8-8a3e-3e3f-9592-92c5d57f9cc7 | -11.68748 | -43.67157 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bba1c6f7-7acd-3b62-88df-e698403ecd8f | -10.49929 | -44.42025 | 2026-10-06 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05316a49-4e56-3b45-8323-a184908e4b5d | -7.75343 | -49.20473 | 2026-10-06 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28a4c311-acbb-39b4-b7f8-3684a0700c68 | -10.24033 | -49.65467 | 2026-10-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b0d11d7-c855-3f25-9cf3-ba04db473baf | -9.59154 | -47.78239 | 2026-10-06 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a701ced-d62b-3da6-9e4c-3a13976af989 | -10.9715 | -45.41204 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d47237-0bd8-3df7-983e-3b0e7dd91ab3 | -11.28511 | -45.51243 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 6f501812-43ad-3fd0-874f-12697965f081 | -11.66683 | -43.63723 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d498d4c7-b2cd-3f44-8251-9a5b26195687 | -11.24536 | -45.25529 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa61747-ce91-39e9-a208-9ff8227899d9 | -6.36085 | -42.54747 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1246981-4b4c-34d6-a480-226879e10265 | -10.34678 | -44.73959 | 2026-10-06 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05f4f565-2ffa-3c1c-ba20-9c46b75f3878 | -11.27162 | -45.50135 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 525d63ea-07b2-358f-ae45-0a87dafba985 | -10.19117 | -36.23225 | 2026-10-06 04:40:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72982852-562c-3183-a071-a6c2fe662641 | -6.88735 | -43.68351 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c8be9eb-2d92-3866-a326-9984b15db8a4 | -8.32343 | -45.46634 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95c9f9fe-8b08-3190-9911-ebf36e68d477 | -9.77164 | -44.79401 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cb3e00f-f57b-3722-9b3f-0169ae335e33 | -7.57212 | -46.63802 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4528e04-37ab-38b3-bbab-d787de1aa235 | -6.34566 | -42.56456 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b8d37d43-65bb-32a2-8463-2e84a3c8a7ef | -9.81789 | -44.79396 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d9f1df2-37e1-3063-9856-ace6752cb69b | -11.67153 | -43.63406 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 694dc5b0-cd6d-3b5d-8e06-537b1883f2c7 | -11.26902 | -45.51908 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2b6ad605-9d53-344f-af4b-670aa3a2839e | -11.25988 | -45.50411 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1dfad7ba-f015-3769-acd4-158b01054677 | -6.87958 | -43.68231 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f144450-a276-36e8-8456-0e05cd5a2073 | -5.68403 | -53.48868 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24bdd54d-21e7-321d-8fc2-c8ca1260fb79 | -5.84009 | -45.02105 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71a90d71-fcf3-3725-b517-8be02f5a0264 | -10.367 | -45.02924 | 2026-10-06 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc745345-0ea9-3498-aed9-83cd803b237b | -5.58362 | -47.27155 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 575feef6-dcab-34d4-9664-8466969a3679 | -11.22296 | -44.84873 | 2026-10-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07330d26-63d0-3511-81f0-981559ed7260 | -7.1038 | -42.53888 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86b5185b-8ecc-3927-8311-0c36aa854a29 | -6.35253 | -42.54631 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcb5a280-928a-36b8-abf1-ac3d849bc19d | -10.24366 | -49.65521 | 2026-10-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e4d497d-17da-39b7-a22a-ca6b049e7ec1 | -7.86753 | -48.59681 | 2026-10-06 04:40:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bd6d6c4-0a4d-30b1-b3b7-ee30b8060037 | -7.48014 | -42.7983 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 16df6552-8ae4-3863-bc59-cdb62bc5d222 | -10.42676 | -49.25291 | 2026-10-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d88fb3-4b45-3e8a-a41f-35c6eb61720b | -7.47486 | -42.80534 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 873a9028-4718-313d-a216-b39582e23751 | -4.80896 | -54.73593 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
