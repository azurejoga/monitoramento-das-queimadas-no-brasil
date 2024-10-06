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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dadc136e-f795-3014-9619-d70066ca89c0 | -12.84955 | -62.80117 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 638e6d19-8271-32ae-86a5-dcd46a54da52 | -12.84581 | -62.8005 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90c252e5-3100-3344-8981-bc9a2e2acce6 | -12.64273 | -63.09638 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53546db-9d33-3e8a-b2d0-dd73742ff302 | -12.64189 | -63.10119 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af7c90b-015c-390a-83c4-711e61c8b15d | -12.63426 | -63.09985 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf2846c-e0bd-33b6-9174-68bd36802859 | -12.71464 | -62.95234 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47ccdc46-dac8-3dd4-94f8-2f11d58819ab | -12.71328 | -62.93754 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f81d93-4e70-34f1-bdca-c631c07f2867 | -12.71086 | -62.95166 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfc76e51-3979-3733-979f-7ad9f55b277e | -12.71032 | -62.93217 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51353989-2300-3dcd-a42b-47668e258c02 | -12.70951 | -62.93687 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e891c0d-b492-366d-881a-185263d2701d | -12.70789 | -62.94629 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93bc8183-5cf1-3d4e-940b-8efe86794bdf | -12.70654 | -62.9315 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c3a25da-5c60-30ae-9e4d-8b545fa288bf | -12.70573 | -62.9362 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd47d40e-96cb-3977-bf95-cf8cb4d2d42a | -12.02528 | -63.74191 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a61fe48-0aa6-3a3d-9999-46e6f40c226c | -12.02466 | -63.74546 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11679246-bc30-33ae-a8fb-936d27ebf017 | -12.02404 | -63.74903 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6caed1ed-4df3-3f86-98b6-de44a4e5df4b | -12.02341 | -63.75262 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7ad5a0-0f56-3b65-b5af-a442621b6fd4 | -12.02128 | -63.74121 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72cbdc97-4d63-369e-9d04-898cdf53f25d | -12.02066 | -63.74475 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 935cf20e-d9e7-361d-bfd2-e3a6ebabcaf5 | -12.02003 | -63.74831 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c096ea05-9cc6-316a-a0ea-993de89deeff | -11.98983 | -63.53035 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 620ee926-4b1f-3362-ba0c-56ef4f3b2229 | -11.98942 | -63.52682 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5990ff91-725c-3d0d-95c7-87e7ad7508c2 | -11.88619 | -63.28831 | 2024-10-06 05:14:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 245ec3d6-68a7-3712-96a3-a922f4e110e5 | -11.87839 | -63.28691 | 2024-10-06 05:14:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 699f1274-4f01-3ee9-b54c-da9ab2627970 | -12.43721 | -63.69085 | 2024-10-06 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd80b6f-7005-32e8-962f-6c94dde2c6a5 | -21.85741 | -48.44071 | 2024-10-06 05:16:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5c87fb8-9efe-38c8-b912-ac5f15d249b7 | -21.85697 | -48.44605 | 2024-10-06 05:16:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6ae3d05-7ea0-3c23-ba99-1fc8b0fe921d | -21.85063 | -48.4452 | 2024-10-06 05:16:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6409c6f1-242a-3de1-b1cc-1df10c64178f | -21.85019 | -48.45052 | 2024-10-06 05:16:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 368c43d6-c149-3622-a811-5833881dcd79 | -21.58899 | -47.94562 | 2024-10-06 05:16:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d7719f2-09e3-33e3-a5b2-c329a9dac4a7 | -21.58882 | -47.94358 | 2024-10-06 05:16:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bbebbf1-4b62-33c7-bada-f0fe95e7cea1 | -21.58838 | -47.94944 | 2024-10-06 05:16:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff1ab764-6dde-389d-853d-8451c8101ed1 | -20.78209 | -54.82801 | 2024-10-06 05:16:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2485c886-d3a8-35cc-82dd-970c87b9bd4c | -21.40989 | -57.24901 | 2024-10-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10119a59-0e38-3d24-99bd-67c160e07586 | -21.4093 | -57.25336 | 2024-10-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7825d23-aa94-3513-a2ad-6061e2460ad3 | -21.40678 | -57.24431 | 2024-10-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 570cec33-2a64-3e40-b88b-4646e542dd89 | -21.4062 | -57.24868 | 2024-10-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4546eda2-b88a-303c-8be5-5ec247dd82ed | -21.40561 | -57.25303 | 2024-10-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d030520-33e9-3e42-8b8c-8e408619b13c | -21.78155 | -46.18659 | 2024-10-06 05:16:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 326d2a38-d1c3-37ab-8096-2324c0095072 | -23.72429 | -50.0574 | 2024-10-06 05:16:00 | NOAA-21 | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8a5d04d7-bb50-35a7-b742-486f1dfcd74d | -21.51305 | -50.91742 | 2024-10-06 05:16:00 | NOAA-21 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2ab0cdb4-0e0b-3fcd-ac84-9a11ac4dd304 | -24.98164 | -51.84588 | 2024-10-06 05:16:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 667f4fdd-0156-34ee-a0aa-a31f772879ad | -24.9813 | -51.84956 | 2024-10-06 05:16:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2be359d2-8ac0-3ba5-b291-aa57c85f12ca | -25.02108 | -54.07843 | 2024-10-06 05:16:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 10418e51-c601-3699-8971-7ecc44a275fd | -25.02058 | -54.08326 | 2024-10-06 05:16:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4743d00d-987d-35cd-9037-8af1252f669d | -25.01643 | -54.07788 | 2024-10-06 05:16:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 572cc7c1-ec10-3ea8-9b24-084e40320a3e | -25.01592 | -54.08277 | 2024-10-06 05:16:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e3064af0-a82a-34d5-a355-5eacab8f0e83 | -23.89537 | -54.22218 | 2024-10-06 05:16:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a3f35278-76fc-3a06-a70c-fefa8d09caeb | -23.89441 | -54.22093 | 2024-10-06 05:16:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aa749214-e354-3d18-bd8f-5bed4af29258 | -23.89387 | -54.22579 | 2024-10-06 05:16:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee314e68-f2b6-3604-b51c-bb0088024f29 | -20.78161 | -54.83185 | 2024-10-06 05:16:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfd6c36f-0015-3ed7-89fc-62e833da89a6 | -20.58274 | -55.74548 | 2024-10-06 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69262224-9876-3e39-996a-3fc1a5c9f996 | -20.5821 | -55.74625 | 2024-10-06 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd442b23-8dea-3fdb-9247-550facac2996 | -1.04216 | -48.70693 | 2024-10-06 05:31:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96f6cd13-7bcd-3df2-bb76-4e28d7d0faaf | 2.17636 | -50.68902 | 2024-10-06 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49195799-2277-3c7d-b816-d7ff298cd412 | 2.17031 | -50.69002 | 2024-10-06 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d564f748-c7ac-36f7-a9f5-941b94f17002 | -7.9652 | -54.76045 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fee6915c-900c-3f82-88ca-7e9e0956b478 | -4.90448 | -65.3297 | 2024-10-06 05:33:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bc1e5a2-57d4-3f40-80fb-482b77c45a5e | -3.21922 | -48.96969 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f06dd38-5f42-354e-9a62-8cd230435340 | -8.63395 | -50.04199 | 2024-10-06 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca37414d-701b-36bd-b9ab-497af542a250 | -8.63222 | -50.04343 | 2024-10-06 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a2a412e-d18d-38a3-99e3-01568c3b6145 | -8.62666 | -50.04115 | 2024-10-06 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1e831c-69b3-3b1f-a0db-e65c4fa53594 | -3.15204 | -50.23246 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521fab75-e075-321a-9e29-06eab5b0bf81 | -3.14867 | -50.23443 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c238639e-6853-35c4-928f-fb2d49657497 | -3.14618 | -50.22546 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55d97262-9995-3184-9c73-49c56a20682e | -3.14532 | -50.23149 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbc80fef-c0f8-33d1-9fdc-f8c3855e0629 | -3.14286 | -50.22742 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d12158b5-2f99-398a-aee4-c80f40704fc0 | -3.13195 | -50.41889 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52b4d00e-9007-3e5d-962e-5bd939bffd89 | -3.13108 | -50.42493 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f091743-42f7-3b4c-ad55-4f97c04ae5b9 | -3.12736 | -50.4207 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0aef9c0a-f698-34b2-88a7-f816f665b4ad | -3.12527 | -50.41818 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ae1ddf1-8f42-3adb-8f0a-6f622ed1b200 | -3.12442 | -50.4241 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dad149ed-a197-3e72-b45c-05482bc43097 | -3.12069 | -50.41997 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69b98d1d-6563-32e9-b557-61500a680f0d | -3.1186 | -50.41742 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa395943-dd67-3e13-aac2-41e5822f3fbf | -3.11404 | -50.41902 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a3d4ff-5e89-3974-ad11-b9cf6c25743e | -3.10635 | -50.47014 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b523bae-2d5b-3832-9207-777503e328e9 | -3.1046 | -50.46771 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8027de44-44e6-333f-b882-2d72f16044a9 | -3.1006 | -50.46337 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cc465f3a-b03b-33ea-909d-c0b2cea1e6cf | -3.09973 | -50.46915 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68fd7805-3320-3927-a90e-a71773a4f4a6 | -3.09881 | -50.46095 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e75d1196-fa5a-3082-b0b4-0bb4490fe2cf | -3.09798 | -50.4667 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c7838593-6c46-3150-a09d-852c159ebf05 | -3.09397 | -50.46244 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d637e19d-37ee-3a5f-aa04-39b4d43533f6 | -3.09218 | -50.45999 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a3fd118-372c-3c2a-99d8-6715b6c79139 | -2.69605 | -49.06776 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 646111aa-e785-399f-9876-0d8bf17456fc | -2.68891 | -49.06662 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d50fea39-7947-3847-9e84-6a38783fd477 | -3.50409 | -50.26705 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 234935f3-707a-3f87-a3bf-843d29cefd13 | -3.50322 | -50.27305 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86be92b6-476c-3ad3-b39a-59bcbc79991a | -3.49648 | -50.27213 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70e0ac3e-048c-3979-9104-2c25028c92f9 | -3.42604 | -50.38131 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c770813-0512-35f8-89a9-76d235b3d30b | -3.42545 | -50.13346 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ce38bf-1dd7-3712-9220-5d07aba15a52 | -3.42522 | -50.38712 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dff83aa1-4ab5-3cb3-a4bb-c8544865620c | -3.4246 | -50.13932 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac16b647-a095-3609-abc4-b643ddd382c2 | -3.42336 | -50.38131 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3217652c-7cf7-3567-a4fe-63d5e41acda6 | -3.42249 | -50.38712 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4e333b73-2dd2-3093-94cf-a751465c5516 | -3.41937 | -50.38023 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 995e7cee-090b-3e27-8d52-486790d7f0fa | -3.41855 | -50.38604 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10e9c334-db4d-3c7d-8106-b516b18b49f5 | -3.4127 | -50.37917 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9910dd3-6f28-352c-b255-f85e3650aa1e | -3.41002 | -50.37917 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede20088-3308-37ef-b62f-3781141297a6 | -3.40918 | -50.38487 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bb674f9-28bd-39cc-ae7d-2c11a21ebc57 | -3.32081 | -49.13721 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README129.md)
