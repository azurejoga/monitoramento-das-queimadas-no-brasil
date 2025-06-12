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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7da955f2-4639-3786-9ea5-8b04a4d9b6e6 | -10.6587 | -49.352901 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dffdce71-4c8d-323d-ba36-8fcef0572a7a | -10.2361 | -52.2411 | 2025-06-12 00:44:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68660460-c6e6-31a9-a92e-688ddb30848a | -12.212 | -49.628799 | 2025-06-12 00:44:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8db59f7b-cd60-3a54-a870-d8627a2ae433 | -7.4587 | -45.512001 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9d702ae-024c-32a6-81ad-46c4474c50c9 | -10.4231 | -49.771599 | 2025-06-12 00:44:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f541b5b4-69f5-34cc-9745-3b6e2eaa9052 | -11.9848 | -57.219299 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c740491-b1eb-381b-a39b-3964bb19e5a2 | -10.705 | -49.5135 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8d37aa-3426-3747-b3d4-72eae61cd553 | -10.655 | -49.428001 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83d992f-51bc-35da-a01a-2da30fecd79e | -9.2782 | -48.263901 | 2025-06-12 00:44:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f399c567-5e1b-3f78-bffd-a98d802cc116 | -10.6534 | -49.420898 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9122ade9-d7e0-35c0-84a6-eb81836366a9 | -20.6061 | -48.872299 | 2025-06-12 00:44:00 | METOP-C | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30925843-fe40-3588-8e4e-56d993543023 | -12.3838 | -45.767799 | 2025-06-12 00:44:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 967a08e8-83c3-3280-adf8-73c04df4ab35 | -13.2862 | -57.070599 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce3dd72e-ba02-360b-a006-8c6314b315e8 | -10.6619 | -49.367001 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92407005-98d5-3042-8052-7aa43d7a257f | -6.9561 | -44.573799 | 2025-06-12 00:44:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0f3e342-0d94-3167-a502-a5f90c28e546 | -9.247 | -57.522301 | 2025-06-12 00:44:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c783ce0-9e2b-3206-9685-2242b6f1d319 | -10.1421 | -47.445301 | 2025-06-12 00:44:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f82be056-e997-3e74-b2bb-dd8ae00399d1 | -14.2007 | -45.497799 | 2025-06-12 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be67511b-3e6e-30cd-8fd4-5097ad209b0f | -8.312 | -47.919899 | 2025-06-12 00:44:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd83b23d-72cd-3400-9f1f-37e8534c8614 | -10.6648 | -49.4258 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65f3122e-0eed-38be-a98a-15000e1b85c8 | -12.0607 | -48.077702 | 2025-06-12 00:44:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4761be5f-ea54-349e-87b3-f1386ae31cad | -5.6549 | -43.621201 | 2025-06-12 00:44:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33528130-3858-3220-986f-fb2eb41e6aa1 | -10.6518 | -49.413799 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4278d84-cd61-317f-aba6-247be423b2ca | -11.5747 | -47.4394 | 2025-06-12 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91871b57-edd2-3b5b-a99c-90259701d07e | -12.3856 | -45.775501 | 2025-06-12 00:44:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 351218b6-c3cb-3194-86d2-f490d17ea866 | -10.8889 | -54.746601 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc1729c5-ed6c-3020-9d77-f5668f635160 | -10.6483 | -49.444302 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42f96b8e-1b6d-332c-9988-3de327853bdf | -10.7082 | -49.527699 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1f8ae8-1fb4-3a1f-8925-0792764bc82b | -7.4706 | -45.518501 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78d67301-17e3-3e27-9ded-3c8648d4c008 | -14.0328 | -55.133701 | 2025-06-12 00:44:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10c0bd3c-c9c8-3b70-813d-4c55dedb183f | -5.9041 | -43.459099 | 2025-06-12 00:44:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a20aa304-5b6f-3dba-96fc-1939eb7f2c7a | -12.1165 | -48.874599 | 2025-06-12 00:44:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15e5f068-709f-3521-95fc-ca1c02722397 | -10.8617 | -54.321701 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f46e506b-a19e-392c-8778-8fe843fc0773 | -7.1992 | -47.437 | 2025-06-12 00:44:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 661d69fd-c5d1-37e3-9151-38e92162cfe0 | -6.9537 | -44.563801 | 2025-06-12 00:44:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5031d84-0fad-344e-9ccb-ab6cdbb27a26 | -13.8974 | -48.7384 | 2025-06-12 00:44:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f9dae481-f989-3297-b29e-5af46921ab33 | -10.8817 | -54.7616 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed07ce8-6197-3e6c-a6d7-1cc1526bc3a3 | -13.2998 | -57.0891 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e11f6bab-289a-35cb-b64e-18598acda085 | -14.1793 | -45.494999 | 2025-06-12 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbdda7b9-e1f8-3ebb-b5ee-441cd705eff4 | -10.8791 | -54.7486 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e678133-318f-3d28-b84b-76feb5dbf3a7 | -9.2509 | -57.541199 | 2025-06-12 00:44:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18e34ab9-0de1-3596-bf30-cae67708a49f | -11.9907 | -57.197498 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1459c74c-65e8-3196-8623-221f5d43cd7d | -13.9056 | -54.6498 | 2025-06-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0513c04c-07b3-3564-a28d-49127091db2e | -7.4575 | -45.5116 | 2025-06-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 00fa6c8e-1a09-3e4e-93d6-0fa558f94ce5 | -10.669 | -49.3597 | 2025-06-12 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 6cfcbbd1-7465-31e3-8c7c-64996584d2f9 | -11.9874 | -57.2076 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 078960e1-1ef0-3ea6-a750-741dc136c50e | -13.2989 | -57.0734 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 239b321c-8f59-3745-986f-6eb314dde955 | -13.2798 | -57.0751 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| baa952d6-40c3-34bd-b529-dab5081f09b0 | -5.6577 | -43.6001 | 2025-06-12 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b9752929-ca22-34c2-af50-72a7442fb259 | -12.0063 | -57.2061 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| bb47dc49-232e-3a4b-8f55-b6cf603becea | -10.8832 | -54.742 | 2025-06-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b2b276a5-4309-3d12-98c2-ad1ca7d554e7 | -7.4572 | -45.5342 | 2025-06-12 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 1276b68c-0e6d-3b01-b872-0db1bf7ec1e9 | -7.4763 | -45.5099 | 2025-06-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7c2deffa-286e-315e-85d5-6f6e1f6b0567 | -12.6979 | -58.0257 | 2025-06-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 16f71d98-4842-393e-983a-cc1c249ea2f4 | -13.2986 | -57.0935 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 1949b06c-8978-3e05-9cab-31e7de38bc0f | -11.9278 | -57.4717 | 2025-06-12 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a8d5a9e4-dfaf-34bf-9e89-234e83661b0b | -13.8864 | -54.6519 | 2025-06-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9ff2d6b2-17a2-3a51-bb21-1f291e55d790 | -13.8867 | -54.6312 | 2025-06-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 28eff413-c557-30d6-9090-e143dd2b8497 | -13.2796 | -57.0952 | 2025-06-12 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 23f4bc14-41f8-3f76-b7fd-7e925d75b397 | -10.883 | -54.7624 | 2025-06-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3c74d727-74f9-3abe-af3d-7c3e07c2aef3 | -10.883 | -54.7624 | 2025-06-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d4f46ac7-7570-3a9b-b4d7-b62180d6e79b | -11.9874 | -57.2076 | 2025-06-12 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4417bcdc-8b66-3243-bc5c-0afb01880630 | -13.2986 | -57.0935 | 2025-06-12 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 29288d3b-9432-3114-b17c-9d94b5079b9d | -13.8867 | -54.6312 | 2025-06-12 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| d11efbaf-fdc6-37ba-bdcf-15f84861a0d3 | -13.8864 | -54.6519 | 2025-06-12 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b5e1e42c-0222-3941-a8a1-2fe839ded548 | -13.2989 | -57.0734 | 2025-06-12 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| bd045eee-33d5-3f47-8340-80f327487e07 | -12.0063 | -57.2061 | 2025-06-12 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7de94468-3606-36c5-b237-26f924a23ab6 | -12.6979 | -58.0257 | 2025-06-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 390c8dcc-26ab-3a1d-998c-905fc80be5df | -10.8832 | -54.742 | 2025-06-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 477a9630-80dc-31a8-9337-7ddaae8f242d | -13.9056 | -54.6498 | 2025-06-12 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 32c451ef-4a99-3ba4-99af-4bea3f1c9e95 | -11.9278 | -57.4717 | 2025-06-12 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| ec37797b-fa34-3162-9ee2-d19053291d57 | -13.2798 | -57.0751 | 2025-06-12 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1bdab2f7-9fb1-3b3a-9320-abd4518d1c97 | -10.6501 | -49.3617 | 2025-06-12 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2929091d-ecdc-3e44-a09c-eb539a4e0c93 | -11.9874 | -57.2076 | 2025-06-12 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0842a42b-5e4c-37c0-81cd-7c77b579986f | -7.476 | -45.5325 | 2025-06-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c83232f1-5473-3820-86fb-453aab848daf | -10.7048 | -49.507 | 2025-06-12 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ce6603d6-e68d-3f71-b1c3-f8c51577a132 | -7.4575 | -45.5116 | 2025-06-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ac0ebe14-6e42-3e8a-99ab-9b4aaea0e36d | -12.7169 | -58.0242 | 2025-06-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 137f0a26-10f8-32bd-ae9f-78c54785f772 | -13.9059 | -54.6291 | 2025-06-12 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 18508700-0496-3e17-ad5f-cb77d9e3685d | -13.9056 | -54.6498 | 2025-06-12 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ab45d61f-cc33-30b2-ba6b-a91ffa8614cb | -10.883 | -54.7624 | 2025-06-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3966ce81-ccd7-3614-8dc6-837c9fea3a89 | -13.2989 | -57.0734 | 2025-06-12 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 2dc8dce4-31ff-3289-8163-e46e8a843d0b | -13.2986 | -57.0935 | 2025-06-12 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| b182fa53-2822-3591-be83-5d6008f3384d | -12.0063 | -57.2061 | 2025-06-12 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 47217e48-b3c9-36a9-9abf-d80496aded6d | -13.2798 | -57.0751 | 2025-06-12 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| dfe03b3c-66ee-3e3b-a2f9-9b7e8ba94e26 | -7.4763 | -45.5099 | 2025-06-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0d2cb73c-bcef-3f60-8f15-1b4cafc9bc03 | -10.8832 | -54.742 | 2025-06-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| b048257b-b176-3aa1-9da0-d14816b674c5 | -7.4572 | -45.5342 | 2025-06-12 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 48a0afab-7460-313b-8af2-83b611d0a6f9 | -13.8864 | -54.6519 | 2025-06-12 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d8ab5463-a0a5-38a4-85a3-0168668cc8f8 | -10.8832 | -54.742 | 2025-06-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 660c5622-4bd1-3c8f-9d97-ccc5c0e25901 | -13.9059 | -54.6291 | 2025-06-12 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 1ea168bd-52a4-3024-8434-b9670d485568 | -13.9056 | -54.6498 | 2025-06-12 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cae378bc-7b66-33e5-96b0-dbae975bdb44 | -13.2796 | -57.0952 | 2025-06-12 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f67ca81e-afe2-302d-941e-68fc0f89645c | -12.7169 | -58.0242 | 2025-06-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 0348bfb8-b6db-3710-8751-a89455d27e34 | -13.8864 | -54.6519 | 2025-06-12 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 870a5898-3223-3ea4-9e0f-7b6491c9b5c5 | -10.7048 | -49.507 | 2025-06-12 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 8fb4eebe-2dce-35d5-b56f-0fe8c9233930 | -10.883 | -54.7624 | 2025-06-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 265b654d-5137-36df-b8b1-3bafcd084bb2 | -13.2986 | -57.0935 | 2025-06-12 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fa5a5eac-13e9-37db-88f3-b8df232894a8 | -13.2989 | -57.0734 | 2025-06-12 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 49aa7960-5e6d-35d0-a44b-305172506409 | -13.2798 | -57.0751 | 2025-06-12 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |


[Clique aqui para ver as próximas entradas](README5.md)
