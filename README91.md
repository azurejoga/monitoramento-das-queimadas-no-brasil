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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f587450-2a3b-3353-a0e0-03e87c94f08d | -13.03039 | -51.0286 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b3d13490-14a6-3b14-89b7-624e426b462b | -13.08049 | -47.8357 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14d9a652-caf3-303f-811f-8a284b8f3fc5 | -11.84854 | -45.06311 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25016fc7-e23c-3524-b747-a2b16c542386 | -8.5202 | -48.23244 | 2025-10-07 04:57:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8126e979-9dd9-3088-bf38-c2b2d8fd1eea | -11.04663 | -51.66135 | 2025-10-07 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a8e58d7-c1a8-3739-b3d4-e13b0f7cd05e | -12.14342 | -50.87608 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7200c8fe-5d26-3d76-b243-c3f6c9f56b1b | -14.74999 | -46.03235 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 227c04d4-abd1-391b-8b39-b49668c225d9 | -11.5081 | -51.48146 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 63a1f5af-4d99-3774-967c-8ae2b3940311 | -12.98638 | -46.78789 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 408558e7-9dcb-30d7-bd7a-e3f67153082a | -11.15688 | -47.7574 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02b229b3-9d99-35fe-9bbb-74517498b611 | -11.05284 | -50.90574 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b183f48-e731-3dc8-b3b6-b6555048eeb9 | -12.61065 | -44.75916 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9024278d-40fd-35c4-986e-d34efe529002 | -13.09129 | -47.8603 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c124ff5-53db-3344-a377-36a5bc0b976a | -13.97009 | -53.89514 | 2025-10-07 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb8db215-9492-32a3-9a58-0c5df69ca6a1 | -11.79581 | -45.09667 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7e4aab1-ee67-39b8-8de2-2daa318ac204 | -13.54165 | -42.99373 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 05eb72eb-dbef-3e78-a00d-86b6bf873431 | -10.42575 | -50.32845 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f49b896b-e9b9-3dc4-9202-e2b2217f894f | -12.30298 | -55.11108 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcd72ab4-6c43-34d2-abdf-f77da817ca18 | -11.68086 | -46.34921 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74dc5669-c3e4-3ecd-bfe5-c00cb41aaf3a | -14.77288 | -46.07753 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 677fe286-26f9-30ec-b136-57c6a1125577 | -15.50103 | -47.92175 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27f0ab7e-272e-3cf6-ad55-7a7e5bb25421 | -10.41365 | -45.38576 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e3d81c6-57c9-39ed-869e-bea264f4258d | -10.38682 | -50.29508 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f020b3ae-172f-3502-8eb6-0cd361b35b1a | -8.85798 | -62.3622 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c253343b-bf90-38ea-9f8f-0ad60384d3cf | -11.94697 | -51.48078 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8c1bdda-649a-3d8c-be54-ef85ffe1cb7b | -11.94375 | -46.46273 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a19f9382-607d-3dc1-bbed-e850b63960fd | -14.86587 | -51.45103 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19ad8321-c5dd-3315-9118-0124abfd7c83 | -11.80714 | -45.05203 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b26f3db5-2ed2-3643-9838-0acb83e9425b | -13.25572 | -48.06007 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 465b18c6-4cce-3e19-86c4-f9af314a5052 | -13.54051 | -43.0047 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8c995ae6-2772-3fa7-8ffd-7d8418217704 | -11.04835 | -50.90993 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72c51303-4159-36da-acee-4d045f235405 | -13.26952 | -47.1628 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ba151e5-47ad-3fbf-9a4d-e4d7149b2bb5 | -9.38786 | -59.42201 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d4529e-377b-3332-9382-bfed95beadc7 | -15.22466 | -49.31094 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87184a65-48d2-3861-bea8-9d99c4c448ff | -15.38181 | -46.27824 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68b563ca-7957-35aa-bd06-60ccd077be10 | -10.6772 | -54.69506 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36e87d31-3d9e-39b1-b939-df02b870f939 | -9.045 | -50.6941 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efbeb01a-04e3-3c44-a951-a76eafb367e2 | -15.58506 | -47.26678 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f09ef2-0f5a-3d68-98b4-7bcc516a42b8 | -12.1621 | -51.43723 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e962a439-2663-3e7a-a791-e745fddde1f9 | -11.42206 | -55.07718 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b01f98f-1a93-3ac2-bf7b-afb9c3db39fb | -10.3222 | -51.45749 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72069357-2696-3b48-8c39-04f646680b45 | -10.38927 | -50.30574 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7893e473-16c8-3d35-ba07-8c88b88b7947 | -12.01963 | -47.79018 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 833b224f-4a44-3f41-bd1f-7be865fb914b | -9.61963 | -54.31495 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf472637-3d0e-3bad-b4d8-121c79a57053 | -10.74236 | -50.49298 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79b66391-ca58-374d-8557-8adcc804d8bb | -10.88795 | -47.13376 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d25d23c-7086-3388-b95e-a138b745d5ba | -13.31625 | -47.77191 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa77e61a-2022-378f-ac5e-a46b0c23e6f9 | -11.15084 | -47.75463 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25e6567a-5294-386f-8151-db23054ea59c | -10.45849 | -51.24797 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 307d3a95-bd3c-3c6c-830e-731068aba026 | -7.43302 | -63.74811 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a989d34c-6ccb-3116-b901-39224b1b0952 | -8.52884 | -54.85826 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79bb8a7f-348b-3f93-9e84-07800985733d | -11.50679 | -51.47879 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b6b2121-a74f-3fab-986a-a8ec87ca4ff4 | -13.21889 | -47.81439 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c2ca42f9-b2f7-37e2-bd84-92fc50183385 | -9.40174 | -61.44384 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 686f0b3c-d0c9-3184-b4d8-1d5307ac180c | -12.99276 | -46.79218 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 753723f2-cd3d-3b53-9031-8d07d404a2d4 | -10.15024 | -53.7176 | 2025-10-07 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4b2f9e6-c2a9-354c-b548-ed8b2dce16fa | -13.71903 | -54.71437 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4e0e39e-9c71-39da-ace1-db30f43e4cff | -11.046 | -51.66316 | 2025-10-07 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 093637af-654c-39fc-a7e3-81fb0513076d | -10.39832 | -51.60117 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 599a05c1-7388-3e39-9922-967e0fe07abe | -14.77554 | -46.05486 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c25899-935f-3e22-8496-3b8062a6b5dd | -14.91858 | -46.86861 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33cb3db-d916-3b91-b98c-1d474e36a50f | -13.36501 | -47.25337 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d847a824-c47c-3f58-8f6d-1a1b6555b616 | -15.39403 | -48.00557 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3bf05bc-c24a-339b-a66e-37b5ccff827e | -9.8317 | -61.99323 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82233c4c-82d1-3604-a599-33fe6ffe5d42 | -11.71584 | -44.44431 | 2025-10-07 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18b79666-93a1-33a4-986b-af4e5578247d | -9.18281 | -47.82853 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55b23d4f-b2ee-3d83-b322-3ca362036185 | -10.42647 | -50.3234 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 767260dd-519c-3422-8c69-4c8fe36665b6 | -11.49214 | -44.97416 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37bdcf7f-f58b-3327-82d0-b47515af6082 | -14.92129 | -46.80226 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0480022a-adfd-3ffe-9ad1-02292da5c862 | -12.89901 | -54.74933 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b2c84cf-dd50-331d-a8b4-70e2927db85f | -15.38148 | -47.98569 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4de14af6-9a7a-377b-a3b3-3683322faaf7 | -11.74153 | -43.29707 | 2025-10-07 04:57:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7272a0f2-8f3b-30ee-bfdb-612f146a09d1 | -11.15768 | -54.87997 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bd71167-e4c9-3cf2-84da-04361a5f3c4e | -12.72606 | -47.93644 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0e0c734-0d6b-339c-8bfc-06c55528b754 | -14.61624 | -52.48942 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446c14b0-3ebf-3a88-bdd6-23fdf160de67 | -13.51777 | -48.61971 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f12215c-f4ba-3eb4-b427-171fbc46cab8 | -11.15219 | -47.75653 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5bff7b1-c896-3fe2-8622-267d775961a1 | -10.79306 | -48.59613 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c5f981b-9804-38ac-8691-130bafeb9e3e | -12.97644 | -46.78351 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cf24940-0dee-35aa-9fb2-4f0d3c5f6916 | -13.26044 | -48.06096 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fd2f060-2547-3aec-a946-8483d6f9d6af | -10.12386 | -52.34647 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908fab3e-5ddb-320a-b44b-fb483562a0f6 | -13.51203 | -48.62823 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f071271-1502-3744-972c-c954f3bc0f97 | -15.49785 | -46.8303 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c061ed7-54c6-3f7d-a8d3-1498223d8cc8 | -12.38283 | -51.08246 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37581fd-f94f-3b2f-8de2-0570e3326786 | -12.95075 | -46.82117 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed1ff44a-72e8-301a-a3a2-54ed1d4c8ffe | -14.36063 | -52.16164 | 2025-10-07 04:57:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d960ee6d-9839-3742-be32-b9e2263d7691 | -14.92574 | -46.80066 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f47739f-31d9-3a50-8dbc-c69eb8352397 | -13.28009 | -48.47479 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7426131-87dc-3ae5-a9b0-d7bf8d9d6a7b | -15.76324 | -47.77228 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab07b532-021c-386e-866d-dac425ffc7c2 | -14.92086 | -46.80581 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 595b0491-4f45-3e34-bb30-5d6e70e045fb | -13.50263 | -43.66788 | 2025-10-07 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e99257dd-8a42-336f-9912-05acf66e7fbe | -10.74508 | -49.71389 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9322108-0c72-32bc-8ac4-260cd43fb590 | -11.67508 | -46.34726 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c75fea20-37da-30b3-8736-81363fcc4d85 | -14.91819 | -46.8718 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae3cdf6-f9ea-3d10-a416-bcf812933eef | -14.92072 | -51.4048 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f5731ef-96ec-37dc-ba4a-e08f41f99b65 | -11.94414 | -46.45972 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 409eb9d0-4830-38e6-ae15-56e113749681 | -13.30775 | -47.77407 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b5b4b1-837b-3e15-ab46-da6a3b6fe1f0 | -15.27413 | -46.33644 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59d4d1f4-595e-3759-9e85-7a15de73fa1c | -10.15024 | -56.89521 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 128d4f01-f982-3ff8-ba31-be85c4e8b66b | -11.02788 | -50.92368 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README92.md)
