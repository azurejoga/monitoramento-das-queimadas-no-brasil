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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e051d44-078b-3665-8ddb-1a6703832495 | -4.10472 | -42.50206 | 2026-08-15 11:34:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| cf1bdfc3-bdb7-3b4a-a443-45b2faf8a396 | -7.00123 | -45.90439 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 85ffb606-847e-3011-afd3-6751c243a43c | -6.12149 | -44.02316 | 2026-08-15 11:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3439ac5e-f236-358d-9684-c512b10909b9 | -6.93228 | -43.63587 | 2026-08-15 11:34:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a8e8ec28-7b8a-3463-91ca-11168e82c580 | -3.43407 | -39.0425 | 2026-08-15 11:34:00 | TERRA_M-M | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3f7a0858-7fda-34fc-9104-4c7be247d3de | -6.93103 | -43.64475 | 2026-08-15 11:34:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 4c40b8a0-e9c5-3173-bbc4-2e361b0ed699 | -7.00262 | -45.89489 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c3cb6ef7-1341-37a4-9584-c1ce6a5a8444 | -5.9358 | -43.63731 | 2026-08-15 11:34:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4bda35be-ce67-3769-b984-8162ebb453c0 | -6.83973 | -45.36562 | 2026-08-15 11:34:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a5abc3c-d3a7-33fb-a027-fdf3f8f563d9 | -6.12024 | -44.03196 | 2026-08-15 11:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cbb7e29a-9c8e-36fc-b7ec-a0a67bff47a3 | -7.27121 | -44.68005 | 2026-08-15 11:34:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70117981-804f-3a24-816c-e0be9b4aa828 | -6.99207 | -45.90303 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ac232684-ab60-39c5-aefb-a4fce255c734 | -7.00904 | -45.91494 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d3073256-e62b-3972-b630-ba9895449464 | -6.83841 | -45.37475 | 2026-08-15 11:34:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ccc56bd9-7efd-385e-aede-344a4f74ce47 | -7.81396 | -44.11052 | 2026-08-15 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| adbdc6f6-8d85-3444-8a5a-23b11b3c4130 | -11.62929 | -45.34663 | 2026-08-15 11:36:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93e9568f-5844-3d27-921b-142cb4a9332a | -11.94028 | -46.32145 | 2026-08-15 11:36:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 40b1265c-b8ef-3df4-8df8-acf4c67e9ea4 | -13.54607 | -46.25968 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5e111709-26fa-3ab2-b865-9e3aed848f01 | -14.4606 | -45.67316 | 2026-08-15 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3732fc67-f2c5-3bd5-9fac-47944fa07500 | -8.52147 | -46.53572 | 2026-08-15 11:36:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7fa26923-01d4-3774-b567-c16c6a37c96f | -14.06991 | -41.84264 | 2026-08-15 11:36:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 07d5fb17-3b8b-3942-abac-fb17ef24a413 | -13.55495 | -46.261 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| efb0ed6f-fde3-3d00-91e3-b2bdb76bc806 | -9.11434 | -46.40072 | 2026-08-15 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1c0c10f2-1364-3f19-80b2-deac2cf8b6b1 | -14.44688 | -45.69239 | 2026-08-15 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37656691-b01a-3a53-8789-7c95a5c71487 | -7.82279 | -44.11177 | 2026-08-15 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fb6344be-51d8-3e7c-8909-69499b64dbc3 | -14.96916 | -46.6203 | 2026-08-15 11:36:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db9c38f3-5cf9-326f-a2b9-15060948f20a | -11.07706 | -47.23472 | 2026-08-15 11:36:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9a52fee7-b396-3848-92af-23cb404174ba | -12.6484 | -47.63999 | 2026-08-15 11:36:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5a6d7768-5c72-3010-a985-9f585193c8d6 | -9.71542 | -46.08117 | 2026-08-15 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b2e7dd91-f0ae-3c0c-a573-724c530da87f | -14.29051 | -42.19584 | 2026-08-15 11:36:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fcf1ff1e-adfa-3dcd-afee-4574097b76ea | -11.33712 | -46.22282 | 2026-08-15 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a8c731cf-9b7b-3ca2-afb5-950b824e4146 | -12.72234 | -48.43147 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 67c18633-cb00-398a-ba4f-a83846768f3d | -14.92149 | -46.62569 | 2026-08-15 11:36:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| acf6dfd0-577f-32b5-ab49-cb98576db2af | -12.44368 | -46.6632 | 2026-08-15 11:36:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4bedf5f2-eb78-3b90-9983-037a8c993470 | -14.4593 | -45.68222 | 2026-08-15 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 21a7f4be-6139-3223-9bc0-a39b23dda22d | -11.46584 | -46.59833 | 2026-08-15 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 867cc6b8-b7b2-356c-8bda-f040a4e61e5f | -14.96778 | -46.62961 | 2026-08-15 11:36:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a5d5db72-f0a2-31b8-a34f-e3f8fd66ef9b | -12.44229 | -46.67261 | 2026-08-15 11:36:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b34edc22-5c31-346b-9e74-c4cc22360c76 | -11.43532 | -43.9185 | 2026-08-15 11:36:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1097cd1-d5b3-38d0-8dfe-6e0495ebd2bc | -11.91373 | -47.36282 | 2026-08-15 11:36:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 886c962c-613f-343c-b57d-7ba363a0552b | -7.81523 | -44.10166 | 2026-08-15 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d490e80-afb2-36e8-b164-df0a4e54b4f1 | -14.46907 | -46.75299 | 2026-08-15 11:36:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8c7ab9c-d90d-3609-bdfd-f9732c8ac284 | -11.94166 | -46.31197 | 2026-08-15 11:36:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 046553e9-b3d0-3327-9641-e4577c66514b | -7.58441 | -45.00398 | 2026-08-15 11:36:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8454f0f6-1397-3261-9763-d2ff58ea439b | -14.75223 | -48.24522 | 2026-08-15 11:36:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d9c8504c-9e8e-380f-a24a-9b0a6dffef30 | -14.4677 | -46.76229 | 2026-08-15 11:36:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ebcacd49-12a8-3ad6-a198-37278641ddcd | -12.73382 | -48.42205 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0d837d4b-1582-3a1b-a2bc-498baa1bbe5c | -8.5685 | -45.34119 | 2026-08-15 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2a26357d-7bba-3e51-bed6-5ea6844d2d41 | -11.07856 | -47.22457 | 2026-08-15 11:36:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 731b4da9-066f-3066-98c0-e847f919c98e | -14.92282 | -46.61662 | 2026-08-15 11:36:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 53251b24-1037-3db9-9cf3-2be9d0e1175d | -14.56464 | -41.8061 | 2026-08-15 11:36:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 483480e7-c9dc-32d9-9497-6f51348ab498 | -14.29209 | -42.18313 | 2026-08-15 11:36:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| da1d9390-4e03-38c3-95cf-1e695190a57e | -14.56299 | -41.81926 | 2026-08-15 11:36:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 73e95d30-4ffe-39ea-8855-95986bb4eaf9 | -10.62498 | -46.54731 | 2026-08-15 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1c6a1991-eeda-3965-b502-a2509f52be7e | -7.82153 | -44.1206 | 2026-08-15 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1746bbe0-c7df-3d44-851a-f7b584de71b1 | -9.70639 | -46.07992 | 2026-08-15 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f8862934-92f6-3ce4-96e0-d0f34404f61d | -12.02016 | -46.40567 | 2026-08-15 11:36:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 60ebceeb-acca-37c5-9c26-15c4dc5e7ab6 | -11.33851 | -46.21346 | 2026-08-15 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1688aa4c-c333-3d17-b4a0-dd7c91f62acb | -9.56857 | -45.37896 | 2026-08-15 11:36:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 02983441-032a-32de-b0de-90affee46fd6 | -9.12352 | -46.40204 | 2026-08-15 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a50a8d07-52d6-354e-8dde-4b3fad00c67f | -10.61586 | -46.54598 | 2026-08-15 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b563a39e-644e-3963-a27a-c6a09474dd9c | -8.49714 | -44.74413 | 2026-08-15 11:36:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6c19a34b-468b-30d7-a409-6b944fe4a285 | -12.3782 | -46.41787 | 2026-08-15 11:36:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3c0b30dd-1d09-33f7-b2aa-c0f69d05816a | -12.4527 | -46.66457 | 2026-08-15 11:36:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e1726b9-d8c3-36dd-a35f-e1e0663120ba | -12.64684 | -47.65027 | 2026-08-15 11:36:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4be87aa3-780a-3db1-bba7-76b4cb12e332 | -13.68379 | -46.25838 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e9e5da5b-e566-33fd-a9bf-25fa5950e3ef | -8.01825 | -44.16064 | 2026-08-15 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e56ac7db-7d44-377f-9705-834cc09a0886 | -12.77113 | -47.12515 | 2026-08-15 11:36:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a4cb64f6-968f-3dfb-bcfb-602c95402346 | -12.73221 | -48.4326 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f6f82319-b521-3df1-9604-a79946d0d8ba | -13.54741 | -46.25052 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b5a105c9-a238-3cb7-a11d-cb260ab6209c | -12.68941 | -48.44936 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 663de56d-e665-366e-a8c0-6d8e06c449aa | -12.77259 | -47.11546 | 2026-08-15 11:36:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4b60f70b-0f88-3fe7-9b8e-5fa2ed62b187 | -12.02151 | -46.3964 | 2026-08-15 11:36:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e6430514-c0fb-32ff-a403-53d9e3088f5f | -15.56817 | -43.43386 | 2026-08-15 11:36:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| a7312db4-205f-3c0f-9f68-e0b706bccf4b | -13.69266 | -46.25969 | 2026-08-15 11:36:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0b2c374b-c419-3203-84ff-baf611b13a60 | -12.37688 | -46.42688 | 2026-08-15 11:36:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d897acc7-4e94-37ac-a5e0-9a6a65f730c9 | -14.95704 | -46.6313 | 2026-08-15 11:36:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 82ebb395-6b08-310a-805d-973488781b22 | -15.15426 | -50.0628 | 2026-08-15 11:38:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5d45fb63-c335-33e9-a6ad-aa534d332b2e | -15.14814 | -50.03329 | 2026-08-15 11:38:00 | TERRA_M-M | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b7330c34-fbe3-3610-8179-6f6015a74822 | -18.19418 | -49.33229 | 2026-08-15 11:38:00 | TERRA_M-M | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d695b757-9150-30e9-b582-cb5acb9fba1b | -20.47837 | -45.41638 | 2026-08-15 11:38:00 | TERRA_M-M | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e2245f0b-4c29-364a-ad75-48bf29d49abc | -15.72973 | -50.72665 | 2026-08-15 11:38:00 | TERRA_M-M | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2c531025-fe7a-32cf-bba8-9532b5486c86 | -16.71572 | -46.39696 | 2026-08-15 11:38:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ccd47db-7e0a-376a-870f-8b553d46b97b | -14.40984 | -51.90249 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0c5effd6-6c44-32c6-a140-85264b9fa858 | -15.91086 | -42.03302 | 2026-08-15 11:38:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7ef11982-7917-3831-be9e-fcb91bf46b1e | -16.32487 | -49.53534 | 2026-08-15 11:38:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| eb8dde21-466e-36e8-936d-e5e5fdb6b083 | -16.10035 | -45.14529 | 2026-08-15 11:38:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d219755e-f79d-3db7-a307-caf9767ed55c | -18.19586 | -49.3216 | 2026-08-15 11:38:00 | TERRA_M-M | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 09efb8bd-d7cf-31e4-b729-875c0396fa0f | -20.33661 | -46.72621 | 2026-08-15 11:38:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a9c00a1-5897-3b4b-814b-d38db36a6de4 | -14.42602 | -51.86029 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 0393a82b-73dc-3f20-8889-498982ca93ff | -20.90716 | -44.89564 | 2026-08-15 11:38:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 446b99e4-6299-3e01-95b0-66c883c1b378 | -15.90921 | -42.04631 | 2026-08-15 11:38:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a9a99c1-66c2-3da2-a629-4e3a1e37b939 | -16.10923 | -49.86186 | 2026-08-15 11:38:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6321bd72-b66e-3748-a203-8cd2937fc805 | -14.49469 | -52.02006 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e220b495-adbc-3705-8bf4-52ed8e6cefd6 | -14.43167 | -51.8491 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 46bc8e1f-b6de-3441-a47e-27e7d8d0b491 | -14.41993 | -51.89737 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 4f780332-1371-33a4-b868-9c8ba3f11939 | -21.45889 | -46.46932 | 2026-08-15 11:38:00 | TERRA_M-M | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 398fc173-9c61-32be-85aa-ce322e3b2c35 | -14.43127 | -51.92545 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| bfb115d9-0bcc-3196-9598-bf0bf50b9524 | -14.42906 | -51.84177 | 2026-08-15 11:38:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 602f80b6-ed93-3504-8dcc-ac301031df07 | -18.58204 | -47.14199 | 2026-08-15 11:38:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README50.md)
