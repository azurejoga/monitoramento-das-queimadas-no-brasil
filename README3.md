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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 546fb630-c263-36ea-ad1d-ef1828a69234 | -10.3125 | -46.7813 | 2025-08-27 00:22:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 195c7d61-d132-34c2-8fe5-e3ece81a3d45 | -6.454 | -44.5522 | 2025-08-27 00:22:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ac12992-b70f-3410-94af-de4b6208b5c1 | -8.4519 | -43.6604 | 2025-08-27 00:22:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfe07658-ba23-31f7-8758-6176b73d6a6c | -13.4051 | -46.895802 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4cc84630-2012-3be9-b64b-9cda7384f064 | -8.6859 | -47.193699 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c3f438e-1c27-395a-bb44-228b04cc3437 | -11.3787 | -55.340401 | 2025-08-27 00:22:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27d437fe-ee0f-3dda-beda-5d3151d0252e | -9.1685 | -59.527901 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2c88468-5c4e-3f3e-bfc8-8ce421d3592e | -6.6257 | -53.311501 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2fe30f4-f568-3754-b92d-bc3a4c5bbad2 | -15.6414 | -52.719002 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e68c7455-89af-3437-a761-260c53da0a9c | -5.5376 | -44.245899 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce0efa7-aead-34c6-b138-f4609b1043eb | -9.1588 | -59.5298 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13c1a83a-8cd9-3475-94b6-fca30206280e | -10.1222 | -47.425598 | 2025-08-27 00:22:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| deb2cc42-546d-3074-a83a-3d46590686fe | -11.0372 | -45.136002 | 2025-08-27 00:22:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 791076f4-3433-3712-ba19-bcbad3a4996b | -9.1374 | -50.758999 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7069b8e-d471-31a5-bfa5-ecb99ded5bfb | -21.0956 | -48.822899 | 2025-08-27 00:22:00 | METOP-B | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd5724dc-39ad-3ec3-9bde-d847ac75fccc | -8.8972 | -60.696999 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec33e88a-02bc-37ee-a843-7616cfb232a5 | -13.8284 | -45.881302 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51fb602c-f8b3-3d5f-9cd0-2bb6feb0eaa5 | -7.7402 | -50.268101 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 090f0826-dd91-3178-8630-4c890fd77929 | -7.7104 | -45.763599 | 2025-08-27 00:22:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee79b888-9558-3639-9dcd-81aa69698154 | -10.4938 | -51.592201 | 2025-08-27 00:22:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da21c009-93f7-3e49-b994-6d82e25acd7e | -9.0816 | -49.546299 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6702b9b0-656a-3a99-86b7-6c6e14cb88fc | -13.4291 | -46.9991 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 69d927c9-6a6b-35d8-a537-34d3b42125b2 | -7.5631 | -47.465302 | 2025-08-27 00:22:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 034cdbb5-6c18-30c6-9716-7a9270fecb20 | -15.1939 | -49.525299 | 2025-08-27 00:22:00 | METOP-B | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aaa82f64-5571-31db-9526-58efc14565cd | -9.5879 | -55.365799 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8feda80c-fb5a-3d60-b742-f0c5b11ae731 | -5.1171 | -43.218498 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e28ba94-2b2c-39f2-9ab9-f642411498a9 | -11.4562 | -47.304298 | 2025-08-27 00:22:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 836ced66-7ebd-3b64-a7b5-50e928aa06ee | -9.0848 | -49.560299 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 842a04e7-772d-3754-b149-c54f2291b8f5 | -5.1088 | -43.184101 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2fe38a3-ad5b-351d-8a19-152022e23ffd | -7.3523 | -57.599602 | 2025-08-27 00:22:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9831327-29a9-32cf-a6e0-bcb1b5780cd9 | -14.9129 | -49.604698 | 2025-08-27 00:22:00 | METOP-B | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 812ce098-0f5e-3adc-b9a6-bb47b27542bd | -6.9591 | -44.084702 | 2025-08-27 00:22:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 343e859b-6f53-3454-9e05-fa2f12b5b527 | -3.4207 | -49.034801 | 2025-08-27 00:22:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7fc3fd-28a2-3e6f-9b26-a539821636e0 | -6.6372 | -53.317001 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f994af3b-cd6c-35fa-969d-c024a990ee68 | -13.1655 | -45.266899 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b56d46a3-fd77-337f-8fb8-b44fdf5a970b | -15.6254 | -52.741299 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74b65df1-e0a1-36a9-bcef-7eb442d94ff1 | -11.8111 | -46.789398 | 2025-08-27 00:22:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 867ca964-fef1-3daf-bc36-e5f35fc5febe | -8.566 | -51.337601 | 2025-08-27 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d3d597-fe8d-396d-b022-ebc12c4b49e0 | -5.0991 | -43.186501 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28df2a30-8109-34c0-a889-0c3cf40eea0c | -12.729 | -48.174198 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86961ddd-c92f-3062-bd66-34dc968ccbad | -9.0766 | -49.569599 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 458ce493-369b-3a57-89c2-753a586ab9b0 | -10.7147 | -47.311001 | 2025-08-27 00:22:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ef70a8c-ed6a-3eb3-ac80-2cb21b7be658 | -15.6609 | -52.714802 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a42bf72-0521-3ec4-bec8-7ebabf04f0df | -9.2663 | -50.229301 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17463df3-904a-388f-ae9c-abf662ec6e1b | -9.1762 | -59.465401 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7fb614-cf34-3144-8af3-ef6da0edff90 | -12.7926 | -48.136101 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c4bae12-1d58-34d1-8eb1-17d47c41436a | -12.7486 | -48.169601 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df333ad0-8ab4-34dd-b32c-7b4459f5f3d5 | -10.6065 | -52.3009 | 2025-08-27 00:22:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a966be94-0f43-3fd9-be67-c61cb1876eb4 | -6.6388 | -53.324501 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8926002-2832-3f90-a8a1-5d53f742bd63 | -20.987499 | -44.317902 | 2025-08-27 00:22:00 | METOP-B | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cee6a73-3faf-391e-902c-cfec469c506a | -8.9015 | -47.321999 | 2025-08-27 00:22:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17936df4-fc35-3327-9f1a-3de9b0962307 | -13.1116 | -49.3237 | 2025-08-27 00:22:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c141596d-07a3-34bd-b285-a18871b44907 | -12.7536 | -48.191502 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a74767f7-191d-3db2-aaad-ea5f5c8de0bf | -12.7941 | -48.097099 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 315c57af-7136-343b-becd-1418f8b6376f | -13.4069 | -46.903702 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2aafced1-fd9a-381f-82ad-64937f16ae21 | -12.9302 | -46.322102 | 2025-08-27 00:22:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e691706e-4915-3ca5-b4b4-cb208b43bfe0 | -10.5984 | -52.3106 | 2025-08-27 00:22:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b70ab79-949c-3915-b8be-aa646e97132f | -9.106 | -49.562901 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d35380d-1628-3bdc-aded-0611b6a8ebff | -4.4852 | -47.6581 | 2025-08-27 00:22:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d75665-1089-3002-a41d-3cd362ce28c0 | -9.3043 | -48.261002 | 2025-08-27 00:22:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83c2e1f0-f918-3a08-b645-e4abc2a28b29 | -17.017099 | -47.942699 | 2025-08-27 00:22:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2635d7c8-772c-3a9c-952d-3a36f584bd64 | -21.111601 | -48.850498 | 2025-08-27 00:22:00 | METOP-B | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd88cda8-74a4-3b71-bc13-5c73d0cd02e6 | -8.8921 | -60.722401 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42498a15-b703-3e84-b070-637ad85ec27c | -8.5546 | -51.332802 | 2025-08-27 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 945816df-73e5-37e6-b8de-51927e107f43 | -8.8659 | -47.169399 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b283fc71-aa0c-38b7-bf66-26561a845538 | -15.6529 | -52.725899 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5003dc62-bcd4-328a-8d81-d2b4a56b483e | -4.4932 | -46.360401 | 2025-08-27 00:22:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7bc373-a9f3-3ef4-ad51-90b70edbd21b | -12.7859 | -48.1068 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26dc23b8-0e59-34ea-b851-3fd1e5219123 | -18.145399 | -44.425098 | 2025-08-27 00:22:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ecb8c4e1-d583-34d8-b1ba-4f46ec93e221 | -10.3145 | -46.789902 | 2025-08-27 00:22:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07c9a976-bb46-373e-8393-f3bf8a7949db | -6.3625 | -55.7803 | 2025-08-27 00:22:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f69ab9f-485c-372c-9595-0960b89b4fc4 | -7.7546 | -50.286701 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb9ab26-6906-34be-b46c-45438082502e | -6.2407 | -59.959 | 2025-08-27 00:22:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8057a4a3-86ad-36ba-8f18-d7c46ef8f43b | -3.4189 | -49.026901 | 2025-08-27 00:22:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a526161-bd16-352d-ad5d-83902eb26243 | -6.2447 | -59.978001 | 2025-08-27 00:22:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 317bcb2f-e446-32d0-bf4b-73904fb9dcd2 | -9.2808 | -56.883099 | 2025-08-27 00:22:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29c3db26-745d-331c-9264-55f70fedf083 | -8.2527 | -45.097198 | 2025-08-27 00:22:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4176d387-5c2e-3d71-92e6-e67eac75a590 | -9.4221 | -60.449299 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe571430-a639-3cbb-9e79-11a71efd69b8 | -9.4079 | -60.4282 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c222ff20-95d9-3c61-9510-d8e893787977 | -21.5917 | -47.483601 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d9d8688d-fedc-34ee-8ddb-dff93e9aece5 | -9.5933 | -55.3428 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fba8c954-f945-3871-9981-a13b911a06b0 | -5.1268 | -43.216202 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7f752c0-54f3-3952-9454-90deb06ccf3e | -12.7632 | -48.143002 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95e6eb27-44d9-3f7c-af0d-398f86f477e5 | -9.0846 | -49.604801 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec86938c-9a44-328e-a14b-ad3401cdd435 | -3.7407 | -49.037498 | 2025-08-27 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1736d2c-9a62-308c-9630-efaead37ca89 | -16.708401 | -50.405899 | 2025-08-27 00:22:00 | METOP-B | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3683d5b-d6c5-3f29-817d-2a832cd8ebe9 | -6.9247 | -52.848301 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbe94b2-029e-3909-9180-e24b31d852a0 | -7.7562 | -50.293598 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af25acf-fe89-33a7-8cb3-c5fc405b5857 | -13.639 | -45.692299 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f10208e7-c036-3d8e-ad53-eeb4265cd17c | -16.498501 | -49.471901 | 2025-08-27 00:22:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e986f15-bf6f-34bb-9846-89be43f11b0c | -7.2575 | -57.633499 | 2025-08-27 00:22:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb58ba6-a445-359c-8eb1-a4193fec10ff | -3.5353 | -53.011799 | 2025-08-27 00:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c010142f-c43a-391b-ba6e-9c7056479485 | -13.4172 | -46.8591 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb7576e7-4ba2-3cc1-a3c3-f3f84277778c | -5.113 | -43.201302 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6862b946-4c2c-3fa4-a03f-5d7f2225f0c2 | -13.071 | -46.305801 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 962d1ac4-51fc-3f50-a929-a03784c120dd | -8.8679 | -47.178001 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 191aa884-aa46-3deb-a74f-b9d3cab87c65 | -12.7943 | -48.143398 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 930c3d76-0223-3f7a-b728-6e0a34fbbf38 | -8.8995 | -47.313599 | 2025-08-27 00:22:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b95f752b-6290-3c51-91e0-5290b375b0a4 | -3.9796 | -47.8773 | 2025-08-27 00:22:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da44478-0321-3e1f-a75c-7aed1726e33b | -13.4352 | -46.9809 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
