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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 365e482d-3dff-3c5e-abd7-3e51837f3882 | -12.23705 | -49.38291 | 2025-11-18 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d9499a0-f079-35e8-8e62-da04c142d173 | -10.05501 | -54.32415 | 2025-11-18 05:12:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac3ccf09-7a0c-32ef-88eb-de7873d08848 | -12.19221 | -61.06986 | 2025-11-18 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db349917-d829-33ce-84ae-ff50c8a0c653 | -14.59064 | -47.99173 | 2025-11-18 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ffc7e3b-0228-3c66-a50d-0c80e5c5090e | -12.69981 | -46.79909 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6424bf22-72e6-337f-9233-7ff85675fc53 | -11.39813 | -61.17896 | 2025-11-18 05:12:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48fe823d-82aa-32c2-8607-77337a3b9456 | -11.55811 | -48.46593 | 2025-11-18 05:12:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc563dde-4800-308c-864e-0b7fd3f4fb39 | -12.00484 | -49.26995 | 2025-11-18 05:12:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5af278ce-26df-3c97-9ec8-4b544e248f33 | -10.39035 | -59.18976 | 2025-11-18 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d9b009e-6b8e-3a07-a505-71994fbc5f46 | -12.70236 | -46.79671 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73cea0d7-46a6-3d7c-9890-317789112056 | -11.52092 | -48.95965 | 2025-11-18 05:12:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a8e1d41-c725-37f1-979a-a6716a52c0f2 | -9.32697 | -64.43848 | 2025-11-18 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1996bc5c-4aee-33a0-a227-a700ae3d938e | -11.84585 | -49.23073 | 2025-11-18 05:12:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c142307-b189-3ff5-aa6b-3a6a494e99ef | -11.20908 | -49.41543 | 2025-11-18 05:12:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52b68a37-abce-308a-8193-e1e81c8aacae | -12.89775 | -54.72089 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e64139-0a12-3336-8fda-2a378bdc6332 | -10.14194 | -64.89766 | 2025-11-18 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c26e730-7f96-3fb0-990c-69feb37ae73f | -10.6581 | -49.37783 | 2025-11-18 05:12:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd2ebd07-c1fe-3f61-a6d6-0a0c147159f9 | -11.07902 | -59.11383 | 2025-11-18 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a9ab617-4b53-35c5-a3ff-151e8a1b8acb | -12.66634 | -46.75233 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e76a9acf-ff38-3858-b4fe-1bbfa6c795bc | -12.41686 | -54.35381 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4d81e4-ddb7-3058-859b-8b7cc2576930 | -10.58818 | -49.01031 | 2025-11-18 05:12:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc582947-e491-3e58-94dd-e3bd76e2207e | -14.59208 | -47.98984 | 2025-11-18 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12ef843f-8468-3ad7-adee-4ed4bdab4bb2 | -11.84628 | -49.22734 | 2025-11-18 05:12:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c97ce34-6707-322a-9b70-caf55520ee36 | -11.85167 | -49.22809 | 2025-11-18 05:12:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b628fcd-7816-399d-8e51-2acc0fb18ff0 | -12.89708 | -54.72569 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66818750-7155-385c-8f10-e6c5f624daf4 | -8.84823 | -62.85202 | 2025-11-18 05:12:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ce8c24e-bb00-32db-8872-dd4fca05f9fd | -12.69583 | -46.77759 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79b701c7-5cb6-346a-bd84-28cd561cbd0e | -10.79676 | -47.64342 | 2025-11-18 05:12:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4bd3cd0-6fdc-392c-80fb-b94df02a391d | -11.55858 | -48.462 | 2025-11-18 05:12:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0a81128-f13d-3797-a385-c082f83fb94d | -14.59015 | -47.99612 | 2025-11-18 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef528ff-358c-33b3-9d35-d52b4a7c68b4 | -12.88017 | -54.7404 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50dfe5d4-6b88-313e-8eee-cee862546c12 | -10.99449 | -50.92415 | 2025-11-18 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22e25ce7-7a61-3b11-83d9-a51c2469c508 | -12.69186 | -46.77433 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6cd3a02c-d35a-3e8a-a0f8-4cbab78b7af7 | -10.54015 | -47.99561 | 2025-11-18 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a6ce637-4118-3bab-b87a-0c763c722dba | -12.87924 | -54.74245 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48c4520b-8ce4-3f51-9e9a-546ad92beb3f | -11.99901 | -49.27279 | 2025-11-18 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07d9fa55-79ae-397d-8400-fd4fad91a717 | -14.59604 | -47.99825 | 2025-11-18 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e22064d-6cd9-3f18-91b5-af10573d0a2b | -8.84764 | -62.85548 | 2025-11-18 05:12:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ae83bf4-c0d9-3684-8a34-e1243000c543 | -12.89328 | -54.72514 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 732f486b-0c12-3fb4-bab1-e6341b27bdc8 | -7.55338 | -63.44687 | 2025-11-18 05:12:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec36394c-5869-3bf6-9ea2-7b17e051ce0d | -10.65852 | -49.37461 | 2025-11-18 05:12:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0f0fca0-f0bc-3ebd-951f-143e680282a6 | -10.27996 | -60.5312 | 2025-11-18 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af9fa9ba-8171-3687-84b7-932a0a130f0a | -13.20322 | -48.32042 | 2025-11-18 05:12:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac043116-1eb8-37d0-b415-35114b9b9b0e | -9.93073 | -59.53315 | 2025-11-18 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f68a00-9bc1-335d-a50b-acae9c3ad1ed | -10.55721 | -61.15449 | 2025-11-18 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7dd1ee0-b077-35d0-acbc-53c4733bb4cf | -11.56145 | -48.46343 | 2025-11-18 05:12:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5be1a6a6-2117-3575-a2f8-c69ea0220247 | -11.83932 | -47.60044 | 2025-11-18 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 277d4fbf-ab26-32bb-b5c3-8f55c97f6df2 | -10.58278 | -49.00966 | 2025-11-18 05:12:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22478f95-b0df-38b4-b9e4-64f14513fca1 | -10.23945 | -58.17346 | 2025-11-18 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a74b7aef-bb5b-3055-8eee-12c520c3177e | -12.70222 | -46.77834 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f17336-e738-3346-ac61-8a50fa665728 | -12.87637 | -54.73983 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1afc01ee-006b-3340-80bc-4fa4403861a5 | -10.81113 | -55.5685 | 2025-11-18 05:12:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07f3309c-8909-35ea-b279-88631c2fbabd | -10.65936 | -49.36814 | 2025-11-18 05:12:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69fdbf82-3662-3366-86b7-390928c380a4 | -10.81203 | -55.56638 | 2025-11-18 05:12:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8a61ed-7dee-33f6-8014-aba5d9efb761 | -12.00239 | -49.26904 | 2025-11-18 05:12:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 74fee542-b966-31e7-a36d-f07fe227a953 | -12.00194 | -49.27256 | 2025-11-18 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 408002e3-8436-37dd-bd37-8d97fed5d116 | -11.2038 | -49.41466 | 2025-11-18 05:12:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c5b49fa-4204-34b9-ab99-3816334d6d65 | -9.06129 | -61.67374 | 2025-11-18 05:12:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b951c151-7661-3bd0-9ca1-89cda04e02e3 | -10.6642 | -49.37208 | 2025-11-18 05:12:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870de345-9542-3c54-ad13-637a6785d51b | -11.99944 | -49.26927 | 2025-11-18 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 442f6849-a925-3318-8c2a-e9e190bd74c7 | -12.69825 | -46.77509 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 331b7cd3-c88e-37c7-ab8e-2b50f0f05fc0 | -9.59743 | -63.35909 | 2025-11-18 05:12:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee86702b-28eb-392a-8252-ac6b1b846459 | -10.53911 | -47.99692 | 2025-11-18 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b46daef6-504d-32b2-8750-eca5511eaff7 | -12.19567 | -61.0705 | 2025-11-18 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 604c2b40-4562-301f-9168-bf1682ac8ef8 | -12.69523 | -46.7828 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 091ee822-8adf-383e-8cf1-f37cf5fa8738 | -9.8923 | -44.1681 | 2025-11-18 05:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 974bfbc5-8c6b-36fb-8921-be0df69a931a | -9.8919 | -44.1914 | 2025-11-18 05:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| c699eb02-0a73-3239-9798-ef5b9e6e432c | -9.3969 | -48.4523 | 2025-11-18 05:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3511bdc2-c023-3afd-beac-b40c29a947a3 | -9.8729 | -44.1938 | 2025-11-18 05:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 00c99c6d-a178-3df4-b2ee-c8f4fd797397 | -9.8732 | -44.1705 | 2025-11-18 05:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 138da5af-cbd8-3ff0-b3ce-d971431bc084 | -1.9292 | -48.7946 | 2025-11-18 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c5c68372-4285-34d6-915a-5b71efbfe34b | -4.6547 | -47.9444 | 2025-11-18 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 5d048d4a-5bca-3807-b491-19431bb1ac70 | -1.9292 | -48.7946 | 2025-11-18 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| eeb1ec48-5e13-3fe6-9061-c447e4757b9c | -9.4158 | -48.4504 | 2025-11-18 05:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 88e96b77-44b3-3e9e-a96e-707158570132 | -9.8919 | -44.1914 | 2025-11-18 05:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 96680b72-3b87-317f-b74d-237d74e8f5a3 | -9.8729 | -44.1938 | 2025-11-18 05:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 565fbe28-1b7e-3f8d-99fd-9a6285add40e | -9.3969 | -48.4523 | 2025-11-18 05:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6af8248e-03f5-3dc2-866c-c7d832e79e9e | -4.6547 | -47.9444 | 2025-11-18 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 5f202ed3-e5e3-30dc-97ea-d5a797b27be7 | -9.3969 | -48.4523 | 2025-11-18 05:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3e4548c6-8a6a-3074-ad2c-410e89970ef5 | -9.8919 | -44.1914 | 2025-11-18 05:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bb2e72da-c8ce-3949-8682-5ac83e6a5ff1 | -4.6547 | -47.9444 | 2025-11-18 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 1d65595f-fb56-32f8-97e4-10fa1cd97ff3 | -9.8729 | -44.1938 | 2025-11-18 05:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fdbc523f-437c-3a42-b459-671d912acc99 | -4.6547 | -47.9444 | 2025-11-18 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cfce4521-6b78-3bca-beff-2b4eabdf7af8 | -9.3969 | -48.4523 | 2025-11-18 05:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 50d91423-0baa-3e61-abb3-96a6678fef2d | -1.9292 | -48.7946 | 2025-11-18 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f618139b-da47-35bf-a5cc-235f15d0a058 | -4.6361 | -47.9453 | 2025-11-18 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 35e6ca49-2822-3591-aac9-2e88ca402e22 | -9.3969 | -48.4523 | 2025-11-18 06:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7fade01d-da31-34ab-8948-d0794816142d | -9.8919 | -44.1914 | 2025-11-18 06:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 71903f04-bcf2-364a-bd6d-94692aaea211 | -4.6547 | -47.9444 | 2025-11-18 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 58084b26-945c-3756-904c-692517c611d2 | -4.6361 | -47.9453 | 2025-11-18 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| cc49c8d8-4a71-3a99-b8ff-722708f516ba | -9.32591 | -64.43795 | 2025-11-18 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe1d1307-cb4c-3c68-bebe-13c9b6b18458 | -9.06393 | -61.67282 | 2025-11-18 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 441d69cf-944c-33c4-80ca-6042c94eea02 | -9.49255 | -63.50793 | 2025-11-18 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af628e04-3f8c-354f-81d8-7b271618dddf | -9.03137 | -64.03644 | 2025-11-18 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6553c16-b5ea-3fff-bf46-a64cfca6a3d7 | -9.49322 | -63.5031 | 2025-11-18 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40dd9a4e-bf7c-3e01-a7ab-f4c202ce06b1 | -9.22517 | -61.91179 | 2025-11-18 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0dd4ba7-60d2-34db-ac80-2fbb38e0c0af | -9.49124 | -63.50886 | 2025-11-18 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7260830-6a14-350c-8e1c-4a0ad34800a5 | -2.33732 | -55.80227 | 2025-11-18 06:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec42396c-b356-3f56-b01c-3c89f6e69a92 | -2.33824 | -55.79589 | 2025-11-18 06:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a2e7be3-e683-3e5c-92b1-74c222f97099 | -9.1257 | -61.77496 | 2025-11-18 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
