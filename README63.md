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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08db60be-feb2-302a-b24e-1a95d23faf62 | -12.2829 | -44.0568 | 2025-09-27 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| f6fa6a39-df7a-3eeb-bfe6-f68d9ffd13c2 | -7.7794 | -46.9371 | 2025-09-27 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 9c6ccee8-7a8a-3465-9705-64a922178ecb | -7.7792 | -46.9593 | 2025-09-27 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| a7fb84a4-9845-3d82-a7a7-6af223953ebb | -10.4025 | -48.1256 | 2025-09-27 12:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8a5c0a38-e177-32b5-81c2-52814a07cb77 | -10.0062 | -46.7081 | 2025-09-27 12:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 53761053-2708-35d9-a334-5a3624c9bd90 | -11.3642 | -45.0339 | 2025-09-27 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 5b818688-8587-3f6c-bd4c-50788f01a92c | -11.3646 | -45.0108 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 71c426f6-150a-3bdb-9730-8fdd42e972f1 | -8.822 | -46.2564 | 2025-09-27 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.7 |
| c75306e5-dc8a-3ccd-8ad0-cc65cabbaf2b | -11.4221 | -45.0025 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0634ca39-767d-395c-bcf4-1e6f13f3c66f | -11.6058 | -45.4364 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 5cd98e11-319a-3fac-ad96-cbea7998d5ae | -8.9778 | -44.4876 | 2025-09-27 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 708c14f5-312e-348c-8157-072dda10a203 | -11.4413 | -44.9998 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 78ef144e-a117-377a-9455-d01992e35f55 | -8.8409 | -46.2544 | 2025-09-27 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| fa772d0e-4bcb-36a2-9f08-915eb982d683 | -9.6159 | -47.5741 | 2025-09-27 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2d47fafb-acda-3d12-a9f8-c7e24c40ad82 | -20.59842 | -57.08673 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 627dac36-9e67-31b6-b81c-bc8e15af19b8 | -20.59381 | -57.0793 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 15a0b770-f0dc-3289-b012-d216c42af624 | -20.74151 | -57.77887 | 2025-09-27 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 45607847-ba52-37b6-b954-0e87b333e599 | -20.73 | -57.78855 | 2025-09-27 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| a3344248-25b8-30b2-ae6b-21b6228be378 | -21.90471 | -49.8607 | 2025-09-27 12:40:00 | TERRA_M-T | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.9 |
| fe6af1c9-c15b-3db9-b2a1-42cdddd511b6 | -20.57288 | -57.15216 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f3b3579-36a7-343a-ae17-39ebffa5d6ec | -21.09369 | -47.83952 | 2025-09-27 12:40:00 | TERRA_M-T | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 098179ab-6412-3398-a5fc-9ce23a6df9a7 | -21.09594 | -47.81707 | 2025-09-27 12:40:00 | TERRA_M-T | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| a53896c8-1d97-3802-9806-4150b67ac0f8 | -18.30721 | -57.09021 | 2025-09-27 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.7 |
| d9d8cf95-ffc6-3d30-81a0-bd27fc4e5a2a | -17.17115 | -56.4011 | 2025-09-27 12:40:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| d67533e5-658a-3e32-b0b8-e9a97b9d42dd | -20.51891 | -57.06641 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a28135ba-9a78-33c7-970a-93e574825b04 | -21.07063 | -44.96599 | 2025-09-27 12:40:00 | TERRA_M-T | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 583fa39f-3a06-39a4-955f-58dcf67514b2 | -18.29757 | -57.08855 | 2025-09-27 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 559f96a7-6176-38ca-8e74-ade2b6528400 | -21.89329 | -49.85921 | 2025-09-27 12:40:00 | TERRA_M-T | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 6826de66-03e9-3293-bb23-a39e0b439422 | -20.59216 | -57.08992 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 1e92417c-a7c6-3308-ac0e-1b5baec04f89 | -20.52059 | -57.05583 | 2025-09-27 12:40:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 87e03739-b08c-351c-afa0-cb44548b3c63 | -20.83593 | -49.42189 | 2025-09-27 12:40:00 | TERRA_M-T | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| bff9236c-bc1c-3e44-affd-59695aa0a504 | -18.18502 | -53.32502 | 2025-09-27 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7b9df617-48f6-3ac6-9fc1-ebb527d84898 | -20.73182 | -57.77714 | 2025-09-27 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 5fb0d8e8-d3a9-3958-95fd-18f0e6a7dae9 | -22.55889 | -53.01141 | 2025-09-27 12:42:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.8 |
| cc13d94e-1035-3749-ac1e-0e04834868ad | -22.56031 | -53.0006 | 2025-09-27 12:42:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 07cd5002-3f91-3d9a-88e1-ad70bd9a4a82 | -27.02262 | -52.1382 | 2025-09-27 12:42:00 | TERRA_M-T | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ee4ea5a0-498d-3a28-8805-40a93a4f24f8 | -28.79569 | -49.37972 | 2025-09-27 12:42:00 | TERRA_M-T | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| b8846a0e-26a9-3869-97a1-9541671c1124 | -22.16819 | -52.8973 | 2025-09-27 12:42:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 993d6f7e-072d-3b76-8e89-d1459d4f270f | -22.56513 | -53.00719 | 2025-09-27 12:42:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 9a14dcca-1b8c-3646-98be-36f170987c77 | -22.13714 | -50.02332 | 2025-09-27 12:42:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 237d2c57-b8c0-39a2-89bf-eee4b682ccdd | -22.56376 | -53.01801 | 2025-09-27 12:42:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| f8798ffb-628e-3934-86a8-81d9f3307fe9 | -28.79334 | -49.3851 | 2025-09-27 12:42:00 | TERRA_M-T | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 65507d10-80da-3bbc-b480-05b70c053e58 | -26.26153 | -52.82966 | 2025-09-27 12:42:00 | TERRA_M-T | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6df7e6bc-6f5c-338c-a9ba-91a0ced2f745 | -30.55771 | -52.69325 | 2025-09-27 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 11.4 |
| 398a8b8c-204d-393a-bcaa-dd2e3a8cb3ef | -30.56404 | -52.68787 | 2025-09-27 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 8.7 |
| 9e00dacb-3ea1-3b03-82c7-e407249837e5 | -30.56828 | -52.69499 | 2025-09-27 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| bac4f0e7-4bdf-353d-97a5-410902f5035c | -30.56239 | -52.7027 | 2025-09-27 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 19.6 |
| 7af16266-69b3-36c5-819d-126e23c8812e | -11.3642 | -45.0339 | 2025-09-27 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| d89a1b20-7134-3027-9949-55cbe139a257 | -11.4413 | -44.9998 | 2025-09-27 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2b145bd9-1b21-36cc-9f9d-0527e707b1b7 | -11.3451 | -45.0366 | 2025-09-27 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b3b516e1-f948-3fda-8959-09b06639ae4a | -11.6058 | -45.4364 | 2025-09-27 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 50840214-dc1f-3957-a224-bac9701e1670 | -12.2829 | -44.0568 | 2025-09-27 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 259a016c-488f-3f89-b23b-03e38912f341 | -15.5776 | -51.7007 | 2025-09-27 12:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0059a2d3-5912-3eee-bc4b-c632dbbcf21b | -6.8444 | -43.1745 | 2025-09-27 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 71dd0472-ae5f-3a87-b29a-8d2a85918935 | -7.7792 | -46.9593 | 2025-09-27 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 217418ad-5b8b-3135-8fda-955d6b6118b7 | -11.3646 | -45.0108 | 2025-09-27 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 0bb09e9e-7f6e-3cfa-9ca5-81de31feb6a9 | -7.5571 | -46.6906 | 2025-09-27 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4c76be1c-e1ef-362a-b97f-43f927ebe72f | -14.0807 | -48.8292 | 2025-09-27 12:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 861b44aa-7f46-32fa-952f-6bfb6f1f5872 | -8.822 | -46.2564 | 2025-09-27 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| a35cf171-b3a2-3f7b-b168-58e7a916032c | -7.5568 | -46.7128 | 2025-09-27 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7b2606cb-28de-3193-90ee-3e59534e4cbc | -11.3646 | -45.0108 | 2025-09-27 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f531d35a-29a3-3822-942f-7edf07efeb6d | -7.5568 | -46.7128 | 2025-09-27 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 91a7a36b-9e8a-36cc-82c7-0060d8199530 | -11.3451 | -45.0366 | 2025-09-27 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8b53567a-28ff-3ffa-a1f0-16cbf22a2bdd | -5.7588 | -42.7976 | 2025-09-27 13:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 44e5423a-fcc7-3537-8f10-1f3f54d6a6f6 | -12.2829 | -44.0568 | 2025-09-27 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 876fd92f-023a-33d3-9040-ed71ebd8e642 | -8.4827 | -47.8202 | 2025-09-27 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 471a4aab-4220-3eac-af91-9afd14378793 | -12.2636 | -44.0599 | 2025-09-27 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| edda95a7-a023-3501-9680-9c31601b55ff | -15.5776 | -51.7007 | 2025-09-27 13:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a9e56a49-cf6e-3aec-a559-2a167a294613 | -8.6439 | -44.0164 | 2025-09-27 13:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0e2d4755-748c-39ab-8f4f-bc983c53d9ea | -5.7961 | -42.8182 | 2025-09-27 13:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 024d6ae5-05b4-3257-ac65-1e04e932df96 | -11.6058 | -45.4364 | 2025-09-27 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| b610934c-2d99-3929-81ba-23dc1778d3b2 | -15.5772 | -51.7223 | 2025-09-27 13:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 87b616d3-bc5a-3204-98c1-165208bc11cd | -11.3642 | -45.0339 | 2025-09-27 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 4a244df5-ea17-3354-8dcd-c2b71d038921 | -11.4413 | -44.9998 | 2025-09-27 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f9896ae2-6124-3057-873e-f00dc48a8e87 | -9.3517 | -47.5801 | 2025-09-27 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7c559dd9-3659-3325-becd-a92a581f2744 | -5.8149 | -42.8167 | 2025-09-27 13:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 8e20a5a9-fb74-3886-b137-5913a2127c23 | -8.822 | -46.2564 | 2025-09-27 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 73a1ae46-21f6-3197-970a-1b7ead4e6b78 | -6.8444 | -43.1745 | 2025-09-27 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 0d41dd51-86b3-3050-bde2-f8bbbd21fd7f | -7.7794 | -46.9371 | 2025-09-27 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 347.8 |
| 4524219f-a1fc-34f1-8c1c-4fa3c5e72ba8 | -7.798 | -46.9576 | 2025-09-27 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 56ad6c5f-15a7-3754-a9f6-0c5b1d1bf591 | -7.7982 | -46.9354 | 2025-09-27 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| eba4fbfe-1aa5-350a-88ea-6668ca2645e4 | -11.3451 | -45.0366 | 2025-09-27 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| b1146ee2-aeed-3922-80e2-19ce425be165 | -8.6439 | -44.0164 | 2025-09-27 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| a141c120-6b44-326b-9e98-3d94406fbb96 | -9.3517 | -47.5801 | 2025-09-27 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1c4edccf-90a1-367e-9163-76569de37801 | -7.5568 | -46.7128 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 60536197-922d-301a-8c08-7df802ad109f | -11.3642 | -45.0339 | 2025-09-27 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 4e9927a0-e531-361b-8103-90ffa4226596 | -8.8226 | -46.2115 | 2025-09-27 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c900f5f4-2426-36df-9f88-224a42b13366 | -6.8444 | -43.1745 | 2025-09-27 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 5bb5a521-fc56-36aa-ac62-ba87dbb98c45 | -5.7961 | -42.8182 | 2025-09-27 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 89f6057c-b26d-3f66-9c18-2a7a05bff826 | -12.6495 | -51.6797 | 2025-09-27 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| be55afa0-ca80-3cc7-8484-d030580f23e3 | -7.798 | -46.9576 | 2025-09-27 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6dcc33e9-8ac1-3e4d-9a55-f50ab8c295b2 | -9.7383 | -48.3079 | 2025-09-27 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6362c488-a1ff-3c0f-836a-dc529a817e18 | -11.4413 | -44.9998 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 4651527c-5fd3-307b-a25c-cd59c9329b08 | -11.4221 | -45.0025 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c175eee5-8273-3190-adcb-062a44780dde | -7.3847 | -47.0378 | 2025-09-27 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1c422dcf-69d4-38b0-8a03-87b838852d8e | -5.4937 | -43.0761 | 2025-09-27 13:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f82a2086-09d4-3e01-9b3e-e3f541aca8d0 | -12.2632 | -44.0834 | 2025-09-27 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 45a484f0-70e4-3ab8-9175-decd7e55bfbd | -8.6628 | -44.0142 | 2025-09-27 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| db12d65a-7289-3fdc-9108-d3c940bb630c | -5.3693 | -42.3077 | 2025-09-27 13:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| cdae1216-1557-36e1-8e75-8f7e6858b33c | -11.4425 | -44.9303 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |


[Clique aqui para ver as próximas entradas](README64.md)
