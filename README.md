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
| baffe435-fca5-3fc5-b49d-ec022728d79d | -7.2217 | -43.0917 | 2025-06-15 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| f2f8e86a-2995-3250-88b8-f384a1601254 | -13.9254 | -54.6063 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 366.0 |
| 9f7ac5bf-4c8d-37a3-8900-c6c178ed4dfa | -11.0113 | -55.0764 | 2025-06-15 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| b44ae97d-c3bd-3bf0-b4bc-b87fb75adf3d | -10.9167 | -56.8336 | 2025-06-15 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bc6e7251-5334-3607-8cd3-18280ce1bef0 | -10.9207 | -54.7592 | 2025-06-15 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c0ac45e4-2196-3050-841a-4a3acec44c51 | -13.9059 | -54.6291 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 3990406c-18b4-3b18-bcae-82be3ff7e7a5 | -7.2028 | -43.0936 | 2025-06-15 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| 107aa047-7f95-3ca1-bdf3-a1989c9847db | -10.9355 | -56.8322 | 2025-06-15 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 7d4290b2-fbcc-3066-9e7e-9b9eb1d2df74 | -13.9065 | -54.5878 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 93e58725-39e1-3ef3-ae01-3d8dd74099d7 | -12.696 | -52.3917 | 2025-06-15 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a77d748e-30cf-3b9a-b846-7abc6809f935 | -10.9924 | -55.078 | 2025-06-15 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 5d51f916-7b63-3da3-96e7-7944199c7d40 | -11.8853 | -54.6722 | 2025-06-15 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 99c0a7a6-e306-3f81-8a9f-6612882589db | -7.2025 | -43.1171 | 2025-06-15 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.8 |
| 0bd07a9b-39a7-32a2-bc0d-146ff31c47a5 | -13.9251 | -54.627 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 1a47608e-2411-349d-812a-0dd4b88c63e8 | -13.9062 | -54.6084 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 276.5 |
| cfc9d400-6757-328a-b67a-e70294fb7b8d | -11.011 | -55.0967 | 2025-06-15 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 98d55cbe-6d7f-3290-b911-cc230f759f81 | -9.4158 | -48.4504 | 2025-06-15 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| f0912b30-b5b3-3c56-9e9d-bca97914af9e | -13.9257 | -54.5856 | 2025-06-15 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0c6a2f29-f4ee-3f21-a537-1915423d2f7e | -11.885 | -54.6926 | 2025-06-15 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 17458640-dc50-32be-a56d-be0eff43665b | -10.9018 | -54.7608 | 2025-06-15 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ad27ae1f-7fb5-3532-bd6f-d2b210d6a46a | -7.2214 | -43.1153 | 2025-06-15 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 98fe6d53-18e4-31f6-9259-9e263f59cb05 | -12.696 | -52.3917 | 2025-06-15 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f632e980-a2a2-370f-900b-8817c9a1ce07 | -7.2214 | -43.1153 | 2025-06-15 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 54b1284b-7cf3-3735-bcaa-c9582d2967c0 | -11.8853 | -54.6722 | 2025-06-15 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fc9b6b25-681b-334a-bda8-c39a3bf408df | -11.885 | -54.6926 | 2025-06-15 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b91a3a14-1086-3cf6-9823-169c45e8853b | -7.2025 | -43.1171 | 2025-06-15 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 185.4 |
| 0637a387-3a1c-336c-ba14-21f75dd5c5c5 | -10.9355 | -56.8322 | 2025-06-15 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9913c0f2-fb71-3d25-8480-49f6a2d1db6b | -9.4158 | -48.4504 | 2025-06-15 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 4518d023-bf0c-3197-be44-0f806f828ec3 | -10.9207 | -54.7592 | 2025-06-15 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| b914571a-170d-3a82-859b-3dff017d5f9d | -11.011 | -55.0967 | 2025-06-15 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bb866838-98f5-3734-a6d5-850231475983 | -7.2028 | -43.0936 | 2025-06-15 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.7 |
| ad398d51-efae-3a46-a8ea-718959378baa | -9.4161 | -48.4286 | 2025-06-15 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 821b5645-be88-3532-9207-7f37aa77bca3 | -10.9018 | -54.7608 | 2025-06-15 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f11ba999-bb66-3a26-835c-71fdd9b930f0 | -7.2217 | -43.0917 | 2025-06-15 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 321868f1-a4fa-38c5-9dac-df212ad0a7cf | -10.9924 | -55.078 | 2025-06-15 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 74ec8e33-3898-3230-a70f-c53e86c2c47c | -11.0113 | -55.0764 | 2025-06-15 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 8b587318-a836-398b-85df-624fa758f65d | -7.2217 | -43.0917 | 2025-06-15 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 831af4e7-895e-379e-a943-0fb77f1a8cd2 | -10.9207 | -54.7592 | 2025-06-15 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 4367812a-471b-3659-a0bb-a673379a0fe0 | -10.9924 | -55.078 | 2025-06-15 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e960c6fa-28a7-314c-9ae5-126beea71e9d | -11.885 | -54.6926 | 2025-06-15 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4a1dfee7-e9dc-3248-86bc-07806e4ecff8 | -11.0113 | -55.0764 | 2025-06-15 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| f01720ce-817a-3a06-9ed1-dc41f6ff43c1 | -7.2025 | -43.1171 | 2025-06-15 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| 378d83dd-d998-3e25-b898-209b3c20ccbf | -11.011 | -55.0967 | 2025-06-15 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ee2e4ec3-e8e6-31ef-809a-d0d4a77116e0 | -10.9355 | -56.8322 | 2025-06-15 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 671dd2f9-9ac3-3b84-9732-858af3010fd3 | -9.4158 | -48.4504 | 2025-06-15 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 8017337c-a98f-3e2b-8575-4b3bb197cbf6 | -12.696 | -52.3917 | 2025-06-15 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fc7ea97e-d34d-35d4-b6b3-99f95b719cd4 | -7.2028 | -43.0936 | 2025-06-15 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.6 |
| 0362be77-bd80-3437-b57b-76d0e1689926 | -7.2214 | -43.1153 | 2025-06-15 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 98999ae8-3477-3fa3-a305-5cfcdcc701da | -10.9355 | -56.8322 | 2025-06-15 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f45070fa-5784-305d-924e-b1f9aa70164e | -11.885 | -54.6926 | 2025-06-15 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7f93fd43-7b45-3411-ae96-efbd2b563ce6 | -10.9207 | -54.7592 | 2025-06-15 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a7b25eb4-dd9f-3551-85ba-4fa213b4b35c | -13.9257 | -54.5856 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 54c17863-c952-30a9-82cf-286e38baaf64 | -9.4158 | -48.4504 | 2025-06-15 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| c7901b7a-5551-329a-b3c8-54c4f271d1c3 | -7.2028 | -43.0936 | 2025-06-15 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 5ddaecdd-ff49-399f-aafa-afa8fd5c3165 | -11.8853 | -54.6722 | 2025-06-15 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 17879ec7-5ca6-3e92-b321-b50d702bab06 | -10.9924 | -55.078 | 2025-06-15 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f3f9cb3a-f90b-3e0f-ab28-6df1f49185c3 | -13.9065 | -54.5878 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a5ed0d32-57c2-33a8-b02a-c921551c602e | -7.2217 | -43.0917 | 2025-06-15 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 849b16ff-3ff1-3ea7-9860-78526c3f79b8 | -11.0113 | -55.0764 | 2025-06-15 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| e0e5167d-1482-3a7e-a9cd-c3a7a550eed7 | -13.9059 | -54.6291 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6c391721-1a84-39c6-a5e7-7a5a1001082f | -7.2025 | -43.1171 | 2025-06-15 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.7 |
| d435dd72-f82f-341c-8c8d-560444d6bb76 | -7.2214 | -43.1153 | 2025-06-15 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 5491c9ca-ebb3-3dbf-8d4d-be15a34b5b60 | -13.9251 | -54.627 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 314.1 |
| e073b7e1-1851-369d-ae06-9a59c244a470 | -13.9254 | -54.6063 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 591.8 |
| a017e3ee-ed96-3611-84c1-e42cda1a470a | -13.9062 | -54.6084 | 2025-06-15 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 411.7 |
| df8eb00a-6114-3236-a646-e50c79e79039 | -12.696 | -52.3917 | 2025-06-15 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 623a81e5-a462-3f50-ba23-ea78ef41fb1d | -21.26229 | -50.29692 | 2025-06-15 00:37:00 | TERRA_M-M | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| e31616fd-678f-3490-971d-a70d05fd163b | -18.39251 | -44.19638 | 2025-06-15 00:37:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a142673-4da2-33b0-b4b0-479e57366f26 | -18.39794 | -44.18966 | 2025-06-15 00:37:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94a38abf-2564-335c-9760-56acae6deb10 | -11.78083 | -47.39444 | 2025-06-15 00:39:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3c0f116-c3af-3188-b1b4-3e63ee624a76 | -7.20449 | -43.12659 | 2025-06-15 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 48bd4ab1-18fc-3307-a1cc-3e7a6e9e8cb8 | -10.91043 | -54.76213 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 30fd4fc5-6758-3d4f-9f04-cdc808c65f5d | -15.40207 | -47.87781 | 2025-06-15 00:39:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6187339f-4885-381f-b4b7-5f8bd15af990 | -10.45839 | -47.95403 | 2025-06-15 00:39:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 568b2d44-e1e7-3618-843f-a0246462dc4f | -10.65967 | -49.36526 | 2025-06-15 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e8b4d6c2-48b6-3e85-bde7-d43889300651 | -10.92614 | -54.78173 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 188fae26-aea5-3b6c-bad8-cd4fa657802d | -9.14314 | -48.97735 | 2025-06-15 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7faf354-16cd-3107-92d4-5b50e0c3d227 | -7.21384 | -43.10756 | 2025-06-15 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.5 |
| 0bf327aa-ec6f-32c4-ba53-66c91a2f2d95 | -9.41995 | -48.44047 | 2025-06-15 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9b8fa86e-74ae-390e-a9f4-ac2cad574d31 | -8.96636 | -47.9743 | 2025-06-15 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 02dd0f17-fced-325f-8db1-c3784f4d93e6 | -10.50632 | -53.5824 | 2025-06-15 00:39:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3da53194-041d-38e4-8092-d7725fa9ac71 | -10.72093 | -46.55643 | 2025-06-15 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cc44907c-a54b-3b55-909c-27bfcccec015 | -7.23639 | -44.16467 | 2025-06-15 00:39:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 67bd6685-90bf-333c-bfd2-263bd852fff8 | -11.89165 | -47.46375 | 2025-06-15 00:39:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36440508-b4de-3da1-8e43-de9aa5468c34 | -12.69564 | -52.40509 | 2025-06-15 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| be1f7b08-b2c9-301b-b7bc-bf172c56bb8b | -10.9236 | -54.76041 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a978a4c6-52fe-3829-ace8-983ebbcfa7ac | -11.87881 | -54.67197 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 14145b74-655b-39ef-a36b-544678efe99d | -10.7223 | -46.56588 | 2025-06-15 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09b8c73e-d09c-3ed7-9b1f-3fa90dac42c0 | -10.74158 | -44.49844 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23023a61-43d8-37a6-ad5d-a19a129709b5 | -10.07997 | -52.74455 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0eac6798-6cf9-3d21-a68c-af71d844686c | -11.87758 | -54.68881 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| c5c060db-ad96-3553-b07e-0628a631bc69 | -10.23563 | -52.24269 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 37d95773-f8a5-3617-999e-10d45ef81ab3 | -10.23395 | -52.22945 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ca8a6ac8-23e4-3d3f-b5bb-4a341428718b | -13.91791 | -54.65783 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 835329ab-571b-3c6e-ada0-cf9e07c79b9f | -11.18991 | -44.48136 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 04be9e01-c818-3af1-837f-dcfb5a3a2ff1 | -6.83483 | -43.40305 | 2025-06-15 00:39:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9e807426-917f-3766-84f1-6ee28fe614af | -15.40971 | -47.86717 | 2025-06-15 00:39:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2babb15f-08eb-3bd3-b8ae-d5c17cb1c4b2 | -11.00326 | -55.08388 | 2025-06-15 00:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 438d6523-c154-3a04-99c6-1a9a1bf0f846 | -8.96511 | -47.96539 | 2025-06-15 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1009e14-9108-3933-bc25-8dfdc497d0bf | -7.20185 | -43.10938 | 2025-06-15 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 244.9 |


[Clique aqui para ver as próximas entradas](README2.md)
