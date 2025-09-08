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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0a1ff30-28e5-3829-909e-322a3e791133 | -12.9021 | -47.9823 | 2025-09-08 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| bff77d99-a372-3ca1-8261-e4cceaad5622 | -12.9017 | -48.0045 | 2025-09-08 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 3962a4ec-69da-348d-b5c5-c16b95cc0390 | -11.90917 | -50.97039 | 2025-09-08 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 75e8eb07-6027-3423-96f1-65864e823808 | -9.62388 | -64.20384 | 2025-09-08 06:50:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 89b3d924-b365-398e-aac8-03193dc95136 | -10.05635 | -59.36149 | 2025-09-08 06:50:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 33849d2c-9810-32eb-8e12-8b0cce13f029 | -12.61322 | -56.97062 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 1df2af64-b2bf-36c9-a0c9-0901d53e35e7 | -12.95041 | -54.78032 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d35bfc30-4450-3eb2-96d5-34e19c3fbf28 | -12.63501 | -56.97355 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c1145438-1f35-37ca-9eb6-aa2150ed0f3c | -10.04728 | -59.36016 | 2025-09-08 06:50:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4e295e63-323c-3c09-8dd2-37717e788fea | -11.85946 | -51.07856 | 2025-09-08 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 10af1c89-f522-32d1-b113-de606a122404 | -12.62411 | -56.97213 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bb16c97c-53b5-314c-8daa-dd504e369a7f | -12.62219 | -56.98625 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d429ddd2-f059-3eda-93b4-a97024031782 | -12.62571 | -56.97938 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 8cef8894-776d-3f2a-b352-560bf6a7eaad | -12.62754 | -56.96511 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ec74899c-0f31-3704-9801-bbd63928b1fb | -12.94785 | -54.80122 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| aa63f059-219e-3e82-b3bb-d6b709e1b9ae | -10.87783 | -55.71581 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 068fd6be-c69f-3b9b-b86a-eb93109665a1 | -9.44926 | -61.81757 | 2025-09-08 06:50:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 269b7586-353e-3675-ad00-91ed1a36f4c2 | -10.5794 | -61.25075 | 2025-09-08 06:50:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e64083ba-b98a-3b16-89dd-5414e6c2a72e | -10.88805 | -55.70587 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f8ab6185-a2f2-387b-b07c-8a380d3f466a | -9.44785 | -61.82668 | 2025-09-08 06:50:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 94bd8cdc-26c3-3fdf-9549-9f3120e97a0b | -11.86401 | -51.03878 | 2025-09-08 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| b4526a0d-fae2-36f9-a258-ff252e2ad890 | -12.41658 | -63.89315 | 2025-09-08 06:50:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 740b2138-223a-3f9e-8bda-21dc1b69fd17 | -11.866 | -51.04691 | 2025-09-08 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 161.5 |
| cde65d7c-3171-36ad-b1ff-830a4cf8c557 | -12.93735 | -54.77869 | 2025-09-08 06:50:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 6745f33b-b352-3324-9cf2-53d7dbae0875 | -11.90771 | -50.96225 | 2025-09-08 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 56b3df68-304b-31f5-b20f-26f576256193 | -9.62358 | -64.20947 | 2025-09-08 06:50:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60cd2fec-0fbe-39c0-9a94-40a0ffb9daaa | -12.9017 | -48.0045 | 2025-09-08 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b0d1c436-2949-31e7-98bc-2dd3a8899a32 | -12.9017 | -48.0045 | 2025-09-08 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 85d29949-d944-3063-a6b3-3bbc3c43690b | -18.7598 | -49.5805 | 2025-09-08 07:30:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f1589e5b-2fc6-3f7f-ba92-602b4e590611 | -18.7598 | -49.5805 | 2025-09-08 07:40:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 86f878d4-09c9-35bc-8640-f544b35298b3 | -18.7598 | -49.5805 | 2025-09-08 07:50:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2b5a23bd-8907-30eb-b674-84b8b49ea054 | -6.8708 | -47.9129 | 2025-09-08 07:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7c0161c6-43ea-337c-9153-20cef6dd0f7e | -18.7592 | -49.6031 | 2025-09-08 08:00:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 01b933da-43e0-3cab-9b45-e9d18d229312 | -18.7598 | -49.5805 | 2025-09-08 08:00:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2c13b8de-4b3e-3719-84e1-05f3823baad8 | -13.8403 | -46.2828 | 2025-09-08 08:00:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d069b3a3-bf71-3314-9685-bccc9fc1ecb5 | -20.4748 | -43.9683 | 2025-09-08 08:10:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| e90db694-0315-373e-877b-57e7a03ca965 | -15.9632 | -48.0984 | 2025-09-08 08:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 82e50491-c659-3c82-ad5a-733373340334 | -18.7592 | -49.6031 | 2025-09-08 08:10:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 33dd7916-05ee-316d-9c63-8f314025f944 | -15.9829 | -48.0949 | 2025-09-08 08:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6cbe0764-2d9f-37e9-b70c-feda2492de6a | -14.5067 | -48.8085 | 2025-09-08 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 89b23f5e-5676-3751-b12f-4f65f920761a | -20.4756 | -43.9435 | 2025-09-08 08:10:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 8aa28fc5-9b4f-338f-945d-3fff87e84013 | -18.7598 | -49.5805 | 2025-09-08 08:10:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 148933d1-65b6-3e98-87da-68c5dfc72c73 | -18.7592 | -49.6031 | 2025-09-08 08:20:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 9333d89d-bdab-30bf-9ff3-024a1fc8dea4 | -18.7598 | -49.5805 | 2025-09-08 08:20:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d19fc1e0-4d7e-32a8-9c04-7303841e2992 | -15.9829 | -48.0949 | 2025-09-08 08:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 87b71a37-86c6-320e-8e53-faa85d98c7c8 | -17.2404 | -46.5757 | 2025-09-08 08:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 16e1eb03-975e-352e-bf63-b6dfee47ad79 | -18.4722 | -49.0736 | 2025-09-08 08:30:00 | GOES-19 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| ee697355-c0e1-3e75-b911-f497a0e207ec | -15.9627 | -48.121 | 2025-09-08 08:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 49f8c64e-2b09-3403-81d5-fee5999cec7b | -18.7598 | -49.5805 | 2025-09-08 08:30:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6bbd3723-2852-33db-82c3-5d195e9c2e23 | -15.9829 | -48.0949 | 2025-09-08 08:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 9ea89978-f8dc-3209-8227-8b09e10bcf7b | -15.9824 | -48.1175 | 2025-09-08 08:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 6265c957-adb9-3ae2-aecb-5730ae126e3d | -15.9632 | -48.0984 | 2025-09-08 08:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5a2b0abe-1f4c-3858-82a1-a5302f5895c7 | -18.7592 | -49.6031 | 2025-09-08 08:30:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 4a6883e6-cc01-39e4-9aeb-fca701490f75 | -18.7592 | -49.6031 | 2025-09-08 08:40:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 53fe5384-9dcf-35f0-a8c3-bdb201b7329a | -18.7598 | -49.5805 | 2025-09-08 08:40:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c1a9aefd-1510-36c7-9f1e-3d61f4573ea2 | -18.7592 | -49.6031 | 2025-09-08 10:20:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 34d45f26-a1d2-362a-8d17-acddd348854e | -18.7598 | -49.5805 | 2025-09-08 10:20:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |
| b1b4460f-a8e0-388e-93de-66eacbb0aa7a | -18.7598 | -49.5805 | 2025-09-08 10:30:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c5338631-ace2-368b-b1a5-2ac06828979f | -11.282 | -46.5269 | 2025-09-08 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| a45550f2-f7a8-3210-852a-4fcfb563e7f8 | -11.282 | -46.5269 | 2025-09-08 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 64182333-cce9-3ccc-a51e-3c8e953569fd | -10.177 | -46.6881 | 2025-09-08 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8bd2560d-c820-31b6-9ad6-5f3e7c6cefa7 | -7.6559 | -47.9593 | 2025-09-08 11:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fd468d6f-d9d9-38ca-a9cc-1afe2546f21f | -15.044 | -50.1118 | 2025-09-08 11:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 938e7089-a552-3a82-9460-e1b1959679cc | -5.7113 | -43.8972 | 2025-09-08 11:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 910e1c27-46be-360b-a3d5-247c85741da2 | -11.3011 | -46.5244 | 2025-09-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 44bd435e-84d7-340c-b1e7-c6aa412eb1ae | -12.2941 | -49.9904 | 2025-09-08 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 69bffda0-7906-3c59-8eae-70de33b2fe96 | -15.0445 | -50.0899 | 2025-09-08 11:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 95a68399-8cdb-3d75-b0ff-92c1edd70bf8 | -11.2823 | -46.5043 | 2025-09-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 80461079-69f0-3420-9ad5-1b1f00867904 | -15.0635 | -50.1089 | 2025-09-08 11:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 56e249bb-9f41-39c0-b3d0-5f78f6e44234 | -7.4367 | -49.2747 | 2025-09-08 11:30:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 7f978889-4c40-39a2-895b-cd5b6b8bc8d3 | -11.282 | -46.5269 | 2025-09-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 434.5 |
| cb9bc0ce-62a5-3b8b-848f-a5bc2aa952e7 | -4.48924 | -37.89027 | 2025-09-08 11:34:00 | TERRA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7ba44cdf-e12b-37a3-8d2d-016e71902c94 | -5.17837 | -37.85201 | 2025-09-08 11:36:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ca597959-66ac-3ab6-b567-721d3b58f2a5 | -4.89272 | -42.21553 | 2025-09-08 11:36:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 39a0f8f2-ee6f-34e7-a1e3-ade508a11491 | -4.89297 | -42.20867 | 2025-09-08 11:36:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| ee6b97a7-5704-31ab-a0d6-ce8079182f40 | -4.13164 | -41.43875 | 2025-09-08 11:36:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 94268743-807d-359d-9920-169dd484e466 | -11.28387 | -46.50332 | 2025-09-08 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 8878c1ed-75d7-38e9-bafd-0891f4b63e95 | -6.11189 | -44.14012 | 2025-09-08 11:36:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| add04d2b-6a7a-3e2e-9186-6ccab96bb544 | -10.1765 | -46.69439 | 2025-09-08 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0f36918c-074a-3f15-a503-e167e1082ed6 | -6.21884 | -43.37894 | 2025-09-08 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ab825438-8029-3353-a8ee-515a7487f230 | -5.71912 | -43.91384 | 2025-09-08 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 0e858ac1-a013-3eca-a6f5-cc3f3b913737 | -4.14373 | -41.44058 | 2025-09-08 11:36:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a61652cb-653d-3ffb-85e0-7742fe4c8107 | -8.05966 | -45.48951 | 2025-09-08 11:36:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0f839e90-35a8-3d4b-9adb-8bc1a2a94c5c | -8.1966 | -44.76626 | 2025-09-08 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 3c393d99-0f08-3ba7-8c83-ee599d3948b5 | -4.89004 | -42.22813 | 2025-09-08 11:36:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| a7cc5683-8ffc-3a57-9d1a-02fffd05ede0 | -5.72309 | -43.88836 | 2025-09-08 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9b224bc7-ecbd-39a6-890e-a7d8143156b4 | -5.25761 | -37.36958 | 2025-09-08 11:36:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8feff340-0768-3fb6-99db-ff1acf44026e | -5.4568 | -42.80058 | 2025-09-08 11:36:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| dbc5f7b5-97f4-38d3-9040-427430538867 | -8.06508 | -45.48303 | 2025-09-08 11:36:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 8f6dae21-34d3-33fc-b057-c6a920dc1e3b | -4.90278 | -42.23001 | 2025-09-08 11:36:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 9e3e4025-b797-3ab4-8cb0-0f8bad5d72e6 | -11.42079 | -43.63731 | 2025-09-08 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1db73821-b58f-31d9-b26f-ec7a27edc2f5 | -6.21226 | -43.37098 | 2025-09-08 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 2c3fd25a-c102-3922-84a7-60e45b4e8a33 | -14.26335 | -44.96028 | 2025-09-08 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 290.9 |
| da714953-d3a4-3baa-afda-3838d5694c0f | -16.90339 | -45.83466 | 2025-09-08 11:38:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ceb76336-adb5-3f32-b649-b12ae7340a0a | -13.81835 | -46.27017 | 2025-09-08 11:38:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 1e38a406-1ac9-3761-9c59-a407e9655677 | -11.29308 | -46.51061 | 2025-09-08 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 294.0 |
| c3c6f012-0ce8-35af-a0b4-e130af950617 | -18.35271 | -43.92689 | 2025-09-08 11:38:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e923892b-412b-3c37-992b-a2b250946476 | -15.82803 | -42.59677 | 2025-09-08 11:38:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| bfb84be8-81f7-3442-a64d-cb5294d1ce97 | -15.19318 | -47.96737 | 2025-09-08 11:38:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8575c7f4-b0bd-37e2-9476-d10f6ce26859 | -11.28758 | -46.54151 | 2025-09-08 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 321.0 |


[Clique aqui para ver as próximas entradas](README95.md)
