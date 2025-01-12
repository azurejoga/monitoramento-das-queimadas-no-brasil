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
| 6651d673-d4e9-3d1a-91fb-a92d1c2d12af | -28.73645 | -55.84337 | 2025-01-12 03:49:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| a1d85b3d-2947-3620-ab9b-be5d88427fb4 | -28.73836 | -55.83665 | 2025-01-12 03:49:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| c6e61386-00b8-3909-b3ea-44197e20ccfe | -30.38727 | -56.17936 | 2025-01-12 03:49:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4c7b2103-8e14-345f-aea2-fd1694511f62 | 0.5563 | -59.6885 | 2025-01-12 03:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 16ab6426-05db-3d13-b559-7da278a05f36 | 0.5563 | -59.7076 | 2025-01-12 03:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 22384705-bd14-3cf8-afe9-4ac353d0f21d | 0.5563 | -59.7076 | 2025-01-12 04:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 02457ddc-068b-3fc1-8ed5-fcc82db186be | 0.5563 | -59.6885 | 2025-01-12 04:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 72e955e4-921f-3ba6-911c-0c664ee57e17 | 0.5563 | -59.7076 | 2025-01-12 04:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3bc7d2db-7ced-315f-aa76-c0b3fd69c297 | 0.5563 | -59.6885 | 2025-01-12 04:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 41c5b18c-2c31-3e79-ba57-5f497dd7b024 | -3.27163 | -43.51937 | 2025-01-12 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a956000-16a6-38ca-80e7-7bdb926200e1 | -4.46857 | -44.22223 | 2025-01-12 04:31:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5546bf4-9d7a-35d8-adaa-710eecbe8465 | -4.38496 | -42.60095 | 2025-01-12 04:31:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87b1692d-82f7-3504-b58b-affaaff8e395 | 1.11043 | -59.46016 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61d64449-9632-3711-b605-c9a02dfd33b3 | -3.82945 | -45.3619 | 2025-01-12 04:31:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c18afd3-0e92-34b3-81cd-13ddab83f3ca | -5.45094 | -39.44687 | 2025-01-12 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15ec22f0-742e-3efd-9a48-e0dd844707a2 | -3.87221 | -54.23117 | 2025-01-12 04:31:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56bbdcfc-eac9-3619-b660-0e2589bb7574 | -2.68955 | -42.76115 | 2025-01-12 04:31:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 203ce283-973c-3537-b410-7f63d1a8e887 | 1.11807 | -59.46217 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63c5579e-5aa9-356c-aebc-1072415634a6 | -5.44592 | -39.44615 | 2025-01-12 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b905322-8dce-3229-b72a-4015c0a7fa66 | 0.55922 | -59.68895 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| cb0e4e7d-8478-3201-b732-ff60c8ae2fb3 | -2.6857 | -42.76057 | 2025-01-12 04:31:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f61ce474-6a5e-3ede-b4ef-461b377ebef5 | 0.66069 | -59.66019 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bf749f0-ea81-3904-970d-8de37be306f2 | -3.44941 | -39.63718 | 2025-01-12 04:31:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5eb745e1-b97d-35d9-8c81-d9ddf995f470 | 0.5613 | -59.70214 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 3b4b07f5-4ddf-347a-9793-7d52d5cd71ef | 1.11736 | -59.45924 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| efe5a839-6c2d-3c41-af21-c32703b05667 | 0.56025 | -59.69548 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 94cb8a07-3e2f-3a01-9c53-e65041a2df11 | 1.125 | -59.46122 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86284071-664a-33f6-9ce3-8c0e32b2c179 | 0.55328 | -59.69648 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| b604fa89-32d2-36c3-afef-3e419e7815cb | 1.11114 | -59.46312 | 2025-01-12 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95a985bc-7a13-364d-8478-0affce082dba | -15.07978 | -48.94641 | 2025-01-12 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e3a6d04-6b1c-36d9-8965-4455a86516d0 | -26.08174 | -53.73267 | 2025-01-12 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 28ac3a03-0ec5-3c6b-90c0-268d49183d80 | -21.449 | -48.60962 | 2025-01-12 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ba0b97d2-a0c0-3595-9ee0-052105ede7a0 | -21.44489 | -48.61322 | 2025-01-12 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 346f2ba0-dd2b-3634-ab4f-611559d3bc82 | -21.56499 | -54.19715 | 2025-01-12 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f19b6479-cc47-3737-9370-de58acc414dd | -21.44548 | -48.60903 | 2025-01-12 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 26140250-5ea2-3e4a-8148-561758731cbc | -23.46181 | -51.8694 | 2025-01-12 04:38:00 | NOAA-21 | SARANDI | PARANÁ | Brasil | 4126256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58da1295-b19e-3a1b-b797-361076040d57 | 0.5563 | -59.6885 | 2025-01-12 04:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1385ee12-88ae-3443-a155-abc36a1dbe8c | 0.5563 | -59.7076 | 2025-01-12 04:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a706c02d-767b-32c4-bb4d-a193bff7021a | -29.95466 | -51.61678 | 2025-01-12 04:40:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e4b65eac-c7ac-3832-9552-c0bb90a5e016 | -30.39813 | -56.16466 | 2025-01-12 04:40:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| c4827d39-fd58-3c7c-8d8d-be1630dee693 | -30.83722 | -55.38962 | 2025-01-12 04:40:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| ef480018-4ae3-3b2d-95d4-86a207345066 | -30.24931 | -51.58619 | 2025-01-12 04:40:00 | NOAA-21 | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| d390dbb8-c090-3d2e-8165-67267f314fa7 | -30.83652 | -55.39375 | 2025-01-12 04:40:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 20b1f6b4-4f91-37d1-975b-3a192959c4a9 | -28.41557 | -54.97913 | 2025-01-12 04:40:00 | NOAA-21 | SÃO LUIZ GONZAGA | RIO GRANDE DO SUL | Brasil | 4318903 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4273f3c8-c799-378d-85ca-6e3dc2cb22dd | -28.73931 | -55.83991 | 2025-01-12 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 9d0e90fc-307a-3d2e-ad04-32e2d339dbb5 | -30.95947 | -53.07096 | 2025-01-12 04:40:00 | NOAA-21 | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 5963f99b-1b6c-35da-ae0d-7582f79c4cb6 | -30.15211 | -52.02586 | 2025-01-12 04:40:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 3f05a433-0768-3319-a630-740dbaf7363f | -28.73586 | -55.83915 | 2025-01-12 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 051702d1-95d6-3f77-bdcf-4331aee0ca15 | -30.24871 | -51.59044 | 2025-01-12 04:40:00 | NOAA-21 | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 3ff968e0-1dd7-3af2-bdbe-3cd173907db3 | -28.73855 | -55.84419 | 2025-01-12 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| 0cd6962d-8ba1-347f-b3ca-c591cef8cdc2 | -29.74558 | -53.88836 | 2025-01-12 04:40:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 24f177eb-91c2-3510-bbef-c73a87cb91e4 | -29.39083 | -54.75177 | 2025-01-12 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO SUL | RIO GRANDE DO SUL | Brasil | 4313037 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6af34744-5654-3149-b8b8-5a7dd91ce91d | -30.83387 | -55.38886 | 2025-01-12 04:40:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| c1864a9a-0bd0-3ee8-873b-6b968a8a4df3 | -28.74351 | -55.83638 | 2025-01-12 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 8e94589c-aad2-37d4-a720-8fd61fd4962f | 0.5563 | -59.6885 | 2025-01-12 04:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f0bff479-a8a4-3512-a829-c8874197ddc9 | 0.5563 | -59.7076 | 2025-01-12 04:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c7289599-60c2-30c9-a492-ddacbfb65018 | 0.55946 | -59.69219 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fa84eef4-86c5-3cad-a141-e9367c3d4c22 | 0.62059 | -60.62172 | 2025-01-12 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46d714cd-d2fa-3351-9f78-12a7e24c70ae | 1.94003 | -60.40584 | 2025-01-12 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56e31bc-547e-36aa-b9a5-498e0a6caa1c | 1.17282 | -60.50011 | 2025-01-12 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cbe06c4-130e-3a62-ab5f-a2e78eeebf70 | 0.55792 | -59.68855 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 017c37d1-9c12-3f6a-9a54-f7e2e465338c | 0.56323 | -59.69253 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 377956c8-0569-3261-bfa4-ff6813e8e91c | 0.85222 | -59.54079 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be94538-7514-33eb-acc4-2c2ca4c1947f | 0.66493 | -59.65981 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acbcbd4c-5262-3010-a000-f05284117f15 | 0.56006 | -59.70271 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 033caa53-a8f4-3be9-a4f9-442867a8cf88 | 0.56021 | -59.69688 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 0f87e0bf-1ae2-3018-949b-969b8c01493a | 1.94085 | -60.41114 | 2025-01-12 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2336f632-9e71-3f3d-8661-de97a3949743 | 1.11394 | -59.45751 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd2e3e47-637b-3bfc-b2e6-723e7c4df600 | 0.61569 | -59.75718 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de6219ce-e32f-30ce-b007-2bc9bf7624ea | 1.17366 | -60.50561 | 2025-01-12 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 854048a6-c9e7-387a-80b9-5831ba9441d7 | 1.17773 | -60.49936 | 2025-01-12 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32857dc0-49cd-395e-8483-88bcaa1fabae | 2.17552 | -60.04279 | 2025-01-12 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06437c9d-eeee-33bb-ba73-5dbe3e311894 | 0.66159 | -59.65818 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 184a5b19-9a4e-3de1-a7b7-c937d25f2352 | 0.56406 | -59.69147 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9de035c1-cc94-3f73-9faa-bb07d52598bd | 1.11923 | -59.46145 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ac18f7b5-5256-37ed-8354-f7dce9d09a9e | 0.5556 | -59.69759 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ea8c657f-bea6-3996-89c9-6d24af713c9b | 0.66032 | -59.66051 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0065467-6065-3b4f-bc82-ccacd89d0d56 | 1.93513 | -60.40685 | 2025-01-12 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86209e23-3f54-3c77-b40a-2c26312086d3 | 0.62192 | -60.62093 | 2025-01-12 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93dfc3d7-6862-3247-bdbe-9299a3978ea0 | 0.85295 | -59.54538 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac5f962-0c39-30ca-9b98-84cb401342db | 1.12381 | -59.46076 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8955b16f-6503-3de7-b4d0-ae9fc3984ecd | 0.55871 | -59.68751 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfda385f-6a31-38ba-8c52-166fa10885dc | 0.66459 | -59.67699 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59667e9b-a4c4-3ea6-8af2-369191272847 | 1.93598 | -60.41233 | 2025-01-12 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cc7bba9-707f-3230-9b96-112a6e7dd9bc | 0.56252 | -59.68781 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dbd02be-c811-3f5d-8aa1-d3b49b91bfa0 | 0.91211 | -60.39038 | 2025-01-12 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cde2b80-7eb2-3004-a0fe-b2bafc3ea7b1 | 0.67856 | -60.62879 | 2025-01-12 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab676f6-bbad-3693-bb59-0fc7219dcbf6 | 0.66619 | -59.65749 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4a2c5ff-8bb4-3e73-83c0-73440247c7be | 0.55863 | -59.69324 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cc6e60ac-a010-35bf-9ef5-7526e0b8b497 | 0.55934 | -59.69796 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 7b1e3938-f931-3df5-b243-707ec9e37e71 | 0.56395 | -59.69725 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| be8920a4-da44-329c-9a2e-9273472ae720 | 0.56331 | -59.68679 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66632895-653b-3a8e-a8a4-83fd52200995 | 0.56096 | -59.70162 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| f40d4e10-ae4a-3269-a007-96ad5e1416ac | 1.10937 | -59.4582 | 2025-01-12 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00150aad-8657-3398-a531-39a86ec3d96d | 0.68349 | -60.62804 | 2025-01-12 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03eb4699-1f1f-324d-87fc-c0c443fb0df7 | -4.03974 | -54.78989 | 2025-01-12 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40b97118-36a1-3a5e-ad74-ad305f21b5d7 | -4.04309 | -54.79042 | 2025-01-12 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca3a0994-9b10-318d-94c4-5053fb9a5640 | -1.3064 | -53.42075 | 2025-01-12 04:57:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8ddcb90-cb85-391c-9deb-dc1c851c741f | -15.07715 | -48.94522 | 2025-01-12 04:59:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2b57065-b72d-3c90-ba43-3926e870faa2 | 0.5563 | -59.7076 | 2025-01-12 05:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |


[Clique aqui para ver as próximas entradas](README3.md)
