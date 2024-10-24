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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded4cb69-7f65-321c-93a7-92df82d287ea | -12.15938 | -46.99656 | 2024-10-24 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ecfc76f0-3d24-3bb3-b1d1-954951154e66 | -12.15592 | -46.99611 | 2024-10-24 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edbbb7b3-0e4b-3589-b2b0-2bb2da333554 | -12.15538 | -46.99976 | 2024-10-24 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a5676e0-71f5-3915-9398-4a1cb76b7870 | -12.15308 | -46.99158 | 2024-10-24 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0c5e25-e31e-3db0-a04c-7d3170261766 | -12.15248 | -46.99562 | 2024-10-24 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83f405c7-3901-3501-9876-83dd0e8760dc | -12.05822 | -46.70794 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4812acb-2b29-3d40-b46a-0bf3d877bdf8 | -12.05416 | -46.71128 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8b9d504-6d59-3d4d-8504-791f305fd313 | -12.05069 | -46.71074 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48707de9-baba-39f2-b0a5-dad1a449bb4b | -12.05011 | -46.71463 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1869c76e-1e85-32a2-b594-1e2d685d7d52 | -12.03797 | -47.79929 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bef9823d-1cf6-33a2-bd22-39d4425336cf | -11.98528 | -47.15226 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 347c4bde-b870-32b4-9fa2-3e40d05eacc2 | -11.98187 | -47.15172 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1cb7715-902c-324c-b46b-86ab7425ffc0 | -11.94419 | -47.56453 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d94d5a7-39b0-36df-865c-dd4f59a187b0 | -11.9427 | -46.58621 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 641c069c-8c3e-3873-b33a-5271542a50c6 | -11.94179 | -47.48883 | 2024-10-24 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52affa54-79c1-30d7-b30d-2964c8e6cf70 | -11.93571 | -46.58517 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e2ab218-3090-342a-8fa7-f23d5c46dc4f | -11.82518 | -47.07434 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23776099-2cb6-3928-ab7f-a4ccba251c3f | -11.8246 | -47.07813 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a69d9d92-6bd8-30a4-96c7-20ae56a1a392 | -11.82175 | -47.07382 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 511219b8-2b2c-3613-a40e-d1e09a170b7f | -11.82118 | -47.07759 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 72a2f23e-7c0b-3619-ad15-7bb75345321b | -11.79094 | -47.06909 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e5d7779-e032-30a0-ad14-6fdb4f1b6a34 | -11.78751 | -47.06856 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e89b347-7bc1-3280-93c5-218954a747b0 | -11.78695 | -47.07235 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84bea5fd-5fb5-3835-a8b7-2ef2253dab34 | -11.78409 | -47.06802 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f63902c8-cb94-37a8-bd6f-3d9bdc1bcc0f | -11.78353 | -47.07181 | 2024-10-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 661fe776-bbd8-3b0e-9a42-ab5f4f1b2eb7 | -11.47294 | -47.06384 | 2024-10-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18d5a0a4-6312-35d4-8f92-0ca1f7258de5 | -11.47237 | -47.0676 | 2024-10-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95f313b6-ad94-392d-9d6e-8ec1ce1f3a27 | -11.31258 | -47.58715 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1466c9c-861e-3207-a8a0-b6c7dfec8300 | -11.28236 | -47.58237 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03129e14-b3bc-310d-bc4a-af55781a4b99 | -11.15943 | -47.27928 | 2024-10-24 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e118268b-7ca2-3e57-b14c-f55b40bb3e2e | -11.09623 | -47.51248 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1de37071-49a8-3b44-995f-4e2614ec9294 | -11.04285 | -47.63723 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf8e79a-65a1-3233-82c6-299fa3194543 | -12.99635 | -47.16314 | 2024-10-24 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c14b67b6-af01-3be6-b225-5df07a9cb105 | -12.64432 | -47.62252 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3659f8d-d9c2-308e-a13d-a7cb6e98f913 | -12.52407 | -47.83752 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86033c74-be5b-3c6f-adde-bff0d3a80892 | -12.37978 | -47.32687 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a74353d-5af7-363b-af37-46cf59c37b78 | -12.26916 | -47.64087 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 381a54a2-1c32-302c-9dac-85949cd8eea3 | -9.24282 | -48.32695 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52b1948d-bff5-3119-9ba5-df993b568e2d | -5.84766 | -47.28387 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a5eaa7f2-28ef-3e67-8b0e-b89f90729589 | -5.84712 | -47.28733 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e8ca204-3615-3b65-901e-7e52ae489ffc | -5.84436 | -47.28336 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e37e6f00-036c-32dc-b689-8ebe37f55879 | -5.84382 | -47.28681 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54719d5b-9927-32a5-b857-ef236629d229 | -5.84105 | -47.28284 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 49aef573-4eee-3059-9cec-96022ae5238b | -5.70191 | -47.62812 | 2024-10-24 04:34:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de6267c1-bbb8-390f-8444-420172eaac21 | -5.70144 | -47.3458 | 2024-10-24 04:34:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0130235e-d602-32e5-a55d-1c686502d804 | -5.7009 | -47.34925 | 2024-10-24 04:34:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2527fb7b-0bb4-392f-9d78-8f742d8f3ed6 | -5.69814 | -47.34529 | 2024-10-24 04:34:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22fb03f7-0384-3752-81ff-258ae0802860 | -5.69484 | -47.34478 | 2024-10-24 04:34:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d5f2056-93cb-3a8e-a352-756536511462 | -5.65096 | -46.97306 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e8b1626-89ef-31ea-beb1-40a9a02741c7 | -5.64764 | -46.97254 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7cc3d2c1-abf0-3530-842b-3fc83d20751d | -5.6471 | -46.97602 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 35d09b76-fcfa-3947-a815-9d4f972383be | -5.64433 | -46.97203 | 2024-10-24 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6d3be5f6-a211-31cb-994a-cfec5b0ef009 | -5.44766 | -47.68299 | 2024-10-24 04:34:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 52bfa8c0-a9a8-3df4-8687-34761955c080 | -5.4449 | -47.67904 | 2024-10-24 04:34:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d7aca71e-51fc-3a4d-86de-de961352f25b | -5.44436 | -47.68248 | 2024-10-24 04:34:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 62d2a422-3e6d-3542-a626-f6ad5458a5ba | -5.44107 | -47.68196 | 2024-10-24 04:34:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f57e1470-841a-3576-9748-1ff306f7431e | -5.42968 | -47.53922 | 2024-10-24 04:34:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbea5b88-333a-38c5-9664-e524d852eac9 | -6.46921 | -46.67687 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5369f6fb-74fc-38e9-81ab-a185ca38d421 | -6.52324 | -47.26971 | 2024-10-24 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a8b0208-467e-3ff2-84bc-774a514dc168 | -6.52047 | -47.26572 | 2024-10-24 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ab1f149-e50e-3c8c-93ce-ac7f13426187 | -6.51993 | -47.2692 | 2024-10-24 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c463da5-ec64-3599-b1be-e97a9fae6ced | -6.51138 | -47.03968 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 556a2471-e295-3012-b9da-9715aa0f5272 | -6.51054 | -47.26419 | 2024-10-24 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47639fd6-0242-366a-936e-cb88069fa3d5 | -6.31394 | -47.21579 | 2024-10-24 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d676e56-0cf0-3ecb-8664-b07ac91f55c7 | -6.28574 | -48.13431 | 2024-10-24 04:34:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d69a5de8-75b8-315d-ada2-942b3df3b2e9 | -6.13567 | -47.00586 | 2024-10-24 04:34:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ffa577-1135-335c-9669-c0aa86d7430d | -6.11974 | -46.82452 | 2024-10-24 04:34:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 733f9b3e-298f-37d1-9641-925edd3278c0 | -6.03278 | -47.96651 | 2024-10-24 04:34:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b64ad213-72a1-3003-ae3e-90f9f4370a81 | -7.6379 | -48.25458 | 2024-10-24 04:34:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7573f89e-8dd4-32b8-86f1-51b354782e86 | -7.23873 | -47.50365 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cddfd40c-ec3a-3ef4-b8e7-0eea4d68670b | -7.20061 | -46.91692 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c48c4dd5-038d-32ce-a0c3-195978d9e0b4 | -7.10816 | -47.20479 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99889f7e-b247-33b6-9a4c-159875a848c0 | -7.10092 | -47.18579 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff13da2c-d472-3d70-80b6-3e6f6fc9423d | -7.05271 | -46.94828 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e108d50a-8e21-3dd8-8e13-8c4367cbc0c9 | -7.05217 | -46.95179 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e87a234-f52e-3cbb-99e5-4405a5f7736f | -6.98491 | -47.82137 | 2024-10-24 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc78c9ea-4393-315a-9fc4-ca78394b75f2 | -6.88625 | -46.96878 | 2024-10-24 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54ddabdf-8328-3a03-aab8-02a8094edbba | -6.74677 | -48.059 | 2024-10-24 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 197c8f9d-0693-3639-b050-2725fd1e7b19 | -6.72775 | -47.07006 | 2024-10-24 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c90efe3-1207-3fc0-9c64-1ec4eee37209 | -6.71393 | -47.07147 | 2024-10-24 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47645b73-3f78-3a68-bc87-02636254f54d | -6.71061 | -47.07094 | 2024-10-24 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 070f2b30-cfab-310e-8fcb-50afe341eeaf | -6.63304 | -47.35125 | 2024-10-24 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e93faa9-451e-355a-ae41-954362d7d8c2 | -6.50139 | -47.69135 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c891e708-b6ff-3f25-9522-13b1c5444307 | -7.68604 | -47.31667 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36334567-0cfb-3172-a0dc-392aafb6f0ea | -7.68313 | -47.31287 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13f6816f-ead2-33e7-b22e-b7e2bbdbf297 | -7.68258 | -47.31637 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 514436db-4348-3ad3-8ffa-f3ea01234594 | -7.63419 | -47.82534 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 681f02f2-cb4b-3a52-ba76-112adc606e69 | -7.63375 | -47.67617 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eba4359-382e-3b8f-acb2-954d878f83ab | -7.63089 | -47.82482 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c161d17-7336-3b75-9ebd-c21f1a7a2f97 | -7.60959 | -47.7187 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d30c41e4-e604-36ab-9c34-7722fa223107 | -7.60905 | -47.72216 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a057eec5-2184-3949-8b34-b1b71920cee8 | -7.59317 | -47.0824 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a67167db-82fa-3279-bf8e-afa69d01a599 | -7.59262 | -47.08594 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ae028c6-703d-302e-8c55-a2310912c387 | -7.58984 | -47.08188 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15730fbb-deb1-3b71-a51c-e13829dd202b | -7.58159 | -47.55075 | 2024-10-24 04:34:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc81fdfc-54d4-3ea6-aaae-eefb12bc89bc | -7.57883 | -47.54675 | 2024-10-24 04:34:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01acaf5a-3201-3f0a-ab00-c78e4f7c3e79 | -7.57829 | -47.55023 | 2024-10-24 04:34:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f84fa0df-0417-3ac1-b390-6b4884151afd | -7.51584 | -48.07959 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adb42c69-828f-3135-a50e-9fb713d0be47 | -7.51308 | -48.07561 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bfaf78e-da0e-3e81-b504-c22dc1f225ac | -7.51254 | -48.07907 | 2024-10-24 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
