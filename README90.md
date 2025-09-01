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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 332d1909-f3e0-3a34-aaeb-733c02f027ae | -8.66225 | -62.92855 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad9c2a0f-4ab0-3c7e-b3a6-39ee4bb43f74 | -9.48169 | -65.59889 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9606fe66-cf66-324a-8705-6eb356870f7a | -9.12499 | -65.76569 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba781c8d-908b-3707-9910-024324b2c397 | -10.27445 | -64.29563 | 2025-09-01 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d86e6a33-58a4-308b-9972-b83a67da57ed | -10.0863 | -68.47221 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a58fac97-689c-3269-948f-c8d43e3b404c | -9.02294 | -70.65975 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09222829-5f5d-345e-bb45-598ba7cea004 | -9.83891 | -65.05305 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 802931db-15c8-3967-a4b4-9a8bb0a94a05 | -9.82423 | -65.05486 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64e09c78-f629-3d53-bf49-ea61547d84c8 | -9.4412 | -60.57682 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 989f67de-eeae-3e06-92cb-19753d2deb65 | -7.9356 | -63.00698 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5fb5d7a-158f-3cf2-8c11-bc332f041373 | -9.00373 | -65.69084 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daf6f3cb-e8c2-3f8a-a04c-2b08d84cc3c3 | -9.04878 | -65.73885 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e45be61-9884-3363-a211-95b0df5434a5 | -9.4366 | -60.57621 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd9d9d19-aec3-3ead-ab03-9c7773cdbaf9 | -9.0724 | -65.4263 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7f86681-4d8e-35d7-bb52-0f0cc74c4a66 | -9.44646 | -60.57275 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5e4dcfe-00b5-3da7-8c30-5c07efe226ff | -8.62803 | -62.59023 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24aa12eb-1dc7-3e71-b232-5c57ba1480b5 | -9.48513 | -65.59942 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af17cf51-525c-384d-83fd-ca629890d346 | -9.14696 | -65.84837 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05dcb254-4947-36fd-bdbe-7a61e2be0c83 | -9.87126 | -65.02966 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e40a22ee-5045-31b9-87ef-b04a7433c92e | -9.95563 | -66.87563 | 2025-09-01 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8a44045-38af-3704-992b-10e068a48e54 | -9.4585 | -62.34312 | 2025-09-01 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8618a2f0-c1f5-3934-b065-26acd751c0ef | -9.06493 | -65.42901 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfdb8857-dbb0-3ecc-b3ad-5c14653b274f | -8.76226 | -61.42846 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dae4ed0-7c7b-33d6-9074-3dbb20e00d86 | -8.03566 | -70.08823 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a72a43a-7564-3eb6-862e-5ab207f34350 | -9.12721 | -65.54555 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d107e80-ec64-39aa-bed7-b6d1a85ffc54 | -12.43272 | -63.92642 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12a560b3-a168-305a-94ad-5a0729f7a5f1 | -6.92777 | -71.78115 | 2025-09-01 05:53:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c323bec-0fee-3c86-948a-4190cb70600d | -9.11928 | -65.73465 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 646a3a6e-e197-3599-84e7-7f5ba7cdfc84 | -8.75797 | -61.42782 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b4eab1f-481c-33cc-8015-d1c164152894 | -8.7894 | -62.92997 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74eca14a-bce3-3c4e-9280-02b41aead1e4 | -10.76201 | -69.47796 | 2025-09-01 05:53:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b54f3e66-5946-3daa-a4fd-01a2965f75cd | -9.83598 | -65.04855 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44c2a89f-47fa-35bd-9f8b-374f27e7ae9e | -8.76399 | -67.2979 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9a3e31-709d-3acd-a183-42a996c37792 | -12.4414 | -63.92943 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c872c865-b052-3d0a-b184-6d6d78b22f21 | -8.42822 | -62.29002 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bbd108-49c8-3b22-9518-c57442ab8c1f | -8.81249 | -71.05199 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0b7884-9ac2-3bf3-a046-3b0c1b03f783 | -9.13631 | -65.85036 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a795d4-1615-3fbe-923a-0f036b852047 | -9.88071 | -65.01487 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 957c6a86-2276-3e2b-a15c-fb57545f6b38 | -12.44042 | -63.92754 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c459fa-5ecb-3718-978b-2401f94d7f7b | -9.69379 | -65.01094 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4b21109-eb2c-3d0f-9d96-92b2d975595b | -8.06283 | -72.35216 | 2025-09-01 05:53:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c1b3e0-497e-3a98-8afe-6f1a250d5608 | -10.50343 | -68.10876 | 2025-09-01 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac6f786f-9405-34cc-acbb-e1da7bc7b4e7 | -8.60493 | -70.90688 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c1ead36-529a-3ef6-8687-ac311bb39165 | -9.05746 | -65.43172 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f2ce02-b389-3ad5-90ee-640c4828d8fa | -8.6201 | -62.58907 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e75115-3eee-3e04-983b-2c42d4a2c174 | -9.00209 | -71.57983 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0676b8ad-fbf8-3aa5-b551-d3927da52df5 | -9.82482 | -65.0509 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 812f7b06-70aa-3af2-889e-53cdcd0954e9 | -9.06264 | -65.42092 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 951efd6a-dbef-33ca-a473-9f73075c7993 | -8.35374 | -70.26382 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df40ee42-442d-3acd-a8b6-bb3bfe97cdda | -9.17475 | -67.56768 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f18ded6-c22c-33d9-9b69-0013ed908a90 | -9.26112 | -67.64249 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fac5c6ab-7e2c-3213-b900-be90fdfc912d | -8.22591 | -62.94025 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b300b6-bdb7-3c46-9572-a3cefa342ce0 | -7.90355 | -63.01183 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e139de-cfc5-36cf-adea-e5473627b438 | -8.37959 | -70.75549 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba6fa7dc-e410-3866-9c02-c7ac1b060b4f | -12.44427 | -63.9281 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9df5b2a-8abd-31a1-af40-893ce738e1b1 | -9.14016 | -65.84731 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a89460f-1fad-38b4-aced-409dac9aa03e | -9.07929 | -65.42738 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51ae7e34-d096-3cff-9884-9029fff36ff4 | -9.88544 | -65.00746 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f7bed6-5f45-31b5-8995-d5d1dcb2af3a | -9.13064 | -65.84196 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca345ac4-218a-36c2-8a49-9037505aee7b | -9.86833 | -65.02515 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d17739-7830-38d7-bc5e-45393dc9e6e0 | -7.93418 | -63.01643 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4580c3b2-f5b3-31c4-9401-8a38f863dfcf | -9.02658 | -70.66035 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 389862b1-0c53-3fad-b2da-8b2a54965590 | -8.97504 | -65.9678 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a14af7bf-e5b0-38ef-ae3d-0ff579e22655 | -8.22977 | -62.94083 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6367a7ef-6841-3bda-ade5-1fd9eda61151 | -9.4458 | -60.57743 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef8daec1-a648-3585-84ec-c34b8269b8f1 | -8.90595 | -62.10493 | 2025-09-01 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 879e612d-f522-3fc7-9280-c904649e99d0 | -8.97221 | -65.96364 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3005bac-322f-3014-86be-b6b9ad22d85e | -8.37451 | -70.85368 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fa6b84-1e47-3140-8e53-fa258f055641 | -10.57792 | -67.76029 | 2025-09-01 05:53:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7e1c51c-dbf2-3f11-98de-2e70e34b06bc | -9.45106 | -60.57337 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a22930f-596a-335f-bb62-24721a4be3d7 | -8.61216 | -62.58792 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857552d9-7e35-3fc8-a926-f537cdd670f3 | -9.86773 | -65.02912 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cf484dc-b73c-349f-88a9-ece53282658c | -9.13348 | -65.84617 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 923e304d-a29d-3613-a4ef-08ead352a7e8 | -9.13752 | -65.54714 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc385931-6c38-3502-8da8-b0b9f5c70f05 | -9.02365 | -65.69772 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872d65a3-f077-3164-b8b2-109c9fc19697 | -9.13461 | -65.83883 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66e96af1-8a41-38fa-a649-be30dd161f5c | -9.13007 | -65.54982 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0771b252-f4ef-3e64-883b-3c40458bfca1 | -10.84211 | -55.75435 | 2025-09-01 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84c291d9-e148-3fc4-bd86-ad04eca14046 | -8.65376 | -62.93231 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba7a8427-130d-3042-b964-c9f60d8c5819 | -9.83246 | -65.04802 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b5fa3d9-a49c-3828-a3e9-9e40dc3a9cca | -9.13694 | -65.55088 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39b86cd7-de74-3faa-83ab-bac5a7347f07 | -10.08575 | -68.99856 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d96fca7-de09-35a6-84df-83ab23c5456a | -8.65836 | -62.928 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe246970-c376-358f-9e4b-5f0e0f0f533c | -9.16843 | -65.55191 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd576a7-1d94-3ac3-be34-beea9cfb31a6 | -9.85781 | -65.26044 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6e8db37-45d7-3fd3-b650-2e18fc3cad97 | -8.95017 | -65.94904 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4199c1ed-fd19-35e8-b16c-0c64f6d6923d | -9.17197 | -67.56365 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9673d885-0176-3a66-963c-4d82978ac54f | -8.51884 | -72.69874 | 2025-09-01 05:53:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d24c841b-22a2-3acd-9aaf-0971e00c6472 | -7.67824 | -72.50723 | 2025-09-01 05:53:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53661524-f94d-3595-900a-18001c521559 | -9.8342 | -65.06042 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acbf59b8-1332-31b2-bc75-884d3abc7617 | -8.6688 | -62.82915 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2033abb7-f111-3ad0-8219-4376f16e16c0 | -10.27077 | -64.2951 | 2025-09-01 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ab5e47d-0989-37f2-99b1-d183f50e4e7a | -9.14412 | -65.84415 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e31b0e3e-c59f-3c35-8650-efce732a8f7e | -10.07464 | -68.26687 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e079cd9-0f26-3a3b-b50d-c863319ccf44 | -10.2688 | -68.79156 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd99a67d-b628-3b73-a2f2-54510035fa47 | -8.63446 | -62.60159 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ad5a88d-183d-3d31-9186-15acf7398bbb | -8.72023 | -62.41809 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40f1abce-69d7-32b8-9e36-daa589525e1d | -9.87778 | -65.01035 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de395bb3-f12a-3ade-b72e-01750c9faef8 | -8.88128 | -69.46741 | 2025-09-01 05:53:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 000787e3-805e-380a-8a59-b7378b4cb496 | -8.7574 | -61.43184 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README91.md)
