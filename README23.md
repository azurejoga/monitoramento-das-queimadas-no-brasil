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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3060bbdd-0419-33fa-a8ac-d91162b1f1a3 | -11.83093 | -51.13624 | 2025-07-19 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b8d7426-208c-3eb8-9eec-a9c651e39ff9 | -10.62629 | -44.76911 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bcc6261d-2091-379f-bf5a-6647d295a7df | -9.81278 | -47.74329 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ab08c579-b612-33e9-90e7-aef94543f057 | -11.35667 | -48.72868 | 2025-07-19 04:36:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdbf3a66-a1d3-3023-aa9e-d3bb001a3ff3 | -11.96387 | -47.02087 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d36f162b-0727-3631-9e00-1c6a0b887397 | -15.89266 | -43.45998 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bdd12fcf-b8f6-3f34-9534-f4a4c08a5642 | -10.29501 | -60.54605 | 2025-07-19 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9211b77e-dd5f-33f3-b82c-4601dfb9a41f | -10.85706 | -47.17088 | 2025-07-19 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e92c7478-78df-32f6-a776-2f1b2783b923 | -10.87803 | -47.14767 | 2025-07-19 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd42adb8-5e06-3cd4-97fd-57c2f26ff194 | -12.57766 | -56.97255 | 2025-07-19 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52415668-a812-3563-a3ae-539283875825 | -11.56111 | -47.08182 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74cb2897-fccf-3551-a06a-ec45a7e93b8d | -11.96444 | -47.01705 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 644b4d4b-45c2-3518-bf58-e4c0eb34c1d4 | -11.96453 | -45.46827 | 2025-07-19 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 985fb3df-02a9-36ea-a9e0-2f437bdee330 | -10.08979 | -47.23799 | 2025-07-19 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c4495c-c8b4-318b-89c8-8cc7ad904773 | -10.63456 | -45.23592 | 2025-07-19 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31dbd7d3-268f-3a9e-9cd1-0638ef2f8417 | -22.83412 | -46.84285 | 2025-07-19 04:38:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8dd68ce1-2c8e-3469-8d64-b31bbea7fb91 | -22.70391 | -47.2147 | 2025-07-19 04:38:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba57e2f7-092d-3fb5-aca6-b752bbdf3bc1 | -16.77373 | -49.37971 | 2025-07-19 04:38:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91c11bf7-26ce-3aff-9608-b8f3d111bfc1 | -15.99593 | -49.81908 | 2025-07-19 04:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54981841-19ac-3637-a260-7de46caa9254 | -13.66562 | -59.83835 | 2025-07-19 04:38:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f6bfc7f-b9bb-33c7-8e95-4069679e998a | -20.20423 | -56.61211 | 2025-07-19 04:38:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 57dd46d9-c97b-37e4-a9c7-e9fac94dab28 | -20.4768 | -53.6745 | 2025-07-19 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8767c51c-2253-3b2b-8e59-326303ae02b0 | -22.5057 | -47.11842 | 2025-07-19 04:38:00 | NPP-375D | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d22aab7f-ba7a-3d2d-853f-23566b59bea5 | -16.89673 | -52.67645 | 2025-07-19 04:38:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94420ae5-37a5-3ef9-98ee-6a554fec8610 | -21.75361 | -52.44278 | 2025-07-19 04:38:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c98ce529-e2b5-383e-a344-24a16b553f14 | -18.8371 | -47.68136 | 2025-07-19 04:38:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 047f7d66-39d7-33ca-bd55-e203177e0480 | -16.27018 | -46.28931 | 2025-07-19 04:38:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b62c83f8-fd86-37f6-868e-80a3a0540a91 | -18.46366 | -52.15983 | 2025-07-19 04:38:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f54bc1e1-5fd9-35a6-96e4-fa16f541cb10 | -23.48426 | -45.37212 | 2025-07-19 04:38:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02f6c799-b1eb-34af-bab3-cb2f49dfc493 | -14.18231 | -58.19933 | 2025-07-19 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a149d70e-6f11-3082-a2af-fe2851b2cf45 | -21.49932 | -57.06429 | 2025-07-19 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dda0491-be23-366a-aeb2-e9c8f05210e6 | -16.4458 | -49.9678 | 2025-07-19 04:38:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9acf82ba-1eed-37dc-85b1-ccb4b1dff395 | -20.75064 | -49.33044 | 2025-07-19 04:38:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d7d2f04-21fc-3d3f-9b50-8564e7a65658 | -16.37668 | -43.03893 | 2025-07-19 04:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0597f52b-7941-3340-b270-38de8b6f6111 | -22.05628 | -48.16013 | 2025-07-19 04:38:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95914451-e4a9-3680-ab0c-a1b28638f3ca | -19.50813 | -43.88132 | 2025-07-19 04:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5569e6-37f4-30d0-87f4-47a21cc1a044 | -22.98094 | -49.17596 | 2025-07-19 04:38:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a716333-93ab-3d20-844c-9f106a6641f0 | -18.20848 | -54.4616 | 2025-07-19 04:38:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 995ea2d4-3223-3693-a2f6-d43af94a18b3 | -18.42239 | -49.74159 | 2025-07-19 04:38:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227f3ff0-3ea3-3b61-a0e5-1c33b09ac911 | -17.65578 | -44.20984 | 2025-07-19 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edcd5755-0bdc-31c4-8a2f-df5ec69e0769 | -17.6533 | -44.45925 | 2025-07-19 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba186f3c-5467-328d-b209-c70791253899 | -18.05106 | -47.94636 | 2025-07-19 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc95dbd4-2767-3754-b753-99eb58671037 | -22.50504 | -47.12354 | 2025-07-19 04:38:00 | NPP-375D | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc211c19-8d9b-3163-9dec-81c773e727cc | -15.85724 | -48.01225 | 2025-07-19 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8975a157-deba-3826-9967-b196d08c2a94 | -21.86599 | -56.74008 | 2025-07-19 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9490cf0-c7f3-3173-a57d-7875385c94d9 | -16.90022 | -52.67705 | 2025-07-19 04:38:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54fd50c5-e17e-3bb3-be7d-a006334bb33e | -22.98775 | -48.64434 | 2025-07-19 04:38:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bac4c03b-ce13-34f3-bc6b-5d1ee6a3136b | -15.99537 | -49.82267 | 2025-07-19 04:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a867831-e871-35ea-840b-c6b7cd35cf1f | -22.83808 | -46.84317 | 2025-07-19 04:38:00 | NPP-375D | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| de01708c-e3b6-31b0-bfcf-1ba513d8b179 | -21.04039 | -55.98473 | 2025-07-19 04:38:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b6e50ee-d72c-3aa5-8a75-a36221e0b35c | -17.55322 | -44.24593 | 2025-07-19 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75b747a8-ae49-38d3-9f48-4e9727390b9e | -20.59854 | -51.60971 | 2025-07-19 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dcb1a6ea-69f3-3eef-9ad4-0c2945ef1a28 | -22.00362 | -51.56059 | 2025-07-19 04:38:00 | NPP-375D | PRESIDENTE BERNARDES | SÃO PAULO | Brasil | 3541208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b38412d4-c523-346d-a829-a1ade4a8b9f4 | -15.70032 | -48.12982 | 2025-07-19 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49cfad71-bd28-3274-ad9d-2d774625b1ff | -21.75026 | -52.44215 | 2025-07-19 04:38:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2f1a7cf-1bd7-3edc-9f15-87ea041460f5 | -21.77762 | -44.33433 | 2025-07-19 04:38:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7bcb688c-06e8-3fe8-a10f-bf56b34c86bc | -22.98384 | -49.18078 | 2025-07-19 04:38:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49a4c278-2bf5-3134-91fe-44e0723bc62d | -18.26927 | -51.2098 | 2025-07-19 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5baf6cfd-96c9-37b7-b527-722b8116d2ad | -18.05457 | -47.94692 | 2025-07-19 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1c4b658-2166-330f-9b81-a62a2da67274 | -14.1767 | -58.20127 | 2025-07-19 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86ef5135-96ca-35fe-92d5-fe2c7f184a3d | -22.98444 | -49.17657 | 2025-07-19 04:38:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a2d9e97-a78e-3bf6-beab-8bacefaf5c72 | -14.17167 | -58.20025 | 2025-07-19 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45cc76b2-fa31-3dd0-b288-b7ce5b98aaf4 | -16.22088 | -48.70333 | 2025-07-19 04:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95916da7-b5bc-305f-a327-cd1f5a05b82b | -21.04427 | -55.98555 | 2025-07-19 04:38:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38981044-bc2e-3295-8ab5-7c07683fa163 | -18.83798 | -47.68391 | 2025-07-19 04:38:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20faa6c4-6cc2-3075-9989-7df5e9a00b37 | -16.72441 | -49.21808 | 2025-07-19 04:38:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5204e490-4680-371d-a860-ff56ac401d7b | -22.98034 | -49.18018 | 2025-07-19 04:38:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33929cab-1fef-3dd9-bb45-fb4dd90a17b5 | -19.2757 | -49.38482 | 2025-07-19 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1bb86b-88c9-3229-95f5-118a87eb8b18 | -22.75759 | -44.76894 | 2025-07-19 04:38:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28fbefda-0151-31d0-9cd9-8f377fc07ae5 | -22.83345 | -46.84823 | 2025-07-19 04:38:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6987e718-4345-3ae6-ab19-360846859b67 | -20.80236 | -49.32964 | 2025-07-19 04:38:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0c76ac7e-9f2a-393a-b426-63512f503e00 | -19.50698 | -43.89088 | 2025-07-19 04:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9139eef-bf04-3d97-a442-0d3a83b03d23 | -17.65033 | -44.45615 | 2025-07-19 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a919941-e419-3688-abc7-c6cd12fe6481 | -18.657 | -55.72686 | 2025-07-19 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 29cb0ca6-6090-3457-a195-2b82b81c4e65 | -19.50756 | -43.88609 | 2025-07-19 04:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 425482f9-e3ed-307b-b099-c33409761366 | -19.51208 | -43.88681 | 2025-07-19 04:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afe056c3-a319-3329-af51-2d2fe5843650 | -17.65144 | -44.2094 | 2025-07-19 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe6569af-52f2-3cc0-95db-1fe617ae2afe | -19.4776 | -49.29225 | 2025-07-19 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c769a54-4904-3086-bf2f-d70699550faa | -18.65899 | -55.71614 | 2025-07-19 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5f686015-aa9d-3970-8105-de7cc0267cd5 | -17.65382 | -44.45503 | 2025-07-19 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c1159ea-e6bc-3877-a95b-e39b70370b04 | -15.99261 | -49.81853 | 2025-07-19 04:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a606333-fca1-3b8b-b008-0d599f9c8bb5 | -21.50339 | -57.06526 | 2025-07-19 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c9387cd-d178-32a3-b3c9-a13b47d2972b | -22.7032 | -47.25062 | 2025-07-19 04:38:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 377f4382-3004-3207-b285-b588843ad674 | -18.41904 | -49.74103 | 2025-07-19 04:38:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6e7dff3-f1fd-3fea-af52-09cf5c75aff4 | -11.7317 | -48.1849 | 2025-07-19 04:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 68caab24-206b-3111-8923-9050d4db33e1 | -11.7313 | -48.207 | 2025-07-19 04:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a66de006-869c-3805-a2d6-1bcbe9317415 | -2.9109 | -48.2325 | 2025-07-19 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 65244890-e033-3687-9c69-ba642d8cfad8 | -2.9108 | -48.254 | 2025-07-19 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4fe51314-9d77-3f55-8012-5d89ef8da1b0 | -5.6567 | -43.7161 | 2025-07-19 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 836925a5-dd3f-3184-bfa1-c590da91b248 | -23.32343 | -50.13492 | 2025-07-19 04:40:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6df67b45-b0b0-3953-bbd9-9ec9436c183b | -23.76399 | -49.63459 | 2025-07-19 04:40:00 | NPP-375D | SANTANA DO ITARARÉ | PARANÁ | Brasil | 4124004 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95ac54f9-828d-3c08-948b-f2c8f2250486 | -23.32684 | -50.13551 | 2025-07-19 04:40:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a3701feb-c444-3d0d-b9f0-74c63a9fd1a3 | -27.68723 | -48.75108 | 2025-07-19 04:40:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fad9cc41-7ffa-37c8-bd49-9124a3d1df54 | -23.61014 | -49.01163 | 2025-07-19 04:40:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d1cf88-81a1-338c-8cae-3db3d9d0f327 | -25.10913 | -52.73316 | 2025-07-19 04:40:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f37a985b-b51e-3633-b626-c9095fae3623 | -23.60775 | -49.01335 | 2025-07-19 04:40:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7adadbc7-7810-3bdf-a7a1-c04a35c0ac19 | -24.11784 | -49.11045 | 2025-07-19 04:40:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 150790c1-2024-314d-ae78-46468ef4734e | -23.60659 | -49.01103 | 2025-07-19 04:40:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09cc3c14-e1af-302f-a4c8-2fb885d299f6 | -24.1143 | -49.10978 | 2025-07-19 04:40:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87801222-1cc7-311c-908c-40d9a97fedc7 | -23.60836 | -49.00907 | 2025-07-19 04:40:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
