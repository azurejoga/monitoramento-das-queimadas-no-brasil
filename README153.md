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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71461fd9-a5cb-3fa3-ba3d-9d49330cd013 | 1.9977 | -50.8605 | 2026-09-22 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 239b02f4-9570-332d-84e7-0fd1564f80ba | -3.1514 | -58.644 | 2026-09-22 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8c4b8717-b535-3009-8c32-83e5aa4bc9ac | -3.1096 | -60.6892 | 2026-09-22 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fb755fb0-9e20-362b-aa42-2eab054adcab | -6.3251 | -55.8252 | 2026-09-22 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a4b8b520-841d-3472-8dcf-a15d43bea62e | -3.2955 | -59.4476 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e6237c79-441f-345b-9397-84a722563f82 | 1.5099 | -56.0426 | 2026-09-22 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a414fd5e-1d03-39af-bbff-eea167ed2b45 | -6.2024 | -47.5245 | 2026-09-22 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| a4a38634-a3e3-3857-988a-ac55354d4fca | -3.7707 | -59.5909 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bffb804e-ab65-3036-a30d-add380a37303 | -3.1278 | -60.6889 | 2026-09-22 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 440e0c3b-e143-323d-96af-9e10a3f31334 | -5.9333 | -53.5362 | 2026-09-22 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 65155473-cc88-343c-820b-bd093e271381 | -5.4179 | -60.2166 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 65b92cde-7594-3e22-825a-7925ed9c4000 | -3.6632 | -58.8643 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 11873c41-40ca-35c7-872b-35bd1f4c64fc | -2.5687 | -57.5135 | 2026-09-22 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0ea84b92-f6a4-3127-9179-3c37b7e29284 | -3.4186 | -61.2895 | 2026-09-22 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 410ca43e-0bc1-3ed5-9ace-f3791b9d5997 | -3.3311 | -59.8101 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e9c31433-5756-3bf5-b709-5d707f29d2b9 | -2.4023 | -58.2908 | 2026-09-22 15:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 003c2121-24b1-318f-974b-28b6541819ab | -11.5116 | -45.3581 | 2026-09-22 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0fc073c9-af85-3ce8-a7e2-7653201497a8 | -6.3567 | -59.9559 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4fa50117-6bce-3234-a7ac-37858fa31fa3 | -2.9723 | -57.214 | 2026-09-22 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9b1989b5-5fe5-3c60-adc4-65ceb966f61d | -5.8411 | -53.5002 | 2026-09-22 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3048113c-ab2c-309b-8843-d24906ec6084 | -3.7313 | -60.5638 | 2026-09-22 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 18ddfd8e-7a6a-3361-bb9e-de150e9b5403 | -3.0345 | -61.5977 | 2026-09-22 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5db894ce-77eb-302e-bb0a-338c2eb7ef3a | -10.7997 | -50.8668 | 2026-09-22 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 86c820f1-770e-3ade-b584-f3e9768e0b89 | -6.4302 | -59.9724 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 0961e00d-4ecc-3fb6-809e-391c9a6a6039 | 1.968 | -55.8989 | 2026-09-22 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4186c819-ce6f-34e6-8e81-5f034d876116 | -3.0616 | -58.0086 | 2026-09-22 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 669b2e68-0cad-3817-aeca-1763308d357c | -8.7706 | -45.8567 | 2026-09-22 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ced9b013-e446-3b06-b5bf-874e56d0e0f2 | 1.1503 | -50.998 | 2026-09-22 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 469607a7-69a5-345f-915a-3d2644187a20 | -3.1901 | -57.8704 | 2026-09-22 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bdaf2a60-4c4e-310e-8571-605ee90067e5 | -6.3199 | -59.9381 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1e0f5df7-430b-34a1-8917-aa9d2c52a573 | -2.9723 | -57.1945 | 2026-09-22 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7c92f079-ebb5-3405-b5ea-679c18dcb0f0 | -1.4302 | -48.9529 | 2026-09-22 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7d237b23-d70e-30d3-812e-05e6afba9643 | -3.3493 | -59.8288 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4062861a-6746-3cb5-ae4d-774104d9b3d3 | -3.3358 | -58.1384 | 2026-09-22 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6bf16f61-d9f3-3021-bada-ddb5f0e9e7ac | -3.6032 | -60.5853 | 2026-09-22 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 2cf1abaf-099e-3a9e-80e3-74308cee0234 | 2.4027 | -50.9769 | 2026-09-22 15:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9e9f7c0e-3990-3e95-bb65-2fa7f6616609 | -3.6997 | -58.9019 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7df86f00-51f3-3104-987f-479dab567ef7 | -10.6875 | -50.7722 | 2026-09-22 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 1900553d-9721-36ea-a2e3-8edac42cb59a | -3.3001 | -57.8487 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3fef6588-7dc1-347c-8b73-4fa73ed2903d | -6.8985 | -41.6976 | 2026-09-22 15:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 820.7 |
| 3682dad2-c4de-3a4a-a7c8-755795e5eace | -3.6264 | -58.9228 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 3848de6f-24b6-32cb-ba61-75074f4c09ba | -6.6782 | -58.4584 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d1b09886-3cd9-3b50-8767-300260ec91d3 | -10.8941 | -50.8782 | 2026-09-22 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0ba6f3e2-9c3e-3fb7-acf9-616fb1a38fa7 | -5.8408 | -53.5408 | 2026-09-22 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0aa73f0c-4844-3c60-bace-4925b03ba544 | -7.6079 | -57.616 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e6f7104e-bfe9-3bf5-9db3-6033a99750e6 | -6.1838 | -47.5258 | 2026-09-22 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d5d8fa50-cad2-31a4-bd38-a63055b031bd | -3.2818 | -57.8491 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| df3e0382-926f-3d23-94cb-fea66acaae78 | -3.0719 | -61.1819 | 2026-09-22 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e46c80c5-d89b-3944-9131-f8b34a33b676 | -3.1851 | -59.6982 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b79e2f08-c5e4-34fb-8d37-17d6ec8e961d | -3.4974 | -59.1944 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ab4f31aa-4307-3652-a554-4c1b0f90f3bc | -5.4363 | -60.2161 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 94215a5a-909e-3867-acaa-dc0eab3036d2 | 3.9168 | -59.7023 | 2026-09-22 15:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 897364ed-6fd3-3d09-aae9-7ac6bf8f3000 | 1.547 | -55.7466 | 2026-09-22 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1d84144f-50ce-35cd-8769-2231bd01c855 | -2.9525 | -57.72 | 2026-09-22 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4cd4d39d-dc8b-37fa-8189-1511fa52aede | -3.4975 | -59.1752 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f1ab641d-d504-3d5a-984e-f796cc9ad1c4 | -6.1653 | -47.5052 | 2026-09-22 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 83e900d0-011b-3866-8665-e22982706758 | -6.8468 | -55.2617 | 2026-09-22 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6023e5ed-93cf-3140-8e68-3b572e9de00e | -2.4206 | -58.2712 | 2026-09-22 15:40:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4070c995-fb4d-30dd-ab93-64f610f4b3da | -3.4003 | -61.2898 | 2026-09-22 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 71fdea56-bc83-371d-a769-b805a4e1ea54 | -3.7364 | -58.8626 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d3d48b0a-62c2-3d35-ba91-e2925dd960db | 4.1314 | -61.3134 | 2026-09-22 15:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b2ad6ab6-5445-3722-955a-1c7dea94e26b | -9.788 | -46.0819 | 2026-09-22 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a4da794d-786f-38e1-807c-60ae381d2385 | -10.2446 | -49.986 | 2026-09-22 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7558a54b-a840-3c8e-af97-8adf77e14356 | -1.0244 | -48.8087 | 2026-09-22 15:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a907fa5d-f110-3add-a171-ddd51f8ce35d | -5.4179 | -60.2166 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| d071e01a-adbd-34a8-a60a-da42a7cf311a | -3.1095 | -60.7081 | 2026-09-22 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| fcf27430-8518-3982-9359-f15c9f0e46cc | -10.6875 | -50.7722 | 2026-09-22 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5ee79c20-1861-36ed-b1a3-a7c6ee8398d3 | -1.4302 | -48.9529 | 2026-09-22 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9b9dad35-788c-3548-be7e-a62c9424d21f | -6.9849 | -59.663 | 2026-09-22 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 3f0391e2-c7df-35a4-9d5d-30bee8ba78d6 | -3.6032 | -60.5853 | 2026-09-22 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 86ad4f05-2fe3-3301-9d8f-2cfcb539bcc5 | -3.3359 | -58.1191 | 2026-09-22 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d26bc690-eb7e-3c92-9eec-ec4149ddae4d | -11.4527 | -50.2409 | 2026-09-22 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1faf6c1d-7a95-3471-a093-832fa623d1d3 | -6.7485 | -59.0557 | 2026-09-22 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 073f5313-fa70-302f-8739-262b6711f0a1 | -6.6782 | -58.4584 | 2026-09-22 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| a6552818-4440-3954-8bf1-b57d024bf0a5 | -3.6997 | -58.9019 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4bc32ecb-b82a-36ba-a0c2-79d44242e093 | -3.44 | -60.094 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 36b4590d-c586-3674-9d30-c285beb5f9b8 | -3.1357 | -57.697 | 2026-09-22 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3079719a-ddef-3192-829f-2b04814f2f2c | -10.3916 | -50.2916 | 2026-09-22 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e7608997-abc1-3ee8-96ef-6cd686c73338 | -10.8941 | -50.8782 | 2026-09-22 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3a158f39-0077-38b3-9b35-25a4f8125d99 | 1.9497 | -55.8992 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6bbd3543-01a8-31bf-ace7-7327e0ab18d5 | -2.9997 | -60.8047 | 2026-09-22 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| dd1da294-2c1a-37bb-b9d4-49790fc3f9c8 | -3.6632 | -58.8643 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 465c66b3-cab6-3396-83e5-81d5a2390c3a | -3.6996 | -58.9404 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5a0bbba9-12cb-3819-8340-13dbb020f656 | -6.161 | -62.5263 | 2026-09-22 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| dfe1cb69-2568-3116-9837-a68c3ab45c3a | -3.0717 | -61.2575 | 2026-09-22 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| cdcbcb46-013e-31ee-8505-2340d30e3e8e | -3.4635 | -58.3096 | 2026-09-22 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 23f356c0-dad6-3c77-a62f-81a71f71bb06 | -3.6448 | -58.9031 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 72054a4d-985c-30bf-a123-081d031025cf | -6.1651 | -47.5271 | 2026-09-22 15:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ce5ef70b-1f38-3094-8c16-0781d00a93c4 | -7.9172 | -61.329 | 2026-09-22 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b4ce2d49-c122-3859-a869-3f0f3c00060f | -3.713 | -60.5452 | 2026-09-22 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 724b36a5-054d-3946-8925-d7c83da7f4ad | -5.8411 | -53.5002 | 2026-09-22 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 71ce0552-e0b7-3a9f-8be5-00cc37523141 | -2.9326 | -58.3397 | 2026-09-22 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a3e879ab-3c7b-3060-bd7f-66c0abb1f11b | -11.3976 | -44.2167 | 2026-09-22 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 251.3 |
| a5a96fc7-e46e-358a-830f-73076ab86f91 | -10.7816 | -50.805 | 2026-09-22 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| efd56302-a86f-359b-9e03-d9a911b83a9c | -3.331 | -59.8292 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| cd5a4cc9-edd1-39b3-8ad4-761dd79d3474 | -3.5528 | -59.0397 | 2026-09-22 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4a441394-4cc2-3de8-84e6-b332404b99df | -3.6447 | -58.9224 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 0eacf613-100b-31cb-87f3-0e1d81e33b91 | -3.3358 | -58.1384 | 2026-09-22 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 45c02f8c-7c46-3f17-8944-4072bcd3f89e | -6.4671 | -59.9711 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 9a7bcac8-94e6-358f-b8e4-0fc1f4404dda | -3.1358 | -57.6775 | 2026-09-22 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |


[Clique aqui para ver as próximas entradas](README154.md)
