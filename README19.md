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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1486b4ac-41fa-3b33-b3ee-954c36512ebd | -6.33725 | -38.93287 | 2026-08-31 03:53:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e1365830-f7f5-3268-b7ff-bab98c186be0 | -5.19166 | -35.84521 | 2026-08-31 03:53:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6d051f3e-ee18-3052-8cce-7cfc0772d285 | -8.08561 | -45.46324 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc06ee7b-5fdd-30d9-90e7-6f6617c1d50a | -7.93938 | -44.25099 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9af34b0-d9dc-32bf-9d2a-71f22c5b153a | -7.18525 | -43.71002 | 2026-08-31 03:53:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18559324-1fc8-377f-9d0a-695c0e0ba9e5 | -7.92907 | -44.24931 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 435eeed8-eee4-329a-bebe-56af7de5154e | -8.37893 | -45.00068 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8cfaee67-2816-38b7-878a-ba537e947ab6 | -11.9292 | -45.05952 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3908c301-5110-3f32-8a2d-31d700fb5f4b | -16.28145 | -42.58458 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b33d38cc-8bed-3773-824d-8bb5f3b8688e | -12.95235 | -45.94653 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d925e6d8-2257-3377-86b8-0391df6e22dc | -11.20881 | -45.33363 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49f8404-330d-3006-8680-be26c4e5fa58 | -10.82224 | -45.35786 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc2ddaf6-3116-3411-83c9-e910b403b190 | -11.21525 | -45.32819 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8146895c-03d2-3449-8806-c70f766ab983 | -10.83889 | -45.32661 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8868cdf-092c-37ca-b2a4-825dbfc83a26 | -12.89615 | -45.84946 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69bdefc1-a8a2-32cd-96eb-906694e6e62c | -11.32819 | -45.18643 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cf88e23-99fc-349e-b397-cc29a3f3d7a9 | -10.82164 | -45.36111 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc01e446-5d9d-322e-af0d-9af10e4d7578 | -11.20513 | -43.38054 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 790913e2-a6f6-3158-883a-db23ca747ada | -15.66643 | -45.9334 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9ce1eb1e-291f-351b-bdaa-1a1423e5b1a9 | -17.79202 | -39.70527 | 2026-08-31 03:55:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4c09da14-5647-3e1a-a8b1-ac2e5c491b16 | -14.197 | -46.56028 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fbc3075-4adc-3eb3-9949-4fe369e35851 | -11.88057 | -45.82505 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ded61d3-d9dd-3670-a99c-7ac277972380 | -10.14101 | -45.76101 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dc86d9d-08ec-37e8-b1c7-bcbb4cb237c6 | -14.20162 | -46.56499 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7572b61f-39ca-3777-b368-dd5f4b154bfc | -10.73434 | -47.9651 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 216567d0-1e3b-3f34-8c5b-26c5db52b5cb | -10.75068 | -44.87469 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3819e8e0-e7c5-3e4b-9bbc-1da19173f8c2 | -11.69095 | -47.60481 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 45dee497-df89-3f9a-b01b-257bd12a5071 | -10.83895 | -45.31956 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d240521f-1ac5-3023-9b55-1577a1d27d1a | -10.13174 | -45.75022 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2acbed27-ede6-313a-a263-241fa7f7627f | -11.49821 | -46.93557 | 2026-08-31 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eca8b3f-c11c-3354-b181-975392079262 | -11.78745 | -47.6689 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26c41ff0-3d6e-3720-93bb-f3c20f78107b | -10.84009 | -45.32012 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 739ee017-7e5d-3634-9b9c-b9f52236f153 | -9.4195 | -45.65451 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b71fb7eb-8aaf-350b-8fb2-23f85aa9db24 | -10.544 | -46.20949 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3b4fa61-f683-398b-b90e-30e89c8af6d9 | -11.20617 | -45.05621 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99326e58-faad-35bc-9a0d-fbd3bc833a68 | -11.36716 | -45.20632 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6895ff39-08ad-3916-a6ae-89559eb1a307 | -11.32655 | -45.167 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6baf0b91-ec97-3341-9415-b2a35c474840 | -15.19461 | -46.2472 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18119713-ea02-3b08-9ef8-1b299e5015ad | -10.54749 | -46.20987 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85454e15-05fe-3a4c-9169-ea062b84af03 | -11.23282 | -45.09418 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0786a5e4-7853-3015-b60f-e7839effcd9a | -13.0841 | -45.17728 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11f8cea-372b-3e3a-8cd0-2bf21ce198b1 | -11.37236 | -45.20711 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d844a676-0ab1-394c-832b-0139c3108753 | -10.15401 | -45.72231 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d608715a-fa6e-3775-a532-b32e7404f093 | -12.91555 | -45.91121 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d18e8a95-1679-3872-8250-738f7da182cc | -12.08629 | -44.98473 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6203dd13-cbf1-39a1-8f37-fe41082bcbb3 | -11.33277 | -45.19043 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2aff040-8daa-350d-957c-bf7cfebfcac7 | -12.89736 | -45.84312 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71991e29-719c-3eaa-9028-502483c23394 | -12.0937 | -45.05453 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18119980-56b9-3c75-a559-2dcde2071d0f | -11.3741 | -45.1693 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9587407f-c7f2-3980-9efb-43c83d5286c3 | -9.43932 | -45.67026 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4064ca2b-00aa-3656-b348-5283118e1986 | -11.69213 | -47.60698 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c117168-3046-3cab-ab63-32830d8285d0 | -13.19524 | -44.06861 | 2026-08-31 03:55:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaf877fb-b44a-3a13-a301-20b65e23fef2 | -11.33733 | -45.19454 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f9974f0-58f7-3057-ad05-a2c378a34a3a | -11.22797 | -45.14776 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d97c9480-f9e2-3707-8312-1c4c8241606b | -10.82141 | -50.69356 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecbbceab-e707-38bf-9784-3b9dd51134aa | -11.35799 | -45.22671 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b352cc94-fbc6-37a2-ac3e-983dd5986b56 | -11.32708 | -45.19225 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e364eaca-0b30-3ce3-8352-cff6d3dbb1b3 | -9.43117 | -45.68348 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 270a981c-deeb-3f09-a294-b055ce9e90e4 | -11.21463 | -45.33142 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8267a132-4528-3bf3-a69f-fb52e8f64a5a | -11.36258 | -45.2023 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34a472cc-3a28-3893-8b4f-6ce93cdcb66b | -11.3311 | -45.17109 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c376ca0-89fd-3935-9053-f45327803789 | -11.22092 | -45.1008 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2db67f1-8695-31f2-bb95-140cf84ca1b3 | -11.68431 | -47.607 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 153e3ee6-6cef-33ec-90e0-ac5b504bdd6c | -12.7788 | -46.46167 | 2026-08-31 03:55:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e6b16ec-7d83-3664-94de-27a5a5171264 | -14.74542 | -44.64624 | 2026-08-31 03:55:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c1c603d-9679-3342-a70a-7816035d28cd | -10.84256 | -45.3575 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e81a324e-bc7d-3320-962b-873ca15de2af | -10.83949 | -45.32337 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15bc060f-52dc-32d8-b1f5-8a14a4876818 | -12.0751 | -44.98874 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 979067b1-e6ec-33b2-9aca-05372c6bd657 | -12.08028 | -44.98888 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c71da386-598b-3272-8079-377a13c2a9d6 | -10.85052 | -45.37283 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69d987de-ce64-3a59-a31c-9230f1618619 | -15.02615 | -48.16212 | 2026-08-31 03:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c22a1192-6362-3996-b339-d641f5a6cd5d | -12.89509 | -45.84923 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86c8cb65-d782-33f9-a772-a09fcf297026 | -9.43663 | -45.68473 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f1e4537-879a-389a-a2b9-4695e7705480 | -11.37064 | -45.2163 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36f4f0c6-71db-33b7-816c-48bbf3648475 | -10.73635 | -47.96917 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aede841a-a9a4-3638-b2fa-712f9c9afeeb | -10.75187 | -44.86836 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1a0eed0-9d0b-3e84-af0c-fb08b2ae337b | -10.73345 | -47.96949 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4494167-eb64-3451-8199-db0fccef499f | -11.49869 | -46.93435 | 2026-08-31 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4af85798-f4aa-32ad-92ec-b3d14b2a342e | -12.13452 | -47.25682 | 2026-08-31 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9168c119-076a-3c30-9b5c-6bca9e40f535 | -12.11347 | -45.03305 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482f4c45-7a2f-319c-bfbc-01a1e7df87af | -12.93837 | -45.90601 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 104d3125-e6b6-3c04-a1c2-de9b86ad03cf | -11.21575 | -45.10001 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09e75949-a0ab-371d-99c1-0b7b88248598 | -15.66793 | -45.93186 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3059cbce-0ac7-3fa9-9f5f-326dbabce3c9 | -16.99032 | -40.93327 | 2026-08-31 03:55:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d65f3209-0436-3dbb-a081-bef425155754 | -11.92967 | -45.05701 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1833e7d-3316-38c5-8a43-a6eee1ae90be | -11.79439 | -47.66539 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc5d5f35-b9eb-3edc-9deb-593a3b2f9062 | -11.37466 | -45.16628 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5171cdec-97c7-3163-be3c-d757c1efe357 | -11.2005 | -45.06864 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0944cf60-feb3-377a-b130-d4d2cfa027fd | -12.14694 | -47.25503 | 2026-08-31 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e006840b-c673-3120-bde3-c9dcfb346603 | -13.88395 | -41.63592 | 2026-08-31 03:55:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd311ed0-3d28-3edf-8866-9c38637ac794 | -12.93773 | -45.90934 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22140c2a-3326-3977-a213-ea465d9b1af0 | -15.19771 | -46.23129 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11ded0c0-cf61-3c74-985a-f16888287397 | -12.92015 | -45.91557 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9446c7ce-0f94-3244-a2b6-75914e7ac63a | -14.19785 | -45.30555 | 2026-08-31 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c022c2d5-02fc-3d6e-876e-6bffeb689434 | -11.32535 | -45.17327 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3cb4f4d-17df-3ff7-9ab7-1b28f6a4caf5 | -11.88122 | -45.82167 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b4b83cc-a042-353b-9109-cc725fdd35d0 | -10.83486 | -45.31905 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c11a6301-5f1b-3828-a314-d3501f9630cf | -15.02726 | -48.16522 | 2026-08-31 03:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 85e82c87-cdda-3b89-bd8b-046f0330d41c | -12.10401 | -45.05523 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b2fbd65-bad5-3195-9ea4-9e0f38f168cc | -11.69125 | -47.61137 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README20.md)
