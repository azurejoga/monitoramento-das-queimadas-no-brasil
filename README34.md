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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d65fd98d-be86-32a5-9361-b60a3114ab6c | -19.72593 | -45.41134 | 2024-10-15 04:06:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97b44cb-14c4-3988-adb5-6af0f99c0840 | -19.51414 | -45.86155 | 2024-10-15 04:06:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed69ead2-5fd3-3c07-b270-f1b3499a1bc8 | -20.00736 | -46.69548 | 2024-10-15 04:06:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ee927f-5acb-3898-97bc-bc1becf5629c | -20.00654 | -46.70006 | 2024-10-15 04:06:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd3df82d-7efe-36bf-8b04-8b4d575b782d | -10.3711 | -61.1935 | 2024-10-15 04:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 4b887377-6c34-3566-bf46-8ac305b08011 | -12.0799 | -50.275 | 2024-10-15 04:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 14ada949-5737-35b4-b195-b4d5233f640a | -12.0994 | -50.2512 | 2024-10-15 04:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 5021562e-6c1b-333a-8145-b5b8605308a9 | -12.1185 | -50.2489 | 2024-10-15 04:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e367b467-c1ae-319e-9ffb-38f48836031f | -12.515 | -63.263 | 2024-10-15 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f13f149c-e254-3d22-a212-8e7cc20e56e1 | -13.1287 | -62.3034 | 2024-10-15 04:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 019872c2-84aa-34c6-b274-1a7829872d23 | -13.1475 | -62.3215 | 2024-10-15 04:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 523b97d5-1a75-30b2-a1e4-dccba118cda3 | -13.9274 | -45.8091 | 2024-10-15 04:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| d5e6d4e0-d890-3eee-8586-e90b17f5be32 | -13.9075 | -45.8355 | 2024-10-15 04:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 2b897c5f-d12d-31d2-b000-341ac0a49c78 | -13.9079 | -45.8124 | 2024-10-15 04:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4490db33-c84d-3fcb-add5-86fe519d05b7 | -13.9269 | -45.8323 | 2024-10-15 04:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| c9f4340b-eae8-3a01-8259-a66c87287a1f | -19.541 | -56.9917 | 2024-10-15 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 10feeb71-ee74-3f6a-a1a9-b85971f02067 | -19.5414 | -56.9708 | 2024-10-15 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 2f966e1f-0417-3409-ac3c-52c0e73e8809 | -19.5611 | -56.989 | 2024-10-15 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| d5be153b-d834-3436-8164-d8c5c9209bed | -28.585 | -49.44164 | 2024-10-15 04:08:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c4c9103-24e9-3ad5-9813-e9ec66007875 | 1.0199 | -52.2162 | 2024-10-15 04:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e5bce160-c5c6-3746-9481-e49671ff1839 | 1.0016 | -52.2164 | 2024-10-15 04:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 13a8f76e-2fa0-319f-bc79-0d44c4aaf436 | -3.1099 | -54.2263 | 2024-10-15 04:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2820fefe-38e7-3546-968b-30f8bf43aae7 | -3.1283 | -54.2259 | 2024-10-15 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bb80b968-ddeb-3f84-b22c-ff7fc0ddaa94 | -3.908 | -42.402 | 2024-10-15 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 5b0c4380-a88e-3885-9fba-1247b835f941 | -3.9265 | -42.4246 | 2024-10-15 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 177.0 |
| dfd65a27-eb73-3102-86cb-c558dc83157b | -3.9267 | -42.401 | 2024-10-15 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 201.5 |
| 6931d6b2-bff2-32d0-badb-3b1a7efb7b64 | -6.5505 | -48.2408 | 2024-10-15 04:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4ee99356-bf74-364b-aede-e04443c48d29 | -6.5691 | -48.2395 | 2024-10-15 04:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 70b49fe5-7e42-3d99-bc52-22e3aed92e6d | -6.5693 | -48.2178 | 2024-10-15 04:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9761f4d5-c272-3df8-88fd-171153bebfef | -6.5878 | -48.2381 | 2024-10-15 04:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a2f8aaad-3b50-3cd6-af2a-fe39a6e61202 | -6.6701 | -49.4586 | 2024-10-15 04:15:44 | GOES-16 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 61faf300-10b8-3ac0-b3d7-ba00cab7d78d | -9.4556 | -44.1763 | 2024-10-15 04:15:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f3bd219c-0312-39be-a1ce-5983edc31940 | -10.3711 | -61.1935 | 2024-10-15 04:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| e3297625-68a2-3cfd-a6c4-2d6b520a7cb9 | -10.3713 | -61.1743 | 2024-10-15 04:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f0b39c31-551f-3d30-95c6-2c4589990464 | -11.5737 | -53.8609 | 2024-10-15 04:16:11 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0d638ca0-6816-3b14-8aa8-2dc75ba27546 | -12.0799 | -50.275 | 2024-10-15 04:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 7e3f842d-3738-377a-bd2e-c8286fb75b9f | -12.0994 | -50.2512 | 2024-10-15 04:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a16bd8d8-70ec-3a81-8549-d366937c7b3e | -12.1185 | -50.2489 | 2024-10-15 04:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6ca77168-8db2-367e-b0cc-996ea61271f5 | -12.515 | -63.263 | 2024-10-15 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7a588734-e58b-3033-8072-15198f15dfc2 | -13.1475 | -62.3215 | 2024-10-15 04:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6043252e-8bfb-32e5-96f8-8269728dee84 | -13.9075 | -45.8355 | 2024-10-15 04:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ad6b5029-448d-35ed-ae54-29eb9db28f41 | -13.9079 | -45.8124 | 2024-10-15 04:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 08634473-b00e-3bcb-8a15-dd0c47490c63 | -13.9269 | -45.8323 | 2024-10-15 04:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| aa8d8b6e-a7c4-3057-88b2-f94e7277d1ba | -13.9274 | -45.8091 | 2024-10-15 04:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c1650c88-36e9-3d1d-abdb-f76f9f221eb9 | -19.541 | -56.9917 | 2024-10-15 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 5fe3bf02-d830-313e-af6b-4b34c232f69f | -19.5611 | -56.989 | 2024-10-15 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| b9b06c8c-392e-3e03-a9de-63c14ad207b3 | -2.14315 | -47.99649 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee871c5-2f2a-395f-89c6-35bedff1f00b | -2.04015 | -48.03093 | 2024-10-15 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 502c1bbf-09bc-341a-af1e-fcdd99314be1 | -2.02275 | -47.55204 | 2024-10-15 04:23:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f983df46-25bf-3045-81dd-bea985412479 | -1.90905 | -47.88509 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6bc07d3-c42c-3c93-b52b-7b23786bfd03 | -1.90825 | -47.8839 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fefdee1-7df5-331b-ae76-b89c916c02ec | -1.87579 | -47.88798 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef64615-290b-3140-ab5b-4cf32071c19d | -1.87353 | -47.81017 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9e7c8da-172a-38e9-b03e-e1e317df856a | -1.8729 | -47.81413 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2266379-1f3c-3e43-99ab-6cfd0416ac61 | -1.86999 | -47.8096 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 014b98cd-415b-3007-bfbb-4888764e1958 | -1.86495 | -47.8414 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fc3cc46-1c44-30e3-b070-03d73753a7b2 | -1.86203 | -47.83684 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f863607d-c25d-37aa-8d4a-060135fa2a58 | -1.8614 | -47.84084 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd6d3909-a4d8-311a-b94d-b3a6def6cc33 | -1.86076 | -47.84483 | 2024-10-15 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ed0dfc75-ddcc-3539-bcb5-c81f73ea6c86 | -1.58834 | -48.0354 | 2024-10-15 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98221a34-6c23-32a9-8496-fccb97d5783e | -1.47324 | -47.16808 | 2024-10-15 04:23:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a690699-5423-3fd8-aa82-5f980bade2a8 | -1.17239 | -48.09306 | 2024-10-15 04:23:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0df10f5-5750-3e7c-b4b4-eeff6f2b84f9 | -3.46572 | -47.67179 | 2024-10-15 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f06a9d0-3cb1-3b88-b6ae-fd5b61f22afe | -3.16516 | -48.37182 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e42e962-eaa9-3577-8842-c686fc32d734 | -3.05294 | -47.96997 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3367c4be-53d4-3aa5-8c2c-1a448ede5912 | -2.9831 | -48.61985 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d297ced-8851-3442-9954-ae347466daa4 | -2.44844 | -48.67371 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6a3f681-e78c-34e4-bf0c-a5d4c7c3b7a8 | -2.44774 | -48.67801 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01e82fb7-779d-315f-b8a8-a732028128d1 | -2.40008 | -48.10985 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1637d3e1-3d31-36d7-b756-ac2d5f8a25cc | -2.38447 | -47.59431 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b844637d-bb31-3823-936d-105945ac03ec | -2.384 | -47.59094 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4b19c30-384f-35c7-9c79-106e13c067f7 | -2.3834 | -47.59478 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe6d630-7c50-3ebc-96a5-54ed07eb2ad9 | -2.38166 | -47.70089 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ed6db2-ebde-339b-b80c-e86f613a73f8 | -2.38103 | -47.70477 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7db8bd0-8d80-37e4-9535-c6d25f6bbc12 | -2.32972 | -48.55759 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d88717-1cc2-3b11-bae8-a2cbf5d590b4 | -2.32905 | -48.56182 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecece9a5-de35-37e7-b6ee-2f0a72c3ca3e | -2.32571 | -48.58312 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f896ecdf-1c49-332c-bc4b-e5a35c384073 | -2.32503 | -48.8611 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab263b35-d216-3fb0-aaee-49bef6bd84bd | -2.32204 | -48.58254 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dd54e66e-13fa-34b0-9c82-9c8f98c2a5cd | -2.29834 | -47.90587 | 2024-10-15 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9488d85-f64f-3f34-be46-f568330c9114 | -2.29204 | -48.13127 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64b409e5-83fd-3f3f-a7f3-c963b12bfa7d | -2.23724 | -48.01484 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b34f481-7235-321c-96f1-613692414d06 | -2.2366 | -48.01887 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e55dbd92-1701-3917-abc3-e2c1fea4d5d0 | -2.19722 | -48.35656 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81ab5acd-e82e-3bca-851b-6eb49fefb6f6 | -2.17961 | -48.82381 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42df755a-2ba2-3439-9839-a4a335b55274 | -2.15868 | -48.81143 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2825396e-4098-346d-8cef-93eb50a609cd | -2.15496 | -48.81084 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c17948c-545c-3527-9935-ae39686e61b9 | -2.15124 | -48.81026 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0598c26-394b-3c28-9d9e-32fa997d8f37 | -2.14683 | -48.81408 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 702035c6-6528-367f-bf5f-0c0f0efdbbe0 | -2.1431 | -48.8135 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07a4fe05-ab22-3e31-8b73-711b37d79afd | -2.85723 | -48.24284 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f068c3-d1be-3d0b-b6dc-34692cb31e60 | -2.78565 | -48.08415 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0152e72e-a083-3437-b39e-e251e589532f | -2.78501 | -48.08815 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80dbba03-b474-31dc-a9ca-b5be749ada6f | -2.78437 | -48.09216 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d95b440-5da1-3066-b91b-4ce15d46b603 | -2.75574 | -48.69327 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cd1db4a-62a4-3523-aeca-07e50447e28b | -2.75495 | -48.69127 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b1723c-697c-3be2-84e2-3de462a999cc | -2.69358 | -48.63528 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d138922c-f907-3739-a8f8-14bf9d3e9ddc | -2.68995 | -48.70473 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9a714fc-c1f8-33b8-a587-f5d430b01a58 | -2.68992 | -48.6347 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 348dcac8-178f-3f82-bdd6-06ea86993b28 | -2.64772 | -48.43062 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
