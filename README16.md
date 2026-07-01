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
| 3c1cbfed-b23f-344e-a937-a91c69227e98 | -8.15613 | -46.66492 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60bd671c-a701-3880-9ce8-f5aad2de25ea | -13.47476 | -47.87681 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 621a14a7-9188-3c30-90c7-c0939edb0d13 | -11.0192 | -45.24346 | 2026-07-01 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d17708-467d-39ca-886d-72d410a90408 | -9.0215 | -59.53522 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbdc1c0d-46a5-38a4-b3f0-4d35fb97887f | -9.60165 | -56.9348 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc8456fc-d470-32e5-83f9-cbbee7ccca84 | -10.76362 | -53.54723 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d743fba-89ac-3995-953c-7045d9dd1358 | -10.66718 | -54.53852 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39684546-29d0-3fc3-ba94-c2f788395963 | -12.77013 | -44.49954 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| c32547bd-141b-34a1-8a34-a662fc1bf5ab | -10.80127 | -53.54366 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51363800-54b8-3a9a-9d35-2e9d3317a9d1 | -10.84258 | -45.0543 | 2026-07-01 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4ba4c09-a822-3d19-a6fd-b1baeba0bb16 | -8.15335 | -46.66091 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6d68683-d1f6-3386-a957-603e6284c87f | -12.41212 | -58.39552 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bcc586ad-5baa-39b1-8087-474cb452d6ca | -10.68269 | -54.53157 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 781374e6-98ec-3749-b5e2-d459af51d184 | -11.43048 | -56.06037 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d1b5d6f-0562-372c-b31c-7cefeec9ef57 | -12.82824 | -44.34891 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| a4e7aab3-91d3-3ebd-9229-658f24e90598 | -9.6037 | -56.92377 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ddea21f-681e-3434-acf7-ead590537d4c | -12.84677 | -44.35175 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2e333790-a78c-3fa9-a309-541c6bf563d1 | -14.2043 | -42.76449 | 2026-07-01 04:38:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84f2c459-9cee-37d5-a255-5bc9593181d7 | -12.79812 | -54.86682 | 2026-07-01 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98e5ffbc-43f4-3c7f-b73e-018c0a3f4746 | -10.9274 | -43.04997 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ab5f338f-5793-34cc-95df-f5e9281ab4e7 | -8.59143 | -50.97652 | 2026-07-01 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3b1e9e8-a34c-3876-82a8-9e7f167b3a68 | -10.85324 | -56.66116 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc84176d-0ea8-3ffe-aa9c-6a96774fab39 | -10.67809 | -54.53072 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 27ba6b66-e532-387f-9c45-bf38af8b5dcc | -11.90193 | -57.38715 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f83e1fe-ab65-3258-bbc6-cf54d375cdbd | -8.59861 | -48.00428 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d6f241c2-945a-314e-afa2-4a9b49b1a027 | -10.77726 | -53.54534 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0e6f05f-3d29-35c0-859e-3eac7416b69a | -12.77142 | -44.4908 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b470a45e-7ed9-39a0-a0e9-ee3b0b0833dd | -11.50504 | -54.50657 | 2026-07-01 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab547aea-31d4-3abd-b2de-fd0e5a94e461 | -11.56314 | -52.80499 | 2026-07-01 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b32f060b-fbdd-33de-8aee-0acc69710f10 | -11.42545 | -56.05941 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ef463775-8b9a-3a48-9d01-9e26bb04a308 | -10.66974 | -54.52435 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0edfee4b-13da-3629-9532-bdf89843001b | -9.16998 | -58.06247 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab0557c9-2d0d-33d8-90fe-8141f276f1cb | -8.49288 | -47.20764 | 2026-07-01 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c2987b1-a7d3-3089-b7f5-6c1e1014e943 | -10.79088 | -53.54355 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a329c35e-1b2f-3cd2-9ef9-d1811a00b0a8 | -11.63714 | -59.01474 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5bb2938-bdd4-3b80-be16-2c24e94f52dc | -12.46413 | -49.5867 | 2026-07-01 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68b3ac75-b276-31c0-bcc3-3e3de60c9e05 | -9.18023 | -58.07353 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cbb767b-0a25-344b-8f76-7a867495e9af | -11.91024 | -43.39599 | 2026-07-01 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d4a51a-f6ee-38c6-a168-870e458e9576 | -9.08971 | -59.49761 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb0f3c6-3be1-384f-aacc-fb7d46efd888 | -11.50052 | -54.50569 | 2026-07-01 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 485e700d-a7d9-357c-b595-6185eae55495 | -11.54973 | -47.4561 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| db6e2f87-13b7-3700-bd9b-923b587e376e | -11.89002 | -55.53132 | 2026-07-01 04:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed8a895f-f3b5-3397-96fe-86d90bfb8cbf | -11.93827 | -57.0467 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df755da8-636b-333b-b3c5-68cef25a81ea | -10.76038 | -42.11144 | 2026-07-01 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b268e487-b033-35e3-9953-8077f306fb12 | -10.13237 | -52.10158 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d485fc7-e348-305a-92c0-9f48dfbb2b0c | -9.88693 | -50.39769 | 2026-07-01 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3720ba65-7920-316e-ab50-c0b70f12dd1b | -9.33088 | -58.0213 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd163c1f-b0ee-33df-ad3e-0a56bb9cbb83 | -10.8521 | -56.65696 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34cc6d92-9bb9-31e7-bf23-fc1120b6b40d | -12.07378 | -49.77393 | 2026-07-01 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 407b7326-67d0-3c12-8ecd-c901d3437bb8 | -11.91876 | -57.38338 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04a4a33f-f07b-3286-86c3-d335c35863b2 | -11.49986 | -47.42636 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95ab6ae9-e490-3772-985f-d2fbf373bdf4 | -11.42374 | -56.06842 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7e23c49-a002-3568-8e96-5f4bc228bd1c | -10.85145 | -56.66029 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ceb01b56-fb8c-3f71-9987-756949e64fd9 | -11.84398 | -56.94808 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eceb90e-f9ec-3f5a-ae80-767cee113c9f | -12.44771 | -49.58002 | 2026-07-01 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 820b137f-addd-3377-93c7-5abe3fa51474 | -7.70677 | -45.93663 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beffe218-e5ff-3154-8cd8-edb370da5aa3 | -12.84613 | -44.35622 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 05f65b16-819f-331a-9540-95b378fcb8c8 | -9.27878 | -48.76312 | 2026-07-01 04:38:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8faa4d6a-b479-3673-97ed-603dddda8d6a | -10.81299 | -49.34108 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ab1571-d489-36c8-90c8-5a5fca91fbfc | -11.43629 | -55.92106 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55a66ca7-8e09-3244-b489-6ba830beac0d | -11.4883 | -47.39578 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a8b2e3c-e407-348e-ac2a-859b673cc38d | -8.13108 | -47.88523 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8c69266-480e-38c1-ac29-00c7778e1e6c | -13.08792 | -42.14082 | 2026-07-01 04:38:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30bc3277-5edf-32f1-b5c1-e3c2f0824d45 | -12.76646 | -44.49899 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 107061cd-0de6-3ef6-9b43-bea9464753cf | -11.53089 | -47.44582 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0c9a715-dc35-3763-96bf-ef01b8aa5867 | -11.54917 | -47.45963 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82f21ff1-014e-30fd-af31-659c68fbd3b4 | -9.68707 | -56.0927 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e36efc7c-02b8-36cc-9099-2ae6ae782f58 | -8.78153 | -44.8278 | 2026-07-01 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff303d73-13d5-3ef5-b9bc-e6e97ee0b2e7 | -11.42876 | -56.0694 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bf17901e-ab1a-3300-bce7-36b7fab2d763 | -9.74727 | -49.0406 | 2026-07-01 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07c35c04-a235-3f91-9eed-b9b887230bb5 | -10.12138 | -52.09439 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| db0c5092-6c83-3cac-b43b-9aab6a7e280b | -8.61192 | -48.02842 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e78c895-023e-398b-833a-a3279ece2853 | -11.42819 | -56.07241 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4c71b7ca-15ad-3688-b546-b2c757cd8f6a | -11.83933 | -56.94373 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c14a0e42-4155-3e86-b055-dac83287ad08 | -10.43593 | -49.59082 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f4c5cbd-b45f-3ca4-9c66-3f9a57ab71a3 | -12.76103 | -44.48478 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b183b740-51ed-317b-b0a3-62e78211b076 | -7.73861 | -45.91959 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97affd42-685a-3108-b3fd-552061611057 | -11.63524 | -59.02425 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b347cf61-3f33-312b-a7a6-dc206294eb40 | -12.7647 | -44.48532 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 74cafc94-8cde-33aa-a91e-9607a1679b16 | -9.69166 | -56.09692 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358195c5-44d8-3c3f-a08e-c1dca812d738 | -11.63619 | -59.0195 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cffbc238-4627-3405-9ac1-8d3702c69693 | -9.69686 | -56.09788 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea7f6dc-104f-334f-b786-45b58910e10b | -9.68646 | -56.09596 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc9eaac0-88e2-3c97-9d20-5fa40df6fb89 | -11.80063 | -57.00189 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63c2a382-9913-3e6f-bc58-874dcabc6843 | -10.67178 | -54.53935 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e62084d-5998-3a77-b77b-6e7c2c5b02b6 | -8.50527 | -50.15104 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4223d38-32ef-37f7-9734-c09579f45413 | -11.92255 | -43.39278 | 2026-07-01 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5520ef01-88f3-3e61-8f45-408758296d15 | -10.37919 | -49.58916 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc378d9c-12a6-3305-9158-dee54c1ca721 | -10.83912 | -54.03321 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63e79847-4f7b-38f1-a6a0-4781a4b677a3 | -11.90736 | -57.3882 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ed85ce-11f2-36bc-8791-145c1995d1d8 | -9.17429 | -58.07233 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd7b20c8-a563-3f4e-9405-bcf0a1953cef | -7.74767 | -44.19255 | 2026-07-01 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73147f09-8774-354a-9cea-3e2c13a9d73a | -10.67519 | -54.52049 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c418bd29-a61b-38aa-9399-614363a00020 | -11.54252 | -47.45855 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea2f9083-b2c8-38b3-98a6-f189150981c1 | -9.60851 | -56.92851 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d09a3b-2bad-3146-9fa7-83041ce5f293 | -12.75735 | -44.48422 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e4d11bf-aaf7-37fb-b871-2f2dbf3d1d90 | -9.60783 | -56.93219 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39a354c8-fcad-3ffd-ab29-c993072a84e8 | -11.90263 | -57.3836 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548611a7-5b80-33e6-b851-9bd1bf5f363f | -11.91895 | -57.38668 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f6c8455-118a-3373-9eff-f3ccc0c9f41d | -10.75679 | -42.10711 | 2026-07-01 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
