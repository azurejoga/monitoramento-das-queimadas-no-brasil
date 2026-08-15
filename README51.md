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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 718f4bb4-a5b0-379b-b9b1-8f118f3096c7 | -14.4302 | -51.9243 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2de69fdf-941f-3644-a16b-02997a3ac2b3 | -14.4313 | -51.8602 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 51753da9-53b6-3a48-b251-27970321bd62 | -14.4306 | -51.9029 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b36f9792-9d4f-3994-9c81-8b0605e9fb60 | -12.446 | -46.6584 | 2026-08-15 13:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 205.8 |
| de5a196f-0e72-3a99-b19a-ec9345b1d81d | -6.9334 | -43.6333 | 2026-08-15 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 161.7 |
| c187e8be-c1e2-31de-9a74-9af18817cacc | -7.2786 | -44.7091 | 2026-08-15 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 47665927-8b7e-3510-8b27-4ecba0852af1 | -11.9347 | -46.3244 | 2026-08-15 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1ab4acbe-7c50-30a0-943c-10be1d410352 | -14.4313 | -51.8602 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7388f405-be10-3fde-b8ec-f55f4cc9fd0d | -16.1015 | -49.8794 | 2026-08-15 13:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0f44b7d4-d977-38eb-a211-4676fd1524fa | -14.4302 | -51.9243 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| be611a4c-8731-3046-801a-7ded2048c9ff | -16.1211 | -49.8761 | 2026-08-15 13:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8dd1f885-bc88-3886-96fb-786008e81a4e | -14.4298 | -51.9457 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 01abb6a7-1f12-3deb-ab25-25fc63d506d6 | -13.2804 | -54.2021 | 2026-08-15 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 10e11291-909a-3a94-be0a-5065b9650a30 | -6.9334 | -43.6333 | 2026-08-15 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 83c5c50c-2fb0-38bf-8fd8-d8443f001b69 | -6.9331 | -43.6566 | 2026-08-15 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0fb635cd-f1da-3214-b78b-92ec6c8cd4e2 | -8.1682 | -47.4099 | 2026-08-15 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 81687fd4-54e0-3625-9fa3-23791371c119 | -14.4317 | -51.8388 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4facf6a5-944d-3a02-9853-8536d61c92ad | -16.102 | -49.8573 | 2026-08-15 13:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 228.9 |
| e8879dac-1764-3810-be37-dff3f5381ad9 | -13.2613 | -54.2042 | 2026-08-15 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 3d25af04-2ea4-33ab-8379-43c881c348ca | -7.2788 | -44.6862 | 2026-08-15 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| cface88c-7169-328f-bae6-736efc8944e6 | -12.446 | -46.6584 | 2026-08-15 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| baa9c3a2-3665-3b4b-8cae-d3658fd6339f | -6.9145 | -43.6351 | 2026-08-15 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 38d2a5b8-e19d-342c-a5bb-9a02b2c47aca | -14.4499 | -51.9004 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f45dfec2-f8e0-32ea-80ed-1e075b2a5e0d | -14.9597 | -46.618 | 2026-08-15 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| da25d7a7-eba5-37bd-b0a3-ae4ff3ff9cf1 | -14.4112 | -51.9055 | 2026-08-15 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 73534cc4-4a20-3f95-bdff-7e5fe2366665 | -7.2786 | -44.7091 | 2026-08-15 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 4c6a98eb-86b8-32e8-bb90-ae44deee8567 | -16.1216 | -49.854 | 2026-08-15 13:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 269.8 |
| e5554b6d-7332-3972-b626-dd79cd000ae8 | -12.446 | -46.6584 | 2026-08-15 13:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 399.1 |
| 1808d78b-f5d1-39ae-bba3-37bac499e006 | -14.9592 | -46.6409 | 2026-08-15 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 766510b6-8c25-3fd7-8df1-3a6713ba2405 | -11.4184 | -46.3506 | 2026-08-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 720.8 |
| a0c4d8a9-3a23-3b80-bf73-8586e04fb862 | -13.2807 | -54.1814 | 2026-08-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 708937ae-536a-3c57-bc1c-5b00865a3006 | -12.4456 | -46.6811 | 2026-08-15 13:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 14533ee3-dbb3-3617-9b6e-3bf77dadb242 | -7.2786 | -44.7091 | 2026-08-15 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| dfd1e2aa-566a-3409-96ed-8250112e989b | -6.9334 | -43.6333 | 2026-08-15 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 197.0 |
| dd95892a-eddd-3afc-8c9f-73993cb178fb | -11.3809 | -46.3105 | 2026-08-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e906649a-eca6-3cb9-b3f4-3ef1efd9c305 | -7.2974 | -44.7074 | 2026-08-15 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| db7bdc61-6dad-3c1a-9282-7fb20109c7ce | -6.9331 | -43.6566 | 2026-08-15 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4a5bcdc7-166a-3861-82ab-71b2d8c8a6ff | -11.3992 | -46.3532 | 2026-08-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| db0dab36-18ca-3e60-96b8-b14648c253e4 | -13.2616 | -54.1835 | 2026-08-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6e706eaa-b534-3465-8449-8610a00996cc | -6.9145 | -43.6351 | 2026-08-15 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8bb3f0b3-beb5-3d3e-bc48-09fe308d690e | -16.1211 | -49.8761 | 2026-08-15 13:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 56402034-e208-3613-b2f3-135d0c5554c2 | -11.9347 | -46.3244 | 2026-08-15 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 43a18e6c-8700-3460-911b-160c13c0c59c | -14.9792 | -46.6145 | 2026-08-15 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 42900cd4-0f42-38c8-b685-4a85d106ddb1 | -16.1216 | -49.854 | 2026-08-15 13:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 9cab6eb2-06f6-30d3-8d73-6ad66fd2cc67 | -11.3996 | -46.3305 | 2026-08-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 444f4d63-c43a-35fd-ae1f-ed311e18b5d1 | -14.9597 | -46.618 | 2026-08-15 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 8ec4af04-2c5d-381f-b556-526df9215fcb | -13.2804 | -54.2021 | 2026-08-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 259c55f8-69fb-36d2-8f43-2ccacb92d4be | -7.2788 | -44.6862 | 2026-08-15 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e6dd9d9f-8acc-313e-a346-b0f6a43b58a2 | -13.2613 | -54.2042 | 2026-08-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 8ac31eb7-2d46-3b38-b6ba-9cb520e295e5 | -16.1216 | -49.854 | 2026-08-15 13:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 300.2 |
| 20e59b66-cf98-3dca-9b07-747a441c1aeb | -13.2804 | -54.2021 | 2026-08-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 5e9d218a-cd46-364d-9ed1-7d7ceef33d75 | -16.1211 | -49.8761 | 2026-08-15 13:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 39a7a6dc-990f-3a9b-a744-f51d206c2d5b | -7.2788 | -44.6862 | 2026-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6d41ba6e-e0b8-3a65-8def-f6203762ded2 | -6.9334 | -43.6333 | 2026-08-15 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| a5a6f733-3a4e-359a-91a2-748468c9bd22 | -12.4456 | -46.6811 | 2026-08-15 13:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| df69644b-d439-315d-acdb-66199e450697 | -7.26 | -44.6879 | 2026-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 975441f5-d00e-3186-9c1b-ed709d7a14f8 | -10.0887 | -46.2493 | 2026-08-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b2cb5ad0-34fe-3b77-932f-b93f32c7342c | -11.9351 | -46.3017 | 2026-08-15 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 00537271-2d1a-39c1-8079-be51cb295248 | -11.9347 | -46.3244 | 2026-08-15 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 1348fabd-b157-3ee3-8e43-c6f9b23e75bc | -13.5507 | -46.2615 | 2026-08-15 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a8705fb8-7eda-30b6-bbd0-458e964c81c1 | -6.9336 | -43.6101 | 2026-08-15 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 54fb9a58-58a2-301b-868e-5259a15e97a1 | -11.3992 | -46.3532 | 2026-08-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 25d82c7b-6245-3110-ac17-02f2adf6f5c5 | -11.4184 | -46.3506 | 2026-08-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 480.0 |
| 6b49c7cb-f7a3-3ae7-b281-2e5d492ca27a | -13.2616 | -54.1835 | 2026-08-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 63580d2b-b01a-3d69-8f37-2e47c8a874a8 | -6.9331 | -43.6566 | 2026-08-15 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4301eb26-f435-3535-926c-967b87986f08 | -7.2786 | -44.7091 | 2026-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 17156f4a-ce8b-3720-9b79-79c7e3f9c739 | -13.2613 | -54.2042 | 2026-08-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 237.4 |
| 647409d6-3d98-3477-8acc-fc200c11382f | -6.9145 | -43.6351 | 2026-08-15 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 21ed0896-f4a7-3f96-a5e5-ea46428c4570 | -13.2807 | -54.1814 | 2026-08-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d8ee7dd3-7d40-3ead-b1e1-5b1112f407d3 | -16.1015 | -49.8794 | 2026-08-15 13:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fbdf74f5-d99a-3028-a84e-ef3e496ec6f5 | -14.9592 | -46.6409 | 2026-08-15 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f1d78070-4440-36df-a41a-d9c60619a2f0 | -11.3996 | -46.3305 | 2026-08-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f94e34a0-5662-3666-97ce-09c640eb1d7e | -11.3809 | -46.3105 | 2026-08-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7d84b1c5-890f-35e6-bf57-bfe9c40be0e2 | -12.446 | -46.6584 | 2026-08-15 13:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 490.8 |
| 286cfbb1-bfa4-3245-8380-0bb25c04206f | -11.3992 | -46.3532 | 2026-08-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| bcee5452-ec57-37e5-a86a-1cef974e6564 | -13.2807 | -54.1814 | 2026-08-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8cd1f5ef-a5aa-3224-8348-d2ccb834c11c | -11.9436 | -51.76 | 2026-08-15 13:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 3aab3ecd-4192-3e89-9112-27450e329d28 | -7.2788 | -44.6862 | 2026-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c803901a-ef72-3187-b939-fa647b02a73f | -13.5507 | -46.2615 | 2026-08-15 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 15c934e3-a64f-3f86-b02f-2b54420efd61 | -14.9597 | -46.618 | 2026-08-15 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7b9cbe09-ad35-3ff8-96f0-f415c3d47ef5 | -16.1211 | -49.8761 | 2026-08-15 13:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 50a1c5ce-63f8-382f-a8f4-8ea85767eb5d | -11.4184 | -46.3506 | 2026-08-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| a925ed6c-2bed-370b-8f34-e51c7f0a687f | -7.2974 | -44.7074 | 2026-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d8a05f32-fab2-388f-bfa6-e4cfd83e8571 | -13.2616 | -54.1835 | 2026-08-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| be76dffe-fa69-37e8-ad94-441c3c60ff1c | -13.2613 | -54.2042 | 2026-08-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 160a3e75-99f3-3714-9550-b153b72a9c9c | -13.2804 | -54.2021 | 2026-08-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 1db8f43c-a8c8-34a9-acf2-8edd3ed2d3a3 | -12.4456 | -46.6811 | 2026-08-15 13:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f69b3461-3b1d-32a5-ae84-46e6c4519933 | -16.0823 | -49.8605 | 2026-08-15 13:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| c1831c68-fa11-3973-9694-880daa4789b5 | -10.5281 | -44.8492 | 2026-08-15 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4046f80f-4ebc-314f-a67c-01c068992406 | -7.2598 | -44.7108 | 2026-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d743e872-f2e6-3087-bd83-7788db7f56bd | -6.9331 | -43.6566 | 2026-08-15 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ee72456d-4ee8-3a71-b0c6-0584de7ee497 | -9.9708 | -53.9419 | 2026-08-15 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ad76a5d9-9e81-301d-a284-a38cc54769d5 | -11.3996 | -46.3305 | 2026-08-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 237883f3-1418-3837-9349-482c10663b1b | -14.9792 | -46.6145 | 2026-08-15 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 515ecc59-65f9-3660-b81a-75967c308a4f | -12.446 | -46.6584 | 2026-08-15 13:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 304.4 |
| b72799ee-f533-3c96-a71e-cee89a86bd6a | -13.5511 | -46.2386 | 2026-08-15 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 774a7907-80f9-307a-a243-c6426b3e9e87 | -7.26 | -44.6879 | 2026-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a33939c2-a8ed-3fff-8986-95834da6dad9 | -14.9592 | -46.6409 | 2026-08-15 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 121cc5a9-36b6-3c8b-a665-4d2c39037dfb | -6.9145 | -43.6351 | 2026-08-15 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f422ed5e-d2db-33bb-9271-045b6133f3b9 | -7.2786 | -44.7091 | 2026-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 236.6 |


[Clique aqui para ver as próximas entradas](README52.md)
