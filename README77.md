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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9edae9c-be64-303d-91ab-d7db687a47cd | -9.37572 | -46.95081 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbb3c56f-c05c-3ac6-a890-f4107c5857f2 | -10.65315 | -45.24437 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33704393-cbd4-32ce-ab55-8664e46fba4d | -12.33135 | -47.82803 | 2025-10-16 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a1f4cee-a03c-36c9-ba4e-4d7ff93ee6d8 | -12.02811 | -47.66066 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c2880bd-d215-3a4f-8355-84ad51105f35 | -5.86083 | -43.88111 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03374a33-5b37-34b3-8fef-a1e65721255c | -9.69075 | -44.52592 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 51483935-78ea-3411-8279-8324e543cace | -7.0598 | -45.05627 | 2025-10-16 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d887ec24-5a11-3369-b085-a7681023f7a8 | -8.81341 | -47.30896 | 2025-10-16 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d39f5263-aa39-3ef3-a428-1c645a0045dc | -5.47274 | -42.93841 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 056abd9f-de1e-3ce9-bbed-a93a9f50f142 | -6.33077 | -44.31628 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ff8fd2-0893-3cc5-b519-5643acd93ca7 | -10.03224 | -43.83891 | 2025-10-16 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afb977b6-d0e4-30a4-bb6c-0f7d647e9a37 | -5.68495 | -45.10151 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ce097570-8a17-3356-8e74-5940b2e7d614 | -5.91871 | -45.44213 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b559201a-b22a-3361-8e3d-5a62a6030ce9 | -9.67785 | -47.90111 | 2025-10-16 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8973beb-59f1-3ffc-8dc4-617275aea694 | -8.4643 | -44.18281 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5d793953-d4b1-3466-b308-5856314805f4 | -5.8793 | -43.88901 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad1d2571-62d3-334c-9b0c-b6d3930e3c6d | -6.71923 | -44.38136 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c73ec7c6-120e-3d53-bcb6-d4aede1e65bb | -6.13122 | -44.29199 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72778d85-ae87-3381-beb3-f57427e709c4 | -7.94976 | -44.13774 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3468bde9-2d84-383d-b0be-f2a2aef52eba | -6.18506 | -44.30172 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6979ac63-8fdd-3160-8c02-3b0e81017aac | -9.69271 | -44.51661 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ab2d805-55b7-3bbd-841b-af64ebbc3d18 | -10.12089 | -44.56259 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3417360-90b9-3c5b-a051-a59b851bc75d | -10.61508 | -45.2442 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ba1046d-346e-3e6b-a002-901b771088d0 | -12.04645 | -47.6583 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd4ca8f0-0092-36e8-8295-08bcf0854fbb | -8.40424 | -46.23842 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0643a0fb-7a58-3022-bf7e-055ff75f32d1 | -8.40955 | -46.25893 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9afae91c-79e7-3f86-9bb0-24e5c2c87311 | -6.22855 | -55.63274 | 2025-10-16 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e2ae6f1-1f88-3073-b948-5203feca1d80 | -9.69344 | -44.50504 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7227764a-8f90-3891-87a3-9bf0d2431305 | -6.75235 | -44.37244 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42e6cdab-de75-3b2a-a39a-ac6a22ea5557 | -11.57148 | -48.56131 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04f730ba-2a3f-3caa-bba8-42a706f7a9a3 | -4.78176 | -49.23793 | 2025-10-16 05:08:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b420538-7674-3a14-8985-64b6a14411cf | -6.51727 | -42.19186 | 2025-10-16 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ead366e-a02a-326c-9bac-5f0dda47eb71 | -9.09009 | -47.9486 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57335b06-62e8-35c3-aa73-4132e860674f | -5.87289 | -43.88142 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e778962d-71ed-3dc9-9b2f-c4377f1c6e58 | -7.93144 | -44.12436 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1fcce040-466a-3aef-9db4-f34bb1a36cf3 | -7.34008 | -43.86916 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792a1cca-889d-3ae2-a964-bf66f6a2ca99 | -5.88723 | -43.87865 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc468e43-007b-3a94-95fa-c0f7fb341c90 | -5.86005 | -43.88686 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f42082e-a891-34de-8972-025c1b623158 | -5.51407 | -47.30536 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4721d820-f0e8-3282-a5fc-7d0cb31c2252 | -10.63656 | -44.41753 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78768174-d62f-32b7-aaba-158133318ab5 | -7.34607 | -43.86473 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3b77e0dd-a937-392d-b75d-678ffc9f70ca | -4.2993 | -50.40136 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 599c1890-526f-319b-a01f-348f1b0c7bcc | -7.20359 | -45.49341 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee82d57-dc6a-309d-8d1b-19f3d0468fc4 | -9.68296 | -44.53547 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c881e46-fa5e-3c65-8e83-ffebb8212563 | -10.72447 | -47.58388 | 2025-10-16 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44fdc592-2b8b-32d6-99d9-9b382122f5d1 | -5.87725 | -42.81352 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e7d1ffb-3091-347e-8bcd-4fd449037c20 | -9.08496 | -47.9479 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca22fcd5-399d-3d63-949d-49ed6d2e57bf | -10.6951 | -44.43032 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| def632fb-b9e1-3e91-83d4-854dd5abb1d2 | -4.81754 | -46.83659 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 438af004-6ebd-3f17-b800-78e2983dc921 | -8.46386 | -44.18464 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 09e78e7c-b462-3222-9914-63e798796d95 | -6.33868 | -44.01409 | 2025-10-16 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befdc169-3e81-3b24-b03a-58c78e2c1786 | -6.75423 | -44.37659 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b300e29c-150b-3a37-865f-2331114fd070 | -8.21573 | -43.31149 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3dc87e60-cb75-39e2-a0c7-6771e3d06f8e | -12.04602 | -47.66191 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46a2c602-093e-3e02-8632-1a5e36629d94 | -5.49042 | -48.95068 | 2025-10-16 05:08:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df84b2aa-7e5b-3e04-bd25-1b952a9db37e | -9.68499 | -44.52613 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4b26d740-a251-36ab-bbe7-abdfdc63856c | -7.03589 | -42.73652 | 2025-10-16 05:08:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 99dcf38c-128a-3011-9a08-760beedc8df6 | -9.36994 | -46.95067 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f5aaf7-3749-3f42-915c-417dfc8eff9f | -9.15632 | -46.87432 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fdcb760-9330-3950-bdc1-d4aadcafd451 | -8.20341 | -47.01336 | 2025-10-16 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4884de9b-0130-3d38-a95d-76d713e24b75 | -10.04042 | -43.82814 | 2025-10-16 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f98c322-acf4-3225-926f-b69e0eb4b3cc | -10.88117 | -47.93356 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18499708-eaac-3e8b-b2ad-7030d3799194 | -5.91929 | -45.43806 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a4b5d38-2175-32ca-b981-22356ab715c7 | -8.25231 | -44.13879 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9d2c940-d836-34d1-9561-b073e5dd4e3e | -8.3915 | -46.26418 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31a41be6-8909-3d70-9166-bdf79095d479 | -8.2956 | -44.97365 | 2025-10-16 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1f22bf-7a21-358d-bc41-e567d8205123 | -11.45395 | -44.05474 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 738b9dc1-bfb4-39d3-a43d-701972555ddd | -8.25418 | -44.07334 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 751c887e-7664-3897-9e22-4460178d1e83 | -8.40477 | -46.23456 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24869c0d-5f26-3885-8e6d-5c69a0a44446 | -7.16867 | -42.51811 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e6c84c2e-8d11-3726-9ac0-99a4e3014fea | -9.68939 | -44.53647 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3f684c1-50ec-3b13-878a-c99c0073291b | -10.13191 | -44.58013 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e11549a0-b4e9-3302-af92-6da64250970e | -8.07283 | -45.42688 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c1c2abe-6243-3b69-be88-680eaeb7e6df | -7.20353 | -45.48248 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b418358e-a2b5-3e02-a098-7e8a21a4023d | -8.21525 | -43.31205 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0ac258f-715e-342d-a64f-0a57b4d3ef7d | -7.35326 | -43.86053 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b6158268-5221-308e-927b-08a17dcf237e | -8.45711 | -44.18747 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 38d5a7be-d78f-351f-8a28-284363cf0112 | -5.91359 | -44.72919 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a648a424-c427-39cc-864b-212575b8ce50 | -6.75168 | -44.37744 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43415354-23fc-376f-beac-3d9e0921a651 | -7.11002 | -44.72496 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d15036f2-c721-351c-ad1c-cb7cc126044a | -10.62513 | -45.24893 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 774eef2c-baae-3daf-bf42-e64bcc97b2ee | -8.25487 | -44.06779 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bc62143-9520-3608-a413-a2771e152bbd | -7.94369 | -44.13156 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ebfcc94-07b6-3cbc-8e9a-5ed12f057c26 | -5.76766 | -47.91045 | 2025-10-16 05:08:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7045c319-8438-3a9c-b01e-d8534360c24e | -7.00669 | -43.74622 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef15907b-242a-30b1-902c-e305a1c55b43 | -7.95017 | -44.13229 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bac7a987-e78c-34b6-9fc6-fb9b959355cc | -4.82232 | -46.84019 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bb4e70d-18e2-3a4b-ab93-5015035ec219 | -6.25921 | -44.34269 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f844fa28-921e-3f6f-ab00-0136b914ba7e | -11.47781 | -47.64149 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3509e9-c5ee-3a9d-86d3-36444475089e | -5.68794 | -45.10405 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 795d0601-60ec-313a-a554-842c369e1d56 | -10.88854 | -47.91798 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 529ee31c-64a0-360c-882a-618349bd76bd | -6.53514 | -44.69514 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 582750ca-d63b-32ad-8730-fccbbae1388b | -11.58861 | -44.08953 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3461730d-8a4b-3d89-ae85-f0cca4ec9007 | -7.05531 | -46.68624 | 2025-10-16 05:08:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64615c33-b466-345f-8031-7c33f8128ee8 | -6.05238 | -41.93652 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7d61eb4e-1f4c-329e-ae81-4d64bb8b16f9 | -5.34843 | -43.75742 | 2025-10-16 05:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b46cf291-5fda-3a6c-81db-15e8f8cfae86 | -6.56527 | -42.96683 | 2025-10-16 05:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4642d34-7c80-3d4d-8ccb-63a238383e55 | -5.88084 | -43.8777 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bc1eeb5-f45d-370c-9cc3-2e39f45e5bbb | -8.2458 | -44.13806 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f6915a3-7a85-31d8-8470-86772d9a5c64 | -5.68261 | -45.09897 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README78.md)
