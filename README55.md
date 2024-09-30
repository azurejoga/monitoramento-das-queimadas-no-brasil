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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09c4365d-74d9-3b7d-a369-fe3fa5e46875 | -19.35898 | -48.90133 | 2024-09-30 04:34:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edd61083-5fcb-3bec-b0e0-57c9f76a9fa1 | -19.35558 | -48.90075 | 2024-09-30 04:34:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e5006bbe-50ea-3871-b22b-6579556ba38b | -19.31827 | -49.37101 | 2024-09-30 04:34:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1995fca-9826-3a69-9fe1-4d6079cb40e7 | -18.7975 | -48.05035 | 2024-09-30 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7513dfc1-2eb6-3c87-b0d9-200df5bc017e | -20.82823 | -49.51508 | 2024-09-30 04:34:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3977db97-d6fe-354b-9c2d-3f34a965382a | -20.63523 | -48.74774 | 2024-09-30 04:34:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| eef09e5f-7b56-3853-b349-a476aa278604 | -20.63465 | -48.75182 | 2024-09-30 04:34:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0e7189ca-b06d-3907-a818-807799d53b4b | -22.24873 | -49.66979 | 2024-09-30 04:34:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c95fe51-3338-3230-a42d-34f70eb57ab6 | -22.24816 | -49.67371 | 2024-09-30 04:34:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f7497c98-ec09-3a0e-9c52-33457e78b24a | -22.24533 | -49.6692 | 2024-09-30 04:34:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 899bcc29-962f-37d2-ae49-8cba7c46bf3e | -22.24476 | -49.67312 | 2024-09-30 04:34:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 927d932c-dea3-3ca9-9280-f3cee4ee31dc | -22.24419 | -49.67704 | 2024-09-30 04:34:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 44480d02-d88a-3211-bb98-0a2e7e24003a | -21.37135 | -48.48804 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd274972-6999-3d55-af84-60d18f368844 | -21.37076 | -48.4922 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52031db0-04e5-3818-ab52-837e54398655 | -21.37017 | -48.49635 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1b4e57bd-9f1b-3110-bd5c-ea4d5ead6747 | -21.36723 | -48.49168 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f7e2de2-ef32-3eae-8ec3-e85ed846d1c4 | -21.36664 | -48.49586 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd2997a8-2bba-32a5-93fc-781064a60363 | -21.36605 | -48.50005 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fff9da33-19cd-3601-b122-64ebdeec49c3 | -21.36546 | -48.50423 | 2024-09-30 04:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 48add938-b0ed-355b-abed-7e73b4a91a61 | -21.49767 | -49.831 | 2024-09-30 04:34:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| 1d812ba1-6924-38be-ae65-2559736d42dc | -21.31643 | -49.42565 | 2024-09-30 04:34:00 | NOAA-20 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4ba4cfad-44d1-379c-849a-7a0e14f27d0b | -21.09274 | -49.13638 | 2024-09-30 04:34:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfd9711b-95a3-3f9b-be13-63092f2bb1d7 | -22.5408 | -48.81215 | 2024-09-30 04:34:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a189b58-9e23-3b1d-9781-647b3b78498b | -15.07731 | -48.94451 | 2024-09-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83722720-9f86-335a-88fd-a5c54ea3cd14 | -16.47062 | -49.9413 | 2024-09-30 04:34:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4ce81f4-cfee-3130-8541-03ffc7fe37d1 | -16.14774 | -48.90789 | 2024-09-30 04:34:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae2714ab-008e-3a78-bfee-a8c65a2a5612 | -17.86705 | -49.91012 | 2024-09-30 04:34:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df204302-4149-3061-b007-1116eb1a7d49 | -17.86649 | -49.91374 | 2024-09-30 04:34:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce81f50c-e38e-3390-b2be-f19dde43ce70 | -17.86373 | -49.90956 | 2024-09-30 04:34:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83460729-204f-36a4-b35c-7f0b8cee69ee | -17.86317 | -49.91318 | 2024-09-30 04:34:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cdb5e3f-8537-3487-800e-c3422bbdf949 | -17.12687 | -49.86907 | 2024-09-30 04:34:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e603241-6556-3c4a-9333-1cff45dc6d14 | -17.00827 | -49.77946 | 2024-09-30 04:34:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2770cb6c-7f56-3d16-ac99-b3b88097f645 | -16.72537 | -49.17202 | 2024-09-30 04:34:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73224d81-d6cd-3bb1-8c54-911a108b89c2 | -16.69971 | -49.2948 | 2024-09-30 04:34:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a9ddc4d-b47b-3cfc-bc8f-3b9b9a5469a5 | -18.4654 | -50.16616 | 2024-09-30 04:34:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4c99c1fa-b5fc-36e0-ba5e-cf384eb0633c | -18.46209 | -50.16559 | 2024-09-30 04:34:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc9c5b0b-9962-3083-9343-9e7d5ff1eb81 | -18.45877 | -50.16502 | 2024-09-30 04:34:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6c59f76-2b36-3e0d-b8b0-647584a50356 | -18.45602 | -50.16082 | 2024-09-30 04:34:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 57d28407-3175-39af-b2a5-8c2d64be8ab7 | -20.4246 | -49.77771 | 2024-09-30 04:34:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ce49cf-bc85-3253-a137-0a1ad2ab4db4 | -20.42125 | -49.77715 | 2024-09-30 04:34:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61ee3fde-d4e6-380e-84d5-fe668f2521f0 | -20.8459 | -50.41835 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5eed35b0-15f0-387b-8418-8edba4e04e42 | -20.84257 | -50.41779 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6c24dd1-0ed4-33c6-b517-2fee2acb26d2 | -20.842 | -50.4215 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec5cf386-5678-3e6c-a7a1-3f8dd8837f9a | -20.53103 | -50.41526 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47c3de45-c9b8-30c6-96a6-5a578714ae02 | -20.53046 | -50.41895 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 07f0d7e8-a765-3a77-8a2c-21cede923661 | -20.5277 | -50.41469 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9dbcef4f-1d5d-3260-aa2b-73908ba10485 | -20.52714 | -50.41838 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e41417e-1df0-365e-ba16-6f1964b0203b | -20.51774 | -50.41297 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 00ca0cd7-abfb-3952-9272-566631ce6ca2 | -20.10343 | -50.08155 | 2024-09-30 04:34:00 | NOAA-20 | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b20fc03-093a-3332-9940-1d343b5e2d61 | -20.10009 | -50.08099 | 2024-09-30 04:34:00 | NOAA-20 | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aaf4e204-1236-30e4-a733-df20ecb21471 | -20.09953 | -50.08471 | 2024-09-30 04:34:00 | NOAA-20 | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4333508b-2929-33c7-8910-9de2e31ff867 | -21.77625 | -50.79018 | 2024-09-30 04:34:00 | NOAA-20 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 59947d1d-68b8-37b6-9057-8d4799d18180 | -17.72037 | -53.18545 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90f2837e-3a95-3f54-a0bd-389fd0ddab31 | -16.10274 | -50.35716 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f3a75b5-7bd3-34b9-8ed3-42ef5060accd | -16.59038 | -51.32021 | 2024-09-30 04:34:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2925a723-4ec7-359a-a3f3-6418a992d0fb | -16.58703 | -51.31961 | 2024-09-30 04:34:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70cb8764-2845-393b-88a2-1472e152d6c9 | -16.58643 | -51.3233 | 2024-09-30 04:34:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 423861b1-712a-336a-927f-1004935d938f | -16.11485 | -50.36665 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f94518ab-926e-3eb1-8c37-b758a33e630f | -16.11428 | -50.37024 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f685cc6-5e5d-35a8-b325-fef0a4f174bc | -16.1121 | -50.36248 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 899375b8-9606-3e39-94bf-96582736092a | -16.11154 | -50.36607 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fdba610-688a-3e3a-88aa-6a790491bc65 | -16.11097 | -50.36967 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d76f2ec-07cd-3f79-908b-06e055afdec7 | -16.10879 | -50.3619 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a5d6f38-3a81-384f-bece-fd38f53e112f | -16.10662 | -50.35417 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f13ee86-4acf-397a-b9fe-b0971142531a | -16.10605 | -50.35774 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46eb7222-d3b5-3f8c-a28e-1b2d81e64dc8 | -16.10548 | -50.36132 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1338d9e-7c1d-3646-b6ec-b09813bddf14 | -16.10331 | -50.35358 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54a349f9-c17c-3ce9-a7ea-022e6aa86077 | -16.10056 | -50.34942 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac446a2b-5e49-334e-a3db-c7e04e200670 | -16.09999 | -50.35299 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dae70ee4-ccba-30e7-8195-29370ae9889f | -16.09394 | -50.34824 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da4e8829-c904-338a-b900-c56412280d69 | -16.08732 | -50.34709 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fb943b9-d30b-38cd-a3d8-e46e406510c4 | -16.08116 | -50.36452 | 2024-09-30 04:34:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a74eb203-9cf7-3b46-a622-71f2328cf031 | -16.08059 | -50.36812 | 2024-09-30 04:34:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 602e18d9-4b21-3b31-acb2-dd8907364239 | -16.08002 | -50.37171 | 2024-09-30 04:34:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27283f68-ba49-3de4-b897-b372c741456a | -16.07945 | -50.3753 | 2024-09-30 04:34:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 027df2bb-ad78-3218-b716-aaf4d6598776 | -16.07888 | -50.3789 | 2024-09-30 04:34:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6a6e46de-bc90-3bfe-bf27-cedcc2a29aba | -16.07568 | -50.3562 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9622241-78ad-3832-9794-93e3ede3298f | -16.07557 | -50.37836 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acf3b8ac-a1da-385c-9b94-eb954c454853 | -16.07511 | -50.35981 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2408d81c-9273-3d29-b2d7-3e39d9d3848b | -16.07454 | -50.3634 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| add9c719-169a-31e6-aa32-78f1cda119a0 | -16.07397 | -50.367 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d98641f5-12b4-3372-9c90-d0f8d5526217 | -16.07339 | -50.37061 | 2024-09-30 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 924389f5-d709-3ded-885a-f86d28fee9c2 | -16.67635 | -51.72147 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e294415-96f8-37a5-abc0-4e22e24df298 | -16.67572 | -51.72527 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eacaf83-2b0f-3ac4-ba1e-f73c8b9db8e7 | -16.67296 | -51.72091 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77d2642c-1f8d-3ea7-bcfe-8c0e89f3a054 | -16.67233 | -51.72468 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 545d4ae0-be7b-3cd2-9a52-0c7bc97538ac | -18.64731 | -52.47409 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f4fada3-f151-3e17-bc6b-7246a4a5c3f0 | -18.64666 | -52.47797 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 326f1744-9ce1-391d-b7e7-ba2817187f86 | -15.10684 | -51.90814 | 2024-09-30 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aadedde9-05f6-3762-ac37-7ee58996165c | -14.91493 | -52.97807 | 2024-09-30 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 811e9f66-bf5c-3270-b3af-1b85582b71f9 | -17.72948 | -53.19582 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52f1cb18-46aa-3769-a31c-fc880c70d144 | -17.72183 | -53.17855 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af077066-20bd-334f-ad31-8e3cb782b107 | -17.72181 | -53.17714 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69302da6-3026-33f5-b935-348609fa3917 | -17.72113 | -53.18272 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 513b4eaa-8956-3219-93fc-e20c438b0993 | -17.72113 | -53.1612 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acea05cd-ee72-33b6-a7b1-3ecd1412bf0a | -17.71831 | -53.17789 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c52a117-6cd8-357e-bcbb-0903847454a9 | -17.71761 | -53.18203 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 635186fc-bd36-3a3a-a108-11a45c149391 | -17.65773 | -53.1494 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 465ffd16-d1c7-3d2f-be01-f89033d1cc9e | -17.65702 | -53.15357 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4421df9e-2135-37d5-95bb-addd8c488683 | -17.64715 | -53.14753 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README56.md)
