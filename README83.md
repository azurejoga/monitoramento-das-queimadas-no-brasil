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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b25d7d38-b55e-358d-8dcb-6144e8de6e2f | -10.97186 | -47.82355 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6795bdf4-ffbb-3c11-87bb-5f5f58fe87db | -7.2919 | -45.06932 | 2025-10-28 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1ca0c36c-6027-3961-b9fa-3adec993f279 | -8.57893 | -54.6276 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 191ce3e7-c154-35e9-b90f-c53afcdfd9c7 | -6.61084 | -44.64726 | 2025-10-28 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ad16e00-e00a-3fd7-9791-e2f974a5af08 | -13.57416 | -48.53273 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8b1bd3b-cb1e-3301-95ac-83134fe47322 | -7.81444 | -46.43309 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3432e37c-ac59-36f2-a2d0-645afb123e1d | -7.60071 | -43.59083 | 2025-10-28 05:04:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cb719d8-d5d4-3898-ab5c-3e7b376afd95 | -10.5606 | -49.77944 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a1549bcc-376c-3706-aafb-3290dcc410a9 | -7.94433 | -45.49492 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e4d5612e-7f7c-33ec-807b-8913e93b92b1 | -7.50979 | -46.28016 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 650a88b7-afe4-33db-9c63-d22e7367569c | -13.56042 | -47.16423 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6717913-5f75-3c91-9462-3f88b217de4b | -6.08914 | -53.50522 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ea5a0a-d5a7-3bb1-ae8a-51219e0485d8 | -13.63449 | -47.62025 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79034c97-f2dc-386b-9051-861308c8d0d7 | -12.07662 | -46.40002 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f5a8d88-4cb7-3dcc-9cad-17cccc676e5f | -13.55786 | -47.16169 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 523bdd64-1cd9-34ae-bd51-e6894fbc87e6 | -10.29503 | -47.18694 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c886b5a3-1c03-3e8c-97a2-b885d6bdc2f8 | -10.94825 | -50.2777 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd71c074-ccd1-3675-91e3-04f97fb8d1c4 | -10.53149 | -49.54909 | 2025-10-28 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1aa1fb4-c90b-3f80-a5b1-05b68d36f110 | -7.8095 | -46.46838 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cd07b55-a2a3-3ac6-bc71-9ee428e44ea7 | -8.11383 | -45.96045 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e73f07e-e480-3af4-8102-064d292b2225 | -9.94993 | -47.10694 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49da9b0d-ac44-36da-9d5e-6bd7823bba00 | -10.96888 | -50.25829 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0a1dafe-38e8-3750-875b-fdf3535ac99a | -13.42174 | -47.38351 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dca06e5-8539-377b-9ea1-79202e9e634f | -7.60666 | -46.47942 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5172d74-f7e4-3e29-8e78-f0c1b7ea8a73 | -7.94537 | -45.48695 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f753dd01-c6e4-3cc0-b541-9914ada155a0 | -7.98503 | -46.74231 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1b6dca4-12bf-31b2-a3e4-4592c453718a | -7.98721 | -46.74673 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc0a7504-63c1-3d32-816a-198412a62d14 | -10.29737 | -47.21169 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f1a98c-0fae-335b-b629-8a3be8dbf1fc | -8.0552 | -54.92602 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ddf9ea6-4f88-3d56-9123-c58b33ee6bd1 | -7.29843 | -45.06587 | 2025-10-28 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7dabbf1a-323e-3761-9438-4cfa33fbced7 | -12.70531 | -46.3247 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4ce7579-346d-34e0-9fc5-3530c7646c90 | -7.3515 | -47.64481 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 378217e3-c467-35fb-9256-99567072e4fd | -13.31915 | -48.34559 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf211cfd-1d3c-3bc3-8288-806ab408a567 | -7.10241 | -47.27326 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaf65927-37e5-303b-afea-26ea77b286ae | -7.93243 | -49.73788 | 2025-10-28 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d0b0aee-21f4-338b-aa4e-80021d1f8deb | -12.08727 | -45.65925 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 169d1d09-36b5-3014-b845-5220837cbd77 | -13.2606 | -47.96318 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aaf6e2b-16d5-31c4-bd55-1359f8fde9e6 | -7.98742 | -46.19433 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9aac268-b1a9-3c2b-b71c-c150fa938330 | -13.39431 | -48.51431 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5df9ac30-4e32-320a-9ae4-12714c43e02a | -7.81239 | -46.44773 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 950fb807-fb84-3f90-8581-443c2183770a | -13.24957 | -47.96469 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53761078-d137-3bf3-8b87-582e97b327cc | -10.76458 | -44.75447 | 2025-10-28 05:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d9fc02-d453-34df-a890-046b13431fb8 | -8.14636 | -47.00264 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b93b1eb2-81d9-3198-94ae-ff8b754cda71 | -9.45842 | -46.87086 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203d0277-3776-3614-806e-6989d202a0ab | -10.96702 | -47.81984 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43eacabf-d0dc-302b-883a-d3019ab38cd9 | -13.67028 | -46.52762 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6297d55e-3be8-34a9-aa75-5ae23b5dac71 | -10.86012 | -50.13192 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5e5b6d7-956e-3d98-92d9-31427be7a713 | -12.97521 | -47.93288 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28172a06-17ef-36b8-ab45-5a0561a81d03 | -7.47097 | -47.16137 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 160d10ed-86e6-32f7-98c2-9f0b50da4a68 | -7.93182 | -49.74216 | 2025-10-28 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f1841eb-2f8a-3c26-bc30-366300b89577 | -12.70344 | -46.32766 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4769c29-3d40-3a29-83e0-ac6215993c5d | -13.56078 | -47.16125 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f575d8c-aa33-316e-9938-e597913e4321 | -10.35313 | -48.04946 | 2025-10-28 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507433a8-a47d-30d8-ac93-b1f7177105dd | -8.6335 | -47.71108 | 2025-10-28 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f09c2942-bc56-3fb6-8e12-a88324aa6651 | -9.53935 | -46.94087 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd420398-1207-36c6-bde8-65a8817e778a | -11.07798 | -48.34259 | 2025-10-28 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0702c99a-8be7-3279-8516-1bff1cf99da8 | -11.79805 | -52.49934 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe11631d-aa1e-3044-907e-531ca7f36bb1 | -8.08224 | -45.96072 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05f1382f-d2f0-3490-95ac-a94c22db686e | -7.26665 | -44.9665 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6402a74-08fb-3113-b539-5c9949ee833c | -4.96811 | -56.27733 | 2025-10-28 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a0a144c-9281-3d13-8953-55605289eebf | -13.31165 | -47.69766 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f984974-0077-3e56-8eb1-f4ed1181d52f | -10.56134 | -47.89617 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2f6418b-7edd-3058-a274-b643bb7e9613 | -11.80136 | -52.4937 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5441648b-3e06-3038-b9b5-9e0979cc40db | -10.5632 | -49.79398 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb4ac0af-66be-3d60-9749-36bd1dac2e54 | -11.28821 | -45.51392 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ddd7cf99-ecfb-3fd3-b2e0-5170187a4423 | -7.86488 | -46.39666 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9c47e7f-89ab-3391-bc26-0b9c8a12e383 | -7.82203 | -46.42389 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c539626a-4b28-34fa-b550-348389eab26b | -11.07895 | -48.33492 | 2025-10-28 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fe76eb4-accf-3814-b9aa-833499407340 | -7.44936 | -49.41222 | 2025-10-28 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 94e042c2-8dd0-38b3-9d86-97e210c07d4d | -9.55666 | -46.97639 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0f1af88-28bf-33c7-8f61-fb8a98607f1a | -10.29633 | -47.17675 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d20dae3-dce4-3973-a421-b96663563043 | -10.55931 | -49.82173 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a315bdf7-07ff-3b3c-b92d-6292b39f93a5 | -13.31875 | -48.34879 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0839793-b809-3eed-aa36-4f0e6efbbc23 | -7.92745 | -49.74149 | 2025-10-28 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46ee61b4-b34c-30c9-8755-e21a692b9a75 | -9.86969 | -47.46595 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b5533c-ffbd-3513-b865-64c8621f2864 | -10.9343 | -47.61947 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64b919b8-69a0-3434-af45-59c71f537e26 | -8.25728 | -46.89682 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f82f699f-571d-34d0-94e1-ae678ce12890 | -9.04001 | -46.94519 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0844dcba-e9f2-32bd-a396-caabdeec8723 | -9.53721 | -46.96956 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d10fc0fe-d2c2-338b-9fd8-37d3cd461056 | -7.93777 | -45.50298 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4695580-e81b-39fd-8a94-bc4b6189ab68 | -8.64579 | -45.28464 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d31df178-12ea-3392-a13f-991a62a1eb7e | -10.55867 | -49.82633 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 643f63fe-9d03-3576-95aa-6bbed71e70dc | -7.80754 | -46.48237 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e9b8353-4bc0-376d-ad97-16b54e96c980 | -10.92367 | -50.26221 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e93e9be-c87a-33a2-897c-701a95fa1186 | -9.95178 | -47.10884 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13463e58-4394-38b8-a47d-8e4aa6099fd5 | -10.99106 | -50.35894 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7f638e-0ff0-35c1-b4dd-ad3a10fc56bb | -8.18597 | -44.44202 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84707c49-840c-32d7-b10c-a7b26146fd67 | -9.14056 | -51.29956 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fcec59b-863c-3b41-873d-be1cbaa651a7 | -13.67172 | -46.51483 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cec24bd8-3a4c-3260-9485-44fae952e547 | -9.13552 | -51.30604 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 96c1eb85-5db1-34c8-b56e-70d2cb946317 | -8.10925 | -55.0798 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74ecc253-a5e8-38dc-a9b7-5d4cd8649419 | -10.91102 | -50.256 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54b6872c-6d02-3c6c-9d09-a80f8eb76b57 | -8.15796 | -46.99701 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d55b1f-27a8-3848-808d-955a56532a4d | -9.53596 | -46.96615 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de53d462-e1a8-3783-a848-7d19a146e5b1 | -10.32085 | -48.79039 | 2025-10-28 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b00b215b-6415-3b44-b2b9-a4127fecf0ec | -7.80803 | -46.47881 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a3f7b39-8e10-3c09-8ee6-6ff777b9de4e | -10.94942 | -50.26896 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fd72a12-d84d-3f5b-bb95-28d8a4133962 | -13.2208 | -47.09638 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db975a83-f704-3d0a-b2c1-4ae084a83134 | -11.07863 | -48.33745 | 2025-10-28 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e5ce94e-f975-3c37-9f63-e19cb97c0fce | -7.92806 | -49.73721 | 2025-10-28 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README84.md)
