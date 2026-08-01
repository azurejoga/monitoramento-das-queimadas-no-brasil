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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b151cc6-ddd9-3434-b51b-783d242f1d49 | -13.95738 | -49.14858 | 2026-08-01 05:18:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a47fef36-6b45-3b15-8dba-1f51e8f134e7 | -14.06654 | -46.2874 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 996c9104-66f0-309b-86bc-8548b0fd9acc | -15.82885 | -48.18658 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f2d5bea1-d81d-3ab1-848a-7d5cd25f1bb9 | -16.39589 | -53.34703 | 2026-08-01 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31695496-154d-3958-92c0-cb086f6fbfab | -17.46481 | -51.72891 | 2026-08-01 05:18:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 803e677c-7db4-385d-a60a-7c49489cca48 | -14.08062 | -46.28327 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bcfc70b-298d-3a57-a548-05bc00dfa519 | -14.07541 | -46.29234 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eff2e9f8-e0d8-3845-afd1-25bb38a8de75 | -14.08214 | -46.29311 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 798091f7-fb55-3219-9eb0-a7f7abb3af14 | -14.34179 | -48.03099 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85737f02-4456-3ba8-86ac-39f6349fedcf | -14.33581 | -48.0293 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d440ba7a-e7d4-32c3-ae9c-514015463c94 | -13.06188 | -52.72012 | 2026-08-01 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b657d806-df91-336f-b2f4-f20944bc2a12 | -14.89368 | -47.22783 | 2026-08-01 05:18:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21d3d716-2dce-39bf-833f-e555341ba793 | -14.07971 | -46.24939 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da8271a6-77cc-3adb-879e-eed4a01a63e2 | -12.2509 | -59.31666 | 2026-08-01 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 559e8bf0-4a51-356c-addf-0a625701deeb | -14.34125 | -48.02856 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b920d7e1-7b8e-39e3-b345-ec106f6fbe62 | -12.80916 | -47.17507 | 2026-08-01 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7936f324-5f84-3a72-a3fa-d2ff3c478b50 | -13.06569 | -52.72497 | 2026-08-01 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 805a7511-f1cd-32e6-8147-0f3dbca2ce65 | -14.0698 | -46.25671 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c416d58b-530f-316e-a847-b234ecabf4fb | -12.80975 | -47.16999 | 2026-08-01 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a02d1884-a6be-3859-93a5-29f4fcdbac4e | -14.0793 | -46.2956 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 742342fb-a4ab-3bff-9387-8d0a464170c4 | -14.34068 | -48.03356 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddbb1318-e84c-33f0-a271-71e76a7e7792 | -13.95346 | -47.82805 | 2026-08-01 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30d20b97-bab9-3e92-a996-837a24ee6c55 | -11.44603 | -61.17702 | 2026-08-01 05:18:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ff8853-ac05-3daa-b46f-9bf5380c3b53 | -13.06131 | -52.72439 | 2026-08-01 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72508abf-40e2-3ceb-8373-1878d1d6b33b | -14.07654 | -46.25758 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4a5504f7-d11d-340c-8521-b12a3edbc59e | -14.34063 | -48.04177 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d5991ab-1fc3-34d2-9c2e-5dc29b5af002 | -14.08464 | -46.26833 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8b77a10e-def3-3e94-8629-35b168a80bf4 | -14.07258 | -46.29467 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c25afa07-de94-3944-81f2-fe446dbf64f7 | -13.16697 | -53.25315 | 2026-08-01 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dcd59c4-707a-3c80-8590-1ecd2feaca3e | -14.07525 | -46.26966 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f72707d6-af62-3ae0-9154-62e192fac1f6 | -14.07591 | -46.26351 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 39c0e6f7-0b44-3e44-984c-0aea168cf812 | -14.07717 | -46.25167 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f97e432e-7906-3a15-958b-38997e1ed79f | -14.08752 | -46.2397 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26b4d7de-ce71-3f01-8858-8b02f0d5a0bd | -14.0725 | -46.2899 | 2026-08-01 05:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b9863345-c8eb-358d-95d3-d5175976b8a8 | -14.0925 | -46.2637 | 2026-08-01 05:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 39f31cab-b5aa-3f11-a79e-1db42f1bbd69 | -14.073 | -46.2669 | 2026-08-01 05:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d178d26b-72f9-31a5-a79c-affdd28cd1fe | -11.2591 | -54.8517 | 2026-08-01 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| dbbae8b6-1c82-33ab-98d0-609e9abe68a2 | -21.98545 | -57.59986 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fd44f21-3349-32d5-a6f1-6200595abe0b | -20.38566 | -58.02361 | 2026-08-01 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 744211f5-b0cc-3203-a025-c8c7ca15eb0a | -18.49418 | -51.61153 | 2026-08-01 05:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54525f47-84b9-38fb-a309-0e7920eed04c | -20.60741 | -57.30381 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49fb7fbb-a280-3096-89e3-6f6d119e03ee | -20.56167 | -57.31241 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fe77757-2c09-3af9-9aaf-5b9c239a94bb | -21.03923 | -55.82874 | 2026-08-01 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 052aa89b-94b5-3ec6-947e-1a68ebca518d | -18.48353 | -51.70415 | 2026-08-01 05:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12be9813-51a6-32d3-9579-44e8d682859f | -20.5623 | -57.30787 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1841313-d381-33d1-8292-728d9fe6dc0d | -20.56042 | -57.32143 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24035657-51a0-3f9f-8300-bd8d3cd820ce | -21.29412 | -56.14096 | 2026-08-01 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39c946e5-8658-3eb4-b520-a26fe5530b57 | -20.11208 | -50.74422 | 2026-08-01 05:21:00 | NOAA-20 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 852096e0-d749-3d7a-8b3c-b9d97c561dfb | -21.66875 | -56.33083 | 2026-08-01 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4b5577b-26a8-326c-99d4-f8f070da0099 | -21.24024 | -49.16105 | 2026-08-01 05:21:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 19705475-0f44-3d60-a4cf-a579821bdba9 | -20.54588 | -57.29148 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3889425-b266-35fb-a8ac-1136ed7558dc | -18.48424 | -51.69802 | 2026-08-01 05:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ceb2443a-82ec-3c0b-9368-6cce6ea799cf | -21.66551 | -56.32511 | 2026-08-01 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59b8ba08-1642-393a-961a-e783253d9534 | -20.56491 | -57.26202 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae10c66f-1059-302b-ac52-b46e7d5d4481 | -21.25958 | -49.15244 | 2026-08-01 05:21:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9acb489d-ce6d-32e4-905f-72c4b51c062c | -18.48388 | -51.7011 | 2026-08-01 05:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 234fca0b-ae71-309c-aa44-919c8cb14f0c | -20.60679 | -57.30835 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17e92dcc-bf2a-31ac-892a-56b63a7c97d3 | -23.02962 | -52.65933 | 2026-08-01 05:21:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 087acf21-878e-3660-a8c4-354d3dbeb4b8 | -21.98483 | -57.60445 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8227adf-b692-32fc-b528-44a7081cc9cb | -20.60864 | -57.29474 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2f0ea8a-f935-3a0f-b4d3-59b54fc365f7 | -20.6123 | -57.29531 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6ba49aa-cd32-35c5-8ee8-8f9c957a98a7 | -20.38506 | -58.00202 | 2026-08-01 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 70017f73-426f-3334-b6c0-c45624158f48 | -21.66482 | -56.33035 | 2026-08-01 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba100c11-422d-37e3-946a-3d3262f73e90 | -20.56105 | -57.31693 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bcb29ac-aee7-32ff-b5ce-6cbea069e4cc | -18.49346 | -51.61784 | 2026-08-01 05:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e91df29d-63b8-3ed1-b682-fdd4eab8142e | -21.66943 | -56.3256 | 2026-08-01 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 488cead0-5093-3387-a626-a4861e06eb14 | -23.78847 | -49.29506 | 2026-08-01 05:21:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ccdb207d-128e-3885-93ea-5e9d3fa0329e | -20.70274 | -54.59123 | 2026-08-01 05:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da4fe7d3-c7bc-319b-a95d-e5c8d8c0b633 | -20.60375 | -57.30322 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75282cf9-1043-3c8d-94ef-33e98aa13cb8 | -23.02993 | -52.65629 | 2026-08-01 05:21:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 32ea9de0-2a05-32a3-b30f-258776d6871b | -20.3852 | -58.00361 | 2026-08-01 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a32dc891-316f-36f6-8ee3-9a76cfae9320 | -21.23982 | -49.16579 | 2026-08-01 05:21:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d1190265-2c59-37f8-ab01-e2096171e1ef | -20.60436 | -57.2987 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c9f4e84-5939-3bfe-a109-e78461d08365 | -23.02457 | -52.65888 | 2026-08-01 05:21:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3bcfbbef-0f68-378f-a84b-679921be40a3 | -21.26573 | -49.15296 | 2026-08-01 05:21:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 395b0df5-bf9c-33e7-aa97-227e30864cd4 | -20.55516 | -57.25125 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2379e85a-0820-3a77-b341-2a053acf7d1b | -20.52043 | -57.17569 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b128e131-eb97-30a5-be06-4c02d00212af | -20.1117 | -50.74798 | 2026-08-01 05:21:00 | NOAA-20 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8800dc3e-5697-31f4-897c-7c57141a4c0d | -20.5465 | -57.28697 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4dabc0c-3afe-370e-9323-9e6e822e2d1a | -20.5472 | -57.25468 | 2026-08-01 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6feb565-515c-3fe5-a682-89724aba4130 | -20.37976 | -58.01408 | 2026-08-01 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d1e97f88-cac0-311d-b277-6c7571085a87 | -28.59031 | -50.23533 | 2026-08-01 05:23:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90da36c7-6c0d-3afc-b513-7f2cbc21482d | -14.0925 | -46.2637 | 2026-08-01 05:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 22756b0a-78c3-3324-b226-3cfba907d21d | -14.073 | -46.2669 | 2026-08-01 05:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 67931c18-7fca-3f57-bda4-bf1312274435 | -11.2402 | -54.8534 | 2026-08-01 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5a23a0fd-3b59-3da0-a7aa-9ce47f216a74 | -14.0725 | -46.2899 | 2026-08-01 05:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 169ac883-ce45-33db-add2-1e8d1a72bcbc | -14.0725 | -46.2899 | 2026-08-01 05:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 32f0a4c2-60bf-3f07-8541-1e63007869e0 | -14.073 | -46.2669 | 2026-08-01 05:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 52af55c3-4175-3c57-9af0-30cbe4fba1b8 | -14.0735 | -46.2439 | 2026-08-01 05:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| dd3e0323-1619-3d1a-930c-52bce99ac29e | -4.2597 | -38.03985 | 2026-08-01 05:48:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ed386fcf-503e-3e0f-b99b-783b40addde2 | -4.26158 | -38.02788 | 2026-08-01 05:48:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 736a5053-775b-3c64-9d24-f1fe2f2c9daa | -17.4239 | -42.6386 | 2026-08-01 05:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 00c121d4-b963-30b9-90c8-dff01abbbb57 | -14.0735 | -46.2439 | 2026-08-01 05:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ded4e0a1-d9e3-3b0e-9977-7985077f2cc4 | -14.073 | -46.2669 | 2026-08-01 05:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 7bf13137-a761-366d-bde6-aeb5bf781052 | -14.0725 | -46.2899 | 2026-08-01 05:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 6d338937-d554-3995-a0cb-d6558f438adc | -17.444 | -42.6337 | 2026-08-01 05:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 44b88804-049d-39ac-aa96-14da535a48dd | -17.4246 | -42.6137 | 2026-08-01 05:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d2809f2e-9bac-34b8-b68c-f7e351b52bc6 | -14.0925 | -46.2637 | 2026-08-01 05:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5e05dc24-6832-331c-af16-18432889c441 | -17.4447 | -42.6088 | 2026-08-01 05:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 468e2ff3-6f03-3979-909d-34710e08e3a1 | -14.07145 | -46.27913 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |


[Clique aqui para ver as próximas entradas](README25.md)
