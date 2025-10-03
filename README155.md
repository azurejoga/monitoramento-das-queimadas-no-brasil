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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c858fb68-a0ca-30bc-afc7-9b9ed58dfd57 | -7.5693 | -42.3945 | 2025-10-03 14:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| c3a75da4-6d92-3973-a563-203ba1dc2246 | -11.9151 | -46.3499 | 2025-10-03 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d2bb71a0-9a85-3a5a-b0ad-c2b7a1ae884d | -6.0809 | -42.4881 | 2025-10-03 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 79c7f093-dff6-3862-9b27-16ac4ec61c3b | -9.6452 | -48.2084 | 2025-10-03 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 1c72790c-8a8d-393c-8661-f64270b533f6 | -7.7308 | -46.2513 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 96de6b00-bdf6-3c0a-b2a1-df87301a9ac4 | -16.0217 | -50.9207 | 2025-10-03 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bea55348-f3a2-350d-9215-581af7360f15 | -8.1699 | -44.1608 | 2025-10-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| e0443a42-368c-31c8-a4e8-1f2c9a82a4b3 | -9.355 | -45.9284 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c770bd43-c55e-3242-b15c-ef965eaa9ba4 | -16.023 | -50.8553 | 2025-10-03 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e2469db0-91cc-310b-b234-ec7564c6b704 | -6.2882 | -42.4229 | 2025-10-03 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 03db7546-2bd3-327f-b6a9-e9a61b9e4109 | -14.0027 | -44.9845 | 2025-10-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 03eac717-d79a-38e0-87a6-c972b3bcd27a | -5.4777 | -42.7721 | 2025-10-03 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 90f3d722-2065-31e4-b9e7-b74cf82a5aff | -6.3788 | -44.6268 | 2025-10-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c9928c13-450d-3355-a7c3-a43c8fcd1bb0 | -6.3786 | -44.6496 | 2025-10-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 6d700823-afe0-34cb-ba54-4065933a1728 | -13.155 | -47.8121 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| de8a30c6-c58d-3901-899b-dfa15da34605 | -9.9035 | -45.9553 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d4ae8e63-3e8a-3a3a-8dc5-007f5c1f02d1 | -13.3418 | -48.1188 | 2025-10-03 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 80e0b300-ee69-3d06-ab22-507d3f40e6db | -10.2773 | -50.3673 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a934e7ee-8519-35c2-b914-f9fc333eaed0 | -15.6538 | -44.4838 | 2025-10-03 14:30:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a8b00be7-b7a1-3540-b440-356d9c5fa1a4 | -7.7944 | -42.5132 | 2025-10-03 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 31282962-f95d-39d1-9575-8497103f00f9 | -14.367 | -46.1251 | 2025-10-03 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 6478a04d-06a0-3474-adde-69f6242ec53c | -10.0714 | -50.2387 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f90f3063-852e-3bc1-8bc6-6fac3193a81c | -11.9159 | -46.3044 | 2025-10-03 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 93aa855a-7314-39bc-a688-4605f4e455b1 | -11.1379 | -47.1959 | 2025-10-03 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4d90a0af-180d-3276-b01b-ae249a293f8e | -6.0806 | -42.5118 | 2025-10-03 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 172.5 |
| bd2c2706-a2ef-30dc-bb1d-e4447f47efbd | -6.6978 | -42.8118 | 2025-10-03 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 5dfcbd5b-87e7-3d81-ae69-5513c4350659 | -6.6976 | -42.8354 | 2025-10-03 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| aa0db989-0095-36c9-972c-3f20cab2ae04 | -8.8222 | -44.8043 | 2025-10-03 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5f9443e9-a8ac-3bc5-8a53-b45db8531a17 | -8.8543 | -46.6781 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3f5a2570-273c-3fc4-aecb-1556c117165a | -13.3422 | -48.0965 | 2025-10-03 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| bc5e93e9-02a2-3b3f-9bcb-a643c24d86f1 | -11.5687 | -47.6526 | 2025-10-03 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c3f93f52-2c37-3881-900d-d28b16040d03 | -8.5599 | -44.6494 | 2025-10-03 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c9012cd1-6c2a-3192-9693-71a01873e8b2 | -12.1215 | -43.4453 | 2025-10-03 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0298f757-10de-3124-badd-3078c04a93ca | -9.3354 | -45.9758 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c8d053c1-ef34-3fb3-a02a-a5a5313fe949 | -7.7933 | -47.3776 | 2025-10-03 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d888110f-8adc-3f59-b6fd-e0b1210f2446 | -9.3357 | -45.9532 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b20f075d-17c4-34d0-9718-de5a9cc4ce66 | -11.8818 | -44.9815 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 449391a0-b8b1-388c-9ff1-9e7622654313 | -16.0408 | -50.9395 | 2025-10-03 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4b2a6b4f-9660-3260-b759-ad46ab8245cd | -7.2845 | -44.18 | 2025-10-03 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3d9acb8f-d803-3a5b-844f-81d3e145675d | -13.1932 | -47.8288 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| aea34ee8-ac51-35b9-962c-67f1cc5fbf39 | -3.7481 | -41.048 | 2025-10-03 14:30:00 | GOES-19 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 182.2 |
| c4a70a80-c453-3a8e-a657-47fef85a0f60 | -9.9031 | -45.978 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7fb37748-262a-3d15-a52e-02d9253bbae5 | -6.679 | -42.8136 | 2025-10-03 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 8d38c0b6-6e5d-363c-aefd-5c1965985e28 | -7.7499 | -46.2272 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e35f44ce-c08b-3c11-a695-3e7017603b39 | -10.2398 | -50.3497 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 17f51282-c0d4-3da2-baf9-1d1854519b20 | -13.1534 | -47.9015 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b5b537b7-3fba-3ee6-ae0c-202bdecf079e | -12.9314 | -46.3818 | 2025-10-03 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 01007448-41cb-3cda-a132-d9370181d46a | -6.3529 | -43.4516 | 2025-10-03 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7520d4da-3f42-36d7-b9d7-18615951a0f1 | -9.8772 | -47.8103 | 2025-10-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7337e98b-be76-3332-a314-deb225436d81 | -8.1731 | -46.9897 | 2025-10-03 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c8a54228-808e-3df8-bdae-be9455c84983 | -7.7684 | -46.2479 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0262efb1-9f1c-335d-bd14-620125ec1f49 | -5.7688 | -41.7278 | 2025-10-03 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 33c38cd8-e1de-3b3c-a736-fc18dab6a174 | -7.2776 | -44.8007 | 2025-10-03 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7cd096e3-02fe-36b3-bae2-87a077c236d7 | -10.2401 | -50.3284 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 38e9061b-c9a6-3198-b096-caf8e18cf602 | -11.5496 | -47.6551 | 2025-10-03 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 93c9d74c-b2d8-3244-a59b-fd184a7aabea | -14.7341 | -48.1045 | 2025-10-03 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 132.9 |
| dbcf667a-9de0-3468-87e9-1b04d7fd91a3 | -13.3422 | -48.0965 | 2025-10-03 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0c495b6f-c3bd-3ab2-a135-af6ca5f8f41c | -14.7536 | -48.1013 | 2025-10-03 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7a502302-41f8-3dc8-b216-47e719bcfa2b | -5.7022 | -42.8255 | 2025-10-03 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| d155c741-1da8-3715-aa77-6ab0fcd07005 | -8.8732 | -46.6762 | 2025-10-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a4e6274e-38a0-3e22-b4ca-af3c4cb8e13f | -11.4796 | -44.9943 | 2025-10-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f48e8ba6-a704-3308-a64a-dddaaebbc3d7 | -11.8238 | -45.0132 | 2025-10-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9f9632d5-473a-345e-b156-de8faaf6a4a8 | -6.2721 | -44.0381 | 2025-10-03 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 52c20f7f-be94-3d58-8aeb-b123420384bb | -6.679 | -42.8136 | 2025-10-03 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 6077f627-5d04-3353-a94c-d3af60411e59 | -14.2934 | -45.9307 | 2025-10-03 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 386.7 |
| 19e259d0-49b6-3c2d-9495-c994bde11b10 | -8.1917 | -47.0101 | 2025-10-03 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e76ed0f3-4bbf-3ae8-b99e-ff9e2f8519b8 | -15.8097 | -43.7355 | 2025-10-03 14:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 89e649aa-37b4-32a1-b72d-428d3cf4c8fb | -9.8769 | -47.8324 | 2025-10-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e4dd2e58-0e22-30a3-8f0e-fdea5c0524bf | -6.3529 | -43.4516 | 2025-10-03 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0a62dab3-0229-38db-baee-53a4c297d8d3 | -7.7746 | -42.5865 | 2025-10-03 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 206.1 |
| f29a3ed3-d886-3d97-b1a3-136f620cff1d | -10.1098 | -50.1921 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f813f051-5e49-35a6-8d67-f91d374b184a | -8.2478 | -47.027 | 2025-10-03 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6da75fd4-5674-3698-8591-a3920155fe3c | -10.4486 | -50.2644 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 2bcd6649-0946-30c9-8dcb-029964c69484 | -9.3547 | -45.951 | 2025-10-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 17e53aed-9267-3166-bd97-ba853cec6262 | -11.1444 | -43.3845 | 2025-10-03 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 175.6 |
| 47b1ab6d-0f10-3be8-b601-f4df07a7bf0f | -9.9391 | -43.6012 | 2025-10-03 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 4657679d-c4b5-3c85-b70d-e0b6805af9bd | -13.155 | -47.8121 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 0274a219-02c9-3f2b-8b60-9989e4906fa7 | -14.2944 | -45.8845 | 2025-10-03 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 008f0696-a136-38f1-bb9a-76701ab5251f | -6.2408 | -45.3424 | 2025-10-03 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| eb34e8de-ca1a-3272-9480-9e2917f3d87f | -10.0187 | -48.5183 | 2025-10-03 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b03818ae-9d44-3b2b-8ba2-0302de5562dd | -16.0413 | -50.9177 | 2025-10-03 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dd78bc4b-5ef3-3c39-be3c-c9f7a5950c04 | -16.0212 | -50.9425 | 2025-10-03 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f24152b9-ba33-3d89-8092-a9b23aac92a5 | -6.6604 | -42.7917 | 2025-10-03 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| ffea72c7-46c4-33b6-817f-e83c3ac8905e | -6.3532 | -43.4283 | 2025-10-03 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4cd85b70-f1d3-3aaf-bbb6-86bc38e13597 | -16.0217 | -50.9207 | 2025-10-03 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0b902b28-f1b0-3ff8-84e7-b74b9949b1bd | -13.1919 | -47.8959 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f9db40cb-e684-32ee-be3a-63dc1ba73d93 | -8.1731 | -46.9897 | 2025-10-03 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b1461ca7-59db-37e7-8d66-8d722d550b09 | -10.0909 | -50.194 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e1b8188f-e4df-332d-8bde-444a1b2deaeb | -13.7858 | -51.3047 | 2025-10-03 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4afc737d-39ba-3493-99c8-3bae48721597 | -8.5035 | -50.9947 | 2025-10-03 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 0a2fb957-55b1-3648-a68c-b2b4e6494a3c | -11.0714 | -47.804 | 2025-10-03 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b4e5db37-ad66-3e6e-97a5-3c115643a970 | -9.3386 | -45.7493 | 2025-10-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| bd3be6e5-ea12-38cd-8fd2-ed9d382ae3e3 | -10.1089 | -50.2563 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d3a6862f-bc6f-3912-872f-806c3275f575 | -14.3675 | -46.102 | 2025-10-03 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 344.0 |
| a08800e5-cbfd-3c41-988f-474c4a357692 | -11.9155 | -46.3272 | 2025-10-03 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 385.1 |
| 0269f946-3939-3445-8ccf-1db865123408 | -5.7033 | -42.7077 | 2025-10-03 14:40:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 4e501779-d4d7-3cd4-9f19-6dc67003b4c2 | -13.1932 | -47.8288 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1c28b8bc-65aa-3e35-8974-9afe5a08128c | -6.5551 | -43.8758 | 2025-10-03 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6f7957d9-5549-3897-a948-5029fe287e64 | -8.1699 | -44.1608 | 2025-10-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 3a53b8e4-e185-3fce-bc6c-e879c3959f7d | -13.1345 | -47.882 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 200.5 |


[Clique aqui para ver as próximas entradas](README156.md)
