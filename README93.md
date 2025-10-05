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
| 1a623208-3eac-3773-94a4-e96e84f6c970 | -13.54987 | -47.23404 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 13cdc102-4058-395f-8be7-18b114f32f7a | -12.4504 | -44.73737 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a5de81b-ed6a-32b7-b523-6f5bc1e337ca | -10.94566 | -47.08425 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39002e28-9e45-3c50-93cc-bb057097e83e | -9.91774 | -50.19544 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f55e7f-afc2-3948-8b56-7a71c4cd02e1 | -12.39938 | -44.83108 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5670230-4e81-3d25-bfa1-45657027bae3 | -8.16322 | -43.34734 | 2025-10-05 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73de514c-2e3a-3d5c-a748-804746d499c9 | -10.46701 | -57.48395 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 659b664f-270f-3608-8cba-3f78d42a5246 | -7.46224 | -43.05127 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c34e06a9-b3f7-33aa-a127-be31825e9db3 | -13.10235 | -47.85286 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cfce507-3967-3db4-b218-2f2477b547fc | -9.60278 | -57.75033 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17637d27-69af-3789-97f5-12b6e2f43c3f | -7.41768 | -46.48456 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74372d0e-d8f3-30bd-a27a-d4c8f3c543f6 | -12.31501 | -55.12569 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97d0692e-3fcd-3411-9cf5-dabd062eeef3 | -11.69038 | -45.28025 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baf14105-092f-3b39-b7eb-47e69bffc89c | -12.57427 | -48.16341 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bbf84fd-8bbd-3422-98f3-f573496d7bc9 | -13.1343 | -47.93958 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a746882-4339-3029-8257-1aa3530c5e41 | -8.57625 | -46.33326 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7bb37de6-ac89-35cb-a012-8c3ee8707306 | -7.2467 | -42.98187 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| efe0330b-8127-3be2-b4c5-d1212ed41a31 | -7.03051 | -42.76688 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09a899de-6d26-321c-83aa-90c50a23b39f | -13.30598 | -47.79985 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 263d6878-03fe-3afc-b88a-3305f830785b | -6.95891 | -50.33082 | 2025-10-05 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36081ea-af06-3a29-9e8d-6afafa74d55a | -13.5237 | -47.24164 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a68d5cc0-2b9c-3d19-b5e9-c360adbe8117 | -11.80483 | -46.81737 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ee84985-50f5-3bf1-aa80-46123ca2d60a | -12.98496 | -51.04678 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30bc449f-d352-333a-bd5e-b0bfd16e7aa0 | -10.40056 | -45.39441 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1e741df-2e61-3e69-be30-5f1fcfd1179c | -12.40158 | -51.11401 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a306dc54-fa70-399e-8d6f-0ae3c8c4d0ee | -13.08859 | -47.92184 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c4b115b-b276-382d-8297-909c4fe804c2 | -8.63754 | -51.09045 | 2025-10-05 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45726ebf-ebe3-3700-b4c7-34b7e5442437 | -11.09929 | -49.86808 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2be998a-9499-37cd-9cd0-b8c3fe8c0087 | -13.65 | -47.29131 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39657fce-2b44-3c7c-96df-6e9e3cd221f8 | -7.79093 | -44.55019 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43bc5d0f-afc4-387c-9089-c2ad365db753 | -11.82905 | -45.08092 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b1c2846e-a4fb-3ef6-95ff-52388091eeac | -7.24916 | -46.94537 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9eabfe30-6a97-38ca-8790-386602c483fd | -13.34313 | -47.59141 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1876019d-0b1d-3df2-be2f-75fbb3325e98 | -10.21658 | -54.12569 | 2025-10-05 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b413d498-60ce-3f93-a108-d986f327b733 | -11.91438 | -46.24247 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6622bbaf-c05f-37f5-9401-e5dd02636e4e | -7.81624 | -44.53521 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 520b433f-892b-3146-9b75-d635ad172e01 | -8.59101 | -46.31701 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5125c8a8-12cf-38a5-be20-8b31f84a018a | -7.64574 | -45.41952 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 540392be-59c4-3486-b317-a113e1997836 | -8.90569 | -46.59029 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65740dfa-d223-3db7-bee7-949add8239e9 | -9.98033 | -48.27892 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ea12661-aa2b-31c5-ac66-a52d27a0e71a | -11.68711 | -47.48783 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e914cdc-9763-3cf5-9f93-4b91fe7768a8 | -9.14374 | -60.29877 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc51ab8-2fa8-33b0-80f9-95c31d3af2a3 | -11.54289 | -47.66086 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69f09a9c-f4e9-3232-8de3-4bdb2ee29019 | -7.35035 | -45.21839 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01c608b9-57ea-3a3c-b945-ca0e33801cec | -13.28127 | -47.59536 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 788eeb79-02b9-32f6-b120-4e622ed1ebca | -12.39878 | -51.10985 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d547ad2a-8d6a-3db2-aa41-837ae0bd6e5b | -10.01546 | -48.26465 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aef2b19-323c-3323-b5e6-d0b748096813 | -12.97987 | -51.03467 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2d50a4c-f9cd-3c6a-9a71-c4e5093aa517 | -9.51624 | -54.73668 | 2025-10-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edfba53e-1de9-36fc-b972-c8498aaf8b98 | -11.45039 | -49.72008 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 646c57d1-a173-31ad-8aa2-2bb913450516 | -13.40659 | -44.38551 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc89bae4-01ea-3efa-bf78-e54edfb969c1 | -13.27044 | -47.18419 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82e9c523-f440-37e8-b5c1-b925a9c9c091 | -11.46198 | -51.51991 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 487f6e13-326e-30c6-851f-00cd4eacc2ec | -11.86981 | -56.87779 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 27d1b120-1d67-3200-94ac-01cfa5f515af | -6.98566 | -44.37411 | 2025-10-05 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5700e41b-54f5-366a-8c83-9d2975cbe6f9 | -11.51039 | -54.47047 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0d84a1b-bac8-3ce1-8b84-0e751117368d | -9.81426 | -47.88002 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22087f89-a0d5-3ce7-abff-fa9004f6369b | -10.99134 | -46.66421 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2e7d117-0cc3-3d43-8702-dd6ef097abb5 | -7.7821 | -42.60363 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb033d98-03ea-3fc8-b222-ef0162e111fe | -11.82716 | -45.09512 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d246d696-b551-3f26-9872-967fbaf8ff97 | -11.86017 | -45.04909 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed6b748d-a484-3681-99b0-600ce5ea7b62 | -10.94908 | -47.05919 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 050a19a6-a0b3-3efd-9466-5320f65e9b59 | -12.55894 | -48.16116 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea8b9517-33cb-3756-a355-308ba311ebaa | -10.15238 | -45.43383 | 2025-10-05 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14ac9b00-af54-3fbe-88e9-f5b35e58a5de | -12.93279 | -46.912 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b5af55-019d-3fee-8b57-af947778492c | -6.601 | -48.05394 | 2025-10-05 04:46:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08f3524c-c672-3b91-85ef-9314abde8153 | -10.58896 | -48.69859 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abc11a33-32e3-3b42-bcae-07f2317a9e71 | -13.28792 | -47.17903 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e01bd87-5d38-3e92-b897-317cfeef5c51 | -10.94022 | -47.09407 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c950c088-f4a3-3498-9e1f-379113d1c6d5 | -6.6154 | -44.3125 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a80bd9ba-b7f2-34c7-8145-6b4ae1fd0040 | -12.59184 | -54.7603 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f9b11d1-6f4f-3e81-9076-d789e5900fa0 | -13.33911 | -47.59095 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7330d7f4-0164-38ee-ba43-049c79df0c50 | -11.49102 | -44.98281 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 993d910b-bfd5-3bf1-8b50-39e38608146e | -6.95505 | -50.33382 | 2025-10-05 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71fbd0a4-3111-3e61-8e74-feafe0e46eea | -11.12569 | -47.91027 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1998a67-428a-38c4-b441-c9be8a098570 | -10.81318 | -47.9571 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 079b1774-04fc-30c3-962d-77ada9767c86 | -11.07626 | -47.87396 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4094cdfe-5b3c-3a05-93d1-58a2d8204fb6 | -10.45577 | -48.37471 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35d3be86-f086-3725-9fad-3fc2b7c4ed36 | -8.54977 | -46.31448 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2c0b310-6e6b-39c3-8bd5-3168ba12da91 | -12.31218 | -55.12109 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1db8a59d-0d89-3f1a-a085-6f7594807763 | -10.61393 | -49.13199 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6945d463-7f26-3b2a-9bfe-ca4e84a0e445 | -8.17279 | -55.07521 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b6fd203-20ca-3106-8e0d-8f2c3f271879 | -13.2511 | -47.8179 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6ee9c0e-8e35-366d-987f-af633320a00b | -8.75478 | -47.19941 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 246a69fa-0b03-30ba-a1a1-4e0238097dcd | -13.29578 | -47.57877 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76996338-81fe-3812-9b90-825e0c8441df | -9.19831 | -58.96188 | 2025-10-05 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d87479ae-5fca-3979-91d9-263241a0bbb6 | -9.30091 | -45.99919 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1a77ade6-ae6c-3750-a1f1-e1fb3d5a023e | -10.45146 | -48.37856 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8ff1fa8-3529-3dec-b752-bfe9f80f529d | -8.5854 | -46.3273 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| abebbf6f-3e2b-3825-9a61-3a3c80475e7b | -8.62958 | -54.99004 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 219bcf7a-fae2-309c-860a-1ac494cc3c66 | -7.46931 | -43.03714 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fceee75c-5e32-3ad1-aa14-5da0ca581f17 | -13.08694 | -47.96162 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42c5e7de-335b-3d43-bdda-946176f11f46 | -11.40375 | -47.16436 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b63263fa-387d-3854-96e5-26ae7ab55b82 | -11.94459 | -43.92133 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efa59d76-6a6a-3877-a721-c889414e372c | -7.7731 | -42.62117 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc223284-5f11-398e-a848-8a286b1906fb | -13.3056 | -48.09333 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d70e2c60-7195-3b8b-892f-673c14980212 | -10.50032 | -51.84337 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5de2c38-c45a-3b83-85c0-3d459fd60d64 | -9.25629 | -51.81473 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad3e3b6-d714-357c-abff-3d82583c7ac6 | -11.23993 | -47.78696 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e18d73e0-7836-3aac-84b5-cc8ea08a9725 | -8.57256 | -47.65774 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README94.md)
