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
| e3ca971a-f471-357f-8608-7b736b9106fb | -8.02861 | -43.14064 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 637b0a77-63b2-3c22-abc3-e6db162a9f85 | -6.52595 | -42.81613 | 2025-08-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11666eed-6203-3417-85a1-ab2b4046ceca | -7.24474 | -43.38415 | 2025-08-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d65e00c-48d1-3ce0-8487-83c045c4e494 | -8.44767 | -47.4818 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffc6f3f0-0b98-3920-a630-8de3127b165b | -8.02274 | -43.14586 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e50e8254-aff0-369f-a269-8eda19f6667c | -6.70306 | -44.35915 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a03f735-1405-3149-930b-41a43e263562 | -8.29149 | -46.35587 | 2025-08-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4776d750-4d26-3e8f-a8f7-e49cd97330b9 | -10.46167 | -52.71929 | 2025-08-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba5bc4c8-69ca-3bd5-aabd-3a6cca563038 | -4.31385 | -48.09957 | 2025-08-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 962b05d9-65b9-3d5e-bd25-de806e69ef5a | -10.07683 | -46.77885 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0d6e49d-c6a8-364e-bc1f-dc1e6173f6e1 | -10.0284 | -44.71494 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 195fa288-eb74-3e49-9d38-08d21b7d6412 | -7.28439 | -43.05481 | 2025-08-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3784d4e5-5c71-31a5-bb41-210c80978648 | -11.93992 | -46.67865 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2a18557-32a5-308b-b0a4-6f4aa6ce4d5d | -7.87727 | -45.53337 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdda5543-7636-391a-99ef-a6a927416a41 | -8.25357 | -49.59648 | 2025-08-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9723030-9e67-3ad2-b395-3e33e5300a59 | -8.04787 | -43.11292 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 477f7ab7-8ebe-3dba-988f-ae67a867cd44 | -11.35149 | -51.26135 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2405010-7091-3f2b-90da-4fcb1ebef06d | -10.08055 | -46.77954 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab26b2cb-f0a7-3c9e-8381-2ec4b061a643 | -6.66664 | -44.74303 | 2025-08-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae26dcde-efc9-3af5-9ee7-f3257a03f567 | -8.70636 | -47.3409 | 2025-08-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6e2773a-4c36-3d66-960d-1681533db2a6 | -10.03309 | -44.71561 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bb65dab4-85cb-3edf-a8a8-668599b82812 | -9.39481 | -45.49957 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9a89e80-5c4c-38e9-9b9a-7b0410ca2133 | -6.69923 | -43.07297 | 2025-08-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac6ec72a-ac78-39f2-b023-8a2c6f9f437c | -10.04525 | -44.71426 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09eea36d-c2e2-3a2f-8078-047012c299f6 | -8.03689 | -43.11743 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 06139ce6-faa2-3f22-b66a-12c6305514d4 | -11.67125 | -43.77362 | 2025-08-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239e480f-8a59-366f-a418-03f92e9d9269 | -6.7037 | -44.35462 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0f241b5-7338-3ec4-8221-80d480096d14 | -11.94578 | -44.92073 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ccc328e-db4e-3d22-a4bd-187d3c4ef161 | -8.03101 | -43.12267 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 2782f901-460b-3768-af98-0edcf864c1e0 | -9.19533 | -45.28918 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46832499-0d6e-3e54-86e7-a208cf79fa6c | -11.94467 | -46.67524 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f29e40b1-1a5f-324c-8d5b-4f5e49185551 | -8.91552 | -47.33534 | 2025-08-02 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bea1baa2-81c5-329b-8eff-73e8ccce85e2 | -11.9584 | -46.66899 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6266deb6-5a68-330c-b571-05d14f9a6288 | -8.02821 | -43.14362 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c2cc40b3-7178-35c8-b011-9e59057bc3fa | -10.08104 | -46.77596 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5251ef6-ce3b-32ec-8558-8348eaf5eaf5 | -7.33471 | -44.66045 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 467c6618-f42d-3fa7-b07b-cb68d9dfab36 | -8.03181 | -43.11666 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| cb08b3ba-8cda-3e68-b383-a8d83c9f4b9b | -7.69228 | -45.11431 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 624ede3e-9332-3ece-bc9a-c71faded58c1 | -8.03569 | -43.12642 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0086ad0c-b846-3515-9c5c-e9d216575e7a | -7.58257 | -46.10418 | 2025-08-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aadf01db-f171-3ee7-8edf-b27daf3fa51d | -8.05376 | -43.10765 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c96a467a-e075-383b-baae-c4759e002edd | -6.52553 | -42.81907 | 2025-08-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d768d6d-612d-3d7f-a16c-987a2b16e48d | -6.68477 | -44.35635 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a56a7fe6-704f-3367-b664-f5dc0c5c57c9 | -11.92093 | -44.84397 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 391cade4-c371-3973-ae0b-9ae285f53d96 | -7.87671 | -45.53748 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8578334-c771-3a34-9f04-61b6c6b39734 | -8.03489 | -43.13242 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 9dff4f85-84c7-3256-9a65-d9ce7b214767 | -10.03584 | -44.71311 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98f9b743-33d3-336d-90cb-085c3e78c73d | -6.96342 | -44.50765 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38aa74e3-bcab-3ef9-a4ec-6e8bb21f1ce4 | -8.04238 | -43.11518 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c3c1b27b-5bfa-3323-b843-13b25b4914a8 | -10.25631 | -50.25821 | 2025-08-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48368367-0cbe-3b65-90e2-d12ef3e31d2d | -10.25401 | -50.25023 | 2025-08-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df50e2ce-58b2-351a-9fbd-f13a9ab67ff3 | -7.04241 | -44.40968 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80699171-0fca-3d5f-8541-88ee78818b65 | -8.03141 | -43.11966 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 4825785f-36fb-35de-bf75-764faef9b55a | -10.62734 | -45.30258 | 2025-08-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc64dce9-4dfb-39c8-bb72-fc1717670f5b | -7.11677 | -44.67648 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9da33e83-3f60-37a0-a1d3-5d612293683a | -4.7767 | -45.33627 | 2025-08-02 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d0f5de6-7dd9-30d7-937d-50e052aee4dd | -8.4957 | -48.21759 | 2025-08-02 04:46:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff588043-a827-32bb-a7b6-0305beee5d4a | -8.70831 | -47.34346 | 2025-08-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c07c0279-40e8-3ed1-b5f1-afb0039c7a9f | -10.04249 | -44.7168 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31ee425b-0937-3437-9fbd-273a3354d1fd | -8.02901 | -43.13765 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b3ecd299-d3a1-3ba7-9c36-4c35fbbef0c7 | -10.5793 | -45.27227 | 2025-08-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 081c0294-a004-36ce-92e2-325bec12e21a | -10.45121 | -47.22858 | 2025-08-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f2325a1-ec44-3437-8183-fb577a6fbd33 | -8.03729 | -43.11444 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0c2bacd5-e32f-3614-84e1-4ed1a935f906 | -8.2336 | -49.93828 | 2025-08-02 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dad9884e-8385-3391-a518-b76fd2690f5b | -10.08092 | -46.77944 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7df94d6-253a-34bc-a92a-b273f2d47b1b | -11.95077 | -44.91241 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66c5bc08-9e2d-3cc6-bf5e-dc4f31727fc8 | -5.4823 | -42.1576 | 2025-08-02 04:46:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 995f5a69-47f8-39ce-9774-4a94a3a82097 | -5.65903 | -42.57808 | 2025-08-02 04:46:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b14b8e92-3c77-3aeb-a4a1-f63e7ac900b0 | -11.97584 | -46.66732 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 722c8a3c-d796-30a8-b629-babd2e96d713 | -7.88157 | -45.53404 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c6ea80b-0780-3961-bde4-d3b65c26e575 | -7.88317 | -45.53521 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0944824f-e53a-36ea-a39e-e4f7da6273b4 | -9.19919 | -45.29401 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc5d550a-638c-3373-861b-73185eda1de5 | -10.25686 | -50.25449 | 2025-08-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5cb4071c-e686-3c65-bd7e-b4b0acb6b1a0 | -7.74729 | -45.13764 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b3cbe03-b582-3eb7-9be6-d76ebb84aadd | -6.70253 | -44.09375 | 2025-08-02 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd467018-94bd-36de-8527-f98dc7de0d49 | -9.5844 | -43.84457 | 2025-08-02 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88d38445-3f01-3c9a-aa07-3ab0150009ae | -7.75172 | -45.13808 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5854406-fba5-3514-932f-4de27ba4ef23 | -6.66728 | -44.73859 | 2025-08-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e63e8c-9274-3987-a7b8-470ce371057d | -11.51793 | -44.3327 | 2025-08-02 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41467384-ef1e-3bca-8267-1ab1bee104a5 | -6.23648 | -46.15501 | 2025-08-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cff0e51-6f49-32ea-bd0f-b3dfe7b12554 | -11.96317 | -46.66546 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2be2ddb-9928-321a-897e-b02af5d685df | -8.70568 | -47.34575 | 2025-08-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8285c75-d13c-3e04-9d23-2db2e2a892c2 | -8.05417 | -43.10464 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a67e48ae-1b1f-3f46-b131-5670ac0e87a6 | -9.3998 | -45.4958 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e35f15ae-53ba-3370-9ff6-0e83e09e389c | -9.59009 | -43.83972 | 2025-08-02 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1839595c-c587-317d-b0b9-0d5befde8823 | -8.02981 | -43.13168 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 972b2301-b640-38b4-83bc-d8cecb36b8f1 | -10.37497 | -55.31813 | 2025-08-02 04:46:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f187b85a-5ae8-3875-93fb-e3c6a91ba498 | -10.46072 | -47.23149 | 2025-08-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7ffe986-eaf5-3cdd-8849-c83a961dc981 | -9.39519 | -45.49752 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f42c8c63-e853-3b66-a998-32de3e5d34fe | -7.80905 | -44.92197 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb678d1-925e-30a7-90d0-de74d2bb70cf | -6.73106 | -43.99138 | 2025-08-02 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83e6ed95-fecb-353e-9ecf-0b85dc8a1005 | -6.78811 | -42.98517 | 2025-08-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d3fd476b-c31d-3aee-bc02-507a97d9fdc8 | -11.94414 | -46.67922 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 913e799b-1ca0-3e24-bd08-36446caf93e5 | -9.05443 | -45.0649 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d58402b9-cf01-3237-83b0-f8295e6b1202 | -7.33971 | -44.69001 | 2025-08-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a34e9cd3-8062-3413-a18e-2ae776dd8fa3 | -7.34885 | -44.65849 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4db9c835-a35e-3c5f-b922-e38f29c3014b | -7.15261 | -43.27171 | 2025-08-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b3e994d-f5b2-303e-ae2a-a2fd1eafea7c | -10.68136 | -56.55268 | 2025-08-02 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bca329f-8611-3753-ae47-0df644402b62 | -9.58515 | -43.83895 | 2025-08-02 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8da6e98d-0307-3aa3-ae67-bf922dbc9108 | -7.29331 | -46.03669 | 2025-08-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
