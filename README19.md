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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c7825b6-c7fc-3122-a312-9c3545c82ac1 | -15.12211 | -52.95371 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a7d2b34-8b53-358b-a65a-7757816eee4c | -10.22679 | -48.08305 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14723a22-059d-3106-87fe-c21d9e043bb1 | -10.19834 | -48.09134 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91013d0d-695b-3b46-b7fe-ee59ea47e376 | -14.68186 | -53.41172 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5d7a1e8-b5d2-3c76-8127-23e63556fe07 | -15.11883 | -52.94781 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 68c0a8c1-5543-3572-841e-402af475ef95 | -14.6839 | -53.39707 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 881807cc-14a4-3a04-807d-d78476f08319 | -15.11954 | -52.94247 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a0662b2-dd25-344d-9321-c9a994579d41 | -15.11485 | -52.94717 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 132ebece-8098-36bf-a29b-a1f3efc9a601 | -11.27323 | -52.46729 | 2025-12-03 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a52bd0a-315f-32f7-8e14-69985ac5e795 | -15.12164 | -52.94684 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 844abcbd-fafa-3841-842d-b10ebcb4fea5 | -14.68639 | -53.40746 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ca34c93-97c7-3655-b98a-b2bb479f38a5 | -14.67937 | -53.40134 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9566094-edf8-39c7-898d-64a69e8f7800 | -14.68322 | -53.40196 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fd08ba6-a761-3ee8-adf5-da57c9e4f6ef | -14.68005 | -53.39648 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 092feb31-b1a7-3fce-830b-56b4c9a34307 | -14.68254 | -53.40684 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db3aa759-a5e4-38e2-b347-8e4505455323 | -10.22164 | -48.08232 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 127d03a0-0dc8-3872-bc3c-fdd94393530a | -10.22639 | -48.0861 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 450f0d94-87ec-3811-a8b7-c0f7afec57bc | -10.1979 | -48.09461 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03c79b85-883c-35cb-a403-3067dc8127cf | -15.11766 | -52.94623 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba13ce7a-a9d6-3af2-9d0c-dc40fbf1597d | -15.11841 | -52.94089 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3518adcb-7fe9-3458-9bbb-d4741f8cd976 | -14.68707 | -53.40257 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b7a989f-d819-352f-a2ec-3abd6698ab65 | -15.1209 | -52.95213 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c7e139a-3be3-37ac-8408-3d64a302ee79 | -14.68775 | -53.39764 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1a79561-b6a4-37a4-8dd1-3188d2a1eebf | -14.67869 | -53.40623 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7777d4d6-0d0b-30e0-868b-4fd53ae3fb22 | -15.12239 | -52.94148 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 063c5946-29aa-3943-b746-c4b3a529305f | -15.12352 | -52.94305 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8067d83a-9b9f-37e3-8541-0d8d48a7fae0 | -15.12282 | -52.9484 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d2c4d6e-c898-34c4-b14d-aeb57a8d9b6a | -15.11813 | -52.95308 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe450f69-7f07-3c82-8ccb-fced00f272c8 | -14.94582 | -53.05861 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53253490-120b-3760-b292-13f24f3d1e8f | -15.11693 | -52.9515 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 629c70ff-0b0f-3027-9c44-7119a37f944d | -10.19947 | -48.09148 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59de4c2c-4564-3dbf-a79a-5559191e0b72 | -15.12017 | -52.95738 | 2025-12-03 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2c6bce4-dda7-3f4a-afa9-1344cf074bfd | -11.27393 | -52.46236 | 2025-12-03 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c993c5aa-9596-302a-809f-ccf4e163c728 | -11.27783 | -52.46293 | 2025-12-03 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ca1120-461b-3801-b1fa-c2349a3462b2 | -17.54245 | -57.21834 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d637bbf5-a5e6-3d2d-9ffb-43bcc99d2f98 | -19.63149 | -56.78024 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| afa613b5-3dd1-30c6-bd1c-df2403446852 | -17.54076 | -57.2295 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1f60bdb9-2fb2-3e3b-9453-a7e3bc313508 | -19.62053 | -56.78254 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9bafb1ef-b0e5-3a0e-a813-4fae5e68e972 | -17.52482 | -57.19326 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3a9e95c2-dba3-38c7-b3ed-4ac7994ded16 | -21.62797 | -56.13514 | 2025-12-03 05:12:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 199c8532-c4f6-3138-be31-9bdb2e6e0c31 | -17.53627 | -57.23638 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c126181b-1a2c-32f8-98f6-adb3698a65f7 | -19.61532 | -56.79389 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7e24e7f1-3604-3484-b5b3-425ca21022c0 | -21.62073 | -56.13397 | 2025-12-03 05:12:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd1508be-51f1-3bb5-b969-297e9ac27852 | -17.5301 | -57.23154 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 56c63561-b166-37c9-a91d-4eacb9061cb7 | -17.54188 | -57.22206 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7da90568-713f-3638-a378-422ee8c3a03e | -19.62745 | -56.78366 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 72fc6be3-5239-3a55-b3a2-4e122d6954a5 | -17.5329 | -57.23582 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7802edb1-7187-3454-85d4-336e51efd405 | -19.62804 | -56.77968 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 919480fe-e4d8-39da-befe-542b8946b087 | -19.61474 | -56.79787 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4aa6ec0d-d022-3ae5-ba85-e4fbf9caadf0 | -20.30554 | -47.34686 | 2025-12-03 05:12:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fffc829f-f792-3243-ad8c-b16e46cb66d7 | -17.53346 | -57.2321 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dc865146-8963-346a-9f18-449a9369e36b | -19.63091 | -56.78422 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 990078ea-530a-3184-8566-2920893c38c2 | -19.63032 | -56.78819 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5604df7a-77f6-34a1-8509-3ecdb0cf1e3f | -19.61591 | -56.78992 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d84eef41-7dfe-3341-b4da-b6fb53593498 | -19.61128 | -56.79731 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 203cc5e8-2749-3a1d-ab80-c80648d7b3ca | -17.53739 | -57.22894 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 54a76100-83ed-3ce8-9ce6-fffeda0f628c | -17.54638 | -57.21518 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2e8bc916-ae59-3fcc-a72f-fc0fe16ba998 | -17.54581 | -57.21889 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ecdda20e-b23f-3a0e-9cc0-dd69cec092c9 | -17.5402 | -57.23322 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f089ee0d-d567-3033-aa79-3f100b9305b3 | -21.32412 | -55.78455 | 2025-12-03 05:12:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a26c7757-c2a2-3d75-84ae-2e803247d442 | -21.62435 | -56.13456 | 2025-12-03 05:12:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b371834a-4577-3355-975b-f2ef9904f13d | -20.30503 | -47.35246 | 2025-12-03 05:12:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3961e60-b5ec-356e-b9e7-7cad5558bc6c | -19.62458 | -56.77912 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 842c0bc9-1650-3c05-97cd-1104f9e78a9e | -19.61415 | -56.80184 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4bc9e6ea-894a-3449-9f9e-12d324e08148 | -17.53683 | -57.23266 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 574d1e85-643a-3e55-8aa3-b8f1fa4840db | -17.52954 | -57.23526 | 2025-12-03 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3beabf91-e6d0-3662-8425-2a2e0e39aad5 | -19.61761 | -56.8024 | 2025-12-03 05:12:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d612f38a-8719-3650-b9ac-edfad79a6436 | -30.51369 | -52.80577 | 2025-12-03 05:16:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 64fc0230-7459-3abe-85b8-c39e10d76874 | 3.48669 | -51.26399 | 2025-12-03 05:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8987494-4100-3a04-9999-ce3986654d72 | 3.49134 | -51.25999 | 2025-12-03 05:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0029ee-dbda-3e16-8b72-d9d45198c2de | 3.48616 | -51.26086 | 2025-12-03 05:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c239c76f-316f-37ab-a415-e9e50b3ed31b | -2.35771 | -50.11377 | 2025-12-03 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17fcea2e-858d-3d70-b09e-6cbad69b4c16 | -2.24651 | -52.77465 | 2025-12-03 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 980bfb18-769a-3d67-86c7-a5f6605bf3db | -2.38685 | -49.39533 | 2025-12-03 05:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5a3b13b-0b41-3a92-99c1-e720d661d170 | -2.38883 | -49.39169 | 2025-12-03 05:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db54e0a-7d5f-374a-bf79-320e53eb684d | -2.9799 | -49.52066 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 397efc12-ac0c-3bcc-98a7-2dfe9061f14a | -2.98629 | -49.52172 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa28e3b7-0d8e-3aa0-9f47-854e41c3c396 | -2.70472 | -49.31609 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a42e8804-5443-3df3-937a-73bdcdc93b6a | -2.69826 | -49.31516 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed06e730-9e89-38e2-b39c-1ef3a5ff1d04 | 2.87526 | -60.26727 | 2025-12-03 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c96a1b68-4bfa-3098-9ef4-edd3358c87b0 | -1.19989 | -53.08926 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 05201e34-f196-37b4-a9a7-d16e96e88fa1 | -1.05787 | -53.10361 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0d4cd3-b0f7-368d-bccd-e1b4a40d535b | -2.15063 | -53.53704 | 2025-12-03 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3403938b-7b54-3adf-ab38-4f2f2c3870a0 | -2.21082 | -48.00639 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4cddd23-f302-3b53-b83e-1e9c4ba6d2e3 | 2.87418 | -60.26041 | 2025-12-03 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdd41908-cd62-376c-964d-56419c6acdf6 | -2.17067 | -48.36697 | 2025-12-03 05:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cb9e7d2-ddff-3159-b3d4-e5a554021564 | -2.16973 | -48.37318 | 2025-12-03 05:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bd0ae38-635c-391b-826a-3bf4a7ad0484 | -2.83147 | -50.46796 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c49bc66-dba9-395c-913f-06004e32e881 | -2.69265 | -51.7984 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0f6a8d-22ac-39a5-b839-a31b4979f524 | -3.30831 | -52.56844 | 2025-12-03 05:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ffd821-a866-3ff0-aebc-32747cc021c4 | -2.24699 | -52.77147 | 2025-12-03 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f7c272-d6dc-30ee-9340-c3593d36efa0 | -1.19858 | -53.08767 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36ea2046-5f3e-32a2-9c6d-4efad093071c | 4.16487 | -59.95477 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81fb7873-a228-3849-bf5b-cc18518a129c | 4.16492 | -59.93367 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39fc3475-0052-359b-abdd-40851cebd150 | -2.21177 | -48.00008 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96748266-4b0e-3c36-97d1-0f1841b02c53 | 4.15287 | -59.9215 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be4490a1-f283-3297-9e42-297c2c448a99 | -2.20463 | -48.00532 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 29df5dfe-af92-34b4-883d-4f3bd28b5ef0 | 1.99797 | -55.71159 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0802b5c-cd50-3dac-917f-4b57c00f6cd4 | -2.69745 | -49.32048 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2ddf608-0e12-3c4b-be0f-af1ccb18b9ab | -2.80093 | -52.9026 | 2025-12-03 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README20.md)
