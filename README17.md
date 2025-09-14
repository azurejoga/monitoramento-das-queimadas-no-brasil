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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c19adb8-840e-35ac-8c1d-c09268425fd7 | -11.49227 | -43.63146 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 455f5af7-7c53-352d-9650-2a321ef6166a | -12.75729 | -48.00737 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c023019e-94da-3345-a8be-1c0e63e02958 | -12.78618 | -48.00469 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6e4f01b3-3b79-3e8a-be8e-46799d261e37 | -6.10158 | -45.94817 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21e14647-dc39-3b0a-886b-97b3f4d28109 | -14.2838 | -46.12201 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30fbe3cb-70d2-3b71-8b01-34f96da7592a | -15.99394 | -47.94324 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a02bb68-8a10-325e-aee2-121dc57379f6 | -15.93308 | -49.97152 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95581bfb-6930-318b-8114-38d35c82e8d0 | -15.19937 | -52.49516 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 78cb53e8-496b-398a-8135-cbba3415d536 | -17.29248 | -46.12253 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9482416-ca36-345b-a153-2a72d733084d | -15.63567 | -44.38065 | 2025-09-14 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da7e207-8781-3d06-94d8-ebc5def3219d | -17.25969 | -47.24574 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82d815d8-b094-3b7b-9c99-d3cacd662490 | -6.25784 | -43.47727 | 2025-09-14 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c920e6f-19c5-3b5e-8221-7a4e4fd60510 | -13.89529 | -48.30606 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a2bec2f-f540-37f2-9ee8-79709660e026 | -12.92943 | -47.94288 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ce1b415-196f-3df4-a04a-0d92394ffd1c | -6.42627 | -42.62467 | 2025-09-14 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bec7177b-96b0-33ea-98ee-4b384ff7016f | -15.23431 | -44.03548 | 2025-09-14 03:49:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1a54e8-cb64-3ee5-a0a1-a596450c8285 | -12.76258 | -48.00723 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20e199f9-f060-3652-bef4-d8165637a5b5 | -11.78061 | -46.62744 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f67f69b5-a6fa-3731-93e4-7cf96d722770 | -15.60228 | -47.94407 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf1516bd-ee9c-342d-8e0f-7ad48c7240a1 | -11.46253 | -48.70787 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cbdc9167-2197-34ac-ad73-64a6adb819d6 | -11.29575 | -50.83083 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e259d2-a447-3257-8cdd-ca4830f2e545 | -12.04306 | -46.5514 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fad1ae86-191f-3e5d-8d2d-fc55ace802c6 | -6.17546 | -41.17231 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3cfd6007-aa93-3451-aae2-af3b9a686f9a | -15.76209 | -52.23979 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9f7c24c0-d660-3fe1-a371-9d12f3d2d551 | -15.12861 | -52.49169 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01813042-e7ff-307d-afb0-8ef2f24d4de9 | -17.43139 | -49.22447 | 2025-09-14 03:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38693ab0-a32f-3df2-aca2-72ca186ce8b2 | -12.245 | -46.7859 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 940a2068-cb94-3294-9c6f-62b456faa159 | -14.18702 | -44.79529 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aace7924-80fb-366f-9f45-46b2f3ba1c35 | -14.63675 | -52.11211 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 211a1850-7a76-3b8f-b179-901fba0b5a8a | -16.2873 | -45.68537 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5ed6d00-8e7c-3a59-9e9d-560f40e1153e | -14.48223 | -47.35032 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4114b463-9f5a-37de-bc4d-8579d602b77a | -11.45921 | -48.69934 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99eae02f-e67a-34ca-a5b0-14fe9ce6f65e | -12.96647 | -48.04217 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2652bace-be26-31ad-8bb7-d18426cefe1a | -6.01546 | -38.64646 | 2025-09-14 03:49:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7629bfec-7dd4-3575-9401-6eb7f0383b60 | -13.90596 | -48.30938 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32527e62-f6eb-38be-9568-eac826f63aab | -10.9018 | -47.20674 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebb1ec84-af7b-3b43-a161-e35bac866e86 | -14.63206 | -52.10994 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fef636c4-3a66-34c7-8628-72a2e63e1f68 | -16.18686 | -43.13473 | 2025-09-14 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f968efab-17ef-3f86-90cd-1d68045d9983 | -12.96575 | -48.04586 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 65ce882f-acef-3fd6-abfb-a3cb8e1b7b38 | -17.99915 | -46.96237 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9af97b6-3455-3028-bcc8-8c532b059ed1 | -6.79856 | -43.40482 | 2025-09-14 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e3209771-b3df-3e92-a2d8-8e1933b7cae5 | -17.01512 | -42.11281 | 2025-09-14 03:49:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c68931a7-0985-3167-92f2-6daa81ef9bda | -10.32228 | -48.82893 | 2025-09-14 03:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4c7e5a8-89b3-3d83-a1c1-56be3327c208 | -17.31328 | -46.08652 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a0913e-36bc-35b4-a71b-aa55eed8d973 | -12.08841 | -44.87487 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deffef53-33a1-31e5-8dcb-e794f3d47e1a | -10.75948 | -46.4666 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a289e1f0-0cc7-376a-a706-ce56e06e729e | -12.1445 | -47.58411 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3a56b02-16e1-31bf-8483-75eb26b24fd9 | -12.78422 | -48.04309 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb686c97-33ee-3188-bf21-2d39490118f5 | -17.31483 | -46.10238 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c72ddcce-b52d-3589-a19e-dd2e94183926 | -12.08502 | -44.72857 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a369da81-ee23-33b5-8094-4201a50989fc | -16.64475 | -49.76616 | 2025-09-14 03:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17823798-57b3-35c3-9bc3-9b5235a6bb70 | -10.89581 | -45.56071 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d77cc4b3-9782-3a21-8f76-ea504285cab0 | -15.15511 | -52.46907 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 857e85e5-6c11-3706-8eb0-8ae906f69f23 | -17.0689 | -47.15699 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27a5debf-428d-34f9-8ad4-1ffb0164bbac | -11.66886 | -46.5076 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc9cc8bd-7e01-3482-b358-717c65b8a880 | -17.28991 | -46.112 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ed31cc-cb0d-38eb-9553-412d83e50601 | -12.75877 | -47.99998 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 312e8883-2da3-34be-8c7b-9539db8e3229 | -12.0841 | -44.89821 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9102d353-7677-32ae-b757-77340dbae4e7 | -17.0146 | -42.11162 | 2025-09-14 03:49:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 560bd4fb-c3a0-3cd0-972d-c02d71082b29 | -17.30419 | -46.10974 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a49fb229-9038-334c-8bcb-0abf71b46682 | -12.77282 | -48.01291 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6e9626af-d2c7-3863-8412-6ad1758d1950 | -10.91411 | -45.56932 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e328be70-c374-3bf6-a4c7-ee6c603def53 | -14.40816 | -46.40278 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c621671a-e9fa-30bf-bb3f-76f21bb9bff7 | -5.39526 | -40.34589 | 2025-09-14 03:49:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ac0ffe98-bdfc-302d-a668-1ee99b06bd91 | -12.94551 | -48.03353 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4899880b-d206-36bb-a149-1c398833ad98 | -18.8412 | -41.91906 | 2025-09-14 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7eca1a5c-c464-3b54-8b70-c6f197b1740f | -12.80302 | -47.14452 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 49e552ac-bb32-3f1d-afc7-769dbbc31601 | -12.75642 | -48.00977 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1548520-bfe4-38fc-a493-e7198392b95e | -16.50381 | -42.12703 | 2025-09-14 03:49:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2f434d4e-d2de-35af-b6b7-c763bcfd3a6a | -11.46717 | -43.57838 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebbb1c2d-4d55-31ef-9e56-c31f56f420a0 | -12.74267 | -48.02223 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9f1aa6bf-6147-331f-a58d-49354f163159 | -11.47835 | -43.61253 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 504464c6-0a87-3ba9-b2ce-75053833b7f4 | -13.90672 | -48.30563 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2a1c6cc-e84d-3ff0-9229-b0615496b7df | -5.98424 | -43.77932 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5419a17-aacb-3061-808f-e1875b797eaf | -14.61664 | -52.04209 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| edcc012e-106c-38bf-b185-0402c5a31488 | -11.35613 | -43.49552 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b890a6a-91d8-3bae-84f2-06f4d9e0d890 | -17.35195 | -42.62526 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 912bff93-d395-36b6-b0f4-b7c05b5123da | -11.30902 | -50.83363 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 782bfec2-bdc8-318d-a4c9-790eccdf2f45 | -12.78132 | -47.9981 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7259022f-e721-3374-ae14-7da30aab44a7 | -11.84641 | -50.50246 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8a43ed1-3e7c-310d-89b4-ba640980f642 | -12.77843 | -48.01513 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1c95e57-cf15-38c6-9142-bf5796a69726 | -11.05039 | -43.24675 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12199a8f-f5ce-3e61-b6b3-b30d877ecdec | -12.11769 | -44.84175 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f3da043-ed3d-368c-b4e8-2ac91dfde527 | -5.08847 | -41.16145 | 2025-09-14 03:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29401ca0-0f9b-345b-a788-315a00d313ce | -14.47243 | -47.31977 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a55cf1fc-f41e-3287-ac87-2049fcde72db | -14.33488 | -46.62495 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4158fb4e-fa05-30ad-851a-3a5866a9c8cc | -11.49452 | -43.69263 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179aac8e-dca7-36cf-ba1c-34ee7338222a | -16.11943 | -52.1671 | 2025-09-14 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e126397-f47e-3935-88fa-13b4848462d3 | -16.33509 | -51.52284 | 2025-09-14 03:49:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c740677-fa76-3f32-9749-2a12e3d7e75f | -12.80665 | -47.95848 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7f9a844-c06e-3af0-953c-2eb8a4624423 | -13.93702 | -44.84932 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00885ba5-8a45-3a51-b1bc-c1ab1d5519ac | -11.46306 | -50.76059 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04fc6681-b83f-38cf-b38a-e2f4399284cc | -15.66414 | -44.69094 | 2025-09-14 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d7b561-ae13-3d27-b29c-4f56117a6d56 | -6.65471 | -46.08825 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d63e3b0f-4912-3e1f-90da-7432f23d357a | -18.0867 | -42.93658 | 2025-09-14 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7d3e12d9-0e25-38d2-9426-f244176dba66 | -11.13374 | -45.31402 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de7f9f25-d515-367c-8b12-acc6bb406c9d | -12.24637 | -46.79106 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5969416c-0117-3389-a2e3-64264512b47d | -11.78159 | -46.65007 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36259bb7-935d-3a59-a958-3eb16848afc5 | -15.43257 | -47.35577 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0aa77d6e-fa40-3a55-8dae-6e82dfa39a1a | -13.94108 | -44.82751 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
