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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16a6ea87-c040-34f0-8d2f-ef81ddd22426 | -20.04902 | -46.16202 | 2025-09-16 04:32:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19d43ca1-eac7-3f89-88cd-f7bb0c10cf44 | -16.68434 | -49.76289 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6687ff1-4c90-3da7-93c2-cc256cbfec2f | -17.83361 | -50.4207 | 2025-09-16 04:32:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed0c9758-0ef2-38ee-8d9c-aa96fd1ef355 | -16.58504 | -42.91004 | 2025-09-16 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b45dbada-4ceb-3a80-b213-ba6e554d0a32 | -14.52922 | -47.39006 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfcfb88c-bd01-32f3-932f-b09a5d3f9520 | -14.52811 | -47.39723 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c6a6002-07df-3a71-9a62-6d0094bebad1 | -16.02788 | -59.4561 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35cd0d55-560b-37a5-b21e-1df869f5d9ed | -14.51139 | -47.37243 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6892b9e-a0d4-3108-8edf-7fb1e71c38ab | -20.3474 | -48.78413 | 2025-09-16 04:32:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51740df5-5acf-3eb6-878f-26578bf66f6b | -14.60089 | -46.32809 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45374fd0-5d06-3bfd-85b9-3e18c3d43641 | -15.84351 | -42.68341 | 2025-09-16 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2b208f6-269f-3c26-91a0-0d4a1d1943ee | -17.32938 | -46.80074 | 2025-09-16 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0144cf4-85dc-371e-8de9-fb629ec7f3d3 | -16.01039 | -59.45245 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45be2f10-a721-30c4-98d6-7f7b907aa086 | -15.80147 | -53.4826 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ac9978e-5fd6-3c37-a9f2-239931fb2a83 | -14.52198 | -47.39256 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b98bf3d7-dea6-3a12-878b-f51b7528e1cd | -20.34683 | -48.78786 | 2025-09-16 04:32:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5518b54e-318d-37a5-af97-5139f71771d9 | -19.00924 | -49.9311 | 2025-09-16 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3651f43f-a925-30b8-afcb-1902f6cb3688 | -20.41366 | -45.51406 | 2025-09-16 04:32:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25c97470-e671-3a4d-8ae9-08ed2faaae62 | -14.92125 | -51.65306 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c73f79fa-a4bc-3a0c-9cdc-cca0ad033733 | -14.64719 | -42.71173 | 2025-09-16 04:32:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 42f9a9cf-e0cc-3a47-a8de-5ad0d3f30c4e | -15.46539 | -47.31589 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36d064a4-6066-3335-b692-57a02002d8b2 | -14.5254 | -47.34851 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51f13fd7-bfcc-353b-9317-6990cc4be05b | -15.80136 | -53.46077 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b8eef03-beca-3385-84bc-d5b5a8f904aa | -14.79879 | -51.67523 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a14c576e-4844-3088-9b37-6c1153eeb51e | -14.80472 | -51.66267 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf543015-cc59-35ef-be16-6a9e73420cf5 | -14.63857 | -46.38103 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 587a644b-7160-3b17-bf87-73cfd39b5669 | -16.715 | -54.9476 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5a86787-6000-3d22-b047-d5a642c06cf3 | -14.96939 | -46.56619 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6333f3c-aa1b-30cc-84b9-29f40e190143 | -14.82603 | -51.66483 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e96351c8-1a25-310c-9e6d-c1ae76208853 | -19.15664 | -48.72874 | 2025-09-16 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 58095fbc-fdd5-37dc-bc78-8abe6a75f224 | -20.96651 | -44.50299 | 2025-09-16 04:32:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc03fce3-f419-3bb1-a9ba-dd6c19404529 | -14.39037 | -52.8924 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77318e5b-eecc-3ca0-953a-ef5b8c64d5ef | -16.06533 | -59.42325 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 112b32d4-7796-3b1e-8d48-ed526927004f | -21.17801 | -47.58639 | 2025-09-16 04:32:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 760bcaa9-9565-351f-b5c7-c6eecae7db64 | -20.53796 | -45.61509 | 2025-09-16 04:32:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f7c664-b20f-38a8-87c0-d0e901cd852d | -16.70641 | -54.94564 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 913e91ea-e36a-3eb1-a068-ae7df1ecc5d4 | -13.75727 | -48.76266 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 646acc80-e382-3ff2-9aff-a7c244b65d76 | -19.56512 | -49.44256 | 2025-09-16 04:32:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 564d4f17-5003-315a-b3a0-95042b0cf0eb | -16.67484 | -49.75748 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c852cfc9-7985-389e-b469-2d82bb10aef0 | -16.67792 | -49.7809 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59173b87-36ef-37e2-8e49-776393ee31ab | -14.53153 | -47.35322 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d086e948-7c24-3711-99fa-3be20489b761 | -14.30376 | -49.53321 | 2025-09-16 04:32:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fdc23c2-3929-3fa6-a6df-c131696b5f96 | -20.86136 | -46.21234 | 2025-09-16 04:32:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d26c8994-7943-3c05-b026-c92d12df337f | -20.12729 | -49.10806 | 2025-09-16 04:32:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7db280e5-5a11-3af2-ade6-da33b555fe1e | -16.68986 | -49.77143 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09437ff7-298e-30d0-acec-8e91b38494b6 | -15.40452 | -41.7117 | 2025-09-16 04:32:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f3fb746-88e0-31b0-96dd-14448f1bddb9 | -16.68801 | -49.78269 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e7180d1-9868-3c4f-a455-37e0028c2e15 | -13.78186 | -54.94976 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7267803-2142-3556-934d-a7db135ad690 | -20.43961 | -47.13127 | 2025-09-16 04:32:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e4aef5-3437-3662-9e03-8781fdea16ab | -14.63915 | -46.37717 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 054ba638-42dd-3514-8604-ace8af597b5b | -14.61007 | -46.38416 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 989de6d7-01fb-3773-83a0-3ebee2405718 | -15.9915 | -59.26435 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa286e1-24ab-375f-b432-fe76d93dc659 | -16.02524 | -59.24701 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 480545e3-71c3-3c0f-8628-24d04daf2e06 | -14.51083 | -47.37603 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9f5dde-648d-3c96-b1a0-473bf1568e70 | -14.50971 | -47.38321 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cde8a89d-61f0-3091-b2fa-6c7557a4949f | -16.70623 | -54.94343 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c160ef45-1312-36d7-a6b1-76b8a92e166d | -14.8106 | -51.66654 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fff97804-ce34-333a-892b-905d4bad3e36 | -14.80771 | -51.66146 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcab2f59-1347-35c3-8242-06c361036e0f | -15.7242 | -39.32564 | 2025-09-16 04:32:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 40d1bdd8-1daa-34bf-9c73-9ed1c2c143f4 | -14.81426 | -51.66721 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63a4d39a-0ef3-3e1a-9f5d-c3f0ecd68172 | -21.15811 | -44.32056 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4373af06-7964-3e8a-94f3-2b899d7aa2e9 | -14.8773 | -51.67425 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8e7c1bc-3d3f-3884-8b5c-8a292a77f76b | -14.51027 | -47.37963 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea130ad-c647-3282-aaca-4b725801305a | -15.77854 | -53.44313 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83f0c765-331e-3a5b-ab8d-a2f7d17dc3c9 | -16.65344 | -49.76138 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ed8f456-ea87-3aee-94d0-2eb26a73d487 | -16.48041 | -55.11018 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| d0d8a374-24b1-34d7-88ba-995f8df3c4f2 | -18.15831 | -49.20077 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 264e6051-684c-3543-9601-bb74335ab210 | -15.95828 | -46.98494 | 2025-09-16 04:32:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71ec6be7-3fbe-3c2b-9151-346e5a2309ba | -13.28318 | -54.245 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bf5e9c1-7f57-30fa-af52-8922d4b009cb | -20.56451 | -46.3737 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64b6da5a-1c7d-3cef-b7e4-85f726288595 | -15.40885 | -47.34027 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 430b127a-f64f-3e2d-96ee-4deea77cb019 | -14.79955 | -51.67081 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b3ce28-83c9-3748-997a-71e7c866d0b2 | -21.23208 | -45.01265 | 2025-09-16 04:32:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a8ea627-770d-3c07-b61e-09df57f51552 | -13.76119 | -48.75967 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8289746-e95c-3ce8-97f9-79d97c1758f1 | -18.56774 | -43.57404 | 2025-09-16 04:32:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32636fea-8f35-3038-ac33-94b242f21f9d | -16.00724 | -59.24685 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25efa7c7-4c8a-3cfa-a527-789ffd5ff538 | -14.96652 | -46.56207 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78b91891-723e-348d-8e40-c5b84ccaddb3 | -18.90134 | -49.57645 | 2025-09-16 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de0a320d-c0c5-397f-ba83-964d3a9b1eda | -14.53033 | -47.38289 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4c0a5c0-52eb-38b6-954b-8afe10a10296 | -16.68465 | -49.78208 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8760c664-2827-3897-99de-fa926e035322 | -18.16047 | -49.20864 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 600502ff-0bcf-3ecb-bae9-eddf871a1c0c | -15.78834 | -53.44178 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f0b955f-2c49-3bb7-8e3d-67959d6a5b27 | -15.88221 | -59.41304 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 406e91b0-8cfc-3ea7-b672-5739254bbe47 | -16.00637 | -59.45241 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cabdea86-4c56-3301-b5ab-faacaf2706a5 | -17.72715 | -46.77713 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb5facc2-956f-3a19-b2a4-dca86f08a72d | -14.52256 | -47.36673 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 998c83ec-5051-3bed-a3c3-4b1274f41add | -18.55974 | -49.25867 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.0 |
| b632b886-1162-3f0b-b786-4ef81f3c7dcd | -15.9923 | -59.26059 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb372561-4152-348b-88ec-238e219f1d93 | -21.20124 | -44.37293 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e9f9f49d-e9b1-3742-95cb-637814c0d7c0 | -16.69534 | -49.78024 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4483e950-6cc5-3c95-859e-4b832e3d66ba | -16.05012 | -59.43756 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cdc81d5-b54e-3f1b-ab5e-26df3ae014b9 | -16.47959 | -55.11446 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| f540850f-e4e3-3bfd-937d-d96f7c731536 | -14.60268 | -46.38673 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 199d5049-ac25-3156-9147-d1076a975a3f | -16.01397 | -45.1368 | 2025-09-16 04:32:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 696126ba-8a3a-3353-a898-59d2963cdffb | -14.38735 | -52.89513 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 941271be-7746-3a6d-9efc-1dd9b39b6e72 | -15.9981 | -59.26162 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6fb8aee-53b9-3330-99a6-05dcfa6067ba | -16.42856 | -45.67255 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6ccc2e1-be2c-36fd-9592-40402c3c49b7 | -15.88131 | -42.7193 | 2025-09-16 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e270d0a8-b9ee-355e-8f56-f8020301b4d3 | -17.73583 | -46.76633 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3da2f4f-a5ee-3a26-94f1-601491e52b11 | -15.86753 | -59.39609 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README59.md)
