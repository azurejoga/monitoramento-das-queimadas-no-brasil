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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98a7e1ef-da3e-3bb9-a77e-065afe6d9ea0 | -13.60427 | -45.7757 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbce8ca1-bad4-311b-856a-1ac4aa5d3b53 | -11.33259 | -48.38202 | 2026-08-28 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d072253f-568e-37ce-af67-f7ce9a4c0235 | -14.41834 | -52.58994 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01fd1a7e-ec28-35fd-9e55-f8fbc3f7f027 | -14.30683 | -51.70901 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b20960a-b14c-3a5e-9e9f-01cbdd3e0d18 | -11.20782 | -51.24074 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| df8db40c-7048-3030-8fdb-6c360177681f | -11.59212 | -45.39505 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d8d2c47-c9f3-3904-878f-519fcd8191c0 | -12.0697 | -47.16214 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9470ce52-6574-3ae1-a6e9-e55692e3489c | -8.99581 | -52.38587 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 877f1337-31a1-3596-921a-314149be463c | -11.02433 | -49.66237 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8088a357-9456-3100-bd79-506147320ea0 | -14.41498 | -52.58933 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bed8e5a9-445f-3b4e-aac4-5cd128d9c6d9 | -9.65299 | -48.30597 | 2026-08-28 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e857846-7e0b-3862-b92b-e1d649361848 | -15.02411 | -48.15313 | 2026-08-28 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2124636b-f807-3b8f-8202-efa0c2f4aaec | -13.58315 | -45.77622 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a58c1bc-727f-3909-98d0-1cc4bdfc35c9 | -13.8352 | -54.04223 | 2026-08-28 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54a2755d-33c5-3cf0-a466-fb29e85d613b | -14.21614 | -45.30822 | 2026-08-28 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb445aeb-9b08-389f-9fb5-2f6f5fede09b | -6.97002 | -55.64586 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65834a76-053f-3acd-9db8-ba15693c895f | -14.32793 | -51.70523 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e301bef4-9b04-3a14-9b7b-debf1f40186b | -8.78781 | -50.07484 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0ff8acb-c2c3-389b-a775-8e0baa1f8d0f | -11.22408 | -54.00317 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1263268-7b09-3d86-ad6e-acb4c27bec6a | -11.8007 | -47.67341 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80488ad5-0aa9-3212-bd41-f7c81d1797e4 | -9.22603 | -51.54742 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ab198d-8e78-3f35-9c44-6a281d6dd998 | -9.43299 | -51.69608 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f367c921-7b23-33ad-838d-a133b7eade71 | -14.88447 | -52.60139 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 125db108-3ceb-3074-9023-7e3cf2ffb646 | -11.79648 | -47.67707 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eefe148e-620c-39aa-9d3e-ec5b99306659 | -13.59963 | -45.77886 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcae9e9a-a696-3f44-aee9-b94cc38cae93 | -11.27148 | -54.01156 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5667d6ae-f24f-3098-825c-dc7c11134148 | -8.80488 | -50.4968 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed8904e-7b4a-3bde-8f74-89c1e8bf191d | -8.94859 | -50.16896 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3891c6e-568c-36e9-9de8-ccca0ff2bf6f | -14.93844 | -52.59518 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c6bcf252-0943-316e-a009-1ee5bbd4fb5b | -6.76001 | -55.687 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ebe1320-9a3f-328c-881f-cc3e188f333e | -10.77439 | -54.02944 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c14a097d-183f-3b0a-a095-3d7c3da904d4 | -12.50642 | -43.81165 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed028e0d-0575-3ab5-8fb5-0d7f33602a08 | -8.00936 | -48.40572 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d0690f-4a25-338f-9596-0f70695cc30d | -13.42111 | -51.79225 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21575a3e-f8ae-3537-bb0b-d9a4adcc70aa | -6.77806 | -55.6855 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01c184d6-7d4e-3d7e-bf70-39b9061d2a93 | -9.66393 | -55.08163 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5af11295-6d95-389b-bb5e-d496d467ea85 | -10.78722 | -54.0068 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54351996-ab63-38c5-9ae3-e5d5f06f1abd | -11.23353 | -54.01379 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 968c7aa1-33b4-3ff7-b513-d56b2fed7a1c | -9.0144 | -40.99537 | 2026-08-28 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 42b4af88-8dbc-3fa6-9129-92411fcede3d | -14.93387 | -52.60199 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84df7750-4d68-3cf1-a918-5465921bf15b | -9.46682 | -51.70179 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5ec5ce8-84f1-3fe2-95d0-3781b24b0be8 | -11.24067 | -45.04488 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 848c36ef-fb31-39cf-8bb3-95a61a40ad8f | -11.01651 | -49.64648 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0b8f37d-afb3-3486-8c33-b2d1494d7a3e | -14.18966 | -52.83163 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 34c47ed4-a832-3e2d-bf32-3c2a93b76d40 | -11.21499 | -53.99486 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 674ce8fe-4f74-3e48-87df-d2f86227558d | -12.23728 | -50.57235 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d433d4b-fed9-3e60-bd38-75eaac80f8e9 | -13.41436 | -51.40747 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af0e75d7-f962-32e9-b4e6-b42d943fe9f7 | -11.21679 | -54.0019 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbbe1f94-ee86-3fd5-9dde-5e1dd47c5b7d | -8.09347 | -51.68044 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96b9c68-99ad-3d38-a305-7236103b961b | -14.17056 | -52.82074 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc221f45-6275-375c-a319-e971d27512d6 | -10.55598 | -50.48826 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f41a6c6f-9414-3273-b41a-71548257f7dd | -11.47751 | -46.95133 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2d46676-eaf6-3b6f-bbdb-d1cdda72e916 | -9.4515 | -51.71039 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b16ba3-c5c4-39b8-9a1d-57a6643f7985 | -11.27221 | -54.0294 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e9335ab-c262-30df-afc1-03922ac11c0c | -10.96385 | -50.302 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 505d7234-0f7e-3988-9df6-2bf76927f97a | -11.22773 | -54.00383 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b22b3e88-bd13-369f-af09-47295a5d4325 | -10.89202 | -46.63551 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13c8f78e-27a8-3e7d-811e-1d39bdf24e85 | -8.59571 | -54.79397 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cb940c4-c241-33de-b4bb-83c87659b027 | -14.93267 | -52.60932 | 2026-08-28 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb53a358-9064-39cf-8854-92f19631aa26 | -10.89646 | -46.63147 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852d3725-8af4-33e7-903e-9d53ecf93006 | -10.77038 | -54.03979 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08e07e13-1ed9-36d6-acca-c9e54fdb2a86 | -9.21691 | -51.56101 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 267973b6-aca3-3f9b-b17b-53755be2df2b | -8.59259 | -54.78829 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 162f9be8-f250-3640-bc4e-d73c975532e7 | -7.70448 | -55.37114 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a92b03-c9c7-380d-bfd5-248a62d53dae | -7.35516 | -55.16681 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0f13d67e-1315-3e66-a4c2-bcc7023634f5 | -9.88535 | -60.26695 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1b0cf68-bcfd-3ca1-872d-c3bbf2762156 | -8.59475 | -54.79051 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c555f43-91c7-308e-bc2b-23cfa91eb87d | -9.22439 | -51.53614 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38affc71-fb28-3746-8693-5d3e9e059d46 | -9.23218 | -51.55228 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d050cdeb-634e-37a1-b345-c87bad1c9234 | -12.2406 | -50.57289 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 557cb3e3-8a3e-3c71-ac4f-2be8979baddf | -10.00854 | -46.41698 | 2026-08-28 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a44a1d7c-d021-33ef-a8ad-2ae1fb2ba555 | -9.2373 | -51.54206 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cb74566-b0a9-3c48-82ae-0960758be84a | -11.7502 | -54.51773 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fee79324-4f5e-38cf-8951-f07c5bad4955 | -12.28994 | -50.6063 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d510ec7f-d073-3f28-ae31-994069b1d58d | -11.66874 | -50.46992 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c6778b-f0ba-33e3-bbf0-ea1684ed0908 | -8.58732 | -54.76303 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f18f728-e362-3da6-9687-00003f1e1787 | -10.99047 | -51.09608 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aba05f95-59d0-3985-b4a0-245a228e7144 | -14.15455 | -52.83325 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3c9607e-13de-37a5-8ad0-ad671ba0f733 | -11.29119 | -54.02827 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b112c722-aa4d-37be-81f5-cd82b12bc33d | -10.79359 | -54.00581 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ceae0d-87a2-30e9-825b-66dbd9485780 | -8.11131 | -51.65685 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8083633c-97af-3fba-861e-c2ff53118f62 | -10.84902 | -50.51786 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a21e0d9-ca11-3ea1-b0e1-938711747c18 | -11.57477 | -45.52155 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1648f1b-ba55-3513-855e-5de0d6364b79 | -11.21571 | -53.99057 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c679f8-b6d4-38bb-a3c1-2008d2f260be | -12.28717 | -50.60223 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8953d449-f98f-3206-b598-80d7033a51ef | -9.0605 | -45.78592 | 2026-08-28 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dae0507a-8dc2-3adc-ab40-b6f8a19b83b0 | -8.59077 | -54.78991 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bfdb21d7-8bd1-3b60-a8c0-aa4d5e3b1b9d | -8.67265 | -49.54128 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 994f07a3-e544-3c21-8dfb-d1e8699c4bb8 | -13.40772 | -51.40637 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1e01d5f2-40c7-333b-aed9-a803b937bad9 | -9.43604 | -51.58883 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 737c4c08-bf02-32d6-9602-b14ef341c693 | -10.32244 | -49.97633 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a25345c1-cce9-3488-9668-d5895ce80b16 | -11.73223 | -54.53313 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4ec2473-fd32-3cab-b1c4-760bd5c816f2 | -9.28374 | -57.07785 | 2026-08-28 04:51:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e10eadfb-6503-31ff-9473-c600be04b2e8 | -8.80156 | -50.49626 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da92f6f2-7809-3c79-9d43-63d1bcb18217 | -11.16401 | -51.21536 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 661e1619-e10b-3946-ab5f-e659d406d436 | -13.43176 | -53.99269 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3420715-51d6-3e0a-ba76-9477fdf65447 | -13.58727 | -45.77687 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b9a526-9ec9-31ed-b7ca-96c8568a64cb | -12.18178 | -50.58548 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf955aac-58b6-3697-b2e6-d3caa614d3d8 | -9.86235 | -60.26643 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2792797-b5fc-3ae6-b4a1-2d48f2843dd5 | -8.53403 | -55.28212 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
