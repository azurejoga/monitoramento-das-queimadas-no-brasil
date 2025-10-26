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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b8e3df-0eb6-3619-8c21-a9d5106ab52e | -10.48385 | -55.61229 | 2025-10-26 05:23:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b14ec16-7fef-379a-a2fc-0e8cfb594ad6 | -11.50251 | -60.73493 | 2025-10-26 05:23:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf7a9cc3-4ece-3a76-b843-3723d0aced26 | -10.94449 | -48.07281 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 274b020a-86ec-3e35-b202-50fd881cb98c | -11.81069 | -57.93951 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f34d02d2-778d-384b-92b4-65122bc4134e | -13.28162 | -47.50666 | 2025-10-26 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ff9f628-effe-366f-b28b-63a480abf362 | -14.83782 | -52.4455 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d05400-0a3e-3f69-9aeb-a62cb7df6bde | -11.74029 | -50.22917 | 2025-10-26 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae0a88d4-48a5-3a22-be55-8b2804b70480 | -9.18314 | -57.68887 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2d213d7-acc0-3598-a85a-42f1119d6332 | -11.69623 | -55.46037 | 2025-10-26 05:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e1d188-1398-36e2-9b1b-03cb9c61ab31 | -12.00533 | -46.78386 | 2025-10-26 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e901760-b829-3825-8bdd-a496166231d8 | -9.73157 | -55.01816 | 2025-10-26 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ac827e7-7094-3cd6-b9d6-342653afb07f | -10.87759 | -48.03412 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43046ecc-896a-31e5-9dcb-24e9d7a0398d | -16.09484 | -57.27413 | 2025-10-26 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6a98e7d-3332-3101-896f-ac7eb4be1581 | -13.43892 | -47.39473 | 2025-10-26 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ac55a50-7983-381d-a21e-e175c18849c2 | -14.4986 | -57.33662 | 2025-10-26 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ba77581-b740-38f8-acd9-8319fba587cb | -10.87695 | -50.14139 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c127a569-2e0d-3773-908a-3300ebcc0744 | -11.21646 | -54.84077 | 2025-10-26 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afdce1d6-99d4-3f38-a3ff-8049478eeaad | -9.28805 | -57.54924 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb76c0e3-0bbc-3bef-8d69-70479bb1c234 | -10.97458 | -52.02534 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfb90a3d-51a5-3e05-97fb-83996ec65b89 | -12.10924 | -52.48877 | 2025-10-26 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 202b858f-3297-3a48-8db2-f12a2ea12b52 | -9.28863 | -57.54543 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 226a78ea-9983-34d1-b7a6-7d4d5c51e6bc | -12.41727 | -57.8047 | 2025-10-26 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6cccf62-ddfd-3cdf-a0bf-84a0f5efeb35 | -11.91028 | -55.37752 | 2025-10-26 05:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 073dd895-3981-39f9-a95f-18664c0d9ec4 | -10.8914 | -48.02759 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0555e89f-3d22-3c11-a274-45693055d2cf | -14.83424 | -52.4327 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 194037ff-3bf0-31e9-a5fb-da95067822df | -21.76054 | -50.04113 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 39c45170-552d-3046-a3e4-c2f65262b253 | -12.863 | -48.65253 | 2025-10-26 05:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a96255d4-241e-330d-8461-bb89d53eb835 | -11.62406 | -54.99856 | 2025-10-26 05:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae50384-1091-355b-bba2-736560e8d408 | -10.82755 | -47.62916 | 2025-10-26 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c28e0890-3650-3f52-ab37-543a2f4eae1a | -14.43695 | -49.95733 | 2025-10-26 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cb7b5ae-4a57-34f4-97ed-a6f47c6686b9 | -15.18586 | -47.233 | 2025-10-26 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca476663-5fc1-3c27-a245-6bbdff32ba2c | -9.68645 | -56.48752 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba9ab247-ab52-3f2e-aa67-cb518b0f2c03 | -9.35747 | -59.39147 | 2025-10-26 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c01b069e-5a6e-30d4-b997-4c0cea7eb496 | -9.72652 | -54.62037 | 2025-10-26 05:23:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f85a7e53-6cbc-3662-922d-e308a6701334 | -10.94385 | -48.07798 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a4107fc-aac5-3648-a4cf-620ed4fd3fe9 | -15.30438 | -50.75845 | 2025-10-26 05:23:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc39361-4145-3597-9d1a-3852ace92ec6 | -14.89405 | -52.47931 | 2025-10-26 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb821731-344c-311f-9af2-5aaf9231fb31 | -9.446 | -56.6514 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e73e928-a058-3f52-b639-cccd81d9753a | -9.45024 | -56.64777 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4bbbc4b-6240-30e0-9092-573336be6dbf | -9.2921 | -57.54596 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5c1f6d6-be3f-3896-9834-a6dbf3a96609 | -10.83408 | -47.63031 | 2025-10-26 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73580825-a337-368d-adae-efb9f319bb8f | -9.18256 | -57.69264 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d85a6fd8-0ecd-390f-8606-00e7b0225698 | -11.21236 | -54.84015 | 2025-10-26 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 219f330d-3a22-320d-a610-f508939ef039 | -9.63454 | -57.0154 | 2025-10-26 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ef557e3-2243-3735-b647-473648e8e797 | -11.10521 | -55.55843 | 2025-10-26 05:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf217df3-90a3-3108-afd3-54376fbe7de5 | -10.88397 | -48.03528 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b53ada3-4f81-354b-a986-91622ccd583d | -11.40134 | -54.6945 | 2025-10-26 05:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81983880-d29b-3dbe-8c26-b0347180367b | -12.00829 | -46.77906 | 2025-10-26 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45be65a6-0275-3374-92cc-4fbd67bfc948 | -21.76008 | -50.04649 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b4df603b-8410-32f7-9e6d-4a21d33eb833 | -11.81476 | -57.93615 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e34e5d1a-dcc2-3617-bc99-e099446d5a20 | -9.45385 | -56.64828 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18d2c45b-df2b-3bb4-bbe3-9d9576797f8a | -12.00603 | -46.7773 | 2025-10-26 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29588d3b-86d6-3b3e-bc8e-23fb14f81bff | -14.76576 | -46.61908 | 2025-10-26 05:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c26bb758-aacd-3a28-a891-77b800327fd8 | -10.89203 | -48.02234 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efc16c6c-dcfb-386f-b785-98b3b84a4b31 | -11.05856 | -48.33685 | 2025-10-26 05:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc47d339-1119-336a-8bc4-2d7cfdd32b1b | -10.61215 | -47.99884 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d369cb9d-237c-3cbb-8503-4b188b64238c | -14.43418 | -55.91724 | 2025-10-26 05:23:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0328a232-2d26-3ddf-a283-1d0de025c39a | -11.06477 | -48.3385 | 2025-10-26 05:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07a15014-3ec1-3d23-a441-3d913672f87c | -14.9162 | -52.46648 | 2025-10-26 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51f11f18-9e1b-3da3-8d21-c9e6f9f5d303 | -10.82816 | -47.624 | 2025-10-26 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a08d76b-ad99-3c25-9be4-ca2b51ebac7e | -10.87182 | -50.13688 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91db0bfa-005f-369a-ae00-7c71c13c6c92 | -9.44961 | -56.65192 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4803903-06df-39fe-b718-828638ff5af3 | -14.92125 | -52.46741 | 2025-10-26 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f44d841-ea3a-3380-9833-1bb29e96c59b | -13.76938 | -56.12648 | 2025-10-26 05:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f07ab03d-9275-30cf-ac4e-203a2a5e1021 | -14.4429 | -49.95796 | 2025-10-26 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76a6d8f2-a92c-3827-adc7-5a25449e75c6 | -11.43961 | -54.09404 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b07cecb7-a7e8-3a49-adb7-7343f44fde6e | -9.44662 | -56.64725 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 754dac64-d240-32d9-83c1-5be2b3707faa | -14.83933 | -52.43325 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37f4882d-aace-3f08-9703-ceebcfba9afa | -21.76024 | -50.05215 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8be3282e-825f-3c04-90e0-7215133261c0 | -11.7296 | -59.31437 | 2025-10-26 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f44179a-3844-380d-b1a3-d0f67dac35ef | -16.7433 | -52.32328 | 2025-10-26 05:23:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b4cd5e8-ad02-374f-be18-6cc278389c42 | -9.72597 | -64.0743 | 2025-10-26 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 295a50c6-db2c-3dce-a811-50b06a245f40 | -15.93929 | -51.06051 | 2025-10-26 05:23:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8955eb56-a387-3408-82c5-1f850e23026b | -10.22036 | -49.85081 | 2025-10-26 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e1ee27b-8842-32d9-882f-bcaed758814b | -14.22002 | -49.50924 | 2025-10-26 05:23:00 | NPP-375D | ALTO HORIZONTE | GOIÁS | Brasil | 5200555 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 741ba874-0b79-3381-adb1-323921445c22 | -11.95936 | -55.25919 | 2025-10-26 05:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff01ec18-adea-3f08-bef3-4bae3769b60d | -10.48704 | -55.61771 | 2025-10-26 05:23:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 080d00e8-a2ff-350e-83c2-e3e6b9e75bdf | -12.89343 | -54.73645 | 2025-10-26 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f572f06-02f8-301a-8bd4-6ed82f12c771 | -13.91896 | -48.37691 | 2025-10-26 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b1a2121-7589-374c-8661-7ee9455f8be2 | -21.76112 | -50.04121 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9b3f318a-1626-3133-9e43-0027d293d912 | -11.53911 | -47.1018 | 2025-10-26 05:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a00a80f-460f-3b22-8524-2908556f96f6 | -10.94661 | -48.06898 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6974b565-a6d3-3641-89e0-d710c7e2ce52 | -12.42058 | -57.80646 | 2025-10-26 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 962feaa0-195f-327e-bdba-af220642b087 | -14.76638 | -46.6174 | 2025-10-26 05:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| abe914e7-4198-38b6-b6d0-67f32737b1c3 | -12.42079 | -57.80526 | 2025-10-26 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 46e387e4-7dfc-329a-8b8b-236068868bb7 | -10.88454 | -48.03046 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 406570f0-71ae-3469-95e2-9e4bd033c031 | -10.22603 | -49.85155 | 2025-10-26 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bca1180-d55c-323a-9c5f-fb9bb8e50857 | -11.73983 | -50.23301 | 2025-10-26 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c506f3-e733-3f41-974f-08a57e7805f3 | -9.97534 | -65.11349 | 2025-10-26 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a278ad5-f043-3afa-9c1a-dc3211abd7d6 | -21.76664 | -50.05297 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8c8bbe45-7557-3dd6-a879-54a20aa4a355 | -10.39835 | -57.32545 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d680fcc7-8e34-3c67-813c-01590f31aa0b | -14.83819 | -52.44252 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfa4cd1b-17d1-3b9b-ba55-f9dc6af412c6 | -10.48772 | -55.61286 | 2025-10-26 05:23:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55f9c3a4-b4c8-3d88-8948-7e7c9db760f9 | -11.81127 | -57.93562 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 658641cf-d371-3173-940d-4bca4ca5e75b | -11.24868 | -49.86455 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c4207b5-3d19-397b-bac0-629d74421b00 | -21.76648 | -50.04726 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2e8cd209-f27f-3e4e-802f-796d0a289a2c | -11.43763 | -54.0954 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5d5beb-4d3f-3c42-a91a-a824339e96d8 | -12.04442 | -54.23539 | 2025-10-26 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5a290a2-2d17-3aa9-bfe5-4eb0ec5f5cbb | -11.36356 | -54.31299 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a8c0634-9c95-3d6e-b7b0-84ff6f5e0c96 | -10.95088 | -48.0737 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README52.md)
