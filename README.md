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
| fd53df6d-4ca1-3246-84e7-88e3793b68d9 | 0.2278 | -60.5256 | 2026-02-28 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3dcd182d-2b0b-3e78-8cb3-48901571752e | 0.2461 | -60.5067 | 2026-02-28 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d2b93d34-2bbb-3b2d-b8a9-d34dc8c9239e | 0.2278 | -60.5067 | 2026-02-28 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 468925bc-7eae-3766-a638-16a2573800fb | 1.4853 | -60.9174 | 2026-02-28 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 9b2f0296-e923-3f9d-aaea-7a43dd6dd7cb | 0.2461 | -60.5256 | 2026-02-28 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 7b7a036b-f0c9-3479-b445-327f3e5040d8 | 1.8681 | -60.914 | 2026-02-28 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 942f1f3f-70ac-36ec-b41f-bb61eff01ab8 | 1.8864 | -60.9138 | 2026-02-28 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| f80566d9-e9de-3263-a056-bdfeffe1ea03 | 1.4853 | -60.8985 | 2026-02-28 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.7 |
| e2fe878d-07a4-3a06-8654-ebeb116c6667 | 0.2278 | -60.5067 | 2026-02-28 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8bf45047-e064-3feb-86f8-125965dccb5a | 1.4853 | -60.8985 | 2026-02-28 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8b8ae39d-3c74-3778-8d80-022b9461f784 | 1.4853 | -60.9174 | 2026-02-28 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 4fb13ca9-df93-34bf-8e41-45d118f695c0 | 1.8681 | -60.914 | 2026-02-28 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5d3ec9e2-c64c-3ed9-a117-84032019c8b8 | 0.2278 | -60.5256 | 2026-02-28 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d8e07221-c273-30e0-aa99-a38633860a67 | 1.8864 | -60.9138 | 2026-02-28 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 866daa90-3914-335c-97ac-09e78db47dcc | 1.8681 | -60.914 | 2026-02-28 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| d37a2990-e5e4-3089-a3f7-6895fef8615a | 0.2278 | -60.5067 | 2026-02-28 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 030602de-b0e8-3187-ba17-cd6190387de2 | 1.4853 | -60.8985 | 2026-02-28 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 958b5a5c-f716-3bbb-904f-4d245aaa6a6d | 1.4853 | -60.9174 | 2026-02-28 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.3 |
| f468bec7-a49e-3c6d-98a8-f9ac364bbf62 | 0.2278 | -60.5256 | 2026-02-28 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 33.9 |
| f3fab2c3-f1ce-3828-9942-e91daa5fc615 | 1.8864 | -60.9138 | 2026-02-28 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ac918856-a4dc-32e5-888a-9746e422f092 | 0.2278 | -60.5256 | 2026-02-28 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c129eeb2-8900-36c8-b52f-74e8c91cf936 | 1.8681 | -60.914 | 2026-02-28 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.1 |
| d9c9cede-0495-32ca-86b2-4fdfb9443907 | 0.2278 | -60.5067 | 2026-02-28 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7808a780-0861-3334-80f6-75d9041a19a5 | 1.8864 | -60.9138 | 2026-02-28 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6c422c2f-6d25-33cd-bd10-9758d425d30e | 1.8681 | -60.914 | 2026-02-28 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| cbeb0ac1-9473-3e29-ab10-948c974f9980 | 0.2278 | -60.5067 | 2026-02-28 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9ea47517-fef6-3237-812b-7930282e48b8 | 0.2278 | -60.5256 | 2026-02-28 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0353eb95-081d-34c3-a8cc-f3b0267ead56 | 1.8681 | -60.914 | 2026-02-28 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ade2eb57-c1be-3272-b597-83c8a73f0b65 | 1.8681 | -60.914 | 2026-02-28 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.7 |
| b59e956a-d205-3fff-932a-1b853d49bd72 | 1.8864 | -60.9138 | 2026-02-28 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 08e57a32-3025-32df-b1c8-e70332b7d174 | -20.51352 | -50.8383 | 2026-02-28 01:02:00 | TERRA_M-M | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 87bad244-ad40-3ab3-82fe-6a7bbf03a12a | -21.22759 | -56.25532 | 2026-02-28 01:02:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 280601fc-c754-31a9-8569-aef9d0efb8f9 | -21.79887 | -52.72463 | 2026-02-28 01:02:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 39e71116-8afc-387a-8944-cbfbe312fc00 | -21.68805 | -56.31616 | 2026-02-28 01:02:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| edbcadd0-07b0-3a99-9c8d-838ca9e079b7 | -21.17953 | -56.49762 | 2026-02-28 01:02:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 62adecd6-d516-39c0-945a-a9c68d5fd7a1 | -21.22618 | -56.24556 | 2026-02-28 01:02:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e7f96a41-daaa-321a-a98c-172c6e3b3c44 | -21.68944 | -56.32581 | 2026-02-28 01:02:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 14f49f4e-7b3c-372b-a58b-2ecccfee8d38 | -20.52609 | -50.8355 | 2026-02-28 01:02:00 | TERRA_M-M | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.7 |
| 8da3b0dd-ef42-3752-9e86-5fdf3abff5fc | -21.6805 | -56.32732 | 2026-02-28 01:02:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38384528-7499-3029-96b8-f510b883fdfe | -11.95291 | -58.73763 | 2026-02-28 01:04:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 004da16a-5c65-3e7a-933d-31c2bdae2a33 | -11.9542 | -58.74673 | 2026-02-28 01:04:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cc224004-2ce6-38b7-b860-763666b963ae | -8.55109 | -64.12676 | 2026-02-28 01:04:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f1c4217e-6108-3b67-9297-ae4024486542 | -8.55274 | -64.13971 | 2026-02-28 01:04:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 93f18ab6-5b39-375a-8123-be513288c3f8 | 1.43635 | -59.95816 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3ff5ded3-2e25-3b2e-a1d7-9e9019729337 | 1.50794 | -59.92693 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 808aa2d7-dac5-3c8f-8b32-0dbeb96d0417 | 1.87683 | -60.92103 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.9 |
| affbede1-5907-3fdc-9862-dfc369efeccc | 1.50514 | -59.94709 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7b2d1c92-8caa-3868-8291-03feaff633db | 1.47821 | -59.93312 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 9d136e44-2813-39a5-8960-151ae6346518 | 1.48764 | -59.93447 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 15b7e0b6-ae8b-3577-b969-cd6675a015e1 | 1.49709 | -59.93574 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d108fa53-0152-3659-ba9a-8905cd2860db | 1.4796 | -59.92299 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 3c89a4df-9dad-373d-a8e8-f9a79bb32017 | 1.4999 | -59.91542 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f6c460d2-ea8d-3a0a-b54a-156a06c3d4c2 | 1.50654 | -59.93701 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 16716c94-a3e1-34f0-b055-719a7e915248 | 1.46878 | -59.93171 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fffe7e58-0657-3137-931a-3864b3bc5b02 | 1.48905 | -59.92425 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 4920b2ba-acfb-3740-a85c-bff26caaaba7 | 1.59236 | -60.44338 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a932d54a-b11d-3abc-8010-0ff195df2e04 | 1.8781 | -60.91175 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 92a0889f-f17a-3615-af6c-3afbe3cef411 | 1.516 | -59.93825 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2d77767e-ace2-36c2-82d0-ba75ff191c5b | 1.47543 | -59.95339 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0394a8b5-579b-39df-be1d-9aa0bc077d93 | 1.49045 | -59.91405 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 09aea347-be7e-363f-9812-2b1a4b8aa8ea | 1.48209 | -60.91062 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5903ee1c-20c9-3ce8-a7a7-b98ba033e2f4 | 1.43021 | -59.96114 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d3992cd-c7aa-3b87-8f96-7955366bbe2f | 2.11404 | -60.80452 | 2026-02-28 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff362759-080e-322f-8818-e033e73cd9f8 | 1.47682 | -59.94324 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0702d831-d758-3f3c-a30c-5d5b72fb6bbe | 1.4985 | -59.92558 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 89edff6d-b839-37ed-8ec2-cde48ada125f | 1.48337 | -60.90141 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e29770c4-e462-312f-b98c-c76ea1ba96a4 | 1.43161 | -59.95111 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c32af0cb-6a6f-3d48-b958-58520b57c4de | 1.48626 | -59.94453 | 2026-02-28 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 112441fa-8fc1-3b9f-beb7-7b1064f2aa83 | 4.80181 | -60.14538 | 2026-02-28 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 37a8429c-4d1e-3f42-836a-4782844e61fb | 4.08954 | -59.89781 | 2026-02-28 01:09:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 427a1b26-9822-3efe-b232-b5b001f5de37 | 3.42069 | -59.861 | 2026-02-28 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 59a840c6-b3c9-3117-8ca2-01e23c237777 | 3.37504 | -60.54802 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d85dfb37-cd48-3bf7-a10b-31bc0abd3e78 | 3.48348 | -60.68541 | 2026-02-28 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f46d4da-a8b0-3849-a935-e03fe659160f | 3.04178 | -60.2942 | 2026-02-28 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c7a60c7a-d0be-3a88-8fe4-2238e13eda92 | 3.38861 | -60.56632 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b2da652-83c9-317d-9dbb-f9f92fac4500 | 4.80989 | -60.15836 | 2026-02-28 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 448a7b81-a9d9-390c-bc50-ec4c7017cdfb | 3.38193 | -60.54523 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78950cba-da3a-3737-a07b-9df399175acd | 3.374 | -60.60444 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de3edf90-5447-3c7e-ae16-3a16b3fffefe | 3.04793 | -60.2911 | 2026-02-28 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5a22d4da-1433-3bcb-9661-392f32e875de | 3.37268 | -60.61432 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 3fb27cb7-8641-3f74-8da0-a9b5f897db18 | 3.04319 | -60.28407 | 2026-02-28 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1c6e6b08-a273-3677-aa4a-33fc3a384679 | 2.87918 | -60.5989 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98e0d727-4f31-36d9-98f4-d224ed911252 | 4.80321 | -60.13506 | 2026-02-28 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5c4ef4f-045f-38df-a4ec-f9e24410cfd4 | 3.49671 | -60.72701 | 2026-02-28 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 10d0ce7b-da24-3e46-8c4f-cede87ee8277 | 4.44135 | -60.76028 | 2026-02-28 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89611649-36d1-35bd-86e6-adc48d9ac48d | 3.36549 | -60.617 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a894ab88-f212-3af3-ba0a-771aa0a165ba | 3.36686 | -60.60714 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 51be12f4-12ae-3f87-ae66-66fd258099a7 | 2.87785 | -60.60864 | 2026-02-28 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a1f56f3-c858-340a-9a97-f88b0844111a | 1.8681 | -60.914 | 2026-02-28 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2e0277ed-bd96-39c3-ae7f-b8e2a6e1cdc1 | 1.8864 | -60.9138 | 2026-02-28 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 8570a35d-9817-34a0-a884-1611c8ae396b | 1.8681 | -60.914 | 2026-02-28 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c1e24c11-7dde-34ef-9631-8ceef7b36426 | 1.8864 | -60.9138 | 2026-02-28 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| ab7d7d26-3493-3b09-b187-309f08110cfc | 3.3655 | -60.6088 | 2026-02-28 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 659d155b-ff1f-3d52-8b6b-583cd47f36b9 | 1.8681 | -60.914 | 2026-02-28 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 77b38435-60c7-32db-978f-c0d296cc63ba | 1.8681 | -60.914 | 2026-02-28 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e8cf9d5c-fd6c-364f-b853-50b204b4fb2f | 1.8681 | -60.914 | 2026-02-28 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| f9e31ad3-a17a-3ef1-8180-7ef7167dc54b | 1.8681 | -60.914 | 2026-02-28 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| b0491217-bff1-35b1-bc51-597257a107be | 1.8681 | -60.914 | 2026-02-28 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.1 |
| dcee4f7e-6a0f-3a95-b0c9-384d5d23876a | 1.8681 | -60.914 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| ff563bd8-c244-3659-a771-7181dbc52c36 | 1.4681 | -59.9309 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |


[Clique aqui para ver as próximas entradas](README2.md)
