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
| 12d8934f-5b85-3d67-b9b3-acd88c0a2216 | -12.73782 | -47.02044 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bb16d16-7387-3736-a3da-6d976f5ce06d | -13.00618 | -46.98265 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6916ca40-5bc4-3afa-84e1-9784cc6c9c0e | -9.04049 | -48.75757 | 2026-09-19 04:40:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f8a257c-1a9c-33d7-a028-26ec94856621 | -11.3181 | -47.27156 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 190f713f-78ea-35e2-9501-2a3e0f71cf1d | -14.78986 | -48.58089 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 732c3ec3-0ba6-3eb4-a085-49c679c98ce0 | -9.24392 | -45.93135 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d5dcf9a-acae-3deb-b0f8-608ce72f9b0f | -14.67787 | -46.67639 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e3ce79b-5ae2-3a7f-a3c7-e52c375d3286 | -7.57812 | -57.69778 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52b50df6-d65e-327a-9831-c49b8e2129cf | -12.142 | -47.02 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d504dfa-9b50-3459-9133-a1f6dec70422 | -12.99397 | -44.83541 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7e37ca0-57b0-3908-aa02-1df1750344d5 | -11.94386 | -50.10524 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf814cce-9ac0-30bd-9e1c-62d5fceef88b | -11.55329 | -46.89718 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fefaba3-f97a-3763-90e5-9d4517f80a1a | -9.6815 | -48.32191 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee3d616b-8cc6-3459-9ebe-a3de1f3c1757 | -12.13644 | -47.0118 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93e44ef7-4a2c-3a9e-b927-f56168acd284 | -10.90927 | -50.84789 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a65a78ec-08ea-32db-a984-1e7807bb216d | -9.76213 | -46.07502 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd2caf5-30ba-3ae5-aa18-730bced4b9ce | -14.67333 | -46.66037 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66af51c8-388e-3e9c-822d-a14607de4e85 | -9.89153 | -46.54169 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdc091ea-df6b-3ac3-953f-6bb8b5b1feb1 | -10.18048 | -48.51881 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74639d7b-5731-3ba7-b23b-79bb73b8d6e2 | -11.14447 | -54.01984 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 246ffd0d-47b7-3556-a2da-38c0fa05230b | -9.91129 | -46.58431 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f24bee7e-d5a7-3f78-be19-4860c6ecb982 | -10.45096 | -48.68322 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79589fb-7448-34c7-b6e9-c3494cd346c8 | -9.7835 | -45.06207 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dc0c8a6-2658-38c8-8fa4-b350b50c42a1 | -12.69491 | -45.94444 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df3ed52e-736e-3b1c-8e21-073edc86deb7 | -14.95116 | -49.9412 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10c8b162-6051-36e1-a7c6-2e9b58a48a05 | -10.71349 | -60.73556 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0c66fb3-eff1-353e-a0e8-41148547022f | -12.58405 | -49.09971 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85e9ee30-adf6-3d60-8b0e-7752d8d49daf | -11.40793 | -47.28613 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bebe429-2307-371f-80d5-630f6d8072bf | -13.00558 | -46.96438 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b4d799d-70d2-38eb-ad1e-a4751f5e2b04 | -11.4251 | -51.45234 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4915851b-530b-3421-81c1-900f99eb6943 | -13.2368 | -46.91187 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d6f27bb-1d43-324c-b95f-ceba1e31889b | -14.81662 | -48.56337 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 659ef4e9-8088-3afc-a780-049775b308ac | -12.12586 | -46.99184 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24e89047-6091-3260-bb14-653499f1e89e | -10.88133 | -54.06686 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d36b303-dbf1-37c7-a905-77e1e48008ba | -12.01897 | -55.55006 | 2026-09-19 04:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae77138-df4e-3eb4-8b43-d0d6b6ef72d4 | -21.02514 | -47.257 | 2026-09-19 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb08c32d-d065-376e-a976-6d13ba6de1b5 | -18.02006 | -51.07493 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8184ef1c-8bbc-32c3-9d8b-0eb962d78b38 | -16.83454 | -47.64042 | 2026-09-19 04:42:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39137ef1-d2e2-3625-ba66-7e9d83919460 | -18.02284 | -51.07951 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1060bd36-2d6a-3f11-b47d-d1437ce23773 | -18.92295 | -44.72829 | 2026-09-19 04:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c090350-932b-3349-bdc8-7b56d4f8e120 | -22.02935 | -49.54546 | 2026-09-19 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c7a5f765-edbf-38cc-8960-f0093a6d0250 | -16.30774 | -53.86314 | 2026-09-19 04:42:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59fdef69-c7cd-386d-a37f-651a4dfce8c8 | -18.01939 | -51.07887 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac9ecefa-305e-3b46-a068-f24d3f6ffb1b | -21.24927 | -54.19629 | 2026-09-19 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25fb5e65-0632-30c4-9a0e-3a8d267d45a8 | -18.4105 | -49.16792 | 2026-09-19 04:42:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f800a3c-5b86-3c4d-aac4-4efdf3d3aac9 | -16.79756 | -46.99026 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4047100-ac4f-36e7-85be-0c9833520b61 | -16.41595 | -48.97276 | 2026-09-19 04:42:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 166d5adb-5df7-34db-af67-6d37986b4168 | -18.6797 | -44.61441 | 2026-09-19 04:42:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d60bcc2-2b6c-392f-a7dd-f25cd75072b3 | -18.01805 | -51.0868 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02a4af3a-c019-3fc0-b4a4-77595bb597ad | -18.41108 | -49.16427 | 2026-09-19 04:42:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a8a878e6-bbf1-36f3-ad72-dce13ce0b6f0 | -16.88344 | -50.57856 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 97031918-35ef-358e-a7dd-8ce5f0bb47be | -16.80496 | -46.98755 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d11a61e7-f8c2-306b-ac9b-84fae11c051c | -17.03377 | -47.29464 | 2026-09-19 04:42:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c73de33f-648e-3268-b9a0-178c42da1e1e | -16.88752 | -50.57531 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 511a90ec-12c6-388a-ba9b-5897bdec753f | -21.23818 | -50.85898 | 2026-09-19 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 29f790a6-bf4f-3e4e-93ac-51e1eb7427eb | -19.81702 | -46.46529 | 2026-09-19 04:42:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d09da0f-75e1-345b-b24e-34c2de112f0c | -22.02601 | -49.54486 | 2026-09-19 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4512e163-833c-3903-b3be-2c28a756c38a | -18.87221 | -49.51353 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61a01915-60c3-3cd1-af85-5c56e121cdf5 | -18.82154 | -48.25158 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 894d12b0-814c-3fca-b9a2-3ff50c721ef0 | -19.19167 | -46.66927 | 2026-09-19 04:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f77444c-ffde-3eab-a9aa-7420a6f516d3 | -18.01383 | -51.06974 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| febb861f-5762-3ef4-b62f-4c6706ce317d | -18.40833 | -49.16005 | 2026-09-19 04:42:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7b2fdb3-8824-33f7-ad85-eec4e5dac5a4 | -18.01872 | -51.08283 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4194ab27-2bf1-3250-96b2-0204fa8a107e | -16.88409 | -50.57471 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9ad1f500-f735-3a79-8d8f-48b598574bbb | -18.01727 | -51.07038 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6acd5ad-3da3-30c7-98c3-179d1a49c447 | -22.03152 | -49.55353 | 2026-09-19 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 14611426-a214-3968-a58c-a1ccb8e42feb | -18.83562 | -47.6805 | 2026-09-19 04:42:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3597bd5c-f162-3e9a-b7a9-d0a57cef62e7 | -17.03716 | -47.2952 | 2026-09-19 04:42:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268e7ea0-af84-3a1f-96af-26de1349d878 | -18.84286 | -48.25458 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02983066-d3dd-3ced-856f-2bf90ebd9d07 | -20.45082 | -47.5934 | 2026-09-19 04:42:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f46adbb-c4c5-3329-b4e9-a93dc5145f34 | -17.24142 | -46.71784 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e28544ef-2ebe-3431-9c17-f60134b9342c | -18.40775 | -49.16369 | 2026-09-19 04:42:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58b228a7-5948-3886-97af-769f69173f7f | -16.7987 | -46.98265 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54ea64e6-5e8a-3701-9d52-b56992720ea9 | -16.79813 | -46.98647 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bb132cf-e104-337a-976d-af15954e9916 | -16.80098 | -46.9908 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e62936a7-e97c-33c7-8c93-cdfcd3426948 | -17.31886 | -46.62535 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6aae6d72-f2fb-39f2-b38b-5bb5b7110533 | -16.80155 | -46.98701 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93546dcd-9405-3fab-9803-237d0f120c77 | -17.24084 | -46.72177 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf69979b-55c3-3461-ba0d-a5d2c3633698 | -20.45269 | -47.59314 | 2026-09-19 04:42:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fe8fe902-f36c-37d6-b724-3195ae47c107 | -18.405 | -49.15947 | 2026-09-19 04:42:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6db09f91-c66a-3ff3-a6b9-3310cdd45cdd | -18.87888 | -49.51471 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5d2e5448-50fa-35c8-b155-9edffce4d243 | -18.01661 | -51.07431 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 551fa578-bf6b-33a3-87e0-0d405041fd56 | -16.83398 | -47.64409 | 2026-09-19 04:42:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bf500f7-bb53-3bd3-91c2-c681e2bf26b2 | -22.49429 | -47.09614 | 2026-09-19 04:42:00 | NPP-375D | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9791137-bbc7-3676-abad-ab035e158e06 | -16.88687 | -50.57915 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c486cc68-0063-392f-9485-e0e2acdd68f5 | -16.88622 | -50.58299 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 164c0545-89ff-3567-9534-d891bf5e782a | -17.2443 | -46.72233 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6be7ed0c-d62a-3ece-8ba8-15c803969830 | -16.11769 | -51.94326 | 2026-09-19 04:42:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 562dafc1-2fce-3b87-823d-f7d2a719c789 | -20.45141 | -47.58945 | 2026-09-19 04:42:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4114fbde-fe82-3aef-a173-9890a22521a3 | -22.0382 | -49.55472 | 2026-09-19 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17539a71-0a57-36d4-b50d-7144925c2cc8 | -19.55933 | -47.66257 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 574c96d0-81b1-3958-9220-f49307927951 | -18.01594 | -51.07825 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80f45cbe-19f9-3292-ab1e-6b67ca57cfe1 | -16.83904 | -47.6336 | 2026-09-19 04:42:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e15a0d1b-28ef-38f4-bf37-cda962766a67 | -16.97499 | -48.6262 | 2026-09-19 04:42:00 | NPP-375D | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8553e395-2b5b-3c36-b049-b7e83c01e482 | -17.06287 | -48.66669 | 2026-09-19 04:42:00 | NPP-375D | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1944832a-575a-3de4-8699-81102fa8288a | -22.02659 | -49.54112 | 2026-09-19 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20070423-6f3e-3723-bd3d-afe974902fbe | -17.05772 | -45.63613 | 2026-09-19 04:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b54a059-a748-31e5-b779-7b5061c845e9 | -16.8828 | -50.5824 | 2026-09-19 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0c99326-f9e3-3b47-bd90-14cb71158df9 | -19.56158 | -47.67084 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f97e920-275e-3400-b712-792dd9a57251 | -18.8257 | -47.9309 | 2026-09-19 04:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README68.md)
