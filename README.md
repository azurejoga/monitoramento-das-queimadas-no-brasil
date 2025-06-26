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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e4e4545-1f55-3d57-aac4-06c44c165d5e | -6.1977 | -48.0699 | 2025-06-26 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 58823170-8dac-3cf2-9a8d-df20fb28415b | -13.0408 | -48.825 | 2025-06-26 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 2a561c17-171b-360f-afe6-74f07e95d222 | -13.0985 | -52.303 | 2025-06-26 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b3573fbd-991e-301e-91c6-68ebd498ccf4 | -9.1213 | -49.4313 | 2025-06-26 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 4646c9c9-5a88-3392-b954-dac61b0c47bb | -6.1975 | -48.0916 | 2025-06-26 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7c481284-c2c3-3d54-82c5-bd5ac67ddf91 | -7.2028 | -43.0936 | 2025-06-26 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 2dafede3-83f6-3ba3-952b-acc09f8a1b6e | -9.4993 | -56.0988 | 2025-06-26 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 20e6580a-326a-36b4-92fa-88b45a2d02c9 | -11.0644 | -55.3757 | 2025-06-26 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 5afe0047-c4d2-3fbf-b8bc-bedc902a72de | -9.5178 | -56.1175 | 2025-06-26 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 86d1dd44-3c35-3b13-a102-80dd3248d05a | -6.1791 | -48.0712 | 2025-06-26 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 74ee141c-6b9e-35b5-899a-9b95f158e746 | -9.121 | -49.4528 | 2025-06-26 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9e0da9c5-650d-3ba3-93cc-401de6d7ea2c | -4.524 | -48.0593 | 2025-06-26 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 714ba89e-4164-3673-b0b1-a4a3c37bb86e | -4.5427 | -48.0367 | 2025-06-26 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| d31abd05-7be0-355a-9ad4-2b79d53936af | -9.518 | -56.0975 | 2025-06-26 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1fa43e2b-4d5a-3069-ae13-b2fb0860d551 | -4.5242 | -48.0377 | 2025-06-26 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 662c59c2-b8cf-3a88-a070-fc7fc4571b97 | -6.1789 | -48.0929 | 2025-06-26 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 20d15168-cd1b-3f73-bd7a-f8a40e27476b | -11.0832 | -55.3741 | 2025-06-26 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1521af9b-d9ce-3c06-8ead-00c4d8802a91 | -13.0988 | -52.2819 | 2025-06-26 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 34752940-bc4e-3270-a722-35cfe83501de | -4.5426 | -48.0584 | 2025-06-26 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 19f18459-0e9a-3bb4-84ac-cde24149254a | -9.121 | -49.4528 | 2025-06-26 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0e6b55cc-6c3f-3878-afd0-140a5c6f0f87 | -4.524 | -48.0593 | 2025-06-26 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 204.8 |
| ad5c098d-da31-3cca-9bcc-fc5003de4270 | -4.5426 | -48.0584 | 2025-06-26 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 81243ae1-af38-3cbe-82fa-356701b43335 | -4.5242 | -48.0377 | 2025-06-26 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 874efc52-80b9-3fde-aeac-a2c033557979 | -13.0985 | -52.303 | 2025-06-26 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6424fcc0-a440-3098-9b0b-5234ebdd80e9 | -6.1975 | -48.0916 | 2025-06-26 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 17b9e950-a521-364a-a36a-47dcdc1af1dc | -11.0646 | -55.3555 | 2025-06-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c0721930-cbcc-32c2-b90d-9839cabc2260 | -9.518 | -56.0975 | 2025-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 097f5ab4-0c16-3a43-b6ac-c903ab1a3d5a | -4.5427 | -48.0367 | 2025-06-26 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 227e96ba-e509-3984-a436-8a6760f3fb81 | -6.1789 | -48.0929 | 2025-06-26 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 75bb5afe-091f-331a-b391-9e24ba6b7087 | -9.4993 | -56.0988 | 2025-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b7e66791-fbdf-3125-9a4a-d03f3cacb1e6 | -6.1977 | -48.0699 | 2025-06-26 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a1cbdff1-833d-32cd-bcf4-5dad2b8288da | -11.0644 | -55.3757 | 2025-06-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| be02d300-efcf-3307-a2b9-4ef9bc59608c | -9.5178 | -56.1175 | 2025-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| dede4e1b-c832-3fe5-a159-71eb680bea33 | -6.1791 | -48.0712 | 2025-06-26 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 257.3 |
| bbceb2f8-2bfd-36dd-8378-26bce740a46f | -13.0408 | -48.825 | 2025-06-26 00:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| fd7165ea-5908-3452-ac38-3730beea0969 | -9.1213 | -49.4313 | 2025-06-26 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 6e208f00-7f67-3686-84fa-3b92d72e7a6f | -9.4994 | -56.0788 | 2025-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c422c7af-ae4d-3056-b0b7-e250063b142d | -11.0832 | -55.3741 | 2025-06-26 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| de14171e-f77c-3ab1-9b0e-ec574eae3b08 | -4.5427 | -48.0367 | 2025-06-26 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 71df6847-3f93-3cf9-8b4a-37ff0272d096 | -4.5242 | -48.0377 | 2025-06-26 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| b56984e8-dce2-3245-bd06-45683d88638e | -9.4993 | -56.0988 | 2025-06-26 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 1b1e2ae5-3a59-3598-9575-58a5de218977 | -9.5178 | -56.1175 | 2025-06-26 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b5d3fd49-84b3-3f09-988b-e4392aeb75b0 | -6.1977 | -48.0699 | 2025-06-26 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 39d35a35-c73f-3d82-ba78-6a0a1b7d1572 | -6.1791 | -48.0712 | 2025-06-26 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 57b912f3-a415-3510-990e-810eb144225c | -13.0408 | -48.825 | 2025-06-26 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3862bfc0-435e-37fc-a9bd-66b5d9ab3651 | -13.0985 | -52.303 | 2025-06-26 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bbcaef08-a55b-3335-9ad6-a988cea3c869 | -9.518 | -56.0975 | 2025-06-26 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e6f88f90-402e-324c-9e07-f9662b85dd40 | -11.0644 | -55.3757 | 2025-06-26 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 5ca25288-c300-3bba-9920-c19687385173 | -6.1789 | -48.0929 | 2025-06-26 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 353bc16f-cde1-3973-9b4a-f16774feefc5 | -9.1213 | -49.4313 | 2025-06-26 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fb2d273a-2413-30d9-b596-a5379ab9a0be | -9.121 | -49.4528 | 2025-06-26 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 18c4a4a7-c8d2-3ea4-b2ed-52f79842648d | -4.524 | -48.0593 | 2025-06-26 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| a12656fd-f234-3830-b763-8bae6067e7a4 | -4.5426 | -48.0584 | 2025-06-26 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 9f800a85-14c1-3a32-8cc8-9a6f775ce525 | -6.1789 | -48.0929 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| ded1761f-01c5-3bf3-b950-815ad132a80d | -13.0601 | -48.8223 | 2025-06-26 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 67f1e156-4b76-3ee1-baef-0f87de45f2b4 | -6.1977 | -48.0699 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e23ba63c-42e9-3625-95e3-5b7a0e44129d | -7.2028 | -43.0936 | 2025-06-26 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| a74d8c48-ba99-3162-9525-f3c9e446914d | -9.121 | -49.4528 | 2025-06-26 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ebc1a6c5-ceb6-3dda-a508-bec6a99fe4ba | -6.1791 | -48.0712 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 282.2 |
| d9e1644f-4474-330a-a93e-b3db2d6bb9dd | -11.0644 | -55.3757 | 2025-06-26 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| d394cb9a-f4a2-3e9a-888f-9f7297df9b0b | -9.5178 | -56.1175 | 2025-06-26 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f1f4e353-5f62-33a6-a35d-efcc5c3a71b6 | -6.1975 | -48.0916 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f3057d6a-de57-33a4-9946-5b96445fc6b5 | -9.4993 | -56.0988 | 2025-06-26 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 530ad776-b904-30d3-b978-b4943693fc74 | -11.0832 | -55.3741 | 2025-06-26 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2b652bc2-0620-3032-808c-875d96f7707d | -4.5242 | -48.0377 | 2025-06-26 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 081cfba0-6aa7-39a1-8de0-ba9b3c727b33 | -9.1213 | -49.4313 | 2025-06-26 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 254b31bc-7777-3995-87ed-81a1b05763e6 | -9.518 | -56.0975 | 2025-06-26 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 22b98cfd-6db2-3d1c-9852-a7bb3040030d | -6.1602 | -48.0941 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6a292c70-2e27-3150-9efc-3e0ca5bb6768 | -13.0408 | -48.825 | 2025-06-26 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2642fc1f-2d1c-3a6a-b473-0994805c6347 | -4.524 | -48.0593 | 2025-06-26 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| b85ced72-9097-3f22-93b0-c8e8b9c8db74 | -6.1604 | -48.0724 | 2025-06-26 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 226adcc3-85a6-3b7a-900c-8b76db8d5edd | -11.0644 | -55.3757 | 2025-06-26 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 14d54235-014d-37bf-8c79-70f55848a5b8 | -6.1791 | -48.0712 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 307.2 |
| b3189be1-c71b-32b8-b544-7efc318205af | -9.1213 | -49.4313 | 2025-06-26 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| f2f05f3d-5d41-3104-87c4-da5596e1a3f9 | -9.518 | -56.0975 | 2025-06-26 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 00ee6db8-fdef-3640-be81-49f196b86f5e | -11.0832 | -55.3741 | 2025-06-26 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9b5a0242-3a04-3d23-babd-fe37b407e64d | -4.5242 | -48.0377 | 2025-06-26 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| a264b0da-3a7c-3d18-be2c-a0b5ac6b415d | -6.1789 | -48.0929 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 31e40dcc-85f4-3937-9897-1236f0595cb0 | -13.0601 | -48.8223 | 2025-06-26 00:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 13255e78-33fa-3fec-987d-3c2c477f07d6 | -13.0408 | -48.825 | 2025-06-26 00:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5457deeb-cd1f-3ed3-b578-99c2db229397 | -4.5426 | -48.0584 | 2025-06-26 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dbc6961b-dd78-3fcb-afcb-0c0c7887ef00 | -9.4993 | -56.0988 | 2025-06-26 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 815ee814-4cc2-3ac3-82be-5126fd963ba0 | -9.121 | -49.4528 | 2025-06-26 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f08e066f-e295-30f0-b6a0-f5e89165c52c | -4.524 | -48.0593 | 2025-06-26 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 4d3d26ba-c868-37fe-a1f6-8340c5cf64d1 | -6.1604 | -48.0724 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f30b8ae2-1623-380c-b6d9-8b1e2ef06cfd | -6.1975 | -48.0916 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f73678aa-a069-3f55-a3eb-8762517a495d | -6.1977 | -48.0699 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 01fda71f-1cff-36d6-a64c-a0f7d58efd02 | -9.5178 | -56.1175 | 2025-06-26 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5eede8f4-c035-350e-8b95-6b25973e74a1 | -6.1602 | -48.0941 | 2025-06-26 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 67e3adc7-cc90-3dc9-a414-06b634eb8de9 | -6.1789 | -48.0929 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 9f3376c3-d3ff-38dd-80dd-7ed430d2ffb8 | -4.5426 | -48.0584 | 2025-06-26 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 79db4e88-d463-3314-8efe-8ebc84e8391a | -7.2028 | -43.0936 | 2025-06-26 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.2 |
| b7934c67-9f5f-3a5f-bfa8-f064b7110afc | -4.5242 | -48.0377 | 2025-06-26 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 67d40098-4041-3a40-a314-19c97389aeaa | -6.1791 | -48.0712 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 422.9 |
| 4d15e72e-24dc-3379-8aab-563ccfc91054 | -9.5178 | -56.1175 | 2025-06-26 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 11a3a12f-f6e2-380a-a443-60a8674e9ba4 | -6.1604 | -48.0724 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 698da6f3-d156-38ad-a972-1cc68519d6b4 | -13.0408 | -48.825 | 2025-06-26 00:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 41ebec77-f0eb-3dce-a9a1-ff218180e1d1 | -6.1792 | -48.0494 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| e96fcc58-c626-3cf5-a8a6-8207ae841a04 | -9.4993 | -56.0988 | 2025-06-26 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4dd3d3d6-eddc-35ba-8bde-87276f615695 | -6.1977 | -48.0699 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |


[Clique aqui para ver as próximas entradas](README2.md)
