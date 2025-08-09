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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f8cf799-c7c8-3f96-a92c-2fab04fca18e | -11.73586 | -45.01175 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bdeeb71-6299-31c6-8c20-1cd87ce69054 | -20.58057 | -41.68445 | 2025-08-09 04:17:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f9f71249-d711-3a9d-b50c-7b90244132d2 | -22.14342 | -49.44436 | 2025-08-09 04:17:00 | NOAA-21 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 92e84c62-3522-38ca-abf6-21c1263bacf8 | -12.61147 | -48.10389 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73538484-1e59-3b0e-8fd3-255c9e63688e | -14.19543 | -42.08867 | 2025-08-09 04:17:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 171cb5d7-6e9e-3cf8-b3eb-7235209b337b | -13.61839 | -49.01006 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b3a1dc4-786c-3024-95e5-6fb387451f27 | -11.73657 | -47.50199 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5697206-4f04-37b7-8378-1312e52da1ca | -20.58451 | -41.68502 | 2025-08-09 04:17:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 179df4a6-cf0b-3eb9-9290-aef599fd74d0 | -10.45529 | -44.39716 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe177650-897e-3b55-8212-faa0bba09111 | -13.60728 | -48.98435 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47973f4c-d5ec-33ab-8f2b-3b1b79e00a93 | -13.61027 | -48.98951 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b942a67-abf1-3327-aefc-c06aa4c5156a | -13.06689 | -43.83949 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 50876372-72eb-3f49-837f-f01981f6f766 | -11.9354 | -44.54319 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f60c7325-c7c0-3282-9286-5f71a254ac7b | -18.8053 | -43.11168 | 2025-08-09 04:19:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 916c217d-e4b7-326b-8075-e76b930d2b12 | -17.5144 | -50.28391 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36a61662-f841-3696-aa49-3c0636447dd3 | -19.8071 | -46.03471 | 2025-08-09 04:19:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c15f1486-e54e-3438-b3b0-7a6236fa33f2 | -23.55841 | -51.62787 | 2025-08-09 04:19:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| a1232e22-5b9e-3dc8-834a-4bf52028fe73 | -20.21602 | -41.38641 | 2025-08-09 04:19:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aff6a625-0d82-3cc3-8a1b-9f6159494418 | -16.95963 | -51.05542 | 2025-08-09 04:19:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b57ffcc-f5dc-3c40-a7bb-8f81ff36823e | -18.61152 | -48.25593 | 2025-08-09 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3643ddfa-f9c5-3ff4-9400-3bed717f052d | -20.0419 | -44.97898 | 2025-08-09 04:19:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ba19c29-fb7c-3b6f-8384-69c43bda2089 | -17.75946 | -48.45426 | 2025-08-09 04:19:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ee58983-f63c-3578-ba89-18603c7b18ad | -18.84457 | -43.83043 | 2025-08-09 04:19:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830d6e04-69eb-38c7-80fb-a36ae573bc24 | -17.78915 | -50.12011 | 2025-08-09 04:19:00 | NOAA-21 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b67641-9311-3b0c-ae42-f7184ebb4612 | -16.96029 | -51.05174 | 2025-08-09 04:19:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac4ab721-7c4f-30f7-8279-1f370f3eae11 | -20.45227 | -41.5279 | 2025-08-09 04:19:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 020aa172-9803-3a00-9741-db0aa6d52f75 | -18.98709 | -43.74051 | 2025-08-09 04:19:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1716794a-486b-3d07-9260-fa84c124cd37 | -23.56217 | -51.62862 | 2025-08-09 04:19:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| b0e8c468-185c-3387-8e67-ff0dab62ca17 | -18.98767 | -43.73649 | 2025-08-09 04:19:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e396fd5-05f1-383a-a0f9-3b63048eb3ef | -17.52118 | -50.29026 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fcf3619-d5fa-3a57-8981-af166ab488c4 | -17.61657 | -46.70903 | 2025-08-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8bd2417-631f-3fb2-9178-9bb0d3b10449 | -16.98453 | -49.29844 | 2025-08-09 04:19:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99f50084-52da-3632-b301-50908252dac8 | -18.96517 | -45.18487 | 2025-08-09 04:19:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adaa9cc5-7c62-3927-b75c-324d243a2a0d | -17.6199 | -46.70961 | 2025-08-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58435da4-35e9-32ab-8a53-52d26a56d826 | -19.85804 | -41.43492 | 2025-08-09 04:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| b7437a6b-992b-3cd5-ba9b-120e38009972 | -20.44891 | -41.52249 | 2025-08-09 04:19:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8d612ffe-ee5f-3b54-956c-670a2c565b54 | -19.78962 | -46.03899 | 2025-08-09 04:19:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f791995-10d0-3de5-b5c0-ea7f4ca3850b | -17.51265 | -50.29375 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 731850e8-9d1d-3c30-8194-2dc550be2779 | -19.96926 | -42.11896 | 2025-08-09 04:19:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ae58e812-5430-3f8e-b58d-e87a728ff5e3 | -17.51735 | -50.28955 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9059f9fd-3a94-3fc6-95b0-3ed6fce4a8fe | -18.31038 | -48.80857 | 2025-08-09 04:19:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6ec88254-9c06-3d22-b355-757fb3bc8495 | -19.81908 | -45.01697 | 2025-08-09 04:19:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb935593-f6e5-3bca-9c5b-c8e5ac2978d0 | -19.82638 | -45.01431 | 2025-08-09 04:19:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b729c9-1d73-33a5-8ea0-a103dfe49d31 | -19.73646 | -42.07088 | 2025-08-09 04:19:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 4089b811-098d-32ff-baaa-55452a11a176 | -18.9647 | -43.25912 | 2025-08-09 04:19:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7007a88e-5549-3725-bdba-de9dc62874a1 | -17.79783 | -48.59557 | 2025-08-09 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3e4396c-287b-3449-8082-23d868b904bd | -19.59959 | -42.6884 | 2025-08-09 04:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 96b0dc82-b150-308a-8588-ebb90c07ac79 | -18.696 | -47.49786 | 2025-08-09 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97ff2492-5517-330b-b9c9-671a2f4884bc | -19.82245 | -45.01754 | 2025-08-09 04:19:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb736f5d-3b7b-3ebb-83ce-c7c50983855a | -19.59595 | -42.68756 | 2025-08-09 04:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f0bf8378-385d-37a0-9497-816a86dd0097 | -20.43039 | -41.57403 | 2025-08-09 04:19:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a0f72df-bc2b-3770-864d-5e7db7e2d2d0 | -20.24185 | -42.27423 | 2025-08-09 04:19:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 045bea55-f076-3958-8caa-6d9784a54f49 | -20.42295 | -41.69815 | 2025-08-09 04:19:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f77872d0-7e2e-35a3-a103-7f3a7327b152 | -17.75598 | -48.45359 | 2025-08-09 04:19:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81eba4d6-d1fb-3f27-9579-28c877976616 | -17.79 | -50.11528 | 2025-08-09 04:19:00 | NOAA-21 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45b744eb-f08b-3d47-9005-bbd59ee9c474 | -17.51823 | -50.28463 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5def3260-64be-3e81-922c-881d553cbf72 | -18.89772 | -43.78119 | 2025-08-09 04:19:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27a2836e-7504-3843-a89a-f3995de119ee | -19.59899 | -42.69284 | 2025-08-09 04:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 652f98c6-0391-373a-92d4-1a2eef53f4ff | -17.98916 | -43.94313 | 2025-08-09 04:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4548697a-23df-39e8-9e98-31e0773f7b3a | -19.59228 | -42.68697 | 2025-08-09 04:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 83097240-070c-35f1-9351-1dbb69da37e6 | -19.42567 | -40.73119 | 2025-08-09 04:19:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6b2445f5-1fa5-3ac1-a885-f9e7b7828794 | -20.43107 | -41.5775 | 2025-08-09 04:19:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 66889504-e848-35cf-a793-f371f5d767da | -17.50882 | -50.29303 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db8581d5-5341-385d-a1b2-e628dbc7266b | -19.2872 | -47.42567 | 2025-08-09 04:19:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33f8e38c-f870-3cc8-adc2-d5bdff1cb232 | -20.42973 | -41.57933 | 2025-08-09 04:19:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3745384f-026e-3479-93dc-419619da5c89 | -17.76014 | -48.45024 | 2025-08-09 04:19:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 232162e2-70b5-3a10-bede-bd51864276e5 | -19.5929 | -42.6824 | 2025-08-09 04:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1177aa66-b850-3073-a6b3-90091875e38d | -17.52676 | -50.28113 | 2025-08-09 04:19:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf12858a-cfd3-3268-ac0b-ed40b8b53c1e | -17.79293 | -50.12079 | 2025-08-09 04:19:00 | NOAA-21 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 467fdda5-e244-362c-8a5f-09820c27c526 | -18.55923 | -48.02275 | 2025-08-09 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fedacc99-7d78-38bc-82b4-52d75388338a | -17.98631 | -43.93866 | 2025-08-09 04:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27412c20-250b-33e8-8640-933dcdddabc8 | -16.96096 | -51.04808 | 2025-08-09 04:19:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd666dbf-792a-3612-8ae5-eb9efa36d526 | -19.8124 | -47.0634 | 2025-08-09 04:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5f974ce5-4083-301c-9a0c-5419cb724e58 | -7.0615 | -59.1779 | 2025-08-09 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f84a2d0c-f53b-33a2-bf96-f5aeaa9e1b9a | -7.0616 | -59.1586 | 2025-08-09 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 569bb169-289d-3eeb-8f66-da0279b8e9e7 | -7.08 | -59.1771 | 2025-08-09 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 259f1088-d6e6-3029-a65b-e250c614ac58 | -7.0801 | -59.1578 | 2025-08-09 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 18186b02-b861-3e5a-8c4d-b7e5a45ba507 | -6.5856 | -44.564 | 2025-08-09 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5dd5ae38-f929-39cf-8c97-b55e6664947d | -7.0615 | -59.1779 | 2025-08-09 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 8dbb4aca-71e9-385f-ba36-bab2b7e84147 | -7.0801 | -59.1578 | 2025-08-09 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| fd9c2204-40b8-329e-bd3c-76beb7b8ef61 | -19.8124 | -47.0634 | 2025-08-09 04:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| f9bff288-4d2b-3788-a8db-1a40d6f4d752 | -8.9213 | -60.7489 | 2025-08-09 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7af6f5dc-64b3-39bc-8e81-af60fd295a23 | -7.0616 | -59.1586 | 2025-08-09 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 425cade4-d59f-3236-9021-564f636f93d4 | -7.08 | -59.1771 | 2025-08-09 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| bc9ac001-8657-38ab-a042-0458905927cf | -8.9399 | -60.7481 | 2025-08-09 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f3b6e3a1-78ea-306a-9d8e-88b9a926ead2 | -19.7396 | -42.0522 | 2025-08-09 04:30:00 | GOES-19 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| b07403c7-5f2a-35bc-90cd-429875e18191 | -7.0801 | -59.1578 | 2025-08-09 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 48070bc4-9bbe-3caf-a1ed-8104f280f223 | -6.5856 | -44.564 | 2025-08-09 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| abf4c352-9de4-3e7c-9d18-c18bc7a1d32a | -8.9213 | -60.7489 | 2025-08-09 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f0dc0428-6e08-3574-a3c4-a078e6a2904b | -7.08 | -59.1771 | 2025-08-09 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 248a9db2-f218-3369-8a48-8c0000f84eb8 | -19.8124 | -47.0634 | 2025-08-09 04:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| e185056e-4c95-32ca-83b5-63de70e880a2 | -7.0616 | -59.1586 | 2025-08-09 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 26fa36b6-a2d5-393c-9bb8-f427139dfa54 | -19.813 | -47.0398 | 2025-08-09 04:40:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| e60d96b0-f271-36f4-bca5-a3fe31de9d37 | -8.9399 | -60.7481 | 2025-08-09 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| b595ad90-015a-3244-adcc-22279413d061 | -7.0615 | -59.1779 | 2025-08-09 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| dd74a624-308d-30ae-b451-4fae572c0e6a | -5.88872 | -57.74709 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82bbdb8b-58a7-3927-8101-97a02f9df532 | -7.25643 | -44.65942 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9253730b-f2ee-3d36-b798-c0568fca6c8d | -5.81806 | -42.94803 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 13b955c0-4443-38a4-a957-4bd421c871e5 | -7.25571 | -44.65775 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3632077-fd7b-37f2-9339-94002ffa125e | -3.8206 | -41.5732 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
