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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70513564-5418-3fbd-a695-ca95fac95c1c | -10.9971 | -50.2702 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b4deabd6-9f48-3797-a93a-26552174a404 | -12.1191 | -46.7279 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b58e084c-6176-3dd3-b2b2-ce1370983f76 | -12.0862 | -46.4162 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 295fea5e-6573-3410-a9b0-fce06c18e731 | -6.2857 | -40.8606 | 2025-10-24 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 126.6 |
| 41d3e3c4-858d-320c-87e8-48b78138dcb1 | -2.8645 | -50.7152 | 2025-10-24 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2df0a2f0-5e83-3785-bcb7-426f794154dc | -10.9041 | -50.1519 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d06a65da-d574-3356-bbef-c354b386621e | -11.1773 | -49.6051 | 2025-10-24 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 14b7024c-9ab8-30ae-bc51-b545388f1228 | -6.2498 | -46.3958 | 2025-10-24 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2655239a-3270-314e-8760-ccc595078e8c | -11.0222 | -49.8383 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 98dfd51d-e63d-30c5-9cac-1202bc1ddbc8 | -4.9122 | -43.2103 | 2025-10-24 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1e8f7042-2d19-3df8-82ac-0a76e7e60e07 | -13.9151 | -48.3889 | 2025-10-24 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ac859708-84d6-3a02-bbea-1e8dd40d240a | -14.3792 | -51.5255 | 2025-10-24 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 2d10acc6-b791-3ef5-b100-320a0e91d812 | -12.0666 | -46.4416 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f4d15a3e-624a-36ec-9d75-0326e7892224 | -11.0219 | -49.8598 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7c5eafde-5831-3163-b3b6-05ba90eecf9f | -19.0319 | -57.5382 | 2025-10-24 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 2048be54-8139-3019-9643-06eba7dc3e4a | -10.9399 | -50.2979 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| df478934-8d2d-3efa-be0d-0850bc73ef85 | -10.9586 | -50.3172 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1edcf0bb-19ab-302c-982b-6d76a1f3b9b7 | -11.1583 | -49.6073 | 2025-10-24 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e142f5d5-e8d1-369b-9eeb-8fa84e551853 | -12.8328 | -50.9552 | 2025-10-24 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c9446b1c-6ac0-3ff3-8072-0cf9893dc3c6 | -12.0858 | -46.4389 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e56befab-1e9e-3adb-a913-853c1c77367a | -6.9667 | -44.0246 | 2025-10-24 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 32e10fe9-3971-3d71-af13-05fa2a8e2c32 | -10.8854 | -50.1325 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 017728ba-870c-35a8-9cf7-94d1dc8c1d8e | -10.9047 | -50.109 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 553b5539-468e-3757-9a93-7d7d7b735cf2 | -12.1003 | -46.708 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| dcaef5ff-c19b-30a5-888c-e9ac1721a443 | -12.5574 | -43.7999 | 2025-10-24 14:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f00ed69e-e3ba-33d3-b791-98e054223bda | -13.8958 | -48.3919 | 2025-10-24 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c59d29a2-f5c9-34d0-81a9-a6620fc3300c | -12.0674 | -46.3962 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bf7661fd-55dd-332f-95f6-f82745fdf54d | -6.9479 | -44.0263 | 2025-10-24 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 656a3bcb-1308-362d-8b02-eeb45090e4d2 | -12.067 | -46.4189 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 76728195-12f2-3598-97f3-df654931a67e | -12.0478 | -46.4217 | 2025-10-24 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 69273d05-c0cd-3a7d-ab8e-ce7e57efed86 | -6.9291 | -44.028 | 2025-10-24 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 659bd7f9-b481-3c2a-abf3-24d5af287fef | -10.9396 | -50.3193 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 07cf0873-d9d9-3129-80a5-671bd6a5beda | -10.9044 | -50.1304 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a038f65a-a1fb-38f5-89cc-0c24c7263702 | -10.9399 | -50.2979 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 86433833-f3f1-3194-865e-fbfd88f543a5 | -6.9479 | -44.0263 | 2025-10-24 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f79ca720-2896-3b2e-9073-3f52efd4036d | -11.0406 | -49.8792 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a1e6bcbb-a70f-39ff-b943-e1e2b93ad96e | -5.7039 | -49.3066 | 2025-10-24 14:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ded8631a-ee9a-3bf2-82ce-ca3a0bfba683 | -12.1003 | -46.708 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 110e7a1b-30a3-3f22-90c9-f5814abc2b94 | -14.7456 | -46.6096 | 2025-10-24 14:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 2fef7526-a8d4-353b-bb89-c31ea98781aa | -12.8136 | -50.9576 | 2025-10-24 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1b33b4c3-88cb-3057-9519-c781680841c8 | -12.0478 | -46.4217 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1cb73f14-6c2c-3f7f-867a-ab62270ac12c | -6.9373 | -45.0134 | 2025-10-24 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 99ed7731-6b52-34c3-af17-809510bbfa18 | -12.8331 | -50.9338 | 2025-10-24 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 187b9d8e-73f8-3d2c-8105-e6cf69ef8afb | -10.9586 | -50.3172 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b1e553ea-7ef3-3ee1-becc-6f867aaa82fa | -11.0222 | -49.8383 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a5b3688e-263b-32f2-9e7f-42d0c383b709 | -10.9041 | -50.1519 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4932f509-20dd-318d-b612-561802efd5d2 | -17.335 | -55.0366 | 2025-10-24 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| de3c16ab-6217-34de-aa26-d2e3fce2599a | -12.1884 | -49.4404 | 2025-10-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| be2b2075-47af-3858-a1e6-a0c92362be1b | -12.067 | -46.4189 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| eec725ab-fb50-3e6a-9d83-3afc6f9a85b7 | -10.9396 | -50.3193 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 6c3914c1-b29a-321d-873c-c2fd2fab5e58 | -12.0674 | -46.3962 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 2d40f70a-2c85-3fe7-b413-07cb8e209b8f | -12.8328 | -50.9552 | 2025-10-24 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 172.9 |
| b2f5a294-7553-325e-875f-215f857412e1 | -13.8958 | -48.3919 | 2025-10-24 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ee27062d-cd1b-3a33-9b4b-17623fbb68ed | -17.3353 | -55.0156 | 2025-10-24 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 722b9575-60c9-3061-aeeb-5f56892786f3 | -10.9231 | -50.1498 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 71d3f3cc-4135-373e-87e9-f0c4dd440c58 | -19.0323 | -57.5174 | 2025-10-24 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| f3191169-16f0-3605-bcea-f49c15b3b559 | -10.9971 | -50.2702 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 32d40671-f116-3734-93e1-7a010755a78c | -12.0862 | -46.4162 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ffc00635-155b-38d4-ad10-2b7c7646c444 | -10.9044 | -50.1304 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3bb664a4-5984-3372-a9a8-9c467e7b71b1 | -14.7261 | -46.613 | 2025-10-24 14:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b4bfb4df-0c76-3ade-b869-2576cfd130eb | -10.921 | -50.2999 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4cee4401-cffa-3a3c-bb8b-405b33e2599f | -1.2085 | -49.0838 | 2025-10-24 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8e4e4322-462d-3b55-9fe8-dc0a08d2e29b | -10.9047 | -50.109 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 2c7f618d-08a0-33cd-9340-3061093548f5 | -14.9277 | -48.14 | 2025-10-24 14:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6b7a1b3e-c134-37ed-94d2-5a58cd9011ad | -6.8017 | -45.4332 | 2025-10-24 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 92e9a1fe-760c-3d0d-b988-5b241986cf89 | -10.8854 | -50.1325 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 6810a6cf-b0e5-3392-bede-f45654c82dc1 | -12.0666 | -46.4416 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| eefb075e-3285-339f-be94-83f759ad45a7 | -12.1191 | -46.7279 | 2025-10-24 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7cd25ae6-f6fb-32a8-94c4-955f359d9737 | -6.9291 | -44.028 | 2025-10-24 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fa914958-5564-38ee-89cf-d088ebba9894 | 1.4084 | -50.7868 | 2025-10-24 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 888763fc-5bf7-3553-bd92-f3fff3b3ddd9 | -5.6065 | -45.1852 | 2025-10-24 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| df711525-5de6-3bf0-a08d-acf2ae73e1c0 | -6.8015 | -45.4558 | 2025-10-24 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7b4fcf13-faea-3a82-8c52-1dce9535aeb5 | -12.1693 | -49.4428 | 2025-10-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 236.6 |
| a62e8648-5b63-3e5b-8bf2-d9e54e5a46dc | -19.0319 | -57.5382 | 2025-10-24 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| a0e1d1fd-56cf-3972-8a2d-ccad833c6570 | -6.2498 | -46.3958 | 2025-10-24 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 843b3361-6e79-3e01-af91-4237867153c8 | -14.3792 | -51.5255 | 2025-10-24 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e4e77d99-9cf7-358b-b459-c5bbb2b6ba3b | -13.9151 | -48.3889 | 2025-10-24 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3f2f57e0-9b13-372d-94ce-41e4a0271ed9 | -11.0219 | -49.8598 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| df167782-51ef-39eb-8291-e2be34d3c890 | -10.8857 | -50.111 | 2025-10-24 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 75d1d104-41e2-3373-be21-fcdcc3e18cdd | -14.4278 | -50.9605 | 2025-10-24 14:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| be0a5c9c-e9e4-33ec-9396-da2eba8b8466 | -14.4472 | -50.9578 | 2025-10-24 14:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2623e374-27aa-310f-b707-f1cdda4e2745 | -6.2498 | -46.3958 | 2025-10-24 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| ecfc484d-75ca-3253-881d-13a9c8c1fc31 | -19.0323 | -57.5174 | 2025-10-24 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| de144d2b-622f-332a-94e0-f968709e4cf2 | -12.7594 | -47.378 | 2025-10-24 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 08b32662-010b-3d9c-b833-a4fb468f3adf | -12.0674 | -46.3962 | 2025-10-24 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9f8871df-652b-3be1-8583-183ab70d79e3 | -12.0862 | -46.4162 | 2025-10-24 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| cf390837-f59a-3c56-99da-739695332f51 | -8.6334 | -44.8021 | 2025-10-24 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1910b494-7c9e-3f6e-9154-37fd58e22042 | -1.2086 | -49.0625 | 2025-10-24 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 6bd76137-9dad-3e85-a0fe-5611d7ea227a | -7.6373 | -44.5835 | 2025-10-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d5c5a0ac-b0b2-34a2-97dc-a77d7566192e | -5.7786 | -49.2595 | 2025-10-24 14:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2ccca706-7063-37ae-af2d-851971e80d47 | -6.0751 | -49.3908 | 2025-10-24 14:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 49cdf777-e90f-30d4-a0d0-ec626d8f83cb | -6.0752 | -49.3695 | 2025-10-24 14:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5a4c542e-5c08-39d6-8bf8-66ffd198e0c9 | -13.8958 | -48.3919 | 2025-10-24 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 14b623b0-258b-3195-ad0c-2acbb69cc5da | -6.9667 | -44.0246 | 2025-10-24 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 948cb929-9953-3cac-bdb2-3f15f1b96399 | -17.3353 | -55.0156 | 2025-10-24 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 09cb58ca-ee7c-3276-ae8b-c72275d198d3 | -14.3792 | -51.5255 | 2025-10-24 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 03d0b709-5ee8-384a-b618-cfcce7eaba26 | -12.0478 | -46.4217 | 2025-10-24 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| eb35c9c2-ce53-3073-9095-bdde8bbdea18 | -1.0981 | -48.8933 | 2025-10-24 14:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ddabe470-c592-3626-a2b7-b1cf3b39a2f5 | -6.1043 | -48.0979 | 2025-10-24 14:20:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4f6975b7-898c-37aa-a099-577ddad5040f | -13.9151 | -48.3889 | 2025-10-24 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |


[Clique aqui para ver as próximas entradas](README62.md)
