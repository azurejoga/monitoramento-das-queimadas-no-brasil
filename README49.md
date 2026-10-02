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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb0e6d30-29c0-3eb0-adf0-69fcc34e54bc | -11.70255 | -43.59483 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18cadb93-e5bb-3e3a-a827-8f1f44f01575 | -10.24684 | -44.56715 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9683cfd-3bcc-326a-85f7-4b273167974d | -10.6144 | -48.05227 | 2026-10-02 04:17:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a51f73a1-c852-3e43-8627-22d4e5f3c13a | -13.14009 | -40.87411 | 2026-10-02 04:17:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7749486f-5a5b-33a0-9709-f2ee4de1f676 | -9.33966 | -50.99619 | 2026-10-02 04:17:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c217f9ed-2f9b-300c-b21d-2eff411d3f4a | -12.52106 | -43.1071 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| df609d85-13c4-3aba-9f9a-471c41a9e8e5 | -15.24252 | -46.16075 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a97865b2-ef2e-33a9-8cd4-22b4abd77a2f | -10.42379 | -48.11857 | 2026-10-02 04:17:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2bfc191-72e7-3e8d-831a-bbad3688f035 | -11.79714 | -43.57731 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7f30105-be36-3590-91b3-743b690a971d | -13.34756 | -43.86689 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56f8e839-859b-38ce-8fe0-7d7a8455d2f8 | -11.69074 | -43.49855 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35aab0d5-01c7-3281-8950-2dffeae0be6e | -13.34264 | -43.8551 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f275f89-aab7-3666-93b2-406e134cd63e | -12.28849 | -42.46931 | 2026-10-02 04:17:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b040477-e810-3a8e-931f-1e9c80d1b97a | -12.17192 | -44.66112 | 2026-10-02 04:17:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caf92750-421e-3158-9b01-29ad412c38c0 | -11.46248 | -43.41727 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e8d7f32-4e56-3ee6-a81f-faaaea33e08f | -11.76506 | -43.56487 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68c955d-4e34-304c-a50d-0b8ef5cd4bf3 | -11.59848 | -43.54509 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89024a24-d5d3-3d9c-afee-a1a4d6abac84 | -11.6769 | -43.49989 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5844c56-a249-37ea-8657-ff9845655ef7 | -17.44235 | -41.91736 | 2026-10-02 04:17:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a0be8666-25a4-3a80-9d2c-232f74cb607f | -11.43128 | -43.40139 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd55d6d9-774a-3114-a5f1-259f4bfabf59 | -11.42797 | -43.40084 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69ec59b4-c49d-3f1c-b6c4-e79782ed298e | -11.31214 | -43.57022 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb79bde-b819-3e89-b6d3-03170cc0499c | -11.73584 | -43.57856 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fc00c554-1f40-35f8-9207-15f11fb64fde | -11.78944 | -43.5616 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| acb2c014-05b7-3dc8-a50c-5cd7dda8d941 | -11.13774 | -44.58987 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de4c4b24-58f0-369a-ada8-0c93f000e35f | -10.9015 | -43.84272 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c50de986-84d0-328c-9e97-ee20a6477a12 | -10.25026 | -44.56775 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6d3de1-c910-3c00-bc6a-3ff4c6c40100 | -11.67358 | -43.49934 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d65641a-e0dd-399d-942c-8b67028ef357 | -11.23038 | -45.17968 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6185e43-429f-3db3-8b6c-18dcb03416ed | -8.5406 | -54.56397 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 001e02e7-6b8b-3817-85e9-7aec6cb1db1c | -16.86083 | -40.57297 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebeb9e56-9d74-38c8-92fe-e88ed5cfe017 | -11.77001 | -43.57648 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30b9232c-29d2-3ea2-8511-7fd3493deca2 | -11.73641 | -43.57503 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 516b079a-a1db-39a7-80ac-9c93e6d54570 | -10.25813 | -49.66396 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63c75899-6310-3427-8fd3-9bfac4ccba10 | -11.65823 | -43.59478 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5a789df0-4780-3f01-a0a0-0206318da25b | -11.51309 | -43.50528 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2400fd5-33a1-35b1-b421-204b0155229a | -11.6643 | -43.59941 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f0751f3-f347-39c2-9850-84f0e862057b | -12.52441 | -43.08597 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92f6809e-d84d-37d0-9a4f-26a86b8bcd79 | -11.66098 | -43.59886 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fac9c897-9480-3c28-b637-c36b28b2c933 | -13.02899 | -41.03722 | 2026-10-02 04:17:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aebdff91-db3b-3244-a601-ef9178f93c7d | -11.23604 | -45.18869 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba65b5d-0430-3309-81f1-bba0689d318c | -11.73077 | -43.43996 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb529a5d-6a2c-310d-b63b-a1ea756d3974 | -11.76402 | -43.55018 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59ffc49f-45e5-38a7-ab64-a012e84a991a | -11.74015 | -43.44514 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e60c36-19cf-3d44-ac08-e46619420ef5 | -12.85722 | -43.81109 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82f879de-0c1d-3724-b543-a0236e5c1f25 | -11.68035 | -43.60567 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea309cfa-01a4-3155-a499-244dbddbb070 | -11.77333 | -43.57701 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be989093-a7dd-3f9c-b65b-9b68d0f47d43 | -10.29575 | -44.65314 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9774c77f-ff47-32ac-a8f6-a5316005e059 | -14.24047 | -44.23294 | 2026-10-02 04:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2078b83-81cb-3d68-8976-3ef420c0601b | -12.32481 | -46.3758 | 2026-10-02 04:17:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2bca1e3-f905-36db-803a-cb6d2ce3db54 | -16.86126 | -40.57505 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c6fb06e8-4de0-3c0f-9b42-cb913bdbde67 | -11.47017 | -43.43301 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b337cb3-58aa-352a-857c-5e81dc8457b8 | -14.3797 | -44.73062 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab3c3b2f-17fd-3e43-8199-0a2f35f28368 | -13.88341 | -44.46018 | 2026-10-02 04:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b99216-d5dc-3fdf-a0f5-de620614b7c8 | -11.4147 | -43.39865 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d74f0a18-3434-3ab7-801c-596720a1e5b9 | -12.53103 | -43.08705 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08c959d1-9b5f-33d1-83ad-d608fc605fa7 | -11.65319 | -43.60485 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7bc071a6-794a-3a81-8bbe-2a71838fd450 | -12.56142 | -43.06674 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e74ef47a-c500-3167-8452-dceece33225d | -11.65433 | -43.59777 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 400c64e5-b23e-32ac-8122-a839661cbff4 | -11.43711 | -43.53261 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19b9e206-4e58-3bf8-b1d8-216a3ade3d1f | -11.90634 | -46.5617 | 2026-10-02 04:17:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 318d175f-a7c9-313a-b4c7-95de187bbde0 | -13.25108 | -42.6317 | 2026-10-02 04:17:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f895851e-226b-35e2-918d-5707698fe160 | -11.1217 | -44.60246 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17226fb5-fa18-395e-a961-ed4fdb6b448d | -11.38865 | -43.41246 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8f2fda2-ddf9-32f2-907a-00c6319274d0 | -15.76735 | -43.6456 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d43d347-1f79-3b84-96b5-cd78204d89f2 | -15.7701 | -43.64973 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a803609d-3167-39d8-84fb-0e2fb327b5e3 | -12.98664 | -51.28729 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 742ea652-3d07-3725-9f3e-4f44520a49fe | -16.90215 | -42.09994 | 2026-10-02 04:17:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 19708a0f-1e65-3c9a-ad94-ee91fe42f587 | -9.78852 | -53.829 | 2026-10-02 04:17:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 955424a0-fbb8-31d4-9d09-6fa63deed329 | -11.1273 | -44.61108 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed595de9-b232-3482-8e66-770f74e0df1e | -11.68813 | -43.59971 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3c02918-2961-3a98-9764-f9a041bd3146 | -18.33835 | -40.05972 | 2026-10-02 04:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0cfc4afb-4d20-3cb3-bd6e-f8033ccfb55a | -13.33817 | -43.86166 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 502a2de0-594d-3dcf-9d20-59af3e529f30 | -12.51332 | -43.11306 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6f8e997-e8ab-3d3c-a0a2-29712adb2b1c | -11.68734 | -43.51974 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38079aa3-9f34-3a65-95f8-3c0ace66e471 | -11.40206 | -43.37125 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8ba1a19-cdc5-332c-811d-351ee2df200a | -10.61368 | -48.05639 | 2026-10-02 04:17:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f91b36de-c26e-33d0-9566-14bea895c8f7 | -11.7828 | -43.56053 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d5a2e4-9a0c-3bcf-8433-cdaa66a157f8 | -11.72667 | -43.50812 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d18aa188-464d-3b8b-9472-4cefb22f3672 | -11.68109 | -43.55862 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ce9f1bb5-0c05-3ec9-8bab-e82635b755a2 | -11.45585 | -43.41617 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1332c41b-9cc0-3490-8179-bd85dd0e71f5 | -12.99504 | -51.28261 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| cac0aca8-03fc-3f06-8dff-219166f9d908 | -11.42077 | -43.40327 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdc887fc-552a-3473-bec1-014dbe2db0d1 | -10.89642 | -43.85287 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c07c34e9-0bf2-30be-a9fc-53b7d239a8d1 | -13.0018 | -51.31337 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7081dcbe-d11c-3cb2-9c42-daa276c67bc3 | -10.83673 | -48.69057 | 2026-10-02 04:17:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0997b08-fc23-33ca-9acf-38180734c896 | -11.24291 | -45.23376 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87dd27d0-b6c2-303a-8a93-eca2d2c5776f | -10.56034 | -50.0757 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d355fa9f-3a14-3f47-b27d-f39cce5332f9 | -11.75795 | -43.54556 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d64d66b-e941-3e6b-b644-fe82bf4e5d63 | -11.13787 | -44.61268 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 578f9235-ce3e-3a3d-8483-81d16cbe0e2a | -15.39994 | -43.00053 | 2026-10-02 04:17:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5287fa17-6c70-352e-beb9-9a4e0f200d08 | -11.22692 | -45.17902 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1942900b-dd28-3829-b746-3193cfc48d93 | -10.24629 | -46.62978 | 2026-10-02 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03f8d1ac-151a-32c9-8709-e8e097a0b6b1 | -18.33685 | -40.05678 | 2026-10-02 04:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a4562dc-1ccc-3e3b-947e-3d99498af5ab | -19.03035 | -45.64862 | 2026-10-02 04:19:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1a24ceb-d070-323f-bcd4-15444d50dffe | -19.02641 | -45.65168 | 2026-10-02 04:19:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70b7938a-e5f6-3098-ac0c-8c8418a286de | -17.98548 | -45.86709 | 2026-10-02 04:19:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2077a7f-95e2-3d23-b9b2-cb9ded6d2d38 | -19.25999 | -44.34342 | 2026-10-02 04:19:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac75464c-5ca3-3ef5-8917-e55fce34d62b | -19.39495 | -44.26122 | 2026-10-02 04:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cffc602-da1f-3bb2-be07-25238d5ead96 | -19.03308 | -45.65291 | 2026-10-02 04:19:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
