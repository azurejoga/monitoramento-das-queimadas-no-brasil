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
| 3f97852c-2340-3304-bda2-d59dce475827 | -11.5618 | -47.44995 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bb8e02b-7c64-31fc-bb5e-ab1db8cd3fb9 | -11.55724 | -47.45674 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d3db7d9-f4b9-30ef-9025-3d6610dcb510 | -11.42868 | -47.29966 | 2024-09-28 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6984a53-bb87-37d0-8036-7f86a3c14d81 | -11.37283 | -47.57773 | 2024-09-28 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 617a2b21-95b4-366f-933e-9821ba28e519 | -11.32238 | -46.88516 | 2024-09-28 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e23c7261-e7f4-381b-832f-65104ed0c3e0 | -11.31905 | -46.88461 | 2024-09-28 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b986563-eb51-3bd5-a2a9-46721ea5e7b1 | -11.10929 | -46.17142 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e0e4d62-c145-3561-86be-8124238db1e1 | -11.10599 | -46.17088 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ad7b5f6-dea5-32b0-8238-45efb979e9e2 | -11.08456 | -46.13508 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a83673f9-5f0e-3ac5-a1c6-8ab2483d3a64 | -11.08181 | -46.13104 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 368b2d5a-fc0c-30c7-a5cf-8c1b7f9d26fa | -11.08125 | -46.13453 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe9ed6f3-98be-3728-b0f9-5d6ccf2861aa | -11.07851 | -46.13049 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b79db1d-af60-35f3-9a16-e7cea044fc10 | -11.07521 | -46.12996 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8369aae2-3e91-3aed-b885-ef268f6cec8d | -11.05042 | -46.13672 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7b61817-ce34-32da-a685-1d11d7d15f8c | -12.26346 | -47.67612 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aabc060-8309-3cfd-abb1-45f595a7a346 | -12.26128 | -47.66815 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2292a19-8c28-3be2-aef6-db1b56611a5c | -12.98003 | -47.20441 | 2024-09-28 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c8f63e2-1bbf-390e-841e-87afaffd237f | -12.80209 | -47.46067 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 99dbf7d6-767b-3cd6-a6d5-2a8032e777f5 | -15.20302 | -47.39729 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6154a36d-5b7c-37e1-ab7f-6c905a00954b | -14.60202 | -48.14479 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1449f082-56e5-3d5e-b4e5-86d22bc70bd1 | -14.59527 | -48.14362 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 975b3946-2918-36d6-8a9d-c34a527c41f1 | -14.59189 | -48.14308 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28396827-09a8-37b8-977f-9b162c9ac5a0 | -14.59008 | -48.15415 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43fff002-9f10-3516-9354-adbd7bdcba36 | -14.58885 | -48.16166 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a574781-dbe1-3c09-b95c-2205d721045f | -14.58729 | -48.14995 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc303435-dec1-3338-8295-5c9d8c0fb94b | -14.58547 | -48.16111 | 2024-09-28 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6a733d8-66d2-3a8e-954a-50043e44c7d2 | -13.90428 | -47.25912 | 2024-09-28 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6b6c17b-8664-37ad-bb19-e755bf32a635 | -16.30883 | -48.78097 | 2024-09-28 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eeecc75-1435-3534-af84-362483e0c8f1 | -16.14585 | -48.61656 | 2024-09-28 04:21:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dd01056-e5ec-3ce1-8e1f-151c95ce5e2b | -15.92853 | -47.37283 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6240f7c1-0552-3bbe-a2c1-2f7d4f633a4c | -15.92796 | -47.3764 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e6b1b20-a86e-3fcc-b04f-b73610cc918e | -15.92522 | -47.37226 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99e76279-943c-33d2-a655-ce1c4e96b0fd | -15.68541 | -47.63766 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15209cbf-f240-3305-a955-7c4dd414b333 | -15.63054 | -47.23432 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93c59586-16c3-3342-86a1-02f2aa5e0f29 | -15.62997 | -47.23788 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3457f5b5-c745-3a04-8491-859b86cdead8 | -15.62724 | -47.23377 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 149f1219-d881-34a3-9bc1-13437e7f7036 | -15.62449 | -47.22965 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f96ddb7-b4fc-3c11-921a-8dcf010a3b68 | -15.62119 | -47.22909 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dacfe7a0-644b-3eef-adf8-5b245a5ec288 | -15.61789 | -47.22854 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7be0bb4-caa5-354c-8a8d-2fcb64d95cc5 | -15.61732 | -47.23211 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e853c63b-19cc-3a24-8ef8-994da276969e | -15.61493 | -47.58842 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b015bd27-2b80-3d49-8abb-17e4485e054b | -15.61468 | -47.82246 | 2024-09-28 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0d9c5c9-2635-3f98-9ce4-2885a14511dc | -15.48515 | -48.03342 | 2024-09-28 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dceb774-e73a-3a5b-ad92-1e260d99a22a | -15.48456 | -48.03708 | 2024-09-28 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 86ea65d1-1dea-3baf-a7fb-eddb8b841d14 | -15.48299 | -48.02554 | 2024-09-28 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6e27a4c-6919-3d32-a236-88e74057fc9e | -15.4824 | -48.0292 | 2024-09-28 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1625453d-07b3-3ae0-b889-09b35416a8fc | -15.41518 | -47.45447 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6045f401-553f-37ce-a02d-372f7e7e1060 | -15.41244 | -47.45034 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 791cda61-c590-3a75-9edf-be34dc18ecc3 | -15.41187 | -47.45391 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a0e9cb9f-e55b-34d3-bba6-b45c79c879da | -15.40855 | -47.45337 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| adca02e9-954e-3ebe-91fe-b6ad241f1db1 | -15.40581 | -47.44924 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9bde655-0c64-3c3b-a413-7b78f85575e3 | -15.40523 | -47.45282 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d119576a-f732-3cb8-a27d-10a389e0a835 | -15.38954 | -47.46516 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e4b4257-8ed1-396b-984e-587c9b77e041 | -15.38896 | -47.46876 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13193ad2-2306-3693-829b-7bf835aa1389 | -15.38565 | -47.4682 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72e6942e-cfeb-3244-9c92-687f1747eb2a | -15.37959 | -47.46352 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40a3314c-0c05-3a40-bffc-48f6b1b0302d | -15.37627 | -47.46297 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06a2d698-99d7-3745-958a-5c90d83bd39f | -15.37467 | -47.45171 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d899ebc0-1530-3993-a43d-f203d9c18a47 | -15.3741 | -47.45529 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7512f885-d01e-3cfe-a5e4-819d11805b6c | -15.37353 | -47.45886 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fb5bbbf-fc62-31ef-b744-db31e158fd53 | -15.3686 | -47.44715 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dae3b222-034d-3819-86ab-299c7c2b9eab | -15.36802 | -47.45071 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9d4db67-1e3c-34e6-b7e7-1281d8cf2614 | -15.36746 | -47.45426 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad5104bf-64f6-3c3c-a194-ed3c9d287db0 | -15.31815 | -47.46442 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67472b85-222c-382e-a7b4-d590023bddf0 | -15.31759 | -47.46793 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f82dd492-869f-3433-b220-c1dd0aa5a248 | -15.31385 | -48.01495 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7746077-494c-319e-8a87-fe0979c3fd5b | -15.31289 | -47.99978 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4538f284-ad72-3519-b8eb-14d6121312fb | -15.3126 | -47.47792 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 447cc740-81f8-34d5-9055-818e6c633b91 | -15.31229 | -48.00344 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e95ac38-728b-3d45-830c-c6751d8aaed0 | -15.3117 | -48.00708 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b660a63-a90c-3bc8-b9ef-8e4c47b2def8 | -15.31052 | -47.9997 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f4140af-8b3e-3257-baa9-d4c489f14c5f | -15.31038 | -47.4704 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 041beae2-7350-3c99-a55d-7c0b9bd76daf | -15.30993 | -48.00337 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4285999f-1a82-36cd-ae6c-9d5ce85d6f2f | -15.30983 | -47.4739 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbffda15-ad17-34b8-ae3f-f7d66d7bcc6e | -15.30934 | -48.00701 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c3a3555-2453-3134-8398-3e14d0b181f0 | -15.26414 | -48.29538 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 42e72744-5c16-3e51-a7f6-aa6d18987de0 | -15.26317 | -48.2918 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 116b7c73-6e34-3dfd-a22c-1d3747ef91d9 | -15.26256 | -48.29553 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 32d3ba6b-79aa-3f4b-9d7b-a45899a12ce0 | -15.25919 | -48.29494 | 2024-09-28 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ebf54eb5-38a4-3d93-904f-2baa86b896d3 | -13.45767 | -48.58392 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfa94ef3-42c0-3124-b94b-83bc2cdde481 | -9.27817 | -48.20506 | 2024-09-28 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48f9c7f6-d024-3ba5-ac79-387bd6800344 | -9.16723 | -47.60349 | 2024-09-28 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7625a01-0be4-3066-8587-cb6440188b10 | -9.16504 | -47.60301 | 2024-09-28 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8583bedf-332a-3973-8460-32c07a2919e4 | -9.92358 | -48.23209 | 2024-09-28 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ecff5fc-39ba-3d54-a9fb-1fd0cd66c888 | -9.53553 | -47.78563 | 2024-09-28 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49e53fa6-3dc1-3321-8640-97d0edaef6a6 | -9.53489 | -47.78954 | 2024-09-28 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9d0b145-0866-39db-91db-9c1d32d33dee | -10.75869 | -48.56208 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f812634-3f78-377a-a5a5-8dd76966fbe8 | -10.72529 | -48.75959 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef88a93f-5356-345b-b8b4-d5b050ef1af6 | -10.71372 | -48.75029 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27055666-d423-3976-a7e4-31a0cafdfaee | -10.70027 | -48.5655 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86ea8f5c-f05a-3185-aaa7-c2f63b53c9fe | -10.68224 | -47.95011 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f881b7b8-0881-362d-92a4-d694ffb48fcd | -10.67876 | -47.94962 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eedfd8fc-bc7b-3c61-90ef-8527c78bb5ad | -10.54864 | -48.05646 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8190330e-ba94-3d24-b49c-4c4951e05c16 | -10.54799 | -48.06035 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb4d5ed5-35a4-3ccc-b66a-f7b009774874 | -10.54583 | -48.05183 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19b4c657-e1ab-374f-bbfc-a41f859cb856 | -10.5452 | -48.05564 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c8ca55e0-c69f-34aa-8441-5375f6f78415 | -10.54301 | -48.04731 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35d3e1b6-7c2e-38d9-bc32-6d38e938f748 | -10.54239 | -48.05105 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83afcd54-d958-3e4b-a805-de3847c43bba | -10.5402 | -48.04271 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b81a3f12-8aa0-3fa8-bf35-ed6cdd4f7bbb | -10.53957 | -48.04651 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README53.md)
