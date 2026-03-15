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
| 5baaae07-cb54-3762-b9aa-91555a6714d0 | -8.7957 | -44.8084 | 2026-03-15 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1687d140-c846-3aa9-ad97-627e41820cdf | -11.78098 | -47.09619 | 2026-03-15 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b864c7ca-8bc7-3137-944d-5f56f3fb93ae | -12.6604 | -47.09539 | 2026-03-15 04:59:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb3da997-9b6f-3c65-b3f8-6b9f49785009 | -11.7855 | -47.09678 | 2026-03-15 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63f3a500-0055-3de2-aba2-5a888b3b84d2 | -11.78675 | -47.09408 | 2026-03-15 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c2194a-a75d-35e1-8d10-6938fdcf6d31 | -11.78223 | -47.09349 | 2026-03-15 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0a71cc4-4ac2-3bae-9096-14cb9687fa89 | -22.07098 | -55.32182 | 2026-03-15 05:01:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fdd5087-a5c2-3dc6-9a6b-77b3c1bc63ca | -19.87921 | -55.54826 | 2026-03-15 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 64e38e13-aa5f-3477-a4c5-31ca75f0ee07 | -23.45308 | -46.70116 | 2026-03-15 05:01:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a317018a-618c-3140-afa5-573952e4cfd3 | -19.87531 | -55.55135 | 2026-03-15 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 227bf8bb-577a-327a-a0af-41c11a0ecc58 | -19.87864 | -55.55193 | 2026-03-15 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7d09a552-33be-334e-b054-33af653cbbe3 | -25.2343 | -52.13298 | 2026-03-15 05:04:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6c430b3a-0a64-35de-b8c3-9582e70aa525 | -25.63907 | -53.38592 | 2026-03-15 05:04:00 | NPP-375D | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f8a36882-ffba-36cc-834c-e490a2d54104 | -25.63537 | -53.38538 | 2026-03-15 05:04:00 | NPP-375D | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9754df41-568a-36ec-8629-037e1515fa1c | -27.49379 | -54.48074 | 2026-03-15 05:04:00 | NPP-375D | NOVO MACHADO | RIO GRANDE DO SUL | Brasil | 4313425 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b49c75ce-d8e6-30e8-a02c-d331aef5fd1f | 3.13622 | -60.13547 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f1016ad-df1d-3991-9385-96d55a79e9b8 | 1.87198 | -60.53199 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07841295-3b21-3b43-b52c-e241944c6f76 | 0.9109 | -60.2964 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27626b23-441e-347f-a829-287211b45348 | 1.17641 | -60.00204 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7162a782-3877-3d15-846f-b113bd3d81f2 | 0.9038 | -60.29752 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be4d2d9e-7d72-3a23-95ed-3e94fa0d7893 | 1.47459 | -60.05761 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02dfc867-c24e-3c47-93f3-fe81eebd5558 | 2.30991 | -60.23934 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a6039f0-6bc5-367d-9876-210e7d6531e7 | 1.93702 | -60.37292 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 419c275f-4732-3314-8bbe-11c20ae96f20 | 1.95942 | -60.61064 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44372e15-fade-3ee2-9cbe-78402a0b8d91 | 3.20552 | -60.61652 | 2026-03-15 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8861c1f-b201-366b-8948-6984956b3409 | 2.94828 | -60.37632 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bf8e498-01a2-35c3-8cdb-5a83d1b46379 | 1.9348 | -59.99143 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0916149e-45e8-3e04-9736-7fee79f624ae | 1.1758 | -59.99812 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e178282d-3840-3ccb-b404-2eb60576ef75 | 1.87618 | -60.43348 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81a96ad4-e4f7-3a49-8379-df48f4db65d7 | 1.47042 | -60.05416 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 254cc726-e59e-3fb7-8810-b2077f816992 | 3.13983 | -60.1349 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a9991a-bba0-3dc9-b9ab-c54e9c45e61e | 2.94868 | -60.37746 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c422b60a-f406-39a8-805a-9a5f2654cc03 | 3.14642 | -60.12962 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da00e32e-02d1-303e-9c47-b7b958d01d8e | 3.14281 | -60.13018 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18554bab-5078-30c3-97fc-fc6e70421e5f | 2.31706 | -60.23798 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d06442c-d62b-3e81-8072-ac3e50ff9dc3 | 1.64914 | -60.2967 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2056d1b4-cded-36d3-a33f-1ea87e4fd2c3 | 0.8379 | -60.13163 | 2026-03-15 05:16:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8fb9fcd-e7d6-3675-b9a7-1e03cb18a1cd | 1.17228 | -59.99869 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5275aa8b-80e1-3b8b-a132-385893e0eee6 | 1.17931 | -59.99756 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dc5aeb4-b423-387e-afbb-79c8e798306c | 1.87915 | -60.42871 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2130d717-c7d4-3aa5-b84c-c484c633439a | 1.87554 | -60.4293 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2f0873e-48ea-34a9-ac8f-e213c78ba763 | 2.32063 | -60.23724 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aef16802-0232-3b4e-9f5b-1b88867c8baa | 2.31349 | -60.2387 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29de101c-9b17-3422-9644-ac473a5865d9 | 0.90735 | -60.29696 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 016aaefb-ef89-3900-ad67-89b959a60cc5 | 2.32637 | -60.20321 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82b02946-7775-3afd-950f-f9e839b28275 | 2.327 | -60.20726 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c495e051-0f26-31c8-b5c6-6d2715dd86e1 | 1.81876 | -60.33538 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5c54a8a-a01a-3ede-8de0-0fc8ad22b7b4 | 0.90672 | -60.29295 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e18400-b28e-3815-8e33-be5a14d8b8af | 3.14344 | -60.13435 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e128442b-2b4b-366b-8886-45b3e534da8e | 3.19487 | -60.37319 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c0b92e0-ed5a-3cbc-8c9a-6c91536e0ede | 2.24781 | -60.18449 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa79e486-b5c6-3efb-a72e-9ec39794699e | 1.04247 | -59.77164 | 2026-03-15 05:16:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3aa526-4b60-37af-be2a-6c78448023bb | 0.83438 | -60.13217 | 2026-03-15 05:16:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cd40992-6abb-3109-a03b-65609d8f3b5f | 1.10938 | -60.38763 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4159d3d-a775-3b87-8f8d-d77bec743fce | 1.55281 | -60.28163 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05c2ba9e-0197-32d6-94ef-a0fdeeeec429 | 0.90317 | -60.29351 | 2026-03-15 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a078ed9c-b044-39f1-98fa-2bd120c6576d | 1.42581 | -60.06953 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5076257c-32ee-3b26-b533-0145c4061777 | 1.54924 | -60.2822 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcabbbad-7645-3c9c-9f73-d4455a2f3b72 | 3.20856 | -60.61153 | 2026-03-15 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08384355-c418-3027-86cd-00eeb14e571b | 2.10394 | -60.19297 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41afbebd-743b-394a-8a72-5b800a8ce59d | 1.88148 | -60.4198 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a40d2382-fb08-3676-aa4d-43d027bc942f | 1.47396 | -60.05365 | 2026-03-15 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 432b79dd-910b-3d63-ac92-6342a72d5d3f | 1.9747 | -60.61264 | 2026-03-15 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0892524-e192-3e7f-80e9-a346069e2c62 | 3.15003 | -60.12906 | 2026-03-15 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0d7bb3-bc08-33d8-b87f-a1e2bdf25dd1 | -5.13746 | -60.3851 | 2026-03-15 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d1220c2-f020-3177-b295-42544c4861d2 | 0.85921 | -60.61247 | 2026-03-15 05:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0788229-59b4-3df2-8f86-864bbe6d9062 | -25.63839 | -53.38642 | 2026-03-15 05:23:00 | NOAA-20 | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 880410ce-0f04-3281-95e6-82d7d50f8692 | -25.23101 | -52.12992 | 2026-03-15 05:23:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1a1aa8c-37b2-3564-98c0-f4cea1c313ef | -19.87875 | -55.54729 | 2026-03-15 05:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 568a5a37-c7a2-3954-917f-297ee6def44d | -19.87822 | -55.55185 | 2026-03-15 05:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31c5a40f-396d-3bfd-9e4f-225409182cda | -19.87903 | -55.54918 | 2026-03-15 05:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 14e8cffb-e4f3-3db3-a0f6-712108d456a2 | -10.13636 | -36.23415 | 2026-03-15 06:03:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 59043676-4018-3037-8321-a8f164d022f4 | -10.14183 | -36.24225 | 2026-03-15 06:03:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| a6f22cab-0031-3157-9d95-a5d1538159ce | 1.96029 | -60.61171 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f921e110-39ca-3b4c-a0ce-99ead3281eff | 4.056 | -60.1797 | 2026-03-15 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec08155-f26b-3693-b3ec-3c2ad3ea42c5 | 1.93935 | -60.3756 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b3d7fac-50fa-3d69-822e-1d697c2bf271 | 1.17174 | -59.9989 | 2026-03-15 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6afb1276-d12a-37a6-a510-4edb5831bfea | 0.83286 | -60.13509 | 2026-03-15 06:05:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17e83e16-3992-36d9-b118-06c92d747a7e | 1.95495 | -60.61264 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0accdbcb-7db2-3a02-b086-aabc0dae4cef | 0.83644 | -60.13291 | 2026-03-15 06:05:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5172c333-a05c-39de-8580-bbc0edbd1225 | 0.83229 | -60.1314 | 2026-03-15 06:05:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85cdb99e-f09f-3568-9fe8-0af7f47e3295 | 1.17739 | -59.99804 | 2026-03-15 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2abf16bc-8932-3d18-96e8-7b0ba39dbf9c | 1.55129 | -60.28177 | 2026-03-15 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| becf59ea-1e45-3d0b-8657-e25b6e59761d | 1.93576 | -60.37611 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4398369e-b9d2-3a7d-ba9f-44f19bf53f3d | 1.87566 | -60.4295 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09357183-697a-34d2-a5cc-488387c2b70f | 4.05071 | -60.18074 | 2026-03-15 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7553ab8-a920-3b98-80bd-b97191b83362 | 1.95975 | -60.60833 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a948139-61fa-32b1-8387-208560a4dcc0 | 0.83083 | -60.13383 | 2026-03-15 06:05:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7a29e29-436c-3539-aefd-9552557aea25 | 1.87623 | -60.43295 | 2026-03-15 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274d9ed7-408a-3a90-8f52-fc586b2b257d | 1.64411 | -60.29548 | 2026-03-15 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73b906e0-bba2-34de-a6b7-62853b54bf1c | -4.79117 | -41.68859 | 2026-03-15 11:47:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 120f39dc-6e01-3023-986f-a5d32a7ceb80 | -6.31166 | -39.15922 | 2026-03-15 11:47:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 8012752c-0410-345a-b37f-affe038cbbf5 | -11.05262 | -45.38846 | 2026-03-15 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca4ed944-0d1c-3497-a639-f83fce770b6d | -9.362 | -36.9181 | 2026-03-15 12:20:00 | GOES-19 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 7676e7b5-3744-3320-9156-3890501d78ae | -9.362 | -36.9181 | 2026-03-15 12:30:00 | GOES-19 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 2415440f-285c-3a34-82b0-6de2bd2b5408 | -9.362 | -36.9181 | 2026-03-15 12:50:00 | GOES-19 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 97.7 |


