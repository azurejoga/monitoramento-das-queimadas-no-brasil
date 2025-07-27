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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72813fd0-de0a-3dd5-8d69-5910c6069c1c | -22.21962 | -56.77845 | 2025-07-27 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 470c468a-cd59-3de6-b3f0-ffac67b422e1 | -23.07371 | -49.67078 | 2025-07-27 05:01:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1a9ba0aa-f0e4-3150-9d15-3d1d433ee2f1 | -16.40985 | -48.92655 | 2025-07-27 05:01:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd51df73-7580-3ffb-987c-5fef6e42e591 | -20.4836 | -54.74637 | 2025-07-27 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a89f46ea-f014-3cd4-8760-d98e64987862 | -21.60612 | -57.5816 | 2025-07-27 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c275242-d49e-359c-ba6f-f7721f235683 | -17.24533 | -46.90689 | 2025-07-27 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b55eec-b3cc-3f78-8856-467662f94389 | -20.35075 | -45.99065 | 2025-07-27 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41100b49-0c3c-3d04-a9c3-29e7b4bf4067 | -26.0216 | -49.00609 | 2025-07-27 05:04:00 | NOAA-21 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a6e7b913-dcdf-3347-b984-5d4b54f1ca6b | -26.01338 | -48.97516 | 2025-07-27 05:04:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d628ae8-da81-3965-9845-c8ae0e2fd429 | -26.01846 | -48.97924 | 2025-07-27 05:04:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61c2ef0e-ecf2-3bf6-bdd9-2dffecb4e38d | -26.02135 | -49.00905 | 2025-07-27 05:04:00 | NOAA-21 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bcb017d8-d162-303b-aab6-4ede7c4ac990 | -26.01959 | -48.96577 | 2025-07-27 05:04:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e040cdbb-1493-31fd-839f-f39946305207 | -24.5193 | -48.85549 | 2025-07-27 05:04:00 | NOAA-21 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2099591a-1248-3568-a3a6-5f28d6e3077c | -26.01873 | -48.97601 | 2025-07-27 05:04:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a43a63ee-997b-3eaf-afa9-79b93130e2fd | -26.01989 | -48.9622 | 2025-07-27 05:04:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3e3a93d5-7bff-3a64-a15f-bb687ce2f176 | -6.6575 | -58.8468 | 2025-07-27 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 01bd84cd-f06f-3577-88d0-cea645583672 | -6.6389 | -58.8669 | 2025-07-27 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 42f5dffc-229c-3b9e-bfd5-5f2931741d00 | -6.639 | -58.8475 | 2025-07-27 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 030ca23d-6da2-32ee-8015-ea4cf69b5826 | -12.04417 | -45.82504 | 2025-07-27 05:14:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7598e63f-fa31-3c45-9acf-6926d4366ad0 | -5.78325 | -43.59771 | 2025-07-27 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ee780658-0bf1-375a-8c51-ab9033cee258 | -5.78047 | -43.60925 | 2025-07-27 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 065a0334-0826-3298-be7e-0dfc781d5774 | -12.03286 | -45.83843 | 2025-07-27 05:14:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 51cb688b-0276-3db8-8e04-7af4b4171cf5 | -12.67309 | -47.02332 | 2025-07-27 05:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 52195aa4-8097-3940-8928-5d32d92132d3 | -12.67793 | -46.99692 | 2025-07-27 05:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5e4ca3a8-b725-35d7-8636-e3ef8089e245 | -13.4898 | -45.49928 | 2025-07-27 05:16:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8ba23e67-cbb2-3ecc-8e9b-3fcfffaae2bb | -13.48816 | -45.49376 | 2025-07-27 05:16:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 096d7622-5e13-3da5-93f3-292b3b1a2f9b | -12.67458 | -46.99176 | 2025-07-27 05:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5a7d65e9-51f9-3326-b71b-44b703a5a4fd | -12.66991 | -47.01826 | 2025-07-27 05:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a19ca5a2-13c2-3a60-965c-f08662aa38e4 | -6.6575 | -58.8468 | 2025-07-27 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 91ac6b15-af39-3e8d-a78c-7c2804f9c0a0 | -6.6389 | -58.8669 | 2025-07-27 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d4205986-1944-36a7-be1c-888b9c0d47fa | -6.639 | -58.8475 | 2025-07-27 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 7cff6f12-b029-3f8b-a970-46411bd82b6d | -3.37273 | -52.80109 | 2025-07-27 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d88b9cfe-038e-3f27-a924-18157c266875 | -4.1073 | -47.93501 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5a19f9b7-5213-34ae-b056-318a8a9dddf9 | -4.10812 | -47.92941 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9529292-5975-3c9e-862f-ead92c52c6b3 | -4.10196 | -48.20258 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d417c8-0f84-3c46-bc0b-8772ee9cfc50 | -4.10768 | -47.92979 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90157983-4273-32e9-bda0-adec3e966059 | -4.11454 | -47.9307 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a235da37-fc7c-3599-8878-0bab5613be6d | -4.10058 | -48.20155 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 063fd2f4-8b37-33dc-bf36-0cc3eb02999f | -3.57254 | -49.50656 | 2025-07-27 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91cbae05-76e7-3d48-93a4-9797128af51d | -4.20883 | -54.88876 | 2025-07-27 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65f0953a-e99d-315d-b23a-5dc75bddfd18 | -3.57312 | -49.50253 | 2025-07-27 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43d073b5-8e07-324a-9576-e3e968fb69dd | -6.989 | -47.08057 | 2025-07-27 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9b6d1ee-69f7-36f7-8efb-6321196ac2af | -3.57234 | -49.50883 | 2025-07-27 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 412078d0-8939-3a1b-82d6-5aaffbf30c6f | -4.13363 | -47.64775 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd78353a-8002-32c8-b684-14d3741bd484 | -4.10762 | -48.20844 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91484794-f77b-32db-85b4-f20eb04f2878 | -6.98808 | -47.08738 | 2025-07-27 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 377431ad-79c7-3f7a-ae88-1fbc27a36e59 | -4.11374 | -47.93619 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b5fbd2a4-8910-36dd-84a2-e6821ee46dee | -6.40019 | -53.33619 | 2025-07-27 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45045c1b-83c3-3f39-b117-e23d4d73ed4d | -6.4009 | -53.33131 | 2025-07-27 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b104c009-20bb-382e-baea-8a519ff7db0a | -4.1141 | -47.93115 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d1fb47d-4a8f-302e-b941-96ce91f9e4b5 | -4.13288 | -47.65315 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9912faa5-81fc-35c9-934e-cb14270fab19 | -4.10689 | -47.93542 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5ac3563-e93c-31b6-972f-f7f496797034 | -4.11333 | -47.93661 | 2025-07-27 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 614c6ab0-bb45-3d6c-b631-d03031eb96ad | -3.57294 | -49.50485 | 2025-07-27 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1d811da-4575-367c-b606-64cdb97e2078 | -6.66648 | -58.84234 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88327672-8f70-3d4b-a9cb-34e904c4b048 | -6.67387 | -58.83972 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaaeb58d-d780-3be7-a9ad-c77c90ae5911 | -6.68012 | -58.84444 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eeb49f8-a0f2-38fe-9e91-a0d66942561e | -6.68296 | -58.84862 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 339c14c2-4079-3d25-84c0-1f8da556ddd0 | -6.63353 | -58.85228 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9bce242-246f-34fa-98bb-b63ab0066aa8 | -6.55386 | -56.18527 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b51865-22cf-3c67-8f80-0fcbb96f005d | -2.74153 | -48.68206 | 2025-07-27 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6fa1ab8-a90b-3002-b92e-53b90ce964b5 | -7.90435 | -61.51092 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e935c94c-cab1-30b0-94f9-678b59d63b3e | -6.65001 | -58.85855 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 18bbddef-4ccd-304d-88c7-c7ed3dd3069d | -13.09444 | -52.13792 | 2025-07-27 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4eb747c-261b-3a0c-9bc8-9a9b54684ad5 | -6.64773 | -58.82812 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a49905f7-3e69-3a23-b1e8-73a03301d6d5 | -6.63693 | -58.83023 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b991ed8-739f-31c9-bd45-18c7748a6eb1 | -6.63125 | -58.84446 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee56f717-96b6-30a7-acfe-53020dcfb364 | -6.65739 | -58.8334 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33d0567f-31ca-3ca6-a1c9-e5db92744481 | -8.60267 | -64.0413 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a07e598f-7922-3d5c-871a-d938d553f0e7 | -6.66364 | -58.83813 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca19395-92eb-3747-849a-81c2dabe57a7 | -3.39173 | -47.49105 | 2025-07-27 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5df33edc-4258-3dab-a458-26fdc6876edb | -3.06483 | -49.50091 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50bc9326-0301-3030-b5ec-b6968b031cd4 | -9.02619 | -59.76329 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5914bbb1-850f-3370-a793-3dea05412c03 | -11.52522 | -54.68429 | 2025-07-27 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c245511e-5f9a-3598-aba9-a19ab6719ff5 | -7.75201 | -51.13112 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb1f108b-eb5e-398f-86f0-893da2970cf0 | -9.02676 | -59.75965 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04ac841d-3bb4-3253-883f-ce361e85fae7 | -8.07549 | -63.86626 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f47d4b1-77c5-3276-a735-4a668eeb0f3f | -6.56407 | -56.19667 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2376560-37a4-3c57-99ef-742a7545c4d6 | -6.68126 | -58.83712 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd0c2aae-dad3-3eb5-8651-be5e92b28595 | -6.65057 | -58.83234 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a9ae83a-6daa-34cb-9ce2-e25c4dd62b38 | -6.6341 | -58.84864 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30bffacd-7ceb-3d3a-8b31-2591aafa8d6f | -2.81309 | -49.00743 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4140124-4678-31fe-b0cc-8a721fc3e6d1 | -6.6625 | -58.84548 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b193b44f-9a43-3d70-acf3-fa9367b43ccc | -6.6608 | -58.85646 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0df2e002-5c17-3f90-ba35-648ab358d88e | -7.1692 | -59.8261 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ac3242-e884-3cd7-85e9-d097aacf8a69 | -6.5447 | -56.19387 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8baa6d4-e0ad-3248-833d-cf015a62ea4b | -6.62444 | -58.84338 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63dcee9d-7e38-34a9-830c-60fcf125b9fa | -6.63977 | -58.83444 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d28f7b99-afb6-32a0-9bc0-3626620a9f83 | -6.67558 | -58.8287 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98516b0f-7dc5-3f3d-ad05-40f64c45a673 | -6.65398 | -58.83287 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c9ed975-ccfb-3497-a1fc-b359b09a0a5f | -6.89177 | -52.86505 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6038f6d-7249-336b-ab1a-066f2fcf2510 | -11.303 | -55.12071 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9bfb4dce-85bb-324c-8518-35106d599885 | -2.7476 | -48.68295 | 2025-07-27 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ba5770-f469-35ba-847b-68ac1ce37ea9 | -10.02112 | -67.69312 | 2025-07-27 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c59e8e9-c9b7-3502-a5e6-7d014ba46ec6 | -6.49121 | -56.20293 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3057cc09-b368-3c3c-b2eb-dd24304654ac | -6.62216 | -58.83552 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cedd6874-c656-38a2-9665-8df07c0812b9 | -7.49968 | -63.50633 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c48de5f6-54e7-3bf1-8c0d-66904d1b9b91 | -6.67217 | -58.82817 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e02387-9474-3737-8342-5540009f285a | -11.3 | -55.14251 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7caa7d2c-f91b-3f01-a0a1-661568dedad9 | -6.65512 | -58.8481 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README21.md)
