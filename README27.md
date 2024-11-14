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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c528ba9a-aafb-3e87-81ef-373f9f0f1595 | -3.41002 | -50.37423 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd9e8da5-dc40-39af-9e83-b3e64e6a5f59 | -1.60723 | -52.49689 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5bec989-c204-31f5-9f4d-f06d99681078 | -2.66914 | -46.81352 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dec257af-5cd0-3c4d-81de-65fd18a55b27 | -4.29877 | -48.10188 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18938986-7d86-3fc8-b392-0963d6ab04ca | -2.64716 | -45.80132 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f256ad10-1b49-3491-8beb-6c9729a22cfa | -3.78225 | -46.0581 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ea455f78-be30-3fff-b25f-1bd92c62ee50 | -2.40536 | -45.34156 | 2024-11-14 04:40:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78f2c924-1571-3181-abb0-e3df6cd52fc5 | -4.29814 | -46.87357 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be21660f-ca8c-3ffc-aa0c-88bbc86675f7 | -2.63877 | -46.53637 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31b87ea6-63a2-3488-b0ee-5a1dc347e16d | -2.64373 | -46.18178 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7bfb560-9187-3274-a0eb-7ea03f01db1b | -3.96946 | -46.70432 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d47deadc-7eb1-35ca-b2df-210b99a3e990 | -1.40412 | -51.11449 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f7c819-492c-3e64-9b83-1f9139e8b9ab | -2.3471 | -49.12352 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed29903-fb04-3b23-a2f7-4288911bf434 | -2.45082 | -48.02322 | 2024-11-14 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9c9bb0-70e0-325a-abd0-2069d7d150d7 | -4.12161 | -48.49928 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9a65c2c-d391-3dde-8c69-4526684a2da3 | -2.23696 | -46.83965 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dce1271f-3648-31c7-93a0-fd1d94860cb3 | -3.67206 | -50.7399 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ebf6524-fcc8-30e3-a39c-5a68fb41d412 | -3.67153 | -50.16095 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6397d911-6176-32dd-abcc-653585558b35 | -3.13234 | -47.46897 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 856979dc-8e45-39f2-94f1-0035fb734abe | -2.89204 | -46.84692 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7586d618-e099-3638-934a-9c5a2a77bb82 | -2.63532 | -49.52297 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2751ba37-31d5-3404-b629-388a4c45b58e | -1.20998 | -51.76806 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ae6a888-9d48-3f32-a2a3-615302820581 | -2.20285 | -46.81172 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf07bb2c-81c3-3aaa-b5bf-d71421b9098f | -3.89171 | -50.07986 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a305427-8955-3c72-ab84-ea456e0c2870 | -3.87348 | -51.04213 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f8d1c3-2080-3f07-ab2f-4f8da4c33ffd | -3.14783 | -45.48253 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1af9ffa7-f2f8-31d8-99ee-0c4914652a1a | -1.49239 | -45.6328 | 2024-11-14 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55e36431-76b2-3e63-b8fd-e14c78519513 | -2.92781 | -47.02574 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753bd5a7-08d3-3f62-86f8-cda439e55f30 | -3.94988 | -48.99154 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7b49c26-8017-36d4-aee9-a3fa3588de98 | -1.46853 | -51.48563 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2c6b584-eb0e-3648-bd91-cafce3774b68 | -2.81651 | -46.65567 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e89a4f9-a7c6-31f8-9c14-289bca04fd3c | -2.60858 | -46.1764 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95811deb-2bbd-3be9-a8c5-b97fe75d2c61 | -1.26993 | -52.17244 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7986c9ce-e6c5-3cb2-9789-354470b1da7e | -3.05323 | -50.32597 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1bfc36-db5c-3a91-a3ed-5fe564fafe7d | -2.65136 | -46.17892 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba104cba-7f26-33f7-a1a7-eef7e1e4ac81 | -2.02994 | -46.92813 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 770466df-6d38-3341-9338-b5cf5399ad9c | -1.8479 | -53.69018 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91b234c9-b4ef-30d2-94fc-62cc3231b00e | -1.65105 | -47.47803 | 2024-11-14 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfd95b0e-9e46-34a3-9fc3-30f7eed8cd53 | -1.24923 | -51.7784 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bcb9368-87fc-34f4-9d45-14142b73ede0 | -2.37887 | -53.87286 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2063676-1079-37b1-a114-b97a33ad922c | -1.4035 | -51.1184 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e39578e-4174-3f5c-a797-47f90bb50a08 | -4.80253 | -45.29607 | 2024-11-14 04:40:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68862d9a-d103-31b2-98f2-a9d4612961c9 | -1.49 | -51.12304 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ef85f4-73c4-3829-a8b4-055cda207fd3 | -1.05235 | -51.74212 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3caec3b-b8c3-3150-bd1b-042f35dc825d | -2.34614 | -47.97507 | 2024-11-14 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b67ce9ce-86a5-3f2a-8de1-bc95b50f5532 | -1.23866 | -52.15417 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e40285-8141-3e94-8c03-12e80624fdbd | -3.94711 | -48.9876 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e496f17-81c2-3320-a08e-71968d5eee00 | -3.80043 | -47.45995 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313a9dc4-155e-3cb0-a160-19508e9b14d9 | -3.64314 | -50.59438 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12c04a93-0840-37ab-bafc-9750b6733032 | -4.3815 | -49.92849 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bde950a0-c02c-3d72-900a-01e77a7eb990 | -4.36937 | -50.81113 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83b67b34-da19-330a-b9fe-609b35a404a7 | -2.17133 | -48.44265 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33a2650d-6e2b-3067-8ca3-ca17b314739b | -4.15542 | -45.77406 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed285fe5-4f55-38ef-a47c-6d0bfa761b30 | -3.17607 | -50.45574 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb79e21-9960-3a82-80f4-64b1f6022597 | -4.02934 | -46.54676 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c841756d-27e7-3ca4-b6d6-81fedbaeb5e2 | -2.20525 | -48.39864 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c0064f-4a25-3808-90df-bfad96f31be5 | -2.27025 | -50.67813 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e09fe0-8e10-3a43-a1ec-1a96b94f6951 | -1.8561 | -46.28437 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd860221-37e4-3e45-97af-5045f585a883 | -1.13659 | -51.68512 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f0249d9-c879-33bf-b0ae-379041cd01f7 | -3.7751 | -47.48938 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ee3fa5-5f13-3d9a-a19d-991f3901973f | -4.37818 | -49.92798 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 980c3e3a-42e2-3a13-9189-c5ea9a9d2ca4 | -3.92184 | -52.26525 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc09ca7-82cf-3fb2-be5d-84993671ac34 | -2.37588 | -48.52707 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0c1a042-8713-388b-909f-37f4db51f80e | -4.2095 | -50.49944 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 152065ee-01d2-36e9-a308-f973556e4dc5 | -1.22614 | -51.78346 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 467e20ac-eaba-34db-98da-d86d4368d6cf | -1.36815 | -52.33577 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba0daff-f265-3012-b1c4-c1734156c392 | -2.59138 | -48.19067 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b0d965-58b1-314f-95ff-a5f917fa0817 | -2.96799 | -50.50459 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22f231c-4d34-35c0-aa79-d882c7c420b3 | -4.12988 | -46.9385 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e97653-8100-3cdc-b737-9b6d36bced9e | -3.86905 | -43.93655 | 2024-11-14 04:40:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52f6a8d9-0bdb-3491-b6ae-ffc4f806db44 | -1.04807 | -51.74578 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a0b1aec-b2f2-319f-926f-1f6c8ff91b1a | -1.63066 | -52.5191 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d27507ff-983d-3165-b702-b7a40cef3b78 | -2.48917 | -47.7758 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a817a130-4283-39c8-b835-8a7d02f45b15 | -1.57073 | -52.02436 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b32d04b-a3f5-3574-ac65-25fd646109fb | -2.26288 | -48.46732 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 012dbecd-f51e-3c07-81fe-3bdbfbae4261 | -2.90356 | -51.79257 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caed75a4-c9a5-32d0-84f1-c6292e1bc4ac | -2.31099 | -49.1814 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93a67088-a902-3fa7-986e-eaa62f5f226b | -1.21228 | -51.77702 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ab8a82b-36b8-3782-b133-f3c2d13898ca | -2.88919 | -46.84266 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f110c7-27db-39f0-b2cd-610bec16d511 | -2.72974 | -51.7417 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02e5a210-21eb-3d9e-aad5-80f0ed7254e0 | -2.68649 | -46.70136 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e597913-ca10-324d-a5e4-40e100050612 | -4.35936 | -45.99063 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60e9b74a-10f7-386c-8277-8a6cc81eee67 | -2.21032 | -53.75106 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 255755f2-105f-3f5c-ac1e-98afde980536 | -3.71406 | -50.60544 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 08964bfe-b553-3d57-81f9-c785c34ae81e | -0.79228 | -49.49561 | 2024-11-14 04:40:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24f799f7-5107-33e9-8965-a6360eee95df | -2.82282 | -46.66051 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb6ad36f-7917-38c1-a2dd-52a419c01185 | -2.32218 | -49.088 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce0d7ff8-d049-3fbe-b202-287a957da75d | -1.36306 | -47.29646 | 2024-11-14 04:40:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b98f69ce-d227-3467-999a-b9e91e84840a | -3.16293 | -50.58321 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e0db5003-d6f8-31c3-ac9b-035580ac0f40 | -2.3498 | -51.98426 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33e7d4ec-31e2-30ee-a251-16302544ef35 | -2.18757 | -48.38186 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1723144-c098-377d-b00a-b5b5a6316711 | -5.19376 | -44.3539 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c33233-9b76-3426-a8a6-6ae7180d77a9 | -1.80527 | -52.17598 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 74042439-cd21-3626-b506-524373c99381 | -2.29203 | -50.89508 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea478c91-290b-3b6d-875b-8afe4300de9b | -2.92611 | -48.07242 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede62db0-f945-3879-b376-81a55579ec7a | -2.63424 | -49.52991 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d91944c-4e34-33fe-81ac-3ba53b7a7bfe | -2.15726 | -53.63523 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49cb27de-8d6c-3817-97c0-9eb4c1e75cc0 | -5.03215 | -46.83829 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c548056-1d6d-3891-879b-fa80faf60693 | -1.24495 | -51.78205 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b570b7-af40-3766-81a5-a201071d5368 | -2.72909 | -53.19957 | 2024-11-14 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README28.md)
