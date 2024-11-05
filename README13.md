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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| def0830f-7741-374f-a2ee-8d728e1f4fa2 | -4.23747 | -45.6761 | 2024-11-05 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cafb9faf-90da-399e-9089-970df6568df8 | -3.54542 | -47.4003 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7fe58de-a57f-3aa4-91e0-44639311adc9 | -2.66282 | -46.74659 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574f71f3-7d6f-3f12-b98e-07b731916fdd | -4.45859 | -42.19565 | 2024-11-05 04:08:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cdc5cef1-d5bb-33d4-8536-c7a367731d83 | -6.14653 | -43.43868 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ac8bec3-7acd-32a8-a305-b86bd597f2f8 | -5.22345 | -45.80112 | 2024-11-05 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6502cbc-d182-3561-ab6d-e89b08f8374f | -3.00516 | -45.84962 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5818dd5a-8ea2-3aba-aa7d-d59cdb878898 | -6.52649 | -45.93304 | 2024-11-05 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0226784f-790a-337c-97ea-f0db94717522 | -5.06893 | -44.22942 | 2024-11-05 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6ddfa9e-4c31-36e8-9d37-ad5cc6408fe8 | -2.81268 | -51.4894 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee0cd0f3-db62-3612-b316-c8cb11befbdf | -2.6594 | -48.56643 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 85c83539-c9f0-34c0-9079-c2fecbc00550 | -3.94951 | -41.49498 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dab87f7b-6b85-323b-9038-2275e3cf604b | -7.0434 | -38.72046 | 2024-11-05 04:08:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| faa80594-b4f5-35da-8bb3-2b3414d83e55 | -3.22708 | -44.41712 | 2024-11-05 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 158cc07f-0ad9-3c3e-b3de-26f9d9da540a | -5.30629 | -43.20181 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65428ff0-edf6-30da-89f1-340f904cbadf | -5.9404 | -43.6532 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a45a62c6-5cd4-35b6-b23f-4adde135e837 | -4.9017 | -46.72184 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9d0e81f-eda3-3930-a029-e98478afa5c8 | -5.15897 | -45.57884 | 2024-11-05 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5bebec8-0c20-3ae9-8e79-8855d83f8b49 | -5.4638 | -46.22457 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b93ef965-5fca-398b-92e6-759f36475d98 | -5.46837 | -42.82409 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5075fd4a-a89e-3a2d-a379-92c4f31f8341 | -5.8525 | -39.42413 | 2024-11-05 04:08:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7373c220-be60-3e68-aa4e-eae68f22482b | -8.5437 | -40.47898 | 2024-11-05 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6d795a99-497a-3788-b317-889aefbd0848 | -8.34624 | -43.58452 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4998a552-d5dc-3bba-b83f-a231f466200b | -5.93591 | -43.63695 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7e8d5be-b9fb-3aa4-9a0d-1fe3284d322d | -4.35273 | -45.90803 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 174776ff-4200-3111-afb6-36f34f47f1ea | -4.05522 | -46.93783 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cdad6507-3102-3de9-bc88-72c85f0fe083 | -5.93695 | -43.65265 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f66adaea-90d6-3fd7-991b-12f7cc46ea73 | -5.22283 | -46.7239 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b3f519-a7ad-384a-9082-a6e4f0389de5 | -4.88926 | -46.71981 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec9d5d3-36a8-3cc9-bee5-d215b97c2fc2 | -5.15944 | -45.07037 | 2024-11-05 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2a18cfe-46be-318d-922d-1fe56b7ff4e2 | -5.83522 | -43.65203 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 190e5cac-a9d5-373b-97c9-d44c423aca56 | -4.60224 | -45.83368 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f44eaca-7e2d-309c-8533-7db8b5d80607 | -5.93971 | -42.66401 | 2024-11-05 04:08:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f37a0f5d-924b-369b-aae0-3047f91b1d86 | -6.11486 | -43.97023 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97e3a3f0-e0c1-30fe-ac31-30709c070b6d | -3.0424 | -53.2799 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fea53dcc-fc5c-39c3-b096-27b6cedafb06 | -3.53948 | -47.38107 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b27075a4-a3b3-3015-b471-fc1872067dcb | -3.51467 | -40.3557 | 2024-11-05 04:08:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26b581fc-d459-3346-a1b2-3e0d7817079b | -4.75862 | -44.55318 | 2024-11-05 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da6d4aa7-abca-3259-94fd-9bea2f50cd3e | -4.26427 | -50.71979 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f7a8007-7487-32a5-b6d3-6c1b242185a8 | -3.70342 | -47.6179 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9da87867-8936-387d-bb74-18449e3a905f | -5.46725 | -46.22843 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5231402b-910f-36b9-a9f8-e9634fda0928 | -4.42646 | -45.84917 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 055b38bd-0292-3375-b300-487b95cb2170 | -6.30724 | -42.03726 | 2024-11-05 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9abc9dff-f362-3c05-bec6-9c7ea9e328ba | -2.80707 | -48.66009 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 036c6331-5dcd-3db6-9d8e-d9d75099dcdb | -3.96033 | -46.37241 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a488a64a-8b4d-3133-8d5d-05b80a86c8c7 | -3.46823 | -45.52914 | 2024-11-05 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30bb6b2a-7f5d-3f5b-be10-dc735fdeae5a | -4.60106 | -46.86586 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e23a8f42-b834-3006-a513-0f27439a8bfe | -4.23211 | -48.54557 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a79965a-8dc3-35ca-b5a8-7336549be661 | -3.03859 | -53.27163 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 213508b8-8bfa-38c1-87ae-2b229c8540d3 | -5.60633 | -41.64663 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89ad29b3-a8a6-37e4-baaf-186ddc1d595d | -2.29942 | -46.50128 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ae58545-7655-312c-9a55-a56ce0968e2a | -4.34873 | -45.9076 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d16f15-ee9f-382c-b40b-47923f9e6ef9 | -5.8565 | -39.42092 | 2024-11-05 04:08:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7717e5c7-094f-3b49-ad52-78faa5e32ccc | -4.25714 | -50.72627 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8793f63c-4151-3334-ad5b-b7f39281aa30 | -5.5432 | -43.47889 | 2024-11-05 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97b9a647-97a0-39bf-b636-5b09cfa6c2ed | -6.12123 | -43.9752 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa3cbeb6-3fae-30d2-b8ae-6388b3f24cef | -3.45806 | -47.66756 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 981345ba-5b13-30eb-a5fd-b67205807f75 | -3.78919 | -41.6074 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3810d0b-7dec-357b-a360-52cf2201c368 | -5.07336 | -40.70152 | 2024-11-05 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0581962e-b49c-3453-ab69-e4bd87e5abf8 | -3.30652 | -47.0076 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d9a633c-e29f-3bde-b584-07e1baf35b9b | -5.47009 | -42.81329 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddb2d37e-f701-397e-9d36-f339738a3275 | -7.16415 | -40.2113 | 2024-11-05 04:08:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ecf8a84a-912f-3def-945e-f1f1748eadd9 | -2.95215 | -48.61812 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e89138d7-3991-3915-82cc-239c6ff0eba4 | -4.7203 | -46.4229 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96e9f4fe-0a59-34f8-8be9-e6395cab8400 | -3.15476 | -46.49695 | 2024-11-05 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ccf205a-defd-3101-8160-92f794238868 | -3.85409 | -46.15105 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b28b3c4e-7a19-3d13-9398-be1f0d97e817 | -2.91974 | -48.05886 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4a1e4d9-17c3-3934-a2fd-5adcbee59246 | -5.12259 | -45.15638 | 2024-11-05 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 627e95cd-2184-30ef-86ad-04103a8bd674 | -4.37125 | -47.23789 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6772453a-cb2e-3e1c-9d0b-8060d45f8519 | -2.08682 | -46.50198 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d4f0020-1f10-3ca0-9a83-7ddf84fd0abe | -6.30669 | -42.04074 | 2024-11-05 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df8bdf2f-e0b9-32bd-bc5b-4f99ccb2b264 | -3.35437 | -41.66715 | 2024-11-05 04:08:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 72991509-d078-38b2-a4ed-51de7b0291d1 | -8.34942 | -43.62996 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc6c5d8b-2ccc-3c0c-9842-476abab22a14 | -2.81704 | -51.48865 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b4c9076-3bba-3a9d-82dd-1ce4c3739b8c | -5.91405 | -44.7193 | 2024-11-05 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c74b4b3-3229-3165-8096-dbceb855b6bd | -6.51878 | -45.9319 | 2024-11-05 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58281435-ba60-3f49-ae1b-d60aeac0f47f | -4.54213 | -46.41335 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 748390e4-6fdd-310c-8842-8d525c3d7531 | -5.83237 | -43.6477 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d14133e4-12d2-3717-931f-8891310cba22 | -4.4516 | -45.86874 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 137701b9-ea27-3cdf-a3ed-25323a9d252a | -6.06152 | -44.2605 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99a641cf-ead0-3449-b618-ea2fafc6890a | -5.61246 | -41.67231 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cf0f97a-cd09-3690-8285-aa157ebbb77d | -7.54647 | -42.85413 | 2024-11-05 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35f3090e-808e-390b-a27e-2699e34d9fbb | -8.48666 | -42.17834 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a814a602-4800-35e8-8b24-cb4bef67c70c | 0.04939 | -49.56214 | 2024-11-05 04:08:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89c16bd5-99c5-3feb-b614-899d0e6a9760 | -4.41386 | -43.11592 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f817bb56-1773-3965-a7bc-407c867309d4 | -2.65362 | -48.57101 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7f60f2df-0d9c-3d43-ad55-94967ceede10 | -3.30585 | -47.01175 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57c132da-46f4-3778-b4dc-661d8fabc445 | -5.46951 | -42.81689 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6914273a-2d57-381d-b901-8892ac4ecf08 | -4.62603 | -40.18635 | 2024-11-05 04:08:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61776ec9-85be-3035-8184-d5f29e8220f6 | -2.84049 | -48.45575 | 2024-11-05 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e6f8e1c-2abc-33fc-97d9-df2a8222c788 | -5.4199 | -48.14289 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f99e4138-0ab8-3d62-a88d-6a44e804af1c | -6.98918 | -41.30991 | 2024-11-05 04:08:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02895c3e-2111-3b33-8c59-aa2c60281de0 | -4.66225 | -43.82379 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33c2cb47-969b-3221-a0e5-1a4f6dfa6a6c | -5.00466 | -46.89584 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cfc367f-a5d4-3203-918d-a74afc8f7570 | -4.41103 | -43.11167 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0ab700f5-2995-397e-b359-533500d16f7b | -4.74474 | -44.10159 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89cbd190-b81e-3f4b-b2f7-7ffaf08425ae | -2.17749 | -48.86238 | 2024-11-05 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 448e53e2-f0f9-3b7f-ae3b-250f9d1a4ab4 | -4.91333 | -44.36129 | 2024-11-05 04:08:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3781e960-ba36-34b1-b46b-bd37446a679e | -5.16388 | -45.06649 | 2024-11-05 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc254865-a33b-33e9-9b58-bc2c6a345733 | -2.79642 | -51.47757 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
