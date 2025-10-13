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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91feb997-1d49-35e2-8df8-2c42bdbb6b4c | -14.27197 | -51.50422 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b22b8b-bb78-38b6-941f-58e1dc31a4ed | -14.18858 | -51.50203 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6096dd1d-35e8-399e-898d-d19cdb9f70cf | -12.76838 | -50.67729 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 07837218-c643-3d13-b2a2-b76302d6edea | -13.84242 | -45.53434 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df664237-4e4c-3a10-9f89-038d63fa3f77 | -12.92754 | -47.04455 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eca5d1b5-a61c-3be4-9265-d816d08d0023 | -12.92638 | -47.05176 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2694bbc3-d180-36a1-aa89-d6329fc7d4e2 | -17.88478 | -45.00456 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17e9110b-f1c1-3cb8-8574-f123862b28c7 | -13.87817 | -45.48082 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b544490e-1273-39cf-b146-943b7e417b1c | -12.95122 | -47.00422 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 953560c3-b984-382a-9050-7db9aed3c757 | -12.9303 | -47.04873 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5cc8aa1-7b1e-3097-8673-b8bc6c81ba03 | -14.20835 | -51.51403 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3fcce123-a606-3e31-a49c-5975d85c433b | -13.82451 | -45.49436 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ef01100-a3f5-3670-b5d3-80ff16d7c796 | -14.21936 | -51.52158 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5e7a23b8-9524-3d07-940e-f6cec91182bd | -15.66295 | -43.90261 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43246b4d-3fe6-3fc8-9954-3b18ad0dc42b | -13.49685 | -51.31128 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2164c780-36e8-368f-beeb-dc93782e2682 | -15.02357 | -48.74633 | 2025-10-13 04:25:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0cfe1ac-5cf0-38a9-b89f-3d048773390e | -14.18975 | -51.5187 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d67c1700-5d7c-34e6-af05-c702539e0f19 | -14.30222 | -51.54281 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53cb80a6-1a89-3774-9577-0e1e45fe997b | -12.77614 | -50.67871 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 674b45be-3ede-3f84-9935-2d31094c248c | -13.27412 | -47.78918 | 2025-10-13 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f343b27-e9ba-3c26-826b-19653e789e90 | -16.90762 | -43.9581 | 2025-10-13 04:25:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d27d56a-6d9c-3b19-8215-09b6ec67a9c6 | -16.31746 | -43.10342 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b943130c-a382-39b3-8184-146dfde2d0fa | -13.86308 | -45.48948 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d5aa4bf-fec9-3b72-a8bf-a93134b21bf2 | -13.86696 | -45.4419 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da53ed07-d2fb-340c-a265-a1e11b5b96b4 | -16.12467 | -53.97549 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d2e494e6-441a-3811-b467-9133b69e05d9 | -13.84465 | -45.5421 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46f00dab-a6f7-38a8-8493-40b7ecffad6b | -16.11926 | -53.97931 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2187d25-2f16-3101-af87-60f9b957d467 | -12.93568 | -46.99421 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c6daa81-0b7f-3a18-b5bb-77ce6eb0914a | -17.32174 | -53.80626 | 2025-10-13 04:25:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab1cebde-0677-3c83-9248-cfc8eb766995 | -17.89178 | -45.00567 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42846095-cc7b-322a-a1ba-e785f06161a7 | -17.89587 | -45.02688 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b339c93b-6246-399a-b169-43885b70a9cb | -17.87606 | -45.01552 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 289aef7e-42f3-3c31-b4df-a505bd94fe80 | -12.9502 | -46.98932 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b3d5a84-3201-387b-b392-db11ab2a241b | -14.20759 | -51.51112 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53321308-cc4b-346a-aa33-bcedb6b1cf5d | -13.27071 | -47.78873 | 2025-10-13 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb998e25-2f02-3e59-8168-1851aa9a33e7 | -12.95688 | -46.99042 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da6a1a87-307d-3019-bc4c-22d5ae8737a0 | -14.21956 | -51.5134 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce84ec40-4cdf-3aa6-9777-328e95276929 | -14.30976 | -51.55109 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffd6df75-fd6b-3ad3-85ff-44c0d9f8cbdd | -13.8519 | -45.51736 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da250b9c-9eb5-35c7-ad78-80a63677a53e | -15.65876 | -43.90622 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4e481e5-af01-3700-8099-65eadf282d7e | -16.90824 | -43.95372 | 2025-10-13 04:25:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c267604-db6e-3b97-b805-e2c58485159c | -16.12556 | -53.97076 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 67235343-9ca0-32c8-8f07-62ad36bed476 | -12.94628 | -46.99232 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a48b384a-be82-303f-96ac-20ef5e3c232a | -14.30621 | -51.54358 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ced0bdde-64ba-397d-9bbf-588232130269 | -12.95296 | -46.99343 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f157819-13ad-3a7e-8630-2a67776dac80 | -17.88828 | -45.00511 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b095f88-98d1-374c-8034-d16ba8c0c9cc | -13.64486 | -43.61963 | 2025-10-13 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11731e6a-bdd1-3e2c-a9d3-795419ab5bf3 | -16.76604 | -42.3078 | 2025-10-13 04:25:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dac39c81-a025-3ad8-a162-e3837c1a4f4b | -14.29823 | -51.54205 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4154970c-3c1d-35d8-978d-d23b1a4f1921 | -15.66121 | -43.90067 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 780302f6-e024-39d2-8df9-45f5d92a52c5 | -16.1676 | -42.85131 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ca049f0-fee9-3701-82ce-b26c5c52422a | -14.21557 | -51.51264 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0f3bf480-472f-3e40-b048-6b661773eb3e | -11.74347 | -54.71905 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04c401b3-8939-36a2-87cb-45a8eb78fed7 | -14.24997 | -51.48913 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0314804c-56b2-3741-bc3c-b338101c7306 | -14.28415 | -51.5284 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32aaa539-abf1-36a2-ac5c-060a46d6ac89 | -16.91187 | -43.95424 | 2025-10-13 04:25:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32f50e4c-4154-37ee-a6d4-03f3a2cfe287 | -16.21522 | -59.13379 | 2025-10-13 04:25:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 58773d06-0b8b-314e-a17f-74199397d386 | -12.74403 | -50.65568 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ac87a3e-d623-3b1a-abe7-c0c9f435bd64 | -12.93902 | -46.99476 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7df59ad1-0b7c-3d16-8813-9a61add46cb2 | -13.75458 | -45.64939 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bcbd680-8a35-30d3-b8e7-91c51a8fe6d2 | -12.93788 | -47.00188 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bbf6679e-3d3f-3015-a711-8398a9a2b64e | -14.19069 | -51.51339 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60367bc7-26ea-373d-ab9a-79295743a732 | -13.43574 | -47.91145 | 2025-10-13 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b06fd64-2591-33db-ade2-be7753df5dd4 | -17.32524 | -53.81176 | 2025-10-13 04:25:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f06bd6-1c18-30b9-874b-a0a97375007f | -13.88096 | -45.48498 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a43b8f54-0eec-3afb-8111-460aa1195d85 | -14.18764 | -51.50734 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ccbe904-b1a9-37f9-942a-c3f8a07cf5f5 | -14.30834 | -51.55495 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 402d5492-2f7e-36e0-a064-b6d03bd7373d | -19.7959 | -42.36707 | 2025-10-13 04:25:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1058b2c1-31e2-31c8-a315-149e58fadc05 | -16.11838 | -53.98397 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e24e389a-e045-3bd6-b9b3-ae9e96b44db6 | -13.43234 | -47.9109 | 2025-10-13 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd4a71f9-263a-3a7e-b609-216a6728b617 | -15.70142 | -42.18473 | 2025-10-13 04:25:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64fa2add-838c-3880-aa3b-2f9a6a603023 | -14.29518 | -51.53598 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 418c7e03-13f6-30bf-a301-0307845a67da | -14.25337 | -51.539 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 771dcca7-1840-3ff7-a926-601ddc8a11b4 | -14.3074 | -51.56028 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9387f15e-3378-3b2f-82c9-cc102176da5d | -15.02013 | -48.74569 | 2025-10-13 04:25:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3f0df4a-9c45-3fae-b4af-807b6faa47aa | -13.43975 | -47.90831 | 2025-10-13 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9cbc40a-3b19-3c45-86e6-8c24897ba446 | -13.43636 | -47.90772 | 2025-10-13 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f20a65fc-f135-31c6-9926-4d18c0a21af1 | -14.30275 | -51.54428 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2623b1c9-96c6-3a64-82e2-bba904c38a69 | -15.01948 | -48.74955 | 2025-10-13 04:25:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e09649e-71df-3f63-a2eb-51258ce6410b | -14.30879 | -51.55639 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04050ffe-d0c7-3160-8f91-f5af328dcf52 | -16.35466 | -42.38446 | 2025-10-13 04:25:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98d9f802-520e-33b9-bb2a-3b6f8ad4207f | -12.95906 | -46.99816 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 695274ea-9f8c-381c-bd28-2a063c915803 | -13.88152 | -45.48136 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 52238965-b91d-33ad-947b-89634f18c8b8 | -14.24201 | -51.48762 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa46659-ac58-31bb-adc1-3887f9aba4e0 | -14.23802 | -51.48687 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d098d9b7-2bc9-3c34-ad5a-56698bcdaa09 | -16.12194 | -53.96513 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0545c356-bf51-3724-b53a-f96127012216 | -13.85135 | -45.52098 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1224e68-6d41-3df7-b1c6-791dea234f14 | -14.31279 | -51.55715 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcfb1528-926b-33e6-a23c-c7d2681a58bd | -13.75402 | -45.65299 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad20f7d2-955f-3950-8ddc-82771dcb97f6 | -17.88362 | -45.01265 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19ef2ffe-01a7-3374-b92b-ff4a74c25b7a | -14.24599 | -51.48838 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d01c0a1-641c-3484-ae4d-934d5bee6e08 | -11.87011 | -54.67394 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d095dbe0-23f5-3817-8079-59859791c191 | -14.31233 | -51.55572 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e26fcf8-dd3e-37d0-a057-b97b6667ac50 | -13.85581 | -45.492 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b53dbeda-66ac-3002-88f0-dd8e548c916a | -14.21234 | -51.51479 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a74db667-5a83-300d-b360-8953a472509a | -16.12015 | -53.97462 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 438d3183-0411-3c38-94f4-32b99e915f23 | -14.3102 | -51.54433 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bc9490c-deb3-3eaa-98cf-1763799effea | -17.8842 | -45.00861 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6159f135-e7e0-3a2d-9f87-37c56d6ac3ea | -13.80404 | -52.79238 | 2025-10-13 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cddc8563-8095-337a-ad7a-9ebc7f796bf0 | -13.86028 | -45.48531 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README25.md)
