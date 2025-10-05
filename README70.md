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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ef40dd1-8ac5-3276-98e8-9e68ba775ac7 | -19.42811 | -44.18084 | 2025-10-05 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ea8c038-2595-3b86-bd6f-b59535ea9e9f | -23.0214 | -46.2498 | 2025-10-05 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a36ad115-01c4-3474-be9d-b7486219362f | -23.20653 | -46.02703 | 2025-10-05 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 39812222-360f-3fce-bfa0-bf58b23cf13f | -21.16694 | -44.27001 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5876392a-4142-3f37-bfbd-fd7537ed31b1 | -22.12773 | -44.84649 | 2025-10-05 03:57:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12d22997-0a52-3602-b760-f8c7ab57d2d6 | -21.82642 | -47.39783 | 2025-10-05 03:57:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f0f7469-b4c7-3fdc-b429-dabe4cb01e95 | -21.00953 | -43.97933 | 2025-10-05 03:57:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b70f95e4-a463-3b17-baa2-0a51248d37bc | -22.48063 | -47.05197 | 2025-10-05 03:57:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5429509-4dc7-377c-b317-b9383fa62881 | -20.11982 | -44.39989 | 2025-10-05 03:57:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c2bc1a9-1127-335f-b81e-4d4ce478988d | -22.48517 | -46.81552 | 2025-10-05 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77278bab-f81c-35e8-aa09-7138f7fd30af | -20.32674 | -47.73723 | 2025-10-05 03:57:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccf3ed29-8614-3ff1-baef-5c6d7f9c74c1 | -19.9471 | -44.63551 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1feed72-6cda-37c4-bbd8-4ff0424ecaad | -17.99222 | -51.63446 | 2025-10-05 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 024fdbfa-fbe8-3365-b892-025fe70f4c30 | -22.16782 | -46.73974 | 2025-10-05 03:57:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e41f3a18-0ade-3ce5-bbaf-499a4972b383 | -22.20243 | -42.984 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c7e4e4b5-4275-3ddd-8cc5-b2f698a7e2e6 | -20.73019 | -49.61712 | 2025-10-05 03:57:00 | NOAA-20 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c31892b5-7fb9-397c-a0c1-a53c828aa6e9 | -19.01381 | -50.60656 | 2025-10-05 03:57:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 20c68f7d-795d-357d-9dec-fe08e37d1712 | -19.59068 | -44.62661 | 2025-10-05 03:57:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22422821-3372-30d6-8b28-8fed5a6f751e | -19.51598 | -43.83786 | 2025-10-05 03:57:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee6bf78a-656f-3db3-8168-0357931023b0 | -19.50441 | -50.37553 | 2025-10-05 03:57:00 | NOAA-20 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2df763af-75a9-3796-9efe-ebc558bd130f | -22.64846 | -42.81355 | 2025-10-05 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b9f2b8dd-a697-32b0-b9c5-145ea81fee64 | -19.58554 | -44.63473 | 2025-10-05 03:57:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f9e8904-dafa-3642-b078-c0ee8c3502f7 | -19.98798 | -44.13501 | 2025-10-05 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae2b9935-4fa5-30bb-8c85-37b208697312 | -21.29946 | -42.97969 | 2025-10-05 03:57:00 | NOAA-20 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd4c53a8-e463-339e-99be-d2ad4c034674 | -23.01767 | -46.24905 | 2025-10-05 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4915eaeb-469f-314b-baba-f8616187c801 | -17.97622 | -51.14268 | 2025-10-05 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd763f76-844f-3bd2-8220-50905374cbff | -17.97462 | -51.15029 | 2025-10-05 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8391bb0-cc61-37e9-aefe-19024ca4f4eb | -23.18946 | -45.62348 | 2025-10-05 03:57:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0144b464-e249-34cf-94c8-d85df959d4b7 | -19.71269 | -42.05509 | 2025-10-05 03:57:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 126da9b2-7044-3084-b847-5d3b149cc999 | -21.93198 | -46.59285 | 2025-10-05 03:57:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f3320784-656f-35ca-b05b-b81145457e0d | -17.97543 | -51.14643 | 2025-10-05 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd02b049-dca7-36da-97fa-53a477f1503b | -18.1868 | -53.3623 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68b0cef2-231c-375b-880e-2be3bd8996a9 | -23.01988 | -46.25329 | 2025-10-05 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 857692df-2549-3899-b760-7976de989713 | -18.2479 | -53.35331 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd217146-7324-3ea8-95e2-53f9ea887b4b | -20.73583 | -44.32651 | 2025-10-05 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93479306-da18-38e4-bf7e-1240255d9977 | -20.51777 | -47.53782 | 2025-10-05 03:57:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63615d08-e892-3eb9-9596-e0b20d6f7779 | -18.24661 | -53.35901 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a53ad584-d763-349e-a579-d941e5b6d465 | -21.58858 | -45.27837 | 2025-10-05 03:57:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe92dd1c-7aeb-3112-8f98-356066efd80a | -22.64908 | -42.80978 | 2025-10-05 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a1e2045b-6d1b-3b68-95d1-469fe6933bca | -19.42884 | -44.17661 | 2025-10-05 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53a7e9ff-36e4-3e9e-aa47-0c01530f73a0 | -20.12339 | -44.40042 | 2025-10-05 03:57:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e07d0aa8-5cb9-3731-aa16-e6ec26a39acc | -22.99172 | -50.36955 | 2025-10-05 03:57:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c603e174-b16c-3473-a160-e9249c7618a4 | -21.82567 | -47.40182 | 2025-10-05 03:57:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5b306ef-8b11-37d5-b6f1-0b837f8245da | -22.36624 | -47.03667 | 2025-10-05 03:57:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e63452-1a32-36b5-93ed-945d29e371be | -19.9463 | -44.63999 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9950297c-e80e-3668-a17e-9b3d1412baab | -20.51155 | -43.92531 | 2025-10-05 03:57:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 27f36785-4f4d-303e-b0c5-224c74fabe11 | -22.98965 | -45.62509 | 2025-10-05 03:57:00 | NOAA-20 | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c95128b9-4e5f-3b05-8a80-ac8fcb391592 | -18.20151 | -53.38424 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e131f1e3-28d6-3999-8de4-47f783f25b78 | -20.88313 | -45.76959 | 2025-10-05 03:57:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bd4b756-f9a1-37a2-abb8-c32d74ab9c33 | -19.84689 | -46.52362 | 2025-10-05 03:57:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30cbc2b6-367c-3a92-8088-4e90054b3e22 | -19.7121 | -42.05877 | 2025-10-05 03:57:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf0a0e7e-7f82-3ddc-b1d3-f3fc1a1cae7f | -23.18867 | -45.62786 | 2025-10-05 03:57:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| df9cd81f-5088-3200-be01-154a71d1643a | -20.79981 | -51.65698 | 2025-10-05 03:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a920e8e-21ca-3b58-b50d-0abfe7b94853 | -17.99145 | -51.63807 | 2025-10-05 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e2b924e-ccfe-3d1b-9269-e15fa74e41dd | -20.2701 | -45.47706 | 2025-10-05 03:57:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 88e6fbe6-4119-3d95-9131-2afe8589dc2b | -19.58992 | -44.63095 | 2025-10-05 03:57:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10023274-5721-3386-87e4-81cd155bea59 | -23.02076 | -46.24842 | 2025-10-05 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0fa42aa4-a6d4-32ae-a421-04bf06498900 | -17.9683 | -51.15294 | 2025-10-05 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3eb08dad-d52f-3864-9212-d5fc150c76e2 | -22.37298 | -50.02507 | 2025-10-05 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7405f8e6-c478-3083-a0f7-13f24cc89c6b | -18.19019 | -53.36069 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9f0986e-21d4-33e6-9b20-4d1920f6b30b | -22.64514 | -42.81292 | 2025-10-05 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 207a6fd1-3c48-3104-8315-f7e19f40ea34 | -21.68858 | -48.43062 | 2025-10-05 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 842b4995-3b67-3937-b4be-dc73eed475b5 | -20.77327 | -49.38728 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41c27453-fc15-3906-b38c-f519dd484565 | -23.18666 | -45.61832 | 2025-10-05 03:57:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1201788c-bb6e-3b6d-95bf-17a845105f4d | -18.14682 | -53.34908 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb9e8b93-81d0-300e-a668-7f2c328d5cf7 | -18.5615 | -46.50941 | 2025-10-05 03:57:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a1c8a7f-735c-376f-9af4-afbc8c36daac | -20.73512 | -44.33068 | 2025-10-05 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae308bd0-2759-3955-ad2f-15807202a056 | -20.42489 | -42.62593 | 2025-10-05 03:57:00 | NOAA-20 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a213e040-8855-3bbb-999f-e03207270048 | -21.79988 | -48.12821 | 2025-10-05 03:57:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b73a4bd-b354-3200-aa94-3d666456db28 | -22.16664 | -46.74274 | 2025-10-05 03:57:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08bd32bb-7085-3e6b-8a31-2af78189d24e | -23.43825 | -45.47373 | 2025-10-05 03:57:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ce887a9c-5e35-3245-919d-1d9f87d18e7d | -19.9455 | -44.64449 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f146cf31-feeb-3c0a-b627-80046f09b964 | -19.94987 | -44.64082 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3f80971-0362-35e9-8578-0fe136e5a0bd | -21.82632 | -47.39746 | 2025-10-05 03:57:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 840d5f89-4acf-3aeb-b0ff-df2837ee641e | -22.69818 | -44.45502 | 2025-10-05 03:57:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 57899f0c-a4f3-3e14-acf2-e0d891dabc9b | -18.14068 | -53.34718 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b13481dc-9b9d-3950-be3d-50e28d4da05d | -20.42171 | -47.81029 | 2025-10-05 03:57:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3db55a15-6faf-3fde-9f6f-3a54f77e9daa | -18.16663 | -53.36425 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5b48c6d9-00bd-3b9e-b9ad-5e0546435ad6 | -21.16623 | -44.27414 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f41af81-861f-3d7f-a2aa-ee3e06e9eda7 | -22.94163 | -45.40806 | 2025-10-05 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f36bf1e0-be77-3257-bd47-33ec1ae90eca | -20.87938 | -45.76882 | 2025-10-05 03:57:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee62b5d2-94f5-3ced-9608-6dfa696c86cc | -21.97842 | -46.42816 | 2025-10-05 03:57:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e704cffd-590b-3729-988d-3fc9fe889b86 | -19.9689 | -44.16148 | 2025-10-05 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f26f000f-fffb-3a05-aac1-c631599b47f8 | -19.94362 | -44.39146 | 2025-10-05 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd4efad7-25ff-3b2b-a377-73f1daabfb19 | -21.68246 | -50.0751 | 2025-10-05 03:57:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b037144-81df-32b5-9e14-6bded078951f | -6.1351 | -44.6461 | 2025-10-05 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 596bfb5a-75d2-3d86-b9b5-f565dbb6223e | -21.6943 | -48.4176 | 2025-10-05 04:00:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 903f3ad7-b83d-3015-93dc-85e437b89151 | -15.6015 | -52.5102 | 2025-10-05 04:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| dcb54d96-d802-3eaf-ae5c-b1a467486646 | -21.6936 | -48.4411 | 2025-10-05 04:00:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 66.8 |
| cf6dd61e-b735-32fa-9edd-1ddd0506cd1b | -12.4669 | -45.5155 | 2025-10-05 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| e6eaef9b-07ea-39e9-8180-9af140412d9e | -4.6505 | -43.1805 | 2025-10-05 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e988ea75-9326-3a19-85a9-288809ad6892 | -18.3338 | -45.8971 | 2025-10-05 04:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4c8956c8-8703-3225-a171-20a9774f4b52 | -4.3197 | -48.0908 | 2025-10-05 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| f8a0d7e2-d860-3004-9dae-b277882a85e2 | -11.4874 | -46.7922 | 2025-10-05 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 62289482-f211-331f-a604-d08a5ba045b9 | -5.8891 | -42.9048 | 2025-10-05 04:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 71cc9cc7-7802-36cc-ae38-78ab78e20335 | -8.5764 | -46.3041 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 06a32dbc-0c44-37ea-a4b9-074e413742c2 | -8.5759 | -46.349 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 08fbb003-02b8-3d1b-83cb-8f6ee6e624ca | -10.6378 | -46.3396 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 4d8a788c-55fb-3d37-8c2a-bf43237caf6b | -4.6318 | -43.1816 | 2025-10-05 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 64922feb-f85d-3174-891b-8c770e3efd4e | -8.595 | -46.3246 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |


[Clique aqui para ver as próximas entradas](README71.md)
