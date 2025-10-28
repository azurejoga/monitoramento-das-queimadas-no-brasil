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
| ddb5653a-c129-3d4e-9b94-f7496a4ccc0c | -6.0974 | -44.6718 | 2025-10-28 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 56b2388b-8c77-3a43-b01f-44a8ac61571a | -10.5683 | -49.8018 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6bf37b18-ca9f-36bf-89cc-e503f2515314 | -4.3812 | -44.2832 | 2025-10-28 00:20:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cfbd8228-2ffb-3868-bee3-671f30822f13 | -4.3625 | -44.2842 | 2025-10-28 00:20:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| b33beef6-3591-36b7-a21e-eb3bafe935bf | -7.9368 | -49.7271 | 2025-10-28 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 5ad1e5f9-0c10-3df8-a5f6-da46712d27fd | -1.8608 | -54.5114 | 2025-10-28 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 81dd46d9-2b1d-353c-89a1-ef0ca936d062 | -2.7555 | -45.422 | 2025-10-28 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cb254531-008d-3fbd-8970-5fa2f85a123a | -10.9216 | -50.2571 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a96a2cf8-1d70-3379-938c-53e6b5321cd7 | -7.9464 | -45.4882 | 2025-10-28 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b87be4db-adfe-328b-8b09-9ca4fc049853 | -10.9405 | -50.255 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d0a3e1c5-f7fe-3828-9a56-e08f23fcf51f | -5.8386 | -46.4472 | 2025-10-28 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 319a3773-bbe1-3816-b096-0a25cab6e64f | -10.9402 | -50.2764 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 90a48e9a-355b-32ae-a5f0-5601ed91fb7e | -6.7064 | -42.0278 | 2025-10-28 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| e44fddbe-b8c0-35f0-a0e8-6217cc9ba677 | -14.155 | -44.2289 | 2025-10-28 00:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ab2dce7f-1ef6-319f-bc0b-7f0f15a1d70e | -14.1545 | -44.2527 | 2025-10-28 00:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9d42e03e-d55b-3da2-9ee3-7523515248b6 | -12.629 | -45.0749 | 2025-10-28 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 46488d9f-d01e-316d-bd6b-2ed8c03ad8e4 | 0.9845 | -51.1035 | 2025-10-28 00:20:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 0abfba98-f8d2-32f9-918a-ba90176348d7 | -7.965 | -45.509 | 2025-10-28 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 8b98d26a-22ac-3bbf-8c6f-8944ebcd8eea | -7.9882 | -46.7406 | 2025-10-28 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fd375e2b-aacd-373e-859f-6cceb7056706 | -6.6873 | -42.0535 | 2025-10-28 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 157.2 |
| d8cd1d7d-c9dd-33ee-9d1b-d684cdb73b59 | -7.9366 | -49.7485 | 2025-10-28 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 807de72d-795c-3f94-ad7b-6fbf7d8f7abe | -5.8386 | -46.4472 | 2025-10-28 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0cc297c1-8101-3153-ab6e-493e475f4241 | -2.7556 | -45.3995 | 2025-10-28 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.5 |
| d194f19d-4f78-39bb-8c91-11bb55a72253 | -7.9647 | -45.5317 | 2025-10-28 00:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 50a98d21-44a2-384e-8418-36dcec6bc253 | -10.9213 | -50.2785 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5a3d58ef-f335-3f01-abdc-22b8f5ab18a2 | -10.9216 | -50.2571 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3e141f91-1b38-3a5d-9fb1-cd364a2a210c | -11.2798 | -45.5052 | 2025-10-28 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a6cee60b-e696-3142-a657-69a962b0feca | -12.0804 | -45.6655 | 2025-10-28 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a24320ec-19e9-3e3e-a491-981f9b4d4d39 | -10.9405 | -50.255 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5daca03b-24c2-30fb-8f6f-d9959c2c3f9f | -10.5686 | -49.7803 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| dff0526b-cb91-33d6-9431-4f5c6253a528 | -10.9402 | -50.2764 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 882bae4c-1013-3986-ad03-545df7ba7e43 | -7.4539 | -49.4232 | 2025-10-28 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| db20ff38-9daa-32ec-a7ae-e5492c813532 | -6.7061 | -42.0517 | 2025-10-28 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 219ccf4f-57fe-38b0-a28b-65566be3dfec | -7.4354 | -49.4032 | 2025-10-28 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cc94a295-eb4a-3804-a023-2435f6c79514 | -7.4541 | -49.4018 | 2025-10-28 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 8eb2a124-1185-3852-9e87-12f9f6c16c40 | -7.9368 | -49.7271 | 2025-10-28 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d75a38ca-38e8-330f-91cd-4ac29d8e6ee6 | -6.7064 | -42.0278 | 2025-10-28 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 5da60173-0ff8-3cee-bd91-beded8cd8bf7 | -4.3625 | -44.2842 | 2025-10-28 00:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 19952587-bbef-34ec-a96d-22095be1bf33 | -6.6875 | -42.0296 | 2025-10-28 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 157.0 |
| de394bdf-2b4b-3e3c-b55a-165512a4ff59 | -5.8572 | -46.4459 | 2025-10-28 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bd7c56fb-c075-3399-abd2-09156eb24df5 | -10.5683 | -49.8018 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f80252f4-ad60-306c-a5ca-bd071ac68bf3 | -7.9882 | -46.7406 | 2025-10-28 00:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 93c47534-5590-3e03-8272-a98a136b5acc | -4.3812 | -44.2832 | 2025-10-28 00:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9da58afb-eacb-36e3-8368-2c486017f580 | -10.5872 | -49.7998 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a18b99fa-cfe8-3b7b-87d1-d4351fc9dc13 | -7.965 | -45.509 | 2025-10-28 00:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 4fd07a92-ba18-3ec6-bc26-f8b290b49b6f | -12.629 | -45.0749 | 2025-10-28 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d2c7b7ab-f041-31e7-9c10-6a962110dc55 | 0.9845 | -51.1035 | 2025-10-28 00:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 47ea2604-9407-3152-8b0c-10dc20a90a39 | -2.7555 | -45.422 | 2025-10-28 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0757f44f-6049-3500-8443-0d5a52846a5d | -10.568 | -49.8233 | 2025-10-28 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 0ce2f6bf-55fd-32a3-9c42-b4178a231fae | -7.9368 | -49.7271 | 2025-10-28 00:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0cb144ae-a0b5-3377-ab4d-cf36c4c4ee6b | -7.9882 | -46.7406 | 2025-10-28 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 233a396f-afb2-34ba-b64b-4f7cb771514b | -5.8572 | -46.4459 | 2025-10-28 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7c4e99f1-8b51-3414-9d2a-99b6831447e6 | -4.3625 | -44.2842 | 2025-10-28 00:40:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d1d100b7-1639-3391-b7be-cf6e8cff07d5 | -4.3812 | -44.2832 | 2025-10-28 00:40:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f9c996ff-4597-3823-96f8-fc7345e1d592 | -10.5683 | -49.8018 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 104f0746-5881-357f-9ab2-159c1948f58d | -10.5686 | -49.7803 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 21b1ff9c-44ec-37ba-b7a0-4b10e05cce85 | -10.9216 | -50.2571 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8369706c-db4c-3d5c-8c21-6b27d7722717 | -7.965 | -45.509 | 2025-10-28 00:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b3d4a606-1285-3261-82c3-006e6b26ab03 | -9.1371 | -51.299 | 2025-10-28 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 91a7441e-f660-3235-8e04-a09e34862594 | -6.7061 | -42.0517 | 2025-10-28 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| e18e57eb-6714-36e4-b980-c53cf4632b5e | -7.4539 | -49.4232 | 2025-10-28 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 334446ac-f92e-3bd5-9928-9ef68b6c93f1 | -7.9647 | -45.5317 | 2025-10-28 00:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 34da11ed-cae7-3b04-b8d1-dc4432703196 | -6.6875 | -42.0296 | 2025-10-28 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 6a61bf98-427a-391f-abcd-42f01e74ffb0 | -3.5831 | -43.634 | 2025-10-28 00:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f0cc020f-8645-3762-998e-c09bb0a73c7f | -2.7555 | -45.422 | 2025-10-28 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 73c934e4-c82a-3cf2-90d7-cf20a608afc9 | -12.6097 | -45.0779 | 2025-10-28 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0fcb98ac-0b04-324c-ab87-89085d6449b1 | -7.4541 | -49.4018 | 2025-10-28 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 654e2738-32ce-32cb-8330-9b28de9c5a64 | -6.7064 | -42.0278 | 2025-10-28 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 6c3a47de-b661-38e4-8c2f-2f072bdc0a1a | -4.4632 | -43.2386 | 2025-10-28 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 525bc2fa-57cd-3549-8117-c3450757985b | -6.6873 | -42.0535 | 2025-10-28 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 350a06d7-0b73-30fc-abfe-050d3de22e89 | -10.568 | -49.8233 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 562e21ec-e686-337a-9eac-7f6d594d8e42 | -3.5833 | -43.6108 | 2025-10-28 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 2b84315e-f3d4-3f7b-b9dc-36155f290c87 | -12.629 | -45.0749 | 2025-10-28 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 39b6bcd3-2320-3087-8f40-e08721424cd9 | -10.9213 | -50.2785 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ea5f20fc-eda8-3039-9def-f7d3fec39e0b | -5.8386 | -46.4472 | 2025-10-28 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1f1349d8-a2fd-3c2d-9ad8-800ae899aaae | -2.7556 | -45.3995 | 2025-10-28 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| d6e5e126-6b64-3463-8131-530528438952 | -10.9402 | -50.2764 | 2025-10-28 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c59f3173-389a-31e6-875c-7a71034d70af | -7.9644 | -45.5543 | 2025-10-28 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 9f9192d8-352e-3325-9bd0-c3eee997c01d | -11.2798 | -45.5052 | 2025-10-28 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 599f1409-3ab3-39f7-bf31-fa763dcd4c2f | -3.5833 | -43.6108 | 2025-10-28 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| bc79b2af-0877-3827-88a0-5d0f191d6b4c | -3.5831 | -43.634 | 2025-10-28 00:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 40421943-43a4-3411-9f59-27695d5377af | -4.3812 | -44.2832 | 2025-10-28 00:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1d7d632b-2d31-3532-8d17-36eb5df642b0 | -5.8386 | -46.4472 | 2025-10-28 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e4c95ac2-8e57-38a2-992e-26a6ee8e953e | -7.8223 | -46.4664 | 2025-10-28 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 4c86659f-ea5c-35d0-a6f0-02d49f0674c8 | -2.7555 | -45.422 | 2025-10-28 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 188313b8-2d22-3f17-bd2f-65af46a2330b | -7.4541 | -49.4018 | 2025-10-28 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| ea74f3c6-1825-393f-8b29-d0f6f8685959 | -11.2798 | -45.5052 | 2025-10-28 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ca68ae44-3167-3811-813f-c01c2c7c4ab5 | -7.9459 | -45.5335 | 2025-10-28 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| f69399a2-0687-3541-a10b-a3ceebbb00ef | -6.6873 | -42.0535 | 2025-10-28 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| f03ed322-dd63-3db2-9a7f-28f1c616753e | -2.7369 | -45.4226 | 2025-10-28 00:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| bf9eafbc-2ade-395e-ab25-78969a0ec62c | -4.4602 | -43.6569 | 2025-10-28 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b4db437f-288b-34ad-8594-f8632f84b8ff | -12.629 | -45.0749 | 2025-10-28 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a0207a28-770b-3128-b473-2d98407ddc4b | -7.965 | -45.509 | 2025-10-28 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4bf40aee-adb2-3bba-a91d-7eefdd43670d | -7.9644 | -45.5543 | 2025-10-28 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| f72720ef-a4fc-3725-830f-a006fbd1ef88 | -2.737 | -45.4002 | 2025-10-28 00:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 15329b56-f432-3998-aa10-eae2041fa04d | -7.4539 | -49.4232 | 2025-10-28 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| af4ff981-4abb-3bb8-b309-5286bfb39ee0 | -5.8572 | -46.4459 | 2025-10-28 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ed5eee74-e834-3a92-a549-85868db0542a | -4.4604 | -43.6337 | 2025-10-28 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9030ab95-8be5-317c-814c-b421866657d5 | -7.9835 | -45.5298 | 2025-10-28 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ac568282-27cd-37cd-a814-c0bd4814812c | -10.9216 | -50.2571 | 2025-10-28 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |


[Clique aqui para ver as próximas entradas](README3.md)
