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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c464274b-5c90-349e-a1bf-50f875ba4377 | -1.2017 | -53.6769 | 2024-11-20 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0420708c-cf24-3576-82de-bdd480bda9f8 | -2.93 | -53.0601 | 2024-11-20 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 73e62206-94ed-3125-a80b-ae4fba3db8c3 | -4.4405 | -46.5754 | 2024-11-20 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 83985679-e4c3-36a5-907d-d683755761c6 | -2.7501 | -51.8171 | 2024-11-20 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5c151a35-78e8-34e3-97e7-a2d74538116e | -11.1109 | -54.6204 | 2024-11-20 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| fd89e8c4-d53a-3cf2-b045-1bb6318784ca | -2.9116 | -53.0606 | 2024-11-20 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a54060a7-0191-3273-bf63-cb65cd50df1f | -1.8613 | -54.2714 | 2024-11-20 03:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b5bb2466-565d-3754-8772-ded2a489e6e8 | -3.2014 | -54.3243 | 2024-11-20 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 70adb59e-477a-312e-a857-ea02ea7434f9 | -11.092 | -54.6221 | 2024-11-20 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8281fc62-dfbd-3866-a205-ca63e88fe105 | -2.7501 | -51.8171 | 2024-11-20 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c912bde7-dd49-31d1-86e7-36946d93ab1d | -3.2014 | -54.3243 | 2024-11-20 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b184ad4c-57bf-32df-beb5-397d93418175 | -2.9116 | -53.0606 | 2024-11-20 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a0ef1c06-4cd6-3d9b-b6f9-ed9b979aa837 | -2.7217 | -49.3508 | 2024-11-20 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 371a115f-a755-36dc-8847-69d16d05548e | -2.75 | -51.8377 | 2024-11-20 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9d767afd-5724-3cd4-8c97-5ff7db259999 | -4.4404 | -46.5975 | 2024-11-20 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e9cce986-8e00-364a-bd7c-23717f4827ce | -4.5614 | -48.0141 | 2024-11-20 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| d75e4474-df8b-3dfd-b89b-95925c970fe7 | -2.93 | -53.0601 | 2024-11-20 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c6968da4-b091-30d4-a98b-42f854986794 | -11.0917 | -54.6425 | 2024-11-20 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9a11418c-f16a-3e0b-8cc4-d4d72ed71820 | -4.4405 | -46.5754 | 2024-11-20 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c8c3040c-8cb1-3591-bb09-a2b901af5d6c | -2.9115 | -53.0809 | 2024-11-20 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| be2610fc-bff0-3629-973d-b790cecde542 | -11.1106 | -54.6408 | 2024-11-20 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 26b8ce65-fe72-3576-ab98-d54a4a09e018 | -2.7218 | -49.3295 | 2024-11-20 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 23c0cfdd-50c0-3988-a1b0-08fb459e036e | -1.2017 | -53.6769 | 2024-11-20 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 18644fea-4caf-38df-966f-d7ebb87f1308 | -11.1109 | -54.6204 | 2024-11-20 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 28bd6cc3-08a0-380a-b9de-dc664590cc4b | -2.7402 | -49.3502 | 2024-11-20 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 5a0cefb4-d428-3006-bc92-6274adb72a9f | -5.9742 | -48.063 | 2024-11-20 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| f8eab273-de80-3669-9d73-0875e56baa80 | -1.8612 | -54.2914 | 2024-11-20 03:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b8088bd5-cc1b-3d7e-84cd-0cae2acb7861 | -5.9556 | -48.0642 | 2024-11-20 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 7d8e0a39-4b79-3bb2-a6e1-7fe1b47e1a64 | -2.6212 | -51.7997 | 2024-11-20 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 92ec1961-8c13-3f65-a3a4-3c5e21d6eeaf | -1.8613 | -54.2714 | 2024-11-20 03:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 187f9878-75ad-3d6e-bcf7-0ac2a7aa6a8a | -2.9299 | -53.0805 | 2024-11-20 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0e8c1153-af2e-3582-8342-96e39b1fd0b9 | -11.06381 | -41.6258 | 2024-11-20 03:10:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ecb9e7a5-6438-3ed0-bfae-84747ec69c30 | -9.41396 | -35.97681 | 2024-11-20 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 816e3cd9-334c-306e-b5a1-15fbea4ee9a1 | -6.01222 | -38.65865 | 2024-11-20 03:10:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f6b42fbc-0d80-3726-ade5-4fe10569ae07 | -9.4195 | -35.97476 | 2024-11-20 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f63685a4-e3a6-398b-948e-4b0c754c6c96 | -6.0113 | -38.66373 | 2024-11-20 03:10:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 894257e3-a22d-3266-98b2-ccd6c4d5b214 | -10.53828 | -36.73264 | 2024-11-20 03:10:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c46400d4-2e0e-3868-a3e8-97bbee2c6fe7 | -11.06505 | -41.61982 | 2024-11-20 03:10:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 26aee40d-0bf1-3fa9-b40b-c5be1e0252ba | -9.41844 | -35.98042 | 2024-11-20 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a18aa8f0-e345-34b1-812d-3212a8c30ea0 | -4.52792 | -38.57594 | 2024-11-20 03:10:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30996874-04d4-39e8-9ad9-d0b750dc6b3f | -4.5343 | -38.57709 | 2024-11-20 03:10:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 714fcb6c-c233-3e4f-a480-c269e7ff2fa3 | -10.53885 | -36.72954 | 2024-11-20 03:10:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db21c966-8573-36a4-8cb6-a3c73b326541 | -9.41893 | -35.97778 | 2024-11-20 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c0712b61-a2f7-3e26-9fab-1b7ce7845f05 | -9.79737 | -36.54533 | 2024-11-20 03:10:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 887595c3-1953-3b4c-9086-17b41ef57de4 | -5.9742 | -48.063 | 2024-11-20 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1acb2d66-2682-342b-8e3b-50a41fed43aa | -11.1106 | -54.6408 | 2024-11-20 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 36f5574e-f421-3b10-8977-384b5149a410 | -3.2014 | -54.3243 | 2024-11-20 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| dc40b27c-e3a5-31c5-81aa-5d7a8f01c9f1 | -1.2017 | -53.6769 | 2024-11-20 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a68ad5bc-52e3-3ece-9306-a283e26f94ba | -11.092 | -54.6221 | 2024-11-20 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 52d38867-c243-3c08-8cd1-dbe9c894fa28 | -2.6212 | -51.7997 | 2024-11-20 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| c2e677d9-6e45-306b-b01f-4025c58d8f1f | -5.9556 | -48.0642 | 2024-11-20 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| d52232f6-033d-300c-9d21-322a7b2899b5 | -11.0917 | -54.6425 | 2024-11-20 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| af8be873-8242-3594-878f-7e4065a72cc0 | -4.4405 | -46.5754 | 2024-11-20 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5f8dc4c7-ac0f-3eee-809b-deeafe4ab9ad | -11.1109 | -54.6204 | 2024-11-20 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| e6f09af2-22d7-3c47-94d9-6d46fbb48410 | -4.4592 | -46.5745 | 2024-11-20 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ecb1e5a1-066e-3c42-8719-b38b337efd5e | -1.8613 | -54.2714 | 2024-11-20 03:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5813672b-7ec9-3d61-ba40-35432d4d0cbc | -3.8021 | -47.7887 | 2024-11-20 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 51bf9bf0-2ffc-3638-877f-c1af81604a45 | -2.7501 | -51.8171 | 2024-11-20 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 9e1794d5-5c51-3f60-be6c-1d5b1907cd7e | -3.2014 | -54.3243 | 2024-11-20 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ece17428-21c5-3777-ba54-3bfb4f63782e | -5.9556 | -48.0642 | 2024-11-20 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| fef349df-bc34-3db7-9b8b-d439e2a47139 | -4.4592 | -46.5745 | 2024-11-20 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2125c374-0f92-3001-a35e-42e47f6299e9 | -3.2194 | -45.5622 | 2024-11-20 03:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 00c4c7f4-77b0-3d0f-a6a3-fcd73f1d47f5 | -3.2379 | -45.5615 | 2024-11-20 03:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0a224ecb-f192-3817-bdea-2c137d3bc6f6 | -1.2017 | -53.6769 | 2024-11-20 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1ad4e7ba-d82e-3acd-9ca9-53b569ad4930 | -2.75 | -51.8377 | 2024-11-20 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 91727d47-5ed7-3416-b8a7-ac78e5454df0 | -3.8205 | -47.8096 | 2024-11-20 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 96198d7b-9af8-32c7-90b0-abf1d0ada3fc | -5.9742 | -48.063 | 2024-11-20 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 5680f726-eca0-306e-a344-09d2b3a9e802 | -2.7316 | -51.8382 | 2024-11-20 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 22dfc6fb-9054-37a2-81fc-8ed1a82283c0 | -2.7317 | -51.8176 | 2024-11-20 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 1a4e024d-b80a-3b25-b74b-746b3add2bf5 | -3.802 | -47.8104 | 2024-11-20 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9c191f18-176c-3f9e-af4b-2314652ef00e | -11.1109 | -54.6204 | 2024-11-20 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a70ae3b0-77f9-3bb8-8190-dd64faf5f188 | -1.73214 | -45.58993 | 2024-11-20 03:32:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccef3202-e484-3a17-bb49-8a1321e80a7f | -2.26382 | -45.46554 | 2024-11-20 03:32:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c145d72a-adf8-301f-ab3c-c7cc245e92a5 | -2.88545 | -41.7638 | 2024-11-20 03:32:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c60cf53c-a1ba-3f30-b814-a477eb478377 | -3.78434 | -44.06837 | 2024-11-20 03:34:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 790333d2-9f08-3a15-9a55-947fb2849f6b | -5.3951 | -45.13617 | 2024-11-20 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 138d825d-d0e9-3f59-93fa-5967fce8ab55 | -9.4981 | -43.19164 | 2024-11-20 03:34:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d75d9f1e-fe47-340a-bcaa-abb877e2d320 | -8.73728 | -44.09449 | 2024-11-20 03:34:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5803113e-7939-3e20-99a2-23f8f5eb8c4f | -3.5968 | -43.62872 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfdde6ed-2341-38ab-afcb-57d1da115c47 | -2.74738 | -45.70892 | 2024-11-20 03:34:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42747cf8-3648-3b64-8b89-2d06e86c7c42 | -5.59446 | -46.17724 | 2024-11-20 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c6c29fa-ffa1-3906-97ee-2d0fd2360b8f | -10.49226 | -42.5119 | 2024-11-20 03:34:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a2ae1ba-7c67-3332-8e13-769294bc3439 | -2.99193 | -45.44614 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4444fd8e-a338-35ee-8095-9f065f4f95b8 | -5.41848 | -44.70961 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45658f71-b808-3653-b25f-eef3afa606f4 | -10.53988 | -36.73341 | 2024-11-20 03:34:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42d3efbb-1a31-37b2-bad5-805bd25aead9 | -3.77829 | -44.06732 | 2024-11-20 03:34:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe19c51d-a982-3827-9749-df0dfbcdb666 | -8.0005 | -44.3889 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2cc5a7c-65b4-3e99-9884-7da73b9985d9 | -5.41934 | -44.70474 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 117dba02-2323-31ca-b03d-f6e0e38147e4 | -3.36877 | -44.42939 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ede8bfa8-6df2-34e6-b2f4-1b6555ada653 | -9.19979 | -35.36813 | 2024-11-20 03:34:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40a4b191-ae0e-312d-96ae-b878f6017e76 | -9.17043 | -44.72588 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d2d6876-0003-3bc9-8a0a-cf2338278e66 | -5.50764 | -46.44735 | 2024-11-20 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4c5abc8-88c4-3cb6-94e5-dd16a40e702a | -7.99973 | -44.39302 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32d8c490-9a5a-3d3d-b7d4-40aa6505be1c | -5.24978 | -43.83539 | 2024-11-20 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbb10fad-21c6-3aa7-aa12-170cd8179066 | -6.53614 | -44.18853 | 2024-11-20 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70d6fb0f-45aa-3ca8-b7c0-3f348aeeeffa | -5.44855 | -44.82827 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab54cf7-dcf2-3d23-8207-748a44f29643 | -7.74333 | -35.11927 | 2024-11-20 03:34:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1aab0146-b68a-3b1d-bce8-9443ef02d276 | -3.05376 | -45.13406 | 2024-11-20 03:34:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8dc9de4d-9303-3cd0-807d-02127a300bcf | -9.43407 | -39.03002 | 2024-11-20 03:34:00 | NOAA-20 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 81c64ca7-c871-39e6-b53f-11bbea498fb8 | -7.15552 | -39.35693 | 2024-11-20 03:34:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README18.md)
