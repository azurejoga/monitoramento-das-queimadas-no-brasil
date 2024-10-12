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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d42e9b-2bfd-3087-976f-6b07946d6896 | -3.9396 | -46.4229 | 2024-10-12 02:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 25cb3e29-27cd-3487-ad5a-9fe890e56e16 | -3.9581 | -46.422 | 2024-10-12 02:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| aa890b92-6287-3fdd-8c4d-cacfe6c54c4a | -4.1148 | -48.2515 | 2024-10-12 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8b0a388f-5a73-30fb-b3a1-9b8fbe042666 | -4.7188 | -60.7882 | 2024-10-12 02:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 69317c92-079e-3ad1-a2a2-3e26270b5061 | -4.8562 | -45.6838 | 2024-10-12 02:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| d61a4e82-8075-3e89-a979-31043ede69bd | -6.0791 | -44.6276 | 2024-10-12 02:15:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ac367138-4f02-30dc-b1db-cb03ce96cb89 | -6.7469 | -59.3452 | 2024-10-12 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e56b48a2-e8b4-33da-8b37-165dc4e9f6d5 | -6.747 | -59.3259 | 2024-10-12 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 7331a5fb-a833-3ea2-a2e0-0db5c34b0f55 | -7.3105 | -64.6671 | 2024-10-12 02:15:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 392561c8-d896-3387-8e25-678e20a560a1 | -7.292 | -64.6676 | 2024-10-12 02:15:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 25139548-5813-3a56-bb36-38d293af4a37 | -8.4417 | -55.4692 | 2024-10-12 02:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ac468209-55f0-33e9-bcc3-e01c10a123a2 | -8.4233 | -55.4503 | 2024-10-12 02:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 428d6971-b391-3bab-be32-186e65b2124d | -8.4231 | -55.4704 | 2024-10-12 02:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 702edfc6-e65b-3e54-8cf9-5f5a99e4079c | -9.577 | -55.7932 | 2024-10-12 02:16:01 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f6d04e1a-c6c1-3faf-a22e-7b563a1be474 | -9.5768 | -55.8133 | 2024-10-12 02:16:01 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a4a1f494-b970-3469-b896-f61ff4f907c9 | -10.4079 | -61.2685 | 2024-10-12 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| e8fe1687-8ff7-37b2-bbd0-42da2b2d9c60 | -10.3897 | -61.2118 | 2024-10-12 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a6f98d92-dce6-3d54-98cf-28599980a810 | -10.3892 | -61.2695 | 2024-10-12 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 04f37172-359d-32a5-98f5-d278ff4d0fc9 | -10.3708 | -61.232 | 2024-10-12 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 9c5bd1b2-d2eb-378f-b2c5-5d359cc96a08 | -10.9506 | -44.653 | 2024-10-12 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 2b1a449a-4dd0-392b-8473-f570fd9ba241 | -10.951 | -44.6298 | 2024-10-12 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 68448794-9081-366b-99fe-1997bb64154b | -10.9697 | -44.6504 | 2024-10-12 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2865862c-7c28-3777-8c09-9da2fbb7b745 | -11.2761 | -60.5038 | 2024-10-12 02:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a0cbe7f5-cb43-354b-86aa-05909ab7cbb2 | -11.5358 | -53.8645 | 2024-10-12 02:16:12 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 365108a9-a91a-32b1-bf3d-3cd1a2f55d04 | -11.8377 | -58.8445 | 2024-10-12 02:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1fcbcaea-7161-361a-a25f-d7426933e183 | -12.456 | -54.5554 | 2024-10-12 02:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| efffdfff-b83a-3aea-b6ab-024204528bb6 | -12.4558 | -54.576 | 2024-10-12 02:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2e42568f-257d-361c-960f-387db433c81e | -12.4367 | -54.5778 | 2024-10-12 02:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5bd84ac3-208f-3528-ae1a-f343e976d679 | -12.7871 | -44.8639 | 2024-10-12 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5a458184-e96b-305f-8f4e-2d84c638b934 | -12.7875 | -44.8406 | 2024-10-12 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e63ab108-04b1-3645-8078-c6741efd6120 | -12.806 | -44.8841 | 2024-10-12 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d93f33b8-ecee-38a4-8d90-e69890436050 | -12.8064 | -44.8608 | 2024-10-12 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| aa318e51-63bd-3481-a90a-6d6e3fd1cfb0 | -12.8069 | -44.8375 | 2024-10-12 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ee750083-58be-36bf-a9f2-07c6b36e979c | -17.0426 | -56.0333 | 2024-10-12 02:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 2085a881-ddff-3252-9917-b18d7a441c0f | -17.1761 | -57.4585 | 2024-10-12 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.6 |
| ed4632c4-ca32-3b81-aef7-434564f17a89 | -17.1758 | -57.479 | 2024-10-12 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| d80731c1-0c05-319e-9b2e-7b71ffe471d6 | -17.627 | -56.3318 | 2024-10-12 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 71ed5c0c-6783-3762-9f60-8eee1cbf7bf9 | -17.6467 | -56.3292 | 2024-10-12 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.5 |
| 1be6bcac-c255-3c6d-9d68-6e696b709c30 | -17.6471 | -56.3084 | 2024-10-12 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 603cb407-a749-385c-9f04-7130d1efa0b0 | -17.6478 | -56.2668 | 2024-10-12 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 9eb13176-7c80-3258-9b22-5cb5ed7b9072 | -17.6675 | -56.2643 | 2024-10-12 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 4b701272-078a-3ed5-a4b5-6fd071dcfb39 | -17.6679 | -56.2435 | 2024-10-12 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 74e2b531-ef04-30d7-bd34-c2a776c32931 | -17.964 | -57.3843 | 2024-10-12 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 5b13d270-0848-32e7-aeee-8b15542e8c73 | -17.9643 | -57.3637 | 2024-10-12 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 514f33b7-cbe4-3bff-932d-666bd1f7dc60 | -17.9837 | -57.3819 | 2024-10-12 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| dd1e719f-9d14-3f79-b244-d970105d9ad2 | -1.8793 | -54.4312 | 2024-10-12 02:25:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 01c8fc50-fa86-393b-b97e-bf717ba76b4e | -1.8977 | -54.4309 | 2024-10-12 02:25:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| aadd2cc0-62f2-3327-8d04-7b4187f3649d | -2.77 | -51.3829 | 2024-10-12 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a1bc5fb3-262e-3ff9-b5d0-5e1be19a1892 | -2.7701 | -51.3622 | 2024-10-12 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7815ddd8-29c0-3593-a677-8fee36e5ff4b | -2.7884 | -51.3825 | 2024-10-12 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 866dc2f2-1ff0-3273-89c1-79fc545c9527 | -2.7885 | -51.3618 | 2024-10-12 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 0e48b9fb-7217-3246-98f7-6740a5ec2af9 | -2.7983 | -54.0129 | 2024-10-12 02:25:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 22be7d1e-dc42-3119-85b5-bf51480b45f4 | -2.8254 | -51.3401 | 2024-10-12 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6bd39798-d325-3102-8483-5df15c5b845a | -2.8611 | -51.6699 | 2024-10-12 02:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ee932b1a-9058-324e-9432-50187011a3d0 | -3.2136 | -46.7843 | 2024-10-12 02:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ecd91afc-2f45-3c8f-b5d8-966a5e8cf7df | -3.6901 | -47.9234 | 2024-10-12 02:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 483379eb-a13e-3c96-90bd-04011b48cdec | -3.7086 | -47.9444 | 2024-10-12 02:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 110c5567-8c28-3f08-bcad-b134288612fc | -3.7087 | -47.9227 | 2024-10-12 02:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 7dd067cd-f3d1-35f1-a0e2-ebde5262ffe6 | -3.8167 | -52.3403 | 2024-10-12 02:25:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 04a63bd4-a26c-31f0-beef-97e9aa37986f | -3.9394 | -46.445 | 2024-10-12 02:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 2108b6dd-527c-3687-ad65-3ca02531966b | -3.9396 | -46.4229 | 2024-10-12 02:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 6822ad7f-76e1-31c3-8d68-b062fd593165 | -4.1148 | -48.2515 | 2024-10-12 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| ef295943-dec7-3ad0-a3dd-bdd0ee6996c6 | -4.7188 | -60.7882 | 2024-10-12 02:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bd746564-7b69-36a8-be81-4fffff8e9b20 | -4.8562 | -45.6838 | 2024-10-12 02:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 869c7a82-1a54-3bbe-8295-c1c1cbc6e1da | -6.747 | -59.3259 | 2024-10-12 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.0 |
| f428e35c-98a1-3fb4-93e3-e9cc024d0835 | -6.7469 | -59.3452 | 2024-10-12 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c35d207c-2f36-32f3-8b08-7c89d8e11293 | -6.7285 | -59.3267 | 2024-10-12 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1eeeb422-0685-3fe5-89c2-434739e4e3e4 | -7.292 | -64.6676 | 2024-10-12 02:25:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2240d277-30a4-3813-89f6-9d8c68f61df3 | -8.4417 | -55.4692 | 2024-10-12 02:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 020c996f-e5f2-3c2a-86d6-b3f35f8ca0ee | -8.4233 | -55.4503 | 2024-10-12 02:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 42119ed3-caad-3a98-aed5-aaa0ffa8ec53 | -8.4231 | -55.4704 | 2024-10-12 02:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b9250ba6-dce7-31ac-9f16-3b887ee725a1 | -10.3708 | -61.232 | 2024-10-12 02:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| b498b993-738e-3aa3-9f53-29d82afff673 | -10.9506 | -44.653 | 2024-10-12 02:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| bce7b73f-92fa-3576-b75e-2c2713d25d15 | -10.951 | -44.6298 | 2024-10-12 02:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dda348cd-a146-368c-a94a-e592ea264453 | -10.9697 | -44.6504 | 2024-10-12 02:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8199b477-acbc-3fa4-8dd7-e559f24025cc | -11.2761 | -60.5038 | 2024-10-12 02:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ff35392d-97d5-3935-ba54-87483c4d9de4 | -11.8377 | -58.8445 | 2024-10-12 02:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 01c764dd-a055-395e-a949-048a4def81d0 | -12.4558 | -54.576 | 2024-10-12 02:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0a3f3b44-00f9-3f79-a494-322db4632c5f | -12.437 | -54.5573 | 2024-10-12 02:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e36670a2-073c-376f-9123-52cfff145139 | -12.4367 | -54.5778 | 2024-10-12 02:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| bb1c7238-9e70-37d3-b623-9e5b791c5bf5 | -12.7866 | -44.8873 | 2024-10-12 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4f92c72e-2e15-3b44-8da6-6a713f8937fc | -12.7871 | -44.8639 | 2024-10-12 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 97bf64f4-6f23-388a-85a9-84fb540230fe | -12.7875 | -44.8406 | 2024-10-12 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 943604c2-928d-3588-ada6-6ac08b2cc86b | -12.8064 | -44.8608 | 2024-10-12 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| d297a805-1267-346f-b4de-5ac166c2b0f1 | -12.8069 | -44.8375 | 2024-10-12 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ab8e0e90-1ac7-338e-a184-3fa5f869b602 | -12.9655 | -53.5319 | 2024-10-12 02:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cb1ded42-b6ff-35c9-bf41-8e40cadf836c | -12.9464 | -53.5339 | 2024-10-12 02:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0a1adeeb-d11d-3f49-ab9c-cdf32be1b80a | -17.0426 | -56.0333 | 2024-10-12 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 5b38eff6-2a80-3f65-a7fc-23ce5a2bcde8 | -16.9805 | -57.4404 | 2024-10-12 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 4a66587c-ac4e-3c39-aa56-09a7bc510e97 | -16.9998 | -57.4586 | 2024-10-12 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| b0e65501-84d6-3349-9c6d-6c463bceac08 | -17.1761 | -57.4585 | 2024-10-12 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| e68750ed-6a07-3f7e-9c34-e434defbc725 | -17.1758 | -57.479 | 2024-10-12 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| d1cea1f7-0d6d-3910-aeae-aa148ae273dd | -17.627 | -56.3318 | 2024-10-12 02:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 8188d5a7-7b44-396a-9ccc-1963b201c97a | -17.6467 | -56.3292 | 2024-10-12 02:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.5 |
| ad0459f5-0b5e-3c38-ba31-f3b8c87b9315 | -17.6471 | -56.3084 | 2024-10-12 02:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| d212563f-c2fe-3f58-852a-0c47381d992c | -17.964 | -57.3843 | 2024-10-12 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 1bfd3858-ae11-3403-a4cb-3255c00f72b9 | -17.9643 | -57.3637 | 2024-10-12 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.3 |
| d3f43648-6c96-3436-8fb8-61e1a923b8a3 | -17.9837 | -57.3819 | 2024-10-12 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 9656425e-6642-3d64-9aa2-e84895952c77 | -17.9841 | -57.3612 | 2024-10-12 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 63258d3d-27a0-3c2d-af33-d93604871b9d | -1.8793 | -54.4312 | 2024-10-12 02:35:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |


[Clique aqui para ver as próximas entradas](README31.md)
