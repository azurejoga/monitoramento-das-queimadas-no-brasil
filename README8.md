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
| 74668d57-7734-3197-88e2-71c223d56d05 | -2.8292 | -49.219002 | 2026-09-15 00:25:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eff3103-98b9-31f8-aa75-9f8c8255aced | -9.314 | -48.700199 | 2026-09-15 00:25:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75f09c8e-d0f0-373e-bdb4-6537a798089a | -4.6661 | -42.079102 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| df497458-bd6b-30fc-ba0d-dd2ed7c943f5 | -6.9585 | -44.536201 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85764e45-e88d-3900-8a30-00e0a4ac9482 | -10.0244 | -52.0872 | 2026-09-15 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd3225b-1310-3cda-a7f4-8e699acd899a | -5.9539 | -49.271999 | 2026-09-15 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10138502-34cb-316e-8d4d-1dac20e4f071 | -3.9291 | -42.9884 | 2026-09-15 00:25:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 329a443f-303a-3bac-a826-d33eec608212 | -6.9471 | -44.5317 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a30290c-e1ff-38a7-8b20-332d228bf788 | -11.1151 | -50.915199 | 2026-09-15 00:25:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e08f878-4a1b-355f-a953-be81dc796cbf | -5.3115 | -49.244701 | 2026-09-15 00:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5513e7-e5e9-335c-b2c7-69c645acb3e8 | -9.4555 | -48.548698 | 2026-09-15 00:25:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 406f7da8-c96f-34de-852b-db853190558d | -3.5368 | -53.977501 | 2026-09-15 00:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc55c9b-292b-3297-ab8f-4ba4ea4e39a9 | -14.2198 | -47.422401 | 2026-09-15 00:25:00 | METOP-C | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e66d2819-96e2-3e20-a916-ca69d46f6327 | -5.413 | -48.501301 | 2026-09-15 00:25:00 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 290b5171-2a17-340a-9f80-29584001de4e | -10.4364 | -48.636501 | 2026-09-15 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4496a18-ab48-372a-971a-520c8038576f | -6.9487 | -44.538502 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6567b593-66b0-3556-a994-bffc340ff8cc | -8.4714 | -46.8624 | 2026-09-15 00:25:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5f8ea21-8fe7-3623-96d9-f2f0f50e80d0 | -6.4334 | -43.0644 | 2026-09-15 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 985b7c9e-5d23-3ecf-aa90-d44aa41b7408 | -9.3161 | -48.709999 | 2026-09-15 00:25:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| baa95f17-f0fb-3204-a386-ed08b178b3fa | -15.5407 | -48.813801 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd391e1d-8700-3e76-9fd0-2cad339c232e | -9.3531 | -50.081501 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a2d2d1-0bde-3d75-94aa-a7950840d2d1 | -8.2087 | -43.780602 | 2026-09-15 00:25:00 | METOP-C | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e80d15c0-4d91-35be-8f93-ccb9749ff2c7 | -4.1869 | -48.672699 | 2026-09-15 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47ff7315-30d0-3bbf-955f-71ae04bd1719 | -5.3509 | -50.162899 | 2026-09-15 00:25:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7f19dc-45e9-3199-ac99-aa3b7566cdcd | -6.1469 | -55.681198 | 2026-09-15 00:25:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed3950fa-18eb-3a61-9ee8-614dfa39a681 | -5.1117 | -41.0788 | 2026-09-15 00:25:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38f40755-53da-3b1f-b575-5c0c4f746c3d | -11.1719 | -42.8022 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cd309b27-228b-33e6-88ed-eec038808d2b | -6.2588 | -41.962898 | 2026-09-15 00:25:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bbb9b808-637b-3961-805a-433e5d6583c7 | -5.4277 | -43.979698 | 2026-09-15 00:25:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dabd0e1-e307-3ec8-aab1-d65fa19d5da7 | -15.9243 | -47.3699 | 2026-09-15 00:25:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| ef704a0a-7ace-337d-b916-af645036f655 | -13.5943 | -47.904499 | 2026-09-15 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b90d6d63-f8ac-3ba2-b1c8-7042cd63ce54 | -4.1844 | -49.394001 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f027400-3a69-3d2a-83b1-d0642d5b336c | -5.6052 | -44.841301 | 2026-09-15 00:25:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd1f11f9-dcac-36a3-83f3-cdacbb8f5c04 | -7.7413 | -44.7131 | 2026-09-15 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02d8092b-bf93-3b01-a321-a0ae982db6db | -14.7638 | -42.949402 | 2026-09-15 00:25:00 | METOP-C | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f9117970-d74d-325a-a010-c274ddc8d683 | -6.2626 | -41.979099 | 2026-09-15 00:25:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 140f678d-1ab8-3365-a580-8899d59f4a99 | -3.7954 | -44.103699 | 2026-09-15 00:25:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1db152ea-521a-3caf-b458-885a1459ac2d | -7.0904 | -41.812401 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0baacad8-3c73-31a9-bef4-bcfc0e7cfe5e | -12.5574 | -47.105999 | 2026-09-15 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e3acd73-9e0d-3490-925b-5c22d6a5e69e | -6.787 | -46.460602 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 418df27e-c765-3560-9a17-5a8d900b1b92 | -18.8256 | -44.518902 | 2026-09-15 00:25:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4641300f-2124-3104-939d-9a1c4793a80a | -13.5705 | -47.8885 | 2026-09-15 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae68c51a-1631-34ea-bbe0-be4784108580 | -14.9553 | -47.522301 | 2026-09-15 00:25:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 591e3cab-66fa-3443-91aa-d3cc2b5e7734 | -3.6634 | -40.575699 | 2026-09-15 00:25:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a83e0af5-7767-3ed7-a0d1-0cd9f5a7e85a | -7.0182 | -44.6166 | 2026-09-15 00:25:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3774fa12-63f1-3735-aca2-9580d5d1d2a6 | -12.9781 | -41.066601 | 2026-09-15 00:25:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3ee0dd19-8b39-3cf6-820c-2198104b65f1 | -4.1771 | -48.674801 | 2026-09-15 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c88f700-e064-3b51-8071-aef403028a15 | -8.483 | -44.5746 | 2026-09-15 00:25:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45e7211a-dcec-37c5-80b5-04952abd7dc4 | -18.016701 | -50.288898 | 2026-09-15 00:25:00 | METOP-C | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03d6780c-af65-3165-b8ea-26680e91bf13 | -7.0856 | -42.099499 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a5bb8bd-36ce-3293-a763-62544b769743 | -10.8711 | -46.327099 | 2026-09-15 00:25:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc346e48-e52d-34f4-a1c5-386ac5436481 | -3.2284 | -50.579601 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3c49342-105b-3f30-b3f6-4fdf0ad6e9f0 | -14.6773 | -48.010101 | 2026-09-15 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d10dac8-f6e0-36e5-ab21-ceb423715e45 | -12.9762 | -41.0588 | 2026-09-15 00:25:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cc5d0111-1b6a-3441-b65c-9198f7a8153b | -17.207199 | -41.487202 | 2026-09-15 00:25:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac1fb5bf-a01e-36ed-aaf5-f0e6731d279e | -7.2093 | -46.1409 | 2026-09-15 00:25:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd4c6279-a38d-3199-93cf-8bc3280f88c9 | -10.7539 | -44.821098 | 2026-09-15 00:25:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57bde762-a9c0-3bc6-8c30-d8396918a7f8 | -11.8858 | -43.8074 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 691eb3f4-bc56-3a73-9b8a-06b53330ecc0 | -1.7725 | -54.473598 | 2026-09-15 00:25:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5342a5ca-1fa1-3e58-9060-584b66adfe53 | -2.8919 | -50.407001 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 580f38ef-2d79-37f7-a462-61aaebc80e73 | -5.6348 | -40.848301 | 2026-09-15 00:25:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3050ff53-7a90-3f20-8739-371e0a049c25 | -11.2283 | -43.453701 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 606cdb7f-c382-3df1-af06-72cadb81c2f0 | -14.2178 | -47.412701 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0c03fe4-1250-357c-91d4-1c30ca45e78c | -7.1321 | -42.121799 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 880d24e5-d120-36de-9144-b576d98a8458 | -14.8588 | -48.150902 | 2026-09-15 00:25:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c0c3018-02d6-3eb7-a146-6ff54054603c | -13.6181 | -42.4454 | 2026-09-15 00:25:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 04e7bebe-9d0f-3523-90c1-715813d550fb | -5.4092 | -48.484501 | 2026-09-15 00:25:00 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fad51e3d-1347-3a90-b4ea-8e560e74cf90 | -11.8874 | -43.8144 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb76b4c1-536d-3205-abe8-496396a53220 | -15.5725 | -48.820099 | 2026-09-15 00:25:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b53656fc-624b-3f41-8a8e-98a4036e75b9 | -9.875 | -47.786098 | 2026-09-15 00:25:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64fed0f0-62cb-30b3-abc9-aedb776c0b69 | -4.6562 | -42.433899 | 2026-09-15 00:25:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22b91c79-abe2-3924-b84d-90f35684f152 | -14.1629 | -47.394402 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b24c73d7-0ee7-3fa2-b5a2-a136be470869 | -13.5537 | -43.5266 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b895c4c3-4bc8-36b7-a3ff-df2369d86dc9 | -5.4234 | -43.425499 | 2026-09-15 00:25:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1cf6f7d-4e07-3490-86e8-c2656ca94e32 | -13.434 | -43.82 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a854f98-e56e-3e59-9ccc-ea8ded2485ed | -11.2447 | -43.435299 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3372d3a4-caed-3369-b661-a390a7dd2338 | -7.9273 | -49.722099 | 2026-09-15 00:25:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f42a3ef2-551d-3786-aa9d-826ea8744f91 | -3.4896 | -50.3717 | 2026-09-15 00:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4d8395-02d1-331c-8ea4-f4e21ae583af | -7.7315 | -44.715302 | 2026-09-15 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 999dfb9c-a360-39b2-8753-a46205df98d1 | -7.3277 | -47.2677 | 2026-09-15 00:25:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2af9a1f-c548-3302-9ec3-9ec2ca05eb5f | -10.6674 | -54.1362 | 2026-09-15 00:25:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6d38d60-4dd4-3bf1-a0a4-05ec9d303219 | -6.1565 | -52.7314 | 2026-09-15 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09dd89f-8825-311d-9043-dffd0fb8b7ae | -11.1849 | -42.813999 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c155277c-96aa-32f1-911d-67996fcbea45 | -10.5699 | -47.729099 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf327ede-b83f-3c12-b425-79bad63f4555 | -3.9691 | -43.116199 | 2026-09-15 00:25:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 129f50b6-c90d-3bcb-a691-6bbaf36f3082 | -13.4356 | -43.827 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93487ca2-b8fc-33e4-ae65-6f9c633a2d17 | -17.306101 | -42.521801 | 2026-09-15 00:25:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 064a63e0-8824-360b-862f-d248e4b5778e | -13.3062 | -43.709 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a63fdc8f-1258-3271-a517-cf9167fc6495 | -4.6544 | -42.073101 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 520b36c1-35c0-3196-baea-91b32a50bec7 | -10.787 | -46.224201 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f712f71e-6740-3436-b225-bbae5869ede0 | -4.6681 | -42.087399 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94b151f9-8348-3522-a625-757c39266762 | -3.4874 | -50.361599 | 2026-09-15 00:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347ca952-1a8f-3baf-a7df-ae08f6f6b8e5 | -2.8194 | -49.2211 | 2026-09-15 00:25:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3155d5c4-c594-3fc8-bedf-4ac9445061ba | -7.4674 | -46.1437 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc7fac7-37a6-3d58-97a6-8078bc2fda70 | -15.575 | -48.781399 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 625ebb69-1d25-34a4-a92f-b70cff8db89f | -12.4921 | -44.629902 | 2026-09-15 00:25:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae858116-17a4-3a75-9335-eb5bef1017d3 | -6.9569 | -44.5294 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f533171a-99ee-378f-abbb-1737418c8b34 | -7.0715 | -42.127602 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd1e0ef0-b075-31a0-b452-7a6dfdcd635f | -4.2909 | -49.0895 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6727259-6881-3c7e-b4d2-c65f037ada5f | -18.166599 | -51.7547 | 2026-09-15 00:25:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
