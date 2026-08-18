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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a73b38-e96f-3098-8e57-c2367214f64a | -11.86088 | -50.18305 | 2026-08-18 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a28eca2-9e32-328a-829e-8ec4d558ea90 | -11.60728 | -54.68282 | 2026-08-18 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b00cd7f-f582-3bad-8941-762ac9119954 | -14.84303 | -46.6313 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29158969-3eb6-39e6-acef-87aaa73b9288 | -14.29935 | -47.17807 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23cf8637-50a6-379e-8490-c8c66b73b48c | -14.80557 | -46.64819 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 30e7edd5-c310-35ce-be3f-9f1c5440318d | -14.31229 | -53.04313 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86a59828-a3e3-35a8-a089-a47cd331d35d | -14.43834 | -51.88599 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04469570-b85e-3f62-85d9-c62dd00974e7 | -14.35357 | -51.92715 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5e725d-1b4b-361e-9f0d-f6c5890cda25 | -12.25999 | -45.8726 | 2026-08-18 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd9d2149-d366-31f7-9c7e-6f0ba91ef63d | -14.35642 | -51.94017 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efade057-4a5c-33ff-a4db-11d5a727e023 | -14.82086 | -46.63935 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b1d12768-f957-3627-b94f-bc5ef9fdc6cd | -10.27284 | -50.42065 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 34788326-7530-3b47-8f22-2d213c893763 | -13.39769 | -54.34816 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310598d8-05cf-311d-a56b-7856c586ff46 | -13.41688 | -57.03941 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7161ba82-7ec9-33fd-acc5-b4e5cc161dc0 | -12.73584 | -48.45459 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 559afdf4-8831-3f8e-b9bb-f721d17ccbec | -15.26666 | -56.49741 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3310bbc-5bef-3ecc-a7c1-c8212e0c30c3 | -13.01763 | -56.59021 | 2026-08-18 04:40:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d3bb0f6-1dd9-3d56-9a2c-65f2a0389e03 | -14.16479 | -52.90417 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c01ad45-d567-34fe-ad03-5b5227b39999 | -9.16065 | -59.66796 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50879e68-521f-3166-bfd3-cbcf39b39394 | -13.43134 | -57.07568 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39859a16-a988-3fab-a9d1-f3ca4aca0e72 | -10.93728 | -57.10722 | 2026-08-18 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5073857-2db2-3076-bf95-ba74ece8fc6f | -14.87712 | -46.63686 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3b72ff8-3072-37e8-8965-a247e618b304 | -11.33195 | -45.92211 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d513206b-337e-309c-bfae-42035ab42957 | -12.26056 | -51.53993 | 2026-08-18 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1c14318-0f94-3e2b-b060-966f31e681dc | -14.04823 | -53.69172 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ccfa3af-99d3-3925-afdf-a07476641391 | -14.4586 | -51.83441 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 418f882c-f596-3905-bfea-49a9b3e45f13 | -13.42218 | -57.06723 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7968ccd2-1c31-371d-8d46-a6137053adce | -9.42615 | -60.44323 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 54ae0ce1-78c8-3c53-887b-28b919d47806 | -12.51702 | -47.8735 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6e34e17-c295-3ad3-9449-2f83c48d7341 | -15.2094 | -52.70238 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9cda323-4ba2-38dc-a161-f109146b8b23 | -14.27928 | -51.93695 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f48477-623c-3e6f-b8aa-873d0d8685a6 | -12.39909 | -54.96035 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9de2a58d-b58a-3185-8414-bd94acf96d15 | -15.24742 | -56.48107 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 588c5161-2e63-321d-bc74-531b79101e16 | -14.03152 | -53.60975 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e4d96a3-189c-3970-88d3-a36d3650adb0 | -14.82426 | -46.64001 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e8d110e0-01f3-38f0-8d71-5652f6f043d3 | -10.14329 | -54.27878 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a04c19dc-4273-36ea-8325-d3fdfbd00e56 | -14.82765 | -46.64067 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 89617020-898c-38ab-846c-1fe7335fe86a | -14.43097 | -51.88462 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1462aed-2b84-369c-882d-d8eb168604f0 | -14.03584 | -53.68946 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b42448c8-96a6-3ba0-8d35-a65336943f5b | -11.14084 | -47.28896 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 820400e0-84a1-3a45-afc6-eb2156021838 | -12.77317 | -48.42753 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afb3431e-b914-36ee-9b5f-3760da8e249b | -11.36144 | -55.41905 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a75e8d4-14db-34c6-8d47-b8ec0e961186 | -11.13918 | -47.27791 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8849d9b-3397-3ad4-86a4-33556472c0c0 | -14.17491 | -52.909 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 15ef9f17-4eb6-37c6-ae16-7f8e8cc8bc56 | -13.42741 | -57.06817 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c78b7d0-1bb6-3096-a2db-8915b38092df | -13.64722 | -46.2403 | 2026-08-18 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de93696a-abbc-3906-b436-2b648587b889 | -15.01707 | -52.69677 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aa49b5f-3df5-3874-a53d-d144b1b530d8 | -14.27755 | -47.18572 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12651cfb-104e-3a8d-9323-0a69972dd2a3 | -14.17863 | -52.91772 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 799a54bc-a049-326b-ad0a-2eee3642a009 | -11.29472 | -46.32401 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47e56090-d07e-37d1-b092-b10f68e39168 | -8.9547 | -60.52305 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f422684-03a9-34ac-aac0-280c53a77da5 | -13.26337 | -51.6508 | 2026-08-18 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| beebccb4-bf32-35bb-ab73-687d577a6989 | -8.90267 | -60.57447 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61f43f8f-9cd4-331c-a587-0218391595b0 | -11.47307 | -46.56968 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2275c70-9be0-3950-be04-cd4070f5a76f | -11.52444 | -46.63644 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a1e6494-2927-37c0-8786-608a3b15abcd | -9.42321 | -60.42246 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f45e758-d65a-3fdf-b312-f2ffcba504a1 | -11.19775 | -54.81786 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3541bedb-7616-3636-8369-d68ca8e6512b | -15.38822 | -52.7942 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 224924e7-d3e4-39bf-a7a8-700ca3b6726d | -12.94063 | -56.64793 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc2bfe00-3466-3c19-becc-7b31bd8e964d | -9.00983 | -60.49961 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c187e5f4-96de-3e87-833b-37aa6afedcdb | -15.3017 | -56.44705 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c78d47d3-d55c-3232-83c0-7fc7b8c4f7dc | -15.03261 | -46.55136 | 2026-08-18 04:40:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8946c004-4f50-3efb-9057-7189c140f25e | -11.45968 | -46.56745 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4adc7aed-c5f8-3474-9112-eecbfb58351b | -13.56094 | -51.69964 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee62aeab-c471-3849-834d-3a77cdf9e55d | -8.94915 | -60.52182 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 985d3a24-1def-3056-8b11-baff8ceabe77 | -12.00907 | -46.42024 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab49a67f-0f01-353b-8911-99390736073e | -13.39688 | -54.3525 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddcaceda-1ebd-38ea-9bbe-d996df3b355f | -11.33706 | -45.91137 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86fbe9fc-7c35-3679-9513-6eb41b6825c3 | -14.55377 | -46.99705 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6840643b-7dbf-33ed-b661-80912184dd42 | -10.78181 | -50.32719 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8039ddd1-1956-389f-a806-eb370f73f802 | -14.30606 | -47.17916 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6a72c28-6ba7-31ae-85b3-418a1c96a4c1 | -12.70105 | -48.52209 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24983aa4-6e2f-3ed9-a70e-1316e55fd1b1 | -14.17586 | -52.90381 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 20954f5b-fbef-3c1d-8963-7b52de324fac | -14.1799 | -52.93367 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c734b330-f44c-39bb-a3d8-b8702ca709af | -11.10479 | -49.90579 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6387c6ff-0745-3392-883e-9740d2633afb | -9.16049 | -59.70348 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7a5cf3f-b412-3a34-8c60-99b37bd68d21 | -14.81181 | -46.65306 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d88948d3-2897-3285-9768-a076f879625b | -14.82542 | -46.63231 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71d7522a-cd3b-31c9-bf49-827ada218a3e | -13.41909 | -54.37871 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11f5f3d9-f8df-3c62-a429-a501824a7fab | -14.81011 | -46.64121 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c2dcddc-2725-37d2-bab4-1fcb2258e71f | -11.14514 | -49.04016 | 2026-08-18 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c486134-285a-3842-ae87-c51cfc3d49b7 | -14.85611 | -46.63723 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00138be-ddb0-34a5-bc0c-1a9220193f16 | -14.1305 | -53.66097 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 072bd683-7ff7-3e49-bb40-e04e1b781468 | -14.02741 | -53.60904 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82c7c723-9689-3d89-b031-2602a717ef45 | -14.25531 | -52.13984 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b64c1a8-d217-30c2-ba0a-d700ef44c839 | -12.51758 | -47.86997 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c930619a-4870-3251-92a1-c475be78f822 | -14.17598 | -52.9329 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ff6101d-e621-3c80-a393-369251079253 | -13.40915 | -57.05278 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0150a3fe-3e1e-3b2f-b4a1-51c9978470a0 | -14.17605 | -52.92504 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48fad12d-04e9-359e-b227-9907ee445ee2 | -9.42686 | -60.4396 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff0061f5-26ad-3c79-b17e-a0a7c4d9848c | -14.5035 | -45.67424 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32436202-63a5-3f19-8803-10aec5d5bd1e | -14.03743 | -53.6579 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bab76b1-0c4f-3d8d-a395-5ed574ac9079 | -14.17471 | -52.91696 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a1ac9c2-bdbf-3253-9ff7-1e2fbd2b43bf | -15.2958 | -56.45157 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6464d22d-b9ad-3ada-9b5c-52b92d4c4eb3 | -11.71726 | -54.62165 | 2026-08-18 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f57da2f-0e29-3abb-8209-15ecaeeda380 | -13.40458 | -57.04843 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f26933-12af-30da-858d-79c7b86f6fd9 | -12.94121 | -56.64482 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47a1e967-edd5-30e1-85dc-a764b0142cf3 | -11.12053 | -46.49579 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da92b397-33cc-3a97-a156-182d43302e7f | -11.48688 | -45.10403 | 2026-08-18 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec6f2684-c6c9-336e-9cbd-f8157fafd98b | -14.17952 | -52.91263 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README26.md)
