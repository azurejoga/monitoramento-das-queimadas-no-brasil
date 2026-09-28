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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad145a48-a8c7-3372-9f3c-541016f95da7 | -11.1771 | -44.8064 | 2026-09-28 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 503.7 |
| c5466724-96c8-343d-a06f-79042489ef7d | -17.2931 | -44.5157 | 2026-09-28 14:20:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 1f553488-bf03-3d05-b226-5df5ceea076a | -10.6035 | -49.9913 | 2026-09-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 79259d0e-6831-3ee1-b821-ce0e01b3e5c6 | -12.2699 | -50.3166 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9f19702c-8947-32ca-8a82-b13d585166ea | -11.3735 | -43.4209 | 2026-09-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 5edb09d3-31ca-3e7b-9090-82f088242057 | -11.5161 | -47.3703 | 2026-09-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0cdf19d8-312b-3371-865f-57dc77b6417c | -13.5911 | -51.458 | 2026-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7df9e213-dd7e-31ef-a811-efebdd07be67 | -12.7868 | -54.0275 | 2026-09-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0ed66df7-0fc7-3769-8033-d02aeb7650e4 | -11.7141 | -50.5538 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5d5bb715-234a-33e2-869d-38f0ce9f520f | -12.6836 | -47.3217 | 2026-09-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 5ee76038-d81a-3e84-b085-754867049297 | -9.7684 | -44.8312 | 2026-09-28 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 38558e40-daba-3e34-99db-cc90e078f129 | -7.6643 | -45.4925 | 2026-09-28 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| aa3671a5-2d1d-354e-a7e7-6fbb63201ec6 | -11.5625 | -50.5283 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d7ae6b12-aabe-322b-9a34-a652928004bb | 1.6749 | -55.9422 | 2026-09-28 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6206188c-1f1e-337d-afdc-3990c4ebdfe5 | -15.1847 | -46.141 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 037d09b4-34b5-386f-880b-364beb6f6ae2 | 1.6566 | -55.9227 | 2026-09-28 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 5da5bd25-9698-3ba0-8d7a-463ddcfbca59 | -12.1744 | -50.3282 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 076f1275-1beb-343c-a6aa-ca899a03018b | -8.2293 | -45.4375 | 2026-09-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ef62b154-bf34-3658-a404-be0c53eaf3dd | -11.3735 | -43.4209 | 2026-09-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e066da12-f8fc-325b-9d92-d5114cb03cd9 | -9.7684 | -44.8312 | 2026-09-28 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 213.1 |
| bb82aa06-79c3-31d9-933d-094e8f337bff | 1.6749 | -55.9619 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e501cbb3-25f4-3fbc-8cf4-160f776e33fd | -11.2158 | -44.7778 | 2026-09-28 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.0 |
| e0dd7045-0bcd-3e39-9167-341d39bcc24e | -12.8061 | -54.0048 | 2026-09-28 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d20a2a96-3b6d-3399-8960-55d855f2edf9 | -10.7343 | -48.7661 | 2026-09-28 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| be040607-aa87-35ca-af72-66f33939707b | -10.2067 | -49.9898 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 391306c1-be86-3e1e-86f1-5c536aca61ac | 1.6749 | -55.9422 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 51661ae4-db0a-3fff-b300-2d6b025600d1 | -10.8238 | -60.744 | 2026-09-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b926796b-3249-3713-95f1-4379e4c148ba | -12.7868 | -54.0275 | 2026-09-28 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| fdb3cf0d-ae03-3a2a-9911-97c852793e75 | -12.6836 | -47.3217 | 2026-09-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 791ef0fe-ca52-31cf-ba8e-7a2f994c0aaa | -8.5982 | -54.6341 | 2026-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f20f85b6-aa7d-3d26-b946-01c0343e42b2 | -7.468 | -44.5768 | 2026-09-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 9b506f80-c3f7-3f76-a6bb-8fd5da9818fd | -13.4205 | -51.3304 | 2026-09-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9cbd2a73-f12a-30bf-b783-b1727b75c1ff | -10.8723 | -54.0694 | 2026-09-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d99c8d82-b4e2-3f1b-8af4-8ad1bc5fe9c4 | -12.6878 | -45.0192 | 2026-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| aa81d230-8cdb-36ab-8630-85da09a480a7 | 1.6198 | -56.0216 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| ed5cbadb-61b8-3ab3-be7c-7f0fade6bc27 | -9.997 | -50.1607 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fbe4da88-c6c9-35ea-b9a3-d7f5fc1ea5ca | -12.155 | -50.352 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| bed35501-5a62-3f8f-a0c3-5693f17f693b | -10.4046 | -53.803 | 2026-09-28 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0385dc62-63f4-3c37-862f-76dc3d7db96b | -12.3088 | -50.2688 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 244.0 |
| faf33d08-a710-3b5e-a246-3a0a980cbf12 | -13.5911 | -51.458 | 2026-09-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| a820205c-c634-3270-9162-a8dd95f47584 | -11.1183 | -54.0062 | 2026-09-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c4a0b32d-45cf-3c79-b3b3-e785c910c216 | -13.1606 | -48.5658 | 2026-09-28 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 43f7eb86-513f-3ef5-a7b2-92cfa987a373 | -8.2807 | -54.7158 | 2026-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 7099ac83-97c3-3684-9638-8c681f8a70de | -10.7114 | -60.7505 | 2026-09-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6b62c369-5d75-3ee8-bca8-8c826a909956 | -12.289 | -50.3143 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 66c2a2ed-3702-3462-b9d0-9596f89a3040 | -12.2311 | -50.3643 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1bddb537-0f34-35ef-8ae1-72e3e8e7db5a | -10.7916 | -48.7377 | 2026-09-28 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 02cbc457-4a13-311f-bca9-320ef9560bee | -8.6171 | -54.6126 | 2026-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a9da072d-4490-3c06-970c-d5a256c5cd9a | -9.9266 | -60.7171 | 2026-09-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1e105228-1405-39f6-97a5-fddf9bbd04ff | -10.872 | -54.0899 | 2026-09-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9178d82d-74c1-34ad-8bc1-038833bdda10 | -12.2699 | -50.3166 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ba1ef08f-0012-3647-989b-a3a0d4390f57 | -9.9784 | -50.1412 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 317e44c1-c366-3f27-accc-260820958333 | 1.6566 | -55.903 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5fbd5f1a-b6d5-31cf-b327-739568c00468 | -7.4869 | -44.5751 | 2026-09-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f0aef04b-79fd-3b18-8574-0ca963f5045a | -11.0991 | -54.0285 | 2026-09-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 3c27593f-9244-3f81-ae31-8d9666de47b3 | -10.7115 | -60.7312 | 2026-09-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 452e5483-14b9-3cda-baeb-81c27a6df47c | -10.2154 | -53.9011 | 2026-09-28 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8978c33b-4d1b-35d7-9594-eca4dfc8b43e | -8.3608 | -45.4695 | 2026-09-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 2f085d59-cbf8-3539-85f6-81451ba96162 | -12.8658 | -44.7813 | 2026-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| c9fdcbc5-e6ff-3af2-a541-1470aff6adba | -11.1966 | -44.7805 | 2026-09-28 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 404.5 |
| a06fe73d-96fd-311a-bb8c-3c68c2c0d8db | -7.4974 | -55.0256 | 2026-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 94277e06-2feb-31b3-9c33-dd6ef93140da | -9.9781 | -50.1626 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6ce07035-f9f5-33b4-b196-edcf88f76c2c | -11.5628 | -50.5069 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 33d6f1b4-a234-3f41-a8fa-0f8b91acfb4d | -11.7647 | -50.996 | 2026-09-28 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 24e1614b-bd31-334d-8387-f33a40dd4ae8 | -10.6094 | -53.9902 | 2026-09-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 49d0090e-56f2-3aea-b484-4e508e516ead | -9.1871 | -45.7663 | 2026-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d2ad6feb-e59c-307a-aae1-f88aec43156a | -7.4492 | -44.5786 | 2026-09-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a17f47e8-3d3a-38b8-979d-9495b1b08dc3 | -12.3085 | -50.2904 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d22a02c5-af99-330e-b41b-d42742623d5a | -12.2508 | -50.3189 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 09a9c247-7620-39cb-864d-d7b6a356e3ef | -11.9622 | -50.5036 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6c836851-72b5-3952-b369-c30231fba209 | -9.1771 | -61.3882 | 2026-09-28 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| b7c7bcc1-a102-3266-8bfe-3e448c647d00 | -10.2827 | -49.9606 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 72d8105d-c18c-36c9-b09f-bd795d1cf695 | -15.1451 | -43.6088 | 2026-09-28 14:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 153.7 |
| 9de24a4e-dd60-3722-8d73-e8ca3d150d54 | -9.4513 | -45.8044 | 2026-09-28 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 41a93ec5-e95f-3d6c-838a-426cca097ad4 | -11.5818 | -50.5047 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| db9667c7-376c-3c48-b69a-40727f300ec9 | 1.6383 | -55.9033 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f8678fd6-89dd-3ba5-aa7e-55c559e47a4d | -11.1962 | -44.8037 | 2026-09-28 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 725.1 |
| 94325678-e7b0-3968-8976-b3ba7e58cc5e | -12.9112 | -52.0508 | 2026-09-28 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b8d638a6-2596-3cb2-90d1-8c7543f45cc8 | 1.6749 | -55.9225 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 6fa9b3c5-d05c-3d34-966f-bfe223f0824f | -15.1847 | -46.141 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 401a71f0-d8c7-3db9-b2ae-c3b7cbf77aef | -9.7874 | -44.8289 | 2026-09-28 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 32e2171e-2bf7-34a8-ad25-c6c80bc5f7c5 | -12.7223 | -50.6905 | 2026-09-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 71d4f882-e4c0-35f0-a2d1-ee1c614cba2e | -11.8641 | -47.1004 | 2026-09-28 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 2428b3ee-bdf3-393f-a4b6-831c19b5131c | -16.6424 | -48.4724 | 2026-09-28 14:30:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ba4ca19c-3e05-3f4a-a355-3260ea17b45a | -9.206 | -45.7642 | 2026-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 75c468ab-73a2-3580-b579-571145eb0830 | -9.9695 | -45.3336 | 2026-09-28 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 6f53c9e8-a06d-38b6-b8a5-7cd12c6e35c5 | -20.1966 | -48.5773 | 2026-09-28 14:30:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2a474753-9f37-3f15-bfb4-bd3fbfe5f7ab | -8.9633 | -44.1655 | 2026-09-28 14:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f4823d90-ed52-3418-84eb-1cbf403434bc | -11.1517 | -50.0603 | 2026-09-28 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0c3fda4f-7d8b-3eff-be2c-cbcb241ba24e | -11.077 | -51.3462 | 2026-09-28 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a8b5504f-0433-3f47-9fb1-dbc745c84460 | -11.5815 | -50.5261 | 2026-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 04d08c2c-4104-3228-afcc-60c102bc693a | 1.6566 | -55.9227 | 2026-09-28 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| a7324d14-6a8e-33bd-b1d0-17ae614995fd | -10.8187 | -57.2192 | 2026-09-28 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ef5a96d8-736c-347a-8a9a-c40f28c1ff40 | -10.4043 | -53.8236 | 2026-09-28 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1067e2df-6ae8-34ae-8c25-3056104c801c | -13.1803 | -48.5409 | 2026-09-28 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| ce9922bf-8776-318c-9482-c94df6b28190 | -11.2154 | -44.801 | 2026-09-28 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 407.2 |
| 14ee5c80-0508-370b-9b2e-652ed4deb504 | -8.2291 | -45.4602 | 2026-09-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| f6c1e681-3cfa-3bea-b65a-46afca73017c | -8.5984 | -54.6139 | 2026-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 9a2179e6-2095-3995-b5ec-41cd801aaf52 | -9.4999 | -46.385 | 2026-09-28 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 339c64f1-cbe6-3547-bfe9-db48e7ef9c4e | -11.3927 | -43.418 | 2026-09-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.2 |


[Clique aqui para ver as próximas entradas](README80.md)
