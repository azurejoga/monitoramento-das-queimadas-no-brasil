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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79544d92-b1c9-3e8f-9729-137daa1a4f38 | -14.94304 | -46.79383 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9477e596-6b78-314e-a81c-4eb6edcaa238 | -13.73715 | -45.72131 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5868e6f1-4d10-342a-86a1-d933aeacfe29 | -12.02569 | -45.20197 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 893db8ee-1ea4-347b-a049-fed87dfd5d26 | -13.30191 | -48.03081 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7ce44c5-44dc-320e-af0c-0eaeab4cd2df | -15.79996 | -46.24886 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e34109-402a-3f80-ac97-04547f50029e | -11.67735 | -50.96238 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| fafc0367-e551-38a7-a801-9539d8f22ef4 | -13.34556 | -47.5574 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7dfef10-5aad-36c0-b73a-c4632ee54882 | -15.40133 | -47.997 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2b10fb1-3545-397d-bdb3-22dd1d499751 | -14.74946 | -47.85872 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83c026eb-6877-3a3d-90d0-ef487c2b536c | -11.16908 | -54.90456 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9124c7e1-3483-32c1-85ef-0ca096785937 | -11.15145 | -54.89104 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef770c0a-8a08-3c31-95c8-d17abb0e92c1 | -12.15824 | -51.43751 | 2025-10-08 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ba7873-01ff-3cba-908d-71d54888d5a3 | -11.99593 | -47.19028 | 2025-10-08 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dad0107e-1651-3fcc-bb20-6b7ce2f1790c | -12.30257 | -55.10693 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90f013b1-6e0a-3bdc-8144-b0023eee9458 | -13.69626 | -47.32378 | 2025-10-08 04:40:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2ca430f-f01a-3489-ae89-e53e5f3b2008 | -11.17944 | -54.89096 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c5e584e0-3ad6-3742-94a2-42a763e1832f | -17.90255 | -44.40561 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a155ba93-e08e-3448-9bef-3b893e0fb40b | -15.3663 | -47.3027 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d4e11652-b4f5-3dde-8515-6191c78c99b6 | -14.71154 | -46.0864 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39df366a-a190-381d-9ede-4d5d0c81719a | -19.57984 | -44.65042 | 2025-10-08 04:40:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee655813-9d0f-3503-8fdd-50ebb3ac269e | -11.17514 | -54.86974 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69c314d6-645f-3b34-9e93-850d2894be70 | -13.36069 | -47.55542 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f71ea91d-0292-3f51-800e-39abdde6c1d2 | -18.41819 | -45.21134 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b14a873-95e4-3608-a9ba-2c9d3067f99f | -10.6957 | -56.15986 | 2025-10-08 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0233027-a3e7-3a22-87c4-48f18654828b | -18.40079 | -45.2045 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53424453-4c46-36e5-ac8d-ab55efe9e542 | -14.89842 | -46.84869 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5f79a60-52a8-3a38-b37b-c7a4676ebaca | -16.33792 | -47.05241 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ae92e7-4047-3fac-850b-bb28f34bb65c | -12.32758 | -50.26346 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7ddec1c-2450-343c-ae60-cdb9fe79ca23 | -15.95282 | -42.60469 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1517ea7c-a850-3012-afa5-5264adac8a12 | -11.7441 | -50.92624 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 02f1df42-d803-3456-b778-4edcd3634e1c | -13.29836 | -48.0303 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d3f3a52-8b1c-3509-8973-d740617d2266 | -12.31761 | -50.10979 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d24ed2d-c3f7-32ce-967a-1e485fb02f90 | -17.56747 | -46.06451 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e51d2fe-81c8-36cc-8eff-99513a051e35 | -12.39454 | -51.13014 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ff93d71b-2302-389c-a0fa-ffa632d0c9f6 | -14.79585 | -46.07616 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4711b7d-2f6e-3d77-a80a-2274ad092833 | -13.75494 | -45.74235 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2834c80b-4c43-3dd8-91b4-924e0d8eb1d9 | -14.70656 | -46.09298 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2808ae60-f8d6-3b85-b76c-e11ddf546fb2 | -19.30254 | -43.16622 | 2025-10-08 04:40:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 46d4285d-e68f-3153-9c83-af41a3f31b09 | -15.99984 | -50.96568 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df9632eb-6d42-3aca-9867-1eeaee1954a8 | -15.99172 | -50.84237 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 766258b9-474c-3917-af23-b26735fecb35 | -15.14825 | -52.76562 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a3d2236-eefc-38b2-ad4b-e717e56d85d3 | -14.74219 | -47.8577 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96ccc1c1-7e7a-355a-aa69-280f456ce488 | -11.15404 | -54.87626 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d0030c0-89b1-3ed5-842a-ba65252e6bee | -18.07762 | -44.45116 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6dbffba-08aa-367e-81ff-e1f2d0b49e52 | -15.3173 | -46.17437 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1f70e2dd-c533-3d8d-b9c9-d1e1974ec0e2 | -11.94215 | -51.47097 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 840ed1d3-a3be-3647-bd83-2e063a21de48 | -16.00172 | -50.82182 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60eb0a75-4ecd-3501-8d31-1107e54a8c58 | -11.71423 | -50.94301 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2f7ddef2-cba5-37dd-b956-197b7f743d82 | -13.06477 | -43.59553 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6df6b402-7a2e-3f0a-b21c-ea6bbbd30c42 | -12.92611 | -46.82161 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45d8c6e5-0f59-3a21-8dc2-9fa84c55c0c8 | -15.99653 | -50.9651 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 630cf725-6c0d-3542-ae59-6a22c46d42ce | -15.19744 | -43.73424 | 2025-10-08 04:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9934b039-b282-3ec6-8f72-45fc54276082 | -12.3851 | -51.14672 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c2e7b2f-128d-3879-9ef9-77fbf5c1c35e | -10.6728 | -54.69855 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa8f4984-7bdd-37bf-bacd-946069c349b1 | -13.69963 | -55.01328 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67bc9133-ec5a-3eee-9730-a02ece36d446 | -18.62408 | -46.61761 | 2025-10-08 04:40:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2365830-d234-33a6-bd83-5dd17094a42f | -13.25301 | -47.79064 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87025845-135e-3dcc-993f-20c4418037ce | -13.35602 | -47.77627 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71cda3c8-9e89-3b8c-8b5c-a16e0478c5e0 | -15.37943 | -47.32143 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cc713bd-db32-39c2-a66b-d8f1ec93438d | -15.19269 | -43.73362 | 2025-10-08 04:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee7c3f90-d534-3603-ac78-181b788b14be | -14.39206 | -46.02707 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00c53004-299d-3367-be53-98154e1810de | -13.77102 | -45.80754 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a54ead6-e34d-34d0-ad94-e44db09755f0 | -15.49267 | -47.93043 | 2025-10-08 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31d7d8cc-1ae6-391d-b039-a797babc53f2 | -12.23361 | -43.78452 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b76ea11-9019-31f6-b278-e7396f131f05 | -12.86199 | -42.62812 | 2025-10-08 04:40:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16956182-4db5-3eca-8afd-2bac920154d9 | -12.38566 | -51.14318 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c0c584-2166-3506-83a3-1796a7c41efe | -14.74155 | -47.86208 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0cf027f-81c9-315e-9d98-1f673c36a936 | -17.28934 | -42.65934 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 080841d0-b084-32b4-a37b-44dd64d6b940 | -15.94727 | -42.60726 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e96e8d95-2709-359d-a92a-3bf60beab83f | -11.16351 | -54.86774 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2350a8a4-4b76-36de-8195-9364c0d7b72d | -17.45492 | -43.39472 | 2025-10-08 04:40:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c45982b0-03f1-328d-84bf-b92c64086388 | -13.755 | -45.74187 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96836aa4-ff08-3d21-99a0-fdfd54864cf9 | -14.61683 | -52.47846 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79346459-185f-3387-bd77-c71758499f96 | -11.15964 | -54.8671 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c51e174d-273b-338c-a954-597dbf7d241f | -12.23671 | -47.85949 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 685369bd-49a1-3c6c-9742-e0157731f7c2 | -12.32093 | -50.11032 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d311d74-e137-37db-879f-ba4358a663e3 | -11.21488 | -53.25777 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| af412667-62a6-3c27-ba97-7f62aaf4ad5d | -14.36111 | -47.73341 | 2025-10-08 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52266159-8a3e-3c00-a939-68b8e9f0a02c | -15.62445 | -52.5778 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cbfab51-d0cd-39bd-b7fd-c51f061fe62d | -18.29567 | -45.44449 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d486ba5-29c8-38be-9bc3-50ac39d5e302 | -15.99047 | -50.96033 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 122fec9d-f48f-365b-93ff-3b0dad80075d | -15.99322 | -50.96452 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f44b3c82-159c-3496-ac70-de1e9687353f | -10.88539 | -53.76157 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f64484bc-be04-3d19-8c5c-ee822814936b | -10.28272 | -55.66805 | 2025-10-08 04:40:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2513b236-334a-3174-a9a3-8a81ff6038f7 | -15.30967 | -46.16977 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d5e5b1f-1531-3f1a-86f4-6973b539312c | -11.74905 | -50.93789 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3d892da9-4a6f-3fc0-ad7b-8aa3394a38d2 | -18.03438 | -51.14999 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4982725-6f84-3a62-bb97-cd276ee71a97 | -11.18116 | -54.881 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7bf140be-7a56-3f19-ad80-da5dc111bdfe | -11.16049 | -54.8622 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eda1517a-17ed-3c61-badf-0f071771b70c | -12.01438 | -45.19277 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc341a85-73e2-332e-a145-b3aa5fa96246 | -11.96271 | -51.47078 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a84c4b-a8c5-3472-b1f7-f65892f00dc6 | -12.32206 | -50.27703 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40706b46-0e00-36b3-b5b9-a00298117f6e | -11.75004 | -51.48326 | 2025-10-08 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2660a7e0-c4c8-334d-bb1b-7d73a6baecf4 | -13.73055 | -45.70909 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5e68db-c31e-3981-92ee-e37a75ad0258 | -11.04735 | -54.3279 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 811d5061-b8f5-383e-85b8-909a83623fb5 | -12.21544 | -44.257 | 2025-10-08 04:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368f0755-7407-356c-8ec8-7885fe5fe164 | -13.27062 | -48.04634 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 544f8ec9-58d2-383a-9a11-f0cb22879673 | -12.93955 | -46.8614 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d390fecd-484f-31da-b35b-584d53de1baf | -11.12645 | -54.89679 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86273e49-f439-3a86-b77c-971b2e35b57d | -11.14282 | -54.89466 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README76.md)
