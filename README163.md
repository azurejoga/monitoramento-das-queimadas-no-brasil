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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbf498ca-4f15-32c4-aaa4-aacda8cef46c | -7.5332 | -43.8319 | 2025-10-05 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 89f90543-9969-30b5-9e4f-c74950d7abcd | -7.7743 | -42.6103 | 2025-10-05 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 197.8 |
| 865333c8-adc8-3324-a580-e2eb45c949ae | -5.9269 | -42.8783 | 2025-10-05 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| f66b04e8-e472-3139-857a-2e6ad38c0582 | -11.6841 | -45.3333 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 1102f78d-1400-3a29-9ecd-71ca7a457ade | -5.9229 | -43.3003 | 2025-10-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| cf42a11a-b99f-36dd-b211-cf5b5e3c0558 | -9.6287 | -46.6394 | 2025-10-05 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ea906b4a-e892-36da-9303-fef5a624fa59 | -7.7746 | -42.5865 | 2025-10-05 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 9f2d09d5-19b5-3336-afd5-79c8d1284093 | -7.7123 | -46.2307 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9b6afe0b-4e2d-357d-88e7-e1d34f683a0e | -10.456 | -48.3607 | 2025-10-05 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 074c540e-e173-3e28-aaec-1b128ade8b0f | -7.4464 | -46.5223 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4b3bda69-3798-381d-a205-038591484e87 | -7.4669 | -43.0674 | 2025-10-05 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 69659d0c-4b26-30b7-9148-dc1f01ff8cc5 | -10.6568 | -46.3372 | 2025-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| c3f0e803-c8d2-343a-ac2c-afeccc4f87c8 | -16.0212 | -50.9425 | 2025-10-05 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0a0c2f2c-b473-3911-ac9d-0b9f6fce3640 | -6.7052 | -43.8859 | 2025-10-05 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 5ec8d078-06db-3af8-bd77-e5eb405dea7c | -9.2976 | -45.98 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 83d6242e-8012-3693-8939-8ce065210db7 | -5.9772 | -43.5057 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| aae8b9e5-f4d2-3e23-ae7e-38c1f8b8c83b | -11.1168 | -49.8492 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 9b1eb5c9-814a-39d4-89bd-8b770a797218 | -6.7167 | -42.8101 | 2025-10-05 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 9001a160-0f92-3eae-a430-0285f62d7efc | -7.0367 | -42.8036 | 2025-10-05 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| f45797cc-b9a4-3108-92c8-cb92935c5727 | -12.5297 | -54.7326 | 2025-10-05 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ba37af56-ddd1-3777-801e-3de3917ef9ed | -15.9084 | -48.8254 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5e812424-305e-3bba-9061-cc0954527a1a | -6.7164 | -42.8337 | 2025-10-05 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 63371251-5d8b-3384-90c2-95cf2a31b989 | -9.9212 | -50.1895 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b1fb57f5-ce54-3a71-9e01-f0d306caf62c | -6.2156 | -44.0658 | 2025-10-05 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| f354c1e7-aca3-307d-85d6-525e4f81ffc9 | -11.0978 | -49.8513 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 385fea0e-b226-36d4-ba08-63d4519b08c9 | -6.0616 | -42.537 | 2025-10-05 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 1a71da4e-0848-38ad-b684-b7c660c701cf | -6.7866 | -41.5882 | 2025-10-05 14:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| c46586e7-79ff-383c-a813-6375f313bca0 | -10.5651 | -48.6762 | 2025-10-05 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 01d98337-b7da-3da4-93d4-6fafdf4fc318 | -16.077 | -51.0859 | 2025-10-05 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 713bd32b-9688-3746-b218-fc203da53e06 | -8.5405 | -47.7051 | 2025-10-05 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 41228541-0dd0-39a7-b6a3-31dcd8090959 | -6.1966 | -44.0904 | 2025-10-05 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 3ca9f380-8278-3032-ba08-9cf00f5994ca | -5.9879 | -44.3598 | 2025-10-05 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7d8a9dfa-e406-3f43-a591-d127ae077b21 | -8.5407 | -47.6831 | 2025-10-05 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a2ffc728-f746-311a-a43a-31c925154169 | -11.8418 | -45.0799 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 9c2a76fe-4ee5-3c29-aed2-2837b79785d1 | -10.6565 | -46.3598 | 2025-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| c5a8d334-bfe0-3cd4-9dbe-9b9de8df8dc5 | -13.304 | -48.0798 | 2025-10-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4b8d9cc6-3d28-3f2a-9960-6a2985aaa698 | -10.1497 | -45.9709 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| add500bb-1f12-3d6e-b29c-66d6a008dad7 | -12.3911 | -51.1153 | 2025-10-05 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 9f11ef31-8a13-3140-b473-d6d1444ae62e | -10.1386 | -45.4497 | 2025-10-05 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| db176d55-8dae-3822-904a-ca11ff5ea485 | -8.5393 | -46.2631 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 91068527-6cfd-30fe-8d54-e5bb7a901ba8 | -7.712 | -46.2531 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 212328f7-10b0-370e-bdd1-9757154fa19b | -7.7885 | -44.5228 | 2025-10-05 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 407dd9a8-af20-32d2-88b5-074b214526f1 | -10.1576 | -45.4473 | 2025-10-05 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d45a1f6d-339e-3022-872b-2d0c9f83bff4 | -9.2641 | -45.6671 | 2025-10-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1b2e5446-9af3-3906-805e-0cf906a253de | -6.1353 | -44.6232 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 6f3764a2-2fdb-34a4-bef2-c32bc9f61430 | -7.8047 | -48.0558 | 2025-10-05 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8a818215-a058-39f4-b351-2399fb4d3fba | -7.7308 | -46.2513 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9ebab0a0-d82d-3122-823b-8219061f8087 | -12.5487 | -54.7307 | 2025-10-05 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 09313fe0-5d22-3b0a-bd61-221b142a3a6b | -18.1968 | -53.3638 | 2025-10-05 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 97b13fd8-8ae0-3b39-8bf8-a234d6c1954c | -11.5301 | -47.6798 | 2025-10-05 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b86c70c4-6647-3d09-bd93-886c355b62e3 | -8.133 | -44.0953 | 2025-10-05 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e3f5ba30-3a32-32d0-95ca-e7317fae81b5 | -6.6976 | -42.8354 | 2025-10-05 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 343e3b2d-8d0b-331a-9f3f-fdaf3370b655 | -6.3982 | -42.6972 | 2025-10-05 14:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 6ccc2e04-6da5-3d2f-b261-eed9c40da0a9 | -12.3157 | -55.1212 | 2025-10-05 14:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 853f7e5b-f87d-320d-852d-3cd6e72ba4d0 | -15.9829 | -50.905 | 2025-10-05 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 8673810b-268d-39a3-88d5-70dd324c417f | -18.1972 | -53.3423 | 2025-10-05 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8414bc7b-1f50-37d4-96c4-640213f87fca | -9.9024 | -50.1914 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 21ac15f1-4fa7-3b0c-8376-8b52b648e67b | -9.5791 | -46.1286 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 1ef8f6c3-2841-379a-b56c-2e9b7a9c679a | -11.1165 | -49.8707 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a372fc98-532f-34d2-b65a-f753cf3ccf27 | -7.646 | -45.4489 | 2025-10-05 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 54da959e-2f28-382c-9371-092d547c5a5e | -15.9825 | -50.9268 | 2025-10-05 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| e759614d-61fd-3281-82f0-9ba4ed65c6f2 | -17.9661 | -51.1474 | 2025-10-05 14:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 8e6329d6-7974-33e2-9caa-cf5fc1127866 | -11.4298 | -43.4833 | 2025-10-05 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 7ebf48d7-ef53-3ac8-ba19-32f94de0122f | -6.3889 | -43.6115 | 2025-10-05 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 2ba6ea40-acb2-3ef4-9993-396e23302344 | -11.0975 | -49.8729 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8a403941-31f8-3b8f-8370-424eecd0edc0 | -7.7749 | -42.5628 | 2025-10-05 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| ac80e27d-ede9-3a3d-8d2f-1040fea64b94 | -11.0316 | -46.6946 | 2025-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 59c19926-36a9-398f-b153-f3500314cf1b | -7.2723 | -45.2792 | 2025-10-05 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 8deb7a67-d5f1-30b9-af04-cdcee5590f60 | -7.6458 | -45.4716 | 2025-10-05 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 21af68ff-f20b-3b69-ba3f-66b323e2666d | -13.0968 | -47.8429 | 2025-10-05 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6c82e2c9-614c-37da-a776-e45df946a2fc | -6.1534 | -44.6903 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7c2525f6-7975-3d11-9794-ca7bae51af83 | -6.2153 | -44.0889 | 2025-10-05 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 0c19ab61-d3d4-3233-8148-a2c8f5dd7b33 | -16.0805 | -50.9116 | 2025-10-05 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f7d1fd24-aea1-3972-b0bd-258759b0d7c5 | -8.5956 | -46.2798 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ce939e24-4521-3c30-af1f-e5761fa9c2a7 | -10.158 | -45.4244 | 2025-10-05 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 7f9f26bf-02c7-39ec-b53d-dab6224889bd | -11.8038 | -45.0624 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 6773208c-2c25-35c0-bc25-47c5d88a63f2 | -10.0315 | -50.4131 | 2025-10-05 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 47550029-6b31-3e6b-9c82-6b60f60bee78 | -17.9602 | -57.611 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 498ff3cd-7c97-3108-b0c0-6fee81bd62d7 | -7.7933 | -44.1304 | 2025-10-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b52dfa3a-2ac6-3dea-82de-27700d4405f2 | -11.0911 | -47.7573 | 2025-10-05 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1a177a4d-253f-3427-990f-e1973ee71fe5 | -7.4276 | -46.5239 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3d9d7a79-caf3-3faf-a0be-48f4b2cd68fb | -5.8925 | -42.551 | 2025-10-05 14:10:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 6422b27f-c3eb-316d-8428-3be00d0e1f8e | -8.1327 | -44.1185 | 2025-10-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| c53db003-0e19-383c-866c-9aa33ef670f6 | -9.931 | -50.911 | 2025-10-05 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 4c9758eb-dd3b-3dd0-b7d6-8724a92e1e25 | -16.0021 | -50.9238 | 2025-10-05 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 9cf9ccc6-e2f9-385b-a73f-9ce8f9998edd | -7.8121 | -47.3759 | 2025-10-05 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c8cb0987-35d1-3ad3-aa16-82c25588db41 | -6.3341 | -41.6309 | 2025-10-05 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| d28c0628-f6f8-3ce8-9bd1-3f1e8f8d05e4 | -17.9605 | -57.5904 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 40d90267-5794-35e5-9d8b-1901db257737 | -13.69 | -48.0447 | 2025-10-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c784f9b7-15d7-3266-992e-89656aec23bf | -21.6888 | -50.0559 | 2025-10-05 14:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.4 |
| 4c0796da-7220-3aee-a8c5-79ff494c15a0 | -12.5485 | -54.7512 | 2025-10-05 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| ccb0c3cf-4261-3430-ba02-fcf646c759ac | -7.6993 | -42.5708 | 2025-10-05 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 0f03c89f-3b5c-3820-89cb-daf229ca75bd | -7.7932 | -42.6082 | 2025-10-05 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 151.6 |
| f0b81e47-ce32-368c-b422-701ee92c91bf | -6.0428 | -42.5386 | 2025-10-05 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 8d9dc70e-6420-3543-b3e5-8b0c4871607b | -7.7935 | -42.5845 | 2025-10-05 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 153.5 |
| 5dda0915-2710-3612-a2da-ea9b3666a9fc | -18.2569 | -53.3329 | 2025-10-05 14:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 112.9 |
| dc0b83e3-acb0-36ff-9489-fe879467c550 | -17.8417 | -57.6254 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| da3a7d92-91f9-329e-8a10-2c1ec360bb4d | -13.3233 | -48.077 | 2025-10-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 652340e3-8cc5-31af-b5b5-3ba5b3156195 | -8.8618 | -46.0949 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 62df1160-6886-32c5-a0a1-b155f245c5ca | -9.3938 | -45.8562 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |


[Clique aqui para ver as próximas entradas](README164.md)
