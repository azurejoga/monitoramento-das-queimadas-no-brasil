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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 587af80c-c35a-3900-a5db-0633d1683fb6 | -15.2015 | -44.49286 | 2025-10-09 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04a041ee-00f9-3773-8c48-7e731fb10ecb | -15.21799 | -46.38401 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2c28c97-a367-3a66-94c2-7fd71ec5eea9 | -15.55632 | -45.31723 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c6044bc-4744-31e3-8033-897cd94f4365 | -17.93848 | -57.54655 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 379b4ce8-5b93-3072-9d95-aefe91a4e8d5 | -18.04646 | -44.99194 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e57881c1-8e8f-3f4b-83f1-db2bea7393cd | -17.98962 | -57.4912 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12f33c32-8355-3c44-bb5b-ce12b9386a4d | -15.56529 | -45.30357 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47bc9305-3b58-3f6b-bdea-a160a7ce9eb3 | -17.37501 | -46.89743 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03fe445a-fca0-3c62-8959-414fa572229f | -15.38416 | -48.05524 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c21eb7-bcde-320c-9b55-ee1d2a57d96d | -16.27368 | -47.13874 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f275937-de32-370e-b612-df5b4f835684 | -17.38533 | -45.06781 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96029bb7-6e0d-3ccc-8bbf-06f39d3aab41 | -18.03725 | -57.56651 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f697b304-0ab1-30ef-bc49-dec64ff8e059 | -17.89894 | -44.26025 | 2025-10-09 04:21:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a07246b-db8d-3da9-b1db-55bb7d92d968 | -17.57896 | -44.25372 | 2025-10-09 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 882d83b5-a70e-372e-9a2e-6a5663ea63ae | -18.07339 | -44.4796 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42273e4c-9762-3289-9080-d5061cfc05b6 | -15.92021 | -43.29676 | 2025-10-09 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ae7feb2-fcf0-31a4-8a67-17333d90caa8 | -17.89748 | -57.65907 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fb6fa968-2b21-3422-adb7-6dbced54c0af | -16.11546 | -43.28675 | 2025-10-09 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c1df7c-ed49-3643-9642-e408954e080c | -15.07336 | -46.61173 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9944ec2c-06e3-373f-86f0-a8615fd55664 | -15.24395 | -46.37004 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3edcd3f-df8d-364e-8788-ce6b9aeab435 | -21.47539 | -52.62085 | 2025-10-09 04:21:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2743b5dc-8cd9-39ab-8af8-a0fbe6e6f53a | -17.98903 | -45.61636 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94132e8d-77b4-386d-9c0f-8942a5dafae0 | -16.70646 | -47.61967 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0622945f-6b39-33e6-b200-623cc8ff5073 | -16.69609 | -47.59933 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22667b4f-e1ee-337e-848e-71bc0dd4212e | -15.52487 | -41.85513 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9068f00f-a0e2-33dc-b606-2e203c87bbab | -18.05221 | -44.95248 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ae469f2-5ac0-3cde-9bc0-b6cb03e58a63 | -16.63076 | -45.43286 | 2025-10-09 04:21:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef131989-d354-3bf4-b4a0-00b4332fb995 | -18.40388 | -45.24637 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9106480f-72ac-375f-a56b-73ef3dadcc46 | -18.06219 | -44.48219 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eea40c39-55bd-311d-9a6d-f0b5df824bff | -17.95767 | -45.00272 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4b39fbe-8654-3efd-8b59-f92baf2ffd25 | -15.44416 | -47.03595 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5effb6fa-4502-3889-96b4-acf105349a2d | -15.47293 | -47.95664 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51134574-330f-3b57-951d-0e553a1980cd | -20.30135 | -49.69209 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2276c88a-e982-3db0-9751-089a1834195f | -17.89025 | -57.66571 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c9c9931b-a989-37df-8576-c426d69e79db | -17.21057 | -47.65438 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6b56c2a2-5508-328b-9a0d-f8be0624e30f | -17.38058 | -46.88359 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b82e6c51-0be9-3bb5-89df-4003e8adeea5 | -16.71211 | -47.60581 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 519c14b3-001b-3a14-9702-e26f71fffa36 | -15.07723 | -46.60872 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 460e2fe2-8e36-3419-8ed4-28ab0fec8258 | -15.91053 | -44.28661 | 2025-10-09 04:21:00 | NOAA-20 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 149e372b-b434-3ba2-91de-270d4845d9ab | -15.28996 | -47.3196 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 972ee345-e260-3835-bcd7-90f10455b4cc | -15.24782 | -46.36703 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66de1d5f-e315-3a6f-895b-183d56bba45f | -15.21855 | -46.38046 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 184b7c61-6d66-37c4-b92f-a146597cd98a | -17.8203 | -57.63771 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| aa4236d0-034a-3087-ac6e-5f32438f6c7e | -17.53479 | -46.05847 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3362d667-f948-3a53-9220-1e28cefcb20e | -17.82227 | -57.62862 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d0b304bd-069e-3cc9-8948-036d6dfe7acb | -17.37469 | -46.66034 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff489c22-97ca-3bad-a5a9-fc11c037d8f1 | -21.2074 | -47.76745 | 2025-10-09 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02f7c973-dfd1-3054-ba09-75750d2adfc4 | -15.78544 | -46.25008 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f50eb9-9a58-32c8-a628-9240464e50a2 | -15.63617 | -46.44559 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 290f4296-8f25-3f68-bb31-0c4b7c1c83a8 | -18.05336 | -44.96885 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ca6aee10-414d-3c2d-b748-20425ad95c00 | -16.26985 | -50.9851 | 2025-10-09 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edc5df73-0ef7-3a78-a929-81c970b37acc | -20.30002 | -49.69986 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 256653db-640f-3b70-9c36-10d991380b3c | -17.95423 | -45.00213 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| cf86d9d8-b388-3624-917a-c86f11d6b9e2 | -15.71825 | -43.94912 | 2025-10-09 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d56fe627-abc3-30c7-bd8d-c6b1f8bb6f14 | -17.26786 | -46.90876 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e257548b-4386-380b-bdaa-d550bc003ed6 | -18.00556 | -44.98147 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 235d76b0-f0e4-38dc-a7f0-afca340a869f | -17.99185 | -45.62067 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 292fe780-aa57-3e23-bc32-535af20f27a1 | -17.37081 | -46.6634 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2acb23ed-64b8-3b06-b2dc-dcb58981c493 | -15.39028 | -48.06018 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6f01b86-914b-323c-9952-bee255b9aab3 | -17.2552 | -46.9029 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d15551e-3f93-37e4-b2ec-169c91e1286e | -16.58762 | -46.54767 | 2025-10-09 04:21:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f64191de-4a9d-3461-a06f-4599a87b42df | -15.49908 | -46.86189 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d50e440-2c11-3380-b22e-c1c4a3c11201 | -18.06573 | -44.48267 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7efe6048-8141-39d5-96d6-9df3f9c58da3 | -15.38478 | -48.05151 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97f9aeec-81aa-3c32-9f25-b3253b87401f | -15.4914 | -47.95938 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7737aefa-cdbc-3185-864c-4b45c10c6c02 | -15.38354 | -48.05898 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba5215e4-a585-3b68-922d-085d941934e4 | -16.63219 | -45.43288 | 2025-10-09 04:21:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 158f1429-10c5-3abb-9339-3d63390d53f6 | -16.74859 | -43.9817 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14879ea1-b277-3e70-8bba-0ad31f9a471a | -18.03956 | -44.99081 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27839f0e-9095-353b-b81a-93ded9715cf6 | -16.11522 | -48.24081 | 2025-10-09 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b1e5706-0005-385d-94dd-3c395d59d138 | -18.40904 | -45.23504 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e92be803-65b4-3b94-b839-da09fd52c43f | -16.69941 | -47.59991 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f74b21b6-8a81-3282-9d84-b12f2c4dbba6 | -18.29228 | -45.43589 | 2025-10-09 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb87aa2-72af-352c-832d-80c5763bb549 | -15.39609 | -48.04589 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34017f36-9a58-3ff0-ac2a-d4fd3539b3b1 | -15.55968 | -45.31776 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81b0c6b5-c26c-373d-a0be-ca65d324504f | -15.3661 | -47.10013 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c9efbdb-92d9-399d-944b-864fd1dcfd16 | -17.20725 | -47.65379 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34741e5c-8af7-3ec7-a70b-cf46e628d1c1 | -15.31385 | -46.18398 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21afe873-0082-324c-8270-07c55a5a169e | -19.93669 | -44.8922 | 2025-10-09 04:21:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deed8c03-3b22-3cc5-a8e4-d56f8d5c7de1 | -16.59847 | -58.16121 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 913ad31c-9129-373e-a05f-7c2830d34432 | -14.94425 | -46.78382 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 106a7135-10a2-3867-a2ca-af1b8b537cb1 | -15.22628 | -46.37445 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc4d863f-3d56-343a-8117-883b64f37042 | -15.25444 | -46.36811 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3cf32d1-bbc3-35d4-8ae5-f3e4076ad0c5 | -17.91955 | -57.5214 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0b8a21b3-ef6f-32e2-8631-2d47c861d520 | -14.94525 | -47.70775 | 2025-10-09 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7915c89-b93b-3a3c-8d0a-b106ceb7875b | -18.04512 | -57.52382 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d423040c-1b95-3e08-a684-afe3553ee30b | -14.84316 | -48.43808 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef2bd5e-aca1-3417-9fe0-b7346f20fd36 | -16.28304 | -47.14402 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d1bfe37-f940-34fe-9f47-7953afba3c63 | -16.37411 | -42.30487 | 2025-10-09 04:21:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 04ca84e6-4082-3272-8bd8-54573712a9e4 | -18.61359 | -43.31937 | 2025-10-09 04:21:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ea7ec1a-8e6e-33cc-af5d-e03a164ef6c1 | -17.5366 | -46.75355 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14468758-9c66-332d-9496-46a3636b6081 | -18.04104 | -44.70901 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f082e3a-73e0-3981-b820-238f6af97897 | -15.92385 | -43.29731 | 2025-10-09 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 96a12b3b-0165-3e48-bbed-c8c5c733bf48 | -18.92085 | -46.97464 | 2025-10-09 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cf7598b-4fc9-3a0e-847d-24532ab1e16e | -15.07279 | -46.61529 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 213c2a5a-fba0-348c-95a9-115f7d67d885 | -16.27311 | -47.14234 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b6c5f13-6a6e-3ca8-a6b2-13109b19b6ce | -15.3731 | -47.32974 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d6dd026-8a02-3300-97cc-9b57d6729b4a | -18.06425 | -57.54225 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 63ab6c0a-f4fe-388a-befb-74dc4f85c2e8 | -15.64194 | -40.8461 | 2025-10-09 04:21:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1382e26-8a58-3013-9676-a68c5f4bdeaa | -18.54459 | -45.07017 | 2025-10-09 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
