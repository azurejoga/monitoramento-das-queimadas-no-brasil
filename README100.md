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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f312896-68b7-3783-a7aa-aaf8d4a39386 | -10.20932 | -53.91524 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b70d860-deaf-334b-9d28-d4024841da96 | -7.57061 | -57.68137 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4f582af9-390a-3b08-8c8b-d5ce699bef39 | -10.67175 | -50.72714 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 609750e1-0c5b-37b3-b3fa-edb7c16494bd | -6.3788 | -60.01295 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61dd2043-031a-360b-b515-add0c73fcac4 | -8.78064 | -68.84534 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d79dc853-b011-3719-b2a6-e2c7d874e3ec | -6.28118 | -59.92061 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a170b29-75e2-3a93-89dd-3a9a543bf297 | -5.85467 | -53.53461 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57649ebe-77cb-3ddb-b0c3-4d3bd1d66daa | -7.25109 | -55.58818 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727c475e-97a1-3fb6-b08f-ed397726d79b | -8.60559 | -54.61914 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5655868b-8c35-312c-b07f-0cd3752a79cb | -11.02573 | -54.13968 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35b99837-4287-3592-82fb-bdd7ddaf9dc2 | -6.14299 | -55.70609 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d29e9fb9-02b4-371e-8566-116f82918135 | -10.20889 | -53.91861 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 204e28fa-f844-30c3-8eab-184b07a44b24 | -9.02675 | -60.35876 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf2b858-0666-38c6-9e65-2db44d04ae37 | -8.79236 | -60.79521 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 713fb43f-c4b2-397f-840f-d61740844d48 | -5.77338 | -57.58818 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365e6eb0-5b7b-3b6b-8336-36aae10fd4c7 | -9.0654 | -61.42406 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d33fa8e1-4482-320e-9a5d-795712e1ad5a | -8.79923 | -60.79629 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c9657e-5aac-38de-be0f-41c183884a91 | -9.6701 | -54.33315 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5246ca7-c4ff-38ce-9473-ad841ce8c23f | -6.73115 | -55.07699 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5d4693b-7a1e-37a2-9ce1-ebba0052eb3c | -6.1878 | -57.77789 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be9302c5-f60e-3ef6-bf49-6b398d726ccb | -8.85202 | -62.36092 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d00bf99-52e5-3e81-a55c-cc1ef0e7ccf0 | -10.42916 | -50.2379 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 91081369-67e9-34ba-99b0-c80e844102f0 | -9.61504 | -61.81883 | 2026-09-21 05:42:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbe173b2-4029-3dc2-a74c-2ef17aa08178 | -5.80735 | -57.73889 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 616b3706-0d24-3cd0-8e86-93110bfb2985 | -9.04765 | -60.99821 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 145d578c-75ab-39a4-9cae-e75a05832f33 | -10.92422 | -53.95057 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2105a5-5c7d-3b4a-a10a-7cdf7a0abc41 | -7.82 | -61.8028 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e02bb78-7486-3709-8a05-b8f12a24b52f | -8.01842 | -71.2313 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0bcc533-b7b9-3ec1-a829-b3ffc62f04e1 | -6.83421 | -55.53665 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 448dc70a-84ee-3c23-916b-4c0d3b3867ee | -10.91664 | -53.96677 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54d0436-d411-3242-a00a-e541f4adad67 | -6.74228 | -59.0765 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56c15900-43f7-3f59-af8d-b8c07b7b32b4 | -11.1294 | -54.00777 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e18a93c0-73c3-3d5d-b9bf-61030cf02d42 | -9.36127 | -60.31498 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31413d1f-e4e8-30d7-87b9-a8e7793cf416 | -9.37029 | -65.47948 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72aa034-817e-3c92-abd0-d6544ce8c9d5 | -10.87514 | -54.07708 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 204d0357-d93e-327d-a4b1-51a112b593ef | -8.16119 | -54.82444 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0e34b5-13cb-34b8-a694-89e245a511bc | -8.53958 | -54.68856 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b00f07a9-ce34-3fe7-804e-466c8c971209 | -9.03699 | -61.65168 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c86b71b-a1fd-3aa6-94a9-9194a9068e5f | -6.73782 | -55.09735 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a889d374-8f5a-3f95-9990-559018b6e45d | -5.80939 | -53.52165 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99537ec1-70fc-33f6-957e-26adc50acef4 | -5.83843 | -53.53826 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2b1fab6-2a05-3497-90a8-907b6630504a | -10.45908 | -61.31803 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d6df394-af65-3fa9-a53b-a2e1b70e7c72 | -6.20328 | -57.7802 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 75b19366-bd4d-3f4f-975f-8e0ca8625e26 | -10.46879 | -50.27266 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3906955-3f00-3595-957e-50d664f9684b | -10.8926 | -53.98404 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ef9509-e39f-3c2b-b973-a3ec84ebd956 | -6.11557 | -57.35541 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c47cc5d-7e5f-3a1b-bce2-84f159f61ff3 | -6.14267 | -59.9354 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdbf7e5-84a1-3e36-af30-5baf8d810e8a | -7.56813 | -57.67056 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07f7ffc-a90d-3997-ae10-214e8619e30c | -9.02616 | -60.36266 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39ce294d-a0f0-3eea-8460-1478aa042e51 | -6.15731 | -57.95346 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae1a01e2-5105-3614-bffb-04270f3f4c8f | -6.09161 | -56.46896 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e49845e-ee47-32c4-a08a-5bdc75987028 | -10.79935 | -50.75731 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52164db8-5414-3d95-98bd-103b744a7af0 | -6.4462 | -59.97569 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82311f68-898f-39e8-8fcb-b16b4c6982eb | -8.79645 | -48.74656 | 2026-09-21 05:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 21b1e6b4-f918-3e86-a6e1-0d80800bf274 | -6.13804 | -59.94242 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94c04927-2861-3d4a-b7d6-878a60602af4 | -6.76315 | -59.10961 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c10d5152-de50-34c5-8902-76fb4b6ad3b4 | -5.84042 | -53.5607 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 142c11b5-8ea5-3845-8f89-a417430082dd | -7.24455 | -55.60137 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c90181e6-38e5-3e7e-abda-10f68b7da9a1 | -6.73422 | -55.07587 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3e435a9-d48e-3adc-8661-490577071347 | -6.12995 | -59.94892 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98d248b5-b1f2-3234-b069-be7dc48f927c | -8.186 | -54.73359 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35fa49dc-0bde-3887-be00-12e7eda1bcc8 | -9.04393 | -60.45676 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18697de-37fa-3cd3-a442-37faca35d612 | -8.1887 | -54.76831 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede1c6f9-4689-30d9-9a80-957d3242a4fe | -5.83548 | -53.52235 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521d7d88-a8fc-36ab-aeed-5d8e547ce004 | -6.46297 | -59.9822 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b91fdeb0-0466-3628-b557-910cf9e6560e | -6.1468 | -57.84041 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c71eb42-7f01-33ce-8adb-1a6abb1f0da1 | -6.4572 | -59.97351 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a9ad73e-64f7-3da9-aed5-6541fcdb2919 | -8.18209 | -54.76071 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd88cf4b-a19b-3fe6-923f-a8df5000270a | -9.29959 | -60.53287 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f28a6d7-d031-33ce-bffd-2c00e4642954 | -6.923 | -59.63246 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45b218ec-f74b-34b7-9dba-cb0c0a108f00 | -8.86824 | -68.80495 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6268885-2144-3bce-a925-dbd2090deaf5 | -6.72812 | -55.08482 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 409cc191-06bb-3e25-8e45-f2cbd7c84f9a | -9.56549 | -66.05109 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13239e03-62dc-3606-9543-ed849abffe84 | -9.55016 | -66.03107 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bb21c08-7b07-35f6-a7fa-c7ec8740218c | -9.28006 | -68.36958 | 2026-09-21 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c49ab5a8-67c7-3c4e-96c4-4ae4157e0ade | -10.79687 | -50.76862 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fba67c9c-be93-38b4-b8c2-ea5f5a16e048 | -9.93962 | -60.7259 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b126f2c9-8436-3af5-a6f1-0916d648be75 | -11.03021 | -54.14695 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4721f5b3-9170-3abd-98dd-e26cd95b5b68 | -6.96354 | -71.76235 | 2026-09-21 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d6c223-fe9f-3c91-a70e-cd0cb3202a4f | -6.35268 | -57.77182 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c026c15-2bbd-3764-abe2-1f5d7e552062 | -10.46205 | -50.2718 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef070d0f-b418-3b11-85a8-71fc9e0fc28d | -10.91842 | -53.95313 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a460c22d-1c44-3224-b002-bc436b015b6e | -10.7973 | -50.77406 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2703a9ff-f41c-3ff7-9eed-b7042e71077e | -5.20357 | -56.07276 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b96f925b-0fdf-3d09-ab27-2b740bd954f8 | -10.46599 | -51.33603 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0425b6d5-ca5e-3624-8ea3-1e808d4b785c | -6.64933 | -59.96696 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6520bba-9d07-325e-b6d3-d3625fe00987 | -10.81656 | -50.77117 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| beb30f80-a0da-30be-b1ec-24995d503a25 | -8.85257 | -62.35742 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73090f3b-9bff-3281-bbed-daa00a9e0158 | -7.57383 | -57.68705 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca0fb8d0-0b03-3094-a0e9-026ca342fdd8 | -5.83943 | -53.49493 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53d345cd-2539-3718-a4fc-b24df798ca14 | -10.2189 | -59.40114 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8d2809c-b0ad-313e-91ce-7559fed00c8f | -6.09847 | -57.68363 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7795989f-9189-3f28-b580-825b6f6f472d | -9.55729 | -66.01061 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a9e94cd-0b11-3e6e-bbf3-18de1eace37f | -11.04407 | -54.16533 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f37661d6-e20e-3dde-acf6-b113089071c5 | -7.48699 | -64.70541 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79ffc381-412b-34ea-a0b9-7e912b51cdd1 | -10.80223 | -50.83704 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57171aca-9fd0-3860-b362-738ef9be499e | -8.08121 | -55.34064 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be179b43-e6a5-3ba6-93b4-535a57cf7136 | -9.1797 | -60.30118 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d37e2da9-33d9-3ec2-b4ab-66a5e1584a75 | -5.80806 | -57.73412 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fa5d1fd-0577-32be-a03d-c694e7b90f83 | -6.44828 | -48.45208 | 2026-09-21 05:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README101.md)
