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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe68e46-5617-38b2-b014-9abad62580ce | -9.9396 | -50.2304 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 6e4ca6f9-2003-37ef-b93d-4ffc43edc184 | -10.2254 | -50.0093 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 7357a74b-402a-3c9d-9694-5866a9023a2f | -12.9653 | -51.0457 | 2026-09-28 19:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 05b9746a-f5b7-323c-bc99-b31cef792319 | -12.8061 | -54.0048 | 2026-09-28 19:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| b3b4d712-8d50-36c2-997e-e16e984bf446 | -8.9823 | -44.1633 | 2026-09-28 19:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 15182931-0b91-39a4-be27-334d6f1cd857 | -8.4734 | -48.6276 | 2026-09-28 19:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 99fef276-0a60-375f-970b-e96e52717ef8 | -10.824 | -60.7246 | 2026-09-28 19:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 98de73d7-29f8-376c-bba6-184a40dd7f7f | -9.9781 | -50.1626 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c05ec217-4017-34fb-80bf-c9d7816805ec | -11.3247 | -54.1103 | 2026-09-28 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a423430c-40bd-3930-9838-fd6c9b7555df | -12.7868 | -54.0275 | 2026-09-28 19:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 167aaa45-27fb-3b64-a069-c7678c839388 | -10.9154 | -50.7059 | 2026-09-28 19:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 8e91691e-a7a4-38e7-9e87-f3e2fddf3d15 | -10.2257 | -49.9879 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3c70e3c8-c68c-3e35-9e7d-b5a0bf6e1d1c | -6.1249 | -43.7494 | 2026-09-28 19:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9dde8cc3-2484-3ab8-ae6f-15dbc057914c | -10.0148 | -50.2443 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| cb9972c6-41db-3974-a1c2-fcac997bb958 | -14.4154 | -52.7954 | 2026-09-28 19:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d819e3a6-0f81-36d2-a75c-99b1aa27345b | -9.1335 | -49.987 | 2026-09-28 19:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 8092d548-b011-34c9-91df-ddccb63942da | -11.2945 | -43.551 | 2026-09-28 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 9765a465-622a-3141-a291-66a563cefb36 | -11.6096 | -44.1382 | 2026-09-28 19:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| e6ba5d58-ef03-3923-a364-4615f123b031 | -11.7178 | -43.4623 | 2026-09-28 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| d95b7a52-a0c9-3d51-b857-4d7b7140305e | -10.9343 | -50.7039 | 2026-09-28 19:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.0 |
| b02c642c-26b5-31a3-b8ba-7f687b1de655 | -6.6628 | -55.0912 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 01e1def0-f246-3915-acfc-2276decddcbb | -14.7295 | -45.5527 | 2026-09-28 19:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| c9adef53-1b16-3190-b9d0-d1d1eefc1dc7 | -7.6712 | -44.9008 | 2026-09-28 19:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3d1c6319-68c9-34fa-9630-2cbbdcfb2cee | -5.4762 | -45.1262 | 2026-09-28 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a1c5a031-cdf2-353d-9435-3f5333c3e767 | -8.6637 | -45.3697 | 2026-09-28 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a37166a5-9483-359e-9116-b44548355f7f | -14.5171 | -52.4864 | 2026-09-28 19:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| bc485d07-896a-3d62-895c-2d8bf6bc95fc | -8.2482 | -45.4356 | 2026-09-28 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f114a6cb-974d-30e6-a027-9b791b39895a | -11.4973 | -47.3504 | 2026-09-28 19:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 54586831-e4ac-372a-8a2a-46d4e5dba1c5 | -8.2994 | -54.7146 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 61839082-2dea-33e3-a6e0-5015c98c5424 | -13.6866 | -56.6131 | 2026-09-28 19:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a869cf9f-7a02-32d6-a547-746786b0ffbd | -10.8371 | -61.418 | 2026-09-28 19:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 12b2ba96-80eb-386a-b4c3-cf03744426bc | -15.0793 | -48.3389 | 2026-09-28 19:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0067cad9-c694-31d5-98aa-19dae9e8559b | -12.6267 | -47.2851 | 2026-09-28 19:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 14707918-5049-34c6-94f8-7ea8d5021834 | -7.437 | -55.6291 | 2026-09-28 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| a43053e4-5d60-3c24-ba88-3d957f8b097c | -12.7677 | -54.0296 | 2026-09-28 19:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| f24a88eb-c259-3d7b-8397-9589988e24a1 | -12.9456 | -46.652 | 2026-09-28 19:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 11d87211-774b-3831-a452-09e266a2d5e1 | -10.9637 | -43.8821 | 2026-09-28 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6af02251-734e-3c2f-8162-6e51937b24d9 | -12.1202 | -57.1767 | 2026-09-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 83a3dea4-a338-3763-8047-7b72354de43b | -11.1962 | -44.8037 | 2026-09-28 19:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 70fec0a0-a0f3-34b4-b4da-7a3f4acb7e97 | -8.2291 | -45.4602 | 2026-09-28 19:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7d30d69c-b0a9-3a4a-a617-a81cba031883 | -9.9784 | -50.1412 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 89a0f311-bdc0-3e1b-9b0f-919f601a3a88 | -11.4966 | -47.3951 | 2026-09-28 19:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 42564861-50ee-39b5-9bac-bd2d81253750 | -9.9593 | -50.1644 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| bbf667e8-e844-36a7-ab1d-709adadf9feb | -10.7916 | -48.7377 | 2026-09-28 19:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 8b290301-cd15-3c26-8d2b-50bddd744b01 | -11.1966 | -44.7805 | 2026-09-28 19:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| afa5022a-a82c-39e5-a9da-430c243f587f | -7.7038 | -54.7521 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| da6ad313-2e18-3c21-bcde-03a2bbbccc7f | -11.3444 | -54.047 | 2026-09-28 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 890.5 |
| d94b8dea-c8e0-39f9-9504-0e0417f425d5 | -8.2807 | -54.7158 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| dab43287-c59c-36e6-b4bb-475ec14980a7 | -10.7726 | -48.7399 | 2026-09-28 19:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 188a1092-a280-3674-8434-35da74db7d47 | -10.9533 | -50.7018 | 2026-09-28 19:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 101998d4-4da2-35c8-a11c-15c43bbcd707 | -11.1771 | -44.8064 | 2026-09-28 19:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| da3867a1-28b6-3ea4-9ea3-e227e9e0f1e3 | -0.4889 | -49.1327 | 2026-09-28 19:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8a918db7-68e0-3b7c-aac4-2c0b547b25be | -11.4788 | -49.7646 | 2026-09-28 19:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ac8d4612-10d9-3f0c-9f2e-7c5fe3634984 | -10.9445 | -43.8849 | 2026-09-28 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5963eeac-d5fe-3225-a5cd-769283d008ab | -0.5073 | -49.1326 | 2026-09-28 19:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 19efd67d-6fc4-39b5-99e9-63f27d5fd440 | -9.5002 | -46.3625 | 2026-09-28 19:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ead6ea22-0990-3c68-9215-f60d26417155 | -12.0019 | -57.6051 | 2026-09-28 19:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| cfd13f6a-f8da-3470-bf3c-850618f72dd2 | -11.5384 | -47.1664 | 2026-09-28 19:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| be1e8224-9ce2-3aba-9848-a8e120313463 | -13.3943 | -57.0645 | 2026-09-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 512f4fb5-93c8-3419-8ce6-183e926cbc41 | -8.6451 | -45.3489 | 2026-09-28 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 72e33d66-3f3a-3c02-9518-d405c7029bbc | -5.1887 | -46.0888 | 2026-09-28 19:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 39aee848-8e89-30c5-bdc4-aaee259dc981 | -7.4974 | -55.0256 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 6a77a11c-2117-378d-8224-3f057beb8bd3 | -9.1525 | -49.9639 | 2026-09-28 19:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 9eccbba9-1519-3092-8739-d91f86a8e398 | -11.4977 | -47.3281 | 2026-09-28 19:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1379752d-2ea1-37a3-9fd2-7daec9f4fef1 | -10.7056 | -50.8341 | 2026-09-28 19:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 80196d45-1a61-3440-ae90-d232cf5d5dcb | -9.6864 | -58.1258 | 2026-09-28 19:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 0b71f4c7-1dfe-3da7-b10d-55af79476ae0 | -9.1871 | -45.7663 | 2026-09-28 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 35f769d9-6cdd-352f-bcfe-e1f355ce2cc5 | -7.2181 | -45.0797 | 2026-09-28 19:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 130e8613-802b-3ed2-af96-719b2b6a44fc | -15.0616 | -54.5988 | 2026-09-28 19:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5c10687c-6522-3efe-8314-20d2ad435967 | -10.2067 | -49.9898 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 510c54ff-080d-3eb7-97ae-5493339144f1 | -9.4813 | -46.3646 | 2026-09-28 19:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 29c0254a-e20a-32c1-87ab-0df7cad094f8 | -6.1251 | -43.7262 | 2026-09-28 19:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a40d143c-5ca9-3c7a-a008-226aad22ecc3 | -5.7388 | -45.0172 | 2026-09-28 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4b7b0856-bdff-3487-8bf0-044a56e85486 | -9.7051 | -58.1247 | 2026-09-28 19:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| fd63610d-158f-3255-b5e9-3ba0f2a925b8 | -20.0991 | -57.2067 | 2026-09-28 19:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 13f59f20-729f-34b3-9eb9-04fa146b312c | -11.8641 | -47.1004 | 2026-09-28 19:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 20beb37e-266a-314a-936b-eda288bb9d20 | -10.8001 | -57.2007 | 2026-09-28 19:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| b341c151-a00f-36b7-a916-e11ad932a00a | -11.0796 | -46.079 | 2026-09-28 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e6735b2f-7269-3e02-a701-69103316988d | -9.5002 | -46.3625 | 2026-09-28 19:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 43b8acd2-2e0f-39a0-aa51-a73c74b08c6c | -10.0148 | -50.2443 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d7766aa9-dac3-3add-b512-441859710eea | -6.1249 | -43.7494 | 2026-09-28 19:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 062bfc2a-eb7c-3a8d-8bb9-031b9c65a00c | -10.9343 | -50.7039 | 2026-09-28 19:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 6f1df698-bb5f-36b1-8c10-faf19c5be01b | -10.2065 | -50.0113 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 58d9f8e6-d5de-3f01-a47b-4bc90ea0f38b | -12.7868 | -54.0275 | 2026-09-28 19:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| ec71a62f-a020-325c-bb09-3f31323b7f84 | 1.877 | -55.5844 | 2026-09-28 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| dae5ce89-c581-337d-8e57-f39ee838ff5c | -10.2443 | -50.0074 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1bc34c9b-730a-3740-8cec-9877abff33e3 | -10.2254 | -50.0093 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 8ba02433-26b9-3e52-8b67-e6420c944673 | -12.9646 | -51.0886 | 2026-09-28 19:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 083caa82-5f85-396a-bc09-371ef22eb8bf | -11.1324 | -50.0839 | 2026-09-28 19:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4f7f7594-4bda-368b-aeaa-0367652a7203 | -9.0783 | -49.8853 | 2026-09-28 19:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 5f804388-1912-3db6-9be1-c20b92095962 | -14.5171 | -52.4864 | 2026-09-28 19:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 0931d0ed-e4e8-3683-b584-565bfeb343aa | -11.5384 | -47.1664 | 2026-09-28 19:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4664712c-e95b-33ec-a5b3-7a72f9cd6bdb | -10.8191 | -57.1795 | 2026-09-28 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 6538ae74-e12a-38f3-85ff-c72deb910702 | -9.9266 | -60.7171 | 2026-09-28 19:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 208.6 |
| f6ea2823-90f7-34f7-91f0-753084fd57aa | -10.9533 | -50.7018 | 2026-09-28 19:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 179.1 |
| e9f2bdc9-6686-3e57-b15a-3100cbf356d0 | -5.7386 | -45.0399 | 2026-09-28 19:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 073f7d0e-f5c8-3394-a8c6-038f32c45d61 | -10.2067 | -49.9898 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 14f781aa-3140-3d6e-ab53-096084aac1eb | -9.1525 | -49.9639 | 2026-09-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 6199a7b7-df2f-39ec-b4b2-a5a8c0aff4d0 | -10.8001 | -57.2007 | 2026-09-28 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 43753bd1-4581-3b98-a7ad-6355a52fca35 | -10.824 | -60.7246 | 2026-09-28 19:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |


[Clique aqui para ver as próximas entradas](README182.md)
