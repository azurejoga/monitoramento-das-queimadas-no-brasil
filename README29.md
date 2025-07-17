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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 842710ee-6957-3524-9589-8370574e042b | -11.94738 | -48.41975 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf62678e-342c-373e-a32f-e18a2b9739c3 | -12.41177 | -50.04882 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0e46f6-ce5d-3f83-9d25-0d94b41ff7a9 | -12.50097 | -57.78222 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9bf28f8-50a0-3d21-b355-79222efe0178 | -10.97165 | -46.47959 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ee11c7f-200d-3416-9d1b-777e6a717a54 | -10.81112 | -50.46801 | 2025-07-17 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b32dbe9e-4e19-36cf-897f-b4fc0893eb37 | -10.0555 | -64.99507 | 2025-07-17 05:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b22133-8732-3870-b771-8a47f8695c95 | -12.37657 | -50.37549 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e77b94aa-c304-394f-866c-bde6021b5439 | -9.02489 | -61.22252 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6bbc540-5a14-3510-8424-bca224247dcf | -9.10001 | -64.15587 | 2025-07-17 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fdc6e55-f53c-381d-85dc-d8931fa3e0c1 | -12.37583 | -50.3814 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de542ce4-f532-3fb6-a470-3c4c90c7c668 | -10.24227 | -59.27492 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd354023-1ed5-309a-af59-6a4575456b8d | -10.05956 | -59.10667 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d96c6d4-a42d-397b-a4c2-07f330672bec | -12.40348 | -50.4863 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50d0b778-affd-37bf-9bdd-55f0e45cbbfe | -10.12135 | -52.34855 | 2025-07-17 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff2e8899-e42d-31b9-9b1d-87549f8bb859 | -11.46045 | -45.10131 | 2025-07-17 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e580c594-4c74-3f10-a3f2-e4f0bb2d198f | -11.94722 | -48.42988 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94236f6c-2ca9-30a8-9e2f-26f3e4f9fea3 | -12.41731 | -50.04641 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64d76817-2d11-3fde-9c3a-eabfda05aca8 | -10.65893 | -49.47809 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2c23132-066a-378a-a68e-ab277c8c59ab | -12.09832 | -48.19539 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 923fb4f2-f84a-3bec-af7a-02d94c40f884 | -11.87458 | -55.44648 | 2025-07-17 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a8ebae0-1665-364d-8bea-842c630aef80 | -12.50152 | -57.77862 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa191003-03c3-34a9-9064-bc04bbc31788 | -9.17775 | -59.78257 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c5e82fc-b173-3f8a-b6b4-74e794ce04d7 | -12.48069 | -46.91688 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c09d9603-04f2-31ed-9797-d97e6f035dc9 | -10.97104 | -46.4847 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d54f33b-a6c1-3228-aa77-7141e07f840a | -14.9585 | -56.40531 | 2025-07-17 05:14:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 79beb037-7569-3a06-acdc-ad2d5bbdb77d | -20.99491 | -49.77006 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ed21ead3-3e68-3cd5-9b6c-863a77fe66af | -21.18492 | -53.18153 | 2025-07-17 05:16:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4f39127-44d4-37a0-a756-e8c3bb22935d | -23.06412 | -51.51786 | 2025-07-17 05:16:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 209ac8d0-fd07-3a52-bb14-e07a5d3dc61f | -20.00859 | -49.05482 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 429f463a-b214-3119-93f7-b52f5b6ee0d0 | -19.96364 | -48.99562 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 45517aa2-374c-3d1c-ba2f-12d49784c968 | -20.00901 | -49.05012 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54e5a850-fe48-31cc-8fc6-686ab92aa1d1 | -19.44483 | -48.54159 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6746837-95c2-3ad8-b06f-3db7e4b6b952 | -19.46354 | -55.44728 | 2025-07-17 05:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8853b3c7-fff0-3764-b447-49eaf133b041 | -18.65532 | -55.7312 | 2025-07-17 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 31721bc5-a3f6-313a-ab04-9b803a6337dc | -21.1857 | -53.1839 | 2025-07-17 05:16:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf548d63-3ec0-3026-9ed3-6877a864ff92 | -23.08486 | -49.73355 | 2025-07-17 05:16:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a7982468-d5e8-3cd3-9af1-3e86fd11c430 | -19.47913 | -49.29444 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4df440bd-d16a-3737-bbcf-1c6114275bc0 | -19.4502 | -48.53838 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 059cf6ba-bbf0-3f42-a680-277f367fc131 | -20.98966 | -49.7721 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b7e7726f-457a-3d93-ae56-ff15ff0e4ad5 | -20.42446 | -46.596 | 2025-07-17 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcf4f87d-bfa3-3b08-9b79-00569f32884e | -22.39392 | -49.78896 | 2025-07-17 05:16:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fa1de2c3-663c-3ec0-aa41-bbdef050803f | -20.98925 | -49.77636 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 04a78040-5995-39e8-87ff-4e124b0af5f4 | -20.01322 | -49.0539 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ef3d3e75-5de3-32d1-a457-530e599ed55b | -19.47955 | -49.28995 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d70d4cdb-03c5-3470-9382-83e292f09d08 | -19.47626 | -49.29294 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 199ef65e-8728-3d0e-b85e-1889eabc32e7 | -20.99593 | -49.7683 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a8ca454a-66a6-3277-a4d2-a2c81fb59c89 | -19.44397 | -48.53805 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9f36c7f-f9e5-3490-84cb-30f7aae69573 | -23.05874 | -51.51733 | 2025-07-17 05:16:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b06402c-1d6f-33c5-a4e8-d3dd94407a2f | -20.91332 | -55.75131 | 2025-07-17 05:16:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa1f92e3-ed5e-3d74-b575-ef1fd5857157 | -20.98944 | -49.76507 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d3940188-4fc9-3b45-8d93-024a09e7b4d9 | -19.48219 | -49.29356 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7c04e2-a2ce-389e-99c5-777d3a196309 | -19.95759 | -48.99479 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d174a7f-b94a-3962-a6c0-767d8427661a | -23.08824 | -49.73719 | 2025-07-17 05:16:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78515d32-f583-3d5a-89b1-4de3d0a285d2 | -21.0839 | -48.68596 | 2025-07-17 05:16:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac89d535-54eb-36b6-a063-c73083d76cc4 | -20.00717 | -49.05321 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 019205b4-d6a4-3eff-8ad8-116b58d740c2 | -19.44527 | -48.53704 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a264e3c1-b439-3d39-b05a-15a021cd5847 | -20.43155 | -46.59552 | 2025-07-17 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71b5d5e5-ad87-32f0-b812-946f39edcfba | -19.3154 | -55.15772 | 2025-07-17 05:16:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a7bd64d-e9d5-3036-a78e-dc3a5a3df316 | -19.31491 | -55.16143 | 2025-07-17 05:16:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efcc9f61-28ee-3bd3-b6f2-dfc2266135b8 | -20.98867 | -49.7738 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9930bd8e-0645-3054-b5a0-a9ed223cdd53 | -19.45956 | -55.4467 | 2025-07-17 05:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 05961549-6b3b-3a74-99ca-cb17a6ac651a | -23.08223 | -49.7368 | 2025-07-17 05:16:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 21492f8a-d80a-35a7-9691-e04217b1756e | -19.95801 | -48.99023 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5e28a16a-7f43-3c71-9e58-c56b59a3236b | -20.01506 | -49.05082 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1633d0a0-c69a-3aa8-9f02-8be0f80c364e | -23.06444 | -51.5144 | 2025-07-17 05:16:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3c6aafa-c379-3410-9dc7-29fb6fe4e76e | -20.00763 | -49.04849 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c949a48-f139-3e76-88ca-f545024461e3 | -20.99452 | -49.77441 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a2a34298-b9c1-39ad-9fad-00ebf585b074 | -22.39354 | -49.79336 | 2025-07-17 05:16:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 85171a68-c57a-358b-b6a8-491120bc20e8 | -23.51955 | -47.02135 | 2025-07-17 05:16:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 156b15b9-5440-3fdb-beed-277f87d25edc | -19.96408 | -48.99095 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e0c11823-45a5-310e-9ccf-4406d90c21dd | -20.01464 | -49.0555 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d082df4-35da-3c57-a35d-b99133ca39b3 | -19.95844 | -48.98558 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 34136ddf-cd24-3583-9d93-e8a0d35caa51 | -21.08345 | -48.69098 | 2025-07-17 05:16:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0105954d-0d16-3555-9b06-84b0de15aac1 | -20.98905 | -49.76947 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c6fce2bd-6d97-3044-a660-6bb8ce9ec01d | -19.4498 | -48.54287 | 2025-07-17 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03fadadb-db99-33e6-9c15-62e16efab551 | -21.08166 | -48.6865 | 2025-07-17 05:16:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8fcb7801-6090-3f19-af15-18f7dca6004e | -20.9953 | -49.76566 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| da534a66-dffe-34a0-b4ef-572716b91c68 | -23.0845 | -49.73809 | 2025-07-17 05:16:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 569f68ab-1a67-3942-a4ef-4a87d1fd0c69 | -20.00943 | -49.04539 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43bad5f0-d715-3038-a3f0-1105e2214209 | -20.01367 | -49.04922 | 2025-07-17 05:16:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1f771288-d2d7-3261-ab69-8d58ed3155f6 | -20.99551 | -49.77267 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 63462c80-f31f-375d-beee-da4ee93c7e95 | -20.99007 | -49.76774 | 2025-07-17 05:16:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1ff03fda-8829-30d5-b6e4-07e0f4144627 | -5.66693 | -43.72061 | 2025-07-17 05:18:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8dd76a6c-1485-3780-bc9f-05969641d4b6 | -6.97179 | -42.81222 | 2025-07-17 05:18:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 985bdb4a-eb00-37a2-a3f6-22e2c908a573 | -3.38384 | -47.45766 | 2025-07-17 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 07fe3d98-8ac2-3f9e-bb99-b430280a4dd9 | -6.97368 | -42.80002 | 2025-07-17 05:18:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 646cfa9a-8916-38c5-bb7a-ea32e438304e | -10.96163 | -46.45853 | 2025-07-17 05:18:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 01800a25-0d71-3255-a098-595146cadb83 | -7.34279 | -44.19803 | 2025-07-17 05:18:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c8ca281b-ebd3-326b-a667-b82e3117b396 | -3.37849 | -47.46182 | 2025-07-17 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 04e99cc7-590f-378e-a22f-856a19fa3ad3 | -8.87519 | -44.79324 | 2025-07-17 05:18:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9e4b0f3e-dbae-364c-b638-c9b64094d91c | -6.70384 | -44.30669 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3d1a9d05-1bcd-3a03-8aba-26dcc51143ce | -5.65566 | -43.71892 | 2025-07-17 05:18:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 263.6 |
| 3e6d656d-9291-3cdc-8aee-c71425dc7abb | -6.73141 | -44.33371 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f45af954-f848-33a4-8644-92a8fc1b133b | -6.71981 | -44.33188 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 203e3e0b-fef0-3655-8fba-5b9e7f1638df | -27.21143 | -50.66583 | 2025-07-17 05:18:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 078b4631-e8d9-3522-9acd-7d1d95940735 | -6.70137 | -44.32212 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| da32ebe1-1ad7-3322-9878-31cf89144ebb | -10.95826 | -46.47831 | 2025-07-17 05:18:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| c362670d-b272-37b9-97e1-3dd3f718b063 | -6.72241 | -44.31619 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 815345c0-58fa-3006-be91-a2ff5c854b10 | -6.96971 | -42.8062 | 2025-07-17 05:18:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 2ac3e5b1-1184-38c3-b30b-d4cec65f77e7 | -5.65803 | -43.70416 | 2025-07-17 05:18:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |


[Clique aqui para ver as próximas entradas](README30.md)
