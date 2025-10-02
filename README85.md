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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c119e14-be91-3a6e-9653-96ebffede967 | -15.54618 | -48.17892 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f60148cf-2c25-3608-87fe-06b3617f5609 | -13.16616 | -47.80723 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46ab71be-be00-3b5c-8a40-86231259f939 | -12.93994 | -46.43228 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6a0191f-e87a-3cf6-a0e0-60fa4319dcf7 | -12.88485 | -46.92587 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 779a4f25-d0f9-35fa-be58-1d9f53b59f82 | -14.70564 | -48.2057 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85ac8b82-15fd-398d-a92a-97be9b28cc35 | -14.28755 | -45.96926 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3727355d-ed9a-32c2-bb3c-361789060011 | -15.25578 | -49.27865 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2783e1b9-4321-35fb-911c-37db33ac6e4c | -15.92887 | -43.33872 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d871a734-871f-3567-9366-66b4d53b8185 | -15.92532 | -43.33443 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6602e7f-6dad-3756-9ec7-aafe9849146f | -15.93274 | -46.24456 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a31a22-706f-3a48-a9a0-909ad13125de | -14.31128 | -45.97668 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90dd93b0-9c59-30de-b7e3-5b5bed60b1ee | -14.89262 | -48.0974 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58bbd049-fc24-351d-b7e1-0e94ed8af5ba | -13.05585 | -47.06343 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72b77f15-9a60-35d5-b63b-7b0995dd0ce8 | -14.40978 | -46.10982 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65453b5a-a335-39ea-a8d5-75e7875dccb4 | -15.0896 | -47.34979 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23d238fd-9187-329f-b209-a3be4aa714cf | -14.35144 | -43.84272 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8144bb9-c9d4-3078-884e-5b1ab79602fb | -14.60686 | -48.23362 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5d23953-1059-3cb9-acfa-2330f991b4ff | -15.34881 | -47.09085 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d2c889f-b20a-3a76-873e-570e79c876d2 | -15.26726 | -47.90122 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3389f0d2-9215-39af-9002-6e6b44099082 | -12.85429 | -47.03455 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 322906bd-5cef-32b1-8bf0-8fdc33c9f9fa | -13.34274 | -47.79997 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2711eaa1-be82-3c34-a253-d6cc3570f32b | -15.2613 | -49.28715 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3595541b-71a6-32f8-9da4-6808e1c95d1a | -12.63974 | -46.95684 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6d15441-391c-3a2f-b53f-cfcdc08b0c5f | -15.19664 | -48.16206 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e974250c-2c8a-3866-9f9d-6cd5a551f6ce | -18.50529 | -44.03078 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf1626c8-4e8b-33e3-a87d-cb52584dc31d | -12.83564 | -46.86626 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2a749a6-0946-36d4-8dce-2226b6a63b89 | -15.70006 | -46.26235 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 930a8315-ee73-3417-9e53-9edd074d40be | -14.44407 | -46.36895 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a09dbe0-6d03-31e5-a3ee-373e53d591ea | -13.30977 | -47.19582 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be11f841-ef21-36a9-bbe5-f8b83a9b1a29 | -15.55538 | -48.17683 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0ccff78-a325-3770-9d8a-aebd242a7035 | -18.84363 | -43.14719 | 2025-10-02 04:32:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0de242a1-7e9d-38b1-89ff-6227e3bfecea | -13.14899 | -47.78624 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36ec66ee-8ed6-3d0c-a61d-935503d0147c | -19.96047 | -43.65167 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 63fde817-f571-3f6c-b8ba-2dcaaa4d0aea | -13.30309 | -47.19477 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 138544d4-a8fd-3b03-b8fc-346d1724542b | -12.66868 | -46.85843 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0a27263-5dde-3cc6-b20d-eb45b6da21f5 | -12.01964 | -49.71405 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dc4f683-88ae-39bf-bb49-25d7ae0d33b9 | -10.88022 | -53.76699 | 2025-10-02 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 791d2a26-0711-38a2-b240-9c2ee0735193 | -19.59456 | -45.8952 | 2025-10-02 04:32:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0c6c9ee-b6a2-3c6c-892c-9f9aac266917 | -11.84051 | -49.50761 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351d8af7-3d04-3232-9308-233f7ddc9162 | -13.32423 | -47.22407 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e9a2c49-4e6b-322d-8008-25cda725f982 | -14.69255 | -48.11562 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25f9ea89-3afc-3b4c-9446-018ebc78a0c4 | -13.16557 | -47.83261 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4021d67-917a-34a0-bff2-4e3dc66e9083 | -11.85374 | -48.04385 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddcff304-e0c1-3c07-83a3-83f45fc27862 | -14.62276 | -48.30583 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28222f6d-c1f0-36f9-9d37-cdfc6748e21c | -15.74664 | -43.67765 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4441ea81-af70-380d-9182-f10b5ce34bfe | -13.30252 | -47.19836 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6798e0ee-6db8-343d-bf45-9506e2d09dc4 | -13.40098 | -47.77674 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c695e4a1-fae9-3918-8d33-1cb8eb50b66f | -13.00989 | -45.218 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e42834e-d542-35c8-a046-f7b19ece59f4 | -14.59487 | -46.71034 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a402c418-c48d-362d-8af0-5611fe4696dd | -13.5325 | -47.25307 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0e83806-6e99-36fb-a0b0-049d6d28ddd1 | -18.12729 | -43.99171 | 2025-10-02 04:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f940233d-8dea-3ddd-adbf-8e40785cc9de | -13.64871 | -48.02424 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8277fd3-6d21-3759-bae6-ff4f4bb2cce3 | -18.17573 | -53.2774 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9f24c1a-e13c-35ec-a19b-a66fc1b9be64 | -13.32901 | -47.80525 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b1bc4f1-22f0-37d2-884f-7161b8381c46 | -12.25233 | -47.79253 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99cacf6b-d264-3660-ae96-a942baf1324f | -12.89824 | -46.90591 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 216aad2e-ce9b-377f-9322-5c8c7d885138 | -19.52049 | -43.60902 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71ba0795-83ae-32ac-8a83-da7e255bfc79 | -13.04915 | -47.06235 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74603300-73ee-3ed4-b002-4fa69f84f593 | -13.21414 | -47.34846 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4754a28-bd0d-347d-b70e-884ac208fb3b | -13.29475 | -47.24833 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b197954-eca6-3123-bb6a-3ae2302c8c2b | -14.00823 | -44.97499 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21c3ba51-558d-361d-8267-fe8f3fa4a094 | -16.0416 | -50.89378 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0656c5b4-d746-35b3-aaf0-e2e02f5cadcf | -13.34436 | -47.33693 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ac08b43-9569-376e-9b7d-9d8d3c5fb02b | -14.91881 | -47.2332 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4784675-e9fc-3839-a731-7e0e3a213a3f | -12.4131 | -45.16965 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94981b15-6538-3338-9c2c-eb14687d3142 | -15.22574 | -50.10817 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d4f2d2a-1332-38c6-bd85-f7538b35bee7 | -12.50989 | -50.28506 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3ae60bda-5035-3c03-a2fc-f2b74b1cf630 | -15.32224 | -46.29345 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 333aab8d-36be-368e-8d4f-22209256660a | -13.40151 | -47.79505 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95807417-a3b5-3bbe-ada0-1b7dbc58221f | -15.20472 | -48.00164 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 059599a6-0a16-37ae-a4b6-3f1745018f3a | -12.90953 | -47.1757 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e6cfbcb-9471-3d5b-a99f-96463e99fc2e | -14.70139 | -49.61855 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 354946ea-e8b9-3224-9a86-f38f52873b9a | -12.81249 | -47.03881 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a3f317b-6bc2-3a6d-b16c-6202bd3aa085 | -13.4187 | -47.79422 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 526658d3-5481-3bce-97c4-386502926394 | -13.43496 | -44.22541 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e324cba-b646-3adb-8839-ee7abb51ebd4 | -12.02407 | -46.63182 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e984c1e4-5a98-3b48-bc00-adda46008d7a | -15.26366 | -49.28342 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f8806fe-2f0f-366d-ae63-decf1e5e5349 | -13.40484 | -47.79559 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0298e8-239f-354a-963a-31cdecb57623 | -12.65753 | -46.86395 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aeb84a8-a722-30b9-86d7-afb882bd07b5 | -13.18283 | -47.78816 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65c59c94-8191-3abe-a61b-71674ebb6b7c | -13.14668 | -47.84407 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56719a1d-ebd1-3125-8ed0-6d5d43ff102c | -12.88875 | -46.90063 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40526d8-6591-33a0-b295-c30a39722cc5 | -14.59551 | -48.3269 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab1755a8-7d3e-3145-b932-971015aa9e96 | -14.89755 | -48.1312 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c6b600-503f-3b53-a2b7-3a687b5778c9 | -16.2789 | -42.5487 | 2025-10-02 04:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801ddaf7-0f39-3719-b0f8-f6b08a7777cc | -14.3263 | -45.8754 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6320985b-6662-3be9-b166-5047631e62ef | -19.44069 | -44.16073 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb793b33-d2d1-3b67-8dd1-4816b6c8f8d4 | -14.2148 | -44.93389 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f626a625-b7e0-3a36-bdba-f506cc4026eb | -14.22441 | -46.11787 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 463d767f-5bb3-3d1f-85f5-bb0e01eac4c7 | -13.3388 | -47.32867 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 385df470-408a-3cf8-8c7b-ec5e3c98c776 | -12.26142 | -47.81629 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baec7478-c124-3713-b4af-8df7eb167022 | -11.92957 | -47.88164 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae729a07-79f4-3ab4-b3ab-f373fa8a74b8 | -18.5034 | -44.04787 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0a559753-cb0e-35c4-b16c-ea4269b79b37 | -12.01235 | -46.64096 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f3e14c-3a74-369d-b4e4-d10ed52c54c7 | -13.20579 | -47.33612 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdcbd448-8036-3abc-8b54-282c9f69283f | -13.33324 | -47.34243 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91631461-43f4-37e8-a271-c0b3891b658b | -13.35711 | -48.11916 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd92838a-cae6-3f8c-af96-b2ab86b104fd | -17.1718 | -47.01537 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b6af7d8-790a-331f-9fb7-3e1dcbf0e5e1 | -14.42416 | -46.13176 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1932ff8b-9839-3121-86b8-7decd9c5b679 | -13.34492 | -47.33334 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README86.md)
