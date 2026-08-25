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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cb24423-b1a5-3033-b41a-c5e7ae36b0c3 | -6.8008 | -59.5934 | 2026-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 428f4bca-c2b3-3832-be85-2a20bc40adfe | -7.2903 | -45.3456 | 2026-08-25 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| fc551e31-5cd4-3bbd-80dd-2ea1b084875b | -7.5475 | -61.3627 | 2026-08-25 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6ad5e586-f280-3945-9956-8b03f0681846 | -7.0058 | -59.2382 | 2026-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| c90a560e-cbbf-395d-983d-7b0faeb6c454 | -3.5221 | -48.1896 | 2026-08-25 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 776d78c3-d0bf-3303-a801-f0c31c6ebf7b | -6.641 | -58.4987 | 2026-08-25 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 176.4 |
| b7c1c038-894b-3c6f-9c41-ce49b26b40c8 | -11.1443 | -44.4865 | 2026-08-25 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 24e673d9-cee6-3b56-a0a7-6f938f02703d | -6.6411 | -58.4793 | 2026-08-25 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 333e4302-f419-3a2d-9804-bd109e78cf49 | -11.1447 | -44.4632 | 2026-08-25 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 01b66ca5-c5ec-34c1-b450-68b24d61cfc7 | -7.0057 | -59.2575 | 2026-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 977ac67f-1c50-327d-848e-35836494f172 | -9.4769 | -40.3365 | 2026-08-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 66887900-baaf-3f06-b687-0f6c965e895c | -9.4578 | -40.3392 | 2026-08-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 150.7 |
| a9e00d27-cfb3-3388-aaf0-8d5ff2400863 | -11.1252 | -44.4892 | 2026-08-25 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8d5c9a6f-1891-38f2-bf61-8836180f20ec | -7.2713 | -45.37 | 2026-08-25 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 8875db24-c644-3351-936e-a77ee7338aa8 | -14.3718 | -51.9533 | 2026-08-25 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c5b05a35-f2fe-35b4-9929-610c788de555 | -3.5222 | -48.168 | 2026-08-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9e340424-ea8e-3fae-9fad-f2354889c0bc | -6.641 | -58.4987 | 2026-08-25 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 21d8de2c-5588-3847-b71a-69ed153dfe10 | -9.4769 | -40.3365 | 2026-08-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 7389edc3-3a47-34c5-b25f-5737babb20e2 | -7.5475 | -61.3627 | 2026-08-25 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5e461e8a-c2f4-3251-a9cf-f80a095d5dd9 | -6.1286 | -57.8198 | 2026-08-25 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7e7dbf83-a5e7-38a5-bb8b-4e3ffdb7ee58 | -7.0057 | -59.2575 | 2026-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 0a961baa-ee2e-3b3f-9057-2463522a1d73 | -9.4773 | -40.3116 | 2026-08-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 2878fc0d-234d-3adf-9f32-509bcd4335bd | -11.1447 | -44.4632 | 2026-08-25 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 9c21d9c1-b859-3dd1-b794-833a152aa8a5 | -9.4582 | -40.3143 | 2026-08-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 165.3 |
| 8fe8a20d-7d5d-366b-803e-d297d6439032 | -6.9873 | -59.2389 | 2026-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 216fa7f0-8130-35b1-9725-073baf658b0d | -11.1443 | -44.4865 | 2026-08-25 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 897dbc33-c378-3992-9d08-bcd66a8088e5 | -7.0058 | -59.2382 | 2026-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.6 |
| fe20d050-95bb-39d1-b3f7-3e0a0afaa4ed | -14.3715 | -51.9747 | 2026-08-25 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d99c7bec-6980-3fd2-8c34-91235fb143e9 | -7.2903 | -45.3456 | 2026-08-25 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 3d192846-c4e5-336b-86bc-46b0cf0f3ecd | -12.7797 | -44.2576 | 2026-08-25 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 38203d76-00c7-3acc-b721-765be310406f | -7.2901 | -45.3683 | 2026-08-25 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| bb973884-53fe-30fd-8960-331872ba84bb | -10.3727 | -45.0537 | 2026-08-25 02:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e5a3d8ac-de5c-386f-959a-4f9d6e4b1b42 | -6.6411 | -58.4793 | 2026-08-25 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5dd37dcd-aade-39b4-b00e-5cc435555484 | -7.2661 | -45.8443 | 2026-08-25 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 24429e2a-a8d0-339d-94aa-0e0bc86f0aa0 | -6.6226 | -58.4995 | 2026-08-25 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7f70c156-4317-3a35-9791-110bb7e94e55 | -7.2713 | -45.37 | 2026-08-25 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c0f33533-9902-30d9-9f87-d27d6f31ed73 | -3.5406 | -48.1889 | 2026-08-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 751f5543-7cad-3020-9c77-27828b5073c9 | -9.4578 | -40.3392 | 2026-08-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.4 |
| d53ce917-eb82-31f3-bdb1-7ff4f6c531a6 | -3.5221 | -48.1896 | 2026-08-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ff96e847-d7c4-3978-bb88-cba538aebe33 | -11.1252 | -44.4892 | 2026-08-25 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| acb2865a-62ae-3897-a76f-488923cc821a | -3.5407 | -48.1673 | 2026-08-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 023b1b3d-30ea-382b-a89b-c68049dede9f | 2.5983 | -60.697 | 2026-08-25 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7ef9889d-2e5f-3091-8d9b-0e3cc2c90027 | -6.9872 | -59.2582 | 2026-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 54d8f02d-7d68-3394-b286-8dbeaa8952c4 | -11.1256 | -44.4659 | 2026-08-25 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ce94d086-1dde-3cd8-8590-41d3350ff003 | -7.2713 | -45.37 | 2026-08-25 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 58bdd824-db61-3aec-963d-cf90896796f7 | -3.5222 | -48.168 | 2026-08-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1052c178-8146-36a5-a868-244650b7ef0e | -7.2661 | -45.8443 | 2026-08-25 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0f24e0d6-10c5-361f-99d2-e6e3df4d5d78 | -11.1447 | -44.4632 | 2026-08-25 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 2be57784-2387-342d-95b6-a73a5cc62fa9 | -11.1443 | -44.4865 | 2026-08-25 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| d1e4910d-3416-378d-8127-9d405128170e | -7.0057 | -59.2575 | 2026-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 86369bcc-87e5-35ef-a94b-645c9947a876 | -10.3723 | -45.0767 | 2026-08-25 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| dbf9e67b-2217-306b-a918-09e405f09a14 | -6.641 | -58.4987 | 2026-08-25 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 8b014220-dcf9-39fd-aa71-8e9b191b7a9d | -6.9873 | -59.2389 | 2026-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e46f5373-fed0-3a16-9522-5afaa8203c73 | -3.5221 | -48.1896 | 2026-08-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 3a04a552-e9e8-3d46-9d98-2bfd732e1cf2 | -10.3727 | -45.0537 | 2026-08-25 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| d1e3c7c1-317c-3870-94a1-2fcd846a3771 | -12.7797 | -44.2576 | 2026-08-25 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 69d1d84f-d780-35ed-a73d-1de2a6577c01 | -6.6226 | -58.4995 | 2026-08-25 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a3ab47ae-a860-3faa-817d-3ed45f83926a | -7.0058 | -59.2382 | 2026-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 076cb4f4-c7c0-3213-8501-52351f3b4f22 | -6.9872 | -59.2582 | 2026-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5bed1727-4690-3f08-8771-d9da83271f50 | -7.2901 | -45.3683 | 2026-08-25 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 78a9e0ac-027c-3f8c-8770-c2216c1582a5 | 2.5983 | -60.697 | 2026-08-25 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 32935574-0ec7-3f3c-b8cd-64f719cb6d22 | -3.5407 | -48.1673 | 2026-08-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 77f036c5-4125-3655-b703-3965cbffb2ab | -3.5406 | -48.1889 | 2026-08-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 496bafe6-5775-373e-a0c8-246311d0b0b8 | -7.2474 | -45.846 | 2026-08-25 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| cc44f9fa-e550-3648-a41d-c644315de152 | -6.6226 | -58.4995 | 2026-08-25 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2ec6cc6b-a0fc-3a70-b40c-121a95b52a6d | -3.5221 | -48.1896 | 2026-08-25 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0914b3ff-8e0a-3e57-a747-95ce46c0b970 | -6.9872 | -59.2582 | 2026-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 204ee02c-2f81-341e-8df9-7fa247b1f219 | -12.7797 | -44.2576 | 2026-08-25 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3a50972d-8568-3ddd-87ce-d17aa2f26e41 | -21.6337 | -49.8168 | 2026-08-25 03:10:00 | GOES-19 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| 77c888f0-4b1f-3a85-98a3-55139dad9ad0 | -6.9873 | -59.2389 | 2026-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5e714503-d93d-37fe-ac42-daf494191fa0 | -10.3727 | -45.0537 | 2026-08-25 03:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 56cc66e7-7c08-345a-98c3-aea847d9cfb8 | -7.2661 | -45.8443 | 2026-08-25 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 0890ea1d-f0ba-382e-9430-8951dc4fce88 | -3.5406 | -48.1889 | 2026-08-25 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 6642f28d-2ba7-3295-918e-6c749a415c41 | -7.0057 | -59.2575 | 2026-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 4806a402-a246-3805-a89f-4e1760cc66cb | -7.2713 | -45.37 | 2026-08-25 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 05549b8c-c668-3fc8-8b73-16996533801d | -7.2901 | -45.3683 | 2026-08-25 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4ab6711c-1ac8-3147-b147-b5ff4f2832fa | -7.0058 | -59.2382 | 2026-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 49d31007-9ccc-3bef-82c0-d6879b9aa515 | -21.6544 | -49.8122 | 2026-08-25 03:10:00 | GOES-19 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 62e3d51b-fa0b-3aad-817c-2a73bd5e6582 | -3.5407 | -48.1673 | 2026-08-25 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| b318de25-1c8f-33a6-bc64-3900a4c90c96 | -3.5222 | -48.168 | 2026-08-25 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| aedbe411-36f7-32bd-b373-6a843e6797af | -6.641 | -58.4987 | 2026-08-25 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| ea270361-bc45-3ff7-881e-139502001a07 | -7.2474 | -45.846 | 2026-08-25 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| fbc3c945-3551-3804-a72b-7884275b3c09 | -6.9873 | -59.2389 | 2026-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 2c8764f8-b193-3182-a9f1-a7b93ec133a8 | -7.0057 | -59.2575 | 2026-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 00824d8c-ee53-375a-85fd-5e5f3b0bd5c0 | -3.5406 | -48.1889 | 2026-08-25 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| b267f88d-65af-3805-9888-2b94d848c2d6 | -7.0058 | -59.2382 | 2026-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 05ff5fc3-d8fb-3c23-9e96-647e09eef687 | -7.2713 | -45.37 | 2026-08-25 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4a249699-4360-345c-9348-7b2b9535e596 | -6.641 | -58.4987 | 2026-08-25 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 2e7faad2-74f9-3d15-ab0b-967951d91030 | -3.5407 | -48.1673 | 2026-08-25 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 42bab95d-165d-3729-9cb8-132a2815879a | -6.6226 | -58.4995 | 2026-08-25 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e45b5540-dcc4-3bc9-9992-3bd11047fcf2 | -7.2901 | -45.3683 | 2026-08-25 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c486b4ab-be4a-329d-a292-d2c40e40831e | -7.2661 | -45.8443 | 2026-08-25 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 80346e9e-a931-3034-9726-d080ee49237b | -6.9872 | -59.2582 | 2026-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 60ea0ab3-21ce-3f87-9171-0b726fbd1b55 | -7.5475 | -61.3627 | 2026-08-25 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 129950da-0617-3068-9bfb-b809812a7c3a | -3.5221 | -48.1896 | 2026-08-25 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 343206cf-1304-3ebc-bec9-106ea1be9b61 | -3.5222 | -48.168 | 2026-08-25 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b9c77105-92cc-379f-9993-6322c22468aa | -10.3727 | -45.0537 | 2026-08-25 03:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 67bad213-2105-3336-a9f9-62bba0de7ab2 | -7.2903 | -45.3456 | 2026-08-25 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f6d60e92-07b2-357f-90f7-9ae5e76e0a50 | -10.3727 | -45.0537 | 2026-08-25 03:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7a5d52da-d4b4-3f0b-b575-c1708759543d | -6.9872 | -59.2582 | 2026-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |


[Clique aqui para ver as próximas entradas](README16.md)
