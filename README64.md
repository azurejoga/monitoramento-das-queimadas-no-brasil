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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 192237b6-33b0-399d-9a18-858855034b32 | 0.61253 | -51.77261 | 2024-11-17 05:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| de0f3e3b-3be9-38b1-a677-ab3641a1e696 | -2.41103 | -54.62354 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b39927f-52e6-31d4-9699-e93826a933e3 | -2.37127 | -54.63678 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c9806c6-dc71-3889-a130-77fb22bf9b9e | -2.23465 | -53.60836 | 2024-11-17 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5887f96-29a2-30ea-98ce-92065193da1b | -3.03382 | -54.10051 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29aa2e77-e3b2-3951-9de1-0a8b178f30de | 1.05871 | -60.59995 | 2024-11-17 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef0384dd-76c2-39c5-befb-090872622553 | 0.61951 | -51.77134 | 2024-11-17 05:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0d761a8f-ce34-3929-9cc5-98b78cb54621 | 0.61495 | -51.77106 | 2024-11-17 05:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 261dbc43-a8a2-35bd-84a5-4cb3212e9710 | -1.29259 | -51.73762 | 2024-11-17 05:46:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f734b778-aa65-3b27-8a4c-ae7a8b125260 | -2.99108 | -52.59881 | 2024-11-17 05:46:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 965517a2-0db3-3b8c-bdf7-3a7139feb31d | -3.03458 | -54.09864 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17e89f5c-89e5-3d9b-bd72-ee482f3d4d8a | 1.05947 | -60.60484 | 2024-11-17 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce9299f-2e15-3457-95e6-93dc20a43ff6 | -0.11089 | -51.59853 | 2024-11-17 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63e55f7f-bf55-3a70-ab22-23f84685aac5 | -3.48657 | -53.9943 | 2024-11-17 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e9f6aa0-5750-313b-bc33-18602b07379b | 1.05949 | -60.60294 | 2024-11-17 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb36ad1-7384-3a8e-bb22-8aec6527dab3 | -1.14193 | -51.69333 | 2024-11-17 05:46:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 92d9012e-9ad1-3a48-8786-631a4e9f295c | -1.29978 | -51.73878 | 2024-11-17 05:46:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0320a66a-e45e-3104-837d-0194685763d2 | -2.22814 | -53.60722 | 2024-11-17 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d5f3220-0629-3476-9634-1157bb711ca3 | -1.62884 | -53.28525 | 2024-11-17 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2603a116-7a4c-3411-941b-e31e3f77ed45 | -2.2338 | -53.61395 | 2024-11-17 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4b5c613-73ab-3758-b800-b9997d380d19 | -3.74473 | -54.71924 | 2024-11-17 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 020c085b-f03b-36e6-bf6f-331b550fdd52 | -2.99014 | -52.60523 | 2024-11-17 05:46:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77c39d0e-973d-3032-a441-844d24156506 | -2.33202 | -53.5726 | 2024-11-17 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b738e902-325f-3bdd-9f12-5266fd186cac | -3.48603 | -53.99191 | 2024-11-17 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f187ef2-e123-398b-a8e6-f1c909db6c54 | -3.75096 | -54.72025 | 2024-11-17 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68a9e360-1d54-31f1-88b7-cfcee6349c37 | -0.10373 | -51.59749 | 2024-11-17 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67ea079e-17b2-37b0-90df-fe9abed1b916 | -3.48678 | -53.98665 | 2024-11-17 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b75b04c0-4adf-3a22-8104-4b2ff99836d5 | -3.0274 | -54.09959 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f58466d-2f4b-39a0-b1e3-7aaa11fa673e | -1.63784 | -52.67015 | 2024-11-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9375ce26-9d05-30fb-a501-0f08adcada84 | 0.61369 | -51.77959 | 2024-11-17 05:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 23.8 |
| c23e1277-074b-3cad-a96d-6058e69186c4 | -10.94483 | -59.10316 | 2024-11-17 05:48:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f5d6b510-6c1c-38c5-8c7e-4b4968cff59e | -10.95 | -59.10386 | 2024-11-17 05:48:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c903596-7f36-33c3-b030-28106ee66f4c | -4.5616 | -47.9925 | 2024-11-17 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 01883367-fe57-3866-8864-cf68c9e9a1ad | -2.8615 | -46.7086 | 2024-11-17 05:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 96b7382a-295b-3027-a41f-84aaa3b15d2f | -3.5309 | -50.2547 | 2024-11-17 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 7089138d-1683-3f1c-8101-d9d67c7c4f35 | -2.6322 | -48.5634 | 2024-11-17 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4b09ef54-0cf1-374e-a8d8-67034f654b1b | -2.6137 | -48.5639 | 2024-11-17 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c11b6976-a54f-3157-86e0-41cf3b03aa42 | -2.8614 | -46.7306 | 2024-11-17 05:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| af1c01ef-bba2-3d48-bf21-70338420c661 | -4.5614 | -48.0141 | 2024-11-17 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| c49e036b-f679-3783-bfa6-75aa7d111a81 | 0.6159 | -51.7676 | 2024-11-17 05:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4030fac0-41fc-3c36-ba51-9ac45e28d992 | -15.05485 | -58.23164 | 2024-11-17 05:50:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0ff9e65d-0991-343e-96a5-5fe62e5bb50f | -15.04906 | -58.23092 | 2024-11-17 05:50:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9666a2a2-8c20-39da-a36e-de058f966a63 | -12.55903 | -57.82462 | 2024-11-17 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49a32f9c-04b6-3477-8b4a-4f11b44978bd | -12.55289 | -57.77792 | 2024-11-17 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74e50a26-da70-386d-bd19-907609471632 | -15.91816 | -59.80386 | 2024-11-17 05:50:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 013a7c76-97ab-3380-b9d7-4d861e5095f6 | -19.49258 | -56.61144 | 2024-11-17 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 24cc2766-b351-3537-b556-3dfbfd21b170 | -17.61596 | -57.55428 | 2024-11-17 05:50:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f3aeaf77-fe2c-3db0-86c6-e359e0907b6c | -19.48586 | -56.61077 | 2024-11-17 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 85698d5f-4ac6-3af6-bdd2-8b9f8aa4922e | -12.39496 | -57.52631 | 2024-11-17 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebbdb827-d0ec-3926-8f83-09f14bc3e64f | -14.54611 | -59.95991 | 2024-11-17 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21207661-e4eb-3366-b20c-61ee3993728f | -15.92266 | -59.8113 | 2024-11-17 05:50:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7879d683-c556-385c-9012-b5f46a604d13 | -15.92795 | -59.81194 | 2024-11-17 05:50:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c7ea7b-483d-38d7-a270-15a5c71ad22d | -12.39545 | -57.52219 | 2024-11-17 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 892a8362-a431-3cb8-a213-40ca7dd948bc | -14.54647 | -59.95691 | 2024-11-17 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 755b433d-cff9-3453-b3ff-516c141a70e7 | -15.92228 | -59.81464 | 2024-11-17 05:50:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c591cfeb-007f-3c5f-b290-9621e02c62f4 | -12.55338 | -57.77385 | 2024-11-17 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 050c5b02-5127-311b-97e0-2dbe08bb32e0 | -15.91663 | -59.81723 | 2024-11-17 05:50:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcf6f573-f819-3ff2-a6db-3b372c05a968 | -12.39009 | -57.51732 | 2024-11-17 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fa93bfd-d4f7-3686-b821-89c7db55c231 | -12.5648 | -57.82526 | 2024-11-17 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b33334c3-6799-3543-bc21-2e7b0264b92f | -19.49206 | -56.61755 | 2024-11-17 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 76fb1892-1321-3830-9610-c2b7914972a7 | -12.39595 | -57.51802 | 2024-11-17 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f5202c4-41a1-3b4a-b0d8-3c0c11186d61 | -2.90008 | -53.05168 | 2024-11-17 05:57:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b654ad4-1be1-3b44-90f8-c59ab55bc343 | -0.31504 | -51.50122 | 2024-11-17 05:57:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c0acaaa6-fdcb-3f1a-a1bf-19f8865b6c8c | -2.606 | -51.79362 | 2024-11-17 05:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1784ef0d-039f-30e1-9d56-5625cf155840 | 0.62034 | -51.77548 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 93493b4c-b29f-37c4-b18b-7a7079907b2d | -0.94039 | -51.63552 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de1cd8cf-9a71-353c-a6e4-fcf680ace3da | -1.2084 | -51.76262 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4999d44d-8cfa-3725-8a5f-51798de1f4d3 | -1.20696 | -51.77241 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| db2d10b8-a01a-344f-a8de-9a99981688fc | -2.33361 | -53.56843 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1afab3c-1810-3523-93ee-b12e5b4a95a8 | -3.58215 | -50.51952 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 6be84864-567c-374d-bae9-c81f5887ff12 | -1.53184 | -53.55772 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d2d77f6-b3d1-3ab8-8a03-5d9da6d118d2 | -4.57982 | -48.01582 | 2024-11-17 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 08d8c834-9b7b-33ab-8358-5e777c27139f | -1.14575 | -51.68771 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 64cf1787-ac9c-3c22-aabd-2fa2d8253642 | -4.03956 | -50.88195 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f23c64f6-ecd9-3e76-87ec-0e7cac0ed76c | -2.99465 | -52.60406 | 2024-11-17 05:57:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 41dfe4ac-c73e-32b0-9bf4-f6e3e46886f0 | -4.55888 | -47.98549 | 2024-11-17 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c3b852c1-602f-3b43-be21-083d9c0dda58 | -2.60697 | -47.53583 | 2024-11-17 05:57:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b56284d1-000b-3b54-9c2f-b55664ca160f | -2.09685 | -48.26053 | 2024-11-17 05:57:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8900cc71-6b23-3c23-8354-528412851407 | -2.86093 | -46.70641 | 2024-11-17 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6dccd837-8ba6-3a83-9a68-146559f76d08 | -2.86679 | -46.71246 | 2024-11-17 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 582ca40b-5e01-38d5-aaf5-d40598848864 | -1.29912 | -51.96075 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 964a137f-0f05-386f-a2f9-8deec11df332 | -1.2899 | -51.95942 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b927e545-82b9-3bc3-b9c0-d6bd14cb54ca | -4.57903 | -48.02898 | 2024-11-17 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 6fb1d0e6-46e4-3ede-975a-89b884960c78 | -2.22669 | -53.60941 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d597d29-2e10-3b13-8796-1694959fe0c0 | -1.62744 | -53.29006 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7999b89c-4b8f-3dbc-8546-31cf3193c773 | 0.41202 | -50.8646 | 2024-11-17 05:57:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a0ea532-c874-3370-ba79-0f19cbe7d478 | -2.15435 | -46.92369 | 2024-11-17 05:57:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| be697506-76d1-33a4-9978-a6170492f5ba | -2.33229 | -53.57724 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39fdc2a3-d586-3a1c-8aea-766d28dd3f06 | -2.15298 | -50.69782 | 2024-11-17 05:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5aae969a-d5fc-3bf8-a328-8070e2ac7c70 | -1.37974 | -51.08619 | 2024-11-17 05:57:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd2524a9-d96f-3426-be71-c8b8bddfb14d | -0.10665 | -51.59849 | 2024-11-17 05:57:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7840ed0c-634a-3b88-9838-7b2709866b2a | -0.92324 | -51.64655 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe00b8b3-dc55-3405-97b8-b68ff4a1ebcc | -2.99605 | -52.59468 | 2024-11-17 05:57:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c0e44b2-635e-377e-a11f-81cc09c60f31 | -1.10964 | -51.93077 | 2024-11-17 05:57:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f6ef716-5d52-34d0-9b64-b5c9046bea5d | -4.58188 | -48.00918 | 2024-11-17 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6808c930-d46f-3c30-842a-fd9ff75c1253 | -1.29512 | -51.73177 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 12db4dde-6d3e-39e7-873f-77e6627c9a36 | -4.81206 | -44.47727 | 2024-11-17 05:57:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e6b235d5-23d9-3305-bb77-6ad07eced1cc | -3.63231 | -50.2204 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c15fd80e-f2c2-32c8-97d0-75e6e0e785f4 | -2.62856 | -48.56424 | 2024-11-17 05:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 3bf8ea2f-6261-38d6-b77a-898af57ed68b | -0.94598 | -51.72652 | 2024-11-17 05:57:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README65.md)
