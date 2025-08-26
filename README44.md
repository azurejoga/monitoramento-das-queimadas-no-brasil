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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 569eef76-8e5f-3ccd-85ae-71e0fef98db0 | -13.48806 | -47.00915 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92efdc58-0408-388a-aa96-a5ccc26d793a | -13.65171 | -45.70292 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a090c578-42f8-3c2b-bec3-d93447b90c51 | -14.29852 | -43.91205 | 2025-08-26 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a69b775-a4fa-3b3e-b527-0c83d3a4feaa | -15.18158 | -48.18996 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33f8c70d-0ce2-3ae7-a152-ebde6b650e2c | -12.94358 | -46.33757 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfa17010-e04e-313d-bc9a-ed1d33873cee | -11.55241 | -52.10596 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef872097-a8fc-34f1-9ab2-5641ed19124d | -14.80593 | -48.96785 | 2025-08-26 04:23:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7758b6a4-59ab-3831-8fdb-9d1a3d60c498 | -11.54331 | -52.13093 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93c8bf68-68c4-33f8-ac41-d33e8f458a99 | -16.40364 | -49.4799 | 2025-08-26 04:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61dacc26-88e0-3772-82f0-cc07c483165d | -13.44767 | -46.99111 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7c40df3-916f-3534-b094-5d3661f36611 | -13.45331 | -46.87072 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95b3b35-1996-31e3-ba53-2065cdd59d62 | -11.54849 | -52.12741 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cdf8624-93b2-35bc-a9e6-13e6f0b05d35 | -13.41428 | -46.87895 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fac34eb9-12ea-3e7a-851e-08ef65e2be93 | -13.43925 | -47.00077 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 522e5960-b970-366e-80b8-fc9716146af1 | -13.52277 | -46.90059 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c97f044-a78c-3c34-8cf6-4a060adbad28 | -13.41037 | -46.88194 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dc8a1e5c-d4e5-31d1-ad11-0cb79d399a41 | -14.76393 | -59.70823 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce4a4143-c93d-3445-8726-c4a2cda67195 | -15.63089 | -52.72449 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e81473e-44c0-3ee5-bda8-ca58f956cad8 | -12.75699 | -48.10231 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b92799ba-2e80-3265-8929-bcf931640ce5 | -12.73087 | -48.1531 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b16720-0182-3aea-ad1a-84262cad959a | -12.76261 | -48.14234 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2ef4628-39da-3d1e-9d08-3df163905a85 | -13.1654 | -45.28781 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7aeba304-90d5-3065-bd2a-0e54b0d2b495 | -15.11525 | -48.65274 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a269c5b-6471-3b24-b871-877b74c8d931 | -11.91534 | -47.60539 | 2025-08-26 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 278375e1-666d-3957-8219-179fa963773a | -10.38955 | -57.69252 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf6d69cb-b10c-389d-b400-7d229b23c96f | -15.02633 | -48.15624 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 513e51cb-59df-3381-973a-1d2d4ca6bf7d | -13.412 | -46.89315 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b374cdd7-b053-3ade-8253-855e9b496df8 | -15.41188 | -46.59435 | 2025-08-26 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f088b33-64a9-39ea-bbf5-3dfe62f08780 | -17.22707 | -44.80818 | 2025-08-26 04:23:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35a709d0-d476-3f9a-88e0-af4af12ace40 | -12.43953 | -43.56634 | 2025-08-26 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c19d17ae-0f9e-311b-b431-f1b45fd96d04 | -9.18722 | -59.45272 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d27b1a30-8f16-3a84-a021-72acf74203c7 | -11.55679 | -52.10675 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eed1ab04-44ed-3eac-afdd-bef0b12cabfc | -11.51632 | -52.1321 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 93d39a13-58b5-35f5-b593-ea21ec7b2ece | -9.18972 | -59.5146 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95904aac-2e61-3391-b337-741a5219acd3 | -12.74786 | -48.09314 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f6b5564-b541-32ba-93e0-ec0f6dff2d1a | -12.72802 | -48.14886 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6955d5e7-4963-3b55-b034-b35d76a645bf | -14.76154 | -59.71894 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb281099-8c0e-3e94-a637-e27263268fd1 | -13.41752 | -46.90144 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cca82e6-03f7-38bb-a28a-68a7c0aa5893 | -14.47939 | -51.94983 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590c634e-fede-3bd0-96bc-94df0d453491 | -9.15978 | -59.54935 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 07a0f05f-08df-3dd0-909e-a9d9df07d5b9 | -15.0816 | -48.66278 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8496cf62-3504-3b49-a12c-d41f43e66c7f | -9.19541 | -59.5237 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f9886b6-9ac2-3527-b253-446624467205 | -11.50602 | -52.13902 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0e49bc1b-e25f-34d6-9686-269dfd3c0699 | -9.16625 | -59.55587 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fa50c85-429b-3d93-8828-90d1eab39831 | -12.93197 | -46.32473 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b155fbe-97b7-3b9a-9a20-f508470b7d18 | -11.50239 | -52.13388 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9881638-147d-3c1b-a325-3c0c64425535 | -13.42029 | -46.90554 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80fff605-f326-3540-9672-19d5fe5893e1 | -15.02973 | -48.15684 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b76139c-ba2a-31af-81cc-1416a0175149 | -13.60449 | -48.19696 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ce880d1-041d-3fb9-925e-b8d09a04004e | -13.16429 | -45.29498 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fadba541-9439-3652-8d05-3f47bd73995b | -9.18161 | -59.51507 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46c6d0ed-dbe3-3f72-b7b4-7026358ce2c2 | -12.48733 | -47.22931 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dd6f22d-a7d5-3781-9ca5-575718e79b00 | -9.18374 | -59.54409 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 063f1ce7-9766-33a2-bf34-de03248309ac | -14.90861 | -47.3133 | 2025-08-26 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfafc095-afc9-32ac-9ae4-e9b4161c17b7 | -14.75903 | -59.71768 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3397fa83-63be-3b26-a572-24a450fd01ae | -12.63129 | -47.86312 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c3f3408-79a9-3037-81e7-9d2cdcd849bb | -13.41094 | -46.87839 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 860211ab-d97b-357a-b1b4-a906335e0d1f | -16.74856 | -47.59866 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac2b1e65-9278-30bf-9544-67d23b0909c2 | -9.15538 | -59.46142 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36d2d6ae-286f-3200-81ac-155f6af7f45d | -15.09734 | -48.71728 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a19c875b-373e-3a94-a29c-3a1375f033c7 | -14.25163 | -48.04437 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8cb7f4e2-9bd5-33bf-92bc-878fb401e947 | -11.03413 | -49.14384 | 2025-08-26 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83b3c09e-9a8f-3824-99d7-fc3947cb2c04 | -11.53927 | -50.45583 | 2025-08-26 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db68b572-1df8-360d-b854-57c361b24dd2 | -11.91517 | -47.11262 | 2025-08-26 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6977c92-dd13-3db6-93aa-23e857c6244b | -14.63529 | -49.07971 | 2025-08-26 04:23:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fb67bdf-ad6c-383f-8096-9df719db6231 | -12.74033 | -48.0958 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3547f527-cde1-36b2-90f6-198d89eef3ee | -14.36336 | -51.9201 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebfd8ace-f52d-3756-96a2-61500483d285 | -12.76133 | -48.14995 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc3cbcc-4fbb-36cf-a77a-d1f1d7741dd8 | -13.4098 | -46.88547 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6ed75883-ca70-353a-b4ff-c809cdea79f8 | -11.05069 | -52.0123 | 2025-08-26 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7750b44d-90b8-3a21-95e6-764a5ca95060 | -15.10728 | -48.74295 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc20557d-e668-3ba7-b45f-c36d78574a55 | -13.41637 | -46.90855 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa2ac7d8-da5f-3ab8-a10b-feaaba16ff0e | -16.78564 | -47.57104 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccc1071a-1338-386b-b415-6eab8aa8438f | -13.41142 | -46.89674 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83d99567-4c87-3533-803a-d4e403653001 | -15.64057 | -52.73331 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4eb5f95d-79ab-31b0-bd90-a6d6c9821f41 | -9.20412 | -59.51792 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a824ce5f-1169-38dc-9898-96f112345370 | -11.55287 | -52.12827 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1db89c55-f6fd-323f-9ffc-346f6a297ab4 | -10.87863 | -55.79238 | 2025-08-26 04:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed671745-ba54-3343-925c-cd5eda42ad28 | -14.4556 | -53.35572 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 441aaedb-9279-3df8-915f-4331fd083a12 | -11.50678 | -52.13472 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4eafb683-d8e2-3601-8ec1-3a4a7b8c6233 | -10.39596 | -57.69378 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1edf94f2-ab9a-3358-8642-52e59e756a84 | -12.37281 | -46.55694 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d67f7800-2972-3f35-b0d1-a175e53f76a0 | -12.93253 | -46.32118 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f9fa02a-9abe-3a04-81c9-469ed9499ccf | -13.46331 | -46.87248 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f50b8e77-eacc-3581-85ba-92d9acc9ab95 | -14.76272 | -59.71367 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61a66e64-0c69-315a-b47e-9ee2c3414c3e | -15.03183 | -48.6747 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e173352-6e5c-3fae-b7b5-c2e4b38e4b2e | -12.94471 | -46.33047 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2deb15d-ec1e-3f04-ad82-37582edb0206 | -11.63618 | -44.86219 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db3413cd-badd-3d07-a989-cb9a11eb99d1 | -9.64255 | -59.63793 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 44ad0eb7-de17-3535-8498-8aeae750b8c0 | -9.17728 | -59.46065 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5e421527-865c-3c74-85cc-751c6651994b | -15.08607 | -48.55196 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fc72cd3-0ffa-31ec-b3d0-956c7c4c3b52 | -15.62854 | -49.38036 | 2025-08-26 04:23:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73fdfcbf-0e04-3f75-8d03-2f73d2b066e7 | -14.30737 | -60.37191 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df6e0a5e-4127-3c5b-9f32-953bbabebeef | -13.61419 | -48.1594 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7034a5f0-4ea0-3b6c-8733-c5a7250cb837 | -15.40855 | -46.59379 | 2025-08-26 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87cc2425-7d7b-3c6b-a8a2-ff31e434bb45 | -9.1758 | -59.50629 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41b8e482-4a74-32d2-8ee2-ba0385637461 | -11.54691 | -52.13611 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 814a318c-351c-329e-830e-a3ee7ff76e97 | -13.04883 | -46.31465 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 353754f1-2b46-38bd-9f3f-32dcada0aa48 | -9.19842 | -59.50881 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f9ed33f-4949-3154-889f-ae9573544948 | -11.57071 | -52.10488 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README45.md)
