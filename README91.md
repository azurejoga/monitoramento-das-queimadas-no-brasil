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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dbf79ef-b431-33ae-952f-eff6aa48f89b | -14.0197 | -53.8892 | 2025-10-01 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e24c9d7-d4d6-35f7-862a-d69b44d1202d | -10.91546 | -46.56644 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 694d6d8b-2cb0-33be-964e-4e7c77eb9b6a | -11.16127 | -47.21291 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc0ad76-34c1-3f38-ba50-f4a3c0582ac9 | -13.53232 | -47.26161 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56182e42-00a6-3de3-8c36-54c17971756c | -11.85287 | -45.0176 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f531eea1-ac23-3129-86e4-4ff205284f6d | -11.08262 | -47.83089 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41e0aac-4baa-30b4-b969-9225429fbbcc | -12.2396 | -47.81866 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d471e957-9a35-3cd2-b22c-a8d155ea2bca | -13.15006 | -47.40727 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff9674d0-6e5d-37dd-9060-1490ed7b3b72 | -11.83894 | -48.05391 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4d80e818-860d-3a96-a2be-5174fe81d801 | -12.85427 | -46.9432 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e86b7c3e-0776-31ef-9600-f215296328ed | -14.17983 | -46.12225 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3cd36d5-98bf-3063-b0bc-f4d88937797f | -15.29863 | -47.8688 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eba40d0d-689d-3245-9401-c2b579c451cc | -11.95955 | -46.58708 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd414b9b-c973-307a-9536-cbcd2c28186e | -13.36229 | -48.15588 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d9b309-c0c9-3360-abd9-31b7ac747c76 | -12.40056 | -51.07605 | 2025-10-01 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00651f76-948f-3a31-bcc7-049e2a7747e1 | -11.79962 | -46.62337 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b5a84c36-baff-3cfd-8dff-cb12e057441b | -13.77352 | -48.31988 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59180d74-2593-3095-a1a7-37bec89728a6 | -11.91453 | -48.00364 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75e4a352-709b-3112-892e-57aeee249f24 | -11.33962 | -48.3174 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4626b706-9247-338d-8429-10aaf332e063 | -15.26202 | -49.2798 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 60a714bd-3a03-3745-9647-68c8040ed19f | -12.87524 | -46.91505 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e7355a5-713a-36cc-8134-86175bcdae35 | -16.00627 | -50.8741 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6ac9c1c-24fc-3b7f-b38c-748df800c2ee | -15.54218 | -44.33363 | 2025-10-01 04:51:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| eac0ab79-92ee-33cf-9529-5a0fe6de2b91 | -9.57423 | -50.95101 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82b70564-5c31-3b64-afe1-2e06c31b0e70 | -14.98948 | -46.96946 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d10edad-491d-3b68-bbdd-4648729614f5 | -12.42953 | -50.17793 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dce506ad-8bbd-3753-bfce-13ca63d7f34d | -13.76552 | -48.40762 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db043a72-13e3-391f-abcc-2309cbaf2e1a | -11.85549 | -44.99812 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 69831e10-5981-3e56-a7cc-928cdbf69acb | -11.56778 | -50.1851 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaf0b4c3-123b-346d-9b83-9582c903603a | -14.70834 | -48.26508 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf336168-03e5-3fe3-ace8-1b8f162d6272 | -12.83303 | -47.03624 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15b0d7e8-31ec-311f-b617-b9d66bdbac37 | -12.81953 | -56.55404 | 2025-10-01 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 759a641d-6d44-36e1-af75-a8e370878992 | -11.16694 | -54.1203 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caed56e3-09b0-3ebc-8b8d-db5bc73340fc | -14.18797 | -46.1223 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad06f77a-cdb4-311b-a8d6-c5373fe51c30 | -12.21356 | -47.80449 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52812e8d-2fc0-3444-9a78-31326cc14c0d | -12.78413 | -46.86221 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5ce8ac3-e2ac-33e6-a1fa-17174a3386ed | -15.48931 | -45.90792 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6efe9ed5-cc07-3a82-aba6-4a6350daf94f | -15.18372 | -46.4057 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20a46673-715f-33fb-83a5-ef5846276749 | -12.00845 | -46.63281 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec330d1-c05a-3f82-8312-a2b0a02b7463 | -14.05834 | -45.03522 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 843e0c2b-04b2-312b-ad8b-619c165ec0ba | -11.75348 | -46.83658 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0876f5f7-0d67-372e-94bb-7400437bf439 | -13.61127 | -47.28105 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98def8c3-fc72-39b0-94e2-6864e023e664 | -10.6713 | -48.55084 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b4a8f6-d6ad-3a4f-99a1-4dae3e2519ea | -8.26063 | -54.95711 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fe6bd06-d3ca-3911-bb7e-e4bf41417be2 | -9.89625 | -45.93797 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ff5656-f5d8-3d3b-90e4-bc2759e68607 | -15.32632 | -47.37087 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdaddb62-e289-321f-8ef5-cbabe6336f10 | -15.236 | -48.73199 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8dd46fe-47e5-39a0-85ef-9b91149d1c7b | -15.17087 | -49.08031 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 324efedf-9766-348f-b684-9b8d6469407c | -14.7187 | -48.16013 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2e4ed2a-a2d6-3857-92e9-63419e4c616d | -14.92566 | -47.8219 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae766ed9-22f4-3d4b-ac12-1d30b618bd8d | -13.13018 | -47.43048 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7b67dcb-3ef5-3cc7-8c25-7ef5c78ac90b | -10.28795 | -50.46337 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 02a91b31-3063-38bb-8815-e97da2f8686a | -9.48624 | -51.78725 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9257c828-833e-354d-88c2-77e3d9eabcc0 | -13.32392 | -48.14528 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa00b36-7132-3c33-8e21-f0ee8cb5163f | -13.29236 | -47.2322 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe98c12b-c7af-35b3-88cc-22147d7e359d | -11.28098 | -47.80853 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5e3c0f4-4a73-347f-ace7-d4109d7c53af | -12.77455 | -46.86947 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e139d6c9-ff2b-3dca-af1f-0aa1826a0d1a | -14.34772 | -45.93297 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46a94fa3-7700-3433-980e-29996f28f927 | -9.41824 | -54.70721 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f7a82c-eecb-39af-9c1a-f45fc4f3a256 | -11.08133 | -47.84001 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6561e5e-c767-33f2-9dc9-06f328a84990 | -9.40185 | -54.71716 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9236f155-de57-38a6-b77d-24d54236c3d1 | -13.71352 | -48.65394 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94adf5a8-52fe-30bc-9986-031d366594a0 | -14.70184 | -48.25372 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4bd8bcf-d03e-3b70-b487-616e022a2fb9 | -14.01756 | -46.32378 | 2025-10-01 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cfa8164-176c-3838-b9e1-cbe3db671a8c | -10.8356 | -45.38675 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cba6cb5d-81ae-3055-91a3-a78e7987dad7 | -12.22804 | -43.74987 | 2025-10-01 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 361524e8-ca13-31da-997a-8710c5a1bf33 | -14.55029 | -48.2322 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71a7081d-bdfb-3dcf-969f-b709fa041ebf | -11.08719 | -47.8265 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a4f1280-13b6-34c1-ad19-7d27c27bccbb | -11.16005 | -54.11912 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dd553b7-271b-39ef-8d50-34dfd596738a | -11.94758 | -47.07823 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2295a7a2-c7df-372d-95bd-c54392e3eb0d | -11.08331 | -47.82609 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 963040b8-b2c7-3472-baf9-51d9595bbc83 | -10.06749 | -50.26376 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1ae1ecd-ce8a-36b3-8888-f3dd997391aa | -11.45756 | -44.97192 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bf6405d-75f8-3d71-933c-0263019b2657 | -13.33728 | -47.33506 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dae66e70-426d-3e5b-8ee6-2913f740c505 | -11.84674 | -44.99184 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6d75348-dc22-3c92-a495-f6f9d9d6f20e | -9.40817 | -54.70128 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17fcaebc-8221-3ed1-8f17-5a7f4dd05dc1 | -12.47548 | -50.23583 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 73474f71-ccb8-35f8-ae74-487dbda4e262 | -16.40858 | -47.06281 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 735ec4ae-0e18-3134-b5b1-320d269d4d74 | -12.86691 | -46.94443 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0062ed6-f9a8-3367-9630-6c40f56a1483 | -16.08682 | -51.0358 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6182742-6c42-33d6-9a01-9dba93b3c856 | -14.98223 | -46.95784 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64468f15-84f2-39db-adb6-87689970c1f9 | -13.33365 | -47.81262 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc90706f-7499-312f-aa90-c39a405926f8 | -13.77217 | -47.95326 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00964fc7-a475-3719-9b92-8ae7354e16ff | -13.72484 | -48.81593 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a65326b-c3c1-3789-8323-49af78d7a5cc | -11.92258 | -47.88954 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b094c6f-936c-358e-abff-fe51b2a606a6 | -12.95368 | -48.4296 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ced0a76-37f2-300e-b11a-fc13b29ecc4a | -9.93569 | -43.6639 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4669f22c-1ef1-3f78-ac92-0ed4e90c275b | -15.61415 | -47.85532 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e6154c9-2650-307c-9de8-0cb8dfa82a93 | -10.10789 | -50.31919 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d36cbe71-7a36-3e9d-b434-7b525176ad6b | -13.73549 | -48.82243 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47c527fb-dae6-300a-8747-d326c29e3bfa | -10.7451 | -45.37524 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e059287-a3fd-38e8-94c5-7cb1f03402a9 | -12.00685 | -46.64463 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a35b2b9-46b5-3226-8b9f-717de957ce8e | -12.85647 | -47.02011 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f61d070-97f9-324d-aafe-d1dbf180dfbc | -13.9328 | -48.11219 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b979bfe7-e0dc-3a26-8886-798d71f39d00 | -11.43503 | -44.94606 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5925b271-fffc-3c0d-b2c7-5a42174bb7dc | -9.93493 | -43.66973 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49a7e6c8-32a3-3a88-92d0-004e6cb6291b | -15.44069 | -43.64225 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba808f6d-9e8a-366f-9374-e3e2c431a0d0 | -13.92661 | -48.10958 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ab65ddd-b801-364d-891a-3ccaa4b20644 | -15.29473 | -46.19032 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 324eb004-ad34-3d28-ac39-4ff2c581772c | -13.80212 | -47.48945 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README92.md)
