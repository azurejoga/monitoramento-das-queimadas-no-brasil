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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fb2d2dd-bbc1-3f2e-ba44-992fdc575a52 | -9.58277 | -54.94943 | 2025-10-07 04:38:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3726bfd-9f36-353b-ae92-812a09720020 | -14.28397 | -45.84444 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f96c8ab6-3f13-3030-b80f-98934797245c | -15.21709 | -49.2994 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5683ce92-a6fd-3623-9e44-0cb122c1d34e | -15.36802 | -47.30757 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 732dc657-b31c-3a40-bbec-af01c1e8e6f6 | -10.73838 | -50.49093 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a2ba67f-43a5-3188-9cb9-d68aecd252f0 | -13.26097 | -46.47174 | 2025-10-07 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 522b2dad-5529-3ed3-977d-00bcf3f4b95c | -11.80747 | -45.12613 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42935eb4-7e4f-3665-b2f8-755f9b70d6c8 | -13.72883 | -48.06511 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81469b42-d8ea-395f-bf3a-6f05da51cd59 | -14.61861 | -52.48642 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 18f52fdc-3200-3ee6-86a1-605201bde51d | -14.91762 | -46.81119 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2859a9f5-8af1-342d-b930-36fb194dffdd | -11.12189 | -47.21899 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e17586c5-0c4e-35dd-8e44-8e09960115f8 | -17.87496 | -48.23234 | 2025-10-07 04:38:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 182db1f9-e936-36cf-9287-2f1cad634f8e | -15.22488 | -49.31541 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3644b4a-20e2-3b1a-8938-a4459be5a991 | -11.02387 | -51.15263 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14cfe05d-9f2d-311c-ae2d-7f4c140a422e | -14.762 | -46.05423 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4756a88b-44e4-3716-8196-b59856f4a4fb | -13.57375 | -48.14731 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31f66969-f3d4-3969-8aef-0ac9abce5dee | -13.08976 | -48.00493 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e74fb3d-ba93-32bb-94ae-9c998a1f5a8e | -13.74017 | -47.94462 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 939e0e36-88cf-388b-ac89-d66721f7ce18 | -13.67308 | -47.94974 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 173a6e3f-2b27-33e6-8599-a7190acb9209 | -10.40794 | -50.31219 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 623ed793-e228-3060-80e3-e27ee7619688 | -16.38265 | -48.9929 | 2025-10-07 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8eb8765e-baaf-33ba-9304-03e68b1637d3 | -15.58681 | -52.55007 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a4561f0-b394-3348-a277-d86ccb1117bd | -13.50134 | -43.67093 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 111ca12b-5bf6-3138-8e55-bb166bc10bb8 | -13.01917 | -51.03067 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f9a4067-9671-36ea-987b-f3608f5df0d7 | -10.45697 | -50.41854 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf610066-e7e0-3045-90d6-fbdd4b471b61 | -15.97224 | -50.83464 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5880ef5f-00fc-325f-a849-70c9e967ae5d | -9.33898 | -54.52384 | 2025-10-07 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53efcbd8-dc02-391b-8d2d-d7c7d995d42a | -16.06171 | -50.99167 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fcfaf94-c091-36ab-b49e-e6fa8f1b4af7 | -10.09796 | -50.52024 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0298596-4d7e-309a-b655-b8ad74c036da | -10.79551 | -48.58805 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72db18cf-99d2-3c47-a33e-d5bc23355d6a | -15.38573 | -47.98602 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71e54cb9-ae1f-3064-ac30-017560797d38 | -11.7396 | -51.49628 | 2025-10-07 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2490f498-1d75-346c-86d7-f4aac3183122 | -13.33591 | -47.76146 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b98c8f65-d081-3dc0-87d1-7e02313b0a2d | -16.05994 | -51.00258 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4d34ec-daad-348f-99ae-340f1766ffd0 | -12.89691 | -54.75528 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4dffc1f-7bf6-3616-a2d3-df84c97deb50 | -15.42999 | -45.86606 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e3b5faf-4ebb-3bcf-b014-3222549c7420 | -11.94351 | -46.44349 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 74cfcbdd-e3d9-32c6-ac97-5f35595b10ab | -15.07964 | -46.63853 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c97d9598-157a-3a39-a6fe-a609d9e3f405 | -15.07602 | -46.63783 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a92e0d8-a702-3e7a-a0d4-cb7816b8a730 | -14.76509 | -46.05935 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b134ca6d-eb7b-39f9-ab61-d868cf2903d4 | -15.60092 | -52.57353 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d54404e2-51b5-35ea-b7cc-0a4ad9da1d25 | -16.10405 | -48.94547 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52204218-6e7a-3e63-886b-e042bcfbbf4a | -17.96049 | -44.40567 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb42b06-d691-3e4f-83ac-5370ed27717a | -15.17249 | -45.73358 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97e5b9c7-4a44-3121-bd7e-889590432699 | -15.38997 | -47.99365 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 105d081a-d99d-3144-bf29-211f08a75d80 | -13.2619 | -47.18171 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3a6dfc0-d053-37f9-8058-bb68fe2c8070 | -10.61431 | -48.66755 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2271b4a-ec0b-3689-b831-2731864efa2d | -11.27935 | -49.01643 | 2025-10-07 04:38:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54d3b377-9271-3d52-9035-f4997a0c1191 | -16.06623 | -50.92127 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bddba80a-163c-3d50-8868-a45efd52b5e3 | -12.97836 | -46.78333 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c3294dd-fcce-3306-8c7b-abdfe91b5b6f | -11.02193 | -50.91769 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5363f82d-1aff-315c-9082-2f43e4498b72 | -11.71793 | -44.30026 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f860f4a-3032-3aef-9fe9-cae78819da19 | -12.86049 | -42.62622 | 2025-10-07 04:38:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89f09f7b-0d68-3404-a044-2491f42e67ed | -9.45422 | -56.6536 | 2025-10-07 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd303366-6359-318d-9b16-cde4e7cc30e7 | -10.40295 | -50.30007 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e762a008-430e-3779-996d-84bd513f00bd | -12.57442 | -52.20123 | 2025-10-07 04:38:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40cf4790-5ba5-3df6-b450-f776e61fe118 | -10.31957 | -51.45685 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baceb557-6587-3770-808f-eebb4dfb543b | -11.74107 | -54.72208 | 2025-10-07 04:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f99015c-0e74-3756-83e5-90b97958effe | -11.04121 | -50.92014 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a57a9cc-e419-3ad5-8a2c-3b01cb40d182 | -11.80682 | -45.13062 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d33a9194-7e57-3d6d-a850-23e6fa3377a4 | -13.73619 | -47.94786 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 811cef19-1e48-3ea6-a28b-6e8f5da3f58b | -14.29016 | -45.85474 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e619f593-16d5-387e-a7c0-d381ba3e3f17 | -13.30972 | -47.77271 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8fb1542-bb72-36e7-bd13-124086f19894 | -11.93935 | -46.44699 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07bd1ea3-9ed2-3f74-975f-6e795c85dc6b | -13.85677 | -43.99082 | 2025-10-07 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58fdb1f8-56c8-378b-9817-5b59dbfea703 | -12.18547 | -47.78593 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83878a71-db22-31c4-a7c0-f41ff7aa6bad | -13.27102 | -48.07389 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2575d8d7-1951-3955-abdf-5e411bde3e63 | -9.38909 | -59.42492 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 561e87cc-e5d0-35f8-9d92-c6eaab64d8ae | -11.23646 | -47.77043 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33f88ddc-bbdb-3046-81bf-993ddf02b0e8 | -14.5627 | -48.94957 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dae8cfd6-dadf-3024-a2b1-ef287f186f95 | -8.85814 | -62.37114 | 2025-10-07 04:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c6a48a-9282-3675-a11e-6678595d9af2 | -13.35815 | -47.5677 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb399104-71cc-3a48-9f43-0b66fbb8b792 | -18.27965 | -45.46159 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf635fc-1bea-3ded-b134-dae2830889bc | -15.96831 | -50.8377 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bf5e3fc-ec4c-3c90-b0d7-96b2e3d28662 | -14.72045 | -48.35231 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea4b2ff2-1ef0-3769-b4a1-635df9f656df | -13.32525 | -48.03727 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dae4d7a-5102-3a9c-8e80-5eb45839dca1 | -10.74539 | -50.46936 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a688b1d5-2838-38a5-98fc-1ec2c5a9f3ee | -16.0142 | -51.05091 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77b7ee53-0665-309b-a15a-05da3a26437f | -14.51118 | -46.92086 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c930b91e-ec43-351e-a40d-dcbe50171f5c | -17.16296 | -43.44874 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9dafe2a-971c-3858-b7b2-c9abee13d42f | -11.9423 | -46.45153 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98002804-8dc6-3d3b-9563-d0650a4b1d21 | -10.41932 | -48.0948 | 2025-10-07 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b490911a-ae8d-3068-bdbb-13925a6101ac | -14.61086 | -52.48919 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384d60bf-b358-37ba-a423-c96cd4f2455d | -14.9122 | -51.44086 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 241f7a32-cfd6-3bc3-8744-009cc4823ca6 | -14.92457 | -51.45074 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0419ea95-1a81-37b2-8c42-0bbeb7cf041a | -15.38799 | -47.9944 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99a5eccb-0609-387e-97e5-a8bf6cda0096 | -18.28364 | -45.67949 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 354e6fff-0919-3ad3-86ea-b9265cb02ba3 | -13.26307 | -48.05776 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 308f14f1-fd55-3f61-a6b0-964c91f695f6 | -13.28043 | -48.47226 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e365f5da-b548-382a-b1a6-d8e1a9f81f0b | -13.3171 | -47.77017 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e0ba1db-f771-32c6-b4a9-edd95c9a44e2 | -13.71238 | -48.19555 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cc7b6ab-3728-3a73-9a9a-c44821222d74 | -15.17154 | -52.76546 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b32895f-c1eb-34d9-b8ea-c34f57bd94ff | -13.71864 | -48.0634 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d4a08a-41c2-3a90-a119-b93523e102e5 | -12.01787 | -47.78672 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abc92a12-cef2-36d6-92be-a40b5c63679b | -18.28058 | -45.45445 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84424cf5-e3df-3a5f-9633-239866fa1b9d | -14.61601 | -52.54475 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a4b5a5e-8ba8-392e-a2c9-200070dfb6ec | -11.03066 | -50.90749 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9253005-1323-372e-bdd7-46b0450c5053 | -12.41072 | -51.13759 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507d6068-d0b7-32f4-bdeb-cc4e871bde2a | -12.58179 | -48.11296 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 525d907a-fe46-34f0-932c-5148ed8ccee1 | -10.50374 | -51.49886 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README72.md)
