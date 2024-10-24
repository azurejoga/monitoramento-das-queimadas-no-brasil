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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea65bc3-f4dc-382c-8f0d-96322dfb9ea6 | -19.57253 | -56.68685 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 9260dd69-d01a-3fcd-90a5-416f14408c4b | -19.57033 | -56.67891 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 1faa7124-7d97-3bee-aabe-463d48f5c8d4 | -19.56976 | -56.68259 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 25495780-944c-392b-b074-a69873d087d4 | -19.56643 | -56.68202 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| a594ccbc-b03e-3f00-b9d1-ac1c9ab63c9e | -19.56545 | -56.64404 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| bb409724-465a-379c-b6dc-ff63b3a41295 | -19.5626 | -56.66246 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bc9df0b3-c96a-3ea8-969a-693173ff6fe6 | -19.56211 | -56.64347 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2826474b-04f4-3fa1-8c58-b95fa4e31a48 | -19.56154 | -56.64716 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 394356b9-cf36-351e-b491-a50c8dea13f1 | -19.56147 | -56.66983 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6a73b49f-f84a-3a00-a727-a98e638ba4fc | -19.55878 | -56.64289 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2fd52c07-05f9-39c5-b578-76219c0278bd | -19.55601 | -56.63864 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a748d70b-95f9-3d88-8e36-5613881ec5f5 | -19.55472 | -56.69134 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9278c9ba-a92d-3823-bd84-cab97d33d32d | -19.55423 | -56.67236 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 24d4823b-9db9-3580-9377-d36d614cdcf6 | -19.55309 | -56.67973 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b1b399bb-d35f-33d5-b3b0-8808ea088229 | -19.55025 | -56.69813 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ba30c5a5-8385-33bc-892b-8b330afb7eaf | -19.54976 | -56.67915 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 78bf1062-2baf-37a3-ad63-ebc7f7c8ee7c | -19.54968 | -56.70181 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97420d6f-27df-355d-b652-4ad20e5512fa | -19.54919 | -56.68283 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fa1bd0a4-3af8-3fd6-871a-caab7825577d | -19.54862 | -56.68651 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 876ee9f2-e91a-3c37-8692-f9f996ffaec2 | -19.54585 | -56.68226 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e0d6ff09-dc5d-33e9-ac2c-85dbef467396 | -19.54536 | -56.66328 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a5219d9-7b8b-38c2-99df-4ea282384552 | -19.54365 | -56.67432 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e01eb20d-e378-39ce-9f94-cea72dacc201 | -19.54202 | -56.6627 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6db5f3d2-1f6c-33d3-8583-19446c3e98ca | -19.54096 | -56.6474 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f831424f-0d7c-3f9c-9578-da9cb9bd3601 | -19.54032 | -56.67375 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a46f9e99-7882-39a3-ae2d-f17b98872374 | -19.53975 | -56.67743 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 685185c8-2d7d-3cb8-982a-2e8c9060edc0 | -19.53926 | -56.65845 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d97b05af-88f5-366e-a694-eac86e0a3db6 | -19.53812 | -56.66581 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 900add3e-01ae-3124-af72-e532cc07e113 | -19.53592 | -56.65788 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 20c4cdc1-436c-3932-91ba-4646bfc6d3d1 | -19.53528 | -56.68422 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0974625f-2796-3a36-a575-ace5ac81ab9b | -19.53422 | -56.66892 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| baa5276f-729b-3353-8c5e-761b521dc62a | -19.53415 | -56.69158 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 829cbbc0-2c06-3a81-a2a8-c1db24228dbf | -19.53202 | -56.66098 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e1913072-223b-3419-8b7d-433bfa494092 | -19.53088 | -56.66835 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| f06c6f3e-5c6c-3f49-abff-f042de65a152 | -19.52812 | -56.66409 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb1fc663-f0ef-3106-b997-2b29c16e3bd2 | -19.51904 | -56.66699 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5938097f-8370-3db8-8116-b5a53ff7b5a1 | -19.50912 | -56.6426 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c7adbb9d-dda4-36aa-b491-0eb5786399cd | -19.50847 | -56.66895 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 92ed5d12-fa2f-3330-9f61-7619bcbba2ce | -19.50636 | -56.63835 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7dbe0785-b328-3708-9e88-15d4958cca87 | -19.50513 | -56.66838 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 745b5315-1349-31ed-a037-ee53a0ce2718 | -19.50245 | -56.64146 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 544b0a2e-235d-3d1b-bdde-85e6a0021d00 | -19.50131 | -56.64882 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5eda37a4-63b0-3509-96c5-7bd4b976c975 | -19.50074 | -56.6525 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c5d8ccef-035d-3e36-b8b3-fdc604d3b3c3 | -19.50018 | -56.65619 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| bfb64ce1-8d3e-33d7-a7a8-26a076891564 | -19.49798 | -56.64825 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3814541e-d45a-35bd-b2a7-b5910c62325e | -19.49684 | -56.65561 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 547e5a5f-b228-3ac2-b32e-b507f3c9885a | -19.64328 | -56.79684 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01836cca-420f-3ce9-a0f3-5cca40aade17 | -19.64318 | -56.81948 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3e99faa5-d519-3514-9717-da9b4e8cd448 | -19.6428 | -56.77782 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dc4b3d46-4cff-3bad-af84-18292c2d4454 | -19.64271 | -56.80052 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c240fc11-9ee9-338e-88fb-a99a92316a5a | -19.64261 | -56.82315 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 151d9b94-4589-30e9-b378-2c9c2114dc78 | -19.64252 | -56.84579 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 5f9a78bf-ea5d-34a3-80d9-cd712f41b167 | -19.64214 | -56.8042 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eac0b0f0-b334-3d7a-809a-c5811b0e1a5f | -19.64195 | -56.84946 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 0c91af3e-3c35-3f1e-9239-14321e278c10 | -19.64166 | -56.78518 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ab26156-fbe6-3a17-bc79-3507993235cd | -19.64157 | -56.80787 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a911aff8-a64e-3836-8e9c-8463395ab21e | -19.64148 | -56.83046 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c0a3fc9c-1045-3c77-b1ed-bfc57231a747 | -19.64138 | -56.85313 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3307cb80-7bed-3a48-b27f-273b60d7f62c | -19.641 | -56.81155 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 92314b36-b313-3cb8-870b-2b3177776b0f | -19.64091 | -56.83413 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 37818f07-043e-3879-af31-460e2a9265e6 | -19.64075 | -56.98877 | 2024-10-24 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 21d76b05-b033-3078-8446-9dd51482dd77 | -19.63977 | -56.84149 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cf36f442-b001-3c09-8086-fb66a6de7fc8 | -19.63938 | -56.79994 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 953dc6b5-d605-37a8-bdea-7a97824ea9ce | -19.63929 | -56.82258 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9101b427-fcb7-38fd-a12e-ae7e56fda0c7 | -19.63919 | -56.84521 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 84f9e651-3b72-3763-bdb7-5b0c4e521749 | -19.63881 | -56.80362 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c71ba4a-9bc5-3e68-9b8b-982a7fc91b44 | -19.63872 | -56.8262 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8d66fd38-bea4-3f17-83af-47205b941a3a | -19.63862 | -56.84888 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aeb88b93-8e68-3ac3-828e-4b1979e65457 | -19.63815 | -56.82988 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| adf4d0a9-4a3c-3c6b-9e3d-4ca8329e6555 | -19.63805 | -56.85256 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cbcb4a1a-19e6-3362-a08d-c4b1170fdcd3 | -19.63766 | -56.81097 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 080baad6-eb0f-33d3-b91a-637df7a4a03f | -19.63743 | -56.98819 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b694028a-d0a4-3684-8b12-5a782ded7cea | -19.6371 | -56.81459 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 841b000e-3214-3176-828a-957808eaddc2 | -19.63653 | -56.81828 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 67098a94-a19c-30d0-8f76-244c06d45a89 | -19.63644 | -56.84091 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2e89ce0f-ba37-3fe1-a9c3-70117e312a6e | -19.63596 | -56.82195 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ce51cb4c-3eb0-343c-8a26-9a67198216df | -19.63539 | -56.82563 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 840d5fd9-c0ba-35bb-a0fe-728fee47a0af | -19.63529 | -56.8483 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3a12e96-04fc-3e2b-a12f-15ebcaaaaf1a | -19.63482 | -56.8293 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 11516e3e-62b6-307b-8c63-527c184b8377 | -19.63472 | -56.85198 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7ab81c10-64eb-3b92-adaf-08ac1a03df34 | -19.63263 | -56.82138 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cd4bf0f7-4fa1-353e-94d6-2f73484c6c68 | -19.63206 | -56.82505 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 368f7c9d-49e5-334b-aab8-9f1d3ea4c244 | -19.63196 | -56.84773 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e16af9e1-d40f-30b0-91d4-1c8d5805f7be | -19.63139 | -56.8514 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 43e7f5b4-2645-3265-b9c6-9e8f04a39083 | -19.62863 | -56.84711 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3ad543ee-136f-3af6-a78d-febe1e797438 | -19.62806 | -56.85083 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9b9495b0-9cb1-3561-a43a-6a2edecc1793 | -19.62614 | -56.77494 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c5aa9914-1ead-3435-8d70-25cd0d967cf0 | -19.6253 | -56.84653 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5714025-639d-3674-9a98-7c7f473f55c9 | -19.62254 | -56.84228 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9b3b03d9-ad79-3849-b865-99d524ac124f | -19.62197 | -56.84595 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f611adc2-41d8-3d71-bf30-b62887e5172b | -19.61169 | -56.91208 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f91e6d85-b25f-382d-9a45-9dc743357b46 | -19.57683 | -57.00402 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6302fc92-79bc-3e84-b6f0-2aaaee3de486 | -19.72411 | -56.73899 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 61ce67d2-a5b7-3d09-9995-0da9d9fc3f2d | -19.72078 | -56.73842 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 128fa284-74e9-3019-a35f-a2bb5def0596 | -19.72021 | -56.7421 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2fb030db-287f-3170-8739-5df9a1bad340 | -19.71687 | -56.74153 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c1b164cb-852f-3892-ab07-2a332e6fe4ee | -19.71468 | -56.73359 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d320b5bb-01c8-3647-8a8f-be959f36596d | -19.71411 | -56.73727 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1dc23af3-b3b7-3666-b870-6607cd36eb43 | -19.71354 | -56.74095 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf02a6da-230f-307a-806d-04da44a06283 | -19.71287 | -56.7673 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README84.md)
