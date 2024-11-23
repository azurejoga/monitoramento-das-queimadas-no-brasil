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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc74ce82-0a95-30f7-acc5-ea7fec11a312 | -4.6761 | -45.66256 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2c8e5b-5bff-3b95-a6c6-4e1252ed1798 | -3.90142 | -47.94138 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17b6dc7f-9b04-35f2-9714-7bb5ef153373 | -4.67028 | -45.66739 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2466684-49c1-3e98-894f-c8552872946d | -5.22464 | -44.9067 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a998c61c-01f4-3121-b3a9-cad70c896e2b | -3.96777 | -46.64266 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d32d2ee-bba2-348e-9f5c-1a841d83bfaf | -3.70748 | -47.61858 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7890521-8743-3a4c-954d-017bc48d4a5b | -4.11833 | -43.23565 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cf884c8-c078-3e53-b8ac-e0567f5ae151 | -5.57383 | -46.29131 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa87b1f-6d86-3af6-842a-b1c619f7e75b | -13.29297 | -39.80371 | 2024-11-23 03:55:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3a1561b-4f51-3788-8395-52fa13bf5456 | -5.66196 | -47.34011 | 2024-11-23 03:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2da447e4-a0e4-3aaa-b88e-64a81c54fa7a | -6.40214 | -39.1235 | 2024-11-23 03:55:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 25f8ac4e-9b3c-3817-91e2-33311f16afd1 | -3.66484 | -51.57217 | 2024-11-23 03:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19f16db1-e05c-363d-bb58-9debd11be0f5 | -6.5024 | -41.48565 | 2024-11-23 03:55:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1cd6c94c-9a74-3ee1-9762-c4935ee2fd09 | -4.72657 | -45.49702 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5dd84625-dd1e-3af6-aad1-0e1c497d53b3 | -5.54274 | -45.78876 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e98e830d-825a-35be-a966-92bd79681f5a | -4.34236 | -45.88487 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914fa272-8577-3987-93c6-9c4c19760bb6 | -3.67191 | -47.14011 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff2d2025-06ce-37bd-aa75-03e7fac32598 | -4.11769 | -43.23944 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd6da22b-7d51-30f7-aa6f-2b15f0d4fc8f | -4.53748 | -42.91678 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5e71134d-c787-3d98-b7c6-0e14d0389e68 | -4.25561 | -48.69844 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7547b0b9-d75b-3e57-8fc5-6c175e1eaecf | -3.47017 | -47.6866 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6cbc60b-d416-3943-b9f8-a59949dc1bbd | -6.04933 | -44.82685 | 2024-11-23 03:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7751f0f0-2d56-3ca4-94be-e9145f9ee1d8 | -3.6725 | -47.13651 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed51d2e6-68e8-3ec3-aaba-fa411529e856 | -5.74851 | -46.26263 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fca97ea1-5399-3720-9f14-3bc868ed8f13 | -3.96675 | -46.64887 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f4548f66-d9df-34df-a21c-1a44a2514791 | -4.26822 | -46.28959 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 058fec3f-f55e-3cc2-ae25-7819ace1144d | -6.34661 | -39.79346 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ec67e80-f213-3997-9a0e-ad61e0bd8e28 | -5.95303 | -44.46641 | 2024-11-23 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ff5a24-9870-31c5-90eb-62891ad47648 | -4.16344 | -46.80573 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d92020cc-7c20-3a6d-a563-7a7f519b2062 | -4.90466 | -47.4171 | 2024-11-23 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cee07817-f2e0-340b-a050-8b0f965921c5 | -4.55455 | -45.81343 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e031fbf4-acd4-3c68-a789-464b56b20f4d | -4.70693 | -45.85133 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 71f88390-9ca2-33e2-8300-7a89f1976b6c | -4.60746 | -46.50576 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ba20f0f5-6182-39a9-8d80-f3aeff8920d7 | -6.63106 | -37.97891 | 2024-11-23 03:55:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63cc34a1-d03f-371d-a903-b53893741576 | -3.97209 | -46.64946 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c24a1453-0131-3ba6-96b6-a4ac0f9436ed | -4.91301 | -47.86151 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c4c24ca-5f92-3f24-acec-ab95d6351801 | -4.41715 | -49.69476 | 2024-11-23 03:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5614eb8-08e1-35c0-9f4d-8283648f53d9 | -4.75014 | -49.10009 | 2024-11-23 03:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc91b395-3084-3a41-aba5-b417b9d56ea5 | -3.97081 | -46.64593 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b09434d1-5e47-34eb-852d-863cf53999ce | -4.27335 | -46.29049 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf88bcf7-019f-35d9-ac17-e134c000b018 | -4.02505 | -48.86654 | 2024-11-23 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4b91065-8bdd-32ad-974b-77e3d7402b71 | -5.46431 | -43.2421 | 2024-11-23 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c3ffbc-27ce-3779-9329-071bdaea9813 | -4.42465 | -44.11794 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4ad64a1-6d54-332d-8a2c-d091d7277a85 | -4.03617 | -46.19474 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3db4d0e1-b8f4-3c62-a643-565533ed89f4 | -5.1234 | -47.03325 | 2024-11-23 03:55:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1f97a91-365a-3f6f-b325-6bed6c179759 | -5.20371 | -46.81875 | 2024-11-23 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4a3d41b-8172-3a2d-a495-5d9398e3c3f9 | -5.10389 | -44.03526 | 2024-11-23 03:55:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 629ee6c5-c00d-3cc4-8ddb-6fbddd7aba58 | -6.56386 | -39.76798 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1191b56b-f84e-30ec-83ef-75cdd8ccb83e | -5.29314 | -44.86543 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fe5b46fa-7c54-38c2-b7c5-503d98c196f8 | -5.65777 | -45.2025 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de82006-0145-3896-9e7c-a3d1a7f03274 | -6.08847 | -43.54152 | 2024-11-23 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 497f49d0-9821-3c13-a1c9-3056776e79a3 | -5.22516 | -44.90932 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4456bd1-ba91-36b3-926e-54b90a059c0d | -5.759 | -46.25422 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37aac011-a37c-32e8-8816-8c678ff9d358 | -11.9394 | -44.55214 | 2024-11-23 03:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc4e51c7-b1d2-3514-b857-c1bead6c7fe2 | -4.66029 | -45.67879 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 03afc8b7-84b5-39b4-9f46-8f6b8a814cf5 | -3.94507 | -47.96244 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf430084-4879-36e7-8aca-c6559fd74fdb | -4.53341 | -42.91608 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7d957abf-b58f-33c2-8916-e7960f7ca8ef | -6.04025 | -42.22694 | 2024-11-23 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e05484fa-959c-3482-b326-cbafd1aca383 | -4.66352 | -45.67783 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6e8ff726-3f12-3722-b316-71d94e0a99cd | -7.01633 | -39.22461 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 94e93b15-f12c-350d-ab8e-77ff79df9fd0 | -4.7077 | -45.81647 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 560882ba-aed2-3a19-a002-74c5454d1768 | -5.56335 | -46.29196 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47814c4a-bc50-3ab9-b34b-1aaed4d7518c | -4.534 | -42.91251 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 069b30fb-1ce0-31bd-bea2-ef0b25c6e92a | -4.42023 | -44.11718 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d5104ae7-bb1b-3a22-9bb4-7ed3818d4740 | -3.68132 | -50.11309 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41d83dc0-d57f-3e20-a708-022e6f79926f | -4.91368 | -47.85756 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b553c0-0a52-38f2-9c2c-0b16d2c7a4a6 | -5.29393 | -44.86073 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 14be0e16-137e-353d-a900-7c277a95e8d7 | -5.12937 | -47.0305 | 2024-11-23 03:55:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 564e4727-dc16-3b39-998b-0f5242ff1023 | -3.99913 | -46.93263 | 2024-11-23 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b1d668-488b-33e2-ae98-f1a0526f4e25 | -5.22056 | -44.90848 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 936685fa-7628-3dad-b51a-a186ceec5135 | -4.66618 | -45.6739 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 615c82ae-0f9d-3541-a1f1-4e05eb9f0d8a | -4.28448 | -44.81182 | 2024-11-23 03:55:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf755c33-ef15-3c47-9f7f-e6161005a410 | -4.17705 | -48.63547 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 780dc64d-da39-338b-affb-aa9cb05ac186 | -12.10844 | -44.75151 | 2024-11-23 03:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aef0cb3d-0738-3318-99f1-f08d5f26bd7e | -4.59174 | -46.07402 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccfa3a94-e960-37df-b883-70440e7059b5 | -3.89627 | -47.93674 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89fb82f7-704f-3a0b-bb00-248093db25ea | -4.6586 | -45.67713 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f180fe47-648d-3ce5-b75e-e1e907e91691 | -5.86397 | -39.66483 | 2024-11-23 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 88aacc71-2083-367d-bcb2-c493a5a243dc | -3.95117 | -47.96357 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 938a306d-cc37-38ea-9828-94cc505846b7 | -7.01242 | -39.22765 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86ccf09b-efc5-3dd9-9b82-1230fa7f189f | -4.02496 | -48.86992 | 2024-11-23 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe167bc-18e5-3737-9a86-a87d91b41586 | -5.1284 | -44.29118 | 2024-11-23 03:55:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55d43065-7cdd-3e4e-86c1-97668e8e4ca2 | -5.27917 | -45.18565 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5623c17b-9ffd-3ef0-b55a-13c17c4855dd | -4.54287 | -45.88161 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 039d069d-9f10-3fd8-8402-1bb9da481f3c | -3.80357 | -51.33902 | 2024-11-23 03:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecad936f-53e7-3cf7-ad00-fab57de6a8a7 | -4.26768 | -46.29274 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdfc43eb-508c-3a5e-9043-71e8f9b2b308 | -11.7791 | -44.635 | 2024-11-23 03:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e85eb87-c96c-33d1-b6c6-b2d6e9f9ffa0 | -4.01247 | -44.33851 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bd52cfe-9bed-33a8-bfe3-69df262f5d94 | -4.69199 | -45.84924 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 744d29ed-7fea-3d51-a99c-4bdf986e97ce | -4.60376 | -46.49603 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e24dd908-ad3f-3f13-a808-1765b10ac54e | -4.25641 | -48.69389 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 00480668-88f8-3373-8d61-e8c6d7f9ebdb | -4.94872 | -47.80614 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6eef5f8-9ca5-3604-89b6-08c877cc18d6 | -4.60797 | -46.50273 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 241be12a-17cf-3512-a020-a359f486dad6 | -4.03775 | -46.19526 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6acdef31-fd98-3dda-9e9e-380c495a6a47 | -6.35341 | -39.79452 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b151faa0-c4df-3550-a814-17b4deb2057b | -5.1293 | -41.55792 | 2024-11-23 03:55:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7992f09f-4fcf-3142-9574-b4a6daca6f4b | -4.22011 | -46.15825 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2222e886-b596-368a-92a1-3daaa72e6a7c | -4.09677 | -51.05993 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2def7c42-b975-3c96-ae1a-8a30fd30c0f6 | -6.13732 | -44.72881 | 2024-11-23 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a9314ad-7dca-3b04-a326-936f59ce48c4 | -6.91733 | -40.06763 | 2024-11-23 03:55:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
