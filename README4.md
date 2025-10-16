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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1893bce1-fdce-3545-b416-4d911a3ca9c3 | -4.0976 | -48.0144 | 2025-10-16 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 3d147986-eaf8-3726-843a-ee293841e996 | -12.6805 | -43.4235 | 2025-10-16 00:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 6c739725-8eb2-3379-b16d-b804a892791b | -5.4762 | -42.9367 | 2025-10-16 00:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| b9fb3a2e-f71d-341e-97c4-44208417efdb | -4.3872 | -43.406 | 2025-10-16 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 7e6a1892-84bf-396f-aa51-f7ef44a5b23c | -10.8856 | -48.7923 | 2025-10-16 00:50:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7bc58047-5dae-38b6-8a83-c2d7c6456e6d | 1.8217 | -55.7629 | 2025-10-16 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| afb0af53-dd8b-361b-897b-b15aa8076584 | -7.9628 | -44.1362 | 2025-10-16 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 1586dcfa-19b7-359d-9190-7f0f763918ec | -4.0976 | -48.0144 | 2025-10-16 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| f966e8de-3455-3558-b5e3-05202baad243 | -4.35 | -43.3849 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 2b674709-03ec-37b5-9645-6d9e2e1c4cb7 | -5.4762 | -42.9367 | 2025-10-16 01:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| b7937bee-840f-30a3-86eb-7677070cbc14 | 1.8218 | -55.7431 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 260b7426-4e87-3cf5-a624-6614c3151774 | -2.9971 | -45.391 | 2025-10-16 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 269e8e13-9c42-3a7b-8203-9b33c7582838 | -4.0974 | -48.0361 | 2025-10-16 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6082edc2-8174-3008-a37a-42745ebee9d2 | -4.5227 | -45.4108 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 16041972-b269-33c9-8e31-1ab042228042 | -5.4764 | -42.9132 | 2025-10-16 01:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| ed7eae46-9e2d-3248-9269-d76238265974 | -3.0158 | -45.3679 | 2025-10-16 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |
| d2187512-e74d-38ab-ba61-d4af14f0f137 | -8.2464 | -44.0832 | 2025-10-16 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 77739cb6-8806-3d64-a4a9-1cf13be19f09 | -4.9293 | -45.8811 | 2025-10-16 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7ec86987-99e8-30f7-80f9-64ef0e70a111 | 1.8401 | -55.7232 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 09e326c8-53dd-3929-b30c-69e8d7649766 | 1.8401 | -55.7429 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d83637b1-263a-3ab3-b672-ce7b3b45bb9f | -7.9442 | -44.115 | 2025-10-16 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| eb847876-f665-3124-b2c0-63fa8932aa8f | -9.2255 | -48.6 | 2025-10-16 01:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e725c896-642e-34ba-b6e4-eff65c40c060 | -12.6801 | -43.4474 | 2025-10-16 01:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 1f5c3006-1ead-3a2b-91ba-bc8bbd5e62a1 | -7.4706 | -42.7605 | 2025-10-16 01:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| adfde9b3-263f-3c33-a0fc-adbc0685a83d | -12.6612 | -43.4268 | 2025-10-16 01:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| b23560b1-094b-3224-8e4b-c9a77d3ac965 | -4.4854 | -45.4128 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 25dad6ff-a78d-3cde-bce3-d1736b4c1c3d | -5.496 | -47.308 | 2025-10-16 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6da84e25-23e8-3436-9fb5-e17c9caf1ec3 | -8.265 | -44.1044 | 2025-10-16 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c05d931a-75b4-3c54-a4e7-dc42bac361ad | -12.6805 | -43.4235 | 2025-10-16 01:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 249.0 |
| b003bbed-7b99-3580-819f-ca9828bd6f0a | -4.4059 | -43.4049 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3ea0ed19-56a7-3e98-9c19-e891e6ddbd91 | -9.3602 | -46.9368 | 2025-10-16 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f87b8ffb-1581-33dc-b19d-6ce40ce65d61 | -8.4714 | -44.1978 | 2025-10-16 01:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4a5166bf-28fb-3ae8-abf2-f35e0136582b | -9.3599 | -46.959 | 2025-10-16 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 47762400-afaa-3d26-a4a6-aad2e2e80e30 | -4.1161 | -48.0136 | 2025-10-16 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 3a1eaa0c-4c4f-3243-bffe-a49d4a37f6c8 | -4.3874 | -43.3827 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 522.9 |
| 7a4e6d5c-00f0-3f48-8169-809e614e9dce | -7.9439 | -44.1381 | 2025-10-16 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 4c446dc5-b0f4-3e23-9f4c-c8e4d379f8e7 | -4.5041 | -45.4118 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 100.5 |
| da2234be-7d7e-3134-8779-9cc697fa6b93 | -4.4061 | -43.3816 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6a37889f-332d-3786-9f02-3bb825b175cc | -7.4894 | -42.7586 | 2025-10-16 01:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 5ab4e977-cf75-3fe7-bc49-c9045c06697d | 1.84 | -55.7824 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 6fb5427b-381c-3093-a2b4-8c2d8f358618 | -4.5042 | -45.3893 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 94.0 |
| cad6ba3f-0e0e-33a4-84df-8f5d4f80efe7 | 1.84 | -55.7626 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6abed639-16b6-312f-a9e3-2f51075e8a06 | -8.2653 | -44.0812 | 2025-10-16 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 271cacf1-66dc-3c5e-8273-7a52626a2036 | -8.247 | -44.0368 | 2025-10-16 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 577b72e5-0fa2-3d05-b8b4-3482126610c7 | -4.3498 | -43.4082 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f0e37805-92d4-3af0-b514-6c3577fe466d | -4.5229 | -45.3882 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f7e512da-7e4c-3654-94d7-ea82f8719964 | -4.4856 | -45.3903 | 2025-10-16 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 41f95ac5-ac70-3335-b9df-c86327361669 | -8.4717 | -44.1746 | 2025-10-16 01:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 72df7ffd-9b55-3938-9b17-bc7d458c40b0 | -5.5148 | -47.2849 | 2025-10-16 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 07323ac9-b7f5-303e-8c27-0dd38da4c3fc | -4.3685 | -43.4071 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 413.0 |
| cb5672e2-059c-3f9f-9093-9640894c09b0 | 1.8032 | -55.8815 | 2025-10-16 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2b733cbd-0d6d-363e-985a-0e620258d5c1 | -3.0157 | -45.3903 | 2025-10-16 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| df04ca1f-b4ea-3c1f-a063-698fe1db9555 | -5.4575 | -42.9381 | 2025-10-16 01:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 3a37fae0-aa93-3ded-ad1e-10bf1917894c | -4.3687 | -43.3838 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 531.8 |
| b17d60de-9503-360f-8c24-33bdabdf1aa7 | -7.9631 | -44.113 | 2025-10-16 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b4602d34-f0ad-38d1-b3d2-d14033225e49 | -9.2398 | -63.2489 | 2025-10-16 01:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 4cb47619-599a-3059-9b28-1a22516ff20a | -10.133 | -44.5777 | 2025-10-16 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 67442d49-89d4-31d1-bc0c-d498e66a6bf6 | -4.116 | -48.0352 | 2025-10-16 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 84a7f586-7082-30e3-8694-2336cfa494d3 | -5.7863 | -46.005 | 2025-10-16 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 61c42127-707a-32f0-b3fa-9a991313e32e | -4.3872 | -43.406 | 2025-10-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 515.0 |
| 1e7f46ab-29f8-3f28-8838-a9902efc27ee | -8.4528 | -44.1767 | 2025-10-16 01:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8c4b9a86-9725-3424-934d-f4197f6da0a7 | 1.8217 | -55.7629 | 2025-10-16 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 3ed1af24-5089-3d1a-bb66-ebacbc618bae | -5.5147 | -47.3069 | 2025-10-16 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 5b01476e-4783-34f9-8e96-00d37f207595 | -7.9628 | -44.1362 | 2025-10-16 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| e8fc6eec-558b-370a-8012-a2519ff7f451 | -10.8856 | -48.7923 | 2025-10-16 01:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2b9f25ba-0723-30ce-8496-263e74d5e4e1 | -26.81751 | -50.54435 | 2025-10-16 01:07:00 | TERRA_M-M | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 43a21638-6710-3fb1-99ee-ed2d67b22c41 | -29.18517 | -50.11788 | 2025-10-16 01:07:00 | TERRA_M-M | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 143b40ab-f063-3d9b-8e47-0dc4501fb82d | -29.1834 | -50.12637 | 2025-10-16 01:07:00 | TERRA_M-M | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 3be7668b-14be-3453-b006-0c4843c723ad | -29.18582 | -50.14024 | 2025-10-16 01:07:00 | TERRA_M-M | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| 9b68ca28-8acd-3fcf-b102-2a8ead0b77be | -29.19221 | -50.15967 | 2025-10-16 01:07:00 | TERRA_M-M | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0a8cc5f5-35a2-33fe-9ab8-3a3cfb36c531 | -26.81998 | -50.55891 | 2025-10-16 01:07:00 | TERRA_M-M | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| a1b665f2-5959-3f87-b648-98cc1d92bf2d | -29.18751 | -50.13175 | 2025-10-16 01:07:00 | TERRA_M-M | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 26816b45-4096-32d7-89d8-bed01fdf730d | -17.21373 | -56.19753 | 2025-10-16 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 3fe50ba9-2ed2-35a5-b6fd-4b735f9404c9 | -18.5916 | -47.4675 | 2025-10-16 01:09:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 02dfd643-5753-3f4f-bc5e-af019551cc50 | -17.60895 | -46.70133 | 2025-10-16 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 36.2 |
| e41e15e8-3075-3543-ab2b-a71adf1b0f94 | -18.5814 | -47.47485 | 2025-10-16 01:09:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d29bdb5b-7095-30de-98db-106b1dc85a6f | -20.95229 | -47.40327 | 2025-10-16 01:09:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 0e12966c-2ec7-3292-9f1c-2163381bc6d9 | -17.60471 | -46.70899 | 2025-10-16 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3a7a3c17-257f-3c60-b1b4-2434266536a5 | -7.9442 | -44.115 | 2025-10-16 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e1338879-a87c-349c-bdce-6965f38bbb96 | 1.8032 | -55.8618 | 2025-10-16 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 00e45c5b-07e2-34e1-a9c4-a9eb4f87e9e0 | -4.5227 | -45.4108 | 2025-10-16 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| caa36af7-4b33-3a8e-98bf-5f3c5c38137e | -7.9628 | -44.1362 | 2025-10-16 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 8a9bb873-2614-3df2-bcc3-30405e8965d6 | -8.4717 | -44.1746 | 2025-10-16 01:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 8dc2b382-eda6-31a4-8f73-e375e50d8207 | 1.8217 | -55.7629 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7be37c73-4baa-30cf-8abc-4102fc54a059 | -2.9972 | -45.3685 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 66b203b7-3637-3263-b7cf-9e00f44bb096 | -5.8987 | -43.8829 | 2025-10-16 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a74d449e-42e8-3afb-822d-597bffcddf5b | -5.8989 | -43.8598 | 2025-10-16 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4129b1f2-0e58-306c-81ee-386948ea5f40 | -4.3498 | -43.4082 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f8c8628f-db25-3718-b4cc-696580907b83 | -8.2653 | -44.0812 | 2025-10-16 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0a31132b-4997-3948-8a8d-804b17683e97 | -5.8802 | -43.8613 | 2025-10-16 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 92ac793f-58f1-33e7-971b-2b4d23ac6d07 | -8.4528 | -44.1767 | 2025-10-16 01:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ff54a4cf-5183-3571-ab34-9e15f3123305 | -4.3685 | -43.4071 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 276.5 |
| 9890df36-0ba0-348c-a35c-5a88b40991b8 | -5.4764 | -42.9132 | 2025-10-16 01:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 655e0b20-bfb2-33c3-8ff2-9e619d679d60 | -8.265 | -44.1044 | 2025-10-16 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dae3668e-fd92-3fc9-b10e-a39e42c1f88e | -8.2458 | -44.1296 | 2025-10-16 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 27c80b9f-3657-3a52-9d29-fa3137e77a8f | -5.7861 | -46.0274 | 2025-10-16 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6519977d-658c-39b7-a6e8-23adcd16524f | -10.8856 | -48.7923 | 2025-10-16 01:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 51dc3d11-b180-3458-8212-0bc883f5ab2e | -2.9971 | -45.391 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 94ca5c5e-bc9c-3981-aa91-5fc6b38d9be2 | 1.8401 | -55.7232 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| cb1636d3-9885-36b3-85aa-ed13dc1643e7 | -11.7601 | -61.0743 | 2025-10-16 01:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README5.md)
