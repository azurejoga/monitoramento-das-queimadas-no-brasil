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
| 6eaec961-2fdb-328d-9036-08ba79389042 | -19.35707 | -43.69633 | 2025-12-26 04:40:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93781144-5e81-389e-b3b2-087b380bc9b8 | -16.14028 | -43.5609 | 2025-12-26 04:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b72c0163-319b-3542-b9f6-f6b24e52c31a | -13.67086 | -46.2775 | 2025-12-26 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f67c07df-bdf7-3449-9831-8780a41ba222 | -13.36076 | -41.34052 | 2025-12-26 04:40:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 792564c6-61bf-3813-bb39-a44f72135a7c | -16.14084 | -43.55643 | 2025-12-26 04:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4358f1ba-c90c-3139-8e32-3fd5183441f0 | -21.24988 | -49.27527 | 2025-12-26 04:42:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 55b3da9c-6b9b-3580-802c-1259c233cead | -20.20446 | -43.61558 | 2025-12-26 04:42:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ce55be72-1824-3599-9b14-20f5f6451002 | -20.19963 | -43.61597 | 2025-12-26 04:42:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4337ab87-ba6c-3c6d-8366-f2a29f1ac238 | -20.19312 | -43.63113 | 2025-12-26 04:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0f55f95f-1937-30b4-9e0a-65bf54490ca8 | -20.19366 | -43.6264 | 2025-12-26 04:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a59e3d54-8a0b-309b-bbf1-ef61fd7887cf | -20.19902 | -43.62132 | 2025-12-26 04:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 245f87f7-ff96-3468-91b2-c5cbaad501b4 | -20.20388 | -43.62056 | 2025-12-26 04:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 00f40044-f511-3a54-92d5-a9fd985dc491 | -19.32716 | -49.38272 | 2025-12-26 04:42:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb48bdab-a082-3838-95c4-ebe6048af8be | -20.59826 | -51.6096 | 2025-12-26 04:42:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a744c3ae-d949-3d19-8064-f426fe7fbae7 | 3.8175 | -60.51775 | 2025-12-26 04:55:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef71482-d9c2-3375-a408-0c03068b9b86 | 4.07291 | -60.16372 | 2025-12-26 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a73d3267-0b1f-3c2f-aeca-2ffc7f0ef6bf | 4.07781 | -60.16216 | 2025-12-26 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84d276df-146f-3a94-bb38-72bd519832bf | 3.81794 | -60.52076 | 2025-12-26 04:55:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2625bd82-97a0-3599-b26b-b802e21b5545 | -2.37394 | -51.90559 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 269eaaff-9391-322f-afc2-8fbf6dc2ebac | -3.6547 | -48.93611 | 2025-12-26 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4659ed54-4ef4-3501-87eb-92b40b7eccb0 | -1.59207 | -54.06182 | 2025-12-26 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a86bd88-4214-39dd-b8bd-0a440f4d7bbd | -2.36662 | -51.90813 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d070e0e-844b-3499-a7aa-092e4f338a25 | 0.46943 | -60.41851 | 2025-12-26 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e2ec5f2-e5de-3c08-bb11-fbf3e2a2d0c8 | -2.37 | -51.90865 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fcf6886-47ba-3968-978b-96754518a9e8 | -2.9086 | -51.84995 | 2025-12-26 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5af9bec7-fd10-365b-b40a-9632ac3f800b | -2.90237 | -51.84529 | 2025-12-26 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dee5bdf-4a1c-3a7e-a951-b89b9273add6 | -3.14174 | -50.20357 | 2025-12-26 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 793562db-3c34-32b1-8b17-d101699b5dde | -2.37281 | -51.91278 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 324c85b3-620c-3405-92ad-aa8b0562e53e | -2.37056 | -51.90506 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f399e824-186e-36cc-80ba-fb26e1c5a8bb | -2.46268 | -47.77701 | 2025-12-26 04:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dca00cf8-3ab6-3cb7-9321-97de05fb8547 | -2.36718 | -51.90454 | 2025-12-26 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4acfe013-b1b1-301a-a49b-5754760e0e79 | -3.37394 | -52.67423 | 2025-12-26 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e673f759-3eba-3129-9850-449aee9c3cdf | -2.90577 | -51.84581 | 2025-12-26 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 460e44b5-1f1e-32d9-a85a-c1246bb2df0e | -12.55678 | -54.75827 | 2025-12-26 04:59:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad1b1523-36da-3439-b32a-467c58dd9894 | -20.20451 | -43.61934 | 2025-12-26 05:01:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dbca5270-68fe-3692-b23e-f5c04c5105bf | -18.15366 | -46.94104 | 2025-12-26 05:01:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83d1d72c-eb04-3c27-88e1-aea35904719c | -15.95533 | -57.73805 | 2025-12-26 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecd0fd2c-feb1-30ad-9443-1df2c50b18c9 | -20.92937 | -56.19621 | 2025-12-26 05:01:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fb07954-56b3-3ff1-9c2c-af9e2b8529c6 | -14.30212 | -57.58446 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be7db293-eebe-3d49-87f0-d3e8457dd431 | -16.13719 | -43.56384 | 2025-12-26 05:01:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1071dcbb-2c0b-39a1-a3a6-3374b3b99ba5 | -14.29814 | -57.5876 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bdaf2007-4d87-3f56-a512-71cf207da49f | -14.30549 | -57.58503 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df60af21-1351-3401-a533-97eb1d49f458 | -14.30151 | -57.58817 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1966d51-f1f2-33a5-8d89-31a0bc6fb264 | -15.46014 | -57.82035 | 2025-12-26 05:01:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d96979d-657b-3946-9303-c67a0e4108f9 | -14.29875 | -57.5839 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c45bafd-efa2-36a9-9b5e-0dc9770d2c63 | -20.18967 | -43.62989 | 2025-12-26 05:01:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a9e18cd8-b92a-3dfe-92bf-ae4c09c9d7f8 | -16.32185 | -53.79189 | 2025-12-26 05:01:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1a41366-cd4a-3f4e-98f6-c8e7b9c34860 | -16.13778 | -43.55785 | 2025-12-26 05:01:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 880ab52f-767a-3f86-a2b3-b2c986d38d00 | -18.15797 | -46.94379 | 2025-12-26 05:01:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca667508-6413-366a-b02a-ecee18597c3b | -20.19725 | -43.62252 | 2025-12-26 05:01:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a558e5c-b395-35f5-92e4-aed42a411840 | -18.15242 | -46.94284 | 2025-12-26 05:01:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c7d8651-fca6-31f7-b2bb-8e0dddf918ad | -14.30488 | -57.58873 | 2025-12-26 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2c2ad1b-1f8d-3d4d-bebf-d155c971da02 | -17.65009 | -56.44576 | 2025-12-26 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 12751c96-e6e6-34fc-8d8e-c59737fb6635 | 3.81195 | -60.52377 | 2025-12-26 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c956b1a1-9677-314f-966e-162f8c57c82e | 4.07212 | -60.15737 | 2025-12-26 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6348d134-a5fb-3215-891b-0ecfabd79e8d | 3.45015 | -60.642 | 2025-12-26 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac54ebb1-d1ae-32d7-b686-e6efe75c93bb | 3.81121 | -60.51908 | 2025-12-26 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a456710-44a7-3047-868a-34c931bc7ea9 | 3.81487 | -60.52146 | 2025-12-26 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb398f83-9640-3d09-a35b-8ea6ba0c6b82 | 4.07286 | -60.16203 | 2025-12-26 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21df14cb-d255-3689-9724-58a76cc0fcda | 3.81107 | -60.52208 | 2025-12-26 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 544fcbba-6287-3e7a-9392-8d09edd4d85b | 4.07374 | -60.16027 | 2025-12-26 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b19a47c7-6d23-3617-8407-2d68cce1d110 | 0.46607 | -60.4186 | 2025-12-26 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11197adb-69e7-3dcd-baf3-18f3a8f97123 | -14.29794 | -57.58817 | 2025-12-26 05:52:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00c39bab-e0c1-3382-87d4-0125f582c659 | -14.31043 | -57.58573 | 2025-12-26 05:52:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7dbe627b-9315-37ee-bd00-f3e96cccbdf6 | -14.30394 | -57.5892 | 2025-12-26 05:52:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c64c6819-659d-3915-afad-04baca3d9072 | -14.30443 | -57.58475 | 2025-12-26 05:52:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ea14959-ab19-3ff0-b375-b0038bccdba9 | -14.29843 | -57.5837 | 2025-12-26 05:52:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 044228fb-2282-37ad-b0eb-75f886fa6814 | 3.81171 | -60.52338 | 2025-12-26 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 555a06d6-bd02-3bc9-a6ab-489ec76bd90f | 3.811 | -60.51918 | 2025-12-26 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc7a409e-541f-3748-af7c-931e4e11eff9 | -8.85295 | -44.16766 | 2025-12-26 12:36:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3ffb4017-6e06-33c3-8cd4-4414d85586c4 | -11.7404 | -49.08062 | 2025-12-26 12:38:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2deb00b0-96ac-3967-abea-cec1e160e392 | -15.51888 | -51.87157 | 2025-12-26 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b3ba75e7-5560-3315-9335-ee7dcd4e42c3 | -15.52038 | -51.85951 | 2025-12-26 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 195.8 |
| f95874e5-8504-35ca-8775-37aede270558 | -22.59859 | -47.99593 | 2025-12-26 12:40:00 | TERRA_M-T | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e53a2dd7-b656-329f-9ef4-0957c2c05525 | -20.49682 | -52.87194 | 2025-12-26 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 178e4e1a-cfc7-3bb7-bf07-58be41fe9c78 | -17.68792 | -45.3773 | 2025-12-26 12:40:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7f3db516-3702-3ce7-ab30-626bf73ff2e9 | -23.00583 | -54.97736 | 2025-12-26 12:40:00 | TERRA_M-T | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 4d1daf33-9394-3ea1-83ec-c205c8e43728 | -22.21544 | -49.65203 | 2025-12-26 12:40:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 7f39817e-9998-3aa0-9a53-ef39e8349402 | -21.4398 | -52.97647 | 2025-12-26 12:40:00 | TERRA_M-T | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6de1a9a9-2034-3d27-9bdc-cda9d871ff42 | -25.34627 | -54.24134 | 2025-12-26 12:40:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 49841ec0-561a-3288-8d7b-662e5451f244 | -22.59727 | -48.00252 | 2025-12-26 12:40:00 | TERRA_M-T | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a7ec2742-5947-3f4b-87e3-f4ff54754132 | -17.74141 | -49.11117 | 2025-12-26 12:40:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5578b677-c12d-3983-97d0-65c716d2ad2b | -21.4355 | -54.07317 | 2025-12-26 12:40:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b4c45e8a-7624-30fb-a896-e0444b1d9577 | -18.97714 | -49.46053 | 2025-12-26 12:40:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| da9ca1c0-950b-3ece-943d-2c9d114beb94 | -20.38469 | -51.73584 | 2025-12-26 12:40:00 | TERRA_M-T | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 022bffac-5d7c-372a-82b1-dcba5c840489 | -23.87226 | -53.89285 | 2025-12-26 12:40:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| f32b1ffe-bfd5-3cd6-a458-23bf3b434cd1 | -20.56995 | -52.93858 | 2025-12-26 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9e6140ae-6a37-3fc3-bb64-8e45f6365cc6 | -24.86879 | -49.2172 | 2025-12-26 12:40:00 | TERRA_M-T | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 6eae538c-7890-3bc6-ae82-65a252e8a535 | -22.17895 | -50.27592 | 2025-12-26 12:40:00 | TERRA_M-T | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 6c01eed2-4e25-39ed-b0de-dae803354a7b | -16.07629 | -56.59204 | 2025-12-26 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ec41074b-559f-32e2-b5ac-190288572006 | -21.68518 | -47.13396 | 2025-12-26 12:40:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 32.7 |
| bb54bd2d-c85c-3147-bf46-e346dfc12603 | -22.2132 | -49.67438 | 2025-12-26 12:40:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 0afe90cc-b44f-3326-b7a4-ba9075a5d3d6 | -23.04509 | -51.81017 | 2025-12-26 12:40:00 | TERRA_M-T | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| d0775621-efe2-3e61-8442-46bf619b1cbe | -20.81644 | -49.49608 | 2025-12-26 12:40:00 | TERRA_M-T | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 457f579a-ced0-3af6-9a76-e2972f1ddbb2 | -21.67904 | -47.13893 | 2025-12-26 12:40:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 0a556f53-c71f-380e-b078-9f6a1e3f24b6 | -22.56273 | -54.65864 | 2025-12-26 12:40:00 | TERRA_M-T | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 9ea66305-2969-3ae6-8628-7bb28ad13919 | -24.41944 | -53.82983 | 2025-12-26 12:40:00 | TERRA_M-T | MARIPÁ | PARANÁ | Brasil | 4115358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ef713fc0-f283-3007-b28c-0c09742f6c30 | -27.8702 | -51.06311 | 2025-12-26 12:42:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| d3b82c3a-26da-370c-9b8d-45f183370dbd | -27.78165 | -51.17997 | 2025-12-26 12:42:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 441cf624-22a2-3e3f-a55c-f94037a334ce | -27.87216 | -51.04163 | 2025-12-26 12:42:00 | TERRA_M-T | CERRO NEGRO | SANTA CATARINA | Brasil | 4204178 | 42 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |


[Clique aqui para ver as próximas entradas](README4.md)
