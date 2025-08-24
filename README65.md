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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c07e3d7d-3afc-3029-b323-c438b802d802 | -9.04347 | -65.71948 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b5cc10d-215b-3b1f-b5b4-5682b4ae5ab5 | -14.53877 | -53.23708 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2758ccbe-db5c-398f-9a2d-e042ac673f0a | -13.43463 | -47.03421 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8a727b4-706b-3abf-a956-9b068b9438c4 | -10.34736 | -58.59872 | 2025-08-24 05:01:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4c078ee-ee16-3d9c-8915-735638facbd0 | -9.51349 | -60.51201 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cff6c8b-131a-3dab-94c4-701088219ffb | -10.04985 | -59.35925 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 527c23c5-0391-36a8-a992-31c0e15b3686 | -13.47276 | -47.02169 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ebe918f-7591-3c6d-9ea8-9d158ca8aee2 | -9.64844 | -59.64603 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c90c0662-ae7d-35e3-b1f3-630744d0a3a2 | -15.30012 | -56.16385 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6237b50d-fb38-3baa-ae39-460df5600457 | -15.05272 | -48.52142 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc0032d-cb4a-3c9a-8f08-1e7854596e45 | -12.72873 | -48.13615 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 547d932a-fb7b-3f33-9a32-1a0687e49aec | -14.51139 | -51.92184 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca481005-dbae-3df3-9f7e-63b025e6cac8 | -11.70708 | -60.19058 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7861bb3-5dc2-3659-a450-481fd7412e8b | -9.65026 | -59.63534 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a9ad519-e292-3fd2-8632-577648633fa3 | -15.31845 | -56.1559 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 156a2e23-034e-3bbc-b18b-86b9c740c113 | -14.98441 | -50.17672 | 2025-08-24 05:01:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd97b0d8-e5c8-3115-ba52-8926baebb617 | -9.65242 | -59.64673 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75a943f8-ae20-33a8-b178-43001a33a766 | -13.35688 | -47.50039 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9039fc4-ea88-32dd-8992-bab7d4123f18 | -13.47211 | -47.02692 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9acd91c4-f942-3623-8d0a-e6c85a5d6536 | -9.023 | -65.6967 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88e92452-e45e-372b-8293-4c6e925d293b | -13.48799 | -47.02538 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 877330bb-b132-3eb2-b82e-63fc50d96fb4 | -11.1831 | -55.03382 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0fb38a-9081-3b0e-97d8-7705ecababca | -9.52058 | -60.5214 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de31466f-b8c4-3f39-83fc-ec1af37d988c | -14.29046 | -60.37755 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c26f52c-aa59-32da-b439-8f63ee7ff366 | -13.17168 | -46.92265 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 778baf49-c0a7-3456-b5aa-11d93a0622c1 | -15.67456 | -53.87732 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34e0cbb8-7dd8-366c-ac65-f6d211bcdafb | -11.73319 | -51.69413 | 2025-08-24 05:01:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 017082ad-eac5-3c90-8464-b9c89d3819d0 | -14.2806 | -48.02715 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 523c0755-c4a2-3549-91df-9fefed956e67 | -13.41157 | -51.79185 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6133490-dd03-32b0-ab98-1c71774004c3 | -11.67406 | -51.59625 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f7e9f8b1-45fd-3338-a781-20b532d96e9e | -14.28652 | -60.37719 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 122c6185-2ee1-3494-916a-315581d4b2c2 | -11.52867 | -51.85155 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| dd58a86a-e96f-3206-aae0-e51a04dc1cc0 | -13.03346 | -45.21584 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9940e4a-f246-3308-8bb1-73725d90994d | -13.04983 | -46.32607 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef3b31be-2b25-326b-8e27-177305e0592d | -12.99698 | -45.22776 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c947c10b-ebe8-39a9-bdce-2f99b33832dd | -9.52413 | -60.52611 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b339f814-6784-34b1-89e4-4d8152e1271f | -11.94111 | -46.73129 | 2025-08-24 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3520c56f-f3ce-34e5-b04e-6e6d9a6dfa48 | -12.99169 | -45.22297 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33412b2a-c6f5-362b-998d-ce27fa0c9f41 | -13.6653 | -47.99032 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695f2ec1-e84e-3ccc-bbba-a6b93aca3fff | -12.72805 | -48.1412 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d089e35a-ca14-30aa-9be5-6bdbab588fb5 | -15.92272 | -52.20999 | 2025-08-24 05:01:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7709c443-f41e-3752-af90-dbbd2bbf2317 | -8.99822 | -63.63908 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a16d931-881e-37d1-a578-55daf14696fa | -12.72341 | -48.13995 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89090272-98be-30fa-a044-276ea4c654dc | -16.79571 | -51.35033 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 31d632c5-9722-3174-833e-88fe5fdbe2a0 | -15.67805 | -53.87786 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f27a035-bae6-38d5-8180-725686a43bee | -15.53196 | -54.75633 | 2025-08-24 05:01:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a122dee-4554-3d1e-82b6-ff2d177c1f3d | -15.29459 | -56.15557 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5ace5d0f-7bef-3b92-91fa-c3cd092054ec | -9.45322 | -63.50832 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 675a420a-6cbc-3f36-a991-15341b2cab56 | -9.19042 | -64.55577 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e05499-41ef-3ca1-9a8c-2f0cd45204cd | -9.00755 | -65.7124 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b3f1b89-abc0-3a52-b01d-0f5ba30e33f4 | -14.29811 | -58.49715 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f9e8695-9048-3d70-9813-8894c3b92012 | -14.37748 | -49.16533 | 2025-08-24 05:01:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 069379df-991d-3acd-b85b-65c2f5f68a77 | -13.02655 | -56.87908 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be7afdd8-8767-3a31-9a2b-c6b398efe46a | -18.39769 | -46.8468 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbb1e228-9dff-33fe-bd1d-f6a51cfd87c2 | -14.80031 | -59.62956 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a04f1148-79a9-36f1-a466-6cb2b7c7a6e6 | -13.48793 | -46.89998 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ced2fbdf-121b-3935-a67c-09fcb90f12d2 | -16.79907 | -51.3514 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25512a81-71ed-3797-ab5e-94b972994aef | -16.49288 | -46.75429 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 371fca90-17c4-3a45-a750-493f69d1cd83 | -12.58987 | -60.35531 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27f63e53-2be7-3b2a-8d89-6e6208d70ac1 | -9.00504 | -65.69326 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a14c4ea7-c047-3353-8225-40ddc1e2e10e | -14.33835 | -58.59863 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ef70c40-633d-3ed7-a9f2-2626d6094e7c | -13.1713 | -46.92573 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a02f5d9-0bf4-3873-b86c-cbfe0b098067 | -13.48267 | -47.02613 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb87e6c-f775-3e8b-9a1d-b748e0396cb0 | -9.52305 | -60.55437 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79a1080a-dfbb-382f-82e1-d1a2365727b9 | -13.03203 | -45.22794 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1542070a-41af-3aaa-902a-cc310a821b31 | -15.31456 | -56.15892 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ca4d404-6cad-33d7-afbf-456b452231db | -15.32787 | -56.16116 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8618df40-809c-3a61-b77c-a15d77546fdc | -11.51329 | -51.8799 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53b20538-fab7-309c-b62c-097bbef90573 | -9.01777 | -65.71424 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96cac079-5fd6-3aab-9d37-42854013a5eb | -13.45671 | -47.02464 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf542479-32be-3061-9f18-68b1bd102886 | -11.18421 | -55.02679 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ba7226-d701-38fd-bd5c-d446cb1ba766 | -11.18365 | -55.0303 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c331f8b-2e75-3028-8d74-956cb0670aef | -14.50761 | -51.92128 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4203cb77-1c31-37eb-8e28-e0c33bd5d04c | -9.01443 | -65.70892 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 79e6d1e7-6651-3679-a8cb-c16c9b26b5b4 | -14.81088 | -47.92165 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1d96cfeb-8fed-3eb3-a30e-5e1a89ef60c2 | -11.54144 | -51.86657 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5d6f138-7f10-3e13-8d9d-e5e4a338fe31 | -9.01095 | -65.71753 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81527ea3-fe4a-369e-bec7-22adf334709c | -14.51824 | -52.03728 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc6fa370-cf3d-3ba7-b2da-da500180131e | -12.72522 | -48.13693 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25f084ad-05da-37f7-83b7-88cec69c872d | -9.95128 | -60.18388 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e0ed29c-df05-3181-bd57-ebfc1afe633d | -13.43494 | -47.03168 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf0de181-a9da-35c4-ab61-1ea74045442c | -14.29741 | -60.38357 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb99f3c8-0d4a-3df7-9fae-88af8d42cc7e | -9.03235 | -65.71268 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d748e15-6a48-3dbd-9dec-7adc1d360575 | -9.8215 | -64.2635 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 626b638a-472b-3112-bf2b-5ff011321788 | -13.4516 | -47.02368 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1991b06-0c83-3f7c-80f0-c2c4354b5ed4 | -11.83381 | -55.21453 | 2025-08-24 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f4dab43-dcb5-36bc-b1b3-d41a110342fc | -9.01355 | -65.7135 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8a264a4-7b1c-3a21-815f-0d9960617338 | -13.62796 | -48.16833 | 2025-08-24 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4da5f16b-a9bd-35d3-b70c-b6307d08f565 | -14.77148 | -55.41629 | 2025-08-24 05:01:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ec26971-5154-3160-a499-da1ff3bdd333 | -15.67573 | -53.86946 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 897eb792-4d9e-371e-a993-e0795c19f69c | -11.18143 | -55.02273 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec97909-68bf-3dc9-9d53-f7f189976c55 | -14.65491 | -56.57824 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d7b6c77-d3e8-3244-ab8f-35a012c86cbc | -14.49523 | -53.0973 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5fe92c7-ecb2-3645-9419-f2f79d5d4662 | -14.33129 | -58.59734 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74a60e4f-c064-39af-81d5-e3e6e04de9f9 | -12.49398 | -53.82758 | 2025-08-24 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd3ec9d3-cdf2-3ea5-a92d-6c3dc76e8053 | -9.95474 | -60.18828 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e93115-40d0-3798-ac47-dc294143adb2 | -9.00621 | -65.38219 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c4a31e1-3907-37ac-b554-4641c6944359 | -12.733 | -48.11338 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92b6a32b-2018-3d38-9201-8bb86f2ae2e7 | -11.17811 | -55.0222 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b11ad730-3b3d-3b41-a912-9568d9bca4aa | -12.72406 | -48.13511 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README66.md)
