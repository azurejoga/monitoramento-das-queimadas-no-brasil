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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89e91edd-c7e1-3919-9c63-90d59c888c0a | -5.7025 | -53.45739 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3954befd-1874-3620-86ee-21b728ab124e | -3.2259 | -53.96901 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51906eb5-9eae-35bf-af41-14da14747ee3 | -3.00568 | -54.06066 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f692c6-7ab4-303d-a6eb-8a6813e52f1d | -11.67626 | -46.77422 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a1199cb-14f1-342f-9d6e-3746d00c25d6 | -5.99623 | -40.94262 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61878cda-fbe6-3d34-8692-9dae3d869264 | -3.93563 | -55.71765 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 413ed90e-eb35-3bc6-9c98-ea3d8532a379 | -4.04858 | -46.90784 | 2026-10-09 05:04:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1675de35-d65b-3fa7-9ad2-6b10973da0cc | -6.31963 | -54.80915 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59bf480-a680-3538-b79a-f24b349d1de5 | -9.71856 | -46.94617 | 2026-10-09 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce5a9c63-7742-351f-baef-51abf984e7ea | -6.5058 | -55.38846 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678731c8-dd2f-34c1-89e3-271474cf5566 | -3.01184 | -54.09227 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6d62c3-03d8-32af-9d5d-1f03c9ad46ad | -3.07124 | -53.96835 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d944bd9-b467-30e8-bfe6-35c8a9d45e34 | -3.17595 | -58.84318 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67210abc-7c77-35ff-a874-7204ef7dcc1a | -3.08388 | -54.27075 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42631e01-29b3-359b-96f2-e617319811dc | -8.99701 | -45.90811 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44da284b-3112-3e28-813c-e37ecc0fac6c | -3.03468 | -54.08409 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8df93bc5-f40d-3840-ade1-6fe6950dd645 | -3.16878 | -58.62813 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dc8ed60-833d-3ef2-ae2d-b0f495bac969 | -3.0611 | -54.2552 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef048fff-e9bd-3c16-8430-874976e0bafc | -9.10656 | -48.80658 | 2026-10-09 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f78b17-f757-3e45-a321-c1e11b4555e6 | -7.17985 | -44.28492 | 2026-10-09 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58d66531-24e4-369c-b81a-2aa9d3e9c97f | -3.00746 | -54.11922 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01122412-5a0c-35df-8e15-ef5318535904 | -8.93281 | -48.60643 | 2026-10-09 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e965aff-d584-304b-b938-34bf965a5de4 | -3.23449 | -53.89271 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c095eeca-7055-3f82-a1ef-240fe62f55c8 | -6.13095 | -53.05626 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a9ea062-9bc5-37eb-9377-d42895a64c03 | -8.33576 | -50.87854 | 2026-10-09 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da60673b-2217-3013-bf7c-72459d8a1ad1 | -10.95347 | -50.70525 | 2026-10-09 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac7bb034-f5b6-3dee-b420-bec2fba7b09a | -3.26511 | -54.06414 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f27ebed3-aa5f-3fca-bbf5-54eda2c39860 | -3.25791 | -54.26473 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae538d4f-bdde-367e-a09c-bd4286716c5a | -9.91293 | -44.78562 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c8b9259-cc19-35b5-a2cc-fe36b46b3173 | -3.39039 | -61.07706 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82dd7499-ac2e-30bd-ac23-beaf8940b60e | -8.3387 | -49.12728 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a5f30a1-fdf5-33c7-ae4a-2b4be75a92c1 | -7.44353 | -63.55151 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc89449-7027-3153-8f68-b931d391678b | -3.9166 | -52.13462 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 304a8031-66dd-391a-8c1e-156704ab8fc0 | -3.54334 | -54.66895 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425b6edf-9fa4-30ce-98dc-c79e6e4f76de | -6.49491 | -55.29963 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c7894c3-d52e-3207-9c4d-525c9f088d6d | -5.70416 | -53.46859 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9e16f88-9339-3acc-ae9a-bd473f52e842 | -11.99735 | -43.47223 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70c6f36d-3b16-3f70-ab39-6829bf2ad76d | -3.01795 | -54.76416 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 094be096-9482-304f-8da7-ac35604aa187 | -5.09622 | -56.19708 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a5a7a34-bea4-39b7-b13c-c664dcb53cc9 | -5.91345 | -53.88467 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0e58812-b317-3b68-b67f-da6819a32a64 | -10.29296 | -46.60913 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14f6118a-ec9d-330a-8698-a11d8c7b61e5 | -5.70976 | -53.46182 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c97aa8ee-eea9-3e0e-9971-c0e9dfd52e96 | -3.97123 | -56.11921 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c2eb058-d218-35bf-a629-d8ce35c190c3 | -2.8785 | -54.17924 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca07887-fdc1-3654-928e-0e5d114973fb | -3.59748 | -61.62126 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ee56390-b257-3a90-a910-31aad4ac54ab | -8.71187 | -62.41804 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4df9dcc1-036f-3822-af7f-7e55be447d8a | -3.1205 | -53.79432 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 071d9994-30b1-3a1c-9b6b-e500205117c7 | -3.3036 | -54.04682 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba2b2353-4ce8-3d89-a7db-df7e918b0e88 | -6.0667 | -53.60667 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0764ac3-36f9-3a07-9628-56ebec986e18 | -7.2898 | -45.41777 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 454df486-0ea0-39d8-a808-8546d918f0d1 | -5.67622 | -46.35228 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe73e983-581e-390b-9a31-a4d3c4cbb3b4 | -3.1184 | -53.76322 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a2f7903-6a1f-3e6a-af26-a00be6916ea3 | -3.28969 | -54.04458 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e84efe-f0e9-3283-99a9-ab1ad09d2d46 | -3.00485 | -54.09116 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16882d1f-fdf1-3bf4-96d0-310b848cd0ec | -3.87891 | -55.82612 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 003621b3-a22c-3a7a-9c70-3406eeacbf5c | -6.6721 | -63.03119 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf8a5ef2-b5d1-3293-a55d-a9cfa4c3ee44 | -2.46877 | -58.00816 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45808fd8-7820-3e52-be8f-9e33a2cc5658 | -3.56843 | -54.48933 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d6fe13-9c67-3bcc-8997-1e7e83e1fbc7 | -3.2596 | -54.03197 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f038b007-bb9c-3cdf-81d3-51403e37784f | -2.85109 | -59.27246 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5fb420f-55ee-3cec-b72f-9679c4dfae81 | -2.92814 | -54.11938 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e909fb23-7eab-35d8-8c61-c59ad0cf16d7 | -4.54785 | -54.96794 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85077086-8ae1-3abb-9f56-9e34fffd42e3 | -3.5435 | -59.40616 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 32cb64e8-a541-3ef3-ae15-5f9ef81a1866 | -9.80255 | -44.77258 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b6cf2d7-6f66-3de6-8081-630e891f095f | -6.87648 | -45.90005 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fe960bb8-af08-3151-9cd5-89c19a18cc81 | -3.04205 | -54.10503 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 255fd9d8-58ce-32b2-aa50-0cd8eba82f35 | -11.75608 | -45.47692 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 531ef7cc-c656-38c4-96bd-9ab0704e0f91 | -4.36363 | -55.64519 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1406aaaa-63d2-38df-a8cc-735cbed52930 | -3.92754 | -56.02539 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25829e32-0684-380a-8ef8-1b6131738b91 | -6.45662 | -55.05346 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b028b05-9c72-3781-a43b-a78b06da34a1 | -5.10014 | -46.22408 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5830f7a-d4ff-3118-8023-ac76794679c7 | -3.21263 | -53.96292 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 545e758a-7e6b-3c7c-a896-8e9feb3eb043 | -11.39698 | -46.66914 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 205f1ed4-f4cd-386d-af4e-410a9c418b12 | -3.98153 | -56.11412 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06325377-eccd-3958-9602-b7643dfef691 | -8.7303 | -45.15874 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 586ac28e-a6f6-3b7f-adaa-82bce2b41ef4 | -6.96314 | -45.25108 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc9ccdab-5b29-3133-84ba-6162b504ee26 | -3.87571 | -55.99062 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f72bc32-b42d-31bb-827d-f8fdf0a4a14c | -5.99171 | -55.35868 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20e30256-1a73-382b-93ee-85046020c3c2 | -3.03281 | -54.09562 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaeab39e-5433-3283-b294-174d881cc3ee | -2.49834 | -58.06907 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ece61f5-30ca-3a18-b790-5277c95232a0 | -6.48997 | -62.8499 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7770d0ce-0bb2-3dea-abd9-09f7746294ef | -3.93914 | -55.71558 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c5fe5a-ee6a-3382-bf3b-1b5aed1e088f | -2.88808 | -54.07356 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 916d12b1-b663-3952-9027-ef72487afb49 | -3.90343 | -55.89069 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 197b8629-ce9c-3c6e-97e8-6ec0ed017a14 | -6.50147 | -43.95257 | 2026-10-09 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af7dbbc4-a48d-3b8a-9165-e3bf166f7252 | -3.94897 | -56.11077 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8392231-fa4d-3c8c-be69-00b0679cc1ef | -3.9881 | -59.34892 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ac5f5b9-e3f7-31f0-82c4-1fb0fc70b8cc | -3.00595 | -54.10413 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e93272-f3da-3d8f-87c5-8fa86e022a03 | -3.03631 | -54.09618 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe26c88c-a477-37b7-9612-0178475f7abd | -3.28659 | -53.9973 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8150ab8-63bc-3254-bfd5-fc1c774c73e2 | -4.2946 | -48.60526 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c040014d-41b3-3103-bc6a-d6db0c9e2146 | -11.76832 | -44.95596 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2414037a-614e-3a32-a9c2-4f0a10f7e454 | -2.98374 | -54.10848 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9947e056-544c-3680-b43d-1a215fc2f488 | -11.76918 | -44.94933 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 430a5a11-d74f-3700-918a-215137e95b3a | -10.25051 | -49.67999 | 2026-10-09 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a1cc5bc-63c9-3b82-a105-67df76f5e0b3 | -3.17681 | -54.74621 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad47c43f-1ad5-3501-945f-bf3912df9ade | -3.66967 | -60.60527 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50fcfc2a-ce1c-340f-a85d-1016b57a041c | -3.24978 | -54.66986 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdbe1aff-9b6c-3d76-a330-12b4e9d3d800 | -3.80491 | -49.94052 | 2026-10-09 05:04:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 382a5fda-91f6-3f53-a973-f27a5404aaef | -11.6088 | -43.71314 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README132.md)
