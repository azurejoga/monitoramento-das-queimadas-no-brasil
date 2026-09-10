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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c92ea5b-66f9-3705-ba49-c444076114ec | -6.7077 | -45.4635 | 2026-09-10 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 249.1 |
| c0c688be-e727-3b3d-8525-990f2a1e2a0c | -9.7141 | -43.3956 | 2026-09-10 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 993d3092-4049-34a7-aa45-dd0ba402a959 | -5.7756 | -45.0826 | 2026-09-10 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| abddaf75-3c07-3a5c-b355-ee9cedab4bc3 | -10.7395 | -45.9194 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| e06e0785-83de-3f2e-aaf9-6803270f4896 | -10.0697 | -46.2516 | 2026-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b2911f5c-e184-3fda-9618-65675eb36ab4 | -10.7582 | -45.9397 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 3dad654b-95d6-3acd-9184-1ca54b3fd2bb | -2.7331 | -57.6271 | 2026-09-10 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| c01fd67b-232e-3e31-a493-8ab09f473e26 | -9.7889 | -43.48 | 2026-09-10 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5e44f407-9063-3172-b616-56d4d6f0d6ea | -6.7863 | -58.8995 | 2026-09-10 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 873b374d-964c-3a5e-88e0-773e78fa4246 | -8.8982 | -61.4393 | 2026-09-10 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 03188c6f-4944-3214-9457-80b93647f1ec | -10.6981 | -46.1287 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 528.0 |
| 2260159b-5b64-332a-b204-665f7d88b8a8 | -11.3326 | -45.772 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e44d3411-d998-3ffc-9c61-02dd35620db2 | -7.4976 | -45.2814 | 2026-09-10 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7b04fa3f-1b87-320c-be03-8fb87a1c98b8 | -9.7885 | -43.5036 | 2026-09-10 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 665ad520-91c7-3955-8cff-3282ad5db565 | -6.1538 | -44.6446 | 2026-09-10 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ca090b73-9f73-39da-a73a-39ace911c011 | -10.7585 | -45.917 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9ce59f56-4f3e-3a54-82aa-cda8361e568f | -6.7077 | -45.4635 | 2026-09-10 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 378.2 |
| 41839c29-e6d6-3808-b6c1-a30a163d2d99 | -6.708 | -45.4409 | 2026-09-10 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1acb9833-32f7-3cee-9bed-e0d9585e852a | -10.0697 | -46.2516 | 2026-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| e0363edc-58c1-3fef-9773-37ae810b27bb | -2.7331 | -57.6271 | 2026-09-10 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 11911ff4-ce43-3014-a9dd-3ab98cd1b8e0 | -13.2295 | -61.6578 | 2026-09-10 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ab752a79-744b-3b19-a580-2cc76e712d83 | -9.6746 | -43.4948 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 79418b63-b072-3bb2-bab7-f3eaf78f273d | -6.7863 | -58.8995 | 2026-09-10 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1d6efdc9-cdf6-3719-b4a8-e813436b2fcf | -10.7585 | -45.917 | 2026-09-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 67bcc09b-b8ad-395d-b4b7-118699439344 | -5.7569 | -45.084 | 2026-09-10 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 45377459-b77c-35f9-98ca-879566ee3d3b | -7.1198 | -42.1309 | 2026-09-10 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 0ae60af3-b2b6-35ad-85e7-cd7012b2adb7 | -7.4976 | -45.2814 | 2026-09-10 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 5dff0f61-51f5-3014-a587-8164cc615083 | -9.694 | -43.4688 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 5513cd37-1ce5-3a99-9d41-a28238ad965a | -7.587 | -45.6804 | 2026-09-10 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d97f5d7a-be48-31ab-a156-92a62f42bb47 | -9.7889 | -43.48 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6120f14b-1405-3993-a714-1c649c714d4d | -9.7885 | -43.5036 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| b5713d3b-25ed-36e0-a657-2f0bdcc88ce8 | -9.7141 | -43.3956 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 105.2 |
| d614c6fc-a7ac-3a3b-94a5-d9c05c9e7bec | -8.8982 | -61.4393 | 2026-09-10 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3066f5fc-640a-35ee-a190-cdb11e901342 | -13.2293 | -61.6772 | 2026-09-10 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0baa68af-6317-34e6-af41-066cecad2069 | -13.2297 | -61.6384 | 2026-09-10 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d05f2e10-d8a4-3a4f-a24e-c9dd25069bd5 | -7.9837 | -43.9719 | 2026-09-10 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1acfa264-66e2-3579-9d32-469dd2fa7194 | -10.7674 | -60.7666 | 2026-09-10 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 65abcebd-f4ed-31e7-9fae-3c51fe0e2d70 | -10.7582 | -45.9397 | 2026-09-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 468.8 |
| 28cf82be-6dd7-3c29-984c-d3993af19830 | -6.8226 | -58.9947 | 2026-09-10 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 074ad36e-0f29-3ca7-bd2c-54dea26e1b54 | -7.9834 | -43.9951 | 2026-09-10 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 28b90ca6-13a5-3afa-92ed-81d19cbcf3b4 | -10.6981 | -46.1287 | 2026-09-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| f664264b-0a84-3ec2-917a-120754c78d1d | -6.1538 | -44.6446 | 2026-09-10 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6e57bfd3-5c70-3094-a643-b8adcf0aa95b | -9.675 | -43.4713 | 2026-09-10 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 139.1 |
| bd36a782-72b4-3613-9b7c-8d2d23fa6e4e | -7.1009 | -42.1327 | 2026-09-10 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 1c677bbc-fe6f-36f0-82fe-0f532bacee9d | -9.08779 | -67.87305 | 2026-09-10 13:46:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 52b1000c-d3ee-38dc-b477-016278166398 | -9.7889 | -43.48 | 2026-09-10 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 44659d66-fc7e-33ad-a7e4-1139f5ea812f | -7.1009 | -42.1327 | 2026-09-10 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 69144f64-ee58-3690-a01c-afd1f77bcfed | -13.3055 | -61.6527 | 2026-09-10 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 81314cd6-dabe-3aba-84af-aa0e888a9ebf | -10.2559 | -45.2292 | 2026-09-10 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| da9c3958-ca17-3b0f-85bb-c31b4e530da8 | -10.7578 | -45.9624 | 2026-09-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 13eff06e-0a18-3b6d-ae16-53028b34b40b | -13.2295 | -61.6578 | 2026-09-10 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6cfbb886-2d8d-3857-906a-69700537049b | -6.7863 | -58.8995 | 2026-09-10 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 623720b0-18ce-3767-9750-17ee10bb1047 | -10.7582 | -45.9397 | 2026-09-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 731.6 |
| 5ddb79b2-5cb5-303a-b0ab-cd7a6bb6d811 | -5.7569 | -45.084 | 2026-09-10 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3cf95839-9a83-36be-8d7d-5c8df5923dcd | -9.7141 | -43.3956 | 2026-09-10 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 0eca6dde-3dc3-3ebc-a3ef-5a8f46a425a3 | -7.9837 | -43.9719 | 2026-09-10 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 66fc8c18-4e2b-3975-8d28-ef6a3a4dec57 | -7.9834 | -43.9951 | 2026-09-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| a81fb8f0-dfc6-3c08-b1b2-5c837e3b7b6b | -7.4976 | -45.2814 | 2026-09-10 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d626d55e-2739-38e5-b735-398855e8daa2 | -13.2297 | -61.6384 | 2026-09-10 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| cedbdace-abab-35fb-9beb-7a9c8d44eaf6 | -10.7585 | -45.917 | 2026-09-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 1b1557ea-4d6f-3778-9334-faae1ec1701a | -9.675 | -43.4713 | 2026-09-10 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 9a4bee4a-fe7b-35cf-b755-04430baa3de7 | -7.1198 | -42.1309 | 2026-09-10 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 18efb094-a5c3-3a68-b021-7b57e8606844 | -9.694 | -43.4688 | 2026-09-10 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 08c2e6b1-7e3c-366a-a76d-a5328502231c | -13.2293 | -61.6772 | 2026-09-10 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d8fd9345-f493-3e1d-9086-81e4817a483c | -6.7684 | -45.0279 | 2026-09-10 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| c86fd348-e7bb-3ba3-a4ba-fc1afb3c9850 | -10.0697 | -46.2516 | 2026-09-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a39df7f4-19cf-38f4-8147-bda1b551e15e | -10.7674 | -60.7666 | 2026-09-10 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 705f3836-9a2c-3f95-92eb-2a3cad4cc4ab | -9.7885 | -43.5036 | 2026-09-10 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 1aad66ce-a246-3dcd-9d34-ab9a29fd46a1 | -6.7077 | -45.4635 | 2026-09-10 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0e87bfef-2b7d-31db-b1bf-ff385f07193e | -8.8982 | -61.4393 | 2026-09-10 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0e6e0136-51e5-311e-af9d-478409636671 | -7.9837 | -43.9719 | 2026-09-10 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f25ebd5d-7860-3dc7-9fe8-b842edda8f67 | -7.9834 | -43.9951 | 2026-09-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 68372366-83db-3b26-b207-c9ae0beecc34 | -7.1781 | -43.6105 | 2026-09-10 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c7d0a867-976e-3079-b884-0665f2f61190 | -7.1198 | -42.1309 | 2026-09-10 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 96d9686e-760a-390e-b130-6be98dcc4c64 | -11.3326 | -45.772 | 2026-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 99cced09-16fc-3e83-a2af-8d6337475831 | -7.4976 | -45.2814 | 2026-09-10 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8ebce049-1990-3992-b0e2-674da42fa53d | -9.675 | -43.4713 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 03bae087-033f-3004-99e0-a50fe51dd169 | -7.1009 | -42.1327 | 2026-09-10 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| ba5b2fc0-3933-3b80-ba91-55078e0a5ed9 | -9.7889 | -43.48 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 45eea045-a6fa-3a9b-8525-6d3af518ffe1 | -10.6985 | -46.106 | 2026-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| d00097d7-1e13-30f1-a6f5-2f1eb920d7ad | -6.7077 | -45.4635 | 2026-09-10 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3e687759-7fe1-33a7-9804-27d4a20f8e2b | -13.2297 | -61.6384 | 2026-09-10 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2101f6e4-487b-3f8e-b295-90508a94d2c1 | -10.6981 | -46.1287 | 2026-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 452.1 |
| 92489601-f349-3d13-8f54-96e37d5acee9 | -13.2666 | -61.7524 | 2026-09-10 14:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 92a845a8-49dc-366a-8ebd-77d3852328d8 | -10.2358 | -45.3004 | 2026-09-10 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a4cdad98-f948-3c22-985f-040056a0b54e | -10.7674 | -60.7666 | 2026-09-10 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3073da45-db28-3d04-9940-2a1ac196b25a | -10.2362 | -45.2775 | 2026-09-10 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| cc486d37-cc99-3a0a-82b1-d0e1bcc8415e | -8.9898 | -44.9918 | 2026-09-10 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 701ba874-516f-31ac-98cb-764e8ddfdcae | -9.694 | -43.4688 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 243b3cc1-8277-3a75-84b7-4c95e90d91a2 | -8.8982 | -61.4393 | 2026-09-10 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 39426fde-cdbc-32bb-82e6-ce51ddb03f3d | -13.2667 | -61.7329 | 2026-09-10 14:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 94bef4c4-b745-3cb9-90ca-e6ef9869e46f | -9.7141 | -43.3956 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 135.3 |
| e729a602-b9ea-3a86-8c0c-ebb5a7d0a325 | -5.7569 | -45.084 | 2026-09-10 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3fc859c1-4e35-33b6-9ce9-97a23b48cb09 | -7.5167 | -45.2569 | 2026-09-10 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bfc760a8-d69f-300d-8d81-53baa8668757 | -9.6746 | -43.4948 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 199be1ef-b024-34b8-9b91-13dd8097f615 | -13.2295 | -61.6578 | 2026-09-10 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5eaa9daa-2b5d-31fe-8cd3-23f096f918ad | -7.587 | -45.6804 | 2026-09-10 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4afbcfcf-72d9-3328-9272-f0e73ae375c4 | -9.7892 | -43.4564 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d976ee32-73c3-3c81-91b6-d8c423a14efd | -10.4288 | -45.1153 | 2026-09-10 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 86a90d41-3d34-3d9f-988b-1a498c5a3333 | -6.8226 | -58.9947 | 2026-09-10 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |


[Clique aqui para ver as próximas entradas](README49.md)
