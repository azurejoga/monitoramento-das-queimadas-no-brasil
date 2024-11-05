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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd272aba-97ee-385e-b656-19d41dbb964c | -5.58442 | -41.67855 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c16250be-8e4a-303f-b849-2ad766e281f5 | -5.44755 | -43.2616 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f5d052f2-f784-36b0-a9d4-45d87d172427 | -3.54171 | -47.39518 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9183341a-6586-3805-85a9-57d67e746caf | -4.60816 | -46.87512 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| afcb2639-a8b3-3bd7-886b-97d514e47a15 | -5.06601 | -44.2248 | 2024-11-05 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a921daf-7d34-3a96-9b98-95dad8b3c2ba | -4.07357 | -48.31261 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7350dd62-016f-3027-a123-6afaf0cb0d40 | -6.0303 | -44.02852 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 234a5a91-cc72-311b-a7da-35ed8a4499a1 | -2.18456 | -46.37909 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42ca63e3-47e4-32af-81e0-4bf420983da7 | -2.18879 | -46.37973 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc034883-a15f-39d4-9ff0-f6eb3f5bc5cf | -7.49025 | -37.30352 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5059d0a4-e55d-312d-9aa8-79120b49f37b | -3.54615 | -47.39588 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fcac9e7-a49b-3ccb-8bad-284fff0402d2 | -5.80948 | -44.13646 | 2024-11-05 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 765bb790-402b-3b2f-acc2-94413de9e6c9 | -8.32366 | -43.59579 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883c4323-922e-3949-94c6-240237de58a0 | -4.4074 | -43.11159 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fde5ab49-0564-3998-94f0-be5797dab16d | -5.30377 | -46.24961 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa061cc-2b7c-3c49-8709-360316095fc1 | -5.71394 | -43.92021 | 2024-11-05 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6f9fe1-62e2-36d3-9e30-85d512da316b | -4.57599 | -38.61282 | 2024-11-05 04:08:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4a6993c-9728-370a-a830-1b6ac1671313 | -7.55692 | -38.77057 | 2024-11-05 04:08:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b45e150-7dc9-36f6-a575-3e67d6a3d9e7 | -6.11424 | -43.97414 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08ccb45b-89b1-3430-9e14-2d49145a83af | -2.65182 | -48.5634 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| bc9a3d3e-10ec-33dc-9632-64e1e5b45d07 | -5.60855 | -41.65404 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 641d767d-39c3-3447-a594-ddedc1dd72b2 | -5.06764 | -44.23752 | 2024-11-05 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66034a31-8003-34ac-99c2-7e63801f8a34 | -5.10121 | -38.44221 | 2024-11-05 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 091e268d-553b-3cd5-bbe9-8ba2a7d02463 | -4.81386 | -43.22786 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5696950f-c773-3aa2-b86b-9500b6eb4e8c | -4.23294 | -48.54055 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fae1139-3f4a-3902-aa66-bfd189c77fee | -4.14168 | -46.83416 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857f75c0-d747-3539-a8c5-07db977d342d | -6.3096 | -46.69254 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b64c305-51b3-39a1-a036-a881efad4f86 | -2.81112 | -51.48773 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c36eb31-6779-36ca-bc8f-cb35956d2e82 | -7.54298 | -35.13261 | 2024-11-05 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0232445-7afa-3fc8-96fb-5c61c7ef8739 | -7.40826 | -35.16146 | 2024-11-05 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee6bcf43-acbc-37da-9289-536e0067151d | -6.28422 | -43.38921 | 2024-11-05 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 756b776f-fb05-3f37-9dc2-5d0a9b51ab75 | -4.8952 | -46.70942 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6023e40d-150e-3ad1-afe8-1388caad17e1 | -6.46864 | -42.22312 | 2024-11-05 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51b06e48-3222-3b46-a9fa-67cb675ff8fc | -6.50997 | -41.4147 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| faa25ad5-055d-3069-a9d6-9f12b10c76c7 | -4.25991 | -45.56371 | 2024-11-05 04:08:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3b1215-b61a-38e4-ba03-28aa0851e4c8 | -6.0067 | -44.62727 | 2024-11-05 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00117363-5c64-3720-a3cf-391c35c600c7 | -4.41788 | -43.11275 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffb8c7ee-f071-36db-9920-b82ab57686f9 | -3.9072 | -46.43905 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a12dbf-7aaa-37ed-af36-0b8878df9e6a | -3.4535 | -47.66702 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05fa50ef-a1ed-35fc-8c00-f59c9d7ac4a4 | -2.71382 | -46.67594 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47946052-ff68-39c6-9cef-658dfe06c380 | -2.80228 | -51.47884 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18b6235a-4e62-369b-9ffe-0e9142a8497b | -4.54624 | -46.41386 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0470e330-1030-3a51-a4e2-229e5087672d | -3.55134 | -47.39193 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 42f58aa6-0920-3f4f-adb5-217c0ea0b596 | -4.93651 | -43.62703 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 630c7fd2-5be9-3edb-bbed-b34560a52bba | -2.21654 | -46.39594 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c135b3-bfa1-34e3-871a-09d3b1b40876 | -2.64608 | -48.56799 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| daa20bf9-df83-34d7-9090-1e206aae8c75 | -8.34344 | -43.58038 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d74879ca-09b6-3c78-b2b7-995287df57ce | -5.244 | -40.98274 | 2024-11-05 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d85342e3-9695-3e87-8283-c99ec5bdc0f8 | -2.6567 | -48.56419 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 326a0802-57ed-3b25-8441-a1614d4a6a68 | -8.31585 | -43.57961 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c337d4db-9b53-3704-9b36-d9005beb16be | -5.83177 | -43.65148 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ded16460-42c9-331f-b7b4-b3448d3299a4 | -3.03774 | -53.26783 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dc41722-29aa-3e1a-9bd4-235a5022312b | -4.26515 | -50.60993 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a268b8cb-8841-3d90-8f9a-c6c63d55a404 | -5.51495 | -48.08312 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc59b984-25ea-3814-a1be-2cc600680c9f | -4.75567 | -44.54837 | 2024-11-05 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9650a3e3-68e5-358d-b51e-6d02638c11fb | -4.05162 | -46.93315 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ec9e7b2-16ae-3a9e-859c-c2fea96f999e | -5.2586 | -46.15078 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73bfb679-32da-3448-866a-d2970d56d6f5 | -3.55866 | -47.37503 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4a6b4465-aad4-37cd-bdd7-c7eaa3bdf194 | -3.49552 | -51.07873 | 2024-11-05 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| beda7b28-9a8e-3c57-b8cf-47dfb33533ae | -2.66072 | -48.57032 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e5970b55-f917-3055-b341-f7343e20d9bc | -2.812 | -51.49353 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8d2ec118-4856-3fb3-8c97-9d5ff11ee5d0 | -6.1943 | -39.23107 | 2024-11-05 04:08:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b098358-d177-33d9-a1ae-f3f75d03b149 | -5.34515 | -46.48476 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8191cad8-7e82-384c-8687-648264bf1d04 | -4.6046 | -46.87057 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c3afc353-e7c8-31c2-93b4-636afe1ce916 | -8.26237 | -44.85588 | 2024-11-05 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3700cbdb-aa7e-3559-a0bb-159e90a962a8 | -5.76437 | -46.37805 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 832162f8-92db-360d-bfc6-8830b9435b0a | -6.65738 | -41.41 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac6fb71d-fad2-390c-8b86-3a36098ae6af | -4.26365 | -50.72336 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91001a6-e90b-30d3-851b-786ccc22ed47 | -5.48747 | -40.92572 | 2024-11-05 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 01341209-6f85-381c-b4e1-a27debc24f6f | -4.25751 | -50.72613 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4748174-3070-3d57-83e1-11ed04b68035 | -6.25187 | -43.57018 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 031b8b3e-a36a-3e16-9411-8d3201b8fa82 | -2.63363 | -48.03081 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd21b98d-e1d6-3062-b4d6-50c8748aff7d | -7.24578 | -46.04586 | 2024-11-05 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e89ed8f-c50c-3b2c-8a54-332f61fbee6d | -6.42098 | -44.59711 | 2024-11-05 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 171c0005-d9b9-312a-95f2-2fd9a70600dc | -5.941 | -43.64942 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3770590-5814-3230-9d5f-1b686187a450 | -3.31926 | -40.03765 | 2024-11-05 04:08:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b07ecc15-0520-38f3-be7a-1de679a80bdf | -4.34806 | -43.52441 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c1ba741-8829-337e-8991-9ec707a888db | -3.42991 | -39.02821 | 2024-11-05 04:08:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eb12aec0-8383-349f-aedb-6dabfd084351 | -2.63834 | -48.03155 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88a1797f-1c23-3684-bc48-b50b6e738e5b | -5.66211 | -45.20728 | 2024-11-05 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbb4083b-2865-3e98-a844-f10dc755850d | -5.93186 | -43.6402 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d87646f2-6581-330d-8260-eef4ff40fb9a | -2.28454 | -50.67174 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f9239e1-4626-3851-914e-6f3aac36d67a | -6.8458 | -38.90199 | 2024-11-05 04:08:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8bc884ab-78aa-368f-9728-ca943adcf79b | -3.00977 | -45.84669 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 42df8d89-dee7-3094-b488-c45b93844278 | -4.79209 | -43.78306 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e3f895a-8de7-3252-a8e1-866ff591c44e | -4.05948 | -46.93853 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5697a000-96d7-3856-bef0-f5c2888e4c41 | -2.92253 | -48.31346 | 2024-11-05 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d322610-7056-334e-8660-7a73202cdb80 | -6.11138 | -43.96968 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e832a961-900b-3372-9098-25ee784523df | -5.34347 | -46.46969 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1087b290-f03b-39bb-8a1c-52041d85c55d | -5.44472 | -43.25736 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a3ce845-cec4-3f93-86a9-9864eb359afa | -3.85344 | -44.53419 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 428574c5-a5d0-3bb3-a6b3-f2754b3ce02b | -3.54765 | -47.38671 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f7070b5c-b57e-3fa1-b724-aa37d53dc6bd | -5.61577 | -41.67282 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39419916-eaa2-3175-a864-edaf2590f6b2 | -3.94444 | -45.5717 | 2024-11-05 04:08:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1e7227ee-2728-3a30-9a7f-b7d2bae6c673 | -3.54975 | -47.37392 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6cd03f99-dfcb-39c7-a559-7d6df01c360b | -6.10215 | -43.96024 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b9521f94-9366-337a-b0e1-d6fb9732cd50 | -5.22454 | -47.47143 | 2024-11-05 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df62d837-d1a4-3981-bcd9-d09b0f9aaaf2 | -3.70267 | -47.62237 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33fe726c-e0df-37e3-bb3d-0904a88e7cff | -4.41024 | -43.11584 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| addbf3cc-ca62-3d0b-8c3d-af64959c858a | -3.31594 | -40.03714 | 2024-11-05 04:08:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
