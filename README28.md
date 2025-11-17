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
| 67347f5c-fd8d-3894-b246-99614889cbfb | -3.58896 | -43.59765 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 376391d4-20ea-3235-aa0c-a1b99fc009af | -3.79714 | -51.15915 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2388021c-561c-3bca-9a18-8c384eb9261b | -3.38708 | -50.13559 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35493ff1-1c7b-38df-b85c-816bc8ce05ab | -3.80918 | -51.33923 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7214b43b-fe7d-3fc3-99e1-a89bad17ea17 | -4.4074 | -49.34083 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ea41352-d46d-3214-8b2b-5206072619a0 | -5.47941 | -40.96262 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 30f60341-e856-33ce-8011-5bc1217cfbc0 | -8.05342 | -45.66362 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74e75267-208d-3663-8336-efadec923de6 | -3.6495 | -50.22454 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075ecd33-1fad-3d5a-af05-fc9bc9f366c1 | -2.52678 | -47.81504 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e098b64-8ec0-34ec-8535-1d6f574b56ae | -1.62917 | -55.71141 | 2025-11-17 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb525159-1493-3919-90b0-c4898a0e0ac4 | -3.26057 | -50.77704 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c843e0-569c-3403-b02c-269693c59557 | -3.01391 | -51.34138 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77ed55e2-d743-3d4c-ba97-17a3d6112cad | -4.95287 | -48.24656 | 2025-11-17 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c3e9f14-6d07-344b-9e13-bd48f8059bbd | -3.3509 | -44.43085 | 2025-11-17 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d9b0409-7487-395a-a45e-3ed30548d418 | -2.9665 | -53.21822 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47373af8-85a5-3ef0-982c-245d039884da | -3.44839 | -51.41457 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af5151a-e382-3f38-b333-a99cd0650b0e | -3.58834 | -43.59824 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79507b30-66fb-31b3-9f6f-5cd524b7ebda | -3.32675 | -50.17788 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 642e2870-add3-3c1e-870c-dbd3e96a6675 | -4.0596 | -47.49645 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e250b49e-4ab6-353e-a348-b26232a34e9f | -3.81137 | -47.49442 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46dce23a-4db9-374d-ae3c-22bda725b69f | -3.3583 | -50.1863 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9aa7f09a-437e-3547-910e-0b4ded8bc2d6 | -3.78031 | -50.14191 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258d1dcf-2e7d-39c3-a8a6-0f855626d813 | -3.09813 | -47.77225 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 192d44eb-5e3c-3b70-9611-c9ca87401016 | -3.2299 | -50.50592 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12639b35-10c1-329b-8bc2-19f9e8af8cc1 | -5.40816 | -47.26459 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bdf5555-a8be-39d6-bcca-ae3f2c310206 | -4.55263 | -48.47861 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b816b9eb-4d4a-30a8-9457-f95d53334d87 | -8.21075 | -43.56469 | 2025-11-17 04:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58c93e82-1500-3889-801f-0b6e04ed9dfe | -7.12777 | -47.11804 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d85ea64-44ff-3252-810c-2e9ff823963f | -5.48991 | -46.9129 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dc2c387-dd54-3aab-af2a-4adecc7c4408 | -2.10935 | -50.57428 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48f21c47-d527-3386-a5f8-851a6151dd87 | -7.36785 | -45.8315 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b3ff6ec-507b-38f5-8a52-7b5728a0928d | -3.8341 | -55.80589 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6effb630-ba1f-35b0-a546-355cb88e5163 | -6.68694 | -42.05049 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 26aa25f8-2816-36f1-acf2-b80cd6e12e44 | -4.00958 | -49.10089 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7eb0cdbd-65cb-3c20-b254-dab09c9f8ad5 | -3.60774 | -42.41788 | 2025-11-17 04:38:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d1ab3e2-caff-3e68-abf4-d514aa105df9 | -3.40432 | -50.26734 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6deeaa41-54a7-334d-95c5-1e07571fdc71 | -3.60838 | -42.41362 | 2025-11-17 04:38:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8dc4e9fe-ccfa-3109-a7b4-803081e9d424 | -3.0166 | -51.37032 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 049b4dd4-e278-391e-b989-078bb4ddacdc | -8.12409 | -43.54054 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3916e809-e6a0-3eb1-95c3-b88a4a2e8cd4 | -4.69283 | -46.31184 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf016a40-9e6f-37c3-90f7-de0e5014e6bd | -6.81343 | -48.79058 | 2025-11-17 04:38:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e79728-eb03-30bb-b726-6cbbc57260e2 | -3.35213 | -44.85198 | 2025-11-17 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b62c6af4-797f-3e64-ad0f-0f8451de66a5 | -3.40274 | -50.18951 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e224a1dd-d4f7-3ed3-8da8-179b4ccee944 | -2.51684 | -47.8135 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 427e1766-d019-35fc-b313-1fe10dfd3ae8 | -2.94419 | -51.75974 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42456cc0-55cb-3738-b0de-5b51b5197c6a | -3.77752 | -50.13782 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| becf6082-41c7-3770-afdf-75a04624d338 | -3.58294 | -50.71575 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9c9d2ac-eb1a-3d58-975f-0b55f6eaa1aa | -3.66816 | -44.88941 | 2025-11-17 04:38:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d05c1115-7a80-30fd-821d-ec21933fa7cd | -3.59249 | -43.60179 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a638e4eb-5c41-3b35-ac1a-1d6dc6926a3e | -3.22327 | -50.96545 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3859c654-d4e0-34f5-9e14-467d9500ecad | -3.4135 | -50.12129 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff703c80-78e9-330a-8a99-e2877a2bab91 | -3.04929 | -50.24928 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b953824-17ba-39ff-886d-8420fc5a7141 | -5.74658 | -51.30934 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9778872a-c8e1-30e0-ab1f-e2621479df39 | -2.51245 | -47.81991 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e11e3cd2-ff50-3b48-84b6-9b473aea8bd7 | -3.32686 | -49.89263 | 2025-11-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 767423b4-88aa-352b-b7a1-f8b8e579ca20 | -3.23614 | -50.51068 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5183a8e1-c829-38f8-a8f5-c0b49a5d6c8d | -3.8799 | -47.18617 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 870585e8-6d29-3201-b5c2-1d1644e2ab53 | -4.05117 | -49.02984 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7a6ceba-d4f6-37dd-8fd3-111f788d5c0c | -4.09907 | -48.02784 | 2025-11-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6bb701ad-24e8-3bc7-b9c7-87ae6c355481 | -5.09339 | -47.69139 | 2025-11-17 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d22b619-4cdd-34c6-900a-798e2d204aaf | -3.83331 | -55.81057 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 821468aa-49b4-3059-988c-758fe7d635aa | -5.09857 | -46.07435 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e92aa07-d351-3fb1-92d4-ba7926a04aec | -7.9672 | -50.00653 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbb0a2b7-c851-3398-829c-ef2e8f67248b | -3.50818 | -49.92794 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21bcc847-6e02-3434-932f-c354f164a3fd | -3.46756 | -50.1186 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc58f8c-3deb-37d9-b998-542c9087ed3f | -4.09805 | -47.11559 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c389070-3823-32e3-a900-1aa53ae3a527 | -3.45609 | -44.85638 | 2025-11-17 04:38:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 270bb478-9231-3ced-9521-361a3a621c88 | -3.07459 | -45.19707 | 2025-11-17 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c11cd10-f6f3-323c-85c8-85355cd701c5 | -7.70397 | -49.38614 | 2025-11-17 04:38:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d9633d7-f297-3062-b794-c8529cafea1f | -4.40409 | -49.34031 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c0db4e1-460e-34cc-bd7a-021ea7bd24bb | -3.49349 | -50.34791 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3eda80e-4dc0-3850-8627-e66cd348f0a9 | -4.67966 | -46.93869 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66ad85f7-09b5-3ae6-b45c-087bc241d97d | -7.95077 | -46.84493 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89a14799-c6a9-3c26-8fd4-71381d84e821 | -4.245 | -49.68063 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 797bd306-ff46-302f-b35c-b99632f0552f | -4.64491 | -50.97157 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4a6767-0fdf-38cf-b297-a7b6d1eee555 | -4.39878 | -49.78397 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c12c618b-3e5a-3953-9c7d-5e81c3a0ee40 | -1.53279 | -55.51806 | 2025-11-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c1265ff-943a-3873-88e7-022b7141aaec | -3.77636 | -47.74176 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e02ec70d-a55e-3e05-970f-a1d911159f7c | -3.74942 | -45.87476 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e88a51ea-ea3a-3926-b2c2-6f4955e62b45 | -3.17455 | -48.13204 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9a746d-6553-3638-a103-b1dd5cfe4741 | -4.97486 | -43.88314 | 2025-11-17 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 427e9dd4-15ef-32f5-8782-c33d965be0aa | -8.30789 | -43.94236 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 426676ea-c961-33e1-9e34-6e6b39e47c3e | -5.62425 | -37.80325 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 32f19b32-4568-3097-a989-f8934a9b3754 | -3.55387 | -41.99409 | 2025-11-17 04:38:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0cb5ae7-1459-34eb-beb4-593053216c52 | -2.20382 | -50.82252 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7e77da2-35f3-3058-9d08-3e92865241f5 | -6.48577 | -47.19178 | 2025-11-17 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7233d59-b56d-3924-81e3-c6e5f987c08f | -4.9979 | -44.35471 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c10e442e-5b06-3aa3-aafa-5813b746517b | -5.11435 | -46.23384 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ebfedb2-c7c0-3a12-81d5-d5ead2e2ab9f | -3.66076 | -44.73495 | 2025-11-17 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45991d95-3280-3344-9e8f-4a7830630dc1 | -3.46362 | -50.12165 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a867f6c-7728-3bd0-a95d-54817cc8b3e2 | -2.24463 | -53.6197 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fe295cc7-584b-3226-ac2b-a61c7d52b4b4 | -7.83755 | -47.19259 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67dccd91-4f3f-3433-9723-a2198a70be1c | -7.12718 | -47.12191 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d669cdff-728d-3f49-a4f5-9ba092826942 | -4.70478 | -46.3086 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e77b05c-2dca-3dbf-97c7-929fff4d4cf2 | -3.89972 | -45.18595 | 2025-11-17 04:38:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a8aa4f4-c4d0-3926-9a93-2b8fd9c3a773 | -2.4759 | -50.23521 | 2025-11-17 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1b1f62e-5303-3ee8-801d-fe5c0fe47a7e | -3.8907 | -46.46043 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9145421e-2a52-340f-9301-feda9322173e | -3.80975 | -48.92181 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fb921a09-018a-3289-a4ec-a7f19313de8a | -7.61931 | -42.57955 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f01d9163-feb4-3604-9e19-12456b44c328 | -6.77268 | -41.44333 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |


[Clique aqui para ver as próximas entradas](README29.md)
