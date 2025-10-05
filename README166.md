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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d490c2b-5b7f-3f53-9f8b-d0e1a6879b50 | -8.1702 | -44.1377 | 2025-10-05 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ab718a57-a27a-326b-845f-d30d646ca1f9 | -7.8121 | -47.3759 | 2025-10-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 88f28604-39f9-38a4-88f0-cea770b92aa7 | -9.9024 | -50.1914 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 155b26a9-154a-3bd6-a8a0-67c114078915 | -5.852 | -42.8608 | 2025-10-05 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| a978604c-b846-37a2-9eed-43288b85b3f7 | -5.7762 | -42.9372 | 2025-10-05 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 4cc7369a-b4df-3d76-8e50-08a2189c6f64 | -18.1963 | -53.3853 | 2025-10-05 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5e69418d-42e7-3f85-b757-35ef72f6bc2a | -11.1573 | -47.1712 | 2025-10-05 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 94ccbd3f-9f98-392d-95e3-de90c0fcd50b | -10.1943 | -45.5339 | 2025-10-05 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1d80348d-d642-3e52-a25a-27b3864f3780 | -12.3157 | -55.1212 | 2025-10-05 14:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ea564bf2-ee02-38f1-a64a-7e74c24083bf | -16.0021 | -50.9238 | 2025-10-05 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| bb97fc17-3f2a-3526-ab4e-09fbbe831adf | -17.9408 | -57.5928 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| ffd200b4-6125-363c-afe1-cf4b14608d0c | -12.3154 | -55.1416 | 2025-10-05 14:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 4b6fa273-bb83-3272-ab98-857fbc2523ef | -1.2085 | -49.1051 | 2025-10-05 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f4008ae6-e213-3c8e-b43c-ecd676f937c5 | -6.6976 | -42.8354 | 2025-10-05 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 48808b73-6e74-336e-b8b3-434819478157 | -11.8635 | -44.938 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 5c5e4ae3-8469-3711-88ff-af75ce19802d | -7.646 | -45.4489 | 2025-10-05 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| e695de73-7993-36e7-af06-0e75a015a553 | -8.5596 | -47.6813 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6a04fc03-6449-3ea7-8eae-7718717afeaa | -8.6911 | -47.6906 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| f2c221cb-f087-36c5-abfd-40f3924e89cf | -6.3982 | -42.6972 | 2025-10-05 14:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 7c9ce6de-f5a3-3de3-b498-a8a4488569b4 | -7.6622 | -47.367 | 2025-10-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1abe629d-9fb1-301f-81dc-494438b5b578 | -6.1536 | -44.6675 | 2025-10-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 198.4 |
| f6d51462-0fc7-37cd-85c0-e8857faae404 | -6.2596 | -45.341 | 2025-10-05 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3b7f4c19-525e-3982-870b-1da24df4b925 | -16.0774 | -51.0642 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 97aae279-b547-3bee-9ef7-ecd88935c903 | -7.7743 | -42.6103 | 2025-10-05 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 247.7 |
| 02e914db-7989-39c1-bf39-dd178485185f | -5.8761 | -44.2994 | 2025-10-05 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d2c45d94-abfb-3ad0-b889-20fd7263195a | -15.6015 | -52.5102 | 2025-10-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 42aa8914-b94a-3614-bbc9-3a7d8afe4e7f | -6.4134 | -43.0489 | 2025-10-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9fb15fd8-0b44-31fb-9266-6179337f59ad | -5.9397 | -43.5087 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5637f6f9-85d3-3693-b431-54e49cc8e2b8 | -7.7306 | -46.2737 | 2025-10-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 88c925e0-2491-3cc3-a3e9-ca216c848d8b | -15.582 | -52.5129 | 2025-10-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 161.7 |
| d0859045-5840-352a-b028-0154fb83cd0a | -11.1455 | -47.9275 | 2025-10-05 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e1d07d32-b72c-3a8c-a668-8af670e4a503 | -7.348 | -45.227 | 2025-10-05 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| aab31ef3-4fad-3a01-9098-e4648b73205c | -10.4557 | -48.3827 | 2025-10-05 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 7c715112-1acd-3574-97b5-1caebcdc4e47 | -6.2156 | -44.0658 | 2025-10-05 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 91d5beff-52bc-3097-8f2f-1c2f22d1e4b4 | -18.1968 | -53.3638 | 2025-10-05 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 3179db5c-61e8-3a46-b7cb-2210fdc1e630 | -7.4672 | -43.0438 | 2025-10-05 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| ae2e05d5-8e14-303c-bad6-1a55c644c786 | -16.0016 | -50.9456 | 2025-10-05 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d9e860b7-2e49-354d-a759-c9300a0548b9 | -7.448 | -38.5672 | 2025-10-05 14:20:00 | GOES-19 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 121.5 |
| cb7da2b1-52bc-3fbd-afb1-6b4116852e46 | -13.7277 | -51.3337 | 2025-10-05 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f1f31661-6f38-32de-8965-728a3ec1994d | -6.1353 | -44.6232 | 2025-10-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9069b5ac-8bb8-3540-846e-d28d0b76eed1 | -14.3348 | -47.6981 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 32d8f571-4708-311b-8a11-e1e781b88fc9 | -8.5405 | -47.7051 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| aceda3d7-d34e-399c-be9a-b081b64cfb75 | -17.9404 | -57.6134 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| cedcbf39-7a2b-33e4-b7eb-aabbcc716769 | -10.8093 | -48.8229 | 2025-10-05 14:20:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 2556cf6c-83cb-3ec5-be72-53a3e4dfdeed | -10.0504 | -50.4113 | 2025-10-05 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 665594c7-1012-3d4d-b7e7-3f27fcc59134 | -7.0372 | -42.7563 | 2025-10-05 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| e1a1813e-3701-3875-a321-f3743da77ae3 | -1.2085 | -49.0838 | 2025-10-05 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 73926065-6433-37ae-9828-48fba8d02407 | -11.0975 | -49.8729 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f709378d-3ad9-32bd-b2f3-b231b984802d | -6.6129 | -43.7317 | 2025-10-05 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| cab17f38-0a0f-3fb2-be16-583d2fd440c7 | -16.097 | -51.0611 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ccf5566b-1fdb-33d9-a9f7-1957f956b58c | -11.0978 | -49.8513 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| fe8b0ea0-f46f-3764-86e4-ae4a253b4239 | -14.5561 | -52.4601 | 2025-10-05 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 47431450-84ac-36a8-8e21-79adf851447b | -11.0316 | -46.6946 | 2025-10-05 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 144e31b2-3183-3151-bb81-d1642d3251a0 | -11.1172 | -49.8276 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 97aaaec5-dea5-3f10-af85-7f7c69775b67 | -9.2976 | -45.98 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 611e9dff-4a81-3c00-8983-eddc51458320 | -10.1576 | -45.4473 | 2025-10-05 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 6bd5b7d5-7cb8-33db-a559-4fc2c68e0f84 | -3.8945 | -41.5938 | 2025-10-05 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| f3961a99-09cb-3cf3-a3fa-784a0e254257 | -16.3627 | -51.4752 | 2025-10-05 14:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 6e7c65fa-fe14-361f-a35f-c58bf6b54de3 | -5.8067 | -45.8021 | 2025-10-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 259.4 |
| a66c39d4-67c1-3661-9702-ab49f1bcaac0 | -11.8234 | -45.0364 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 08fc1841-8e62-3e56-9089-aa259052ad21 | -14.1611 | -53.0377 | 2025-10-05 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 474eb60c-f67f-382e-832a-23e3a49ca6d7 | -5.4962 | -42.7942 | 2025-10-05 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 34e4d54c-b9b8-326b-b33a-d251b1bb0b52 | -10.1497 | -45.9709 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 342.4 |
| 6f9be902-ff25-3b31-b722-30bd30712cec | -7.7933 | -47.3776 | 2025-10-05 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 79f3548c-0818-3306-b731-c9be45c98470 | -5.837 | -42.4609 | 2025-10-05 14:30:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| ab4a360f-d7d9-3da7-8c04-a9fe6b7916be | -15.6015 | -52.5102 | 2025-10-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 241.5 |
| da6eb9ef-4a7a-34d2-a23c-80c68dc63d78 | -16.0805 | -50.9116 | 2025-10-05 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| fe35366b-42c5-365d-bb19-1fda0bc4bb82 | -5.8182 | -42.4624 | 2025-10-05 14:30:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 08ab69fe-c8e4-3817-bc24-317a74fa1b6a | -8.8618 | -46.0949 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4abe21c9-7fd6-3ba6-affe-eebbaa856609 | -6.2515 | -44.2242 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f3fd85f9-b214-3048-8253-a7bb9757690b | -9.0966 | -49.9263 | 2025-10-05 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| eb3f3e85-0859-3d7f-abd2-c8e9f2616e3e | -11.2429 | -47.7827 | 2025-10-05 14:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 33d5a6d9-336b-3b47-928a-11a83c141d96 | -7.4464 | -46.5223 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 86c3b5f1-f1fc-3f95-be38-f87e2ac1b061 | -15.2015 | -56.8231 | 2025-10-05 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5cd89a3d-f0fa-387d-ad24-5d5e6d14a42e | -6.1966 | -44.0904 | 2025-10-05 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3c46f1a4-3c56-3aa1-ac9c-60a954eca3b5 | -10.3907 | -50.3557 | 2025-10-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| c375e256-162d-3eb8-8ef5-f1ea212bb4e7 | -5.4734 | -43.2646 | 2025-10-05 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6be6331d-5c7d-3784-922c-0a1835f0152a | -11.4414 | -43.9057 | 2025-10-05 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| a3bbd967-8998-3437-8381-05aabdc55c2b | -7.0558 | -42.7782 | 2025-10-05 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 0b3c4a20-f982-3cef-8cb4-769657d74c50 | -6.0618 | -42.5133 | 2025-10-05 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 68cb65f0-4ae7-3b9c-b287-c7d959aa594b | -7.7749 | -42.5628 | 2025-10-05 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| b5822704-c8fa-3b16-8a8c-d5878858d1e6 | -5.8105 | -43.2858 | 2025-10-05 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ca69e382-78c6-3fc8-bf29-d3ab75646143 | -6.3341 | -41.6309 | 2025-10-05 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| cca67d6b-18d0-3a3b-9157-993ef6269d91 | -6.4134 | -43.0489 | 2025-10-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 163abdde-0529-356d-82fd-2dedc62987c2 | -15.582 | -52.5129 | 2025-10-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 377d8f50-d5a5-314e-a801-72d9a343d1c9 | -6.0616 | -42.537 | 2025-10-05 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| c080f310-8ce7-3370-bb06-b2e88a1b8cf8 | -7.7123 | -46.2307 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d1f2f771-4489-346a-9a56-d41af7902b6d | -17.8417 | -57.6254 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 9d779ec0-3413-3c3b-bf0f-cd44376f1099 | -11.5091 | -54.4824 | 2025-10-05 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e5d76afb-40c2-3713-ab51-5f3f89843abb | -9.2627 | -51.8117 | 2025-10-05 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 4948e10f-206a-3e52-b776-576bcea5bc57 | -5.5536 | -42.6721 | 2025-10-05 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 084eb1bb-8691-39f2-bea8-25e43c623652 | -6.2153 | -44.0889 | 2025-10-05 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 59fa6c1a-9657-3eb0-a21d-0e2d018b19c9 | -13.7277 | -51.3337 | 2025-10-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 66c37b61-c47f-355e-9eaa-26fb9dac7ba2 | -17.8614 | -57.623 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 0e4ec1b8-f46c-351e-affe-4cfd854eb4bd | -6.6069 | -44.3098 | 2025-10-05 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 7c6f2277-6ca9-368a-85da-47da380edba5 | -12.2967 | -55.123 | 2025-10-05 14:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a533c7ee-708d-393b-9e89-14d1a0129f16 | -10.7677 | -45.3458 | 2025-10-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c586d1e9-8f2b-3163-931c-3d6deba277ba | -10.1946 | -45.5111 | 2025-10-05 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 153c5469-5a3c-3713-afb0-7dcb97c3ac67 | -7.8121 | -47.3759 | 2025-10-05 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 92871c68-066e-3534-8667-9cdd79bc7993 | -5.9266 | -42.9018 | 2025-10-05 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |


[Clique aqui para ver as próximas entradas](README167.md)
