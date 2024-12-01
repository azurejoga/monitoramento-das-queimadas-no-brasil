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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 111313a0-9504-3b04-b2eb-ace8187acaa1 | -3.44877 | -45.67083 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e8c2ebb4-e74f-3cff-869f-6fa2574563dc | -2.52097 | -51.83228 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0fb593a3-8c27-3228-8522-57920c42647b | -2.11597 | -46.55066 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1ebec6b5-0db8-3c5d-865c-df025d719313 | -3.52645 | -51.13306 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4734597d-03e9-3a59-83a1-7fa73d471a00 | -3.37932 | -43.49853 | 2024-12-01 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b5d4114-98ba-35c0-8d1c-2cad81fb3bad | -2.69308 | -51.73715 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 24245672-01f7-322a-a591-7b611ad407f7 | -2.81609 | -53.0758 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8ce2d1eb-3e4b-34d8-b369-7dee9d393856 | -2.4649 | -46.569901 | 2024-12-01 00:34:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d754175a-6796-3908-858d-cf7b23d20e94 | -3.0949 | -53.7197 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86175153-6c24-39ad-92ab-df94242acaae | -3.6827 | -51.812199 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d5d471a-bb68-38d0-b517-b15c30fe7ef1 | -3.2488 | -53.6287 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cbe054e-fc51-3bac-b660-4bed9bb2bf4b | -8.1284 | -44.476898 | 2024-12-01 00:34:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc5fb53-8f39-3772-b75a-03a457b0e0c8 | -3.0603 | -51.061901 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 283bd3f7-2000-35b4-908c-c9a957910b3a | -2.0882 | -46.278599 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cde7ef-0ddc-3734-8429-9b6dec6b3da3 | -3.4844 | -53.810299 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3b6f8b-cb3d-3a2c-888e-08acbad245b9 | -3.1779 | -54.318199 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 381ebb97-8a19-33c6-9186-737d6dc81e8f | -2.6316 | -54.2132 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c5caa2f-a658-3f17-8920-d0a8e5dc5667 | -2.1186 | -46.2318 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28547ab9-9dab-3a53-9bcc-ee2f762d10f2 | -2.5566 | -46.564701 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b61e9db2-aff0-33ab-8eeb-079a688ab42c | -4.5483 | -45.720901 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e542efe8-8eed-3229-bb1d-6fb59e7af9d3 | -6.1851 | -44.423599 | 2024-12-01 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 961b4a3d-62b2-34bf-ae56-dca686d45fa9 | -2.4666 | -46.577202 | 2024-12-01 00:34:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54d7b14a-581f-3373-b0ba-a315805bd52f | -10.6549 | -44.5033 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f53ba379-3f1a-3310-ad4d-a01ffae52c01 | -3.3319 | -50.216702 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee888798-5253-3944-8163-a308e3d6ce84 | -3.7084 | -51.059799 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e92b5c31-d9a6-3fdb-8ffd-3ea78276e0e9 | -3.1341 | -54.533699 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcacf99-7cda-3ea4-b96f-5646018da263 | -3.8121 | -52.2505 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d65f8a-4e05-3c48-a01a-260d43fed8ea | -3.3822 | -49.848999 | 2024-12-01 00:34:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4550fae2-7e93-350a-b9fc-7f70309c6713 | -8.9313 | -44.246101 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf242044-7c48-3cb1-96e3-a2e11eee28e0 | -1.6956 | -46.1418 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d008cd06-6064-3d5e-a674-1ba5e5b0cd8f | -3.009 | -51.789799 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ac417b-f5ff-3723-acef-e2b05a72d8f8 | -2.1227 | -46.561798 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 781a30b7-9c02-3868-acb2-d0dc51041002 | -2.4783 | -50.359798 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4023f7eb-da1f-3555-bfc0-cc549153e0b8 | -10.522 | -42.424599 | 2024-12-01 00:34:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c1917f2b-0509-3b99-8f68-b0b2b2c129b7 | -2.6277 | -51.7416 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43426cfa-c8f1-30f1-9c04-ab5cb32b9d41 | -3.4869 | -53.821602 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f92ab503-9423-3384-9547-e7f7a3bedabd | -1.5164 | -45.901901 | 2024-12-01 00:34:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d85dc9c-2b87-3ee8-9b83-b9e19487bda8 | -3.8219 | -52.248402 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aaf1b59-2429-302d-957e-d43dec9c20bd | -6.2858 | -43.8451 | 2024-12-01 00:34:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd90dd04-9a06-3522-8850-e047da632b42 | -2.9979 | -51.0592 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb596d3b-a153-3eaf-85bb-28489f659665 | -3.5395 | -50.178501 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7582666-21b6-3ea9-be64-5ce8619db330 | -3.2168 | -54.1717 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2945d54-f3bf-3f6d-a999-052f3459ed15 | -2.544 | -45.619598 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2b3a2a-5bfa-3c22-9710-3088d2363fe5 | -2.0994 | -47.624401 | 2024-12-01 00:34:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c26f63-e5f6-381e-9f0b-c47262922d3f | -3.6583 | -50.702301 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef4fd1a2-c566-3aaf-9576-e223b7560640 | -2.9997 | -51.067001 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9730ae-88c4-352a-9450-2b968c007b21 | -3.1187 | -54.510899 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcbf6dc3-31b7-3f2a-a176-a40d572e97af | -6.8698 | -47.238201 | 2024-12-01 00:34:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2244385-7278-3d0b-b636-08d9dc7829d2 | -2.6533 | -46.581402 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e92b60f8-f621-3d8c-96fe-ec552ecb47ed | -3.5946 | -50.3755 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce09c39-f71c-3e73-aca0-1170a8e0626f | -4.264 | -47.616402 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9c3e2dd-f0e0-30f6-a395-50e515526b4c | -2.1112 | -46.556702 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faadb3f6-d406-3066-8572-afa522816ad2 | -6.9187 | -43.553902 | 2024-12-01 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 899755de-a853-341d-ac13-21e6d8f22bf5 | -3.3084 | -53.848701 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95baea32-bad1-380d-8f77-b741d5b4a265 | -3.3352 | -53.3736 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 039bb5b8-b4fa-3a0b-be9d-ce3c5ef3f34b | -3.6944 | -51.818802 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc45138-3bdc-3eae-aa1e-345abb8863b6 | -5.9148 | -43.846699 | 2024-12-01 00:34:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a25d568-554a-3af8-94c3-e2d69a2d2cd0 | -2.2428 | -45.432098 | 2024-12-01 00:34:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e27d4d5-37ab-33a6-976a-d164967630d1 | -2.7517 | -51.653301 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec88a49-0a54-34c3-8705-7bccd3e21bd0 | -6.1949 | -44.421398 | 2024-12-01 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 615b473e-6f8d-3403-9218-2cca207dd4dc | -2.8282 | -52.582401 | 2024-12-01 00:34:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f3a7e6-372c-325e-a16d-7869000e46d4 | -3.0653 | -53.2686 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9508df09-7715-3240-a4e9-adbfe9a7c2d0 | -2.1146 | -46.5714 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef79200-2fe8-32a5-9cc9-3ed7e8922e5b | -3.1285 | -54.508801 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5158e747-1a0f-3e2c-ab36-45e719db1b21 | -2.8842 | -47.448399 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8d91a6-89c6-38a4-b9ce-6a92ff998105 | -2.101 | -47.631302 | 2024-12-01 00:34:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b4609a-e1e8-3764-8ecb-edd7a4fe8af6 | -3.2063 | -53.1199 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb4caf0-83ce-35a9-80fe-bfba62a57142 | -2.6797 | -46.606201 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| baf80982-05f0-3eb2-ad27-4785cfb51a0a | -3.1148 | -53.808399 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a73d67-219c-3b0f-bbe3-cafa2bdf227e | -3.2664 | -50.2005 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfca0c3d-7cda-31cc-a5c2-ebeab17d9121 | -3.3839 | -49.856098 | 2024-12-01 00:34:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9603923b-b9cd-3715-8a16-05913c6f05a8 | -3.063 | -53.258301 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2e129f-c4c0-38b6-838c-fcd1e876766c | -3.6633 | -51.726299 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d354ae3a-8aa2-3a29-a2aa-714792fb34c8 | -3.2391 | -53.630798 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56901dd3-abbc-3b08-9b5c-ef343cd3f36e | -2.7551 | -45.951302 | 2024-12-01 00:34:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8989d985-2138-3846-85c0-de5dc038fe64 | -3.0358 | -50.2286 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ba3630-9ba7-392d-ae20-3d5022d133e6 | -6.9166 | -43.5448 | 2024-12-01 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 168fd609-c447-396c-bf53-7b619e595eb8 | -3.9471 | -48.168201 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d461e33-ea8c-3a23-b6a5-9aea3ca64672 | -3.2866 | -53.34 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f845c120-9d18-3c95-877b-e353190dacb4 | -5.9126 | -43.8377 | 2024-12-01 00:34:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f86caefe-b103-38f5-9146-48b9100de02d | -2.9282 | -51.9328 | 2024-12-01 00:34:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff89b39-099d-3694-bdd2-f9d434abf139 | -3.3236 | -50.180199 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b135fe6-df65-3ede-9e24-d3572620bee0 | -2.4685 | -50.362 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fea056fa-fb04-343d-98df-bc8baf8ba8d8 | -2.5422 | -45.611599 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53afe701-d469-3a1d-b6c2-9cdc5a2fa1d1 | -2.5897 | -53.981899 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21c7d593-cd75-3fe5-b560-e392588ea563 | -2.4281 | -48.7864 | 2024-12-01 00:34:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd57c44-aee6-3f4e-8f41-b88c70507202 | -2.8992 | -51.577499 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662657b6-d033-34fd-a3fb-b3da172b6898 | -3.7102 | -51.067699 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e31d81ca-c9e3-39b8-96b2-18cd5bb09a58 | -3.3034 | -53.826099 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 612ef17d-f98f-3141-9169-6fcb9e3b48eb | -3.0276 | -50.238098 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e986ae73-a927-33db-8be9-8b2bb5365f49 | -1.947 | -45.8466 | 2024-12-01 00:34:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e55a5f49-90b5-3174-9b04-24f7d1edcda8 | -3.4696 | -50.278801 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea992d10-8ec5-3ebb-bca0-e30121e10c98 | -3.4967 | -53.8195 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b05799-96ce-3b1a-9b15-797216045e49 | -3.116 | -51.307701 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f33be407-2550-3250-9a57-5167988721ac | -6.9285 | -43.551601 | 2024-12-01 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 103d8078-6846-3589-aeb8-5a86661b7c94 | -3.2924 | -47.025799 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579790dc-c16f-3bd2-ab73-b3948e68e0f7 | -3.0707 | -53.794701 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3a32cc-382f-3a94-9209-92b57721c759 | -3.311 | -53.860001 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51535e7-93d4-3fb4-adb2-37eaf9dd6959 | -1.445 | -47.112099 | 2024-12-01 00:34:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4fad19-ff6f-3295-a445-8ef53bca1649 | -3.2611 | -53.637501 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
