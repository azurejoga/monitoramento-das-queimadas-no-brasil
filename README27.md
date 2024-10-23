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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe3f0d1-6fcd-36de-bfec-48fa7b33934f | -10.93071 | -47.82867 | 2024-10-23 04:00:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 921968a8-5c74-3d86-a627-b0fab281edd5 | -10.92987 | -47.83324 | 2024-10-23 04:00:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39466128-c7f7-375d-b9b2-26d56614f149 | -10.92901 | -47.82997 | 2024-10-23 04:00:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2cb9a696-3476-3624-b38f-540d850b7d6f | -5.2651 | -48.2709 | 2024-10-23 04:00:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 407eac02-6011-3ee2-9827-dd26b9bf7b47 | -5.49367 | -49.5083 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd589fbb-831c-3e7f-b603-4b46b39054d3 | -5.4875 | -49.51096 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c94e59f-aefa-3c4d-8ea7-54efd88e1d60 | -7.56162 | -49.93348 | 2024-10-23 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2de0b385-8bdf-3a9b-a3ae-be6e25d26fdc | -7.56096 | -49.93713 | 2024-10-23 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17363287-0e30-34d2-b654-9eb0ef4fede4 | -7.44939 | -49.64695 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 55f89aac-80e7-3a5b-a8c6-9761d1fe4cc5 | -7.44778 | -49.64709 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd1fc42b-c1f9-381e-92a3-368d4a5490bf | -7.44399 | -49.64593 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5be706a3-4d57-3893-bf16-ca87f9f04abe | -7.44335 | -49.64938 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0fc876d4-a13e-340c-b78f-c5b5e44a5e10 | -7.44238 | -49.64605 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c5c44580-1673-311e-9452-88c409b48934 | -7.44177 | -49.64951 | 2024-10-23 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a9b160bf-bda2-35fb-86c6-21708ba6d08f | -7.13169 | -49.50992 | 2024-10-23 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 562560a8-2d2d-3a4c-8090-be3ea6d9e5f9 | -7.00921 | -49.34298 | 2024-10-23 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9b01ed-728f-3c3b-8637-b33147136361 | -7.00386 | -49.34205 | 2024-10-23 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a05e98f1-4372-3098-8151-aeaa8edf73e3 | -9.43427 | -48.88248 | 2024-10-23 04:00:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c714094f-63f0-32ca-8ef9-5133bd95fc31 | -8.73673 | -50.05923 | 2024-10-23 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc3adb8-4a47-36d6-b6b8-9eb2863cf377 | -8.73608 | -50.06277 | 2024-10-23 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8119486e-70a7-369c-92fe-a631cba7193c | -8.18273 | -49.75849 | 2024-10-23 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab6b3d86-b82c-3a00-8479-b3f6aab2ee0d | -8.1821 | -49.76201 | 2024-10-23 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| addb360b-2cf8-3f54-8364-24db103652a9 | -8.17946 | -49.75871 | 2024-10-23 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 600b3a23-666a-3be5-8533-1ab2e1ccdd7d | -8.17736 | -49.75741 | 2024-10-23 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8be93b3-2143-396f-8648-9fed74cb62c1 | -7.9736 | -49.69016 | 2024-10-23 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c59fc816-eacb-336c-9263-feec127a0e29 | -12.18802 | -54.25927 | 2024-10-23 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 866203d5-7df3-38db-bc8b-404302b1dfc5 | -12.1868 | -54.26508 | 2024-10-23 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f66a8897-3a0e-30d6-8811-ceea97ac47ea | -11.32957 | -54.35336 | 2024-10-23 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3b13f32-d7a2-315a-924e-b426c84082c1 | -11.32831 | -54.35946 | 2024-10-23 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f83cc86d-be1b-3f09-8c3c-b77f13e532bc | -11.31751 | -54.34352 | 2024-10-23 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 921aaab1-d262-35dc-81b4-04a7a8bb609f | -11.31609 | -54.34306 | 2024-10-23 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4ca63c3-865a-3386-935c-bd135f8a5990 | -11.31209 | -54.3357 | 2024-10-23 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57e2e164-1d4e-3a55-88b6-c42b42b15d23 | -11.31062 | -54.33525 | 2024-10-23 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7551ce39-566c-34f4-a405-69cd1893e3f1 | -14.61816 | -40.60308 | 2024-10-23 04:02:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc86818e-c1d7-3f1c-bf5f-79f83e33a8ac | -14.71349 | -40.73379 | 2024-10-23 04:02:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3add44ad-c9e9-37de-89c6-fd45351e37d2 | -14.39244 | -41.31805 | 2024-10-23 04:02:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 544b51e3-b6f4-39b1-b0de-1d17ad1db0a4 | -14.13329 | -41.69379 | 2024-10-23 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| feb4d622-a387-3a59-95d9-c3d822cad571 | -17.61143 | -42.55772 | 2024-10-23 04:02:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f0d6ca4-4016-384b-97c4-99dfcd5e35d1 | -17.38468 | -42.66019 | 2024-10-23 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fe9883a-a517-3544-bc54-b847db429ffb | -19.63478 | -42.36112 | 2024-10-23 04:02:00 | NOAA-20 | VARGEM ALEGRE | MINAS GERAIS | Brasil | 3170578 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00234819-757f-38e2-bba6-f17180cd63dd | -11.99648 | -43.08249 | 2024-10-23 04:02:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c5fb042-d975-30cc-939f-0c9dd3ce90cc | -11.99587 | -43.08626 | 2024-10-23 04:02:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50b84d45-830d-3233-93ea-01cacd99bfbe | -13.09773 | -43.36574 | 2024-10-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7381399-7054-367e-ae8c-b7c308630ded | -13.0858 | -42.27773 | 2024-10-23 04:02:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| beb9844c-7752-3dfe-9aef-1b94fa43af64 | -12.89897 | -43.18574 | 2024-10-23 04:02:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e83a1af6-daaa-3254-9bef-43adc77acdbf | -12.24738 | -42.94324 | 2024-10-23 04:02:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8712f091-0d46-3b1c-a569-6ff37ce166d8 | -13.66477 | -43.07343 | 2024-10-23 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9fd96455-4b75-36d7-baf2-1698433e6393 | -13.10114 | -43.36633 | 2024-10-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1147196a-4a09-328d-a0d7-201542e7ca16 | -13.10053 | -43.37011 | 2024-10-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3399603e-c5d1-3bb1-bc1d-89bf708755fc | -13.09712 | -43.36952 | 2024-10-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2b78733-2d78-3bab-b0ad-a0d488042c4c | -14.36428 | -43.60463 | 2024-10-23 04:02:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e21d936-ffa2-343a-b0df-7499275272d8 | -14.19851 | -42.31251 | 2024-10-23 04:02:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 99294206-68b2-3fd9-bddf-d1af81a87abe | -16.51424 | -43.59432 | 2024-10-23 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 185780ce-2b03-39b0-a5a2-02a04b8275c5 | -16.34734 | -43.6951 | 2024-10-23 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3a3aaed-d0c8-3bac-b945-0fc669a95a6e | -15.61329 | -42.89989 | 2024-10-23 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767a4bab-5b5a-31db-89ad-8238dc99f623 | -15.52157 | -43.13439 | 2024-10-23 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67287a7d-4a77-39b3-89c9-80adc57610c9 | -15.5196 | -43.10409 | 2024-10-23 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e4c7d6e-4d31-3c52-9a22-37fa42a514fd | -15.51823 | -43.13382 | 2024-10-23 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc1c04e1-5a49-36c1-b8de-a87a5c84b27f | -15.40701 | -43.08467 | 2024-10-23 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ed2bb66d-026d-345d-9de7-a6e972ecdf74 | -15.52098 | -43.13804 | 2024-10-23 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25d890f3-5884-3462-b9f9-35e0b6ae4191 | -18.00779 | -43.48133 | 2024-10-23 04:02:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af0da778-77ff-3417-a66b-783072563654 | -17.59476 | -43.19668 | 2024-10-23 04:02:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13222cb0-1304-3d4a-a97d-107dce37b5d2 | -17.09462 | -43.80522 | 2024-10-23 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebc39be1-f3a4-3f23-a9f9-4de3327d9adf | -16.68101 | -43.88383 | 2024-10-23 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b724a3f-6b3a-325c-8bd0-153baa4617f9 | -11.90881 | -44.17551 | 2024-10-23 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bf5b187-44e6-34bd-a689-0256f6ffce74 | -12.24838 | -43.42704 | 2024-10-23 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22372968-1108-3544-b26f-255a269ecdc7 | -12.15023 | -44.07826 | 2024-10-23 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a893fcf-5d55-313a-8965-da817ef2570c | -11.97082 | -44.6725 | 2024-10-23 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 057deb7f-0bbc-3483-9b17-85b34911dc97 | -11.94545 | -44.24149 | 2024-10-23 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3058437-561e-3671-b989-171b3921b0b3 | -11.8812 | -43.37908 | 2024-10-23 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5089e97c-c868-3bbf-b604-c1b3515037a4 | -11.88057 | -43.38295 | 2024-10-23 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aba0ef7e-1f58-3f74-b48a-d3b474cb8383 | -13.60453 | -43.9949 | 2024-10-23 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592ef708-9128-3e2e-8a4b-0cf218bc5b8f | -12.4554 | -43.74858 | 2024-10-23 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 448a5e7b-5834-312e-b813-12e7b7882243 | -13.60388 | -43.99883 | 2024-10-23 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af7ed586-b4e7-3cba-858d-60c8a738bc53 | -13.60106 | -43.99431 | 2024-10-23 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7e9964c-7634-3723-95f6-19d59f805e2b | -13.6004 | -43.99824 | 2024-10-23 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17121282-38e4-316c-af6b-4d233f89fff6 | -13.48803 | -44.36548 | 2024-10-23 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b76e032c-97b4-373b-8e46-59c16ddd4276 | -12.02802 | -47.79692 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b98e1ac6-9bc1-3cb2-8532-de249c28ab62 | -12.02357 | -47.79631 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3891c224-06d6-3fa2-953e-d8105d6bab5c | -11.8854 | -47.71166 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9982d24a-6c3d-37cf-a2e5-c2cc33bc5d34 | -11.88461 | -47.71608 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da65adb6-ead4-355a-a3c5-d72282ed3465 | -11.88101 | -47.71077 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78af5210-5a9f-3cd1-aa43-ef1ce0c532c9 | -11.6284 | -47.57956 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ed73ecca-03ea-3e5b-a241-7e940693b8a0 | -11.62761 | -47.58387 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ddca0e23-9f45-3556-9405-ba80a5f35e69 | -11.62402 | -47.57872 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c3ca074-8cdf-3eb1-95f4-35b93763eca6 | -11.62375 | -47.57996 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cf9761f4-ce8a-35f1-9c2e-ba2af584e6d4 | -11.62323 | -47.58302 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b780406-0efa-3e89-979c-060dc6aa0b3f | -11.61937 | -47.57913 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71281dfb-134b-342c-be8f-2dd1211c558b | -11.61885 | -47.5822 | 2024-10-23 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2dd59258-5765-3b89-b918-e4ccd654d74a | -12.53896 | -46.80494 | 2024-10-23 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e2babad-582d-36b3-94cf-4f450df8ed5d | -12.43325 | -47.19872 | 2024-10-23 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e66342a-63f4-3667-a152-ac23b8c4a153 | -12.43255 | -47.20274 | 2024-10-23 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0d6b22e6-ac90-3052-932d-2e8b1c1f31ad | -11.94547 | -48.05894 | 2024-10-23 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae7a5321-5407-3343-8f71-3387a41cedba | -11.94465 | -48.06351 | 2024-10-23 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acbe8a60-bfe7-39af-932b-b43685811be1 | -11.94099 | -48.05801 | 2024-10-23 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 949456c0-41e4-3052-b253-7cf143bcd475 | -11.5912 | -48.52637 | 2024-10-23 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ba244a7-57f5-388c-a190-564a35c19ba8 | -11.56954 | -48.72321 | 2024-10-23 04:02:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd89b756-5330-3bcd-873c-e06a6ce6812a | -11.56482 | -48.72222 | 2024-10-23 04:02:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10e1f8c9-efd7-3c0b-ada6-a156d6b0330b | -11.25211 | -48.00639 | 2024-10-23 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19692a85-209d-3e4e-9a35-0240b689f3d9 | -11.12145 | -48.10211 | 2024-10-23 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
