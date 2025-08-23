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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ba322fe-8e87-3c94-bb2d-e9ad269e7499 | -9.24724 | -61.02077 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ab24ca8-2934-345b-8a40-3c6242cedcad | -7.95247 | -63.04821 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 932d9471-5af6-361d-ac45-18d54a35c81b | -7.82193 | -63.55733 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b428f1cf-973d-3c29-a3ef-126b6e08b2c3 | -12.7853 | -48.71763 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d08ec48-c6dd-39a2-b39c-ef8e4b9a966d | -9.16575 | -59.59268 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9320f213-ec1a-3819-a2f1-d55260ba4923 | -15.02028 | -54.8868 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2362ba8e-0bdf-3481-a48a-00402cfbee92 | -11.61901 | -50.42686 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4929477-3ca8-3216-8bad-b356c45868a2 | -9.94334 | -60.17091 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6409ca2c-b759-352f-8212-90626f23abeb | -9.25876 | -59.77598 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e10aa570-4ef5-326b-b147-4ffd2dd91053 | -13.42411 | -46.26171 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| abbb5c23-e203-32e4-9f68-dff0c486a6c5 | -9.81711 | -64.27174 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3b20bed-e048-3e41-8fc6-c9140bead2a9 | -9.19125 | -59.64687 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69c4f51e-c879-3fe3-afe5-63faf67f7462 | -9.21645 | -60.79931 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f8901b-3a86-354c-bcb8-85f23fedd8bd | -13.43181 | -57.17637 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc40f594-e0b4-3e97-9b4f-f85084b360d5 | -9.20611 | -59.44513 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac83f8f2-11fa-3599-a2b3-8ecb34f8e7ce | -12.77962 | -48.71197 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5b77af4-99b8-3539-b965-640a2a40df36 | -9.65544 | -59.64269 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f208e9c-75d2-397c-ad94-7b35421a5176 | -7.44857 | -57.62191 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d54ae2b-324b-30d5-b39f-1fbc5ab57c1b | -14.80239 | -47.94591 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e349240-f54e-32e7-b380-666186bcd36d | -13.41615 | -46.26786 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98aff177-dd7e-3978-bcd2-c1f05871460e | -11.19152 | -55.0413 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e1a6438-67c9-39e9-a937-f49069fe14ec | -9.24829 | -59.60949 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 226ca4d5-fe8c-3d9a-baba-4ff208347d44 | -9.25487 | -59.77896 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 991c96d1-13bd-390e-af1e-6c6327e83ef1 | -12.50992 | -53.82097 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa6721e-6b9e-396d-b6da-6589e00cf85e | -13.37515 | -46.22011 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32188f43-380e-3233-8de3-fb48213a2014 | -14.31309 | -58.55376 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7752450-3f8b-3189-b13b-7940848c85bd | -9.20666 | -59.44164 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc38118e-ff29-30bd-952b-0c270556da12 | -14.66125 | -56.58649 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3eb5089-87d8-3e62-924a-ed7631641869 | -9.52308 | -60.56107 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3fb6bc3-9ea5-311c-b6d9-6055484613fe | -7.55975 | -63.85793 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5943a77-e06e-380b-b716-6720ebc42fe5 | -14.91469 | -47.31557 | 2025-08-23 05:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 990e3693-7efd-3187-972a-98a9ef88511f | -9.19235 | -59.61843 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 69f30fb8-4d33-3071-94a1-601000e7f39c | -9.5031 | -60.51387 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a7fd0a8-111b-3e2a-a7f6-e82b421f1ee9 | -9.22284 | -59.77028 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e04aea46-3583-390f-bca1-e1e0747bdccd | -13.68652 | -57.7539 | 2025-08-23 05:21:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45a9eba6-f7a5-3b32-b5e4-a42f44631825 | -8.88536 | -62.43023 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab4bc25b-d62f-38cb-9e83-f67e6dbf54aa | -15.0182 | -54.8692 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cfb81ce-6644-3ec0-8fab-18079ce43228 | -8.88108 | -62.43378 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac0f05f-3a4b-3245-aca1-95a73d5f2b5e | -9.20058 | -59.45857 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0388f452-c6ab-3929-8020-d186ffa054a7 | -8.59982 | -62.62294 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea5f3a7-29e5-3b28-aae4-9e193ea4b129 | -8.69069 | -62.86281 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26d5a8ef-5e55-3fc2-9100-2842191c6735 | -9.51537 | -60.52319 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c58f7cbe-3d6b-3837-874a-265e01a496c5 | -15.00169 | -54.87671 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2981b748-5d78-34d5-8800-c2a69d09898f | -9.20557 | -59.47012 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98e96542-07b4-31c3-b60b-69bb2fdee936 | -7.10342 | -62.96969 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df8bc386-de8a-308e-ae47-fa48c0c15d2c | -9.15522 | -59.59457 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4414427-9bb9-36ed-bffb-244c15c46c0f | -14.26817 | -58.53538 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b26b6c91-85da-3fbe-9808-c1b701ba0cf0 | -7.50588 | -63.83814 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28dc2238-5be3-34c6-b2bf-f9903d4a865d | -9.50966 | -60.55888 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6f4b0c0-b8f1-3113-9f0a-07bea075b08c | -8.88176 | -62.42963 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee497d6-b644-3062-8ba1-a22aaa712856 | -9.65212 | -59.64216 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f38393a-b33d-3baa-8e99-0ba9507e6bbe | -9.17463 | -59.70872 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3974d011-062d-34b5-878a-c87369f5c678 | -10.75213 | -48.24836 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be459eca-d4b4-325f-9e8e-ab27d8b3b957 | -13.36591 | -54.40072 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4fb490a-a5e7-3334-ae0f-c5b03098bcb7 | -14.62345 | -54.84431 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7504e9b8-d426-3ebf-bfb9-eb0ee5cf9b8f | -13.42476 | -46.25537 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e25f12d9-be35-3f3f-aa9c-4d0b622c36e6 | -14.57457 | -54.50213 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41541aaa-9446-3510-88ed-d9c3e264e12e | -14.72608 | -55.41743 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70f83fca-643d-32ed-8115-d0f9d9b170c4 | -7.30582 | -59.6283 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e63c3f87-08eb-333d-bba2-9307c5fe3ca5 | -9.19124 | -59.62542 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b07debd8-1b9f-37a6-b993-c58787671a96 | -9.19448 | -59.45402 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b6df31b-af33-3642-a396-0e42ba022d20 | -15.02343 | -54.89606 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 140cfe07-7d95-3398-aeec-7ecec6a3136d | -9.08849 | -61.43396 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f774d4-3c21-3d9d-9a80-e9d31e80a0b1 | -14.29179 | -58.55441 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 838c41e2-4971-397f-ba01-ee3c1e98eaa1 | -8.53283 | -48.86334 | 2025-08-23 05:21:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 127b03d3-7d5a-3239-93b4-cef200ef7085 | -14.65174 | -56.59871 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c891692-12c0-316f-ae55-c7eea5794317 | -9.5203 | -60.55696 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 545be218-45d9-3639-b60d-401ceaa5a8bd | -7.73412 | -67.06806 | 2025-08-23 05:21:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fcd0bfc-dcf5-31f8-914f-e9b403b659ac | -9.44752 | -47.6596 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5cb7b43e-f261-3f49-b880-b59cf59bb02f | -9.10006 | -61.42813 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9a931db-f734-3529-8b51-0a507aa18b11 | -11.18354 | -55.04007 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06976bb2-6e74-3fc3-a1b1-4cfa220fbad0 | -13.02795 | -56.82889 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdbd721e-260e-389c-adf6-a2ed7c52ce0e | -6.87576 | -59.8225 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f5896c5-9e79-3d06-9b9b-56ee50582aca | -14.64784 | -54.92091 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 056e77ca-8182-3010-9768-2ff2db855491 | -9.21762 | -60.79207 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cda57ad-1878-3d93-8668-88f8192ed6ce | -13.36338 | -54.40646 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 588689fd-1e2b-36da-9951-e964e675cc49 | -9.16184 | -59.50968 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 731226d2-3413-3ffc-b63a-5ef2d89aafc4 | -9.5265 | -60.53966 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13b45f1e-ed64-3ab6-b73e-737da68c41ca | -7.79053 | -61.57393 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ef3d7ae-bacc-39c0-ac12-6f7e667977e1 | -9.19669 | -59.44004 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0aeecbd-8a40-3958-baa0-9cc7eac6d4d4 | -8.9013 | -62.42787 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a19116-6a05-3f80-8013-2dbba881dff4 | -8.89616 | -62.43206 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca52098e-751c-34ff-863c-2393e2febb99 | -9.50981 | -60.51497 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41b1743e-fed8-3e57-a18d-62fce8671e9a | -9.1918 | -59.64338 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a765f83c-bdb7-39b2-9e00-08e53befb2d2 | -7.30193 | -59.63127 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| babaabae-1a0e-3bff-9a71-d7749bb1bd19 | -11.32232 | -55.22046 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977913be-84ef-3765-b260-227a4af589cc | -14.94402 | -48.01382 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f9aecf9-3acd-31c3-b709-c182a470a3ae | -9.56196 | -68.57645 | 2025-08-23 05:21:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc26d0e-ff32-38d1-a201-fdf45208778c | -11.31956 | -55.22674 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1805434f-7d0c-3fef-a125-4b93d264fec7 | -9.15744 | -59.60209 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d97759d6-33fb-3c1a-8c88-ae77ecd4d21d | -9.94611 | -60.17497 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2b7e99-1c24-371b-af5d-426f2a7f8809 | -9.52151 | -60.52786 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d810186-b671-30de-9898-8b16a83069ea | -12.78238 | -48.70909 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 01d1234e-5888-3116-ac33-179d3af4e8cf | -6.83372 | -59.89189 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25de2400-3ad4-3fe1-9b98-343042554319 | -9.19402 | -59.6509 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b33e110-e09e-3b8b-8eef-1673ba525b53 | -9.52422 | -60.55394 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a44acd0-58dc-3c37-80d4-d0635e068fbb | -8.46457 | -64.04655 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06d08bd-3ca6-3f54-b9d3-5471f109dba8 | -11.30896 | -55.14483 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c11320db-bc22-370b-bc73-1f0ae46491eb | -14.75662 | -55.98795 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61741510-1449-328c-98d1-ac65284fb8a8 | -13.37504 | -54.39782 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
