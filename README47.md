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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4164e5b-5199-3b5d-8596-f333f7be84d8 | -21.01049 | -57.83666 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2371aad0-b3b2-3661-b634-9666fa90ea36 | -15.64244 | -56.40173 | 2026-08-30 04:36:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 560bdc39-99b8-36e1-a769-8816da1f911f | -20.51208 | -49.04826 | 2026-08-30 04:36:00 | NOAA-20 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 587b882f-a4e7-3eb3-8e9b-e2a88f36a5fb | -19.08723 | -57.39795 | 2026-08-30 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 74a87ecf-4fe0-34e9-b5eb-f872bb1f2a33 | -17.8615 | -44.29437 | 2026-08-30 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 379a507e-7a99-34d3-9f26-1b173e737275 | -20.5565 | -47.59688 | 2026-08-30 04:36:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e44b062-6208-38fe-b404-6c968f887c09 | -21.03183 | -57.81059 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 34fad927-7169-36d9-8611-213674fe929f | -20.11486 | -48.27131 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fe260531-402f-39d4-b382-8d3e1c598fb4 | -18.82283 | -47.4588 | 2026-08-30 04:36:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bcbdfd2-18d0-33f5-91ac-e4b2c9f5d6e6 | -19.23423 | -46.73357 | 2026-08-30 04:36:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c06a3fb1-3045-3e17-9eb2-d2bc4f9bf205 | -23.20751 | -46.98081 | 2026-08-30 04:36:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 598e464d-49fc-33c2-bc34-797d64d44c6b | -23.39017 | -46.78589 | 2026-08-30 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b2f5f8e-833c-3a64-b3de-f6df5ab3923f | -22.19551 | -48.99561 | 2026-08-30 04:36:00 | NOAA-20 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61128669-8c06-313f-9c48-77aee0b8176c | -21.03293 | -57.80529 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 8dfbdb7d-3f16-3967-93dc-c586beb3de53 | -22.64848 | -47.67084 | 2026-08-30 04:36:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e300803e-3860-3fe6-af78-c8e04894c4dc | -23.15648 | -48.6689 | 2026-08-30 04:36:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddb0ac59-6126-3ada-83e8-4ac4c0144a30 | -19.87704 | -44.6146 | 2026-08-30 04:36:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 03bbfb1f-c231-3f29-a3b0-cc3404cb7a29 | -18.11228 | -42.87413 | 2026-08-30 04:36:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64a08cde-b498-3449-9660-f0083ff33b47 | -20.11823 | -48.27187 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5bd4e7c3-10dd-398f-97bf-5bcddaa025f8 | -20.10868 | -48.26637 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e4dd9c0-86eb-3fb3-b821-fe3f4b583b8d | -21.02273 | -57.83071 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f3469b1b-1be3-35b5-853d-778c1289ed47 | -21.60696 | -46.06821 | 2026-08-30 04:36:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| adb2875b-61cf-31af-82fd-351d71d551be | -18.52895 | -42.15423 | 2026-08-30 04:36:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e59f2809-8710-306c-adde-873008a59a5d | -22.31208 | -51.88784 | 2026-08-30 04:36:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f0ab9b9-070b-34c6-a1b6-db5be927099f | -21.00581 | -57.83555 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 253ad690-fd20-39e0-bdf3-3d42ac8d581f | -20.11205 | -48.26694 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26bd8e50-09a8-31d6-a64e-b6b0b5dfbd9f | -20.92801 | -46.03981 | 2026-08-30 04:36:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fed3f50d-075f-32d9-b48f-1a0bd4e20212 | -22.51278 | -46.0284 | 2026-08-30 04:36:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4396fba-bc4e-323c-a345-862f03ea4839 | -18.65822 | -46.8477 | 2026-08-30 04:36:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f75f7a7-37d9-3056-8380-72ce39c3c149 | -18.52378 | -42.15578 | 2026-08-30 04:36:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad24bcbe-2200-37cc-bfdf-2bf66ecab2f7 | -19.07777 | -57.39577 | 2026-08-30 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9fb9de04-928a-3455-9d72-eccb024c5205 | -19.84224 | -48.37869 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5ad0a9-f7ae-3f92-8326-3d186571f5f4 | -19.86938 | -46.3953 | 2026-08-30 04:36:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 132e437c-a6c7-3346-a8b6-bc3fdeb71aab | -15.88359 | -56.22254 | 2026-08-30 04:36:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b16ed2f1-fd17-3d80-be1d-f3d191adb398 | -18.5284 | -42.15902 | 2026-08-30 04:36:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 01a5f50e-e8c3-3f10-a3bf-5288af58e782 | -18.52833 | -42.15657 | 2026-08-30 04:36:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b19b531c-c3cc-3672-95ba-b2c8dab28c09 | -23.3548 | -47.69723 | 2026-08-30 04:36:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ab7c198c-087b-39ba-b18f-f47b90a29b6c | -19.86877 | -46.39964 | 2026-08-30 04:36:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfef0fbc-6409-3950-8e0c-06cac12e958d | -20.11766 | -48.27566 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 14f911eb-393e-3aa8-acf4-ff11eed566f0 | -18.6623 | -46.8442 | 2026-08-30 04:36:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 921bcdf5-792a-3f7b-8882-1d2e64c11a84 | -18.65763 | -46.85175 | 2026-08-30 04:36:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3078062d-14be-3982-ab69-b119e2a562cf | -18.46306 | -44.90046 | 2026-08-30 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19b3f60e-bc72-3a56-8c18-3cfca92daece | -20.11148 | -48.27074 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fc3effe-d638-3e5d-ad16-382c6667f9e6 | -17.53524 | -44.6133 | 2026-08-30 04:36:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af870847-a7a5-3f4c-b8e1-5e7f6b53451f | -19.09802 | -46.23949 | 2026-08-30 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0eadd412-7bbc-3700-8230-82aa6efa15ea | -18.87651 | -46.38277 | 2026-08-30 04:36:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ecc0346-cab8-37a6-8b35-93abd9ea91a5 | -18.4669 | -44.90098 | 2026-08-30 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3522d778-9b24-3cea-be41-ec9097f56f01 | -21.00645 | -57.83804 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| efbf08ca-4937-33ca-a019-115a415cf519 | -18.02792 | -49.20168 | 2026-08-30 04:36:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9eb7539-3c1b-32b0-9148-b5c958161061 | -21.52644 | -48.626 | 2026-08-30 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c5452bd-7a17-3521-a1b5-b6b8765717ec | -19.15097 | -44.8591 | 2026-08-30 04:36:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf1d6b90-6b61-3d98-b36b-ef4da1747f09 | -23.29928 | -45.62027 | 2026-08-30 04:36:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ed94099-0b37-386b-96b7-bb016bf72a8c | -19.74082 | -48.97208 | 2026-08-30 04:36:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a08c5d9b-537e-3c44-b489-9216fe3615c7 | -19.09196 | -57.39903 | 2026-08-30 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10f81c67-6faa-3a96-8688-7d2c9deb58d1 | -19.06154 | -46.22638 | 2026-08-30 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6ee371-b3bf-3275-be03-83adae7e5169 | -20.11429 | -48.27509 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 565bf653-b3bc-3cdf-9833-a57756e8231b | -25.62231 | -50.66975 | 2026-08-30 04:38:00 | NOAA-20 | REBOUÇAS | PARANÁ | Brasil | 4121505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45a50f0d-3a30-3616-8f77-1d5327165ada | -23.48193 | -47.29372 | 2026-08-30 04:38:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dab93d59-6a00-3f57-af0c-4ea787c9ca64 | -23.49449 | -47.17291 | 2026-08-30 04:38:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6faed1ba-e4e7-3868-8bbe-59c73aee8c8f | -23.49511 | -47.16825 | 2026-08-30 04:38:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eeb488cb-8e1d-316d-9511-ab616b8b82e5 | -23.82678 | -48.71953 | 2026-08-30 04:38:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e44b9eb-4a0f-3627-9087-4106dab5ba5f | -23.48252 | -47.28931 | 2026-08-30 04:38:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7906235d-331f-33ab-80d3-babae5dee2c9 | -24.28742 | -49.59838 | 2026-08-30 04:38:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f47fe3df-47fa-3a0b-8bb6-a7ab9591f856 | -23.49811 | -47.17345 | 2026-08-30 04:38:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e921ba26-3e3a-3850-b5b9-5867e747c52d | -22.01155 | -56.03046 | 2026-08-30 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06fab0df-1a4d-3245-a7fa-60a86ccb0b4b | -23.49701 | -47.58294 | 2026-08-30 04:38:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 93b065e6-93b6-3b1a-962e-76ebedaca87e | -5.871 | -57.7715 | 2026-08-30 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 406dd378-24fd-3838-9256-7bd924c934cd | -11.8021 | -51.0343 | 2026-08-30 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 37b25636-412b-31ca-a6c1-784f220fc04c | -11.8211 | -51.0322 | 2026-08-30 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e6fc59b8-e4c0-3acd-a22e-779d266764b1 | -9.8927 | -60.2752 | 2026-08-30 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1cf01db8-2427-3345-a4cb-7809e1cf8502 | -11.8208 | -51.0535 | 2026-08-30 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 881c000c-0655-3245-8b90-bc36d4f4d4a1 | -5.4876 | -57.1416 | 2026-08-30 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 290e84ca-acad-3d5f-9ec7-1813ef5d9ad8 | -11.8018 | -51.0556 | 2026-08-30 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| fb5ce091-1d6e-3c43-9102-36988de811db | -6.861 | -41.6772 | 2026-08-30 04:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 4d2d33dc-cc77-3504-84d8-5347504044a0 | -11.7831 | -51.0365 | 2026-08-30 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a4776bd6-ddf5-398e-906b-f0f678cf3365 | -4.9604 | -55.8424 | 2026-08-30 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| b739eef4-2501-3351-922a-63739be5dd9c | -11.7831 | -51.0365 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c9fdc222-a2c3-3ff4-a246-58a1b63a7221 | -6.861 | -41.6772 | 2026-08-30 04:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 44d02b20-1b70-3340-9f17-b94a443a720d | -11.8021 | -51.0343 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 98616aab-f7f3-356d-b4d0-fc0453e62967 | -11.8211 | -51.0322 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c2aee657-67fc-3523-9f28-bc4dcdd307aa | -11.7828 | -51.0578 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 5302c83a-ba46-3efe-a08c-94b4c0ed05da | -9.8927 | -60.2752 | 2026-08-30 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 348baf2c-48a7-344f-b1e0-f555849152b0 | -5.4876 | -57.1416 | 2026-08-30 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a8aef3d2-1891-3b64-8e16-a488e052b29d | -11.8208 | -51.0535 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2ab19d0e-51ce-3fe1-ad27-88b816be35d9 | -11.8018 | -51.0556 | 2026-08-30 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| d8d4dc7c-3955-37c0-ba2b-fc4ce47c0ddc | -4.9604 | -55.8424 | 2026-08-30 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 65df8318-dc52-333b-ab2f-c23a9f8a3c5f | -4.9604 | -55.8424 | 2026-08-30 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| b0e5432f-c1b0-3ce8-98f6-0480a7ad8025 | -9.8927 | -60.2752 | 2026-08-30 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 34aee6d0-b487-3a87-b37e-8c36c675c456 | -15.1314 | -50.6214 | 2026-08-30 05:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| faaad8ac-5c6f-3511-9b4f-ab9085de5275 | -11.8018 | -51.0556 | 2026-08-30 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6e215ec4-2426-3b80-87e6-baf6bbf18365 | -15.1509 | -50.6185 | 2026-08-30 05:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| dab03e53-d2ac-387f-91ee-b382b5afb108 | -11.7831 | -51.0365 | 2026-08-30 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c5a54e17-0f78-3ae7-bcbc-9edb3fe10056 | -5.4876 | -57.1416 | 2026-08-30 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b6d48f4d-5e41-3eec-b634-09bd1867abb5 | -11.8211 | -51.0322 | 2026-08-30 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 219fcb53-c343-3fa5-af62-623f2d934ba1 | -11.8021 | -51.0343 | 2026-08-30 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 5ddf18bb-fa2f-3998-b51c-7d67279314d3 | -5.871 | -57.7715 | 2026-08-30 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 58682c3e-9c46-3d80-821f-22e557663dbe | -5.4876 | -57.1416 | 2026-08-30 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 86d7dcee-2d55-3bff-a66d-7ed5984e7a4a | -4.9788 | -55.8417 | 2026-08-30 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| eecc84f4-75da-3f90-9836-dce01efa16da | -11.7831 | -51.0365 | 2026-08-30 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 60956ef6-7db0-397e-9d9a-68aa88cab533 | -9.8927 | -60.2752 | 2026-08-30 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |


[Clique aqui para ver as próximas entradas](README48.md)
