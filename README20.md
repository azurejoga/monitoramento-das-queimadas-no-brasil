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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d25b2644-4052-3905-b5bf-83388683c56a | -12.70325 | -46.36421 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b38fee-ec1d-39f7-998b-4a16fb63b80f | -14.30523 | -51.99523 | 2025-08-11 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eac8935f-ff5f-3bb7-a13d-7f31b788c903 | -15.42536 | -53.92935 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 94319fd3-fcb5-310f-8353-bc3bcaddb694 | -16.70856 | -49.07584 | 2025-08-11 04:27:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33b298c7-f188-319d-b4d9-dd3f1f8c75fe | -15.43762 | -53.93171 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e47017e-9e0c-3e2f-9822-2a6aef100fe1 | -13.62391 | -46.93647 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49abe1f2-7ea1-3165-a6fa-d9653834c0f6 | -15.57244 | -42.69037 | 2025-08-11 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dde1469a-ffe1-31b1-af67-f4ef40f467ef | -18.79703 | -43.87661 | 2025-08-11 04:27:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66555fa5-b780-3ca8-b755-84136984884d | -12.54865 | -47.06717 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| befd3774-ee9f-3a05-80d5-ad288460b754 | -12.24396 | -45.05411 | 2025-08-11 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e532af2-8e15-314c-8424-54ccb79bddc3 | -13.59272 | -46.93871 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67e54d89-7cc2-317b-b6ba-643274f0456a | -11.75405 | -51.61998 | 2025-08-11 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e58419d-2b41-338b-bd81-4d37e6eb5374 | -14.47743 | -47.07799 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ac6545-8177-3aea-b9ed-ec9c0e3c2a39 | -11.76371 | -49.11918 | 2025-08-11 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b8e4a0f-491a-34c8-bb6d-41b078f59a40 | -18.79252 | -43.87947 | 2025-08-11 04:27:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81c192c0-a272-3117-8157-d0096c4e66b7 | -12.5799 | -41.27762 | 2025-08-11 04:27:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62bf6f4f-9eaa-3b1b-9d69-d5353c1a1456 | -14.30258 | -51.96663 | 2025-08-11 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0971dde-d9fd-3542-ac6b-93b3eaf7154f | -11.75485 | -51.61535 | 2025-08-11 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23409e8-3987-3a68-8c6f-67caaa5943ae | -11.11312 | -50.46894 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 494003a9-517d-39ef-b1b7-97b655a017b8 | -15.41923 | -53.91648 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6adc573-ed64-3139-94f4-efbaa10dd2d8 | -12.60755 | -47.14553 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8a6dc35-5506-39c7-a2e4-6cf24ca032f2 | -17.56924 | -47.50563 | 2025-08-11 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33230c64-3efe-329a-970e-c8fe99341766 | -12.57605 | -41.27261 | 2025-08-11 04:27:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4661f240-f659-3659-902a-a65a1c103803 | -15.40767 | -53.91036 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bff1cb-2548-3996-9434-b25ace258b18 | -18.03509 | -44.45972 | 2025-08-11 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35f11a97-df9a-3222-854f-9bb301720436 | -19.2146 | -46.8043 | 2025-08-11 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce1a448d-63e4-3f4b-982a-15fb9476b8f4 | -17.22892 | -46.95114 | 2025-08-11 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77812da2-d6db-3282-85d9-086b544710b0 | -16.30742 | -52.92632 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642f83a5-d580-3e07-a5dd-73b5bfc3de38 | -15.45643 | -53.93912 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ea06385-216c-372a-96a3-4c7caec7fbb2 | -12.547 | -47.07781 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd713d0-3ae4-361b-9a33-a679630c78d3 | -18.6825 | -51.20029 | 2025-08-11 04:29:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caba5c44-9227-33f5-b7a1-8ab472e0ef64 | -21.78044 | -44.68232 | 2025-08-11 04:29:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8063b8f3-461e-3f5d-ad31-0286f7081500 | -19.8184 | -47.97772 | 2025-08-11 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04e3f9f6-071f-35c1-8a7a-5e8a7b16428e | -22.7021 | -47.36016 | 2025-08-11 04:29:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f8d3676-5e4c-30f5-a637-c335968ede38 | -24.58798 | -52.82226 | 2025-08-11 04:29:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8aec5d55-3206-3cdf-aa13-55545626e3a4 | -19.27267 | -49.78424 | 2025-08-11 04:29:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5783d9e-c184-36c6-b815-32abd831a914 | -20.15872 | -47.29501 | 2025-08-11 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8e1a917-849c-3e5d-932b-03e72f9e75c6 | -19.25493 | -49.78861 | 2025-08-11 04:29:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22244fad-1609-3fc5-8db6-045ef176aa49 | -19.2828 | -49.76346 | 2025-08-11 04:29:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a899ed96-4e5f-34d1-b674-5ef9be64be84 | -24.2038 | -50.94434 | 2025-08-11 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d6a2abf-1f09-3a7d-abb7-fc993d082b2d | -22.28698 | -46.59396 | 2025-08-11 04:29:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 397fdf52-7fe2-3217-a17c-8c2a62d08b53 | -20.64711 | -48.69659 | 2025-08-11 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1595a3b-687d-3689-9e47-bc9fea1551fe | -24.58508 | -52.82257 | 2025-08-11 04:29:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e3d7bc1-998c-31fe-8c08-ac4ed8f326c1 | -19.90082 | -43.87988 | 2025-08-11 04:29:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 58eb5272-e631-388c-875a-81ecc71abc2e | -22.51334 | -46.79262 | 2025-08-11 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c81e8f6c-75e1-3394-8b3f-9735acacec33 | -20.95794 | -46.94681 | 2025-08-11 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ec2d350-ef03-3c54-badf-bbd09104b696 | -19.5568 | -46.58309 | 2025-08-11 04:29:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54bed012-7a0e-36c4-bed2-d8966b11cb5d | -20.59805 | -51.61103 | 2025-08-11 04:29:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e099a179-eea4-37c1-b1a8-6f11d3e2a81c | -19.67212 | -44.87833 | 2025-08-11 04:29:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 11eebcd9-13c9-3fef-ae02-39806d3fd5ca | -19.676 | -44.87883 | 2025-08-11 04:29:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ba125cee-2c54-3b63-bdfa-694610486bfb | -19.9007 | -48.20089 | 2025-08-11 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 697902fd-da21-37c1-8ee4-e48c42aa2d06 | -21.8519 | -41.32651 | 2025-08-11 04:29:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b430c7d-bf46-3a3e-a4b4-ae59e9234b4f | -19.72507 | -48.97979 | 2025-08-11 04:29:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 481e3060-d0e3-3ab7-826a-65c59f55a1ec | -21.47319 | -44.69372 | 2025-08-11 04:29:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8bccd0ad-6a48-3534-bd05-3a2d713cb9ae | -22.28674 | -46.59672 | 2025-08-11 04:29:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 741d2c43-b2ee-3ebd-b072-c80c3595b4f1 | -22.06347 | -46.81685 | 2025-08-11 04:29:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8988e1ce-6f4c-372c-b554-292b84d2ec8d | -19.55973 | -46.58788 | 2025-08-11 04:29:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5324c79f-eb20-37cc-9fe3-1966c5e91871 | -21.08978 | -43.41805 | 2025-08-11 04:29:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 555ef77c-f831-36bf-bae5-59cfb0c19ee3 | -20.47827 | -53.67686 | 2025-08-11 04:29:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c9af1f-8b8c-3ae1-a747-4ec6a579a0fd | -20.60257 | -48.87663 | 2025-08-11 04:29:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 70cae2ba-2bd2-398e-871b-942447977a74 | -20.64433 | -48.6923 | 2025-08-11 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b472b02-c95d-3b75-be41-78d89f0f0d5e | -22.71002 | -47.27815 | 2025-08-11 04:29:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 933b6f6f-989b-39ab-9fd1-b10af9d37506 | -19.28222 | -49.76711 | 2025-08-11 04:29:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a90ac9fd-ef32-33af-996a-de56862d7c87 | -19.28047 | -49.77809 | 2025-08-11 04:29:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb8c3c3-5db8-314b-b97f-f5d7b13626ef | -19.73005 | -47.88964 | 2025-08-11 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58fe4140-3a09-3bd3-a9d0-b102a8fef140 | -21.28719 | -46.71053 | 2025-08-11 04:29:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cb0d1ce-fa53-3f63-b794-1bd9e6d08838 | -21.77961 | -44.68291 | 2025-08-11 04:29:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2d22a22e-9fbe-36fa-b693-fa53bf51c114 | -24.73797 | -50.91806 | 2025-08-11 04:29:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2b7c5a45-5d9e-318d-82df-021a336a1922 | -21.14818 | -42.91048 | 2025-08-11 04:29:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bc821718-2503-320f-8787-f885ee82abce | -19.81897 | -47.9739 | 2025-08-11 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3ad8430-7d65-365b-9494-417f5c52ce9b | -21.6342 | -49.8412 | 2025-08-11 04:29:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0aadc11-ed98-3fa6-9d08-0e30b274a9dc | -20.86484 | -46.63887 | 2025-08-11 04:29:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 4bcc320d-203b-3f47-a4f2-da8e48a0a496 | -22.06707 | -46.8174 | 2025-08-11 04:29:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e21d0fdd-4453-3f5b-a0d6-d640dd05f14c | -22.87146 | -46.61989 | 2025-08-11 04:29:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 82328b31-1510-3634-a7f2-5111e731c48e | -21.14872 | -42.90576 | 2025-08-11 04:29:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 50de3c7d-5ff7-3d50-8aa8-ed26c901e64c | -19.26921 | -52.08021 | 2025-08-11 04:29:00 | NOAA-20 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b36c331c-b49b-39bc-a9e7-7413351c3f59 | -15.4407 | -53.9258 | 2025-08-11 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 242.9 |
| e9b34293-d32d-3d73-82b6-1396e7e87495 | -15.441 | -53.9048 | 2025-08-11 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| b048f6a0-c216-3d71-bf91-9cef05dfd481 | -15.4018 | -53.9308 | 2025-08-11 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| b79a4032-4695-3963-b9b0-2ec38231b105 | -6.5856 | -44.564 | 2025-08-11 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2677dfde-841f-3910-bec8-a5fb54eadddf | -15.4216 | -53.9073 | 2025-08-11 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 247.1 |
| bfbefbe9-b88f-3cef-9e2b-d1ec3469df0b | -7.0799 | -59.1964 | 2025-08-11 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 95dcd2da-f50f-3175-bc63-53aeddcffb3f | -9.3806 | -61.5315 | 2025-08-11 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f5ef1d1e-374f-3245-9add-e16eb3fe1084 | -5.4824 | -44.3969 | 2025-08-11 04:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| a3c24b23-0345-3f8b-b0fe-a62c3e97e1eb | -15.4212 | -53.9283 | 2025-08-11 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 287.0 |
| bdbf7787-4c59-3234-bf1a-5048e64c2dcb | -7.0614 | -59.1972 | 2025-08-11 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 63883431-577e-3780-a622-f806aeff76ec | -24.87122 | -52.06345 | 2025-08-11 04:32:00 | NOAA-20 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 373b6dc6-5682-33c6-8b39-7bb3af2eae58 | -27.30615 | -48.68544 | 2025-08-11 04:32:00 | NOAA-20 | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1050709-675b-389b-8b0f-4053c47586cd | -15.4212 | -53.9283 | 2025-08-11 04:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 4389215b-1de6-3769-bb83-c62997e4ff92 | -9.3806 | -61.5315 | 2025-08-11 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e6535eed-0e1a-30dc-983a-d01996829ec8 | -15.4216 | -53.9073 | 2025-08-11 04:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 196.7 |
| e9e098e8-59cb-3813-8a11-e4ca016a145c | -15.4407 | -53.9258 | 2025-08-11 04:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 07b3036d-534e-3711-be5b-77773369d2eb | -15.441 | -53.9048 | 2025-08-11 04:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 9422af64-877e-3f99-8506-a496d08e6ccd | -7.0799 | -59.1964 | 2025-08-11 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1acb8192-c625-37d0-b589-5c598e8b4d62 | -6.5668 | -44.5655 | 2025-08-11 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f6878f59-5285-3304-a9b6-1e29b30ee546 | -7.0614 | -59.1972 | 2025-08-11 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| dc0016aa-af40-3937-8eec-82b5e8321303 | -8.5604 | -54.6973 | 2025-08-11 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| aefd0ab3-06e0-3471-a8e6-244e17c9ce75 | -5.4824 | -44.3969 | 2025-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a09f6492-8e36-3fd8-beec-b5d795e00716 | -6.5856 | -44.564 | 2025-08-11 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9e764735-60d4-3e31-b7ec-8187a602754b | -15.4212 | -53.9283 | 2025-08-11 04:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |


[Clique aqui para ver as próximas entradas](README21.md)
