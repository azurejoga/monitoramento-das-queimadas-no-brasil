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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 503a0d95-86fa-3772-9567-4a2b52fd8b77 | -3.11221 | -53.25922 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b89e4e3-e229-3953-9a81-a37c600b36dc | -2.26261 | -53.47356 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9391f4d-93c7-37e2-8f79-b02ee26101d6 | -1.66123 | -52.47785 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 417c60aa-ec4a-3ead-8287-e863d2932e53 | -3.63822 | -54.44641 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847c9fca-53b7-3b74-81af-c793b7693288 | -3.25086 | -50.76957 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01536daf-63b3-3b93-a969-9573ebadf497 | 1.31111 | -60.40983 | 2024-11-28 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23cd216f-f590-3b97-816f-d78402433b55 | -2.18325 | -52.12956 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82507375-a7a5-36e8-b798-4cdcea31ffcf | -1.64282 | -52.72853 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 808bdef5-232d-310c-ab9f-2fc44b799e2b | -1.3286 | -51.92591 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08a179d5-34da-3ab5-b760-28146c8ea264 | -4.21042 | -50.88959 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cd60bef-bbb3-3b9a-a152-87c30d5f3659 | -1.36152 | -55.01395 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9045608d-c12a-3f00-b247-71a031373817 | -4.08745 | -54.76188 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b5a64b1-b092-32c4-9d72-79472e9edda8 | -2.60377 | -53.96637 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31fe569e-5b2b-3c0f-8240-8370a37d3577 | -1.58452 | -52.2753 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c91f3c0-f11d-387c-8705-9a2c6bcde4e4 | -2.1462 | -54.81942 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cac2a02-6bbb-306f-aa8a-0d11803eca0a | -2.83416 | -54.12476 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6509cc52-4574-31ad-b6bd-c04c3ecfed80 | -3.30588 | -54.17564 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f152b719-beb7-3a2f-9158-6315204101e3 | -2.62375 | -54.30357 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f25a0a7-605e-3550-97b1-406b0302141f | -2.90202 | -51.37098 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54a361b8-f682-36e5-b6bd-3e9ff1e8dcef | -2.91426 | -51.71226 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fb4eb52-4d51-391e-a5aa-0749ca471572 | -1.98906 | -53.29144 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a140dcd5-bbb4-3a54-ab58-2f42ad964f8b | -3.18889 | -50.82611 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37e0c8c-8fa7-3232-bd8f-0d95adf19c22 | -9.51744 | -64.46336 | 2024-11-28 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ff81b9c-a427-3d3b-951c-aac8705255e8 | -9.8928 | -63.94521 | 2024-11-28 05:42:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cebbb64c-b28b-3a71-8423-eee3ad260d61 | -17.62949 | -57.58037 | 2024-11-28 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d0d1e5b3-1e58-3ef8-a0f9-ff5604ac08e8 | -17.54432 | -57.4351 | 2024-11-28 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 151fd2ee-8002-3a15-917f-3b785df0f4e2 | -17.57868 | -57.59986 | 2024-11-28 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66e0a195-af30-3535-9405-0162043e9752 | -17.57826 | -57.60377 | 2024-11-28 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5f2f9f44-0d0f-3ea8-8f3d-91682b7f2dda | -16.12558 | -59.63363 | 2024-11-28 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1b845e4-8563-32a5-be2a-1eb9f8eba24f | -11.9128 | -63.67805 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 283799b7-4c41-35c9-8e06-eee38cd221b3 | -18.77396 | -55.84724 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 193a3fac-7035-3d2c-b6d3-f0e29dfb5fbb | -18.78131 | -55.83724 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 857cadd8-15b8-3cf8-abb4-76a68814cfa0 | -11.91554 | -63.67712 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd817c0b-b229-360a-a005-6d20aed271a8 | -17.63554 | -57.57711 | 2024-11-28 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 761eb6ac-b615-34d0-80ab-8aeb7a6e1abc | -16.07354 | -59.70764 | 2024-11-28 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45826137-2710-3eae-a802-2740faebbc89 | -15.22016 | -60.2656 | 2024-11-28 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ba8609b-658b-3d01-a337-d0507153117d | -18.78082 | -55.84258 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 782fa805-eb33-3afd-8a0f-758537066be8 | -16.07958 | -60.10069 | 2024-11-28 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97bbeace-9485-358e-956a-ff90d44b5228 | -12.58425 | -62.00585 | 2024-11-28 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 198478da-1188-39c1-bc67-df4a0f68efd1 | -12.28101 | -63.73721 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbf273db-3e14-304b-80e3-9253771ed79a | -16.07836 | -60.1108 | 2024-11-28 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a936467-e5e5-3734-98ea-148885a76e85 | -18.77493 | -55.83657 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 27c78768-e41d-3bd9-8239-3682fffdee75 | -12.11794 | -63.7986 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afbb19f1-1210-35b1-9c26-f8233c523399 | -15.69109 | -59.14665 | 2024-11-28 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f4da410-bcb9-3ce7-93b3-19cd386a726c | -16.16272 | -59.61079 | 2024-11-28 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203d4d3b-da7a-3f8a-8f03-c21ec19a898d | -16.07897 | -60.10575 | 2024-11-28 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d8ee89c-072b-34ba-bdcc-23f633464362 | -12.58827 | -62.00987 | 2024-11-28 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 474c4a9c-1cba-3b13-a26b-b775c08298d2 | -12.58818 | -62.00642 | 2024-11-28 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99237d17-2a57-32c3-8932-e0392017508f | -12.58434 | -62.00929 | 2024-11-28 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98593542-1739-3fef-8788-ccc28647b4c8 | -18.77445 | -55.84191 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d037070e-d833-3759-8023-ae8ca2d86052 | -13.41621 | -60.19743 | 2024-11-28 05:44:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2277b051-e0e8-3920-b806-68b7a7b0d211 | -17.64119 | -57.57779 | 2024-11-28 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c362b62e-d2f7-3b1e-b171-855f41d90318 | -15.21955 | -60.27041 | 2024-11-28 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b1309d-a43f-375d-9246-de2896294b2c | -12.11684 | -63.8013 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41be2404-a817-31f9-8b64-e8c867ac125a | -11.90924 | -63.67751 | 2024-11-28 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbe8fbbf-f447-338c-8829-cf32815ba33a | -18.76856 | -55.8359 | 2024-11-28 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63900186-eb78-378c-9c84-fec8e4cf864d | -20.72496 | -54.43375 | 2024-11-28 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91fdf6a2-c69a-3ada-be8c-7f74a0c462f4 | -21.60627 | -57.49899 | 2024-11-28 05:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c77ab4bb-fa28-351d-bb10-ccb10d2fd203 | -20.71791 | -54.4332 | 2024-11-28 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4cf52851-98fd-31e6-8e09-3978d4d570a3 | -21.60663 | -57.49479 | 2024-11-28 05:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 386cfb9c-8365-32f0-a5f8-a063bb941633 | -20.72088 | -54.43531 | 2024-11-28 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a3c82c5-cbd6-36cb-826e-aeb19ceded33 | -20.72146 | -54.42797 | 2024-11-28 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f10ce36-5ecf-37a3-babf-5f50a63ab2d3 | -21.60901 | -57.49792 | 2024-11-28 05:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce29cda8-1461-3c9a-8d69-ef2b26dab4b2 | -21.60304 | -57.49752 | 2024-11-28 05:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea5ede1a-e418-3cd1-a957-9668a3394be4 | -5.9788 | -45.3621 | 2024-11-28 05:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 00ee6622-f0af-3d14-8aed-9db08343a1ee | -5.979 | -45.3395 | 2024-11-28 05:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8e3e00d6-14a0-3e65-84f6-12a58239095d | -1.5897 | -52.271 | 2024-11-28 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9768bdde-ba1e-3401-86e6-a9940834bfba | -3.3853 | -45.8241 | 2024-11-28 05:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 114.2 |
| a1ecc430-0068-3d1e-aecc-47a0a930e6cd | -6.1735 | -42.6221 | 2024-11-28 05:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 2c4180cf-01a3-3437-bedd-fbdee9e8eb3e | -3.3666 | -45.8472 | 2024-11-28 05:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c2a9955a-7826-3d04-b111-849e1a944660 | -3.3852 | -45.8465 | 2024-11-28 05:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 658d2d8b-70b1-3f64-96f2-836d99f420c4 | -3.3837 | -50.1125 | 2024-11-28 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| cf539838-4091-3050-a3ff-8e8f5af79948 | -5.9975 | -45.3607 | 2024-11-28 05:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7229fb83-a42f-33a5-8f03-2965a3acb09e | -3.4038 | -45.8457 | 2024-11-28 05:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d20a75e8-4240-35d2-918c-649c52c491e0 | -3.4039 | -45.8234 | 2024-11-28 05:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b49cec59-13e8-3714-8c6b-3b6e9fca5895 | -2.8347 | -54.1125 | 2024-11-28 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 341dd0d5-8ac6-3775-9e21-809bef6884c9 | -5.9788 | -45.3621 | 2024-11-28 06:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 215ac685-36ff-3a69-9160-39a511bde6ea | -3.3837 | -50.1125 | 2024-11-28 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 847330f8-b5e2-32bc-97c5-8413c4738aad | -3.3853 | -45.8241 | 2024-11-28 06:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 7b0b26a0-bd66-3c4e-9aeb-a1647ac182f2 | -3.3666 | -45.8472 | 2024-11-28 06:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3c499ba1-066e-3bcc-ab47-2183d7926f11 | -3.3852 | -45.8465 | 2024-11-28 06:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 183.6 |
| eb67294a-9e85-3190-87c7-a03ea778d8b7 | -6.1735 | -42.6221 | 2024-11-28 06:00:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 8896db5d-dc46-31d3-ac8c-933619e23a26 | -1.5897 | -52.271 | 2024-11-28 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| fbad49c7-79e5-3b18-8a39-f46bd1ab6b6c | -3.4038 | -45.8457 | 2024-11-28 06:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4dc18e04-1a0a-3f20-bf28-c33c6a97c6cb | -3.4 | -45.84 | 2024-11-28 06:00:00 | MSG-03 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdb57210-d316-3dd9-b9d2-1649dbbd230a | 4.25966 | -59.99111 | 2024-11-28 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777a889f-1d17-398d-a980-9c746ec39da3 | 1.31146 | -60.41012 | 2024-11-28 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba42d36-3282-3bc8-a7ca-aedc67ab0231 | 1.31202 | -60.41365 | 2024-11-28 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85332f86-2352-310a-a07d-403a6e331f08 | -11.91317 | -63.67875 | 2024-11-28 06:05:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa824ae-d2d9-38e5-9cfc-aba3b9d0ed53 | -11.90787 | -63.67803 | 2024-11-28 06:05:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4c4851f-bf66-3b4a-9351-c8587c6637d8 | -16.07659 | -60.10958 | 2024-11-28 06:07:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6bb6d326-9df2-318c-8a96-c54dc02716ef | -16.07743 | -60.10837 | 2024-11-28 06:07:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8ab3db5-f9d6-3553-814b-ef2e0aa2b44d | -12.5835 | -62.00957 | 2024-11-28 06:07:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a3c46a5-7b2a-30a7-af9c-53a2cb9785f8 | -16.07679 | -60.1151 | 2024-11-28 06:07:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c99d4506-51dc-399e-bf2b-0ae77febc2d1 | -5.9975 | -45.3607 | 2024-11-28 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a4b6c357-4a37-34ad-ac91-79a07b7b2667 | -1.5897 | -52.271 | 2024-11-28 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ed667ed2-3a9a-32a3-9773-98c26dc135d5 | -3.3853 | -45.8241 | 2024-11-28 06:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| be15b281-4bb6-316e-953c-8f6882785ae9 | -3.1113 | -53.8242 | 2024-11-28 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 5c8b824b-4316-34b8-8f18-e56883b816af | -3.3666 | -45.8472 | 2024-11-28 06:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 62de62b9-edc3-3d60-b245-5d0ab3d28031 | -3.1114 | -53.8041 | 2024-11-28 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |


[Clique aqui para ver as próximas entradas](README98.md)
