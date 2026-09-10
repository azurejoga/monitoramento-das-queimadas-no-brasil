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
| bc1a04f8-81ec-3ca9-b2aa-152af5f3b6b0 | -7.4945 | -45.280602 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88875873-7393-3696-964b-82d16bca5538 | -10.0863 | -45.469398 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4b29bf8-9203-3c32-aa21-46e6fc2296e7 | -4.3686 | -47.784599 | 2026-09-10 00:05:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d01a2a-ffdb-338d-b2bb-8ab8bc5dad52 | -5.1179 | -46.015301 | 2026-09-10 00:05:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 774e8e8d-6264-3582-9548-7bfb77cdbd41 | -12.8444 | -44.3256 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3147599d-c676-3245-b180-91a00e8ae3e6 | -12.8523 | -44.315201 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 359dc59d-72cc-321d-95f3-714bd27e0046 | -5.4144 | -41.838001 | 2026-09-10 00:05:00 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d86d4bd2-d673-3b67-9be1-ce06498e47e2 | -3.3723 | -50.396099 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e71ae3-b0bc-3979-8cc1-0768c2490ccf | -11.2182 | -49.939899 | 2026-09-10 00:05:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfc2adc-55a6-361f-88e0-0beb953a1449 | -12.8268 | -44.338501 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8599d66-0a93-33dd-b8fe-46e2f4920498 | -5.7594 | -45.090801 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c93855d7-e722-3afa-b28b-6ca805332589 | -12.3602 | -48.197899 | 2026-09-10 00:05:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb184c80-cc98-3029-a97e-af69dbfb0b00 | -5.6021 | -44.858002 | 2026-09-10 00:05:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 402a489f-9c91-33c8-9c75-c05bdb1b9d3e | -11.8532 | -44.856201 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13c2a1db-e0f2-3e66-a3a2-ab2ece51e9a0 | -10.9123 | -47.837399 | 2026-09-10 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d0129ad-7743-3dbe-bc8f-fb84dbe86339 | -3.2508 | -50.818001 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918b9e82-8935-32da-9558-dbbd52942118 | -10.0649 | -45.4664 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db57680f-453f-3acd-ae51-83c3423b2ee6 | 0.2572 | -51.473701 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0e217d54-9630-30f1-8a41-058ba45bf29c | -5.9229 | -44.951801 | 2026-09-10 00:05:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30741860-6205-3a48-a314-17a27778e43a | -3.2349 | -43.227901 | 2026-09-10 00:05:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fc5d0c4-602a-346f-9511-24bea8d70981 | 0.2489 | -51.464401 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e4ef82ed-03ee-3c1c-a0c4-b13039f3d3d3 | -12.3586 | -48.1908 | 2026-09-10 00:05:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3d6c2ab-2ebe-3b2a-944e-502a9b445029 | 2.5106 | -50.852299 | 2026-09-10 00:05:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ec5fc195-efdc-3608-b095-9ab0b55b5b30 | -10.9264 | -50.779499 | 2026-09-10 00:05:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81412577-ea89-38a8-a50f-5283c511be72 | -3.3738 | -50.403099 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8479966-ec45-3788-864a-95c53d0980d2 | -10.2712 | -45.199001 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf91b155-7e9c-3ca9-85c7-02420dc09b74 | -18.868601 | -48.921902 | 2026-09-10 00:05:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62a7c39d-f3f3-3c3f-9e6c-9ebcfe18289c | -7.0479 | -42.729 | 2026-09-10 00:05:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c6a05e6-3953-394e-ba20-e6618d5bc9c8 | -10.6871 | -46.109001 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86820f50-9728-3880-991a-c6ff7358c0ca | -10.0765 | -45.471699 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62a859f9-0bc9-342c-998a-0a06359732ff | -10.7353 | -45.914101 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83c72fdc-9faa-31f3-a6d1-2721518f5893 | -18.0343 | -43.0163 | 2026-09-10 00:05:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a289ef8-33da-3f76-ad4a-dcd93fb762e1 | -10.0782 | -45.479301 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e815b907-5c5b-32c3-9ce1-96822d31ee39 | -7.2634 | -45.351501 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dad76db6-d854-33c2-8faf-8af067b2d3ae | -13.4399 | -43.826099 | 2026-09-10 00:05:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8b106ea-037e-30a7-a926-b21587335a33 | -4.3653 | -47.7705 | 2026-09-10 00:05:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85bf8d93-d258-3f28-b4f5-3d516487fe67 | -12.8132 | -44.324699 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cec3b276-1f33-38ea-a1e1-3e3d82d50fb1 | -7.9874 | -43.950001 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35baea80-fb1e-368b-916b-cb380ada0100 | -10.2285 | -45.192699 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 160fbb18-0cca-30b2-8ab5-02915b57a277 | -12.858 | -44.339298 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40f4cdc0-77f3-319d-8d33-60a469de1882 | -12.8249 | -44.330399 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06cf0772-dec8-3875-afa7-a547692c7a2d | -8.3219 | -45.112999 | 2026-09-10 00:05:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6bdf2c1-8f36-3db4-ae89-622095f04392 | -5.7574 | -45.0821 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4ede1f-1044-313c-bee6-8ba5fd1ccd12 | -4.0384 | -50.887901 | 2026-09-10 00:05:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 283bda54-9995-33ce-ae9d-00b4c5580070 | -10.6707 | -46.082401 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5794fd3d-1c6a-386b-b6a9-25578b4affcf | -5.6099 | -44.846802 | 2026-09-10 00:05:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e46645d4-74e3-368b-b732-599438efcbab | -6.26 | -46.363998 | 2026-09-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 885b2d27-3e74-3aaf-9e62-5a7f45143118 | -7.0549 | -42.715199 | 2026-09-10 00:05:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d0c1982-aed9-3fe9-afd0-06c2e225860b | -9.2994 | -44.3517 | 2026-09-10 00:05:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc9d16a9-9e19-3149-a0a3-f4efe36965ef | -11.4364 | -45.150799 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58a115e6-fda8-3eff-a565-b7bf5ae33b51 | -14.1126 | -44.007801 | 2026-09-10 00:05:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcbaba3a-267c-352f-bf93-be7fd543b4d3 | -15.7807 | -43.543098 | 2026-09-10 00:05:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cc033cc8-4a73-3a72-8a2c-4e618b2d7d37 | -8.9415 | -44.409302 | 2026-09-10 00:05:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ccd3986f-4ced-379a-8ff6-fa7ada2bcbf6 | -4.2772 | -46.527599 | 2026-09-10 00:05:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abcf4200-c742-35d0-a456-3d79b69e3cd6 | -9.6855 | -43.452999 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8cd2d2f8-9a51-3ca3-91fc-93d23d5478bb | -9.6809 | -43.433899 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a5dfc54-57c3-34e9-81d7-822ca48de9ae | -2.9343 | -50.463402 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c76d615b-8fcb-304d-9c0b-0653205bfa40 | -6.0926 | -44.134701 | 2026-09-10 00:05:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c510f83e-76c8-39eb-9505-e6932030b842 | -7.9056 | -46.705799 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97e58404-5a4c-3aad-94ff-f2d42546334f | -6.7163 | -46.330601 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 012e2989-d691-3e32-bac0-4dc8b1196807 | -10.4604 | -44.947498 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc636606-969f-3167-92ce-5b432d097984 | -3.2706 | -50.081699 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3892e96b-35a3-3107-8923-332a2086882e | -2.427 | -50.268501 | 2026-09-10 00:05:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96623129-fb05-31b6-a0c5-ebfc12117aa9 | -10.1183 | -48.804798 | 2026-09-10 00:05:00 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 829e1eda-76fe-3ba0-a98a-cfb5c103e04c | -9.7033 | -43.3979 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 55e81edc-a111-3a5c-8f22-4f1e20f81488 | -9.3014 | -44.360401 | 2026-09-10 00:05:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 686d0f65-d8a5-3a30-938c-083081e65c18 | -5.7652 | -45.071201 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5250567f-066f-3d2b-bb37-faf8a94a08bd | -5.775 | -45.069 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8af15509-da90-38eb-abd1-26f020d83f63 | -10.0684 | -45.481602 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78394062-5e26-3987-aa25-119e4eb1b872 | -5.6546 | -44.288101 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c877cdeb-e14f-33bb-9cde-de48b1b96023 | -10.0747 | -45.4641 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57d7be35-6bff-3c77-9ce6-a29e9fc5ea89 | -10.9329 | -47.8839 | 2026-09-10 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7bc1dc3-1bea-31b5-921b-8686e4d9acce | -12.8678 | -44.337002 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca0ec70b-cb3b-3d9c-a6ef-41457130f2e0 | -12.8151 | -44.332699 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d54676e-78f0-3a58-b1b7-45c2855241c9 | -6.7294 | -45.449699 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e07cbf7-1b34-3f2a-9529-3ead0e135a80 | -13.4438 | -43.8428 | 2026-09-10 00:05:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f20e962-c348-3337-95ce-e0eaba3952ad | -12.8659 | -44.328999 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f084c86-7ea1-3d5f-8924-de20a7ac6d20 | -6.4461 | -46.097301 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa17bab8-68c9-346a-88a5-353ae1ec49f6 | -6.0949 | -44.144402 | 2026-09-10 00:05:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f801a639-98c5-38d8-aa35-e27968007b2f | -9.7756 | -43.441399 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11458e70-4087-3e10-af55-c9e4b229b090 | -6.4977 | -47.584202 | 2026-09-10 00:05:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2273eafe-afd5-332f-a934-47e0618cac02 | -6.2698 | -46.361698 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 951000e4-944f-37f9-a0bc-1dc06f593115 | -9.7108 | -43.386002 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c8c65bb-d888-35c2-b980-56951807dec7 | -14.8969 | -44.673 | 2026-09-10 00:05:00 | METOP-B | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| de42c942-7e1d-3c51-b012-47e33c99f4d1 | -11.216 | -46.348301 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 765ab86c-60d6-378b-b7ab-3d0b0c2ff6df | -12.85 | -44.349701 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52608acc-f779-312a-bcb5-4cc897f9dfcf | -11.2166 | -49.932098 | 2026-09-10 00:05:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 424a8e1f-a1d6-3958-b73b-da7ad385ff93 | -12.8602 | -44.614498 | 2026-09-10 00:05:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 525bfdd4-44e5-34c1-bbe5-5fffa251ea71 | -2.9425 | -50.454201 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4603c5a1-4810-364a-86ca-37764bc24784 | -6.1601 | -44.642899 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 254c86c4-5a72-30b7-9fab-a82c598522df | -6.7614 | -44.569099 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09e0725d-bfa3-3182-89c8-a2f1f1f890e0 | -13.4419 | -43.834499 | 2026-09-10 00:05:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32bd4df6-998a-36a3-8909-ad2c1a960f16 | -6.4974 | -47.6283 | 2026-09-10 00:05:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 146491b3-2a0b-3aac-9beb-46fd1685be49 | -12.7467 | -48.367298 | 2026-09-10 00:05:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a353bba-8bf1-3b69-8e99-bc2abc700762 | -12.8366 | -44.336102 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88d64673-dc0d-3a61-a78e-745d29148b34 | -6.4587 | -46.286701 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5e3e924-5b4a-3c71-955b-a94c83a97e18 | -3.2592 | -50.077 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dadf9084-61ba-398b-897a-3f99807b212d | -12.8598 | -44.347301 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d919d4e-d237-3571-aeca-e4f607db54e4 | -5.5978 | -45.371201 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06878a07-6993-3682-9012-de5eb971829f | -4.0367 | -50.8806 | 2026-09-10 00:05:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
