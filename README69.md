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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eced44f7-9cc3-3969-9360-33e7c2ed8741 | -11.36225 | -46.55888 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb2b310c-6317-3273-a524-acd22262aef3 | -11.48098 | -43.67788 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e293374-5d83-3eb1-a37d-6f8fca0d3f7b | -9.08066 | -46.96818 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4d7efaa-8612-3785-a163-eeefe1f20dad | -12.0549 | -50.93404 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f888cd2-8c50-3b60-b15e-215acaf161c1 | -11.77512 | -46.50253 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c54de7b0-cd0f-3a1c-8137-8b56db54828e | -10.32351 | -48.81059 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e518551b-03b3-35e7-853c-d135c8369162 | -12.37984 | -54.17438 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbfcf51a-8cdb-3754-9078-eab9fef6b6c4 | -12.16698 | -48.48756 | 2025-09-11 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 203cdf44-9c7e-3380-94ad-d5e4a800a81b | -15.80803 | -42.57168 | 2025-09-11 04:23:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b5dd608-b2a9-3ac4-ac5c-5283a21ff404 | -9.53423 | -48.30059 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39e029d7-c28e-32cc-b71d-722aaaf5adb6 | -11.42071 | -43.54705 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5686f592-c980-3d43-85c8-1d60ef06aa83 | -11.68464 | -46.89492 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3670e4d-5e99-3cb0-9e8b-eb185896a1e2 | -12.4228 | -47.81242 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86bb9e2e-0d7b-34b6-b6ac-dce2819f07e2 | -10.00273 | -51.71641 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcd27fe6-f208-3331-a3e1-a4a5d7d10d90 | -10.54994 | -49.88071 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86e25234-c1f6-37db-8e08-a344969a53da | -11.87966 | -58.81508 | 2025-09-11 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7da2d3e5-9252-32b4-8b76-e73627442023 | -11.37733 | -43.52159 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab708747-e974-3d2c-ad8f-4bdea46bd4a7 | -11.36895 | -46.55994 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| faa23571-176c-3719-8e59-605fed748ff2 | -9.05689 | -47.0713 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae2e3b67-e0da-347c-87c3-98aa47fa0709 | -13.6503 | -45.70151 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8153e8ec-9801-3188-8c9d-990cd3e5c73a | -15.22694 | -44.01978 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d09f3b6-76c1-3cc6-b16a-551ebc179356 | -10.31917 | -48.81421 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 384f8960-4c4a-3b1b-b0ce-ce576104d792 | -11.50466 | -50.39103 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ccb1ca0-50d0-3c27-9cdb-fc04c649108d | -11.49771 | -43.66084 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21979393-aa2f-32d6-9928-e8cd58e1b44c | -11.47858 | -43.63514 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 102e699a-b2f5-3eb2-89fa-e3ffa087913b | -11.7197 | -50.63314 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 115810a1-3e2c-351e-834a-2962df3a0593 | -11.49252 | -43.67183 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b91413-3414-3bf1-a2a6-c9baa9377a36 | -11.48616 | -43.66689 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87384a11-9080-38c0-ab99-b7f9aa8e91e5 | -11.08268 | -51.32995 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1df120b7-dd2c-3374-8830-e2d9a79f53d0 | -10.48161 | -49.3713 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7be34e6-7176-315f-8add-beccf0528d19 | -11.02533 | -45.06029 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3134de39-b7f9-33a6-a4ad-15c0aeecd22f | -11.63211 | -46.76091 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0a7e082c-9468-33e7-b5cf-ba693c7f1ef1 | -9.67909 | -47.52409 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f87005d-7b65-3bb9-9672-e4e050aaa613 | -12.93143 | -54.79769 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f6bfb64-57da-36f1-9976-5c5c7a88f23a | -11.47927 | -43.68939 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8abffa88-47c1-311c-9bfb-ed83540162e7 | -11.44447 | -43.57859 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1432d26-de1e-3be5-a6f0-b76b8a29a2f6 | -15.19573 | -44.04142 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4d35096-0974-310a-b70f-35e576f1674e | -12.94565 | -54.7502 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e07a5734-605a-3036-84e8-3cd06fcab5d2 | -11.50075 | -50.39032 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2b51d6a-f68d-3add-b105-cd17239dafe0 | -10.18742 | -46.21074 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaf10429-35b5-30d2-b5b7-4219617b2e1d | -11.47916 | -43.6313 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a6491d7-0e90-3901-a127-887050ad9ff0 | -11.39459 | -43.53106 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bf7c137-c148-354e-88b9-9e880e89df65 | -8.51742 | -54.76799 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a678f76-5f6c-39ef-8b49-2ca9fadbae31 | -13.84708 | -47.34844 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bef5abca-40c8-3a22-b60c-7c9c8d67203b | -13.65321 | -45.7163 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0eafc301-658b-3a72-a22b-3ee0edcccafb | -13.95425 | -48.22997 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b1e1384-2287-3385-a584-364875ddef0c | -12.92197 | -54.76411 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eb5e25b-12c6-3b9f-b7c0-74eadf62f7f2 | -10.37816 | -50.52191 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 867fdbec-001b-3af3-8ee6-5d2cecbb75b1 | -12.01238 | -47.5869 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bfc18c8d-3657-37d3-9715-0baf96f3e930 | -11.13582 | -48.34809 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 867947aa-b13e-3da5-a472-2d4020b1c43d | -11.08699 | -51.334 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0cf30b2-9857-3e8a-8c3b-242ba1fad759 | -9.52134 | -54.63966 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26a867dd-34c9-3cf8-a781-3b7d643730c5 | -12.01737 | -47.59926 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 675d4d3e-5592-3729-bb74-9e9e106835fa | -11.0411 | -46.05256 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a5c6257d-c11c-39f1-ad05-951a31a8cde3 | -11.04166 | -46.04904 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a1590e7e-039d-38f2-8059-45ad3ff00877 | -12.93201 | -54.79461 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88585222-475e-3b40-92f8-97745bbc4e1c | -10.556 | -49.89171 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3577399d-cd3d-3be3-97ae-daa9014fde4f | -11.47908 | -43.67844 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60841738-e12c-39b3-a854-ec7d66d74ee6 | -11.48388 | -43.68226 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f929ce5-e5f2-3541-9aac-f71b6f64adbd | -12.43429 | -47.80668 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 719847b9-942a-3e27-a0f6-0c379d6bd7fa | -11.87312 | -58.81322 | 2025-09-11 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5c372b7-ccf7-32b9-969f-25ae34261d24 | -11.79636 | -50.58007 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98c1e2fb-8e33-3681-b957-c4b498b49d5a | -11.35181 | -46.5063 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7666e1c7-29fc-3327-9989-45c868a1932b | -13.05385 | -47.15409 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 284e2124-2500-33f3-9d01-d5cc6253ccf9 | -9.06498 | -47.06479 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fc37c2c-359c-3537-93a7-fbc3a0194196 | -11.02867 | -45.06083 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e08fce3f-f54b-3f3b-9607-e86eb96d1509 | -13.84372 | -47.34795 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a49e218-38db-313b-83f9-a823e49be18b | -13.58376 | -47.69878 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54bab383-63f4-3d45-bc18-f016e917c909 | -12.06041 | -50.94964 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff28d839-c531-3a99-8e4b-7761c2fcb27c | -12.60721 | -56.97076 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66869d0f-fe74-3161-b767-7db1b35dc0b2 | -9.02777 | -49.78006 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d80c8b69-abf3-3f8c-b0ed-1a07f739381c | -11.11659 | -48.3983 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7af7f8e-c456-3f60-9455-8d6ede49f37a | -15.22519 | -44.05694 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd3071ae-9a10-391e-86f3-effd9b5441eb | -12.00094 | -47.5926 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e518849c-ca9d-3825-b27f-856b7aa9e7c4 | -11.47562 | -43.67791 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce570dc-4220-3ff1-9218-97b94c1dd3ce | -14.27856 | -49.39608 | 2025-09-11 04:23:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6874b57-3ebb-35ef-9ec3-62e1b5649732 | -11.80867 | -46.75325 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ccf4faa-d70e-388b-9320-beb47d1b9e77 | -14.41356 | -47.3252 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4ff9e3ad-4e0f-3194-8cac-feb248e5074a | -14.38851 | -47.31 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4491712-f56b-3490-b9a6-e7c7f03945b3 | -8.5709 | -51.35604 | 2025-09-11 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86ddae6b-d444-318a-a805-d64b9bdf1f7b | -11.73334 | -50.62503 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e163771b-dcda-3db9-b7a4-c7d46f1378f9 | -15.22283 | -44.04826 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ff8c7d0-15dc-32ca-87c6-039526063508 | -10.48083 | -49.37584 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 893167ee-6ae5-306e-a3cc-fe412f470338 | -12.98196 | -46.73725 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbde3cbd-02a9-31e9-a2a1-c3a004bb453a | -11.36246 | -46.51505 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e57d468e-1421-3e2a-b198-e12a660cd2af | -15.21871 | -44.05176 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffedee59-8340-3f6d-989b-0e4310c95009 | -14.77867 | -48.23206 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f9cbaac-4a43-3179-a471-305cf986c137 | -13.16747 | -45.28256 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 060bb8c1-4b94-3a2f-9347-fb6ecbb2cfcc | -9.2023 | -51.80948 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b615e19-514b-3269-80f1-127b3f74a5c9 | -13.66992 | -44.22262 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53019c4e-1b06-3372-8d56-b33554ed69c4 | -9.01742 | -49.52955 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 757625b4-2453-34d0-a884-b98d21edb27c | -12.60218 | -56.96534 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e6d04c5-b8fd-379f-8267-34db870a3ee2 | -9.7599 | -47.85038 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d6c6fbf-675f-3408-939e-29c1acbe7b1e | -9.05533 | -47.05926 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee118088-2838-3559-9e3f-b13d0109486a | -12.90938 | -47.9964 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a4d2fd0-28ea-3479-84fc-b48643308cbc | -11.3265 | -47.37853 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ee8d8ed-4f4c-37b9-ae17-d11c2b9aa651 | -11.77405 | -46.48777 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 514d9d46-c8c7-36eb-a0db-13fb20386976 | -10.7344 | -48.28797 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e8fa158-ee95-3849-a936-ee6d2980c002 | -10.31697 | -48.80493 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5beb7a5e-7f18-30c9-bf93-ba1b20802a8d | -11.40621 | -43.54878 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README70.md)
