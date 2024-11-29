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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffa4f543-2ff1-3e66-bf7d-9c6f064eb611 | -2.88117 | -46.83957 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd39718-2d1d-363f-b168-2facdaa3c5a8 | -1.67885 | -52.53037 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83457311-e364-3f2f-abbf-f361a3265a16 | -2.3476 | -53.92318 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ec53e7c-d51a-38cf-a589-8fe97dd5fdd6 | -3.67656 | -54.45048 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c8093da-76fa-3a2f-9444-dedbf310a5a4 | -2.21563 | -52.4799 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6066c7-c973-3875-9c7f-1dd34a6786bc | -2.88963 | -55.22175 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c7b7d3d-1abe-3c72-be61-849f1e65a2dc | -2.84911 | -54.02468 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 918948fd-98d9-3f2f-a636-9d20943c3f64 | -3.96894 | -47.94661 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f31f72be-716d-3b38-a967-8db88fa83137 | -3.22982 | -54.09802 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 188c84f1-788e-32d0-810a-639a4b002ca3 | -2.36946 | -55.70836 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db654bab-3e2c-3464-9cee-0d251f80cc64 | -3.7024 | -50.51408 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2267f511-1a7f-3b1a-bbe7-51868129e520 | -3.33105 | -46.69242 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0da6fc02-df02-3e51-905c-79e440e48373 | -3.46963 | -50.53052 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdd30599-d478-3993-849a-d863cded8252 | -3.1716 | -46.30536 | 2024-11-29 05:22:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e49f3545-addf-3996-907d-6e68ea4917a2 | -3.67361 | -52.11023 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58488fe7-330b-3607-9040-8590a9e40ff6 | -3.03049 | -54.18876 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8d7269-3365-37f2-ac84-c861bd947f55 | -1.64618 | -52.74375 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b66ba7f-854b-33ef-93c1-8e1c977b0ddc | -3.6968 | -51.37107 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c65236-30bd-3b77-bded-c7dc8bbd478f | -2.98156 | -53.89643 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34e620ca-b3a6-3832-b2c4-9d59f1055a51 | -3.21366 | -53.38107 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044cef65-48b8-3afe-97c0-5e4df7e0bd52 | -2.05682 | -56.08018 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2289a85b-2c0f-3974-a1d4-2268cb1f3c85 | -2.83344 | -54.10126 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 494cf3cf-9f7d-3a6d-a13e-415487ee0e01 | -3.49934 | -53.82876 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 674d8970-f010-3356-a05b-ee4e0f29cb38 | -2.98439 | -53.35537 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5964092a-71b0-3a8c-bc18-ce3d77a94365 | -3.42442 | -53.88714 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaec46b7-5267-3c71-881b-be4ed1588b85 | -1.58087 | -53.84117 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 09a95fb5-32a0-3467-8b87-1684cdacb147 | -1.5803 | -53.84498 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 37a0ef6e-dfb1-3907-8d4a-ea2b28c26b30 | -3.91833 | -53.66738 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fec2fa2-ea60-341a-ba8e-cefe8fdf6d26 | -3.20294 | -46.56406 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| afa119a6-8def-363f-af82-dc26c794fda1 | -1.52617 | -55.37508 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56149ce0-0903-3b0b-8fa8-2a46f90f4944 | -4.33738 | -47.57399 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 409c8b57-23f4-3298-8489-b97011d96294 | -2.26214 | -53.47544 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 591835d3-62df-3067-b69f-a5a9174cf6f3 | -2.97776 | -53.27808 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aec08c14-e0e8-3eef-b779-c8308ee43b5d | -1.70073 | -52.45828 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 47d529cf-0d8c-3bd5-bb1f-d3d4bb037d76 | -3.9607 | -48.08482 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81cece54-45ae-3507-8090-bfc782ed923f | -3.38641 | -54.28666 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56f084c1-3411-3939-97d4-dc3e8c11bc9a | -4.18171 | -48.61156 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7198137f-d255-31f6-99b7-062e9209c5c4 | -2.37127 | -56.11978 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae05485c-6ef7-3560-8612-82426303940e | -2.65644 | -48.78625 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1448af6f-6a62-3a51-804a-606185c97c7b | -1.32738 | -55.83537 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebee8ad9-3b5c-3560-adba-fe28626355dc | -3.09534 | -54.01986 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525c7d87-cf3b-32f6-9904-91b6bfe2154b | -2.66111 | -48.79595 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 174143a2-8a93-3ea2-9cfa-25700c0ca7f7 | -1.70148 | -52.45353 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 4b6d2dfa-6b4d-3a13-a193-3b2c410f06b2 | -3.39182 | -50.11021 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e792c351-f5d8-39f1-aafb-1dbcdf76cf6a | -3.85188 | -52.30368 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e6ea75d-0df7-3a9f-b5e1-c63750493593 | -4.47941 | -48.11575 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb23b6c7-2b9a-3d1d-9cad-6863ecc63e44 | -2.29666 | -51.98628 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 274c43e2-ae59-3d2e-9381-49cd6926bf98 | -1.68762 | -52.45144 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b494c9c-e9cd-355c-9a92-f3a240ebb4b8 | -3.71075 | -51.79978 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a43b9f93-82b3-31f5-b7fe-8dba5dd8937a | -1.58445 | -55.24315 | 2024-11-29 05:22:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb1c615e-84a6-3a15-898b-0df5be7df559 | -1.65214 | -52.7354 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f896f8f2-141d-33d2-9002-5cd39788516b | -2.21837 | -52.48205 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6d241b7-f20c-3aa0-a3ce-bf9e5b0e4c58 | -3.68995 | -50.22108 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f58e18-fcb2-35d7-8aea-09ba697ddaca | -1.66477 | -55.23149 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2829da72-170e-3b37-b23b-3c3a3b381c87 | -2.13973 | -54.90508 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ef827eb-b22b-33dc-bde2-0a65bf8b35fb | -3.41195 | -50.16569 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be13b8e6-c963-3457-a6a9-8d9ac7757f43 | -1.72426 | -52.47947 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3edf548-cb0c-3a9f-859f-1a640ee19a84 | -3.85799 | -50.15048 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9241e7ad-d3ef-30a7-a3d5-779671dd6547 | -2.26776 | -53.46791 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93d9c283-61fe-3e4d-829d-7aa3f502ee89 | -2.83696 | -49.88767 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd2097f5-2834-326b-af40-5f9f329d9ed9 | -4.17938 | -48.6122 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb9da69a-adaa-3589-9474-7bf5f6dc85cd | -3.39477 | -54.28793 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 552df08d-8a1f-3d54-a29b-0f6d1b327025 | -1.69686 | -52.45284 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 4820ea35-b55f-33ec-bacb-40a0acade3ae | -2.74397 | -54.03761 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08f651ba-2149-3f60-ba1c-9e717159f465 | -3.05318 | -54.04268 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6453a3f-7057-3c08-ada0-2f97202281f2 | -2.76583 | -55.32755 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e03204e3-e66e-3271-9e6f-bf86da23f10f | -3.2441 | -50.77344 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a279a3a6-af52-3e2b-a247-fcf02cf64757 | -8.1265 | -47.98524 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d242304-e3d9-30cc-b12a-256d6dd4349a | -1.8926 | -54.54295 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fb90762-7738-372a-a5ff-6368c5998a44 | -2.84129 | -48.09444 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93fba5c0-bfc2-38b8-8705-6cb9c34837ac | -3.22917 | -53.63407 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69da7486-20f9-34d6-9344-037ef7e14297 | -3.2304 | -54.09423 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93f37ac1-5a14-3411-aefb-0dc36459143f | -1.58481 | -53.83883 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f0a553e6-e470-36ee-9d77-522f3b1ef94e | -3.46921 | -54.53785 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f989fccc-9561-3707-982d-596abf29952f | -2.83532 | -49.88607 | 2024-11-29 05:22:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b804f91-5de1-3c97-afb6-f865a27b92aa | -1.71749 | -52.49292 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 904f7c09-32f1-35f9-8f30-685167400bfe | -4.09391 | -54.76349 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33b530c7-bcb3-3e89-8965-bc30c392ee7e | -3.49996 | -53.79575 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe5a34b0-c2bd-33e7-9a88-c0177408c9db | -2.56994 | -49.07753 | 2024-11-29 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53f53c2-96f7-33c5-89f2-1b7efeb5bba3 | -3.32622 | -50.21678 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15dbe685-b4cf-30a4-94b3-f9591a782c14 | -3.41697 | -50.17007 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5f2f841-0ff6-3965-ae6b-80458fb0973c | -3.25533 | -53.63811 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d33fe3aa-2ab0-3b2e-9a48-d80a6debf065 | -3.49696 | -50.46026 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6274b4bd-2c4f-3ec3-ae1c-fbdbbe056f48 | -2.25101 | -53.46115 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fb5516d-791b-3831-9da5-021e5aba5df2 | -4.07675 | -50.03606 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 224c1ebf-189a-3646-bd4e-728033df60c4 | -1.90907 | -52.8881 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b17901-694e-3186-8a67-a5fd35acb856 | -4.20024 | -50.6886 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9795db7-7a04-383c-a8e6-e6069f063d12 | -2.61001 | -53.9827 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7e7845-7e41-35cb-ac83-485eb672ee59 | -3.53794 | -54.08334 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d927eac-6666-344d-be27-5b99a6fb7a02 | -1.70529 | -52.63437 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91087ba5-14d6-3d72-a654-7625696d32a5 | -3.30122 | -50.75509 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43e007f7-082b-3d8b-b539-ae918883fbac | -2.58891 | -53.97951 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddb710d1-7e0a-3cd9-b71e-52b25acd8406 | -3.25471 | -53.64227 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c740e3c-b0aa-37a5-865b-07363be4c0f6 | -3.18135 | -50.27996 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e6fc95d-d21d-32a1-9662-e662821027b1 | -3.05992 | -51.30425 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e6f1ec7-8378-3880-b064-b84eb7c6f502 | -3.17262 | -46.29863 | 2024-11-29 05:22:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e665ec7e-b237-389b-86fa-e2d91989fd9b | -3.79193 | -50.1332 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e940fab-02fc-378c-83c9-f90473152b61 | -2.59528 | -54.07801 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6d6409c-35b3-3433-b921-61c30d89eedc | -3.86179 | -50.15175 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a2ba3a-eb07-30c5-94a6-766149d76c2e | -3.2261 | -54.06568 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README95.md)
