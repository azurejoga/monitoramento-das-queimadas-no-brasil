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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5ec1994-c00c-3a2a-99a1-4e1bd8b2e8b8 | -8.8968 | -60.5476 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 703d589a-4f1e-3296-9420-0d39838e0fbb | -6.84897 | -58.96849 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25bf0d44-90e3-3f8b-808a-a60fef874d0c | -6.20731 | -55.49179 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9f4eb7-17cd-3197-998a-f139df8ce4f2 | -6.87231 | -59.42925 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed077192-da99-3296-8fda-1cf8e93f392e | -8.5757 | -54.77818 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 587843c1-4205-3e9e-85a5-8f0a11b3f3ae | -7.59997 | -60.94362 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96058817-c9e9-3c9e-9550-626a2018dc02 | -13.93385 | -53.85679 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f3007fd-e467-3504-839b-75ffcad2cdaf | -15.72108 | -47.79305 | 2026-08-21 05:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9504bf6e-ad4e-3388-8b3a-4f8cc1cf8da4 | -6.85077 | -59.41053 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccb3debb-133b-3250-800f-733170d7b522 | -6.10096 | -57.86471 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83882a36-8fe8-3d02-88ca-83fb09a63a0c | -6.91617 | -59.35299 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13151902-248d-38e5-a16a-42dd1efa2c57 | -6.21593 | -55.48169 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93f9d214-c914-3ea8-ad9d-347b491e7192 | -13.67915 | -48.76521 | 2026-08-21 05:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4cc6462-5816-3e86-81c7-ee4171cb5206 | -5.81951 | -55.71988 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40447248-63dd-3e26-aeb7-09a43c654d7e | -8.58805 | -54.74561 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0607846c-f2db-3638-b8a4-5ca50ba641b2 | -6.94327 | -60.08261 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad82d550-0494-356b-a2de-8bfd6f19b345 | -14.0954 | -58.85854 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bfb4d57-80f7-3374-9c84-ca1d25cc471d | -7.45557 | -46.15681 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68f8d359-95f1-3624-b4ec-ef70524d35a1 | -13.43807 | -51.81767 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 903a96a6-a668-38ea-a261-0b4cfa4ab9ce | -6.23278 | -55.39616 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26ed67f2-3592-345d-842c-0fa8b2d89f64 | -7.63055 | -45.76962 | 2026-08-21 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b137eba-6cd5-327f-8e53-126eaf5f017e | -12.51264 | -54.76139 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67451b76-21d5-3c5e-95ec-a9dcbcd69f3a | -13.38374 | -54.37385 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 9bbc22e3-e6dc-3595-a151-11f0a951ac86 | -14.72544 | -47.14243 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c46103-18c9-3962-a3fa-f36d81d6a853 | -13.3963 | -54.37057 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 147273b4-35ac-3a7f-8fc0-110335ca0c57 | -8.39407 | -62.69398 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c423dab5-06d3-3b21-af4e-ec795b1a7cb8 | -6.0893 | -57.91631 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3948332c-3a94-3fd9-81c7-3c6b62e8343a | -6.60956 | -58.39071 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b46a021f-5356-30fc-979e-573a0341c273 | -6.90075 | -58.9955 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e903a935-dc7e-3d7c-844d-6897ad076e94 | -6.95687 | -52.8156 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1aecfd1e-860c-3e9d-a0fe-b15da5b30b9b | -9.20708 | -59.77287 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee527de-eb6e-3660-a9f9-e3b4015d3e34 | -15.16775 | -48.78806 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e617829e-7df3-374b-8abc-76a4ef1c9181 | -6.64323 | -56.41768 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f26b4c46-caef-3ade-b50d-a5b96174f7ef | -6.13675 | -59.91296 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 356d544a-2043-3dc0-88dc-efe677a4993e | -7.37398 | -45.80915 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0e992d9b-214b-3901-99b9-a1065bd15de7 | -6.58388 | -58.98929 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a884f0-d20d-3e33-9c71-fbbef649a9c4 | -8.277 | -57.35209 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a95375a-b1f6-38ad-9220-45a7b6a42e8c | -8.11053 | -50.03027 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6318e264-29e5-33af-9df4-3e0f6c0cf80a | -6.21535 | -55.4854 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf800b44-6931-318f-b7c9-74b3b1f9953e | -14.02325 | -58.86898 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f370b280-e1b8-3e3e-9781-ffaa05f9b596 | -9.21196 | -59.65701 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7acf160-285a-3356-8610-0698b3f590bc | -8.7148 | -49.61291 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf5bb64-914e-3240-a702-64ef012cc5e5 | -6.25962 | -48.65199 | 2026-08-21 05:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5b3e81c-8921-3692-99cb-84b1fa869c59 | -6.11507 | -59.91346 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71f44080-692e-3412-8e9d-33cf2dd12a16 | -14.46197 | -45.62618 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a9366fc-b8c2-3f7c-8747-246a60fe1088 | -8.10895 | -50.04197 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bc259a4-4e77-3a70-b4fc-bb0fa405f4ed | -6.97584 | -59.591 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5bb81ba-b164-325d-8f4e-00d54fe40517 | -6.55203 | -56.26482 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2f4131e-b0a8-3e94-bc96-48d9ce6ba143 | -4.94121 | -55.77855 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b45b3869-7366-39be-8c09-de4c98ff84bb | -6.88811 | -56.43394 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16b99b14-5081-30c6-943f-f06a7edb9f0f | -4.53304 | -55.6204 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8fdae0e-9813-34ad-b655-882aa92dfee2 | -14.2053 | -52.87969 | 2026-08-21 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4568e1fa-bddb-3675-9a96-b07a83ada0f6 | -6.83207 | -59.39609 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e351426-47a2-387c-978a-42481fd2429f | -6.16552 | -55.44318 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddaf9d3b-0225-3e72-9360-34f7b46ed877 | -9.2495 | -59.81423 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394a0626-fffc-3175-a70b-95157b539ebc | -6.59841 | -59.11457 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89184904-1b2a-36cb-9787-051e7d687fa7 | -10.6618 | -49.01914 | 2026-08-21 05:23:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62917a4f-909e-34de-b721-9c32576752ff | -6.72045 | -59.09273 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ec7fd4-6435-3c83-962d-b5a387f49667 | -5.86897 | -57.66447 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ba578bf-70be-3a78-941b-745286e695a4 | -7.05384 | -59.84337 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7c2127-680f-3b50-85cf-3db23db066a9 | -6.86205 | -59.42756 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8898010f-6d08-348a-bc3e-805816f54f9c | -9.05921 | -60.43752 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4dac691-f5be-3051-9cd2-e8426f4958a8 | -8.37562 | -62.70661 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e476eb16-672a-312a-a091-f657be9d86ea | -8.37165 | -62.70595 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| faa12249-ebca-31f1-99b5-9970d9a7b507 | -9.15872 | -59.6632 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d530f7d-d2cc-3002-b845-720f1cd09473 | -8.49911 | -54.86954 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d3252d-c691-3857-8cad-03f5d8989653 | -8.17864 | -54.99368 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fd68d50-9edd-3e69-a9fb-441a972fb0be | -6.55259 | -56.26124 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 220ad2f7-c314-3db1-9b57-44d602a0c189 | -7.572 | -60.86602 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0d669bd-da4f-366a-9de0-1ac0e67ce350 | -6.76196 | -59.46482 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4941c757-1007-3aef-9cc8-5adbf457b06e | -6.01504 | -57.82973 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc573bd0-2a9b-344f-b5e6-7afcd9551d9a | -6.24904 | -55.42094 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb78205-2ba8-3db8-99ed-7c2c8d78bbce | -8.1049 | -51.66971 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5ec4645-ee22-38b5-8d87-b73c4ce7cc1e | -7.02661 | -56.61564 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5843d4aa-f812-330a-a292-0a0c1e03dedf | -14.726 | -47.13703 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1e2ba07-61b1-37eb-9fb0-7f3d9f4ecad3 | -6.87123 | -59.02774 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83be1e21-2dff-3213-bee4-486684710b0a | -8.52141 | -54.86863 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21bfaca-7d46-31c1-88eb-f835c1af7180 | -13.74123 | -51.85388 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb4185fe-ac14-3296-b7b0-37ea76da2739 | -8.22088 | -55.02883 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08d96678-d1a0-397c-9b7c-d8c450acb14b | -8.61808 | -54.71952 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 145d92fe-2ea6-3335-b30c-3b19db6dca6b | -13.44274 | -51.81842 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0df568e6-a8d1-3367-99a4-ab09f284ba6a | -6.37878 | -54.9454 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04aa62a3-c27c-3b29-bc8c-2f710be301b1 | -6.42044 | -56.18564 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36066292-ce6d-3f7d-9054-8f38bd53e98a | -5.80249 | -55.71727 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a1237a-675e-39ba-95b4-0243e95e9c05 | -6.87915 | -59.43039 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a71a5b22-4895-36cf-96b3-8d2a80436c5c | -7.00701 | -56.54344 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d1ca76b-2647-3c57-99e4-59b58730a9a8 | -6.20504 | -55.48379 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bcc79ec-f6fe-341d-b2c8-f784c1413d3e | -6.2016 | -55.48326 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c44f7519-1b3b-38b7-8806-ff96cb2f5e7b | -4.92025 | -56.26223 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0ca6c1a-d87b-38d2-8704-ed927dfa7ece | -8.38838 | -62.70351 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c20e8a35-e57f-3222-a487-521f042b1e93 | -6.76435 | -59.14805 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85b373b0-de70-388d-a257-2172eea2fdb3 | -6.16838 | -55.4475 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cacf6d09-d854-3f32-8f31-b3f105eac994 | -6.43858 | -54.95334 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db00f0a4-42a5-3cb1-a99c-51886b814276 | -6.39055 | -54.93914 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9c4e06d-5471-3d06-8df1-177b9257fd0f | -9.21669 | -59.77822 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc0f8557-01b8-315f-a249-ada48b21e318 | -4.34899 | -59.54095 | 2026-08-21 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d2accc-cb4c-3714-91ac-33ca4e10d1d9 | -8.09604 | -51.66632 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c123b58f-7faa-3136-b2f4-8430904a56db | -6.88882 | -59.43575 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 521288f5-b2f0-3909-8392-a5d9f61ff1dd | -6.69309 | -58.9397 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f96b2f05-b4b9-3fde-9989-ec00958f575a | -6.89855 | -58.98773 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README56.md)
