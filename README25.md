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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a040bb6-95ff-3ca3-916c-e7df8bf5cd6c | -13.48649 | -60.34956 | 2024-12-11 04:59:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a80bd5da-e09e-39b5-ad46-99675e0cc6b3 | -18.02275 | -52.98498 | 2024-12-11 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d71094a7-e0e5-36f6-9876-6a8e27f07e8b | -15.03202 | -56.2365 | 2024-12-11 04:59:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a0d9886-d8ef-391d-8ade-d56e82a3e8c1 | -12.53959 | -58.33799 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a8fadb2-6c22-3259-92a1-507843ba3f22 | -14.96755 | -44.40749 | 2024-12-11 04:59:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae43a84e-0bda-3d4b-87bd-ce85139b5f2b | -12.53655 | -57.73477 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 661fc8d1-2276-3b3f-80f3-b110bdea0953 | -11.6633 | -58.272 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 945c88f5-0d4e-3b30-8725-308a5e9379e6 | -12.54529 | -58.3473 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eb6416b6-3308-32ec-b369-b9f1f076ff35 | -14.97103 | -44.41116 | 2024-12-11 04:59:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b47966a1-0817-3f2f-af63-5d6bc0026025 | -12.24708 | -54.29083 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7407cf21-e81e-39a6-8582-213d6d2df921 | -12.5454 | -58.36814 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae36c4a3-db57-3a19-864f-ed1bb3581001 | -12.54063 | -57.73155 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b52bcac-bbd4-3ce3-be09-6542622b1b47 | -15.02479 | -57.6138 | 2024-12-11 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14b48da5-8ad4-3554-8bce-b1ba01589d69 | -14.28677 | -57.46612 | 2024-12-11 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4171f5be-bcf9-3f65-8d15-caabe97d7d1f | -12.54038 | -58.35477 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b8f88f1-9405-3463-a098-c536b62bb3f8 | -12.52784 | -58.34927 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7560197-ab90-3279-892e-a85ae955c8ba | -14.28459 | -57.45815 | 2024-12-11 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 453e655c-232e-3e21-84dd-75c1fc313e82 | -15.09214 | -59.63255 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28e8ccbf-3078-37c5-8932-92417e1ca20a | -15.02298 | -57.62493 | 2024-12-11 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83e3168d-dc76-324d-8248-aa5052088532 | -12.53501 | -57.72271 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23c7f00-34ee-374a-9804-5983c0606666 | -12.52906 | -58.35703 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17df633c-c795-39b4-8ba3-ace9241126f8 | -12.5589 | -57.70712 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6306a84-3a12-32ab-b8b5-4ec1aa308510 | -12.92076 | -55.05308 | 2024-12-11 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92677260-c1f3-3ac3-905b-34b295348d53 | -12.56378 | -58.36721 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 755b716e-6935-3abd-b394-07d842657bd5 | -12.53546 | -58.36227 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 48ee9755-488a-3392-9f2a-261d63ed1486 | -15.97396 | -57.16526 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded81053-6478-3f22-9bf8-faaef087970e | -15.97338 | -57.16889 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| accb800c-1012-3371-92fe-1a38806d1694 | -12.5389 | -58.34203 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d9be973b-14fc-3f3a-aecd-486116151b0e | -18.02338 | -52.98026 | 2024-12-11 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 569d12fd-8574-3ed7-a84f-df0e8c35a90e | -16.26749 | -59.5174 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cf8205e-d70e-3f76-b431-621496ae29c4 | -12.53426 | -58.35452 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9161fe92-3080-3d39-a24f-cfc949d0b202 | -15.92603 | -57.51244 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b3ebcdc-edb2-3fee-bcbb-41e4cd6326ff | -15.02813 | -56.23952 | 2024-12-11 04:59:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3bea478-0fb7-37e9-b518-cf9c9bebfcc3 | -12.56726 | -57.76376 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06b33813-c933-378c-9132-820c731a4dbc | -14.57025 | -56.7104 | 2024-12-11 04:59:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4fca361-a8f7-3c77-b604-011a65037c70 | -12.55385 | -58.36127 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54c25afb-d795-39bf-bc95-2cb3e6f300e9 | -12.54963 | -58.3647 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4dfc651d-9d3b-3863-ad98-136158d67cdb | -14.97329 | -44.41311 | 2024-12-11 04:59:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d807dbb2-a1bd-3cad-aa3f-5c1a74366dfe | -12.53615 | -58.35822 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5ca62ffc-9cac-3614-bfc8-f54497472b97 | -12.53044 | -58.34894 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7e5851c7-b9f0-3bc0-a522-28fbb7739408 | -14.967 | -44.41258 | 2024-12-11 04:59:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b612a3f2-6169-319e-8d1b-0c762f04e59b | -14.57359 | -56.71097 | 2024-12-11 04:59:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8496dc72-a0f0-3a8b-9586-13a39604e7b7 | -12.53138 | -58.34987 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 570163f0-8d2e-380c-9c9c-ad9b31fc558a | -12.53005 | -58.35797 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9b918e9-fb66-3578-8fed-3e51258a4737 | -12.55167 | -58.35261 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4f3aed6-5b8f-3fce-b52f-54cbbbaea05f | -12.53205 | -58.34583 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0bae32c9-694a-319e-8ba0-0279409ae09f | -12.53225 | -58.36671 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7088b0a3-98a2-3ab0-b739-52b963003091 | -12.53821 | -58.34608 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d2a5a7f5-796f-3d22-9583-70b020489f4a | -12.539 | -58.36288 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 11e153c6-79ab-33d6-9f59-346b5f1ea2d2 | -6.9161 | -43.4952 | 2024-12-11 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 0a725fce-3028-3c1e-b6d2-4a480ac853fd | -6.8972 | -43.4969 | 2024-12-11 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 71be1760-1df4-3204-ab69-4c6d1200860a | -6.897 | -43.5202 | 2024-12-11 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c88f5cce-7153-35af-8877-8b2fa3894398 | -6.9592 | -42.9994 | 2024-12-11 05:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 906e6094-fcec-32a4-9a14-a70e2e67c02e | -6.1368 | -42.5307 | 2024-12-11 05:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| dedd6c6f-d8a5-3146-a39a-2676c8138c9b | -12.6755 | -45.6672 | 2024-12-11 05:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b58f09a4-0921-3d34-9260-49647895f90a | -6.118 | -42.5323 | 2024-12-11 05:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| a2976258-a683-3b0e-8fc1-45c77cc22078 | -6.978 | -42.9977 | 2024-12-11 05:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| dd2c4d23-408b-3035-a55e-6eb1a738203f | 2.7444 | -60.6381 | 2024-12-11 05:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 87bf8dca-49df-3d32-a090-03884a4faf43 | 2.7627 | -60.6378 | 2024-12-11 05:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8093214f-56d3-3d0b-979d-a5633ab7d0ff | -6.9594 | -42.9759 | 2024-12-11 05:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| de643f5e-0a6f-3f9e-9f41-7359071cbc4a | -6.1366 | -42.5544 | 2024-12-11 05:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 21954210-1769-377f-a37b-96f55e359667 | -6.1178 | -42.5559 | 2024-12-11 05:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 26f0f619-690f-3310-8f07-258b4c996e94 | -25.57061 | -49.35538 | 2024-12-11 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61eedae9-b4ab-365c-a11f-d6df07b93dc3 | -25.57116 | -49.35178 | 2024-12-11 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5b9477c-790a-36b0-9d6e-765c88d62c09 | -18.53042 | -55.95152 | 2024-12-11 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2337b8cf-45a5-35fc-b3c5-61b4cee230d2 | -22.54175 | -48.81182 | 2024-12-11 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab941e1d-4eff-3974-be8a-1f39341eca54 | -25.57093 | -49.35187 | 2024-12-11 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5be037dc-762e-33be-a052-2a6458bf6684 | -22.53655 | -48.8112 | 2024-12-11 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6e963a45-fe51-39cb-a767-6e1101a9be83 | -18.01984 | -53.99807 | 2024-12-11 05:01:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c667149-f769-3567-8637-8436127e0dd9 | -30.16137 | -54.99772 | 2024-12-11 05:03:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 58d4f56f-0f10-3e15-a586-e9fa66d4ad0b | -30.16069 | -55.00334 | 2024-12-11 05:03:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 982cc6c3-2c80-3602-a05d-ab48bf84acd8 | -6.897 | -43.5202 | 2024-12-11 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b1c31342-a28b-398f-876c-2123c7b886aa | -6.9592 | -42.9994 | 2024-12-11 05:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| c693c600-8457-3a04-a879-ff85744e1e8d | -12.6755 | -45.6672 | 2024-12-11 05:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| fbee55f1-da89-3f7a-a0e3-acb77d36a5f7 | -6.978 | -42.9977 | 2024-12-11 05:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 909ebbd1-b596-37cf-9785-99efc5989cfc | -6.1366 | -42.5544 | 2024-12-11 05:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| ee639010-2322-3235-9a70-285db2aaed6e | -6.1368 | -42.5307 | 2024-12-11 05:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| f461fb8e-7828-3df7-acda-2ef4ac84a700 | -6.118 | -42.5323 | 2024-12-11 05:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 29bf1fa8-1774-33aa-bccd-68d1c431f08c | -6.9158 | -43.5185 | 2024-12-11 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a83bac83-7378-3f0d-9f8d-2c212d3dc509 | 2.7627 | -60.6378 | 2024-12-11 05:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 300fe0f4-9298-3bfb-a7bc-22dbe1e8e235 | -6.8972 | -43.4969 | 2024-12-11 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 8d2fec71-0f38-328b-897d-91fc66cf1856 | -6.9161 | -43.4952 | 2024-12-11 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c952448e-3b21-3571-a62b-5e2a6de3f6fb | 2.7454 | -60.64582 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93dfddbe-a8be-33e7-b040-e5ca632048a7 | 1.30489 | -60.41118 | 2024-12-11 05:18:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc38fb0-16d4-372f-8764-de5f8dc55bc5 | 1.30432 | -60.40752 | 2024-12-11 05:18:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837c465f-99ff-3249-a94f-9796b05b9191 | 2.74598 | -60.64965 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e153a890-5371-369e-b8bf-93f8e49888a3 | 2.75582 | -60.6442 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ae79c852-4047-30cc-a8f9-accd6d2519e2 | 2.75929 | -60.64367 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc836f3d-4b3a-374f-baf3-be6a4ed71fd6 | 2.73582 | -60.39939 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae573f7f-29fa-3887-be2d-2839c4cb88de | 1.30149 | -60.41171 | 2024-12-11 05:18:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 939b5615-8a85-3839-b924-9c5314b93970 | 3.20365 | -60.59374 | 2024-12-11 05:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23da298a-23ae-3fe2-a42f-d3f4f8a89899 | 2.75117 | -60.6371 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c3ec37d-7291-3569-b161-63c1e07035d2 | 2.74946 | -60.64911 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6a72c5b-d20d-334a-afbc-3ae6e9958e9d | 2.75406 | -60.63274 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5090530c-bee5-3660-b513-8ebbaf2553a3 | 2.57488 | -60.69452 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3459e9a-181c-3f02-bfb1-22f7c174199c | 2.7587 | -60.63985 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 746c11c6-c25f-3207-810f-9afdc83ba6ed | 2.73524 | -60.39565 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1093106-8c0b-36ba-a936-7d3bb9e1e792 | 2.74887 | -60.64528 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c52da4f9-44d3-3987-ae8c-fa014cdc1bf5 | 2.75811 | -60.63603 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 99a3b4b2-40e9-3cff-aa3d-6be5e78a7425 | 3.22788 | -61.19576 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README26.md)
