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
| ffd3802f-6dad-3c0f-85ba-5fff4f1bf62c | -2.2729 | -45.3245 | 2024-11-14 03:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 2f4e59a4-700f-375d-9dd9-b33428bb7039 | -17.5675 | -57.5351 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 0bffa6b3-0bb7-38f6-bf67-a2adbbfee9d7 | -17.5672 | -57.5557 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 4cb75377-f504-342b-bfac-a123449b6125 | -6.0472 | -44.0331 | 2024-11-14 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 21e755a8-e076-3aa7-aae4-43bcb99318a2 | -2.2729 | -45.347 | 2024-11-14 03:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 142.2 |
| ef97b331-8fca-3a43-92c1-e2ad094ed825 | -17.6263 | -57.5486 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| c97e4987-bc80-3f1c-b130-a7f50ee60aec | -17.5869 | -57.5533 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 4ccf055e-98dd-3128-9d48-98104462929a | 1.048 | -60.5986 | 2024-11-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 60ce7743-fa83-34ec-be54-a9e335e9a687 | -17.7052 | -57.5392 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 179e9c1d-3a1d-31da-a4f6-612c75694155 | -1.2228 | -51.783 | 2024-11-14 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7e1a03ac-0dad-3fe4-9a46-7b6a9a79ece3 | -7.78409 | -34.93398 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 633a6947-f026-303b-af9f-3da9089bbd4f | -6.96662 | -35.24932 | 2024-11-14 03:00:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c1e460c7-4d58-3af8-a35c-7f11521efdf0 | -7.7848 | -34.93006 | 2024-11-14 03:00:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 60fcbc89-2688-3b55-aab0-242046f0da11 | -7.78191 | -34.94595 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3ca6e14e-7282-3400-ad00-e32c8f22f4c8 | -9.73187 | -37.45342 | 2024-11-14 03:00:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ccab4548-50ed-3030-a4e1-6a641c64dbf7 | -7.78337 | -34.93794 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| bd660ac2-d41d-3bd1-bb05-87394ff998dd | -9.93405 | -37.62029 | 2024-11-14 03:00:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bffce9a1-96c9-3689-85ab-7ed36484ec81 | -7.78983 | -34.93488 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 463aad72-007d-3232-ac04-6a1b871b140e | -7.78117 | -34.95002 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7307a1ff-c142-3dc4-b486-536924fdb6d8 | -5.81686 | -35.38455 | 2024-11-14 03:00:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 2377a472-66f2-315b-8e9f-9b59ed3f7303 | -7.78912 | -34.93882 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 908d8865-7e53-387d-b6fa-f6729f2a9688 | -7.7884 | -34.94279 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 931370b2-29a1-3a3c-b4da-6535d843b161 | -5.81567 | -35.38664 | 2024-11-14 03:00:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0e0f9632-6690-36cc-888a-7f19030a5220 | -5.81648 | -35.38197 | 2024-11-14 03:00:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4e8e9050-8850-3b8a-addf-bae20c056c3e | -6.96738 | -35.24513 | 2024-11-14 03:00:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9e9480a2-8f52-33ee-b53a-b47290af5bfe | -7.78264 | -34.94194 | 2024-11-14 03:00:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3e8fb15f-06f5-32a3-8a7b-7ec8f5de2365 | -10.52391 | -36.81747 | 2024-11-14 03:00:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 851a8a8c-9749-3d29-8e47-4df99e94f644 | -17.5672 | -57.5557 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 5da23c90-9e95-3aff-935f-a8d3e1e77107 | -1.8105 | -52.1857 | 2024-11-14 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a3a6b455-c206-358e-a79f-286c562cc654 | 1.3034 | -60.4263 | 2024-11-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e9b663fb-193c-345b-923e-a59120bfbe8c | 1.048 | -60.5986 | 2024-11-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f1837584-f0f8-3384-aee6-ec4bf326bcb1 | -17.5869 | -57.5533 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 4eb8f5d6-5d0b-3713-875a-409b524d7cea | -17.5872 | -57.5328 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| a90e1c13-e4d5-3bd1-b995-e165f662b6b5 | -1.8106 | -52.1652 | 2024-11-14 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 59cfec64-6b3b-343a-b87a-ce354d60b3c1 | -1.7922 | -52.1655 | 2024-11-14 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 1a5817e2-a365-393f-b4f2-684b1c53bd45 | -1.7921 | -52.186 | 2024-11-14 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| c5a56f45-3da4-3b33-a2a1-dfbc9c69874c | -4.5614 | -48.0141 | 2024-11-14 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8e0b5b47-993a-3526-861f-2535abae21cb | -17.7052 | -57.5392 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 3419547e-5cd7-3e62-a0f1-b70c87e1c10f | -17.5675 | -57.5351 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 3ebb0abe-1e94-3fb8-91b5-e14c7d87e557 | -17.6066 | -57.551 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| c14eedae-5d5a-352f-b46c-e41f0872dad7 | -2.8791 | -51.7932 | 2024-11-14 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8db1eb73-b952-3626-a4df-dc356fc11e04 | -6.0472 | -44.0331 | 2024-11-14 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6186e6ba-2c6a-3a8b-a3b4-8124bb239847 | -1.3894 | -51.1197 | 2024-11-14 03:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a7eb061b-30ac-3368-a402-2723710bc7c3 | 1.2852 | -60.4265 | 2024-11-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e30a4a3c-4eb3-33de-b21a-23e124a3b4fb | -2.2729 | -45.347 | 2024-11-14 03:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| f51975f6-96ac-35c7-ab15-b90dacab2747 | -17.5879 | -57.4917 | 2024-11-14 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 325f24d6-89f5-38cd-b702-ed5e30d029fe | -17.2543 | -57.4698 | 2024-11-14 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| cf617983-fb8f-311d-8310-6a6f5ad0dbac | -17.6076 | -57.4893 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.8 |
| 7c5d2c3e-54f1-3652-9aff-268b5c60094f | -17.6066 | -57.551 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 648d6b53-b636-3d2d-ac88-8e0a7fbc72af | -1.3894 | -51.1197 | 2024-11-14 03:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b21f2834-eaee-32f8-ad88-25e569e08689 | -17.5675 | -57.5351 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 5d3b4e80-0243-3bca-a6ff-eddbcaa7289c | -17.5672 | -57.5557 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| f7a4aa81-1d46-39c2-8732-05ff2504fa73 | -17.5872 | -57.5328 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 0da3da19-d1d1-339d-9290-87fdf9b3593e | -1.7921 | -52.186 | 2024-11-14 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 77e76487-34c7-3b02-8a91-1387e909c973 | -6.0472 | -44.0331 | 2024-11-14 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0fd5fdfc-d64e-3c1c-b569-c3cb69019a62 | 1.048 | -60.5986 | 2024-11-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| db230f3b-c6d0-3a5a-a5dc-6facf6e4c386 | -1.8105 | -52.1857 | 2024-11-14 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d29c57eb-cc74-3835-b69c-1a7f4534bca2 | -17.5869 | -57.5533 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 7e51da42-6962-355e-9fcc-f80d1ed393d1 | -17.6263 | -57.5486 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 5057a6d0-755b-3fad-b285-48378c6b2e55 | -1.7922 | -52.1655 | 2024-11-14 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7c4f0fe5-6c2a-3a63-8a0b-cd0086fba398 | -4.5614 | -48.0141 | 2024-11-14 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 081e047c-b3a1-3dc5-9a34-58ca92be205c | -1.8106 | -52.1652 | 2024-11-14 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| cc1bc900-246d-3f88-a15c-8acd2ec95d3b | 1.0663 | -60.5985 | 2024-11-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6d993604-19d8-3973-a7eb-41fc3e3fd73f | -17.2543 | -57.4698 | 2024-11-14 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 3a25f76c-a4e4-3351-a7a2-f7d87f245033 | -2.2729 | -45.347 | 2024-11-14 03:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| fa85c748-5c5d-3548-a7b0-4e291059580d | -4.5616 | -47.9925 | 2024-11-14 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0c69b1ba-8589-3785-b323-bbc28647872b | -17.7052 | -57.5392 | 2024-11-14 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 7ac22094-426a-384f-9771-d7ca11003348 | -1.4078 | -51.1195 | 2024-11-14 03:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2f0f34a8-f7a3-3640-87f3-204f57bcf74f | -6.04722 | -44.03786 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4d699538-a352-34fb-a4c6-2f2ff445ff5f | -4.14471 | -43.85471 | 2024-11-14 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6752343f-3922-31d4-b6ab-52bbcc2e1a58 | -5.81666 | -35.38476 | 2024-11-14 03:21:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d74d002c-4642-33cd-aacd-2c02029db4ad | -6.60312 | -35.32791 | 2024-11-14 03:21:00 | NPP-375D | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b24be362-8515-389d-912e-ce1fae4ab43a | -8.39038 | -35.02631 | 2024-11-14 03:21:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b17fbd07-7035-3268-87cf-dfc3ead720cd | -3.01509 | -40.21001 | 2024-11-14 03:21:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c82ba556-cb0d-30e7-94f9-9b8a7d439822 | -8.8171 | -35.67307 | 2024-11-14 03:21:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 91d114ec-1d56-3b48-8d59-d91d86e16ff4 | -3.77782 | -41.59506 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 49e8e776-d85d-32e9-8592-91fdf663b34d | -5.93405 | -43.78093 | 2024-11-14 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 542b9563-83bc-3c30-965a-12de03eac4e2 | -5.93284 | -43.78753 | 2024-11-14 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a21c51a-431d-369b-9685-8bbef58dc687 | -7.06819 | -38.88083 | 2024-11-14 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5f981fc-761c-3edd-abec-bc1f439a67d0 | -6.24889 | -35.15658 | 2024-11-14 03:21:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 270f1ee7-6e11-3b4f-b6a1-0db27d93b182 | -6.04275 | -44.04493 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d5bc764c-1f91-34d0-b607-00574c3861c1 | -8.82018 | -35.679 | 2024-11-14 03:21:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d1613055-5ae7-3bd8-a4e5-f8cb79e4ea29 | -6.62267 | -35.18845 | 2024-11-14 03:21:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| dbaaaafa-a86c-3cda-aa81-eb0b7bf97a4e | -6.52661 | -35.26456 | 2024-11-14 03:21:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f39c0bb9-8984-3380-9008-bc36376bcc7f | -7.22405 | -39.96371 | 2024-11-14 03:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 250d3c4b-42d6-37a6-97d7-ed43676a30f2 | -9.73494 | -37.45539 | 2024-11-14 03:21:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 43246648-78c5-3b92-ba8d-c323cd371d5c | -6.04406 | -44.03765 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 447f847c-0829-3b4f-8609-96e856041191 | -3.77862 | -41.5956 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90f1d5ba-8311-32f2-aeb5-e29cc35fab1a | -8.82106 | -35.67384 | 2024-11-14 03:21:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 83135e91-8655-3965-9b0b-5745e7592021 | -4.1434 | -43.8543 | 2024-11-14 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa6e3e54-ed75-3262-9efa-bf6556a1eaee | -5.93986 | -43.78891 | 2024-11-14 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73069079-e2db-3926-bb6f-dc3dde7d8579 | -5.937 | -43.78654 | 2024-11-14 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3b10784-e311-3e96-9d57-99a7a88c191e | -4.13756 | -43.8529 | 2024-11-14 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01e57843-083b-39bc-8b44-84c44227a76d | -5.81973 | -35.38477 | 2024-11-14 03:21:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ac3d489-d470-3a99-a463-9d538f5e5599 | -6.95835 | -39.83308 | 2024-11-14 03:21:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bcf37849-4c1a-34ab-b1cc-0e2a7d73aff8 | -7.22949 | -39.96473 | 2024-11-14 03:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c95033c2-03c3-3df4-aa83-d491de6e245e | -3.02102 | -40.21101 | 2024-11-14 03:21:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 08bda122-1e4b-3bb5-92ef-b5dec964019e | -6.06021 | -44.04713 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a75ca74d-d791-3fcb-9041-3472dad90066 | -5.35923 | -43.54932 | 2024-11-14 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c4e8d7-4e8e-3c6e-8e54-d00b929642d4 | -3.77049 | -41.59942 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
