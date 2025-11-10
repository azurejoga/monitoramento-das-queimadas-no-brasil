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
| 5c20613d-795c-325e-86fe-962084ff05b6 | -9.12995 | -50.08738 | 2025-11-10 03:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f68be9e9-acdf-3c6e-9982-ef5bec4c73b1 | -8.73856 | -48.31342 | 2025-11-10 03:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c01c61f-4ea0-39ac-8074-8f70ddb5857a | -12.6898 | -49.11218 | 2025-11-10 03:59:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93bc028f-4105-3541-878a-8423e6fd8e0f | -9.65629 | -44.50513 | 2025-11-10 03:59:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acd9ed15-0813-362c-8111-58840be716e8 | -10.79743 | -44.24444 | 2025-11-10 03:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4f5eac0-1e0b-3d01-882d-3e13fa981e57 | -10.61563 | -52.17709 | 2025-11-10 03:59:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c412c276-fa95-34bb-af54-9c1ef9404df0 | -14.69289 | -46.58064 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 036d60da-d603-3935-8288-1813f14514d9 | -14.70115 | -46.60851 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 754e351d-0e33-3120-9c81-cb170cfa9237 | -9.12908 | -50.09182 | 2025-11-10 03:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60500b55-9eb2-36a1-a6a2-c7e27cce6dc0 | -11.75112 | -40.21661 | 2025-11-10 03:59:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4cb70ab-668a-37a0-a3eb-14f16d36a969 | -10.09619 | -45.65965 | 2025-11-10 03:59:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37be4031-d8c0-375b-a8df-b2e0ce787fc8 | -9.12913 | -50.08567 | 2025-11-10 03:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19bd21b3-ac43-34d7-b24c-56f9014914fb | -8.74425 | -48.3215 | 2025-11-10 03:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fc06d4d-7a66-38a0-bb27-12eb71429580 | -12.39655 | -46.58644 | 2025-11-10 03:59:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7543973a-0147-3fd0-b150-e2ab69ba862a | -11.16177 | -43.57417 | 2025-11-10 03:59:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5bc5acb7-9954-3a5e-b9ef-0171376ceb10 | -14.69907 | -46.59564 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16ad1d90-eb3e-3175-8bdb-8bd8bc00cd4b | -13.72752 | -51.4645 | 2025-11-10 03:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56ec1b92-86f4-340f-8ad2-e2adb0c4a23e | -11.22058 | -41.54699 | 2025-11-10 03:59:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e76a48b9-b275-320a-8274-12e6fef35b02 | -9.13085 | -50.0828 | 2025-11-10 03:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db500511-8832-3b41-ab38-9f293cee484e | -4.2128 | -50.6273 | 2025-11-10 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 178667cf-b87b-3356-9ae7-e98d95f63dfb | -18.47788 | -53.41092 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cd76006d-0c27-37d8-83d2-8d43f91d4d46 | -17.24021 | -45.9023 | 2025-11-10 04:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e3c53ec-ff16-39cd-a94d-675a2c3ab5fd | -18.51224 | -53.48951 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03044378-bd13-3339-bda5-22b24af1a394 | -16.52048 | -52.38344 | 2025-11-10 04:01:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 277c2344-c234-3171-8d85-3ff817f07c9f | -18.48063 | -53.40982 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 26caa898-f42b-3b31-9eaa-0943b06f42b0 | -18.47452 | -53.40796 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 84bae2a9-3a21-3de4-80e8-2f4afdd67f29 | -18.50363 | -53.49864 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eed8ec2b-854b-3a5d-8ec4-a4bb7e2982cc | -18.47917 | -53.40528 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3bccee5e-6f67-38b3-bf01-58f87bb34b3e | -18.51104 | -53.49485 | 2025-11-10 04:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15acbb2b-0268-3935-bb66-6ef7c04f8679 | -19.36838 | -48.61218 | 2025-11-10 04:01:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15a0948c-66cb-3cb4-9246-c46f5e356467 | -17.26492 | -48.04994 | 2025-11-10 04:01:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42e6eba6-6241-3d56-a7d9-74f7059d733f | -17.65606 | -50.75109 | 2025-11-10 04:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39320d0b-7e58-395a-a43a-1e3d39117e6d | -14.95594 | -46.38086 | 2025-11-10 04:01:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b5963cb-d71a-3a28-b868-448c6835525c | -17.65 | -50.75316 | 2025-11-10 04:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd87e367-77ce-3021-859d-81eac1225c32 | -17.24119 | -45.89691 | 2025-11-10 04:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03ce9277-dddb-3ba9-9ec6-c57a1354e0f2 | -17.65533 | -50.75454 | 2025-11-10 04:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f896b6c-7a60-3eb6-ada2-9bd556832c25 | -21.97133 | -49.80798 | 2025-11-10 04:04:00 | NPP-375D | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1439af72-1c24-31e7-ba44-eee768c2ec9d | -21.97024 | -49.81318 | 2025-11-10 04:04:00 | NPP-375D | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0531d1e-60c0-3efc-bb85-c3ef37110d60 | -21.96902 | -49.81176 | 2025-11-10 04:04:00 | NPP-375D | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a1873bb0-04f7-374b-a0bb-5fe77cab7b02 | -21.97008 | -49.80655 | 2025-11-10 04:04:00 | NPP-375D | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c0d9db9-688f-31cf-9695-2c91a9135f06 | -21.96668 | -49.80693 | 2025-11-10 04:04:00 | NPP-375D | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5927c13-7f93-3609-aead-34bb4dc9c4cb | -4.1943 | -50.6281 | 2025-11-10 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c80fe628-fe81-3a20-833d-e56775f0ddc5 | -4.2128 | -50.6273 | 2025-11-10 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b6116b34-e88b-34f6-94a7-ebdcfb11def6 | -2.95207 | -49.35336 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d258d76e-1fe6-3297-90f1-af73138a5132 | -2.26648 | -47.84822 | 2025-11-10 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea4cfe9e-20a8-346d-a7c2-858126c9cf33 | -2.56681 | -50.64145 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24bc0e03-2116-3773-8924-0fb5f6518c73 | -2.28542 | -46.44443 | 2025-11-10 04:18:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8a6fb35-b855-3e36-a4cc-b012536063a1 | -1.79256 | -48.07092 | 2025-11-10 04:18:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aea4a79e-0b2d-3c74-83ad-1004501d370c | -0.81455 | -47.15204 | 2025-11-10 04:18:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8986599-e24b-34dc-b546-bbf008f6fd37 | -2.6421 | -49.22 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21f4a451-445b-322a-9ee9-ccead0eb3d0f | -2.26722 | -47.84361 | 2025-11-10 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123d93f8-9fec-370c-a85d-ce7fc25f536e | 0.66107 | -51.54725 | 2025-11-10 04:18:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26b5b22c-937a-3ba7-a0ca-da36a3676e84 | -3.2972 | -45.53144 | 2025-11-10 04:18:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 017eae01-ea5a-3f23-aca3-444fd5f0f228 | -2.4372 | -49.34243 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 405a8aeb-c98c-3d5b-ae6a-13316a08ff92 | -2.93173 | -51.05183 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0591fa6a-9028-3dae-8692-4d0480392e69 | -2.84738 | -48.65209 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eeacc31b-b955-385c-8230-bc6533ef4652 | -2.29395 | -47.87171 | 2025-11-10 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 413f416a-09b0-3e2b-bb64-6e05bb818bd6 | -3.00396 | -50.5309 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b2b11e7-fe5f-3557-b99c-c46ca2746808 | -2.82674 | -48.66211 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e2a4113-7cb5-3a92-a219-3853e07012c6 | -1.76401 | -55.03276 | 2025-11-10 04:18:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fe55bdfa-a275-3882-8d62-f038374f9c2d | -2.60727 | -49.22577 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3c31ec-5d52-3dbb-951e-50a4880644fc | -2.44337 | -49.22702 | 2025-11-10 04:18:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c5b6a4-1e30-3092-b8f5-811a6633044e | -3.09637 | -49.26464 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 913e94b4-2f07-3e7a-b207-892a311265c7 | -4.07322 | -44.1325 | 2025-11-10 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 014d6aa8-dbe9-3022-8ed1-c40cb8414111 | -2.9654 | -45.07721 | 2025-11-10 04:18:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a82d8a82-99c3-3a6f-bd55-95dcdec84b42 | -3.2238 | -48.78918 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc6c503d-e272-3eb0-ab05-a774d353dca8 | -4.07652 | -44.13301 | 2025-11-10 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4c7b1bc-b19b-3a6d-acd1-b723148ca295 | -2.84901 | -48.65 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d5ed18e-df1a-3396-b854-60ec80b1fcbc | -2.79354 | -49.65681 | 2025-11-10 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b16bf7-3d0a-3301-b491-af01f8919f23 | -2.99248 | -48.05875 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6fb15e5a-0087-3cff-b62e-349689cabc0e | -2.29321 | -47.87637 | 2025-11-10 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6f7dcec-c3f6-315a-95ae-386d3e32d13f | -2.91766 | -40.00822 | 2025-11-10 04:18:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c6b2caec-2786-31bd-a174-4546abd15313 | -2.11575 | -48.18511 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb97cfb8-19c7-3eb5-b254-9a76950d80f3 | -2.84108 | -48.64872 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8c4c9b42-d967-3993-88a4-9fe3406d34d6 | -3.10918 | -50.19468 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4862c7ae-bde1-30b2-9d35-55a977d7b3b4 | -3.10412 | -50.19817 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37e241e5-e38d-3a93-beb6-d8f073838c1f | -4.06992 | -44.13198 | 2025-11-10 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db250ff6-c4d9-31e3-9b7d-5f6a336424d1 | -3.09719 | -50.3246 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0996f9eb-c821-38ce-92ca-9661278cc6f2 | -2.96765 | -44.5901 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b0a5f26-c296-32d1-a46b-e5fd1677b42b | -2.60253 | -49.22883 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 28e6e216-ab6c-34a6-8d31-4a525071966b | -2.91764 | -45.2919 | 2025-11-10 04:18:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae6d6720-a9b1-34ca-889d-2c78eb2c670b | -2.91834 | -40.00372 | 2025-11-10 04:18:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cce76221-97b5-3b61-819c-b7674231cc4d | -2.84341 | -48.65145 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 679826d3-a40a-3826-a633-12cda2e8d40a | -3.10048 | -49.26533 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26831c1e-f757-363e-9d4f-6cfb43295030 | -2.43155 | -48.04864 | 2025-11-10 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e37aedb2-69b6-3889-a53c-46a443a9a27f | -3.19781 | -46.58535 | 2025-11-10 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f03b2cf0-f4b9-3729-8d26-e32b69784b9c | -2.64991 | -49.28967 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b32460c-3910-3847-8aa6-2803dd7cc3e0 | -1.76322 | -55.03757 | 2025-11-10 04:18:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 54f2a4ef-9c8f-38a8-830b-91f864f7f6a7 | -2.32237 | -48.59349 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 551b8d0d-2c62-3ac8-905a-6dd0aa6f268d | -2.60314 | -49.2251 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16409b53-53bf-328c-b5db-1b07de53e5e5 | -4.52413 | -40.36058 | 2025-11-10 04:18:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2030e193-097e-3982-8cdb-d0b510dae797 | -2.98092 | -44.59218 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db00fb55-12b7-33ae-a63b-777355a29dcf | -2.70666 | -47.39647 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1472ffa-bd31-3a3c-b9e0-99f91cbd6b57 | -2.18997 | -48.24842 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f99aa00d-7e6c-30d4-890a-71c52b02715f | -3.98377 | -42.13144 | 2025-11-10 04:18:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4dc16339-ba4f-3dbe-8ac9-a4cf975614c7 | -2.41506 | -49.34666 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc7e7f8-595b-31ba-b269-2cbf200f263e | -2.97035 | -49.82333 | 2025-11-10 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a564ea42-df01-33f3-a4cd-31ce869415ed | -2.93638 | -51.05263 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c55403f2-1cf0-3a55-9bfb-239f21fbb6a8 | -4.07706 | -44.12957 | 2025-11-10 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b81f88b4-d324-34ce-aa91-12f085f1e563 | -2.76701 | -48.35731 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
