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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d31cb7ea-6436-3988-a63b-2a9b7baf355c | -6.9872 | -59.2582 | 2026-08-25 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fd878176-b318-3471-8120-eb90447b980d | -15.2854 | -52.8084 | 2026-08-25 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 193b35d6-6ccc-3a70-86a6-d494f4aadfbf | -13.3402 | -48.2079 | 2026-08-25 08:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 167.3 |
| d2b5d6ab-ebf6-3164-ba65-3cf54e8b6a7f | -3.5406 | -48.1889 | 2026-08-25 08:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7555c793-84d2-341f-a85a-9cddf3e19606 | -7.0057 | -59.2575 | 2026-08-25 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 25654e4f-05a4-3a9f-83f5-9fc32ce0baf7 | -10.562 | -46.3266 | 2026-08-25 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 0cd13ebf-21c8-3ec1-94b2-3b12b71e37be | -3.5407 | -48.1673 | 2026-08-25 08:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5194a92b-a8f1-391f-8063-a6cb8831f4b5 | -10.581 | -46.3242 | 2026-08-25 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f006ce60-dc1f-30fe-9bb9-45764703b123 | -10.5814 | -46.3016 | 2026-08-25 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 57719bda-ce8a-3715-8ef8-68a55b3b9923 | -7.2901 | -45.3683 | 2026-08-25 08:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 3e0b8761-e091-3553-a6c8-d4c9d7738320 | -13.3595 | -48.2051 | 2026-08-25 08:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 2a315a56-c956-3f0a-87d3-497e95610ed3 | -13.3595 | -48.2051 | 2026-08-25 08:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| cd8dc3bc-6a52-39d9-946e-f773ee709ad2 | -6.9872 | -59.2582 | 2026-08-25 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ae3c7d6a-8ddf-3612-a2c5-93f4ed198b7b | -3.5406 | -48.1889 | 2026-08-25 08:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5d719088-512b-3228-b5d9-7f66fa0f5f53 | -13.3402 | -48.2079 | 2026-08-25 08:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e9c43860-cb61-3351-b209-33a75846bc99 | -7.0057 | -59.2575 | 2026-08-25 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a631e472-6456-36f7-850f-52d6d31b2611 | -10.5814 | -46.3016 | 2026-08-25 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 17fbd629-c2a0-3bdb-af48-6ca2ccca016b | -7.0057 | -59.2575 | 2026-08-25 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| fc3c7404-d5d1-3bd2-a764-b26c15093999 | -7.2901 | -45.3683 | 2026-08-25 08:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2d9c8c88-472a-35ea-b965-2ec9ea19e3e9 | -6.9872 | -59.2582 | 2026-08-25 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| b8399ea1-076c-33d5-9ec9-afb41c12be2d | -13.3402 | -48.2079 | 2026-08-25 08:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 583c1098-28e3-3573-9ab2-0df78fe16f12 | -15.2663 | -52.7898 | 2026-08-25 08:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5cddadc5-8077-3651-8f12-b318a1aeef1d | -15.2858 | -52.7872 | 2026-08-25 08:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5c258b95-aa04-3e45-afba-77edd95e459b | -13.3591 | -48.2273 | 2026-08-25 08:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 1bbd4301-7b03-317d-8606-22c1189e61d8 | -13.3595 | -48.2051 | 2026-08-25 08:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 192.7 |
| c26543d3-1d2a-3b5b-873b-970bbc9ea95e | -3.5406 | -48.1889 | 2026-08-25 08:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 67953368-d871-35f3-80e8-d52be6186305 | -10.581 | -46.3242 | 2026-08-25 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| a2f19a44-6d57-3037-9d08-b87d3b1aa911 | -6.9872 | -59.2582 | 2026-08-25 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 8624e8b7-ab55-3d4f-96a5-9dcff5f9eeba | -6.9873 | -59.2389 | 2026-08-25 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 17f0e3e7-0463-36f6-b093-0363aead676c | -15.2858 | -52.7872 | 2026-08-25 08:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 09e8f0f8-0243-3b3e-b8a9-51ef6313df70 | -7.0057 | -59.2575 | 2026-08-25 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a64c495d-37b2-3520-b638-ac2c9c76a0a5 | -3.5406 | -48.1889 | 2026-08-25 08:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e6113e4e-dca8-3ea2-a054-8b5273a4f73d | -13.3595 | -48.2051 | 2026-08-25 08:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 177.1 |
| c908fd32-24f4-3858-9446-9a6e5dd2f10f | -13.3402 | -48.2079 | 2026-08-25 08:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| acf866aa-a94b-326b-8b4c-8a9cba97e440 | -13.3591 | -48.2273 | 2026-08-25 08:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c517760a-1ce8-310b-a580-c607506e4657 | -13.3398 | -48.2301 | 2026-08-25 08:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| acff3ad8-1935-3dd8-bfaa-cb9a56838e27 | -13.3591 | -48.2273 | 2026-08-25 08:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6ee65354-d52f-3b69-95b7-d124273e3e74 | -6.9872 | -59.2582 | 2026-08-25 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| e7ed709c-8ac8-3d04-9f40-e46d404ffa6f | -13.3402 | -48.2079 | 2026-08-25 08:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 17968ec1-111c-3675-ad57-5ec211e2e85c | -13.3595 | -48.2051 | 2026-08-25 08:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 1170decc-beba-3b09-8b42-e53ea30ee0e6 | -7.0057 | -59.2575 | 2026-08-25 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 3d03d695-f044-3248-ab73-7cf25ba6a922 | -7.0057 | -59.2575 | 2026-08-25 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3fa1e480-f5fb-35bb-a2dd-2402fc414a6b | -6.9872 | -59.2582 | 2026-08-25 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 74224d91-b84a-32d3-917b-50181c9ca19d | -6.9873 | -59.2389 | 2026-08-25 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6c10b554-3bba-31f8-9272-5a833983c75f | -6.9872 | -59.2582 | 2026-08-25 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a969fd5f-901d-3fab-80af-dc425b94942a | -13.8576 | -54.0136 | 2026-08-25 09:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f8f0697d-5a31-3e85-a09c-3af1e5fa4202 | -7.0057 | -59.2575 | 2026-08-25 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 23110fff-0a0b-34a6-aff2-d52b9f46d062 | -6.9873 | -59.2389 | 2026-08-25 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 35f02244-4c3d-30d0-8951-4a40d4c4d0d5 | -6.9872 | -59.2582 | 2026-08-25 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 58b277f4-e17a-3482-85bb-31ccfde016ce | -7.0057 | -59.2575 | 2026-08-25 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 02f400df-ae26-3b89-8fa9-316ae11dd4a9 | -6.9873 | -59.2389 | 2026-08-25 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ccd45677-c506-379a-b778-1344c2204eef | -6.9872 | -59.2582 | 2026-08-25 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3699f12b-d88e-34af-9962-dc421ac23ac0 | -7.0057 | -59.2575 | 2026-08-25 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1d22ed2c-c55e-37b6-a8ec-e57e75d6b70d | -11.4298 | -44.5615 | 2026-08-25 10:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 04581dd6-a9f8-3239-813e-08ab143e8297 | -13.3591 | -48.2273 | 2026-08-25 10:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1863e92e-d2e0-39cc-8460-36ff15e08d9c | -13.3402 | -48.2079 | 2026-08-25 10:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 599928f9-375b-3a20-b7b6-0774d576f280 | -11.4298 | -44.5615 | 2026-08-25 10:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| af600ac9-e62f-3cb1-adb2-f3d3f94021bc | -11.449 | -44.5587 | 2026-08-25 10:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| c82a1137-4549-365f-985f-47d6cb5d0b23 | -6.9872 | -59.2582 | 2026-08-25 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 07ba4b08-387c-3402-85e4-ade3255074fa | -13.3595 | -48.2051 | 2026-08-25 10:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| e8eefa62-bbda-38a3-9cf9-5906c98f9795 | -13.3398 | -48.2301 | 2026-08-25 10:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 179.1 |
| a5fd4ed7-43e9-3f0e-9804-af46b2d249d2 | -13.3402 | -48.2079 | 2026-08-25 10:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ac57e5be-6403-34a2-bac8-2e27d9186f12 | -11.4302 | -44.5382 | 2026-08-25 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| de7bb589-53af-32cb-9339-55053fa37059 | -13.3591 | -48.2273 | 2026-08-25 10:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 132.6 |
| c12cdfe1-92a1-3f68-8e6d-34d4b3c6a081 | -11.449 | -44.5587 | 2026-08-25 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 541d2355-f170-38e2-8807-30f2c6929cbc | -11.4298 | -44.5615 | 2026-08-25 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| b5c5bb4b-bd1d-3f13-833e-cadf4e83f456 | -6.9872 | -59.2582 | 2026-08-25 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 9d176656-06de-3a40-948c-03596880faad | -13.3595 | -48.2051 | 2026-08-25 10:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1cfcb412-8f52-3503-83b7-c58bbb134706 | -13.3398 | -48.2301 | 2026-08-25 10:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 394e2449-a19b-3017-957f-c5a9a1c7bf76 | -11.449 | -44.5587 | 2026-08-25 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 93e03447-ee14-30c3-859b-8880bb85443b | -7.0057 | -59.2575 | 2026-08-25 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| bd832d6d-b646-32fd-a1de-552c6842e8a8 | -6.9872 | -59.2582 | 2026-08-25 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 8327180d-21bd-365c-b4e7-e257de618069 | -11.4298 | -44.5615 | 2026-08-25 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 3709999e-2e6d-31ad-9ac9-6fd5ceda6398 | -11.4302 | -44.5382 | 2026-08-25 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 2a116885-729f-3964-8d0c-307400b06d25 | -7.2901 | -45.3683 | 2026-08-25 11:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b385d2c1-16c5-314f-8aa4-dbfefbcc647f | -13.3402 | -48.2079 | 2026-08-25 11:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5f4e1088-5543-39d9-a611-3b24541c04cd | -6.9872 | -59.2582 | 2026-08-25 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 31c81953-e9d7-3e1e-9b71-dd14c54c4359 | -7.2901 | -45.3683 | 2026-08-25 11:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4c72bcaa-e158-3f16-92a6-f979bc30cc88 | -7.0057 | -59.2575 | 2026-08-25 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ee9cca6a-68b0-3e9b-8c90-9e68c67d1488 | -13.3402 | -48.2079 | 2026-08-25 11:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| bac7870d-b658-36a8-8307-7a0dca7e9258 | -11.4302 | -44.5382 | 2026-08-25 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| ecbd33f6-fae7-3b4d-998e-bbde3536dc3a | -11.449 | -44.5587 | 2026-08-25 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4cd03b9b-533b-3013-b1cf-b60915b0be3a | -11.4298 | -44.5615 | 2026-08-25 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 408.1 |
| c701b514-58f8-38c7-a649-549bb8770c2a | -11.45 | -44.59 | 2026-08-25 11:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c990c67b-39e9-3d4f-8931-09272dab638d | -11.4298 | -44.5615 | 2026-08-25 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 406.8 |
| ce27f949-e33b-3674-86f2-1a63c6be01f2 | -11.449 | -44.5587 | 2026-08-25 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 69fded19-5202-3498-b3df-a74f4739fba7 | -13.3595 | -48.2051 | 2026-08-25 11:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 44c73e6a-2982-3c4c-9d63-ebc918812b02 | -11.4302 | -44.5382 | 2026-08-25 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 270.0 |
| 275b9b25-97a1-3b10-9bef-e7ae1beba294 | -11.4494 | -44.5353 | 2026-08-25 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1bb9c28e-debd-3c1e-8d58-f3891f5e9524 | -6.9873 | -59.2389 | 2026-08-25 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a5c4d0ab-5b5f-3c60-a94e-24c5e67f42c9 | -6.9872 | -59.2582 | 2026-08-25 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 85f89cfa-a0e7-3193-a4fb-394a2d8444ac | -7.2901 | -45.3683 | 2026-08-25 11:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 16e9e932-a44a-32c8-a099-46d815a2b819 | -13.3402 | -48.2079 | 2026-08-25 11:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |
| af4b2e0d-48a2-37af-a1ec-3967ed930e88 | -7.0057 | -59.2575 | 2026-08-25 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a181d5f2-4ee6-33d6-b42b-6c0ec39d89e8 | -11.4302 | -44.5382 | 2026-08-25 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 542.5 |
| 2cfd28dd-be07-3946-a0f7-c53189fa142f | -11.449 | -44.5587 | 2026-08-25 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 5a8e8bb4-8d3f-3c1b-89fe-ae99dd89cddc | -11.4298 | -44.5615 | 2026-08-25 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 736.5 |
| ad663ca3-5b26-35ab-ace2-9d16512ef684 | -6.9872 | -59.2582 | 2026-08-25 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.2 |
| fc03ffed-7002-32cb-aefd-523a2c3bff5c | -7.0057 | -59.2575 | 2026-08-25 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 0572195a-8e12-3d45-821a-fce2862ccdce | -6.6359 | -45.1525 | 2026-08-25 11:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |


[Clique aqui para ver as próximas entradas](README70.md)
