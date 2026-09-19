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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b2306d5-3aec-34f3-bcff-386390a24ce0 | -1.176 | -49.305302 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14c2a35-8686-39f3-b486-bce2b5517572 | -13.6849 | -48.5924 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25e2b702-c22f-3701-a2ee-fef0edaf0bb7 | -1.8292 | -54.854 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c789345f-5c50-3144-9e62-65190ce3537d | -18.048 | -49.297298 | 2026-09-19 00:41:00 | METOP-C | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a811dc8c-05fd-3ec9-b957-45c35b371f4a | -10.1291 | -45.561699 | 2026-09-19 00:41:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 808a2b8c-6914-3f92-853e-10f91a35fe96 | -5.8882 | -49.7911 | 2026-09-19 00:41:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85789b9-68a2-33e1-92e3-39c52ddedbe2 | -7.6349 | -46.109299 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 573f3bb2-d4d5-3bc4-8c7d-a3bbc7524e4f | -10.9222 | -53.956902 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 726dc5a1-aa2f-38f8-89d1-809938352fab | -14.1297 | -45.170898 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 398492a0-edbf-3fff-99d7-f086156cefca | -12.9706 | -46.980999 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6467ad5-bc73-3836-903c-f20aa21b9b1f | -14.1001 | -44.827499 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b34a040-c212-38a2-b422-416937b05869 | -8.4093 | -54.719799 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2590188-d99b-377c-8d1a-1ce1d1ae7831 | -2.8231 | -50.456001 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f63fcfb-96bd-3035-b541-56a117442523 | -10.8223 | -50.159901 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13bb65e6-f677-35c7-8ccc-184178a1e5d1 | -2.6608 | -49.4814 | 2026-09-19 00:41:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3da4da-943c-3004-af8e-29aa56363bbd | -6.0026 | -51.7953 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49caa7b0-3752-343a-ac51-7a29f3aca2f3 | -13.013 | -46.941101 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f773cb1-7695-3920-9a67-aad137a91c5a | -12.4067 | -45.055 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3150020c-6296-36c4-a9fd-508afd007a55 | -15.027 | -48.5658 | 2026-09-19 00:41:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2c685b7-a987-3953-819d-be4121d9ced4 | -11.3109 | -47.2584 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6db7bb-66a6-3f8c-bd96-4decd6ce2464 | -10.6165 | -50.252499 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67b4f36f-1e05-339f-9d91-4b307bc10f7c | -12.5496 | -47.080002 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60e4cde0-84b7-3803-a208-74ca12696d20 | -12.7405 | -47.012798 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c481f96-bd02-397f-beee-02f2c3c562a0 | -13.0162 | -48.6404 | 2026-09-19 00:41:00 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5a96284-7f44-3330-8ebe-34eafef527d3 | -12.2857 | -49.150902 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cca0a47-528a-37b5-98c4-9de9ff370a7b | -4.5638 | -42.969898 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b637ea1-a165-379e-bba0-61085c071fcf | -8.0798 | -50.9636 | 2026-09-19 00:41:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f445c1-5a85-3ef3-af85-c5c8743c006f | -12.8357 | -44.384201 | 2026-09-19 00:41:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5801d9a3-7b7f-38be-9a3c-5fcd94a1d26d | -14.7956 | -48.5425 | 2026-09-19 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bbc2d607-33fe-33fd-95e2-61d4c32e9b1b | -4.5995 | -42.947102 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 175f8b43-3e32-3d0c-9600-f43f77f11664 | -9.2535 | -45.922001 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec6d8ecb-5bbf-3fbb-8455-776f22d08441 | -1.2213 | -47.7155 | 2026-09-19 00:41:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a81bb0f-8d0a-317c-95ce-b4ff19ea540d | -7.5554 | -49.597401 | 2026-09-19 00:41:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51357158-c5e4-31a0-91b1-cadecb515d3d | -11.4115 | -51.445499 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29320a4b-ace5-35ac-b2f7-84096f8bf612 | -12.1286 | -46.999802 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f37ba46d-4bb9-31f2-b5c1-17c8da4077de | -8.4749 | -47.004101 | 2026-09-19 00:41:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96f00f9c-eab2-368e-bcbe-87fe1b1e88c6 | -4.5669 | -42.940399 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 647daf4f-99dd-3490-afb4-ca32af84ca7b | -6.6605 | -50.922798 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1fb88c3-b28d-39df-b668-b034517706cf | -5.516 | -43.8022 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb819b3e-9b86-3124-9fb4-4880f1e9f305 | -7.8559 | -44.866699 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a6cf33e-cc2a-3e43-8c20-90344c5ee2cd | -5.8965 | -49.782001 | 2026-09-19 00:41:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65210cc1-6903-3496-98b3-36288e54cb31 | -0.5226 | -49.1558 | 2026-09-19 00:41:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f4d3d4-bbce-3e72-85c3-13ad69b56d9d | -10.932 | -53.954899 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 920f3063-7e67-316a-bd52-fbe46cd54a61 | -10.9166 | -48.420799 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2b6dba2-03cb-30a4-9070-39b010eddd54 | -9.2456 | -45.932301 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0258a9b-eec0-3241-807c-0ccb672b40b5 | -12.1449 | -46.980999 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 339aab97-ecf5-387b-b457-e0d7d4443c18 | -11.4384 | -51.4753 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c264ea29-cf7d-3bce-932e-7cb4c6e13b6d | -3.5171 | -50.784199 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51b04f8-0711-30cd-bc52-bb542ec83082 | 1.2591 | -50.961201 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| acad2bec-ecde-3641-a54c-3c1f54cf087c | -6.0043 | -51.802898 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da1bf98c-09a8-3575-b8b8-6a9016c3698e | -10.799 | -50.894501 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19e34f8a-cb35-3039-99ae-4ff9e41cf74d | -5.9945 | -51.805 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0417ffcb-988d-3526-94d0-68584c0b6abf | -10.9295 | -53.943298 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86cedc57-b563-3a34-b91f-250568752ad1 | -11.2777 | -43.504299 | 2026-09-19 00:41:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0ba0b98-a431-3be3-8b82-1e4ae2688c8f | -10.6096 | -46.108799 | 2026-09-19 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d2d016b-e746-3a4f-bb90-53aef7813a79 | -6.3172 | -45.601898 | 2026-09-19 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73112185-2290-3816-8b1a-19f19edb1e53 | -22.0359 | -49.557701 | 2026-09-19 00:41:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e85c7649-2051-304a-b846-b648d4d04b8c | -5.2502 | -50.972099 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96a07964-4329-3ebe-ba8e-e49b6eea5298 | -10.8469 | -50.177898 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54cb0a8b-aa48-31be-beee-f26d985bbe50 | -7.0226 | -44.6637 | 2026-09-19 00:41:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08b3a545-8b1c-30ab-8a03-88afb0fbda78 | -10.1712 | -48.4529 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6e151ad-c763-3747-a0f8-109b9164fa6e | -11.9335 | -50.117298 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5c1de1f-75de-3ad6-b1d7-1e03f3ecbd95 | -3.3322 | -50.112801 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b04386e7-7aaa-37b4-8288-95771ae24920 | -19.558599 | -47.658401 | 2026-09-19 00:41:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5227f7-1b63-353a-9a42-e75f93d52049 | -7.2255 | -49.642502 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d16c6ce-52fd-3124-977c-291470a40bc3 | -9.0488 | -48.730701 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c5e4788d-4242-39a6-a9bb-b86bd959f5d8 | -3.3697 | -50.455898 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae95a3f-0a64-3e51-8da6-78dbce80aab2 | -8.364 | -47.237301 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8768ffd4-675d-3785-bef3-fb35fd4d40f0 | -2.7279 | -49.459099 | 2026-09-19 00:41:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 910c3086-0bf0-34d2-96c0-e953fe95bbd1 | -5.8866 | -49.784199 | 2026-09-19 00:41:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596c1248-5c2b-30c5-86bb-6a34add0e5c3 | -11.4366 | -51.466702 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11e6f67f-3bdd-31f3-9d2c-86cd141540d1 | -6.987 | -42.180801 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 327704f6-edea-3c22-ab7c-683237446d71 | -11.361 | -44.144798 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 051f398d-0a21-3333-a22b-921b58ee5af5 | -10.4482 | -48.673698 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfac1a11-6828-3979-8516-bac5662be6c0 | -9.7869 | -45.036098 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 31550068-9934-36f2-aaf4-c76536ff309b | -4.0586 | -56.2355 | 2026-09-19 00:41:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad1daf7-fa86-323c-a112-9398c24e9e3d | -14.6884 | -46.641499 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f2de301a-8871-33f1-979f-86728493a982 | -12.3311 | -50.7164 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e7e73aa-c146-3518-b06c-d40fe1961503 | -9.0472 | -48.723801 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 11f586f9-2bcd-32c0-9fe1-e5f179cdf6ff | -10.2028 | -46.576801 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30d409f2-7f46-31a3-9c91-30ab56bd9ce7 | -10.9174 | -53.982399 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 251457fc-7a8d-34e5-91f0-518d6accf332 | -10.0517 | -44.889999 | 2026-09-19 00:41:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3aa1ae40-8868-3024-92b3-2778e17d940d | -14.6917 | -46.655701 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38fc79ee-8878-3e82-9d88-160e18e82b9c | -7.8674 | -46.4384 | 2026-09-19 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61d60582-cad0-30d3-ae56-e47b64dc661a | -9.2478 | -46.2043 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 927bfb31-930a-3ab6-a1eb-70f9f7c401ff | -11.018 | -54.122299 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab38e8d-4569-30f2-835f-1f26837c41e3 | -4.2571 | -48.530102 | 2026-09-19 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2672039f-f3fe-32cb-b086-d150a0cecbb2 | -12.1319 | -47.014 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa44251d-7ab9-31d8-b603-4e56f4f0bc56 | -13.6084 | -46.927502 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aea27408-782a-34d1-b498-b55bb08fa634 | -17.952101 | -45.117401 | 2026-09-19 00:41:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab8d891-14a5-344d-aba7-ffefbe4c79c4 | -17.323999 | -46.619499 | 2026-09-19 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5564fe66-6074-3641-9822-794207a8ce11 | -10.2063 | -46.591599 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9b70600-d93c-36cc-a9d7-3c882ee2d9c8 | -22.0341 | -49.548302 | 2026-09-19 00:41:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38a90f30-c84b-3bad-9c86-e5653cd88796 | -10.8371 | -50.180099 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d9c340a-ae36-334c-ae0c-45df9f3f3ac7 | -3.0321 | -51.368698 | 2026-09-19 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cea87a43-d7ce-3361-94ef-29d6c9f88671 | -11.3336 | -47.356998 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2a1f4e-0de5-30d6-88c4-827fbd535fa1 | -9.0441 | -48.709999 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7783bd-394b-3975-a543-97f17096f68d | -7.8569 | -45.173401 | 2026-09-19 00:41:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79b79f3b-3bd5-357b-a809-4183f5feef65 | -14.1675 | -47.026299 | 2026-09-19 00:41:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a1d987bf-1758-3a4f-8d3f-c75153864978 | -9.9377 | -45.277901 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
