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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7a115dd-0071-33cd-8621-29d9d2bcacd8 | -21.05448 | -47.32488 | 2025-10-25 00:30:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 527d4571-9208-3b09-be6b-9e266df715cb | -18.36519 | -49.3089 | 2025-10-25 00:30:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 423e270e-a8c1-3c89-a6da-89e1e0a1d148 | -18.371 | -49.30227 | 2025-10-25 00:30:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d4d4a05-3b93-3a8b-84bb-e6a1396e02c4 | -21.05576 | -47.33442 | 2025-10-25 00:30:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a1290920-6c52-3055-94d6-68cd027982ed | -22.15089 | -55.26442 | 2025-10-25 00:30:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 49fe2fb4-31b7-364f-a6e7-89c6e3d73a7e | -22.32071 | -52.27394 | 2025-10-25 00:30:00 | TERRA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 7fae821d-4d28-3000-ad93-3bbbe216fb3a | -19.87816 | -45.83158 | 2025-10-25 00:30:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29578ced-2cdb-3e4a-ba49-c224d3214e09 | -19.76713 | -48.29727 | 2025-10-25 00:30:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 326.9 |
| d08f8ba0-d0b2-32c2-98ea-422e0ba7bfac | -21.49818 | -44.6775 | 2025-10-25 00:30:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| e4d20870-34c7-31c0-b71e-d1264757dbff | -19.33805 | -49.09193 | 2025-10-25 00:30:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 963c3d01-10f0-34bb-a295-69e4d0ae1225 | -17.37904 | -43.12829 | 2025-10-25 00:30:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 15096c16-ae5b-377a-9506-d42efa3749c0 | -19.32876 | -49.09328 | 2025-10-25 00:30:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d72b17d6-abd5-3a52-9297-a9b6a39d40e9 | -19.84789 | -49.06668 | 2025-10-25 00:30:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d4083cf-5a51-344f-b473-940c0e9837a9 | -19.87205 | -48.32563 | 2025-10-25 00:30:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 48283693-2897-3e53-a289-ab0de3b00922 | -19.62984 | -46.80512 | 2025-10-25 00:30:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d50dbbbb-895c-3972-8ea2-092b03357cab | -21.20128 | -46.71878 | 2025-10-25 00:30:00 | TERRA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| f8f2e747-56ca-38ab-888a-f044c2441b73 | -20.32551 | -55.22001 | 2025-10-25 00:30:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b992aa70-6d0a-37fe-bf20-7e56927dd410 | -19.76584 | -48.28745 | 2025-10-25 00:30:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 370.3 |
| 15e82034-8047-3807-b1f2-a43a7aaefa64 | -17.38406 | -43.11976 | 2025-10-25 00:30:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d9afc35e-543a-32bf-920e-f4d1f358a05e | -20.29539 | -47.15446 | 2025-10-25 00:30:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8c2503f-5593-379f-af56-a80bfddd6260 | -20.32408 | -55.22543 | 2025-10-25 00:30:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 48393dd9-0e15-32d3-88b4-19ddbe57d976 | -21.50609 | -44.68021 | 2025-10-25 00:30:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 98dea880-fd82-3b44-a56d-388c3fe3cb43 | -19.33671 | -49.08162 | 2025-10-25 00:30:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c9e662b2-477d-3a51-93ac-d670854c981f | -19.32743 | -49.08293 | 2025-10-25 00:30:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ad9908b6-6cca-3621-b1c2-f17efee7accd | -20.38868 | -45.92297 | 2025-10-25 00:30:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| fcc6fe6b-e8ce-3885-8ead-bcf1df7dfaee | -21.55006 | -46.51263 | 2025-10-25 00:30:00 | TERRA_M-M | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7a484e28-f97f-31f1-a4bb-0ee48889c8a9 | -22.1535 | -55.29458 | 2025-10-25 00:30:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 388237df-e0a2-33b2-9f1c-f8a3f4fd618d | -17.38623 | -43.13353 | 2025-10-25 00:30:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 483f12c8-fd1c-3c23-a154-21cafc95e216 | -18.91667 | -47.24833 | 2025-10-25 00:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fa154d4b-4902-3629-aa20-9d831d6def91 | -20.87693 | -42.97408 | 2025-10-25 00:30:00 | TERRA_M-M | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 3c526202-5294-38ec-89bc-0edbfbb91761 | -21.50455 | -44.67004 | 2025-10-25 00:30:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.1 |
| e0083c5a-a37e-3606-b8ff-fc8b004a3c26 | -18.5615 | -50.28156 | 2025-10-25 00:30:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| 7ed0ae24-2221-3152-8676-07e12cc08b0d | -20.38731 | -45.91344 | 2025-10-25 00:30:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ced11492-ca3d-3ae3-a296-e30b722af991 | -21.49666 | -44.66727 | 2025-10-25 00:30:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 787dc64e-6752-3bce-aac0-7c482c8e61ab | -22.13843 | -55.29573 | 2025-10-25 00:30:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9714c876-fcd0-3d76-96c8-4267c9162a1f | -12.63733 | -44.30383 | 2025-10-25 00:33:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 25292340-aeeb-3e1d-9162-c2aacc726860 | -16.06371 | -46.61432 | 2025-10-25 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23fae410-91a1-322c-b615-d8330e70544d | -10.70638 | -51.87002 | 2025-10-25 00:33:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3311abc9-b985-34ae-801d-ce9279683255 | -14.47544 | -45.27177 | 2025-10-25 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87b5e207-afae-3ab7-af26-4d8778db6320 | -10.51638 | -50.24921 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 71b03a43-732d-3435-9c54-ccf4e88859ad | -10.6599 | -48.07988 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6b2f4b9c-52e2-317d-99a1-8ef2716240f7 | -11.43693 | -44.67943 | 2025-10-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 99316c20-68ea-39cd-b405-1487800e02f0 | -10.62135 | -48.07261 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98432d1c-2665-3ffd-9683-27ae39eb1093 | -14.92427 | -48.13505 | 2025-10-25 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5b827d46-bac9-31fb-af5d-fe3dcb8374e7 | -14.46224 | -47.92892 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e65e37ac-fb8d-3fd8-8398-731c85e3ed04 | -14.36969 | -51.81151 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1a00ca45-e2e5-32b4-abc2-e40a8d1efd36 | -13.94322 | -43.80832 | 2025-10-25 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 169ecd38-8151-3a55-9afe-2dcf7c279475 | -12.13149 | -46.71497 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 76082104-52ca-3558-936f-8d49a9b70461 | -15.57996 | -43.21928 | 2025-10-25 00:33:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| bd29c05c-1afd-34ed-87d4-918a52bfbc46 | -10.99685 | -50.33354 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4fedd59d-2bb1-3f1e-997e-2b7f8011bdb7 | -12.82842 | -47.25859 | 2025-10-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc1fcd15-5ab3-3177-bfce-381892ada8c7 | -10.56516 | -47.9974 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c11dffa-6a77-3cb7-82c6-9364ece95c0f | -14.89658 | -47.87037 | 2025-10-25 00:33:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c966645-b4d6-317c-b116-01463df89686 | -12.7726 | -47.38139 | 2025-10-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28982d01-2c0b-393f-85d2-832c728757c2 | -12.13004 | -46.7051 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 25ce28d7-98d4-39f4-9198-a9c609b58e81 | -10.95542 | -50.29707 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 996310fb-7528-3bd1-b76b-b1430fe5e7e5 | -10.51388 | -50.23056 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6ccc32a6-c083-3c7b-886c-448e737f9d0a | -15.2367 | -47.93983 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95560535-0e49-300c-bf02-dd2b6a645609 | -14.15287 | -44.30923 | 2025-10-25 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47bc3f03-b24b-3800-a429-b976761afa38 | -10.57697 | -50.22169 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8956699a-9e77-3236-ab92-85237b0951d7 | -13.88278 | -48.40026 | 2025-10-25 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bca407ff-ecec-3c6b-9bba-58fc31e3bc04 | -16.49199 | -43.65631 | 2025-10-25 00:33:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d2516b87-3739-3ab8-96dc-fe4c921c9cde | -11.5469 | -43.15187 | 2025-10-25 00:33:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 504dc871-a296-3dd9-ae73-5a1b9ae0373a | -13.26472 | -50.36549 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd88e769-375e-3614-9cc3-106199c880c7 | -16.06506 | -46.62379 | 2025-10-25 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 11d02360-b633-364c-9ab6-8d974f409b33 | -10.51513 | -50.23988 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 827abb7e-6b16-3ce4-a927-895510d6b5a4 | -11.00477 | -49.84201 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4276dbb9-bb59-32b0-b9ef-1b2e3ac4b182 | -14.18206 | -47.31219 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 47261a58-fe39-3922-996b-a65bbdfbafd0 | -10.6108 | -47.86841 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55ab4ac9-d635-3f31-97a9-c5bee78f04d0 | -17.21436 | -47.6551 | 2025-10-25 00:33:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d60e80ac-5d28-38bf-b94e-62523887d61b | -11.55767 | -44.68797 | 2025-10-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a55854b0-6e9d-35bc-bf56-1c185d84624a | -18.16862 | -51.75072 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 252533e2-15fc-3a7e-8679-7ab534cdc414 | -10.42586 | -48.05817 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 067246d0-2604-3252-95d2-6d64fde6c957 | -14.15725 | -44.31429 | 2025-10-25 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1bc7f6da-4f7e-3896-a110-77d02a8b4e16 | -14.37096 | -51.80504 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 082f35c0-b2d0-3122-b2e6-db08e13199be | -11.14498 | -44.93231 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fab73d27-2cf0-37d9-aaf2-2fd88185bfbc | -10.84766 | -48.96947 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 66415bd6-7b40-3cd5-9930-20baaa2425c1 | -14.36819 | -51.79908 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5992fc70-77a7-3ab7-842a-1818ae18b0a7 | -12.06983 | -46.40231 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fa6df6eb-d97b-3172-9672-d2d09788ebea | -15.00659 | -49.98903 | 2025-10-25 00:33:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c5ac756-cb24-3b73-839d-72c924e702f4 | -13.45284 | -44.07047 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dc1f65e4-22b6-3721-a3af-a61f2be43e51 | -11.00191 | -50.37149 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6817063a-9456-3679-8bf0-a3dc5f5cafe8 | -18.1578 | -51.75195 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4536942c-ff6f-3f84-bc6e-1d2707eecf44 | -12.12081 | -46.70656 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ccee5b90-ee3d-3208-88e8-f4e5685bcba7 | -10.51763 | -50.25854 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4832000d-a73d-34c3-ab11-4d4ad28d0d69 | -10.70923 | -51.87457 | 2025-10-25 00:33:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ed8a2bc-cbcc-38bf-9691-88b57997bcbb | -15.24409 | -47.91426 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 104ff730-1709-348f-ba18-d60b19be11bd | -14.36227 | -51.81878 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6376dc3b-1283-3f39-a547-7e87e2c27782 | -14.86898 | -48.07512 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 396cf58e-2898-363e-ad61-1bfcc3538af2 | -10.42832 | -48.01105 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9bda048b-22fc-375b-8084-fa5ec59f760e | -10.55407 | -49.77848 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f8cbb7b-ce51-3ad5-a23f-8242f0712b6c | -10.80386 | -49.6504 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 490aa942-b420-3037-b835-fb3212c3d3d0 | -10.87695 | -48.05403 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 86d0abd2-2fef-310e-9a7e-87ff4a954c19 | -10.59012 | -49.64396 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2faf3c2c-b6f1-368e-9552-363b740d7ce7 | -11.85305 | -49.85554 | 2025-10-25 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 593c0c60-59d2-37b7-834a-3eaa3a346173 | -14.54279 | -48.04061 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0ce7a517-a427-397b-bdd4-52a28cd63273 | -18.15946 | -51.76624 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e3ff0f6f-4471-3f35-8497-be0e803d9d44 | -10.47336 | -50.20463 | 2025-10-25 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc70a54a-3f0a-3882-b47e-387bdf503266 | -10.82316 | -48.00308 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34601c3b-1811-37c1-a074-4e6f879f0f1f | -10.93468 | -48.06694 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README3.md)
