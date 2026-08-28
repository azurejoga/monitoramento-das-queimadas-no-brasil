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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf8898ad-4358-3d75-8a64-32903812de47 | -3.43875 | -59.08371 | 2026-08-28 17:30:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb186b21-8573-3d1c-b096-e3932f87b374 | -1.86927 | -47.98114 | 2026-08-28 17:30:00 | NPP-375 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5313466f-89b9-3079-8e2e-466855af09ba | -3.19299 | -61.13463 | 2026-08-28 17:30:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 623cfa17-c7fa-3186-a2cc-63896a35d07e | 1.29004 | -50.77999 | 2026-08-28 17:30:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4d2fbc4-32bb-3976-bc4d-eb8ecb292910 | -1.19854 | -47.56771 | 2026-08-28 17:30:00 | NPP-375 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3885c1ba-751e-3c69-ac8d-d410f6c8b889 | -1.25152 | -55.71079 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c7a49c48-fa4c-3306-a5f7-bae37545b2f1 | -1.11314 | -50.30219 | 2026-08-28 17:30:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 110973df-8a5d-3bf6-8966-285fd69b5000 | -3.754 | -61.03257 | 2026-08-28 17:30:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fae177e-5dab-3a28-b8fe-98fd41b0f250 | -1.24801 | -55.71135 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 2f04ffe1-f0a1-37a8-a182-7045af9f9360 | -3.45871 | -59.51477 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7ecad304-c42e-3d5c-8cc8-9b87f94de55b | -2.81074 | -57.85666 | 2026-08-28 17:30:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0a4beeb-75e4-34d0-abfd-ee00a770e786 | -1.9664 | -48.37179 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65947ad3-c441-3463-bb4e-f1930ec3cefe | -1.3227 | -56.12775 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61d41ab3-c0f7-353f-bc26-f306edd29ece | 2.09905 | -55.89258 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2e4dbabb-314c-3493-a831-b046fa27bdf9 | -3.46215 | -59.51427 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80c8cf8e-c3db-36a4-a91e-0977a28a7c3a | -1.96143 | -48.37628 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d802e79-7a91-3064-a9e2-441a6bd46140 | -3.62899 | -60.54409 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a36e3cca-1648-3e75-9c5b-2edaf14ceb57 | -1.78835 | -54.96478 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9767e13-b229-3b56-9fc7-f40d94fecb61 | 1.78977 | -55.82224 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8ef3461e-153e-38a5-8aee-7017f5fad046 | -4.32734 | -63.33283 | 2026-08-28 17:30:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 90851195-9145-38e1-b238-1796e32d73ac | -3.34601 | -58.19807 | 2026-08-28 17:30:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6286f23c-20f3-3ec3-b907-17d032263ad1 | -1.10592 | -49.19412 | 2026-08-28 17:30:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b19fb6d2-75cd-3a51-b66c-078bf5d9784a | -2.84049 | -57.23552 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1490c7fe-95c8-3add-a3a2-59c080f67d42 | -3.44125 | -58.02317 | 2026-08-28 17:30:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7543e2c1-fcf0-3fbf-87e1-484f443d42f9 | 2.246 | -50.76507 | 2026-08-28 17:30:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 44308bde-a369-3c9e-b39f-6b59239f7381 | 0.14445 | -60.40056 | 2026-08-28 17:30:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1c93142-2a6c-32cf-99bd-7014d2711f48 | -3.88757 | -60.92592 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 58d14e19-6633-3f0d-a354-b44b136304b4 | -3.90919 | -60.94466 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 69fb9511-8547-371b-92eb-4c242d2f7f15 | -1.58938 | -48.34021 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 63812a3e-8451-32e4-b7b8-a1af44efe4bf | -3.45527 | -59.51529 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bcc4a34c-b417-30dd-924b-a9d4216625a9 | 0.91362 | -59.62881 | 2026-08-28 17:30:00 | NPP-375 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 82352b0b-a465-39e1-90c9-fd8c420d7a04 | -1.38483 | -50.53491 | 2026-08-28 17:30:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a17b8a6-0527-3434-befc-0b947ed2c0fa | -3.21884 | -64.83096 | 2026-08-28 17:30:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d185a0e-5236-30fc-8a38-9a2f9a0b7963 | -1.57608 | -47.7445 | 2026-08-28 17:30:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 49ac99f0-1f0b-35e5-880c-abc6b35fff23 | -1.79747 | -54.97602 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e80622fc-18c0-31d7-8f61-f9d5f3d52d50 | -3.40035 | -59.56546 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e437af0-d7b6-3255-b03a-494e3c4a2e7e | 2.24511 | -50.76704 | 2026-08-28 17:30:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d2079be6-aa7b-39e1-8f1d-f6d7e9fb1dfa | -3.55322 | -60.88145 | 2026-08-28 17:30:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 833ad25b-a701-3678-bf47-eb90ef588e1a | -2.81016 | -57.16534 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12165b80-7770-3432-95e8-f519409102ac | -1.81972 | -55.70364 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57d0884a-df30-328c-96c5-e2365e46a03b | -2.15793 | -48.78626 | 2026-08-28 17:30:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b259eeb0-bae5-35c9-857c-0ef13428aeb1 | -3.88821 | -60.93021 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af0c04b0-3a5c-30de-994c-81b7a5db67cb | 1.9481 | -55.71048 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f0b2d81-c2c7-3a96-aead-f8ba05c84924 | -3.10071 | -58.05208 | 2026-08-28 17:30:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f1d70754-034c-3533-aa91-28592d49add1 | -1.47228 | -46.56414 | 2026-08-28 17:30:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e110db3f-bd04-38b9-bf1e-7f40e972e7e1 | -1.3677 | -55.39215 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 859201e1-35da-3f53-9b14-bad5c84cbe22 | -3.27427 | -64.83948 | 2026-08-28 17:30:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fff4b0e6-30de-328a-8856-a5b42752e31e | -1.77688 | -54.96236 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8ca2d42e-7f8f-3949-91c8-f279a0662ac3 | -3.4265 | -57.99347 | 2026-08-28 17:30:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a89023aa-9f41-34e1-8f43-4c930b9a4210 | -3.09539 | -57.2202 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6942a87d-b0c7-30f4-a10c-fcf6fcff60fa | -2.90346 | -59.21708 | 2026-08-28 17:30:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1173b427-8c79-30a3-8f62-3fd0fa348d60 | -1.74404 | -47.12409 | 2026-08-28 17:30:00 | NPP-375 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c392ee30-11c3-36bc-918d-f0bfba0524ab | -10.7649 | -50.6366 | 2026-08-28 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b786dd88-2c8e-3637-8408-93b15e41df47 | -8.6311 | -66.5287 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ae2036f3-e831-313c-a142-6a19de2186c1 | -10.8993 | -50.4945 | 2026-08-28 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 38a1de6f-af7a-32fe-924f-3cb4bfba7319 | -10.7598 | -54.0179 | 2026-08-28 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5625a150-3ea3-3a0c-b343-1acd6dc12d61 | -8.8399 | -70.8578 | 2026-08-28 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 45740cd3-3c23-3fa1-b244-01c07c2fca47 | -9.2081 | -65.7857 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2797a43e-72c9-36a7-b1c4-49f081d817cf | -8.87 | -66.8935 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 137b45e8-7d0f-365f-9174-7fee9cfae5d1 | -8.5777 | -54.8373 | 2026-08-28 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 2ab2f3ff-33a2-3c7e-b013-6007ae35ac77 | -6.8571 | -59.4179 | 2026-08-28 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ce71e13d-ffb7-3b68-90f4-b540d928b534 | -8.631 | -66.5473 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 21a22614-59da-3a43-a224-d4f5b1388770 | -5.78 | -57.5605 | 2026-08-28 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 2cdff999-1454-3ee4-9e73-09f22d6888e1 | -6.7123 | -58.9412 | 2026-08-28 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b3abe8aa-6a23-369b-a2f8-b0645a163358 | -11.1452 | -45.5694 | 2026-08-28 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| d0722930-94ee-3f9d-8f0e-0e394b8951ce | -11.1643 | -45.5668 | 2026-08-28 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1c428968-d2d5-308e-bf34-64ca0353717f | -8.5975 | -54.715 | 2026-08-28 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f3756fea-8170-3e94-bb6f-1c8f0dd0b8c2 | -8.803 | -70.84 | 2026-08-28 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a005ef4b-3065-3b5e-9506-799175a3617f | -13.4132 | -51.7784 | 2026-08-28 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9cc7ac1c-4608-3df3-bf77-c2cb66a380e8 | -6.6726 | -59.4445 | 2026-08-28 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d75cec32-6915-3fca-86f7-060aaf06e3dc | -8.6852 | -62.9496 | 2026-08-28 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| da616815-3f3f-3536-906b-601394678507 | -6.8019 | -59.4008 | 2026-08-28 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6f550d09-d661-3eb5-a771-449fa0fe6d90 | -7.9169 | -61.3671 | 2026-08-28 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1240786a-db6e-3fdd-a26f-928f4f8d2981 | -9.1525 | -65.7874 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 172d77b4-bbf0-3852-a786-4b2198647764 | -6.9737 | -55.6341 | 2026-08-28 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fbd5cbec-e9f5-32f1-a55a-32b209545e21 | -8.6694 | -49.5369 | 2026-08-28 17:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 536f7ad3-d806-36a1-939c-746b26514fc4 | -8.637 | -70.7506 | 2026-08-28 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d55edb37-8457-3f71-9c01-152f92df5952 | -7.5846 | -61.3232 | 2026-08-28 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b2d4c176-9989-3b23-b34d-c37f3531b0e9 | -7.6031 | -61.3225 | 2026-08-28 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9e5f7c13-9f84-3d33-a8bf-e659b5c91a04 | -4.3021 | -59.4826 | 2026-08-28 17:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 56813b32-60ab-37eb-91b8-3c720b088576 | -15.3654 | -53.7887 | 2026-08-28 17:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ff6ebb45-57e2-3659-9a60-00e80ab4b71e | -8.7772 | -49.955 | 2026-08-28 17:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| deed7358-2a7f-3b34-95d0-c193f5c685aa | -8.6495 | -66.5468 | 2026-08-28 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6594a001-c8d0-3958-908e-f4cd9d286532 | -8.6735 | -70.9883 | 2026-08-28 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9a75d493-26b4-3cfd-be3d-b73b2d983ee4 | -9.4566 | -48.2061 | 2026-08-28 17:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 9ac9ca44-36d0-351d-9644-00cdb82cc6c0 | -8.0739 | -45.8372 | 2026-08-28 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6cd534b7-7cdd-36a1-ba99-b931d3237832 | -8.6919 | -70.9881 | 2026-08-28 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 308703e3-0be5-3490-a575-62e2e248126f | -7.5852 | -61.2089 | 2026-08-28 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 587ea0a2-9d75-3531-85ee-0ba9637ea8f5 | -11.1998 | -55.0805 | 2026-08-28 17:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| a7d19fa6-06d2-3ea4-9a53-7a7ed8e5ceab | -11.006 | -49.6461 | 2026-08-28 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5567229a-50bd-31a4-9c02-f1138b391fb9 | -22.85316 | -49.34239 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d49997a-5613-3034-903b-3becdd7ffd42 | -25.49522 | -50.48214 | 2026-08-28 17:41:00 | NOAA-20 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 7383cacb-9ead-3726-93c4-f073999bb814 | -25.57105 | -52.86049 | 2026-08-28 17:41:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| feee4f9b-ec24-3129-9936-832dd8d75704 | -24.64585 | -51.5893 | 2026-08-28 17:41:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 28a124cf-f70f-39d0-9a38-4fff665716c8 | -22.85135 | -49.34422 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2bc21025-3755-3921-b202-81e132104956 | -28.6104 | -55.32133 | 2026-08-28 17:41:00 | NOAA-20 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 12.1 |
| dc61109a-07f6-35c4-bd7e-dfe7c6fcedc5 | -25.49469 | -50.47944 | 2026-08-28 17:41:00 | NOAA-20 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4205702e-5d02-385c-b192-25a2440e314a | -26.19422 | -53.26766 | 2026-08-28 17:41:00 | NOAA-20 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 1c71017f-4a79-30cd-8a59-9731228226e4 | -22.78653 | -47.62714 | 2026-08-28 17:41:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 506e1397-a2d3-33cb-bd3b-23f009de652f | -25.03492 | -51.19728 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |


[Clique aqui para ver as próximas entradas](README134.md)
