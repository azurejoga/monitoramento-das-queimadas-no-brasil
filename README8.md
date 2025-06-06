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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8483af6-21ac-3d0d-a8c4-0b229b876aed | -6.20743 | -43.33795 | 2025-06-06 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43f52cdf-58b5-3381-8291-72216a26136a | -3.40729 | -47.58615 | 2025-06-06 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7578ea40-bb10-3965-a361-8aae5e976861 | -6.64328 | -47.35101 | 2025-06-06 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ff23eaf-1cfa-3800-96ef-3aa805287846 | -8.95073 | -50.0111 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b4bfd11-4ad1-388e-93af-a36aac4fbeb4 | -8.72806 | -47.98801 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ad5357-a381-36b7-aa12-5c760812b7a9 | -7.20143 | -43.13319 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e23a635b-deee-31da-8d0d-e401c9f1002b | -9.07647 | -47.14157 | 2025-06-06 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83b73573-ee35-37e8-a61b-82e9fcc6dafe | -8.72748 | -47.99179 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 397febf7-e892-38f1-8efe-eb7ed85be151 | -7.9044 | -50.35975 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 720c536c-362a-3b87-bc11-e1cce3e02353 | -7.01074 | -44.60421 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b254913-680e-383e-9c20-e92258b32449 | -9.21848 | -48.85845 | 2025-06-06 04:40:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99800623-670f-3878-a4b8-22697dd6cfee | -8.73209 | -47.98478 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 407c5e78-721d-3ab8-883d-4a54cddb0df1 | -5.69616 | -47.54406 | 2025-06-06 04:40:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 489ab505-7e41-32dd-b3da-a28e5d4e596d | -7.01126 | -44.60064 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb68b4cb-3358-3f88-a5fe-80cda289d889 | -7.01024 | -44.60773 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d15bb5c-347c-3c87-9f91-cb08384f942c | -7.01885 | -44.60539 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feb4e9f6-b7b1-33ea-bbfa-bc0e2a8213b6 | -5.47859 | -49.57467 | 2025-06-06 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30bc5564-9324-3f36-b63b-c2b22d2d7556 | -6.0488 | -44.16879 | 2025-06-06 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 327d0acb-6c1b-37a8-9086-a0dc549af2f8 | -7.1991 | -43.13393 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec3de0e8-378a-3d0c-bc45-fc53845704ba | -6.96277 | -42.90246 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a7a0425a-566d-3eca-8a4c-6bf571f4f887 | -7.73308 | -44.18142 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1851b58a-5eae-350f-b26c-778374d278fc | -8.74585 | -48.03319 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7da52e99-8155-3fc8-ae4f-68c25d4cfa0b | -4.1763 | -47.53447 | 2025-06-06 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bbfb683-af15-3f5d-a6b9-af6ef9eaa2bb | -6.33036 | -47.48258 | 2025-06-06 04:40:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82dd34aa-dd0f-3ecf-967e-38f6cae42088 | -4.59238 | -47.89172 | 2025-06-06 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ff6487-93ee-3201-bc41-a6a474c1cdbe | -8.4605 | -46.4827 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 836b7b31-7299-3885-83b4-96954a037af1 | -7.90662 | -50.36729 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ed29d62-ee47-37e5-ae1f-9c29a549c26a | -6.23372 | -48.55499 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdf03b3a-9779-3c99-a158-f148abb8a733 | -9.08006 | -47.14211 | 2025-06-06 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ae75c36-5eca-3f32-90dd-065f65b33a19 | -10.65847 | -55.3135 | 2025-06-06 04:42:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a71a84f-0e3a-3448-96e9-2f11787acddd | -13.51757 | -56.57409 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b3a1442-5c59-30b7-be81-e5574ca71571 | -13.51793 | -56.55928 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a1f313-db05-3862-9ad5-53362c58d449 | -14.22529 | -45.4889 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc09844-feb9-37fc-b181-d518c75a9630 | -13.52031 | -56.55914 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6905acf-8843-3749-b2b1-5edd95114fd0 | -14.02459 | -55.13556 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd51bb59-649e-3c28-a0c9-b8a0660732e4 | -11.5123 | -49.81783 | 2025-06-06 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb7e863e-c1d2-300f-9534-68f2dacca253 | -10.49125 | -53.66383 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5ecc17dd-0f07-3a7e-945c-1a8e91391b24 | -10.68336 | -57.59524 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633a996a-ca5c-3d33-8a1b-2cf17399557a | -13.52205 | -56.56004 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09244abf-3dbd-33d6-9c87-01bbe373761e | -12.9556 | -46.77637 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab69d925-ab62-3ced-af9f-811c13671b12 | -9.60561 | -49.01759 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 328ca5ea-ee8e-3bef-833a-d256f7cbbfa1 | -9.84273 | -48.60636 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f14a975-42c3-313a-85e4-07f3d71e5293 | -11.02672 | -54.24852 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 393e5c8e-044c-3f43-963e-5d9702edba77 | -11.78801 | -54.77081 | 2025-06-06 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8fac0f-a00b-36ad-82a1-86a0f413c86f | -9.66581 | -48.60159 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 595ccdb3-0779-3963-ac80-6c5424a3bd84 | -14.02834 | -55.13623 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e804446-9bfc-373a-800a-f18951758f57 | -14.22899 | -45.49349 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef1aafa-f675-3277-9663-b773e74fdb23 | -14.22952 | -45.48951 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cbdb1a6-8e51-3085-a1a1-bfab98a5a86f | -13.52168 | -56.57484 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98f5772-a1b1-34cd-a2c2-fbf18e2274ce | -14.04037 | -55.13376 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d682ca8c-fb86-367a-a3bc-b23e11249295 | -12.66277 | -58.21288 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 120cb511-6506-3ca3-a9a3-33100969dcdd | -12.52823 | -58.35698 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08c49539-3268-35a1-8081-46a9a24fc3df | -11.38835 | -56.55796 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0dfbe890-2c98-3231-9d1b-ba5a11c298f8 | -14.23376 | -45.49012 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9adf8a46-982e-3828-a997-aeec1e6a1b62 | -14.7363 | -45.09665 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e297a806-4a9d-3227-a0cc-5a749b4594c4 | -15.14235 | -45.5101 | 2025-06-06 04:42:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fa0c198-8b6a-3fa7-bf20-c7ac4402179d | -9.37713 | -48.55083 | 2025-06-06 04:42:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e666b64-c637-356c-8f61-4fa09eb10591 | -13.52139 | -56.56376 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5de3a17c-bef2-33c7-a47c-7db1270ff26d | -10.34793 | -43.30031 | 2025-06-06 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6cc583c5-c72c-3779-9e4c-8283e5d093cc | -14.73688 | -45.09232 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8298482c-99bc-3ac0-b046-60edae48ee0f | -13.52306 | -56.56732 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f946c912-9bfe-36c3-b6b4-105055856b01 | -11.38555 | -56.54909 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c5b4609-b348-3a1e-b86f-a7708c170190 | -10.99522 | -59.15345 | 2025-06-06 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 686d49e1-105c-3741-ac43-947aa82d8e3d | -12.84086 | -47.38733 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d692bb76-51c6-3f2b-94af-5536f748f440 | -9.84216 | -48.61006 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ca002e4-1dd1-3a85-b0f7-fd273c6d48fc | -12.66811 | -58.22046 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bfdd1a5-31b5-3174-b73f-9a0b539faec7 | -10.47042 | -51.89101 | 2025-06-06 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a6045ae-93f9-3c29-8685-ea39b10dc106 | -11.13274 | -54.21908 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3bb547ca-7343-3a3b-b984-0830857e69c8 | -11.57642 | -47.4404 | 2025-06-06 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea8b36f8-80d3-3020-a2de-8b965e5f2771 | -14.66829 | -53.12056 | 2025-06-06 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0540b84f-1af7-337f-b892-d01ed509cfe1 | -10.65167 | -44.49648 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1afed8d9-909a-3021-b93e-c9240e9fd4b1 | -11.02472 | -45.23808 | 2025-06-06 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ff876d5-7638-3aec-8742-098914811930 | -11.38907 | -56.55395 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 791b965b-5801-3de2-a6d3-b96c22ed0654 | -13.52008 | -56.57123 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08047026-eba7-396d-b38c-ff326a352a9f | -10.99303 | -49.01774 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90012fd2-f884-3636-8fc6-9d262e616683 | -10.81548 | -56.96179 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd0b780a-34c1-37a8-985d-088a68b9f552 | -13.51316 | -56.56227 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1cf9d05-022d-308d-a3da-1e193a3dd91d | -9.33854 | -49.5449 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 937289e6-26f2-38d5-96de-5d43045c2ca8 | -11.53495 | -56.43948 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5627dd10-fe71-33fd-af4a-9205b990eb40 | -12.67115 | -58.21971 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 156c7c79-63e8-364e-88cc-3687d1c86fa1 | -9.66938 | -48.71512 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d3ee6cd-5611-3f8d-b1c6-4dcdb6ee1dde | -11.38482 | -56.55315 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc6f4a24-4d1d-3fd6-9278-c93d3f70f04f | -13.71511 | -57.48113 | 2025-06-06 04:42:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b52b18dc-6db8-3f7b-a945-9a092a523fbf | -11.57215 | -47.44415 | 2025-06-06 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0eb4ffc-a12d-30a0-8d42-d3c24218a368 | -10.73628 | -47.61116 | 2025-06-06 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9433834e-7c20-395d-9966-d488f76ebe15 | -11.37683 | -54.35044 | 2025-06-06 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70d6751-fc1a-3713-8310-ab0466a2553d | -12.95626 | -46.77163 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d09f5c1f-b7bc-393a-84d8-e920c8c77ee4 | -14.92997 | -45.98697 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a7248a-8af4-3b2d-aa1a-1f4449c5dd0f | -10.14721 | -52.13792 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d3c6d91-64e6-3f66-95bf-20fc33524430 | -12.15777 | -43.20322 | 2025-06-06 04:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1a53f357-2b19-35cf-96fb-28e701c7c28a | -14.22106 | -45.48828 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4313ea7-f400-3adc-b614-1d766f343f7c | -10.14378 | -52.13736 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c3cc34-7d4a-3e09-9479-61055751217e | -13.51894 | -56.56658 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2325bc39-8af8-3d63-a63b-24fe6e8102a5 | -12.83715 | -47.38679 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6ec7e0f-f7af-393a-8262-a0058f2167b2 | -12.66348 | -58.21951 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7af39749-5115-3dfa-90de-e336d2f336d9 | -11.70977 | -56.45343 | 2025-06-06 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 353c4fa2-ed18-35de-97fc-3d4ba5d8ab25 | -12.96328 | -46.77747 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b43036d-4e42-36be-b552-515414c17102 | -13.07343 | -49.25062 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a022bfc-00fd-3946-839f-10f9cbd41c9b | -10.49196 | -53.65957 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1dc59771-8811-35c3-8242-286fc5027b32 | -9.54625 | -47.77283 | 2025-06-06 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
