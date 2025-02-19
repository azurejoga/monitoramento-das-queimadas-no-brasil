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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4990e61-f43a-302b-8a4c-29f8d2e73e89 | -14.4899 | -45.8272 | 2025-02-19 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 652f8be2-65b3-3fa2-b86f-5eb5db16edba | -14.4704 | -45.8306 | 2025-02-19 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| d2e8550e-ef32-3cc6-b256-f6848fd5a0d2 | -14.4904 | -45.804 | 2025-02-19 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 56cc0b8a-42b3-39a3-8b35-ec497885330c | -14.4709 | -45.8074 | 2025-02-19 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 575df464-148b-3f01-82f2-845fcbdfd33e | -14.4704 | -45.8306 | 2025-02-19 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 013ccd86-6294-3bbe-9b84-ea6115250c94 | -14.4709 | -45.8074 | 2025-02-19 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 298.0 |
| de4aef26-5e51-3736-872a-e783945f3e83 | -14.4904 | -45.804 | 2025-02-19 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 17437496-c7a2-3e46-a09b-fb06fcd26a56 | -14.4709 | -45.8074 | 2025-02-19 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 328.4 |
| dcb922cb-fbb4-3f5b-bd63-6115c7c98bc0 | -14.4904 | -45.804 | 2025-02-19 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0d4a94d4-76d7-307f-9342-6a5a549c59ae | -14.4704 | -45.8306 | 2025-02-19 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| cab5a619-5d4f-342f-921e-0970fcf538c3 | -14.4709 | -45.8074 | 2025-02-19 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 314.6 |
| e4a683aa-62f0-38d8-b677-20a55a0a91b6 | -14.4704 | -45.8306 | 2025-02-19 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| b2b08cf7-a18a-3d48-8a13-34ceb14520d2 | -14.4904 | -45.804 | 2025-02-19 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a2eafd69-9635-31e5-857e-7dcf3f8201b3 | -14.4904 | -45.804 | 2025-02-19 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ee23a447-1e2b-3c93-85eb-84d76a4fd135 | -14.4709 | -45.8074 | 2025-02-19 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 334.1 |
| f21fa25f-a917-3fae-94dd-ab79130ed325 | -14.4704 | -45.8306 | 2025-02-19 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5d8ff5fd-26ca-3705-a152-892915baa265 | -12.7844 | -45.0037 | 2025-02-19 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| ac4b8bc6-5fc1-34e0-a78d-e5d7cdbab16f | -14.4704 | -45.8306 | 2025-02-19 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 402ed5cd-d6ca-3efb-80fd-d0504f3679f4 | -14.4709 | -45.8074 | 2025-02-19 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 339.2 |
| 9b228494-56cd-3d58-91e1-07a5e6a7f384 | -14.4904 | -45.804 | 2025-02-19 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d736f57a-6289-39bd-846a-e3922a7fe45e | -12.7844 | -45.0037 | 2025-02-19 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a41facfc-813c-39b3-8798-c43ccf589e77 | -14.4904 | -45.804 | 2025-02-19 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7eaad426-139c-3c60-b385-46d89cf645d3 | -14.4704 | -45.8306 | 2025-02-19 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| a0120cfd-9314-31f0-a059-136a14dca713 | -14.4709 | -45.8074 | 2025-02-19 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| b1f948a2-561c-3d21-a53e-a1a954adb2f6 | -14.4704 | -45.8306 | 2025-02-19 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| aa721883-9fb2-3754-9a34-bde0ba2d5011 | -14.4904 | -45.804 | 2025-02-19 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 99b1af4d-d1fb-3cd7-a334-51aa39a22489 | -12.7844 | -45.0037 | 2025-02-19 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a1c003e1-026a-387f-a969-c9aa1111dd68 | -14.4704 | -45.8306 | 2025-02-19 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 92792f9a-5458-387a-9f98-89af6f78a81e | -14.4899 | -45.8272 | 2025-02-19 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 646d6977-2d0e-30e7-98a8-d1ab69c7f655 | -14.4709 | -45.8074 | 2025-02-19 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 408.0 |
| d7a707b2-8876-32c5-87f8-464adbe9445b | -14.4904 | -45.804 | 2025-02-19 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 75fcde0a-2b96-3990-9049-8985119d4f00 | -12.7844 | -45.0037 | 2025-02-19 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8a331172-ee76-392a-9efc-f9113a0f86b0 | -14.4904 | -45.804 | 2025-02-19 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 255.5 |
| 3bd597cd-1161-34c9-8749-c73a3022bb8b | -14.4709 | -45.8074 | 2025-02-19 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 319.7 |
| 33dc3d4d-1508-3a45-80dc-7b85df8c9388 | -14.4899 | -45.8272 | 2025-02-19 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| a652159c-b5a8-39bb-b668-d8c373ca7aeb | -12.7844 | -45.0037 | 2025-02-19 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f566e530-f028-3557-8368-430e10852852 | -14.46 | -45.85 | 2025-02-19 14:00:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| defefa00-b921-3ec7-83a1-3f11ef751f5d | -14.4704 | -45.8306 | 2025-02-19 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 8b760fc9-6f09-36a3-818c-f91f19c69e20 | -14.4904 | -45.804 | 2025-02-19 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 316.3 |
| f7728a54-11be-358e-9585-c1f048b867ec | -14.4899 | -45.8272 | 2025-02-19 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0e65d628-b59a-3c10-9dd2-5e9e2f3596fe | -14.4704 | -45.8306 | 2025-02-19 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 0cc9b37e-2e92-3706-a5a3-f34e63c1d949 | -11.6903 | -43.9148 | 2025-02-19 14:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3c8d0ca6-f4e1-35b2-a2f3-4c2459eea2a1 | -14.4904 | -45.804 | 2025-02-19 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 08539652-4fc7-3b52-9798-70226b50e7b3 | -14.4899 | -45.8272 | 2025-02-19 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5056c243-a9e2-3fd7-bc45-797b182a8c39 | -12.7844 | -45.0037 | 2025-02-19 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 036d9384-7f7d-31c8-9b8a-fdfb271afd1b | -11.6903 | -43.9148 | 2025-02-19 14:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6cf8fc4e-db17-34c8-9ceb-e6bb9d9450ca | -14.4899 | -45.8272 | 2025-02-19 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d8255e5a-5d60-3dc8-bd0f-366760a643ba | -14.4904 | -45.804 | 2025-02-19 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 6661d021-8174-3f0f-aec0-f67b35e245ce | -14.4704 | -45.8306 | 2025-02-19 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 185.6 |


