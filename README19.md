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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07e83589-844e-3e0b-bc5d-cdd7800d6883 | -14.0917 | -59.3975 | 2026-06-04 14:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b47e4b8e-afe4-3f91-9ac4-006591a19e40 | -12.4466 | -58.4627 | 2026-06-04 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1083.4 |
| 80c45143-f059-34d7-949c-bc02d5a92421 | -11.6329 | -55.1844 | 2026-06-04 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 033096cc-8d81-3665-9999-006d3d379250 | -11.886 | -57.8329 | 2026-06-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| abf20411-1dd5-33ea-aaee-591d90ec8553 | -16.5973 | -58.2365 | 2026-06-04 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| cfeacb89-3547-3669-8886-1529f6cfcd91 | -12.4281 | -58.4246 | 2026-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c3abece9-0e1c-36c0-ab61-3e20cff6bc01 | -12.2325 | -57.2872 | 2026-06-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 11e52958-9de3-34f2-b890-a7c5a691446b | -12.2327 | -57.2672 | 2026-06-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7e0df35a-bb06-3131-98ce-07cad1cafa4e | -12.2136 | -57.2888 | 2026-06-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b572c823-64cf-3ba3-855a-79dd304d268f | -10.8573 | -53.7425 | 2026-06-04 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b8eabc51-3d7b-3c4e-b0c3-da92792efa5f | -12.4471 | -58.4231 | 2026-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b24c088c-a9fc-3108-ab81-09ca5b76c82c | -12.2138 | -57.2688 | 2026-06-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1394e7d0-80fe-33a8-9c9f-b6e77ad90275 | -12.4473 | -58.4033 | 2026-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5784d902-7862-336b-aefc-9bb050b68bb6 | -12.4473 | -58.4033 | 2026-06-04 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 173.8 |
| fcbd5698-d539-36c5-9c60-37f94fe77b86 | -12.4283 | -58.4048 | 2026-06-04 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c60a3df7-b35a-3034-b8ee-1f4b4011389d | -12.4471 | -58.4231 | 2026-06-04 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e82599f9-0340-313d-8a88-2df021b8219f | -11.886 | -57.8329 | 2026-06-04 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 159.2 |
| a7f87722-5244-3469-8c5f-4121ef459ae8 | -16.1853 | -58.4619 | 2026-06-04 14:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 4656fb24-097e-3189-922e-20232e651555 | -12.4656 | -58.4612 | 2026-06-04 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 348.7 |
| 490e2f35-8c71-39c4-95a6-ba5698a2e0ea | -12.4281 | -58.4246 | 2026-06-04 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 170cfd4e-af77-358d-aee5-f79211e525e5 | -14.0917 | -59.3975 | 2026-06-04 14:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f20d39a5-6736-3312-898e-fc77294e9b1f | -16.5973 | -58.2365 | 2026-06-04 14:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| abce43f6-5885-3418-9efd-dca9d637b46f | -12.4466 | -58.4627 | 2026-06-04 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 755.9 |
| 396d0ece-daf1-3d24-a07b-595468af5f9b | -11.6329 | -55.1844 | 2026-06-04 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 633f81ee-9f4e-3629-b03e-823b329477f3 | -10.8573 | -53.7425 | 2026-06-04 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 952e385b-499f-3093-a7fd-d350584b2de9 | -12.2325 | -57.2872 | 2026-06-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a025c12a-4e0f-3c93-95ff-1902ae0f03d2 | -12.4466 | -58.4627 | 2026-06-04 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 796.7 |
| 4886817e-1c60-33c8-bb0a-327c8fabd1dd | -11.886 | -57.8329 | 2026-06-04 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 1c89fe78-7f5e-38de-bd6e-6f204aca9cf2 | -12.4473 | -58.4033 | 2026-06-04 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 843b1b25-bbd0-3440-8114-af4500a1b66f | -14.173 | -58.9937 | 2026-06-04 15:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d48bd98d-25e7-3d37-9620-45d1ced6628c | -11.6329 | -55.1844 | 2026-06-04 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| b9fe3d3e-8d27-32f2-a7d1-000c8d69a87d | -12.4471 | -58.4231 | 2026-06-04 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 890d202a-5304-34ea-9c55-912434a5cbd2 | -16.1853 | -58.4619 | 2026-06-04 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 002e9f4e-e00c-3f04-93aa-8b2b82e16116 | -12.4281 | -58.4246 | 2026-06-04 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 71e92649-49f0-3f5b-8f92-8f84650bde24 | -12.2327 | -57.2672 | 2026-06-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| fc89666c-26e9-3de6-8b84-6fba2dd7f46e | -16.185 | -58.4822 | 2026-06-04 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| d0e8895e-a374-36b5-b477-7ffff7508f9e | -12.4656 | -58.4612 | 2026-06-04 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 378.3 |
| 05c11d86-c299-309d-bc94-91370d3ac192 | -9.1833 | -58.0584 | 2026-06-04 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 68200567-ee75-3402-b9f3-c039e8ec2eb7 | -16.5973 | -58.2365 | 2026-06-04 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 94534465-8f8e-3acd-a5d9-42fa076a987e | -12.4283 | -58.4048 | 2026-06-04 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 49cc5864-c2ef-3133-8815-950217c1ddf0 | -10.8573 | -53.7425 | 2026-06-04 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d35f33c3-d9f1-32c3-b77e-50899fb8f25f | -11.886 | -57.8329 | 2026-06-04 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 5e837e91-9b2d-3f7c-969f-466e40b69628 | -16.5973 | -58.2365 | 2026-06-04 15:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 1f7aa7e9-2868-336e-928a-5e84d688dcd6 | -12.4471 | -58.4231 | 2026-06-04 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4d4fefba-f03a-3d19-a534-efe9965d46a7 | -12.4281 | -58.4246 | 2026-06-04 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 615f6ef0-a2ea-3d8e-963c-9cb69b7551e0 | -16.185 | -58.4822 | 2026-06-04 15:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 3c1d9ec6-3b63-3206-b3d8-e7381f54fcda | -12.4466 | -58.4627 | 2026-06-04 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 733.2 |
| 7461ba6b-dc49-34e8-8e56-6964de281552 | -10.8573 | -53.7425 | 2026-06-04 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d7aa0d65-5efe-3410-b028-58c88d5b5b4d | -12.4656 | -58.4612 | 2026-06-04 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 354.1 |
| 16d5e240-2a59-3954-b01f-c44f459ad588 | -12.2325 | -57.2872 | 2026-06-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 35cfc9fa-109b-3de3-8c53-9a34dd5832d1 | -12.2136 | -57.2888 | 2026-06-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 99b892e0-8a27-3edf-90a5-3f4bb05febd6 | -16.1853 | -58.4619 | 2026-06-04 15:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| f00cb1df-1fd7-389e-ba7c-14b0e4818613 | -12.2327 | -57.2672 | 2026-06-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d96234ff-3a07-3fc3-942e-92d0a90bc4b8 | -12.4283 | -58.4048 | 2026-06-04 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0e99fcbb-0712-3dff-9899-6f481d38293d | -12.4473 | -58.4033 | 2026-06-04 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| de2eb238-480e-3451-aacb-d39545b1a529 | -9.1833 | -58.0584 | 2026-06-04 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d542ed5b-e65c-3b74-82c2-bdd8fc89a0bf | -9.1833 | -58.0584 | 2026-06-04 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 293cbc25-2fab-353f-98bc-b03ee36edc2e | -12.4281 | -58.4246 | 2026-06-04 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 21c9acd8-bb25-3924-91ed-2dc376403080 | -12.4473 | -58.4033 | 2026-06-04 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 095bb332-5e0e-3048-96a1-16478e934580 | -16.185 | -58.4822 | 2026-06-04 15:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 7a0a8aed-ea85-3b15-b32e-875083e343be | -12.4466 | -58.4627 | 2026-06-04 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 610.3 |
| 4ff6e602-fe0f-3477-92b5-adf8e54c6c93 | -11.886 | -57.8329 | 2026-06-04 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 264.2 |
| 7c6dfd41-35eb-3a54-8042-1c54694d6380 | -12.2325 | -57.2872 | 2026-06-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2b2d0a38-3dd8-3566-a113-0cf4c717c8fe | -12.4283 | -58.4048 | 2026-06-04 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 64e2579b-a304-312a-993f-16381f7156cc | -11.5499 | -52.7867 | 2026-06-04 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2894874f-6133-35d2-9072-7ce1be18cbf6 | -16.5973 | -58.2365 | 2026-06-04 15:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 96ad748d-9887-3a32-bc5c-7ec13160408b | -12.4656 | -58.4612 | 2026-06-04 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 1fd07bf2-cce7-3978-9d1d-de97509bca49 | -14.0917 | -59.3975 | 2026-06-04 15:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 20244d94-00b7-3ada-9ee6-0002ee5d2283 | -12.2136 | -57.2888 | 2026-06-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 67a96d4e-9bb4-3ea6-8766-8b1f2ce79344 | -12.2327 | -57.2672 | 2026-06-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fe6cec1b-72f9-3dff-bc1b-d6c3afc57625 | -10.8573 | -53.7425 | 2026-06-04 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7feeb074-e79a-3d8f-869b-b969f57c9a41 | -12.4471 | -58.4231 | 2026-06-04 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| bc09c92f-d739-34e5-9b23-3a8f5bca11df | -16.1853 | -58.4619 | 2026-06-04 15:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| ec078325-7a43-3188-a38b-0a02cf222ea2 | -12.4656 | -58.4612 | 2026-06-04 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 33f40393-f81a-332b-90bc-659f9673d4ac | -12.2327 | -57.2672 | 2026-06-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9e474d73-f0b9-30a8-b1ff-394a9061cff6 | -12.4283 | -58.4048 | 2026-06-04 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ea57a1ab-17f1-3d75-8ecc-b1e9ccb215b2 | -16.5973 | -58.2365 | 2026-06-04 15:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 5565e9b7-c2bb-385f-b4ef-383dbd09398a | -12.4471 | -58.4231 | 2026-06-04 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6ee8af74-cb27-3e98-880b-a9c82aac8fd9 | -12.2136 | -57.2888 | 2026-06-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9650b00a-c667-32ea-a75f-cf5f814b1587 | -10.8573 | -53.7425 | 2026-06-04 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 200b15ba-c861-34a6-b9f7-3da2efba5fcc | -12.4473 | -58.4033 | 2026-06-04 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 111e552f-d752-319f-8044-4faa83ab1854 | -12.4466 | -58.4627 | 2026-06-04 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 543.3 |
| 77af8abe-cf5e-3726-abcb-e6853a0bb08d | -16.1853 | -58.4619 | 2026-06-04 15:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| a2bfbcf5-8d12-338f-8b2c-6b454f250538 | -12.2325 | -57.2872 | 2026-06-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8b4dc2e2-ad97-3a24-9e4c-428c500a9061 | -11.886 | -57.8329 | 2026-06-04 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 266.9 |
| f64ed06d-db3b-30f3-8e1a-db649c89e952 | -9.1833 | -58.0584 | 2026-06-04 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3098d8d5-cb81-3417-a2b2-30a1e0698a21 | -12.4281 | -58.4246 | 2026-06-04 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 091e1a1a-b2aa-391a-8adf-8735629f5695 | -11.5499 | -52.7867 | 2026-06-04 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 41c46ff3-bf76-3915-a991-eac6165426a3 | -10.349 | -64.4689 | 2026-06-04 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cfa98f10-785d-3c34-9ec4-0be6dd578ee1 | -10.8573 | -53.7425 | 2026-06-04 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e73d4d08-28e8-3e32-96cc-2b510948a1a3 | -16.1853 | -58.4619 | 2026-06-04 15:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 3fe7fec7-18e1-3e54-bff4-361024589622 | -16.5973 | -58.2365 | 2026-06-04 15:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 886ee3af-cdf3-3a29-b712-cdfcbf2d2d58 | -12.4283 | -58.4048 | 2026-06-04 15:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a3c1b24f-a5ea-39c1-bc44-7930eff5aec1 | -12.4656 | -58.4612 | 2026-06-04 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 5580efb4-0beb-3dd3-a8b6-5fc0e66d34d5 | -11.886 | -57.8329 | 2026-06-04 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 270.8 |
| 4154d6ab-3cc8-3368-b80d-86b951154788 | -12.4466 | -58.4627 | 2026-06-04 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 502.7 |
| 9b740927-fa07-37fb-87f4-af4f4efad8ef | -9.1833 | -58.0584 | 2026-06-04 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d4c88e6b-812d-3060-bf14-1ed185c96785 | -12.2136 | -57.2888 | 2026-06-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2c62f3bf-74d1-37a3-809e-c73aa8d1381a | -12.0923 | -51.9966 | 2026-06-04 15:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d16f3e7d-0edc-3fa9-89f5-9914a39c7c6c | -12.2327 | -57.2672 | 2026-06-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README20.md)
