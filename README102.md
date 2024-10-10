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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d2a40a5-d37f-3bfd-ba04-180ac51d25b1 | -10.67681 | -48.71843 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49aae350-1dd7-3837-90f6-3f56ddc23fed | -10.67628 | -48.71561 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf72d2cb-6e89-383e-8e7f-8e2fa74d021d | -10.67566 | -48.71973 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34657364-023d-38af-bf57-e22e69a85c27 | -10.67562 | -48.72668 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a91a6119-9447-3269-87e7-867d1e0b96d6 | -10.67505 | -48.72386 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40cebd90-e8fc-374f-8b41-edbe1c2e9683 | -10.67443 | -48.72801 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b101172a-208c-3564-8bbf-9dbbe889186b | -10.67322 | -48.71771 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0488cf77-7f76-39e4-9734-6a8343ccb050 | -10.67262 | -48.72186 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67b88218-1cce-3d31-9d67-a51e711462dc | -10.67207 | -48.71902 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20db6218-6ad1-3b3a-a4a4-1558db9f10b8 | -10.67202 | -48.72606 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4697a007-857f-3905-a24a-fcbbb11a045b | -10.67145 | -48.7232 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3ba22eb-12b1-3087-ad56-3601228facd6 | -10.67082 | -48.72742 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1144e24-c15f-3b6f-acd3-310938b2f95a | -10.66841 | -48.72547 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833d22c8-8a25-348d-a0ed-896d494cd6c4 | -10.66784 | -48.72261 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 560d2710-e664-3e3e-95db-218540acde74 | -10.61157 | -48.29568 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 979b983f-1123-392f-b9be-9e59cb5ff960 | -10.60788 | -48.2951 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536d4f54-5683-3438-a796-051f0e669cfd | -10.60772 | -47.709 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7091c69-3218-361c-b846-37beb6b12f09 | -10.60555 | -47.70647 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 379d0c95-2860-3700-892b-fabb4cf0a592 | -10.60485 | -47.71123 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ce76092-6acf-396c-a0ff-66b8ee123a41 | -10.60457 | -47.70367 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a41fc768-7c8f-3dd4-a940-45efd63e58f2 | -10.6039 | -47.70844 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cca57e07-d174-35cc-a926-46c91403294b | -10.60173 | -47.70591 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3bc7e213-1665-3003-89a4-fae28b3dc516 | -10.60074 | -47.70311 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4040cf08-150c-3878-b599-afdeff1f9868 | -10.60007 | -47.70786 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a1022fd-ecc8-34f6-a03c-dd08c0ead6ab | -10.57806 | -47.89244 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d040d87c-e020-3e75-a514-c5a98c7bcb3d | -10.57783 | -47.89486 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1bcfbac-280a-3a78-9095-4bcf76917fdc | -10.57774 | -48.03053 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fff25f2f-da4d-31f8-98b0-ccdcdc77737a | -10.57465 | -48.02536 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 49ff343b-47d8-345d-8f38-672916230953 | -10.57399 | -48.02999 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe79ffd4-623e-3aae-b319-1ce70ad8c591 | -10.57335 | -48.0345 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b74454b4-04a8-31ee-87eb-2d2cf89d8568 | -10.57089 | -48.02484 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10d6caad-dc67-36ae-bd3b-acf974467179 | -10.56715 | -48.02418 | 2024-10-10 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cac63aa3-301d-3a47-bc6d-07aa27cb7f11 | -12.10027 | -48.6505 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7683ca0d-dbdd-3f64-8215-40e30ea4e9a2 | -12.09374 | -48.65116 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af5ff9ff-0ee4-31c5-a8f6-99b0b9aac17a | -12.09309 | -48.6556 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af45dd9c-1519-36d3-af67-f15a64056685 | -12.09288 | -48.64941 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccb8e3e9-917b-378c-9539-1e23d67e1407 | -11.58645 | -48.43369 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3cc5658-5225-3456-ac5a-92dba3070b73 | -11.58501 | -48.43095 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdac36b4-7593-3cc0-9777-e7c9aa485482 | -11.58435 | -48.43546 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 150378f9-d849-3358-b850-109526d53eda | -11.58274 | -48.43312 | 2024-10-10 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47b308d6-d9fe-3c54-b720-2dae9443d9f2 | -10.9775 | -47.88237 | 2024-10-10 04:44:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ab747da-0063-306b-9c42-71d8820f42dd | -5.06462 | -48.45136 | 2024-10-10 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caf5cede-8217-30a5-a97c-f29c274a16ab | -5.06234 | -48.44324 | 2024-10-10 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad55d5d-bd46-3072-8d04-c037c821146d | -4.99199 | -48.41708 | 2024-10-10 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e874fcd-ec22-3789-9b6b-a47aab144efa | -4.95653 | -49.05664 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8935cb2d-1479-3bc5-8d67-78d956910d8e | -4.95596 | -49.06026 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a4265d1-8afd-3c0a-addb-22d8f1341200 | -4.89599 | -48.56505 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6742431a-6b6e-3b51-99ef-20049a385375 | -4.83787 | -48.94176 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d438a412-7d5a-3fb3-9c57-f4e659c1eac1 | -4.78557 | -48.89303 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 287d6128-75c2-3baf-95f1-df74e09372aa | -4.785 | -48.89667 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ebb01df-ec22-31b6-801e-b2db4bea9d49 | -4.78216 | -48.89254 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 575c68dc-e373-3ceb-9e57-5d67005d7756 | -4.78159 | -48.89619 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b1f859a-9ab7-3cc4-adcf-a70664c327fd | -4.7697 | -48.92786 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e83cc0-3b34-3dac-b31c-df1bcffc60ed | -4.76575 | -48.90865 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60d3c3d4-ddc4-386b-9721-eaa0c11f1f9f | -4.74705 | -48.87227 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c04e9655-b8c0-3df2-9df1-1a9778c20363 | -4.74309 | -48.87539 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d99dd3-0d5b-3bbb-bfe8-80ba530eb8a7 | -4.74196 | -48.88269 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8227137e-aa99-354c-93ea-4f51e9048973 | -4.73913 | -48.87851 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e32c7e56-ec3a-3d12-92c5-6b1ccf631860 | -4.73856 | -48.88217 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d947ce28-0363-31d6-9290-0efd9602c7a1 | -4.66869 | -48.58526 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be931572-f564-357a-a037-8f45bf87667e | -4.52687 | -49.06928 | 2024-10-10 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a21b32f-abe4-3d87-92d8-d741400cadd6 | -4.98853 | -48.41657 | 2024-10-10 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d31242e-d969-35ea-893f-fda462fb2a8e | -4.68744 | -47.8739 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22ed64cf-3a2b-3dd9-bf0b-42ccf83f9110 | -4.68391 | -47.87337 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5824e900-69e2-3231-9d09-bd6e73307fe5 | -4.60128 | -48.06145 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f48574e-abc4-3245-9d9f-e81297fabd51 | -4.60068 | -48.06538 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87e4c8ec-73ae-3fac-b4cf-63677b19052a | -4.57572 | -48.01059 | 2024-10-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58779258-e2d9-3bfa-86b4-fb0e6ca3577b | -6.21914 | -48.16766 | 2024-10-10 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e7e656-bfe1-3c55-bcad-b9db3a5a210b | -5.32384 | -48.01682 | 2024-10-10 04:44:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67be2393-d555-3673-bb70-afeeb5b1de20 | -5.32031 | -48.01627 | 2024-10-10 04:44:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b4e2858-3729-3943-87cc-20ebec858a98 | -5.22309 | -47.96561 | 2024-10-10 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 670fbe6f-d63f-38fe-a145-b4230bdcb799 | -5.82616 | -48.82526 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4595833-7769-3cd3-a243-e0e87dc47b74 | -5.77667 | -49.01135 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9a1bb5bc-53df-3926-9258-b5a1f5391a48 | -5.75607 | -49.2588 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 135c6c01-04de-3327-bcec-38dc17da7aa7 | -5.75552 | -49.26242 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92b7056d-19ce-394e-9077-d2c4204897d4 | -5.75043 | -49.2505 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a201fb7-1c9b-303a-91aa-73981a2c4804 | -5.74704 | -49.24997 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 115e19ad-f627-3152-a29b-c44817aaf4b2 | -5.59788 | -49.03404 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05759ece-4c95-3a89-b9a7-d53daefc9c17 | -5.59731 | -49.03771 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b4d55ad-00d6-31a7-b753-ab1e8a619998 | -5.52508 | -48.36112 | 2024-10-10 04:44:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3396e829-87f0-3155-9b46-6f159d200d63 | -5.52358 | -48.36166 | 2024-10-10 04:44:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50973ad8-ff62-360e-a13f-0b6d91d77af1 | -5.45694 | -48.26028 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3468c5-dac0-33fb-a2b0-a97e8b9cca91 | -5.45344 | -48.25975 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de00130e-5247-35be-b295-9508d4ca6f6f | -5.32323 | -48.02078 | 2024-10-10 04:44:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2daa7e9-de57-3efd-be11-ce282b36ff69 | -5.26679 | -48.41081 | 2024-10-10 04:44:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d01a5573-8213-3186-aa7e-9f5f5ea00965 | -5.2237 | -47.96164 | 2024-10-10 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c7e80d2-6ca2-38bf-835f-6aeced1cd5a4 | -5.19369 | -48.22657 | 2024-10-10 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebf174de-b844-3af4-80df-2842df61b986 | -5.17665 | -48.26759 | 2024-10-10 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd696e24-c81a-3b35-bde2-8f12bd072268 | -7.12784 | -49.15232 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ced7f3f8-6945-3307-acc1-543b84afe12d | -7.12581 | -49.75516 | 2024-10-10 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b923d7f-67cd-33a2-acc1-0b2a5ee0007a | -7.12098 | -49.15129 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beca2d01-cdd3-34a6-9fba-79147ae4a5a8 | -7.11755 | -49.15076 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b30f19f-1f20-32d8-94ae-d8d48b628a6a | -7.11355 | -49.15395 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dda026b1-3c24-3466-8868-2be9d36315f2 | -7.0263 | -48.54602 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05a03f73-3dd0-32df-941c-1d8489201db5 | -7.01928 | -48.54496 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4f5950a-4267-36ca-ab84-46616561fcdc | -7.01636 | -48.54046 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44d49ba6-1443-30f9-9d30-dbc0715b625a | -7.01617 | -48.5374 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1fc81e6-3958-31b3-9a40-3f3b810c823d | -7.01168 | -48.54778 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06913fce-1edd-3746-aa0f-cd98cae41774 | -7.01085 | -48.54865 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8059949b-ea92-3b43-8d43-9d0637704de5 | -7.00734 | -48.54812 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README103.md)
