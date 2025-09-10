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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 094ac072-8e97-3edf-92d0-635427ab70a1 | -11.4465 | -43.6224 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| b4865f58-cf27-3f06-8df0-a3dbb2b15006 | -5.5892 | -45.0278 | 2025-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| dc728f26-ca47-3c6f-b6c1-f5338e9c4b25 | -11.4473 | -43.5751 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b52452ef-06e1-337a-8fb2-dafc76754a38 | -5.7555 | -47.4669 | 2025-09-10 00:00:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9bfd4f0c-0806-3093-be73-675901375ba1 | -15.8869 | -51.8274 | 2025-09-10 00:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 78f0d20c-8010-3190-b0dc-cf2ffaf639aa | -5.6786 | -43.3659 | 2025-09-10 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 9dd7e7a0-e870-35ae-bb00-83e252ed54b9 | -13.1364 | -54.9376 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| a72a9232-e620-39a2-bd6d-c6f037400abf | -10.0157 | -51.6821 | 2025-09-10 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2fc7a5ff-2692-3cd7-8dcb-f90638de9c1b | -11.488 | -50.4298 | 2025-09-10 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 435e9617-1a79-3b2c-bfd9-f82ba5cdfb03 | -5.5705 | -45.0291 | 2025-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9d7a0098-1224-37c0-a1cb-b4cd58a42d38 | -11.4883 | -50.4083 | 2025-09-10 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f62d607e-8da5-3fbe-b8a5-d6c15416ce28 | -15.8873 | -51.8059 | 2025-09-10 00:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1672ef56-ade1-3e20-a8dd-17280b9cb1cf | -13.1178 | -54.8986 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| eb4dc6e2-9f57-3f8d-8f2c-ab27a656aa43 | -12.9286 | -54.7949 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e118b0d4-d825-38cb-b2f3-10387ef6b9fd | -17.2527 | -46.0844 | 2025-09-10 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 95bb050d-9f87-3365-89fb-fb028a0f462a | -16.4573 | -50.6773 | 2025-09-10 00:00:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b23a5ffe-3bcf-3707-b7b0-36e3901f1e6d | -11.4456 | -43.6697 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| dcb8caa1-3456-377b-85c8-9ac1f83f6aa3 | -5.6788 | -43.3425 | 2025-09-10 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |
| ec9c0bbc-2c8e-3810-9df4-7e6765f1d650 | -12.9289 | -54.7744 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 30c9dbcc-3898-3148-8648-803107a50f2c | -11.3202 | -46.5218 | 2025-09-10 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 40c7907c-3e01-3c6d-9333-57135840be38 | -5.5703 | -45.0518 | 2025-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4e5a90fe-a19c-3c8c-b337-1b3aa73e9e49 | -6.2595 | -43.4129 | 2025-09-10 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 44ad99db-c565-3c29-a9a8-1b6e418b3cfe | -15.8673 | -51.8303 | 2025-09-10 00:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4b45233a-1d6b-37cf-8f4a-98c4d357434c | -18.1519 | -51.7281 | 2025-09-10 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| bd6c9c34-afc8-3784-b5a6-a00899e300a8 | -11.4657 | -43.6195 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 593e6df6-60a1-3f48-a71a-d8757169517c | -8.0604 | -48.664 | 2025-09-10 00:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 11e5dec8-31f5-3e7d-9c1d-bc0d40e02072 | -11.3205 | -46.4992 | 2025-09-10 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 4882f00b-6fee-3a94-86a9-c0a3e238aca3 | -16.0604 | -49.9741 | 2025-09-10 00:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 5c5c4643-bf98-3e80-9b3a-12aa55abbe7c | -8.0602 | -48.6856 | 2025-09-10 00:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 9104ab82-f141-3afd-acd9-2b4b5f18ebb6 | -11.4277 | -43.6017 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4c4d797d-87f1-3072-aaee-0365439388a0 | -11.3393 | -46.5193 | 2025-09-10 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 160036a7-70d9-3421-82e2-7af33a8b4dcc | -11.4469 | -43.5988 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 74213933-5426-3913-85a7-658fbff1347f | -12.9482 | -54.7519 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 36dc501b-9f32-30e5-b8dd-818ed15a56e4 | -18.1325 | -51.7096 | 2025-09-10 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| fb6b3450-299c-365c-8021-20d1c28c7127 | -16.0608 | -49.9521 | 2025-09-10 00:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d825d1f6-67f6-3360-97d1-24921af43499 | -13.1369 | -54.8966 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2038ded7-a839-34bf-ab98-bd16d1eb7584 | -13.1173 | -54.9396 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 21074059-cb07-386f-8ef6-3f894b8819be | -8.7564 | -63.4756 | 2025-09-10 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 12bf73b7-893a-3d7d-a154-2a53c0aacdc8 | -11.4281 | -43.578 | 2025-09-10 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7ab6f9a9-079e-3e77-9e2f-56c36f190af7 | -13.9762 | -48.224 | 2025-09-10 00:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6b391bf1-ae4a-3648-bb1f-317132b8d207 | -5.589 | -45.0505 | 2025-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 691a87bb-e277-31a1-b8a8-792df16db1cb | -13.1837 | -45.2865 | 2025-09-10 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| e0123987-7d3d-31c8-a34c-77337f68ae63 | -18.132 | -51.7315 | 2025-09-10 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 73ac3ec9-21ba-3235-b358-87a26e3776b1 | -13.2031 | -45.2834 | 2025-09-10 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c0c82a00-7906-346b-a9ff-e5d3d8fef1bf | -13.1367 | -54.9171 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 262.9 |
| 91069f8e-d0ee-368c-9dd6-62a7136e24d3 | -12.9673 | -54.7499 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6403e856-d27a-3ce8-a335-dcde91a12aa3 | -19.3571 | -47.4464 | 2025-09-10 00:00:00 | GOES-19 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f13d4540-436e-3c87-88bb-7ea4ce697bf4 | -13.1176 | -54.9191 | 2025-09-10 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 302.7 |
| e9c3442d-59f6-3ec9-a7a0-2b523f113148 | -13.2036 | -45.2601 | 2025-09-10 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 03020555-ae2c-30bd-a0dd-dda85f094e26 | -18.1524 | -51.7062 | 2025-09-10 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3021163a-215c-35d0-8454-c30e0e6cb08a | -15.8677 | -51.8087 | 2025-09-10 00:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 656de70d-2c00-3901-a237-373065ff67dd | -8.0414 | -48.6873 | 2025-09-10 00:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 110202ef-2f3b-3da4-9cde-c9e244f72f7b | -7.7705 | -46.0684 | 2025-09-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1a42bc23-3038-3733-9253-84397a5193b6 | -21.0371 | -48.41 | 2025-09-10 00:00:00 | GOES-19 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 80b43809-44e1-36d6-b1c9-01045f2f3811 | -15.8869 | -51.8274 | 2025-09-10 00:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 152d92e7-b9cb-386f-9730-18fdf36dbec8 | -5.7555 | -47.4669 | 2025-09-10 00:10:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bdaec126-8011-393f-a56f-e5d87965903e | -13.937 | -48.2522 | 2025-09-10 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8764f483-7f94-320a-943a-9f323befcb94 | -19.3571 | -47.4464 | 2025-09-10 00:10:00 | GOES-19 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 39e05133-cfc2-3efe-96f9-ed95710ded26 | -5.5892 | -45.0278 | 2025-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 958a4695-a1db-36f1-8437-adc546b1ae1f | -13.2036 | -45.2601 | 2025-09-10 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c0c6fb26-ef94-3267-af07-64dd4b433fad | -13.1173 | -54.9396 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3bc3a58b-a1b6-3294-9d0e-9b9705ca6fc2 | -11.3397 | -46.4967 | 2025-09-10 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 88110972-638e-3c47-85dc-8d583c0401e5 | -23.758 | -51.8917 | 2025-09-10 00:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| b79f5442-6ced-3d52-b018-d41dfe6bc1f5 | -18.132 | -51.7315 | 2025-09-10 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 59105b10-0a57-3277-8037-f17c41e8285e | -12.9482 | -54.7519 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 413b2c35-9e79-32b3-8b9d-09f6d1b59359 | -11.3202 | -46.5218 | 2025-09-10 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| d188a61f-d2bf-30d7-962a-94390d8d33c8 | -11.4281 | -43.578 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bf9d4fdd-2f1b-3b76-a2aa-14ddaf289c09 | -15.8677 | -51.8087 | 2025-09-10 00:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| ee98ee22-f920-37fd-90b8-0f9647a4a2cd | -11.4883 | -50.4083 | 2025-09-10 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| aadb3df7-1b0b-3cbd-b904-65e4002642a7 | -13.9564 | -48.2493 | 2025-09-10 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f8f8b291-b968-39bc-b5ef-fecd0c8d35f8 | -8.0414 | -48.6873 | 2025-09-10 00:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 54acb5bc-1f7b-334e-a03c-dd2b5644d4ac | -5.5703 | -45.0518 | 2025-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bbd388c4-5187-323c-a21e-f597215295de | -12.9673 | -54.7499 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 560c4c82-eb1e-335a-9014-6d4b6017786c | -11.488 | -50.4298 | 2025-09-10 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| f933a0e6-e106-343f-babd-2dbf2d719959 | -5.6788 | -43.3425 | 2025-09-10 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c74cd501-11c9-3323-bd43-2142ecc3166a | -8.7564 | -63.4756 | 2025-09-10 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8c20b2ca-7008-3090-8a58-8910ef9b340b | -5.589 | -45.0505 | 2025-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a73984ad-bb33-3262-a8a7-91ebd99a2c9e | -16.4573 | -50.6773 | 2025-09-10 00:10:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b5587a12-70ad-3dc9-a96d-6dd2b259ad8c | -11.4661 | -43.5959 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 0291a7e1-10e8-39ef-a9ae-248caf046626 | -11.3205 | -46.4992 | 2025-09-10 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 336e3431-3321-36d2-9766-51133e585e9a | -8.0943 | -54.748 | 2025-09-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a2246a42-bb58-3ff3-8bda-d071448660ce | -13.2031 | -45.2834 | 2025-09-10 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f20de7c5-c023-3f30-bbda-595081793abf | -15.8673 | -51.8303 | 2025-09-10 00:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 122fd6ba-2fc7-3214-bea7-c4c314b644e3 | -8.0604 | -48.664 | 2025-09-10 00:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.3 |
| b4ab55d4-7285-3d0d-9429-20be9550d857 | -11.4465 | -43.6224 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 31c77b9c-f5b5-356c-8424-94f45fc91b63 | -13.1178 | -54.8986 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 912d509a-497f-3c6d-ad3b-f3ad85bda013 | -13.1176 | -54.9191 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 295.5 |
| d8cdca10-ffe3-3fa0-b5c0-05fb4599581a | -8.0602 | -48.6856 | 2025-09-10 00:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 147.4 |
| bd1a0961-5fa6-37c3-9145-ba15e8733230 | -7.7705 | -46.0684 | 2025-09-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2945b5aa-34a5-381a-8bde-1c88d5783346 | -9.0768 | -46.9668 | 2025-09-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e3b7f9cc-c41b-3f99-9965-4febb9efec4b | -13.1369 | -54.8966 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 72de45b4-015d-3533-ba13-cce239269112 | -11.4657 | -43.6195 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 2d9e97a0-892b-3217-be26-00deef702b2f | -6.2595 | -43.4129 | 2025-09-10 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5e19070b-94cc-3d87-83ef-8ded03c65151 | -5.5705 | -45.0291 | 2025-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f86e1649-53b5-3b72-a345-5e59826b0a78 | -11.4469 | -43.5988 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| f430deb2-5b71-37e4-942a-c601015bc04c | -18.1524 | -51.7062 | 2025-09-10 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f23aafa0-8a07-340b-8812-ea753152dc98 | -12.9289 | -54.7744 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0dbfc0dc-3277-3b10-b006-a16560e2d1bf | -11.4277 | -43.6017 | 2025-09-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2d4ecf6f-3d8d-38d0-9b91-72582a6d20f3 | -13.1367 | -54.9171 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 246.2 |
| f8b55b13-11f1-3f17-99eb-853b296bbe79 | -10.0155 | -51.7031 | 2025-09-10 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |


[Clique aqui para ver as próximas entradas](README2.md)
