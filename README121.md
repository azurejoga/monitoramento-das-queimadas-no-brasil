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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84d8e1e9-8749-3629-952b-902290a8feca | -11.12031 | -49.60081 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db580df6-8238-38d2-9efc-c79ba44e5189 | -11.11974 | -49.60437 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbb20256-2450-337a-ae38-676ad8d494f5 | -11.11918 | -49.60793 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5d84570-2ec2-3672-934c-7ad6ce92a134 | -11.10019 | -49.61942 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1dfc6ee-feb8-3b9e-9575-492bac11cd16 | -11.09962 | -49.62298 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4bb823c-7ce3-3c94-bf8f-ae112cb22ac6 | -11.09685 | -49.61887 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f390ea31-0844-350e-a92e-85be475a5490 | -11.09628 | -49.62243 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d327536f-d0b6-3a55-ad04-d6ecec8641e5 | -11.08796 | -49.61011 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f40dcb3-bd51-3a5e-98c5-f643057a17fc | -11.08518 | -49.606 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23fda079-af86-3199-883e-671de78bbf9c | -11.08461 | -49.60956 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33a80d2e-dd55-3647-8296-fc60191b67f9 | -11.08184 | -49.60546 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2889bbe-502a-3c97-ba7e-fda3682efc08 | -11.08127 | -49.60902 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e660cd4-7847-3f3d-96e1-d6dc1d587637 | -11.00645 | -50.20254 | 2024-10-04 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ab348b4-6398-35e6-a9c6-0c5c855e604c | -10.97517 | -50.15992 | 2024-10-04 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 405d1961-18b8-3021-afb7-b971d804fd41 | -10.96166 | -50.15767 | 2024-10-04 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bc19647-a756-3066-805e-09d8851125cf | -11.34973 | -50.79914 | 2024-10-04 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c16c9178-2915-3c8f-8f44-79067b7dee3e | -13.63218 | -51.19891 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e85bf20-bc4a-3de7-943e-f0b21f7b383f | -13.62876 | -51.19832 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0834e701-2362-3e66-b44d-aa1f053e478c | -13.62721 | -51.18644 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 939a2d50-35cf-3372-a5f7-d5e8be8ac683 | -13.62659 | -51.1902 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d695b006-0d87-305e-a57c-346255d552fe | -13.62596 | -51.19397 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 758f2016-22a9-3554-ac77-553c8b9923ce | -13.62534 | -51.19773 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92de69bb-edef-3c9c-b496-0d8095c68e85 | -13.62472 | -51.2015 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b221118c-ef1a-332a-a81c-9c2e1670215e | -13.62441 | -51.18209 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9912155-7db4-33b2-a513-b9974ac32290 | -13.62379 | -51.18585 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4de620c-b766-3897-8f5a-2c2814bc39e8 | -13.62317 | -51.18961 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50287876-bb05-36e7-9d09-13eb61259393 | -13.62285 | -51.21282 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bfe3266-e43f-32e3-a322-cf505e9aad7c | -13.62255 | -51.19338 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba4d2246-e50a-3117-a03c-c1c7493b9495 | -13.62222 | -51.21659 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c79350ef-eed4-32c6-8fd6-337abf61bd42 | -13.62192 | -51.19715 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90bcf628-8e6a-3e8f-8374-e0319063dbad | -13.6216 | -51.22036 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b76cc562-6a2c-3c8d-b51d-81f302319e16 | -13.6213 | -51.20092 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 154822eb-66ab-371f-bc49-7ec9f5c07ef1 | -13.621 | -51.1815 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cc7d3e8-949b-34e0-b540-a16fc19bc815 | -13.62068 | -51.20469 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa2de016-0cd6-33cd-bdaf-a54527a8018a | -13.62038 | -51.18526 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e0259af-237f-3cad-a68e-673a9ea604f0 | -13.62005 | -51.20845 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15d62cb7-9cd4-391e-ba7d-7824b13e036c | -13.61975 | -51.18903 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffc3a1c4-ef49-3ff7-a22e-0d28f50ae028 | -13.61943 | -51.21223 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 645fc9ea-33b2-3035-be5a-fb3d752f6ec5 | -13.61913 | -51.19279 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f904434d-20e5-33c7-a07d-559eafbe9f11 | -13.6188 | -51.216 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f255e7d-6d0f-3915-b6c3-b20df585168a | -13.61851 | -51.19656 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| beeee46b-6320-3d08-a337-fa3f1d9fe611 | -13.61818 | -51.21978 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8e080e2-536d-3376-857b-85b9412043e0 | -13.61788 | -51.20033 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccbb7001-592d-31a9-bb6a-3ef1be6883b6 | -13.61726 | -51.20409 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 699b3978-1421-3359-9ce1-213ebe39087c | -13.61663 | -51.20787 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd6c3ef9-df75-3d20-ae19-da856abf25e0 | -13.61601 | -51.21164 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f66c1d-00b0-32f9-8612-ded720106da6 | -13.61539 | -51.21541 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 401e6ff1-1960-36e4-acc1-036201829d0f | -13.61476 | -51.21918 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7619e658-e892-3890-a8a1-44a452455594 | -13.61447 | -51.19974 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dec6ba61-06d7-36c0-b0ec-36499b7abbcb | -13.61384 | -51.2035 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88812255-5303-3b0b-996b-6dcd2d6680f7 | -13.61322 | -51.20728 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de9122a5-29ce-37ef-8029-658e29d99b9d | -13.61259 | -51.21104 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcdbde41-90ca-395f-94c4-5630ebb84fc9 | -13.61197 | -51.21482 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24c7b7f2-cb7d-36af-99ce-c79b4ce671d1 | -13.6098 | -51.20669 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a805f677-1e04-357f-9020-8ff51806c8ea | -16.09499 | -50.44098 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 374ad637-48fe-3926-8d66-5ffb33864239 | -13.60917 | -51.21046 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0b8df8f-aee5-3dc2-b5d3-62b913e8ef9e | -13.6073 | -51.22178 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0140a465-dd52-3ec1-8c81-d3c58869d929 | -13.60542 | -51.2331 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19809661-700f-3451-9ba6-441804721ca5 | -13.59988 | -51.16228 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a0b5885-b1e3-3e59-a445-228aed699b92 | -13.59708 | -51.15793 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e4746c3-09f6-3fcd-b824-d92a4fe88ce6 | -13.568 | -51.24992 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c966cb5b-efad-3ecb-ba7e-ffe9671d3f2c | -13.5652 | -51.24555 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8b971c-3609-3822-bdff-6d03185718df | -13.56457 | -51.24933 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc837fec-a43b-35d0-b7e6-3525503bf40b | -13.07654 | -51.13301 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9cfc32ab-6bad-32a6-9a86-063d524d3741 | -13.07592 | -51.13678 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 31d0d015-9959-3a7f-b433-031063a23950 | -13.07312 | -51.13242 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bc771a9e-2eba-396b-8308-d792a30bfa76 | -13.07249 | -51.13619 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| acb77cd3-a9c1-3cae-92e5-c8e2f5a1f797 | -13.07039 | -51.1128 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1ab6793c-155c-310f-95ef-49a3f03a8ff7 | -13.06977 | -51.11657 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d8ec2db0-f60f-33c3-b8a6-03f2768745f5 | -13.0697 | -51.13183 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6270cce-12e2-392d-8108-6d5d24b18c31 | -13.06941 | -51.11238 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1c89ff2f-1f1d-3e0f-b6e8-69a1b3bd641b | -13.06916 | -51.12035 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 980f90af-28b0-360d-80cc-d6fe0cba91ee | -13.06878 | -51.11615 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a154971-056b-36d6-a929-bf936d02e41c | -13.06816 | -51.11992 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5da0cfbc-6070-3b54-b9c8-e3433cb7bf8d | -13.06753 | -51.12369 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5573dab2-df97-36c6-b9df-f0da4e8ef54c | -13.0669 | -51.12747 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b755c42b-e547-301a-9118-174f7068f54c | -13.06573 | -51.11976 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1dc5b44d-24c2-3389-b60a-2084f0bc49f9 | -13.06512 | -51.12353 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38421d8a-d42b-3b21-9671-5884eaa7d10e | -13.06231 | -51.11917 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 41b4bf5b-a251-3ca5-9370-95da7c6ddc92 | -13.0617 | -51.12294 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64f36878-675f-3009-830c-d825c957398f | -13.05827 | -51.12236 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e76b159-3370-31f7-9bb8-2d6b99dcf156 | -16.09441 | -50.44464 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93bf5a89-40fa-3384-8dde-2fcc8518c6d4 | -13.04738 | -51.12437 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfaef417-1d76-3a07-9ce6-ded9634a39c0 | -13.03992 | -51.12698 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7ad0a0b-f863-300f-8783-05ca2ca24941 | -13.03649 | -51.12638 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f829c6eb-9538-3e19-bcbe-39553be528de | -13.03183 | -51.13335 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0468f5c8-3c8f-3538-8d0c-1e6142fa2ce7 | -13.02964 | -51.12521 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5bd3c132-d031-3340-bc45-21a84c3714c1 | -13.02903 | -51.12899 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d861f42c-f8f7-3bff-8eee-2d0759b8338c | -13.02841 | -51.13277 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1b3e172-f747-30be-a2da-24bf640174c3 | -13.02622 | -51.12463 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc7c2e1e-d17f-3fb4-8cd3-c0db44a06d63 | -13.0256 | -51.1284 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d986fef3-00db-3451-978a-3d8c0c7d9d75 | -13.00909 | -51.12169 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9369595f-6fc5-3ae1-a7db-4961be03162b | -13.00629 | -51.11733 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a96e890-e0db-3250-a4bb-202ae9fa0603 | -13.00567 | -51.1211 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad0c8bc-c29f-36c9-a8f2-2157d9fd93a1 | -13.00287 | -51.11674 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20cbb5c0-98d2-3e27-8244-f9feb5d8699a | -13.00224 | -51.12051 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b2b94f3-9c6e-309d-b99f-f35cc6cdbead | -12.9845 | -51.12136 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39dfc8ea-cce4-3505-9f8e-ea4eb2d44191 | -12.98387 | -51.12513 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56d20b4e-fe5c-3a82-96b0-78d401b2c99f | -12.98325 | -51.1289 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b76c6dba-d3af-3b1a-a905-5a1dbf2a4ba4 | -12.98107 | -51.12077 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README122.md)
