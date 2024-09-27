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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5159ea5-7560-3083-8f8d-10db56d9005a | -10.8729 | -57.4336 | 2024-09-27 00:06:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 159.9 |
| a2989e26-dfa2-398a-80c3-0abdb4288f81 | -10.8731 | -57.4137 | 2024-09-27 00:06:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e11d5769-87be-32b0-bf7c-c4fe686bd2ea | -10.9076 | -54.2709 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 3903f1bf-d8d6-3284-a0ba-0c71e13541f0 | -10.9078 | -54.2504 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| bb3db36c-e6f6-3147-87f8-5218292ba52d | -10.9264 | -54.2692 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 343.1 |
| 6788dded-e3fd-364c-8931-fc28dd6bb8bd | -10.9267 | -54.2488 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 436.0 |
| 7ef32327-72cb-3ccd-bbb9-523417e4442d | -10.9453 | -54.2676 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| bb97612a-c20d-3681-aebc-12aac4af4a2e | -10.9456 | -54.2471 | 2024-09-27 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| bed37bd5-d0ec-3303-b7e4-32fd5c2a9204 | -11.1219 | -50.8328 | 2024-09-27 00:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b57b5b55-af45-3bc6-8b6a-3b70968cd031 | -11.1409 | -50.8307 | 2024-09-27 00:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d813225a-6dd5-3cc9-ac00-d28b5751d28d | -11.2034 | -54.7752 | 2024-09-27 00:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 48f7c09a-b5fa-3fac-806b-2c7d75020dfa | -11.2036 | -54.7548 | 2024-09-27 00:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 7abe5786-722a-3199-8642-336e604ba32a | -11.2223 | -54.7735 | 2024-09-27 00:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 2c536c44-8b04-33c8-9bfa-3634481690a3 | -11.2412 | -54.7719 | 2024-09-27 00:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 4bb51aa4-e2f5-3d4e-a738-b105a9e71d34 | -11.5872 | -63.9596 | 2024-09-27 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| bea7e6f7-9f3b-32e0-b4c8-9759fb8da17d | -11.5874 | -63.9406 | 2024-09-27 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 884f2457-c06e-3599-afc4-bdd66260552a | -11.5891 | -63.6933 | 2024-09-27 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 04e2373e-935a-3049-bdca-c96b1f4fcaa2 | -11.606 | -63.9587 | 2024-09-27 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4f711c26-9a1b-3cd5-ac2b-356d00ef7fe1 | -11.6061 | -63.9397 | 2024-09-27 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e8ae9d83-b72e-34d8-9ea5-ba12f25513f6 | -12.1533 | -40.8694 | 2024-09-27 00:06:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 47a5dc1d-4362-3bf8-8e93-dcb6b930e89c | -12.1538 | -40.8445 | 2024-09-27 00:06:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| bf68fccf-c291-33b2-92b5-d87ece734398 | -12.1863 | -50.7981 | 2024-09-27 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 07db24b4-9b35-3acc-9753-64ffd8ea43fa | -12.1866 | -50.7767 | 2024-09-27 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 229.1 |
| fa5dbd6e-76d6-3fa5-a085-e13b19ce4c0c | -12.2053 | -50.7959 | 2024-09-27 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 22d4c015-787b-334d-826e-4a99fc708b35 | -12.2057 | -50.7745 | 2024-09-27 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e8277ff7-a2e9-3170-a0b3-8f04b38c2780 | -12.6633 | -54.6988 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| c222c2e9-b1cc-3734-afc0-ed710d32fd21 | -12.6636 | -54.6782 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| fda8bd6d-c4fa-355a-8262-b69192d3a1d9 | -12.6639 | -54.6577 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e24fa54d-044f-381c-80a0-156c351a0d46 | -12.6824 | -54.6968 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 5e66a554-cb08-3f08-bc5a-77652ee72f57 | -12.6826 | -54.6763 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| cdbb23ee-0912-355d-b15b-0bcd4f0c48ed | -12.6829 | -54.6558 | 2024-09-27 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2c7aaaad-6258-37f3-b0aa-9b66e298719d | -12.8437 | -54.0422 | 2024-09-27 00:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 7d4ab507-6c92-3c8c-8c65-2d59deba84dd | -12.844 | -54.0215 | 2024-09-27 00:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 4fdba87b-2ab2-3f86-95d6-1a53a0a36ddc | -12.8625 | -54.0609 | 2024-09-27 00:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f3454f7e-3ed0-35bb-b8ee-3f992876a02c | -12.8628 | -54.0402 | 2024-09-27 00:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 278.5 |
| 37e28933-dfe5-3a52-ac1f-b4932ea97399 | -12.8631 | -54.0195 | 2024-09-27 00:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| d305ee5e-6328-37b4-896a-60dcbfbe5e39 | -13.4413 | -44.0267 | 2024-09-27 00:06:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 163e6ce6-19a9-3b67-ad99-09b17cfcbe12 | -16.713 | -55.847 | 2024-09-27 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 14ed876e-0314-3c89-9ec5-1306bb70514b | -16.7133 | -55.8262 | 2024-09-27 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 9aaf3be6-aba8-3714-8c99-c81faa16a6dc | -16.7322 | -55.8653 | 2024-09-27 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 74507302-4b0e-37c4-b9ce-7de5aeeab690 | -16.7325 | -55.8445 | 2024-09-27 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 157.0 |
| aee4f822-e211-3496-ba1c-a12715385628 | -16.7329 | -55.8237 | 2024-09-27 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 8d1f5108-73ed-34a2-94dc-4639bcb83d64 | -19.378 | -42.5556 | 2024-09-27 00:06:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| e7faea09-a9b1-3e7f-805a-d1b9bec33533 | -19.6136 | -42.8159 | 2024-09-27 00:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 4a846b17-30f4-35fb-a835-6353091fe0b9 | -19.5266 | -47.8952 | 2024-09-27 00:06:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d4517fb8-21d5-3737-ba39-09dd0121d7e2 | -19.5272 | -47.872 | 2024-09-27 00:06:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8f7523ef-d18c-3302-aefa-1f347a7092bc | -21.078 | -49.1393 | 2024-09-27 00:07:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| f764ad7c-f586-39c3-9d6f-04b0d75eb98c | -21.098 | -49.1578 | 2024-09-27 00:07:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 163.2 |
| 0c8da0b0-9e2d-38fa-93cd-b4c23728ee99 | -21.0986 | -49.1347 | 2024-09-27 00:07:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 498.3 |
| 45348cfe-cb21-3339-ad6d-4c6e01f90023 | -21.0993 | -49.1115 | 2024-09-27 00:07:03 | GOES-16 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 190.2 |
| ef6fbce6-4c80-3b5a-8c86-394c96b951b3 | -21.1192 | -49.13 | 2024-09-27 00:07:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 175.1 |
| 15c9f1a9-1847-3ea6-964a-f3fd63295414 | -21.1199 | -49.1069 | 2024-09-27 00:07:03 | GOES-16 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| b869e6b9-7b5e-3dcf-b8b1-3c16aadde92b | -21.3016 | -49.2037 | 2024-09-27 00:07:04 | GOES-16 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 9399d247-7b13-3b37-a48f-dfdb7c514aa8 | -21.3108 | -48.879 | 2024-09-27 00:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 142.4 |
| ad9dfdf8-1e40-3176-881d-62432760958d | -21.3314 | -48.8742 | 2024-09-27 00:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 73b44886-f812-30a6-bda4-14389a8c5ef6 | -22.7433 | -44.8035 | 2024-09-27 00:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| debdaf78-8c49-3331-aa31-de42c033df91 | -22.7442 | -44.7785 | 2024-09-27 00:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 20e54695-2813-3434-8a57-ae2edd11ec6c | -23.5808 | -47.365 | 2024-09-27 00:07:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| 4de6cfe3-0727-3c77-8ae9-8d0d9d01ad45 | -23.5816 | -47.3408 | 2024-09-27 00:07:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.6 |
| 9ae69ba3-a7d5-3e72-9e6e-d5515c09afe9 | -1.7494 | -55.2495 | 2024-09-27 00:15:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4753d3c7-1e3a-31b1-bf6d-35e02f962509 | -1.7494 | -55.2297 | 2024-09-27 00:15:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e3b5f628-0e36-3229-9e1a-33ec6ff79524 | -2.6783 | -57.5893 | 2024-09-27 00:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c846fba4-7f55-339b-a804-6564c0ac4e6c | -2.8611 | -51.6699 | 2024-09-27 00:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c73ae375-bd92-3fd9-98ce-a5ada9fd27d4 | -2.8795 | -51.6695 | 2024-09-27 00:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| d42af22c-a46d-3bce-89f1-be09da7c221f | -3.1134 | -59.1445 | 2024-09-27 00:15:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0169b6ee-9499-3c6d-b0b6-d56190428da6 | -3.1135 | -59.1253 | 2024-09-27 00:15:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| eec4206d-6cdf-3e34-b134-855fc242e828 | -3.1317 | -59.1441 | 2024-09-27 00:15:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4e0fae97-5398-3054-9864-cd538b4ced09 | -3.1318 | -59.125 | 2024-09-27 00:15:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 132e1d30-afa6-3480-b7f8-2da54814f26a | -3.6437 | -54.051 | 2024-09-27 00:15:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 45d16fad-5827-32a0-85d3-74369baa9266 | -3.6438 | -54.0309 | 2024-09-27 00:15:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4ed43ef1-df77-341b-b9c4-928d6fe0a5fa | -4.5616 | -47.9925 | 2024-09-27 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 09968f72-86ea-3409-b48f-3482e101267d | -5.0199 | -43.7839 | 2024-09-27 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3310c23e-176e-38fc-837f-45eb17dac118 | -5.2497 | -45.4348 | 2024-09-27 00:15:36 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 81b885ec-82e8-33ab-8dea-6cb2de07bcdd | -5.5888 | -42.9282 | 2024-09-27 00:15:38 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| e402ce5e-13c8-31fc-951d-775fb468932b | -5.7549 | -63.1384 | 2024-09-27 00:15:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a8dcbd28-f0ba-3b5d-b382-309f3c978373 | -6.8199 | -63.1651 | 2024-09-27 00:15:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| ff55e62a-f534-325c-93f5-785e552e52e1 | -6.82 | -63.1463 | 2024-09-27 00:15:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 22e1b868-8df5-30c6-8874-a2b11333a5ca | -6.8383 | -63.1645 | 2024-09-27 00:15:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 813a549e-7479-3190-8601-3614e8bd45b1 | -6.8384 | -63.1457 | 2024-09-27 00:15:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5531eb44-9541-3aec-9f5b-00ed43d8db39 | -6.8927 | -59.6475 | 2024-09-27 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 16dc58e1-8778-30e5-98c4-ede3b7dd942e | -7.2905 | -61.106 | 2024-09-27 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 41b0ea28-b281-307b-810b-7e32c84cbea2 | -7.2906 | -61.0869 | 2024-09-27 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fec9cc42-bdeb-3e03-82b8-56914e1490be | -7.3089 | -61.1053 | 2024-09-27 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 13f8a098-8915-3387-8c6b-93c6f76bef47 | -7.309 | -61.0862 | 2024-09-27 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cd7c206c-62ba-3a84-9293-ccefbeb43dca | -7.4605 | -60.4114 | 2024-09-27 00:15:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c9cf1c7e-fee9-3311-9844-70a7da2eda43 | -7.4606 | -60.3923 | 2024-09-27 00:15:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 4ca5bc40-251d-35aa-89bf-0cfbaa0000f6 | -7.5289 | -61.3825 | 2024-09-27 00:15:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 24a8fed0-ceeb-3637-b60f-2a3d06c0f65c | -7.529 | -61.3635 | 2024-09-27 00:15:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 38889515-9f17-3f35-ac91-13fa6fc6706a | -7.5474 | -61.3818 | 2024-09-27 00:15:50 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| bd25f41a-14eb-3499-925e-3faa6f68c41d | -7.5703 | -60.5984 | 2024-09-27 00:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 5c5e9e8d-cd76-349b-9773-b97fa342e6d4 | -7.5887 | -60.5976 | 2024-09-27 00:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| efcf2945-c2fe-3d14-b107-115d0883d428 | -7.5888 | -60.5785 | 2024-09-27 00:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a570d3f0-032b-3fcb-a046-e359e187cb93 | -7.77 | -61.2015 | 2024-09-27 00:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 84f67a1c-051b-34d6-bd12-3b625149ae1d | -7.7701 | -61.1825 | 2024-09-27 00:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 6c4ed611-7cad-357f-ab1d-98e32cce05af | -7.8156 | -54.7252 | 2024-09-27 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 9664a113-67b8-3629-bb0b-f1d42b4aa011 | -7.7885 | -61.2008 | 2024-09-27 00:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| ccdb037e-334a-36b5-b9b9-651a34f34a85 | -7.7886 | -61.1817 | 2024-09-27 00:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| ea243533-bb4d-30a6-94f6-ef672b8d6af9 | -7.9081 | -62.9976 | 2024-09-27 00:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4a5967f5-f5c7-3cde-9893-5d48a07f7c9d | -7.9082 | -62.9787 | 2024-09-27 00:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| dc33cdff-c451-3dc3-8de9-1ef255a434a5 | -7.9174 | -61.2909 | 2024-09-27 00:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |


[Clique aqui para ver as próximas entradas](README3.md)
