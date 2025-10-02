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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a6d3a65-5a08-3d77-87e4-b1221ce3449d | -11.29194 | -47.82866 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cc9d682-7352-346c-a38d-6c59d4b614c7 | -10.21678 | -50.34004 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c923437-ff57-3074-89a5-60afdb138b4a | -9.89775 | -45.94333 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1def059-d996-3cf4-9474-fe8f87264fd0 | -7.77461 | -42.53781 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 141974cc-2027-3bff-965d-e0667983e52a | -11.7927 | -47.57302 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98e3c60e-1193-32c5-9582-eba3c4274330 | -11.37787 | -45.04145 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde62bf1-3832-37ce-bfdc-6bb4a764e169 | -11.16408 | -47.26951 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49bf4b7b-162e-3391-9e2e-2e5e56daa07e | -11.8198 | -44.99983 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abcc3949-ce6f-3494-b00c-3aa6f70468e3 | -11.36027 | -48.33555 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2944b1f7-5848-3e95-b27d-944c9e644980 | -10.99424 | -46.54312 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98adb8c2-a02b-3c95-8e8b-6f5eedc90013 | -10.2536 | -50.32041 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce1b97cb-5701-326a-aef7-ca2837ec2dfc | -11.27274 | -47.82883 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4108dfc-cd19-3c11-8457-3c147d5da285 | -7.15451 | -46.06167 | 2025-10-02 04:29:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d16d1c-6b9e-3a22-80de-bb43750fc387 | -9.9301 | -43.71357 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 829f07ae-4bc6-3ad7-926c-04f8680b901c | -8.57544 | -44.79066 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e6d6d9f-a70f-3085-8a3b-facaa5b5a37a | -6.69793 | -42.81534 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 312d1728-20ad-3f8f-8419-b207c939b688 | -7.5538 | -42.40253 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6cc1e79-a788-3b10-a7af-fed689f23b58 | -9.40364 | -47.58039 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c9f7c4d8-3846-36a5-a63c-6698e943f363 | -7.78118 | -42.51952 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5db4aa49-6dbe-3a66-9bb2-5a40b50b174e | -9.79904 | -45.95058 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9108ebb-228a-31b2-81a3-9497d054d1f8 | -10.82401 | -46.63285 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32dc53e9-97a8-3157-ba7f-6a3429078789 | -6.77221 | -45.58572 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c3d93697-a36e-3cce-9a25-c54bfab3254a | -9.80788 | -47.84501 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e3fa6e1-fa5e-3803-b7b0-f7fec2a7e03f | -11.94463 | -43.91128 | 2025-10-02 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 512b6470-75a0-35ad-9fdc-815ef93f07f5 | -11.48112 | -45.00367 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f195221b-8b83-3c4a-8dcd-8747a6bc822d | -9.9226 | -50.49115 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 057a74e0-ccd7-3d5c-8e3e-5ba55e38894e | -10.99758 | -46.54366 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ad71ea3-bbc3-36fd-8a97-235d412ba3a0 | -11.47008 | -44.98159 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff1d22b3-24e3-37ee-8a91-e3df242bbae0 | -10.64088 | -47.45946 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4c71cd6-9be8-3098-af59-303a0e661543 | -7.77843 | -42.53838 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c7aa42f8-368d-34c4-ba0c-1e42182f14c9 | -11.19293 | -47.75051 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1d1829d-436a-360c-b8ed-b23a9ad57632 | -11.06754 | -47.81358 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 301953b7-f7f3-3d89-8397-2ab53a50e9f5 | -8.6398 | -43.9842 | 2025-10-02 04:29:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a7e4ad3-d225-3686-a311-41fc24e57adc | -11.21319 | -48.21249 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9217fa7-de6a-3cad-a777-5955e3e3e1cd | -6.66517 | -41.39619 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 762c62ba-db7f-36bc-a26d-e0f28f47a97d | -9.93938 | -43.70172 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f800e9f9-74b0-3f57-8b67-d63f05bf1559 | -11.36084 | -48.33197 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69df2d10-fd45-3df8-ae88-d8251052dc6b | -7.04712 | -43.31216 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 982a2e1b-a614-3727-958c-f5f94448ce94 | -11.56847 | -47.02343 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f1a0c5-0498-377b-898f-31e57e268106 | -10.9931 | -46.52834 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd8fcea9-e557-30f4-a809-892ef92c4d6d | -11.86288 | -45.00113 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2529b141-fb2f-3294-8592-5bd01ee92d8d | -11.13183 | -43.38905 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7798f530-5c33-308f-b05c-1280d785b772 | -9.93424 | -43.73613 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8cb80198-cbd2-311a-b845-d604dd012c26 | -9.93167 | -43.75331 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 315cc58b-904a-3c35-baf2-8ad29d012113 | -11.17129 | -47.28871 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d5a9079c-5831-359a-946c-bbe74e01a4d5 | -11.82239 | -45.03141 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0ec7c166-421d-3415-991e-2d76f44341ab | -10.23553 | -50.31731 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 32797910-c29b-39e8-ab3e-21d90a5dde1d | -10.85678 | -46.57623 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f769d6a-2548-3185-a047-f89649bc85d0 | -11.44087 | -44.96048 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95337312-346f-3ba3-a3c7-2f0be31a9b89 | -9.03251 | -46.68055 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3137c6c-03a5-389c-aae3-5f386201b258 | -10.35095 | -48.2074 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4372d64-ba03-35b6-8a7f-312a2e6bf63b | -10.65103 | -48.51071 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d89d379d-06f9-3a0d-877d-88672bcbe7cc | -12.22803 | -43.76217 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87cd4793-03fc-32c2-8c18-ce22b1862494 | -10.82195 | -47.95166 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c46cd8fa-d912-3498-a0ca-df67cc89bb09 | -9.82843 | -48.26234 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9626330e-8e1f-3c04-a641-9787d781c6a9 | -11.47849 | -45.11853 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb702515-ada1-3632-b5d4-c5bc66ffd10d | -9.94241 | -43.70657 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a87f1e-1cbf-32be-b096-ca60d18042f4 | -8.9055 | -46.66765 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d13e0ae-fd1d-3a82-b1d5-6d2770446487 | -11.19733 | -47.18822 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bb6790a-1ad4-32d1-be89-59aa1890e76d | -11.09156 | -49.6967 | 2025-10-02 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecf0a94a-0328-3002-8d9e-2865f838d394 | -11.70443 | -44.30896 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47795aa1-7c48-391f-a6c5-81b9cd49d6f2 | -10.69507 | -48.58104 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe3ea9a2-8c35-3fb2-803b-167ec011ecc7 | -5.83625 | -45.75812 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 706df5e1-ea84-35ca-a4b8-c8fed8e79018 | -7.79855 | -42.50762 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3bf3cad-81da-3334-bc8e-f7c180023820 | -11.81045 | -47.59039 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e5ab1ac-864a-3549-9723-9e62ae26bed5 | -9.93488 | -43.73184 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50ff22a2-b3d7-3ad7-9ad9-d798f658fe81 | -10.22152 | -48.2227 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea18ea04-33bd-349f-ba16-c1710a527c4b | -10.82977 | -47.94567 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1477845a-1eac-325c-88d1-43fcaa12d092 | -11.84179 | -45.0219 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cb240c0-2c01-3090-8308-c3383d304b3f | -11.27218 | -47.83237 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6765f75f-d6ac-3064-aafc-ebe276b8d086 | -11.44252 | -43.50252 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25485297-978b-3b82-bfa2-a7d0ca7fa0b5 | -10.23914 | -50.31793 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c3282a28-a84a-3335-9c9e-5997b2486ef2 | -10.26066 | -48.06424 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6707c75c-35ea-3bfd-851e-3d74bc1e6c4d | -9.16391 | -50.8418 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c64fdf-2184-35e5-86b7-4a8ec719f39c | -10.93215 | -48.58327 | 2025-10-02 04:29:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b502cdf3-8f7a-3bf7-9bd8-3a8770fe976a | -10.9432 | -48.56229 | 2025-10-02 04:29:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d1864b0-f6f3-3c56-a536-0ad41c72420e | -8.90532 | -46.06659 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d4aae9-f491-3199-8f2f-c83b0b384d1c | -10.20217 | -50.27018 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 49de204c-2234-3851-b45f-c5a47be78712 | -11.71139 | -44.46545 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f92b3bbf-f4d1-3e1d-847b-42f6bf0af802 | -7.78186 | -42.5148 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5f33c1d2-78be-36bf-a28a-b1be29deb4a9 | -13.24751 | -47.33193 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dccd2a9-60bd-3f23-a5ba-75e0d748b9a4 | -13.30795 | -47.85267 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e45e3045-ed10-3266-92a7-1ae58d446b94 | -15.39392 | -47.04499 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc57b0ca-1826-3587-98b3-2c570cc722ce | -13.76775 | -48.00056 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64de6b72-715a-3b24-89bf-410713f917e8 | -13.20022 | -47.3279 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4628a4d-f37f-3150-b66b-3ccd364b2532 | -12.88484 | -46.90374 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4c9dbc2-42be-3f97-b89d-be2d3313bfaa | -15.18797 | -46.42267 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9248c6cb-a6ec-3c0a-8a44-af56d5fa54c5 | -12.91119 | -47.165 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8de9442-e225-3d06-8cd6-f1e2ccd71d75 | -14.49177 | -48.42649 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e64cb8f0-8574-374e-990e-a43a8bf01159 | -14.41438 | -46.07897 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb65e960-3570-35f5-ba12-b13613bacae8 | -13.36819 | -46.34297 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e67a44e-2e69-3c99-b0c2-167763f27d2e | -14.48228 | -48.44323 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7cce6b4d-f094-329d-9b29-b40cf6f72062 | -14.89525 | -48.37603 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b159599e-2359-3ba4-9ef8-c6ee30e921d2 | -12.66255 | -46.8759 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a63b7362-fb7d-35c9-82fc-f02abc28af42 | -13.21358 | -47.35201 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4369bb6-6339-3180-a155-bbe3c629d841 | -13.75604 | -48.70826 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 507b511d-d534-3ab8-a5bc-6e051aa3bc74 | -13.17612 | -47.83071 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be2d13fa-18fe-30f9-9f66-63ba9efcdd3d | -13.75893 | -47.96989 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf001588-0e05-39f9-8ce0-41333881d4ef | -14.64673 | -48.26219 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae683aee-4e2f-3c43-849c-3d7e8c9be5c0 | -15.40499 | -47.04623 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
