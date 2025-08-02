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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed794057-9fc1-3f4e-9603-a6faf9e8dac2 | -8.30737 | -55.11033 | 2025-08-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee02002-48d6-3f86-ab80-813396e06104 | -9.19087 | -45.28861 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eaef258b-c63f-3f7a-8e12-3c8e53067379 | -3.53073 | -52.86773 | 2025-08-02 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ad942fa-2839-3b75-8e91-c95ac0405727 | -8.91455 | -47.33355 | 2025-08-02 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac733c79-13f5-3e75-8877-2dceac1ff909 | -8.02941 | -43.13466 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 984bed68-02df-3319-a89f-02eb9dc462ce | -7.87948 | -45.53042 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4edf3f92-f030-3304-b990-3a4740523406 | -5.48754 | -42.15828 | 2025-08-02 04:46:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc724f63-ec2b-3006-b5e3-90f50a7504c2 | -8.03529 | -43.12942 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8fc010d6-05dc-321c-91d9-154f0eb5dc2a | -8.29611 | -46.35285 | 2025-08-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 672e2566-54e6-35b6-91c0-e619f8902f47 | -5.74017 | -39.77153 | 2025-08-02 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d94a3006-af57-3f7d-8fe1-3c531262fd28 | -8.5949 | -45.50159 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f2c97f7-1b17-3beb-bde8-9090d3e6a3c0 | -7.04443 | -44.39553 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ffbeb24-b12e-3ee0-ba82-74b722bfa500 | -10.6413 | -45.23142 | 2025-08-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09144c79-3b3f-3c60-bb75-094ea26c9ebd | -10.45675 | -47.23086 | 2025-08-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61b23240-61aa-391a-bbef-debeb6c167f2 | -10.25345 | -50.25396 | 2025-08-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf08eb03-3a18-310e-988a-6fc2317b71d8 | -9.04868 | -45.07337 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7607854e-7380-3c61-bc58-6cbfa41185b2 | -9.06473 | -45.05682 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e34258de-120c-3f14-85ba-31ed537c1f0d | -8.43933 | -47.48546 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f90c6072-3223-3155-88a7-824b1bb2f748 | -8.05926 | -43.10538 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86359e63-0246-37b0-a2b0-f53639f74d56 | -8.57493 | -51.54405 | 2025-08-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564db156-d2f4-3384-b649-4c8591ee70cc | -7.58146 | -44.81158 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c37b1501-dfac-3582-b78c-6c769d9992f9 | -11.23294 | -48.90078 | 2025-08-02 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54127497-215f-3706-9c7f-8162287c7e21 | -10.32903 | -57.48037 | 2025-08-02 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9fadf17-c692-3f3c-8d3e-c2d678fe34da | -10.07632 | -46.78246 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957d8ada-2794-3f42-adcc-b0b8aa5d4ba6 | -8.38234 | -44.03181 | 2025-08-02 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b070e21-e9c6-35c3-b5a4-2af3e8c7fe37 | -11.35483 | -51.26188 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a1b081-42f2-3df2-8da6-2adc9f136bfa | -11.9141 | -44.85916 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43e98e42-0f81-3101-b38c-a8a03bff6ce7 | -7.87888 | -45.53455 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c46b177a-227f-3ed9-bdc8-19db15e68165 | -10.03778 | -44.71627 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fbb3da8d-bed1-3329-8b1c-313e091308da | -11.76267 | -44.97723 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f0cb189-f7e3-3f32-b8aa-2c7bfabd685f | -10.64068 | -45.23618 | 2025-08-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f36503f8-4997-317a-ac78-0a5d80ceabc8 | -9.39018 | -45.50124 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9aeb660c-b0b4-32ad-a86e-9fd1cc870fc3 | -5.74628 | -39.77264 | 2025-08-02 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83a637c5-ec2c-35ac-b2ec-b8ee172a5741 | -10.45519 | -47.22921 | 2025-08-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad58a05-58cd-31fd-a439-7a4f2b3395b2 | -4.77255 | -45.33557 | 2025-08-02 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 194131fb-2799-3103-bdaa-8362483045a5 | -7.56801 | -44.80937 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65c9b796-82ec-37ad-96eb-fb6dbe1b8636 | -8.04278 | -43.11219 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 07a46fb0-65a7-3b26-b912-7e6f8b5d97f4 | -10.58319 | -45.27783 | 2025-08-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 060057a2-2f53-370c-b9a3-fe0ec4ae493e | -10.46109 | -46.94139 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc36f694-5d7d-37a9-a980-60b3d747ac05 | -8.49937 | -48.2181 | 2025-08-02 04:46:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8c020fc-7d60-3cdd-ad85-22d228579daf | -5.91282 | -45.58567 | 2025-08-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f16be3-f823-30f1-8d39-e8bdaaaee8dd | -7.56864 | -44.80481 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42654e16-fc87-35d8-9024-47219eeef57c | -8.44385 | -47.48127 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 618e5085-77af-353f-83f6-4632da58a5a8 | -6.96281 | -44.51205 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1140e06b-ab3f-3c32-976f-ad1a50c8f3d7 | -7.03713 | -44.41394 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 600d7759-ef27-3439-8cba-d355c0d0e108 | -10.46057 | -46.94503 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 386450ee-feb5-3acb-a2fa-2390ae285645 | -8.8415 | -49.85609 | 2025-08-02 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 148ebe93-64b6-3684-b9b9-9b1cb3eef25b | -6.53226 | -42.80817 | 2025-08-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0ced1e1-5bba-303c-aee7-cc739badefec | -11.9479 | -46.71563 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2aba4ea-97bd-3e56-a78c-5b17d026d65f | -7.87829 | -45.53867 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b877ca4-11b7-3301-a66e-27584746e1ad | -7.82079 | -46.88913 | 2025-08-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 350b362e-08ad-3492-a306-868e123ef5b5 | -8.91484 | -47.34024 | 2025-08-02 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf048fd3-9365-305e-801a-3ce965a1a896 | -9.04994 | -45.06406 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa7c942-b0d7-30a2-96b8-ea2981ae084c | -9.39539 | -45.49525 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 21226e3e-fb41-308f-8cb7-550625153464 | -9.0878 | -45.89684 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 244581dc-bcff-3f37-a9ca-439562a76c3f | -9.39078 | -45.49694 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0af5b33-bf0f-31f9-a634-3f261da87870 | -9.39961 | -45.49806 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68169adf-7f09-3870-892f-1c486e6ece03 | -8.03649 | -43.12042 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 22fc90b7-5693-395d-b556-38db3ec7324e | -7.65927 | -44.78094 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f47c19b-ef0e-3a80-bf27-749edd4bd6b2 | -7.43807 | -43.82818 | 2025-08-02 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff3d1a0e-b8b2-3caf-ab5f-bb69f5629268 | -11.56916 | -44.84991 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ce5098-0615-3fbc-9951-152f755667a0 | -6.69383 | -43.07509 | 2025-08-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04c290f2-b260-3605-b5b3-8f7b5c22cd82 | -11.23356 | -48.8965 | 2025-08-02 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ae0cbdd-d382-3864-ac61-cd8aad4db3a5 | -11.19365 | -51.51413 | 2025-08-02 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0497d8cf-6726-37ef-bb3a-ddaa844b80fe | -8.44073 | -47.47596 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fd327fc-69b0-3d4a-9590-745baed2bad9 | -10.45917 | -47.22985 | 2025-08-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf19cf2e-f169-334e-bcbe-ecc0fb48d05a | -9.19984 | -45.2894 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4961836d-d45b-38b7-8ec2-14e8bfcbe010 | -10.23497 | -50.5156 | 2025-08-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b02716b1-0e80-3eb4-a8fa-45df3831bc55 | -9.19855 | -45.29858 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 318888bb-d917-3d92-b130-dc7654002049 | -5.65144 | -42.59505 | 2025-08-02 04:46:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40b554ec-20ab-3a1c-9f79-703e05c2e7a0 | -6.68546 | -44.35147 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 777700a7-217f-32fc-8a54-8554dcdf0948 | -4.77419 | -45.33821 | 2025-08-02 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc99ab9f-a9e0-378c-8fc1-2895eb0aa833 | -11.94942 | -46.67184 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9069af36-46d6-3d60-b0de-e042a8e843de | -9.1947 | -45.29369 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| becbb3e6-aea0-3191-ac5f-51b387a8e703 | -8.44003 | -47.48073 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a8d0eb0-e46f-39aa-bfd9-c0a472d0cc4f | -9.0506 | -45.0591 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26cf89e3-47cd-3587-b2a2-f8aeec71ddc7 | -8.2302 | -49.93776 | 2025-08-02 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a02458d5-9ebe-3457-8fbc-514848acac09 | -10.49199 | -47.4575 | 2025-08-02 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86ffba81-dc16-31c8-a4d7-f075fba9f7e8 | -7.04837 | -44.4007 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23c6d92c-0eb2-3e7d-b0d3-31a7377f3f1b | -9.04807 | -45.07792 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f751d25-4d38-30ce-a3ce-41271ccfeddc | -7.0378 | -44.40923 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e2a17f1-75cb-3462-873a-5ed3a60aa3c1 | -11.1931 | -51.51768 | 2025-08-02 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 685cb90b-861a-35fb-9ebc-40f3e03aea35 | -4.31325 | -48.1035 | 2025-08-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63ec8708-4898-3012-9178-0a66daa8c31b | -8.03061 | -43.12567 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 84add5eb-ceb9-30ff-a9ab-1eb0ab128837 | -11.92024 | -44.84922 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccd8b9f6-12ce-3cbd-882a-44570c205ee8 | -10.46613 | -46.96428 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab91bdba-04dd-3eda-acd5-4de5245ae1aa | -7.34373 | -44.66198 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f2984f1-69ac-3115-b8c0-98f65433715a | -5.91336 | -45.58199 | 2025-08-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 015278c5-3630-3caa-a47e-c0052a0bb1c5 | -10.46111 | -52.72281 | 2025-08-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28ca9bdf-85e6-39c1-855a-37a6baf910f0 | -4.77473 | -45.33443 | 2025-08-02 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f32e176d-d135-37d4-a19f-683093ae195a | -10.45191 | -47.00647 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a3ac2c6-34bd-31ca-96aa-008741db7ed4 | -10.4616 | -46.93773 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d251c325-a3d4-3fc9-9f90-960aab861aa1 | -6.5656 | -43.90997 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 519e77c7-23ba-3670-8e80-5533ae35001e | -10.45858 | -46.92977 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1380b035-27c6-3d30-9d31-b48f3d647f5f | -6.7072 | -44.09436 | 2025-08-02 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba903417-5006-3518-92a0-2be7dc28f2a7 | -10.03115 | -44.71242 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a953c5e6-3e4a-39d3-9d79-f2f97878ac35 | -10.64524 | -45.23689 | 2025-08-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 630d03c2-3846-31a5-a544-0f1667e6e430 | -6.48287 | -44.77176 | 2025-08-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fadba726-5394-36f0-a57a-527b1e1aa0cc | -8.02235 | -43.14883 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| cbc6471e-c959-322f-859d-9990c49b08bd | -8.57162 | -51.54353 | 2025-08-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
