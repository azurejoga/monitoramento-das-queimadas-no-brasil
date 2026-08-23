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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ba980d2-5f60-3d4f-bd4d-0611435b4394 | -7.43268 | -59.79025 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d34a684e-39e5-37cb-bac0-8b1eae547261 | -17.16042 | -46.40958 | 2026-08-23 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbd432b5-32ab-38da-91a0-97a1993bfd2a | -9.06634 | -60.43851 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7d78d7a-7208-3ef9-85f2-c17b60a44247 | -13.09119 | -43.34937 | 2026-08-23 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9586d1a3-0a7c-3201-bfb7-e0d355b883f2 | -13.1627 | -51.42217 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 43296dc5-c945-3b66-a576-a742f59dbb81 | -9.63903 | -48.31739 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9e9b501-5935-3fa7-af65-342858d945d0 | -8.62062 | -54.68985 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeb63c86-b8ae-3778-80ab-36e1c207b895 | -9.06732 | -60.43344 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 579e519a-ba67-35aa-9218-99ca59ad17f6 | -12.75408 | -48.40858 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00b898d2-bbdc-352e-b65f-257fcb86209e | -9.16122 | -59.45558 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9093d63-82a1-349d-be3d-ae691e965e4a | -14.57542 | -53.02713 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a4b090d-6a68-34b0-b66d-a1d670e2b7bb | -12.81406 | -48.4103 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6223366-7cad-379d-a3b3-5c116c082038 | -13.18389 | -51.42194 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9378b75-aceb-3735-9002-d13cba301dbb | -17.07077 | -46.41857 | 2026-08-23 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3021d20-3ddb-3492-8e33-dfb196189143 | -16.40037 | -51.8488 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee3aa47a-6eaa-3baf-9243-6630aaeaff20 | -12.64948 | -47.63963 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4422bbba-059f-345a-a1b7-a046cb783c34 | -17.16042 | -46.41249 | 2026-08-23 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51ef509c-3225-3046-b7cf-3e58022c3de6 | -9.80311 | -46.61409 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4c3995b-7b54-34a1-b44a-ae6784913ed2 | -8.91704 | -60.72554 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57f7b7ce-3319-300e-b718-fc03179cbd65 | -8.52329 | -55.34811 | 2026-08-23 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 226b1fa7-83a9-320d-a6aa-f96bc758897e | -14.39256 | -51.78535 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e611aded-d522-30df-99ec-115f1c9d78ea | -10.68716 | -45.05195 | 2026-08-23 04:46:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5af5a4a-33b0-3e5f-874b-fe1d19e6d1b4 | -14.53948 | -52.99852 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 429f9128-3b35-3543-a15f-2bf0580c7693 | -14.14167 | -48.05181 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12c1b050-ac29-30bc-85c4-7155a5b6cf48 | -10.51251 | -50.44767 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a1d56f5-b735-3c91-be71-d7663b7155d7 | -10.46407 | -49.97403 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8204706-916e-3f8e-a4c2-4186c8cd1c7f | -14.3384 | -51.7766 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b86f90db-ea0e-3fac-9b06-380eed7ce704 | -9.85642 | -60.10579 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 691cdbe7-c979-3b97-941e-9c5816a8e246 | -9.04364 | -60.44295 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb632323-8156-39e7-92c6-6e457ffd842f | -15.64427 | -55.95404 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b32521d-244b-346a-a01f-b2e8a79c8b86 | -9.86014 | -60.11836 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817a7c51-a407-31f7-ae9b-dcbe4f6a7f5d | -9.03927 | -60.44333 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a7ac1bd-6b69-3ff7-b0c3-1ab361803c74 | -12.23724 | -43.12646 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13a73c7d-ed27-3dbc-b7d4-184777c83390 | -14.56394 | -53.00739 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f30fb0-e1a8-3652-aada-22ecb3fc93e4 | -7.78465 | -61.42907 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d138de6-a95e-305d-b3be-1e0e810d7fed | -8.94664 | -60.57284 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7be0ac1-a18c-33cc-8311-e1a89e1016c3 | -11.9398 | -45.51614 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c892fe48-917c-31ee-9054-a391fe5a9b2a | -14.36244 | -51.78083 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54c28b36-fa99-3511-bd36-ba24b417aead | -9.44696 | -56.90844 | 2026-08-23 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d82d89f2-eb27-3b86-a75e-8dee81562b09 | -14.38633 | -51.78031 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f53d55b-c2ae-3bda-aa4b-d63af01c954a | -14.38912 | -51.78474 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3c8db0b-5b89-3249-a574-99509903ad89 | -10.801 | -50.96882 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fc042b5-12af-34d9-8265-50f069570a56 | -10.26768 | -50.38112 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48307221-1940-3b65-ba76-8214554c32a4 | -13.45943 | -57.0569 | 2026-08-23 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 057edb06-af74-3b26-b4a0-8355d353e804 | -11.16128 | -54.01782 | 2026-08-23 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1de5b59f-e8b5-3b2e-9926-ee219c0c00f3 | -14.33904 | -51.77278 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e617dd29-1da1-3652-890d-46f826b1394a | -14.36322 | -51.84015 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acbab7af-989d-3c1d-bf01-b00109a79bb9 | -11.29029 | -49.02508 | 2026-08-23 04:46:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c85ef7f-663b-351f-a85f-02ad5c92c6c0 | -14.38024 | -51.78003 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac615d29-6aa9-35bc-909f-c566a8e8ef95 | -8.92344 | -60.72691 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f612248-ea95-3291-a240-342c5d9a7154 | -12.75859 | -48.37957 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25af9391-4fdb-3218-8579-837e7843d0e2 | -9.8607 | -60.11612 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92cb535-b6a8-3065-a9a1-09b02f12efd7 | -14.54501 | -52.79602 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a233647f-8785-3ada-a615-4edea1849cc0 | -12.75798 | -48.40557 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64b9b60-9396-33cc-a19f-86124d5ecc31 | -12.22143 | -43.16916 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 82c9b7d5-5a10-3b5e-be43-a3a21ad6c513 | -15.22548 | -48.23793 | 2026-08-23 04:46:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaec7fbd-ac6b-3893-92f2-0d0368076371 | -10.69046 | -47.71928 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea4008d1-60aa-3056-9e63-bc0f7696f604 | -14.96609 | -52.66558 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8619f72b-0f5f-37ef-a113-9b081f70191e | -14.3459 | -51.77398 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f191d882-78a1-376c-bc56-2e4045484f06 | -15.76301 | -49.96882 | 2026-08-23 04:46:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb6ee0a3-92d5-3008-b69d-09d99636e7f7 | -14.96042 | -52.65611 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf854616-e63c-3b33-a7f4-4f0b091e5813 | -8.52694 | -54.81526 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 149b4685-e4f2-382a-aada-4ef675e4522b | -15.22158 | -52.79592 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a516407-350e-3398-be1b-331450426fc8 | -11.61317 | -50.5572 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8725c1a4-cfae-371b-ac35-490d8d65aec9 | -14.34183 | -51.77721 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4479d74e-58dc-305d-8170-bf598b35aab0 | -12.21655 | -43.17247 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9a19490-5fca-3d04-90cc-2ce9ad14f089 | -12.75467 | -48.38267 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 145da88f-5ed4-3a37-9665-ad43aa6db4c0 | -9.01878 | -50.73502 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b14e53d6-8cdd-326c-99c2-5dc88eda5935 | -13.19011 | -51.42691 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f892cb2b-9aa6-3ac2-91ea-2ed736a5c725 | -9.18733 | -59.44717 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba0a3b1f-604c-3d7d-b78b-44c90b9aaad6 | -8.53207 | -54.81179 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d8b34c-4601-39e4-8276-b9597f8c6ee0 | -10.05044 | -46.42957 | 2026-08-23 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a49a9131-0a20-3ac7-9065-4130caa3a64d | -7.57131 | -61.20619 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21e3600c-999b-3ccc-a229-373bdbc5258e | -12.82134 | -48.47427 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd63c421-46b7-3b5f-bc27-af5ea18876aa | -12.23654 | -43.12427 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7b96c5f1-1b6f-3137-9b85-be49362758c9 | -9.04171 | -60.45317 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c3d3b3c-4335-3376-833e-c686a5f41a41 | -9.4314 | -51.61189 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e7cb512-1a26-34a6-be0a-e3e25ead6178 | -12.81349 | -48.41396 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf3219b-75e9-3ead-a6f3-a3ef458477d5 | -15.04382 | -48.69826 | 2026-08-23 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e73c4480-07dc-34d6-ba0c-f8255ed738a0 | -10.84285 | -50.98758 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dcd99650-cd08-3657-8745-c23b73c92f35 | -11.98654 | -45.50927 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5669671a-5925-3155-a90c-926f32bd4d16 | -12.24144 | -43.12096 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 10cfdec6-f478-3841-ad9a-342dcbeaba78 | -13.19416 | -51.42372 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d30f9ce8-58aa-34ce-949f-266b14896b6f | -12.24594 | -43.12778 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fa9a6c96-145f-3ef6-8a46-55ac2149cabc | -12.7362 | -48.39088 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5828aa54-030b-3a5d-ba04-f3c9743c180c | -9.03828 | -60.4484 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ac1d078-a9a1-39e1-b6f9-2f926286cecb | -12.83753 | -48.48059 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9eb75b2-8dd4-3f1a-9877-f6acf948627a | -14.36931 | -51.78204 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68b4a415-af15-3a6d-b04e-66af1c1d0536 | -12.2182 | -43.16053 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b226d88-f465-39f9-9396-0113b23e402f | -10.80444 | -50.96939 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 007fbede-76c1-364d-bd8d-5952ce386ee6 | -8.99364 | -50.75828 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe8c7eaa-80ef-35e0-ac58-807269b32183 | -9.17387 | -59.45354 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0016a928-22f7-3921-9c07-5e95e6db9ae7 | -16.71772 | -49.13034 | 2026-08-23 04:46:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7659f3ed-d9fc-3f36-8194-df1366624336 | -9.4278 | -51.61139 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fcc0d88-5b7e-32cf-9671-36ea015172b0 | -9.17222 | -59.46221 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e04fdba-3341-3d87-8f73-8f0dfbdba95e | -14.14964 | -48.06837 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9baa8c7-c094-3c1f-bb5f-c17299dda207 | -12.26582 | -43.17783 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d58aa02f-d4e4-313d-950c-32f6291a2c2c | -9.85889 | -60.1253 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 792be5a9-1705-32e2-b68c-8fd37c52b5b1 | -12.64891 | -47.64337 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be572d0-1d54-3ad6-94ac-c5af8adcd2b1 | -16.05032 | -50.43643 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README37.md)
