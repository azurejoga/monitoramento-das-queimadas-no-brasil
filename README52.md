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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871da104-1bef-3867-a712-4d65a93ef474 | -15.22445 | -46.18631 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b8ec863-c236-3aeb-924d-6dae0b5ca610 | -15.63321 | -52.68895 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49329d73-194b-377c-b415-b97a9315c5c4 | -14.63335 | -52.13717 | 2026-09-29 04:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78f5bb77-e533-3e93-85f3-120e7aaf522e | -15.45361 | -46.13813 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de5bb9fa-05a4-3840-8e0b-6c95b369f6dd | -15.24705 | -43.27869 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.7 |
| eaf71248-991f-3b15-b1cd-62758e3335a3 | -15.0118 | -51.4077 | 2026-09-29 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa79f7e-0ea1-3349-95c4-2a131ee0a388 | -14.50959 | -52.48313 | 2026-09-29 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fa5cbed-4324-3d8f-afd9-46884d442a8e | -16.3818 | -46.90283 | 2026-09-29 04:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8395b4dc-e443-3270-a478-f10f7c6b2755 | -14.80045 | -45.96139 | 2026-09-29 04:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74980ec3-9a92-32fa-a3f6-a5b0f32f96a8 | -14.95883 | -47.5409 | 2026-09-29 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 073e4b15-6ffc-3ce8-a4e2-263b7c875b76 | -15.04799 | -48.56921 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd5e3496-c940-3e13-b238-f4006b1a8f72 | -16.35115 | -42.58469 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75246f58-7321-3841-9b2a-5e85d1e9d3af | -15.46687 | -46.13293 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24d66712-99c5-3fdd-802c-ac98c83cad2c | -15.73355 | -46.02698 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6da80452-4019-34b3-9619-c180279da2db | -14.96332 | -47.53624 | 2026-09-29 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac7157d-b611-36e1-a8bb-8b420041e9fd | -16.34702 | -42.57418 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40335d58-7ce1-32be-b953-bc82c18d8bfa | -15.39692 | -47.92443 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdab897d-7cf8-3267-8864-b8b58181f07e | -14.63394 | -52.13355 | 2026-09-29 04:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42baed06-e1e3-3ca9-b3e3-b5efca81ff2c | -14.22182 | -48.51013 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5e53597-1e5e-3ca4-b05b-af0523711a82 | -16.34666 | -42.57733 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07514c92-3fb5-33ed-a3cb-e81f572ee528 | -16.06275 | -47.91546 | 2026-09-29 04:53:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e153e00-b4ff-3e01-a6d9-8c6fcd20462c | -15.24769 | -43.26656 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 50.2 |
| b37c0047-be1d-3b27-ac39-711481e215f7 | -15.22128 | -46.17891 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4bf2114-22f7-3a90-8edd-0df8193fe366 | -18.56941 | -48.42058 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 08865ead-22ff-3988-a565-69679db77a16 | -15.00903 | -51.40355 | 2026-09-29 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11b2ea47-2386-3fc4-9798-d738143a4666 | -14.54295 | -48.3113 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6ff2bf4-0f3a-3f30-97f5-ea3d57ccaec8 | -15.1759 | -46.12432 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c48bc58-9523-3822-b3a3-70296deb8596 | -15.44904 | -46.14101 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 830ea0f0-1446-3d97-9d0f-bd240a281c91 | -18.87174 | -46.66681 | 2026-09-29 04:53:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ba97678-14b1-3c8c-aaa2-1a4928c2d365 | -15.38011 | -47.92408 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35b35cf-2f4f-3df4-9aab-fb78fa7a7a1d | -15.00067 | -47.86852 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aecc442c-0046-309f-a56d-94dc7099f8b2 | -15.08726 | -48.32667 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f9ef1b-209f-346e-951e-2f3e7205c4b8 | -13.88718 | -53.67967 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afd56c4a-ec5d-32b5-9d38-8184bc387ad7 | -15.16841 | -48.67926 | 2026-09-29 04:53:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4bacfee-0f50-3465-ab37-29cdf620169c | -18.40504 | -42.31044 | 2026-09-29 04:53:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b784324a-3741-36d0-a76c-72f2ab5fb500 | -14.81876 | -47.28433 | 2026-09-29 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e440f633-29eb-3136-a883-015147df077d | -15.64453 | -52.6833 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32eb5996-3eba-31a4-ad8c-43153ea9a5ba | -15.33958 | -48.1255 | 2026-09-29 04:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 798d71de-bc0d-3398-8dd9-33f5e1859db5 | -15.08302 | -48.33039 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55c7e87b-daae-3482-bc1c-ead13c5d5ec4 | -18.76473 | -47.6174 | 2026-09-29 04:53:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 623560eb-7e02-3ab7-92fb-7fbff90a943c | -15.17084 | -46.13078 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cb6a506-d8f8-3e3b-8142-a535030603b3 | -14.50944 | -48.31466 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11b79034-89f6-3ffd-b9e2-c7e14e7392c2 | -14.79884 | -45.95842 | 2026-09-29 04:53:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34aa8129-a758-3bcc-a2cf-43499e8aa0df | -15.44953 | -46.13737 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ec34ca1-6697-34cc-981b-40cf25f1bd72 | -14.86473 | -47.99012 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44bad327-116d-35ea-8fef-5815f97cf2ec | -15.25192 | -43.273 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 50.2 |
| 6a4d2805-ec82-3c8f-b73c-9c6d1c4342c2 | -15.1754 | -46.12793 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a4ad106-d101-344a-8f1b-cf6d8462dcb9 | -14.52747 | -48.29169 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eda827e9-88f1-3bb7-ba14-1cfa97119ffb | -14.51124 | -48.30229 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2178395c-6bbc-3dab-878e-16b7204038a0 | -15.17353 | -46.17216 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f19e194-1865-374e-b6c8-48b33a589c7d | -17.97723 | -44.49041 | 2026-09-29 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa8fbca6-eb5b-368d-b8e7-acf3fdc4f0fd | -15.24772 | -43.27298 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.7 |
| f4de7fe3-bf7a-3f8c-870a-e6f6cde08782 | -15.38774 | -47.9091 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba549ff-b131-358a-8242-e293d493dd89 | -18.68335 | -48.62365 | 2026-09-29 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a37b4c1-dd1d-3308-b0b0-ab53ed8db39a | -15.38838 | -47.9045 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eacdde5-c8f7-3d88-afeb-23aca285c14b | -15.17761 | -46.17273 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 430639da-7595-3473-8404-9e5b383b9602 | -18.90877 | -46.85188 | 2026-09-29 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 146f3f23-9743-3096-9109-034b5f43dc39 | -17.60996 | -43.71544 | 2026-09-29 04:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54aff70c-196a-3234-abb0-ce4657ac48f5 | -16.19538 | -42.87858 | 2026-09-29 04:53:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9321a4a-ded6-3f73-9df2-df6ebc4b219d | -16.22916 | -48.06372 | 2026-09-29 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d78cb2d-48f9-31a7-b96c-269c44bcf5fb | -15.38216 | -47.92207 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a3ae0d1-9109-3898-a9b6-c27215148566 | -15.8397 | -49.17261 | 2026-09-29 04:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c02c3d2-d725-3486-a079-9f70ecdc972d | -15.35038 | -59.14761 | 2026-09-29 04:53:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54528a61-58ce-3a44-81cc-4f662abfca5f | -18.67965 | -48.62307 | 2026-09-29 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25a1c4fd-c030-33fd-ab12-1a1d1b527579 | -15.22593 | -46.17525 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4252a2d5-34e0-334f-9eae-14f657754907 | -15.24208 | -43.27803 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.7 |
| cf933ad4-c6ff-3cb2-b0eb-8b71493a0313 | -15.00436 | -47.86902 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 044670fd-49cb-38e8-8682-092d329e9e41 | -15.19175 | -46.13049 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23385151-dae0-3728-8be0-8320e9d5268b | -15.21407 | -46.17049 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4370338-87d6-390b-9810-d0f83a0c19c1 | -15.20997 | -46.16998 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deab1f98-301c-3c3f-b1c5-ee15b2b42924 | -15.4587 | -46.13137 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c419af02-2695-3989-9ac5-e57db6462cee | -15.38523 | -47.92704 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56f0c9ea-bc79-3f33-acd3-1a61e03dc096 | -15.24345 | -43.26648 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| f68d0719-fc82-3daa-9867-dc080f02ec4a | -14.50766 | -48.30168 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdd55304-f38e-34dc-90e5-906a4853d39b | -19.53618 | -42.93148 | 2026-09-29 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3491ba7e-f51c-38f1-8492-0fe4ddb61ec6 | -14.51248 | -48.29377 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f066d5a-80b2-3aeb-93c4-211d9089e65f | -14.8641 | -47.99459 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9daed80d-5e01-3ecb-8a1f-6834171f44eb | -15.38278 | -47.9176 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c7959b0-f91d-3b4b-95ad-1e7125cee524 | -13.58472 | -51.4456 | 2026-09-29 04:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a6cab6b-5d94-3ad7-baf7-07de9f332363 | -18.90827 | -46.85578 | 2026-09-29 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b2912ef-4766-3fc4-8383-666284b3f72a | -18.57378 | -48.41649 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 09b54f0f-6948-3a34-aa2a-331c90f252a7 | -18.16354 | -48.0167 | 2026-09-29 04:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb8b05e1-cf3c-32b9-81e0-72154f9acda9 | -20.21617 | -48.55996 | 2026-09-29 04:53:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e3996dc-9329-32c9-acdf-af9b95302b26 | -15.6326 | -52.69264 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8508dac3-41bd-3cea-90b3-689179b6b781 | -14.95955 | -47.5358 | 2026-09-29 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4b975d5-6277-3b76-a371-f879d2ec3d7f | -15.45819 | -46.13523 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3290e83e-0c2f-3930-ac01-72edd89530fd | -15.24128 | -43.27741 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 90.4 |
| b5644381-a6dc-366f-839b-1ebccddbeb28 | -15.09787 | -53.87157 | 2026-09-29 04:53:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 330b57ab-c6d3-3502-9cf9-648329866ff7 | -14.49931 | -59.74767 | 2026-09-29 04:53:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2ae77b0-bbca-3356-9e83-28328bb82ed1 | -15.95776 | -42.96078 | 2026-09-29 04:53:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55089a7f-d2a0-3d20-8cf3-52d8ac37d3ff | -18.40467 | -42.31378 | 2026-09-29 04:53:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eaff5586-fde2-3501-9c5f-2be5d7d28e6d | -14.21924 | -48.51124 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 980b3b75-fc84-38f3-9549-04b24844af8f | -18.8759 | -46.66741 | 2026-09-29 04:53:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7134e623-89c9-3a52-aa60-7f02902130b8 | -14.52308 | -52.48542 | 2026-09-29 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81f2d4d6-ae3f-388d-8566-985325b238d6 | -15.93971 | -42.33565 | 2026-09-29 04:53:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 268ad2d0-97a9-34b0-9a26-f7863129fddb | -14.52032 | -52.48117 | 2026-09-29 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2505aeb2-228c-30d2-a88b-2121342e0a7f | -15.46132 | -46.14312 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f68bef32-1382-3942-8fae-75c735a611cb | -18.57315 | -48.42113 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ae27b03e-b3fc-3822-a43c-b22bc27af5e8 | -14.52683 | -48.29602 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca2d7c6d-3bf1-3558-ae9d-66fff899de53 | -23.00659 | -48.61932 | 2026-09-29 04:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README53.md)
