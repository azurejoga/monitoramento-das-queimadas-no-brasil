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
| b1d6d07e-b153-3cf5-8a07-30f61c214815 | -11.42954 | -45.10593 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d2e9d71-33ee-3bc0-a1e7-654f3e15dda0 | -7.22649 | -43.06844 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a346e410-9b3f-33bf-9ea5-abacde262247 | -8.64948 | -48.49541 | 2025-07-09 04:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b69d625d-a46d-3120-9f11-c1e156004d05 | -6.83731 | -43.35022 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61cf8de3-710b-39da-8df9-49a9412166d8 | -10.58239 | -49.1312 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf89def-9571-3ce9-b6ac-9e184833df77 | -9.2193 | -48.59696 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b87f1b10-f8f7-341a-9a99-03cc3fdd672e | -7.24645 | -43.07533 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7d497be0-746d-331e-93b4-7e1c2205ad58 | -6.67985 | -43.19651 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4cba2ea6-a4e3-36fd-a10e-b4c05e6cf4c1 | -7.64431 | -45.35727 | 2025-07-09 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbeb9916-f216-399e-b2bb-7f806121a0aa | -11.42121 | -45.11551 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92cd0886-0e34-3ea0-bd67-ebd3c0d079ca | -11.43009 | -45.10239 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 158de0f3-a72e-393d-a262-6f8f5dea9855 | -11.41953 | -45.10434 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69113811-af94-3142-b538-732240776bf8 | -5.96289 | -44.17677 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14b6082e-f8e7-3ae4-ad93-efb84d83da39 | -7.08781 | -49.16761 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 380f1880-c074-3434-b786-d4021293e3bc | -8.17883 | -46.51016 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eee806b7-570f-34d8-a268-a7c9c6eb5864 | -8.51687 | -43.29669 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 418f6c38-3de9-308b-baa4-fdd928b05427 | -7.03349 | -43.32427 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71a702fe-5af9-3866-9812-9f8e74b9625f | -9.23092 | -48.59454 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 55e60eff-954b-39a5-ba98-77258057565d | -5.96513 | -44.18423 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb7b59d5-ec04-32e5-a49d-40ba32743d45 | -11.42176 | -45.11197 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| edb7651d-86a4-3c82-821e-737a3f791c4b | -6.73001 | -44.3325 | 2025-07-09 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caf1a6b1-4850-3cfe-a57f-50ca8c03ada1 | -8.51287 | -43.2999 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f6a51336-fa27-3a70-9888-e7a455882655 | -8.21866 | -44.93521 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75b5dd0c-ee7c-332e-a0e0-41d74068e422 | -5.77605 | -43.62113 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df717dd2-4686-3d81-b7b7-1a8cf75b26c9 | -6.85725 | -42.79228 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc249091-9057-3a24-a0a2-45b11d3d5c6d | -4.7164 | -42.78367 | 2025-07-09 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb41fb8-2999-32ae-98be-3b9275d16cc5 | -6.95638 | -43.25687 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 610034c9-bacd-386b-8d8d-6603b46097ec | -7.67144 | -44.3695 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db358f5-29e7-3e77-9e88-634b0d9f5df3 | -11.45196 | -45.10938 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb3e246-f77b-3b1c-8be3-ac0998fec847 | -8.5163 | -43.30042 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a4dde37f-e779-3de0-8de6-ed119e786d64 | -7.08942 | -49.16515 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8ce6b921-6fae-3730-b5cd-f821c91f14cb | -7.08822 | -43.42185 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 19f7fae9-f452-3551-8027-27dd476b344d | -8.30861 | -55.10943 | 2025-07-09 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 239eb2fd-6117-3b16-99e4-6f717ef488ff | -6.95698 | -42.70651 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4822739a-3988-33f1-8121-597fd4bd370c | -11.43398 | -45.09937 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 02d9099c-3bc8-3dba-b691-3453397597db | -11.43621 | -45.107 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d3e51b12-7a16-38d0-abb0-8076986c4b6c | -6.66568 | -43.89986 | 2025-07-09 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b551efd-b52d-3871-b3bd-624fd0c98da8 | -12.05658 | -43.5106 | 2025-07-09 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10f39a50-fa23-387f-9edd-69e6784b5905 | -8.379 | -43.94769 | 2025-07-09 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4360c79f-390e-39b6-891d-a3e699386332 | -10.18004 | -51.15835 | 2025-07-09 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7750634f-32ea-344d-9678-ca90a567210a | -8.17149 | -46.51269 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8dbb374-ac5d-366c-babc-3c24e95ff5ec | -5.23113 | -45.21312 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff040ea5-fa00-33a5-a3fd-f3a60782d5c1 | -11.41843 | -45.11143 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7df53a9-8f78-3cdb-aa41-a4e74ae65fab | -7.22934 | -43.07267 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ce7b2585-5c41-3653-868f-e876aa29f70e | -9.22001 | -48.59266 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f7fed19-4155-3d3e-bd49-0dda4742edb0 | -5.58917 | -45.34163 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fb3d7d4-24fd-349c-9f34-75debef69843 | -11.41286 | -45.10328 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8f3f41-48a7-3266-ac45-3aaa4a234954 | -11.43642 | -45.12146 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eee4a1b5-f14c-34f5-9642-5efe5033894f | -7.80907 | -46.57396 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30bab28b-8271-371f-9f06-9222a6276f1f | -11.43787 | -45.09635 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a0c43021-57f2-361f-9679-ffa36fa4e535 | -5.59048 | -45.03742 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aeca892-ca8e-3e1a-8b75-9b6127696cee | -7.02954 | -43.32739 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c880b53-5b66-38bf-838a-65115edd3669 | -10.63216 | -49.44901 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83119953-341a-3e62-9dee-6e5492b28f15 | -11.41509 | -45.1109 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25f70efb-62f3-3ddd-9a7c-6ced961f8cda | -6.741 | -43.16103 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 288f0b65-9105-375a-8d82-e3f9ffafd92f | -7.0939 | -43.45232 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4b0b816-62ce-3e02-bedf-c2b16ec17ec9 | -5.78495 | -43.60807 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beb58d44-6c09-3792-9252-7c6a5c5ae3c0 | -7.66424 | -44.37194 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87935e41-5a30-3797-bd51-7c4fb2be6470 | -11.42565 | -45.10895 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d1d76644-664e-3769-8c19-963cf65c72e5 | -4.78014 | -45.34706 | 2025-07-09 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 390a667f-d618-3e9e-8cc6-4c5c00bf7d48 | -7.03406 | -43.32064 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fda33182-6893-3c11-80ea-5f4c515e9836 | -10.56843 | -49.12438 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f8883a0-0f42-303f-8831-d91ff034d133 | -8.51515 | -43.28494 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c5e54ea-b17f-356f-bedc-2f057cc141c3 | -7.24701 | -43.07163 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 92677275-9bba-3136-8922-755293064ba3 | -6.17594 | -48.05477 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c538176-b01a-31ea-851c-b38509356d8e | -6.54798 | -43.6182 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dedb70fa-e995-318f-bfaa-db304bfc5568 | -6.82882 | -44.65397 | 2025-07-09 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62200400-a0a9-3a79-9797-db81899c1079 | -8.30582 | -55.11028 | 2025-07-09 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33810e5f-8143-331a-b4da-f68f1e694d86 | -8.54437 | -49.94875 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fe76f3b-07a3-3389-ae48-1194a960e367 | -11.43011 | -45.1242 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6dadf10-fb1a-3776-8ee1-7eac1ed0987b | -10.56989 | -49.12191 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23b0a7ec-bd27-347d-b860-bc14967136d0 | -6.14314 | -43.97657 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1462f0aa-4b9d-3ad7-b8dc-11ecae64cb35 | -9.40856 | -48.44888 | 2025-07-09 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f49b7c49-b964-32d1-9708-d7f95c1a64aa | -7.07868 | -44.31248 | 2025-07-09 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9ba7020-3a78-3132-b86d-586f7b41ab0c | -6.16861 | -48.05349 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4343e654-2406-3734-ade3-74e9576b703c | -7.0916 | -43.42238 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9defae6a-dea6-3890-aa42-e746d966ef11 | -10.58163 | -49.1356 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d115b16-7d1b-3ece-90e3-5c4baa970000 | -11.67139 | -43.77995 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 469f8aad-a8f2-370e-99f9-24efc510788e | -8.2253 | -44.93627 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96c43e97-df98-35c6-abef-2afac9e93670 | -10.56916 | -49.1263 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b55dd260-11f2-3f23-aada-9031c1e41828 | -6.83675 | -43.35383 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ff9bb4f-52b7-3055-aaa8-b6c72e93fb21 | -4.71584 | -42.7873 | 2025-07-09 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b4c9e58-de36-344c-94f3-6121a836cb2b | -6.1693 | -48.04927 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| e3b4f990-8655-3ba5-ad4e-09009ad78a6f | -11.43343 | -45.10292 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8cf168ce-784a-3bdb-88aa-f63547f4edfc | -10.58022 | -49.12179 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95e3ef74-661e-3d72-a2ae-cd698a0ead92 | -9.4779 | -48.67928 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bde0b166-db29-39ac-9e13-3b17f38f32cc | -11.43565 | -45.11055 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48a53751-fbba-36e2-a1bb-a9595e73600a | -7.67199 | -44.366 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99556764-709a-3a26-815a-5cd59d04dde1 | -8.50602 | -43.29884 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ce721705-df93-3d33-b74c-3fb7134992b8 | -11.42788 | -45.11657 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b4f1873-1aad-3e28-9799-94cc34623211 | -8.27588 | -42.27451 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 111d4196-210b-3806-ab3e-df752ffdf49a | -7.09247 | -49.16336 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2edfdfca-02a3-3c29-abb1-e703ec9a3afa | -7.23789 | -43.0626 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69abf3eb-076c-3dec-9b50-6c970d004730 | -7.10707 | -44.37049 | 2025-07-09 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1017785-7a27-35c9-ab37-b7f3c14feb1c | -5.78384 | -43.61514 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc68f44c-bdc7-3756-8af0-b1f41dfa4ef9 | -7.68762 | -44.91151 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed8ee6db-a834-3b13-b51d-1969b01df6c3 | -7.662 | -44.36441 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20202c21-7983-3220-ac22-051fc8ec0725 | -7.03525 | -43.49088 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b9491e-c0ef-325d-a3c4-59ec884a3a65 | -9.28611 | -44.83959 | 2025-07-09 04:21:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 590fe464-d5a3-3747-8e90-2e23f2c52ce0 | -6.85684 | -44.06249 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
