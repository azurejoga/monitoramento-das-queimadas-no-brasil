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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d5a32fa-767b-3f0c-9896-353dbb8ccbe9 | -4.75102 | -50.59986 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| feab0421-52ce-3f36-a984-a723ace8735d | -5.98072 | -49.81259 | 2025-11-13 04:42:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9222b354-0afe-3c1c-a712-c960e96eb34c | -5.08317 | -47.92876 | 2025-11-13 04:42:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a96a22f-971c-3031-b274-3e0d94df7f05 | -3.24135 | -52.92055 | 2025-11-13 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff36bde6-6ca8-3008-84f1-4ed7ac0ebf6a | -5.6043 | -41.06825 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8172931-875d-348d-80e5-14dc539fcc24 | -3.09165 | -49.27418 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4ef958f-4e70-38fe-8de6-b99bfcace9f1 | -5.72347 | -43.52478 | 2025-11-13 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67481359-8a8c-3016-b945-77c1b5254fad | -4.04633 | -46.12389 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfe0331-d5e9-3812-b0f7-39855bfa3bee | -4.205 | -47.80859 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 060abd65-7de3-3e4c-aab6-d0fa72330675 | -6.35388 | -39.79351 | 2025-11-13 04:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb9ffdf9-1de9-38f9-95c4-39176b5eccff | -2.03677 | -47.04468 | 2025-11-13 04:42:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c050ee3f-9d25-3d16-b0f9-456bc7afa4b3 | -3.1801 | -48.71455 | 2025-11-13 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9a0aac9-1563-30bb-bb34-8f6b66d616ae | -2.8724 | -51.47777 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d97e5522-5ffc-3c85-9acb-301135e20e6b | -7.1489 | -41.70302 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd73e7fb-6426-34a7-9c5f-9428d3330fb3 | -6.2882 | -41.74464 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c646d5b3-f604-31c1-928f-46f868687eb7 | -7.77754 | -43.79657 | 2025-11-13 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07dcc650-712e-3691-a2e8-efdfe5330305 | -3.74424 | -52.24733 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f0a8159-3c2c-3a78-ae2a-3fe534d395b3 | -2.8244 | -52.87362 | 2025-11-13 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5686800c-8b86-396a-9d1c-c057b847ac10 | -7.78125 | -43.80131 | 2025-11-13 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 43c713ef-f2aa-3a7c-99f6-4908d234920b | -2.72683 | -47.40596 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cbe9863-46bd-31d1-9c99-0c9632348296 | -5.66715 | -46.52748 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79a44a45-7532-32f6-a73f-b3c933a793ce | -5.57434 | -47.10301 | 2025-11-13 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f9e780f-ac31-3244-93b7-39a6662a2a6d | -5.08262 | -47.93232 | 2025-11-13 04:42:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a3e7127-e3a2-35ee-821d-e2cca0b61e00 | -5.72289 | -43.52879 | 2025-11-13 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b2ddb00-54c5-30bb-93f5-e5bd461d353b | -3.34046 | -48.3861 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba07839d-54de-3ddd-b791-ea8306640dde | -3.1303 | -49.24116 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12598c9c-dfd4-31b2-942a-630d33bb8119 | -5.64957 | -41.07493 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b29ee65-12cd-335e-a40f-87a4970fc05a | -7.106 | -42.36446 | 2025-11-13 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5d609781-01c1-37d5-bf10-f33d55d000ca | -4.36414 | -46.1402 | 2025-11-13 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fbf6e7c-f290-3421-b8b3-68983709c6d7 | -4.75564 | -48.83138 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aa87c04-741f-3388-9911-01a82b09513b | -4.82728 | -50.62316 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2d4836-d1de-3820-854a-c1d2e684c114 | -5.84142 | -47.56314 | 2025-11-13 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 551ea7f4-e54a-3346-b834-b28b5356fbca | -2.45314 | -49.26226 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2819ae27-d65e-33c9-bf8f-467ffa41ecc5 | -6.95712 | -46.35237 | 2025-11-13 04:42:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84e03808-d4b0-3154-b6f4-359dee3ebbb6 | -5.66448 | -47.68978 | 2025-11-13 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aaa6b07-85a2-366a-838d-5078ee40e8a6 | -2.30253 | -48.33278 | 2025-11-13 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10c6326a-49b2-37b8-b9b3-37ee98ba2d69 | -4.00834 | -48.80546 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0fceee4-aaf3-3d58-a0eb-85c4c036dd07 | -3.53095 | -44.84844 | 2025-11-13 04:42:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b3cf9e-5cae-3f2b-9256-a9f86faba93b | -6.48618 | -48.37077 | 2025-11-13 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227154ac-f0fb-3e3e-a13d-58fd91e23742 | -4.71439 | -46.44413 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 090d0ca3-09f2-38c7-9155-1cca83f91bae | -2.55452 | -49.118 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27dd0975-7b5b-3613-b8f6-4bdc0e58971e | -3.09443 | -49.27817 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fefe9901-dec2-3d74-a0dd-79e67e9d6edc | -7.15227 | -41.70807 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 26f8c91b-3b02-3299-9de2-b9199de45023 | -3.12613 | -46.04042 | 2025-11-13 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9805b68-c901-305a-88ef-0133e8445015 | -5.66034 | -46.28574 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7397fb7-f1c8-3daa-aa0b-ba2366a64f5e | -2.87662 | -51.47431 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 481c9a8e-dc77-367d-a9a1-88d5f2a8fc30 | -7.47947 | -42.55105 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcb2a202-7461-3c9e-b3d4-868b089c927b | -5.72715 | -44.83405 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c476c173-d6be-334a-8ebf-5d839c36c7a9 | -4.52312 | -46.41964 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883bc024-f782-364f-82cb-905172c3f747 | -5.18997 | -47.73615 | 2025-11-13 04:42:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7278540-2a63-3418-8ffd-56ee0705df33 | -6.69126 | -47.79623 | 2025-11-13 04:42:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a962276-517f-3a7e-82f2-24dd7298a2d2 | -3.23003 | -45.58715 | 2025-11-13 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0c0bf86-acff-351e-9412-27ff43ca9ec6 | -3.10094 | -49.27567 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7d0672c-12aa-3891-a503-bcdd801ad3c3 | -4.24268 | -49.6727 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0b12fd4-cc3b-3518-9213-41cab4bfc781 | -3.20334 | -43.47519 | 2025-11-13 04:42:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50a27554-2d72-3412-9df0-6841e8ba9e1d | -4.69647 | -49.65155 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 977ad6a4-6da6-3e87-8bb6-4d8ffefd39d9 | -3.86242 | -49.79192 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b56538c7-0d33-3f78-a417-4e66df12b764 | -2.52407 | -47.8104 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aeff68b-cfd4-3a58-b3a2-24b16113c133 | -7.82156 | -41.76609 | 2025-11-13 04:42:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d3e364af-ada3-38dc-b8f2-4505834304cd | -3.13916 | -50.27752 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41560ff9-1707-3253-8687-6b43a2f9b61a | -2.39906 | -49.39323 | 2025-11-13 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b85e528-74aa-3e3f-a7ac-83fc6d4658cf | -4.71148 | -46.43964 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 718d0904-5718-3924-9997-b97c59f1f05b | -1.6436 | -53.22461 | 2025-11-13 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc451372-3966-306f-9490-95a11dda1b8e | -7.4748 | -42.55038 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8ef1a0d-676f-3daf-98b3-910c7db4a212 | -3.37014 | -48.40825 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf1a4dbc-10f9-3c8b-9734-211e04d3575c | -3.89935 | -52.11806 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1a49458-5adb-387b-9ac8-b75c2564b65c | -7.15387 | -41.7034 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 97612928-f40e-3c87-bc7b-6d59fc3b869c | -3.34433 | -48.38317 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5ac64ef-5f17-396a-80b3-e227ac11fd6d | -3.89503 | -52.12167 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3217d024-1b42-3e97-a8f0-9679b2b32450 | -7.45624 | -42.5667 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56de8d67-7b66-37c9-86d4-1be2c1810db3 | -3.70239 | -49.02631 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c088bf-cd99-3c57-880a-c197f34fe489 | -2.55301 | -51.24663 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69a1d02b-db74-33d4-9ca2-ccd642676f4f | -2.86884 | -51.47721 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d78e160-3ebb-3d8c-a3c8-a92243fd6dc0 | -7.90378 | -43.17387 | 2025-11-13 04:42:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9999a376-bb54-3df4-af55-5a85c51d4d45 | -5.57779 | -47.1036 | 2025-11-13 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066779dd-30ec-3ade-9d66-b2f37bbcb8f6 | -5.08654 | -47.92929 | 2025-11-13 04:42:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 761d4987-2a92-306d-b62f-c714125319b9 | -2.15444 | -52.76235 | 2025-11-13 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bf8d1ce-dd78-32e2-a2b0-396a93b46554 | -2.79931 | -48.94064 | 2025-11-13 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e651a04c-316f-395c-8c9c-8d30632281d9 | -5.75448 | -46.15878 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5b7b5da7-423e-32da-86a9-97e30b127d51 | -3.84265 | -50.05707 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e58a95eb-2980-3f79-9ce1-350848bfd2e7 | -2.52796 | -47.80743 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b9d279-7633-359f-992a-bd5146bd4694 | -7.48415 | -42.55172 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa70e479-d273-379d-b753-e70b22ea44fd | -4.4413 | -50.15116 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f0abd0b-ab7c-3f1c-901d-2a283675b09f | -5.64946 | -41.07134 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0806b43-de59-3c2f-b834-114a8eb5c0e2 | -3.09872 | -49.2682 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70417b1-49ee-3724-a308-4aa0c4aefe5e | -4.89324 | -48.96607 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bafd412-f0db-389f-9965-bcdf156f0a18 | -4.56104 | -45.77701 | 2025-11-13 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e1a3eb-f226-311f-8331-83a170d3a0af | -5.02139 | -46.83815 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55ea7fa3-24eb-3275-8ef9-93e88720520a | -4.84392 | -42.37366 | 2025-11-13 04:42:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fac9955a-ea51-3a78-8ea8-adce2abf8e54 | -3.34683 | -48.38335 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f72ee4a2-74a4-3b98-838b-8eec4472a3e3 | -2.72712 | -49.58109 | 2025-11-13 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1406918-d492-3edc-944d-709dd4b4c67f | -7.5134 | -46.93323 | 2025-11-13 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c204840f-ff9a-322f-be8a-ccb922d17a1f | -2.15788 | -47.5601 | 2025-11-13 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f793eeb6-08a5-375d-a6b8-006349d72adb | -2.02102 | -47.32627 | 2025-11-13 04:42:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeb61d01-1b5f-34b4-aea5-f950a51dc5ba | -3.34574 | -48.39027 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95863a31-a0b7-3201-8d5e-a2ed815937b5 | -2.17114 | -48.37245 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fa65535-dec0-38b6-89f0-815b898f9488 | -4.30972 | -48.24584 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce52020-79c6-3e25-8281-fbb711ed5b3e | -4.24064 | -48.38134 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4dfa42e-b06f-3653-94d0-3ec20532c231 | -2.90016 | -48.06505 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 986f94d4-58c2-329f-b56b-a97ada9ac2aa | -4.18816 | -50.3377 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
