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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19fa32b5-61de-3f69-9224-0ffa4d91f6f5 | -7.7433 | -50.281898 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd94176-7e00-30e8-ade2-5cc2e4853834 | -13.4992 | -46.856098 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98439792-ee91-3bfd-bbbb-88e113a95a20 | -7.5788 | -47.488701 | 2025-08-27 00:22:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a584925b-ef14-3205-b9d4-b25107cc245b | -8.2581 | -45.120098 | 2025-08-27 00:22:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06f24155-648b-38bc-9df5-b566dfdfa544 | -13.4211 | -47.009399 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dbef5c22-e5ee-3533-a197-0a1fac8de562 | -8.6956 | -47.191399 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8f05dae-a453-3f39-906a-18ed2bacb2ce | -6.6274 | -53.319099 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b227f05-8e6d-33d9-b302-2110f29682ad | -7.1718 | -59.709301 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 606479e5-945c-3bc0-8761-b8c59781f965 | -3.9776 | -47.868301 | 2025-08-27 00:22:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184df1c1-d21a-3179-91ab-21c5aca61d58 | -13.6508 | -46.886799 | 2025-08-27 00:22:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b015986-af11-32d6-9dac-fbcb97eb09ff | -6.8188 | -58.937901 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac3b1515-a762-307e-bb9e-c76d947ea8a1 | -9.2003 | -46.7024 | 2025-08-27 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2dc3910-cb2c-335d-99ae-8123d1a16757 | -11.5778 | -47.6068 | 2025-08-27 00:22:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a48424e3-44ca-338e-ac15-ac3eada76dcc | -5.5542 | -44.272202 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2acdb77-1815-327d-ac17-6681f67243f5 | -4.9618 | -55.793701 | 2025-08-27 00:22:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c50a35c-c743-3b07-9ce7-f255395ed40d | -9.7882 | -49.8927 | 2025-08-27 00:22:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 910f17c6-27ba-32c5-8c8a-8cd72644fd33 | -21.586901 | -47.461498 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1b916d-2404-315c-9090-4b16e2e1ed24 | -5.7576 | -53.756599 | 2025-08-27 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e4192d-1fcb-3bcf-a160-5d48f915a1ae | -9.3975 | -60.477901 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4bd05f1-2460-3806-b7d5-8da4297341d9 | -9.2647 | -50.222401 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8de009-caa5-31a1-a740-bbca23fb62db | -9.184 | -59.4034 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d478088-4ff4-372d-b3b5-16d61ea3ab55 | -8.4353 | -49.604401 | 2025-08-27 00:22:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 438128a1-aa8c-347d-b851-2df6da0c5d04 | -5.6603 | -47.483002 | 2025-08-27 00:22:00 | METOP-B | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b24ae96-ca8f-3e29-a8db-bd3050398efe | -13.0613 | -46.308201 | 2025-08-27 00:22:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1a69b82-c3fc-3d6b-8a11-5d44e694ffb0 | -9.5977 | -55.363701 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f468874-a628-382f-9402-e767b87bff1c | -13.1701 | -45.286098 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d77ac5d2-009a-3d8d-be15-6604246ffbb2 | -12.7649 | -48.150398 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7860525-b286-36df-a153-6445c777b7b6 | -8.1308 | -55.532001 | 2025-08-27 00:22:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| defecd03-ac11-3d61-b222-8e4ebcb629f6 | -6.629 | -53.326698 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526d46cc-fc05-3aab-9e5e-06fd878fedec | -13.11 | -49.316601 | 2025-08-27 00:22:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 612cea05-7b65-3560-97dc-ab5671749d81 | -21.325899 | -42.801601 | 2025-08-27 00:22:00 | METOP-B | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3fa4393d-a6d3-3176-ba32-ea44132a129e | -7.4396 | -49.622101 | 2025-08-27 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8f8a83-ad62-39eb-803a-830f898d43cc | -5.541 | -44.260201 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ecc3a88-b17c-34ff-ac50-be8524c99c87 | -8.8778 | -60.700802 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7825dd8a-5ffa-3767-97ef-4e93dcad583d | -15.6627 | -52.723801 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e864cb79-a6a0-30eb-b94f-bb401413b66f | -13.5261 | -46.8834 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0aab8989-3141-396f-b5c3-b73a9e4384e7 | -9.5759 | -55.3573 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3907f5b7-51bb-37c8-8d58-8ee311df8418 | -15.1047 | -48.607498 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4abf7e-f1bb-3a46-af8f-a894fd58a137 | -8.8639 | -47.1609 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638f0362-3d26-3de5-9992-22071ff16528 | -12.7388 | -48.171902 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ede8441-40fc-376a-b4b0-ff9ed60275c7 | -6.9133 | -52.843102 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceff6416-c24e-3981-a991-3f249dd8288e | -5.7593 | -53.764301 | 2025-08-27 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf011b4-5803-3abe-9f07-993b48e2b403 | -13.4545 | -46.841599 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6a534ff9-02cb-3126-9dda-b269d559af02 | -17.5509 | -46.607101 | 2025-08-27 00:22:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cef64649-37a4-3e60-9bbd-b198b74dc8e5 | -12.719 | -48.130199 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d30f69fd-909d-3df4-a28c-c274f786a352 | -19.5721 | -47.523399 | 2025-08-27 00:22:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65cbbc51-76cf-3ebf-9ab9-fbb4d23e3223 | -4.4957 | -46.371201 | 2025-08-27 00:22:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9f0d1a-f989-3638-9d71-0ba68c1b3395 | -21.1054 | -48.820599 | 2025-08-27 00:22:00 | METOP-B | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e07c556-b519-32b0-a905-7497fa72ec6f | -9.5662 | -55.359299 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 209b73e9-b418-3063-95d8-e7cb1d2f73bb | -13.4309 | -47.007 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 539097f4-3b12-347c-83e5-b7f2008ba29c | -13.5377 | -46.889 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44892f2b-ba9b-395c-aef0-236daaffeb45 | -21.106899 | -48.828098 | 2025-08-27 00:22:00 | METOP-B | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8540642-6b1c-3057-881e-ea58a1ca335c | -13.4032 | -51.751999 | 2025-08-27 00:22:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 930c67e2-8dd4-37bc-ad80-c75098833d82 | -13.1678 | -45.276501 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d73fe3a6-934a-3cee-be1b-01506f175048 | -5.5473 | -44.2435 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62a31f2b-1536-343e-bf85-70733dfefdbf | -6.848 | -58.9319 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aefd8c98-e5b8-3039-abac-501e2f42c5d2 | -16.7418 | -47.5877 | 2025-08-27 00:22:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a74c9825-d082-3dc2-9a7a-99fc5e5da5f7 | -12.7974 | -48.111801 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 048c06e4-7be6-3654-bec0-068fac226b08 | -12.7843 | -48.0994 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c6b143a-6c4e-3be4-b797-0179c6c25c52 | -11.8229 | -46.795502 | 2025-08-27 00:22:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eec0d1a3-37b2-3de9-826a-9511ecc4098a | -9.1108 | -49.584 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5c65b4c-fabf-316c-9f77-70294f80a4a7 | -7.3807 | -47.036201 | 2025-08-27 00:22:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51af2bbc-3460-36e8-9631-5ccb65439b41 | -9.4021 | -60.500999 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 795a1f1d-44bd-32c1-8de3-eb25d9c24856 | -9.7013 | -48.328201 | 2025-08-27 00:22:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 375c166d-b063-3c10-8a7c-48ac8e25c5a2 | -11.0578 | -52.0131 | 2025-08-27 00:22:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 213db624-d43c-3e73-b863-90e23735f7e8 | -13.842 | -46.687901 | 2025-08-27 00:22:00 | METOP-B | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67248252-5cf6-3d9e-924d-694fb93e9117 | -19.5639 | -47.5331 | 2025-08-27 00:22:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34ed7d5e-0402-3db3-9664-aff0d14d9f93 | -17.778299 | -44.4916 | 2025-08-27 00:22:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ea662d47-f5a2-36d1-ad57-a7212b4a2c15 | -10.6082 | -52.308399 | 2025-08-27 00:22:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7410cee4-da74-386d-b8ae-bdd249ba651f | -19.5623 | -47.525799 | 2025-08-27 00:22:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a87c032-42ef-34b1-833e-237ce9b3438c | -13.6269 | -48.131699 | 2025-08-27 00:22:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7df1bd50-8eb8-32aa-ae10-2ab4fb54209d | -9.0864 | -49.567402 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e63cb880-d861-3c4c-ad65-5440f8e23c56 | -9.0832 | -49.553299 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 737e9469-ab2c-3f35-b55f-c315b1dbc636 | -9.3982 | -60.43 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25761cc8-63a9-3502-9a9c-33461d60c707 | -9.2781 | -56.870098 | 2025-08-27 00:22:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42a6ced9-d42e-3d20-8865-51d6ac585bc6 | -11.5215 | -52.1166 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9e86716-5d48-3c24-af34-1c1598fb9b4b | -8.2652 | -45.106201 | 2025-08-27 00:22:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 907fd771-457a-3cc5-8d3d-e63f70e400da | -13.073 | -46.314301 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c9b8deb-71a6-320c-b71b-2f431af2c625 | -9.0978 | -49.572201 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61f00860-221a-3f86-9498-480cd6dec07e | -22.6171 | -42.146301 | 2025-08-27 00:22:00 | METOP-B | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49c8187f-21cd-3f0e-be18-64dec801fbce | -13.4547 | -46.9762 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd3378e3-1ef1-3774-841a-57f6ca6b5e44 | -11.5657 | -44.629799 | 2025-08-27 00:22:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f63d829-b060-3c0f-94e1-ddc172f77f53 | -11.0382 | -52.017399 | 2025-08-27 00:22:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2e2df28-4602-3b77-bbca-18f8ce0ef2c2 | -11.3809 | -55.351501 | 2025-08-27 00:22:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f41791f7-ba86-31fe-bcac-0e2b2fd8a217 | -9.1607 | -59.488701 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02a18593-60bf-30db-9e95-21b6c218b1fe | -9.2632 | -50.2155 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 811eb713-0a1a-3d44-bfaa-b466e7f35342 | -7.7079 | -45.752998 | 2025-08-27 00:22:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a21019d8-9577-330e-af11-5ab6639b4ba4 | -9.0732 | -49.599998 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 130519f9-0aa0-393b-b742-b85defbfe155 | -21.113199 | -48.858002 | 2025-08-27 00:22:00 | METOP-B | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 827f7360-5be8-3689-b4c5-34ab70d531a5 | -18.1551 | -44.4226 | 2025-08-27 00:22:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c48f0a2-3b27-3f3d-9e0d-996de2a645d0 | -20.326 | -46.879601 | 2025-08-27 00:22:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 598596c2-d766-3fec-b488-0de342429d58 | -8.8828 | -60.675499 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a95e1f8-a31b-38d2-bb37-537d0e3f4802 | -11.8209 | -46.787102 | 2025-08-27 00:22:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bade6871-f5d7-3dff-b032-a79e95b3d192 | -7.8037 | -51.057098 | 2025-08-27 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5aef950-fa0f-3fce-a5fd-3216fb8b0ec9 | -5.1033 | -43.203701 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a71b290-5585-3c64-8f55-a444c42194af | -13.6368 | -45.6833 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f372544d-5909-3ced-86bd-4dd7a8b4c72a | -9.0994 | -49.579201 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7683d7f-9e29-3244-85a1-33272086c99e | -11.5684 | -44.6408 | 2025-08-27 00:22:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 761c862a-75b5-3d16-af34-85991766f9ac | -10.4178 | -57.677502 | 2025-08-27 00:22:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eae3a45-4225-3f01-9865-070369bb8873 | -12.874 | -48.085999 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
