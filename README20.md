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
| 7202bbcf-1e2e-3aae-bac6-67c76783a172 | -12.2325 | -57.2872 | 2026-06-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a0fe33ab-9639-3738-9169-edd9196adcf2 | -12.4471 | -58.4231 | 2026-06-04 15:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 328b6ca2-34df-3f23-a627-1049cd2f482b | -16.185 | -58.4822 | 2026-06-04 15:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 44950bc0-65ea-3886-91a0-c1e317af3649 | -12.4473 | -58.4033 | 2026-06-04 15:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| cf6a6af6-662f-362c-be5a-f430f81f90a7 | -12.2136 | -57.2888 | 2026-06-04 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3a2c14bc-8324-3f1d-858f-47dd8568c83b | -16.185 | -58.4822 | 2026-06-04 15:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 27d81b45-808b-3901-8df0-2d594cbf470e | -12.4473 | -58.4033 | 2026-06-04 15:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 2ae26f16-34be-3d3f-bc4a-260f42337eac | -12.0923 | -51.9966 | 2026-06-04 15:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 84b7a87d-79b4-361e-a79e-b9ab726c53bd | -12.2327 | -57.2672 | 2026-06-04 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a0fe659-cef0-3a81-a563-c53f1427650e | -12.2325 | -57.2872 | 2026-06-04 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 14054fe3-9549-342c-925b-6821c4a35d83 | -10.349 | -64.4689 | 2026-06-04 15:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4eaf501d-7d39-3674-a873-d959c24b6a5e | -12.4466 | -58.4627 | 2026-06-04 15:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 469.8 |
| dfdd3462-b2bb-30e4-8372-596e85e96209 | -9.1833 | -58.0584 | 2026-06-04 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 710cb7e9-041a-31bb-9545-d3342763c6b2 | -12.4471 | -58.4231 | 2026-06-04 15:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| dc15bf39-b4a6-3556-a723-fcb0497e9a96 | -12.4656 | -58.4612 | 2026-06-04 15:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 2e03a4ac-ce67-3bc7-a2ea-316fa6a3657e | -10.8573 | -53.7425 | 2026-06-04 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0e5f908b-104a-32ad-b693-5817975efd01 | -12.4283 | -58.4048 | 2026-06-04 15:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 4f8e4d6f-a138-3ead-a080-3a3950c55937 | -16.5973 | -58.2365 | 2026-06-04 15:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| dc6e6300-6c1e-3bd0-893a-4833ae488965 | -11.886 | -57.8329 | 2026-06-04 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 252.7 |
| 10bfefae-8b2f-34b1-b64d-f372274864bc | -16.1853 | -58.4619 | 2026-06-04 15:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 60847ec0-20c6-380d-9071-717cd6810d97 | -16.5973 | -58.2365 | 2026-06-04 16:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| ac76eaba-f2d7-333f-b0f6-1b526e8c7956 | -14.0919 | -59.3777 | 2026-06-04 16:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| fe720046-4cb4-3005-9448-9d3a6afe9f23 | -12.4283 | -58.4048 | 2026-06-04 16:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4592d7f4-c5df-3c6a-a66f-08a511dfbdd9 | -12.2136 | -57.2888 | 2026-06-04 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 52cead7e-68ed-386e-be63-0343dacbdce8 | -12.4466 | -58.4627 | 2026-06-04 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 423.7 |
| 3482c47b-6f09-3b4d-b9e8-6067e0b40c70 | -14.0917 | -59.3975 | 2026-06-04 16:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 99bc35eb-9681-33dd-a9b2-7da884e103f8 | -12.2138 | -57.2688 | 2026-06-04 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 655d976c-31cc-3d97-9eb5-ae935d486edc | -12.4656 | -58.4612 | 2026-06-04 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| ab2be4e9-ecc7-316a-986d-0e4c880e3afa | -16.1853 | -58.4619 | 2026-06-04 16:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 03c46887-fc74-30b3-b91c-c9dcffa3de91 | -10.8573 | -53.7425 | 2026-06-04 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b2348006-347b-3138-87da-4e85365ebc76 | -12.4473 | -58.4033 | 2026-06-04 16:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| f741adcb-ce4f-3c04-900a-476316b585f1 | -12.2327 | -57.2672 | 2026-06-04 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d82b16b4-91e2-3eef-8db9-2d4f7186a4d6 | -11.5499 | -52.7867 | 2026-06-04 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 04b9f176-d42a-379e-a04f-96d09b059da8 | -12.4471 | -58.4231 | 2026-06-04 16:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a3d7bab5-8df1-3d21-8585-b77c20a59b63 | -9.1833 | -58.0584 | 2026-06-04 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e69d166a-33f8-3399-a614-93790f26eb63 | -12.0923 | -51.9966 | 2026-06-04 16:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4774e12a-0c7e-34c3-9825-9604d686b0f1 | -12.2325 | -57.2872 | 2026-06-04 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 378b9a5f-4a81-3069-89c8-91d19fc43666 | -11.886 | -57.8329 | 2026-06-04 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 197.5 |
| b7049ed4-93b5-3380-88af-d49a4c487530 | -16.185 | -58.4822 | 2026-06-04 16:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| d0b76d83-5b02-3d39-98b3-308f13e00c40 | -12.4466 | -58.4627 | 2026-06-04 16:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 350.5 |
| 271a214a-7656-309b-8029-9faf845a17ce | -16.5973 | -58.2365 | 2026-06-04 16:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 99db4832-9e22-3353-807c-b449580d8271 | -12.2136 | -57.2888 | 2026-06-04 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 0402e8ee-e0e5-3831-9412-b52ae47260ee | -16.1853 | -58.4619 | 2026-06-04 16:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 20916527-6dfd-3de4-ac7c-74f015e65801 | -11.886 | -57.8329 | 2026-06-04 16:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 288.2 |
| 438f4c3a-660f-38fc-8a36-a5568bf72db5 | -14.0917 | -59.3975 | 2026-06-04 16:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 146681b9-d203-336d-957d-e78de2c66655 | -10.8573 | -53.7425 | 2026-06-04 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 28c26774-0867-3d2c-a9a2-1e3fa1333114 | -12.4283 | -58.4048 | 2026-06-04 16:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 505c1236-368a-3a4f-836f-b6e487ad13b3 | -12.4656 | -58.4612 | 2026-06-04 16:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| faa226f0-af00-3ade-b5bd-4f24931ed6c9 | -12.2325 | -57.2872 | 2026-06-04 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b49f3c8b-0f29-3ee3-a9b9-223934ba4dc8 | -12.2138 | -57.2688 | 2026-06-04 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| aee3a276-bfb6-358d-82e5-3b421ad76ca0 | -12.0923 | -51.9966 | 2026-06-04 16:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 24c68823-2bf1-38e3-bdf8-c7a2c6ad3251 | -12.2327 | -57.2672 | 2026-06-04 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 70c6e3c0-148e-33ea-9393-693d5f94d1f5 | -12.4473 | -58.4033 | 2026-06-04 16:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d7800a12-7bc9-3010-a561-e09187827d2c | -12.2136 | -57.2888 | 2026-06-04 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6cd4b1dc-f795-31bb-944b-d0ea0fcb2c2a | -12.2138 | -57.2688 | 2026-06-04 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 10123a21-61b7-399b-9dfb-2fa49d48ecbd | -12.2325 | -57.2872 | 2026-06-04 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b1b86e4d-a964-3ecc-8fc2-c615c5f31d5e | -11.886 | -57.8329 | 2026-06-04 16:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 250.5 |
| 0f96abfd-3be7-38ca-97c1-1c6f07de5b80 | -12.4473 | -58.4033 | 2026-06-04 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 809708b8-43c8-3b10-9b98-a77784f02c3b | -16.185 | -58.4822 | 2026-06-04 16:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 09c90641-792f-3f29-ba31-891b50c6614e | -12.0923 | -51.9966 | 2026-06-04 16:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 7c90a5df-7026-3ffd-bbba-27cd5aa5d0f1 | -12.4281 | -58.4246 | 2026-06-04 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1d1d3cb8-037c-3cdf-b7cc-0e458f74b214 | -10.8573 | -53.7425 | 2026-06-04 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 958da0b4-9cc8-3629-a13d-0f8fdade8baf | -9.1833 | -58.0584 | 2026-06-04 16:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a927e4bd-57b3-3a2d-9e98-9a6c359ad77e | -12.4656 | -58.4612 | 2026-06-04 16:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 40b5cbd7-47f8-3380-8e00-95cbcc002cdc | -12.4466 | -58.4627 | 2026-06-04 16:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 294.0 |
| b40b09a7-e59e-3c58-b8c2-50899a7899dd | -12.4471 | -58.4231 | 2026-06-04 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 5c458aa5-c733-3346-b9f5-87405eb2d341 | -12.4283 | -58.4048 | 2026-06-04 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c403b7fd-b352-3590-9528-0b35a5436adf | -16.1853 | -58.4619 | 2026-06-04 16:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 35cdbfd1-89fa-30c0-8905-0717afe3d8be | -16.5973 | -58.2365 | 2026-06-04 16:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 2b7d430e-f411-3733-9ce4-9a33f589c0df | -12.2327 | -57.2672 | 2026-06-04 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 858b37fe-2638-3d58-9a69-82f82be5d360 | -12.4471 | -58.4231 | 2026-06-04 16:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 18b0cb60-18fc-37fe-871f-cf1c47e773e6 | -12.2327 | -57.2672 | 2026-06-04 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c6fe27df-101b-35c5-8177-b05da298e253 | -16.1853 | -58.4619 | 2026-06-04 16:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 6d05f14d-5504-3973-83d6-f8d4430a206c | -12.4466 | -58.4627 | 2026-06-04 16:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 337.6 |
| f90dc5a7-b433-314e-b37e-e2b45a3b28a4 | -16.5973 | -58.2365 | 2026-06-04 16:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 899cce0f-3d85-3d0f-9b1e-78c2c2eca6c8 | -12.4473 | -58.4033 | 2026-06-04 16:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4ec6a9e2-56d0-3a51-bd38-fd12eac08d93 | -12.4656 | -58.4612 | 2026-06-04 16:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2e458e68-bf4f-34e1-b0eb-edc422349d16 | -12.4283 | -58.4048 | 2026-06-04 16:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e2ba56a9-54ce-3c7a-b234-058125f4bed4 | -10.8573 | -53.7425 | 2026-06-04 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b0c73aeb-2500-364e-a245-4f6db68017fd | -12.0923 | -51.9966 | 2026-06-04 16:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 9e1d81dc-1de9-384a-959b-94cf55d4accf | -11.6329 | -55.1844 | 2026-06-04 16:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d1cd5cfc-e85d-3093-8990-0bb7fd6b59a5 | -11.886 | -57.8329 | 2026-06-04 16:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 194.9 |
| b380dfa5-6697-3b92-9268-d60b5d2c2741 | -12.2136 | -57.2888 | 2026-06-04 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4d9174df-8e54-36b8-9ada-06f1cfecf394 | -12.2138 | -57.2688 | 2026-06-04 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7a9437fb-c79d-362c-b920-786c0e66e2b5 | -16.185 | -58.4822 | 2026-06-04 16:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 7c93ed47-976b-3405-90da-521eb5c10565 | -12.0923 | -51.9966 | 2026-06-04 16:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 9b41e34b-55f1-3256-9919-cb4a94632b50 | -16.185 | -58.4822 | 2026-06-04 16:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| bbcf2b06-ffed-3773-b4ae-a7e73b88a68e | -12.4466 | -58.4627 | 2026-06-04 16:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 289.9 |
| d8e3c00f-8e84-3a62-8eb7-d17436604112 | -12.2138 | -57.2688 | 2026-06-04 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d1af1c17-4200-3d90-b844-aa25aeb2b925 | -12.4656 | -58.4612 | 2026-06-04 16:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 43ab8921-d653-36df-bc9c-9e40597265f9 | -10.8573 | -53.7425 | 2026-06-04 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8257b730-9d7f-3716-a485-ac90822d5016 | -12.2325 | -57.2872 | 2026-06-04 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5815b766-1b0e-39cd-8096-5d8468ee13fb | -12.2327 | -57.2672 | 2026-06-04 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c062c532-a54e-379a-82fc-eda683524931 | -12.4283 | -58.4048 | 2026-06-04 16:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2c7841db-a99b-31e4-9dca-5b6644bcc4d4 | -12.2136 | -57.2888 | 2026-06-04 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 01e734f7-ff2b-3874-99bf-5ad509c03ba6 | -11.886 | -57.8329 | 2026-06-04 16:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 250.0 |
| f5084fe8-97ba-3688-a9b9-b5cf9fce8968 | -12.4473 | -58.4033 | 2026-06-04 16:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| de084037-57ee-3bb4-b43c-8ef51f432267 | -16.1853 | -58.4619 | 2026-06-04 16:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |


