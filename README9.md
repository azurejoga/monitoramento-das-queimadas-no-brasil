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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee8c9e46-4e0f-3ded-a519-ca1769ad7ab8 | -2.4163 | -53.6633 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7907ec05-4848-3343-818c-5f9f468f685a | -2.9459 | -49.502701 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1207df8f-52e1-3279-9b96-5809a6adb64e | -2.8367 | -54.015598 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12c5f8bc-c43f-390a-8d68-4e9d7321a4e8 | -3.6673 | -50.212502 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a9f7b3-56de-3564-b13d-33c14125ac72 | -3.0183 | -50.977798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a9310c-6770-3246-a2f4-f2bf805c7d8d | -3.0902 | -53.318501 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33315352-8bc4-3420-8e90-4e0c04932d21 | 0.1744 | -51.089901 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 01ab400a-e172-3ca4-9f28-6b74e88de83a | -2.1666 | -46.4268 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5ed38ff-de4b-394e-8330-009a386d8db7 | -3.5774 | -52.245499 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a4fddc-1a00-34c1-8073-a5f15579ce88 | -2.1858 | -53.691799 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b282bc2-9bcf-3de2-b2b5-5209bbe7600f | -3.2451 | -48.748402 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68e846cd-5bec-3d33-9ac6-06962eca59fa | -3.3077 | -50.487301 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad6a56e-11d9-33cd-9753-6e22a5bef7a0 | -3.2456 | -50.307598 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2705a89-f18f-3b99-a7ae-91b37ac8ea01 | -1.2196 | -51.7701 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29598a6-94b0-3ab2-abd5-4343bbd295b5 | 0.4639 | -50.951698 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 97b1079c-7ede-3ab6-8288-82bcc13ca8e2 | -2.736 | -49.1759 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efddfb85-7854-3ca5-95b7-4123329a2b36 | -2.9398 | -49.4319 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af28f3f-7cff-379b-a1e5-108441252e84 | -1.5758 | -53.7295 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04ce185-9d69-32fd-bdef-983e4f22ad0f | -3.5218 | -53.494099 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df2af6cc-b87d-36d4-80fd-f5d8a0a113c0 | -3.669 | -50.219601 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e2487ba-7942-38e3-a35f-e102521f25aa | -1.218 | -51.763302 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837bd3f2-0332-35d4-afd1-4fdfebb3d76d | -3.8657 | -51.973 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b70b37f-9550-3db3-a347-f0315c7e5c83 | -2.6906 | -51.7062 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf94ac0-97f1-31d3-b50d-a70204a6d512 | -3.6385 | -52.332699 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa14d016-c945-39be-8eb1-9dac70126f73 | -3.6657 | -50.205399 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a7fd9b-c655-32ae-9d3c-b88203d497fb | -3.5688 | -52.297798 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541c9333-03a0-3d21-b9ef-5268b1d6e532 | -1.5631 | -51.289398 | 2024-11-11 00:51:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe19bc1-e389-30cb-b55e-e1e481e98e8b | -2.2997 | -48.452 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd927de-cb41-35ee-8dc0-97d0146cab8a | -17.2686 | -57.479099 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b3ada86-0480-3da0-b915-f0fc6c2ff03a | -3.0536 | -53.882 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 943c3e79-f945-3586-90fb-089308768e26 | -2.4201 | -50.486099 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92c95b3-ef48-361a-a083-f020812a7b08 | -5.9687 | -45.3536 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebd5d6ed-c3c9-335c-81dd-520568da7a39 | -3.6771 | -50.2103 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da65cb91-f21b-3d42-9466-fcdf59bdb97b | -6.1241 | -44.93 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60cf5d66-9517-336a-bab1-b1e613b04745 | -3.2473 | -50.314701 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05d6eebf-a79c-3c0c-90b6-4d2435579a93 | -2.8402 | -52.539398 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4ba424-4fe1-310f-8099-17ff95bcb77b | -2.8748 | -49.373901 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d94fcee7-98ac-3b06-9a06-2de8b5ab8d9b | -3.4583 | -54.621799 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a6a83c-0416-30e1-be0c-23d3e6a6a972 | -3.3565 | -51.686001 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccb45e92-6baf-323b-83b2-0eee6e83f4e4 | -3.0829 | -51.079201 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ab5ac6-bcc3-387a-9c5e-057e7c8c7dfc | -3.1019 | -49.4193 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e58ebf-190b-3d55-8fea-d81da0c08221 | -2.5676 | -54.734798 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f516894-7fae-35ff-8964-34321a8a3b7d | -2.7562 | -49.352001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e10343-53b1-3b46-a2ff-276edd388beb | -2.9551 | -48.034901 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e56e2cd4-c6e3-3083-991a-9ec5c7d49464 | -3.2381 | -53.062801 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe71bfa-78b7-31a1-87a2-297cf4020a69 | -3.2566 | -51.5653 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb43f742-d87a-31bb-9c9a-fdd9b988b4ec | -3.1032 | -53.330502 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084533f6-8e62-3240-924b-d718c9aa1744 | -6.1338 | -44.9277 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12d08df1-c6c7-3002-91c8-6cfad5fec106 | -17.583799 | -57.499599 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 461d512a-5327-33ef-b9bb-61f781325417 | -1.2249 | -55.801399 | 2024-11-11 00:51:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67209447-be07-369a-ac2f-4f64379ce78f | -3.8993 | -52.209801 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d839911b-3ba4-3930-a981-2c1e40d72d61 | -3.0903 | -53.273602 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba50cb0-e2aa-37a3-ae0c-29d2d3fe4bbc | -2.7803 | -52.864101 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bcb7239-ee0f-3ee8-b6e3-45be8ee501f2 | -2.3817 | -49.8284 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73df195e-ebe5-3a65-a2cb-fe04ee31211e | -2.7133 | -51.715401 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a9c091-df25-3914-a7e6-6861e1455835 | -1.2273 | -51.9832 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37f6c70c-5467-38cc-b07c-897c945b36c0 | -2.2492 | -46.515598 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ee6d01-0de9-3d9a-8777-94f2d06b5b47 | -3.2283 | -53.064999 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e171974c-8327-3408-af29-0d4f0cef5d73 | -1.6357 | -55.210098 | 2024-11-11 00:51:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9528c8-1deb-30e1-b984-fb9467c38c1d | -2.9354 | -49.368301 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85a762fc-badd-33db-8a67-cfee42fd4ba6 | -2.7064 | -56.528099 | 2024-11-11 00:51:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4d9447c-7751-3f14-a2a3-50a82a1099fc | -3.0184 | -45.806301 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd57cc0f-77e4-3188-acea-624fa3d0d225 | -3.5927 | -44.546902 | 2024-11-11 00:51:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a225295-08da-3fd5-ba59-b268962d1bec | -1.4924 | -51.744999 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06fe3325-1626-3337-b586-b839dcf02207 | -2.6077 | -47.738998 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8750eeae-ef2e-32e7-b198-d2ff405af362 | -3.4695 | -53.490501 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b812b63-9ee3-3644-8b6c-7138b8de269a | -5.9716 | -45.365398 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 632caf46-fbbd-34a9-acd3-47de52789030 | -3.0464 | -49.5359 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97afafc-a478-39f6-a049-25d39078d88c | -1.2 | -53.619301 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a05aa7-8c62-35fe-82e8-742dca1727f2 | -3.2299 | -53.071999 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 438e87fc-c496-3370-8e28-b0a8fd1bcb64 | -2.9822 | -45.2631 | 2024-11-11 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54a08ff2-498e-3ed6-ace1-65abb4d232a1 | -1.3336 | -51.4133 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50102b3-5185-3db3-a376-f80c5240d5fc | -2.1003 | -50.2174 | 2024-11-11 00:51:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6056c6-d1ad-3474-8cd6-68e1d7001263 | -2.9345 | -52.771599 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f64797-6f07-3c13-8cb8-f2e24a9e6663 | -2.8303 | -49.137901 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07be2ff9-0964-35a9-9dd0-620181b415f9 | -3.7001 | -54.644299 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8b8c9b-7b39-35dd-91ce-68d414fbe8f5 | -2.7732 | -49.380699 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5ce458-1236-3e2e-b90e-d16a511c52a1 | -2.6332 | -49.533401 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 606408ad-e761-383d-b7d0-b4939e72b3ff | -3.2289 | -46.217999 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69403771-498e-3fc6-b26f-923ce8cf75ce | -1.5169 | -52.211399 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d54eff-b344-36ab-94a0-7c6ec99e767b | -1.231 | -51.7747 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d849d2b3-13d2-311c-8906-89ed98094845 | -0.9742 | -52.4538 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac8112f-0f79-3fee-9918-be085550d5fd | -1.6326 | -52.535702 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97be8dc8-8f2f-3f78-aeeb-f0efaf8a54cb | -3.244 | -50.300499 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfbc265a-4b06-39a3-b935-4976852dceeb | -1.5365 | -52.207001 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae39cb8-c161-3fea-b610-9eeab0fa714c | -3.2817 | -53.6618 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fbbdff7-3e22-39cd-b153-c5626c76b7e5 | -3.0241 | -45.8307 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69991d8b-76bb-38be-8a8e-f32b1e70bdd6 | -4.1185 | -49.131802 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d3cff2-6785-38e7-b371-7610c282e00e | -1.3352 | -51.4202 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f5552f-1418-350c-a03e-9474f17d8f10 | -2.7118 | -51.708599 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6513f89-a3f7-3228-835c-41d9cd04c77c | -2.9865 | -46.9809 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43bcc0ba-9162-396a-a97f-d380b15b9584 | -2.5909 | -51.721401 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1cb6e3-f954-3240-9685-bf8e04bab8c2 | -2.2299 | -53.659401 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2192ac57-5a7b-3a65-956e-4d452bb2d686 | -2.7819 | -52.870998 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a39f6a8d-c901-3b1b-a051-53bab8866057 | -17.5832 | -57.439899 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1302d8f-9aa3-338b-8938-c2285e945194 | -1.1788 | -52.086899 | 2024-11-11 00:51:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f1c9a077-db51-3194-b014-77b6f36a782d | -3.0805 | -50.486599 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbfc8542-ba87-31b6-8336-5825d1a3639f | -1.6212 | -52.530998 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c08517d6-49ee-3945-95fd-e3395fe674e9 | -17.2943 | -57.454601 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 83f4be50-19be-3120-9bf2-34b8de7ab851 | -3.2719 | -53.664001 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
