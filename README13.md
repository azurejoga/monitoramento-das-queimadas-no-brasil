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
| 0ca47fe7-6d77-30b4-9795-18d3656217c9 | -17.53558 | -53.71442 | 2025-07-26 04:06:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cacbb55b-f980-323a-8eba-1bfec2dcf97d | -14.37055 | -50.32857 | 2025-07-26 04:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a544e0b-1f63-3207-a9da-184d4e05cefa | -16.06276 | -43.64141 | 2025-07-26 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 749dc875-7c28-3ab6-ab6f-6f39c6b652f0 | -18.24667 | -44.7835 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 862f63f7-cd45-36d3-bcdd-e6ae30da82d9 | -15.26072 | -47.13759 | 2025-07-26 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edceb382-628c-32d5-9c92-74a131c5d84f | -15.1632 | -49.58038 | 2025-07-26 04:06:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7575c89a-1cd4-33c8-9fe2-da5102a6186e | -17.51184 | -47.99569 | 2025-07-26 04:06:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05fb654d-895c-3e61-bd23-48332277bca2 | -16.69195 | -41.0165 | 2025-07-26 04:06:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e558248e-6ea1-371c-8934-430ab14b29a8 | -18.17999 | -44.0351 | 2025-07-26 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36190c02-f575-3641-9c09-b73e63c0e8d5 | -14.95771 | -46.9662 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db1cec9b-ac4a-346f-a38a-0386544d84e3 | -16.098 | -42.27656 | 2025-07-26 04:06:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 3ef64e29-155f-37f0-83e2-d1cc52dd0c63 | -14.93177 | -46.94908 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c95b212-3fa0-3fb5-ae20-93e7e4e3a7d6 | -14.93243 | -46.94546 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b33feaed-95e2-3938-9162-3d5a0c32e6d3 | -19.97409 | -48.43163 | 2025-07-26 04:06:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71fd4122-7887-3926-8dac-b414b0a8666d | -14.96489 | -46.9724 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21067c59-fb3d-31fe-9ead-32846a888313 | -15.05254 | -46.50663 | 2025-07-26 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| becf29bc-8106-3e97-8f21-f2ea520cbae9 | -14.37559 | -50.32964 | 2025-07-26 04:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f3a9d3a-fd91-37f4-8915-07b4e7814ae2 | -17.7181 | -42.70546 | 2025-07-26 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 54612a14-c182-31b2-b360-2877bf088802 | -15.26544 | -47.1346 | 2025-07-26 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1560ef4-d22a-35d8-a813-af7fe3f213b7 | -16.12184 | -47.40509 | 2025-07-26 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8561f9a-55c8-34ec-a100-a8110c204c8e | -16.04966 | -43.72042 | 2025-07-26 04:06:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 02e85554-aaaf-3aee-8a51-933047a13dc8 | -19.97078 | -48.42702 | 2025-07-26 04:06:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22d97921-8e1b-397b-85b5-d331fb6e7f30 | -14.94338 | -46.95372 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72a28169-1caa-37d9-8b26-08c889108e03 | -16.5521 | -40.5075 | 2025-07-26 04:06:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3325fa50-ffcc-3330-9649-c0d75922ab39 | -18.24945 | -44.78805 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d43b81e5-cf3c-380a-ad04-9f557287d58c | -16.77941 | -42.5647 | 2025-07-26 04:06:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c9718d2-14e3-303a-89ab-b44d8bf3c3b1 | -14.93856 | -46.9574 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a9c6032b-23c5-38c9-a522-9eb080f8e2e3 | -15.78925 | -41.32994 | 2025-07-26 04:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b5189261-733a-3200-901b-2d34c142bcd0 | -15.72862 | -41.1531 | 2025-07-26 04:06:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0093958-58b9-3372-b899-df7a2cc89b2e | -18.17936 | -44.03894 | 2025-07-26 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92e226c3-c396-37b1-8cf7-5eeda2a750ea | -19.0117 | -46.13046 | 2025-07-26 04:06:00 | NPP-375D | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 749439e1-fd4b-3174-8c1a-47b63a2066da | -14.95737 | -46.99105 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c6ee680-51a7-35ed-9f91-09861bb33de6 | -14.94405 | -46.95002 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f9640d14-0e70-3cbb-92e8-a43d8b11472a | -15.14781 | -46.19238 | 2025-07-26 04:06:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff2240cf-95e4-3ba7-9e50-8e5561e514f2 | -14.93714 | -46.94241 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ca158b3-c2cf-3f76-94f5-650adfac47dd | -14.94203 | -46.96113 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ddc76576-d5ff-3bc2-9da2-4115e750a53f | -17.87157 | -39.66465 | 2025-07-26 04:06:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1207126d-01c6-3f9d-a47d-f781e83d5426 | -20.63979 | -42.90472 | 2025-07-26 04:06:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eaa80b10-5e78-374e-9312-ce7ffbdef757 | -14.93581 | -46.9497 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be0ceb9c-6fb9-3a2e-a83b-202f288c624a | -15.37276 | -44.28153 | 2025-07-26 04:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f59fdc8e-66bc-3f67-aad5-20e7e011a64a | -19.97482 | -48.42786 | 2025-07-26 04:06:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9bf406d-5196-38b7-80f5-443eaf5064ac | -14.96421 | -46.97617 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd265e3a-b488-38d5-bfcd-bfd1c62b75cd | -15.78313 | -41.32521 | 2025-07-26 04:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62d5092f-acfb-3ad0-8fb3-5a5357cd7de3 | -15.87306 | -43.28773 | 2025-07-26 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2f24ea3-bba1-3b1f-90c6-230d4e3c3cd9 | -14.93648 | -46.94604 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51305c52-b507-38ae-8c85-f540409eecbf | -14.95029 | -46.96133 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 673e9a75-eef7-3cd3-813e-f6f703193408 | -16.04627 | -43.71982 | 2025-07-26 04:06:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| aa46bd8e-8ff5-3de0-b329-9373737de707 | -14.94134 | -46.96489 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99f7ea42-3d9c-3d39-a6d3-71abdcf72539 | -16.29958 | -52.92464 | 2025-07-26 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d658979-da36-3484-8102-d1156731dff2 | -14.96205 | -46.98816 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dfec729-c42f-37f0-b86e-1dc35e28eca9 | -19.45088 | -41.6262 | 2025-07-26 04:06:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3b394a7d-9f70-3cf9-b32c-f00247e72565 | -14.93923 | -46.9537 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1083e42d-ee8d-31eb-b379-97affc3b8472 | -14.9475 | -46.95384 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82eb545b-d1e5-39d8-b37e-ccbe69dac611 | -18.25079 | -44.7802 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47954f19-dbad-3ced-a38b-d5eb37dd5732 | -14.9427 | -46.95743 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0ea28236-f015-36ce-bce6-e55a8898a767 | -20.62396 | -54.84187 | 2025-07-26 04:08:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7051990-106e-36e4-8870-28641beaa2d8 | -21.99776 | -57.61677 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6beadbbe-c2d8-38d5-8205-901b0ee8cd9c | -21.04734 | -46.3739 | 2025-07-26 04:08:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d9e08ac-2416-3205-99b5-87cc29dcce48 | -21.3874 | -48.67576 | 2025-07-26 04:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56f88540-438f-3d6b-9f7b-0683d0918f84 | -21.99118 | -57.60987 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c55ff3d-e6c5-382f-820c-3eb57fa7948c | -20.62503 | -54.8372 | 2025-07-26 04:08:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74ec90b4-bc5f-3157-95fb-73b75307c47f | -22.03854 | -47.93534 | 2025-07-26 04:08:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7e5cbbd-cab8-31ef-a883-7877daabcded | -21.99647 | -57.61732 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 44698616-2d6e-3932-ac93-4068f3a3dad9 | -21.99113 | -57.61477 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fa106f3a-ff40-3c4b-bb5c-6be78993ba27 | -21.39139 | -48.67662 | 2025-07-26 04:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262e9bc2-8241-32c8-9d0c-bf60ef144f6c | -21.99787 | -57.61165 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f79faf5b-0fd0-3d47-905f-4e7b56d146f8 | -21.98985 | -57.61524 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9edd0a11-b03f-391a-9f34-4f959e5f8293 | -21.9925 | -57.60936 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f199f2b2-4b06-36d3-9213-7ffd05a0d0f0 | -21.99922 | -57.61102 | 2025-07-26 04:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c28ceb8f-be98-3308-a1cc-51ab34e04e3f | -20.228 | -50.90311 | 2025-07-26 04:08:00 | NPP-375D | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a57950dc-36b9-352b-9211-6f7eda968d9a | -20.88729 | -51.39806 | 2025-07-26 04:08:00 | NPP-375D | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0db026b4-a98c-304c-9671-ead02d3b3f53 | -20.22843 | -50.90442 | 2025-07-26 04:08:00 | NPP-375D | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e0709e1-8b46-37e9-a6cf-59d80824da2f | -3.3957 | -47.5003 | 2025-07-26 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fc51f298-7505-3647-8dec-d687afc0dec1 | -30.12172 | -52.07656 | 2025-07-26 04:10:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 3e7de0d8-2e9f-38db-a55d-bc9621d43a00 | -30.12082 | -52.08094 | 2025-07-26 04:10:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 42124335-eedd-3119-8202-819d2b917927 | -9.3626 | -40.328 | 2025-07-26 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.3 |
| f84023e3-8992-37fe-98d0-a68bb8c2b34a | -18.2637 | -44.7961 | 2025-07-26 04:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 766b1a85-3308-3d86-86f2-78e2a1f2d136 | -9.363 | -40.3031 | 2025-07-26 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 655e8514-6338-3254-977e-7fd94b125c88 | -18.2644 | -44.772 | 2025-07-26 04:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c39ad748-e91e-316f-ae9b-aa93ba03143e | -18.2435 | -44.8008 | 2025-07-26 04:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 10470b47-1897-357c-9490-1bd57158f694 | -18.2442 | -44.7767 | 2025-07-26 04:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| bcca42a4-612c-31b1-a584-c44357541c79 | -3.3945 | -47.49047 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dd67c9d7-2064-3f8d-a4b8-0b39b76a30b7 | -3.39507 | -47.48682 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7501852-74b4-3a18-ad4c-82c7cf675212 | -3.04362 | -47.38341 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47551f93-f298-33a1-aca5-7cf4e684e935 | -2.98993 | -49.32133 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c9b1ced-7daa-3144-a666-40475610dd0e | -3.43536 | -43.14211 | 2025-07-26 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ce0f9c-1acb-3027-898b-e8a1da27317f | -2.28303 | -48.56341 | 2025-07-26 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e92fb621-9894-320f-91b8-a86b4c4d6ca7 | -4.03907 | -42.51327 | 2025-07-26 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b8a4c8c3-2229-3c60-9c04-713b41bc8d64 | -3.43153 | -43.13809 | 2025-07-26 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c64e5d3-6d95-3832-b6e2-842f355e44e1 | -3.11566 | -46.79981 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bf19a99-16de-376e-b80a-4d53fbb95ec6 | -2.63907 | -47.30217 | 2025-07-26 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6d01a29-cd6d-3e37-8e5a-10cd2a5c0b7e | -3.43185 | -43.14157 | 2025-07-26 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49d08e10-9c82-3d87-b17b-13f131d5bb77 | -3.82384 | -41.57062 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96b27c75-49f0-31a5-a7e3-1a56884b73a6 | -2.57413 | -49.10921 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 335d166e-10a6-3d56-9c79-c79535a01af3 | -3.12667 | -47.01205 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22530490-faeb-3c3e-8a51-8cc03e0e6881 | -3.81322 | -42.54639 | 2025-07-26 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bb153a2-d1c4-3a51-b07e-044c666e2841 | -4.0727 | -42.53853 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8e3ffb6f-65be-3fed-91d1-7ac5f0429644 | -2.90301 | -48.2445 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df8c8b0b-fa79-32b6-9da1-a944d9de10ab | -3.31056 | -48.7125 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89e71568-787a-3df8-8617-46ee01686292 | -3.04421 | -47.37973 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
