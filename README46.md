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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a803c87d-a30c-3231-8f97-3f9843f9819f | -6.57269 | -44.1547 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3db59e8f-7d0e-3ec8-9ec9-3dfa726120f1 | -8.71386 | -61.40546 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34310b9c-ce83-3e3c-a740-11bd7cd46ca3 | -6.0201 | -53.53405 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a284e600-51fe-3e30-b9d1-0acee0544f72 | -10.35279 | -45.02461 | 2026-10-04 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b20f2220-ac70-369e-bd08-54c179d30233 | -3.90256 | -55.82472 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 038d310f-b45e-32e8-891b-1e8e32f86cf8 | -7.87764 | -61.43668 | 2026-10-04 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d4e242a-01b2-3233-96da-725741ea2dfc | -6.08114 | -53.47125 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8961adfc-8873-3434-b6b9-1193c39c92fa | -5.78033 | -50.20313 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdd80e1b-ad21-3f74-9bab-3ababbd4f462 | -5.99523 | -53.64101 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8837ca9-ef9b-3845-a0e9-779ab194ed0c | -9.6972 | -57.45227 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97c2dcd0-c832-3a73-81dc-8fb605abe606 | -8.35183 | -62.8398 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecff2216-1fc8-33cc-b12b-a1cabde2170a | -6.20414 | -52.79589 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 038dd634-1dce-368d-a755-847509117edd | -10.83494 | -57.20691 | 2026-10-04 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1234e9a0-f045-3429-8272-93b8b2d6b795 | -4.81101 | -49.28135 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc05ec5-9871-3fa4-9767-88bbef214e1c | -4.05934 | -54.31792 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5b4b5275-6e80-3e23-9a4b-c564370d7602 | -6.81281 | -46.65284 | 2026-10-04 04:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8843c52c-40de-3136-8b4c-209ecd3fddeb | -7.01182 | -47.52603 | 2026-10-04 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 505c651a-4f79-38d3-9481-f56934baa31d | -6.08257 | -53.30653 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d90e37e3-540f-369e-a98a-4a46279de9ee | -4.13221 | -54.15394 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f9c2d6d-f17e-357d-8993-2ef9252fee95 | -5.1794 | -49.33773 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f79cec-5741-36bb-9f99-efa630e063b9 | -9.21445 | -57.63766 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f07ae9-6136-33b9-aa94-4dd6f6cda6ff | -11.81458 | -43.54464 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34fe8758-e0c3-3ed8-90e7-0f63aa5627de | -6.0326 | -53.88544 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c4957d-59a9-3870-86a0-fccdce3aae2c | -10.87016 | -49.74147 | 2026-10-04 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3abd806-9d17-3308-873a-1c8cf7abe0ed | -5.25641 | -55.92374 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb40bf54-f98b-3415-b729-36eb84a30372 | -9.08366 | -61.1552 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0753418e-bdbc-3e1a-bf8e-c6b366f8f0ad | -5.80359 | -52.0958 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b173c537-8f01-3c8d-9241-c4dab6b7acae | -6.20798 | -53.26612 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dd56eb9-9208-3efe-a710-bf7c3001fa6a | -9.08848 | -61.16083 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab6c29bc-0866-3d02-bafb-ce1abb357f6b | -10.25271 | -49.65883 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f5197b8-141d-3ba6-926d-1bbf2cdf3acb | -5.99946 | -53.52688 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 089779c0-faab-33a5-aac2-5eaf108105a3 | -4.13148 | -54.15848 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0508132-90bc-3b42-95f9-8371d6a292e2 | -3.90509 | -55.8868 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a6b1d71-0f18-3d1d-b647-81da0cce506d | -9.70004 | -57.46091 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7b38d5e-7d68-30be-b0b2-e944fb5fad23 | -6.4542 | -55.4561 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 787229da-b27d-343e-94fa-43f056f269bc | -8.71529 | -61.39795 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d59d01c-26a8-3ec2-8d4d-e7a26798c0da | -5.79577 | -48.82729 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c2d1711-5ec4-3bc9-ad87-42bf87afca48 | -5.62896 | -50.02896 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe8d555-5c30-3fdc-96aa-16fe4bf56028 | -6.07906 | -53.30596 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6b397f-616a-3c28-8794-cb24989d0328 | -5.96335 | -55.35178 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70a27396-b66b-3197-bb63-0a3ab524285c | -4.12847 | -54.15332 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97315d51-dcbb-3e5c-8cb0-2d108c56a511 | -10.24693 | -49.65007 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b413baf0-36df-3312-abb1-acbb040dae70 | -4.53414 | -55.97289 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21e4544f-d933-3e93-b259-5acfc960862b | -8.34484 | -62.83473 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d41dbc16-f006-367a-88f5-bb0ad41d4d9a | -6.37062 | -52.69255 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f6994dd-fc62-33d4-a731-294b0f2e3a51 | -11.82006 | -43.54287 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8525466a-6752-3108-babd-aefc736cd2e4 | -6.00301 | -53.5274 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6c7521c-3858-3cf0-91da-706503661b2b | -8.709 | -61.4006 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 50a390e1-dbc8-3e57-bb2e-f543eab23eca | -3.96101 | -55.78057 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be5c2645-bd74-38f1-a874-740c4472db74 | -6.86447 | -46.41735 | 2026-10-04 04:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 766ab2d0-9918-32f9-9051-4dd31f2634bb | -4.1009 | -54.32456 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2a3e91a-43ba-3bfa-8e08-634b2ceea088 | -9.13475 | -65.9508 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f09cf38e-6a4c-39b9-b31c-9fcda62a335c | -3.94169 | -56.05355 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a923c821-ed86-3a71-94cd-27c14413b4fa | -4.42122 | -55.74831 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c4adda4-451b-3319-97ca-b4c7f0f5adf6 | -6.90139 | -43.68394 | 2026-10-04 04:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| edc69dc4-db6e-31a8-beca-01e465ff1f14 | -4.42702 | -55.75032 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf8b182b-e7ce-3bbc-b5ee-906bf05aa1ce | -6.57881 | -44.14342 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b468af-47d7-33b0-a93d-5041677163fb | -5.73964 | -45.14265 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2887699e-b0a2-3f93-9009-2540c8c3231d | -3.86496 | -55.81144 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e04b2186-489c-34e6-b053-b3bd3d250809 | -5.74329 | -45.14717 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b957cdf-4874-38e4-9c1f-70e00dde71cc | -4.4253 | -55.74913 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e01934a-3077-37a6-a900-5561dd0b420d | -9.08776 | -61.16341 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d8590ca-c04a-3760-8d99-a0ef58cb1000 | -6.013 | -53.53296 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8413ce47-bb81-3194-a77b-330520be3782 | -4.44499 | -54.96848 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f9ef8ce-161f-3d9c-a6fc-abd5cbf367bf | -10.24287 | -49.65339 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 809d0eec-2d05-3ec7-b4b4-1bb5659063e4 | -4.43688 | -55.23481 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d460d93-060b-377a-8dc7-f18916e36641 | -6.22137 | -52.68844 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e35ef0-2476-3353-9e08-f2c0c1955d04 | -4.8523 | -49.41968 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 988f9ebd-f383-3d27-8c8c-1a7ec76553a5 | -6.00618 | -53.55235 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9c857e-baef-35ac-8679-85352cc6762f | -7.00812 | -47.52544 | 2026-10-04 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd07fa7b-097c-3c7d-b995-4fd11a469658 | -6.31336 | -43.34121 | 2026-10-04 04:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f427c28e-085f-395d-89c6-2e10cc3be82b | -5.85952 | -55.70454 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ab770f1-90a4-3ea2-ac84-86442b4ef5e9 | -10.2556 | -49.66321 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 662cec55-14de-3078-bdb8-d20091ab2569 | -5.78092 | -50.22112 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bed7ba9f-4547-3c1f-b859-acb633ac9e11 | -5.96023 | -55.34634 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e043b386-8aec-3d0c-8ad0-d0523487c26c | -6.21085 | -53.27061 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f5b5c36-e334-308e-9a5f-beb4bdebc6ab | -8.716 | -61.3942 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed59e709-2944-3311-be92-17ff76c39454 | -3.86556 | -55.80772 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| df6ac3ef-71b4-3fe4-a430-1cadf8818454 | -9.70142 | -57.45304 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9b7efe-6b8b-3e61-bbd5-4e9be8b57384 | -4.42764 | -55.74648 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820961a0-2ee3-3a37-a51a-8d3070ef8fc8 | -8.34209 | -62.84898 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90034c02-d259-3b8b-823f-0ae1b18703c1 | -6.23707 | -53.15268 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e5c1810-2adc-336c-b92b-b5574b01eb26 | -9.48252 | -64.69195 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d75f5673-ff0e-358b-a278-8326b5cc728f | -10.24923 | -49.65831 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73da89f5-dc49-3403-9569-785cb92dd16f | -6.45811 | -55.45676 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5006864a-e81b-3799-a4a7-cd763386b89b | -8.86698 | -50.52739 | 2026-10-04 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb591e0c-e056-3027-8ca1-1724928f9a6c | -9.47398 | -64.34113 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb7ecf69-b5b0-3836-b98a-697f8a6e17d6 | -10.2417 | -49.66108 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 261de49c-efa7-34b5-a526-a13e5dc11536 | -4.53476 | -55.96916 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7c0910a-37da-30af-aca2-f35b9b60a7c7 | -10.2194 | -59.08846 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26925dbe-976e-3405-b66c-db7c32bc8f11 | -6.45504 | -55.45117 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e58d904-d5ec-3410-b7e6-cc8e13558c8c | -8.35271 | -62.83504 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d613ff6c-0ee0-364f-880d-40decf328e17 | -4.12774 | -54.15786 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceea2d37-7468-345f-8036-4aa5e2fcca94 | -4.52144 | -55.75403 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b7f0872-6d1c-3442-838b-b4c970fa204c | -5.82593 | -50.19598 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60e5fd85-4831-3836-ad44-9b641881237d | -4.13449 | -54.16364 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a56aae09-a57c-3a54-800c-10263b1889f7 | -6.21341 | -52.7967 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c4fdc29-e11f-3f48-b00b-e646e2796c24 | -9.08914 | -61.15723 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de89e087-19bf-365b-93c3-9acb3eb1f861 | -9.50874 | -54.63371 | 2026-10-04 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6090873b-afc2-3e0f-8349-efe0af29d274 | -4.81766 | -54.72779 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
