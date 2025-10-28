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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb29aa75-c528-32ee-9947-c3e10be61e9c | -8.1106 | -44.3749 | 2025-10-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e4b22374-7025-308c-b6be-63662d96ee96 | -4.3237 | -41.8078 | 2025-10-28 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 78141dce-9a1c-3ff4-9347-27c93b5f7b00 | -3.9993 | -49.0295 | 2025-10-28 14:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c5283655-51c5-3965-b74a-a44f99bc0ed4 | -7.8223 | -46.4664 | 2025-10-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e79a45e7-68de-3633-8d27-cf88d4524e0b | -7.4888 | -46.0716 | 2025-10-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b276a690-c86b-34bc-9cd0-3a555b99ec13 | -7.8035 | -46.4681 | 2025-10-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d6357fba-5699-32e7-bfca-3b17c4883f08 | -15.2003 | -47.2142 | 2025-10-28 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 41594bc0-b2c9-321e-9811-bb99e912479f | -7.686 | -46.9011 | 2025-10-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5c60e6db-96ea-3f28-a900-c941c2bf96d0 | -7.8225 | -46.444 | 2025-10-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 59207f89-d2cf-3c4f-87e6-995c6564e13e | -7.9884 | -46.7183 | 2025-10-28 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 41051e6b-ac83-38bf-9527-6419ef9421a0 | -8.1883 | -47.2979 | 2025-10-28 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0c8955e7-f055-3ea1-b4b9-d15cca5fd00a | -3.5645 | -43.6348 | 2025-10-28 14:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8fd9d35c-1a3a-3a73-bfdb-d339203607c0 | -9.9629 | -47.0925 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 9e41842a-b308-3678-b3a6-0592b414f939 | -8.4962 | -48.2778 | 2025-10-28 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 368.6 |
| 698f768e-b51a-33ec-b030-078a8042bebc | -7.7971 | -45.3893 | 2025-10-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 93c10fe7-78c8-3e0b-a5d0-5532fc02baac | -8.1883 | -47.2979 | 2025-10-28 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 01f78196-dfd8-355f-9bba-fa40ab58d27a | -8.6062 | -45.4439 | 2025-10-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 820f947d-d314-3958-a4a9-624b64c8fa0c | -13.2695 | -47.8622 | 2025-10-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a8a9b5c9-d1e4-3818-a84d-056600b68798 | -6.2567 | -41.8298 | 2025-10-28 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 500b5bf8-141e-38cf-9edb-f77bf6151755 | -6.2844 | -44.7029 | 2025-10-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 8129dbe6-0a42-3832-853a-fc2ee9d849a1 | -13.9337 | -48.4305 | 2025-10-28 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 08a55553-ed3c-3ad2-9aae-d151007bdf8e | -12.8299 | -47.7254 | 2025-10-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 20ada468-653a-305a-83b0-30526ae10383 | -7.8037 | -46.4458 | 2025-10-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 2d8d5f22-8acf-39e4-9c1a-aec7791de56f | -7.8223 | -46.4664 | 2025-10-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 20f0f6a4-0b60-3b76-a6e7-05f0fe8109c8 | -9.5298 | -46.9628 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 243.6 |
| d63e085f-9267-35f3-82d5-7b1a414a77b7 | -7.4583 | -47.1641 | 2025-10-28 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 75f2a0de-54ea-3e93-ab93-5581fb2bc177 | -7.8225 | -46.444 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8e532426-a19b-3b56-8bbf-c797ab6f39c0 | -3.7075 | -41.556 | 2025-10-28 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 212.1 |
| 5d88b85e-4d96-3385-8f8e-96358bbc04dc | -9.4739 | -46.9021 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 25215a56-663b-3b0e-8050-42c2a2a507e7 | -3.6975 | -43.2106 | 2025-10-28 14:30:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ac57a656-e5f1-389b-8b07-bb0b9df321de | -9.9632 | -47.0702 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8c7ae3ad-b233-3c89-875a-9dcb96405f80 | -3.9992 | -49.0508 | 2025-10-28 14:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2379e44b-1269-3b47-9f25-208fe7cb3fd7 | -14.2975 | -52.9366 | 2025-10-28 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a918953f-012d-3f0d-adc1-11d94321e6c5 | -7.8418 | -46.3976 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d7cb092c-d95c-3873-8e72-363a600e2155 | -7.9467 | -45.4655 | 2025-10-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 7c5b7fd6-f684-37be-b5a3-bba86bbd0f10 | -12.913 | -47.378 | 2025-10-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f7f1e4dd-2b83-3806-81dd-495b2eb764f5 | -8.5588 | -47.7472 | 2025-10-28 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 58030217-f186-3b59-af1f-e81a5637eb67 | -8.0447 | -45.1378 | 2025-10-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 8748a670-48e9-3383-be1d-07b4175c78e9 | -13.9465 | -47.7595 | 2025-10-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 834ee308-e61c-3fd2-968d-e0007262354d | -3.9993 | -49.0295 | 2025-10-28 14:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 61326a0a-36c4-3041-9391-24478657f36f | -6.164 | -41.6941 | 2025-10-28 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 0dcc1f3a-0ea6-3851-a4cb-f0efa4149305 | -12.5489 | -49.5901 | 2025-10-28 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5f3a6618-38b5-3c11-83e2-4a1a1f447c0c | -7.1225 | -47.0375 | 2025-10-28 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| de0b0191-1a49-3edd-8ad4-55ab3743bda7 | -6.0974 | -44.6718 | 2025-10-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 540c7e6b-26e6-3b44-afd6-9a0c4dfef094 | -7.965 | -45.509 | 2025-10-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 274b82c2-102a-3da6-885b-f70b29376c51 | -8.3245 | -45.3597 | 2025-10-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| ab335e9b-c111-3682-bf6c-1354d4a0bc39 | -7.9696 | -46.7201 | 2025-10-28 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ccfee7e1-dc8e-3998-adb5-66197a4da735 | -8.1853 | -44.4363 | 2025-10-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f0935c39-c841-3ef1-be90-730ce254c894 | -15.2003 | -47.2142 | 2025-10-28 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4d457fe4-4872-37c1-ba6c-41b1276b328a | -7.8606 | -46.3959 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| c484c5de-7abe-3e27-bcda-9be07e34470c | -9.1846 | -44.579 | 2025-10-28 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e678caa2-f26a-3234-922b-d333d6f5fc77 | -9.0582 | -46.9465 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 78ec829e-58d9-316b-a458-04758c57b88f | -9.5487 | -46.9608 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| ea558e9a-cad2-3c88-a64c-fa9f0fe42948 | -7.8228 | -46.4217 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5bbe2839-90c5-3183-abf1-6630e28f12f7 | -7.9355 | -44.8291 | 2025-10-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| d1ff0bed-fc0b-3e34-81b5-0d030dd91854 | -9.549 | -46.9385 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0b85b715-76bd-3fb9-82d1-fa266cff130d | -8.646 | -45.2806 | 2025-10-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7380d1b0-6e13-3e92-b32d-6c4c08feeda8 | -6.986 | -39.103 | 2025-10-28 14:30:00 | GOES-19 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 09f1f505-00ca-34dc-82a7-e53a77121206 | -9.9 | -44.9069 | 2025-10-28 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| fb39196d-ab2a-3bad-9a5f-fcb0b59c715a | -8.6065 | -45.4212 | 2025-10-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 20aedcc6-060d-3e6c-9423-6c156289d1d9 | -10.0191 | -47.1305 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 61d693dd-7973-3639-b328-1b73a2f2509b | -14.3599 | -51.5281 | 2025-10-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cb16fbf9-37f6-319f-95df-eab7a342278d | -9.9809 | -47.1571 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ed851332-54f9-3a3a-b344-dd53445e949e | -6.0786 | -44.6733 | 2025-10-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 66b4da18-c389-3c50-bd8b-f78000162f53 | -6.1655 | -41.5498 | 2025-10-28 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| a34bef7b-9de7-3c8a-ba46-7a3215e5396c | -9.5301 | -46.9405 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 53bba556-5eb0-3770-a0a4-997fb3072ad6 | -3.5834 | -43.5877 | 2025-10-28 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b6a373da-7091-381a-8b7e-4ff285d01d6a | -4.388 | -43.2896 | 2025-10-28 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2f4d4cf4-c8e3-3c8a-a4ac-4c2eb59e9a99 | -4.7252 | -43.1991 | 2025-10-28 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 96d23843-23f8-3bc8-bd79-1fa74ed51aa3 | -10.0194 | -47.1083 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3a3da4c1-9ff5-37c9-9f5a-8a45be534446 | -9.7942 | -46.978 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7db81f9e-4789-385a-89df-8d5f847c6dd6 | -6.3031 | -44.7014 | 2025-10-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| be71254f-c267-3a24-9cf5-bf1ba352d9a1 | -3.7101 | -47.6403 | 2025-10-28 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 563bd432-ee55-3a98-8327-ba3eee01172e | -9.8814 | -44.8862 | 2025-10-28 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 458f937a-84de-38d5-8b78-73344ebb6e51 | -4.8951 | -43.001 | 2025-10-28 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7520bd16-92e2-3574-9a9e-d90d5ea62acb | -3.1954 | -42.8836 | 2025-10-28 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0427154b-6b53-3d55-bb69-baf1e40fb767 | -10.0188 | -47.1528 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 88800d24-bcb3-3145-895d-ddd14321e234 | -4.5033 | -42.862 | 2025-10-28 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 89b19b69-ec98-3af0-ac14-9a6c1f61430d | -9.9626 | -47.1147 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 232d9b2f-bdb1-33b2-b014-4b7cfc1cbae7 | -5.7758 | -42.9842 | 2025-10-28 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 584cdc11-a549-3fb0-8920-6d346c2610d2 | -9.1657 | -44.5812 | 2025-10-28 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cd5ffa9c-292a-314a-8ba8-772e089020ab | -8.4781 | -48.2141 | 2025-10-28 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0dd240ff-119e-39d8-8e94-f26b733ddd03 | -8.9522 | -44.9731 | 2025-10-28 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6e248b47-a3aa-3614-b9a8-2ee003bca5dc | -8.6526 | -44.7771 | 2025-10-28 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 292083fe-ff54-30b8-a466-367ac8dd1473 | -13.2691 | -47.8846 | 2025-10-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 57bc4c90-03bc-30ae-b238-4d62fb2a097a | -9.4929 | -46.9001 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f45850f2-cdf9-3853-b96a-3b143bda6e82 | -7.5242 | -46.27 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bf60d7cb-5f55-32c8-b9a5-8f783ead0dea | -9.9818 | -47.0903 | 2025-10-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b7afe670-d586-347a-9445-5c8f7257cf30 | 1.602 | -55.7262 | 2025-10-28 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 27750748-fed9-3f4f-bab9-0dab647ad284 | -3.0148 | -41.6851 | 2025-10-28 14:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 9eff1236-33a2-3025-afe5-9f7b020d11df | -4.3237 | -41.8078 | 2025-10-28 14:30:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 4ac34f03-7724-3071-965d-e7392ffd858b | -7.9655 | -45.4637 | 2025-10-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d3edbe9e-4e65-356b-8d86-be17b489e979 | -9.1843 | -44.602 | 2025-10-28 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7b11c55f-d62a-35e8-b6a3-f514562b5584 | -9.0497 | -47.6112 | 2025-10-28 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ba49f467-4281-37b7-a7e3-c68689d7036b | -6.6414 | -44.6051 | 2025-10-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| df5a5204-b535-3cbc-87b2-c69b380bc36e | -7.3613 | -42.4399 | 2025-10-28 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 74751644-466e-3a90-9816-96b7e789e53e | -7.8035 | -46.4681 | 2025-10-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e8f166ac-ee60-3c23-8560-6f8d6679ee50 | -7.823 | -46.3993 | 2025-10-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f99ab414-fbec-3175-9042-53ff8ce59e5a | -7.9693 | -46.7423 | 2025-10-28 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 9d0d6e6f-6988-39cb-9e74-fd452113c9ea | -8.0256 | -45.1625 | 2025-10-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |


[Clique aqui para ver as próximas entradas](README94.md)
