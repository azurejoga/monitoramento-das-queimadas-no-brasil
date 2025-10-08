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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc84e811-4dee-3106-b79f-32e1b08662b1 | -19.26212 | -44.12121 | 2025-10-08 04:40:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd6111e9-9a73-356f-a3f1-882b7cafd320 | -11.11777 | -54.05065 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e93afa25-9f19-38e2-8e64-08295a60b554 | -18.04877 | -44.45309 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2508098c-f3bb-3ec6-9f9c-d7ec1c058968 | -18.07073 | -44.46887 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05651a5e-a027-3f09-a8d0-ba47019b4366 | -14.10272 | -44.30526 | 2025-10-08 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dafaf685-0f65-3c6b-9314-6ccccf35b248 | -11.17041 | -54.87396 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7913a428-3c9c-3d5a-b980-1db0efd99925 | -15.39643 | -48.00543 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2de15832-8b9b-3bac-ab24-3b5a959da19b | -15.31371 | -46.17035 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db8f07d6-7a80-3aa9-a0c9-98d6921ab9d2 | -11.72585 | -50.93408 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8d3909eb-4b7c-3cdc-a0c9-f8cc29ed15f7 | -12.93888 | -46.86599 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d841b328-5a71-3ed8-94af-b0c8e6a47a6b | -13.26295 | -48.04924 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebf50b83-7281-35a9-91e9-6939a5f887fb | -11.33936 | -56.20678 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f873c6e8-c287-31f4-b50d-e4bac5657e7c | -17.30181 | -58.06525 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 20cb3896-cc39-39d7-89d3-2099db88c173 | -16.17959 | -51.7449 | 2025-10-08 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b5af030-be68-352a-978c-8e1c81ec5d9c | -12.00035 | -46.76664 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 617d767c-8a27-3b46-93fd-33eddcff7de5 | -15.08248 | -46.62162 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddfb4760-1825-328c-b550-d8037791c60d | -12.50431 | -54.71242 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3edcce72-c1f2-3baf-93df-42e0508c0a13 | -13.06247 | -47.93932 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12665440-33cb-3b5a-bb32-f3a073d0ce20 | -11.72743 | -50.96687 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7524d0d3-704c-3edc-a4d9-41584e591e77 | -11.38129 | -54.35085 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73179c51-f9f9-3c3e-9e9e-72443df3b45b | -11.69428 | -50.96143 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5754c24-6f50-31df-be2a-d1bb3e0ec0af | -13.29421 | -48.03381 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63757616-d600-3148-9c10-24b551628c6e | -17.15434 | -43.44071 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c111af87-b132-3e34-8917-b78fdcb10074 | -12.48846 | -54.71428 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa1b825-ff37-3950-8a23-5ecb77506699 | -14.95686 | -46.83643 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 976f4e79-fc9c-3042-b014-033d8b832176 | -11.1747 | -54.89524 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d074cc9f-8f5c-399e-84e6-fb9cd254c0ad | -13.06413 | -47.82794 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e15760df-3f02-3299-a019-3ea07bf74e46 | -12.1663 | -50.98438 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96056586-f883-3d03-8361-17e003afd281 | -14.74582 | -47.85823 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d637e2fe-0aa2-3b05-9dff-f4d2bdf837ab | -13.7275 | -45.70111 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb56072d-dcc7-3b4c-beb6-89834c22a3f7 | -11.7181 | -50.94004 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 984e2324-0174-3de4-844a-edb23c68e4d1 | -13.18047 | -53.83941 | 2025-10-08 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8454d2a8-8f01-3a51-b374-ef5844c95f6c | -15.1556 | -52.76306 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 859e188f-e78f-3574-880b-71d90f293ec3 | -12.58047 | -57.22382 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 137e868c-7daa-3870-bfb4-ac6adc9b556b | -12.93646 | -46.85625 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c69bf17c-d390-3c4b-bc37-3a95d2bc647c | -14.94871 | -46.80991 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1d32286-8353-3b02-b8e3-2f678b71dfa1 | -11.37755 | -54.35015 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bf71bc1-8a57-3523-bca7-15bb49a38ea5 | -10.67839 | -54.68921 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f686b6d5-07ba-3b66-871d-61389116cae4 | -12.48765 | -54.71893 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f82753d-f364-3537-9c22-e089b0ad4e47 | -12.946 | -46.84338 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fde4679-3ef5-3c41-94be-a894ebfbab77 | -11.67791 | -50.95885 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e3479b51-8061-352f-90e3-7b89a3e4ef82 | -14.52832 | -46.64202 | 2025-10-08 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22b37f0b-5f15-364a-aa07-d36d6caf8a08 | -11.17857 | -54.89597 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 702ecce5-3803-3ef3-977c-62ecf60d58d7 | -11.74354 | -50.92976 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 27662989-df3f-3ec5-ae0f-145a7268daea | -11.67292 | -50.96887 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4441f922-7900-3951-afd7-7f5dc9bcd070 | -11.1437 | -54.88968 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 872856d3-e6b9-3627-8b6c-d598ebc1ff16 | -12.16961 | -50.98492 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888862ce-0023-3d4f-9f5a-adbe1a82c9a3 | -14.82903 | -48.4229 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1370ea00-8756-3cfb-b3a6-0b5f06db6bee | -12.37562 | -50.30402 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a1541ad-9e81-3389-bb11-2872727a6683 | -11.13059 | -54.8908 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5835b47e-05cc-34c4-adc2-fb4bea04414b | -11.99533 | -46.77519 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| daf93fed-138a-3437-9a84-115a0bbf66a1 | -14.39464 | -46.0383 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9b0bea8-2fb8-34bc-aecd-bbfc392eb6c8 | -17.51374 | -44.99901 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0633808-292c-38d2-96a6-9c7bd141669f | -11.13292 | -54.88275 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8516c7a-ee6c-3f9d-b787-bbeace4f01ca | -13.22665 | -47.17021 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7a3a3ec-a83b-340b-b9b4-a09bd4f57c82 | -15.30572 | -46.16224 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 747aee7d-6fb9-3b87-85c8-197c58af37ba | -11.11407 | -54.05001 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b954a7b-64cd-32e8-8fd5-5a360d8cc895 | -10.86639 | -53.74038 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4dffd6d3-e948-3ce7-9754-ef34f56d85d0 | -11.71968 | -50.97283 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ec541f5-eddc-3ab5-97e7-10f4289936f6 | -13.38567 | -47.56707 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7881aa6f-5165-3fe3-abaf-c7c37a243cf1 | -11.44557 | -50.21481 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743ac255-006e-3f8f-ae08-21817022391e | -14.7157 | -46.02459 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 513f59ff-9850-39ad-8c52-8e0c1525aa9b | -11.13614 | -54.88163 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f357c66-cea3-3636-9933-0853467c21ec | -12.24674 | -47.86499 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fcf430c-d275-34ef-b568-6363887ee6af | -13.74749 | -48.6543 | 2025-10-08 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fe8a8b5-e09f-3172-b850-1e9783e4f213 | -12.3901 | -51.13666 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76af70ec-060e-330e-98f9-f53cf03d4b2d | -14.68885 | -48.41805 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 701fcb97-a146-386d-b14d-1af07aee1f00 | -12.5027 | -54.72169 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f841c5f0-7f56-3871-951a-6ef1c25acf5d | -14.71039 | -46.06429 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d9ae93d-0047-338f-b89a-4d95dfd18373 | -11.67236 | -50.97239 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dc78fc3-9a35-3b78-b81f-b3d45cac8892 | -11.71024 | -50.98936 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c80efc86-df6c-3314-a1f5-49a123332300 | -16.62638 | -45.42129 | 2025-10-08 04:40:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e227df63-b570-31e3-a9dd-a4c32ac0a68f | -13.69983 | -48.07293 | 2025-10-08 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2ae6cd-88c7-3973-bfeb-715d0b8802dc | -18.06598 | -44.46868 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 513c20b2-95a9-350b-8e04-86e80281c118 | -11.45716 | -50.20588 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8882020-375d-37ab-aadc-0f5cd6e0839e | -14.25274 | -45.86005 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13b86dad-552d-36c1-8b2d-4faa0c5264c1 | -14.5322 | -46.64257 | 2025-10-08 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac15e514-1adf-31fc-b54e-a6e258e52f9a | -13.25502 | -47.61471 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 665240b7-ed80-3c60-917a-4867559b166f | -11.15878 | -54.872 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f41d028-fa6b-3beb-8888-e8ce7a538c7c | -17.29597 | -58.07277 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2b8ed41a-945f-3087-bd01-c83503a7911c | -12.51103 | -54.7184 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2227ba0-613b-356e-9cd1-aca8b71b5d2f | -12.43976 | -54.22011 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35fea6b0-2906-38d5-94af-102f3d8e5cb4 | -11.69816 | -50.95845 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8cdf92ee-445b-3592-aa93-646a7ea540fc | -13.07003 | -43.59123 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d8d96d1-a67b-36f6-946f-9843fc9605e7 | -12.31118 | -54.11386 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8aca5850-72af-320d-a822-168146b9bc4c | -12.30174 | -55.1048 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24efcf11-40f3-305f-98ab-26c23a07a30b | -15.19391 | -56.81551 | 2025-10-08 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a518c2da-4290-3f7e-acff-b75e3830d8b7 | -11.74079 | -50.9257 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 2c563df0-8fcc-3eba-afec-810a1ec38a25 | -18.02189 | -44.31348 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3170feea-d838-3051-aa63-fc7d3a6aaf1b | -13.37067 | -47.22605 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c916bca-30e3-3375-b7e9-0eaeb0576b29 | -11.74074 | -50.94737 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ae23aac8-f970-320f-86c1-514c31750f2b | -15.61716 | -52.5803 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 447980fd-3127-3e49-a275-ede2dd3d1937 | -15.1213 | -52.76088 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35f74dbf-9508-3fba-98fc-d8ad19eb5e61 | -11.72086 | -50.9441 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 14d91977-a8ba-3445-8f86-30435e9cdf2d | -14.74518 | -47.86264 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b996a0f-e7bc-38a3-a32b-2ea3e22ce27b | -14.71444 | -46.06475 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64758d44-1c22-3c11-87ef-358c8e3c9f5e | -13.0601 | -47.95554 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9751c5a-e28f-3d5f-a2a8-efa6cf742320 | -15.60986 | -52.58284 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69abec36-9572-327d-83cd-2fc4fa9189be | -11.94434 | -51.47861 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e73ae4f-88be-348d-acb6-c80ebe0a548d | -17.45564 | -43.38861 | 2025-10-08 04:40:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README85.md)
